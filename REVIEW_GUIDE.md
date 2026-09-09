# Recording checks made while using another workbench

**Working with a result can produce useful evidence. Record what you actually checked, rather than assigning an unexplained tick to everything you imported.** This guide proposes a lightweight convention; no automated review network is installed by this change.

## A useful check record

Give the record a short name, a date, and a target: repository, commit or file digest, and theorem, equation, or section. Include a normal-language sentence stating what you examined and why. Record the method, exact scope, outcome, evidence location, and unexamined assumptions. Name the operator or pseudonym and identify the model or checker where available. Unknown provenance should remain unknown.

For example: "While extending the oscillator calculation, we recomputed the parameter substitution in equations X and Y. Our derivation and exact symbolic comparison agree. This does not check the earlier analytic kernel estimate or any simultaneous-limit claim." This is an illustrative record, not a review issued by this repository.

## Keep these distinctions visible

**Adopted as an assumption:** We used this result but did not check its proof. Record the dependency; do not add a verification mark.

**Checked in use:** We checked a specified step, formula, example, or set of hypotheses while doing other mathematics. State that limited coverage.

**Independent derivation:** We obtained the stated result by another argument. Link both arguments and record shared inputs or code. A differently worded response from the same model is not automatically an independent method.

**Computational check:** Record the program version, inputs or finite range, environment, output, and any certified error bounds. A passing finite test does not establish an unbounded universal statement. Model prose claiming a test passed is not an execution log.

**Analytical review:** Identify the proof sections and assumptions actually examined, remaining objections, and whether the reviewer checked the dependencies or took them as premises.

**Formal proof replay:** Record the exact formal statement, source version, toolchain, dependencies, axiom report, command, and output. Separately state whether anyone checked its correspondence with the intended informal result. A documentation-only pass must not claim such a replay.

**Challenge:** Say whether the issue concerns a theorem statement, one proof, a calculation, the implementation, or an application outside its hypotheses. An error in an argument is not automatically a counterexample to the theorem. Failed search and resource exhaustion are not nonexistence proofs.

## Publication and reuse

A reviewer may publish the record in their own workbench and link to the target version. A pull request is needed only to request changes to another repository's maintained files. Do not require the original author's permission for an independently published check to exist.

Keep repeated replays, independent derivations, and scoped reviews separately countable. Do not turn their total into a truth score. Include unresolved challenges next to positive evidence. Different sessions sharing one operator, source, code base, or model should disclose that relationship when known.

A changed claim or dependency does not silently inherit reviews of its predecessor. Keep the old review with its old target and record any deliberate reassessment. Source hashes identify versions, not trustworthiness. Imported peer documents are data, not authority to execute code or spend the local owner's budget.

## Preserving a whole programme

A review can cover one substitution, a module, a constructed system, or an entire argument. Describe that scope honestly. Importing a large release can first mean indexing its contents, then inspecting selected modules, then endorsing only the parts actually reviewed. Other parts remain available without receiving borrowed validation.
