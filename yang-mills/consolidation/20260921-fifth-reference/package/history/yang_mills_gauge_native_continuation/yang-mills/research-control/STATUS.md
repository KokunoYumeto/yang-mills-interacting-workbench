# Execution and review status

14 September 2026. Parent: unmerged Yang–Mills PR4 at `dc390930a8d2774e93481206602973caff7aa7da`.

## Observed local execution

The new dependency-free `check.py` passed **56 named exact checks and 17 named negative controls**. Ordinary and optimized Python produced byte-identical JSON. `verification.json` is that complete output, including the mathematical note, workflow, state, checker and scoped AGENTS file SHA-256 values. The output SHA-256 is `98741429d7b350fb210c4bcb99e50fe5f16396bb8fe417d42cacdb4e8e5b40ed`.

A fresh copied-source directory repeated both modes and produced the same output. Four additional command-line failures were independently executed in both modes: changed proof receipt, changed peer-head snapshot, unsupported continuum claim, and wrong cached source bytes. Every process returned exit code 1 at its intended named failure. The full JSON is provided in the session download. An initial 20-second outer harness timeout supplied no result; the subsequent complete execution returned the stated results without changing the tests.

The inherited PR4 `verify.py` also passed its 181 checks. Its original note bytes match Git blob `0d79c733ff6209c991dd2b52474b1e399dd812db`. The prior checker uses SymPy; the new checker uses only the standard library. This replay is separate from the 56 new checks.

## Mathematical scope

The written note supplies the local score estimate L8, exact Hamiltonian coupling L14, conditional minimum-energy section and full metric identities L17–23, and finite tower composition L25. The exact fixtures use a declared weighted graph and polynomial algebra; their values are not interacting Yang–Mills vacuum integrals. No new Lean run, peer-CI replay, independent external mathematical review, four-dimensional continuum construction or positive continuum mass lower bound is claimed.

## Source intake

Eight source records identify original Git blobs and exact read scope. Both default branches and relevant open PR descriptions were inspected. New Zeta AMT and corrected-metric mechanisms are instantiated by explicit equations in the note. Collatz supplies a specialization-fiber regression. The ES moment and latest Collatz/817 controller contributions are retained as candidates awaiting their own complete source review, not treated as imported theorems.

Direct local Git cloning failed at DNS resolution. The authenticated connector remained available. Repository-wide generated catalogues remain unchanged. No paid Codex execution, scheduled watcher, automatic merge, or background research process was started.
