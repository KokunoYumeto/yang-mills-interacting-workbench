# Mathematical findings and propagation

## SZ-20261011-001

PK172–PK177 retained all word occurrences but used a bound proportional to the entire link count. IP2–IP9 evaluate both the first and squared occurrence sums with every repeated root segment and boundary exclusion. The resulting bound grows as \(n^7\), improving the former \(n^9\) bound and its original-path negative loss from \(j^{31}\) to \(j^{23}\). This is a bound on the actual expression; it does not determine the expression's asymptotic value or sign.

Full proof: [IP1–IP9](PHASE_MOMENTS_AND_ORIGINAL_PATH.md). It strengthens the finite receiving estimates used in PK202 and PK227.

## SZ-20261011-002

PK148 treats a bounded sine observable. Applying its strong vacuum limit alone to the unbounded polynomial \(x-y\) would leave a tail unjustified. IP10–IP17 derive the required actual potential moments, global phase bounds and derivative bounds, then prove norm and energy convergence for every fixed polynomial at fixed \(L,a\). IP18–IP20 evaluate raw norm, energy, fourth moment, first odd-cluster weight, and the full polynomial matrices. The limiting Gram rank is \(R\) and nullity is \(R(R-1)/2\), although every finite-regulator Gram matrix is positive definite.

Full proof: [IP10–IP22](PHASE_MOMENTS_AND_ORIGINAL_PATH.md). This strengthens PK148, PK202 and PK205 without changing their quantifiers. IP21–IP22 preserve the unresolved difference between the iterated limit and the prescribed joint path. The tail coefficient's growth is a proved property of the bound, not a lower bound on the true tail.

## SZ-20261011-003

J7 left the third Schur coefficient, full complementary inverse and accumulated tail unevaluated. P3–P26 prove a central-sign involution on the original labelled source and its exact assembly quotient. Every odd-degree return word vanishes separately; in particular the third coefficient is zero. P20–P21 bound the full complementary inverse. P31–P38 bound every remaining even order by an explicit rational majorant. P39–P45 retain the original Hamiltonian scalar, actual vacuum map and full nonlinear interior inverse.

Full proof: [P1–P45](ORIGINAL_J5_PARITY_AND_TAIL.md); prior exact channels: [J1–J7](BASELINE_J5.md). The first unevaluated Schur coefficient is now the fourth. No new physical gap or enlarged nonlinear endpoint follows from the auxiliary bounds.

L. Li and Y. Meurice's original arXiv:hep-lat/0410029v2 TeX, Sections II–IV and the Appendix at the recorded coverage, supplies the human antecedent for center reversal and coupling parity. The original kinetic, label and boundary comparisons are proved here. Novelty is not asserted.

## SZ-20261011-004

The open-box sign construction extends to all rectangular open boxes. For periodic rectangular boxes with \(N_i\ge3\), CS9–CS14 prove existence exactly when every \(N_iN_j\) is even. All assignments are classified, including their winding signs: one central gauge class in the open case, eight in the admissible periodic case. The precise obstruction is the constant face cochain, evaluated on the coordinate two-tori. CS4 also constructs the gauge-equivariant bijection between all \(U_p=-I\) fields and all flat fields once a reversing assignment exists; the larger field quotient is not asserted to consist of eight points.

Full proof: [CS1–CS19](CENTRAL_SIGNS_AND_BOUNDARIES.md). This gives the exact boundary scope of the map used in SZ-20261011-003. The unique elementary plaquette-data set in Li–Meurice is preserved as such and is not read as a classification by all winding observables.

## Propagation and remaining calculation

The original phase proof PK1–PK227 and original J1–J7 provider remain identifiable. These additions are linked from the programme reading paths, entered in its result and claim ledgers, and included in the cumulative TeX. Historical records remain historical; current continuation instructions now start the Jacobian branch at the fourth coefficient.

The source's positive finite-regulator Gram result remains correct. Its conditioning can deteriorate in the fixed-box coupling limit, as proved above. That degeneration must remain in any simultaneous-cutoff estimate involving the inverse Gram matrix. The existing approximation certificate controls numerical error, while the actual shrinking-window covariance cancellation still needs a mathematical estimate.

The interacting continuum state, reconstruction, global smoothness and no-gap endpoint remain the active research goal.

## SZ-20261011-005

IP17–IP20 give fixed-box Gram and energy matrices but not every spectral weight. [SP1–SP16](PHASE_SPECTRAL_WEIGHTS.md) prove the finite Hermite coefficient formula, the full determinant generating kernel and convergence of all original phase-family actual cluster weights at fixed box. The complete cubic raw weights are 2700, 2160 and 1440. The exact oscillator second-moment matrix and complementary energy map have residual entry 864δ*². Its minimal invariant closure is the three-dimensional space generated by q, uq and q³ times the complete vacuum. This strengthens IP17–IP20 and supplies the full limiting target for the PK223 complement calculation. It does not assert convergence of unbounded actual second moments, convergence of finite-regulator inverse Gram matrices, or a uniform joint-path estimate.

Every formula and connecting operator is proved in SP1–SP16. The 104 finite rational checks supplement those proofs. The source and reading record retains PK102–PK112 and IP10–IP20. No novelty claim is made for Gaussian or Hermite methods.

## SZ-20261011-006 — exact reflection normal map and global two-link component

[JP1–JP49](BOUNDARY_REFLECTION_AND_RAW_ENDPOINT.md) preserve the original box, rooted words, coefficient rows, vacuum and regulator path. They prove the reflected-word map, the full boundary normal metric \(G_{\mathcal B}=2I+mD_{\rm wall}D_{\rm wall}^{t}\), and a nonzero normal derivative although the original correction vanishes on the identity boundary fibre. The exact global two-link harmonic gives
\[
\mu|\nabla D|^2\ge d_*^2e^{-24\pi\xi}/8,\quad
\mu D^2\ge d_*^2e^{-40\pi\xi}/8,\quad
G\ge\beta_0^2d_*^2e^{-24\pi\xi}/12,\quad
C_F\ge\kappa\beta_0^2d_*^2e^{-24\pi\xi}/6.
\]
The earlier all-link and boundary-only bounds remain proved, but JP43–JP49 strengthen their exponential loss to order \(j^2\). The full six-term endpoint and the direct even mass-to-energy map retain every contribution. These are lower bounds for different actual quantities, not a quotient estimate or proof of positive shrinking-window mass. The actual four-loop/gradient cancellation remains unfinished. All 66 finite word, derivative, metric and harmonic checks passed; they supplement the complete proofs.

## SZ-20261011-007 — complete fourth Schur coefficient and physical response

[Q1–Q50](fourth_return/FOURTH_SCHUR_COEFFICIENT.md) evaluate all eight fourth-order return words of the unchanged fifth-reference Jacobian, preserving intermediate complementary projections and union labels. Independent exact recurrence, parity and geometry calculations establish every coefficient and the all-box formula. Its boundary skew matrix is
\[
S_{[4]}-S_{[4]}^t=-\frac{703}{19712160}[D_{\rm deg},A_{\rm adj}],
\qquad\|S_{[4]}\|_{H\to H}\le\frac{4574447}{33510672}.
\]
The full remainder from degree six has the original local-norm bound in Q40. Q47 proves the exact observation-and-resolvent map to the symmetric physical susceptibility, including the normalized vacuum scalar and higher source correction. Q50 proves that no positive metric tending to the original Haar metric can make this Schur map self-adjoint near zero. Its defect defines the explicit boundary skew matrix and its receiving map; it is not a failure of physical self-adjointness. This completes the former fourth-coefficient backlog. The independent cube proof and polynomial differentiation certificate are retained with all seven replay scripts and their exact dependencies. No new continuum gap claim follows.

## SZ-20261011-008 — physical inverse at every finite real source

[GPR1–GPR55](GLOBAL_PHYSICAL_RESPONSE.md) prove the original physical source Jacobian is invertible on every physical zero-Haar-mean Sobolev space at every finite real independent source. The complete inverse retains both different means, the actual vacuum and the original factor κ. GPR11–GPR18 prove the exact bounded map from all original union labels to their assembly quotient and an independent global inverse on that quotient. The old labelled Taylor-series radius is unchanged.

GPR19–GPR26 strengthen the earlier response statement to strict positive definiteness and identify the Wilson expectation map as a real analytic diffeomorphism onto the interior of the convex hull of the actual full Wilson image. GPR35–GPR40b compute the complete two-link mixed trace derivatives and cancel the exact Haar cube volume by averaging every centre, retaining every exterior link and actual density. With the full original face norm and \(C_*=1/(e2^{37})\), the unchanged path satisfies
\[
\|(R_j^{\rm phys})^{-1}\|\le16C_*^{-2}M_j^2
\left(1+128\sqrt3\,{10000j^2\over\kappa_*^2}\right)^8=O(j^{40}).
\]
This improves the provisional local-coordinate powers while preserving all original objects. The complete source inverse has its different explicit estimate; no full spectral inverse is assigned the face-response bound. GPR53–GPR55 also prove the actual integrated homogeneous-response identity, with its endpoint justified by the original vacuum energy bound. These finite-source results do not determine the actual shrinking-window phase weight or the continuum endpoint. The unquotiented relation-kernel inverse is a subsequent calculation, not assumed here. Exact symbolic checks and a reproducible inspected figure accompany the proof. No novelty claim is made for the underlying elliptic or convex methods.

## SZ-20261011-009 — polynomial score comparison and original-row optimization

[PC1–PC52](POLYNOMIAL_CONDITIONAL_BOUNDS.md) prove a complete degree-two quaternion-polynomial comparison in the original radius-two metric. For every positive unit density with logarithmic score at most \(B\),
\[
\int|P|^2\rho\,dU\ge c_{\rm cap}(1+B)^{-8}\int|P|^2dU,
\qquad c_{\rm cap}=\frac{\cos^{14}(1/4)}{1024\cdot105041\pi3^{9/2}}>2^{-37}.
\]
The exact stereographic map retains its denominator and all lower-degree coefficients. A complete 35-dimensional cube Gram estimate and averaging every cap centre prove the bound. The explicit smooth densities PC20–PC22 prove exponent-eight optimality for this full polynomial space. The original colour-vector receiving map has exponent two, with its own proved optimality family and complete constant in PC25.

PC45–PC48 prove the full word, conjugation and derivative maps for a larger pair of links already present in the original phase. Its coefficient \(d^\circ=8\cos(3h)\cos^3h/n^3\) is the exact maximum within the specified receiving family; the original state and regulator path are unchanged. PC49–PC52 give actual-vacuum lower bounds whose right sides have scales \(j^{-46}\) for odd mass and energy, \(j^{-44}\) for even mass, and \(j^{-45}\) for the positive endpoint correction. These improve the exponential bounds in JP43–JP49. They are asymptotics of proved bounds, not of the unknown expectations. The complete four-loop/gradient cancellation and low-window mass remain unresolved. All 21 checks passed; exact Gram checks and numerical word/limit checks are distinguished in the receipt. The inspected figure illustrates the proved sharpness family and original coefficients, with full reproducible quadrature retained.

## SZ-20261011-010 — the full labelled inverse at every finite real source

[UL1–UL47](union_label_global/FULL_UNION_LABEL_INVERSE.md) prove a bounded real analytic inverse of the entire original union-labelled Jacobian, including the assembly relation kernel. For every edge subset, the proof uses the full original Hamiltonian with exactly its contained face sources, its actual positive vacuum, and both original means. Boolean cumulative coordinates give the exact conjugacy and inverse
\[
\mathfrak L_x^{-1}=\mathfrak m\,\operatorname{diag}(\mathscr L_A^{-1})\,\zeta.
\]
All supported domains, real uniqueness, the original source germ and its full union labels, energy coefficients, removed Haar scalars and vacuum normalization coefficients are proved explicitly. This completes the full finite-source inverse beyond the previously established assembly quotient. It does not enlarge the Taylor disk at zero. All 7,656 exact Boolean and constant checks passed; elliptic assertions are supported by the complete proofs.

## SZ-20261011-011 — exact connected supports and stronger transformation constants

[UF1–UF17](SUPPORT_AND_SCALAR_FACTORIZATION.md) prove product-vacuum factorization for disjoint sets of interacting link variables before imposing gauge constraints. Möbius inversion then shows that the vacuum, energy, removed scalar and normalization coefficients vanish outside connected unions of active face boundaries, for every finite real source. Every label remains in the inverse. The full original two-adjacent-face example retains its shared-edge term \(v_{P\cup Q}-v_P-v_Q\), with all seven oriented edges and Wilson words displayed.

The original physical gauge constraint forces each nonzero supported coordinate to contain at least four edges. Applying this to the exact Boolean count strengthens each transformation norm to \((N+4)2^{N-7}\), and propagates its square through the full inverse and the original-path bound. The estimate still has exponential volume dependence; quantitative control of the connected coefficients and the actual shrinking-window endpoint remain to be derived. All 14,120 exact support/counting checks passed. The inspected figure and its source display the complete inverse and the actual adjacent-face example.

## SZ-20261011-012 — exact cap blocks, sharp vector exponent and all boundary derivatives

[PS1–PS76](POLYNOMIAL_SCORE_AND_ORIGINAL_ENDPOINT.md) prove the complete fourteen-dimensional cap comparison with constant \(C_2=24398405/306317856079872>2^{-24}\), strengthen the original two-link mass and mass-Gram estimates, and prove the exact three-component quadratic-vector estimate with arbitrary affine remainders and constant \(C_6=2595575/14797504512\). The full polynomial exponent eight and the special-vector exponent six are proved optimal for their stated score classes by explicit smooth densities. Every actual conditional and marginal score, metric factor, boundary word and coefficient sign is retained.

Adding all distinct selected physical derivatives gives the complete functions \(B_6,B_2^-,B_2^+\) in PS58. Their original-path odd and even energy bounds have order \(j^{-34}\), and the positive endpoint correction has order \(j^{-33}\), with full constants. These are lower-bound functions, not asymptotic evaluations of the unknown expectations. Both exact rational and symbolic replay certificates pass. The original Dai–Wang author TeX is used only for the precise polynomial-space, measure and metric comparison PS76; no unspecified theorem constant or literature novelty is claimed.

## SZ-20261011-013 — full gradient comparison and every original bulk-link energy

[PG1–PG70](POLYNOMIAL_GRADIENT_BOUNDS.md) retain all scalar, vector and tensor Dirichlet blocks, including their affine off-diagonal terms. Their complete cap calculation proves
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

## SZ-20261011-067 — Exact boundary force and actual current-moment bounds

[BQ1–BQ18](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDARY_FORCE_PROJECTION.md) prove that the derivative of the original inside kinetic quotient is the full weighted exact projection of the inside potential gradient. Every wholly inside face derivative cancels from the conditional force; the complete crossing field and original ground-state projection remain. Exact projection and Casimir-gradient remainders give actual force and mixed-Hessian bounds on both established collars, including \(a_j^6\|F_j\|^2\to0\) and \(a_j^5\mathcal O_{Q_j}\to0\). The first current moment is computed without third kinetic derivatives and has a quantitative upper estimate. The second moment retains its weighted boundary divergence and all six signed covariance terms. Unscaled limiting spectral mass and the smooth interacting no-gap endpoint remain active calculations.

## SZ-20261011-068 — Boundary divergence and the original marginal-current moments

[BD1–BD19](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDARY_DIVERGENCE_AND_MARGINAL_MOMENTS.md) prove an exact mixed derivative and two-square identity for the full projected boundary field. Weighted integration removes its mixed-Hessian contraction from the divergence estimate while retaining the inside score and every original crossing derivative. Both established collars give \(\smash{a_j^7\|J_j\|^2\to0}\) with explicit rates. The existing marginal-gradient block has complete first and second moments and \(\smash{a_j^{11}m_{2,j}^\gamma\to0}\), again with explicit collar constants. The arbitrary-weight force map, full scalar trial line, signed second-moment cross term, exact scalar optimizer and both physical residuals remain. The full-gradient mixed-Hessian fluctuation and limiting physical spectral weight still require evaluation.

## SZ-20261011-069 — Original kinetic current, inverse column and physical energy

[KC1–KC28](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/KINETIC_CURRENT_AND_PHYSICAL_ENERGY.md) retain the original kinetic quotient and its complete conditional mean, and decompose the full current into kinetic and score fluctuations. The actual kinetic variance has a boundary-count bound with all nonnegative energy remainders. Its first two moments control the full kinetic column of the conditional inverse at the original shrinking energy. Differentiating its conditional mean gives the exact full physical energy, including a retained conditional covariance. That covariance supplies an explicit enlargement of the physical scalar trial space, an exact Green-function gain and its full residual. The source gain and limiting physical spectral weight remain unevaluated; the complete earlier current family remains available.

## SZ-20261011-070 — Complete local energy and physical spectral windows

[LE1–LE23](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/LOCAL_ENERGY_PHYSICAL_WINDOWS.md) add the entire retained inside-energy fluctuation to the conditional kinetic vector. Its full physical gradient is the original projected boundary field. Complete norm, first-moment and second-moment identities retain all scalar energies and cross terms; explicit upper and lower bounds are proved. The original supported observable has zero mixed first energy but a retained ordinary covariance and mixed second moment. Its full two-vector Green calculation includes the complementary physical residual. An invertible coefficient map proves that the complete inside-function trial space is the existing KC space, preventing a spurious additional gain. The original full-Hamiltonian shrinking-window tails are bounded; the actual surviving norm and source mass remain unevaluated.

## SZ-20261011-071 — Smooth spatial energy and exact sector covariances

[WH1–WH33](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SMOOTH_WEIGHTED_LOCAL_ENERGY.md) construct the complete original energy with smooth spatial weights and calculate its full physical forcing, including exact face-trace cancellation. A comparison for every actual edge subset and an exact finite level decomposition prove a variance bound while retaining all nested-sector covariances. The noncommuting weighted-sector defect is computed explicitly. The original observable trace has an evaluated limit; its subtracting covariance and all distinct-face energy contractions remain. Complete norm, first-energy and second-moment matrices give the scalar Green gain and full physical residual, including dependent-vector cases. Original shrinking-window upper functions improve. The exact one-face physical vector vanishes, demonstrating why surviving mass requires the actual coupling between faces. No limiting spectral mass is assigned.

## SZ-20261011-072 — Shared-face physical coupling and the complete exterior state

[SF1–SF27](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SHARED_FACE_WORDS_AND_PHYSICAL_COUPLING.md) evaluate the original shared-edge contraction as an exact difference of six-edge and eight-factor Wilson words, with every traversal sign and enlarged support count. The seven-edge two-face graph has an explicit physical Haar isometry and a retained mixed Casimir. Its weighted-energy fluctuation has strictly positive norm for every positive coupling whenever the two face averages do not sum to twice the shared-edge weight. The full original lattice marginal has an exact receiving equation that retains the exterior energy, conditional kinetic contribution and complete variance. These formulas connect the finite interaction mechanism to the original state without assuming a surviving continuum spectral mass.

## SZ-20261012-001 — Actual-vacuum edge variance and surrounding-loop energy

[EV1–EV29](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_EDGE_ENERGY_VARIANCE.md) prove strictly positive edge-energy variance for every edge in the original full vacuum, including boundary edges. The exact decomposition retains the raw fiber-ground overlap, its full mass, the mean square and the entire excited remainder. Original surrounding paths determine six-edge loops and an explicit conditional-energy profile with all scalar and metric factors. The local vacuum budget proves averaged alignment of those paths and shows that one extreme-configuration lower estimate decays; it does not prove decay of the actual variance. Complete original-source, cross-edge and smooth-weight maps and full physical moments remain available for the shrinking-window calculation.

## SZ-20261012-002 — Full ground-family coupling and actual raw overlap

[GF1–GF31](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/FULL_HAMILTONIAN_GROUND_FIBER.md) compute the complete original full-Hamiltonian coupling to the positive one-edge ground family, including every outside derivative, potential scalar, complementary inverse and source correction. [RO1–RO17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/RAW_OVERLAP_AND_ORIGINAL_METRIC.md) retain the exact radius-two metric, Haar prefactor and Jacobian to prove a positive local raw overlap and derivative contribution in the actual vacuum. Separate kinetic and potential limits give the exact aligned derivative constant 9/(8 sqrt(m)) and strengthen the local marginal lower coefficient to 27R³/16. The variational overlap constant is proved positive and retained explicitly. The full complementary interaction and original shrinking spectral window remain active calculations; no continuum no-gap endpoint is asserted.

## SZ-20261012-003 — Full physical lift and original-source spectral windows

[PLF1–PLF26](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/FULL_PHYSICAL_LIFT_AND_SOURCE.md) calculate the complete physical norm, vacuum subtraction and first two energy moments of the coupled ground-family lift. The original Wilson observable differs from an outside multiplier by a proved spectral-amplitude error at most16a_j M_f. At the original scale s_j=100kappa_*a_j, the complete corrected-source error also tends to zero. A three-scale resolvent estimate subtracts low- and high-energy contributions and gives an exact lower bound for the original physical window, with no bounded total source-norm assumption. Every complementary term is retained. The actual signed three-scale value remains to be evaluated; these formulas do not assert a continuum no-gap result.

## SZ-20261012-004 — Actual filtered currents and the complete inverse contribution

[FTC1–FTC33](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_FILTERED_CURRENT_AND_TAIL.md) transfer the original positive first energy to the outside Wilson source and prove a positive filtered-response bound with its original vanishing scale retained. The complete inverse contribution is located through an exact map from the physical window, including its full metric. Direct optimization of the filtered response retains the original force, every mixed Hessian and all exterior rows in a complete second-moment matrix. Both physical residual norms remain. An explicit comparison measure shows why the moment bounds alone do not establish surviving low-energy weight. The signed three-scale interacting response and the continuum no-gap endpoint remain active calculations.

## SZ-20261012-005 — Actual score moments and the full second-energy matrix

[SOM1–SOM24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_SCORE_MOMENTS_AND_SECOND_ENERGY.md) prove all even moments and an exponential tail for the actual conditional ground-state score at every outside configuration. A full weighted score/Hessian identity controls the second-energy matrix with all exterior rows and force cross terms retained. Its original source-vector norm is evaluated with explicit removed-face and lattice-sampling errors. The matrix trace bound is sufficient for a fully evaluated filter estimate at its stated vanishing scale; it does not improve the earlier filter bound or establish surviving low-energy weight. Source-directed inverse and residual calculations, reconstruction and the smooth no-gap endpoint remain active.

## SZ-20261012-006 — Stronger source energy and retained current inverses

[CTI1–CTI39](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURRENT_TAILS_AND_RETAINED_SOURCE.md) prove exponential tails for the complete ground-state current and a stronger lower energy for the unchanged Wilson source:
\[
\begin{gathered}
e'_{\mathbf f}=\max\{e_{\mathbf f},3\kappa_*^2J_t/4\},\qquad
J_t=\sum_d\int t_d^2,\\
\liminf_jE_{h,j}\ge e'_{\mathbf f},\quad
\liminf_jE_{F,j}\ge e'_{\mathbf f},\qquad
\liminf_j\frac{\mathcal W_{h_{e_0}\psi_j}(\theta s_j)}{a_j^3}
\ge\frac{100\theta\kappa_*(e'_{\mathbf f})^3}{D_{\mathbf f}^2}.
\end{gathered}
\]
The full original upper constants and previous lower bound remain; CTI23–CTI26 give the complete formulas and exact strict improvement for the three-orientation tent. CTI24 also proves the finite-source matrix-order bound. This strengthens CE7–CE10, EF3 and FTC4–FTC12 without changing their source, metric or regulator. CTI27–CTI37 retain asymptotically all of the original source-vector norm in a set with a proved lower trial norm and explicit inverse accuracy. The complete omitted-direction Schur term and physical residual remain in CTI32–CTI33. Their signed three-shift contribution, reconstruction and the smooth no-gap endpoint remain active calculations.

## SZ-20261012-007 — Original source Hessian and the stronger full-source response

[HSF1–HSF17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ORIGINAL_SOURCE_HESSIAN_AND_FILTER.md) evaluate the actual source-Hessian limit and retain the original energy inside the finite filter denominator. For both the full original Wilson observable \(X_j=F_j\) and its outside source \(X_j=h_{e_0,j}\), they prove
\[
\begin{gathered}
a_j\mu_j\|\nabla^2X_j\|^2\longrightarrow3J_t+9J_2^\Sigma,\\
\liminf_j\frac{\mathcal W_{X_j\psi_j}(\theta s_j)}{a_j^3}
\ge\frac{100\theta\kappa_*(e'_{\mathbf f})^3}
{\{\kappa_*^2(3J_t+9J_2^\Sigma)+4e'_{\mathbf f}\}^2}.
\end{gathered}
\]
HSF1–HSF6 retain all signed Hessian terms, original face counts and finite errors. HSF7–HSF9 prove the complete energy-dependent comparison; every original upper and lower constant remains available. HSF10 gives coefficient \(100\theta\kappa_*^3R^3/363\) for the unchanged three-orientation tent. HSF11–HSF15 apply the bound directly to the full original observable and retain every cross term in its exact relation to the outside source. This strengthens FTC12 and CTI23 while keeping the factor \(a_j^3\). The signed original-window response, full inverse and residual contributions, reconstruction and the smooth no-gap endpoint remain active calculations.

## SZ-20261012-008 — Complete residual and exact stereographic current

[TCR1–TCR21](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/TWO_SIDED_CURRENT_RESIDUAL.md) give complete two-sided bounds for the original filtered response and its signed three-shift window. They retain the actual least-squares defect and the original uncut trial metric. Projection orthogonality and a direct singular-value estimate prove
\[
\|\widetilde c\|\le\sqrt{2q_R/\gamma},\qquad
\sqrt{\kappa_*/z}\,\epsilon_R\|\widetilde c\|
=O\!\left(a_j^{\rho-3}\sqrt{\log(1/a_j)}\right).
\]
With the original CTI13 cutoff, every \(\rho>9/2\) makes this cutoff contribution \(o(a_j^{3/2})\); the interacting residual remains to be evaluated.

[SC1–SC24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/STEREOGRAPHIC_CURRENT_AND_CUBIC.md) supply the exact stereographic coordinate, density, radius-two metric and state maps for those integrals. Gauge invariance proves that each unfixed original link has a Haar marginal: its stereographic moments are finite exactly below order three. SC8–SC15 retain every rational face term and prove that the local density approximation in Chatterjee, [arXiv:2401.10507v4](https://arxiv.org/abs/2401.10507v4), label “approxdens”, omits a cubic nonabelian contribution. The full-density counterexample and corrected expression are proved without claiming that the source's main scaling theorem fails. This extends OW's ordered-action comparison and prevents an invalid polynomial-moment substitution in the current calculation. Actual window values, reconstruction, intended-theory identification and the smooth global no-gap endpoint remain active work.

The subsequent calculation [SC18–SC24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/STEREOGRAPHIC_CURRENT_AND_CUBIC.md) evaluates all five rational action terms in the actual vacuum, including with bounded gauge-invariant score multipliers. Its original four-link tensor average is
\[
\mu(q_1^a q_2^b q_3^c q_4^d)
=\frac{\mu\operatorname{Tr}U_p}{128}\,
\frac12\operatorname{Tr}(E_aE_bE_cE_d).
\]
This determines every signed term in SC10 and their exact cancellation on the original coupling path. SC24 also gives the full force pairing in original staple-loop and two-plaquette expectations, with all orientations, original coefficients and remaining mixed score moments retained. These identities evaluate gauge averages; they do not yet evaluate the complete residual or establish the no-gap endpoint.

## SZ-20261012-009 — Positive current measures and individual plaquette means

[CFC1–CFC26](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CENTERED_CURRENT_COVARIANCE.md) construct the positive original-configuration measure
\[
d\nu_e=\frac{\kappa(2R_e+G_e)+(3b/4)\sum_{p\ni e}D_p}{6b}\,d\mu .
\]
Its exact mixture and full source retain twice the force pairing. A deterministic subset carrying at least three quarters of the original squared source-norm limit has uniform tilted score tails and a trial inverse lower bound without the earlier logarithmic loss. The full complementary block and physical residual remain.

CFC22–CFC26 prove an individual-face lower mean, the resulting lower density \(3\kappa_*/16\) for every orientation of the limiting spatial vacuum mean, and
\[
K_R^{\rm kin}=\min\{K_R,\mathsf L_R-9\kappa_*R^3/16\},\qquad
\limsup a_j^2(\Lambda_Q-d_Q)\le K_R^{\rm kin}.
\]
This strictly improves the kinetic ceiling when \(\kappa_*R<128/3\), and the original gradient-trial response constants are rederived. All finite roots, counts and crossing terms remain. The force upper bound uses the original \(K_R\), not this kinetic ceiling. Spatial mean domination is not an operator lower bound for every vector or a smooth continuum field. The signed interacting source/Gram evaluation, reconstruction and smooth global no-gap endpoint remain active calculations.

## SZ-20261012-010 — Exact density flux and stronger physical residual

[DF1–DF21](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CURRENT_DENSITY_FLUX_AND_PROJECTED_RESIDUAL.md) evaluate the positive-density potential and its original-observable receiver:
\[
Y_e=\frac{\Delta_ew+2T_e}{6b},\qquad
\nu_eX-\mu X=\frac{\kappa}{6b}\mu\langle d\Delta_ew,dX\rangle .
\]
The proved mean difference is uniformly \(O(\sqrt{a_j})\) on the retained source set, using the unchanged bounded energy of the full growing observable. This requires no uniform spectral gap and retains every outside derivative.

The full collective calculation also gives
\[
\mathsf B_zc=(PD_z\mathsf Cc,zP^\perp\mathsf Cc),\qquad
z^2\mathsf N\le\mathsf Z_\star=\mathsf B_z^*\mathsf B_z\le\mathsf Z .
\]
The original force graph proves strict removal of the curl cost on every nonempty proper trial patch. The optimized augmented residual is strictly improved at at least two of the three original window shifts for all sufficiently large regulators. Complete gain formulas, projected physical norms, complementary penalties and actual cutoff errors remain in the two-sided spectral bounds. The signed window still requires the collective moments and full residual; no limiting spectral weight or smooth interacting no-gap endpoint is assumed.

## SZ-20261012-011 — Quantitative original force curl and exact patch constant

[QCF1–QCF16](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/QUANTITATIVE_FORCE_CURL.md) calculate the full ordered SU(2) mixed-face Hessian and weighted codifferential. They retain both inverse signs, the complete second face moment, every coface neighbor and outside score. The complete original face graph has the exact patch constant
\[
\mathcal G(c)\ge16\sin^2\!\left(\frac{\pi}{2q}\right)\|c\|^2,
\qquad q=\lceil R/a\rceil+3,
\]
with an explicit unscaled attaining field. The actual projected-current matrix then satisfies
\[
\mathsf Z-\mathsf Z_\star\ge m_{C,Q}(a)I,\qquad
\frac{m_{C,Q_j}(a_j)}{a_j^3}
\longrightarrow\frac{\pi^2}{32\kappa_*R^2}.
\]
The finite constant is given completely in QCF14, and the limit concerns that proved lower bound. QCF16 propagates it into the exact optimized residual gain while retaining its raw coefficient norm and both remaining positive terms. The collective signed source and physical residual still determine the original spectral window; no limiting mass or smooth interacting no-gap endpoint is assumed.

## SZ-20261012-012 — Actual source graph and its next spatial scale

[QG1–QG20](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/THREE_SHIFT_GAINS_AND_SOURCE_GRAPH.md) quantify the original three-shift augmented gains and evaluate the actual raw-source graph:
\[
a_j^{-3}\mathcal G(\mathsf b_{I_j})\longrightarrow9J_{\rm an},
\qquad
J_{\rm an}=\int\sum_{d<k}(t_d-t_k)^2.
\]
The complete face incidence improves the graph-norm constant from24 to16 and strengthens the retained-source estimates. The exact joint leading matrix has the equal-component test space as its kernel. On that space, the full original summation-by-parts calculation gives
\[
\mathbf f=(\varphi,\varphi,\varphi):\qquad
\liminf a_j^{-5}\mathcal G(\mathsf b_{I_j})
\ge36\mathcal E(\varphi),
\]
where \(\mathcal E\) is the extended Dirichlet energy. No derivative regularity of the vacuum means is assumed. QG18–QG20 propagate these results into the full joint source-force matrices at their original \(a_j^4\) and \(a_j^6\) scales, preserving mixed entries, raw coefficient norms and the complete Hessian-pair term. The noncommuting inverse and signed physical residual still determine the spectral window; no limiting mass or smooth interacting no-gap endpoint is assumed.

## SZ-20261012-013 — Complete patch Green matrix and actual source inverse limit

[GG1–GG15](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/EXACT_PATCH_GREEN_AND_PHYSICAL_RECEIVER.md) give the complete original patch Green matrix, including every longitudinal boundary mode and its raw sine norm. They evaluate the actual interacting source form:
\[
a_j^{-1}\mathsf b_{I_j}^*\mathsf G_{I_j}^{-1}\mathsf b_{I_j}
\longrightarrow
\frac94\langle h,\mathcal T_Rh\rangle,
\qquad h=f_{12}+f_{13}+f_{23},
\]
where \(\mathcal T_R\) is the fully specified Dirichlet inverse on the original physical support cube. The proof retains the full vacuum error and bounds every high and boundary mode before taking the limit. Together with QG's angular graph form, the joint limit detects every original test combination except exact zero relations. GG6–GG8 and GG14 construct the exact noncommuting map through the actual physical matrix \(Z\), preserving its nine shift-moment terms, dependent-frame kernel, graph projection residual, full Hessian-pair term and remaining optimized residual. The retained-set correction is explicit in GG13. Evaluation of the signed physical window and construction of the smooth interacting no-gap state continue.

## SZ-20261012-014 — Actual kinetic profiles and full joint shift receiver

[KP1–KP17](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_KINETIC_PROFILE_AND_SHIFT_MOMENTS.md) construct actual subsequential kinetic profiles and prove
\[
0<\tau_d\le3/\kappa_*,\qquad
\sum_d\int_{\mathcal Q}\tau_d^{-1}\le16K_R/9.
\]
The full first current-energy matrix obeys
\[
0\le Q_j\le15a_j^2/\kappa_*,
\]
with its entire positive Hessian remainder retained. One constructed actual subsequence carries the kinetic profiles, a bounded first-energy operator and every member of a finite original test family. KP11 evaluates four joint Green moments, including both mixed entries, at their unchanged \(a_j^5,a_j^6,a_j^7\) scales. KP16 gives the original source norm and energy matrices; KP15 proves their local relation to the plaquette-mean measures. The five remaining moments retain the complete current-span residual in KP13, and KP17 identifies the exact remainder-saturation space for further calculation. All raw coefficient factors, shift powers and physical residuals remain; the smooth interacting no-gap goal continues.

## SZ-20261013-001 — Full current Schur response and actual complementary measure

[CSR1–CSR21](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/FULL_CURRENT_SCHUR_AND_ENERGY_MEASURE.md) construct the full current-span Schur response with its corrected source and both physical solution components. The actual complementary coupling measure satisfies
\[
M_j([0,\theta s_j])\le1500\theta a_j^3I,\qquad
\int\lambda^{-1}dM_j(\lambda)\le Q_j .
\]
A common actual subsequence gives a bounded relative-energy measure with both endpoint atoms retained. It evaluates the effective current energy and the full complementary lift's norm and energy at their original \(a_j^4,a_j^5\) scales. The exact effective kernel includes KP17's current-trial kernel; the full physical projection and source cross measure remain in the response. All three original shifts, raw coefficient norms and complementary contributions are preserved. The signed physical window and smooth interacting no-gap endpoint remain active calculations.

## SZ-20261013-002 — Exact scalar physical receiver and stronger state bounds

[PFR1–PFR19](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHYSICAL_SCALAR_RECEIVER_AND_CURRENT_COVARIANCE.md) prove the full scalar receiver for the physical current Schur lift, including both density/score-fluctuation mixed terms. The exact diagonal Hessian defect, with all exterior rows retained, improves the actual state bounds to
\[
a_jT_e\le\Theta_0(a_j)<\frac3{2\kappa_*},\qquad
\liminf_j\frac{\mu_jD_p}{a_j}\ge\frac{3\kappa_*}{8},\qquad
0\le Q_j<\frac{9a_j^2}{\kappa_*}I .
\]
The plaquette inequality uses PFR12's uniform finite lower root; it holds along any sequence of original faces. PFR13–PFR16 strengthen the finite local budget, spatial mean floors and original observable's first-energy and resolvent coefficients. The force/source upper constant \(K_R\) is unchanged.

The KP kinetic profiles now have ceiling \(3/(2\kappa_*)\). CSR10's complementary low-energy bound is \(900\theta a_j^3I\), CSR13's measure total is at most \(9/\kappa_*\), and CSR16's derivative ceiling is \(9m!/(\kappa_*\theta^m)\). The retained finite norm terms in CSR15 and CSR19 are bounded by \(150\theta a_j^2\) and \(150a_j^2\). Earlier weaker bounds remain valid. PFR17–PFR19 supply the complete equal-time scalar covariance, inverse-energy bound and explicit positive trace defect. All raw coefficient errors, original shifts, cross covariances and physical complementary components remain. Positive first energy does not yet establish positive mass in the original shrinking spectral window; that calculation and the smooth interacting continuum endpoint remain active.

## SZ-20261013-003 — Actual physical measure, injective total and original window

[PSC1–PSC10](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PHYSICAL_SCORE_SPECTRAL_MEASURE.md) construct the actual physical current-norm measure and its complete joint source/energy measure on the original relative-energy interval. They prove
\[
\ker\mathcal M([0,\infty])\cap L^2(\mathcal Q;\mathbb C^3)=\{0\},
\qquad
d\mathcal C_j(r)=100a_j^2r\,d\mathcal M_j(r).
\]
The first statement concerns the total physical measure, including both endpoint atoms. The second preserves the exact map to the leading score covariance, whose original-scale limit is \(\mathcal G\delta_\infty\). Its possible zero coefficient is retained.

PSC7 keeps the surviving original source in one positive block measure. PSC8–PSC9 give all physical cross-shift norm, energy, source and original signed-window limits with their full factors and signs. PSC10 identifies the different kernels obtained when infinity or both endpoints are excluded. Thus total injectivity is proved without assigning it to finite relative energies. The actual allocation of mass and the sign of the original three-shift window remain active calculations toward the smooth interacting continuum no-gap goal.

## SZ-20261013-004 — Original gauge constraints, full graph receiver and stronger state bounds

[GWH1–GWH15](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GAUGE_HESSIAN_AND_COVARIANT_GRAPH.md) differentiate the original vertex gauge invariance with its full connection term, apply both endpoint constraints, and retain every outside Hessian row. They prove the stronger actual ceiling and the physical norm correction
\[
\begin{gathered}
\Theta_G(a)=\frac{-3a/2+\sqrt{9a^2/4+144/[\kappa_*^2(7/5)]}}8,
\qquad a_jT_e\le\Theta_G(a_j)<\frac3{2\kappa_*}\sqrt{\frac57},\\
\mathsf C_j^*P\mathsf C_j+\mathsf V_{g,j}\le\mathsf N_j,\qquad
c^*\mathsf V_{g,j}c
=a_j^4\mu\langle K_U^*D_cg,(K_U^*K_U)^\dagger K_U^*D_cg\rangle .
\end{gathered}
\]
The original full gauge graph, holonomy transports and all gauge zero modes remain. Horizontality of the physical exact-current columns follows from their proved gauge invariance and projection equivariance. The full row minimum and its complete residual are GWH8–GWH9.

GWH6 and GWH12–GWH15 propagate the finite root through the complete current and scalar covariance bounds, complementary spectral measure and derivatives, original cube budget and oriented means, first-energy and both original resolvent trials, and the exact density variance. The scalar-score low-energy ceiling is \(100\theta\Theta_G(a_j)\); the current energy ceiling is \(a_j^2(3/\kappa_*+4\Theta_G(a_j))\). The complete four mixed density/score terms, raw coefficient errors and source upper constant \(K_R\) remain. The actual physical total satisfies
\(\mathcal M([0,\infty])+\mathcal V_g\le M_{\mathbf1_{\mathcal Q}\tau}\).
These strengthen the existing receivers without assigning physical mass to a spectral interval. The original window and interacting smooth global no-gap endpoint remain active.

## SZ-20261013-005 — Full gauge-current covariance and exact dynamic curl

[GCM1–GCM16](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/GAUGE_CURRENT_COVARIANCE_AND_DYNAMIC_CURL.md) retain the complete vertex cross covariance and prove the full matrix lower bound
\[
\mathsf V_g\ge a_j^4\mathsf A_0\mathsf A_1^\dagger\mathsf A_0
\ge\frac{a_j^4}{12}\mathsf A_0,\qquad
\mathsf A_0=\mu B_U^*B_U,\quad
\mathsf A_1=\mu B_U^*(K_U^*K_U)B_U .
\]
The physical source-energy receiver keeps this entire correction. Its scalar inverse and continuum inverse-half domains are proved in GCM6–GCM9. The single-edge bound \((\mathsf V_g)_{ee}\ge2\mathsf N_{ee}/7\) is a diagonal statement: the full original constant list has \(\mathsf V_g\mathbf1=0\) and \(P\mathsf C\mathbf1=\mathsf C\mathbf1\). No factor inferred from the diagonal replaces the actual matrix.

The original contraction \(\mathscr T\alpha=K_U^*\alpha^\sharp\) satisfies
\[
\mathscr T L_1-L_0^{\mathbb V}\mathscr T
=\kappa_*\mathscr R\,d,\qquad
\mathscr R\omega=\mathscr S_U((*_e\omega_{ee})_e).
\]
GCM13–GCM16 prove every connection sign, the \(12\) degree bounds, the current identity with zero initial diagonal curl, and the complete two-form resolvent correction. GCM10–GCM12 construct the graph-energy receiver for a common smooth spatial weight, with no infinity atom at \(\lambda/a_j^2\). Its connection to physical time energy \(\lambda/s_j\) remains the exact norm and dynamic maps above. All endpoint atoms in the physical measure, original raw coefficients, mixed scalar kernels and the signed physical window remain.

## SZ-20261013-006 — Two-form force spectrum and the common physical source

[TFC1–TFC26](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/TWO_FORM_FORCE_AND_COMMON_SPECTRUM.md) prove the full original force-curl receiver, including
\[
L_2d\mathsf Cc=-a_j^2d(D_cdV),\qquad
\mathsf N^\perp=\kappa_*a_j^4
\int_{(0,\infty)}\lambda^{-3}\,d\Omega_j(\lambda).
\]
The actual force covariance tends strongly to \(9/\kappa_*^2\) times the direction-difference projection on the original support cube. Its kernel is exactly the common-coefficient subspace. For a common \(C_c^1\) coefficient, TFC15 evaluates the next spatial term and TFC21–TFC22 prove a uniform removed-current second moment at the unchanged energy. All face deficits, their second moments, outside neighbors and limiting zero atoms remain.

The original common plaquette observable \(X_{\varphi,j}\) and the explicitly defined centered squared-score observable \(Q_{\varphi,j}\) satisfy
\[
dX_{\varphi,j}+dQ_{\varphi,j}
=-\frac{\kappa_*a_j}{2}L_1P\mathsf Cc_j+Pe_{\varphi,j},
\qquad \|e_{\varphi,j}\|=O(a_j).
\]
TFC23–TFC25 prove the complete low-band and original three-shift comparisons. The displayed scaled response error is \(O(a_j)\); its unscaled error is only \(O(1)\), and no positive window sign is inferred. TFC26 proves that the leading full Hessian-pair remainder kills the common subspace, with \(\mathcal Qh=\kappa_*\mathcal Gh\) there. These formulas strengthen the existing physical, score and force receivers while leaving the actual spectral allocation and interacting smooth global no-gap construction active.

## SZ-20261013-007 — Common scalar source and original physical mass

[TSC1–TSC12](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SCALAR_COMMON_SOURCE_RECONSTRUCTION.md) integrate the common-source gradient identity with every original centering constant:
\[
X_{\varphi,j}+Q_{\varphi,j}
=\frac{\kappa_*^2a_j^3}{2}B_{c_j}+r_{\varphi,j},
\qquad r_{\varphi,j}=\kappa_*L_0^{-1}\delta_\mu e_{\varphi,j}.
\]
The full scalar score term has norm \(O(\sqrt{a_j})\). For every Borel subset \(B\subset[\epsilon s_j,\infty)\), the exact finite estimate proves
\[
\|E_0(B)(X_{\varphi,j}+Q_{\varphi,j})\|
\le d_{\varphi,j}(\epsilon s_j)=O(\sqrt{a_j}).
\]
Consequently the original \(X\) and squared-score \(Q\) masses have equal extended liminf and limsup on every such sequence of bands, including the original shrinking annulus. This compares the actual unweighted physical masses without assigning a positive value to either one. TSC8–TSC9 retain all three original response shifts and give explicit signed bounds. TSC10–TSC12 evaluate the actual mixed density/score covariance combination and give a whole-variance floor of order \(a_j\). The weighted Poisson residual at zero, all mixed terms and original coefficient norms remain. The spectral allocation and smooth interacting continuum no-gap construction continue.

## SZ-20261013-008 — Scalar residual and local-energy moment geometry

[SLE1–SLE24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SCALAR_RESIDUAL_AND_LOCAL_ENERGY.md) identify the full scalar residual with the original centered weighted energy:
\[
r_{\varphi,j}=D_{\varphi,j}
-\frac{\kappa_*^2a_j^3}{2}\upsilon_{c_{\varphi,j}},
\qquad \|D_{\varphi,j}\|=o(1)\quad(\varphi\in C_c^1).
\]
The original interpolation covariance gives the sharper \(O(a_j)\) error for \(C_c^2\), with both cell and face terms retained. SLE8 compares the full spectral roots on every Borel set, including energy approaching zero. For \(v_e=(A_e-m_e)\psi\), the first energy matrix satisfies
\[
\mathsf E_{ef}=\tfrac12\langle\psi,[A_e,[H,A_f]]\psi\rangle,
\qquad \operatorname{dist}_{\rm coface}(e,f)>2\Longrightarrow\mathsf E_{ef}=0.
\]
SLE17 retains the exact six/eight-edge Wilson difference at distance two; the ordinary and second-energy covariance matrices retain every spatial pair. SLE19–SLE22 derive all three original inverse moments from the same actual score-contracted source measure. SLE23–SLE24 prove that the geometric field kernel consists exactly of constants and characterize the remaining energy-vector kernel by ground-density-preserving flows. These complete finite-regulator results strengthen the original receiver without assigning a positive shrinking-annulus mass. The interacting smooth global no-gap construction remains the goal.

## SZ-20261013-009 — Original face action and the ground-density defect

[FPA1–FPA11](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/FACE_FIELD_PHYSICAL_ACTION.md) calculate the original field action on every elementary face:
\[
Y_cD_q=\sum_{\substack{p\ne q\\p\cap q=\{g\}}}
(c_g-\bar c_p)\theta_{pq,g}.
\]
Independent central link characters isolate every term. Their exact Haar coefficient is \(3/16\), giving
\[
\sum_q\|Y_cD_q\|_{\rm Haar}^2
=\frac3{16}\sum_p\sum_{g\in\partial p}(m_g-1)|c_g-\bar c_p|^2 .
\]
Every nonconstant original coefficient array therefore changes at least one gauge-invariant face observable. The actual interacting form retains all cross terms through the exact density component \(\Pi_{\partial p\triangle\partial r}(\psi^2)\); it has not been replaced by Haar measure. FPA9–FPA11 derive the full score-source equation and kinetic-deformation cancellation, including the original Ricci coefficient \(1/2\). A possible nonconstant energy-kernel field preserves the ground density while acting on observables. Its density contributions and physical-window inverse moments remain the next calculation toward the smooth interacting global no-gap goal.

## SZ-20261014-001 — Actual density characters and quantified central-reversal escape

[DCH1–DCH22](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_DENSITY_CHARACTERS.md) derive the complete original density-character equations, including the kinetic-density and weighted local-energy sources. For every original face collection \(A\), the exact map satisfies
\[
\begin{gathered}
\|\rho_{S_A}-\sigma_A\rho_\varnothing\|_1
=2\mu(\mathcal T_A<0)\le\sum_{p\in A}\mu D_p,\\
[1-\tfrac12\sum_{p\in A}\mu D_p]_+
\le\|\rho_{S_A}\|_1\le1 .
\end{gathered}
\]
All physical face cross terms retain their actual central density and a proved mixed-deficit error. For the original common smooth coefficients, DCH15 bounds the actual face-action form uniformly, while DCH16 gives its full Haar comparison \(9(16a_j)^{-1}\int|\nabla\varphi|^2+o(a_j^{-1})\). DCH17–DCH22 calculate the original central-reversed ground's spectral weight: it concentrates near the full energy \(4b_jM_j\), and its mass in each fixed multiple of the original shrinking window is \(O(a_j^2)\). The original scalar observable and squared-score source retain their own unresolved signed response. The even-density Gram and complete kinetic-density sources are the next receiving calculation toward the smooth interacting global no-gap goal.

## SZ-20261014-002 — Complete central kinetic source and physical resolvent

[CK1–CK24](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CENTRAL_KINETIC_SOURCE.md) calculate the complete central-orbit kinetic source and its exact original-Hamiltonian representation. The actual marginal amplitude \(A=\sqrt{\rho_\varnothing}\), probabilities \(p_\tau=\rho_\tau/(2^{N_j}\rho_\varnothing)\), and \(h_\tau=\sqrt{p_\tau}\) satisfy
\[
\Pi_\varnothing|d\psi|^2=|dA|^2+A^2\sum_\tau|dh_\tau|^2 .
\]
All nonempty-character cross terms are retained. The full physical operator couples the central-average component to its fluctuation through
\[
Bf=-2\kappa_*(\langle dh_\tau,df\rangle)_\tau .
\]
CK19–CK24 prove the complete two-component resolvent on its exact form domains, retaining both source components, their cross terms, shift derivatives and the nonnegative residual gain over the central-average trial. The original squared-resolvent response is \(z\mathcal G_Z(z)-z^2\|(\mathcal M+z)^{-1}\mathbf Z\|^2\); all three original shifts and signs remain. The actual gain at one shift does not assign a positive signed three-shift limit. That joint evaluation, reconstruction and the smooth interacting global no-gap endpoint remain active.

## SZ-20261014-003 — Exact central fluctuation energy and full response residual

[CFE1–CFE14](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CENTRAL_FLUCTUATION_ENERGY.md) compute the original conditional mean-gradient defect \(t_Z=dx-\sum_\tau p_\tau dZ_\tau\), its complete adjoint coupling, and the full positive fluctuation energy
\[
q(y,y)=\kappa_*\int A^2\left[
\sum_\tau p_\tau|dZ_\tau-v_Z|^2+|t_Z|^2\right]dU,
\quad v_Z=\sum_\tau p_\tau dZ_\tau .
\]
Every nonempty original character is retained in \(C_{S,T}=r_{S\triangle T}-r_Sr_T\). Its exact inverse contains \(n^{-2}\sum_\tau\chi_S\chi_T/p_\tau\). The full physical residual \(\eta_z=y-B(L_A+z)^{-1}x\) has the exact Gram square in CFE13, including its possible cross-term cancellation. CFE7–CFE8 bound all three original signed responses, and CFE14 derives the density-character derivative source from the original Wilson ground equation. These formulas keep every raw coefficient, metric, boundary and inverse probability. The actual derivative estimates and nonzero shrinking-window weight, followed by reconstruction and the smooth global no-gap endpoint, remain the active calculation.

## SZ-20261014-004 — Central configurations and strict physical resolvent gain

[FPR1–FPR8](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CENTRAL_FIXED_POINT_RESIDUAL.md) prove that global gauge isotropy makes every first derivative of a smooth physical scalar vanish at each original central configuration. Thus \(Bf_z^0(I)=0\), and every nonzero original sampled face test has the strictly positive residual
\[
\sum_\tau|\eta_{z,\tau}(I)|^2
=a_j^2\sum_{p,r}\overline{\varphi(x_p)}\varphi(x_r)
C_{\partial p,\partial r}(I)>0.
\]
The full original norm has the explicit radius-two product-ball bounds FPR4/FPR7. With \(m_z=\|\eta_z\|^2\) and the complete residual energy \(e_z\) in FPR5,
\[
\mathcal G_{X_\varphi}(z)-\langle x,(L_A+z)^{-1}x\rangle
\ge\frac{m_z^2}{e_z+zm_z}>0.
\]
FPR6–FPR8 calculate the exact covariance and residual-density curvature, retaining the original potential, vacuum energy, Casimir factor and Hessian cross term. This strengthens CK24 at each finite regulator. The product volumes and derivative maxima retain their full regulator dependence; the signed three-shift limit and the smooth global no-gap endpoint remain active.

## SZ-20261014-005 — Actual central Hessians and full original face maps

[CHM1–CHM13](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/CENTRAL_HESSIAN_FACE_MAP.md) prove the complete central Hessian form \(\mathscr H^f=K^f\otimes I_3\), all original vertex constraints, an explicit integer face filling and the exact map \(K^f=R(FK^fF^{\mathsf T})R^{\mathsf T}\). Both face Gram factors and the full colour factor \(3\) remain in the FPR8 receiving contraction. The actual original conditional ground Hessians satisfy
\[
K^{\mathcal F}=2\mathfrak V,\qquad
\mathfrak V=\sum_\tau p_\tau(K_\tau-\overline K)^2\ge0,
\quad \Delta\mathcal F(\mathbf I)=6\operatorname{Tr}\mathfrak V.
\]
CHM9 proves its strict original-state curvature bound with the complete face covariance and circulation dimension. CHM10–CHM13 calculate every original second/fourth-derivative ground, marginal, test-source, resolvent and character term, including both matrix product orders. The global Wilson-word realization CHM6 does not assign an actual ground state. The actual matrix estimates and signed shrinking-window response, followed by reconstruction and the smooth global no-gap construction, remain active.
