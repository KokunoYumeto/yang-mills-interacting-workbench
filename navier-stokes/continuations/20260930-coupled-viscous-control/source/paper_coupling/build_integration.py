"""Produce an integration body with namespaced labels from the standalone proof."""
from pathlib import Path
import hashlib
import json
import re

base=Path(__file__).resolve().parent
source=(base/'coupled_background.tex').read_text(encoding='utf-8-sig')
body=source.split(r'\maketitle',1)[1].split(r'\end{document}',1)[0].strip()+'\n'
body=re.sub(r'\\(label|ref|eqref)\{([^}]+)\}', lambda m:'\\'+m[1]+'{pc:'+m[2]+'}', body)
(base/'coupled_background_body.tex').write_text(body,encoding='utf-8')
labels=re.findall(r'\\label\{([^}]+)\}',body)
manifest={
    'body':'coupled_background_body.tex',
    'source':'coupled_background.tex',
    'label_prefix':'pc:',
    'labels':labels,
    'packages':['amsmath','amssymb','amsthm','mathtools','hyperref'],
    'macros':{'R':r'\mathbb R','AB':r'\mathrm{AB}','epsv':r'\varepsilon_{\mathrm v}',
              'kapth':r'\kappa_{\mathrm{th}}','Gcal':r'\mathcal G','dd':r'\mathrm d'},
    'operators':{'tr':'tr','sym':'sym'},
    'theorem_environments':['proposition'],
    'standard_environments':['proof'],
    'source_sha256':hashlib.sha256(source.encode()).hexdigest(),
    'body_sha256':hashlib.sha256(body.encode()).hexdigest(),
    'mathematical_changes':'None; document wrapper removed and labels/references prefixed pc:.'
}
(base/'integration_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'body':manifest['body'],'labels':len(labels),'prefix':'pc:'}))
