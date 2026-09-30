"""Preserve the previously verified edition before the new combined build."""
from pathlib import Path
import hashlib
import json
import shutil

here = Path(__file__).resolve().parent
target = here/'releases'/'first_stage_37_pages'
target.mkdir(parents=True, exist_ok=True)
expected = 'e9403745882a0d89165becacd09818d29a88f39905fe46a48b7b9045825a9b6f'
pdf_target = target/'coupled_viscous_control.pdf'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
if pdf_target.exists():
    assert sha(pdf_target) == expected
else:
    assert sha(here/'coupled_viscous_control.pdf') == expected
    for rel in ['coupled_viscous_control.pdf', 'checks/final_qa_receipt.json',
                'checks/build_receipt.json', 'integration_manifest.json',
                'integration/coupled_viscous_control_body.tex',
                'integration/coupled_viscous_control_preamble.tex',
                'HANDOFF.md', 'README.md']:
        dest = target/rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(here/rel, dest)
    (target/'RELEASE.json').write_text(json.dumps(dict(
        pages=37, exact_checks=91, pdf_sha256=expected,
        archived_before_second_stage_extension=True), indent=2)+'\n', encoding='utf-8')
print(json.dumps(dict(previous_release_preserved=True, pdf_sha256=sha(pdf_target))))
