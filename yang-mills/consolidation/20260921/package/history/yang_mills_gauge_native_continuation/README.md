# Yang–Mills: gauge-native source, full physical band, and coupling continuation

15 September 2026. This delivery contains the full written mathematical continuation, exact certificates, and the selected complete predecessor sources needed to replay it. No remote branch or pull request was created by this delivery and no merge was performed.

## Read the results

Start with `yang-mills/research-control/CURRENT.md`, then the current directory:

`yang-mills/continuations/20260915-gauge-native-band/`

Its four complete proof files are `RESEARCH_NOTE.md`, `SECOND_SOURCE.md`, `BAND_AND_CERTIFICATE.md`, and `SPATIAL_RETURN.md`. The strongest final domain is in SECOND_SOURCE R10–14, extending the intermediate domains retained in the other arguments.

For the original full finite SU(2) operator, with kappa=2g²/a and xi=1/(4g⁴), every open box L>=2 and physical spacing a>0 satisfies

    Delta_L >= (3 kappa/2)(1+sqrt(1-256xi/3+10720xi²/9)),
    0<xi<=3/[4(32+sqrt(354))],
    g²>=sqrt((32+sqrt(354))/3).

The complete actual second vacuum source has the proved coefficient bound 236. The spatial vacuum and dynamics have a unique constructed volume limit on that same closed domain. The full original plaquette-band coefficient, volume-uniform all-order analytic error, original band Gram and actual L=2 first-excitation certificate are included. The fixed-spacing result and the exact original running-path domain are retained; no nontrivial four-dimensional continuum field or finite positive continuum mass is claimed.

## Replay

From this archive root, run:

```sh
python -B yang-mills/continuations/20260915-gauge-native-band/replay.py
```

The program replays the current and unchanged immediate predecessor, ordinarily and under Python -O, copies the sources, checks 20 intended CLI corruptions, restores the proof, and records observed exit codes. This full run completed successfully in the delivery session. The current exact suite has 642 named checks and 27 false-formula controls. The 240-face certificate retains all 2,303,960 checked fraction-free divisions.

For only the current mathematical certificate:

```sh
python -B yang-mills/continuations/20260915-gauge-native-band/verify.py --verify-receipt yang-mills/continuations/20260915-gauge-native-band/verification.json --verify-box-certificate yang-mills/continuations/20260915-gauge-native-band/BOX_L2_CERTIFICATE.json
```

Finite tests and file hashes have their declared scope. The operator-domain, infinite-volume, and analytic-remainder proofs are written in full; no new Lean execution or independent analytical review is claimed. Historical receipts preserve their source-time meaning.

## Apply exactly one patch

The cumulative `yang_mills_gauge_native_continuation.patch` targets the exact PR6 revision `e98b2c3af77f66fb1c1396143ca53daef586404f`. It adds the previous two unpublished delivered continuations together with the present contribution, and updates only the CURRENT pointer among inherited paths.

The incremental `yang_mills_gauge_native_continuation_incremental.patch` targets the immediately preceding delivered uniform-gap/zero-shift tree. It adds fifteen new files and updates CURRENT. Do not apply both patches to the same tree.

Each patch was checked, applied to its own freshly restored selected base, compared against every one of the 60 selected target file bodies, and replayed normally and under -O. `PATCH_VALIDATION.json` records all four successful post-application executions. `SELECTED_SOURCE_MANIFEST.json` names all 60 selected mathematical source/receipt files. These selected bases are explicitly not a full repository clone.

`PROPOSED_PR.md` contains the proposed publication description. Source attribution and inspected peer/literature scope are recorded in SOURCE_INTAKE. No downloaded third-party paper, credentials, fonts, private dialogue or unused development corpus is included.
