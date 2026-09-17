# Audit, corrections, and completed calculations

17 September 2026. Requested basis: the exact uploaded `Pasted markdown(6).md`.

## Result in brief

This package repairs the recoverable transcript, independently checks its explicit scalar arithmetic, supplies a complete exact fourth-order logarithmic-vacuum source catalogue, and calculates the complete sixth-order ground-energy coefficient of the original three-dimensional open SU(2) box. The sixth-order result includes the six-distinct-face elementary-cube contribution. The complete new calculation is accompanied by a finite-volume analytic remainder and executable exact arithmetic.

The earlier strong-coupling gap and convergence claims are retained as historical source assertions. This session audits their displayed finite arithmetic, but does not independently certify the full chain of their analytic norm estimates, full-domain spectral arguments, or volume-limit claims. No further coupling-threshold improvement or continuum mass-gap solution is claimed here.

## 1. What the uploaded material actually contains

The upload contains part of the previous cubic/linearized proof, a printed inventory of historical `/mnt/data` files, an old ZIP directory listing, and the start of a fourth-order session. It contains the status text “Computed sixth-order linked-cluster coefficients”, but no sixth-order formula, calculation, or receipt. The actual fourth-order output is also absent. A status caption does not supply the missing result.

The original file is preserved byte-for-byte in `input/`. Its historically printed filenames are listed in `sources/historical_artifact_inventory.json`, explicitly marked as unavailable original files in this runtime. A filename inside a transcript is not a mounted attachment. The old session ZIPs have not been fabricated or silently represented as recovered.

The authenticated GitHub read located the actual cubic PR8 at the pinned revision `91434b6962062bd80439d4cb2cae9d2479264dde`. It was an open draft at the time of reading. The exact original geometry source was recovered and its Git blob verified. The proof bodies were consulted through the connector; the whole historical ZIP was not accessible as an attachment in this session. The optional `sources/recover_pinned_github.py` can retrieve the committed text files at that immutable revision on a network-enabled machine. It never runs downloaded code automatically.

## 2. Corrections and distinctions

### Corrupted transcription

The pasted Python lost indentation and equality/inequality symbols, producing strings such as `if ji`, `if atroot`, and `if len(set(ps))1`. The recovered `geometry.py` has the original `if j==i`, `if at==root`, and `if len(set(ps))==1`, plus its original indentation and all source bytes. Its Git blob is `c8d385b276909ea1e885747c42773e64e9553c87`. This repairs the transcription; it does not invent a replacement graph.

`recovered/linearized_excerpt_clean.md` repairs escaped underscores and the damaged Catalan notation while explicitly marking that the supplied proof ends mid-sentence. The untouched upload is retained for comparison. No missing paragraphs were silently completed in that recovered excerpt.

### Residual term versus the full fourth coefficient

At `q2=xi v1+xi^2 v2`, the source residual is

    R2=xi^3 v3+xi^4 B(v2,v2).

The full fourth vacuum coefficient has the additional incoming term:

    v4=2B(v1,v3)+B(v2,v2).

The uploaded equations correctly define the residual. They do not by themselves complete v4. The new catalogue computes the signed sum of both contributions. On one original plaquette the result is

    v4^(p,p,p,p)=17 chi1(Omega_p)/10368-7 chi2(Omega_p)/51840.

The added incoming term beyond b22 is exactly `chi1/648-chi2/9720`. This is an explicit source difference, not a substitution of one object for another.

### Four faces can require five independent chord coordinates

A four-face cube-side tube has five independent graph cycles. It is class25 of the catalogue. Any implementation that presupposes one chord variable per face would lose one original coordinate on this support. The new tree-coordinate map uses the actual rank `|E|-|V|+1`; its inverse, original kinetic fields and gauge return are given in the proof and JSON. The exact kinetic calculation includes all original tree-edge derivatives.

### Sixth order requires a six-face closed surface

At order six, a scalar contribution can have either all-even face multiplicities or the six distinct faces of an elementary cube. The original link-center symmetries and cubical boundary argument prove this classification. The cube's Haar product is exactly `1/16`, and its 720 time-ordered insertions give linked weight `-83/1944`. Omitting it changes the three-dimensional answer. A separate three-plus-three calculation reproduces it.

This is a necessary term discovered in completing the missing calculation, not a claimed numerical correction to an old sixth-order value—the upload provided none.

### Finite arithmetic and analytic proof have different scopes

The inherited `ell`, `delta`, quartic discriminant, root enclosure, physical-parameter conversion, and stated `xi=1/64` benchmark all pass the separate scalar audit. That audit uses the original coefficient-bound inputs as written. It does not prove those inputs or transform passing regression tests into an independent proof of a uniform mass-gap theorem.

The new coefficient identities are established by complete rational-polynomial residuals in the original SU(2) quotient algebra. Original-link Taylor-jet evaluations are additional independent regression tests. The written coordinate, topological, and analytic-remainder arguments remain available for independent mathematical review; no new Lean or external analytical review has been performed.

## 3. Completed fourth-order catalogue

There are 8,621 anchored connected face multisets of order four. The original cubic-lattice isometries and translations partition them into 78 classes: one of multiplicity4, two of3+1, two of2+2, nineteen of2+1+1, and fifty-four with four distinct faces.

The 78 files in `results/quartic_coefficients/` contain all4,044 nonzero rational monomials, with original faces, tree links, chords, derivative fields, source multiindices, and full Haar means/norms. Each class is reconstructed once; its geometric multiplicity is recorded separately. The complete finite-box coefficient is obtained by pulling back the representative through its explicit original lattice and tree maps and summing every contained multiset once.

Across all coefficient downsets, 1,053 exact inverse equations and 1,053 exact logarithmic-source equations are executed. The tangent coefficient in every original plaquette direction through degree three is also explicitly evaluated. A separate direct-logarithm recurrence reconstructs all78 coefficients independently, then verifies2,156 complete polynomial tangent equations and stores282 expanded signed response entries. These finite signed tangent data are not promoted to an unevaluated all-order operator estimate.

## 4. Completed sixth ground-energy coefficient

Write

    H/kappa=K+xi(2M-S), kappa=2g^2/a, xi=1/(4g^4),
    E0/kappa=2M xi+e2 xi^2+e4 xi^4+e6 xi^6+R8.

The connected weights at sixth order are

| Original connected support | Weight |
|---|---:|
| One plaquette | -289/77760 |
| Adjacent pair | 22285/23654592 |
| Three-face path | -4909/118272960 |
| Three faces on one edge | 244/4312035 |
| Cube-corner triple | -212/542997 |
| Six distinct cube faces | -83/1944 |

For `m=2L`, retaining the original open boundaries, the complete coefficient is

    e6=-(211396463 m^3+30959193 m^2+21845782 m+2336684)/4691494080.

For the original `L=2` box, this gives

    E0/kappa=480 xi-80 xi^2+(1198/351)xi^4
              -(3528610133/1172873520)xi^6+R8(xi).

The analytic proof in `proofs/SIXTH_ORDER_ENERGY.md` establishes the independent finite-volume error bound

    |R8(xi)| <= (3/4) (|xi|/R)^8/[1-(|xi|/R)^2],
    R=3/(8M), |xi|<R.

At L=2, R=1/640. The physical error is kappa times this expression. The volume dependence remains explicit.

The one-plaquette coefficient is independently checked against NIST DLMF28.6.5 using the exact original parameter map `e_one(xi)=b2(-4xi)/4-1`. The standard exponential-vacuum and linked-source framework is credited to the inspected primary literature. This verifies the one-plaquette convention; it does not assert that the full spatial result is historically new or externally reviewed.

## 5. What the ZIP includes and how to use it

Read the two proofs first; then run `python -B checks/verify.py --verify-receipt results/verification.json` from the extracted root. The corresponding `-O` command executes the same explicit checks. All dependencies are included and use Python's standard library. `checks/replay.py` records ordinary/optimized and fresh-copy executions plus named corruptions. The full receipt lists every test and exact coefficient identity.

The ZIP contains the untouched upload, exact recovered geometry, cleaned partial excerpt, both proofs, all catalogue coefficients, every cube ordering, independent original-link audit, the scalar audit, code and working-code records, observed execution logs, source provenance, optional pinned-source recovery code, and a SHA-256 manifest. No private reasoning log, font, inaccessible historical binary, invented CI run, remote write, or background task is included or claimed.

The remaining analytic program is explicit: turn the complete signed fourth-order coefficient and tangent data into original coefficient-norm estimates and an all-order return before asserting any improved uniform physical gap. This package does not silently skip that step.
