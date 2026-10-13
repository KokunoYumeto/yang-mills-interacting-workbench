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

## Actual energy vectors and bounded phase history maps

[EF1–EF27](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ENERGY_ROOT_AND_ANCHORED_HISTORIES.md) prove that all actual CE heat-increment vectors have one continuous-time receiver, with their complete escaped Gram retained. A bounded sine-cylinder approximation receives every positive-energy component of the actual energy-root vector in an explicitly enlarged curvature-phase cyclic space. The proof preserves the smaller CM space and every zero-energy, original-window and cyclic-compression defect. Exact anchored variance and reflection formulas retain both spectral endpoints; a quantitative original-energy window bound uses the actual variance and the full fourth-moment remainder. EF25–EF27 additionally prove that the actual small-phase energy measures receive the complete finite-energy spectral measure, including its zero endpoint, and give a quantitative bound for positive windows. No actual coefficient is assigned a positive value merely from whole-vector survival.

## Positive-time covariance and the full resolvent tail

[PT1–PT36](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POSITIVE_TIME_COVARIANCE.md) prove the actual energy correlation’s exact weighted one-form representation on the original SU(2) lattice, including the radius-two Ricci term, gauge constraints and complete exterior Hessian inverse. The two-time current cancellation is evaluated. The full Hessian expansion has a proved finite-regulator remainder bound, and every truncation with a_j(N_j+1) tending to zero is proved to vanish. Any surviving response is received by its complete tail, whose spectral concentration near one and exact unitary map to the physical resolvent vector are established. The raw and energy-weighted original shrinking windows remain explicit. No positive value of an unfinished limiting coefficient is assumed.

The primary-source comparison uses original author TeX by Jon Johnsen and Assane Lo, with exact versions and bounded reading coverage. The compact-domain convexity obstruction is proved together with the curved weighted-form map that remains available. Complete proofs, reproducible figures and checks are included.

## Actual ground-gradient trials and complete variational residual

[SG1–SG33](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_GROUND_GRADIENT_TRIAL.md) construct edge-weighted gradients of the actual logarithmic ground density and compute their complete energy, current covariance, source overlap and exterior Hessian contributions. Exact optimization over every deterministic edge weight gives a strictly positive finite matrix and an explicit residual mapping its value to the full physical resolvent. A forced equation relates the trial directly to the derivative of the original plaquette potential. For the unchanged three-orientation tent test, the sign trial improves the previous proved lower-bound coefficient by more than ten thousand; its lattice-spacing scale is retained. The remaining signed contraction and full residual have not been assigned limiting values. Complete proofs, exact coefficient comparisons and reproducible inspected figures are included. The physical exact projection removes the entire nonnegative Hessian graph energy while preserving source overlap. Its improved current-covariance matrix retains both full residual norms. Every exterior graph connection and the complete kernel of the removed defect are specified.

## Conditional ground currents and independent fluctuation weights

[CG1–CG34](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CONDITIONAL_GROUND_CURRENT_TRIAL.md) split the actual ground-gradient trial into orthogonal marginal and conditional-fluctuation parts. The fluctuation has zero source overlap, so its independent weight can be optimized. The complete current matrix, including exterior drift and all zero directions, gives an exact nonnegative improvement over the previous SG matrix and an explicit additional lower-bound term. The physical resolvent retains both full residual norms. The conditional ground equation evaluates the remaining marginal contribution while preserving outside energy, crossing faces and conditional kinetic derivatives. Complete proofs, reproducible diagnostics and an inspected figure are included; no positive value of the limiting gain is assumed. A further exact minimization over every outside one-form replaces the conditional noise by its full outside resolvent multiplier, without an exterior-mode cutoff. Its original-Hamiltonian map, additional nonnegative gain, zero space, mixed derivatives and both physical residual norms are proved in CG23–CG34. Fixed-regulator small-z limits are not interchanged with the regulator limit.

## Retained derivatives and actual good boundary cubes

[RD1–RD22](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/RETAINED_DERIVATIVE_AND_GOOD_BOUNDARIES.md) evaluate the derivative retained in CG22 using the full ground equation, marginal equation, conditional variance and both Hessian contractions. The original supported sign and continuous weights have exactly zero direct crossing trace. For unit edge magnitudes, deterministic boundary selection in the actual ground gives a vanishing scaled crossing potential while the full Laplacian trace tends to \(9R^2/\kappa_*\). The original square-root collar and an additional logarithmic collar have complete finite bounds and different proved error rates. Every scalar, outside energy and conditional-current term remains in the calculation; no limiting spectral weight is assumed.

## Wilson covariance and ground-current signs

[GS1–GS12](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/WILSON_AND_CURRENT_COVARIANCE_SIGNS.md) construct a smooth gauge-invariant comparison on two disjoint original plaquettes with strictly positive Wilson-trace covariance and strictly negative distinct-edge ground-current covariance. Complete analytic constants, partition factors and the comparison Hamiltonian are retained. The exact unitary, full potential difference, vacuum change and current transformation connect it to the original Yang–Mills ground. The comparison rules out an inference from Wilson positivity alone; the specific actual-current contractions remain to be evaluated.

## Conditional outside forcing and current moments

[OC1–OC24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/OUTSIDE_FORCE_AND_CURRENT_MOMENTS.md) derive the actual conditional score equation, positive averaged potential Hessian and complete outside-current forcing, preserving the entire original kinetic quotient and every mixed Hessian. Exact first and second moments give a quantified resolvent improvement with both physical residuals. A crossing plaquette proves that the full-cube positive-weight current is nonzero, so the specified finite-regulator improvement is strictly positive. The full covariance, Hessian and force kernels coincide and retain inside gauge directions. The global oscillation comparison is evaluated on the original path; it supplies no vanishing filter coefficient. The limiting current moments and smooth interacting no-gap endpoint remain open calculations.

## Exact boundary projection and actual current-moment bounds

[BQ1–BQ18](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDARY_FORCE_PROJECTION.md) prove that the derivative of the original inside kinetic quotient is the full weighted exact projection of the inside potential gradient. Every wholly inside face derivative cancels from the conditional force; the complete crossing field and original ground-state projection remain. Exact projection and Casimir-gradient remainders give actual force and mixed-Hessian bounds on both established collars, including \(a_j^6\|F_j\|^2\to0\) and \(a_j^5\mathcal O_{Q_j}\to0\). The first current moment is computed without third kinetic derivatives and has a quantitative upper estimate. The second moment retains its weighted boundary divergence and all six signed covariance terms. Unscaled limiting spectral mass and the smooth interacting no-gap endpoint remain active calculations.

## Boundary divergence and marginal second moments

[BD1–BD19](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDARY_DIVERGENCE_AND_MARGINAL_MOMENTS.md) prove an exact mixed derivative and two-square identity for the full projected boundary field. Weighted integration removes its mixed-Hessian contraction from the divergence estimate while retaining the inside score and every original crossing derivative. Both established collars give \(\smash{a_j^7\|J_j\|^2\to0}\) with explicit rates. The existing marginal-gradient block has complete first and second moments and \(\smash{a_j^{11}m_{2,j}^\gamma\to0}\), again with explicit collar constants. The arbitrary-weight force map, full scalar trial line, signed second-moment cross term, exact scalar optimizer and both physical residuals remain. The full-gradient mixed-Hessian fluctuation and limiting physical spectral weight still require evaluation.

## Original kinetic current and its full physical energy

[KC1–KC28](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/KINETIC_CURRENT_AND_PHYSICAL_ENERGY.md) retain the original kinetic quotient and its complete conditional mean, and decompose the full current into kinetic and score fluctuations. The actual kinetic variance has a boundary-count bound with all nonnegative energy remainders. Its first two moments control the full kinetic column of the conditional inverse at the original shrinking energy. Differentiating its conditional mean gives the exact full physical energy, including a retained conditional covariance. That covariance supplies an explicit enlargement of the physical scalar trial space, an exact Green-function gain and its full residual. The source gain and limiting physical spectral weight remain unevaluated; the complete earlier current family remains available.

## Complete local energy and physical spectral windows

[LE1–LE23](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/LOCAL_ENERGY_PHYSICAL_WINDOWS.md) add the entire retained inside-energy fluctuation to the conditional kinetic vector. Its full physical gradient is the original projected boundary field. Complete norm, first-moment and second-moment identities retain all scalar energies and cross terms; explicit upper and lower bounds are proved. The original supported observable has zero mixed first energy but a retained ordinary covariance and mixed second moment. Its full two-vector Green calculation includes the complementary physical residual. An invertible coefficient map proves that the complete inside-function trial space is the existing KC space, preventing a spurious additional gain. The original full-Hamiltonian shrinking-window tails are bounded; the actual surviving norm and source mass remain unevaluated.

## Smooth spatial energy and exact sector covariances

[WH1–WH33](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SMOOTH_WEIGHTED_LOCAL_ENERGY.md) construct the complete original energy with smooth spatial weights and calculate its full physical forcing, including exact face-trace cancellation. A comparison for every actual edge subset and an exact finite level decomposition prove a variance bound while retaining all nested-sector covariances. The noncommuting weighted-sector defect is computed explicitly. The original observable trace has an evaluated limit; its subtracting covariance and all distinct-face energy contractions remain. Complete norm, first-energy and second-moment matrices give the scalar Green gain and full physical residual, including dependent-vector cases. Original shrinking-window upper functions improve. The exact one-face physical vector vanishes, demonstrating why surviving mass requires the actual coupling between faces. No limiting spectral mass is assigned.

## Shared-face physical coupling and the complete exterior state

[SF1–SF27](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SHARED_FACE_WORDS_AND_PHYSICAL_COUPLING.md) evaluate the original shared-edge contraction as an exact difference of six-edge and eight-factor Wilson words, with every traversal sign and enlarged support count. The seven-edge two-face graph has an explicit physical Haar isometry and a retained mixed Casimir. Its weighted-energy fluctuation has strictly positive norm for every positive coupling whenever the two face averages do not sum to twice the shared-edge weight. The full original lattice marginal has an exact receiving equation that retains the exterior energy, conditional kinetic contribution and complete variance. These formulas connect the finite interaction mechanism to the original state without assuming a surviving continuum spectral mass.

## Actual-vacuum edge variance and surrounding-loop energy

[EV1–EV29](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_EDGE_ENERGY_VARIANCE.md) prove strictly positive edge-energy variance for every edge in the original full vacuum, including boundary edges. The exact decomposition retains the raw fiber-ground overlap, its full mass, the mean square and the entire excited remainder. Original surrounding paths determine six-edge loops and an explicit conditional-energy profile with all scalar and metric factors. The local vacuum budget proves averaged alignment of those paths and shows that one extreme-configuration lower estimate decays; it does not prove decay of the actual variance. Complete original-source, cross-edge and smooth-weight maps and full physical moments remain available for the shrinking-window calculation.

## Full ground-family coupling and positive actual raw overlap

[GF1–GF31](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/FULL_HAMILTONIAN_GROUND_FIBER.md) compute the complete original full-Hamiltonian coupling to the positive one-edge ground family, including every outside derivative, potential scalar, complementary inverse and source correction. [RO1–RO17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/RAW_OVERLAP_AND_ORIGINAL_METRIC.md) retain the exact radius-two metric, Haar prefactor and Jacobian to prove a positive local raw overlap and derivative contribution in the actual vacuum. Separate kinetic and potential limits give the exact aligned derivative constant 9/(8 sqrt(m)) and strengthen the local marginal lower coefficient to 27R³/16. The variational overlap constant is proved positive and retained explicitly. The full complementary interaction and original shrinking spectral window remain active calculations; no continuum no-gap endpoint is asserted.

## Full physical lift and original-source spectral windows

[PLF1–PLF26](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/FULL_PHYSICAL_LIFT_AND_SOURCE.md) calculate the complete physical norm, vacuum subtraction and first two energy moments of the coupled ground-family lift. The original Wilson observable differs from an outside multiplier by a proved spectral-amplitude error at most16a_j M_f. At the original scale s_j=100kappa_*a_j, the complete corrected-source error also tends to zero. A three-scale resolvent estimate subtracts low- and high-energy contributions and gives an exact lower bound for the original physical window, with no bounded total source-norm assumption. Every complementary term is retained. The actual signed three-scale value remains to be evaluated; these formulas do not assert a continuum no-gap result.

## Actual filtered currents and the complete inverse contribution

[FTC1–FTC33](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_FILTERED_CURRENT_AND_TAIL.md) transfer the original positive first energy to the outside Wilson source and prove a positive filtered-response bound with its original vanishing scale retained. The complete inverse contribution is located through an exact map from the physical window, including its full metric. Direct optimization of the filtered response retains the original force, every mixed Hessian and all exterior rows in a complete second-moment matrix. Both physical residual norms remain. An explicit comparison measure shows why the moment bounds alone do not establish surviving low-energy weight. The signed three-scale interacting response and the continuum no-gap endpoint remain active calculations.

## Actual score moments and the full second-energy matrix

[SOM1–SOM24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md) prove all even moments and an exponential tail for the actual conditional ground-state score at every outside configuration. A full weighted score/Hessian identity controls the second-energy matrix with all exterior rows and force cross terms retained. Its original source-vector norm is evaluated with explicit removed-face and lattice-sampling errors. The matrix trace bound is sufficient for a fully evaluated filter estimate at its stated vanishing scale; it does not improve the earlier filter bound or establish surviving low-energy weight. Source-directed inverse and residual calculations, reconstruction and the smooth no-gap endpoint remain active.

## Stronger source energy and retained current inverses

[CTI1–CTI39](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURRENT_TAILS_AND_RETAINED_SOURCE.md) prove exponential tails for the complete ground-state current and a stronger lower energy for the unchanged Wilson source:
\[
\begin{gathered}
e'_{\mathbf f}=\max\{e_{\mathbf f},3\kappa_*^2J_t/4\},\qquad
J_t=\sum_d\int t_d^2,\\
\liminf_jE_{h,j}\ge e'_{\mathbf f},\quad
\liminf_jE_{F,j}\ge e'_{\mathbf f},\qquad
\liminf_j\frac{\mathcal W_{h_{e_0}\psi_j}(\theta s_j)}{a_j^3}
\ge\frac{100\theta\kappa_*(e'_{\mathbf f})^3}{D_{\mathbf f}^2}.
\end{gathered}
\]
The full original upper constants and previous lower bound remain; CTI23–CTI26 give the complete formulas and exact strict improvement for the three-orientation tent. CTI24 also proves the finite-source matrix-order bound. This strengthens CE7–CE10, EF3 and FTC4–FTC12 without changing their source, metric or regulator. CTI27–CTI37 retain asymptotically all of the original source-vector norm in a set with a proved lower trial norm and explicit inverse accuracy. The complete omitted-direction Schur term and physical residual remain in CTI32–CTI33. Their signed three-shift contribution, reconstruction and the smooth no-gap endpoint remain active calculations.

## Original source Hessian and the stronger full-source response

[HSF1–HSF17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORIGINAL_SOURCE_HESSIAN_AND_FILTER.md) evaluate the actual source-Hessian limit and retain the original energy inside the finite filter denominator. For both the full original Wilson observable \(X_j=F_j\) and its outside source \(X_j=h_{e_0,j}\), they prove
\[
\begin{gathered}
a_j\mu_j\|\nabla^2X_j\|^2\longrightarrow3J_t+9J_2^\Sigma,\\
\liminf_j\frac{\mathcal W_{X_j\psi_j}(\theta s_j)}{a_j^3}
\ge\frac{100\theta\kappa_*(e'_{\mathbf f})^3}
{\{\kappa_*^2(3J_t+9J_2^\Sigma)+4e'_{\mathbf f}\}^2}.
\end{gathered}
\]
HSF1–HSF6 retain all signed Hessian terms, original face counts and finite errors. HSF7–HSF9 prove the complete energy-dependent comparison; every original upper and lower constant remains available. HSF10 gives coefficient \(100\theta\kappa_*^3R^3/363\) for the unchanged three-orientation tent. HSF11–HSF15 apply the bound directly to the full original observable and retain every cross term in its exact relation to the outside source. This strengthens FTC12 and CTI23 while keeping the factor \(a_j^3\). The signed original-window response, full inverse and residual contributions, reconstruction and the smooth no-gap endpoint remain active calculations.

## Complete residual and exact stereographic current

[TCR1–TCR21](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/TWO_SIDED_CURRENT_RESIDUAL.md) give complete two-sided bounds for the original filtered response and its signed three-shift window. They retain the actual least-squares defect and the original uncut trial metric. Projection orthogonality and a direct singular-value estimate prove
\[
\|\widetilde c\|\le\sqrt{2q_R/\gamma},\qquad
\sqrt{\kappa_*/z}\,\epsilon_R\|\widetilde c\|
=O\!\left(a_j^{\rho-3}\sqrt{\log(1/a_j)}\right).
\]
With the original CTI13 cutoff, every \(\rho>9/2\) makes this cutoff contribution \(o(a_j^{3/2})\); the interacting residual remains to be evaluated.

[SC1–SC24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/STEREOGRAPHIC_CURRENT_AND_CUBIC.md) supply the exact stereographic coordinate, density, radius-two metric and state maps for those integrals. Gauge invariance proves that each unfixed original link has a Haar marginal: its stereographic moments are finite exactly below order three. SC8–SC15 retain every rational face term and prove that the local density approximation in Chatterjee, [arXiv:2401.10507v4](https://arxiv.org/abs/2401.10507v4), label “approxdens”, omits a cubic nonabelian contribution. The full-density counterexample and corrected expression are proved without claiming that the source's main scaling theorem fails. This extends OW's ordered-action comparison and prevents an invalid polynomial-moment substitution in the current calculation. Actual window values, reconstruction, intended-theory identification and the smooth global no-gap endpoint remain active work.

The subsequent calculation [SC18–SC24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/STEREOGRAPHIC_CURRENT_AND_CUBIC.md) evaluates all five rational action terms in the actual vacuum, including with bounded gauge-invariant score multipliers. Its original four-link tensor average is
\[
\mu(q_1^a q_2^b q_3^c q_4^d)
=\frac{\mu\operatorname{Tr}U_p}{128}\,
\frac12\operatorname{Tr}(E_aE_bE_cE_d).
\]
This determines every signed term in SC10 and their exact cancellation on the original coupling path. SC24 also gives the full force pairing in original staple-loop and two-plaquette expectations, with all orientations, original coefficients and remaining mixed score moments retained. These identities evaluate gauge averages; they do not yet evaluate the complete residual or establish the no-gap endpoint.

## Positive current measures and individual plaquette means

[CFC1–CFC26](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CENTERED_CURRENT_COVARIANCE.md) construct the positive original-configuration measure
\[
d\nu_e=\frac{\kappa(2R_e+G_e)+(3b/4)\sum_{p\ni e}D_p}{6b}\,d\mu .
\]
Its exact mixture and full source retain twice the force pairing. A deterministic subset carrying at least three quarters of the original squared source-norm limit has uniform tilted score tails and a trial inverse lower bound without the earlier logarithmic loss. The full complementary block and physical residual remain.

CFC22–CFC26 prove an individual-face lower mean, the resulting lower density \(3\kappa_*/16\) for every orientation of the limiting spatial vacuum mean, and
\[
K_R^{\rm kin}=\min\{K_R,\mathsf L_R-9\kappa_*R^3/16\},\qquad
\limsup a_j^2(\Lambda_Q-d_Q)\le K_R^{\rm kin}.
\]
This strictly improves the kinetic ceiling when \(\kappa_*R<128/3\), and the original gradient-trial response constants are rederived. All finite roots, counts and crossing terms remain. The force upper bound uses the original \(K_R\), not this kinetic ceiling. Spatial mean domination is not an operator lower bound for every vector or a smooth continuum field. The signed interacting source/Gram evaluation, reconstruction and smooth global no-gap endpoint remain active calculations.

## Exact density flux and stronger physical residual

[DF1–DF21](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md) evaluate the positive-density potential and its original-observable receiver:
\[
Y_e=\frac{\Delta_ew+2T_e}{6b},\qquad
\nu_eX-\mu X=\frac{\kappa}{6b}\mu\langle d\Delta_ew,dX\rangle .
\]
The proved mean difference is uniformly \(O(\sqrt{a_j})\) on the retained source set, using the unchanged bounded energy of the full growing observable. This requires no uniform spectral gap and retains every outside derivative.

The full collective calculation also gives
\[
\mathsf B_zc=(PD_z\mathsf Cc,zP^\perp\mathsf Cc),\qquad
z^2\mathsf N\le\mathsf Z_\star=\mathsf B_z^*\mathsf B_z\le\mathsf Z .
\]
The original force graph proves strict removal of the curl cost on every nonempty proper trial patch. The optimized augmented residual is strictly improved at at least two of the three original window shifts for all sufficiently large regulators. Complete gain formulas, projected physical norms, complementary penalties and actual cutoff errors remain in the two-sided spectral bounds. The signed window still requires the collective moments and full residual; no limiting spectral weight or smooth interacting no-gap endpoint is assumed.

## Quantitative force curl on the original patch

[QCF1–QCF16](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/QUANTITATIVE_FORCE_CURL.md) calculate the full ordered SU(2) mixed-face Hessian and weighted codifferential. They retain both inverse signs, the complete second face moment, every coface neighbor and outside score. The complete original face graph has the exact patch constant
\[
\mathcal G(c)\ge16\sin^2\!\left(\frac{\pi}{2q}\right)\|c\|^2,
\qquad q=\lceil R/a\rceil+3,
\]
with an explicit unscaled attaining field. The actual projected-current matrix then satisfies
\[
\mathsf Z-\mathsf Z_\star\ge m_{C,Q}(a)I,\qquad
\frac{m_{C,Q_j}(a_j)}{a_j^3}
\longrightarrow\frac{\pi^2}{32\kappa_*R^2}.
\]
The finite constant is given completely in QCF14, and the limit concerns that proved lower bound. QCF16 propagates it into the exact optimized residual gain while retaining its raw coefficient norm and both remaining positive terms. The collective signed source and physical residual still determine the original spectral window; no limiting mass or smooth interacting no-gap endpoint is assumed.

## Joint source graph and spatial force bounds

[QG1–QG20](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/THREE_SHIFT_GAINS_AND_SOURCE_GRAPH.md) quantify the original three-shift augmented gains and evaluate the actual raw-source graph:
\[
a_j^{-3}\mathcal G(\mathsf b_{I_j})\longrightarrow9J_{\rm an},
\qquad
J_{\rm an}=\int\sum_{d<k}(t_d-t_k)^2.
\]
The complete face incidence improves the graph-norm constant from24 to16 and strengthens the retained-source estimates. The exact joint leading matrix has the equal-component test space as its kernel. On that space, the full original summation-by-parts calculation gives
\[
\mathbf f=(\varphi,\varphi,\varphi):\qquad
\liminf a_j^{-5}\mathcal G(\mathsf b_{I_j})
\ge36\mathcal E(\varphi),
\]
where \(\mathcal E\) is the extended Dirichlet energy. No derivative regularity of the vacuum means is assumed. QG18–QG20 propagate these results into the full joint source-force matrices at their original \(a_j^4\) and \(a_j^6\) scales, preserving mixed entries, raw coefficient norms and the complete Hessian-pair term. The noncommuting inverse and signed physical residual still determine the spectral window; no limiting mass or smooth interacting no-gap endpoint is assumed.

## Exact source Green limit and physical inverse receiver

[GG1–GG15](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/EXACT_PATCH_GREEN_AND_PHYSICAL_RECEIVER.md) give the complete original patch Green matrix, including every longitudinal boundary mode and its raw sine norm. They evaluate the actual interacting source form:
\[
a_j^{-1}\mathsf b_{I_j}^*\mathsf G_{I_j}^{-1}\mathsf b_{I_j}
\longrightarrow
\frac94\langle h,\mathcal T_Rh\rangle,
\qquad h=f_{12}+f_{13}+f_{23},
\]
where \(\mathcal T_R\) is the fully specified Dirichlet inverse on the original physical support cube. The proof retains the full vacuum error and bounds every high and boundary mode before taking the limit. Together with QG's angular graph form, the joint limit detects every original test combination except exact zero relations. GG6–GG8 and GG14 construct the exact noncommuting map through the actual physical matrix \(Z\), preserving its nine shift-moment terms, dependent-frame kernel, graph projection residual, full Hessian-pair term and remaining optimized residual. The retained-set correction is explicit in GG13. Evaluation of the signed physical window and construction of the smooth interacting no-gap state continue.

## Actual kinetic profiles and joint shift moments

[KP1–KP17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md) construct actual subsequential kinetic profiles and prove
\[
0<\tau_d\le3/\kappa_*,\qquad
\sum_d\int_{\mathcal Q}\tau_d^{-1}\le16K_R/9.
\]
The full first current-energy matrix obeys
\[
0\le Q_j\le15a_j^2/\kappa_*,
\]
with its entire positive Hessian remainder retained. One constructed actual subsequence carries the kinetic profiles, a bounded first-energy operator and every member of a finite original test family. KP11 evaluates four joint Green moments, including both mixed entries, at their unchanged \(a_j^5,a_j^6,a_j^7\) scales. KP16 gives the original source norm and energy matrices; KP15 proves their local relation to the plaquette-mean measures. The five remaining moments retain the complete current-span residual in KP13, and KP17 identifies the exact remainder-saturation space for further calculation. All raw coefficient factors, shift powers and physical residuals remain; the smooth interacting no-gap goal continues.

## Full current complement and its relative-energy measure

[CSR1–CSR21](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md) construct the full current-span Schur response with its corrected source and both physical solution components. The actual complementary coupling measure satisfies
\[
M_j([0,\theta s_j])\le1500\theta a_j^3I,\qquad
\int\lambda^{-1}dM_j(\lambda)\le Q_j .
\]
A common actual subsequence gives a bounded relative-energy measure with both endpoint atoms retained. It evaluates the effective current energy and the full complementary lift's norm and energy at their original \(a_j^4,a_j^5\) scales. The exact effective kernel includes KP17's current-trial kernel; the full physical projection and source cross measure remain in the response. All three original shifts, raw coefficient norms and complementary contributions are preserved. The signed physical window and smooth interacting no-gap endpoint remain active calculations.

## Exact physical scalar receiver and stronger original-state bounds

[PFR1–PFR19](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHYSICAL_SCALAR_RECEIVER_AND_CURRENT_COVARIANCE.md) prove the full scalar receiver for the physical current Schur lift, including both density/score-fluctuation mixed terms. The exact diagonal Hessian defect, with all exterior rows retained, improves the actual state bounds to
\[
a_jT_e\le\Theta_0(a_j)<\frac3{2\kappa_*},\qquad
\liminf_j\frac{\mu_jD_p}{a_j}\ge\frac{3\kappa_*}{8},\qquad
0\le Q_j<\frac{9a_j^2}{\kappa_*}I .
\]
The plaquette inequality uses PFR12's uniform finite lower root; it holds along any sequence of original faces. PFR13–PFR16 strengthen the finite local budget, spatial mean floors and original observable's first-energy and resolvent coefficients. The force/source upper constant \(K_R\) is unchanged.

The KP kinetic profiles now have ceiling \(3/(2\kappa_*)\). CSR10's complementary low-energy bound is \(900\theta a_j^3I\), CSR13's measure total is at most \(9/\kappa_*\), and CSR16's derivative ceiling is \(9m!/(\kappa_*\theta^m)\). The retained finite norm terms in CSR15 and CSR19 are bounded by \(150\theta a_j^2\) and \(150a_j^2\). Earlier weaker bounds remain valid. PFR17–PFR19 supply the complete equal-time scalar covariance, inverse-energy bound and explicit positive trace defect. All raw coefficient errors, original shifts, cross covariances and physical complementary components remain. Positive first energy does not yet establish positive mass in the original shrinking spectral window; that calculation and the smooth interacting continuum endpoint remain active.

## Actual physical spectral measure and its total kernel

[PSC1–PSC10](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PHYSICAL_SCORE_SPECTRAL_MEASURE.md) construct the actual physical current-norm measure and its complete joint source/energy measure on the original relative-energy interval. They prove
\[
\ker\mathcal M([0,\infty])\cap L^2(\mathcal Q;\mathbb C^3)=\{0\},
\qquad
d\mathcal C_j(r)=100a_j^2r\,d\mathcal M_j(r).
\]
The first statement concerns the total physical measure, including both endpoint atoms. The second preserves the exact map to the leading score covariance, whose original-scale limit is \(\mathcal G\delta_\infty\). Its possible zero coefficient is retained.

PSC7 keeps the surviving original source in one positive block measure. PSC8–PSC9 give all physical cross-shift norm, energy, source and original signed-window limits with their full factors and signs. PSC10 identifies the different kernels obtained when infinity or both endpoints are excluded. Thus total injectivity is proved without assigning it to finite relative energies. The actual allocation of mass and the sign of the original three-shift window remain active calculations toward the smooth interacting continuum no-gap goal.

## Original gauge constraints and stronger actual-state bounds

[GWH1–GWH15](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GAUGE_HESSIAN_AND_COVARIANT_GRAPH.md) differentiate the original vertex gauge invariance with its full connection term, apply both endpoint constraints, and retain every outside Hessian row. They prove the stronger actual ceiling and the physical norm correction
\[
\begin{gathered}
\Theta_G(a)=\frac{-3a/2+\sqrt{9a^2/4+144/[\kappa_*^2(7/5)]}}8,
\qquad a_jT_e\le\Theta_G(a_j)<\frac3{2\kappa_*}\sqrt{\frac57},\\
\mathsf C_j^*P\mathsf C_j+\mathsf V_{g,j}\le\mathsf N_j,\qquad
c^*\mathsf V_{g,j}c
=a_j^4\mu\langle K_U^*D_cg,(K_U^*K_U)^\dagger K_U^*D_cg\rangle .
\end{gathered}
\]
The original full gauge graph, holonomy transports and all gauge zero modes remain. Horizontality of the physical exact-current columns follows from their proved gauge invariance and projection equivariance. The full row minimum and its complete residual are GWH8–GWH9.

GWH6 and GWH12–GWH15 propagate the finite root through the complete current and scalar covariance bounds, complementary spectral measure and derivatives, original cube budget and oriented means, first-energy and both original resolvent trials, and the exact density variance. The scalar-score low-energy ceiling is \(100\theta\Theta_G(a_j)\); the current energy ceiling is \(a_j^2(3/\kappa_*+4\Theta_G(a_j))\). The complete four mixed density/score terms, raw coefficient errors and source upper constant \(K_R\) remain. The actual physical total satisfies
\(\mathcal M([0,\infty])+\mathcal V_g\le M_{\mathbf1_{\mathcal Q}\tau}\).
These strengthen the existing receivers without assigning physical mass to a spectral interval. The original window and interacting smooth global no-gap endpoint remain active.

## Full gauge-current matrix and exact dynamic curl

[GCM1–GCM16](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GAUGE_CURRENT_COVARIANCE_AND_DYNAMIC_CURL.md) retain the complete vertex cross covariance and prove the full matrix lower bound
\[
\mathsf V_g\ge a_j^4\mathsf A_0\mathsf A_1^\dagger\mathsf A_0
\ge\frac{a_j^4}{12}\mathsf A_0,\qquad
\mathsf A_0=\mu B_U^*B_U,\quad
\mathsf A_1=\mu B_U^*(K_U^*K_U)B_U .
\]
The physical source-energy receiver keeps this entire correction. Its scalar inverse and continuum inverse-half domains are proved in GCM6–GCM9. The single-edge bound \((\mathsf V_g)_{ee}\ge2\mathsf N_{ee}/7\) is a diagonal statement: the full original constant list has \(\mathsf V_g\mathbf1=0\) and \(P\mathsf C\mathbf1=\mathsf C\mathbf1\). No factor inferred from the diagonal replaces the actual matrix.

The original contraction \(\mathscr T\alpha=K_U^*\alpha^\sharp\) satisfies
\[
\mathscr T L_1-L_0^{\mathbb V}\mathscr T
=\kappa_*\mathscr R\,d,\qquad
\mathscr R\omega=\mathscr S_U((*_e\omega_{ee})_e).
\]
GCM13–GCM16 prove every connection sign, the \(12\) degree bounds, the current identity with zero initial diagonal curl, and the complete two-form resolvent correction. GCM10–GCM12 construct the graph-energy receiver for a common smooth spatial weight, with no infinity atom at \(\lambda/a_j^2\). Its connection to physical time energy \(\lambda/s_j\) remains the exact norm and dynamic maps above. All endpoint atoms in the physical measure, original raw coefficients, mixed scalar kernels and the signed physical window remain.

## Exact force receiver and common physical source

[TFC1–TFC26](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/TWO_FORM_FORCE_AND_COMMON_SPECTRUM.md) prove the full original force-curl receiver, including
\[
L_2d\mathsf Cc=-a_j^2d(D_cdV),\qquad
\mathsf N^\perp=\kappa_*a_j^4
\int_{(0,\infty)}\lambda^{-3}\,d\Omega_j(\lambda).
\]
The actual force covariance tends strongly to \(9/\kappa_*^2\) times the direction-difference projection on the original support cube. Its kernel is exactly the common-coefficient subspace. For a common \(C_c^1\) coefficient, TFC15 evaluates the next spatial term and TFC21–TFC22 prove a uniform removed-current second moment at the unchanged energy. All face deficits, their second moments, outside neighbors and limiting zero atoms remain.

The original common plaquette observable \(X_{\varphi,j}\) and the explicitly defined centered squared-score observable \(Q_{\varphi,j}\) satisfy
\[
dX_{\varphi,j}+dQ_{\varphi,j}
=-\frac{\kappa_*a_j}{2}L_1P\mathsf Cc_j+Pe_{\varphi,j},
\qquad \|e_{\varphi,j}\|=O(a_j).
\]
TFC23–TFC25 prove the complete low-band and original three-shift comparisons. The displayed scaled response error is \(O(a_j)\); its unscaled error is only \(O(1)\), and no positive window sign is inferred. TFC26 proves that the leading full Hessian-pair remainder kills the common subspace, with \(\mathcal Qh=\kappa_*\mathcal Gh\) there. These formulas strengthen the existing physical, score and force receivers while leaving the actual spectral allocation and interacting smooth global no-gap construction active.

## Exact scalar source and full positive-energy band

[TSC1–TSC12](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SCALAR_COMMON_SOURCE_RECONSTRUCTION.md) integrate the common-source gradient identity with every original centering constant:
\[
X_{\varphi,j}+Q_{\varphi,j}
=\frac{\kappa_*^2a_j^3}{2}B_{c_j}+r_{\varphi,j},
\qquad r_{\varphi,j}=\kappa_*L_0^{-1}\delta_\mu e_{\varphi,j}.
\]
The full scalar score term has norm \(O(\sqrt{a_j})\). For every Borel subset \(B\subset[\epsilon s_j,\infty)\), the exact finite estimate proves
\[
\|E_0(B)(X_{\varphi,j}+Q_{\varphi,j})\|
\le d_{\varphi,j}(\epsilon s_j)=O(\sqrt{a_j}).
\]
Consequently the original \(X\) and squared-score \(Q\) masses have equal extended liminf and limsup on every such sequence of bands, including the original shrinking annulus. This compares the actual unweighted physical masses without assigning a positive value to either one. TSC8–TSC9 retain all three original response shifts and give explicit signed bounds. TSC10–TSC12 evaluate the actual mixed density/score covariance combination and give a whole-variance floor of order \(a_j\). The weighted Poisson residual at zero, all mixed terms and original coefficient norms remain. The spectral allocation and smooth interacting continuum no-gap construction continue.
