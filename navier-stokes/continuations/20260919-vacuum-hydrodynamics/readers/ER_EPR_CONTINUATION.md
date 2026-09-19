*GitHub reading copy; only mathematical delimiters have changed. [Unchanged source](../archive/er-epr-continuation/docs/ER_EPR_CONTINUATION.md).*

# Two-sided entanglement, vacuum-fluid circulation, and gravitational frame transport

## 1. The calculated object

The two-sided observable developed here is the correlation of the gravitational normal-frame connection. On a timelike gravitational cutoff, that connection is exactly a projection of Brown–York momentum. In the thermal, linear hydrodynamic sector of a specified two-sided Einstein geometry, its left–right correlation is

$$
\boxed{
\mathcal C^{\mathcal A_i\mathcal A_j}_{LR}(\omega,\mathbf k)
=
\frac{4\pi\hbar G_5}{c^3}\,\zeta_c\,
\frac{k^2\omega}
{(\omega^2+\nu^2 k^4)\sinh(2\pi\nu\omega/c^2)}
\left(\delta_{ij}-\frac{k_i k_j}{k^2}\right),\qquad k\ne0.
}\tag{1.1}
$$

Here $\zeta_c=(r_h/r_c)^3$ is retained. The label $LR$ always uses the explicit transpose pairing of the left operator in Section 3, with the same pairing for the left gravitational source. Equation (1.1) is a leading semiclassical, leading hydrodynamic correlation function, with its full quantum thermal factor retained. It is not an all-frequency constitutive equation. It is computed below both from the entangled thermal preparation and from the two-sided black-brane prescription. The same connection has the nonlinear fluid coefficient

$$
\mathcal A^{\mathrm{NS}}=-\frac{\zeta_c}{2\nu}(U_i+a_i)\,dx^i,\tag{1.2}
$$

where $a$ is reconstructed from the actual force, not set to zero. Its curvature coefficient has an exact material evolution law, and that law admits a quantitative lower bound in terms of the full Navier–Stokes velocity. Thus there are two concrete calculations: a two-sided quantum/gravitational response, and a nonlinear source-dependent circulation observable.

The input is the full preterminal velocity, pressure, and smooth force retained in `archive/ns-vacuum-propagation/docs/PROPAGATION.md`. No further proof of the upstream Navier–Stokes existence theorem is asserted here. The earlier package is preserved unchanged. The new derivations do not identify its leading vortex profile with the full corrected solution.

The foundational two-sided setting is the thermofield construction of Maldacena (2003); the real-time bulk matching is Herzog and Son (2003); the horizon transport calculation is Iqbal and Liu (2009). The proposed general ER = EPR statement is broader than these calculable sectors (Maldacena & Susskind, 2013). The final section states exactly which part has and has not been established.

## 2. A two-sided Einstein family with fixed physical viscosity

### 2.1 Metric, cutoff, and physical coordinates

Let $L,r_h,G_5,c,\hbar,k_B$ be positive. Consider the five-dimensional planar Einstein metric

$$
ds^2=\frac{r^2}{L^2}\big[-c^2 f(r)dt_b^2+d\mathbf x_b^2\big]
+\frac{L^2}{r^2f(r)}dr^2,
\qquad f(r)=1-\frac{r_h^4}{r^4},\tag{2.1}
$$

with its maximally extended two-sided geometry. Its equation is $R_{AB}=-4g_{AB}/L^2$, equivalently vacuum Einstein gravity with $\Lambda=-6/L^2$. The cosmological term has not been suppressed.

Choose $r_c>r_h$, and put

$$
f_c=f(r_c),\quad N_c=\frac{r_c\sqrt{f_c}}{L},\quad
 t=N_ct_b,\quad x^i=\frac{r_c}{L}x_b^i,\quad x^0=ct.\tag{2.2}
$$

The induced metric at the cutoff is $-(dx^0)^2+d\mathbf x^2$. The outward unit normal is $n=(r\sqrt f/L)\partial_r$. Define

$$
K_{ab}=\gamma_a{}^A\gamma_b{}^B\nabla_A n_B,
\quad \mathcal C_5=\frac{c^4}{8\pi G_5},
\quad \mathsf T_{ab}=\mathcal C_5(K\gamma_{ab}-K_{ab}).\tag{2.3}
$$

At the flat cutoff, the local counterterm $-3\mathcal C_5\gamma_{ab}/L$ subtracts the pure-AdS background. All thermodynamic quantities below include this subtraction. It has zero mixed contraction with a vector tangent to a spatial cut and its timelike normal; it therefore does not change the normal-frame connection calculated in Section 5. Intrinsic-curvature counterterms for curved sources can generate additional local contact terms and are not assumed absent at higher derivative order.

Direct radial differentiation gives

$$
K_{00}=-\frac{\sqrt{f_c}}L-\frac{r_cf'_c}{2L\sqrt{f_c}},
\quad K_{ij}=\frac{\sqrt{f_c}}L\delta_{ij}.
$$

Consequently

$$
\varepsilon_c=\frac{3\mathcal C_5}L(1-\sqrt{f_c}),\qquad
p_c=\frac{\mathcal C_5}L
\left(3\sqrt{f_c}-3+\frac{r_cf'_c}{2\sqrt{f_c}}\right),\tag{2.4}
$$

$$
w_c=\varepsilon_c+p_c
=\frac{2\mathcal C_5 r_h^4}{Lr_c^4\sqrt{f_c}},
\qquad \chi_c=\frac{w_c}{c^2}.\tag{2.5}
$$

$\chi_c$ is momentum susceptibility, not a claim that the microscopic theory has the material rest-mass density of an arbitrary classical liquid.

The Hawking temperature in boundary time and the redshifted cutoff temperature are

$$
T_H=\frac{\hbar c r_h}{\pi k_B L^2},\qquad
T_c=\frac{T_H}{N_c}
=\frac{\hbar c r_h}{\pi k_B Lr_c\sqrt{f_c}}.\tag{2.6}
$$

Horizon area per proper cutoff spatial volume gives

$$
s_c=\frac{k_Bc^3}{4\hbar G_5}\left(\frac{r_h}{r_c}\right)^3,
\qquad
\eta_c=\frac{c^3}{16\pi G_5}\left(\frac{r_h}{r_c}\right)^3.\tag{2.7}
$$

The second formula is also obtained from the gravitational radial flux below. These quantities obey the exact background identities

$$
w_c=T_cs_c,\qquad
\nu_c=\frac{\eta_c}{\chi_c}
=\frac{cLr_c\sqrt{f_c}}{4r_h}
=\frac{\hbar c^2}{4\pi k_BT_c}.\tag{2.8}
$$

These statements concern the Einstein two-derivative model and its equilibrium/linear-response transport, not arbitrary materials or higher-curvature actions (Iqbal & Liu, 2009).

### 2.2 An explicit family preserving the input viscosity

Fix the Navier–Stokes viscosity $\nu>0$. For each $L>0$ define

$$
a_L=\frac{4\nu}{cL},\qquad
y_L=\left[\frac{a_L^2+\sqrt{a_L^4+4}}2\right]^{1/2},\qquad
r_c=y_Lr_h.\tag{2.9}
$$

Then $y_L^2-y_L^{-2}=a_L^2$. Substitution into (2.8) proves $\nu_c=\nu$ for every member of the family. In particular,

$$
T_c=\frac{\hbar c^2}{4\pi k_B\nu},\quad
\zeta_c=y_L^{-3},\quad
\chi_c=\frac{\mathcal C_5\zeta_c}{2c\nu},\quad
\eta_c=\frac{\mathcal C_5\zeta_c}{2c}.\tag{2.10}
$$

No temperature, viscosity, speed, length, or gravitational coupling is assigned the value one. $r_h$ can remain a fixed positive length along this family; it cancels from the metric expressed in proper cutoff coordinates.

The exact proper radial distance from the horizon is

$$
\rho(r)=\int_{r_h}^r\frac{L\,dr'}{r'\sqrt{1-r_h^4/r'^4}}
=\frac L2\operatorname{arcosh}\left(\frac{r^2}{r_h^2}\right).\tag{2.11}
$$

Thus $r=r_h\sqrt{\cosh(2\rho/L)}$, and $\rho_c=(L/2)\operatorname{arcosh}(y_L^2)$. In the coordinates (2.2), the metric is exactly

$$
\begin{aligned}
ds^2={}&-c^2
\frac{\sinh^2(2\rho/L)/\cosh(2\rho/L)}
{\sinh^2(2\rho_c/L)/\cosh(2\rho_c/L)}dt^2\\
&+\frac{\cosh(2\rho/L)}{\cosh(2\rho_c/L)}d\mathbf x^2+d\rho^2.
\end{aligned}\tag{2.12}
$$

At fixed $\nu$ and fixed finite $\rho>0$, as $L\to\infty$,

$$
\rho_c\longrightarrow\frac{2\nu}c,
\quad \zeta_c\longrightarrow1,
\quad ds^2\longrightarrow
-\frac{c^4\rho^2}{4\nu^2}dt^2+d\rho^2+d\mathbf x^2.\tag{2.13}
$$

The convergence and all coordinate derivatives are local on compact subsets away from the static-coordinate horizon. The limiting horizon itself is regular in Minkowski coordinates $X^0=\rho\sinh(c^2t/(2\nu))$, $X^4=\rho\cosh(c^2t/(2\nu))$ on the right wedge; the left wedge has $X^4=-\rho\cosh(c^2t_L/(2\nu))$ and its own future-directed $t_L$. This is a local two-sided limit, not a theorem that the global topology of an Einstein–Rosen bridge is invariant under the limit.

Set $\ell=\nu/c$, $R=\rho^2/(4\ell)$, and

$$
x^0_{\mathrm{EF}}=ct+2\ell\log(\rho/\rho_*),\qquad \rho_*>0.\tag{2.14}
$$

Substitution into (2.13) gives exactly

$$
ds^2=-\frac R\ell(dx^0_{\mathrm{EF}})^2+2dx^0_{\mathrm{EF}}dR+d\mathbf x^2,\qquad R_c=\ell.\tag{2.15}
$$

This is the seed used by the prior vacuum-fluid calculation. The map (2.9)–(2.15), rather than an identification of unrelated coordinate viscosities, connects the two-sided AdS benchmark to that seed. At every finite $L$, there is a genuine two-sided black-brane geometry; in the limit, the local horizon geometry is flat Rindler space. The construction does not yet supply a nonlinear two-sided bulk solution for the singular NS field.

## 3. The EPR calculation: cross-side momentum correlation

### 3.1 Preparation and the exact spectral factor

Fix a finite-volume ultraviolet regulator and a faithful Gibbs state for the selected Hamiltonian $H$,

$$
\rho_\beta=Z^{-1}e^{-\beta H},\qquad
\beta=(k_BT_c)^{-1},\qquad
|\Omega_\beta\rangle=\sum_n\sqrt{p_n}|n\rangle_L|n\rangle_R,
\quad p_n=Z^{-1}e^{-\beta E_n}.\tag{3.1}
$$

The left observable corresponding to a right operator $O$ is defined using its matrix transpose in this displayed energy basis. This fixes the left identification, including the orientation of the future time on each side. For a Hermitian real-smeared operator,

$$
C_{LR}(t)=\langle\Omega_\beta|O_L^{\mathsf T}(0)O_R(t)|\Omega_\beta\rangle
=\operatorname{Tr}\big(\sqrt{\rho_\beta}O(t)\sqrt{\rho_\beta}O\big).\tag{3.2}
$$

With both sides evolved toward their respective futures, the argument of this function is $t_L+t_R$. The transpose in (3.2) denotes the specified operator identification, not a change of time direction hidden in notation.

Use the temporal Fourier transform $\widetilde F(\omega)=\int_{\mathbb R}e^{i\omega t}F(t)dt$. Direct insertion of energy eigenstates gives

$$
C_{LR}(\omega)=2\pi\sum_{m,n}\sqrt{p_mp_n}|O_{mn}|^2
\delta\left(\omega-\frac{E_n-E_m}{\hbar}\right).\tag{3.3}
$$

The commutator spectral distribution is

$$
\varrho_O(\omega)=2\pi\sum_{m,n}(p_m-p_n)|O_{mn}|^2
\delta\left(\omega-\frac{E_n-E_m}{\hbar}\right).\tag{3.4}
$$

On each nonzero-frequency contribution, $p_n/p_m=e^{-\beta\hbar\omega}$, so

$$
\boxed{C_{LR}(\omega)=\frac{\varrho_O(\omega)}{2\sinh(\beta\hbar\omega/2)}.}\tag{3.5}
$$

A zero-frequency conserved contribution is treated as a distributional limit or separately by its Gibbs variance; it cannot be recovered by dividing two zero numbers. This qualification matters for the total momentum sector.

For a source coupling $H'=-jO$, define the physical response

$$
\mathcal G_R(t)=\frac{i}{\hbar}\Theta(t)\operatorname{Tr}(\rho_\beta[O(t),O(0)]).
\tag{3.6}
$$

Expanding the unitary to first order verifies $\delta\langle O\rangle=\mathcal G_R*j$. The spectral definition gives $\varrho_O=2\hbar\operatorname{Im}\mathcal G_R$, hence

$$
\boxed{C_{LR}(\omega)=\frac{\hbar\operatorname{Im}\mathcal G_R(\omega)}{\sinh(\beta\hbar\omega/2)}.}\tag{3.7}
$$

For direct comparison with a retarded kernel defined as $G_R^{(-i)}(t)=-i\Theta(t)\langle[O(t),O(0)]\rangle$ in the same physical time coordinate, $\mathcal G_R=-G_R^{(-i)}/\hbar$. This fixes the sign by an explicit map. Herzog and Son's half-thermal-circle off-diagonal correlator is the same spectral identity after this translation (Herzog & Son, 2003, eqs. 8–11).

For a time-reversal-invariant spinless sector with a real energy basis, a momentum operator has $\pi^{\mathsf T}=-\pi$. In that sector the correlator of the raw left momentum and right momentum is the negative of the paired correlator used here. The corresponding left source and spatial-frame identification must be transformed with the same sign. Nothing in (3.7) authorizes discarding that transpose.

The regulator makes the trace derivation literal. In continuum QFT, the statement applies to suitably smeared thermal correlation distributions, not to an assumed trace-class density operator for an unregulated local algebra.

### 3.2 The actual hydrodynamic momentum operator

Let $\widehat\pi_i$ denote the momentum operator conjugate to a small velocity source $a_i$ through $H'=-\int a_i\widehat\pi_i\,d^3x$. At the unperturbed flat cutoff it is $\widehat T^{0i}/c$. On a boundary with shift $a_i$, its leading canonical momentum is instead

$$
\pi_i=\chi_c(U_i+a_i).\tag{3.8}
$$

This source contact term is essential. For transverse linear perturbations, the gravitational metric-force equation gives

$$
\partial_t U_i-\nu\Delta U_i=-\partial_ta_i,
\qquad \partial_iU_i=\partial_ia_i=0.
$$

Substituting (3.8) gives

$$
\partial_t\pi_i-\nu\Delta\pi_i=-\chi_c\nu\Delta a_i.
$$

Therefore the retarded response in the transverse sector is

$$
\mathcal G^{\pi\pi}_{R,ij}(\omega,\mathbf k)
=\chi_c\frac{\nu k^2}{\nu k^2-i\omega}
P_{ij}(\mathbf k),\qquad
P_{ij}=\delta_{ij}-\frac{k_ik_j}{k^2}.\tag{3.9}
$$

This derivation retains the shift term rather than incorrectly identifying momentum with $\chi_cU$ while differentiating the source. Terms beyond the leading constitutive expansion are not part of (3.9). Local real contact terms that do not change its spectral part do not alter the displayed nonzero-frequency thermal relation.

Equations (3.7) and (3.9) now yield

$$
\boxed{
C_{LR,ij}^{\pi\pi}(\omega,\mathbf k)
=\frac{\hbar\chi_c\nu k^2\omega}
{(\omega^2+\nu^2k^4)\sinh(\beta\hbar\omega/2)}P_{ij}.
}\tag{3.10}
$$

At $\beta\hbar|\omega|\ll1$ within the hydrodynamic regime, its time transform reduces to

$$
C_{LR,ij}^{\pi\pi}(t,\mathbf k)
=\chi_ck_BT_c\,e^{-\nu k^2|t|}P_{ij}
\quad\text{at leading classical hydrodynamic order}.\tag{3.11}
$$

The finite-temperature factor in (3.10) is retained in all other calculations. At $k\to0$, an unconstrained Gibbs total-momentum sector contains $2\pi\chi_ck_BT_c\delta(\omega)$ per appropriate volume convention. Projecting to fixed total momentum changes that sector and must be specified separately.

A product of the two Gibbs states has zero connected left–right correlator. Equation (3.10) thus distinguishes the chosen entangled preparation from that product preparation. A nonzero two-sided correlator alone is not a universal entanglement witness for arbitrary mixed states; here the global state is explicitly the pure thermofield state (3.1).

## 4. The ER calculation: the same kernel from horizon matching

The tensor perturbation $h^x{}_y=Z(r)e^{-i\omega_bt_b}$ at zero spatial momentum satisfies the massless radial equation

$$
\partial_r(r^5f\partial_rZ)+\frac{L^4r\omega_b^2}{c^2f}Z=0.\tag{4.1}
$$

Near the future horizon the ingoing solution is

$$
Z\sim f^{-i\omega_bL^2/(4cr_h)}
=f^{-i\beta_H\hbar\omega_b/(4\pi)},\qquad
\beta_H=(k_BT_H)^{-1}.\tag{4.2}
$$

The physical quadratic-action radial momentum per boundary coordinate volume is

$$
\Pi=-\frac{c^4}{16\pi G_5}\frac{r^5f}{L^5}\partial_rZ.\tag{4.3}
$$

Substitution of (4.2) gives

$$
\Pi(r_h)=i\omega_b\frac{c^3r_h^3}{16\pi G_5L^3}Z(r_h).
$$

To first order in frequency, (4.1) transports this flux radially without change. Converting to the proper cutoff volume gives exactly $\eta_c$ in (2.7). Momentum conservation then supplies the vector/shear diffusion response (3.9). The zero-momentum tensor equation is used to determine viscosity; it is not silently substituted for the finite-momentum vector perturbation equation (Iqbal & Liu, 2009).

For the full two-sided state, continue the regular modes through the lower/upper half Kruskal planes with the Hartle–Hawking prescription. The two exterior source insertions are separated by half a Euclidean thermal circle. The transition weight is

$$
q_\omega=e^{-\beta_H\hbar\omega_b/2}
=e^{-\beta\hbar\omega/2},\qquad \omega_b=N_c\omega.\tag{4.4}
$$

The last equality follows from (2.2) and (2.6); the product $\beta\hbar\omega$ is unchanged by the redshift. The off-diagonal bulk matching has coefficient

$$
\frac{q_\omega}{1-q_\omega^2}
=\frac1{2\sinh(\beta\hbar\omega/2)}.\tag{4.5}
$$

Multiplying the retarded discontinuity by (4.5) reproduces (3.5), and therefore (3.10). This is the real-time two-boundary calculation, not an appeal to entanglement entropy by itself (Herzog & Son, 2003).

At finite cutoff, these observables can be defined by the two-sided Dirichlet gravitational generating functional and inherited thermal state, with the regulator and edge-mode sector fixed. This is not a claim that every finite-cutoff theory is an autonomous ultraviolet-complete local conformal field theory. The response and continuation are semiclassical holographic calculations in the specified Einstein model. Non-equilibrium doubled constructions exist, but their gradient expansions also have a stated domain (Glorioso et al., 2018).

## 5. From momentum to an exact geometric connection

### 5.1 Normal bundle and signs

Let $S$ be a spacelike three-surface inside a timelike cutoff. Denote its future-directed unit timelike normal within the cutoff by $\tau$ and its outward unit spacelike bulk normal by $n$. Thus $g(\tau,\tau)=-1$, $g(n,n)=1$, $g(\tau,n)=0$. For $e_i\in TS$ define the normal-frame connection

$$
\mathcal A_i=g(n,\nabla_{e_i}\tau).\tag{5.1}
$$

Differentiating $g(n,\tau)=0$ and using (2.3) gives the exact identity

$$
\boxed{
\mathcal A_i=-K_{ia}\tau^a
=\frac{\mathsf T_{ia}\tau^a}{\mathcal C_5}
=-\frac c{\mathcal C_5}\pi_i,
\qquad
\pi_i=-\frac1c\mathsf T_{ia}\tau^a.
}\tag{5.2}
$$

The trace term drops because $\gamma(e_i,\tau)=0$, not by choosing a stress component to neglect. At the flat-background order relevant to (3.10), the AdS subtraction has the same vanishing mixed contraction. Higher curved-source contact terms require the corresponding explicit subtraction.

Under

$$
\tau'=\cosh\lambda\,\tau+\sinh\lambda\,n,
\quad n'=\sinh\lambda\,\tau+\cosh\lambda\,n,
$$

direct differentiation gives

$$
\mathcal A'=\mathcal A+d\lambda.\tag{5.3}
$$

This is the $SO^+(1,1)$ connection on the normal two-plane. Its curvature is $\mathcal F=d\mathcal A$.

The bulk curvature is defined throughout by

$$
R^A{}_{BCD}=\partial_C\Gamma^A{}_{DB}-\partial_D\Gamma^A{}_{CB}
+\Gamma^A{}_{CE}\Gamma^E{}_{DB}-\Gamma^A{}_{DE}\Gamma^E{}_{CB}.
$$

Let $b^{(0)}_{ij}=g(\nabla_{e_i}\tau,e_j)$ and $b^{(1)}_{ij}=g(\nabla_{e_i}n,e_j)$. The full Ricci equation, with these definitions, is

$$
\boxed{
\mathcal F_{ij}=R_{n\tau ij}
+b^{(0)}_j{}^k b^{(1)}_{ik}-b^{(0)}_i{}^k b^{(1)}_{jk}.
}\tag{5.4}
$$

To check the sign, write $\nabla_i\tau=b^{(0)}_i{}^ke_k+\mathcal A_in$ and $\nabla_ie_j=\Gamma^k{}_{ij}e_k+b^{(0)}_{ij}\tau-b^{(1)}_{ij}n$, apply the two derivatives, and contract with $n$. The shape-operator terms remain in (5.4). Normal curvature is not equated to one bulk Riemann component after dropping them.

### 5.2 A completed two-sided geometric correlator

Combining (5.2) with (3.10),

$$
\mathcal C_{LR,ij}^{\mathcal A\mathcal A}
=\left(\frac c{\mathcal C_5}\right)^2 C_{LR,ij}^{\pi\pi}.\tag{5.5}
$$

Use (2.10) and $\beta\hbar/2=2\pi\nu/c^2$. The result is precisely (1.1). At fixed viscosity and $L\to\infty$, $\zeta_c\to1$, giving the local Rindler-fluid limit

$$
\boxed{
\mathcal C_{LR,ij}^{\mathcal A\mathcal A}
\longrightarrow
\frac{4\pi\hbar G_5}{c^3}
\frac{k^2\omega}
{(\omega^2+\nu^2k^4)\sinh(2\pi\nu\omega/c^2)}P_{ij}.
}\tag{5.6}
$$

The factor $\hbar G_5/c^3$ has dimensions of length cubed. With the Fourier measure $d\omega\,d^3k/(2\pi)^4$, (5.6) has the dimensions required for the correlation of connection components of dimension inverse length. The result is a fluctuation kernel, not a new classical stress covariance identified with quantum entanglement by terminology.

Curvature correlations follow by applying the exterior derivative to each argument. In Fourier space, with $\mathcal F_{ij}=i(k_i\mathcal A_j-k_j\mathcal A_i)$, the real-space operation is explicitly $d_xd_y\mathcal C^{\mathcal A\mathcal A}$; the signs in a given Fourier component must retain the opposite momenta on the two legs.

### 5.3 Holonomy

For a normal vector with components $(v^0,v^1)$ in $(\tau,n)$, parallel transport obeys

$$
dv+\mathcal A\,Jv=0,\qquad
J=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Around a closed loop $\gamma\subset S$,

$$
\mathcal H_\gamma=\exp\left(-J\oint_\gamma\mathcal A\right),\qquad
\theta_\gamma=-\oint_\gamma\mathcal A.\tag{5.7}
$$

The sign in the rapidity is fixed by the displayed parallel-transport equation. For a contractible loop, Stokes' theorem gives $\theta_\gamma=-\int_\Sigma\mathcal F$ with the induced orientation. Noncontractible loops retain independent global holonomy information.


### 5.4 A gauge-invariant two-sided loop observable

The component correlator (5.5) uses the specified outward/future normal frame. A closed-loop observable removes the local boost-frame ambiguity. Let $w(k^2)$ be a specified real smooth Fourier filter, compactly supported inside the wavenumber regime in which the hydrodynamic expansion is being used. This filter is part of the observable; modes outside its support are not claimed to have been calculated. Define

$$
J_\gamma^i(\mathbf k)=\oint_\gamma e^{i\mathbf k\cdot\mathbf x}dx^i,
\qquad k_iJ_\gamma^i=\frac1i\oint_\gamma d(e^{i\mathbf k\cdot\mathbf x})=0.
$$

Smear the connection by the filter and define $\theta_{\gamma,w}=-\oint_\gamma\mathcal A_w$. Its two-sided spectral correlation is

$$
\boxed{
C^{\theta_L\theta_R}_{LR}(\omega)=
\int\frac{d^3k}{(2\pi)^3}\,w(k^2)^2
J_{\gamma_L}^i(\mathbf k)J_{\gamma_R}^j(-\mathbf k)
\mathcal C^{\mathcal A_i\mathcal A_j}_{LR}(\omega,\mathbf k).
}\tag{5.8}
$$

Closed-loop integration annihilates $d\lambda$ exactly. For identical coaxial circles of physical radius $R_\gamma$ in the $x^1x^2$ plane at the same position,

$$
J_\gamma(\mathbf k)=2\pi i R_\gamma J_1(R_\gamma k_\perp)
\frac{\widehat z\times\mathbf k_\perp}{k_\perp},
$$

where $J_1$ is the Bessel function. After the azimuthal integral, (5.8) becomes

$$
C^{\theta_L\theta_R}_{LR}(\omega)=R_\gamma^2
\int_0^\infty k_\perp dk_\perp\int_{-\infty}^{\infty}dk_z\,
 w(k_\perp^2+k_z^2)^2J_1(R_\gamma k_\perp)^2
\mathcal K(\omega,\sqrt{k_\perp^2+k_z^2}),\tag{5.9}
$$

where $\mathcal K$ is the scalar multiplying $P_{ij}$ in (1.1). Thus the calculated two-sided observable can be expressed as a correlation of frame-transport rapidities around physical loops, not just gauge-dependent connection components. An unsmeared zero-thickness loop would require ultraviolet information not supplied by the hydrodynamic kernel.

## 6. The nonlinear NS input changes the connection through the full drive

The preterminal physical equation is

$$
\partial_tU+(U\cdot\nabla)U-\nu\Delta U+\nabla P=f,
\qquad \nabla\cdot U=0.\tag{6.1}
$$

Take the leading boundary metric source

$$
\gamma=-(c^2+2\Phi)dt^2+2a_i\,dt\,dx^i+\delta_{ij}dx^idx^j.
$$

Its nonrelativistic forcing relation is

$$
f_i=-\partial_ta_i-\partial_i\Phi
+U^j(\partial_ia_j-\partial_ja_i).\tag{6.2}
$$

This source relation is the same one used in the preserved calculation, derived from the nonrelativistic fluid limit of metric perturbations (Bhattacharyya et al., 2009). It is an equation at that constitutive order; it is not an all-order bulk reconstruction theorem.

Choose $\Phi=U\cdot a$. Then

$$
(\partial_t+\mathcal L_U)a=-f^\flat,
\qquad
 a(t)=(X_t^{-1})^*\left[a(0)-\int_0^tX_s^*f^\flat(s)ds\right],\tag{6.3}
$$

where $\dot X_t=U(X_t,t)$. This is an exact solution of the source-identification equation for every smooth preterminal input.

Let $\alpha=U^\flat+a$. Adding (6.1) and (6.3) gives

$$
(\partial_t+\mathcal L_U)\alpha
=-d\left(P-\frac12|U|^2\right)+\nu\Delta U^\flat.\tag{6.4}
$$

The pressure and the $|U|^2/2$ term are retained before taking a closed-loop integral. For a material loop $\gamma_t=X_t\gamma_0$,

$$
\frac d{dt}\oint_{\gamma_t}\alpha
=\nu\oint_{\gamma_t}\Delta U_i\,dx^i.\tag{6.5}
$$

Using (3.8), (5.2), and (2.10), the NS coefficient of the connection and its rapidity are

$$
\mathcal A^{\mathrm{NS}}=-\frac{\zeta_c}{2\nu}\alpha,
\qquad
\theta^{\mathrm{NS}}_{\gamma_t}
=\frac{\zeta_c}{2\nu}\oint_{\gamma_t}\alpha.
$$

For a fixed background member (so $\zeta_c$ is time-independent),

$$
\boxed{
\frac d{dt}\theta^{\mathrm{NS}}_{\gamma_t}
=\frac{\zeta_c}{2}\oint_{\gamma_t}\Delta U_i\,dx^i.
}\tag{6.6}
$$

The drive has not been ignored: it has cancelled through its exact reconstruction. Equation (6.6) is an equality for the explicitly defined NS connection coefficient. An actual higher-order bulk connection additionally has the higher-order constitutive terms.

Let $\omega=\nabla\times U$, $B=\nabla\times(U+a)$, and $b_c=-\zeta_c B/(2\nu)$, the Hodge-dual vector of $d\mathcal A^{\mathrm{NS}}$. Exterior differentiation of (6.4) gives

$$
\boxed{
\mathscr D_Ub_c:=(\partial_t+U\cdot\nabla)b_c-(b_c\cdot\nabla)U
=-\frac{\zeta_c}{2}\Delta\omega.
}\tag{6.7}
$$

For rest data, $a(0)=0$, and $J_t=DX_t$,

$$
b_c(t,X_t(a_0))
=-\frac{\zeta_c}{2}J_t(a_0)
\int_0^tJ_s(a_0)^{-1}\Delta\omega(s,X_s(a_0))ds.\tag{6.8}
$$

Mass preservation is $\det J_t=1$. It places no uniform bound on the separate factors $J_t$ and $J_t^{-1}$ in (6.8).

## 7. A new lower bound for the curvature-transport rate

This section is an analytic deduction from the full velocity. It does not require evaluating an unverified axis jet.

For a nonzero compactly supported smooth divergence-free $V$ on $\mathbb R^3$, put

$$
H=\|V\|_\infty,\quad E=\|V\|_2,\quad
W=\|\nabla\times V\|_\infty,\quad
D=\|\Delta\nabla\times V\|_\infty.
$$

All vector norms are Euclidean. For $G_s(x)=(4\pi s)^{-3/2}e^{-|x|^2/(4s)}$,

$$
\|G_s\|_2=(8\pi s)^{-3/4},\qquad
\|\nabla G_s\|_1=\frac2{\sqrt{\pi s}}.
$$

Since $\nabla\times\nabla\times V=-\Delta V$,

$$
V=G_s*V+\int_0^s\nabla\times(G_b*\nabla\times V)db,
$$

and therefore

$$
H\le(8\pi s)^{-3/4}E+\frac4{\sqrt\pi}\sqrt{s}\,W.
$$

Choosing the positive auxiliary smoothing time

$$
s=\left[2(8\pi)^{-3/4}E/H\right]^{4/3}
$$

proves

$$
W\ge\frac\pi{2^{13/6}}H^{5/3}E^{-2/3}.\tag{7.1}
$$

This is not a rescaling of the physical solution: $s$ is the auxiliary parameter in an inequality valid for every $s>0$.

For each unit vector $e$, the kernel for $e\cdot\nabla\times(G_s*V)$ has squared $L^2$ norm $\|\nabla G_s\times e\|_2^2=(2s)^{-1}(8\pi s)^{-3/2}$. Also,

$$
\nabla\times V-G_s*\nabla\times V
=-\int_0^sG_b*\Delta\nabla\times V\,db.
$$

Thus

$$
W\le C_0s^{-5/4}E+sD,
\qquad C_0=2^{-1/2}(8\pi)^{-3/4}.
$$

Take $s=(2C_0E/W)^{4/5}$. This proves

$$
D\ge 2^{2/5}\pi^{3/5}E^{-4/5}W^{9/5}
\ge\frac{\pi^{12/5}}{2^{7/2}}H^3E^{-2}.\tag{7.2}
$$

Apply (7.2) to the actual preterminal $U(t)$ and use the equality (6.7):

$$
\boxed{
\|\mathscr D_Ub_c(t)\|_\infty
\ge\zeta_c\frac{\pi^{12/5}}{2^{9/2}}
\frac{\|U(t)\|_\infty^3}{\|U(t)\|_2^2}.
}\tag{7.3}
$$

If $U(t)=0$, the curvature-rate identity remains valid; the quotient form is used only when its denominator is nonzero. With the retained uniform energy bound $\|U(t)\|_2\le E_*$, one can replace the denominator by $E_*^2$ to obtain a weaker uniform estimate.

The constructive-path lower bound already recorded in the previous package is $\|U(T_0(1-\tau))\|_\infty\ge A_*\tau^{-1/2-h}$ for every sufficiently small $\tau>0$, with $A_*>0$. Inserting that retained input yields

$$
\|\mathscr D_Ub_c(T_0(1-\tau))\|_\infty
\ge\zeta_c\frac{\pi^{12/5}A_*^3}{2^{9/2}E_*^2}
\tau^{-3/2-3h}.\tag{7.4}
$$

Equation (7.3) is independently derived here for every input in the stated class. Equation (7.4) additionally uses the source-dependent amplitude estimate from the earlier edition; this session does not independently re-verify the upstream construction proving that input.

This is a bound on the *materially transported curvature rate*, not a lower bound on $b_c$ itself. Transport, stretching, and time cancellation are explicit in (6.8). A diverging right-hand side in that evolution does not justify suppressing those terms or claiming a freely falling curvature singularity of an unconstructed exact metric.

There is also a definite non-flatness result. If $b_c$ vanished identically on a whole open time interval, (6.7) would imply $\Delta\omega=0$ there. Compact support implies $\omega=0$ by integration by parts; $\nabla\cdot U=0$ then gives $\Delta U=0$, and compact support gives $U=0$. Therefore a nontrivial compactly supported NS flow cannot maintain identically flat source-coupled connection curvature throughout an interval. This does not forbid a special individual time at which the curvature coefficient vanishes.

## 8. The exact operator map across an entangled state

The left–right entanglement data must also be carried when the metric is driven. Let $\mathcal U_L,\mathcal U_R$ be the unitary evolutions generated by the selected complete regulated source Hamiltonians $H_L[\gamma_L]$, $H_R[\gamma_R]$. Define the state coefficient matrix

$$
C(t)=\mathcal U_L(t)\sqrt{\rho_\beta}\,\mathcal U_R(t)^{\mathsf T},
\qquad |\Psi_C\rangle=\sum_{ij}C_{ij}|i\rangle_L|j\rangle_R.\tag{8.1}
$$

Then

$$
i\hbar\dot C=H_LC+CH_R^{\mathsf T},\quad
\rho_L=CC^\dagger=\mathcal U_L\rho_\beta\mathcal U_L^\dagger,
\quad
\rho_R=(C^\dagger C)^{\mathsf T}=\mathcal U_R\rho_\beta\mathcal U_R^\dagger.\tag{8.2}
$$

The factor $Z^{-1/2}$ in (3.1) makes the state have unit norm. It is a required state normalization displayed explicitly, not a rescaling of the input physical fields.

For faithful $C$, define the linear anti-homomorphism

$$
\mathfrak m_C:\mathcal B(\mathcal H_R)\longrightarrow
\mathcal B(\mathcal H_L),\qquad
\mathfrak m_C(O)=CO^{\mathsf T}C^{-1}.\tag{8.3}
$$

It obeys

$$
(\mathfrak m_C(O)\otimes I)|\Psi_C\rangle=(I\otimes O)|\Psi_C\rangle,
\quad
\mathfrak m_C(O_1O_2)=\mathfrak m_C(O_2)\mathfrak m_C(O_1).\tag{8.4}
$$

It is not generally a star-preserving homomorphism. Its precise adjoint identity is

$$
\mathfrak m_C(O)^\dagger=\rho_L^{-1}\mathfrak m_C(O^\dagger)\rho_L.\tag{8.5}
$$

The inverse in the continuum can be unbounded; (8.3) is asserted as a bounded matrix map at the regulator, and otherwise only on a common specified domain.

For a fixed right operator, direct differentiation proves

$$
\boxed{
\partial_t\mathfrak m_C(O)
=-\frac i\hbar[H_L,\mathfrak m_C(O)]
+\frac i\hbar\mathfrak m_C([H_R,O]).
}\tag{8.6}
$$

Thus the map across the two sides evolves even though the Schmidt coefficients and total left–right entropy are unchanged. The correlation is exactly

$$
\langle O_L\otimes O_R\rangle_C
=\operatorname{Tr}(C^\dagger O_LCO_R^{\mathsf T}).\tag{8.7}
$$

This distinguishes evolution of the entanglement *pattern* from changing only a scalar entropy. It supplies a concrete object for interior mirror reconstruction in a chosen semiclassical code subspace, without claiming that a classical velocity determines a microscopic Hamiltonian (Czech et al., 2019, Section 2.1; Maldacena & Susskind, 2013).

For the source in (6.2), the first variation of a covariant Hamiltonian around the flat cutoff includes

$$
\delta H=\int d^3x\left[\frac{\Phi}{c^2}\widehat\varepsilon-a_i\widehat\pi_i\right].\tag{8.8}
$$

The full $H[\gamma]$, including nonlinear source terms, counterterms, and any curvature couplings of the specified quantum theory, is what appears in (8.1)–(8.6). Equation (8.8) is not substituted for it at finite source amplitude. The exact source dependence of $\mathfrak m_C$ is consequently well-defined once that theory and preparation are fixed. It is not a claim to have solved its full driven many-body dynamics for the singular NS force.

For example, for a first-order transverse drive on the right, Dyson expansion gives the explicit functional derivative

$$
\left.\frac{\delta\langle O_L O_R(t)\rangle}{\delta a_i(s,x)}\right|_{a=0}
=\frac i\hbar\Theta(t-s)
\langle O_L[O_R(t),\widehat\pi_i(s,x)]\rangle_{\Omega_\beta}.\tag{8.9}
$$

This three-point object, rather than the equilibrium two-point function alone, determines the first change of a general two-sided correlator under a finite-time NS-derived preparation. Higher source orders require the corresponding nested commutators and contact terms.

## 9. Modular transport: an explicit map, and its geometric domain

For a regulated family of reduced states $\rho_A(\lambda)$, put $K_A(\lambda)=-\log\rho_A(\lambda)$. Let $P_0$ project an operator onto the blocks commuting with $K_A$; degenerate eigenspaces are kept as whole blocks. Modular parallel transport is generated by the anti-Hermitian operator $V_a$ satisfying

$$
\partial_aK_A-P_0(\partial_aK_A)=[V_a,K_A],\qquad P_0(V_a)=0.\tag{9.1}
$$

In an eigenbasis $K_A|m\rangle=\kappa_m|m\rangle$,

$$
(V_a)_{mn}=\frac{(\partial_aK_A)_{mn}}{\kappa_n-\kappa_m}
\quad(\kappa_m\ne\kappa_n),\qquad
(V_a)_{mn}=0\quad(\kappa_m=\kappa_n).\tag{9.2}
$$

These formulas explicitly transport changes of state/subregion into changes of modular frames. They are not an assertion that the NS velocity is a modular Hamiltonian.

Define the derivative on transported vectors as $D_a=\partial_a-V_a$, so its parallel equation is $\partial_a\psi=V_a\psi$. The finite-regulator curvature then has the zero-mode component

$$
\mathscr R_{ab}=P_0\big(-\partial_aV_b+\partial_bV_a+[V_a,V_b]\big).\tag{9.3}
$$

The precise gauge representative and its zero-mode bundle are specified by (9.1). The bulk holographic comparison uses the code-subspace modular relation

$$
K_A^{\mathrm{boundary}}
=\frac{c^3}{4\hbar G_5}\widehat{\operatorname{Area}}(\mathcal X_A)
+K_a^{\mathrm{bulk}}+\text{the specified semiclassical corrections}.\tag{9.4}
$$

This is a relation for a selected boundary region, its extremal surface, and its entanglement wedge (Jafferis et al., 2016), not for every timelike cutoff slice automatically.

Czech et al. (2019) construct the geometric comparison using a family of HRRT surfaces $\mathcal X_A(\lambda)$, including both normal boosts and diffeomorphisms along the surface. Their source equations (3.9)–(3.18) determine the extremal-surface displacement and the corresponding frame connection. Their direct Riemann-curvature interpretation retains the scale restriction $R\gg K^2,\nabla K$ in source equation (3.19). Near a concentrating geometry this restriction must be tested rather than inferred from the word "horizon."

For a boost generator $Q_B$ with units of action, choose the unitary representation

$$
U_B(\theta)=e^{-i\theta Q_B/\hbar},\qquad K_B=2\pi Q_B/\hbar.\tag{9.5}
$$

The normal holonomy in (5.7) maps to

$$
U_B(\theta_\gamma)
=\exp\left[\frac{iK_B}{2\pi}\oint_\gamma\mathcal A\right].\tag{9.6}
$$

Using the NS coefficient gives the explicit normal-sector expression

$$
\boxed{
U^{\mathrm{NS}}_\gamma
=\exp\left[-\frac{i\zeta_cK_B}{4\pi\nu}
\oint_\gamma(U_i+a_i)dx^i\right].
}\tag{9.7}
$$

Equation (9.7) is the unitary representation of the defined normal-frame boost coefficient. Its interpretation as a modular Berry holonomy requires an actual family of entanglement wedges and the holographic matching just described. A spatial loop on one cutoff and a loop in the space of boundary subregions have different base spaces. Their map requires the family $\mathcal X_A(\lambda)$ and its frame transport; it has not been fabricated by calling both loops $\gamma$.

The new result is therefore not a universal equality between (9.7) and every quantum modular holonomy. The completed quantities are the two-sided normal-connection kernel (1.1), the exact classical coefficient transport (6.6)–(6.8), and its lower bound (7.3). Equations (9.1)–(9.7) identify and calculate the exact operator and geometric components of the further comparison.

## 10. What the singular NS result changes

The background ER geometry and its thermofield state already provide a calculable equality of two-sided response functions. The new NS input is a nonlinear concentration trajectory for the same leading fluid variables. Under the force reconstruction, it specifies $\alpha=U^\flat+a$, normal holonomies, and the curvature-transport functional (6.8). Its velocity growth forces the lower bound (7.3), and the retained constructive-path input strengthens this to (7.4).

This supplies a physically definite investigation: increasingly singular transport of the relative normal frames of a horizon-fluid geometry, together with a quantum two-sided observable that measures fluctuations of those frames. It is not a particle acquiring infinite rest mass. The material-volume identity and finite dissipation statements of the preserved package continue to hold for the NS input.

Neither a divergent fluid gradient nor the coefficient estimate proves that the full Einstein solution has a divergent invariant or that a global bridge has been created. A source-controlled, convergent two-sided bulk construction for the terminal NS flow has not been produced. Nor has the universal proposition that every entangled pair has a gravitational bridge been proved. Those limits do not erase the explicit response calculation: they locate its actual regime.

The equilibrium spectral formula must not be evaluated at the terminal NS wavelength and then advertised as an all-scale prediction. It is valid for weak fluctuations around the specified thermal background within the hydrodynamic regime. The exact force/source and material-transport formulas retain their preterminal classical meaning outside that approximation, but their equality to a completed quantum-gravitational solution has not been established.

The supplied code evaluates (1.1), (2.9), and the cutoff quantities with physical parameters. It also integrates (6.8) from user-supplied full-field functions and reports numerical volume drift. No synthetic field is presented as the upstream construction. Exact algebraic checks and numerical implementation checks are identified separately. No Lean kernel verification or upstream comparator replay was performed in this continuation.

## References

Bhattacharyya, S., Minwalla, S., & Wadia, S. R. (2009). The incompressible non-relativistic Navier–Stokes equation from gravity. *Journal of High Energy Physics, 2009*(08), 059. doi:10.1088/1126-6708/2009/08/059. arXiv:0810.1545.

Bredberg, I., Keeler, C., Lysov, V., & Strominger, A. (2012). From Navier–Stokes to Einstein. *Journal of High Energy Physics, 2012*(07), 146. doi:10.1007/JHEP07(2012)146. arXiv:1101.2451.

Compère, G., McFadden, P., Skenderis, K., & Taylor, M. (2011). The holographic fluid dual to vacuum Einstein gravity. *Journal of High Energy Physics, 2011*(07), 050. doi:10.1007/JHEP07(2011)050. arXiv:1103.3022.

Czech, B., de Boer, J., Ge, D., & Lamprou, L. (2019). A modular sewing kit for entanglement wedges. *Journal of High Energy Physics, 2019*(11), 094. doi:10.1007/JHEP11(2019)094. arXiv:1903.04493.

Glorioso, P., Crossley, M., & Liu, H. (2018). *A prescription for holographic Schwinger–Keldysh contour in non-equilibrium systems* [Preprint]. arXiv:1812.08785.

Herzog, C. P., & Son, D. T. (2003). Schwinger–Keldysh propagators from AdS/CFT correspondence. *Journal of High Energy Physics, 2003*(03), 046. doi:10.1088/1126-6708/2003/03/046. arXiv:hep-th/0212072.

Iqbal, N., & Liu, H. (2009). Universality of the hydrodynamic limit in AdS/CFT and the membrane paradigm. *Physical Review D, 79*(2), 025023. doi:10.1103/PhysRevD.79.025023. arXiv:0809.3808.

Jafferis, D. L., Lewkowycz, A., Maldacena, J., & Suh, S. J. (2016). Relative entropy equals bulk relative entropy. *Journal of High Energy Physics, 2016*(06), 004. doi:10.1007/JHEP06(2016)004. arXiv:1512.06431.

Maldacena, J. (2003). Eternal black holes in anti-de Sitter. *Journal of High Energy Physics, 2003*(04), 021. doi:10.1088/1126-6708/2003/04/021. arXiv:hep-th/0106112.

Maldacena, J., & Susskind, L. (2013). Cool horizons for entangled black holes. *Fortschritte der Physik, 61*(9), 781–811. doi:10.1002/prop.201300020. arXiv:1306.0533.

Son, D. T., & Starinets, A. O. (2002). Minkowski-space correlators in AdS/CFT correspondence: Recipe and applications. *Journal of High Energy Physics, 2002*(09), 042. doi:10.1088/1126-6708/2002/09/042. arXiv:hep-th/0205051.
