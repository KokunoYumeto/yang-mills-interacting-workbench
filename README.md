# Yang–Mills and Navier–Stokes workbenches

This repository contains readable research workbenches, source bundles, exact checkers, and provenance. For the Yang–Mills work, start with [the current-lanes reading guide](06_CURRENT_YM_LANES_README.md) and the separately downloadable topic PDFs.

## Navier–Stokes — corrected 9 September 2026

The principal readable artifact is [the 208-page Navier–Stokes workbench](navier_stokes_workbench_208p.pdf); [the complete LaTeX](navier_stokes_workbench.tex) and [byte-preserving source package](navier_stokes_source_bundle.zip) accompany it.

The edition records the reconstructed finite-time, smooth-forced positive-viscosity construction and its exact bridges into the Yang–Mills calculations, while preserving the forcing, viscosity, transport, pressure, and nonlinear terms. The included JSON files give the source manifest and replay/check results. They record the current validation boundary explicitly: the complete analytic/Lean validation of the supplied Navier–Stokes construction remains in progress, and this package does not by itself claim a finished Millennium-problem proof or a source-free quantum Yang–Mills mass-gap theorem.

The source package is provenance material for readers who want to audit the definitions, maps, calculations, and checkers rather than rely on a summary. The separate Yang–Mills files are retained alongside this addition.

## Finding and continuing the work

Read [the workbench map](WORKBENCH.md) for a plain-language route through the programmes, source versions, and open verification questions. [The machine-readable inventory](workbench.json) pins the indexed source revision. [The current handoff](RESEARCH_LOG.md) explains this organizational pass and what remains to do; [the review guide](REVIEW_GUIDE.md) explains how to record checks made while reusing another workbench's results. These additions do not certify the mathematics or replace the original research artifacts.
