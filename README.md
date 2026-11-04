# Yang–Mills, S6 and Navier–Stokes: an AI-produced mathematical research workbench

A research workbench with three AI-produced mathematical programmes: interacting SU(2) lattice Yang–Mills theory
(the vacuum, ground energies, physical excitation spectra and coarse-graining maps on finite cubic lattices, with
separate manuscripts on continuum questions); the S6 programme (calculations built on the complex-threefold
construction on the six-sphere circulated by Levent Alpöge); and Navier–Stokes (a corrected 208-page reconstruction
of the finite-time blowup construction and later continuations). It holds the papers with complete LaTeX proofs,
reproducible computations, check records and an account of what was tried.

## How it was made

The research is AI-produced, by OpenAI models GPT-5.6 Sol and GPT-6 Astra, in an open human–AI collaboration
([PolyClank](docs/polyclank/)). The written analytic arguments and the executed finite checks have separate, stated
scopes, and each continuation records which proofs were supplied and which checks were replayed. The originating
constructions by Levent Alpöge and the other sources are credited at their point of use ([ATTRIBUTION.md](ATTRIBUTION.md)).

## Status

Research in progress; the repository was last updated on 16 October 2026. The Yang–Mills papers are a developing
lattice-gauge research programme, not a claimed solution of the four-dimensional continuum mass-gap problem. The
Navier–Stokes material is a reconstruction with continuations, not an independent certification of every global step
of the construction; the infinite modified trajectory and a complete independent global validation remain
unfinished. For the S6 construction, see the [5 October status note](s6/STATUS_2026-10-05.md). Errors may remain.

## Contents and where to start

- [WORKBENCH.md](WORKBENCH.md): what each programme investigates, what the released material contains and where its
  results stop; [ATTEMPTS.md](ATTEMPTS.md): what was tried, why, and how far it got; [RESEARCH_LOG.md](RESEARCH_LOG.md).
- **Yang–Mills.** [yang-mills/README.md](yang-mills/README.md) is the reading guide to the full proofs and editable
  LaTeX; [yang-mills/AI_READING_INDEX.md](yang-mills/AI_READING_INDEX.md) indexes every continuation. Start with the
  [fourth-order vacuum and sixth-order energy reader](yang-mills/consolidation/20260917/reader/yang_mills_quartic_cube_reader.pdf).
  Later work: the [21 September heat and volume edition](yang-mills/consolidation/20260921/), the
  [fifth-reference continuation](yang-mills/consolidation/20260921-fifth-reference/), the
  [30 September S6-reduced triality-to-profile continuation](yang-mills/continuations/20260930-s6-ns-moment-map-bridge/)
  and the dated October continuations in [yang-mills/continuations](yang-mills/continuations/). The foundation
  readers: [quantum coarse-graining (79 pages)](yang-mills/readers/quantum_coarse_graining.pdf),
  [interacting tensor bands (71)](yang-mills/readers/quantum_interacting_tensor_band.pdf),
  [non-Abelian vertices (63)](yang-mills/readers/quantum_nonabelian_vertex.pdf),
  [volume-uniform vacuum estimates (81)](yang-mills/readers/volume_uniform_vacuum.pdf) and
  [spatial-continuum maps and obstructions (129)](yang-mills/readers/spatial_continuum.pdf); earlier versions of these
  readers are at the top level of the repository.
- **S6.** The [five-page key-advances reader](s6/26_s6_key_advances_frozen_2026-09-06.pdf)
  ([LaTeX](s6/27_s6_key_advances_frozen_2026-09-06.tex)) and the [project guide](s6/README.md).
- **Navier–Stokes.** The [208-page corrected reader](navier_stokes_workbench_208p.pdf) with its
  [LaTeX](navier_stokes_workbench.tex); [navier-stokes/](navier-stokes/) holds the structured proofs, checks, the
  [vacuum-hydrodynamics continuation](navier-stokes/continuations/20260919-vacuum-hydrodynamics/), the
  [finite-control and force collection](navier-stokes/continuations/20260930-coupled-viscous-control/) and an
  [editable LaTeX reconstruction of the source paper](navier-stokes/sources/openai-source-faithful-20260920/).
- [workbench.json](workbench.json): machine-readable catalogue of the tracked files;
  [releases/2026-09-09](releases/2026-09-09/): release manifests; [ARCHIVE.md](ARCHIVE.md): earlier filenames and
  editions; the [live Overleaf workbench](https://www.overleaf.com/read/rtmyqxyrzprn#fa24eb).
- [CONTRIBUTING.md](CONTRIBUTING.md) and [REVIEW_GUIDE.md](REVIEW_GUIDE.md): how to contribute an argument, a
  calculation or a check.

## Sources and credits

- Levent Alpöge: the Jacobian counterexample used in the material-tensor branch,
  [announced on 20 July 2026](https://x.com/__alpoge__/status/2079028340955197566) (the announcement credits Akhil for
  the question and Fable for the work producing the example), and the S6 complex-threefold construction, circulated by
  Alpöge and produced with Claude ([original manuscript](https://alpo.ge/s6.pdf)).
- Terence Tao's [exposition of the Jacobian counterexample](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/)
  (21 July 2026); Philip Engel, [*Complex structures on S6*](https://arxiv.org/abs/2609.38442) (arXiv:2609.38442), which
  gives a self-contained proof of the S6 construction by a geometric route.
- Sung-Jin Oh's global Cauchy theorem, applied in the compact-support evolution continuations.
- OpenAI, [*Finite Time Blowup for Navier–Stokes*](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf),
  the source paper of the Navier–Stokes programme; its separate transcription is
  [openai-navier-stokes-latex](https://github.com/KokunoYumeto/openai-navier-stokes-latex).
- The point-of-use credits and the exact dependencies are in [ATTRIBUTION.md](ATTRIBUTION.md); the papers cite the
  literature they use.

## Rights

The repository has no licence file. Cited works, the source paper and the originating constructions keep their
authors' rights; see [CONTRIBUTING.md](CONTRIBUTING.md) for what may be published here.
