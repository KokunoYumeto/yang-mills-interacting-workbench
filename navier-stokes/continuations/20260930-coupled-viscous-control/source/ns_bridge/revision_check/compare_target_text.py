from pathlib import Path
import difflib
import json
import re

HERE=Path(__file__).resolve().parent
pages={key:(HERE/f'{key}_poppler_layout.txt').read_text(encoding='utf-8').split('\f') for key in ['old_165p','new_166p']}
spans={'pulse_equations':(74,87),'stress_selection_equations':(108,110),'intro_operator_citations':(7,15),'profile_stress_citations':(24,27),'section9_opening_citations':(101,103)}
for name,(first,last) in spans.items():
    chunks={key:'\f'.join(value[first-1:last]) for key,value in pages.items()}
    for key,value in chunks.items():
        (HERE/f'{key}_{name}_pages_{first}_{last}.txt').write_text(value,encoding='utf-8',newline='')
    delta=''.join(difflib.unified_diff(chunks['old_165p'].splitlines(keepends=True),chunks['new_166p'].splitlines(keepends=True),fromfile=f'old_165p:{first}-{last}',tofile=f'new_166p:{first}-{last}',n=3))
    (HERE/f'{name}_unnormalized.diff').write_text(delta,encoding='utf-8',newline='')
    print(name,'diff characters',len(delta))

