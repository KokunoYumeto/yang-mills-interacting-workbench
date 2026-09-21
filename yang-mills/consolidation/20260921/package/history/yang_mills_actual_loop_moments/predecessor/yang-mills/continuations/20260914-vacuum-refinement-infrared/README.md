# Vacuum refinement and the infrared Schur budget

Full proofs and source locations: [RESEARCH_NOTE.md](RESEARCH_NOTE.md). Research account: [ATTEMPTS.md](ATTEMPTS.md).

This continuation adds smooth finite-link holonomy sections with their exact curvature cost, an interacting-vacuum conditional-refinement identity, a projective equal-time limit, uniform infrared Schur-memory bounds, and the complete comparison kernel for regulator-state sequences. It also records three precise corrections to the spectral-reconstruction continuation: the spectral supremum, the matrix imaginary part, and escaping-label detection.

Run the exact algebraic fixtures with Python 3 and SymPy:

```sh
python verify.py --output verification.json
```

The checker covers declared rational and symbolic fixtures. The analytic proofs are written in the note. No interacting Yang–Mills vacuum or continuum mass value is computed by these fixtures.
