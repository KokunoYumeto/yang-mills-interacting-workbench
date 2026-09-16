# Independent bounded audit: gauge-native physical gap and spatial return

Date: 2026-09-16.

## Claim and primary verdict

The selected claim is the analytical implication from the written, absolutely convergent, gauge-invariant logarithmic-vacuum coefficient construction to the physical spectral gap of the original finite-box Hamiltonian, and then to the physical gap of the explicitly constructed fixed-spacing infinite-volume semigroup. The selected finite-box statement is SECOND_SOURCE.md R10:

\[
\Delta_L\ge\frac{3\kappa}{2}\bigl(1+\sqrt{P_2(\xi)}\bigr),\qquad
P_2(\xi)=1-\frac{256}{3}\xi+\frac{10720}{9}\xi^2,
\]
\[
L\ge2,\quad a,g>0,\quad\kappa=2g^2/a,\quad\xi=1/(4g^4),
\quad0<\xi\le\alpha=\frac3{4(32+\sqrt{354})}.
\]

The selected spatial statement is R14 for the generator and measure actually constructed by SPATIAL_RETURN.md, at fixed original \(a,g\):

\[
A_\infty\big|_{L^2_{\rm phys}(\nu)\cap1^\perp}
\ge\frac{3\kappa}{2}\bigl(1+\sqrt{P_2(\xi)}\bigr).
\]

**Primary verdict for this selected implication: proved as written.** This is a bounded mathematical audit of the explicit analytical inference, not a certification of every statement or fixture in the delivered package. No concrete analytical failure was found in that inference. In particular, it would be incorrect to classify the physical gap argument as merely extrapolating from a finite spin census or a finite coefficient matrix: the written proof treats every smooth physical eigenfunction and returns to the original Hilbert form. This report does not change any repository theorem status.

The following are outside this verdict: the four-dimensional continuum problem; claims of literature priority; every predecessor response error constant; exact replay of the 240-by-240 integer certificate; and the primary-source comparison in BAND_AND_CERTIFICATE.md B8. The files expressly leave the continuum problem unevaluated. No missing continuum theorem is silently supplied here.

## Source identity and method

All paths below are relative to:

`yang-mills/`.

The main four files were read in full with numbered lines. Relevant precursor norm, vacuum, form, conditional-kernel, and local-density passages were also read. The package's archived workflow instructions were treated as historical evidence, not as authority to perform remote publication or new research.

| Source | SHA-256 |
|---|---|
| `continuations/20260915-gauge-native-band/RESEARCH_NOTE.md` | `c24f5235b8c25daa1ee20fb81a13d8db94b88cb99b298ac7d10c8b4e5faafebd` |
| `continuations/20260915-gauge-native-band/SECOND_SOURCE.md` | `044279aa33cc6a53ea933ebe0aa903741653b4964883d7ea40b14b6bf5b9ff14` |
| `continuations/20260915-gauge-native-band/SPATIAL_RETURN.md` | `b7c24b984cf19ac793ae6df532bfa9fb9db98d6319e1a02bb3b92607366f626e` |
| `continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md` | `0e02c37b3ecc51f04d2f3c18cca686cc96bc7a8b5fd3bb467b143970a02d7887` |
| `continuations/20260915-uniform-gap-zero-shift/RESEARCH_NOTE.md` | `83d4de98b7b3e5de85efd747f56f1a42261cc55570e419c0d8fe62ccab93bad8` |
| `continuations/20260915-actual-loop-moments/RESEARCH_NOTE.md` | `0ac4afbec39b2e878d5555af85a86803d9ba6ac5505dc7817f231e5533c0dd2b` |

Skill used: `mathbox:proof-audit`; relevant checklist portions: logic and typing, representation and symmetry, computation-dependent claims, and external sources. An additional read-only subagent independently inspected SPATIAL_RETURN.md S10–S13 and its supporting S5–S6, and SECOND_SOURCE.md R4, without being given a proposed defect or substitute model. That check reported no concrete failure. Agreement is not treated as mathematical evidence in place of the derivations below.

## Objects, norms, and exact return maps

The finite graph consists of the vertices \(\{-L,\ldots,L\}^3\), all positively oriented contained nearest-neighbor links, and all contained elementary faces. The Hilbert space before restriction is \(L^2(SU(2)^{E_L},dU)\) with product Haar probability; the physical subspace is fixed by the original vertex gauge action. The original operator is

\[
H_L=\kappa K_L+\kappa\xi\sum_p(2-W_p),\qquad
K_L=-\sum_{e,\alpha}X_{e,\alpha}^2.
\]

Its finite compact-group operator/form domains are respectively \(H^2\) and \(H^1\), restricted to invariant functions in the physical case. The actual positive unit vacuum \(\psi_L\) supplies \(\rho_L=\psi_L^2\). Multiplication by \(\psi_L\) is the unitary map from \(L^2(\rho_LdU)\) to the original Haar Hilbert space. Its inverse divides by \(\psi_L\). The transported form is exactly

\[
q_{\mathcal A_L}(f,h)=\kappa\int\rho_L\sum_{e,\alpha}
\overline{X_{e,\alpha}f}X_{e,\alpha}h\,dU.
\]

These assertions are at gauge-native RESEARCH_NOTE.md lines 7–30. The positive-vacuum construction retaining the energy scalar is lines 204–219; it is not a change of physical measure made without a map.

For original product-spin labels, \(c(j)=\sum_ej_e(j_e+1)\) and \(A_j=d_j\int f\pi_j^*dU\), so that \(f=\sum_j\operatorname{Tr}(A_j\pi_j)\). The auxiliary spaces used in the spectral inference are

\[
X_0=\{f:\ A_0=0,\ \sum_{j\ne0}\|A_j\|_1<\infty\},\qquad
Y_0=\{f:\ A_0=0,\ \sum_{j\ne0}c(j)\|A_j\|_1<\infty\}.
\]

Here \(\|\cdot\|_1\) is the trace norm of the full coefficient matrix, including the original \(d_j\). The local source norm is a different norm on labelled coefficient families:

\[
\|v\|_{\mathrm{loc},1}
=\max_e\sum_{S\ni e}\sum_{j\ne0}c(j)\|A_{S,j}\|_1.
\]

The support label \(S\) contains the active spin support and is retained after cancellation. None of these norms is identified with the physical \(L^2\) norm. The finite-box total \(c\)-weighted coefficient sum is at most \(|E_L|\|v\|_{\mathrm{loc},1}\); that factor is used for finite-box regularity, not for the uniform spectral estimate.

The exact map from centered-vacuum functions to Haar-mean-zero functions is

\[
f\longmapsto Q_Hf,\qquad
y\longmapsto y-\langle y\rangle_{\rho_L}.
\]

On their respective centered domains these maps are inverses. They intertwine \(\mathcal A_L\) with \(\kappa K_L-2\kappa Q_H\sum_i(X_iv)X_i\). This is the decisive bridge, given explicitly at RESEARCH_NOTE.md lines 242–256. No volume-uniform bound on the norms of those inverse maps is needed for the eigenvalue exclusion argument.

## Dependency graph and obligation matrix

The audited chain is:

1. Vertex invariance implies the incident-spin inequalities G5; the cubic graph then gives \(c(j)\ge6j_e\), and every nonconstant physical block has \(c(j)\ge3\).
2. The full coefficient product inequality and original generator bounds imply G13 and G23, retaining all output irreducibles and union labels.
3. The original first and second sources give the positive majorant R7; the endpoint tail R9 proves convergence also at \(\alpha\).
4. Finite-box second-derivative summability identifies the assembled positive eigenfunction with the actual vacuum, including \(E_{0,L}\).
5. G23 plus the inverse mean-change map gives an exclusion interval for every physical eigenfunction; complete compact spectral resolution gives R10 on the full physical form domain.
6. Interior drift-row summability constructs the actual semigroup volume limit. Fourier norm dissipation gives uniform mixing and a coupling modulus. The endpoint is reached by the modulus, without assigning a finite derivative row there.
7. Uniform cylinder-semigroup convergence and weak vacuum-measure convergence pass the finite physical \(L^2\) estimate to R14; gauge averaging gives density in the complete physical Hilbert space.

| Obligation | Result | Precise location / scope |
|---|---|---|
| Physical spin restriction and free spectral minimum | Passed | RESEARCH_NOTE.md 52–89; includes all physical blocks, not a sampled spin range |
| Complete Fourier multiplication/derivative estimates | Passed | RESEARCH_NOTE.md 111–145; predecessor U7–U14 at 112–209 |
| Original coefficient source and endpoint convergence | Passed | RESEARCH_NOTE.md 158–219; SECOND_SOURCE.md 7–123 |
| Auxiliary-to-physical eigenfunction return | Passed | RESEARCH_NOTE.md 229–280; reconstruction below |
| No missing volume factor in spectral inequality | Passed | Its relative drift bound uses an edge anchor; regularity is only needed separately for each finite volume |
| Infinite-volume dynamics and mixing | Passed | SPATIAL_RETURN.md 110–185 and 250–333 |
| Endpoint extension without divergent row bound | Passed | SPATIAL_RETURN.md 335–398; SECOND_SOURCE.md 152–176 |
| Physical Hilbert-space gap passage | Passed | SPATIAL_RETURN.md 187–205; original finite gap is applied before taking limits |
| Band contour and all-order remainder, as written analytical argument | Passed in bounded inspection | BAND_AND_CERTIFICATE.md 7–99, 243–264; no rank-to-continuum inference |
| All entries of the integer L=2 certificate | Out of scope for execution | No checker or certificate was executed in this audit |
| External planar-paper comparison | Out of scope | BAND_AND_CERTIFICATE.md 308–369 is corroboration, not an input to R10/R14 |
| Four-dimensional continuum conclusion | Out of scope; source explicitly does not assert it | SECOND_SOURCE.md 181–185; SPATIAL_RETURN.md 230–248, 400–404 |

## Decisive analytical reconstruction

### 1. The original gauge restriction really improves the drift constant

For a nonzero physical Fourier block, a vertex invariant intertwines each incident spin into the tensor product of the others, giving \(j_e\le\sum_{f\ni v,f\ne e}j_f\). For an edge with endpoints \(u,v\), let \(J_1\) be the spin sum on other edges incident on those endpoints. Then \(J_1\ge2j_e\). On the cubic graph the other endpoints of these edges are distinct. Summing the same vertex inequality there gives \(J_1\le2J_2\), where \(J_2\) counts the remaining neighboring edges once. Consequently \(\sum_fj_f\ge j_e+J_1+J_2\ge4j_e\). Since \(j(j+1)\ge(3/2)j\) for every nonzero half-integer spin, \(c(j)\ge6j_e\). This proof uses the stated open cubic graph, so it does not assume a graph inequality valid on arbitrary graphs.

For a source satisfying \(\|v\|_{\mathrm{loc},1}\le r\),

\[
\sum_{S\ni e,j}j_e\|A_{S,j}\|_1\le r/6.
\]

The coefficient product and derivative inequalities therefore give, for arbitrary scalar \(f\in Y_0\),

\[
\left\|Q_H\sum_i(X_iv)(X_if)\right\|_{X_0}
\le3\sum_k\|A_k(f)\|_1\sum_e k_e\frac r6
\le\frac r3\|f\|_{Y_0}.
\]

The last inequality uses \(\sum_ek_e\le(2/3)c(k)\), which holds on the full scalar space. Thus the source needs physical gauge invariance, but \(f\) need not be physical for this particular drift estimate. With \(\epsilon=2r/3\), the full perturbation has norm at most \(\kappa\epsilon\) from \(Y_0\) to \(X_0\). This distinguishes the hypotheses needed on the two factors.

### 2. Every physical eigenfunction is covered

Let \(\mathcal A_Lf=\lambda f\), \(\lambda>0\), in the physical Hilbert space. The compact smooth elliptic problem makes \(f\) smooth. For each fixed finite box its Fourier coefficients belong to \(Y_0\); no uniform-in-volume regularity constant is required. Set \(y=Q_Hf\ne0\). The exact mean-change map gives

\[
(\kappa K_L-\lambda)y=-V_\xi y.
\]

For \(0<\lambda<3\kappa\), every physical coefficient has \(c\ge3\), and

\[
\sup_{c\ge3}\frac{c}{\kappa c-\lambda}
=\frac3{3\kappa-\lambda}.
\]

Hence

\[
\|y\|_{Y_0}
\le\frac{3\kappa\epsilon}{3\kappa-\lambda}\|y\|_{Y_0}.
\]

Because \(y\ne0\), this excludes \(0<\lambda<3\kappa(1-\epsilon)\). Eigenvalues already at least \(3\kappa\) satisfy the same lower bound. The full compact spectral expansion then gives the form inequality for every physical \(H^1\) vector centered in the actual vacuum measure. Substituting \(r_2=(3/4)(1-\sqrt{P_2})\) gives R10. This is an exact spectral argument on the original operator, not an estimate only on the coefficient window.

### 3. The endpoint spatial argument does not require a hidden finite derivative row

Write the actual finite evolution as \(T_L(t)F=c(t)+y(t)\), where \(c\) is its Haar mean. Its smooth finite solution is differentiable in \(X_0\), and

\[
y'=-\kappa K_Ly-V_\xi y.
\]

For \(y\in Y_0\), dominated convergence applied to the individual coefficient norms gives

\[
\left.\frac d{dh}\right|_{h=0+}\|(I-h\kappa K_L)y\|_{X_0}
=-\kappa\|y\|_{Y_0}.
\]

The domination is \(\kappa c(j)\|A_j\|_1\). The perturbation estimate proves

\[
D^+\|y(t)\|_{X_0}\le-\kappa(1-\epsilon)\|y(t)\|_{Y_0}.
\]

The same coefficient estimate *before* removing the constant coefficient bounds \(|c'|\le\kappa\epsilon\|y\|_{Y_0}\). Integrating both inequalities reconstructs the vacuum mean and yields

\[
\|T_L(t)F-\langle F\rangle_{\rho_L}\|_\infty
\le\frac{\|Q_HF\|_{X_0}}{1-\epsilon}
e^{-\kappa c_*(1-\epsilon)t},
\]

with \(c_*=3\) for physical \(F\) and \(3/4\) on the scalar space. A fixed cylinder has the same original Fourier norm in all larger boxes. That fact supplies the volume-independent prefactor.

For interior couplings the full derivative matrix has a finite row sum, so the finite SDE comparison constructs the uniform cylinder-semigroup volume limit on compact time intervals. The displayed mixing estimate then makes the entire sequence of vacuum expectations Cauchy: first send the box sizes to infinity at fixed \(t\), then send \(t\) to infinity. Duhamel's formula, the same full coefficient drift estimate, and integrated \(Y_0\) dissipation give

\[
\sup_{t\ge0}\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
\le\frac{\epsilon_2(\eta)-\epsilon_2(\xi)}{1-\epsilon_2(\xi)}
\|Q_HF\|_{X_0}.
\]

For \(\eta=\alpha\), the scalar quotient is
\(\sqrt{P_2(\xi)}/(1+\sqrt{P_2(\xi)})\to0\). Inserting an interior coupling between two endpoint finite-volume evolutions proves that the endpoint family is Cauchy. This uses the convergent original source and its coupling modulus, not the divergent endpoint derivative series. Finite reversibility, uniform semigroup convergence, weak measure convergence, and density of gauge-averaged cylinders then give the physical \(L^2\) inequality R14.

## Concrete non-load-bearing document defects

These are transcription/cross-reference defects, not missing mathematical implications:

1. `RESEARCH_NOTE.md:30` says the direct positive-vacuum/form proof is in “G8.” The proof is at G20–G21, lines 204–219. Equation G8 is the free physical Casimir spectrum.
2. `SPATIAL_RETURN.md:3` and `:228` call the later additions “S10–14” as sections; equations S10–S14 elsewhere already denote conditional/drift statements. The later section titles are numbered 10–14 and the endpoint calculation itself is at equations S31–S35. Readers should use the section locator, not the earlier equation labels.
3. `BAND_AND_CERTIFICATE.md:360–362` has malformed TeX in the summation subscript of B32 (`p\ {` / `m in\ plane}\p\sim q`). The preceding paragraph and the left side determine the intended sum over plaquettes in the fixed plane sharing an edge with \(q\). The finite and infinite spectral gap derivations do not depend on this rendering.

## Computation/source checks and limitations

Commands used here were read-only PowerShell `Get-Content` with line enumeration, `rg` searches, and `Get-FileHash -Algorithm SHA256`. No Lean, Lake, Elan, external source program, or supplied Python checker was run by this audit agent. The Python checker was inspected sufficiently to locate its actual scope; its final result explicitly says “Exact finite algebra, integer graph/inertia calculations and rational evaluation of written analytic estimates” and states that the analytic proofs are not formally certified (`verify.py:775–782`). That disclosure is accurate as to what such a checker can establish.

The local-density input used for the nonzero Wilson vector was traced past the uniform-gap note's U54 to `20260915-actual-loop-moments/RESEARCH_NOTE.md:107–134,420–434`: a maximum-principle argument proves \(\sup|X_e\log\rho|\le16\xi\) at all positive couplings, and the original group diameter \(2\pi\) gives the four-link marginal lower bound \(e^{-128\pi\xi}\). This check avoids importing a small-coupling bound into the enlarged domain without examining its stated range.

No external literature theorem is being imported from BAND_AND_CERTIFICATE.md B8 into the selected claim. Its planar paper comparison was not independently fetched or verified. Standard compact elliptic regularity, Peter–Weyl decomposition, and compact self-adjoint spectral resolution are the analytical background used in the written proof; this bounded audit checked their stated finite compact-manifold setting and their role, rather than reconstructing those background theories.

## Remaining work and strongest safe consolidation wording

No smallest missing implication was identified in the selected coefficient-to-fixed-spacing-physical-gap chain. The independent spatial cross-check reached the same bounded conclusion. This is not a claim that an exhaustive proof audit of the entire historical package has been completed.

A safe consolidation description is: “Written strong-coupling results for the original SU(2) lattice Hamiltonian, including an explicit volume-uniform physical gap, its fixed-spacing infinite-volume return, and a finite-band calculation with an analytic remainder; exact finite fixtures and execution receipts are tracked separately. The four-dimensional continuum limit remains unevaluated.”

The source's retained running path \(a_n=a_0 2^{-n}\), \(g_n^2=1/c_n\), \(c_n=g_0^{-2}+\beta n\log2\) with \(\beta>0\) eventually leaves the admissible domain. In particular the displayed strong-coupling theorem cannot be presented as a continuum mass-gap solution. This is an explicit limitation already proved and stated by the sources, not a newly invented condition.
