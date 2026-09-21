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
