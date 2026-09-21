# Originating constructions and their use in this workbench

Attribution clarification, 21 September 2026.

Levent Alpöge's work supplies concrete mathematical inputs to this collection, not merely an informal motivation. Two distinct constructions enter different branches. Their original sources must be distinguished from the subsequent coordinate calculations, physical-state maps and analytical estimates developed here.

## The Jacobian counterexample and the material-tensor branch

The polynomial historically called “Fabel/Jacobi” in this workbench is the counterexample [announced by Levent Alpöge on 20 July 2026](https://x.com/__alpoge__/status/2079028340955197566). That announcement credits Akhil for the question and Fable for the work producing the example. With the third coordinate denoted here by $w$, it is

$$
\begin{aligned}
F_1&=(1+xy)^3w+y^2(1+xy)(4+3xy),\\
F_2&=y+3x(1+xy)^2w+3xy^2(4+3xy),\\
F_3&=2x-3x^2y-x^3w.
\end{aligned}
$$

Its determinant is $\det DF=-2$, whereas the three distinct points $(0,0,-1/4)$, $(1,-3/2,13/2)$ and $(-1,3/2,13/2)$ have the same image $(-1/4,0,0)$. Thus local invertibility does not imply global injectivity for this map. The map and this mechanism are source results, not discoveries of the present workbench. [Terence Tao's geometric exposition](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/), dated 21 July 2026, is a separate source for understanding the construction, not a substitute for crediting its origin.

The point-of-use attribution applies to:

- [Fabel/Jacobi coordinate audit](yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_JACOBI_TO_YM_COORDINATE_AUDIT.md), §1: the polynomial, determinant and colliding points.
- [Material-tensor transfer](yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_TENSOR_TRANSFER.md), “Coordinate-level cubic symmetries and the full covector map”: the polynomial immediately before equation (102).
- [Cumulative quantum manuscript](yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/extensive_quantum_blocking.md), the same material-tensor section, and its [TeX addendum](yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/fabel_propagation_addendum.tex).

The material derivative, its inverse-transpose covector, and their later gauge-invariant local-energy state maps are subsequent calculations in those sections. Crediting the input does not attribute these later constructions to Alpöge or identify the polynomial's collision value with a physical energy. The source sections give the actual maps and the mathematical extent of each result.

## The S6 construction and the period-dependent magnetic branch

The S6 programme begins with the complex-threefold construction circulated by Levent Alpöge and produced with Claude, available in the [original manuscript](https://alpo.ge/s6.pdf). Its page 2 “Setup” and §3 specify the regular-fibre period matrix

$$
\Pi(z)=\begin{pmatrix}6\mu(z)&\tau(z)&1&0\\\beta(z)&\mu(z)&0&1\end{pmatrix}.
$$

[Philip Engel's separate exposition, *Complex structures on S6*](https://philip-engel.github.io/S6.pdf), dated 13 September 2026, explicitly credits that origin in its abstract and discusses this same period matrix in §1.3. The original construction and Engel's exposition have distinct authorship and roles.

This is the input to the [retained-cusp calculation](yang-mills/sources/ym_gap_primary_20260908/retained_cusp_nonlinear_bridge.md), §1, and the [magnetic-translation calculation](yang-mills/sources/ym_gap_primary_20260908/magnetic_translation_true_vacuum.md), §1, especially equations (1.2)-(1.4). The latter uses the original imaginary-period block to construct a connection, its explicit frame changes, magnetic link transports and a gauge-covariant map into the full Wilson Hilbert space. The [volume-uniform manuscript](yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md), §19, retains this construction. These are substantive uses of the period data; the physical maps and ensuing estimates are the workbench's later calculations. Their stated hypotheses do not require an independent proof here of the completed threefold's identification with the six-sphere.

The S6 construction is not the July Jacobian counterexample. Giving both the label “Fable” must not merge their provenance or mathematical content.

## The new heat and volume edition

The [21 September heat and volume proofs](yang-mills/consolidation/20260921/) use the original lattice Hamiltonian and their stated local-source, heat-semigroup and Gram-form arguments. Their [transfer manuscript](yang-mills/consolidation/20260921/package/workbench/yang-mills/continuations/20260921-heat-response-transfer/RH_HEAT_TRANSFER.md) identifies the precise heat and original-metric lemmas received from the Riemann workbench. It does not use the Jacobian polynomial or the S6 completion as a hypothesis of the heat estimates. The earlier originating constructions remain part of the research history and have the explicit point-of-use credits above.

## Reading historical editions

Some frozen source texts use “Fabel” without naming Alpöge. That attribution is incomplete: read those passages with the credits and locators above. The five-page S6 reader already names him on its opening page; this clarification makes the actual mathematical dependencies explicit across the current public guides and the new reader. Earlier ZIPs and dated PDFs retain their original bytes so their checksums, equations and citations remain reproducible. This clarification supplements those editions; it does not claim their omissions never occurred.
