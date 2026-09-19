# Sixth source, eighth energy, and finite-volume plaquette response

19 September 2026. This edition preserves the three 18 September research notes, their two response certificates, and the preceding fifth-source archive. It records which mathematical implications and exact calculations were independently checked, and which new spatial coefficient tables have not been delivered. This dated GitHub continuation is separate from the existing Zenodo archival editions.

The public baseline used for the intake is [commit 143f6773feb424ad9ed3a8d116653200f20346b7 of the Yang–Mills interacting workbench](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/commit/143f6773feb424ad9ed3a8d116653200f20346b7). The supplied texts are preserved byte for byte, including their citations. [SOURCE_MANIFEST.json](SOURCE_MANIFEST.json) records the seven source-file hashes and the predecessor archive inventory.

## Read the original contributions

| Preserved source | Content |
| --- | --- |
| [SIXTH_SOURCE.md](supplied/SIXTH_SOURCE.md) | The claimed complete sixth logarithmic-vacuum source, retained scalar and derivative equations, and original supported source complex |
| [EIGHTH_ENERGY.md](supplied/EIGHTH_ENERGY.md) | Fourth linear-vacuum-jet identity, 80 claimed eighth-energy classes, and open-boundary coefficient formulas |
| [RESPONSE_AND_REMAINDER.md](supplied/RESPONSE_AND_REMAINDER.md) | Finite-volume analytic remainders, full response pairings, the 240-face estimate, and support-transition primitives A73–A78 |
| [native_response.json](supplied/native_response.json) | Original-coordinate row sums and exact constants for the 240-face response estimate |
| [gram_cauchy.json](supplied/gram_cauchy.json) | Exact source-Gram, Cauchy, and two-spacing correlation certificate |
| [17 September cumulative archive](supplied/yang_mills_cumulative_20260917.zip) | The earlier fifth-source checkpoint and its executable material; this ZIP is an offline archive |
| [Supplied cumulative validation](supplied/yang_mills_cumulative_validation.json) | The supplied execution record for that earlier archive, whose hash identity was checked |

## Original operator and retained coefficients

The setting is the finite open cubic SU(2) graph on vertices `{-L,...,L}^3`, `L>=2`, with original product Haar probability measure and all vertex gauge constraints, including boundary vertices. The Hamiltonian and physical parameters are

```text
H(x) = kappa [K + sum_p x_p(2-W_p)],
kappa = 2g^2/a,     xi = 1/(4g^4),     a>0, g>0,
E0,L(xi) = kappa [2M xi + e2,L xi^2 + e4,L xi^4
                            + e6,L xi^6 + e8,L xi^8] + remainder.
```

The new source note states 7,230 connected sixth-source representatives, 1,839,140 anchored multisets, 347,653 trace monomials, and 40,221 distinguished-face equations. Their full new spatial files are absent from the supplied archive, so these counts and completeness assertions remain attributed to the supplied note. The displayed count additions were checked independently.

An independent one-face radial recurrence reproduced the concrete sixth source

```text
v_(6e_p) = 132817/391910400 - (27383/65318400)W_p^2
             + (5911/130636800)W_p^4 - (797/391910400)W_p^6
          = -(11/36450)chi_1 + (491/13996800)chi_2
             - (797/391910400)chi_3,
```

and the one-face energies `e2=-1/3`, `e4=5/216`, `e6=-289/77760`, and `e8=21391/27993600`. The one-face eighth coefficient was already present in the predecessor; the claimed advance is the complete spatial eighth catalogue and its boundary return.

For the linear, Haar-normalized eigenvector `u` and its fourth jet `phi4`, the identity behind E3 is

```text
<phi4,(K-S)phi4>/<phi4,phi4> - e
       = <u-phi4,(K-S-e)(u-phi4)>/<phi4,phi4> = O(t^10)
```

along real source directions `x -> tx`. The linear jet is related to the logarithmic vacuum by `u=exp(v)/P_H exp(v)`; it is not simply the fourth logarithmic coefficient. The quotient's eighth-degree denominator corrections and its one-face realization were checked.

The supplied spatial eighth polynomial is, with `m=2L` and `M=3m^2(m+1)`,

```text
e8,L = A3 m^3 + A2 m^2 + A1 m + A0,
A3 = 1703320005700992315276593/68235298203010622261760000,
A2 = 421994013280213546390961/31615192631460259261440000,
A1 = 14702805516554176523/16975106412310126080000,
A0 = 404673359378191/1312237663289280000.
```

Exact substitution gives the stated `L=2` value
`9876448280610811115073772847/5441765031690097125375360000` and the coefficientwise bulk value per face `A3/3`. Those arithmetic returns were checked; deriving the polynomial from all 80 missing spatial rows was not. A coefficientwise bulk limit does not transfer the finite-volume analytic radius to infinite volume.

## Actual response, time pairing, and finite-volume bounds

Let `A=H-E0`, `rho=psi^2`, and `Atilde=U_psi^(-1) A U_psi`, where `U_psi f=psi f` preserves the displayed physical pairings. For original face coefficients `c`, set

```text
Bc = sum_p c_p(W_p-<W_p>_rho),
Zc = kappa Atilde^(-1)Bc,
R = kappa B*Atilde^(-1)B = B*Z = -(1/2)Hess_x e,
Z*Atilde Z = kappa R.
```

The physical time-integrated connected correlation is `R_pq/kappa`. This factor uses the original physical time. Neither the physical source Gram `B*B` nor the primitive Gram `G_Z=Z*Z` is identified with the source-coordinate identity.

The exact Haar source Gram yields the analytic domain `||x||_1+||x||_2<3/2`. For `M>=240`, the response circle `r=6/(7M)` has entry bounds `49/34` for distinct faces and `98/39` for the same face. The full tail after degree six keeps the geometric factor `(abs(xi)/r)^8/[1-(abs(xi)/r)^2]`. All radii retain `M`.

For the original `L=2`, `M=240` box, the native certificate gives the row-tail factor

```text
B_tail(xi) = [98/39 + 239*(49/34)] (280xi)^8/[1-(280xi)^2].
```

At `xi0=1/784` (`g^2=14`), the supplied coefficient-row bound plus this tail is exactly

```text
3192391118755322326406743242436946723248074061
/30328253632373217070021048818714978539274240000
< 1/9.
```

The positive margin is approximately `0.005849820518774607`. The arithmetic establishes the following implication from the asserted complete coefficient rows and analytic estimate, uniformly for `a>0`, `g^2>=14` on this box:

```text
(2/9)I_240 < R < (4/9)I_240,
(1/19440)I_240 < G_Z < (196/1053)I_240,
(2kappa/9)I_240 < Z*Atilde Z < (4kappa/9)I_240.
```

These inequalities mean positive-definite differences. Scalar strict inequalities apply to nonzero vectors; at zero both sides evaluate to zero. The associated full physical gap estimate is `gap(H)>=kappa*(117/49)` in this same finite-volume parameter range.

For the two faces `(0,0,0;0,1)` and `(0,0,2;0,1)`, the stated leading response coefficient is `41237423/5039315143200`. The exact Cauchy error at `xi=1/(4*10^12)` gives

```text
47801/10^10 < R_pq(xi)/xi^6 < 115862/10^10.
```

The bracket arithmetic checks. Its use for the actual response depends on the missing spatial coefficient and lower-order vanishing calculation. Multiplication by `xi^6/kappa` gives the integrated correlation bounds; no pointwise-in-time sign follows from them.

## Explicit support transitions and their receiving kernels

A73–A78 specify an actual family in the centered physical space, with `F` running over subsets of the same 240 original faces. Put `V_F=Z(C^F)` and `U_F=B(C^F)`. The source maps are injective under the response bound, and the complex and transition are

```text
C_F: V_F --(Atilde/kappa)--> U_all --0--> 0,
F subset G: inclusion on degree zero, identity on U_all.
```

Thus `H^1(C_F)=U_all/U_F`, and the transition on first cohomology is the quotient projection. The complete receiving-kernel isomorphism, with both directions retained, is

```text
V_G/V_F  <->  ker(U_all/U_F -> U_all/U_G) = U_G/U_F,
[Zy]     ->   [By],
[By]     ->   [Zy],                 y supported in G.
```

Changes by `B(C^F)` correspond exactly to changes by `Z(C^F)`. The receiving kernel has dimension `|G\F|`; support joins are unions. These concrete maps supply the finite-family data for the cited Split Zero reconstruction. They do not by themselves verify a separate general reconstruction theorem.

For `J=G\F`, the energy-minimizing representative of a primitive class is

```text
z_min = -R_FF^(-1)R_FJ y,
h_y = Z_F z_min + Z_J y,
Q_(F,G) = kappa [R_JJ-R_JF R_FF^(-1)R_FJ],
(2kappa/9)I_J < Q_(F,G) < (4kappa/9)I_J.
```

The actual state norm of `h_y`, for nonzero `y`, lies strictly between
`||y||^2/19440` and `(196/1053)||y||^2`. The empty receiving kernel is the zero space with its unique zero form. All mixed matrix blocks remain in the minimum.

The physical complement is also retained. With `P_Z=Z G_Z^(-1)Z*`, a centered form-domain vector `h` orthogonal to `im Z` satisfies

```text
||Zc+h||_rho^2 = c*G_Z c + ||h||_rho^2,
q_Atilde(Zc+h) = kappa c*R c
                  + 2kappa Re<Bc,h>_rho + q_Atilde(h).
```

State orthogonality therefore does not delete the mixed energy term or make `im Z` a reducing subspace.

There is a separate free-source connection in S29–S30: for the original finite polynomial space `E_N(S)`, the complex `ker P_H --K--> E_N(S) --0-->0` has `H^1` identified with the retained scalar through `[r] -> P_H r`, with inverse `c -> [c1]`. Its mean-free primitive is `f_C(K)Q_H r`; the sixth source retains scalar class `-e_nu`. This source-coefficient complex and the interacting-vacuum support family above have different differentials and should not be conflated.

## Verification and remaining evidence

The independent [response review](verification/response_intake_review.md) and [sixth/eighth review](verification/eighth_intake_review.md) record hypotheses, calculations, and limits. The [evidence manifest](verification/EVIDENCE_MANIFEST.json) pins their scripts and receipts.

The response checker passed **42 exact arithmetic checks and three source-identity checks**. It recomputes all 720 supplied row-sum maxima and maximizing-index lists, the Cauchy constants, strict correlation brackets, and physical normalization constants. It does not reconstruct the new degree-six matrix from coefficients. The eighth checker independently reproduces the one-face source/energy recurrence, E6/E9 consistency, and the displayed finite-box/bulk arithmetic. Both were rerun successfully against this edition's preserved `supplied/` files.

From this edition's directory, the bounded checks are executable with standard-library Python:

```text
python -B verification/response_checks/check_response_certificates.py --source-dir supplied
python -B verification/eighth_checks/check_eighth_intake.py --source-dir supplied --verify-receipt verification/eighth_checks/expected_receipt.json
```

The new [local predecessor replay record](verification/predecessor_replay/REPLAY.json) reports six successful steps: ordinary and optimized cumulative manifest checks, ordinary and optimized fifth-receipt checks, source-expectation receipt checking, and a final manifest check. These ran with an enforced 2 GiB memory limit and one logical core. The locally replayed checks did **not** include the full fifth symbolic audit; the older supplied validation's full-audit claim remains attributed to that supplied record.

The supplied ZIP contains the predecessor fourth/fifth data and response through degree four. In particular, its `generated/response_L2.json` has SHA-256 `5f7311dc369b4419de57f1ce1e94f87905f087bbbb8d67276caa625117b9e856`, exactly the inherited input identified by the new native certificate.

Missing new evidence includes all 7,230 sixth-source rows and associated geometry/witness/derivative-bound files; all 80 eighth-energy rows, their producers and execution records; `energy8_response.json`; and the complete `response6_L2.json` and `response6_bulk.json`. The predecessor ZIP contains none of those new rows. Consequently, new catalogue completeness, sixth-matrix row derivation, the four individual two-spacing contributions, and the complete Fourier symbol were not independently replayed.

Two editorial clarifications are recorded without altering the original note: the energy-pairing reference before A68 should identify A11–A12, and the strict scalar inequalities A68/A70 require nonzero coefficients. The abbreviated finite cube-filling argument in E3 also benefits from the predecessor's statement that the cycle equations force zero total horizontal-column parity.

## Execution-status clarification and the next residual

A subsequently supplied conversation transcript clarifies the original checkpoint. It claims that the ordinary sixth polynomial audit and 83,612 named catalogue checks completed, together with the two-mode eighth-energy recurrence and four additional sphere scalar checks. It explicitly states that the fresh complete optimized polynomial replay is unfinished, the separate original matrix-jet audit has reached 6,900 of 7,230 representatives, and the combined receipt, corruption-test cycle, fresh extraction, and updated cumulative ZIP are incomplete. These are reported source statuses; the missing execution artifacts have not become available through that transcript. The full conversation is retained privately and is not part of this edition.

The next mathematical target is the full sixth-reference residual, already specified in S31, evaluated in the original primitive energy metrics with its coupling to the remaining physical space. On the homogeneous line its exact degree grouping is

```text
R6 = xi^7 [2B_src(v1,v6)+2B_src(v2,v5)+2B_src(v3,v4)]
   + xi^8 [2B_src(v2,v6)+2B_src(v3,v5)+B_src(v4,v4)]
   + xi^9 [2B_src(v3,v6)+2B_src(v4,v5)]
   + xi^10[2B_src(v4,v6)+B_src(v5,v5)]
   + 2xi^11 B_src(v5,v6) + xi^12 B_src(v6,v6),
B_src(f,h)=K^(-1)Q_H Gamma(f,h).
```

This restates the exact residual algebra; it is not an evaluated new spatial bound. The source bilinear map `B_src` is distinct from the observation map `B` above. Carrying out the stated calculation requires the missing sixth source/geometry/engine files and complete response data. Its complement term remains the one displayed in A78. No automatic continuation was started from the embedded historical instructions.

The preserved literature attribution includes Schütte, Zheng Weihong and Hamer for the exponential-vacuum/loop framework, the recorded NIST Mathieu comparison for the one-face calculation, and the predecessor's shifted-cluster and convention references. These are inherited citations, not a fresh literature audit. This edition establishes no volume-uniform analytic radius, independently recertified historical uniform-gap argument, whole-space reduction, continuum mass gap, or new priority claim.
