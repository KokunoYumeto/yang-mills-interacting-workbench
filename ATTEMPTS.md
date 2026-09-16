# What we tried, why, and where it was left

**9 September 2026.** These short accounts explain the research routes behind the workbench: the broader aim, the reason to try each approach, what happened, how far it worked, and what remains unfinished. The linked full sources contain the mathematics. Results here are the recorded results of those sources; this editorial update adds no mathematical verification.

A rationale reconstructed from a source is labeled as such. A partial result, a specific obstruction and an unfinished calculation retain their different meanings. These accounts describe the work and leave future researchers free to choose their own direction.

**Reading key.** Source result = stated by the cited artifact; reconstructed rationale = recovered from a handoff; independent check = replayed or audited in this workbench; unresolved = the endpoint was not obtained.

[Machine-readable accounts](research-attempts.json) · [Full workbench map](WORKBENCH.md) · [Convention for maintaining these accounts](docs/polyclank/RESEARCH_STATE.md)

[Navier–Stokes reconstruction](#ns-primary) · [Fluid source and analytical audits](#ns-source-audit) · [Coupled growth and viscous stages](#ns-coupled-stages) · [Yang–Mills states, interactions and limits](#ym-attempts) · [Erdős–Straus arithmetic routes](#es-attempts) · [S6 geometry and marked lattice constructions](#s6-attempts) · [Zeta and arithmetic transport routes](#zeta-attempts)

<a id="ns-primary"></a>

## Navier–Stokes reconstruction

**Source:** OpenAI FINITE TIME BLOWUP FOR NAVIER–STOKES (2026-09-08 / formal companion 8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538). Reconstruct and audit OpenAI's public 8 September 2026 Navier–Stokes release, FINITE TIME BLOWUP FOR NAVIER–STOKES (165-page manuscript; formal companion pinned at openai/NavierStokesAndEuler@8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538). The source claims a classical 3D forced Navier–Stokes solution with positive viscosity, zero initial velocity, smooth compactly supported forcing, bounded kinetic energy, and a terminal unbounded-velocity event; this account records reconstruction status, not independent certification. The concrete source sequence is: leading profiles (manuscript §4 and App. B), base/heat correction (§5 and App. A), oscillatory velocity/shear fields (§§6–7 and App. C), mean corrections (§8), finite correction cycle (§9), and endpoint/localization (§10). Naming those objects lets the reader distinguish what was reconstructed from what remains unverified.

<a id="ns-reconstruct-source"></a>

### Reconstruct OpenAI's FINITE TIME BLOWUP FOR NAVIER–STOKES stage sequence

We reconstructed the named OpenAI manuscript's sequence: leading profiles (§4/App. B), base and heat correction (§5/App. A), oscillatory velocity/shear fields (§§6–7/App. C), mean correction (§8), finite cycle (§9), and endpoint/localization (§10). The result is the corrected 208-page reader plus 13 complete component bodies and finite checks. That makes the source inspectable; it does not independently verify the assembled infinite construction.

[Purpose and route; Full calculation bodies; Where the work was left](navier-stokes/RESEARCH_STATE.md)

<a id="ns-actual-shear-repair"></a>

### Retain the actual shear and repair the pulse calculation

We checked the OpenAI manuscript's actual varying shear in the oscillatory velocity stage, because dropping its remainder changes the production estimate. Retaining the remainder produced corrected production bounds, transport derivatives, and an explicit plane-coordinate inverse in the reader. These local repairs do not certify the manuscript's full cycle or endpoint.

[Corrections and recorded checks](navier-stokes/RESEARCH_STATE.md) · [Complete corrected source bodies and provenance](navier_stokes_primary_manifest.json)

<a id="ns-formal-endpoint"></a>

### Check the formal endpoint against the stated problem

We ran the formal companion openai/NavierStokesAndEuler@8937a8f4cbc7abaab5e9e97d1cc7f5d2319d9538 against its stated endpoint and Comparator target. Source/import inspection and a coordinated compilation attempt stopped before an endpoint or Comparator certificate. The formal route is paused and unfinished.

[formal_source; current_formal_run_status; NS-INDEPENDENT-VALIDATION](navier-stokes/research-state.json) · [Where the work was left](navier-stokes/RESEARCH_STATE.md)

<a id="ns-source-audit"></a>

## Fluid source and analytical audits

**Source:** fluid_blowup_reconstruction.zip, 40-page reconstruction report (2026-09-09 local audit; public bundle navier-stokes_source_bundle.zip). Audit the 40-page fluid-blowup reconstruction report in fluid_blowup_reconstruction.zip and its named Boussinesq, CKN, rational-cylinder, IPM, and moving-centre constructions against the incompressible Navier–Stokes target. The bundle is a local handoff of explicit formulas, not a theorem by itself. We tested each proposed transfer by preserving coordinates, divergence, pressure, force, viscosity, and energy terms, so a successful local identity is not silently promoted to a global singularity proof.

These accounts report the retained local task handoffs. Exact public counterparts for these later calculations have not yet been verified in this index; they are not silently assigned to the earlier 208-page archived reader.

<a id="ns-incoming-fluid-bundle-audit"></a>

### Audit the 40-page fluid_blowup_reconstruction.zip report

We audited the 40-page fluid_blowup_reconstruction.zip report, reading its Boussinesq, CKN, rational-cylinder, IPM, and moving-centre maps. The bounded audit repaired omitted scales, coefficients, pressure terms, and force residuals and produced complete local proof fragments. It neither certifies the report nor proves a classical Navier–Stokes singularity.

[Public source bundle; Boussinesq/CKN/rational-cylinder/IPM/moving-centre payloads](navier-stokes/navier_stokes_source_bundle.zip)

<a id="ns-solenoidal-arithmetic-heat"></a>

### Test the report's arithmetic heat map in divergence-free velocity space

We tested the report's arithmetic heat map as a map into divergence-free velocity fields. Its componentwise range had no nonzero solenoidal field, so we constructed the solenoidal isometry, inverse, complement, and the nonlinear, pressure, forcing, and energy terms. The six-channel image has zero averaged swirl; no Navier–Stokes singularity or zeta-zero conclusion follows.

[Arithmetic heat map, solenoidal correction, angular-momentum audit](navier-stokes/RESEARCH_STATE.md)

<a id="ns-comparison-analytic-foundations"></a>

### Replay the Sobolev, Riesz, pressure, and H3 closure checks

We made the comparison's named Sobolev, pressure, and H3 inputs explicit: cutoff Sobolev estimate and norm dictionary, ordered double-Riesz estimate, and H3 approximation, time, pressure, and energy identities. Review repaired a missing cutoff derivative and initial-energy omission. These bounded foundations do not certify the OpenAI manuscript or its global endpoint.

[Sobolev, Riesz, H3, pressure and energy closure review](navier-stokes/RESEARCH_STATE.md)

<a id="ns-coupled-stages"></a>

## Coupled growth and viscous stages

**Source:** coupled viscous Boussinesq stages and finite pulse bridge (2026-09-09 handoff set; finite-stage and pulse-bridge readers). Track the coupled Boussinesq growth/transition/steering/holding system with physical viscosity, then compare its finite pulse to the OpenAI manuscript's profile/shear stages. The question was whether the finite viscous mechanism survives diffusion and whether its pulse can be mapped into the released Navier–Stokes construction. The finite stages and comparison maps are separate objects; the unfinished third return and infinite endpoint are recorded as such.

These accounts report the retained local task handoffs. Exact public counterparts for these later calculations have not yet been verified in this index; they are not silently assigned to the earlier 208-page archived reader.

<a id="ns-coupled-finite-viscous-stages"></a>

### Continue the coupled Boussinesq stages with physical viscosity

We evolved the coupled Boussinesq growth, transition, steering, and holding stages with physical diffusion. Exact determinant and numerator identities enabled direct shooting; the first two targets, second return, and the third growth/transition/initial-steering interval were completed with compact fields and forces. The third return, a fixed-positive-diffusion infinite sequence, and smooth terminal forcing remain unproved.

[Finite viscous stages, return status, diffusion and continuation boundary](navier-stokes/RESEARCH_STATE.md)

<a id="ns-coupled-source-pulse-bridge"></a>

### Compare the finite viscous pulse with OpenAI's Navier–Stokes profile/shear stages

We compared those finite viscous Boussinesq stages with the OpenAI manuscript's profile and pulse stages. Cylindrical operator maps, a moving tangent frame, a finite-interval intertwiner, compact curl, pressure, and full momentum residual were reconstructed; frame and covariance defects were corrected. The finite bridge is complete, but no uniform endpoint estimate transfers to the distinct candidate.

[Finite pulse comparison, curl/pressure/residual calculations](navier-stokes/navier_stokes_workbench.tex)

<a id="ns-radial-moment-finite-class"></a>

### Reduce the finite pulse residual to radial moments and stress

We controlled the residual left by that pulse comparison using its computed axial flux moments and the source's moment/mean-velocity correction operations. Shifted pressure, radial moments, compact symmetric stress, five-row velocity inverse, and fixed-band derivative costs were obtained. A stress representation is not a correcting velocity or wave covariance; increasing-band uniformity and infinite iteration remain unfinished.

[Radial moments, stress and fixed-band correction material](navier-stokes/navier_stokes_workbench.tex)

<a id="ym-attempts"></a>

## Yang–Mills states, interactions and limits

**Source:** Yang–Mills interacting workbench source edition (2026-09-09 / source revision 8dc1a52). Test the selected 9 September 2026 Yang–Mills source edition's explicit finite-box interacting system against quantum blocking, nonabelian interaction, vacuum, and continuum-limit requirements. Each route names the finite-box or lattice object it actually computes. The results concern selected channels, fixed boxes, or specified paths; they do not by themselves establish a four-dimensional mass gap.

<a id="ym-quantum-blocking"></a>

### Quantum coarse-graining with retained memory

We repeatedly blocked the finite-box/lattice Yang–Mills system while retaining an explicit memory term for eliminated variables. Path maps, vacuum integrations, and Schur complements gave associative reconstruction and volume-independent bounds for selected Wilson-loop channels. Those channels retain high-energy weight; the calculation does not determine every lowest-energy state or the continuum mass gap.

[Exact memory, resolvent reconstruction, and physical norms](yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/extensive_quantum_blocking.md)

<a id="ym-nonabelian-vertex"></a>

### Recovering a nonabelian interaction beyond the free comparison

We expanded the original kinetic and plaquette terms on the L=2 finite box to see whether the nonabelian interaction survives the free comparison. The physical cubic vertex is nonzero, with fixed-box vacuum and covariance responses. Survival through simultaneous spatial, coupling, and time limits remains unfinished.

[Opening scope statement](yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/nonabelian_vertex_publication_20260909/NONABELIAN_VERTEX.md)

<a id="ym-interacting-tensor-band"></a>

### Mapping the material tensor into the interacting first band

We mapped the material tensor into the interacting first excitation band using the retained Gram matrix, intermediate modes, and six-coordinate map. At each fixed box and sufficiently small positive coupling the map is onto and reaches three symmetry channels. The three coefficient evaluations and simultaneous limits remain unfinished.

[Opening scope statement](yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/interacting_band_publication_20260909/INTERACTING_TENSOR_BAND.md)

<a id="ym-volume-uniform-vacuum"></a>

### Local estimates that survive growth of the spatial box

We tested local vacuum and covariance estimates as the finite spatial box grows. Local projections, cluster coordinates, and covariance estimates give explicit coupling intervals and a finite-box window at every positive coupling. The certified endpoint diverges along the logarithmic path, so no fixed-energy spectral weight is established.

[2. A local projection and an exact comparison operator](yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md)

<a id="ym-spatial-limit-routes"></a>

### Testing candidate states through the spatial limit

We compared native magnetic states, electric covariances, and radial observables along specified lattice-refinement and finite-box sequences. Some selected native sequences lose finite-energy weight even as the gap closes. The prescribed exact-lattice limits and a surviving interacting continuum remain unresolved.

[1. Objects and scope of the calculation](yang-mills/sources/ym_spatial_continuum_astra_20260908/spatial_continuum.md)

<a id="es-attempts"></a>

## Erdős–Straus arithmetic routes

**Source:** Erdős–Straus arithmetic source edition (2026-09-09 / source revision ead4c88). Study the Erdős–Straus conjecture—every integer n>1 is a sum of three positive unit fractions—while retaining the original factor, exponent, congruence, and boundedness data. The route tests whether exact divisor shells and transport maps can force a bounded Egyptian-fraction witness. Structural maps and finite fibres are useful even where universal occupancy and the final bounded witness are still open.

[Maintaining workbench](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/9a3ddfe8b38a424f1ff0426201a1f4f6f9d2772f/ATTEMPTS.md)

<a id="es:attempt:full-shell-factor-sieves"></a>

### Full-shell occupancy and factor sieves

For the Erdős–Straus conjecture, we tested full divisor shells and factor exponents rather than only coarse congruences. Exact first-two-shell tests and a primewise all-shell criterion were obtained. We have not proved occupancy at every prime or found a prime with all shells empty.

[Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/first_two_shell_sieve.tex) · [Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/counterexample_sieve/all_shell_no_hit.tex)

<a id="es:attempt:bounded-shared-constraints"></a>

### Simultaneous constraints and bounded CRT

We tested whether linked Erdős–Straus congruences can be solved by bounded CRT while preserving the original shared variables and exponent bounds. Lattice, bounded-divisor, and incidence calculations give finite fibres and explicit obstructions. Integral compatibility still does not force a bounded solution, and the prime-output map is not known onto.

[Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex) · [Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/shared_variable_crt.tex)

<a id="es:attempt:witness-propagation"></a>

### Witness propagation and exact first codes

We transported Erdős–Straus witnesses while retaining order, factor scale, and codes. Ratio maps, shears, and returns classify integer domains and give a first code on occupied residual-three shells. Universal occupancy remains unresolved; two passing adjacent positive shears do not compose.

[Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex) · [Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/exact_audit/fixed_y_successor.tex)

<a id="es:attempt:divisor-cyclic-interface"></a>

### Divisor categories and cyclic coordinates

We constructed the corrected Connes–Consani divisor/cyclic-coordinate interface for the original Erdős–Straus arithmetic. Intersections, returns, primitive marks, and an affine correction give exact maps with recoverable arithmetic. A zero integral obstruction still does not force an occupied bounded fibre.

[Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/connes_reading/connes_primitive_intersections.tex) · [Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/bounded_transport.tex)

<a id="es:attempt:auxiliary-torus-operators"></a>

### Auxiliary torus, sampling and directional inverse

We passed Erdős–Straus character packets through the auxiliary torus and back to the original operators. Extra sampling terms were found and the packets repaired without changing counts; directional inverse estimates followed. A prime-to-fluid construction, universal occupancy, and complete fluid validation remain unachieved.

[Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/torus_cover_lemma.tex) · [Full arithmetic source](https://github.com/KokunoYumeto/erdos-straus-foundation/blob/ead4c88dff3c2e3bdf4b6c8dff6baf2237ad3641/research/expanded-2026-09-08/exact_bounded_transport_72/ns_operator_bridge/sieve_character_cover.tex)

<a id="s6-attempts"></a>

## S6 geometry and marked lattice constructions

**Source:** 27_s6_key_advances_frozen_2026-09-06.tex (2026-09-06 / Zenodo 22678442). Inspect the claimed complex-threefold construction on S^6 circulated by Levent Alpöge with Fable, using the frozen key-advances reader and complete archive (Zenodo 22678442), while separating geometric certificates from broader physical interpretations. The calculations ask whether the proposed fibration, period deformation, finite fillings, and marked cubic lattices are intrinsic and exact. They do not turn the geometric construction into a Yang–Mills or mass-gap theorem.

For a self-contained explanation of the object, the two aims, and each route's
concrete result and limit, read the [S6 cold-start attempt history](s6/ATTEMPTS.md).

<a id="s6-intrinsic-fibration"></a>

### Recover the fibration from the threefold

For the claimed complex threefold on S^6, we tested whether the fibration is recoverable from the threefold rather than chosen as an external coordinate. Canonical sections and the full anticanonical graded algebra give an explicit degree-two map with the original projective coordinates retained. This is a certificate for the specified analytic construction.

[1. The anticanonical ring recovers the fibration; full proof Theorem 53.17, CR1–CR5](s6/27_s6_key_advances_frozen_2026-09-06.tex) · [Complete S6 source archive](https://doi.org/10.5281/zenodo.22678442)

<a id="s6-period-deformation"></a>

### Vary the original period parameter

We varied the S^6 construction's original period parameter and computed the period and Kodaira–Spencer maps. The intrinsic fibration and three fixed critical values give a nonzero first-order fibre variation. This does not classify all deformations or distinguish every pair of unmarked fibres.

[2. The original period constant gives a nonzero deformation; Theorem 53.18, PD1–PD18](s6/27_s6_key_advances_frozen_2026-09-06.tex) · [Complete S6 source archive](https://doi.org/10.5281/zenodo.22678442)

<a id="s6-finite-fillings"></a>

### Compute the actual finite fillings and attachments

We computed the finite fillings and attachment maps in the S^6 construction while retaining its periods and affine generators. Product covers and deck groups give the cover kernels, complete central attachment kernel, and a smooth normal-line trivialization with inverse. These finish the specified finite-centre calculations, not every global step.

[3. Finite fillings; full proofs Theorems 53.4, 53.6, 53.7, 53.9, FF1–FF46](s6/27_s6_key_advances_frozen_2026-09-06.tex) · [Complete S6 source archive](https://doi.org/10.5281/zenodo.22678442)

<a id="s6-marked-cubic-transport"></a>

### Carry cubic arithmetic through the marked lattices

We carried the cubic arithmetic through the marked Niemeier and Leech lattices in the S^6 reader. Integral neighbours and full cubic polarization give explicit value-group inclusions and quotients. They concern generated value groups; they do not identify the lattices or prove a physical mass gap.

[4. Niemeier–Leech transport; higher-rung Sections 9–11, pp.106–125](s6/27_s6_key_advances_frozen_2026-09-06.tex) · [Complete higher-rung paper and source](https://doi.org/10.5281/zenodo.22678442)

<a id="s6-literal-triality-intersection"></a>

### Find the literal common lattice in the original triality space

We computed the literal intersection of the cyclic octonionic construction with the retained embeddings in the original Cayley frame. Both contain the same diagonal D4 lattice, while its cubic has a generated-group value that is not attained. This separates the literal intersection from the abstract arithmetic value group.

[5. A literal common lattice; higher-rung Section 12, pp.125–135](s6/27_s6_key_advances_frozen_2026-09-06.tex) · [Complete S6 source archive](https://doi.org/10.5281/zenodo.22678442)

<a id="zeta-attempts"></a>

## Zeta and arithmetic transport routes

**Source:** zeta-function-research-reader complete source archive (2026-09-09 / archive commit 490a7ac7). Reconstruct the frozen 411-page zeta reader (Zenodo 22678086) and its complete source archive, then test explicit Weil, Mellin, angular-momentum, and radial-recursion claims without treating a transported signal as an RH proof. The route keeps the actual polynomial mechanism, theta input, corrected fluid field, full Mellin factors, and axis recursion named. This makes clear which calculations are exact source results and which RH-relevant conclusions remain unproved.

[Maintaining workbench](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/63dc28e53c37a0c17c2648a5e006b3aea758e182/ATTEMPTS.md)

<a id="zeta-retained-branches"></a>

### Keep the branches, then transport the equations

In the frozen zeta reader's retained polynomial mechanism (satellites/23_source_mechanism_transfer.tex), we kept inverse branches, exceptional fibres, and diffusion maps while transporting the equations into fluid and arithmetic coordinates. The pullback metric has an escaping trajectory but is incomplete; no classical Euclidean fluid singularity or off-critical zeta zero follows.

[Complete zeta source archive](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/490a7ac7ef693702e9d92ba1e933a440d8f55b9b/zenodo_collection_20260909_main411/07-complete-mathematical-sources.zip)

<a id="zeta-actual-weil-test"></a>

### Test the negative coefficient in the complete Weil form

We evaluated the negative coefficient against the complete Weil form using the actual theta input whose Fourier transform is Riemann Xi, retaining pole, gamma, prime-power, cross, and tail terms. The source records a positive value, about 2.0984855607004 × 10^-19, so this input is not a negative witness; global Weil positivity and RH remain unsettled.

[Complete zeta source archive](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/490a7ac7ef693702e9d92ba1e933a440d8f55b9b/zenodo_collection_20260909_main411/07-complete-mathematical-sources.zip)

<a id="zeta-actual-swirl-mellin"></a>

### Transport the actual concentrating swirl into arithmetic

We transported the released corrected fluid field's angular-momentum observable through dilation and Mellin maps, retaining nonlinear fluxes, force, viscosity, and projection remainder. The calculation gives a growing arithmetic derivative and matching Mellin residue at s=-1. This is a transported source signal, not an off-critical zeta zero; independent validation of the imported source theorem remains unfinished.

[Complete zeta source archive](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/490a7ac7ef693702e9d92ba1e933a440d8f55b9b/zenodo_collection_20260909_main411/07-complete-mathematical-sources.zip)

<a id="zeta-hidden-mellin-data"></a>

### Recover data hidden by trivial-zero cancellation

We expanded the full Mellin product at negative integers to track data hidden when a zeta factor cancels a pole. Odd Taylor coefficients come from residues and even coefficients from regular values divided by the nonzero multiplier derivative. This recovers the Taylor sequence, not an arbitrary smooth germ; flat remainders remain.

[Complete zeta source archive](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/490a7ac7ef693702e9d92ba1e933a440d8f55b9b/zenodo_collection_20260909_main411/07-complete-mathematical-sources.zip)

<a id="zeta-finite-radial-recursion"></a>

### Make the higher radial source data constructive

We extended the corrected fluid field's axis calculation beyond its first radial derivative, retaining pressure, viscosity, cutoff, and Mellin residue/value terms. The written induction gives vanishing above correction order n>m and a finite algorithm at each fixed degree. It does not prove convergence of the uncut series or produce an autonomous finite-dimensional fluid system.

[Complete zeta source archive](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/490a7ac7ef693702e9d92ba1e933a440d8f55b9b/zenodo_collection_20260909_main411/07-complete-mathematical-sources.zip)

## Yang–Mills continuation: retained responses, gauge-native sources and cubic return

The 14–16 September session applied retained-source and minimum-energy constructions to the original lattice operator, then developed actual-loop response estimates, strong-coupling source bounds, a gauge-native band calculation and the complete cubic/linearized return. The [complete continuation edition](yang-mills/consolidation/20260916/) preserves full arguments and the source sequence; its current state keeps the finite-lattice and fixed-spacing volume-limit ranges separate. The fourth vacuum-energy coefficient is supplied, while the connected fourth vacuum-source calculation was still in progress at the export boundary. Earlier response bodies and missing attachment distinctions are retained so that attempted routes are inspectable.
