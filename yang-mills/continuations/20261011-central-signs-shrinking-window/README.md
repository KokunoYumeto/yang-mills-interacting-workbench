# Yang–Mills phase moments and central link symmetry

This continuation calculates the original polynomial phase observable in the actual interacting vacuum, improves its bound on the prescribed growing-box path, and completes the odd-order Jacobian return calculation. It belongs to the S6 and Navier–Stokes inspired Yang–Mills programme.

The original path remains \(L_j=j^4\), \(a_j=1/(100j)\), \(g_j^2=\kappa_*/(200j)\), with window \(s_j=\kappa_*/j\). Its actual positive low-energy weight and the interacting continuum no-gap result remain to be established.

- [Original phase moments and the unchanged shrinking window](PHASE_MOMENTS_AND_ORIGINAL_PATH.md), IP1–IP22: exact original-word occurrence sums improve the negative loss bound from order \(j^{31}\) to order \(j^{23}\). The actual vacuum equation gives all potential moments and controls unbounded polynomial multipliers at each fixed box. The original \(x-y\) vector has limiting raw norm squared \(12\), first energy moment \(12\delta_*\), fourth moment \(720\), and first odd-cluster weight \(12\). All polynomial Gram and energy limits are evaluated, with their exact degenerating rank.
- [All odd Schur coefficients and the complete even tail](ORIGINAL_J5_PARITY_AND_TAIL.md), P1–P45: an explicit central-sign involution preserves every original gauge constraint, spin block and union label. Each odd-degree face-return word is zero. The full complementary inverse, even remainder, original vacuum scalar and full nonlinear interior inverse have proved bounds.
- [Central signs and the exact boundary obstruction](CENTRAL_SIGNS_AND_BOUNDARIES.md), CS1–CS19: every open box has one physical face-reversing sign map. A periodic rectangular box admits these maps exactly when at most one side length is odd; its eight central gauge classes retain the three winding signs. The full Hamiltonian identity includes \(4\kappa M\xi I\).
- [Original first Jacobian block and return](BASELINE_J5.md), J1–J7: preserved complete provider for the outgoing channels and second coefficient. Its formerly unfinished third coefficient is settled in P26.

The fixed-box phase limit cannot yet be exchanged with the specified joint path: IP22 retains an explicit tail coefficient growing as \((35831808/\pi^4)n^{12}\). The improved joint-path lower bound still has a negative endpoint. Neither statement supplies the missing positive limiting weight.

The center-reversal mechanism has an antecedent in [L. Li and Y. Meurice, Lattice gluodynamics at negative \(g^2\)](https://arxiv.org/abs/hep-lat/0410029v2). The proofs give the exact comparison to their conventions and preserve the scope of their periodic construction. No novelty claim is made.

[Complete combined TeX source](RESEARCH_CONTINUATION.tex) retains every mathematical block from the listed proof sources and their independent certificates. Compilation of this source edition is pending. The [source-fidelity record](TEX_FIDELITY.json) records the verified source identities; no new PDF is represented as compiled.

Reproduce the independent finite checks with Python, using mpmath for the phase enumeration: check_central_signs.py, verify_phase.py, and verify_jacobian.py. The nine exact incidence cases, 32 phase checks, and rational Jacobian certificates supplement the complete proofs. All displayed figures have retained reproducible sources. [Source identities and reading coverage](SOURCE_READING_USE_LEDGER.json) and [claim propagation](CLAIM_LEDGER.md) accompany this edition.

The next direct spectral calculation is a volume-dependent estimate of the actual reflected four-loop and gradient difference with accuracy sufficient for division by \(s_j\). The fourth coefficient is now evaluated; the full physical inverse beyond the small-source region is proved in the global continuation below. These are distinct calculations within the continuing programme.

## Complete fixed-box spectral weights

The [spectral continuation](PHASE_SPECTRAL_WEIGHTS.md), SP1–SP16, evaluates every limiting cluster-weight matrix for the original polynomial family by a finite Hermite sum and a full determinant formula. It proves convergence of the corresponding actual fixed-box spectral measures. For the original cubic vector the raw weights are 2700, 2160 and 1440 at the three energies δ*, 2δ* and 3δ*. The original two-dimensional phase compression has an exact omitted energy contribution 864δ*²; the minimal invariant oscillator space includes the radial polynomial uq. The 12δ*/5 variational value is accounted for by its two occupied energies. The simultaneous growing-box estimate is still required.

The [104 exact checks](PHASE_SPECTRAL_CHECKS.json) compare independent Hermite, determinant and moment calculations. [Reproducible spectral figure](PHASE_SPECTRAL_WEIGHTS.png) shows all raw masses, with its source retained.

## Original joint-path and fourth-return continuation

The [complete reflection calculation](BOUNDARY_REFLECTION_AND_RAW_ENDPOINT.md), JP1–JP49, proves the global two-link bounds and the exact original endpoint. The [fourth-return proof](fourth_return/FOURTH_SCHUR_COEFFICIENT.md), Q1–Q50, evaluates the full original coefficient and the physical-response map. The [illustrations](BOUNDARY_AND_FOURTH_ILLUSTRATIONS.md) show the exact coordinate geometry, harmonic components and boundary entries.

Run `verify_boundary_reflection.py` for its 66 checks and `fourth_return/verify_fourth_return.py` for the seven independent exact replay scripts. The latter uses only the retained local sources and Python's standard library. `fourth_return/PORTABLE_REPLAY.json` lists every dependency. The [result and claim ledger](RESULTS_20261011.md) records precise scope and propagation.

## Global physical source and expectation maps

[GPR1–GPR55](GLOBAL_PHYSICAL_RESPONSE.md) establish the exact physical source inverse and the original assembly-quotient inverse at every finite real source. The Wilson expectation map covers the interior of the full finite-box Wilson convex image with a unique analytic inverse. Two-link conditional averaging gives the complete original-path inverse susceptibility bound O(j⁴⁰). The [figure](GLOBAL_PHYSICAL_RESPONSE.png) shows the actual operators and Haar averaging map. Run `check_global_response.py` with SymPy for the exact trace, Gram, constant and polynomial-degree checks; the complete proof is retained alongside them.

## Polynomial bounds in the actual vacuum

[PC1–PC52](POLYNOMIAL_CONDITIONAL_BOUNDS.md) prove the full degree-two score comparison, an explicit smooth family attaining its exponent, the sharper colour-vector bound, and the exact receiving-link optimization inside the original phase. The resulting actual-vacuum bounds replace exponential losses by powers. [The inspected illustration](POLYNOMIAL_CONDITIONAL_BOUNDS.png) includes reproducible numerical quadrature of the proved sharpness family, identified separately from the physical vacuum. Run `verify_polynomial_conditional.py` with SymPy and mpmath for the 21 recorded checks.

## Full labels, inverse and connected vacuum supports

[UL1–UL47](union_label_global/FULL_UNION_LABEL_INVERSE.md) prove the full inverse at every finite real source, including all assembly relation directions. [UF1–UF17](SUPPORT_AND_SCALAR_FACTORIZATION.md) prove the exact connected-support property of the vacuum and all its scalar families, and a stronger transformation bound. The complete original Hamiltonians, labels, means and coupling factors are retained. [The inspected diagram](FULL_UNION_LABEL_INVERSE.png) displays the inverse and a seven-edge adjacent-face calculation. Run `union_label_global/check_union.py` and `check_support_factorization.py` to replay the finite exact certificates; the full analytical arguments are in the linked proofs.

## Complete cap and gradient estimates

[PS1–PS76](POLYNOMIAL_SCORE_AND_ORIGINAL_ENDPOINT.md) give exact cap Gram blocks, explicit optimal exponents for the full polynomial and special-vector classes, and all selected boundary derivative sums. [PG1–PG70](POLYNOMIAL_GRADIENT_BOUNDS.md) give the complete gradient inequality, every original bulk derivative and their disjoint addition to the boundary energies. Full constants, affine terms, actual-vacuum score maps and both signed endpoint inequalities remain visible. [The matrix figure](CAP_GRAM_COMPARISON.png) has reproducible 60-digit data. Run `cap_constants.py`, `verify_symbolic_geometry.py` and `verify_polynomial_gradient.py` for the retained checks.

## Actual-vacuum score and complete receiving maps

## SZ-20261011-014 — full phase response and the exact endpoint defect

[PRE1–PRE55](PHASE_RESPONSE_AND_ENDPOINT.md) prove the full physical Poisson inverse, its actual mean and Haar mean, and the complete response matrix for the original odd phase and its generator image. All vacuum, potential and logarithmic scalars remain. Completing the exact square gives
\[
G-C_F/s=\frac{sT_F}{4\kappa}
-\frac{\kappa}{s}\mu\left|\nabla\left(F-\frac{s}{2\kappa}u_F\right)\right|^2.
\]
The complete tree-word calculation proves degree at most two along every physical edge subgroup, including tree edges and reflected words. The resulting direct energy-to-mass upper estimate has order \(j^{16}\), improving the earlier quotient of separate bounds. PRE53–PRE55 construct, within the same physical odd operator, a family with fixed mass and response but unbounded energy. This identifies precisely what those two data do not determine. All 102 checks pass. The full original endpoint remains unevaluated.

## SZ-20261011-015 — actual conditional edge entropy and a square-root score

[ESE1–ESE38](CONDITIONAL_EDGE_ENTROPY_AND_SCORE.md) and the complete [independent derivation ID1–ID57](INDEPENDENT_EDGE_ENTROPY_PROOF.md) retain the full outside-path law, the terminal vacuum and every factor in the Brownian generator. Their exact terminal-preserving group transformation fixes the Girsanov sign and the directional variance. Conditioning on the outside path gives the actual edge-path entropy bound; the full path entropy retains its additional outside-marginal term.

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

[HR1–HR25](HEAT_RATIO_PROOF.md) prove strict radial decrease, the exact endpoint extrema, all Gaussian-image and spectral factors, and
\[
\sup_{u,v,w}\frac{p_\tau(u,w)}{p_\tau(v,w)}
=\frac{p_\tau(0)}{p_\tau(\pi)}<e^{\pi^2/\tau},\qquad \tau>0.
\]
The coefficient \(\pi^2\) is optimal because \(\tau\log[p_\tau(0)/p_\tau(\pi)]\to\pi^2\). Short-time image signs and a separate large-time spectral bound cover the full time domain. The retained full Hamiltonian yields the one-edge logarithmic oscillation bound \(4\pi\sqrt{r_e\xi}\), at physical time \(\pi a/(2\sqrt{r_e})\). The inspected figure and 160-digit replay retain 35 series comparisons, 181 ratio samples, eight endpoint checks and three Haar integrals; the analytic proof supplies the inequalities.

The original [Baudoin–Bonnefont v1 author TeX](https://arxiv.org/src/0802.3320v1), Section 3.2, is compared with the precise generator map \(\Delta_{\rm source}=4\Delta\), time \(\tau/4\), and full Haar factor. Its first image formula is correct. Pairing its terms proves that the hyperbolic-sine sign in the immediately following second expression must be negative; HR25 gives the full correction. This bounded source correction concerns that v1 expression only. Neither the current proof nor the local-score proof uses the erroneous rewrite.

## SZ-20261011-017 — the stronger actual local score and full boundary estimates

[LS1–LS57](SQUARE_ROOT_LOCAL_SCORE.md) combine the proved heat comparison with exact conditional stochastic differentiation to obtain
\[
\|\nabla_e\log\psi^2\|_\infty
\le\min\{4r_e\xi,(2+2\sqrt{4+2\pi})\sqrt{r_e\xi}\}.
\]
Every outside link remains in the path integral. The actual conditional and marginal densities receive both the local score and the stronger independent oscillation floor. Applying the complete earlier cap estimates strengthens the original raw odd mass lower-bound function to order \(j^{-38}\), the even mass bound to \(j^{-34}\), and the boundary positive endpoint correction to \(j^{-27}\), with every coefficient and sign given in LS49–LS57. The score comparison figure displays proved upper-bound functions, not numerical vacuum values. Original Thompson author TeX is used for the exact derivative-formula comparison with all generator, potential-sign and time factors; no external estimate constant is imported.

## SZ-20261011-018 — every bulk derivative and every inverse receiving map

[SR1–SR72](SQUARE_ROOT_SCORE_RECEIVING_MAPS.md) propagate both independently proved scores through PS, PG, GPR, UL and UF. The complete raw masses, all boundary classes, all affine terms, actual marginal factors, face pairs, means, support labels and norm domains remain. Every positive summand has its own exact original-path exponent and coefficient; these are limits of explicit bounds, not asymptotic evaluations of unknown expectations.

The complete even bulk bound has order \(j^{-20}\); with the original endpoint factor its positive contribution has order \(j^{-25}\), strengthening the boundary-only \(j^{-27}\) calculation. The odd energy lower-bound function has order \(j^{-24}\), producing a negative correction of order \(j^{-23}\) in the corresponding upper endpoint inequality. SR34 and SR70 retain both correctly signed inequalities and all unresolved joint expectations. No conclusion is drawn by comparing these separate lower bounds.

The full six-class face calculation improves the finite face-response inverse bound from \(O(j^{40})\) to \(O(j^{32})\), with exact constants. The physical and full-labelled energy inverses retain their exponential bounds, every original Boolean factor and their distinction from the coefficient norm. The stronger slice oscillation gives the exact leading exponent coefficient \(38400\pi/\kappa_*\) at order \(j^{13}\). This is a proved improvement in these finite-volume estimates; it does not establish the continuum state, reconstruction or no-gap conclusion.

## SZ-20261011-019 — Exact rooted curvature and original phase

[CW1–CW49](CURVATURE_ROOTED_WORDS.md) retain every noncommuting transport, factor order, reflected orientation and boundary face. Signed summation of the original first row proves |u1|² ≤ W12/(2 sin² h); uniqueness and cubic symmetry of the actual vacuum give μ(W12)=μ(W)/3. Together with the retained variational bound B=min{2M,6g²√(NM)}, this yields μ(|u1|²) ≤ B/(6 sin² h) and Q4 ≤ min{16 S1² S3²,2 S3² B/(3 sin² h)}. CW28–CW32 prove the full third-row curl identity with its quadratic nonabelian remainder and a closed bound.

CW34–CW39 propagate these estimates to the original D, F, complete physical word-derivative energy and signed spectral endpoint. CW41 improves the excess of the curvature branch over the pointwise cap from j^19 to j^7, with exact coefficient 3π²κ*/1600. That branch still exceeds the cap eventually on the original path; this is a statement about proved upper-bound functions, not actual vacuum asymptotics.

CW42–CW49 give explicit original-tree configurations with W/M=O(j^-8) and F² asymptotic to [20000·2^20/(81κ*²π^6)]j^18, and show that the n^5 power in configurationwise S² ≤ C n^5 W cannot be reduced. Gauge and cube symmetry averaging preserves the curvature budget and a positive fraction of F². These are tests of what mean curvature and symmetry can imply; they are not substitute vacua. The actual joint moment and energy difference in CW39 remains to be evaluated. The smooth global interacting no-gap result remains the research goal.

Status: complete proof reviewed by owner. The portable checker passed 3,396 exact word and rational identities, plus three noncommuting original-row identities and finite coefficient/limit checks. The reproducible figure was visually inspected. This strengthens PK177 without changing its earlier valid statements; no novelty claim is made.

## SZ-20261011-020 — Ordered action, complete cubic term and source repair

[OW1–OW23](ORDERED_WILSON_ACTION.md) repair two backtracking coordinate definitions and the nonunitary Taylor-polynomial step in Chatterjee, arXiv:1602.01222v6, Section 16, equation `phiur`, source lines 1762, 1832 and 1843–1844. The source's quadratic action comparison survives: the direct ordered derivative proof gives explicit global constants and the complete cubic imaginary-trace term. Restriction to the original SU(2) generators gives Dp=|Cp|²/4+(1/4)Σ[a<b<c] ya·(yb×yc)+R4,p, with |R4,p|≤(Σ|ya|)^4/192. OW21–OW22 calculate the nonzero quartic commutator energy on the exact zero-linear-circulation space; OW23 gives the positive Taylor-product defect as a full sum of squares. Every orientation, constant and integral remainder is retained, and the full original potential and actual-vacuum receiving inequality are proved in OW16–OW17.

OW18 evaluates the sign change from exchanging two ordered factors. OW19–OW20 evaluate the complete CW42 potential and quadratic-comparison defect on the unchanged j path, including the exact negative correction coefficient −625π^4/(12κ*). These are deterministic configurations, not replacement vacua. The full electric operator and vacuum are unchanged. Source reading is bounded to the original author TeX definitions and the complete comparison proof; no free-energy theorem is imported. The 637 coefficient, orientation, source-defect, remainder and path checks passed; the reproducible figure was inspected. No novelty claim is made.

## SZ-20261011-021 — Coupled signed endpoint and even-composite energy

[AC1–AC50](ACTUAL_PHASE_CANCELLATION.md) retain the complete original mass–energy covariance. The actual-state enclosure AC17/AC33 uses one full finite-cutoff state, its proved overlap error and its entire signed-density variance, including the coefficient −8Σ0D in AC20. The finite-cutoff means have not been numerically evaluated, so no positive endpoint is claimed.

AC28–AC30 prove the all-physical-link quaternion degree-two map and exact Casimir decomposition with central flips, Haar integration and the full actual density drift. AC41–AC47 calculate the mixed moment μ[F²Γ(F,F)] through the full vacuum equation and the even-composite energy 〈F²ψ,(H−E0)F²ψ〉. All score, potential, scalar, harmonic-cross and mean terms remain. AC48–AC50 prove the finite-cutoff correction with its essential residual eΛ=(H−uΛ)φΛ; an exact SU(2) calibration checks that this residual term can be nonzero. The final finite polynomial formula retains every ordered edge pair and all 49 component pairs in the gradient-square moment. The available gap bound does not decide the cancellation on the original path. Owner reviewed the complete proof and replayed 120 checks; its exact-map figure was inspected.

## SZ-20261011-022 — Actual vacuum limit, Wilson representation and complete escape

[ASL1–ASL66](ACTUAL_SEMIGROUP_LIMIT.md) construct one actual Hilbert ultraproduct, the positive-time semigroup, its strong zero-time projection P, a nonnegative generator on its range, and the complete nonzero escape space. ASL15 gives its exact ordered spectral-tail norm, while ASL16 retains endpoint-atom defects. Original bounded observables have the full product defect PB(I−P)CP. The original fixed finite Wilson algebra reduces P by the complete multiplier form estimate, so its compression preserves products. An actual oscillatory face multiplier proves the escape space and its unit Schwarz defect are nonzero.

ASL33–ASL38 construct actual limiting correlations, reflection-positive histories and their cyclic reconstruction. ASL64–ASL66 give one ordinary subsequence for a specified countable Wilson family at all real times including collisions. ASL46–ASL52 prove that each original orientation-average trace acts as exactly 2I on the entire cyclic space. ASL39–ASL45 retain the growing physical-loop length, all occurrence cross terms and curvature bounds; the current budget reaches its cap. ASL53–ASL63 keep the original raw phase, exact finite-norm germ domain, and all amplitude/spectral norm and correlation cross terms. Its actual raw norm and low-window weight remain unevaluated. All 37 checks passed and the complete source and figure were reviewed. These results do not identify the intended interacting four-dimensional theory.

## SZ-20261011-023 — Stronger ordered action bounds with original factors

[UR1–UR15](ORDERED_WILSON_INDEPENDENT_REVIEW.md), propagated through [OW24–OW25](ORDERED_WILSON_ACTION.md), remove the matrix-size factor from the general Hilbert–Schmidt cubic remainder: the bound is 32η³/3. The complete derivative estimate keeps the minimum of r qop^k and qHS² qop^(k−2), with all original norm definitions and ordered factors. For the original SU(2) product on the exact coordinate locus C=B=0, its action is at most |t|⁶(Σ|y|)⁶/2304. All source-path and Taylor-product corrections remain, and OW17's expectation statement explicitly requires measurable representatives with finite fourth moments; its principal chart already supplies them. The complete independent derivation and 63 checks were read and replayed. No actual-vacuum concentration on that coordinate locus is inferred.

## SZ-20261011-024 — Continuous actual Wilson histories and full-time collapse

[TR1–TR17](WILSON_TIME_REGULARITY.md) strengthen ASL38 using the original reversible ground-state diffusion. The exact forward/backward identity retains and cancels both full logarithmic drift integrals. Its complete 2p moment estimate is (2p−1)!!(2κ*D²|t−u|)^p; an original face has D²≤4, giving fourth coefficient 192κ*². The dyadic argument proves continuous versions with every local Hölder exponent below one half and convergence of the same selected subsequence on the specified countable continuous-path space. TR17 proves the squared maximum orientation-average error on [0,T] is at most 8εj+320κ*T/(m_j²n_j), tending to zero. The full growing-loop constants remain explicit and are not uniform. The derivation was checked, with 73 independent exact heat-calibration and incidence checks; the calibration model is not substituted for the interacting vacuum. Temporal continuity does not establish spatial smoothness, a four-dimensional field or the spectral endpoint.

## SZ-20261011-025 — Physical conjugate and full actual-vacuum variance

[CV1–CV47](CONJUGATE_VARIANCE.md) construct the exact physical soft lift with both tree-root contributions, then its divergence-free contraction B=Y(V23,u1), which preserves h=|u1|². The commutator retains its signed correction Xi and proves 4G VB≥β0²(2μh+μXi)². The full vacuum equation gives VB=(E0/κ)μh−ξμ(Wh)+(1/2)μΔh−T(3|1), with the complementary nonnegative kinetic quantity retained. CV28–CV39b compute every rooted kinetic and potential term in the double commutator and prove finite bounds. The original reflected metric and boundary products remain in CV18b.

On the unchanged path the evaluated variance bound has order j25, its curvature gain is relatively j^-7, and the full signed numerator correction remains uncontrolled at the needed scale. CV47 is the exact projection identity receiving these terms, without an assumed positive numerator. Owner read the entire proof, repaired two multiplication transcription defects in CV39/CV42 against their complete adjacent derivations, replayed the exact rooted checks and full noncommuting face Hessians, and inspected the figure. This advances the explicit conjugate calculation but does not establish the spectral endpoint.

## SZ-20261011-026 — An explicit anisotropic Wilson sequence for the original endpoint

[AT1–AT60](ANISOTROPIC_TEMPORAL_BRIDGE.md) preserve every physical link, gauge integral, spatial face, temporal endpoint weight, Bessel multiplier, scalar energy and raw phase. AT12–AT15 give quantitative compact-kernel estimates; the joint-spectrum proof removes an unnecessary square-root edge-count factor. AT21–AT36 derive all growing-box transfer and full-phase domain constants. AT37–AT48 recover the actual vacuum from constant open-time boundary vectors, retaining the exponential denominator costs. AT49–AT58 give one explicit temporal sequence on the unchanged original path whose finite four-dimensional Wilson expectation combination differs from G_j−C_F,j/s_j by at most 3/(4j). AT60 retains the exact positive finite-difference energy defect. The endpoint sign remains unknown. All 321 checks passed; the full proof, original provider comparison and reproducible figure were reviewed.

## SZ-20261011-027 — Stronger actual Wilson path estimates

[R1–R29](WILSON_TIME_REVIEW.md) independently verify TR1–TR17 and strengthen their receiving bounds. The complete forward/backward identity gives exponential increments, an explicit logarithmic time modulus, and maximum coefficient 25cT/4. The full original curvature moment recurrence then proves limsup j² E sup_[0,T](2−average W_de,j)²≤27κ*²/10000. Its summable tails give limsup j sup_[0,T](2−average W_de,j)≤9κ*/100 almost surely under any specified coupling with the actual marginal path laws. No independence of faces or uniform vacuum-drift estimate is assumed. The original valid TR bounds remain, and their strengthenings are propagated to TR and ASL. All 323 check groups passed; the complete proof, source comparison and figure were reviewed.

## SZ-20261011-028 — Actual shrinking-window and positive-energy maps

[LEM1–LEM55](ACTUAL_LOW_ENERGY_MAPS.md) prove the exact zero-energy flag for the original shrinking windows, its raw norm domain, its map into the cyclic reconstruction and the positive compression defect. Every fixed or moving spectral endpoint keeps its below, exact and above pieces. Full coefficient arrays for original face sums give a j^-3 positive-energy upper bound for bounded physical local quadratures, whose scalar vacuum value is not supplied by this proof. Actual physical-time detectors kill zero energy and escape while retaining every positive interval; explicit Bernstein sums recover interior weights and atoms with full error coefficients. A strictly positive finite-regulator face band retains its declining mass and both moving endpoints. The complete finite-vacuum/Duhamel and full-residual estimates are received into those same detectors. All 41 check groups passed and the full proof and figure were reviewed. No unknown limiting spectral weight is assigned a positive value.

## SZ-20261011-029 — Actual local curvature and the evaluated physical quadratures

[LC1–LC42](LOCAL_CURVATURE_BUDGET.md), including LC15a and LC25a, prove a local actual-vacuum energy budget for every induced cubic patch, with every original boundary class retained. Full and physical lowest energies are proved equal before using the outside-ground tensor trial. Each crossing face has one inside edge and three outside edges; the exact outside gauge sign makes that open-path expectation zero, so its trial action is exactly 2b. The budget retains both inside kinetic energy and the actual potential subtraction. Its full local moment recurrence supplies concentration and explicit constants on the unchanged path.

The original physical observable a_j³ Σ f(x_p) W_p now converges in actual vacuum norm to 2∫f, and acts as exactly that scalar on the whole cyclic reconstruction. Thus the previously possible centered zero-energy component in LEM27 is evaluated as zero for this observable. LC34 gives the complete finite-word error, LC35 retains every positive spectral interval and the original shrinking window, and LC40–LC42 give full-time estimates and the stated almost-sure limit under any specified coupling of the original path laws. The result uses no translation invariance or uniform individual-face expectation. All 38,567 check groups pass; the complete proof and corrected reproducible figure were reviewed. The covariance and physical spectral weight of candidate fluctuating observables remain separate unfinished calculations.

## SZ-20261011-030 — Original curvature covariance and complete source maps

[PVC1–PVC50](PHYSICAL_LOCAL_COVARIANCE.md) preserve the original all-orientation curvature, its complete scalar, actual mean and raw covariance. The full source projection and reduced inverse are differentiated explicitly; short original-face pulses receive equal-time covariance and first energy with quantitative errors, including the 3/(16j) energy error. The exact local kinetic-plus-potential uncertainty relation yields both roots of a positive local-curvature constraint. It proves a mean of order a_j^-1 for nonnegative nonzero tests and positive finite first-energy bounds when the test integral is nonzero. The sharper denominator retains the actual potential contribution. The actual source-averaged covariance is O(a_j); its difference from source zero is the complete signed three-point response, with both oriented integrals retained. Original-source covariance and fixed-energy mass remain unevaluated. The proof, 155 checks and reproducible diagram were reviewed.

## SZ-20261011-031 — Curvature phases and their actual continuous histories

[CP1–CP50](CURVATURE_PHASE_RECONSTRUCTION.md) use local gradient moments and bounded Markov word ratios to construct a larger cyclic representation of the original bounded curvature phases. Exact products, adjoints, time collisions and reflection positivity hold; the continuous projection loses no norm on these words and its product defect vanishes there. Actual reversible martingale estimates give continuous real anchored increments, all time Hölder exponents below one half, and an explicit logarithmic modulus. Initial compact characters, the regular-character reducing projections and centering translations are constructed with their exact vacuum weights. Positive energy is equivalent to a nonconstant anchored history; its value remains uncomputed. The complete first-energy loss and interval approach spaces are retained, including the original shrinking window. The human comparison is Grothaus, Kondratiev, Lytvynov and Röckner, original author TeX math/0211323v1, Section 6.1. The complete proof, 76 checks and reproducible diagram were reviewed.

## SZ-20261011-032 — Original curvature as a continuous spatial distribution history

[DH1–DH19 and DH9a](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/DISTRIBUTION_CURVATURE_HISTORIES.md) construct the original atomic, anchored curvature distributions with coefficient a_j and all three orientations. Exact local moment bounds give tight continuous paths in the explicitly weighted sine-coordinate Hilbert spaces for every exponent above three halves. The full finite constants, maximal estimates, compact tails, interior test maps, gluing and stationary increments are proved. The ambient boundary kernel is retained. The exact heat detector connects these histories to CP; nonzero limiting energy and spatial smoothness are not asserted. The complete proof, 139 diagnostic checks and reproducible figure were reviewed.

## SZ-20261011-033 — Interior recovery and the actual Hilbert path law

[DR1–DR17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/DISTRIBUTION_HISTORY_REVIEW.md) sharpen the compact tail and construct an explicit infinite family of boundary-kernel vectors. Original moment estimates and smooth cutoffs recover every actual Hilbert coordinate uniformly on compact time intervals almost surely. This gives a Borel representative section on its exact image and supplies the full argument for DH18's Hilbert-law assertion. A boundary-layer sequence proves that the section is not continuous. Gaussian even-moment upper constants yield an explicit tail and logarithmic time modulus; they do not assert Gaussianity. The complete proof, 50 checks and reproducible figure were reviewed.

## SZ-20261011-034 — Actual-vacuum Hessian and original-source variance

[OS1–OS40, with OS8a and OS13a](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORIGINAL_SOURCE_COVARIANCE.md), calculate all stationary curvature terms on the radius-two SU(2) product and prove Hess(log psi) >= -2 sqrt(b/kappa) times the original metric, independently of volume. Exact signed-test integration and the full face Hessian give positive finite first-energy bounds for every nonzero continuous compactly supported real test. The original centered variance has a positive lower bound of order a_j, with an explicit raw spectral window of energy order 1/a_j and a short-time heat decrement. The original covariance upper bound, fixed-energy weight and shrinking-window endpoint remain unresolved. The complete proof, 32153 exact diagnostics and reproducible figure were reviewed. Ascione, Castorina, Catino and Mantegazza, original arXiv:2107.13846v1 TeX, provide a methodological comparison; their different PDE theorem is not imported.

## SZ-20261011-035 — Sharper raw spectral and heat bounds

[HVR1–HVR34](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/HESSIAN_RECEIVING_REVIEW.md) independently derive the full Hessian calculation and original face constants, sharpen the actual variance lower bound to (e_f^*)^2/(63 kappa_*^2 integral(f^2)+4 e_f^*) after division by a_j, and construct a completely explicit finite-regulator receiving window. The sharp Jensen inequality gives a positive decrement bound for every original time tau a_j, without a small-tau restriction. Exact face interference yields a_j times the mean squared face Hessian tending to 63 integral(f^2), leaving the actual ground-state Hessian contraction explicit in the second energy moment. All raw measures and coefficients are retained. The proof, 2988 checks and reproducible figure were reviewed; no novelty claim is made.

## SZ-20261011-036 — Full raw S6 Hessian and physical conjugate covariance

[RH1–RH51 with RH36a/RH41a](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/RAW_S6_HESSIAN_RECEIVING.md) prove complete root and reflection tensors, actual raw Gram and energy matrices, and an exact physical acceleration cancellation. Full root coefficient sums reduce the available conjugate-variance upper function from order j^25 to j^13; the ratio times j^12 tends to 1/72. The remaining signed contraction is an explicit rank-at-most-three off-diagonal covariance block, extended by RH48 to all original root rows. RH50–RH51 evaluate the failure of two direct unsigned substitutions to certify the shrinking window; they do not determine its actual sign. All coefficients, states, original raw norms and energy units are retained. Complete proofs, direct derivative checks, finite row sums, asymptotic constants and the reproducible figure were reviewed.

## SZ-20261011-037 — Stronger upper covariance at the original source

[ZU1–ZU44](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SOURCE_ZERO_COVARIANCE_UPPER.md) prove an exact weighted kinetic-square identity in the actual vacuum. It retains the original absolute face weights, both uncertainty roots, outside and crossing remainders, actual mean, and signed-test subtraction. The leading upper constant strictly improves on the original path; the available variance upper exponent remains a_j^-2. An optimized square and individual-face incidence terms give further evaluated nonnegative subtractions. The complete proofs, symbolic identities, original-lattice derivative checks and figure were reviewed. No source average, auxiliary state or covariance-sign assumption enters this bound.

## SZ-20261011-038 — Potential covariance identities and exact scope of the sign question

[PVI1–PVI24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POTENTIAL_VARIANCE_IDENTITIES.md) derive the original stationary potential-score identity, exact kinetic variance equality and full local exterior covariance. They independently verify and strengthen the kinetic-square calculation. Explicit Euclidean and compact gauge-invariant positive ground states with specified different potentials disprove a universal covariance sign inferred solely from stationarity and gauge constraints. The compact example uses parameter1/100 and the strict rational bound -506181/49000 for its stated scaled covariance. It does not assign that sign to the original plaquette potential. Complete proofs, exact checks and the figure were reviewed.

## SZ-20261011-039 — Actual bounded phase escape and exact defect space

[BP1–BP33](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDED_PHASE_SPECTRAL_RECEIVING.md) give complete phase energy matrices, finite raw spectral/heat bounds, and an evaluated positive loss of continuous norm for actual phase parameters with a_j theta_j^2 tending to a positive finite value or infinity. BP26 retains every original constant and scalar phase. Fixed parameters retain norm. BP28–BP33 prove the exact compression defect and construct its nonzero high-energy space. The prescribed shrinking-window weight and smooth four-dimensional theory remain unfinished. Complete proofs, 798 diagnostic checks and the reproducible figure were reviewed.

## SZ-20261011-040 — Exact soft-direction root defect and covariance receiving maps

[DP1–DP43 plus DP36a–DP36b](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/DIRECTIONAL_POTENTIAL_AND_ROOT_DEFECT.md) retain every root-frame connection and commutator, prove exact face-orientation cancellations, and obtain the uniform coefficient 3/2+8/pi^2. The actual directional Hessian receives the transported-curl covariance with an explicit error of order j^-1/2 before its original magnetic coefficient. An exact original-link example retains transverse Hessian 1/2 while elementary face defects vanish. Full local-moment covariance maps, signed kinetic and score-root contractions identify the actual-state data still to evaluate. Complete proofs, direct word derivatives, finite sums and the figure were reviewed.

## SZ-20261011-041 — Exact bounded-energy projection and positive defect matrix

[BR1–BR27](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDED_PHASE_SPECTRAL_REVIEW.md) independently prove the phase receiver and strengthen it by identifying the continuous projection with the full increasing bounded-energy projection limit. BR17–BR18 give finite spectral-tail and moving-band lower bounds with their original endpoints. BR25 proves the complete positive matrix of multiplication defects. The retained norm statement extends to all bounded parameter sequences. These complete proofs were read and the independent algebra/spectral checks replayed; no actual low-energy or smooth continuum result is asserted.

## SZ-20261011-042 — Actual potential law and removal of the upper covariance endpoint

[FO1–FO56](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PUSHFORWARD_OPTIMIZATION.md) construct the actual coarea law and both zero-flux currents across critical values, evaluate the optimum over all score functions, and retain the complete conditional ground equation and outside energies. The upper-tail estimate gives O(a) scaled upper excess and a contribution from the far upper endpoint smaller than every fixed power of a. The central-range variance integral, actual mean, lower-side term and drift defect remain explicit; the full centered covariance exponent has not improved yet.

## SZ-20261011-043 — Independent endpoint and scalar ground-form derivation

[PF1–PF53](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PUSHFORWARD.md) independently prove the current, optimizer, sharper tail integral, endpoint score limits and exact central variance receiver. The explicit original-link path passes through every potential value with a regular point in each interior fiber. PF27–PF32 construct the exact scalar ground representation and map it back to the full physical operator. PF17's all-face label serialization was repaired with the original full scalar and face sum preserved.

## SZ-20261011-044 — Full scalar domain and second-energy residual

[OP1–OP19](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PUSHFORWARD_OPERATOR_RECEIVING.md) prove the closed scalar form domain, natural endpoint conditions and unit ground function. Its physical isometry gives the full Gram, first-energy and second-energy matrices. The positive residual matrix retains both original conditional fluctuations and their correlation, with evaluated geometric upper bounds. OP18–OP19 supply every physical-time and volume factor in the primary-source comparison. These are exact finite-regulator results; the smooth interacting gapless four-dimensional state remains the goal.

## SZ-20261011-045 — Both energy-root tails and inverse-weighted retained-energy bounds

[LR1–LR58](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/LOWER_SIDE_RETAINED_ENERGY.md) evaluate both original energy-root tails and all fixed negative moments on the original regulator path. The actual inside energy Y+A has variance O(a^-1), with every mixed-Hessian, shifted-Hessian and conditional-score remainder retained. The next weighted equation gives mu[((e−Y)+−A)^2/Y^k]=O(a^(2k−1)), with explicit finite constants. LR58 proves the original signed compensated map and its full means and covariance. Separate centered curvature variance still retains its signed energy covariance.

## SZ-20261011-046 — Exact inside marginal, residual and covariance verification

[IM1–IM42](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/INSIDE_MARGINAL_ENERGY.md) independently construct the actual inside marginal and conditional vector, full outside derivatives and the exact physical operator residual. The complete nonnegative retained-energy difference and inverse-weighted Bochner bounds agree with LR. A specified separate compact positive-ground example disproves a universal covariance-sign inference; it does not assign that sign to the original Wilson model. All88 independent diagnostic checks pass and the full proof and figure were reviewed.

## SZ-20261011-047 — Exact scalar operator domain and phase covariance cancellation

[OR1–OR17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/INDEPENDENT_OPERATOR_REVIEW.md) independently verify the full scalar operator construction and physical-time factors. OR6 proves the associated-operator domain in both directions, including the global integrable flux and both endpoint conditions. OR9–OR10 prove the action on every stated smooth test and its exact map to the original Hamiltonian. OR13 cancels the mixed conditional covariance on the diagonal for actual scalar phases; OR14 retains it off the diagonal and OR15 restores the entire original second energy. The full proofs and illustration were reviewed, and all17 bounded symbolic checks pass.

## SZ-20261011-048 — Actual transported-curl covariance and signed Wilson bound

[WC1–WC55](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_WILSON_COVARIANCE.md) prove an actual-vacuum lower bound for the original transported soft curl using conditional one-link scores and an exact two-link Haar fibre. All repeated-edge Casimir cross terms and exceptional tree rows are retained. WC33–WC35 prove the scalar and full mixed-row covariance bounds. On the original path, WC39–WC45 evaluate the positive constant in the lower function of order j^-1, while the ordinary cochain curl squared is of order j^-8. WC46–WC55 retain the full curvature, kinetic, score and raw spectral maps. The potential-error upper function remains too large for the new magnetic lower function alone to close the spectral estimate.

## SZ-20261011-049 — Full original root-score matrix and signed kinetic trace

[SK1–SK39](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SIGNED_KINETIC_TRACE.md) prove the actual full root-frame score bound, exact ancestor decomposition and all block ranks. The positive trace is (3m−1)/2 plus an explicit logarithmic upper remainder; the negative trace is retained. The original-path kinetic upper function is 1200j^5+O(j log j). SK29–SK39 give the full actual chord-score covariance, Gauss relation, physical variable-colour Gram and original raw-window map.

## SZ-20261011-050 — Bounded original energy and complete signed limiting covariance

[BM1–BM69](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDED_ENERGY_MULTIPLIER.md) derive every original Hessian overlap, prove first energy of order a² and second moment O(a), and map the actual centered vector into the unchanged shrinking window. The central bounded energy map retains its original cyclic visibility defect. BM58–BM69 give the two-root support, full potential/retained-energy heat-word maps, exact signed limiting covariance and companion matrix. The actual limiting variance remains unevaluated; these equations do not establish an improved raw covariance exponent.

## SZ-20261011-051 — Independent cyclic and retained-energy receiving derivation

[IB1–IB46](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDED_MULTIPLIER_RECEIVING.md) independently prove the original spectral endpoint and visible/hidden decomposition, all polynomial compression defects, and the full potential/retained-energy moment map. Both root excess bounds and the shifted resolvent recurrence keep all mixed terms. IB39–IB45 identify the actual leading covariance and its exact relation to the bounded Gram, including its possible collapse.

## SZ-20261011-052 — Exact negative trace and actual root-cell contraction

[TC1–TC18](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/NEGATIVE_TRACE_COMPRESSION.md) prove that the negative trace of the full original signed matrix has order log n, preserving every nodal and boundary channel. The exact coefficient is evaluated in [G1–G52](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GAMMA_INTEGRAL.md), including two independent rational enclosures. TC14 proves a strictly negative actual-vacuum root-cell term; TC10–TC16 retain the complete complement, cross and incoming-flux terms. The full actual contraction remains to be evaluated.

## SZ-20261011-053 — Smooth holonomy map and the actual curvature scale

[HC1–HC24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/HOLONOMY_CURVATURE_RECEIVING.md) prove a gauge-compatible surjective smooth-connection-to-link map, the exact curvature factor1/4, and the actual-vacuum curvature threshold of order a^(-3/2). A compact smooth three-colour family attains this scale and has an explicitly calculated receiver of the original signed observable, with all finite errors retained. The full static source and an exact globally smooth homogeneous Yang–Mills comparison are derived; the latter has infinite spatial total energy.

## SZ-20261011-054 — Universal curvature bounds and exact physical-time accumulation

[HCR1–HCR8](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/HOLONOMY_CURVATURE_REVIEW.md) prove the exact gauge inversion dictionary, almost-sure curvature lower bounds for every smooth-preimage sequence under any coupling of the actual marginals, and bounds for every positive curvature moment. They construct a nonzero receiver for every original nonzero signed test and determine the complete fixed-time accumulation interval of the symmetric homogeneous classical family. Actual continuum-state identification, finite-energy dynamics and reconstruction remain active calculations.

## SZ-20261011-055 — One simultaneous spatial measure for the original state

[CM1–CM63](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SIMULTANEOUS_CENTRAL_MEASURE.md) construct the exact positive central Radon measure for all three original plaquette orientations on one state path and one ultrafilter. Full cube bounds, atomlessness, a positive absolutely continuous component, possible singular mass, covariance measures, original cyclic compression and all mixed heat-word maps are proved. The original signed observable, root constants and crossing-face terms are retained.

## SZ-20261011-056 — Current collapse and surviving original fluctuations

[CE1–CE50](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURRENT_COVARIANCE_EQUALITY.md) evaluate the entire CM current defect to zero, identify the next centered current with the same spatial covariance, and give complete finite variance identities with geometric and outside-energy remainders. Every nonzero orientation triple has explicit positive first-energy and raw-variance lower bounds. CE46–CE50 strengthen the first heat-increment result to every positive heat parameter, retaining the exact spectral remainder. CE35–CE42 give the unchanged shrinking-window and visible/escape maps; the actual low-window energy coefficient and central covariance remain to be evaluated.

## SZ-20261011-057 — Smooth realization of every positive spatial orientation measure

[SM1–SM12](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SMOOTH_MEASURE_REALIZATION.md) and [AA1–AA20](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/AMPLITUDE_ALGEBRA.md) construct the full smooth compact realization of arbitrary positive Radon orientation triples by the original Wilson faces. All density factors, cutoff derivatives, finite errors, explicit regulator schedules, Borel maps and joint-moment limits are proved. The source and its polynomial-time correction are complete; the boundary-amplitude defect is calculated.

## SZ-20261011-058 — Global smooth solution laws, energy receiving maps and stationarity

[GM1–GM28](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GLOBAL_MEASURE_EVOLUTION.md) apply the established finite-energy global theorem to those exact initial data. They prove a continuous global solution map receiving the actual central spatial law, full conserved energy and its local receiving limit, the exact first temporal correction and a strictly positive initial electric observation. Explicit time averages have stationarity defect at most min(2,|h|/T) times the test bound. The complete virial proves that a stationary probability on conserved finite-total-energy smooth trajectories is flat almost surely, including laws without a finite expected-energy assumption. The inclusion into the space allowing infinite total energy preserves dynamics and all local observations. The actual quantum receiving correlations, reconstruction and smooth no-gap endpoint remain active calculations. No novelty claim is made.

## SZ-20261011-059 — Stationary smooth phase laws, exact window mass and receiving obstructions

[HP1–HP40](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/STATIONARY_PHASE_RECEIVING.md) construct stationary global smooth homogeneous Yang–Mills laws and calculate their complete phase, spatial and time correlations. The actual CM lower bounds exclude this isotropic phase family, with an explicit continuous witness and a uniform interval-defect probability. The original finite Wilson observations retain a fully calculated shrinking-window weight under the specified auxiliary positive generator: the coefficient decays as j^(-63/4) for aC and j^(-55/4) for raw C, with a relative norm error of order j^(-4). Complete energy matrices and HP37 contrast this auxiliary spectrum with the actual quantum leading receiver, whose original first energy tends to zero. HP38–HP40 prove the exact composition-generator restriction and reflection-form comparisons, keeping the direct Euclidean interpretation distinct from analytic continuation. These comparisons do not assign the actual quantum window weight or establish the interacting no-gap endpoint.

## SZ-20261011-060 — Actual fluctuation and anchored-history receiving maps

[EF1–EF27](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ENERGY_ROOT_AND_ANCHORED_HISTORIES.md) prove that all actual CE heat-increment vectors have one continuous-time receiver, with their complete escaped Gram retained. A bounded sine-cylinder approximation receives every positive-energy component of the actual energy-root vector in an explicitly enlarged curvature-phase cyclic space. The proof preserves the smaller CM space and every zero-energy, original-window and cyclic-compression defect. Exact anchored variance and reflection formulas retain both spectral endpoints; a quantitative original-energy window bound uses the actual variance and the full fourth-moment remainder. EF25–EF27 additionally prove that the actual small-phase energy measures receive the complete finite-energy spectral measure, including its zero endpoint, and give a quantitative bound for positive windows. No actual coefficient is assigned a positive value merely from whole-vector survival.

## SZ-20261011-061 — Actual positive-time covariance and required full tail

[PT1–PT36](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/POSITIVE_TIME_COVARIANCE.md) prove the actual energy correlation’s exact weighted one-form representation on the original SU(2) lattice, including the radius-two Ricci term, gauge constraints and complete exterior Hessian inverse. The two-time current cancellation is evaluated. The full Hessian expansion has a proved finite-regulator remainder bound, and every truncation with a_j(N_j+1) tending to zero is proved to vanish. Any surviving response is received by its complete tail, whose spectral concentration near one and exact unitary map to the physical resolvent vector are established. The raw and energy-weighted original shrinking windows remain explicit. No positive value of an unfinished limiting coefficient is assumed.

The primary-source comparison uses original author TeX by Jon Johnsen and Assane Lo, with exact versions and bounded reading coverage. The compact-domain convexity obstruction is proved together with the curved weighted-form map that remains available. Complete proofs, reproducible figures and checks are included.

## SZ-20261011-062 — Actual ground-gradient energy and stronger variational bound

[SG1–SG33](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_GROUND_GRADIENT_TRIAL.md) construct edge-weighted gradients of the actual logarithmic ground density and compute their complete energy, current covariance, source overlap and exterior Hessian contributions. Exact optimization over every deterministic edge weight gives a strictly positive finite matrix and an explicit residual mapping its value to the full physical resolvent. A forced equation relates the trial directly to the derivative of the original plaquette potential. For the unchanged three-orientation tent test, the sign trial improves the previous proved lower-bound coefficient by more than ten thousand; its lattice-spacing scale is retained. The remaining signed contraction and full residual have not been assigned limiting values. Complete proofs, exact coefficient comparisons and reproducible inspected figures are included. The physical exact projection removes the entire nonnegative Hessian graph energy while preserving source overlap. Its improved current-covariance matrix retains both full residual norms. Every exterior graph connection and the complete kernel of the removed defect are specified.

## SZ-20261011-063 — Conditional currents and a larger physical trial space

[CG1–CG34](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CONDITIONAL_GROUND_CURRENT_TRIAL.md) split the actual ground-gradient trial into orthogonal marginal and conditional-fluctuation parts. The fluctuation has zero source overlap, so its independent weight can be optimized. The complete current matrix, including exterior drift and all zero directions, gives an exact nonnegative improvement over the previous SG matrix and an explicit additional lower-bound term. The physical resolvent retains both full residual norms. The conditional ground equation evaluates the remaining marginal contribution while preserving outside energy, crossing faces and conditional kinetic derivatives. Complete proofs, reproducible diagnostics and an inspected figure are included; no positive value of the limiting gain is assumed. A further exact minimization over every outside one-form replaces the conditional noise by its full outside resolvent multiplier, without an exterior-mode cutoff. Its original-Hamiltonian map, additional nonnegative gain, zero space, mixed derivatives and both physical residual norms are proved in CG23–CG34. Fixed-regulator small-z limits are not interchanged with the regulator limit.

## SZ-20261011-064 — Retained derivatives and actual boundary selection

[RD1–RD22](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/RETAINED_DERIVATIVE_AND_GOOD_BOUNDARIES.md) evaluate the derivative retained in CG22 using the full ground equation, marginal equation, conditional variance and both Hessian contractions. The original supported sign and continuous weights have exactly zero direct crossing trace. For unit edge magnitudes, deterministic boundary selection in the actual ground gives a vanishing scaled crossing potential while the full Laplacian trace tends to \(9R^2/\kappa_*\). The original square-root collar and an additional logarithmic collar have complete finite bounds and different proved error rates. Every scalar, outside energy and conditional-current term remains in the calculation; no limiting spectral weight is assumed.

## SZ-20261011-065 — Exact gauge-invariant covariance-sign comparison

[GS1–GS12](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/WILSON_AND_CURRENT_COVARIANCE_SIGNS.md) construct a smooth gauge-invariant comparison on two disjoint original plaquettes with strictly positive Wilson-trace covariance and strictly negative distinct-edge ground-current covariance. Complete analytic constants, partition factors and the comparison Hamiltonian are retained. The exact unitary, full potential difference, vacuum change and current transformation connect it to the original Yang–Mills ground. The comparison rules out an inference from Wilson positivity alone; the specific actual-current contractions remain to be evaluated.

## SZ-20261011-066 — Actual outside forcing and a strict current improvement

[OC1–OC24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/OUTSIDE_FORCE_AND_CURRENT_MOMENTS.md) derive the actual conditional score equation, positive averaged potential Hessian and complete outside-current forcing, preserving the entire original kinetic quotient and every mixed Hessian. Exact first and second moments give a quantified resolvent improvement with both physical residuals. A crossing plaquette proves that the full-cube positive-weight current is nonzero, so the specified finite-regulator improvement is strictly positive. The full covariance, Hessian and force kernels coincide and retain inside gauge directions. The global oscillation comparison is evaluated on the original path; it supplies no vanishing filter coefficient. The limiting current moments and smooth interacting no-gap endpoint remain open calculations.
