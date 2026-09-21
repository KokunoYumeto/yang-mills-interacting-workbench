# Cumulative Yang–Mills reader: physical heat and original metric return

21 September2026. The complete earlier reader follows unchanged as a dated body.
The newly recovered sixth-source documents and the three complete heat/metric
proofs are appended below. This edition preserves the older independent-audit
qualification; it does not relabel historical claims as newly recertified.

## Current complete proofs

- `workbench/yang-mills/continuations/20260921-heat-response-transfer/PHYSICAL_HEAT_COEFFICIENTS.md`
- `workbench/yang-mills/continuations/20260921-heat-response-transfer/HEAT_REMAINDER_AND_NATIVE_METRICS.md`
- `workbench/yang-mills/continuations/20260921-heat-response-transfer/RH_HEAT_TRANSFER.md`

The first gives84 complete time functions and the fourth-order band, the second
an independently proved finite-volume all-time bound and original Grams, and
the third the exact heat/observation/section transfer and quantified errors.
`START_HERE.md` and `CURRENT_STATE.json` contain the active scope.

---

## Preserved reader dated17 September2026

# Cumulative Yang–Mills mathematical reader

This file appends complete preserved proof texts; it does not revise their historical claims into new audited results. The latest scope is stated in START_HERE and in the final two new chapters. The received independent-session report is preserved separately in incoming/.

## Contents
1. `workbench/split_zero_ym/RESEARCH_NOTE.md`
2. `workbench/yang-mills/continuations/20260914-coupled-response/RESEARCH_NOTE.md`
3. `workbench/yang-mills/continuations/20260914-spectral-reconstruction/RESEARCH_NOTE.md`
4. `workbench/yang-mills/continuations/20260914-splitzero-smooth-continuum/RESEARCH_NOTE.md`
5. `workbench/yang-mills/continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md`
6. `workbench/yang-mills/continuations/20260915-actual-loop-moments/RESEARCH_NOTE.md`
7. `workbench/yang-mills/continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md`
8. `workbench/yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md`
9. `workbench/yang-mills/continuations/20260915-gauge-native-band/SECOND_SOURCE.md`
10. `workbench/yang-mills/continuations/20260915-gauge-native-band/SPATIAL_RETURN.md`
11. `workbench/yang-mills/continuations/20260915-uniform-gap-zero-shift/HEAT_BATH_GAP.md`
12. `workbench/yang-mills/continuations/20260915-uniform-gap-zero-shift/OPTIMIZED_DOMAIN.md`
13. `workbench/yang-mills/continuations/20260915-uniform-gap-zero-shift/RESEARCH_NOTE.md`
14. `workbench/yang-mills/continuations/20260915-uniform-gap-zero-shift/VOLUME_LIMIT.md`
15. `workbench/yang-mills/continuations/20260916-cubic-linearized/CUBIC_SOURCE.md`
16. `workbench/yang-mills/continuations/20260916-cubic-linearized/LINEARIZED_RETURN.md`
17. `workbench/yang-mills/continuations/20260917-quartic-cube/PHYSICAL_RETURN.md`
18. `workbench/yang-mills/continuations/20260917-quartic-cube/QUARTIC_SOURCE.md`
19. `workbench/yang-mills/continuations/20260917-quartic-cube/SIXTH_ENERGY.md`
20. `workbench/yang-mills/research-control/RESEARCH_NOTE.md`
21. `workbench/yang-mills/continuations/20260917-fifth-source/FIFTH_SOURCE.md`
22. `workbench/yang-mills/continuations/20260917-fifth-source/PLAQUETTE_RESPONSE.md`


---

# Chapter 1 — split_zero_ym / RESEARCH_NOTE.md

Original text path: `workbench/split_zero_ym/RESEARCH_NOTE.md`.

# Split Zero and the Yang–Mills workbench: retained boundary primitives and spectral memory

Research calculation, 14 September 2026.

## Source ledger and scope

The following public mathematical sources were read. Yang–Mills `main` paths are recorded with this access date; no immutable revision is asserted for those paths. The Split Zero foundational files below are pinned to commit `7ea0a49945390eae14d3160a5730858899768b5f`.

1. Yang–Mills original finite-box Hamiltonian, tree maps, domains, and exact frequencies:
   https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md
2. Yang–Mills complete cubic vertex, equations (179)–(187), and the published rational certificate:
   https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/NONABELIAN_VERTEX.md
3. Yang–Mills six-coordinate band, equations (203)–(209):
   https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/interacting_band_publication_20260909/INTERACTING_TENSOR_BAND.md
4. Split Zero reconstruction and transported-class kernel, sections 1–4:
   https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7ea0a49945390eae14d3160a5730858899768b5f/formal/splitzero/DERIVED_MATHEMATICS.md
5. Split Zero retained jets, section 7.1:
   https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7ea0a49945390eae14d3160a5730858899768b5f/workbenches/split-support-rees-trace/RESEARCH_NOTE.md
6. Current Zeta reader index, including the September 14 continuation:
   https://github.com/KokunoYumeto/zeta-function-research-reader/blob/main/workbenches/splitzero-tandem/continuations/20260914-recursive-source-relations/README.md

The constructions and proofs below concern explicitly defined finite-regulator spaces and the full finite-lattice operator. The executed calculation independently recomputes the 112 frequency blocks underlying the cubic certificate. A four-dimensional continuum mass-gap theorem has not been established in this work.

Run the exact computation with Python 3.10 or later:

```sh
python exact_certificate.py
```

The standard-library program writes `certificate.json`. Every numerical assertion uses integer interval endpoints with denominator `10**40`, or exact rational arithmetic. The program does not use floating point or a network connection. The mathematical proofs of the operator and cohomology identities are given here; the executable has the narrower certificate scope stated above.

## 1. Original vertex and its raw coordinates

Fix the original open box L=2 and retain the spacing a>0. The vertices are n in {-2,-1,0,1,2}^3. There are 125 vertices, 300 positively oriented edges, and 176 maximal-tree chords.

Use the workbench's exact cubic coefficient H^(1), its oscillator vacuum Phi_0, and A_0=H_osc-mu_0. This means the coefficient of the full chart operator, including the kinetic contribution. With p_c=(Kx)_c, v_e=sum_c t_ce p_c and theta_e=sum_c b_ce x_c cross p_c, the vertex polynomial is

\[
q=H^{(1)}\Phi_0=P_3\Phi_0,\qquad
P_3=\frac1{8a}\sum_e v_e\cdot\theta_e
+\frac1{4a}\sum_p A_p\cdot B_p.
\]

The kinetic term follows directly from D^0 Phi_0=-v Phi_0/4 and D^1 Phi_0=theta Phi_0/8. The summed derivatives of v and theta vanish by the alternating colour tensor. Therefore the anticommutator acting on the vacuum contributes -v dot theta/16, and its original prefactor -2/a gives the displayed 1/(8a). The face contribution retains the original ordered Pauli products.

Let Lambda be the set of increasing triples of distinct spatial modes. In the original creation coordinates define

\[
b_I=\sum_{\alpha,\beta,\gamma=1}^3
\epsilon_{\alpha\beta\gamma}
a^\dagger_{i\alpha}a^\dagger_{j\beta}a^\dagger_{k\gamma}\Phi_0,
\qquad
E_I=\frac{\sigma_i+\sigma_j+\sigma_k}{a}.
\]

Then

\[
q=\sum_{I\in\Lambda}d_Ib_I,\quad
A_0b_I=E_Ib_I,\quad
\langle b_I,b_J\rangle=6\delta_{IJ}.
\]

The last equality counts the six nonzero colour assignments. Their oscillator occupations are mutually orthogonal and each assignment has the workbench's original unit vacuum norm. No change to b_I is made.

For the alternating original-chord coefficients c_J, the workbench's coordinate map is

\[
P_3=\sum_{j_1<j_2<j_3}c_J\,
x_{j_1}\cdot(x_{j_2}\times x_{j_3}),\qquad
D=\sqrt2\,G^{1/2}O\Sigma^{-1/2},\qquad
d_I=\sum_Jc_J\det D_{J,I}.
\]

It gives the exact raw identity

\[
\|q\|^2=6\sum_I|d_I|^2
=6c^*\bigwedge^3(2K^{-1})c.
\]

## 2. Apply the Split Zero reconstruction to the actual boundary equation

Put U=span_C{b_I:I in Lambda} and U_J=span_C{b_I:I in J} for every subset J of Lambda. On the join-semilattice P(Lambda), with join given by union, define the actual cochain window

\[
C_J^0=U_J\xrightarrow{\,d_J=A_0|_{U_J}\,}
C_J^1=U\xrightarrow{\,0\,}C_J^2=0.
\]

For J contained in K, the degree-zero map is inclusion, the degree-one map is the identity on U, and the degree-two map is the unique zero map. The cochain square commutes: both routes send sum z_I b_I to sum E_I z_I b_I. The next differential composed with the incoming differential is zero.

The full coordinate isomorphism of the degree-one cohomology is

\[
\Theta_J:H^1(C_J)\longrightarrow\mathbb C^{\Lambda\setminus J},
\qquad
\Theta_J\left(\left[\sum_Iz_Ib_I\right]\right)
=(z_I)_{I\notin J}.
\]

A change by d_J(sum y_I b_I) changes precisely the J coordinates, by E_I y_I. Thus Theta_J is well-defined. Its inverse sends a coordinate tuple to the class of its displayed sum on the omitted indices. Their compositions are identities: the discarded part has the explicit primitive sum_{I in J} z_I b_I/E_I. Every E_I is strictly positive by the original frequency formula.

For J contained in K, the transported-class kernel is consequently computed by

\[
\Psi_{J,K}:\mathbb C^{K\setminus J}
\longrightarrow\ker\bigl(H^1(C_J)\to H^1(C_K)\bigr),
\qquad
(z_I)\longmapsto\left[\sum_{I\in K\setminus J}z_Ib_I\right].
\]

The inverse reads those same coordinates. Surjectivity follows because a class transported to zero has every coordinate outside K equal to zero; quotienting at J removes its J coordinates with the primitive already displayed. Its retained boundary primitive and inherited squared norm are

\[
\pi_{J,K}(z)=\sum_{I\in K\setminus J}\frac{z_I}{E_I}b_I,
\qquad
\|\pi_{J,K}(z)\|^2
=6\sum_{I\in K\setminus J}\frac{|z_I|^2}{E_I^2}.
\]

This is the Split Zero construction R_{P(Lambda)} evaluated on this concrete diagram over C. On its reconstructed total, addition is

\[
(J,[v])+(K,[w])=(J\cup K,[v+w]_{J\cup K}),
\]

supported scalar action is r^bullet(J,[v])=(J,[rv]), and tau acts by the global bottom zero. The equality d_next d_prev is represented by the typed supported-zero map (J,x) -> (J,0).

In particular, the class [q] at empty support belongs to the kernel of the map to full support. Its full-support image is (Lambda,0). The retained datum includes the original kernel element [q] and the unique primitive

\[
u=A_0^{-1}q=\sum_I\frac{d_I}{E_I}b_I.
\]

The actual first vacuum correction in the source is -u. Define its scalar memory on the real domain z<=0 by

\[
M_{\mathrm{vac}}(z)
=\langle q,(A_0|_U-z)^{-1}q\rangle
=6\sum_I\frac{|d_I|^2}{E_I-z}.
\]

Termwise differentiation is valid for this finite sum and gives

\[
M_{\mathrm{vac}}'(0)=6\sum_I\frac{|d_I|^2}{E_I^2}=\|u\|^2.
\]

Thus the terminal supported zero has an explicitly computed transported-class kernel, boundary primitive, and memory derivative.

## 3. Independent 112-block computation and strengthened lower constants

For N=5, retain every j=(j_1,j_2,j_3) in {0,1,2,3,4}^3 having at least two positive entries. There are 112 blocks and sum_j(k_j-1)=176 transverse spatial modes. Set s_j=2 sin(pi j/10), sigma(j)^2=sum_d s_{j_d}^2. With l=n_d+2, use the exact original counting-space functions

\[
v_0(l)=\sqrt{1/5},\quad
v_j(l)=\sqrt{2/5}\cos\frac{\pi j(l+1/2)}5,\quad
w_j(l)=-\sqrt{2/5}\sin\frac{\pi j(l+1)}5.
\]

The index map l=n_d+2 leaves the original physical edge midpoint a(n+e_d/2) unchanged. Put

\[
\phi_{(n,d)}(j)=w_{j_d}(n_d+2)\prod_{h\ne d}v_{j_h}(n_h+2),
\]

with value zero for j_d=0. The complete edge spectral matrix is

\[
\mathcal S_{e,f}
=\sum_j\sigma(j)\phi_e(j)\phi_f(j)
\left(\delta_{d(e),d(f)}-
\frac{s_{j_{d(e)}}s_{j_{d(f)}}}{\sigma(j)^2}\right).
\]

The parent rule decreases the first coordinate, in direction order 1,2,3, exceeding -2. For a chord c, the row b_ce equals -1 on that chord and equals -epsilon(s(c),e)-epsilon(t(c),e) on tree edges. The executable builds these integer paths explicitly.

In the ordered original chords

\[
c_1=((-1,1,-2),2),\quad
c_2=((-1,2,-2),3),\quad
c_3=((-1,1,-1),2),
\]

K_I is the selected chord submatrix of S and Q_I is the selected submatrix of bS. The program independently verifies all eighteen published short entry enclosures and retains its much narrower original intervals in the JSON output.

The kinetic-plus-magnetic coefficient is evaluated as

\[
ac=\frac18\bigl(
-Q_{12}K_{13}+Q_{13}K_{12}
+Q_{21}K_{23}-Q_{23}K_{21}
-Q_{31}K_{32}+Q_{32}K_{31}\bigr)-\frac18.
\]

The last term is checked independently from the ordered face vectors e_1,e_2,-e_3,0, using the exact recurrences A_new=A+z and B_new=B+(A cross z)/2. They give (A dot B)/4=-1/8.

The executed strict rational enclosure is

\[
-\frac{242460588472}{10^{12}}
<ac<
-\frac{242460588471}{10^{12}}.
\]

Define beta=242460588471/10^12. This proves that the absolute value of the corresponding alternating coefficient, after retaining the displayed order or its exact permutation sign, is greater than beta/a.

Every numerical enclosure is proved inductively. Values are stored as integer endpoints divided by M=10^40. Addition and negation are exact; multiplication and division take all endpoint pairs and round outward. Square roots use integer-square bounds at the same denominator. The starting values are sin(pi/10)=(sqrt(5)-1)/4 and cos(pi/10)=sqrt((5+sqrt(5))/8); the angle-addition recurrence supplies the required multiples. For completeness, sin(5theta)=1 at theta=pi/10 implies

\[
16u^5-20u^3+5u-1=(u-1)(4u^2+2u-1)^2=0,
\quad 0<u<1/2,
\]

which selects the stated value of u; the positive cosine follows from 1-u^2. Thus the interval leaves encode exact algebraic trigonometric values.

### Retain the actual largest-frequency multiplicities

The largest spatial frequency and the next distinct one are

\[
\Omega=\sqrt{\frac{3(5+\sqrt5)}2},\qquad
\Omega_2=\sqrt{\frac{13+3\sqrt5}2}.
\]

The largest block is (4,4,4), with transverse multiplicity two. The next blocks are the permutations of (4,4,3). Strict increase of sin(pi j/10) for j=0,...,4 proves these order statements. Consequently the three largest spatial frequencies counted with multiplicity are Omega, Omega, Omega_2.

Let iota insert chord coordinates into all edge coordinates, with zero tree entries. Its counting-space Gram matrix is the identity, and K=iota^* S iota. The matrix K is positive: a vector with zero S energy is a gradient; a gradient vanishing on every tree edge has constant potential along the connected tree, hence is zero on every edge.

The exterior-power morphism is exact:

\[
\bigwedge^3K
=(\bigwedge^3\iota)^*(\bigwedge^3\mathcal S)
(\bigwedge^3\iota).
\]

The squared norm of a wedge of distinct counting-coordinate vectors is one; hence wedge^3 iota is an isometry. The largest eigenvalue of wedge^3 S is Omega^2 Omega_2, the product of the top three eigenvalues with their actual multiplicities. Therefore

\[
0<\bigwedge^3K\preceq\Omega^2\Omega_2 I,
\qquad
\bigwedge^3(2K^{-1})
=8(\bigwedge^3K)^{-1}
\succeq\frac8{\Omega^2\Omega_2}I.
\]

Combining this with the exact raw coefficient identity gives

\[
\boxed{\|q\|^2>
\frac{48\beta^2}{\Omega^2\Omega_2\,a^2}.}
\]

The excitation E_I sums three distinct spatial-mode frequencies, so every such E_I is at most (2Omega+Omega_2)/a. Retaining the original sixfold Gram factor in the spectral sums yields

\[
\boxed{\|u\|^2=M_{\mathrm{vac}}'(0)>
\frac{48\beta^2}
{\Omega^2\Omega_2(2\Omega+\Omega_2)^2},}
\]

\[
\boxed{M_{\mathrm{vac}}(0)>
\frac{48\beta^2}
{\Omega^2\Omega_2(2\Omega+\Omega_2)a}.}
\]

The program also encloses these algebraic constants. The ratio of the new primitive lower constant to the published 14641/(13500000 sqrt(3)) is proved, using the same integer interval operations, to lie strictly between 139/100 and 140/100.

## 4. Exact full nonlinear operator: the restored Gram identity

Retain the full finite-lattice operator on its physical Hilbert space H:

\[
H_g=\frac{2g^2}{a}\sum_e E_e+
\frac1{2g^2a}\sum_p(2-\operatorname{tr}U_p),
\quad a>0,\ g>0,
\qquad A=H_g-\mathcal E_0(g).
\]

Its physical domain is the invariant part of the original Sobolev H^2 domain. The source establishes self-adjointness, compact resolvent and an actual lowest eigenvalue; hence A is nonnegative.

Use the original six S_I in order (11,22,33,12,13,23), and form the pre-projection chart columns

\[
r_I=\mathcal B_g^*\bigl(\chi(gx)S_I\bigr),\qquad
R:\mathbb C^6\to H,\quad Rx=\sum_Ix_Ir_I.
\]

Here B_g^* is the source's exact local Haar-density and chart map, and chi is its fixed invariant smooth cutoff equal to one near the identity. The r_I are smooth original physical vectors. Their independence follows by restricting a vanishing linear combination to that neighbourhood: after removal of the common strictly positive Gaussian and chart density, the six independent quadratic polynomial coefficients vanish individually.

Retain G=R^*R. In particular G is the raw six-by-six Gram matrix. The maps

\[
P=RG^{-1}R^*:H\to H,\quad Q=I-P,
\quad B=QAR:\mathbb C^6\to QH
\]

satisfy P^*=P, P^2=P, PR=R and QR=0 by direct matrix multiplication. Define

\[
D=QAQ:\operatorname{Dom}(A)\cap QH\longrightarrow QH.
\]

This compression is self-adjoint and nonnegative. Here is the domain verification. Because range P consists of finitely many vectors in Dom(A), AP extends to a bounded finite-rank map and PA is its adjoint. Therefore C=QAP+PAQ is bounded self-adjoint. For T>||C||, both I-C(A plus or minus iT)^{-1} are invertible by their Neumann series. Thus A-C is self-adjoint on Dom(A). It is block diagonal for P and Q; its Q block is D. Nonnegativity follows from <u,Du>=<u,Au> for u in Dom(D).

For t>0, D_t=D+t is onto and has bounded inverse with norm at most 1/t. Indeed ||D_tu||>=t||u|| gives closed range, while the orthogonal complement of that range is ker(D_t)=0 by self-adjointness. Define the concrete matrices and lift

\[
F(t)=R^*AR+tG-B^*D_t^{-1}B,
\qquad L_t=R-D_t^{-1}B:\mathbb C^6\to\operatorname{Dom}(A).
\]

The relation being eliminated is exactly

\[
D_t(-D_t^{-1}Bx)=-Bx,
\qquad Q(A+t)L_tx=0.
\]

Its two-support complex has degree-one space QH at both supports, incoming source 0 at the first support, and incoming source Dom(D) with differential D_t at the second. Its transported-class kernel contains the literal vector -Bx; its primitive is -D_t^{-1}Bx. This is the same Split Zero reconstruction applied to the full operator relation.

Entry by entry,

\[
F_{IJ}(t)=\langle r_I,Ar_J\rangle+tG_{IJ}
-\langle B_I,D_t^{-1}B_J\rangle,
\quad B_I=QAr_I.
\]

The resolvent identity gives d(D_t^{-1})/dt=-D_t^{-2}. Since R^*Q=0,

\[
\boxed{F'(t)=G+B^*D_t^{-2}B=L_t^*L_t.}
\]

Each entry on the right is the actual original Hilbert inner product <r_I-D_t^{-1}B_I, r_J-D_t^{-1}B_J>. The cross terms vanish by orthogonality of P and Q.

Direct expansion, using D_t(-D_t^{-1}B)=-B, also gives

\[
\boxed{L_t^*(A+t)L_t=F(t),\qquad F(t)\succeq tG.}
\]

The inequality follows from A>=0 and ||L_tx||^2=||Rx||^2+||D_t^{-1}Bx||^2. In particular F(t) is invertible. The block equations for (A+t)(Rx+v)=Ry read

\[
F(t)x=Gy,\qquad v=-D_t^{-1}Bx.
\]

Therefore the exact compressed resolvent in the original raw coordinates is

\[
\boxed{R^*(A+t)^{-1}R=G F(t)^{-1}G.}
\]

These identities hold for the full H_g displayed above, with its full face words and kinetic terms. The calculation uses no perturbative truncation of that operator.

## 5. Six-band memory, the Split Zero jet morphism, and residue inversion

Retain the source's six comparison vectors S_I, its Delta=2sigma_*/a, and the exact occupation coefficients

\[
c_{I,n}=\langle h_n\Phi_0,H^{(1)}S_I\rangle,
\qquad \omega_n=\sum_{i,\alpha}n_{i\alpha}\sigma_i/a,
\qquad |n|=3\text{ or }5.
\]

The complete physical cubic action has precisely the retained three- and five-creation terms; its degree-one physical projection vanishes. Consequently omega_n-Delta>=sigma_*/a on these index sets. The finite matrix function

\[
\Sigma_{IJ}(z)=\sum_{|n|=3,5}
\frac{\overline{c_{I,n}}c_{J,n}}{\omega_n-z}
\]

is holomorphic near Delta. Direct differentiation yields

\[
\mathsf K=V-\Sigma(\Delta)-E^{(2)}I,
\qquad
\boxed{\Sigma'_{IJ}(\Delta)
=\sum_n\frac{\overline{c_{I,n}}c_{J,n}}{(\omega_n-\Delta)^2}
=(G_2)_{IJ}.}
\]

Thus the source's second-order energy matrix and raw first-correction Gram matrix are a value and derivative of this one exact finite memory function. The vacuum correction E^(2) is retained in the energy identity.

For the typed Split Zero morphism, let A_h=C{h}, the algebra of holomorphic germs at zero, and let epsilon^2=0. Define

\[
j^1:A_h\to\mathbb C[\epsilon]/(\epsilon^2),
\quad f\mapsto f(0)+\epsilon f'(0),
\qquad
\operatorname{ev}_0:\mathbb C[\epsilon]/(\epsilon^2)\to\mathbb C.
\]

The product rule proves that j^1 is a ring homomorphism, including its exact coefficient of epsilon. Apply the source's scalar G-construction to these commutative rings, entry by entry. For

\[
E_{IJ}(h)=\Sigma_{IJ}(\Delta+h)-\Sigma_{IJ}(\Delta),
\]

the actual typed sequence is

\[
G(A_h)\xrightarrow{G(j^1)}G(\mathbb C[\epsilon]/\epsilon^2)
\xrightarrow{G(\operatorname{ev}_0)}G(\mathbb C),
\qquad
E_{IJ}^{\bullet}\longmapsto
(\epsilon(G_2)_{IJ})^{\bullet}\longmapsto0^{\bullet}.
\]

Both maps send tau to tau and supported elements to supported elements. This is an entrywise scalar-ring construction; no commutativity of matrix multiplication is asserted.

### Recover every energy-grouped residue from a finite jet

Enumerate the distinct positive values of omega_n-Delta as nu_1<...<nu_N. Define the six-by-six residue matrices

\[
(B_j)_{IJ}=\sum_{n:\,\omega_n-\Delta=\nu_j}
\overline{c_{I,n}}c_{J,n},
\qquad
M_r=\frac{\Sigma^{(r)}(\Delta)}{r!}
=\sum_{j=1}^N\frac{B_j}{\nu_j^{r+1}}.
\]

All energy-degenerate contributions remain in their displayed sums. Form the exact scalar polynomials

\[
p_j(t)=\prod_{k\ne j}
\frac{t-\nu_k^{-1}}{\nu_j^{-1}-\nu_k^{-1}}
=\sum_{r=0}^{N-1}\ell_{jr}t^r.
\]

The strict ordering makes every displayed denominator nonzero. Evaluating at nu_k^{-1} gives delta_jk, so every matrix entry satisfies

\[
\boxed{B_j=\nu_j\sum_{r=0}^{N-1}\ell_{jr}M_r.}
\]

Indeed substitution of the moment expression turns its right side into sum_k (nu_j/nu_k) B_k p_j(nu_k^{-1}), whose only surviving term is B_j. This proves an explicit inverse for the finite moment map on the actual energy-grouped residue matrices. The formula has been proved here; the full occupation-coupling table has not been numerically evaluated by the accompanying executable.

Positivity supplies further exact consistency identities. For x in C^6,

\[
x^*B_jx=\sum_{n:\,\omega_n-\Delta=\nu_j}
\left|\sum_Ic_{I,n}x_I\right|^2\ge0,
\qquad
\frac{M_0}{\nu_N}\preceq M_1\preceq\frac{M_0}{\nu_1}.
\]

For s>=0 and a finite list of vectors x_0,...,x_m, the entire block-moment identity is

\[
\sum_{r,k=0}^m x_r^* M_{r+k+s}x_k
=\sum_n\frac1{(\omega_n-\Delta)^{s+1}}
\left|\sum_{r=0}^m\sum_I
\frac{c_{I,n}(x_r)_I}{(\omega_n-\Delta)^r}\right|^2\ge0.
\]

It follows by expanding the displayed squared absolute values. Thus the retained jets contain exact relations tying together the energy correction, raw Gram correction, and higher memory coefficients.

## Established scope

This work computes the support-indexed cohomology of the actual cubic boundary equation, proves full finite-lattice restored-metric and compressed-resolvent identities, gives the exact Split Zero first-jet morphism for the six-band memory, and proves finite residue reconstruction and positivity identities. The independently executed certificate reproduces the complete 112-block calculation and strengthens the published finite-box primitive lower constant. The scope of the executable and the scope of the written proofs are recorded separately above. No GitHub repository was modified.


---

# Chapter 2 — 20260914-coupled-response / RESEARCH_NOTE.md

Original text path: `workbench/yang-mills/continuations/20260914-coupled-response/RESEARCH_NOTE.md`.

# Coupled Hamiltonians, retained response classes, and two-sided energy enclosures

14 September 2026. Written continuation of the original SU(2) finite-regulator Yang–Mills calculation. Parent: `f583ed5ddb13b3ca517c1bab2958f6a4be612d78`, PR5, unmerged at intake. Original physical units and all state/energy Grams remain. The statements below concern each actual finite regulator and its specified form restrictions. No continuum mass lower bound or arithmetic spectral realization is asserted. Exact finite fixtures accompany, rather than certify, the analytic proofs. General Schur elimination and residual variational identities are established operator techniques; no general-priority claim is made.

## 1. The original form and its actual coupled realization

Retain the parent notation: `A_n=H_n-E_0,n`, `kappa_n=2g_n^2/a_n`, `rho_n=psi_n^2`, and the unitary `U_n f=psi_n f`. Its transported closed form is

    q_n(f,v)=kappa_n int rho_n sum_(e,alpha) conjugate(X_e,alpha f) X_e,alpha v.       (C1)

For a fixed refinement r<n use the same fine vacuum, its marginal m, conditional expectation E, pullback J=E*, b=2^(n-r), and kernel K=ker E from parent L6–L15. D is the nonnegative self-adjoint operator of q_n restricted to H^1_phys intersect K, constructed by the closed-form proof in parent L17. The score operator T and its actual adjoint obey

    (Th)_a=E(h S_a),   T*u=sum_a S_a J u_a,
    q_n(Jf,h)=-kappa_n b <Xf,Th>_m.                                             (C2)

Choose a finite independent list of centered smooth coarse physical functions f_1,...,f_m0. Define R x=sum_i x_i f_i. The original coarse state and kinetic Grams and kernel forcing columns are

    G=R*R,   K0_ij=kappa_n b <Xf_i,Xf_j>_m,
    W:C^m0 -> K,    W x=kappa_n b T* X(Rx).                                    (C3)

All entries are the original interacting-vacuum integrals. G is positive definite by independence. W is bounded because its domain is finite dimensional and its smooth columns are in K. On smooth kernel functions D h=(I-JE) U_n* A_n U_n h: testing C1 against the dense smooth kernel functions proves this formula. Conditional expectation preserves smoothness at fixed regulator by its compact smooth positive-density formula. Thus W and every D^j W have smooth columns in Dom(D).

Give C^m0 plus K the ORIGINAL pairing

    <(x,h),(y,k)>_G=x*G y+<h,k>_rho.

The map V(x,h)=JRx+h is an isometry onto H_F=J ran(R) plus K. Indeed the cross terms vanish by E h=E k=0 and EJ=I. Its inverse on H_F is f -> (G^-1 R* E f, f-JE f). The restriction of C1 to H_F has the block energy

    q_F((x,h),(y,k))=x*K0 y-x*W*k-<h,Wy>+q_D(h,k).                             (C4)

The operator representing it is exactly

    H_F(x,h)=(G^-1(K0 x-W*h), D h-Wx),
    Dom(H_F)=C^m0 plus Dom(D).                                                (C5)

For a domain proof, diag(G^-1 K0,D) is self-adjoint in the displayed pairing. The off-diagonal map (-G^-1 W*h,-Wx) is bounded and self-adjoint there, since its two mixed pairings are conjugates. For a real t greater than that bounded map's norm, factor H_F +/- it through diag(G^-1 K0,D) +/- it. Its resolvent has norm at most 1/t, so the remaining factor is invertible by the norm-convergent geometric series. Both ranges are the whole Hilbert space. This proves self-adjointness on exactly C5. Nonnegativity follows from C4=q_n(V.,V.) and C1.

The map to the unrestricted operator is a FORM restriction, explicitly q_F=q_n(V.,V.). It retains an additional coarse complement. For a smooth g perpendicular to ran(R) in L^2(m), a general vector in H_F plus Jg has norm

    ||JRx+h+Jg||^2=x*Gx+||h||^2+||g||_m^2,

and its energy has, in addition to q_F((x,h)) and q_n(Jg), the exact mixed term

    2 Re { kappa_n b <X(Rx),Xg>_m - kappa_n b <Th,Xg>_m }.                      (C6)

No invariance of H_F under the full operator is used. Growing coarse lists retain this complement and its displayed coupling.

## 2. Complex response and its complete Gram kernel

For z outside [0,infinity), use the existing resolvent of D and set

    M(z)=W*(D-z)^-1 W,
    F(z)=K0-zG-M(z),
    L_z x=(x,(D-z)^-1Wx).                                                     (C7)

The second block of (H_F-z)L_z is zero. The first is G^-1 F(z). The full self-adjoint resolvent of H_F exists, so F(z) is invertible: a kernel vector would give a kernel vector L_z x of H_F-z, and surjectivity follows by solving (H_F-z)(x,h)=(G^-1 y,0). With i x=(x,0) and its ACTUAL adjoint i*(x,h)=Gx,

    i*(H_F-z)^-1 i=G F(z)^-1 G.                                               (C8)

Here i* is the adjoint from the raw-G Hilbert space into the ordinary coefficient dual identified by its specified coordinates.

The resolvent identity (D-z)^-1-(D-bar(w))^-1=(z-bar(w))(D-bar(w))^-1(D-z)^-1 gives, for z,w in the upper half-plane,

    -(F(z)-F(w)*)/(z-bar(w))
       =G+W*(D-bar(w))^-1(D-z)^-1W
       =L_w* L_z.                                                            (C9)

Adjoints of the lift use the raw-G pairing. The block array with (i,j)-entry L_zi* L_zj is positive: contracting it by x_1,...,x_N gives ||sum_j L_zj x_j||_G^2. In particular

    -Im F(z)/(Im z)=L_z*L_z,
    Im F=(F-F*)/(2i).                                                        (C10)

At the negative real coordinate z=-s, s>0, write M_s=M(-s), F_s=F(-s). Then

    dF_s/ds=G+W*(D+s)^-2W=L_-s*L_-s.                                         (C11)

Thus the complex response, the restored real state metric and the coupled self-adjoint operator are connected by the stated maps. C9 also retains off-diagonal parameter pairings, not only the diagonal imaginary part. It generalizes the parent's real derivative identity on its exact finite coarse form restriction.

Positivity of C4, evaluated at (x,(D+s)^-1Wx), gives

    0 <= K0-M_s-sW*(D+s)^-2W.

Spectral monotone convergence therefore proves

    M_0 := int_(0,infinity) lambda^-1 W*dE_D(lambda)W <= K0,
    E_D({0})W=0.                                                             (C12)

## 3. Split Zero source windows and an exact response-error certificate

Let V_j be nested finite-dimensional spaces of smooth vectors in K. At support j use the actual cochain window

    V_j --(D+s)--> K --0--> 0.                                                (C13)

The transition j->j+1 is inclusion in degree zero and identity in degree one. The square commutes by restriction of the SAME D+s. The induced first cohomology is K/(D+s)V_j. Invertibility of D+s gives the exact transported-kernel isomorphism

    V_(j+1)/V_j -> ker[ K/(D+s)V_j -> K/(D+s)V_(j+1) ],
    [h] -> [(D+s)h].                                                        (C14)

For surjectivity write a killed representative as (D+s)h with h in V_(j+1). Its inverse is [(D+s)h] -> [h]; changing representative by (D+s)V_j changes h by exactly V_j. This proves both inverse laws. Applying the original Split Zero reconstruction to these windows preserves their support labels and sends each relation to the zero at its own support.

For ANY actual trial-column map Y:C^m0 -> Dom(D), put

    R_Y=W-(D+s)Y,
    B_Y=W*Y+Y*W-Y*(D+s)Y.                                                    (C15)

Expand R_Y*(D+s)^-1R_Y, with every term retained. Since (D+s)(D+s)^-1=I on K and the inverse sends K to Dom(D), the result is exactly

    M_s=B_Y+R_Y*(D+s)^-1R_Y.                                                 (C16)

In particular, for every s>0,

    B_Y <= M_s <= B_Y+s^-1 R_Y*R_Y,
    K0+sG-B_Y-s^-1 R_Y*R_Y <= F_s <= K0+sG-B_Y.                              (C17)

These are whole-matrix inequalities in the original coordinates. The independently proved F_s>=sG remains available at the same time; no matrix minimum of noncommuting bounds is introduced.

Give the forcing space K the positive pairing <r,t>_dual,s=<r,(D+s)^-1t>. Each finite boundary (D+s)V_j has an orthogonal projection for this pairing. The Galerkin columns Y_j with range in V_j are the unique solutions of

    <v,(D+s)Y_j x>=<v,Wx> for every v in V_j.

Then R_j is orthogonal in the dual pairing to (D+s)V_j and represents the original class [Wx] at support j. C16 identifies its ENTIRE quotient Gram as M_s-B_j. On the source, <(D+s)h,(D+s)v>_dual,s=q_D(h,v)+s<h,v>. Hence C14 is an isometry of these quotient pairings; the primitive, support transition and energy cost all remain explicit. Minimization over V_j subset V_(j+1) proves B_j<=B_(j+1)<=M_s. The coefficient source at support j is the chosen actual V_j, without an assumed completeness claim about a finite family.

The restoration error also has an exact norm:

    ((D+s)^-1W-Y)*((D+s)^-1W-Y)=R_Y*(D+s)^-2R_Y <= s^-2 R_Y*R_Y.              (C18)

For 0<eta<1, expansion of ||Yx+((D+s)^-1W-Y)x||^2 and 2|<u,v>|<=eta||u||^2+eta^-1||v||^2 gives

    (1-eta)Y*Y-(eta^-1-1)s^-2 R_Y*R_Y
       <= W*(D+s)^-2W
       <= (1+eta)Y*Y+(1+eta^-1)s^-2 R_Y*R_Y.                                 (C19)

Adding G encloses the restored state metric C11. The exact cross terms in C18's expansion are retained in its proof; the two inequalities are bounds on them.

## 4. Finite moment inputs, including every singular coefficient fiber

Smoothness from section 1 makes the following literal kernel moments well-defined at each finite regulator:

    N_j=W*D^jW,  j>=0,
    Z_d(x_0,...,x_d)=sum_(j=0)^d D^jW x_j.

Use V_d=ran Z_d and keep all original columns, including linear dependencies. Its state, energy-plus-shift and forcing matrices are

    J_d=[N_(i+j)]_(i,j=0)^d,
    H_d(s)=[N_(i+j+1)+sN_(i+j)]_(i,j=0)^d,
    B_d=[N_i]_(i=0)^d.                                                       (C20)

They equal Z_d*Z_d, Z_d*(D+s)Z_d and Z_d*W, respectively. Positivity gives ker H_d=ker Z_d: a zero quadratic form is q_D(Z_dx)+s||Z_dx||^2, forcing Z_dx=0. Every column of B_d is orthogonal to this kernel because x*B_d=(Z_dx)*W. For the finite Hermitian matrix H_d, range H_d=(ker H_d)^perp, so its actual normal-equation fiber is nonempty:

    H_d(s) X=B_d,  Y_d=Z_d X.                                               (C21)

Any two solutions differ by columns in ker H_d=ker Z_d, making Y_d and every formula below independent of the coefficient solution. No inverse of a singular H_d is requested. Galerkin orthogonality now yields

    B_(Y_d)=B_d*X=X*H_dX,
    R_d*R_d=N_0-C_d(s)*X-X*C_d(s)+X*J_d^(2)(s)X,
    C_d(s)=[N_(i+1)+sN_i]_(i=0)^d,
    J_d^(2)(s)=[N_(i+j+2)+2sN_(i+j+1)+s^2N_(i+j)].                           (C22)

Thus moments through order 2d+2 give both sides of C17, retaining all ranks, source fibers and physical units. C19 uses Y_d*Y_d=X*J_dX. This is a direct finite input for the response and its mass metric, not a numerical evaluation of the Yang–Mills moments in this contribution.

## 5. Exact shift recurrence and inherited resolvent mechanism

Fix a physical sigma>0 and s in (0,sigma]. Put

    T_sigma=(D+sigma)^-1,  H_(s,sigma)=(sigma-s)T_sigma,
    X_s=(D+s)^-1.

Their actual bounded-operator identity is (I-H_(s,sigma))X_s=T_sigma. This is the typed instance of source [SZ-R, SR6], whose finite ring identity retains both the constant term and exponent N+1. No arithmetic metric or scalar source mass is transferred to K.

For N>=0 let

    P_N=sum_(j=0)^N (sigma-s)^j W*(D+sigma)^(-j-1)W.

Multiplying the finite sum gives

    M_s-P_N=(sigma-s)^(N+1) W*(D+sigma)^(-N-1)(D+s)^-1W >=0.                 (C23)

Writing theta=1-s/sigma and using the spectral multiplier with C12 proves BOTH bounds

    0<=M_s-P_N<=theta^(N+1) K0,
    0<=M_s-P_N<=theta^(N+1)s^-1 N_0.                                        (C24)

All coefficients and the physical sigma remain. These estimates apply to the unbounded original D because the displayed resolvents are bounded functions of its proved self-adjoint spectral resolution. For fixed s0>0 and s in [s0,sigma], theta<=1-s0/sigma<1, explicitly controlling the iteration count for this actual source. The endpoint s=0 is retained through C12 and the parent's inverse-energy endpoint analysis; C24 makes no uniform-in-s positive lower-edge assertion.

## 6. Evaluated original parameter bounds and the active next calculation

For F containing the coarse edges on which the chosen f_i depend, put

    B_F=ess sup_W sum_i sum_a |X_a f_i(W)|^2.

It is finite for the chosen smooth list. Conditional Cauchy–Schwarz and parent L8 give

    N_0 <= (kappa_n b)^2 B_F I_F I_m0
        <= (32 |F| b^2/a_n^2) B_F I_m0,
    K0 <= kappa_n b B_F I_m0.                                               (C25)

The exact coefficient identity is kappa_n^2 xi_n=1/a_n^2. In C25 the scalar I_F is the parent's INTEGRATED score trace; it is used only after the explicit supremum B_F, never substituted for a pointwise score bound. Consequently C24 supplies explicit response-error bounds

    M_s-P_N <= theta^(N+1) kappa_n b B_F I_m0,
    M_s-P_N <= theta^(N+1) (32 |F| b^2/(s a_n^2)) B_F I_m0.                  (C26)

These have no exterior-volume factor. The ultraviolet, coupling, source-family and s dependence stays in the displayed expressions.

The next selected task is evaluation/enclosure of the actual N_0,N_1,N_2 in C20–22 for the original loop/energy observables, including conditional vacuum derivatives, followed by comparison of the C17 energy interval with the C19 restored metric on growing lists. The first degree already uses a specified finite triple of matrices. No vacuum integrals in those three matrices have been numerically evaluated here. The independent coarse complement C6, the parent's escaping-state quotient, and the full four-dimensional identification remain recorded quantities. A strict positive continuum physical edge has not been established.

## 7. Cross-workbench source and result record

[YM] Parent PR5, commit f583ed5ddb13b3ca517c1bab2958f6a4be612d78, `yang-mills/research-control/RESEARCH_NOTE.md`, blob d138482ac7b40017560cef5a93b21ada4440ce13. Complete delivered body read; original conditional score coupling, closed kernel form and energy section used.

[SZ-R] Zeta PR31 commit b4060b25c21f1a49a5e7730e9aff76d4c93c820d, `workbenches/tau-signed-resolvent-formal/RESEARCH_NOTE.md`, blob 7166debc7724f6805aac125a012e3a59d594dc84, sections 1–6 read. SR6 is instantiated by the EXACT map H->(sigma-s)(D+sigma)^-1, T->(D+sigma)^-1, X->(D+s)^-1. Its finite algebraic identity is rederived in C23. Its historical Lean execution was not rerun here.

[SZ-M] Zeta PR32 commit 9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6, observation-metric note blob 866ed2f6e8ed9ca544f6ec0af97c5dec3fecedad, already proof-read in the parent. Its original-metric section identity is instantiated by source metric <r,(D+s)^-1t>, relation map (D+s)|V_j and source columns W in C13–18. Both identities are proved above in their actual spaces.

[F] G. Dusson, I. M. Sigal, B. Stamm, *The Feshbach-Schur map and perturbation theory*, arXiv:2105.02058 (2021). Abstract consulted for method attribution, not as a premise supplying Yang–Mills estimates. The general coupling/elimination mechanism is an established method. All domain and coefficient calculations used here are written above.

Current peer intake: Zeta main advanced to 91ed3b7c358a1f444d0d48c292e4a400ca509eff. Its current README lines 1–80 and the four-commit comparison were read for orientation. Its new conductor/arithmetic asymptotics are not imported as proved estimates here. A search of tracked open peer PRs updated since the parent's intake found Erdős–Straus PR7, with higher-support and uniform Green-norm calculations; only its description was read, and it is a candidate for actual proof inspection. Collatz, Erdős 817 and Erdős–Straus main refs were refreshed and retain their previous revisions.

The user's Hamiltonian/self-adjointness suggestion is retained as a cross-workbench research direction. C5–11 provide the actual transferable operator construction and metric identity; no unspecified arithmetic spectrum is assigned to it. No personal-memory feature, autonomous watcher, paid model job or automatic merge is activated.


---

# Chapter 3 — 20260914-spectral-reconstruction / RESEARCH_NOTE.md

Original text path: `workbench/yang-mills/continuations/20260914-spectral-reconstruction/RESEARCH_NOTE.md`.

# Continuum spectral reconstruction from retained smooth correlation kernels

Date: 14 September 2026

This continuation starts from the full finite-regulator Hamiltonians and Wilson/Schur maps already retained in `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_WILSON_SCHUR_MEMORY.md`, together with the smooth-frame lesson supplied by the explicit S6 normal-line trivialization in `s6/27_s6_key_advances_frozen_2026-09-06.tex`. Every Gram matrix and every spectral measure below is kept in its original coordinates.

## 1. Countable gauge-invariant observable system

For each finite open lattice `n`, let `A_n=H_n-E_{0,n}I` on the physical Hilbert space and let `psi_n` be the positive unit vacuum. Let `mathscr O` be the countable union, over all lattice levels, of gauge-invariant spin-network functions obtained from finite SU(2) representation labels and fixed finite intertwiner bases. Pull a member born at level `N(i)` to every finer level by the exact ordered edge-product refinement map. Denote the resulting bounded multiplication observable by `O_{i,n}`.

For `n>=N(i)` set

\[
 r_{i,n}=(O_{i,n}-\langle\psi_n,O_{i,n}\psi_n\rangle)\psi_n
\]

and

\[
 C^{(n)}_{ij}(t)=\langle r_{i,n},e^{-tA_n}r_{j,n}\rangle,\qquad t>0.
\]

For every fixed pair `(i,j)` and every integer `q>=0`, spectral calculus gives

\[
 \left|\frac{d^q}{dt^q}C^{(n)}_{ij}(t)\right|
 \le 4\|O_i\|_\infty\|O_j\|_\infty
 \left(\frac{q}{et}\right)^q,
\]

with the `q=0` factor interpreted as one. Indeed

\[
 \frac{d^q}{dt^q}C^{(n)}_{ij}(t)
 =(-1)^q\langle r_{i,n},A_n^qe^{-tA_n}r_{j,n}\rangle,
\]

`||r_{i,n}||<=2||O_i||_infty`, and

\[
 \|A_n^qe^{-tA_n}\|=\sup_{\lambda\in\sigma(A_n)}\lambda^qe^{-t\lambda}
 \le\sup_{\lambda\ge0}\lambda^qe^{-t\lambda}
 =\left(\frac{q}{et}\right)^q.
\]

Diagonal extraction over the countable triples `(i,j,q)` and rational compact positive-time intervals therefore supplies one regulator subsequence `n_k` and smooth limits

\[
 C_{ij}(t)=\lim_{k\to\infty}C^{(n_k)}_{ij}(t)
\]

in `C^infty_loc((0,infty))` for every `i,j`.

For every finite set of labels, every positive times `s_a`, and every complex coefficients `z_a`,

\[
 \sum_{a,b}\overline{z_a}z_b C_{i_ai_b}(s_a+s_b)\ge0
\]

because this is the limit of the corresponding finite-regulator squared norms.

## 2. Reconstructed continuum observable Hilbert space and generator

Let `D` be the complex vector space generated by symbols `[i,s]`, `i in mathbb N`, `s>0`, and define

\[
 \langle[i,s],[j,t]\rangle=C_{ij}(s+t).
\]

Quotient by the exact null space of this sesquilinear form and complete. Call the resulting Hilbert space `H_obs`. Define

\[
 T(u)[i,s]=[i,s+u],\qquad u\ge0.
\]

The kernel identity gives `T(u+v)=T(u)T(v)`. Positivity and the spectral-calculus derivative bounds inherited above give strong continuity on the dense symbol span. The operators `T(u)` are positive self-adjoint contractions. Hence there is a nonnegative self-adjoint generator `A_obs` with

\[
 T(u)=e^{-uA_{obs}}.
\]

The limits

\[
 \xi_i=\lim_{s\downarrow0}[i,s]
\]

exist exactly when the finite-energy zero-time matrix

\[
 G^f_{ij}=\lim_{t\downarrow0}C_{ij}(t)
\]

is finite; the bounded-observable estimates above give finiteness. Their spectral matrix measure is

\[
 \mu_{ij}(B)=\langle\xi_i,E_{A_{obs}}(B)\xi_j\rangle,
\]

and

\[
 \boxed{C_{ij}(t)=\int_{[0,\infty)}e^{-t\lambda}\,d\mu_{ij}(\lambda).}
\]

The closure of the union of the diagonal supports is exactly the spectrum:

\[
 \boxed{\sigma(A_{obs})=
 \overline{\bigcup_i\operatorname{supp}\mu_{ii}}.}
\]

Proof. A Borel open set `U` with `mu_ii(U)=0` for every `i` has

\[
 \|E(U)\xi_i\|^2=\mu_{ii}(U)=0.
\]

Therefore `E(U)e^{-sA_obs}\xi_i=0` for every `i,s`; these vectors span a dense subspace by construction, so `E(U)=0`. Conversely a point in `supp mu_ii` has nonzero spectral projection in every open neighbourhood. The spectral characterization of a self-adjoint operator then gives the displayed equality.

This identifies the exact spectral object reconstructed by the continuum correlation system.

## 3. Constructive recovery from positive time only

Fix `h>0` and put

\[
 x=e^{-h\lambda}\in(0,1].
\]

Push `mu_ij` forward by this map and denote the resulting matrix measure on `(0,1]` by `nu_ij`. Set

\[
 M_0=\lim_{t\downarrow0}C(t),\qquad M_m=C(mh)\quad(m\ge1).
\]

Then, entry by entry,

\[
 M_m=\int_{(0,1]}x^m\,d\nu(x),\qquad m\ge0.
\]

For every continuous scalar function `f` on `[0,1]`, define its Bernstein polynomial

\[
 B_Nf(x)=\sum_{k=0}^N f(k/N){N\choose k}x^k(1-x)^{N-k}.
\]

Expansion in monomials gives the coordinate-level recovery formula

\[
 \boxed{
 \int B_Nf\,d\nu
 =\sum_{k=0}^N\sum_{j=0}^{N-k}
 f(k/N){N\choose k}{N-k\choose j}(-1)^jM_{k+j}.
 }
\]

Bernstein uniform convergence on `[0,1]` and finiteness of the matrix measure give

\[
 \boxed{
 \int f\,d\nu
 =\lim_{N\to\infty}
 \sum_{k=0}^N\sum_{j=0}^{N-k}
 f(k/N){N\choose k}{N-k\choose j}(-1)^jM_{k+j}.
 }
\]

Thus the complete finite-energy matrix spectral measure is determined constructively by the retained positive-time values `C(mh)` together with `C(0+)`. No frequency discretization is introduced.

For a continuous function `phi` on the one-point compactification `[0,infty]` whose value at infinity is fixed to zero, take

\[
 f(x)=\begin{cases}
 \phi(-h^{-1}\log x),&x>0,\\
 0,&x=0.
 \end{cases}
\]

The preceding formula then reconstructs `int phi(lambda) dmu(lambda)` directly from the positive-time continuum kernel.

## 4. Resolvent and exact interval masses

Define the positive-half-line Stieltjes matrix

\[
 S(s)=\int_0^\infty e^{-st}C(t)\,dt
 =\int_{[0,\infty)}\frac{d\mu(\lambda)}{\lambda+s},\qquad s>0.
\]

Every entry is finite and analytic on `Re s>0`. Let

\[
 R(z)=\int_{[0,\infty)}\frac{d\mu(\lambda)}{\lambda-z},
 \qquad z\in\mathbb C\setminus[0,\infty).
\]

On the negative real axis `R(-s)=S(s)`, so the analytic function `R` is uniquely fixed by the retained positive-time data.

Use the matrix imaginary part `Im R(z)=(R(z)-R(z)^*)/(2i)`, which retains the complex off-diagonal entries of the spectral measure. For `0<a<b<infty`, entrywise integration of the Poisson kernel gives

\[
 \boxed{
 \lim_{\eta\downarrow0}\frac1\pi
 \int_a^b\operatorname{Im}R(x+i\eta)\,dx
 =\mu((a,b))+\frac12\mu(\{a\})+\frac12\mu(\{b\}).
 }
\]

The atom at `lambda_0>=0` is recovered by

\[
 \boxed{
 \mu(\{\lambda_0\})
 =\lim_{\eta\downarrow0}
 \eta\,\operatorname{Im}R(\lambda_0+i\eta).
 }
\]

Both identities hold as matrix identities because they hold after contraction by every finite coefficient vector and polarization recovers each entry.

## 5. Exact gap readout on the reconstructed observable sector

For every nonzero diagonal measure define

\[
 m_i=\inf\operatorname{supp}\mu_{ii}.
\]

The Laplace principle here requires no density. The upper estimate

\[
 C_{ii}(t)\le \mu_{ii}([0,\infty))e^{-m_it}
\]

and, for every `epsilon>0`, the support property

\[
 C_{ii}(t)\ge
 \mu_{ii}([m_i,m_i+\epsilon))e^{-(m_i+\epsilon)t}
\]

prove

\[
 \boxed{
 m_i=\lim_{t\to\infty}-\frac1t\log C_{ii}(t).
 }
\]

Combining this with the spectral-support equality yields the exact observable-sector spectral bottom

\[
 \boxed{
 \inf\sigma(A_{obs})
 =\inf_i\lim_{t\to\infty}-\frac1t\log C_{ii}(t).
 }
\]

All centered Wilson/spin-network labels remain present. The spectral-support and large-time formulas determine the reconstructed fixed-label observable sector. The regulator-state comparison has the retained kernel `K/N` constructed in [the vacuum-refinement continuation, Section 6](../20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md#6-the-regulator-state-comparison-and-the-escaping-label-kernel); its equation (6.6) computes an escaping-label class together with its norm and energy sequence.

## 6. Retaining the energy-infinity endpoint

The positive-time map annihilates a compactified atom at `lambda=infty`. Let the weak compactified regulator measure have endpoint matrix `E_infty`. Let `G^c` denote its complete zero-time Gram limit before applying the positive-time multiplier. Then

\[
 \boxed{E_\infty=G^c-\lim_{t\downarrow0}C(t).}
\]

This is the same retained Split-Zero endpoint class already isolated in the previous continuation. The finite-energy measure reconstructed in Sections 3--5 and `E_infty` together give the complete compactified matrix measure.

## 7. Smooth frames and the S6 continuation mechanism

The S6 finite filling has the explicit nowhere-zero smooth section

\[
 H_j(x)=\exp(-2\pi i\varepsilon_j\gamma(x))
\]

and the mutually inverse smooth maps

\[
 [x,n]\mapsto([x],n/H_j(x)),\qquad
 ([x],z)\mapsto[x,zH_j(x)].
\]

The operation needed for the Yang--Mills smooth observable family is the corresponding finite-coordinate frame transport. Let `T(theta)` be an invertible smooth matrix relating two retained raw observable frames. Their correlation kernels and spectral measures obey

\[
 C^{T}(t,\theta)=T(\theta)^*C(t,\theta)T(\theta),
\]

\[
 \mu^{T}(B,\theta)=T(\theta)^*\mu(B,\theta)T(\theta).
\]

The inverse map is written explicitly:

\[
 \mu(B,\theta)=T(\theta)^{-*}\mu^T(B,\theta)T(\theta)^{-1}.
\]

Therefore

\[
 \mu^T(B,\theta)=0\quad\Longleftrightarrow\quad\mu(B,\theta)=0.
\]

The spectral support recovered from a complete retained frame is invariant under this smooth invertible transport while the full raw Gram matrices remain stored. This is the precise continuation mechanism used here; no orthonormalization is performed.

## 8. What this advances

The continuum programme now contains a direct spectral extraction layer rather than only variational quotients:

1. a single subsequence carries all correlations of a countable gauge-invariant cylindrical family;
2. those kernels construct a positive self-adjoint continuum observable generator;
3. its complete finite-energy matrix spectral measure is reconstructible from positive-time data by an explicit Bernstein-moment formula;
4. Stieltjes inversion recovers interval masses and atoms;
5. the bottom of its spectrum is exactly the infimum of the large-time exponential edges of the diagonal correlations;
6. the compactified energy-infinity class remains separately retained by the zero-time Gram defect;
7. smooth invertible frame transport preserves spectral support by the displayed typed inverse.

The remaining mass-gap task is concentrated into the continuum-limit dynamics of these exact measures: proving a strictly positive lower edge for the full reconstructed gauge-invariant observable sector and identifying this sector with the four-dimensional Yang--Mills Hilbert space required by the target theorem. This note does not assert either conclusion.


---

# Chapter 4 — 20260914-splitzero-smooth-continuum / RESEARCH_NOTE.md

Original text path: `workbench/yang-mills/continuations/20260914-splitzero-smooth-continuum/RESEARCH_NOTE.md`.

# Split Zero continuum continuation: smooth source germs, exact refinement, and positive-time spectral control

Research continuation, 14 September 2026.

## 0. Provenance and completed scope

This is an additive, locally prepared contribution for `KokunoYumeto/yang-mills-interacting-workbench`. It continues the supplied `split_zero_ym/RESEARCH_NOTE.md`. Publication to GitHub has not occurred in this session. The GitHub integration was offered; its discovery response reported that it was not installed. Public source reading was possible through the browser, but direct network requests from the execution container failed.

The following mathematical source bodies were retrieved on 14 September 2026:

- [YM1] `yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`, especially §§1–2: the full Hamiltonian, gauge action, physical domains, positive unit vacuum and ground-state identity.
- [YM2] `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_WILSON_SCHUR_MEMORY.md`: original link-transport convention, complete magnetic value, retained memory and metric.
- [YM3] `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_TENSOR_TRANSFER.md`: full nonlinear transport and observable/state distinctions, with the actual maps retained.
- [SZ] `KokunoYumeto/zeta-function-research-reader`, revision `7ea0a49945390eae14d3160a5730858899768b5f`, `workbenches/split-support-rees-trace/RESEARCH_NOTE.md`, §§2 and 7.1: supported linear diagrams and the retained-jet ring morphism.

YM paths refer to `main` as retrieved on the stated date; an immutable YM revision was not obtained. Complete URLs and retrieval scope are recorded in `sources.json`.

The S6 entry point `s6/README.md` and the S6 section of `ATTEMPTS.md` were retrieved. The latter locates the smooth normal-line trivialization and its inverse at Theorems 53.4, 53.6, 53.7, 53.9 / FF1–FF46 of the frozen project. Fetches of the linked S6 TeX, project guide, PDF, and archive endpoint failed. No unexamined S6 proof is used as a mathematical premise below. Section 2 gives a fully written smooth-germ construction for the actual YM holonomy map.

The completed results are:

1. Exact gauge-equivariant refinement maps and the complete Hamiltonian intertwining defect, including its composition law.
2. Smooth holonomy continuation, every parameter derivative, the exact flat-germ kernel, and a quantitative non-Abelian magnetic continuum remainder.
3. Regulator-independent positive-time correlation, high-energy tail, and Schur-memory bounds for the original nonlinear Hamiltonians.
4. A simultaneous spatial/coupling/volume subsequence with a smooth positive-time spectral limit, retaining both the mass at infinite energy and the mass at zero energy.
5. A literal Split Zero cohomology window for the infinite-energy boundary and a strongly continuous positive-energy Hilbert reconstruction from the limiting kernels.

All constants below retain the original state norms and physical spacing. The proofs establish these specified objects. They establish no positive numerical mass lower bound for the limiting four-dimensional theory.

## 1. Original operators and an actual simultaneous sequence

Fix physical spacing `a_0>0`, coupling `g_0>0`, and parameter `beta>0`. For every integer `n>=0`, define

\[
a_n=a_0 2^{-n},\qquad L_n=4\,2^{2n},\qquad
 g_n^2=\frac1{g_0^{-2}+\beta n\log 2}.
\tag{1.1}
\]

This is an explicitly prescribed path. No identification of `beta` with a quantum beta-function coefficient is asserted. The physical half-side is

\[
a_nL_n=4a_0 2^n.
\tag{1.2}
\]

Use precisely the source's open cubical graph with vertices `{-L_n,...,L_n}^3`, positively oriented contained edges `E_n`, and contained elementary faces `P_n`. Write `Q_n=SU(2)^{E_n}` with its original product Haar probability measure `dU_n`. The physical Hilbert space \(\mathcal H_n\) is the invariant subspace under

\[
U_e\longmapsto h_{s(e)}U_eh_{t(e)}^{-1}.
\tag{1.3}
\]

Use `T_alpha=-i sigma_alpha/2`, left derivatives `X_{e,alpha}` and

\[
K_n=\sum_{e\in E_n}E_e,\qquad E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,
\]
\[
V_n(U)=\frac1{2g_n^2a_n}\sum_{p\in P_n}(2-\operatorname{tr}U_p),
\qquad H_n=\frac{2g_n^2}{a_n}K_n+V_n.
\tag{1.4}
\]

Every ordered plaquette word and the full scalar term in `V_n` remain. By [YM1], the physical operator has domain the invariant part of `H^2(Q_n)`, compact resolvent, and a unique positive smooth unit vacuum `psi_n`. Denote its exact ground energy by `E_{0,n}` and put

\[
A_n=H_n-E_{0,n}I\geq0.
\tag{1.5}
\]

The energy shift in (1.5) is recorded explicitly and reappears in the refinement defect below.

### 1.1 Ordered product map and its exact Haar and gauge properties

A coarse vertex with integer coordinate `v` is the fine vertex `2v`. A coarse edge of physical length `a_n` consists of two fine edges of length `a_{n+1}=a_n/2`, in their original order. Define

\[
\pi_n:Q_{n+1}\longrightarrow Q_n,\qquad
(\pi_n U)_e=U_{e,1}U_{e,2}.
\tag{1.6}
\]

The fine links outside these coarse chains remain in `Q_{n+1}` as additional variables. Distinct coarse chains have disjoint fine-edge sets. Haar invariance gives, for integrable `f`,

\[
\int f(U_1U_2)\,dU_1dU_2=\int f(W)\,dW.
\tag{1.7}
\]

Indeed, for each fixed `U_1`, the substitution `W=U_1U_2` is left translation of Haar measure. Fubini on the disjoint chains, followed by integration of the additional variables, proves `(pi_n)_*dU_{n+1}=dU_n`. Consequently

\[
J_n:\mathcal H_n\longrightarrow\mathcal H_{n+1},\qquad J_nf=f\circ\pi_n,
\qquad J_n^*J_n=I.
\tag{1.8}
\]

For a fine gauge transformation, the product on one chain is

\[
(h_sU_{e,1}h_m^{-1})(h_mU_{e,2}h_t^{-1})
=h_s(U_{e,1}U_{e,2})h_t^{-1}.
\tag{1.9}
\]

Thus `J_n` maps physical vectors to physical vectors. Iteration gives `J_{n,k}=J_{k-1}...J_n`; associativity of the original ordered products proves `J_{r,k}J_{n,r}=J_{n,k}`.

### 1.2 Complete kinetic and Hamiltonian defect

For a smooth coarse function,

\[
X_{e,1,\alpha}J_nf=J_nX_{e,\alpha}f,
\]
\[
X_{e,2,\alpha}J_nf
=\sum_{\gamma=1}^3(\operatorname{Ad}_{U_{e,1}})_{\gamma\alpha}
 J_nX_{e,\gamma}f.
\tag{1.10}
\]

The adjoint coefficients in the second expression are constant under differentiation of `U_{e,2}`. They satisfy

\[
\sum_\alpha(\operatorname{Ad}_{U_{e,1}})_{\gamma\alpha}
(\operatorname{Ad}_{U_{e,1}})_{\delta\alpha}=\delta_{\gamma\delta},
\]

because conjugation preserves the original form `-tr(T_gamma T_delta)/2=delta_gamma_delta/4`. Squaring (1.10) and summing therefore proves, including the factor from both subedges,

\[
K_{n+1}J_n=2J_nK_n.
\tag{1.11}
\]

The unused fine edges differentiate `J_nf` to zero; they remain in the original fine Hamiltonian. Define the full defect on `Dom(A_n)` by

\[
\mathcal D_n=A_{n+1}J_n-J_nA_n.
\]

Its coordinate expression is

\[
\boxed{
\mathcal D_n=
\frac{8g_{n+1}^2-2g_n^2}{a_n}J_nK_n
+M_{V_{n+1}-V_n\circ\pi_n}J_n
+(E_{0,n}-E_{0,n+1})J_n.
}
\tag{1.12}
\]

Here `M_f` denotes multiplication by the displayed full function on `Q_{n+1}`. Every fine plaquette, including plaquettes involving additional fine links, occurs in `V_{n+1}`.

The map `J_n` sends `H^2(Q_n)` continuously into `H^2(Q_{n+1})`: apply the chain rule twice to the smooth finite product map, use bounded coefficients on the compact groups, and integrate with (1.7). Thus (1.12) is a bounded map from the graph domain of `A_n` to \(\mathcal H_{n+1}\) at each fixed pair of regulators.

For `s>0`, multiplication of the two resolvents gives the exact bounded-operator identity

\[
\boxed{
(A_{n+1}+s)^{-1}J_n-J_n(A_n+s)^{-1}
=-(A_{n+1}+s)^{-1}\mathcal D_n(A_n+s)^{-1}.
}
\tag{1.13}
\]

To verify it, multiply the left side by `A_{n+1}+s`; the result is `-D_n(A_n+s)^{-1}`. All compositions have the domains just established. Composition retains every intermediate defect:

\[
\boxed{
A_kJ_{n,k}-J_{n,k}A_n
=\sum_{r=n}^{k-1}J_{r+1,k}\mathcal D_rJ_{n,r}.
}
\tag{1.14}
\]

Expanding the right side telescopes adjacent terms, with their exact signs.

### 1.3 Vacuum and centered-state transition data

For a bounded physical coarse observable `f`, let `f'=f circ pi_n`, `m_n=<psi_n,f psi_n>`, and `m_{n+1}=<psi_{n+1},f' psi_{n+1}>`. The corresponding original centered vectors obey

\[
\begin{aligned}
&(f'-m_{n+1})\psi_{n+1}-J_n((f-m_n)\psi_n)\\
&=(f'-m_{n+1})(\psi_{n+1}-J_n\psi_n)
 +(m_n-m_{n+1})J_n\psi_n.
\end{aligned}
\tag{1.15}
\]

This is direct expansion. No compatibility of the two vacua has been assumed.

## 2. Smooth continuum holonomy and retained flat germs

Let `Q=[-3a_0,3a_0]^3`. Work with the actual space of smooth `su(2)`-valued one-forms `A(theta,x)=sum_i A_i(theta,x)dx^i`, where `theta` ranges over an open interval containing zero and each `A(theta,.)` has support in `(-2a_0,2a_0)^3`. A fixed compact parameter interval supplies finite suprema of every displayed derivative. Neither Lie-algebra commutators nor spatial coordinates are removed.

For an oriented path `gamma:[0,ell]->Q`, parameterized by arc length, write

\[
a_\theta(r)=\sum_i\mathcal A_i(\theta,\gamma(r))\dot\gamma^i(r),
\quad U_\theta'(r)=U_\theta(r)a_\theta(r),\quad U_\theta(0)=I.
\tag{2.1}
\]

This is the inverse-transport convention of [YM2], expressed in the original lattice gauge variables. Since `a_theta^*=-a_theta`, differentiating `U_theta U_theta^*` proves unitarity. With

\[
\mathcal A_i^h=h\mathcal A_i h^{-1}-(\partial_i h)h^{-1},
\]

differentiating `h(gamma(0)) U_theta(r) h(gamma(r))^{-1}` proves the gauge transform (1.3). The convention in [YM2] written with `h^{-1}` at the initial endpoint is obtained by the explicit substitution `h -> h^{-1}`.

### 2.1 Every parameter derivative, in its original order

Set `U_theta(r,s)=U_theta(r)^{-1}U_theta(s)`. Differentiating (2.1), and then differentiating the product `(partial_theta U)U^{-1}`, gives

\[
\partial_\theta U_\theta(\ell)
=\int_0^\ell U_\theta(0,r)(\partial_\theta a_\theta(r))
 U_\theta(r,\ell)\,dr.
\tag{2.2}
\]

Repeated differentiation yields, for each integer `k>=1`,

\[
\begin{aligned}
\partial_\theta^kU_\theta(\ell)
={}&\sum_{r=1}^k\sum_{j_1+\cdots+j_r=k\atop j_b\ge1}
\frac{k!}{j_1!\cdots j_r!}
\int_{0<t_1<\cdots<t_r<\ell}
U(0,t_1)a^{(j_1)}(t_1)U(t_1,t_2)\\
&\hspace{26mm}\cdots a^{(j_r)}(t_r)U(t_r,\ell)\,dt_1\cdots dt_r.
\end{aligned}
\tag{2.3}
\]

One proof is induction using (2.2): a derivative either increases one `j_b` or inserts a new derivative into one of the intervening transport intervals. The multinomial coefficients count the allocations of the `k` labeled differentiations; the ordered simplex retains their chronological order. This also follows by differentiating the convergent Picard series on a compact parameter interval, whose differentiated series is dominated by an exponential times a finite polynomial in the derivative suprema.

Writing `M_j=sup_r ||partial_theta^j a_theta(r)||_op`, the unitary factors and the simplex volume give

\[
\boxed{
\|\partial_\theta^kU_\theta(\ell)\|_{\rm op}
\le\sum_{r=1}^k\frac{\ell^r}{r!}
\sum_{j_1+\cdots+j_r=k\atop j_b\ge1}
\frac{k!}{j_1!\cdots j_r!}\prod_{b=1}^r M_{j_b}.
}
\tag{2.4}
\]

The total physical length `ell` remains in this bound. Splitting the path into any number of consecutive pieces leaves the ordered product equal to `U_theta(ell)`, by uniqueness for (2.1). Therefore both its value and every derivative in (2.3) are exactly compatible with (1.6) under arbitrarily many refinements. This is a smooth continuum-to-link continuation for the complete non-Abelian word.

### 2.2 Smooth source algebra and its exact kernel

Let `A_sm` be the algebra of complex smooth germs at `theta=0`. For `q>=0`, define

\[
j^q:A_{\rm sm}\to\mathbb C[\eta]/(\eta^{q+1}),\qquad
j^qf=\sum_{k=0}^q\frac{f^{(k)}(0)}{k!}\eta^k.
\tag{2.5}
\]

The product rule proves that these are algebra homomorphisms. Taylor's formula with integral remainder proves

\[
\ker j^q=\theta^{q+1}A_{\rm sm}.
\tag{2.6}
\]

Indeed, with the first `q+1` derivatives zero,

\[
f(\theta)=\frac{\theta^{q+1}}{q!}
\int_0^1(1-u)^qf^{(q+1)}(u\theta)\,du,
\]

and the integral is smooth in `theta`. Conversely, the product rule gives vanishing derivatives through order `q` for every member of the displayed ideal.

Define `J_infty f=(f^{(k)}(0)/k!)_{k>=0}` with its formal-series product and let `F_flat` be the smooth germs with every derivative at zero equal to zero. The exact sequence is

\[
\boxed{
0\longrightarrow F_{\rm flat}\xrightarrow{\rm inclusion}A_{\rm sm}
\xrightarrow{J_\infty}\operatorname{im}J_\infty\longrightarrow0.
}
\tag{2.7}
\]

The kernel statement follows coefficient by coefficient, and the last map is onto its displayed image by definition. No reconstruction from a formal series has been inserted.

Apply the Split Zero scalar functor from [SZ] to every map (2.5) and every truncation between target rings. A supported germ is mapped to a supported jet; `tau` maps to `tau`. Multiplicativity was proved above, so these are the same typed scalar morphisms as the source's holomorphic first-jet construction, now with the full smooth-germ kernel (2.7) retained.

An explicit YM member of that kernel is available. Fix a rectangle of sides `ell_1,ell_2>0` inside the region where a smooth cutoff `chi` is one, and fix `b!=0`. Set

\[
\eta_0(\theta)=\begin{cases}e^{-1/\theta^2},&\theta\ne0,\\0,&\theta=0,\end{cases}
\quad
\mathcal A_2=b\,x^1\chi(x)\eta_0(\theta)T_3,
\quad \mathcal A_1=\mathcal A_3=0.
\tag{2.8}
\]

Every derivative of `eta_0` is a polynomial in `theta^{-1}` times `e^{-1/theta^2}` away from zero. For each fixed power `p`, `|theta|^{-p}e^{-1/theta^2}->0`, proved by the exponential power-series bound. Induction then gives its smooth extension and vanishing derivatives of every order.

For the original rectangular loop wholly in `chi=1`, direct integration in (2.1) gives

\[
2-\operatorname{tr}U_C(\theta)
=2-2\cos\bigl(b\ell_1\ell_2\eta_0(\theta)/2\bigr).
\tag{2.9}
\]

Its image under every `j^q` is zero. Its exact value is strictly positive for all sufficiently small nonzero `theta`, as its nonzero argument has absolute value less than `2pi`. Thus the actual source germ and its membership in the explicitly computed kernel (2.7) both remain available.

## 3. Quantitative non-Abelian magnetic continuum remainder

All estimates in this section apply to the complete connection space just specified, uniformly on a fixed compact parameter interval. Define, over `Q` and that interval,

\[
M_A=\max_i\sup\|\mathcal A_i\|_{\rm op},\quad
M_F=\max_{i<j}\sup\|F_{ij}\|_F,\quad
M_{\partial F}=\max_{k,i<j}\sup\|\partial_kF_{ij}\|_F,
\]
\[
F_{ij}=\partial_i\mathcal A_j-\partial_j\mathcal A_i
+[\mathcal A_i,\mathcal A_j].
\tag{3.1}
\]

The norm `||.||_F` is the original matrix Frobenius norm, with no division by its dimension. Put

\[
C=M_{\partial F}+2M_AM_F+\frac{a_0}{2}M_F^2.
\tag{3.2}
\]

### 3.1 Exact face integral and its remainder

On one oriented square `[0,a]^2` in directions `i,j`, construct `h(u,v)` by transport first along `(0,0)->(0,v)` and then along `(0,v)->(u,v)` using (2.1). Then `partial_u h=h A_i`, and on `u=0`, `partial_v h=h A_j`. The transformed connection consequently satisfies `A_i^h=0` on the square and `A_j^h(0,v)=0`. Direct substitution in (3.1) proves `F_{ij}^h=hF_{ij}h^{-1}` and

\[
A_j^h(a,v)=C_p(v):=\int_0^a h(u,v)F_{ij}(u,v)h(u,v)^{-1}\,du.
\tag{3.3}
\]

Three boundary transports are identities in this gauge; the original plaquette is the remaining right-edge transport `V`, satisfying `V'=VC_p`, `V(0)=I`. The base gauge value is `h(0,0)=I`, so the plaquette matrix itself is unchanged. Thus

\[
U_p-I=\int_0^a V(v)C_p(v)\,dv,
\qquad \|U_p-I\|_F\le a^2M_F.
\tag{3.4}
\]

Retain the exact remainder

\[
\begin{aligned}
R_p={}&\int_0^a\!\int_0^a
\bigl(hF_{ij}h^{-1}-F_{ij}(0,0)\bigr)\,du\,dv\\
&+\int_0^a(V(v)-I)C_p(v)\,dv,
\qquad U_p-I=a^2F_{ij}(0,0)+R_p.
\end{aligned}
\tag{3.5}
\]

Unitarity and path length give `||h-I||_op <= (u+v)M_A`. It follows that

\[
\|hF_{ij}(u,v)h^{-1}-F_{ij}(0,0)\|_F
\le (u+v)(M_{\partial F}+2M_AM_F).
\]

Also `||V(v)-I||_op <= va M_F` and `||C_p(v)||_F <= aM_F`. Integrating proves

\[
\|R_p\|_F\le a^3(M_{\partial F}+2M_AM_F)+\frac{a^4}{2}M_F^2
\le a^3C\qquad(0<a\le a_0).
\tag{3.6}
\]

### 3.2 The original magnetic sum, with every factor

For `U in SU(2)`, direct expansion gives

\[
\|U-I\|_F^2=4-2\operatorname{tr}U,
\quad
\frac{2-\operatorname{tr}U}{2g^2a}
=\frac{\|U-I\|_F^2}{4g^2a}.
\tag{3.7}
\]

Equations (3.5)–(3.7) give the exact single-face difference

\[
\frac{2-\operatorname{tr}U_p}{2g^2a}
-\frac{a^3}{4g^2}\|F_{ij}(x_p)\|_F^2
=\frac{2a^2\operatorname{Re}\operatorname{tr}(F_{ij}(x_p)^*R_p)
+\|R_p\|_F^2}{4g^2a}.
\tag{3.8}
\]

At level `n`, the support assumption places every nonidentity plaquette inside `Q`; all plaquettes outside the corresponding anchored cube sum have identity edge transports. The original graph boundary is farther away. The cube has exactly `(6a_0/a_n)^3` cells. There are three oriented faces in the anchored sum per cell. These account for every nonzero term of the original magnetic sum; all other terms are exactly zero.

For `f_ij=||F_ij||_F^2`, each coordinate derivative is bounded by `2M_F M_partialF`. Integrating the line-segment derivative estimate within each cube gives the bound `6a_n M_F M_partialF` for its pointwise Riemann discrepancy. Summation of (3.8) over the three orientations, followed by this Riemann estimate, proves

\[
\boxed{
V_n(U[\mathcal A])=
\frac1{4g_n^2}\int_Q\sum_{i<j}\|F_{ij}(x)\|_F^2\,dx+\varepsilon_n,
}
\tag{3.9}
\]
\[
\boxed{
|\varepsilon_n|\le
\frac{3|Q|}{4g_n^2}
\left(2a_nM_FC+a_n^2C^2+6a_nM_FM_{\partial F}\right).
}
\tag{3.10}
\]

The term with `a_n^2` and the complete commutator in (3.1) remain. Along (1.1), the right side tends to zero because `n 2^{-n}->0`. For instance `n<=2^{n/2}` for integers `n>=4`, proved by induction from `n+1<=sqrt(2)n` for `n>=3`. Thus the decay is controlled explicitly. The full leading term is

\[
\frac{g_0^{-2}+\beta n\log2}{4}
\int_Q\sum_{i<j}\|F_{ij}\|_F^2\,dx.
\tag{3.11}
\]

It remains in (3.9), including its growth with `n`. This section evaluates the full magnetic multiplication function on the displayed smooth connection family; the quantum vacuum and kinetic operator remain those of (1.4).

## 4. Uniform positive-time control in the actual interacting vacua

### 4.1 Six original-coordinate loop vectors

Choose the six positively oriented square loops of side `a_0` in the plane `x^3=0`, with lower-left corners

\[
a_0(-3,-3,0),\ a_0(-1,-3,0),\ a_0(1,-3,0),\
a_0(-3,1,0),\ a_0(-1,1,0),\ a_0(1,1,0).
\tag{4.1}
\]

They are edge-disjoint and belong to every graph in (1.1). At level `n`, each has `4*2^n` original edges. Let `W_{i,n}` be the trace of its complete ordered word. Define

\[
\mu_n(f)=\langle\psi_n,f\psi_n\rangle,
\quad r_{i,n}=(W_{i,n}-\mu_nW_{i,n})\psi_n,
\]
\[
R_n:\mathbb C^6\longrightarrow\mathcal H_n,
\quad R_nx=\sum_{i=1}^6 x_i r_{i,n},\quad G_n=R_n^*R_n.
\tag{4.2}
\]

The centering is the explicit orthogonal projection `I-|psi_n><psi_n|` applied to `W_{i,n}psi_n`. Each vector is physical and lies in every power domain of the original elliptic Hamiltonian. Since an `SU(2)` trace is real and lies in `[-2,2]`,

\[
\|r_{i,n}\|^2=\mu_n(W_{i,n}^2)-(\mu_nW_{i,n})^2\le4,
\quad \operatorname{tr}G_n\le24,\quad 0<G_n\preceq24I_6.
\tag{4.3}
\]

Strict positivity follows without changing these vectors: a vanishing linear combination is a continuous identity after division by the positive `psi_n`. Vary one edge in loop `i`, keep all other links equal to identity, and subtract the value at the all-identity configuration. The result is `x_i(tr U-2)=0` for every `U in SU(2)`, forcing `x_i=0`. Edge-disjointness supplies this argument for each `i`.

### 4.2 Correlation derivatives and explicit high-energy tails

For `t>0`, retain the matrix

\[
C_n(t)=R_n^*e^{-tA_n}R_n.
\tag{4.4}
\]

For integer `r>=1`, differentiating spectral scalar multipliers yields

\[
C_n^{(r)}(t)=(-1)^rR_n^*A_n^r e^{-tA_n}R_n.
\]

The scalar derivative of `lambda^r exp(-t lambda)` has its maximum at `lambda=r/t`, with value `(r/(et))^r`. Therefore

\[
\boxed{
0\preceq(-1)^rC_n^{(r)}(t)
\preceq24\left(\frac r{et}\right)^r I_6\quad(r\ge1),
\qquad 0\preceq C_n(t)\preceq24I_6.
}
\tag{4.5}
\]

The same norm bound holds for the holomorphic derivatives on `Re(t)>0`, with `t` replaced by `Re(t)`. The spectral multipliers and their derivatives are bounded there; differentiation in operator norm on compact subsets follows from the difference quotient and a dominating multiplier with one extra derivative. This proves all the asserted differentiability.

For a retained positive time `tau>0`, define the explicit state morphism

\[
S_{\tau,n}=e^{-\tau A_n/2}:\mathcal H_n\to\bigcap_{k\ge0}\operatorname{Dom}(A_n^k),
\qquad R_{\tau,n}=S_{\tau,n}R_n.
\tag{4.6}
\]

The vectors are not divided by their norms. Their Gram matrix is exactly `G_{tau,n}=C_n(tau)`. For every physical energy threshold `Lambda>0`,

\[
\boxed{
0\preceq R_{\tau,n}^*\mathbf1_{[\Lambda,\infty)}(A_n)R_{\tau,n}
\preceq24e^{-\tau\Lambda}I_6.
}
\tag{4.7}
\]

This follows by comparing the scalar multipliers `1_[Lambda,infty)(lambda)e^{-tau lambda}` and `e^{-tau Lambda}` on the entire nonnegative spectrum. Every quantity in (4.5)–(4.7) uses the full operator (1.4). The right sides are independent of `n`, `a_n`, `g_n` and `L_n`.

### 4.3 Extension to a countable separating supply of physical observables

At each graph level, take all monomials in the fundamental link matrix entries and their conjugates and average each monomial over the original compact vertex gauge group. Enumerate these averages over all levels. Each monomial and its average have absolute value at most one. They are smooth physical functions. The real and imaginary parts may also be retained as separate entries with the same bound. Transport an entry introduced at level `r` to level `n>=r` by the exact product pullback `J_{r,n}`.

For completeness, these averages span a dense physical subspace at each fixed level. The polynomial *-algebra contains constants, separates points of the compact product of matrix groups, and is closed under conjugation. The Stone–Weierstrass theorem gives uniform density in continuous functions; continuous functions are dense in Haar `L^2`. Gauge averaging is an orthogonal projection, so averaging this dense space gives density in its physical range. Multiplication by the original positive smooth vacuum is bounded with bounded inverse on the compact group; consequently the centered vectors from these averages span densely in `psi_n`-orthogonal physical space at that level.

Include the six entries (4.1) first. For any finite list of these observables with actual sup bounds `B_i`, put

\[
K_m=\sum_{i=1}^m B_i^2.
\tag{4.8}
\]

The proof of (4.3) gives `tr G_n <= K_m`. Every subsequent estimate for this finite list holds with `24` replaced by `K_m`. No bound independent of the length of the observable list is asserted. This supplies a single countable index set for the diagonal construction in §6, rather than restricting that construction to six modes.

### 4.4 Exact zero-time energy moments, with the full lattice factor

The positive-time bounds have the following exact zero-time companion. In the source's original quaternion coordinates write an arbitrary loop holonomy as

\[
U_C=q_0I-i\sum_{\alpha=1}^3q_\alpha\sigma_\alpha,
\qquad \sum_{\alpha=0}^3q_\alpha^2=1,
\qquad W_C=2q_0.
\]

For a varied original edge of this loop, cyclicity of the trace places its generator at the beginning of an ordered loop word. An inversely traversed edge supplies the corresponding minus sign and conjugated generator. Conjugation acts by the same orthogonal adjoint matrix in (1.10), so in either orientation the sum of derivative squares is unchanged. Direct matrix multiplication gives `tr(T_alpha U_C)=-q_alpha`. Therefore every edge in the loop satisfies

\[
\boxed{\sum_{\alpha=1}^3|X_{e,\alpha}W_C|^2
=\sum_{\alpha=1}^3q_\alpha^2
=1-\frac{W_C^2}{4}.}
\tag{4.9}
\]

For an edge outside the loop, all these derivatives are zero. The complete ground-state identity in [YM1], polarized in the two centered functions, is

\[
\langle r_{i,n},A_n r_{j,n}\rangle
=\frac{2g_n^2}{a_n}\sum_{e,\alpha}
\int\psi_n^2(X_{e,\alpha}W_{i,n})(X_{e,\alpha}W_{j,n})\,dU_n.
\tag{4.10}
\]

This follows directly by expanding the kinetic product derivatives, integrating by parts, and inserting the exact equation `H_n psi_n=E_{0,n} psi_n`; the full multiplication term cancels against the same term in that exact equation. Thus its effects remain in the actual vacuum `psi_n` and its moments. Edge-disjointness in (4.1) makes every off-diagonal integrand zero. Each of the six loops has exactly `4*2^n` edges. Consequently

\[
\boxed{
-C_n'(0)=\int_{[0,\infty)}\lambda\,d\mu_n(\lambda)
=\frac{8g_n^2a_0}{a_n^2}
\operatorname{diag}_{i=1}^6\left(1-\frac{\mu_n(W_{i,n}^2)}4\right).
}
\tag{4.11}
\]

Here `mu_n` in the integral denotes the matrix spectral measure defined in (6.2), and `mu_n(W^2)` denotes the vacuum functional in (4.2); their types and both definitions are explicit. Equivalently, with the original means `m_{i,n}=mu_n(W_{i,n})`, the diagonal entry is

\[
\frac{8a_0}{a_n^2(g_0^{-2}+\beta n\log2)}
\left(1-\frac{(G_n)_{ii}+m_{i,n}^2}{4}\right).
\tag{4.12}
\]

Equations (4.11)–(4.12) retain both the exact regulator growth factor and its exact interacting-vacuum multiplier. They express the complete first spectral moment in measured coordinate entries, including the off-diagonal zeros. All six vectors lie in the operator domain, so the derivative and the finite first moments at zero used here exist at every original finite regulator.

## 5. Uniform retained Schur memory and its raw metric

Fix `tau>0`. Abbreviate `R=R_{tau,n}`, `G=R^*R`, `A=A_n`, and define

\[
P=RG^{-1}R^*,\quad Q=I-P,\quad B=QAR:\mathbb C^6\to Q\mathcal H_n,
\]
\[
D=QAQ:\operatorname{Dom}(A)\cap Q\mathcal H_n\to Q\mathcal H_n.
\tag{5.1}
\]

The multiplier in (4.6) is strictly positive on every finite spectral value and hence has zero kernel. Therefore `R` is injective and its displayed finite Gram inverse exists. Direct multiplication gives `P=P^*=P^2`, `PR=R`, and `QR=0`. These facts retain the original coefficient metric `G`.

### 5.1 Compression domain

The range of `P` is contained in `Dom(A)`. The operator `AP` is bounded finite rank, with adjoint the bounded extension of `PA`. Thus `QAP+PAQ` is bounded self-adjoint. The operator

\[
A-(QAP+PAQ)
\]

on `Dom(A)` is self-adjoint: for real `T` exceeding the bounded perturbation norm, factor its shifts by `+/-iT` using the resolvent of `A`; the remaining factors have convergent Neumann inverses. This symmetric operator has both such shifts onto and is therefore self-adjoint. It commutes with `P` on its domain, whose `P` and `Q` parts are preserved. Its restriction to the reducing `Q` subspace is `D`. Finally `<v,Dv>=<v,Av>>=0`, so `D` is nonnegative. Consequently `(D+s)^{-1}` exists on \(Q\mathcal H_n\) for `s>0` and has norm at most `s^{-1}`.

### 5.2 Bounds with all regulator dependence removed from the right side

Define the full memory, reduced matrix and restored-vector map

\[
\mathcal M_{\tau,n}(s)=B^*(D+s)^{-1}B,
\]
\[
F_{\tau,n}(s)=R^*AR+sG-\mathcal M_{\tau,n}(s),
\qquad L_{\tau,n}(s)=R-(D+s)^{-1}B.
\tag{5.2}
\]

Spectral calculus in (4.6) and the scalar maximum already computed give

\[
\|AR\|^2\le\frac{96}{e^2\tau^2},\qquad
0\preceq R^*AR\preceq\frac{24}{e\tau}I_6.
\tag{5.3}
\]

Since `||Q||<=1`, the first also bounds `||B||^2`. Differentiating the resolvent now proves for every integer `r>=0`

\[
\boxed{
0\preceq(-1)^r\mathcal M_{\tau,n}^{(r)}(s)
=r!B^*(D+s)^{-r-1}B
\preceq\frac{96r!}{e^2\tau^2s^{r+1}}I_6.
}
\tag{5.4}
\]

The identity `Q(A+s)L=0` follows by substitution in (5.2). Since `R^*Q=0`, expansion gives

\[
\boxed{
F_{\tau,n}'(s)=G+B^*(D+s)^{-2}B=L_{\tau,n}(s)^*L_{\tau,n}(s),
}
\tag{5.5}
\]
\[
\boxed{
F_{\tau,n}(s)=L_{\tau,n}(s)^*(A+s)L_{\tau,n}(s),
\quad sG\preceq F_{\tau,n}(s)
\preceq24\left(s+\frac1{e\tau}\right)I_6.
}
\tag{5.6}
\]

For the lower bound, `||Lx||^2=||Rx||^2+||(D+s)^{-1}Bx||^2` by orthogonality. This also proves the uniform raw-metric bound

\[
G\preceq F_{\tau,n}'(s)
\preceq\left(24+\frac{96}{e^2\tau^2s^2}\right)I_6.
\tag{5.7}
\]

Solving `(A+s)(Rx+v)=Ry` in its `P,Q` components yields `F(s)x=Gy` and `v=-(D+s)^{-1}Bx`. Hence

\[
\boxed{
R^*(A+s)^{-1}R=G F(s)^{-1}G.
}
\tag{5.8}
\]

Equations (5.4)–(5.7) bound the memory and restored raw metric across the actual simultaneous regulator path. Equation (5.8) retains both Gram factors and the matrix inverse at each finite regulator.

## 6. Infinite-regulator spectral limit with both endpoint masses retained

Let `X=[0,infty]` be the compact space obtained by adjoining one point at infinite energy. A neighborhood of that point is `(M,infty]`, with the original energy threshold `M`. Define

\[
k_t(\lambda)=e^{-t\lambda}\quad(\lambda<\infty),\qquad k_t(\infty)=0,
\quad t>0.
\tag{6.1}
\]

For the six original vectors define the positive matrix-valued measures

\[
\mu_{n,ij}(B)=\langle r_{i,n},\mathbf1_B(A_n)r_{j,n}\rangle
\quad(B\subset[0,\infty)),\qquad \mu_n(\{\infty\})=0.
\tag{6.2}
\]

Then

\[
G_n=\mu_n(X),\qquad C_n(t)=\int_X k_t\,d\mu_n.
\tag{6.3}
\]

For every finite measurable partition, Cauchy–Schwarz for the spectral projections gives

\[
\sum_b|\mu_{n,ij}(B_b)|
\le\left(\sum_b\|\mathbf1_{B_b}(A_n)r_{i,n}\|^2\right)^{1/2}
\left(\sum_b\|\mathbf1_{B_b}(A_n)r_{j,n}\|^2\right)^{1/2}
\le4.
\tag{6.4}
\]

Thus each entry has total variation at most four, uniformly in `n`.

### 6.1 A single subsequence and its smooth kernel

Here is a direct sequential construction. Fix a retained time `t_*>0`. The map

\[
x:X\to[0,1],\qquad x(\lambda)=e^{-t_*\lambda},\quad x(\infty)=0
\tag{6.5}
\]

is a continuous bijection, with inverse `lambda=-log(x)/t_*` for `x>0` and `infty` for `x=0`. This proves its exact topological type while retaining the energy and time in both directions. Polynomials in `x` with rational complex coefficients form a countable uniformly dense subalgebra of `C(X)`, by ordinary polynomial approximation on `[0,1]`.

For every pair of observable indices from §4.3 and each member of this countable test algebra, consider the sequence after the larger introduction level of the two observables. This eventually defined sequence of integrals is bounded. Repeated subsequence selection and the diagonal sequence give convergence for all of them simultaneously. The total-variation bound extends the limit uniquely to every `f in C(X)`. Positive quadratic combinations remain positive; the representation of a bounded positive functional on a compact space by its finite Borel measure supplies a consistent positive matrix-valued measure `mu` for every finite list. The construction uses one subsequence, denoted `n_k`, for the entire countable list.

In particular,

\[
G_{n_k}\longrightarrow G_\infty=\mu(X),\qquad
C_{n_k}(t)\longrightarrow C_\infty(t)=\int_Xk_t\,d\mu.
\tag{6.6}
\]

For every `r>=0` and compact time interval `[delta,T]` with `delta>0`, the functions `lambda^r e^{-t lambda}`, extended by zero at infinity, are continuous on `X`; their suprema and their next time derivatives are uniformly bounded by (4.5). A finite time grid plus this derivative bound upgrades pointwise convergence to uniform convergence on `[delta,T]`. Applying this to every `r` proves

\[
\boxed{C_{n_k}\longrightarrow C_\infty
\text{ in }C^\infty_{\rm loc}((0,\infty);M_6(\mathbb C)).}
\tag{6.7}
\]

This is an actual subsequential limit along (1.1), not a uniqueness assertion for all regulator subsequences.

### 6.2 Raw infinite-energy mass and zero-energy mass

Define the two retained positive matrices

\[
E_\infty=\mu(\{\infty\}),\qquad Z_0=\mu(\{0\}).
\tag{6.8}
\]

Monotone convergence applied to each positive scalar quadratic form gives

\[
\boxed{
G_\infty=\lim_{t\downarrow0}C_\infty(t)+E_\infty,
\qquad
Z_0=\lim_{t\to\infty}C_\infty(t).
}
\tag{6.9}
\]

At each finite regulator, `mu_n({0})=0` because the vectors (4.2) are orthogonal to the unique vacuum. Formula (6.9) retains the actual zero-energy atom of the limiting measure as an additional datum; its value is not assigned by that finite-regulator identity.

For the explicitly transported vectors (4.6), the measure is

\[
d\nu_{\tau,n}=k_\tau\,d\mu_n,\qquad
\nu_{\tau,n_k}\longrightarrow\nu_\tau=k_\tau\mu.
\tag{6.10}
\]

Multiplication by the continuous function `k_tau` proves convergence. It also gives `nu_tau({infty})=0` and the uniform tail bound (4.7). The entire source measure remains retained. The multiplier has kernel precisely the measures supported at infinity, as proved in §7; its attenuation at each finite energy is the displayed factor `exp(-tau lambda)`.

### 6.3 Limiting resolvents without replacing the raw matrix products

For `s,tau>0`, use the scalar integral `1/(lambda+s)=int_0^infty exp(-(lambda+s)t)dt`. Then (5.8) gives

\[
\begin{aligned}
Z_{\tau,n}(s)
&:=G_{\tau,n}F_{\tau,n}(s)^{-1}G_{\tau,n}\\
&=\int_0^\infty e^{-st}C_n(\tau+t)\,dt
=\int_X\frac{k_\tau(\lambda)}{\lambda+s}\,d\mu_n(\lambda).
\end{aligned}
\tag{6.11}
\]

The multiplier at infinity is zero. The uniform bound `||C_n||<=24` supplies an integrable dominating function `24e^{-st}`. Thus

\[
\boxed{
\lim_{k\to\infty}G_{\tau,n_k}F_{\tau,n_k}(s)^{-1}G_{\tau,n_k}
=\int_0^\infty e^{-st}C_\infty(\tau+t)\,dt.
}
\tag{6.12}
\]

The two original Gram factors and the finite-regulator inverses remain in the left side. An inverse of a limiting Gram matrix is not needed to define the right side.

### 6.4 Simultaneous smooth Schur-memory limits and their endpoint records

The preceding subsequence can retain the full Schur memory itself. Fix a positive time `tau_0` and use the countable set `T={tau_0} union {q t_*:q in Q, q>0}`. For each `tau in T`, the six-vector matrices `B_{tau,n}` and self-adjoint compressions `D_{tau,n}` are exactly those of §5. Define their positive matrix-valued measures on `X` by

\[
\sigma_{\tau,n}(S)
=B_{\tau,n}^*\mathbf1_S(D_{\tau,n})B_{\tau,n}
\quad(S\subset[0,\infty)),
\qquad \sigma_{\tau,n}(\{\infty\})=0.
\tag{6.13}
\]

Their total matrices obey

\[
0\preceq\sigma_{\tau,n}(X)=B_{\tau,n}^*B_{\tau,n}
\preceq\frac{96}{e^2\tau^2}I_6.
\]

The partition argument in (6.4) consequently bounds every entry's total variation by `96/(e^2 tau^2)`. Include their integrals against the same countable test algebra in the diagonal selection in §6.1. The result is one subsequence for all the correlation measures and all `tau in T`, with positive weak limits `sigma_tau`.

For `s>0`, the multiplier `(lambda+s)^{-1}` on finite energies, extended by zero at infinity, is continuous on `X`. The same holds for every derivative in `s`. The uniform derivative bounds in (5.4), followed by the finite-grid argument used for (6.7), prove the actual limits

\[
\boxed{
\mathcal M_{\tau,n_k}\longrightarrow\mathcal M_{\tau,\infty}
\quad\hbox{in }C^\infty_{\rm loc}((0,\infty);M_6(\mathbb C)),
\qquad
\mathcal M_{\tau,\infty}(s)
=\int_X\frac{d\sigma_\tau(\lambda)}{\lambda+s}.
}
\tag{6.14}
\]

The multiplier at infinity in (6.14) is defined to be zero. Set

\[
F_{\tau,\infty}(s)
=-C_\infty'(\tau)+sC_\infty(\tau)
-\mathcal M_{\tau,\infty}(s).
\tag{6.15}
\]

This is the smooth limit of the original finite matrices `F_{tau,n_k}`. In particular the raw restored metric has the exact coefficient limit

\[
\boxed{
\lim_{k\to\infty}L_{\tau,n_k}(s)^*L_{\tau,n_k}(s)
=F_{\tau,\infty}'(s)
=C_\infty(\tau)+\int_X\frac{d\sigma_\tau(\lambda)}{(\lambda+s)^2}.
}
\tag{6.16}
\]

Every inequality in (5.4), (5.6), and (5.7) passes to these displayed finite-matrix limits. The product limit (6.12) also remains valid along this same subsequence; (6.15)–(6.16) require no inverse of a limiting Gram matrix.

Finally retain the endpoint matrices

\[
\Xi_\tau=\sigma_\tau(\{\infty\}),\qquad
Y_\tau=\sigma_\tau(\{0\}),\qquad
K_{\tau,\infty}=\sigma_\tau(X).
\]

The exact scalar multiplier `s/(lambda+s)` is bounded between zero and one at finite energies, and is zero at infinity. Dominated convergence, separately as `s` increases without bound and as `s` decreases to zero, gives

\[
\boxed{
K_{\tau,\infty}
=\lim_{s\to\infty}s\mathcal M_{\tau,\infty}(s)+\Xi_\tau,
\qquad
Y_\tau=\lim_{s\downarrow0}s\mathcal M_{\tau,\infty}(s).
}
\tag{6.17}
\]

Thus the limiting coupling-vector Gram matrix, memory, restored metric, and both of its endpoint atoms are retained together. The same boundary primitive in §7 applied entrywise to `sigma_tau` is the corresponding entry of `Xi_tau`.

## 7. The infinite-energy boundary as a literal Split Zero complex

Let `M(X)` be the complex vector space of finite complex Borel measures on `X`. At support `0`, use the cochain window

\[
C_0^0=0\longrightarrow C_0^1=M(X)\longrightarrow0.
\]

At support `1`, use

\[
C_1^0=\mathbb C\xrightarrow{\ d_1:c\mapsto c\delta_\infty\ }
 C_1^1=M(X)\longrightarrow0.
\tag{7.1}
\]

The support transition is the zero inclusion in degree zero and the identity on `M(X)` in degree one; its cochain square commutes exactly. Restriction to finite energies supplies the explicit cohomology isomorphism

\[
\Theta:H^1(C_1)\xrightarrow{\cong}M([0,\infty)),\qquad
[\nu]\longmapsto\nu|_{[0,\infty)}.
\tag{7.2}
\]

Its inverse extends a finite measure by zero at infinity and takes its class. Composing the maps changes `nu` by precisely `nu({infty}) delta_infty`, which is the displayed boundary with primitive `nu({infty})`. Consequently

\[
\boxed{
\ker(H^1(C_0)\to H^1(C_1))=\mathbb C\delta_\infty,
\quad c\delta_\infty\longleftrightarrow c.
}
\tag{7.3}
\]

There is also an exact identification with the kernel of the positive-time observation map

\[
\mathcal L:M(X)\to C^\infty((0,\infty)),
\qquad \mathcal L\nu(t)=\int_Xk_t\,d\nu.
\]

Indeed, `L(delta_infty)=0`. Conversely, `L nu=0` implies `int x^j d nu=0` for every integer `j>=1`, using (6.5). Every continuous function of `x` vanishing at zero is uniformly approximated by polynomials with zero constant term: approximate by a polynomial and subtract its value at zero. Hence `nu` annihilates all continuous functions vanishing at infinity. It is therefore `c delta_infty`, with `c=nu(X)`, proving

\[
\boxed{\ker\mathcal L=\mathbb C\delta_\infty.}
\tag{7.4}
\]

Apply the Split Zero reconstruction of [SZ] to this two-support complex over `C`. The map sends `(0,c delta_infty)` to the supported zero `(1,0)`, while (7.3) retains its source and unique primitive `c`. Entry by entry, the actual boundary primitive for the spectral limit is exactly `(E_infty)_{ij}`. This ties the retained-zero construction to a concrete infinity in the regulator limit.

The same two-support construction records the full refinement defect (1.13): replace `M(X)` by \(\mathcal H_{n+1}\), replace `d_1` by `A_{n+1}+s` on its actual domain, and take source vector `D_n(A_n+s)^{-1}u`. Its unique primitive is `(A_{n+1}+s)^{-1}D_n(A_n+s)^{-1}u`, with the minus sign in (1.13). Thus both the finite refinement defect and the infinite-energy boundary have explicit typed primitives.

## 8. Positive-time Hilbert reconstruction and energy-window bounds

Use the single subsequence and countable observable list from §6. Form the complex vector space of finite formal sums

\[
v=\sum_b c_b[i_b,t_b],\qquad t_b>0,
\]

and define its exact sesquilinear form by

\[
\langle v,w\rangle
=\sum_{b,c}\overline{c_b}d_c\,
 C_{\infty,i_bj_c}(t_b+s_c).
\tag{8.1}
\]

For a finite list of indices, the spectral expression is the integral of
`sum_ij conjugate(w_i(lambda)) w_j(lambda) d mu_ij(lambda)`, with
`w_i(lambda)=sum_{b:i_b=i}c_b exp(-t_b lambda)`. It is nonnegative. Quotient by the explicitly defined null space and complete; call the resulting Hilbert space `H_lim`.

For `h>=0`, define

\[
T(h)[i,t]=[i,t+h].
\tag{8.2}
\]

The spectral expression for the change in squared norm is the integral of
`(1-exp(-2h lambda)) sum_ij conjugate(w_i)w_j d mu_ij`, which is nonnegative. Hence `T(h)` descends to a contraction. The identical expression with multiplier `exp(-h lambda)` proves that it is positive and self-adjoint. The parameter addition proves `T(h+k)=T(h)T(k)`.

For a finite formal vector, the squared norm of `(T(h)-I)v` is the same integral with multiplier `|exp(-h lambda)-1|^2`. Dominated convergence gives its limit zero as `h downarrow 0`; the positive times `t_b` make the integrand vanish at infinity. Contractivity extends this convergence to every vector of `H_lim`. Thus `T` is a strongly continuous self-adjoint contraction semigroup.

A direct resolvent construction supplies its nonnegative self-adjoint generator. For `s>0`, set

\[
\mathscr R(s)=\int_0^\infty e^{-sh}T(h)\,dh.
\]

This is bounded positive self-adjoint and at most `s^{-1}I`. The semigroup law and Fubini prove
`R(s)-R(t)=(t-s)R(s)R(t)`. For every nonzero `v`, strong continuity at zero gives `<v,R(s)v>>0`, so `R(s)` is injective and has dense range. Spectral calculus for this bounded positive self-adjoint operator defines `R(s)^{-1}` on its range. The resolvent identity shows that `A_lim=R(s)^{-1}-s` is independent of `s`; it is self-adjoint and nonnegative. The Laplace transform of `exp(-h A_lim)` equals the displayed resolvent. Uniqueness of scalar Laplace transforms, applied to every matrix coefficient, identifies this semigroup with `T(h)`. On the formal heat-vector space its energy form is

\[
\boxed{
\langle[i,t],A_{\rm lim}[j,s]\rangle
=-C_{\infty,ij}'(t+s).
}
\tag{8.3}
\]

For a heat vector, the difference quotients of `T(h)` converge in the Hilbert norm: in the spectral formula their multipliers converge to `-lambda exp(-t lambda)` and are dominated in squared norm by `lambda^2 exp(-2t lambda)`, which is bounded and integrable. This proves membership in `Dom(A_lim)` and (8.3). Repetition proves the higher derivative formulas using `lambda^{2r}exp(-2t lambda)`.

The span of these heat vectors is an operator core. Indeed it is dense and preserved by every `T(epsilon)`. For `v in Dom(A_lim)`, `T(epsilon)v` converges to `v` in graph norm as `epsilon` decreases to zero. At fixed positive `epsilon`, approximate `v` in Hilbert norm by finite heat-vector sums; applying `T(epsilon)` upgrades convergence to graph norm because `||A_lim T(epsilon)||<=1/(e epsilon)`. These two approximations prove the core assertion without changing the original sesquilinear form.

The exact retained energy-window estimates are as follows. For `m>0`, `tau>0`, and `t>0`, let

\[
N_\tau(m)=\nu_\tau([0,m]).
\]

On `[0,m]`, `e^{-t lambda}>=e^{-tm}`; on `(m,infty)`, `e^{-t lambda}<=e^{-tm}`. Integrating these two pointwise inequalities, respectively, gives

\[
\boxed{
\frac{C_\infty(\tau+t)-e^{-tm}C_\infty(\tau)}{1-e^{-tm}}
\preceq N_\tau(m)
\preceq e^{tm}C_\infty(\tau+t).
}
\tag{8.4}
\]

The lower matrix may have negative eigenvalues; the displayed Loewner inequality still follows from the integral proof. The zero-energy atom is `Z_0`, as in (6.9). These formulas keep the finite-energy, zero-energy and infinite-energy contributions in their actual spectral positions.

## 9. Verification scope and end state of this continuation

`verify.py` is an offline, standard-library exact-arithmetic checker. It verifies:

- ordered quaternion holonomy composition, gauge cancellation and inverse paths;
- the two-subedge Casimir identity on every four-coordinate polynomial monomial through degree three, using exact polynomial differentiation, and the original loop-trace derivative-square identity;
- the non-Abelian commutator sign and magnetic fourth-order coefficient in a formal plaquette word;
- the raw-Gram Schur lift, its energy and derivative metric, and the compressed-resolvent identity on an explicitly declared rational positive operator with a zero vacuum eigenvalue;
- the complete algebraic defect-composition identity and the retained-jet product coefficients.

These finite checks test formulas and their signs. Their matrices are declared test data, not a computed spectrum of the Yang–Mills Hamiltonians. Infinite-dimensional bounds, smooth-germ kernel, magnetic remainder and subsequence reconstruction are proved in the preceding text; execution of the finite checks is not described as a formal proof of those analytic arguments.

The previous 112-block cubic certificate is separately replayed from the user-supplied script, and its output is compared to the supplied certificate. It is provenance for the preceding continuation, not a calculation of the new regulator-limit spectral measure.

The completed endpoint is a smooth positive-time spectral extension along an explicit simultaneous path, a high-energy tail bound and a Schur-memory derivative bound uniform along that path, exact smooth-source and refinement maps, and retained source data for the two energy endpoints. No numerical value is assigned here to the limiting matrices `E_infty`, `Z_0`, `Xi_tau`, `Y_tau`, or the low-energy measure in (8.4). Nontriviality of a limiting quantum field theory is not established by the positive-time spectral reconstruction alone. No positive mass lower bound for the limiting four-dimensional theory is established by this contribution. No remote repository modification is claimed.


---

# Chapter 5 — 20260914-vacuum-refinement-infrared / RESEARCH_NOTE.md

Original text path: `workbench/yang-mills/continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md`.

# Vacuum-aware refinement, smooth holonomy sections, and an infrared Schur budget

14 September 2026. Additive research continuation against Yang–Mills commit
`fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`.

This note proves five connected statements for the retained programme: smooth local sections of the complete finite-link holonomy map with their exact curvature cost; refinement in the actual interacting vacuum measure with a complete Dirichlet square identity; a projective equal-time vacuum limit; a regulator-uniform inverse-energy Schur budget; and the exact kernel comparing regulator-state sequences to the reconstructed observable space. The last construction corrects the escaping-label inference in the preceding spectral-reconstruction note. No positive continuum mass lower bound is asserted.

## 1. Source objects and conventions

[YM] is `yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`, §§1–2, at the commit above. [SR] is `yang-mills/continuations/20260914-spectral-reconstruction/RESEARCH_NOTE.md` at the same commit. [S6] is `s6/27_s6_key_advances_frozen_2026-09-06.tex`, §3, at the same commit. [SZ] is `formal/splitzero/DERIVED_MATHEMATICS.md`, §§1–4, in `KokunoYumeto/zeta-function-research-reader` at `7ea0a49945390eae14d3160a5730858899768b5f`. These source bodies were inspected. The S6 source supplies explicit formulas and locations of its longer proofs; the elementary quotient-map verification used below is written here.

Keep the original generators `T_alpha=-i sigma_alpha/2`, product Haar probability `dU_n`, and all oriented plaquette words. Fix the actual sequence

\[
a_n=a_0 2^{-n},\quad L_n=4\,2^{2n},\quad
g_n^2=(g_0^{-2}+\beta n\log 2)^{-1},\qquad a_0,g_0,\beta>0.
\tag{1.1}
\]

The displayed beta is a prescribed path parameter. On the open graph with vertices `{-L_n,...,L_n}^3`, let `Q_n=SU(2)^{E_n}` and

\[
\kappa_n=2g_n^2/a_n,\quad
H_n=-\kappa_n\sum_{e,\alpha}X_{e,\alpha}^2+
\frac1{2g_n^2a_n}\sum_p(2-\operatorname{tr}U_p),\quad
A_n=H_n-E_{0,n}I.
\tag{1.2}
\]

The positive unit vacuum `psi_n`, its exact energy `E_{0,n}`, and the invariant `H^2` and `H^1` operator/form domains are those of [YM]. Write `rho_n=psi_n^2`. Multiplication

\[
\mathscr U_n:L^2(Q_n,\rho_n dU_n)\longrightarrow L^2(Q_n,dU_n),
\qquad f\longmapsto\psi_n f
\tag{1.3}
\]

has inverse `u -> u/psi_n` and preserves the displayed inner products. Both maps preserve the physical invariant subspaces. The full ground-state identity is

\[
q_{A_n}(\mathscr U_n f)=\kappa_n\int\rho_n
\sum_{e,\alpha}|X_{e,\alpha}f|^2dU_n.
\tag{1.4}
\]

Its polarized form follows by expanding the kinetic derivatives and using the exact equation `H_n psi_n=E_{0,n} psi_n`. Every magnetic term enters that vacuum equation and the actual density `rho_n`.

## 2. Smooth extension with the complete curvature cost

### 2.1 The inspected S6 map

The source's retained data obey `gamma(Lambda) subset Z`, `gamma A=gamma`, `gamma(v)=epsilon in {1,-1}`, and `zeta=exp(-2 pi i/m)`. Set

\[
H(x)=e^{-2\pi i\epsilon\gamma(x)}.
\]

Then `H(x+lambda)=H(x)` and

\[
H(Ax+v/m)=e^{-2\pi i\epsilon(\gamma(x)+\epsilon/m)}=\zeta H(x).
\]

The retained deck actions on the total line are `(x,z) -> (x+lambda,z)` and `(x,z) -> (Ax+v/m,zeta z)`. Consequently the quotient-line maps

\[
[x,z]\longmapsto([x],z/H(x)),\qquad
([x,w])\longmapsto[x,wH(x)]
\tag{2.1}
\]

are invariant under both displayed deck generators, are smooth, and compose to the respective identities. The factor `H` remains in the inverse. The source uses `m=3,4`. The following Yang–Mills sections are constructed with their own explicit domains, inverses, and energy factors.

### 2.2 Smooth local sections at every finite-link configuration

Fix level `r` and a reference configuration `U^0 in Q_r`. For each positive edge `e=(x,x+a_r e_i)`, choose two real smooth profiles `p_0,p_1` with disjoint compact supports in `(1/4,3/8)` and `(5/8,3/4)`. Retain their actual nonzero integrals and squared integrals

\[
I_j=\int p_j(t)dt,\qquad J_j=\int p_j(t)^2dt\quad(j=0,1).
\]

Choose `chi in C_c^infty(R^2;R)` supported in the unit disk with `chi(0)=1`, and retain `J_chi=int |grad chi|^2`. Choose `0<epsilon<1/16`. The tubes of transverse radius `epsilon a_r` about these central edge segments are disjoint, including between edges in different coordinate directions.

Choose `K_e^0 in su(2)` with `exp K_e^0=U_e^0`. On the open neighborhood where the spectrum of `(U_e^0)^{-1}U_e` avoids the negative real axis, use the analytic matrix logarithm

\[
K_e(U)=\log((U_e^0)^{-1}U_e).
\]

For `x'=x+a_r t e_i+y`, `y perpendicular e_i`, define the one-form in the edge tube by

\[
\mathcal A_e(U)(x')=
\frac1{a_r}\left(\frac{p_0(t)}{I_0}K_e^0+
\frac{p_1(t)}{I_1}K_e(U)\right)
\chi\!\left(\frac{y}{\epsilon a_r}\right)dx_i,
\qquad \mathcal A(U)=\sum_e\mathcal A_e(U).
\tag{2.2}
\]

Every profile and every integral stays in (2.2). Extending each summand by zero gives a compactly supported smooth connection. It depends smoothly on `U` in the displayed neighborhood. In the original transport convention `V'=V mathcal A(dot gamma)`, the exact edge transport is

\[
\operatorname{Hol}_e(\mathcal A(U))=
\exp K_e^0\,\exp K_e(U)=U_e.
\tag{2.3}
\]

Indeed the two longitudinal supports are ordered and disjoint, and their integrals are respectively `K_e^0,K_e(U)`. The transverse cutoff equals one on the edge; every other edge misses that tube. Thus (2.2) is a smooth local right inverse of the **whole** finite-link holonomy map at every `U^0`, including reference links equal to `-I`.

All products between connection components in one tube have the same differential `dx_i`, and distinct tubes are disjoint. Therefore `mathcal A wedge mathcal A=0` for this constructed connection. The curvature in a tube is its exact transverse derivative. With the original matrix Frobenius norm,

\[
\boxed{
\int_{\mathbb R^3}\sum_{i<j}\|F_{ij}(\mathcal A(U))\|_F^2dx
=\frac{J_\chi}{a_r}\sum_{e\in E_r}
\left(\frac{J_0}{I_0^2}\|K_e^0\|_F^2+
\frac{J_1}{I_1^2}\|K_e(U)\|_F^2\right).
}
\tag{2.4}
\]

To verify the coefficient, a transverse derivative contributes `(epsilon a_r)^{-1}`, the connection contributes `a_r^{-1}`, and `dx=a_r(epsilon a_r)^2 dt dz`. Their squared factors leave `a_r^{-1}`. The disjoint longitudinal supports remove precisely the cross product of the two displayed profiles. The magnetic curvature functional retains the additional factor `1/(4g_r^2)` when (2.4) is inserted into that functional.

The maps (2.2)–(2.3) supply smooth local continuation. Equation (2.4) simultaneously retains its ultraviolet energy cost; none of its `a_r`, `g_r`, or profile factors is removed.

## 3. Refinement in the actual fine-vacuum measure

Fix `r<n` and `b=2^{n-r}`. Each coarse edge consists of `b` ordered fine links. Fine links outside those chains remain as variables. Put

\[
\pi_{r,n}(U)_e=U_{e,1}\cdots U_{e,b}.
\tag{3.1}
\]

An explicit global coordinate map is

\[
\Phi_{r,n}:Q_n\longrightarrow Q_r\times Z_{r,n},\quad
U\longmapsto(W,(U_{e,j})_{j<b},U_{\rm unused}),
\]

where `Z_{r,n}` is the product group with exactly `(b-1)|E_r|+|E_n|-b|E_r|` factors. Its inverse retains the displayed first `b-1` links and unused links and sets

\[
U_{e,b}=(U_{e,1}\cdots U_{e,b-1})^{-1}W_e.
\tag{3.2}
\]

Both compositions are identities. Haar translation in the last link on each chain proves `dU_n=dW dz` in these coordinates. Gauge equivariance is the cancellation of every intermediate vertex factor in (3.1).

Define the actual marginal and conditional map

\[
m_{r,n}(W)=\int_{Z_{r,n}}\rho_n(\Phi_{r,n}^{-1}(W,z))dz,
\]
\[
(\mathsf E f)(W)=\frac{1}{m_{r,n}(W)}
\int f(\Phi_{r,n}^{-1}(W,z))\rho_n(\Phi_{r,n}^{-1}(W,z))dz,
\quad \mathsf Jg=g\circ\pi_{r,n}.
\tag{3.3}
\]

These formulas retain the fine vacuum. The density `m=m_{r,n}` is smooth, strictly positive, gauge invariant, and has integral one. Fubini proves

\[
\mathsf J:L^2(m\,dW)\to L^2(\rho_n dU_n),\quad
\mathsf J^*\mathsf J=I,\quad\mathsf J^*=\mathsf E.
\tag{3.4}
\]

Thus `mathsf E mathsf J=I` and `mathsf P=mathsf J mathsf E` is an orthogonal projection. The maps commute with gauge averaging. Their comparison with the original coarse vacuum is also explicit: the identity-on-functions map from `L^2(rho_r dW)` to `L^2(m dW)` has squared norm pairing

\[
\langle f,g\rangle_m=\int\overline f g\frac{m}{\rho_r}\rho_r dW.
\tag{3.5}
\]

Both densities and their ratio remain recorded.

### 3.1 Exact horizontal fields and the retained density derivative

Write `P_{e,j-1}=U_{e,1}...U_{e,j-1}`, with the empty product `I`, and

\[
a_{e,j;\alpha\beta}=(\operatorname{Ad}_{P_{e,j-1}})_{\alpha\beta},\qquad
Y_{e,\alpha}=\frac1b\sum_{j=1}^b\sum_\beta
 a_{e,j;\alpha\beta}X_{e,j,\beta}.
\tag{3.6}
\]

Differentiation gives `X_{e,j,beta} mathsf Jg=sum_alpha a_{e,j;alpha beta} mathsf J X_{e,alpha}g`. Orthogonality of each adjoint matrix consequently proves

\[
Y_{e,\alpha}\mathsf Jg=\mathsf JX_{e,\alpha}g,
\qquad \langle Y_{e,\alpha},Y_{f,\gamma}\rangle
=b^{-1}\delta_{ef}\delta_{\alpha\gamma}.
\tag{3.7}
\]

The inner product in (3.7) is the generator-coordinate coefficient inner product of the original sum of squares. Each coefficient in a summand of (3.6) is independent of the differentiated link `U_{e,j}`. Each `X` has Haar divergence zero. Hence every `Y` has Haar divergence zero.

Define the actual centered density derivative

\[
S_{e,\alpha}=Y_{e,\alpha}\log\rho_n-
\mathsf J(X_{e,\alpha}\log m).
\tag{3.8}
\]

All these functions are smooth at each finite regulator. Integration by parts against a coarse smooth test function gives

\[
X_{e,\alpha}(m\mathsf E f)
=m\mathsf E(Y_{e,\alpha}f+fY_{e,\alpha}\log\rho_n).
\]

Applying this to `f=1` and then substituting back proves

\[
\boxed{\mathsf E S_{e,\alpha}=0,\qquad
X_{e,\alpha}\mathsf E f=
\mathsf E(Y_{e,\alpha}f)+\mathsf E(fS_{e,\alpha}).}
\tag{3.9}
\]

These component formulas hold on the full scalar spaces. Under gauge transformations their generator indices rotate by the endpoint adjoint matrices; the contracted expressions below preserve the physical invariant subspace.

### 3.2 The full Dirichlet square identity

For smooth physical `f`, put `g=mathsf E f`, `h=f-mathsf Jg`, and
`v_{e,alpha}=mathsf E(hS_{e,alpha})`. Then `mathsf E h=0` and (3.9) gives `mathsf E Y_{e,alpha}h=-v_{e,alpha}`.

Let `nabla_v` be the orthogonal complement of the fields in (3.7) in the original fine generator coordinates. More explicitly its chain component is

\[
(\nabla_v f)_{e,j,\beta}=X_{e,j,\beta}f-
\sum_\alpha a_{e,j;\alpha\beta}Y_{e,\alpha}f,
\tag{3.10}
\]

and its unused-edge components are the original `X f`. Squaring (3.10), using the adjoint identities, proves
`sum |Xf|^2=b sum |Yf|^2+|nabla_v f|^2` pointwise. Also `nabla_v mathsf Jg=0`. Conditional expansion of each horizontal square now proves

\[
\boxed{\begin{aligned}
q_{A_n}(\psi_n f)
={}&\kappa_n b\int m\sum_{e,\alpha}|X_{e,\alpha}g-v_{e,\alpha}|^2dW\\
&+\kappa_n b\int\rho_n\sum_{e,\alpha}
 |Y_{e,\alpha}h+\mathsf Jv_{e,\alpha}|^2dU_n\\
&+\kappa_n\int\rho_n|\nabla_vh|^2dU_n.
\end{aligned}}
\tag{3.11}
\]

The second line is exactly the conditional variance of `Yh`. The cross term retained in the expanded form is
`-2 kappa_n b Re int m sum overline{Xg} mathsf E(hS)`.
In particular the coarse cylindrical form is

\[
q_{A_n}(\psi_n\mathsf Jg)=\kappa_n b\int m\sum|Xg|^2dW,
\quad
\kappa_n b=\frac{2a_r}{a_n^2(g_0^{-2}+\beta n\log2)}.
\tag{3.12}
\]

The represented coarse operator on smooth functions is
`-kappa_n b m^{-1} sum X(m X)`; integrating by parts proves this expression directly. Equations (3.8) and (3.11) retain the entire fine-vacuum drift and the cross terms with fiber fluctuations.

There is also a completely evaluated global bound for the density derivative. Orthogonality in (3.7) and conditional variance give

\[
\int\rho_n\sum|S|^2\le\frac4b\int\sum|X\psi_n|^2
\le\frac{4E_{0,n}}{b\kappa_n}
\le\frac{2|P_n|}{b g_n^4}.
\tag{3.13}
\]

For the last step, the constant trial function has energy `|P_n|/(g_n^2 a_n)`: integrating any plaquette trace over one of its four distinct link variables gives zero. The potential is nonnegative, so the kinetic vacuum energy is at most `E_{0,n}`. The graph has `|P_n|=3(2L_n)^2(2L_n+1)`. Thus every regulator factor in this global bound is explicit.

### 3.3 Split Zero and the full hierarchy

Use the two cochain windows `0 -> H_f -> 0` and `ker mathsf E -> H_f -> 0`, with the second incoming map the actual inclusion. Here `H_f=L^2(rho_n dU_n)`, or its physical invariant subspace. The transition is the identity in the middle degree. The map

\[
H_f/\ker\mathsf E\longrightarrow H_c=L^2(m dW),
\quad[f]\longmapsto\mathsf E f
\tag{3.14}
\]

has inverse `g -> [mathsf Jg]`. Their compositions follow from `mathsf E mathsf J=I` and `f-mathsf J mathsf E f in ker mathsf E`. The transported-class kernel is exactly `ker mathsf E`; its boundary primitive is the original fluctuation `h`. Applying [SZ]'s two-support reconstruction records `(1,0)` together with that primitive. Equation (3.11) retains its full energy interaction.

For fixed `n`, the projections for all coarse levels obey `mathsf P_r mathsf P_s=mathsf P_min(r,s)`: test the conditional integrals against an arbitrary function of the coarser ordered products and use Fubini. Therefore, with `d_0=mathsf P_0 f` and `d_r=(mathsf P_r-mathsf P_{r-1})f`,

\[
f=\sum_{r=0}^n d_r,\quad
\operatorname{Var}_{\rho_n} f=\operatorname{Var}_{\rho_n}d_0+
\sum_{r=1}^n\|d_r\|_{\rho_n}^2,
\]
\[
q_{A_n}(\psi_n f)=\sum_{r,s=0}^n
\kappa_n\int\rho_n\sum_{e,\alpha}
\overline{X_{e,\alpha}d_r}X_{e,\alpha}d_s.
\tag{3.15}
\]

The first identity uses orthogonal projections. The second retains every off-diagonal energy entry.

## 4. A projective equal-time vacuum and its smooth sections

Let `nu_{r,n}=(pi_{r,n})_*(rho_n dU_n)`. At every finite `n`, the exact product law gives
`(pi_{r,s})_*nu_{s,n}=nu_{r,n}` for `r<s<=n`. Every `Q_r` is compact metric. Select a countable uniformly dense algebra of matrix-entry polynomials on each `Q_r`; diagonal subsequence selection for their bounded integrals gives one sequence `n_k` with weak limits `nu_r` for every `r`. Positivity and the bound by the uniform norm extend each limit functional to `C(Q_r)`, and its representing probability measure is `nu_r`. Testing against a continuous function proves `(pi_{r,s})_*nu_s=nu_r`.

The inverse limit

\[
\mathfrak Q=\{(W_r)_{r\ge0}:\pi_{r,r+1}W_{r+1}=W_r\}
\tag{4.1}
\]

is compact metric. Surjectivity of each (3.1) follows from (3.2). Compatible integration against `nu_r` defines a positive functional on its cylinder algebra. This algebra contains constants, is closed under conjugation, and separates points; uniform polynomial approximation and the representation of positive functionals therefore give a probability measure `nu` with all these marginals. Gauge invariance follows by change of variables at each finite level and passage to the same limits.

Smooth connections map into `mathfrak Q` by their complete ordered edge holonomies. ODE concatenation proves compatibility. This image is dense: a nonempty cylinder neighborhood is detected at some finite level `r`, and (2.2) realizes any chosen configuration at that level by a smooth compactly supported connection. For each finite level the local section and its exact curvature cost remain (2.2) and (2.4).

For any fixed cylindrical observables `O_i,O_j`, the complete equal-time Gram limit is consequently

\[
G^c_{ij}=\int\overline{O_i}O_j\,d\nu-
\overline{\int O_i d\nu}\int O_jd\nu.
\tag{4.2}
\]

The same diagonal selection can retain the positive-time correlations in [SR]. Their endpoint equation stays
`E_infty=G^c-C(0+)`. Thus the equal-time measure, the finite-energy correlations, and the exact endpoint defect have now been put on one actual refinement subsequence. No value of `E_infty` is assigned by this construction.

## 5. A regulator-uniform infrared Schur budget

Take a fixed finite list of smooth bounded physical observables. Write

\[
r_{i,n}=(O_{i,n}-\langle\psi_n,O_{i,n}\psi_n\rangle)\psi_n,
\quad R_{0,n}x=\sum_i x_i r_{i,n},\quad
K_*=\sum_i\|O_i\|_\infty^2.
\]

The exact variance identity gives `R_{0,n}^*R_{0,n} preceq K_* I`.
For a concrete six-vector frame, take the six positively oriented squares of physical side `a_0` in the `x^1,x^2` plane at `x^3=0`, with lower-left corners `a_0(-3,-3,0)`, `a_0(-1,-3,0)`, `a_0(1,-3,0)`, `a_0(-3,1,0)`, `a_0(-1,1,0)`, and `a_0(1,1,0)`. They lie in the original boxes and have disjoint edge sets; each loop uses exactly `4*2^n` fine edges. Take their complete ordered fundamental traces. Then `K_*=24`; independence follows by varying one edge in each loop while fixing all other links. Fix `tau>0`, set `R=e^{-tau A_n/2}R_{0,n}`, and use the following constructions for that six-vector frame. The heat multiplier is injective, so its raw Gram matrix `G=R^*R` is positive definite.

Set

\[
P=RG^{-1}R^*,\quad Q=I-P,\quad K=R^*A_nR,\quad
B=QA_nR,\quad D=QA_nQ\big|_{\operatorname{Dom}(A_n)\cap Q\mathcal H_n}.
\tag{5.1}
\]

`D` is self-adjoint and nonnegative. Indeed `A_nP` is bounded finite rank since the range of `R` lies in every power domain of `A_n`. Its adjoint is the bounded extension of `PA_n`. Subtracting `QA_nP+PA_nQ` from `A_n` is a bounded self-adjoint perturbation with reducing subspaces `P,Q`; its Q restriction is `D`, and its quadratic form there equals that of `A_n`.

For `s>0` define

\[
M(s)=B^*(D+s)^{-1}B,\quad F(s)=K+sG-M(s),\quad
L(s)=R-(D+s)^{-1}B,
\]
\[
d\sigma(\lambda)=B^*dE_D(\lambda)B.
\tag{5.2}
\]

Substitution gives `Q(A_n+s)L=0`. Orthogonality to the range of R proves

\[
F=L^*(A_n+s)L,\quad F'=L^*L=G+B^*(D+s)^{-2}B,
\quad R^*(A_n+s)^{-1}R=GF^{-1}G.
\tag{5.3}
\]

In particular `F>=sG`, so `M(s)<=K` for every `s>0`. This also follows directly by inserting `Rx-(D+s)^{-1}Bx` into the positive quadratic form of `A_n`; its value is `x^*[K-M(s)-sB^*(D+s)^{-2}B]x`.

Monotone convergence of the positive scalar contractions as `s downarrow0` now proves

\[
\boxed{\sigma(\{0\})=0,\qquad
M(0):=\int_{(0,\infty)}\lambda^{-1}d\sigma(\lambda)\preceq K.}
\tag{5.4}
\]

This proves inverse-energy integrability rather than imposing it. The heat multiplier maximum gives `K preceq K_* /(e tau) I`; for the six loops this is `24/(e tau) I`. It follows that

\[
\boxed{\sigma([0,\epsilon])\preceq\epsilon K
\preceq\frac{24\epsilon}{e\tau}I\quad(\epsilon>0).}
\tag{5.5}
\]

For `r>=1`, differentiation under the resolvent and (5.4) give the sharper bounds

\[
\boxed{
0\preceq(-1)^rM^{(r)}(s)
\preceq
\frac{r!r^r}{(r+1)^{r+1}s^r}K
\preceq\frac{24r!r^r}{e\tau(r+1)^{r+1}s^r}I,
\qquad 0\preceq M(s)\preceq K.
}
\tag{5.6}
\]

Indeed write `d alpha=lambda^{-1}d sigma`. The derivative integrand is `r! lambda/(lambda+s)^{r+1}`. The derivative of `lambda/(lambda+s)^{r+1}` in lambda is `(s-r lambda)/(lambda+s)^{r+2}`, so the maximum of the derivative integrand occurs at `lambda=s/r` and has precisely the displayed value. In particular

\[
\boxed{G\preceq F'(s)\preceq G+\frac{K}{4s},\qquad
sF'(s)\preceq F(s).}
\tag{5.7}
\]

The latter inequality also follows at once from (5.3) and `A_n>=0`.

### 5.1 The inverse-energy endpoint and its exact retained class

Restore the regulator suffix. Spectral calculus gives the additional bound
`B_n^*B_n preceq 4K_* /(e^2 tau^2) I`. Let
`d alpha_n=lambda^{-1}d sigma_n` on `(0,infty)`, with zero endpoint atoms initially. Its total matrix is at most `K_n`, and

\[
\alpha_n([\Lambda,\infty))\preceq
\frac{4K_*}{e^2\tau^2\Lambda}I.
\tag{5.8}
\]

Weak subsequence selection on `[0,infty]`, jointly with the previous selection, gives `alpha_n -> alpha`, `sigma_n -> sigma_infty`, `G_n -> G_infty`, `K_n -> K_infty`, and `S_n:=K_n-alpha_n([0,infty]) -> S_infty>=0`. Formula (5.8), tested with continuous tail cutoffs, proves `alpha({infty})=0`. Its possible atom at zero is retained as `Z_alpha=alpha({0})`.

For `s>0` the function `lambda/(lambda+s)`, extended by zero at zero and by one at infinity, is continuous on this compactification. Hence

\[
M_\infty(s)=\int\frac{\lambda}{\lambda+s}d\alpha(\lambda),
\qquad
\boxed{F_\infty(0+)=S_\infty+Z_\alpha.}
\tag{5.9}
\]

To prove the second equality, use `alpha(X)=lim M_n(0)`, `M_infty(0+)=alpha(X)-Z_alpha`, and `sG_n ->0` after the fixed-s regulator limit. Thus the endpoint correction is the exact difference between the two displayed zero-energy limit orders.

For clarity, the ordinary memory limit satisfies `sigma_infty({0})=0` and `int_(0,infty) lambda^{-1}d sigma_infty<=K_infty`. The first assertion follows by testing (5.5) with shrinking continuous cutoffs. On each compact finite-energy interval, `d sigma_infty=lambda d alpha`; monotone cutoff integration proves the second. The atom `Z_alpha` remains visible in (5.9).

On the vector space of finite complex measures on `[0,infty)`, the observation map

\[
\mathcal T\alpha(s)=\int\frac{\lambda}{\lambda+s}d\alpha(\lambda)
\tag{5.10}
\]

has kernel exactly `C delta_0`. Here is the converse proof. Vanishing for every `s>0` and bounded convergence as `s downarrow0` show that the restriction to `(0,infty)` has total mass zero. Then `lambda/(lambda+s)=1-s/(lambda+s)` shows that its Stieltjes transform vanishes. Differentiation at `s=1` gives all integrals `(lambda+1)^{-k}`, `k>=1`; the total mass supplies k=0. The explicit coordinate `x=(1+lambda)^{-1}`, with inverse `lambda=x^{-1}-1`, transports these to all polynomial moments on `[0,1]`. Polynomial approximation proves that the restricted measure is zero. This argument applies entry by entry.

The two-support windows `0 -> M ->0` and `C -> M ->0`, with incoming map `c -> c delta_0`, consequently have transported kernel `C delta_0`. Its actual primitive for the limit in (5.9) is each original matrix coordinate `(Z_alpha)_{ij}`. This is the inverse-energy Split Zero record.

## 6. The regulator-state comparison and the escaping-label kernel

Use one of the actual subsequences from [SR], jointly selected with §4. Let `z_{i,t,n}=e^{-tA_n}r_{i,n}` for positive rational times. The limiting symbols `z_{i,t}` span densely in the separable reconstructed space `H_obs`. Let `B_lim` be the vector space of bounded regulator-state sequences `(v_n)` for which every scalar limit
`lim <z_{i,t,n},v_n>` exists. Omit finitely many indices preceding an observable's birth. Let `N` be its subspace with `||v_n|| ->0`.

For a finite symbol sum z, define

\[
\ell_v(z)=\lim_n\langle z_n,v_n\rangle.
\]

Cauchy–Schwarz and convergence of `||z_n||` prove
`|ell_v(z)|<=limsup ||v_n|| ||z||`. Therefore the Riesz representation theorem defines an actual linear map

\[
\boxed{\mathfrak b:B_{\rm lim}\longrightarrow H_{\rm obs},\qquad
\langle z,\mathfrak b(v)\rangle=\ell_v(z),\quad
\|\mathfrak b(v)\|\le\limsup_n\|v_n\|.}
\tag{6.1}
\]

Its kernel is exactly

\[
\mathcal K=\{v:\lim_n\langle z_{i,t,n},v_n\rangle=0
\text{ for every fixed }i,t\}.
\tag{6.2}
\]

The map is onto. To prove this, approximate any `w in H_obs` by finite symbol sums `w_j` with error at most `2^{-j}`. Enumerate the rational-time test symbols. Choose increasing regulator thresholds `N_j` after all births in `w_j` so that, for all later regulators, the squared norm of its regulator counterpart differs from `||w_j||^2` by at most `2^{-j}`, and its first j test pairings differ from the limiting pairings by at most `2^{-j}`. Set `v_n` equal to the counterpart of `w_j` for `N_j<=n<N_{j+1}`, and zero before `N_1`. This sequence is bounded, has every test-pairing limit equal to that of w, and satisfies `||v_n|| -> ||w||`. Hence `mathfrak b(v)=w`.

The exact cochain comparison is

\[
C_0:\quad\mathcal N\hookrightarrow B_{\rm lim}\longrightarrow0,
\qquad C_1:\quad\mathcal K\hookrightarrow B_{\rm lim}\longrightarrow0.
\]

Use inclusion in degree zero and identity in degree one. Then

\[
\boxed{
H^1(C_0)=B_{\rm lim}/\mathcal N,
\quad H^1(C_1)\xrightarrow{\cong}H_{\rm obs},\ [v]\mapsto\mathfrak b(v),
\quad\ker H^1(C_0\to C_1)=\mathcal K/\mathcal N.
}
\tag{6.3}
\]

The inverse is the class of any lift constructed above; two lifts differ by an element of `mathcal K`, which proves independence. The norm bound in (6.1) proves `N subset K`. This is a full typed comparison from regulator sequences, including its retained source relations, rather than an inference from density at each separate regulator.

### 6.1 An exact commuting-observable test of escaping labels

Define a finite test system `Omega_n={-1,1}^n` with its original product probability `2^{-n}`. Let `F_j` flip coordinate j and put

\[
A_n^{\rm test}=\sum_{j=1}^n\frac{c_{j,n}}2(I-F_j),\qquad
c_{j,n}=1\ (j<n),\quad c_{n,n}=1/n.
\tag{6.4}
\]

Constants are the unique vacuum. The ordered refinement map forgets the last coordinate, and its pullback preserves these product inner products. Multiplication by the Walsh functions
`chi_S(omega)=prod_(j in S) omega_j`, for fixed finite nonempty S, is a bounded commuting observable of norm one. The exact identities are

\[
\langle\chi_S,\chi_T\rangle=\delta_{ST},\qquad
A_n^{\rm test}\chi_S=\left(|S\setminus\{n\}|+
\frac{\mathbf1_{n\in S}}n\right)\chi_S.
\tag{6.5}
\]

The character basis spans the full space at each finite n. For every fixed S, its energy equals `|S|` at every `n>max S`; all fixed-label limiting correlations are consequently
`delta_ST exp(-t |S|)`. The reconstructed centered generator has spectral bottom one. The actual regulator states

\[
v_n=\chi_{\{n\}},\quad \|v_n\|=1,\quad
\langle v_n,A_n^{\rm test}v_n\rangle=1/n,
\quad \mathfrak b(v)=0
\tag{6.6}
\]

satisfy the last equality because every fixed-label pairing is eventually zero. Thus their class is an explicitly nonzero element of `mathcal K/N`, with its complete energy sequence retained. Equations (6.4)–(6.6) are algebraic test data; they assign no numerical value to a Yang–Mills gap.

In [SR] §5 replace the sentence beginning “A sequence of low-energy states approaching zero is therefore recorded” by the exact statement: “The spectral-support and large-time formulas determine the reconstructed fixed-label observable sector. The regulator-state comparison has the retained kernel `K/N` constructed in the vacuum-refinement continuation, §6; equation (6.6) computes an escaping-label class together with its norm and energy sequence.” The previous spectral-support and Laplace-principle formulas remain as written.

Two further notation corrections are recorded for [SR]: in §1 use
`||A_n^q exp(-tA_n)||=sup_(lambda in sigma(A_n)) lambda^q exp(-t lambda) <= sup_(lambda>=0) lambda^q exp(-t lambda)`; and in §4 define the matrix imaginary part as `(R(z)-R(z)^*)/(2i)`. The latter retains complex off-diagonal spectral entries in the stated polarization argument.

## 7. Verification and mathematical scope

`verify.py` checks exact rational SU(2) chain and adjoint identities, the raw nonorthogonal Schur formulas and inverse-energy budget on declared finite fixtures, the derivative constants, a conditional-density square calculation, and the full Walsh escaping-label calculation. Its finite fixtures check specified algebraic identities. The measure, domain, smooth-section, and limit statements are proved in the text above; they are not claimed as outputs of those finite tests.

This continuation supplies explicit smooth extensions with an energy cost, an actual vacuum-marginal refinement hierarchy with all cross terms, a projective equal-time limit, uniform infrared memory bounds, and the complete regulator-state comparison kernel. The quantities `rho_n`, the zero-energy inverse-memory matrix `Z_alpha`, and the interacting low-energy state content of `K/N` have not been numerically determined here. A nontrivial four-dimensional continuum Yang–Mills field and a positive physical continuum mass lower bound have not been established by this contribution.


---

# Chapter 6 — 20260915-actual-loop-moments / RESEARCH_NOTE.md

Original text path: `workbench/yang-mills/continuations/20260915-actual-loop-moments/RESEARCH_NOTE.md`.

# Actual Wilson-loop response moments from the full interacting vacuum

15 September 2026. Additive continuation of the SU(2) Yang–Mills workbench,
parent `e98b2c3af77f66fb1c1396143ca53daef586404f` (PR6).

This contribution evaluates response quantities of the original interacting
vacuum with finite errors independent of the exterior box. It proves
all-coupling pointwise logarithmic-derivative and response-moment bounds;
a gauge-covariant inverse estimate with a regulator-independent coefficient
and its full physical kappa dependence; an exact
local SU(2) calculation of three response-moment coefficients; and finite
intervals for the actual response and restored metric. The narrow intervals
are on the explicitly stated small-xi domain. The simultaneous continuum
path remains explicit in section 11. A positive physical continuum gap and a
nontrivial four-dimensional continuum field have not been established here.

The executable checks actual quaternion polynomial identities, local lattice
incidence, Haar integrals, and rational endpoints for the proved error bounds.
It does not numerically solve for the vacuum or formally verify the analytic
proofs. No general historical-priority claim is made.

## 1. Original operator, coordinates, and derivative identities

Use the original open graph with vertices `{-L,...,L}^3`, integer `L>=2`,
all contained positive edges, and every contained elementary face. Physical
spacing `a>0` and coupling `g>0` remain. Write

\[
 T_\alpha=-i\sigma_\alpha/2,\quad
 X_{e,\alpha}f(U)=\left.\frac d{dt}f(\ldots,e^{tT_\alpha}U_e,\ldots)\right|_{0},
 \quad K=-\sum_{e,\alpha}X_{e,\alpha}^2,
\]
\[
 \kappa=\frac{2g^2}{a},\qquad v=\frac1{2g^2a},\qquad
 \xi=\frac v\kappa=\frac1{4g^4},\qquad
 V=v\sum_p(2-W_p),\qquad H=\kappa K+V.                 \tag{A1}
\]
Here `W_p` is the trace of its complete oriented four-link word. The scalar
`2v|P|` is present. The original generator metric has
`c(T_alpha,T_beta)=delta_alpha,beta/4`; thus `Delta^c=4 sum X^2`, exactly as
in the primary source. Every formula below uses the original `X` and `kappa`.

The primary source [YM] proves that the full scalar compact-group operator
has a smooth positive unit ground vector `psi`, unique and gauge invariant,
with ground energy `E0`. Its operator domain is `H^2`, form domain `H^1`;
physical spaces are their gauge-invariant parts. Set

\[
 u=\log\psi,\quad \rho=\psi^2,\quad b_{e,\alpha}=X_{e,\alpha}u,
 \quad \Delta=\sum X^2,\quad
 \mathscr L=\Delta+2\sum b_{e,\alpha}X_{e,\alpha}.
\]
Multiplication `f -> psi f` is a unitary from `L^2(rho dU)` to the original
Haar Hilbert space, with inverse `F -> F/psi`. Direct differentiation gives

\[
 \Delta u+\sum b_{e,\alpha}^2=V/\kappa-E_0/\kappa,
 \qquad \mathcal A:=\psi^{-1}(H-E_0)\psi=-\kappa\mathscr L,
\]
\[
 \langle f,\mathcal A h\rangle_\rho
 =\kappa\int\rho\sum\overline{Xf}Xh.                 \tag{A2}
\]
The displayed energy offset is retained in the first equation; the derivative
of that scalar is zero in the next calculation.

Our fields have bracket
`[X_e,alpha,X_e,beta]=-epsilon_alpha,beta,gamma X_e,gamma`.
This sign follows by differentiating `U -> T_alpha U` twice. The Casimir
commutes with every `X_e,alpha`. Also
`X_e,alpha(sum_i b_i^2)=2 sum_i b_i X_i b_e,alpha`: the commutator correction
is a contraction of an antisymmetric epsilon tensor with `b_i b_j` and is
zero. Differentiating the first equation in A2 consequently proves

\[
 \boxed{\mathscr L b_{e,\alpha}=\kappa^{-1}X_{e,\alpha}V,
 \qquad \mathcal A b_{e,\alpha}=-X_{e,\alpha}V.}       \tag{A3}
\]
This is an equality of the actual smooth functions on the complete graph.
Its components may be gauge covariant; A2 and A3 also hold on the full scalar
space before restriction to the physical subspace.

For a single loop trace `F=tr U_C` in which each edge occurs once, Pauli
multiplication gives, at every link in its word,

\[
 \sum_\alpha|X_{e,\alpha}F|^2=1-F^2/4\le1,
 \quad \|[X_{f,\beta}X_{e,\alpha}F]_{\beta,\alpha}\|_{op}\le\tfrac12,
\]
\[
 \sum_{\alpha,\beta}|X_{f,\beta}X_{e,\alpha}F|^2
 =\tfrac12+F^2/16\le\tfrac34.                        \tag{A4}
\]
The last two formulas concern edges in the word. To verify them, move each
inserted generator to a common end of the word by conjugation, retaining its
orthogonal adjoint matrix. In coordinates `Q=q0 I-i sum q_alpha sigma_alpha`,
`sum q_i^2=1`, one has `tr(T_alpha Q)=-q_alpha` and
`tr(T_alpha T_beta Q)=-(delta_alpha,beta q0+epsilon_alpha,beta,gamma q_gamma)/2`.
For the three by three matrix M in the last trace formula, multiplication
gives `M^T M=(I_3-q_vec q_vec^T)/4`; its positive outer-product deficit
proves the operator bound. Summing its diagonal gives the Frobenius identity.
Inversely traversed links use
`d(U^{-1})=-U^{-1}(dU)U^{-1}` and the same adjoint rotations. No edge is
replaced by an independent inverse variable: the coordinate map `U -> U^{-1}`
is its own Haar-preserving inverse and intertwines the Casimir sum.

## 2. All-coupling pointwise vacuum control

Let `r_e` count the original faces incident on edge e, so `r_e<=4`.
For the three by three matrix `B_beta,alpha=X_e,beta X_e,alpha u`, its
antisymmetric part has squared Frobenius norm

\[
 \sum_{\alpha,\beta}|(B_{\beta\alpha}-B_{\alpha\beta})/2|^2
 =\tfrac12\sum_\alpha|b_{e,\alpha}|^2.
\]
Therefore `sum_(i,alpha)|X_i b_e,alpha|^2 >= |b_e|^2/2` pointwise.
At a maximum of `w_e=sum_alpha b_e,alpha^2` on the compact product group,
A3 and the product rule imply

\[
 0\ge\tfrac12\mathscr L w_e
 =\sum_{i,\alpha}|X_i b_{e,\alpha}|^2
  +\kappa^{-1}\sum_\alpha b_{e,\alpha}X_{e,\alpha}V
 \ge\tfrac12 w_e-r_e\xi\sqrt{w_e}.
\]
We used `|X_e V|<=v r_e`, proved from A4. The quadratic inequality at the
maximum proves

\[
 \boxed{\sup_U|X_e\log\psi|\le2r_e\xi\le8\xi,
 \qquad \sup_U|X_e\log\rho|\le4r_e\xi\le16\xi.}     \tag{A5}
\]
There is no exterior-volume constant, and A5 holds at every positive coupling.

Integrating A3 against `rho b_e,alpha`, followed by Haar integration by parts,
also gives an exact differentiated-vacuum sum rule:

\[
 \boxed{\int\rho\sum_{i,\alpha}|X_i b_{e,\alpha}|^2
 =\frac1{2\kappa}\langle\Delta_e V\rangle_\rho
 =\frac{3\xi}{8}\left\langle\sum_{p\ni e}W_p\right\rangle_\rho
 \le\frac{3r_e\xi}{4}.}                              \tag{A6}
\]
All derivative indices i in A6 range over the full graph. The identity uses
`Delta_e W_p=-3W_p/4`. The primary local exterior-operator comparison further
supplies

\[
 \gamma_e:=\int\rho|b_e|^2\le2r_e\xi\le8\xi.         \tag{A7}
\]
For completeness, write
`H-E0=kappa E_e+K_e-v sum_(p containing e) W_p`, where `K_e>=0` acts on
exterior links. This follows by testing H on the constant in e times an
exterior ground vector; each incident trace has zero Haar integral in e.
Taking the vacuum expectation gives A7. Every exterior term stays in K_e.

## 3. A gauge-covariant inverse and a quantitative local drift expansion

### 3.1 The inverse is proved on its exact source sector

At vertex v let `G_v,alpha` be the infinitesimal vertex gauge action. It is
the sum of outgoing left generators and incoming negative right generators.
Right generators are related to the displayed left generators by the actual
adjoint matrices of their links. If `d_v` is the vertex degree, pointwise
Cauchy–Schwarz gives

\[
 \sum_\alpha|G_{v,\alpha}h|^2
 \le d_v\sum_{e\ni v,\alpha}|X_{e,\alpha}h|^2,
 \qquad d_v\le6.                                    \tag{A8}
\]
The difference of the two sides of the vector inequality
`d_v sum|z_e|^2-|sum z_e|^2` is exactly `sum_(e<f)|z_e-z_f|^2`.

Use the spin-one gauge-Casimir subspace
`E_v={h: -sum_alpha G_v,alpha^2 h=2h}`, with its closed Hilbert realization
from the compact unitary gauge action on `L^2(rho dU)`. Haar averaging in the
vertex gauge variable supplies this closed sector; equivalently it is the
range of `3 int chi_1(g) U_v(g) dg`, where
`chi_1(g)=(tr g)^2-1`. Matrix-coefficient orthogonality proves the projection
formula. The original H and rho commute with this action, so A reduces E_v.
Integration by parts in the gauge variable and A8 give

\[
 q_{\mathcal A}(h)\ge\frac{2\kappa}{d_v}\|h\|_\rho^2
 \ge\frac\kappa3\|h\|_\rho^2\quad(h\in E_v),
\]
\[
 \boxed{\| (\mathcal A|_{E_v}+s)^{-1}\|
 \le\frac1{s+2\kappa/d_v}\le\frac1{s+\kappa/3},
 \qquad s\ge0.}                                      \tag{A9}
\]
The form inequality extends from smooth vectors by closure. Self-adjointness
then gives the inverse on exactly this sector.

For an edge e starting at v, the vector `b_e` transforms by the adjoint
three-dimensional representation at v. Indeed `G_v u=0`, and commuting G_v
with X_e gives `G_v,alpha b_e,beta=-epsilon_alpha,beta,gamma b_e,gamma`.
The other vertex gauge generators commute with this derivative. Thus each
component of b_e is in E_v; contracting twice with epsilon gives its Casimir
2. This proves that A9 applies to the actual derivative in A3.

The physical contraction in a Wilson-loop forcing is the map
`(h_alpha,c_alpha) -> sum_alpha h_alpha c_alpha`. Both factors transform
by the same orthogonal adjoint matrix at the edge source, so this product
is invariant there. Its derivative is the full product rule
`X_i sum h_alpha c_alpha=sum [(X_i h_alpha)c_alpha+h_alpha(X_i c_alpha)]`.
The cross terms in its energy are retained below. A9 is used on its specified
covariant sources through this map, rather than assigned to the invariant
contraction without its energy calculation.

### 3.2 First local drift and its remainder

Set

\[
 u_0=\frac\xi3\sum_p W_p,\qquad b_e^0=X_eu_0,
 \qquad \mathfrak r_e=X_e(u-u_0).                              \tag{A10}
\]
The scalar E0 is still in A2. The derivative formula here follows because
`Delta u0=-xi sum_p W_p`, so `Delta b_e^0=kappa^{-1}X_e V`.
Consequently

\[
 \mathscr L \mathfrak r_{e,\alpha}
 =-2\sum_i b_i X_i b^0_{e,\alpha}.                   \tag{A11}
\]
Each block `J^0_ef=[X_f,beta b^0_e,alpha]` satisfies, by A4,

\[
 \sum_f\|J^0_{ef}\|_{op}\le\frac{2r_e\xi}{3}\le\frac{8\xi}{3},
 \quad |b_e^0|\le\frac{4\xi}{3},
 \quad |\mathcal A \mathfrak r_e|\le\frac{128\kappa\xi^2}{3}.  \tag{A12}
\]
In the first sum only edges sharing a plaquette with e occur. Each such
plaquette has four original edges and contributes at most `xi/(3*2)` per
block; multiplicities are counted.

The residual vectors in A10 have the same spin-one covariance as b_e.
A9 and A12 give,
at **every** xi>0,

\[
 \boxed{\|\mathfrak r_e\|_{L^2(\rho;\mathbb R^3)}\le128\xi^2,
 \qquad \sum_\alpha\|\nabla \mathfrak r_{e,\alpha}\|_\rho^2
 \le\frac{16384}{3}\xi^4.}                          \tag{A13}
\]
The second inequality is A2 paired with the residual vector and A12, using the first.

On the stated range `0<xi<=3/64`, the pointwise constant is sharper. Take a
maximum over all edges and configurations of `|r_e^rem|=R`. The antisymmetric
second-derivative calculation in section 2 applies to `X_e(u-u0)` too.
At that maximum A11 and A12 give

\[
 (\tfrac12-\tfrac{16\xi}{3})R^2
 \le\tfrac{64\xi^2}{9}R.
\]
The coefficient on the left is at least 1/4. Hence, putting `A_*=256/9`,

\[
 \boxed{|\mathfrak r_e|\le A_*\xi^2,\quad
 \sum_\alpha\|\nabla \mathfrak r_{e,\alpha}\|_\rho^2
 \le\frac{128A_*}{3}\xi^4,
 \quad \|\mathcal A \mathfrak r_e\|_\infty\le\frac{128\kappa}{3}\xi^2.} \tag{A14}
\]
The middle inequality follows by pairing A11 with the residual vector and using the row
bound and A5; it sums derivatives over every fine link. This is a proved
remainder bound on the full interacting vacuum, not a formal series premise.

## 4. The loop observation and its exact relation to the earlier refinement

Let C be an axis-aligned square of side b lattice edges in the x1,x2 plane,
with a one-plaquette collar inside the box. Set `ell=4b`, and let
`Omega=U_C` be its ordered group holonomy, including every inverse traversal.
For b=1 one may take the face with base (0,0,0), directions (1,2); L>=2
contains its collar. Denote `F=tr Omega`.

In oriented link variables V_j along C, the map

\[
 (V_1,\ldots,V_\ell,U_{C^c})
 \mapsto(\Omega=V_1\cdots V_\ell,V_1,\ldots,V_{\ell-1},U_{C^c}) \tag{A15}
\]
has inverse `V_ell=(V_1...V_(ell-1))^{-1}Omega`. Product Haar is exactly
`dOmega dz`, by translation in the last link. Inverse traversals are carried
by the explicit involution in A4. Let

\[
 m(\Omega)=\int\rho(\Omega,z)dz,\quad
 \mathsf Eh=m^{-1}\int\rho h\,dz,\quad
 \mathsf Jf=f(\Omega),\quad P=\mathsf J\mathsf E,\quad Q=I-P. \tag{A16}
\]
Fubini gives `EJ=I`, `E=J*` in the actual rho and m pairings. These maps
intertwine the original gauge action with conjugation at the loop base.
Their physical subspaces therefore use the actual conjugation-invariant
functions on the observed SU(2) variable.

For the earlier full coarse-edge observation pi_all, a square born on that
coarse grid has `pi_C=chi_C pi_all`, where chi_C is the same four-coarse-edge
word. On the same fine vacuum the conditional expectations obey
`E_C=E_chi E_all`, by testing both sides against functions of Omega. Hence
`P_C<=P_all`. Their kernel comparison is the actual isomorphism

\[
 \ker E_C/\ker E_{all}\longrightarrow\ker E_\chi,
 \quad[h]\mapsto E_{all}h,
 \qquad k\mapsto[J_{all}k].                           \tag{A17}
\]
Both compositions follow from `E_all J_all=I` and
`h-J_all E_all h in ker E_all`. In particular the new observation retains
the additional coarse kernel in A17. Its forcing decomposes orthogonally as
`-Q_C A F=-Q_all A F-(P_all-P_C)A F`. Thus its zeroth forcing norm is the
sum of the two original squared norms. Higher energy entries use the full
coupled form, as in the parent's minimum-section composition. They are not
silently assigned to the old, smaller kernel.

The original horizontal fields now average all ell original links:
`Y_alpha=ell^{-1}sum_(j,beta)(Ad prefix_(j-1))_(alpha,beta)X_(j,beta)`.
They satisfy `Y_alpha J=J X_alpha` and
`sum_alpha|Y_alpha h|^2<=ell^{-1}sum_(j,beta)|X_(j,beta)h|^2`.
Each coefficient is independent of its differentiated link, giving Haar
divergence zero. Set

\[
 S_\alpha=Y_\alpha\log\rho-\mathsf J X_\alpha\log m,
 \quad (Th)_\alpha=\mathsf E(hS_\alpha),
 \quad \Gamma_{\alpha\beta}=\mathsf E(S_\alpha S_\beta).
\]
Integration by parts gives `ES=0`, `X Eh=E(Yh)+E(hS)` and
`T* z=sum S_alpha J z_alpha`. A5 gives `|Y log rho|<=16xi`, and thus

\[
 \boxed{\Gamma\preceq256\xi^2 I_3,\quad
 \|T\|\le16\xi,\quad
 \|X\mathsf Eh\|_m\le\ell^{-1/2}\|\nabla h\|_\rho+16\xi\|h\|_\rho.} \tag{A18}
\]
For Gamma the exact covariance is
`E[(Y log rho)(Y log rho)^T]-(E Y log rho)(E Y log rho)^T`.
The second term is retained in the equality and bounded by positivity.

Let D represent the restriction of the form A2 to `H^1_phys intersect ker E`.
At each finite regulator, E and J preserve H^1 by A18 and their finite smooth
coordinate formulas. Smooth kernel functions are dense, the restricted form
is closed, and D is nonnegative self-adjoint. On smooth physical kernel
functions `Dh=Q A h`. These facts also follow by the parent's same closed-form
argument after A15. All functions below are smooth, so every used power of D
has its stated domain. The off-diagonal action is

\[
 Q\mathcal A\mathsf Jg=-\kappa\ell T^*Xg.             \tag{A19}
\]
It follows by pairing A2 against a kernel function and using A18.

Define the ACTUAL scalar forcing and its three moments by

\[
 j=\sum_{e\in C,\alpha}b_{e,\alpha}X_{e,\alpha}F,
 \quad W=2\kappa Qj=-Q\mathcal AF,
\]
\[
 \boxed{N_0=\|W\|_\rho^2,\quad
 N_1=\langle W,DW\rangle_\rho,\quad N_2=\|DW\|_\rho^2.} \tag{A20}
\]
Indeed `KF=(3ell/4)F`, so the Casimir term is killed by Q and A20 follows
from A2. The actual response is `M(s)=<W,(D+s)^{-1}W>_rho`.

## 5. Actual moment bounds at every positive coupling

Set

\[
 J_\ell(\xi)=\min(8\ell\xi,\sqrt8\,\ell\sqrt\xi),
\]
\[
 \begin{split}
 P_\ell(\xi)={}&3\ell^{3/2}\sqrt\xi+(4\ell+6\ell^2)\xi
 +16\sqrt3\ell^{3/2}\xi^{3/2}\\
 &+128\sqrt3\ell^2\xi^2+2048\ell^2\xi^3.
 \end{split}
\]
Then the original interacting moments satisfy

\[
 \boxed{0\le N_0\le4\kappa^2J_\ell(\xi)^2,\quad
 0\le N_1\le4\kappa^3J_\ell(\xi)P_\ell(\xi),\quad
 0\le N_2\le4\kappa^4P_\ell(\xi)^2.}                \tag{A21}
\]
Here ell, kappa, and xi retain their values; the exterior box is arbitrary.

Proof: A4, A5 and A7 give `||j||<=J_ell`. For `c_e,alpha=X_e,alpha F`,
A4 gives `||c||_infty<=sqrt(ell)` and
`||grad c||_infty,HS<=sqrt(3)ell/2`. A6, summed over e in C, gives
`sum_(e,alpha)||grad b_e,alpha||^2<=3ell xi`. The product rule therefore gives

\[
 \|\nabla j\|_\rho\le\sqrt3\ell\sqrt\xi
                      +4\sqrt3\ell^{3/2}\xi.          \tag{A22}
\]
A3 and `Kc=(3ell/4)c` give, keeping all three product-rule terms,

\[
 \mathcal A j=\sum c_i\mathcal A b_i
              +\sum b_i\mathcal A c_i
              -2\kappa\sum_{i,k}(X_kb_i)(X_kc_i),
\]
\[
 \|\mathcal Aj\|_\rho
 \le\kappa\{(4\ell+6\ell^2)\xi
       +64\sqrt3\ell^2\xi^2+3\ell^{3/2}\sqrt\xi\}.   \tag{A23}
\]
The respective bounds use `|X_e V|<=4kappa xi`, A5, and A6. A18 and A22 give
`||X E j||<=sqrt(3ell)sqrt(xi)+4sqrt(3)ell xi+128ell xi^2`.
Finally A19 gives
`DW=2kappa[Q A j+kappa ell T* X E j]`. Substitution proves
`||DW||<=2kappa^2 P_ell`, and Cauchy–Schwarz proves all three inequalities
in A21. No pointwise-to-integrated replacement is used.

## 6. Local density comparison, including the conditional fiber

Let S be any finite edge set containing C and the local polynomials under
consideration; write d=|S|. A5 and the original group diameter `2pi` in the
X-generator coordinates show that changing S while fixing its exterior
changes `log rho` by at most `32pi d xi`. After integrating the exterior,
the exact Haar marginal density rho_S consequently satisfies

\[
 e^{-32\pi d\xi}\le\rho_S\le e^{32\pi d\xi}.          \tag{A24}
\]
To prove the bounds from the oscillation, note that its Haar integral is one:
its minimum is at most one, its maximum at least one, and their ratio is
at most the displayed exponential. This uses the existing Haar probability
mass, without changing the physical state.

At fixed Omega in A15, varying a first-chain link also changes the final
chain link by left and right translations. Each such pair has total path
length at most `4pi`; every other S link has path length at most `2pi`.
Thus the conditional local density relative to its original Haar fiber has
ratio bounded by `exp(32pi(d+ell-2)xi)`. Put

\[
 \delta=e^{32\pi d\xi}-1,\qquad
 \eta=e^{32\pi(d+\ell-2)\xi}-1.                     \tag{A25}
\]
For a local polynomial P whose conditional Haar average E_H P is zero,

\[
 \|\mathsf EP\|_\infty\le\eta\|P\|_\infty,
 \quad
 \|X\mathsf EP\|_m
 \le\eta\ell^{-1/2}\|\nabla P\|_\infty+16\xi\|P\|_\infty. \tag{A26}
\]
For the second formula `E_H YP=X E_H P=0` follows from A18 with constant
density; apply the conditional density comparison to YP, then A18 to the
score term. For arbitrary local P,Q, A24 also gives
`|<P,Q>_rho-<P,Q>_H|<=delta ||P||_H ||Q||_H`.

## 7. Exact original neighboring-plaquette calculation

Let p range over elementary faces meeting C, excluding p=C when b=1. Define

\[
 J_p=\sum_{e\in C\cap\partial p,\alpha}(X_{e,\alpha}W_p)(X_{e,\alpha}F),
 \quad J=\sum_pJ_p,\quad s_p=|C\cap\partial p|.        \tag{A27}
\]
For b=1 there are twelve faces, all s_p=1. Four are coplanar with bases
`(-1,0,0),(1,0,0),(0,-1,0),(0,1,0)` and directions (1,2); four have directions
(1,3) with x1=0, x2 in {0,1}, x3 in {-1,0}; four have directions (2,3) with
x1 in {0,1}, x2=0, x3 in {-1,0}. Their union with C has 12 direction-1,
12 direction-2 and 8 direction-3 edges: d=32.
For b>=2 the four inner corner faces have s_p=2 and every other meeting face
has s_p=1. Counting four incidences per C edge gives `4ell-8` faces of type
1 and four of type 2. These statements use the actual contained face words.
An exterior-independent support bound is `d<=13ell`. Here is also the exact
count. Vertical edges have their horizontal coordinates on the square's ell
vertices and their z base in {-1,0}, giving 2ell edges. Direction-1 edges at
z=+1 or -1 lie on the two horizontal sides, giving 4b edges in total. At z=0
their (x,y) bases form the union

    {0,...,b-1} x {-1,0,1,b-1,b,b+1}
      union {-1,0,b-1,b} x {0,...,b}.

For b>=3 its count is 6b+4(b+1)-8=10b-4. At b=2 its count is
10+12-6=16, the same formula. At b=1 it is 4+6-2=8.
Direction-2 edges have the transposed count. Hence d=32 at b=1 and
`d=2(14b-4)+8b=36b-8=9ell-8` at every b>=2. All these edge sets
come from the displayed original adjacent faces; the weaker bound suffices
for the general error estimates.

Each overlap is a connected path. Orient p to traverse this common path in
the same direction as C; `tr U_p^{-1}=tr U_p` proves equality of the original
trace functions under that operation. Let U be the common path product, A
and B the two remaining products, so `F=tr(UA)`, `W_p=tr(UB)`. The product
Haar pushforward to U,A,B is independent Haar, proved by repeated translations
in disjoint link sets. Every shared-edge contraction equals

\[
 j_p=\sum_\alpha\operatorname{tr}(T_\alpha UA)
                         \operatorname{tr}(T_\alpha UB)
 =-\tfrac14\operatorname{tr}(UAUB)+\tfrac14\operatorname{tr}(AB^{-1}),
 \qquad J_p=s_pj_p.                                  \tag{A28}
\]
The equality follows from Pauli multiplication (Fierz) and
`tr X tr Y=tr(XY)+tr(XY^{-1})`, verified in the same quaternion coordinates.
Integration of U yields

\[
 j_p^{(0)}=\tfrac38\operatorname{tr}(AB^{-1}),\quad
 j_p^{(1)}=j_p-j_p^{(0)},\quad
 \|j_p^{(0)}\|_H^2=\tfrac9{64},\quad
 \|j_p^{(1)}\|_H^2=\tfrac3{64},\quad
 \langle j_p^{(0)},j_p^{(1)}\rangle_H=0.              \tag{A29}
\]
For a direct check, `int tr(UAUB)dU=-tr(AB^{-1})/2`. Integrating B in
`j_p^2` first gives `(1/4)sum_alpha|X_alpha tr(UA)|^2`, whose mean is 3/16.
The first norm in A29 is `9/64` because the remaining trace has Haar square
mean one; subtracting it from 3/16 gives the second.

Every unshared edge occurs once in a fundamental representation, contributing
3/4 to K. The shared U-singlet has Casimir zero and the shared triplet has
Casimir 2 on each of its s_p original links. Equivalently direct Pauli
second differentiation gives K_U j_p^(0)=0 and K_U j_p^(1)=2j_p^(1), and
ordered product pullback supplies the factor s_p. Thus, with

\[
 \nu_p=\tfrac34(\ell+4-2s_p),
 \qquad Kj_p^{(0)}=\nu_pj_p^{(0)},\quad
 Kj_p^{(1)}=(\nu_p+2s_p)j_p^{(1)}.                   \tag{A30}
\]
For distinct p,q there is an edge in `partial p \ (C union partial q)`:
p has at least two exterior edges and distinct elementary faces share at
most one edge. Central sign change at that edge makes every cross product
between their components and their K iterates integrate to zero. This proves
all cross-face Haar cancellations with their actual unmatched-edge witnesses.

Also `E_H J=E_H KJ=0`, by integration in an exterior edge of each face.
A4 and the product rule give the following local suprema, with
`S1=sum_p s_p`, `S2=sum_p s_p^2`:

\[
 \|J\|_\infty\le S_1,\quad
 \sum_e\|X_eJ\|_\infty\le L_J:=\tfrac{\ell+4}{2}S_1,
 \quad \|KJ\|_\infty\le K_J:=(3+3\ell/4)S_1+\tfrac32S_2. \tag{A31}
\]
For the last inequality, apply K to each original product in A27. The two
Casimirs give `(3+3ell/4)J_p`; the mixed second derivatives are at most
`2*(3/4)s_p^2` by A4. For the first derivative, each pair of shared-edge
factors contributes at most 1/2 at each of its four plus ell differentiated
edges. For b=1, `(S1,S2,LJ,KJ)=(12,12,48,90)`.

Define w and z1 (the latter is an energy vector, not a spectral parameter) by

\[
 w=\tfrac{2\kappa\xi}{3}J,\qquad
 z_1=\tfrac{2\kappa^2\xi}{3}KJ.
\]
Equations A29–30 prove the exact coefficients

\[
 \|w\|_H^2=\kappa^2\xi^2 c_0,\quad
 \langle w,z_1\rangle_H=\kappa^3\xi^2 c_1,\quad
 \|z_1\|_H^2=\kappa^4\xi^2 c_2,
\]
\[
 c_j=\sum_p\frac{s_p^2}{48}
            \{3\nu_p^j+(\nu_p+2s_p)^j\},\quad j=0,1,2. \tag{A32}
\]
For an elementary loop these are `(1,5,103/4)`. For b>=2 they are

\[
 \boxed{c_0=\frac{\ell+2}{3},\quad
 c_1=\frac{\ell(3\ell+14)}{12},\quad
 c_2=\frac{9\ell^3+66\ell^2+76\ell+104}{48}.}        \tag{A33}
\]
These coefficients have now been evaluated; the return to the interacting
vacuum and its conditional D is the next, quantitative step.

## 8. Full finite remainders for the interacting moments

Use `0<xi<=3/64` and `A_*=256/9`. Write
`d_j=sum_(e in C,alpha)r^rem_e,alpha X_e,alpha F`. Then

\[
 j=\frac\xi3 J+d_j+\frac\xi3(4-F^2)\,\mathbf1_{b=1},
 \quad \|d_j\|_\rho\le\ell A_*\xi^2.               \tag{A34}
\]
The last term is an actual function of Omega and is killed exactly by Q.
Let `t=(xi/3)J+d_j`, so `W=2kappa Qt`.

For complete finite constants put

\[
 B_d=\ell\sqrt{128A_*/3}+\frac{\sqrt3}{2}\ell^{3/2}A_*,
\]
\[
 C_d(\xi)=\frac{128\ell}{3}+\frac{3\ell^2A_*}{4}
              +8\sqrt3\ell^2A_*\xi
              +\sqrt{128}\ell^{3/2}\sqrt{A_*}.
\]
A4 and A14, applied to the full product rule, give

\[
 \|\nabla d_j\|_\rho\le B_d\xi^2,
 \qquad \|\mathcal A d_j\|_\rho\le\kappa C_d(\xi)\xi^2. \tag{A35}
\]
For explicit verification, the derivative terms are bounded by
`ell sqrt(128A_*/3)xi^2` and `(sqrt(3)/2)ell^(3/2)A_*xi^2`.
In A d_j the terms `c A r`, `r kappa(3ell/4)c`,
`-2kappa r b grad c`, and `-2kappa grad r grad c` have respective bounds
`128ell/3`, `3ell^2 A_*/4`, `8sqrt(3)ell^2 A_*xi`, and
`sqrt(128)ell^(3/2)sqrt(A_*)`, all multiplied by `kappa xi^2`.

Define

\[
 H_t=\frac\xi3\{\eta L_J/\sqrt\ell+16\xi S_1\}
              +B_d\xi^2/\sqrt\ell+16\ell A_*\xi^3,
\]
\[
 e_0=2\{\ell A_*\xi^2+(\xi/3)\eta S_1\},
\]
\[
 e_1=2\{(\xi/3)\eta K_J+(16\xi^2/3)L_J
                   +C_d(\xi)\xi^2+16\ell\xi H_t\}.    \tag{A36}
\]
A26 and A35 give `||X E t||<=H_t`. The identities

\[
 W-w=2\kappa Qd_j-\tfrac{2\kappa\xi}{3}PJ,
 \quad
 DW=2\kappa\{Q\mathcal At+\kappa\ell T^*X\mathsf Et\}
\]
now give

\[
 \boxed{\|W-w\|_\rho\le\kappa e_0,\qquad
 \|DW-z_1\|_\rho\le\kappa^2 e_1.}                  \tag{A37}
\]
For the second identity the unprojected leading term is `(kappa xi/3)KJ`;
its projection error is bounded by `(kappa xi/3)eta KJ`. Its drift error is
bounded by `(16kappa xi^2/3)LJ`, using A5. A35 bounds the remainder and
A18 bounds the final conditional coupling. These are precisely all four
terms in e1.

Here are explicit error radii epsilon_j (distinct from the ground energy E_0),
solely as coefficient functions retaining
the full original kappa and xi factors:

\[
 \epsilon_0=\delta c_0+2\sqrt{(1+\delta)c_0}\,e_0/\xi+(e_0/\xi)^2,
\]
\[
 \epsilon_1=\delta\sqrt{c_0c_2}+\sqrt{(1+\delta)c_0}\,e_1/\xi
       +\sqrt{(1+\delta)c_2}\,e_0/\xi+e_0e_1/\xi^2,
\]
\[
 \epsilon_2=\delta c_2+2\sqrt{(1+\delta)c_2}\,e_1/\xi+(e_1/\xi)^2.
\]
A24, A32, A37 and expansion of each inner product prove

\[
 \boxed{|N_j-\kappa^{j+2}\xi^2c_j|
          \le\kappa^{j+2}\xi^2\epsilon_j,\qquad j=0,1,2.}     \tag{A38}
\]
For fixed loop, all displayed epsilon_j tend to zero with xi, uniformly over every
exterior box containing the collar. The complete finite formulas, rather
than just this asymptotic statement, determine the actual certificate below.

## 9. The actual response and restored metric are also enclosed

Specialize only the loop to the elementary face; retain arbitrary L>=2 and
a>0. Let `J0=sum_p j_p^(0)`, `J1=sum_p j_p^(1)`, so `J=J0+J1`. At the actual
positive shift `s=kappa`, use the explicit LOCAL polynomial

\[
 Z=\frac4{33}J_0+\frac4{45}J_1
   =\frac4{45}J+\frac{16}{495}J_0,
 \quad z=\xi Z,\quad Y=Qz.                           \tag{A39}
\]
A30 gives `(K+1)Z=(2/3)J=:U`, and the twelve exact Haar contributions give

\[
 \langle U,Z\rangle_H=m_*:=\frac{28}{165},\qquad
 \|Z\|_H^2=z_*:=\frac{796}{27225}.                    \tag{A40}
\]
Each fused trace in J0 has six original edges. Thus
`||J0||_infty<=9`, `sum_e||X_eJ0||_infty<=27`, and A31 gives

\[
 \|U\|_\infty\le8,\quad \|Z\|_\infty\le Z_*:=\frac{224}{165},
 \quad \sum_e\|X_eZ\|_\infty\le L_*:=\frac{848}{165}. \tag{A41}
\]
Both `E_H Z` and `E_H Y_alpha Z` are zero. Put

\[
 h_z=\xi\{\eta L_*/2+16\xi Z_*\},\quad
 r_z=8A_*\xi^2+16\xi^2L_*+64\xi h_z,\quad
 n_z=\sqrt{(1+\delta)z_*}.                            \tag{A42}
\]
Then `||X E z||<=h_z`, `||Pz||<=xi eta Z_*`, and `||Y||<=xi n_z`.
The ORIGINAL response residual is

\[
 R=W-(D+\kappa)Y
   =2\kappa Qd_j+2\kappa\xi Q\sum_i b_iX_iZ
                  -\kappa\ell T^*X\mathsf Ez,
 \quad \|R\|_\rho\le\kappa r_z.                    \tag{A43}
\]
All three terms are retained. In particular no inverse of D at zero is used.

The parent residual identity, proved again by expanding the square, is

\[
 M(\kappa)=2\langle W,Y\rangle_\rho-q_{\mathcal A+\kappa}(Y)
             +\langle R,(D+\kappa)^{-1}R\rangle_\rho. \tag{A44}
\]
Define the following seven nonnegative terms:

\[
\begin{array}{ll}
 a_1=\delta\xi^2\sqrt{z_*}, &a_2=16\xi^3 Z_*L_*,\\
 a_3=16\xi^2\eta^2 Z_*, &a_4=16A_*\xi^3 n_z,\\
 a_5=4h_z^2+(\xi\eta Z_*)^2,
 &a_6=128\xi^2 n_z h_z,\\
 a_7=r_z^2.&
\end{array}
\]
Set `E_M=(sum a_i)/xi^2` and

\[
 E_Z=\delta z_*+(\eta Z_*)^2+2n_zr_z/\xi+(r_z/\xi)^2.
\]
Then

\[
 \boxed{|M(\kappa)-\kappa\xi^2m_*|\le\kappa\xi^2E_M,
 \quad |\|(D+\kappa)^{-1}W\|_\rho^2-\xi^2z_*|
                                      \le\xi^2E_Z.} \tag{A45}
\]
Here is the full expansion proving the first estimate. Writing p=Pz, A44's
first two terms equal

\[
 2\langle w,z\rangle-q_{\mathcal A+\kappa}(z)
 -2\langle Pw,p\rangle+4\kappa\langle d_j,Y\rangle
 +q_{\mathcal A+\kappa}(p)+2q_{\mathcal A}(Y,p).
\]
Weighted integration by parts and `(K+1)Z=U` turn the first pair into
`kappa xi^2 <U,Z>_rho+2kappa xi^2 int rho Z sum_i b_i X_iZ`.
A24 and A40 bound its first error by kappa a1. A5 and A41 bound its drift
term by kappa a2. Conditional comparison bounds the removed projection
by kappa a3. A14 bounds the d_j term by kappa a4. A18 bounds the coarse
energy by kappa a5 and the mixed energy by kappa a6. Finally the positive
residual term in A44 is at most `||R||^2/kappa<=kappa a7`.
For the second estimate, `||Y||^2=||z||^2-||Pz||^2` and
`||(D+kappa)^{-1}W-Y||<=r_z`; expand the squared norm and apply A24 and A42.

These are direct enclosures of the interacting response and restored metric,
using a specified original Wilson-polynomial trial, not a fit to vacuum data.
The exact section correction in the Split Zero application is as follows.
In the parent's complex `V_j --(D+kappa)--> ker E`, take the actual
one-dimensional source `V_1=span{Y}`. Its forcing representative is R and
its remaining primitive is `(D+kappa)^{-1}R`. Define

\[
 a_Y=q_{\mathcal A+\kappa}(Y),\quad c_Y=\langle Y,W\rangle_\rho,
 \quad \alpha_Y=c_Y/a_Y,\quad
 R_{\rm can}=W-(D+\kappa)(\alpha_Y Y).
\]
The number a_Y is strictly positive. Indeed the Haar-mean-zero local
polynomial z has positive Haar norm A40, so it is not a function of Omega:
applying E_H to such a function would fix it and hence force z=0.
The actual density rho is everywhere positive, so the same equality of
functions cannot hold in L2(rho). Thus Y=Qz is nonzero and
`a_Y>=kappa ||Y||^2>0`.

In the original pairing `\langle h,k\rangle_{dual}=
\langle h,(D+\kappa)^{-1}k\rangle_\rho`, direct multiplication gives
`\langle (D+\kappa)Y,R_can\rangle_dual=0`. Therefore R_can is the
minimum-norm representative of [W], and the complete identities are

\[
 \boxed{\begin{aligned}
 \|[W]\|_{\mathcal K/(D+\kappa)V_1,dual}^2
     &=M(\kappa)-|c_Y|^2/a_Y,\\
 R&=R_{\rm can}+(\alpha_Y-1)(D+\kappa)Y,\\
 \langle R,(D+\kappa)^{-1}R\rangle_\rho
     &=\|[W]\|_{\mathcal K/(D+\kappa)V_1,dual}^2
                         +a_Y|\alpha_Y-1|^2.
 \end{aligned}}                                                   \tag{A45a}
\]
The cross term is zero by the just-proved orthogonality. The correction has
its original primitive `(alpha_Y-1)Y`; neither this vector nor its energy is
dropped. Both nonnegative terms in A45a are at most `kappa r_z^2` by A43–44.
This is the precise map between the chosen trial residual and the canonical
cohomological residual. It bounds the original quotient class on an actual
Yang–Mills source while retaining the section correction.

## 10. Finite evaluated certificate and the raw state metric

Take the exact value `xi=1/100000000`, equivalently `g^2=5000`, while keeping
`a>0` arbitrary, hence `kappa=10000/a`. These conditions are within A14's
proved domain. Evaluate A25–45 with `ell=4`, `d=32`. The standard-library
checker obtains rigorous rational upper endpoints, giving for every L>=2

\[
 \boxed{\begin{aligned}
 0.9994\,\kappa^2\xi^2&<N_0<1.0006\,\kappa^2\xi^2,\\
 4.9963\,\kappa^3\xi^2&<N_1<5.0037\,\kappa^3\xi^2,\\
 25.728\,\kappa^4\xi^2&<N_2<25.772\,\kappa^4\xi^2,
 \end{aligned}}                                                   \tag{A46}
\]
\[
 \boxed{\left|M(\kappa)-\frac{28}{165}\kappa\xi^2\right|
                  <0.0000075\,\kappa\xi^2,\qquad
 \left|\|(D+\kappa)^{-1}W\|_\rho^2-\frac{796}{27225}\xi^2\right|
                  <0.0000021\,\xi^2.}                            \tag{A47}
\]
No finite-volume vacuum integral was numerically substituted: these are
bounds for the actual vacuum, proved using A5–45, with exact arithmetic
for the final constants. The sharpness of the constants is not claimed.

The original centered state has raw Gram `G=<F^2>-<F>^2` and kinetic entry
`K0=kappa(4-<F^2>)`. Their control also improves to order xi^2. The exact
weighted identities, obtained by integrating K F=3F and
K(F^2)=8(F^2-1), are

\[
 3\langle F\rangle=2\langle j\rangle,\qquad
 \langle F^2\rangle-1=\tfrac12\langle Fj\rangle.      \tag{A48}
\]
Let `delta_C=exp(128pi xi)-1` and define

\[
 B_2=\xi\delta/4+(\sqrt5\xi/6)\delta_C+4A_*\xi^2,
 \quad e_\mu=(2\xi/9)(B_2+3\delta/2)+(8A_*/3)\xi^2.
\]
A34, A48 and the exact Haar moments
`<F^2>_H=1,<F^4>_H=2,<F^6>_H=5` give

\[
 |\langle F^2\rangle-1|\le B_2,\quad
 |\langle F\rangle-2\xi/3|\le e_\mu,\quad
 |G-1|\le B_2+(2\xi/3+e_\mu)^2,\quad |K_0-3\kappa|\le\kappa B_2. \tag{A49}
\]
For verification of B2, the Haar means of FJ and F(4-F^2) vanish;
`||F||_H||J||_H=3/2` and `||F(4-F^2)||_H=sqrt(5)`. Their expectation
errors are at most `3delta/2` and `sqrt(5)delta_C`, respectively, and
`|<F d_j>|<=8A_*xi^2`. Substitute into A48. The mean estimate follows
by retaining `<J>`, `4-<F^2>`, and `<d_j>` in its first equation.
At A46's exact coupling both Gram and kinetic relative radii are below
`11/10^14`. The restored lift Gram is the actual sum
`G+||(D+kappa)^{-1}W||^2`; G is retained rather than reset to one.

There is also a direct return to the original physical energy. Put
`h_kappa=(D+kappa)^{-1}W`, `f=F-<F>`, and
`Phi=psi(J f+h_kappa)`. Its mean is zero since `E h_kappa=0`, so
`Phi` is in the original physical space and perpendicular to psi. It is
nonzero since G>0. The original excitation form is used on its H1 domain.
The exact norm and form energy are

\[
 \|\Phi\|^2=G+\|h_\kappa\|_\rho^2,\qquad
 q_{H-E_0}(\Phi,\Phi)
       =K_0-M(\kappa)-\kappa\|h_\kappa\|_\rho^2.
\]
Indeed the two mixed form entries are each `-M(kappa)`, and
`q_D(h_kappa)=M(kappa)-kappa||h_kappa||^2`. Both entries are retained
in this calculation. Substitution of A47 and A49 gives, at the exact
coupling A46,

\[
 \boxed{(3-5\cdot10^{-13})\kappa
 <\frac{q_{H-E_0}(\Phi,\Phi)}{\|\Phi\|^2}
 <(3+5\cdot10^{-13})\kappa.}                       \tag{A49a}
\]
The actual map from this state to the finite-volume spectral assertion is
the inclusion of `span{Phi}` in `psi^perp intersect H^1_phys` and the exact
variational formula
`Delta_L=inf_(0!=v perpendicular psi) q_(H-E0)(v)/||v||^2`.
It gives `Delta_L` at most the middle expression in A49a. The lower bound
in A49a concerns the displayed state, with its own source and norm; no
inequality with the reverse variational direction is used.

For an additional arithmetic check, the single-column trial `Y=W/(6kappa)`
has leading response lower coefficient 1/6 and residual coefficient 1/48,
yielding the leading interval [1/6,3/16]. The exactly evaluated coefficient
28/165 lies strictly inside it. A39–47 give the tighter certified return.

## 11. Physical refinement, scope, and the next quantitative target

On the retained simultaneous path

\[
 a_n=a_0 2^{-n},\quad L_n=4\,2^{2n},\quad
 g_n^2=(g_0^{-2}+\beta n\log2)^{-1},\quad
 c_n=g_0^{-2}+\beta n\log2,
\]
\[
 \kappa_n=2^{n+1}/(a_0c_n),\quad \xi_n=c_n^2/4,
 \quad \ell_n=4\,2^{n-r}\quad\hbox{for a fixed level-r square}. \tag{A50}
\]
The all-coupling A5, A9, A13, A18 and A21 apply with these literal values.
For instance `|X_e log psi_n|<=2c_n^2` and the gauge-covariant inverse has

\[
 \| (\mathcal A_n|_{E_v})^{-1}\|
 \le\frac{3a_0c_n}{2^{n+1}}\longrightarrow0,           \tag{A51}
\]
uniformly in the vertex and exterior volume, including vertices changing
with n. The limit follows from `(constant+linear n)/2^n ->0`.
The physical contraction and all its cross derivatives remain those proved
in section 3; A51 is an estimate on that specified source sector.

The narrow interval A46 uses g^2=5000. Along A50, xi_n grows. A14's sharper
pointwise remainder is applicable precisely on `xi_n<=3/64`; A13's L2
remainder remains available at all xi_n with its displayed larger constant.
No substitution between those domains is made. Physical loop length grows
as ell_n, and the exact A21 constants retain that growth. A33 also quantifies
the loop-size growth of the small-xi coefficients. These facts locate the
remaining infrared problem in the full singlet contraction and its retained
conditional-kernel response, rather than conceal it in source coordinates.

The next quantitative calculation is the zero-shift physical response and
its smallest generalized energy relative to the restored Gram on coupled
loop families, with the exact A17 additional kernel retained. This cycle has
completed the three-moment task and one positive-shift response evaluation
on the above actual sources. It has also supplied all-coupling source inverse
and moment bounds. It has not evaluated a physical continuum mass lower edge.

## 12. Verification, source pins, and failures retained

`verify.py` uses original real quaternion coordinates and exact rational
polynomials. Its Haar integration uses
`int prod q_i^(2a_i)=prod(2a_i-1)!! / prod_(j=0)^(sum a-1)(4+2j)`, and odd
monomials integrate to zero. This identity follows by expressing four
independent real Gaussian coordinates in polar coordinates and cancelling
the identical radial moments; no physical measure is replaced by that
Gaussian auxiliary integral. The coordinate identity tested is on
`sum q_i^2=1` via explicit polynomial division with its retained remainder.
Original graph words and unique unmatched-edge witnesses are checked for
square sides 1 through 12. These finite cases accompany the incidence proof
for every side in section 7.

For numerical endpoints, Machin's identity
`pi=16 atan(1/5)-4 atan(1/239)` is verified by the tangent addition formula
and its interval (0,pi/2). Alternating rational sums prove `pi<355/113`.
The exponential upper bound uses thirty positive Taylor terms plus the
geometric bound on the remaining term ratios; square-root bounds use integer
squares at scale 10^50. Every inequality A46–47 and A49's reported radius is
then checked with rational upper endpoints. Ordinary and optimized Python
must produce identical records; errors use explicit exceptions.

An initial development run failed the Machin tangent check because the test
applied a redundant angle doubling to the already quadrupled tangent 120/119.
The test was corrected to `(120/119-1/239)/(1+(120/119)(1/239))=1`.
The analytic statements and source bounds were unchanged. The final written
proof audit also corrected the interpretation of the noncanonical trial
residual: A45a now retains its exact difference from the canonical quotient
norm. The response and moment inequalities A38 and A45 retain their values;
a new exact regression rejects the false identification. Notational review
separates the residual vector mathfrak r_e from the plaquette count r_e, and
the error radii epsilon_j from the ground energy E_0. No failed run or earlier
file is represented as a certificate for these final bytes.

[YM] `KokunoYumeto/yang-mills-interacting-workbench`, primary source at
`fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`,
`yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md`,
Git blob `66a7453a6452c2555a28270efcf53fa1997c26a8`, sections 1–3.
The original full operator, ground-state domain and local exterior comparison
are used. All new derivative and response estimates are proved above.

[Parent] Same repository, PR6 at
`e98b2c3af77f66fb1c1396143ca53daef586404f`,
`yang-mills/continuations/20260914-coupled-response/RESEARCH_NOTE.md`,
blob `1f6bfb085a626f3b1aa693e86a619e81af41529a`, especially C13–22.
Its full delivered body was read. A15–20 prove the additional observation map
and its kernel; A43–45 instantiate its actual residual-cohomology certificate.
Earlier workbench attribution and the primary SU(2) conventions are preserved.
No new number-theoretic asymptotic or peer formal certificate is imported.


---

# Chapter 7 — 20260915-gauge-native-band / BAND_AND_CERTIFICATE.md

Original text path: `workbench/yang-mills/continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md`.

# The complete plaquette band, its interaction matrix, and a certified first eigenvalue

15 September 2026. All notation is from RESEARCH_NOTE.md G1–31. Energies below retain kappa=2g^2/a. Fourier norms are auxiliary estimates on the original coefficients; the raw physical band Gram is written explicitly in B6. No spin truncation of the Hamiltonian is used.

## B1. Spectral exclusion and an isolated physical band

Let epsilon=(1-sqrt(1-256xi/3))/2 on 0<=xi<=3/256. The estimate G23 yields, on the physical Haar-mean-zero Fourier source,

\[
 \| (\kappa K_L-z)^{-1} V_\xi \|_{Y_0\to Y_0}
 \le\epsilon\sup_{c\in\operatorname{spec}(K_L|_{\rm phys})\setminus\{0\}}
            \frac{\kappa c}{|\kappa c-z|},
 \quad V_\xi=-2\kappa Q_H\sum_i(X_iv(\xi))X_i.            \tag{B1}
\]

All positive physical eigenvalues consequently belong to the union of the intervals

\[
 [\kappa c(1-\epsilon),\kappa c(1+\epsilon)],
 \qquad c\in\operatorname{spec}(K_L|_{\rm phys})\setminus\{0\}. \tag{B2}
\]

For a real point outside the union, the right side of B1 is strictly smaller than one; at large c the quotient tends to one. The same eigenfunction contradiction as G26 proves B2, including the endpoints by closure.

For 0<=xi<3/400, epsilon<1/5. The c=3 interval is separated from all c>=9/2 intervals. The fixed contour

\[
 \mathcal C:\quad |z-3\kappa|=3\kappa/5                 \tag{B3}
\]

has sup kappa c/|kappa c-z|<=5, attained in its free bound at c=3 or c=9/2. It therefore lies in the resolvent set throughout this interval. The entire first physical excitation band is inside this contour and contains exactly |P_L| eigenvalues, including multiplicities. In particular the spectral gap is the lowest eigenvalue in this band. The coupling range is g^2>10/sqrt(3); the endpoint xi=0 is an auxiliary spectral parameter used to fix the rank.

Here is a precise operator justification including that endpoint. On X_0, K_L with domain Y_0 is closed and has compact inverse, since 1/c tends to zero and only finitely many product-spin labels have bounded c. G23 makes V_xi a relatively bounded perturbation with relative bound epsilon<1. The resolvent of kappa K_L+V_xi on the physical mean-zero space is supplied on B3 by the convergent operator Neumann series; its compactness follows from the compact free inverse. Its eigenvectors and generalized eigenvectors are C^2 by the Fourier domain, then smooth by elliptic bootstrapping. The exact G24 map identifies them with the original centered physical operator for real xi. The latter is self-adjoint, so no generalized eigenspace enlargement is introduced by this Banach realization. Conversely all original physical eigenfunctions belong to Y_0 by G23's regularity argument.

The coefficients of v(zeta) are holomorphic for |zeta|<3/256, with the same absolute majorant at |zeta|. Thus the resolvent on B3 and its Riesz projection vary analytically wherever 5epsilon(|zeta|)<1. At zero the projection is the original Haar projection P onto span{W_p}; its rank is |P_L| by G8. Contour-resolvent continuity fixes that finite rank on the stated real interval. This proves the asserted band for the actual Hamiltonian, without requiring a finite spectral cutoff.

## B2. The exact coefficient map and a uniform analytic remainder

Work first on the closed complex disk |zeta|<=rho_*=1/320. Put eta=epsilon(|zeta|). The exact scalar inequality sqrt(11/15)>107/125 gives

\[
 \eta<9/125,\qquad 5\eta<9/25.                           \tag{B4}
\]

Let P_zeta be the Riesz projection from B3, E_zeta=P P_zeta P on the original plaquette space, and

\[
 U_\zeta=P_\zeta P E_\zeta^{-1},\qquad
 A_{\rm band}(\zeta)=P(\kappa K_L+V_\zeta)U_\zeta.        \tag{B5}
\]

No arbitrary frame is chosen: P U_zeta=I, and the original plaquette coefficient vector is the retained coordinate. On this frame the X_0 norm is 8 sum_p|x_p| and the Y_0 norm is 24 sum_p|x_p|, by G14 and orthogonality of the distinct product-spin blocks. Thus induced matrix 1-norms have no omitted frame factor.

To prove E_zeta invertible and compute the remainder constant, expand the contour resolvent using the complete V_zeta. Its zeroth contribution to E_zeta is I. Its one-insertion contribution is the integral of P V_zeta P/(z-3kappa)^2 and is exactly zero. Every term with at least two insertions is bounded on X_0 by its geometric bound. Hence

\[
 \|E_\zeta-I\|_1\le\frac{(5\eta)^2}{1-5\eta},\qquad
 \|E_\zeta^{-1}\|_1\le
       \frac{1-5\eta}{1-5\eta-25\eta^2}.                 \tag{B6}
\]

The denominator is positive by B4. Also

\[
 \|(I-P)P_\zeta P\|_{X_0\to Y_0}
          \le\frac{15\eta}{1-5\eta}.                   \tag{B7}
\]

Indeed its free term is zero. Integrate R_0 V_zeta R_zeta P around the contour: the radius is 3kappa/5, the Q-free resolvent norm into Y_0 is at most 5/kappa, V has norm kappa eta, and the full resolvent on P has norm at most 5/[kappa(1-5eta)] into Y_0. These four factors give B7.

Write b=64/3. The source recurrence implies that V_zeta's first Taylor coefficient has norm at most kappa b, and its higher-coefficient tail at |zeta| has norm at most kappa(eta-b|zeta|), from Y_0 into X_0. Section B3 below proves P V_[1] P=0. Since P U_zeta=I, equations B5–7 give

\[
 \|A_{\rm band}(\zeta)-3\kappa I\|_1
 \le\kappa\left[3(\eta-b|\zeta|)
            +\frac{15\eta^2}{1-5\eta-25\eta^2}\right].  \tag{B8}
\]

For Cauchy's coefficient estimate evaluate B8 on the boundary |zeta|=1/320. There b|zeta|=1/15 and eta<9/125, so

\[
 \|A_{\rm band}(\zeta)-3\kappa I\|_1
 \le\kappa B_*,\quad
 B_*:=3(9/125-1/15)+
       \frac{15(9/125)^2}{1-5(9/125)-25(9/125)^2}
       =\frac{6713}{39875}.                             \tag{B9}
\]

All denominators and signs in this bound are retained. Matrix-valued Cauchy integration now gives the exact expansion

\[
 A_{\rm band}(\xi)=3\kappa I+\kappa\xi^2T_L+\mathcal R_L(\xi),
 \quad
 \boxed{\|\mathcal R_L(\xi)\|_1
       \le\kappa B_*\frac{(320|\xi|)^3}{1-320|\xi|}}
 \quad (|\xi|<1/320).                                   \tag{B10}
\]

This is uniform in the original box size. The first coefficient is exactly zero, and T_L is calculated next. The estimate sums every higher order; it is not a finite-spin replacement or an assumed remainder. The underlying square-root source radius remains 3/256; 1/320 is the explicitly chosen interior contour radius for this numerical bound.

## B3. The full second coefficient with the extensive cancellation retained

Let S=sum_p W_p and M=|P_L|. The unchanged scalar vacuum-energy expansion is

\[
 E_{0,L}(\xi)=2\kappa M\xi-\kappa M\xi^2/3+O_L(\xi^3).
                                                               \tag{B11}
\]

It follows directly from G20–21: v_[1]=S/3, int_H W_pW_q=delta_pq and K_L W_p=3W_p imply int_H sum|Xv_[1]|^2=M/3. The O_L notation in this identity describes its fixed finite box Taylor tail; the band tail itself is the explicit volume-uniform B10.

The first band coefficient vanishes. For all p,q,r, int_H W_p W_q W_r=0. If exactly two indices coincide, an unmatched link of the third face makes the integral zero. If all three coincide, the third fundamental character moment is zero. If three distinct faces occurred without an unmatched edge, each edge of one face would need a different neighboring face; only two others are present. This is impossible because distinct elementary plaquettes share at most one edge. Thus P S P=0. Integration by parts with the three original plaquette Casimirs also proves P V_[1]P=0 in the ground-transformed coefficient system.

On the full original Haar physical space, let Q_3=I-P, so Q_3 includes the constant. Matching the second Taylor coefficient in the original Schrödinger equation gives

\[
 \boxed{T_L=\frac M3 I-P S Q_3
              (K_L-3)^{-1}Q_3 S P.}                    \tag{B12}
\]

The inverse is on Q_3, where its original eigenvalues include -1/3 on the constant and positive inverses for c>=9/2. The term M/3 in B12 is precisely B11's vacuum-energy contribution.

To verify that B12 is also the B5 coefficient, the literal multiplier e^{v(zeta)} intertwines the original Schrödinger operator H_L(zeta)-E_*(zeta) and its ground-transformed operator. Its first multiplier coefficient is v_[1]=S/3, and P v_[1] P=0 by the just-proved triple integral. The additional scalar in G24 lands in the constant block. Thus the P coefficient of this intertwining map is I+O(zeta^2). Conjugating a band matrix whose zeroth coefficient is 3kappa I and whose first coefficient is zero by I+O(zeta^2) changes no second coefficient. Alternatively, its order-one equation is (K_L-3)phi_1=Q_3 Sx for x in P, and projecting its order-two equation gives B12 directly. This proves the complete map and its coefficient-level return rather than assigning the two source formulas the same name.

## B4. Evaluate every intermediate channel

The identities F_p^2=1+chi_1(Omega_p) give two original intermediate components: the constant of Haar norm one and energy zero, and the spin-one plaquette character of Haar norm one and Casimir 8. Distinct spin-one plaquette components are orthogonal.

For p!=q with no shared edge, F_pF_q is an original Casimir eigenfunction of value 6 and Haar norm one, regardless of a shared vertex.

For p,q sharing one edge, retain its original link U. Cyclic trace and inversion of a whole SU(2) trace put the two original words into the form Tr(UA), Tr(U^-1 B), where A and B are their respective ordered three-link path products. Both transformations are literal word identities. The Haar map U,A,B retains independent product Haar, by integrating the original remaining path links successively. Therefore the spin-zero projection at U is

\[
 P_{U,0}(F_pF_q)=\tfrac12\operatorname{Tr}(AB),\qquad
 \|P_{U,0}(F_pF_q)\|_H^2=1/4.                           \tag{B13}
\]

The product has total norm one. The complementary spin-one component at the shared edge consequently has norm squared 3/4, and the two components are orthogonal. The six other original spin-1/2 edges contribute 9/2 to K_L; the shared spin-one edge adds 2. Their exact energies are thus 9/2 and 13/2. Their total resolvent weight at the original band energy 3 is

\[
 \frac{1/4}{9/2-3}+\frac{3/4}{13/2-3}
       =\frac16+\frac3{14}=\frac8{21}.                  \tag{B14}
\]

No pair channel has been omitted. To prove orthogonality for distinct unordered pairs, use independent central sign changes of the original links. The half-integer spin support of F_pF_q is the mod-two symmetric difference of the two face boundaries. Equality for two different unordered pairs would yield a nonzero mod-two sum of at most four elementary faces with zero boundary. Each of the four edges of any included face would require a different other face, giving at least five faces. Hence equality is impossible. Orthogonality follows from the actual sign-changing Haar substitution. The self-pair channels have even center parity and are separated from these distinct-pair channels; their nonconstant parts were already separated by their spin support.

Write p~q for shared-edge adjacency and d_p=#{q:q~p}. Substituting all channels into B12 gives

\[
 \boxed{(T_L)_{pp}=\frac7{15}-\frac{d_p}{21},\qquad
 (T_L)_{pq}=\begin{cases}-1/21,&p\sim q,\\0,&p\not\sim q,\ p\ne q.
 \end{cases}}                                          \tag{B15}
\]

For clarity, the unreduced diagonal calculation is

\[
 \frac M3+\frac13-\frac15
   -\frac{M-1-d_p}{3}-\frac{8d_p}{21}.
\]

For a nonadjacent off-diagonal pair its terms are +1/3 from the constant and -1/3 from the actual two-plaquette intermediate. For an adjacent pair they are +1/3 and -8/21. These equalities retain each canceled extensive or off-diagonal contribution as its original intermediate channel.

Let A_adj be this adjacency matrix and D_deg=diag(d_p). The exact operator statement is

\[
 T_L=\frac7{15}I-\frac1{21}(D_{\rm deg}+A_{\rm adj}).     \tag{B16}
\]

All open-boundary degrees remain; replacing d_p by twelve changes the actual finite matrix.

## B5. Boundary-sensitive bounds, the full physical lower edge, and one original-box certificate

Each elementary plaquette has d_p<=12. The complete column sum of the absolute entries in T_L is at most 71/105. Indeed at degree d the sum is |7/15-d/21|+d/21; for d<=9 it equals 7/15 and for 10<=d<=12 its largest value is 71/105. Gershgorin's bound for B10, with its whole column residual, consequently proves

\[
 \boxed{\Delta_L\ge\kappa\left[
       3-\frac{71}{105}\xi^2
         -B_*\frac{(320\xi)^3}{1-320\xi}\right],
       \quad 0<\xi<1/320.}                              \tag{B17}
\]

The gap belongs to the band by B1. This lower bound uses the entire actual physical spectrum, not the Rayleigh quotient of one observed vector. G26 remains simultaneously available. At xi=10^-8, integer/rational evaluation gives

\[
 \boxed{\Delta_L>\kappa(3-7.314\,10^{-17})
          \quad\hbox{for every }L\ge2.}                 \tag{B18}
\]

No matrix minimum is formed between the two different lower-bound arguments.

The degree count is exact. Put m=2L. There are M=3m^2(m+1) faces, and the edge incidence values 4,3,2 occur respectively 3m(m-1)^2, 12m(m-1), 12m times. Since a pair of distinct faces shares at most one edge,

\[
 \sum_p d_p=12m(3m^2-1),\qquad
 \overline d=\frac{4(3m^2-1)}{m(m+1)}.                   \tag{B19}
\]

The original constant coefficient vector on all M plaquettes has squared Haar norm M. In B16 it therefore gives

\[
 -\frac{71}{105}\le\lambda_{\min}(T_L)
 \le\frac7{15}-\frac{2\overline d}{21}
 =-\frac{71}{105}+\frac{8(3m+1)}{21m(m+1)}.              \tag{B20}
\]

This evaluates the large-box limit of the actual second coefficient with an explicit boundary remainder. It does not interchange that coefficient limit with a varying-coupling spectral limit.

The checker additionally computes the full original L=2 matrix, containing 240 plaquettes. Let Q_L=D_deg+A_adj. Starting with the original vector x_0=(1,...,1), it computes x_100=Q_L^100 x_0 by integer multiplication. All entries are positive. The minimum and maximum of (Q_L x_100)_p/(x_100)_p enclose its largest eigenvalue: the upper bound is the row-sum bound after diagonal conjugation by diag(x_100); the lower bound follows either by the positive Perron vector or by the Rayleigh quotient. Q_L is symmetric nonnegative and its graph is connected. Direct exact computation returns

\[
 21.86319640514<\lambda_{\max}(Q_L)<21.86319641826,
\]
\[
 -0.57443792469<\lambda_{\min}(T_L)<-0.57443792405.        \tag{B21}
\]

A separate fraction-free symmetric congruence of Q_L-21I has inertia (1 positive,239 negative,0 zero). Every integer division and all 240 pivot determinants are retained in BOX_L2_CERTIFICATE.json. At stage k the exact symmetric Schur step is

\[
 a_{ij}^{\rm new}=(a_{kk}a_{ij}-a_{ik}a_{jk})/d_{k-1},
\]

with d_-1=1 and d_k the current pivot; the actual pivot of the ordinary Schur complement is d_k/d_(k-1). Congruence by unit triangular elimination proves that their signs give the stated inertia. No numerical eigenvalue routine is used for this certificate. It proves that every other eigenvalue of T_L is greater than -8/15.

On 240 by 240 matrices, ||R||_2<=sqrt(240)||R||_1<16||R||_1. At the actual coupling xi=10^-10, B10 therefore bounds the perturbation in (A_band-3kappa)/(kappa xi^2) by

\[
 \delta_*:=16B_*\frac{320^3\xi}{1-320\xi}<0.008827.       \tag{B22}
\]

Use the fixed contour of radius 1/50 around -574438/10^6. B21 and the just-certified other-eigenvalue bound put this contour at distance greater than delta_* from the spectrum of the Hermitian T_L. Resolvent Neumann expansion along the finite interpolation T_L+t(A_band-3kappa-kappa xi^2T_L)/(kappa xi^2) preserves its rank-one spectral projection. The actual band eigenvalues are real by Section B6 below. Normal-resolvent distance bounds place the single eigenvalue in the B21 interval enlarged by delta_*, while every other band eigenvalue is above -8/15-delta_*. The single eigenvalue is thus the original spectral gap. The final outward rational bounds are

\[
 \boxed{
 \kappa(3-0.5833\xi^2)<\Delta_{L=2}<\kappa(3-0.5656\xi^2),
 \quad \xi=10^{-10},\quad g^2=50000,\quad\kappa=100000/a.
 }                                                        \tag{B23}
\]

This certificate concerns the full interacting Hamiltonian in the original L=2 box, for every a>0. Its analytic remainder contains every Fourier spin and every higher perturbative order. The auxiliary 240 by 240 matrix is the exact second Taylor coefficient, not a truncation declared to equal the Hamiltonian.

## B6. The original band metric and its intertwining map

For real xi in B5's domain, let y=U_xi x in the original Haar coefficient source, and define

\[
 \mathcal R_\xi x
   =\psi_L\left[y-\langle y\rangle_{\rho_L}\right],\quad
 G_\xi=\mathcal R_\xi^*\mathcal R_\xi.                    \tag{B24}
\]

The map is injective because P U_xi=I and the only removed functions are constants. It is onto the complete first physical band: the Riesz range and G24 give the inverse by taking its original Haar plaquette coefficients after dividing by psi_L. Thus G_xi is the actual positive Gram in these prescribed coefficient coordinates. At zero its value is I because int_H W_pW_q=delta_pq, a calculated source identity.

The exact operator and energy identities are

\[
 (H_L-E_{0,L})\mathcal R_\xi=\mathcal R_\xi A_{\rm band}(\xi),
 \quad E_\xi=\mathcal R_\xi^*(H_L-E_{0,L})\mathcal R_\xi
             =G_\xi A_{\rm band}(\xi)
             =A_{\rm band}(\xi)^*G_\xi.                 \tag{B25}
\]

The inverse on the Riesz image and all physical pairings are retained. This proves the claimed reality of the actual band spectrum and exhibits the self-adjoint Hamiltonian comparison without replacing G_xi by an identity matrix.

## B7. Complete second-order spatial propagation in the original lattice coordinates

On the infinite cubic plaquette graph, index a plaquette by its normal axis a in {1,2,3} and base n in Z^3. Its center is n+c_a, with c_a=(e_b+e_c)/2 for the other axes b,c. The Fourier map and inverse are

\[
 (\mathcal F x)_a(k)=\sum_nx_{a,n}e^{-ik\cdot(n+c_a)},\quad
 x_{a,n}=\frac1{(2\pi)^3}\int_{[-\pi,\pi]^3}
            e^{ik\cdot(n+c_a)}(\mathcal Fx)_a(k)\,dk.     \tag{B26}
\]

Orthogonality of the original exponentials proves the isometry with the displayed measure. The components retain their boundary phase under k_i->k_i+2pi: e^(-2pi i(c_a)_i). This records the half-link center coordinates rather than discarding them.

Counting the actual shared links gives Q(k)=12I+A(k), with

\[
 A_{aa}(k)=2\cos k_b+2\cos k_c,\qquad
 A_{ab}(k)=4\cos(k_a/2)\cos(k_b/2)\quad(a\ne b),
 \quad T(k)=\frac7{15}I-\frac1{21}Q(k).                 \tag{B27}
\]

For the four perpendicular neighbors of a,b their relative center displacements are (+/-e_a+/-e_b)/2; summing their four exponential factors proves the off-diagonal formula. The four coplanar displacements are +/-e_b,+/-e_c, proving the diagonal formula. These are the actual adjacency maps of B16, now at every retained spatial momentum.

At k=0 the raw vector (1,1,1), of squared norm 3, has T-eigenvalue -71/105. Its coefficient-orthogonal plane x_1+x_2+x_3=0 has eigenvalue -11/105. On the fundamental cube all cos(k_a/2)>=0 and every row sum of Q(k) is at most 24; the maximum 24 is attained at k=0. Hence the bottom of the complete second-coefficient spatial operator is exactly -71/105.

The simple lowest branch has the Taylor expansion

\[
 t_{\rm low}(k)=-\frac{71}{105}+\frac4{63}|k|^2+O(|k|^4). \tag{B28}
\]

For a direct calculation, the diagonal quadratic change of A is -(k_b^2+k_c^2), and its a,b off-diagonal change is -(k_a^2+k_b^2)/2. Their full sum divided by the raw squared norm 3 is -(4/3)|k|^2. The other two eigenvalues are separated at zero, all matrix first derivatives there vanish, and the finite eigenvalue equation consequently gives B28; the eigenvector correction first contributes at fourth order. All original spatial directions remain.

With physical momentum p and k=ap, the corresponding exact Taylor coefficients of the energy band are

\[
 3\kappa-\frac{71}{105}\kappa\xi^2
       =\frac{6g^2}{a}-\frac{71}{840g^6a},\qquad
 \frac4{63}\kappa\xi^2a^2|p|^2=\frac{a}{126g^6}|p|^2.  \tag{B29}
\]

These are coefficients of the original strong-coupling band. B10 controls its full finite-box analytic remainder; B20 controls the large-box second coefficient. Neither a relativistic dispersion relation nor an exchange of the small-xi, volume and a->0 limits is asserted.

## B8. A primary-source coefficient check with the physical dictionary retained

A separate final source check located the planar coefficient in Bernd Dahmen,
*Strong coupling expansion for scattering phases in hamiltonian lattice field
theories. II. SU(2) gauge theory in (2+1) dimensions*, DESY 94-236,
arXiv:hep-lat/9412080, equations (1.7)–(1.11), Figure 1.3 and (1.26)–(1.29).
The original PDF pages 3, 4, 9 and 10 were inspected, including the graph signs.
This is a local-coefficient comparison; no three-dimensional remainder bound
is imported from that paper.

On the same planar graph, write its hopping coefficient as h_D, its coupling
as g_D, and its unscaled Hamiltonian as H_D'. The exact physical dictionary is

\[
 h_D=\xi,\qquad g_D=2^{3/4}g,\qquad
 H_{\rm plane}(a,g)=\frac{\sqrt2}{a}H_D'(g_D)
                        +2\kappa\xi M I.               \tag{B30}
\]

Indeed h_D=2/g_D^4=1/(4g^4), while
(sqrt(2)/a)(g_D^2/2)=2g^2/a=kappa. The Casimir identity
(n^2-1)/4=j(j+1) uses n=2j+1, and the original plaquette word is
identical under the original link labels. Thus B30 is equality of the
operators on the common planar-link domain, retaining its energy multiplier
and additive scalar. Ground-energy differences retain the multiplier.
The comparison at a periodic planar graph uses that graph on both sides;
it assigns no periodic boundary to the original open three-dimensional box.

On the planar plaquette graph the bulk degree is four. Repeating B12–16
with those actual incidences gives

\[
 T_{\rm plane}=\frac{29}{105}I-\frac1{21}A_{\mathbb Z^2},
 \qquad
 t_{\rm plane}(k)=\frac3{35}
                   +\frac{4-2\cos k_1-2\cos k_2}{21}.  \tag{B31}
\]

These are precisely the source's second coefficient and momentum coefficient
under B30. The common self and neighboring contributions have the original
values 2/15 and -8/21 in its Figure 1.3, as calculated in B12–14.

For the relation to the three-dimensional coefficient, let J_plane insert the
coefficients of one fixed plane and orientation into the full infinite
plaquette array, with zero on all other faces. Its adjoint reads precisely
those coordinates, so J_plane* J_plane=I. Each such face has its four planar
neighbors and eight perpendicular neighbors. Consequently

\[
 J_{\rm plane}^*T_{\mathbb Z^3}J_{\rm plane}
           =T_{\rm plane}-\frac8{21}I,
 \quad
 ((I-J_{\rm plane}J_{\rm plane}^*)T_{\mathbb Z^3}J_{\rm plane}x)_q
       =-\frac1{21}\sum_{\substack{p\ {
m in\ plane}\p\sim q}}x_p.
                                                               \tag{B32}
\]

The second equation retains the complete coupling to the other plaquettes.
The three-dimensional lowest coefficient -71/105 comes from B27's complete
three-component matrix, not from deleting that coupling. This source check
supports the local matrix arithmetic and preserves the antecedent's credit.


---

# Chapter 8 — 20260915-gauge-native-band / RESEARCH_NOTE.md

Original text path: `workbench/yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md`.

# Gauge-native source bounds and the full physical excitation band

15 September 2026. This continuation starts from the original SU(2) Hamiltonian and the delivered `20260915-uniform-gap-zero-shift` source. Its new calculations use the vertex-gauge action before estimating the nonlinear source. All original links, spin labels, Fourier coefficients, physical energy factors, means, relation labels and vacuum scalar remain. `BAND_AND_CERTIFICATE.md` calculates the first physical band and its full second coefficient, with a uniform analytic remainder. `SPATIAL_RETURN.md` gives the unique spatial-volume return on the enlarged domain. The final enlarged source and volume domain is established in SECOND_SOURCE.md R1–16 using the actual second vacuum coefficient. These are written proofs, accompanied by exact finite verification. No four-dimensional continuum mass-gap conclusion, new Lean verification or literature-priority claim is made.

## G1. Original objects and the precise retained quotient

For integer L>=2 take the vertices {-L,...,L}^3, all positive contained nearest-neighbor links E_L, and all contained elementary plaquettes P_L with their original oriented four-link words W_p. Put

\[
 H_L=\kappa K_L+\kappa\xi\sum_{p\in P_L}(2-W_p),\quad
 K_L=-\sum_{e,\alpha}X_{e,\alpha}^{2},\quad
 \kappa=2g^2/a,\quad \xi=1/(4g^4),\quad a,g>0.                 \tag{G1}
\]

Here T_alpha=-i sigma_alpha/2 and X differentiates exp(t T_alpha)U_e. Product Haar probability, the scalar 2 kappa xi |P_L|, and the original physical invariant subspace are retained. Let psi_L>0 be the positive unit vacuum and E_0,L its actual energy. The original multiplication map

\[
 \mathcal U_L:L^2(\rho_LdU)\longrightarrow L^2(dU),\quad
 f\longmapsto\psi_Lf,\quad \rho_L=\psi_L^2
\]

is unitary, with inverse division by psi_L. Its transported form is

\[
 q_{\mathcal A_L}(f,h)=\kappa\int\rho_L\sum_{e,\alpha}
       \overline{X_{e,\alpha}f}X_{e,\alpha}h\,dU,
 \qquad \mathcal A_L=\mathcal U_L^{-1}(H_L-E_{0,L})\mathcal U_L. \tag{G2}
\]

On this finite compact group the operator and form domains are H^2 and H^1, respectively, with their invariant subspaces in the physical calculation. The positive smooth vacuum and the form identity are also proved directly in G8 for the constructed range of couplings.

For product-spin labels j=(j_e), keep

\[
 c(j)=\sum_ej_e(j_e+1),\quad
 f_j(U)=\operatorname{Tr}(A_j\pi_j(U)),\quad
 A_j=d_j\int f(U)\pi_j(U)^*dU.                              \tag{G3}
\]

The representation dimension d_j is part of the coefficient; the matrix trace norm below is that of A_j. Vertex-gauge averaging P_G acts on this original coefficient space, commutes with K_L, and preserves every j block and every local support. The exact quotient map is

\[
 \mathscr C/\operatorname{im}(I-P_G)\xrightarrow{\cong}
 \operatorname{im}P_G,\quad [f]\mapsto P_Gf,
 \quad h\mapsto[h].                                      \tag{G4}
\]

Indeed P_G^2=P_G by Haar multiplication, ker P_G=im(I-P_G), and f-P_G f is that displayed original relation. Each coefficient eliminated by the gauge map is still a vector in this kernel. Only its actual image is used in the next estimate.

## G2. A graph inequality on every nonzero physical Fourier block

At each vertex v of a nonzero physical block, its incident spins obey

\[
 j_e\le\sum_{f\ni v,\,f\ne e}j_f.                        \tag{G5}
\]

For a proof, a nonzero invariant tensor at v gives an intertwiner from V_{j_e} into the tensor product of the other incident representations, with duals for opposite orientations. SU(2) duals have the same spin. Irreducibility makes this intertwiner injective. The highest J_3 weight of the target is at most the sum of those other spins; the image contains weight j_e. This proves G5. A nonzero global Fourier invariant supplies such a local invariant at every vertex, by grouping its original incident matrix indices. Thus no separate spin-network ansatz is assumed.

Fix e={u,v}. Write E_1 for the other edges incident on u or v, and O for their other endpoints. The original cubic graph is simple and triangle-free, so these endpoints are distinct and none is u or v. Each w in O has exactly one edge of E_1 entering {u,v}. Put J_1=sum_{f in E_1}j_f. The two inequalities G5 at u and v give J_1>=2j_e. Summing G5 at the vertices of O gives J_1<=2J_2, where E_2 consists of edges incident on O outside {e} union E_1 and J_2=sum_{f in E_2}j_f. Each such edge is counted at most twice. Hence

\[
 \sum_f j_f\ge j_e+J_1+J_2\ge4j_e.
\]

Every nonzero half-integer spin satisfies j(j+1)>=(3/2)j. Consequently

\[
 \boxed{c(j)\ge6j_e\quad\hbox{for every edge e in every nonzero physical block}.}
                                                               \tag{G6}
\]

The constant 6 is attained by a spin-1/2 elementary plaquette. The separate estimate

\[
 \sum_ej_e\le(2/3)c(j)                                   \tag{G7}
\]

continues to hold for arbitrary product-spin labels, including nonphysical ones. G6 and G7 have different specified domains and will be used at their respective places.

In particular every nonconstant physical block has c(j)>=3. If c(j)<9/2, its active support has at most five edges. No active vertex can have valence one by G5. A finite subgraph with at most five edges and no vertices of valence one in the cubic lattice is a four-cycle: it contains a cycle, the lattice has no triangle or odd cycle, and a fifth edge cannot have both endpoints on a four-cycle without producing a chord absent from the nearest-neighbor lattice. Every four-cycle is an elementary plaquette. The two-edge vertex invariants force the four spins to coincide. Their Casimir is 4j(j+1), equal to 3 at j=1/2 and at least 8 at j>=1. Thus

\[
 \operatorname{spec}(K_L|_{\mathrm{phys}})\subset
 \{0,3\}\cup[9/2,\infty),\qquad
 \ker(K_L-3)=\operatorname{span}\{W_p:p\in P_L\}.          \tag{G8}
\]

At a two-edge spin-1/2 vertex the invariant contraction is unique up to its scalar; following the four actual indices gives W_p. Different p have orthogonal product-spin blocks, and int_H W_p W_q=delta_pq. This proves both equality in the eigenspace statement and its dimension |P_L|.

## G3. The original coefficient source with all relation labels retained

For every nonempty finite edge label S retain a zero-Haar-mean physical function f_S with coefficients A_(S,j), including j whose active support is strictly smaller than S. Define

\[
 \|f\|_{\mathrm{loc},1}
 =\max_e\sum_{S\ni e}\sum_{j\ne0}c(j)\|A_{S,j}\|_1.     \tag{G9}
\]

This is an auxiliary absolute-convergence norm, on the SAME coefficient families as the predecessor. On each finite graph its identity map to the predecessor's weight-5/4 source has both inverse maps and bounds

\[
 \|f\|_{\mathrm{loc},1}\le\|f\|_{\mathrm{loc},5/4}
 \le(5/4)^{|E_L|}\|f\|_{\mathrm{loc},1}.                 \tag{G10}
\]

The volume-dependent comparison is recorded and is never used to assert a uniform bound. The physical pairing is still G2.

Assembly takes A_(S,j) to sum_{S containing supp(j)} A_(S,j). Its kernel is the original coefficient equation that this sum is zero for every j. The relation (B at (S,j))-(B at (supp(j),j)) and the actual coefficient at every S strictly containing supp(j) reconstruct that whole kernel, exactly as in predecessor U9-11. The physical subspace is preserved under this relation. Zero assembly therefore retains the original relation primitive, rather than deleting its supports.

The coefficient product and derivative bounds used here are

\[
 \sum_\ell\|A_\ell(f_jh_k)\|_1\le\|A_j\|_1\|B_k\|_1,
 \qquad\|A(X_{e,\alpha}f_j)\|_1\le j_e\|A_j\|_1.        \tag{G11}
\]

For completeness, the product is Tr((A_j tensor B_k)(pi_j tensor pi_k)). Unitary decomposition into the complete irreducible/multiplicity spaces, pinching to diagonal blocks, and partial trace over multiplicity give its exact output coefficients. Pinching is an average of unitary conjugations. For partial trace, trace-norm duality bounds Tr((Z tensor I)C) by ||C||_1 for ||Z||op<=1. These facts prove the first bound, retaining all output labels. The second follows from the original spin generator norm ||J_alpha||=j and trace-norm duality. All three alpha values remain.

Let Q_H remove only the trivial Haar coefficient. Define the original bilinear source

\[
 \mathcal B(f,h)_S=K_L^{-1}Q_H
 \sum_{S_1\cup S_2=S}\sum_{e,\alpha}
                  (X_{e,\alpha}f_{S_1})(X_{e,\alpha}h_{S_2}). \tag{G12}
\]

The scalar removed at each S is recorded separately. The active product support may become smaller, but the original union label S is retained.

For an anchor a in S_1, G6 on the h block and G7 on f give

\[
 3\sum_{S_1\ni a,j}\|A_{S_1,j}\|_1
       \sum_e j_e\sum_{S_2\ni e,k} k_e\|B_{S_2,k}\|_1
 \le\frac13\|f\|_{\mathrm{loc},1}\|h\|_{\mathrm{loc},1}.
\]

Interchanging f,h gives the other anchor contribution. Counting the overlap twice is an upper bound. The output c(j) cancels the exact inverse Casimir in G12, and therefore

\[
 \boxed{\|\mathcal B(f,h)\|_{\mathrm{loc},1}
           \le(2/3)\|f\|_{\mathrm{loc},1}\|h\|_{\mathrm{loc},1}.} \tag{G13}
\]

G13 is on the gauge-invariant source. Its proof retains the generator sum, graph constraints, and all representation multiplicities.

## G4. Exact plaquette coefficient, convergent source, and the closed endpoint

For the original word Tr(U1 U2 U3^-1 U4^-1), its complete 16 by 16 coefficient in G3 is

\[
 A_{(i_1,i_2,1-i_2,1-i_3),(i_0,i_1,1-i_3,1-i_0)}
       \mathrel{+}=(-1)^{i_0+i_2},\qquad i_0,i_1,i_2,i_3\in\{0,1\}. \tag{G14}
\]

All other entries are zero. The inverse-entry formula (U^-1)_(r,c)=(-1)^(r+c)U_(1-c,1-r) proves the identity in the original coordinates. The four disjoint two-row/two-column blocks have the entries [[1,-1],[-1,1]], with the remaining rows and columns unused. Thus (A* A)^2=4A* A and Tr(A* A)=16. The positive square root is (A* A)/2, giving ||A||_1=8. This independently reproduces predecessor O1-2.

The first source is v_[1]=(1/3)sum_p W_p, with its actual four-link labels. At most four plaquettes meet an edge, so

\[
 \|\xi v_{[1]}\|_{\mathrm{loc},1}\le32\xi.               \tag{G15}
\]

Use the full coefficient recurrence

\[
 v_{[p]}=\sum_{i=1}^{p-1}\mathcal B(v_{[i]},v_{[p-i]}),\quad
 v(\xi)=\sum_{p\ge1}\xi^p v_{[p]}.
\]

With C_n=(2n)!/(n! (n+1)!), G13 proves

\[
 \|\xi^p v_{[p]}\|_{\mathrm{loc},1}
 \le a_p(\xi):=C_{p-1}(2/3)^{p-1}(32\xi)^p.             \tag{G16}
\]

The original union recurrence also gives |S|<=3p+1, connected support, and j_e<=p/2 at order p. These are exact support facts, not alterations of any coefficient.

Set

\[
 \theta=256\xi/3,\quad
 r(\xi)=\frac34(1-\sqrt{1-\theta}),\quad
 \epsilon(\xi)=\frac23r(\xi)=\frac{1-\sqrt{1-\theta}}2.  \tag{G17}
\]

For 0<=theta<1 the Catalan recurrence proves sum_p a_p=r and

\[
 \sum_{p>P}a_p\le\frac{32\xi\theta^P}{1-\theta}.         \tag{G18}
\]

At the endpoint xi=3/256 the series still converges absolutely. The complete scalar tail there is

\[
 \sum_{p>P}a_p(3/256)
   =\frac34\frac{\binom{2P}{P}}{4^P}
   \le\frac{3}{4\sqrt{P+1}}.                            \tag{G19}
\]

To verify the exact equality, put b_P=binom(2P,P)/4^P. Then C_P/4^P=2(b_P-b_(P+1)). Telescoping and b_P->0 give the formula. The bound b_P<=1/sqrt(P+1) follows by induction from ((2P+1)/(2P+2))^2<=(P+1)/(P+2). It also proves b_P->0 without an asymptotic substitution.

For every finite box G9 is complete, and its total c-weighted coefficient sum is at most |E_L| times G9. G11 bounds the original first and second derivatives by that total. Absolute convergence, including G19, therefore gives a C^2 function and permits G12 to be summed. The fixed equation is

\[
 K_Lv=\xi\sum_pW_p+\sum_i(X_iv)^2-C_L,\quad
 C_L=\int_H\sum_i(X_iv)^2.                               \tag{G20}
\]

All removed scalar coefficients are exactly included in C_L. Set

\[
 c_L=-\tfrac12\log\int e^{2v}dU,\quad
 \psi_*=e^{v+c_L},\quad
 E_*=2\kappa\xi|P_L|-\kappa C_L.                         \tag{G21}
\]

Equation G20 and direct differentiation prove H_L psi_*=E_* psi_*. The positive C^2 solution becomes smooth by elliptic bootstrapping. For every smooth h the product rule proves q_(H_L-E_*)(psi_*h)=kappa int psi_*^2 sum|Xh|^2. Multiplication and division by the positive smooth psi_* preserve H^1 on this compact finite group. Hence E_* is the actual lowest energy; dividing any other ground vector by psi_* proves uniqueness. This identifies G21 with the original vacuum, including its full scalar and Haar mass. The completed closed coupling domain is

\[
 \boxed{0<\xi\le3/256,\qquad g^2\ge8/\sqrt3.}           \tag{G22}
\]

No contraction constant smaller than one is asserted at theta=1; G19 supplies that endpoint directly.

## G5. A relative bound for the original drift, and the full physical gap

Let X_0 be the zero-Haar-mean Fourier algebra with norm sum_j ||A_j||_1; let Y_0 carry sum_j c(j)||A_j||_1. Use the physical subspaces when explicitly indicated. For a smooth zero-Haar-mean f, the same original coefficient product gives

\[
 \left\|Q_H\sum_i(X_iv)(X_if)\right\|_{X_0}
 \le 3\sum_k\|A_k(f)\|_1\sum_e k_e
        \sum_{S\ni e,j}j_e\|A_{S,j}(v)\|_1
 \le\frac r3\|f\|_{Y_0}.                                \tag{G23}
\]

Only v uses G6; f uses G7. Thus G23 also holds on the full scalar space. The complete relative perturbation -2 kappa Q_H sum (Xv)X has norm at most kappa epsilon from Y_0 to X_0.

Every smooth function on the finite product belongs to Y_0. One direct proof uses Peter-Weyl Plancherel, ||A_j||_1<=sqrt(d_j)||A_j||_HS, and Cauchy-Schwarz with sufficiently many original Casimir powers. The series sum_j d_j^2(1+c(j))^-M is finite for M>3|E_L|/2; elementary comparison of the product-spin sums proves it. Smoothness supplies all these powers. This step requires no uniform-in-volume regularity constant.

The coefficient projection Q_H is related to the original centered-vacuum space by the two inverse maps

\[
 f\mapsto Q_Hf,\quad y\mapsto y-\langle y\rangle_{\rho_L},
 \quad \langle f\rangle_{\rho_L}=0,\ \int_Hy=0.           \tag{G24}
\]

Both compositions are identities. They intertwine A_L with its literal Haar quotient

\[
 \overline{\mathcal A}_L
 =\kappa K_L-2\kappa Q_H\sum_i(X_iv)X_i.                 \tag{G25}
\]

For the inverse identity in the operator square, int rho_L A_L y=0 gives precisely the constant required in G24. No Haar mean is substituted for a vacuum mean.

Let A_L f=lambda f be a nonzero physical excitation, and y=Q_Hf. For 0<lambda<3kappa, G8 and G23 give

\[
 \|y\|_{Y_0}
 \le\frac{3\kappa\epsilon}{3\kappa-\lambda}\|y\|_{Y_0}.
\]

The vector is nonzero, so lambda>=3kappa(1-epsilon). Every finite-regulator eigenfunction is smooth by the original elliptic equation. Compact spectral resolution consequently extends the result to the whole physical form domain:

\[
 \boxed{\Delta_L\ge d_{\rm phys}(\xi)\kappa,
 \quad d_{\rm phys}=3(1-\epsilon)
       =\tfrac32(1+\sqrt{1-256\xi/3}).}                   \tag{G26}
\]

On the full scalar space replace the free value 3 by its original 3/4. The identical argument proves

\[
 \boxed{\Delta_L^{\rm scalar}\ge d_{\rm sc}(\xi)\kappa,
 \quad d_{\rm sc}=\tfrac34(1-\epsilon)=d_{\rm phys}/4.}   \tag{G27}
\]

The inclusion of the original physical subspace into the scalar space intertwines both Hamiltonians; G26 uses its explicitly computed free Fourier support G8. All physical states, including volume-dependent states, are covered by G26.

For example at every g^2>=5,

\[
 \Delta_L\ge\tfrac32(1+\sqrt{11/75})\kappa
             >2.07445\kappa.                            \tag{G28}
\]

In the original physical units the general bound is

\[
 \Delta_L\ge\frac{3g^2}{a}
          \left(1+\sqrt{1-64/(3g^4)}\right).             \tag{G29}
\]

## G6. The native primitive and the zero-shift response return

On centered physical H^1 define d_X f=(X_i f)_i with its ORIGINAL energy norm kappa int rho sum|X_i f|^2. The inverse on its actual range is p_X(d_X f)=f. The variational characterization, with the G2 unitary, proves

\[
 \|p_X\|^2=1/\Delta_L\le1/(\kappa d_{\rm phys}).          \tag{G30}
\]

This is the primitive of the original gradient window. G4 and the assembly relations retain the sources used to control it. The auxiliary Fourier source norm supplies the spectral estimate; it has not replaced either the physical state norm or the derivative energy norm.

For the predecessor's loop observation, gauge averaging commutes with the actual conditional expectation: change variables in its defining conditional-density integral and use the basepoint conjugation of the original loop holonomy. It therefore commutes with the form compression D. Let I:K_phys->K be the isometric inclusion of its physical reducing subspace. The domain and resolvent identities are

\[
 DI=ID_{\rm phys},\quad (D+s)^{-1}I=I(D_{\rm phys}+s)^{-1}.
\]

The actual forcing W=-Q_C A_L F and the displayed trial and residual are physical. Consequently their unchanged response pairing is

\[
 \langle W,D^{-1}W\rangle
 =\langle I^*W,D_{\rm phys}^{-1}I^*W\rangle,
 \quad \|D_{\rm phys}^{-1}\|\le1/(\kappa d_{\rm phys}).   \tag{G31}
\]

All predecessor minimum-section, quotient-residual and mixed-state identities now use this stronger proven inverse bound on their actual source. The scalar inverse on the whole K retains its separate value G27.

## G7. What was audited and what is continued

The predecessor's Fourier pinching, original union labels, vacuum-scalar return, Haar/physical form maps and conditional comparison have been inspected at their displayed proof steps. The gain here is G6 on the original gauge image, followed by the explicitly re-derived constants G13, G15 and G23. A blanket independent review of every historical artifact is not claimed.

The full next calculation is in BAND_AND_CERTIFICATE.md: the entire first excitation band, the exact boundary-sensitive second-order matrix, and an actual finite-L eigenvalue enclosure with a uniform analytic remainder. SPATIAL_RETURN.md proves the full-volume result on the complete closed source domain, retains its separately calculated conditional-influence subdomain, and computes the original running continuum path. The strong-coupling endpoint G22 and the physical band do not assign a result at g approaching zero.


---

# Chapter 9 — 20260915-gauge-native-band / SECOND_SOURCE.md

Original text path: `workbench/yang-mills/continuations/20260915-gauge-native-band/SECOND_SOURCE.md`.

# The actual second vacuum source and continuation beyond the first endpoint

15 September 2026. This calculation uses the actual plaquette pair channels B12–14 to evaluate the second logarithmic-vacuum source before estimating higher orders. It improves the source endpoint further, while every original coefficient, relation label, Hamiltonian term, physical Gram and energy unit stays fixed. The previous estimates remain valid on their stated domains. R10–14 below supply the final enlarged finite- and infinite-volume domains of this continuation.

## R1. Evaluate the entire second source, including its zero coefficients

Use S=sum_p W_p and v_[1]=S/3. The original Casimir product rule gives

\[
 \sum_i(X_iS)^2=3S^2-\tfrac12K_LS^2,
 \qquad
 v_{[2]}=\left(\tfrac13K_L^{-1}-\tfrac1{18}I\right)Q_HS^2.
                                                               \tag{R1}
\]

The inverse acts only on the original nonconstant Haar coefficients. The scalar removed here remains in G20–21, whose second ground-energy term is exactly -kappa |P_L| xi^2/3.

For a single plaquette, W_p^2=1+chi_1(Omega_p), and the nonconstant term has Casimir 8. For distinct faces without a shared edge, the product has Casimir 6, so its coefficient in R1 is exactly zero. For an unordered adjacent pair {p,q}, let P_0 and P_1 be its actual shared-edge spin-zero and spin-one projections from B13. Their original Casimirs are 9/2 and 13/2. Substitution into R1 proves

\[
 \boxed{
 v_{[2]}=-\frac1{72}\sum_p\chi_1(\Omega_p)
   +\sum_{\{p,q\}:p\sim q}
      \left[\frac1{27}P_0(W_pW_q)-\frac1{117}P_1(W_pW_q)\right].}
                                                               \tag{R2}
\]

The factor two for an unordered pair comes from the two ordered terms of S^2. The labels remain the original plaquette or pair union. In particular P_0 has six active links but retains its seven-link union label. Every disjoint-pair coefficient is explicitly zero at its original union; it is not relabelled as an absent source.

## R2. Trace norms in the original link orientations

For a simple closed loop of length ell in the original positively oriented cubic links, let t be the number of local maxima of height x_1+x_2+x_3 around the loop. It also has exactly t local minima and ell-2t other vertices. At a maximum or minimum the original fundamental index contraction is the SU(2) alternating two-index vector, of Euclidean norm sqrt(2); at the other vertices it is a two-dimensional identity contraction. After separate permutations of the original row and column tensor indices, the Fourier coefficient is exactly a tensor product of those rectangular contractions. Row and column permutations preserve its singular values. Tensor-product singular values therefore give

\[
 \|A_{\rm loop}\|_1=(\sqrt2)^{2t}2^{\ell-2t}
                    =2^{\ell-t}\le2^{\ell-1}.         \tag{R3}
\]

The height cannot be strictly increasing around a closed loop, so t>=1. This also proves the original coefficient's full rank and singular values: rank 2^(ell-2t), with each nonzero singular value 2^t. These are original oriented coefficients; inversion of a single link is not assumed to preserve a tensor matrix's trace norm.

For the original spin-one plaquette the same four contractions have dimension three, with one maximum and one minimum. Its norm is exactly 3^3=27. Equivalently, the literal G14 matrix with indices in {0,1,2}, complements 2-i, and the same signs has nine rank-one three-by-three blocks. Each nonzero singular value is three.

For an adjacent pair, P_0(W_pW_q)=Tr(Omega_6)/2 on the actual simple six-link boundary. Equation R3 proves

\[
 x:=\|A(P_0(W_pW_q))\|_1\le16,
 \quad x+y\le64,\quad y:=\|A(P_1(W_pW_q))\|_1.          \tag{R4}
\]

The second bound is the full coefficient-product inequality G11 applied to the two original norm-eight plaquettes, including both irreducible outputs. No norm is assigned to P_1 from its Haar mass alone.

In the unchanged Casimir-weighted source G9, an adjacent pair's complete R2 contribution is at most

\[
 (9/2)x/27+(13/2)y/117
       =x/6+y/18\le16/3.                              \tag{R5}
\]

A spin-one self contribution is at most 8*27/72=3. For an anchored edge e, write r_e<=4 for its original face incidence. Counting each adjacent pair containing a face at e and subtracting its exact double count when both faces contain e gives

\[
 \#\{\{p,q\}:p\sim q,\ e\in\partial p\cup\partial q\}
 =\sum_{p\ni e}d_p-\binom{r_e}{2}
 \le12r_e-\binom{r_e}{2}\le42.
\]

Together with at most four self terms this proves the volume-independent bound on the ACTUAL second source:

\[
 \boxed{\|v_{[2]}\|_{\rm loc,1}\le4\cdot3+42\cdot16/3=236.} 
                                                               \tag{R6}
\]

The earlier purely bilinear estimate was (2/3)*32^2=2048/3. R6 uses the evaluated original pair channels and their complete coefficient norms.

## R3. A larger convergent source, with an explicit endpoint tail

Set a_1=32, a_2=236, and for n>=3 define the positive numbers

\[
 a_n=\frac23\sum_{i=1}^{n-1}a_i a_{n-i}.
\]

G13 and R6 prove ||v_[n]||loc<=a_n by induction, on the same original support-labelled coefficients. Their generating function r_2=sum_(n>=1)a_n xi^n satisfies

\[
 r_2=32\xi+236\xi^2+\frac23(r_2^2-1024\xi^2),
\]
\[
 \boxed{
 P_2(\xi)=1-\frac{256}{3}\xi+\frac{10720}{9}\xi^2,
 \qquad r_2(\xi)=\frac34(1-\sqrt{P_2(\xi)}),
 \qquad \epsilon_2=\frac23r_2.}                         \tag{R7}
\]

The branch has value zero at xi=0. Its positive coefficient recurrence proves the absolute majorant before any endpoint is taken. The first positive root is

\[
 \alpha=\frac3{4(32+\sqrt{354})},\qquad
 \beta_2=\frac3{4(32-\sqrt{354})},\qquad
 P_2=(1-\xi/\alpha)(1-\xi/\beta_2).                    \tag{R8}
\]

Write gamma=alpha/beta_2, so 0<gamma<1. In sqrt(1-z)=1-sum_(n>=1)b_n z^n the numbers b_n=C_(n-1)/(2*4^(n-1)) are positive. Multiplication of the two square-root series gives

\[
 0\le a_n\alpha^n
 \le\frac34 b_n(1+\gamma^n).
\]

The subtracted convolution has positive terms; the lower sign follows independently from the a_n recurrence. The exact binomial tail sum_(n>P)b_n=binom(2P,P)/4^P, already proved in G19, yields

\[
 \boxed{
 \sum_{n>P}a_n\xi^n
 \le\frac34(\xi/\alpha)^{P+1}(1+\gamma^{P+1})
                 \frac{\binom{2P}{P}}{4^P}
 \le\frac34(\xi/\alpha)^{P+1}
                    \frac{1+\gamma^{P+1}}{\sqrt{P+1}}}
 \quad(0\le\xi\le\alpha).                            \tag{R9}
\]

Thus the complete original source converges absolutely also at alpha. Monotone convergence of its positive majorant gives r_2(alpha)=3/4 and epsilon_2(alpha)=1/2. The same finite-box derivative summability and positive eigenfunction argument G20–21 identify the sum with the actual vacuum, retaining its scalar. On the common earlier domain both constructions sum identical original coefficients; their identity map and its inverse are literally the identity coefficient by coefficient.

## R4. Return to the complete physical spectrum and the unique volume limit

The original drift bound G23 now has r_2 in place of r, because its proof uses the same coefficient sum. Apply G24–27 to every actual physical eigenfunction, then the full compact spectral resolution. This proves on the closed enlarged domain

\[
 \boxed{
 \Delta_L\ge\frac{3\kappa}{2}(1+\sqrt{P_2(\xi)}),
 \quad 0<\xi\le\alpha,
 \quad g^2\ge\sqrt{(32+\sqrt{354})/3}.}                 \tag{R10}
\]

There is no dependence on L. The full scalar bound is one quarter of R10. In original physical units R10 is

\[
 \Delta_L\ge\frac{3g^2}{a}
       \left(1+\sqrt{1-\frac{64}{3g^4}+\frac{670}{9g^8}}\right).
                                                               \tag{R11}
\]

At the rational benchmark g^2>=17/4,

\[
 \Delta_L\ge\frac{3\kappa}{2}
           \left(1+\sqrt{35401/751689}\right)>1.8255\kappa.
                                                               \tag{R12}
\]

For xi<alpha the complete drift row sum is bounded by

\[
 \sum_{n\ge1}n a_n\xi^n
   =\xi r_2'(\xi)
   =\frac{32\xi-(2680/3)\xi^2}{\sqrt{P_2(\xi)}}<\infty.
\]

Coefficient compatibility and this row sum give exactly the finite-dynamics comparison S13–19 on that domain. The direct finite-semigroup proof S24–28 uses only G23 and now proves the full uniform mixing estimate with epsilon_2. In particular the whole vacuum-measure sequence converges by S29–30; a conditional-influence row smaller than one is not used in this return.

The actual coupling difference is bounded by r_2(eta)-r_2(xi), by the positive recurrence. The same complete Duhamel formula S31–33 consequently gives

\[
 \sup_{t\ge0}\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
 \le\frac{\epsilon_2(\eta)-\epsilon_2(\xi)}{1-\epsilon_2(\xi)}
          \|Q_HF\|_{X_0},\qquad0\le\xi\le\eta\le\alpha. 
                                                               \tag{R13}
\]

At eta=alpha this ratio is sqrt(P_2(xi))/(1+sqrt(P_2(xi))) and tends to zero. Inserting an interior coupling between two endpoint finite boxes, as in S13, proves the whole endpoint dynamics limit. Equation R9 supplies its actual drift convergence; no finite derivative row is assigned at alpha. Uniform mixing makes its limiting vacuum the unique invariant probability of this constructed semigroup, and finite reversibility and physical cylinder density give

\[
 \boxed{A_\infty|_{L^2_{\rm phys}(\nu)\cap1^\perp}
       \ge\frac{3\kappa}{2}(1+\sqrt{P_2(\xi)}),
       \qquad0<\xi\le\alpha.}                         \tag{R14}
\]

The raw physical primitive G30 and physical conditional inverse G31 receive the same stronger bound. The original response pairing and minimum-section correction remain unchanged. The complete band coefficient and its analytic error B10–32 remain valid on their already stated domains; no further band radius is assigned here.

## R5. Actual continuation scope

The final endpoint is approximately g^2=4.1156161030. The old g^2>=15 bound, the first gauge-native g^2>=8/sqrt(3) bound, and R10 refer to the same original Hamiltonian; the explicit coefficient inequalities and their physical return prove the successive gains. The construction at the old source-majorant endpoint is continued by the actual second source rather than by declaring that endpoint a physical singularity.

On the retained path g_n^2=1/c_n, c_n=g_0^-2+beta n log2, the final domain is c_n^2<=3(32-sqrt(354))/670. This follows by rationalizing 3/(32+sqrt(354)); both physical parameters stay those of S31. For beta>0 the path eventually leaves this domain. A nontrivial four-dimensional continuum field and a finite positive continuum mass along that path remain unevaluated.

The next selected source calculation is the actual order-three connected coefficient and full linearized remainder at xi v_[1]+xi^2 v_[2], with its original union labels. The present R2, R6, R9 and R14 are completed inputs to that calculation, not presumed estimates for it.

## R6. Return the coupling comparison to both original physical coefficients

For positive kappa_1,kappa_2 and 0<xi_1,xi_2<=alpha, set
xi_-=min(xi_1,xi_2), xi_+=max(xi_1,xi_2), kappa_+=max(kappa_1,kappa_2),
and e_-=epsilon_2(xi_-), e_+=epsilon_2(xi_+). The full physical inverse
is always g_j^2=1/(2sqrt(xi_j)), a_j=1/(kappa_j sqrt(xi_j)).
The actual vacuum density depends on xi_j; its dependence follows directly
from G20–21, whose energy scalar retains its factor kappa_j.

At one fixed xi the original generators satisfy

\[
 \mathcal A_{\kappa_2,\xi}-\mathcal A_{\kappa_1,\xi}
  =(\kappa_2-\kappa_1)
       \left[K_L-2\sum_i(X_iv_L(\xi))X_i\right].        \tag{R15}
\]

On the nonconstant evolved coefficient y, the full supremum norm of the
bracketed expression is at most (1+epsilon_2(xi))||y||Y. Duhamel's formula,
Markov supremum contraction, and S26 applied to the evolution with kappa_+
therefore bound the integrated coefficient change by
|kappa_2-kappa_1|(1+epsilon_2)/(kappa_+(1-epsilon_2))||Q_HF||X.
Insert the common intermediate coupling xi_- and use R13 for the other
change. This proves the explicit full-parameter estimate

\[
 \boxed{
 \sup_{t\ge0}\|T_{L,\kappa_2,\xi_2}(t)F
                 -T_{L,\kappa_1,\xi_1}(t)F\|_\infty
 \le\left[
      \frac{e_+-e_-}{1-e_-}
      +\frac{|\kappa_2-\kappa_1|}{\kappa_+}
                  \frac{1+e_-}{1-e_-}
      \right]\|Q_HF\|_{X_0}.}                         \tag{R16}
\]

The two evolutions use the same original physical time t. The result holds
for the constructed infinite-volume semigroups by their proved uniform
convergence. All four physical parameters are recovered by the displayed
inverse maps. This comparison has the exact domain R10; it does not assign
itself to the unproved later portion of the running continuum path.


---

# Chapter 10 — 20260915-gauge-native-band / SPATIAL_RETURN.md

Original text path: `workbench/yang-mills/continuations/20260915-gauge-native-band/SPATIAL_RETURN.md`.

# Unique spatial vacuum and dynamics across the first closed source domain

15 September 2026. This calculation re-evaluates the actual coefficient, conditional and dynamical maps of predecessor V1–22 using G6–23. Physical a>0 and g>0 remain fixed in the volume limit. The stronger physical gap is G26. S10–14 strengthen the conditional route to the full closed domain 0<xi<=3/256 by a direct volume-independent mixing bound and an explicit coupling modulus. The separate simultaneous continuum path is computed in S9 and returned in S14. SECOND_SOURCE.md R4 extends this same original dynamics to the later, larger source endpoint.

## S1. One compatible source family and its exact tails

The coefficient v_(S,[p]) is the SAME coefficient in every original box containing S: the source plaquette, inverse original Casimir, Haar projection and order-p union recurrence depend only on S. Induction proves this equality before summing the series. Connected order-p supports obey |S|<=3p+1 and j_e<=p/2. Let a_p be G16 and v_S=sum_p xi^p v_(S,[p]). Then

\[
 \sup_e\sum_{S\ni e}\sum_jc(j)\|A_{S,j}\|_1\le r,
 \quad \|v_S\|_\infty\le\tfrac13\sum_jc(j)\|A_{S,j}\|_1. \tag{S1}
\]

The factor 1/3 uses the proved physical nonconstant Casimir G8. In each finite box the original density is exactly

\[
 \rho_L=\frac{\exp(2\sum_{S\subset E_L}v_S)}{Z_L},
 \quad Z_L=\int\exp(2\sum_{S\subset E_L}v_S)dU,
 \quad c_L=-\tfrac12\log Z_L.                            \tag{S2}
\]

Each support retains its original union label even after an active Fourier cancellation. Thus an exterior contribution is not reassigned to an interior label.

For theta=256xi/3<1, differentiating the positive scalar majorant gives

\[
 \sum_{p\ge1}p a_p=\xi r'(\xi)=\frac{32\xi}{\sqrt{1-\theta}},
 \quad
 \sum_{p>P}p a_p\le32\xi\theta^P
       \frac{(P+1)-P\theta}{(1-\theta)^2}.              \tag{S3}
\]

Both tails are bounds for the complete original coefficient series. At theta=1 only the different tail G19 is used; S3 does not claim a finite derivative sum there.

## S2. The actual conditional kernels and their sharper influence

For a finite link set Lambda and original exterior configuration eta define

\[
 \gamma_\Lambda(dU_\Lambda\mid\eta)=
 \frac{\exp(2\sum_{S\cap\Lambda\ne\varnothing}v_S(U_\Lambda\eta))dU_\Lambda}
 {\int\exp(2\sum_{S\cap\Lambda\ne\varnothing}v_S(V_\Lambda\eta))dV_\Lambda}.
                                                               \tag{S4}
\]

S1 makes this sum uniformly absolutely convergent, and the denominator is positive. These are the limits of the actual finite-vacuum conditional densities; no independent density is assigned to the infinite Haar product.

Changing only exterior edge f changes the original single-edge log density at e by a function Delta of oscillation at most 8 sum_(S containing e,f)||v_S||_infinity. For the actual interpolating probabilities p_t proportional to exp(t Delta)p_0,

\[
 \frac12\int|\partial_t p_t|
 =\tfrac12 E_{p_t}|\Delta-E_{p_t}\Delta|
 \le\tfrac14\operatorname{osc}\Delta.                  \tag{S5}
\]

To verify the last inequality without omitting its constant, let m<=Delta<=M and mu=E Delta. The chord bound for the convex function |x-mu| yields E|Delta-mu|<=2(mu-m)(M-mu)/(M-m)<=(M-m)/2. The constant case has both sides zero. Consequently an actual influence majorant is

\[
 c_{ef}=2\sum_{S\ni e,f}\|v_S\|_\infty\quad(e\ne f),
 \qquad c_{ee}=0.                                       \tag{S6}
\]

Every denominator of S4 is included in the interpolation derivative. S1, |S|-1<=3p and S3 prove

\[
 \boxed{\sup_e\sum_f c_{ef}\le q(\xi):=
          2\xi r'(\xi)=\frac{64\xi}{\sqrt{1-256\xi/3}}.} \tag{S7}
\]

The actual strict domain q<1 is

\[
 \boxed{0<\xi<(\sqrt{13}-2)/192,
 \qquad g^4>\tfrac{16}{3}(2+\sqrt{13}).}                 \tag{S8}
\]

Every g^2>=11/2 lies in this domain. At its stated closed benchmark,

\[
 q^2\le12288/12947<1.                                   \tag{S9}
\]

The unweighted source is used with its full order-dependent size information; no bound on support cardinality was discarded.

## S3. Uniqueness and convergence of the actual measures

Here is the complete finite comparison underlying the volume statement. In a finite set Lambda, update one original link uniformly using its exact conditional density S4. Each finite conditional measure is invariant under that update by Fubini. Couple two such chains with different exterior configurations, using maximal coupling of their original link conditional densities. The probability of disagreement at the selected link is exactly its total-variation distance. Let p_e(t) be the disagreement probabilities and b_e=sum_(f outside Lambda)c_ef. The complete vector inequality is

\[
 p(t+1)\le[(1-1/|\Lambda|)I+C_\Lambda/|\Lambda|]p(t)+b/|\Lambda|.
                                                               \tag{S10}
\]

The matrix has maximum row sum at most 1-(1-q)/|Lambda|. Telescoping an original cylinder function F over disagreeing links, iterating S10, and taking t to infinity give

\[
 |\gamma_\Lambda F(\eta)-\gamma_\Lambda F(\eta')|
 \le\sum_{e\in\operatorname{supp}F}\operatorname{osc}_e(F)
              [\sum_{j\ge0}C_\Lambda^j b]_e.            \tag{S11}
\]

The initial error tends to zero by the strict row bound; no stationarity of the joint coupling is assumed. As Lambda exhausts the original countable lattice, b_e->0 for every fixed edge and b_e<=q. Every fixed power term tends to zero by dominated convergence of the summable nonnegative rows; the remainder after j=J is bounded by q^(J+2)/(1-q). Thus S11 tends to zero uniformly in the two exterior configurations for each fixed F.

Extend rho_L dU inside its original box by independent original Haar factors outside. Compactness of the countable configuration product supplies weak subsequential limits. The finite-vacuum conditional on Lambda differs from S4 only by original supports not contained in E_L. Its omitted log-density is bounded by 2 sum_(e in Lambda) sum_(S containing e,S not contained E_L)||v_S||, which tends to zero by S1 and coefficient compatibility. S5 then gives uniform convergence of these kernels in total variation. Their action on continuous functions is continuous; conditional integration passes to any weak limit, and a monotone-class argument extends the exterior tests. Every weak limit therefore has S4 as its actual conditional kernels.

Integrate S11 over the exterior laws of two such limiting probabilities. They agree on every cylinder function and hence are equal. This proves a unique measure nu and convergence of the whole sequence rho_L dU to nu on S8. Its gauge action remains the original vertex action, passed through each finite invariant measure.

## S4. Complete drift matrix, including all mixed derivatives

Set b_e^infinity=X_e sum_(S containing e)v_S, with its three original components. The exact order-p spin restriction and G7 give

\[
 3j_e\sum_fj_f\le3(p/2)(2/3)c(j)=p c(j).
\]

Thus the complete derivative majorant

\[
 B_{ef}=3\sum_{p,S\ni e,f,j}\xi^p j_ej_f\|A_{S,j,[p]}\|_1
\]

is symmetric, nonnegative, and obeys

\[
 \boxed{\sup_e\sum_fB_{ef}\le\frac{32\xi}{\sqrt{1-256\xi/3}}.} \tag{S12}
\]

The same bound and the tail S3 retain all cross-link derivatives and their spatial tails. Each X-coordinate group translation is an isometry, and its diameter is 2pi. Integrating the derivative along the original group paths proves

\[
 |b_e(U)-b_e(V)|\le\sum_fB_{ef}\operatorname{dist}_X(U_f,V_f). \tag{S13}
\]

On each coefficient the three-vector derivative has norm at most sqrt(3)j_e||A||_1. G6 bounds this by sqrt(3)c||A||_1/6. If the original line-graph ball of radius 3P around e is contained in E_L, source compatibility therefore gives

\[
 t_e(L):=\|b_e^\infty-b_e^L\|_\infty
 \le\frac{\sqrt3}{6}\sum_{p>P}a_p,
 \qquad t_e(L)\le\frac{\sqrt3}{6}r.                      \tag{S14}
\]

For e outside the box set b_e^L=0. The second bound still applies. All t_e(L) tend to zero at fixed e. No full-volume norm convergence of a density is asserted.

## S5. Direct convergence of the original dynamics

Use the original link diffusion

\[
 dU_e^L=\sqrt{2\kappa}\sum_\alpha T_\alpha U_e^L\circ dB_{e,\alpha}
        +2\kappa\sum_\alpha b_{e,\alpha}^L(U^L)T_\alpha U_e^Ldt,
                                                               \tag{S15}
\]

with free copies outside the box and the same countable Brownian family for all boxes. Its generator is -A_L on inside functions by G2. Let R_e be the free group Brownian solution with R_e(0)=I and write U_e^L=R_e V_e^L. The Stratonovich product rule gives the original random ordinary equation

\[
 \dot V_e^L=2\kappa
      R_e^{-1}\bigl(\sum_\alpha b_{e,\alpha}^L(U^L)T_\alpha\bigr)R_e V_e^L.
                                                               \tag{S16}
\]

Conjugation rotates the three coefficient coordinates orthogonally. Comparing two such ordinary equations by the triangle inequality after a common infinitesimal group translation gives, for z_e=dist_X(U_e^L,U_e^M),

\[
 z_e(t)\le2\kappa\int_0^t
       [(Bz(s))_e+t_e(L)+t_e(M)]ds.                     \tag{S17}
\]

At the cut locus the same upper-Dini-derivative bound follows from the metric triangle inequality. Iterating S17 with w=t(L)+t(M) gives

\[
 \sup_{s\le t}z_e(s)
 \le\sum_{j\ge0}\frac{(2\kappa t)^{j+1}}{(j+1)!}(B^jw)_e. \tag{S18}
\]

The iterated remainder is at most 2pi(2kappa B_*t)^N/N! and vanishes. Every fixed matrix power tends to zero by S12–14, and the exponential tail is uniform on compact time intervals. The convergence is deterministic and uniform in the initial configuration and common Brownian paths. It constructs the limiting process; S17 with w=0 proves its pathwise uniqueness.

For every smooth cylinder F, S18 proves uniform convergence of T_L(t)F to T(t)F on compact physical time intervals. Smooth cylinders are dense in the continuous functions on the compact countable product, so positivity and contraction extend the convergence and the semigroup law to that space. The generator on cylinders is the unchanged expression

\[
 A_\infty F=\kappa K F-2\kappa\sum_{e,\alpha}b_{e,\alpha}^\infty X_{e,\alpha}F.
                                                               \tag{S19}
\]

Its uniform bound on each fixed cylinder also proves strong continuity. On the conditional domain S8, finite reversibility and S3's proved measure convergence pass to the limit, making T(t) a strongly continuous self-adjoint Markov contraction semigroup on L^2(nu). Sections S11 and S13 prove the measure convergence on the remaining subcritical and critical domain, and then use this same reversibility argument. The resulting generator is nonnegative and self-adjoint; its construction uses the displayed finite dynamics and their actual limit.

## S6. Full physical gap in the unique volume limit

For a fixed physical cylinder F, its support is inside every sufficiently large E_L. The original finite semigroup then acts only inside, so the full PHYSICAL estimate G26 applies before passage to the limit. Uniform semigroup convergence and weak measure convergence give

\[
 \|T(t)(F-\nu F)\|_{L^2(\nu)}
 \le e^{-\kappa d_{\rm phys}t}\|F-\nu F\|_{L^2(\nu)}.
\]

Gauge averaging of dense cylinder approximations proves their density in the physical L^2 space. Hence

\[
 \boxed{A_\infty|_{L^2_{\rm phys}(\nu)\cap1^\perp}
           \ge\kappa d_{\rm phys}(\xi).}                 \tag{S20}
\]

The scalar limit retains G27. Its extended finite outside factors have the original free scalar gap 3kappa/4, at least kappa d_sc; this proves the scalar semigroup bound too. No scalar estimate is substituted for S20's sharper physical input.

All original time-ordered local correlations converge by repeated uniform semigroup convergence and the same vacuum measure limit. The exact map from the correlation Hilbert space is [O,t]->T(t)(O-nu O); its pairings equal the original limiting correlations, and its zero-time physical cylinder range is dense. Its inverse is completion of those same cylinder vectors. This identifies the complete constructed physical generator and preserves its raw inner product.

For the elementary loop, the predecessor's original pointwise density comparison and exact gradient give

\[
 \operatorname{Var}_\nu(F)\ge e^{-128\pi\xi},\quad
 q_\infty(F-\nu F)\le4\kappa,
\]
\[
 e^{-128\pi\xi}-4\kappa t\le C_F(t)
       \le C_F(0)e^{-\kappa d_{\rm phys}t}.              \tag{S21}
\]

Thus the constructed centered physical space contains a quantitatively nonzero finite-energy vector. The uniform first moment and the full gap retain, respectively, zero energy-infinity mass and zero zero-energy mass in its centered spectral measure. These endpoint statements are at fixed a,g in S8.

## S7. Source estimates and original response kernels

The source quotient of G4 and the labelled-assembly quotient of G9–12 retain their actual kernels. G30 bounds the original physical gradient primitive after their coefficient estimates are returned through the explicit eigenfunction map. The physical restriction in G31 carries the unchanged Schur residual and minimum-section identities to the stronger inverse bound. This includes the original section correction; a prescribed local trial is not relabelled a minimum section without that correction.

The new finite-band map B24–25 preserves its full original Gram G_xi. The Fourier transform B26 is an additional exact map on the calculated second coefficient, with both inverse laws and its original momentum measure. It does not identify a finite coefficient window with all physical states. Full physical coercivity came from G26 on every eigenfunction and then on the whole form domain.

## S8. The admitted source at the closed endpoint

At xi=3/256 the local coefficient sum and the original finite-box vacuum remain well-defined by G19. It gives a uniform algebraic tail and fixed-edge drift convergence through S14. The derivative series S3 and the Dobrushin bound S7 are not assigned finite values there. The conditional-coupling proof in S2–6 uses exactly S8. The additional full-domain argument S10–14 below uses a different, explicitly derived semigroup estimate; it never assigns a finite value to the divergent derivative series at theta=1.

## S9. Original continuum path and the domains actually reached

Keep a_n=a_0 2^-n and c_n=g_0^-2+beta n log2, with g_n^2=1/c_n and beta>0. The full finite-regulator physical result G22 applies exactly for

\[
 c_n\le\sqrt3/8.                                       \tag{S22}
\]

The conditional-comparison volume construction in S2–6 has c_n^2<3/[16(2+sqrt13)]; its closed benchmark is c_n<=2/11. The stronger construction in S10–14 reaches the full closed domain S22. The isolated physical band has c_n<sqrt3/10. These domains are larger than the preceding c_n<=1/15 domain, but c_n increases without bound, so none is assigned to the full n->infinity path.

At a fixed admissible g, the a_n->0 limit has

\[
 \Delta_n\ge (2g^2/a_n)d_{\rm phys}\longrightarrow\infty. \tag{S23}
\]

The original bounded centered positive-time correlations then vanish by the displayed exponential estimate, with any retained nonzero zero-time mass in the energy-infinity endpoint. The physical second-band propagation coefficients in B29 also keep their actual powers of a and g. No energy multiplier has been selected to force a continuum dispersion.

The completed output is a sharper full physical primitive bound, an actual interacting plaquette band with a uniform analytic error, and unique spatial vacuum/dynamics on an enlarged explicit coupling domain. A nontrivial smooth four-dimensional continuum field and a finite positive continuum mass remain unevaluated. The next selected original quantity is the higher-order physical band/response under the original changing-coupling refinement; all kernels and original energy units remain attached.

## S10. Volume-independent mixing from the original Fourier dynamics

This argument strengthens the preceding conditional route. It holds on the complete CLOSED source domain 0<=xi<=3/256, at each finite box, without a hypothesis on q(xi).

For a smooth cylinder F in a finite box write the actual finite semigroup as

\[
 T_L(t)F=c(t)1+y(t),\quad c(t)=\int_H T_L(t)F,\quad y(t)=Q_H T_L(t)F.
\]

The Fourier spaces X_0,Y_0 are exactly G23. Smoothness of the original finite heat equation makes y(t) differentiable in X_0, with y(t) and its derivative controlled in all finite-volume smooth norms. In particular it is continuous in Y_0. This regularity follows directly from the original self-adjoint compact spectral resolution and elliptic regularity, with a smooth initial function; no volume-uniform regularity constant is required.

Its exact coefficient equation is

\[
 y'(t)=-\kappa K_L y(t)+2\kappa Q_H\sum_i(X_iv_L)X_i y(t).
                                                               \tag{S24}
\]

For f in Y_0, the right derivative at h=0 of sum_j |1-h kappa c(j)| ||A_j(f)||_1 equals -kappa||f||_(Y_0). Dominated convergence is justified by the summable bound kappa c(j)||A_j(f)||_1. Apply the triangle inequality to S24's first-order difference in X_0 and use G23. The upper-right derivative therefore obeys

\[
 D^+\|y(t)\|_{X_0}\le-\kappa(1-\epsilon)\|y(t)\|_{Y_0}. \tag{S25}
\]

The norm is locally absolutely continuous because y is X_0-differentiable. Integrating the inequality and using ||y||_Y>=c_*||y||_X gives

\[
 \|y(t)\|_{X_0}\le e^{-\kappa c_*(1-\epsilon)t}\|Q_HF\|_{X_0},
\]
\[
 \kappa(1-\epsilon)\int_t^\infty\|y(s)\|_{Y_0}ds
       \le\|y(t)\|_{X_0}.                               \tag{S26}
\]

Here c_*=3 for physical F by G8, and c_*=3/4 for unrestricted scalar F. The mean equation retains the original constant contribution:

\[
 c'(t)=2\kappa\int_H\sum_i(X_iv_L)X_i y(t),\qquad
 |c'(t)|\le\kappa\epsilon\|y(t)\|_{Y_0}.                \tag{S27}
\]

The full coefficient product bound before Q_H proves the latter inequality with the same epsilon. S26 proves that c(t) tends to a constant c_infinity and that

\[
 |c_\infty-c(t)|\le\frac{\epsilon}{1-\epsilon}\|y(t)\|_{X_0}.
\]

The actual finite vacuum is invariant under T_L; uniform convergence to c_infinity therefore identifies c_infinity=int rho_L F. Combining these identities proves the volume-independent SUPREMUM-norm estimate

\[
 \boxed{
 \|T_L(t)F-\langle F\rangle_{\rho_L}\|_\infty
 \le\frac{\|Q_HF\|_{X_0}}{1-\epsilon}
        e^{-\kappa c_*(1-\epsilon)t}.}
                                                               \tag{S28}
\]

Every function, original Haar mean, vacuum mean, and constant drift term is retained. The initial Fourier norm of a fixed cylinder is identical in every larger box: all additional spin indices are trivial with dimension one and Haar integral one. Consequently S28 has no volume-dependent prefactor. For the actual elementary plaquette trace its initial norm is exactly 8, by G14.

This proof uses the actual finite semigroup, rather than assuming that an auxiliary Banach semigroup agrees with it. The coefficient estimates were applied to its smooth solution, and S27 reconstructs its constant component explicitly.

## S11. Full subcritical volume convergence without the conditional row restriction

For every theta<1, the drift row bound S12 is finite, regardless of the value of the conditional row bound q. The direct dynamical construction S13–19 therefore gives uniform convergence of T_L(t)F on compact time intervals for every cylinder F throughout 0<=xi<3/256.

Fix a common original configuration U. By S28,

\[
 |\langle F\rangle_{\rho_L}-\langle F\rangle_{\rho_M}|
 \le |T_L(t)F(U)-T_M(t)F(U)|
       +\frac{2\|Q_HF\|_{X_0}}{1-\epsilon}
                          e^{-\kappa c_*(1-\epsilon)t}. \tag{S29}
\]

First let L,M grow at fixed t; the first term tends to zero. Then let t grow. This proves Cauchy convergence of the entire vacuum expectation sequence on every matrix-coefficient cylinder polynomial. Positivity and the uniform supremum bound extend the limit to a probability nu on the compact countable configuration space. The same convergence holds for all continuous functions by density. Passing S28 to the limit gives

\[
 \|T(t)F-\nu F\|_\infty
 \le\frac{\|Q_HF\|_{X_0}}{1-\epsilon}
               e^{-\kappa c_*(1-\epsilon)t}.            \tag{S30}
\]

Every invariant probability of this limiting semigroup has the same expectation of every such F by S30, hence equals nu. This proves uniqueness of its invariant vacuum measure. Reversibility, self-adjointness, physical density, and all time-ordered correlations return by the exact arguments S5–6. Thus S20 holds for every subcritical 0<xi<3/256, not merely on the smaller S8 domain.

## S12. An explicit coupling modulus for the full original semigroup and vacuum

Treat (kappa,xi) as the two retained positive operator coefficients. Their inverse physical parameter map is

\[
 g^2=1/(2\sqrt\xi),\qquad a=1/(\kappa\sqrt\xi).
                                                               \tag{S31}
\]

For xi>0 the two displayed maps are mutual inverses by substitution. At xi=0 only the auxiliary operator kappa K_L is used; no finite physical a,g are assigned by S31. The identity on original link-index configurations compares two such coefficient pairs. It changes neither a link word nor a matrix coefficient, and S31 records its effect on the physical parameters. In the following comparison kappa is fixed and no energy factor is divided out.

For 0<=xi<=eta<=3/256, the full positive coefficient majorant yields

\[
 \|v_L(\eta)-v_L(\xi)\|_{\mathrm{loc},1}
       \le r(\eta)-r(\xi).
                                                               \tag{S32}
\]

Indeed expand each original coefficient in powers and sum (eta^p-xi^p)||v_[p]||. G16 evaluates their entire sum. This also holds at the endpoint by G19.

Differentiate T_(L,eta)(t-s) T_(L,xi)(s)F on the original smooth source. Integrating the product rule gives the full Duhamel formula with difference generator

\[
 2\kappa\sum_i X_i(v_L(\eta)-v_L(\xi))X_i.
\]

The Markov contraction in the target supremum norm, G23 before its mean projection, and S26 on the xi evolution give

\[
 \boxed{
 \sup_{t\ge0}\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
 \le\frac{\epsilon(\eta)-\epsilon(\xi)}{1-\epsilon(\xi)}
                         \|Q_HF\|_{X_0}.}              \tag{S33}
\]

Every density and drift in this expression is its own actual finite vacuum. The bound is independent of the original box size and of t. Sending t to infinity with S28 proves the same bound on |<F>_(rho_L,eta)-<F>_(rho_L,xi)|. This supplies a quantitative coupling comparison, not an assertion of uniform analytic control beyond the constructed interval.

## S13. The closed source endpoint has a unique spatial vacuum and dynamics

Put xi_c=3/256 and s_xi=sqrt(1-256xi/3). The modulus in S33 becomes exactly

\[
 \frac{\epsilon(\xi_c)-\epsilon(\xi)}{1-\epsilon(\xi)}
       =\frac{s_\xi}{1+s_\xi}\longrightarrow0.
                                                               \tag{S34}
\]

For fixed xi<xi_c the complete subcritical volume convergence was just proved. Compare two finite boxes at xi_c by inserting their evolutions at xi; S33 bounds the two outer differences by twice S34 times ||Q_HF||_X, uniformly in physical time. Let L,M grow first, then xi increase to xi_c. This proves uniform convergence on compact time intervals of the entire critical family T_(L,xi_c)(t)F.

The limit preserves the semigroup law, positivity and constants. Its strong continuity follows from the finite generator bound on each cylinder: b_e^L is uniformly bounded by sqrt(3)r/6 even at the endpoint, and the cylinder has finitely many original derivatives. G19 and S14 give convergence of each drift coefficient. Thus the limit generator on cylinders is the original expression S19. This argument does not assign a finite value to the divergent derivative majorant S3 at the endpoint, and does not claim the S16 pathwise-uniqueness proof there. It constructs the critical dynamics as the unique uniform limit of the original finite semigroups.

The finite mixing estimate S28 remains valid at epsilon=1/2. The Cauchy argument S29 now proves the full critical vacuum-measure limit. S30 makes this measure the unique invariant probability of the limiting semigroup. Finite reversibility passes to the limit and supplies the self-adjoint generator and its complete physical representation. The spectral, raw-metric, nontriviality and correlation arguments of S6 apply unchanged.

Consequently the final unique-volume domain is the full CLOSED domain

\[
 \boxed{
 0<\xi\le3/256,\qquad g^2\ge8/\sqrt3,
 \quad A_\infty|_{\mathrm{phys}\cap1^\perp}
           \ge\tfrac32\kappa(1+\sqrt{1-256\xi/3}).}      \tag{S35}
\]

The same supremum-norm mixing and coupling modulus hold on the limiting cylinder algebra by passage through the proved maps. Both the source tail and its physical return are controlled at the endpoint.

## S14. Final continuum scope

The full spatial statement S35 reaches c_n<=sqrt3/8 on the original running path, including equality. S8 remains the smaller domain of the separately proved conditional-influence comparison. The physical band and Cauchy-remainder domains remain those in B1 and B10. For beta>0, c_n still grows beyond sqrt3/8 after finitely many steps. No estimate in this continuation assigns the strong-coupling source or its band to that later part of the path.

The new quantitative coupling estimate S33 is an explicit tool for continuing the original Hamiltonian family; it does not assert extension to g approaching zero. The four-dimensional smooth-continuum field, a finite positive continuum mass, and the required change in physical scaling remain unevaluated. The completed results keep their full physical domains and all original observables, source relations, state norms and generator maps.


---

# Chapter 11 — 20260915-uniform-gap-zero-shift / HEAT_BATH_GAP.md

Original text path: `workbench/yang-mills/continuations/20260915-uniform-gap-zero-shift/HEAT_BATH_GAP.md`.

# Full-domain gap through the actual vacuum conditionals

15 September 2026. This is the final quantitative strengthening in the present
continuation. It uses the exact original plaquette coefficient O1–2 and the
same convergent labelled source, but returns its information to the original
Hamiltonian through conditional variances. All operators below act on the
actual finite-vacuum Hilbert space. Every link, physical coefficient, vacuum
factor and scalar ground energy remains those of U3–4.

The completed domain is

    g^2>=15,  0<xi=1/(4g^4)<=1/900,  a>0, L>=2.           (H1)

There is no assumption about an unevaluated gap in this domain. The argument
below proves the full physical estimate, the zero-shift inverse bound and the
spatial-volume return with explicit constants.

## H2. The same exact source converges on this larger closed domain

Use w=5/4, B_xi=(625/8)xi and the bilinear coefficient bound 8/3 from O3–6.
Take the fixed radius R_15=9/64. At the endpoint xi=1/900,

    B_xi+(8/3)R_15^2=25/288+27/512=643/4608
                          <648/4608=R_15,
    (16/3)R_15=3/4<1.                                    (H2)

Thus the actual nonlinear source map preserves this ball and contracts by
at most 3/4. The complete same-source Picard proof in O3 gives the original
positive vacuum, including its recovered scalar and energy, throughout H1.
The exact coefficient series also gives the sharper actual radius

    r_xi=(3/16)(1-sqrt(1-(2500/3)xi))<=9/64,
    theta_xi=(2500/3)xi<=25/27<1.                         (H3)

Every coefficient is the original coefficient of U26 and V1. Positivity and
ground-state uniqueness identify the assembled function with the same psi_L;
no auxiliary vacuum is used. The tail B_xi theta_xi^P/(1-theta_xi) remains a
proved summable bound for the full series. The curvature formula O13 retains
its own domain; the physical lower bound below is derived independently of
its sign.

## H3. Conditional projections on the original interacting Hilbert space

For an original edge e, let P_e be the actual conditional expectation given
all link variables except U_e, in rho_L dU_L. Its displayed density is

    p_e(U_e|eta)=rho_L(U_e,eta)/int rho_L(V_e,eta)dV_e.      (H4)

Fubini proves P_e=P_e*=P_e^2 on the original L2(rho_L dU_L). The two retained
form identities are

    <f,(I-P_e)f>_rho=||f-P_e f||_rho^2
                   =E_rho Var_(p_e)(f),
    B_L=sum_e(I-P_e).                                    (H5)

This bounded self-adjoint nonnegative B_L uses dimensionless heat-bath rates.
It is related to the original energy operator by the explicit form comparison
H11 below, on the common original state space. The physical kappa is not
assigned to these auxiliary rates or removed from that comparison.

The exact conditional densities from the same support potentials are V5.
Their original influence majorant V6 now satisfies, directly from H3,

    q_xi=(65536/9375)r_xi<=3072/3125<1.                   (H6)

The coefficient calculation is O24. No Haar marginal is substituted here:
c_ef bounds the TV difference of the actual p_e when only the exterior U_f
changes. It is obtained by differentiating the full exponential conditional
ratio; every support containing e and f is counted.

## H4. A complete spectral proof for the actual conditional operator

Write N=|E_L| and P=N^-1 sum_e P_e. For a real continuous f let osc_i f be its
oscillation when only the original edge i is varied. The actual conditional
comparison yields, for i!=e,

    osc_i(P_e f)<=osc_i f+c_ei osc_e f,
    osc_e(P_e f)=0.

To verify the first line, compare the two original conditional integrals.
The change of the integrand with fixed integration variable is bounded by
osc_i f. The change of its conditional probability is bounded by c_ei; a
real function with range length osc_e f pairs against this signed zero-mass
probability difference by at most c_ei osc_e f. This retains the TV convention
one half of the L1 distance and needs no new factor. Averaging gives

    osc(Pf)<=[(1-1/N)I+C^T/N]osc(f).                      (H7)

The sum of the components contracts by at least
1-(1-q_xi)/N, since the row sums of C are at most q_xi. The bounded exponential
has the literal Poisson series

    exp(-t B_L)=e^(-Nt)sum_(k>=0)(Nt)^k P^k/k!.

Positivity, the componentwise inequality H7 and that absolutely convergent
series give

    ||exp(-t B_L)(f-rho_L f)||infinity
        <=e^(-(1-q_xi)t)sum_i osc_i f.                   (H8)

The total oscillation of any function on this finite product is at most the
sum of its single-edge oscillations by telescoping original coordinates;
its mean lies in its real range. These facts prove H8. Complex functions
are handled by their real and imaginary parts; the exponential rate stays
the same. The prefactor is finite for each finite graph, and is not claimed
to be independent of its size.

For a centered continuous f, apply the spectral resolution of the bounded
self-adjoint B_L. Positive spectral mass below 1-q_xi-epsilon would bound
||exp(-t B_L)f||_2^2 below by that mass times
exp(-2(1-q_xi-epsilon)t), contradicting H8 as t increases. Thus its spectral
measure gives zero mass to [0,1-q_xi). Centered continuous functions are
dense in centered L2 of the original smooth positive probability. The same
spectral projection therefore vanishes on that whole space. We have proved

    <f,B_L f>_rho >=(1-q_xi)Var_rho f                     (H9)

for every original L2 function. This proof did not require compact resolvent
of B_L, a finite spin cutoff, or a uniform mixing prefactor.

## H5. Return to the complete original Hamiltonian form

The actual pointwise estimate already proved in the predecessor is

    |X_e log psi_L|<=2r_e xi<=8xi.

The original X-coordinate path diameter of SU(2) is 2pi. Therefore the
logarithm of the actual conditional density H4 has oscillation at most

    beta_xi=32pi xi,
    (sup p_e)/(inf p_e)<=exp(beta_xi).                   (H10)

The conditional denominator is independent of U_e, so it has zero derivative
in this step. The original single-link Haar Casimir has first positive
value 3/4. Completeness of the original matrix coefficients proves its full
Poincare inequality. For a fixed exterior configuration retain m_e=inf p_e,
M_e=sup p_e, and the two actual probability means. Then

    Var_(p_e)f
       =inf_c int p_e |f-c|^2
       <=M_e inf_c int_H |f-c|^2
       <=(4/3)M_e int_H sum_alpha |X_e,alpha f|^2
       <=(4/3)(M_e/m_e)int p_e sum_alpha|X_e,alpha f|^2.

The identities and inequalities use the same original function and both
explicit measures. They do not replace either mean or pairing by the other.
Integrating over all original exterior variables and summing gives

    <f,B_L f>_rho <= [4 exp(beta_xi)/(3kappa)] q_A_L(f).   (H11)

This is the promised typed comparison: the identity on the original smooth
functions, extended to their original form domain, relates the bounded
conditional form and the full ground-relative Hamiltonian form. It preserves
the state Gram and retains the physical factor kappa=2g^2/a.

Combining the two proved inequalities H9 and H11 establishes

    q_A_L(f)>=kappa d_xi^HB Var_rho f,
    d_xi^HB=(3/4)(1-q_xi)exp(-32pi xi)>0.                (H12)

Density extends it from smooth functions to the original H1 form domain.
Multiplication by psi_L is the original Haar-unitary ground-state transform.
Thus H12 is a lower bound for the full scalar excitation spectrum, and also
for the complete physical spectrum. It includes every regulator-dependent
choice of physical state; a finite observation window was not used.

There are two convenient fully rational closed-domain values. On all of H1,
use q_xi<=3072/3125 and 32pi xi<176/1575. The elementary inequality
e^(-x)>=1-x and the original pi<22/7 then give

    d_xi^HB >=(3/4)(53/3125)(1399/1575)
             =74147/6562500 >1/100,       g^2>=15.       (H13)

On the stronger subdomain g>=4, xi<=1/1024. Use R_4=7/64; the same literal
source map has

    B_xi+(8/3)R_4^2<=625/8192+49/1536=2659/24576
                           <2688/24576=R_4,
    (16/3)R_4=7/12<1.

Consequently q_xi<=7168/9375 and 32pi xi<11/112. The same exponential
inequality gives

    d_xi^HB >=(3/4)(2207/9375)(101/112)
             =222907/1400000 >3/20,       g>=4.          (H14)

In original physical units these are

    Delta_L >=kappa/100=g^2/(50a),            g^2>=15,
    Delta_L >=3kappa/20=3g^2/(10a),           g>=4,       (H15)

with the stronger actual value H12 retained at every coupling. Both hold for
every original L>=2 and a>0. No original operator term or energy origin is
changed in any of these comparisons.

## H6. An explicit factorization of the original cohomological primitive

Let d_X f=(X_i f)_i, with the original energy pairing
||d_X f||_1^2=kappa int rho sum|X_i f|^2. Define the bounded conditional
source map on L2(rho)

    d_B f=(f-P_e f)_e,
    ||d_B f||^2=<f,B_L f>_rho.

H9 proves its kernel is exactly the constants and its range is closed.
On that actual range set

    p_B(d_B f)=f-rho f,
    ||p_B||<=(1-q_xi)^(-1/2).

The actual map from the physical gradient source is

    T:ran(d_X|H1)->ran d_B,
    T(d_X f)=d_B f,
    ||T||<=[4exp(beta_xi)/(3kappa)]^(1/2).                (H16)

It is well-defined because changing f by a constant changes neither source;
the norm estimate is exactly H11. Its inverse on its actual image is
z->d_X p_B z. Both inverse laws follow from p_B d_B f=f-rho f. No bounded
inverse on an unspecified larger range is assumed. The primitive of the
original gradient complex now has the exact factorization

    p_X=p_B T,
    ||p_X||^2<=1/(kappa d_xi^HB).                         (H17)

The source and target maps, the kernels and the original physical energy
pairings are explicit. In the support-labelled reconstruction these are the
same incoming original-gradient relations and their actual primitive; the
conditional comparison provides their quantitative bound without deleting
any retained relation or replacing the original Hilbert metric.

## H7. Zero shift, canonical section, and actual numerical return

For the original loop observation, K=ker E consists of zero-mean functions
in rho. Its original restricted closed form therefore represents

    D>=kappa d_xi^HB,
    ||D^-1||<=1/(kappa d_xi^HB).                          (H18)

All moment, residual and primitive formulas U31–50 remain literal identities
for their original functions. The pointwise precursor estimates are proved
for xi<=3/64, which contains H1. To evaluate their error on the whole present
domain, use H18 in place of the baseline inverse bound in a7,E_Z. Specifically

    a7=r_z^2/d_xi^HB,
    E_M^HB=(a1+...+a6+a7)/xi^2,
    E_Z^HB=delta z_*+(eta Z_*)^2
          +2n_z r_z/(d_xi^HB xi)+(r_z/(d_xi^HB xi))^2.     (H19)

Every other quantity is the same original U38–40 value. At the actual
xi=10^-8, g^2=5000, kappa=10000/a, the rational interval evaluation gives

    d_xi^HB>0.74999514999,
    E_M^HB<0.0000094,
    E_Z^HB<0.00000319,
    r_z^2/(d_xi^HB xi^2)<0.0000000000142.                (H20)

Thus

    |M0-(8/39)kappa xi^2|<0.0000094 kappa xi^2,
    |||D^-1W||^2-(196/4563)xi^2|<0.00000319 xi^2.          (H21)

The full nonnegative canonical quotient-plus-section-correction cost U45 is
less than 0.0000000000142 kappa xi^2. This bound retains both its terms and
the actual primitive, not only a support flag.

The raw state G, kinetic K0 and one-state variational upper bound U49–50
remain. The lower bound is now the full-domain H12. Their return is

    0.74999514999 kappa <=Delta_L<(3+5/10^13)kappa         (H22)

at the stated coupling, for every a,L. The endpoint directions have their
separate exact variational justifications; the trial-state lower endpoint
is not used to estimate the whole physical spectrum from below.

## H8. Full spatial-volume return on g^2>=15

The proof of `VOLUME_LIMIT.md` is now applied to the same support series with
the explicitly established source radius at most9/64. Every required estimate
is evaluated here, so the return has no new unproved premise:

    sum_(S containing e)||v_S||infinity <=(16/15)r_xi,
    sum_f c_ef <=q_xi<=3072/3125<1,
    sum_f B_ef <=(384/125)r_xi<=54/125,
    coefficient tail <=B_xi theta_xi^P/(1-theta_xi),
    theta_xi<=25/27<1.                                  (H23)

V1's exact cutoff identity is independent of the auxiliary norm. V5–9 now
have the strict influence factor3072/3125, so their full coupling proof
still gives one unique vacuum measure and full-sequence convergence. V14–18
use the actual complete drift matrix with row bound54/125; their exponential
comparison converges on every finite physical-time interval without needing
positive curvature. The original local pointwise drift bound remains8xi.
Thus the direct full semigroup limit, original generator expression,
reversibility, gauge-invariant physical space and all time-ordered local
correlations V19–22 hold on H1.

In the finite spectral return use the full lower edge kappa d_xi^HB from H12.
The outside free-link gap is3kappa/4, and d_xi^HB<=3/4. The exact tensor
comparison in V20 therefore applies with this value. The limiting physical
vacuum representation has the same positive lower bound, a nonzero centered
loop vector, and zero atoms at both compactified energy endpoints. The
surjective time-symbol unitary is the one explicitly constructed in V22.
The original regulator-sequence kernel is not inferred to vanish from it.

The actual extensive energy estimate and its unique per-plaquette volume
limit V23–25 retain their original coefficients as well. Their pointwise
remainder domain contains H1, and their local drift convergence is H23.

The completed result is thus a fixed-spacing spatial infinite-volume
construction, from the original finite positive vacua, of the vacuum measure,
full original ground-relative dynamics, local time-ordered correlations,
extensive energy density and a positive physical spectral lower edge,
throughout g^2>=15. This supplies no ultraviolet change of the original
physical fields or coupling parameters.

For the retained running path c_n=g0^-2+beta n log2 and g_n^2=1/c_n, the
present closed domain is exactly c_n<=1/15. With beta>0 that is a finite
initial segment. At fixed admissible g and a->0, the physical bound scales
as1/a and the positive-time endpoint calculation U57 applies with d_xi^HB.
No four-dimensional smooth-continuum Yang–Mills field or finite positive
continuum mass is assigned to either parameter limit.

## Verification scope

The checker verifies the fixed-point balls, exact influence constants,
conditional projection matrices in a genuinely interacting rational fixture,
the full noncommuting heat-bath generator and its weighted spectral inequality,
the original single-link Haar factor3/4, exact physical comparison constants,
and the outward rational H20 intervals. The complete analytical proof is
H1–23 together with U1–57, O1–26 and V1–25. These finite checks are not a
formal proof or an independent external mathematical review. The method's
classical conditional-comparison antecedent is recorded in [DC] in the volume
note; the entire spectral and physical return used here is proved above.


---

# Chapter 12 — 20260915-uniform-gap-zero-shift / OPTIMIZED_DOMAIN.md

Original text path: `workbench/yang-mills/continuations/20260915-uniform-gap-zero-shift/OPTIMIZED_DOMAIN.md`.

# Exact plaquette coefficient and the sharper full-gap domain

15 September 2026. This sharpens, on the same original coefficients and
physical operators, the fully written construction in `RESEARCH_NOTE.md`.
It also returns the sharpened constants through every step of
`VOLUME_LIMIT.md`. The baseline estimates are preserved in those files for
comparison; the present formulas give the stronger domain and lower bound.

The actual coefficient recurrence, plaquette words, representations, product
Haar coordinates, vacuum, physical energy and observation maps are unchanged.

## O1. The original plaquette coefficient has trace norm exactly eight

Write the four independent original link variables in their word order:

    W_p=Tr(U1 U2 U3^-1 U4^-1).

The inverse entry of an SU(2) matrix is

    (U^-1)_(r,c)=(-1)^(r+c) U_(1-c,1-r), r,c in {0,1}.

It follows directly from det(U)=1, or from multiplication by the original
matrix epsilon=[[0,1],[-1,0]]. Keeping all four trace indices gives the
coefficient A in W_p=Tr(A(U1 tensor U2 tensor U3 tensor U4)):

    A_[(i1,i2,1-i2,1-i3),(i0,i1,1-i3,1-i0)]
        +=(-1)^(i0+i2),  i0,i1,i2,i3 in {0,1}.             (O1)

Every unlisted entry is zero. This formula is the complete original Fourier
coefficient, with the trace convention U6; there is no change in source mass.
For each fixed pair (i1,i3), the two possible rows (i2=0,1) and columns
(i0=0,1) form the block [[1,-1],[-1,1]]. Different pairs have disjoint row
sets and disjoint column sets. There are four such blocks and eight unused
rows and columns. These are explicitly permuted original row and column
indices, not chosen singular vectors.

Consequently A* A is positive, (A* A)^2=4A* A, and Tr(A* A)=16. The matrix
(A* A)/2 is positive and its square is A* A. Uniqueness of the positive
square root proves

    ||A||_1=Tr sqrt(A* A)=8.                              (O2)

The Haar norm check is Tr(A* A)/16=1, agreeing with the original plaquette
second moment. Any permutation into the fixed global order of edge tensor
factors conjugates A by the explicitly corresponding tensor permutation,
preserving O2. This proves the value for every original plaquette in the box.

## O2. A second auxiliary support norm, with its complete comparison

Put w=5/4. On the same labelled coefficient families in U9 define

    ||f||_w=max_e sum_(S containing e) w^|S|
                            sum_(j nontrivial)c(j)||A_(S,j)||_1. (O3)

The map between this coefficient space and U10 is the identity on each
original A_(S,j); its inverse is the same identity. On each finite original
graph their exact estimates are

    ||f||_w <= ||f||_2 <= (8/5)^|E_L| ||f||_w.             (O4)

This follows by comparing the displayed positive weights at each original
support label. The second factor retains its volume dependence. It is not
used to transfer a volume-uniform estimate. The physical L2 and energy
pairings have not been changed; O3 is an auxiliary absolute-convergence norm
for the exact same source coefficients and their assembly map.

Since w^|S union T|<=w^|S|w^|T|, the entire anchored calculation U12–14 gives,
with its original matrices and all generator components,

    ||B(f,h)||_w <= (8/3)||f||_w||h||_w.                  (O5)

O2 and the actual maximum of four incident plaquettes give the improved
source estimate

    ||v_[1] xi||_w <= B_xi,
    B_xi=4 w^4 *8 xi=(625/8)xi.                          (O6)

The factor c(j)=3 still cancels the original inverse Casimir 1/3. Every
weight and each of the four plaquette links remains explicit.

## O3. Sum the convergent majorant instead of replacing it by twice its input

Define the following actual scalars from the original coupling:

    theta_xi=(2500/3)xi,
    r_xi=(3/16)(1-sqrt(1-theta_xi)),
    0<xi<451/552960.                                    (O7)

This interval lies strictly inside theta_xi<1. Direct multiplication gives

    r_xi=B_xi+(8/3)r_xi^2,
    (16/3)r_xi=1-sqrt(1-theta_xi)<125/288<1.              (O8)

The closed r_xi ball is therefore preserved by the literal nonlinear map
f->v_[1]xi+B(f,f), and its difference bound is the strict constant in O8.
Starting at zero, the successive differences are bounded by that constant
to their iteration power times B_xi. Their sum converges in the complete
labelled norm. Passing in the bounded bilinear map proves the fixed equation;
the same difference inequality proves uniqueness in that ball.

Equivalently, the complete order coefficients satisfy the already proved
Catalan recurrence and now obey

    ||xi^p v_[p]||_w <= C_(p-1)(8/3)^(p-1) B_xi^p,
    sum_(p>=1) C_(p-1)(8/3)^(p-1) B_xi^p=r_xi.            (O9)

The equality follows from the scalar generating equation c=1+z c^2 and the
branch with constant coefficient one, on 4z<1. For a direct justification,
the Catalan convolution proves the equation coefficient by coefficient;
C_n<=4^n gives absolute convergence, and the positive solution continuous
at z=0 is (1-sqrt(1-4z))/(2z). Its omitted tail after order P is at most

    B_xi theta_xi^P/(1-theta_xi).                         (O10)

Every coefficient is the same exact coefficient as in U26. Thus on the
common convergence interval the labelled families themselves agree, including
the assembly-kernel data. The improved radius extends that original family;
it does not select another observation or another vacuum. The C2 convergence,
elliptic bootstrap, recovered scalar c_L and ground energy E0,L are precisely
the constructions U17–18, now applied to this convergent same-source series.
Their proofs identify the actual positive unit vacuum at every g in O7.

## O4. The complete second derivative and the full physical gap

The elementary integer maximum needed in the original row estimate is

    sup_(m>=1) (m+1)/(5/4)^m=256/125, attained at m=3,4.  (O11)

The ratio of successive terms is (4/5)(m+2)/(m+1): it exceeds one at m=1,2,
equals one at m=3, and is smaller afterwards. Substitution into the full
mixed-block estimate U18, before any diagonal entry is removed, gives

    ||S_u||op <= (384/125)r_xi.                          (O12)

The same bound holds for the nonnegative full derivative row majorant used
for the drift comparison. The original group coordinate Gamma2 calculation
U20–22 is unchanged. It consequently proves on the full centered scalar
form domain, and hence on its complete physical invariant subspace,

    Delta_L >= kappa d_xi^sharp,
    d_xi^sharp=1/2-(768/125)r_xi
             =(144/125)sqrt(1-(2500/3)xi)-163/250 >0.    (O13)

This is valid for every L>=2 and a>0 on the explicit domain O7. The upper
endpoint of O7 is obtained by exact squaring:

    1-(2500/3)(451/552960)=(163/288)^2,
    r_(451/552960)=125/1536.                             (O14)

No strict estimate is asserted at that endpoint. In the original coupling
coordinate the proved positive-gap interval is

    g^4>138240/451.                                     (O15)

A useful closed subinterval with a simple physical constant is

    g>=9/2  => xi<=4/6561,
    Delta_L >= (3/20)kappa =3g^2/(10a).                 (O16)

For this explicit domain the inequality is proved, rather than inserted as
an assumption: 1-theta_xi>=9683/19683, and
9683/19683>(401/576)^2. Multiplying the latter square-root bound by 144/125
and subtracting 163/250 gives a number strictly greater than 3/20.
The weak endpoint notation in O16 is therefore safe throughout the closed
g-domain. At larger g the original formula O13 retains its stronger value.

The exact primitive relation remains

    ||p_L||^2=1/Delta_L <=1/(kappa d_xi^sharp),
    p_L((X_i f)_i)=f, int rho_L f=0.                    (O17)

Its source/target pairing is the original physical one in U25, not O3.
All physical states, including regulator-dependent choices, are included in
O13. No finite trial-space lower bound has been substituted.

## O5. Return to the actual zero-shift moments and the canonical residual

The actual D of U31 is the same original conditional-kernel form restriction.
Every element of that kernel has zero mean in rho_L. Therefore

    D>=kappa d_xi^sharp,
    ||D^-1||<=1/(kappa d_xi^sharp).                       (O18)

The actual elementary-loop constructions U33–40 retain their original
forcing W, trial Y, remainder R=W-DY, raw G, kinetic K0, and coefficients
8/39 and 196/4563. The predecessor's pointwise log-vacuum remainder is proved
on xi<=3/64, which contains the entire domain O7. Thus the same explicit
expressions delta,eta,h_z,r_z,n_z and a1,...,a6 remain applicable. In a7 and
the restored-state error, replace the inverse bound by the proved O18:

    a7=r_z^2/d_xi^sharp,
    E_M^sharp=(a1+...+a6+a7)/xi^2,
    E_Z^sharp=delta z_*+(eta Z_*)^2
          +2n_z r_z/(d_xi^sharp xi)+(r_z/(d_xi^sharp xi))^2. (O19)

These are estimates in the original physical Hilbert pairing. They give

    |M0-(8/39)kappa xi^2|<=kappa xi^2 E_M^sharp,
    |||D^-1W||^2-(196/4563)xi^2|<=xi^2 E_Z^sharp.          (O20)

The exact canonical quotient/primitive energy identity U45 is unchanged,
and its full nonnegative error is at most kappa r_z^2/d_xi^sharp.

At the already specified actual coupling xi=10^-8, g^2=5000, kappa=10000/a,
outward rational square-root bounds prove

    d_xi^sharp>0.49999519998,
    E_M^sharp<0.0000094,
    E_Z^sharp<0.0000041,
    r_z^2/(d_xi^sharp xi^2)<0.000000000022.               (O21)

Thus all zero-shift intervals U41–50 remain valid with this sharper full-gap
lower endpoint. In particular the actual complete physical gap satisfies

    0.49999519998 kappa <= Delta_L < (3+5/10^13)kappa.    (O22)

The upper bound is still the actual one-state variational upper bound U49;
its direction and scope have not changed. The lower bound is from the full-
domain argument O13. The polynomial coefficients and actual-vacuum remainder
estimates have been retained separately in O19–20.

## O6. Complete return through the spatial-volume construction

The proof in `VOLUME_LIMIT.md` uses the actual coefficient recurrence,
absolute support bounds, a summed conditional influence below one, and a
summable drift derivative row bound. Each input is now evaluated explicitly
on O7; the following formulas replace only the auxiliary bounds in that
proof, on the exact same finite-volume vacua.

First, labelled coefficients are cutoff-compatible by V1, independently of
the auxiliary norm. Their complete w-weighted bound is r_xi. Thus

    sup_e sum_(S containing e)||v_S||infinity<=(16/15)r_xi. (O23)

Here c(j)>=3/4 and w^|S|>=5/4 were used directly. The original conditional
densities V5 consequently have the same uniformly absolutely convergent
meaning. Their original influence majorant V6 now obeys

    sup_e sum_f c_ef<=(65536/9375)r_xi<128/225<1.         (O24)

Indeed sup_(m>=1)(m-1)/(5/4)^m=4096/3125, attained at m=5,6, and multiplying
by 16/3 gives the first coefficient. Its endpoint value at r=125/1536 is
128/225. The finite heat-bath comparison V8–9 is therefore the same actual
comparison, with q=128/225 and its complete Neumann powers. The proof gives
uniqueness and full-sequence convergence of the original vacuum measure on
the entire sharper interval O7.

The full mixed drift matrix in V10 has row sum at most

    B_*=(384/125)r_xi<1/4.                               (O25)

Its long-distance rows are bounded by
(3/2)r_xi (m_d+1)/(5/4)^m_d, with m_d=max(3,d+1), by O11 and the original
connected-support argument. The drift approximation is supplied by the
complete coefficient tail O10. All original variables, vector fields and
Brownian coefficients in V12–18 remain fixed. Hence the direct dynamics,
its invariant measure, and every local time-ordered correlation converge
along the full box sequence just as proved there. In V20 substitute the
proved full-domain lower value kappa d_xi^sharp. This constructs the same
physical vacuum representation and gives its self-adjoint generator that
positive lower edge. Both compactified spectral endpoint atoms are zero at
fixed a,g, using the same local first-moment bound U51.

The scalar vacuum energy identity V23–25 is also unchanged: its pointwise
input xi<=3/64 contains O7, and its local drift convergence now uses O10.
Thus the original energy-per-plaquette limit and its finite explicit error
remain established on this larger domain.

Finally, the original simultaneous path keeps

    a_n=a0 2^-n, c_n=g0^-2+beta n log2, g_n^2=1/c_n,
    xi_n=c_n^2/4.

The exact new validity interval on that path is

    c_n < sqrt(451/138240).                              (O26)

For beta>0 only a finite initial part of that unbounded c_n path lies in this
proved domain. With fixed admissible g and a->0, the original physical lower
bound kappa d_xi^sharp diverges as 1/a; the positive-time collapse and the
retained infinite-energy endpoint in U57 follow with this same exact value.
No finite continuum mass or smooth four-dimensional field construction is
assigned to these parameter maps.

## Scope of verification

The checker constructs the complete original 16 by 16 Fourier coefficient,
checks its positive-square-root identity, and verifies the trace convention
against literal four-link SU(2) words using exact rational quaternions. It
checks the finite support norm comparisons, all extremal weight constants,
the exact quadratic majorant, domain endpoints, original physical factors,
and O21 with integer-square outward bounds. The general analytic arguments
and infinite-limit proofs are the written proofs U1–57 and V1–25 with the
explicit substitutions O1–26 above. Exact finite checks do not constitute a
new Lean build or an independent mathematical audit. No general-priority
claim is made for the Fourier, contraction, curvature or Gibbs methods.


---

# Chapter 13 — 20260915-uniform-gap-zero-shift / RESEARCH_NOTE.md

Original text path: `workbench/yang-mills/continuations/20260915-uniform-gap-zero-shift/RESEARCH_NOTE.md`.

# Volume-uniform physical coercivity and the actual zero-shift Wilson response


**Final completed estimate.** `HEAT_BATH_GAP.md` proves the full original
physical bound Delta_L>=kappa/100 for g^2>=15, and the stronger
Delta_L>=(3/20)kappa for g>=4. Its coupling-dependent value H12 controls
the actual zero-shift response and the unique full spatial-volume dynamics.
All physical constants and the actual conditional measure remain explicit.

**Independent curvature estimate.** `OPTIMIZED_DOMAIN.md` evaluates the exact original
plaquette Fourier coefficient and the full scalar majorant. It proves the
stronger full physical lower bound O13 for g^4>138240/451, including
Delta_L>=(3/20)kappa for every g>=9/2. Its zero-shift and full spatial-volume
returns are O19–26. The baseline constants below are preserved for audit.

15 September 2026. Additive continuation of the delivered
`20260915-actual-loop-moments` calculation. Its remote ancestor is Yang–Mills
PR6, `e98b2c3af77f66fb1c1396143ca53daef586404f`. The delivered predecessor is
identified by its own SHA-256 and is not assigned an invented remote commit.

## Results and exact scope

For every original open box L>=2, every a>0, and every **g>=8**, retain

    kappa=2g^2/a, v=1/(2g^2 a), xi=1/(4g^4).

The complete physical excitation gap satisfies

    Delta_L >= kappa(1/2-6144 xi) >= kappa/8.                  (U1)

The proof constructs the actual vacuum logarithm in a support-labelled
Fourier source, controls its full mixed second-derivative matrix, and returns
that bound to the original physical energy. No finite spin or observable
cutoff supplies the lower bound.

At xi=10^-8, equivalently g^2=5000 and kappa=10000/a, the elementary-loop
forcing W and full conditional-kernel operator D of the predecessor satisfy

    |<W,D^-1 W>_rho - (8/39) kappa xi^2|
         < 0.0000094 kappa xi^2,
    | ||D^-1 W||_rho^2 - (196/4563) xi^2 |
         < 0.0000041 xi^2.                                  (U2)

These are enclosures of the **actual zero-shift response**, uniform over all
exterior boxes L>=2. The finite remainder formulas are in U36–43. Section 9
controls both spectral endpoints in the volume limit at fixed a and g>=8,
producing a nonzero gapped limiting correlation generator. The spacing and
coupling path of the four-dimensional continuum program remains explicit in
section 10; no continuum mass lower bound is asserted here.

Fourier-algebra multiplication, contraction mapping, and the integrated
second-derivative spectral argument are classical methods. The present
calculation supplies the original-operator maps, support estimates, constants,
and physical response enclosures. No historical-priority claim is made.
Executable finite checks accompany the written analytic proof; they do not
constitute a formal verification of its infinite-dimensional assertions.

## 1. The unchanged operator, state, and energy form

The vertices are {-L,...,L}^3. E is the set of all contained positive edges
and P the set of all contained elementary faces. Use the original matrices
T_alpha=-i sigma_alpha/2 and derivatives

    X_e,alpha f(U)=d/dt f(...,exp(t T_alpha)U_e,...) at t=0,
    K=-sum_(e,alpha)X_e,alpha^2,
    V=v sum_(p in P)(2-W_p), H=kappa K+V.                   (U3)

W_p is its complete oriented four-link fundamental trace. Reverse traversal
uses the inverse of that same link. The scalar 2v|P| is retained. Every dU
below is the original product Haar probability measure. In the source metric
c(T_alpha,T_beta)=delta_alpha,beta/4 the operator uses its original factor;
all following derivatives continue to be the original X with coefficient kappa.

The full scalar compact-group operator has domain H^2, form domain H^1,
compact resolvent and a unique smooth positive unit ground state psi [YM].
It is gauge invariant; the physical spaces are the invariant parts. Put
u=log psi, rho=psi^2 and b_i=X_i u, where i=(e,alpha). Multiplication f->psi f
and its inverse h->h/psi give

    A=psi^-1(H-E0)psi=-kappa L,
    L=sum_i X_i^2+2 sum_i b_i X_i,
    q_A(f,h)=kappa int rho sum_i conjugate(X_i f)X_i h.      (U4)

The scalar ground energy E0 and unit state are those of the complete H.
No new state or energy pairing replaces U4.

## 2. Original Fourier coefficients, labelled supports, and a local product bound

### 2.1 All original representation labels

For each edge keep j_e in {0,1/2,1,...}. The product representation pi_j has

    d_j=product_e(2j_e+1), c_e(j)=j_e(j_e+1),
    c(j)=sum_e c_e(j), S(j)={e:j_e>0}.                      (U5)

For explicit generator coordinates let J_3|m>=m|m>,
J_+|m>=sqrt((j-m)(j+m+1))|m+1>, J_-=J_+^*,
J_1=(J_++J_-)/2 and J_2=(J_+-J_-)/(2i). Then d pi_j(T_alpha)=-i J_alpha.
Multiplication gives sum J_alpha^2=j(j+1)I; rotations in this same unitary
representation give ||J_alpha||op=j. Thus the original K acts by c(j),
retaining its 3/4 value on a spin-1/2 factor.

Use the coefficient convention

    f(U)=sum_j Tr(A_j pi_j(U)),
    A_j=d_j int f(U)pi_j(U)^*dU.                           (U6)

Matrix-entry orthogonality proves the inverse formulas and uniqueness.
In particular the trivial coefficient is int f dU. Write a_j=||A_j||_1,
the trace norm of the complete coefficient matrix. Then

    |Tr(A_j pi_j(U))|<=a_j,
    ||X_e,alpha Tr(A_j pi_j)||Fourier<=j_e a_j,
    ||X_f,beta X_e,alpha Tr(A_j pi_j)||Fourier<=j_e j_f a_j. (U7)

The Fourier norm here is sum_j ||A_j||_1, with the d_j already present in U6.
These standard compact-group Fourier coordinates are described in [FA].
Their use here estimates derivatives of the original state and does not
alter the physical measure or inner product.

Here is a coefficient proof of the product bound used below. A product of
two summands is

    Tr((A_j tensor B_k)(pi_j tensor pi_k)(U)).

A unitary decomposition of pi_j tensor pi_k into irreducibles retains all
multiplicity spaces. The coefficient of an output irreducible is the partial
trace over its multiplicity space of the corresponding diagonal block.
For such a block C, trace-norm duality gives

    ||Tr_m C||_1=sup_(||Z||op<=1)|Tr((Z tensor I_m)C)|<=||C||_1.

Pinching into all diagonal blocks is an average of unitary conjugations
using the roots of unity as block phases. Its trace norm is at most the
original one by the triangle inequality. Since the trace norm of a tensor
product is the product of its trace norms, the full coefficients satisfy

    sum_output ||C_output||_1<=a_j b_k.                    (U8)

Every output active support is contained in S(j) union S(k). All its
coefficients and multiplicities remain. Absolute summability extends U8 to
the stated Fourier series by norm and uniform convergence.

### 2.2 The support source and its exact assembly kernel

For every nonempty edge label S retain a local zero-Haar-mean function
f_S=sum_(j nontrivial, S(j) subset S)Tr(A_(S,j)pi_j). An inactive edge may
remain in S after a coefficient cancellation. The declared observation is

    Assembly((f_S))=sum_S f_S,
    (Assembly A)_j=sum_(S containing S(j)) A_(S,j).          (U9)

Use the auxiliary source norm

    ||f||loc=max_(e in E) sum_(S containing e)
                      2^|S| sum_(j nontrivial)c(j)||A_(S,j)||_1. (U10)

For the finite graph this is a complete norm on the coefficient families.
The total c-weighted coefficient sum is at most |E| ||f||loc; U7 therefore
supplies uniform convergence of the assembled function and of all original
first and second derivatives. The physical form remains U4.

The kernel of Assembly consists exactly of the coefficient equations
sum_S A_(S,j)=0 for every nontrivial j. Its complete primitive presentation
is explicit. For S strictly containing S(j), define

    d(S,j,B)=(B at (S,j))-(B at (S(j),j)).                  (U11)

Assembly d=0. Given a kernel family, use its A_(S,j) as incoming coefficients
at every S != S(j). Their boundaries recover those components. The remaining
S(j) component is their negative sum, which is exactly its original component
by the kernel equation. This constructs an inverse presentation and proves
ker Assembly=im d, without erasing any old label. The sums converge in the
finite-graph source norm: there are finitely many labels and lowering a label
only lowers its exponential weight.

### 2.3 The nonlinear bound without an exterior-volume factor

Let P_H be the original Haar-constant projection, Q_H=I-P_H, and let K^-1 on
the nontrivial Fourier source multiply its j coefficient by 1/c(j). Define

    B(f,h)_S=K^-1 Q_H sum_(S1 union S2=S) sum_(e,alpha)
                      (X_e,alpha f_S1)(X_e,alpha h_S2).    (U12)

Each output has its actual union label. The removed trivial Fourier coefficient
is retained as a scalar at that label; the sum of those scalar coefficients
will determine the original ground energy in U17.

For every spin label,

    j_e<=(2/3)c(j), sum_e j_e<=(2/3)c(j).                   (U13)

Indeed j(j+1)*(2/3)-j=j(2j-1)/3>=0 for every nonzero spin.
For an anchor a in S1, U7–8 and 2^|S1 union S2|<=2^|S1|2^|S2| give the bound

    3 sum_(S1 containing a,j)2^|S1| ||A_(S1,j)||_1
       sum_e j_e sum_(S2 containing e,k)2^|S2| k_e||B_(S2,k)||_1
      <=(4/3)||f||loc ||h||loc.

The inner sum is at most (2/3)||h||loc by U13, and sum_e j_e is at most
(2/3)c(j). The factor three retains every generator component. Contributions
with a in S2 have the same bound with f and h exchanged. Counting both is an
upper bound also on their overlap. Finally, the c(output) in U10 cancels
exactly its inverse multiplier in U12. Thus

    ||B(f,h)||loc<=(8/3)||f||loc ||h||loc.                  (U14)

All sums are absolutely convergent under these estimates. No constant depends
on |E|, and every active and retained support is present.

## 3. Construction of the actual vacuum and its full Hessian bound

Assign (xi/3)W_p to its four-edge label boundary(p). Its Casimir is 3.
The original four-link trace expands into sixteen signed products of fundamental
entries. The exact inverse formula U^-1=epsilon U^T epsilon^-1,
epsilon=[[0,1],[-1,0]], expresses every inverse entry as a signed original
entry. Each product is a coefficient matrix unit in the tensor product of four
spin-1/2 representations and has trace norm one. Thus ||W_p||Fourier<=16.
At most four plaquettes meet an original edge. The complete labelled source is

    f^(1)=(xi/3)sum_p W_p, ||f^(1)||loc<=4*2^4*16*xi
         =1024 xi=:b_0.                                  (U15)

Its assembly is precisely the predecessor's first local term u_0. Keep the
full nonlinear iteration

    F(f)=f^(1)+B(f,f), f^(0)=0, f^(m+1)=F(f^(m)),
    R=2048 xi=2b_0.

For 0<xi<=1/16384, R<=1/8. U14 gives, on the closed R-ball,

    ||F(f)||loc<=R/2+(8/3)R^2<=(5/6)R,
    ||F(f)-F(h)||loc<=(16/3)R||f-h||loc<=(2/3)||f-h||loc.   (U16)

The iterates are Cauchy by summing their geometric successive differences.
Completeness gives the fixed point in this ball, unique there. Every iterate
is real and gauge invariant: the source, Casimir, Haar projection and the
complete generator contraction commute with the original gauge action.
Their assembled limit v_* has the same properties and original derivatives.

Let C_S be the removed scalar of U12 at this fixed point, and let
C=sum_S C_S=int sum_i(X_i v_*)^2dU. The actual assembled equation is
K v_*=xi sum_p W_p+sum_i(X_i v_*)^2-C. Retain the scalar coordinate

    c_*=-(1/2)log int exp(2v_*)dU,
    psi_*=exp(v_*+c_*), E_*=2v|P|-kappa C.                 (U17)

The original constant 2v|P| and all removed scalar contributions remain.
The coordinate map on a positive unit function is
psi -> (Q_H log psi,P_H log psi); U17 reconstructs this particular solution
with its original unit norm and measure. No scalar from that state is dropped.

Uniform convergence of second derivatives gives a C^2 solution v_* of the
assembled equation. The right side is C^1, hence locally Hölder. Elliptic
regularity gives C^(2,alpha) and repeated regularity of this same equation
gives smoothness. Direct differentiation proves H psi_*=E_* psi_*. Moreover
for every smooth h,

    q_(H-E_*)(psi_*h)=kappa int psi_*^2 sum_i |X_i h|^2>=0.

Multiplication by psi_* and its inverse preserve H^1 on this compact finite
graph. The identity proves E_* is the lowest energy. The source uniqueness
therefore identifies psi_*=psi, E_*=E0 and v_*+c_*=log psi. The iteration has
constructed the original interacting vacuum, rather than an auxiliary one.

Let J_(e,f) have entries X_e,alpha X_f,beta u and S_u=(J+J^T)/2. U7 implies

    ||J_(e,f)||op<=3 sum_(S containing e,f,j)j_e j_f||A_(S,j)||_1.

For n active edges of a coefficient, applying 2ab<=a^2+b^2 to each f != e gives

    j_e sum_f j_f<=((n+1)/2)sum_f j_f^2<=((|S|+1)/2)c(j).

The same symmetric block majorant controls J and its symmetric part. Since
(|S|+1)/2^|S|<=1 for every nonempty label, each full block-row sum is at most
(3/2)R. The symmetric Schur row bound follows directly from
2|x_e||x_f|<=|x_e|^2+|x_f|^2. It proves the pointwise, full-matrix estimate

    ||S_u||op<=(3/2)R=3072 xi.                            (U18)

The construction's nonzero labels are connected in the line graph of original
edges. Plaquette boundaries are connected and a nonzero product in U12 has
a shared derivative edge. Thus for integer d>=0, the same estimate restricted
to f at line-graph distance at least d from e gives

    sum_(f:dist(e,f)>=d)||(S_u)_(e,f)||op
      <=(3/2)R (d+2)/2^(d+1).                            (U19)

Each contributing connected S has |S|>=d+1; (m+1)/2^m decreases for m>=1.
This spatial estimate keeps every cross-link block and its original support.

## 4. Coordinate-level proof of full physical coercivity

For real smooth f set Gamma(f)=sum_i(X_i f)^2. The original bracket is
[X_e,alpha,X_e,beta]=-epsilon_alpha,beta,gamma X_e,gamma and the Casimir
commutes with each X_j. Differentiating L in U4 gives exactly

    Gamma_2(f):=(1/2)L Gamma(f)-sum_j(X_j f)X_j Lf
      =sum_(i,j)(X_i X_j f)^2
         -2 sum_(i,j)(X_j f)(X_j X_i u)(X_i f).             (U20)

The intermediate bracket term is
2 sum_(i,j,k)b_i(X_j f)c_(ij)^k(X_k f). On each edge its epsilon coefficient
is antisymmetric in j,k while the derivative product is symmetric, so the
term is exactly zero. The antisymmetric part of J_u also contracts to zero;
the retained part is S_u with its entire mixed matrix.

For each original edge the antisymmetric part of [X_e,alpha X_e,beta f]
has squared Frobenius norm (1/2)sum_alpha(X_e,alpha f)^2, by the same bracket
calculation. The symmetric parts and all other blocks contribute nonnegative
squares. Therefore U18–20 give

    Gamma_2(f)>=(1/2-6144 xi)Gamma(f)=:d_xi Gamma(f),
    d_xi>=1/8 on 0<xi<=1/16384.                           (U21)

This retains the original curvature coefficient 1/2 and the full drift cost.
Integration in the actual invariant density rho gives
int rho Lh=0, int rho conjugate(f)Lh=-int rho sum conjugate(Xf)Xh, hence

    int rho Gamma_2(f)=int rho(Lf)^2.                      (U22)

Every nonconstant eigenfunction of the original scalar A is smooth; use a real
basis of its eigenspace, or apply the identity to real and imaginary parts.
For A f=lambda f, U22 reads int Gamma_2=(lambda/kappa)int Gamma. The latter
integral is positive. Thus lambda>=kappa d_xi. The complete compact spectral
resolution then gives on the full original form domain

    q_A(f)>=kappa d_xi (||f||_rho^2-|<1,f>_rho|^2).         (U23)

Restricting this inequality to the gauge-invariant domain proves U1, or in
unchanged physical parameters

    Delta_L>=(g^2-3072/g^2)/a, g>=8.                      (U24)

The centered gradient primitive p(df)=f uses the original source norm
||df||energy^2=kappa int rho sum|Xf|^2. Its exact variational characterization is

    ||p||^2=1/Delta_L<=1/(kappa d_xi).                     (U25)

This includes all centered physical vectors and regulator-dependent choices
of vector, as well as the previously retained finite observation families.

## 5. Support tails and a genuine volume extension

Keep a>0,g>=8 fixed. The fixed point has the completely specified coefficient
series

    v_[1]=K^-1 sum_p W_p (with original plaquette labels),
    v_[p]=sum_(j=1)^(p-1)B(v_[j],v_[p-j]),
    v_*=sum_(p>=1)xi^p v_[p].                             (U26)

Each order-p label is a union of p original plaquettes joined by shared edges.
The union recursion proves |S|<=3p+1. Each representation has j_e<=p/2 by
tensor-product decomposition; there are finitely many terms touching a fixed
edge at this fixed order. Let C_m=binom(2m,m)/(m+1). Its quadratic recurrence,
U14 and U15 prove

    ||xi^p v_[p]||loc<=C_(p-1)(8/3)^(p-1)(1024xi)^p.

Since C_m<=4^m, theta=(32768/3)xi<=2/3 gives the actual convergent tail

    ||sum_(p>P)xi^p v_[p]||loc
       <=1024xi theta^P/(1-theta).                        (U27)

No finite order replaces the full Hamiltonian. At a fixed edge all coefficients
through order P are identical in every box containing its line-graph ball of
radius 3P. This follows from U26's support unions. The original derivatives
b_e^L=X_e log psi_L consequently have a uniform limit on the full countable
configuration product. The finite/infinite difference has the explicit bound

    |b_e^L-b_e^infinity| <= (4/sqrt(3))1024xi theta^P/(1-theta) (U28)

when that ball is contained. Each of the two tails uses
|X_e f|<=(2/sqrt(3))||f||loc from U7 and U13.

Extend the finite vacuum probability by original independent Haar factors
outside its box. Compactness of the countable SU(2) product and diagonal
selection on its matrix-entry cylinder algebra give weak subsequential limits
nu. The original gauge invariance passes to every limit. For smooth cylinders,
finite-volume integration by parts and U28 prove

    int X_i f dnu=-2 int b_i^infinity f dnu.                (U29)

Each limiting drift is bounded and continuous, being a uniform limit of the
specified local functions. No density relative to the infinite Haar product
is asserted or needed for U29.

The original cylinder form has a closed realization. Define df=(X_i f)_i
with target the Hilbert direct sum of the original L^2(nu) components. For
f_n->0 in L^2 and df_n->h in the direct sum, U29 against a cylinder test w gives

    <w,h_i>=-lim_n<X_i w+2 b_i^infinity w,f_n>=0.

Density of cylinders proves h=0. Thus d is closable. The form
q_infinity=kappa||closure(d)||^2 is closed and nonnegative; the chain rule and
closure give its Markov property. Passing U23 on cylinders to nu and closing
gives its full centered lower bound kappa d_xi. Section 9 constructs the
limiting correlation generator directly from finite-vacuum observations and
gives an explicit form comparison with this realization.

## 6. The full conditional kernel now has an inverse at zero

Use the elementary square at the origin, its ordered holonomy Omega, and
F=tr Omega from [ALM, A15–20]. The coordinate map

    (V1,V2,V3,V4,U_out)->(Omega=V1 V2 V3 V4,V1,V2,V3,U_out)

has inverse V4=(V1 V2 V3)^-1 Omega and preserves product Haar. Its actual maps are

    m(Omega)=int rho(Omega,z)dz,
    E f=m^-1 int rho f dz, Jf=f(Omega), Q=I-JE.             (U30)

E=J*, EJ=I in the original pairings. Every member of Kcal=ker E has global
rho mean zero. The closed restricted form from [ALM, A18–20] represents D.
U23 therefore proves on that full kernel

    D>=kappa d_xi I,
    ||(D+s)^-1||<=1/(kappa d_xi+s), s>=0.                  (U31)

Exterior and additional coarse fluctuations are included. This proves the
zero-shift inverse on the actual Hilbert kernel, without replacing it by a
trial subspace. Define W=-Q A F=2kappa Qj, where
j=sum_(e in C,alpha)b_e,alpha X_e,alpha F. For any actual Y in Dom(D), set
R=W-DY. Expanding the full residual square gives

    M0:=<W,D^-1W>=2 Re<W,Y>-q_D(Y)+<R,D^-1R>,
    0<=<R,D^-1R><=||R||^2/(kappa d_xi),
    ||D^-1W-Y||^2=<R,D^-2R><=||R||^2/(kappa d_xi)^2.        (U32)

These are full Gram identities for any finite family of columns as well.
On the actual spectrum lambda>=kappa d_xi the resolvent multipliers give

    0<=M0-Ms<=[s/(kappa d_xi)]M0,
    ||(D+s)^-1W-D^-1W||
       <=[s/(kappa d_xi+s)]||D^-1W||, s>=0.                (U33)

Thus the positive shift can be taken to zero with a uniform error on the
stated coupling domain.

## 7. Original local zero-shift trial and every error term

Retain the twelve neighboring plaquettes and their full original contractions
j_p from [ALM, A27–30]. The explicit singlet/triplet components sum to J0,J1,
and J=J0+J1, with

    KJ0=(9/2)J0, KJ1=(13/2)J1,
    ||J0||_H^2=27/16, ||J1||_H^2=9/16, <J0,J1>_H=0.        (U34)

Each unequal-plaquette cross term has an original unmatched-link Haar witness.
These are exact local polynomial identities; their interacting measure return
is bounded below. Define

    U=(2/3)J,
    Z=(4/27)J0+(4/39)J1=(4/39)J+(16/351)J0,
    z=xi Z, Y=Qz.                                        (U35)

U34 gives KZ=U and the complete coefficients

    <U,Z>_H=m_*=8/39,
    ||Z||_H^2=z_*=196/4563.                               (U36)

For example m_*=(3/4)/(9/2)+(1/4)/(13/2), retaining both components.
The original local suprema in [ALM, A31,A41] give

    ||U||infinity<=8,
    ||Z||infinity<=Z_*=64/39,
    sum_e||X_e Z||infinity<=L_*=80/13.                     (U37)

The support is the same 32 original links. Both the conditional Haar mean
of Z and that of each horizontal derivative vanish.

Put A_*=256/9, ell=4, and retain

    delta=exp(1024 pi xi)-1, eta=exp(1088 pi xi)-1,
    hz=xi(eta L_*/2+16xi Z_*),
    rz=8A_*xi^2+16xi^2 L_*+64xi hz,
    nz=sqrt((1+delta)z_*).                               (U38)

The exponential factors are the predecessor's actual marginal and constrained-
fiber comparisons. Its remainder r_e=X_e(u-u0) satisfies |r_e|<=A_*xi^2 on
xi<=3/64, which contains our entire new domain. Set
dj=sum_(e in C,alpha)r_e,alpha X_e,alpha F. Then

    W=(2kappa xi/3)QJ+2kappa Qdj, ||dj||_rho<=4A_*xi^2,
    ||X E z||_m<=hz, ||J E z||_rho<=xi eta Z_*, ||Y||_rho<=xi nz,
    R=W-DY=2kappa Qdj+2kappa xi Q sum_i b_i X_i Z
                           -4kappa T* X E z,
    ||R||_rho<=kappa rz.                                 (U39)

Here T is the original score operator with ||T||<=16xi. The signs follow
from DQz=QAz-QAJEz, A=kappa K-2kappa b.X, KZ=U, and
QAJf=-4kappa T*Xf. The conditional coupling stays in the residual.

The seven nonnegative response errors are exactly

    a1=delta xi^2 sqrt(z_*), a2=16xi^3 Z_* L_*,
    a3=16xi^2 eta^2 Z_*, a4=16A_*xi^3 nz,
    a5=4hz^2, a6=128xi^2 nz hz, a7=rz^2/d_xi.

Set

    E_M=(a1+a2+a3+a4+a5+a6+a7)/xi^2,
    E_Z=delta z_*+(eta Z_*)^2+2nz rz/(d_xi xi)+(rz/(d_xi xi))^2. (U40)

The actual values satisfy

    |M0-kappa xi^2 m_*|<=kappa xi^2 E_M,
    | ||D^-1W||_rho^2-xi^2 z_* |<=xi^2 E_Z.                (U41)

To verify the entire response error, put w=kappa xi U and p=JEz. The
variational part of U32 expands to

    2 Re<w,z>-q_A(z)-2 Re<Pw,p>+4kappa Re<dj,Y>
                           +q_A(p)+2 Re q_A(Y,p).

KZ=U and weighted integration by parts turn its first pair into
kappa xi^2<U,Z>_rho+2kappa xi^2 int rho Z sum_i b_i X_i Z.
The marginal comparison bounds its first error by kappa a1. The actual
|b_e|<=8xi bounds the drift term by kappa a2. Both conditional Haar means are
zero, so the removed projection costs kappa a3. The differentiated-vacuum
remainder costs kappa a4. The coarse form is 4kappa||XEz||^2, giving kappa a5.
The complete mixed form and ||T||<=16xi give kappa a6. Finally U31–32 give
kappa a7. Every term is included with its original sign before estimation.
For the metric use ||Y||^2=||z||^2-||p||^2 and
||D^-1W-Y||<=rz/d_xi, expanding the squared norm and keeping its cross term.
This yields exactly E_Z in U40.

## 8. Evaluated certificate, cohomological correction, and physical return

At the exact original value xi=1/100000000,

    d_xi=1/2-6144/100000000=0.49993856.                    (U42)

The checker uses rational pi<355/113, positive exponential series with explicit
remainder, and upper square roots certified by integer squares. It evaluates
U38–40 outward and gives

    E_M<0.0000094, E_Z<0.0000041,
    rz^2/(d_xi xi^2)<0.000000000022.                       (U43)

These are U2's stated enclosures for the actual vacuum. The preceding forcing
and three moments retain their own certified values and domains.

In the actual cochain window span{Y} --D--> Kcal --0-->0, define

    aY=q_D(Y), cY=<Y,W>_rho, alphaY=cY/aY,
    Rcan=W-D(alphaY Y).                                  (U44)

Y is nonzero: positive rho would turn z=JEz into an equality of the same
smooth functions under Haar, whose conditional Haar mean would force z=0,
contradicting U36. Hence aY>=kappa d_xi||Y||^2>0. In the original dual pairing
<r,D^-1t>, the equality <DY,D^-1Rcan>=0 follows by multiplication. Therefore

    ||[W]||_(Kcal/Dspan{Y},dual)^2=M0-|cY|^2/aY,
    R=Rcan+(alphaY-1)DY,
    <R,D^-1R>=||[W]||^2+aY|alphaY-1|^2<=kappa rz^2/d_xi.   (U45)

This retains the complete quotient norm, the original boundary primitive
(alphaY-1)Y and its separate energy. For nested actual spaces Vj in Dom(D),

    V_(j+1)/Vj <--> ker(Kcal/DVj -> Kcal/DV_(j+1)),
    [h] -> [Dh], [Dh] -> [h]                              (U46)

are well-defined inverse maps: a change by DVj changes the primitive by Vj.
U31 supplies the uniform completed inverse. The Split Zero reconstruction
keeps these supported relations, primitives, and original energy pairings.

Retain the actual observed variance G and kinetic entry K0. From [ALM, A48–49],
put

    deltaC=exp(128pi xi)-1,
    B2=xi delta/4+(sqrt(5)xi/6)deltaC+4A_*xi^2,
    emu=(2xi/9)(B2+3delta/2)+(8A_*/3)xi^2,
    EG=B2+(2xi/3+emu)^2.                                 (U47)

Then |G-1|<=EG and |K0-3kappa|<=kappa B2; at U42 both radii are below 11/10^14.
For h0=D^-1W and f=F-<F>_rho, the actual physical state
Phi0=psi(Jf+h0) is centered, nonzero, and in the full form domain. Its exact
pairings are

    ||Phi0||^2=G+||h0||^2,
    q_(H-E0)(Phi0)=K0-M0.                                (U48)

Both mixed entries are -M0 and q_D(h0)=M0. Substitution of U41,U47 proves

    (3-5*10^-13)kappa < q_(H-E0)(Phi0)/||Phi0||^2
                                      < (3+5*10^-13)kappa. (U49)

The complete-domain lower bound U23 and the variational inclusion of span{Phi0}
give, with their respective proved maps,

    0.49993856 kappa <= Delta_L < (3+5*10^-13)kappa          (U50)

for every a>0, L>=2 at g^2=5000.

## 9. Both spectral endpoints at fixed spacing and coupling

Keep a>0,g>=8 fixed and let L grow. For each finite list of smooth bounded
physical cylinder observables O_i use their actual centered vectors
r_i,L=(O_i-<O_i>_rhoL)psi_L. Their matrix spectral measure mu_L satisfies by U23

    mu_L([0,kappa d_xi))=0.                               (U51)

For every coefficient vector x the original first-moment identity is

    int lambda d(x*mu_L x)(lambda)
       =kappa int rho_L sum_e,alpha |X_e,alpha sum_i x_i O_i|^2
       <=kappa sum_e,alpha ||sum_i x_i X_e,alpha O_i||infinity^2. (U52)

Only the original finite supports occur on the right. Dividing this bound
by Lambda controls all mass above Lambda, uniformly in L. Thus weak selection
on [0,infinity], jointly with the equal-time vacuum selection, gives

    mu({0})=0, mu({infinity})=0,
    supp mu subset [kappa d_xi,infinity),
    G^c=C(0+), C(t)=int exp(-t lambda)dmu(lambda).           (U53)

Polarization gives the full matrix statement. A countable gauge-invariant
cylinder algebra and diagonal selection retain it for every finite list.
For the conditional memory, D_L>=kappa d_xi similarly excludes zero-energy
mass. Its inverse-energy measure has no atom at zero. U33 controls the two
limit orders down to zero shift. Thus the previously retained Z_alpha is
proved zero in this fixed-spacing, fixed-coupling volume limit.

The limiting elementary-loop vector survives quantitatively. The predecessor's
four-link marginal bound proves

    Var_rhoL F=inf_c int rho_L |F-c|^2
        >=exp(-128pi xi) inf_c int_H |F-c|^2
        =exp(-128pi xi).                                 (U54)

Also q_A(F)<=4kappa. Spectral integration of exp(-t lambda)>=1-t lambda and
U51 yields in the limit

    C_F(t)>=exp(-128pi xi)-4kappa t,
    0<=C_F(t)<=C_F(0)exp(-kappa d_xi t).                   (U55)

In particular the lower bound is positive for the explicitly stated interval
0<t<exp(-128pi xi)/(4kappa).

For the limiting generator use symbols [i,t], t>=0, paired by C_ij(t+s),
quotient the complete null space, and complete. Time translation
T(u)[i,t]=[i,t+u] retains the finite-volume positive self-adjoint contraction
Gram inequality. U52 gives continuity at zero, hence strong continuity on
the dense span. Equivalently realize each symbol as exp(-t lambda)e_i in the
Hilbert space of the positive matrix measure; its closed cyclic span reduces
the multiplication semigroup and its generator. The generator is multiplication
by lambda with domain int lambda^2|h|^2 dmu<infinity on that reducing span.
Its lower bound is kappa d_xi and its Hilbert space is nonzero by U54–55.
This is a nontrivial gapped infinite-volume correlation generator at fixed
lattice spacing, obtained from the actual vacuum correlations.

The comparison with section 5's cylinder form is explicit. The map sending a
centered cylinder f in L^2(nu) to its zero-time correlation vector xi_f is an
isometry, since U53 identifies its Gram with the original limiting covariance.
It extends to a closed-range isometry U. For each such f the predecessor's
all-coupling derivative estimate |b_e^L|<=8xi gives a volume-uniform bound on

    ||A_L f||infinity<=kappa||Kf||infinity
                  +16kappa xi sum_e||X_e f||infinity.

Thus its spectral second moments are uniformly bounded. This supplies uniform
integrability of its first moments, so polarization and U52 give
q_obs(Uf,Uh)=q_infinity(f,h) on cylinders. Closure extends the isometric form
inclusion to the closed cylinder form domain. This is the declared map between
the two constructions; any orthogonal complement of its range remains in the
correlation Hilbert space with the same lower bound. The further argument in `VOLUME_LIMIT.md`, V1–25, proves a unique original
vacuum measure and a direct dynamical limit, and constructs the surjective
unitary between this correlation space and its full physical vacuum
representation. The cylinder-form inclusion here retains its stated domain;
that subsequent identification is proved through the semigroups.

## 10. Exact comparison with the running continuum path

The earlier path remains

    a_n=a_0 2^-n, L_n=4*2^(2n),
    c_n=g_0^-2+beta n log2, g_n^2=c_n^-1,
    xi_n=c_n^2/4, kappa_n=2^(n+1)/(a_0 c_n).               (U56)

The newly proved domain is exactly c_n<=1/64. It contains only finitely many
indices on that path for beta>0. The predecessor's all-coupling derivative and
gauge-sector estimates remain available with their complete c_n dependence;
U1 is not asserted outside its proved domain.

There is a precise further path calculation at any fixed g>=8. Along a_n->0,
U1 gives Delta_n>=2g^2 d_xi/a_n->infinity, independently of the box sequence.
For uniformly bounded centered observables,

    |C_ij,n(t)|<=||r_i,n|| ||r_j,n||exp(-2g^2 d_xi t/a_n)->0 (t>0). (U57)

For every fixed finite energy Lambda the excited spectral mass in [0,Lambda]
is eventually exactly zero. The compactified zero-time mass is retained at
energy infinity. Consequently the fixed-spacing volume limit U53 and this
change of spacing U57 have explicitly different parameter maps and endpoint
formulas. Neither is substituted for the original g_n->0 path.

This cycle has supplied full-domain physical coercivity, a quantitatively
controlled inverse at zero, actual zero-shift response values with finite
errors, and the fixed-spacing volume extension. Extending control of the
complete vacuum Hessian and conditional response beyond the stated xi range,
while retaining the physical spacing and growing support, is the next original
quantity in the workbench. No desired continuum estimate is inserted as a
premise. The four-dimensional continuum field and positive physical mass remain
unestablished by this contribution.

## 11. Provenance and verification scope

[YM] KokunoYumeto/yang-mills-interacting-workbench, original source commit
`fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`,
`yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md`,
blob `66a7453a6452c2555a28270efcf53fa1997c26a8`, sections 1–3. Original operator,
positive ground state and domains. The source's Hamiltonian antecedents and
original physical conventions retain their attribution.

[ALM] The complete delivered `20260915-actual-loop-moments/RESEARCH_NOTE.md`
and checker. Used equations A4–5, A14–20, A24–31, A34, A48–49. The complete
file was read and its exact original checker replayed. The positive-shift
response of that source is preserved; U31 justifies the new zero-shift inverse.

[CR] PR6 `e98b2c3af77f66fb1c1396143ca53daef586404f`,
`20260914-coupled-response/RESEARCH_NOTE.md`, especially C13–22: actual support
windows and full residual identities. The completed zero-shift instance is
U31–33,U44–46, with its physical norm explicitly retained.

[FA] Hun Hee Lee, Ebrahim Samei, Nico Spronk, *p-Fourier algebras on compact
groups*, arXiv:1411.2336v2, sections 0.1–0.2 and 1.1, public HTML
https://arxiv.org/html/1411.2336v2 . These are the standard Fourier-coefficient
antecedents. U7–14 prove the precise derivative and support estimates used here.

The current peer PR descriptions and Zeta head were inspected for continuation
intake. New Collatz completion and ES cofactor developments are recorded as
candidates; they supply no premise to this proof. No unread peer theorem or
reported CI count is presented as new verification here.

`verify.py` checks coordinate Gamma_2 identities on original SU(2) polynomials,
representation/support and contraction constants, raw-Gram zero-shift matrix
identities, corrected cohomological residuals, and rational endpoint evaluation.
Finite matrix examples are declared fixtures. The full analytic contraction,
regularity, spectral and limit arguments are written above. Receipts identify
the executed source bytes and exit codes; no new Lean, remote CI, independent
external review, or historical-priority conclusion is claimed.


---

# Chapter 14 — 20260915-uniform-gap-zero-shift / VOLUME_LIMIT.md

Original text path: `workbench/yang-mills/continuations/20260915-uniform-gap-zero-shift/VOLUME_LIMIT.md`.

# The full spatial-volume limit: original vacuum measure and dynamics

15 September 2026. This completes the fixed-spacing volume extension of
`RESEARCH_NOTE.md`, equations U26–29 and U51–55. Throughout this file the
original physical spacing a>0 and coupling g>=8 are fixed,

    kappa=2g^2/a, xi=1/(4g^4), R=2048xi<=1/8,
    d_xi=1/2-6144xi>=1/8.

The original finite-box Hamiltonians, their positive unit vacua and every
local link coordinate remain those of U3–4. No infinite scalar ground energy
or density relative to the infinite Haar product is stipulated. We construct
the limit of the actual finite ground-relative dynamics and its vacuum
representation. `OPTIMIZED_DOMAIN.md`, O23–26, evaluates the same complete proof inputs on
the larger domain g^4>138240/451, retaining all the following maps and replacing
only the stated auxiliary bounds. The continuum change a->0 remains the separate parameter
calculation U56–57.

## V1. Exact compatibility of the retained support coefficients

Let E_infinity be the countable set of positive nearest-neighbor edges of
Z^3. For every nonempty finite label S use the coefficient convention U6–10.
The order-p coefficient with label S in U26 depends only on coefficients
with labels S1,S2 whose union is S, and on source plaquettes with boundary S.
Every such label is a subset of S. The multiplier K^-1 on functions of S
is the same sum-of-original-Casimirs inverse in every box containing S.
The original Haar-constant projection on a function of S is likewise the
integral over those same S variables. Induction in the exact coefficient
recurrence therefore proves

    v_(S,[p])^L=v_(S,[p])^L'                              (V1)

for every two boxes containing S. For each p this is a finite identity:
S is contained in a finite graph, the spin at each edge is at most p/2,
and the recurrence has only finitely many partitions of its order and labels.

U27 is a convergent bound for the full series. Define

    v_S=sum_(p>=1)xi^p v_(S,[p]).

The same v_S occurs in every finite-box vacuum containing S. The finite-box
logarithm and density are exactly

    log psi_L=c_L+sum_(S subset E_L) v_S,
    rho_L=exp(2 sum_(S subset E_L)v_S)/Z_L,
    Z_L=int exp(2 sum_(S subset E_L)v_S)dU_L.               (V2)

The scalar c_L=-(1/2)log Z_L is the original scalar coordinate in U17. The
higher labels remain even when Fourier active support becomes smaller. In
particular, contributions from an outside cluster have not been reassigned
to a smaller label and then mistaken for an inside term.

Set a_(S,j)=||A_(S,j)||_1 in the original trace convention. The full bound is

    sup_e sum_(S containing e)2^|S| sum_j c(j)a_(S,j)<=R.   (V3)

The same estimate holds for the infinite family: for each finite partial
collection take a box containing its supports, apply U16, and take the
increasing supremum of the nonnegative sums. Since c(j)>=3/4 for every
nontrivial representation,

    ||v_S||infinity <= (4/3) sum_j c(j)a_(S,j),
    sup_e sum_(S containing e)||v_S||infinity <= (2/3)R.   (V4)

All local conditional sums below consequently converge absolutely and
uniformly. Their terms are continuous real functions of the original links.

## V2. Actual conditional measures and a quantitative influence bound

For a finite edge set Lambda and an exterior configuration eta, define the
finite conditional kernel by its complete density

    gamma_Lambda(dU_Lambda|eta)
      = exp(2 sum_(S intersects Lambda) v_S(U_Lambda eta)) dU_Lambda
        / int exp(2 sum_(S intersects Lambda) v_S(V_Lambda eta)) dV_Lambda. (V5)

The sum is uniformly absolutely convergent by V4 and the finite number of
anchors in Lambda. The denominator is strictly positive and finite. Terms
entirely outside Lambda would be the same factor in numerator and denominator;
V5 is the explicit conditional formula retaining their exact cancellation.
For an individual edge e, its dependence on an exterior link f is bounded by

    c_ef=4 sum_(S containing e,f)||v_S||infinity (e!=f),
    c_ee=0.                                                (V6)

Here c is an actual nonnegative influence majorant, not an assumed matrix.
To prove the bound, change only the exterior link f. The change Delta(U_e)
in the logarithm before division by the integral is
2 sum_(S containing e,f)(v_S(U_e eta)-v_S(U_e eta')). Its oscillation in U_e
is at most 8 sum ||v_S||infinity. For the interpolation of the two actual
probabilities p_t proportional to exp(t Delta)p_0, differentiation gives

    d p_t/dt=(Delta-E_(p_t)Delta)p_t.

The total-variation speed is at most (1/2)osc(Delta). Integration over
0<=t<=1 proves TV(p_1,p_0)<=c_ef. The differentiation is justified by the
bounded continuous Delta. Changing multiple exterior coordinates follows
by telescoping; countably many changes follow by uniform convergence of
V5 and the summability established next.

The row sums obey

    sup_e sum_f c_ef
      <= (16/3) sup_e sum_(S containing e)(|S|-1) sum_j c(j)a_(S,j)
      <= (4/3)R <= 1/6.                                  (V7)

Indeed (m-1)/2^m<=1/4 for every integer m>=1. This retains the original
factor two in the vacuum density, every link in each support, and the
original Fourier bound. No source mass or physical coupling was changed.

## V3. Complete finite comparison and uniqueness

For completeness we prove the comparison used here, rather than supplying a
uniqueness criterion as an unevaluated premise. Fix Lambda and two exterior
configurations. Their probabilities in V5 are invariant under the operation
which chooses one edge of Lambda uniformly and replaces it by its own exact
conditional probability. This follows by Fubini from V5. Couple two such
chains starting with those two invariant probabilities as their marginals.
On the selected edge, couple the conditional densities maximally: use their
common density min(p,p') on the diagonal and the two residual densities on
the remaining event. This is a measurable coupling in the original Haar
coordinates. The residual event has probability exactly their TV distance.

Let p_e(t) be the probability of unequal links in this joint chain. Put
b_e=sum_(f outside Lambda)c_ef. From V6 and telescoping the remaining inside
coordinates, one update gives

    p(t+1) <= [(1-1/|Lambda|)I+C_Lambda/|Lambda|]p(t)
                       +b/|Lambda|.                      (V8)

The matrix norm of the bracket in the max norm is at most
1-(1-q)/|Lambda|, q=1/6. Both marginals remain their original invariant
probabilities at every time. For a cylinder function F depending on
Delta subset Lambda, define its original single-edge oscillation osc_e F.
Telescoping F on the two configurations bounds the difference of expectations
by sum_(e in Delta)(osc_e F)p_e(t). Iterating V8 and letting t grow gives

    |gamma_Lambda F(eta)-gamma_Lambda F(eta')|
       <= sum_(e in Delta)(osc_e F)
              [sum_(r>=0) C_Lambda^r b]_e.                (V9)

All entries on the right are actual convergent nonnegative sums. The initial
error tends to zero by the strict matrix-norm bound. This proof uses no
assumption about the existence of a stationary joint coupling.

As Lambda exhausts E_infinity, each b_e tends to zero because the row of c is
summable; b_e<=q. For each fixed r and e, C_Lambda^r b tends to zero by the
dominated convergence theorem for the corresponding absolutely summable
countable matrix products. The remainder of the Neumann sum after r=N is
bounded by q^(N+2)/(1-q). Thus the right side of V9 tends to zero for each
fixed F, uniformly over both exterior configurations.

Every weak subsequential limit nu of the original finite-box vacuum measures
satisfies the conditionals V5. To check this assertion precisely, the actual
finite-volume conditional on Lambda uses only S subset E_L in V5. The
supremum of its omitted logarithmic terms is at most

    2 sum_(e in Lambda) sum_(S containing e,S not subset E_L)||v_S||infinity,

which tends to zero by V4. Its conditional kernel therefore converges in TV,
uniformly over exterior configurations, to V5 by the same bounded-exponent
interpolation. The limiting kernel applied to a continuous cylinder function
is continuous on the full compact configuration product: its potentials are
uniform limits of continuous functions, its finite Haar integral is continuous,
and its denominator is bounded away from zero. The finite conditional
integration identity consequently passes to the weak limit, also after
multiplication by any bounded continuous exterior cylinder test. A monotone-
class argument extends those tests to the exterior sigma-algebra. This proves the
stated conditional property without prescribing it to the vacuum.

Any two probabilities with these conditionals have equal expectations of
all cylinder functions by V9, applied inside Lambda and then integrated over
their exterior laws. The cylinder algebra determines the measure. Hence there
is exactly one such nu. Since every subsequential vacuum limit has that
property and the whole family is compact, **the complete sequence of original
finite-box vacuum measures converges to nu**. The original normalized masses
and the constants Z_L have been retained in V2; no infinite product density
has been assumed. The finite marginals remain nontrivial and have the earlier
explicit positive density bounds.

The comparison mechanism is classical Dobrushin theory [DC]. Equations
V1–9 prove its actual input and full application here in the specified
original coordinates and coupling interval.

## V4. A complete majorant for the limiting drift

Let b_e^infinity=X_e sum_(S containing e)v_S, with all three original
components. Termwise differentiation is justified by V3 and U7. At finite
L extend b_e^L to zero outside E_L. The complete derivative majorant is

    B_ef=3 sum_(S containing e,f) sum_j j_e j_f a_(S,j),
    sup_e sum_f B_ef <= (3/2)R=:B_* .                     (V10)

This is the original, generally mixed, derivative matrix estimate before
taking its symmetric part. It is nonnegative and symmetric in e,f. For the
path length defined by dot U=sum_alpha a_alpha T_alpha U and length
int sqrt(sum_alpha a_alpha^2), let dist_X be the induced distance. The
adjoint matrices preserve this coefficient norm, so both group translations
are isometries. The diameter is 2pi in these original T coordinates. Relative
to the source metric c(T_alpha,T_beta)=delta_alpha,beta/4, the exact metric
identity is dist_X=2 dist_c; the physical kappa in every generator is unchanged.

V10 and integration along an original group path prove

    |b_e^infinity(U)-b_e^infinity(V)|
       <= sum_f B_ef dist_X(U_f,V_f).                    (V11)

For countably many changed links this follows from the finite telescoping
formula and the uniform cylinder approximation of b_e^infinity. The summed
majorant is finite. Define

    t_e(L)=sup_U |b_e^infinity(U)-b_e^L(U)|.

U28 proves t_e(L)->0 for each fixed e. The predecessor's actual pointwise
bound gives t_e(L)<=16xi uniformly in e,L. The same derivative construction
can also give its explicit coefficient-tail bound when the required ball is
contained in the box. V10 is an estimate for the same original three-component
drift appearing in the full ground-state-transformed Hamiltonian.

## V5. Direct dynamical limit on the original configurations

For every original edge choose three independent real Brownian motions, using
one fixed countable family for all boxes. At edges in E_L use the original
finite-vacuum diffusion; outside use the free original link diffusion:

    dU_e^L=sqrt(2kappa) sum_alpha T_alpha U_e^L o dB_e,alpha
            +2kappa sum_alpha b_e,alpha^L(U^L)T_alpha U_e^L dt. (V12)

The stochastic integral is Stratonovich. Its generator on smooth cylinders is
kappa sum X_i^2+2kappa sum b_i^L X_i. In a fixed box the coefficients are the
original smooth finite-vacuum coefficients; the outside processes are independent
free copies. Thus this process is defined without a new interaction model.
Its invariant probability is the original rho_L dU_L times outside Haar. For
functions of inside links the inclusion J_L f=f o restriction is an isometry
with Haar-conditional inverse on its range, and its semigroup satisfies

    T_L(t)J_L=J_L exp(-t A_L),
    A_L=psi_L^-1(H_L-E0,L)psi_L.                           (V13)

This proves the exact relation of the extended process to the finite original
quantum correlation, including its original vacuum and energy units.

Here is an explicit convergence proof. Let R_e(t) solve V12's free group
Brownian equation with R_e(0)=I. Write U_e^L=R_e V_e^L. The Stratonovich
product rule gives the ordinary differential equation, path by path,

    dot V_e^L=2kappa [R_e^-1 sum_alpha b_e,alpha^L(U^L)T_alpha R_e]V_e^L. (V14)

The conjugation rotates the original three coefficients orthogonally. The
same R_e is used for two boxes and initial configurations agree. Left
multiplication is an isometry for dist_X. The upper right derivative of the
distance of the two ODE solutions is therefore bounded by twice kappa times
the difference of their rotated coefficients. One proof uses the triangle
inequality after advancing both solutions by the same infinitesimal left
translation, whose contribution to their distance is zero. This remains a
valid upper-Dini-derivative bound at the cut locus.

Set z_e(t)=dist_X(U_e^L(t),U_e^M(t)). Equations V11 and V14 give

    z_e(t)<=2kappa int_0^t
        [sum_f B_ef z_f(s)+t_e(L)+t_e(M)]ds.               (V15)

The original group diameter bounds every z_e by 2pi. Iterating the integral
inequality, with w=t(L)+t(M), gives the complete bound

    sup_(s<=t) z_e(s)
      <= sum_(r>=0) (2kappa t)^(r+1)/(r+1)! (B^r w)_e.   (V16)

The iterated remainder is at most 2pi(2kappa B_*t)^N/N! and tends to zero.
No spatial cross term in B^r is dropped. Since w is uniformly bounded by
32xi and tends to zero at each fixed edge, each fixed matrix product tends
to zero by dominated convergence of its absolutely summable rows. The full
series is dominated by the exponential series with B_*, uniformly on compact
time intervals. V16 therefore tends to zero for every e as L,M grow.

The bound is deterministic and uniform in the initial configuration and in
all common Brownian paths for which the countably many free group processes
exist. Hence the finite processes converge coordinatewise, uniformly on
compact time intervals, to a continuous process on the original countable
configuration product. Passing in V14 proves its drift is b^infinity. The
same inequality with w=0 and the iterated remainder above proves pathwise
uniqueness for that initial configuration and Brownian family.

Let T(t) be its semigroup on continuous functions. For smooth cylinder F,
V16 bounds ||T_L(t)F-T(t)F||infinity by the finite sum of its original edge
Lipschitz constants times the right side. Thus convergence is uniform in
configuration and compact time. Smooth cylinders are uniformly dense in the
continuous functions on the compact product; the contraction property extends
this convergence to that whole space. Positivity and preservation of constants
pass to the limit. The semigroup law follows by taking the limit in
T_L(t+s)=T_L(t)T_L(s), using the two uniform convergences and contraction.

For a fixed smooth cylinder F the exact finite generator satisfies

    ||A_L F||infinity
       <=kappa||K F||infinity+16kappa xi sum_e||X_e F||infinity, (V17)

uniformly in L, including outside links where b^L is zero. Integrating the
finite generator proves ||T_L(t)F-F||infinity<=t times this constant. Passing
to the limit and using density proves strong continuity of T(t). The drift
convergence similarly proves F is in its generator domain and

    A_infinity F=kappa K F-2kappa sum_e,alpha
                             b_e,alpha^infinity X_e,alpha F. (V18)

All derivatives of F here are on its actual finite support; all dependence
of b^infinity on the remaining configuration stays in the formula.

## V6. Actual vacuum representation, spectral gap, and all local correlations

Finite reversibility, V13, uniform semigroup convergence and the full weak
measure limit V3 give, for continuous F,G,

    int conjugate(F) T(t)G dnu = int conjugate(T(t)F) G dnu,
    int T(t)F dnu=int F dnu.                              (V19)

Both sides use the original conjugate-linear first entry. Therefore T(t) extends to a self-adjoint Markov contraction
semigroup on L^2(nu). Strong continuity follows from the already proved
uniform continuity on continuous functions and their L^2 density. Its
nonnegative self-adjoint generator is the ground-relative A_infinity.

The full finite inside scalar gap is at least kappa d_xi. Every free outside
link has original scalar gap 3kappa/4, and d_xi<=1/2. Conditional variance and
the two original product factors show that the extended finite semigroup has
centered norm at most exp(-kappa d_xi t) on cylinder functions. More explicitly,
the product vacuum is one, the two constant/nonconstant decompositions are
orthogonal, and on every nonconstant product component at least one factor
has this decay. Completing the finite-variable tensor expansions proves the
bound without an assumed independence inside the interacting box.

The integrands T_L(t)F converge uniformly, and nu_L converges weakly, so the
squared L^2 inequality passes to the limit. Density gives

    ||T(t)(F-nu F)||_L2(nu)
       <=exp(-kappa d_xi t)||F-nu F||_L2(nu),
    A_infinity|_(1 perpendicular)>=kappa d_xi.            (V20)

The original gauge action commutes with every finite semigroup and preserves
its vacuum. Uniform convergence passes both facts to T(t),nu, so V20 holds
on the complete centered physical subspace as well. This construction has a
unique unit constant vacuum in its Hilbert space, by V20. It concerns the
unique limit of the specified positive finite-box vacua and dynamics; no
unexamined family of other infinite-volume quantum representations is assigned
to this statement.

The vacuum representation is explicit:

    H_infinity=L^2_phys(nu), vacuum=1,
    pi_infinity(O)F=OF,
    T(t)=exp(-t A_infinity).                              (V21)

For a finite time-ordered local list, the original finite vacuum expression
has the exact ground-state transform

    <psi_L, O_0 exp(-t_1(H_L-E0,L)) O_1 ...
                  exp(-t_m(H_L-E0,L)) O_m psi_L>
     =int O_0 T_L(t_1)(O_1 T_L(t_2)(...T_L(t_m)O_m))dnu_L. (V22)

All O_i are the original bounded continuous physical multiplication observables,
and all t_i>=0 are original physical times. Repeated uniform convergence and
the measure limit return V22 to the same formula with nu,T. Thus **all such
local Euclidean-time vacuum correlations converge along the full box sequence**.
The positive-time reflection Gram remains a squared Hilbert norm, by V19–21.
No spatial continuum symmetry or ultraviolet limit is asserted by this fact.

The elementary loop satisfies the nonzero variance and two-sided correlation
bounds U54–55 with this unique limit. In particular the limiting physical
Hilbert space has a nonzero centered vector of finite energy. The two compactified
spectral endpoint atoms remain zero at fixed a,g, by U51–53.

Finally the correlation Hilbert space of U53 has a complete typed identification
with V21. Send its time symbol [O,t] to T(t)(O-nu O). Its pairings are exactly
the limiting original correlations, so it descends through the actual null
space to an isometry. Its range is dense because t=0 includes the entire
centered physical cylinder algebra; gauge averaging proves that algebra is
dense in the physical L^2 space. Thus it extends to a unitary, with inverse
given by completion of the zero-time cylinder vectors. It intertwines time
translations and T(t), and therefore the self-adjoint generators and their
spectral measures. This removes the unspecified closed-range complement that
was retained in the earlier subsequential construction through an actual
surjective map, rather than declaring it absent. This complement is the one inside the
correlation Hilbert space just identified. The original bounded-regulator-
sequence comparison and its kernel remain their separately defined maps;
no vanishing of that whole sequence kernel is inferred here. The finite full-
domain bound U23 already controls energies of every such state sequence.

The cylinder form of U29 is carried into this semigroup form by the original
coordinate identity q(F,G)=kappa int sum conjugate(XF)XG dnu. All closed-form
comparisons made in U53 retain that domain statement. The primary dynamical
realization here is the direct process/semigroup limit V12–22.

## V7. The extensive ground energy and its volume limit

The original scalar ground energy is also retained quantitatively. From U17,
with the original Haar integral,

    E0,L=2kappa xi |P_L|-kappa int_H sum_e |b_e^L|^2.

Write b_e^0=(xi/3)sum_(p containing e)X_e W_p, as in the predecessor. At
xi<=1/16384 its proved actual remainder obeys
|b_e^L-b_e^0|<=A_*xi^2, A_*=256/9. The complete original Haar identity is

    int_H sum_e |b_e^0|^2=xi^2 |P_L|/3.                   (V23)

Indeed int_H W_p W_q=delta_pq: unequal faces have an unmatched original
fundamental link, and the equal trace has second moment one. Integration
by parts and K W_q=3W_q give int_H sum_e X_e W_p.X_e W_q=3delta_pq.
Multiplication by xi^2/9 proves V23, including all cross terms.

The actual local bound |b_e^0|<=r_e xi/3 and the complete squared difference
then give

    |E0,L-kappa |P_L|(2xi-xi^2/3)|
      <=kappa [(2048/27)|P_L|xi^3+(65536/81)|E_L|xi^4].    (V24)

Here sum_e r_e=4|P_L| was used exactly; the two coefficients are
8A_*/3 and A_*^2. With the original counts
|E_L|/|P_L|=(2L+1)/(2L)<=5/4, this also supplies an explicit per-plaquette
remainder while retaining the full energy and its extensive factor.

The energy per plaquette has a unique limit. The coefficient family V1 is
translation invariant on the infinite cubic graph and is invariant under
permutation of the three spatial axes, by its exact source recurrence.
Thus the original infinite Haar product gives the same value

    B_H=int_H |b_(0,1)^infinity|^2

at every bulk edge orientation. This is an integral of a bounded continuous
function supplied by U28; it is not assigned to the vacuum probability nu.
The constant Fourier coefficient in U17 is exactly why this Haar integral
occurs here. Edges a fixed distance from the boundary have b_e^L uniformly
close to that limiting function by U28. Boundary edges are a vanishing
fraction of the total for a fixed collar, and both drifts are bounded by
8xi. Taking first the volume and then the collar width to infinity proves

    E0,L/|P_L| -> kappa(2xi-B_H),
    |B_H-xi^2/3|<=(2048/27)xi^3+(65536/81)xi^4.           (V25)

The last constant uses the exact limiting ratio |E_L|/|P_L|=1 in V24.
All finite corrections remain in V24. This records the actual extensive
vacuum energy alongside the ground-relative gapped dynamics, rather than
silently setting the scalar term to zero.

## Scope and antecedents

The completed limit is spatial infinite volume with lattice spacing a>0 and
g>=8. Both original couplings and the continuous physical time remain.
The mass lower bound is kappa d_xi. The original running path g_n->0 eventually
leaves this proved interval, exactly as U56 records. The fixed-g change a->0
has the divergent physical lower edge and endpoint transport U57. No
four-dimensional smooth-continuum Yang–Mills construction or positive finite
continuum mass has been obtained by replacing either parameter map.

[DC] Patrick Rebeschini and Ramon van Handel, *Comparison Theorems for Gibbs
Measures*, arXiv:1308.4117 (2013), is a modern primary reference for the
Dobrushin/Markov-chain comparison method. Its abstract was inspected for
attribution; V5–9 supply the full elementary coupling proof used here and
evaluate its input on the actual vacuum interaction. No theorem from that
paper is invoked with unchecked hypotheses.

Finite Stratonovich equations on a compact group and their product rule are
used on their usual smooth global coefficient domains. The infinite-volume
step is proved explicitly by the original group-flow transformation V14 and
its complete summable comparison V15–16; no infinite-dimensional SDE existence
assertion is used as a premise. All source Hilbert pairings remain specified.

The exact checker verifies the scalar influence constants, finite conditional
interpolations, signed support compatibility, matrix comparison identities,
majorant rows and full matrix powers. These fixtures accompany the complete
analytic measure/dynamical proof above. No new Lean or independent external
verification is claimed.


---

# Chapter 15 — 20260916-cubic-linearized / CUBIC_SOURCE.md

Original text path: `workbench/yang-mills/continuations/20260916-cubic-linearized/CUBIC_SOURCE.md`.

# The complete connected cubic vacuum source in original SU(2) link coordinates

16 September 2026. This note executes the first of the two tasks retained in the delivered gauge-native checkpoint: calculate the connected third logarithmic-vacuum coefficient. `LINEARIZED_RETURN.md` executes the second task on the same coefficients. The preceding delivered second-source result had endpoint g^2 = sqrt((32+sqrt(354))/3); that stronger saved result is the comparison here. No historical-priority claim or independent analytical-review claim is made.

## C1. Original operator and source

Fix L>=2, vertices {-L,...,L}^3, every contained positively oriented nearest-neighbor edge e=(n,i), and every contained plaquette p=(n;i,j), i<j. Its actual word is

    W_p=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)).

Put T_alpha=-i sigma_alpha/2, X_e,alpha f=d/dt f(...,exp(t T_alpha)U_e,...) at zero, E_e=-sum_alpha X_e,alpha^2, and K=sum_e E_e. The Hilbert space has original product Haar probability dU; the physical subspace consists of vertex-gauge invariant functions, including all boundary vertices. Retain

    H=kappa K+kappa xi(2M-S),  S=sum_p W_p,  M=|P_L|,
    kappa=2g^2/a,  xi=1/(4g^4),  a,g>0.                         (C1)

Operator and form domains are the physical parts of H^2 and H^1 on the original compact product. The potential is smooth and bounded at each finite L. The actual vacuum is smooth and strictly positive. These original domains and the ground-state identity are supplied in `finite_box_weak_coupling_physical_gap.md` at Git fab69fdc4ac197159b8e6ae8d73a82bde2b20d55, blob dfee77c0ca0d6ed897c4172fcbfe23cd9d10d313, section 1.

Let P_H f=int f dU, Q_H=I-P_H, and Gamma(f,h)=sum_(e,alpha) (X_e,alpha f)(X_e,alpha h). Define, on zero-Haar-mean physical coefficients,

    B(f,h)=K^(-1) Q_H Gamma(f,h),
    v=xi v_1+B(v,v),   v_1=S/3,
    v_n=sum_(i=1)^(n-1) B(v_i,v_(n-i)).                     (C2)

The inverse K^(-1) acts only on actual nonconstant representation blocks. Scalars removed by Q_H remain recorded. Once the series is summed, set

    c_L=-(1/2)log int exp(2v)dU,
    psi=exp(v+c_L),  C_L=int Gamma(v,v)dU,
    E_0=2kappa xi M-kappa C_L.                             (C3)

The companion proof constructs convergence and proves that these are the original vacuum and energy. No vacuum, measure, or coupling is assigned from the auxiliary coefficient norm below.

## C2. Original Fourier coefficients and the two spin budgets

In the original product spin basis write f_j(U)=Tr(A_j pi_j(U)), and c(j)=sum_e j_e(j_e+1). For each original nonempty union label S_0 retain A_(S_0,j), even when its active spin support is smaller. A zero coefficient at a present union is retained at that union. Assembly sums these matrices for each j. Its kernel consists exactly of coefficient families with sum_(S_0) A_(S_0,j)=0 for every j. The differences between an occurrence at S_0 and its occurrence at the actual active support span this kernel and retain the original coefficient matrices.

The auxiliary coefficient norm and budgets are

    ||f||loc=max_a sum_(S_0 contains a,j!=0) c(j)||A_(S_0,j)||_1,
    m(f)=max_a sum_(S_0 contains a,j!=0) (sum_e j_e)||A_(S_0,j)||_1,
    t(f)=sup_e sum_(S_0 contains e,j!=0) j_e||A_(S_0,j)||_1.       (C4)

Every nonzero physical Fourier block obeys c(j)>=6j_e. To verify the gauge input, at each endpoint v of e the actual invariant vertex tensor gives j_e<=sum_(f incident v,f!=e)j_f. The other edges A_e at both endpoints therefore have total spin at least 2j_e. Their remote endpoints are distinct because the cubic graph has no triangles. At these remote endpoints the same invariant inequality gives sum_(f in A_e)j_f<=2 sum_(f outside A_e union {e})j_f; each exterior edge is counted at most twice. Thus sum_f j_f>=4j_e. For every nonzero half-integer spin, j(j+1)>=3j/2. This proves

    c(j)>=6j_e,  sum_e j_e<=2c(j)/3,
    t(f)<=||f||loc/6,  m(f)<=2||f||loc/3.                 (C5)

The gauge tensor exists in every physical coefficient block: decomposing at a vertex is an orthogonal decomposition under that vertex's unitary representation, and the invariant projection kills a block without an invariant intertwiner. This proves the use of the spin inequalities for the actual coefficients. In particular every nonconstant physical block has c(j)>=3.

The full coefficient-product inequality is

    sum_output ||A_output(f_j h_k)||_1<=||A_j||_1||A_k||_1,
    ||A(X_e,alpha f_j)||_1<=j_e||A_j||_1.                 (C6)

For the first, the product coefficient is A_j tensor A_k. Unitary decomposition of the original tensor representations, pinching to all diagonal irreducible blocks, and partial trace over their multiplicity spaces give the actual product coefficients. Pinching is an average of unitary conjugations and has trace-norm bound one. The partial-trace bound follows from |Tr((Z tensor I)A)|<=||A||_1 for ||Z||op<=1. This retains every output multiplicity. The second bound uses the original spin-generator operator norm j_e; all three generator indices remain in Gamma.

For an anchor in the first input union, the absolute product sum is at most 3m(f)t(h). Anchoring in the other input gives 3m(h)t(f); double counting their intersection is a bound. Output c(j) cancels the exact inverse Casimir in C2. Hence

    ||B(f,h)||loc<=3[m(f)t(h)+m(h)t(f)],
    ||B(f,h)||loc<= (2/3)||f||loc||h||loc.                 (C7)

These are estimates on the original labelled coefficient source. The physical pairing is still int rho conjugate(f)h dU, with rho=psi^2, and its energy pairing is kappa int rho sum conjugate(Xf)Xh dU.

## C3. Original loop norms and the complete second coefficient

For a simple original closed link loop of length ell, let t be the number of local maxima of n_1+n_2+n_3 along the loop; the number of minima is also t. At extrema the fundamental coefficient tensor has the original alternating two-index contraction, of Euclidean norm sqrt(2). At each other vertex it has the two-dimensional identity contraction. Separate permutations of original row and column tensor indices expose their tensor product. Their singular values give ||A_loop||_1=2^(ell-t)<=2^(ell-1). No inversion of one link is asserted to preserve a tensor trace norm. For a spin-j plaquette, the same four contractions have dimension 2j+1 and one maximum/minimum pair, giving norm (2j+1)^3. In particular

    ||A(W_p)||_1=8, ||A(chi_1(Omega_p))||_1=27,
    ||A(chi_(3/2)(Omega_p))||_1=64.                       (C8)

These formulas also follow from the literal plaquette index matrix: for spin 1/2 its nonzero entries are

    A_[(i1,i2,1-i2,1-i3),(i0,i1,1-i3,1-i0)] += (-1)^(i0+i2).

There are four nonzero singular values, each two. Keeping indices 0,...,2j and the invariant alternating spin-j form gives (2j+1)^2 singular values, each 2j+1, for the character plaquette.

For adjacent p,q, write P_0 for Haar integration of their shared edge in W_pW_q and P_1=I-P_0 on that product. The two actual Casimirs are 9/2 and 13/2. If x,y denote the two original trace coefficient norms, the exact six-link boundary formula and C6 give

    P_0(W_pW_q)=(1/2)W_boundary(p,q),
    x<=16, x+y<=64.                                      (C9)

It follows either by integrating the original shared matrix entries, int U_ab conjugate(U_cd)=delta_ac delta_bd/2, or by the equivalent SU(2) alternating contraction in its inverse traversal. The boundary orientation is the original oriented concatenation after that contraction.

The Casimir product rule is

    2Gamma(f,h)=(c_f+c_h)fh-K(fh)                         (C10)

for actual Casimir eigenfunctions f,h. Since W_p^2=1+chi_1(Omega_p), its nonconstant self component has Casimir 8. Distinct nonadjacent plaquette products have Casimir 6. Applying C10 to C2 evaluates the entire second source:

    v_2=-(1/72)sum_p chi_1(Omega_p)
       +sum_{unordered adjacent {p,q}}
         [(1/27)P_0(W_pW_q)-(1/117)P_1(W_pW_q)].           (C11)

Nonadjacent terms have the exact multiplier 1/(3*6)-1/18=0 at their original union. Each edge lies in at most four self plaquettes and 42 unordered adjacent pair unions. The latter count is sum_(p contains e) deg(p)-binom(r_e,2)<=12r_e-binom(r_e,2)<=42. Thus

    ||v_1||loc<=32,   ||v_2||loc<=236.                    (C12)

Indeed each self term contributes at most 8*27/72=3; each pair at most x/6+y/18<=16/3.

## C4. All projectors have explicit original-coordinate formulas

For an edge carrying a finite product of the specified spin functions, let J_e be its complete allowed Clebsch-Gordan spin list. On that product space set

    P_(e,j)=product_(l in J_e,l!=j)
        [E_e-l(l+1)I]/[j(j+1)-l(l+1)],
    P_boldj=product_e P_(e,j_e).                          (C13)

Every denominator is a displayed nonzero rational number. The original compact SU(2) decomposition proves that C13 projects onto exactly that spin eigenspace, including its full multiplicity. Different-edge projectors commute. This is a finite polynomial in the original link derivatives, so all coefficient formulas below are effective coordinate formulas. In particular an explicit eigenvalue denominator is not an unspecified inverse problem.

For the cubic product there are five connected types: a self triple; a repeated adjacent pair; three distinct faces with two adjacency edges (path); three distinct faces sharing one edge (common-edge); or three faces forming a cube corner with three different shared edges. This exhausts the original coordinates: coplanar face adjacency is the square grid; two perpendicular faces determine their shared coordinate edge; a third face adjacent to both either contains that same edge or is the third face at one endpoint, with its other two shared edges. All other multisets are disconnected in edge adjacency.

## C5. The full cubic table

Each triple below is an unordered multiset of original faces. Each distinct choice of the outer face in 2B(v_1,v_2) occurs once, with the second coefficient already carrying its original unordered-pair multiplicity.

**Self {p,p,p}.** The contribution is

    -(1/81)W_p+(1/810)chi_(3/2)(Omega_p).                 (C14)

Its Casimirs are 3 and 15. The character product W_p chi_1=chi_(3/2)+W_p and C10 give K times C14 as chi_(3/2)/54-W_p/27.

**Repeated adjacent {p,p,q}.** Let F=(W_p^2-1)W_q. On the shared edge its allowed spins are 1/2 and 3/2. Then the contribution is

    -(11/4212)P_(1/2)F+(11/11232)P_(3/2)F.              (C15)

The respective total Casimirs are 9 and 12. Here the first projector has the concrete recoupling identity

    P_(1/2)F=(4/3)W_p P_0(W_pW_q)-(1/3)W_q.             (C16)

To prove C16, expose the shared original unit quaternion u. The two traces can be written 2u dot v, 2u dot w with v,w unit quaternions formed from the unchanged remaining path products (inverse orientations use their exact quaternion conjugates). Original Haar moments are int u_i u_j=delta_ij/4 and
int u_i u_j u_k u_l=(delta_ij delta_kl+delta_ik delta_jl+delta_il delta_jk)/24. The linear harmonic part of (u dot v)^2(u dot w) is [u dot w+2(v dot w)(u dot v)]/6. Also P_0(W_pW_q)=v dot w. These equations give C16 pointwise, for every original remaining path product.

For full coefficient verification, put H=P_(1/2)F, J=P_(3/2)F, z=P_0(W_pW_q). Then
W_p z=(3H+W_q)/4 and W_p P_1(W_pW_q)=H/4+J+3W_q/4. The two W_q coefficients in K v_3 from the adjacent source are 1/72 and -1/72; they cancel exactly. The self-source product has only H,J. The H coefficient in K v_3 is -1/72-1/2808-1/108=-11/468; the J coefficient is 5/702+1/216=11/936. Division by the original 9 and 12 gives C15. The cancelled W_q component remains a present zero at the original seven-link union.

**Distinct path.** Let F=W_pW_qW_r. On its two distinct shared edges, use P_(s,t), s,t in {0,1}. With n=s+t, its total Casimir and coefficient are

    c=6+2n;
    n=0: 1/162;  n=1: -11/8424;  n=2: 1/3510.          (C17)

The entire contribution is the sum of those four projected functions times their specified coefficients. For a selected channel, there are exactly two nonzero outer-face terms. With (c_0,a_0)=(9/2,1/27) and (c_1,a_1)=(13/2,-1/117), their sum is

    [a_s(3+c_s-c)+a_t(3+c_t-c)]/(3c),

which evaluates to C17. This verifies each factor without a coordinate replacement.

**Distinct common-edge triple.** On the single shared edge, retain the whole spin-1/2 multiplicity space and spin-3/2 space. Their Casimirs and coefficients are

    c=15/2: -2/1755;  c=21/2: 2/2457.                  (C18)

On the original tensor (C^2)^(tensor 3), the three pair singlet projectors obey

    P_0^(12)+P_0^(13)+P_0^(23)=(3/2)P_(total 1/2).       (C19)

One verification is P_0^(ij)=1/4-J_i dot J_j, followed by expansion of (J_1+J_2+J_3)^2. The eigenvalues are 3/4 and 15/4. Thus the total singlet sum has values 3/2 and zero; this proves C19 including both copies of spin 1/2. The pair projectors need not commute, and no product of them is used. Under the original trace map,

    P_(1/2)F=(2/3)sum_outer W_r P_0(W_pW_q).

In C10 the summed pair-spin-zero multiplicity is 3/2 on total spin 1/2 and zero on spin 3/2; the pair-spin-one multiplicities are 3/2 and three. Substitution gives C18.

**Distinct cube corner.** On its three different shared edges use P_(s,t,u), n=s+t+u. The coefficients and Casimirs are

    c=9/2+2n;
    n=0: 2/81; n=1: 34/13689; n=2: -38/17901;
    n=3: 2/2457.                                       (C20)

The entire n=1 projection is exactly zero. At the central original vertex it would have one spin-one edge and two spin-zero edges, which has no invariant vector. We retain the displayed pre-zero coefficient and its zero projected function. The channel coefficient before that zero follows from

    [(3-n)a_0(3+c_0-c)+n a_1(3+c_1-c)]/(3c).

Moreover P_(0,0,0)F=(1/4)W_boundary, a six-link loop. Write the original three face traces as tr(U_a A U_b^-1), tr(U_b B U_c^-1), tr(U_c C U_a^-1). Integrating U_b and U_c supplies two factors 1/2 and leaves tr(U_a ABC U_a^-1)=tr(ABC); integration of U_a leaves this same trace. This proves the complete factor 1/4 and its original boundary product.

Every disconnected triple has zero source because either its second coefficient is zero by C11 or the outer derivative has no original edge in common with that second coefficient. Thus C14–20 calculate all of v_3, with all original union labels and all cancelled or zero channels retained.

## C6. Evaluate the whole cubic source bound

For one cluster the following are bounds in the original Casimir-weighted trace norm:

    self: 40/27;
    repeated adjacent: 66/13;
    path: 1408/351;
    common-edge: 512/117;
    corner: 3504/351.                                   (C21)

For self use 3*8/81+15*64/810=40/27. For repeated adjacent, the two output norms have sum at most 27*8=216. Their largest absolute Casimir-weighted coefficient is 11/468, giving 66/13.

For a path let x_st denote the original norms of its four projections. C6, C9 and the actual boundary integration give

    sum x_st<=512, x_00<=32,
    x_00+x_01<=128, x_00+x_10<=128.

The double spin-zero component is (1/4) times the original eight-link boundary loop, so C8 gives 32. Each single spin-zero projection is the original six-link boundary times the remaining plaquette, divided by two, giving 16*8=128. The absolute Casimir-weighted norm is exactly bounded by

    [3 sum x_st+8(x_00+x_01)+8(x_00+x_10)+20x_00]/1053
    <=4224/1053=1408/351.

For a common-edge triple, sum of both complete projected coefficient norms is at most 8^3=512. Both absolute Casimir-weighted coefficients are 1/117. For a corner the total is at most 512, x_000<=8 by its six-link boundary divided by four, and the other nonzero weighted coefficients are at most 19/1053. Therefore its bound is

    (19*512+98*8)/1053=3504/351.

For each original anchor edge the numbers of clusters in C21 are bounded respectively by

    4, 84, 460, 40, 24.                                 (C22)

Here is a counting proof of the three distinct-face counts. In a cubic periodic counting grid of side at least nine, the two-neighbor patterns are in bijection with their original infinite-grid local coordinates. This is only a finite combinatorial enumeration; no Hamiltonian or measure is transported to that grid. There are three faces per cell, twelve neighbors per face, twelve common-edge triples per cell, and eight corner triples per cell. The number of centered adjacency wedges per cell is 3*binom(12,2)=198. Subtracting three for every triangle leaves 138 paths. Their unions contain ten original edges; common-edge unions also contain ten, and corner unions nine. Translation and axis permutation are explicit bijections of this incidence count. Division of total incidences by three edges per cell gives 460,40,24. Equivalently `geometry.py` enumerates all four anchor faces, all first neighbors, and all second neighbors and retains the resulting original coordinates. The 42 adjacent pairs each have two repeated-face choices. Any finite-box cluster injects into the corresponding original infinite-grid list, proving the same upper counts at boundaries.

Summing all five contributions proves

    ||v_3||loc <= 4*(40/27)+84*(66/13)+460*(1408/351)
                  +40*(512/117)+24*(3504/351)
               =944984/351.                             (C23)

The predecessor's bound obtained before evaluating this source was 30208/3. C23 is less than 2693. The sharper bound follows from the actual channel coefficients and original support geometry; the complete norm remains an upper bound rather than an assigned equality.

## C7. Original fourth vacuum-energy coefficient, with an independent calculation

The link-center involution

    (Zf)(U)=f((s_e U_e)_e), s_(n,i)=(-1)^(sum_(j<i)n_j)

preserves Haar, the gauge action and K, and changes the sign of every original plaquette trace. Hence Z v_n=(-1)^n v_n by C2. It also gives the literal signed-parameter operator identity Z H(xi) Z=H(-xi)+4kappa xi M I. Negative xi is used here solely as the algebraic/analytic source coordinate; no negative physical g is introduced. Thus E_0-2kappa xi M is even.

Let J be the original number of unordered adjacent plaquette pairs. The complete coefficient is

    E_0=2kappa M xi-kappa M xi^2/3
         +kappa(5M/216-2J/1053)xi^4+O(xi^6).            (C24)

To verify it directly from the vacuum source, the only v_3 component pairing with v_1 in Haar energy is the self -W_p/81 in C14. The repeated lower component cancels as proved in C15–16. A product of three distinct faces and one testing face has an edge with odd occurrence: a nonempty set of at most four distinct squares cannot have every edge even, because each other square shares at most one of a chosen square's four edges. Its Haar integral is zero by the center change on that edge. Distinct v_2 labels have the same unmatched-edge argument or different spin sectors. The actual component masses are ||chi_1||_H^2=1, ||P_0(W_pW_q)||_H^2=1/4 and ||P_1(W_pW_q)||_H^2=3/4. Therefore

    int Gamma(v_1,v_3)=-M/81,
    int Gamma(v_2,v_2)=M/648+2J/1053,
    [xi^4]C_L=2*(-M/81)+M/648+2J/1053
              =-5M/216+2J/1053.

Equation C3 proves C24, including its sign.

An independent Rayleigh–Schrodinger coefficient calculation for the original K-xi S gives

    [xi^4](E_0/kappa)=M^2/27
          -(1/9)<Q_H S^2,K^(-1)Q_H S^2>_H,
    <Q_H S^2,K^(-1)Q_H S^2>_H
       =M/8+(2/3)binom(M,2)+(2/117)J.                  (C25)

For completeness, with Haar-constant vacuum coefficient fixed at one, the first two wavefunction coefficients are u_1=S/3 and u_2=K^(-1)Q_H S^2/3. The second energy coefficient is -M/3. Testing the order-three eigen-equation against S and then the order-four constant equation gives the first line of C25. The nonconstant self sector is chi_1/8; a disjoint pair contributes 2/3; an adjacent pair contributes 4[(1/4)/(9/2)+(3/4)/(13/2)]=80/117=2/3+2/117. Cross terms vanish by the same original edge parity. Substitution reproduces C24 exactly.

With m=2L the complete box counts are M=3m^2(m+1), J=6m(3m^2-1). At L=2, C24's fourth coefficient is 1198/351. As L increases, J/M tends to six and its fourth coefficient per plaquette tends to 11/936. On a planar square array the corresponding ratio tends to two, giving 163/8424; the plane-to-space operator defect is recorded in the companion literature section. These are source coefficients, with the exact finite-box counts kept before their limits. The companion note supplies an explicit all-higher-order remainder for C24.

## C8. Verification scope

The independent original-link checker differentiates the actual oriented plaquette products in 2Gamma(v_1,v_2), while the receiving calculation uses C14–20 and Haar projectors. It checks all 612 anchored multisets at two exact rational quaternion assignments. The 24-cell separately verifies the harmonic recouplings using all Haar moments through degree five. The original eight-by-eight singlet matrices verify C19 and reject their false commutation. These finite tests accompany the full coordinate and representation proofs above; they do not replace them or certify a continuum limit.


---

# Chapter 16 — 20260916-cubic-linearized / LINEARIZED_RETURN.md

Original text path: `workbench/yang-mills/continuations/20260916-cubic-linearized/LINEARIZED_RETURN.md`.

# The full linearized residual and its return to the original physical gap

16 September 2026. This is the second executed calculation, on exactly the original operators and source coordinates of `CUBIC_SOURCE.md`. It evaluates the full residual at xi v_1+xi^2 v_2, bounds the actual linearized inverse and every nonlinear correction, and returns the result to the complete physical form domain. The proof does not assume a spectral gap to construct this inverse.

## L1. Two sharper spin budgets for the evaluated second source

Retain C1–13, including all union labels. The first source has

    m(v_1)<=64/3,   t(v_1)<=16/3.                         (L1)

An anchor meets at most four plaquettes; each has coefficient norm 8/3, total spin two and anchor spin 1/2. This proves both numbers.

For the actual second source C11, its self contributions to m are at most six. On a pair, with the original x<=16, x+y<=64, its total-spin weighted norm is x/9+4y/117<=400/117. There are at most 42 anchored pairs. Thus

    m(v_2)<=6+42*(400/117)=5834/39.                       (L2)

For t(v_2), self terms contribute at most 3/2. At most six pairs share the anchor itself: their spin-zero term has anchor spin zero, and their spin-one contribution is at most 64/117 per pair. In the other at most 36 pairs, the anchor occurs once and its spin is 1/2, giving at most (1/2)(x/27+y/117)<=176/351. Hence

    t(v_2)<=3/2+6*(64/117)+36*(176/351)=137/6.            (L3)

All original boundary patterns inject into these bulk lists. C7 and C5 now prove

    ||B(v_1,h)||loc<=(64/3)||h||loc,
    ||B(v_2,h)||loc<=(1566/13)||h||loc,
    ||B(v_2,v_2)||loc<=799258/39.                        (L4)

For the middle coefficient, 3[m(v_2)/6+(2/3)t(v_2)]=1566/13. For the last, 6m(v_2)t(v_2)=799258/39. The two inputs have their actual separately evaluated budgets; neither is replaced by a generic unknown vector.

## L2. Evaluate the complete residual, including its quartic source

Set x=xi as the same original source parameter, and define

    q_2=xv_1+x^2v_2,
    R_2=xv_1+B(q_2,q_2)-q_2=x^3v_3+x^4b_22,
    b_22=B(v_2,v_2),
    J_2 h=2B(q_2,h),  L_2=I-J_2.                        (L5)

The source v_3 is the complete five-family table C14–20. Here is also a finite formula for every component of b_22, avoiding an unevaluated Casimir inverse. Let mu enumerate the original terms of C11, with functions F_mu and coefficients a_mu. Their Casimirs are respectively 8,9/2,13/2 and their a_mu are -1/72,1/27,-1/117. Each F_mu has definite original edge spins, including its zero shared edge in the P_0 channel. For every ordered (mu,nu), let J_e be all spins from |j_mu,e-j_nu,e| to j_mu,e+j_nu,e in unit steps. These are at most two. With the literal polynomial projectors C13,

    b_22=sum_(mu,nu) a_mu a_nu
          sum_(boldj with c(boldj)>0)
          [c_mu+c_nu-c(boldj)]/[2c(boldj)]
          P_boldj(F_mu F_nu).                           (L6)

Each input, edge-spin range, polynomial projector, coefficient and denominator is now specified in original coordinates. This is a finite full-coefficient formula at every finite L. For disjoint active supports c(boldj)=c_mu+c_nu and the corresponding source is exactly zero at its original union. Output constants are retained outside Q_H, as below. No truncation of the full Hamiltonian is performed.

For example, the self/self term at one original plaquette is

    b_22^(p,p)=chi_1(Omega_p)/10368-chi_2(Omega_p)/31104,
    int Gamma(v_2^(p),v_2^(p))=1/648.                   (L7)

This follows from chi_1^2=1+chi_1+chi_2, with Casimirs 0,8,24 and the original factor 1/72^2. The entire removed scalar for the original q_2 is

    C(q_2)=int Gamma(q_2,q_2)
          =M x^2/3+x^4(M/648+2J/1053).                  (L8)

The odd term is zero by the original center involution in C7. Thus the full residual of the approximate exponential has the exact operator identity on smooth original functions

    e^(-q_2) H e^(q_2)
      =kappa[K-2Gamma(q_2,.)]
       +kappa[2Mx-C(q_2)]I-kappa M_(K R_2).             (L9)

Here M_(K R_2) is multiplication by the displayed original polynomial. To verify L9, expand the original Laplacian on e^(q_2)f and use K R_2=xS+Q_H Gamma(q_2,q_2)-Kq_2. This retains both the scalar energy and every quartic residual term.

## L3. The full linearized inverse and nonlinear correction

For every source h, C23 and L4 give

    ||J_2 h||loc<=ell(x)||h||loc,
    ||R_2||loc<=delta(x),
    ell(x)=(128/3)x+(3132/13)x^2,
    delta(x)=(944984/351)x^3+(799258/39)x^4.             (L10)

No derivative term is omitted: L_2 is the Frechet derivative of v-xv_1-B(v,v) at q_2, because B is bilinear and symmetric. Put

    D(x)=(1-ell(x))^2-(8/3)delta(x)
        =[46457856x^4+183150656x^3+18324072x^2
          -1168128x+13689]/13689.                       (L11)

Let alpha be the unique root of D in (17/1000,171/10000). This is the first positive root. Indeed D(0)=1; D'' has positive coefficients on x>=0, and D'(171/10000)<0. Hence D'<0 on that whole interval. Exact rational endpoint signs give D(17/1000)>0>D(171/10000). In particular D>=0 on [0,alpha], and ell(x)<=ell(171/10000)<1 there.

The Neumann sum of the ACTUAL J_2 constructs

    L_2^(-1)=sum_(j>=0)J_2^j,
    ||L_2^(-1)||<=1/(1-ell(x)).                         (L12)

Its complete source coordinates are unchanged. For w=v-q_2 the full equation is

    L_2 w=R_2+B(w,w).

Define z=L_2^(-1)R_2 and C=L_2^(-1)B. Then

    ||z||loc<=z_*:=delta/(1-ell),
    ||C(f,h)||loc<=c_*||f||loc||h||loc,
    c_*=(2/3)/(1-ell).                                  (L13)

Construct w explicitly by the binary-tree recurrence w_1=z, w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i)). Its terms have bounds

    ||w_n||loc<=Catalan_(n-1) c_*^(n-1) z_*^n.

The discriminant L11 gives theta_*=4c_*z_*<=1. The series converges absolutely on the ENTIRE closed interval, and its sum satisfies the full equation. Its bound is

    w_*(x)=(3/4)[1-ell(x)-sqrt(D(x))],
    ||v-q_2||loc<=w_*(x).                               (L14)

At theta_*=1 the endpoint is obtained from the actual convergent Catalan series, not from a strict nonlinear contraction. Its omitted-tree tail after N>=1 is at most

    [3(1-ell)/4] theta_*^(N+1) binom(2N,N)/4^N
     <=[3(1-ell)/4] theta_*^(N+1)/sqrt(N+1).              (L15)

To prove it, use Catalan_n/4^n=2(b_n-b_(n+1)), b_n=binom(2n,n)/4^n, and telescope. The original linear-source truncation has the independent exact identity and bound

    L_2^(-1)R_2-sum_(j=0)^N J_2^jR_2
        =J_2^(N+1)L_2^(-1)R_2,
    norm <=ell^(N+1)delta/(1-ell).                       (L16)

Thus both infinite operations have explicit residuals. Every application of J_2 adds at most two original plaquettes to its union label, and the initial R_2 has at most four. The finite linear sum in L16 is supported in actual unions of at most 4+2N plaquettes. The tree recurrence retains all further unions and all original coefficient multiplicities.

At each finite L the labelled c-weighted source is complete. Its global c-weighted sum is bounded by |E_L| times the local norm. The original spin-generator estimates bound all first and second link derivatives by that sum. Therefore the series gives a C^2 function v on the compact original product and permits the full source equation to be summed. With C3, direct differentiation gives H psi=E_0 psi. Elliptic regularity makes psi smooth. For every smooth h,

    q_(H-E_0)(psi h)=kappa int psi^2 sum_i |X_i h|^2.

Multiplication and division by the positive smooth psi preserve H^1 at this finite L. This proves E_0 is the actual lowest energy and identifies psi with the original positive unit vacuum; a second ground state divided by psi has zero derivative and is constant. Gauge invariance follows from the invariant source. This identification does not presume a gap.

The convergent construction is analytic for complex |x|<alpha by the same absolute coefficient majorants. At every original power x^n its unique formal coefficient is C2, so the new construction and the earlier source constructions agree coefficient by coefficient on their common domains. Their coefficient identity maps have literal inverse identities. No new source metric or different physical vacuum is selected.

## L4. Numerical endpoint and fully retained benchmark

Exact bisection and integer-square comparisons give

    0.0170787544707772675 < alpha < 0.0170787544707772677,
    3.825973052393385 < 1/(2sqrt(alpha))
                         <3.825973052393386.             (L17)

This is the new sufficient coupling threshold g^2. The cubic coefficient alone, with the old generic recurrence for higher orders, gives the intermediate discriminant

    D_3(x)=1-(256/3)x+(10720/9)x^2+(20714816/1053)x^3

and first root approximately 0.0166569913896066, or g^2 approximately 3.8741080015. The full linearized calculation L10–17 gives the additional improvement. Its source-specific m and t budgets are part of that gain.

At the exact original coupling g^2=4, x=1/64, a>0 and kappa=8/a,

    ell=28973/39936,
    ||L_2^(-1)||<=39936/10963,
    ||z||loc<=33836149/808280064,
    D=10028381/224280576,
    theta_*=439869937/1081686321,
    ||w||loc<=0.047293824576905,
    ||w-z||loc<0.005432.                                 (L18)

The displayed decimal bounds are outward rational bounds checked against L13–14. They bound the ACTUAL linear response and its complete further nonlinear correction. No value of an uncomputed vacuum integral is assigned. The total source satisfies

    ||v||loc<=32x+236x^2+w_*
       =(3/4)(1-sqrt D)+(719/13)x^2.                    (L19)

## L5. Return to the entire physical spectrum, using the evaluated spin budget

Use the actual ground-state transform A=psi^(-1)(H-E_0)psi=kappa(K-D_v), where D_v=2Gamma(v,.). Its physical pairing is int rho conjugate(f)h dU, rho=psi^2. C5, L1 and L3 give the sharper point-spin budget

    t(v)<=(16/3)x+(137/6)x^2+w_*/6.

For an original zero-Haar-mean coefficient family h, C6 and sum_e j_e<=2c(j)/3 yield

    ||D_v h||_X<=4t(v)||Kh||_X<=chi(x)||Kh||_X,
    chi(x)=1/2(1-sqrt D(x))-(1136/39)x^2.                (L20)

Here X is the full sum of original trace coefficient norms after assembly. The scalar output is also bounded by the same complete product estimate. To check L20 without its displayed cancellation, chi is exactly
4[(16/3)x+(137/6)x^2+w_*/6], a positive-coefficient majorant. This form proves its monotonicity. Its closed-endpoint value is strictly less than 1/2.

For an actual physical eigenfunction A f=lambda f with lambda>0, let h=Q_Hf. The source and physical-centered maps are

    f -> Q_Hf,
    h -> h-<h>_rho,
    <f>_rho=0, int_H h=0.                               (L21)

Both compositions are identities, and h is nonzero. The original eigen-equation gives

    (K-lambda/kappa)h=Q_H D_vh.

Every finite-regulator eigenfunction is smooth. Its original Fourier coefficients have summable c(j)||A_j||_1: Peter–Weyl Plancherel followed by Cauchy–Schwarz with sufficiently many Casimir powers gives this, since sum_j dim(j)^2(1+c(j))^(-N)<infinity for large N on the finite product. No volume-uniform smoothness constant is used. For 0<lambda/kappa<3, every actual nonconstant physical block has c(j)>=3, and therefore

    ||(K-lambda/kappa)h||_X
        >=[1-lambda/(3kappa)]||Kh||_X.

Combining with L20 proves lambda>=3kappa(1-chi). For lambda>=3kappa that inequality is automatic. The full compact spectral resolution gives, on the ENTIRE centered physical form domain,

    Delta_L>=kappa d(x),
    d(x)=(3/2)(1+sqrt D(x))+(1136/13)x^2,
    0<x<=alpha, L>=2, a>0.                              (L22)

Equivalently, x=1/(4g^4), kappa=2g^2/a and g^2>=1/(2sqrt(alpha)). The scalar-space version has the original free constant 3/4 and gives one quarter of L22. No excitation is declared physical merely from an unprojected color vector.

Because chi has positive power coefficients and increases on the interval, d decreases to d(alpha). The exact endpoint satisfies

    d(alpha)=3/2+(1136/13)alpha^2
             >61/40=1.525.                              (L23)

At the rational interior point and throughout its lower-x interval,

    g^2>=4 => Delta_L>1.8385 kappa,
    d(1/64)= (3/2)(1+sqrt(10028381/224280576))+71/3328
             =1.8385178195961905... .                    (L24)

Every a and exterior L factor remains in kappa. This is a lower bound for the full original physical spectrum, obtained from a convergent complete source rather than a finite-dimensional trial-space lower estimate.

## L6. The retained source complexes and their exact physical defect

At fixed x in the closed domain, define V_N=span{R_2,J_2R_2,...,J_2^N R_2} in the original labelled coefficient space V. At support N use the actual complex

    V_N --L_2--> V --0-->0,
    H^1_N=V/L_2 V_N.

The source inclusions and target identities commute. Since L_2 is invertible, the exact transported-kernel isomorphism is

    V_(N+1)/V_N -> ker(H^1_N -> H^1_(N+1)),
    [h] -> [L_2 h],
    inverse [L_2 h] -> [h].                             (L25)

Changing representatives by L_2V_N changes h by exactly V_N; this proves both inverse identities. The actual source R_2 has representative J_2^(N+1)R_2 after the primitive sum in L16 is subtracted. The same original support label survives on a zero receiving coefficient. These are the support-indexed quotient maps used by Split Zero; the formula retains the full primitive, not only its support flag.

The linearized source maps to the auxiliary differential operator by the exact square

    K L_2 h=Q_H[K-2Gamma(q_2,.)]h.                       (L26)

Its relation to the actual physical operator is the complete defect

    Q_H A h-kappa K L_2h=-2kappa Q_H Gamma(w,h).          (L27)

The bound from C5–7 is at most (2kappa/3)w_*||Kh||_X on the right. Equation L9 separately retains the multiplication residual and scalar of the approximate exponential. Thus the approximate section and actual physical dynamics are connected by specified maps and controlled, unremoved terms.

On the original centered physical form domain put d_Xf=(X_if)_i with norm squared kappa int rho sum_i |X_if|^2. Its inverse on its actual range is p_X(d_Xf)=f. The ground-state map U:f->psi f is unitary with inverse u->u/psi. The variational definition of the first excitation therefore gives exactly

    ||p_X||^2=1/Delta_L<=1/[kappa d(x)].                 (L28)

For an original physical conditional-expectation kernel, its closed restricted form has D_phys>=kappa d(x). All zero-shift primitive and response errors on that kernel consequently have the same inverse bound. The inclusion into the full scalar kernel intertwines the operators and resolvents when the original conditional expectation commutes with gauge averaging; that commuting property follows by changing variables in its actual vacuum conditional integral. No forcing or state Gram is altered by this return.

## L7. Explicit complete higher-order remainder for the energy coefficient

On the complex circle |x|=1/60, L19 is less than 7/10, verified by rational square bounds on D(1/60)=5458199/462003750. For each original link and each of its three generators, |X_e,alpha v|<=||v||loc/6. Hence

    |C_L(x)|<=|E_L| ||v||loc^2/12<49|E_L|/1200

on that circle. Analyticity inside alpha and the exact evenness from C7 give the Cauchy coefficient estimate and its full geometric tail:

    |E_0-2kappa Mx+kappa Mx^2/3
           -kappa(5M/216-2J/1053)x^4|
      <=(49kappa |E_L|/1200)
             (60|x|)^6/[1-(60|x|)^2],
    0<|x|<1/60.                                        (L29)

The scalar term 2kappa Mx and every extensive factor remain. This bounds all omitted orders, rather than assigning a numerical fourth-order polynomial as the exact energy. The complete finite-box coefficients M,J and the independent coefficient calculation are C24–25.

## L8. Literature crosscheck with the actual parameter maps

The exponential vacuum equation and connected loop expansions have established Hamiltonian lattice-gauge antecedents. The following comparisons are to inspected primary bodies, with their scope retained.

D. Schuette, Zheng Weihong and C.J. Hamer, *The Coupled Cluster Method in Hamiltonian Lattice Field Theory*, Phys. Rev. D55 (1997) 2974–2986, arXiv:hep-lat/9603026v1, equations (17), (21)–(26), (30) and (38), formulate the exponential vacuum and its linear excitation equation using original gauge-invariant loop/representation coefficients. Their dimensionless coefficient is x_C=2/g_C^4 and physical operator g_C^2[K-x_C S]/(2a). At fixed a, g_C=2^(3/4)g gives x_C=xi and

    H_original(a,g)=sqrt(2) H_C(a,2^(3/4)g)
                         +2kappa xi M I.                (L30)

Substituting both coefficients proves the complete identity, including the additive energy. With their Hermitian generator lambda_alpha=sigma_alpha/2, their multiplication commutator derivative is i X_alpha. Hence S_(mu mu)=K v and S_mu S_mu=-Gamma(v,v). Their equation (23) becomes exactly the original scalar equation C2–3 under S=v+c_L. No sign is inferred from an unnamed convention.

B. Dahmen, *Strong coupling expansion for scattering phases in Hamiltonian lattice field theories—II. SU(2) gauge theory in (2+1) dimensions*, arXiv:hep-lat/9412080, equations (1.7), (1.24), gives the original planar coefficient H_D'=(g_D^2/2)[K-h_D S], h_D=2/g_D^4, and the ground coefficient -M h_D^2/3. The exact return is g_D=2^(3/4)g and

    H_plane(a,g)=(sqrt(2)/a) H_D'+2kappa xi M I.          (L31)

This reproduces the -kappa M xi^2/3 term and the actual local Casimir denominators. The inspected second-order calculation does not independently certify our cubic norm or the quartic majorant.

P. Hui, X.-Y. Fang and T.-Y. Shi, *Approximated seventh order calculation of vacuum wave function of 2+1 dimensional SU(2) lattice gauge theory*, arXiv:hep-lat/0408035v1, equations (3), (4), (6), use g_H^2[K-(4/g_H^4)S]/(2a). The map g_H=2g gives

    H_plane(a,g)=H_H(a,2g)+2kappa xi M I.                 (L32)

Their section 2 explicitly defines subsequent finite-order/random-phase replacements. This contribution retains the exact product and every residual term in L5–16 instead. The earlier method and the existence of higher-order loop calculations are attributed; no claim that the general cubic expansion or exponential ansatz is new is made.

For the original planar edge subset inside the spatial cube let J_pi be cylinder pullback, with inverse on its image the original unused-link Haar integral. Fubini proves J_pi^*J_pi=I, and original differentiation gives K_3 J_pi=J_pi K_2. The full operator difference is exactly

    H_3 J_pi-J_pi H_2
      =kappa xi [2(M_3-M_2)-sum_(p outside plane)W_p]J_pi. (L33)

Thus local planar channels are compared by their actual inclusion, and all perpendicular and exterior plaquettes remain in L33. The common-edge and cube-corner contributions in C18–20 are calculated in the spatial graph rather than silently assigned a planar identity.

Primary URLs: https://arxiv.org/html/hep-lat/9603026v1 ; https://arxiv.org/pdf/hep-lat/9412080 ; https://arxiv.org/html/hep-lat/0408035v1 . Their cited formulae were read. The literature check establishes these parameter/equation correspondences; it does not establish a global novelty or best-known coupling-range claim.

## L9. Continuum path, completed scope, and the next actual quantity

The running test path remains a_n=a_0 2^(-n), g_n^2=1/c_n, c_n=g_0^(-2)+beta n log 2. Its exact inclusion in the new domain is

    c_n<=2sqrt(alpha).

For beta>0 it eventually leaves the proved strong-coupling domain. A nontrivial four-dimensional continuum field and a finite positive continuum mass have not been constructed by L22. The original units and this parameter boundary are explicitly retained.

The two requested calculations are complete: the actual cubic source C14–23, and the complete linearized residual/inverse L5–16 with physical return L20–28. The fourth energy coefficient and its all-order remainder are additional consequences. This is written analysis supported by finite exact regressions, not an independent external review or Lean certificate.

A directly specified next computation is the full source v_4=2B(v_1,v_3)+b_22 on its original connected four-face supports, together with a signed, channel-resolved estimate of J_2 on those same supports. The b_22 formula L6 and the cubic table are now evaluated inputs; there is no reason to repeat their generic norm bounds as new work. Any different continuation must retain its exact link to the physical primitive norm L28 and the running parameter boundary above.


---

# Chapter 17 — 20260917-quartic-cube / PHYSICAL_RETURN.md

Original text path: `workbench/yang-mills/continuations/20260917-quartic-cube/PHYSICAL_RETURN.md`.

# Full corrections at the cubic and fourth sources in the original physical energy

17 September 2026. All operators, parameters, coefficient spaces and source maps are those of `QUARTIC_SOURCE.md` (Q1-Q26). R24-R34 give the strongest result, using the complete fourth source; R1-R23 preserve the cubic-reference calculation and its explicit maps. This argument constructs the full correction rather than truncating the Hamiltonian. The final estimate is for the original finite-regulator physical spectrum, uniformly in L. The smooth four-dimensional continuum mass is not determined by this contribution.

## R1. The actual cubic reference and its whole residual

Write x=xi without changing its physical value, and set

    q3=x v1+x^2 v2+x^3 v3,
    R3=x v1+B(q3,q3)-q3
      =x^4 v4+2x^5 B(v2,v3)+x^6 B(v3,v3),
    J3 h=2B(q3,h), L3=I-J3.                              (R1)

Every term is an original function. Q11 evaluates all of v4. The fifth and sixth terms remain as the displayed complete bilinear functions, with the independent bounds below. The Frechet factor two follows by expansion of B(q3+h,q3+h) using symmetry of the original Gamma.

Put

    A4=2296826751679/30073680,
    m3=336572872/208845, t3=225985217/1253070,
    m2=5834/39, t2=137/6,
    l3=m3+4t3=292337810/125307,
    b23=3(m2*t3+m3*t2)=222621900791/1163565,
    b33=6m3*t3=76060493515233224/43616234025.              (R2)

The exact Q17 source estimate and the three evaluated lower coefficients give

    ||J3|| <= ell(x)=(128/3)x+(3132/13)x^2+l3*x^3,
    ||R3||loc <= delta(x)=A4*x^4+2b23*x^5+b33*x^6.        (R3)

For the cubic part of J3, Q17 and Q16 give
`2*3[m3/6+(2/3)t3]=m3+4t3`; this retains the two different spin budgets. The fifth residual coefficient is twice b23, not b23. All sixth-order residual terms are included in b33.

Define the explicitly specified rational polynomial

    D4(x)=(1-ell(x))^2-(8/3)delta(x).                    (R4)

Let alpha4 be its unique root between 178/10000 and 179/10000. Exact rational evaluation proves opposite signs at these endpoints and ell(179/10000)<1. On [0,179/10000], ell and delta are increasing, and

    D4'(x)=-2(1-ell(x))*ell'(x)-(8/3)delta'(x)<0.

Thus alpha4 is also the first positive root; D4>=0 and ell<1 on [0,alpha4]. The full constants in R2-R4 define the polynomial without rounded coefficients.

## R2. Both infinite constructions and their actual residuals

The actual source operator L3 has the norm-convergent inverse

    L3^(-1)=sum_(j>=0)J3^j,
    ||L3^(-1)||<=1/(1-ell(x)).                           (R5)

Let z=L3^(-1)R3 and C=L3^(-1)B. Define w_1=z and
`w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i))`. From R3 and Q17,

    ||w_n||loc <= Cat_(n-1) c_*^(n-1) z_*^n,
    z_*=delta/(1-ell), c_*=(2/3)/(1-ell),
    theta=4 c_* z_*<=1.

The complete series w=sum_n w_n is absolutely convergent, including x=alpha4, and satisfies L3w=R3+B(w,w). Its bound is

    ||w||loc<=w_*(x)=(3/4)(1-ell(x)-sqrt(D4(x))).         (R6)

At theta=1 the convergence comes from the Catalan series itself. With b_N=binom(2N,N)/4^N, the exact identity Cat_N/4^N=2(b_N-b_(N+1)) gives the full nonlinear tail

    ||sum_(n>N)w_n||loc
       <=(3/4)(1-ell)theta^(N+1)b_N
       <=(3/4)(1-ell)theta^(N+1)/sqrt(N+1).              (R7)

The final inequality follows from b_N^2<=1/(N+1), proved by induction from the displayed ratio b_(N+1)/b_N=(2N+1)/(2N+2). Independently, the finite linear sum has the exact original residual

    L3^(-1)R3-sum_(j=0)^N J3^j R3
       =J3^(N+1)L3^(-1)R3.                             (R8)

Its norm is at most ell^(N+1)delta/(1-ell). Each J3 operation adjoins at most three original faces to the union label, and R3 has at most six; the finite linear sums therefore retain supports of at most6+3N faces. R7 retains every subsequent nonlinear union.

## R3. Identification with the original positive vacuum and its scalar

At each finite L the labelled normed coefficient source is complete, and its global c-weighted sum is at most |E_L| times its local norm. The original spin-generator bounds control every first and second derivative by that global sum. Thus the convergent v=q3+w is C^2 on the original compact product group. The source equation can be summed with its full derivatives. Retain

    C(v)=int_H Gamma(v,v),
    c_L=-(1/2)log int_H exp(2v),
    psi_L=exp(v+c_L),
    E0,L=2kappa x M-kappa C(v).                         (R9)

The original product rule gives H psi_L=E0,L psi_L. Elliptic regularity makes psi_L smooth and strictly positive. Multiplication and division by psi_L preserve the original finite-volume H^1 domain. Integration by parts gives, for every smooth f,

    q_(H-E0,L)(psi_L f)=kappa int psi_L^2 sum_i|X_i f|^2. (R10)

This proves E0,L is the actual ground energy. A second ground state divided by psi_L has every original derivative zero and is constant. The source construction is gauge invariant, so this is the actual physical vacuum. The argument does not assume an excitation gap.

The approximate exponential has a separate exact identity, which retains its multiplication defect:

    exp(-q3) H exp(q3)
      =kappa[K-2Gamma(q3,.)]
       +kappa[2Mx-C(q3)]I-kappa M_(K R3).                (R11)

Here M_(K R3) means multiplication by the full original polynomial K R3. Q1-Q2 and a direct differentiation prove R11. Its scalar C(q3) and the multiplication operator remain; they are not replaced by the actual E0,L before R9 is proved.

The same absolute coefficient arguments give analyticity for complex |x|<alpha4. At every original power the unique coefficient recurrence is Q2. Consequently this solution agrees, by its actual coefficients and the ground-state identification, with the preceding constructions on their common domain. No competing vacuum or comparison measure is substituted.

## R4. Return to the complete physical spectral problem

The original transported operator is

    A=psi_L^(-1)(H-E0,L)psi_L=kappa[K-2Gamma(v,.)].      (R12)

The complete actual point-spin budget is

    t(v)<= (16/3)x+(137/6)x^2+t3*x^3+w_*/6.

For a physical Fourier function h, the three original generator indices and sum_e j_e<=2c(j)/3 give

    ||2Gamma(v,h)||_X<=chi(x)||Kh||_X,
    chi(x)=4[(16/3)x+(137/6)x^2+t3*x^3+w_*/6].           (R13)

The norm X is the sum of the original trace norms of Fourier coefficients. The scalar output is included in this bound. Substitution of R6 gives the exact identity

    3(1-chi(x))=d4(x)
      =(3/2)(1+sqrt(D4(x)))+(1136/13)x^2+p3*x^3,
    p3=(3/2)m3-6t3=278874091/208845>0.                 (R14)

In particular chi<1 throughout the entire closed domain. At alpha4, d4 exceeds3/2.

Let lambda>0 be an actual physical excitation eigenvalue, and h the zero-Haar-mean part of its eigenfunction after division by the actual vacuum. A constant transported eigenfunction has eigenvalue zero, so h is nonzero. The original eigen-equation gives

    (K-lambda/kappa)h=Q_H 2Gamma(v,h).                  (R15)

Smoothness on this fixed finite product implies absolute summability of its c-weighted Fourier trace coefficients: applying arbitrarily high powers of the elliptic K gives rapid decay, while the number and dimensions of product-spin representations grow polynomially in c at this fixed L. Cauchy-Schwarz then gives the required trace-norm summability. Hence R13 applies to the actual eigenfunction. Q16 gives c>=3 on every nonconstant physical block. For 0<lambda/kappa<3,

    ||(K-lambda/kappa)h||_X
       >=(1-lambda/(3kappa))||Kh||_X.

Combining this with R13 proves lambda>=kappa d4(x). Excitations with lambda/kappa>=3 obey the same bound because d4(x)=3(1-chi(x))<=3. The compact physical spectral resolution returns this to the full original physical form domain:

    Delta_L>=kappa d4(x),
    q_A(f)>=kappa d4(x) Var_(rho_L)(f),
    L>=2, a>0, 0<x<=alpha4.                             (R16)

Thus the result includes states whose original labels depend on L. It is a lower bound on all physical excitations, not a lower bound only on a chosen finite trace family.

## R5. Exact numerical enclosures in original physical units

Rational bisection and integer-square comparisons give

    0.01781868048538520630 < alpha4 < 0.01781868048538520631,
    3.745693472404566975 < 1/(2sqrt(alpha4))
                        < 3.745693472404566976.          (R17)

The exact condition on the original coupling is g^2>=1/(2sqrt(alpha4)). A sufficient rounded condition is g^2>=3.745693472404566976. The parent threshold was about3.825973052393386; the comparison retains that stronger saved value, not an earlier weaker summary.

At g^2=15/4, x=4/225, the bound is

    d4(4/225)>1.5794.

The same rational bound holds for all g^2>=15/4. To verify the required monotonicity, for 0<=x<=4/225 use D4<=1, ell'>=128/3 and R4 to bound

    d4'(x)<=-(3/2)(1-ell(4/225))(128/3)
             +2(1136/13)(4/225)+3p3(4/225)^2<0.

Every number in this final test is rational. Therefore

    Delta_L>1.5794*kappa=3.1588*g^2/a,
    g^2>=15/4.                                        (R18)

At g^2=4, x=1/64,

    d4(1/64)>1.88578,
    ||v-q3||loc<0.019533267617373.                      (R19)

The unchanged physical scale is kappa=8/a there. These bounds include the complete linear and nonlinear tails in R7-R8. The generated verification record contains exact rational brackets, not only these decimal renderings.

## R6. Retained source kernels, complete operator defect, and physical primitive

For the actual finite windows

    V_N=span{R3,J3R3,...,J3^N R3},
    V_N --L3--> V --0--> 0,

the inclusion in degree zero and the identity in degree one give the commuting support transitions. R5 supplies the explicit isomorphism

    V_(N+1)/V_N -> ker[V/L3 V_N -> V/L3 V_(N+1)],
    [h] -> [L3h],   inverse [L3h] -> [h].               (R20)

Changing a representative by L3 V_N changes the inverse by exactly V_N, proving both inverse laws. Subtraction of the actual finite primitive sum leaves J3^(N+1)R3 as the representative. The source label remains attached at a receiving zero. This is the actual Split Zero support-indexed complex and its retained primitive, with the same original coefficient domain throughout.

The map from this source to the physical equation has the exact identities

    K L3 h=Q_H[K-2Gamma(q3,.)]h,
    Q_H A h-kappa K L3h=-2kappa Q_H Gamma(w,h).           (R21)

The right side has X norm at most(2kappa/3)w_*||Kh||_X by the original spin bounds. R11 separately retains the entire multiplication residual and scalar of the reference exponential. Thus no identity between the linearized source and the full physical operator is asserted without its displayed defect.

On centered original physical functions let d_X f=(X_i f)_i, with squared derivative norm kappa int rho_L sum_i |X_i f|^2. The inverse on its actual range is p_X(d_X f)=f. Its uniqueness follows from the derivative-zero functions being constants and the centering condition. The original ground-state map f->psi_L f and its inverse h->h/psi_L preserve the specified pairings. The variational characterization and R16 give

    ||p_X||^2=1/Delta_L<=1/(kappa d4(x)).                 (R22)

An actual gauge-invariant conditional-expectation kernel is a centered subspace. Restriction of R16 to its original closed form consequently gives the same lower bound for its physical restricted operator. This returns the stronger inverse estimate to the previously computed zero-shift response without changing its forcing or Gram matrix.

## R7. Continuum scope and literature correspondence

The standing path is a_n=a0*2^(-n), g_n^2=1/c_n, c_n=g0^(-2)+beta*n*log2. Its inclusion in R16 is exactly c_n<=2sqrt(alpha4). For beta>0 the path eventually leaves this proved domain. This finite-regulator, volume-uniform result does not assign a finite continuum mass or a nontrivial ultraviolet field to that path.

The exponential vacuum and linear excitation equations have established antecedents. In Schuette, Zheng Weihong and Hamer, arXiv:hep-lat/9603026v1, the coefficient x_C=2/g_C^4 and physical operator H_C=g_C^2[K-x_C S]/(2a) have the exact original-coordinate return

    g_C=2^(3/4)g,
    H_original=sqrt(2)H_C(a,g_C)+2kappa xi M I.           (R23)

Substitution verifies both coefficients and the additive energy. Their Hermitian-generator commutator derivative corresponds to iX here, giving the original signs K v-Gamma(v,v)-xi S. The exact physical Haar/energy pairings and complete source residuals in R1-R22 are kept after this comparison. The general method and existence of higher-order calculations are not claimed as new. No global priority or best-known-threshold statement follows from this scoped literature reading.


## R8. Execute the full correction at the calculated fourth source

The fourth table is now used as an actual reference, rather than left as a remainder estimate. Put

    q4=x v1+x^2 v2+x^3 v3+x^4 v4,
    J_[4]h=2B(q4,h), L_[4]=I-J_[4].

Expansion of the unchanged source equation Q2 gives the entire residual, with all ordered contributions:

    R_[4]=x v1+B(q4,q4)-q4
      =x^5[2B(v1,v4)+2B(v2,v3)]
       +x^6[2B(v2,v4)+B(v3,v3)]
       +2x^7 B(v3,v4)+x^8 B(v4,v4).                   (R24)

Each displayed B is the original function with its full union support. The fifth source is not claimed to have been separately expanded into its final channel table. R24 is an exact expression for every part of the reference residual, including the sixth, seventh and eighth degrees.

Use the exact m4,t4 from Q26, together with the earlier m_i,t_i. Define

    l4=m4+4t4,
    b14=3(m1*t4+m4*t1), b24=3(m2*t4+m4*t2),
    b34=3(m3*t4+m4*t3), b44=6m4*t4,
    ell_[4](x)=ell(x)+l4*x^4,
    delta_[4](x)=(2b14+2b23)x^5+(2b24+b33)x^6
                       +2b34*x^7+b44*x^8,
    D_[4](x)=(1-ell_[4](x))^2-(8/3)delta_[4](x).        (R25)

All of these constants are rational and positive. The underlying estimates are exactly Q17:

    ||J_[4]||<=ell_[4], ||R_[4]||loc<=delta_[4].

In particular the fourth contribution to the derivative is
`2*3[m4/6+(2/3)t4]=m4+4t4`, and the factor two in each unequal reference pair is retained.

Let alpha_[4] be the first positive root of the polynomial D_[4]. On [0,182/10000], ell_[4]<1, ell_[4] and delta_[4] are increasing, and

    D_[4]'=-2(1-ell_[4])ell_[4]'-(8/3)delta_[4]'<0.

Exact signs at 181/10000 and 182/10000 therefore prove existence and uniqueness of this root in that interval, and its first-positive-root status. Integer-square comparisons and rational bisection give

    0.018104972231644127075 < alpha_[4]
                           < 0.018104972231644127076,
    3.715960362535435236 < 1/(2sqrt(alpha_[4]))
                        < 3.715960362535435237.         (R26)

For every 0<x<=alpha_[4], L_[4] has its actual norm-convergent Neumann inverse and the complete correction w^[4]=v-q4 is constructed by the same explicit binary-tree series as R5-R7, with the R25 data. Thus

    ||L_[4]^(-1)||<=1/(1-ell_[4]),
    ||w^[4]||loc <= w_[4]*(x)
       =(3/4)(1-ell_[4](x)-sqrt(D_[4](x))).             (R27)

For clarity, set z=L_[4]^(-1)R_[4], C=L_[4]^(-1)B, w_1=z and
`w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i))`. Its scalar majorants are
`z_*=delta_[4]/(1-ell_[4])` and `c_*=(2/3)/(1-ell_[4])`.
The parameter theta_[4]=4c_*z_* lies in [0,1]. The exact complete tail is bounded by

    ||sum_(n>N)w_n||loc
       <=(3/4)(1-ell_[4]) theta_[4]^(N+1)
                          binom(2N,N)/4^N
       <=(3/4)(1-ell_[4]) theta_[4]^(N+1)/sqrt(N+1).    (R28)

At alpha_[4] this converges to zero by the central-binomial bound. The inverse truncation separately has residual
`J_[4]^(N+1)L_[4]^(-1)R_[4]` and norm at most
`ell_[4]^(N+1)delta_[4]/(1-ell_[4])`. These equations control both infinities without replacing their actual coefficient sources. A finite inverse term has original support in at most8+4N faces, and every nonlinear union remains recorded.

The resulting v=q4+w^[4] is C^2 in the original finite-volume coordinates by the same global c-summability proof in R3. Its full equation proves R9-R10 with this v, hence identifies the same actual positive physical vacuum and its scalar. The exact approximate exponential formula is R11 with q3,R3 replaced by q4,R_[4]; the full multiplication defect K R_[4] and the scalar C(q4) remain.

## R9. Strongest full physical lower bound and retained inverse

The actual point-spin bound is now

    t(v)<=t1*x+t2*x^2+t3*x^3+t4*x^4+w_[4]*/6.

The complete physical excitation argument R12-R16 applies to this actual v. Its returned margin is exactly

    d_[4](x)=(3/2)(1+sqrt(D_[4](x)))
             +(1136/13)x^2+p3*x^3+p4*x^4,
    p4=(3/2)m4-6t4
       =32092619324045301088/823531037954625>0.          (R29)

Indeed expanding `3[1-4(t1*x+t2*x^2+t3*x^3+t4*x^4+w_[4]*/6)]` using R27 proves R29 term by term. In particular d_[4]>3/2 on the full closed positive-coupling interval. The exact original theorem is

    Delta_L>=kappa d_[4](xi),
    q_A(f)>=kappa d_[4](xi) Var_(rho_L)(f),
    L>=2, a>0, 0<xi<=alpha_[4].                        (R30)

The proof includes every physical form-domain vector through the complete compact spectral resolution as in R15-R16. No preassigned missing excitation gap is used in the source construction. A sufficient rounded original coupling condition is
`g^2>=3.715960362535435237`; the exact condition is `g^2>=1/(2sqrt(alpha_[4]))`.

At the concrete original parameters,

    g^2=15/4, xi=4/225: d_[4](xi)>1.6584,
    g^2=4, xi=1/64:     d_[4](xi)>1.89811.              (R31)

The first bound holds throughout g^2>=15/4. For x0=4/225 the exact rational inequality

    -(3/2)(1-ell_[4](x0))(128/3)
       +2(1136/13)x0+3p3*x0^2+4p4*x0^3<0

bounds d_[4]' from above for 0<x<=x0, because sqrt(D_[4])<=1 and ell_[4]' >=128/3. Thus d_[4] decreases on that interval. It follows in original physical units that

    Delta_L>1.6584*kappa=3.3168*g^2/a,
    g^2>=15/4.                                        (R32)

At g^2=4 the complete reference error obeys
`||v-q4||loc<0.011169768000312`. The generated receipt retains full rational brackets for the correction, discriminant, and original energy factors.

For the actual source windows `V_N=span{R_[4],J_[4]R_[4],...,J_[4]^N R_[4]}`, the two degree maps and inverse in R20 are now the explicit maps

    [h] -> [L_[4]h], inverse [L_[4]h] -> [h].

They are well-defined on `V_(N+1)/V_N` and the corresponding transported cohomology kernel because L_[4] is injective and its inverse is R27. Both inverse compositions remain literal. The receiving scalar, support and full physical defect are

    K L_[4]h=Q_H[K-2Gamma(q4,.)]h,
    Q_H A h-kappa K L_[4]h=-2kappa Q_H Gamma(w^[4],h),
    ||p_X||^2=1/Delta_L<=1/(kappa d_[4](xi)).             (R33)

The defect norm is at most `(2kappa/3)w_[4]*||Kh||_X`. The physical derivative norm and ground-state multiplication/division maps are exactly those in R22. Thus the stronger inverse also restricts to the original physical conditional kernel, without changing a forcing vector or its raw Gram matrix.

The standing simultaneous path has the exact domain

    a_n=a0*2^(-n), g_n^2=1/c_n,
    c_n=g0^(-2)+beta*n*log2 <= 2sqrt(alpha_[4]).          (R34)

For beta>0 it eventually leaves the certified interval. The root in R26 is the endpoint of this particular proved majorant, not an assigned singularity of the actual theory. This contribution gives no ultraviolet continuum field or finite positive continuum mass. The complete fourth table and its q4 correction are now finished inputs; the next unevaluated coefficient is the original channel-resolved v5.


---

# Chapter 18 — 20260917-quartic-cube / QUARTIC_SOURCE.md

Original text path: `workbench/yang-mills/continuations/20260917-quartic-cube/QUARTIC_SOURCE.md`.

# The complete connected fourth source in the original cubic SU(2) Hamiltonian

17 September 2026. Parent: `91434b6962062bd80439d4cb2cae9d2479264dde`, the unmerged PR8 contribution. This file, `PHYSICAL_RETURN.md`, and `SIXTH_ENERGY.md` form one continuation. The exact original-coordinate tables are generated by `verify.py`; every entry and every original anchored multiset is retained. This is a written proof with finite exact computation, not a Lean certificate or an independent external analytical review. No claim of historical priority is made.

## Q1. Original operator and labelled coefficient source

Vertices are `{-L,...,L}^3`, L>=2. Edges are every contained positively oriented nearest-neighbor link e=(n,i). Faces p=(n;i,j), i<j, carry the original word

    W_p=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)).

With T_alpha=-i sigma_alpha/2 and X_e,alpha the original left derivative, retain

    K=-sum_(e,alpha) X_e,alpha^2,
    H=kappa K+kappa xi(2M-S),
    S=sum_p W_p, M=|P_L|, kappa=2g^2/a, xi=1/(4g^4).       (Q1)

The scalar 2kappa xi M remains. The Hilbert measure is the original product Haar probability. All vertex gauge transformations, including boundary vertices, are imposed in the physical space. The physical H^2 and H^1 domains and positive ground-state identity are as in the pinned original `finite_box_weak_coupling_physical_gap.md`, blob `dfee77c0ca0d6ed897c4172fcbfe23cd9d10d313`.

Let P_H be original Haar integration and Q_H=I-P_H. On nonconstant physical Fourier blocks define

    Gamma(f,h)=sum_(e,alpha)(X_e,alpha f)(X_e,alpha h),
    B(f,h)=K^(-1) Q_H Gamma(f,h),
    v_1=S/3, v_n=sum_(i=1)^(n-1)B(v_i,v_(n-i)).           (Q2)

Every occurrence keeps its multiset of original face labels. The support is their original union; cancellation of a coefficient does not delete that support record. At the function level, assembly is the map

    A: direct_sum_multisets V_multiset -> functions,
       (f_multiset) -> sum f_multiset.                   (Q3)

Its kernel is the set of coefficient families with zero assembled Fourier matrix at every original spin label. Neither a zero matrix nor a trace identity is assigned an inverse outside the stated quotient. Scalars removed by Q_H are returned to the ground energy in R9 of the companion file.

## Q2. A finite trace presentation with an explicit evaluation map

An oriented edge word is a tuple (s_1 e_1,...,s_r e_r), s_i=+1 or -1. Its evaluation is tr(product_i U_ei^si), in that order. A monomial is a product of these original trace evaluations. The coefficient algebra is rational. The retained map `ev` sends a formal rational sum of such monomials to its actual smooth cylinder function.

The program chooses representatives only using the following proved relations in ker(ev):

* adjacent U_e U_e^(-1)=I, with tr(I)=2 kept as the scalar 2;
* cyclic trace rotation;
* reversal of the entire word with every sign reversed, since tr(V^(-1))=tr(V) for V in SU(2);
* tr(V^r)=P_r(tr V), where P_0=2, P_1=x, P_r=x P_(r-1)-P_(r-2).

The last identity follows by multiplying V^2-tr(V)V+I=0 by V^(r-2) and taking the trace. Thus `ev` factors through the displayed trace relations. It is this factorization, with the original multiset still attached, that relates the coefficient representatives. No faithfulness of an unrestricted trace-word algebra is presumed, and no physical parameter, vector norm, or Haar factor is changed.

Here are the exact derivative formulas used by `trace_algebra.py`. An occurrence of U_e has sign +1 and a cut immediately before that occurrence. An occurrence of U_e^(-1) has sign -1 and a cut immediately after it. If w_i is the cyclic word starting at that cut, then

    X_e,alpha tr(w)=sum_occ s_occ tr(T_alpha w_occ).       (Q4)

For two trace factors A,B, the original Pauli matrices give

    sum_alpha tr(T_alpha A)tr(T_alpha B)
       =-(1/2)tr(AB)+(1/4)tr(A)tr(B),
    sum_alpha tr(T_alpha A T_alpha B)
       =-(1/2)tr(A)tr(B)+(1/4)tr(AB).                    (Q5)

These follow by substituting
`sum_alpha (T_alpha)_ij(T_alpha)_kl=-(1/2)delta_il delta_jk+(1/4)delta_ij delta_kl`.

For one word w and edge e, each occurrence contributes (3/4)tr(w) to E_e tr(w). Two different occurrences, with cut segments A,B and signs s,t, contribute

    st tr(A)tr(B) - (st/2)tr(w).                         (Q6)

For a product of trace factors, retain the entire product rule

    K product f_i = sum_i(Kf_i) product_(j!=i)f_j
                 -2 sum_(i<j) Gamma(f_i,f_j) product_(k!=i,j)f_k.   (Q7)

Equations Q4-Q7 prove that the rational word operators intertwine evaluation with the original K and Gamma, on every original link assignment. They also retain the nonzero cross terms. The separately implemented `differential_audit.py` differentiates quaternion matrix products by explicit generator insertions and never calls these Fierz contractions.

## Q3. Original finite Casimir inverse, with its scalar fibre

For a multiset C of n faces, an edge occurring r_e times has the full spin list

    j_e=r_e/2,r_e/2-1,...,r_e mod 2 /2.                 (Q8)

At each original vertex, a contributing invariant tensor has integral summed spin and max j_e <= sum of the other j_e. The necessity follows from the maximum weight of their tensor product. The sufficiency follows by successively adjoining a spin: the attainable spins fill the interval from the excess of the largest spin over the others (or the parity minimum) to their total, in unit steps. This inductively gives spin zero exactly for the two stated tests. For the computation only their necessary direction is needed; retaining extra channels would still give a valid inverse interpolation.

Enumerate all assignments in Q8 satisfying those vertex tests and retain their original Casimirs c=sum_e j_e(j_e+1). Call the resulting finite set C_C. Every actual representation of the coefficient source lies in that list. Define

    q_C(t)=product_(c in C_C, c>0)(1-t/c),
    f_C(t)=(1-q_C(t))/t-q_C(t) sum_(c in C_C,c>0)1/c.    (Q9)

The quotient by t in Q9 is a polynomial because its numerator has zero constant term. Direct substitution gives f_C(0)=0 and f_C(c)=1/c for every positive listed c. The original product-group spectral decomposition therefore proves

    K f_C(K) f=Q_H f                                   (Q10)

on this whole finite coefficient space, with every repeated spin multiplicity retained. This is a polynomial in the original derivatives, not an inverse on an independently chosen matrix. The constant removed by Q10 is recorded explicitly by original Haar integration.

For a face multiset C, let C=A+B range over ordered nonempty proper submultisets, with their original multiplicities. The complete coefficient is

    v_C=f_C(K) sum_(A+B=C) Gamma(v_A,v_B),
    v_{ {p} }=W_p/3.                                  (Q11)

For repeated labels each distinct submultiset is counted once. For distinct labels both ordered complementary choices occur. This agrees exactly with Q2 on expansion of the original sums. It proves each computed entry without introducing an eigenfunction cutoff for H: n bounds only the degree of the one Taylor coefficient being calculated.

## Q4. Exhaustive fourth coefficient and inverse coordinate transports

Start at the four original faces incident on the anchor edge (0,0,0;1). Grow a multiset by adjoining a face already present or a face sharing an original edge with a present face. Retain all results as multisets. The cardinalities at orders one through four are

    4, 46, 612, 8621.                                  (Q12)

This exhausts connected anchored multisets: choose a face containing the anchor, take a spanning tree of the adjacency graph of the distinct faces, grow along that tree, and insert each remaining repeated occurrence. This gives a growth order of every such multiset. A disconnected term is zero in Q11 because either an input source is already zero or the two differentiated active supports are disjoint.

The fourth multiset counts and representative counts are respectively

| Multiplicity | Original anchored multisets | Cubic representatives |
|---|---:|---:|
| 4 | 4 | 1 |
| 3+1 | 84 | 2 |
| 2+2 | 42 | 2 |
| 2+1+1 | 1572 | 19 |
| 1+1+1+1 | 6919 | 54 |
| Total | 8621 | 78 |

The representative map retains an actual permutation pi of the three axes, signs epsilon_i, and an integer translation d:

    y_i=epsilon_i x_(pi(i))-d_i,
    x_(pi(i))=epsilon_i(y_i+d_i).                       (Q13)

A positive original edge maps to the corresponding signed edge under Q13. The link-variable map uses that same U or U^(-1). A face maps to the original face word or its whole inverse, which have equal fundamental traces. Haar integration and each link Casimir are preserved by this map. Applying Q4-Q7 proves that Q13 transports every coefficient in Q11. The full inverse is retained for every one of the 8621 original multisets in `quartic_transports.json`.

No invariance of the auxiliary trace-coefficient norm under separate link inversion is asserted. The estimates in Q6-Q8 below use bounds valid in every original orientation.

`quartic_coefficients.json` contains all 78 polynomials: 743 nonzero rational trace-monomial terms, their original edge dictionaries, face words, multiplicities and complete allowed Casimir lists. The exact self contribution is

    v_{ {p,p,p,p} } = (17/10368) chi_1(Omega_p)
                        -(7/51840) chi_2(Omega_p).      (Q14)

Here chi_1=W_p^2-1 and chi_2=W_p^4-3W_p^2+1. All other contributions are exposed in the table in the same original words. The producer regenerates the entire table; it does not merely test a few displayed examples. Its differential audit checks the original equation for every representative at two declared rational quaternion assignments. Those finite evaluations accompany, rather than replace, the general intertwining proof Q4-Q11.

## Q5. The auxiliary norm and its original physical gauge inequality

For an original nonempty union label S and spin tuple j, write the coefficient as Tr(A_(S,j) pi_j(U)). Define

    ||f||loc=max_a sum_(S contains a,j!=0)c(j)||A_(S,j)||_1,
    m(f)=max_a sum_(S contains a,j!=0)(sum_e j_e)||A_(S,j)||_1,
    t(f)=max_e sum_(S contains e,j!=0)j_e||A_(S,j)||_1.    (Q15)

All these sums concern the explicitly retained coefficient source. The physical norm stays int rho |f|^2 and physical energy stays kappa int rho sum|Xf|^2.

For any active edge e, the endpoint invariant-tensor inequalities force at least 2j_e total spin on the other edges at its endpoints. Their remote endpoints are distinct on the triangle-free original cubic graph. Applying the same inequality there and counting every further edge at most twice forces at least j_e further total spin. Thus sum_f j_f>=4j_e. Since j(j+1)>=3j/2 on nonzero half-integers,

    c(j)>=6j_e, m(f)<=2||f||loc/3, t(f)<=||f||loc/6.     (Q16)

A nonconstant physical block has c>=3. Products of coefficient matrices have trace-norm bound ||A tensor B||_1=||A||_1||B||_1. Decomposing the actual tensor representation, pinching to its isotypic blocks and tracing the multiplicity factors gives the complete actual product coefficients with total trace norm at most that product. The last assertion follows by trace duality against block-diagonal contractions; all multiplicities remain. Each original spin generator has operator norm j_e. Summing its three indices and retaining both possible anchored inputs proves

    ||B(f,h)||loc<=3[m(f)t(h)+m(h)t(f)]
                 <=(2/3)||f||loc||h||loc.              (Q17)

The first source has (||v1||loc,m(v1),t(v1))<=(32,64/3,16/3). The full second source retains (236,5834/39,137/6), from the parent Q2 expansion.

## Q6. Exact cubic channel capacities, including all mixed channels

This stage further evaluates the original cubic table; it changes no coefficient. The per-cluster nuclear masses x are constrained as follows. Every coordinate is nonnegative.

* Pair: x_0+x_1<=64, x_0<=16.
* Repeated cubic: x_(1/2)+x_(3/2)<=216, x_(1/2)<=520/3.
* Path cubic: x_00+x_01+x_10+x_11<=512; x_00<=32; x_00+x_01<=128; x_00+x_10<=128.
* Common-edge cubic: x_(1/2)+x_(3/2)<=512; x_(1/2)<=256.
* Corner cubic: retain 000,011,101,110,111, with total at most512, x_000<=8, and x_000+x_b<=128 for each b in {011,101,110}. Each one-spin channel is exactly zero by the original central-vertex invariant condition.

The pair and path bounds are original single-link Haar contractions. For the repeated cubic, H=(4/3)W_p P_0(W_p W_q)-(1/3)W_q gives ||H||_1<=(4/3)*8*16+8/3=520/3, and the full product chi_1(Omega_p)W_q has norm at most27*8=216. For the common-edge cubic, its entire half-isotypic projection is (2/3)sum W_r P_0(W_pW_q), with norm at most(2/3)*3*8*16=256; this keeps both half-spin copies. The corner single-zero projections have norm at most8*16=128; its triple-zero projection is one quarter of the original six-edge boundary trace, giving8. These bounds follow from literal original Haar contractions and Q17, not from independent assignment of channel masses.

A self cubic has the two fixed bounds 8,64 on its half- and three-half character terms. Maximizing each actual weighted coefficient over these finite polytopes, then summing over the 612 anchored multisets with their actual anchor spins, gives

    ||v3||loc <= 918680/351,
    m(v3) <= 336572872/208845,
    t(v3) <= 225985217/1253070.                         (Q18)

The weights are respectively c(j)|a_j|, (sum j_e)|a_j|, and j_anchor|a_j| for the complete parent cubic coefficients a_j. `channel_bounds.py` records every rational facet and vertex. The exact vertex calculation solves every candidate set of active facets, retains feasible vertices and evaluates those displayed weights. Since each polytope is bounded, a linear functional has a maximum on that list. This is a finite complete certificate of all three sums. The original v3 coefficients, signs and physical state norm remain unchanged.

## Q7. Three independently valid fourth-source estimates

For each original fourth multiset C, the table bounds its full c-weighted norm by the smallest of the following separately proved scalar upper bounds.

**Input-channel bound.** For each ordered split A+B=C in Q11, use the actual eigencomponents (a_mu,F_mu) and (a_nu,F_nu) of the lower sources. The c-weighted inverse cancels the output c. Thus the bound is

    3 sum_(mu,nu)|a_mu a_nu| (sum_e j_mu,e j_nu,e) x_mu x_nu.    (Q19)

Maximize it over the two actual mass polytopes of Q6. A bilinear functional on two compact polytopes reaches a maximum at a pair of vertices: fix one variable, maximize the other linearly, then maximize the retained first coordinate linearly. The producer evaluates every such pair, including equal lower multisets without presuming independence of their actual masses. This is a bound; treating their equal masses as independent merely enlarges the admitted domain. Sum every ordered split.

**Complete trace expression.** Compute Kv_C by Q6-Q7 from the exact table. A nonempty reduced closed word of length l has a tensor trace coefficient of nuclear norm at most2^(l-1). To verify it before identifying repeated edge variables, use independent fundamental factors for its occurrences. At a maximum and minimum of the original coordinate height along the closed walk, the alternating two-index contractions each have Euclidean norm sqrt(2); the other contractions are two-dimensional identities. Separate row/column permutations give norm2^(l-t), with at least one maximum t>=1. Identifying repeated original links is the actual tensor-representation restriction, followed by the trace-norm-contractive isotypic decomposition used in Q17. Thus the bound2^(l-1) is valid in every orientation, also for repeated original edges. Products of words multiply these bounds. Applying this to every rational term of Kv_C gives a whole-source bound on ||v_C||loc; constants cause no difficulty because the nonconstant Fourier sum is at most the full sum. No rotational invariance of this auxiliary norm is used.

**Joint output-channel bound.** For a four-distinct-face multiset with no edge in more than two faces, choose s_e=0,1 on each shared edge. Single-occurrence edges have spin1/2. Keep every assignment admitted by the original vertex conditions. Let c_A(s) be the original Casimir of a submultiset A in that assignment. For singleton A set a_A=1/3; otherwise define

    a_A(s)=sum_(empty!=B proper subset A)
       [(c_B(s)+c_(A\B)(s)-c_A(s))/(2c_A(s))]
        a_B(s)a_(A\B)(s).                              (Q20)

A zero c_A is assigned zero by the original Q_H. At every shared edge a subset has either zero factors, one fundamental factor with scalar Casimir3/4, or the full pair with the total edge Casimir. Hence these lifted subset Casimirs commute with the final edge projectors. Q10 and the product rule prove Q20 on the full product of the original four traces. A forbidden intermediate component can have a formally displayed coefficient, but its projected function is literally zero; it is not assigned a new vector.

For each set Z of shared edges, integrate precisely those original edge variables. The projection P_(0,Z) is product_(e in Z)(I-E_e/2) on this four-face product. Its trace expression, produced by Q6-Q7, supplies the orientation-independent norm bound b_Z just proved. Therefore its final channel masses satisfy

    sum_(s with s_e=0 for all e in Z) x_s <= b_Z.         (Q21)

Maximize sum_s c(s)|a_C(s)|x_s over x_s>=0 and every constraint Q21. The file `quartic_bounds.json` retains the entire constraint list, all coefficient weights, a rational primal vector and a rational dual vector y. The checker verifies y>=0, A^T y>=the weights and equality of primal and dual objectives. Consequently b^T y is a proved upper bound independent of any numerical optimization. `exact_lp.py` obtains it by exact rational elimination with Bland's rule; all certification inequalities are checked again. Forty-four of the 78 representatives admit this particular commuting-channel calculation; the others retain Q19 and the complete trace bound.

## Q8. Complete summed bound and physical scope

Sum the selected per-cluster bounds over every original anchored multiset using Q13 and the orientation-independent inequalities above. The complete rational sum is

    ||v4||loc <= A4 := 2296826751679/30073680
                       < 76374.                        (Q22)

The complete table includes the 78 exact source polynomials and their 8621 transports. The bound itself includes every ordered input split, every admitted joint output channel and every original scalar return. It is stronger than the preceding unevaluated estimate
`(128/3)*(944984/351)+799258/39`.

The three quantities in Q18 and the full fourth coefficient Q22 are the inputs used in `PHYSICAL_RETURN.md`. That argument controls every remaining order. The finite fourth-coefficient calculation is never substituted for the full interacting Hamiltonian.

## Q9. The fourth source's total-spin and actual-anchor-spin bounds

The complete fourth coefficient also gives more information than its c-weighted norm. Retain each original coefficient family and the actual list of allowed spins from Q8. For a representative C with a proved whole c-weighted bound b_C, two immediate estimates are

    m_C <= b_C max_(j in C_C,j!=0) (sum_e j_e)/c(j),
    t_C,e <= b_C max_(j in C_C,j!=0) j_e/c(j).           (Q23)

These follow term by term on the original Fourier coefficients. The maximum is over the complete displayed assignments, not just their distinct Casimir values. It is finite and rational. Every extra admitted spin enlarges these upper bounds.

There is also an estimate directly from the complete v_C trace polynomial. For a monomial m let r_e(m) be its full occurrence count on edge e. Tensor decomposition places every actual output spin at most r_e(m)/2. With b_m=2^(sum_words(length(word)-1)), the orientation-independent bound from Q7 gives

    m_C <= sum_m |a_m| b_m (sum_e r_e(m))/2,
    t_C,e <= sum_m |a_m| b_m r_e(m)/2.                  (Q24)

Every term and its original occurrences remain. These are bounds on the same canonical Fourier coefficient quantities as Q23; taking the smaller of the two scalar upper bounds does not change a coefficient or physical metric.

For the 44 commuting-channel cases in Q20-Q21, retain the identical mass constraints A x<=b and x>=0. Use instead the two complete objective rows

    weight_m(s)=(sum_e j_e(s)) |a_C(s)|,
    weight_e(s)=j_e(s) |a_C(s)|.                        (Q25)

Exact rational dual vectors y>=0 with A^T y>=weight bound these quantities by b^T y. The producer computes and verifies the primal and dual equations as for Q21. The table `quartic_spin_budgets.json` keeps every dual, the selected scalar bounds and the original edge multiplicities.

For the point-spin sum the anchor must be transported as well. In each actual map Q13 its endpoints 0 and e_1 go to -d and (epsilon_i delta_(pi(i),1)-d_i)_i. The code locates that exact original edge in the representative dictionary and adds its own t_C,e bound. The total-spin bound is added once for every original anchored multiset. Thus every original orientation and anchor are retained. In particular this computation uses universal orientation bounds, not a claimed nuclear-norm invariance under a partial transpose.

The resulting complete rational sums are

    m(v4) <= m4 := 17270702970768271/341697152160,
    t(v4) <= t4 := 110695177857394584026401/18025447358750832000. (Q26)

Their approximate sizes are 50543.88912 and 6141.050242. The exact fractions in Q26, rather than those renderings, are used in every subsequent bound. The point-spin result is strictly smaller than A4/6. These are proved bounds for the entire original fourth source, not selected channels or a sampled cluster. `PHYSICAL_RETURN.md` R24-R34 uses them to complete the full correction at q4; R1-R23 retain the earlier cubic-reference calculation as an intermediate result.

## Sources and attribution

The pinned parent provides the complete second and third coordinate calculations, original support reconstruction, and auxiliary coefficient norms; its cubic producer was replayed unchanged. Classical exponential-vacuum and gauge-invariant character/Casimir approaches are described by Schuette, Zheng Weihong and Hamer, arXiv:hep-lat/9603026v1, especially equations17,21-26,30,38; the actual physical parameter/energy dictionary is retained in the companion return file. No new general coupled-cluster method or worldwide-priority claim is asserted. Source scopes and the latest peer README discovery are in SOURCE_INTAKE.json.


---

# Chapter 19 — 20260917-quartic-cube / SIXTH_ENERGY.md

Original text path: `workbench/yang-mills/continuations/20260917-quartic-cube/SIXTH_ENERGY.md`.

# The complete sixth-order ground energy and its original cube contribution

17 September 2026. This calculation uses the actual fourth source evaluated in `QUARTIC_SOURCE.md`, not a finite Hamiltonian approximation. The original scalar energy and all extensive and boundary factors are retained. The coefficient is reproduced by an independent eigenvector recurrence, and the cube contribution is additionally computed by all720 original face orderings.

## E1. Eliminate the fifth source through its exact equation

Retain the original real Haar pairing and source recurrence. Since

    C(v)=int_H Gamma(v,v), E0=2kappa xi M-kappa C(v),

its sixth energy coefficient is

    e6:= [xi^6](E0/kappa)
       =-2 int Gamma(v1,v5)-2 int Gamma(v2,v4)-int Gamma(v3,v3).

The original fifth equation is Kv5=2Q_H Gamma(v1,v4)+2Q_H Gamma(v2,v3). Integrating against the zero-Haar-mean v1, and using int Gamma(f,h)=int f Kh, gives

    e6=-4 int v1 Gamma(v1,v4)-4 int v1 Gamma(v2,v3)
        -2 int Gamma(v2,v4)-int Gamma(v3,v3).             (E1)

This identity includes all fifth-source contributions; none is estimated or discarded. For a specified original multiset of six faces, expand every product in E1 over ordered allocations of that multiset to the displayed sources. A repeated label is allocated by its actual multiplicity, as in Q11. The resulting coefficients depend only on sources through degree four, all evaluated in the adjoining tables.

## E2. Exact original Haar integration

Each word is evaluated in its original SU(2) edge variables. For an edge of even total occurrence r, its full spin-zero projector on that polynomial is

    P_e,0=product_(j=1,...,r/2)[I-E_e/(j(j+1))].         (E2)

Odd occurrence has zero Haar integral, proved by U_e->-U_e. Formula E2 follows by its values1 on Casimir0 and0 on each original positive spin Casimir in that edge's complete occurrence range. Its output is independent of U_e. Thus replacing U_e by I after E2 is the actual original-edge integration, not a substitution for an unevaluated integral. Repeat over every edge. Q4-Q7 make each step a rational original trace calculation. The code retains the resulting constants, including tr(I)=2.

The integration algorithm is independently checked on the fundamental character moments1,2,5 at powers2,4,6. For every sixth-order coefficient below, the same final number is obtained from the separate Rayleigh-Schrodinger recurrence for the original K-xi S. Its overall vacuum amplitude remains a separate scalar factor; the energy coefficients are independent of that factor because the original eigen-equation is homogeneous in it. The numerical polynomial entries in that recurrence are coefficient multipliers, not an assigned physical vacuum norm. The actual amplitude and original unit Haar norm are returned by R9.

Explicitly, with multivariate face couplings, write those coefficient multipliers as u_C, u_empty=1, int u_C=0 for C nonempty, and keep the overall scalar amplitude a as a separate factor a u_C. The energy coefficients satisfy

    e_C=-sum_(p distinct in C) int W_p u_(C-{p}),
    u_C=K^(-1)Q_H[sum_(p distinct in C)W_p u_(C-{p})
                   +sum_(empty!=A proper submultiset C)e_A u_(C-A)].    (E3)

Both equations follow by comparing each original face-coupling monomial in K(a sum u_C x^C)-sum_p x_p W_p(a sum u_C x^C)=e(x)(a sum u_C x^C). The same scalar a appears on both sides; no energy or coupling is rescaled. E3 and E1 give the same six local coefficients. The first calculation uses the logarithmic-vacuum equation, while E3 uses the original linear eigen-equation.

## E3. Exhaustion of the sixth-order connected supports

For each face p, changing U_e to -U_e on one original edge multiplies a source coefficient by the parity of that edge's total original occurrences. Differentiation and all Casimir inverses commute with this center action. A nonzero Haar scalar therefore requires the set of odd-multiplicity faces to have even boundary over F2.

A nonempty finite even-boundary set of elementary cubic faces has at least six faces. Equality is the six-face boundary of one original cube. Here is an explicit finite filling argument. Let c12,c13,c23 be its binary face arrays. Set the binary cube array

    b(n1,n2,n3)=sum_(k>n3)c12(n1,n2,k) mod2.

The edge-boundary equations imply that the sum over k of c12 is constant in n1 and n2; finite support makes that constant zero. Thus b is finite also toward negative n3. Its upper-minus-lower cube boundary has the required c12 array. The remaining face difference is a finite2-cycle with c12=0. The boundary equations on directions1 and2 force its c13,c23 arrays to be constant in direction3; finite support makes them zero. This proves the finite filling and its exact boundary map.

For a nonempty finite cube array b, each nonempty column along an axis has at least two boundary faces normal to that axis. Therefore its boundary has at least twice the sum of the cardinalities of its three coordinate projections, hence at least six. Equality forces each projection to be a singleton, so b is exactly one cube. This proves the stated six-face classification without deleting nonreduced or repeated face labels.

At total order six, all-even multiplicities are6,4+2,2+2+2. Their connected distinct-face supports are respectively a single face, an adjacent pair, or a path/common-edge/corner triple. The only all-odd surviving support is one complete cube. Disconnected supports have zero logarithmic energy coefficient by Q11 and E1; equivalently the original operator on disjoint active link supports is the sum of its commuting tensor-factor operators, so their scalar eigen-energy has no mixed coefficient. The original scalar and all variables remain in that tensor comparison.

## E4. Complete local coefficient table

The coefficient for each indicated original multiset is

| Original multiset | e_C |
|---|---:|
| {p,p,p,p,p,p} | -289/77760 |
| {p,p,p,p,q,q}, p~q | 22285/47309184 |
| {p,p,q,q,r,r}, distinct path | -4909/118272960 |
| Same multiplicities, common-edge triple | 244/4312035 |
| Same multiplicities, cube corner | -212/542997 |
| Six distinct faces bounding one cube | -83/1944 |

The first pair row has the separate original role exchange p<->q; a sum over unordered adjacent pairs counts both roles. The complete finite evidence includes both pair embeddings (coplanar and perpendicular), all nine original cubic-orbit embeddings of distinct triples, and the exact coefficients computed from both E1 and E3.

For clarity, the four terms in E1 for the cube are

    -43/1458, -7/972, -13/2916, -1/648.

For the single face they are

    -17/5832, -1/1458, 17/46656, -7/14580.

Their sums give the corresponding rows. `sixth_energy.json` retains all four terms for every row, together with their original face words and multiplicities.

## E5. A second, path-resolved cube proof

Orient the six cube faces outward. Reversing a whole SU(2) loop preserves its trace, so this is the exact original trace product. Each of the twelve edges now occurs once as U and once as U^(-1). The original integral

    int U_ij conjugate(U_kl)=delta_ik delta_jl/2

supplies twelve factors1/2. Its delta identifications leave one free fundamental color at each of the eight vertices. Hence

    int product_(six cube faces) W_p=2^8/2^12=1/16.     (E4)

In the independent six-distinct-face perturbation coefficient, each proper subset has zero scalar energy coefficient by E3 and the even-boundary argument. In any original ordering, edges occurring twice in an intermediate subset occur in no later face. Integration of those edges projects them onto spin zero. Every edge occurring once carries spin1/2. The original intermediate Casimir is consequently exactly (3/4)|boundary(subset)|. These projections commute with later independent edge variables and with the original total K. Therefore the full cube coefficient is

    -(1/16) sum_(pi in S6) product_(j=1)^5
                        4/[3 |boundary(first j faces of pi)|].       (E5)

No intermediate denominator is replaced by the plaquette denominator3. The complete path count is

| Five successive boundary lengths | Multiplicity |
|---|---:|
| (4,8,8,8,4) | 48 |
| (4,8,8,6,4) | 96 |
| (4,6,8,8,4) | 96 |
| (4,6,8,6,4) | 192 |
| (4,6,6,6,4) | 288 |

There are720 paths. Their rational sum before the1/16 factor is166/243. Equation E5 therefore gives exactly -83/1944, matching the complete coefficient recurrence. This retains all original intermediate boundaries, their denominators, and the terminal Haar contraction. It is the first closed-surface scalar term on six distinct original faces.

## E6. All original finite-box factors and the complete higher-order remainder

Let m=2L. Denote by M,J,P,T,C,B the numbers of original faces, unordered adjacent pairs, three-face paths, common-edge triples, corners and cubes. Their exact values are

    M=3m^2(m+1), J=6m(3m^2-1),
    P=138m^3-126m^2-24m+12,
    T=12m^2(m-1), C=8m^3, B=m^3.                       (E6)

For T sum binom(r_e,3) over the original edge degrees r_e in {2,3,4}. There are3m(m-1)^2 degree-four edges and12m(m-1) degree-three edges, giving the stated T. Each cube has eight three-face corners. To obtain P, count centered face-adjacency wedges and subtract three for each triangular triple. A face degree is s_i+s_j+4r_k-4, where s_i,s_j are3 at one of the two cell-end positions and4 otherwise, and r_k is1 at either normal boundary and2 internally. The direct count is

    sum_p binom(deg p,2)=198m^3-162m^2-24m+12.

Subtract3(T+C), proving P. These formulas preserve every original open boundary. The verifier independently enumerates the actual boxes L=2,3,4.

Summing all rows in E4 gives

    e6= -289M/77760 +22285J/23654592 -4909P/118272960
                       +244T/4312035 -212C/542997 -83B/1944
       =-(211396463m^3+30959193m^2+21845782m+2336684)/4691494080.   (E7)

Thus the original full ground energy is

    E0,L=2kappa M xi-kappa M xi^2/3
       +kappa(5M/216-2J/1053)xi^4+kappa e6 xi^6+R_ge8.  (E8)

The parent analyticity proof on the complex circle |xi|=1/60 bounds the complete scalar C(v) by49|E_L|/1200 there. The new source agrees coefficientwise with that proved construction. The exact center involution makes E0-2kappa Mxi even. Cauchy's estimate and the full geometric tail therefore give

    |R_ge8| <= (49kappa |E_L|/1200)
                 (60|xi|)^8/[1-(60|xi|)^2],
    0<|xi|<1/60.                                       (E9)

The finite coefficient polynomial is accompanied by all higher orders through this bound. Its validity range remains stated; it is not silently extended past the Cauchy circle.

At L=2, e6=-3528610133/1172873520. Along the original spatial-volume limit m->infinity, the coefficient per face is

    lim e6/M=-211396463/14074482240.                     (E10)

This is a limit of the specified Taylor coefficient with its complete original counts. It does not by itself exchange a spatial or ultraviolet limit with a coupling series beyond the proved domain.

## E7. Literature and scope

Schuette-Zheng-Hamer's coupled-cluster/character method and Llewellyn Smith-Watson's shifted linked-cluster formulation are primary antecedents, arXiv:hep-lat/9603026v1 and hep-lat/9212025v1. The former's operator dictionary to Q1 is R23. The latter explicitly describes its truncation and cluster-shift prescriptions; this calculation keeps the original products and uses the full residual bounds R3-R8 and E9. This establishes the method correspondence and the actual all-order error returned here; it is not a claim that the general expansion method or every displayed coefficient is historically new. The scoped search did not establish an independent published match or global priority for the full spatial sixth coefficient E7.


## E8. Return to an actual measured plaquette observable

For real 0<xi<1/60 at fixed original kappa, the constructed simple vacuum is differentiable in xi. Its original mass is one, hence `2 Re<psi,partial_xi psi>=0`. Differentiating `H psi=E0 psi` and testing with the same psi therefore proves the exact Hellmann-Feynman identity

    dE0/dxi = kappa(2M-sum_p <W_p>_rho).

No derivative of the vacuum is omitted: its two terms cancel through the displayed mass derivative and the actual eigen-equation. Define the original mean half-trace as an explicit observation map

    P_L(xi)=(1/(2M))sum_p <W_p>_rho.

Keeping M and the complete coefficients e4,e6 from E8 gives

    P_L(xi)=xi/3-(2e4/M)xi^3-(3e6/M)xi^5+R_P,L,
    |R_P,L| <= (49|E_L|/(40M))
         (60xi)^7 [8-6(60xi)^2]/[1-(60xi)^2]^2.         (E11)

To prove the tail, the same original Cauchy bound used in E9 gives
`|e_(2n)|<=(49|E_L|/1200)60^(2n)` for every n>=4. Differentiate its absolutely convergent series on |xi|<1/60. The exact scalar sum

    sum_(n>=4)2n r^(2n-1)=r^7(8-6r^2)/(1-r^2)^2

follows by differentiating r^8/(1-r^2). Its factor60 and the factor1/(2M) in the actual observation give precisely E11. The ratio |E_L|/M=(m+1)/m is retained and is at most5/4 for L>=2; consequently the entire error is independent of exterior volume after this explicitly defined spatial average.

For each fixed coefficient, all connected source supports have a finite number of original faces. Their interior translates contribute the same coefficient, and the boundary embeddings have vanishing proportion as m->infinity. The bounds just used are uniform after division by M. Dominated power-series summation therefore proves the full mean-observable limit on |xi|<1/60, as well as differentiation of its energy-density series. Its first terms are

    P_infinity(xi)=xi/3-(11/468)xi^3
                       +(211396463/4691494080)xi^5+R_P,infinity,
    |R_P,infinity| <= (49/40)
         (60xi)^7 [8-6(60xi)^2]/[1-(60xi)^2]^2.         (E12)

This is a fixed-lattice-spacing observable return. No continuum scaling limit is used in the coefficientwise or dominated-series argument.

## E9. Explicit correspondence to a current variational benchmark convention

Spriggs, Greplova, Carrasquilla and Nys, arXiv:2509.12323v1, equation1, use the physical convention

    H_N(g_N,a)=g_N^2/a [K/2+(4/g_N^4)sum_p(1-W_p/2)].

Specialize this formula to the same original edge and face sets as Q1. Then the literal coefficient substitution is

    g_N=2g, lambda_N=4/g_N^4=xi,
    H_N(2g,a)=H_original(g,a),
    (a/g_N^2)H_N=H_original/(2kappa).                   (E13)

The generator commutators and E^2=-Delta_(S3)/4 in their equations1-3 agree with the original T_alpha=-i sigma_alpha/2 coordinates through their Hermitian derivative iX. Direct substitution in E13 gives exactly kappa and kappa xi for the two original coefficients. The trace map in their equation4 is W_p->W_p/2, precisely the measured observation in E11. All energy and trace factors are exhibited.

Their reported finite numerical lattices have their own boundary choice. To retain the comparison on a periodic extension of our same vertex set, let J be pullback from the old edge variables, with inverse adjoint the Haar integral over the additional wrapping links. For side2L+1>=5 its actual operator defect is

    H_periodic J-J H_open
       =kappa xi sum_(p in P_periodic\P_open)(2-W_p)J.  (E14)

The electric terms on the added links annihilate the pullback, and all old terms agree; expansion proves E14. Thus E13 is a convention correspondence on matched index sets, and E14 keeps the added interactions needed for the other boundary choice. No numerical data from that paper are presented as an evaluation or independent verification of E7 or E12. The earlier 1985 perturbative source cited in that paper was identified bibliographically but its full text was not retrieved here. The new coefficients and remainder are offered as explicit original-convention benchmark data, with their written derivation and exact replay.


---

# Chapter 20 — research-control / RESEARCH_NOTE.md

Original text path: `workbench/yang-mills/research-control/RESEARCH_NOTE.md`.

# Local density-derivative control and exact energy-minimizing refinement

14 September 2026. A continuation of the full SU(2) Yang–Mills workbench.

This note proves statements about the original finite-regulator Hamiltonian at every positive spacing and coupling. It retains the physical constants, interacting vacuum, observation kernel, and both the energy and state-norm pairings. The continuum mass-gap conclusion is not established here. The executable companion checks declared finite algebraic fixtures; the analytic arguments are the written proofs below, not a new Lean certificate. No general priority claim is made.

## 1. Original objects and the precise mass-gap quantity

Fix the workbench's open graph with vertices {-L,...,L}^3, L>=2, its complete positively oriented edges and faces, a>0 and g>0. Use T_alpha=-i sigma_alpha/2 and its original left derivatives X_(e,alpha). Set

    kappa=2g^2/a, v=1/(2g^2 a), xi=v/kappa=1/(4g^4),
    E_e=-sum_alpha X_(e,alpha)^2,
    H=kappa sum_e E_e+v sum_p(2-tr U_p),
    A=H-E_0 I, rho=psi^2.

Here psi is the actual positive unit vacuum and E_0 its energy. [YM1, sections 1–2] supplies self-adjointness, the invariant H^2 operator domain, invariant H^1 form domain, compact resolvent, smooth positivity and uniqueness of this vacuum. Multiplication

    U:L^2_phys(rho dU)->H_phys, f |-> psi f

has inverse u |-> u/psi and satisfies <Uf,Uh>=int rho conjugate(f)h. The original ground-state identity is

    q(f,h):=<Uf,A Uh>=kappa int rho sum conjugate(Xf)Xh.       (L1)

The equality is interpreted as a form identity on H^1. All subsequent q notation uses this transported form, not a newly selected Hamiltonian.

On centered physical H^1 functions let d f=(X_(e,alpha)f), and give its image the pairing kappa int rho sum conjugate(u)v. A zero derivative makes f constant on the connected product group; centering makes that constant zero. Thus the actual primitive p(d f)=f is well-defined. The spectral variational principle, through U, gives

    ||p||^2=sup_(f centered, f!=0) ||f||_rho^2/q(f,f)=1/Delta. (L2)

Delta is the first physical excitation energy of this finite regulator. This identity fixes the quantity to which later estimates return; no numerical value for Delta is inserted.

## 2. A local all-coupling electric bound

Let r_e be the number of original plaquettes incident on e and W_e their trace sum. In this open graph r_e<=4. Retain the exact decomposition from [YM2, section 2]

    A=kappa E_e+K_e-v W_e,
    K_e=H_ext,e+2v r_e-E_0 >=0.                              (L3)

To verify the sign, use a vector constant on e and an exterior ground vector. Every term of W_e has zero Haar integral in that link, so E_0<=inf H_ext,e+2v r_e. K_e acts on exterior variables and strongly commutes with E_e.

The original vacuum equation is (kappa E_e+K_e)psi=v W_e psi. With gamma_e=<psi,E_e psi>, taking its expectation and using ||W_e||<=2r_e proves

    0<=gamma_e<=2r_e xi.                                    (L4)

Joint spectral calculus also gives ||E_e psi||<=2r_e xi. The original single-link eigenvalues j(j+1), j=0,1/2,1,..., give E_e<=(4/3)E_e^2. Therefore

    gamma_e <= (16/3) r_e^2 xi^2,
    gamma_e <= eta_e:=min(2r_e xi,(16/3)r_e^2 xi^2).          (L5)

Every exterior interaction remains in K_e. Equations L4 and L5 hold at all positive g; their different coupling dependence is retained.

## 3. The full conditional score and an exterior-volume-free bound

Use the already specified dyadic spatial refinement r<n, with b=2^(n-r) fine edges in each ordered coarse edge. All objects in this section use the actual fine vacuum rho_n. The global coordinate map Phi_(r,n) sends a chain to its ordered product W_e=U_(e,1)...U_(e,b), its first b-1 links, and all unused fine links. Its inverse retains those links and sets

    U_(e,b)=(U_(e,1)...U_(e,b-1))^(-1) W_e.

Haar translation gives dU_n=dW dz. Write

    m(W)=int rho_n(Phi^(-1)(W,z)) dz,
    (E f)(W)=m(W)^(-1) int f rho_n dz,  Jg=g o pi_(r,n).

E:L^2_phys(rho_n dU_n)->L^2_phys(m dW), J in the opposite direction, obey EJ=I and E=J*. Their projection is P=JE and their retained kernel is K=ker E. Smoothness and positivity hold on these compact manifolds.

For the original prefixes P_(e,j-1), put

    a_(e,j;alpha,beta)=(Ad P_(e,j-1))_(alpha,beta),
    Y_(e,alpha)=b^(-1) sum_(j,beta) a_(e,j;alpha,beta) X_(e,j,beta).

The full coefficient matrices, including the prefix dependence, remain present. Their adjoint-matrix identities give

    Y_(e,alpha) Jg=J X_(e,alpha)g,
    sum_alpha |Y_(e,alpha)psi_n|^2
       <= b^(-1) sum_(j,beta)|X_(e,j,beta)psi_n|^2.          (L6)

Each coefficient is independent of its own differentiated link. Thus Y has Haar divergence zero. Integration by parts against every smooth coarse test function yields

    X_a E f=E(Y_a f)+E(f S_a),
    S_a=Y_a log rho_n-J X_a log m,  E S_a=0.                (L7)

Here a=(e,alpha); this index is unrelated to physical spacing. Substituting f=1 before subtracting proves the last equation and identifies J X_a log m as the conditional mean of Y_a log rho_n. These are the original fields of [YM3, section 3].

For a finite set F of coarse edges, retain the entire conditional matrix

    Gamma_(a,c)(W)=E(S_a S_c)(W), a,c in F x {1,2,3}.

It is positive semidefinite because z*Gamma z=E(|sum_a z_a S_a|^2). Its exact integrated trace is the conditional variance of Y log rho_n. In particular

    I_F:=int m tr Gamma
       =sum_(a in F x {1,2,3}) [int rho_n |Y_a log rho_n|^2
                               -int m |X_a log m|^2]
       <= (4/b) sum_(e in F) sum_(j=1)^b gamma_(e,j)
       <= (4/b) sum_(e in F) sum_(j=1)^b eta_(e,j)
       <= 32 |F| xi_n.                                    (L8)

Proof: conditional variance gives the first inequality after dropping its explicitly displayed nonnegative coarse term. The identity rho_n |Y log rho_n|^2=4|Y psi_n|^2 and L6 give the next expression. L4–5 apply to the original fine links. Finally r_(e,j)<=4 gives eta_(e,j)<=8xi_n, and there are b links in each of the |F| chains.

This replaces an exterior-volume-dependent bound for this local quantity with one depending on the chosen coarse-edge count and actual coupling. It does not give a pointwise bound on Gamma(W). Along the explicit test path g_n^2=(g_0^(-2)+beta n log 2)^(-1), L8 reads

    I_F <= 8|F|(g_0^(-2)+beta n log 2)^2.                   (L9)

That growth is retained; beta remains a prescribed path parameter, not an identified quantum beta-function coefficient.

## 4. The score is the exact off-diagonal Hamiltonian map

First work in the full scalar L^2 spaces and their coarse vector-field space with counting of generator indices. The following operators restrict to the physical scalar and gauge-covariant vector-field spaces: individual generator components rotate by adjoint matrices, and their contractions are invariant.

Define the bounded finite-regulator map

    T:K->L^2(m; coarse generator coordinates),
    (T h)_a=E(h S_a).

Its adjoint is

    T* u=sum_a S_a J u_a,                                  (L10)

which belongs to K because E S_a=0. Direct substitution proves

    T T* u=Gamma u,
    ||T* u||_rho^2=int m u*Gamma u.                         (L11)

The fields S are real smooth functions, so these formulas also retain the conjugations for complex f,u. In particular all mixed entries of Gamma survive. For h in K the pointwise conditional Cauchy–Schwarz identity gives

    (Th)(Th)* <= E(|h|^2) Gamma.                            (L12)

Contraction by any z proves it as the scalar inequality
|E(h z*S)|^2<=E(|h|^2)E(|z*S|^2).

Let q_n be L1 and retain kappa_n=2g_n^2/a_n. For smooth g and h in K, the original horizontal/vertical splitting and L7 give

    q_n(Jg,h)=-kappa_n b <Xg,T h>_m,
    q_n(Jg,Jv)=kappa_n b <Xg,Xv>_m.                         (L13)

For completeness, X_(e,j,beta)Jg=sum_alpha a_(e,j;alpha,beta)JX_(e,alpha)g. Summing its pairing with Xh gives b<Xg,E Yh>; L7 with Eh=0 makes E Yh=-T h. Unused fine-edge derivatives of Jg vanish, proving both identities without removing any face potential from H.

Thus the exact off-diagonal generator on smooth coarse functions is

    C g:=(I-P) U_n^* A_n U_n Jg=-kappa_n b T* Xg.           (L14)

The weak identity L13 proves L14 by testing against smooth kernel vectors, which are dense in K. The coarse component is the represented operator

    A_c g=-kappa_n b m^(-1) sum_a X_a(m X_a g),
    U_n^* A_n U_n Jg=J A_c g+Cg.                            (L15)

This explicitly connects the retained density derivative with the full operator, rather than assigning it only a support label.

For a coarse g whose derivatives are supported in the coordinates of F, L8 and L11 also prove

    ||Cg||_rho^2
       <= (kappa_n b)^2 ||Xg||_(infinity,l2)^2 I_F
       <= 32 |F| b^2/a_n^2 ||Xg||_(infinity,l2)^2.          (L16)

The last equality of coefficients uses (2g_n^2/a_n)^2 xi_n=1/a_n^2. The factor b^2/a_n^2 is retained. This is an explicit smooth-observable bound, not an operator bound obtained from an integral trace bound.

## 5. Exact minimum-energy section, residual Gram, and mass derivative

Let s>0 and q_(n,s)=q_n+s<.,.>_rho. On K restrict q_n to H^1_phys intersect K; call its represented nonnegative self-adjoint operator D. Here are the domain details. Conditional expectation preserves H^1 at fixed regulator: L7, conditional Cauchy–Schwarz, bounded smooth S and the finite coefficients of Y bound each coarse derivative by the fine H^1 norm. J also preserves H^1. Hence (I-P) sends smooth functions to smooth kernel functions and approximates every L^2 kernel vector. The restricted form is densely defined. It is closed because K is L^2 closed and q_(n,s) is equivalent to the original H^1 norm at this fixed positive smooth density. This proves the assertions about D by the representation of closed nonnegative forms. No regulator-uniform norm-equivalence constant is claimed.

For g in coarse H^1 define

    h_s(g)=kappa_n b (D+s)^(-1) T* Xg,
    S_s g=Jg+h_s(g).                                       (L17)

The inverse exists with norm at most 1/s. T*Xg is in K and L^2, so h_s is in Dom(D). Equation L13 extends by H^1 continuity. It proves, for every kernel k in the form domain,

    q_(n,s)(k,S_s g)=0,  E S_s g=g.                         (L18)

Every lift f with Ef=g has the unique expression f=S_sg+k. Therefore

    q_(n,s)(f,f)=q_eff,s(g,g)+q_(n,s)(k,k),
    q_eff,s(g,v)=s<g,v>_m+kappa_n b<Xg,Xv>_m
       -(kappa_n b)^2 <T*Xg,(D+s)^(-1)T*Xv>_rho.            (L19)

These identities prove that S_s is the unique energy-minimizing section on each original observation fiber. The induced form is closed on coarse H^1: the boundedness of E and J in H^1 gives upper and lower equivalence with the coarse H^1 norm at this fixed regulator, and the minimizer supplies the quotient norm. Every mixed family follows by polarization, not by deleting cross entries.

The original state norm has its separate exact expression

    ||f||_rho^2=||g||_m^2+||h_s(g)+k||_rho^2.               (L20)

Thus the state-norm cross term 2 Re<h_s(g),k> is retained. For a rectangular list of lifts X and their observed columns Z, canonical residual R=X-S_s Z satisfies the full Gram identity

    Gram_(q_n,s)(R)=Gram_(q_n,s)(X)-Gram_(q_eff,s)(Z).        (L21)

In finite coordinates with raw state Gram G and raw energy matrix E_mat, use Q_s=E_mat+sG and an onto observation Lambda. Then

    W_s=(Lambda Q_s^(-1) Lambda*)^(-1),
    S_s=Q_s^(-1) Lambda* W_s,
    (X-S_s Lambda X)*Q_s(X-S_s Lambda X)
       =X*Q_s X-(Lambda X)*W_s(Lambda X).                   (L22)

This is the explicit instantiation of [SZ2, OK1–2] with its source Gram mapped to Q_s and its observation mapped to Lambda. A fixed section J differs by S_s-J in ker Lambda; the difference and its full norms remain in L20–22.

Differentiating the actual resolvent in L19 gives

    d/ds q_eff,s(g,v)
       =<g,v>_m+(kappa_n b)^2<T*Xg,(D+s)^(-2)T*Xv>_rho
       =<S_sg,S_sv>_rho.                                  (L23)

The derivative is exactly the state Gram of the restored vectors. This is an infinite-dimensional conditional-observation version of the earlier finite-frame memory identity.

## 6. Exact composition over arbitrarily many finite refinement levels

Fix r<t<n and keep the same fine vacuum rho_n throughout. Let E_(t,n), E_(r,n) be the preceding observations. Let E_(r,t)^(n) be conditional expectation from the marginal m_(t,n) to m_(r,n). Fubini proves

    E_(r,n)=E_(r,t)^(n) E_(t,n).                            (L24)

Define S_(t,n;s) by minimizing q_(n,s), and on the middle space use exactly the induced form q_eff,(t,n;s). Let S_(r,t;s)^(n) be its minimum section for E_(r,t)^(n). Then

    S_(r,n;s)=S_(t,n;s) S_(r,t;s)^(n).                      (L25)

Proof: for f with coarse value g, put y=E_(t,n)f. L19 decomposes its energy as q_eff,(t,n;s)(y)+the nonnegative fine residual energy. The values y range over exactly the fiber E_(r,t)^(n)y=g, since each has its fine lift S_(t,n;s)y. Minimizing the middle fiber and then lifting gives the unique fine minimizer, proving L25 and its inverse observation law. The same argument iterates to every finite chain of levels and retains the sum of the actual residual energies at all levels.

The middle form and density in this identity are written explicitly. In particular, the identity-on-functions comparison to the separately constructed regulator-t vacuum has pairing

    <f,h>_(m_t,n)=int conjugate(f)h (m_(t,n)/rho_t) rho_t.

No equality of those two measures is presumed. No independent Markov property across scales is presumed. The complete state Gram in the energy-section coordinates is transported by the original synthesis map and retains all off-diagonal entries.

The finite algebra behind L25 is precisely the composed-minimum-lift identity [SZ1, AMT7–9]. For onto Lambda_1,Lambda_2 and positive Q,

    Q_1=(Lambda_1 Q^(-1) Lambda_1*)^(-1),
    Q_2=(Lambda_2 Q_1^(-1) Lambda_2*)^(-1),
    S_(Lambda_2 Lambda_1,Q)=S_(Lambda_1,Q) S_(Lambda_2,Q_1).

Substitution of Q_1^(-1)=Lambda_1 Q^(-1) Lambda_1* proves it directly. The exact checker evaluates this on non-diagonal energy and norm matrices, with nonzero kernel corrections.

## 7. Completed advance and current mathematical direction

L8 is a local all-coupling score estimate independent of exterior volume. L14 identifies that score with the original Hamiltonian's off-diagonal map. L17–23 give its complete energy-minimizing section and restored state metric. L24–25 prove their finite refinement composition with the actual induced intermediate forms. These are a connected calculation on the same original vacuum; none of them sets the memory, kernel, or state-metric cross terms to zero.

The next chosen research quantity is the response matrix/form

    (kappa_n b)^2 <T*Xg,(D+s)^(-1)T*Xv>

relative to the full kinetic energy kappa_n b<Xg,Xv> and the restored metric L23, on increasing physical observable families. The integral bound L8 has no asserted pointwise replacement. Its n-dependent coefficient L9 and the ultraviolet coefficient L16 remain explicit. A uniform positive physical lower edge, a nontrivial four-dimensional continuum field, and treatment of every compact simple gauge group are not supplied by these calculations. SU(2) is the present workbench's literal gauge group.

## 8. Sources actually used and review scope

[YM1] KokunoYumeto/yang-mills-interacting-workbench, main fab69fdc4ac197159b8e6ae8d73a82bde2b20d55, yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md, sections 1–2 and 6. Git blob dfee77c0ca0d6ed897c4172fcbfe23cd9d10d313. Original objects, domains, vacuum and gap characterization.

[YM2] Same main, yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md, sections 1–3. Git blob 66a7453a6452c2555a28270efcf53fa1997c26a8. Original local exterior comparison and electric estimates. The new linear expectation bound L4 is proved above from its full equation.

[YM3] Same repository, unmerged PR4 head dc390930a8d2774e93481206602973caff7aa7da, yang-mills/continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md, sections 3 and 5. Git blob 0d79c733ff6209c991dd2b52474b1e399dd812db. Full source is present in this branch; its delivered bytes were matched to that blob and its earlier checker replayed in this session.

[SZ1] KokunoYumeto/zeta-function-research-reader, main 8fd2157e8b41783224b42781699432d824ec0c15, workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/13_ARITHMETIC_MIXED_TRANSFER.tex, AMT1–10 (source lines 1–275 inspected). Git blob b6cfec2ac9517acc378aa02686ada6e7923ef381. Only its explicit finite metric/minimum-section mechanism is instantiated here; its arithmetic constants and later asymptotics are not assigned to Yang–Mills.

[SZ2] Same repository, unmerged PR32 head 9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6, workbenches/tau-observation-kernel-formal/RESEARCH_NOTE.md, sections 1–7 inspected. Git blob 866ed2f6e8ed9ca544f6ec0af97c5dec3fecedad. Complete rectangular corrected residual and observed-iterate maps. Its reported Lean run was not rerun in this session.

The workflow's peer intake additionally records Collatz, Erdős–Straus and Erdős 817 observations with their exact review scopes. Those independent source identities are not certificates for the analytic results in this note.


---

# Chapter 21 — 20260917-fifth-source / FIFTH_SOURCE.md

Original text path: `workbench/yang-mills/continuations/20260917-fifth-source/FIFTH_SOURCE.md`.

# The complete fifth logarithmic source and its signed plaquette derivatives

17 September 2026. This continuation uses the original finite open SU(2) Hamiltonian. It extends the available fourth-source calculation by one complete order. The incoming independent-session report is retained verbatim in the cumulative archive. Its separately linked calculation ZIP was not present among the mounted files; the report is therefore recorded as a report, rather than assigned the verification status of unavailable programs.

The result here is an exact Taylor-coefficient calculation with complete polynomial-identity certificates. The finite-volume analytic response estimate is proved separately in `PLAQUETTE_RESPONSE.md`. No new uniform-in-volume coupling threshold or continuum mass-gap theorem is asserted. The earlier written gap arguments remain preserved historical sources; this calculation does not independently recertify their full analytical chain.

## F1. Original operator, scalar and independent source parameters

Fix an integer L>=2. The vertices are {-L,...,L}^3. The positively oriented edge e=(n,i) runs from n to n+e_i whenever both endpoints occur. Every contained elementary face p=(n;i,j), i<j, has the original trace

    W_p(U)=tr[U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)].       (F1)

Each inverse is the inverse of that same original edge variable. The original generators, derivatives and kinetic operator are

    T_alpha=-i sigma_alpha/2,
    X_e,alpha f=(d/dt) f(...,exp(t T_alpha)U_e,...) at t=0,
    K=-sum_(e,alpha) X_e,alpha^2.                                (F2)

The scalar product is the original product-Haar probability integral. Physical functions are invariant under every original vertex gauge action U_e -> h_s U_e h_t^(-1), including boundary vertices.

Introduce independent real parameters x_p in the actual potential:

    H(x)=kappa K+kappa sum_p x_p(2-W_p),
    kappa=2g^2/a,
    x_p=xi=1/(4g^4) on the original homogeneous line.             (F3)

The parameters x_p are bookkeeping coordinates for derivatives of this same family. At a fixed finite box its real ground state is smooth, strictly positive, unique and physical. For a neighbourhood of the origin it has a smooth real-analytic choice, proved by the isolated spectral projection and elliptic bootstrapping. Indeed the contour construction in P3 gives an analytic eigenvector in L2. The eigen-equation and bounded smooth multiplication then give analytic dependence in each fixed Sobolev space, using the inverse of K+1; choosing a Sobolev order above half the finite manifold dimension plus two gives analytic dependence in C2. At the origin the vector is the constant 1, so the real logarithm is defined in a neighbourhood of the origin.

Write

    psi_x=exp(v(x)+c(x)),  P_H v(x)=0,
    c(x)=-1/2 log int exp(2v(x)) dU,
    E_0(x)=kappa[2 sum_p x_p+e(x)].                              (F4)

Here P_H is the original Haar integral and Q_H=I-P_H. Product differentiation of exp(v) in the original generators gives

    K v=sum_p x_p W_p+Q_H Gamma(v,v),
    e(x)=-P_H Gamma(v,v),
    Gamma(f,h)=sum_(e,alpha) (X_e,alpha f)(X_e,alpha h).           (F5)

The scalar removed from the source in F5 is exactly the displayed contribution to the original energy. The scalar c(x) retains the original unit-vacuum mass.

Use ordinary multivariate monomial coefficients, with the explicit derivative rule

    v(x)=sum_(nu!=0) v_nu x^nu,
    partial_xp[x^nu]=nu_p x^(nu-e_p).                            (F6)

There is no extra factorial in v_nu. For a single nonzero entry nu=e_p, v_nu=W_p/3. Equating the complete coefficients of F5 gives

    K v_nu=Q_H sum_(0<mu<nu) Gamma(v_mu,v_(nu-mu)),
    P_H v_nu=0.                                                (F7)

The inequalities on multiindices in this formula mean componentwise inclusion, with zero and nu excluded. Thus every ordered split is retained. On the homogeneous line the fifth coefficient is the full expression

    v_[5]=2B(v_[1],v_[4])+2B(v_[2],v_[3]),
    B(f,h)=K^(-1)Q_H Gamma(f,h).                                (F8)

Every proper split in F7 for degree five uses only already specified degrees one through four.

## F2. Exact original differential algebra and finite inverse

The elementary Pauli identities in F2 are

    sum_alpha tr(T_alpha A)tr(T_alpha B)
       =-tr(AB)/2+tr(A)tr(B)/4,
    sum_alpha T_alpha A T_alpha=-tr(A)I/2+A/4,
    -sum_alpha T_alpha^2=3I/4.                                 (F9)

They follow by multiplying the three displayed two-by-two Pauli matrices. Every occurrence of U_e differentiates as T_alpha U_e; every occurrence of U_e^(-1) differentiates as -U_e^(-1)T_alpha. Applying the product rule to every original occurrence and then F9 gives the complete trace-word formulas for Gamma and K implemented in the inherited `trace_algebra.py`. In particular, no interaction at a shared edge is replaced by a diagonal pairing.

Each trace word is retained with its original edge labels. The identities tr(AB)=tr(BA), tr(U^(-1))=tr(U) for U in SU(2), and cancellation of an adjacent U_e U_e^(-1) have their literal matrix proofs. The trace-power recurrence is

    tr(U^n)=tr(U)tr(U^(n-1))-tr(U^(n-2)),                       (F10)

obtained by multiplying U^2-tr(U)U+I=0 by U^(n-2). The raw representative files expose every resulting rational trace term. Their image as an original function is what enters the equations.

For a face multiset nu, let r_e be the number of occurrences of e in its original face words. Its edge representation factors have the finite spin list

    j_e=r_e/2, r_e/2-1, ..., (r_e mod 2)/2.                    (F11)

This list belongs to the particular Taylor coefficient. The full Hamiltonian retains its entire spin spectrum. At each vertex, an invariant tensor requires sum_e 2j_e even and 2 max_e j_e <= sum_e j_e. The lists accepted by these tests contain all actual physical representations, including their multiplicities. Every such tensor has original Casimir sum

    c=sum_e j_e(j_e+1).                                       (F12)

Let C be the set of those values, as explicitly stored in every row. Define

    q_C(t)=product_(c in C,c>0)(1-t/c),
    f_C(t)=(1-q_C(t))/t-q_C(t) sum_(c in C,c>0) 1/c.             (F13)

The numerator of the first term has zero constant coefficient. Direct substitution proves f_C(0)=0 and f_C(c)=1/c at each positive c. On this coefficient space the actual spectral action consequently gives

    K f_C(K)=Q_H.                                             (F14)

The possible zero-Casimir functions are constants, as follows either from the product representation or from int sum|Xf|^2=0. This identifies Q_H in F14 and proves uniqueness of the zero-Haar-mean solution of F7. All rational divisions in the producer are by the displayed positive Casimir values.

## F3. Complete enumeration and exact coordinate transports

Anchor the original edge at (0,0,0;0). Start with the four faces incident on it. At each subsequent order append either a face already present or a face sharing an original edge with one of the present faces. Retain the sorted multiset, with multiplicity. Induction proves completeness: a connected multiset with at least two distinct faces has a non-root leaf in a spanning tree of its face-adjacency graph; remove one occurrence there, or remove a repeated occurrence first. The remaining multiset still admits the construction. A one-face multiset is generated by repetition.

The consecutive anchored counts are 46, 612, 8,621 and 124,864 at degrees two, three, four and five. The degree-five pattern counts are

| Multiplicities | Anchored multisets | Coordinate representatives |
|---|---:|---:|
| 5 | 4 | 1 |
| 4+1 | 84 | 2 |
| 3+2 | 84 | 2 |
| 3+1+1 | 1,572 | 19 |
| 2+2+1 | 1,572 | 19 |
| 2+1+1+1 | 27,676 | 171 |
| 1+1+1+1+1 | 93,872 | 448 |
| Total | 124,864 | 662 |

Each of the 48 signed coordinate permutations is an explicit map

    y_i=s_i x_(pi(i))-d_i,
    x_(pi(i))=s_i(y_i+d_i),  s_i in {-1,1}.                     (F15)

The translation d and the chosen permutation/signs are stored for every anchored original multiset in `generated/geometry_fifth.json`. A positive original edge maps to its corresponding positive edge variable or to that variable's inverse when its orientation reverses. The image of a face word is the target face word up to cyclic starting point and reversal; its SU(2) trace is preserved by F9-F10's elementary matrix identities. Haar measure is preserved by variable permutation and inversion, and K is carried to the target K because the original left/right Casimirs agree.

Returning a representative to its original multiset therefore uses F15's inverse and the same oriented link substitution. Every original multiset appears once. There is no division by an orbit size or multiplication by a factorial. The original anchor edge is retained in the transport record even when its representative position moves.

A disconnected source coefficient vanishes by induction in F7: all nonzero lower inputs are connected; factors on disjoint edge-adjacency components have Gamma=0. Thus the table accounts for every nonzero coefficient at degree five in every original finite open box. Near a boundary one uses precisely the multisets whose original faces are contained in that box.

## F4. The tree/quaternion morphism used for full identities

For a connected original edge union choose the tree obtained by adding original edges in their stored order whenever they join two distinct vertex components. Its root is the smallest original vertex. Let t_v be the ordered original tree-path holonomy from the root to v, including inverse traversals. For each original chord e=(s,t), put

    Z_e=t_s U_e t_t^(-1).                                     (F16)

The full coordinate map U -> (original tree links, Z_e) has the inverse

    U_e=t_s^(-1)Z_e t_t on chords; original tree links unchanged. (F17)

F16-F17 are inverse maps by substitution. Fubini and left/right Haar invariance prove preservation of the product Haar measure. The gauge action h_v=t_v sends the tree links to I and the chords to Z_e. Every original physical function is thereby determined by its values on this tree section. Residual simultaneous conjugation of the chords remains; no chord is removed on that account.

Write every chord in the original quaternion coordinates

    Z_c=x_(c,0)I-i sum_(a=1)^3 x_(c,a) sigma_a,
    x_(c,0)^2+x_(c,1)^2+x_(c,2)^2+x_(c,3)^2=1.                (F18)

The target coefficient algebra is

    A_C=Q[x_(c,a)]/(sum_a x_(c,a)^2-1 for every chord c).        (F19)

The original trace-word algebra maps to A_C by replacing tree links with I and chords with F18, applying ordinary quaternion multiplication, and retaining the polynomial remainder with exponent zero or one in each x_(c,0). The defining monic relations have distinct leading variables, so their reductions commute. Every intermediate rational coefficient and every variable is retained in the map record.

This is an identity test on complete functions. To prove faithfulness, a remainder has degree at most one in each x_(c,0). For a fixed chord, evaluate x_(c,0) at both signs of sqrt(1-|y_c|^2), with y_c in its open unit ball. A remainder vanishing on the sphere gives zero for both its coefficient of 1 and its coefficient of x_(c,0). Repeat for each chord. The resulting polynomials vanish on products of open balls, hence have all coefficients zero. Thus F19 is exactly the coordinate relation ideal of the product of these real spheres for these polynomial identities.

The inverse on the image of the physical trace algebra is the explicit substitution of the original Z_e(U) from F16. Therefore zero of the complete target polynomial proves zero of the original physical function. As a map from formal trace expressions, the kernel is exactly the trace expressions whose tree-quaternion image lies in the ideal F19. Both the raw expressions and their target polynomial are stored, so this kernel is exposed rather than treated as missing support.

The degree-five representatives have cycle-rank distribution

    rank 1: 1; rank 2: 4; rank 3: 38;
    rank 4: 170; rank 5: 444; rank 6: 5.                        (F20)

Every rank is the actual |E|-|V|+1. In particular five representatives retain six chords. `generated/quotient/0176.json` is an explicit six-chord case. Its specialization Z_6=I and the original polynomial have a nonzero difference, retained as a negative-control calculation.

## F5. The complete fifth catalogue and its checks

The full answer is in `generated/fifth/0000.json` through `0661.json`: 14,063 rational trace monomials, with original faces, multiplicities, edge coordinates, words, Casimir values and every signed coefficient. The same functions are completely expanded in F19 in `generated/quotient/`, with 300,821 rational monomials.

For every representative the checker recomputes the entire right side of F7 from the lower coefficients, applies the original K to the new coefficient, and proves that their difference is the zero polynomial in F19. It also checks the stored raw RHS and stored raw residual against those recomputed expressions. There are 281 raw residual trace expressions which have nonempty formal representatives; all 281 map to the zero polynomial through F16-F19. The remaining 381 are already zero in the retained trace representation.

The explicit central link action

    U_(n,i) -> (-1)^(sum_(j<i)n_j) U_(n,i)                     (F21)

multiplies every original plaquette trace by -1. The coefficient v_nu of total degree five changes sign under this Haar-preserving action. Its Haar mean is exactly zero. The script verifies this sign on every original trace monomial. This supplies the mean condition accompanying F7, not merely its differentiated equation.

The independent directional audit `direct_matrix_checks.py` also recomputes K and Gamma directly from quaternion matrix jets at a declared rational original-link assignment for each of the 662 representatives. Its derivative engine uses matrix multiplication and the original generators, without calling the Fierz-contracted K/Gamma routines. Those finite-point regressions accompany, rather than replace, the complete polynomial tests.

## F6. A fully explicit single-face coefficient and an independent recurrence

For the multiset containing the same original face five times, the table is

    v_(5e_p)=79 W_p/34020-41 W_p^3/136080+11 W_p^5/680400.       (F22)

The original character substitutions

    chi_(1/2)=W,
    chi_(3/2)=W^3-2W,
    chi_(5/2)=W^5-4W^3+3W                                    (F23)

and their triangular inverse give

    v_(5e_p)=49 chi_(1/2)/27216
             -23 chi_(3/2)/97200+11 chi_(5/2)/680400.           (F24)

`character_check.py` supplies a separate calculation. Write chi_n for spin n/2, so K chi_n=n(n+2)chi_n and W chi_n=chi_(n-1)+chi_(n+1). Solve the original linear eigenvector recurrence with original Haar coefficient one, then take its complete formal logarithm and remove only its explicitly computed Haar scalar. At order N only indices n<=N can occur because each original fundamental insertion changes n by one. This recurrence returns F24 exactly and also the original energy coefficients through degree eight. The subsequent scalar restoring the unit vacuum starts at -xi^2/9; it remains recorded separately.

## F7. Every signed degree-four source response

For each face p define z_p(x)=partial_xp v(x). In the original monomial coordinates,

    Z_(p,rho)=(rho_p+1)v_(rho+e_p).                            (F25)

Differentiating the full equation F5 gives

    K z_p=W_p+2Q_H Gamma(v,z_p).                               (F26)

For every degree-four multiindex rho, the complete coefficient is

    K Z_(p,rho)
      -2Q_H sum_(0<mu<=rho) Gamma(v_mu,Z_(p,rho-mu))=0.         (F27)

All 3,047 distinct pairs (representative, face-direction) supplied by the fifth table are checked as complete zero polynomials. The derivative weights, both ordered product contributions, and every original source label are retained. The files also contain each full trace-polynomial response; the stored multiplication factor records its map to the same fifth coefficient.

For comparison with the incoming report, this session independently checked all 78 available fourth coefficients and their 282 degree-three derivative directions in the same original sphere-quotient method, including their nonzero Haar RHS constants. Our particular stored tree section produces 6,048 monomials at degree four. The other session reports 4,044 in its own unavailable coordinate files. The present comparison is of the original equations and the explicit available coordinate maps; no bytewise equality of those unavailable polynomials is claimed.

## F8. Higher terms and their exact retained defect

Define V_i(x)=sum_(|nu|=i) v_nu x^nu and q_5(x)=sum_(i=1)^5 V_i(x). Its residual is the complete original polynomial

    R_5=sum_p x_p W_p/3+B(q_5,q_5)-q_5
       =sum_(6<=i+j<=10, 1<=i,j<=5) B(V_i(x),V_j(x)).          (F28)

On x_p=xi, each summand in F28 carries its original xi^(i+j). No term in F28 is set to zero merely because the first five source equations have been solved.

The signed derivative has exactly the defect

    K partial_xp q_5-W_p-2Q_H Gamma(q_5,partial_xp q_5)
       =-K partial_xp R_5.                                    (F29)

Its coefficients through degree four vanish by F27; its retained degrees five through nine are the displayed derivative of F28. The observation onto degrees <=4 is the coefficient map modulo the original parameter ideal m^5, with kernel exactly m^5. The original face labels and the coefficients of F28 remain upstream of that receiving supported zero. This is the literal finite-source jet use of the Split Zero retention convention. It supplies no claim that q_5 is the full vacuum.

The map to the actual physical inverse, including the unit-vacuum scalar and the full energy pairing, is calculated in P1-P2 of `PLAQUETTE_RESPONSE.md`.

## F9. Verification scope and attribution

The new finite calculation uses the preserved cubic/quartic exact trace engines, whose inputs and hashes are recorded. Both complete symbolic fifth-source replays were executed, in ordinary Python and under -O, without cached-row acceptance. Each reconstructed polynomial file matched the delivered bytes. The separate direct-matrix audit covers all 662 representatives. Named false controls preserve the incoming v1/v4 term, derivative multiplicity, factor two, original sixth chord, support, and vacuum scalar.

These are exact rational computational certificates backed by the algebraic proofs F9-F19. They are not a new Lean elaboration or an independent audit of every earlier analytical argument. The original connected exponential-vacuum framework is credited to the Hamiltonian coupled-cluster literature, including Schuette, Zheng Weihong and Hamer, hep-lat/9603026v1. The present exhaustive coefficients, source response records and proof scope are stated without a historical-priority claim.


---

# Chapter 22 — 20260917-fifth-source / PLAQUETTE_RESPONSE.md

Original text path: `workbench/yang-mills/continuations/20260917-fifth-source/PLAQUETTE_RESPONSE.md`.

# Full signed plaquette susceptibility and a finite-volume analytic enclosure

17 September 2026. This calculation returns the original source derivatives to the actual vacuum and its zero-energy resolvent. It gives the complete homogeneous response matrix through degree four, including a nonzero entry between opposite cube faces, and an explicit remainder for the actual finite-volume response. Its analytic proof uses only the original free physical spectrum and bounded original plaquette multiplication. Its radius retains its volume dependence.

## P1. Actual Hamiltonian derivatives and original metric

Retain F1-F4 of `FIFTH_SOURCE.md`. Put A=H(x)-E_0(x), rho=psi_x^2, and let the original unitary map U_psi send f to psi_x f. Its inverse is f -> f/psi_x. The equality

    <U_psi f,U_psi h> = int rho conjugate(f)h dU                (P1)

proves both its scalar-product preservation and its stated inverse. The transported excitation operator is

    Atilde=U_psi^* A U_psi=kappa[K-2Gamma(v,.)],
    q_Atilde(f,h)=kappa int rho sum_i conjugate(X_i f)X_i h dU.  (P2)

The potential is the complete original potential in F3. Formula P2 follows from its exact ground-state equation and integration by parts; it retains the original energy coefficient kappa.

Write z_p=partial_xp v. Differentiating the original unit-vacuum mass gives

    partial_xp c=-<z_p>_rho,
    partial_xp psi=psi Z_p,
    Z_p=z_p-<z_p>_rho.                                        (P3)

The derivative of the full Hamiltonian is kappa(2-W_p). Its actual eigen-equation gives

    partial_xp E_0=kappa(2-<W_p>_rho),
    Atilde Z_p=kappa(W_p-<W_p>_rho).                           (P4)

Every operator and derivative in these formulas is on the original compact finite graph. The strictly positive simple vacuum and the isolated branch constructed below justify the differentiations. Define the original centered states

    r_p=(W_p-<W_p>_rho)psi.

Their zero-energy response matrix is

    R_pq(x)=kappa <r_p,A^(-1)r_q>
           =-1/2 partial_xp partial_xq e(x)
           =q_Atilde(Z_p,Z_q)/kappa.                          (P5)

For real source coordinates and trace observables these entries are real. Indeed the ground state and all differentiated states can be chosen real. Differentiating <W_p> and using P3-P4 gives partial_xq<W_p>=2kappa<r_p,A^(-1)r_q>, proving P5 with its full off-diagonal entries. On complex linear combinations the same matrix is Hermitian positive semidefinite by the actual resolvent pairing.

The original integrated connected Euclidean correlation is

    int_0^infinity <r_p,exp(-tA)r_q> dt = R_pq/kappa.            (P6)

The finite positive spectral gap below proves convergence of the integral. The factor 1/kappa remains in the physical return. P3-P5 also give the exact physical minimum-energy primitive of the source: the centered logarithmic derivative is kappa times the inverse applied to the original centered observable. Its raw state and energy norms are unchanged.

## P2. Sixth-order source data, with each original multiplicity

The complete previous sixth-energy calculation is re-evaluated here on its seven geometric input cases using both the logarithmic-source recurrence and the separate linear eigenvector recurrence. Their common trace/Haar dependency is explicitly retained. The inhomogeneous scalar polynomials are

    e_2=-sum_p x_p^2/3,
    e_4=(5/216)sum_p x_p^4-(2/1053)sum_{p,q adjacent} x_p^2x_q^2,
                                                                    (P7)

where the second sum is over unordered original adjacent pairs. At degree six,

    e_6=a sum_p x_p^6
        +b sum_{p,q adjacent}(x_p^4x_q^2+x_p^2x_q^4)
        +sum_{p,q,r connected} c_type x_p^2x_q^2x_r^2
        +d sum_cubes C product_(p in boundary C) x_p,           (P8)

with every triple unordered and consisting of distinct original faces, and

    a=-289/77760,
    b=22285/47309184,
    c_path=-4909/118272960,
    c_common=244/4312035,
    c_corner=-212/542997,
    d=-83/1944.                                               (P9)

The two pair monomials in P8 are exchanged by the literal bijection (p,q,4,2) -> (q,p,4,2). On the homogeneous line their joint contribution is 2b. This is the exact map from the incoming report's unordered-pair total 22285/23654592 to the ordered multiplicity coefficient used in the Hessian.

For completeness of the degree-six support possibilities, the original independent link-center action forces the parity of the face multiplicities to be a cubical two-cycle. A finite such cycle bounds a finite mod-two three-chain: one explicit filling assigns to a cube at (x,y,z) the sum modulo two of the horizontal-face coefficients above it in that column. The two-cycle equations make its other boundary faces exactly the specified vertical faces; the coefficients vanish outside a finite set. A nonempty set of at least two cubes has projections onto at least two coordinate planes of size at least two and onto the third of size at least one. Each occupied column contributes at least two exposed faces. Its boundary therefore has at least ten faces. Thus a nonzero two-cycle with at most six faces is exactly one cube boundary. The other degree-six possibilities have all face multiplicities even and at most three distinct faces. Connectivity leaves precisely the cases P8-P9. No original cube term is omitted.

The cube coefficient has a separate complete calculation. Every one of its twelve edges occurs once in each orientation in the outward face product. Haar contraction yields one factor 1/2 per edge and one free two-dimensional vertex index at each of its eight vertices, giving 2^8/2^12=1/16. For a face insertion order pi, the proper intermediate subset A_j has its original boundary energy 3|boundary A_j|/4. Consequently

    d=-(1/16)sum_(pi in S_6) product_(j=1)^5 [4/(3|boundary A_j|)]
     =-(1/16)(166/243)=-83/1944.                               (P10)

All 720 orders are recomputed in the checker.

## P3. An independent finite-volume analytic disk

The original free physical spectrum has simple eigenvalue zero with vector 1. Every other physical product-representation block has an active edge graph of minimum degree at least two: an isolated nontrivial representation at a vertex admits no invariant vector. A finite graph of minimum degree at least two contains a cycle. The original cubic graph has no triangles and no doubled edges, so the cycle has at least four original edges. Each nonzero spin contributes at least 3/4. Therefore

    K|_{physical, 1-perp} >=3.                                (P11)

Consider the original bounded perturbation B(x)=-sum_p x_p W_p, with complex x. Since |W_p|<=2,

    ||B(x)||<=2||x||_1.                                       (P12)

On the contour |z|=3/2, the original resolvent (K-z)^(-1) has norm at most 2/3. Hence I+B(x)(K-z)^(-1) is invertible by its geometric series for ||x||_1<3/4. The contour projection of K+B(x) is analytic there. Along the radial path from zero its rank is constant and equals one. It defines one analytic eigenvalue e(x) with e(0)=0.

On ||x||_1<=3/8, P12 gives ||B||<=3/4. Outside distance ||B|| from spec K, the same resolvent factorization is invertible. The selected eigenvalue lies inside |z|<3/2 and therefore within distance 3/4 of zero, rather than of the remaining spectrum starting at three. This proves

    |e(x)|<=3/4 for ||x||_1<=3/8.                             (P13)

For real x in this region, the original min-max inequalities give E_1(K+B)-E_0(K+B)>=3-4||x||_1>0. The selected real eigenvalue is the actual ground energy with its original scalar 2kappa sum x restored. These arguments do not use any earlier uniform-volume source-series bound.

Let M be the actual number of original plaquettes, and set

    r=3/(16M),   a_source=3/32.                                (P14)

For |z|<=r and |u|,|w|<=a_source, the original parameter vector z*1+u e_p+w e_q has l1 norm at most 3/8. Cauchy's two-variable integral, including p=q where both variables perturb the same source, gives

    |partial_u partial_w e(z*1+u e_p+w e_q) at (0,0)|
       <=(3/4)/a_source^2=256/3.

Thus P5 has the explicit bound

    |R_pq(z*1)|<=128/3 on |z|<=r.                             (P15)

The original central link substitution F21 sends every W_p to -W_p while preserving K and Haar. It carries K+B(x) to K+B(-x); uniqueness of the analytic eigenvalue gives e(-x)=e(x). Consequently R_pq(z*1) has only even powers. Cauchy's coefficient estimate and the geometric sum give the complete tail

    |R_pq(xi)-R_(0),pq-xi^2 R_(2),pq-xi^4 R_(4),pq|
       <=(128/3) (|xi|/r)^6/[1-(|xi|/r)^2],  |xi|<r.          (P16)

The actual M and physical kappa are retained. For any finite complex coefficient vector h, summing the entry bound gives the corresponding quadratic-form error at most the right side of P16 times (sum_p |h_p|)^2. The complete cross terms are included in this sum.

## P4. The full response matrix through degree four

Twice differentiating each original monomial P7-P8 and then applying P5 gives

    R(xi)=(1/3)I+xi^2 R_(2)+xi^4 R_(4)+remainder,
    R_(2)=-(5/36)I+(2/1053)D_degree+(4/1053)A_adj.              (P17)

Here D_degree contains the original face-adjacency degrees, including boundaries, and A_adj is their actual adjacency matrix. For a face p, let t_p^tau count original connected distinct triples of type tau containing p. Let t_pq^tau count those containing p and q, and c_pq count original cubes containing the two distinct faces. The entire degree-four matrix is

    R_(4),pp=-15a-7b d_p-sum_tau c_tau t_p^tau,
    R_(4),pq=-8b 1_(p adjacent q)-2sum_tau c_tau t_pq^tau
              -(d/2)c_pq,  p!=q.                             (P18)

The coefficient signs, ordered pair multiplicities and all cube cross entries are retained. The cube monomial is linear in each of its individual source variables, so its same-variable second derivative is zero; its two-distinct-source derivatives are the displayed off-diagonal contribution.

`generated/response_L2.json` contains all three matrices on the actual 240-face L=2 box. Its degree-four matrix has 9,660 nonzero entries. `generated/response_L3.json` contains the original 756-face L=3 answer. The complete sums of entries agree with -one-half the second homogeneous derivative of the original finite-volume energy; all boundary terms are included.

An initial implementation comparison used a bulk diagonal for an L=2 entry whose degree-four supports meet the boundary. That comparison was corrected: the full bulk anchor row is used only where all its supports are contained, and the finite L=2 matrix is retained without that replacement. The checker explicitly rejects that substitution. The opposite-face entry below has all of its required supports contained in L=2.

## P5. An actual positive response between opposite faces

Take the original faces

    p=(0,0,0;0,1),   q=(0,0,1;0,1).                           (P19)

They are the opposite horizontal faces of one cube. Their degree-zero and degree-two response entries are zero. There are exactly four connecting three-face paths and one cube. Formula P18 gives

    R_(4),pq=-8c_path-d/2
       =4909/14784120+83/3888
       =641033/29568240.                                     (P20)

This includes both the four path contributions and the complete cube contribution. In the actual L=2 vacuum put

    xi=1/10^13,
    g^2=500000 sqrt(10),
    kappa=1000000 sqrt(10)/a,
    r=1/1280.                                                (P21)

Insert these exact values in P16. Rational arithmetic gives the strict enclosure

    21677/10^6 < R_pq(xi)/xi^4 < 21682/10^6.                   (P22)

Thus the original connected zero-energy integrated correlation in P6 is strictly positive, with bounds obtained from P22 by multiplying by xi^4/kappa. No vacuum sampling or spin cutoff is used. The large coupling and the finite volume of this numerical certificate are explicit; its error radius is not assigned a volume-independent value.

## P6. Complete coefficientwise bulk symbol and its raw orientation frame

Each coefficient through degree four depends on a finite set of original nearby faces. Therefore its spatial coefficient limit is exact once those supports are contained in the box. This constructs a coefficientwise finite-range bulk kernel; it does not invoke convergence of the full interacting infinite-volume response.

Index orientations by a=0,1,2 with original plane axes (1,2),(0,2),(0,1). Their actual centers are c_a=(e_i+e_j)/2. For an original counting-norm coefficient function f_a(n), use the explicit Fourier map and inverse

    fhat_a(k)=sum_n exp[-i k.(n+c_a)] f_a(n),
    f_a(n)=(2pi)^(-3)int_[-pi,pi]^3 exp[i k.(n+c_a)] fhat_a(k) dk. (P23)

Orthogonality of the original exponentials proves both inverse laws on finitely supported coefficients and the Plancherel identity with the displayed measure. An entry connecting (n,a) to (n+d,b) has symbol phase exp[i k.(d+c_b-c_a)]. The archive stores all these rational coefficients and twice-center displacements in `generated/plaquette_response.json`; the full adjoint symmetry is checked by (a,b,d)->(b,a,-d).

At k=0 the three-by-three matrix preserves the scalar orientation direction (1,1,1) and the two-dimensional zero-sum space. Their coefficient polynomials are

    R_scalar(0,xi)=1/3-(11/156)xi^2
                    +(211396463/938298816)xi^4,
    R_zero_sum(0,xi)=1/3-(163/1404)xi^2
                    -(22137985/938298816)xi^4.                 (P24)

These are the coefficients through degree four; no omitted tail is set to zero. The actual coordinate frame

    (1,1,1), (1,-1,0), (1,1,-2)

has original Gram diag(3,2,6). Its inverse coordinate map sends x to

    ((x_1+x_2+x_3)/3, (x_1-x_2)/2, (x_1+x_2-2x_3)/6).          (P25)

Multiplication verifies both inverse laws and the Gram. In particular no change to the original orientation norm is used to obtain P24.

## P7. One-plaquette literature cross-check with its exact operator map

For one original plaquette, gauge reduction leaves its holonomy class angle theta in [0,pi], W=2cos(theta), and Haar class measure (2/pi)sin^2(theta)dtheta. The original kinetic operator is

    K=-(d^2/dtheta^2+2cot(theta)d/dtheta).

Set t=theta/2 and y(t)=sin(2t)F(2t). Its exact inverse is F(theta)=y(theta/2)/sin(theta) on the induced operator domain, and its norm return is

    (2/pi)int_0^pi sin^2(theta)|F(theta)|^2 dtheta
       =(4/pi)int_0^(pi/2)|y(t)|^2 dt.                         (P26)

The original equation (K-xi W)F=e F becomes

    y''+[4(e+1)+8xi cos(2t)]y=0.                              (P27)

The branch starting at y=sin(2t) is the Mathieu b_2 branch, with the exact maps q=-4xi and e=b_2(q)/4-1. The full one-plaquette physical energy retains kappa(2xi+e). NIST DLMF equation28.6.5 gives, under that map,

    e=-xi^2/3+5xi^4/216-289xi^6/77760
          +21391xi^8/27993600+... .                           (P28)

The independently executed character recurrence reproduces each of these coefficients. This literature check verifies the displayed one-plaquette convention and coefficient return. The spatial fifth catalogue and cross-face response have their own complete identities and certificates.

The exponential-vacuum and connected-loop setting is credited to the original Hamiltonian coupled-cluster work of Schuette, Zheng Weihong and Hamer, `hep-lat/9603026v1`. No historical-priority or best-known-bound claim is made.

## P8. Completed scope

The completed results are the entire original fifth coefficient, all of its degree-four plaquette-source derivatives, the full response matrices P17-P18, their coefficientwise bulk symbol, and the actual finite-volume analytic enclosure P22. The unit-vacuum scalar, the original energy pairing, all source labels, cube paths and boundary contributions remain attached.

The independent-session report expressly leaves the earlier uniform-gap analytical chain without independent recertification. Its limitation is preserved in the cumulative reading guide. The present P11-P16 calculation is a separate finite-volume proof with its explicit M-dependent radius. It neither upgrades those older claims by repetition nor establishes a nontrivial four-dimensional continuum Yang-Mills field or a finite positive continuum mass.


---

# Supplementary original vacuum-density return

# Separate return through the original vacuum density

This supplementary calculation recomputes the susceptibility coefficients through the original source derivative and the full unit-vacuum density. It does not obtain them by differentiating the stored energy polynomial. It shares the explicitly retained original trace/Haar engine with the coefficient producer.

Let D(x)=exp(2v(x))=sum D_nu x^nu, with D_0=1. The exact Euler derivative gives

    |nu| D_nu=sum_(0<mu<=nu) 2|mu| v_mu D_(nu-mu).

This determines the full required density coefficient, including every ordered product. Its actual mass is Z_nu=P_H D_nu. For a numerator N(x), the coefficients of its original vacuum expectation A=N/Z obey

    A_nu=N_nu-sum_(0<mu<=nu) Z_mu A_(nu-mu),   Z_0=1.

For z_q=partial_xq v, its coefficient is (alpha_q+1)v_(alpha+e_q). Thus the direct original response is

    R_pq=[<W_p z_q>_rho-<W_p>_rho<z_q>_rho].

`source_expectation_check.py` executes these three finite coefficient equations on the actual source indices. No source-mass term is discarded. The required degree-four response uses the fifth source but no higher unknown source coefficient.

For one of the four paths connecting opposite cube faces, the two terms are

    density moment =186029/59136480,
    product of means=1132/369603,
    their difference=4909/59136480.

For the six-face cube source, the two terms are 83/3888 and 0. The complete opposite-face coefficient is therefore

    4*(4909/59136480)+83/3888=641033/29568240.

The file `source_expectation_receipt.json` retains all nine checked original source cases, their faces, multiindices, marked derivatives, both original expectation terms and the resulting connected entry. Cases include the one-face result, both diagonal adjacent-pair multiplicities, an off-diagonal adjacent pair, path/common-edge/corner triples, and the cube. Every value agrees with the independently differentiated sixth-energy polynomial.

The source equations and their coefficient expansions are exact. The full response at positive coupling receives the separately proved finite-volume analytic tail in P13-P22 of the main response proof; this supplementary calculation does not claim that its finite polynomial equals the entire response.

Replay from the cumulative root:

```sh
python -B supplementary_audits/source_expectation_check.py --verify-receipt supplementary_audits/source_expectation_receipt.json
python -O -B supplementary_audits/source_expectation_check.py --verify-receipt supplementary_audits/source_expectation_receipt.json
```


---

# Recovered sixth-source written checkpoint

Only the six delivered proof/result files recorded in RECOVERY_STATUS.json were
available. Their text is preserved. The absent catalogue, producer and formerly
unfinished audits have not been assigned a new successful execution. These
documents are historical statements; the new heat proof has separate inputs.


---

## Retained source: SIXTH_SOURCE.md

# Sixth logarithmic vacuum source: complete original coefficients, scalars and signed derivatives

18 September 2026. Continuation of the cumulative text edition dated 17 September. The objects below are the original finite open SU(2) lattice Hamiltonian and its Taylor coefficients. The earlier source and coefficient files are preserved. In particular, the independent-session report's limitation concerning independent recertification of the historical volume-uniform gap arguments remains in force. This note establishes finite coefficient identities. `EIGHTH_ENERGY.md` and `RESPONSE_AND_REMAINDER.md` supply new energy calculations and a separate, explicitly finite-volume analytic return.

## S1. Original graph, operator, scalar and pairing

Fix L>=2. Vertices are n in {-L,...,L}^3; the positive edge e=(n,i) runs from n to n+e_i whenever both vertices occur. All contained elementary faces p=(n;i,j), i<j, occur with

    W_p=tr[U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)].       (S1)

An inverse traversal always uses that same original link variable. The generators, vector fields, Haar pairing and kinetic operator are

    T_alpha=-i sigma_alpha/2,
    X_e,alpha f=(d/dt)f(...,exp(t T_alpha)U_e,...) at t=0,
    <f,h>_H=int conjugate(f)h dU,
    K=-sum_(e,alpha) X_e,alpha^2.                               (S2)

Here dU is the original product Haar probability measure. Physical functions are invariant under every vertex transformation U_e -> h_s U_e h_t^(-1), including all boundary vertices. Independent original face parameters give

    H(x)=kappa K+kappa sum_p x_p(2-W_p),
    kappa=2g^2/a,  a,g>0,
    x_p=xi=1/(4g^4) on the original homogeneous line.            (S3)

The original unit vacuum and its energy are written

    psi_x=exp(v(x)+c(x)),    P_H v=0,
    c(x)=-1/2 log int exp(2v(x))dU,
    E_0(x)=kappa[2 sum_p x_p+e(x)].                            (S4)

The function c and the scalar 2 kappa sum x_p are retained. On real parameters sufficiently close to zero, the analytic rank-one ground branch and its positive eigenfunction are constructed in `RESPONSE_AND_REMAINDER.md`, A1–A3. Its analytic finite-degree coefficients are the objects calculated here.

Put Q_H=1-P_H and

    Gamma(f,h)=sum_(e,alpha)(X_e,alpha f)(X_e,alpha h),
    B(f,h)=K^(-1)Q_H Gamma(f,h).                               (S5)

The inverse in S5 is on the actual zero-Haar-mean physical coefficient image. Integration by parts and the original eigen-equation yield

    Kv=sum_p x_p W_p+Q_H Gamma(v,v),
    e(x)=-P_H Gamma(v,v).                                     (S6)

Write v=sum_(nu!=0) v_nu x^nu in ordinary monomial coefficients, without divided-power factorials. The equations are

    v_(e_p)=W_p/3,
    Kv_nu=Q_H sum_(0<mu<nu) Gamma(v_mu,v_(nu-mu)),
    P_Hv_nu=0.                                               (S7)

Every multiindex and every ordered split occurs. On the homogeneous line the complete sixth coefficient is

    v_[6]=2B(v_[1],v_[5])+2B(v_[2],v_[4])+B(v_[3],v_[3]).      (S8)

The factor two is the explicit pairing of the ordered indices (i,j) and (j,i) in the symmetric bilinear map Gamma. The two occurrences of the degree-three input remain ordered inside B(v_[3],v_[3]).

## S2. Exact differential and Casimir maps

For the specified Pauli matrices, direct multiplication gives

    sum_alpha tr(T_alpha A)tr(T_alpha B)
       =-tr(AB)/2+tr(A)tr(B)/4,
    sum_alpha T_alpha A T_alpha=-tr(A)I/2+A/4,
    -sum_alpha T_alpha^2=3I/4.                                (S9)

An occurrence of U_e differentiates to T_alpha U_e and an occurrence of U_e^(-1) to -U_e^(-1)T_alpha. The product rule over every occurrence and S9 calculate Gamma and K on complete original trace words. These formulas are the declared inherited `trace_algebra.py` dependency; all shared-edge terms are retained.

The coefficient words are represented using the literal matrix identities: cyclicity of trace, tr(U^(-1))=tr(U) for U in SU(2), cancellation of an adjacent U_e U_e^(-1), and

    tr(U^n)=tr(U)tr(U^(n-1))-tr(U^(n-2)),                       (S10)

which follows by multiplication of U^2-tr(U)U+I=0. Their coordinate kernels are checked in S4 rather than treating a nonempty trace expression as automatically nonzero.

For an original face multiset nu, let r_e count all occurrences of its original edge e. Its complete finite coefficient representation lies in the tensor products with edge-spin lists

    j_e=r_e/2,r_e/2-1,...,(r_e mod 2)/2.                       (S11)

At each original vertex an invariant tensor requires integral total spin and max(j_e)<=sum_(f!=e)j_f. These tests include every actual invariant representation, with its multiplicity. The resulting candidate values

    c=sum_e j_e(j_e+1)                                        (S12)

are stored in each source row. Extra candidates would only add interpolation nodes; none of the actual values is removed.

For their distinct positive values define

    q_C(t)=product_(c>0)(1-t/c),
    f_C(t)=(1-q_C(t))/t-q_C(t)sum_(c>0)1/c.                    (S13)

The numerator 1-q_C has zero constant term. Substitution proves f_C(0)=0 and f_C(c)=1/c for each positive candidate c. The original Casimir action thus proves on this coefficient space

    K f_C(K)=Q_H.                                             (S14)

The zero-Casimir space consists of constants: its energy is int sum|Xf|^2, so every link derivative vanishes. Consequently f_C(K) selects the unique solution of S7 with its original zero Haar mean. The finite spin list is the list of one Taylor coefficient. No projection of the full Hamiltonian onto a finite spin space is performed.

## S3. Complete sixth-order geometry and original coordinate transports

The input is the entire fifth-degree catalogue. Extend each of its original coordinate representatives by one repeated face or one face sharing an original edge, then take its explicit signed-permutation/translation representative. This covers every connected sixth multiset. Indeed a repeated occurrence can be removed; when all faces are distinct, removal of a leaf from a spanning tree of the face-adjacency graph leaves a connected lower multiset. Induction reaches the one-face source.

Every signed coordinate operation is retained as

    y_i=s_i x_(pi(i))-d_i,
    x_(pi(i))=s_i(y_i+d_i),   s_i in {-1,1}.                    (S15)

An original edge goes to the corresponding target edge, or its inverse traversal when the positive orientation reverses. The face word is carried to its target word up to cyclic starting point and reversal, whose traces agree by S9–S10. Variable permutation and inversion preserve product Haar measure. Left and right link Casimirs coincide, so the same operation intertwines K and Gamma.

Each representative is returned to every original multiset containing the anchor edge (0,0,0;0). For a signed image of the representative, translate each positive axis-zero edge to that actual anchor. Duplicates are removed by equality of the complete original face multisets, retaining a specified inverse witness. This enumerates precisely all placements: any placement sends a representative edge to the anchor and therefore occurs in this list. Distinct representatives cannot share an original multiset, since S15 is invertible. No factorial or orbit-size division changes a coefficient.

The complete counts are:

| Original multiplicities | Representatives | Anchored multisets |
|---|---:|---:|
| 6 | 1 | 4 |
| 5+1 | 2 | 84 |
| 4+2 | 2 | 84 |
| 4+1+1 | 19 | 1,572 |
| 3+3 | 2 | 42 |
| 3+2+1 | 31 | 3,144 |
| 3+1+1+1 | 171 | 27,676 |
| 2+2+2 | 9 | 524 |
| 2+2+1+1 | 268 | 41,514 |
| 2+1+1+1+1 | 2,075 | 469,360 |
| 1+1+1+1+1+1 | 4,650 | 1,295,136 |
| Total | 7,230 | 1,839,140 |

Every witness and the original anchored-multiset digest are in `generated/geometry_sixth.json`. `geometry_core.json` is its explicitly indexed view omitting only the large placement lists; it supplies the same coefficient representatives to the worker processes.

The original graph cycle ranks |E|-|V|+1 have distribution

    1:1; 2:6; 3:59; 4:436; 5:2056; 6:4550; 7:121; 8:1.        (S16)

Representative 1906 retains eight independent original chords. All eight enter the coefficient and identity calculations.

Disconnected coefficient supports vanish by S7: its nonzero lower sources have connected face support; two factors in different edge-adjacency components have no common differentiated link, hence Gamma=0. The enumeration therefore covers every nonzero sixth coefficient in every original open box. Boundary return selects exactly the multisets whose original faces are contained in that box.

## S4. Complete tree/quaternion polynomial identities

On each original connected edge union choose the tree obtained by processing its stored edges and accepting each edge that joins two components. Root it at its smallest original vertex. Let t_v be its ordered original tree-path holonomy. For each chord e=(s,t), retain

    Z_e=t_s U_e t_t^(-1).                                     (S17)

The full map from original links to (original tree links, all Z_e) has inverse

    U_e=t_s^(-1)Z_et_t on chords,
    original tree links unchanged.                            (S18)

Both identities follow by substitution. Left/right Haar invariance on each chord and Fubini prove the exact product measure return. The gauge transformation h_v=t_v makes every tree link I. Residual simultaneous conjugation of all chords remains; it removes no chord coordinate.

For every chord c use

    Z_c=x_(c,0)I-i sum_(a=1)^3 x_(c,a)sigma_a,
    sum_(a=0)^3 x_(c,a)^2=1.                                  (S19)

The target is the original coefficient algebra

    A_S=Q[x_(c,a)]/(sum_a x_(c,a)^2-1 for every original chord). (S20)

Its stored polynomial remainder has exponent zero or one in each x_(c,0); the three remaining exponents are retained. The defining monic relations involve different leading variables, so the reductions commute. The original trace algebra maps to A_S by S17–S19 and ordinary quaternion multiplication. Its inverse on the physical-function image substitutes the original Z_e(U).

For completeness, this target is faithful on those functions. A remainder is linear in x_(c,0). Evaluating at both signs of sqrt(1-|y_c|^2), with y_c in the open three-ball, forces both coefficients to vanish on that ball. Iterating over every chord forces the remaining polynomials to vanish on a product of open balls; their coefficients are all zero. Therefore the ideal in S20 is exactly the polynomial relation ideal relevant to these original functions. A zero complete target polynomial proves a zero original physical function, with its source expression and support retained.

For the compiled evaluation, the original free-group map sends each tree-edge letter to 1 and each original chord letter to itself. Its section inserts the chord letters, and their composite on the chord free group is the identity. The word evaluation square commutes with S17–S19: deleting a tree letter substitutes its identity matrix; cancelling adjacent inverse letters uses U U^(-1)=I in the sphere coefficient ring; trace cyclicity and tr(U^(-1))=tr(U) follow from the original determinant-one matrix identity. Every original chord remains a separate generator. The target coefficient at exponent a is exactly sum_m c_m Phi(m)[a] in either evaluation implementation. The compiled program accumulates that same finite rational sum and caches the same chord-word image. Selected output comparisons, including the cube and eight-chord examples, are byte-identical; the complete current replay uses this explicit factorization.

The eighth-chord test retains the actual specialization A_8 -> A_7 given by Z_last=I and the section A_7 -> A_8 inserting the other seven original coordinates. On representative 1906, a specified rational unit-quaternion assignment gives the nonzero difference

    64707599699535109/123037171363830566406250000.

The original and specialized values, all eight quaternion coordinates and their complete map are stored in `generated/eight_chord_witness.json`. Thus the retained coordinate participates in the actual coefficient; its specialization is recorded as a map with a concrete changed value.

The complete source catalogue contains 347,653 rational trace monomials. Every original trace coefficient is delivered in `generated/sixth/0000.json` through `7229.json`. The polynomial audit actually expands every source and its complete residual in S20. Its output stores the coefficient count and SHA-256 of each full sorted expansion, the exact scalar, all signed identities, and the original source-file hash. The full quaternion expansions are additionally exposed for the single-face, closed-cube and eight-chord examples. The complete original trace polynomials and executable map suffice to regenerate every other expansion without accepting any stored digest as a proof.

The audit integrates each full coefficient independently in the chord spheres. For a single original Haar sphere,

    int x^a =0 if any a_i is odd,
    int x^a =product_i (a_i-1)!! / product_(j=0)^(|a|/2-1)(4+2j)
       for every even exponent vector a.                     (S21)

This follows from rotation invariance, sum_i x_i^2=1, and the resulting moment recurrence (equivalently its elementary Gaussian radial integral). Independent chord measures multiply. Every sixth coefficient has exactly zero original Haar mean under this calculation.

## S5. Original sixth scalar and every signed derivative

For degree six the actual raw equation is

    Kv_nu-r_nu=e_nu 1,
    r_nu=sum_(0<mu<nu)Gamma(v_mu,v_(nu-mu)),
    e_nu=-P_Hr_nu.                                            (S22)

The audit retains this scalar before projecting. Its nonzero values reproduce the independently calculated sixth energy: -289/77760 for one face six times; 22285/47309184 for one adjacent 4+2 multiplicity; -4909/118272960, 244/4312035 and -212/542997 for doubled path/common-edge/corner triples; and -83/1944 for the six distinct faces of a cube. All other classes have scalar zero. Each stored raw trace residual is mapped through S17–S20 to its exact displayed constant. Nonempty trace-relation representatives remain in their original rows.

For a distinguished original face p and |rho|=5 define

    Z_(p,rho)=(rho_p+1)v_(rho+e_p).                            (S23)

Differentiating S6 in the same original source coordinate gives

    KZ_(p,rho)-2sum_(0<mu<=rho)
       Gamma(v_mu,Z_(p,rho-mu))
       =(rho_p+1)e_(rho+e_p)1.                               (S24)

Applying Q_H makes the displayed scalar zero at its receiving support; its value is retained upstream. There are 40,221 specified (representative, face-direction) equations.

The two audit implementations prove S24 by equivalent explicit routes. The first expands every signed residual in S20. The second independently assembles the same raw signed RHS and checks the complete trace-coefficient identity

    signed_RHS=(rho_p+1)r_(rho+e_p).                           (S25)

It then carries that exact scalar multiple through the already evaluated full source polynomial. To prove S25 algebraically, put nu=rho+e_p, pair the ordered terms mu and nu-mu using symmetry of Gamma, and add their distinguished exponents: mu_p+(nu_p-mu_p)=nu_p. Both implementations keep all ordered terms before this equality. The second changes repeated evaluation of the same target polynomial, not the equation being certified. Its selected comparison and full replays are separately recorded in `execution/`.

The original center-link substitution

    U_(n,i) -> (-1)^(sum_(j<i)n_j)U_(n,i)                      (S26)

reverses each plaquette trace. Every degree-six monomial therefore has even center parity. This is checked on every original trace monomial; it does not replace the independent Haar-mean calculation S21.

## S6. A completely explicit coefficient

For six occurrences of one original face p,

    v_(6e_p)=132817/391910400
              -27383 W_p^2/65318400
              +5911 W_p^4/130636800
              -797 W_p^6/391910400.                          (S27)

The original character substitution and its triangular inverse give

    v_(6e_p)= -11 chi_1/36450
              +491 chi_2/13996800
              -797 chi_3/391910400,                           (S28)

where chi_1=W^2-1, chi_2=W^4-3W^2+1, and chi_3=W^6-5W^4+6W^2-1. The independent one-plaquette linear-character recurrence followed by its formal logarithm reproduces every coefficient in S28. Its scalar logarithm component and the scalar restoring the original unit vacuum are separately recorded. The raw equation S22 has scalar -289/77760.

## S7. Actual supported source complex and its scalar energy class

For a finite original edge support S and a nonnegative integer N, let E_N(S) be the finite-dimensional space spanned by the original physical polynomial matrix coefficients of total entry degree at most N. Include all coefficient parities and the original constant. Under inclusion of supports and increase of N, maps insert identity functions on additional original links. They preserve P_H and intertwine K. Consequently the actual cochain diagram is

    C^0_N(S)=ker(P_H:E_N(S)->C)
       -- K --> C^1_N(S)=E_N(S) --0-->0.                      (S29)

K preserves each space and is invertible on its mean-free part by S12–S14. Thus its first cohomology has the explicit inverse maps

    H^1(C_N(S)) -> C,  [r] -> P_Hr,
    C -> H^1(C_N(S)),  c -> [c1].                            (S30)

Their compositions are identities: r-(P_Hr)1=K f_C(K)r, and P_HK=0. The inverse primitive is the original f_C(K)Q_Hr. The support transitions commute with S30. Applying the Split Zero support reconstruction retains each original label and represents its relation by the zero in that receiving fibre.

For the actual sixth source r_nu, its retained scalar class is -e_nu. Its mean-free primitive is v_nu. Equation S24 supplies the corresponding derivative of that same class; it does not erase the scalar ground-energy contribution. As a formal trace observation, the map to S20 has the explicitly identified trace-relation kernel, so an original supported expression and its receiving zero are both available.

The remaining source terms are also recorded. Put q_6=sum_(i=1)^6 V_i(x). Its complete defect is

    R_6=sum_p x_p W_p/3+B(q_6,q_6)-q_6
       =sum_(7<=i+j<=12,1<=i,j<=6)B(V_i,V_j).                 (S31)

The signed defect is exactly

    K partial_p q_6-W_p-2Q_H Gamma(q_6,partial_p q_6)
        =-K partial_p R_6.                                   (S32)

The degree-five derivative calculation closes precisely the displayed coefficients; S31 retains all higher degrees. The formal parameter observation modulo m^6 has kernel m^6, with its original face labels and coefficients. The physical inverse and response norms used in the subsequent note are returned through the actual unit vacuum, not assigned from the coefficient norm of this source complex.

## S8. Evidence and attribution

The catalogue is complete by S3, and its complete-function equation checks use S9–S21. Ordinary and optimized execution records state exactly which commands and files were replayed. Finite exact polynomial certificates, the written analytic proof of a separate finite-volume radius, and historical claims have distinct scopes. No new Lean run, external analytical review, improved volume-uniform coupling threshold, or four-dimensional continuum mass-gap result is asserted.

The exponential-vacuum and linked character/Casimir methods retain their Hamiltonian coupled-cluster antecedents, including Schütte, Zheng Weihong and Hamer, hep-lat/9603026v1. The original Split Zero coefficient/support framework and all inherited trace, geometry and sphere-map files remain identified in `SOURCE_INTAKE.json`. The new complete coefficient catalogue and its energy/response return are offered for review without a global priority claim.

The separate direct original-matrix check evaluates K and Gamma by quaternion matrix jets, rather than by the Fierz-contracted trace differential routines. In its retained-gradient implementation, each finite original gradient vector (X_(e,alpha)v_mu)_(e,alpha) is evaluated once at the declared rational link assignment. Every ordered pair (mu,nu-mu), including zero contributions, then returns its complete dot product. Derivatives on links absent from an original word are exactly zero by the original coordinate definition; these positions remain in the full gradient vector. The implementation comparison checks the same K value, Gamma sum, scalar and source hash against the direct non-cached routine. The complete per-row ordered pairing list is stored. These single-point derivative regressions accompany the full function identities proved in S4–S5; they are not used in place of the polynomial identity test.

## S9. Direct local derivative bounds without an exterior-volume factor

There is an additional bound using only the newly calculated original trace polynomials, independent of the older Fourier-source norm arguments. For one term

    c_m product_(w in m) tr(U_w)

let k(m) be its number of original trace factors, r_e(m) its number of occurrences of original edge e, and ell(m)=sum_e r_e(m) its total original entry count. All monomials in the sixth source have ell(m)<=24.

For any original unitary SU(2) product A, the same Pauli identity gives

    sum_alpha |tr(T_alpha A)|^2=1-(tr A)^2/4<=1.             (S33)

Cyclically moving the differentiated occurrence inside its original trace therefore bounds its three-component derivative vector by one. The other k-1 original traces have absolute value at most two. Applying the triangle inequality to all differentiated occurrences proves

    |X_e v_nu|_(three components)
       <= sum_m |c_m| r_e(m) 2^(k(m)-1)=C_(nu,e).             (S34)

For an ordered second derivative, the original matrix norm of each generator is 1/2. Two differentiated occurrences, including two on the same original link, have product norm at most 1/4. The trace bound gives

    |X_(f,beta) X_(e,alpha) v_nu|
       <= sum_m |c_m| r_e(m) r_f(m) 2^(k(m)-2).               (S35)

Every occurrence remains; the order of two generators is not interchanged. Summing over all original f and beta at a fixed e,alpha gives the row bound

    D_(nu,e)=3 sum_m |c_m| r_e(m) ell(m)2^(k(m)-2)
       <=36 C_(nu,e).                                        (S36)

For every original anchored placement in S3, use the inverse coordinate map S15 to read the exact representative edge mapped to the anchor. If its operation is (pi,s) and translation d, the first endpoint has x_(pi(i))=s_i d_i; the positive lower endpoint is decreased by one in coordinate pi(0) precisely when s_0=-1. This constructs its actual edge label, counted in the stored anchor-preimage register. Reversal of an edge is handled by differentiating the transported original inverse word in S9; it has the same bounds in S34–S35. No derivative of an unrecorded frame change is discarded.

Summing C_(nu,e) and D_(nu,e) over all 1,839,140 original anchored multisets proves, on every original box and every original link,

    sup_U (sum_alpha |X_(e,alpha)v_[6](U)|^2)^(1/2)
        <=C_6<1085503440,

    max_(e,alpha) sum_(f,beta)
         ||X_(f,beta)X_(e,alpha)v_[6]||_infinity
        <=D_6<35700643605,
    D_6<=36 C_6.                                              (S37)

The exact rational values, all 7,230 per-representative rows, every original edge budget and anchor-preimage count are in `generated/local_derivative_bounds.json`. An open boundary selects a subset of the positive bounding contributions, so the constants contain no exterior-volume factor. They bound the sixth Taylor coefficient only. Its contribution to the actual drift 2kappa Xv is multiplied by the original factor 2kappa xi^6; no estimate for all remaining orders is inferred from this one coefficient. These concrete quantities are retained inputs for the next original residual calculation S31.


---

## Retained source: EIGHTH_ENERGY.md

# Complete eighth ground-energy coefficient and the original fourth-jet return

18 September 2026. The result concerns the original finite open SU(2) Hamiltonian in S1–S4 of `SIXTH_SOURCE.md`. It gives every inhomogeneous degree-eight scalar coefficient, with open-boundary counts, two independent recurrence assemblies and explicit original Haar integration. `RESPONSE_AND_REMAINDER.md` proves the finite-volume all-higher-order enclosure and the physical observable return. Earlier uniform-gap arguments are not used as premises for that enclosure.

## E1. A fourth-jet identity with the complete state norm retained

Put S(x)=sum_p x_p W_p and H(x)=kappa[K-S(x)+2 sum_p x_p]. The scalar e(x) is the analytic eigenvalue of K-S(x) issuing from zero. The original unit vacuum psi_x is strictly positive at small real x. Its original Haar coefficient m(x)=P_Hpsi_x is then positive. Retain the explicit coordinates

    u(x)=psi_x/m(x),     psi_x=m(x)u(x),
    P_Hu=1,             m(x)^2<u,u>_H=1.                    (E1)

The coordinate m is not dropped from the physical vacuum. It cancels from the following quotient by the displayed multiplication, while the original denominator is retained. Equivalently, u is the unique formal eigenvector section with original constant coefficient one and zero Haar mean in every higher coefficient.

Write u=sum_(j>=0)u_[j](x), u_[0]=1, with u_[j] homogeneous of degree j. The rank-one resolvent branch is analytic in the original graph norm near x=0: its eigen-equation gives Ku=(e+S)u, whose right side is analytic in L^2, and therefore both u and Ku are analytic. Define the actual finite polynomial vector

    phi_4=sum_(j=0)^4 u_[j],     w=u-phi_4.                  (E2)

For fixed real source direction x and scalar t near zero, w(tx)=O(t^5) in the graph norm of K. Since (K-S-e)u=0 and K-S is self-adjoint on real x, expansion of both sides gives the exact equality

    <phi_4,(K-S)phi_4>_H/<phi_4,phi_4>_H-e
       =<w,(K-S-e)w>_H/<phi_4,phi_4>_H.                    (E3)

All four cross terms cancel by the actual eigen-equation; the denominator is the original Haar state norm, tending to one. Cauchy–Schwarz in L^2 and the graph-norm bound give an O(t^10) right side. Thus the full quotient in E3 reproduces every original energy coefficient through degree nine. Repeating over real directions proves the multivariate coefficient identities; each coefficient is a polynomial in the original x_p, so equality on an open real set proves equality of all coefficients. This argument does not apply a conjugate-linear quotient as a holomorphic function away from real parameters.

The original center-link action S26 sends S(x) to -S(x) and commutes with K. The analytic eigenvalue is unique, so e(-x)=e(x). Its odd homogeneous coefficients are zero. The original coefficient recurrence for E1 is

    Ku_[n]=S(x)u_[n-1]+sum_(j=1)^n e_[j]u_[n-j],
    P_Hu_[n]=0 (n>0),
    e_[n]=-<1,S(x)u_[n-1]>_H.                               (E4)

It uses all original face variables. Only a finite Taylor coefficient is evaluated; the full operator retains every spin.

## E2. The complete eighth quotient and its exact return

Let u_j denote u_[j] in this section. Since P_Hu_j=0 for j>0, the degree-eight numerator and the denominator coefficients of E3 are

    N8=<u4,Ku4>-2<u3,S(x)u4>,
    D6=2<u2,u4>+<u3,u3>,
    D4=2<u1,u3>+<u2,u2>,
    D2=<u1,u1>.                                               (E5)

All pairings are the original Haar pairings, interpreted coefficientwise on real polynomial vectors. Dividing the full power series in E3 gives

    e8=N8-e2 D6-e4 D4-e6 D2.                                 (E6)

The original degree-four eigenvector equation is

    Ku4=S(x)u3+e2 u2+e4*1.                                  (E7)

Taking its pairing with u4, with P_Hu4=0, gives

    <u3,S(x)u4>=<u4,Ku4>-e2<u2,u4>.                         (E8)

Substitution of E8 in E5–E6 cancels the two actual e2<u2,u4> contributions. Therefore the same coefficient is

    e8=-<u4,Ku4>-e2<u3,u3>
       -e4(2<u1,u3>+<u2,u2>)-e6<u1,u1>.                    (E9)

Both E6 and E9, with every contributing term, are stored separately in every row. No product of means or quotient denominator is omitted. The first producer checks that their complete original multiindex sums agree.

For a specified original multiplicity nu, the product <u_a,u_b>_nu in these formulas means precisely

    sum_(mu<=nu,|mu|=a) <u_mu,u_(nu-mu)>_H,
    |nu|=a+b.                                                (E10)

The multiplication by S adds one distinguished original face with its actual multiplicity index. This specifies every ordered input of the calculation.

## E3. Complete classification of the degree-eight scalar supports

Multiplication of one original edge variable U_e by the central element -I preserves K, the original Haar measure and the physical subspace. It changes the sign of precisely the face terms incident on that edge. Uniqueness of the analytic ground branch therefore forces an energy coefficient e_nu to vanish unless

    sum_(p containing e)nu_p is even for every original edge e. (E11)

The faces whose multiplicities are odd form a finite cubical two-cycle over F_2. Its finite filling by cubes has an explicit construction. At each cube, assign the parity of the horizontal marked faces above it on the positive third-coordinate ray. Finite support gives zero outside a bounded region. The horizontal boundary differences reproduce those horizontal faces; the two-cycle identities at horizontal edges force the vertical boundary differences to reproduce the other faces. Hence the boundary of this finite cube chain is exactly the specified marked face set. The filling is unique: a nonzero finite cube chain has a highest exposed horizontal face.

For any finite nonempty cube set, each nonempty coordinate column has at least two boundary faces perpendicular to that coordinate. With at least two distinct cubes, their three coordinate-plane projections have total cardinality at least five: two distinct cube positions have distinct images in at least two of the three projections. Thus the boundary contains at least ten faces. A boundary of at most eight faces consequently is either empty or consists of the six faces of one original cube.

At total degree eight, E11 therefore permits exactly these cases:

1. Every multiplicity is even. Dividing each displayed integer multiplicity by two gives an original degree-four face multiset; multiplying it back by two is the inverse map. This yields the 78 complete connected fourth-source representatives.
2. Six cube faces have odd multiplicity, and two additional occurrences are put on one original face. This face is either a face of the cube (one multiplicity becomes three), or an external face occurring twice.

The scalar coefficient is connected in original face-edge adjacency. One way to prove this is the source recurrence S7: all nonzero lower logarithmic sources are connected, and Gamma requires a common differentiated edge. Its Haar scalar has the same property. For an external doubled face in case 2, it must therefore share an original edge with the cube. There are exactly 24 such external faces, and the original signed cubic coordinate group acts transitively on them. The six choices of a marked cube face are also one orbit. The proof retains their actual placements; it does not divide their coefficients by these counts.

Thus the full degree-eight scalar catalogue consists of exactly 80 coordinate representatives: 78 doubled fourth-source representatives, one marked cube, and one cube with an adjacent external doubled face. `generated/energy8_patterns.json` records every source multiset and inverse coordinate witness. `generated/energy8/000.json` through `079.json` contain all coefficients and all terms of E6 and E9.

## E4. Explicit coefficients, including both cube families

A few readable components of the complete catalogue are

    e_(8e_p)=21391/27993600,
    e_(6e_p+2e_q)=-684413851/5147712311040  (p adjacent q),
    e_(4e_p+4e_q)=-322564213/2789727962112  (p adjacent q).     (E12)

For six faces C=boundary(cube) and a marked p in C,

    e_(sum_(q in C)e_q+2e_p)
       =366249151389169/58572365289984000.                    (E13)

For an original external face p adjacent to C,

    e_(sum_(q in C)e_q+2e_p)
       =-336785779/647189637120.                             (E14)

Equations E13–E14 retain the distinct original multiplicities and complete shared-edge recouplings. They include all original scalar returns, rather than only a boundary-length approximation to an intermediate representation.

For four distinct faces in an original straight face-adjacency path, with each face occurring twice, the coefficient is

    c_path4=-41237423/40314521145600.                          (E15)

The full list includes all other four-face shapes and their original words, rather than assigning E15 to an unspecified path geometry. Its use for the two-separated-face response is checked on exactly the four shapes returned in `RESPONSE_AND_REMAINDER.md`.

The independent program `audit_energy_eight.py` reconstructs E4 through degree seven and then takes the original Haar scalar at degree eight, without using E6, E9 or supplied sixth-energy coefficients. It reproduces all 80 entries. The linear recurrence and the fourth-jet producer share the declared exact trace, Casimir and Haar implementation. The separately recorded chord-sphere integration tests use the original product-S^3 moments as an additional scalar-return check. Their scope is given by their exact execution record.

## E5. Exact open-boundary embedding counts

For every representative apply all 48 original signed coordinate operations and translate the minimum coordinate to zero. Equality of the complete oriented face multisets identifies duplicate images, leaving a list of distinct original oriented shapes. For one such shape, let w_i be the extent of its original vertices in direction i. In the box with side m=2L, the original translation coordinates lie in

    -L<=n_i<=L-w_i,

so there are exactly product_i(m+1-w_i) placements. All displayed shapes have w_i<=4, and L>=2 covers the complete list. Planar supports retain the factor m+1 in their unused direction. The inverse map reads the original minimum vertex and its unique translated shape.

Each original face multiset has exactly one such shape and translation, so the count introduces no orbit-size or factorial correction. Multiplying these integer count polynomials by the coefficients in E12–E14 and all remaining rows yields

    e8,L=A3 m^3+A2 m^2+A1 m+A0,       m=2L,                  (E16)

where

    A3=1703320005700992315276593/68235298203010622261760000,
    A2=421994013280213546390961/31615192631460259261440000,
    A1=14702805516554176523/16975106412310126080000,
    A0=404673359378191/1312237663289280000.                    (E17)

`energy8_response.json` retains each shape's widths, integer embedding polynomial and independently enumerated L=2 placement count and digest. Every finite placement is verified against the actual contained face set before differentiation.

In particular the L=2 box has M=240 and

    e8,L=9876448280610811115073772847/
          5441765031690097125375360000.                       (E18)

The coefficient per original plaquette has the exact spatial limit

    e8,bulk/face=A3/3
      =1703320005700992315276593/
         204705894609031866785280000.                         (E19)

This is the limit of the coefficient of xi^8. The complete finite-volume analytic remainder is stated separately and retains its actual dependence on M.

## E6. Complete original energy and external single-face check

The lower coefficients retained from the independently checked predecessor are

    e2,L=-M/3,
    e4,L=5M/216-2J/1053,
    M=3m^2(m+1),   J=6m(3m^2-1),
    e6,L=-(211396463m^3+30959193m^2+21845782m+2336684)/4691494080.
                                                                    (E20)

The original physical energy therefore has the complete displayed series

    E0,L=kappa[2Mxi+e2,L xi^2+e4,L xi^4+e6,L xi^6+e8,L xi^8]
          + original higher-order remainder.                 (E21)

The independent one-face character recurrence reproduces E12 and every lower one-face coefficient. For the original class angle theta, W=2cos(theta) and

    K=-(d_theta^2+2cot(theta)d_theta).

The exact coordinate map t=theta/2, y(t)=sin(2t)F(2t), with inverse F(theta)=y(theta/2)/sin(theta) on the induced domain, has the norm return

    (2/pi)int_0^pi sin^2(theta)|F(theta)|^2dtheta
      =(4/pi)int_0^(pi/2)|y(t)|^2dt.                          (E22)

The original eigen-equation becomes y''+[4(e+1)+8xi cos(2t)]y=0. Thus its branch is

    q_Mathieu=-4xi,   e_one=b_2(q_Mathieu)/4-1,
    E_one=kappa(2xi+e_one).                                  (E23)

NIST DLMF 28.6.5 gives the coefficient 21391/27993600 after exactly this substitution. This checks the single-face convention and coefficient. The full spatial catalogue, its two cube families and its boundary return have the separate original-coordinate calculations above.

## E7. Scope and source credit

The complete tables are finite exact Taylor calculations with full original representation lists. E3 supplies the all-state variational identity underlying the new fourth-jet evaluation. A separate finite-volume contour proof encloses the uncomputed orders; it does not invoke the historical volume-uniform source norm estimates. No new continuum gap, volume-independent analytic radius, external analytical review, Lean certificate or global priority claim is made.

The original Hamiltonian exponential-vacuum/linked-cluster and character methods retain their attribution to Schütte–Zheng–Hamer and the predecessor workbench sources. NIST's authored Mathieu chapter is cited for E23 only. The complete used local dependency identities and original publication URLs are in `SOURCE_INTAKE.json`.


---

## Retained source: RESPONSE_AND_REMAINDER.md

# Full sixth-degree plaquette response and a certified two-spacing correlation

18 September 2026. This note returns the complete eighth energy coefficient to the original state, energy and time pairings. It proves its own finite-volume analytic remainder from the original free physical gap and bounded plaquette multiplication. The radius depends on the actual number M of plaquettes. No historical uniform-coupling estimate is used to remove that dependence.

## A1. Original analytic branch on an explicit finite-volume domain

Retain H(x), K, W_p, kappa, the original product Haar measure and all vertex gauge constraints from S1–S4 of `SIXTH_SOURCE.md`. The free physical constant is the unique zero eigenvector of K. A nonconstant physical Fourier component has an active edge graph whose vertices have no degree one: a single nonzero SU(2) representation at a vertex has no invariant vector. Every finite active component therefore contains a cycle. The original cubic graph has neither doubled edges nor triangles, so at least four nonzero edges occur. Their original Casimirs are each at least 3/4. Hence

    K|_(physical,1-perp)>=3.                                 (A1)

The invariant part of the original compact product-group Laplacian has domain H^2_phys, compact resolvent and form domain H^1_phys. This follows from its product representation decomposition, or equivalently the compact elliptic Laplacian. Original smooth bounded plaquette multiplication preserves the operator domain.

For the complex original source vector x, set B(x)=-sum_p x_p W_p. Its bound is

    ||B(x)||<=2||x||_1.                                      (A2)

On |z|=3/2, A1 gives ||(K-z)^(-1)||<=2/3. Thus I+B(x)(K-z)^(-1) has its convergent Neumann inverse for ||x||_1<3/4. The contour projection of K+B(x) is analytic throughout that ball; along the radial path from zero it has constant rank one. Its unique enclosed eigenvalue is the analytic e(x) with e(0)=0.

For ||x||_1<=3/8, the perturbation norm is at most 3/4. The same resolvent factorization outside the ||B||-neighbourhood of spec(K) confines the enclosed eigenvalue to |e|<=3/4: points inside |z|<3/2 cannot be within 3/4 of the remaining spectrum starting at three. Therefore

    |e(x)|<=3/4 on ||x||_1<=3/8.                             (A3)

For real x in this region, the min-max principle on the same physical domain gives

    gap(K+B(x))>=3-4||x||_1>=3/2.                            (A4)

The contour branch is consequently the actual ground energy, and its strictly positive smooth unit eigenvector psi_x exists by the elliptic maximum principle and the modulus form inequality. Ground-state simplicity also follows directly from the original identity

    q_(H-E0)(psi_x f)=kappa int psi_x^2 sum_i|X_i f|^2.        (A5)

This identifies the branch and the physical vacuum used below. It proves each inverse below on the actual centered space; no unknown mass-gap lower bound is imposed as a hypothesis.

The analytic source coefficients also have their original smooth domains. Near x=0, the contour projection applied to 1 has a nonzero Haar coefficient. Dividing by that retained scalar gives the section u of E1, and its inverse multiplies by the same scalar. The equation Ku=(e+S(x))u first gives graph-norm analyticity. Each original W_p is smooth, and multiplication by it is bounded on every fixed Sobolev space of this compact product. Repeating the equation and elliptic regularity gives analyticity in H^{2r} for every finite r. Sobolev embedding at a sufficiently large r gives C^k analyticity for any chosen k. For real sources near zero, u remains positive in C^0, so its original logarithm is analytic there as well. Subtracting its explicitly retained Haar scalar gives precisely v and S6. This establishes that the unique finite coefficient solutions calculated in the source catalogue are the actual Taylor coefficients of this original vacuum.


## A2. Scalar symmetry and the full physical energy remainder

Let C be the original Haar-unitary link-center substitution

    U_(n,i) -> (-1)^(sum_(j<i)n_j)U_(n,i).

It preserves K and reverses every original W_p. In the complete Hamiltonian,

    C H(x) C^(-1)=H(-x)+4kappa sum_p x_p I.                   (A6)

The original scalar 2 kappa sum_p x_p is retained on both sides. After using its specified decomposition E0(x)=kappa[2 sum x_p+e(x)], uniqueness of the analytic branch gives e(-x)=e(x).

Put M=|P_L| and

    R=3/(8M).                                                (A7)

The homogeneous line x_p=z satisfies ||x||_1=M|z|. A3 and Cauchy's coefficient formula bound the nth coefficient of e(z*1) by (3/4)R^(-n). Summing the even terms from degree ten yields

    |e(xi)-e2,L xi^2-e4,L xi^4-e6,L xi^6-e8,L xi^8|
      <=(3/4)(|xi|/R)^10/[1-(|xi|/R)^2],  |xi|<R.            (A8)

Multiplication by kappa returns the physical energy remainder. The complete coefficients e2,L through e8,L, with their original boundary terms, are in E16–E21 of `EIGHTH_ENERGY.md`. At L=2, M=240, R=1/640.

## A3. Actual source derivatives and the original zero-energy response

Write A=H-E0, rho=psi_x^2. The multiplication map

    U_psi:L^2(rho dU)->L^2(dU),  f->psi_x f,
    U_psi^(-1)h=h/psi_x

has both inverse identities and pairing

    <U_psi f,U_psi h>=int rho conjugate(f)h dU.               (A9)

Let z_p=partial_(x_p)v and Z_p=z_p-<z_p>_rho. Differentiating the original unit mass in S4 gives

    partial_p c=-<z_p>_rho,    partial_p psi=psi Z_p.          (A10)

The original derivative of the Hamiltonian is kappa(2-W_p). Differentiating its actual eigen-equation, with the original scalar included, yields

    partial_p E0=kappa(2-<W_p>_rho),
    Atilde Z_p=kappa(W_p-<W_p>_rho),
    Atilde=U_psi^(-1) A U_psi.                               (A11)

For the actual centered physical states r_p=(W_p-<W_p>_rho)psi, define

    mathcal R_pq(x)=kappa<r_p,A^(-1)r_q>
                  =-1/2 partial_p partial_q e(x)
                  =q_Atilde(Z_p,Z_q)/kappa.                 (A12)

The real positive vacuum and real trace functions make these real symmetric entries; complex combinations give the full Hermitian positive semidefinite form. To prove the middle equality, differentiate <W_p> using A10 and use A11 to write its derivative as 2kappa<r_p,A^(-1)r_q>. This keeps all off-diagonal pairings.

The full finite-volume gap A4 proves convergence of the physical time integral

    int_0^infinity <r_p,exp(-tA)r_q>dt=mathcal R_pq/kappa.     (A13)

The factor 1/kappa remains attached to the original physical time. Neither a coefficient matrix nor its source norm replaces the actual pairing in A12.

## A4. A separate analytic bound for the response through degree six

Set

    r=3/(16M),    a_src=3/32.                                 (A14)

For |z|<=r and |u|,|w|<=a_src, the original vector z*1+u e_p+w e_q has l1 norm at most 3/8. The two-source Cauchy integral applied to A3 gives

    |partial_u partial_w e(z*1+u e_p+w e_q)|_(u=w=0)
      <=(3/4)/a_src^2=256/3.                                 (A15)

This includes p=q: u and w are two independent variables for the same original face coordinate, so partial_u partial_w is exactly partial_p^2. By A12, |mathcal R_pq(z*1)|<=128/3. A6 makes this homogeneous response even. Thus

    |mathcal R_pq(xi)-(R0)_pq-xi^2(R2)_pq-xi^4(R4)_pq-xi^6(R6)_pq|
      <=(128/3)(|xi|/r)^8/[1-(|xi|/r)^2],   |xi|<r.           (A16)

The actual M remains in r. Contracting by any finite coefficient vector h gives a quadratic-form error bounded by the right side times (sum_p |h_p|)^2, which keeps all mixed terms.

## A5. Complete original response matrices through degree six

The retained lower matrices are R0=I/3 and

    R2=-(5/36)I+(2/1053)D_degree+(4/1053)A_adj.                (A17)

The complete original R4, including all three-face and cube contributions, is preserved in the predecessor `20260917-fifth-source/PLAQUETTE_RESPONSE.md` and its finite-box tables. No bulk diagonal is substituted for an original boundary row.

For the complete eighth energy monomials sum_(|nu|=8)e_nu x^nu, the new coefficient is

    (R6)_pq=-1/2 sum_(|nu|=8) e_nu nu_p(nu_q-delta_pq).        (A18)

The sum is over the actual original embeddings in the specified box. Each face, multiplicity, and pair of derivative directions remains in A18. The 80 complete coefficients are classified and calculated in E3–E4.

The producer independently enumerates every fitting translate and checks membership in the original box face list before applying A18. For L=2, `generated/response6_L2.json` contains the original ordering of 240 faces and all 20,796 nonzero entries. It verifies the exact adjoint symmetry and the complete scalar return

    sum_(p,q)(R6)_pq=-28 e8,L.                                (A19)

The factor 28 is 8*7/2 from twice differentiating the same homogeneous energy, not a discarded count of mixed derivatives. Each individual matrix entry has the analytic error A16 when combined with R0,R2,R4.

## A6. A positive actual response across two original lattice spacings

Use the original horizontal faces

    p=(0,0,0;0,1),    q=(0,0,2;0,1).                         (A20)

Their centers differ by the original displacement 2e_2. In the L=2 box both faces and all contributing intermediate faces are contained. R0 and R2 give zero. A pair of these faces cannot lie in one elementary cube or a connected triple of faces, so the complete previous R4 entry is also zero; the retained finite matrix verifies this directly.

At degree six, A18 has exactly four nonzero original contributions. Each consists of p,q and the two successive side plaquettes on one side of the two-cell column. All four doubled face-multisets are explicitly listed in `energy8_response.json`. Their actual coefficient is E15. The two cube families E13–E14 cannot span A20 at this total order: an attached face shares an original cube edge, whereas the second horizontal face in A20 is one complete spacing beyond the nearest cube face.

Thus

    (R6)_pq=-8 c_path4=41237423/5039315143200.                 (A21)

The same value is obtained from the complete 240-face matrix and independently from all original bulk translates containing p. The original four individual contributions remain in the record.

Take the actual parameters

    xi=1/10^18,  g^2=500000000,  kappa=1000000000/a,
    M=240, r=1/1280, a>0.                                   (A22)

Let

    E_R=(128/3)(1280xi)^8/[1-(1280xi)^2].                     (A23)

The exact rational certificate evaluates c_path_response-E_R/xi^6 and c_path_response+E_R/xi^6, proving

    81828/10^10 < mathcal R_pq(xi)/xi^6 < 81835/10^10.         (A24)

All endpoints are rational and checked without floating acceptance tests. In decimals these are 8.1828*10^(-6) and 8.1835*10^(-6). The original integrated connected correlation is strictly positive, with bounds obtained by multiplying A24 by xi^6/kappa. This states the sign of its full time integral; no pointwise-in-time sign is assigned from that calculation.

A22 is a large-coupling finite-volume certificate. Its error radius is the actual A14. No infinite-volume or continuum analytic conclusion is assigned to this particular bound.

## A7. Coefficientwise spatial Fourier return with the original orientation norm

Every degree-six response coefficient has a finite original support. Once that support is inside a box, its coefficient is unchanged. This gives a coefficientwise bulk finite-range kernel. Its complete anchor rows for orientations a=0,1,2, with planes (1,2),(0,2),(0,1), are stored in `generated/response6_bulk.json`.

For an original counting-norm coefficient sequence f_a(n), let c_a=(e_i+e_j)/2 be the actual face-center offset. The Fourier map and inverse are

    fhat_a(k)=sum_n exp[-i k.(n+c_a)]f_a(n),
    f_a(n)=(2pi)^(-3)int_[-pi,pi]^3 exp[i k.(n+c_a)]fhat_a(k)dk. (A25)

Orthogonality of the original exponentials proves both inverse laws on finite sequences and the same Plancherel pairing with the displayed measure. A matrix entry from (n,a) to (n+d,b) has the original phase exp[i k.(d+c_b-c_a)]. The full transpose/negative-displacement involution gives the Hermitian symbol.

At k=0, the sixth coefficient on the original scalar orientation direction (1,1,1) is

    -1703320005700992315276593/7310924807465423813760000.       (A26)

On the zero-sum orientation plane it is

    347891210081791900228897/20470589460903186678528000.        (A27)

The complete original frame (1,1,1),(1,-1,0),(1,1,-2) has Gram diag(3,2,6). Its inverse coordinate map is

    x -> ((x0+x1+x2)/3,(x0-x1)/2,(x0+x1-2x2)/6).              (A28)

Multiplication proves both inverse identities and the stated Gram. Equations A26–A27 do not change that metric. A26 also equals -28 times the eighth energy per original plaquette in E19, as the full scalar Hessian sum requires.

The complete two original orientation coefficient series through xi^6 are

    R_scalar(0,xi)=1/3-(11/156)xi^2
       +(211396463/938298816)xi^4
       -(1703320005700992315276593/7310924807465423813760000)xi^6,

    R_zero_sum(0,xi)=1/3-(163/1404)xi^2
       -(22137985/938298816)xi^4
       +(347891210081791900228897/20470589460903186678528000)xi^6,
                                                                    (A29)

with the higher coefficients still to be determined. These are exact coefficientwise spatial returns, not an assignment of the finite-volume analytic radius to infinite volume.

## A8. Original plaquette readout through seventh degree

Define the actual original average half-trace

    P_L(xi)=(1/(2M))sum_p <W_p>_rho.                          (A30)

The map from the original trace expectation to this specified readout retains its factor 1/(2M). Differentiating the complete physical energy at fixed kappa gives

    dE0/dxi=kappa[2M-sum_p<W_p>_rho].                         (A31)

The derivative of the original unit-vacuum mass cancels the two eigenvector derivative terms; no change of physical pairing is made. Consequently

    P_L=xi/3-(2e4,L/M)xi^3-(3e6,L/M)xi^5-(4e8,L/M)xi^7
          +retained tail.                                   (A32)

Differentiating the absolutely convergent scalar coefficient series from A3, with t=|xi|/R, proves

    |tail in A32| <= t^9(10-8t^2)/(1-t^2)^2,   |xi|<R.       (A33)

Indeed the coefficient factor is (3/4)/(2MR)=1 for the specified R=3/(8M); the entire dependence on M remains in t. This derivative estimate comes from the full Cauchy coefficient bound, not differentiation of an unsigned pointwise remainder alone.

Its coefficientwise spatial seventh coefficient is -4 times E19. The existing third and fifth coefficients remain -11/468 and 211396463/4691494080, respectively. E17 supplies every boundary correction for finite L.

## A9. Scope, next original quantity and evidence

The completed outputs are every sixth source coefficient, its original scalar and signed derivative equations, all 80 eighth energy coefficients, the complete sixth-degree response matrix and symbol, and the actual finite-volume bound A24. The archive retains the source-to-physical equations A9–A13 and the finite-volume parameter range A14–A16.

The standing simultaneous continuum path has a_n=a_0*2^(-n) and g_n^2=1/(g_0^(-2)+beta*n*log 2). This note derives no lower bound on the full continuum spectrum along that path. In particular M enters A7 and A14. The historical volume-uniform gap claims remain at their prior audit scope; neither the new finite coefficients nor their checksum records recertify those analytical arguments.

The next source coefficient is the original v_[7]=2B(v_[1],v_[6])+2B(v_[2],v_[5])+2B(v_[3],v_[4]). The sixth table is a completed input, while S31 retains the full residual of the current q_6. A quantitatively useful next response task is to evaluate that original residual and its energy pairing on growing supports, keeping the finite-volume radius and all scalar returns explicit. No automatic continuation, paid model job or remote merge is started by this checkpoint.

## A10. A sharper original-Haar Schur bound and its complete Cauchy return

The exact original Haar matrix elements give more information than A2 alone. Let P_H be the original rank-one projection onto 1, and Q_H=I-P_H. For distinct elementary faces p,q, at least one original link belongs to just one of them; its central sign makes the Haar integral of W_p W_q zero. For one face, retain U_1,U_2,U_3 and set Omega=U_1 U_2 U_3^(-1) U_4^(-1). The inverse is U_4=Omega^(-1)U_1 U_2 U_3^(-1). Fubini and original Haar translation/inversion invariance carry its measure to the Haar measure of Omega and the three retained links. In the quaternion coordinates Omega=q_0 I-i sum q_a sigma_a, the four second moments are equal and their sum is one; hence int q_0^2=1/4. Since tr(Omega)=2q_0, its squared Haar norm is exactly one. Thus

    P_H W_p=0,   <W_p,W_q>_H=delta_pq.                       (A34)

The map U:C plus Q_H H_phys -> H_phys, U(c,h)=c*1+h, has inverse (P_H f,Q_H f) and preserves the original pairing |c|^2+<h,h>_H. In this exact decomposition put

    V_x=-sum_p x_p W_p,
    W_x=Q_H V_x i,   Z_x=i* V_x Q_H,
    D_x=Q_H K Q_H+Q_H V_x Q_H,
    i:C->H_phys, i(c)=c*1,  i*f=P_H f.                      (A35)

Its block matrix is [[0,Z_x],[W_x,D_x]], with original domain C plus (H^2_phys intersect Q_H H_phys). Both original off-diagonal norms satisfy

    ||W_x||=||Z_x||=(sum_p |x_p|^2)^(1/2)<=||x||_1.          (A36)

For the row this follows by applying the original adjoint to 1: V_x*1=-sum_p conjugate(x_p)W_p. Thus A36 holds for the complex sources used by the Cauchy integrals, as well as for real parameters.

Fix 0<rho<3/4 and ||x||_1<=rho. The already constructed analytic ground eigenvalue obeys |e(x)|<=2rho by the original resolvent factorization. Since 3-2rho-|e|>=3-4rho>0, the same factorization on the full Q_H block gives

    ||(D_x-e)^(-1)||<=1/(3-2rho-|e|).                       (A37)

The eigenvector's P_H component is nonzero: otherwise it would be a kernel vector of the invertible D_x-e. Solving the second block and substituting in the first therefore proves the literal scalar relation

    e(x)=-Z_x(D_x-e(x))^(-1)W_x.                            (A38)

Every physical Q_H direction remains in this inverse. Equations A36–A38 give

    |e|(3-2rho-|e|)<=rho^2.                                 (A39)

The two roots of t(3-2rho-t)=rho^2 are

    h_-(rho)=(3-2rho-sqrt(9-12rho))/2,
    h_+(rho)=(3-2rho+sqrt(9-12rho))/2.                       (A40)

Along the actual path x -> s*x, 0<=s<=1, the same fixed-rho estimate holds and |e(s*x)| is continuous, starting at zero. The interval (h_-,h_+) is excluded by A39. It follows that

    |e(x)|<=h_-(rho) on ||x||_1<=rho<3/4.                   (A41)

This is a proved bound on the original analytic branch, not a supplied spectral assumption. At the explicit value rho=20/27, the two roots are 16/27 and 25/27. Hence

    |e(x)|<=16/27 on ||x||_1<=20/27.                        (A42)

For real sources in this ball, the original min-max gap is at least 3-4rho=1/27, so the branch remains the actual simple physical ground energy. The positive-source example below lies far inside this finite-volume region.

The following Cauchy radii keep the same original parameter coordinates:

    R_*=20/(27M),
    r_*=16/(27M),   a_*=2/27,
    M r_*+2a_*=20/27.                                       (A43)

Using A42 on the original homogeneous line improves the complete energy tail to

    |E0,L-kappa[2Mxi+sum_(j=1)^4 e_(2j),L xi^(2j)]|
      <=(16kappa/27)(|xi|/R_*)^10/[1-(|xi|/R_*)^2].         (A44)

Using the two original source circles of radius a_* gives

    |mathcal R_pq(z*1)|<=(16/27)/(2a_*^2)=54,
       |z|<=r_*,                                           (A45)

and the full response remainder is consequently

    |mathcal R_pq(xi)-sum_(j=0)^3 xi^(2j)(R_(2j))_pq|
      <=54(|xi|/r_*)^8/[1-(|xi|/r_*)^2].                    (A46)

Every inequality retains M and kappa. The earlier A8 and A16 remain valid independent bounds; A44 and A46 use the additional exact off-diagonal information A34.

The choice in A43 has an explicit optimality statement within this family of first-omitted-coefficient estimates. For fixed rho, with M r+2a=rho, the product a^2 r^8 is maximized at M r=4rho/5 and a=rho/10, by differentiation of 2log a+8log r. The constant to minimize is then h_-(rho)/rho^10 times the fixed factors 50(5M/4)^8. Introduce gamma=sqrt(9-12rho), with inverse rho=(9-gamma^2)/12. Direct substitution gives

    h_-(rho)/rho^10
      =12^9/[(3-gamma)^8(3+gamma)^10], 0<gamma<3.            (A47)

The logarithm of the denominator has derivative -8/(3-gamma)+10/(3+gamma) and strictly negative second derivative. Its unique maximum is at gamma=1/3, which gives rho=20/27. This optimizes the leading coefficient constant inside the displayed Cauchy family. The geometric tail factor in A46 is retained separately, rather than assigned the same optimization claim.

For the actual two-spacing faces A20, take the larger source and its original physical parameters

    xi=1/10^14,  g^2=5000000,  kappa=10000000/a,
    L=2, M=240, R_*=1/324, r_*=1/405.                      (A48)

Set E_*=54(405xi)^8/[1-(405xi)^2]. Inserting the complete calculated coefficient A21 into A46 gives the exact rational interval

    42744/10^10 < mathcal R_pq(xi)/xi^6 < 120919/10^10.       (A49)

The exact unrounded endpoints are stored in `generated/schur_remainder.json`. They are approximately 4.2744258723*10^(-6) and 1.2091854794*10^(-5). The original integrated connected correlation therefore lies strictly between the two bounds in A49 multiplied by xi^6/kappa. The same positivity holds for every smaller positive xi on this same finite graph, because E_*/xi^6 is increasing with xi in (0,r_*). The squared coupling in A48 is one hundredth of the earlier conservative example A22; the Hamiltonian, lattice spacing variable, and physical time are unchanged.

Finally, the improved scalar coefficient bound returns to the original plaquette readout A30. With t_*=|xi|/R_*, its uncomputed terms after xi^7 obey

    |tail in A32|
      <=(2/5)t_*^9(10-8t_*^2)/(1-t_*^2)^2.                 (A50)

The factor 2/5 is exactly (16/27)/(2M R_*). Thus the derivative estimate retains both the original readout factor 1/(2M) and the actual M-dependent analytic radius.

## A11. Retaining the exact source Gram enlarges the analytic domain

Equation A36 is an equality before its final l1 bound. Retaining it gives an additional independent estimate, including outside the original l1 ball of radius 3/4. For the original complex source define

    rho=||x||_1,  sigma=||x||_2,  d=3-2rho.

Consider the explicit open domain

    D={x: ||x||_1+||x||_2<3/2}.                             (A51)

On any fixed closed source set with ||x||_1<=rho0, ||x||_2^2<=eta0 and 4eta0<(3-2rho0)^2, put d0=3-2rho0>0. In the original blocks A35, the contour |z|=d0/2 has

    ||(D_x-z)^(-1)||<=2/d0,
    |Z_x(D_x-z)^(-1)W_x|<=2eta0/d0<|z|.                    (A52)

The first bound follows from K on Q_H being at least three and ||Q_H V_x Q_H||<=2rho0. The second uses the actual row and column norms sigma, including the conjugate coefficients in the row adjoint. The original block elimination therefore makes the full resolvent invertible on that contour. Along s*x, 0<=s<=1, the same bounds hold. Its contour projection has constant rank one, equal to the original constant projection at zero. This constructs an analytic simple branch on each such source set, without assuming a physical gap. The local branches agree on overlaps: their circles are concentric, each encloses exactly one eigenvalue, and the smaller circle's eigenvalue must also be the larger one's single eigenvalue. They give the same analytic branch throughout A51.

The selected eigenvalue satisfies |e|<d0/2. Applying the exact A38 to it now gives |e|(d0-|e|)<=eta0. The function t(d0-t) is strictly increasing on [0,d0/2], so

    |e(x)|<=h(d0,eta0):=(d0-sqrt(d0^2-4eta0))/2.            (A53)

In particular one may take the actual source norms by a limiting choice of the closed bounds. This proves |e(x)|<=h(3-2||x||_1,||x||_2^2) on A51. Every Q_H direction and every original plaquette remains in D_x; A52 estimates its full inverse.

For real sources, Q_H(K+V_x)Q_H>=d0. The original variational characterization with the one-dimensional excluded subspace span{1} gives lambda_1(K+V_x)>=d0. Its actual ground energy is at most <1,(K+V_x)1>=0. Thus the selected branch is that ground energy and

    gap(H(x))>=kappa d0.                                   (A54)

This is a finite-source estimate in the original physical space. On the homogeneous line its analytic domain is |xi|(M+sqrt(M))<3/2. It is not assigned a volume-independent xi radius. The min-max step and the analytic contour have their separate displayed source domains.

The two-source Cauchy calculation can retain this Gram instead of bounding it by rho0^2. For p!=q and |z|<=r, |u|,|w|<=a, the original source x=z*1+u e_p+w e_q obeys

    ||x||_1<=M r+2a=:rho0,
    ||x||_2^2<=M r^2+4ra+2a^2=:eta_distinct.                (A55)

Indeed the exact squared norm is M|z|^2+2Re(conjugate(z)(u+w))+|u|^2+|w|^2. For p=q its last two source terms combine, and the retained upper bound is instead

    eta_same=M r^2+4ra+4a^2.                                (A56)

There is no identification of the two source Grams. Their two inverse cases are the original distinct- and same-coordinate insertions. A53 and the Cauchy formula give respectively the response-circle constants h(d0,eta_distinct)/(2a^2) and h(d0,eta_same)/(2a^2), whenever the displayed closed-source inequalities in A52 hold. These apply to the actual original source polydiscs just constructed, and retain the full geometric tail on returning to xi.

For every original L>=2, M>=240. Choose the explicit common radii

    rho0=1,  d0=1,  r_**=6/(7M),  a_**=1/14.

Their original source budgets and Gram estimates are

    M r_**+2a_**=1,
    eta_distinct=48/(49M)+1/98<=1/70,
    eta_same=48/(49M)+1/49<=6/245.                           (A57)

Both satisfy 4eta<1. Direct rational multiplication gives

    (1/68)(1-1/68)>1/70,
    (1/39)(1-1/39)>6/245,
    1/68<1/2, 1/39<1/2.

Thus the exact smaller-root comparison A53 and the original two-source derivative give

    |R_pq(z*1)|<=49/34   for p!=q,
    |R_pp(z*1)|<=98/39,
    |z|<=6/(7M).                                           (A58)

The first constant is (1/68)/(2a_**^2); the second is (1/39)/(2a_**^2). These are two proved full-operator circle bounds, not replacements of an original norm by a chosen coefficient metric. The earlier optimized family A47 retained only the l1 source bound; A55–A58 use additional information from the exact original Haar Gram.

By the same exact source parity and Cauchy sum as A16, for distinct p,q the complete response tail after degree six is now

    |R_pq(xi)-sum_(j=0)^3 xi^(2j)(R_(2j))_pq|
       <=(49/34)(|xi|/r_**)^8/[1-(|xi|/r_**)^2].            (A59)

For a diagonal entry use 98/39. The complete quadratic-form error is bounded using the larger of the two constants and the original sum of coefficient absolute values, with all mixed entries retained.

For the original two-spacing faces A20 in the complete L=2 box, set

    xi=1/(4*10^12),  g^2=1000000,
    kappa=2000000/a,  a>0,  r_**=1/280.                     (A60)

The source equation xi=1/(4g^4) is exact. Let E_**=(49/34)(280xi)^8/[1-(280xi)^2]. The full coefficient A21 and A59 yield the rational interval

    47801/10^10 < R_pq(xi)/xi^6 <115862/10^10.               (A61)

The unrounded endpoints are approximately 4.7801443923*10^(-6) and 1.1586136274*10^(-5). Multiplication by xi^6/kappa returns the strict positive bounds on the original integrated connected correlation. This is a certificate of the complete finite-volume quantity. Its coupling, spacing, all 240 original plaquettes, and full spin spectrum remain. It supplies no pointwise-in-time positivity or volume-uniform analytic radius.

The same original-Gram calculation also sharpens the homogeneous energy circle. For |z|<=1/M, one has ||z*1||_1<=1 and ||z*1||_2^2<=1/M. Since M>=240, the full A52 contour applies. Moreover (2/M)(1-2/M)>=1/M and 2/M<1/2, so A53 gives |e(z*1)|<=2/M. Consequently the complete physical energy tail after degree eight satisfies

    |E0,L-kappa[2Mxi+sum_(j=1)^4 e_(2j),L xi^(2j)]|
      <=(2kappa/M)(M|xi|)^10/[1-(M|xi|)^2],  |xi|<1/M.     (A62)

The corresponding original average-half-trace tail after degree seven is at most

    (1/M)t^9(10-8t^2)/(1-t^2)^2,  t=M|xi|<1.              (A63)

The factor 1/M is exactly (2/M)/(2M*(1/M)), from the original readout derivative. The constant could also retain the exact smaller root h(1,1/M); A62–A63 use its displayed rational upper bound. The physical and volume factors have not been removed.

## A12. A two-sided native-energy bound for the full original plaquette family

The same circle also returns a quantitative bound for the entire 240-dimensional original observation family at a much wider real coupling range than the small off-diagonal sign certificate. Retain the complete original L=2 face order in `response6_L2.json` and the inherited degree-zero-through-four matrix. Their face arrays are exactly identical. The full absolute row sums give

    ||R_(2)||_2<=227/1404,
    ||R_(4)||_2<=3451329067/14074482240,
    ||R_(6)||_2<=43015053233874982762407882061
                 /130602360760562331009008640000.            (A64)

Here the norm is on the fixed original coefficient space C^240 with its counting pairing. Every row sum and every maximizing original face index is stored in `generated/native_response.json`. To justify the bound without a matrix-frame change, Hermiticity and 2|c_i c_j|<=|c_i|^2+|c_j|^2 give

    |sum_(i,j) conjugate(c_i) A_ij c_j|
       <=max_i sum_j |A_ij| * sum_i |c_i|^2.

Every original matrix cross term remains in this inequality.

For the complete tail matrix, A58--A59 give the absolute-row bound

    B_tail(xi)=[98/39+239*(49/34)]
                  * (280xi)^8/[1-(280xi)^2].                (A65)

The diagonal and off-diagonal constants have not been interchanged. At xi0=1/784, corresponding to the original g^2=14, exact rational calculation proves

    (227/1404)xi0^2+(3451329067/14074482240)xi0^4
    +(43015053233874982762407882061
      /130602360760562331009008640000)xi0^6+B_tail(xi0)
       <1/9.                                                (A66)

Every term is increasing on 0<=xi<=xi0. Returning to the complete physical response, for every a>0 and g^2>=14 in this original box,

    (2/9)I_240 < R(xi) < (4/9)I_240.                        (A67)

The inequalities mean positive definite differences in the displayed source-coordinate pairing. They do not replace the actual physical source-state Gram. That original Gram is

    G_pq=<r_p,r_q>,  r_p=(W_p-<W_p>_rho)psi.

The original source-to-state map is c -> r(c)=sum_p c_p r_p, with inverse on its image given by the unique original plaquette coefficient vector. Its injectivity also follows from A67 and R=kappa r* A^(-1)r. There is no replacement of G by I in this statement.

The actual centered logarithmic derivative primitive is

    Z(c)=sum_p c_p[partial_(x_p)v-<partial_(x_p)v>_rho],
    Atilde Z(c)=kappa sum_p c_p(W_p-<W_p>_rho).

Equations A2--A3 return its full energy pairing:

    (2kappa/9)||c||^2
       <q_Atilde(Z(c))<(4kappa/9)||c||^2.                    (A68)

This bound is in the actual interacting-vacuum energy, on the entire original plaquette source image. The coupling domain is g^2>=14 on L=2; no extension of this finite matrix bound to all volumes is asserted.

Its original state norm also has explicit bounds. The constant trial state has zero expectation for K+V_x. The original min-max inequality for its first physical excitation gives, throughout this real source range,

    gap(H_L)>=kappa(3-2Mxi)>=kappa*(117/49).                 (A69)

This follows from K on its nonconstant physical subspace being at least three, ||V_x||<=2Mxi, and the ground energy being at most zero before restoring the scalar. Combining A68 with A69 gives

    ||Z(c)||_rho^2 < (196/1053)||c||^2.                     (A70)

For the lower bound, the actual original source variance satisfies

    ||r(c)||^2
       =Var_rho(sum_p c_p W_p)
       <=4(sum_p|c_p|)^2<=4M||c||^2.

The original pairing is <sum c_p(W_p-<W_p>),Z(c)>_rho=c*R c. Cauchy--Schwarz, with all source coefficients retained, and A67 therefore give

    ||Z(c)||_rho^2 > (1/19440)||c||^2                       (A71)

for nonzero c. Together, in the original plaquette coordinate frame,

    (1/19440)I_240 < Z*Z < (196/1053)I_240,
    (2kappa/9)I_240 < Z*Atilde Z < (4kappa/9)I_240.          (A72)

The adjoints in these formulas use the original rho-Hilbert pairing. The same primitive, its source labels, its energy and its restored state metric thus have two-sided bounds. These are results about a specified finite original observation family inside the full physical Hamiltonian, not a new continuum mass or a removal of the orthogonal physical complement.

## A13. Quantitative support-transition primitives in the same physical space

Retain the original 240 face labels and the same real vacuum at L=2, a>0, g^2>=14. Define the actual coefficient maps into the centered rho-Hilbert space

    Bc=sum_p c_p(W_p-<W_p>_rho),
    Zc=kappa Atilde^(-1)Bc.

They are injective by A67, have their original adjoints, and satisfy Atilde Z=kappa B. For each subset F of the 240 original labels put V_F=Z(C^F) and U_F=B(C^F). Use the actual cochain window

    V_F --(Atilde/kappa)--> U_all --0--> 0.                  (A73)

For F contained in G, the transition is inclusion in degree zero and the identity on U_all. The original operator restriction proves its cochain square. Its first cohomology is U_all/U_F. The exact transported-kernel map and inverse are

    V_G/V_F -> ker(U_all/U_F -> U_all/U_G),
    [h] -> [(Atilde/kappa)h],
    [By] -> [Zy] for y supported in G.                      (A74)

Changing By by an element of U_F changes Zy by its exact image in V_F because B and Z are injective with Atilde Z=kappa B. These statements prove well-definedness, both inverse laws, and the full receiving kernel. Source labels are subsets of the original plaquettes and their join is their union. Applying the original Split Zero reconstruction retains every receiving zero at its support; the physical orthogonal complement is kept below.

Let J=G minus F, in the original face order. The primitive class with remaining coefficient y in C^J has all representatives Z_F z+Z_J y. Its actual energy is the full quadratic form

    kappa*(z,y)* R_GG (z,y),

including R_FJ and R_JF. Since R_FF>(2/9)I, direct differentiation in the original coefficients, or completing this exact quadratic form, gives the unique minimum

    z_min=-R_FF^(-1)R_FJ y,
    Q_(F,G)=kappa[R_JJ-R_JF R_FF^(-1)R_FJ].                 (A75)

Every inverse is on the indicated original nonempty block; for empty F the term involving F has its unique empty value. To bound the quotient, minimize the lower inequality A67 over z; it gives Q_(F,G)>(2kappa/9)I. For the upper bound use the actual lift z=0 in the same fibre and A67. Therefore, on every nonempty receiving kernel,

    (2kappa/9)I_J < Q_(F,G) < (4kappa/9)I_J.                (A76)

For J empty the space and quadratic form are the original zero space and its unique form. No nonzero direction is manufactured there.

The minimum primitive h_y=Z_F z_min+Z_J y also retains its original state norm. A71 and ||(z_min,y)||^2>=||y||^2 give its lower bound. A69 and the upper bound in A76 give its upper bound. Thus

    (1/19440)||y||^2 < ||h_y||_rho^2
                         < (196/1053)||y||^2               (A77)

for y nonzero. These statements control every subset support transition of this actual original observation family. Their energy and state pairings are distinct displayed forms, with the exact map and coefficients A75 connecting their common primitive; neither form is replaced by the other.

The rest of the physical Hilbert space remains explicit. Let G_Z=Z*Z with the bounds A72 and define

    P_Z=Z G_Z^(-1)Z*,  S_Z=G_Z^(-1)Z*.

Multiplication proves P_Z*=P_Z, P_Z^2=P_Z, S_Z Z=I, Z S_Z=P_Z and ker S_Z=im(Z)^perp. For a form-domain h perpendicular to im Z, the full original norm and energy of Zc+h are

    ||Zc+h||_rho^2=c*G_Z c+||h||_rho^2,
    q_Atilde(Zc+h)=kappa c*R c
          +2kappa Re< Bc,h>_rho+q_Atilde(h).                (A78)

The mixed term follows from Atilde Z=kappa B and has not been removed by the state-orthogonal decomposition. In particular the maps above do not presume that im Z is a reducing subspace. The complement and its displayed forcing are retained when this finite source family is used in further physical refinement. The continuum and growing-volume conclusions remain outside the domain of A67–A78.


---

## Retained source: NEXT_CALCULATION.md

# Next original calculation after the completed sixth source

The target remains the interacting four-dimensional continuum Yang–Mills theory and its physical excitation-energy edge. This edition completes the sixth logarithmic coefficient and its forty-thousand original directional identities, the entire eighth energy and the sixth-degree response. A seventh catalogue alone is not used as a progress criterion.

The next selected object is the full residual of the original q6=sum_(i=1)^6 V_i:

    R6=sum_(7<=i+j<=12, 1<=i,j<=6) B(V_i,V_j).

Its first original coefficient is

    v7=2B(v1,v6)+2B(v2,v5)+2B(v3,v4).

Both expressions retain all original ordered support unions and the Haar scalar removed by Q_H. The existing local derivative bounds S34–S37 supply explicit sixth-order entries in the same source. The exact physical defect is

    Q_H Atilde h-kappa K[I-2B(q6,.)]h
        =-2kappa Q_H Gamma(v-q6,h).

The selected work is to calculate the native energy/derivative cost of that residual, its correction and the displayed physical defect with the box, spacing, coupling and actual scalar return retained. Growing source-support and coefficient norms must remain connected by explicit maps, rather than assigning an auxiliary coefficient bound to the physical state norm.

A useful second interface is now A38 and A51–A78: the original Haar off-diagonal block has norm ||x||_2 exactly, while its full Q_H diagonal keeps every interaction. The original source-Gram analytic domain ||x||_1+||x||_2<3/2, its improved finite-volume Cauchy radius 6/(7M), and the actual coefficientwise bulk response are completed results. Their M-dependence is the next scaling quantity to analyze, not an omitted factor. The direct first- and second-derivative bounds for v_[6] are volume-independent coefficients only; their uncomputed all-order return remains explicit.

The standing path is still a_n=a0*2^(-n), g_n^2=(g0^(-2)+beta*n*log2)^(-1). No new result in this edition is assigned to that full path. Earlier uniform-gap manuscripts retain the independent report's audit qualification. New estimates should be derived or reviewed on their full stated domain before using them in the continuum calculation.

The cumulative source, current exact data and replay scopes are authoritative for continuation. Refresh the actual peer source and PR snapshots before importing another session's theorem. The present peer README/PR intake is orientation-only, not an independent audit or a transferred arithmetic constant. Leave another additive cumulative checkpoint after the next completed calculation.


---

# New complete source: PHYSICAL_HEAT_COEFFICIENTS.md

# Original Yang–Mills heat correlations: the complete fourth-degree return

21 September 2026. This is an additive continuation of the recovered cumulative
workbench. The original open-box SU(2) operator, physical units, Haar measure,
gauge constraints and source coordinates remain. The coefficient calculation
uses the complete available fifth-source archive. The separately saved sixth-source
proofs are preserved with their recovery status; their missing catalogues are
not prerequisites for this calculation. General exponential-vacuum and character
methods retain Schütte–Zheng–Hamer (1996) as a human antecedent. The exact finite
calculations here are accompanied by analytic proofs and executable audits;
independent external analytical review and historical priority are not asserted.

## H1. The actual operator and time coordinate

For L>=2 use every vertex n in {-L,...,L}^3, every contained positive edge
(n,i), and every contained elementary face p=(n;i,j), i<j. Put

    W_p=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)),
    T_alpha=-i sigma_alpha/2,
    X_e,alpha f=d/ds f(...,exp(s T_alpha)U_e,...) at s=0,
    K=-sum_(e,alpha) X_e,alpha^2,
    H(x)=kappa K+kappa sum_p x_p(2-W_p),
    kappa=2g^2/a,   x_p=xi=1/(4g^4) on the homogeneous line.       (H1)

The inner product on the original product Haar probability space is conjugate
linear in its first entry. The physical subspace is invariant under all vertex
gauge transformations, including boundary vertices. The domains are the physical
parts of H^2 and H^1. The original bounded smooth potential preserves these
domains; the compact elliptic operator has a smooth strictly positive unit
ground state psi_x with energy E0(x). These domain and vacuum facts are the
ones in the pinned original finite-box source (SOURCE_INTAKE.json, YM0).

The coefficient operator and its inverse physical return are exactly

    B_x=(H(x)-2kappa sum_p x_p I)/kappa=K-sum_p x_p W_p,
    H(x)=kappa B_x+2kappa sum_p x_p I,
    E0(x)=kappa[2sum_p x_p+e(x)].                              (H2)

Both scalar energy terms remain in the return. Let A_x=H(x)-E0(x) and
r_p=(W_p-<W_p>_rho)psi_x, rho=psi_x^2. Define

    C_pq(t;x)=<r_p,exp(-t A_x)r_q>,
    Chat_pq(tau;x)=C_pq(tau/kappa;x),
    tau=kappa t,   t=tau/kappa.                              (H3)

This is an invertible physical-time change; no link or field coordinate is
changed. The Laplace variable z below is conjugate to this stated tau:

    F_pq(z;x)=int_0^infinity exp(-z tau) Chat_pq(tau;x) dtau
             =kappa <r_p,(A_x+kappa z)^(-1)r_q>.              (H4)

All expressions are initially at real sufficiently small x and z>0. The
separate analytic proof gives their full domains and uniform time remainders.

## H2. The complete coefficient recurrence, including the ground pole

Retain the source section u=psi_x/m_x, m_x=P_H psi_x. Its inverse is
psi_x=m_x u, and its original scalar obeys m_x^2<u,u>_H=1. Thus P_H u=1
and the original norm N(x)=<u,u>_H is kept in every expectation. Expand
u(x)=sum_nu u_nu x^nu, e(x)=sum_(nu!=0)e_nu x^nu, with u_0=1,
P_H u_nu=0 for nu!=0. The exact eigen-equation gives

    e_nu=-sum_(j:nu_j>0) P_H(W_j u_(nu-e_j)),
    K u_nu=sum_j W_j u_(nu-e_j)
              +sum_(0<mu<=nu)e_mu u_(nu-mu).                 (H5)

The last term includes e_nu u_0, and its Haar scalar makes the RHS centered.
Its unique centered inverse is the original K^(-1)Q_H. The recovered coefficient
engine supplies these actual finite coefficients and all their source labels.

For a marked face q, define h_q(z;x)=(B_x-e(x)+z)^(-1)W_q u(x).
Its coefficient equation is

    (K+z)h_(q,nu)=W_q u_nu+sum_j W_j h_(q,nu-e_j)
                         +sum_(0<mu<=nu)e_mu h_(q,nu-mu).     (H6)

The source index may include repeated faces; all multiplicities remain literal
multiindex coefficients. Define

    N_nu=sum_(alpha+beta=nu)<u_alpha,u_beta>_H,
    Mp_nu=sum_(alpha+beta=nu)<u_alpha,W_p u_beta>_H,
    Hpq_nu=sum_(alpha+beta=nu)<u_alpha,W_p h_(q,beta)>_H.        (H7)

Coefficient division by N, with N_0=1, gives the original mean mu_p=Mp/N
and the uncentered resolvent Hpq/N. The complete connected answer is

    F_pq=Hpq/N-mu_p mu_q/z.                                  (H8)

The subtracted term is retained as an actual ground-state contribution. The
source shift e_mu in (H6), both norm divisions and this term are all required.
Every resulting coefficient in the catalogue has zero coefficient at each
power z^(-j), j>0. The original positive free excitation gap also proves this
cancellation analytically near (x,z)=(0,0), after the ground projection is removed.

## H3. Exact original Casimir inversion and time reconstruction

An original invariant trace monomial has a finite tensor representation on its
original edge set. For r_e occurrences on edge e, the allowed doubled spins are
r_e,r_e-2,... . At each original vertex the sum of the doubled spins is even,
and no one exceeds the sum of the others. These are the SU(2) invariant-tensor
conditions: iterated angular-momentum addition supplies every intermediate spin
in the parity-compatible interval, so zero belongs exactly on those conditions.
The resulting finite Casimir list contains all eigenvalues of that monomial.
It retains multiplicities inside every equal-eigenvalue eigenspace.

For its distinct values C, use the literal original operator projectors

    P_c=product_(d in C,d!=c)(K-dI)/(c-d),
    (K+z)^(-1)f=sum_(c in C) P_c f/(z+c).                     (H9)

The full physical operator has all spins. The finite list in (H9) is the complete
representation space reached by that Taylor coefficient and its marked word.
It does not discard a path contributing to the coefficient.

Every response coefficient is stored as exact partial fractions

    F_nu(z)=sum_(c>0,n>=1) a_(c,n)/(z+c)^n.                   (H10)

Their time functions are exactly

    Chat_nu(tau)=sum_(c,n) a_(c,n) tau^(n-1)exp(-c tau)/(n-1)!.(H11)

Indeed direct integration of each finite term gives (H10). The analytic
heat construction in the companion proof shows these are the actual Taylor
coefficients, and uniqueness of the Laplace transform identifies them.
For explicit uniqueness, weighting a vanishing transform by exp(-s0 tau)
produces a finite complex measure; x=exp(-tau) carries its integer Laplace
samples to all polynomial moments on [0,1]. Polynomial approximation forces
the measure to vanish; continuity gives equality of the time functions.

Products in the partial-fraction engine are also exact. For a!=b, the principal
part of (z+a)^(-m)(z+b)^(-n) at -a has coefficients

    (-1)^k binom(n+k-1,k)/(b-a)^(n+k),  k=0,...,m-1,          (H12)

at power (z+a)^(-(m-k)); the analogous -b principal part is retained. Their
sum has the same two principal parts and vanishes at infinity, so the rational
functions are equal. Coincident poles add their orders. This retains every
repeated pole and hence every time-polynomial factor in (H11).

The exact original source equation (H6) is audited as a complete polynomial in
all retained tree/chord quaternion coordinates, separately for every pole.
The map is Z_e=t_s U_e t_t^(-1), with its original inverse
U_e=t_s^(-1)Z_e t_t and the tree variables retained. On each chord,
Z=x0 I-i sum x_a sigma_a and sum_(a=0)^3 x_a^2=1. The remainder basis has
x0 exponent zero or one. The map and injectivity argument are the recovered
fifth-source coordinate proof, unchanged. Every residual coefficient is zero
in this full product-of-spheres algebra, not merely at sampled links.

## H4. Complete support classification and original box assembly

A change U_e -> -U_e multiplies each source or marked trace using e by -1.
Thus a nonzero coefficient has an even total multiplicity on every original
edge, counting both marked traces. At total face multiplicity 2 or 4 this
requires all face multiplicities even. At total multiplicity 6 it permits,
in addition, the six distinct faces of one elementary cube. The original
closed cubical two-chain argument is retained in the sixth-energy proof:
a nonempty closed mod-two face set has at least six faces; at six, each of
the four edges of an extreme face requires its adjacent side face, and closure
of their remaining edges forces the opposite face. The resulting set is the
boundary of that original cube.

A disconnected face source factors over disjoint original edge factors. The
original operators, positive vacua and their means factor accordingly. A source
component containing neither mark cancels between numerator and N; marks in
different components have zero connected correlation. This remains true with
shared graph vertices: the full tensor-product Hamiltonian and the actual
invariant vectors give the same physical expectation. Connectedness therefore
means sharing original edges, exactly as in the source catalogue.

The complete list is:

| heat/source degree | total face multiplicity including marks | coordinate cases | marked responses |
|---|---|---:|---:|
| 0 | 2 | 1 | 1 |
| 2 | 4 | 3 | 7 |
| 4 | 6 | 13 | 76 |

There are 84 full rational time functions. At total degree six the cases are
one single face, two geometries of an ordered 4+2 pair, seven geometries of a
three-face path, one common-edge triple, one cube corner and one cube. All marks
and all allowed diagonal marks are retained. Faces with repeated multiplicity
are never replaced by a factorial convention.

A signed coordinate permutation and translation

    y_i=epsilon_i x_(pi(i))-d_i,
    x_(pi(i))=epsilon_i(y_i+d_i)                              (H13)

transports every actual face multiset and both marked faces to its record.
Each original edge is mapped to the corresponding forward or inverse edge.
The product-Haar map is unitary, carries K to K on that support, and maps the
actual face words to the target face word or its inverse. In SU(2), tr(U^-1)=tr(U)
by the two eigenvalues lambda,lambda^-1; hence the same trace is returned.
The inverse in (H13) returns every source to its original coordinates.

The L=2 assembly retains all 240 original faces, 1,128 adjacent pairs, 6,732
paths, 576 common-edge triples, 512 corners and 64 cubes. The coefficient
matrices have respectively 240, 2,496 and 9,660 nonzero entries. Their entire
time integrals agree entry by entry with the preceding static matrices:

    int_0^infinity Chat_0(tau)dtau=I/3,
    int_0^infinity Chat_2(tau)dtau
      =-(5/36)I+(2/1053)D_degree+(4/1053)A_adj,                (H14)

and the full original Chat_4 integral is the previously calculated R4,
including every boundary row and cube. All complete matrices and all their
coordinate transports are in generated/heat_matrix_L2.json and
heat_transports_L2.json. Those files preserve the original face ordering.

## H5. Explicit time-dependent functions

For one original plaquette with only its own source parameter, the degree-two
coefficient is

    exp(-3tau)[-241/900-(7/15)tau]+(4/225)exp(-8tau).          (H15)

For two different faces sharing one original edge, the coefficient of x_p x_q is

    exp(-3tau)[-409/17199+tau/21]
       +exp(-9tau/2)/36+exp(-13tau/2)/588.                    (H16)

Its integral is 4/1053 and its value at zero is 2/351. The corresponding
diagonal, neighbour-source term replaces -409/17199 by -13/441; its integral
is 2/1053 and its time-zero value is zero. These distinct values retain the
full source and state pairings.

Now take opposite faces

    p=(0,0,0;0,1),  q=(0,0,1;0,1).                          (H17)

Their coefficients at degrees zero and two vanish. Four original three-face
paths and one original cube contribute at degree four. One path gives

    P(tau)=exp(-3tau)[75173779/67612708800
                     -(4441/3611790)tau+tau^2/882]
       -(121/108864)exp(-9tau/2)+(1/11664)exp(-6tau)
       -(197/9988160)exp(-13tau/2)+(1/163800)exp(-8tau)
       +(1/6492304)exp(-10tau).                              (H18)

The cube gives

    B(tau)=exp(-3tau)[-235/648+(10/27)tau]
       +exp(-9tau/2)[1123/2916+(23/81)tau+tau^2/18]
       +(1/648)exp(-6tau).                                  (H19)

Thus the complete actual degree-four coefficient is

    h_4(tau)=4P(tau)+B(tau),
    h_4(0)=8869/365040,
    int_0^infinity h_4(tau)dtau=641033/29568240.               (H20)

All six decay rates and both repeated-pole orders remain. The coefficient
at tau=1 is enclosed by rational exponential bounds in generated/heat_bounds.json;
its numerical size is approximately 0.00859150755. This diagnostic decimal is
not an acceptance test. The companion proof turns (H20) into intervals for the
full actual correlation, retaining every higher Taylor order.

## H6. Independent checks on the same original geometry

The single-plaquette check uses the infinite original character basis chi_(j/2),
where K chi_(j/2)=j(j+2)chi_(j/2) and
W chi_(j/2)=chi_((j-1)/2)+chi_((j+1)/2), with the negative-index term zero.
At order n every contributing insertion path has j<=n+1; the independent
recurrence retains all these indices. It reproduces all three self-source
heat coefficients, with both original norm divisions and the ground pole.
Its integrated coefficients are 1/3,-5/36,289/5184. They also follow by twice
differentiating the retained one-plaquette energy coefficients. The original
radial coordinate return e_one(xi)=b_2(-4xi)/4-1 matches the NIST DLMF 28.6.5
expansion; the map and scalar energy term are in the recovered audit report.
This comparison covers that one-plaquette coefficient convention only.

There is an additional computation for every marked cube pair. Orient the six
faces outward. Original Haar integration yields 2^8/2^12=1/16. For any proper
visited face subset S, each edge already visited twice can never occur in a
later insertion. Its surviving representation is the original spin zero; each
boundary edge carries the remaining spin one-half. Therefore its original
intermediate energy is c(S)=3|boundary S|/4.

For marks p!=q, arrange the other four faces in a permutation and split the
ordered list into right-vacuum, middle-heat and left-vacuum pieces. All 24
permutations and all 15 length triples occur. Right and left vacuum prefixes
contribute 1/c(S); the middle heat state begins at {q} union right and each
middle insertion contributes 1/[z+c(S)]. The original 1/16 remains. Summing
these 360 rational functions gives exactly the cube coefficient in (H10).
All fifteen marked cube pairs were checked: 5,400 complete original insertion
records, including every intermediate boundary energy. This calculation imports
none of the trace-differentiation or Casimir-projection engine.

The time-zero covariance, its first derivative -<Gamma(W_p,W_q)>_rho,
and its second derivative <[K,W_p]u,[K,W_q]u>_H/N are also calculated separately
from the entire original density quotient at each coefficient. All 84 rational
functions reproduce these three values. The full-polynomial source audit and
these moment identities have distinct execution records.

## H7. Sources and present mathematical scope

The original operator/domain and maximal-tree maps are the pinned finite-box
workbench source. The exponential and character/Casimir antecedent is
D. Schütte, Zheng Weihong and C. J. Hamer, arXiv:hep-lat/9603026. The residue
and minimum-section comparison imported from the current Split-Zero heat
work is specified completely in RH_HEAT_TRANSFER.md, with its exact source
revision and read equations. No arithmetic period or Gamma constant is
assigned to a physical Yang–Mills matrix.

These are actual finite-regulator heat coefficients and actual finite-volume
analytic bounds. The Cauchy radius in the companion is 1/M. It therefore
retains dependence on the original volume, and does not supply an ultraviolet
continuum construction. The earlier uniform-gap manuscripts retain their
recorded independent-audit qualification.

## H8. The complete fourth-order first-band return in its original metric

The original free energy-three space is exactly span{Wp}. To see the next
separation, an active invariant graph with four edges is a four-cycle; its
vertex intertwiners force equal edge spins, giving energy 4j(j+1)=3,8,... .
A simple bipartite active graph with five edges and minimum degree at least two
would have one cyclic component with five vertices and five edges, hence an
odd five-cycle, or at most four vertices, where bipartiteness permits at most
four edges. Both cases contradict its assumptions. Therefore any other active
assignment has at least six edges and energy >=9/2. Thus

    spec(K_phys) subset {0,3} union [9/2,infinity),
    P3H_phys=span{Wp},   dim P3=M.                           (H21)

For sufficiently small real xi let Pi_xi be the complete spectral projection
near energy 3 of B_xi-e(xi), and put

    Y_xi c=Pi_xi sum_p c_p r_p,
    Gband=Y_xi*Y_xi,
    (B_xi-e)Y_xi=Y_xi Aband.                                (H22)

The exact quantitative construction below proves invertibility of this frame
onto the actual band. At xi=0, c->sum c_p Wp is the original Haar isometry R0.
Projection of the heat resolvent onto its original energy-three poles gives

    Cband(tau)=Gband exp(-tau Aband),
    Gband=I+xi^2 G2+xi^4 G4+...,
    Aband=3I+xi^2 T2+xi^4 T4+....                            (H23)

The original center symmetry makes both matrices even. For each of the full
heat matrices let A_(n,j) be the coefficient of (z+3)^(-j). Then literal
multiplication of the two series in (H23) proves

    G2=A_(2,1),  G4=A_(4,1),  T2=-A_(2,2),
    A_(4,3)=T2^2,
    T4=-A_(4,2)-G2 T2.                                    (H24)

All matrix factors retain their order. The complete L=2 calculation gives

    T2=(7/15)I-(D_degree+A_adj)/21.                          (H25)

It gives all 9,660 nonzero entries of T4 and all 9,660 entries of G4 in
first_band_L2.json. Every entry of A_(4,3)=T2^2 is checked. Original
self-adjointness returns through the full Gram as

    Gband Aband=Aband* Gband,
    T4-T4* = T2 G2-G2 T2.                                  (H26)

The right side has 1,440 nonzero entries for this open box. For the original
faces (-2,-2,-2;0,1) and (-2,-1,-2;0,1), the displayed difference is exactly
2/7371. This is the explicit correction between the coordinate adjoint and the
original metric adjoint. Its value is retained, rather than forcing a symmetric
coefficient matrix by dropping the mixed product.

Here is a complete analytic remainder for (H23). Work on the complex
homogeneous circle |zeta|=1/(32M). The original ground/complement calculation
in A1--A2 applies with ||W||^2=eta=1/(1024M) and Re D>=47/16. On |e|=eta,
||Z(D-e)^(-1)W||<eta, so the same scalar argument principle gives |e|<=eta.
Consequently

    ||B_zeta-e-K|| <=1/16+1/(1024M)<1/15.                    (H27)

On the spectral circle |lambda-3|=1/2 the original free resolvent has norm
at most 2. Its norm-convergent resolvent series gives

    ||Pi-P3|| <=2/13,
    ||(B_zeta-e-3)Pi||<=1/13.                               (H28)

For the first inequality, integrate the difference of resolvents: the bound
is 2b/(1-2b) with b<=1/15. For the second, integrate that difference multiplied
by lambda-3, obtaining b/(1-2b). The corresponding free integral is zero
because (K-3)P3=0. The circle encloses exactly the original M-dimensional
band, by the same resolvent homotopy and finite rank at zero.

Use the exact Haar section u=1+w, where ||w||<=1/(92sqrt(M)); the denominator
in its block inverse exceeds 23/8. The column map Fu:c->sum c_p Wp u satisfies

    ||Fu-R0||<=2sqrt(M)||w||<=1/46.

Define Yhat=Pi Fu. Its original coefficient map obeys

    ||R0*Yhat-I||<=107/598,
    ||(R0*Yhat)^(-1)||<=598/491.                             (H29)

Indeed the two contributions are Pi-P3 and Pi(Fu-R0), bounded by 2/13 and
(15/13)/46. Its inverse on the band is (R0*Yhat)^(-1)R0*. The actual unit-vacuum
frame is Y=m Yhat, with psi=m u and m^2<u,u>_H=1 retained. Its scalar cancels
from the operator intertwining, not from Gband. Thus

    Aband=(R0*Yhat)^(-1)R0*(B_zeta-e)Yhat,
    ||Aband-3I|| <=(598/491)(1/13)(47/46)=47/491.             (H30)

All these maps are analytic on a neighborhood of the closed source circle.
The original center involution sends Yhat_-zeta=-C Yhat_zeta and R0*C=-R0*,
so Aband is even. Cauchy's formula and the full even tail prove

    ||Aband-3I-xi^2T2-xi^4T4||
      <=(47/491)(32M|xi|)^6/[1-(32M|xi|)^2],
                         |xi|<1/(32M).                    (H31)

Multiplication by kappa returns this to physical energy. This is an actual
finite-volume matrix remainder, with all original band coordinates, the
nonidentity Gram (H23), and the dependence on M retained. No diagonalization
of T4 or uniform-in-volume fourth-order spectral claim is inferred here.


---

# New complete source: HEAT_REMAINDER_AND_NATIVE_METRICS.md

# Full-time heat bounds and the original plaquette response metrics

21 September 2026. This proof uses the unchanged finite-box SU(2) Hamiltonian
and the complete coefficients in PHYSICAL_HEAT_COEFFICIENTS.md. Its analytic
argument is finite-volume and independent of the inherited volume-uniform
source-norm estimates. The original number M of plaquettes appears in every
Cauchy radius. Written arguments and executed finite checks have separate
records. All inner products are conjugate-linear in the first entry.

## A1. Original free spectrum and Haar blocks

Use H1--H3 of the coefficient proof. The original physical free operator K has
its constant eigenvector 1, and every other physical Fourier block has energy
at least 3. Here is the graph argument. In a nonzero invariant representation
assignment, a vertex incident to only one active edge has no invariant tensor.
Thus the finite active graph has minimum degree at least two and contains a
cycle. The original simple cubic graph has no triangles and every cycle has at
least four edges. Each active edge has spin j>=1/2 and Casimir j(j+1)>=3/4.
Hence the complete physical K on the orthogonal complement of 1 is >=3.
The elementary plaquette trace has four spin-one-half edges and energy 3.

Write P0=|1><1| and Q0=I-P0 in the original product Haar space. Integrating
one original link gives P0 Wp=0. Two distinct elementary plaquettes have an
edge occurring in just one of their two words; integration over that link
vanishes. For p=q, the product holonomy has the original Haar law and the
fundamental character has squared norm one. Therefore

    <Wp,Wq>_H=delta_pq.                                      (A1)

For the complex homogeneous coefficient zeta, x_p=zeta, put B_zeta=K-zeta S.
This complex variable retains the physical return H= kappa B_xi+2kappa M xi I
at real xi. On C1 plus Q0 H_phys the full original block operator is

    B_zeta = [[0,Z],[W,D]],
    D=Q0(K-zeta S)Q0 on Dom(K) intersect Q0 H_phys,
    W=-zeta sum_p Wp,   Z=-zeta P0 S Q0.                     (A2)

Z is the original complex-linear row, with no conjugation of its parameter
in the analytic extension. Equation (A1) proves exactly

    ||W||=||Z||=sqrt(M)|zeta|.

On |zeta|<=1/M, Re<Dh,h> >= ||h||^2 since ||zeta S||<=2.
The closed operator D is a bounded perturbation of Q0KQ0 on the same domain.
For Re e<1 its inverse D-e exists with norm <=(1-Re e)^(-1): injectivity and
closed range follow from the real part inequality; the same inequality for
its adjoint gives dense range, hence surjectivity. All finite boxes here have
M=3(2L)^2(2L+1)>=240.

## A2. A complete ground/complement decomposition on the complex disk

The scalar equation for the small eigenvalue is

    f(e)=e+Z(D-e)^(-1)W=0.                                  (A3)

On |e|=2/M the second term has modulus at most 1/(M-2)<2/M. The finite scalar
argument principle, or Rouche's theorem applied to e, gives one simple zero
inside that circle, with multiplicity counted. The contour construction
makes e(zeta) analytic on a neighborhood of the closed |zeta|<=1/M disk and
|e|<=2/M. Define the actual right and left graph coordinates

    w=-(D-e)^(-1)W,
    ell=-Z(D-e)^(-1),
    P=(1,w)(1,ell)/(1+ell w).                               (A4)

They satisfy B(1,w)=e(1,w), (1,ell)B=e(1,ell), ell W=e, and
Z+ell D=e ell. Their norms obey

    ||w||,||ell|| <= sqrt(M)/(M-2),
    M/(M-2)^2 <= 240/238^2 < 1/225.

The last bound decreases with M>=240 by differentiating M/(M-2)^2.
Consequently 1+ell w is nonzero, P^2=P, and

    ||P||_trace <= (1+1/225)/(1-1/225)=113/112.               (A5)

The original complement is ker(1,ell). Its exact coordinate map and inverse are

    J:Q0H -> ker(1,ell),   Jh=(-ell h,h),
    J^(-1)=Q0 restricted to ker(1,ell).                     (A6)

On the unchanged operator domain direct multiplication gives

    (B-e)J=J Bc,   Bc=D-e-Well.                             (A7)

Every factor in the feedback Well is retained. For its real part,

    Re<Bc h,h> >= [1-2/M-1/(M-2)]||h||^2
                 >=[1-1/120-1/238]||h||^2
                 > (49/50)||h||^2.                         (A8)

Bc is again the same self-adjoint free operator plus a bounded perturbation.
The norm-convergent Duhamel series constructs its strongly continuous semigroup;
its derivative on Dom(K), followed by the real-part energy inequality (A8),
proves ||exp(-tau Bc)||<=exp(-49tau/50). Density extends this estimate to all
vectors. Holomorphy in zeta follows locally from the uniformly convergent bounded
perturbation series and the analytic coefficients in (A4).

The exact excited semigroup is therefore

    exp[-tau(B-e)](I-P)=J exp(-tau Bc)Q0(I-P).               (A9)

The bounds on the original graph maps are

    ||J||<=226/225,
    ||Q0P||<=113/1680,
    ||Q0(I-P)||<=1793/1680.                                 (A10)

For example Q0P=w(1,ell)/(1+ell w), and using ||w||<=1/15 and
sqrt(1+1/225)<=226/225 gives 113/1680. No product-space Gram is replaced.

For real xi, B_xi is the full self-adjoint physical operator less its displayed
scalar. Its lowest eigenvalue is <=0 by the original constant trial state.
Equation (A8) leaves the entire remaining spectrum positive after subtracting
e. Thus e is its actual ground eigenvalue. P is its actual orthogonal ground
projection, obtained above on the same domain. This also identifies the analytic
branch without choosing a surrogate vacuum.

## A3. The complete all-time analytic bound

Define the analytic connected heat observable by the literal trace

    Chat_pq(tau;zeta)
      =Tr[P Wp exp[-tau(B-e)](I-P)Wq].                       (A11)

At real xi this equals the original C_pq(tau/kappa;xi), with its actual
vacuum-mean subtraction. The complex trace is its holomorphic continuation;
no conjugation of zeta is inserted. Each original multiplication Wp has norm
at most 2. Equations (A5), (A9), (A10) give

    |Chat_pq(tau;zeta)|
      <=4(113/112)(226/225)(1793/1680)exp(-49tau/50)
      <5 exp(-49tau/50),    |zeta|<=1/M, tau>=0.             (A12)

The original link-center substitution U_(n,i) ->
(-1)^(sum_(j<i)n_j) U_(n,i) sends every plaquette trace to -Wp, preserves Haar,
K and all gauge spaces, and is its own inverse. It carries B_zeta to B_-zeta.
Both marked traces change sign, so (A11) is even in zeta. Cauchy's coefficient
formula on the original circle |zeta|=1/M and summation of the full even tail
now prove

    |Chat_pq(tau;xi)-C0_pq(tau)-xi^2 C2_pq(tau)-xi^4 C4_pq(tau)|
      <=5 exp(-49tau/50)(M|xi|)^6/[1-(M|xi|)^2],
                    |xi|<1/M, tau>=0.                     (A13)

All constants and all higher orders remain. The bound is uniform in positive
time, with its original volume dependence. It also justifies differentiation
in the source before Laplace integration. The finite rational functions in the
coefficient proof are therefore precisely the Taylor coefficients of (A11).
The Laplace uniqueness argument H3 returns their actual time functions.

## A4. A positive original opposite-face correlation on an entire time interval

For the two faces H17, C0=C2=0 and C4=h4=4P+B with H18--H20. Exact rational
Taylor remainder estimates enclose exp(-x) for each x in [0,50]: the even
Taylor sum of degree 240 is an upper bound, and subtracting x^241/241! is a
lower bound. Taylor's Lagrange remainder has the required negative sign and
magnitude <=x^241/241!. The code checks positive lower endpoints. This is
an interval calculation with rational endpoints, including at all cited times.

At L=2, M=240, xi=10^(-10), tau=1, evaluation of H18--H20 and (A13) gives

    85879/10^7 < Chat_pq(1;xi)/xi^4 < 85951/10^7.             (A14)

The complete rational inner endpoints are in generated/heat_bounds.json.
The physical parameters are g^2=50000, kappa=100000/a, and t=1/kappa.

The positivity on 1<=tau<=3 has a continuous proof. In the first bracket of
H18, let a=1/882, b=-4441/3611790, c=75173779/67612708800. Its quadratic
minimum is c-b^2/(4a). Exact rational comparison gives

    c-b^2/(4a) > (121/108864)/4+(197/9988160)/16.              (A15)

Since exp(-3/2)<1/4 and exp(-7/2)<1/16, the two negative exponentials in H18
are bounded by this quantity times exp(-3tau) for tau>=1. Its other terms are
positive. Thus P(tau)>0 throughout tau>=1. In H19 the first bracket is at
least 5/648 at tau=1 and increases, and both other terms are positive. Hence

    h4(tau) >= (5/648)exp(-3tau),    tau>=1.                 (A16)

For tau in [1,3], the ratio of the complete error (A13) to xi^4 times (A16)
is at most

    648 M^6 xi^2 exp(303/50)/[1-(Mxi)^2] < 0.531 < 1         (A17)

at the actual M and xi above. Consequently the full interacting-vacuum
correlation, not just its leading coefficient, is strictly positive on
1/kappa<=t<=3/kappa. Its original integrated value has all physical factors
retained by H4.

## A5. Full inverse-power metrics, including the original state norm

Let R:C^M->H_phys,0 have the original centered columns r_p. For integer k>=1,

    G^(k)=kappa^k R* A^(-k) R
         =int_0^infinity tau^(k-1) Chat(tau)d tau/(k-1)!.     (A18)

The actual finite-regulator spectral theorem and the positive centered gap
established in A2 justify the integral. Equation (A12) gives a uniform
integrable majorant for the analytic Taylor coefficients and their remainder.
For a partial fraction a/(z+c)^n, its exact contribution is

    a (k+n-2)!/[(k-1)!(n-1)! c^(k+n-1)].                    (A19)

Every original pole and multiplicity is used. Integrating (A13) proves the
entrywise bound

    |G^(k)_pq - sum_(j=0)^2 xi^(2j) G^(k)_(2j),pq|
      <=5(50/49)^k (M|xi|)^6/[1-(M|xi|)^2].                 (A20)

The physical energy response is G^(1). For the actual derivative primitive

    Phi=kappa A^(-1)R,
    A Phi=kappa R,    Phi*Phi=G^(2),
    Phi*A Phi=kappa G^(1),                                 (A21)

the original state and energy metrics remain separately specified.

All coefficients for k=1,2 on the original 240-face L=2 box are calculated
entry by entry in generated/native_inverse_metrics_L2.json. Let L_(k,j) be the
maximum absolute row sum of the exact degree-2j coefficient matrix. A real
symmetric M by M error whose entries have magnitude at most e has operator
norm at most M e: apply the row and column bounds and Cauchy--Schwarz. Therefore
(A20), with the complete off-diagonal rows, gives

    [3^(-k)-w_k]I <= G^(k) <= [3^(-k)+w_k]I,
    w_k=xi^2 L_(k,1)+xi^4 L_(k,2)
          +5M(50/49)^k(Mxi)^6/[1-(Mxi)^2].                  (A22)

For 0<xi<=1/1600, all the scalar terms on the right increase with xi, so its
endpoint evaluation bounds the whole interval. Exact rational evaluation gives

    (3/10)I_240 < G^(1) < (11/30)I_240,
    (9/100)I_240 < G^(2) < (13/100)I_240.                    (A23)

This is the original L=2 box, every a>0, and every g^2>=20. The identities use
the original coefficient pairing on C^240; the actual state Gram is the
calculated G^(2), not the identity. The complete original energy form on these
primitive columns is kappa G^(1). The tighter rational endpoints and each
original row-sum certificate are retained in generated/heat_bounds.json.

## A6. Scope and comparison with the preceding analysis

The finite-volume Cauchy circle in (A13) has radius 1/M. Equation (A23) has been
evaluated on the original L=2 family, with all 240 columns. Every dependence on
M, a, g and time is displayed. These statements establish neither a nontrivial
four-dimensional continuum field nor a uniform-in-volume positive mass bound.
They do not independently recertify the earlier uniform-source/gap argument.

The method uses classical bounded perturbation, block resolvents, the scalar
argument principle and the original spectral theorem. A relevant primary
Feshbach--Schur antecedent is Dusson--Sigal--Stamm, arXiv:2105.02058. The present
proof gives all blocks, graph inverses and finite constants on the actual
Hamiltonian instead of supplying a desired spectral gap as an input. The new
Split-Zero heat transfer to the resulting actual Grams is in RH_HEAT_TRANSFER.md.

## A7. The original forcing Gram for the same observation family

The time-zero matrix is the original forcing Gram G^(0)=R*R=Chat(0). It is
computed from exactly the same complete pole coefficients by

    G^(0)_(2j),pq=sum_(c>0) a_(c,1),                        (A24)

because higher pole orders vanish at tau=0. Equation (A13) at zero supplies its
complete entry error 5(Mxi)^6/[1-(Mxi)^2]. The identical full row-sum argument
on the actual L=2 box and 0<xi<=1/1600 proves

    (49/50)I_240 < G^(0) < (51/50)I_240.                    (A25)

No division by a chosen source norm is involved. The tighter rational
interval is retained with G^(1),G^(2) in generated/heat_bounds.json. Thus all
three original Grams R*R, Phi*A Phi/kappa and Phi*Phi are quantitatively
controlled together. Their use in the actual inverse-power observation is
proved in T7 of the source-transfer note.

## A8. The full original kinetic Gram, retaining its local zero entries

The forcing columns have original energy Gram R*A R=kappa Kobs, where

    Kobs_pq=<Gamma(Wp,Wq)>_rho=-Chat'_pq(0).                 (A26)

The ground-state form identity proves the first equality; differentiation of
the original semigroup proves the second. In the coefficient file each simple
pole contributes its energy times its coefficient and each double pole
contributes minus its coefficient. Higher poles contribute zero. This gives
all entries through degree four in native_inverse_metrics_L2.json.

Every off-diagonal entry outside the original face adjacency is zero exactly:
Gamma differentiates a common original edge. On a diagonal,
Gamma(Wp,Wp)=4-Wp^2 has absolute value at most4. On adjacent distinct faces,
their single shared-edge derivative vectors each have Euclidean length at most
one; writing the original SU(2) product as q0I-iq.sigma gives the length
sqrt(1-q0^2). Their scalar product has absolute value at most1. Each face has
at most12 original neighbours. All assertions concern the unchanged original
link derivatives, with their generator factor1/2 retained.

The complex ground projection from (A4)--(A5) therefore bounds the diagonal
expectation by4*113/112 and each adjacent expectation by113/112. Original
center symmetry makes these analytic expectations even. Cauchy's formula on
|zeta|=1/M bounds the entire row of the omitted tail by

    (113/112)*16*(M|xi|)^6/[1-(M|xi|)^2].                   (A27)

This uses the exact local support, rather than a dense-M multiplier on this
particular Gram. The exact degree-two and degree-four row sums and (A27) give,
on the original L=2 box with g^2>=20,

    (29/10)I_240 < Kobs < (31/10)I_240.                     (A28)

The sharper rational endpoints and every nonzero coefficient are retained in
the same records. This is the further original energy input used in T8 to
bound the correction between the actual state-minimum and energy-minimum
sections of the inverse-power family.


---

# New complete source: RH_HEAT_TRANSFER.md

# The Split-Zero heat comparison transferred to the original Yang–Mills Grams

21 September 2026. This is a source-specific transfer, accompanied by a new
calculation of actual Yang–Mills heat correlations. The inspected Riemann
workbench revision is 128aa308dd2a70ba6e073816a957d1ee6414ba2c. The exact read
ranges and source blobs are in SOURCE_INTAKE.json. Its arithmetic quantities
remain attached to their own source; the Yang–Mills quantities below are
computed from the original Hamiltonian and its physical vacuum.

## T1. What was read and what is transferred

The complete argument used from the Riemann workbench is HM6--HM14 and
HM19--HM24 of HEAT_TO_ORIGINAL_QUOTIENT_METRICS.tex (19 September). It constructs
its original coefficient column map Rcal and a finite heat replacement
Rcal_J=Rcal-T_s Pcal. The physical arithmetic source pairing is unchanged and
T_s* T_s=s^(-1)I. From the complete original Gram, including both relation
cross blocks, HM13 proves the relative column error. Triangle inequalities
give (1-delta)^2 G <= G_J <=(1+delta)^2 G. Completing the square on the same
coefficient fibers carries these bounds through their actual restrictions and
quotient minima. HM22--HM24 retain every determinant rank and give the finite
heat depth for a prescribed return error.

HG6--HG10 of ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.tex were also read. They expand
actual observation/kernel currents with both mixed products and give their
error under a relative change of the same original Gram. The fixed-divisor
subexponential estimate HG1--HG5 is retained as an inspected arithmetic result;
no value of its divisor-dependent constants is assigned to a Yang–Mills bound.

The common column-map calculation is instantiated below, on actual Yang–Mills
spaces. Its input error is supplied by the original physical semigroup rather
than by the arithmetic dilation. A source-specific map between arithmetic
zeta packets and physical gauge fields is not asserted. The explicit shared
interface and each new map are the displayed linear maps below.

## T2. The original physical heat columns and their entire forcing defect

Fix the original L=2 open box, M=240, a>0, and g^2>=20. Let A=H-E0 on the
centered physical Hilbert space H0, with its unchanged inner product. The
source columns R have entries rp=(Wp-<Wp>_rho)psi. From A23,

    Phi=kappa A^(-1)R,
    G2=Phi*Phi,   E=Phi*A Phi=kappa G1,
    (9/100)I<G2<(13/100)I,
    (3kappa/10)I<E<(11kappa/30)I.                           (T1)

All original coefficient axes p are retained. In particular Phi is injective.
The finite-regulator inverse and the original source identity A Phi=kappa R
are established in the analytic proof, not assumed as an observation metric.

The physical gap needed here has an independent short derivation. In the
original Haar space, minmax applied to B_xi=K-xi S gives its second physical
eigenvalue >=3-2Mxi. Its ground eigenvalue is <=0 by the original constant
trial vector. Therefore, for the actual centered A,

    A >=kappa(3-2Mxi)I >=(27kappa/10)I                       (T2)

because xi<=1/1600. This is a bound for this original box and coupling domain.
Every volume factor in its derivation is explicit.

For T>0 define the actual map and its convergent inverse on H0

    C_T=I-exp(-TA),
    C_T^(-1)=sum_(j>=0)exp(-jTA),
    ||C_T^(-1)|| <=[1-exp(-27kappa T/10)]^(-1).              (T3)

They commute with A on Dom(A); convergence in the graph norm follows by
commuting A through each term and applying the same geometric bound. Put

    Phi_T=C_T Phi=kappa int_0^T exp(-tA)R dt,
    E_T=Phi_T*A Phi_T,  G2_T=Phi_T*Phi_T.                   (T4)

Both state and energy errors retain their complete mixed products. Specifically,

    E_T-E =-Phi*A exp(-TA)Phi
            -Phi*exp(-TA)A Phi
            +Phi*exp(-TA)A exp(-TA)Phi,                     (T5)

with the analogous identity omitting A for G2. The two cross products are
equal here because the original A and its heat semigroup commute; their
origin in the expansion remains explicit. The source equation is

    A Phi_T=kappa R-kappa exp(-TA)R.                        (T6)

Thus the original forcing defect and its primitive are exactly
-kappa exp(-TA)R and -exp(-TA)Phi, respectively.

For epsilon=exp(-27kappa T/10), spectral calculus applied on the complete
centered physical space gives

    (1-epsilon)^2 G2 <= G2_T <= G2,
    (1-epsilon)^2 E <= E_T <= E.                            (T7)

For the energy inequality one applies C_T to A^(1/2)Phi; for the state
inequality one applies it to Phi. These are the actual column-map instances
of HM11, with a sharper one-sided upper bound supplied by the semigroup.
The norm of the omitted column is bounded relatively in its own original
state/energy pairing. All constants are independent of a after the exact
physical time T is inserted; T itself retains its factor 1/kappa.

## T3. Original support quotients and the corrected minimum

For an original face subset F, put V_F=Phi(C^F), U_F=A V_F=kappa R(C^F).
The complex is

    V_F --A--> H0 --0--> 0.                                 (T8)

Its support transition F subset G is the actual inclusion in degree zero and
identity on H0. The differential square commutes by the same original A.
For J=G\F, the transported cohomology kernel is exactly

    V_G/V_F -> ker[H0/U_F -> H0/U_G],
    [h] -> [Ah].                                           (T9)

Surjectivity follows by writing a killed class as Ah with h in V_G.
Changing h by V_F changes Ah by U_F, and conversely the injectivity of A on
H0 implies that a change by U_F has exactly a change by V_F. The inverse is
[Ah] -> [h]. The heat complexes use V_F^T=C_TV_F with the same target H0
and differential A. The actual pair (C_T,C_T) intertwines their differentials
and is invertible by (T3). It commutes with every support inclusion. Applying
the Split-Zero support reconstruction therefore retains F and its receiving
zero, together with the original killed representative and its primitive.

The energy-minimum representative of [Phi_J y] in V_G/V_F has the old-support
coordinate

    x_F=-E_FF^(-1)E_FJ y.

All blocks are taken in the fixed original face coordinates. Its exact quotient
Gram is

    Q_E(F,G)=E_JJ-E_JF E_FF^(-1)E_FJ.                       (T10)

Completing the square in x_F proves this formula and both inverse coordinate
maps to the quotient. The removed primitive Phi_F x_F remains. The state
minimum has the separately calculated formula with G2; it is not substituted
for the energy minimum.

Equation (T7) holds at every vector (x_F,y) in the same original coefficient
fiber. Taking the infimum in x_F on both sides proves

    (1-epsilon)^2 Q_E(F,G)<=Q_(E_T)(F,G)<=Q_E(F,G),           (T11)

and the state counterpart. The same proof applies successively to every finite
chain of fixed restrictions and quotient maps, retaining the same two bounds,
not multiplying an error factor at each stage. This is the actual HM19--HM21
minimum-fiber argument in the physical metric. A rank-zero quotient retains
its unique zero vector and determinant one.

To retain the surrounding physical space, put P_Phi=Phi G2^(-1)Phi*. Its
multiplication identities give P_Phi^2=P_Phi=P_Phi*. For any original form-domain
h perpendicular to im(Phi), the full energy is

    q_A(Phi c+h)=kappa c*G1 c
                +2kappa Re<Rc,h>+q_A(h).                  (T12)

This is the complete original coupling to the remaining physical functions.
No reducing-subspace property of the finite observation family is used.

## T4. A finite heat horizon for every four-return determinant

For a rank-r positive form G and its same-coordinate heat comparison satisfying
(T7), its relative eigenvalues belong to [(1-epsilon)^2,1]. The determinant
ratio is invariant under the displayed congruence with G^(-1/2), including its
inverse G^(1/2). Hence

    |log det G_T-log det G| <=2r[-log(1-epsilon)].           (T13)

The difference uses the same original frame and, for energy Grams, the same
kappa^r factor, which cancels exactly in the ratio. For any four prescribed
restriction/quotient returns with coefficients +1,+1,-1,-1 and ranks r_j<=240,

    |L_T-L| <=2 sum_j r_j [-log(1-epsilon)]
              <=1920 epsilon/(1-epsilon).                 (T14)

The final inequality follows by integrating 1/(1-x) from zero to epsilon.
Take the actual physical horizon

    T=10/kappa=5a/g^2.                                     (T15)

Then epsilon=exp(-27). The exact rational exponential enclosure gives

    epsilon<19/10^13,
    1920 epsilon/(1-epsilon)<4/10^9.                        (T16)

The calculated inner upper bound is approximately 3.608695327762*10^(-9).
The complete rational fraction is in generated/heat_bounds.json. This is one
common finite heat horizon for all four original returns and all original
support choices in this 240-column family. It requires no estimate of a newly
selected arithmetic comparison constant or observation angle.

## T5. Every signed observation current retains its mixed terms

Fix a surjection Lambda from the original C^240 onto its actual chosen
observation image; for example its rows can read a fixed subset of original
face coordinates. From the energy Gram E define

    Q=(Lambda E^(-1)Lambda*)^(-1),
    Omega=Lambda*Q Lambda,
    L=E-Omega.                                             (T17)

The minimum representative S=E^(-1)Lambda*Q satisfies Lambda S=I and
E S=Lambda*Q. Direct expansion proves that y*L y is the squared E-norm of
(1-S Lambda)y. Thus both the kernel residual and boundary Gram are the original
canonical ones, with every rectangular mixed entry preserved. Define the heat
versions using E_T and the identical Lambda.

Put eta=2epsilon-epsilon^2. Equation (T7) gives
(1-eta)E<=E_T<=E. Minimize on the identical Lambda fibers to get the same bounds
for Q. For fixed original columns a1,a2,v and omega>0 let

    K_i=a_i*L v, B_i=a_i*Omega v,
    d_i=a_i*E a_i, E_v=v*E v,
    Phi_K=2Re(conj(K1)K2)/omega,
    Phi_B=2Re(conj(B1)B2)/omega,
    Phi_cross=2Re(conj(K1)B2+conj(B1)K2)/omega.              (T18)

The same-fiber bounds and Cauchy--Schwarz give
|Delta K_i|<=2eta sqrt(d_i E_v), |Delta B_i|<=eta sqrt(d_i E_v), while each
original |K_i| and |B_i| is at most sqrt(d_i E_v). Expanding every linear and
quadratic product in (T18) proves the HG8 receiving inequalities

    |Delta Phi_K|<=2sqrt(d1 d2)E_v(4eta+4eta^2)/omega,
    |Delta Phi_B|<=2sqrt(d1 d2)E_v(2eta+eta^2)/omega,
    |Delta Phi_cross|<=2sqrt(d1 d2)E_v(6eta+4eta^2)/omega.    (T19)

These estimates contain the original phases and both cross products. The
actual source/target numerical values in this application are the calculated
Yang–Mills Grams, and their relative error is (T16). No sign of a current is
inferred from its norm alone.

## T6. Source and execution scope

This contribution reads the original HM/HG heat and metric proofs and proves
the displayed Yang–Mills instances in full. The arithmetic dilation T_s, its
Mellin variables, zeta-zero jets, original source masses and period-dependent
constants remain in the cited RH construction. Here exp(-TA) is the physical
ground-relative semigroup, with T (T15) in the original time units.

The heat coefficients, original box matrices, graph constants and rational
bounds are independently exercised by the executable tests described in
VERIFICATION.md. Their complete analytic proofs are supplied as written
arguments for review. The tests do not give a Lean proof, independently audit
every older source estimate, or establish the four-dimensional continuum gap.
The standing continuum path and the growing-volume problem still require
bounds beyond the explicitly finite M-dependent domain proved here.

## T7. The latest inverse-power observation has a concrete receiving instance

After the heat-source intake, the complete 21 September source
INVERSE_POWER_CONDUCTOR_OBSERVABILITY.tex was read at the same pinned commit.
Its IK9--IK10 construct a literal left inverse of selected original conductor
rows on their inverse-power space. IK12 returns that inverse through the
original source and observation Grams, retaining their eigenvalue factors.
IK13 explicitly permits its lower bound to tend to zero with its cutoff.
Those coefficients, root differences and guards remain in that construction.

In the present Yang–Mills family the actual inverse-power source is

    Phi=kappa A^(-1)R:C^240->H0,
    O=R*:H0->C^240,
    O Phi=G^(1).                                           (T20)

The independent computed bound (A23) makes this original response matrix
invertible, so its exact coefficient left inverse is

    W=(G^(1))^(-1) R*,
    W Phi=I_240,   ||(G^(1))^(-1)||<=10/3.                  (T21)

This is a proved inverse on these specific columns, not an assumed observation
angle. The original quotient metric for the observation O is (G^(0))^(-1):
minimizing the physical Hilbert norm over R*h=z has the representative
R(G^(0))^(-1)z. Its full residual is perpendicular to im(R), as multiplication
by R* verifies. Thus P_R=R(G^(0))^(-1)R* is the actual orthogonal projection,
and every nonzero coefficient vector c satisfies

    ||P_R Phi c||^2=c*G^(1)(G^(0))^(-1)G^(1)c,
    ||Phi c||^2=c*G^(2)c.                                  (T22)

Returning the three computed original metrics (A23),(A25) gives

    G^(1)(G^(0))^(-1)G^(1) >= (3/34)I,
    ||P_R Phi c||^2 / ||Phi c||^2 > 150/221.                 (T23)

Indeed the first coefficient is (3/10)^2/(51/50)=3/34, and dividing by the
upper state coefficient 13/100 gives 150/221. Every source metric and its
inverse has been retained. This is the IK12 left-inverse/minimum argument
applied to the original physical inverse-power family, with the needed Gram
bounds actually calculated here. It detects all 240 columns simultaneously
at L=2, every a>0 and g^2>=20. It does not supply an infinite-volume fraction or
an independence assertion for an uncomputed concatenation of higher powers.

The portion outside this observation is the exact vector
(I-P_R)Phi c. Its squared norm is

    c*[G^(2)-G^(1)(G^(0))^(-1)G^(1)]c,                       (T24)

and is positive semidefinite by the original orthogonal decomposition. No
component is removed from the energy formula (T12). The maps (T20)--(T24)
state the entire receiving construction; they make no identification of
arithmetic zeta zeros with physical spectral points.

## T8. The actual residual between the state and energy sections is bounded

Retain the original orthogonal state projection P_R from T7 and define

    h=(I-P_R)Phi,
    B0=(G^(0))^(-1)G^(1),   P_R Phi=R B0.                  (T25)

All columns of h satisfy R*h=0. Since A Phi=kappa R, the mixed energy
q_A(Phi c,h d) vanishes for every coefficient pair c,d, by the original
Hilbert adjoint identity. Thus Phi is the actual minimum-energy section
of the affine fibers R*f=G^(1)c. The state-minimum section of that same
fiber is R B0 c. They have the exact comparison

    h*Ah=kappa[G^(1)(G^(0))^(-1)Kobs(G^(0))^(-1)G^(1)-G^(1)],
    (P_R Phi)*A(P_R Phi)=Phi*A Phi+h*Ah.                    (T26)

To verify the first identity, expand the whole expression
(Phi-RB0)*A(Phi-RB0). Both cross products are kappa G^(1), while the last
term is kappa B0* Kobs B0; their signed sum is (T26). This also proves
nonnegativity of the right side. The state residual remains the matrix (T24).

The three raw bounds (A23),(A25),(A28) give the strict original energy bound

    0<=h*Ah < (1322/7203) Phi*A Phi.                        (T27)

Indeed congruence by (G^(1))^(-1/2), with its explicitly inverse square root,
puts the bracket in (T26) below

    [(31/10)(50/49)^2(11/30)-1]I = (1322/7203)I.

Returning that congruence proves (T27) in the original coefficient coordinates.
Thus the state-section correction has at most this fraction (less than0.184)
of the original primitive's energy, and (T23) retains more than150/221 of its
state norm in the actual observed force span. The difference itself remains
an element of ker(R*) with its complete state and energy Grams, rather than
being dropped. Both conclusions hold simultaneously for all240 original
columns on the specified finite box and coupling domain.

For a prescribed observation z, the two exact sections are
Phi(G^(1))^(-1)z and R(G^(0))^(-1)z, and their difference is
h(G^(1))^(-1)z. Their source-to-observation compositions are both the identity.
This supplies the explicit section-correction morphism and its quantitative
energy return in the original metric. It is the same minimum-section mechanism
read in the Split-Zero source, now with all physical Grams evaluated and the
entire correction bounded on its stated domain.
