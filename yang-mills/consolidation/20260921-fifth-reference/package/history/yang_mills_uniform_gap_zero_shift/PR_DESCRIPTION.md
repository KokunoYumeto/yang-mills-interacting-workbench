# Proposed PR: full physical strong-coupling gap, unique spatial limit, and zero-shift response

This is a proposed description accompanying a tested local patch, **not a
record of an opened PR**. The combined patch is based on PR6 commit
`e98b2c3af77f66fb1c1396143ca53daef586404f`. It preserves all inherited source
and receipt bytes, imports the previously delivered actual-loop-moment
continuation, and adds the new proof/verification/volume-limit continuation.
Only the active `CURRENT.md` pointer is updated among the old tracked files.
No remote branch, main, other-session branch or PR was modified or merged.

## Completed original-operator result

For every original open SU(2) box L>=2, spacing a>0 and coupling g²>=15,
with kappa=2g²/a and xi=1/(4g⁴), the **full physical gap** satisfies

    Delta_L >= kappa d_xi,
    d_xi=(3/4)(1-(65536/9375)r_xi) exp(-32pi xi),
    r_xi=(3/16)(1-sqrt(1-(2500/3)xi)).

The proof gives the convenient lower bounds kappa/100 on g²>=15 and
3kappa/20 on g>=4. It does not infer a full lower bound from a trial vector.
The original loop coefficient has exactly computed Fourier trace norm8;
all16 original term indices, the exact support series, the scalar vacuum
coordinate and the full energy/conditional-variance comparisons remain.

At g²=5000, every a>0 and exterior box, actual zero-shift loop response and
restored norm are enclosed about (8/39)kappa xi² and (196/4563)xi² with
respective radii 0.0000094kappa xi² and0.00000319xi². The physical gap is
at least0.74999514999kappa and less than(3+5/10^13)kappa. The exact quotient
residual and its canonical section-correction primitive remain separately
nonnegative and bounded by the computed original response residual.

## Spatial infinity and the physical norm

At fixed a>0,g²>=15 the support coefficients are exactly cutoff-compatible.
The written proof constructs the unique limiting vacuum measure, convergence
of the original ground-relative dynamics and every local time-ordered
correlation, the explicit unitary onto the full centered physical correlation
space, and the same positive energy edge. The original extensive vacuum
energy has a controlled energy-per-plaquette limit with its scalar retained.
The primitive factorization p_X=p_B T preserves the original derivative and
conditional residual sources, norms and inverse maps.

The earlier simultaneous continuum path lies in the new domain exactly while
c_n=g0^-2+beta n log2<=1/15. No theorem extends the new bound past that range.
No nontrivial smooth four-dimensional field or positive finite continuum mass
is claimed. This is a strong-coupling and full spatial-volume result with
actual physical units, offered for independent analytical review.

## Complete proof and execution

All four mathematical sources are included in full: RESEARCH_NOTE.md (U),
OPTIMIZED_DOMAIN.md (O), HEAT_BATH_GAP.md (H), VOLUME_LIMIT.md (V).
The final result is H1–H23 with its exact U/O/V dependencies.

The final standard-library checker passed273 uniquely named exact tests and
35 false-formula controls. The complete replay records seven successful
positive executions: current and parent in both modes, copied-source current
in both modes, and restoration after deliberate corruption. All18 additional
CLI corruption cases failed with exit1 at their intended exact named error.
The unchanged actual-loop predecessor passed134 tests and12 false controls.
Fresh patch application and selected source identities are recorded separately
in the delivery manifest. Analytical arguments are written proofs; these
finite tests are not a Lean certificate or an independent analytical audit.
No sampled vacuum or spin truncation is used for the numerical enclosures.

Run from the complete repository/package root:

```sh
python -B yang-mills/continuations/20260915-uniform-gap-zero-shift/replay.py
```

The source intake records the actual current default heads and separately
labels newer peer PR descriptions as discovery-only. No unread arithmetic
result or different source metric is imported into the present estimate.
No paid model run, remote CI run, automatic research process or merge occurred.
