"""Bind the actual completed 41-page release and preserve every prior release."""
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
assert b['new_registered_checks']==120 and b['total_registered_checks']==228
for name,h in b['source_hashes'].items():assert sha(bridge/name)==h,name
for name,h in b['rendered_pages'].items():assert sha(root/'qa'/name)==h,name
for r in b['new_replays']:
 assert sha(root/r['script'])==r['script_sha256']
 assert sha(root/r['receipt'])==r['receipt_sha256']
priorhashes={
 lane/'coupled_viscous_control.pdf':'f74103eee85b3ba41dc8a746e3a97953bb5dfd31b053fa08e7a247c9f5c57d0f',
 bridge/'source_bridge_reader.pdf':'4794e0a72eb468d8e1f21e9cd4560446fa578e2acf5b0c125b52683a03b9d1e6',
 bridge/'actual_result_propagation/current_bridge_reader.pdf':'0e6480272410fbd1017651077d2fc134c15c3eab5e797a18df6c26b2b1545f3d'}
for p,h in priorhashes.items():assert sha(p)==h,p
scope=(
"The actual third-growth signed pair now has proved component derivative bounds "
"and closed all-order recurrences in its original evolving-parent data. The original "
"temperature target retains lambda_hat3^(-7/8), whereas the attained vorticity magnitude "
"is bounded on both sides by explicit constants times A0 lambda_hat3^(1/8)/(sigma2 sqrt(n_i)). "
"The exact source physical clock has zero spatial derivative and time derivative Q^(-1-h). "
"With fixed original coupled data across labels this proves complete amplitude/spatial "
"factorization of the physical curl and pressure. The actual source tangent frame, "
"its inverse norms and signed diffusion mismatch are calculated. The explicit initial "
"map preserving S3 and u_i, followed by its proved finite fundamental-matrix intertwiner, "
"maps the actual third-growth trajectory exactly to the source Lemma 7.4 homogeneous "
"pulse at the source's viscosity one and harmonic one. Its inverse, determinant, "
"initial scale costs and forward/inverse propagation costs are proved. Full physical "
"curl shapes, both radial moments, clock costs, old-wave interactions, pressure, diffusion "
"and every mixed-label nonlinear residual term have explicit formulas and finite bounds."
)
limits=(
"The complete source theorem remains attributed source input; this lane has not "
"independently certified the entire manuscript. Its source-selected positive swirl "
"and exact reflected negative swirl retain their respective forces. Finite source-pulse "
"equality preserves that source object's own estimates, but does not prove uniform "
"weighted estimates for the distinct direct candidate L=I. The full third shooting "
"return, infinite fixed-positive-d modified coupled sequence and terminal smooth-force "
"extension for that candidate remain unproved. The source theorem does not dispose "
"of the candidate's calculated nonzero residual."
)
nextwork=(
"Continue from the actual source pulse equality and explicit physical residual. "
"Quantify the source-shape derivative costs in the needed weighted classes and use "
"the computed axial flux moments in the source's correction operations, retaining "
"the baseline, old-wave, curl, cutoff and quadratic terms. Apply the exact full-field "
"viscosity/orientation map wherever the source's own completed witness applies. "
"Do not restart auxiliary third shooting absent the parent's source-bridge programme "
"change. Parent owns full-source audit, cumulative TeX, publication, Overleaf and sole Lean."
)
handoff=f"""# Complete source bridge with actual third-growth quantitative costs

Reader: current_bridge_reader.pdf, {b['pages']} pages.
PDF SHA256: {b['pdf_sha256']}
Unabridged parent-ready body: complete_body.tex.
Body SHA256: {b['body_sha256']}
Preamble: complete_preamble.tex.

This body contains all of the preceding 24-page bridge's mathematics and all three
new proof components. Replace the prior bridge integration body with this complete
body; importing both duplicates their mathematics and labels. All {b['prefixed_labels']}
labels are unique, with nsbridge:, nsprop:, nsmom:, tgdc:, tgframe: and tgq: prefixes.
The preamble adds the theorem environment used by the new derivative proofs.

{scope}

{limits}

Validation: the build verifies the preceding 108-case release bindings and actually
runs 120 new exact cases: 55 original derivative cases, 40 source clock/frame/map
cases and 25 complete residual/units cases. These 228 registered cases are distinct
from the 688 checks of the untouched companion 102-page stage reader. The written
proofs supply the analytic claims; symbolic replay is not a substitute for them.
All three full new bodies have been read by root. Independent reviews of the
quantitative and frame proofs are in derivative_costs/REVIEW_QUANTITATIVE.md and
derivative_costs/REVIEW_FRAME.md.

The source d_r error found during review was corrected to the exact p63 equation
(6.2), including the factor two on h kappa_s. The frame also distinguishes the source
growth constant lambda0 from the coupled frequency lambda0=mu and proves smooth
parameter dependence using uniformly differentiated ordered-integral series.
Root repaired TeX delimiters and long displays without changing mathematics.

The final reader has zero compilation warnings, unresolved references and
overfull/underfull boxes. All 41 final rendered pages were personally inspected.
build_receipt.json and qa/visual_review.json bind sources, outputs and rendered
pages. The previous 102-, 15- and 24-page readers are unchanged.

Next calculation: {nextwork}

The assignment goal remains active. No Lean, remote publication, parent-owned edit
or new user permission gate was used. Parent and dissemination delivery receipts,
when present, establish dispatch only; actual integration requires its own evidence.
"""
(root/'HANDOFF.md').write_text(handoff,encoding='utf-8')
marker='## Verified third-growth quantitative source bridge'
entry=(marker+f"\n\nCurrent cumulative source bridge: ns_bridge/third_growth_quantitative/current_bridge_reader.pdf "
f"({b['pages']} pages; SHA256 {b['pdf_sha256']}). Its complete body "
f"ns_bridge/third_growth_quantitative/complete_body.tex has SHA256 {b['body_sha256']}. "
f"There are {b['prefixed_labels']} unique labels and 120 newly replayed exact cases "
"with 108 prior registered cases preserved by verified bindings. All 41 pages were inspected, "
"with no unresolved build or layout issue. Full handoff: ns_bridge/third_growth_quantitative/HANDOFF.md.\n\n"
+scope+"\n\n"+limits+"\n\n"+nextwork+"\n")
for name in ['LOGBOOK.md','ACTIVE_GOAL.md','HANDOFF.md','README.md']:
 p=lane/name;old=p.read_text(encoding='utf-8-sig')
 if marker not in old:p.write_text(old+'\n\n'+entry,encoding='utf-8')
for p in [lane/'CONTINUATION.md',root/'CONTINUATION.md']:
 old=p.read_text(encoding='utf-8-sig')
 if not old.startswith(marker):p.write_text(entry+'\n---\n\n'+old,encoding='utf-8')
p=bridge/'HANDOFF.md';old=p.read_text(encoding='utf-8-sig')
if marker not in old:p.write_text(old+'\n\n'+entry,encoding='utf-8')
s=json.loads((lane/'STATUS.json').read_text())
s.update(current_source_bridge_reader='ns_bridge/third_growth_quantitative/current_bridge_reader.pdf',
 current_source_bridge_pages=b['pages'],current_source_bridge_pdf_sha256=b['pdf_sha256'],
 current_source_bridge_body_sha256=b['body_sha256'],third_growth_quantitative_source_bridge_verified=True,
 source_actual_homogeneous_pulse_exactly_matched=True,
 source_whole_theorem_independently_verified_by_this_lane=False,
 actual_source_result_scope=scope,actual_source_result_limits=limits,active_work=nextwork)
(lane/'STATUS.json').write_text(json.dumps(s,indent=2)+'\n')
reviews=[root/'derivative_costs/REVIEW_QUANTITATIVE.md',root/'derivative_costs/REVIEW_FRAME.md']
receipt=dict(schema='third-growth-quantitative-handoff-v1',verified=True,
 pdf_sha256=b['pdf_sha256'],body_sha256=b['body_sha256'],
 build_receipt_sha256=sha(root/'build_receipt.json'),visual_receipt_sha256=sha(root/'qa/visual_review.json'),
 reviewed_proof_sources={str(p.relative_to(root)):sha(p) for p in [
 root/'derivative_costs/derivative_costs.tex',root/'frame_audit/frame_body.tex',root/'quantitative_body.tex']},
 independent_review_hashes={str(p.relative_to(root)):sha(p) for p in reviews},
 prior_reader_hashes={str(p.relative_to(lane)):h for p,h in priorhashes.items()},
 root_all_new_proofs_read=True,source_whole_proof_verified=False,parent_integration_confirmed=False)
(root/'handoff_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
