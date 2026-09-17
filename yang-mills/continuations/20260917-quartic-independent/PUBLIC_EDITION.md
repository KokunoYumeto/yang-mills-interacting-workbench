# Reading and reproducing this edition

This directory contains the independent tree-quaternion calculation of the fourth logarithmic vacuum source, the explicit signed response to individual plaquette couplings, and the sixth-order vacuum energy for the original open-box SU(2) Hamiltonian. The proof notes explain the equations; the coefficient tables retain the exact rational answers; the programs regenerate and check them.

Start with [the collection reader and guide](../../consolidation/20260917/README.md). The [verification account](../../consolidation/20260917/VALIDATION.md) explains how this calculation agrees with the original trace-word description and how its finite-volume remainder differs from the separate volume-uniform source argument.

## Preserved mathematics

The original proof notes, calculation programs, generated tables and historical receipts are retained unchanged. Two added scripts make their receipt checks portable across Windows and slash-based file systems. They do not change the recurrence, differential operator, rational arithmetic, coefficient tables or mathematical tests.

From this directory:

```sh
python -B verify_public_catalogue.py --package-root .
python -B verify_portable_tangent.py --package-root .
```

The first command executes the original verifier's `main_checks` and compares its complete reconstructed mathematical record with `results/verification.json`: the result data, all named checks, negative controls and scope statements must agree exactly. It also checks every distributed source hash named in that receipt. The second executes the unchanged signed-tangent checker and compares the complete receipt after changing only path separators to forward slashes. A nonzero exit means the replay did not pass.

For resource-capped execution, use the serial [collection runner](../../consolidation/20260917/verification/run_checks.py) with `--checks quaternion tangent` and a new output directory. It enforces one worker, one CPU, a 2 GiB memory cap and a 600-second wall limit for each check.

## The one excluded input

The supplied research package included a raw conversation transcript at `input/Pasted markdown(6).md`. This public edition omits that transcript. It is historical context, not a mathematical input read by `main_checks`; its removal does not remove any coefficient program, proof or certificate.

The preserved original receipt names that file and records its historical SHA-256:

`080f9b988c5dff5b1d8669041f672bf44d783bbeb062c88d48a7eb836cc35f16`.

The public wrapper explicitly reports this as an excluded provenance input and marks it `freshly_checked: false`. It does not substitute another transcript or invent a successful file check. Every other required source identity is checked normally. A strict replay with the original private input was also completed before publication, but the public command neither needs nor distributes it.

Consequently the unmodified historical all-input command in the original README is not the public reproduction command: it still expects that private file, and its path keys also differ on Windows. Use the additive wrappers above. The originals remain available for comparison rather than being silently rewritten.

## Exact scope of the response

The tangent receipt checks 2,156 class-indexed coefficient equations: 282 degree-zero equations with their plaquette forcing subtracted, and 1,874 positive-degree zero residuals. Its 282 stored degree-three response polynomials are exact finite coefficients. Repeated lower-order entries in different class downsets are not distinct new global results. A truncated response is not asserted to invert the entire infinite operator; the remaining higher-degree residual is given in the proof note.

The collection's independent trace-to-quaternion program compares every one of the 78 fourth-order representatives as a full polynomial and verifies the selected transports for all 8,621 anchored supports. It does not infer equality from sampling a few link configurations.
