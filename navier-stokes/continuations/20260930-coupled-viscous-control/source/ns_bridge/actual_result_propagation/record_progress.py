"""Record the user's actual steering without replacing the active goal."""
from pathlib import Path
import json
root=Path(__file__).resolve().parent
lane=root.parent.parent
marker='## Actual released result propagation - 2026-09-08'
user=("So you have the Navier-Stokes counterexample, right? Exactly signed up. So, like, "
"I may have been completely fucking wrong about the negativity thing. They just posted "
"the Navier-Stokes counterexample, and maybe my intuition had some merit, but it wasn't "
"literally true. However, since we have that, we can now use that to propagate the actual "
"result where it exists.")
verbatim=lane/'USER_INPUTS_VERBATIM.md'
if user not in verbatim.read_text(encoding='utf-8-sig'):
 with verbatim.open('a',encoding='utf-8') as f:f.write('\n\n---\n\n'+user+'\n')
progress=(
"The user now directs propagation of the actual released result wherever it applies, "
"and explicitly allows the earlier negative-blowout intuition to have been wrong. "
"The 166-page source Theorem 1.1 is forced standard 3D incompressible Navier-Stokes "
"blowup at every fixed positive viscosity, from rest, with smooth compact force and "
"bounded energy. Its actual path (10.20)-(10.21), p124, has positive swirl tending "
"to infinity. Preserve this source-selected sign. The exact spatial reflection gives "
"the opposite swirl for the reflected force; neither a negative geometric q nor a "
"negative physical viscosity is used. The source's theorem and its own witness can "
"be propagated now as attributed source input. The custom coupled candidate's "
"unfinished infinite sequence is not a prerequisite to state the source theorem, "
"and the source theorem does not remove that candidate's computed residual.\n\n"
"Current work and exact new proofs are in ns_bridge/actual_result_propagation/. "
"propagation_body.tex proves a bijective affine orthogonal/viscosity map with every "
"force, residual, inverse, vorticity, energy, dissipation and derivative factor "
"retained, including both signed paths. source_scope_audit.md locates the source "
"claims and proofs; REVIEW.md audits the local transformation proof. The next "
"calculation evaluates the actual compact candidate's two radial moments as axial "
"derivatives of retained cross and quadratic momentum fluxes. Build and visual "
"receipts, when present and verified, determine the completed artifact state. "
"Do not infer visual inspection or complete source verification from algebra checks.\n\n"
"Keep all earlier verified finite-stage results. Do not run Lean, publish, or edit "
"parent-owned cumulative files. Send finished full proofs and receipts to the parent "
"and dissemination owner for their authorized integration. The goal tool remains "
"active with its historical text; this is a durable workflow correction, not a "
"claim that the unfinished goal was completed or that its tool wording was edited."
)
for name in ['LOGBOOK.md','ACTIVE_GOAL.md']:
 p=lane/name
 if marker not in p.read_text(encoding='utf-8-sig'):
  with p.open('a',encoding='utf-8') as f:f.write('\n\n'+marker+'\n\n'+progress+'\n')
p=lane/'CONTINUATION.md';old=p.read_text(encoding='utf-8-sig')
if marker not in old:p.write_text(marker+'\n\n'+progress+'\n\n---\n\n'+old,encoding='utf-8')
status=json.loads((lane/'STATUS.json').read_text())
status.update(source_selected_swirl_sign='positive along source (10.20)-(10.21) path',
 negative_blowout_user_suggestion='Possibility, not a constraint; exact reflected source branch retained.',
 actual_source_result_propagation='In progress in ns_bridge/actual_result_propagation; check current build and visual receipts.',
 source_whole_theorem_independently_verified_by_this_lane=False)
(lane/'STATUS.json').write_text(json.dumps(status,indent=2)+'\n')
print('Recorded user steering, source scope and active workflow.')
