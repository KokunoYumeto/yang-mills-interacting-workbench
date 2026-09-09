# Start here: what this workbench contains

**This repository holds several research programmes, not one finished proof.** It records work on interacting Yang–Mills systems, fixed-box calculations, volume and spatial-continuum questions, and source-dependent Navier–Stokes bridges. The purpose of this page is to help a person or another agent find the relevant work without reconstructing the project's history from large files.

**Inventory checked: 9 September 2026, at commit ed8cb4bee090d8f7cc14166199aebdef557d066e.** This is a snapshot of one repository, not a claim to contain everything known about these problems. The machine-readable companion is [workbench.json](workbench.json).

## What we are trying, and what is established here

The repository's [original overview](README.md) describes exact calculations and bridges that preserve forcing, viscosity, transport, pressure, and nonlinear terms. The [Yang–Mills release guide](06_CURRENT_YM_LANES_README.md) distinguishes the separate programmes and says the interacting four-dimensional continuum and mass-gap conclusions remain unfinished. These are the maintainers' published descriptions; this organizational pass has not independently proved the underlying results.

One specific motivation is stated in the [prescribed-path kernel note](scaled_angle_prescribed_kernel_rates.md): obtain estimates for a fixed-box oscillator kernel and determine whether they can transfer to an exact interacting lattice along simultaneous limits. Its final section identifies missing volume-uniform control. The note does not identify the oscillator calculation with an interacting-continuum result.

For other programmes, the full motivation and theorem inventory still need extraction from their source bodies. Their titles below are navigation labels, not independently verified conclusions. Do not fill in those missing descriptions by guessing.

## Where to read

### Quantum coarse-graining — YM-QUANTUM

Start with [the 75-page reader](quantum_coarse_graining_75p.pdf). The release guide groups two component readers with it: [interacting tensor bands](quantum_interacting_tensor_band_71p.pdf) and [nonabelian vertices](quantum_nonabelian_vertex_63p.pdf). Associated source material and check records are described in the Yang–Mills bundle below. These reader bodies were not reviewed during this pass.

### Volume-uniform actual-vacuum work — YM-VOLUME

Start with [the 77-page volume reader](volume_uniform_vacuum_77p.pdf). Keep its hypotheses and limiting regime attached to every result reused elsewhere; its title alone does not establish a bound uniform in any particular parameter. The release guide identifies this as a separate programme.

### Spatial-continuum work — YM-SPATIAL

Start with [the 129-page reader](spatial_continuum_129p.pdf), accompanied by [Markdown](spatial_continuum_129p.md) and [TeX](spatial_continuum_129p.tex). The [inspected commit's own message](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/commit/ed8cb4bee090d8f7cc14166199aebdef557d066e) identifies this as the current standalone reader and explicitly limits it to regulator-level results.

The [121-page reader](spatial_continuum_121p.pdf) and [127-page reader](spatial_continuum_127p.pdf), with [127-page Markdown](spatial_continuum_127p.md) and [TeX](spatial_continuum_127p.tex), remain available. The release guide still describes the 121-page bundled edition. Do not assume the bundle or its manifest includes later standalone additions, and do not infer that every argument was preserved merely from increasing page counts. No source comparison was performed here.

### Prescribed-path kernel rates — YM-KERNEL

Read [the standalone note](scaled_angle_prescribed_kernel_rates.md). It states finite-box oscillator estimates and separately discusses the missing uniform bridge to simultaneous exact-lattice limits. Equations PK7 and PK10 were previously raised for a prefactor audit in the project discussion; no mathematical correction or recheck is included in this navigation pass. Do not interpret this listing as an endorsement of those equations.

### Fixed-coupling disk checker — YM-DISK

The root contains [a Python checker](check_fixed_coupling_analytic_disk_obstruction.py). It is indexed here but was not executed or reviewed in this organizational pass. The next reviewer should record its exact test range, what claim those tests address, and what they leave unproved.

### Navier–Stokes work and its bridges — NS-BRIDGES

Start with [the 208-page workbench](navier_stokes_workbench_208p.pdf) and [its TeX](navier_stokes_workbench.tex). The [source bundle](navier_stokes_source_bundle.zip), [primary manifest](navier_stokes_primary_manifest.json), and [reported check records](navier_stokes_checks.json) accompany it. The original README says complete analytical/Lean validation of the supplied construction remains in progress. These files are not being newly certified here.

### Yang–Mills source archive — YM-ARCHIVE

The [current-programmes ZIP](05_current_authored_ym_lanes_2026-09-09.zip), [release guide](06_CURRENT_YM_LANES_README.md), and [manifest](07_CURRENT_YM_LANE_MANIFEST.json) are the archive entry points. The guide describes source and reader directories inside the ZIP; those are not ordinary root directories in the inspected Git tree. The archive was not unpacked in this pass. Preserve it as a release artifact rather than rewriting it to update this index.

## What another workbench can check

A useful review can emerge while reusing the mathematics. Record it against the exact source version and identify the part actually examined. For example: "While deriving this consequence, we independently checked the substitution in equation X under assumptions A and B." That earns a scoped check record, not an automatic endorsement of the whole programme.

Use [the review guide](REVIEW_GUIDE.md) for adoption, calculations, analytical review, formal replay, and challenges. The initial machine inventory contains no new mathematical reviews. A hash identifies file contents; it is not a correctness score.

## How to resume without losing the purpose

Read [the current handoff](RESEARCH_LOG.md), then choose a programme or direction. Before starting a substantial calculation, write what you are trying, why the route is worth trying, which sources support it, and what would count as progress. A speculative analogy is a valid starting point when marked as such.

Keep the original objective and outstanding user requests outside the conversation. When the direction changes, say why. At the end of a run, link the actual artifacts and distinguish proposed, derived, tested, reviewed, and formally checked results. A workbench can contain a whole theory's worth of work; its overview must still make that work findable.

## What this organizational pass did not do

It did not move or delete any mathematical source, extract archives, install dependencies, run a model swarm, execute repository code, replay Lean, certify novelty, or revise a theorem. The new documents are navigation and proposed collaboration conventions. They do not license third-party material or authorize peer content to issue commands on a contributor's computer.
