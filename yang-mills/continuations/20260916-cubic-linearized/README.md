# Connected cubic source and full linearized Yang–Mills return

The two calculations selected by the saved checkpoint are executed here. Read `CUBIC_SOURCE.md`, then `LINEARIZED_RETURN.md`. Both proof bodies preserve the full original SU(2) Hamiltonian, physical units, Haar mass, gauge image, source labels and scalar energy.

The complete cubic source has five connected geometric/multiplicity families and norm at most 944984/351. The actual residual at q2=xi*v1+xi^2*v2 is xi^3*v3+xi^4*B(v2,v2), with a fully specified finite Casimir-projector formula for every quartic residual component. Its evaluated spin budgets give the quartic discriminant

    D(x)=(46457856*x^4+183150656*x^3+18324072*x^2-1168128*x+13689)/13689.

Let alpha be its first positive root, approximately0.0170787544707772676. For every original open box L>=2, every a>0 and g^2>=1/(2sqrt(alpha)), the proof gives

    Delta_L >= kappa [3(1+sqrt(D(xi)))/2+(1136/13)*xi^2],
    kappa=2g^2/a, xi=1/(4g^4).

The threshold for g^2 is between3.825973052393385 and3.825973052393386. In particular g^2>=4 gives Delta_L>1.8385*kappa. The inverse, full nonlinear tail and closed endpoint are proved, rather than assumed. The actual fourth ground-energy coefficient is kappa(5M/216-2J/1053), with original finite-box M,J and an explicit analytic remainder.

## Reproduce

Python3.10+ and its standard library suffice. From this directory:

```sh
python -B verify.py --verify-receipt verification.json
python -O -B verify.py --verify-receipt verification.json
```

The programs differentiate original link products and independently evaluate projected receiving formulas. All612 anchored connected cubic multisets are tested at two exact rational quaternion assignments. Haar harmonic moments, noncommuting singlet projectors, full original graph counts, coefficient recurrences, source budgets, root brackets and an independent energy recurrence have separate tests. False formulas and malformed receipts must be rejected in their specified checks. The analytical proofs are written arguments for review; no new Lean execution, vacuum sampling, spin truncation of the full Hamiltonian, or independent analytical review is claimed.

`state.json` is the mathematical checkpoint. `SOURCE_INTAKE.json` records exact reading scopes and primary literature parameter maps. `execution.json` records observed local executions; the mathematical receipt contains no elapsed-time-dependent data. Existing main and earlier review branches are preserved. This packet is self-contained for its mathematical proofs and checker, so it can be reviewed on PR6 without pretending that every earlier owner-facing archive was remotely published.

The four-dimensional continuum field and finite positive continuum mass remain unestablished. The next actual source is v4=2B(v1,v3)+B(v2,v2), retaining the complete same-support action rather than repeating the completed generic bounds.
