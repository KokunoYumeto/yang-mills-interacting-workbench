# PolyClank: workbenches that explain themselves and exchange research

Design notes • 9 September 2026 • Proposed community protocol, not a deployed network

**A workbench says what it tried, why it tried it, and where that leaves the research. It does not prescribe the next participant's mathematical ideas.**

PolyClank is the working name for a network of independently maintained, human- and machine-readable mathematical workbenches. A contribution may be a single checked calculation, a formalization of an existing theorem, an exposition, or a large programme containing several systems, proofs, failed approaches and open dependencies. The network's objects are smaller addresses within that programme; they are not a requirement to make the programme small.

The current design separates three things: the material published by a workbench; the evidence supporting its mathematical claims; and the local decisions about what another participant wishes to investigate. Publication does not require a single master repository. Reuse does not silently become verification. Network messages do not authorize execution or spending.

## Read by question

**How would workbenches communicate without all being on GitHub?** Read [Networking and libp2p](NETWORKING.md). It describes a static-file starting point, optional peer-to-peer transport, message types, offline catch-up, and implementation acceptance tests.

**What should a returning person or model know before continuing?** Read [Research state and large jobs](RESEARCH_STATE.md). It defines descriptive handoffs, programme-level contributions and durable memory without compulsory microtask decomposition.

**How do we identify thousands of problems without confusing similarly named statements?** Read [Problem catalogue](PROBLEM_CATALOGUE.md). It separates short catalogue aliases from exact statement revisions and mathematical relationships.

**Where can material be mirrored or assigned a DOI, and what may be published?** Read [Hosting, rights and releases](PUBLISHING.md). It records a dated check of official provider policies and distinguishes legal reuse permission from a provider's narrower submission rules.

**What did this session actually find in the linked repositories?** Read [Repository observations and GitHub basics](REPOSITORY_NOTES.md). It points to the already-published Navier–Stokes material, the Lean fork, and the handoff issue.

## What this documentation changes

It records the owner's requested shift from an externally assigned task queue to a network of self-describing research programmes. A job may contain many self-chosen experiments, subagents and mathematical branches. Optional bounded review requests remain useful, but the next researcher is not obliged to follow a predecessor's plan.

This change adds documentation only. It does not install libp2p, modify existing agent instructions, create a live registrar, contact models, issue a DOI, merge another pull request, or validate any mathematical theorem. The networking names and example paths below are proposed PolyClank conventions, not existing public standards or running endpoints.

## Success criterion

Two separately hosted workbenches can discover one another, retrieve exact published objects, preserve concurrent branches, and publish checks without mutual repository write access. Their readers can understand what was tried and what the checks actually cover. Large contributions can be indexed without either wholesale acceptance or a complete reread at every synchronization.
