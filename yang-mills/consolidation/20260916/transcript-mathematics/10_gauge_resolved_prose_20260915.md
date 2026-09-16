**The revised argument gives a stronger physical gap on a substantially larger coupling range, and the same inverse now controls the entire spatial-volume limit-including the endpoint.**

The new bound, for every original open box $L\ge2$ and every $a>0$, is
$$
\boxed{
\Delta_L\ge
\frac{3g^2}{a}
\left(1+\sqrt{1-\frac{64}{3g^4}}\right),
\qquad
g^2\ge\frac8{\sqrt3}.
}
$$

This extends the previous domain $g^2\ge15$ to $g^2\ge8/\sqrt3$. The improvement comes from the original gauge constraints on the Fourier coefficients. It applies to the complete physical form domain.

[Physical-gap proof](sandbox:/mnt/data/yang_mills_gauge_resolved_gap.md) · [Spatial-volume and resolvent proof](sandbox:/mnt/data/yang_mills_gauge_volume_resolvent.md) · [Complete research package](sandbox:/mnt/data/yang_mills_gauge_resolved_gap.zip)

## 1. The decisive improvement is in the actual gauge projection

Keep the original operator and parameters:
$$
H_L=\kappa K_L+\kappa\xi\sum_p(2-W_p),
\qquad
\kappa=\frac{2g^2}{a},
\qquad
\xi=\frac1{4g^4},
$$
$$
K_L=-\sum_{e,\alpha}X_{e,\alpha}^2.
$$
Every original link, oriented plaquette word, and vertex gauge transformation-including boundary vertices-remains.

For a full Fourier representation label $\mathbf j=(j_e)_e$, its original electric eigenvalue is
$$
c(\mathbf j)=\sum_ej_e(j_e+1).
$$

A nonzero physical Fourier coefficient contains an invariant tensor at every vertex. At an edge $e$ incident on $v$, this forces
$$
j_e\le\sum_{\substack{f\ni v\\f\ne e}}j_f.
$$
The reason is explicit: the invariant tensor gives an intertwiner from the dual spin-$j_e$ representation into the tensor product of the other incident representations, whose maximum weight is their summed spin.

Now fix $e=\{v,w\}$. Let $A_e$ be the other edges incident on $v$ or $w$. The two endpoint inequalities give
$$
\sum_{f\in A_e}j_f\ge2j_e.
$$
The original cubic graph has no triangles. The remote endpoints of those edges are consequently distinct. Applying the same invariant-tensor inequality at those endpoints gives
$$
\sum_{f\notin A_e\cup\{e\}}j_f
\ge\frac12\sum_{f\in A_e}j_f.
$$
The factor $1/2$ retains the fact that an exterior edge can be counted at most twice.

Therefore
$$
\sum_fj_f\ge4j_e.
$$
Since $j(j+1)\ge3j/2$ for the original half-integer spins,
$$
\boxed{
c(\mathbf j)\ge6j_e,
\qquad
\frac{j_e}{c(\mathbf j)}\le\frac16.
}
$$

Every nontrivial physical coefficient thus has $c(\mathbf j)\ge3$, attained by the original four-edge plaquette with spin $1/2$ on each edge.

That inequality improves both the actual vacuum series and the operator acting on the excitation source. The proof and checker retain an active-bridge example; they also retain the triangle and unprojected single-link examples that prevent extending the bound beyond its stated graph and gauge domains.

## 2. The endpoint vacuum series and the physical inverse are now controlled separately

Write the actual positive vacuum as
$$
\psi_L=e^{v_L+c_L},
\qquad
c_L=-\frac12\log\int e^{2v_L}\,dU.
$$
The scalar energy is retained through
$$
E_{0,L}
=
2\kappa\xi|\mathsf P_L|
-\kappa\int\sum_i(X_iv_L)^2\,dU.
$$

On the same support-labelled Fourier coefficients used in the preceding calculation, the new gauge inequality improves the quadratic estimate to
$$
\|\mathcal B(f,h)\|_0
\le\frac23\|f\|_0\|h\|_0.
$$
The original plaquette coefficient has trace norm $8$, so the actual first source is bounded by $32\xi$.

Set
$$
\theta=\frac{256}{3}\xi,
\qquad
r=\frac34\left(1-\sqrt{1-\theta}\right).
$$
The complete vacuum series converges for
$$
0<\xi\le\frac3{256},
$$
including the closed endpoint. At that endpoint, its exact omitted-order bound is
$$
\boxed{
\sum_{p>P}n_p
=
\frac34\,\frac{\binom{2P}{P}}{4^P}
\le\frac{3}{4\sqrt{P+1}}.
}
$$

The nonlinear difference estimate reaches one there. I have kept that value. Convergence at the endpoint is proved by this explicit summable Catalan series.

For the excitation operator, put
$$
u_L=\log\psi_L,
\qquad
\mathcal A_L
=\psi_L^{-1}(H_L-E_{0,L})\psi_L
=\kappa(K_L-\mathscr D_u),
$$
$$
\mathscr D_uf
=
2\sum_{e,\alpha}(X_{e,\alpha}u_L)X_{e,\alpha}f.
$$
The gauge-resolved coefficient bound gives
$$
\boxed{
\|\mathscr D_uh\|_{\mathcal A}
\le\chi\|K_Lh\|_{\mathcal A},
\qquad
\chi=\frac{2r}{3}
=\frac{1-\sqrt{1-\theta}}2
\le\frac12.
}
$$
Here $\|\cdot\|_{\mathcal A}$ is the explicitly specified trace-coefficient norm. The physical state pairing remains $\int\rho_L\overline f h\,dU$.

For an actual positive-energy physical eigenfunction, subtract its Haar scalar to obtain $h$. Its original eigen-equation becomes
$$
(K_L-\epsilon)h=Q_H\mathscr D_uh,
\qquad \epsilon=\lambda/\kappa.
$$
On the physical Fourier coefficients, for $0<\epsilon<3$,
$$
\|(K_L-\epsilon)h\|_{\mathcal A}
\ge
\left(1-\frac{\epsilon}{3}\right)
\|K_Lh\|_{\mathcal A}.
$$
Consequently $\epsilon\ge3(1-\chi)$. The complete physical spectral resolution returns this estimate to the original form domain:
$$
\boxed{
q_{\mathcal A_L}(f)
\ge
\kappa d_{\mathrm p}\operatorname{Var}_{\rho_L}(f),
\qquad
d_{\mathrm p}
=
\frac32\left(1+\sqrt{1-\theta}\right).
}
$$

The scalar-space constant is separately
$$
d_{\mathrm s}=\frac{d_{\mathrm p}}4.
$$

At the endpoint, the physical lower bound is $3\kappa/2$. A convenient interior consequence is
$$
\boxed{
\Delta_L\ge2\kappa=\frac{4g^2}{a},
\qquad g^2\ge5.
}
$$

## 3. Split Zero now carries a bounded inverse back to the original physical source

On the zero-Haar-mean coefficient space, define
$$
T=Q_H\mathscr D_uK_L^{-1},
\qquad
p=P_H\mathscr D_uK_L^{-1}.
$$
The complete bound includes the scalar output:
$$
|py|+\|Ty\|_{\mathcal A}
\le\chi\|y\|_{\mathcal A}.
$$
Thus
$$
S=(I-T)^{-1}=\sum_{m\ge0}T^m
$$
exists on the closed coupling domain.

For an original smooth physical observable $F$, put $q=Q_HF$. The inverse gives both the primitive and the actual vacuum expectation:
$$
\boxed{
h_F=K_L^{-1}Sq,
\qquad
\langle F\rangle_{\rho_L}
=
P_HF+pSq.
}
$$
Indeed,
$$
\mathcal A_Lh_F
=
\kappa\bigl(F-P_HF-pSq\bigr),
$$
and integration in the actual vacuum proves the scalar-return identity. The physical inverse is therefore
$$
\boxed{
\mathcal A_L^{-1}
\bigl(F-\langle F\rangle_{\rho_L}\bigr)
=
\kappa^{-1}
\bigl(h_F-\langle h_F\rangle_{\rho_L}\bigr).
}
$$

The proof checks its original operator-domain membership through coefficient convergence and the actual elliptic equation.

For the finite admitted source
$$
V_N=\operatorname{span}\{q,Tq,\ldots,T^Nq\},
$$
use the actual complexes
$$
V_N\xrightarrow{I-T}\mathcal A_0\xrightarrow0 0.
$$
The primitive
$$
y_N=\sum_{m=0}^NT^mq
$$
has the exact retained residual
$$
q-(I-T)y_N=T^{N+1}q.
$$
The transported-class kernel is computed by
$$
V_{N+1}/V_N
\longrightarrow
\ker\!\left(
\mathcal A_0/(I-T)V_N
\to
\mathcal A_0/(I-T)V_{N+1}
\right),
\quad
[v]\longmapsto[(I-T)v],
$$
with inverse supplied by $S$.

Its chain map to the physical equation retains $\kappa$:
$$
J_0y
=
\kappa^{-1}
\left(K_L^{-1}y-\langle K_L^{-1}y\rangle_{\rho_L}\right),
\qquad
J_1z=z-\langle z\rangle_{\rho_L},
$$
$$
\boxed{\mathcal A_LJ_0=J_1(I-T).}
$$

The resulting state error is
$$
\boxed{
\left\|
\mathcal A_L^{-1}(F-\langle F\rangle_{\rho_L})-J_0y_N
\right\|_{\rho_L}
\le
\frac{\chi^{N+1}\|Q_HF\|_{\mathcal A}}{\kappa d_{\mathrm p}}.
}
$$
The corresponding energy-error bound has denominator $\sqrt{\kappa d_{\mathrm p}}$.

This is a quantitative primitive on the original physical source, with its support transitions, scalar return, and residual retained.

## 4. The spatial-volume construction now reaches the same closed endpoint

Every support-labelled vacuum coefficient is exactly identical in every box containing its original support. The summable coefficient bounds therefore give an infinite local drift and strong convergence of the source operators $T_L,p_L$.

The scalar-return formula above proves convergence of the **entire** sequence of actual vacuum measures:
$$
\nu_L\longrightarrow\nu.
$$
Positivity and unit mass pass from the actual finite vacua. The construction makes no assumption of an infinite density relative to product Haar measure.

The positive-shift inverse also retains its scalar term. With
$$
\sigma=s/\kappa,\quad
k_\sigma=(K+\sigma)^{-1},
$$
$$
T_\sigma=Q_H\mathscr D_uk_\sigma,
\quad
p_\sigma=P_H\mathscr D_uk_\sigma,
\quad
X_\sigma=(I-T_\sigma)^{-1}Q_HF,
$$
the exact returned resolvent is
$$
\boxed{
R_sF
=
\kappa^{-1}k_\sigma X_\sigma
+
\frac{P_HF+p_\sigma X_\sigma}{s}\,1.
}
$$

This provides full-sequence convergence of the original dynamics at the endpoint as well. For the finite ground-relative semigroup $T_L(t)$, the proof derives the uniform approximation
$$
\boxed{
\left\|
T_L(t)F-
\left[\frac mtR_{m/t}^{\,L}\right]^mF
\right\|_\infty
\le
\frac{t\,\kappa(1+\chi)\|KF\|_{\mathcal A}}{\sqrt m}.
}
$$
It comes from the exact mean and variance of the original exponential-time resolvent averages. Convergence of the resolvents then determines the limiting semigroup.

The completed argument establishes the original cylinder core, the unique stationary and conditional vacuum measure, and the full physical Hilbert-space realization. Its generator satisfies
$$
\boxed{
A_\infty\big|_{1^\perp}\ge\kappa d_{\mathrm p}
}
$$
at fixed $a>0$. All bounded local time-ordered vacuum correlations converge through the original ground-state transform.

### Explicit control of the omitted spatial supports

For $\theta<1$, let $R$ be the distance from an observable’s original link support to the exterior of the box, measured in the original edge adjacency graph. Then
$$
\boxed{
|\nu_L(F)-\nu(F)|
\le
\theta^{R/3}\|Q_HF\|_{\mathcal A}.
}
$$
For the original plaquette at $g^2=5$, this gives
$$
R\ge192:
\quad
|\nu_L(W_p)-\nu(W_p)|
\le8(64/75)^{64}<0.000313.
$$

At the closed endpoint, the separate source and inverse truncations give
$$
\boxed{
|\nu_L(F)-\nu(F)|
\le
\left[
4\frac{\binom{2P}{P}}{4^P}+2^{1-M}
\right]\|Q_HF\|_{\mathcal A}
}
$$
once the box contains the radius-$3PM$ neighbourhood of the original support. Both terms tend to zero under the displayed truncations.

The limiting physical space is quantitatively nonzero. For the original elementary plaquette $F$,
$$
\operatorname{Var}_\nu(F)\ge e^{-16r/3}\ge e^{-4},
\qquad
q_\infty(F-\nu F)\le4\kappa.
$$
Its correlation therefore obeys
$$
\boxed{
e^{-16r/3}-4\kappa t
\le C_F(t)
\le C_F(0)e^{-\kappa d_{\mathrm p}t}.
}
$$

## 5. Return to the actual zero-shift response

The conditional kernel retains its scalar bound. Its gauge-invariant part is a reducing subspace, with the explicit inclusion $I$ satisfying
$$
DI=ID_{\mathrm{phys}},
\qquad
D^{-1}I=ID_{\mathrm{phys}}^{-1},
\qquad
D_{\mathrm{phys}}\ge\kappa d_{\mathrm p}.
$$
The original loop forcing, trial, and residual belong to this physical part.

Using that map, the unchanged local calculations at
$$
\xi=10^{-8},\qquad g^2=5000,\qquad\kappa=10000/a
$$
now give
$$
\boxed{
\left|
\langle W,D^{-1}W\rangle_{\rho_L}
-\frac8{39}\kappa\xi^2
\right|
<
0.00000931\,\kappa\xi^2,
}
$$
$$
\boxed{
\left|
\|D^{-1}W\|_{\rho_L}^2
-\frac{196}{4563}\xi^2
\right|
<
0.00000184\,\xi^2.
}
$$
The complete canonical cohomology-class error plus the retained minimum-section correction is less than
$$
0.00000000000355\,\kappa\xi^2.
$$

Combining the new full-domain lower estimate with the preceding explicit physical trial gives
$$
\boxed{
2.99999935999\,\kappa
\le\Delta_L
<
\left(3+\frac5{10^{13}}\right)\kappa
}
$$
at that coupling, uniformly in the exterior box.

## Scope, verification, and workbench delivery

The original simultaneous path remains
$$
a_n=a_02^{-n},
\qquad
g_n^2=\frac1{c_n},
\qquad
c_n=g_0^{-2}+\beta n\log2.
$$
The enlarged proved domain is exactly
$$
\boxed{c_n\le\frac{\sqrt3}{8}.}
$$
For $\beta>0$, the path eventually leaves that domain.

Every path that stays in the proved domain while $a_n\to0$ obeys
$$
\Delta_n\ge\frac{8\sqrt3}{a_n}\longrightarrow\infty.
$$
The original plaquette retains a positive zero-time norm while its bounded positive-time correlations vanish. The proof follows that norm to the energy-infinity atom of the compactified spectral measure. **A nontrivial four-dimensional ultraviolet field and a finite positive continuum mass remain unestablished.**

The new verifier completed **360 named exact checks and 17 false-formula controls**. The replay includes ordinary and optimized execution, the unchanged predecessor, fresh copied sources, and **16 named command-line corruption rejections**. Both patches were applied to fresh selected source trees and their verification outputs reproduced.

[Verification record](sandbox:/mnt/data/yang_mills_gauge_verification.json) · [Execution record](sandbox:/mnt/data/yang_mills_gauge_execution.json) · [Patch-validation record](sandbox:/mnt/data/yang_mills_gauge_patch_validation.json)

These executable checks cover the finite representation identities, original graph constraints, scalar-return equations, and rational bounds. The analytical arguments are complete written proofs supplied for review; independent external review and Lean verification have not been performed.

[Combined patch against PR6](sandbox:/mnt/data/yang_mills_gauge_resolved_gap.patch) · [Incremental patch after the previous delivery](sandbox:/mnt/data/yang_mills_gauge_resolved_incremental.patch)

The active checkpoint now records the enlarged domain, the full physical inverse, and the coupling-response calculation at its endpoint. No new remote PR or merge was performed; the available GitHub actions remain read-only.
