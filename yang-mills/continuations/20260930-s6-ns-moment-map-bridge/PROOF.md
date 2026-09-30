# Redo of the Sol 6 \(S^6\), triality, and Yang--Mills bridge

**Date:** 30 September 2026
**Status:** audited replacement for the overclaimed parts of the 29 September
work; complete proof of the corrected classical domain-to-profile result;
no source-free quantum state or mass-gap contradiction is claimed here.

## 1. Programme goal and present theorem

The programme goal remains

\[
 \boxed{\begin{gathered}
 \text{construct a globally smooth interacting state within the stated}\\
 \text{four-dimensional Yang--Mills axioms, prove that its reconstructed}\\
 \text{Hamiltonian has no positive mass gap, and derive the contradiction}\\
 \text{of the stated four-dimensional Yang--Mills mass-gap claim.}
 \end{gathered}}
\]

This is the goal.  It is not a conclusion of this note.

The 29 September work did prove a useful topological reduction and a local
non-Abelian seed.  It did not construct the advertised map from the retained
rank-\(24\) triality bundle to spatial profiles.  The present redo constructs
that missing map.  It also calculates the exact obstruction that appears
next: on an explicit three-direction core, the generated field has nonzero
Yang--Mills source

\[
 \mathcal J_j=-8e_j,\qquad
 J_j=-16T_j/g^2,\qquad j=1,2,3.
\]

Thus the corrected result advances the programme from an arbitrary local
bump field to a global fibrewise polynomial morphism derived from the
retained triality bundle.  Its source defect defines the next correction
space.  It does not yet give the globally smooth source-free state.

## 2. Source identity and reading coverage

The retained original source used here is

\[
\begin{aligned}
&\texttt{sources/higher\_rung/}\\
&\qquad\texttt{s6\_higher\_rung\_24d\_preprint.tex},
\end{aligned}
\]

with SHA-256

\[
\texttt{8c526746de9b56a4fcd0a274df0c470092cc82a16e49857df539a1c9d033956f}.
\]

The exact passages used are:

- lines 5205--5283: the retained map \(H=p_3q_2:X\cong S^6\to S^4\)
  and the pulled-back Hopf bundle \(P_H\);
- lines 5285--5398: the nonzero order-two clutching class, the adjoint
  bundle \(\mathcal A_H\), and its bracket;
- lines 5400--5511: the injection
  \(\rho:\operatorname{Sp}(1)\hookrightarrow\operatorname{Spin}(8)\)
  and the three explicit actions \(B,A,D\);
- lines 5576--5588: the associated-bundle convention and the quaternionic
  line \(\mathcal L_H\);
- lines 5590--5614: the original rank-\(24\) bundle
  \(\mathcal W_H\) and its exact \(\operatorname{Sp}(1)\)-splitting;
- lines 5645--5792: triviality of the extended
  \(\operatorname{Spin}(8)\)-bundle and nontriviality of the retained
  reduction and its marked subbundles.

The proof below uses those source theorems as stated and proves every new map
and coefficient directly.

## 3. Audit dispositions

| 29 September claim | Disposition after rederivation |
|---|---|
| \(P_H\to X\) has nonzero order-two clutching and \(\mathcal A_H\) has no nowhere-zero section | Retained.  This is proved in the original TeX source. |
| \(\rho(\operatorname{Sp}(1))\subset\operatorname{Spin}(8)\) is an explicit proper subgroup and \(P_H\) is a nontrivial reduction of its extended bundle over \(X\) | Retained.  This is a candidate reduction over \(X\), not yet a reduction of the tangent frame bundle of \(F_4/\operatorname{Spin}(8)\). |
| \(\varphi(\mathbf i,\mathbf j,\mathbf k)=2(T_1,T_2,T_3)\) is a Lie-algebra isomorphism | Retained.  It scales the stated inner product by exactly \(4\); it is not an isometry for those two stated metrics. |
| Every \(v\in\mathcal U_H\) defines a global connection on \(X\times\mathbb R^3\) | Corrected.  The displayed \(A_i\,dx^i\) is a spatial, or vertical, partial connection along the \(\mathbb R^3\) fibres.  A full connection also requires components in the \(X\)-directions. |
| The local bump construction is a bundle-to-gauge map from the triality carrier | Rejected.  It chooses a field independently of \(\mathcal W_H\).  It proves that the receiving profile space is nonempty and interacting, but it does not map the retained triality coordinates into that space. |
| The subgroup-selection and classical bundle-map part of Calculation 1 was complete | Rejected.  One candidate subgroup was constructed, while the required triality-to-profile morphism, cusp behaviour, and source-free condition remained absent. |
| The retained reduction is already a member of the original fixed-colour space \(\mathfrak R_{\mathrm{red}}\) | Corrected.  Its colour bundle is \(\mathcal A_H\), which has no global frame.  It belongs only to a bundle-valued candidate space after an actual map \(q\) is supplied. |
| The \(F_4/\operatorname{Spin}(8)\) carrier itself has acquired the retained \(\operatorname{Sp}(1)\) reduction | Rejected at that scope.  The proved reduction is over \(X\cong S^6\) and acts on the pulled-back rank-\(24\) representation bundle \(\mathcal W_H\).  No reduction of the \(24\)-dimensional flag manifold's tangent frame bundle has been constructed. |
| The constructed field is a globally smooth state | Corrected.  It is a smooth classical spatial gauge profile.  A physical state, its gauge projection, its Hamiltonian evolution, and its continuum reconstruction are separate maps that remain to be constructed. |
| Navier--Stokes has supplied a state in finite Yang--Mills local energy | Rejected.  The retained flow map supplies classical divergence-free profiles and gauge curvature.  No map from those profiles to a nonzero physical quantum state was proved. |
| The three-colour curvature and source formulas in Proposition 7.1 are exact | Retained after direct matrix recheck.  They define the source-zero equations; they do not solve them. |
| The two abstract spectral propositions and the finite-dimensional consistency model prove that a locally gapped, globally gapless limit is logically possible | Retained.  They contain no locality, gauge theory, interaction, or reconstruction theorem. |

## 4. Exact retained bundle data

Let

\[
 X\cong S^6,\qquad
 P_H\longrightarrow X
\]

be the pulled-back right principal \(\operatorname{Sp}(1)\)-bundle from the
retained map \(H\).  The associated-bundle convention is

\[
 (pu,v)\sim(p,\sigma(u)v).
\]

The adjoint colour bundle and the left quaternionic line are

\[
 \mathcal A_H
   =P_H\times_{\operatorname{Ad}}\operatorname{Im}\mathbb H,
 \qquad
 \mathcal L_H
   =P_H\times_{u:a\mapsto ua}\mathbb H.
\]

The source gives

\[
 [v,w]_{\mathcal A_H}=vw-wv=2(v\times w)
\]

in each oriented orthonormal imaginary-quaternion frame.  It also gives the
rank-\(24\) bundle

\[
 \mathcal W_H
 =\mathcal V_{r,H}\oplus\mathcal V_{q,H}\oplus\mathcal V_{p,H}
\]

with exact splitting

\[
 \begin{aligned}
 \mathcal V_{r,H}
   &\cong\mathbb R\oplus\mathcal A_H\oplus\mathbb R^4,\\
 \mathcal V_{q,H}
   &\cong\mathcal L_{q,1}\oplus\mathcal L_{q,2},\\
 \mathcal V_{p,H}
   &\cong\mathcal L_{p,1}\oplus\mathcal L_{p,2},
 \end{aligned}
\]

where all four labelled \(\mathcal L\)-summands are copies of
\(\mathcal L_H\).  Fibrewise, the representation is

\[
 W\cong\mathbb R^5_{\mathrm{triv}}
 \oplus\operatorname{Im}\mathbb H_{\operatorname{Ad}}
 \oplus\mathbb H_L^{\oplus4}.
\]

No summand, factor, or label in this decomposition will be suppressed.

## 5. The linear obstruction

The missing map cannot be repaired by an arbitrary equivariant linear
projection that is expected to create a non-Abelian profile.

**Proposition 5.1 (unique linear colour projection).**  As real
\(\operatorname{Sp}(1)\)-representations,

\[
 \operatorname{Hom}_{\operatorname{Sp}(1)}
 \bigl(W,\operatorname{Im}\mathbb H_{\operatorname{Ad}}\bigr)
 =\mathbb R\,\pi_{\operatorname{Ad}},
\]

where \(\pi_{\operatorname{Ad}}\) is the projection from the single adjoint
summand in \(\mathcal V_{r,H}\).

**Proof.**  The adjoint representation on
\(\operatorname{Im}\mathbb H\cong\mathbb R^3\) is irreducible: its image is
\(SO(3)\), whose standard real representation has no nonzero proper invariant
subspace.  The left action on \(\mathbb H\cong\mathbb R^4\) is also
irreducible.  If a real invariant subspace contains \(a\ne0\), the
\(\operatorname{Sp}(1)\)-orbit of \(a\) is the sphere of radius \(|a|\), and
its real span is all of \(\mathbb H\).

There is no nonzero equivariant map from a trivial representation to the
adjoint representation, because an image vector would be fixed by every
rotation.  There is no nonzero equivariant map
\(\mathbb H_L\to\operatorname{Im}\mathbb H_{\operatorname{Ad}}\): its kernel
is invariant, so irreducibility would make a nonzero map injective, which is
impossible from real dimension \(4\) to real dimension \(3\).
Finally, every endomorphism of the standard \(SO(3)\)-representation that
commutes with all rotations is a real scalar.  Applying these facts to the
displayed decomposition of \(W\) proves the formula. \(\square\)

Let \(V\) be any real spatial-profile space on which
\(\operatorname{Sp}(1)\) acts trivially.  Because \(W\) is finite
dimensional,

\[
 \operatorname{Hom}_{\operatorname{Sp}(1)}
 (W,\operatorname{Im}\mathbb H\otimes V)
 \cong
 \operatorname{Hom}_{\operatorname{Sp}(1)}
 (W,\operatorname{Im}\mathbb H)\otimes V.
\]

Therefore every equivariant linear map has the form

\[
 a\longmapsto\pi_{\operatorname{Ad}}(a)\otimes w
\]

for one fixed \(w\in V\).  For a resulting spatial field, every component
has the same colour direction.  Hence

\[
 [A_i,A_j]=0
\]

for every pair of spatial indices.  The linear obstruction is thus exact:
the retained representation contains only one linear adjoint channel, and
that channel cannot generate non-Abelian curvature from one fibre input.

Following the rule that every obstruction defines a new space, the next
receiving space is the space of smooth equivariant polynomial bundle maps
from \(\mathcal W_H\) to bundle-valued divergence-free profiles.

## 6. Quadratic quaternionic moment maps

For each unit \(e\in\{\mathbf i,\mathbf j,\mathbf k\}\), define

\[
 \mu_e:\mathbb H_L\longrightarrow
 \operatorname{Im}\mathbb H_{\operatorname{Ad}},
 \qquad
 \mu_e(a)=ae\bar a.
\]

**Lemma 6.1 (equivariance, norm, zero set, and rank).**  The map \(\mu_e\)
is a homogeneous quadratic \(\operatorname{Sp}(1)\)-equivariant map.  It
satisfies

\[
 \mu_e(ua)=u\mu_e(a)\bar u,\qquad
 |\mu_e(a)|=|a|^2,\qquad
 \mu_e(a)=0\Longleftrightarrow a=0.
\]

Its differential is

\[
 d\mu_e|_a(h)=he\bar a+ae\bar h.
\]

For \(a\ne0\), this differential has real rank \(3\); at \(a=0\), it has
rank \(0\).

**Proof.**  Associativity in \(\mathbb H\) gives

\[
 \mu_e(ua)
 =(ua)e\overline{ua}
 =u(ae\bar a)\bar u.
\]

Quaternionic norm multiplicativity and \(|e|=1\) give
\(|ae\bar a|=|a|^2\), proving the zero statement.  Differentiating the
quadratic formula gives the displayed differential.

For the rank, write \(a=ru\) with \(r>0\) and
\(u\in\operatorname{Sp}(1)\), and write an arbitrary tangent vector as
\(h=u(t+\xi)\), where \(t\in\mathbb R\) and
\(\xi\in\operatorname{Im}\mathbb H\).  Then

\[
 d\mu_e|_{ru}\bigl(u(t+\xi)\bigr)
 =r\,u\bigl(2te+[\xi,e]\bigr)\bar u.
\]

The radial term \(2te\) spans \(\mathbb Re\), while
\(\{[\xi,e]:\xi\in\operatorname{Im}\mathbb H\}=e^\perp\).
Their direct sum is \(\operatorname{Im}\mathbb H\), so the rank is \(3\).
At \(a=0\), both terms in the differential vanish. \(\square\)

The equivariance proves that \(\mu_e\) descends without a chosen frame to a
bundle map

\[
 \boldsymbol\mu_e:\mathcal L_H\longrightarrow\mathcal A_H,
 \qquad
 [p,a]\longmapsto[p,ae\bar a].
\]

Indeed, using the source convention,

\[
 [pu,a]\longmapsto[pu,ae\bar a]
 =[p,u(ae\bar a)\bar u],
\]

which is the value obtained from the equivalent representative
\([p,ua]\).

## 7. The global triality-to-profile morphism

Choose \(0<r<R\) and
\(\chi\in C_c^\infty(\mathbb R^3)\) with
\(\chi=1\) on \(B_r(0)\) and
\(\operatorname{supp}\chi\subset B_R(0)\).  Define the three exact spatial
fields

\[
 \begin{aligned}
 w^{(1)}&=\nabla\times(0,0,\chi x_2),\\
 w^{(2)}&=\nabla\times(0,0,-\chi x_1),\\
 w^{(3)}&=\nabla\times(0,\chi x_1,0).
 \end{aligned}
\]

Each is smooth, divergence-free, and supported in
\(\operatorname{supp}\chi\).  On \(B_r(0)\),

\[
 w^{(1)}=(1,0,0),\qquad
 w^{(2)}=(0,1,0),\qquad
 w^{(3)}=(0,0,1).
\]

In particular they are linearly independent as elements of
\[
 \mathcal V_{\mathrm{div},R}
 =\{w\in C_c^\infty(\mathbb R^3,\mathbb R^3):
   \nabla\cdot w=0,\ \operatorname{supp}w\subset\overline{B_R(0)}\}.
\]

The stated Euclidean metric identifies these vector fields with spatial
one-forms; this identification introduces no rescaling.

Use the ordered bundle coordinates

\[
 (\zeta;\alpha,\beta;\gamma,\delta)
 \in
 \mathcal V_{r,H}\oplus
 (\mathcal L_{q,1}\oplus\mathcal L_{q,2})\oplus
 (\mathcal L_{p,1}\oplus\mathcal L_{p,2}).
\]

Define

\[
 \boxed{
 \mathcal M_H(\zeta;\alpha,\beta;\gamma,\delta)
 =
 \boldsymbol\mu_{\mathbf i}(\alpha)\otimes w^{(1)}
 +\boldsymbol\mu_{\mathbf j}(\beta)\otimes w^{(2)}
 +\boldsymbol\mu_{\mathbf k}(\gamma)\otimes w^{(3)}.}
\]

Its target is

\[
 \mathcal A_H\otimes\underline{\mathcal V_{\mathrm{div},R}},
\]

the bundle over \(X\) whose fibre consists of compactly supported
\(\mathcal A_{H,d}\)-valued divergence-free spatial one-forms.

**Theorem 7.1 (corrected domain-to-profile theorem).**  The map \(\mathcal M_H\) is a
globally defined smooth fibrewise quadratic bundle morphism.  It has all of
the following exact properties.

1. Its spatial support is contained in \(\overline{B_R(0)}\).
2. Every output satisfies the spatial divergence equation.
3. Its fibrewise zero set is the rank-\(12\) subbundle
   \[
   \mathcal M_H^{-1}(0)
   =
   \mathcal V_{r,H}\oplus
   0_{\mathcal L_{q,1}}\oplus
   0_{\mathcal L_{q,2}}\oplus
   0_{\mathcal L_{p,1}}\oplus
   \mathcal L_{p,2}.
   \]
4. If exactly \(m\) of \(\alpha,\beta,\gamma\) are nonzero, the vertical
   differential of \(\mathcal M_H\) has rank \(3m\).  Thus the vertical rank strata
   are \(0,3,6,9\).
5. Its image contains profiles with all three spatial directions and all
   three colour directions active on \(B_r(0)\).

**Proof.**  Lemma 6.1 proves that every \(\boldsymbol\mu_e\) is a global
smooth bundle map.  Tensoring it with a fixed spatial field and summing
preserves smoothness and equivariance.  The support and divergence statements
follow from the three \(w^{(a)}\).

Their linear independence implies that \(\mathcal M_H=0\) exactly when all three
moment-map coefficients vanish.  Lemma 6.1 then gives
\(\alpha=\beta=\gamma=0\), with \(\zeta\) and \(\delta\) unrestricted.  The
remaining real rank is \(8+4=12\), proving the zero-set formula.

The vertical derivative is the direct sum of the three differentials
\[
 d\boldsymbol\mu_{\mathbf i}|_\alpha\otimes w^{(1)},\quad
 d\boldsymbol\mu_{\mathbf j}|_\beta\otimes w^{(2)},\quad
 d\boldsymbol\mu_{\mathbf k}|_\gamma\otimes w^{(3)}.
\]
The independence of the \(w^{(a)}\) makes their target summands independent.
Lemma 6.1 gives rank \(3\) for each nonzero selected coordinate and rank
\(0\) for each zero coordinate.  This proves the rank formula.

For the last statement, fix \(d\in X\) and \(p\in(P_H)_d\), and take the
three selected line coordinates to be
\([p,1],[p,1],[p,1]\).  The moment maps give
\([p,\mathbf i],[p,\mathbf j],[p,\mathbf k]\), while the spatial fields are
the coordinate fields on \(B_r(0)\). \(\square\)

This theorem supplies the map missing from the earlier note.  It uses the
two labelled spinor sectors of the original triality representation:
two quaternionic lines from \(\mathcal V_{q,H}\) and one from
\(\mathcal V_{p,H}\).  The vector sector and the fourth quaternionic line
remain present in the zero subbundle; they have not been discarded from the
domain.

## 8. Curvature and energy on the three-direction core

Fix the fibre input used in Theorem 7.1(5).  On \(B_r(0)\), write

\[
 v_1=\mathbf i,\qquad
 v_2=\mathbf j,\qquad
 v_3=\mathbf k
\]

in the frame represented by \(p\).  These coefficients are spatially
constant on the core.  Therefore

\[
 \begin{aligned}
 \mathcal F_{12}&=[\mathbf i,\mathbf j]=2\mathbf k,\\
 \mathcal F_{23}&=[\mathbf j,\mathbf k]=2\mathbf i,\\
 \mathcal F_{31}&=[\mathbf k,\mathbf i]=2\mathbf j.
 \end{aligned}
\]

Under

\[
 \varphi(\mathbf i)=2T_1,\qquad
 \varphi(\mathbf j)=2T_2,\qquad
 \varphi(\mathbf k)=2T_3,
\]

the local \(SU(2)\) curvature is

\[
 F_{12}=4T_3,\qquad
 F_{23}=4T_1,\qquad
 F_{31}=4T_2.
\]

Since
\(-2\operatorname{tr}(T_aT_b)=\delta_{ab}\), the exact magnetic density on
the core is

\[
 -2\sum_{i<j}\operatorname{tr}(F_{ij}^2)
 =16+16+16=48.
\]

This is a three-direction non-Abelian interaction witness derived from
\(\mathcal W_H\), rather than an independently chosen parameter-chart bump.

## 9. Exact Yang--Mills source defect

Interpret the displayed coefficients as a time-independent spatial partial
connection with \(A_0=0\).  In bundle-valued notation define

\[
 \mathcal J_\nu=D^\mu\mathcal F_{\mu\nu}.
\]

The time component vanishes on this static core:

\[
 \mathcal J_0=0.
\]

All spatial derivatives also vanish on \(B_r(0)\), so

\[
 \mathcal J_j=\sum_{i=1}^3[v_i,\mathcal F_{ij}].
\]

No term is omitted.  Direct calculation gives

\[
 \begin{aligned}
 \mathcal J_1
 &=[\mathbf j,-2\mathbf k]+[\mathbf k,2\mathbf j]
 =-8\mathbf i,\\
 \mathcal J_2
 &=[\mathbf i,2\mathbf k]+[\mathbf k,-2\mathbf i]
 =-8\mathbf j,\\
 \mathcal J_3
 &=[\mathbf i,-2\mathbf j]+[\mathbf j,2\mathbf i]
 =-8\mathbf k.
 \end{aligned}
\]

Applying \(\varphi\) gives

\[
 \varphi(\mathcal J_j)=-16T_j.
\]

With the source convention

\[
 D^\mu F_{\mu\nu}=g^2J_\nu,
\]

the physical source coefficients on the core are

\[
 \boxed{
 J_0=0,\qquad
 J_j=-\frac{16}{g^2}T_j,\quad j=1,2,3.}
\]

The current \(D^\mu F_{\mu\nu}\) is covariantly conserved for every smooth
connection.  Indeed, using antisymmetry of \(F_{\mu\nu}\),

\[
 2D^\nu D^\mu F_{\mu\nu}
 =[D^\nu,D^\mu]F_{\mu\nu}
 =[F^{\nu\mu},F_{\mu\nu}]=0.
\]

This identity means covariant conservation; it does not make the source
zero.  The generated core is therefore an interacting, covariantly
consistent sourced profile and is excluded from the source-free space.

![Corrected triality-to-profile morphism and source defect](figures/S6_NS_MOMENT_MAP_BRIDGE.png)

*Figure 1.  The retained rank-\(24\) bundle, the obstruction to a linear
non-Abelian map, the quadratic moment-map construction, its zero set and
rank strata, and the exact core curvature and source.  The proof locators are
Theorem 7.1 and Sections 8--9 above; the original source is the retained TeX,
lines 5205--5792.  The reproducible source is
`figures/s6_ns_moment_map_bridge_figure.py`.*

## 10. Corrected reduction space

For this base \(X\), define
\(\mathfrak R_{\mathrm{bun}}^{X,\mathrm{poly}}\) to consist of tuples

\[
 (K,P,\rho_{\mathrm{col}},\mathcal A,\mathcal W,Q,\varphi)
\]

such that:

1. \(K\subsetneq\operatorname{Spin}(8)\) is a stated closed subgroup;
2. \(P\to X\) is a proved \(K\)-reduction of a stated extended principal
   bundle, with its clutching data retained;
3. \(\rho_{\mathrm{col}}:K\to SO(3)\) and
   \(\mathcal A=P\times_{\rho_{\mathrm{col}}}\mathbb R^3\) retain their
   metric, orientation, and bracket;
4. \(\mathcal W\) is the full labelled domain representation bundle;
5. \(Q:\mathcal W\to
   \mathcal A\otimes\underline{\mathcal V_{\mathrm{div},R}}\) is a stated
   smooth equivariant polynomial map with zero set, vertical rank strata,
   support, and curvature proved;
6. \(\varphi\) is a local Lie-algebra identification with every metric
   scaling factor retained.

**Corollary 10.1.**  The tuple

\[
 \bigl(
 \rho(\operatorname{Sp}(1)),P_H,\operatorname{Ad},
 \mathcal A_H,\mathcal W_H,\mathcal M_H,\varphi
 \bigr)
\]

is an element of
\(\mathfrak R_{\mathrm{bun}}^{X,\mathrm{poly}}\).

**Proof.**  Items 1--4 are the retained source theorems.  Theorem 7.1 proves
item 5.  The exact bracket and metric calculations
\[
 \varphi([v,w])=[\varphi(v),\varphi(w)],\qquad
 -2\operatorname{tr}(\varphi(v)\varphi(w))
 =4\langle v,w\rangle_{\mathbb H}
\]
prove item 6. \(\square\)

This is the corrected completion statement: one explicit bundle-valued
polynomial candidate over the retained \(S^6\) base has been constructed.
The candidate has not been proved to be the unique or final higher domain,
and it is not yet an admissible soft-period gauge domain.

## 11. Exact boundary and next correction space

The following statements are now proved:

1. the retained \(S^6\) class produces the nontrivial
   \(\operatorname{Sp}(1)\) bundle \(P_H\) and adjoint colour bundle
   \(\mathcal A_H\);
2. the complete rank-\(24\) pulled-back triality representation has the
   source splitting used above;
3. linear equivariant maps have only one adjoint channel and cannot produce
   non-Abelian commutator curvature from one fibre input;
4. three quadratic quaternionic moment maps overcome that linear
   obstruction;
5. \(\mathcal M_H\) is a global triality-to-profile morphism with exact support,
   zero set, and vertical rank strata;
6. its image contains a three-direction profile with magnetic density
   \(48\) on an open spatial core;
7. that explicit core has source
   \(\mathcal J_j=-8e_j\), hence is not source-free.

At the original moment-map checkpoint the following objects were unfinished. The appended higher-carrier continuation now supplies the base relation, full parameter connection, and homogeneous source-free evolution; the original finite-energy spatial correction and quantum steps remain unfinished:

1. a noncompact soft-period base carrying \(P_H\) with its clutching class
   controlled along the full end;
2. cusp asymptotics of \(\mathcal M_H\);
3. a correction \(\alpha\) for which
   \(D_{A+\alpha}^{\mu}F_{\mu\nu}(A+\alpha)=0\);
4. an exact map from regular Navier--Stokes solutions into the selected
   quaternionic line coordinates of \(\mathcal W_H\);
5. a full connection including \(X\)-direction components;
6. link holonomies followed by a nonzero physical gauge projection;
7. a continuum interacting state with unique vacuum and low-energy spectral
   mass in every \((0,\varepsilon)\);
8. the universality or theory-identification morphism needed for the stated
   contradiction.

The source defect defines the next space:

\[
 \mathfrak C_{\mathcal M_H}
 =
 \left\{\alpha:
 D_{\mathcal M_H+\alpha}^{\mu}
 F_{\mu\nu}(\mathcal M_H+\alpha)=0
 \text{ for all }\nu,\qquad
 \mathcal M_H+\alpha\text{ retains a nonzero commutator term}
 \right\}.
\]

The next calculation is to derive the full bundle-valued equation for
\(\alpha\), including its Gauss component, boundary/support conditions,
and the four rank strata of \(\mathcal M_H\).  In parallel, the soft-period
pullback must specify how \(P_H\) and \(\mathcal W_H\), with their clutching
maps, extend along the end and how \(\mathcal M_H\) extends over that data.
Neither task is replaced by the present obstruction.

## 12. Machine verification

The reproducible checker

\[
\texttt{verify\_sp1\_moment\_map\_bridge.py}
\]

writes

\[
\texttt{SP1\_MOMENT\_MAP\_BRIDGE\_CHECK.json}.
\]

It verifies:

- all three coordinate moment maps and their vanishing scalar parts;
- \(|\mu_e(a)|^2=|a|^4\);
- the exact Jacobian identity
  \[
  D\mu_e(a)D\mu_e(a)^{\mathsf T}=4|a|^2I_3
  \]
  and determinant \(64|a|^6\);
- polynomial \(\operatorname{Sp}(1)\)-equivariance;
- divergence and core values of all three spatial curls;
- the three quaternionic core curvatures;
- the three source coefficients \(-8\mathbf i,-8\mathbf j,-8\mathbf k\);
- their \(SU(2)\) images \(-16T_1,-16T_2,-16T_3\).

All recorded checks pass under SymPy 1.13.1.  The receipt also records the
retained source hash and exact source-line ranges.  These checks support the
displayed calculations; the global bundle proofs remain the arguments in
this note and the cited original TeX source.

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
