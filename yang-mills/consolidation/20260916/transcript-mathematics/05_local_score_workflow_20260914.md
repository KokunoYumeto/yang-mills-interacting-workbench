I’ve implemented the workflow, run its first research-and-verification cycle, and opened **draft pull request #5, “Add research workflow and exact local-score energy refinement.”** It is based on the existing PR #4 branch, preserves that work, and adds eight files. Neither pull request has been merged. The new commit is `f583ed5ddb13b3ca517c1bab2958f6a4be612d78`. 

[Complete workflow, mathematics, checker, and execution records](sandbox:/mnt/data/yang_mills_workflow_and_energy_refinement.zip) · [Read the workflow](sandbox:/mnt/data/yang_mills_research_workflow.md) · [Read the mathematical continuation](sandbox:/mnt/data/yang_mills_local_score_energy_note.md)

## 1. The workflow now lives in the workbench

The entry point is `yang-mills/AGENTS.md`. It directs an active research session to read the current mathematical state, inspect relevant developments in the other workbenches, select a connected calculation, execute the checks, and leave an explicit mathematical checkpoint.

The governing quantity is the original energy-controlled primitive:
$$
p_n(d_nf)=f,
\qquad
d_nf=(X_{e,\alpha}f)_{e,\alpha},
$$
on centered physical functions, with the original energy pairing
$$
\|d_nf\|_{1,n}^{2}
=
\frac{2g_n^2}{a_n}
\int\rho_n\sum_{e,\alpha}|X_{e,\alpha}f|^2\,dU_n.
$$
The ground-state transform and variational characterization give
$$
\boxed{\|p_n\|^2=\frac1{\Delta_n}.}
$$
Thus the workflow has an actual spectral quantity to return to, rather than using the number of calculations or checker assertions as a progress measure. The original Hamiltonian and ground-state identity remain the source of this pairing. 

The active loop has four connected stages:

| Stage | What it records or does |
|---|---|
| **Source intake** | Reads current default branches **and open pull requests**, records exact revisions and file identities, and distinguishes proof reading from discovery through a PR description. |
| **Mathematical selection** | Names the original quantity to improve and the maps, norms, domains, parameters, and retained kernels involved. |
| **Derivation and checking** | Writes the argument, runs exact tests and deliberately false formulas, and keeps analytical proof review separate from executable evidence. |
| **Continuation and publication** | Updates the mathematical state and attempt account, checks the dependency revisions, and submits an additive review branch with a precise next calculation. |

The machine-readable `state.json` contains the completed result identifiers, their dependencies, eight source records, explicit cross-workbench transfers, unevaluated quantities, and the next selected calculation. The workflow and checker are stored with the proof and execution record. 

**Source freshness has an explicit interface:** the active session gathers current GitHub revisions; the checker compares that snapshot with the recorded intake. A changed revision causes a named failure until its changes have been read and classified. The Python checker itself makes no network calls.

## 2. I checked the other number-theory workbenches

This produced useful input immediately, including developments on unmerged branches.

### Split Zero / Zeta: applied in this continuation

The current arithmetic-to-Gamma source-transfer calculation, **AMT7-10**, proves minimum-section composition on the same observation fibers while retaining the quotient and kernel metrics. The newer **PR #32** supplies the complete rectangular residual identity
$$
(X-S_G\Lambda X)^*G(X-S_G\Lambda X)
=
X^*GX-(\Lambda X)^*Q(\Lambda X),
$$
including the section correction and all off-diagonal entries. I read those arguments and instantiated their maps with the original Yang-Mills energy and state forms. Their arithmetic constants remain attached to their original measures. 

This was a substantive update to our earlier intake: the workflow now follows both the analytical source development and the independent formalization branches.

### Collatz: an exact regression against losing source information

The inspected history construction retains the explicit specialization fiber
$$
X_v(q)-X_u(q)=\frac{(q-3)(q+4)}{32},
\qquad
X_u(3)=X_v(3)=\frac{19}{32}.
$$
The checker now uses this actual example to reject reconstruction of the original history from the specialized value alone. The polynomial difference and its kernel membership remain recorded. 

The newer stopped, residual, and anchored continuations were also found through the open-PR scan. Their new descriptions are recorded as candidates for further source reading, rather than treated as already imported Yang-Mills results.

### Erdős-Straus: retained as a specific candidate

I inspected the new original-state construction in PR #6: its prime-labelled denominator defects, highest-degree kernel classes, and augmentation map that returns the actual success projector. That supplies a concrete candidate for later endpoint-observation work. The later moment estimates were discovered in the PR description; their proof bodies have not been imported into the present Yang-Mills calculation. 

### Erdős 817: used to strengthen the verification workflow

Its workbench validator provided a useful model for binding claims and receipts to exact source files, rejecting duplicate keys and invalid paths, and retaining the scope of each verification record. I used that design precedent for the independently written Yang-Mills checker. The newer outer-controller work is recorded separately as a mathematical candidate. 

This gives later sessions a maintained exchange record: **what was found, what was actually read, what was transferred by an explicit map, and what remains only a candidate.**

## 3. The mathematical advance from this cycle

The connected calculation follows the original interacting vacuum through

$$
\text{local electric expectations}
\longrightarrow
\text{conditional density derivatives}
\longrightarrow
\text{Hamiltonian coupling}
\longrightarrow
\text{minimum-energy refinement}.
$$

### A local bound without an exterior-volume factor

Retain
$$
\rho_n=\psi_n^2,\qquad
\kappa_n=\frac{2g_n^2}{a_n},
\qquad
\xi_n=\frac1{4g_n^4}.
$$
For refinement from level $r$ to level $n$, let
$$
b=2^{n-r}
$$
be the number of original fine links in each coarse link.

Let $\mathsf E$ be conditional expectation in the **actual fine vacuum**, $\mathsf J$ the ordered-holonomy pullback, and $m$ the actual coarse marginal. The original horizontal derivative is
$$
Y_{e,\alpha}
=
\frac1b\sum_{j,\beta}
\bigl(\operatorname{Ad}P_{e,j-1}\bigr)_{\alpha\beta}
X_{e,j,\beta}.
$$
Define the retained logarithmic density derivative
$$
S_{e,\alpha}
=
Y_{e,\alpha}\log\rho_n
-\mathsf J(X_{e,\alpha}\log m).
$$
It has conditional mean zero. Its conditional covariance is the complete matrix
$$
\Gamma_{ac}(W)=\mathsf E(S_aS_c)(W).
$$

For a finite set $F$ of coarse links, the new estimate is
$$
\boxed{
\begin{aligned}
I_F
&:=\int m\,\operatorname{tr}\Gamma\\
&\le
\frac4b
\sum_{e\in F}\sum_{j=1}^{b}
\min\!\left(
2r_{e,j}\xi_n,\,
\frac{16}{3}r_{e,j}^{\,2}\xi_n^2
\right)\\
&\le 32|F|\xi_n .
\end{aligned}}
$$
Here $r_{e,j}$ is the number of original plaquettes incident on the fine link.

The proof retains the full exterior operator. The original local vacuum equation is
$$
(\kappa_nE_e+K_e)\psi_n=v_nW_e\psi_n,
\qquad
K_e\ge0,\qquad
v_n=\frac1{2g_n^2a_n}.
$$
Taking its expectation gives
$$
\langle\psi_n,E_e\psi_n\rangle
\le 2r_e\xi_n.
$$
Conditional variance, the identity
$$
\rho_n|Y\log\rho_n|^2=4|Y\psi_n|^2,
$$
and the adjoint-matrix coefficients of the original horizontal fields then give the displayed bound.

**The exterior volume has disappeared from this local estimate. The coupling dependence remains.** On the current test path,
$$
g_n^2=(g_0^{-2}+\beta n\log2)^{-1},
$$
the resulting bound is
$$
I_F\le8|F|(g_0^{-2}+\beta n\log2)^2.
$$
That growth is recorded explicitly in the mathematical state.

### The same quantity gives the exact Hamiltonian coupling

Put
$$
\mathcal K=\ker\mathsf E,
\qquad
(Th)_a=\mathsf E(hS_a).
$$
The actual adjoint and covariance identities are
$$
T^*u=\sum_a S_a\,\mathsf Ju_a,
\qquad
TT^*=\Gamma.
$$

For a smooth coarse function $f$, the component of the full transported Hamiltonian landing in the retained kernel is exactly
$$
\boxed{
Cf=-\kappa_nb\,T^*Xf.
}
$$

Thus the density derivative being bounded is precisely part of the original interaction between retained variables and fiber fluctuations. It enters the energy calculation through an explicitly derived operator.

### Minimum-energy sections now compose through refinement

Let $D$ be the nonnegative self-adjoint operator represented by the original energy form restricted to $\mathcal K$. The note proves its closed-form domain and defines, for $s>0$,
$$
h_s(f)=\kappa_nb(D+s)^{-1}T^*Xf,
\qquad
\mathcal S_sf=\mathsf Jf+h_s(f).
$$

This is the minimum-energy lift of $f$ in its original conditional-expectation fiber. Its complete effective form is
$$
\boxed{
\begin{aligned}
q_{\mathrm{eff},s}(f,v)
={}&s\langle f,v\rangle_m
+\kappa_nb\langle Xf,Xv\rangle_m\\
&-(\kappa_nb)^2
\left\langle
T^*Xf,(D+s)^{-1}T^*Xv
\right\rangle_{\rho_n}.
\end{aligned}}
$$

The derivative retains the restored state metric:
$$
\boxed{
\frac{d}{ds}q_{\mathrm{eff},s}(f,v)
=
\langle\mathcal S_sf,\mathcal S_sv\rangle_{\rho_n}.
}
$$
For a residual $k\in\mathcal K$, the original state norm remains
$$
\|\mathcal S_sf+k\|_{\rho_n}^2
=
\|f\|_m^2+\|h_s(f)+k\|_{\rho_n}^2,
$$
including the mixed term inside the last square.

Finally, for $r<t<n$,
$$
\boxed{
\mathcal S_{r,n;s}
=
\mathcal S_{t,n;s}\,
\mathcal S_{r,t;s}^{(n)}.
}
$$
The middle section uses the **actual induced intermediate energy form and the marginal of the same fine vacuum**. The proof minimizes over those same fibers in two stages. It extends through every finite refinement chain.

This is where the newly inspected Split Zero minimum-section machinery has been applied to the Yang-Mills program.

## 4. What the checker actually checks

The new program passed **56 named exact checks and 17 named negative controls**. Ordinary and optimized Python produced byte-identical output; a fresh copied-source directory reproduced it. The previous PR #4 checker also passed its 181 checks separately. The complete records are included in the package. 

[Inspect the new verification record](sandbox:/mnt/data/yang_mills_research_control_verification.json)

The mathematical tests compare the section formula with an independently assembled constrained linear system, retain full mixed Gram matrices, verify refinement composition, and exercise both delayed and permanently invisible observations.

The negative controls include replacing the original Gram matrix by an identity matrix, dropping state-norm cross terms, substituting the uncorrected middle form, and converting an integrated score bound into a pointwise bound. Four additional command-line corruption tests were executed in both Python modes; each returned a nonzero exit status at its intended named failure.

A complete replay from the repository or archive root is:

```sh
python -B yang-mills/research-control/check.py \
  --verify-receipt yang-mills/research-control/verification.json
```

The receipt comparison binds the result to the actual proof, workflow, registry, and checker bytes. **The analytical proofs remain written arguments for review; these finite tests do not certify them as formal proofs.** No new Lean run or peer-CI replay was claimed.

## 5. The recorded continuation point

The next selected quantity is now explicit:
$$
\boxed{
(\kappa_nb)^2
\left\langle
T^*Xf,(D+s)^{-1}T^*Xv
\right\rangle_{\rho_n}.
}
$$
The intended calculation compares this actual response with the original kinetic form and the restored state metric on growing physical observation families, retaining every residual energy in the refinement composition.

The present work has not evaluated those interacting-vacuum response integrals or established a positive continuum mass lower bound. It has supplied a local estimate and an exact refinement mechanism through which that quantitative investigation can proceed.

The workflow, source intake, proofs, tests, and next calculation are now available to later sessions and Codex on the PR branch. No Codex job was started, and no research process is running between sessions.
