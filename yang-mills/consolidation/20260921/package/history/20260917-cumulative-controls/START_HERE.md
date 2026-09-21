# Cumulative Yang–Mills research: readable text edition

17 September 2026. This ZIP contains the available earlier source archives unpacked as text, their complete dated proof versions and receipts, the incoming independent-session report, and the newest completed fifth-source/response calculation. No nested archive must be unpacked to read the mathematics.

## Read the new work

1. [Latest fifth-source proof](workbench/yang-mills/continuations/20260917-fifth-source/FIFTH_SOURCE.md).
2. [Actual plaquette-response matrix and finite-volume remainder](workbench/yang-mills/continuations/20260917-fifth-source/PLAQUETTE_RESPONSE.md).
3. [Source intake and exact audit scope](workbench/yang-mills/continuations/20260917-fifth-source/INTAKE_AND_SCOPE.md).

A [separate vacuum-density return](supplementary_audits/SOURCE_EXPECTATION.md) checks the signed response through the full density and its retained mean subtraction.

The one-file [cumulative mathematical reader](CUMULATIVE_RESEARCH.md) includes the preserved proof texts and the two latest proofs. [Current state](CURRENT_STATE.json) distinguishes completed new calculations from retained older claims.

## Audit scope

The new calculation checks complete rational polynomial identities for the entire fifth coefficient and every degree-four plaquette-source derivative. It proves a separate finite-volume analytic response enclosure from the original free gap and bounded original plaquettes. That radius depends on the actual number M of plaquettes.

The uploaded other-session report explicitly leaves the older volume-uniform gap analytical chain without independent recertification. Its report and that limitation are preserved. Its linked `yang_mills_audit_and_completion.zip` was not mounted; those reported 131 files are not fabricated or listed as imported. Earlier archives actually mounted here are preserved in `history/`, and all their included text entries have exact provenance in `provenance/INPUT_ARCHIVES.json`.

No new continuum mass-gap proof, improved uniform coupling threshold, Lean certificate, independent external analytical review or remote GitHub change is asserted by this cumulative edition.

## Reproduce

From the extracted root:

```sh
python -B verify_cumulative.py
cd workbench/yang-mills/continuations/20260917-fifth-source
python -B verify_fifth.py --verify-receipt generated/verification.json
python -O -B verify_fifth.py --verify-receipt generated/verification.json
python -B audit_fifth.py --verify-existing --workers 4
```

`replay.py` in the same directory runs the complete new replay in both Python modes and checks named corruptions. All scripts use the standard library. Original predecessor dependencies are present in the sibling directories. Historical receipts retain their original execution scopes; the new execution records identify the checks actually rerun in this continuation.

## Arrangement

`workbench/` is the cumulative working text tree with the new checkpoint. `history/` preserves every UTF-8 entry from the ten actual predecessor ZIPs, including every differing older version. `incoming/` preserves the exact new report. `provenance/` records each original ZIP identity and every installed-source transition. `MANIFEST.json` binds every delivered file to its size and SHA-256.
