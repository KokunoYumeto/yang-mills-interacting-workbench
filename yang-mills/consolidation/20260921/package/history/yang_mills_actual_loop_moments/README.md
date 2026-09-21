# Actual Yang–Mills loop moments: complete review package

The new contribution is `yang-mills/continuations/20260915-actual-loop-moments/`.
Start with its README and full research note. The package contains the proposed
current-checkpoint pointer, an additive Git patch, and the selected predecessor
source tree for offline review and replay. It is not a full repository clone.

The patch targets the inspected PR6 head
`e98b2c3af77f66fb1c1396143ca53daef586404f`. No new remote PR was opened.
`PR_DESCRIPTION.md` supplies its proposed mathematical review text. To apply in
a checkout of that parent, use `git apply --check review.patch` followed by
`git apply review.patch`. The delivery record reports a successful fresh-tree
patch application and replay. No merge or paid model execution is scripted.

To reproduce the new exact certificate from this archive's root:

```sh
python -B yang-mills/continuations/20260915-actual-loop-moments/verify.py --verify-receipt yang-mills/continuations/20260915-actual-loop-moments/verification.json
python -O -B yang-mills/continuations/20260915-actual-loop-moments/verify.py --verify-receipt yang-mills/continuations/20260915-actual-loop-moments/verification.json
```

The preserved parent can be replayed separately from the `predecessor` directory
using its existing command. Mathematical statements and executable checks keep
their separate scopes. SHA-256 values in `MANIFEST.json` identify delivered
bytes; they do not certify analytical truth.
