"""Re-render rebuilt PDFs and compare every page with the inspected images."""
from pathlib import Path
import hashlib,json,subprocess,sys
root=Path(__file__).resolve().parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
qa=root/'qa_final'
old=json.loads((qa/'render_receipt.json').read_text())
pages={str(p.relative_to(root)):sha(p) for p in qa.glob('*/page-*.png')}
assert len(pages)==28
subprocess.run([sys.executable,str(root/'render_bridge.py')],check=True,capture_output=True)
changes=[p for p,h in pages.items() if sha(root/p)!=h]
assert not changes,changes
new=json.loads((qa/'render_receipt.json').read_text())
receipt=dict(schema='bridge-full-visual-review-v1',
reviewer='root',all_28_pages_personally_inspected=True,
inspection='All final content pages inspected in 15 two-page contact images; no clipping, overlap, malformed math or unresolved references seen.',
rebuilt_pages_pixel_identical=True,pages=pages,
current_readers=new,previous_inspected_readers=old,
source_versions='Separate bounded source comparison in revision_check/receipt.json.')
(qa/'visual_review.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(dict(all_passed=True,pages_checked=len(pages),
                    rebuilt_pages_pixel_identical=True)))
