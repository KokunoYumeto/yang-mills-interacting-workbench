# Verification and publication status

## Mathematical delivery

The complete written arguments are in `RESEARCH_NOTE.md`. They use the actual
finite-lattice SU(2) Hamiltonian, its positive ground state, and the specified
loop-holonomy conditional measure. In particular, the narrow intervals A46–49
are bounds for that interacting vacuum, obtained by analytical comparison and
exact arithmetic. No sampled or numerically fitted vacuum is used.

The note also supplies all-coupling estimates with the original kappa, xi and
loop-length dependence. Its gauge-sector inverse acts on the stated spin-one
source. The physical contraction, additional observation kernel and all norm
and energy cross terms stay explicit. A positive physical continuum gap has
not been established in this delivery.

## Executed verification

The final verifier executed 134 uniquely named exact conditions and rejected
12 named false formulas. It passed in ordinary and optimized Python, and a
fresh copied-source directory passed in both modes with byte-identical output.
Three command-line corruptions were each rejected in both modes at their
intended errors and with exit code 1: modified receipt, changed proof bytes,
and missing proof file. Exact commands, output hashes and exit codes are in
`execution.json`; the mathematical transcript is `verification.json`.

The unchanged parent PR6 checker was replayed in ordinary and optimized Python
against its original receipt: 189 checks and 12 negative controls, with exact
output SHA-256 `8678d6b9e9c17941676ad5c038e137152841387147fe709bca489dd8086b6075`.
The selected predecessor files in the offline package are retained byte-for-byte.

The arithmetic checks cover quaternion identities and original Haar moments,
face incidence and every unmatched-edge cross-term witness for square sides
1 through 12, the two Casimir contributions, and rigorous rational upper
endpoints for every reported numerical radius. The finite cases accompany
written proofs for arbitrary exterior box and for the general loop-size formulas.
They are not a machine proof of elliptic regularity, the maximum principle,
conditional-measure identities, or the analytical error estimates.

No new Lean execution, external independent mathematical review or remote CI
run is claimed. The noted trial-section correction was repaired before this
final receipt and has a dedicated exact rejection control.

## Publication

Parent PR6 was re-read and remains open at
`e98b2c3af77f66fb1c1396143ca53daef586404f` on
`research/20260914-coupled-response`. This delivery is an additive patch against
that exact parent, with a replacement of its current-checkpoint pointer.
Historical proof files, verification receipts and repository-wide catalogues
are unchanged.

No remote write or new PR occurred in this session. Discovery returned the
installed GitHub integration's 48 read/search actions, with no create/update
or PR-write action, and no authenticated gh command was available locally.
The review patch, complete sources and proposed PR description are delivered
for publication without an invented remote branch, commit or PR number.
