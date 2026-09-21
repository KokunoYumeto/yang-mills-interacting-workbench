# Full physical gap, an actual excitation band, and extended coupling control

15 September 2026. This additive continuation preserves the delivered uniform-gap/zero-shift work and the remote PR6 base `e98b2c3af77f66fb1c1396143ca53daef586404f`.

## Results and exact scope

For the original three-spatial-dimensional open SU(2) Hamiltonian, retain
`kappa=2g^2/a`, `xi=1/(4g^4)`, all original plaquettes, the actual vacuum and its full scalar. For every box L>=2 and a>0, the final result is

    Delta_L >= (3 kappa/2)(1+sqrt(1-256xi/3+10720xi^2/9)),
    0<xi<=3/[4(32+sqrt(354))],
    g^2>=sqrt((32+sqrt(354))/3)=4.1156161030... .

The original vacuum measures and dynamics have a unique spatial-volume limit on this same CLOSED domain, with the displayed physical gap. Uniform-in-volume local-observable mixing and explicit one- and two-physical-coefficient moduli return the result to the original dynamics, including the source-majorant endpoint.

The complete second excitation-band coefficient is

    T_L = (7/15) I -(D_degree + A_adjacent)/21.

Every open-boundary degree is retained. The all-order remainder satisfies

    ||R_L(xi)||_1 <= kappa*(6713/39875)*(320|xi|)^3/(1-320|xi|),
    |xi|<1/320.

A complete integer certificate of the original L=2, 240-plaquette matrix, together with this analytic remainder, encloses the actual first excitation:

    kappa*(3-0.5833xi^2) < Delta_2 < kappa*(3-0.5656xi^2),
    xi=10^-10, g^2=50000, kappa=100000/a.

The matrix is the exact second Taylor coefficient. The analytical tail contains every spin and every later order. The original band Gram and both directions of the physical band map are explicit.

## Read the complete arguments

1. `RESEARCH_NOTE.md` G1–31: original objects, gauge constraints, coefficient source, first closed endpoint, full physical gap and native energy primitive.
2. `BAND_AND_CERTIFICATE.md` B1–32: whole first band, uniform analytic error, all local channels, exact L=2 certificate, spatial propagation, and the primary-source planar comparison.
3. `SPATIAL_RETURN.md` S1–35: complete finite dynamics, uniform mixing, coupling modulus and endpoint spatial return for the first majorant.
4. `SECOND_SOURCE.md` R1–16: the actual second logarithmic-vacuum source, its sharper bound 236, the final enlarged closed domain above, and its full physical and spatial return.

The four proofs are cumulative. R10 and R14 are the final domain, extending the earlier G22 and S35 through identical original source coefficients. The smaller conditional-influence domain is retained with its own proof rather than assigned to the whole dynamics argument.

## Replay

From the extracted package or workbench root:

```sh
python -B yang-mills/continuations/20260915-gauge-native-band/replay.py
```

Direct current verification:

```sh
python -B yang-mills/continuations/20260915-gauge-native-band/verify.py \
  --verify-receipt yang-mills/continuations/20260915-gauge-native-band/verification.json \
  --verify-box-certificate yang-mills/continuations/20260915-gauge-native-band/BOX_L2_CERTIFICATE.json
```

Repeat with `-O -B` to retain optimization coverage. The code uses the Python standard library, exact integers, fractions and outward rational square-root bounds. `BOX_L2_CERTIFICATE.json` retains all 240 original face coordinates, the full positive power vector, every fraction-free pivot determinant and the exact inertia result. `execution.json` records observed exit codes and replay hashes. `SOURCE_INTAKE.json` records source scopes and the unmerged remote base.

These finite checks verify their stated algebra, graph counts, coefficient recurrences and evaluated analytic bounds. They are not formal or independent analytical proof review. No new Lean or peer-CI run is claimed. No historical-priority claim is made for standard harmonic-analysis, perturbative, semigroup or conditional-comparison mechanisms.

## Continuum position

The final domain on the standing path is `c_n^2<=3(32-sqrt(354))/670`, where `g_n^2=1/c_n` and `a_n=a_0*2^-n`. For positive beta, `c_n=g_0^-2+beta*n*log2` eventually leaves that domain. The result does not establish the nontrivial four-dimensional continuum field or a finite positive continuum mass along that path. The next source calculation is the actual connected order-three coefficient and the complete linearized remainder at the already evaluated first two coefficients.

No remote publication or merge has been performed for this delivery. The package includes tested incremental and cumulative workbench patches and a proposed PR description.
