# Yang–Mills, S6 and Navier–Stokes research

Readable mathematical papers, their complete sources, and reproducibility records. Choose a topic below; the corresponding Zenodo edition archives the same dated papers and source packages under a permanent DOI.

[What we tried and what the programmes contain](WORKBENCH.md) · [Contribute or publish a scoped check](CONTRIBUTING.md) · [Machine-readable catalogue](workbench.json) · [PolyClank design](docs/polyclank/)

## Yang–Mills: vacuum, energy and physical excitations

The Yang–Mills programme studies an interacting SU(2) gauge theory on finite cubic lattices, keeping the original gauge constraints and physical scales. The papers construct state and operator maps, calculate the interacting vacuum and its energy, and use controlled corrections to obtain spectral estimates that remain valid as the box grows. Separate manuscripts examine the additional questions involved in a continuum limit.

Start with the [fourth-order vacuum and sixth-order energy reader](yang-mills/consolidation/20260917/reader/yang_mills_quartic_cube_reader.pdf). It introduces the Hamiltonian, derives the new coefficients, explains how they enter a bound on the complete physical excitation spectrum, and includes six full proof notes. Two independent presentations are compared by an exact polynomial change of coordinates, not just numerical agreement. The result includes all finite-box boundary terms and the elementary-cube energy contribution −83/1944. The [mathematical overview](yang-mills/consolidation/20260917/) gives formulas, hypotheses, source links and reproduction instructions.

The [14–16 September reader](yang-mills/consolidation/20260916/) develops the preceding source equations, gauge-coordinate maps, cubic calculation and spectral return. The foundation papers below cover quantum coarse-graining, interacting tensor bands, a non-Abelian vertex, volume-independent vacuum estimates, and spatial-limit maps and obstructions. Together these are a developing lattice-gauge research programme, not a claimed solution of the four-dimensional continuum mass-gap problem.

| Topic | Start reading | Sources and scope | Archived edition |
| --- | --- | --- | --- |
| Yang–Mills | [Vacuum, energy and spectral return](yang-mills/consolidation/20260917/reader/yang_mills_quartic_cube_reader.pdf) | [Reading guide, full proofs and calculations](yang-mills/) | [17 September edition](https://doi.org/10.5281/zenodo.22803564) |
| S6 topology and related constructions | [Key advances — 5 pages](s6/26_s6_key_advances_frozen_2026-09-06.pdf) | [Full frozen project, standalone papers and calculations](s6/) | [10.5281/zenodo.22678442](https://doi.org/10.5281/zenodo.22678442) |
| Navier–Stokes | [Corrected reconstruction — 208 pages](navier_stokes_workbench_208p.pdf) | [Standalone LaTeX, structured proofs and checks](navier-stokes/) | [10.5281/zenodo.22678406](https://doi.org/10.5281/zenodo.22678406) |

The Yang–Mills foundation companions cover interacting tensor-band calculations (71 pages), a non-Abelian vertex (63 pages), volume-independent vacuum estimates (81 pages), and spatial-continuum maps and obstructions (129 pages). The two focused quantum readers retain their original component snapshots; their matching sources are supplied.

The S6 package preserves the complete public project frozen on **6 September 2026**, including the original transcription, historical annotations, later calculations, standalone drafts and mathematical provenance. The corrected Navier–Stokes package and Yang–Mills foundation packet are **9 September 2026** editions; the Yang–Mills continuation now runs through **17 September 2026**. Dates and provenance matter: older reviews are not silently relabelled as present conclusions.

These are AI-assisted research and reconstruction records. The full proofs and qualifications are in the papers. They do not constitute a claimed solution of the interacting four-dimensional Yang–Mills mass-gap problem or independent certification of every global step in the supplied S6 or Navier–Stokes constructions.

## Download or inspect

- [What we tried and why](ATTEMPTS.md): concise accounts of approaches, results, limited successes and unfinished work, with their broader motivations retained.

- [All three topic directories](.): readable readers and source links; the complete S6 archive is linked from its topic guide because it exceeds ordinary repository-file limits.
- [Yang–Mills editable sources](yang-mills/sources/) and [AI reading index](yang-mills/AI_READING_INDEX.md): full mathematical text, not a replacement summary.
- [Release manifests](releases/2026-09-09/): exact file sizes, SHA-256 values and GitHub–Zenodo correspondence.
- [Earlier filenames and editions](ARCHIVE.md): preserved for existing links and reproducibility.
- [Live Overleaf workbench](https://www.overleaf.com/read/rtmyqxyrzprn#fa24eb): evolving workspace; it may contain work later than these archived editions.

Each topic retains its own Zenodo publication family and prior versions. The older mixed full-Overleaf archive remains available in the [historical Yang–Mills edition](https://doi.org/10.5281/zenodo.22667605); subsequent manuscripts are dated continuations, not a relabelling of that older full-project snapshot. Existing public files are retained.

## Participate in PolyClank

This is an open, AI-assisted mathematical workbench, including work with ChatGPT 5.6 Sol and GPT-6 Astra. To contribute, fork this repository, add your argument or reproducible calculation with a readable explanation, and open a pull request. The [contribution guide](CONTRIBUTING.md) explains how to submit and discuss the work. Contributions are assessed on their mathematics; the code and receipts accompany the proofs rather than replacing exposition.
