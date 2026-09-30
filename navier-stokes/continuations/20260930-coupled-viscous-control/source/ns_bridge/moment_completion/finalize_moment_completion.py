"""Finalize only after separately recorded full proof and actual visual reviews."""
from pathlib import Path
import datetime,hashlib,json

root=Path(__file__).resolve().parent
lane=root.parent.parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
read=lambda p:json.loads(p.read_text(encoding='utf-8'))
build=read(root/'build_receipt.json')
visual=read(root/'qa/visual_review.json')
review=read(root/'review/ROOT_FINAL_REVIEW.json')
assert build['all_passed'] and not build['warnings']
assert build['pdf_sha256']==visual['pdf_sha256']==sha(root/'current_bridge_reader.pdf')
assert visual['all_pages_visually_inspected']
assert sorted(visual['inspected_pages'])==list(range(1,build['pages']+1))
assert not visual['unresolved_issues']
assert review['all_new_proofs_read_completely'] and not review['unresolved_mathematical_issues']
for f,h in review['proof_hashes'].items():assert sha(root/f)==h,f
for f,h in review['independent_review_hashes'].items():assert sha(root/f)==h,f
for f,h in review['supporting_review_hashes'].items():assert sha(root/f)==h,f
for f,h in build['source_hashes'].items():assert sha(root.parent/f)==h,f
for item in build['new_replays']:
    assert sha(root/item['script'])==item['script_sha256']
    assert sha(root/item['receipt'])==item['receipt_sha256']
    data=read(root/item['receipt'])
    assert len(data['checks'])==item['check_count']
    assert all(c['passed'] is True for c in data['checks'])
for f,h in build['rendered_pages'].items():assert sha(root/'qa'/f)==h,f
oldreaders={
    'coupled_viscous_control.pdf':'f74103eee85b3ba41dc8a746e3a97953bb5dfd31b053fa08e7a247c9f5c57d0f',
    'ns_bridge/source_bridge_reader.pdf':'4794e0a72eb468d8e1f21e9cd4560446fa578e2acf5b0c125b52683a03b9d1e6',
    'ns_bridge/actual_result_propagation/current_bridge_reader.pdf':'0e6480272410fbd1017651077d2fc134c15c3eab5e797a18df6c26b2b1545f3d',
    'ns_bridge/third_growth_quantitative/current_bridge_reader.pdf':'97c2dd88f216679eb84c64d69ed98cbf2a504d3eea5057790738cc89eb7b31e4'}
for f,h in oldreaders.items():assert sha(lane/f)==h,f
scope=(
    "The complete new proofs compute all three actual pressure/flux defects from the "
    "retained old-wave cross and new quadratic covariance; reconstruct the full shifted "
    "compact pressure including its auxiliary cutoff remainder; prove the exact physical "
    "five-row mean-velocity inverse and its remaining nonlinear defects; construct a "
    "compact symmetric stress cancelling all three components of the actual averaged "
    "force; prove its tracefree-pressure bijection, all force/torque compatibilities, "
    "divergence image and projection; and give all-order original-scale moment, moving-bump, "
    "mean-velocity and full physical force costs. The axial derivative of q and the "
    "pressure-induced change from raw J1 to Jz+c_rho P are retained throughout.")
limits=(
    "The manuscript's forced Navier-Stokes blowup theorem remains attributed source input; "
    "this lane has not independently certified its entire proof. Its displayed positive "
    "swirl and the proved negative reflection retain their respective forces. A compact "
    "stress representation is not asserted to be an added velocity or wave covariance. "
    "The actual five-row velocity update retains its computed nonlinear and differential "
    "defects. Uniform source-weighted bounds for an increasing direct-candidate family, "
    "the full third shooting return, infinite fixed-positive-d modified coupled sequence "
    "and terminal smooth-force extension remain unproved.")
nextwork=(
    "Use the computed full current defects, explicit physical mean correction and its "
    "complete pressure/force costs as the actual next correction inputs. Calculate their "
    "band and pulse-envelope dependence in the source classes, retaining inverse "
    "Vandermonde constants, q derivatives, old-wave and mean cross terms, cutoffs, "
    "quadratic terms and physical viscosity. Keep source-attributed cycle estimates "
    "distinguished from proved candidate estimates. Propagate the source's own completed "
    "witness through the already proved full-field viscosity/orientation map wherever "
    "it applies. Further auxiliary shooting remains deferred under parent steering.")
handoff=f"""# Complete actual pressure, moment and mean-velocity continuation

Reader: current_bridge_reader.pdf ({build['pages']} pages).
PDF SHA256: {build['pdf_sha256']}
Unabridged integration body: complete_body.tex
Body SHA256: {build['body_sha256']}
Preamble: complete_preamble.tex

This complete body contains all preceding 41-page bridge mathematics and all four
new full proof components. Replace the preceding bridge body when integrating;
importing both duplicates their mathematics and labels. All {build['prefixed_labels']}
labels are unique. New prefixes are momop:, mcstress:, mcq: and mcmean:.

{scope}

{limits}

Verification: {build['new_registered_checks']} new exact cases were actually replayed.
The preceding 228 registered cases are preserved through verified source bindings,
giving {build['total_registered_checks']} bridge cases. The 688 checks of the
unchanged companion 102-page finite-stage reader are a separate registry.
Written complete proofs establish the analytic claims. Root read all four new
bodies completely, and independent mathematical reports are bound in
review/ROOT_FINAL_REVIEW.json. The build has zero warnings, unresolved references
or overfull/underfull boxes. Every final page was visually inspected; the named
reviewers and exact rendered-page hashes are in qa/visual_review.json.

The full proofs are in source_operation/operation_body.tex,
stress_completion/stress_completion.tex, quantitative_moments.tex and
mean_costs/mean_costs.tex, reproduced unabridged in the integration body.
build_receipt.json and handoff_receipt.json bind current sources and artifacts.
The preceding 102-, 15-, 24- and 41-page readers remain byte-for-byte unchanged.

Next work: {nextwork}

The assignment goal remains active. Parent task 01a080e3-5d12-7e72-8131-8d1cf92b9737
owns cumulative integration, full-source audit, publication and Overleaf. The
dissemination owner is 01a0814d-b058-7b43-a0ec-6e323caf86ea. No Lean or publication
was performed here. Delivery receipts establish dispatch only; no owner integration
is claimed without separate evidence.
"""
(root/'HANDOFF.md').write_text(handoff,encoding='utf-8')
receipt=dict(schema='actual-moment-completion-handoff-v1',verified=True,
    pdf_sha256=build['pdf_sha256'],body_sha256=build['body_sha256'],
    build_receipt_sha256=sha(root/'build_receipt.json'),
    visual_receipt_sha256=sha(root/'qa/visual_review.json'),
    proof_review_receipt_sha256=sha(root/'review/ROOT_FINAL_REVIEW.json'),
    handoff_sha256=sha(root/'HANDOFF.md'),
    reviewed_proof_sources=review['proof_hashes'],
    independent_review_hashes=review['independent_review_hashes'],
    supporting_review_hashes=review['supporting_review_hashes'],
    prior_reader_hashes=oldreaders,root_all_new_proofs_read=True,
    source_whole_proof_verified=False,parent_integration_confirmed=False)
(root/'handoff_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
status=read(lane/'STATUS.json')
status.update(current_source_bridge_reader='ns_bridge/moment_completion/current_bridge_reader.pdf',
    current_source_bridge_pages=build['pages'],current_source_bridge_pdf_sha256=build['pdf_sha256'],
    current_source_bridge_body_sha256=build['body_sha256'],
    current_source_bridge_registered_checks=build['total_registered_checks'],
    actual_moment_completion_verified=True,actual_source_result_scope=scope,
    actual_source_result_limits=limits,active_work=nextwork)
(lane/'STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
record=f"""
## Verified actual pressure, moment and mean-velocity continuation

Current cumulative reader: ns_bridge/moment_completion/current_bridge_reader.pdf,
{build['pages']} pages, SHA256 {build['pdf_sha256']}.
Full body SHA256 {build['body_sha256']}; {build['prefixed_labels']} unique labels.
All {build['new_registered_checks']} new exact cases passed, with 228 preceding
registered cases preserved ({build['total_registered_checks']} total bridge cases).
Every final page was inspected; current build, proof, visual and handoff receipts
are in ns_bridge/moment_completion/. Earlier verified readers are unchanged.

{scope}

{limits}

Next work: {nextwork}

The goal tool remains active with historical wording. This durable update corrects
the workflow without claiming that tool wording was edited or unfinished work was
completed. Parent owns full-source audit, cumulative TeX, Overleaf and publication.
Write only this lane; no Lean. Follow HANDOFF.md and current receipts. Dispatch and
integration remain separate evidence; do not claim a parent acknowledgement from
a successful tool send.
"""
for name in ['CONTINUATION.md']:
    path=lane/name
    old=path.read_text(encoding='utf-8') if path.exists() else ''
    path.write_text(record+'\n---\n\n'+old,encoding='utf-8')
goal=f"""# Active assignment and authoritative continuation

Carry out the original coupled-viscous-control assignment: reconstruct the actual
released Alpoge--Buckmaster growth, transition, steering, vorticity return and
holding system; derive its retained-viscosity version with evolving parents,
original controls and every force; prove the strongest exact available controlled
stage. Continue toward the requested coupled construction without freezing parent
feedback or replacing missing calculations by assumed hypotheses.

The user directs following the programme implied by the actual results and now
propagating the released Navier-Stokes result wherever it exists. Their suggested
negative blowout was a possibility, not a required sign. Retain the manuscript's
displayed positive swirl path. Use the proved full-field reflection for the
opposite swirl with its reflected force; do not change viscosity's sign or infer
that negating velocity alone preserves the equation.

Write only output/navier_stokes_research_2026-09-08/lanes/coupled_viscous_control.
Parent 01a080e3-5d12-7e72-8131-8d1cf92b9737 owns full-source audit, cumulative TeX,
Overleaf, publication and Lean. Send full proved artifacts to that parent and
dissemination owner 01a0814d-b058-7b43-a0ec-6e323caf86ea. No Lean/Lake/Elan,
remote publication or parent-owned edits here. Continue routine local repairs
without another permission gate. Do not infer attribution from account paths.

Resume from LOGBOOK.md, USER_INPUTS_VERBATIM.md, DELEGATED_INPUT_VERBATIM.md,
CONTINUATION.md, STATUS.json and ns_bridge/moment_completion/HANDOFF.md.
Literal user provenance is kept separately; perform a bounded JSONL audit only
when new uncaptured user input exists. Preserve prior log and artifact history.
The goal tool is active; its historical wording cannot be edited by the available
status-only tool. This durable file corrects the workflow without completing or
replacing that unfinished goal.

Current source bridge: ns_bridge/moment_completion/current_bridge_reader.pdf,
{build['pages']} pages, SHA256 {build['pdf_sha256']}.
Its complete_body.tex reproduces all previous bridge proofs and all four new
components; integrate it as the replacement bridge body to avoid duplicate labels.
There are {build['prefixed_labels']} unique labels and
{build['total_registered_checks']} registered bridge checks, of which
{build['new_registered_checks']} were newly replayed. Build, complete proof review,
all-page visual review and handoff receipts bind current hashes. Earlier 102-,15-,
24- and41-page releases remain unchanged. The separate102-page reader and688 checks
prove the first two returns and holds, third growth, full third transition and the
initial third steering interval with full compact scalar/vector forces.

{scope}

{limits}

{nextwork}

Preserve A0, lambda0, mu, source nu=sqrt(A0) separately from physical viscosity,
every original coordinate, orientation, scale, domain and codomain. Prove each
map, inverse, coefficient, support and force claim in full standalone TeX.
Propagate corrections through affected current proofs and integration exports.
Use exact algebra replay for identities and written complete proofs for analytic
claims. Rebuild and inspect every changed reader page. Report only verified scope;
successful dispatch is not an integration acknowledgement. Keep the goal active
while required mathematics remains. Do not substitute a narrow verification or
an unchanged-state obstruction for the full assignment.
"""
goal=goal.replace(scope,
    "Current new proofs give the actual pressure/flux defects, full shifted pressure "
    "and cutoff remainder, exact five-row physical mean inverse and surviving defects, "
    "compact full averaged-stress cancellation, tracefree-pressure bijection, force/torque "
    "compatibilities and divergence projection. They include all-order original-scale "
    "moment, moving-bump, mean-velocity and full force costs. Every q derivative and "
    "pressure-induced axial flux change is retained.")
goal=goal.replace(limits,
    "The source's forced blowup theorem remains attributed, not independently certified "
    "by this lane. Stress cancellation is not a wave-covariance or velocity realization. "
    "The five-row update leaves its computed defects. Uniform weighted direct-candidate "
    "bounds, the full third shooting return, infinite fixed-positive-d modified sequence "
    "and terminal smooth-force extension remain unproved.")
goal=goal.replace(nextwork,
    "Next compute band and pulse-envelope dependence of the full current defects, "
    "mean correction and pressure/force costs in the source classes. Retain inverse "
    "moment matrices, q derivatives, old-wave/mean cross terms, cutoffs, quadratic "
    "terms and viscosity. Keep attributed cycle estimates distinct from proved candidate "
    "estimates. Apply the established viscosity/orientation map to the source's own "
    "witness wherever it applies. Defer further auxiliary shooting under parent steering.")
assert 3500 <= len(goal) <= 5000,len(goal)
goalpath=lane/'ACTIVE_GOAL.md'
if goalpath.exists():
    oldbytes=goalpath.read_bytes()
    hist=lane/'goal_history';hist.mkdir(exist_ok=True)
    archived=hist/('ACTIVE_GOAL_before_moment_completion_'+hashlib.sha256(oldbytes).hexdigest()[:16]+'.md')
    if archived.exists():assert archived.read_bytes()==oldbytes
    else:archived.write_bytes(oldbytes)
goalpath.write_text(goal,encoding='utf-8')
with (lane/'LOGBOOK.md').open('a',encoding='utf-8') as f:f.write(record)
with (root/'CONTINUATION.md').open('a',encoding='utf-8') as f:f.write(record)
print(json.dumps(dict(verified=True,pages=build['pages'],
    pdf_sha256=build['pdf_sha256'],handoff_sha256=receipt['handoff_sha256'])))
