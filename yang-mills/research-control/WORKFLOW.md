# Research loop and review contract

## The working target

Construct the original interacting continuum theory and determine its physical excitation-energy edge. The current SU(2) workbench supplies finite-regulator operators and comparison maps. Keep the continuum theory, physical units, nontriviality, observable-sector completeness, and gauge-group scope in view while doing each calculation. A finite matrix result receives its exact finite scope.

The immediate measurement is the primitive norm in RESEARCH_NOTE.md L2. The active continuation connects local vacuum scores, the exact off-diagonal Hamiltonian, minimum-energy sections, and their refinement tower (L8–L25).

## A session has six operations

1. **Refresh and inspect.** Read the current workbench and the peer entries in state.json, including open PRs. Record exact head/blob and read scope. New commits trigger a comparison with the previously read source, not automatic acceptance. A full proof read, a partial read, PR-description discovery and an execution receipt have separate records. Never run newly retrieved code before reviewing its imports, I/O and resource use.
2. **Choose the mathematical change.** Name the original quantity being improved and the connected result to compute. Use at least one current original source. A task consisting only of more examples, a new notation, or larger checker counts does not change the declared target quantity. Counterexamples to a particular inference and corrections can be substantive results and keep their explicit maps.
3. **Derive on the original objects.** Write source/target spaces, operator/form domains, actual coefficients, observation fibers, kernel and norm pairings. For a transfer from another problem, write the formula dictionary and the proved comparison. Keep a source's hypotheses attached; a peer asymptotic constant stays with its original source measure until an actual transport computes its return.
4. **Check independently.** Run check.py in ordinary and optimized Python. It uses exact rational fixtures, a separate producer/auditor comparison, structural metadata checks, and named mutation tests. A generic crash never counts as rejection of a false formula. Review analytic arguments independently of these fixtures. Existing Lean receipts stay attached to their source revision; no new Lean claim without a completed relevant run.
5. **Reconcile and publish.** Check the branch heads again, re-read any changed dependency actually used, retain previous attempts, and open an additive PR. Do not merge it. Include tested hashes, scope, what was improved, and what was left unevaluated. Run the repository's full catalogue generator in a complete staged checkout when available; never report a run that was unavailable. This contribution leaves generated catalogues unchanged.
6. **Leave a mathematical checkpoint.** state.json names the completed result IDs, exact source pins, current target quantities and the next selected calculation. A later session can choose another route with a reason and source record. Independent reviewers should be able to reproduce the finite evidence and examine every analytic proof without the originating conversation.

## Checker contract

From the repository root:

    python -B yang-mills/research-control/check.py > ordinary.json
    python -O -B yang-mills/research-control/check.py > optimized.json
    cmp ordinary.json optimized.json
    python -B yang-mills/research-control/check.py --verify-receipt yang-mills/research-control/verification.json > verified.json

These executions require only the Python standard library. Checks raise explicit exceptions and remain active under -O. The output records named tests, named false-formula rejections, code and source hashes, and explicit false values for analytic_proof_checked and continuum_gap_proved.

`check.py --validate-state PATH` validates a candidate state against the same schema and mathematical-scope rules. `check.py --source-cache DIR` additionally verifies any declared cached peer file against its pinned Git blob; absent files are reported as unavailable rather than passed. `check.py --compare-intake PATH` compares a newly gathered peer snapshot with state.json and returns a nonzero status on changed watched revisions. The session must then read and classify the changes; the command never silently updates source pins.

`--verify-receipt PATH` compares a fresh complete execution record, including local input hashes, to an earlier receipt and fails on any difference. A checker pass establishes the checks actually executed. Written analytical proofs remain reviewable mathematics. The machine enforces that a finite fixture cannot be the sole evidence for a universal analytic or continuum claim, but this metadata enforcement is not a semantic proof assistant.

## Cross-workbench exchange

Track Zeta main and the observation-kernel/signed-resolvent PRs; Collatz main and its stopped/residual/anchored continuations; Erdős–Straus main and its boundary/moment contributions; Erdős 817 main and its general-k and outer-controller work. Retrieve their current open-PR list each session, rather than treating these PR numbers as permanently latest.

The current source read uses Zeta AMT7–9 and PR32 OK1–2 to construct the original Yang–Mills energy sections. Collatz history fibers supply exact loss-of-information regression material. Erdős 817's validator supplies a provenance design precedent. Erdős–Straus's original labelled success maps have been inspected; its moment-interface discussion and the latest Collatz/817 PR descriptions are discovery records, not imported Yang–Mills theorems.

Keep every peer result attached to its own original problem, author attribution and proof scope. Do not copy private sessions or third-party literature bodies. Ordinary repository commits and explicit peer records are the synchronization channel; unseen local Codex work remains unseen.

## Current mathematical checkpoint

The new local score trace bound has no exterior-volume factor but retains xi_n. The exact response term to study is

    (kappa_n b)^2 <T*Xg,(D+s)^(-1)T*Xv>.

Its comparison uses the kinetic form kappa_n b<Xg,Xv>, the restored state metric L23, and every residual in the L25 tower. The next selected work is quantitative control of this actual response on growing physical observation families. An integrated score bound is not promoted to a pointwise multiplication-operator bound. The uncomputed continuum quantities remain labelled uncomputed.

## Execution environment of this contribution

The authenticated GitHub connector performed the current repository and open-PR intake. Direct Git cloning in the local execution environment failed at DNS resolution. Local exact tests used the new files and the previously delivered PR4 source archive, whose note bytes match the pinned Git blob. No remote peer checker, new Lean run, paid Codex job, scheduled watcher or background research process was started. The parent finite checker was replayed separately.
