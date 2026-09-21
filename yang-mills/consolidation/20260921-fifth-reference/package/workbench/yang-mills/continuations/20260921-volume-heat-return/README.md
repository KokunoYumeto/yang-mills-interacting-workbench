# Box-independent heat and the complete physical complement

21 September2026. Read VOLUME_UNIFORM_HEAT.md (U1–U33) and GROWING_OBSERVATIONS_AND_COMPLEMENT.md (M1–M25). They retain the original open-box SU(2) Hamiltonian and supply:

- A complex heat row-sum bound512 exp(-3tau/2) on the fixed source disk R0=3/256, replacing the preceding radius1/M for this new estimate. The complete fourth-order heat remainder, all inverse moments, and spatial tails follow with no exterior-volume factor.
- Boundary-safe exact sums of all559 marked contributions on199 original anchored supports. For every L>=2 and g^2>=16 the state, inverse-energy, and kinetic Grams have the explicitly calculated bounds.
- The full original complement is retained. Its zero-energy Schur subtraction is less than1/625 of the plaquette-primitive energy. Both mixed energy terms remain; the restored state norm changes by less than1/600. The same operator statements hold for the infinite plaquette family at fixed lattice spacing.
- Actual opposite-face heat positivity throughout1<=kappa*t<=3 atxi=1e-10, in every exterior box. A fixed physical heat horizon controls fixed-rank quotient returns; growing ranks retain their explicit logarithmic horizon.

The local-source estimates used by this proof are rederived, including the exact Fourier coefficients, scalar-return functional and Banach generator domain. The older stronger-coupling analytical claims keep their previous independent-audit qualification. This is a written proof contribution with exact finite evidence, not a Lean or independent human certificate. A nontrivial four-dimensional continuum theory and finite positive continuum mass have not been established.

Reproduce from this directory:

```sh
python -B produce_bounds.py --verify-existing
python -B audit_bounds.py --verify-receipt verification.json
python -O -B audit_bounds.py --verify-receipt verification.json
python -B replay.py --output-dir /tmp/ym-volume-heat-replay
```

The audit independently reconstructs original geometry and coefficient integration, includes full raw-Gram/complement matrix fixtures, and rejects specified false formulas. Its count is an execution inventory, not a mathematical progress score. The exact parent proof/producer files and receipts remain unchanged in the cumulative workbench. Current execution and attempts are recorded separately.

The additional original-Haar estimate U29a–b retains the Haar coefficient separately from its mean return. Its radius45/4096, prefactor6184/25 and decay15/8 give the M10 improved family intervals. Atg^2>=16 the full complementary energy subtraction is less than1/1000, and the restored state addition is less than1/1000. Broader rows atg^2>=10 and12 retain their full explicit constants. No increase in the conservative all-volume source radius is claimed.

Fresh source, copied-source and named corruption replay:

```sh
python -B replay.py --output-dir /tmp/ym-volume-replay
```

The output directory is deliberately outside the sealed archive. The checker and all named failures remain active under Python -O. The replay calls no network tool and starts no scheduled research process.
