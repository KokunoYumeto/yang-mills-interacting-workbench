# Navier–Stokes: what was tried and where the work stands

**9 September 2026.** [Read the corrected 208-page reconstruction](navier_stokes_workbench_208p.pdf), [open the complete source archive](../navier_stokes_source_bundle.zip), or [inspect the structured research state](research-state.json). The permanent corrected edition is [10.5281/zenodo.22678406](https://doi.org/10.5281/zenodo.22678406).

## Purpose and route

[Short accounts of the reconstruction attempts](../ATTEMPTS.md#ns-primary) · [Fluid source and analytical audits](../ATTEMPTS.md#ns-source-audit) · [Coupled viscous stages](../ATTEMPTS.md#ns-coupled-stages)

The purpose is to make the supplied finite-time Navier–Stokes construction understandable and reusable through complete derivations, original coordinates and reproducible calculations. The programme initially investigated transfers from algebraic, S6-related and heat-flow constructions into fluid equations. Those directions motivated the research; their proposed implications are not certified by this reader. The arrival of the released Navier–Stokes manuscript redirected the main work toward reconstructing its explicit construction with the stated viscosity, initial data, forcing, pressure and nonlinear terms.

The primary manuscript and formal source are identified in the [published manifest](../navier_stokes_primary_manifest.json). The derivation used a 165-page capture; a later 166-page capture and its revision audit are recorded separately. The [component index](research-state.json) preserves the capture hashes, formal repository revision and source-page ranges where known. Authorship remains with the cited sources; reconstruction and checking retain their own provenance.

## Full calculation bodies

The source ZIP has 120 members. Each row below identifies an entire source body in that archive. The JSON index supplies its SHA-256 and associated checker where one was recorded. These entry points supplement the complete reader and source; they do not replace the mathematical statements or proofs.

| Component | Reading purpose | Exact path inside the ZIP |
| --- | --- | --- |
| NS-profiles | Coordinate and leading-profile maps | `proof_sources/profiles/profiles_body.tex` |
| NS-base_heat | Base field and heat correction | `proof_sources/base_heat/derivation.tex` |
| NS-oscillations | Oscillatory velocity and stress | `proof_sources/oscillations/oscillations_body.tex` |
| NS-mean_corrections | Mean corrections | `proof_sources/mean_corrections/mean_corrections_body.tex` |
| NS-stage9 | Finite-stage correction cycle | `proof_sources/stage9/stage9_body.tex` |
| NS-terminal_endpoint | Localization, comparison and periodization | `proof_sources/terminal_endpoint/endpoint_derivation.tex` |
| NS-profile_assembly | Profile assembly review | `proof_sources/profile_assembly_audit/profile_assembly_body.tex` |
| NS-stage_inputs | Initial stage and pulse inputs | `proof_sources/stage_inputs_audit/stage_inputs_body.tex` |
| NS-summation_realization | Summation and realization analysis | `proof_sources/primary_continuation/summation_realization_body.tex` |
| NS-terminal_trace | Terminal trace calculations | `proof_sources/primary_continuation/terminal_trace_body.tex` |
| NS-radial_stress_reconstruction_audit | Radial stress reconstruction | `proof_sources/lanes/web_bundle_audit/tex_handoff/portable_upstream/radial_stress_reconstruction_audit.tex` |
| NS-stage_cycle_gain_audit | Correction-cycle gain calculations | `proof_sources/lanes/web_bundle_audit/tex_handoff/portable_upstream/stage_cycle_gain_audit.tex` |
| NS-global_closure_body | Global assembly analysis | `proof_sources/global_analytic_closure_review/global_closure_body.tex` |

## Corrections and recorded checks

The corrected edition follows the archived [162-page edition](https://doi.org/10.5281/zenodo.22667379). It restores the actual-shear remainder and the corresponding positive-production bounds, retains the polynomial factors in radial transport derivatives, and makes the plane-coordinate inverse and its domain explicit. The full correction calculations appear in the reader and the source bodies above. The earlier edition remains available with its original identity.

The [published check record](../navier_stokes_checks.json) records nine replay programs, 144 named result groups and twelve structural probes. The source manifest also retains static formal-source and declaration comparisons. These are the recorded scopes of those checks. This organizational update verified artifact identities and all 120 archive-member digests; it did not rerun the mathematics or produce a new independent review.

Raw Git JSON and check blobs match the corresponding corrected Zenodo files. A Windows checkout can convert LF to CRLF and consequently have a different local hash; this does not indicate a difference between the published objects. The [release map](../releases/2026-09-09/) records the filenames and archive correspondence.

## Where the work was left

Complete independent analytical and formal validation remains unfinished. The recorded unfinished work includes imported profile and admissible-stress existence, all-stage realization and convergence, the final forcing for the same assembled witness, and a completed formal endpoint and Comparator certificate. The frozen edition records these investigations as in progress. The later local formal run stopped without that endpoint certificate or Comparator result. No new formal run was started for this publication update.

This state records the actual outcome and makes the full work available for reuse. It creates no compulsory continuation queue. The [related zeta workbench](https://github.com/KokunoYumeto/zeta-function-research-reader) and [PolyClank proposal](../docs/polyclank/README.md) provide routes to related research and future independent contributions, with each source version and mathematical map retained.

The reconstruction makes no prize or discovery-priority claim. Recurring mirror work is paused after the current publication update at the owner's request; the public edition and Overleaf reader remain available.

[Whole-workbench reading map](../WORKBENCH.md) · [Topic overview](README.md) · [Research log](../RESEARCH_LOG.md)
