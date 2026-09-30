# The retained \(S^6\) cusp class as an exact bundle-valued \(SU(2)\) bridge

**Date:** 29 September 2026
**Status:** topological reduction and receiving profile space proved; the
29 September completion claim is corrected below.  The missing
triality-to-profile map is now proved in
`PROOF.md`.  No source-free quantum state or
four-dimensional mass-gap conclusion is claimed.

The original version of this note promoted an independently chosen local
bump profile into a completed bundle map.  That promotion was invalid: the
profile did not depend on a point of the retained rank-\(24\) bundle
\(\mathcal W_H\).  The corrected quadratic morphism \(\mathcal M_H\), its zero set,
rank strata, curvature, and source defect are incorporated in Section 6.

## 1. Exact retained input

Let \(X\cong S^6\), and retain the based map

\[
 H=p_3q_2:X\longrightarrow S^4
\]

from the original cusp coordinates.  With the fixed based diffeomorphism
\(d:S^6\to X\), the retained source proves

\[
 [Hd]=\eta_4\eta_5\ne0
 \quad\hbox{in}\quad
 \pi_6(S^4)\cong\mathbb Z/2.
\]

Identify \(S^4\) with \(\mathbb H\mathbb P^1\) by
\(\chi(z)=[1:z]\), \(\chi(*)=[0:1]\), using the ordered affine basis
\((1,\mathbf i,\mathbf j,\mathbf k)\).  Pull back the right quaternionic
Hopf bundle:

\[
 P_H=(\chi H)^*S^7\longrightarrow X.
\]

The retained theorem `rettri:bundleclass` proves

\[
 c(P_H)=\partial[\chi Hd]
 \ne0
 \quad\hbox{in}\quad
 \pi_5(\operatorname{Sp}(1))\cong\mathbb Z/2.
\]

It also proves that the associated oriented real three-plane bundle

\[
 \mathcal A_H
 =P_H\times_{\operatorname{Ad}}\operatorname{Im}\mathbb H,
 \qquad
 \operatorname{Ad}_u(v)=uv\bar u,
\]

has the corresponding nonzero order-two clutching class in
\(\pi_5(SO(3))\), is nontrivial, and has no nowhere-zero continuous
section.  The fibre metric, orientation, cross product, and Lie bracket
descend, with the exact normalization

\[
 [v,w]_{\mathcal A_H}=vw-wv=2(v\times w).
 \tag{1.1}
\]

The source further proves the explicit injection

\[
 \rho:\operatorname{Sp}(1)\hookrightarrow\operatorname{Spin}(8),
 \qquad
 \rho(u)=(B_u,A_u,D_u),
 \tag{1.2}
\]

where, for \(\mathbb O=\mathbb H\oplus\mathbb H\ell\),

\[
 \begin{aligned}
 B_u(a,b)&=(ua\bar u,b),\\
 A_u(a,b)&=(ua,b\bar u),\\
 D_u(a,b)&=(a\bar u,b\bar u).
 \end{aligned}
 \tag{1.3}
\]

The extension

\[
 Q_H=P_H\times_\rho\operatorname{Spin}(8)\longrightarrow X
 \tag{1.4}
\]

is trivial as a principal \(\operatorname{Spin}(8)\)-bundle, while its
specified \(\rho(\operatorname{Sp}(1))\)-reduction \(P_H\) remains
nontrivial.  After choosing any trivialization of \(Q_H\), the reduction is
represented by a non-null map

\[
 f_H:X\longrightarrow
 \operatorname{Spin}(8)/\rho(\operatorname{Sp}(1)).
 \tag{1.5}
\]

The Grassmannian map in the retained source recovers the same three-plane:

\[
 (\Gamma f_H)^*\mathcal T_3\cong\mathcal A_H.
 \tag{1.6}
\]

Thus (1.2) supplies the proper closed subgroup demanded by the first stage
of the higher-domain program.  The class is lost if one retains only the
three unrestricted rank-eight triality bundles; it is retained by the
specified reduction and its distinguished three-plane.

## 2. The exact colour Lie-algebra map

Set

\[
 T_a=-\frac{i}{2}\sigma_a,
 \qquad
 [T_a,T_b]=\varepsilon_{abc}T_c,
 \qquad
 -2\operatorname{tr}(T_aT_b)=\delta_{ab}.
 \tag{2.1}
\]

Define

\[
 \varphi:\operatorname{Im}\mathbb H\longrightarrow\mathfrak{su}(2),
 \qquad
 \varphi(\mathbf i)=2T_1,
 \quad
 \varphi(\mathbf j)=2T_2,
 \quad
 \varphi(\mathbf k)=2T_3.
 \tag{2.2}
\]

**Proposition 2.1 (bracket and metric factors).**  The map \(\varphi\) is a
real Lie-algebra isomorphism.  For all
\(v,w\in\operatorname{Im}\mathbb H\),

\[
 \varphi([v,w])=[\varphi(v),\varphi(w)],
 \qquad
 -2\operatorname{tr}(\varphi(v)\varphi(w))
 =4\langle v,w\rangle_{\mathbb H}.
 \tag{2.3}
\]

**Proof.**  Quaternion multiplication gives

\[
 [\mathbf i,\mathbf j]=2\mathbf k,
 \quad
 [\mathbf j,\mathbf k]=2\mathbf i,
 \quad
 [\mathbf k,\mathbf i]=2\mathbf j.
\]

Equation (2.1) gives

\[
 [2T_1,2T_2]=4T_3=\varphi(2\mathbf k),
\]

and the two cyclic identities are identical.  Bilinearity proves the first
identity in (2.3).  The images of the ordered quaternionic basis are linearly
independent, so \(\varphi\) is an isomorphism.  The second identity follows
from

\[
 -2\operatorname{tr}((2T_a)(2T_b))=4\delta_{ab}.
\]

Every factor of two is therefore retained. \(\square\)

Because \(\operatorname{Sp}(1)\) and \(SU(2)\) are connected and simply
connected, \(\varphi\) integrates to the unique group isomorphism
\(\Phi:\operatorname{Sp}(1)\to SU(2)\) with differential \(\varphi\).
It obeys

\[
 \varphi(uv\bar u)
 =\Phi(u)\varphi(v)\Phi(u)^{-1}.
 \tag{2.4}
\]

Consequently \(P_H\), with its structure group transported by \(\Phi\), is
a principal \(SU(2)\)-bundle, and \(\mathcal A_H\) is its adjoint bundle
with the metric scaled by the explicit factor four in (2.3).

## 3. Why a fixed global colour frame is impossible

**Proposition 3.1 (frame obstruction).**  There is no oriented bundle
isomorphism

\[
 \mathcal A_H\cong X\times\mathbb R^3.
 \tag{3.1}
\]

There is not even one nowhere-zero continuous colour direction in
\(\mathcal A_H\).

**Proof.**  A trivialization in (3.1) would supply three everywhere linearly
independent sections and hence a nowhere-zero section.  The retained theorem
`rettri:bundleclass` proves that no nowhere-zero section exists.  More
explicitly, such a section could be divided by its positive length.  Its
orthogonal complement would be an oriented two-plane bundle over \(S^6\).
Its clutching map lies in
\(\pi_5(SO(2))=\pi_5(S^1)=0\), so that complement would be trivial, forcing
\(\mathcal A_H\) to be trivial.  This contradicts its nonzero clutching
class. \(\square\)

This identifies the exact defect in a map to one fixed
\(\mathbb R^3_{\mathrm{colour}}\).  The correct receiving object is the
adjoint bundle itself.  Local colour triples exist and are related on
overlaps by the \(SO(3)\) adjoint transitions of \(P_H\); they cannot be
assembled into a single global triple.

## 4. The bundle-valued divergence-free profile space

Let

\[
 M=X\times\mathbb R^3,
 \qquad
 \mathcal E_H=\operatorname{pr}_X^*\mathcal A_H\longrightarrow M.
\]

Define

\[
 \begin{aligned}
 \mathcal U_H=\bigl\{
 v={}&\sum_{i=1}^3v_i(d,x)\,dx^i
 \in\Gamma^\infty(
 \mathcal E_H\otimes
 \operatorname{pr}_{\mathbb R^3}^*T^*\mathbb R^3):\\
 &\operatorname{supp}(v)\subset X\times K
 \text{ for some compact }K\subset\mathbb R^3,
 \quad
 \sum_{i=1}^3\partial_i v_i=0
 \bigr\}.
 \end{aligned}
 \tag{4.1}
\]

The divergence in (4.1) is global.  Indeed, the transition functions of
\(\mathcal E_H\) depend on \(d\in X\) and not on the spatial coordinate
\(x\).  If

\[
 v_{i,\beta}=\operatorname{Ad}_{g_{\alpha\beta}(d)^{-1}}
 v_{i,\alpha},
\]

then

\[
 \sum_i\partial_i v_{i,\beta}
 =\operatorname{Ad}_{g_{\alpha\beta}(d)^{-1}}
 \sum_i\partial_i v_{i,\alpha}.
 \tag{4.2}
\]

For \(v\in\mathcal U_H\), define its spatial curvature by

\[
 \mathcal F_{ij}(v)
 =\partial_i v_j-\partial_jv_i+[v_i,v_j]_{\mathcal A_H}.
 \tag{4.3}
\]

Equation (4.2), bracket equivariance, and the absence of spatial derivatives
of the transition functions show that (4.3) is a global section of
\(\mathcal E_H\).  In a local frame, put

\[
 A_{i,\alpha}=\varphi(v_{i,\alpha}).
 \tag{4.4}
\]

On an overlap, (2.4) gives the usual spatial gauge transformation

\[
 A_{i,\beta}
 =\operatorname{Ad}_{\Phi(g_{\alpha\beta})^{-1}}A_{i,\alpha}
 +\Phi(g_{\alpha\beta})^{-1}
   \partial_i\Phi(g_{\alpha\beta}).
 \tag{4.5}
\]

The second term in (4.5) is zero because
\(g_{\alpha\beta}=g_{\alpha\beta}(d)\).  Therefore the local fields in
(4.4) form a global spatial, or vertical, partial connection along the
\(\mathbb R^3\) fibres of \(X\times\mathbb R^3\).  A full connection on
the product also requires components in the \(X\)-directions.  The spatial
curvatures obey

\[
 F_{ij}(A)=\varphi(\mathcal F_{ij}(v)),
 \qquad
 -2\operatorname{tr}(F_{ij}(A)^2)
 =4\lVert\mathcal F_{ij}(v)\rVert^2.
 \tag{4.6}
\]

## 5. An explicit global non-Abelian element

**Proposition 5.1 (compactly supported interacting profile).**  The space
\(\mathcal U_H\) contains a smooth element \(v\) for which

\[
 [v_1,v_2]_{\mathcal A_H}\ne0
\]

on a nonempty open subset of \(X\times\mathbb R^3\).  On a smaller open
subset its derivative curvature vanishes and

\[
 \mathcal F_{12}(v)=2\beta(d)^2\mathbf k_U(d),
 \qquad
 F_{12}(A)=4\beta(d)^2T_{3,U}(d).
 \tag{5.1}
\]

**Proof.**  Choose a trivializing open set \(U\subset X\), an oriented
orthonormal local frame
\((\mathbf i_U,\mathbf j_U,\mathbf k_U)\) of \(\mathcal A_H|_U\), and a
nonnegative function \(\beta\in C_c^\infty(U)\) that is positive on a
nonempty open set \(U_0\Subset U\).  Choose
\(\chi\in C_c^\infty(\mathbb R^3)\) equal to one on a ball
\(B_r(0)\).  With spatial coordinates \((x_1,x_2,x_3)\), set

\[
 \begin{aligned}
 w&=\nabla\times(0,0,\chi(x)x_2),\\
 z&=\nabla\times(0,0,-\chi(x)x_1).
 \end{aligned}
 \tag{5.2}
\]

Both fields are smooth, compactly supported, and divergence-free because
each is a curl.  On \(B_r(0)\),

\[
 w=(1,0,0),
 \qquad
 z=(0,1,0).
 \tag{5.3}
\]

Define on \(U\times\mathbb R^3\)

\[
 v_i(d,x)=\beta(d)
 \bigl(w_i(x)\mathbf i_U(d)+z_i(x)\mathbf j_U(d)\bigr),
 \tag{5.4}
\]

and extend it by zero outside \(U\times\mathbb R^3\).  This extension is
smooth because \(\operatorname{supp}\beta\Subset U\).  It has support in
\(X\times\operatorname{supp}\chi\), and

\[
 \sum_i\partial_i v_i
 =\beta\bigl((\nabla\cdot w)\mathbf i_U
             +(\nabla\cdot z)\mathbf j_U\bigr)=0.
\]

Hence \(v\in\mathcal U_H\).  For \(d\in U_0\) and \(x\in B_r(0)\),
(5.3) gives

\[
 v_1=\beta\mathbf i_U,
 \qquad
 v_2=\beta\mathbf j_U,
 \qquad
 v_3=0.
\]

The local fields are spatially constant there, so the derivative terms in
(4.3) vanish.  Equation (1.1) gives

\[
 \mathcal F_{12}(v)
 =[v_1,v_2]
 =\beta^2[\mathbf i_U,\mathbf j_U]
 =2\beta^2\mathbf k_U.
\]

Applying \(\varphi\) gives the second formula in (5.1).  Since
\(\beta>0\) on \(U_0\), both values are nonzero on
\(U_0\times B_r(0)\). \(\square\)

The construction uses two independent divergence-free directions, retains
the full quaternionic bracket, and has an interaction witness that cannot
cancel against derivative curvature on the stated open set.  It also shows
why the absence of a global colour frame does not prevent a global gauge
profile: the partial connection is a section of an adjoint bundle rather
than a triple of globally labelled scalar coefficients.  This proposition
proves that the receiving space is nonempty.  It does not define a map from
\(\mathcal W_H\) into that space.

## 6. The corrected reduction space

The fixed-frame search space from the first program draft separates into two
objects.

Let \(\mathfrak R_{\mathrm{fix}}\) denote reductions equipped with a global
identification of their colour three-plane with
\(X\times\mathbb R^3_{\mathrm{colour}}\).  Proposition 3.1 excludes the
retained cusp reduction from \(\mathfrak R_{\mathrm{fix}}\).

The earlier version defined \(\mathfrak R_{\mathrm{bun}}\) using only a
receiving profile space \(\mathcal U\).  Membership then became automatic
once \(\mathcal U\) was named, even though no triality-to-profile map had
been constructed.  The corrected base-specific space
\(\mathfrak R_{\mathrm{bun}}^{X,\mathrm{poly}}\) consists of tuples

\[
 (K,P,\rho_K,\mathcal A,\mathcal W,Q,\varphi),
 \tag{6.1}
\]

where:

1. \(K\subsetneq\operatorname{Spin}(8)\) is a stated closed subgroup;
2. \(P\to X\) is a proved \(K\)-reduction of a stated extended principal
   bundle, with all clutching data retained;
3. \(\rho_K:K\to SO(3)\) is the colour action;
4. \(\mathcal A=P\times_{\rho_K}\mathbb R^3\) retains its metric,
   orientation, and fibre Lie bracket;
5. \(\mathcal W\) is the full labelled domain representation bundle;
6. \(Q:\mathcal W\to
   \mathcal A\otimes\underline{\mathcal V_{\mathrm{div},R}}\) is a smooth
   equivariant polynomial map with its zero set, vertical rank strata,
   support, divergence, and curvature laws proved;
7. \(\varphi\) is an exact local Lie-algebra identification with every
   metric scaling factor recorded.

The retained splitting is

\[
 \mathcal W_H\cong
 (\mathbb R^5\oplus\mathcal A_H)
 \oplus(\mathcal L_{q,1}\oplus\mathcal L_{q,2})
 \oplus(\mathcal L_{p,1}\oplus\mathcal L_{p,2}).
\]

For \(e\in\{\mathbf i,\mathbf j,\mathbf k\}\), the quadratic map

\[
 \boldsymbol\mu_e:\mathcal L_H\longrightarrow\mathcal A_H,
 \qquad
 [p,a]\longmapsto[p,ae\bar a]
\]

is well defined because
\(\mu_e(ua)=u\mu_e(a)\bar u\).  It satisfies
\[
 |\mu_e(a)|=|a|^2,\qquad
 \operatorname{rank}D\mu_e(a)=
 \begin{cases}3,&a\ne0,\\0,&a=0.\end{cases}
\]

Choose the three compactly supported divergence-free fields

\[
 \begin{aligned}
 w^{(1)}&=\nabla\times(0,0,\chi x_2),\\
 w^{(2)}&=\nabla\times(0,0,-\chi x_1),\\
 w^{(3)}&=\nabla\times(0,\chi x_1,0),
 \end{aligned}
\]

which equal \(e_1,e_2,e_3\) where \(\chi=1\).  With ordered coordinates
\((\zeta;\alpha,\beta;\gamma,\delta)\) in the displayed splitting, define

\[
 \mathcal M_H=
 \boldsymbol\mu_{\mathbf i}(\alpha)\otimes w^{(1)}
 +\boldsymbol\mu_{\mathbf j}(\beta)\otimes w^{(2)}
 +\boldsymbol\mu_{\mathbf k}(\gamma)\otimes w^{(3)}.
 \tag{6.2}
\]

The complete proof in
PROOF.md, Theorem 7.1, gives

\[
 \mathcal M_H^{-1}(0)
 =\mathcal V_{r,H}\oplus\mathcal L_{p,2},
\]

with the three selected zero sections understood, and proves vertical rank
\(3m\) when exactly \(m\) of \(\alpha,\beta,\gamma\) are nonzero.

**Corollary 6.1 (corrected).**  The tuple

\[
 \bigl(
 \rho(\operatorname{Sp}(1)),P_H,\operatorname{Ad},
 \mathcal A_H,\mathcal W_H,\mathcal M_H,\varphi
 \bigr)
 \tag{6.3}
\]

belongs to \(\mathfrak R_{\mathrm{bun}}^{X,\mathrm{poly}}\).  Its image
contains a three-direction core with

\[
 \mathcal F_{12}=2\mathbf k,\qquad
 \mathcal F_{23}=2\mathbf i,\qquad
 \mathcal F_{31}=2\mathbf j,
\]

but that core has

\[
 \mathcal J_0=0,\qquad
 \mathcal J_j=-8e_j,\qquad
 D^\mu F_{\mu j}=-16T_j.
\]

**Proof.**  The retained source proves the subgroup, bundle, colour action,
and complete splitting.  The cited theorem proves every property of \(\mathcal M_H\).
Proposition 2.1 proves the bracket and the exact metric scaling by \(4\).
The core source follows by the direct calculation
\(\mathcal J_j=\sum_i[v_i,\mathcal F_{ij}]\). \(\square\)

This completes one explicit polynomial bundle-map candidate over \(X\).
It does not select the final higher domain, attach a soft-period end, solve
the source equation, or construct a quantum state.

## 7. Exact remaining boundary

The result establishes all of the following:

1. the retained \(S^6\) class supplies the explicit candidate
   \(K=\rho(\operatorname{Sp}(1))\subsetneq\operatorname{Spin}(8)\);
2. its reduction is nontrivial even though the extended
   \(\operatorname{Spin}(8)\)-bundle is trivial;
3. the reduction supplies an exact adjoint \(SU(2)\) colour bundle;
4. local colour fields patch as a spatial partial connection;
5. smooth compactly supported divergence-free bundle-valued profiles exist;
6. the polynomial map \(\mathcal M_H\) sends the full labelled rank-\(24\) bundle to
   such profiles, with exact zero set and vertical rank strata;
7. its image contains a three-direction profile with proved nonzero
   commutator curvature and magnetic density \(48\) on an open core;
8. the same core has exact nonzero source
   \(\mathcal J_j=-8e_j\).

The following statements have not been established:

1. a global section of \(\mathcal W_H\) selecting a nonzero top-rank
   \(\mathcal M_H\)-profile over every \(d\in X\);
2. a soft-period or Gram degeneration carrying this reduction along a
   noncompact parameter end;
3. a correction of \(\mathcal M_H\) that solves all source and Gauss equations while
   retaining nonzero commutator curvature;
4. a full connection with components in the \(X\)-directions;
5. a physical finite-lattice state and its projected norm;
6. internalization of the parameter \(d\) in one quantum theory;
7. a continuum limit with unique vacuum, interaction, and positive spectral
   mass in every \((0,\varepsilon)\) has been reconstructed;
8. universality has identified such a limit with the canonical
   four-dimensional Yang--Mills theory.

The first source insertion is now complete and produces the nonzero defect
above.  The next calculation is the full bundle-valued correction equation

\[
 D_{\mathcal M_H+\alpha}^{\mu}F_{\mu\nu}(\mathcal M_H+\alpha)=0,
\]

with support, boundary, Gauss, and interaction conditions retained.  In
parallel, the period data must be attached to \(P_H\) and the order-two
clutching class followed along the complete soft end.  These calculations
determine the correction space rather than treating the sourced profile as a
state.

## 8. Proof-source locators

- `sources/higher_rung/s6_higher_rung_24d_preprint.tex`, lines 5205--5283: the exact retained
  cusp map, affine quaternionic coordinate, Hopf bundle, and transition.
- Same source, Theorem `rettri:bundleclass`, lines 5285--5398: nonzero
  clutching classes, absence of a nowhere-zero section, and the fibre bracket
  \([v,w]=2(v\times w)\).
- Same source, Theorem `rettri:subgroup`, lines 5400--5511: the injective
  \(\operatorname{Sp}(1)\) triality subgroup and its three exact actions.
- Same source, lines 5513--5643: the original Peirce-sector bundles,
  determinant, trace form, and nonzero trilinear product.
- Same source, Proposition `rettri:forgetting`, lines 5645--5792: triviality
  of \(Q_H\), survival of the reduction, the non-null reduction map, and the
  Grassmannian realization of \(\mathcal A_H\).
- The source identifies its related-triple convention and Jordan action with
  Yokota, Sections 1.10, 1.16.2, and Theorem 2.7.1, while retaining the exact
  quaternionic and octonionic formulas used here.
- `checks/verify_sp1_bundle_bridge.py` independently checks all nine basis-bracket
  identities, all nine metric-factor identities, both curl divergences, the
  core values of the two spatial fields, and the exact local commutator
  curvature.  Its machine receipt is `checks/SP1_BUNDLE_BRIDGE_CHECK.json`.
- `PROOF.md` proves the corrected polynomial
  domain-to-profile map, its linear obstruction, moment-map rank theorem,
  zero set, rank strata, three-direction curvature, and source defect.
- `checks/verify_sp1_moment_map_bridge.py` checks the exact coordinate,
  equivariance, Jacobian, curl, curvature, and source identities.  Its
  receipt is `checks/SP1_MOMENT_MAP_BRIDGE_CHECK.json`.

## Higher carrier and source evolution — proved continuation

The complete derivation is in [HIGHER_CARRIER_AND_EVOLUTION.md](HIGHER_CARRIER_AND_EVOLUTION.md).
Its Theorem 2.1 constructs the exact map \(r_H:X\to D=F_4/\rho(\operatorname{Sp}(1))\),
with \(r_H^*(F_4\to D)\cong P_H\), \(\pi r_H\) constant, and
\(E_D\cong\pi^*T(F_4/\operatorname{Spin}(8))\). The dimensions are
\(\dim D=49\), \(\dim(F_4/\operatorname{Spin}(8))=24\), and fibre dimension 25.
The profile map extends to \(E_D\); its pullback is exactly \(\mathcal M_H\).
Section 4 supplies a full parameter-space connection and retains its mixed curvature.

For the original compactly supported profile \(C=\mathcal M_H(v)\), the source
\(S_j=\sum_iD_iF_{ij}(C)\) is a permitted initial acceleration with zero
initial electric field. Proposition 6.1 proves that \(A=C+s^2S/2\) preserves
Gauss's law exactly, retains the support, and has the complete residual
\(s^2L/2+s^4Q/4+s^6N/8\). Theorem 7.1 constructs the exact source-free
homogeneous core evolution for every input and every initial rank stratum.
For the equal-colour core, \(f''+8f^3=0\) has
\(f'^2+4f^4=4\) and physical energy density \(24/g^2\).

The homogeneous solution has finite energy on each stated spatial torus and
infinite total energy on \(\mathbb R^3\) when it is nontrivial. The original
cutoff boundary still requires the full PDE correction. Proposition 9.1 proves
that a nonzero-curvature compactly supported correction cannot remain static.
The next calculation therefore retains time evolution, the support boundary,
and the full soft-period data. The quantum-state and reconstruction goal remains active.
