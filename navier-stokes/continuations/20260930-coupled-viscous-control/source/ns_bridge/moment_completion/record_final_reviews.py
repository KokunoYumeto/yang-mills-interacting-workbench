"""Bind completed root proof and visual reviews; never infer unseen pages."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
proofs={
 'source_operation/operation_body.tex':'14ab6d566a4b376eed8bdc9621a2758732ceafb82b640f21359de2fa40e19a7a',
 'stress_completion/stress_completion.tex':'6975ee64e1b7aa9d5615a11c706f281b5d46c3d7fb95b81984c5c2c79b9479f7',
 'quantitative_moments.tex':'da39fd2660a969f893836f232e720ad1e3c54250bf6b7702a6de8324509cad49',
 'mean_costs/mean_costs.tex':'f0a7e8a99b824dd9f84d7dbdcaa45571d2bbc5e06f57595fe56d8c53c7d5603d'}
for f,h in proofs.items():assert sha(root/f)==h,f
independent=['source_operation/REVIEW_OPERATION.md',
             'source_operation/REVIEW_STRESS.md','review/REVIEW_QUANTITATIVE.md']
supporting=['mean_costs/HANDOFF/REVIEW_MEAN.md']
review=dict(schema='moment-completion-full-proof-review-v1',reviewer='/root',
 all_new_proofs_read_completely=True,proof_hashes=proofs,
 independent_review_hashes={f:sha(root/f) for f in independent},
 supporting_review_hashes={f:sha(root/f) for f in supporting},
 unresolved_mathematical_issues=[],
 scope=[
  'Root read all four complete new mathematical bodies, then every changed mathematical passage and final TeX environment repair.',
  'Independent source-operation review caught and verified repair of physical/normalized temporal units, temporal-cutoff product scope, and old residual versus finite increment scope.',
  'Independent quantitative review verified all-order product/scale bounds after full-target/increment and full-pressure/average distinctions were repaired.',
  'Independent stress review covered full divergence, moving-bump correction, compactness, torque, tracefree pressure, exact divergence image and chart units. Root incorporated its averaged-quantities wording refinement and read the final proof.',
  'Mean force formulas received independent component derivation as recorded in the supporting report. Root directly reviewed the full mean proof, including later pressure majorants and Cartesian derivative recursion; no independent whole-mean-proof review is claimed.',
  'Root verified the explicit pressure-free G to D,H,E,Pi to force calculation is not circular, and all axial/time/cutoff/inverse-radius derivatives and original source parameters remain.',
  'Analytic proofs and exact finite algebra replay have distinct roles. Structural checks were excluded from the 190-case mean mathematics count, and three tautological cases removed.',
  'No complete source-theorem certification, terminal uniform estimates, infinite modified coupled construction, or velocity realization of a symmetric stress is asserted.'])
(root/'review/ROOT_FINAL_REVIEW.json').write_text(json.dumps(review,indent=2)+'\n')
build=json.loads((root/'build_receipt.json').read_text())
assert build['pdf_sha256']==sha(root/'current_bridge_reader.pdf')
pages=list(range(61,74))
contacts=[f'contact-{n:02}.png' for n in range(31,38)]
visual=dict(schema='actual-page-inspection-v1',reviewer='/root',
 pdf_sha256=build['pdf_sha256'],inspected_pages=pages,inspected_contacts=contacts,
 contact_hashes={f:sha(root/'qa'/f) for f in contacts},
 rendered_page_hashes={f'page-{n:02}.png':sha(root/'qa'/f'page-{n:02}.png') for n in pages},
 unresolved_issues=[],
 observations='Root actually viewed contacts31-37 at original detail: all13 pages61-73. Equations, table, line wraps, page numbers and transitions are legible and unclipped. Dense force/cost displays have no collisions. Final page73 ends naturally with remaining white space. This receipt covers only these personally inspected pages.')
(root/'qa/visual_review_pages_61_73.json').write_text(json.dumps(visual,indent=2)+'\n')
print(json.dumps(dict(full_new_proofs_reviewed=True,root_visual_pages=pages)))
