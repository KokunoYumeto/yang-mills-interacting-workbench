"""Record completed verification after actual visual inspection, without editing proofs."""
from pathlib import Path
import hashlib
import json

HERE = Path(__file__).resolve().parent
receipt_path = HERE/'verification_receipt.json'
receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
body = HERE/'third_growth_spatial_body.tex'
assert hashlib.sha256(body.read_bytes()).hexdigest() == receipt['body_sha256']
assert not receipt['component_latex_warnings']
assert not receipt['component_text_out_of_page']
receipt['visual_review'] = {
    'status':'passed', 'reviewer':'third_spatial_finish',
    'pages':list(range(58,65)),
    'method':'Inspected all final Poppler page renders in four two-page contact sheets after grouping the opening PDE pair; no clipping, overlap, bad equation breaks, or illegible glyphs.',
    'earlier_reader_scope':'Earlier pages are compilation context; full parent-release QA belongs to the parent.',
}
receipt['dependency_sha256'] = {str(p.relative_to(HERE.parent)).replace('\\','/'):
                               hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in [HERE.parent/'finite_stage/third_growth_entry.tex',
                                         HERE.parent/'modified_spatial/modified_spatial_body.tex']}
receipt_path.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
handoff = f'''# Complete third-growth spatial handoff

The completed component is `third_growth_spatial_body.tex`. Include it after the actual third-growth entry theorem and the existing modified-spatial definitions. It has {receipt['component_label_count']} unique `tgs:` labels. No new mathematical preamble is needed beyond the current root packages. One direct `\\hyperref[tge:nesting]` target must receive the `cvlane:` prefix in the flattened export; the parent has been notified that the earlier exporter handled only brace-form references.

The proof uses the actual evolving second hold, the exact relative material flow `M3=M2(t) M2(tb)^(-1)`, the original radii and profiles, and the actual original third threshold. It gives the complete scalar and full vector residuals at pressure zero, all ordered interactions with the base and both parent waves, every spatial derivative and mixed derivative cost, exact cutoff/metric correspondence, and retained affine-core damping. The primitive constant P(0) remains in the compact fields. The second temperature acts on the third wave even though the second velocity is zero.

The full source support nesting follows from the root's explicit source family. Matrix and inverse norms are at most 145 throughout the proved growth horizon. The phase square is between 1 and 2, the newest temperature is at most its original target before crossing, and the full velocity amplitude estimate retains K3/sigma2. The older amplitude equations are all written locally so the mixed-jet recursion is closed.

The endpoint is the actual third growth threshold, with activation complete and negative newest vorticity. No third transition, steering, return, or infinite iteration is asserted. The force collar uses the explicit length 1/sigma1 within the proved remaining growth horizon and the explicit larger amplitude bound exp(3 Gamma3/sigma1) times the target. The endpoint fields continue by their actual ODE; only the residual forces receive a compact time cutoff.

Validation:

- `replay_third_spatial.py` is self-contained. All {receipt['replay_check_count']} exact SymPy/rational checks passed in `replay_report.json`. These include general profile/envelope jets, exact original-parameter third-flow/inverse/phase identities, full four-field interaction telescoping, primitive-constant cutoff terms, and physical diffusion powers. Written analytic proofs establish the interval, support, and norm inequalities.
- `audit/AUDIT.md` records the earlier independent spatial/support proof. `audit/final_review.md` independently checks the completed equations, coefficient/norm bounds and explicit collar, including four further read-only symbolic identities.
- A cumulative verification reader was built in `audit/preview_build/preview.pdf`; the new component occupies pages 58--64. All seven final pages were rendered with Poppler at 90 dpi and personally inspected. Final reader warnings, new component overflowing boxes, and text out-of-page defects are zero. `verification_receipt.json` records hashes and scope.
- The preview is a local verification artifact, not a replacement for the parent master or a claim of completed parent integration. No parent source, goal, remote object, Lean/Lake/Elan session, or original public source was modified by this finishing agent.

Final body SHA-256: `{receipt['body_sha256']}`.
Replay SHA-256: `{receipt['replay_script_sha256']}`.
Verification-reader SHA-256: `{receipt['reader_sha256']}`.

Reproduce algebra with Python and SymPy by running `replay_third_spatial.py`. `prepare_verification.py` regenerates the self-contained replay from the earlier generic proof checks and the recorded third-specific checks, and prepares the cumulative verification TeX. It reads earlier lane files but writes only this directory. Compile `audit/preview.tex` from the lane directory with the output directory set to `third_growth_spatial/audit/preview_build`; the parent may instead integrate the complete component directly and run its normal cumulative build.
'''
(HERE/'HANDOFF.md').write_text(handoff,encoding='utf-8')
with (HERE/'LOGBOOK.md').open('a',encoding='utf-8') as log:
    log.write(f'\nFinal verification: body {receipt["body_sha256"]}, {receipt["replay_check_count"]} exact replay checks passed, 33 component labels, final reader pages 58--64 rendered and visually inspected. Zero final LaTeX warnings and text-out-of-page defects. Independent review found no mathematical defect; its complete local older equations and explicit collar were checked. The parent repaired the earlier entry section displays during this build. A bracket-form hyperref prefix requirement was sent to the parent for full export. Complete handoff saved in HANDOFF.md. Workflow repair: this newly created handoff helper was initially placed one directory too high; it was immediately moved into the owned component directory before execution, without replacing or editing an existing parent file. All resulting files are within the owned directory.\n')
print(json.dumps({'status':'complete bounded component', 'body_sha256':receipt['body_sha256'],
                  'checks':receipt['replay_check_count'], 'labels':receipt['component_label_count']}))
