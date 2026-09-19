*GitHub reading copy; only mathematical delimiters have changed. [Unchanged source](../manuscripts/RESEARCH.md).*

# Vacuum shear response beyond Navier–Stokes

## Result and scope

The singular Navier–Stokes solution is retained as exact mathematical input. The physical question is whether its concentrating sector is embedded in a larger gravitational evolution, what terms that evolution requires, and what its complete observables do near the singular limit. A familiar liquid is not used as an admissibility test.

A concrete calculation is available before solving the complete nonlinear problem. The five-dimensional vacuum-Einstein shear sector has an exact linear response at all temporal and spatial frequencies. Its hydrodynamic pole reproduces both the viscosity and the first fourth-spatial-derivative coefficient retained in the preceding work. At a numerically located pole collision, the two separately divergent modal residues cancel into a finite polynomial times an exponential. No additional dimension beyond the existing gravitational radial direction is needed for this cancellation.

This is a cancellation in an actual linearized gravitational response, not a cancellation of the nonlinear NS velocity divergence. It identifies a mechanism and a calculable physical replacement for the previous freely chosen elliptic stress. The linear response does not retain the cubic high-wavenumber damping used in the previous global-regularity comparator. Consequently that comparator's nonlinear regularity theorem is not transferred to Einstein gravity.

All gravitational formulas below retain physical c, viscosity nu, and G5. Dimensionless variables are introduced only by displayed transformations. Numerical results are multiprecision floating-point calculations, not certified intervals or formal proof certificates. The stated NS input was checked against the public manuscript; its upstream Lean certificate was not rebuilt.

## 1. The singular input and the physical matching question

The released manuscript states a forced incompressible NS construction, for every positive viscosity, from rest, with smooth compactly supported forcing, bounded kinetic energy, and unbounded velocity as the terminal time is approached. Its construction uses oscillatory momentum fluxes to cancel the singular part of the momentum residual. This makes the force smooth without making the velocity bounded (OpenAI, 2026, Theorem 1.1 and section 2.2).

Write its physical equation as

$$
\partial_tU+(U\cdot\nabla)U-\nu\Delta U+\nabla P=f,
\qquad \nabla\cdot U=0.
\tag{1}
$$

The vacuum-fluid correspondence maps NS data to a gravitational expansion with a timelike cutoff; higher-order terms correct the fluid equations rather than leaving them unchanged (Bredberg et al., 2012; Compère et al., 2011). The question pursued here is what the gravitational shear response actually is when a finite gradient truncation is replaced by the full linearized bulk equation.

There are two different perturbations in this statement. The calculation is exact in frequency and wavenumber, but first order in perturbation amplitude about the Rindler seed. It is not a linearization of the entire blowup construction about its concentrating solution.

## 2. The geometry and its exact coordinate map

Put

$$
\ell=\frac{\nu}{c},\qquad \rho_c=2\ell=\frac{2\nu}{c}.
\tag{2}
$$

The static Rindler seed in five spacetime dimensions is

$$
 ds^2=-\left(\frac{\rho}{\rho_c}\right)^2c^2dt^2
       +d\rho^2+dz^2+dy^2+dx_\perp^2,
 \qquad 0<\rho\le\rho_c.
\tag{3}
$$

Its cutoff metric is exactly Minkowski. The map to the preceding ingoing coordinates is

$$
 R=\frac{\rho^2}{4\ell},\qquad
 x^0_{\mathrm{EF}}=ct+\rho_c\log(\rho/\rho_c).
\tag{4}
$$

Substitution gives

$$
 -\frac{R}{\ell}(dx^0_{\mathrm{EF}})^2+2dx^0_{\mathrm{EF}}dR
 =-\left(\frac{\rho}{\rho_c}\right)^2c^2dt^2+d\rho^2.
\tag{5}
$$

Thus no seed or cutoff is changed. The inertial map is also explicit:

$$
 cT=\rho\sinh(ct/\rho_c),\qquad
 X=\rho\cosh(ct/\rho_c).
\tag{6}
$$

The seed is flat vacuum spacetime. The physical cutoff acceleration is c squared divided by rho_c, and its Brown–York pressure, with the outward normal in the increasing-rho direction, is

$$
 C_5=\frac{c^4}{8\pi G_5},\qquad
 p_0=\frac{C_5}{\rho_c}.
\tag{7}
$$

The three boundary spatial directions remain three. The radial direction is a fourth bulk spatial coordinate. Adding radial modes is not adding spacetime dimensions.

## 3. An exact scalar representation of the gravitational shear sector

Take a Fourier component proportional to exp(-i omega t + i k z), polarized along y. In radial gauge let

$$
 A_0=\delta g_{0y},\qquad A_z=\delta g_{zy},\qquad A_\rho=0,
 \qquad x^0=ct,
\tag{8}
$$

and put

$$
 \Omega=\frac{\omega}{c},\qquad
 q=k\rho_c,\qquad w=\frac{\omega\rho_c}{c},\qquad
 \alpha=-iw.
\tag{9}
$$

For this sector, the linearized vacuum equations are the source-free Maxwell equations for the metric perturbation A on the three-dimensional base (x0,z,rho). This is a representation of the gravitational perturbation, not an independently introduced electromagnetic field. Dualizing its field strength in three dimensions gives a scalar phi. The scalar obeys

$$
 \varphi''+\frac1\rho\varphi'
       +\left(\frac{w^2}{\rho^2}-k^2\right)\varphi=0.
\tag{10}
$$

The gauge-invariant vector master equation in this background is given by Marolf and Rangamani (2012, equation 2.14). The following dual representation derives its solution and boundary response.

Choose orientation epsilon_(0 z rho)=+1 and define F_ab=epsilon_(ab c) g^(cd) partial_d phi, where epsilon is the metric volume form. The reconstruction equations are

$$
 A_0'=ik\frac{\rho}{\rho_c}\varphi,\qquad
 A_z'=-i\Omega\frac{\rho_c}{\rho}\varphi,
\tag{11}
$$

$$
 kA_0+\Omega A_z=i\frac{\rho}{\rho_c}\varphi'.
\tag{12}
$$

Their consistency is exactly equation (10). In particular, the vector master field is proportional to rho phi'. If r=rho/rho_c and Z=r partial_r phi, direct substitution proves

$$
 Z''+\frac{q^2r^2+w^2}{r(w^2-q^2r^2)}Z'
        +\left(\frac{w^2}{r^2}-q^2\right)Z=0.
\tag{13}
$$

Primes in (13) mean r derivatives. The apparent singular coefficient at w squared = q squared r squared does not make the scalar representation singular: its numerator obeys

$$
 Z'=(q^2r-w^2/r)\varphi,
\tag{14}
$$

and vanishes at that same turning point. This is one explicitly verified cancellation in the change of master variables. It is unrelated to assuming that the NS blowup is a coordinate artifact.

An ingoing horizon solution is

$$
 \varphi(\rho)=I_{-iw}(k\rho).
\tag{15}
$$

For generic order it behaves as rho to the power -iw near the horizon, and combines with exp(-i omega t) into dependence on the ingoing null coordinate. Analytic continuation defines the retarded solution at exceptional integer orders.

For zero boundary metric source, the physical shear boundary condition is Z(rho_c)=0. Equation (12) converts this Dirichlet condition for the metric master field into a Neumann condition for phi. Consequently the shear frequencies satisfy

$$
 \boxed{F(\alpha,q):=I_\alpha'(q)=0,\qquad \alpha=-iw.}
\tag{16}
$$

The prime in (16) is differentiation with respect to the Bessel argument, not its order. This distinction is essential for all numerical derivatives below.

## 4. The exact boundary response and source convention

Define the dimensionless compliance

$$
 \boxed{H(w,q)=\frac{I_{-iw}(q)}{q I_{-iw}'(q)},\qquad q>0.}
\tag{17}
$$

This is not yet declared to be a fluid velocity propagator. Its physical interpretation follows from the reconstructed Brown–York stress.

For prescribed boundary values A_0c and A_zc, put

$$
 E_c=kA_{0c}+\Omega A_{zc}.
\tag{18}
$$

Equations (11)–(12) give

$$
 A_0'(\rho_c)=E_c\frac{I_\alpha(q)}{I_\alpha'(q)},\qquad
 A_z'(\rho_c)=-\frac{\Omega}{k}E_c\frac{I_\alpha(q)}{I_\alpha'(q)}.
\tag{19}
$$

At linear order, the off-diagonal Brown–York components are

$$
 \delta T^{\mathrm{BY}}_{0y}
 =C_5\left[\frac{A_{0c}}{\rho_c}
    -\frac{E_c}{2}\frac{I_\alpha(q)}{I_\alpha'(q)}\right],
\tag{20}
$$

$$
 \delta T^{\mathrm{BY}}_{zy}
 =C_5\left[\frac{A_{zc}}{\rho_c}
    +\frac{\Omega E_c}{2k}\frac{I_\alpha(q)}{I_\alpha'(q)}\right].
\tag{21}
$$

The first terms are the pressure contact terms. Omitting them changes the source response.

For a metric-shift source A_0c=a/c and A_zc=0, define the momentum variable V_BY=-c delta T_0y/p0. Then the complete linear transfer is

$$
 \boxed{\frac{V_{\mathrm{BY}}}a=-1+\frac{q^2}{2}H(w,q).}
\tag{22}
$$

In the hydrodynamic scaling w of order q squared,

$$
 H(w,q)=\frac{1+O(q^2)}{-iw+q^2/2+O(q^4)},
\tag{23}
$$

and hence

$$
 \frac{V_{\mathrm{BY}}}a
 =\frac{iw}{-iw+q^2/2}+O(q^2).
\tag{24}
$$

The leading metric force is f=-partial_t a, so f=i omega a for this Fourier convention. Equation (24) is the NS response U=f/(-i omega+nu k squared). The exact response (22), however, is a stress-to-metric-source response. It is not obtained by identifying the leading force map with its all-gradient extension.

## 5. Matching the higher-gradient coefficient without fitting it

Use the Bessel series

$$
 I_\alpha(q)=\frac{(q/2)^\alpha}{\Gamma(1+\alpha)}
 \sum_{m=0}^{\infty}\frac{(q^2/4)^m}{m!(1+\alpha)_m}.
\tag{25}
$$

Removing the common factor in q I' gives the implicit equation

$$
 \sum_{m=0}^{\infty}
 \frac{(\alpha+2m)(q^2/4)^m}{m!(1+\alpha)_m}=0.
\tag{26}
$$

The hydrodynamic root has the expansion

$$
 \alpha(q)=-\frac{q^2}{2}-\frac{3q^4}{16}
            -\frac{29q^6}{192}-\frac{2843q^8}{18432}
            -\frac{392029q^{10}}{2211840}+O(q^{12}).
\tag{27}
$$

The first four coefficients are checked by exact rational substitution in the tests. The fifth is retained from the same symbolic recursion. Since w=i alpha and omega=cw/rho_c,

$$
 \boxed{
 \omega=-i\nu k^2
        -i\frac{3\nu^3}{2c^2}k^4
        -i\frac{29\nu^5}{6c^4}k^6+O(k^8).
 }
\tag{28}
$$

The fourth-order coefficient equals the physical coefficient obtained from Compère et al. (2011, equation 6.3). Here it follows from solving the actual linearized gravitational boundary problem. Matching that coefficient alone would not have determined the full response: the earlier tanh-slab comparator is a different function.

The pole, rather than the choice of a hydrodynamic field frame, is used for this comparison. Off-shell higher-order fluid equations can be altered by field redefinitions; their correctly mapped pole cannot.

## 6. The numerically located mode collision

The hydrodynamic branch and another damped branch meet where

$$
 F(\alpha_c,q_c)=0,\qquad
 F_\alpha(\alpha_c,q_c)=0.
\tag{29}
$$

Multiprecision solution gives

$$
 q_c=0.778472800990330076180356446189\ldots,
\tag{30}
$$

$$
 \alpha_c=-0.569714080972361784438457668663\ldots,
 \qquad w_c=-0.569714080972361784438457668663\ldots\,i.
\tag{31}
$$

The computed nondegeneracy coefficients are

$$
 F_q=1.75035806101433995507814928965\ldots,
 \qquad
 F_{\alpha\alpha}=5.00598854867858334954068222753\ldots.
\tag{32}
$$

The local split is

$$
 w_\pm(q)=w_c\pm C\sqrt{q-q_c}+O(q-q_c),
\qquad
 C=\sqrt{\frac{2F_q}{F_{\alpha\alpha}}}
  =0.836244975595942847875560947195\ldots.
\tag{33}
$$

For q just above q_c, the two modes have opposite real frequencies and negative imaginary parts. The local square-root branch is a singularity of the individually labeled eigenvalues as functions of q. It is not a singularity of the real-frequency response H(w,q).

| q | Positive real part of w | Imaginary part of w |
|---:|---:|---:|
| 0.5 | 0 | -0.139933871958 |
| 0.8 | 0.123810900035 | -0.573255787368 |
| 1 | 0.430856069761 | -0.608420333512 |
| 2 | 1.403477397528 | -0.787443246688 |
| 5 | 4.255269907767 | -1.124758392211 |
| 10 | 9.089901053088 | -1.450541475298 |
| 20 | 18.873138576059 | -1.854544479694 |

The computations were repeated at 85 and 110 decimal working precision for the collision. The archived result files record residuals and cross-precision differences. These checks are not a proof of a certified enclosure, a complete enumeration of the spectrum, or a claim that no nearer complex-q singularity limits the hydrodynamic series.

## 7. Divergent residues and their finite joint limit

This is the explicit cancellation calculation. Define dimensionless time

$$
 \vartheta=\frac{ct}{\rho_c}.
\tag{34}
$$

For a simple pole w_j=i alpha_j of H, the residue is

$$
 R_j(q)=\frac{I_{\alpha_j}(q)}{-iq F_\alpha(\alpha_j,q)}.
\tag{35}
$$

The contribution of the pair to the inverse transform, for positive time, is

$$
 K_{\mathrm{pair}}(\vartheta,q)
   =-i\sum_{j=\pm}R_j(q)e^{-iw_j(q)\vartheta}.
\tag{36}
$$

Each residue diverges as the inverse square root of q-q_c. The sum does not.

Write the principal Laurent part of the exact compliance at q_c as

$$
 H(w,q_c)=\frac{A_{-2}}{(w-w_c)^2}
          +\frac{A_{-1}}{w-w_c}+O(1).
\tag{37}
$$

With I and its order derivative evaluated at (alpha_c,q_c), differentiation gives

$$
 A_{-2}=-\frac{2I}{q_c F_{\alpha\alpha}},
\tag{38}
$$

$$
 A_{-1}=\frac{2iI_\alpha}{q_cF_{\alpha\alpha}}
 -\frac{2iI F_{\alpha\alpha\alpha}}
 {3q_c F_{\alpha\alpha}^2}.
\tag{39}
$$

Numerically,

$$
 A_{-2}=-0.584992396521577666707010309129\ldots,
\tag{40}
$$

$$
 A_{-1}=0.989272465485375774845963505140\ldots\,i.
\tag{41}
$$

The double-pole residue theorem therefore proves

$$
 \boxed{
 K_{\mathrm{pair}}(\vartheta,q_c)
 =\big(0.9892724654853758\ldots
       +0.5849923965215777\ldots\,\vartheta\big)
       e^{-0.5697140809723618\ldots\,\vartheta}.
 }
\tag{42}
$$

The exact version of (42) uses (38)–(39), rather than their rounded decimals. It is finite at every nonnegative time and decays at large time. The selected cluster has a maximum approximately 0.9899505829606581 at dimensionless time 0.0641804049091216. This statement concerns the isolated pair contribution, not the complete response including all other poles, analytic terms, or contact terms.

At dimensionless time one, direct computation illustrates the cancellation:

| q-q_c | Magnitude of each separate contribution | Sum of the two contributions |
|---:|---:|---:|
| 10^-4 | 19.7878461160 | 0.890513841355 |
| 10^-8 | 1,978.62287732 | 0.890541410296 |
| 10^-12 | 197,862.286114 | 0.890541413053 |
| 10^-20 | 1,978,622,861.14 | 0.890541413053 |

The limiting sum is 0.890541413053366943423735889253.... Neither modal divergence was set to zero, bounded by fiat, or removed by a cutoff.

There is also an analytic statement independent of the particular decimal values. For an isolated nondegenerate double zero of F, take a contour enclosing its two nearby zeros and no others. On the contour, H is analytic in q and bounded uniformly for q sufficiently near q_c. The contour integral for the pole cluster consequently continues analytically through q_c. If the contour lies strictly in the lower frequency half-plane, its inverse transform has a uniform exponentially decaying bound. This explains why retaining the complete cluster removes the divergence of its individual residues.

At leading local order, the cancellation is the familiar identity

$$
 \frac{e^{-i(w_c+s)\vartheta}-e^{-i(w_c-s)\vartheta}}{2s}
 =-i e^{-iw_c\vartheta}\frac{\sin(s\vartheta)}s
 \longrightarrow -i\vartheta e^{-iw_c\vartheta}.
\tag{43}
$$

Equation (42) additionally retains the simple-pole coefficient that (43) by itself omits.


### Finite clusters of any required multiplicity

The cancellation is not restricted to two modes. If an isolated cluster coalesces into a pole of order m with principal part

$$
 H_{\mathrm{pp}}(w)=\sum_{j=1}^{m}\frac{A_{-j}}{(w-w_c)^j},
 \qquad \operatorname{Im}w_c=-\gamma<0,
\tag{43a}
$$

then its exact retarded contribution is

$$
 \boxed{
 K_{\mathrm{pp}}(\vartheta)=-i e^{-iw_c\vartheta}
 \sum_{j=1}^{m}\frac{A_{-j}(-i\vartheta)^{j-1}}{(j-1)!}.
 }
\tag{43b}
$$

Every finite required m is allowed. A global-in-time bound is

$$
 \sup_{\vartheta\ge0}|K_{\mathrm{pp}}(\vartheta)|
 \le \sum_{j=1}^{m}\frac{|A_{-j}|}{(j-1)!}
 \left(\frac{j-1}{e\gamma}\right)^{j-1},
\tag{43c}
$$

with the j=1 factor interpreted as one. This follows by maximizing each polynomial-exponential term. For an infinite family of clusters, convergence of the corresponding sum of bounds is a sufficient uniform-control condition; it must be proved, not inferred from finite-stage cancellation. A pole-cluster expansion can also have a non-pole remainder, which must be retained. The multiplicity m counts required modes, not extra spatial dimensions.

## 8. Causality and global linear control of this sector

Introduce the tortoise coordinate

$$
 x=\rho_c\log(\rho/\rho_c),\qquad -\infty<x\le0.
\tag{44}
$$

The complete scalar time-domain equation, at fixed transverse Fourier magnitude k, is

$$
 \boxed{
 \frac1{c^2}\partial_t^2\varphi-\partial_x^2\varphi
       +k^2e^{2x/\rho_c}\varphi=0,
 \qquad \partial_x\varphi(t,0)=0.
 }
\tag{45}
$$

This is a causal wave equation, not an instantaneous elliptic constitutive law. Its energy is

$$
 E_k(t)=\frac12\int_{-\infty}^{0}
 \left[c^{-2}|\partial_t\varphi|^2+|\partial_x\varphi|^2
       +k^2e^{2x/\rho_c}|\varphi|^2\right]dx\ge0.
\tag{46}
$$

Integration by parts gives

$$
 \frac{dE_k}{dt}
 =\operatorname{Re}[\partial_t\bar\varphi\,\partial_x\varphi]_{-\infty}^{0}.
\tag{47}
$$

For finite-energy data on the full tortoise half-line with no boundary drive, the self-adjoint nonnegative operator -partial_x squared + k squared exp(2x/rho_c), with Neumann condition at zero, gives a global energy-conserving wave evolution. For a truncated exterior with outgoing flux at its inner end, the exterior energy decreases by that flux. The two descriptions must not be confused: the horizon lies at x=-infinity in these coordinates and a compact signal does not reach it at finite Rindler time.

Smooth compatible finite-energy data have global linear evolution. Spatial Fourier superposition gives the corresponding shear sector for fields in the required Sobolev classes. Boundary sources add the explicit work term at x=0. The positive operator excludes upper-half-plane growing eigenmodes. Damped quasinormal modes are analytically continued scattering resonances, not finite-energy normal modes.

This is a sector statement. Marolf and Rangamani (2012) discuss separate Rindler boundary-graviton subtleties in the scalar/incompressible sector. The shear proof does not establish causal dynamics for every degree of freedom of a rigid-wall gravitational boundary problem.

## 9. Why the previous hyperdissipative theorem does not transfer

At high q, use X=x/rho_c and write w=q+delta q^(1/3). Near the boundary put X=q^(-2/3) eta. The leading equation becomes

$$
 \partial_\eta^2\varphi+2(\delta-\eta)\varphi=0.
\tag{48}
$$

The ingoing Airy combination is Bi(zeta)+i Ai(zeta), with zeta=2^(1/3)(eta-delta). The Neumann boundary condition selects a zero of Ai'. For the continuation of the first pair, the leading large-q form is

$$
 w_+(q)=q+A e^{-2\pi i/3}q^{1/3}+O(q^{-1/3}),
\qquad
 A=\frac{|a'_1|}{2^{1/3}}
 =0.808616517465501814114013381116\ldots,
\tag{49}
$$

where a'_1 is the first negative zero of Ai'. The sign follows from the ingoing wave condition. Large-order Bessel/Airy expansions provide the asymptotic framework (NIST, n.d., sections 10.20 and 10.41); the finite-q numerical table does not rely on using (49) as an exact formula.

Thus

$$
 \operatorname{Re}\omega\sim ck,
\qquad
 -\operatorname{Im}\omega
 \sim\frac{\sqrt3 A}{2}\frac{c}{\rho_c}(k\rho_c)^{1/3}.
\tag{50}
$$

The previous comparator had instantaneous damping proportional to k cubed at high frequency. Equation (50) is not that damping. The all-frequency physical response has propagating modes and a much weaker asymptotic damping exponent. Agreement of the k fourth coefficient in (28) does not identify the two dynamical systems.

The large-q group velocity of the selected branch tends to c, but a group velocity near a pole collision is not a front-velocity theorem. The direct causal statement comes from (45).

## 10. Propagating the actual concentrating core scale

Let the source remaining-time variable be tau=1-t/T0, and retain the physical leading radial core scale

$$
 L_r(t)=L_{r0}\tau^{1/2}.
\tag{51}
$$

The source manuscript supplies this leading scale; it does not imply that every oscillatory wavelength is equal to the core radius (OpenAI, 2026, section 2.1).

At the explicit diagnostic k=1/L_r, the exact background spectral parameter is

$$
 q(t)=\frac{\rho_c}{L_{r0}}\tau^{-1/2}.
\tag{52}
$$

Consequently the spectral crossing occurs at

$$
 \boxed{\tau_c=\left(\frac{\rho_c}{q_cL_{r0}}\right)^2
 =\left(\frac{2\nu}{c q_cL_{r0}}\right)^2.}
\tag{53}
$$

This lies in the preterminal interval only when the displayed value is between zero and one. The corresponding inverse-wavenumber scale is

$$
 \boxed{\frac1{k_c}=\frac{\rho_c}{q_c}
 =2.5691327910952194\ldots\,\frac{\nu}{c}.}
\tag{54}
$$

The wavelength is 2 pi times this value. No wavelength convention is hidden in (54).

Equations (52)–(54) are a background spectral diagnostic. They do not establish that the nonlinear flow follows the instantaneous quasinormal branch. In fact the large-q damping along this frozen-core diagnostic scales as tau to the power -1/6, while the leading core variation rate scales as tau to the power -1. Their ratio is proportional to tau to the power 5/6 and tends to zero. Adiabatic relaxation therefore cannot be assumed at the endpoint. Actual pulse wavevectors and the metric-source derivatives must be propagated independently.

This supplies a quantitative place to change the calculation from a gradient truncation to a driven time-domain bulk evolution. It does not justify suppressing the core at that scale.

## 11. The first nonlinear consistency issue

A pure linear shear polarization is not a complete nonlinear gravitational truncation. This can be seen without guessing a dissipative correction. For a unit-radius spacelike fiber, consider the metric ansatz

$$
 ds^2=g_{ab}dx^a dx^b+(dy+A_a dx^a)^2+dx_\perp^2.
\tag{55}
$$

The fields are independent of y and x_perp in this restricted comparison. The fiber Ricci component is

$$
 R_{yy}=\frac14 F_{ab}F^{ab}.
\tag{56}
$$

For example, the exact metric with A=a(z)dx0 gives R_yy=-(a'(z)) squared /2, while F_ab F^ab=-2(a'(z)) squared. This non-null check is evaluated directly from the Christoffel symbols in the test suite. In general, using the coframe e^y=dy+A and its exterior derivative de^y=(1/2)F_ab e^a wedge e^b gives (56) by the usual curvature contraction.

Thus a generic non-null shear field cannot remain a vacuum solution with fixed fiber radius. Its quadratic backreaction forces additional metric components to evolve. This does not mean another spacetime dimension has to be invented: the radius and base metric components already belong to the five-dimensional metric.

Allowing a radius exp(sigma) gives, up to the appropriate boundary term, the reduced action per coordinate area in the two Killing directions

$$
 S_{\mathrm{red}}=\frac{c^3}{16\pi G_5}\int d^3x\sqrt{-g}
 \left[e^\sigma R[g]-\frac14e^{3\sigma}F_{ab}F^{ab}\right].
\tag{57}
$$

The equality follows by substituting the warped-fiber scalar curvature and integrating its Laplacian term by parts. The base metric and radius are not external sources in (57); they must be varied. This restricted symmetry sector is not the three-coordinate NS solution, but it exposes the first backreaction that would be missed by treating the linear shear response as an exact nonlinear constitutive equation.

For the full NS construction, retain the unrestricted Einstein equations, the cutoff constraints, the reconstructed sources, and all generated channels. Neither (16) nor (57) has solved that nonlinear problem.

## 12. Black-hole radiation rather than a liquid analogy

There is a physical connection between horizon shear and radiation in black-hole mergers. In particular, simulations of head-on mergers identify quadratic modes in horizon shear with amplitudes related to those of the linear modes (Khera et al., 2023). That does not identify a NS axis angular velocity with an observed wave frequency.

A separate four-dimensional Schwarzschild comparator makes the observable map explicit. Let

$$
 r_s=\frac{2G_4M}{c^2},\qquad
 r_*=r+r_s\log(r/r_s-1).
\tag{58}
$$

For odd-parity gauge-invariant perturbations with ell at least two, the Regge–Wheeler potential is

$$
 V_\ell(r)=\left(1-\frac{r_s}{r}\right)
 \left[\frac{\ell(\ell+1)}{r^2}-\frac{3r_s}{r^3}\right].
\tag{59}
$$

The gauge-invariant construction and flux extraction are described by Martel and Poisson (2005). At fixed omega define the sourced radial equation with the explicit sign convention

$$
 \left[\frac{d^2}{dr_*^2}+\frac{\omega^2}{c^2}-V_\ell\right]
 \Psi_{\ell m}(\omega,r_*)=\mathcal S_{\ell m}(\omega,r_*).
\tag{60}
$$

Let X_in be ingoing at the horizon, X_up be outgoing at infinity, and

$$
 W=X_{\mathrm{in}}X'_{\mathrm{up}}-X'_{\mathrm{in}}X_{\mathrm{up}}.
\tag{61}
$$

Then the exact linear radial Green function is

$$
 \boxed{
 G_\ell(\omega;r_*,r_*')
 =\frac{X_{\mathrm{in}}(r_<)X_{\mathrm{up}}(r_>)}{W(\omega)}.
 }
\tag{62}
$$

Its derivative jump is one. If X_up is normalized to unit outgoing amplitude, the far-zone amplitude is

$$
 \boxed{
 \Psi_{\ell m}^{\infty}(\omega)
 =\frac1{W(\omega)}\int X_{\mathrm{in}}(\omega,r_*')
                  \mathcal S_{\ell m}(\omega,r_*')\,dr_*'.
 }
\tag{63}
$$

Initial-data and boundary-source terms can be included with the same Green identity. Equation (63) is the missing type of map between a concentrating gravitational sector and a waveform: it retains propagation, barriers, mode poles, and the actual source overlap. In vacuum perturbation theory the first-order source can be zero, with radiation encoded in initial data; at second order, quadratic gravitational terms generate an effective source. It must not be replaced by an arbitrary matter source while still calling the same equation vacuum.

For ell at least two, V_ell is nonnegative outside the horizon, giving a positive linear master-field energy. This controls the linear exterior problem, not the nonlinear merger interior.

The four-dimensional radiation example is not silently equated with the five-dimensional Rindler construction. A dimensional-reduction or brane map would be required to make that identification. No such map or NS-specific waveform has been produced here. The source data and gauge-invariant gravitational initial data necessary for that step remain part of the research target.

## 13. Inflow, topology, and the stopping condition for extension

The anomaly-inflow condition remains an independent equation on the full quantum theory: the boundary anomaly theory must pair with its inverse bulk theory. Eta-invariant formulations retain both local and global anomaly information (Witten & Yonekura, 2019). Nothing in the Bessel collision above is asserted to be an FHLT anomaly.

The distinction is productive. A mode label becomes singular at a pole collision, while the complete response remains finite. The first completion therefore consists of retaining the mode cluster already present in one radial direction. The next nonlinear step retains metric components sourced by quadratic shear. An additional physical dimension is justified only if the complete anomaly or dynamical matching problem requires it, not by the number of divergent terms in a chosen expansion.

For a proposed nonlinear completion, retain three separate tests: cancellation of the specified anomaly; satisfaction of Einstein and boundary constraints; and control of stated physical-frame observables. Trivializing one of these quantities does not trivialize the others.

## 14. What has and has not been established

The explicit output is an all-frequency linear gravitational response, its source-to-stress map, its exact hydrodynamic coefficient comparison, a numerically located spectral collision, and an analytic cancellation of divergent modal contributions into a finite joint response. The positive wave energy gives global linear control in the specified sector. The actual physical response also demonstrates why the preceding hyperdissipative regularity theorem cannot be relabeled as an Einstein regularity theorem.

The NS divergence remains part of the input. It has not been shown to coincide with the spectral-residue divergence calculated here. The complete source-dependent nonlinear bulk metric, its terminal curvature, its global topology, and a specific observable merger waveform have not been reconstructed. These are concrete missing maps, not an assertion that the mathematics or the singularity is meaningless.

## References

Bredberg, I., Keeler, C., Lysov, V., & Strominger, A. (2012). From Navier–Stokes to Einstein. *Journal of High Energy Physics, 2012*(7), 146. arXiv:1101.2451.

Compère, G., McFadden, P., Skenderis, K., & Taylor, M. (2011). The holographic fluid dual to vacuum Einstein gravity. *Journal of High Energy Physics, 2011*(7), 050. arXiv:1103.3022.

Khera, N., Ribes Metidieri, A., Bonga, B., Jiménez Forteza, X., Krishnan, B., Poisson, E., Pook-Kolb, D., Schnetter, E., & Yang, H. (2023). Nonlinear ringdown at the black hole horizon. *Physical Review Letters, 131*(23), 231401. arXiv:2306.11142.

Marolf, D., & Rangamani, M. (2012). Causality and the AdS Dirichlet problem. *Journal of High Energy Physics, 2012*(4), 035. arXiv:1201.1233.

Martel, K., & Poisson, E. (2005). Gravitational perturbations of the Schwarzschild spacetime: A practical covariant and gauge-invariant formalism. *Physical Review D, 71*(10), 104003. arXiv:gr-qc/0502028.

National Institute of Standards and Technology. (n.d.). *Digital Library of Mathematical Functions*, sections 10.20 and 10.41. Online reference accessed September 11, 2026.

OpenAI. (2026). *Finite time blowup for Navier–Stokes* [166-page manuscript]. Theorem 1.1 and sections 2.1–2.2.

Witten, E., & Yonekura, K. (2019). *Anomaly inflow and the eta-invariant* [Preprint]. arXiv:1909.08775.
