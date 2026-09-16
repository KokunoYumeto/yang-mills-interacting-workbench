# Yang–Mills mathematical sources and readers

## Current continuation: 14–16 September 2026

Read the [complete web-session consolidation](consolidation/20260916/), its [cumulative PDF](consolidation/20260916/reader/yang_mills_web_continuation.pdf), or the [editable TeX](consolidation/20260916/reader/yang_mills_web_continuation.tex). The edition integrates the actual-loop, uniform-gap, gauge-native, local-fibre, cubic-source and linearized-return proofs with their complete available dependencies and scoped verification records. The [current mathematical state](consolidation/20260916/CURRENT_RESEARCH.md) keeps the finite-lattice gap domain, fixed-spacing volume-limit domain and remaining continuum questions explicit.

The [coverage and provenance](consolidation/20260916/SOURCE_COVERAGE.md) identify the exact archive and Git sources; the [fresh validation record](consolidation/20260916/VALIDATION.md) distinguishes executed finite checks from bounded proof reviews. Earlier source and execution records retain their original historical status. This continuation is a GitHub edition; the DOI below identifies the earlier 9 September archive.

## Foundation edition: 9 September 2026

[What the quantum, interaction, volume and spatial-limit tasks tried—and why](../ATTEMPTS.md#ym-attempts)

This edition collects the supplied current quantum coarse-graining, volume-uniform actual-vacuum, spatial-continuum, and related finite-box mathematical proofs. It supplements the existing Yang-Mills collection, whose previous editions and complete historical workbench remain part of the publication history. This ZIP is an explicitly selected current-source edition, not a replacement for the entire historical workbench.

## Read the manuscripts

| Reader | Pages | TeX source |
| --- | ---: | --- |
| [quantum_coarse_graining.pdf](https://zenodo.org/records/22678364/files/quantum_coarse_graining.pdf) | 79 | [extensive_quantum_blocking.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/extensive_quantum_blocking.tex) |
| [quantum_interacting_tensor_band.pdf](https://zenodo.org/records/22678364/files/quantum_interacting_tensor_band.pdf) | 71 | [extensive_quantum_blocking.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/interacting_band_publication_20260909/extensive_quantum_blocking.tex) |
| [quantum_nonabelian_vertex.pdf](https://zenodo.org/records/22678364/files/quantum_nonabelian_vertex.pdf) | 63 | [extensive_quantum_blocking.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/nonabelian_vertex_publication_20260909/extensive_quantum_blocking.tex) |
| [volume_uniform_vacuum.pdf](https://zenodo.org/records/22678364/files/volume_uniform_vacuum.pdf) | 81 | [VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.tex) |
| [spatial_continuum.pdf](https://zenodo.org/records/22678364/files/spatial_continuum.pdf) | 129 | [spatial_continuum.tex](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_spatial_continuum_astra_20260908/spatial_continuum.tex) |

The quantum reader is cumulative. Its interacting tensor and nonabelian vertex readers retain their separate supplied component snapshots and corresponding sources; they are earlier focused editions, not newly rebuilt components of the cumulative reader. Markdown counterparts preserve the full mathematical text for searching and AI ingestion. The current spatial manuscript includes the fixed-coupling analytic-disk obstruction in Section 27 and the corrected Section 26.13 oscillator path rates. The volume manuscript retains its current covariance-window estimates.

This edition: [10.5281/zenodo.22678364](https://doi.org/10.5281/zenodo.22678364). Repository: [Yang-Mills collection](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/yang-mills), with separate [Navier-Stokes](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/navier-stokes) and [S6](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/s6) collections.

The original finite-box objects, coefficients, domains and hypotheses are stated in the included proofs. The oscillator path rates are fixed-box/oscillator consequences: a volume-uniform comparison with the simultaneous exact-lattice limit is not established. The fixed-coupling disk result identifies the limitation of a particular global perturbative bound. These results do not establish or refute the interacting four-dimensional continuum Yang-Mills mass gap.

## Sources and reproducibility

`sources/` preserves the selected files' original names and local dependency hierarchy. Each quantum component is retained in its own original snapshot directory. `AI_READING_INDEX.md` links the complete Markdown and TeX bodies. Bibliographic entries remain in the manuscripts; no downloaded literature corpus is redistributed. `DEPENDENCIES.json` records resolved literal TeX inputs. `READER_PROVENANCE.json` records page counts and exact PDF/TeX/Markdown hashes. `SOURCE_MANIFEST.json` gives the byte count and SHA-256 of each archived file other than the manifest itself. It contains only archive-relative paths.

The PDFs are supplied artifacts copied byte-for-byte into this archive. The packaging worker did not rebuild them or rerun mathematical checkers. The publication coordinator regenerated the volume reader after correcting a single TeX inline-math closing delimiter to match the already correct Markdown; the mathematical source content was unchanged. Included checker programs and recorded results are finite symbolic, arithmetic or numerical diagnostics within their stated scope. Packaging integrity and dependency checks are not formal verification of the analytical proofs. To compile an included TeX manuscript, run a LaTeX distribution from its containing directory; dependencies identified by literal input commands are supplied. The Markdown-to-TeX conversion intermediate `markdown_source.tex` is included for the current quantum manuscript. Python checkers require their stated imports, including SymPy, NumPy, SciPy and mpmath where used, and should be run from their containing directory. Original sibling lane names are retained so relative cross-lane paths resolve. One recorded result's absolute source locator is replaced by its portable relative path; its mathematical data and cited input hash are retained.

`OMISSIONS.json` records exclusions from the historical allowlist. Private task records, user transcripts, feedback, credentials, copied literature bodies, separate S6 and Navier-Stokes source collections, and the uncertified full-L2 tensor contraction calculation/report are excluded. No mathematical claim is made for that excluded exploratory calculation.
