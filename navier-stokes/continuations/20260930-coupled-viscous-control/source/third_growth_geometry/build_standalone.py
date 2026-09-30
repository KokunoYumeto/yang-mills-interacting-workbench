"""Compile a local section preview without writing in the parent directory."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import fitz

HERE=Path(__file__).resolve().parent
source=HERE.parent/'coupled_viscous_control.aux'
lines=source.read_text(encoding='utf-8').splitlines()
labels=[line for line in lines if line.startswith('\\newlabel{')]
(HERE/'prior_labels.aux').write_text('\n'.join(labels)+'\n',encoding='utf-8')
passes=[]
for run in range(1,4):
    proc=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error',
                         'standalone.tex'],cwd=HERE,capture_output=True,text=True)
    (HERE/f'build-pass-{run}.txt').write_text(proc.stdout+proc.stderr,encoding='utf-8')
    passes.append({'run':run,'exit_code':proc.returncode})
    if proc.returncode:
        raise RuntimeError(f'LaTeX pass {run} failed: {proc.stdout[-3000:]}')
pdf=HERE/'standalone.pdf'
log=(HERE/'standalone.log').read_text(encoding='utf-8')
issues=[line for line in log.splitlines() if re.search(r'Warning|Overfull|Underfull|^!',line)]
doc=fitz.open(pdf)
record={'scope':'Local section preview; cumulative integration and its visual QA remain separate.',
        'passes':passes,'pages':len(doc),'latex_issues':issues,
        'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'body_sha256':hashlib.sha256((HERE/'third_growth_geometry_body.tex').read_bytes()).hexdigest(),
        'prior_aux_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'visual_review':'pending'}
(HERE/'build_receipt.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
