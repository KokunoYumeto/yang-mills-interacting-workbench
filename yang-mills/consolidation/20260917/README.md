# Fourth-order vacuum, sixth-order energy, and physical spectral return

This continuation studies the original SU(2) Hamiltonian on open cubic boxes. It calculates the fourth coefficient of the logarithmic vacuum, the complete sixth coefficient of the ground energy, and the response of that vacuum to individual plaquette couplings. A convergent correction to the fourth-order reference then gives a lower bound on the whole physical excitation spectrum, uniformly in the finite box size. The physical scale and the boundary terms are retained throughout.

Two separately developed calculations are included. They are complementary contributions, not two successive versions in which one replaces the other. One uses original trace words and supplies quantitative source bounds and the all-order spectral return. The other uses explicit tree and quaternion coordinates and supplies full polynomial residuals, signed tangent coefficients, and an independent finite-volume remainder.

Start with **[the reader](reader/yang_mills_quartic_cube_reader.pdf)**, **[editable TeX](reader/yang_mills_quartic_cube_reader.tex)** or **[searchable text](reader/yang_mills_quartic_cube_reader.md)**. The reader introduces the objects and includes all six supplied proof notes. The [comparison and validation](VALIDATION.md) distinguishes algebraic identities, finite checks, analytical arguments and publication history.

## The common calculation

For vertices `{-L,...,L}^3`, `L >= 2`, let `K = -sum X_(e,alpha)^2`, let `W_p` be the fundamental trace of the ordered product around a plaquette, and set

```
H = kappa [K + xi (2M - sum_p W_p)],
kappa = 2g^2/a,      xi = 1/(4g^4),      M = number of plaquettes.
```

The measure is product Haar probability; all vertex gauge transformations, including those on the boundary, are imposed. The logarithm of the positive vacuum satisfies

```
v = xi v1 + B(v,v),
v1 = (sum_p W_p)/3,
B(f,h) = K^(-1) Q_H sum_(e,alpha) (X_(e,alpha)f)(X_(e,alpha)h),
v4 = 2B(v1,v3) + B(v2,v2).
```

Here `Q_H` removes the Haar mean. Removed scalars are retained in the energy, not discarded. Both calculations cover all 8,621 anchored connected fourth-order face multisets, in 78 explicitly transported lattice classes. The 743 trace monomials and the 4,044 quaternion monomials are different coordinate expressions for the same coefficients. The comparison evaluates the trace words in the recorded tree coordinates and checks equality of every complete quotient polynomial; it is not a comparison at sample points.

Writing `m = 2L`, the sixth energy coefficient is

```
e6,L = -(211396463m^3 + 30959193m^2 + 21845782m + 2336684)/4691494080,
E0,L/kappa = 2M xi - M xi^2/3 + (5M/216 - 2J/1053)xi^4 + e6,L xi^6 + R8,
M = 3m^2(m+1),       J = 6m(3m^2-1).
```

The six distinct faces of an elementary cube contribute `-83/1944`. The twelve Haar edge contractions give `1/16`; summing all 720 insertion orders with their actual intermediate boundary Casimirs gives `166/243`, with the negative sign and Haar factor producing the stated coefficient. A separate three-plus-three calculation gives the same answer. For an unordered adjacent pair the weight is `22285/23654592`: this combines the two separate multiplicity assignments, each of weight `22285/47309184`.

## What each contribution adds

| Calculation | Complete source | Significance |
| --- | --- | --- |
| Trace-word fourth coefficient and source/spin estimates | [QUARTIC_SOURCE](../../continuations/20260917-quartic-cube/QUARTIC_SOURCE.md) | Exact finite coefficients with explicit bounds for the full source equation. |
| All-order correction and full physical gap | [PHYSICAL_RETURN](../../continuations/20260917-quartic-cube/PHYSICAL_RETURN.md), R24–R34 | Includes the entire degree-five-to-eight residual, the linear inverse and nonlinear tail, rather than treating a truncated Hamiltonian as the original operator. |
| Sixth energy and mean plaquette | [SIXTH_ENERGY](../../continuations/20260917-quartic-cube/SIXTH_ENERGY.md) | Complete open-boundary counts, an all-order remainder and the observable obtained by differentiating the energy. |
| Tree-coordinate fourth coefficient | [FOURTH_ORDER_SOURCE](../../continuations/20260917-quartic-independent/proofs/FOURTH_ORDER_SOURCE.md) | Complete rational polynomials with explicit gauge-return and kinetic fields, including the four-face cluster that needs five chord coordinates. |
| Signed response to plaquette couplings | [SIGNED_TANGENT_CERTIFICATE](../../continuations/20260917-quartic-independent/proofs/SIGNED_TANGENT_CERTIFICATE.md) | 282 expanded degree-three responses and 2,156 residual identities, with the degree-zero forcing retained. |
| Independent sixth energy and remainder | [SIXTH_ORDER_ENERGY](../../continuations/20260917-quartic-independent/proofs/SIXTH_ORDER_ENERGY.md) | A separate eigenvector derivation, cube pairing calculation and a remainder proved directly from the finite-box free resolvent. |

The full-spectrum estimate is `Delta_L >= kappa d_[4](xi)` for `0 < xi <= alpha_[4]`, with the exact rational-polynomial definitions of `d_[4]` and `alpha_[4]` in R25–R30. The sufficient original coupling threshold lies strictly between `3.715960362535435236` and `3.715960362535435237`. In particular,

```
g^2 >= 15/4  implies  Delta_L > 1.6584 kappa = 3.3168 g^2/a;
g^2 = 4      implies  Delta_L > 1.89811 kappa.
```

The two energy remainders have different proofs and domains. The source-based estimate holds for `|xi| < 1/60`, with its explicit extensive factor. The independent finite-volume estimate holds for `|xi| < R = 3/(8M)` and bounds the remainder in `E0/kappa` by `(3/4)(|xi|/R)^8/[1-(|xi|/R)^2]`. Its radius depends on volume. Keeping both makes clear which inputs each estimate needs.

## Reading and reproduction

- [Trace-word contribution and original replay instructions](../../continuations/20260917-quartic-cube/).
- [Independent polynomial contribution and public replay instructions](../../continuations/20260917-quartic-independent/PUBLIC_EDITION.md).
- [Exact comparison and additional checks](verification/).
- [Previous complete continuation reader and sources, 14–16 September](../20260916/).
- [Foundation papers and earlier DOI editions](../../README.md).

The companion `yang_mills_quartic_comparison_sources_20260917.zip` contains both mathematical source packages, their unchanged historical receipts, the new comparison and replay records, and this reader. A private conversation transcript is excluded; its identity and the precise effect on replay are recorded. No mathematical input is replaced by that omission. Earlier public sources remain available without being relabelled as current results.

The exponential-vacuum and character methods have established precedents: [Schütte, Zheng Weihong and Hamer, hep-lat/9603026](https://arxiv.org/abs/hep-lat/9603026), and [Llewellyn Smith and Watson, hep-lat/9212025](https://arxiv.org/abs/hep-lat/9212025). The detailed papers retain the original operator dictionaries and further citations. No general priority or best-known-bound claim is made.

These results concern the specified lattice Hamiltonian. They do not establish a nontrivial four-dimensional continuum field or a finite positive continuum mass. The separately expanded fifth source is a next calculation, not a missing term in the completed sixth-energy formula or in the bounded full residual.

This is part of the [PolyClank workbench](../../../WORKBENCH.md): readers can fork the repository, add a clearly stated result with its proof or executable calculation, and submit a pull request. [Contribution instructions](../../../CONTRIBUTING.md) explain the process. The mathematical sources are AI-assisted research, including work with ChatGPT 5.6 Sol and GPT-6 Astra; the individual source histories retain their own attribution.
