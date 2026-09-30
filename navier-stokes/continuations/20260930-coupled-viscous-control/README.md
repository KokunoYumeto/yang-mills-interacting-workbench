# Navier–Stokes research: finite controls, exact force maps and review

This addition belongs to the Navier–Stokes reconstruction and validation
collection. The workbench retains the corrected 208-page analytical reader,
the independent source-faithful reconstruction, the vacuum-hydrodynamics
continuation and their original sources. This addition supplies complete
finite Boussinesq control calculations with positive physical diffusion
and the exact maps needed to investigate a modified infinite construction.

## Read the mathematics

The accompanying 121-page PDF is an earlier reading snapshot. It includes
the finite third return, the fixed-diffusion similarity, the based residual
and the returned-core correction. It predates the complete annulus-force
and force-to-state sections. The current complete LaTeX is
source/coupled_viscous_control.tex. Its complete integration body is
source/integration/coupled_viscous_control_body.tex.

The updated sources pass the registered exact replays and static-reference
checks. A final PDF build of the newest two sections remains pending because
the shared TeX slot was occupied at the validated checkpoints. The older PDF
is identified by its actual scope; it is not a compiled copy of the newest TeX.

The new complete arguments are:

- third_return/third_return_completion_body.tex: a definite positive
  equal-diffusion interval, compact nested shooting graph, selected third
  return, strict endpoint margins and retained positive curl.
- infinite_modified/parabolic_similarity_body.tex: exact physical state
  and force scaling at fixed positive diffusion, with every radius and clock.
- infinite_modified/based_cascade_body.tex: the reset obstruction, full
  based-increment residual and exact parent-state interface.
- infinite_modified/return_correction_body.tex: signed residual correction,
  complete chart invariants, actual returned affine state, explicit finite
  unforced core evolution and a compact correction flat at its initial time.
- infinite_modified/full_support_force_body.tex: every full-support signed
  force term and mixed jet, explicit cutoff constants, annulus diffusion
  lower bounds and the exact cancellation-defect map.
- infinite_modified/force_reachability_body.tex: the original-coordinate
  weighted energy identity, the force needed to reach a based state and
  its exact affine target cost.

Each file is under source/. The independent symbolic programs accompany
the full written proofs. The finite calculations do not establish the
modified infinite growing return, all-stage signed force budget or terminal
smooth-force extension. The imported global Navier–Stokes claim remains
unverified by this review.

The audits/ directory preserves the complete Lemma 10.5 rederivation,
its stronger remainder bound, the exact finite angular Gram calculation
and the written review of Claude's source-bound additions. Review of finite
spectral and coefficient results does not validate imported NS/H1–H4.

## Experimental Everyday English reference

A separately named ZIP preserves the earlier full-paper Everyday English
attempt, its PDF, EPUB, HTML and editable sources, together with the later
unfinished page-1 manual draft. The earlier draft was rejected as the basis
for the later rewrite. Its earlier completion and release records are
historical producer decisions. The success of the writing experiment has
not been established. It is retained for reading, comparison and reference.

## Sources and reproduction

Human source: Levent Alpöge and Tristan Buckmaster, *Blowup for the
Boussinesq equations with smooth forcing*, Sections 3.3 and 3.7.10;
the exact source identity and reading limitation are in
source/integration_manifest.json. The original source PDF is preserved,
not newly read here as a substitute for author TeX.
The OpenAI source manuscript and frozen formal revision remain cited in
the parent reconstruction. These additions are independent derivations
and reviews, with no new attribution to the source authors.

From source/ run python build_and_verify.py --skip-pdf for the exact replays
and static checks. At an available TeX checkpoint, run build_and_verify.py
to compile the complete project. No formal kernel certificate is asserted.


The source/ tree also retains the finite-stage auxiliary calculations and
dated source snapshots needed to reproduce and compare the development.
Their earlier PDFs and producer records retain their own recorded scopes.
The current entry point is source/coupled_viscous_control.tex; preservation
of an auxiliary file is not blanket acceptance of its historical claims.
