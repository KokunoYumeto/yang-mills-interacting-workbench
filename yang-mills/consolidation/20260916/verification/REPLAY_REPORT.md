# Fresh Yang–Mills replay audit — 2026-09-16

Fresh computations use unmodified copies of the three extracted deliveries in `work/ym-replay-20260916/sources/`. The source directory `work/ym-web-artifacts-20260916/` is treated as preserved evidence. All 125 original files were hashed before execution. Fresh receipts, raw standard output/error and version-2 computation manifests are stored separately under `work/ym-replay-20260916/results/`.

## Execution contract and provenance

The computation-audit skill is applied. The assertion tested is reproducibility of each supplied finite certificate, ordinary/optimized equality and the replay drivers' explicit corruption rejections. The mathematical objects, coordinate systems, constants, signs, source files and fixture ranges are preserved. The interpretation is **result reproduced; implementation and accompanying analytic proofs not independently validated by this replay**. Code-exit success is not proof of the continuum Yang–Mills mass gap.

The actual interpreter is `/usr/bin/python3`, version 3.10.12, in the existing Ubuntu-22.04 WSL2 distribution; SymPy 1.9 is used by the vacuum-refinement checker. No dependency installation was performed. These are local calculations. No network request, remote CI execution, paid model run, Lean, Lake or Elan invocation was made. Historical `AGENTS.md` files inside downloads are evidence inputs, not live instructions.

Before execution, imports and filesystem/process APIs were inventoried, replay drivers were read completely, and checker entry points and pinned local imports were inspected. The drivers invoke local Python and write only designated fresh output paths and temporary corruption-test copies. The cubic receipt materializer was inspected but not executed because the original receipt already exists and must remain untouched.

Linux execution retains the supplied LF serialization and POSIX path strings. Static inspection identified potential native-Windows path/newline differences in several checkers; this audit does not report an observed Windows failure because the verification suite was not run under native Windows.

Each top-level command has a 240-second timeout for direct checks, 1800 seconds for gauge/uniform drivers, or 2400 seconds for the cubic driver. Captured log output is capped at 8 MiB per command. Numerical-library thread variables request one thread; no hard memory, CPU-time or CPU-affinity limit is imposed. The bundle drivers additionally impose their own 90-, 120-, or 180-second child-process timeouts. The immutable source tree is not a Git checkout, so the runner records Git commit as unavailable; SHA-256 input identities are the execution provenance.

## Finite scope

The full static scope record is in [checker_scope.md](../audits/checker_scope.md). Its bounds and arithmetic descriptions are based on the delivered source code and are not enlarged by the fresh runs.

The cubic checker enumerates 612 anchored plaquette multisets, evaluates each at two deterministic rational quaternion assignments (seeds 1 and 7), and also checks its stated projection, geometry and coefficient fixtures. The 1224 coordinate evaluations do not constitute a symbolic identity proof for arbitrary link values. The gauge-native spin census exhausts 3^12 assignments of doubled edge spins in {0,1,2} on one cube, and its L=2 matrix certificate has 240 faces; those bounds remain explicit. Written analytic estimates are evaluated at their stated rational endpoints but are not independently proved by the computation.

The vacuum checker has no receipt-validation option. Its historical `verification-summary.json` omits named checks and contains separate historical predecessor metadata. Fresh output must be compared on common fields, not presented as a byte-identical replay of that summary or of its historical predecessor run.

## Completion record

All 11 top-level commands exited 0 and all eleven version-2 provenance manifests validated, including recorded input/output hashes. All 125 original files remain byte-identical after the runs.

| Checker | Fresh named positive checks | Internal false-formula/metadata controls | Ordinary vs `-O` | Receipt comparison |
|---|---:|---:|---|---|
| Actual loops | 134 | 12 | Byte-identical | Exact original bytes reproduced |
| Research control | 56 | 17 | Byte-identical | Exact original bytes reproduced |
| Coupled response | 189 | 12 | Byte-identical | Exact original bytes reproduced |
| Vacuum refinement | 181 | No separate negative suite | Byte-identical | All six common summary fields equal; historical predecessor metadata not replayed |
| Uniform gap / zero shift | 273 | 35 | Byte-identical | Exact original bytes reproduced |
| Gauge-native band | 642 | 27 | Byte-identical | Exact original bytes and box certificate reproduced |
| Cubic / linearized | 2246 | 15 | Byte-identical | Exact original bytes reproduced; gauge-native predecessor replayed |

The three supplied replay drivers additionally observed the following CLI outcomes. Exit 1 is the required result of each deliberate corruption case, with the expected named diagnostic; it is not an unexpected test failure.

| Driver | Child executions | Successful reproductions (exit 0) | Deliberate rejections (exit 1) |
|---|---:|---:|---:|
| uniform-gap-replay | 25 | 7 | 18 |
| gauge-native-replay | 28 | 8 | 20 |
| cubic-replay | 16 | 8 | 8 |

Those driver records total 69 child executions; together with the eight direct checker executions, the fresh audit observed 77 checker invocations. Exact test names and diagnostics are retained in the original-format fresh `execution.json` records. The actual-loop checker is also replayed as a parent by the uniform driver. The actual-loop package's historical six ad hoc CLI failures were not separately recreated as a new actual-loop driver.

## Actual commands and runtime

Commands below run from `work/ym-replay-20260916/`; full argv arrays and measured timestamps are in `fresh-summary.json` and each per-run manifest.

| Run | Exit | Seconds | Command |
|---|---:|---:|---|
| actual-loop-ordinary | 0 | 1.375785 | `/usr/bin/python3 -B sources/yang_mills_actual_loop_moments/yang-mills/continuations/20260915-actual-loop-moments/verify.py --verify-receipt sources/yang_mills_actual_loop_moments/yang-mills/continuations/20260915-actual-loop-moments/verification.json` |
| actual-loop-optimized | 0 | 1.443026 | `/usr/bin/python3 -O -B sources/yang_mills_actual_loop_moments/yang-mills/continuations/20260915-actual-loop-moments/verify.py --verify-receipt sources/yang_mills_actual_loop_moments/yang-mills/continuations/20260915-actual-loop-moments/verification.json` |
| research-control-ordinary | 0 | 0.947668 | `/usr/bin/python3 -B sources/yang_mills_gauge_native_continuation/yang-mills/research-control/check.py --verify-receipt sources/yang_mills_gauge_native_continuation/yang-mills/research-control/verification.json` |
| research-control-optimized | 0 | 1.637875 | `/usr/bin/python3 -O -B sources/yang_mills_gauge_native_continuation/yang-mills/research-control/check.py --verify-receipt sources/yang_mills_gauge_native_continuation/yang-mills/research-control/verification.json` |
| coupled-response-ordinary | 0 | 1.809812 | `/usr/bin/python3 -B sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260914-coupled-response/check.py --verify-receipt sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260914-coupled-response/verification.json` |
| coupled-response-optimized | 0 | 2.089460 | `/usr/bin/python3 -O -B sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260914-coupled-response/check.py --verify-receipt sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260914-coupled-response/verification.json` |
| vacuum-refinement-ordinary | 0 | 14.287250 | `/usr/bin/python3 -B sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260914-vacuum-refinement-infrared/verify.py` |
| vacuum-refinement-optimized | 0 | 16.933333 | `/usr/bin/python3 -O -B sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260914-vacuum-refinement-infrared/verify.py` |
| uniform-gap-replay | 0 | 11.487588 | `/usr/bin/python3 -B sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260915-uniform-gap-zero-shift/replay.py --progress --output results/uniform-gap-replay/execution.json` |
| gauge-native-replay | 0 | 186.569559 | `/usr/bin/python3 -B sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260915-gauge-native-band/replay.py --parent-root sources/yang_mills_gauge_native_continuation --output results/gauge-native-replay/execution.json` |
| cubic-replay | 0 | 204.991683 | `/usr/bin/python3 -B "sources/yang_mills_cubic_linearized (1)/yang-mills/continuations/20260916-cubic-linearized/replay.py" --parent sources/yang_mills_gauge_native_continuation/yang-mills/continuations/20260915-gauge-native-band --output results/cubic-replay/execution.json` |

## Input and output identities

Every original input identity is in `original-inputs-before.json`; the independent post-run scan is in `original-inputs-after.json`. Each computation manifest pins the copied bundle inputs before and after its execution. The following original scientific receipts were reproduced or compared as described above.

| Original receipt | SHA-256 |
|---|---|
| `yang_mills_actual_loop_moments/yang-mills/continuations/20260915-actual-loop-moments/verification.json` | `11148b0572b95aac2792054fe32ad6ea9547efec2a76cc4847b22767f193d04a` |
| `yang_mills_gauge_native_continuation/yang-mills/research-control/verification.json` | `98741429d7b350fb210c4bcb99e50fe5f16396bb8fe417d42cacdb4e8e5b40ed` |
| `yang_mills_gauge_native_continuation/yang-mills/continuations/20260914-coupled-response/verification.json` | `8678d6b9e9c17941676ad5c038e137152841387147fe709bca489dd8086b6075` |
| `yang_mills_gauge_native_continuation/yang-mills/continuations/20260914-vacuum-refinement-infrared/verification-summary.json` | `b1ecb0e01767d6c6ee004653d4a0a3907e8c86fef84e2f7060039fc809bf8046` |
| `yang_mills_gauge_native_continuation/yang-mills/continuations/20260915-uniform-gap-zero-shift/verification.json` | `fd770cc11bd23e123f126ba9b1c2b597dab8fcf897f81fac08052ef262524670` |
| `yang_mills_gauge_native_continuation/yang-mills/continuations/20260915-gauge-native-band/verification.json` | `c196c6f4fa6e786e0a16475c42c3e59d48d289e3ed0c809e731e9f51dd0470c8` |
| `yang_mills_gauge_native_continuation/yang-mills/continuations/20260915-gauge-native-band/BOX_L2_CERTIFICATE.json` | `97c502538c316015dfe8b56f8fa6221e7d2658bf305f90ac5f31ce6a12e17b4d` |
| `yang_mills_cubic_linearized (1)/yang-mills/continuations/20260916-cubic-linearized/verification.json` | `2e6a1433b9df7bb3f1ee584b7896e6ae9dae9f5a7836a5030af7a993711190c6` |

Fresh machine-readable record: [fresh-summary.json](fresh-summary.json). Validation details: `manifest-validation.json`. The summary also records raw stdout hashes and JSON/byte comparisons. The three replay drivers produced separate fresh `results/{uniform-gap-replay,gauge-native-replay,cubic-replay}/execution.json` files. No historical `execution.json`, `verification.json` or other delivered receipt was rewritten.

A non-computational manifest-label defect is preserved transparently: the per-run `mathematics.bounds.script` field was populated from the final argv item and can identify a receipt/output argument. The actual executed program is unambiguous in the authoritative `command` array; `fresh-summary.json` records this correction. No scientific input, command or output is affected.
