# Positive slab stresses and their comparison with vacuum gravity

This paper recovers the separate mathematical result developed before the supplied Rindler spectral manuscript: a class of positive boundary stresses obtained from elliptic extensions, and global smoothness for the modified three-dimensional fluid equations they define. The derivation below states the hypotheses and continuation estimate explicitly. It does not replace the original NS forcing or identify this stress with the exact Einstein response.

## 1. The finite-slab map

Let $U$ be a smooth divergence-free field on $\mathbb R^3$, $S=(DU+DU^T)/2$, $\Lambda=(-\Delta)^{1/2}$, and $L,\kappa>0$. Extend each strain component to $0\le y\le L$ by

$$
(\partial_y^2+\Delta_x)Q=0,\qquad Q(x,0)=S(x),\qquad
\partial_yQ(x,L)=0.
$$

For physical wavenumber $k=|\xi|$,

$$
\widehat Q(\xi,y)=\frac{\cosh(k(L-y))}{\cosh(kL)}\widehat S(\xi),
\qquad -\partial_yQ|_0=\Lambda\tanh(L\Lambda)S.
$$

Consequently the symmetric stress per unit mass
$\tau^Q=2\kappa\Lambda\tanh(L\Lambda)S$ has divergence

$$
g=\operatorname{div}\tau^Q=-\kappa\Lambda^3\tanh(L\Lambda)U.
$$

This is the exact composition
$U\mapsto S\mapsto Q\mapsto-\partial_yQ|_0\mapsto\tau^Q\mapsto g$.
The added coordinate is an elliptic extension coordinate. No field-equation-preserving identification with a gravitational radial coordinate has been established. Extension representations of fractional operators provide the broader setting; the finite-slab formula follows from the displayed ODE ([Caffarelli and Silvestre, 2007](https://arxiv.org/abs/math/0608640)).

Integration by parts proves

$$
\int S:\Lambda\tanh(L\Lambda)S\,dx
=\int_0^L\int(|\partial_yQ|^2+|\nabla_xQ|^2)\,dx\,dy.
$$

For the modified equation

$$
\partial_tU+(U\cdot\nabla)U+\nabla P+
\nu\Lambda^2U+\kappa\Lambda^3\tanh(L\Lambda)U=f,
\quad\operatorname{div}U=0,
\tag{S1}
$$

the energy identity, with constant physical mass density $\rho_0$, is

$$
\frac{d}{dt}\frac{\rho_0}2\|U\|_2^2+
\rho_0\nu\|\nabla U\|_2^2+
\rho_0\kappa\|\Lambda^{3/2}\sqrt{\tanh(L\Lambda)}U\|_2^2
=\rho_0\langle f,U\rangle.
\tag{S2}
$$

Thus the extension contributes positive dissipation. The length/time dimensions are $[\nu]=\mathrm{length}^2/\mathrm{time}$ and $[\kappa]=\mathrm{length}^3/\mathrm{time}$.

At small $k$, its added damping is
$\kappa Lk^4-\kappa L^3k^6/3+O(k^8)$. Matching the fourth-order linear coefficient of the vacuum-fluid expansion requires

$$
\kappa L=3\nu^3/(2c^2).
\tag{S3}
$$

For example $L=\nu/c$ gives $\kappa=3\nu^2/(2c)$. This matches a coefficient from [Compère et al., (6.3)](https://arxiv.org/html/1103.3022v2). The complete higher-order nonlinear terms remain in the [predecessor comparison](archive/ns-vacuum-propagation/docs/HIGHER_ORDER.md). The [Rindler response](manuscripts/RESEARCH.md) derives a different all-frequency function from Einstein's equations.

## 2. Stratification and a global regularity theorem

Let $a,b$ be measurable functions of extension depth alone satisfying
$0<a_-\le a\le a_+<\infty$ and $0<b_-\le b\le b_+<\infty$. They are independent of the fluid coordinates and time. Define

$$
m(k)=\inf_{q\in H^1(0,L),\ q(0)=1}
\int_0^L[a(y)|q'(y)|^2+b(y)k^2|q(y)|^2]dy.
\tag{S4}
$$

The free endpoint gives the Neumann condition at $L$. The associated positive Fourier multiplier $\mathcal N$ has symbol $m(k)$. Comparing the energies before taking infima gives

$$
\sqrt{a_-b_-}\,k\tanh\big(Lk\sqrt{b_-/a_-}\big)
\le m(k)\le
\sqrt{a_+b_+}\,k\tanh\big(Lk\sqrt{b_+/a_+}\big).
\tag{S5}
$$

Apply $\mathcal N$ componentwise to strain. The stress $2\kappa\mathcal NS$ has divergence $-\kappa\Lambda^2\mathcal NU$, since $\mathcal N$ commutes with spatial derivatives.

**Theorem.** Fix $\nu,\kappa,L>0$ and coefficients satisfying these bounds. For divergence-free $U_0\in\bigcap_{s\ge0}H^s(\mathbb R^3)$ and smooth forcing whose corresponding Sobolev norms are bounded on each finite time interval, the equation

$$
\partial_tU+(U\cdot\nabla)U+\nabla P+
\nu\Lambda^2U+\kappa\Lambda^2\mathcal NU=f,
\qquad \operatorname{div}U=0,
\tag{S6}
$$

has a unique global smooth velocity solution. Pressure is determined up to its usual spatial constant. The proof uses a high-frequency lower bound and is a specific application of the established hyperdissipative mechanism, not a claim of priority for that mechanism ([Tao, 2009](https://arxiv.org/abs/0906.3070)).

**Proof.** Put

$$
k_*=L^{-1}\sqrt{a_-/b_-},\qquad
c_*=\kappa\sqrt{a_-b_-}\tanh1.
$$

The full damping symbol $d(k)=\nu k^2+\kappa k^2m(k)$ satisfies $d(k)\ge c_*k^3$ for $k\ge k_*$. The energy identity gives
$\|U(t)\|_2\le I(t):=\|U_0\|_2+\int_0^t\|f(s)\|_2ds$.
For $Y=\|\nabla U\|_2^2$, $E=\|U\|_2$, $D=\|\Lambda^{5/2}U\|_2$, Fourier splitting yields differentiated dissipation at least $c_*(D^2-k_*^5E^2)$.

The differentiated nonlinear term is bounded by

$$
\|\nabla U\|_3^3\le C_{\rm GN}^3 E^{6/5}D^{9/5}
\le \frac{c_*}2D^2+C_Yc_*^{-9}E^{12},
\qquad C_Y=\frac1{10}(9/5)^9C_{\rm GN}^{30}.
$$

The first inequality is the three-dimensional Gagliardo–Nirenberg inequality with interpolation exponent $3/5$; the second follows by maximizing the left side minus $c_*D^2/2$ in $D$. For every physical reference time $t_*>0$, Cauchy–Schwarz and Young applied to the differentiated forcing give

$$
Y'\le Y/t_*+2C_Yc_*^{-9}I^{12}
+2c_*k_*^5I^2+t_*\|\nabla f\|_2^2.
\tag{S7}
$$

Grönwall therefore bounds $Y$ on every finite interval. To make continuation explicit, the multiplier semigroup has
$\|e^{-tA}\|_{H^{-1}\to H^1}\le C(1+t^{-2/3})$
on bounded positive time intervals. This follows by maximizing $(1+k^2)e^{-td(k)}$ and using the high-frequency cubic bound. Meanwhile,

$$
\|\mathbb P\operatorname{div}(U\otimes V)\|_{H^{-1}}
\le C\|U\|_{H^1}\|V\|_{H^1},
$$

by $H^1(\mathbb R^3)\hookrightarrow L^4$. The integrable $t^{-2/3}$ singularity gives a local mild contraction with lifespan bounded below on bounded $H^1$ sets. Equation (S7) prevents loss of that bound. The cubic high-frequency smoothing and smooth data give higher regularity by iteration. This proves global smoothness and uniqueness. The homogeneous-slab equation (S1) is the case $a=b=1$. ∎

## 3. Layer composition and its limit

For $k>0$ and a homogeneous layer $j$ of thickness $L_j>0$, let
$Z_j(k)=\sqrt{a_jb_j}k$ and $s_j(k)=L_jk\sqrt{b_j/a_j}$. Propagating the field and conormal derivative through the layer gives its input response to a nonnegative load $z$:

$$
\mathcal T_j(z;k)=
\frac{Z_j\tanh s_j+z}{1+(z/Z_j)\tanh s_j}.
\tag{S8}
$$

Thus $m_N(k)=\mathcal T_1(\mathcal T_2(\cdots\mathcal T_N(0;k)\cdots);k)$ for $k>0$, with $m_N(0)=0$ by continuous extension. For nested initial segments of one uniformly elliptic medium, restriction of competitors in (S4) proves $m_{N+1}\ge m_N$. Trial functions obtained from the constant-coefficient half-line problem give

$$
\sqrt{a_-b_-}k\tanh(L_1k\sqrt{b_-/a_-})
\le m_N(k)\le\sqrt{a_+b_+}k.
\tag{S9}
$$

Hence the symbols increase to a finite positive limit. The same uniform high-frequency bound applies to the limiting Fourier-multiplier equation, and the preceding theorem applies directly to that equation. This statement does not assert any unproved convergence of nonlinear trajectories.

For finite total depth $D_N=\sum_{j=1}^N L_j$, the low-frequency expansion instead has

$$
m_N(k)=B_Nk^2+O(k^4),\qquad B_N=\int_0^{D_N}b(y)dy.
$$

If $D_N\to\infty$ and $b\ge b_->0$, then $B_N\to\infty$. Holding a fourth-order coefficient $\chi=\kappa_NB_N$ fixed forces $\kappa_N\to0$, so the uniform coercivity constant is lost. Uniform regularity with fixed positive $\kappa$ and preservation of a finite fixed low-frequency coefficient are different limiting requirements.

## 4. The precise map back to NS

Let $U$ be the original smooth NS solution on $[0,T]$, $T<T_0$, and let $U_\varepsilon$ solve (S1) with $\kappa$ replaced by $\varepsilon\kappa$, with the same initial data and forcing. Set $\mathcal A_L=\Lambda^{3/2}\sqrt{\tanh(L\Lambda)}$. Taking the difference energy, retaining the added positive term, and applying Young gives

$$
\|U_\varepsilon(t)-U(t)\|_2^2\le
\varepsilon\kappa
\exp\left(2\int_0^t\|\nabla U(s)\|_\infty ds\right)
\int_0^t\|\mathcal A_LU(s)\|_2^2ds.
\tag{S10}
$$

The residual under the original equation is exactly
$\mathcal R_{\rm NS}[U_\varepsilon,P_\varepsilon,f]
=-\varepsilon\kappa\Lambda^3\tanh(L\Lambda)U_\varepsilon$.
Every fixed $\varepsilon>0$ gives a globally smooth modified flow. Neither the bound nor the continuation constants are uniform through the original terminal time as $\varepsilon\downarrow0$.

There is a related exact source-cancellation calculation. If the leading metric force is represented by $(\partial_t+\mathcal L_U)a=-f^\flat$, and an additional force $g$ enters the fluid equation, then

$$
(\partial_t+U\cdot\nabla)B-(B\cdot\nabla)U
=\nu\Delta\omega+\operatorname{curl}g,
\quad B=\operatorname{curl}(U+a),\quad\omega=\operatorname{curl}U.
$$

Erasing $B$ identically from zero initial data requires
$\operatorname{curl}g=-\nu\Delta\omega$. On the decaying simply connected class this means $g=-\nu\Delta U+\nabla\psi$, which injects power $\rho_0\nu\|\nabla U\|_2^2$, exactly cancelling viscous dissipation. Erasure of that leading curvature coefficient does not give a dissipative regularization.

## 5. Anomaly inflow and quantum response: what the maps assert

For a specified invertible anomaly theory $\alpha_5$, a relative boundary amplitude belongs to its line $\mathcal L_{\mathcal B}$. A bulk state in the dual line gives the pairing

$$
Z_4[M,\mathcal B]\otimes Z_{\alpha_5^{-1}}[Y,\mathcal B]
\xrightarrow{\operatorname{ev}_{\mathcal L}}\mathbb C,
\qquad \alpha_5\otimes\alpha_5^{-1}\simeq\mathbf1.
$$

This is the relative-theory construction of [Freed and Teleman](https://arxiv.org/abs/1212.1692) and the invertible-anomaly framework described by [Freed](https://arxiv.org/abs/1404.7224). The filling and extended backgrounds are data. Neutral NS velocity and forcing alone specify no anomaly theory. No anomaly of the particular NS construction was computed here.

The historical local Spin–$U(1)$ benchmark uses Weyl chiralities $\chi_r$ and integer charges $q_r$, with $k_3=\sum\chi_rq_r^3$, $k_1=\sum\chi_rq_r$. Expanding the index density gives

$$
I_6=\frac{k_3}{6}c_1^3-\frac{k_1}{24}c_1p_1,
\quad c_1=d\mathsf A/(2\pi),\quad
p_1=-\operatorname{tr}(\mathcal R\wedge\mathcal R)/(8\pi^2).
$$

With $I_5^{(0)}=(\mathsf A/2\pi)\wedge[k_3c_1^2/6-k_1p_1/24]$, one has $\delta I_5^{(0)}=dI_4^{(1)}$. The convention $\delta W_4=2\pi\hbar\int I_4^{(1)}$ is cancelled by $S_{\rm in}=-2\pi\hbar\int_YI_5^{(0)}$. A global theory needs its eta-invariant/differential refinement ([Witten and Yonekura](https://arxiv.org/abs/1909.08775)); the local descent calculation alone is not a global anomaly audit. The earlier conversation also mentions a Spin–$U(1)$ bordism benchmark, finite Wilson–Dirac models and swampland examples. No source-specific anomaly, microscopic-to-slab map or general swampland theorem was delivered, and none is needed for (S6).

Anomaly cancellation cannot be substituted for an Einstein constraint. If total boundary stress is $\mathbb T=T^{\rm BY}+\tau$, the Brown–York inverse is

$$
K_{ab}=C_5^{-1}\left[
\frac{\mathbb T-\tau}{3}\gamma_{ab}-(\mathbb T_{ab}-\tau_{ab})\right].
$$

A simultaneous shift $(\mathbb T,\tau)\mapsto(\mathbb T+s,\tau+s)$ leaves geometry unchanged. Nor does triviality of an anomaly character $\chi:B\to U(1)$ imply $B=0$: the trivial character on $\mathbb Z/2$ is an explicit counterexample. These are exact comparison statements, not a new S6 topology result.

For a specified regulated thermofield state and transpose-paired Hermitian observable, after separating its conserved zero-frequency sector,

$$
C_{LR}(\omega)=\frac{\hbar\operatorname{Im}\chi_R(\omega)}{
\sinh(\beta\hbar\omega/2)}.
$$

This follows directly from spectral weights and the response convention $\chi_R(t)=(i/\hbar)\Theta(t)\langle[O(t),O(0)]\rangle$. The chosen equilibrium relaxation model
$\chi_R=\chi_s d(k)/(d(k)-i\omega)$,
$d(k)=\nu k^2+\kappa k^3\tanh(Lk)$, has classical two-sided covariance $k_BT\chi_s e^{-|t|d(k)}$. Its equal-time variance is independent of damping. For the flat-source leading curvature coefficient $R_{n012}=-\omega_3/(2\nu)$, a spherical wavenumber cutoff gives

$$
\langle R_{n012}^2\rangle=
\frac{k_BT}{60\pi^2\rho_0\nu^2}K_{\max}^5.
$$

The source-driven coefficient needs the covariances of $a$ and its cross terms as well. This equilibrium model is not a microscopic quantization of (S6), a time-dependent calculation on the concentrating NS core, or a reconstruction of a two-sided Einstein spacetime.

The retained result is the explicit extension-to-stress map, the modified-equation theorem and its comparison estimate. The supplied Rindler manuscript subsequently computes an actual linear gravitational response and shows why the comparator's cubic damping is not that response.
