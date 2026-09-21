# Fifth-reference source, physical spectrum and heat estimates

The interacting SU(2) lattice vacuum can be written as an exponential. Its logarithm satisfies a nonlinear equation whose first coefficients are exactly computable. A finite coefficient list alone does not control the vacuum: the remaining infinite equation must also be solved. This continuation evaluates the complete fifth-order reference and its residual, constructs a convergent correction including the endpoint, and returns that correction to the original physical Hamiltonian. The stronger source estimate then enlarges the domain of the heat bounds and sharpens the energy comparison with the entire complementary physical space.

Start with the [24-page reader](reader/yang_mills_fifth_reference_20260921.pdf): it introduces the original Hamiltonian, explains each result and its domain, and includes both complete proof manuscripts. The [standalone LaTeX](reader/yang_mills_fifth_reference_20260921.tex), [reader source bundle](reader/yang_mills_fifth_reference_20260921_reader_sources.zip) and [build instructions](reader/BUILDING_READER.md) make the exposition reproducible.

The two complete mathematical arguments are [the fifth-reference construction](package/workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md) and [heat flow and the complete complement](package/workbench/yang-mills/continuations/20260921-fifth-reference-return/HEAT_AND_COMPLEMENT.md). Equation labels below refer to these manuscripts. The [complete cumulative archive](archives/yang_mills_cumulative_20260921_fifth_reference.zip) and [all extracted sources](package/) preserve the earlier work as well as this continuation. The [preceding heat and volume edition](../20260921/) remains available separately. This edition's archival identifier is [10.5281/zenodo.22883643](https://doi.org/10.5281/zenodo.22883643).

## The original problem and the fifth reference

For an open cubic box with vertices $\{-L,\ldots,L\}^3$, $L\ge2$, every link carries an SU(2) matrix. The physical Hilbert space is the gauge-invariant part of the original product-Haar $L^2$ space, including the boundary gauge transformations. If $W_p$ is the trace around an oriented elementary plaquette and $M$ is the number of plaquettes, the Hamiltonian is

$$
H_L=\kappa\left[K_L+\xi\left(2M-\sum_pW_p\right)\right],\qquad
K_L=-\sum_{e,a}X_{e,a}^2,\qquad
\kappa=\frac{2g^2}{a},\quad \xi=\frac1{4g^4}.
$$

Here $a>0$ is the lattice spacing. Put $P_Hf=\int f\,dU$, $Q_H=I-P_H$, $\Gamma(f,h)=\sum_{e,a}(X_{e,a}f)(X_{e,a}h)$ and $B(f,h)=K_L^{-1}Q_H\Gamma(f,h)$. The zero-Haar logarithmic source satisfies $v=\xi v_1+B(v,v)$, with $v_1=\frac13\sum_pW_p$. Its fifth reference is $q_5=\sum_{i=1}^5\xi^iv_i$.

The new coefficient estimates retain every original spin channel, trace-word orientation and anchored coordinate transport. Equations F11–F25 give the finite constructions: 662 fifth-source representatives, 124,864 anchored multisets, 6,240 projection constraints and 5,726 rational primal/dual certificates. For a trace word with $\ell$ independent fundamental occurrences and $2k$ cyclic orientation changes, its coefficient matrix has trace norm $2^{\ell-k}$; the proof and actual diagonal-group pullback are in F11–F13. The resulting bounds are

$$
\|v_5\|_{\rm loc}<2476866,\qquad m(v_5)<1638684,\qquad t(v_5)<190128.
$$

These are auxiliary coefficient bounds, with their precise weighted sums defined in F6. They do not replace the physical state or energy inner products.

## A complete correction, not a truncated vacuum

Let $(m_i,t_i)$ be the exact proved upper bounds in F26 and set

$$
b_{ij}=3(m_it_j+m_jt_i),\quad
\ell_5(x)=\sum_{i=1}^5(m_i+4t_i)x^i,\quad
\delta_5(x)=\sum_{\substack{1\le i,j\le5\\i+j\ge6}}b_{ij}x^{i+j},\quad
\mathscr D_5(x)=(1-\ell_5(x))^2-\frac83\delta_5(x).
$$

All residual degrees six through ten are included in $\delta_5$, not discarded. The first positive root $\alpha_5$ satisfies

$$
0.018424953576117616681<\alpha_5<0.018424953576117616682.
$$

Equations F27–F34 construct the full inverse of $I-2B(q_5,\cdot)$ and a convergent nonlinear series for $w=v-q_5$, with

$$
\|w\|_{\rm loc}\le\frac34\left(1-\ell_5(x)-\sqrt{\mathscr D_5(x)}\right),
\qquad x=|\xi|\le\alpha_5.
$$

The endpoint is included by an explicit Catalan-series tail tending to zero; no strict contraction at the endpoint is assumed. Substituting the completed source returns the actual positive vacuum and its scalar energy,

$$
\psi_L=\frac{e^v}{\left(\int e^{2v}dU\right)^{1/2}},\qquad
E_{0,L}=2\kappa M\xi-\kappa P_H\Gamma(v,v).
$$

For the complete physical excitation spectrum, F35–F42 prove

$$
\Delta_L\ge\kappa d_5(\xi),\qquad
d_5(x)=\frac32(1+\sqrt{\mathscr D_5(x)})+
\sum_{i=1}^5\left(\frac32m_i-6t_i\right)x^i,
$$

for every $L\ge2$, $a>0$ and $0<\xi\le\alpha_5$. Thus the exact coupling threshold is $g^2\ge1/(2\sqrt{\alpha_5})$, approximately $3.6835519839857273$. In particular, $g^2\ge3.7$ gives $\Delta_L>1.6207\kappa$, and $g^2\ge4$ gives $\Delta_L>1.9068\kappa$. The whole physical form domain, not only a finite trial band, is the domain of this bound.

## What this changes for heat flow

Let $A_L=H_L-E_{0,L}$ on the centered physical space, $r_p=(W_p-\langle W_p\rangle_{\psi_L^2})\psi_L$, and

$$
\widehat C_{pq}(\tau;\xi)=\langle r_p,e^{-\tau A_L/\kappa}r_q\rangle,
\qquad \tau=\kappa t.
$$

The original matrices $C_0,C_2,C_4$ are unchanged. The infinite remainder now obeys, for all original boxes and all $\tau\ge0$,

$$
\left\|\widehat C(\tau;\xi)-C_0(\tau)-\xi^2C_2(\tau)-\xi^4C_4(\tau)\right\|_{\rm row}
\le\frac{67896}{169}e^{-13\tau/8}
\frac{(55|\xi|)^6}{1-(55|\xi|)^2},\qquad |\xi|<\frac1{55}.
$$

The row norm is the maximum absolute row sum. The circle $1/55$ is larger than the preceding $3/256$ circle. This is control of the complete heat tail, not a new claim that additional heat coefficients were calculated. Equations H1–H13 establish the operator domain, mean, semigroup and analytic bound. Local coefficient agreement and these tails give the fixed-spacing spatial limit in H34.

## Relaxation into all remaining physical states

Write $R$ for the map whose columns are $r_p$, and $\Phi=\kappa A_L^{-1}R$. The original Grams are $G_0=R^*R$, $G_1=R^*\Phi$ and $G_2=\Phi^*\Phi$; the energy is $E=\kappa G_1$. Let

$$
P=\Phi G_2^{-1}\Phi^*,\quad Q=I-P,\quad B_\Phi=QR,\quad D_Q=QA_LQ.
$$

The proof establishes $\operatorname{Dom}D_Q=\operatorname{Dom}A_L\cap Q\mathcal H_0$, self-adjointness and the inverse. Minimizing the energy of $\Phi c+h$ over every $h\in Q\mathcal H_0$ in the form domain gives

$$
E_{\rm full}=E-\kappa^2B_\Phi^*D_Q^{-1}B_\Phi,\qquad
G_{\rm full}=G_2+\kappa^2B_\Phi^*D_Q^{-2}B_\Phi.
$$

The improved heat remainder controls both corrections. For every original box and $g^2\ge13$,

$$
\frac{1999}{2000}E\prec E_{\rm full}\preceq E,\qquad
G_2\preceq G_{\rm full}\prec\frac{2001}{2000}G_2.
$$

For $g^2\ge16$ the respective factors improve to $24999/25000$ and $25001/25000$. The strict comparisons are quadratic-form statements on nonzero coefficient vectors. H14–H30 retain the signed time weight in the leakage Gram, all mixed terms and the original metrics. H31–H34 carry the result to support quotients, finite physical heat horizons and the complete complementary space of the fixed-spacing spatial limit.

## Sources, verification and scope

The [source proof and evidence section](package/workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md#f8-sources-and-evidence) distinguishes the written analytical arguments from finite exact-arithmetic certificates. The supplied execution history records 30 replay executions, including 14 corruption rejections; those remain the source's executions, not silently relabelled as fresh runs during publication. Independent publication-check receipts accompany this edition separately.

The [publication review](checks/INTAKE_REVIEW.md) and [machine-readable verification](checks/PUBLIC_VALIDATION.json) record the fresh scope. Both ordinary and optimized fast replay passed 51 named checks and 11 false-formula controls, including 316 integer tensor calculations and the 124,864-anchor assembly. The manifest passed before and after, and source bytes were unchanged. The full polynomial/dual-certificate auditor and coefficient producer were not rerun; their supplied execution logs were checked for exact hash consistency. Peak sampled checker memory was 214 MiB with one process. No Lean or independent external analytical certification is claimed.

To repeat the non-mutating checks from the extracted cumulative archive, run `python -B verify_cumulative.py`; then, in `workbench/yang-mills/continuations/20260921-fifth-reference-return`, run `python -B verify.py --verify-receipt verification.json`. Repeat with `python -O -B` to check independence from Python assertions. Full producer replay is a separate, more expensive operation and should use a disposable copy; it is not needed to read the proofs.

The exponential-vacuum and character/Casimir framework is credited to D. Schütte, Zheng Weihong and C. J. Hamer, [*The Coupled Cluster Method in Hamiltonian Lattice Field Theory*](https://arxiv.org/abs/hep-lat/9603026), §§2–5. The compact Fourier-algebra antecedent is P. Eymard, *L'algèbre de Fourier d'un groupe localement compact*, Bull. Soc. Math. France 92 (1964), 181–236. Semigroup generation uses G. Lumer and R. S. Phillips, *Dissipative operators in a Banach space*, Pacific J. Math. 11 (1961), 679–698, after the explicit domain and range checks.

Levent Alpöge's originating Jacobian example and the separate S6 construction are explicitly credited in the [workbench attribution clarification](../../../ATTRIBUTION.md), with their actual uses in earlier material-tensor and magnetic-background calculations. They are not presented as direct hypotheses of the fifth-source calculation. Tao's and Engel's expositions retain separate credit.

All results above retain fixed spacing and a stated coupling domain. On the standing path $a_n=a_0 2^{-n}$, $g_n^2=1/c_n$ and $c_n=g_0^{-2}+\beta n\log2$, the source domain requires $c_n\le2\sqrt{\alpha_5}$ and the heat circle requires $c_n<2/\sqrt{55}$. For $\beta>0$ the path eventually leaves both. These estimates do not establish a nontrivial four-dimensional continuum field or a finite positive continuum mass.

This is part of the open PolyClank workbench. To contribute, fork the repository, add your mathematical argument or reproducible calculation with clear exposition, and open a pull request; [the contribution guide](../../../CONTRIBUTING.md) explains the procedure. Existing sources and their attribution remain visible alongside later corrections.
