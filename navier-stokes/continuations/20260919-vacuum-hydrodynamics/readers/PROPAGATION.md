*GitHub reading copy; only mathematical delimiters have changed. [Unchanged source](../archive/ns-vacuum-propagation/docs/PROPAGATION.md).*

# Propagating the released Navier–Stokes construction into vacuum hydrodynamics

## 1. Source and scope

The mathematical input is OpenAI's *Finite time blowup for Navier–Stokes*, released on 8 September 2026. The accessible manuscript has 166 PDF pages. Theorem 1.1 states a smooth, compactly supported forcing construction for every positive viscosity, with rest initial data, fixed compact spatial support of the preterminal velocity and pressure, a uniform velocity $L^2$ bound, and an infinite velocity $L^\infty$ **limsup** as $t\uparrow1$. Corollary 10.6 supplies its periodic version. Theorem 1.1's exact quantifier is not replaced here by a limit. The explicit growing path in the proof supplies additional information, but it is a separate source statement (OpenAI, 2026a, Theorem 1.1; §10).

The upstream formalization metadata identifies the declarations `NavierStokes.Comparator.navier_stokes_breakdown_R3` and `NavierStokes.Comparator.navier_stokes_breakdown_periodic`, both in `NavierStokes/ComparatorSolution.lean`. It reports the axioms `propext`, `Classical.choice`, and `Quot.sound`, and labels review as self-assessed. These are inspected upstream metadata, not a local kernel replay. The challenge file is an independent statement surface with intentional challenge placeholders; the proof submission is a different module (OpenAI, 2026b). Exact acquisition and verification commands are provided separately.

This continuation establishes new downstream identities and estimates. Its analytic proofs concern mass transport, gradient growth, rotational averaging, stress completion, and boundary geometry. The fluid-to-bulk reconstruction remains a hydrodynamic expansion at the orders specified in the gravity literature. A coefficient in that expansion is not presented as an exact, globally constructed singular spacetime. No conclusion in this note depends on the result being an open problem, a prize problem, or an AI-generated result.

The previous package is retained unmodified under `archive/v1`. Its source range $0<h<1/6$ is too broad as a statement of the manuscript's parameter choice: the source uses $0<h<1/100$. The wider inequality only explains why a particular energy exponent would be positive; it is not the construction's admissible range. The current derivations use the source's range.

## 2. The equation and the exact dimensional map

Use physical Cartesian coordinates $x=(x^1,x^2,x^3)$ and time $t$, with constant mass density $\rho_0>0$:

$$
\partial_t U_i+U_j\partial_jU_i-\nu\partial_j\partial_jU_i+\partial_iP=f_i,
\qquad \partial_iU_i=0. \tag{2.1}
$$

Here $P$ is pressure divided by $\rho_0$, $f$ is force per unit mass, and $\nu>0$ is kinematic viscosity. They have units $[U]=L/T$, $[P]=L^2/T^2$, $[f]=L/T^2$, and $[\nu]=L^2/T$.

To interpret source coordinates physically, retain two positive constants $L_0,T_0$. For a manuscript triple $(u,p,f_{\mathrm s})$ at its numerical viscosity $\nu_{\mathrm s}>0$, define

$$
x=L_0\widehat x,\quad t=T_0\widehat t,\quad
U(x,t)=\frac{L_0}{T_0}u(\widehat x,\widehat t),\quad
P(x,t)=\frac{L_0^2}{T_0^2}p(\widehat x,\widehat t),\quad
f(x,t)=\frac{L_0}{T_0^2}f_{\mathrm s}(\widehat x,\widehat t),\quad
\nu=\frac{L_0^2}{T_0}\nu_{\mathrm s}. \tag{2.2}
$$

Substitution makes the left side of (2.1) exactly $L_0/T_0^2$ times the source residual. Incompressibility is multiplied by $T_0^{-1}$. The terminal time becomes $T_0$, rather than being declared one second. No physical parameter has been assigned a numerical value.

For two physical viscosities $\nu_1,\nu_2$, put $a=(\nu_2/\nu_1)^{1/2}$. There is also the exact map

$$
U_2(x,t)=aU_1(x/a,t),\quad P_2(x,t)=a^2P_1(x/a,t),\quad f_2(x,t)=af_1(x/a,t). \tag{2.3}
$$

The time coordinate is unchanged. Each residual term is multiplied by $a$, because $\nu_2/a^2=\nu_1$. Its measurable consequences are

$$
\|U_2\|_2^2=a^5\|U_1\|_2^2,\quad
\nabla U_2(x,t)=\nabla U_1(x/a,t),\quad
\operatorname{curl}U_2(x,t)=\operatorname{curl}U_1(x/a,t). \tag{2.4}
$$

Equations (2.3)–(2.4) are the dimensional version of the manuscript's (10.22)–(10.23). They retain the distinction between changing viscosity and changing time (OpenAI, 2026a).

## 3. Mass conservation, core mass, and energy

### 3.1 The material-volume morphism

For $0\le t\le T'<T_0$, the smooth, compactly supported velocity defines a material flow $X_t$ by

$$
\dot X_t(a)=U(X_t(a),t),\qquad X_0(a)=a.
$$

Let $J_t(a)=D_aX_t(a)$. Differentiating this ODE gives

$$
\dot J_t=(D_xU)(X_t,t)J_t,
\qquad \frac{d}{dt}\det J_t=(\operatorname{div}U)(X_t,t)\det J_t=0.
$$

Therefore $\det J_t=1$ on every preterminal interval. The exact map of measures is

$$
(X_t)_*(\rho_0\,d^3a)=\rho_0\,d^3x,
\qquad \int_{X_t(V)}\rho_0\,d^3x=\rho_0|V|. \tag{3.1}
$$

This proves conservation of the mass of every finite material parcel. In particular, the incompressible construction does not create a density atom: at every preterminal time,

$$
\int_{|x|<r}\rho_0\,d^3x=\frac{4\pi}{3}\rho_0r^3. \tag{3.2}
$$

On $\mathbb R^3$, constant-density fluid fills all space even when its velocity has compact support; its total rest mass is already infinite. Equation (3.1), finite parcels, bounded observation regions, or the periodic domain are the appropriate finite mass statements. None identifies velocity growth with newly created infinite mass.

### 3.2 The source's shrinking core has an exact volume formula

Equations (3.3)–(3.7) first describe the manuscript's numerical-viscosity-one stage, before the explicit map (2.3). For this calculation retain the source variables and exponents

$$
\tau=1-\widehat t,\quad A=\frac12+h,\quad D=\frac12-h,\quad 0<h<\frac1{100},
$$

$$
\tau=q(1-\eta^2),\quad \widehat z=q^D\eta,\quad X=\frac{\widehat r^2}{2q}. \tag{3.3}
$$

These are the source's (3.2), (4.1). They are an exact coordinate map, not an assertion that the final corrected solution is exactly self-similar (OpenAI, 2026a).

At fixed $\tau>0$,

$$
q=\frac{\tau}{1-\eta^2},\qquad
\widehat z=\tau^D\eta(1-\eta^2)^{-D},\qquad
\frac{d\widehat z}{d\eta}
=\tau^D\frac{1-2h\eta^2}{(1-\eta^2)^{D+1}}.
$$

Since $\widehat r\,d\widehat r=q\,dX$ at fixed $\eta$, the cylindrical volume measure is

$$
d^3\widehat x
=\tau^{1+D}\frac{1-2h\eta^2}{(1-\eta^2)^{D+2}}\,dX\,d\theta\,d\eta. \tag{3.4}
$$

For the source's geometric core $0\le X\le X_c$, $|\eta|\le\eta_c<1$, its physical rest mass is exactly

$$
M_{\mathrm{core}}(\tau)
=2\pi\rho_0L_0^3X_c\tau^{3/2-h}
\int_{-\eta_c}^{\eta_c}
\frac{1-2h\eta^2}{(1-\eta^2)^{5/2-h}}\,d\eta. \tag{3.5}
$$

It tends to zero. This core is a moving geometric region, not a fixed material parcel. Equation (3.1) and equation (3.5) are consistent because particles enter and leave that region. For any moving region with boundary velocity $V_b$, the exact relation is

$$
\frac{d}{dt}\int_{C(t)}\rho_0\,dx
=\int_{\partial C(t)}\rho_0(V_b-U)\cdot n\,dS. \tag{3.6}
$$

There is no conversion of decreasing core volume into increasing mass density.

### 3.3 Exact leading-field energy, with both powers retained

The source defines $u_\theta^{(0)}=q^{-A}E$, $u_z^{(0)}=q^{-A}U_{\mathrm{p}}$, and $\widehat r u_r^{(0)}=V_0$. The notation $U_{\mathrm{p}}$ here denotes the source's axial profile $U(X,\eta)$ and avoids collision with physical velocity. Its leading kinetic energy over the same core is

$$
E^{(0)}_{\mathrm{core}}(\tau)=\frac{\pi\rho_0L_0^5}{T_0^2}
\left[\tau^{1/2-3h}I_{\mathrm{tan}}+\tau^{1/2-h}I_r\right], \tag{3.7}
$$

where

$$
I_{\mathrm{tan}}=\int_{-\eta_c}^{\eta_c}\!\int_0^{X_c}
(E^2+U_{\mathrm{p}}^2)(1-2h\eta^2)(1-\eta^2)^{2A-D-2}\,dX\,d\eta,
$$

$$
I_r=\int_{-\eta_c}^{\eta_c}\!\int_0^{X_c}
\frac{V_0^2}{2X}(1-2h\eta^2)(1-\eta^2)^{-D-1}\,dX\,d\eta.
$$

Under the map from numerical viscosity one to $\nu_{\mathrm s}>0$, the image core has every spatial coordinate multiplied by $\sqrt{\nu_{\mathrm s}}$. Its mass is therefore $\nu_{\mathrm s}^{3/2}$ times (3.5), and its leading kinetic energy is $\nu_{\mathrm s}^{5/2}$ times (3.7). These factors follow from the spatial Jacobian and velocity multiplier in (2.3), while the terminal time is unchanged.

The source's axis regularity $V_0=Xv_0$ makes the second integral finite. These are exact integrals of the **leading field**. The final field's uniform energy bound comes from Theorem 1.1, not from replacing it by this leading field.

### 3.4 The full corrected solution has finite total viscous dissipation

Set $F(t)=\|f(t)\|_{L^2}$ and $I(t)=\int_0^tF(s)\,ds$. Multiplying (2.1) by $\rho_0U$ and integrating gives, without a boundary term,

$$
\frac{\rho_0}{2}\|U(t)\|_2^2+
\rho_0\nu\int_0^t\|\nabla U(s)\|_2^2\,ds
=\rho_0\int_0^t\!\int f\cdot U\,dx\,ds. \tag{3.8}
$$

A regularization of the norm at zero gives $\|U(t)\|_2\le I(t)$. Consequently

$$
\frac{\rho_0}{2}\|U(t)\|_2^2+
\rho_0\nu\int_0^t\|\nabla U(s)\|_2^2\,ds
\le\frac{\rho_0}{2}I(t)^2. \tag{3.9}
$$

The smooth compact force has finite $I(T_0)$. Hence the integrated dissipation remains finite up to the endpoint. With $S=(DU+DU^{\mathsf T})/2$, integration by parts gives $\int |\nabla U|^2=2\int S:S$. Both the density conservation and the energy accounting concern the actual corrected solution.

## 4. Unbounded vorticity and strain of the actual corrected field

The following estimates do not require an axis identity or a leading-profile approximation. They are explicit consequences of heat-kernel smoothing, not a priority claim for a new interpolation principle. Let $V\in C_c^\infty(\mathbb R^3;\mathbb R^3)$, $\operatorname{div}V=0$, and write

$$
H=\|V\|_\infty,\qquad E=\|V\|_2,\qquad
W=\|\operatorname{curl}V\|_\infty,\qquad
Z=\|\operatorname{sym}DV\|_{L^\infty;F}.
$$

The vector norms are Euclidean and $F$ denotes the matrix Frobenius norm. For $V\ne0$,

$$
\boxed{W\ge\frac{\pi}{2^{13/6}}H^{5/3}E^{-2/3}},\qquad
\boxed{Z\ge\frac{\pi}{2^{19/6}}H^{5/3}E^{-2/3}}. \tag{4.1}
$$

**Proof.** Let $G_a(x)=(4\pi a)^{-3/2}\exp(-|x|^2/(4a))$ for a heat parameter $a>0$ with units of length squared. Direct radial integration gives

$$
\|G_a\|_2=(8\pi a)^{-3/4},\qquad
\|\nabla G_a\|_1=\frac{2}{\sqrt{\pi a}}. \tag{4.2}
$$

Since $\Delta V=-\operatorname{curl}\operatorname{curl}V$,

$$
V=G_a*V+\int_0^a\operatorname{curl}(G_b*\operatorname{curl}V)\,db.
$$

The cross-product bound in the second convolution gives

$$
H\le(8\pi a)^{-3/4}E+\frac4{\sqrt\pi}\sqrt a\,W. \tag{4.3}
$$

Choose $a=[2(8\pi)^{-3/4}E/H]^{4/3}$. This is an auxiliary integration parameter, not a rescaling of the fluid equation. The first term equals $H/2$. Solving the remaining inequality proves the first estimate in (4.1), including its constant.

For the second estimate, incompressibility gives $\Delta V_i=2\partial_jS_{ij}$. Thus

$$
V=G_a*V-2\int_0^a\operatorname{div}(G_b*S)\,db,
$$

and the Frobenius contraction bound gives

$$
H\le(8\pi a)^{-3/4}E+\frac8{\sqrt\pi}\sqrt a\,Z.
$$

The same value of $a$ proves the second estimate. The zero field satisfies the corresponding homogeneous inequalities trivially. This completes the analytic proof; symbolic checks below verify the integrals and constants, not the functional-analytic argument by themselves.

Apply (4.1) at each preterminal time to the actual OpenAI velocity and use its bounded $L^2$ norm. The infinite velocity limsup forces

$$
\limsup_{t\uparrow T_0}\|\operatorname{curl}U(t)\|_\infty=\infty,
\qquad
\limsup_{t\uparrow T_0}\|S(t)\|_{\infty;F}=\infty. \tag{4.4}
$$

Together, (3.9) and (4.4) show unbounded local strain despite finite space-time integrated strain squared. This is a full-field consequence, not an extrapolation from swirl on the axis.

The leading angular field still gives a useful more local diagnostic. From the source's (4.3),

$$
u_\theta^{(0)}=\frac{\widehat r}{C}q^{-1-h}\phi(X,\eta),\qquad
(\operatorname{curl}u^{(0)})_z=\frac2Cq^{-1-h}(\phi+X\phi_X). \tag{4.5}
$$

The source's (B.3) gives $\phi(0,0)=1$. Its leading-axis value at $\widehat z=0$ is therefore $2C^{-1}\tau^{-1-h}$, and its physical value is divided by $T_0$. Equation (4.5) is explicitly a leading-field statement; (4.4) avoids importing an unverified exact axis evaluation of all correction terms.

### 4.1 Stronger rates from the constructive path, not just the headline limsup

The source's Theorem 3.1(iv), proved in §9, supplies a fixed $X_{\mathrm{in}}\in(0,X_a)$ and $e_0=E_0(X_{\mathrm{in}},0)>0$ such that

$$
u_{\theta,\mathrm{loc}}(\sqrt{2X_{\mathrm{in}}\tau},0,0,1-\tau)
=\tau^{-A}\bigl(e_0+O(\tau^{2h})\bigr). \tag{4.6}
$$

Proposition 10.1 leaves this local field unchanged in a fixed neighborhood of the origin at sufficiently late times. The point in (4.6) eventually lies in that neighborhood. Consequently, the full localized velocity at the source's numerical viscosity-one construction satisfies $\|u_1(1-\tau)\|_\infty\ge(e_0/2)\tau^{-A}$ for every sufficiently small positive $\tau$, not merely along a subsequence (OpenAI, 2026a, Theorem 3.1(iv); Proposition 10.1).

Let $E_1>0$ bound $\|u_1(t)\|_2$. After the source's exact map to numerical viscosity $\nu_{\mathrm{s}}>0$ and the physical map (2.2), the corresponding constants are

$$
\|U(T_0(1-\tau))\|_\infty\ge
\frac{L_0}{T_0}\sqrt{\nu_{\mathrm{s}}}\frac{e_0}{2}\tau^{-A},
\qquad
\|U(t)\|_2\le\frac{L_0^{5/2}}{T_0}\nu_{\mathrm{s}}^{5/4}E_1. \tag{4.7}
$$

Insert both factors into (4.1). The $L_0$ and $\nu_{\mathrm{s}}$ powers cancel through the displayed transformation, while $T_0^{-1}$ remains. For all sufficiently late times,

$$
\boxed{\begin{aligned}
\|\operatorname{curl}U(T_0(1-\tau))\|_\infty
&\ge\frac{\pi}{2^{13/6}T_0}
\left(\frac{e_0}{2}\right)^{5/3}E_1^{-2/3}\tau^{-5/6-5h/3},\\
\|S(T_0(1-\tau))\|_{\infty;F}
&\ge\frac{\pi}{2^{19/6}T_0}
\left(\frac{e_0}{2}\right)^{5/3}E_1^{-2/3}\tau^{-5/6-5h/3}.
\end{aligned}} \tag{4.8}
$$

Thus both norms tend to infinity for this constructed family. Equation (4.8) uses the source's additional path statement and its localization, not a silent strengthening of the quantifier in Theorem 1.1. It does not require differentiating an unproved asymptotic expansion of the final field or assuming an exact corrected-axis jet.

## 5. The nonlinear feedback survives a precise rotational projection

Let $Q_\alpha$ rotate $\mathbb R^3$ about the $z$ axis. Define rotational averaging on vector fields by

$$
(\mathcal P_1U)(x)=\frac1{2\pi}\int_0^{2\pi}Q_{-\alpha}U(Q_\alpha x)\,d\alpha,
$$

and on scalar pressure by $(\mathcal P_0P)(x)=(2\pi)^{-1}\int_0^{2\pi}P(Q_\alpha x)\,d\alpha$. On rank-two tensors define

$$
(\mathcal P_2T)(x)=\frac1{2\pi}\int_0^{2\pi}Q_{-\alpha}T(Q_\alpha x)Q_\alpha\,d\alpha. \tag{5.1}
$$

The factor $1/(2\pi)$ is part of the projection definition; unaveraged integration is $2\pi\mathcal P$. Vector and tensor rotations are included, so averaging Cartesian components at different azimuths is not substituted for averaging cylindrical components. Orthogonal changes of variables prove $\operatorname{div}\mathcal P_2T=\mathcal P_1\operatorname{div}T$ and $\Delta\mathcal P_1U=\mathcal P_1\Delta U$.

Put $\overline U=\mathcal P_1U$, $w=U-\overline U$, and

$$
\Sigma=\mathcal P_2(w\otimes w).
$$

Equivariance of $\overline U$ gives vanishing cross terms, and hence the exact identity

$$
\mathcal P_2(U\otimes U)=\overline U\otimes\overline U+\Sigma. \tag{5.2}
$$

In the cylindrical frame, $\Sigma_{ab}=\langle w_aw_b\rangle_\theta$. It is positive semidefinite pointwise and has trace $\langle|w|^2\rangle_\theta$. Applying the projections to (2.1) gives

$$
\partial_t\overline U+\operatorname{div}(\overline U\otimes\overline U)
-\nu\Delta\overline U+\nabla\overline P
=\overline f-\operatorname{div}\Sigma. \tag{5.3}
$$

The covariance is the exact nonlinear momentum feedback. It is not an additional external force invented after averaging.

For any axisymmetric symmetric tensor $T$, all cylindrical divergence terms are

$$
\begin{aligned}
(\operatorname{div}T)_r&=\partial_rT_{rr}+\partial_zT_{rz}+(T_{rr}-T_{\theta\theta})/r,\\
(\operatorname{div}T)_\theta&=\partial_rT_{r\theta}+\partial_zT_{z\theta}+2T_{r\theta}/r,\\
(\operatorname{div}T)_z&=\partial_rT_{rz}+\partial_zT_{zz}+T_{rz}/r.
\end{aligned} \tag{5.4}
$$

These formulas are checked against a nontrivial divergence-free oscillatory field in the supplied tests. In particular, the radial diagonal stress, the azimuthal curvature term, and both axial derivatives remain present.

### 5.1 The exact lift of the manuscript's two-component stress

Proposition 5.5 supplies a pair $\mathcal T=(\mathcal T_\theta,\mathcal T_z)$, supported in its active annulus, with source residual

$$
\mathcal R(u_B,p_B)
=-(\partial_r+2/r)\mathcal T_\theta e_\theta
 -(\partial_r+1/r)\mathcal T_ze_z+E_B. \tag{5.5}
$$

Here the symbols refer to the source equation; the dimensional map (2.2) multiplies the stress by $L_0^2/T_0^2$ and the residual by $L_0/T_0^2$. The source uses this pair to prescribe tangential flux, rather than specifying every entry of a three-dimensional covariance (OpenAI, 2026a, Proposition 5.5; Proposition 7.5).

Define the symmetric tensor lift explicitly:

$$
\mathcal I(\mathcal T)=
\mathcal T_\theta(e_r\otimes e_\theta+e_\theta\otimes e_r)
+\mathcal T_z(e_r\otimes e_z+e_z\otimes e_r). \tag{5.6}
$$

Equation (5.4) proves

$$
\operatorname{div}\mathcal I(\mathcal T)
=(\partial_z\mathcal T_z)e_r
 +(\partial_r+2/r)\mathcal T_\theta e_\theta
 +(\partial_r+1/r)\mathcal T_ze_z. \tag{5.7}
$$

Therefore the full tensor formulation of the source identity is

$$
\boxed{\mathcal R(u_B,p_B)
=-\operatorname{div}\mathcal I(\mathcal T)
 +(\partial_z\mathcal T_z)e_r+E_B.} \tag{5.8}
$$

The radial term is forced by the tensor lift. Deleting it would change the source statement. This is not an error identified in the manuscript: its Proposition 8.1, equation (8.3), already retains the full covariance and the radial mean equation. The additional term makes our symmetric-tensor encoding agree with that source bookkeeping.

For the final averaged field write $\overline U=U_B+m$ and $\overline P=P_B+\delta P$. Define

$$
\mathcal C_B(m,\delta P)=\partial_tm+(U_B\cdot\nabla)m
 +(m\cdot\nabla)U_B+(m\cdot\nabla)m-\nu\Delta m+\nabla\delta P.
$$

Combining (5.3) and the physical-unit version of (5.8) yields the exact residual bookkeeping

$$
\boxed{\overline f=E_B+(\partial_z\mathcal T_z)e_r+
\mathcal C_B(m,\delta P)+\operatorname{div}[\Sigma-\mathcal I(\mathcal T)].} \tag{5.9}
$$

The source's wave and mean corrections control these terms in its construction. Equation (5.9) preserves the complete mechanism for gravitational transport rather than retaining only a blowup rate.

### 5.2 The positive-semidefinite completion has an unavoidable diagonal cost

At a point prescribe $T=(\mathcal T_\theta,\mathcal T_z)\in\mathbb R^2$. Every positive-semidefinite matrix $\Sigma$ whose $r\theta$ and $rz$ entries equal this pair satisfies

$$
\operatorname{tr}\Sigma\ge2\sqrt{\mathcal T_\theta^2+\mathcal T_z^2}. \tag{5.10}
$$

To prove this for $T\ne0$, set $s=|T|$ and $n=T/s$. Write $\Sigma$ in radial/tangential blocks $\left(\begin{smallmatrix}a&T^{\mathsf T}\\T&B\end{smallmatrix}\right)$. Positivity on the span of the radial vector and $n$ implies $a+n^{\mathsf T}Bn\ge2s$, while $\operatorname{tr}B\ge n^{\mathsf T}Bn$. Equality is attained by

$$
\Sigma_{\min}=
\begin{pmatrix}s&T^{\mathsf T}\\T&TT^{\mathsf T}/s\end{pmatrix}
=\begin{pmatrix}\sqrt s\\T/\sqrt s\end{pmatrix}
\begin{pmatrix}\sqrt s&T^{\mathsf T}/\sqrt s\end{pmatrix}. \tag{5.11}
$$

For $T=0$, choose the zero matrix. The piecewise map is continuous, but its smoothness at a zero of $T$ is not assumed. This is a pointwise algebraic completion, not a replacement for the source's smooth two-wave realization or its polarization and support restrictions.

The lower bound makes the energy channel explicit: a nonzero tangential flux cannot be carried by a covariance with zero diagonal energy. The minimally required fluctuation kinetic-energy density is $\rho_0|T|$. The source's leading stress scale $q^{-1-h}$ yields a minimum integrated annular cost of order $\tau^{1/2-2h}$ on a fixed interior similarity subregion with nonzero stress. That is a lower-bound scaling for the required flux, not an upper bound or exact energy of every final pulse.

## 6. Boundary geometry and the Brown–York transport

Use five-dimensional bulk coordinates $(x^0,R,x^1,x^2,x^3)$, with $x^0=ct$, $c>0$, and

$$
\ell=\nu/c,\qquad
 g_0=-\frac{R}{\ell}(dx^0)^2+2dx^0dR+\delta_{ij}dx^idx^j. \tag{6.1}
$$

At $R=\ell$ the induced metric is $\gamma=-(dx^0)^2+dx^idx^i$. The three fluid spatial dimensions have become a four-dimensional timelike boundary; $R$ supplies the fifth bulk dimension. The construction of Bredberg et al. (2012) and its higher-order extension by Compère et al. (2011) use this radial lift. In their coordinates $r=\ell R$, $r_c=\ell^2$, and $\tau_B=x^0/\ell$; their velocity and pressure variables are $v_i^B=\ell U_i/c$ and $P^B=\ell^2P/c^2$.

Fix the bulk signature $(-,+,+,+,+)$ and

$$
R^A{}_{BCD}=\partial_C\Gamma^A{}_{DB}-\partial_D\Gamma^A{}_{CB}
 +\Gamma^A{}_{CE}\Gamma^E{}_{DB}-\Gamma^A{}_{DE}\Gamma^E{}_{CB}.
$$

Let $n$ be the spacelike unit normal toward increasing $R$, and $K_{ab}=\gamma_a{}^A\gamma_b{}^B\nabla_An_B$. Define the stress prescription, without an additive counterterm,

$$
\mathcal C_5=\frac{c^4}{8\pi G_5},\qquad
\mathsf T_{ab}=\mathcal C_5(K\gamma_{ab}-K_{ab}). \tag{6.2}
$$

For four boundary dimensions the inverse is exact:

$$
\boxed{K_{ab}=\frac1{\mathcal C_5}\left(\frac{\mathsf T}{3}\gamma_{ab}-\mathsf T_{ab}\right)},
\qquad \mathsf T=\gamma^{ab}\mathsf T_{ab}. \tag{6.3}
$$

For the seed $K_{00}=-1/(2\ell)$, $K_{ij}=0$, and

$$
p_0=\frac{\mathcal C_5}{2\ell},\qquad \mathsf T_{00}=0,\quad \mathsf T_{ij}=p_0\delta_{ij}.
$$

At the displayed hydrodynamic orders on a flat cutoff,

$$
\begin{aligned}
\mathsf T_{00}&=\frac{p_0}{c^2}|U|^2+\cdots,\\
\mathsf T_{0i}&=-\frac{p_0}{c}U_i+\cdots,\\
\mathsf T_{ij}&=p_0\delta_{ij}+\frac{p_0}{c^2}
[U_iU_j+P\delta_{ij}-\nu(\partial_iU_j+\partial_jU_i)]+\cdots.
\end{aligned} \tag{6.4}
$$

Here the ellipses stand for specified higher hydrodynamic orders, not terms proved to vanish for the OpenAI solution. Equation (6.4) follows from the stress construction in Bredberg et al. (2012); the higher-order content is analyzed in Compère et al. (2011).

### 6.1 The covariance-to-extrinsic-curvature coefficient

Compare the rotational average of (6.4) with (6.4) evaluated on the mean velocity and mean pressure in the same flat boundary data. The fluctuation contribution is

$$
\delta\mathsf T_{00}=\frac{p_0}{c^2}\operatorname{tr}\Sigma,
\quad \delta\mathsf T_{0i}=0,
\quad \delta\mathsf T_{ij}=\frac{p_0}{c^2}\Sigma_{ij}. \tag{6.5}
$$

Its spacetime trace is zero, not its spatial trace. Applying (6.3) therefore gives

$$
\boxed{\delta K_{ij}=-\frac{\Sigma_{ij}}{2\nu c},\quad
\delta K_{00}=-\frac{\operatorname{tr}\Sigma}{2\nu c},\quad
\delta K_{0i}=0.} \tag{6.6}
$$

Thus the exact tensor lift (5.6) sends the two prescribed flux components into the corresponding extrinsic-curvature coefficients with multiplier $-1/(2\nu c)$. Their diagonal completion produces a nonzero time-time coefficient as well. Equations (5.10) and (6.5) give

$$
\delta\mathsf T_{00}\ge\frac{2p_0}{c^2}|T|. \tag{6.7}
$$

This is a coefficient-level map in a specified common boundary metric. Averaging a nonlinear spacetime metric and reconstructing from its averaged stress are not presumed to commute. With a non-axisymmetric metric source, its additional correlations must also be included.

### 6.2 Exact vacuum constraints and an explicit energy-density map

The Gauss–Codazzi equations for an actual Ricci-flat bulk give

$$
D^a\mathsf T_{ab}=0,\qquad
\boxed{\mathsf T_{ab}\mathsf T^{ab}-\frac{\mathsf T^2}{3}
 +\mathcal C_5^2\mathcal R[\gamma]=0}. \tag{6.8}
$$

The second formula follows by substituting (6.2) into $\mathcal R[\gamma]=K^2-K_{ab}K^{ab}$. It remains part of the map; a divergence-free stress alone does not exhaust the gravitational data.

For a stress with a unit timelike Landau vector $u^a$, write

$$
\mathsf T_{ab}=e\,u_au_b+p(\gamma_{ab}+u_au_b)+\pi_{ab},
\quad u^a\pi_{ab}=0,\quad \gamma^{ab}\pi_{ab}=0.
$$

Then (6.8) is exactly

$$
\frac23e^2+2pe+\pi_{ab}\pi^{ab}+\mathcal C_5^2\mathcal R[\gamma]=0. \tag{6.9}
$$

For $p>0$, its branch continuous from the Rindler seed is

$$
e=\frac{-3p+\sqrt{9p^2-6[\pi_{ab}\pi^{ab}+\mathcal C_5^2\mathcal R[\gamma]]}}2. \tag{6.10}
$$

The square root must be real. On a flat boundary and at small dissipative stress this gives $e=-\pi_{ab}\pi^{ab}/(2p)+O(\pi^4/p^3)$; with $\pi_{ab}=-2\eta_s\sigma_{ab}+\cdots$, $e=-2\eta_s^2\sigma_{ab}\sigma^{ab}/p+\cdots$, matching the vacuum-fluid calculation of Compère et al. (2011, §7).

The rest-mass measure in (3.1) and the boundary energy in (6.10) are connected through $(U,P,f)\mapsto\mathsf T\mapsto e$, not through the substitution $e=\rho_0c^2$. This explicit map explains how mass-preserving incompressible motion can feed nontrivial geometric energy and shear data without asserting an infinite-mass particle.

## 7. The force must be included in the curvature map

Use the boundary source metric

$$
\gamma=-(c^2+2\Phi)dt^2+2a_i\,dt\,dx^i+\delta_{ij}dx^idx^j. \tag{7.1}
$$

The symbol $a_i$ is a metric-source covector with units of speed, not acceleration. Its leading nonrelativistic force map is

$$
f_i=-\partial_ta_i-\partial_i\Phi+U^j(\partial_ia_j-\partial_ja_i). \tag{7.2}
$$

Boundary metric forcing is obtained in the relativistic-to-incompressible limit by Bhattacharyya et al. (2009). That paper gives an asymptotically AdS construction. Applying its boundary force identity to the Ricci-flat cutoff setup does not by itself supply a new all-order Ricci-flat solution; the bulk and boundary problems remain specified separately.

The gauge change $a\mapsto a+d\chi$, $\Phi\mapsto\Phi-\partial_t\chi$ leaves (7.2) unchanged by direct differentiation. This is a symmetry of the displayed force map; an exact finite diffeomorphism of a completed bulk metric is not being inferred from it. Choose $\Phi=U\cdot a$. The complete equation is then

$$
(\partial_t+\mathcal L_U)a=-f^\flat,
\qquad (\mathcal L_Ua)_i=U^j\partial_ja_i+a_j\partial_iU^j. \tag{7.3}
$$

For the material flow already used in the mass proof,

$$
a(t)=(X_t^{-1})^*\left[a(0)-\int_0^tX_s^*f^\flat(s)\,ds\right]. \tag{7.4}
$$

This is an exact reconstruction of the leading force equation. In particular, neither the velocity-dependent term nor the derivatives of the inverse material map are omitted.

The Lorentzian signature condition is

$$
c^2+2\Phi+|a|^2=c^2-|U|^2+|U+a|^2>0. \tag{7.5}
$$

It is satisfied in the small-velocity regime. Smoothness of (7.4) for each $T'<T_0$ does not establish uniform smallness or signature at a singular endpoint outside that regime.

### 7.1 The full stress-to-curvature identity

The curvature definition in §6 fixes the exact Codazzi equation

$$
R_{nabc}=D_cK_{ab}-D_bK_{ac}.
$$

Substitution of the inverse Brown–York map gives

$$
\boxed{R_{nabc}=\frac1{\mathcal C_5}
\left[\frac{D_c\mathsf T}{3}\gamma_{ab}-\frac{D_b\mathsf T}{3}\gamma_{ac}
-D_c\mathsf T_{ab}+D_b\mathsf T_{ac}\right].} \tag{7.6}
$$

This identity is exact for an actual hypersurface. At the leading fluid order with (7.1), it yields

$$
R_{n0ij}=-\frac{\partial_i(U_j+a_j)-\partial_j(U_i+a_i)}{2\nu}
+\text{higher fluid and source orders}. \tag{7.7}
$$

The coordinate $0$ denotes $x^0=ct$. With $a=0$, (4.4) makes the supremum of the antisymmetric coefficient unbounded; in detail,

$$
\sup_x\left(\sum_{i<j}|R^{\mathrm{coeff}}_{n0ij}|^2\right)^{1/2}
=\frac{\|\operatorname{curl}U\|_\infty}{2\nu}. \tag{7.8}
$$

For the actual forced correspondence, (7.7), not (7.8), is the relevant coefficient. These mixed components also do not by themselves determine a Lorentzian scalar curvature invariant or geodesic incompleteness.

### 7.2 The exact transported quantity and a useful cancellation

Set $B=\operatorname{curl}(U+a)$ and $\omega=\operatorname{curl}U$. Adding (2.1) to (7.3) in one-form notation and applying exterior differentiation proves

$$
(\partial_t+U\cdot\nabla)B-(B\cdot\nabla)U=\nu\Delta\omega. \tag{7.9}
$$

Using $\det J_t=1$ from mass conservation, the vector solution is

$$
B(t,X_t(a_0))=J_t(a_0)\left[B(0,a_0)+\nu\int_0^tJ_s(a_0)^{-1}
\Delta\omega(s,X_s(a_0))\,ds\right]. \tag{7.10}
$$

For the rest preparation and $a(0)=0$, $B(0)=0$. Divide by the explicit $\nu$ in (7.7): the leading dual curvature vector is

$$
\boxed{-\frac{B(t,X_t(a_0))}{2\nu}
=-\frac12J_t(a_0)\int_0^tJ_s(a_0)^{-1}
\Delta\omega(s,X_s(a_0))\,ds.} \tag{7.11}
$$

The explicit prefactor of viscosity cancels, while the material flow and the vorticity still depend on viscosity. This is an algebraic cancellation within a derived identity, not an assumption of an inviscid model. It specifies exactly what to extract from the released solution for the source-coupled curvature calculation.

The initial value $a(0)$ remains genuine preparation data. Changing it adds the homogeneous transported field to (7.10). The same NS triple need not select the same geometric drive unless this preparation is fixed.

## 8. A quantitative description of the nonuniform limit

Compère et al. (2011, equation 6.3) compute the first linear fourth-spatial-derivative correction. In physical variables its displayed contribution is

$$
-\frac{3\nu^3}{2c^2}\Delta^2U_i. \tag{8.1}
$$

The full sixteen-term displayed correction, the corrected incompressibility equation, and their exact dimensional conversion are retained in `docs/HIGHER_ORDER.md`. The forced pressure identity is $\Delta P+(\partial_iU_j)(\partial_jU_i)=\operatorname{div}f$; it replaces the unforced pressure-elimination step used in that source. The complete curved-boundary forced correction is not obtained by merely appending $f$. The dimensionless ratio of (8.1) to $\nu\Delta U_i$ on a Fourier mode of wavenumber $k$ is

$$
\frac32\left(\frac{\nu k}{c}\right)^2=\frac32(\ell k)^2. \tag{8.2}
$$

Thus the shrinking radial scale $L_r\asymp L_0\tau^{1/2}$ gives a ratio proportional to $\tau^{-1}$ at fixed $\nu,c,L_0$. The exact NS source does not by itself remove this gravity-side correction.

There are nevertheless distinct, explicit simultaneous limits worth calculating rather than conflating.

### 8.1 A fixed-viscosity parabolic dilation

For a fixed $\lambda>0$ define another solution

$$
U_\lambda(x,t)=\lambda U(\lambda x,\lambda^2t),\quad
P_\lambda=\lambda^2P(\lambda x,\lambda^2t),\quad
f_\lambda=\lambda^3f(\lambda x,\lambda^2t). \tag{8.3}
$$

Viscosity is unchanged and terminal time is $T_0/\lambda^2$. Sampling a family at source remaining time $\tau$, choose $\lambda=\tau^a$; this is a family of fixed-$\lambda$ solutions, not a time-dependent substitution into one solution.

For the leading core,

$$
\frac{|U_\lambda|}{c}\asymp\tau^{a-1/2-h},\qquad
\frac{\ell}{L_{r,\lambda}}\asymp\tau^{a-1/2},\qquad
|R^{\mathrm{coeff}}_{n012}|\asymp\tau^{2a-1-h}/(\nu T_0). \tag{8.4}
$$

Taking $a>1/2+h$ makes the first two quantities small, but also sends this flat-source leading curvature coefficient to zero. It does not retain a singular coefficient in that particular family.

### 8.2 A changing-viscosity, approaching-cutoff family

Use instead the exact map (2.3) with $\nu_2=\nu_1\tau^b$, so the spatial dilation factor is $\tau^{b/2}$. Each member has constant positive viscosity; the parameter labels different solutions. Then

$$
\frac{|U_2|}{c}\asymp\tau^{b/2-1/2-h},\quad
\frac{\ell_2}{L_{r,2}}\asymp\tau^{b/2-1/2},\quad
|R^{\mathrm{coeff}}_{n012}|\asymp\frac{\tau^{-b-1-h}}{\nu_1T_0}. \tag{8.5}
$$

For $b>1+2h$, the velocity and radial derivative parameters vanish while this flat-source leading curvature coefficient diverges. Its dimensionless counterpart $\ell_2^2|R^{\mathrm{coeff}}|$ tends to zero like $\tau^{b-1-h}$. This is a consistent coefficient-level scale separation: large dimensionful curvature can coexist with a small curvature measured in a simultaneously shrinking cutoff length.

The same map sends the seed cutoff to $\ell_2=\nu_2/c$ and its acceleration and temperature to

$$
a_{\mathrm{cut}}=\frac{c^2}{2\ell_2},\qquad
T_{\mathrm{cut}}=\frac{\hbar c}{4\pi k_B\ell_2}. \tag{8.6}
$$

They diverge in this family. Thus it does not describe one fixed-temperature background through time. Equations (8.4)–(8.6) retain this change instead of making the two limiting procedures appear identical.

The complete field also contains shorter oscillatory carrier and auxiliary scales; the radial-core estimate alone does not bound all those scales. Nor does it control $a$ in (7.4) or prove convergence of the bulk expansion. Accordingly (8.5) is a computed family of coefficients, not a claim of a uniformly controlled full vacuum solution. The explicit source-coupled target is (7.11).

## 9. The horizon and entanglement interfaces

For a hypersurface-orthogonal null generator $k$ in five bulk dimensions, with $\nabla_kk=\kappa k$, the focusing equation is

$$
k(\theta)-\kappa\theta=-\frac{\theta^2}{3}-\sigma_{AB}\sigma^{AB}-R_{AB}k^Ak^B. \tag{9.1}
$$

The coefficient $1/3$ is the reciprocal of the three-dimensional horizon screen. In vacuum the Ricci term vanishes; shear remains. The membrane derivation connects the incompressible velocity gradient to the leading horizon shear, while its trace gives leading incompressibility (Eling et al., 2009). Equations (3.9) and (4.4) therefore supply the correct fluid inputs for studying concentration of that shear coefficient with a finite integrated dissipation budget. Transporting a complete horizon area or its terminal behavior still requires the actual bulk geometry and generator parametrization.

For the proposed ER = EPR application, the classical path already constructed is

$$
(U,P,f)\longmapsto(\overline U,\Sigma,a)\longmapsto
(\gamma,\mathsf T^{\mathrm{coeff}})\longmapsto(K^{\mathrm{coeff}},R^{\mathrm{coeff}}), \tag{9.2}
$$

with exact averaging and source equations and with the gravitational expansion orders marked. The quantum extension requires a preparation map, not a relabeling of the covariance as entanglement.

A precise test of the information retained by the classical data is available in a finite-dimensional regulator. Let $H|n\rangle=E_n|n\rangle$ and

$$
\rho_\beta=Z^{-1}\sum_ne^{-\beta E_n}|n\rangle\langle n|,
\quad Z=\sum_ne^{-\beta E_n}.
$$

There are two explicit preparation maps:

$$
\rho_\beta\mapsto\rho_{\mathrm{prod}}=\rho_\beta\otimes\rho_\beta,
\qquad
\rho_\beta\mapsto|\mathrm{TFD}\rangle=Z^{-1/2}\sum_ne^{-\beta E_n/2}|n\rangle_L|n\rangle_R. \tag{9.3}
$$

Partial trace of either preparation gives the same $\rho_\beta$ on either side. Hence every one-sided expectation $\operatorname{Tr}(\rho_L\widehat T_{ab})$ and every one-sided covariance agree, while the product preparation has zero mutual information and the pure preparation has mutual information $2S(\rho_\beta)$ when this entropy is nonzero. These are exact maps exhibiting the fibre over one-sided data; they do not assert that both preparations have the same bulk geometry.

The two-sided black-hole interpretation of the thermofield preparation is the established holographic setting of Maldacena (2003); the broader ER = EPR proposal is formulated by Maldacena and Susskind (2013). The Navier–Stokes result constrains the classical coefficient data downstream of a selected preparation. This note has not constructed a state-to-bulk map for the new singular flow or proved the general ER = EPR proposal. The definite physical object to investigate is the source-driven concentration of extrinsic curvature, circulation, and horizon shear given by (5.9), (6.6), and (7.11), with mass conservation already proved.

## 10. Results and reproducibility

The completed downstream analysis supplies: the exact material mass map and exact shrinking-core mass; an energy bound for total viscous dissipation; explicit full-field vorticity and strain lower bounds; the rotational stress projection; the symmetric stress lift with its radial correction; a sharp pointwise diagonal-cost bound; the Brown–York coefficient transport and exact scalar constraint; and the source-coupled curvature transport formula. The two simultaneous limits are evaluated with their different physical parameters retained.

`tests/test_exact.py` checks the encoded algebra, Gaussian integrals, tensor divergences, dimensions, and exponents. `reports/verification.json` records actual execution. Those tests do not certify the external NS proof or the analytic existence of a singular bulk. `lean/AuditUpstream.lean` and the audit script provide the real upstream declarations to replay in a Lean-enabled, networked environment. No local Lean result is represented as having passed.

The current package is directly importable into a Git working tree. It does not require account authentication for its public-source acquisition commands and performs no remote write. The repository access report distinguishes actual browser inspection from unavailable full source bytes.

## References

Bhattacharyya, S., Minwalla, S., & Wadia, S. R. (2009). The incompressible non-relativistic Navier–Stokes equation from gravity. *Journal of High Energy Physics, 2009*(08), 059. doi:10.1088/1126-6708/2009/08/059. arXiv:0810.1545.

Bredberg, I., Keeler, C., Lysov, V., & Strominger, A. (2012). From Navier–Stokes to Einstein. *Journal of High Energy Physics, 2012*(07), 146. doi:10.1007/JHEP07(2012)146. arXiv:1101.2451.

Compère, G., McFadden, P., Skenderis, K., & Taylor, M. (2011). The holographic fluid dual to vacuum Einstein gravity. *Journal of High Energy Physics, 2011*(07), 050. doi:10.1007/JHEP07(2011)050. arXiv:1103.3022.

Eling, C., Fouxon, I., & Oz, Y. (2009). The incompressible Navier–Stokes equations from black hole membrane dynamics. *Physics Letters B, 680*(5), 496–499. doi:10.1016/j.physletb.2009.09.028. arXiv:0905.3638.

Fefferman, C. L. (2000). *Existence and smoothness of the Navier–Stokes equation*. Clay Mathematics Institute. Official Millennium problem statement.

Maldacena, J. (2003). Eternal black holes in anti-de Sitter. *Journal of High Energy Physics, 2003*(04), 021. doi:10.1088/1126-6708/2003/04/021. arXiv:hep-th/0106112.

Maldacena, J., & Susskind, L. (2013). Cool horizons for entangled black holes. *Fortschritte der Physik, 61*(9), 781–811. doi:10.1002/prop.201300020. arXiv:1306.0533.

OpenAI. (2026a). *Finite time blowup for Navier–Stokes* [166-page manuscript]. Released September 8, 2026. Theorem 1.1; equations (3.2), (4.3), (5.41), (10.22)–(10.23), and (B.3); Propositions 5.5 and 7.5; Corollary 10.6.

OpenAI. (2026b). *NavierStokesAndEuler* [Lean source repository]. Inspected September 10, 2026. Repository README, formalization metadata, comparator documentation, and indexed portions of the comparator specification. Revision could not be newly pinned in this environment; an inherited revision is separately labeled in provenance.
