**The Hamiltonian/self-adjointness connection is now recorded in the workbench, and I developed it into a concrete continuation of the Yang-Mills response calculation.** I opened **draft PR #6, “Coupled Hamiltonian response: retained cohomology and two-sided energy certificates,”** at commit `e98b2c3af77f66fb1c1396143ca53daef586404f`. It adds nine files on top of PR #5, preserving the earlier sources and receipts; nothing has been merged. 

[Full mathematical note](sandbox:/mnt/data/yang_mills_coupled_response_note.md) · [Proofs, checker, and execution records](sandbox:/mnt/data/yang_mills_coupled_response.zip) · [Git patch](sandbox:/mnt/data/yang_mills_coupled_response.patch)

The main advance is **an exact connection between the retained cohomology class and the error in the Hamiltonian response**. That supplies two-sided bounds for the effective energy and bounds for the restored state metric.

## 1. The coupling has an explicit self-adjoint realization

At a fixed original regulator, retain the conditional-expectation kernel
$$
\mathcal K=\ker\mathsf E,
$$
and its nonnegative self-adjoint energy operator $D$. For a finite independent family of centered smooth coarse observables $f_i$, retain
$$
G_{ij}=\langle f_i,f_j\rangle_m,
\qquad
(K_0)_{ij}=\kappa_n b\langle Xf_i,Xf_j\rangle_m,
$$
and the actual coupling
$$
Wx=\kappa_n b\,T^*X\!\left(\sum_i x_if_i\right).
$$
Here $m$ is the marginal of the interacting fine vacuum, and $T$ is the conditional density-derivative operator from the preceding calculation. These are the same physical quantities already used in PR #5. 

On $\mathbb C^m\oplus\mathcal K$, keep the pairing
$$
\langle(x,h),(y,k)\rangle_G=x^*Gy+\langle h,k\rangle_{\rho_n}.
$$
The coupled operator is
$$
\boxed{
\mathcal H_F
\begin{pmatrix}x\\h\end{pmatrix}
=
\begin{pmatrix}
G^{-1}(K_0x-W^*h)\\
Dh-Wx
\end{pmatrix},
\qquad
\operatorname{Dom}\mathcal H_F
=
\mathbb C^m\oplus\operatorname{Dom}D.
}
$$

Its diagonal operator is self-adjoint in this pairing. Its two off-diagonal terms are bounded and are each other’s adjoints in that same pairing. The note proves self-adjointness on the displayed domain by factoring the resolvents through the diagonal operator. The map back to the original physical functions is
$$
V(x,h)=\mathsf J\!\left(\sum_i x_if_i\right)+h,
$$
with
$$
q_F(u,v)=q_n(Vu,Vv).
$$
The energy coupling to the remaining coarse functions is also retained explicitly. 

For the complex spectral parameter, define
$$
M(z)=W^*(D-z)^{-1}W,\qquad
F(z)=K_0-zG-M(z),
$$
$$
L_zx=\bigl(x,(D-z)^{-1}Wx\bigr).
$$
The resolvent identity gives the complete two-parameter formula
$$
\boxed{
-\frac{F(z)-F(w)^*}{z-\overline w}
=
G+W^*(D-\overline w)^{-1}(D-z)^{-1}W
=
L_w^*L_z.
}
$$
In particular,
$$
\boxed{
-\frac{\operatorname{Im}F(z)}{\operatorname{Im}z}=L_z^*L_z,
\qquad
\operatorname{Im}F=\frac{F-F^*}{2i}.
}
$$

That is a reusable connection between **a coupled self-adjoint operator, its complex response, and the original state inner product**. The general elimination mechanism belongs to established Feshbach-Schur machinery; the contribution here spells out its domains, raw Gram factors, and retained conditional kernel for this workbench.  ([arXiv](https://arxiv.org/abs/2105.02058))

## 2. The unresolved response now carries an exact error certificate

This is the part most directly useful for continuing the mass-gap calculation.

For $s>0$, let
$$
M_s=W^*(D+s)^{-1}W.
$$
Take trial columns
$$
Y:\mathbb C^m\longrightarrow\operatorname{Dom}D
$$
and retain their residual
$$
R_Y=W-(D+s)Y.
$$
Define
$$
B_Y=W^*Y+Y^*W-Y^*(D+s)Y.
$$

Expanding the complete residual expression proves
$$
\boxed{
M_s=B_Y+R_Y^*(D+s)^{-1}R_Y.
}
$$
Since $D\ge0$,
$$
\boxed{
B_Y\preceq M_s
\preceq B_Y+\frac1sR_Y^*R_Y.
}
$$
Consequently, the effective energy matrix satisfies
$$
\boxed{
K_0+sG-B_Y-\frac1sR_Y^*R_Y
\preceq F_s
\preceq K_0+sG-B_Y.
}
$$

The restored-state error is controlled by the same original residual:
$$
\boxed{
\bigl((D+s)^{-1}W-Y\bigr)^*
\bigl((D+s)^{-1}W-Y\bigr)
=
R_Y^*(D+s)^{-2}R_Y
\preceq\frac1{s^2}R_Y^*R_Y.
}
$$
The note carries this through to bounds on the restored state metric, retaining its mixed terms. 

### Its Split Zero interpretation is literal

For nested finite trial spaces $V_j\subset\operatorname{Dom}D$, use the actual complexes
$$
V_j\xrightarrow{D+s}\mathcal K\xrightarrow0 0.
$$
Their cohomology is
$$
H_j^1=\mathcal K/(D+s)V_j.
$$
The transported-class kernel has the explicit isomorphism
$$
\boxed{
V_{j+1}/V_j
\longrightarrow
\ker(H_j^1\to H_{j+1}^1),
\qquad
[h]\longmapsto[(D+s)h].
}
$$
Its inverse sends the class represented by $(D+s)h$ to $[h]$. Changing that representative by $(D+s)V_j$ changes the inverse by precisely $V_j$.

With the original resolvent pairing
$$
\langle r,t\rangle_{\mathrm{dual},s}
=
\langle r,(D+s)^{-1}t\rangle,
$$
the canonical residual represents the unresolved forcing class, and its **full quotient Gram matrix is exactly**
$$
M_s-B_Y.
$$

Thus enlarging the admitted primitive space comes with a computable energy-error matrix. The support transition, killed class, primitive, and quantitative cost remain connected by their actual maps. 

## 3. The next physical inputs are now three specific matrices

The calculation reaches a finite-moment interface:
$$
\boxed{
N_0=W^*W,\qquad
N_1=W^*DW,\qquad
N_2=W^*D^2W.
}
$$

For the first trial space $\operatorname{ran}W$, the coefficient equation is
$$
(N_1+sN_0)X=N_0,\qquad Y=WX.
$$
The complete solution fiber is retained when the coefficient matrix is singular. Indeed,
$$
\ker(N_1+sN_0)=\ker W,
$$
because its quadratic form is
$$
\|D^{1/2}Wx\|^2+s\|Wx\|^2.
$$
Thus different coefficient solutions produce the same actual trial vector $Y$.

Higher trial spaces retain
$$
W,\ DW,\ldots,D^dW,
$$
and moments through order $2d+2$ determine the corresponding response and residual matrices. The shifted cross moments
$$
N_{i+1}+sN_i
$$
remain in the residual formula; the checker explicitly rejects replacing them by unshifted moments. 

**The actual Yang-Mills entries of $N_0,N_1,N_2$ have not been evaluated in this cycle.** They are now the recorded next calculation, with a precise route from their enclosures to the effective energy, restored norm, and original primitive norm.

## 4. The workflow and peer exchange were exercised

The new checker passed **189 exact checks and 12 deliberately false-formula controls**, with identical results in ordinary and optimized Python. A fresh copied-source replay reproduced the receipt, and the additive patch was applied to the delivered parent and reproduced it again. The unchanged parent checker also passed against its original receipt. The tests include raw-metric self-adjointness, an independently assembled block inverse, complex spectral parameters, singular moment fibers, and full residual Grams. These are declared finite fixtures; the analytical arguments remain written proofs for review. 

[Inspect the complete verification record](sandbox:/mnt/data/yang_mills_coupled_response_verification.json)

The source refresh also detected further Zeta exterior-conductor developments and a new Erdős-Straus higher-support/Green-norm continuation. Those were recorded at their actual reading scope. The mathematical import used here is the pinned Zeta finite-resolvent identity, instantiated by
$$
H\mapsto(\sigma-s)(D+\sigma)^{-1},
\qquad
T\mapsto(D+\sigma)^{-1},
\qquad
X\mapsto(D+s)^{-1}.
$$
The newer asymptotic and higher-support claims remain candidates for proof-body inspection. 

The active checkpoint is now `yang-mills/research-control/CURRENT.md`. It preserves your Hamiltonian/self-adjointness observation as a cross-project direction while keeping the next execution focused on the original Yang-Mills response matrices. **A positive continuum mass lower bound remains unestablished; this cycle supplies the coupled-operator and residual certificates needed to assess that next calculation quantitatively.**
