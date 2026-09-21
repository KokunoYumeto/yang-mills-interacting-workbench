**I audited the pasted material, repaired the recoverable text and code, and completed the fourth-order source and sixth-order ground-energy calculations.** The ZIP contains **131 text-based artifacts**, including the untouched upload, proofs, every calculated coefficient, executable checkers, recovery notes, and execution records.

## Download

[**Complete audit and calculation package**](sandbox:/mnt/data/yang_mills_audit_and_completion.zip)

Individual reading copies: [Audit report](sandbox:/mnt/data/yang_mills_audit_report.md) · [Fourth-order source proof](sandbox:/mnt/data/yang_mills_fourth_order_source.md) · [Sixth-order energy proof](sandbox:/mnt/data/yang_mills_sixth_order_energy.md)

## What needed correction or completion

The uploaded material contains an interrupted fourth-order session. It includes the status caption “Computed sixth-order linked-cluster coefficients,” but no sixth-order formula, derivation, or verification record. I treated that as a missing calculation and derived the result explicitly.

The pasted Python also lost indentation and comparison symbols. I recovered the original `geometry.py` from the pinned GitHub revision and verified its exact Git blob, rather than guessing how strings such as `if ji` or `if atroot` were intended to execute. The original upload remains unchanged alongside the restored file.

Two mathematical distinctions are important.

First, the uploaded residual

```math
R_2=\xi^3v_3+\xi^4B(v_2,v_2)
```

is correctly written for `q_2=\xi v_1+\xi^2v_2`. The **complete fourth vacuum coefficient**, however, is

```math
\boxed{v_4=2B(v_1,v_3)+B(v_2,v_2).}
```

The additional incoming term must remain. The new catalogue calculates the signed sum of both terms.

Second, the sixth-order spatial calculation requires the **six distinct faces of an elementary cube**. Their original Haar contribution survives. A calculation restricted to supports of at most three plaquettes would omit that contribution. Its exact linked weight is

```math
\boxed{-\frac{83}{1944}\quad\text{per elementary cube}.}
```

I verified this value by two different calculations: the sum over all **720 insertion orders**, and a separate pairing of three-face states with their complementary three-face states.

## 1. Completed fourth-order source

The calculation preserves the original Hamiltonian and physical parameters:

```math
H=\kappa\bigl[K+\xi(2M-S)\bigr], \qquad K=-\sum_{e,\alpha}X_{e,\alpha}^{\,2}, \qquad S=\sum_pW_p,
```

```math
\boxed{\kappa=\frac{2g^2}{a},\qquad \xi=\frac1{4g^4}.}
```

The fourth-order catalogue contains all **8,621 anchored connected face multisets**, organized into **78 original lattice-symmetry classes**:

| Face-multiplicity patternClasses |        |
| -------------------------------- | ------ |
| `4`                              | 1      |
| `3+1`                            | 2      |
| `2+2`                            | 2      |
| `2+1+1`                          | 19     |
| `1+1+1+1`                        | 54     |
| **Total**                        | **78** |

Every class has a fully expanded rational polynomial, not an unevaluated `K^{-1}` or `B` expression. The files retain the original faces, spanning tree, chord variables, kinetic fields, source multiplicities, Haar means, and coefficient norms.

Across the catalogue there are **4,044 nonzero rational monomials**. The producer checks **1,053 inverse equations and 1,053 logarithmic-source equations** as identities of complete polynomials in the original SU(2) sphere quotient.

A readable component is the contribution of one plaquette repeated four times:

```math
\boxed{ v_4^{(p,p,p,p)} = \frac{17}{10368}\chi_1(\Omega_p) -\frac7{51840}\chi_2(\Omega_p). }
```

Here `\chi_1,\chi_2` are the original spin-one and spin-two characters.

For comparison, the previously available own-face part of `B(v_2,v_2)` is

```math
\frac1{10368}\chi_1-\frac1{31104}\chi_2.
```

The remaining incoming contribution is exactly

```math
2B(v_1,v_3)^{(p,p,p,p)} = \frac1{648}\chi_1-\frac1{9720}\chi_2.
```

Their sum gives the displayed complete coefficient.

### An original-coordinate issue that the extension must retain

One four-face class—the four lateral faces of a cube—has **five independent graph cycles**. Its correct chord count is

```math
|E|-|V|+1=5.
```

The calculation retains all five. Assuming one chord per face would change the source on this cluster.

The archive includes all **8,621 explicit signed-coordinate transports** from the anchored original multisets to their representatives, with the inverse-link orientation rule. Thus the coefficient files can be returned to the original finite box without an extra factorial or an implicit geometry convention.

### The signed tangent calculation is also completed

A second program constructs the logarithmic source directly, independently of the eigenvector-to-logarithm recurrence used by the main producer. It then calculates the original plaquette-direction responses

```math
Z_{p,\rho}=(\rho_p+1)v_{\rho+e_p}.
```

It verifies every retained coefficient of

```math
KZ_{p,\rho} - 2Q_H\sum_{0<\mu\le\rho} \Gamma(v_\mu,Z_{p,\rho-\mu})
```

through degree three: the result is zero at positive degree and the original `W_p` at degree zero.

The complete record contains **282 explicitly expanded degree-three response polynomials and 2,156 exact zero-polynomial tangent identities**.

[Read the signed-tangent certificate](sandbox:/mnt/data/yang_mills_signed_tangent_note.md)

## 2. Completed sixth-order ground energy

Write

```math
\frac{E_0}{\kappa} = 2M\xi+e_2\xi^2+e_4\xi^4+e_6\xi^6+R_8(\xi).
```

The original lower coefficients remain

```math
e_2=-\frac M3, \qquad e_4=\frac{5M}{216}-\frac{2J}{1053},
```

where `J` counts original unordered adjacent plaquette pairs.

The complete sixth-order linked weights are:

| Original connected supportSixth-order weight |                   |
| -------------------------------------------- | ----------------- |
| One plaquette                                | `-289/77760`      |
| Adjacent pair                                | `22285/23654592`  |
| Three-face path                              | `-4909/118272960` |
| Three faces sharing one edge                 | `244/4312035`     |
| Three faces at a cube corner                 | `-212/542997`     |
| Six distinct faces of a cube                 | `-83/1944`        |

### Why the cube term survives

Orient the six original cube faces outward. Each of its twelve links then occurs once in each direction. Original Haar integration contributes `1/2` per edge; the remaining contractions have eight independent two-dimensional color loops. Therefore

```math
\left\langle\prod_{p\in\partial c}W_p\right\rangle_H = \frac{2^8}{2^{12}} = \frac1{16}.
```

For an insertion order `\pi`, let `A_k(\pi)` be its first `k` faces. The surviving intermediate energy is the original boundary Casimir

```math
\frac34|\partial A_k(\pi)|.
```

The complete contribution is

```math
-\frac1{16} \sum_{\pi\in S_6} \prod_{k=1}^{5}\frac4{3|\partial A_k(\pi)|} = -\frac1{16}\frac{166}{243} = -\frac{83}{1944}.
```

All 720 orders and their intermediate boundary counts are stored in the ZIP.

The proof also establishes completeness of the support classification: original link-center symmetry permits either even face multiplicities, which at order six use at most three distinct faces, or a six-face closed cubical surface. The latter is an elementary cube.

### The complete open-box answer

For the original box with vertices `\{-L,\ldots,L\}^3`, put `m=2L`. The result is

```math
\boxed{ e_6= -\frac{ 211396463m^3+ 30959193m^2+ 21845782m+ 2336684 }{4691494080}. }
```

In particular, for the original `L=2` box,

```math
\boxed{ \frac{E_0}{\kappa} = 480\xi-80\xi^2 +\frac{1198}{351}\xi^4 -\frac{3528610133}{1172873520}\xi^6 +R_8(\xi). }
```

This retains the original open boundaries, all 240 plaquettes, all adjacent-pair and triple counts, and all 64 elementary cubes.

### An explicit remainder

I proved a separate finite-volume analytic bound using the original free physical gap and the bounded multiplication operator `S`. It does **not** rely on the inherited uniform-coupling claims.

Set

```math
R=\frac3{8M}.
```

Then

```math
\boxed{ |R_8(\xi)| \le \frac34 \frac{(|\xi|/R)^8}{1-(|\xi|/R)^2}, \qquad |\xi|<R. }
```

For `L=2`, this is

```math
\boxed{ |R_8(\xi)| \le \frac34 \frac{(640|\xi|)^8}{1-(640|\xi|)^2}, \qquad |\xi|<\frac1{640}. }
```

The remainder here belongs to `E_0/\kappa`; multiplying by `\kappa` returns the physical energy error. Its volume dependence is explicit.

## 3. What the checks establish

The final main verifier passed **630 named checks and nine false-formula controls**. Ordinary Python, optimized Python, and fresh copied-source executions reproduced the same complete record. Sixteen additional command-line corruption runs failed at their intended errors.

The independent tangent calculation also passed in ordinary and optimized Python from fresh copies.

The checks cover complete symbolic coefficient identities, original-link kinetic and gauge-return regressions, the full cube calculation, independent small-cluster energy calculations, the original finite-box counts, and the inherited scalar arithmetic.

The one-plaquette coefficient has an external check. The original coordinate transformation gives

```math
e_{\mathrm{one}}(\xi)=\frac14b_2(-4\xi)-1.
```

NIST’s Mathieu expansion consequently yields

```math
e_{\mathrm{one}}(\xi) = -\frac{\xi^2}{3} +\frac{5\xi^4}{216} -\frac{289\xi^6}{77760} +\frac{21391\xi^8}{27993600} +\cdots,
```

matching the independent character recurrence through eighth order. This verifies that convention and coefficient; it is not external certification of the entire spatial calculation. ([DLMF](https://dlmf.nist.gov/28.6.E5 "https://dlmf.nist.gov/28.6.E5"))

The exponential-vacuum and linked-source framework has established antecedents, which the proof credits. I make no global novelty or best-known-bound claim. ([arXiv](https://arxiv.org/html/hep-lat/9603026v1 "https://arxiv.org/html/hep-lat/9603026v1"))

**The inherited discriminant and endpoint arithmetic check out when their stated coefficient bounds are supplied as inputs. The full analytical chain behind the older uniform-gap claims has not been independently recertified in this audit.** The present results concern explicit vacuum coefficients and a finite-volume remainder; no new continuum mass-gap theorem or improved coupling threshold is asserted.

## Archive contents and recovery limits

The ZIP contains the original upload, corrected geometry, cleaned partial excerpt, three proof notes, every fourth-order coefficient, every signed response, all cube paths, source and recovery records, calculation programs, verification records, execution logs, and a SHA-256 manifest. Every packaged file was decompressed and checked against that manifest.

[Main verification record](sandbox:/mnt/data/yang_mills_audit_verification.json) · [Execution record](sandbox:/mnt/data/yang_mills_audit_execution.json) · [Archive validation](sandbox:/mnt/data/yang_mills_audit_archive_validation.json)

From the extracted root:

```sh
python -B checks/verify_manifest.py
python -B checks/verify.py --verify-receipt results/verification.json
```

The old ZIP filenames printed inside the upload were not available as mounted files. I have **not fabricated or silently replaced those historical archives**. Their inventory and availability are recorded, and an optional pinned GitHub recovery script is included for the committed prior-session text. No remote repository modification was performed during this audit.