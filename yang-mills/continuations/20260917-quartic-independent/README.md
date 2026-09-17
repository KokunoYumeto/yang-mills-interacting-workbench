# Yang–Mills audit and completed fourth/sixth-order calculations

**Requested basis:** the uploaded `Pasted markdown(6).md`, preserved unchanged.
**Result:** corrected recovery of the interrupted text, a complete fourth-order
logarithmic-vacuum source and signed tangent catalogue, and the complete sixth-order
original open-box ground-energy coefficient, including the six-face cube surface.

Start with [AUDIT_REPORT.md](AUDIT_REPORT.md). The complete arguments are:

- [Fourth-order source](proofs/FOURTH_ORDER_SOURCE.md), with all 78 exact coefficient files.
- [Sixth-order energy](proofs/SIXTH_ORDER_ENERGY.md), including both cube calculations and an independent finite-volume remainder.
- [Signed tangent certificate](proofs/SIGNED_TANGENT_CERTIFICATE.md), with 282 explicitly expanded third-degree response entries.

## Completed results and scope

The original parameters remain `kappa=2g^2/a` and `xi=1/(4g^4)` in
`H/kappa=K+xi(2M-S)`. On the original open box with vertices `{-L,...,L}^3`,
put `m=2L`. The completed sixth ground-energy coefficient is

    e6=-(211396463*m^3+30959193*m^2+21845782*m+2336684)/4691494080.

For L=2:

    E0/kappa=480*xi-80*xi^2+(1198/351)*xi^4
              -(3528610133/1172873520)*xi^6+R8(xi),
    |R8(xi)| <= (3/4)*(640*|xi|)^8/(1-(640*|xi|)^2), |xi|<1/640.

The fourth-order source includes all 8,621 original anchored connected multisets,
organized in 78 exact lattice-symmetry classes. Its 4,044 rational monomials and
all original-coordinate return maps are stored, not left as an unevaluated inverse.
In particular,

    v4^(p,p,p,p)=17*chi1(Omega_p)/10368-7*chi2(Omega_p)/51840.

The three-dimensional sixth-order calculation must include the original cube's
six distinct faces, with linked contribution `-83/1944` per cube. Its 720
insertion orders and independent three-plus-three calculation both appear in the
record. The one-plaquette coefficient matches DLMF28.6.5 under the explicitly
proved original parameter map.

The inherited scalar discriminant arithmetic passes its separate audit, but the
older uniform physical-gap and volume-limit proofs are not independently
recertified here. No new uniform-coupling threshold, nontrivial continuum field,
or four-dimensional continuum mass-gap theorem is claimed by this package.

## Reproduce, without external dependencies

Use Python3.10+ and its standard library from this extracted directory:

```sh
python -B checks/verify_manifest.py
python -B checks/verify.py --verify-receipt results/verification.json > verification_replay.json
python -O -B checks/verify.py --verify-receipt results/verification.json > verification_replay_optimized.json
python -B checks/verify_signed_tangent.py --verify-receipt results/signed_tangent.json > tangent_replay.json
```

The main verifier rebuilds every polynomial coefficient, checks its original
inverse/source equations, repeats the original-link jet and gauge-return audit,
checks all small-cluster sixth energies, all cube orders, finite-box counts,
Mathieu coefficients and scope-sensitive negative controls. The signed-tangent
verifier independently constructs the logarithmic source directly and evaluates
every finite tangent residual.

To generate a new observed process record without replacing this delivery's
historical receipt:

```sh
python -B checks/replay.py --output results/execution_rerun.json
python -B checks/replay_signed_tangent.py --output results/signed_tangent_execution_rerun.json
```

These are explicit foreground research/checking commands. No remote service,
paid model, background watcher or Git write is started by this package.

## Contents

`input/` has the original upload. `recovered/` has the exact Git-verified geometry
and an explicitly incomplete cleaned excerpt. `proofs/` has the three new notes.
`calculations/` and `checks/` contain all executable dependencies. `results/`
has every coefficient, all8,621 symmetry transports, all720 cube paths, the full
verification records and observed execution logs. `sources/` has provenance,
historical-file availability and an optional pinned GitHub recovery helper.
`logs/` preserves this session's actual calculation output. The manifest binds
all packaged bytes; newly generated replay files are not historical manifest entries.

Two working artifacts are retained rather than presented as final programs:
`calculations/gauge_polynomial_v1.txt` is the earlier source version before the
four-face/five-cycle extension, and `calculations/linked_sixth_scratch.py` is the
intermediate linked-weight calculation. Use the entry points above for the final
verified results. These are calculation artifacts, not a private reasoning transcript.

## Recovery limits

Earlier ZIP names printed inside the upload were not mounted attachments in this
session. They are listed in `sources/historical_artifact_inventory.json`, rather
than replaced by fabricated files. The exact original geometry was recovered from
PR8 at the pinned Git revision; other historical proof text was read through the
connector where available. `sources/recover_pinned_github.py DESTINATION` can
retrieve all committed cubic-source text at that revision when network access is
available. It checks Git blobs and never executes downloaded code. It was not
represented as successfully run in this offline calculation environment.

No remote repository change or pull request was made during this audit. All
new calculations are supplied here for independent review. Exact polynomial
certificates verify their stated finite algebra; the written structural and
analytic proofs are not a Lean certificate or an independent external review.
