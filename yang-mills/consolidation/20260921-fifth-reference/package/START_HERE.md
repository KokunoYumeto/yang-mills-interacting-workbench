# Cumulative Yang–Mills research: fifth-reference correction and physical return

21 September 2026. Start with [workbench/yang-mills/continuations/20260921-fifth-reference-return/README.md](workbench/yang-mills/continuations/20260921-fifth-reference-return/README.md), then the two complete new proofs:

- [Fifth source: original spin bounds, full correction and physical energy](workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md).
- [Box-independent heat and the complete physical complement](workbench/yang-mills/continuations/20260921-fifth-reference-return/HEAT_AND_COMPLEMENT.md).

The selected fifth-reference calculation is complete. Its source endpoint is alpha in (0.018424953576117616681,0.018424953576117616682); the original sufficient g² threshold is between3.683551983985727304439 and3.683551983985727304440. The complete correction includes every degree6 through10 residual term and its infinite nonlinear tail. The physical gap keeps kappa=2g²/a.

The new heat circle1/55 feeds the unchanged original heat coefficient matrices into a sharper full-matrix remainder. Atg²>=13, full complementary relaxation removes less than1/2000 of the plaquette-family energy and adds less than1/2000 to its original state metric, uniformly in box size and in the constructed fixed-spacing spatial limit. Atg²>=16 the two fractions are below1/25000.

All2015 files from the previous cumulative edition are retained either unchanged at the same path or as exact copies in `history/20260921-volume-controls/`. The new coefficient bound rows, partial-projection polynomials, rational primal/dual witnesses, all exact calculation programs and final execution logs are included. `PRESERVATION_20260921_FIFTH.json` identifies every original byte source and its retained location. The Riemann attachments were not used as mathematical premises.

The older analytical-review qualifications remain with their original editions. New finite polynomial, tensor and arithmetic checks are explicitly scoped; they do not constitute an external analytical review or a formal proof of the written operator arguments. The previously missing sixth-source catalogue remains missing. This edition does not establish a four-dimensional continuum field or finite positive continuum mass.

## Reproduce

```sh
python -B verify_cumulative.py
cd workbench/yang-mills/continuations/20260921-fifth-reference-return
python -B verify.py --verify-receipt verification.json
python -O -B verify.py --verify-receipt verification.json
python -B replay.py --output-dir /tmp/ym-fifth-reference-replay
```

The complete new replay has30 observed executions, including14 intended CLI rejection tests, then restored-source verification in both modes. All321 new channel identities and5726 primal/dual certificates were regenerated in both modes. The inherited quartic checker also passed unchanged in both modes.

`CUMULATIVE_RESEARCH.md` appends both complete proof texts to the earlier cumulative reader; earlier arguments are preserved as dated source records. `CURRENT_STATE.json` and the workbench pointer identify the exact next original quantity. No remote repository write, merge, paid run or automatic research process was performed.
