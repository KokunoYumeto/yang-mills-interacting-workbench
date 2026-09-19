# Navier–Stokes concentration and the black-hole interior

## 1. What is being identified

The previous two-sided continuation calculated a cutoff normal-connection observable and its material transport. It did not identify the terminal Navier–Stokes singularity with the spacelike curvature singularity inside the black hole. In particular, a divergent coefficient in a hydrodynamic expansion is not an exact singular metric.

This continuation supplies a radial calculation that was absent: the finite-cutoff, horizon-regular tensor perturbation, its continuation toward the interior singularity, and its first-order contribution to the anisotropic collapse coefficients. The central derived relation is

$$
\boxed{\mathfrak p^{[1]}_{ij}
=-\frac{2\nu}{c^2}S_{ij}
=\frac{\delta\mathsf T^{\mathrm{TF}}_{ij}}{\varepsilon_c+p_c},
\qquad S_{ij}=\frac{\partial_iU_j+\partial_jU_i}{2}.}
\tag{1.1}
$$

Here the superscript \([1]\) means the coefficient obtained by taking the first variation of the metric **before** the interior endpoint limit. It is not a set of finite Kasner exponents obtained by substituting an arbitrarily large Navier–Stokes strain into a nonlinear spacetime. The precise geometric definition is given in Section 6.

The resulting interpretation is an increasingly singular *linear response of the interior collapse data* to the concentrating fluid. The equilibrium geometry already has an interior singularity when the fluid is at rest. Consequently this calculation concerns a deformation of that singularity, not its creation from an initially nonsingular bulk.

OpenAI's manuscript is the source of the forced fluid, not a source of a gravitational identification. Its Theorem 1.1 gives compactly supported smooth forcing, rest initial data, bounded kinetic energy, and unbounded velocity limsup; Theorem 3.1 and Section 10 provide the local growth path and localization near the terminal origin. These are imported mathematical inputs, not an independently replayed Lean certificate (OpenAI, 2026, Theorems 1.1 and 3.1; Proposition 10.1). The earlier project export records the same distinction between the released flow and its downstream workbench observables (project export, lines 2484–2522).

All bulk calculations below use five-dimensional Einstein gravity with the cosmological term retained. The flat-vacuum Rindler theory is reached by an explicit local limit, not identified with the entire two-sided black-brane spacetime.

## 2. The exact background and its two different endpoints

Let \(L,r_h,c>0\), and define

$$
F(r)=\frac{r^2}{L^2}\left(1-\frac{r_h^4}{r^4}\right),
\qquad f(r)=1-\frac{r_h^4}{r^4}.
\tag{2.1}
$$

The metric is

$$
g^{(0)}=-c^2F(r)dt_b^2+\frac{dr^2}{F(r)}
+\frac{r^2}{L^2}\delta_{ij}dx_b^idx_b^j,
\qquad R_{AB}=-\frac4{L^2}g_{AB},\quad\Lambda=-\frac6{L^2}.
\tag{2.2}
$$

This is the planar background of the AdS fluid/gravity construction, with dimensions restored rather than suppressed (Bhattacharyya, Hubeny, Minwalla, & Rangamani, 2008). We use

$$
R^A{}_{BCD}=\partial_C\Gamma^A{}_{DB}-\partial_D\Gamma^A{}_{CB}
+\Gamma^A{}_{CE}\Gamma^E{}_{DB}-\Gamma^A{}_{DE}\Gamma^E{}_{CB}.
\tag{2.3}
$$

Direct contraction, or equivalently the warped-product expression
\(F''{}^2+6(F'/r)^2+12(F/r^2)^2\), gives

$$
\boxed{R_{ABCD}R^{ABCD}=\frac{40}{L^4}+\frac{72r_h^8}{L^4r^8},
\qquad C_{ABCD}C^{ABCD}=\frac{72r_h^8}{L^4r^8}.}
\tag{2.4}
$$

The value at the horizon is \(112/L^4\); it is finite. The divergence is at \(r\downarrow0\), while \(R=-20/L^2\) remains constant. It is Weyl curvature, not an infinite matter density, that distinguishes the interior endpoint in this vacuum solution.

Choose \(r_c>r_h\), set \(f_c=f(r_c)\), and introduce physical cutoff coordinates

$$
t=\frac{r_c\sqrt{f_c}}L t_b,
\qquad x^i=\frac{r_c}{L}x_b^i.
\tag{2.5}
$$

The background embedding is the map

$$
\iota_c:(t,\mathbf x)\longmapsto
\left(\frac{L}{r_c\sqrt{f_c}}t,\ r_c,\ \frac{L}{r_c}\mathbf x\right),
\qquad\iota_c^*g^{(0)}=-c^2dt^2+d\mathbf x^2.
\tag{2.6}
$$

The fluid origin \(\mathbf x=0\) is therefore not the equation \(r=0\). Under this embedding, the candidate fluid endpoint \((T,0)\) is at the cutoff. This coordinate fact does not exclude nonlocal holographic encoding of interior information; it excludes treating the radial and fluid coordinates as the same coordinate.

There is, nevertheless, an explicit causal endpoint assignment. Define

$$
r_*(r)=\frac{L^2}{4r_h}\log\left|\frac{r-r_h}{r+r_h}\right|
+\frac{L^2}{2r_h}\arctan\frac r{r_h}-\frac{\pi L^2}{4r_h},
\qquad\frac{dr_*}{dr}=\frac1F,
\tag{2.7}
$$

and \(v=t_b+r_*/c\). Then

$$
g^{(0)}=-c^2Fdv^2+2c\,dv\,dr+\frac{r^2}{L^2}d\mathbf x_b^2.
\tag{2.8}
$$

The curves with fixed \((v,\mathbf x_b)\) and tangent \(-\partial_r\) are affinely parametrized ingoing null geodesics. Indeed \(g_{rr}=0\), \(g_{vr}=c\) is constant, and \(\Gamma^A{}_{rr}=0\). With \(r=r_c-\lambda\), they reach the singular endpoint at finite affine parameter \(\lambda=r_c\).

Let \(\mathscr E_0\) denote the set of ideal endpoints of this specified congruence, labelled by \((v,\mathbf x_b)\). This notation does not claim a smooth metric extension at those endpoints. The map is

$$
\boxed{\mathcal E_c(t,\mathbf x)=
\left(v=\frac{L}{r_c\sqrt{f_c}}t+\frac{r_*(r_c)}c,
\ \mathbf x_b=\frac L{r_c}\mathbf x;\ r\downarrow0\right).}
\tag{2.9}
$$

Thus the shrinking fluid region can be assigned a shrinking region of labels on the interior endpoint set. However, the same map exists for the resting fluid. It is not itself a singularity-formation theorem. In the full driven geometry the congruence and event horizon would also change; equation (2.9) is the exact background assignment used for perturbation theory.

This distinction is present in the original literature: the spherical fluid/gravity construction discusses a possible fluid singularity as a candidate singularity outside the horizon, assuming control of its expansion, rather than equating it with the background central singularity (Bredberg & Strominger, 2012, Section 5).

### Finite mass does not remove the interior curvature singularity

For a finite periodic quotient with boundary coordinate volume \(V_b\), the background mass is finite:

$$
M=\frac{3c^2r_h^4V_b}{16\pi G_5L^5}.
\tag{2.10}
$$

One derivation uses the pure-AdS-subtracted cutoff energy density
\(\varepsilon_c=3\mathcal C_5(1-\sqrt{f_c})/L\), where
\(\mathcal C_5=c^4/(8\pi G_5)\). The conformal-boundary energy density is
\(\lim_{r_c\to\infty}(r_c/L)^4\varepsilon_c=3\mathcal C_5r_h^4/(2L^5)\), and \(M=\varepsilon_bV_b/c^2\). Without the quotient, the planar solution has finite mass density but infinite total transverse volume. Neither quantity has been identified with the NS material density \(\rho_0\); equation (2.10) is the gravitational stress-to-mass map in the specified background.

## 3. Proper time and the unperturbed interior collapse

Inside the horizon define the remaining proper time for the radial, zero-Killing-energy interior congruence:

$$
s(r)=\frac1c\int_0^r\frac{du}{\sqrt{-F(u)}}
=\frac{L}{2c}\arcsin\frac{r^2}{r_h^2}.
\tag{3.1}
$$

This is a specified congruence, not a formula for the proper time of every possible infaller. With \(\vartheta=2cs/L\), substitution gives the exact interior metric

$$
g^{(0)}=-c^2ds^2+\frac{r_h^2}{L^2}
\left[\frac{\cos^2\vartheta}{\sin\vartheta}c^2dt_b^2
+\sin\vartheta\,d\mathbf x_b^2\right].
\tag{3.2}
$$

Here \(t_b\) is a spacelike direction inside the horizon. As \(s\downarrow0\), the four spatial scale-factor exponents are

$$
(p_w,p_1,p_2,p_3)=\left(-\frac12,\frac12,\frac12,\frac12\right),
\qquad\sum_Ap_A=1,\quad\sum_Ap_A^2=1.
\tag{3.3}
$$

The label \(w\) refers to the interior spacelike direction inherited from exterior time. No component labelled \(w\) is the timelike normal used below. The curvature becomes

$$
R_{ABCD}R^{ABCD}=
\frac{40}{L^4}+\frac{72}{L^4\sin^4(2cs/L)}
\sim\frac9{2c^4s^4}.
\tag{3.4}
$$

### What the local Rindler limit retains

The fixed-viscosity cutoff family of the preceding edition satisfies

$$
\nu=\frac{cLr_c\sqrt{f_c}}{4r_h},\qquad
\frac{r_c^2}{r_h^2}=
\frac{a_L^2+\sqrt{a_L^4+4}}2,
\qquad a_L=\frac{4\nu}{cL}.
\tag{3.5}
$$

For \(L\to\infty\) at fixed \(\nu\), its local near-horizon metric tends to the Rindler seed. Its interior singularity does not remain at a finite value of the proper-time coordinate of this pointed limit. The horizon value is

$$
s_h=\frac{\pi L}{4c}.
\tag{3.6}
$$

At fixed proper time \(\Delta\) below that horizon, put \(s=s_h-\Delta\). Equation (3.4) gives

$$
R_{ABCD}R^{ABCD}
=\frac{40}{L^4}+\frac{72}{L^4\cos^4(2c\Delta/L)}\longrightarrow0.
\tag{3.7}
$$

This explicitly locates the loss of the central singularity in the earlier local vacuum limit. The all-order *formal* Rindler expansion is not a calculation of the entire black-brane interior; it also has higher constitutive corrections to NS (Bredberg et al., 2012; Compère et al., 2011).

## 4. The tensor Einstein equation at finite cutoff

Use ingoing proper-cutoff coordinates \(y^0,\mathbf x\), with \(y^0\) of length dimension. At the cutoff, its constant offset can be chosen so \(y^0=ct\). Write

$$
Q(r)=\frac{r^2}{r_c^2},\qquad
A(r)=Q(r)\frac{f(r)}{f_c},\qquad
D=\frac{L}{r_c\sqrt{f_c}}.
\tag{4.1}
$$

The resting seed has \(g_{00}=-A\), \(g_{0r}=D\), \(g_{ij}=Q\delta_{ij}\). For a unit fluid covector \(u_\mu\), its boosted form is

$$
g^{(0)}=-Q\frac f{f_c}u_\mu u_\nu dy^\mu dy^\nu
+Q(\eta_{\mu\nu}+u_\mu u_\nu)dy^\mu dy^\nu
-2D u_\mu dy^\mu dr.
\tag{4.2}
$$

To extract the tensor coefficient at a chosen boundary event, take the local first-derivative jet

$$
u_0=-1+O(\epsilon^2),\qquad
u_i=\epsilon\sigma_{ij}x^j+O(\epsilon^2),\qquad
\sigma_{ij}=\sigma_{ji},\quad\sigma_{ii}=0.
\tag{4.3}
$$

The coefficient \(\epsilon\) is dimensionless bookkeeping for a first variation; \(\sigma_{ij}\) has inverse-length units. This jet extracts the tensor part of the complete field at that event; it is not an affine replacement for the finite-energy NS solution on all of space.

The metric first variation, including the promoted-velocity pieces, is

$$
\begin{aligned}
h_{0i}&=(A-Q)\sigma_{ij}x^j,\\
h_{ri}&=-D\sigma_{ij}x^j,\\
h_{ij}&=2QH(r)\sigma_{ij}.
\end{aligned}
\tag{4.4}
$$

The radial coefficient is determined by

$$
\boxed{\frac d{dr}\left[r(r^4-r_h^4)H'(r)\right]
=-3Lr_c\sqrt{f_c}\,r^2.}
\tag{4.5}
$$

This equation was checked directly from \(\delta(R_{AB}+4g_{AB}/L^2)\), with all independent tensor components included. For the basis jet \(\sigma=\operatorname{diag}(1,-1,0)\), its only nonzero residuals before imposing (4.5) are

$$
\delta E_{11}=-\frac{\mathcal R_H}{L^2rr_c^2},\qquad
\delta E_{22}=+\frac{\mathcal R_H}{L^2rr_c^2},
\quad
\mathcal R_H=\frac d{dr}\left[r(r^4-r_h^4)H'\right]+3Lr_c\sqrt{f_c}\,r^2.
\tag{4.6}
$$

The physical spatial labels in (4.6) are \(1,2\); the code uses array indices \(2,3\) because its first two entries are \(y^0,r\). Rotations and linearity span every symmetric traceless jet. The test verifies the background and the full first-order Einstein residual of this sector, not the nonlinear Einstein equation for the singular NS field.

Integrating once, regularity at \(r=r_h\) fixes the numerator to vanish there:

$$
H'(r)=-\frac{Lr_c\sqrt{f_c}(r^3-r_h^3)}{r(r^4-r_h^4)}.
\tag{4.7}
$$

The Dirichlet condition \(H(r_c)=0\) fixes the remaining integration constant. Define the dimensionless function

$$
\begin{aligned}
\mathcal F(q)
&=\int_q^\infty\frac{z^3-1}{z(z^4-1)}\,dz\\
&=\frac14\left[
\log\frac{(1+q)^2(1+q^2)}{q^4}-2\arctan q+\pi\right].
\end{aligned}
\tag{4.8}
$$

This is the radial function in Bhattacharyya et al. (2008, equations 4.16–4.20). The finite-cutoff factor and subtraction here follow from (4.5)–(4.7):

$$
\boxed{H(r)=\frac{Lr_c\sqrt{f_c}}{r_h}
\left[\mathcal F(r/r_h)-\mathcal F(r_c/r_h)\right]
=\frac{4\nu}{c}\left[\mathcal F(r/r_h)-\mathcal F(r_c/r_h)\right].}
\tag{4.9}
$$

The integral crosses the horizon without a pole because
\(\mathcal F'(1)=-3/4\). Toward the singularity,

$$
\mathcal F(q)=-\log q+\frac\pi4+\frac{q^3}{3}-\frac{q^4}{4}+O(q^5).
\tag{4.10}
$$

In particular the first regular correction is cubic, not linear. With physical strain \(S=c\sigma\), the explicit tensor metric coefficient is

$$
\boxed{h^{\mathrm T}_{ij}(r,x)
=\frac{8\nu}{c^2}\frac{r^2}{r_c^2}
\left[\mathcal F(r/r_h)-\mathcal F(r_c/r_h)\right]S_{ij}(x).}
\tag{4.11}
$$

The index \(x\) on \(S\) denotes its boundary-event label in the derivative expansion. It does not replace the derivative expansion by an exact spacetime for arbitrary rapidly varying \(S\).

## 5. Forcing and the boundary stress are retained

The source from the previous edition is the metric

$$
\gamma=-(c^2+2\Phi)dt^2+2a_i\,dt\,dx^i+\delta_{ij}dx^idx^j,
\tag{5.1}
$$

with leading force

$$
f_i=-\partial_ta_i-\partial_i\Phi
+U^j(\partial_i a_j-\partial_j a_i).
\tag{5.2}
$$

The metric-forcing limit is established in Bhattacharyya, Minwalla, and Wadia (2009). Choosing \(\Phi=U\cdot a\) gives the exact source-reconstruction equation within that leading force map,

$$
(\partial_t+\mathcal L_U)a=-f^\flat,
\qquad
 a(t)=(X_t^{-1})^*\left[a(0)-\int_0^tX_s^*f^\flat(s)ds\right].
\tag{5.3}
$$

It would be incorrect to set \(a=0\) while keeping the forced NS input. It is equally important not to replace \(S_U\) by the curl of \(U+a\). The symmetric tensor channel behaves differently from the connection's antisymmetric channel.

In the physical coordinate \(y^0=ct\), at the retained weak-source, nonrelativistic order,

$$
u_i=\frac{U_i+a_i}{c},\qquad
\Gamma^0{}_{ij}=-\frac{\partial_i a_j+\partial_j a_i}{2c},
\tag{5.4}
$$

Consequently

$$
\boxed{\nabla_{(i}u_{j)}
=\frac{\partial_i(U_j+a_j)+\partial_j(U_i+a_i)}{2c}
+\Gamma^0{}_{ij}=\frac{S_{ij}}c.}
\tag{5.5}
$$

The metric shift cancels from the *symmetric* shear at this order. It remains present in the source equation and in the antisymmetric connection. Intrinsic source curvature and higher-order constitutive terms are not covered by (5.5).

For the outward spacelike normal at \(r_c\), the complete tensor contribution to extrinsic curvature contains a radial-profile term and a shift term:

$$
\delta K^i{}_j\big|_{r_c}
=\left[\sqrt{F_c}H'(r_c)+\frac1{D\sqrt{F_c}}\right]\sigma^i{}_j
=\zeta_c\sigma^i{}_j,
\quad\zeta_c=\left(\frac{r_h}{r_c}\right)^3.
\tag{5.6}
$$

The shift term must not be discarded simply because the shift itself vanishes at the local-rest event. Its spatial derivative does not vanish. With

$$
\mathsf T_{ab}=\mathcal C_5(K\gamma_{ab}-K_{ab})
+\text{specified intrinsic counterterms},\qquad
\mathcal C_5=\frac{c^4}{8\pi G_5},
\tag{5.7}
$$

the tensor part at this derivative order is

$$
\boxed{\delta\mathsf T^{\mathrm{TF}}_{ij}
=-\frac{\mathcal C_5\zeta_c}{c}S_{ij}
=-2\eta_cS_{ij},\qquad
\eta_c=\frac{c^3\zeta_c}{16\pi G_5}.}
\tag{5.8}
$$

The intrinsic curvature counterterms start at higher derivative order in the local tensor calculation. The background enthalpy is

$$
\varepsilon_c+p_c=\frac{\mathcal C_5\zeta_c c}{2\nu}.
\tag{5.9}
$$

Thus (4.9) has passed a second check: the same radial solution reproduces the finite-cutoff viscous stress with the prescribed physical \(\nu\).

## 6. The geometric calculation at the interior singularity

For \(r<r_h\), put \(A_N=\sqrt{-F(r)}\). Let \(N\) be the future unit timelike normal to the spacelike \(r=\mathrm{constant}\) slices, directed toward decreasing \(r\). Let
\(\mathcal K_{\mu\nu}=\tfrac12(\mathcal L_N g)_{\mu\nu}\) be their second fundamental form. At the unperturbed local-rest event,

$$
\mathcal K^{(0)i}{}_j=-\frac{A_N}{r}\delta^i_j,
\qquad
\mathcal K^{(0)w}{}_w=-\frac{A_N F'}{2F}.
\tag{6.1}
$$

For a diagonal strain jet with eigenvalues \(\sigma_i\), the inverse metric has
\(\delta g^{ri}=\sigma_i x^i/D\). Therefore
\(\partial_i\delta N^i=\sigma_i/(D A_N)\), and

$$
\begin{aligned}
\delta\mathcal K^i{}_i
&=\sigma_i\left[-A_NH'(r)+\frac1{D A_N}\right]\\
&=\sigma_i\frac{r_c\sqrt{f_c}\,r_h^3}
{r^2\sqrt{r_h^4-r^4}},
\qquad\delta\mathcal K^w{}_w=0.
\end{aligned}
\tag{6.2}
$$

This is a geometric eigenvalue calculation, not an identification based solely on reading a logarithm in a coordinate component. The background spatial orthonormal frame \(e_i=(r_c/r)\partial_i\) is parallel along the background radial null rays; it supplies the frame identification between the cutoff tensor and the interior tensor. Spatial rotations diagonalize the arbitrary symmetric strain without changing the coefficient.

Define the response coefficient by

$$
\mathfrak p_A^{[1]}
=-\lim_{r\downarrow0}c\,s(r)
\left.\frac{d}{d\epsilon}\lambda_A(\mathcal K_\epsilon)(r)\right|_{\epsilon=0}.
\tag{6.3}
$$

At each fixed \(r>0\), the first variation is well-defined for sufficiently small \(\epsilon\). The limit in (6.3) is a limit of that coefficient. It neither constructs a nonlinear family through \(r=0\) nor exchanges the limits \(r\downarrow0\) and \(\epsilon\to0\).

Since \(cs(r)\sim Lr^2/(2r_h^2)\), equation (6.2) gives

$$
\boxed{\mathfrak p_w^{[1]}=0,\qquad
\mathfrak p_i^{[1]}=-\frac{Lr_c\sqrt{f_c}}{2r_h}\sigma_i
=-\frac{2\nu}{c^2}S_i.}
\tag{6.4}
$$

Combining (5.8) and (5.9) gives the typed linear map

$$
\delta\mathsf T^{\mathrm{TF}}
\longmapsto \mathfrak p^{[1]}
=\frac{2\nu}{\mathcal C_5\zeta_c c}
\delta\mathsf T^{\mathrm{TF}}
=\frac{\delta\mathsf T^{\mathrm{TF}}}{\varepsilon_c+p_c}.
\tag{6.5}
$$

This ratio is a derived stress-to-collapse response, with the physical enthalpy retained. It is not a choice to set the enthalpy, viscosity, or light speed to one.

### An anisotropic curvature diagnostic

On the local tensor jet, the intrinsic curvature of an \(r\)-slice has no first-order contribution. The Gauss equation with timelike normal gives the leading spatial sectional curvature as products of the shape eigenvalues. Consequently, in the orthonormal \((w,i)\) plane,

$$
\boxed{\lim_{s\downarrow0}c^2s^2\,
\delta R_{\hat w\hat i\hat w\hat i}
=\frac{\nu}{c^2}S_i.}
\tag{6.6}
$$

In particular differences between these sectional coefficients measure
\(\nu(S_i-S_j)/c^2\). These are components in a geometrically specified frame, not a positive sum inferred from an indefinite Lorentzian contraction.

The leading transverse electric tidal coefficient has zero first variation: for a Kasner direction it is \(p_i(1-p_i)\), whose derivative vanishes at \(p_i=1/2\). Likewise the first variation of the leading Kretschmann coefficient vanishes because \(\sum_i\mathfrak p_i^{[1]}=0\). The background scalar diverges, but the *new tensor information* appears first in anisotropic curvature data. It would therefore be wrong to square one growing tensor coefficient and claim that the full scalar invariant has already been computed to that order.

## 7. Transporting the actual NS divergence, without replacing the field

The whole-space result used here concerns the complete smooth, compactly supported preterminal field, not just an axisymmetric leading profile. For any such nonzero divergence-free field \(V\), write
\(E=\|V\|_2\), \(H=\|V\|_\infty\), and
\(M=\|\operatorname{sym}DV\|_{\infty;F}\). The subscript \(F\) is the matrix Frobenius norm.

Let \(G_a(x)=(4\pi a)^{-3/2}\exp(-|x|^2/(4a))\). Integration gives
\(\|G_a\|_2=(8\pi a)^{-3/4}\) and
\(\|\nabla G_a\|_1=2/\sqrt{\pi a}\). Incompressibility yields
\(\Delta V_i=2\partial_jS_{ij}\), hence

$$
V=G_a*V-2\int_0^a\operatorname{div}(G_b*S)\,db,
\qquad
H\le(8\pi a)^{-3/4}E+\frac8{\sqrt\pi}\sqrt a\,M.
\tag{7.1}
$$

Choose the auxiliary smoothing parameter
\(a=[2(8\pi)^{-3/4}E/H]^{4/3}\). This is a choice in an inequality, not a rescaling of the physical solution. It gives

$$
\boxed{\|S\|_{\infty;F}\ge\frac{\pi}{2^{19/6}}
\|V\|_\infty^{5/3}\|V\|_2^{-2/3}.}
\tag{7.2}
$$

Applying the linear map (6.4) gives

$$
\boxed{\|\mathfrak p^{[1]}(t)\|_{\infty;F}
\ge\frac{\pi\nu}{2^{13/6}c^2}
\|U(t)\|_\infty^{5/3}\|U(t)\|_2^{-2/3}.}
\tag{7.3}
$$

The source's complete-field growth path, preserved by localization, supplies constants \(A_*,E_*>0\) with
\(\|U(T_0(1-\tau))\|_\infty\ge A_*\tau^{-1/2-h}\) and
\(\|U(t)\|_2\le E_*\) for sufficiently small positive \(\tau\). The complete construction chooses \(0<h<1/100\); the larger range used for some coordinate identities is not substituted for that construction range (OpenAI, 2026, Theorem 3.1; Sections 9–10).

Thus the response coefficient obeys

$$
\boxed{\|\mathfrak p^{[1]}(T_0(1-\tau))\|_{\infty;F}
\ge\frac{\pi\nu A_*^{5/3}}{2^{13/6}c^2E_*^{2/3}}
\tau^{-5/6-5h/3}.}
\tag{7.4}
$$

Equation (7.4) is a lower bound on a computed linear response coefficient, not a statement that exact Kasner exponents become unbounded.

The endpoint localization can also be made precise. The source's endpoint bounds and exterior heat representation bound derivatives on compact sets avoiding the origin (OpenAI, 2026, Section 10.2). The complete field has fixed compact support. Therefore any sequence of points along which \(\|S\|\) diverges has a subsequence approaching the origin. Under the specified background map (2.9), their endpoint labels approach \((v_*,0)\), where

$$
v_* = \frac{L T_0}{r_c\sqrt{f_c}}+\frac{r_*(r_c)}c.
\tag{7.5}
$$

This concerns a singular neighborhood of the terminal origin. It does not assert that the value \(U(0,t)\) itself is an infinite number, or replace smooth Cartesian axis limits by cylindrical-coordinate artifacts.

## 8. Why the two limits cannot be silently exchanged

There are two distinct limits: \(t\uparrow T_0\), in which the boundary field concentrates, and \(r\downarrow0\), in which the background interior geometry is already singular.

At small \(r\), the relative tensor correction is

$$
Q^{-1}h^{\mathrm T}\sim-\frac{8\nu}{c^2}S\log(r/r_h).
\tag{8.1}
$$

For fixed nonzero strain, its operator norm ceases to be perturbative when
\((8\nu/c^2)\|S\|_{\mathrm{op}}|\log(r/r_h)|\) becomes order one. As NS strain grows, that restriction becomes more severe. At any fixed radial point between the horizon and cutoff, the nonzero kernel (4.11) also amplifies the same strain. There is no calculation here that confines all new loss of control to the pre-existing central singularity.

There is an algebraic test independent of estimating omitted terms. Naively extrapolate the first-order coefficients to

$$
p_w=-\frac12,\qquad p_i=\frac12-\frac{2\nu}{c^2}S_i.
\tag{8.2}
$$

The first Kasner sum remains one, but the second is

$$
\boxed{\sum_Ap_A^2=1+\frac{4\nu^2}{c^4}\sum_iS_i^2.}
\tag{8.3}
$$

For nonzero strain, (8.2) is not an exact vacuum Kasner solution. This does not refute a nonlinear interior response; it proves that the linear relation cannot be promoted to finite exponents by substitution. Second-order constraints and eventually the full nonlinear dynamics must alter the relation.

More generally, real vacuum Kasner exponents in four spatial dimensions obey \(-1/2\le p_A\le1\). For a chosen exponent \(p\), Cauchy–Schwarz on the remaining three gives \((1-p)^2\le3(1-p^2)\), hence the stated interval. Unbounded linear-response coefficients cannot literally become unbounded exact exponents inside this class.

No smoothness of the gravitational source at the terminal time follows merely from smoothness of \(f\): equation (5.3) also contains derivatives of the material map. Likewise \(|U|/c\) and the carrier wavelengths must remain part of the hydrodynamic error estimates. These are concrete limitations of the constructed map, not an argument that fluid singularities cannot have a gravitational interpretation.

## 9. A two-sided observable of the interior deformation

The two-sided state–geometry benchmark is the thermofield preparation for the eternal AdS black hole (Maldacena, 2003). The background singularity and bridge are present before any NS drive. The question that can be tested is how the reconstructed drive changes an interior-sensitive two-sided observable.

For a massive bulk probe with a specified spacelike or complex geodesic saddle \(\Gamma\), the leading exponential contribution is

$$
G_\Gamma\sim A_\Gamma\exp\left[-\frac{mc}{\hbar}\mathcal L_\Gamma\right].
\tag{9.1}
$$

For fixed endpoints and a unit-speed background saddle, the first variation of its length is

$$
\delta\mathcal L_\Gamma=\frac12\int_\Gamma h_{AB}\dot X^A\dot X^B\,d\lambda.
\tag{9.2}
$$

It follows by differentiating the length functional. The path-variation term vanishes by the background geodesic equation and fixed endpoints. Equation (9.2) is invariant under a metric gauge transformation whose generating vector vanishes at the endpoints, provided the complete \(h\) is used.

The tensor-profile contribution from (4.11) is explicit:

$$
\left.\delta\log G_\Gamma\right|_{\mathrm{exponential,T}}
=-\frac{4m\nu}{\hbar c}\int_\Gamma
\frac{r^2}{r_c^2}\left[\mathcal F(r/r_h)-\mathcal F(r_c/r_h)\right]
S_{ij}\dot x^i\dot x^j\,d\lambda.
\tag{9.3}
$$

This is one defined contribution, not the full correlation function. In particular the other two pieces of the local shear jet (4.4) give

$$
\left.\delta\log G_\Gamma\right|_{\mathrm{exponential,jet}}
=-\frac m\hbar\int_\Gamma\left[
(A-Q)S_{ij}x^j\dot y^0\dot x^i
-D S_{ij}x^j\dot r\dot x^i
+QH S_{ij}\dot x^i\dot x^j
\right]d\lambda.
\tag{9.4}
$$

The first two terms cannot be discarded in a complete observable. A varying global NS field also requires its other gradient sectors, boundary source, geodesic deformation, saddle selection, and prefactors. The local-jet response kernel is calculated here; an actual NS-driven, global two-sided propagator has not been evaluated.

A purely radial curve with \(\dot x^i=0\) is blind to this local tensor-jet contribution at first order. A transverse momentum or separation is needed to couple to its strain tensor. This is a concrete selection rule for this response, not a claim that every two-sided probe detects it.

The known interior-sensitive holographic diagnostic also has an essential analytic qualification. Fidkowski, Hubeny, Kleban, and Shenker (2004) show that the singularity-related feature in their heavy-operator correlator appears on a secondary sheet; the naive almost-null real geodesic is not the dominant physical saddle. Their result concerns the specified semiclassical model. It does not justify identifying the real fluid time \(T_0\) with an uncomputed complex-time singularity of the driven correlator.

The map now available is therefore

$$
(U,P,f)\longmapsto S\longmapsto h^{[1]}\longmapsto
\bigl(\mathfrak p^{[1]},\delta R^{[1]}\bigr)
\longmapsto\delta\mathcal L_\Gamma\longmapsto
\left.\delta\log G_\Gamma\right|_{\mathrm{exponential}},
\tag{9.5}
$$

where the first interior arrows are evaluated in the tensor derivative expansion and the last arrows refer to a specified semiclassical saddle. This is not an independent derivation of the holographic dictionary or of general ER = EPR.

## 10. Result and interpretation

The earlier work did not identify the singularities. The present calculation goes inside the black hole and establishes the full radial tensor response, including its regular horizon crossing, logarithmic central behavior, geometric shape-eigenvalue response, anisotropic curvature coefficient, and viscous-stress match.

The strongest justified statement is: the source's concentrated strain has an explicitly divergent image in the **first-order anisotropic data of a pre-existing interior singularity**, under a fixed-viscosity, finite-cutoff Einstein construction. Its origin is assigned to a specified ideal endpoint label through the ingoing congruence. The associated two-sided massive-probe response has an explicit integral kernel.

The stronger statement that the exact NS endpoint *is* the exact black-hole singularity has not been proved. The missing nonlinear identification is visible in the failure of the extrapolated exponents to satisfy (8.3), in the nonuniform logarithm (8.1), and in the fact that the cutoff fluid already probes a geometry with an interior singularity at equilibrium. These calculations identify what the proposed physical correspondence would have to change or preserve, rather than substituting an analogy for it.

## References

Bhattacharyya, S., Hubeny, V. E., Minwalla, S., & Rangamani, M. (2008). Nonlinear fluid dynamics from gravity. *Journal of High Energy Physics, 2008*(02), 045. [Primary manuscript](https://arxiv.org/abs/0712.2456).

Bhattacharyya, S., Minwalla, S., & Wadia, S. R. (2009). The incompressible non-relativistic Navier–Stokes equation from gravity. *Journal of High Energy Physics, 2009*(08), 059. [Primary manuscript](https://arxiv.org/abs/0810.1545).

Bredberg, I., Keeler, C., Lysov, V., & Strominger, A. (2012). From Navier–Stokes to Einstein. *Journal of High Energy Physics, 2012*(07), 146. [Primary manuscript](https://arxiv.org/abs/1101.2451).

Bredberg, I., & Strominger, A. (2012). Black holes as incompressible fluids on the sphere. *Journal of High Energy Physics, 2012*(05), 043. [Primary manuscript](https://arxiv.org/abs/1106.3084).

Compère, G., McFadden, P., Skenderis, K., & Taylor, M. (2011). The holographic fluid dual to vacuum Einstein gravity. *Journal of High Energy Physics, 2011*(07), 050. [Primary manuscript](https://arxiv.org/abs/1103.3022).

Fidkowski, L., Hubeny, V., Kleban, M., & Shenker, S. (2004). The black hole singularity in AdS/CFT. *Journal of High Energy Physics, 2004*(02), 014. [Primary manuscript](https://arxiv.org/abs/hep-th/0306170).

Maldacena, J. (2003). Eternal black holes in anti-de Sitter. *Journal of High Energy Physics, 2003*(04), 021. [Primary manuscript](https://arxiv.org/abs/hep-th/0106112).

OpenAI. (2026). *Finite time blowup for Navier–Stokes* [166-page manuscript]. [Released manuscript](https://cdn.openai.com/pdf/32d9f210-8b73-45e0-91bc-82a30aef8a9a/navier-stokes.pdf).

Project export. (2026). *Branch · Compile Navier Stokes Literature* [Conversation export supplied in this project; updated September 10; lines 2484–2522]. This is a project record, not an independent mathematical publication.
