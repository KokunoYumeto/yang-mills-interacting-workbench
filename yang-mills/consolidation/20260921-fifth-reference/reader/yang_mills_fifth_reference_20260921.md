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


# The complete fifth reference: original spin channels, a convergent correction, and physical energy

21 September 2026. This continues the actual Yang–Mills checkpoint in the cumulative volume/heat edition. The fifth coefficient catalogue is an input already calculated there. Here its complete signed channel action is evaluated for quantitative source control, then the entire remaining nonlinear equation is solved on an explicit disk. The Riemann attachments have no mathematical role in this calculation. The proof supplies written analytic arguments and exact finite certificates; it does not assert an independent external analytical review, a formal-assistant proof, historical priority, or a continuum mass gap.

## F1. Original coordinates, spaces, and coefficient norms

Fix an integer L>=2. The original vertices are {-L,...,L}^3, with every contained positively oriented nearest-neighbor edge e=(n,i) and every contained elementary face p=(n;i,j), i<j. Keep

\[
W_p=\operatorname{tr}\{U_i(n)U_j(n+e_i)U_i(n+e_j)^{-1}U_j(n)^{-1}\},\quad
T_a=-i\sigma_a/2,\quad X_{e,a}f=\left.\partial_t f(\ldots,e^{tT_a}U_e,\ldots)\right|_0.
\tag{F1}
\]

The physical Hilbert space is the invariant part of original product-Haar-probability L2, with all vertex transformations, including boundary vertices, included. The original operator is

\[
H_L=\kappa K+\kappa\xi(2M-S),\quad K=-\sum_{e,a}X_{e,a}^2,
\quad S=\sum_pW_p,\quad M=|\mathsf P_L|,
\quad\kappa=\frac{2g^2}{a},\quad\xi=\frac1{4g^4},\quad a,g>0.
\tag{F2}
\]

The physical operator domain is H2 and the form domain H1 on this compact product. Its smooth bounded potential preserves self-adjointness and compact resolvent. Write P_H f=int f dU, Q_H=I-P_H. For the actual positive ground vector psi,

\[
q_{H-E_0}(\psi f)=\kappa\int\psi^2\sum_i|X_if|^2dU.
\tag{F3}
\]

Integration by parts using H psi=E0 psi proves this identity. The modulus inequality, elliptic regularity and the maximum principle give a positive ground vector; (F3) gives uniqueness. Gauge transformations consequently fix this positive unit vector.

For the original product representation pi_j, with d_j=product_e(2j_e+1), retain

\[
A_j(f)=d_j\int f(U)\pi_j(U)^*dU,\quad
f=\sum_j\operatorname{Tr}(A_j(f)\pi_j),\quad
c_j=\sum_e j_e(j_e+1),\quad \|f\|_X=\sum_j\|A_j(f)\|_1.
\tag{F4}
\]

The norm on the right is an auxiliary coefficient estimate; the physical pairing remains (F3). Original Haar matrix-coefficient orthogonality proves the Fourier map and inverse. Decomposing a product representation with all multiplicities, pinching its coefficient matrix, and tracing its multiplicity spaces gives

\[
\|fh\|_X\le\|f\|_X\|h\|_X,
\qquad \|A_j(X_{e,a}f_j)\|_1\le j_e\|A_j(f_j)\|_1.
\tag{F5}
\]

Pinching is an average of unitary conjugations. For the partial trace, duality with Z tensor I, ||Z||<=1, proves contraction of trace norm. This proves the needed compact-group Fourier-algebra estimates directly; Eymard's Fourier algebra is the antecedent.

Each original coefficient also retains a finite edge label S containing its active representation support. Set

\[
\begin{split}
\|v\|_{\rm loc}&=\sup_a\sum_{S\ni a,j\ne0}c_j\|A_{S,j}\|_1,\\
m(v)&=\sup_a\sum_{S\ni a,j\ne0}\Big(\sum_ej_e\Big)\|A_{S,j}\|_1,\\
t(v)&=\sup_e\sum_{S\ni e,j\ne0}j_e\|A_{S,j}\|_1.
\end{split}\tag{F6}
\]

Assembly sums A_(S,j) over all labels containing supp(j). Its kernel consists exactly of the equations that these sums vanish. For each enlarged S, move its actual A_(S,j) to supp(j) and retain the two-entry relation (+A at S,-A at supp(j)). Reading the enlarged-label entries is the inverse decomposition on this kernel. Hence enlarged zero-function labels remain represented.

## F2. Gauge estimate and bilinear source

At each original vertex, a nonzero physical coefficient contains a singlet intertwiner. Grouping the j_e factor gives j_e<=sum_(f incident v,f!=e)j_f by the highest weight of the remaining tensor factors. For a fixed edge e={u,v}, the other edges at u,v have total spin J1>=2j_e. Their outer endpoints are distinct: a common endpoint would form a triangle in the original cubic graph. Summing their own singlet inequalities gives J1<=2J2, counting every further edge at most twice. Thus sum_f j_f>=j_e+J1+J2>=4j_e. Since j(j+1)>=(3/2)j at every nonzero half-integer,

\[
c_j\ge6j_e\quad\hbox{on physical blocks},\qquad
\sum_e j_e\le\frac23c_j,\qquad
m(v)\le\frac23\|v\|_{\rm loc},\quad t(v)\le\frac16\|v\|_{\rm loc}.
\tag{F7}
\]

This proves c_j>=3 on the nonconstant physical space. The fundamental elementary plaquette attains 3. Active bridges and open boundaries remain in this argument.

Define the original bilinear differential and its zero-Haar inverse,

\[
\Gamma(f,h)=\sum_{e,a}(X_{e,a}f)(X_{e,a}h),\qquad
B(f,h)=K^{-1}Q_H\Gamma(f,h).
\tag{F8}
\]

Every input pair retains its union label. Every removed Haar scalar is stored as a scalar energy contribution. Bounding anchors in each input separately, (F5) gives

\[
\|B(f,h)\|_{\rm loc}\le3\{m(f)t(h)+m(h)t(f)\}
\le\frac23\|f\|_{\rm loc}\|h\|_{\rm loc}.
\tag{F9}
\]

The factor three is the complete generator sum. The output c_j cancels exactly against K^{-1} on the nonconstant output. Two useful consequences are

\[
\|2B(q,\cdot)\|_{\rm loc\to loc}\le m(q)+4t(q),\qquad
\|2\Gamma(v,h)\|_X\le4t(v)\|Kh\|_X.
\tag{F10}
\]

The latter includes the full scalar output.

## F3. Orientation-resolved trace coefficient and its exact transport

Here is a new finite coefficient bound used before absolute summation. First regard each of the l occurrences in a trace word as an independent d-dimensional representation variable, with orientation signs s_i=+1 or -1. Replace each inverse by its actual invariant-dual transpose C pi(U)^T C^{-1}, where C is unitary (for fundamental SU(2), C is the alternating two-index matrix). These coefficient-side unitary matrices preserve the singular values. In the remaining integer index tensor, the cyclic trace indices r_i contribute

\[
A_{(b_i),(a_i)}=\sum_{r_1,\ldots,r_l}
\prod_i\mathbf1\{(a_i,b_i)=(r_i,r_{i+1})\text{ for }s_i=+1;
\ (a_i,b_i)=(r_{i+1},r_i)\text{ for }s_i=-1\},\quad r_{l+1}=r_1.
\tag{F11}
\]

Let 2k be the number of cyclic sign changes. At a vertex with equal consecutive signs, r_i appears once in a row and once in a column; this gives an identity factor. A + to - transition gives a two-row delta vector; a - to + transition gives a two-column delta vector. There are k of each, each of norm sqrt(d), and l-2k identity factors. Separate row and column permutations consequently give

\[
A^*A\text{ has nonzero eigenvalue }d^{2k}
\text{ of multiplicity }d^{l-2k},\qquad
\boxed{\|A\|_1=d^{l-k}.}
\tag{F12}
\]

Equivalently (A* A)^2=d^(2k)A* A and Tr(A* A)=d^l. This includes every original color sum. The checker constructs the actual integer matrices for all signs through length seven at d=2 and length five at d=3: 316 cases, with both complete matrix identities checked.

Repeated occurrences of a link are now identified by the diagonal compact-group homomorphism sending the one original U_e to its occurrence tuple. The representation on that tuple decomposes unitarily with all multiplicities. The pinching and partial-trace argument of (F5) proves that this actual pullback contracts the Fourier trace norm. Thus 2^(l-k) is a rigorous upper bound for an original fundamental trace word, and products multiply these bounds.

The original lattice coordinate transport is y_i=epsilon_i x_(pi(i))-d_i, with inverse x_(pi(i))=epsilon_i(y_i+d_i). It sends the original U_e to the mapped U or its inverse according to orientation. The underlying physical Haar norm and Casimir intertwine through that map. For the coefficient estimate, instead of assigning invariance to every partial transpose, we explicitly retain all eight sign reflections. For an original trace polynomial P=sum_m c_m product_(w in m)Tr(w), put

\[
\mathfrak b(P)=
\max_{\epsilon\in\{\pm1\}^3}
\sum_m|c_m|\,2^{\sum_{w\in m}(|w|-k_\epsilon(w))}.
\tag{F13}
\]

Here k_epsilon(w) counts half the cyclic sign changes after the original axis reflection. The axes permutation only relabels the three reflected coordinates. This proves a bound simultaneously on every original signed transport. Every nonempty closed cubic word has both signs after any reflection, since its net displacement in each coordinate is zero. Hence k_epsilon>=1 and (F13) is at most the preceding length-only sum sum_m|c_m|2^(total length-number of traces).

For clarity, on four independent factors, partial transpose of the last two tensor coordinates sends the all-positive coefficient matrix of trace norm 16 to the ++-- matrix of trace norm 8. The executable checks this exact map and both costs. No norm identity under that partial transpose is inserted.

## F4. Full fifth-source inputs and signed spin-channel recurrence

The preserved fifth catalogue contains 662 representatives, 124864 anchored original multisets and 14063 rational trace-monomial terms. Every coefficient v_nu has its complete original edges, words and multiplicities. The original coefficient equation is

\[
v_1=\frac13\sum_pW_p,\quad
v_n=\sum_{i=1}^{n-1}B(v_i,v_{n-i}),\qquad
v_5=2B(v_1,v_4)+2B(v_2,v_3).
\tag{F14}
\]

For 321 of the fifth representatives all five faces are distinct and each original edge occurs at most twice. Let E_s be the repeated edges; each carries final spin b_e=0 or 1. A singly occurring edge carries 1/2. For a subset A of those five faces, let r_e(A) count its original occurrences and define

\[
c_b(A)=\sum_{r_e(A)=1}\frac34+
\sum_{r_e(A)=2}b_e(b_e+1).
\tag{F15}
\]

The complete admissible spin assignments retain every original vertex singlet constraint. For c_b(A)>0 define

\[
a_b(\{p\})=\frac13,\qquad
a_b(A)=\frac1{2c_b(A)}
\sum_{\varnothing\ne B\subsetneq A}
[c_b(B)+c_b(A\setminus B)-c_b(A)]a_b(B)a_b(A\setminus B).
\tag{F16}
\]

The empty coefficient and zero-Casimir coefficient are zero in the zero-Haar source. For these distinct-face proper subsets there is no nonempty closed surface. Each intermediate shared edge has either the same final pair of fundamental occurrences, or one fundamental occurrence. Therefore its pair projector and its actual intermediate Casimir intertwine with the final projector. Projectors on different edges commute. Applying

\[
2\Gamma(f,h)=(c_f+c_h)fh-K(fh)
\tag{F17}
\]

to every ordered input split proves

\[
\boxed{v_\nu=\sum_b a_b(A_{\rm all})P_b\prod_{p\in A_{\rm all}}W_p.}
\tag{F18}
\]

Every scalar in (F16) is evaluated as a rational number before taking its absolute value. The formula retains all input orderings and zero channels. Complete original quaternion polynomial identities verify (F18) against the inherited fifth coefficient for all 321 representatives, rather than testing only values at selected configurations.

For a set Z of repeated edges,

\[
P_{0,Z}=\prod_{e\in Z}(I-E_e/2),\qquad E_e=-\sum_aX_{e,a}^2.
\tag{F19}
\]

This is the original spin-zero projector on the degree-two occurrence space. Let x_b be the nonnegative trace norm of the coefficient block of P_b product W_p. Pinching into the complete edge-spin blocks gives

\[
\sum_{b:\ b_e=0\ (e\in Z)}x_b
=\|P_{0,Z}\prod_pW_p\|_X
\le\mathfrak b(P_{0,Z}\prod_pW_p).
\tag{F20}
\]

Each right side is calculated from the complete projected trace polynomial and all eight reflection bounds. The 321 families contain 6240 such constraints; 3498 are strictly tighter than their length-only predecessors.

The three objective families are

\[
\sum_b|a_b|c_bx_b,\quad
\sum_b|a_b|(\sum_ej_e(b))x_b,\quad
\sum_b|a_b|j_e(b)x_b\quad\text{for every original edge }e.
\tag{F21}
\]

Each supplied rational dual lambda>=0 satisfies A^T lambda>=the actual objective and has cost b^T lambda. Hence its cost bounds that objective for the actual x. The records also give feasible primal vectors with the same value. A separate auditor reconstructs the constraints, objectives, original Casimirs and polynomial projections, then verifies all 5726 primal/dual certificates without invoking the optimization solver. They certify bounds on the actual coefficients, not an assumption that the actual coefficient masses attain the finite polytope maximum.

## F5. The remaining original configurations and complete anchored return

For every ordered split of a fifth multiset into original submultisets A,B, the complete cubic channel polytopes and the exact saved fourth coefficients give

\[
\|B(v_A,v_B)\|_{\rm loc,one\ label}
\le3\sum_e t_e(v_A)t_e(v_B).
\tag{F22}
\]

For a (2,3) split the record also maximizes the full bilinear expression over the two actual finite input-channel polytopes. Its variables, original edge spins, signed scalar coefficients and all polytope vertices are retained in the inherited channel source. For a (1,4) split, t_e(v_1)=4/3 on that face; hence the sharper joint bound is

\[
4\sup\left\{\sum_j\sum_{e\in\partial p\cap\operatorname{supp}B}
 j_e\|A_j(v_B)\|_1\right\}.
\tag{F23}
\]

This simultaneous edge objective is evaluated on the actual fourth channel polytope where available. On every fourth row it is bounded as well by its saved local-Casimir bound times max_j(sum_selected j_e/c_j), by the complete raw trace estimate, and by the sum of its saved individual edge bounds. For a repeated single face its complete spin-one and spin-two characters give the additional exact coefficient-norm bound. Each of these is a bound on the same scalar objective, so the minimum of the scalar upper bounds is valid.

Summing every ordered split proves an upper bound C_nu for the actual fifth coefficient on its original union. Its total and marked-spin bounds also follow from the full admissible output-spin list:

\[
m_\nu\le C_\nu\max_j\frac{\sum_ej_e}{c_j},\qquad
t_{\nu,e}\le C_\nu\max_j\frac{j_e}{c_j}.
\tag{F24}
\]

The complete inherited trace expression supplies independent raw upper bounds; the explicit one-face fifth character supplies its own further bound. On the 321 rows of F4, the complete signed channel objectives (F21) are also used. Thus all 662 rows are covered, including the other 341 original multiplicity/shared-edge configurations. No generic distinct-face recurrence is applied to an edge with three or more occurrences.

The original anchor is the edge from (0,0,0) to (1,0,0). For every one of the 124864 original anchored multisets the saved signed-coordinate map sends both endpoints into the representative edge set. Summing that representative's actual marked-edge bound, rather than a freely selected representative edge, proves

\[
\begin{split}
\|v_5\|_{\rm loc}&\le
\frac{1141532378446937587064431}{460877915422606500}<2476866,\\
m(v_5)&\le
\frac{6682496758630785752687413327666759}{4077966203261057899505463750}<1638684,\\
t(v_5)&\le
\frac{126023896114060026308152742875366210205679497747117260778732756243249}
{662840019461690772503734890389307666881000651173392960000000000}<190128.
\end{split}\tag{F25}
\]

Every boundary box uses a subset of these original labels, so the same bounds hold independently of L. The complete per-row and per-anchor sums are in generated/rows and generated/fifth_budgets.json. The 124864 coordinate transports and full fifth-source polynomials are preserved in the preceding directory.

## F6. Full fifth-reference residual, inverse, and nonlinear correction

For the following closed formulas use the proved upward bounds

\[
\begin{split}
(m_1,t_1)&=(64/3,16/3),\\
(m_2,t_2)&=(5834/39,137/6),\\
(m_3,t_3)&=(336572872/208845,225985217/1253070),\\
(m_4,t_4)&=(17270702970768271/341697152160,
110695177857394584026401/18025447358750832000),\\
(m_5,t_5)&=(1638684,190128).
\end{split}\tag{F26}
\]

Each coefficient is a bound on the same original source norms in F6. Set q5=sum_(i=1)^5 xi^i v_i. Its complete residual is

\[
\begin{split}
R_5={}&\xi v_1+B(q_5,q_5)-q_5\\
={}&\xi^6[2B(v_1,v_5)+2B(v_2,v_4)+B(v_3,v_3)]\\
&+\xi^7[2B(v_2,v_5)+2B(v_3,v_4)]\\
&+\xi^8[2B(v_3,v_5)+B(v_4,v_4)]
+2\xi^9B(v_4,v_5)+\xi^{10}B(v_5,v_5).
\end{split}\tag{F27}
\]

No coefficient above degree five is treated as zero. Define

\[
b_{ij}=3(m_it_j+m_jt_i),\quad
\ell(x)=\sum_{i=1}^5(m_i+4t_i)x^i,\quad
\delta(x)=\sum_{\substack{1\le i,j\le5\\i+j\ge6}}b_{ij}x^{i+j},\quad
\mathscr D(x)=(1-\ell(x))^2-\frac83\delta(x).
\tag{F28}
\]

All coefficients of ell and delta are positive. On [0,19/1000], ell<1, so D'= -2(1-ell)ell'-(8/3)delta'<0. The signs at 18/1000 and 19/1000 are opposite. Therefore there is exactly one root alpha in that interval and it is the first positive root. Exact rational bisection and integer-square bounds give

\[
\begin{split}
0.018424953576117616681&<\alpha<0.018424953576117616682,\\
3.683551983985727304439&<\frac1{2\sqrt\alpha}
<3.683551983985727304440.
\end{split}\tag{F29}
\]

For any complex |xi|<=alpha, J5=2B(q5,.) satisfies ||J5||<=ell<1. Thus L5=I-J5 has the actual bounded inverse sum_(n>=0)J5^n, on the original local labelled source. The full correction w=v-q5 solves

\[
L_5w=R_5+B(w,w).
\tag{F30}
\]

Put w1=L5^{-1}R5 and w_n=L5^{-1}sum_(i+j=n)B(w_i,w_j). Its nth norm is bounded by Cat_(n-1)[(2/3)/(1-ell)]^(n-1)[delta/(1-ell)]^n. This complete series converges even at the endpoint, and

\[
\boxed{\|w\|_{\rm loc}\le w_*(x)
=\frac34[1-\ell(x)-\sqrt{\mathscr D(x)}],\qquad x=|\xi|\le\alpha.}
\tag{F31}
\]

With theta=8delta/[3(1-ell)^2]<=1, its omitted tree orders satisfy

\[
\left\|\sum_{n>N}w_n\right\|_{\rm loc}
\le\frac34(1-\ell)\theta^{N+1}\frac{\binom{2N}{N}}{4^N}
\le\frac34(1-\ell)\frac{\theta^{N+1}}{\sqrt{N+1}}.
\tag{F32}
\]

The identity Cat_N/4^N=2[binom(2N,N)/4^N-binom(2N+2,N+1)/4^(N+1)] proves the tail exactly; the central binomial bound follows by induction after squaring. Thus the endpoint uses an explicit convergent tail rather than a strict endpoint contraction.

On every finite graph, the total c-weighted coefficient sum is at most |E_L| times the local norm. First and second derivatives converge because j_e and j_e j_f are bounded by constant multiples of c_j. The assembled source therefore solves

\[
Kv=\xi S+\Gamma(v,v)-P_H\Gamma(v,v).
\tag{F33}
\]

For real xi, exp(v) is positive and gives

\[
\psi=e^{v+c_L},\quad c_L=-\frac12\log\int e^{2v}dU,
\quad E_0=2\kappa M\xi-\kappa P_H\Gamma(v,v).
\tag{F34}
\]

Substitution into the original H gives its exact eigen-equation. Equation F3 proves this eigenvalue is the bottom, and uniqueness identifies the actual vacuum. Elliptic bootstrapping gives all higher derivatives. For complex xi the same nonzero exponential solves the complex equation; the mean functional and its nonvanishing denominator are proved in the heat companion.

## F7. Actual physical spectral and primitive return

Let t_* =sum_i t_i x^i+w_*/6 and chi=4t_*. Equations F10 and F31 give ||2Gamma(v,h)||X<=chi||Kh||X. Direct algebra, with every term retained, yields

\[
\boxed{d_5(x)=3(1-\chi)
=\frac32(1+\sqrt{\mathscr D(x)})
+\sum_{i=1}^5(\tfrac32m_i-6t_i)x^i.}
\tag{F35}
\]

Every last coefficient is nonnegative; 0<=chi<1/2 on [0,alpha]. The correction w_* increases on the open interval because differentiation of (1-ell)w-(2/3)w^2=delta gives w'=(delta'+ell'w)/sqrt(D)>0. Therefore chi increases and d5 decreases to its positive endpoint.

Take an actual positive-energy physical eigenvector of H-E0. Division by psi, then subtraction of its Haar scalar, gives a nonzero smooth h with

\[
(K-\lambda/\kappa)h=Q_H2\Gamma(v,h).
\tag{F36}
\]

Smoothness implies sum_j c_j||A_j(h)||1<infinity: Plancherel and Cauchy--Schwarz with a sufficiently high original Casimir power give this on the finite compact product. For 0<lambda/kappa<3,

\[
\|(K-\lambda/\kappa)h\|_X
\ge(1-\lambda/(3\kappa))\|Kh\|_X.
\]

Combining with F35 proves lambda>=kappa d5. Values lambda/kappa>=3 satisfy the same bound since d5<=3. The complete compact physical spectral resolution consequently gives

\[
\boxed{\Delta_L\ge\kappa d_5(\xi),\qquad
q_{H-E_0}(\psi f)\ge\kappa d_5(\xi)\operatorname{Var}_{\psi^2}(f)}
\tag{F37}
\]

for every L>=2, a>0 and 0<xi<=alpha, on the whole physical form domain. In particular

\[
\begin{array}{c|c|c}
g^2\text{ at least}&\Delta_L/\kappa\text{ exceeds}&\|v-q_5\|_{\rm loc}\text{ below}\hline
37/10&1.6207&0.046581\\
15/4&1.6993&0.026352\\
4&1.9068&0.005752
\end{array}\tag{F38}
\]

The exact rational brackets, rather than these displayed rounded consequences, are in physical_return.json.

The approximate exponential retains its complete operator defect:

\[
e^{-q_5}He^{q_5}
=\kappa[K-2\Gamma(q_5,\cdot)]
+\kappa[2M\xi-P_H\Gamma(q_5,q_5)]I-\kappa M_{KR_5}.
\tag{F39}
\]

In particular, for the actual transformed operator Atilde,

\[
Q_H\widetilde Ah-\kappa KL_5h
=-2\kappa Q_H\Gamma(w,h),\qquad
\|\text{right side}\|_X\le\frac{2\kappa}{3}w_*\|Kh\|_X.
\tag{F40}
\]

Thus the reference linearization and physical operator have their exact comparison, including scalar and multiplication terms.

For source windows V_N=span{R5,J5R5,...,J5^N R5}, the actual complexes are V_N --L5--> V --0-->0. Inclusion and identity give their transitions. The map

\[
V_{N+1}/V_N\longrightarrow
\ker[V/L_5V_N\to V/L_5V_{N+1}],\quad [h]\mapsto[L_5h]
\tag{F41}
\]

has inverse induced by L5^{-1}: changing a representative by L5V_N changes its inverse by exactly V_N. The finite primitive sum_(j=0)^N J5^jR5 has residual J5^(N+1)R5. Its omitted norm is at most ell^(N+1)delta/(1-ell). Both the original relation and its support label remain.

On centered physical functions let d_X f=(X_if)_i with the original range pairing kappa int rho sum conjugate(v_i)w_i. The inverse on its actual image is p_X(d_X f)=f. Its uniqueness follows because all derivatives zero force a constant and centering fixes that constant. The exact variational identity is

\[
\boxed{\|p_X\|^2=1/\Delta_L\le1/[\kappa d_5(\xi)].}
\tag{F42}
\]

## F8. Sources and evidence

The original LaTeX was located at repository commit add590f78d0f6a1bdcc6e83cc9e0301cfc9b0f5d, yang-mills/consolidation/20260917/reader/yang_mills_quartic_cube_reader.tex. Its introductory original equations and six-appendix inventory were compared with the mounted source chain. No exhaustive new review of that whole LaTeX reader is claimed. The complete original fifth catalogue, fourth input channel bounds and prior heat proof are retained unchanged in this cumulative archive.

The explicit lower-order input polytopes occur in ../20260917-quartic-cube/channel_bounds.py and its QUARTIC_SOURCE.md/PHYSICAL_RETURN.md proof. The full fifth source is ../20260917-fifth-source/FIFTH_SOURCE.md and its generated catalogue. This continuation's new algebra checks F11--F25; the endpoint and physical-return arithmetic are separately replayed. Analytic Banach-space and elliptic arguments are written above, rather than represented as certified by finite matrix tests.

Human antecedents: D. Schuette, Zheng Weihong and C. J. Hamer, The Coupled Cluster Method in Hamiltonian Lattice Field Theory, arXiv:hep-lat/9603026v1, especially Sections 2--5, provide the exponential vacuum, character and Casimir framework. Their convention is connected by g_C=2^(3/4)g and H_ours=sqrt(2)H_C+2kappa xi M I, with their commutator derivative iX. P. Eymard, L'algebre de Fourier d'un groupe localement compact, Bull. Soc. Math. France 92 (1964),181--236, is the Fourier-algebra antecedent; the needed compact coefficient bounds are proved here. No human reference is asserted to verify the new finite catalogue or coupling threshold.


# Fifth-reference heat bounds and the complete complementary physical space

21 September 2026. This note applies the completed fifth-reference correction in FIFTH_REFERENCE.md to the original Yang–Mills heat, plaquette moments and complementary minimization. The improvement comes from evaluating that source, not from changing a physical norm. It uses the unchanged exact heat coefficients through degree four and constructs a new box-independent analytic remainder. All exterior-volume, observation-rank and physical-time scopes are stated explicitly.

## H1. Complete coefficient generator and original mean

Retain F1--F42 of the companion, in particular kappa=2g^2/a, xi=1/(4g^4), rho=psi^2 and A=H-E0. Fix a complex radius r<alpha. The fifth construction gives a local analytic source v(zeta) and a drift D_v=2Gamma(v,.), satisfying

\[
\|D_vh\|_X\le\chi(r)\|Kh\|_X,\quad
\chi(r)=1-d_5(r)/3<1/2.
\tag{H1}
\]

Let X0 be the nonconstant physical Fourier space with norm sum ||A_j||1, and Y0 its domain sum c_j||A_j||1<infinity. Define the actual maps

\[
T=Q_HD_vK^{-1}:X_0\to X_0,\quad p=P_HD_vK^{-1}:X_0\to\mathbb C,
\quad S=(I-T)^{-1},\quad
\mu(F)=P_HF+pSQ_HF.
\tag{H2}
\]

The complete scalar-and-nonconstant output obeys |py|+||Ty||X<=chi||y||X. Thus ||S||<=1/(1-chi), ||mu||<=1, and |(mu-P_H)Q_HF|<=chi||Q_HF||X/(1-chi). The last bound and chi<=1/2 prove the full mean norm, using the additive original constant/nonconstant coefficient norm. The exact Poisson equation is

\[
(K-D_v)K^{-1}SQ_HF=F-\mu(F).
\tag{H3}
\]

This constructs the scalar as well as the primitive. Integration by parts against exp(2v) gives int exp(2v)F=mu(F)int exp(2v). The latter integral cannot vanish: a vanishing value would make the left side zero for every physical Fourier polynomial, whose uniform closure contains the conjugate of the nonzero smooth gauge-invariant exp(2v). Their paired integral would then be zero. Consequently

\[
\mu(F)=\frac{\int e^{2v}F\,dU}{\int e^{2v}\,dU}.
\tag{H4}
\]

On real coupling this is the original vacuum expectation. The complex formula keeps its full nonzero scalar denominator.

The coefficient operator L=(I-T)K on Y0 is closed, since I-T has a bounded inverse and K is closed. Finite Fourier polynomials give a dense domain. For h>0 the factorization of I+hL through I+hK has remaining factor I-hQ_HD_v(I+hK)^{-1}, whose norm difference from I is at most chi. It is therefore onto with bounded inverse. For f in Y0,

\[
\|(I+hL)f\|_X\ge\|f\|_X+h(1-\chi)\|Kf\|_X
\ge[1+3h(1-\chi)]\|f\|_X.
\tag{H5}
\]

Here the identity ||(I+hK)f||=||f||+h||Kf|| follows coefficient by coefficient. The same derivative estimate proves dissipativity after shifting by 3(1-chi); range surjectivity at a sufficiently large positive parameter follows from the displayed factorization. The Hille--Yosida/Lumer--Phillips generation theorem thus gives

\[
E(\tau)=e^{-\tau L},\qquad \|E(\tau)\|\le e^{-3(1-\chi)\tau}.
\tag{H6}
\]

Both the domain and actual range were verified, rather than inferring a semigroup bound from a single inverse. Analytic parameter dependence follows from the locally analytic resolvents and their exponential Euler powers: each power is a positive scalar gamma-time average of E, has the same contraction bound, and converges strongly by its mean and variance. Bounded weak holomorphic convergence, tested against every continuous linear functional, gives the analytic continuation on every smaller source disk.

The original full heat is

\[
\mathcal T(\tau)F=E(\tau)Q_HF+\mu(F)-\mu(E(\tau)Q_HF).
\tag{H7}
\]

It solves the original transformed equation K-D_v, preserves the actual mean, and on real coupling agrees with the physical Hilbert semigroup by uniqueness. The physical time map and inverse are tau=kappa t and t=tau/kappa.

## H2. New box-independent heat circle

For original marked faces define

\[
r_p=(W_p-\mu W_p)\psi,\quad
\widehat C_{pq}(\tau;\xi)=\langle r_p,e^{-\tau A/\kappa}r_q\rangle.
\tag{H8}
\]

At complex parameter use its bilinear analytic continuation mu[(T(tau)Wp-mu Wp)Wq]. For arbitrary original face coefficients |z_q|<=1 put G_z=sum_q z_qWq. At most four faces meet an edge. Their fundamental coefficient norm 8 and edge spin 1/2 give

\[
\|\Gamma(h,G_z)\|_X\le32\|Kh\|_X.
\tag{H9}
\]

For the original Haar scalar there is a sharper exact selection rule. A physical representation block with spin 1/2 on one elementary face and zero elsewhere is the one-dimensional line C Wp. Its Casimir is 3, coefficient norm is 8|a_p|, and Haar norm of Wp is 1. Integration by parts and Haar orthogonality therefore give

\[
|P_H\Gamma(h,G_z)|\le\frac18\|Kh\|_X.
\tag{H10}
\]

Take h_tau=K^{-1}S E(tau)Wp. Equation H3, followed by integration by parts in H4, proves

\[
\sum_qz_q\widehat C_{pq}(\tau)=\mu\Gamma(h_\tau,G_z),\quad
\|Kh_\tau\|_X\le\frac8{1-\chi}e^{-3(1-\chi)\tau}.
\]

Retaining the Haar contribution (H10) and the full returned-mean contribution in H2 proves

\[
\boxed{\|\widehat C(\tau;\zeta)\|_{\rm row}
\le\frac{1+255\chi}{(1-\chi)^2}e^{-3(1-\chi)\tau}.}
\tag{H11}
\]

The row norm is max_p sum_q|C_pq|, obtained exactly by maximizing over the phases z_q. Transpose symmetry extends from real coupling by analytic continuation, so columns have the same bound. No face count M enters this estimate.

The exact source calculation F28--F35 verifies

\[
\boxed{R=1/55<\alpha,\quad d_5(R)>13/8,\quad
\chi(R)<11/24,\quad C=\frac{1+255(11/24)}{(1-11/24)^2}
=\frac{67896}{169}.}
\tag{H12}
\]

This circle strictly exceeds the saved fourth-reference endpoint 0.018104972231644127076, and the preceding volume-heat radius 3/256. The inequalities are certified by integer-square and rational polynomial bounds in physical_return.json.

The original link-center map U_(n,i) -> (-1)^(sum_(j<i)n_j) U_(n,i) preserves Haar, K and the full gauge action and sends every Wp to -Wp. Therefore the homogeneous connected two-mark heat is even. Applying Cauchy's formula to (H11) on the same circle gives

\[
\boxed{
\|\widehat C(\tau;\xi)-C_0(\tau)-\xi^2C_2(\tau)-\xi^4C_4(\tau)\|_{\rm row}
\le\frac{67896}{169}e^{-13\tau/8}
\frac{(55|\xi|)^6}{1-(55|\xi|)^2},\quad |\xi|<1/55.}
\tag{H13}
\]

This holds for every original L>=2 and every tau>=0. C0,C2,C4 are the complete unchanged inherited heat coefficient matrices; the original source/heat recurrence fixes them uniquely. The new result evaluates an infinite tail beyond those coefficients; it does not relabel a new finite heat coefficient as calculated.

## H3. Original moments and a signed leakage remainder

Let R_col have the original columns r_p and set Phi=kappa A^{-1}R_col. Keep

\[
G_0=R_{\rm col}^*R_{\rm col},\quad
G_1=\kappa R_{\rm col}^*A^{-1}R_{\rm col},\quad
G_2=\Phi^*\Phi,\quad
E=\Phi^*A\Phi=\kappa G_1,\quad
K_o=\kappa^{-1}R_{\rm col}^*AR_{\rm col}.
\tag{H14}
\]

The spectral theorem gives G_k=int_0^infinity tau^(k-1)Chat(tau)d tau/(k-1)! for k>=1. Thus (H13) has moment prefactor C/d^k, d=13/8, retaining every power of kappa in H14. G0 uses tau=0.

The complete kinetic function is <Gamma(Wp,Wq)>rho. A diagonal has coefficient norm at most30, from Gamma(Wp,Wp)=4-Wp^2=3-chi_1 and ||chi_1||X=27. An adjacent off-diagonal has norm at most48. Every face has at most twelve adjacent faces; every other entry is zero. Since ||mu||<=1, its full complex row bound is 606. It consequently has the same even tail factor, with prefactor606.

The actual nonnegative leakage trial is

\[
J=(R_{\rm col}-3\Phi)^*(R_{\rm col}-3\Phi)=G_0-6G_1+9G_2.
\tag{H15}
\]

Keep the sign of the time weight before estimating its remainder:

\[
J=\widehat C(0)+\int_0^\infty(9\tau-6)\widehat C(\tau)\,d\tau.
\tag{H16}
\]

Splitting the scalar integral at tau=2/3 gives the exact expression

\[
1+\int_0^\infty|9\tau-6|e^{-d\tau}d\tau
=1+\frac6d-\frac9{d^2}+\frac{18}{d^2}e^{-2d/3}.
\tag{H17}
\]

For d=13/8, the even 120th Taylor sum of exp(-13/12) is less than339/1000. Taylor's integral remainder is negative at that order, giving a rigorous upper bound for the exponential. Hence the complete leakage-tail prefactor is at most

\[
\boxed{C_J=C\left[1+\frac6d-\frac9{d^2}+\frac{18(339/1000)}{d^2}\right]
=\frac{5156090136}{3570125}.}
\tag{H18}
\]

This is smaller than C(1+6/d+9/d^2). All signed time weights and mixed moment entries remain in H15--H18.

The complete inherited original-support coefficient bounds are

|Matrix|degree two row bound|degree four row bound|
|---|---:|---:|
|G0|149/468|2361994073/4691494080|
|G1|97/468|376882691/938298816|
|G2|73313/657072|982069718963833/3919180324550400|
|Ko|187/468|586668421/1563831360|
|J|6779/73008|152338674005989/435464480505600|

Their actual absolute-motif assembly retains all 199 original supports and559 marked contributions in the preceding volume directory. Boundary rows use subsets; no claim that a signed bulk row is the worst boundary row is used.

For x=xi and u=(55x)^6/[1-(55x)^2], define the explicit widths

\[
\begin{split}
w_k&=B_{k,2}x^2+B_{k,4}x^4+(C/d^k)u\quad(k=0,1,2),\\
w_K&=B_{K,2}x^2+B_{K,4}x^4+606u,\\
\beta&=B_{J,2}x^2+B_{J,4}x^4+C_Ju.
\end{split}\tag{H19}
\]

The original real symmetric matrices therefore satisfy

\[
\|G_k-3^{-k}I\|\le w_k,\quad\|K_o-3I\|\le w_K,
\qquad0\preceq J\preceq\beta I.
\tag{H20}
\]

The operator estimate follows from both row and column bounds. Each width increases with x. Their exact rational values at the original coupling benchmarks, with all square-root enclosures for d5, are in generated/physical_return.json.

## H4. Whole physical observation and complementary coupling

Put l_k=3^(-k)-w_k, u_k=3^(-k)+w_k for k=0,1,2, and u_K=3+w_K. Each benchmark below has l_k>0. Thus R_col and Phi are injective and have closed ranges, with the original Grams H14. The actual state projection is

\[
P_R=R_{\rm col}G_0^{-1}R_{\rm col}^*,\quad
\|P_R\Phi c\|^2=c^*G_1G_0^{-1}G_1c.
\]

Consequently

\[
\frac{\|P_R\Phi c\|^2}{\|\Phi c\|^2}
\ge\frac{l_1^2}{u_0u_2}\quad(c\ne0).
\tag{H21}
\]

This is observation of the actual inverse-energy vectors, with both original state metrics retained.

For the complete physical complement define

\[
P=\Phi G_2^{-1}\Phi^*,\quad Q=I-P,\quad B_\Phi=QR_{\rm col}.
\tag{H22}
\]

Completing the original state-norm square gives

\[
B_\Phi^*B_\Phi=G_0-G_1G_2^{-1}G_1\preceq J\preceq\beta I.
\tag{H23}
\]

The comparison with J follows by inserting the specific admissible coefficient3c into the same state minimum. Every centered physical form-domain vector has the decomposition Phi c+h, h in QH0. Its complete pairing and energy are

\[
\begin{split}
\|\Phi c+h\|^2&=c^*G_2c+\|h\|^2,\\
q_A(\Phi c+h)&=\kappa c^*G_1c
+2\kappa\operatorname{Re}\langle B_\Phi c,h\rangle+q_A(h).
\end{split}\tag{H24}
\]

Take d_ph as any displayed rational lower endpoint for d5(x); then A>=kappa d_ph on H0 by F37. The product A Phi=kappa R_col is bounded. Hence AP is bounded, PA has its bounded adjoint extension, and QAP+PAQ is bounded self-adjoint. Subtraction of this operator from A leaves a self-adjoint block-diagonal operator on Dom(A). Its Q restriction is

\[
D_Q=QAQ,\quad\operatorname{Dom}D_Q=\operatorname{Dom}A\cap Q\mathcal H_0,
\quad D_Q\succeq\kappa d_{\rm ph}I.
\tag{H25}
\]

This proves its operator domain and inverse on the complete complementary space, rather than just a trial subspace. Direct substitution minimizes H24 at

\[
h_{\min}=-\kappa D_Q^{-1}B_\Phi c.
\]

The restored columns and metrics are exactly

\[
\begin{split}
\Phi_{\rm full}&=\Phi-\kappa D_Q^{-1}B_\Phi,\\
E_{\rm full}&=\kappa G_1-\kappa^2B_\Phi^*D_Q^{-1}B_\Phi,\\
G_{\rm full}&=G_2+\kappa^2B_\Phi^*D_Q^{-2}B_\Phi.
\end{split}\tag{H26}
\]

Define the explicit positive numbers

\[
\eta_E=\frac{\beta}{d_{\rm ph}l_1},\quad
\eta_G=\frac{\beta}{d_{\rm ph}^2l_2}.
\tag{H27}
\]

Then

\[
(1-\eta_E)E\preceq E_{\rm full}\preceq E,\qquad
G_2\preceq G_{\rm full}\preceq(1+\eta_G)G_2.
\tag{H28}
\]

The full mixed form H24 also lies between (1-sqrt(eta_E)) and (1+sqrt(eta_E)) times kappa c*G1c+q_A(h), by Cauchy--Schwarz in the actual D_Q energy. The cross term has been bounded, not discarded.

The state minimum section P_R Phi differs from the energy minimum section Phi by h_R=(I-P_R)Phi. The original equation A Phi=kappa R_col gives q_A(Phi c,h_Rd)=0. Expanding both mixed terms gives

\[
h_R^*Ah_R=\kappa[G_1G_0^{-1}K_oG_0^{-1}G_1-G_1]
\preceq\left(\frac{u_1u_K}{l_0^2}-1\right)E.
\tag{H29}
\]

## H5. Explicit improved domains

The rational evaluation of H19--H29 proves, simultaneously for all original boxes L>=2 and a>0:

|Original coupling|Observed state fraction exceeds|Complementary energy loss below|Restored state increase below|
|---|---:|---:|---:|
|g²>=10|977/1000|11/1000|12/1000|
|g²>=12|997/1000|12/10000|12/10000|
|g²>=25/2|998/1000|1/1000|1/1000|
|g²>=13|999/1000|1/2000|1/2000|
|g²>=16|9999/10000|1/25000|1/25000|

“Loss below eta” in this table means E_full>(1-eta)E; “increase below eta” means G_full<(1+eta)G2. All identities and quotients are the original H14,H26, not substituted metrics. At g²=13, the exact diagnostic values of the three respective bounds are approximately0.99904459483,0.00043585425,0.00045023706; the conclusions in the table use strict rational tests. For g²>=16 the corresponding original section-energy change H29 is below1/20000.

For example at g²>=13 the full original Gram bounds include

\[
\|G_0-I\|<119\cdot10^{-6},\quad
\|G_1-I/3\|<73\cdot10^{-6},\quad
\|G_2-I/9\|<45\cdot10^{-6},\quad
\|K_o-3I\|<178\cdot10^{-6}.
\tag{H30}
\]

The physical gap used there has d_ph=29047/10000. Every estimate for larger g² follows because xi decreases, the widths increase with xi, and d5 decreases with xi.

## H6. Support quotients, heat horizon, and spatial limit

For original face sets F subset G, keep V_F=Phi(C^F), U_F=A V_F. The cochain windows are V_F --A--> H0 --0-->0. The exact transported-kernel isomorphism is

\[
V_G/V_F\longrightarrow\ker[\mathcal H_0/U_F\to\mathcal H_0/U_G],
\qquad[h]\mapsto[Ah].
\tag{H31}
\]

Its inverse is induced by the actual A^{-1}; changing a representative by U_F changes its inverse by V_F. For J=G minus F, its original energy quotient is the attained minimum

\[
Q_E(F,G)=E_{JJ}-E_{JF}E_{FF}^{-1}E_{FJ},\qquad
c_F^{\min}=-E_{FF}^{-1}E_{FJ}c_J.
\tag{H32}
\]

Every mixed block and the removed primitive remain in the formula. The finite-time columns

\[
\Phi_T=(I-e^{-TA})\Phi=\kappa\int_0^Te^{-tA}R_{\rm col}\,dt
\]

satisfy A Phi_T=kappa R_col-kappa e^{-TA}R_col. With epsilon=e^(-kappa d_ph T), the original state and energy Grams lie between (1-epsilon)^2 and1 times the original Grams. This follows spectrally from A>=kappa d_ph and commutation with exp(-TA). Taking infima over the identical coefficient fibers in H32 preserves these inequalities.

For a prescribed finite signed determinant return sum_j a_j logdet Q_j of total absolute rank B=sum_j|a_j|rank Q_j, the error is at most2B[-log(1-epsilon)]. A finite physical choice is

\[
\boxed{T=(\kappa d_{\rm ph})^{-1}\log(1+2B/\eta),}
\tag{H33}
\]

which gives error<=eta by -log(1-epsilon)<=epsilon/(1-epsilon). Both rank and physical time factors are explicit.

The same construction also supplies the spatial limit at fixed a,g with xi<1/55. Every original Taylor coefficient of v has a connected original face support, and a degree-n marked heat coefficient depends only on its finite n-neighborhood. This is proved by the actual source/heat recurrences: a derivative product joins supports only at an original common edge; K inversion and its unperturbed resolvent preserve link support. The scalar and disconnected terms remain until the connected subtraction. On disjoint active components the original compact-group operator and positive vacuum factor, giving the same zero coefficients.

On two boxes containing the same N-neighborhood of the marks, all heat coefficients through N coincide. Equation H13 consequently gives

\[
|\widehat C_L-\widehat C_{L'}|
\le2Ce^{-d\tau}\frac{(55|\xi|)^{2(\lfloor N/2\rfloor+1)}}{1-(55|\xi|)^2}.
\tag{H34}
\]

The mean H2 and full heat H7 have analogous local Taylor tails. They converge on cylinder Fourier polynomials, and for real coupling their actual Markov contractions extend convergence to the uniform closure. Positivity, unit mass, semigroup composition and symmetry pass by cylinder approximation. Their unique invariant physical state follows by integrating the uniform decay of H7 on centered cylinders. This is uniqueness on the gauge-invariant observable algebra; the original vertex Haar average supplies its gauge-invariant probability lift.

The resulting self-adjoint generator on L2(mu)_phys has its actual cylinder domain and A_infinity F=kappa(K-D_v,infinity)F: pass the finite semigroup integral equation using the absolute local derivative tails. The finite gap passes by L2 density, yielding A_infinity>=kappa d5(xi) on the centered space. The moment matrices are bounded positive operators on the original l2 infinite face coefficient space, because the row estimates and spatial tails give strong convergence on finite coefficient vectors, then on all l2. Their positive lower bounds remain.

Consequently R_col and Phi extend as closed-range maps and A_infinity Phi=kappa R_col. In particular A_infinity P_Phi is bounded even for this infinite family. The same bounded-off-diagonal domain argument in H25, and the complete H26 minimization, therefore hold for the full infinite complementary physical space. The benchmark table H5 carries over at fixed spacing and coupling.

## H7. Continuum scope and next original quantity

The standing simultaneous path keeps a_n=a0*2^(-n), g_n²=1/c_n, c_n=g0^(-2)+beta*n*log2 and xi_n=c_n²/4. Its exact inclusion in the fifth-source domain is c_n<=2sqrt(alpha); its inclusion in this heat circle is c_n<2/sqrt(55). For beta>0 it eventually leaves both. No positive finite continuum mass or nontrivial smooth four-dimensional field is concluded from these fixed-spacing estimates.

This tranche completes the selected fifth-reference correction and its return to the full physical complement. Merely re-centering the elementary norm inequality reproduces its old endpoint, as the preserved ROUTE_ASSESSMENT calculation proves. A further extension has to use actual additional coefficient or signed inverse information. The concrete next candidate is the same-support linearized action J5 and its preconditioned residual, using the now stored complete edge-channel coefficients; any replacement of the inverse must retain its exact residual operator. The missing sixth-source catalogue remains missing in the delivered source chain and has not been declared reconstructed by these estimates.

## H8. Evidence and attribution

All old heat coefficients and absolute support sums are preserved byte-for-byte. New algebra evaluates the fifth reference; new rational calculations verify its root, heat circle, signed time integral and the benchmark matrix inequalities. The written source-domain and semigroup argument is supplied in F1--F42 and H1--H34; exact finite checks are not represented as formal proof of the analytic passage.

G. Lumer and R. S. Phillips, Dissipative operators in a Banach space, Pacific J. Math.11 (1961),679--698, Theorem3.1, is used only after the domain, dissipativity and range checks H5. P. Eymard's compact Fourier algebra and Schuette--Zheng--Hamer's exp-S/Casimir construction are credited as in the companion. This contribution is on the original Yang–Mills objects. No arithmetic Gamma measure, RH root packet, or Riemann activation asymptotic is imported.
