# Yang–Mills mathematical sources and readers

This collection develops explicit mathematics for interacting SU(2) lattice gauge theory: the vacuum and its response to local couplings, ground energies, physical excitation spectra, and maps relating states and operators at different scales. Finite-box calculations are combined with estimates that can survive growth of the box. The separate spatial-limit investigations state what additional control is needed for a continuum theory.

## Full proofs and editable LaTeX

**Originating constructions.** Levent Alpöge's Jacobian counterexample supplies the polynomial used in the material-tensor calculations; the separate S6 construction circulated by Alpöge and produced with Claude supplies the period data used in the cusp and magnetic-background maps. [Primary citations and exact points of use](../ATTRIBUTION.md) distinguish those inputs from this workbench's subsequent physical-state maps and estimates. Read the older “Fabel” passages with this attribution clarification.

The mathematical manuscripts are public here as editable sources, not only as PDF readers or summaries.

- **S6-reduced triality-to-profile bridge, 30 September:** [complete corrected proof and reading guide](continuations/20260930-s6-ns-moment-map-bridge/), [higher-domain programme](continuations/20260930-s6-ns-moment-map-bridge/HIGHER_DOMAIN_PROGRAM.md), [locally-gapped/globally-gapless spectral programme](continuations/20260930-s6-ns-moment-map-bridge/SPECTRAL_PROGRAM.md), [source provenance](continuations/20260930-s6-ns-moment-map-bridge/SOURCE_PROVENANCE.md), and [public validation](continuations/20260930-s6-ns-moment-map-bridge/PUBLIC_VALIDATION.json). The result constructs the missing global quadratic bundle morphism and calculates its first interaction core. The exact nonzero source identifies the next correction equation; no source-free quantum state or continuum mass-gap conclusion is claimed.

- **Fifth-reference source, physical spectrum and improved heat bounds, 21 September:** [24-page reader with both complete proofs](consolidation/20260921-fifth-reference/reader/yang_mills_fifth_reference_20260921.pdf), [standalone LaTeX](consolidation/20260921-fifth-reference/reader/yang_mills_fifth_reference_20260921.tex), [full exposition and exact statements](consolidation/20260921-fifth-reference/), [the complete source proof](consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md), [heat and complementary-space proof](consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260921-fifth-reference-return/HEAT_AND_COMPLEMENT.md), and [cumulative source archive](consolidation/20260921-fifth-reference/archives/yang_mills_cumulative_20260921_fifth_reference.zip). The full correction includes the source endpoint; the improved heat circle is `|ξ| < 1/55`. This successor preserves the preceding editions below.

- **Heat correlations, box-independent bounds and the full physical complement, 21 September:** [readable PDF with all five complete proof manuscripts](consolidation/20260921/reader/yang_mills_heat_volume_20260921.pdf), [standalone LaTeX](consolidation/20260921/reader/yang_mills_heat_volume_20260921.tex), [source guide](consolidation/20260921/), [cumulative mathematical text](consolidation/20260921/package/CUMULATIVE_RESEARCH.md), and [complete source archive](consolidation/20260921/archives/yang_mills_cumulative_20260921_volume.zip). The five supplied Markdown manuscripts remain unchanged beside the new reading edition.
- **Fourth-order vacuum, sixth-order energy and physical spectral return:** [complete LaTeX, including all six proof notes](consolidation/20260917/reader/yang_mills_quartic_cube_reader.tex), [PDF](consolidation/20260917/reader/yang_mills_quartic_cube_reader.pdf), and [source package](consolidation/20260917/yang_mills_quartic_comparison_sources_20260917.zip).
- **Source equations, gauge coordinates and spectral return, 14–16 September:** [complete cumulative LaTeX](consolidation/20260916/reader/yang_mills_web_continuation.tex), [PDF](consolidation/20260916/reader/yang_mills_web_continuation.pdf), and [source package](consolidation/20260916/yang_mills_complete_available_sources_20260916.zip).
- **Foundation manuscripts:** [LaTeX and accompanying source files](sources/), with individual paper links in [Read the manuscripts](#read-the-manuscripts) below.
- **Sixth-source, eighth-energy and response continuation, 19 September:** [full supplied mathematical texts](consolidation/20260919/supplied/) in their original Markdown format, with the [reading guide](consolidation/20260919/).

## Start reading

- **[S6/NS moment-map bridge](continuations/20260930-s6-ns-moment-map-bridge/):** the current higher-domain branch. It proves the unique linear colour projection, constructs the three equivariant quadratic moment maps, descends them to the retained nontrivial `Sp(1)` bundle, and computes the resulting three-colour curvature and source. Read its claim ledger before using the broader programme: the classical profile is not yet a physical state, and the source-free correction remains open.
- **[Fifth-reference reader](consolidation/20260921-fifth-reference/reader/yang_mills_fifth_reference_20260921.pdf)** (24 pages): the original Hamiltonian and coefficient construction, the complete nonlinear correction including its endpoint, its return to the full physical spectrum, the enlarged heat circle `1/55`, and full-complement corrections below `1/2000` for `g² ≥ 13` and `1/25000` for `g² ≥ 16`. The introduction explains the objects and why the domains differ; both full proofs follow it. This is the latest [Zenodo edition](https://doi.org/10.5281/zenodo.22883643), retaining all 37 files of its predecessor.
- **[Heat, volume and full complementary space](consolidation/20260921/)**: the 21 September edition includes the fourth-order heat functions and first-band matrix, an all-time row estimate with source radius `3/256` independent of the box, the fixed-spacing spatial-volume limit, and the exact full-complement energy minimization. For every original box `L ≥ 2`, every `a > 0`, and `g² ≥ 16`, the new bounds retain more than `999/1000` of the plaquette-family energy after all complementary states relax. Complete written proofs, coefficient tables and separately identified fresh finite checks accompany both unchanged cumulative packages.
- **[Sixth source, eighth energy and finite-volume plaquette response](consolidation/20260919/)**: the 19 September continuation preserves the three new research notes, their response certificates, and the predecessor executable archive. It presents the precise response and support-transition maps alongside the independent one-face and arithmetic checks. The missing new spatial coefficient tables and unfinished final execution package are identified explicitly; no complete spatial replay is claimed.

- **[Fourth-order vacuum sources and sixth-order energy](consolidation/20260917/reader/yang_mills_quartic_cube_reader.pdf)** (49 pages): an introduction to the Hamiltonian, two exact presentations of the fourth logarithmic-vacuum coefficient, the sixth energy including boundary and cube contributions, signed local response, and the resulting physical spectral estimate. All six proof notes are included. [Formulas, sources and reproduction](consolidation/20260917/).
- **[Source equations, gauge coordinates and spectral return](consolidation/20260916/reader/yang_mills_web_continuation.pdf)** (297 pages): the preceding complete 14–16 September continuation, including actual-loop, gauge-native, local-fibre, cubic-source and linearized-return arguments.
- **The five foundation papers below**: broader entry points for quantum state maps, interacting tensor bands and vertices, volume-independent vacuum estimates, and spatial-continuum investigations.

The 17 September reader presents a convergent correction for the original Hamiltonian, not merely its truncated series. In its convention `kappa = 2g^2/a` and `xi = 1/(4g^4)`, it states a complete physical-gap bound uniform in finite box size; in particular `g^2 >= 15/4` gives `Delta > 1.6584 kappa`. That historical argument retains its existing analytical-review qualification. The 21 September heat proof rederives its own conservative local-source and complete-space estimate; it does not recertify the earlier stronger interval. Neither edition establishes a four-dimensional continuum field or a finite positive continuum mass.

The complete 17 September continuation is available here and in the [21 September Zenodo edition](https://doi.org/10.5281/zenodo.22803564), together with the new heat and volume reader, both cumulative archives, and the attribution clarification. All 23 files from the [9 September archive](https://doi.org/10.5281/zenodo.22678364) are retained unchanged. The two fourth-order source packages retain their distinct derivations. Their complete polynomials agree under an explicit coordinate map; the [validation account](consolidation/20260917/VALIDATION.md) explains that comparison, the finite checks and the analytical review separately.

## Previous continuation: 14–16 September 2026

Read the [complete web-session consolidation](consolidation/20260916/), its [cumulative PDF](consolidation/20260916/reader/yang_mills_web_continuation.pdf), or the [editable TeX](consolidation/20260916/reader/yang_mills_web_continuation.tex). The edition integrates the actual-loop, uniform-gap, gauge-native, local-fibre, cubic-source and linearized-return proofs with their complete available dependencies and scoped verification records. The [current mathematical state](consolidation/20260916/CURRENT_RESEARCH.md) keeps the finite-lattice gap domain, fixed-spacing volume-limit domain and remaining continuum questions explicit.

The [coverage and provenance](consolidation/20260916/SOURCE_COVERAGE.md) identify the exact archive and Git sources; the [validation record](consolidation/20260916/VALIDATION.md) distinguishes executed finite checks from bounded proof reviews. Earlier source and execution records retain their original historical status. This continuation is included in the [21 September archived edition](https://doi.org/10.5281/zenodo.22803564); the foundation DOI below retains the 9 September edition.

## Foundation edition: 9 September 2026

[What the quantum, interaction, volume and spatial-limit tasks tried—and why](../ATTEMPTS.md#ym-attempts)

This edition collects the supplied current quantum coarse-graining, volume-uniform actual-vacuum, spatial-continuum, and related finite-box mathematical proofs. It supplements the existing Yang-Mills collection, whose previous editions and complete historical workbench remain part of the publication history. This ZIP is an explicitly selected current-source edition, not a replacement for the entire historical workbench.

## Read the manuscripts

| Reader | Pages | TeX source |
| --- | ---: | --- |
| [quantum_coarse_graining.pdf](https://zenodo.org/records/22678364/files/quantum_coarse_graining.pdf) | 79 | [extensive_quantum_blocking.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/extensive_quantum_blocking.tex) |
| [quantum_interacting_tensor_band.pdf](https://zenodo.org/records/22678364/files/quantum_interacting_tensor_band.pdf) | 71 | [extensive_quantum_blocking.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/interacting_band_publication_20260909/extensive_quantum_blocking.tex) |
| [quantum_nonabelian_vertex.pdf](https://zenodo.org/records/22678364/files/quantum_nonabelian_vertex.pdf) | 63 | [extensive_quantum_blocking.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/nonabelian_vertex_publication_20260909/extensive_quantum_blocking.tex) |
| [volume_uniform_vacuum.pdf](https://zenodo.org/records/22678364/files/volume_uniform_vacuum.pdf) | 81 | [VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.tex) |
| [spatial_continuum.pdf](https://zenodo.org/records/22678364/files/spatial_continuum.pdf) | 129 | [spatial_continuum.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_spatial_continuum_astra_20260908/spatial_continuum.tex) |

The quantum reader is cumulative. Its interacting tensor and nonabelian vertex readers retain their separate supplied component snapshots and corresponding sources; they are earlier focused editions, not newly rebuilt components of the cumulative reader. Markdown counterparts preserve the full mathematical text for searching and AI ingestion. The current spatial manuscript includes the fixed-coupling analytic-disk obstruction in Section 27 and the corrected Section 26.13 oscillator path rates. The volume manuscript retains its current covariance-window estimates.

This edition: [10.5281/zenodo.22678364](https://doi.org/10.5281/zenodo.22678364). Repository: [Yang-Mills collection](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/yang-mills), with separate [Navier-Stokes](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/navier-stokes) and [S6](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/s6) collections.

The original finite-box objects, coefficients, domains and hypotheses are stated in the included proofs. The oscillator path rates are fixed-box/oscillator consequences: a volume-uniform comparison with the simultaneous exact-lattice limit is not established. The fixed-coupling disk result identifies the limitation of a particular global perturbative bound. These results do not establish or refute the interacting four-dimensional continuum Yang-Mills mass gap.

## Foundation sources and reproducibility

`sources/` preserves the selected files' original names and local dependency hierarchy. Each quantum component is retained in its own original snapshot directory. `AI_READING_INDEX.md` links the complete Markdown and TeX bodies. Bibliographic entries remain in the manuscripts; no downloaded literature corpus is redistributed. `DEPENDENCIES.json` records resolved literal TeX inputs. `READER_PROVENANCE.json` records page counts and exact PDF/TeX/Markdown hashes. `SOURCE_MANIFEST.json` gives the byte count and SHA-256 of each archived file other than the manifest itself. It contains only archive-relative paths.

The PDFs are supplied artifacts copied byte-for-byte into this archive. The packaging worker did not rebuild them or rerun mathematical checkers. The publication coordinator regenerated the volume reader after correcting a single TeX inline-math closing delimiter to match the already correct Markdown; the mathematical source content was unchanged. Included checker programs and recorded results are finite symbolic, arithmetic or numerical diagnostics within their stated scope. Packaging integrity and dependency checks are not formal verification of the analytical proofs. To compile an included TeX manuscript, run a LaTeX distribution from its containing directory; dependencies identified by literal input commands are supplied. The Markdown-to-TeX conversion intermediate `markdown_source.tex` is included for the current quantum manuscript. Python checkers require their stated imports, including SymPy, NumPy, SciPy and mpmath where used, and should be run from their containing directory. Original sibling lane names are retained so relative cross-lane paths resolve. One recorded result's absolute source locator is replaced by its portable relative path; its mathematical data and cited input hash are retained.

`OMISSIONS.json` records exclusions from the historical allowlist. Private task records, user transcripts, feedback, credentials, copied literature bodies, separate S6 and Navier-Stokes source collections, and the uncertified full-L2 tensor contraction calculation/report are excluded. No mathematical claim is made for that excluded exploratory calculation.

## Higher-carrier and temporal correction

The [higher-carrier and temporal evolution proof](continuations/20260930-s6-ns-moment-map-bridge/HIGHER_CARRIER_AND_EVOLUTION.md) constructs the exact pullback through the 49-dimensional reduction carrier, extends the profile map, and gives a full parameter connection. It constructs a compactly supported correction satisfying Gauss's law exactly with a computed residual, and proves global source-free evolution of every homogeneous core. The [full compact-support Cauchy continuation](continuations/20260930-s6-ns-moment-map-bridge/COMPACT_SUPPORT_CAUCHY_EVOLUTION.md) now applies Sung-Jin Oh’s established global theorem to the original data and proves finite propagation, the full energy polynomial and its zero set, smooth parameter dependence, bundle descent, dilation and actual link holonomies. The [period and physical-kernel continuation](continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) now supplies the full angular coupling, nonzero finite-lattice physical vectors, exact Gram and Hamiltonian kernels, the corrected same-coupling path, and the full first-electric-layer interaction and complementary return. Continuum spectral weight, reconstruction and theory identification remain active.

## Complete complementary moment, 9 October 2026

The [full complementary calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) evaluates the second
electric moment and fourth magnetic compression, including every six-face
cube term. Theorem 9.2 and PK55–PK62 give the original C*B^2C, the nonzero
next map, its complete Gram and bounds, an exact second return, and a stronger
finite-volume upper resolvent bound. The vacuum shift, both coupling factors,
all face labels and boundary counts remain explicit. The next calculation is
the full second-complement return and actual heat-packet coefficients; the
continuum endpoint remains active.

## Full packet and complete cutoff, 9 October 2026

The [full packet calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) gives both exact complementary
returns for the actual heat packet, with every cross term. PK65–PK75
give a finite electric cutoff, a proved interval for the actual vacuum
energy, and an explicit error for the full raw spectral transform.
The cutoff is specified on the original regulator path with error at most
Gamma_j/(kappa_* j). PK76–PK78 evaluate the whole first cutoff and the
original smallest-box example. A positive lower spectral mass and the
interacting continuum state remain active research calculations.

## Actual packet moments and spectral escape, 9 October 2026

The [complete PK79–PK100 calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) evaluates the actual
first and second interacting moment kernels, with every shared-link
contraction and vacuum-shift term. A sharper variational vacuum bound
and an original-graph Haar estimate prove that the fixed-heat packet
loses its spectral-weight fraction even below the expanding threshold
kappa_* j. Its accurate finite cutoff is not the reason the low-mass
test failed: the actual fraction tends to zero.

The next state map is constructed using the full interacting semigroup.
Its raw norms, decreasing relative energy and preserved spectral support
are proved. The scale of its supported bottom and the required continuum
construction remain active research. This result concerns the specified
packet family; it does not settle the spectrum of other states.

## Actual odd vacuum observable, 9 October 2026

The [complete PK101–PK131 proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) constructs a bounded
smooth reflection-odd observable on the actual interacting vacuum.
At each fixed box its raw first-cluster weight tends to 3/32, and its
supported bottom is the actual lowest odd excitation. All limiting
raw spectral weights and the Euclidean-time correlation are evaluated.
The entire higher-carrier total space receives a global smooth map
through its three selected quaternionic squared norms, with the exact
original zero subbundle and parameter-dependent weights retained.

The original simultaneous path still needs estimates for its actual
odd energy and raw weights. The full continuum construction remains
the research target. The earlier vacuum upper bound is now linked
to its retained spatial-continuum proof with an exact parameter map.

## Joint-path raw mass and global replacement, 9 October 2026

The [complete PK132–PK157 proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) settles the original
chart-supported odd observable's raw mass as zero along the prescribed
joint path. The result uses the actual vacuum and retains the complete
Haar dimension, graph counts and coupling factors. It extends to a
precisely defined class of growing chart supports.

A global smooth group-coordinate observable is then constructed. It is
nonzero at every finite regulator, retains the full higher-carrier domain
with its exact original zero subbundle, and has the earlier fixed-box
spectral limit. Complete ordered word derivatives and actual-vacuum
moments are calculated. Its joint-path mass and energy remain the next
estimates; the full interacting continuum endpoint is still the target.

## Global fourth moment and energy estimates, 9 October 2026

The [complete PK158–PK177 proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) evaluates the original
chord Gram matrix and full Haar fourth moment, and gives the exact
four-loop formula in the actual vacuum. The original raw norm is bounded
by the actual fourth moment times the squared phase. On the unchanged
path, retaining positive limiting raw weight requires growth on at least
the j^6 scale. Actual first and second energy-moment bounds retain every
word occurrence, coupling, colour and boundary contribution. Calculating
the actual four-loop growth and closing odd energy remains active work
towards the full interacting continuum state.

## Actual phase limits and variational space, 9 October 2026

The [complete PK177a–PK206 proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) evaluates every original
chord-face weight and the resulting actual fourth-moment bound. An exact
two-link configuration identifies the nonlinear reflection defect.
At each finite regulator the actual large-amplitude raw mass tends to
1/4, while the opposite iterated weak-coupling limit is 1/2. The actual
energy moments and high-energy escape are proved, including an amplitude
sequence on the unchanged regulator path.

The next state space is constructed through the actual joint phase
measure. Its exact physical isometry, closed energy form, full residual
interaction and convergent finite variational matrices retain the
original vacuum and all mixed terms. Their actual low-energy path
estimates are the next calculation toward the full continuum endpoint.

The same phase construction now has [proved full rank, an actual phase density, positive finite matrices and a complete distributional boundary identity](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md). These are exact finite-regulator results; their original-path coefficients remain to calculate.

## Actual vacuum and certified phase matrices, 9 October 2026

The [complete PK207–PK227 proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md) bounds the actual vacuum mass
below an electric cutoff proportional to the full face count and proves
its vanishing on the original path. It retains the full vacuum energy
and derives an explicit lower bound for that energy.

Complete vacuum-cutoff comparisons now give finite original-word
enclosures for the actual Gram, energy and second-moment matrices,
including their full Hamiltonian residual. An explicit cutoff controls
all three matrix errors on the unchanged path. The certified raw
low-energy expression is now the next calculation toward the interacting
continuum endpoint; positivity in a shrinking window is not assumed.

## Phase moments and central link symmetry, 11 October 2026

The [new continuation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/README.md) proves exact original-word bounds for the
shrinking-window expression and controls every polynomial phase multiplier
at fixed box. Its original first polynomial has raw limiting norm squared
12 and first odd-cluster weight 12. The complete Gram and energy limits
retain their rank degeneration and volume-dependent tail constants.

An exact central-link involution also settles the third and every higher
odd Jacobian return, with full complementary-inverse and even-tail bounds.
The boundary proof classifies all admissible open and periodic central
sign maps, including winding signs and the full Hamiltonian scalar.
The actual growing-box low-energy weight and interacting continuum
endpoint remain the continuing research calculation.

The [complete phase spectral weights](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_SPECTRAL_WEIGHTS.md) now evaluate every fixed-box polynomial cluster and the exact radial direction outside the earlier phase compression (SP1–SP16). The original raw states and full vacuum factors are retained; the joint-path estimate remains the next spectral calculation.

The [exact boundary reflection and two-link harmonic](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDARY_REFLECTION_AND_RAW_ENDPOINT.md) now give actual-vacuum raw mass and energy bounds on the unchanged regulator path, with exponential loss of order j². The [complete fourth Jacobian coefficient](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/fourth_return/FOURTH_SCHUR_COEFFICIENT.md) includes its boundary skew matrix, full degree-six remainder and exact map to physical susceptibility. Positive spectral mass in the shrinking window and the interacting continuum endpoint remain the active targets.

The [global finite-source continuation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GLOBAL_PHYSICAL_RESPONSE.md) proves the exact physical and original assembly-quotient inverses at every finite real source, strict physical susceptibility, and the global Wilson expectation coordinates. Its unchanged-path inverse susceptibility bound is O(j⁴⁰), with all constants and domains retained. The low-window spectral measure and continuum reconstruction remain active calculations.

The [polynomial conditional comparison](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POLYNOMIAL_CONDITIONAL_BOUNDS.md) replaces the prior exponential density loss by explicit polynomial bounds and proves the exact larger receiving-link coefficient inside the unchanged phase. Its complete raw-mass, energy and endpoint formulas retain every affine remainder and physical factor. They sharpen the finite-path estimates while leaving the actual shrinking-window cancellation as the next spectral calculation.

The [complete union-labelled inverse](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/union_label_global/FULL_UNION_LABEL_INVERSE.md) is now proved at all finite real sources, including every assembly relation direction and every vacuum scalar. Its [connected-support consequences](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SUPPORT_AND_SCALAR_FACTORIZATION.md) prove exact factorization and strengthen the original transformation constants. These results complete a finite-source inverse step; quantitative connected-coefficient decay and the physical shrinking-window spectral calculation remain active.

The [full cap and boundary calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POLYNOMIAL_SCORE_AND_ORIGINAL_ENDPOINT.md) and [complete gradient/bulk calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POLYNOMIAL_GRADIENT_BOUNDS.md) now give explicit optimal score exponents and evaluate every retained physical derivative sum. On the unchanged path the odd-energy lower bound improves to order j^(-30), while the even endpoint correction has order j^(-33) with a strengthened coefficient. The actual shrinking-window sign, spectral weight and interacting continuum construction remain the research target.

The [complete square-root score and receiving proofs](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SQUARE_ROOT_SCORE_RECEIVING_MAPS.md) improve actual-vacuum control uniformly in the finite volume. They retain every physical bulk and boundary derivative, give an explicit positive endpoint correction of order j^(-25), and improve the finite face-response inverse bound to O(j^32). The [full response identity](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_RESPONSE_AND_ENDPOINT.md) retains the unresolved joint spectral cancellation. The globally smooth interacting no-gap state, reconstruction and theory identification remain the research goal.

The [exact rooted-curvature calculation, CW1–CW49](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURVATURE_ROOTED_WORDS.md) strengthens the actual-vacuum phase bounds using the original signed coefficients and retains the full quadratic nonabelian remainder. Its explicit configuration family shows why mean curvature and cube symmetry alone cannot decide the original joint spectral endpoint. Complete proofs, finite checks and a reproducible illustration accompany the calculation.

The [coupled signed-endpoint calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PHASE_CANCELLATION.md) retains the mixed mass–energy covariance and the complete finite-cutoff residual. The [ordered Wilson-action calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORDERED_WILSON_ACTION.md) gives the exact cubic term, explicit integral-remainder bounds and a local repair of its source proof. Both are applied to the original objects; neither establishes the unresolved endpoint sign.

The [actual-vacuum limit](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_SEMIGROUP_LIMIT.md) constructs the continuous generator, full spectral escape space and exact Wilson observable representation. The [time-regularity proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/WILSON_TIME_REGULARITY.md) gives continuous histories for the stated countable Wilson family, while retaining the unresolved growing-loop and raw-phase spectral weights. The [ordered-action supplement](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORDERED_WILSON_INDEPENDENT_REVIEW.md) strengthens the complete remainder estimates. These are intermediate results in the original smooth global no-gap research programme.

The [quantitative temporal bridge](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ANISOTROPIC_TEMPORAL_BRIDGE.md) supplies an explicit finite Wilson-integral sequence for the original shrinking-window test. The [spectral receiving maps](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_LOW_ENERGY_MAPS.md) retain zero-energy collapse, cyclic visibility, positive-energy detectors and endpoint atoms. The [stronger path estimates](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/WILSON_TIME_REVIEW.md) refine the actual Wilson histories. These are proved intermediate calculations; the original endpoint sign and interacting four-dimensional identification remain open.

The [local actual-vacuum curvature proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/LOCAL_CURVATURE_BUDGET.md) retains the inside kinetic and potential contributions, all crossing faces and their exact gauge cancellation. It evaluates the original physical face quadratures as scalar observables in the reconstruction, with complete finite-volume and temporal bounds. The programme continues with candidate fluctuations and their actual spectral weights.

The [actual curvature source calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHYSICAL_LOCAL_COVARIANCE.md) proves lower mean and energy bounds and exact covariance receiving maps. The [bounded curvature-phase construction](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURVATURE_PHASE_RECONSTRUCTION.md) adds a continuous cyclic representation and real anchored time histories, retaining the initial-character and spectral-loss maps. Evaluating the original covariance and surviving positive-energy weight remains part of the smooth interacting no-gap research goal.

The [original-source Hessian calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORIGINAL_SOURCE_COVARIANCE.md) and [sharper raw-moment receiving bounds](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/HESSIAN_RECEIVING_REVIEW.md) establish actual-vacuum lower variance bounds and exact spectral and heat estimates. [Spatial distribution histories](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/DISTRIBUTION_CURVATURE_HISTORIES.md) and [interior recovery](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/DISTRIBUTION_HISTORY_REVIEW.md) construct and identify the corresponding continuous distribution paths. The smooth interacting no-gap target still requires nonzero weight in the original shrinking energy window and the full four-dimensional reconstruction.

The [full raw S6 calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/RAW_S6_HESSIAN_RECEIVING.md) proves sharper conjugate estimates and exact signed covariance receiving blocks. The [actual-source kinetic square](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SOURCE_ZERO_COVARIANCE_UPPER.md) strengthens upper covariance constants with complete nonnegative remainders; [potential covariance identities](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POTENTIAL_VARIANCE_IDENTITIES.md) specify the remaining sign question. The original shrinking-window spectral weight and smooth four-dimensional reconstruction remain the programme target.

The [bounded-phase calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDED_PHASE_SPECTRAL_RECEIVING.md) quantifies actual high-energy norm loss and constructs its exact continuous-representation defect space. The [soft-direction calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/DIRECTIONAL_POTENTIAL_AND_ROOT_DEFECT.md) proves full root commutators and transported-curl covariance maps. They retain the actual vacuum and original regulator path; low-energy survival and smooth four-dimensional reconstruction remain the research target.

The [actual potential-law calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PUSHFORWARD_OPTIMIZATION.md) controls its upper covariance endpoint and identifies the exact central-range integral. The [independent derivation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PUSHFORWARD.md) and [complete operator map](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PUSHFORWARD_OPERATOR_RECEIVING.md) retain critical-value fluxes, the scalar form domain and the full second-energy residual in the original interacting vacuum. These results advance the spectral calculation toward the smooth gapless continuum target.

The [two-tail and retained-energy proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/LOWER_SIDE_RETAINED_ENERGY.md) adds exact lower-tail and inverse-moment bounds and evaluates the complete inside-energy covariance. Its [independent marginal derivation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/INSIDE_MARGINAL_ENERGY.md) retains the full physical operator residual and signed map to the original curvature. The research continues toward nonzero low-energy spectral weight and smooth four-dimensional reconstruction.

The [actual transported-curl calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_WILSON_COVARIANCE.md) proves a positive original-path lower bound from conditional Haar geometry and the actual ground-state score. It retains all root-word derivatives and the full spectral maps. The smooth interacting four-dimensional no-gap construction remains the research goal.

The [signed kinetic calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SIGNED_KINETIC_TRACE.md) sharpens the original-path upper function to order j^5. The [bounded energy construction](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDED_ENERGY_MULTIPLIER.md), with its [independent proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDED_MULTIPLIER_RECEIVING.md), identifies the original shrinking-window and full signed-covariance maps. The actual limiting variance and globally smooth interacting four-dimensional no-gap construction remain active research calculations.

The [exact negative-trace calculation](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/NEGATIVE_TRACE_COMPRESSION.md) now retains an evaluated actual root-cell contraction. The [smooth holonomy construction](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/HOLONOMY_CURVATURE_RECEIVING.md) and its [independent strengthening](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/HOLONOMY_CURVATURE_REVIEW.md) identify the actual curvature scale, explicit non-Abelian receiving families and their fixed-time behavior. The globally smooth interacting four-dimensional no-gap state and reconstruction remain the research goal.

The [simultaneous spatial-measure proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SIMULTANEOUS_CENTRAL_MEASURE.md) constructs one actual central measure for all original orientations. The [current and fluctuation proof](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURRENT_COVARIANCE_EQUALITY.md) evaluates its current defect and proves a surviving heat fluctuation for every positive parameter, with exact maps to the original shrinking energy window. Actual window weight, four-dimensional reconstruction and the smooth no-gap endpoint remain active calculations.

## Global source-free evolution of the measure-realizing data

[GM1–GM28](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GLOBAL_MEASURE_EVOLUTION.md) apply Sung-Jin Oh's global Cauchy theorem to the exact smooth compact data, construct continuous solution laws from the actual central spatial measure, and prove their zero-time Wilson and energy receiving maps. The complete time expansion, a strict electric-field stationarity defect, and time averages with an explicit invariance error are calculated. The exact virial proves that any stationary probability on conserved finite-total-energy smooth trajectories is supported on flat fields, without an energy-moment assumption. Its receiving space must therefore be enlarged to allow infinite total energy for a nonflat stationary classical law. Quantum reconstruction and the actual low-window coefficients remain to be established.

## Stationary phase laws and exact quantum receiving tests

[HP1–HP40](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/STATIONARY_PHASE_RECEIVING.md) construct stationary global smooth homogeneous Yang–Mills laws and calculate their complete phase, spatial and time correlations. The actual CM lower bounds exclude this isotropic phase family, with an explicit continuous witness and a uniform interval-defect probability. The original finite Wilson observations retain a fully calculated shrinking-window weight under the specified auxiliary positive generator: the coefficient decays as j^(-63/4) for aC and j^(-55/4) for raw C, with a relative norm error of order j^(-4). Complete energy matrices and HP37 contrast this auxiliary spectrum with the actual quantum leading receiver, whose original first energy tends to zero. HP38–HP40 prove the exact composition-generator restriction and reflection-form comparisons, keeping the direct Euclidean interpretation distinct from analytic continuation. These comparisons do not assign the actual quantum window weight or establish the interacting no-gap endpoint.
