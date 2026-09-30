"""Reproduce the complete bridge readers and registered finite algebra replays."""
from pathlib import Path
import subprocess,sys,json,hashlib,re
root=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def run(args,cwd=root,output=None):
    result=subprocess.run(args,cwd=cwd,text=True,encoding='utf-8',errors='replace',capture_output=True)
    if output: (root/output).write_text(result.stdout+'\n'+result.stderr,encoding='utf-8')
    if result.returncode:
        raise RuntimeError(str(args)+'\n'+result.stdout[-6000:]+'\n'+result.stderr[-2000:])
    return result.stdout
replays=[
 ('bridge_qa/replay_axisymmetric_audit.py','bridge_qa/axisymmetric_operator_audit_receipt.json'),
 ('bridge_qa/replay_pulse_frame_audit.py','pulse_frame_audit_receipt.json'),
 ('covariance_bridge/replay_covariance.py','covariance_bridge/covariance_replay_receipt.json'),
]
checks=0
for script,receipt in replays:
    run([sys.executable,str(root/script)])
    data=json.loads((root/receipt).read_text())
    assert data['all_passed'] and all(c['passed'] for c in data['checks'])
    checks+=len(data['checks'])
run([sys.executable,str(root/'replay_signed_operator.py')])
run([sys.executable,str(root/'pulse_comparison/audit/replay_coordinates.py')])
export=root/'integration'; export.mkdir(exist_ok=True)
source_map=[
 ('axisymmetric_operator_bridge.tex','operator_body.tex'),
 ('pulse_comparison/pulse_comparison.tex','pulse_body.tex'),
 ('covariance_bridge/covariance_bridge.tex','covariance_body.tex')
]
for src,dest in source_map:
    body=(root/src).read_text(encoding='utf-8')
    if r'\begin{document}' in body:
        body=body.split(r'\maketitle',1)[1].split(r'\end{document}',1)[0]
    (export/dest).write_text(body.strip()+'\n',encoding='utf-8')
preamble=r'''\documentclass[11pt]{article}
\usepackage{amsmath,amssymb,amsthm,geometry}
\usepackage[hidelinks]{hyperref}
\geometry{margin=1in}
\newtheorem{proposition}{Proposition}
\newtheorem{remark}{Remark}
\newcommand{\R}{\mathbb R}
\newcommand{\dd}{\,\mathrm d}
\newcommand{\proj}{\operatorname{proj}}
\newcommand{\av}[1]{\left\langle #1\right\rangle}
\newcommand{\Cov}{\mathcal C}
\newcommand{\Cross}{\mathcal B}
'''
intro=r'''\title{Exact signed operator, pulse and covariance bridges}
\author{}\date{}
\begin{document}\maketitle
This reader contains the complete three finite calculations. It retains
the original coupled-stage system, both physical diffusivities, source
chart factors, signed amplitudes, and all displayed residual terms.
The companion 102-page coupled-stage reader remains the complete finite
growth/return construction.

The reference source is the preserved 165-page supplied manuscript.
A later 166-page revision was also checked on the 31 source equations
used here: (7.2)--(7.8), (7.22)--(7.42), (9.12)--(9.14).
The bounded comparison found no displayed formula change there.
This does not certify the whole manuscript or equivalence of its two versions.
The source identifiers are:
\begin{center}\footnotesize
165 pages: \texttt{8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81}\\
166 pages: \texttt{0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f}
\end{center}
Exact page maps and the unchanged raw text of pages 108--110 are
documented in \path{revision_check/REPORT.md}.
The coupled Boussinesq source is the work of Levent Alp\"oge and
Tristan Buckmaster.
\tableofcontents
\clearpage
'''
body='\n'.join([
 r'\part{Axisymmetric operators and reconstruction}\input{integration/operator_body.tex}',
 r'\clearpage\part{Coupled amplitudes and the full pulse residual}\input{integration/pulse_body.tex}',
 r'\clearpage\part{Physical curl, signed covariance and the retained remainder}\input{integration/covariance_body.tex}'
])
(root/'source_bridge_reader.tex').write_text(preamble+intro+body+'\n'+r'\end{document}'+'\n',encoding='utf-8')
(export/'source_bridge_preamble.tex').write_text(preamble,encoding='utf-8')
(export/'source_bridge_complete_body.tex').write_text(
 '\n\n'.join((export/dest).read_text() for _,dest in source_map),encoding='utf-8')
complete=(export/'source_bridge_complete_body.tex').read_text(encoding='utf-8')
label_re=re.compile(r'\\(label|ref|eqref|pageref)\{([^{}]+)\}')
prefixed=label_re.sub(lambda m:'\\'+m.group(1)+'{nsbridge:'+m.group(2)+'}',complete)
(export/'source_bridge_complete_body_prefixed.tex').write_text(prefixed,encoding='utf-8')
labels=re.findall(r'\\label\{([^{}]+)\}',prefixed)
refs=re.findall(r'\\(?:ref|eqref|pageref)\{([^{}]+)\}',prefixed)
assert len(labels)==len(set(labels)) and set(refs)<=set(labels)
run_tex=preamble+r'\begin{document}'+'\n'+prefixed+'\n'+r'\end{document}'+'\n'
(export/'source_bridge_prefixed_check.tex').write_text(run_tex,encoding='utf-8')
for i in range(2):
    run(['pdflatex','-interaction=nonstopmode','-halt-on-error','source_bridge_prefixed_check.tex'],
        cwd=export,output=Path('integration')/f'prefix_check_pass{i+1}.txt')
prefix_log=(export/'source_bridge_prefixed_check.log').read_text(errors='replace')
assert not re.search(r'undefined|multiply defined',prefix_log)
readers=[
 Path('axisymmetric_operator_bridge_reader.tex'),
 Path('pulse_comparison/pulse_comparison.tex'),
 Path('covariance_bridge/covariance_bridge.tex'),
 Path('source_bridge_reader.tex')]
for rel in readers:
    target=root/rel
    for i in range(3 if rel.name=='source_bridge_reader.tex' else 2):
        out=run(['pdflatex','-interaction=nonstopmode','-halt-on-error',target.name],
                cwd=target.parent,output=Path(str(rel.with_suffix(''))+f'.pass{i+1}.txt'))
    log=target.with_suffix('.log').read_text(errors='replace')
    warnings=re.findall(r'^.*(?:Overfull|Underfull|undefined|multiply defined|LaTeX Warning).*$',
                        log,flags=re.M)
    if warnings: raise RuntimeError(str(rel)+'\n'+'\n'.join(warnings))
outputs={str(rel.with_suffix('.pdf')):sha((root/rel).with_suffix('.pdf')) for rel in readers}
sources={str(p.relative_to(root)):sha(p) for p in [
 *[root/src for src,_ in source_map],
 *[root/script for script,_ in replays],
 root/'build_bridge.py',root/'source_bridge_reader.tex',
 *export.glob('*.tex')]}
receipt=dict(schema='source-bridge-build-v3',registered_checks=checks,prefixed_labels=len(labels),
 all_passed=True,readers=outputs,sources=sources,
 visual_review='Required separately; compilation does not assert inspection.',
 source_versions=json.loads((root/'revision_check/receipt.json').read_text()))
(root/'build_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(all_passed=True,registered_checks=checks,readers=outputs)))
