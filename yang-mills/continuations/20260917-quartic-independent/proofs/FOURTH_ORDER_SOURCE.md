# Completed fourth-order source in the original lattice coordinates

Audit and continuation, 17 September 2026. The requested basis is the supplied
`Pasted markdown(6).md`. Its original bytes are preserved in `input/`. The
published cubic predecessor was read at Git revision
`91434b6962062bd80439d4cb2cae9d2479264dde`; source recovery and its limits are in
`sources/`. This note gives a complete, executable fourth-order source catalogue.
It makes no new claim about a uniform gap or the four-dimensional continuum.

## 1. Operator, source, and the distinction that needs to be retained

Use the original finite open cubic graph and positive edges, generators
`T_a=-i sigma_a/2`, derivatives `X_e,a`, and Haar probability. Write

\[
 K=-\sum_{e,a}X_{e,a}^{2},\qquad
 H=\kappa[K+\xi(2M-S)],\quad S=\sum_pW_p,
 \quad\kappa=2g^2/a,\quad\xi=1/(4g^4).
\tag{Q1}
\]
The original ordered face is
`W_(n;i,j)=tr(U_i(n)U_j(n+e_i)U_i(n+e_j)^-1 U_j(n)^-1)`.
Let `P_H` be Haar expectation and `Q_H=I-P_H`. The original physical source
is the zero-Haar-mean logarithmic vacuum `v=Q_H log psi`, with scalar return

\[
 \psi=\exp(v+c),\quad c=-\tfrac12\log\int e^{2v}dU,\qquad
 E_0=\kappa[2M\xi-P_H\Gamma(v,v)],
 \quad\Gamma(f,h)=\sum_{e,a}(X_{e,a}f)(X_{e,a}h).
\tag{Q2}
\]
The scalar `c` and the additive original energy have not been discarded.
The coefficient equation is

\[
 v=\xi v_1+B(v,v),\qquad v_1=S/3,\quad
 B(f,h)=K^{-1}Q_H\Gamma(f,h).
\tag{Q3}
\]
The inverse in Q3 is on its actual nonconstant physical polynomial image.
On a fixed finite graph its uniqueness follows from the positive Casimir and
Haar centering.

Consequently, at `q2=xi*v1+xi^2*v2`, the exact residual and full fourth
coefficient are different specified expressions:

\[
 R_2=\xi^3v_3+\xi^4b_{22},\quad b_{22}=B(v_2,v_2),\qquad
 \boxed{v_4=2B(v_1,v_3)+b_{22}.}
\tag{Q4}
\]
The uploaded L5–L7 give `b22`. Equation Q4 retains the additional incoming
source and its unique `K^{-1}Q_H` primitive. This package computes their
signed sum before any norm bound.

## 2. The exact tree-coordinate map and its inverse

For the original edge union E of a connected face cluster, choose the stored
spanning tree T, root o, and original oriented chords `c_1,...,c_r`, where
`r=|E|-|V|+1`. For a vertex v let `h_v(U)` be the original ordered product
along the tree path from o to v, using inverse links on reverse traversals.
Define

\[
 Z_j=h_{s(c_j)}(U)\,U_{c_j}\,h_{t(c_j)}(U)^{-1},
 \qquad
 \Phi:SU(2)^E\longrightarrow SU(2)^T\times SU(2)^r,
 \quad U\longmapsto(U_T,Z).
\tag{Q5}
\]
Its inverse keeps `U_T` and sets
`U_c=h_s(U_T)^-1 Z_c h_t(U_T)`. Both compositions are literal identities.
Successive left and right Haar translations in the chord variables prove
`dU=dU_T dZ`. A gauge-invariant function pulls back from a function of Z
invariant under simultaneous conjugation; its original Haar norm is exactly
its product-Haar norm in these variables. The remaining root gauge action
is retained, rather than treated as an extra independent observable.

At the slice `U_T=I`, an original chord derivative is `L_(j,a)`, the original
left generator of Z_j. For a tree edge e, let `s_e(c),t_e(c)` be the zero-one
indicators that the original paths to the two chord endpoints cross e.
Up to the common path-orientation sign for that one e, its field is

\[
 V_{e,a}=\sum_c[s_e(c)L_{c,a}-t_e(c)R_{c,a}].
\tag{Q6}
\]
The common sign cancels in the original squared generator and in Gamma.
The reduced kinetic operator is the exact original operator

\[
 K_T=-\sum_{e\in E,a}V_{e,a}^{2}.
\tag{Q7}
\]
To prove Q6–Q7, vary one original tree link as `exp(tT_a)U_e`, and then apply
Q5. Each affected chord becomes `exp(epsilon*s_e*tT_a) Z_c
exp(-epsilon*t_e*tT_a)`. Its first and second derivatives are precisely the
stated fields. Gauge covariance returns this identity from the tree slice
to every original configuration. The checker additionally verifies it by
independent second-order quaternion jets through every original edge of
all 78 representatives. Those are supplementary coordinate tests; Q5–Q7
are the analytic identification of the operator.

## 3. Complete polynomial coordinates with exact relations

Each stored chord has quaternion coordinates
`Z=q0 I-i(q1 sigma1+q2 sigma2+q3 sigma3)`, with
`q0^2+q1^2+q2^2+q3^2=1`. The algebra is the rational polynomial quotient by
these original sphere relations, one per chord. In the stored representative
monomials each q0 exponent is zero or one. The relation maps are explicit:
`q0^2 -> 1-q1^2-q2^2-q3^2`; their inverse interpretation is evaluation on the
original sphere. The ideal generators have relatively prime leading
monomials in different chord groups, so this representation is unique.
No state or energy metric is replaced by a Euclidean coefficient norm.

The generator matrices are the original quaternion multiplications by
`(0,e_a/2)` on the left or right. Thus all their entries are rational halves.
The original moments are

\[
 \int q_0^{d_0}q_1^{d_1}q_2^{d_2}q_3^{d_3}\,dq=0
 \quad\hbox{if any }d_i\hbox{ is odd},
\]
\[
 \int\prod_iq_i^{d_i}dq
 =\frac{\prod_i(d_i-1)!!}{4\cdot6\cdots(2+\sum_i d_i)}
 \quad\hbox{when all }d_i\hbox{ are even}.
\tag{Q8}
\]
The empty denominator and `(-1)!!` are one. Products over distinct chords
use independent original Haar factors. Q8 supplies every mean and full
polynomial Gram used in the package.

## 4. The exact finite inverse and coefficient recurrence

Introduce formal face source coordinates `lambda_p`, with the original
physical diagonal map `lambda_p=xi` after all coefficients have been
computed. The exact physical operator on that diagonal is Q1.
For a multiindex nu, its original edge multiplicity is
`m_e(nu)=sum_(p containing e) nu_p`. Its allowed edge spins are
`j_e=m_e/2,m_e/2-1,...` down to zero or one half. Therefore the finite list
of possible positive Casimirs on that source is

\[
 \mathcal C_\nu=
 \left\{\sum_ej_e(j_e+1)>0:
 j_e\in\{m_e/2,m_e/2-1,\ldots\}\right\}.
\tag{Q9}
\]
Extra allowed values are harmless. The implementation proves that its
returned inverse solves the original equation, not just a matrix fit.
For a centered forcing f, start `r0=f`, `y0=0`, and for each `c in C_nu` set

\[
 y_{j+1}=y_j+r_j/c,\qquad r_{j+1}=r_j-K_Tr_j/c.
\tag{Q10}
\]
The exact identity is `K_T y_j=f-r_j` at every stage. The final polynomial
`r_j` is checked to be zero in the original sphere quotient. This gives a
unique centered inverse because K_T is a sum of nonnegative squares and
its chord fields alone force a zero-derivative function to be constant.
All these operations have finite degree because this is a coefficient
calculation at a stated order; no finite-spin approximation to the full
Hamiltonian or its spectrum is used.

For explicit arithmetic it is convenient to use a formal eigenline
representative `u(lambda)=1+sum_(nu!=0)u_nu lambda^nu`, `P_H u_nu=0`, of
`K-sum_p lambda_p W_p`, with eigenvalue `e(lambda)`. This is an explicitly
recorded choice of the scalar coordinate of the eigenline. Its exact return
is `v=Q_H log u`, followed by Q2 for the physical unit vacuum. The inverse
coordinate relation is `u=e^v/(P_H e^v)`, whose denominator has constant
coefficient one. The original physical normalization is not dropped.
The recurrences used are

\[
 F_\nu=\sum_{p:\nu_p>0}W_pu_{\nu-e_p},\qquad
 e_\nu=-P_HF_\nu,
\]
\[
 K_Tu_\nu=Q_HF_\nu+
   \sum_{0<\mu<\nu}e_\mu u_{\nu-\mu},\quad P_Hu_\nu=0.
\tag{Q11}
\]
Terms are interpreted coefficientwise, with `mu<=nu`. Writing
`l=log u`, differentiation of the formal series gives the complete
coefficient relation

\[
 l_\nu=u_\nu-\frac1{|\nu|}
     \sum_{0<\mu<\nu}|\mu|\,l_\mu u_{\nu-\mu},
 \qquad v_\nu=Q_Hl_\nu.
\tag{Q12}
\]
As an independent polynomial check for each coefficient the program verifies

\[
 K_Tv_\nu=
 Q_H\!\sum_{0<\mu<\nu}
 \Gamma_T(v_\mu,v_{\nu-\mu}),\qquad |\nu|>1,
\tag{Q13}
\]
with `K_Tv_(e_p)=W_p` and
`2 Gamma_T(f,h)=(K_T f)h+f(K_T h)-K_T(fh)`.
These are identities of complete rational polynomials, not agreements only
at finitely many sampled configurations.

## 5. All connected fourth-order supports are included

The source operation Gamma differentiates a common original link. Its
inverse Casimir creates no new link. Consequently every nonzero logarithmic
coefficient has an edge-connected face multiset. Starting from the four
faces incident on the original anchor edge `(0,0,0;direction0)`, the
following exhaustive recursion suffices: add a repeated present face or a
face sharing an original edge with a present face, and retain the sorted
multiset. Any connected multiset containing that anchor can be recovered
in this way by removing a leaf of a rooted spanning tree of its adjacency
graph, or one repeated occurrence. Counts by order are

\[
 4,\quad46,\quad612,\quad8621.
\tag{Q14}
\]
The 48 signed coordinate permutations and translations act on the original
faces and links. A reversed edge maps to its inverse; this is a Haar- and
Casimir-preserving coordinate map. A reversed complete SU(2) face word has
the same trace. Each orbit is represented by its explicitly stored minimum
corner coordinates and ordered axes. The fourth-order orbit counts are

| Face-multiplicity partition | Orbits |
|---|---:|
| 4 | 1 |
| 3+1 | 2 |
| 2+2 | 2 |
| 2+1+1 | 19 |
| 1+1+1+1 | 54 |
| Total | 78 |

`results/quartic_coefficients/class_00.json` through `class_77.json` contain
all 4,044 nonzero rational monomials of these 78 fully calculated source
coefficients. They also give original faces, tree links, chords, root,
original derivative fields, coupling multiindex, Haar mean and full Haar
state/energy norms. These auxiliary Haar norms are not asserted to be the
interacting physical norms.

One class (index25) has four distinct faces but five chord variables: the
four-sided tube formed by the cube's lateral faces. Its original graph has
an extra independent cycle. The implementation retains it. Replacing the
chord count by the number of faces would change this original source.

The source for any original finite box is reconstructed by summing each
contained connected multiset once, pulling its representative polynomial
back through the stored lattice symmetry and Q5, and setting every formal
face coordinate to xi. Q11–13 already include the correct multiplicities;
no additional division by 4! is applied. `results/anchored_quartic_transports.json`
also records all 8,621 original face multisets, their class numbers, and an
explicit signed coordinate permutation plus translation for each. The original
edge orientation and inverse-link rule are implemented by `transform_edge` in
`calculations/reconstruct.py`. This is a complete finite, coordinate-level
specification of v4, rather than an unevaluated B term.

## 6. A readable closed component and the signed derivative

For a single face the fully evaluated contribution is

\[
 \boxed{v_4^{(p^4)}=
   \frac{17}{10368}\chi_1(\Omega_p)
   -\frac7{51840}\chi_2(\Omega_p).}
\tag{Q15}
\]
The own-face part of the already available b22 is
`chi1/10368-chi2/31104`. The other incoming term in Q4 has coefficients
`chi1/648-chi2/9720`. Adding them gives Q15 exactly.
The signs remain in the catalogue before any norms are taken.

The catalogue also determines every formal plaquette-direction response
through degree three by the exact derivative

\[
 Z_p^{[3]}=\partial_{\lambda_p}
       \sum_{1\le|\nu|\le4}\lambda^\nu v_\nu.
\tag{Q16}
\]
Differentiating Q13 coefficientwise proves that the terms through total
degree three in
`[K-2Q_H Gamma(q3,.)] Z_p^[3] - W_p` vanish, with
`q3=sum_(1<=|nu|<=3) lambda^nu v_nu`.
The remaining degree4–6 polynomial is exactly the corresponding sum of
those unremoved higher products. This records the signed tangent data; it
is not being promoted to a uniform bound on the full linearized inverse.

The previous numerical coupling threshold requires a coefficient trace-norm
bound and a full infinite-tail argument. This session does not replace
those with the catalogue's Haar norms or assert a new threshold.

## 7. Evidence scope

Every returned coefficient has zero Haar mean, an exact inverse residual,
and an independently expanded exact logarithmic-source residual. The sum
over all 78 coefficient downsets executes 1,053 inverse/source steps. The
additional second-order-jet audit differentiates original unfixed links and
verifies the tree return and original vertex-gauge invariance at retained
rational assignments for every representative. Those assignments are an
independent regression; the polynomial equalities and operator maps above
are the identity argument. No independent external or Lean review is
claimed. The full raw input, recovered code, calculations and receipts are
included in this session's ZIP.
