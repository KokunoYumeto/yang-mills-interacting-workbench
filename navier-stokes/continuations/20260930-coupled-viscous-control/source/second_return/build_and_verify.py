"""Build the paired actual-entry/second-return reader and render every page.

Only the two references to the completed earlier reader are imported;
new labels can therefore never be silently read from a stale parent aux.
This script does not declare that a human/assistant visual review occurred.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys
import fitz
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
QA = HERE/'qa'
QA.mkdir(exist_ok=True)
sha = lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
ops = []
def run(args, filename):
    proc = subprocess.run(args,cwd=HERE,capture_output=True,text=True,
                          encoding='utf-8',errors='replace')
    (QA/filename).write_text(proc.stdout+proc.stderr,encoding='utf-8')
    ops.append(dict(command=args,exit_code=proc.returncode,log='qa/'+filename))
    if proc.returncode:
        raise RuntimeError('Command failed; inspect '+str(QA/filename))

run([sys.executable,str(HERE/'replay_second_return.py')],'replay.log')
aux = (HERE.parent/'coupled_viscous_control.aux').read_text(encoding='utf-8')
labels = ['sec:cv-diffusive-parent','sec:cv-first-stage']
imports = []
for label in labels:
    matches=[line for line in aux.splitlines() if line.startswith('\\newlabel{'+label+'}')]
    if len(matches)!=1:
        raise RuntimeError('Missing or ambiguous earlier-reader reference: '+label)
    imports += matches
(HERE/'earlier_sections.aux').write_text('\\relax\n'+'\n'.join(imports)+'\n',encoding='utf-8')
latex = shutil.which('pdflatex')
poppler = shutil.which('pdftoppm')
if not latex or not poppler:
    raise RuntimeError('pdflatex and Poppler pdftoppm are required.')
for i in range(3):
    run([latex,'-interaction=nonstopmode','-halt-on-error','second_return.tex'],
        f'latex-pass-{i+1}.log')
log=(HERE/'second_return.log').read_text(encoding='utf-8',errors='replace')
diagnostics=[line for line in log.splitlines()
             if re.search(r'Warning|Overfull|Underfull|undefined|multiply defined',line)]
if diagnostics:
    raise RuntimeError('Final LaTeX diagnostics: '+repr(diagnostics))
pdf=HERE/'second_return.pdf'
run([poppler,'-r','90','-png',str(pdf),str(QA/'page')],'render.log')
doc=fitz.open(pdf)
pages=[]
outside=[]
for i,page in enumerate(doc):
    for block in page.get_text('blocks'):
        if block[0]<0 or block[1]<0 or block[2]>page.rect.width or block[3]>page.rect.height:
            outside.append(dict(page=i+1,bbox=list(block[:4])))
    path=QA/f'page-{i+1:0{len(str(len(doc)))}}.png'
    if not path.exists():
        raise RuntimeError('Missing rendered page '+str(path))
    pages.append(path)
if outside:
    raise RuntimeError('Text outside PDF page: '+repr(outside))
contacts=[]
for group in range((len(pages)+3)//4):
    subset=pages[group*4:group*4+4]
    canvas=Image.new('RGB',(1500,2200),'#d7d7d7')
    draw=ImageDraw.Draw(canvas)
    for j,path in enumerate(subset):
        im=Image.open(path).convert('RGB')
        im.thumbnail((730,1050))
        x=(j%2)*750+(750-im.width)//2
        y=(j//2)*1100+28
        canvas.paste(im,(x,y))
        draw.text((x,y-20),f'Page {group*4+j+1}',fill='black')
    out=QA/f'contact-{group+1}.png'
    canvas.save(out)
    contacts.append(out)
receipt=dict(schema='paired-entry-second-return-build-v1',all_passed=True,
    operations=ops,page_count=len(doc),pdf='second_return.pdf',pdf_sha256=sha(pdf),
    body_sha256=sha(HERE/'second_return_body.tex'),
    entry_sha256=sha(HERE.parent/'finite_stage'/'actual_viscous_entry.tex'),
    replay_receipt_sha256=sha(HERE/'replay_receipt.json'),
    exact_check_count=len(json.loads((HERE/'replay_receipt.json').read_text())['checks']),
    earlier_reference_imports=imports,latex_diagnostics=diagnostics,
    out_of_page_text_blocks=outside,all_pages_rendered=True,
    visual_review_status='pending',
    rendered_page_sha256={p.relative_to(HERE).as_posix():sha(p) for p in pages},
    contact_sheets=[p.relative_to(HERE).as_posix() for p in contacts],
    lean_used=False,infinite_modified_viscous_sequence_proved=False)
(HERE/'build_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(all_passed=True,pages=len(doc),checks=receipt['exact_check_count'],
                     pdf_sha256=sha(pdf),visual_review_status='pending')))
