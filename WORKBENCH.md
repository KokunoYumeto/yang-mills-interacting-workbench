# Start here: research programmes and complete sources

This workbench makes the Yang–Mills, S6 and Navier–Stokes programmes readable and reusable. Each programme retains its complete mathematical source, its reasons for pursuing the construction, and its recorded results. The reading map gives access to that work at the scale of a whole programme as well as an individual calculation.

**Current map: 9 September 2026.** The [machine inventory](workbench.json) identifies all 284 files in source revision [e0a04c0](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/e0a04c078eaf0209e40b3d47d6f6dffb3f2a3e7f). The [earlier 22-file inventory](releases/2026-09-09/workbench_ed8cb4b.json) remains available with its original version pin. New navigation documents are outside that frozen source inventory; their versions are recorded by Git.

## Where to read

| Programme | Current reader | Complete source and context |
| --- | --- | --- |
| Quantum state and spectral maps | [79-page reader](yang-mills/readers/quantum_coarse_graining.pdf) | [Yang–Mills source index](yang-mills/AI_READING_INDEX.md), including the 71-page tensor-band and 63-page non-Abelian-vertex component snapshots linked in the [topic guide](yang-mills/README.md) |
| Volume-independent vacuum estimates | [81-page reader](yang-mills/readers/volume_uniform_vacuum.pdf) | [Full estimates](yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md) and the hypotheses retained in that text |
| Spatial-continuum maps and obstructions | [129-page reader](yang-mills/readers/spatial_continuum.pdf) | [Complete source](yang-mills/sources/ym_spatial_continuum_astra_20260908/spatial_continuum.md); the topic guide identifies the corrected Section 26.13 rates and Section 27 perturbative-disk obstruction |
| Navier–Stokes reconstruction | [Corrected 208-page reader](navier-stokes/navier_stokes_workbench_208p.pdf) | [Programme history and source map](navier-stokes/RESEARCH_STATE.md), [full source ZIP](navier_stokes_source_bundle.zip), and [component index](navier-stokes/research-state.json) |
| S6 topology and related constructions | [Five-page orientation](s6/26_s6_key_advances_frozen_2026-09-06.pdf) | [Frozen-project guide](s6/S6_FROZEN_PROJECT_GUIDE_2026-09-09.md) and the complete 1,079-file project archive at [Zenodo](https://doi.org/10.5281/zenodo.22678442) |

The Yang–Mills programme studies explicit interacting systems, their quantum and spectral maps, and estimates needed for changes of scale, volume and regulator. The complete texts specify what the calculations establish. The interacting four-dimensional continuum and mass-gap endpoint remains unfinished. Earlier reader editions and focused calculations remain findable through [the archive guide](ARCHIVE.md).

The Navier–Stokes programme began with proposed transfers from algebraic and S6-related constructions. The released fluid manuscript supplied an explicit construction to reconstruct. Its [current research state](navier-stokes/RESEARCH_STATE.md) records the resulting work, corrections and unfinished independent validation. The S6 archive preserves its own frozen history and provenance. A link between programmes records a research connection; each mathematical map and its exact hypotheses must be read in the associated source.

## What was tried, why, and where it was left

Read [the research log](RESEARCH_LOG.md) and the relevant full source. A useful record explains the intended calculation, why that route was chosen, the actual outcome, and the exact text or check supporting it. It can describe a large system, an unsuccessful approach, an exposition, a literature connection or a small calculation. Future participants choose their own direction; a descriptive record does not require them to inherit a task queue.

The inventory provides stable artifact identifiers separately from content hashes. The Navier–Stokes index additionally locates 13 complete source components in a 120-member source archive. These are source-body identifiers, not an exhaustive theorem inventory. This integration checked file identities and archive members; it did not add a mathematical review or run the recorded mathematical checks again.

SHA-256 values identify raw Git objects or the named archived bytes. Windows checkout newline conversion can change a text file's on-disk hash without changing its published Git blob. Compare the pinned objects when checking an edition.

## Reuse and independent checking

Use [the review guide](REVIEW_GUIDE.md) to attach a check to the source version and step actually examined while doing mathematics. Preserve the original objects, coordinates, constants, signs, orientations, hypotheses, domains and codomains. Prove the map used for a transfer, including its stated domain and inverse when an inverse is claimed. A failed candidate map establishes that obstruction; it does not establish that two programmes are unrelated.

A check of one calculation earns a record for that calculation. Check counts and hashes are not a truth score. Full derivations, actual execution receipts and explicit correction histories let another workbench assess and reuse the work.

## PolyClank: independently maintained workbenches

[The PolyClank documents](docs/polyclank/README.md) describe a host-neutral discovery and exchange proposal. Each workbench maintains its own research, versions and judgment. GitHub is one transport for the files. Replicated discovery, independent expositions, literature contributions and multilingual access can help workbenches find one another without a central mathematical authority.

This repository currently provides documentation and static indexes. It does not deploy a federation, run automatic peer discovery, or contain an imported 7,000-problem catalogue. The [related zeta reader](https://github.com/KokunoYumeto/zeta-function-research-reader/tree/cf3c5f9dd58524ad2f911a2ecccaff994c3f4f97) is a versioned reading connection, not an independent review of these results.

Collective and pseudonymous contributions are welcome. Preserve source authorship and the actual human, model and tool provenance of a contribution. Criticism should address the mathematical statement, calculation or evidence.

The current Navier–Stokes edition is publicly archived at [10.5281/zenodo.22678406](https://doi.org/10.5281/zenodo.22678406). Independent full validation remains unfinished, and this work makes no prize or discovery-priority claim. Recurring Navier–Stokes mirror work is paused after this publication update at the owner's request.
