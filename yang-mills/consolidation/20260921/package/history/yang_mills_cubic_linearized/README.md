# Two executed Yang–Mills calculations, 16 September 2026

The full connected cubic vacuum source and the complete linearized residual are in
`yang-mills/continuations/20260916-cubic-linearized/CUBIC_SOURCE.md` and
`LINEARIZED_RETURN.md`. The complete uncompressed verification record accompanies them.

From that directory, replay:

    python -B verify.py --verify-receipt verification.json
    python -O -B verify.py --verify-receipt verification.json

The GitHub source-only form reconstructs the identical complete record with
`python -B materialize_receipt.py`; this ZIP already supplies it.
The checker has 2246 named finite checks and 15 false-formula controls. Written
analytic proofs, exact finite tests, and independent/formal proof review retain
the distinct scopes stated in the notes.

Publication: draft PR8 at commit91434b6962062bd80439d4cb2cae9d2479264dde,
stacked on PR6. No merge was performed. `delivery/` records the exact publication
and tested patch against the PR6 parent. The patch adds14 source files and updates
only the mathematical checkpoint. Earlier unpublished owner-facing archives are
not silently included as part of that Git ancestry.

The full physical finite-lattice lower bound is proved on its explicit strong-
coupling domain. A nontrivial four-dimensional continuum field and finite positive
continuum mass remain unestablished. The stated literature comparison proves
parameter/equation correspondences, without assigning global priority.
