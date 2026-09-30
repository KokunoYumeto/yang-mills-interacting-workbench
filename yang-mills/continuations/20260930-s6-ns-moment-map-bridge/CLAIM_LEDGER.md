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
