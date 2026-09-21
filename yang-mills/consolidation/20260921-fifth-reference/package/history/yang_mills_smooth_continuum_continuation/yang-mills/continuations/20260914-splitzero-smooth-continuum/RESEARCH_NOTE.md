# Split Zero continuum continuation: smooth source germs, exact refinement, and positive-time spectral control

Research continuation, 14 September 2026.

## 0. Provenance and completed scope

This is an additive, locally prepared contribution for `KokunoYumeto/yang-mills-interacting-workbench`. It continues the supplied `split_zero_ym/RESEARCH_NOTE.md`. Publication to GitHub has not occurred in this session. The GitHub integration was offered; its discovery response reported that it was not installed. Public source reading was possible through the browser, but direct network requests from the execution container failed.

The following mathematical source bodies were retrieved on 14 September 2026:

- [YM1] `yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`, especially §§1–2: the full Hamiltonian, gauge action, physical domains, positive unit vacuum and ground-state identity.
- [YM2] `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_WILSON_SCHUR_MEMORY.md`: original link-transport convention, complete magnetic value, retained memory and metric.
- [YM3] `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_TENSOR_TRANSFER.md`: full nonlinear transport and observable/state distinctions, with the actual maps retained.
- [SZ] `KokunoYumeto/zeta-function-research-reader`, revision `7ea0a49945390eae14d3160a5730858899768b5f`, `workbenches/split-support-rees-trace/RESEARCH_NOTE.md`, §§2 and 7.1: supported linear diagrams and the retained-jet ring morphism.

YM paths refer to `main` as retrieved on the stated date; an immutable YM revision was not obtained. Complete URLs and retrieval scope are recorded in `sources.json`.

The S6 entry point `s6/README.md` and the S6 section of `ATTEMPTS.md` were retrieved. The latter locates the smooth normal-line trivialization and its inverse at Theorems 53.4, 53.6, 53.7, 53.9 / FF1–FF46 of the frozen project. Fetches of the linked S6 TeX, project guide, PDF, and archive endpoint failed. No unexamined S6 proof is used as a mathematical premise below. Section 2 gives a fully written smooth-germ construction for the actual YM holonomy map.

The completed results are:

1. Exact gauge-equivariant refinement maps and the complete Hamiltonian intertwining defect, including its composition law.
2. Smooth holonomy continuation, every parameter derivative, the exact flat-germ kernel, and a quantitative non-Abelian magnetic continuum remainder.
3. Regulator-independent positive-time correlation, high-energy tail, and Schur-memory bounds for the original nonlinear Hamiltonians.
4. A simultaneous spatial/coupling/volume subsequence with a smooth positive-time spectral limit, retaining both the mass at infinite energy and the mass at zero energy.
5. A literal Split Zero cohomology window for the infinite-energy boundary and a strongly continuous positive-energy Hilbert reconstruction from the limiting kernels.

All constants below retain the original state norms and physical spacing. The proofs establish these specified objects. They establish no positive numerical mass lower bound for the limiting four-dimensional theory.

## 1. Original operators and an actual simultaneous sequence

Fix physical spacing `a_0>0`, coupling `g_0>0`, and parameter `beta>0`. For every integer `n>=0`, define

\[
a_n=a_0 2^{-n},\qquad L_n=4\,2^{2n},\qquad
 g_n^2=\frac1{g_0^{-2}+\beta n\log 2}.
\tag{1.1}
\]

This is an explicitly prescribed path. No identification of `beta` with a quantum beta-function coefficient is asserted. The physical half-side is

\[
a_nL_n=4a_0 2^n.
\tag{1.2}
\]

Use precisely the source's open cubical graph with vertices `{-L_n,...,L_n}^3`, positively oriented contained edges `E_n`, and contained elementary faces `P_n`. Write `Q_n=SU(2)^{E_n}` with its original product Haar probability measure `dU_n`. The physical Hilbert space \(\mathcal H_n\) is the invariant subspace under

\[
U_e\longmapsto h_{s(e)}U_eh_{t(e)}^{-1}.
\tag{1.3}
\]

Use `T_alpha=-i sigma_alpha/2`, left derivatives `X_{e,alpha}` and

\[
K_n=\sum_{e\in E_n}E_e,\qquad E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,
\]
\[
V_n(U)=\frac1{2g_n^2a_n}\sum_{p\in P_n}(2-\operatorname{tr}U_p),
\qquad H_n=\frac{2g_n^2}{a_n}K_n+V_n.
\tag{1.4}
\]

Every ordered plaquette word and the full scalar term in `V_n` remain. By [YM1], the physical operator has domain the invariant part of `H^2(Q_n)`, compact resolvent, and a unique positive smooth unit vacuum `psi_n`. Denote its exact ground energy by `E_{0,n}` and put

\[
A_n=H_n-E_{0,n}I\geq0.
\tag{1.5}
\]

The energy shift in (1.5) is recorded explicitly and reappears in the refinement defect below.

### 1.1 Ordered product map and its exact Haar and gauge properties

A coarse vertex with integer coordinate `v` is the fine vertex `2v`. A coarse edge of physical length `a_n` consists of two fine edges of length `a_{n+1}=a_n/2`, in their original order. Define

\[
\pi_n:Q_{n+1}\longrightarrow Q_n,\qquad
(\pi_n U)_e=U_{e,1}U_{e,2}.
\tag{1.6}
\]

The fine links outside these coarse chains remain in `Q_{n+1}` as additional variables. Distinct coarse chains have disjoint fine-edge sets. Haar invariance gives, for integrable `f`,

\[
\int f(U_1U_2)\,dU_1dU_2=\int f(W)\,dW.
\tag{1.7}
\]

Indeed, for each fixed `U_1`, the substitution `W=U_1U_2` is left translation of Haar measure. Fubini on the disjoint chains, followed by integration of the additional variables, proves `(pi_n)_*dU_{n+1}=dU_n`. Consequently

\[
J_n:\mathcal H_n\longrightarrow\mathcal H_{n+1},\qquad J_nf=f\circ\pi_n,
\qquad J_n^*J_n=I.
\tag{1.8}
\]

For a fine gauge transformation, the product on one chain is

\[
(h_sU_{e,1}h_m^{-1})(h_mU_{e,2}h_t^{-1})
=h_s(U_{e,1}U_{e,2})h_t^{-1}.
\tag{1.9}
\]

Thus `J_n` maps physical vectors to physical vectors. Iteration gives `J_{n,k}=J_{k-1}...J_n`; associativity of the original ordered products proves `J_{r,k}J_{n,r}=J_{n,k}`.

### 1.2 Complete kinetic and Hamiltonian defect

For a smooth coarse function,

\[
X_{e,1,\alpha}J_nf=J_nX_{e,\alpha}f,
\]
\[
X_{e,2,\alpha}J_nf
=\sum_{\gamma=1}^3(\operatorname{Ad}_{U_{e,1}})_{\gamma\alpha}
 J_nX_{e,\gamma}f.
\tag{1.10}
\]

The adjoint coefficients in the second expression are constant under differentiation of `U_{e,2}`. They satisfy

\[
\sum_\alpha(\operatorname{Ad}_{U_{e,1}})_{\gamma\alpha}
(\operatorname{Ad}_{U_{e,1}})_{\delta\alpha}=\delta_{\gamma\delta},
\]

because conjugation preserves the original form `-tr(T_gamma T_delta)/2=delta_gamma_delta/4`. Squaring (1.10) and summing therefore proves, including the factor from both subedges,

\[
K_{n+1}J_n=2J_nK_n.
\tag{1.11}
\]

The unused fine edges differentiate `J_nf` to zero; they remain in the original fine Hamiltonian. Define the full defect on `Dom(A_n)` by

\[
\mathcal D_n=A_{n+1}J_n-J_nA_n.
\]

Its coordinate expression is

\[
\boxed{
\mathcal D_n=
\frac{8g_{n+1}^2-2g_n^2}{a_n}J_nK_n
+M_{V_{n+1}-V_n\circ\pi_n}J_n
+(E_{0,n}-E_{0,n+1})J_n.
}
\tag{1.12}
\]

Here `M_f` denotes multiplication by the displayed full function on `Q_{n+1}`. Every fine plaquette, including plaquettes involving additional fine links, occurs in `V_{n+1}`.

The map `J_n` sends `H^2(Q_n)` continuously into `H^2(Q_{n+1})`: apply the chain rule twice to the smooth finite product map, use bounded coefficients on the compact groups, and integrate with (1.7). Thus (1.12) is a bounded map from the graph domain of `A_n` to \(\mathcal H_{n+1}\) at each fixed pair of regulators.

For `s>0`, multiplication of the two resolvents gives the exact bounded-operator identity

\[
\boxed{
(A_{n+1}+s)^{-1}J_n-J_n(A_n+s)^{-1}
=-(A_{n+1}+s)^{-1}\mathcal D_n(A_n+s)^{-1}.
}
\tag{1.13}
\]

To verify it, multiply the left side by `A_{n+1}+s`; the result is `-D_n(A_n+s)^{-1}`. All compositions have the domains just established. Composition retains every intermediate defect:

\[
\boxed{
A_kJ_{n,k}-J_{n,k}A_n
=\sum_{r=n}^{k-1}J_{r+1,k}\mathcal D_rJ_{n,r}.
}
\tag{1.14}
\]

Expanding the right side telescopes adjacent terms, with their exact signs.

### 1.3 Vacuum and centered-state transition data

For a bounded physical coarse observable `f`, let `f'=f circ pi_n`, `m_n=<psi_n,f psi_n>`, and `m_{n+1}=<psi_{n+1},f' psi_{n+1}>`. The corresponding original centered vectors obey

\[
\begin{aligned}
&(f'-m_{n+1})\psi_{n+1}-J_n((f-m_n)\psi_n)\\
&=(f'-m_{n+1})(\psi_{n+1}-J_n\psi_n)
 +(m_n-m_{n+1})J_n\psi_n.
\end{aligned}
\tag{1.15}
\]

This is direct expansion. No compatibility of the two vacua has been assumed.

## 2. Smooth continuum holonomy and retained flat germs

Let `Q=[-3a_0,3a_0]^3`. Work with the actual space of smooth `su(2)`-valued one-forms `A(theta,x)=sum_i A_i(theta,x)dx^i`, where `theta` ranges over an open interval containing zero and each `A(theta,.)` has support in `(-2a_0,2a_0)^3`. A fixed compact parameter interval supplies finite suprema of every displayed derivative. Neither Lie-algebra commutators nor spatial coordinates are removed.

For an oriented path `gamma:[0,ell]->Q`, parameterized by arc length, write

\[
a_\theta(r)=\sum_i\mathcal A_i(\theta,\gamma(r))\dot\gamma^i(r),
\quad U_\theta'(r)=U_\theta(r)a_\theta(r),\quad U_\theta(0)=I.
\tag{2.1}
\]

This is the inverse-transport convention of [YM2], expressed in the original lattice gauge variables. Since `a_theta^*=-a_theta`, differentiating `U_theta U_theta^*` proves unitarity. With

\[
\mathcal A_i^h=h\mathcal A_i h^{-1}-(\partial_i h)h^{-1},
\]

differentiating `h(gamma(0)) U_theta(r) h(gamma(r))^{-1}` proves the gauge transform (1.3). The convention in [YM2] written with `h^{-1}` at the initial endpoint is obtained by the explicit substitution `h -> h^{-1}`.

### 2.1 Every parameter derivative, in its original order

Set `U_theta(r,s)=U_theta(r)^{-1}U_theta(s)`. Differentiating (2.1), and then differentiating the product `(partial_theta U)U^{-1}`, gives

\[
\partial_\theta U_\theta(\ell)
=\int_0^\ell U_\theta(0,r)(\partial_\theta a_\theta(r))
 U_\theta(r,\ell)\,dr.
\tag{2.2}
\]

Repeated differentiation yields, for each integer `k>=1`,

\[
\begin{aligned}
\partial_\theta^kU_\theta(\ell)
={}&\sum_{r=1}^k\sum_{j_1+\cdots+j_r=k\atop j_b\ge1}
\frac{k!}{j_1!\cdots j_r!}
\int_{0<t_1<\cdots<t_r<\ell}
U(0,t_1)a^{(j_1)}(t_1)U(t_1,t_2)\\
&\hspace{26mm}\cdots a^{(j_r)}(t_r)U(t_r,\ell)\,dt_1\cdots dt_r.
\end{aligned}
\tag{2.3}
\]

One proof is induction using (2.2): a derivative either increases one `j_b` or inserts a new derivative into one of the intervening transport intervals. The multinomial coefficients count the allocations of the `k` labeled differentiations; the ordered simplex retains their chronological order. This also follows by differentiating the convergent Picard series on a compact parameter interval, whose differentiated series is dominated by an exponential times a finite polynomial in the derivative suprema.

Writing `M_j=sup_r ||partial_theta^j a_theta(r)||_op`, the unitary factors and the simplex volume give

\[
\boxed{
\|\partial_\theta^kU_\theta(\ell)\|_{\rm op}
\le\sum_{r=1}^k\frac{\ell^r}{r!}
\sum_{j_1+\cdots+j_r=k\atop j_b\ge1}
\frac{k!}{j_1!\cdots j_r!}\prod_{b=1}^r M_{j_b}.
}
\tag{2.4}
\]

The total physical length `ell` remains in this bound. Splitting the path into any number of consecutive pieces leaves the ordered product equal to `U_theta(ell)`, by uniqueness for (2.1). Therefore both its value and every derivative in (2.3) are exactly compatible with (1.6) under arbitrarily many refinements. This is a smooth continuum-to-link continuation for the complete non-Abelian word.

### 2.2 Smooth source algebra and its exact kernel

Let `A_sm` be the algebra of complex smooth germs at `theta=0`. For `q>=0`, define

\[
j^q:A_{\rm sm}\to\mathbb C[\eta]/(\eta^{q+1}),\qquad
j^qf=\sum_{k=0}^q\frac{f^{(k)}(0)}{k!}\eta^k.
\tag{2.5}
\]

The product rule proves that these are algebra homomorphisms. Taylor's formula with integral remainder proves

\[
\ker j^q=\theta^{q+1}A_{\rm sm}.
\tag{2.6}
\]

Indeed, with the first `q+1` derivatives zero,

\[
f(\theta)=\frac{\theta^{q+1}}{q!}
\int_0^1(1-u)^qf^{(q+1)}(u\theta)\,du,
\]

and the integral is smooth in `theta`. Conversely, the product rule gives vanishing derivatives through order `q` for every member of the displayed ideal.

Define `J_infty f=(f^{(k)}(0)/k!)_{k>=0}` with its formal-series product and let `F_flat` be the smooth germs with every derivative at zero equal to zero. The exact sequence is

\[
\boxed{
0\longrightarrow F_{\rm flat}\xrightarrow{\rm inclusion}A_{\rm sm}
\xrightarrow{J_\infty}\operatorname{im}J_\infty\longrightarrow0.
}
\tag{2.7}
\]

The kernel statement follows coefficient by coefficient, and the last map is onto its displayed image by definition. No reconstruction from a formal series has been inserted.

Apply the Split Zero scalar functor from [SZ] to every map (2.5) and every truncation between target rings. A supported germ is mapped to a supported jet; `tau` maps to `tau`. Multiplicativity was proved above, so these are the same typed scalar morphisms as the source's holomorphic first-jet construction, now with the full smooth-germ kernel (2.7) retained.

An explicit YM member of that kernel is available. Fix a rectangle of sides `ell_1,ell_2>0` inside the region where a smooth cutoff `chi` is one, and fix `b!=0`. Set

\[
\eta_0(\theta)=\begin{cases}e^{-1/\theta^2},&\theta\ne0,\\0,&\theta=0,\end{cases}
\quad
\mathcal A_2=b\,x^1\chi(x)\eta_0(\theta)T_3,
\quad \mathcal A_1=\mathcal A_3=0.
\tag{2.8}
\]

Every derivative of `eta_0` is a polynomial in `theta^{-1}` times `e^{-1/theta^2}` away from zero. For each fixed power `p`, `|theta|^{-p}e^{-1/theta^2}->0`, proved by the exponential power-series bound. Induction then gives its smooth extension and vanishing derivatives of every order.

For the original rectangular loop wholly in `chi=1`, direct integration in (2.1) gives

\[
2-\operatorname{tr}U_C(\theta)
=2-2\cos\bigl(b\ell_1\ell_2\eta_0(\theta)/2\bigr).
\tag{2.9}
\]

Its image under every `j^q` is zero. Its exact value is strictly positive for all sufficiently small nonzero `theta`, as its nonzero argument has absolute value less than `2pi`. Thus the actual source germ and its membership in the explicitly computed kernel (2.7) both remain available.

## 3. Quantitative non-Abelian magnetic continuum remainder

All estimates in this section apply to the complete connection space just specified, uniformly on a fixed compact parameter interval. Define, over `Q` and that interval,

\[
M_A=\max_i\sup\|\mathcal A_i\|_{\rm op},\quad
M_F=\max_{i<j}\sup\|F_{ij}\|_F,\quad
M_{\partial F}=\max_{k,i<j}\sup\|\partial_kF_{ij}\|_F,
\]
\[
F_{ij}=\partial_i\mathcal A_j-\partial_j\mathcal A_i
+[\mathcal A_i,\mathcal A_j].
\tag{3.1}
\]

The norm `||.||_F` is the original matrix Frobenius norm, with no division by its dimension. Put

\[
C=M_{\partial F}+2M_AM_F+\frac{a_0}{2}M_F^2.
\tag{3.2}
\]

### 3.1 Exact face integral and its remainder

On one oriented square `[0,a]^2` in directions `i,j`, construct `h(u,v)` by transport first along `(0,0)->(0,v)` and then along `(0,v)->(u,v)` using (2.1). Then `partial_u h=h A_i`, and on `u=0`, `partial_v h=h A_j`. The transformed connection consequently satisfies `A_i^h=0` on the square and `A_j^h(0,v)=0`. Direct substitution in (3.1) proves `F_{ij}^h=hF_{ij}h^{-1}` and

\[
A_j^h(a,v)=C_p(v):=\int_0^a h(u,v)F_{ij}(u,v)h(u,v)^{-1}\,du.
\tag{3.3}
\]

Three boundary transports are identities in this gauge; the original plaquette is the remaining right-edge transport `V`, satisfying `V'=VC_p`, `V(0)=I`. The base gauge value is `h(0,0)=I`, so the plaquette matrix itself is unchanged. Thus

\[
U_p-I=\int_0^a V(v)C_p(v)\,dv,
\qquad \|U_p-I\|_F\le a^2M_F.
\tag{3.4}
\]

Retain the exact remainder

\[
\begin{aligned}
R_p={}&\int_0^a\!\int_0^a
\bigl(hF_{ij}h^{-1}-F_{ij}(0,0)\bigr)\,du\,dv\\
&+\int_0^a(V(v)-I)C_p(v)\,dv,
\qquad U_p-I=a^2F_{ij}(0,0)+R_p.
\end{aligned}
\tag{3.5}
\]

Unitarity and path length give `||h-I||_op <= (u+v)M_A`. It follows that

\[
\|hF_{ij}(u,v)h^{-1}-F_{ij}(0,0)\|_F
\le (u+v)(M_{\partial F}+2M_AM_F).
\]

Also `||V(v)-I||_op <= va M_F` and `||C_p(v)||_F <= aM_F`. Integrating proves

\[
\|R_p\|_F\le a^3(M_{\partial F}+2M_AM_F)+\frac{a^4}{2}M_F^2
\le a^3C\qquad(0<a\le a_0).
\tag{3.6}
\]

### 3.2 The original magnetic sum, with every factor

For `U in SU(2)`, direct expansion gives

\[
\|U-I\|_F^2=4-2\operatorname{tr}U,
\quad
\frac{2-\operatorname{tr}U}{2g^2a}
=\frac{\|U-I\|_F^2}{4g^2a}.
\tag{3.7}
\]

Equations (3.5)–(3.7) give the exact single-face difference

\[
\frac{2-\operatorname{tr}U_p}{2g^2a}
-\frac{a^3}{4g^2}\|F_{ij}(x_p)\|_F^2
=\frac{2a^2\operatorname{Re}\operatorname{tr}(F_{ij}(x_p)^*R_p)
+\|R_p\|_F^2}{4g^2a}.
\tag{3.8}
\]

At level `n`, the support assumption places every nonidentity plaquette inside `Q`; all plaquettes outside the corresponding anchored cube sum have identity edge transports. The original graph boundary is farther away. The cube has exactly `(6a_0/a_n)^3` cells. There are three oriented faces in the anchored sum per cell. These account for every nonzero term of the original magnetic sum; all other terms are exactly zero.

For `f_ij=||F_ij||_F^2`, each coordinate derivative is bounded by `2M_F M_partialF`. Integrating the line-segment derivative estimate within each cube gives the bound `6a_n M_F M_partialF` for its pointwise Riemann discrepancy. Summation of (3.8) over the three orientations, followed by this Riemann estimate, proves

\[
\boxed{
V_n(U[\mathcal A])=
\frac1{4g_n^2}\int_Q\sum_{i<j}\|F_{ij}(x)\|_F^2\,dx+\varepsilon_n,
}
\tag{3.9}
\]
\[
\boxed{
|\varepsilon_n|\le
\frac{3|Q|}{4g_n^2}
\left(2a_nM_FC+a_n^2C^2+6a_nM_FM_{\partial F}\right).
}
\tag{3.10}
\]

The term with `a_n^2` and the complete commutator in (3.1) remain. Along (1.1), the right side tends to zero because `n 2^{-n}->0`. For instance `n<=2^{n/2}` for integers `n>=4`, proved by induction from `n+1<=sqrt(2)n` for `n>=3`. Thus the decay is controlled explicitly. The full leading term is

\[
\frac{g_0^{-2}+\beta n\log2}{4}
\int_Q\sum_{i<j}\|F_{ij}\|_F^2\,dx.
\tag{3.11}
\]

It remains in (3.9), including its growth with `n`. This section evaluates the full magnetic multiplication function on the displayed smooth connection family; the quantum vacuum and kinetic operator remain those of (1.4).

## 4. Uniform positive-time control in the actual interacting vacua

### 4.1 Six original-coordinate loop vectors

Choose the six positively oriented square loops of side `a_0` in the plane `x^3=0`, with lower-left corners

\[
a_0(-3,-3,0),\ a_0(-1,-3,0),\ a_0(1,-3,0),\
a_0(-3,1,0),\ a_0(-1,1,0),\ a_0(1,1,0).
\tag{4.1}
\]

They are edge-disjoint and belong to every graph in (1.1). At level `n`, each has `4*2^n` original edges. Let `W_{i,n}` be the trace of its complete ordered word. Define

\[
\mu_n(f)=\langle\psi_n,f\psi_n\rangle,
\quad r_{i,n}=(W_{i,n}-\mu_nW_{i,n})\psi_n,
\]
\[
R_n:\mathbb C^6\longrightarrow\mathcal H_n,
\quad R_nx=\sum_{i=1}^6 x_i r_{i,n},\quad G_n=R_n^*R_n.
\tag{4.2}
\]

The centering is the explicit orthogonal projection `I-|psi_n><psi_n|` applied to `W_{i,n}psi_n`. Each vector is physical and lies in every power domain of the original elliptic Hamiltonian. Since an `SU(2)` trace is real and lies in `[-2,2]`,

\[
\|r_{i,n}\|^2=\mu_n(W_{i,n}^2)-(\mu_nW_{i,n})^2\le4,
\quad \operatorname{tr}G_n\le24,\quad 0<G_n\preceq24I_6.
\tag{4.3}
\]

Strict positivity follows without changing these vectors: a vanishing linear combination is a continuous identity after division by the positive `psi_n`. Vary one edge in loop `i`, keep all other links equal to identity, and subtract the value at the all-identity configuration. The result is `x_i(tr U-2)=0` for every `U in SU(2)`, forcing `x_i=0`. Edge-disjointness supplies this argument for each `i`.

### 4.2 Correlation derivatives and explicit high-energy tails

For `t>0`, retain the matrix

\[
C_n(t)=R_n^*e^{-tA_n}R_n.
\tag{4.4}
\]

For integer `r>=1`, differentiating spectral scalar multipliers yields

\[
C_n^{(r)}(t)=(-1)^rR_n^*A_n^r e^{-tA_n}R_n.
\]

The scalar derivative of `lambda^r exp(-t lambda)` has its maximum at `lambda=r/t`, with value `(r/(et))^r`. Therefore

\[
\boxed{
0\preceq(-1)^rC_n^{(r)}(t)
\preceq24\left(\frac r{et}\right)^r I_6\quad(r\ge1),
\qquad 0\preceq C_n(t)\preceq24I_6.
}
\tag{4.5}
\]

The same norm bound holds for the holomorphic derivatives on `Re(t)>0`, with `t` replaced by `Re(t)`. The spectral multipliers and their derivatives are bounded there; differentiation in operator norm on compact subsets follows from the difference quotient and a dominating multiplier with one extra derivative. This proves all the asserted differentiability.

For a retained positive time `tau>0`, define the explicit state morphism

\[
S_{\tau,n}=e^{-\tau A_n/2}:\mathcal H_n\to\bigcap_{k\ge0}\operatorname{Dom}(A_n^k),
\qquad R_{\tau,n}=S_{\tau,n}R_n.
\tag{4.6}
\]

The vectors are not divided by their norms. Their Gram matrix is exactly `G_{tau,n}=C_n(tau)`. For every physical energy threshold `Lambda>0`,

\[
\boxed{
0\preceq R_{\tau,n}^*\mathbf1_{[\Lambda,\infty)}(A_n)R_{\tau,n}
\preceq24e^{-\tau\Lambda}I_6.
}
\tag{4.7}
\]

This follows by comparing the scalar multipliers `1_[Lambda,infty)(lambda)e^{-tau lambda}` and `e^{-tau Lambda}` on the entire nonnegative spectrum. Every quantity in (4.5)–(4.7) uses the full operator (1.4). The right sides are independent of `n`, `a_n`, `g_n` and `L_n`.

### 4.3 Extension to a countable separating supply of physical observables

At each graph level, take all monomials in the fundamental link matrix entries and their conjugates and average each monomial over the original compact vertex gauge group. Enumerate these averages over all levels. Each monomial and its average have absolute value at most one. They are smooth physical functions. The real and imaginary parts may also be retained as separate entries with the same bound. Transport an entry introduced at level `r` to level `n>=r` by the exact product pullback `J_{r,n}`.

For completeness, these averages span a dense physical subspace at each fixed level. The polynomial *-algebra contains constants, separates points of the compact product of matrix groups, and is closed under conjugation. The Stone–Weierstrass theorem gives uniform density in continuous functions; continuous functions are dense in Haar `L^2`. Gauge averaging is an orthogonal projection, so averaging this dense space gives density in its physical range. Multiplication by the original positive smooth vacuum is bounded with bounded inverse on the compact group; consequently the centered vectors from these averages span densely in `psi_n`-orthogonal physical space at that level.

Include the six entries (4.1) first. For any finite list of these observables with actual sup bounds `B_i`, put

\[
K_m=\sum_{i=1}^m B_i^2.
\tag{4.8}
\]

The proof of (4.3) gives `tr G_n <= K_m`. Every subsequent estimate for this finite list holds with `24` replaced by `K_m`. No bound independent of the length of the observable list is asserted. This supplies a single countable index set for the diagonal construction in §6, rather than restricting that construction to six modes.

### 4.4 Exact zero-time energy moments, with the full lattice factor

The positive-time bounds have the following exact zero-time companion. In the source's original quaternion coordinates write an arbitrary loop holonomy as

\[
U_C=q_0I-i\sum_{\alpha=1}^3q_\alpha\sigma_\alpha,
\qquad \sum_{\alpha=0}^3q_\alpha^2=1,
\qquad W_C=2q_0.
\]

For a varied original edge of this loop, cyclicity of the trace places its generator at the beginning of an ordered loop word. An inversely traversed edge supplies the corresponding minus sign and conjugated generator. Conjugation acts by the same orthogonal adjoint matrix in (1.10), so in either orientation the sum of derivative squares is unchanged. Direct matrix multiplication gives `tr(T_alpha U_C)=-q_alpha`. Therefore every edge in the loop satisfies

\[
\boxed{\sum_{\alpha=1}^3|X_{e,\alpha}W_C|^2
=\sum_{\alpha=1}^3q_\alpha^2
=1-\frac{W_C^2}{4}.}
\tag{4.9}
\]

For an edge outside the loop, all these derivatives are zero. The complete ground-state identity in [YM1], polarized in the two centered functions, is

\[
\langle r_{i,n},A_n r_{j,n}\rangle
=\frac{2g_n^2}{a_n}\sum_{e,\alpha}
\int\psi_n^2(X_{e,\alpha}W_{i,n})(X_{e,\alpha}W_{j,n})\,dU_n.
\tag{4.10}
\]

This follows directly by expanding the kinetic product derivatives, integrating by parts, and inserting the exact equation `H_n psi_n=E_{0,n} psi_n`; the full multiplication term cancels against the same term in that exact equation. Thus its effects remain in the actual vacuum `psi_n` and its moments. Edge-disjointness in (4.1) makes every off-diagonal integrand zero. Each of the six loops has exactly `4*2^n` edges. Consequently

\[
\boxed{
-C_n'(0)=\int_{[0,\infty)}\lambda\,d\mu_n(\lambda)
=\frac{8g_n^2a_0}{a_n^2}
\operatorname{diag}_{i=1}^6\left(1-\frac{\mu_n(W_{i,n}^2)}4\right).
}
\tag{4.11}
\]

Here `mu_n` in the integral denotes the matrix spectral measure defined in (6.2), and `mu_n(W^2)` denotes the vacuum functional in (4.2); their types and both definitions are explicit. Equivalently, with the original means `m_{i,n}=mu_n(W_{i,n})`, the diagonal entry is

\[
\frac{8a_0}{a_n^2(g_0^{-2}+\beta n\log2)}
\left(1-\frac{(G_n)_{ii}+m_{i,n}^2}{4}\right).
\tag{4.12}
\]

Equations (4.11)–(4.12) retain both the exact regulator growth factor and its exact interacting-vacuum multiplier. They express the complete first spectral moment in measured coordinate entries, including the off-diagonal zeros. All six vectors lie in the operator domain, so the derivative and the finite first moments at zero used here exist at every original finite regulator.

## 5. Uniform retained Schur memory and its raw metric

Fix `tau>0`. Abbreviate `R=R_{tau,n}`, `G=R^*R`, `A=A_n`, and define

\[
P=RG^{-1}R^*,\quad Q=I-P,\quad B=QAR:\mathbb C^6\to Q\mathcal H_n,
\]
\[
D=QAQ:\operatorname{Dom}(A)\cap Q\mathcal H_n\to Q\mathcal H_n.
\tag{5.1}
\]

The multiplier in (4.6) is strictly positive on every finite spectral value and hence has zero kernel. Therefore `R` is injective and its displayed finite Gram inverse exists. Direct multiplication gives `P=P^*=P^2`, `PR=R`, and `QR=0`. These facts retain the original coefficient metric `G`.

### 5.1 Compression domain

The range of `P` is contained in `Dom(A)`. The operator `AP` is bounded finite rank, with adjoint the bounded extension of `PA`. Thus `QAP+PAQ` is bounded self-adjoint. The operator

\[
A-(QAP+PAQ)
\]

on `Dom(A)` is self-adjoint: for real `T` exceeding the bounded perturbation norm, factor its shifts by `+/-iT` using the resolvent of `A`; the remaining factors have convergent Neumann inverses. This symmetric operator has both such shifts onto and is therefore self-adjoint. It commutes with `P` on its domain, whose `P` and `Q` parts are preserved. Its restriction to the reducing `Q` subspace is `D`. Finally `<v,Dv>=<v,Av>>=0`, so `D` is nonnegative. Consequently `(D+s)^{-1}` exists on \(Q\mathcal H_n\) for `s>0` and has norm at most `s^{-1}`.

### 5.2 Bounds with all regulator dependence removed from the right side

Define the full memory, reduced matrix and restored-vector map

\[
\mathcal M_{\tau,n}(s)=B^*(D+s)^{-1}B,
\]
\[
F_{\tau,n}(s)=R^*AR+sG-\mathcal M_{\tau,n}(s),
\qquad L_{\tau,n}(s)=R-(D+s)^{-1}B.
\tag{5.2}
\]

Spectral calculus in (4.6) and the scalar maximum already computed give

\[
\|AR\|^2\le\frac{96}{e^2\tau^2},\qquad
0\preceq R^*AR\preceq\frac{24}{e\tau}I_6.
\tag{5.3}
\]

Since `||Q||<=1`, the first also bounds `||B||^2`. Differentiating the resolvent now proves for every integer `r>=0`

\[
\boxed{
0\preceq(-1)^r\mathcal M_{\tau,n}^{(r)}(s)
=r!B^*(D+s)^{-r-1}B
\preceq\frac{96r!}{e^2\tau^2s^{r+1}}I_6.
}
\tag{5.4}
\]

The identity `Q(A+s)L=0` follows by substitution in (5.2). Since `R^*Q=0`, expansion gives

\[
\boxed{
F_{\tau,n}'(s)=G+B^*(D+s)^{-2}B=L_{\tau,n}(s)^*L_{\tau,n}(s),
}
\tag{5.5}
\]
\[
\boxed{
F_{\tau,n}(s)=L_{\tau,n}(s)^*(A+s)L_{\tau,n}(s),
\quad sG\preceq F_{\tau,n}(s)
\preceq24\left(s+\frac1{e\tau}\right)I_6.
}
\tag{5.6}
\]

For the lower bound, `||Lx||^2=||Rx||^2+||(D+s)^{-1}Bx||^2` by orthogonality. This also proves the uniform raw-metric bound

\[
G\preceq F_{\tau,n}'(s)
\preceq\left(24+\frac{96}{e^2\tau^2s^2}\right)I_6.
\tag{5.7}
\]

Solving `(A+s)(Rx+v)=Ry` in its `P,Q` components yields `F(s)x=Gy` and `v=-(D+s)^{-1}Bx`. Hence

\[
\boxed{
R^*(A+s)^{-1}R=G F(s)^{-1}G.
}
\tag{5.8}
\]

Equations (5.4)–(5.7) bound the memory and restored raw metric across the actual simultaneous regulator path. Equation (5.8) retains both Gram factors and the matrix inverse at each finite regulator.

## 6. Infinite-regulator spectral limit with both endpoint masses retained

Let `X=[0,infty]` be the compact space obtained by adjoining one point at infinite energy. A neighborhood of that point is `(M,infty]`, with the original energy threshold `M`. Define

\[
k_t(\lambda)=e^{-t\lambda}\quad(\lambda<\infty),\qquad k_t(\infty)=0,
\quad t>0.
\tag{6.1}
\]

For the six original vectors define the positive matrix-valued measures

\[
\mu_{n,ij}(B)=\langle r_{i,n},\mathbf1_B(A_n)r_{j,n}\rangle
\quad(B\subset[0,\infty)),\qquad \mu_n(\{\infty\})=0.
\tag{6.2}
\]

Then

\[
G_n=\mu_n(X),\qquad C_n(t)=\int_X k_t\,d\mu_n.
\tag{6.3}
\]

For every finite measurable partition, Cauchy–Schwarz for the spectral projections gives

\[
\sum_b|\mu_{n,ij}(B_b)|
\le\left(\sum_b\|\mathbf1_{B_b}(A_n)r_{i,n}\|^2\right)^{1/2}
\left(\sum_b\|\mathbf1_{B_b}(A_n)r_{j,n}\|^2\right)^{1/2}
\le4.
\tag{6.4}
\]

Thus each entry has total variation at most four, uniformly in `n`.

### 6.1 A single subsequence and its smooth kernel

Here is a direct sequential construction. Fix a retained time `t_*>0`. The map

\[
x:X\to[0,1],\qquad x(\lambda)=e^{-t_*\lambda},\quad x(\infty)=0
\tag{6.5}
\]

is a continuous bijection, with inverse `lambda=-log(x)/t_*` for `x>0` and `infty` for `x=0`. This proves its exact topological type while retaining the energy and time in both directions. Polynomials in `x` with rational complex coefficients form a countable uniformly dense subalgebra of `C(X)`, by ordinary polynomial approximation on `[0,1]`.

For every pair of observable indices from §4.3 and each member of this countable test algebra, consider the sequence after the larger introduction level of the two observables. This eventually defined sequence of integrals is bounded. Repeated subsequence selection and the diagonal sequence give convergence for all of them simultaneously. The total-variation bound extends the limit uniquely to every `f in C(X)`. Positive quadratic combinations remain positive; the representation of a bounded positive functional on a compact space by its finite Borel measure supplies a consistent positive matrix-valued measure `mu` for every finite list. The construction uses one subsequence, denoted `n_k`, for the entire countable list.

In particular,

\[
G_{n_k}\longrightarrow G_\infty=\mu(X),\qquad
C_{n_k}(t)\longrightarrow C_\infty(t)=\int_Xk_t\,d\mu.
\tag{6.6}
\]

For every `r>=0` and compact time interval `[delta,T]` with `delta>0`, the functions `lambda^r e^{-t lambda}`, extended by zero at infinity, are continuous on `X`; their suprema and their next time derivatives are uniformly bounded by (4.5). A finite time grid plus this derivative bound upgrades pointwise convergence to uniform convergence on `[delta,T]`. Applying this to every `r` proves

\[
\boxed{C_{n_k}\longrightarrow C_\infty
\text{ in }C^\infty_{\rm loc}((0,\infty);M_6(\mathbb C)).}
\tag{6.7}
\]

This is an actual subsequential limit along (1.1), not a uniqueness assertion for all regulator subsequences.

### 6.2 Raw infinite-energy mass and zero-energy mass

Define the two retained positive matrices

\[
E_\infty=\mu(\{\infty\}),\qquad Z_0=\mu(\{0\}).
\tag{6.8}
\]

Monotone convergence applied to each positive scalar quadratic form gives

\[
\boxed{
G_\infty=\lim_{t\downarrow0}C_\infty(t)+E_\infty,
\qquad
Z_0=\lim_{t\to\infty}C_\infty(t).
}
\tag{6.9}
\]

At each finite regulator, `mu_n({0})=0` because the vectors (4.2) are orthogonal to the unique vacuum. Formula (6.9) retains the actual zero-energy atom of the limiting measure as an additional datum; its value is not assigned by that finite-regulator identity.

For the explicitly transported vectors (4.6), the measure is

\[
d\nu_{\tau,n}=k_\tau\,d\mu_n,\qquad
\nu_{\tau,n_k}\longrightarrow\nu_\tau=k_\tau\mu.
\tag{6.10}
\]

Multiplication by the continuous function `k_tau` proves convergence. It also gives `nu_tau({infty})=0` and the uniform tail bound (4.7). The entire source measure remains retained. The multiplier has kernel precisely the measures supported at infinity, as proved in §7; its attenuation at each finite energy is the displayed factor `exp(-tau lambda)`.

### 6.3 Limiting resolvents without replacing the raw matrix products

For `s,tau>0`, use the scalar integral `1/(lambda+s)=int_0^infty exp(-(lambda+s)t)dt`. Then (5.8) gives

\[
\begin{aligned}
Z_{\tau,n}(s)
&:=G_{\tau,n}F_{\tau,n}(s)^{-1}G_{\tau,n}\\
&=\int_0^\infty e^{-st}C_n(\tau+t)\,dt
=\int_X\frac{k_\tau(\lambda)}{\lambda+s}\,d\mu_n(\lambda).
\end{aligned}
\tag{6.11}
\]

The multiplier at infinity is zero. The uniform bound `||C_n||<=24` supplies an integrable dominating function `24e^{-st}`. Thus

\[
\boxed{
\lim_{k\to\infty}G_{\tau,n_k}F_{\tau,n_k}(s)^{-1}G_{\tau,n_k}
=\int_0^\infty e^{-st}C_\infty(\tau+t)\,dt.
}
\tag{6.12}
\]

The two original Gram factors and the finite-regulator inverses remain in the left side. An inverse of a limiting Gram matrix is not needed to define the right side.

### 6.4 Simultaneous smooth Schur-memory limits and their endpoint records

The preceding subsequence can retain the full Schur memory itself. Fix a positive time `tau_0` and use the countable set `T={tau_0} union {q t_*:q in Q, q>0}`. For each `tau in T`, the six-vector matrices `B_{tau,n}` and self-adjoint compressions `D_{tau,n}` are exactly those of §5. Define their positive matrix-valued measures on `X` by

\[
\sigma_{\tau,n}(S)
=B_{\tau,n}^*\mathbf1_S(D_{\tau,n})B_{\tau,n}
\quad(S\subset[0,\infty)),
\qquad \sigma_{\tau,n}(\{\infty\})=0.
\tag{6.13}
\]

Their total matrices obey

\[
0\preceq\sigma_{\tau,n}(X)=B_{\tau,n}^*B_{\tau,n}
\preceq\frac{96}{e^2\tau^2}I_6.
\]

The partition argument in (6.4) consequently bounds every entry's total variation by `96/(e^2 tau^2)`. Include their integrals against the same countable test algebra in the diagonal selection in §6.1. The result is one subsequence for all the correlation measures and all `tau in T`, with positive weak limits `sigma_tau`.

For `s>0`, the multiplier `(lambda+s)^{-1}` on finite energies, extended by zero at infinity, is continuous on `X`. The same holds for every derivative in `s`. The uniform derivative bounds in (5.4), followed by the finite-grid argument used for (6.7), prove the actual limits

\[
\boxed{
\mathcal M_{\tau,n_k}\longrightarrow\mathcal M_{\tau,\infty}
\quad\hbox{in }C^\infty_{\rm loc}((0,\infty);M_6(\mathbb C)),
\qquad
\mathcal M_{\tau,\infty}(s)
=\int_X\frac{d\sigma_\tau(\lambda)}{\lambda+s}.
}
\tag{6.14}
\]

The multiplier at infinity in (6.14) is defined to be zero. Set

\[
F_{\tau,\infty}(s)
=-C_\infty'(\tau)+sC_\infty(\tau)
-\mathcal M_{\tau,\infty}(s).
\tag{6.15}
\]

This is the smooth limit of the original finite matrices `F_{tau,n_k}`. In particular the raw restored metric has the exact coefficient limit

\[
\boxed{
\lim_{k\to\infty}L_{\tau,n_k}(s)^*L_{\tau,n_k}(s)
=F_{\tau,\infty}'(s)
=C_\infty(\tau)+\int_X\frac{d\sigma_\tau(\lambda)}{(\lambda+s)^2}.
}
\tag{6.16}
\]

Every inequality in (5.4), (5.6), and (5.7) passes to these displayed finite-matrix limits. The product limit (6.12) also remains valid along this same subsequence; (6.15)–(6.16) require no inverse of a limiting Gram matrix.

Finally retain the endpoint matrices

\[
\Xi_\tau=\sigma_\tau(\{\infty\}),\qquad
Y_\tau=\sigma_\tau(\{0\}),\qquad
K_{\tau,\infty}=\sigma_\tau(X).
\]

The exact scalar multiplier `s/(lambda+s)` is bounded between zero and one at finite energies, and is zero at infinity. Dominated convergence, separately as `s` increases without bound and as `s` decreases to zero, gives

\[
\boxed{
K_{\tau,\infty}
=\lim_{s\to\infty}s\mathcal M_{\tau,\infty}(s)+\Xi_\tau,
\qquad
Y_\tau=\lim_{s\downarrow0}s\mathcal M_{\tau,\infty}(s).
}
\tag{6.17}
\]

Thus the limiting coupling-vector Gram matrix, memory, restored metric, and both of its endpoint atoms are retained together. The same boundary primitive in §7 applied entrywise to `sigma_tau` is the corresponding entry of `Xi_tau`.

## 7. The infinite-energy boundary as a literal Split Zero complex

Let `M(X)` be the complex vector space of finite complex Borel measures on `X`. At support `0`, use the cochain window

\[
C_0^0=0\longrightarrow C_0^1=M(X)\longrightarrow0.
\]

At support `1`, use

\[
C_1^0=\mathbb C\xrightarrow{\ d_1:c\mapsto c\delta_\infty\ }
 C_1^1=M(X)\longrightarrow0.
\tag{7.1}
\]

The support transition is the zero inclusion in degree zero and the identity on `M(X)` in degree one; its cochain square commutes exactly. Restriction to finite energies supplies the explicit cohomology isomorphism

\[
\Theta:H^1(C_1)\xrightarrow{\cong}M([0,\infty)),\qquad
[\nu]\longmapsto\nu|_{[0,\infty)}.
\tag{7.2}
\]

Its inverse extends a finite measure by zero at infinity and takes its class. Composing the maps changes `nu` by precisely `nu({infty}) delta_infty`, which is the displayed boundary with primitive `nu({infty})`. Consequently

\[
\boxed{
\ker(H^1(C_0)\to H^1(C_1))=\mathbb C\delta_\infty,
\quad c\delta_\infty\longleftrightarrow c.
}
\tag{7.3}
\]

There is also an exact identification with the kernel of the positive-time observation map

\[
\mathcal L:M(X)\to C^\infty((0,\infty)),
\qquad \mathcal L\nu(t)=\int_Xk_t\,d\nu.
\]

Indeed, `L(delta_infty)=0`. Conversely, `L nu=0` implies `int x^j d nu=0` for every integer `j>=1`, using (6.5). Every continuous function of `x` vanishing at zero is uniformly approximated by polynomials with zero constant term: approximate by a polynomial and subtract its value at zero. Hence `nu` annihilates all continuous functions vanishing at infinity. It is therefore `c delta_infty`, with `c=nu(X)`, proving

\[
\boxed{\ker\mathcal L=\mathbb C\delta_\infty.}
\tag{7.4}
\]

Apply the Split Zero reconstruction of [SZ] to this two-support complex over `C`. The map sends `(0,c delta_infty)` to the supported zero `(1,0)`, while (7.3) retains its source and unique primitive `c`. Entry by entry, the actual boundary primitive for the spectral limit is exactly `(E_infty)_{ij}`. This ties the retained-zero construction to a concrete infinity in the regulator limit.

The same two-support construction records the full refinement defect (1.13): replace `M(X)` by \(\mathcal H_{n+1}\), replace `d_1` by `A_{n+1}+s` on its actual domain, and take source vector `D_n(A_n+s)^{-1}u`. Its unique primitive is `(A_{n+1}+s)^{-1}D_n(A_n+s)^{-1}u`, with the minus sign in (1.13). Thus both the finite refinement defect and the infinite-energy boundary have explicit typed primitives.

## 8. Positive-time Hilbert reconstruction and energy-window bounds

Use the single subsequence and countable observable list from §6. Form the complex vector space of finite formal sums

\[
v=\sum_b c_b[i_b,t_b],\qquad t_b>0,
\]

and define its exact sesquilinear form by

\[
\langle v,w\rangle
=\sum_{b,c}\overline{c_b}d_c\,
 C_{\infty,i_bj_c}(t_b+s_c).
\tag{8.1}
\]

For a finite list of indices, the spectral expression is the integral of
`sum_ij conjugate(w_i(lambda)) w_j(lambda) d mu_ij(lambda)`, with
`w_i(lambda)=sum_{b:i_b=i}c_b exp(-t_b lambda)`. It is nonnegative. Quotient by the explicitly defined null space and complete; call the resulting Hilbert space `H_lim`.

For `h>=0`, define

\[
T(h)[i,t]=[i,t+h].
\tag{8.2}
\]

The spectral expression for the change in squared norm is the integral of
`(1-exp(-2h lambda)) sum_ij conjugate(w_i)w_j d mu_ij`, which is nonnegative. Hence `T(h)` descends to a contraction. The identical expression with multiplier `exp(-h lambda)` proves that it is positive and self-adjoint. The parameter addition proves `T(h+k)=T(h)T(k)`.

For a finite formal vector, the squared norm of `(T(h)-I)v` is the same integral with multiplier `|exp(-h lambda)-1|^2`. Dominated convergence gives its limit zero as `h downarrow 0`; the positive times `t_b` make the integrand vanish at infinity. Contractivity extends this convergence to every vector of `H_lim`. Thus `T` is a strongly continuous self-adjoint contraction semigroup.

A direct resolvent construction supplies its nonnegative self-adjoint generator. For `s>0`, set

\[
\mathscr R(s)=\int_0^\infty e^{-sh}T(h)\,dh.
\]

This is bounded positive self-adjoint and at most `s^{-1}I`. The semigroup law and Fubini prove
`R(s)-R(t)=(t-s)R(s)R(t)`. For every nonzero `v`, strong continuity at zero gives `<v,R(s)v>>0`, so `R(s)` is injective and has dense range. Spectral calculus for this bounded positive self-adjoint operator defines `R(s)^{-1}` on its range. The resolvent identity shows that `A_lim=R(s)^{-1}-s` is independent of `s`; it is self-adjoint and nonnegative. The Laplace transform of `exp(-h A_lim)` equals the displayed resolvent. Uniqueness of scalar Laplace transforms, applied to every matrix coefficient, identifies this semigroup with `T(h)`. On the formal heat-vector space its energy form is

\[
\boxed{
\langle[i,t],A_{\rm lim}[j,s]\rangle
=-C_{\infty,ij}'(t+s).
}
\tag{8.3}
\]

For a heat vector, the difference quotients of `T(h)` converge in the Hilbert norm: in the spectral formula their multipliers converge to `-lambda exp(-t lambda)` and are dominated in squared norm by `lambda^2 exp(-2t lambda)`, which is bounded and integrable. This proves membership in `Dom(A_lim)` and (8.3). Repetition proves the higher derivative formulas using `lambda^{2r}exp(-2t lambda)`.

The span of these heat vectors is an operator core. Indeed it is dense and preserved by every `T(epsilon)`. For `v in Dom(A_lim)`, `T(epsilon)v` converges to `v` in graph norm as `epsilon` decreases to zero. At fixed positive `epsilon`, approximate `v` in Hilbert norm by finite heat-vector sums; applying `T(epsilon)` upgrades convergence to graph norm because `||A_lim T(epsilon)||<=1/(e epsilon)`. These two approximations prove the core assertion without changing the original sesquilinear form.

The exact retained energy-window estimates are as follows. For `m>0`, `tau>0`, and `t>0`, let

\[
N_\tau(m)=\nu_\tau([0,m]).
\]

On `[0,m]`, `e^{-t lambda}>=e^{-tm}`; on `(m,infty)`, `e^{-t lambda}<=e^{-tm}`. Integrating these two pointwise inequalities, respectively, gives

\[
\boxed{
\frac{C_\infty(\tau+t)-e^{-tm}C_\infty(\tau)}{1-e^{-tm}}
\preceq N_\tau(m)
\preceq e^{tm}C_\infty(\tau+t).
}
\tag{8.4}
\]

The lower matrix may have negative eigenvalues; the displayed Loewner inequality still follows from the integral proof. The zero-energy atom is `Z_0`, as in (6.9). These formulas keep the finite-energy, zero-energy and infinite-energy contributions in their actual spectral positions.

## 9. Verification scope and end state of this continuation

`verify.py` is an offline, standard-library exact-arithmetic checker. It verifies:

- ordered quaternion holonomy composition, gauge cancellation and inverse paths;
- the two-subedge Casimir identity on every four-coordinate polynomial monomial through degree three, using exact polynomial differentiation, and the original loop-trace derivative-square identity;
- the non-Abelian commutator sign and magnetic fourth-order coefficient in a formal plaquette word;
- the raw-Gram Schur lift, its energy and derivative metric, and the compressed-resolvent identity on an explicitly declared rational positive operator with a zero vacuum eigenvalue;
- the complete algebraic defect-composition identity and the retained-jet product coefficients.

These finite checks test formulas and their signs. Their matrices are declared test data, not a computed spectrum of the Yang–Mills Hamiltonians. Infinite-dimensional bounds, smooth-germ kernel, magnetic remainder and subsequence reconstruction are proved in the preceding text; execution of the finite checks is not described as a formal proof of those analytic arguments.

The previous 112-block cubic certificate is separately replayed from the user-supplied script, and its output is compared to the supplied certificate. It is provenance for the preceding continuation, not a calculation of the new regulator-limit spectral measure.

The completed endpoint is a smooth positive-time spectral extension along an explicit simultaneous path, a high-energy tail bound and a Schur-memory derivative bound uniform along that path, exact smooth-source and refinement maps, and retained source data for the two energy endpoints. No numerical value is assigned here to the limiting matrices `E_infty`, `Z_0`, `Xi_tau`, `Y_tau`, or the low-energy measure in (8.4). Nontriviality of a limiting quantum field theory is not established by the positive-time spectral reconstruction alone. No positive mass lower bound for the limiting four-dimensional theory is established by this contribution. No remote repository modification is claimed.
