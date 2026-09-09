# What this workbench is investigating

This is a collection of mathematical research programmes, not one finished proof. The papers contain the definitions and arguments; this page explains the purpose of each programme, what the released material contains, and where its results stop. The [machine-readable catalogue](workbench.json) identifies exact public file versions.

## Yang–Mills: from explicit interacting models to continuum questions

The investigation starts from specified finite-volume and regulated interacting systems and asks which state maps, spectral estimates and coarse-graining constructions persist when volume and spatial resolution change. The reason for keeping the parameters and nonlinear terms is that a result for an oscillator or a fixed box does not on its own settle the corresponding interacting continuum question.

The current collection has five readers: [quantum coarse-graining (79 pages)](yang-mills/readers/quantum_coarse_graining.pdf), [interacting tensor bands (71)](yang-mills/readers/quantum_interacting_tensor_band.pdf), [non-Abelian vertices (63)](yang-mills/readers/quantum_nonabelian_vertex.pdf), [volume-uniform vacuum estimates (81)](yang-mills/readers/volume_uniform_vacuum.pdf), and [spatial-continuum maps and obstructions (129)](yang-mills/readers/spatial_continuum.pdf). The two component quantum readers preserve their earlier focused snapshots; they are not represented as rebuilt extracts of the cumulative reader.

The spatial manuscript includes corrected oscillator path rates in §26.13 and the fixed-coupling analytic-disk obstruction in §27. The former concerns the fixed-box oscillator comparison; the latter identifies a limitation of the particular global perturbative estimate examined. Neither is presented as a completed volume-uniform comparison with the simultaneous exact-lattice limit. The full interacting four-dimensional continuum/mass-gap question remains unresolved in this collection.

[Read the detailed scope and source guide](yang-mills/README.md), [browse full editable sources](yang-mills/sources/), or [use the AI reading index](yang-mills/AI_READING_INDEX.md). The [9 September edition](https://doi.org/10.5281/zenodo.22678364) preserves the selected source package and its reproducibility records. These descriptions follow the released manuscripts and guide; this navigation update is not a new proof review.

## S6: reconstructing and examining a proposed geometric construction

This programme reconstructs the supplied sphere/complex-geometry construction, makes calculations and maps explicit, and records subsequent questions involving torus degenerations and higher-rung constructions. The purpose is to make the argument inspectable and to investigate consequences without silently assuming that every global claim in the original construction has been established.

Start with [the five-page key-advances reader](s6/26_s6_key_advances_frozen_2026-09-06.pdf), then [the project guide](s6/README.md). The complete project frozen on 6 September contains the original transcription, historical annotations, subsequent workbench, topic drafts, TeX/Bib sources and exact check records. It is available in the [S6 archived edition](https://doi.org/10.5281/zenodo.22678442).

Historical reviews and later calculations retain their own dates and scope. This publication does not independently certify a global complex structure on S6, a counterexample to CDP20, or an interacting Yang–Mills mass-gap conclusion. The original annotations remain provenance; readers should consult the later workbench for subsequent calculations, not reinterpret an old review as today's theorem.

## Navier–Stokes: reconstruction and independent validation

This programme examines the supplied finite-time blowup construction with positive viscosity, zero initial velocity and smooth compactly supported forcing. Its object is to reconstruct the actual equations and correction calculations, retaining pressure, transport, nonlinear terms and forcing, and to inspect the analytical and formal steps.

The [208-page corrected reader](navier_stokes_workbench_208p.pdf) restores the actual-shear remainder and positive-production bounds, retains radial transport derivative factors, and makes the moving-plane projection explicit. [LaTeX, structured records and checks](navier-stokes/) accompany it. The [corrected 9 September edition](https://doi.org/10.5281/zenodo.22678406) preserves the earlier 162-page edition as well.

The original construction is attributed to its cited primary paper and formal repository. This is reconstruction and verification work, not a new claim of discovery; complete independent analytical and Lean validation remains unfinished. [Issue #2](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/issues/2) separately records the unresolved identification of the newest active fluid workspace. Published edition pointers do not establish the state of an uninspected active session.

## How another workbench can use this material

A participant can contribute one calculation, a review, a formalization, or an entire research programme. Describe what was attempted, why that route was chosen, what actually happened, and where the full argument can be found. Preserve original objects, coordinates, constants, signs, hypotheses, domains and codomains. When relating presentations, give the exact map and derivation rather than deleting terms or inferring unrelatedness from nonidentity.

Reuse can produce a check during further research: record which statement and version were examined, by which method, with what evidence and exclusions. Merely adopting a result is a dependency, not a verification event. See [the check-record guide](REVIEW_GUIDE.md) and [contribution instructions](CONTRIBUTING.md).

The [PolyClank design](docs/polyclank/) describes how independently maintained workbenches could exchange records and preserve concurrent research. This repository currently implements a static public catalogue, not live discovery, signed peer checkpoints or automatic model jobs. The [research log](RESEARCH_LOG.md) records what the organizational passes did. It leaves the next mathematical direction to the next researcher.

[All topic readers](README.md) · [Exact release correspondence](releases/2026-09-09/) · [Earlier filenames and editions](ARCHIVE.md)
