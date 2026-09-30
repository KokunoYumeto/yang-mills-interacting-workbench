from pathlib import Path
import hashlib,json,re,subprocess,sys
import fitz
root=Path(__file__).resolve().parent
mc=root.parent
prior_receipt=json.loads((mc/'build_receipt.json').read_text())
assert prior_receipt['all_passed'] and prior_receipt['total_registered_checks']==568
# replay is stdlib and must pass every registered check
subprocess.run([sys.executable,str(root/'replay_class_propagation.py')],cwd=root,check=True)
rp=json.loads((root/'replay_receipt.json').read_text()); assert rp['all_passed'] and all(c['passed'] for c in rp['checks'])
body=(mc/'complete_body.tex').read_text(encoding='utf-8')+'\n\n'+(root/'class_propagation.tex').read_text(encoding='utf-8')
labels=re.findall(r'\\label\{([^{}]+)\}',body); refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^{}]+)\}',body)
assert len(labels)==len(set(labels)), 'duplicate labels'
assert set(refs)<=set(labels), sorted(set(refs)-set(labels))
preamble=(mc/'complete_preamble.tex').read_text(encoding='utf-8')
intro=r'''\title{Navier--Stokes source propagation: finite source classes and signed branches\\
Actual coupled class bounds, full force costs, and finite-band limitations}
\author{}\date{}
\begin{document}\maketitle
This reader extends the verified pressure, stress, moment, and mean-cost bridge
with an exact finite-band propagation statement for the source classes
$M^\alpha$, $S^\alpha$, and $W^\alpha$. It preserves the original chart
powers, phase arithmetic, inverse matrices, pressure cutoff tail, old locally
finite family, all nonlinear cross terms, and the physical viscosity
$\nu_{\rm NS}$. The source theorem remains attributed input; the class
conclusion is finite and compact-support only and does not certify a uniform
infinite modified sequence. Absolute-value class estimates are unchanged by
sign reversal, while the reflected force and vorticity keep their actual signs.
\tableofcontents\clearpage
'''
tex=preamble+intro+'\part{Verified preceding bridge}\n'+body.replace('\\section{Finite propagation of the actual coupled source classes}','\\clearpage\\part{Finite propagation of the actual coupled source classes}\n\\section{Finite propagation of the actual coupled source classes}',1)+'\n\\end{document}\n'
(root/'current_class_reader.tex').write_text(tex,encoding='utf-8')
def run(a):
 p=subprocess.run(a,cwd=root,capture_output=True,text=True,encoding='utf-8',errors='replace')
 if p.returncode: raise RuntimeError(p.stdout[-10000:]+p.stderr[-2000:])
 return p
for j in range(3): (root/f'build_pass_{j+1}.txt').write_text((run(['pdflatex','-interaction=nonstopmode','-halt-on-error','current_class_reader.tex']).stdout),encoding='utf-8')
log=(root/'current_class_reader.log').read_text(errors='replace')
issues=[x for x in log.splitlines() if re.search(r'Overfull|Underfull|undefined|multiply defined|Warning',x)]
assert not issues, issues[:20]
pdf=root/'current_class_reader.pdf'; doc=fitz.open(pdf)
out=[]
for i,p in enumerate(doc,1):
 for b in p.get_text('dict')['blocks']:
  for line in b.get('lines',[]):
   for sp in line['spans']:
    x0,y0,x1,y1=sp['bbox']
    if x0<0 or y0<0 or x1>p.rect.width+.01 or y1>p.rect.height+.01: out.append((i,sp['text']))
assert not out,out
receipt={'schema':'actual-source-class-cumulative-v1','all_passed':True,'prior_registered_checks':568,'new_registered_checks':rp['check_count'],'total_registered_checks':568+rp['check_count'],'new_replay_receipt_sha256':hashlib.sha256((root/'replay_receipt.json').read_bytes()).hexdigest(),'pages':len(doc),'label_count':len(labels),'warnings':issues,'out_of_page_text':out,'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),'tex_sha256':hashlib.sha256((root/'current_class_reader.tex').read_bytes()).hexdigest(),'class_body_sha256':hashlib.sha256((root/'class_propagation.tex').read_bytes()).hexdigest(),'prior_pdf_sha256':prior_receipt['pdf_sha256'],'scope':'finite fixed band, finite labels, compact support; no uniform infinite gain'}
(root/'build_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))

