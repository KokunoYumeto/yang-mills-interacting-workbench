# Reproducible checks

The mathematical meaning of these files is explained in [Mathematical verification and reproduction](../VALIDATION.md). Start there rather than inferring a theorem from a success flag.

The most direct replay is:

```sh
python -B run_checks.py --output-dir runs/my-replay
```

It executes the preserved source programs and the independent comparison in seven serial, resource-capped workers. The destination must be new. The accompanying continuation directories and cubic predecessor must remain in their supplied relative positions.

| File | Contents |
| --- | --- |
| `trace_replay.json` | The ordinary and optimized original trace-producer replays, their exact table hashes and limit readbacks. |
| `quaternion_replay.json` | The complete regenerated mathematical receipt for the quaternion producer and the explicit public provenance exclusion. |
| `tangent_replay.json` | Full signed-tangent receipt comparison and the split between forced degree-zero and positive-degree equations. |
| `catalogue_bridge_delivery.json` | Independent exact comparison of all 78 coefficient classes and all 8,621 selected transports in the supplied packages. Its input keys use their original intake directory labels. |
| `compare_catalogues.py` | The same rational-polynomial comparison with paths adapted to this public directory layout. No producer polynomial implementation is imported. |
| `independent_singleface.py`, `independent_singleface.json` | A separate character recurrence through sixth order and its recorded result. |
| `independent_cube_counts_windows.py`, `independent_cube_counts.json` | All 720 cube orders, twenty complementary triple terms, finite-box incidence counts for m = 2,…,8, and the energy polynomial aggregation. The script supplies its own Windows cap. |
| `check_gap_scalars.py` | Exact rational signs, integer-square enclosures and benchmark checks from the displayed spin budgets. |
| `portable_regeneration.json` | A concise record of canonical-byte regeneration, original-verifier roundtrip, and rejection of an existing output directory. |
| `runs/` | Executed checks of the assembled public edition, with before/after source hashes and individual outputs. |

The original package receipts remain in the continuation directories. The selected records here are additional checks, not replacements for those originals. Private input transcripts, machine-specific absolute paths and copyrighted literature caches are not included.

The small independent recurrence, scalar and geometry scripts use ordinary Python assertions. Run them without `-O`. Only the original trace producer is deliberately replayed in both ordinary and optimized modes.
