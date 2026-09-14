# Research state and publication history

## Current checkpoint — 9 September 2026

**Purpose of this update.** Make the existing work readable and reusable across independent workbenches, from a single checked calculation to a large programme. Preserve the mathematics, expose current readers and sources, and record what was done rather than impose a successor's research plan.

**Mathematical source checkpoint.** Commit [e0a04c0](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/commit/e0a04c078eaf0209e40b3d47d6f6dffb3f2a3e7f) supplied the three current topic trees and published edition links. The subsequent PolyClank integration changes navigation and metadata, not mathematical source/PDF/archive contents.

**What is available.** [WORKBENCH.md](WORKBENCH.md) describes the three programmes and the scope of the released material. [workbench.json](workbench.json) fingerprints the public tracked artifacts and points to exact Zenodo editions. The [release map](releases/2026-09-09/) relates repository and archival names. Existing mathematical statements and reported checks remain attributed to their sources; this update adds no mathematical validation mark.

**What was corrected in the navigation.** The earlier map described the 22-file root snapshot at ed8cb4b. It now points to the 79-page quantum reader, 81-page volume reader, organized source trees, S6 collection, and corrected Navier–Stokes DOI. The old PK7/PK10 follow-up is not reissued as an outstanding assignment: the current spatial guide identifies the corrected oscillator rates in §26.13. A full review of the resulting analytic implications was not performed in this publishing pass.

**Evidence of this pass.** The recorded checks concern repository links, descriptor structure, artifact byte identities and public publication metadata. They do not replay Lean, rerun the mathematical checkers, establish novelty or certify the underlying theorems.

**What remains incomplete.** The workbench descriptor is a static artifact catalogue, not an exhaustive theorem/dependency database. Networking, registrars, signatures and offline peer reconciliation are documented proposals, not a deployed federation. No new worker is automatically authorized by these files. The Navier–Stokes task has now supplied its [current research state](navier-stokes/RESEARCH_STATE.md) and [13-component source index](navier-stokes/research-state.json), including the stopped formal run and unfinished independent validation. This resolves the missing descriptive source handoff; it adds no new mathematical certificate.

**Continuation.** Readers and contributors choose their own directions from the evidence. No fixed next-calculation queue is part of this checkpoint. The owner's recurring publication maintenance is paused; public reading, downloads and contributions remain available.

## Navier–Stokes contribution to the same checkpoint

The reconstruction task added its research history, the exact paths and hashes of 13 full source bodies in the 120-member archive, current Overleaf reading access and the recorded endpoint status. It verified all 120 member digests and the 284 raw source objects at e0a04c0. Published mathematical replay records were not rerun. The original 22-file descriptor is retained at [its historical snapshot](releases/2026-09-09/workbench_ed8cb4b.json).

The source handoff was prepared concurrently with the shared PolyClank integration. The merged result preserves the shared staged-blob catalogue generator and contribution guide, with the new Navier–Stokes documents included in its current inventory. This records both contributions without replacing either participant's mathematical work.

## Provenance of the two proposals

[PR #1](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/pull/1) proposed the human workbench map, machine inventory, research log and scoped review guide from source commit ed8cb4bee090d8f7cc14166199aebdef557d066e. That snapshot remains accessible through Git history. Its artifact aliases are retained when their paths still identify the same public files; hashes identify the actual file revisions.

[PR #3](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/pull/3) proposed networking, programme-state, problem-catalogue and publication documentation. The integration retains its workbench-first design while updating source pointers and removing permission to normalize mathematical data. No local instruction file was replaced.

Private conversation exports, user logbooks, credentials and downloaded literature bodies are not included. This is a public account of work performed, not a publication of the private session.

## Continuation — 14 September 2026: continuum spectral reconstruction

A new additive continuation is recorded at [`yang-mills/continuations/20260914-spectral-reconstruction/`](yang-mills/continuations/20260914-spectral-reconstruction/). It extends the retained positive-time Yang–Mills correlation and Schur-memory programme from finite trial frames to a countable gauge-invariant spin-network/cylindrical family along one regulator subsequence.

The continuation constructs the resulting positive self-adjoint observable-sector generator from the limiting correlation kernel, proves that its spectrum is the closure of the union of the diagonal spectral supports, gives an explicit Bernstein/Hausdorff moment reconstruction of the complete finite-energy matrix spectral measure from the values `C(mh)` and `C(0+)`, records Stieltjes inversion formulas for interval masses and atoms, and identifies the spectral bottom with the infimum of the exact large-time exponential decay edges. The compactified energy-infinity matrix remains retained separately as the zero-time Gram defect.

The smooth-frame step is written with an explicit inverse congruence `mu(B)=T^{-*} mu^T(B) T^{-1}` and keeps raw Gram matrices. Its construction is informed by the explicit mutually inverse S6 smooth normal-line trivialization, while the Yang–Mills spectral statements are proved directly in their own typed spaces. The accompanying exact checker verifies the Bernstein-moment coordinate identity and inverse raw-frame congruence on rational matrix fixtures.

This continuation does not assert construction of the full four-dimensional Yang–Mills theory or a positive continuum mass gap. It concentrates the remaining spectral question into the lower support edge of the reconstructed countable gauge-invariant continuum measures and the identification of that observable-sector reconstruction with the Hilbert space required by the target theorem.
