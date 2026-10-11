# Conditional edge-path entropy and an unconditional square-root vacuum score

11 October 2026. This calculation concerns the same full finite-volume Hamiltonian and its actual positive unit vacuum. The entropy estimate below is for the tilted edge path **conditional on every outside Brownian path**. It does not assert the corresponding bound for the entropy of the entire tilted path law; that entropy contains an additional outside-marginal term.

The exact path transformation proves the proposed derivative inequality with the actual edge oscillation. It also closes that inequality without any additional oscillation theorem, giving an unconditional square-root edge score. All outside paths, the terminal vacuum factor, the original radius-two metric, and the complete potential are retained. The final section applies the result to the original raw phase quotient without changing its path or vector.

The retained original score source is [Spatial continuum, equations (77)–(79)](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/sources/spatial/spatial_continuum.tex#L1415). The full inverse and vacuum are [GPR1–GPR10](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/442786391ab942ad0c829c0ebf32e952585915e0/yang-mills/continuations/20261011-central-signs-shrinking-window/GLOBAL_PHYSICAL_RESPONSE.md). The receiving raw phase estimate is [PRE32–PRE52](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_RESPONSE_AND_ENDPOINT.md). These are programme sources. The existing machine-readable literature indexes were consulted; routing hits are not claimed as read papers. The Gaussian change of measure and entropy estimate actually needed here are proved directly below.

## 1. Original operator, metric, and exact vacuum martingale

Retain the open cubic box \(L\ge2\), \(m=2L\), \(n=m+1\), with original physical vertices \(o+a(i-L,k-L,l-L)\), \(0\le i,k,l\le m\). Its positive edges and faces have counts \(N=3m(m+1)^2\), \(M=3m^2(m+1)\). The link manifold is \(Q_L=SU(2)^{E_L}\) with product Haar probability. At every vertex, including the boundary, impose the original gauge action \(U_{(s,t)}\mapsto q_sU_{(s,t)}q_t^{-1}\). Put
\[
 \begin{gathered}
 T_\alpha=-i\sigma_\alpha/2,\quad
 \langle v,w\rangle_{\mathfrak{su}(2)}=-2\operatorname{tr}(vw),\quad
 v=\sum_{\alpha=1}^3v_\alpha T_\alpha,\quad |v|^2=\sum_\alpha v_\alpha^2,\\
 X_{e,\alpha}f(U)=
  \left.\frac d{dh}f(\ldots,e^{hT_\alpha}U_e,\ldots)\right|_{h=0},
 \quad K=-\sum_{e,\alpha}X_{e,\alpha}^2,\quad
 \Delta=-K .
 \end{gathered}\tag{ESE1}
\]
These three fields are orthonormal for the radius-two sphere metric, whose diameter is \(2\pi\). The complete face word, trace, potential and Hamiltonian are
\[
 \begin{gathered}
 W_{(z;i,j)}
 =\operatorname{tr}\!\left[
 U_i(z)U_j(z+e_i)U_i(z+e_j)^{-1}U_j(z)^{-1}\right],\\
 \kappa=\frac{2g^2}{a}>0,\quad b_{\rm mag}=\frac1{2g^2a},\quad
 \xi=\frac{b_{\rm mag}}{\kappa}=\frac1{4g^4},\quad
 V(U)=\kappa\xi\sum_{p}(2-W_p(U)),\quad H=\kappa K+V,\\
 H\psi=E_0\psi,\qquad \psi>0,\quad\int_{Q_L}\psi^2dU=1,\quad
 \rho=\psi^2,\quad u=\log\psi.
 \end{gathered}\tag{ESE2}
\]
The normalized positive vacuum is unique, smooth, and physical, by positivity of the heat kernel and elliptic regularity on the compact connected link manifold. Every scalar \(2\kappa\xi M\), \(E_0\), and the unit normalization remains part of (ESE2).

Fix an original edge \(e\). Its actual number of incident faces is \(r_e\in\{2,3,4\}\), including boundary incidences, and write
\[
 \beta=r_e\xi,\qquad
 V=V_e+V_{\bar e},\quad
 V_e=\kappa\xi\sum_{p:e\in\partial p}(2-W_p),\quad
 V_{\bar e}=\kappa\xi\sum_{p:e\notin\partial p}(2-W_p).
 \tag{ESE3}
\]
Here \(V_{\bar e}\) is independent of \(U_e\); \(V_e\) retains all outside links in its incident face words. In particular
\[
 0\le V_e\le4\kappa\beta,\qquad
 |\nabla_eV|=|\nabla_eV_e|\le\kappa\beta.
 \tag{ESE4}
\]
For the gradient constant, write an incident face as \(A U_e B\) or \(A U_e^{-1}B\). Bi-invariance and inversion reduce its trace gradient to that of \(2c(U)\), where \(c(U)=\operatorname{tr}U/2\); its squared norm on the radius-two sphere is \(1-c(U)^2\le1\). Summing every incident face proves (ESE4).

For each original edge let \(B^f=(B^{f,1},B^{f,2},B^{f,3})\) be independent standard Euclidean Brownian motions. Brownian motion on \(Q_L\) with generator \(\kappa\Delta\), starting from the arbitrary full configuration \(x\), satisfies the matrix equations
\[
 \begin{split}
 dX_s^f&=\sqrt{2\kappa}\sum_\alpha T_\alpha X_s^f\circ dB_s^{f,\alpha},\\
 dX_s^f&=\sqrt{2\kappa}\sum_\alpha T_\alpha X_s^f\,dB_s^{f,\alpha}
                     -\frac{3\kappa}{4}X_s^f\,ds,\qquad X_0^f=x_f.
 \end{split}\tag{ESE5}
\]
The second line follows from \(\sum_\alpha T_\alpha^2=-3I/4\); it is the exact Itô correction in the original metric. The matrix equation has a unique global strong solution: its real matrix coefficients are linear and therefore globally Lipschitz, while the Stratonovich product rule preserves \(X^*X=I\) and determinant one. Thus it remains in \(SU(2)\), and its generator on smooth functions is \(\kappa\sum_\alpha X_{f,\alpha}^2\).

The full vacuum equation gives the exact positive martingale and normalization
\[
 Z_s^{\rm vac}
  =\frac{e^{E_0s-\int_0^s V(X_r)\,dr}\psi(X_s)}{\psi(x)},
 \qquad \mathbb E_x Z_t^{\rm vac}=1,\qquad
 d\mathbb Q_x=Z_t^{\rm vac}\,d\mathbb P_x .
 \tag{ESE6}
\]
Indeed Itô differentiation of \(\psi(X_s)\) gives drift
\(\kappa\Delta\psi=(V-E_0)\psi\), cancelling the displayed exponential drift. The stochastic integrand is bounded on every finite time interval, since the configuration space is compact and \(V,\psi,\nabla\psi\) are bounded there. Hence the local martingale is a true martingale, with initial value one. Equation (ESE6) proves exactly the Feynman–Kac identity needed below, including its terminal factor and energy scalar.

## 2. The complete endpoint-preserving path transformation

Fix a finite time \(t>0\), a unit \(v\in\mathfrak{su}(2)\), and a real parameter \(\epsilon\). Keep every outside Brownian motion and every outside link path unchanged. For the selected edge put
\[
 a_s=1-\frac{s}{t},\quad
 g_s^\epsilon=\exp(\epsilon a_s v),\quad
 Y_s^{e,\epsilon}=g_s^\epsilon X_s^e,\quad
 Y_s^{f,\epsilon}=X_s^f\ (f\ne e).
 \tag{ESE7}
\]
Thus \(Y_0^{e,\epsilon}=e^{\epsilon v}x_e\) and
\(Y_t^{e,\epsilon}=X_t^e\) exactly. This is a transformation of the whole original edge path with a fixed terminal point, not conditioning on a Brownian bridge.

Write the deterministic adjoint matrix in the original orthonormal Lie basis as
\[
 g_s^\epsilon T_\alpha(g_s^\epsilon)^{-1}
       =\sum_\gamma R_s^\epsilon{}_{\gamma\alpha}T_\gamma,\qquad
 R_s^\epsilon\in SO(3),\quad
 R_s^\epsilon v=v,\quad (R_s^\epsilon)^{\mathsf T}v=v.
 \tag{ESE8}
\]
Conjugation preserves \(-2\operatorname{tr}(vw)\), proving orthogonality; continuity from the identity gives determinant one. Since \(g_s^\epsilon\) is an exponential of \(v\), it fixes \(v\). Define the rotated noise
\[
 B_s^{e,\epsilon}=\int_0^sR_r^\epsilon\,dB_r^e.
 \tag{ESE9}
\]
This is a standard three-dimensional Brownian motion, independent of all outside Brownian motions. To verify the law directly, deterministic stochastic integrals against Brownian motion are Gaussian; for disjoint time intervals their underlying increments are independent, their mean is zero, and
\[
 d\langle B^{e,\epsilon,\alpha},B^{e,\epsilon,\gamma}\rangle_s
       =\delta_{\alpha\gamma}\,ds,\quad
 d\langle B^{e,\epsilon,\alpha},B^{f,\gamma}\rangle_s=0\ (f\ne e),
 \qquad v\cdot B_s^{e,\epsilon}=v\cdot B_s^e .
 \tag{ESE10}
\]
The final equality follows by \(v^{\mathsf T}R_r^\epsilon=v^{\mathsf T}\) inside the integral. In particular no dimension factor multiplies the variance of this unit directional noise.
The inverse deterministic stochastic integral is \(B_s^e=\int_0^s(R_r^\epsilon)^{\mathsf T}dB_r^{e,\epsilon}\), so the two noises generate the same completed filtration. This also makes the subsequent change-of-measure statement a Brownian statement in the full filtration used by the original matrix equation.

The deterministic derivative is
\((g_s^\epsilon)'(g_s^\epsilon)^{-1}=-\epsilon v/t\).
Applying Itô's product rule to (ESE5), with this deterministic matrix, therefore gives
\[
 dY_s^{e,\epsilon}
 =\sqrt{2\kappa}\sum_\alpha T_\alpha Y_s^{e,\epsilon}
                                  \,dB_s^{e,\epsilon,\alpha}
   -\frac{3\kappa}{4}Y_s^{e,\epsilon}\,ds
   -\frac{\epsilon}{t}vY_s^{e,\epsilon}\,ds.
 \tag{ESE11}
\]
There is no extra derivative of \(R_s^\epsilon\) in this equation: (ESE9) is a deterministic orthogonal rotation inside a stochastic integral, and (ESE11) already includes the entire derivative of \(g_s^\epsilon\). This records the adjoint rotation, curvature correction and drift sign separately.

The exact likelihood which removes the final drift is
\[
 \begin{split}
 \Lambda_s^\epsilon
 &=\exp\left[
   \frac{\epsilon}{\sqrt{2\kappa}\,t}\,v\cdot B_s^{e,\epsilon}
                      -\frac{\epsilon^2s}{4\kappa t^2}\right],\\
 \Lambda_t^\epsilon
 &=\exp\left[
   \frac{\epsilon}{\sqrt{2\kappa}\,t}\,v\cdot B_t^e
                      -\frac{\epsilon^2}{4\kappa t}\right],\qquad
 d\mathbb P_\epsilon=\Lambda_t^\epsilon\,d\mathbb P_x .
 \end{split}\tag{ESE12}
\]
The stochastic exponent has quadratic variation
\(\epsilon^2s/(2\kappa t^2)\), so its compensator is exactly the negative half shown above. The exponential has expectation one.

Here the required change of measure can be proved by finite-dimensional Gaussian integration. For a partition of \([0,t]\), the increments of \(B^{e,\epsilon}\) are independent centered Gaussians with covariance \(\Delta s\,I_3\). Multiplication of their joint density by
\(\exp[\theta v\cdot\sum\Delta B-\theta^2t/2]\), with
\(\theta=\epsilon/(\sqrt{2\kappa}\,t)\), completes the square in each increment and shifts its mean to \(\theta v\Delta s\), keeping its covariance and independence unchanged. Cylinder sets on all finite partitions generate the continuous-path sigma field. Consequently under \(\mathbb P_\epsilon\)
\[
 \widetilde B_s^{e,\epsilon}
       =B_s^{e,\epsilon}
                    -\frac{\epsilon s}{\sqrt{2\kappa}\,t}v
 \tag{ESE13}
\]
is standard Brownian motion, independent of the unchanged outside Brownian motions. The latter assertion also follows directly because (ESE12) depends only on the selected edge noise, whose original law is independent of the outside noises.

Substituting (ESE13) into (ESE11) adds
\(+(\epsilon/t)vY_s^{e,\epsilon}ds\), cancelling the negative drift exactly. Strong uniqueness of (ESE5) then shows that the full path \(Y^\epsilon\), under \(\mathbb P_\epsilon\), has exactly the original full Brownian law starting at
\(x^\epsilon=(x_f)_{f\ne e},e^{\epsilon v}x_e\).
This proves the required Cameron–Martin/Girsanov formula with its sign and all metric constants; no bounded-drift estimate or suppressed noise rotation substitutes for the exact law.

## 3. Differentiation with every outside path and terminal factor

Apply (ESE6) at \(x^\epsilon\), then use the just-proved change of law. Terminal preservation in (ESE7) gives
\[
 \begin{split}
 \psi(x^\epsilon)
 &=e^{E_0t}\,
   \mathbb E_x\!\left[
     \Lambda_t^\epsilon
       e^{-\int_0^t V(Y_s^\epsilon)\,ds}\psi(X_t)\right],\\
 \frac{\psi(x^\epsilon)}{\psi(x)}
 &=\mathbb E_{\mathbb Q_x}\!\left[
     \Lambda_t^\epsilon
       e^{-\int_0^t[V(Y_s^\epsilon)-V(X_s)]\,ds}\right].
 \end{split}\tag{ESE14}
\]
The original terminal factor \(\psi(X_t)\) appears explicitly in the first line and in the full tilted law of the second. Every outside path is present in \(V(X_s)\), \(V(Y_s^\epsilon)\), and \(\psi(X_t)\). The constant potential \(2\kappa\xi M\) remains in the first line; it cancels in the potential difference of the second because the same full potential is used at both paths. The vacuum energy \(E_0\) cancels only through the exact normalization (ESE6).

The derivative at \(\epsilon=0\) can be passed through the expectation. Indeed (ESE4) bounds the potential difference by
\(\kappa\beta|\epsilon|\int_0^t a_sds=\kappa\beta|\epsilon|t/2\).
Its derivative is bounded by the same constant. The likelihood and its derivative, for \(|\epsilon|\le\epsilon_0\), are bounded by a constant times
\((1+|v\cdot B_t^e|)
\exp[\epsilon_0|v\cdot B_t^e|/(\sqrt{2\kappa}\,t)]\).
This is integrable under the original Gaussian law. The tilt \(Z_t^{\rm vac}\) is bounded above and below by finite positive constants at this fixed box, configuration, and time, because the vacuum and potential are smooth on the compact manifold. The same dominating function is therefore integrable under \(\mathbb Q_x\).

Differentiating (ESE14) now proves the exact directional formula
\[
 \boxed{\displaystyle
 X_{e,v}\log\psi(x)=
 \mathbb E_{\mathbb Q_x}\!\left[
  \frac{v\cdot B_t^e}{\sqrt{2\kappa}\,t}
  -\int_0^t\left(1-\frac{s}{t}\right)
                         X_{e,v}V(X_s)\,ds\right].}
 \tag{ESE15}
\]
Here \(X_{e,v}=\sum_\alpha v_\alpha X_{e,\alpha}\). The potential derivative includes every incident face with its actual inverse orientations; the estimate (ESE4) merely bounds their complete sum. There is no terminal derivative because \(Y_t^\epsilon=X_t\) holds for every \(\epsilon\), before differentiation.

## 4. Conditional entropy and the exact outside mixture

Let \(\mathbb P_e\) be the driving Brownian law of the selected edge and \(\mathbb P_{\bar e}\) the joint law of all outside link paths, starting at the fixed original outside configuration. The original law factors as \(\mathbb P_e\otimes\mathbb P_{\bar e}\). For an outside path \(y=(y_s)_{0\le s\le t}\), keep
\[
 \begin{split}
 R_y(B^e)
   &=\exp\left[-\int_0^t
                  V_e(X_s^e,y_s)\,ds\right]\psi(X_t^e,y_t),\\
 Z_y&=\mathbb E_{\mathbb P_e}R_y>0,\qquad
 q_y=\frac{R_y}{Z_y},\qquad
 d\mathbb Q_e^y=q_y\,d\mathbb P_e.
 \end{split}\tag{ESE16}
\]
All expressions are measurable; Brownian path spaces are standard Borel, and these explicit positive densities give their conditional laws. Compactness bounds \(R_y\) above and below uniformly by positive finite constants at fixed \(t\). In particular every normalization and conditional expectation here is well-defined.

The actual tilted outside law is
\[
 d\mathbb Q_{\bar e}(y)
 =\frac{e^{E_0t}}{\psi(x)}
   \exp\left[-\int_0^tV_{\bar e}(y_s)\,ds\right]
        Z_y\,d\mathbb P_{\bar e}(y),
 \qquad
 d\mathbb Q_x=q_y\,d\mathbb P_e\,d\mathbb Q_{\bar e}(y).
 \tag{ESE17}
\]
The normalization of the first line follows from (ESE6) and Fubini. Equation (ESE17) retains the terminal vacuum through \(Z_y\) and retains all nonincident potentials through \(V_{\bar e}\). It is not the original outside Brownian marginal in general.

Define the actual edge oscillation and maximal score by
\[
 \omega_e=\max_{z\in SU(2)^{E_L\setminus\{e\}}}
       \left[\max_{U_e}\log\psi(U_e,z)
                         -\min_{U_e}\log\psi(U_e,z)\right],
 \quad
 M_e=\max_{x\in Q_L}|\nabla_e\log\psi(x)|.
 \tag{ESE18}
\]
These are finite actual-vacuum numbers, since \(\psi\) is smooth and positive on the compact product. No estimated oscillation is substituted in their definition.

For every fixed outside path \(y\), (ESE4) and the terminal slice of (ESE18) give
\[
 \operatorname{osc}_{B^e}\log R_y
     \le\omega_e+4\kappa\beta t=:D_t,\qquad
 \operatorname{Ent}(\mathbb Q_e^y\mid\mathbb P_e)
       =\mathbb E_{\mathbb P_e}(q_y\log q_y)\le D_t.
 \tag{ESE19}
\]
The first inequality keeps the potential and terminal terms separately: the integral of \(V_e\) ranges within an interval of length \(4\kappa\beta t\), and the logarithm of \(\psi(X_t^e,y_t)\) ranges within an interval of length at most \(\omega_e\). For the second, \(Z_y\) lies between the minimum and maximum of \(R_y\), so \(q_y\le e^{D_t}\). Integrating \(\log q_y\le D_t\) against its probability density proves the bound. Nonnegativity of entropy follows from \(q\log q-q+1\ge0\), integrated against \(\mathbb P_e\).

The full entropy, by contrast, has the exact chain rule
\[
 \operatorname{Ent}(\mathbb Q_x\mid\mathbb P_e\otimes\mathbb P_{\bar e})
 =\operatorname{Ent}(\mathbb Q_{\bar e}\mid\mathbb P_{\bar e})
    +\int\operatorname{Ent}(\mathbb Q_e^y\mid\mathbb P_e)
                                  \,d\mathbb Q_{\bar e}(y).
 \tag{ESE20}
\]
To prove it, take the logarithm of the product density in (ESE17) and integrate first in the edge variable. All logarithms are bounded at fixed \(t\), so Fubini applies directly. The outside term in (ESE20) is retained. No bound by \(D_t\) for the full entropy is used or follows from (ESE19) alone.

Under the original conditional law \(\mathbb P_e\), the scalar \(Z=v\cdot B_t^e\) is Gaussian with mean zero and variance \(t\), for every unit \(v\). For any probability density \(q\) of finite entropy \(I\), Jensen's inequality gives
\[
 \lambda\,\mathbb E_qZ-I
  =\mathbb E_q\log\frac{e^{\lambda Z}}q
  \le\log\mathbb E_{\mathbb P_e}e^{\lambda Z}
  =\frac{\lambda^2t}{2},\qquad
 |\mathbb E_qZ|\le\sqrt{2tI}.
 \tag{ESE21}
\]
The final inequality follows by minimizing \(I/|\lambda|+|\lambda|t/2\) and choosing the sign of \(\lambda\); if \(I=0\), take \(\lambda\to0\). The Gaussian moment generating function follows by completing the square. These steps apply to \(q_y\), which is bounded and strictly positive.

Apply (ESE21) to each entire conditional density (ESE16), then integrate using the actual outside law (ESE17). Equations (ESE19) and (ESE21) imply
\[
 \left|\mathbb E_{\mathbb Q_x}
       \frac{v\cdot B_t^e}{\sqrt{2\kappa}\,t}\right|
 \le\int\sqrt{\frac{\operatorname{Ent}(\mathbb Q_e^y\mid\mathbb P_e)}
                         {\kappa t}}\,d\mathbb Q_{\bar e}(y)
 \le\sqrt{\frac{\omega_e}{\kappa t}+4\beta}.
 \tag{ESE22}
\]
This is the required conditioning-and-mixture step. The global differentiation was already performed in (ESE15); no derivative of an outside marginal has been ignored by conditioning prematurely.

Finally (ESE4), \(\int_0^t(1-s/t)ds=t/2\), and (ESE15) give, for every \(x\), unit \(v\), and \(t>0\),
\[
 \boxed{\displaystyle
 |X_{e,v}\log\psi(x)|
 \le\sqrt{\frac{\omega_e}{\kappa t}+4\beta}
                          +\frac{\kappa\beta t}{2},
 \qquad
 M_e\le\sqrt{\frac{\omega_e}{\tau}+4\beta}+\frac{\tau\beta}{2}
 \quad(\tau=\kappa t>0).}
 \tag{ESE23}
\]
Taking the supremum over unit directions gives the original three-component metric gradient norm, without an added factor \(\sqrt3\).

## 5. Closing and optimizing the bound without a heat-kernel oscillation claim

The diameter in the original metric gives the unconditional relation
\[
 \omega_e\le2\pi M_e.
 \tag{ESE24}
\]
For each fixed exterior configuration, integrate the derivative of \(\log\psi\) along a shortest one-link geodesic of length at most \(2\pi\), then maximize over the exterior. This proves (ESE24) directly for the actual vacuum.

If \(M_e=0\), every following score bound is immediate. For \(\beta>0\) and \(M_e>0\), choose the permitted time \(\tau=cM_e/\beta\), with any \(0<c<2\). Substitution of (ESE24) into (ESE23) yields
\[
 M_e\le\sqrt{\beta(2\pi/c+4)}+\frac c2M_e,\qquad
 M_e^2\le\beta\,\Phi(c),\qquad
 \Phi(c)=\frac{2\pi/c+4}{(1-c/2)^2}.
 \tag{ESE25}
\]
The unknown positive \(M_e\) is used only to select a time in an inequality already proved for every positive time. This does not assume the desired estimate or change the Hamiltonian.

In particular \(c=1/2\) gives the completely explicit bounds
\[
 M_e\le\frac83\sqrt{1+\pi}\sqrt{\beta},\qquad
 |\nabla_e\log\rho|
       \le\frac{16}{3}\sqrt{1+\pi}\sqrt{\beta}.
 \tag{ESE26}
\]
The exact optimal constant obtainable from (ESE24)–(ESE25) is also explicit:
\[
 c_*=\frac{\sqrt{9\pi^2+32\pi}-3\pi}{8},\quad
 C_\psi=\sqrt{\Phi(c_*)},\quad C_\rho=2\sqrt{\Phi(c_*)},\qquad
 \boxed{M_e\le C_\psi\sqrt{\beta},\quad
             |\nabla_e\log\rho|\le C_\rho\sqrt{\beta}.}
 \tag{ESE27}
\]
Indeed
\[
 \Phi'(c)=
   \frac{4c^2+3\pi c-2\pi}{c^2(1-c/2)^3}.
 \tag{ESE28}
\]
The numerator is strictly increasing for \(c>0\), is negative at zero and positive at two, and has exactly the positive root \(c_*\) displayed in (ESE27). The denominator is positive on \((0,2)\), and \(\Phi(c)\) tends to infinity at each endpoint. Thus this root is the unique global minimizer on the exact allowed interval.

The former score estimate is retained as well. With \(w_e=|\nabla_eu|^2\), the full vacuum equation and the radius-two Ricci tensor give
\[
 (\Delta+2\nabla u\cdot\nabla)w_e
   =2\sum_f|\nabla_f\nabla_eu|_{\rm HS}^2+w_e
                   +2\kappa^{-1}\langle\nabla_eu,\nabla_eV\rangle.
 \tag{ESE29}
\]
This follows by differentiating
\(\Delta u+|\nabla u|^2=(V-E_0)/\kappa\); commuting the factor-\(e\) derivatives contributes twice its Ricci tensor, namely \(w_e\), and retains every mixed Hessian square. At a maximum, (ESE4) implies \(0\ge w_e-2\beta\sqrt{w_e}\), hence \(M_e\le2\beta\). Combining with (ESE27) proves
\[
 \boxed{\displaystyle
 |\nabla_e\log\rho|
    \le \min\{\,4r_e\xi,\ C_\rho\sqrt{r_e\xi}\,\}.}
 \tag{ESE30}
\]
At \(\beta=0\), the potential is independent of the chosen edge. Left translations of that edge commute with the full Hamiltonian. Uniqueness of the positive unit vacuum makes it invariant under those translations, so \(M_e=\omega_e=0\) and (ESE30) still holds.

The same proof applies, with every original scalar retained, to the all-real face-source Hamiltonian
\[
 H(x)=\kappa K+\kappa\sum_px_p(2-W_p),\qquad
 \beta_e(x)=\sum_{p:e\in\partial p}|x_p|,\qquad
 |\nabla_e\log\rho_x|
       \le\min\{4\beta_e(x),C_\rho\sqrt{\beta_e(x)}\}.
 \tag{ESE31}
\]
To verify the extension, the incident potential need not be nonnegative, but its range has length at most \(4\kappa\beta_e(x)\) and its gradient norm is at most \(\kappa\beta_e(x)\). These are the only two potential bounds used in (ESE14)–(ESE30). The complete real potential is bounded at every finite source, so the martingale and domination arguments are unchanged; all constant \(2\kappa x_p\) terms remain in their original positions. If \(\beta_e(x)=0\), the same translation argument applies.

## 6. Status of the sharper proposed constant

The requested numerical substitution is exact:
\[
 \sqrt{\frac{4\pi\sqrt{\beta}}{\,2/\sqrt{\beta}\,}+4\beta}
       +\frac{(2/\sqrt{\beta})\beta}{2}
       =\bigl(1+\sqrt{4+2\pi}\bigr)\sqrt{\beta}.
 \tag{ESE32}
\]
Thus the pathwise derivative and entropy portion of that proposed calculation has all its stated constants. The separate oscillation assertion
\(\omega_e\le4\pi\sqrt{\beta}\) is not proved in this note and is not used in (ESE27), (ESE30), or (ESE31). Its independent verification is needed before the smaller density-score constant \(2+2\sqrt{4+2\pi}\) is recorded as proved. The unconditional square-root improvement above already follows from the actual full vacuum and needs no such assertion.

## 7. Receiving improvement for the original raw phase, with the unchanged path

Keep precisely the original \(F=p-r\), all coefficients, rooted words and affine remainders defined in PRE10–PRE16. PRE32–PRE36 prove degree at most two along every original physical edge subgroup, including all tree links. PRE37–PRE40 then prove, directly in any smooth density with edge score bound \(B_e\),
\[
 \mu(|X_{e,\alpha}F|^2)
       \le b_2(B_e)\,\mu(F^2),\qquad
 b_2(B)=\frac{75}{64}(1+r_B^2)^5e^{4B\arctan r_B}
                  \frac{\arctan r_B}{r_B^3},\quad
 r_B=\frac1{2(B+2)},\quad
 \frac{b_2(B)}{B^2}\longrightarrow\frac{75e^2}{16}.
 \tag{ESE33}
\]
The proof uses the exact coefficient Gram functional \(75/8\), integrates along the full original subgroup interval \([-4\arctan r_B,4\arctan r_B]\), and averages every center in the actual vacuum. It therefore applies to (ESE30) with every outside correlation present.

For \(r=2,3,4\) put
\[
 B_r(\xi)=\min\{4r\xi,C_\rho\sqrt{r\xi}\}.
 \tag{ESE34}
\]
The exact edge multiplicities are \(12m\), \(12m(m-1)\), \(3m(m-1)^2\), respectively. Consequently the original raw quantities
\(G=\mu(F^2)\), \(C_F=\kappa\mu(|\nabla F|^2)\) obey the stronger direct estimate
\[
 \boxed{\displaystyle
 \frac{C_F}{G}\le\kappa\,\widetilde{\mathcal B}_L(\xi),\qquad
 \widetilde{\mathcal B}_L(\xi)=
 3\left[
 12m\,b_2(B_2(\xi))
 +12m(m-1)b_2(B_3(\xi))
 +3m(m-1)^2b_2(B_4(\xi))\right].}
 \tag{ESE35}
\]
This uses the unchanged factor three for the three colour fields. It is a bound for the complete raw quotient, not a ratio of separate lower estimates.

For the original simultaneous path
\[
 L_j=j^4,\quad a_j=\frac1{100j},\quad
 g_j^2=\frac{\kappa_*}{200j},\quad \kappa=\kappa_*,\quad
 \xi_j=\frac{10000j^2}{\kappa_*^2},\quad
 s_j=\frac{\kappa_*}{j},\quad m_j=2j^4,\qquad j\ge2,
 \tag{ESE36}
\]
the new upper bound has the evaluated asymptotic constant
\[
 \boxed{\displaystyle
 \lim_{j\to\infty}
 \frac{\kappa_*\widetilde{\mathcal B}_{L_j}(\xi_j)}{j^{14}}
       =\frac{13500000\,e^2 C_\rho^2}{\kappa_*}.}
 \tag{ESE37}
\]
Indeed \(B_r(\xi_j)=C_\rho\sqrt{r\xi_j}\) for all sufficiently large \(j\). In the leading interior term there are \(3m_j(m_j-1)^2\sim24j^{12}\) edges, with \(r=4\), while its score square is
\(40000C_\rho^2j^2/\kappa_*^2\). Multiplying by the three colour directions and the limit \(75e^2/16\) in (ESE33) gives
\(3\cdot24\cdot(75e^2/16)\cdot40000
=13500000e^2\).
The boundary terms have strictly smaller orders and their exact finite expressions remain in (ESE35).

The corresponding raw endpoint estimate is
\[
 G_j-\frac{C_{F,j}}{s_j}
       \ge[1-j\widetilde{\mathcal B}_{L_j}(\xi_j)]G_j,\qquad
 \frac{j\widetilde{\mathcal B}_{L_j}(\xi_j)}{j^{15}}
       \longrightarrow\frac{13500000e^2C_\rho^2}{\kappa_*^2}.
 \tag{ESE38}
\]
Thus the unconditional score strengthens the proved quotient order from PRE's \(j^{16}\) to \(j^{14}\), while the evaluated endpoint coefficient still eventually becomes negative. This does not decide the actual shrinking-window endpoint or prove gaplessness. All original phase and Hamiltonian factors remain intact.


The separate oscillation estimate discussed in ESE32 is now proved in [HR1–HR25](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/HEAT_RATIO_PROOF.md) and [LS7–LS18](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/SQUARE_ROOT_LOCAL_SCORE.md). Together with this exact entropy derivation it gives the smaller constant in LS32. [ID53–ID57](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/INDEPENDENT_EDGE_ENTROPY_PROOF.md) retain the exact edge-marginal information identity and prove the optimal finite-range entropy bound.
