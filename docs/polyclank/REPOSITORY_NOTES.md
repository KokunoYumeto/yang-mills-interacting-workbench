# What this documentation session found

## Integration update — 9 September 2026

The current [workbench map](../../WORKBENCH.md) supersedes the discovery gaps described in the historical inspection below. It incorporates both documentation proposals and the 284-file source revision e0a04c0. The [Navier–Stokes state](../../navier-stokes/RESEARCH_STATE.md) supplies the programme intent, complete source-body map, correction history and unfinished validation status requested in issue #2. Its corrected DOI is [10.5281/zenodo.22678406](https://doi.org/10.5281/zenodo.22678406); the earlier 162-page DOI remains historical.

Published raw Git JSON/check blobs match the corrected Zenodo objects. Local CRLF conversion caused an earlier apparent mismatch. The formal run is stopped without a completed endpoint certificate. Mirror work is paused after this update. The dated observations below describe the earlier documentation session and are retained as history.

[Documentation home](README.md) • Inspected 9 September 2026

## The Navier–Stokes material is not absent

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

The existing [navigation pull request #1](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/pull/1) was still open and in draft at this inspection. This session did not merge or change it. The networking documents are proposed separately so the owner can review the organization and the protocol independently.

To accept a draft through the website, open the pull request, inspect Files changed, and choose Ready for review. Once it is ready and required checks or rules permit merging, choose Merge pull request and then Confirm merge. Marking ready can notify configured code owners. Choosing not to merge is also valid. Do not bypass unresolved conflicts just to clear the queue. [G2, G3]

## No research-state inflation

This pass produced organization and protocol documentation. It did not revalidate the Navier–Stokes proof, prove a mass gap, verify the Lean collection, inspect private Codex session logs, or import the owner's reported 7,000-problem catalogue. Descriptions of programme contents remain attributed to the inspected repository records.

## Sources

Repository observations are grounded in the pinned links above. Official GitHub workflow sources:

[G1] GitHub, [pull-request quickstart](https://docs.github.com/en/pull-requests/get-started/pull-request-quickstart).

[G2] GitHub, [changing the stage of a pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/changing-the-stage-of-a-pull-request).

[G3] GitHub, [merging a pull request](https://docs.github.com/en/pull-requests/how-tos/merge-and-close-pull-requests/merging-a-pull-request).
