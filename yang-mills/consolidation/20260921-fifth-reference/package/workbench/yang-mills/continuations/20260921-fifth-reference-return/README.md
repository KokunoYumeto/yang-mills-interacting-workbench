# Completed fifth-reference correction and physical return

21 September 2026. Read `FIFTH_REFERENCE.md`, then `HEAT_AND_COMPLEMENT.md`.

This continuation resumes the recorded Yang–Mills task, using the complete available fifth catalogue. It evaluates original edge-spin bounds, the entire degree-six through degree-ten residual, the full correction at its first discriminant endpoint, and its heat/moment return to the complete physical complement. Original units are kappa=2g²/a and xi=1/(4g⁴); no continuum mass is concluded.

The fifth-source bound gives m5<1638684 and t5<190128. Its first positive discriminant root is between0.018424953576117616681 and0.018424953576117616682. The corresponding sufficient g² threshold lies between3.683551983985727304439 and3.683551983985727304440. Every finite box has the displayed full physical gap on that source interval. On the circle1/55 the box-independent heat remainder has prefactor67896/169 and decay13/8. For every box and g²>=13, the complete plaquette-family complement costs less than1/2000 of its original energy and adds less than1/2000 to its state metric. Atg²>=16 both costs are below1/25000.

The new trace-word coefficient estimate retains cyclic orientation changes and every coordinate reflection. It improves3498 of6240 original partial-projection bounds. All321 signed final-spin expansions are checked as complete sphere-polynomial identities, with5726 exact rational primal/dual certificates. All662 original fifth rows and124864 marked transports contribute to the final bounds. The other341 rows use their complete original input splits and retained lower-order channel bounds; they are not assigned the distinct-face recurrence.

The physical source proof is written in full. The matrix/polynomial checks do not constitute a formal proof of the Banach-space, elliptic or spectral arguments. No external analytical review or Lean execution is claimed. The missing sixth catalogue and its previously incomplete execution remain missing; this tranche does not depend on them.

Fast exact replay from this directory:

```sh
python -B verify.py --verify-receipt verification.json
python -O -B verify.py --verify-receipt verification.json
```

Full new regeneration, complete polynomial/dual audit, and named negative controls:

```sh
python -B replay.py --output-dir /tmp/ym-fifth-reference-replay
```

The replay writes its logs outside the sealed cumulative tree, temporarily mutates one isolated row for an intended rejection, restores it, and confirms final source identities. No network, paid service, remote repository write, scheduled process, or merge is invoked.
