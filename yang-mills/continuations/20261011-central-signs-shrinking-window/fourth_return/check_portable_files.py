from pathlib import Path
from datetime import datetime,timezone
import json,re,hashlib
ROOT=Path(__file__).resolve().parent
manifest=json.loads((ROOT/'PORTABLE_REPLAY.json').read_text())
for extra in ['PORTABLE_REPLAY.json','REPLAY_RESULT.json','PORTABILITY_CHECKS.json','check_portable_files.py']:
    if extra not in manifest['files']:manifest['files'].append(extra)
(ROOT/'PORTABLE_REPLAY.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8',newline='\n')
missing=[];private=[]
pattern=re.compile(r'[A-Za-z]:[\\/](?:Users|user|Documents|work|tmp)|corpus[\\/]web-consolidation')
for name in manifest['files']:
    if name=='PORTABILITY_CHECKS.json':continue
    p=ROOT/name
    if not p.is_file():missing.append(name);continue
    text=p.read_text(encoding='utf-8')
    if pattern.search(text):private.append(name)
proof=(ROOT/'FOURTH_SCHUR_COEFFICIENT.md').read_text(encoding='utf-8')
targets=[s for s in re.findall(r'\]\(([^)]+)\)',proof) if not s.startswith('http') and '.md' in s]
missing_links=[s for s in targets if not (ROOT/s.split('#',1)[0]).is_file()]
tags=re.findall(r'\\tag\{Q(\d+)\}',proof)
assert not missing and not private and not missing_links
assert len(tags)==50 and set(tags)==set(map(str,range(1,51)))
assert proof.count(r'\[')==proof.count(r'\]') and proof.count(r'\(')==proof.count(r'\)')
receipt={'completed_utc':datetime.now(timezone.utc).isoformat(),'missing_dependencies':missing,'private_filesystem_paths_in_replay_files':private,'missing_relative_proof_links':missing_links,'distinct_equation_tags_Q1_to_Q50':True,'display_and_inline_math_delimiters_balanced':True,'proof_sha256':hashlib.sha256((ROOT/'FOURTH_SCHUR_COEFFICIENT.md').read_bytes()).hexdigest()}
(ROOT/'PORTABILITY_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(receipt,indent=2))
