# Yang–Mills heat correlations and the full physical complement

This edition studies how local plaquette observables evolve under the heat flow of the interacting SU(2) lattice Hamiltonian, and how much their inverse-energy states interact with the rest of the physical Hilbert space. It includes the complete fourth-order heat calculation, then a continuation whose heat-error bounds do not grow with the box. The latter also constructs a spatial-volume limit at fixed lattice spacing and bounds the energy change when all complementary physical states are allowed to relax.

Start with the [mathematical reader](reader/yang_mills_heat_volume_20260921.pdf): it introduces the original objects, states the results and explains their connections, then includes all five complete proof manuscripts. The [standalone editable LaTeX](reader/yang_mills_heat_volume_20260921.tex), [complete Markdown](reader/yang_mills_heat_volume_20260921.md) and [reader build instructions](reader/BUILDING_READER.md) accompany it. The complete coefficient tables and executable checks are available below, not only this overview; earlier [LaTeX manuscripts](../../README.md#full-proofs-and-editable-latex) remain available separately.

## Read the arguments

The [archived edition on Zenodo](https://doi.org/10.5281/zenodo.22803564) includes the new reader as its default preview, both cumulative source archives, the earlier readers and the dated attribution clarification. The five new source manuscripts retain their original bytes.

| Manuscript | Contents |
| --- | --- |
| [Physical heat coefficients and first excitation band](package/workbench/yang-mills/continuations/20260921-heat-response-transfer/PHYSICAL_HEAT_COEFFICIENTS.md) | All fourth-order time functions, their original geometric assembly, and the first-band matrix with its actual Gram correction. |
| [All-time remainder and original metrics](package/workbench/yang-mills/continuations/20260921-heat-response-transfer/HEAT_REMAINDER_AND_NATIVE_METRICS.md) | Finite-box analytic error, inverse-energy moments, and a genuine interval of positive correlation. |
| [Heat, observation and quotient transfer](package/workbench/yang-mills/continuations/20260921-heat-response-transfer/RH_HEAT_TRANSFER.md) | Explicit receiving maps for the heat/Gram and inverse-power constructions used in the Riemann workbench. |
| [Volume-independent heat](package/workbench/yang-mills/continuations/20260921-volume-heat-return/VOLUME_UNIFORM_HEAT.md) | Local source construction, scalar mean, generator domain, full-row estimate, and the fixed-spacing spatial limit. |
| [Growing observation families and their full complement](package/workbench/yang-mills/continuations/20260921-volume-heat-return/GROWING_OBSERVATIONS_AND_COMPLEMENT.md) | Boundary-safe coefficient sums, original state and energy forms, and minimization over the entire complementary space. |

[Complete cumulative mathematical text](package/CUMULATIVE_RESEARCH.md) · [Browse every supplied file](package/) · [Download the volume edition](archives/yang_mills_cumulative_20260921_volume.zip) · [Download the preceding heat edition](archives/yang_mills_cumulative_20260921_heat.zip)

## The operator and the measured correlation

On each original open cubic box with vertices $\{-L,\ldots,L\}^3$, $L\ge2$, let $W_p$ be the fundamental trace around plaquette $p$. The Hamiltonian is

$$
H_L=\kappa K_L+\kappa\xi\sum_{p\in\mathsf P_L}(2-W_p),
\qquad \kappa=\frac{2g^2}{a},\qquad \xi=\frac1{4g^4}.
$$

Here $K_L$ is the original sum of link Casimirs, $a>0$ is lattice spacing, and all vertex gauge constraints, including the boundary constraints, are retained. Write $\psi_L$ for the positive unit vacuum, $A_L=H_L-E_{0,L}$ for energy measured above it, and $\rho_L=\psi_L^2$. The centered plaquette state is $r_p=(W_p-\langle W_p\rangle_{\rho_L})\psi_L$. Its connected heat correlation is

$$
\widehat C_{L,pq}(\tau;\xi)=\langle r_p,e^{-\tau A_L/\kappa}r_q\rangle,
\qquad \tau=\kappa t.
$$

The first calculation supplies 84 exact time functions with rational Laplace transforms across 17 geometric cases. For the original $L=2$ box they assemble the full 240-plaquette matrices at orders zero, two and four. Their time integrals recover the preceding static response. The first-band calculation retains the matrix ordering in $T_4$ and its nonidentity Gram; its own remainder remains finite-volume. See H4 and H8 of the [coefficient manuscript](package/workbench/yang-mills/continuations/20260921-heat-response-transfer/PHYSICAL_HEAT_COEFFICIENTS.md).

## A heat remainder independent of the box

Let $\|B\|_{\mathrm{row}}=\max_p\sum_q|B_{pq}|$. Sections U3–U8 of the [volume proof](package/workbench/yang-mills/continuations/20260921-volume-heat-return/VOLUME_UNIFORM_HEAT.md) construct the source and semigroup on explicit coefficient domains and obtain

$$
\left\|\widehat C_L-C_{0,L}-\xi^2C_{2,L}-\xi^4C_{4,L}\right\|_{\mathrm{row}}
\le512e^{-3\tau/2}\frac{\theta^6}{1-\theta^2},
\qquad \theta=\frac{|\xi|}{R_0},\quad R_0=\frac3{256},
$$

for every $L\ge2$, $|\xi|<R_0$ and $\tau\ge0$. Unlike the earlier entrywise estimate with radius $1/|\mathsf P_L|$, this controls an entire row with constants independent of volume. U29b supplies a second bound with radius $45/4096$, prefactor $6184/25$ and decay $15/8$; its smaller circle and sharper constants are both retained.

Local coefficient agreement together with these tails gives the spatial-volume limit in U9. This is an infinite spatial lattice at fixed $a$ and admissible $g$, not a limit as the lattice spacing tends to zero.

## What happens when the whole complementary space is included

Let $R$ be the column map with columns $r_p$, and put $\Phi=\kappa A_L^{-1}R$. The original forms are

$$
G^{(0)}=R^*R,\qquad G^{(1)}=R^*\Phi,\qquad
G^{(2)}=\Phi^*\Phi,\qquad E=\Phi^*A_L\Phi=\kappa G^{(1)}.
$$

They are computed from the heat coefficients and bounded with the complete remainder. For every $L\ge2$, $a>0$ and $g^2\ge16$, the sharpened M10 estimates give

$$
\|G^{(0)}-I\|<\frac{124}{10^6},\qquad
\left\|G^{(1)}-\frac13I\right\|<\frac{66}{10^6},\qquad
\left\|G^{(2)}-\frac19I\right\|<\frac{36}{10^6}.
$$

These estimates matter because the plaquette family is not assumed to be a reducing subspace. With $P=\Phi(G^{(2)})^{-1}\Phi^*$, $Q=I-P$, $B=QR$ and the self-adjoint complementary operator $D=QA_LQ$, the energy of $\Phi c+h$, $h\in Q\mathcal H_0$, includes the mixed term $2\kappa\operatorname{Re}\langle Bc,h\rangle$. Minimizing over the full complementary form domain gives

$$
h_{\min}(c)=-\kappa D^{-1}Bc,\qquad
E_{\mathrm{full}}=E-\kappa^2B^*D^{-1}B.
$$

The domain and inverse are established in M5. M10 then proves, on the same domain of parameters,

$$
\frac{999}{1000}E\prec E_{\mathrm{full}}\preceq E,
\qquad
G^{(2)}\preceq G_{\mathrm{restored}}\prec\frac{1001}{1000}G^{(2)}.
$$

Thus allowing every complementary state to relax lowers the original family energy by less than one part in a thousand, while increasing its state Gram by less than one part in a thousand. These are inequalities between quadratic forms in the original coefficients, not entrywise ratios. M8 carries the bounded maps and estimates to the infinite plaquette family. M10 also gives weaker, explicit bounds at $g^2\ge10$ and $g^2\ge12$. [Full argument and constants](package/workbench/yang-mills/continuations/20260921-volume-heat-return/GROWING_OBSERVATIONS_AND_COMPLEMENT.md).

## Correlations, quotient metrics and the next domain question

For the opposite faces $p=(0,0,0;0,1)$ and $q=(0,0,1;0,1)$, at $\xi=10^{-10}$, the complete correlation is positive throughout $1/\kappa\le t\le3/\kappa$, in every $L\ge2$ and in the constructed spatial limit. At $t=1/\kappa$, M26 bounds $C_{pq}/\xi^4$ between $85910/10^7$ and $85920/10^7$. This uses the all-order error, not just the sign of a truncated coefficient.

The heat columns $\Phi_T=(I-e^{-TA_L})\Phi$ retain the forcing defect $A_L\Phi_T=\kappa R-\kappa e^{-TA_L}R$. Their state and energy comparisons pass to restrictions and quotient minima over the same coefficient fibers. At $g^2\ge16$, $T=10/\kappa$ gives error below $4\times10^{-10}$ for any four specified signed log-determinant returns with ranks at most 240, in every exterior volume. M24–M25 give the explicit rank-dependent horizon for growing families.

The [transfer manuscript](package/workbench/yang-mills/continuations/20260921-heat-response-transfer/RH_HEAT_TRANSFER.md) identifies the Riemann-workbench arguments and their Yang–Mills receiving maps. It transfers heat/Gram comparison, quotient minima and original-metric observation inverses; it makes no identification of arithmetic conductors or zeta zeros with gauge fields or physical energy levels.

The [route assessment](package/workbench/yang-mills/continuations/20260921-volume-heat-return/ROUTE_ASSESSMENT.md) evaluates a restart of the elementary source estimate: that certificate reaches the same $3/256$ endpoint. It does not locate an actual source singularity. The shrinking-coupling continuum path eventually leaves the stated strong-coupling domain. A nontrivial four-dimensional continuum field and finite positive continuum mass are not established here.

## Verification and source preservation

Both original archives are preserved unchanged. The volume edition contains all 2,015 supplied files. Of the heat edition's 1,937 files, 1,932 remain at the same paths and five changed control documents are preserved under its history directory. The [source intake record](SOURCE_INTAKE.json) identifies both archives and this preservation check.

Fresh integration checks passed in both ordinary and optimized Python: the volume auditor's 2,425 exact checks and 16 false-formula controls, the heat checker's 879 named checks and 21 controls, and the 52 route calculations. The full package manifest passed before and after those runs; no source bytes changed. [Fresh execution record](checks/EXECUTION.json).

The supplied records additionally contain the full coefficient-production, polynomial and corruption-test executions. Those historical runs are retained, not relabelled as rerun during integration. Neither the finite checkers nor this publication constitute formal or independent external certification of the infinite-dimensional analytic proofs. Earlier analytical reviews retain their own scope.

From the extracted volume archive root, a non-mutating integrity check is `python -B verify_cumulative.py`. The volume checker can be run in its directory with `python -B audit_bounds.py --verify-receipt verification.json`; the heat checker uses `python -B verify.py --verify-receipt verification.json`. Adding `-O` preserves their explicit checks. Full supplied replays regenerate files: use a disposable copy. In particular, the volume replay requires a **new disposable output directory**, since it removes its `fresh/` subdirectory.

Human antecedents and their point-of-use citations remain in the original manuscripts: Schütte–Zheng–Hamer for the exponential-vacuum and character framework, Feshbach–Schur methods for the block return, Eymard for Fourier algebra, and Lumer–Phillips for semigroup generation. The source attributions and existing notices are preserved; no new priority claim is assigned by this integration.

The earlier geometric and material branches also depend on **Levent Alpöge's originating work**: his announced Jacobian polynomial and, separately, the regular-fibre period data of the S6 construction circulated by him and produced with Claude. The [attribution clarification](../../../ATTRIBUTION.md) gives the original sources and exact uses in the older Yang–Mills notes, while distinguishing those inputs from the later state maps and the present heat estimates.
