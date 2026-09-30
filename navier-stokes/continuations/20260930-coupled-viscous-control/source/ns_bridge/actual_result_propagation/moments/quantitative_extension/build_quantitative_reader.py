from pathlib import Path
import hashlib,json,re,subprocess
import fitz
root=Path(__file__).resolve().parent; mom=root.parent; actual=mom.parent
old=json.loads((actual/'build_receipt.json').read_text()); assert old['all_passed'] and old['total_registered_checks']==108
qd=json.loads((root/'replay_receipt.json').read_text()); assert qd['all_passed'] and all(c['passed'] for c in qd['checks'])
base=(actual/'complete_body.tex').read_text(encoding='utf-8'); ext=(root/'quantitative_extension.tex').read_text(encoding='utf-8'); pre=(actual/'complete_preamble.tex').read_text(encoding='utf-8')
labels=re.findall(r'\\label\{([^{}]+)\}',base+'\n'+ext); refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^{}]+)\}',base+'\n'+ext); assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
intro=r'''\title{Actual coupled Navier--Stokes moments and quantitative source-chart orders\\
Retained third seed, old-wave interactions, and physical viscosity}
\author{}\date{}
\begin{document}\maketitle
This reader preserves the complete released-result propagation and actual
compact-curl moment calculation. It adds exact finite source-chart orders
for the retained third-growth seed and coefficient path. The source clock
$\nu=\sqrt{A_0}$ remains distinct from physical viscosity $\nu_{\rm NS}$;
all original parameters and signs are retained. The orders are finite-chart
identities with finite path constants, not uniform endpoint or infinite-cycle
estimates.
\tableofcontents\clearpage
'''
tex=pre+intro+r'\part{The actual released result, propagation, and radial moments}'+"\n"+base+r'\clearpage\part{Quantitative source-chart orders for the retained third seed}'+"\n"+ext+'\n\\end{document}\n'
(root/'current_quantitative_reader.tex').write_text(tex,encoding='utf-8')
def run(a):
 p=subprocess.run(a,cwd=root,capture_output=True,text=True,encoding='utf-8',errors='replace')
 if p.returncode: raise RuntimeError(p.stdout[-10000:]+p.stderr[-3000:])
 return p
for j in range(3): (root/f'build_pass_{j+1}.txt').write_text(run(['pdflatex','-interaction=nonstopmode','-halt-on-error','current_quantitative_reader.tex']).stdout,encoding='utf-8')
log=(root/'current_quantitative_reader.log').read_text(errors='replace'); warnings=[x for x in log.splitlines() if re.search(r'Overfull|Underfull|undefined|multiply defined|Warning',x)]; assert not warnings,warnings[:10]
pdf=root/'current_quantitative_reader.pdf'; doc=fitz.open(pdf); out=[]
for i,p in enumerate(doc,1):
 for b in p.get_text('dict')['blocks']:
  for line in b.get('lines',[]):
   for sp in line['spans']:
    x0,y0,x1,y1=sp['bbox']
    if x0<0 or y0<0 or x1>p.rect.width+.01 or y1>p.rect.height+.01: out.append((i,sp['text']))
assert not out,out
rec={'schema':'actual-moments-quantitative-cumulative-v1','all_passed':True,'prior_registered_checks':108,'new_registered_checks':qd['check_count'],'total_registered_checks':108+qd['check_count'],'pages':len(doc),'labels':len(labels),'warnings':warnings,'out_of_page_text':out,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'tex_sha256':hashlib.sha256((root/'current_quantitative_reader.tex').read_bytes()).hexdigest(),'quantitative_body_sha256':hashlib.sha256((root/'quantitative_extension.tex').read_bytes()).hexdigest(),'quantitative_replay_sha256':hashlib.sha256((root/'replay_quantitative_extension.py').read_bytes()).hexdigest(),'prior_pdf_sha256':old['pdf_sha256'],'scope':'Finite exact source-chart orders on retained third seed and coefficient path; old-parent orders remain explicit; no endpoint or infinite estimate; physical viscosity retained.'}
(root/'build_receipt.json').write_text(json.dumps(rec,indent=2)+'\n'); print(json.dumps(rec,indent=2))
