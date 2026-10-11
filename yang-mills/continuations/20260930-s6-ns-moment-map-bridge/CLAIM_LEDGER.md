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

## S6NS-20261009-005 — the cutoff collapses and the global map continues

Original pending calculation: PK131 asks whether the fixed-box odd-vacuum
observable retains raw mass and first weight along the original joint path.
PK132–PK142 settle both as zero for this chart-supported family. The exact
operator bound retains N links, d chords, all Haar constants, the original
Casimir shift and every boundary term. Its logarithmic exponent is at most
-63/4 after division by d_j log j for fixed chord radius. The supported
observable space, its exact receiving projection and its norm bound are
given in PK141a. Radius growth below j^(21/4) has the same vanishing result.
This does not change the fixed-box limits PK120 and PK129, nor exclude
other states. Interacting semigroup contraction cannot restore this raw mass.

The next construction PK143–PK150 uses exact smooth group trace coordinates
on every original chord, with no logarithm-chart support restriction.
Its original transverse-cochain coefficients are proved in PK143a.
Its finite-regulator norm is positive at every positive coupling and
parameter amplitude, and its higher-carrier zero set is exactly the original
rank-12 subbundle. The same Taylor proof strengthens the earlier cutoff
map's finite-regulator nonzero statement, even though its path mass vanishes.

PK151–PK157 calculate the complete ordered derivatives and actual moments.
The ground-state transform is an earlier programme result, with its full
new application proved here. The new global family's joint-path norm,
energy and spectral measure remain to estimate; finite positivity does
not assert positive limiting weight. Continuum reconstruction and intended
theory identification remain unfinished.

Propagation: full proof, cumulative and standalone TeX, source and claim
ledgers, current programmes, reading paths, dated bulletin and future YM-08
provider updated. Delivered YM-01–YM-03 have no dependent spectral assertion.

Complete proofs: [PK132–PK157](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).

## S6NS-20261009-006 — full chord contractions and the actual fourth-moment scale

Original pending calculation: PK157 asks for the global observable's
actual raw norm and energy moments along the unchanged regulator path.
PK158–PK162 derive the exact original chord coefficients, full three-row
Gram matrix, coincident contraction and absolute sums. No tree edge is
removed from a holonomy word by this coefficient calculation.

PK163–PK171 prove the entire Haar fourth contraction, including the
negative coincident-index correction, and the exact four-loop expression
in the actual interacting vacuum. PK168 bounds actual raw norm by the
actual fourth moment times beta^2. On the original path, beta^-2 is
asymptotic to kappa_*^2 j^6/(5000 pi^2). This is a proved receiving
inequality, not a proof of the needed growth in the actual vacuum.
The Haar fourth moment tends to 3/2 and cannot be substituted into it.

PK172–PK177 supply full word-occurrence derivative bounds and actual
first/second energy-moment bounds at all positive couplings. The retained
score constant xi=1/(4g^4) grows on the prescribed path; the current
upper bounds do not establish a closing actual gap.

Propagation: full proof, source and claim ledgers, programmes, bulletin,
reading paths, inspected figure and cumulative TeX updated. Future YM-08
receives these proved estimates; delivered YM-01–YM-03 are unaffected.
Next calculate the actual four-loop combination and gradient-weighted
expectations. Reconstruction, the intended theory and the continuum
contradiction remain the goal.

Complete proofs: [PK158–PK177](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).

## S6NS-20261009-007 — actual amplitude limits and the complete phase space

The previous global map was proved nonzero at each finite regulator,
with its original fixed-box weak-coupling limit and complete actual
moments. PK177a–PK177f apply the retained potential estimate to every
original chord face, evaluate all weights and prove that this resulting
bound is too weak on the unchanged path.

PK178–PK180 exhibit the exact defect of a global negative-reflection
identification: the two original nonidentity links give phase values
4 beta_0 d_0^2 and -12 beta_0 d_0^2. PK181–PK187 consequently strengthen
finite positivity to the exact actual large-amplitude raw-mass limit
1/4, calculate both leading energy moments and prove spectral escape.
The opposite iterated weak-coupling limit is 1/2. Existing fixed-A
weak-coupling theorems remain valid with their original quantifiers.

PK188–PK189 give an actual noncollapsing higher-carrier sequence on the
unchanged coupling/regulator path, with proved high-energy escape and
divergent first/second moment lower bounds. This is a proved property
of that selected amplitude sequence; it does not exclude low-energy
states or settle the original A=1 family.

Continue with the exact space PK190–PK202: the joint phase image,
actual pushforward measure, isometry, closed energy form, full residual
Hamiltonian action and polynomial variational matrices are constructed
and proved. The second-moment residual is retained; no invariance of
the phase range under the full Hamiltonian is asserted. The first
matrix retains all original four-loop and gradient cross terms.

Propagation: full proof, source and claim ledgers, dated bulletin,
programmes, illustrated reader and future YM-08 provider. Delivered
YM-01–YM-03 have no affected phase or spectral assertion. The next
calculation is the actual matrix entries and residual on the original
path. The continuum endpoint and remaining lessons remain active.

Complete proofs: [PK177a–PK202](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).

PK203–PK206 further prove actual rank two almost everywhere, an actual Lebesgue phase density, null boundary mass and positive definite conditional energy coefficients. The finite polynomial Gram and energy matrices have zero kernel for these original objects. The full operator identity is proved distributionally on the entire phase plane, retaining all boundary contributions. This strengthens the general construction in PK190–PK202 without a uniform ellipticity assertion.

Complete strengthening: [PK203–PK206](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).

## S6NS-20261009-008 — actual vacuum concentration and certified phase matrices

PK190–PK206 constructed the phase matrices in the actual vacuum but did
not evaluate their entries or control a replacement vacuum. PK207–PK211
prove a stronger actual-vacuum statement on the unchanged path: even an
electric cutoff proportional to the number of faces receives vanishing
vacuum mass. The full vacuum energy has an explicit j^12 lower bound.
The original excitation shift H-E0 remains intact.

PK212–PK222 construct quantitative vacuum-cutoff comparisons and
finite enclosures for all three actual phase matrices. These derive
the missing approximation estimates; they do not assume an identified
vacuum. The finite sums include all original words, derivative terms
and every magnetic face. PK223–PK225 retain the entire complementary
second moment and prove its degree limit. PK226–PK227 provide certified
variational and raw spectral-weight intervals. Their shrinking-window
lower endpoint has not yet been proved positive.

Propagation: full proof and TeX, source/claim ledgers, daily bulletin,
programmes, inspected figures and future YM-08 source map. Delivered
YM-01–YM-03 contain no affected spectral or vacuum assertion. This
strengthens the earlier cutoff and phase results; it does not invalidate
their quantifiers or identify electric energy with excitation energy.

Complete proof: [PK207–PK227](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md).

# Mathematical findings and propagation

## SZ-20261011-001

PK172–PK177 retained all word occurrences but used a bound proportional to the entire link count. IP2–IP9 evaluate both the first and squared occurrence sums with every repeated root segment and boundary exclusion. The resulting bound grows as \(n^7\), improving the former \(n^9\) bound and its original-path negative loss from \(j^{31}\) to \(j^{23}\). This is a bound on the actual expression; it does not determine the expression's asymptotic value or sign.

Full proof: [IP1–IP9](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_MOMENTS_AND_ORIGINAL_PATH.md). It strengthens the finite receiving estimates used in PK202 and PK227.

## SZ-20261011-002

PK148 treats a bounded sine observable. Applying its strong vacuum limit alone to the unbounded polynomial \(x-y\) would leave a tail unjustified. IP10–IP17 derive the required actual potential moments, global phase bounds and derivative bounds, then prove norm and energy convergence for every fixed polynomial at fixed \(L,a\). IP18–IP20 evaluate raw norm, energy, fourth moment, first odd-cluster weight, and the full polynomial matrices. The limiting Gram rank is \(R\) and nullity is \(R(R-1)/2\), although every finite-regulator Gram matrix is positive definite.

Full proof: [IP10–IP22](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_MOMENTS_AND_ORIGINAL_PATH.md). This strengthens PK148, PK202 and PK205 without changing their quantifiers. IP21–IP22 preserve the unresolved difference between the iterated limit and the prescribed joint path. The tail coefficient's growth is a proved property of the bound, not a lower bound on the true tail.

## SZ-20261011-003

J7 left the third Schur coefficient, full complementary inverse and accumulated tail unevaluated. P3–P26 prove a central-sign involution on the original labelled source and its exact assembly quotient. Every odd-degree return word vanishes separately; in particular the third coefficient is zero. P20–P21 bound the full complementary inverse. P31–P38 bound every remaining even order by an explicit rational majorant. P39–P45 retain the original Hamiltonian scalar, actual vacuum map and full nonlinear interior inverse.

Full proof: [P1–P45](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORIGINAL_J5_PARITY_AND_TAIL.md); prior exact channels: [J1–J7](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BASELINE_J5.md). The first unevaluated Schur coefficient is now the fourth. No new physical gap or enlarged nonlinear endpoint follows from the auxiliary bounds.

L. Li and Y. Meurice's original arXiv:hep-lat/0410029v2 TeX, Sections II–IV and the Appendix at the recorded coverage, supplies the human antecedent for center reversal and coupling parity. The original kinetic, label and boundary comparisons are proved here. Novelty is not asserted.

## SZ-20261011-004

The open-box sign construction extends to all rectangular open boxes. For periodic rectangular boxes with \(N_i\ge3\), CS9–CS14 prove existence exactly when every \(N_iN_j\) is even. All assignments are classified, including their winding signs: one central gauge class in the open case, eight in the admissible periodic case. The precise obstruction is the constant face cochain, evaluated on the coordinate two-tori. CS4 also constructs the gauge-equivariant bijection between all \(U_p=-I\) fields and all flat fields once a reversing assignment exists; the larger field quotient is not asserted to consist of eight points.

Full proof: [CS1–CS19](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CENTRAL_SIGNS_AND_BOUNDARIES.md). This gives the exact boundary scope of the map used in SZ-20261011-003. The unique elementary plaquette-data set in Li–Meurice is preserved as such and is not read as a classification by all winding observables.

## Propagation and remaining calculation

The original phase proof PK1–PK227 and original J1–J7 provider remain identifiable. These additions are linked from the programme reading paths, entered in its result and claim ledgers, and included in the cumulative TeX. Historical records remain historical; current continuation instructions now start the Jacobian branch at the fourth coefficient.

The source's positive finite-regulator Gram result remains correct. Its conditioning can deteriorate in the fixed-box coupling limit, as proved above. That degeneration must remain in any simultaneous-cutoff estimate involving the inverse Gram matrix. The existing approximation certificate controls numerical error, while the actual shrinking-window covariance cancellation still needs a mathematical estimate.

The interacting continuum state, reconstruction, global smoothness and no-gap endpoint remain the active research goal.

## SZ-20261011-005

IP17–IP20 give fixed-box Gram and energy matrices but not every spectral weight. [SP1–SP16](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_SPECTRAL_WEIGHTS.md) prove the finite Hermite coefficient formula, the full determinant generating kernel and convergence of all original phase-family actual cluster weights at fixed box. The complete cubic raw weights are 2700, 2160 and 1440. The exact oscillator second-moment matrix and complementary energy map have residual entry 864δ*². Its minimal invariant closure is the three-dimensional space generated by q, uq and q³ times the complete vacuum. This strengthens IP17–IP20 and supplies the full limiting target for the PK223 complement calculation. It does not assert convergence of unbounded actual second moments, convergence of finite-regulator inverse Gram matrices, or a uniform joint-path estimate.

Every formula and connecting operator is proved in SP1–SP16. The 104 finite rational checks supplement those proofs. The source and reading record retains PK102–PK112 and IP10–IP20. No novelty claim is made for Gaussian or Hermite methods.

## SZ-20261011-006 — exact reflection normal map and global two-link component

[JP1–JP49](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDARY_REFLECTION_AND_RAW_ENDPOINT.md) preserve the original box, rooted words, coefficient rows, vacuum and regulator path. They prove the reflected-word map, the full boundary normal metric \(G_{\mathcal B}=2I+mD_{\rm wall}D_{\rm wall}^{t}\), and a nonzero normal derivative although the original correction vanishes on the identity boundary fibre. The exact global two-link harmonic gives
\[
\mu|\nabla D|^2\ge d_*^2e^{-24\pi\xi}/8,\quad
\mu D^2\ge d_*^2e^{-40\pi\xi}/8,\quad
G\ge\beta_0^2d_*^2e^{-24\pi\xi}/12,\quad
C_F\ge\kappa\beta_0^2d_*^2e^{-24\pi\xi}/6.
\]
The earlier all-link and boundary-only bounds remain proved, but JP43–JP49 strengthen their exponential loss to order \(j^2\). The full six-term endpoint and the direct even mass-to-energy map retain every contribution. These are lower bounds for different actual quantities, not a quotient estimate or proof of positive shrinking-window mass. The actual four-loop/gradient cancellation remains unfinished. All 66 finite word, derivative, metric and harmonic checks passed; they supplement the complete proofs.

## SZ-20261011-007 — complete fourth Schur coefficient and physical response

[Q1–Q50](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/fourth_return/FOURTH_SCHUR_COEFFICIENT.md) evaluate all eight fourth-order return words of the unchanged fifth-reference Jacobian, preserving intermediate complementary projections and union labels. Independent exact recurrence, parity and geometry calculations establish every coefficient and the all-box formula. Its boundary skew matrix is
\[
S_{[4]}-S_{[4]}^t=-\frac{703}{19712160}[D_{\rm deg},A_{\rm adj}],
\qquad\|S_{[4]}\|_{H\to H}\le\frac{4574447}{33510672}.
\]
The full remainder from degree six has the original local-norm bound in Q40. Q47 proves the exact observation-and-resolvent map to the symmetric physical susceptibility, including the normalized vacuum scalar and higher source correction. Q50 proves that no positive metric tending to the original Haar metric can make this Schur map self-adjoint near zero. Its defect defines the explicit boundary skew matrix and its receiving map; it is not a failure of physical self-adjointness. This completes the former fourth-coefficient backlog. The independent cube proof and polynomial differentiation certificate are retained with all seven replay scripts and their exact dependencies. No new continuum gap claim follows.

## SZ-20261011-008 — physical inverse at every finite real source

[GPR1–GPR55](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GLOBAL_PHYSICAL_RESPONSE.md) prove the original physical source Jacobian is invertible on every physical zero-Haar-mean Sobolev space at every finite real independent source. The complete inverse retains both different means, the actual vacuum and the original factor κ. GPR11–GPR18 prove the exact bounded map from all original union labels to their assembly quotient and an independent global inverse on that quotient. The old labelled Taylor-series radius is unchanged.

GPR19–GPR26 strengthen the earlier response statement to strict positive definiteness and identify the Wilson expectation map as a real analytic diffeomorphism onto the interior of the convex hull of the actual full Wilson image. GPR35–GPR40b compute the complete two-link mixed trace derivatives and cancel the exact Haar cube volume by averaging every centre, retaining every exterior link and actual density. With the full original face norm and \(C_*=1/(e2^{37})\), the unchanged path satisfies
\[
\|(R_j^{\rm phys})^{-1}\|\le16C_*^{-2}M_j^2
\left(1+128\sqrt3\,{10000j^2\over\kappa_*^2}\right)^8=O(j^{40}).
\]
This improves the provisional local-coordinate powers while preserving all original objects. The complete source inverse has its different explicit estimate; no full spectral inverse is assigned the face-response bound. GPR53–GPR55 also prove the actual integrated homogeneous-response identity, with its endpoint justified by the original vacuum energy bound. These finite-source results do not determine the actual shrinking-window phase weight or the continuum endpoint. The unquotiented relation-kernel inverse is a subsequent calculation, not assumed here. Exact symbolic checks and a reproducible inspected figure accompany the proof. No novelty claim is made for the underlying elliptic or convex methods.

## SZ-20261011-009 — polynomial score comparison and original-row optimization

[PC1–PC52](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POLYNOMIAL_CONDITIONAL_BOUNDS.md) prove a complete degree-two quaternion-polynomial comparison in the original radius-two metric. For every positive unit density with logarithmic score at most \(B\),
\[
\int|P|^2\rho\,dU\ge c_{\rm cap}(1+B)^{-8}\int|P|^2dU,
\qquad c_{\rm cap}=\frac{\cos^{14}(1/4)}{1024\cdot105041\pi3^{9/2}}>2^{-37}.
\]
The exact stereographic map retains its denominator and all lower-degree coefficients. A complete 35-dimensional cube Gram estimate and averaging every cap centre prove the bound. The explicit smooth densities PC20–PC22 prove exponent-eight optimality for this full polynomial space. The original colour-vector receiving map has exponent two, with its own proved optimality family and complete constant in PC25.

PC45–PC48 prove the full word, conjugation and derivative maps for a larger pair of links already present in the original phase. Its coefficient \(d^\circ=8\cos(3h)\cos^3h/n^3\) is the exact maximum within the specified receiving family; the original state and regulator path are unchanged. PC49–PC52 give actual-vacuum lower bounds whose right sides have scales \(j^{-46}\) for odd mass and energy, \(j^{-44}\) for even mass, and \(j^{-45}\) for the positive endpoint correction. These improve the exponential bounds in JP43–JP49. They are asymptotics of proved bounds, not of the unknown expectations. The complete four-loop/gradient cancellation and low-window mass remain unresolved. All 21 checks passed; exact Gram checks and numerical word/limit checks are distinguished in the receipt. The inspected figure illustrates the proved sharpness family and original coefficients, with full reproducible quadrature retained.

## SZ-20261011-010 — the full labelled inverse at every finite real source

[UL1–UL47](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/union_label_global/FULL_UNION_LABEL_INVERSE.md) prove a bounded real analytic inverse of the entire original union-labelled Jacobian, including the assembly relation kernel. For every edge subset, the proof uses the full original Hamiltonian with exactly its contained face sources, its actual positive vacuum, and both original means. Boolean cumulative coordinates give the exact conjugacy and inverse
\[
\mathfrak L_x^{-1}=\mathfrak m\,\operatorname{diag}(\mathscr L_A^{-1})\,\zeta.
\]
All supported domains, real uniqueness, the original source germ and its full union labels, energy coefficients, removed Haar scalars and vacuum normalization coefficients are proved explicitly. This completes the full finite-source inverse beyond the previously established assembly quotient. It does not enlarge the Taylor disk at zero. All 7,656 exact Boolean and constant checks passed; elliptic assertions are supported by the complete proofs.

## SZ-20261011-011 — exact connected supports and stronger transformation constants

[UF1–UF17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SUPPORT_AND_SCALAR_FACTORIZATION.md) prove product-vacuum factorization for disjoint sets of interacting link variables before imposing gauge constraints. Möbius inversion then shows that the vacuum, energy, removed scalar and normalization coefficients vanish outside connected unions of active face boundaries, for every finite real source. Every label remains in the inverse. The full original two-adjacent-face example retains its shared-edge term \(v_{P\cup Q}-v_P-v_Q\), with all seven oriented edges and Wilson words displayed.

The original physical gauge constraint forces each nonzero supported coordinate to contain at least four edges. Applying this to the exact Boolean count strengthens each transformation norm to \((N+4)2^{N-7}\), and propagates its square through the full inverse and the original-path bound. The estimate still has exponential volume dependence; quantitative control of the connected coefficients and the actual shrinking-window endpoint remain to be derived. All 14,120 exact support/counting checks passed. The inspected figure and its source display the complete inverse and the actual adjacent-face example.

## SZ-20261011-012 — exact cap blocks, sharp vector exponent and all boundary derivatives

[PS1–PS76](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POLYNOMIAL_SCORE_AND_ORIGINAL_ENDPOINT.md) prove the complete fourteen-dimensional cap comparison with constant \(C_2=24398405/306317856079872>2^{-24}\), strengthen the original two-link mass and mass-Gram estimates, and prove the exact three-component quadratic-vector estimate with arbitrary affine remainders and constant \(C_6=2595575/14797504512\). The full polynomial exponent eight and the special-vector exponent six are proved optimal for their stated score classes by explicit smooth densities. Every actual conditional and marginal score, metric factor, boundary word and coefficient sign is retained.

Adding all distinct selected physical derivatives gives the complete functions \(B_6,B_2^-,B_2^+\) in PS58. Their original-path odd and even energy bounds have order \(j^{-34}\), and the positive endpoint correction has order \(j^{-33}\), with full constants. These are lower-bound functions, not asymptotic evaluations of the unknown expectations. Both exact rational and symbolic replay certificates pass. The original Dai–Wang author TeX is used only for the precise polynomial-space, measure and metric comparison PS76; no unspecified theorem constant or literature novelty is claimed.

## SZ-20261011-013 — full gradient comparison and every original bulk-link energy

[PG1–PG70](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POLYNOMIAL_GRADIENT_BOUNDS.md) retain all scalar, vector and tensor Dirichlet blocks, including their affine off-diagonal terms. Their complete cap calculation proves
\[
\int|\nabla P|^2\rho\,dU\ge\Psi_6(B)\|\Pi_2P\|_2^2,
\quad c_6=(23/24)^{10}/588>2^{-10},
\quad\Psi_6(B)=\max\{2e^{-2\pi B},c_6e^{-B r_6(B)}r_6(B)^6\}.
\]
The exponent six is proved optimal. The exact original receiving map permits summing every distinct direction-two bulk-link energy; the boundary derivatives from PS are disjoint and are added as well. The final inequalities are \(\mu|\nabla D|^2\ge B_6+A_D\) and \(C_F\ge\kappa\beta_0^2(B_6+A_F)\), with every positive summand and boundary class evaluated in PG55–PG67. The odd energy lower bound has order \(j^{-30}\). The positive endpoint correction retains order \(j^{-33}\) with an additional strictly positive leading coefficient from the complete even bulk sum. PG69 gives both correctly signed endpoint inequalities, retaining the unresolved original expectations. All 31 checks pass. A missing square in one explanatory derivative line was corrected before publication; the derivative equations and all subsequent constants already used the squared quantity.

The shared inspected figure plots the exact cap matrices at 60-digit precision beside the proved inequalities; its 25 radii, complete values and reproducible source are retained. The source reader also repairs three presentation defects without changing the original Markdown equations: multiple alignment columns, complete table column counts, and an equation tag inside an inner alignment.

### Source-printing observation retained with its scope

The original [Dai–Wang v1 TeX](https://arxiv.org/src/math/0703768v1), Corollary 1.4 (source lines 507–515), displays an unrooted \(L^p\) integral comparable to discrete expressions raised to \(1/p\). For a nonzero constant function multiplied by \(t>0\), its two displayed sides scale as \(t^p\) and \(t\); when \(p\ne1\), their ratio cannot be bounded above and below independently of \(t\). Thus the printed statement has that scaling defect. Replacing the left side by its \(1/p\) power repairs this necessary scaling, but this observation does not claim to reprove that corrected corollary. None of its estimates enters PS or PG; their complete constants are derived directly.

## SZ-20261011-014 — full phase response and the exact endpoint defect

[PRE1–PRE55](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_RESPONSE_AND_ENDPOINT.md) prove the full physical Poisson inverse, its actual mean and Haar mean, and the complete response matrix for the original odd phase and its generator image. All vacuum, potential and logarithmic scalars remain. Completing the exact square gives
\[
G-C_F/s=\frac{sT_F}{4\kappa}
-\frac{\kappa}{s}\mu\left|\nabla\left(F-\frac{s}{2\kappa}u_F\right)\right|^2.
\]
The complete tree-word calculation proves degree at most two along every physical edge subgroup, including tree edges and reflected words. The resulting direct energy-to-mass upper estimate has order \(j^{16}\), improving the earlier quotient of separate bounds. PRE53–PRE55 construct, within the same physical odd operator, a family with fixed mass and response but unbounded energy. This identifies precisely what those two data do not determine. All 102 checks pass. The full original endpoint remains unevaluated.

## SZ-20261011-015 — actual conditional edge entropy and a square-root score

[ESE1–ESE38](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CONDITIONAL_EDGE_ENTROPY_AND_SCORE.md) and the complete [independent derivation ID1–ID57](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/INDEPENDENT_EDGE_ENTROPY_PROOF.md) retain the full outside-path law, the terminal vacuum and every factor in the Brownian generator. Their exact terminal-preserving group transformation fixes the Girsanov sign and the directional variance. Conditioning on the outside path gives the actual edge-path entropy bound; the full path entropy retains its additional outside-marginal term.

The self-consistent time choice proves
\[
\|\nabla_e\log\psi^2\|_\infty
\le\min\{4\beta_e,C_\rho\sqrt{\beta_e}\},\quad
\beta_e=\sum_{p\ni e}|x_p|,\quad
C_\rho=2\sqrt{\frac{2\pi/c_*+4}{(1-c_*/2)^2}},\quad
c_*=\frac{\sqrt{9\pi^2+32\pi}-3\pi}{8}.
\]
This holds for every finite real source and has no volume factor. The direct original phase quotient bound improves to order \(j^{14}\), with complete coefficient \(13500000e^2C_\rho^2/\kappa_*\). ESE's 33 checks and the independent proof's 35 checks pass.

ID53–ID57 additionally prove the exact edge-marginal entropy decomposition and the sharp logarithmic-range bound
\[
\operatorname{Ent}(R/\mathbb ER)\le J(D),\qquad
J(D)=A(D)-1-\log A(D),\quad A(D)=\frac{D}{1-e^{-D}},\quad J(0)=0.
\]
The proof keeps the original lower scale of \(R\), its expectation and its two-point equality law. Substitution into the same conditional calculation gives the stated stronger finite-time inequality. These consequences make no literature novelty claim.

## SZ-20261011-016 — the all-time radius-two heat ratio

[HR1–HR25](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/HEAT_RATIO_PROOF.md) prove strict radial decrease, the exact endpoint extrema, all Gaussian-image and spectral factors, and
\[
\sup_{u,v,w}\frac{p_\tau(u,w)}{p_\tau(v,w)}
=\frac{p_\tau(0)}{p_\tau(\pi)}<e^{\pi^2/\tau},\qquad \tau>0.
\]
The coefficient \(\pi^2\) is optimal because \(\tau\log[p_\tau(0)/p_\tau(\pi)]\to\pi^2\). Short-time image signs and a separate large-time spectral bound cover the full time domain. The retained full Hamiltonian yields the one-edge logarithmic oscillation bound \(4\pi\sqrt{r_e\xi}\), at physical time \(\pi a/(2\sqrt{r_e})\). The inspected figure and 160-digit replay retain 35 series comparisons, 181 ratio samples, eight endpoint checks and three Haar integrals; the analytic proof supplies the inequalities.

The original [Baudoin–Bonnefont v1 author TeX](https://arxiv.org/src/0802.3320v1), Section 3.2, is compared with the precise generator map \(\Delta_{\rm source}=4\Delta\), time \(\tau/4\), and full Haar factor. Its first image formula is correct. Pairing its terms proves that the hyperbolic-sine sign in the immediately following second expression must be negative; HR25 gives the full correction. This bounded source correction concerns that v1 expression only. Neither the current proof nor the local-score proof uses the erroneous rewrite.

## SZ-20261011-017 — the stronger actual local score and full boundary estimates

[LS1–LS57](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SQUARE_ROOT_LOCAL_SCORE.md) combine the proved heat comparison with exact conditional stochastic differentiation to obtain
\[
\|\nabla_e\log\psi^2\|_\infty
\le\min\{4r_e\xi,(2+2\sqrt{4+2\pi})\sqrt{r_e\xi}\}.
\]
Every outside link remains in the path integral. The actual conditional and marginal densities receive both the local score and the stronger independent oscillation floor. Applying the complete earlier cap estimates strengthens the original raw odd mass lower-bound function to order \(j^{-38}\), the even mass bound to \(j^{-34}\), and the boundary positive endpoint correction to \(j^{-27}\), with every coefficient and sign given in LS49–LS57. The score comparison figure displays proved upper-bound functions, not numerical vacuum values. Original Thompson author TeX is used for the exact derivative-formula comparison with all generator, potential-sign and time factors; no external estimate constant is imported.

## SZ-20261011-018 — every bulk derivative and every inverse receiving map

[SR1–SR72](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SQUARE_ROOT_SCORE_RECEIVING_MAPS.md) propagate both independently proved scores through PS, PG, GPR, UL and UF. The complete raw masses, all boundary classes, all affine terms, actual marginal factors, face pairs, means, support labels and norm domains remain. Every positive summand has its own exact original-path exponent and coefficient; these are limits of explicit bounds, not asymptotic evaluations of unknown expectations.

The complete even bulk bound has order \(j^{-20}\); with the original endpoint factor its positive contribution has order \(j^{-25}\), strengthening the boundary-only \(j^{-27}\) calculation. The odd energy lower-bound function has order \(j^{-24}\), producing a negative correction of order \(j^{-23}\) in the corresponding upper endpoint inequality. SR34 and SR70 retain both correctly signed inequalities and all unresolved joint expectations. No conclusion is drawn by comparing these separate lower bounds.

The full six-class face calculation improves the finite face-response inverse bound from \(O(j^{40})\) to \(O(j^{32})\), with exact constants. The physical and full-labelled energy inverses retain their exponential bounds, every original Boolean factor and their distinction from the coefficient norm. The stronger slice oscillation gives the exact leading exponent coefficient \(38400\pi/\kappa_*\) at order \(j^{13}\). This is a proved improvement in these finite-volume estimates; it does not establish the continuum state, reconstruction or no-gap conclusion.

## SZ-20261011-019 — Exact rooted curvature and original phase

[CW1–CW49](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURVATURE_ROOTED_WORDS.md) retain every noncommuting transport, factor order, reflected orientation and boundary face. Signed summation of the original first row proves |u1|² ≤ W12/(2 sin² h); uniqueness and cubic symmetry of the actual vacuum give μ(W12)=μ(W)/3. Together with the retained variational bound B=min{2M,6g²√(NM)}, this yields μ(|u1|²) ≤ B/(6 sin² h) and Q4 ≤ min{16 S1² S3²,2 S3² B/(3 sin² h)}. CW28–CW32 prove the full third-row curl identity with its quadratic nonabelian remainder and a closed bound.

CW34–CW39 propagate these estimates to the original D, F, complete physical word-derivative energy and signed spectral endpoint. CW41 improves the excess of the curvature branch over the pointwise cap from j^19 to j^7, with exact coefficient 3π²κ*/1600. That branch still exceeds the cap eventually on the original path; this is a statement about proved upper-bound functions, not actual vacuum asymptotics.

CW42–CW49 give explicit original-tree configurations with W/M=O(j^-8) and F² asymptotic to [20000·2^20/(81κ*²π^6)]j^18, and show that the n^5 power in configurationwise S² ≤ C n^5 W cannot be reduced. Gauge and cube symmetry averaging preserves the curvature budget and a positive fraction of F². These are tests of what mean curvature and symmetry can imply; they are not substitute vacua. The actual joint moment and energy difference in CW39 remains to be evaluated. The smooth global interacting no-gap result remains the research goal.

Status: complete proof reviewed by owner. The portable checker passed 3,396 exact word and rational identities, plus three noncommuting original-row identities and finite coefficient/limit checks. The reproducible figure was visually inspected. This strengthens PK177 without changing its earlier valid statements; no novelty claim is made.

## SZ-20261011-020 — Ordered action, complete cubic term and source repair

[OW1–OW23](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORDERED_WILSON_ACTION.md) repair two backtracking coordinate definitions and the nonunitary Taylor-polynomial step in Chatterjee, arXiv:1602.01222v6, Section 16, equation `phiur`, source lines 1762, 1832 and 1843–1844. The source's quadratic action comparison survives: the direct ordered derivative proof gives explicit global constants and the complete cubic imaginary-trace term. Restriction to the original SU(2) generators gives Dp=|Cp|²/4+(1/4)Σ[a<b<c] ya·(yb×yc)+R4,p, with |R4,p|≤(Σ|ya|)^4/192. OW21–OW22 calculate the nonzero quartic commutator energy on the exact zero-linear-circulation space; OW23 gives the positive Taylor-product defect as a full sum of squares. Every orientation, constant and integral remainder is retained, and the full original potential and actual-vacuum receiving inequality are proved in OW16–OW17.

OW18 evaluates the sign change from exchanging two ordered factors. OW19–OW20 evaluate the complete CW42 potential and quadratic-comparison defect on the unchanged j path, including the exact negative correction coefficient −625π^4/(12κ*). These are deterministic configurations, not replacement vacua. The full electric operator and vacuum are unchanged. Source reading is bounded to the original author TeX definitions and the complete comparison proof; no free-energy theorem is imported. The 637 coefficient, orientation, source-defect, remainder and path checks passed; the reproducible figure was inspected. No novelty claim is made.

## SZ-20261011-021 — Coupled signed endpoint and even-composite energy

[AC1–AC50](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PHASE_CANCELLATION.md) retain the complete original mass–energy covariance. The actual-state enclosure AC17/AC33 uses one full finite-cutoff state, its proved overlap error and its entire signed-density variance, including the coefficient −8Σ0D in AC20. The finite-cutoff means have not been numerically evaluated, so no positive endpoint is claimed.

AC28–AC30 prove the all-physical-link quaternion degree-two map and exact Casimir decomposition with central flips, Haar integration and the full actual density drift. AC41–AC47 calculate the mixed moment μ[F²Γ(F,F)] through the full vacuum equation and the even-composite energy 〈F²ψ,(H−E0)F²ψ〉. All score, potential, scalar, harmonic-cross and mean terms remain. AC48–AC50 prove the finite-cutoff correction with its essential residual eΛ=(H−uΛ)φΛ; an exact SU(2) calibration checks that this residual term can be nonzero. The final finite polynomial formula retains every ordered edge pair and all 49 component pairs in the gradient-square moment. The available gap bound does not decide the cancellation on the original path. Owner reviewed the complete proof and replayed 120 checks; its exact-map figure was inspected.

## SZ-20261011-022 — Actual vacuum limit, Wilson representation and complete escape

[ASL1–ASL66](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_SEMIGROUP_LIMIT.md) construct one actual Hilbert ultraproduct, the positive-time semigroup, its strong zero-time projection P, a nonnegative generator on its range, and the complete nonzero escape space. ASL15 gives its exact ordered spectral-tail norm, while ASL16 retains endpoint-atom defects. Original bounded observables have the full product defect PB(I−P)CP. The original fixed finite Wilson algebra reduces P by the complete multiplier form estimate, so its compression preserves products. An actual oscillatory face multiplier proves the escape space and its unit Schwarz defect are nonzero.

ASL33–ASL38 construct actual limiting correlations, reflection-positive histories and their cyclic reconstruction. ASL64–ASL66 give one ordinary subsequence for a specified countable Wilson family at all real times including collisions. ASL46–ASL52 prove that each original orientation-average trace acts as exactly 2I on the entire cyclic space. ASL39–ASL45 retain the growing physical-loop length, all occurrence cross terms and curvature bounds; the current budget reaches its cap. ASL53–ASL63 keep the original raw phase, exact finite-norm germ domain, and all amplitude/spectral norm and correlation cross terms. Its actual raw norm and low-window weight remain unevaluated. All 37 checks passed and the complete source and figure were reviewed. These results do not identify the intended interacting four-dimensional theory.

## SZ-20261011-023 — Stronger ordered action bounds with original factors

[UR1–UR15](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORDERED_WILSON_INDEPENDENT_REVIEW.md), propagated through [OW24–OW25](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORDERED_WILSON_ACTION.md), remove the matrix-size factor from the general Hilbert–Schmidt cubic remainder: the bound is 32η³/3. The complete derivative estimate keeps the minimum of r qop^k and qHS² qop^(k−2), with all original norm definitions and ordered factors. For the original SU(2) product on the exact coordinate locus C=B=0, its action is at most |t|⁶(Σ|y|)⁶/2304. All source-path and Taylor-product corrections remain, and OW17's expectation statement explicitly requires measurable representatives with finite fourth moments; its principal chart already supplies them. The complete independent derivation and 63 checks were read and replayed. No actual-vacuum concentration on that coordinate locus is inferred.

## SZ-20261011-024 — Continuous actual Wilson histories and full-time collapse

[TR1–TR17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/WILSON_TIME_REGULARITY.md) strengthen ASL38 using the original reversible ground-state diffusion. The exact forward/backward identity retains and cancels both full logarithmic drift integrals. Its complete 2p moment estimate is (2p−1)!!(2κ*D²|t−u|)^p; an original face has D²≤4, giving fourth coefficient 192κ*². The dyadic argument proves continuous versions with every local Hölder exponent below one half and convergence of the same selected subsequence on the specified countable continuous-path space. TR17 proves the squared maximum orientation-average error on [0,T] is at most 8εj+320κ*T/(m_j²n_j), tending to zero. The full growing-loop constants remain explicit and are not uniform. The derivation was checked, with 73 independent exact heat-calibration and incidence checks; the calibration model is not substituted for the interacting vacuum. Temporal continuity does not establish spatial smoothness, a four-dimensional field or the spectral endpoint.

## SZ-20261011-025 — Physical conjugate and full actual-vacuum variance

[CV1–CV47](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CONJUGATE_VARIANCE.md) construct the exact physical soft lift with both tree-root contributions, then its divergence-free contraction B=Y(V23,u1), which preserves h=|u1|². The commutator retains its signed correction Xi and proves 4G VB≥β0²(2μh+μXi)². The full vacuum equation gives VB=(E0/κ)μh−ξμ(Wh)+(1/2)μΔh−T(3|1), with the complementary nonnegative kinetic quantity retained. CV28–CV39b compute every rooted kinetic and potential term in the double commutator and prove finite bounds. The original reflected metric and boundary products remain in CV18b.

On the unchanged path the evaluated variance bound has order j25, its curvature gain is relatively j^-7, and the full signed numerator correction remains uncontrolled at the needed scale. CV47 is the exact projection identity receiving these terms, without an assumed positive numerator. Owner read the entire proof, repaired two multiplication transcription defects in CV39/CV42 against their complete adjacent derivations, replayed the exact rooted checks and full noncommuting face Hessians, and inspected the figure. This advances the explicit conjugate calculation but does not establish the spectral endpoint.

## SZ-20261011-026 — An explicit anisotropic Wilson sequence for the original endpoint

[AT1–AT60](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ANISOTROPIC_TEMPORAL_BRIDGE.md) preserve every physical link, gauge integral, spatial face, temporal endpoint weight, Bessel multiplier, scalar energy and raw phase. AT12–AT15 give quantitative compact-kernel estimates; the joint-spectrum proof removes an unnecessary square-root edge-count factor. AT21–AT36 derive all growing-box transfer and full-phase domain constants. AT37–AT48 recover the actual vacuum from constant open-time boundary vectors, retaining the exponential denominator costs. AT49–AT58 give one explicit temporal sequence on the unchanged original path whose finite four-dimensional Wilson expectation combination differs from G_j−C_F,j/s_j by at most 3/(4j). AT60 retains the exact positive finite-difference energy defect. The endpoint sign remains unknown. All 321 checks passed; the full proof, original provider comparison and reproducible figure were reviewed.

## SZ-20261011-027 — Stronger actual Wilson path estimates

[R1–R29](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/WILSON_TIME_REVIEW.md) independently verify TR1–TR17 and strengthen their receiving bounds. The complete forward/backward identity gives exponential increments, an explicit logarithmic time modulus, and maximum coefficient 25cT/4. The full original curvature moment recurrence then proves limsup j² E sup_[0,T](2−average W_de,j)²≤27κ*²/10000. Its summable tails give limsup j sup_[0,T](2−average W_de,j)≤9κ*/100 almost surely under any specified coupling with the actual marginal path laws. No independence of faces or uniform vacuum-drift estimate is assumed. The original valid TR bounds remain, and their strengthenings are propagated to TR and ASL. All 323 check groups passed; the complete proof, source comparison and figure were reviewed.

## SZ-20261011-028 — Actual shrinking-window and positive-energy maps

[LEM1–LEM55](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_LOW_ENERGY_MAPS.md) prove the exact zero-energy flag for the original shrinking windows, its raw norm domain, its map into the cyclic reconstruction and the positive compression defect. Every fixed or moving spectral endpoint keeps its below, exact and above pieces. Full coefficient arrays for original face sums give a j^-3 positive-energy upper bound for bounded physical local quadratures, whose scalar vacuum value is not supplied by this proof. Actual physical-time detectors kill zero energy and escape while retaining every positive interval; explicit Bernstein sums recover interior weights and atoms with full error coefficients. A strictly positive finite-regulator face band retains its declining mass and both moving endpoints. The complete finite-vacuum/Duhamel and full-residual estimates are received into those same detectors. All 41 check groups passed and the full proof and figure were reviewed. No unknown limiting spectral weight is assigned a positive value.
