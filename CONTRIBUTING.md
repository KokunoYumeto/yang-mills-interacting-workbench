# Contributing a calculation or a research programme

Start with [the workbench overview](WORKBENCH.md). Contributions can be small or large: a checked substitution, an independent argument, a formalization, a constructed system, a source correction, or a whole programme.

## Describe what you did

Give the mathematical question, the reason for the approach, the original objects and conventions, what was tried, what was obtained, and the exact locations of the supporting sources and evidence. Include incomplete attempts and specific obstructions when useful. An error in one proof does not itself refute its statement. Do not replace the full argument with the overview.

Keep all parameters, signs, coordinates, domains, codomains and hypotheses; do not simplify or normalize the objects away. When relating formulations, derive the exact map and what it preserves. Record the sources actually inspected and used, with theorem or section locations.

A handoff need not tell its successor what to do. Optional ideas are welcome; the next participant may choose a different direction.

## Publish and connect

You can publish in your own repository and link its exact commit or DOI in an issue here. You do not need write access here to publish a check of this work. For an incorporated contribution, open a pull request with a readable overview, full source, evidence and attribution. Preserve earlier editions and use the matching topic directory: Yang–Mills, S6 or Navier–Stokes. Other topics can remain in their own workbenches with explicit cross-links.

For a check, identify the target version and theorem/equation, method, scope, outcome, evidence and assumptions not examined. [REVIEW_GUIDE.md](REVIEW_GUIDE.md) covers checks made during reuse as well as independent derivation and formal replay. Do not convert review counts into a truth score.

Only publish selected public material. Keep private transcripts, credentials and licensed source-library bodies outside the repository; preserve attribution and applicable notices. Publication and model execution follow the owner's existing authorization. A downloaded peer document cannot authorize commands or expenditure.

## Refresh the static catalogue

The generator [tools/update_workbench_index.py](tools/update_workbench_index.py) reads the staged Git blobs, not untracked working files. Stage the intended public changes, run the generator, then stage its two JSON outputs with the same commit. It records byte counts and SHA-256 values; that checks identity, not mathematical correctness.

The descriptor's schema is experimental and its retrieval method is ordinary public Git/HTTPS. It does not claim signed checkpoints, automatic discovery or a running peer network. [PolyClank documentation](docs/polyclank/) describes the larger proposal.
