# Bounded audit of the early and middle Yang–Mills continuations

Audit date: 16 September 2026. This is a read-only mathematical audit of the source notes listed below. No source note was edited, no Lean process was started, and no execution receipt was treated as a proof of an analytic assertion. The `mathbox:proof-audit` skill and its general logic, representation, computation, and source checklists were used. This report concerns the retained September 14–15 notes, not the strongest status of the later continuations.

## Claim card and primary verdict

**Primary verdict: proved as written for the bounded claim card in this paragraph.** For the original finite open SU(2) lattice Hamiltonian with positive spacing and coupling, smooth positive unit vacuum, original Haar measure, and derivative convention printed in the sources, the inspected conditional-expectation maps and energy identities, finite-source Schur response and residual identities, local vacuum-derivative and spin-one-sector estimates, and the stated comparison from bounded regulator-state sequences to the fixed-label reconstructed observable space have the displayed domains, signs, constants, and directions of inequality. The explicit elementary-loop Haar coefficients agree with the retained local representation decomposition. This verdict does not certify every numerical endpoint, every external analytic theorem, the geometric S6 filling theorem, any later continuation, or a four-dimensional continuum mass-gap theorem. These exclusions are specified below.

No new counterexample or concrete algebraic error was found in that bounded target. Two distinctions that would invalidate stronger conclusions are already explicitly corrected in the retained notes: escaping-label classes lie in the nonzero possible kernel `K/N`, and a chosen trial residual is not generally the canonical minimum-norm representative of its quotient class.

Objects and variance: inner products are conjugate-linear in their first entry; physical scalar functions are invariant under the original vertex gauge group; conditional score coordinates transform covariantly and are contracted using the original three generator coordinates. The finite source coefficient space has its original positive state Gram `G`, rather than an implicit identity Gram. The spectral construction uses a countable cylindrical observable family, a single common regulator subsequence, and positive times. Its target is `H_obs`, not an asserted complete four-dimensional Yang–Mills Hilbert space.

## Exact source scope

All five following research notes were read in full. Line locators in this report refer to these copied bytes, before any later source revision.

| Short name | Repository-relative source | Lines | SHA-256 |
|---|---|---:|---|
| SR | `yang-mills/continuations/20260914-spectral-reconstruction/RESEARCH_NOTE.md` | 324 | `5fffd882e97df0499263875d344f40935561106f0389077b2f832a7c3c568ba0` |
| VR | `yang-mills/continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md` | 549 | `0874d0d59e0fecec8d5fcd88b33918515e635fe22c27b3bd56ae0b3c4cb782c0` |
| RC | `yang-mills/research-control/RESEARCH_NOTE.md` | 249 | `67454e30bc6a0a5f24ef2b63aac16ea05cd4b9fcc087688d351f7b0191a016ec` |
| CR | `yang-mills/continuations/20260914-coupled-response/RESEARCH_NOTE.md` | 218 | `b787a444d6c3995ac39fbc71a4f114478cad824172c40e33a32930661a771433` |
| AM | `yang-mills/continuations/20260915-actual-loop-moments/RESEARCH_NOTE.md` | 981 | `0ac4afbec39b2e878d5555af85a86803d9ba6ac5505dc7817f231e5533c0dd2b` |

Additional targeted source reads were the finite-box primary note, `yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`, lines 1–175, and the local S6 frozen companion, `s6/27_s6_key_advances_frozen_2026-09-06.tex`, especially lines 138–195. For the literal deck-action check, the local full-source export `private intake/S6_CURRENT_FULL_TEX_FOR_AI_20260906_SPECTRAL_UMBRAL_FINAL.md` was read at lines 112246–112274, 112423–112427, and 112625–112645. The finite-box weak-coupling asymptotics after the initial source region were not audited. No `.mathbox` ledger exists at this consolidation root.

## Dependency graph

1. Original compact-product SU(2) Hamiltonian, gauge action, and positive vacuum → multiplication by `psi` is unitary between the actual vacuum-weighted and Haar Hilbert spaces → exact ground-state Dirichlet form. The primary note lines 17–51 gives the initial domain and positivity argument; RC L1 and AM A2 retain the same constants.
2. Ordered edge-product map plus its explicit last-link inverse → Haar factorization → actual vacuum marginal `m`, pullback `J`, conditional expectation `E=J*`, and `EJ=I` → horizontal derivative identity with the score `S` → VR (3.11), RC L13–15, and exact minimum-energy sections RC L17–25.
3. Closed restriction of that original form to `ker E` → nonnegative self-adjoint `D` → raw-`G` block form CR C4–5 → Schur response CR C7–12 → exact residual square CR C16 → two-sided finite-source response/metric enclosures and the singular normal-equation fibres CR C20–22.
4. Actual logarithmic-vacuum equation AM A2 → differentiated equation A3 → pointwise bound A5 and integrated identity A6 → covariant inverse A9 on the explicitly typed spin-one sector → actual local remainder A13–14 → neighboring-plaquette Haar decomposition A28–33 → quantitative return to the actual weighted measure and conditional `D` in A34–45.
5. Uniform bounded-observable spectral estimates → common positive-time kernel subsequence → semigroup on the exact kernel quotient → `H_obs`, `A_obs`, and their matrix measure → spectral-support and Laplace-edge identities. Regulator-state sequences map onto this space through VR (6.1), and the exact source-kernel quotient is VR (6.3), not an injectivity inference from finite-level density.

The general spectral theorem, compact-manifold elliptic regularity/maximum principle, representation of closed nonnegative forms, Riesz representation, and polynomial approximation are standard analytic leaves invoked by the sources. Their applications were checked for the relevant positivity, compactness, domains, and finiteness here; this audit did not reprove those general theorems or perform a new literature audit. The S6 global geometric filling construction and the historical Split Zero/arithmetic constructions are external provenance leaves, not premises supplying a missing Yang–Mills inequality: the actual linear maps needed in these notes are written and checked locally.

## Obligation matrix

| Obligation | Status | Exact locus and finding |
|---|---|---|
| Common subsequence and positive-time derivative estimate | passed | SR 23–60. `sup` over the spectrum is bounded by the nonnegative half-line supremum; the latter is not falsely stated as the former. |
| Semigroup descends through the exact nullspace, is a positive contraction, and is strongly continuous | passed | SR 64–104. The finite-regulator quadratic forms give each property; the expanded proof is recorded below. |
| Spectral-support equality and diagonal Laplace edge | passed | SR 106–119 and 225–259, for the nonzero diagonal measures specified there. A zero diagonal contributes no support; the zero observable space has no positive-gap assertion. |
| Complex matrix Stieltjes inversion | passed | SR 201–221. The actual matrix imaginary part `(R-R*)/(2i)` retains complex off-diagonal entries. |
| Escaping-label inference | passed after the already-integrated correction | SR 261; VR 457–543. The notes now retain an explicit nonzero possible kernel `K/N`. |
| Smooth finite-link holonomy section and curvature coefficient | passed | VR 76–125. Disjoint ordered supports give `exp(K0)exp(K)=U`; the transverse derivative and volume powers leave exactly `J_chi/a_r`. |
| Vacuum marginal, horizontal fields, and score square | passed | VR 129–279 and RC L6–16. Prefix dependence is retained; coefficients are independent of the differentiated link, and all density and energy cross terms remain. |
| Closed kernel form and minimum-energy section | passed | RC 157–225. Smoothness and H1 continuity are only asserted at each finite regulator; the actual induced middle form is used in composition. |
| Raw-Gram block self-adjointness and response metric | passed | CR C4–12. The finite off-diagonal map is bounded; the source adjoint is `i*(x,h)=Gx`, giving `G F(z)^(-1) G`. |
| Singular moment coefficient fibres | passed | CR C20–22. `ker H_d=ker Z_d`, compatibility of `B_d`, and independence of the state `Y_d` from the coefficient solution are proved. |
| All-coupling vacuum derivative and covariant inverse | passed | AM A3–9. The inverse is on the spin-one gauge-Casimir sector; it is not assigned to its invariant contraction without a product-rule calculation. |
| Local neighboring-loop Haar coefficients | passed | AM A28–33 and A39–40. Shared-path singlet/triplet channels and unmatched-edge cancellations give the displayed coefficients. |
| Return from Haar coefficients to actual response | passed | AM A24–38 and A43–45. The actual conditional density and the `Q`-projection errors are retained. |
| Trial residual equals canonical quotient norm without a section correction | failed as a general assertion; corrected in the inspected source | AM A45a, lines 761–798, explicitly writes the extra nonnegative term `a_Y |alpha_Y-1|^2`; no such false identification is used in the retained conclusion. |
| Exact rational endpoint code and archived execution receipts | out of scope for this audit | AM A46–47, A49 radii, and the checker claims at 934–965 were read, but their programs/receipts were not independently replayed here. |
| Later zero-shift, gauge-native, uniform-gap, volume-limit, cubic, and linearized proofs | out of scope | These are later branches of the consolidated result history and are not downgraded by an earlier note's historical `next task` paragraph. |
| Four-dimensional continuum identification or physical continuum mass lower edge | not addressed by the audited contribution | The sources explicitly do not assert these conclusions. This is not a newly imposed proof obligation or an inferred theorem. |

## Decisive checks and exact maps

### 1. Positive-time reconstruction and escaping states

For a finite symbol sum `z=sum c_a[i_a,s_a]`, take its exact finite-regulator counterpart `z_n=sum c_a exp(-s_a A_n)r_(i_a,n)`. Its limiting squared norm is the displayed kernel quadratic form. At the regulator,

`||exp(-u A_n)z_n||^2 <= ||z_n||^2`,

`<z_n,exp(-u A_n)z_n> >= 0`,

and the semigroup is self-adjoint. Passing these inequalities to the common subsequence proves that the symbol shift descends through null vectors to a positive self-adjoint contraction. For each symbol its difference norm at `u=0` is

`C_ii(2s+2u)-2 C_ii(2s+u)+C_ii(2s)`,

which tends to zero by positive-time continuity. Finite sums and the contraction bound extend this to strong continuity on the completion. The bounded diagonal kernels then imply a finite zero-time norm and the Cauchy property of `[i,s]` as `s↓0`. This fills the semigroup details condensed into SR line 76 without altering any source definition.

VR (6.1) has source the vector space of norm-bounded regulator-state sequences for which all fixed rational-positive-time symbol pairings converge. Its target vector is the Riesz representative of those limits. Its exact kernel is `K`, the vanishing-pairing sequences. The diagonal lifting construction in VR line 486 proves surjectivity and produces a lift with norm tending to the target norm. Consequently the map on the two printed cochain windows has kernel `K/N`, where `N` consists of sequences whose norms tend to zero. These are algebraic quotient statements; the source does not silently assert an isometry from every regulator-state class.

For the literal test `v_n=chi_{ {n} }` in VR (6.4)–(6.6), the finite norm is one and energy is `1/n`, but every fixed Walsh label is eventually orthogonal to `v_n`. The fixed-label limiting generator has eigenvalues `|S|` for nonempty finite `S`, hence bottom one. This is a complete counterexample to the earlier unrestricted escaping-state inference and a valid nonzero element of `K/N`. SR line 261 now links to exactly this correction. The early error must not be reported as an unfixed claim in the consolidated SR note.

### 2. Literal retained deck action

VR lines 52–72 print `gamma(Lambda)⊂Z`, `gamma A=gamma`, `gamma(v)=epsilon∈{±1}`, `zeta=exp(-2pi i/m)`, and the total-line action generated by

`(x,z) -> (x+lambda,z)` and `(x,z) -> (Ax+v/m,zeta z)`.

For this literal action, with `H(x)=exp(-2pi i epsilon gamma(x))`,

`H(x+lambda)/H(x)=exp(-2pi i epsilon gamma(lambda))=1`,

`H(Ax+v/m)/H(x)=exp(-2pi i epsilon^2/m)=zeta`.

Therefore `z/H(x)` is invariant under both generators, and the inverse `([x],w)->[x,wH(x)]` is well-defined because replacing `x` by `Ax+v/m` multiplies its fibre value by precisely `zeta`. Both compositions are the identity. The local S6 companion lines 183–193 prints the same equivariance and the same maps. No inverse sign error occurs for the action actually retained here.

The literal cover action was also checked beyond that companion. In the full-source export named above, the embedded `finite_filling_certificates.tex` FF24–25, lines 112254–112274, retains the varying map

`Ghat(z,zeta)=(g_j z,R_(g_j)(z) zeta+Pi(g_j z)v_j/m_j)`

and covariance `R_(g_j)(z)Pi(z)=Pi(g_j z)A_j`. Hence the marking `Xi(z,x)=(z,Pi(z)x)` conjugates it to `(g_j z,A_jx+v_j/m_j)`. FF32, lines 112423–112427, prints the actual marked-cover action `(s,x)->(zeta_j s,A_jx+v_j/m_j)`. Passing its derivative to the tangent-space quotient normal to `s=0` multiplies that quotient by `zeta_j`, giving exactly FF42, lines 112625–112632, and the normal action used in VR. FF43, lines 112634–112645, explicitly explains that the positive section-character exponent corresponds to this quotient, whereas its negative describes the dual normal line.

Under the additional frame change `w=n/H_j(x)`, the action becomes `(x,w)->(A_jx+v_j/m_j,w)`. Its fibre multiplier disappears by that exact conjugation; the matrix `A_j` remains. A translation-only formula in the original unchanged normal coordinate would therefore be a different action, not a justification of the displayed descent. No such conflicting action was found in the inspected passages. This check proves the actual action-to-normal-quotient-to-smooth-frame morphisms; it does not certify all global geometric statements about the S6 filling or claim holomorphic triviality.

### 3. Score coupling and finite-source response

For the ordered refinement map, differentiation in fine link `j` gives `X_(j,beta) Jg=sum_alpha a_(j;alpha,beta) J X_alpha g`. Orthogonality of the retained adjoint matrices yields `Y_alpha Jg=J X_alpha g`. Their own-link independence makes the horizontal field divergence-free. Integration by parts first at `f=1` identifies the conditional mean of `Y log rho`; at general `f` it gives `X Ef=E Yf+E(fS)`. For `h=f-JEf`, this gives `E Yh=-E(hS)` and therefore exactly the three nonnegative squares in VR (3.11), with coefficient `kappa_n b`. In particular the mixed sign in RC L13 and CR C4 is negative.

In CR the raw coefficient pairing is `x*G y`, so the printed block operator is `H_F(x,h)=(G^(-1)(K0 x-W*h),Dh-Wx)`. Eliminating the second component gives `F(z)=K0-zG-W*(D-z)^(-1)W`, with the first-component inverse `F(z)^(-1)G`. Multiplying by the actual source adjoint on the left gives exactly `G F(z)^(-1)G`. The mixed-parameter resolvent identity gives `-(F(z)-F(w)*)/(z-conj(w))=L_w*L_z`, preserving the source Gram.

For an actual trial map `Y`, expansion with `R=W-(D+s)Y` gives

`R*(D+s)^(-1)R = M_s-W*Y-Y*W+Y*(D+s)Y`.

This proves C16 and both directions of C17. In C22 the cross moment is necessarily `N_(i+1)+s N_i`, not the unshifted `N_(i+1)`. The source's attempts record already identifies this repair. Singular `H_d` causes no gap: its nullspace equals `ker Z_d`, and every forcing column is orthogonal to it, so every normal-equation solution produces the same actual `Y_d`.

### 4. Vacuum derivative and local response constants

AM A3 follows by differentiating the full logarithmic-vacuum equation: the Casimir commutes with `X_(e,alpha)`, and the extra first-derivative commutator contracts an antisymmetric epsilon tensor against the symmetric product of the gradient components. At a maximum of `|X_e u|^2`, the squared antisymmetric part of the same-link second-derivative matrix contributes `|X_e u|^2/2`; `|X_e V|<=v r_e` then gives `|X_e u|<=2r_e xi`. This proves A5 with the stated all-coupling domain.

The spin-one-sector estimate has its actual source and target: the vertex gauge-Casimir equals two on `E_v`, while the pointwise sum-of-generators inequality gives `sum |G_v h|^2<=d_v sum_(e incident v)|X_e h|^2`. After integration in the gauge-invariant vacuum measure, `q_A(h)>=2 kappa ||h||^2/d_v`. Thus A9 is valid on `E_v`; the invariant contraction is a different vector whose product derivatives are explicitly calculated in A22–23 and A35. No physical-sector gap follows solely from A9.

In AM A28–30, every shared-path contraction has singlet norm `9/64` and triplet norm `3/64`; the unshared links contribute `nu_p=3(ell+4-2s_p)/4`, while the triplet adds `2s_p`. For `ell=4`, twelve faces have `s_p=1`, hence

`c_j=12 [3(9/2)^j+(13/2)^j]/48`,

which gives `(c0,c1,c2)=(1,5,103/4)`. The trial coefficients `4/33` and `4/45` are exactly `(2/3)/(9/2+1)` and `(2/3)/(13/2+1)`. Thus `(K+1)Z=(2/3)J`, and its two Haar pairings are the printed `28/165` and `796/27225`.

The density comparison is with the actual interacting local marginal and conditional fibre, not a replacement of the vacuum by Haar measure. The pointwise bound is integrated along paths of length `2pi` per ordinary link and `4pi` for each free loop-chain coordinate at fixed product; this gives precisely the exponents `32pi d xi` and `32pi(d+ell-2)xi`. These enter A36–38 and A42–45, including the conditional projection terms.

For the canonical-residual distinction, let `a_Y=<Y,(D+kappa)Y>`, `c_Y=<Y,W>`, and `alpha_Y=c_Y/a_Y`. Then `R_can=W-(D+kappa)alpha_Y Y` is orthogonal to `(D+kappa)Y` in the dual pairing. Consequently

`<R,(D+kappa)^(-1)R> = ||[W]||_dual^2 + a_Y |alpha_Y-1|^2`.

AM A45a retains this exact term. A45 is a valid enclosure from the chosen trial residual without identifying that residual with the minimizing one.

## Remaining scope and consolidation consequence

There is no newly isolated missing algebraic implication in the bounded claim card. The sources expressly leave the continuum physical identification unresolved; an audit of these earlier notes must not replace the later current results by those historical status paragraphs. Conversely, the named later notes cannot be certified by this audit merely because they were imported in the same consolidation.

The strongest safe consolidation statement from this pass is: these retained early and middle notes provide an exact chain of vacuum-weighted refinement, response, residual, spectral reconstruction, and local Wilson-loop estimates in their printed domains; the explicit escaping-state and noncanonical-residual corrections are present and should be linked from the cumulative result history. The numerical certificates remain claims with separate executable verification evidence until the dedicated replay pass checks them. The prescribed continuum path has `xi_n=(g0^(-2)+beta n log 2)^2/4`, so the small-`xi` elementary-loop intervals must retain their coupling domain rather than be extrapolated along that path.

The cheapest follow-up checks are the already separate standard-library checker replay and the later-continuation audit; no Lean run or new research theorem is required by this bounded consolidation audit.

## Commands and audit provenance

Source discovery used `rg --files` and `rg -n` over the named continuation paths; complete reads used `Get-Content` with numbered lines; source pins used `Get-FileHash -Algorithm SHA256`. The first file-discovery call omitted the existing `yang-mills/` path component and returned only path errors; it read or modified no source. One PowerShell hash-list command had a parser error from a pipeline after `foreach`; the corrected read-only command produced the hashes above. These failures are not execution receipts for any proof checker.

A separate bounded subagent checked the printed S6 equivariance and quotient inverse, then located the full-source FF24–25, FF32, and FF42–43 passages. Those exact passages were subsequently read by this audit agent. That is an additional derivation of the action calculation, not a certificate of every S6 global geometric statement. No checker program was executed by this audit agent, and no broad external literature search was performed.
