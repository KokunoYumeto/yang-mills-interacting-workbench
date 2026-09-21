# Coupled response continuation

Read [the full proof](RESEARCH_NOTE.md) and [the current state](state.json).
The original Hamiltonian coupling, its self-adjoint form restriction, the full
complex response Gram, and the Split Zero forcing-class residual now give
explicit two-sided energy and state-metric enclosures. Moment inputs keep
singular coefficient fibers and the shifted cross terms.

From the repository root (Python standard library only):

```sh
python -B yang-mills/continuations/20260914-coupled-response/check.py --verify-receipt yang-mills/continuations/20260914-coupled-response/verification.json
python -O -B yang-mills/continuations/20260914-coupled-response/check.py --verify-receipt yang-mills/continuations/20260914-coupled-response/verification.json
```

The executable imports the unchanged parent rational-matrix helper after checking
its exact Git blob. Finite test matrices are declared fixtures. No actual vacuum
moments, independent analytic audit, new Lean run or continuum gap are certified.
The parent workflow and source reports remain historical, content-addressed records.
New source intake and the Hamiltonian/self-adjointness exchange direction are in
state.json. No watcher, paid model execution or automatic merge was started.

The current advance is the residual certificate, not a claim that positive-time
resolvent control already supplies a positive physical excitation edge. The next
original inputs are N0,N1,N2, with their full fine-vacuum definitions in C20.
