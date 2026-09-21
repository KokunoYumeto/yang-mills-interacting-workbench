# Exact execution and mathematical scope

15 September 2026. The complete finite replay in `execution.json` returned
success. It includes 7 positive executions with retained exit codes and stdout
identities: current ordinary/optimized, unchanged parent ordinary/optimized,
fresh selected-source ordinary/optimized, and replay after every deliberately
corrupted copied source was restored. All corresponding outputs matched their
complete original receipt bytes.

The final current checker has **273 named exact checks and
35 deliberately false-formula controls**. The unchanged actual-loop predecessor
has 134 checks and 12 controls. These counts describe the executed finite
algebra and validation cases, not mathematical discoveries or an analytic
confidence score. An additional **18 CLI corruptions** were rejected with exit1 at
their exact named errors in ordinary and optimized Python. They cover source
pins, source-to-receipt identity, proof-domain changes, continuum promotion,
missing response scope, wrong target and duplicate JSON keys.

Final scientific receipt SHA-256:

    fd770cc11bd23e123f126ba9b1c2b597dab8fcf897f81fac08052ef262524670

Current checker SHA-256:

    d78432d5eeab097efa7aa018de30932d67c4c77edcc4ceeeae843b955f60f655

Full replay source SHA-256:

    a1362e26cff9ec593046085e366a02086e04782afe2615e6ace4bbb1f70c15f1

The exact analytical result is H1–H23, with its full U/O/V proof dependencies.
Its domain is the original operator at g²>=15, a>0, all original open boxes.
The zero-shift narrow interval is for xi=10^-8. The fixed-spacing volume limit
is unique for the actual vacuum and dynamics on this same coupling domain.
The four-dimensional continuum gap is not asserted.

The written analytic proofs have been checked within this research session;
no independent external proof review, new Lean elaboration, numerical vacuum
sample or remote CI run is claimed. Matrix fixtures are marked as such. The
actual response intervals are rational evaluations of the written analytical
bounds, not sampled approximations to the vacuum.

`DEVELOPMENT.md` retains the diagnostic-format repair and the scope of earlier
outer harness timeouts. None of those incomplete runs is counted as passed.
Use `python -B yang-mills/continuations/20260915-uniform-gap-zero-shift/replay.py`
from the repository or complete offline package root for the same complete
finite replay. Its `--output` option writes an explicit execution record.

No remote modification, PR creation, merge, paid model run, or scheduled
research task was performed. The delivery's tested Git patches and outer
`DELIVERY.json` record the exact patch bases and application results. Main,
other research branches and all inherited proof/receipt files stay unchanged.
