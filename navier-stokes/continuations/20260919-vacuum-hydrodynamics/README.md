# Vacuum hydrodynamics: constraint encoding and gravitational shear response

This continuation develops two explicit connections between incompressible velocity data and five-dimensional gravity. One constructs exact nonlinear Einstein initial data from a complete compact velocity field and recovers that field by a left inverse. The other calculates the linear gravitational shear response of a Rindler cutoff at arbitrary nonzero spatial frequency, including a finite combined response when two modal residues diverge. A separate positive-stress comparator gives global smoothness for a modified fluid equation.

These are complementary constructions with different equations and domains. The nonlinear initial-data construction has cosmological constant $\Lambda=-6/L^2$; the Rindler seed is Ricci flat. The explicit fixed-viscosity local limit connecting their background geometries is in the [two-sided predecessor, §3](archive/er-epr-continuation/docs/ER_EPR_CONTINUATION.md). That limit does not identify their complete nonlinear solutions or retain the global interior geometry.

## Read the mathematics

| Paper | What it contains |
| --- | --- |
| [The gravitational identity carried by Navier–Stokes strain](readers/IDENTITY_AND_COMPLETION.md) | Conserved radial tensor, nonlinear Kasner map, exact homogeneous Einstein metric, compact TT lift, scalar constraint existence and uniqueness, complete-velocity decoder, evolution defect and probe functional. |
| [Vacuum shear response beyond Navier–Stokes](readers/RESEARCH.md) | Scalar representation of the Rindler shear sector, Brown–York source response, Bessel poles, hydrodynamic coefficients, pole-cluster cancellation, wave energy and nonlinear backreaction. |
| [Positive slab stresses, stratification and their precise comparison maps](SLAB_COMPARATORS.md) | The distinct regularity result from the earlier literature branch, its layered generalization, preterminal NS comparison and anomaly-inflow scope. |
| [Navier–Stokes concentration and the black-hole interior](readers/INTERIOR_CONTINUATION.md) | The horizon-regular first-order radial calculation on which the nonlinear completion builds. |
| [Two-sided quantum and geometric response](readers/ER_EPR_CONTINUATION.md) | Normal-frame connection, thermal spectral kernel, loop observable, fixed-viscosity geometry limit and regulated operator identification. |
| [Vacuum propagation](readers/PROPAGATION.md) and [higher-order terms](readers/HIGHER_ORDER.md) | Source-coordinate maps, full-field interpolation estimates, averaged stress, geometric force, and the complete displayed higher-order comparison. |
| [Initial vacuum-hydrodynamics note](readers/RESEARCH_NOTE.md) | Historical starting calculation; later papers refine its source range and qualifications. |

The two supplied manuscripts and five predecessor mathematical documents are preserved byte for byte. The linked reading copies change only mathematical delimiters for GitHub rendering, not equations or prose; each links its unchanged source. The [reading-copy manifest](readers/manifest.json) records both identities, and `python build_github_readers.py --check` verifies the conversion. Their historical reports of software checks describe earlier packages. The latest packages' code, test programs and numerical result files were not supplied with these manuscripts. Current reproduction is limited to the small independent [check program](verify_recovered_formulas.py) and the review described below; it does not claim to reproduce those historical suites.

## Exact nonlinear encoding of a complete velocity snapshot

Fix positive physical parameters $\nu,c,L$, a marked Euclidean three-plane $E$, and
$\mathscr U=C^\infty_{c,\mathrm{div}=0}(\mathbb R^3;\mathbb R^3)$.
Choose $b\in C_c^\infty(\mathbb R)$ with $b(0)=0,b'(0)=1$. For $V\in\mathscr U$, let $S_V=(DV+DV^T)/2$. The four-dimensional symmetric tensor

$$
(\mathscr L_bV)_{ij}=b'S_{V,ij},\qquad
(\mathscr L_bV)_{wi}=-\frac b2\Delta V_i,\qquad
(\mathscr L_bV)_{ww}=0
$$

is compactly supported, tracefree and divergence free. The mixed component cancels the transverse residual $b'\Delta V_i/2$; its squared norm is
$b'^2|S_V|^2+b^2|\Delta V|^2/2$. These are exact differential identities.

For a fixed reference phase $0<\vartheta_*<\pi/2$, set

$$
a_*=(L\sin\vartheta_*)^{-1},\quad
\tau_*=-4L^{-1}\cot\vartheta_*,\quad
\kappa_*=12a_*^2,\quad \beta_*=8a_*\nu/c^2,
$$
$$
\bar A=-a_*\operatorname{diag}(-3,1,1,1)+\beta_*\mathscr L_bV,
\qquad q=|\bar A|^2\ge\kappa_*.
$$

There is a unique positive smooth solution

$$
-6\Delta_4\phi+\kappa_*\phi^3-q\phi^{-5}=0,
\qquad \phi\to1\quad\text{at infinity}.
$$

Indeed $q-\kappa_*$ is smooth, nonnegative and compactly supported; the constants $1$ and $(\|q\|_\infty/\kappa_*)^{1/8}$ are ordered barriers. Monotone Dirichlet solves on expanding balls, interior elliptic compactness, and comparison with $(-6\Delta+3\kappa_*)^{-1}(q-\kappa_*)$ prove existence and decay. Strict monotonicity of the scalar nonlinearity proves uniqueness. No small-amplitude hypothesis enters this argument.

The output

$$
h=\phi^2\delta,\qquad
K=\phi^{-2}\bar A+(\tau_*/4)\phi^2\delta
$$

solves the four-spatial-dimensional vacuum constraints with $\Lambda=-6/L^2$. The conformal powers and divergence law agree with [Choquet-Bruhat, Isenberg and Pollack, §2](https://arxiv.org/html/gr-qc/0610045v2); the supplied paper verifies the cosmological coefficients directly.

At the marked plane $w=0$, the volume-weighted three-dimensional tracefree block recovers strain:

$$
\beta_*^{-1}\phi^4\operatorname{TF}_E(K^\sharp)=S_V.
$$

The Newton decoder $\mathcal N(S)_i=2\Delta^{-1}\partial_jS_{ij}$, with the decaying inverse on $\mathbb R^3$, recovers $V$ exactly. If the cutoff-to-reference coordinate scale is $d>0$, its vector-field pushforward is $\mathcal P_dU(\xi)=dU(\xi/d)$. Hence

$$
\mathcal E_{b,d}=\mathcal C_b\mathcal P_d:\mathscr U\to\mathsf{Constr}_{-6/L^2},
\qquad
\mathcal D_{b,d}=\mathcal P_d^{-1}\mathcal N\mathcal R_*:
\operatorname{im}\mathcal E_{b,d}\to\mathscr U,
\qquad \mathcal D_{b,d}\mathcal E_{b,d}=\mathrm{id}.
$$

This is injectivity for marked initial data, including the Euclidean reference structure and distinguished plane used by the decoder. It does not assert injectivity after forgetting that structure or quotienting by arbitrary diffeomorphisms.

## Homogeneous realization, radial response and evolution

For a constant tracefree symmetric strain $S$, define

$$
\mathcal B=-2\nu S/c^2,\quad
\chi=\sqrt{1+\tfrac43\operatorname{tr}\mathcal B^2},\quad
P_w=\tfrac14-\tfrac3{4\chi},\quad
P_\perp=\tfrac14I_3+(I_3/4+\mathcal B)/\chi.
$$

Then $\operatorname{tr}P=\operatorname{tr}P^2=1$. These data define the explicit homogeneous Einstein metric in the [identity paper, (4.2)](manuscripts/IDENTITY_AND_COMPLETION.md). Its marked spatial volume is $\chi$ times the background volume, and the inverse is

$$
S=-\frac{c^2}{2\nu}
\frac{3P_\perp+(P_w-1)I_3}{1-4P_w}.
$$

This is a smooth bijection onto the block Kasner sector $P_w<1/4$. Its derivative at zero matches the ordered first-order radial response $\mathfrak p^{[1]}=-2\nu S/c^2$. The radial equation provides the conserved tensor

$$
\mathcal J=[r(r^4-r_h^4)H'+Lr_c\sqrt{f_c}\,r^3]S/c,
\quad \partial_r\mathcal J=0,
$$

whose boundary and interior evaluations give $\mathfrak p^{[1]}=\delta T^{\mathrm{TF}}/(\varepsilon_c+p_c)$. The equality uses the specified frame, normal orientation, horizon condition and order of differentiation and endpoint limit. Its source construction is [Bhattacharyya et al., (4.16)–(4.20)](https://arxiv.org/abs/0712.2456).

The opposite endpoint of the homogeneous family has exponents $I_4/2-P$ and is singular for every nonzero $S$. The family realizes the response derivative; it is not a globally horizon-regular completion of the forced boundary solution. Its homogeneous constraint solution $\phi=\chi^{1/4}$ solves the scalar differential equation, with a different far-field value. It arises as a smooth local limit of compact-input solutions with far-field value one; their velocity $L^2$ norm grows as $R^{5/2}$.

Each compact-input datum has a maximal globally hyperbolic Einstein development, unique up to the isometries preserving its initial embedding, by the general-dimensional Cauchy theory described in [Sbierski, §2, Theorem 2.8](https://arxiv.org/html/1309.7591v3). An NS snapshot label is a parameter of this construction. Inserting it as spacetime time with zero shift produces the exact defect

$$
\operatorname{TF}_h(\partial_t h-2cNK)
=-2cN\phi^{-2}\bar A\ne0\qquad(N>0),
$$

because $\bar A_{ww}=3a_*>0$. A claimed conjugacy of NS and Einstein evolution would need a further evolution map. For Gaussian Einstein evolution the actual anisotropy balance is $\partial_\lambda(VE)=-V\operatorname{Ric}(h)^{\mathrm{TF}}$.

The manuscript's $\mathsf{SolNS}_\nu$ domain must therefore mean smooth solutions with evaluated snapshots in $\mathscr U$. Differentiating the constraint solve also requires a smooth curve in appropriate decaying function spaces; smooth time dependence with locally common compact support is a sufficient setting. The source-dependent blowup estimates remain imported hypotheses from the existing [NS research state](../../RESEARCH_STATE.md). This integration neither rebuilds nor independently certifies the upstream construction.

## Exact linear Rindler response and finite pole clusters

Set $\rho_c=2\nu/c$, $q=k\rho_c>0$, $w=\omega\rho_c/c$ and $\alpha=-iw$. Linear shear perturbations of the Rindler seed are represented by

$$
\varphi''+\rho^{-1}\varphi'+(w^2/\rho^2-k^2)\varphi=0,
\qquad \varphi=I_{-iw}(k\rho).
$$

The no-source metric boundary condition becomes $I'_{-iw}(q)=0$, where the prime differentiates the argument. The dimensionless compliance and Brown–York momentum response to a metric shift are

$$
H(w,q)=\frac{I_{-iw}(q)}{qI'_{-iw}(q)},\qquad
V_{\mathrm{BY}}/a=-1+(q^2/2)H(w,q).
$$

The contact term is part of the source-to-stress map. The scalar representation matches [Marolf and Rangamani, (2.14)](https://arxiv.org/html/1201.1233v3). Its pole has physical expansion
$\omega=-i\nu k^2-i(3\nu^3/2c^2)k^4-i(29\nu^5/6c^4)k^6+\cdots$, agreeing with the fourth-order coefficient in [Compère et al., (6.3)](https://arxiv.org/html/1103.3022v2).

The collision near $q_c=0.77847280099033007618$, $\alpha_c=-0.56971408097236178444$ is a multiprecision numerical result. An isolated nondegenerate double zero gives a pole-cluster contribution

$$
K_{\mathrm{pair}}(\vartheta,q_c)=(-iA_{-1}-A_{-2}\vartheta)e^{\alpha_c\vartheta},
\qquad \vartheta=ct/\rho_c,
$$

with $A_{-2}\approx-0.5849923965215777$, $A_{-1}\approx0.9892724654853758i$. The analytic finite-limit theorem applies to an isolated nondegenerate double zero; the decimal location is not interval certified. More generally an isolated pole of finite order $m$ contributes a polynomial of degree $m-1$ times a decaying exponential. An infinite expansion needs summability and its non-pole remainder.

The tortoise-coordinate wave operator has nonnegative potential $k^2e^{2x/\rho_c}$ and a positive conserved energy for the homogeneous Neumann problem. This gives global linear shear evolution for compatible finite-energy data. Driven data retain their boundary-work term. The large-$q$ Airy formula is an asymptotic calculation with numerical support; this note does not establish a uniform remainder estimate or a global spectral branch classification. The homogeneous spatial mode needs separate treatment from the displayed $q>0$ formula.

Thus the finite cancellation concerns modal residues of a linear response, not the nonlinear NS velocity norm. Generic nonlinear shear also sources $R_{yy}=F_{ab}F^{ab}/4$, requiring radius and base-metric backreaction. The [slab comparator](SLAB_COMPARATORS.md) has cubic high-frequency damping; this Rindler branch has a different propagating spectrum. Its regularity theorem cannot be transferred by matching one coefficient.

## What was recovered relative to the existing workbench

Comparison used repository commit `143f6773feb424ad9ed3a8d116653200f20346b7`, the complete standalone NS TeX, all 82 text members of its 120-member source archive, the NS research state, and the readable S6 source/guide/attempt files. The exact archive SHA-256 and source identities are recorded in [provenance](provenance.json).

| Recovered result | Relationship to that baseline |
| --- | --- |
| Original NS coordinates, nonlinear averaging, corrections, forcing and concentration input | Already the subject of the 208-page NS reconstruction. Retained as input and linked to its existing validation status. |
| Geometric force transport, Brown–York covariance, explicit interpolation estimates, two-sided normal-connection and operator maps | Additional constructions recovered from the predecessor papers; absent from the compared NS mathematical bodies. |
| Conserved radial tensor and nonlinear Kasner/volume completion | Additional gravitational calculation; neither its formulas nor a corresponding theorem occurs in the compared bodies. |
| Compact TT lift, nonlinear constraint solve and complete-velocity left inverse | Additional exact marked-data construction, independent of any blowup theorem. |
| Rindler Bessel response, hydrodynamic series and finite pole-cluster response | Additional linear gravitational analysis, with numerical and asymptotic qualifications retained. |
| Stratified and recursive slab response with global smoothness of its modified boundary PDE | Distinct recoverable theorem in the second conversation, not contained in the supplied spectral manuscript; reconstructed in the companion with its proof. |
| General ER = EPR, an NS-time Einstein conjugacy, cancellation of nonlinear NS blowup, or an S6 implication | No such theorem or requisite map is supplied. No S6 edge was identified in the inspected material; this is a routing conclusion, not a proof that none can exist. |

The source archive comparison found no occurrences of the distinctive Kasner, Rindler, Brown–York, Lichnerowicz, Einstein, anomaly/inflow or Bessel constructions in any of its 82 text members. The comparison does not claim a literature-wide novelty result or an exhaustive audit of every historical S6 archive member.

## Verification and provenance

The current review checked the TT identities, four-dimensional conformal powers, scalar barrier proof, Newton decoder, homogeneous specialization and evolution defect directly. A fresh independent symbolic calculation verified all five displayed hydrodynamic series coefficients through $q^{10}$, and a fresh multiprecision calculation reproduced the collision and Laurent data. Run `python verify_recovered_formulas.py` with `sympy` and `mpmath` to repeat the compact algebra and numerical checks. They are finite checks, not a PDE existence proof or formal certificate.

Historical reports of 60 symbolic assertions and 21 numerical checks for the identity package, and 19 test methods for the spectral package, were not replayed: their latest code was not among the recovered files. The preceding interior ZIP was found locally and preserved privately in full. Only its mathematical reading documents are included here. Private conversation exports, account links and executable task instructions are not part of this public reader.

This continuation belongs to the Navier–Stokes topic because its defined maps start with divergence-free velocity, strain, metric sources or the associated gravitational shear response. It makes no new claim about S6 complex structures or the Yang–Mills mass gap.

[Navier–Stokes workbench](../../README.md) · [Research state](../../RESEARCH_STATE.md)
