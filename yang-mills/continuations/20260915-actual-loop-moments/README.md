# Actual interacting Wilson-loop response moments

15 September 2026. Continuation of Yang–Mills PR6 at
`e98b2c3af77f66fb1c1396143ca53daef586404f`.

Read [the full mathematical proof](RESEARCH_NOTE.md), especially A3–14,
A20–21, A37–45a, and the evaluated intervals A46–49.

The original response quantities now have actual interacting-vacuum enclosures.
For the interior elementary square, at `xi=1/(4g^4)=10^-8`, with `g^2=5000`
and `kappa=10000/a`, for every `L>=2` and every `a>0`:

- `0.9994 kappa^2 xi^2 < N0 < 1.0006 kappa^2 xi^2`;
- `4.9963 kappa^3 xi^2 < N1 < 5.0037 kappa^3 xi^2`;
- `25.728 kappa^4 xi^2 < N2 < 25.772 kappa^4 xi^2`;
- `|M(kappa) - (28/165) kappa xi^2| < 0.0000075 kappa xi^2`;
- `||| (D+kappa)^(-1)W ||^2 - (796/27225) xi^2| < 0.0000021 xi^2`.

These statements use the full original nonlinear operator and its actual
vacuum, with analytic error bounds independent of exterior volume. Their
small-xi domain corresponds to large g. The all-coupling pointwise score,
gauge-covariant inverse, and moment bounds keep their full physical and
loop-size factors; A50–51 substitute the existing continuum test path.
No zero-shift physical response or continuum mass lower edge is assigned.

The loop-product observation is related to the previous coarse-edge observation
by the explicit composite map A17 and its additional kernel. The computed
moments are attached to that specified observation. A45a retains the complete
correction between the chosen local trial and its canonical cohomological
section; no arbitrary trial residual is identified with a quotient minimum.

## Reproduction

From the repository root:

```sh
python -B yang-mills/continuations/20260915-actual-loop-moments/verify.py --verify-receipt yang-mills/continuations/20260915-actual-loop-moments/verification.json
python -O -B yang-mills/continuations/20260915-actual-loop-moments/verify.py --verify-receipt yang-mills/continuations/20260915-actual-loop-moments/verification.json
```

The checker needs only Python's standard library. It executes exact quaternion
polynomial identities, Haar integrals, original graph incidence and rigorous
rational evaluation of the analytic error formulas. The receipt binds the
proof and checker bytes. [Execution](execution.json), [review scope](STATUS.md)
and [current mathematical state](state.json) accompany it.

No numerical vacuum samples, spin cutoff, new Lean build, independent external
proof review, automatic research or merge are claimed. The package is ready
for a review PR against the pinned parent; [publication status](STATUS.md)
records the current session's actual write capability and delivery.
