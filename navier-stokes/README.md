# Navier–Stokes: corrected reconstruction and validation reader

**Read or download the complete source here.** This workbench now contains the [editable LaTeX](sources/openai-source-faithful-20260920/upstream/reconstruction/), [checked 166-page PDF](sources/openai-source-faithful-20260920/upstream/output/pdf/source-faithful-reconstruction.pdf), and [complete source ZIP](sources/openai-source-faithful-20260920/full-source-release.zip), including figures and verification records. The [build and reading guide](sources/openai-source-faithful-20260920/) explains the preserved copy of release `5e162f34`. This is an independent source-faithful reconstruction, not official OpenAI source and not the 208-page analytical reader below. Its page and formula records concern transcription fidelity, not an independent proof of the mathematics. The [pinned source record](SOURCE_READING_20260920.json) identifies the official PDF, reconstruction revision and verification scope.

Permanent archive of the 166-page source edition, including its editable LaTeX: [10.5281/zenodo.22852310](https://doi.org/10.5281/zenodo.22852310).

## Everyday English: a working comparison

This page-3 example shows an attempt to make the paper's reasoning explicit in everyday prose. Both passages are retained for comparison. The second passage is a working draft, not the finished edition; preliminary feedback on its wording is not a final check of the whole paragraph.

**Original, page 3** ([source LaTeX](sources/openai-source-faithful-20260920/upstream/reconstruction/sections/pp001-006.tex)):

> For any incompressible flow u and pressure p, we can always define the external force f to be the residual in (1.1). The Navier–Stokes equations then hold by construction. The challenge is to choose a flow that blows up while this residual remains smooth. The individual terms in the momentum residual can diverge, but we must arrange sufficient cancellation that their sum and all its derivatives extend smoothly through the singular time.

**Current Everyday English version, 20 September 2026:**

> For any incompressible flow u and pressure p, the external force f can always be set equal to the residual in (1.1), the result of adding up the four terms on its left-hand side. The Navier–Stokes equations then hold by construction, because the force was chosen to equal that result. The hard part is choosing a flow that blows up while this residual stays smooth. The separate terms in this residual from the momentum equation can each become unbounded. Their unbounded parts have to cancel one another so that their sum, and every derivative of that sum, still extends smoothly through the singular time, the time when the velocity becomes unbounded.

## Research continuations and analytical reader

[Vacuum hydrodynamics continuation, 19 September 2026](continuations/20260919-vacuum-hydrodynamics/README.md): exact nonlinear Einstein constraint data with a complete-velocity decoder; the Rindler shear response and finite pole-cluster cancellation; and a separate positive-stress regularity theorem. The continuation retains its source hypotheses and distinguishes exact identities, numerical results and imported NS claims.

[What was tried and where it stands](RESEARCH_STATE.md) · [Machine-readable component map](research-state.json) · [Read in Overleaf](https://www.overleaf.com/read/hzthvczhdyxc#a60fc2)

[What was tried and where it stands](RESEARCH_STATE.md) · [Machine-readable component map](research-state.json)

[Read the 208-page PDF](../navier_stokes_workbench_208p.pdf) · [Standalone LaTeX](../navier_stokes_workbench.tex) · [Complete source ZIP](../navier_stokes_source_bundle.zip)

This 9 September 2026 edition reconstructs and examines the supplied finite-time blowup construction with positive viscosity, zero initial velocity and smooth compactly supported forcing. It retains the original forcing, pressure, transport, nonlinear terms and correction-cycle calculations. The corrected edition restores the actual-shear remainder and its positive-production bounds, retains radial transport derivative factors, and makes the moving-plane projection explicit.

The [structured proof/source manifest](../navier_stokes_primary_manifest.json) and [recorded checks](../navier_stokes_checks.json) accompany the reader. The original construction is attributed to the primary paper and formal repository cited in those files. The complete independent analytic and Lean validation remains unfinished; this collection is a reconstruction and verification workbench, not a claim of discovery or a completed independent certificate.

Permanent corrected edition: [10.5281/zenodo.22678406](https://doi.org/10.5281/zenodo.22678406). The [earlier 162-page edition](https://doi.org/10.5281/zenodo.22667379) remains unchanged and is preserved in the corrected record. The [publication family](https://doi.org/10.5281/zenodo.22667378) resolves to its latest edition.

The GitHub PDF, TeX, source ZIP and check files are byte-identical to their matching corrected Zenodo artifacts; the [release map](../releases/2026-09-09/) records the differently named aliases.

[All topics](../README.md) · [Yang–Mills maps](../yang-mills/) · [S6 topology](../s6/)
