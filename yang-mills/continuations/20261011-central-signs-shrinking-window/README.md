# Yang–Mills phase moments and central link symmetry

This continuation calculates the original polynomial phase observable in the actual interacting vacuum, improves its bound on the prescribed growing-box path, and completes the odd-order Jacobian return calculation. It belongs to the S6 and Navier–Stokes inspired Yang–Mills programme.

The original path remains \(L_j=j^4\), \(a_j=1/(100j)\), \(g_j^2=\kappa_*/(200j)\), with window \(s_j=\kappa_*/j\). Its actual positive low-energy weight and the interacting continuum no-gap result remain to be established.

- [Original phase moments and the unchanged shrinking window](PHASE_MOMENTS_AND_ORIGINAL_PATH.md), IP1–IP22: exact original-word occurrence sums improve the negative loss bound from order \(j^{31}\) to order \(j^{23}\). The actual vacuum equation gives all potential moments and controls unbounded polynomial multipliers at each fixed box. The original \(x-y\) vector has limiting raw norm squared \(12\), first energy moment \(12\delta_*\), fourth moment \(720\), and first odd-cluster weight \(12\). All polynomial Gram and energy limits are evaluated, with their exact degenerating rank.
- [All odd Schur coefficients and the complete even tail](ORIGINAL_J5_PARITY_AND_TAIL.md), P1–P45: an explicit central-sign involution preserves every original gauge constraint, spin block and union label. Each odd-degree face-return word is zero. The full complementary inverse, even remainder, original vacuum scalar and full nonlinear interior inverse have proved bounds.
- [Central signs and the exact boundary obstruction](CENTRAL_SIGNS_AND_BOUNDARIES.md), CS1–CS19: every open box has one physical face-reversing sign map. A periodic rectangular box admits these maps exactly when at most one side length is odd; its eight central gauge classes retain the three winding signs. The full Hamiltonian identity includes \(4\kappa M\xi I\).
- [Original first Jacobian block and return](BASELINE_J5.md), J1–J7: preserved complete provider for the outgoing channels and second coefficient. Its formerly unfinished third coefficient is settled in P26.

The fixed-box phase limit cannot yet be exchanged with the specified joint path: IP22 retains an explicit tail coefficient growing as \((35831808/\pi^4)n^{12}\). The improved joint-path lower bound still has a negative endpoint. Neither statement supplies the missing positive limiting weight.

The center-reversal mechanism has an antecedent in [L. Li and Y. Meurice, Lattice gluodynamics at negative \(g^2\)](https://arxiv.org/abs/hep-lat/0410029v2). The proofs give the exact comparison to their conventions and preserve the scope of their periodic construction. No novelty claim is made.

[Complete combined TeX source](RESEARCH_CONTINUATION.tex) retains every mathematical block from the four proofs. Compilation is pending because the shared TeX slot was occupied at three natural build checkpoints. The [source-fidelity record](TEX_FIDELITY.json) records the verified source identities; no new PDF is represented as compiled.

Reproduce the independent finite checks with Python, using mpmath for the phase enumeration: check_central_signs.py, verify_phase.py, and verify_jacobian.py. The nine exact incidence cases, 32 phase checks, and rational Jacobian certificates supplement the complete proofs. The two current figures and the original Jacobian figure have retained sources. [Source identities and reading coverage](SOURCE_READING_USE_LEDGER.json) and [claim propagation](CLAIM_LEDGER.md) accompany this edition.

The next direct spectral calculation is a volume-dependent estimate of the actual reflected four-loop and gradient difference with accuracy sufficient for division by \(s_j\). The Jacobian continuation now starts with its fourth coefficient. These are distinct calculations within the continuing programme.

## Complete fixed-box spectral weights

The [spectral continuation](PHASE_SPECTRAL_WEIGHTS.md), SP1–SP16, evaluates every limiting cluster-weight matrix for the original polynomial family by a finite Hermite sum and a full determinant formula. It proves convergence of the corresponding actual fixed-box spectral measures. For the original cubic vector the raw weights are 2700, 2160 and 1440 at the three energies δ*, 2δ* and 3δ*. The original two-dimensional phase compression has an exact omitted energy contribution 864δ*²; the minimal invariant oscillator space includes the radial polynomial uq. The 12δ*/5 variational value is accounted for by its two occupied energies. The simultaneous growing-box estimate is still required.

The [104 exact checks](PHASE_SPECTRAL_CHECKS.json) compare independent Hermite, determinant and moment calculations. [Reproducible spectral figure](PHASE_SPECTRAL_WEIGHTS.png) shows all raw masses, with its source retained.
