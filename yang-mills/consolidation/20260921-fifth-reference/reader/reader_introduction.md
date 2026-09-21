---
title: The fifth reference in SU(2) lattice Yang-Mills theory
subtitle: A convergent source correction, enlarged heat bounds, and the full physical complement
author: KokunoYumeto
date: 21 September 2026
---

# Reading the fifth-reference continuation

The fifth reference is an explicitly calculated approximation to the logarithm of the interacting vacuum. Its purpose is to control the whole nonlinear remainder and then recover statements about the original Hamiltonian: a physical spectral gap, heat correlations, and the energy change when an observed family of states can mix with every other physical state. The two manuscripts collected here carry out that programme on a stated strong-coupling domain, uniformly in spatial volume.

The source construction reaches the endpoint $\alpha_5\approx0.018424953576117616681$, corresponding to $g^2\geq1/(2\sqrt{\alpha_5})\approx3.683551984$. Its heat estimate uses the strictly interior circle $R=1/55$. At the stronger benchmark $g^2\geq13$, relaxation into the complete physical complement changes the original energy and state metrics by less than one part in two thousand; at $g^2\geq16$, both changes are less than one part in twenty-five thousand. These are estimates at fixed lattice spacing. No four-dimensional continuum Yang-Mills construction or continuum mass gap follows from them.

This introduction explains the objects, domains and uses of the results. Appendix A reproduces the complete fifth-reference proof, with its original labels F1-F42. Appendix B reproduces the complete heat and complement proof, with labels H1-H34. The introduction writes $\alpha_5$ for the endpoint called $\alpha$ in those sources. Their full mathematical text and citations are retained, including statements of what is not established.

## The original Hamiltonian and its physical pairing

Fix an integer $L\geq2$. The vertices are $\{-L,\ldots,L\}^3$, the links are all contained positive nearest-neighbour edges, and $\mathsf P_L$ is the set of contained elementary plaquettes. A link carries $U_e\in\mathrm{SU}(2)$. Physical functions are invariant under the gauge transformations at every original vertex, including boundary vertices. Their Hilbert space is the invariant subspace of product-Haar-probability $L^2$.

The elementary observable and original derivatives are

$$
W_p=\operatorname{tr}\!\left(U_i(n)U_j(n+e_i)U_i(n+e_j)^{-1}U_j(n)^{-1}\right),
\qquad T_a=-i\sigma_a/2,
$$

$$
X_{e,a}f=\left.\frac{\partial}{\partial t}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
\qquad K=-\sum_{e,a}X_{e,a}^2.
$$

Writing $M=|\mathsf P_L|$ and $S=\sum_pW_p$, the Hamiltonian is

$$
H_L=\kappa K+\kappa\xi(2M-S),\qquad
\kappa=\frac{2g^2}{a},\qquad \xi=\frac1{4g^4},\qquad a,g>0.
$$

Its operator and form domains are the physical parts of $H^2$ and $H^1$ on the compact product of link groups. Let $\psi$ be its positive unit ground vector, $E_0$ its energy, $\rho=\psi^2$, and $A=H_L-E_0$. The physical energy identity is

$$
q_A(\psi f)=\kappa\int\rho\sum_{e,a}|X_{e,a}f|^2\,dU.
$$

This identity retains the interacting weight $\rho$ and the original Haar measure. The coefficient norms used to construct $\psi$ are auxiliary analytic tools; they do not replace this pairing.

The exponential vacuum and character/Casimir framework has a human antecedent in Schütte, Zheng Weihong and Hamer [1], especially Sections 2-5. Appendix A states the conversion from their convention: $g_C=2^{3/4}g$, $H_{\mathrm{ours}}=\sqrt2H_C+2\kappa\xi MI$, and their commutator derivative is $iX$.

## Why the fifth coefficient improves the source domain

Let $P_Hf=\int f\,dU$, $Q_H=I-P_H$, and define

$$
\Gamma(f,h)=\sum_{e,a}(X_{e,a}f)(X_{e,a}h),\qquad
B(f,h)=K^{-1}Q_H\Gamma(f,h).
$$

The logarithmic source satisfies $v=\xi v_1+B(v,v)$, with $v_1=S/3$. Each Fourier coefficient carries its original finite edge support. The local coefficient norm weights a physical representation block by its Casimir $c_j=\sum_ej_e(j_e+1)$; the two additional bounds $m(v)$ and $t(v)$ weight its total spin and its spin at a specified edge. Their precise definitions are F4-F6. Gauge singlet constraints give $c_j\geq6j_e$ and $c_j\geq3$ for a nonconstant physical block. Consequently

$$
\|B(f,h)\|_{\mathrm{loc}}
\leq3\{m(f)t(h)+m(h)t(f)\}
\leq\frac23\|f\|_{\mathrm{loc}}\|h\|_{\mathrm{loc}}.
$$

The compact-group coefficient argument proves the multiplication and derivative estimates directly; Eymard [2] is its Fourier-algebra antecedent. The finite calculation then improves the inputs to this estimate by resolving original signed spin channels before taking absolute values.

The preserved fifth catalogue has 662 representatives, 124,864 anchored multisets, and 14,063 rational trace-monomial terms. On 321 representatives, every face is distinct and no link occurs more than twice. There the signed rational recurrence F16 resolves all admissible spin-zero and spin-one channels on repeated links. Complete polynomial identities compare the channel formula with the original fifth coefficient. On the other 341 representatives, F22-F24 use the applicable lower-order channel bounds and full trace expressions. In particular, the distinct-face recurrence is not applied to links with three or more occurrences.

All 662 rows return to the original marked edge through their saved signed coordinate maps. The resulting uniform upward bounds are

$$
\|v_5\|_{\mathrm{loc}}<2476866,\qquad
m(v_5)<1638684,\qquad t(v_5)<190128.
$$

F25 gives the stronger exact rational bounds. F26 lists the five pairs $(m_i,t_i)$ used in the endpoint calculation. The finite dual certificates bound actual coefficient objectives; they do not assert that the physical coefficient masses attain a polytope maximum.

## A complete correction, including the endpoint

Set $q_5=\sum_{i=1}^5\xi^iv_i$ and $R_5=\xi v_1+B(q_5,q_5)-q_5$. The residual includes every term of degrees six through ten; F27 displays it in full. With $x=|\xi|$, define

$$
b_{ij}=3(m_it_j+m_jt_i),\qquad
\ell(x)=\sum_{i=1}^5(m_i+4t_i)x^i,
$$

$$
\delta(x)=\sum_{\substack{1\leq i,j\leq5\\i+j\geq6}}b_{ij}x^{i+j},
\qquad \mathscr D(x)=(1-\ell(x))^2-\frac83\delta(x).
$$

The first positive root of $\mathscr D$ is $\alpha_5$. The exact enclosures are

$$
0.018424953576117616681<\alpha_5<0.018424953576117616682,
$$

$$
3.683551983985727304439<\frac1{2\sqrt{\alpha_5}}
<3.683551983985727304440.
$$

For $|\xi|\leq\alpha_5$, the actual source linearization $L_5=I-2B(q_5,\cdot)$ has a convergent Neumann inverse. The correction $w=v-q_5$ solves $L_5w=R_5+B(w,w)$ and obeys

$$
\|w\|_{\mathrm{loc}}\leq w_*(x)
=\frac34\left(1-\ell(x)-\sqrt{\mathscr D(x)}\right).
$$

The Catalan expansion converges at $x=\alpha_5$ as well. Its explicit omitted-order estimate F32 decays at least as $(N+1)^{-1/2}$ at the endpoint. This is why the closed source disk includes its boundary even though a strict contraction estimate would not suffice there.

For real coupling, $\psi=e^{v+c_L}$ with $c_L=-\frac12\log\int e^{2v}dU$ gives the original positive ground vector. The same correction yields

$$
\Delta_L\geq\kappa d_5(\xi),\qquad
d_5(x)=\frac32\left(1+\sqrt{\mathscr D(x)}\right)
+\sum_{i=1}^5\left(\frac32m_i-6t_i\right)x^i.
$$

Here $\Delta_L$ is the gap of the whole physical Hamiltonian above its vacuum. F35-F37 show $d_5(x)>0$ throughout the closed interval and prove the corresponding weighted Poincaré inequality on the full physical form domain. For example, $g^2\geq4$ gives $\Delta_L/\kappa>1.9068$ and $\|v-q_5\|_{\mathrm{loc}}<0.005752$. The comparison between the approximate reference and the physical operator retains its scalar, multiplication and drift defects in F39-F40.

## The enlarged heat circle and what its remainder controls

For the centered plaquette states $r_p=(W_p-\langle W_p\rangle_\rho)\psi$, write

$$
\widehat C_{pq}(\tau;\xi)=\langle r_p,e^{-\tau A/\kappa}r_q\rangle,
\qquad \tau=\kappa t.
$$

The physical time is $t$. Appendix B constructs the full coefficient generator, its dense domain and its range, and the complex mean with its nonzero denominator. These are the hypotheses used for the Lumer-Phillips generation theorem [3]; a bound on a single inverse is not substituted for a heat estimate.

On the circle $R=1/55$, the fifth-source calculation gives $d_5(R)>13/8$ and $\chi(R)=1-d_5(R)/3<11/24$. The exact Haar selection rule and the returned mean give the volume-independent row estimate H11. Link-center symmetry makes the homogeneous connected heat even. Cauchy's formula therefore proves

$$
\left\|\widehat C(\tau;\xi)-C_0(\tau)-\xi^2C_2(\tau)-\xi^4C_4(\tau)\right\|_{\mathrm{row}}
\leq\frac{67896}{169}e^{-13\tau/8}
\frac{(55|\xi|)^6}{1-(55|\xi|)^2},
$$

for every $L\geq2$, $\tau\geq0$ and $|\xi|<1/55$, where $\|C\|_{\mathrm{row}}=\max_p\sum_q|C_{pq}|$. Column bounds agree by transpose symmetry. The coefficients $C_0,C_2,C_4$ are the unchanged complete heat coefficients of the earlier edition; the improvement here is the bound on their entire remaining tail.

The radius $1/55$ exceeds both the preceding volume-heat radius $3/256$ and the saved fourth-reference source endpoint $0.018104972231644127076$. It is strictly inside $\alpha_5$, so the heat statement has its own open domain. For real coupling it requires $g^2>\sqrt{55}/2$, whereas the source and physical-gap construction permits $g^2\geq1/(2\sqrt{\alpha_5})$.

## Original moments and the complete physical complement

Let $R_{\mathrm{col}}c=\sum_pc_pr_p$ and $\Phi=\kappa A^{-1}R_{\mathrm{col}}$. On the centered physical space,

$$
G_0=R_{\mathrm{col}}^*R_{\mathrm{col}},\quad
G_1=\kappa R_{\mathrm{col}}^*A^{-1}R_{\mathrm{col}},\quad
G_2=\Phi^*\Phi,\quad E=\Phi^*A\Phi=\kappa G_1.
$$

These distinguish forcing-state norm, inverse-energy response and the state norm of the response. For $k\geq1$, the spectral theorem gives

$$
G_k=\frac1{(k-1)!}\int_0^\infty\tau^{k-1}\widehat C(\tau;\xi)\,d\tau.
$$

The leakage trial $J=(R_{\mathrm{col}}-3\Phi)^*(R_{\mathrm{col}}-3\Phi)=G_0-6G_1+9G_2$ retains its signed time weight $9\tau-6$. Integrating its absolute value against $e^{-13\tau/8}$ gives the improved tail prefactor $5156090136/3570125$ in H18. Together with the full inherited degree-two and degree-four support sums, this supplies explicit widths for the original matrices, uniformly at boundary rows as well as in the interior.

The projection onto the response states and their coupling to the rest of the physical space are

$$
P=\Phi G_2^{-1}\Phi^*,\qquad Q=I-P,\qquad B_\Phi=QR_{\mathrm{col}}.
$$

For every centered physical form-domain vector $\Phi c+h$, $h\in Q\mathcal H_0$, its full energy includes the mixed term:

$$
q_A(\Phi c+h)=\kappa c^*G_1c
+2\kappa\operatorname{Re}\langle B_\Phi c,h\rangle+q_A(h).
$$

Let $d_{\mathrm{ph}}>0$ be a stated rational lower bound for $d_5(\xi)$ at the coupling benchmark. H25 proves that $D_Q=QAQ$ is self-adjoint on $\operatorname{Dom}(A)\cap Q\mathcal H_0$, with $D_Q\geq\kappa d_{\mathrm{ph}}I$. Minimizing over this entire complement gives

$$
\Phi_{\mathrm{full}}=\Phi-\kappa D_Q^{-1}B_\Phi,\qquad
E_{\mathrm{full}}=E-\kappa^2B_\Phi^*D_Q^{-1}B_\Phi,
$$

$$
G_{\mathrm{full}}=G_2+\kappa^2B_\Phi^*D_Q^{-2}B_\Phi.
$$

Let $P_R=R_{\mathrm{col}}G_0^{-1}R_{\mathrm{col}}^*$. The observed state fraction is $\|P_R\Phi c\|^2/\|\Phi c\|^2$ for $c\ne0$. Two improved benchmarks from §H5 are:

| Original coupling | Observed fraction exceeds | Energy loss below | State increase below |
|:--|--:|--:|--:|
| $g^2\geq13$ | $999/1000$ | $1/2000$ | $1/2000$ |
| $g^2\geq16$ | $9999/10000$ | $1/25000$ | $1/25000$ |

An energy loss below $\eta$ means $(1-\eta)E\prec E_{\mathrm{full}}\preceq E$; a state increase below $\eta$ means $G_2\preceq G_{\mathrm{full}}\prec(1+\eta)G_2$. These compare forms on the same coefficient space and are strict on nonzero coefficients. They are not entrywise quotients. The table holds for all $L\geq2$ and $a>0$. At $g^2\geq16$, H29 also bounds the original section-energy change by $1/20000$.

## Spatial limits, finite heat time, and the continuum boundary

The original source and heat recurrences preserve connected finite supports. When two boxes contain the same neighbourhood of the marked faces, their corresponding low-degree coefficients coincide. The remaining geometric tail gives full-sequence convergence of the local vacuum means and heat correlations at fixed $a,g$ with $\xi<1/55$. §H6 constructs the limiting physical state and self-adjoint generator and passes the gap and bounded moment operators to the infinite spatial lattice. At the benchmark couplings, the positive Gram lower bounds and the complete complementary minimization pass to this limit as well.

For a finite time $T$, the response $\Phi_T=(I-e^{-TA})\Phi$ has the explicit residual $A\Phi_T=\kappa R_{\mathrm{col}}-\kappa e^{-TA}R_{\mathrm{col}}$. If a signed determinant return has total absolute rank $\mathcal B$, H33 gives the physical choice

$$
T=\frac1{\kappa d_{\mathrm{ph}}}\log\left(1+\frac{2\mathcal B}{\eta}\right)
$$

for error at most $\eta>0$. The rank, physical time, mixed blocks and quotient-minimum fibers remain explicit.

The simultaneous shrinking-spacing path in §H7 is $a_n=a_0 2^{-n}$, $g_n^2=1/c_n$, $c_n=g_0^{-2}+\beta n\log2$, so $\xi_n=c_n^2/4$. Source inclusion requires $c_n\leq2\sqrt{\alpha_5}$; heat inclusion requires $c_n<2/\sqrt{55}$. For $\beta>0$ that path eventually leaves both domains. The fixed-spacing spatial limit therefore does not prove a positive finite continuum mass or a nontrivial smooth four-dimensional field. The sixth-source catalogue also remains absent from the delivered source chain.

## Human sources and the two upstream branches

The direct analytic antecedents used here are the exponential-vacuum/Casimir construction [1], the compact Fourier algebra [2], and the generator theorem [3]. The two manuscripts give their own source-domain, endpoint and physical-return arguments. Their finite exact checks support the declared algebraic identities and rational inequalities; they do not constitute an external analytic review or a formal verification of the infinite-dimensional passages.

Two separate earlier branches of the workbench credit Levent Alpöge. The Jacobian branch begins with his original announcement of a counterexample to global injectivity with constant nonzero Jacobian [4], which credits Akhil's question and Fable's work. Tao's later exposition [5] is a separate source. The $S^6$ branch begins with the claimed complex-threefold construction circulated by Alpöge with AI assistance [6]; Engel's exposition [7] separately credits that source. These constructions and their later coordinate calculations are distinct. Neither originating construction is invoked as a direct lemma in the fifth-source or heat-complement proofs reproduced here. The workbench's [attribution record](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/ATTRIBUTION.md) records the earlier points of use.

## References

1. D. Schütte, Zheng Weihong and C. J. Hamer, *The Coupled Cluster Method in Hamiltonian Lattice Field Theory*, 1996, Sections 2-5. [arXiv:hep-lat/9603026v1](https://arxiv.org/abs/hep-lat/9603026v1).
2. P. Eymard, *L'algèbre de Fourier d'un groupe localement compact*, Bulletin de la Société Mathématique de France 92 (1964), 181-236. [Original article](https://www.numdam.org/item/BSMF_1964__92__181_0/).
3. G. Lumer and R. S. Phillips, *Dissipative operators in a Banach space*, Pacific Journal of Mathematics 11 (1961), 679-698, Theorem 3.1. [Original article](https://msp.org/pjm/1961/11-2/pjm-v11-n2-p19-s.pdf).
4. Levent Alpöge, [original Jacobian counterexample announcement](https://x.com/__alpoge__/status/2079028340955197566), 20 July 2026; credits Akhil and Fable.
5. Terence Tao, *A digestion of the Jacobian conjecture counterexample*, 21 July 2026. [Exposition](https://terrytao.wordpress.com/2026/07/21/a-digestion-of-the-jacobian-conjecture-counterexample/).
6. Levent Alpöge, $S^6$ construction circulated with AI assistance. [Original manuscript](https://alpo.ge/s6.pdf), especially p. 2, Setup.
7. Philip Engel, *Complex structures on $S^6$*, 13 September 2026. [Expository manuscript](https://philip-engel.github.io/S6.pdf), abstract and Section 1.3.

```{=latex}
\clearpage
\appendix
```
