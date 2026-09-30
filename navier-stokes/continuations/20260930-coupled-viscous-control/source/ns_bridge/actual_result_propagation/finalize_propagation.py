"""Bind completed propagation to actual build and separately recorded visual QA."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parent
bridge=root.parent;lane=bridge.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
b=json.loads((root/'build_receipt.json').read_text())
v=json.loads((root/'qa/visual_review.json').read_text())
assert b['all_passed'] and v['all_pages_personally_inspected']
assert v['pdf_sha256']==b['pdf_sha256']==sha(root/'current_bridge_reader.pdf')
assert b['body_sha256']==sha(root/'complete_body.tex')
for name,h in b['source_hashes'].items():assert sha(bridge/name)==h,name
for name,h in b['rendered_pages'].items():assert sha(root/'qa'/name)==h,name
assert sha(lane/'coupled_viscous_control.pdf')=='f74103eee85b3ba41dc8a746e3a97953bb5dfd31b053fa08e7a247c9f5c57d0f'
scope=(
"The released 166-page source Theorem 1.1 is propagated as attributed source input: "
"forced standard 3D incompressible Navier-Stokes, each fixed positive viscosity, "
"zero initial velocity, smooth compact force, bounded energy and unbounded velocity. "
"Its original signed path has positive swirl. The complete local proof transports "
"the source fields and every candidate residual through arbitrary fixed orthogonal "
"orientation, translation and viscosity ratio, with explicit inverse, vorticity, "
"support, force derivatives, energy and dissipation. The lattice-preserving "
"reflection gives negative swirl with the reflected force. "
"The actual finite compact curl candidate now has its two radial moments computed "
"as axial derivatives of explicit old-wave cross and new quadratic covariances. "
"The calculation proves disappearance of time, viscous, pressure and mean cross "
"terms after the specified average, with all physical terms included first. "
"It retains pointwise moments, all chart powers, field/derivative bounds, and "
"the exact auxiliary oscillation flux relating averaged and evaluated moments."
)
limits=(
"This lane has not independently verified the entire source proof. The source "
"theorem is not a proof of completion of the distinct infinite modified coupled "
"sequence. The full third shooting return remains unproved. Source-weighted "
"terminal estimates have not been transferred to that candidate."
)
nextwork=(
"Use the now explicit axial flux moments and actual chart amplitude/curl formulas "
"to compute quantitative orders for the retained third-growth seed and coefficient "
"path, and control every remaining candidate residual term. Propagate the source's "
"actual completed witness wherever it applies without waiting for that separate "
"candidate calculation. Keep source-selected positive swirl; reflected negative "
"swirl is an exact transformed witness, not a required interpretation."
)
handoff=f"""# Current complete source bridge and actual result propagation

Reader: current_bridge_reader.pdf, {b['pages']} pages.
SHA-256: {b['pdf_sha256']}

Unabridged parent-ready TeX: complete_body.tex.
SHA-256: {b['body_sha256']}
Preamble: complete_preamble.tex.
All {b['prefixed_labels']} labels have unique nsbridge:, nsprop:, or nsmom: namespaces.
This body already includes the full previous bridge; replace that integration body
with this one rather than importing the old body twice.

{scope}

{limits}

The cumulative build validates the old 46-check source bindings and runs
{b['new_registered_checks']} new exact replay cases. Both independent written
reviews and the complete local proofs are retained. There are no compilation
warnings, undefined references, or overfull/underfull boxes. All {b['pages']}
final rendered pages were personally inspected; hashes are bound in
qa/visual_review.json. The existing 102-page stage reader and 15-page prior
bridge remain unchanged.

Next programme: {nextwork}

Source attribution and exact theorem locations: source_scope_audit.md.
User's exact new steering: USER_STEERING.md and the lane USER_INPUTS_VERBATIM.md.
Reproduce: python build_propagation.py. Visual review remains a separate actual
inspection, never inferred from a successful build.

Parent owns cumulative TeX, publication, Overleaf and the sole Lean worker.
No remote publication, parent-owned file edit, or Lean/Lake/Elan run occurred here.
"""
(root/'HANDOFF.md').write_text(handoff,encoding='utf-8')
marker='## Verified actual result propagation'
entry=(marker+f"\n\nCurrent cumulative bridge: ns_bridge/actual_result_propagation/current_bridge_reader.pdf "
f"({b['pages']} pages; SHA256 {b['pdf_sha256']}). Full body: "
f"ns_bridge/actual_result_propagation/complete_body.tex (SHA256 {b['body_sha256']}). "
f"Full handoff: ns_bridge/actual_result_propagation/HANDOFF.md.\n\n"
+scope+"\n\n"+limits+"\n\n"+nextwork+"\n")
for name in ['LOGBOOK.md','ACTIVE_GOAL.md','HANDOFF.md','README.md']:
 p=lane/name;old=p.read_text(encoding='utf-8-sig')
 if marker in old:old=old[:old.index(marker)].rstrip()
 p.write_text(old+'\n\n'+entry,encoding='utf-8')
p=lane/'CONTINUATION.md';old=p.read_text(encoding='utf-8-sig')
if not old.startswith(marker):p.write_text(entry+'\n---\n\n'+old,encoding='utf-8')
with (bridge/'HANDOFF.md').open('a',encoding='utf-8') as f:
 f.write('\n\n'+entry)
s=json.loads((lane/'STATUS.json').read_text())
s.update(actual_source_result_propagation='Verified cumulative artifact in ns_bridge/actual_result_propagation',
 current_source_bridge_reader='ns_bridge/actual_result_propagation/current_bridge_reader.pdf',
 current_source_bridge_pages=b['pages'],current_source_bridge_pdf_sha256=b['pdf_sha256'],
 current_source_bridge_body_sha256=b['body_sha256'],
 actual_radial_moments_computed=True,source_actual_witness_transports_proved=True,
 source_whole_theorem_independently_verified_by_this_lane=False,
 actual_source_result_scope=scope,actual_source_result_limits=limits,active_work=nextwork)
(lane/'STATUS.json').write_text(json.dumps(s,indent=2)+'\n')
receipt=dict(schema='actual-result-handoff-v1',verified=True,
 pdf_sha256=b['pdf_sha256'],body_sha256=b['body_sha256'],
 build_receipt_sha256=sha(root/'build_receipt.json'),
 visual_receipt_sha256=sha(root/'qa/visual_review.json'),
 prior_102_page_reader_unchanged=True,prior_15_page_bridge_unchanged=True,
 source_whole_proof_verified=False,parent_integration_confirmed=False)
(root/'handoff_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
