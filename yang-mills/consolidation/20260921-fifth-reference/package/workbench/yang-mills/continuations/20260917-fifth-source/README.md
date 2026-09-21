# Complete fifth source and signed plaquette response

Read `FIFTH_SOURCE.md`, then `PLAQUETTE_RESPONSE.md`. `INTAKE_AND_SCOPE.md` identifies the exact incoming report, the source files actually available, and the limits of this continuation's audit.

## Completed data

- `generated/geometry_fifth.json`: every one of the 124,864 anchored connected fifth-order multisets, its one of 662 coordinate classes, and its exact signed-coordinate transport.
- `generated/fifth/`: all 662 complete fifth-source trace polynomials, original words, Casimir lists, RHS/residuals, and signed source derivatives.
- `generated/quotient/`: all corresponding complete quaternion-polynomial coefficients and full original-equation identity records; all six chords are retained where present.
- `generated/response_L2.json`, `response_L3.json`: full original finite-box response matrices through degree four, including boundary entries.
- `generated/plaquette_response.json`: complete finite-range bulk symbol, raw-orientation data, opposite-face coefficient and actual finite-volume enclosure.
- `generated/fourth_full_audit.json`, `energy_input_checks.json`, `one_plaquette_check.json`, `direct_matrix_checks.json`: executed predecessor and independent checks at their declared scope.

## Reproduce

From this directory:

```sh
python -B verify_fifth.py --verify-receipt generated/verification.json
python -O -B verify_fifth.py --verify-receipt generated/verification.json
```

These commands validate complete data coverage, all original transports, exact scalar/matrix formulas, source identities and negative controls. To recalculate the entire fifth source and signed derivative identities as full polynomials, rather than only checking the recorded data:

```sh
python -B audit_fifth.py --verify-existing --workers 4
python -O -B audit_fifth.py --verify-existing --workers 4
```

`--verify-existing` does not accept cached answers. It recomputes every original RHS, kinetic image, signed derivative and sphere-quotient polynomial, then requires exact equality with every stored output.

One command for the full new replay and named CLI corruption checks is:

```sh
python -B replay.py
```

The programs use standard-library rational arithmetic. The original paired input engine is preserved in sibling directories `20260917-quartic-cube` and `20260916-cubic-linearized`; the cumulative ZIP includes these dependencies. The formal identities are finite coefficient statements. The analytical response remainder has its separate written proof and explicit finite-volume radius. No new continuum or volume-uniform gap theorem is claimed.
