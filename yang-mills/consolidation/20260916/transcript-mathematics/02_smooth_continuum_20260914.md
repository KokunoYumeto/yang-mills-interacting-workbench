I continued on an **explicit simultaneous spatial-refinement, coupling, and infinite-volume sequence**. The new contribution establishes uniform positive-time bounds for the full interacting Hamiltonians, smooth subsequential limits of their correlation and Schur-memory matrices, and exact records of spectral mass reaching either energy endpoint.

The Yang-Mills update is prepared as an additive contribution:

[Full research note](sandbox:/mnt/data/yang_mills_smooth_continuum_note.md) · [Workbench contribution and verification files](sandbox:/mnt/data/yang_mills_smooth_continuum_continuation.zip) · [Git patch](sandbox:/mnt/data/yang_mills_smooth_continuum.patch)

The S6 reader and research ledger locate its smooth normal-line trivialization and inverse, with theorem references in the frozen project. Fetches of the linked proof bodies failed. Consequently, the smooth continuation below is proved directly from the retrieved Yang-Mills transport equations and the Zeta workbench’s retained-jet construction; I have not used an unexamined S6 theorem as a premise. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/s6/README.md))

## 1. Put the full operator on an actual continuum-volume sequence

Fix $a_0,g_0,\beta>0$, and define
$$
a_n=a_0\,2^{-n},\qquad
L_n=4\,2^{2n},\qquad
g_n^2=\frac1{g_0^{-2}+\beta n\log2}.
$$
Then
$$
a_n\longrightarrow0,
\qquad
a_nL_n=4a_0\,2^n\longrightarrow\infty.
$$

This specifies the coupling path completely. Its parameter $\beta$ has not been identified with a quantum beta-function coefficient.

On the original open graph, retain
$$
H_n=\frac{2g_n^2}{a_n}K_n+V_n,
\quad
K_n=-\sum_{e,\alpha}X_{e,\alpha}^2,
\quad
V_n=\frac1{2g_n^2a_n}\sum_p(2-\operatorname{tr}U_p).
$$
Let $\psi_n$ be its actual positive unit vacuum, $E_{0,n}$ its ground energy, and
$$
A_n=H_n-E_{0,n}I.
$$
The physical domain, gauge action, and ground-state identity used here are the workbench’s original ones. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md))

### Exact refinement and its complete defect

A coarse edge consists of two consecutive fine edges. Define
$$
\pi_n:SU(2)^{E_{n+1}}\to SU(2)^{E_n},
\qquad
(\pi_nU)_e=U_{e,1}U_{e,2},
$$
and
$$
J_n:\mathcal H_n\to\mathcal H_{n+1},
\qquad J_nf=f\circ\pi_n.
$$

Haar invariance proves $J_n^*J_n=I$. Gauge covariance follows from the exact cancellation
$$
(h_sU_{e,1}h_m^{-1})(h_mU_{e,2}h_t^{-1})
=h_s(U_{e,1}U_{e,2})h_t^{-1}.
$$

Differentiation of the ordered product gives
$$
X_{e,1,\alpha}J_nf=J_nX_{e,\alpha}f,
$$
$$
X_{e,2,\alpha}J_nf
=\sum_\gamma
(\operatorname{Ad}_{U_{e,1}})_{\gamma\alpha}
J_nX_{e,\gamma}f.
$$
The adjoint matrix preserves the original generator metric. Squaring and summing therefore proves
$$
K_{n+1}J_n=2J_nK_n.
$$

The **complete Hamiltonian transition defect** is consequently
$$
\boxed{
\begin{aligned}
\mathcal D_n
&:=A_{n+1}J_n-J_nA_n\\
&=\frac{8g_{n+1}^2-2g_n^2}{a_n}J_nK_n
+M_{V_{n+1}-V_n\circ\pi_n}J_n
+(E_{0,n}-E_{0,n+1})J_n .
\end{aligned}}
$$
Here $M_f$ is multiplication by the displayed fine-configuration function. Every additional fine plaquette remains in $V_{n+1}$.

For $s>0$, this produces the bounded-operator identity
$$
\boxed{
(A_{n+1}+s)^{-1}J_n-J_n(A_n+s)^{-1}
=-(A_{n+1}+s)^{-1}\mathcal D_n(A_n+s)^{-1}.
}
$$
The note proves the graph-domain mapping and the telescoping composition law across arbitrarily many levels.

Thus refinement now carries its full kinetic, magnetic, and vacuum-energy discrepancy as explicit data.

## 2. Smooth continuation retains the entire smooth germ

The workbench specifies ordered continuum transport through
$$
U'(r)=U(r)\mathcal A(\dot\gamma(r)),\qquad U(0)=I.
$$
Its interval concatenations agree exactly with the link-product refinement above. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_WILSON_SCHUR_MEMORY.md))

For a smooth parameter-dependent connection, the first derivative is
$$
\partial_\theta U_\theta(\ell)
=
\int_0^\ell
U_\theta(0,r)\,
\partial_\theta\mathcal A_\theta(\dot\gamma(r))\,
U_\theta(r,\ell)\,dr.
$$
The note writes every higher derivative as an ordered simplex integral, retaining every derivative allocation and multinomial coefficient. Unitarity bounds those integrals in terms of the total physical path length and connection-derivative suprema, independently of the number of subdivisions.

There is an important additional piece of retained information when extending the Zeta workbench’s jet construction to smooth germs. The source supplies the typed first-jet algebra morphism; the following construction computes the smooth kernel explicitly. ([GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7ea0a49945390eae14d3160a5730858899768b5f/workbenches/split-support-rees-trace/RESEARCH_NOTE.md))

Let $\mathcal A_{\mathrm{sm}}$ be the algebra of complex smooth germs at $\theta=0$. Define
$$
j^qf=\sum_{k=0}^q\frac{f^{(k)}(0)}{k!}\eta^k
\quad\text{in }\mathbb C[\eta]/(\eta^{q+1}).
$$
The product rule proves multiplicativity. Taylor’s integral formula proves
$$
\ker j^q=\theta^{q+1}\mathcal A_{\mathrm{sm}}.
$$
Retaining all jets gives the exact sequence
$$
\boxed{
0\longrightarrow\mathcal F_{\mathrm{flat}}
\longrightarrow\mathcal A_{\mathrm{sm}}
\xrightarrow{J_\infty}\operatorname{im}J_\infty
\longrightarrow0,
}
$$
where $\mathcal F_{\mathrm{flat}}$ consists precisely of germs whose derivatives of every order vanish at zero.

An actual Yang-Mills holonomy realizes that kernel. Take
$$
\eta_0(\theta)=
\begin{cases}
e^{-1/\theta^2},&\theta\ne0,\\
0,&\theta=0,
\end{cases}
$$
and
$$
\mathcal A_2=b\,x^1\chi(x)\eta_0(\theta)T_3,
\qquad \mathcal A_1=\mathcal A_3=0.
$$
For a rectangle of sides $\ell_1,\ell_2$ contained in $\chi=1$,
$$
\boxed{
2-\operatorname{tr}U_C(\theta)
=
2-2\cos\!\left(\frac{b\ell_1\ell_2\eta_0(\theta)}2\right).
}
$$
Every jet is zero, while the displayed value is strictly positive for sufficiently small nonzero $\theta$.

The source germ, its holonomy, and its exact kernel membership all remain recorded.

### A quantitative full magnetic remainder

For smooth connections supported in $(-2a_0,2a_0)^3$, put
$$
Q=[-3a_0,3a_0]^3,
\qquad
F_{ij}=\partial_i\mathcal A_j-\partial_j\mathcal A_i+
[\mathcal A_i,\mathcal A_j].
$$
Define
$$
M_A=\max_i\sup\|\mathcal A_i\|_{\mathrm{op}},\quad
M_F=\max_{i<j}\sup\|F_{ij}\|_F,\quad
M_{\partial F}=\max_{k,i<j}\sup\|\partial_kF_{ij}\|_F,
$$
and
$$
C=M_{\partial F}+2M_AM_F+\frac{a_0}{2}M_F^2.
$$

An axial gauge constructed from the original ordered transports gives
$$
U_p-I=a_n^2F_{ij}(x_p)+R_p,
\qquad
\|R_p\|_F\le a_n^3C.
$$
Using the exact identity
$$
\|U-I\|_F^2=4-2\operatorname{tr}U
$$
and counting the original plaquettes proves
$$
\boxed{
V_n(U[\mathcal A])
=
\frac1{4g_n^2}\int_Q\sum_{i<j}\|F_{ij}\|_F^2\,dx+\varepsilon_n,
}
$$
with
$$
\boxed{
|\varepsilon_n|
\le
\frac{3|Q|}{4g_n^2}
\left(
2a_nM_FC+a_n^2C^2+
6a_nM_FM_{\partial F}
\right).
}
$$

Along the specified path, this error tends to zero because $n2^{-n}\to0$. The complete leading curvature term retains its factor
$$
\frac{g_0^{-2}+\beta n\log2}{4}.
$$
Its growth remains explicit.

## 3. Uniform control for the actual interacting quantum vacua

Choose six edge-disjoint square loops of side $a_0$, with lower-left corners
$$
a_0(-3,-3,0),\ a_0(-1,-3,0),\ a_0(1,-3,0),
$$
$$
a_0(-3,1,0),\ a_0(-1,1,0),\ a_0(1,1,0).
$$
At level $n$, every loop contains exactly $4\,2^n$ original edges.

Let $W_{i,n}$ be its complete ordered trace, and define
$$
r_{i,n}=
\bigl(W_{i,n}-\langle\psi_n,W_{i,n}\psi_n\rangle\bigr)\psi_n,
$$
$$
R_nx=\sum_{i=1}^6x_ir_{i,n},
\qquad
G_n=R_n^*R_n,
\qquad
C_n(t)=R_n^*e^{-tA_n}R_n.
$$
Because each trace lies in $[-2,2]$,
$$
\operatorname{tr}G_n\le24.
$$

For every $r\ge1$ and $t>0$,
$$
\boxed{
0\preceq(-1)^rC_n^{(r)}(t)
\preceq24\left(\frac r{et}\right)^rI_6.
}
$$
The proof is the spectral multiplier identity
$$
(-1)^rC_n^{(r)}(t)=R_n^*A_n^re^{-tA_n}R_n
$$
and the exact maximum
$$
\sup_{\lambda\ge0}\lambda^re^{-t\lambda}
=\left(\frac r{et}\right)^r.
$$

For the explicit heat-transported vectors
$$
R_{\tau,n}=e^{-\tau A_n/2}R_n,
$$
the high-energy tail satisfies
$$
\boxed{
0\preceq
R_{\tau,n}^*\mathbf1_{[\Lambda,\infty)}(A_n)R_{\tau,n}
\preceq24e^{-\tau\Lambda}I_6.
}
$$

These right-hand sides are independent of lattice spacing, coupling, and volume.

### The zero-time energy matrix is also explicit

For one original loop edge, write
$$
U_C=q_0I-i\sum_{\alpha=1}^3q_\alpha\sigma_\alpha.
$$
Direct multiplication gives
$$
\sum_\alpha|X_{e,\alpha}W_C|^2
=\sum_{\alpha=1}^3q_\alpha^2
=1-\frac{W_C^2}{4}.
$$
Polarizing the full ground-state identity and using edge-disjointness therefore proves
$$
\boxed{
-C_n'(0)
=
\frac{8g_n^2a_0}{a_n^2}
\operatorname{diag}_{i=1}^6
\left(
1-\frac{\langle\psi_n,W_{i,n}^2\psi_n\rangle}{4}
\right).
}
$$

Thus the complete first spectral moment has a known regulator factor and an exact interacting-vacuum multiplier. The note also expresses that multiplier through the original means and diagonal Gram entries.

## 4. The retained Schur memory now has uniform bounds and smooth limits

The workbench already supplies full nonlinear transport and retained state maps. The continuation applies its Schur construction to the heat-transported physical vectors above. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_TENSOR_TRANSFER.md))

For fixed $\tau>0$, abbreviate $R=R_{\tau,n}$, $G=R^*R$, and define
$$
P=RG^{-1}R^*,\qquad Q=I-P,
$$
$$
B=Q A_nR,\qquad
D=QA_nQ
\quad\text{on }\operatorname{Dom}(A_n)\cap Q\mathcal H_n.
$$
The note proves self-adjointness and nonnegativity of this compression through the bounded finite-rank off-diagonal operator.

Set
$$
\mathcal M_{\tau,n}(s)=B^*(D+s)^{-1}B,
$$
$$
F_{\tau,n}(s)=R^*A_nR+sG-\mathcal M_{\tau,n}(s),
$$
$$
L_{\tau,n}(s)=R-(D+s)^{-1}B.
$$

The heat multiplier gives
$$
\|A_nR\|^2\le\frac{96}{e^2\tau^2}.
$$
Consequently, for every $r\ge0$,
$$
\boxed{
0\preceq(-1)^r\mathcal M_{\tau,n}^{(r)}(s)
\preceq
\frac{96r!}{e^2\tau^2s^{r+1}}I_6.
}
$$

The exact metric and resolvent identities remain
$$
\boxed{
F_{\tau,n}'(s)
=G+B^*(D+s)^{-2}B
=L_{\tau,n}(s)^*L_{\tau,n}(s),
}
$$
$$
\boxed{
R^*(A_n+s)^{-1}R
=G\,F_{\tau,n}(s)^{-1}G.
}
$$

The contribution then constructs **one subsequence** for a countable separating supply of physical observables and a countable supply of positive heat times such that
$$
C_{n_k}\longrightarrow C_\infty,
\qquad
\mathcal M_{\tau,n_k}\longrightarrow\mathcal M_{\tau,\infty}
$$
in $C^\infty_{\mathrm{loc}}((0,\infty))$.

The memory limit has the retained measure representation
$$
\mathcal M_{\tau,\infty}(s)
=\int_{[0,\infty]}\frac{d\sigma_\tau(\lambda)}{\lambda+s},
$$
with the multiplier defined as zero at infinity. In particular,
$$
\boxed{
\lim_kL_{\tau,n_k}(s)^*L_{\tau,n_k}(s)
=
C_\infty(\tau)+
\int_{[0,\infty]}
\frac{d\sigma_\tau(\lambda)}{(\lambda+s)^2}.
}
$$

The original finite-regulator matrix product also converges:
$$
\boxed{
\lim_k
G_{\tau,n_k}F_{\tau,n_k}(s)^{-1}G_{\tau,n_k}
=
\int_0^\infty e^{-st}C_\infty(\tau+t)\,dt.
}
$$
This formula requires no inverse of a limiting Gram matrix.

## 5. Split Zero now records the spectral infinity itself

Let
$$
X=[0,\infty]
$$
retain the original finite energy coordinate and one endpoint at infinite energy. The original vectors define positive matrix measures
$$
\mu_{n,ij}(S)
=
\langle r_{i,n},\mathbf1_S(A_n)r_{j,n}\rangle.
$$
Along the constructed subsequence, retain their weak limit $\mu$, and set
$$
E_\infty=\mu(\{\infty\}),
\qquad
Z_0=\mu(\{0\}).
$$

Monotone convergence gives the exact endpoint identities
$$
\boxed{
G_\infty=\lim_{t\downarrow0}C_\infty(t)+E_\infty,
\qquad
Z_0=\lim_{t\to\infty}C_\infty(t).
}
$$

There is a literal two-support cochain construction for the first endpoint:
$$
C_0:\quad 0\longrightarrow\mathcal M(X)\longrightarrow0,
$$
$$
C_1:\quad
\mathbb C\xrightarrow{\,c\mapsto c\delta_\infty\,}
\mathcal M(X)\longrightarrow0,
$$
where $\mathcal M(X)$ is the vector space of finite complex Borel measures.

Restriction to finite energies induces
$$
H^1(C_1)\xrightarrow{\cong}\mathcal M([0,\infty)).
$$
Its inverse extends a measure by zero at infinity and takes its class. The two compositions differ from the original measure by exactly
$$
\nu(\{\infty\})\delta_\infty.
$$
Therefore
$$
\boxed{
\ker\!\left(H^1(C_0)\to H^1(C_1)\right)
=\mathbb C\delta_\infty,
}
$$
and the boundary primitive is the coefficient of $\delta_\infty$.

This is also exactly the kernel of the positive-time observation map
$$
\mathcal L\nu(t)=\int_Xe^{-t\lambda}\,d\nu(\lambda),
$$
with its multiplier zero at infinity. To prove the converse kernel inclusion, use
$$
x=e^{-t_*\lambda},\qquad
\lambda=-\frac{\log x}{t_*}.
$$
Vanishing Laplace observations annihilate every $x^j$, $j\ge1$. Polynomial approximation then annihilates every continuous function vanishing at infinity, forcing $\nu=c\delta_\infty$.

Entry by entry, the actual retained boundary primitive is $(E_\infty)_{ij}$.

### A reconstructed positive generator and an infrared measurement formula

The limiting kernels define
$$
\langle[i,t],[j,s]\rangle=C_{\infty,ij}(t+s).
$$
Quotienting its explicitly defined null space and completing gives a Hilbert space with
$$
T(h)[i,t]=[i,t+h].
$$
The note proves that $T$ is a strongly continuous positive self-adjoint contraction semigroup and constructs its nonnegative generator $A_{\mathrm{lim}}$, with
$$
\langle[i,t],A_{\mathrm{lim}}[j,s]\rangle
=-C_{\infty,ij}'(t+s).
$$

For the actual low-energy matrix
$$
N_\tau(m)=\int_{[0,m]}e^{-\tau\lambda}\,d\mu(\lambda),
$$
direct integration of scalar exponential inequalities gives
$$
\boxed{
\frac{C_\infty(\tau+t)-e^{-tm}C_\infty(\tau)}
{1-e^{-tm}}
\preceq N_\tau(m)
\preceq e^{tm}C_\infty(\tau+t).
}
$$

This relates the infrared spectral content directly to the retained continuum-time correlations, while keeping the zero-energy and infinite-energy atoms explicit.

## Verification and workbench status

The new checker passed **76 exact assertions across 26 check families**, including ordered non-Abelian products, the two-subedge Casimir factor, the loop-energy identity, Schur metric and resolvent identities with their raw Gram factors, and refinement-defect signs. The earlier **112-block cubic certificate reproduced byte-for-byte**. The finite test matrices are declared algebraic fixtures; the analytic results are supplied as written proofs.

The patch adds
```text
yang-mills/continuations/20260914-splitzero-smooth-continuum/
```
with the note, executable, verification reports, provenance, and research-log entry. It was applied and retested in a fresh local tree. **No remote GitHub modification occurred**; publishing requires the GitHub connection shown above.

The completed advance is a connected continuation construction with exact refinement defects, controlled smooth magnetic remainders, regulator-uniform positive-time bounds, smooth correlation and memory subsequences, and retained spectral endpoints. The endpoint matrices and low-energy measures have not been numerically determined. A nontrivial four-dimensional continuum Yang-Mills theory and a positive continuum mass lower bound have not been established by this contribution.

---

**Sources:**

- [https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/s6/README.md](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/s6/README.md)
