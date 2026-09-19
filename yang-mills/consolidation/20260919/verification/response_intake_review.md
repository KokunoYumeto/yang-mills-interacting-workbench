# Response and remainder: bounded independent intake review

Review date: 19 September 2026. Scope: the complete supplied `RESPONSE_AND_REMAINDER.md`, `native_response.json`, and `gram_cauchy.json`. The source documents were read without modification. No broad corpus search, Lean run, coefficient enumeration, publication, or remote operation was performed. Written artifacts are this report, the small reproducible checker `response_checks/check_response_certificates.py`, and its deterministic `response_checks/receipt.json`.

## Assessment

The displayed finite-volume analytic estimates, normalization identities, and support-transition construction are internally consistent under the original Hamiltonian and graph hypotheses inherited from `SIXTH_SOURCE.md`. Independent exact-rational calculation passed 42 checks, including the native-response total error, every stored row maximum and maximizing index, all three displayed two-spacing sign brackets, and the constants used in A67–A78.

This is a successful check of the supplied certificate arithmetic and the stated mathematical implications. It is **not** an independent derivation of the response matrices or their coefficients: the three reviewed inputs do not contain the complete matrices, face arrays, embedding enumeration, or coefficient producers. In particular, the `passed: true` fields are source assertions; they were not used as the basis of this assessment.

A73–A78 give concrete transitions and an exact kernel isomorphism for the 240-label observation family inside the full centered physical space. They support a finite-family application of Split Zero, provided the separate Split Zero theorem's formal hypotheses match this construction. They do not establish a whole-Hilbert-space reconstruction, a volume-uniform estimate, or a continuum Yang–Mills mass gap.

## Sources and identity

The SHA-256 digests of the exact reviewed files are:

| Source | SHA-256 |
| --- | --- |
| `RESPONSE_AND_REMAINDER.md` | `7cd5f28c82e1b6c50d1088a4a02862a83489e36ccd8e56e8abec38562e52278e` |
| `native_response.json` | `3974bafabd00e0f0a565183cfc4bcf6d9f100bddefd5fd2ed71bee67154bb85b` |
| `gram_cauchy.json` | `0ce79adc26349f0e3b5d89263c2459274c9244b13e7946f28c3f013c965bc8f6` |

The note is dated 18 September 2026. Its equation numbering runs through A78. A12 begins at source line 421; A13 begins at line 496.

## Hypotheses and principal statements

The finite graph must be the original simple cubic graph, with all stated vertex gauge constraints retained, no doubled edges, and no triangles. A1 uses these properties to show that a nonconstant invariant Fourier component has at least four active edges, each contributing at least the SU(2) Casimir `3/4`. The resulting free physical gap is `K >= 3` on the complement of the unique constant vacuum. These graph, operator, measure, and domain definitions are inherited from `SIXTH_SOURCE.md`; they were not reconstructed from the three assigned files.

For bounded smooth plaquette multiplication, `||W_p|| <= 2`; for the original complex source, `||V_x|| <= 2||x||_1`. A1–A5 then yield a simple analytic eigenbranch on `||x||_1 < 3/4`, an explicit bound on the smaller ball, and its identification with the physical ground state for real sources. The regularity argument supplies the differentiable/logarithmic vacuum section needed by A10–A12. The original center transformation gives the even energy and response series. Its applicability depends on the original graph and boundary realization; it should not be silently transferred to a different periodic graph.

A34–A41 retain the exact Haar orthonormality of the distinct plaquette trace vectors and improve the Schur bound. The row and column norms in A36 are both `||x||_2`, including for complex sources: the adjoint of the row introduces the conjugated coefficients. A39 is an upper bound on `|e|(3-2rho-|e|)`; the continuity argument is needed to select the smaller root. The note includes that argument.

A51–A54 enlarge the analytic domain to `||x||_1 + ||x||_2 < 3/2`. A fixed-bound formulation requires both `d0 = 3-2rho0 > 0` and `4eta0 < d0^2`; the second inequality by itself would not imply the first. Both requirements hold for every numerical choice made in the note. The rank-one contour and the variational bound on the first excitation correctly keep the full physical complement in the operator. For real sources, the constant trial state gives ground energy at most zero before restoring the scalar, while the min-max principle gives the first excited energy at least `d0`, hence a physical gap at least `kappa*d0`.

A55 and A56 correctly distinguish the two source Grams for distinct versus repeated face directions. For `M >= 240`, the selected radii give the two respective circle constants `49/34` and `98/39`. Their separate use in the complete row-tail estimate A65 is essential.

The numerical family used for A67–A78 is specifically:

- The original `L=2` box, `M=240`, and its fixed original face ordering.
- Real homogeneous source `xi = 1/(4(g^2)^2)` with `g^2 >= 14`, so `0 < xi <= 1/784`; the limiting algebraic value `xi=0` is harmless.
- `a > 0` and the physical factor `kappa = 2g^2/a > 0`.
- The original centered vacuum Hilbert space and self-adjoint operator `Atilde`, including the full spin spectrum.
- Correct complete coefficient matrices through degree six, with the claimed exact row bounds, together with the analytic remainder estimate.

Under these hypotheses, A66 implies the strict positive-definite matrix inequalities `(2/9)I < R < (4/9)I` in the original counting pairing on `C^240`. These are inequalities on a specified observation family; they are not a replacement of its physical state Gram by the identity.

## Independent rational checks

The arithmetic was first recomputed by an ephemeral JavaScript script using normalized `BigInt` numerator/denominator pairs. It was then independently rerun with the delivered Python standard-library checker using `fractions.Fraction`. Every comparison is exact; decimals below are descriptive only. Each implementation parses the two JSON files, recomputes maxima from all 720 stored row sums, and recomputes the displayed bounds from their defining formulas. The delivered checker additionally pins all three source SHA-256 digests and emits a deterministic receipt with every comparison and rational margin.

Replay with the directory containing the three unchanged supplied sources:

```text
python response_checks/check_response_certificates.py --source-dir PATH_TO_SOURCES
```

The default output is `response_checks/receipt.json`; an explicit `--output PATH` is also supported. No third-party package is needed. The receipt distinguishes 42 arithmetic checks from three source-identity checks. Its limitations explicitly exclude matrix reconstruction and any continuum conclusion.

All 42 assertions passed. They cover:

| Check group | Result |
| --- | --- |
| 240 row sums for each of degrees 2, 4, and 6 | Counts correct |
| Maximum of each stored row-sum array | Exactly the A64 constants |
| Entire lists of maximizing zero-based indices | Exact match; 36, 12, and 24 indices respectively |
| A65 tail at `xi0=1/784` | Exact match to JSON |
| A66 finite coefficient contribution and complete error | Exact match to JSON; strictly below `1/9` |
| `g^2=14` and `g^2=1000000` source conversion | Exact match to `xi=1/784` and `xi=1/(4*10^12)` |
| A57 distinct/same source budgets and A52 contour conditions | Exact identities and strict inequalities hold |
| A58 rational smaller-root comparisons and response constants | Correct |
| A61 error and both unrounded endpoints | Exact match to JSON; reported rational bounds are strict |
| A24 and A49 reported brackets | Both strict after recomputing the displayed error formulas |
| A42, A43, A45, A50, A62, A63 scalar/derivative constants | Correct |
| A69, A70, A71 physical-gap and state-norm constants | Correct |

In particular,

```text
B_tail(1/784) = 3667578125/34842697344

computed coefficient shift =
7977652209607479875536810322723248074061
/30328253632373217070021048818714978539274240000

complete response error =
3192391118755322326406743242436946723248074061
/30328253632373217070021048818714978539274240000
= approximately 0.10526129059233649

1/9 - complete response error =
177414840397257348040039959642495336671285939
/30328253632373217070021048818714978539274240000
= approximately 0.005849820518774607 > 0.
```

The A61 unrounded divided-response interval is approximately
`(0.000004780144392300831, 0.000011586136274089066)` and lies strictly inside the reported rational interval. This conclusion depends on the asserted degree-six coefficient `41237423/5039315143200`; that coefficient itself has not been regenerated here.

## Physical normalization and state norms

Write `B c = sum_p c_p(W_p-<W_p>_rho)`, and `Z = kappa*Atilde^(-1)*B`. The central identities are

```text
Atilde Z = kappa B,
R = B*Z = kappa B*Atilde^(-1)B,
Z*Atilde Z = kappa R,
G_Z = Z*Z.
```

The adjoints use the actual `rho` pairing. In physical Haar space, `r=U_psi B`, so the original time-integrated connected correlation is `R/kappa`. A67 concerns the coefficient-space quadratic form of `R`; A68 is the actual primitive energy form, with its required factor of `kappa`.

At the endpoint,

```text
3 - 2*240/784 = 117/49,
(4/9)/(117/49) = 196/1053,
(2/9)^2/(4*240) = 1/19440.
```

Thus the state upper bound follows from the actual physical gap and the energy upper bound. The lower bound follows from Cauchy–Schwarz, `||Bc||^2 <= 4M||c||^2`, and `c*Rc > (2/9)||c||^2`. No identification of `B*B`, `Z*Z`, and the source-coordinate identity is made. The dependence on `M=240` in the lower state bound is retained.

Strict scalar inequalities hold for nonzero coefficient vectors. At `c=0` their correct scalar specialization is equality `0=0`. Matrix inequalities such as A67 and A72 mean that their differences are positive definite, which already has the correct nonzero-vector interpretation. A68 and A70 should explicitly add `for c != 0` when quoted as scalar inequalities.

## Concrete support transitions and Split Zero intake

For each subset `F` of the fixed face set, A73 uses the actual two-term complex

```text
C_F^0 = V_F = Z(C^F),
C_F^1 = U_all = B(C^240),
d_F = (Atilde/kappa)|V_F,
C_F^2 = 0.
```

Here `B` and `Z` are injective, so `d_F` identifies `V_F` with `U_F=B(C^F)`. For `F subset G`, degree zero is inclusion, degree one is the identity on `U_all`, and the cochain square commutes by restriction of the same operator. Consequently `H^0(C_F)=0`, `H^1(C_F)=U_all/U_F`, and the degree-one cohomology transition is the quotient projection. Its full kernel is `U_G/U_F`.

The A74 map is therefore an exact isomorphism

```text
V_G/V_F -> U_G/U_F = ker(H^1(C_F) -> H^1(C_G)),
[Zy] -> [By],
[By] -> [Zy].
```

Changing representatives by `B(C^F)` changes the primitive by precisely `Z(C^F)`. Injectivity verifies both inverse laws. The receiving-kernel dimension is `|G\F|`. Because the two source maps are injective, unions and intersections of coordinate supports give the corresponding sums and intersections of the `V` and `U` subspaces. These are explicit finite-family transition data suitable for comparison with a separately stated Split Zero theorem.

For `J=G\F`, A75 minimizes the actual energy over representatives `Z_F z+Z_J y`. The minimum is attained uniquely because `R_FF` is strictly positive definite. The correct Hermitian Schur complement is

```text
z_min = -R_FF^(-1) R_FJ y,
Q_(F,G) = kappa*(R_JJ - R_JF R_FF^(-1) R_FJ).
```

Every mixed block is retained. Evaluating the strict lower bound at the attained minimizer gives `Q_(F,G) > (2kappa/9)I_J`; evaluating the energy at the lift `z=0` gives the strict upper bound `(4kappa/9)I_J`. The same minimizing primitive has the A77 norm bounds by A71 and the full physical gap. This argument controls every subset transition without enumerating the `2^240` subsets.

Empty `F` has the stated unique empty-block convention. Empty `J` gives the zero receiving kernel and its unique zero form; there is no positive direction to assert. At `y=0`, the scalar norm and energy equal zero. A76 is only presented on nonempty receiving kernels, and A77 already specifies nonzero `y`.

A78 correctly distinguishes state orthogonality from energy orthogonality. Since `G_Z` is positive definite, `P_Z=Z G_Z^(-1)Z*` is the state-orthogonal projection and `S_Z=G_Z^(-1)Z*` is its coefficient inverse. For a centered form-domain `h` orthogonal to `im Z`, the energy retains `2kappa Re<Bc,h>_rho`. There is no assertion that `im Z` reduces `Atilde`. The finite source family therefore does not erase or solve its physical orthogonal complement.

A second independent algebraic check of A73–A78 reached the same result. The separately referenced Split Zero theorem was not among these three sources, so this review verifies the concrete maps and their properties rather than certifying an unspecified broader reconstruction theorem.

## Evidence still required for coefficient reconstruction

The initial check covered exact named paths alongside the downloads; no broad search was made. `SIXTH_SOURCE.md` and `EIGHTH_ENERGY.md` exist there and have a separate intake review. During final integration, a narrowly scoped check of the extracted predecessor archive also located the inherited lower response. Availability and remaining checks are distinguished below:

| Dependency | What remains to be checked with it |
| --- | --- |
| Complete `response6_L2.json` (including `generated/response6_L2.json`) | The 240 face labels/order, 20,796 nonzero entries, Hermiticity, A18 embedding return, actual degree-six row sums, A19 scalar sum, and individual A21 entry |
| Complete inherited degree-zero-through-four matrix and its face array | Present in the supplied ZIP at `workbench/yang-mills/continuations/20260917-fifth-source/generated/response_L2.json`; its hash exactly matches the native certificate's `response_through_four_sha256`. This response review did not independently reconstruct its rows, and comparison with the missing degree-six face array remains unavailable. |
| `20260917-fifth-source/PLAQUETTE_RESPONSE.md` and finite-box tables | Present in the supplied predecessor ZIP; addressed in the separate predecessor/eighth intake, not independently rederived in this three-file response check. |
| `energy8_response.json` and coefficient/embedding producer data | Four specific two-spacing contributions and their claimed completeness; independently obtaining A21 from the eighth energy |
| `generated/response6_bulk.json` | The original bulk rows, displacement involution, full Fourier symbol, and A26–A29 orientation values |
| `generated/schur_remainder.json` | File identity and the saved A49 unrounded endpoints; the reported A49 interval itself was checked directly from its formula |

The downloaded `native_response.json` records the required source-file digests as

```text
response six:
250b7e1bea75e0c4a7ac497bf6b1caafc719fa820faa2bb81a78c47428da840e

response through four:
5f7311dc369b4419de57f1ce1e94f87905f087bbbb8d67276caa625117b9e856
```

The inherited matrix's independently measured hash matches the second value exactly. The new degree-six matrix remains unavailable. Hashes identify inputs but cannot substitute for deriving matrix entries. In particular, the source JSON's row-sum arrays permit checking their maxima and downstream arithmetic, but do not themselves verify that they are the row sums of the claimed matrices. A67–A78 should therefore be integrated with an explicit distinction between the reviewed finite-family implication and the still-unreconstructed new coefficient input.

## Small editorial corrections for any derived exposition

1. At source line 464, `Equations A2--A3 return its full energy pairing` should point to A11–A12 (with A67 supplying the bound). A2–A3 are perturbation and analytic energy bounds, not the primitive-energy identity.
2. Add `for c != 0` to the scalar strict inequalities A68 and A70, or state their equivalent positive-definite form interpretation. Preserve the original file and make this clarification in the integration note if source preservation is required.
3. Keep the explicit restriction of the Split Zero application to this finite support family. Any formal invocation of a separate reconstruction theorem should cite that theorem and check its hypotheses against the concrete complexes above.

No numerical or algebraic obstruction was found in the supplied bounds. The material limitation is missing matrix/coefficient reconstruction evidence, not failure of the displayed rational margins or support-transition algebra.
