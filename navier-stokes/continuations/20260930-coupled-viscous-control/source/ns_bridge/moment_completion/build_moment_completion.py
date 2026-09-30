"""Build the unabridged source bridge with actual pressure/moment completion."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import fitz
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent
bridge=root.parent;prior=bridge/'third_growth_quantitative'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args):
 r=subprocess.run(args,cwd=root,capture_output=True,text=True,encoding='utf-8',errors='replace')
 if r.returncode:raise RuntimeError(str(args)+'\n'+r.stdout[-12000:]+'\n'+r.stderr[-2000:])
 return r
old=json.loads((prior/'build_receipt.json').read_text())
ov=json.loads((prior/'qa/visual_review.json').read_text())
assert old['all_passed'] and old['total_registered_checks']==228
assert ov['all_pages_personally_inspected']
assert old['pdf_sha256']==ov['pdf_sha256']==sha(prior/'current_bridge_reader.pdf')
assert old['body_sha256']==sha(prior/'complete_body.tex')
for name,h in old['source_hashes'].items():assert sha(bridge/name)==h,name
registry=[
 ('source_operation/replay_operation.py','source_operation/replay_receipt.json'),
 ('stress_completion/replay_stress_completion.py','stress_completion/replay_receipt.json'),
 ('replay_quantitative_moments.py','quantitative_replay_receipt.json'),
 ('mean_costs/replay_mean_costs.py','mean_costs/replay_receipt.json')]
new=[]
for script,receipt in registry:
 run([sys.executable,str(root/script)])
 data=json.loads((root/receipt).read_text())
 checks=data['checks']
 assert checks and len(checks)==data['check_count']
 assert len({c['name'] for c in checks})==len(checks),'duplicate replay names'
 assert all(c['passed'] is True for c in checks)
 new.append(dict(script=script,receipt=receipt,check_count=len(checks),
                 script_sha256=sha(root/script),receipt_sha256=sha(root/receipt)))
bodies=[prior/'complete_body.tex',root/'source_operation/operation_body.tex',
 root/'stress_completion/stress_completion.tex',root/'quantitative_moments.tex',
 root/'mean_costs/mean_costs.tex']
content=[p.read_text(encoding='utf-8') for p in bodies]
complete='\n\n'.join(content)
labels=re.findall(r'\\label\{([^{}]+)\}',complete)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^{}]+)\}',complete)
assert len(labels)==len(set(labels)),'duplicate labels'
assert set(refs)<=set(labels),set(refs)-set(labels)
preamble=(prior/'complete_preamble.tex').read_text(encoding='utf-8')
(root/'complete_body.tex').write_text(complete,encoding='utf-8')
(root/'complete_preamble.tex').write_text(preamble,encoding='utf-8')
intro=r'''\title{Navier--Stokes source propagation and the finite coupled bridge\\
Actual pressure defects, complete stress, and mean velocity correction}
\author{}\date{}
\begin{document}\maketitle
This cumulative reader preserves the complete preceding bridge and
third-growth derivative, pulse-map and physical-residual proofs.
The new parts compute the actual pressure-induced compatibility defects,
the source's five-row mean velocity correction and its remaining nonlinear
terms, a compact symmetric-stress representation of the full averaged
force, and the original-scale derivative costs of these operations.

The supplied source theorem remains attributed source input. This lane
has not independently certified its entire proof. Its original positive
swirl and exact negative reflection retain their corresponding forces.
The distinct coupled candidate keeps every calculated residual; a finite
stress representation is not asserted to be an added velocity or a
completed infinite correction sequence. The companion 102-page reader
contains the original finite coupled-stage proofs.
\tableofcontents\clearpage
'''
titles=[
 r'\part{Complete preceding source bridge and original third-growth costs}',
 r'\clearpage\part{The actual source pressure and five-row correction}',
 r'\clearpage\part{Compact completion of the full averaged force}',
 r'\clearpage\part{All-order actual moment and moving-scale costs}',
 r'\clearpage\part{Physical mean velocity and derivative costs}']
parts=[]
for title,body in zip(titles,content):parts.extend([title,body])
tex=preamble+intro+'\n'.join(parts)+'\n'+r'\end{document}'+'\n'
(root/'current_bridge_reader.tex').write_text(tex,encoding='utf-8')
for j in range(3):
 r=run(['pdflatex','-interaction=nonstopmode','-halt-on-error','current_bridge_reader.tex'])
 (root/f'build_pass_{j+1}.txt').write_text(r.stdout+r.stderr,encoding='utf-8')
log=(root/'current_bridge_reader.log').read_text(errors='replace')
warnings=re.findall(r'^.*(?:Overfull|Underfull|undefined|multiply defined|Warning).*$',log,re.M)
assert not warnings,warnings
pdf=root/'current_bridge_reader.pdf';doc=fitz.open(pdf);outside=[]
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
  draw.text((x0,12),f'Complete source bridge and moment correction / page {k+n+1}',fill='black')
  sheet.paste(im,(x0,40));x0+=im.width+30
 path=qa/f'contact-{k//2+1:02}.png';sheet.save(path);contacts.append(str(path))
receipt=dict(schema='actual-moment-completion-cumulative-v1',all_passed=True,
 prior_registered_checks=228,new_registered_checks=sum(x['check_count'] for x in new),
 total_registered_checks=228+sum(x['check_count'] for x in new),new_replays=new,
 pages=len(doc),prefixed_labels=len(labels),warnings=warnings,out_of_page_text=outside,
 pdf_sha256=sha(pdf),body_sha256=sha(root/'complete_body.tex'),
 source_hashes={str(p.relative_to(bridge)):sha(p) for p in [
  *bodies,root/'build_moment_completion.py',root/'current_bridge_reader.tex',root/'complete_preamble.tex']},
 prior_pdf_sha256=sha(prior/'current_bridge_reader.pdf'),
 prior_build_receipt_sha256=sha(prior/'build_receipt.json'),
 source_pdf_sha256=sha(bridge/'openai_navier_stokes_166p.pdf'),
 contacts=contacts,rendered_pages={p.name:sha(p) for p in pages},
 visual_review='Not inferred by the build. Record actual page inspection separately.')
(root/'build_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['all_passed','pages','new_registered_checks',
 'total_registered_checks','prefixed_labels','pdf_sha256','body_sha256']},indent=2))
