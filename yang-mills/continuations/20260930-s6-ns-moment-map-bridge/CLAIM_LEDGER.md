# Underclaims and overclaims for the higher-domain Yang--Mills program

**Date:** 2026-09-29
**Scope:** the \(S^6\), Navier--Stokes, higher-rung, and locally-gapped synthesis.
**Controlling proof:** `HIGHER_DOMAIN_PROGRAM.md`.

## S6NS-20260929-001 — Claude's formulation is narrower than the user's program

- **Original statement:** `y9a_directions.tex`, lines 5--7, calls the closing-gap and spectral-escape question well posed.
- **Strengthening:** the intended direction selects a functionally \(S^6\)-like higher domain, constructs a globally smooth state family, and transports it into one reconstructed Yang--Mills theory.  High-energy escape is an exclusion test.
- **Proof and definitions:** main program, Sections 1, 4, 8--10; spectral companion, Sections 1--3 and 6.
- **Status:** program definition completed; construction unresolved.
- **Propagation:** main program, spectral companion, machine program ledger, current claim dispositions.

## S6NS-20260929-002 — the \(S^6\) input is stronger than one scalar angle

- **Original statement:** the limited Yang--Mills use retains the positive scalar \(D=L_Tq_T+6m_T^2\) and its background angle.
- **Strengthening:** the exact source also supplies the period matrix \(P_R\), integral division lattice, gauge-equivariant holonomy, dual spectrum, low-mode count, continuous-threshold vertical operator, discrete gauge quotient, physical mesh criterion, and closing Gaussian gap.
- **Hypotheses:** the exact radial cusp family and regulator definitions of the retained source.
- **Proof locator:** main program, Sections 2.1--2.4; source labels listed in Section 14.
- **Status:** established for the stated source operators; no interacting continuum inference.
- **Propagation:** candidate-domain criteria and Phases A, D, and E.

## S6NS-20260929-003 — a literal higher complex sphere is unnecessary and obstructed

- **Original possibility:** seek a higher complex sphere that repeats the \(S^6\) geometry literally.
- **Correction:** the retained higher-rung theorem excludes almost-complex homotopy spheres above dimension six, and the direct rank-three toroidal continuation has an Euler mismatch.
- **Strongest replacement:** an admissible soft-period gauge domain is defined by ten functional clauses and need not be a sphere or complex.
- **Proof locator:** main program, Sections 3--4; higher-rung source, Theorem `thm:all-higher-spheres` and Proposition `prop:euler-mismatch`.
- **Status:** obstruction and replacement class established; an admissible member remains unconstructed.
- **Propagation:** candidate ladder and Phase A.

## S6NS-20260929-004 — the claimed singular flow is not the smooth target state

- **Original possibility:** use the claimed Navier--Stokes singular endpoint as the globally smooth Yang--Mills state.
- **Correction:** under the exact retained Cartan map, the complete gauge current becomes singular at that endpoint; fluid time also differs from quantum Hamiltonian time.
- **Surviving use:** regular smooth divergence-free profiles, their exact vorticity density, support scales, and concentration diagnostics remain valid inputs.
- **Proof locator:** main program, Section 6; spatial source, Section 21, lines 4669--5047; gauge bridge, lines 69--143.
- **Status:** correction proved for the displayed map; independent validation of the claimed fluid theorem remains outside this program.
- **Propagation:** Phase B excludes the singular endpoint and retains regular profiles.

## S6NS-20260929-005 — the Cartan flow map omits interaction

- **Original statement:** \(A_i=\lambda u_iT\) transfers fluid curvature into Yang--Mills curvature.
- **Correction:** the image lies in one Cartan line, all connection commutators vanish, and the displayed field is generally sourced.
- **Strengthening:** Section 7 constructs the exact three-colour lift and retains every derivative and commutator term.
- **Proof locator:** main program, Section 7; symbolic receipt `checks/THREE_COLOUR_CURVATURE_CHECK.json`.
- **Status:** three-colour curvature and magnetic density proved.
- **Propagation:** interaction-profile space \(\mathfrak N_{\mathrm{int}}\), Figure 2, Phase C.

## S6NS-20260929-006 — the 24-dimensional carrier does not finish the domain step

- **Original possibility:** the octonionic flag, Albert determinant boundary, or Leech data already form the required Yang--Mills domain.
- **Correction:** they supply a smooth global carrier, three triality sectors, determinant and spectral maps, and marked lattice data, but no soft-period gauge family or interacting quantum Hamiltonian.
- **Proof locator:** main program, Sections 3 and 5; higher-rung source, lines 1538--1622, 1977--2045, 3434--3580, and 7265--7288.
- **Status:** exact available structure and exact missing structure recorded.
- **Propagation:** marked-subgroup Leech/triality soft-period hybrid is the lead construction class.

## S6NS-20260929-007 — a smooth compact carrier does not create continuous threshold spectrum

- **Original possibility:** global smoothness of a compact higher object could itself yield the desired continuum at zero.
- **Correction:** an elliptic operator on one fixed compact smooth carrier has discrete spectrum.  The threshold must arise through a noncompact end, a genuine internal continuous coordinate, or the continuum/infinite-volume limit.
- **Proof locator:** main program, Section 8.4; the \(S^6\) vertical operator in Section 2.3 exhibits the noncompact-parameter mechanism.
- **Status:** exclusion criterion established.
- **Propagation:** domain clause 9, Phase D kernels, and failure-space ledger.

## S6NS-20260929-008 — the contradiction requires the theory-identification map

- **Programme goal:** construct the globally smooth gapless state within the
  stated four-dimensional Yang--Mills axioms and derive the contradiction of
  the mass-gap statement.
- **Required map:** the reconstructed object must be identified with the
  theory selected by the original Yang--Mills action and regulator through
  universality or uniqueness.  Until that map is proved, a distinguished
  gapless branch is an intermediate object whose comparison morphism remains
  to be constructed; it is not the programme's conclusion.
- **Proof locator:** main program, Phase H; spectral companion, Work package H.
- **Status:** goal and completion condition corrected; universality theorem
  unresolved and remains part of the active proof goal.
- **Propagation:** decision language, completion certificate, machine program
  ledger, and current claim disposition.

## S6NS-20260929-009 — divergence-free colour profiles can carry colour charge

- **Original extrapolation:** three divergence-free profiles might preserve \(j_0=0\) from the one-colour Cartan map.
- **Correction:** Proposition 7.1 proves
  \[
   \mathcal J_0^c=-\frac1c\sum_{i,a,b}
   \varepsilon_{abc}\lambda_a\lambda_b
   u_i^{(a)}\partial_tu_i^{(b)}.
  \]
  It also gives every spatial source coefficient.
- **Hypotheses:** \(x^0=ct\), metric \(\operatorname{diag}(-1,1,1,1)\), \(A_0=0\), three smooth divergence-free profiles, and the retained generator normalization.
- **Proof locator:** main program, Proposition 7.1; `checks/verify_three_colour_curvature.py`; `checks/THREE_COLOUR_CURVATURE_CHECK.json`.
- **Status:** complete exact proof and independent symbolic verification.
- **Propagation:** \(\mathfrak Z_{\mathrm{YM}}\) is now the explicit zero set of twelve coefficient equations; Calculation 2 now solves these equations instead of deriving them.

## S6NS-20260929-010 — the full triality stabilizer cannot become a low-dimensional frame group

- **Original extrapolation:** map the three triality sectors directly to three spatial or colour frames while preserving the full \(\operatorname{Spin}(8)\) stabilizer.
- **Strengthened obstruction:** Proposition 3.1 proves every continuous homomorphism \(\operatorname{Spin}(8)\to G\) trivial for every finite-dimensional Lie group with \(\dim G<28\).  This includes \(SO(3)^3\) and \(SO(3)_{\mathrm{space}}\times SO(3)_{\mathrm{colour}}\).
- **Proof locator:** main program, Proposition 3.1.
- **Replacement objects:** the fixed-colour search space
  \(\mathfrak R_{\mathrm{red}}^{\mathrm{fix}}\), followed by the
  bundle-valued polynomial candidate space
  \(\mathfrak R_{\mathrm{bun}}^{X,\mathrm{poly}}\).
- **Status:** general obstruction proved; the second space now contains the
  explicit \(\operatorname{Sp}(1)\) candidate constructed from \(\mathcal M_H\).
- **Propagation:** candidate ladder, Phase A, Calculation 1, and machine program ledger.

## S6NS-20260929-011 — the retained cusp carries an explicit proper-subgroup candidate

- **Earlier underclaim:** after excluding a full
  \(\operatorname{Spin}(8)\)-to-frame homomorphism, the first program draft
  left the selection of every proper subgroup and every non-Abelian profile
  as future work.
- **Strengthening:** the retained cusp class gives the nontrivial Hopf
  pullback \(P_H\to X\), the explicit injection
  \(\rho:\operatorname{Sp}(1)\hookrightarrow\operatorname{Spin}(8)\), and
  the adjoint three-plane bundle
  \(\mathcal A_H=P_H\times_{\operatorname{Ad}}\operatorname{Im}\mathbb H\).
  The extended \(\operatorname{Spin}(8)\)-bundle is trivial, but its specified
  \(\operatorname{Sp}(1)\)-reduction retains the nonzero order-two clutching
  class.
- **Exact morphism:**
  \(\varphi(\mathbf i,\mathbf j,\mathbf k)=2(T_1,T_2,T_3)\) is a
  Lie-algebra isomorphism with
  \(-2\operatorname{tr}(\varphi(v)\varphi(w))=4\langle v,w\rangle\).
  It turns \(\mathcal A_H\)-valued divergence-free spatial one-forms into
  local \(SU(2)\) potentials forming a partial connection along the spatial
  fibres.
- **Constructed receiving-space witness:** with the exact bump-and-curl profile
  of Proposition 3.2,
  \[
   \mathcal F_{12}=2\beta^2\mathbf k_U\ne0,
   \qquad
   F_{12}=4\beta^2T_{3,U}\ne0
  \]
  on a nonempty open set.
- **Further obstruction:** \(\mathcal A_H\) has no nowhere-zero section, so
  no fixed global colour frame exists.  This obstruction requires a
  bundle-valued reduction space.  The bump profile alone does not place the
  triality bundle in that space because it is not a map from
  \(\mathcal W_H\).
- **Proof locators:** `SP1_BUNDLE_BRIDGE.md`, Propositions 2.1, 3.1,
  and 5.1 and Corollary 6.1; main program, Sections 3.2--3.3; retained
  higher-rung source, Theorem `rettri:bundleclass`, Theorem
  `rettri:subgroup`, and Proposition `rettri:forgetting`; exact local check
  `checks/SP1_BUNDLE_BRIDGE_CHECK.json`.
- **Status:** subgroup candidate, reduction, spatial partial-connection
  law, and a non-Abelian receiving profile proved.  The missing
  triality-to-profile morphism is supplied by the corrected result
  S6NS-20260930-012 below.
- **Propagation:** candidate ladder, Phases A--C, Calculation 1, machine
  program ledger, source-use ledger, dated bulletin, and bridge figure.

## S6NS-20260930-012 — the local bump was not a triality-to-profile map

- **Original overclaim:** the chart-supported bump field in Proposition 3.2
  was treated as completing the classical bundle-map part of the first
  domain calculation.
- **Correction:** that field is chosen after entering the receiving space
  \(\mathcal U_H\); it does not depend on a point of
  \(\mathcal W_H\).  It proves nonemptiness and an interaction witness only.
- **Replacement theorem:** the quadratic bundle morphism
  \[
  \mathcal M_H=
  \boldsymbol\mu_{\mathbf i}(\alpha)\otimes w^{(1)}
  +\boldsymbol\mu_{\mathbf j}(\beta)\otimes w^{(2)}
  +\boldsymbol\mu_{\mathbf k}(\gamma)\otimes w^{(3)}
  \]
  maps the complete labelled rank-\(24\) bundle to bundle-valued
  divergence-free profiles.
- **Proof locator:** PROOF.md, Theorem 7.1;
  main program, Section 3.4.
- **Status:** corrected map proved and propagated.

## S6NS-20260930-013 — linear equivariance has exactly one colour channel

- **Finding:** the retained representation decomposes as
  \[
  W\cong\mathbb R^5_{\mathrm{triv}}\oplus
  \operatorname{Im}\mathbb H_{\operatorname{Ad}}\oplus
  \mathbb H_L^{\oplus4}.
  \]
- **Exact obstruction:**
  \[
  \operatorname{Hom}_{\operatorname{Sp}(1)}
  (W,\operatorname{Im}\mathbb H_{\operatorname{Ad}})
  =\mathbb R\,\pi_{\operatorname{Ad}}.
  \]
  Hence every equivariant linear profile map has a single colour direction
  and zero commutator curvature.
- **Constructive consequence:** the quadratic moment maps
  \(\mu_e(a)=ae\bar a\) overcome this linear obstruction.
- **Proof locator:** redo note, Proposition 5.1 and Lemma 6.1.
- **Status:** obstruction and exact morphism proved.

## S6NS-20260930-014 — exact zero set and rank strata of \(\mathcal M_H\)

- **Theorem:** the fibrewise zero set is the rank-\(12\) subbundle retaining
  \(\mathcal V_{r,H}\) and the unused fourth quaternionic line.  If exactly
  \(m\) selected quaternionic coordinates are nonzero, the vertical
  differential has rank \(3m\).
- **Proof ingredients:** \(|\mu_e(a)|=|a|^2\), independence of the three
  spatial curls, and
  \[
  D\mu_e(a)D\mu_e(a)^{\mathsf T}=4|a|^2I_3.
  \]
- **Proof locator:** redo note, Lemma 6.1 and Theorem 7.1; exact receipt
  checks/SP1_MOMENT_MAP_BRIDGE_CHECK.json.
- **Status:** proved for the compact base \(X\); cusp rank behaviour awaits a
  constructed soft extension.

## S6NS-20260930-015 — the flag carrier and the \(S^6\) reduction have distinct bases

- **Original overclaim:** the candidate ladder described the retained
  \(\operatorname{Sp}(1)\) reduction as if it were already a reduction of
  \(T(F_4/\operatorname{Spin}(8))\).
- **Correction:** \(P_H\to X\cong S^6\) reduces the extended bundle
  \(Q_H=P_H\times_\rho\operatorname{Spin}(8)\) over \(X\).  The flag tangent
  splitting is a separate theorem over \(F_4/\operatorname{Spin}(8)\).
- **Required morphism:** an exact base map, pullback, fibre product, or
  comparison functor must relate these objects before they can form one
  higher domain.
- **Status:** distinction propagated; the relation remains an active
  calculation.

## S6NS-20260930-016 — the spatial field is a partial connection

- **Original overclaim:** the coefficients \(A_i\,dx^i\) were called a full
  connection on \(X\times\mathbb R^3\).
- **Correction:** they define a connection along the spatial fibres because
  transition functions depend on \(d\in X\) and have zero spatial
  derivative.  Components in the \(X\)-directions are required for a full
  connection on the product.
- **Status:** corrected in the bridge and main programme.

## S6NS-20260930-017 — the first global three-direction core is sourced

- **Constructed core:**
  \[
  (v_1,v_2,v_3)=(\mathbf i,\mathbf j,\mathbf k),\qquad
  (\mathcal F_{12},\mathcal F_{23},\mathcal F_{31})
  =(2\mathbf k,2\mathbf i,2\mathbf j).
  \]
- **Exact source:**
  \[
  \mathcal J_0=0,\qquad
  (\mathcal J_1,\mathcal J_2,\mathcal J_3)
  =(-8\mathbf i,-8\mathbf j,-8\mathbf k).
  \]
  Its \(SU(2)\) image is \(D^\mu F_{\mu j}=-16T_j\).
- **Consequence:** this core is a genuine interaction witness and is excluded
  from the source-free locus.  Its obstruction defines the correction space
  for \(\mathcal M_H+\alpha\).
- **Proof locator:** redo note, Sections 8--9; exact receipt
  checks/SP1_MOMENT_MAP_BRIDGE_CHECK.json.
- **Status:** source defect proved; source-free correction unresolved.

## Joint consequence

Findings 005, 009--017 now prove the first exact nonlinear bridge.  The
retained class breaks the full triality stabilizer through an explicit
\(\operatorname{Sp}(1)\)-reduction; the four quaternionic line summands then
supply quadratic moment maps into its adjoint colour bundle.  Three selected
lines produce the global polynomial map \(\mathcal M_H\), with a rank-\(12\) zero
subbundle and vertical rank strata \(0,3,6,9\).  Its top stratum contains a
three-direction profile with nonzero commutator curvature and magnetic
density \(48\).

The same calculation proves that the first core has source
\(\mathcal J_j=-8e_j\).  The next construction is therefore the exact
source-free correction \(\mathcal M_H+\alpha\), together with the soft-period
extension and the missing relation between the \(S^6\) base and the flag
carrier.  The topological reduction, nonlinear map, and interaction witness
are established; a globally smooth source-free state and its quantum
reconstruction remain the programme goal.

## S6NS-20260930-018 — the missing base relation is constructed

The earlier open relation between \(X\) and the flag carrier is now
the proved pullback through \(D=F_4/\rho(\operatorname{Sp}(1))\).
The full statement and proof are Theorem 2.1 and Proposition 3.1 of
HIGHER_CARRIER_AND_EVOLUTION.md. This strengthens finding 015.
The map lands in one reduction fibre, while its principal pullback is nontrivial.

## S6NS-20260930-019 — complete connection with mixed curvature

Section 4 of HIGHER_CARRIER_AND_EVOLUTION.md supplies the missing base
components through a specified Maurer-Cartan projection. Every base, mixed,
and spatial curvature term is retained. This strengthens finding 016.
The parameter dimensions are not treated as additional physical spacetime.

## S6NS-20260930-020 — the static source is an initial acceleration

Finding 017 remains correct for the static field. Equations HC15-HC20 prove
that it supplies an admissible acceleration from zero-electric Gauss data.
The exact Gauss-preserving compact-support correction has a degree-six
spatial residual. The homogeneous restriction has an exact global source-free
evolution by Theorem 7.1. Its nonzero R3 energy is infinite; the compact-support
boundary equation remains unfinished. Proposition 9.1 rules out a static
nonzero-curvature compact-support solution and makes time evolution necessary.
This strengthens the source-defect finding without turning it into a quantum result.

## Propagation of findings 018–020

The corrections and strengthenings are propagated through the current proof,
bundle note, higher-domain programme, spectral companion, source-use ledger,
machine claim overlay, dated bulletin, cumulative TeX, status, and next action.
Historical source editions remain unchanged. The quantum endpoint remains open.

## S6NS-20260930-021 — the full classical Cauchy step is supplied

The previous unresolved item was a source-free correction of the original
compact-support data. Theorem 2.1 of COMPACT_SUPPORT_CAUCHY_EVOLUTION.md
now verifies Oh's exact hypotheses and constructs its global classical
evolution. Sections 3–6 prove the parameter, support and energy consequences.
This resolves the classical part of findings 017 and 020. The global PDE
theorem is attributed to Oh and its predecessors; no novelty is claimed for it.

## S6NS-20260930-022 — electric curvature strengthens the core claim

The previous magnetic density vanishes at zeros of the homogeneous f.
The original electric field is nonzero then. Equation CE17 proves that
the sum of the two specified curvature-commutator squared norms is at least
128 throughout the exact inner diamond. This strengthens result
SZ-20260930-008 without dropping the magnetic zero or changing the field.

## S6NS-20260930-023 — zero energy and redundant state labels

Proposition 4.1 proves that a flat, divergence-free, compactly supported
input C is zero, through the complete stress divergence and trace.
The energy therefore vanishes exactly on the rank-12 input subbundle.
CE34a proves the evolved solution map has the same vertical ranks and
fibres as the original moment map, including the exact circle fibres.
Later Gram kernels must identify those equal fields; labels cannot be
declared orthogonal. The mixed cutoff energy terms remain present in CE22.

## Source convention correction encountered in this reading

The global Oh source, line 419, calls Maxwell theory the SU(1) case.
SU(1) consists only of the identity and its Lie algebra is zero.
U(1), whose Lie algebra is one-dimensional and bracket-zero, is the
abelian example that gives Maxwell's equations. This introductory typo
does not affect the SU(2) analytical theorem used here. The author source
is preserved unchanged.

## Propagation of findings 021–023

The current programmes, claim overlay, machine ledger, daily bulletin,
source ledger, cumulative TeX and reader paths carry the new classical
boundary. The quantum endpoint and full period coupling remain active.
Classical dilation is not promoted to a spectral claim.

## S6NS-20261008-001 — restore the coupling in the joint path

The earlier unpublished PK43 used \(\lambda_j=\sqrt j\) with
\(g_j^2=\kappa_*/(200j)\). CE39's fixed-coupling law cannot erase CE22's
\(g^{-2}\). The complete comparison is
\(\mathscr E_{g_j}^{[\lambda_j]}=(g_{\rm ref}^2/(g_j^2\lambda_j))
\mathscr E_{g_{\rm ref}}\). The earlier path therefore grows as
\(200g_{\rm ref}^2\sqrt j/\kappa_*\) for every nonzero input.
The corrected PK43 fixes \(\lambda_j=j^2\), \(T_j=j^6\), cover \(M_j=j^4\),
and graph \(L_j=j^4\). PK43a–PK43g prove the entire box, support, cover and
energy comparison, retaining the full I/J/K bracket and core lower bound.
The prior draft is preserved in the private checkpoint; no published classical
fixed-coupling identity is retracted.

## S6NS-20261008-002 — Gram positivity and its exact domain

The draft called the Gram kernel positive definite on unrestricted labels.
Equal gauge orbits yield equal vectors. PK30 now states positive semidefiniteness
there and proves strict positive definiteness for each finite set of distinct
gauge orbits at fixed heat parameters: the heat map is injective on finite
measures, and the orbit probability measures have disjoint compact supports.
This strengthens the equal-field comparison of finding S6NS-20260930-023 while
retaining its circle and spectator identifications.

## S6NS-20261008-003 — all core faces strengthen the raw norm

PK41's one-face lower bound has coefficient 16. Reflection doubles it.
Theorem 9.1 proves that all elementary faces are the entire first physical
electric layer. PK47 retains every original face coefficient and the full
orthogonal remainder. PK48 uses both complete core cubes and yields
\(32M_m e^{-6t}\sin^8(a/\lambda)\); PK49 supplies the explicit positive
\(j^{-15}\) lower bound. It does not identify the actual asymptotic norm.
The final proof does not assert that the complementary part is nonzero
without a separate derivation.

## S6NS-20261008-004 — evaluate the next interacting return

The electric value 3 is not an eigenvalue assertion for the full Hamiltonian.
PK50 retains the complete magnetic face sum. PK51–PK53 show that a vector
confined to the first odd electric layer has actual excitation-energy mean
\(d=2bM+3\kappa-E_0\), whose proved lower bound grows on the corrected path.
The next calculation is carried out in PK54: it gives the exact block
resolvent and upper/lower complementary-return estimates. The full original
packet is still governed by PK44, PK45 and its complementary coefficients.
No conclusion about a limiting mass gap follows from the finite compression.

## Propagation of the 8 October finite-scale findings

The corrected proof, current programmes, reader paths, source ledger, claim
records, dated bulletin, cumulative TeX and inspected reproducible diagram
carry these results. Earlier source editions remain intact. The research
endpoint and the integrated lesson series remain required.

Complete proofs: [PK1–PK54](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md). Human source conventions: [Brian C. Hall, arXiv:1707.02355v1](https://arxiv.org/abs/1707.02355v1) and [Benjamin Bahr and Thomas Thiemann, arXiv:0709.4636v1](https://arxiv.org/abs/0709.4636v1); exact comparisons in PK25–PK30.

The complementary electric bound is attained at 9/2 by the six-link rectangle with corners (-1,-1,0), (1,-1,0), (1,0,0), (-1,0,0), in every original box L >= 1. Theorem 9.1 supplies its complete Casimir, nonzero-norm and orthogonality proof. This sharpness strengthens SZ-20261008-004 and preserves the PK47 lower estimate.

## S6NS-20261009-001 — the next complementary map is nonzero

Original boundary: PK50 supplies first electric and lower magnetic moments;
PK54 gives an exact first return and the upper bound (M-1)P/s.
The full next calculation is Theorem 9.2 and PK55–PK62. Adjacent faces have
second electric moment 147/4, not 36; six distinct faces may be a cube
boundary, with exact integral 1/16. The complete matrices retain 3(D+A)/4
and 3N/2. The entire complementary moment includes the exact projection
subtraction b^2(M-1)^2P. Its next map has Gram PK59, explicit positive bounds
PK60, exact return PK61, and a strictly improved finite-volume upper bound
PK62. These strengthen SZ-20261008-005; its earlier equalities remain valid.

The increased map norm on the prescribed path is not treated as a proof of
a limiting mass gap or absence of one. The next original calculation is the
full B2 return and the actual packet's complementary coefficients. Propagated
through the cumulative proof and TeX, present programme/claim records, figure,
source-use ledger and dated bulletin. YM-01/YM-02 have no claim depending on
this new moment; YM-08's research provider receives PK55–PK62.

Complete proof: [Theorem 9.2 and PK55–PK62](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).

## S6NS-20261009-002 — the actual packet requires the full complement

Earlier boundary: PK47 supplies the exact first-face projection, and
PK54/PK61 supply compressed returns. These remain valid but do not by
themselves equal the resolvent quadratic form of the full packet.
PK63–PK64 prove the exact receiving map with all complementary packet
components and cross terms. PK65–PK75 prove a complete electric cutoff,
actual vacuum-energy interval, heat-tail estimate and full transform error.
The explicit original path cutoff has error at most Gamma_j/(kappa_* j).
PK76–PK78 recover the earlier two-vector ground trial value as the exact
minimum of the entire first physical cutoff, and evaluate the original
smallest-box example.

The spectral lower endpoint has not been shown positive. The next
calculation is the original f_j or an analytic bound on it, retaining
Gamma_j and every coupling. No continuum conclusion or novelty claim is
inferred from finite accuracy. Propagation covers the cumulative source,
claim/source ledgers, programmes, result bulletin and future YM-08 provider.
Current YM-01/YM-02 have no dependent claim requiring correction.

Complete proofs: [PK63–PK78](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).

## S6NS-20261009-003 — the actual fixed-heat path escapes

Original pending statement: PK75 supplies an accurate low-mass interval,
but its f_j and Gamma_j were not estimated sufficiently to settle weight.
Correction/strengthening: PK79–PK83 compute both full moment kernels.
PK84–PK97 prove nu_j((0,kappa_* j]) <= Gamma_j R_j, R_j -> 0, and
s_j f_j/Gamma_j -> 0. Thus the original fixed-t_* family cannot provide
a nonvanishing fraction of low-energy weight. This is not a theorem
about every interacting state or the desired continuum theory.
The raw norm has not been identified with its decreasing lower bound.

The exact subsequent construction PK98–PK100 uses the full interacting
semigroup, preserves physical oddness and calculates its moment flow.
Its supported spectral bottom remains to estimate on the original path.
The complete second moment retains both mixed terms and every ordered
face pair, including coincident and shared-link faces. The rederived earlier vacuum
upper bound strengthens the earlier finite vacuum intervals by intersection.
Propagation covers the programmes, cumulative TeX, claim ledgers, result
bulletin and planned YM-08 provider. Delivered YM-01–YM-03 have no
dependent spectral claim requiring correction.

Complete proofs: [PK79–PK100](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).

## S6NS-20261009-004 — actual odd support and prior vacuum-bound provenance

Original uncertainty: PK98–PK100 preserve the old packet's supported
bottom but do not identify its overlap with the lowest odd eigenvalue.
PK102–PK120 construct a different explicit bounded odd observable on
the actual vacuum. At each fixed L,a its support reaches the actual
odd bottom for sufficiently small positive g, with raw weight tending
to 3/32. The complete operator, character and overlap proofs are given.
PK121–PK126 evaluate the full limiting raw measure, without dividing
the vector by its mass. PK127–PK129 connect the full higher carrier
through the exact invariant scalar and preserve its rank-12 zero set.
This receiving map is not asserted to retain every angular parameter.

PK130–PK131 keep the original simultaneous regulator path. Its actual
energy error and raw weights remain to estimate. Fixed-box convergence
does not supply uniform-in-volume constants. The old packet's proved
escape remains valid and is not transferred to this different family.

Provenance correction: the PK88 bound for L at least two is already
spatial-continuum Section 12, equations (93)–(99). PK101 proves the
exact map of parameters, partition factors, trial vectors and physical
coefficients. The present rederivation also covers L=1. No new vacuum
bound is claimed. Its previous interval and escape applications survive.

Propagation: current proof and TeX, programmes, source/claim ledgers,
dated bulletin, main reading paths and future YM-08 provider updated.
Delivered YM-01–YM-03 have no dependent spectral statement requiring
correction. Actual continuum reconstruction and theory identification,
YM-04 analytical prerequisites, and J5 third return remain unfinished.

Complete proofs: [PK101–PK131](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).
