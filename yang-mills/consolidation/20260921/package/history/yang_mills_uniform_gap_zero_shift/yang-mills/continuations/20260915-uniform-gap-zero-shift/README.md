# Full physical gap, zero-shift response, and the unique spatial-volume limit

15 September 2026. This is the active additive Yang–Mills continuation.

The final proved domain is **g² >= 15**, a>0, every original open box L>=2.
Use [HEAT_BATH_GAP.md](HEAT_BATH_GAP.md), H1–H23, for the strongest result:

    Delta_L >= kappa (3/4)(1-q_xi) exp(-32 pi xi) > 0,
    r_xi=(3/16)(1-sqrt(1-(2500/3)xi)),
    q_xi=(65536/9375)r_xi, xi=1/(4g^4), kappa=2g^2/a.

In particular Delta_L>=kappa/100 throughout g²>=15, and
Delta_L>=3kappa/20 throughout g>=4. These are lower bounds for the **full
original physical spectrum**, not lower endpoints of one trial quotient.

At xi=10^-8 (g²=5000, kappa=10000/a), the original elementary-loop response
has actual zero-shift enclosures centered at (8/39)kappa xi² and
(196/4563)xi². The respective certified radii are 0.0000094kappa xi² and
0.00000319xi². The true physical gap is at least 0.74999514999kappa and less
than (3+5/10^13)kappa, the latter by the displayed original variational state.

## Complete proof route

Read the complete [baseline source and zero-shift proof](RESEARCH_NOTE.md),
U1–U57, followed by the exact [plaquette coefficient and improved support
norm](OPTIMIZED_DOMAIN.md), O1–O26. Then read H1–H23 for the actual conditional
form comparison and final domain. The [volume proof](VOLUME_LIMIT.md), V1–V25,
is returned to that final domain through the explicit constants H23.
All four proof bodies are present in full. Earlier constants retain their
own domains; the final statement is H1–H23.

The complete support series constructs the actual positive vacuum, with its
scalar coordinate and extensive energy retained. Cutoff-compatible labelled
coefficients give a unique infinite-volume vacuum measure, convergence of the
full original ground-relative dynamics and all local time-ordered correlations,
and the same positive physical lower edge at fixed a and g²>=15.
The actual energy-per-plaquette limit also has its explicit finite remainder.

The original simultaneous running path g_n²=1/(g0^-2+beta n log2) lies in this
new domain exactly while g0^-2+beta n log2<=1/15. No continuation of the bound
past that domain is claimed. No nontrivial smooth four-dimensional continuum
field or positive finite continuum mass has been established by this work.

## Exact replay

From the complete package or repository root:

```sh
python -B yang-mills/continuations/20260915-uniform-gap-zero-shift/verify.py --verify-receipt yang-mills/continuations/20260915-uniform-gap-zero-shift/verification.json
python -O -B yang-mills/continuations/20260915-uniform-gap-zero-shift/verify.py --verify-receipt yang-mills/continuations/20260915-uniform-gap-zero-shift/verification.json
```

The checker is standard-library Python. It pins its predecessor helpers and
rejects changed inputs. The full delivery includes those exact predecessors.
The final receipt records **273 named exact checks and 35 false-formula
controls**. Written analytical proofs, finite tests, and external/formal
reviews retain separate scopes. No Lean build or independent proof audit is
claimed. See [STATUS.md](STATUS.md), [execution.json](execution.json), and
[source_intake.json](source_intake.json).

The mathematical checkpoint is [state.json](state.json). The next source is
the actual coupling-derivative vacuum equation beyond the present xi interval,
with the original scalar energy and all local derivative contributions kept.
No automatic research process, paid model job, or merge is active.
