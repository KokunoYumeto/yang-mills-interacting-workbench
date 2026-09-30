"""Record the explicit completed visual review for the current paired PDF.

Use only after inspecting every rendered page from the current build.
Hashes reject recording against a changed proof, entry file or PDF.
"""
from pathlib import Path
import argparse
import hashlib
import json

parser=argparse.ArgumentParser()
parser.add_argument('--reviewed-all-pages',action='store_true',required=True)
args=parser.parse_args()
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
build=json.loads((HERE/'build_receipt.json').read_text(encoding='utf-8'))
assert build['all_passed']
assert sha(HERE/'second_return.pdf')==build['pdf_sha256']
assert sha(HERE/'second_return_body.tex')==build['body_sha256']
assert sha(HERE.parent/'finite_stage'/'actual_viscous_entry.tex')==build['entry_sha256']
for rel,digest in build['rendered_page_sha256'].items():
    assert sha(HERE/rel)==digest
result=dict(schema='paired-entry-second-return-visual-review-v1',
    all_pages_visually_reviewed=True,
    page_count=build['page_count'],pdf_sha256=build['pdf_sha256'],
    body_sha256=build['body_sha256'],entry_sha256=build['entry_sha256'],
    build_receipt_sha256=sha(HERE/'build_receipt.json'),
    reviewed_contact_sheets=build['contact_sheets'],
    method='Assistant inspected every Poppler-rendered page in the contact sheets.',
    clipping=False,overlap=False,broken_equations=False,
    latex_diagnostics=build['latex_diagnostics'],
    exact_check_count=build['exact_check_count'],
    status='verified_finite_paired_reader',
    infinite_modified_viscous_sequence_proved=False)
(HERE/'visual_review_receipt.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(visual_review_recorded=True,pages=build['page_count'],
                     pdf_sha256=build['pdf_sha256'])))
