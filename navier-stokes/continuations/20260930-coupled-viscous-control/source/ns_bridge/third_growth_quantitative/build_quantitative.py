"""Build complete prior bridge plus original third-growth quantitative proofs."""
from pathlib import Path
import hashlib,json,re,subprocess,sys
import fitz
from PIL import Image,ImageDraw
root=Path(__file__).resolve().parent
bridge=root.parent
prior=bridge/'actual_result_propagation'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args):
 r=subprocess.run(args,cwd=root,capture_output=True,text=True,encoding='utf-8',errors='replace')
 if r.returncode:raise RuntimeError(str(args)+'\n'+r.stdout[-10000:]+'\n'+r.stderr[-3000:])
 return r
old=json.loads((prior/'build_receipt.json').read_text())
oldvisual=json.loads((prior/'qa/visual_review.json').read_text())
assert old['all_passed'] and old['total_registered_checks']==108
assert oldvisual['all_pages_personally_inspected']
assert sha(prior/'current_bridge_reader.pdf')==old['pdf_sha256']==oldvisual['pdf_sha256']
assert sha(prior/'complete_body.tex')==old['body_sha256']
for name,h in old['source_hashes'].items():assert sha(bridge/name)==h,name
replays=[
 ('derivative_costs/replay_derivative_costs.py','derivative_costs/replay_receipt.json',55,'result'),
 ('frame_audit/replay_frame.py','frame_audit/replay_receipt.json',40,'passed'),
 ('replay_quantitative.py','quantitative_replay_receipt.json',25,'passed')]
new=[]
for script,receipt,expected,key in replays:
 run([sys.executable,str(root/script)])
 data=json.loads((root/receipt).read_text())
 assert len(data['checks'])==expected
 assert all(c[key]==('pass' if key=='result' else True) for c in data['checks'])
 new.append(dict(script=script,receipt=receipt,check_count=expected,
                 script_sha256=sha(root/script),receipt_sha256=sha(root/receipt)))
bodies=[prior/'complete_body.tex',root/'derivative_costs/derivative_costs.tex',
        root/'frame_audit/frame_body.tex',root/'quantitative_body.tex']
content=[p.read_text(encoding='utf-8') for p in bodies]
complete='\n\n'.join(content)
labels=re.findall(r'\\label\{([^{}]+)\}',complete)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^{}]+)\}',complete)
assert len(labels)==len(set(labels)),'duplicate labels'
assert set(refs)<=set(labels),set(refs)-set(labels)
preamble=(prior/'complete_preamble.tex').read_text(encoding='utf-8')
preamble+=r'\newtheorem{theorem}{Theorem}'+'\n'
(root/'complete_body.tex').write_text(complete,encoding='utf-8')
(root/'complete_preamble.tex').write_text(preamble,encoding='utf-8')
intro=r'''\title{Navier--Stokes source propagation and the finite coupled bridge\\
Original third-growth scales, exact pulse map, and complete residual}
\author{}\date{}
\begin{document}\maketitle
This reader contains the complete preceding operator, pulse, covariance,
source-transport and radial-moment proofs. The new parts retain the
original third-growth seed and evolving parent, prove all amplitude
derivative costs, identify the exact source clock and tangent frame,
construct an invertible map to the actual source homogeneous pulse,
and calculate the entire compact curl candidate and its force increment.

The released source theorem is attributed to the supplied manuscript;
this lane has not independently certified its whole proof. Its positive
swirl path and the exact negative reflected path retain their respective
forces. The distinct finite coupled candidate has the explicit residual
proved here. The companion 102-page reader contains its preceding
original-stage proofs. No infinite modified coupled construction or
uniform terminal force estimate is asserted by the finite pulse map.
\tableofcontents\clearpage
'''
parts=[r'\part{Complete preceding bridge and actual source propagation}',content[0],
 r'\clearpage\part{Original third-growth derivatives}',content[1],
 r'\clearpage\part{Exact clock, signed frame, and actual source pulse}',content[2],
 r'\clearpage\part{Complete physical curl, moments, and force costs}',content[3]]
tex=preamble+intro+'\n'.join(parts)+'\n'+r'\end{document}'+'\n'
(root/'current_bridge_reader.tex').write_text(tex,encoding='utf-8')
for j in range(3):
 r=run(['pdflatex','-interaction=nonstopmode','-halt-on-error','current_bridge_reader.tex'])
 (root/f'build_pass_{j+1}.txt').write_text(r.stdout+r.stderr,encoding='utf-8')
log=(root/'current_bridge_reader.log').read_text(errors='replace')
warnings=re.findall(r'^.*(?:Overfull|Underfull|undefined|multiply defined|Warning).*$',log,re.M)
assert not warnings,warnings
pdf=root/'current_bridge_reader.pdf'
doc=fitz.open(pdf)
outside=[]
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
  draw.text((x0,12),f'Complete source bridge and third-growth costs / page {k+n+1}',fill='black')
  sheet.paste(im,(x0,40));x0+=im.width+30
 path=qa/f'contact-{k//2+1:02}.png';sheet.save(path);contacts.append(str(path))
receipt=dict(schema='third-growth-quantitative-cumulative-v1',all_passed=True,
 prior_registered_checks=108,new_registered_checks=sum(x['check_count'] for x in new),
 total_registered_checks=108+sum(x['check_count'] for x in new),new_replays=new,
 prefixed_labels=len(labels),pages=len(doc),warnings=warnings,out_of_page_text=outside,
 pdf_sha256=sha(pdf),body_sha256=sha(root/'complete_body.tex'),
 source_hashes={str(p.relative_to(bridge)):sha(p) for p in [
  *bodies,root/'build_quantitative.py',root/'current_bridge_reader.tex',root/'complete_preamble.tex']},
 prior_pdf_sha256=sha(prior/'current_bridge_reader.pdf'),
 prior_build_receipt_sha256=sha(prior/'build_receipt.json'),
 source_pdf_sha256=sha(bridge/'openai_navier_stokes_166p.pdf'),
 contacts=contacts,rendered_pages={p.name:sha(p) for p in pages},
 visual_review='Not asserted by build; actual inspection must be recorded separately.')
(root/'build_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['all_passed','pages','total_registered_checks',
 'new_registered_checks','prefixed_labels','pdf_sha256','body_sha256']},indent=2))
