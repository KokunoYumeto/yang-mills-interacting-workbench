# Actual heat correlations and original-metric error control

21 September 2026. Read these complete proofs in order:

1. `PHYSICAL_HEAT_COEFFICIENTS.md`: all marked time functions through degree four,
   their complete original-link calculation, and the fourth-order first band.
2. `HEAT_REMAINDER_AND_NATIVE_METRICS.md`: independent finite-volume, uniform-time
   remainder; actual time-interval positivity; full forcing/response/state Grams.
3. `RH_HEAT_TRANSFER.md`: the precisely read Split-Zero heat and inverse-power
   sources, their actual Yang–Mills receiving maps, support minima and errors.

The complete physical parameter convention is kappa=2g^2/a, xi=1/(4g^4).
Physical time is t=tau/kappa. All state and energy Grams retain their original
values. The new Cauchy radius is1/M for M original plaquettes; it is explicitly
finite-volume. This contribution does not certify the old volume-uniform
analytical chain or claim the smooth four-dimensional continuum mass gap.

## Reproduction

From this directory run the fast complete-record checker:

```sh
python -B verify.py --verify-receipt verification.json
python -O -B verify.py --verify-receipt verification.json
```

The full mathematical replay is separate:

```sh
python -B produce_heat.py --verify-existing
python -B audit_heat_polynomials.py --verify-existing
python -B independent_heat.py
python -B assemble_heat.py
python -B certified_bounds.py
python -B extract_band.py
```

Each producer reproduces its full exact JSON. The final checker binds their
source, all three proofs, inherited dependency blobs and generated results to
SHA-256. `replay.py` runs the complete ordinary/optimized suite with actual exit
records; `--fast` reruns only the final record checks and independent finite
calculations. It writes its fresh execution record under the requested output
path; avoid changing a sealed cumulative manifest during a replay by directing
that output outside the archive.

## Full data

`generated/heat_coefficients.json` has all17 cases and84 marked rational
resolvents, with their original time-zero and two derivative returns.
`full_polynomial_audit.json` records every original sphere-quotient source
identity. `cube_heat_orders.json` contains all5,400 independent insertion
records, not just a count. `heat_matrix_L2.json` retains the complete original
240-face matrices; `heat_transports_L2.json` retains their inverse coordinate
maps. `first_band_L2.json` includes the fourth coefficient, both Gram
coefficients and all1,440 raw-coordinate adjoint defects. The native metric
and interval records retain all rational endpoints.

Small `adjacent*` and `opposite*` files are earlier exact selected-case records;
the final checker verifies their mathematical entries against the complete
catalogue and box assembly. Their elapsed-time fields are historical diagnostics,
not mathematical inputs or replay acceptance criteria.

## Recovery and provenance

The previous cumulative archive is preserved. Exactly six documents/result files
from the separately delivered sixth-source checkpoint were available and are
included byte-for-byte. Its absent producer, catalogue and unfinished audit
were not recreated or assigned a completed status. See `RECOVERY_STATUS.json`.
The current calculation uses the complete available preceding coefficient
engine instead. `SOURCE_INTAKE.json` distinguishes exact reading, transferred
arguments, orientation-only intake and external primary-source checks.

No paid model job, scheduled process, GitHub write or merge was performed in
this continuation. Mathematical priority and independent analytic verification
are not asserted. The preserved sources retain their human attributions and
existing licences; this additive research text and code carry the same collective
workbench attribution, The Clankers, with AI assistance disclosed here.
