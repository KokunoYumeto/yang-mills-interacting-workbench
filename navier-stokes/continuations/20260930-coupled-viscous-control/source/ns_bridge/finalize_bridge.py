"""Bind handoffs and continuity to the inspected finite bridge artifacts."""
from pathlib import Path
import json,hashlib,re
root=Path(__file__).resolve().parent
lane=root.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
build=json.loads((root/'build_receipt.json').read_text())
visual=json.loads((root/'qa_final/visual_review.json').read_text())
assert build['all_passed'] and visual['all_28_pages_personally_inspected']
for name,h in build['readers'].items():assert sha(root/name)==h
for name,h in build['sources'].items():assert sha(root/name)==h
for item in visual['current_readers']:assert sha(root/item['pdf'])==item['sha256']
pdf=sha(root/'source_bridge_reader.pdf')
body=sha(root/'integration/source_bridge_complete_body_prefixed.tex')
scope=("The finite composite map is proved: retained coupled amplitude -> moving tangent frame "
"and finite-interval intertwiner -> compact physical curl and pressure -> exact momentum-residual "
"increment -> double average -> physical radial moment projection -> signed covariance derivative "
"inverse -> physical label assembly. The resulting residual explicitly retains the baseline, two "
"weighted moments, axial tensor fluxes, old-wave interactions, curl remainder, quadratic "
"self-interaction and pressure. The full spatial reflection proves the exact opposite-swirl "
"map with viscosity, force, vorticity orientation and energy retained.")
limits=("No third shooting return, source-wide correction estimates, infinite modified sequence, "
"terminal force extension, full-paper theorem verification or whole-revision equivalence is claimed. "
"Parent owns cumulative integration, publication, Overleaf and the sole Lean worker.")
nextwork=("Compute the actual coupled candidate's source-chart amplitude/derivative orders and "
"its two residual moments, then establish quantitative control of every term in the displayed "
"finite covariance residual. Do not transfer the source's weighted classes or infinite-cycle "
"gains to the candidate without that calculation. Further auxiliary shooting remains deferred "
"under the parent's source-bridge programme.")
handoff=f"""# Complete finite signed source bridge

Current reader: source_bridge_reader.pdf, 15 pages; SHA-256 {pdf}.
Complete parent integration body: integration/source_bridge_complete_body_prefixed.tex;
SHA-256 {body}. All {build['prefixed_labels']} labels/references in that export use the nsbridge: prefix.
The full preamble and individual unabridged bodies are in integration/.

{scope}

Verification: 46 registered exact checks (6 operator, 15 moving-frame, 25 covariance);
two supplemental overlapping replays also pass and are not added again. All four final
readers build without warnings, unresolved references or overfull/underfull boxes.
All 28 rendered pages (3 operator, 4 pulse, 6 covariance and 15 combined) were personally
inspected. After the final build, all page PNGs were pixel-identical to those inspected.
Receipts: build_receipt.json and qa_final/visual_review.json.

Both supplied source editions remain preserved locally: openai_navier_stokes.pdf
(165 pages, SHA-256 8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81)
and openai_navier_stokes_166p.pdf (166 pages, SHA-256
0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f).
revision_check/REPORT.md and receipt.json document all 31 referenced formula comparisons
and exact page mapping; no displayed formula change was found there. Source raw pages
108-110 are byte-identical. This comparison is bounded to the stated equations/pages.

Earlier pulse/covariance draft handoffs are superseded. Repaired errors include tangent-frame
scope, projection of normal force, signed diffusion discrepancy, the energy defect, physical
r/R conversion and Jacobian, correct fifth moment row, and complete covariance remainders.
Invalid old mathematical drafts remain in withdrawn_drafts_20260908/ for provenance.
Version-specific independent audit reports are under covariance_bridge/audit/.

{limits}

Next concrete programme: {nextwork}

Reproduce: python build_bridge.py; python render_bridge.py.
Visual inspection must be separately recorded; rebuilding does not assert visual review.
"""
(root/'HANDOFF.md').write_text(handoff)
for sub,tex,pd in [('pulse_comparison','pulse_comparison.tex','pulse_comparison.pdf'),
                  ('covariance_bridge','covariance_bridge.tex','covariance_bridge.pdf')]:
    (root/sub/'HANDOFF.md').write_text(
        f'# Final {sub.replace("_"," ")} handoff\n\n'
        f'TeX SHA-256: {sha(root/sub/tex)}\n\nPDF SHA-256: {sha(root/sub/pd)}\n\n'
        'Current verified complete handoff: ../HANDOFF.md. Earlier hashes and draft conclusions '
        'are superseded. Final rendered pages were inspected; source-revision and full scope '
        'are recorded in the complete handoff.\n')
# Refresh the extraction memo handoff hash after its explicit sign correction.
memo=root/'source_cycle_extract/COVARIANCE_CORRECTION_PROVENANCE.md'
mp=root/'source_cycle_extract/HANDOFF.md'
ms=mp.read_text()
ms=re.sub(r'(Memo:.*?\n  - SHA-256: )[a-f0-9]{64}',lambda m:m.group(1)+sha(memo),ms,count=1,flags=re.S)
mp.write_text(ms)
status=json.loads((lane/'STATUS.json').read_text())
status.update(source_bridge_reader='ns_bridge/source_bridge_reader.pdf',
 source_bridge_reader_pages=15,source_bridge_registered_checks=46,
 source_bridge_pdf_sha256=pdf,source_bridge_prefixed_body_sha256=body,
 source_bridge_pulse_pdf_sha256=sha(root/'pulse_comparison/pulse_comparison.pdf'),
 source_bridge_pulse_tex_sha256=sha(root/'pulse_comparison/pulse_comparison.tex'),
 source_bridge_finite_composite_proved=True,source_bridge_full_flow_reflection_proved=True,
 source_bridge_scope=scope+' '+limits,source_bridge_verified=True,
 source_bridge_revision_equations_checked=31,
 source_bridge_new_pdf_sha256='0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f',
 active_work=nextwork)
(lane/'STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
cont=(lane/'CONTINUATION.md').read_text()
a=cont.index('Newest parent steering')
b=cont.index('\n\nAll previously',a)
new=("Newest parent steering preserves the current finite-stage result and requires its exact "
"connection to the supplied NS profiles/pulses before further auxiliary expansion. Parent "
"owns all full-paper audit scopes, cumulative TeX, publication and Overleaf. This lane has "
"now completed the 15-page signed source bridge at ns_bridge/source_bridge_reader.pdf "
f"(SHA256 {pdf}), with {build['prefixed_labels']} prefixed integration labels and46 registered exact checks. "
"All28 rendered pages across the four bridge readers were inspected; final rebuild pixels "
"match the inspected pages. "+scope+" "+limits+"\n\n"+nextwork+
" Both 165/166-page source hashes and31-equation bounded revision comparisons are in "
"ns_bridge/HANDOFF.md and revision_check/REPORT.md. Old draft pulse/covariance notes "
"were corrected and superseded; use the current build/visual receipts and exported full body.")
(lane/'CONTINUATION.md').write_text(cont[:a]+new+cont[b:])
for name in ['HANDOFF.md','README.md']:
    p=lane/name;s=p.read_text()
    marker='## Current finite signed source bridge'
    if marker in s:s=s[:s.index(marker)]
    s+=('\n\n'+marker+'\n\n'+f'The separate complete15-page reader is ns_bridge/source_bridge_reader.pdf '
        f'(SHA256 {pdf}); the parent-ready full TeX is ns_bridge/integration/'
        f'source_bridge_complete_body_prefixed.tex (SHA256 {body}). '
        'It has46 registered checks, clean builds and full visual review. '
        +scope+' '+limits+' Current exact handoff: ns_bridge/HANDOFF.md.\n')
    p.write_text(s)
ap=lane/'ACTIVE_GOAL.md'
with ap.open('a') as f:
    f.write('\n\nCurrent signed-source continuation: the complete15-page finite composite bridge '
            'is saved and verified in ns_bridge/. The full assignment is unfinished; the goal '
            'tool objective was not replaced or marked complete. '+nextwork+'\n')
receipt=dict(schema='bridge-handoff-v1',verified=True,reader_pdf_sha256=pdf,
             prefixed_body_sha256=body,registered_checks=46,
             root_stage_reader_unchanged=sha(lane/'coupled_viscous_control.pdf')==
             'f74103eee85b3ba41dc8a746e3a97953bb5dfd31b053fa08e7a247c9f5c57d0f',
             build_receipt_sha256=sha(root/'build_receipt.json'),
             visual_receipt_sha256=sha(root/'qa_final/visual_review.json'))
assert receipt['root_stage_reader_unchanged']
(root/'handoff_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
