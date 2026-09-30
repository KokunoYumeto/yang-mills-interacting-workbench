"""Refresh the exact local handoff manifest after completed human-visible QA."""
from pathlib import Path
import hashlib
import json

HERE=Path(__file__).resolve().parent
def read(path):
    return json.loads((HERE/path).read_text(encoding='utf-8'))
def sha(path):
    return hashlib.sha256((HERE/path).read_bytes()).hexdigest()
build=read('build_receipt.json')
render=read('qa/render_receipt.json')
visual=read('qa/visual_review.json')
replay=read('replay_receipt.json')
pdf_sha=sha('standalone.pdf')
body_sha=sha('third_growth_geometry_body.tex')
assert build['pdf_sha256']==render['pdf_sha256']==visual['pdf_sha256']==pdf_sha
assert build['body_sha256']==replay['source_sha256']==body_sha
assert not build['latex_issues'] and not render['out_of_page_text']
assert all(p['exit_code']==0 for p in build['passes'])
assert visual['pages_reviewed']==list(range(1,build['pages']+1))
assert not any(visual[k] for k in ['clipping','overlap','unreadable_glyphs','bad_page_breaks'])
assert replay['passed']==len(replay['checks']) and all(replay['checks'].values())
build['visual_review']='passed; exact page/hash record in qa/visual_review.json'
(HERE/'build_receipt.json').write_text(json.dumps(build,indent=2)+'\n',encoding='utf-8')
manifest={
    'status':'complete local geometry section; parent integration separate',
    'mathematical_corrections':[],
    'layout_changes':['Split the original seed display across two lines.',
                      'Display both inherited diagonal damping exponents.'],
    'primary_replay':'replay_third_growth_geometry.py',
    'primary_receipt':'replay_receipt.json',
    'checks':replay['passed'],
    'check_count_note':'43 total includes the original independent20 and23 additional checks; do not count the20 twice.',
    'standalone_pages':build['pages'],
    'build_passes':len(build['passes']),
    'latex_issues':build['latex_issues'],
    'visual_pages_reviewed':visual['pages_reviewed'],
    'body_sha256':body_sha,'standalone_pdf_sha256':pdf_sha,
    'proof':'third_growth_geometry_body.tex',
    'audits':['audit/AUDIT.md','COMPLETION_AUDIT.md','affine_audit/AUDIT.md'],
    'sha256':{p:sha(p) for p in ['third_growth_geometry_body.tex',
        'replay_third_growth_geometry.py','replay_receipt.json','audit/verify_third_map.py',
        'audit/verification.json','build_receipt.json','qa/render_receipt.json',
        'qa/visual_review.json','COMPLETION_AUDIT.md','affine_audit/AUDIT.md']}}
(HERE/'HANDOFF.json').write_text(json.dumps(manifest,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'checks':manifest['checks'],'pages':manifest['standalone_pages'],
                  'body_sha256':body_sha,'handoff':str(HERE/'HANDOFF.json')}))
