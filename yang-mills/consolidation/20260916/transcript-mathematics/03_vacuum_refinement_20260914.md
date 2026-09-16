I advanced the continuum mathematics and opened **pull request #4: “Continue continuum control: vacuum refinement, infrared Schur budget, retained state kernel.”** Its final commit is `dc390930a8d2774e93481206602973caff7aa7da`. The pull request is open; nothing has been merged into `main`. 

[Full mathematical note](sandbox:/mnt/data/yang_mills_vacuum_refinement_note.md) · [Research package and executable verification](sandbox:/mnt/data/yang_mills_vacuum_refinement_research.zip) · [Exact Git patch](sandbox:/mnt/data/yang_mills_vacuum_refinement.patch)

The strongest added estimate is **inverse-energy integrability of the full interacting Hamiltonian’s Schur memory, uniformly over the regulator sequence**:
$$
\boxed{
\int_{(0,\infty)}\frac{d\sigma_n(\lambda)}{\lambda}
\preceq K_n
\preceq \frac{24}{e\tau}I_6.
}
$$
It supplies a quantitative infrared bound, an exact zero-energy limit-order correction, and sharper bounds on every memory derivative. The contribution also constructs refinement in the interacting vacuum measure and corrects a spectral-detection inference in the preceding note through an explicit cohomological comparison.

## 1. Uniform infrared control for the full interacting Hamiltonian

Retain the sequence
$$
a_n=a_0\,2^{-n},\qquad
L_n=4\,2^{2n},\qquad
g_n^2=(g_0^{-2}+\beta n\log2)^{-1},
$$
and the original operator
$$
H_n=
-\frac{2g_n^2}{a_n}\sum_{e,\alpha}X_{e,\alpha}^2
+\frac1{2g_n^2a_n}\sum_p(2-\operatorname{tr}U_p),
\qquad
A_n=H_n-E_{0,n}I.
$$
Here $E_{0,n}$ is its actual ground energy, and $\psi_n$ is its positive unit vacuum. The prescribed parameter $\beta$ remains explicit; no quantum beta-function coefficient is assigned to it. The operator, physical domains, and vacuum are those of the inspected finite-box source. 

Use six positively oriented square loops of physical side $a_0$, in the $x^1,x^2$ plane at $x^3=0$, with lower-left corners
$$
a_0\{(-3,-3,0),(-1,-3,0),(1,-3,0),
(-3,1,0),(-1,1,0),(1,1,0)\}.
$$
Their edge sets are disjoint. Let $O_{i,n}$ be their complete ordered fundamental traces, and define
$$
r_{i,n}=
\bigl(O_{i,n}-\langle\psi_n,O_{i,n}\psi_n\rangle\bigr)\psi_n,
\qquad
R_{0,n}x=\sum_{i=1}^6x_i r_{i,n}.
$$
Each trace lies in $[-2,2]$, so the exact variance formula gives
$$
R_{0,n}^*R_{0,n}\preceq
\operatorname{tr}(R_{0,n}^*R_{0,n})I_6
\preceq24I_6.
$$

Fix a physical heat time $\tau>0$, and put
$$
R_n=e^{-\tau A_n/2}R_{0,n},\qquad G_n=R_n^*R_n.
$$
The six vectors are independent: varying one edge in each loop forces the corresponding coefficient of any constant linear combination to vanish. The heat multiplier is injective, so $G_n$ remains positive definite.

For the following calculation suppress only the written subscript $n$, and define the typed operators
$$
P=RG^{-1}R^*,\qquad Q=I-P,
$$
$$
K=R^*AR:\mathbb C^6\to\mathbb C^6,
\qquad B=QAR:\mathbb C^6\to Q\mathcal H,
$$
$$
D=QAQ:
\operatorname{Dom}(A)\cap Q\mathcal H\to Q\mathcal H.
$$

The domain argument is retained in the note. Since the range of $R$ lies in every power domain of $A$, $AP$ is bounded and finite rank. Its adjoint is the bounded extension of $PA$. Subtracting $QAP+PAQ$ from $A$ gives a self-adjoint operator with reducing subspaces $P\mathcal H,Q\mathcal H$. Its restriction to $Q\mathcal H$ is $D$, and
$$
\langle v,Dv\rangle=\langle v,Av\rangle\ge0.
$$

For $s>0$, set
$$
M(s)=B^*(D+s)^{-1}B,\qquad
F(s)=K+sG-M(s),
$$
$$
L(s)=R-(D+s)^{-1}B.
$$
Substitution proves
$$
Q(A+s)L(s)=0,
$$
and expansion with the original inner products gives
$$
\boxed{
F(s)=L(s)^*(A+s)L(s),\qquad
F'(s)=L(s)^*L(s)
=G+B^*(D+s)^{-2}B.
}
$$
Consequently,
$$
F(s)\succeq sL(s)^*L(s)\succeq sG,
$$
which proves
$$
\boxed{0\preceq M(s)\preceq K.}
$$

This bound remains finite as $s\downarrow0$.

Let
$$
\sigma(S)=B^*E_D(S)B.
$$
Applying monotone convergence to every scalar contraction $x^*\sigma x$ proves
$$
\sigma(\{0\})=0,\qquad
\int_{(0,\infty)}\lambda^{-1}\,d\sigma(\lambda)\preceq K.
$$
Moreover,
$$
K=R_0^*Ae^{-\tau A}R_0
\preceq
\left(\sup_{\lambda\ge0}\lambda e^{-\tau\lambda}\right)R_0^*R_0
\preceq\frac{24}{e\tau}I_6.
$$
Thus, for every regulator and every $\epsilon>0$,
$$
\boxed{
\sigma_n([0,\epsilon])
\preceq\epsilon K_n
\preceq\frac{24\epsilon}{e\tau}I_6.
}
$$

The same inverse-energy measure yields, for every integer $r\ge1$,
$$
\boxed{
0\preceq(-1)^rM_n^{(r)}(s)
\preceq
\frac{r!\,r^r}{(r+1)^{r+1}s^r}K_n.
}
$$
Indeed, writing $d\alpha_n=\lambda^{-1}d\sigma_n$, the derivative integrand is
$$
\frac{r!\lambda}{(\lambda+s)^{r+1}}.
$$
The derivative of its scalar factor without $r!$ is
$$
\frac{s-r\lambda}{(\lambda+s)^{r+2}},
$$
so its maximum occurs at $\lambda=s/r$, giving exactly the displayed constant.

In particular,
$$
G_n\preceq F_n'(s)\preceq G_n+\frac{K_n}{4s},
\qquad
sF_n'(s)\preceq F_n(s).
$$
The original resolvent coordinates remain
$$
\boxed{
R_n^*(A_n+s)^{-1}R_n
=G_nF_n(s)^{-1}G_n.
}
$$

## 2. Refinement now retains the interacting vacuum and every cross term

The second calculation supplies the measure-level refinement underlying those spectral quantities.

Fix $r<n$, let $b=2^{n-r}$, and use the ordered coarse-link map
$$
\pi_{r,n}(U)_e=U_{e,1}\cdots U_{e,b}.
$$
An explicit global coordinate map retains the coarse product $W_e$, the first $b-1$ links in every chain, and every unused fine link. Its inverse sets
$$
U_{e,b}=(U_{e,1}\cdots U_{e,b-1})^{-1}W_e.
$$
Haar translation in the last link proves
$$
dU_n=dW\,dz
$$
in these coordinates.

Write $\rho_n=\psi_n^2$. The actual coarse marginal and conditional map are
$$
m_{r,n}(W)=
\int\rho_n\!\left(\Phi_{r,n}^{-1}(W,z)\right)dz,
$$
$$
(\mathsf Ef)(W)=
\frac{\int f(\Phi_{r,n}^{-1}(W,z))
\rho_n(\Phi_{r,n}^{-1}(W,z))\,dz}{m_{r,n}(W)},
\qquad
\mathsf Jg=g\circ\pi_{r,n}.
$$
Fubini proves the typed identities
$$
\mathsf J:L^2(m_{r,n}dW)\to L^2(\rho_n dU_n),
\qquad
\mathsf J^*=\mathsf E,\qquad
\mathsf E\mathsf J=I.
$$
The comparison with the original coarse vacuum retains the density ratio:
$$
\langle f,g\rangle_{m_{r,n}}
=
\int\overline f g\,
\frac{m_{r,n}}{\rho_r}\,\rho_r\,dW.
$$

### The density derivative

For the prefix $P_{e,j-1}=U_{e,1}\cdots U_{e,j-1}$, define
$$
a_{e,j;\alpha\beta}
=(\operatorname{Ad}_{P_{e,j-1}})_{\alpha\beta},
\qquad
Y_{e,\alpha}
=\frac1b\sum_{j,\beta}
a_{e,j;\alpha\beta}X_{e,j,\beta}.
$$
Direct differentiation and the adjoint-matrix identities prove
$$
Y_{e,\alpha}\mathsf Jg=\mathsf JX_{e,\alpha}g,
\qquad
\langle Y_{e,\alpha},Y_{f,\gamma}\rangle
=b^{-1}\delta_{ef}\delta_{\alpha\gamma}.
$$
Each coefficient is independent of its differentiated link, so $Y_{e,\alpha}$ has Haar divergence zero.

The exact centered density derivative is
$$
S_{e,\alpha}
=
Y_{e,\alpha}\log\rho_n
-\mathsf J(X_{e,\alpha}\log m_{r,n}).
$$
Integration by parts gives
$$
\boxed{
\mathsf ES_{e,\alpha}=0,\qquad
X_{e,\alpha}\mathsf Ef
=
\mathsf E(Y_{e,\alpha}f)
+\mathsf E(fS_{e,\alpha}).
}
$$

For a smooth physical $f$, define
$$
g=\mathsf Ef,\qquad h=f-\mathsf Jg,\qquad
v_{e,\alpha}=\mathsf E(hS_{e,\alpha}).
$$
Then $\mathsf Eh=0$ and $\mathsf EY_{e,\alpha}h=-v_{e,\alpha}$.

The vertical derivative retains the fine-link components
$$
(\nabla_vf)_{e,j,\beta}
=
X_{e,j,\beta}f
-\sum_\alpha a_{e,j;\alpha\beta}Y_{e,\alpha}f,
$$
together with every unused-edge derivative. Squaring this expression proves
$$
\sum|Xf|^2=b\sum|Yf|^2+|\nabla_vf|^2.
$$

Applying the workbench’s full ground-state identity therefore gives the **complete three-square formula**
$$
\boxed{
\begin{aligned}
q_{A_n}(\psi_nf)
={}&\kappa_nb\int m_{r,n}
 \sum_{e,\alpha}|X_{e,\alpha}g-v_{e,\alpha}|^2\,dW\\
&+\kappa_nb\int\rho_n
 \sum_{e,\alpha}|Y_{e,\alpha}h+\mathsf Jv_{e,\alpha}|^2\,dU_n\\
&+\kappa_n\int\rho_n|\nabla_vh|^2\,dU_n,
\end{aligned}}
$$
where
$$
\kappa_n=\frac{2g_n^2}{a_n},
\qquad
\kappa_nb=
\frac{2a_r}{a_n^2(g_0^{-2}+\beta n\log2)}.
$$

In its expanded form, the interaction between retained variables and fiber fluctuations includes exactly
$$
-2\kappa_nb\,\operatorname{Re}
\int m_{r,n}\sum_{e,\alpha}
\overline{X_{e,\alpha}g}\,
\mathsf E(hS_{e,\alpha})\,dW.
$$
That term remains in the identity.

The Split Zero comparison is now literal:
$$
L^2(\rho_n dU_n)/\ker\mathsf E
\xrightarrow{\;\cong\;}
L^2(m_{r,n}dW),
\qquad
[f]\longmapsto\mathsf Ef,
$$
with inverse $g\mapsto[\mathsf Jg]$. The killed-class primitive is the original $h\in\ker\mathsf E$, whose full energy interaction appears above. This uses the inspected transported-class construction with its actual incoming map and quotient. 

## 3. Smooth continuation with its exact ultraviolet cost

I recovered the S6 formula
$$
H(x)=e^{-2\pi i\varepsilon\gamma(x)}
$$
and checked its deck equivariance and mutually inverse maps
$$
[x,z]\longmapsto([x],z/H(x)),
\qquad
([x],w)\longmapsto[x,wH(x)].
$$
The computation retains $\gamma A=\gamma$, $\gamma(v)=\varepsilon$, and
$$
H(Ax+v/m)=e^{-2\pi i/m}H(x).
$$
These are the actual formulas in the S6 finite-filling source. 

For Yang-Mills, the contribution constructs a smooth local right inverse of the **entire finite-link holonomy map at every reference configuration**.

Fix $U^0\in SU(2)^{E_r}$. Choose
$$
e^{K_e^0}=U_e^0,\qquad
K_e(U)=\log((U_e^0)^{-1}U_e)
$$
on its explicit relative-logarithm neighborhood. In disjoint central tubes around the original edges, set
$$
\mathcal A_e(U)=
\frac1{a_r}
\left(
\frac{p_0(t)}{I_0}K_e^0+
\frac{p_1(t)}{I_1}K_e(U)
\right)
\chi\!\left(\frac{y}{\epsilon a_r}\right)dx_i,
$$
where the two longitudinal supports are ordered and disjoint,
$$
I_j=\int p_j(t)\,dt\ne0,\qquad
J_j=\int p_j(t)^2dt,\qquad
J_\chi=\int_{\mathbb R^2}|\nabla\chi|^2.
$$
The note specifies the supports and tube radii.

The original transport equation gives, edge by edge,
$$
\boxed{
\operatorname{Hol}_e(\mathcal A(U))
=e^{K_e^0}e^{K_e(U)}=U_e.
}
$$
This also covers reference links $U_e^0=-I$, because the varying logarithm is taken at the relative identity.

For the same constructed connection, direct differentiation gives
$$
\boxed{
\int_{\mathbb R^3}\sum_{i<j}\|F_{ij}\|_F^2\,dx
=
\frac{J_\chi}{a_r}\sum_{e\in E_r}
\left(
\frac{J_0}{I_0^2}\|K_e^0\|_F^2+
\frac{J_1}{I_1^2}\|K_e(U)\|_F^2
\right).
}
$$
The magnetic curvature functional retains its additional factor $1/(4g_r^2)$.

Thus the smooth extension and its ultraviolet energy cost are established together.

The exact product maps also produce a projective equal-time limit of the interacting vacuum marginals:
$$
\mathfrak Q=
\{(W_r)_{r\ge0}:\pi_{r,r+1}W_{r+1}=W_r\}.
$$
A single subsequence yields compatible probabilities $\nu_r$ and a probability $\nu$ on $\mathfrak Q$. The smooth holonomy image is dense, proved by the finite-level right inverses above. The same subsequence retains the positive-time correlations, with
$$
G^c_{ij}
=
\int\overline{O_i}O_j\,d\nu
-\overline{\int O_i\,d\nu}\int O_j\,d\nu,
\qquad
E_\infty=G^c-C(0+).
$$
The value of $E_\infty$, and support of $\nu$ in smooth connections, have not been established here.

## 4. The inverse-energy endpoint is retained exactly

The new infrared estimate permits
$$
d\alpha_n(\lambda)=\lambda^{-1}d\sigma_n(\lambda),
\qquad
\alpha_n([0,\infty])\preceq K_n.
$$
It also gives
$$
\alpha_n([\Lambda,\infty))
\preceq
\frac{96}{e^2\tau^2\Lambda}I_6.
$$
A joint subsequence therefore has a weak limit $\alpha$ with
$$
\alpha(\{\infty\})=0.
$$
Retain its zero-energy atom
$$
Z_\alpha=\alpha(\{0\}),
$$
and the limit
$$
S_\infty=\lim_n\bigl(K_n-M_n(0)\bigr)\succeq0.
$$
Then
$$
M_\infty(s)
=\int\frac{\lambda}{\lambda+s}\,d\alpha(\lambda),
$$
and direct evaluation of the two limit orders proves
$$
\boxed{F_\infty(0+)=S_\infty+Z_\alpha.}
$$

The associated typed observation map is
$$
\mathcal T:
\mathcal M([0,\infty))\to C^\infty((0,\infty)),
\qquad
(\mathcal T\alpha)(s)
=\int\frac{\lambda}{\lambda+s}\,d\alpha(\lambda).
$$
Its kernel is exactly
$$
\boxed{\ker\mathcal T=\mathbb C\delta_0.}
$$

For the converse inclusion, vanishing observations first give zero total mass on $(0,\infty)$, then a vanishing Stieltjes transform there. Differentiation at $s=1$ gives every moment $(1+\lambda)^{-k}$. The coordinate map
$$
x=(1+\lambda)^{-1},
\qquad
\lambda=x^{-1}-1
$$
transports these to polynomial moments; polynomial approximation forces the restricted measure to vanish.

The corresponding two-support complex uses the actual incoming map
$$
\mathbb C\to\mathcal M([0,\infty)),\qquad c\mapsto c\delta_0.
$$
Its retained boundary primitive is each original matrix entry $(Z_\alpha)_{ij}$.

## 5. A necessary correction: retain states whose labels move with refinement

The preceding spectral note asserted that a sequence of low-energy states approaching zero would be detected in at least one fixed-label diagonal continuum measure. I replaced that assertion with an explicit comparison map and computed its kernel. The earlier spectral-support and Laplace-principle formulas for the reconstructed sector remain. 

Let $\mathcal B_{\lim}$ consist of bounded regulator-state sequences $v=(v_n)$ whose pairings with every fixed positive-time observable vector converge. Define
$$
\langle z,\mathfrak b(v)\rangle
=
\lim_n\langle z_n,v_n\rangle.
$$
Cauchy-Schwarz proves that this defines
$$
\mathfrak b:\mathcal B_{\lim}\twoheadrightarrow\mathcal H_{\mathrm{obs}},
\qquad
\|\mathfrak b(v)\|\le\limsup_n\|v_n\|.
$$
The note proves surjectivity by a diagonal construction of finite-symbol lifts.

Let
$$
\mathcal N=\{v:\|v_n\|\to0\},\qquad
\mathcal K=\ker\mathfrak b.
$$
The cochain comparison
$$
\mathcal N\hookrightarrow\mathcal B_{\lim}\to0
\quad\longrightarrow\quad
\mathcal K\hookrightarrow\mathcal B_{\lim}\to0
$$
has the exact transported kernel
$$
\boxed{\mathcal K/\mathcal N.}
$$

An explicit commuting-observable test computes a nonzero class in this kernel. On
$$
\Omega_n=\{-1,1\}^n
$$
with product probability $2^{-n}$, let $F_j$ flip coordinate $j$, and set
$$
A_n^{\mathrm{test}}
=\sum_{j=1}^n\frac{c_{j,n}}2(I-F_j),
\qquad
c_{j,n}=1\ (j<n),\quad c_{n,n}=1/n.
$$
The Walsh functions
$$
\chi_S(\omega)=\prod_{j\in S}\omega_j
$$
satisfy
$$
A_n^{\mathrm{test}}\chi_S
=
\left(
|S\setminus\{n\}|+\frac{\mathbf1_{n\in S}}n
\right)\chi_S.
$$
Every fixed nonempty $S$ eventually has energy $|S|$, so the reconstructed centered fixed-label generator has spectral bottom one. Yet
$$
v_n=\chi_{\{n\}},
\qquad
\|v_n\|=1,
\qquad
\langle v_n,A_n^{\mathrm{test}}v_n\rangle=1/n,
\qquad
\mathfrak b(v)=0.
$$
Every fixed-label pairing is eventually zero. The sequence therefore gives an explicit nonzero element of $\mathcal K/\mathcal N$, with its norm and energy sequence retained.

This calculation corrects the inference through its exact morphism. It assigns no numerical value to the Yang-Mills gap.

## Verification and completed scope

The new checker passed **181 named exact integer, rational, and symbolic checks**. The existing Bernstein-reconstruction checker was recovered byte-for-byte and passed unchanged. The downloadable patch was applied to a fresh local tree and reproduced all six changed files exactly.

[Full verification log](sandbox:/mnt/data/yang_mills_vacuum_refinement_verification.json)

The analytic domain, measure, smooth-section, and limit arguments are written proofs in the note; the finite executable checks verify their declared algebraic test cases.

The completed advance is **uniform infrared memory control, interacting-vacuum refinement with every cross term, smooth holonomy extension with its full energy cost, and explicit cohomological records of both zero-energy limit-order effects and escaping regulator states**. A nontrivial four-dimensional continuum Yang-Mills field and a positive physical continuum mass lower bound have not been established by this contribution.
