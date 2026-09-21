# Reproduce the complete finite record

This Git contribution exposes both complete proofs and all four producer/replay
programs in ordinary text. The full 180,403-byte `verification.json` is reproduced
locally with its already observed SHA-256 required exactly:

```sh
python -B materialize_receipt.py
python -B verify.py --verify-receipt verification.json
python -O -B verify.py --verify-receipt verification.json
```

Run these commands from this directory. The first command checks every original
source identity before execution, runs the entire producer, verifies the exact
full-output hash, and writes that unchanged complete record. It refuses to replace
an existing different receipt. The owner-facing ZIP also contains the original
uncompressed full record. No record field is omitted from the reconstructed file.

Expected complete SHA-256:
`2e6a1433b9df7bb3f1ee584b7896e6ae9dae9f5a7836a5030af7a993711190c6`.

The producer executes 2,246 named exact checks and 15 false-formula controls.
`execution.json` is the observed 16-run record: ordinary/optimized executions,
the unchanged saved predecessor, copied sources, eight intended CLI corruption
rejections, and restored sources. Those analytical claims have written proofs;
finite checks are not an independent analytical or Lean certification.

`replay.py` reruns the current/copy/corruption sequence. Its optional `--parent`
argument replays the saved gauge-native predecessor and complete L2 certificate;
that earlier owner-facing archive is not silently represented as published by
this focused PR. Current replay:

```sh
python -B replay.py
```

The existing `README.md` and all eight inputs bound by the mathematical record
are preserved byte-for-byte from the completed local verification. This setup
page adds no changed mathematical premise or expected value.
