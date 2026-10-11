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
