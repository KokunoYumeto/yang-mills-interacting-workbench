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
