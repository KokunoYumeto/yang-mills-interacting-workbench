*GitHub reading copy; only mathematical delimiters have changed. [Unchanged source](../archive/vacuum-hydrodynamics/RESEARCH_NOTE.md).*

# Vacuum hydrodynamics, Navier–Stokes concentration, and ER = EPR

## 1. The geometric question

The proposed physical connection has a concrete intermediate object: a **driven, concentrating horizon-fluid configuration whose boundary momentum, vorticity, and shear are encoded in extrinsic curvature and bulk curvature**. The relevant comparison is between a fluid's concentrating momentum transport and a gravitational geometry's concentrating tidal and horizon data. An infinite material speed is not the observable that should be transported into a relativistic spacetime.

The Navier–Stokes input is the released statement of OpenAI (2026b, Theorem 1.1): a three-dimensional incompressible flow, initially at rest, with positive viscosity, compactly supported smooth forcing, uniformly bounded kinetic energy, and an unbounded velocity norm near its terminal time. The present analysis uses that stated construction; its existence proof is not re-established here. The manuscript's concentration scales and the earlier workbench's axis observable are treated separately below.

Three different mathematical operations organize the gravitational investigation. A boundary restriction takes a spacetime metric to its induced metric and extrinsic curvature. A constitutive expansion reads fluid variables from the Brown–York stress. A perturbative reconstruction goes in the opposite direction, building bulk metric coefficients from suitable fluid and boundary-source data. Only the third operation is an inverse construction, and it operates order by order, with the stated boundary and horizon conditions. Bredberg et al. (2012, §5) provide the leading vacuum construction; Compère et al. (2011, §§4–7) give its higher-order extension.

The quantum operation needed for ER = EPR enters later. It takes a specified bipartite quantum state, not merely a stress tensor, into a two-sided holographic description. Maldacena (2003) and Maldacena and Susskind (2013) supply the relevant two-sided black-hole setting. This note computes the classical transport first, then identifies exactly which quantum information it retains and which information it has discarded.

## 2. Dimensions, coordinates, and constants

Write the physical fluid equation as

$$
\partial_t U_i+U_j\partial_jU_i+\partial_i p_{\mathrm{kin}}-\nu\Delta U_i=f_i,
\qquad \partial_iU_i=0.
\tag{1}
$$

Here $t$ is physical time, $U_i$ has units of speed, $p_{\mathrm{kin}}$ is pressure divided by mass density, and $f_i$ is force per unit mass. Introduce the explicitly defined coordinates and fields

$$
x^0=ct,\qquad v_i=U_i/c,\qquad \Pi=p_{\mathrm{kin}}/c^2,
\qquad \ell=\nu/c,\qquad F_i=f_i/c^2.
\tag{2}
$$

No physical parameter has been assigned the value one. Equation (1) becomes

$$
\partial_0v_i+v_j\partial_jv_i+\partial_i\Pi-\ell\Delta v_i=F_i.
\tag{3}
$$

There are three spatial coordinates $x^i$, four boundary spacetime coordinates $x^a=(x^0,x^i)$, and five bulk coordinates $X^A=(x^0,R,x^i)$. The extra gravitational coordinate is $R$. Thus this application of the vacuum-fluid construction has a five-dimensional bulk. A four-dimensional bulk would instead have two spatial fluid coordinates.

Use signature $(-,+,+,+,+)$ and define curvature by

$$
R^A{}_{BCD}=\partial_C\Gamma^A{}_{DB}-\partial_D\Gamma^A{}_{CB}
+\Gamma^A{}_{CE}\Gamma^E{}_{DB}-\Gamma^A{}_{DE}\Gamma^E{}_{CB}.
\tag{4}
$$

The outward unit spacelike normal is directed toward increasing $R$. Extrinsic curvature is $K_{ab}=\gamma_a{}^A\gamma_b{}^B\nabla_A n_B$. These definitions fix the signs in every curvature and boundary-stress calculation below.

## 3. The exact Rindler seed and its thermal interface

Consider

$$
ds_0^2=-\frac{R}{\ell}(dx^0)^2+2\,dx^0dR+\delta_{ij}dx^idx^j,
\qquad 0<R\leq\ell.
\tag{5}
$$

The cutoff embedding is $\iota_\ell(x^a)=(x^0,\ell,x^i)$, and its pullback is exactly

$$
\iota_\ell^*g_0=-(dx^0)^2+\delta_{ij}dx^idx^j.
\tag{6}
$$

The coordinate relation to the variables used in Bredberg et al. is

$$
r=\ell R,\qquad r_c=\ell^2,\qquad \tau_{\mathrm B}=x^0/\ell,
\qquad v_i^{\mathrm B}=\ell v_i,\qquad P^{\mathrm B}=\ell^2\Pi.
\tag{7}
$$

In particular their coordinate viscosity $r_c$ becomes the physical viscosity $c\ell=\nu$ under the displayed map. This is a coordinate and unit conversion, not an identification of a coordinate radius with a physical viscosity without conversion factors.

Define

$$
s=x^0-\ell\log(R/\ell),\qquad \rho=2\sqrt{\ell R}.
$$

Then (5) becomes

$$
ds_0^2=-\frac{\rho^2}{4\ell^2}\,ds^2+d\rho^2+\delta_{ij}dx^idx^j.
\tag{8}
$$

The map

$$
X^0=\rho\sinh\!\left(\frac{s}{2\ell}\right),\qquad
X^1=\rho\cosh\!\left(\frac{s}{2\ell}\right)
\tag{9}
$$

pulls the Minkowski metric back to (8). Consequently the seed is Riemann-flat. Its cutoff observers have $\rho=2\ell$, proper time $s/c$, and proper acceleration

$$
a_\ell=\frac{c^2}{2\ell}.
\tag{10}
$$

The accelerated-detector temperature is therefore

$$
T_\ell=\frac{\hbar a_\ell}{2\pi k_Bc}
=\frac{\hbar c}{4\pi k_B\ell}
=\frac{\hbar c^2}{4\pi k_B\nu}.
\tag{11}
$$

Unruh (1976) supplies the detector interpretation; equations (8)–(10) identify the specific worldlines to which it applies. The final equality in (11) is a property of this gravity-fluid model. It is not an assertion that an arbitrary laboratory liquid with viscosity $\nu$ is at that temperature.

This is the direct interface with the thermal-horizon branch: a specified wedge, specified accelerated worldlines, and their temperature. A particle's ability to entangle does not by itself select these worldlines or this wedge. The required geometric selection has been given explicitly rather than inferred from the word “observer.”

## 4. Brown–York stress and the Einstein constraint

Retain the five-dimensional gravitational constant $G_5$ and put

$$
\mathcal C_5=\frac{c^4}{8\pi G_5},\qquad
\mathsf T_{ab}=\mathcal C_5(K\gamma_{ab}-K_{ab}).
\tag{12}
$$

The boundary tensor has physical energy-density units in the $x^0=ct$ coordinates. Equation (12) is the Brown–York prescription with the normal and extrinsic-curvature definition fixed above; the corresponding prescription is used in Compère et al. (2011, eq. 2.2).

For the exact seed,

$$
K_{00}=-\frac1{2\ell},\qquad K_{ij}=0,\qquad K=\frac1{2\ell},
$$

and hence

$$
\mathsf T_{00}=0,\qquad
\mathsf T_{ij}=p_0\delta_{ij},\qquad
p_0=\frac{c^4}{16\pi G_5\ell}.
\tag{13}
$$

The nonzero boundary pressure is compatible with zero bulk matter stress and zero bulk curvature. It records the embedding of the accelerated cutoff. This already shows why boundary fluid variables must be transported through (12), rather than read as a literal material filling the vacuum.

The leading non-equilibrium stress in the flat induced metric is

$$
\begin{aligned}
\mathsf T_{00}&=p_0v^2+\text{higher hydrodynamic orders},\\
\mathsf T_{0i}&=-p_0v_i+\text{higher hydrodynamic orders},\\
\mathsf T_{ij}&=p_0\left[\delta_{ij}+v_iv_j+\Pi\delta_{ij}
-\ell(\partial_iv_j+\partial_jv_i)\right]
+\text{higher hydrodynamic orders}.
\end{aligned}
\tag{14}
$$

Taking its divergence and retaining the orders shown gives

$$
\partial^a\mathsf T_{ai}=p_0\left(
\partial_0v_i+v_j\partial_jv_i+\partial_i\Pi-\ell\Delta v_i
\right),
\tag{15}
$$

using leading incompressibility. Thus the signs of acceleration, pressure, advection, and viscosity are fixed by one explicit tensor calculation.

The exact momentum constraint is

$$
D^a\mathsf T_{ab}=-\mathcal C_5R_{AB}n^A\gamma^B{}_b.
\tag{16}
$$

For a Ricci-flat bulk, its right-hand side vanishes. For this Ricci-flat bulk, the exact scalar constraint is

$$
\mathcal R[\gamma]=K^2-K_{ab}K^{ab}.
\tag{17}
$$

For three spatial boundary dimensions this becomes

$$
3\,\mathsf T_{ab}\mathsf T^{ab}
-(\mathsf T^a{}_a)^2
=-3\mathcal C_5^2\mathcal R[\gamma].
\tag{18}
$$

These equations exhibit the typed map

$$
(g,\iota_\ell)\longmapsto(\gamma,K)
\longmapsto\mathsf T
\longmapsto(D^a\mathsf T_{ab},\mathcal R[\gamma]-K^2+K_{ab}K^{ab}).
\tag{19}
$$

It is an exact geometric map. The fluid interpretation of $\mathsf T$ and the inverse construction of $g$ introduce the hydrodynamic expansion.

## 5. A concrete bulk metric and its order of validity

Transforming the displayed metric of Bredberg et al. (2012, eq. 14) with (7) gives

$$
\begin{aligned}
ds^2={}&-\frac R\ell(dx^0)^2+2dx^0dR+dx_idx_i\\
&-2\left(1-\frac R\ell\right)v_i\,dx^idx^0
-2v_i\,dx^idR\\
&+\left(1-\frac R\ell\right)
\left[(v^2+2\Pi)(dx^0)^2+v_iv_jdx^idx^j\right]
+(v^2+2\Pi)dx^0dR\\
&-(R^2-\ell^2)\Delta v_i\,dx^idx^0
+\text{further metric coefficients}.
\end{aligned}
\tag{20}
$$

The ordering is $v=O(\varepsilon)$, $\Pi=O(\varepsilon^2)$, $\partial_i=O(\varepsilon)$, $\partial_0=O(\varepsilon^2)$. Equation (20) is a finite-order reconstruction representative. The phrase “further metric coefficients” does not mean those coefficients vanish. Different choices of fluid frame already change cubic coefficients while preserving the leading equations; Compère et al. give the corresponding completion in their chosen frame.

A useful precise type for a finite-order reconstruction is

$$
\mathfrak G_N:
\{\text{fluid and boundary-source jets satisfying the constraints to order }N\}
\longrightarrow
\{\text{Lorentzian metric jets modulo }O(\varepsilon^{N+1})\}.
\tag{21}
$$

The Einstein residual vanishes to the prescribed order. The existence of every coefficient does not supply a convergent sum or an error bound uniform at the terminal singularity. This distinction is about the codomain of (21), not a claim that fluid motion and spacetime geometry lack a relationship.

## 6. Realizing the prescribed force by boundary geometry

For the released forced solution, keeping both a flat boundary metric and a Ricci-flat bulk while inserting a nonzero right-hand side in (15) would violate (16). A geometric drive must be retained. Boundary-metric forcing is developed explicitly by Bhattacharyya, Minwalla, and Wadia (2009, §2.2 and §4); Bredberg et al. (2012, §5.2) also exhibit a vacuum boundary-stirring construction.

Take the boundary metric

$$
\gamma=-(c^2+2\Phi)dt^2+2A_i\,dt\,dx^i+\delta_{ij}dx^idx^j.
\tag{22}
$$

Here $A_i$ has units of speed and $\Phi$ of speed squared. It is Lorentzian when $c^2+2\Phi+|A|^2>0$. In the weak, slowly varying source expansion, the resulting physical force is

$$
f_i=-\partial_tA_i-\partial_i\Phi
+U^j(\partial_iA_j-\partial_jA_i).
\tag{23}
$$

The last term must be kept. A vector potential chosen by $A_i=-\int f_i\,dt$ generally leaves this extra force uncancelled.

There is nevertheless an explicit preterminal reconstruction. Treat $A=A_i dx^i$ and $f^\flat=f_i dx^i$ as spatial one-forms and choose

$$
\Phi=U^iA_i.
\tag{24}
$$

Then (23) is exactly the one-form transport equation

$$
(\partial_t+\mathcal L_U)A=-f^\flat,
\qquad
(\mathcal L_UA)_i=U^j\partial_jA_i+A_j\partial_iU^j.
\tag{25}
$$

For the material flow $X_t$ of the smooth preterminal velocity,

$$
\boxed{
A(t)=(X_t^{-1})^*\left[A(0)-\int_0^tX_s^*f^\flat(s)\,ds\right],
\qquad \Phi(t)=U(t)\cdot A(t).
}
\tag{26}
$$

The proof is differentiation of $X_t^*A(t)$; no force term is discarded. On every closed interval strictly before the terminal time, smooth compactly supported fluid data make this a well-defined smooth construction. The metric conditions remain explicit: with this choice of $\Phi$,

$$
c^2+2\Phi+|A|^2=c^2-|U|^2+|U+A|^2>0
$$

throughout the small-velocity regime $|U|<c$. Smoothness of the formula alone does not enforce small source amplitude or small gradients. Equations (25)–(26) solve the source-identification problem exactly for the leading hydrodynamic force map (23). They do not turn that leading map into an exact all-gradient Einstein solution.

The derivatives of $X_t$ and $X_t^{-1}$ enter (26). Consequently a uniformly smooth prescribed $f$ alone does not establish a uniformly smooth boundary metric through blowup. Terminal source regularity has become a definite calculation involving the material deformation, rather than an unspecified analogy about applying a force to spacetime.

## 7. The curvature component that receives vorticity

With the curvature definition (4), the exact Codazzi identity reads

$$
R_{nabc}=D_cK_{ab}-D_bK_{ac}.
\tag{27}
$$

For a flat induced metric, inversion of (12) gives $K_{0i}=v_i/(2\ell)$ at leading order. Therefore

$$
\boxed{
R_{n0ij}=-\frac{\partial_iv_j-\partial_jv_i}{2\ell}
+\text{higher hydrodynamic orders}.
}
\tag{28}
$$

For the physical three-dimensional vorticity $\omega_U=\nabla\times U$,

$$
R_{n012}=-\frac{(\omega_U)_3}{2\nu}
+\text{higher hydrodynamic orders}.
\tag{29}
$$

In a Ricci-flat solution this component is also a Weyl-curvature component. A direct linearized Riemann calculation for $v=(-\Omega y,\Omega x,0)$ gives $R_{n012}=-\Omega/\ell$, independently checking the orientation and factor of two in (28).

### The additional term required by forcing

For the boundary metric (22), the fluid covector has leading spatial part $(U_i+A_i)/c$. The ideal-fluid contribution to extrinsic curvature is

$$
K_{ab}=-\frac{p_0}{\mathcal C_5}u_au_b
+\text{derivative and higher-amplitude terms}.
$$

Repeating the antisymmetric derivative in (27) gives

$$
\boxed{
R_{n012}=-\frac{[\nabla\times(U+A)]_3}{2\nu}
+\text{higher hydrodynamic and source orders}.
}
\tag{30}
$$

The source potential affects the curvature observable itself, not only the momentum equation. Equation (30) is the appropriate leading diagnostic for the driven configuration. Treating (29) as the full forced answer would silently erase part of the metric.

There is also an exact evolution identity for the quantity appearing in (30). Let $U^\flat=U_i dx^i$ in the Euclidean spatial metric. Equations (1) and (25) imply

$$
(\partial_t+\mathcal L_U)(U^\flat+A)
=-d\left(p_{\mathrm{kin}}-\frac{|U|^2}{2}\right)+\nu\Delta U^\flat,
\tag{31}
$$

and hence

$$
\boxed{
(\partial_t+\mathcal L_U)d(U^\flat+A)=\nu\,d\Delta U^\flat.
}
\tag{32}
$$

This follows because exterior differentiation commutes with the Lie derivative. The force has cancelled between fluid acceleration and geometric drive, while ordinary viscous diffusion remains. The canonically combined vorticity is thus a particularly useful variable for carrying the actual forcing construction into geometry.

For the released rest initial condition, choose the unperturbed geometric source $A(0)=0$. Then $d(U^\flat+A)(0)=0$, and integrating (32) gives the exact two-form identity

$$
\boxed{
d(U^\flat+A)(t)=\nu(X_t^{-1})^*
\int_0^tX_s^*\bigl(d\Delta U^\flat(s)\bigr)\,ds.
}
\tag{32a}
$$

Thus this source choice makes the leading curvature channel a transported, time-integrated viscous-vorticity source. In vector notation, writing $B=\nabla\times(U+A)$ and using incompressibility, the same equation is

$$
(\partial_t+U\cdot\nabla)B-(B\cdot\nabla)U=\nu\Delta\omega_U.
\tag{32b}
$$

In coordinates $a$ labeling the initial fluid particles, incompressibility gives $\det DX_t(a)=1$. Variation of constants for (32b) then gives

$$
\boxed{
B(t,X_t(a))=DX_t(a)\left[
B(0,a)+\nu\int_0^t[DX_s(a)]^{-1}
\Delta\omega_U(s,X_s(a))\,ds\right].
}
\tag{32c}
$$

Indeed $\partial_tDX_t=(DU)(t,X_t)DX_t$; differentiation of $[DX_t]^{-1}B(t,X_t)$ leaves exactly the integrand in (32c). This is a coordinate-level prescription for the leading curvature input, with no assumption that the strain, the viscous source, or its transported integral is small.

Changing $A(0)$ adds the homogeneous transported two-form $(X_t^{-1})^*dA(0)$. Consequently the fluid and force alone do not select a unique boundary-source history; choosing its initial value is real geometric input. Equations (32a)–(32b) retain that choice instead of silently fixing a gravitational preparation.

### Using the retained axis observable

The supplied workbench records an axis angular-velocity observable proportional to $(1-t)^{-1-h}$, with its source normalization $C^{-1}$ (conversation export, lines 2500–2522). Denote its physical-unit version by $\Omega_{\mathrm{ax}}(t)$. For a smooth axisymmetric velocity,

$$
U_\theta(r,0,t)=\Omega_{\mathrm{ax}}(t)\,r+O(r^3)
\quad\Longrightarrow\quad
(\omega_U)_z(0,t)=2\Omega_{\mathrm{ax}}(t).
\tag{33}
$$

Thus the flat-source coefficient (29) becomes $-\Omega_{\mathrm{ax}}/\nu$. The driven coefficient (30) includes $-(\nabla\times A)_z/(2\nu)$ as well. For the full corrected field, (33) additionally requires that non-axisymmetric corrections make no contribution to the first derivatives used there. The workbench’s axis identity is a source input here, not a newly independently audited property of every correction in the released construction.

## 8. Vorticity, shear, and horizon focusing

Near an axis, an incompressible affine velocity can have derivative matrix

$$
DU=\begin{pmatrix}
\alpha&-\Omega&0\\
\Omega&\alpha&0\\
0&0&-2\alpha
\end{pmatrix}.
\tag{34}
$$

Its vorticity is $(0,0,2\Omega)$, whereas its symmetric strain is

$$
S_U=\frac{DU+(DU)^{\mathsf T}}2
=\operatorname{diag}(\alpha,\alpha,-2\alpha),
\qquad S_U:S_U=6\alpha^2.
\tag{35}
$$

A diverging angular velocity cannot simply be substituted for the shear-squared heating term. Rigid rotation contributes to (30); symmetric deformation contributes to viscous heating and the horizon shear.

For a null hypersurface in five dimensions, choose a null generator $k$ with $\nabla_kk=\kappa k$, a three-dimensional screen metric, expansion $\theta$, and screen shear $\sigma_{AB}$. The hypersurface twist vanishes. The exact focusing equation is

$$
k(\theta)-\kappa\theta
=-\frac{\theta^2}{3}-\sigma_{AB}\sigma^{AB}-R_{AB}k^Ak^B.
\tag{36}
$$

Jacobson (1995) derives the Einstein equation from an area-entropy postulate and the Clausius relation on all local Rindler horizons. The construction here starts instead from Einstein geometry and derives its fluid constraint. Their shared interface is the null focusing equation and area entropy; the directions of the two derivations are explicit. The shear term in (36) remains in vacuum. Eling et al. (2009) derive the incompressible horizon-fluid equations and relate viscous energy loss to horizon-area increase in the long-wavelength regime. Chirco and Liberati (2010) identify the corresponding gravitational internal entropy production with tidal heating. These provide the physical dissipative bridge, without requiring bulk matter to be a literal viscous medium.

The Rindler transport coefficients in the units above are

$$
\eta_{\mathrm{phys}}=\frac{c^3}{16\pi G_5},\qquad
s_{\mathrm{hor}}=\frac{k_Bc^3}{4\hbar G_5},\qquad
\frac{\eta_{\mathrm{phys}}}{s_{\mathrm{hor}}}=\frac{\hbar}{4\pi k_B}.
\tag{37}
$$

The leading shear entropy production is $2\eta_{\mathrm{phys}}S_U:S_U/T_\ell$ per boundary volume. The coefficients in (37) and temperature (11) retain the full constants. A spacetime-integrated dissipation bound is not a pointwise bound on $\sigma_{AB}\sigma^{AB}$ along each individual generator.

## 9. What the concentrating profile does to the geometric scale budget

The released manuscript gives the core scalings, in its variables,

$$
L_r\asymp\tau^{1/2},\qquad
L_z\asymp\tau^{1/2-h},\qquad
|U_\theta|,|U_z|\asymp\tau^{-1/2-h},
\qquad 0<h<1/6.
\tag{38}
$$

For dimensional bookkeeping write instead

$$
L_r=L_{r0}(\tau/t_0)^{1/2},\quad
L_z=L_{z0}(\tau/t_0)^{1/2-h},\quad
U_{\mathrm{core}}=U_0(\tau/t_0)^{-1/2-h},
\tag{39}
$$

with positive reference constants retained. Products of these scales give

$$
E_{\mathrm{core}}\asymp\tau^{1/2-3h},\qquad
D_{\mathrm{core}}\asymp\tau^{-1/2-3h}.
\tag{40}
$$

Here $D_{\mathrm{core}}$ denotes the integrated squared radial-gradient scale of the leading core, not a pointwise identity for the full horizon shear. Its time integral is finite because

$$
\int_0^{\tau_0}\tau^{-1/2-3h}\,d\tau
=\frac{\tau_0^{1/2-3h}}{1/2-3h}.
\tag{41}
$$

The core can therefore have a diverging instantaneous dissipation scale while its cumulative leading-order dissipation remains finite. The fluid kinetic-energy integral is not being identified with an ADM mass: the gravitational energy is obtained from the chosen asymptotic or quasilocal stress prescription, such as (12), with its own reference subtraction. In the horizon interpretation this is the useful candidate pattern: concentration in curvature and shear without a forced divergence of the integrated area-production budget. It is not a derived black-hole spacetime.

### An explicit higher-gradient test

The first linear fourth-spatial-derivative term in the higher-order vacuum-fluid equation is, in the coordinates (2),

$$
-\frac32\ell^3\Delta^2v_i.
\tag{42}
$$

For a Fourier component of physical spatial wavenumber $k$, its magnitude divided by the leading viscous term is exactly

$$
\frac{(3/2)\ell^3 k^4}{\ell k^2}
=\frac32(\ell k)^2.
\tag{43}
$$

For $k\asymp L_r^{-1}$ this grows as

$$
\frac32\left(\frac{\ell}{L_{r0}}\right)^2\frac{t_0}{\tau}.
\tag{44}
$$

This is a concrete loss of ordering, not a general slogan that an approximation might fail. The fourth derivative has the damping sign in this linear test; its growth is a reason to solve the corrected equations, not evidence that its sign by itself produces a singularity.

There is a second explicit limit: $U_{\mathrm{core}}/c=(U_0/c)(\tau/t_0)^{-1/2-h}$. At fixed physical constants this eventually ceases to be a small-velocity expansion. The manuscript's oscillatory correction scales can be shorter than the core radius, so (44) is only one diagnostic, not a bound controlling the full multiscale solution.

Changing $\ell$ changes the cutoff acceleration, temperature, equilibrium pressure, and physical viscosity in (10)–(13). Applying Navier–Stokes scaling $U_\varepsilon(t,x)=\varepsilon U(\varepsilon^2t,\varepsilon x)$ instead preserves viscosity but moves the singular time to $T/\varepsilon^2$. Neither operation demonstrates a single fixed-parameter smooth bulk completion through the original terminal event.

## 10. The nonlinear-feedback connection to vacuum gravity

Let a phase average commute with the relevant derivatives, write $U=\overline U+w$, and impose $\langle w\rangle=0$. The exact averaged momentum equation contains

$$
\partial_t\overline U_i+\overline U_j\partial_j\overline U_i
+\partial_i\overline p-\nu\Delta\overline U_i
=\overline f_i-\partial_j\mathcal R_{ij},
\qquad
\mathcal R_{ij}=\langle w_iw_j\rangle.
\tag{45}
$$

Thus oscillatory fluctuations can supply a mean momentum flux even when their linear average vanishes. The released construction uses this kind of quadratic feedback to sustain its concentrating background.

Vacuum gravity has a structurally related expansion. For $g=\overline g+h$ with zero first-order mean, the second-order Einstein equation contains

$$
G[\overline g]=-\langle G^{(2)}_{\overline g}[h,h]\rangle
+\text{higher perturbative and averaging contributions}.
\tag{46}
$$

Isaacson (1968) constructs the high-frequency effective gravitational-wave stress in an appropriate geometric-optics regime. The corresponding Einstein-gravity expression in five dimensions, with five-dimensional index contractions and $G_5$, is

$$
t^{\mathrm{GW}}_{AB}
=\frac{c^4}{32\pi G_5}
\left\langle\nabla_Ah^{\mathrm{TT}}_{CD}\nabla_Bh_{\mathrm{TT}}^{CD}\right\rangle.
\tag{47}
$$

The mean geometry can therefore respond to the quadratic content of vacuum gravitational disturbances. Equations (45)–(47) identify the relevant physical comparison: feedback through averaged quadratic fluxes.

The two quadratic maps have different domains and tensor outputs. The fluid map sends a spatial velocity perturbation to $\langle w\otimes w\rangle$; the gravitational map sends a transverse metric perturbation to derivatives contracted in a spacetime tensor. A reconstruction $w\mapsto h$ must be inserted before comparing them. A possible simultaneous regime requires the gravitational microscopic/horizon scale to be shorter than the perturbation wavelength, and that wavelength to be shorter than the background-curvature scale. Concentration removes this interval unless those scales are controlled together.

## 11. From a horizon-fluid model to a two-sided black-hole model

A Rindler cutoff construction determines a local near-horizon region. The restriction map

$$
(M,g)\longmapsto(\mathcal U\subset M,g|_{\mathcal U})
\tag{48}
$$

forgets the number of asymptotic regions, the continuation behind a horizon, and the global preparation of a quantum state. Those structures cannot be recovered from local fluid data alone.

A concrete setting retaining them is the two-sided AdS black brane. The five-dimensional seed metric in ingoing coordinates is

$$
ds^2=-f_b(r)(dx^0)^2+2dx^0dr+\frac{r^2}{L^2}d\mathbf x^2,
\qquad
f_b(r)=\frac{r^2}{L^2}\left(1-\frac{r_h^4}{r^4}\right).
\tag{49}
$$

It solves $R_{AB}=-4g_{AB}/L^2$, with

$$
T_H=\frac{\hbar c r_h}{\pi k_BL^2}.
\tag{50}
$$

The additional data $L$ and the cosmological constant have not been discarded. Expanding $f_b$ near $r_h$ gives a Rindler lapse to first order in $r-r_h$; this is a local limit of (49), not a global replacement of it by (5).

Bhattacharyya et al. (2008) construct the asymptotically AdS derivative expansion of black-brane fluid flows. Their forced extension with additional sources is given in Bhattacharyya, Loganayagam, et al. (2009). A suitable project therefore has an explicit two-sided geometry and state preparation first, a boundary drive second, and the concentrating fluid profile as a proposed long-wavelength history. Its observables include $R_{n0ij}$, freely falling tidal components $R_{ABCD}e_{\hat0}^Ae_{\hat i}^Be_{\hat0}^Ce_{\hat j}^D$, null expansions, and cross-boundary correlations.

A divergent component in an accelerating frame alone is not a proof of a curvature singularity. Frame-invariant curvature contractions or parallelly propagated curvature along appropriate geodesics, and the causal geometry, distinguish a physical singularity from an observer-dependent blowup. Moreover, the existence of a connected two-sided interior is a global statement; the curvature diagnostic (30) alone does not determine it.

## 12. The exact information test for ER = EPR

The standard thermofield-double preparation is

$$
|\mathrm{TFD}_\beta\rangle
=Z(\beta)^{-1/2}\sum_n e^{-\beta E_n/2}|n\rangle_L|n\rangle_R,
\qquad \beta=(k_BT)^{-1}.
\tag{51}
$$

Its left restriction is $\rho_L=e^{-\beta H_L}/Z(\beta)$. The map

$$
\mathcal P_L:\rho_{LR}\longmapsto\operatorname{Tr}_R\rho_{LR}
\tag{52}
$$

is the finite-system version of restricting a state to one side. In continuum field theory a local algebra need not admit this tensor-factor density-matrix description; (52) is used here as an exact regulated test, not a claim of continuum factorization.

The hydrodynamic observation map is a further reduction,

$$
\mathcal H_L:\rho_{LR}\longmapsto
\operatorname{Tr}\!\left[\rho_{LR}(\widehat T_{ab}^{\,L}\otimes I_R)\right]
\longmapsto\text{constitutive fluid data}.
\tag{53}
$$

This factors through (52). Its non-injectivity can be exhibited without any gravity conjecture.

Take $H=E|1\rangle\langle1|$ and $q=e^{-\beta E}>0$. Define

$$
\rho_\beta=\frac{|0\rangle\langle0|+q|1\rangle\langle1|}{1+q},
\quad
|\Psi\rangle=\frac{|00\rangle+\sqrt q|11\rangle}{\sqrt{1+q}},
\quad
\sigma=\rho_\beta\otimes\rho_\beta.
\tag{54}
$$

Both $|\Psi\rangle\langle\Psi|$ and $\sigma$ have exactly the same left and right thermal marginals. Nevertheless, with $X=|0\rangle\langle1|+|1\rangle\langle0|$,

$$
\langle X_LX_R\rangle_\Psi=\frac{2\sqrt q}{1+q},
\qquad
\langle X_LX_R\rangle_\sigma=0.
\tag{55}
$$

The first state is entangled and pure, while the second is a separable product. Thus even complete one-sided state information—more than a Navier–Stokes stress history at one time—does not select the cross-side correlations. This is an explicit failure of inversion for the observation map, not a denial of the holographic relationship.

There is a further useful exact statement about driving. When the total Hamiltonian contains separate time-dependent left and right terms but no coupling or external quantum bath,

$$
\rho_{LR}(t)=(U_L(t)\otimes U_R(t))\rho_{LR}(0)
(U_L(t)^\dagger\otimes U_R(t)^\dagger),
$$

and

$$
\rho_L(t)=U_L(t)\rho_L(0)U_L(t)^\dagger,
\qquad S_{\mathrm{vN}}(\rho_L(t))=S_{\mathrm{vN}}(\rho_L(0)).
\tag{56}
$$

Such driving can change local stress and dissipative hydrodynamic observables while preserving entanglement across the complete left–right split. Hence a rise in coarse-grained horizon-fluid entropy does not by itself establish creation of EPR entanglement between the two sides.

For time-dependent holography the entropy map uses an appropriate extremal surface, with a specified region and homology constraint, rather than an arbitrary event-horizon cut (Hubeny et al., 2007; Dong et al., 2016). At leading classical order,

$$
S_{\mathrm{vN}}(A)=\frac{k_Bc^3}{4G_5\hbar}\operatorname{Area}(\mathcal X_A),
\tag{57}
$$

within that holographic prescription; quantum and higher-curvature corrections require their own terms. The geometric and state data entering (57) are additional to the classical fluid equation.

## 13. An exact EPR geometry for comparison

Jensen and Karch (2013) give a concrete holographic entangled quark–antiquark construction whose string worldsheet contains a nontraversable bridge. Its geometry is a useful independent calibration of the word “bridge.”

In an AdS metric

$$
ds^2=\frac{L^2}{z^2}\left[-(dX^0)^2+(dX^1)^2+dz^2+d\mathbf x_\perp^2\right],
$$

take the exterior worldsheet embedding

$$
X^0=\sqrt{b^2-z^2}\sinh(s/b),\qquad
X^1=\sqrt{b^2-z^2}\cosh(s/b),\qquad \mathbf x_\perp=0.
\tag{58}
$$

Its pullback is exactly

$$
\boxed{
F^*g=\frac{L^2}{z^2}\left[
-\left(1-\frac{z^2}{b^2}\right)ds^2+
\frac{dz^2}{1-z^2/b^2}\right].
}
\tag{59}
$$

The horizon is at $z=b$, the endpoint proper acceleration is $c^2/b$, and the associated temperature is $\hbar c/(2\pi k_Bb)$. Direct curvature calculation gives

$$
\mathcal R[F^*g]=-\frac{2}{L^2}.
\tag{60}
$$

Thus the worldsheet horizon is regular in intrinsic curvature. The maximal continuation has the two-sided worldsheet causal structure used in the holographic EPR interpretation. The embedding map (58), rather than an equality of vocabulary, explains how this two-dimensional geometry sits in the higher-dimensional spacetime. No Navier–Stokes blowup is required to obtain this established model.

Recent model-specific work continues to derive ER = EPR constructions from specified thermofield-double systems (Jiang et al., 2026). Such constructions start with quantum preparation and holographic data; they do not turn the local, classical fluid observation map (53) into an injective map.

## 14. Research direction and present mathematical result

The strongest vacuum-hydrodynamic programme is an investigation of **source-coupled canonical vorticity, curvature concentration, and horizon entropy production in a specified five-dimensional, two-sided gravitational model**.

The immediate computable object is (26) followed by (30) and (32). It retains the actual force, the material deformation, the gravitational cutoff, and the full sign of the vorticity contribution. The next geometric calculation is the corrected metric's tidal and null data, using the higher-gradient terms rather than extrapolating a leading coefficient beyond (44). Cross-boundary correlation functions and the extremal-surface entropy then test the quantum interpretation in the chosen state.

This yields definite results already: the coordinate-to-viscosity map, the boundary-force reconstruction, the curvature diagnostic including its source term, the canonical-vorticity transport identity, the finite integrated concentration budget, and the explicit information loss under one-sided restriction. It also gives a concrete EPR worldsheet geometry against which to compare a claimed bridge.

The physical hypothesis remains productive: a concentrating fluid solution can be used to investigate sharply focused vacuum gravitational and horizon dynamics. The conclusion “Navier–Stokes proves ER = EPR” is not established by these maps. The classical reconstruction does not determine the bipartite quantum state, and the terminal limit is outside the fixed-order regime demonstrated here. Neither statement prevents further construction; each identifies an actual object and calculation rather than replacing the physical question with terminology.

## Appendix A. The complete displayed fifth-order flat-cutoff correction

To retain the source's correction rather than keeping only its linear fourth derivative, define

$$
\Sigma_{ij}=\partial_iv_j+\partial_jv_i,\qquad
W_{ij}=\partial_iv_j-\partial_jv_i.
$$

In the variables (2), Compère et al.'s (2011, eq. 6.3) displayed correction is

$$
\begin{aligned}
\mathcal F_i={}&-\frac32\ell^3\Delta^2v_i
+2\ell^2v_k\Delta\partial_kv_i
+\ell^2\Sigma_{ik}\partial_l\Sigma_{kl}
-\frac52\ell^2W_{ik}\partial_l\Sigma_{kl}\\
&-\frac34\ell^2\partial_i(\Sigma_{kl}\Sigma_{kl})
-\frac58\ell^2\partial_i(W_{kl}W_{lk})
+\ell^2\Sigma_{kl}\partial_k\Sigma_{li}\\
&-2\ell v_k\partial_k\partial_i\Pi
-2\ell(\partial_kv_i)\partial_k\Pi
-\ell\Pi\Delta v_i-\frac\ell2v^2\Delta v_i\\
&-\frac\ell2(\partial_k\Sigma_{il})v_kv_l
+\frac\ell2(\partial_kW_{il})v_kv_l
+2\ell(\partial_kv_i)W_{kl}v_l\\
&+(\Pi+v^2)\partial_i\Pi-v_i\partial_0\Pi.
\end{aligned}
\tag{A1}
$$

The corrected equation has right-hand side $\mathcal F_i+O(\varepsilon^7)$ in the flat-cutoff source setting. The corresponding displayed incompressibility correction is

$$
\partial_iv_i=v_i\partial_i\Pi-\ell v_i\Delta v_i
+\frac\ell2\Sigma_{ij}\Sigma_{ij}+O(\varepsilon^6).
\tag{A2}
$$

In particular $W_{kl}W_{lk}$ has been retained in its source order. Since $W$ is antisymmetric, replacing it by $W_{kl}W_{kl}$ without changing its sign would be an error. These are the source's flat-boundary corrections after the explicit map (7); they are not the full correction formula for the driven curved boundary (22).

## References

Bhattacharyya, S., Hubeny, V. E., Minwalla, S., & Rangamani, M. (2008). Nonlinear fluid dynamics from gravity. *Journal of High Energy Physics, 2008*(02), 045. doi:10.1088/1126-6708/2008/02/045. [Primary text](https://arxiv.org/abs/0712.2456).

Bhattacharyya, S., Loganayagam, R., Minwalla, S., Nampuri, S., Trivedi, S. P., & Wadia, S. R. (2009). Forced fluid dynamics from gravity. *Journal of High Energy Physics, 2009*(02), 018. doi:10.1088/1126-6708/2009/02/018. [Primary text](https://arxiv.org/abs/0806.0006).

Bhattacharyya, S., Minwalla, S., & Wadia, S. R. (2009). The incompressible non-relativistic Navier–Stokes equation from gravity. *Journal of High Energy Physics, 2009*(08), 059. doi:10.1088/1126-6708/2009/08/059. [Primary text](https://arxiv.org/abs/0810.1545).

Bredberg, I., Keeler, C., Lysov, V., & Strominger, A. (2012). From Navier–Stokes to Einstein. *Journal of High Energy Physics, 2012*(07), 146. doi:10.1007/JHEP07(2012)146. [Primary text](https://arxiv.org/abs/1101.2451).

Chirco, G., & Liberati, S. (2010). Non-equilibrium thermodynamics of spacetime: The role of gravitational dissipation. *Physical Review D, 81*, 024016. doi:10.1103/PhysRevD.81.024016. [Primary text](https://arxiv.org/abs/0909.4194).

Compère, G., McFadden, P., Skenderis, K., & Taylor, M. (2011). The holographic fluid dual to vacuum Einstein gravity. *Journal of High Energy Physics, 2011*(07), 050. doi:10.1007/JHEP07(2011)050. [Primary text, revised version](https://arxiv.org/abs/1103.3022).

Dong, X., Lewkowycz, A., & Rangamani, M. (2016). Deriving covariant holographic entanglement. *Journal of High Energy Physics, 2016*(11), 028. doi:10.1007/JHEP11(2016)028. [Primary text](https://arxiv.org/abs/1607.07506).

Eling, C., Fouxon, I., & Oz, Y. (2009). The incompressible Navier–Stokes equations from black hole membrane dynamics. *Physics Letters B, 680*, 496–499. doi:10.1016/j.physletb.2009.09.028. [Primary text](https://arxiv.org/abs/0905.3638).

Hubeny, V. E., Rangamani, M., & Takayanagi, T. (2007). A covariant holographic entanglement entropy proposal. *Journal of High Energy Physics, 2007*(07), 062. doi:10.1088/1126-6708/2007/07/062. [Primary text](https://arxiv.org/abs/0705.0016).

Isaacson, R. A. (1968). Gravitational radiation in the limit of high frequency. II. Nonlinear terms and the effective stress tensor. *Physical Review, 166*, 1272–1280. doi:10.1103/PhysRev.166.1272. [Primary publication](https://journals.aps.org/pr/abstract/10.1103/PhysRev.166.1272).

Jacobson, T. (1995). Thermodynamics of spacetime: The Einstein equation of state. *Physical Review Letters, 75*, 1260–1263. doi:10.1103/PhysRevLett.75.1260. [Primary text](https://arxiv.org/abs/gr-qc/9504004).

Jensen, K., & Karch, A. (2013). Holographic dual of an Einstein–Podolsky–Rosen pair has a wormhole. *Physical Review Letters, 111*, 211602. doi:10.1103/PhysRevLett.111.211602. [Primary text](https://arxiv.org/abs/1307.1132).

Jiang, X., Wang, P., Wu, H., & Yang, H. (2026). Realization of “ER=EPR.” *Journal of High Energy Physics, 2026*(06), 270. [Primary text, version 3](https://arxiv.org/html/2411.18485v3).

Maldacena, J. M. (2003). Eternal black holes in anti-de Sitter. *Journal of High Energy Physics, 2003*(04), 021. doi:10.1088/1126-6708/2003/04/021. [Primary text](https://arxiv.org/abs/hep-th/0106112).

Maldacena, J., & Susskind, L. (2013). Cool horizons for entangled black holes. *Fortschritte der Physik, 61*(9), 781–811. doi:10.1002/prop.201300020. [Primary text](https://arxiv.org/abs/1306.0533).

OpenAI. (2026a, September 8). *On the Navier–Stokes Millennium Prize Problem*. [Official release](https://openai.com/index/navier-stokes-solution/).

OpenAI. (2026b). *Finite time blowup for Navier–Stokes* [Released manuscript]. [Primary manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf). Theorem 1.1 and §§2–3 are the principal inputs used here.

Unruh, W. G. (1976). Notes on black-hole evaporation. *Physical Review D, 14*, 870–892. doi:10.1103/PhysRevD.14.870. [Primary publication](https://journals.aps.org/prd/abstract/10.1103/PhysRevD.14.870).

*Project source.* (2026). *Branch · Compile Navier Stokes Literature* [Supplied conversation export]. Axis observable: lines 2500–2522; gravity and ER = EPR programme: lines 4591–4624. Its earlier linked archives and manuscripts are not silently treated as files supplied with this note.
