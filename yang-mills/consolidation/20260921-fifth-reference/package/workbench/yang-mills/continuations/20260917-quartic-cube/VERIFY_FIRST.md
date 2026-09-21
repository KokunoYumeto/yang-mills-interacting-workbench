# Replay the original-coordinate calculation

The current source producer uses Python's standard library only. Its one code
input from the preceding contribution is the unchanged sibling `geometry.py`.
The preceding two complete proof bodies are also hash-bound as used inputs.

The archive contains the five full generated tables and both full receipts.
After applying the patch to the exact PR8 tree, reconstruct the preceding
receipt with its original materializer before running the optional parent replay:

```sh
cd yang-mills/continuations/20260917-quartic-cube
python -B ../20260916-cubic-linearized/materialize_receipt.py
python -B verify.py --verify-receipt generated/verification.json
python -O -B verify.py --verify-receipt generated/verification.json
python -B replay.py
```

`verify.py` verifies the actual stored table hashes, regenerates all coefficients,
transports, scalar budgets and energy tables, and compares the resulting complete
mathematical record. It uses explicit exceptions, so `-O` disables no requirement.
`replay.py` also supports `--part current-ordinary`, `current-optimized`,
`parent-ordinary`, and `parent-optimized`. Each part is the corresponding original
command, with its exit and output identity recorded; it changes no mathematics.
The final recorded session executed these four parts separately after combined
harness calls exceeded the execution-service envelope.

Fresh-copy and corruption checks are executable as well:

```sh
python -B audit_delivery.py --phase copy --record copy.json
python -B audit_delivery.py --phase copy --optimized --record copy-O.json
python -B audit_delivery.py --phase negative --record negative.json
python -B audit_delivery.py --phase negative --optimized --record negative-O.json
python -B audit_delivery.py --phase mathematical-negative --record count.json
python -B audit_delivery.py --phase mathematical-negative --optimized --record count-O.json
```

These commands copy the selected source directories to a temporary directory;
all intentional corruptions occur there. Six immediate named corruptions and
one incorrect mathematical count are rejected in each Python mode. A crash at
an unrelated step does not count as success. `execution.json` records the actual
20 completed replay/audit executions and their exact outputs. The external
patch-application audit is in the delivery root's `patch_validation.json`.

The 1,056 named finite checks and 19 false-formula controls verify the declared
coordinate calculations and scalar bounds. The Banach-space construction,
original domains and spectral return are written proofs in the three companion
notes; no Lean certification or independent external analytical audit is claimed.
