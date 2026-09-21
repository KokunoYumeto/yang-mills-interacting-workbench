# Split Zero smooth-continuum continuation

14 September 2026 · additive Yang–Mills workbench contribution

## Read and reproduce

[RESEARCH_NOTE.md](RESEARCH_NOTE.md) contains the full coordinate definitions and proofs. [sources.json](sources.json) records the exact source paths, retrieval date, pinned Zeta revision, and S6 retrieval scope.

From the repository root, run:

```sh
python3 yang-mills/continuations/20260914-splitzero-smooth-continuum/verify.py
```

The standard-library checker uses exact rational arithmetic, sparse polynomial differentiation and finite formal series. Its report records **76 passed assertions across 26 check families**. The declared finite matrices test the Schur identities; they are not computed Yang–Mills spectra.

[prior_certificate_replay.json](prior_certificate_replay.json) records a byte-identical replay of the supplied previous 112-block cubic certificate. The previous certificate and script remain unchanged.

## Completed connected results

The sequence is `a_n=a_0*2^(-n)`, `L_n=4*2^(2n)`, and `g_n^2=1/(g_0^(-2)+beta*n*log(2))`, for fixed positive displayed parameters. The work retains the original full SU(2) Hamiltonian and physical units.

- Sections 1–3 give exact ordered refinement, the complete kinetic/potential/vacuum-energy defect, smooth holonomy derivatives, the flat-germ kernel, and a full non-Abelian magnetic remainder that tends to zero along the displayed sequence. Its leading magnetic growth remains explicit.
- Sections 4–5 give uniform positive-time correlation and Schur-memory bounds, an exact zero-time loop-energy matrix, and the restored raw Gram derivative.
- Sections 6–8 give one simultaneous subsequence for a countable separating observable supply and a countable positive-time supply of Schur memories, smooth positive-time limits, retained energy-endpoint atoms, a literal Split Zero infinity-boundary complex, and the positive-generator Hilbert reconstruction.

The inequalities quantify ultraviolet tails at positive time. The endpoint matrices and finite-energy-window measures remain exact defined data. No positive continuum mass lower bound or nontrivial four-dimensional quantum field theory is established by this contribution.

## S6 and publication scope

The S6 reader and theorem locator were retrieved. Fetches of the linked proof bodies failed. The smooth-germ and holonomy proofs here are independently written from the retrieved Yang–Mills operator and transport formulas; an unexamined S6 theorem is not used.

This contribution was prepared locally. No remote repository write or pull request was performed. The accompanying patch adds this directory without replacing existing workbench files. Patch application was exercised in a fresh local test tree; remote HEAD compatibility was not tested.
