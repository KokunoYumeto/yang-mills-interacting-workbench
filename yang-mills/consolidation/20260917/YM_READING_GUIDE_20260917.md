# Reading the Yang–Mills collection

This collection investigates the interacting vacuum, energy and excitation spectrum of an SU(2) lattice gauge theory, and the mathematical maps needed to compare its states and operators across scales. The starting objects are finite cubic lattices with their actual gauge constraints, Haar measure and physical coupling constants. Some estimates hold uniformly as the lattice box grows. Passing to a nontrivial four-dimensional continuum theory is a distinct question, examined in the spatial-limit papers but not settled by the finite-lattice results.

## A route through the mathematics

Begin with **Fourth-order vacuum sources and sixth-order energy in cubic SU(2) lattice Yang–Mills theory**, the 49-page `yang_mills_quartic_cube_reader.pdf`. Its introduction defines the Hamiltonian and the logarithmic-vacuum equation, derives the common fourth-source and sixth-energy results, and explains how the two independently developed calculations fit together. Six complete proof notes follow. The latest PDF is the default preview of this Zenodo edition; its companion TeX can be compiled independently.

The fourth coefficient is calculated in both trace words and explicit quaternion coordinates. Their equality is established for the complete polynomials in all 78 connected geometric classes, representing 8,621 anchored face multisets. This is a concrete change of coordinates, not an identification based on appearance. The second presentation also calculates the signed response to the individual plaquette couplings.

The sixth ground-energy coefficient includes the face, adjacent-pair, three-face and elementary-cube contributions, with all open-boundary counts retained. In particular, the cube contributes −83/1944. A controlled correction beyond the fourth logarithmic-vacuum coefficient returns to the original Hamiltonian and gives a uniform finite-box bound on the complete physical excitation spectrum. The proof states the coupling interval and all auxiliary estimates. Two energy-remainder proofs have different domains and are both retained, with their different uses explained.

For the preceding development, read **Source equations, gauge coordinates and spectral return**, `yang_mills_web_continuation.pdf` (297 pages). It collects the 14–16 September continuation, including the actual-loop constructions, gauge-native dependencies, local-fibre maps, cubic source and linearized return. Its complete source bundle is `yang_mills_complete_available_sources_20260916.zip`.

## Broader foundation papers

The foundation readers provide several ways into the programme:

| Mathematical subject | Reader |
| --- | --- |
| Quantum states, operator maps and coarse-graining | `quantum_coarse_graining.pdf` — 79 pages |
| Interacting tensor-band calculation | `quantum_interacting_tensor_band.pdf` — 71 pages |
| Non-Abelian vertex calculation | `quantum_nonabelian_vertex.pdf` — 63 pages |
| Volume-independent estimates for the actual vacuum | `volume_uniform_vacuum.pdf` — 81 pages |
| Spatial-continuum maps, proposed limiting paths and obstructions to available estimates | `spatial_continuum.pdf` — 129 pages |

These papers retain their original source dates. A focused component reader is not necessarily a later version of the cumulative quantum reader. The older numbered PDFs and full Overleaf archive are historical editions; their continued inclusion preserves earlier arguments and links, not a claim that every historical statement is current.

## Proofs, calculations and checking

`yang_mills_quartic_comparison_sources_20260917.zip` supplies the two new mathematical packages, the exact cubic dependency, the reader sources and the new comparison and verification programs. Extract it while retaining its directory structure. Start with `yang-mills/consolidation/20260917/README.md`; `VALIDATION.md` explains the mathematical checks and provides replay commands. It distinguishes finite polynomial equalities and exact arithmetic from the convergence and spectral arguments in the proofs. The PDF is an exposition with full proof notes, not a printout of all polynomial tables.

Fresh replays reproduce both coefficient calculations, the signed tangent certificate and the complete change-of-coordinates comparison. An additional exact calculation checks the cube term and open-box counts. These records make the finite computations reproducible. They are not represented as a new Lean formalization or independent certification of every analytical result in the historical collection.

The source archive omits private conversational input. Its identity is retained in the provenance record, while the public replay explicitly reports that omission. The mathematical inputs, coefficients and proofs needed by the published calculation remain available. Original source files and their historical receipts are distinguished from later explanatory and verification material.

## Continuing the work

The [living Yang–Mills GitHub collection](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/tree/main/yang-mills) belongs to PolyClank, an open human–AI mathematical collaboration, including work with ChatGPT 5.6 Sol and GPT-6 Astra. To participate, fork the repository, add your result or calculation with a readable argument and reproducible evidence where relevant, and submit a pull request. The [contribution guide](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/CONTRIBUTING.md) explains the process. The scope of a contribution is determined by its mathematics, not by a prescribed list of allowable discoveries.

The [17 September archived edition](https://doi.org/10.5281/zenodo.22803564) preserves this collection. Related [S6](https://doi.org/10.5281/zenodo.22678442) and [Navier–Stokes](https://doi.org/10.5281/zenodo.22678406) research has separate archival records. The manuscripts retain the relevant literature citations and attribution.
