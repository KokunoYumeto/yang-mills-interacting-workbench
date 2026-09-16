# Current mathematical state at the consolidation boundary

The current complete calculation is the pair [CUBIC_SOURCE.md](../../continuations/20260916-cubic-linearized/CUBIC_SOURCE.md) and [LINEARIZED_RETURN.md](../../continuations/20260916-cubic-linearized/LINEARIZED_RETURN.md), from PR8 commit `91434b6962062bd80439d4cb2cae9d2479264dde`. Its missing gauge-native dependencies are supplied in this edition from the delivered archive. All original proof and certificate bodies retain their bytes.

## Exact domains of the supplied results

The original parameters are `kappa = 2 g^2/a`, `xi = 1/(4 g^4)`, `a > 0`, with the original open boxes indexed by `L` and literal SU(2) gauge action. No change of these parameters is made in the consolidation.

| Source | Result stated and proved in that source | Domain and boundary |
| --- | --- | --- |
| Uniform-gap H1–H23 and V1–V25 | Full physical gap and unique fixed-spacing vacuum/dynamics volume limit | `g^2 >= 15`; later proofs enlarge specified domains. |
| Gauge-native R1–R16 and S24–S35 | Second-source physical return and fixed-spacing volume continuation | `g^2 >= sqrt((32+sqrt(354))/3)`, approximately `4.1156160293`. |
| Cubic C14–C25 and linearized L20–L29 | Complete five-family cubic source, full finite-lattice physical gap uniformly in `L`, fourth ground-energy coefficient and analytic tail | `g^2 >= 1/(2 sqrt(alpha))`, approximately `3.825973052393386`; `alpha` is the first positive root defined by L11. |
| PR7 Z19–Z25 and Z46–Z53 | Conditional-fibre inverse and zero-shift local response, with the exterior links retained | Its own stated local observation and parameter domains; the outer response remains unevaluated. |

The full quartic polynomial defining `alpha`, the signed coefficients, constants, hypotheses, source and target spaces, endpoint arguments and proof of each bound are retained in the linked full sources. This table is navigation, not a replacement theorem or a proof by metadata.

The cubic proof enlarges the finite-lattice gap range. It does **not** supply a new infinite-volume uniqueness proof over that enlarged range. The earlier fixed-spacing uniqueness domain is retained without editorial extrapolation. Likewise the local-fibre inverse is not a uniform estimate for the unobserved full physical sector.

## Corrections and unresolved work

The fixed-label spectral-limit discussion is read with the [escaping-state correction](../../continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md). Its explicit Walsh example and quotient kernel retain moving low-energy states that fixed observation labels can miss. The corrected spectral source supplied by PR4 is integrated; the baseline is pinned in the provenance record.

The later first-source gauge-resolved response is a historical mathematical response, with its separate attachments absent from intake. It does not overwrite the saved second-source bound. The full cubic source and its fourth-order *residual formula* do not constitute an evaluated connected fourth-order vacuum coefficient table. The source session ends with that fourth-order calculation in progress.

A nontrivial four-dimensional continuum field and a finite positive continuum mass remain unestablished in the delivered material. The record does not turn these missing conclusions into hypotheses of a purported completed theorem.

The [validation record](VALIDATION.md) identifies fresh computations and bounded reviews, including their exact exclusions. Earlier `state.json`, `STATUS.md` and execution records are historical snapshots; their statements about prior review or publication are not silently updated.
