# Observed verification and exact scope

15 September 2026.

The final `verify.py` ran successfully with **642 uniquely named exact checks** and **27 deliberate false-formula controls**. Normal and optimized executions produced byte-identical mathematical JSON. The full integer L=2 certificate retains 240 plaquettes, the original face order, the positive power vector and all fraction-free pivot determinants; every one of its 2,303,960 divisions was checked exactly.

`replay.py` completed with exit code zero. Its 28 subprocess records include the new checker in both modes, the unchanged predecessor in both modes, fresh copied-source runs, 20 intentionally corrupted CLI executions at their specified error, and both restored-source reruns. Every recorded successful execution returned zero; each expected corruption returned one and its named message. No disabled Python assertion is used.

Receipt SHA-256:

    c196c6f4fa6e786e0a16475c42c3e59d48d289e3ed0c809e731e9f51dd0470c8

Full original-box certificate SHA-256:

    97c502538c316015dfe8b56f8fa6221e7d2658bf305f90ac5f31ce6a12e17b4d

Complete execution record SHA-256:

    b492d9754adfa9ae404c4efeef6584112e8fd3a398a9ea4ff08fca22d79506fb

The initial attempt to use an interactive container execution failed at `StreamingExecNotEnabledContainerError` before the replay ran. A controlled local subprocess was then launched, its logs and completion file were read, and its successful exit was awaited within this session. This was a verification run, not scheduled or indefinite research.

## What was and was not checked

The finite verifier checks original group-index contractions, quaternion Haar integrals, full graph and Casimir counts, source recurrences, exact field arithmetic, the entire coefficient matrix, exact inertia, physical parameter identities and rational evaluation of the written bounds. It includes both the raw band Gram and the retained zero/section tests.

The new operator-domain, absolute-convergence, infinite-volume, analytic-remainder and coupling-modulus proofs are written in the four complete Markdown sources. They have not received a new independent analytical review or Lean certification. The predecessor was replayed at its unchanged receipt, not retrospectively relabelled as a new proof review. No peer CI job was rerun.

Dahmen's planar second-order coefficient was checked from the original displayed operator and diagram source with the explicit B30 parameter map. This supports the local channel arithmetic and its antecedent attribution. It is not a source for this continuation's three-dimensional uniform error or enlarged coupling range.

No sampled vacuum, finite spin cutoff, floating-point spectral certificate, paid model execution, remote publication or merge is part of this record. The complete mathematical scope and remaining continuum quantities are in `state.json`.
