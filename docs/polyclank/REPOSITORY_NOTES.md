# Public editions and documentation history

[Documentation home](README.md) • Inspected 9 September 2026

## Current integrated repository

The current [workbench overview](../../WORKBENCH.md) and [machine catalogue](../../workbench.json) supersede the earlier 22-file navigation snapshot. [Yang–Mills](../../yang-mills/) contains the 79-page quantum and 81-page volume readers, their companion readers and full selected sources; [S6](../../s6/) links its complete frozen project; [Navier–Stokes](../../navier-stokes/) gives the corrected reader and source records.

The directly inspected current editions are [Yang–Mills 22678364](https://doi.org/10.5281/zenodo.22678364), [S6 22678442](https://doi.org/10.5281/zenodo.22678442), and [Navier–Stokes 22678406](https://doi.org/10.5281/zenodo.22678406). The last is the corrected **208-page** edition; **22667379 is the earlier 162-page edition**. The historical observation below reported a DOI from another README before the actual record could be inspected; it is not the current publication pointer.

The [public Overleaf](https://www.overleaf.com/read/rtmyqxyrzprn#fa24eb) is the shared evolving workbench, not an immutable DOI snapshot. Finding the corrected public reader does not identify the newest active fluid session or establish that an uninspected session has no later changes. That narrower source question remains in issue #2.

PRs #1 and #3 have been integrated into the current topic organization with these corrections. Their original proposals and inspection history remain accessible in Git. This pass changes navigation and metadata, not mathematical source/PDF/archive contents.

## Earlier web-session observations (historical)

[The Yang–Mills repository README](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/ed8cb4bee090d8f7cc14166199aebdef557d066e/README.md) identifies a 208-page Navier–Stokes workbench, full TeX, source bundle and JSON records. It expressly says complete analytical/Lean validation remains in progress. That is the source's scope statement, not a new assessment of the mathematics by this documentation session.

[The zeta reader README](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/cf3c5f9dd58524ad2f911a2ecccaff994c3f4f97/README.md) lists a 208-page fluid reader in a frozen six-reader release and links a separate Navier–Stokes DOI, 10.5281/zenodo.22667379. The DOI is reported from that README. The Zenodo landing page could not be retrieved in this pass. Equal page counts do not establish that the two fluid readers are byte-identical or equally current.

Targeted accessible-repository searches for Navier/Stokes returned the Yang–Mills and zeta repositories, not a separately named Navier–Stokes repository. This does not exclude private or differently named working locations. The newest source session has not been identified.

[Handoff issue #2](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/issues/2) records these findings and requests the current working pointer, programme intent, completed and unfinished work, and actual verification status. It is a persistent message, not proof that another session was contacted or awakened. No model job was triggered or person assigned.

## The linked Lean fork illustrates smaller contributions

The linked [lean-theorems-1](https://github.com/KokunoYumeto/lean-theorems-1/tree/9bba692310c8c4c6886cbd868ee909411888c0c0) is a fork of sneed-and-feed/lean-theorems-1, according to GitHub metadata. Its README has 31 grouped theorem entries at this revision, and Formalization.lean imports 31 modules. Some entries include multiple related theorems, so 31 is not a count of all declarations. GitHub identifies the repository license as CC0-1.0.

This pass read the README, import entrypoint and file inventory, not every formal proof. No Lean build or transitive axiom check was run, and the README's novelty and machine-checking claims were not independently established. The original post's three-theorem starting point and which later proofs came from which session have not been reconstructed here.

For PolyClank this is a useful kind of contribution: retain upstream identity and citations; link each added formalization to its declaration and exact statement; record any build receipt; and preserve the difference between a new formalization and a new mathematical theorem. The same protocol also accommodates a much larger research programme. No changes were made to the Lean fork.

## GitHub without the terminology barrier

A **push** sends local commits to a remote repository. A **pull** brings remote changes into a local checkout. A **pull request** proposes incorporating one branch's changes into another; it is not the same operation as pulling. A **merge** incorporates those changes. A **draft pull request** is a proposal that is not yet eligible to merge. [G1, G2]

The [navigation pull request #1](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/pull/1) was open and in draft at the earlier web-session inspection. The later local integration reconciles it with the current topic directories and incorporates the networking proposal in PR #3. The earlier draft status is not an outstanding request to repeat publication authorization.

For future contributions, a draft can be marked ready and merged through GitHub when its conflicts and applicable checks are resolved. An authorized maintainer can also integrate the commits locally and push the resulting merge. These are alternative workflows, not instructions for a reader to perform another approval of this completed integration. [G2, G3]

## No research-state inflation

This pass produced organization and protocol documentation. It did not revalidate the Navier–Stokes proof, prove a mass gap, verify the Lean collection, inspect private Codex session logs, or import the owner's reported 7,000-problem catalogue. Descriptions of programme contents remain attributed to the inspected repository records.

## Sources

Repository observations are grounded in the pinned links above. Official GitHub workflow sources:

[G1] GitHub, [pull-request quickstart](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart).

[G2] GitHub, [changing the stage of a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/changing-the-stage-of-a-pull-request).

[G3] GitHub, [merging a pull request](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-a-pull-request).
