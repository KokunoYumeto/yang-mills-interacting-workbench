# Yang–Mills, S6 and Navier–Stokes research

Readable mathematical papers, their sources, and reproducibility records. Choose a topic below. The linked Zenodo editions preserve their stated dates; later GitHub continuations are identified separately and are not yet included in those archival records.

[What we tried and what the programmes contain](WORKBENCH.md) · [Contribute or publish a scoped check](CONTRIBUTING.md) · [Machine-readable catalogue](workbench.json) · [PolyClank design](docs/polyclank/)

## Yang–Mills: vacuum, energy and physical excitations

The **[19 September continuation: sixth source, eighth energy and plaquette response](yang-mills/consolidation/20260919/)** adds the complete supplied mathematical notes and exact arithmetic checks. It gives the displayed eighth-energy boundary polynomial, a finite 240-face response estimate, and explicit minimum-energy maps for changing the observed face support. The new spatial tables and final cumulative execution package were not delivered: their completeness is reported by the source, not independently replayed here. The continuation explains this distinction and retains the physical complement and every dimensional factor.

The Yang–Mills programme studies an interacting SU(2) gauge theory on finite cubic lattices, keeping the original gauge constraints and physical scales. The papers construct state and operator maps, calculate the interacting vacuum and its energy, and use controlled corrections to obtain spectral estimates that remain valid as the box grows. Separate manuscripts examine the additional questions involved in a continuum limit.

Start with the [fourth-order vacuum and sixth-order energy reader](yang-mills/consolidation/20260917/reader/yang_mills_quartic_cube_reader.pdf). It introduces the Hamiltonian, derives the new coefficients, explains how they enter a bound on the complete physical excitation spectrum, and includes six full proof notes. Two independent presentations are compared by an exact polynomial change of coordinates, not just numerical agreement. The result includes all finite-box boundary terms and the elementary-cube energy contribution −83/1944. The [mathematical overview](yang-mills/consolidation/20260917/) gives formulas, hypotheses, source links and reproduction instructions.

The [14–16 September reader](yang-mills/consolidation/20260916/) develops the preceding source equations, gauge-coordinate maps, cubic calculation and spectral return. The foundation papers below cover quantum coarse-graining, interacting tensor bands, a non-Abelian vertex, volume-independent vacuum estimates, and spatial-limit maps and obstructions. Together these are a developing lattice-gauge research programme, not a claimed solution of the four-dimensional continuum mass-gap problem.

| Topic | Start reading | Sources and scope | Archived edition |
| --- | --- | --- | --- |
| Yang–Mills | [Vacuum, energy and spectral return](yang-mills/consolidation/20260917/reader/yang_mills_quartic_cube_reader.pdf) | [Reading guide, full proofs and calculations](yang-mills/) | [9 September archive](https://doi.org/10.5281/zenodo.22678364); 17 September archival upload pending |
| S6 topology and related constructions | [Key advances — 5 pages](s6/26_s6_key_advances_frozen_2026-09-06.pdf) | [Full frozen project, standalone papers and calculations](s6/) | [10.5281/zenodo.22678442](https://doi.org/10.5281/zenodo.22678442) |
| Navier–Stokes | [Corrected reconstruction — 208 pages](navier_stokes_workbench_208p.pdf); [vacuum-hydrodynamics continuation](navier-stokes/continuations/20260919-vacuum-hydrodynamics/) | [Standalone LaTeX, new manuscripts, structured proofs and checks](navier-stokes/) | [9 September archive](https://doi.org/10.5281/zenodo.22678406) |

The Yang–Mills foundation companions cover interacting tensor-band calculations (71 pages), a non-Abelian vertex (63 pages), volume-independent vacuum estimates (81 pages), and spatial-continuum maps and obstructions (129 pages). The two focused quantum readers retain their original component snapshots; their matching sources are supplied.

The S6 package preserves the complete public project frozen on **6 September 2026**, including the original transcription, historical annotations, later calculations, standalone drafts and mathematical provenance. The corrected Navier–Stokes package and Yang–Mills foundation packet are **9 September 2026** editions; dated GitHub continuations now include the **19 September 2026** intake. Dates and provenance matter: older reviews are not silently relabelled as present conclusions.

These are AI-assisted research and reconstruction records. The full proofs and qualifications are in the papers. They do not constitute a claimed solution of the interacting four-dimensional Yang–Mills mass-gap problem or independent certification of every global step in the supplied S6 or Navier–Stokes constructions.

## Navier–Stokes and gravitational response

The source paper is available directly in this workbench as a [complete editable LaTeX reconstruction, checked 166-page PDF and source ZIP](navier-stokes/sources/openai-source-faithful-20260920/), also archived on [Zenodo](https://doi.org/10.5281/zenodo.22852310). The complete pinned release, including figures and verification records, is preserved unchanged. It is separate from this workbench's 208-page analytical reader; [source identity and transcription-check scope](navier-stokes/SOURCE_READING_20260920.json) are recorded explicitly.

An [Everyday English working comparison](navier-stokes/README.md#everyday-english-a-working-comparison) pairs a paragraph from page 3 with its current rewritten version. It is a visible draft example, not a completed translation.

The **[19 September vacuum-hydrodynamics continuation](navier-stokes/continuations/20260919-vacuum-hydrodynamics/)** recovers two complementary manuscripts and their mathematical predecessors. The first constructs exact nonlinear Einstein initial data from any compact smooth divergence-free velocity field, with an explicit left inverse recovering the whole velocity. The second calculates the linear shear response of a Rindler cutoff through a Bessel boundary problem. It derives the hydrodynamic coefficients and explains how two individually divergent modal residues combine into a finite response at a pole collision. A companion gives the positive slab-stress construction and the regularity proof for its modified fluid equation.

These results have explicit domains and comparison maps: the Einstein initial-data encoding is not an identification of fluid time with Einstein evolution, and the finite modal cancellation is not a cancellation of nonlinear Navier–Stokes blowup. The reader retains the full equations, proofs, literature references and numerical status. The two recovered source manuscripts are unchanged; fresh compact checks accompany them. Their connection to the existing Navier–Stokes work is described result by result, without assigning them an unproved S6 interpretation.

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
