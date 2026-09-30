"""Temporary layout check of the completed new bodies while the last proof finishes."""
from pathlib import Path
import subprocess,re
root=Path(__file__).resolve().parent
pre=(root.parent/'third_growth_quantitative/complete_preamble.tex').read_text()
parts=[root/'source_operation/operation_body.tex',
       root/'stress_completion/stress_completion.tex',root/'quantitative_moments.tex',
       root/'mean_costs/mean_costs.tex']
text=pre+'\n'+r'\begin{document}'+'\n'+'\n\n'.join(p.read_text() for p in parts)+'\n'+r'\end{document}'
(root/'layout_probe.tex').write_text(text,encoding='utf-8')
for _ in range(2):
 result=subprocess.run(['pdflatex','-interaction=nonstopmode','-halt-on-error','layout_probe.tex'],
                       cwd=root,capture_output=True,text=True,encoding='utf-8',errors='replace')
 if result.returncode:raise RuntimeError(result.stdout[-10000:])
log=(root/'layout_probe.log').read_text(errors='replace')
print('\n'.join(re.findall(r'^.*(?:Overfull|Underfull|undefined|multiply defined|Warning).*$',log,re.M)) or 'No layout warnings')
