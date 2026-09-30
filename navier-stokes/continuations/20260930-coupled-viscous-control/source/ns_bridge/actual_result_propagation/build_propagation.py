"""Build the unabridged current bridge and its exact propagation/moment proofs."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import fitz
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent
bridge=root.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args,cwd=root):
 r=subprocess.run(args,cwd=cwd,capture_output=True,text=True,encoding='utf-8',errors='replace')
 if r.returncode:raise RuntimeError(str(args)+'\n'+r.stdout[-7000:]+'\n'+r.stderr[-3000:])
 return r
old=json.loads((bridge/'build_receipt.json').read_text())
assert old['all_passed']
for name,h in old['sources'].items():assert sha(bridge/name)==h,name
assert sha(bridge/'source_bridge_reader.pdf')==old['readers']['source_bridge_reader.pdf']
assert old['registered_checks']==46
new_replays=[('replay_propagation.py','propagation_replay_receipt.json'),
 ('moments/replay_moments.py','moments/moments_replay_receipt.json')]
count=0;replay_data=[]
for script,receipt in new_replays:
 run([sys.executable,str(root/script)])
 data=json.loads((root/receipt).read_text())
 assert data['all_passed'] and all(c['passed'] for c in data['checks'])
 count+=len(data['checks']);replay_data.append(data)
bodies=[bridge/'integration/source_bridge_complete_body_prefixed.tex',
 root/'propagation_body.tex',root/'moments/moments_body.tex']
preamble=(bridge/'integration/source_bridge_preamble.tex').read_text()
preamble+=r'\usepackage{mathrsfs}'+'\n'
def rendered_body(p):
 text=p.read_text(encoding='utf-8')
 for before,after in [
  (r'{I\choose J}',r'\binom{I}{J}'),
  (r'{j\choose i}',r'\binom{j}{i}'),
  (r'{I+(1,0)\choose K}',r'\binom{I+(1,0)}{K}')]:
  text=text.replace(before,after)
 return text
complete='\n\n'.join(rendered_body(p) for p in bodies)
labels=re.findall(r'\\label\{([^{}]+)\}',complete)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^{}]+)\}',complete)
assert len(labels)==len(set(labels)), 'duplicate labels'
assert set(refs)<=set(labels),set(refs)-set(labels)
(root/'complete_body.tex').write_text(complete,encoding='utf-8')
(root/'complete_preamble.tex').write_text(preamble,encoding='utf-8')
intro=r'''\title{Navier--Stokes source result, exact propagation\\
and the complete finite coupled bridge}
\author{}\date{}
\begin{document}\maketitle
This cumulative reader preserves the complete operator, moving-frame,
physical-curl and signed-covariance calculations of the prior bridge.
It adds the precise released theorem as source input, proves its exact
orientation and retained-viscosity transports, and computes the two
radial residual moments of the actual finite coupled candidate.

The source-selected positive swirl and its proved reflected negative
counterpart are both retained with their corresponding forces.
The source's complete infinite construction is attributed to that
manuscript; the distinct coupled candidate retains its explicit remainder.
The companion 102-page reader contains the finite original-stage proofs.

\tableofcontents\clearpage
'''
parts=[
 r'\part{Complete finite operator, pulse and covariance bridge}',
 rendered_body(bodies[0]),
 r'\clearpage\part{The released result and exact propagation}',
 rendered_body(bodies[1]),
 r'\clearpage\part{The actual coupled candidate radial moments}',
 rendered_body(bodies[2])]
tex=preamble+intro+'\n'.join(parts)+'\n'+r'\end{document}'+'\n'
(root/'current_bridge_reader.tex').write_text(tex,encoding='utf-8')
for j in range(3):
 r=run(['pdflatex','-interaction=nonstopmode','-halt-on-error','current_bridge_reader.tex'])
 (root/f'build_pass_{j+1}.txt').write_text(r.stdout+r.stderr)
log=(root/'current_bridge_reader.log').read_text(errors='replace')
warnings=re.findall(r'^.*(?:Overfull|Underfull|undefined|multiply defined|Warning).*$',log,re.M)
assert not warnings,warnings
pdf=root/'current_bridge_reader.pdf'
doc=fitz.open(pdf);outside=[]
for j,page in enumerate(doc):
 for block in page.get_text('dict')['blocks']:
  for line in block.get('lines',[]):
   for sp in line['spans']:
    x0,y0,x1,y1=sp['bbox']
    if x0<0 or y0<0 or x1>page.rect.width+.01 or y1>page.rect.height+.01:
     outside.append(dict(page=j+1,text=sp['text']))
assert not outside,outside
qa=root/'qa';qa.mkdir(exist_ok=True)
run(['pdftoppm','-png','-r','100',str(pdf),str(qa/'page')])
pages=[qa/f'page-{j:0{len(str(len(doc)))}d}.png' for j in range(1,len(doc)+1)]
assert all(p.exists() for p in pages)
contacts=[]
for k in range(0,len(pages),2):
 ims=[Image.open(p).convert('RGB') for p in pages[k:k+2]]
 sheet=Image.new('RGB',(sum(im.width for im in ims)+30*(len(ims)+1),max(im.height for im in ims)+70),'#ddd')
 draw=ImageDraw.Draw(sheet);x0=30
 for n,im in enumerate(ims):
  draw.text((x0,12),f'Current complete bridge / page {k+n+1}',fill='black')
  sheet.paste(im,(x0,40));x0+=im.width+30
 path=qa/f'contact-{k//2+1:02}.png';sheet.save(path);contacts.append(str(path))
receipt=dict(schema='source-propagation-cumulative-v1',all_passed=True,
 old_registered_checks=46,new_registered_checks=count,total_registered_checks=46+count,
 new_replays=replay_data,prefixed_labels=len(labels),pages=len(doc),warnings=warnings,
 pdf_sha256=sha(pdf),body_sha256=sha(root/'complete_body.tex'),
 source_hashes={str(p.relative_to(bridge)):sha(p) for p in [
  *bodies,root/'build_propagation.py',root/'current_bridge_reader.tex',root/'complete_preamble.tex']},
 source_pdf_sha256=sha(bridge/'openai_navier_stokes_166p.pdf'),
 prior_bridge_pdf_sha256=sha(bridge/'source_bridge_reader.pdf'),
 typesetting_only_conversion='Three explicit primitive choose forms rendered with amsmath binom; mathematical operands unchanged.',
 contacts=contacts,rendered_pages={p.name:sha(p) for p in pages},
 visual_review='Not asserted by this build. Record actual inspection separately.')
(root/'build_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['all_passed','pages','total_registered_checks',
 'new_registered_checks','prefixed_labels','pdf_sha256','body_sha256','contacts']},indent=2))
