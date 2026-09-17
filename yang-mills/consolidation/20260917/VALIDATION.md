# Mathematical verification and reproduction

This collection studies the vacuum and excitations of the original open-box SU(2) lattice Hamiltonian, with all vertex gauge constraints imposed. Its fourth-order vacuum source is given in two different coordinate descriptions. Its sixth-order energy includes the contribution from the six faces of a cube. Written estimates then connect the source calculation to a positive vacuum and a lower bound for the full physical spectral gap at sufficiently strong coupling.

The verification has three distinct parts: exact finite polynomial calculations, an independent comparison between coordinate descriptions, and review of the analytic arguments that pass from finite coefficients to an actual eigenfunction and spectral estimate. A successful finite calculation does not replace the last part. The proofs, programs and receipts are all retained so that these parts can be examined separately.

## What was checked

| Calculation or argument | Evidence and extent |
| --- | --- |
| Fourth source in original trace words | The complete producer was rerun in ordinary and optimized Python. Each run passed 1,056 named checks and 19 false-formula controls, and reproduced all five generated tables and the entire receipt. |
| Fourth source in tree-quaternion coordinates | The preserved producer reconstructed its complete mathematical receipt: 630 named checks and nine false-formula controls. The public replay also verifies every admitted source hash. |
| Equality of the two descriptions | An independent rational-polynomial program compared all 78 connected fourth-order representatives. Every difference was identically zero in the SU(2) coordinate ring. All 8,621 anchored multisets had the same representative and the same selected signed-coordinate transport. |
| Signed response to separate plaquette couplings | The preserved checker reproduced 2,156 polynomial equations: 282 base equations with the plaquette forcing subtracted and 1,874 positive-degree equations. It also reproduced the 282 expanded degree-three response entries. |
| Sixth-order cube contribution | A separate geometric calculation, importing neither producer, exhausted all 720 face orderings and the independent twenty-term three-face/complement pairing. Both give −83/1944. |
| Finite-box multiplicities and energy polynomial | A separate incidence calculation enumerated boxes of side length m = 2,…,8 and checked the displayed support counts and their rational weighted sum. General counting proofs are supplied in the energy notes; finite enumeration is a corroboration, not their substitute. |
| One-face coefficients | A separate SU(2) character recurrence checked every coefficient equation through degree six and recovered both the one-face fourth logarithmic coefficient and sixth energy coefficient. |
| Gap endpoint and numerical benchmarks | A separate integer/Fraction calculation checked the discriminant signs, coupling enclosure, exact residual bounds and outward-rounded displayed benchmarks. It takes the displayed coefficient budgets as inputs. |
| Passage to the full physical spectrum | The written source-space, derivative, convergence, positive-vacuum, elliptic and spectral arguments were reviewed separately. No missing implication was found within their stated finite-regulator scope. These analytic proofs are not Lean-formalized. |

The two principal implementations use different recurrences: one works with trace-word sources, while the other constructs a Haar-centered eigenvector and then its logarithm. Within each implementation, some tests share algebraic primitives. In particular, the quaternion source and tangent computations share the same differential operator and Haar-moment routines. Their agreement is therefore not described as completely independent implementations of every operation.

## Why the coordinate comparison proves an identity

Choose the stored spanning tree for a connected plaquette support. A gauge transformation sends every tree link to the identity. The remaining chord link c has coordinate

\[
Z_c=h_{s(c)}U_c h_{t(c)}^{-1},
\]

where h is the ordered tree-path product from the root. Every trace word in the first catalogue is a closed loop, so its trace is invariant under this transformation.

For each chord, write

\[
Z_c=q_{c,0}I-i\sum_{a=1}^{3}q_{c,a}\sigma_a,
\qquad \sum_{a=0}^{3}q_{c,a}^{2}=1.
\]

The comparison program independently multiplies Hamilton quaternions, replaces a trace by twice its scalar coordinate, and expands products over the rational numbers. It reduces by the sphere relation for each chord, using q₀² = 1 − q₁² − q₂² − q₃². The resulting polynomial dictionary agrees exactly with the second catalogue for every representative: 743 trace-monomial terms become 4,044 nonzero coordinate monomials. This is a whole-polynomial comparison, not a check at selected link values. Equality on the tree slice, together with gauge invariance, gives equality for every original SU(2) link assignment. The checked transports extend it to all stored anchored supports.

The original trace verifier also checks directional derivatives at two deterministic exact assignments for each representative. Those 156 tests remain useful regressions, but by themselves they would not prove a polynomial identity. The independent coordinate comparison and the expanded quaternion equations supply the stronger finite algebraic checks.

## What the signed-response certificate says

With separate plaquette couplings λₚ and the Haar-centered source

\[
v(\lambda)=\sum_\nu\lambda^\nu v_\nu,
\qquad Z_{p,\rho}=(\rho_p+1)v_{\rho+e_p},
\]

the differentiated coefficient equation is

\[
KZ_{p,\rho}-2Q_H\sum_{0<\mu\leq\rho}
\Gamma(v_\mu,Z_{p,\rho-\mu})
=\delta_{\rho,0}W_p.
\]

The 2,156 equations have zero residual **after subtracting the right-hand side**. In particular, their degree-zero equations are KZₚ,₀ − Wₚ = 0, not KZₚ,₀ = 0. The counts are class-indexed checks: lower-degree entries can recur in more than one fourth-order downset.

These are exact finite Taylor coefficients of the response. They do not make a truncated response an exact inverse of the full linearized operator. The nonzero higher-degree residual is displayed in the signed-tangent proof. The separate physical-return proof constructs its actual linear inverse and controls the nonlinear correction by convergent series.

## Sixth order and the relation between the packages

Both calculations give

\[
e_{6,L}=-\frac{211396463m^3+30959193m^2+21845782m+2336684}
{4691494080},\qquad m=2L.
\]

The apparent factor of two in their adjacent-pair entries is a difference in aggregation: 22285/47309184 is the coefficient of one multiplicity assignment, λₚ⁴λ_q². Interchanging p and q contributes equally. Their sum is the second package's unordered-pair weight 22285/23654592. Neither calculation changes the coupling or trace convention.

For a cube, the independent face-ordering calculation gives an electric-resolvent sum 166/243. The Haar contraction contributes 1/16, so the energy contribution is −83/1944. The independent complementary-triple calculation gives the same number. One-face and cube weights have these additional independent derivations; the other local weights were reproduced in the full package replays and compared between deliveries.

The two remainder estimates serve different purposes. The source-based estimate is uniform in volume on |ξ| < 1/60. The second package also gives a direct finite-volume perturbation argument on |ξ| < 3/(8M), where M is the number of plaquettes. That latter radius decreases with volume. It is not presented as a replacement for the former argument.

## Analytic scope

The physical-return argument retains all degrees five through eight of the quartic reference residual, constructs the true source through a convergent Neumann/Catalan expansion, and proves that its exponential is the actual positive ground state. Smooth spectral resolution on the finite product of SU(2) then allows the coefficient estimate to be applied to every physical excitation, not only to a finite trial subspace. The endpoint is included by absolute convergence of the Catalan series, rather than by assuming a strict contraction there.

These steps were checked as written mathematical proofs. The elliptic ingredient is the compact-manifold regularity and spectral theorem in Peter B. Gilkey, *Invariance Theory, the Heat Equation, and the Atiyah–Singer Index Theorem*, first edition, Lemma 1.3.5 (p. 30) and Lemma 1.6.3 (pp. 43–44); see the [author-hosted edition](https://pages.uoregon.edu/gilkey/dirPDF/InvarianceTheory1Ed.pdf). The published collection cites this source; it does not redistribute the book.

The conclusion is a bound for the complete physical spectrum of the stated lattice Hamiltonian, uniform in finite spatial box size on a specified strong-coupling interval. It is not a construction of a four-dimensional continuum Yang–Mills field, a positive continuum mass, or a claim that the sufficient endpoint is a physical singularity. No machine proof of the analytic argument is claimed.

## Reproducing the calculations

The original source and historical receipt files are unchanged. The public tree retains both continuation directories and the cubic predecessor required by the trace producer. The programs use standard-library Python; the recorded replays used CPython 3.13.9 on Windows.

From this consolidation directory, run:

```sh
python -B verification/run_checks.py --output-dir verification/runs/my-replay
```

The destination must be new. The runner executes the trace verifier twice, then the quaternion verifier, tangent verifier, independent coordinate comparison, one-face recurrence and scalar checks, one worker at a time. Every worker has a 600-second wall limit, one CPU and a 2 GiB cap. On Windows the cap covers process and aggregate Job Object committed memory; on supported POSIX systems it bounds address space. The runner records the actual limit readbacks where available, exit codes, output hashes and source hashes before and after. A failed or incomplete run is not a pass.

Individual checks can be selected, for example:

```sh
python -B verification/run_checks.py --checks bridge tangent --output-dir verification/runs/my-comparison
```

The extra cube/count checker has its own Windows Job Object cap and may be run as:

```sh
python -B verification/independent_cube_counts_windows.py
```

Do not use Python's `-O` switch for the small independent one-face, cube/count or scalar scripts: their diagnostic assertions are deliberately active. The original trace verifier uses explicit error checks and was separately replayed under `-O`.

Two additive wrappers address platform-specific serialization, without changing mathematical source code. `regenerate_portable.py` writes the original trace producer's tables as explicit UTF-8/LF bytes to a new destination. The quaternion replay uses forward-slash receipt paths and excludes one raw conversation transcript from fresh public provenance checking. All mathematical source files are still hashed and all mathematical receipt fields compared. See [the public-edition explanation](../../continuations/20260917-quartic-independent/PUBLIC_EDITION.md) for exact commands and the explicit exclusion.

To regenerate the trace tables rather than only check the supplied ones, run the following from `continuations/20260917-quartic-cube/`, choosing a destination that does not already exist:

```sh
python -B regenerate_portable.py --output-dir generated-replay
python -O -B verify.py --verify-receipt generated-replay/verification.json
```

The Windows roundtrip reproduced all six supplied output files byte for byte, including their canonical receipt hashes. An attempted reuse of the output directory was rejected before computation and left its files unchanged.

## Reading the receipts

The [verification directory](verification/) contains the selected fresh mathematical receipts, the independent programs, and the public-edition execution record. The original historical receipts remain beside their original programs. A check count measures named tests, not independent theorems. Neither checksums, test counts nor agreement between programs replace the definitions and proofs in the reader.

The raw input transcript and private workstation run manifests are excluded from the public edition. Its exclusion is stated in the public replay receipt, along with its historical hash; the public replay does not claim to have freshly checked a file it does not distribute. All supplied mathematical source and certificate files are retained.
