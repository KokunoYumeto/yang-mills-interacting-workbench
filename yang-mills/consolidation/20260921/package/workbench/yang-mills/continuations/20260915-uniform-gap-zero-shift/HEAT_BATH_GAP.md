# Full-domain gap through the actual vacuum conditionals

15 September 2026. This is the final quantitative strengthening in the present
continuation. It uses the exact original plaquette coefficient O1–2 and the
same convergent labelled source, but returns its information to the original
Hamiltonian through conditional variances. All operators below act on the
actual finite-vacuum Hilbert space. Every link, physical coefficient, vacuum
factor and scalar ground energy remains those of U3–4.

The completed domain is

    g^2>=15,  0<xi=1/(4g^4)<=1/900,  a>0, L>=2.           (H1)

There is no assumption about an unevaluated gap in this domain. The argument
below proves the full physical estimate, the zero-shift inverse bound and the
spatial-volume return with explicit constants.

## H2. The same exact source converges on this larger closed domain

Use w=5/4, B_xi=(625/8)xi and the bilinear coefficient bound 8/3 from O3–6.
Take the fixed radius R_15=9/64. At the endpoint xi=1/900,

    B_xi+(8/3)R_15^2=25/288+27/512=643/4608
                          <648/4608=R_15,
    (16/3)R_15=3/4<1.                                    (H2)

Thus the actual nonlinear source map preserves this ball and contracts by
at most 3/4. The complete same-source Picard proof in O3 gives the original
positive vacuum, including its recovered scalar and energy, throughout H1.
The exact coefficient series also gives the sharper actual radius

    r_xi=(3/16)(1-sqrt(1-(2500/3)xi))<=9/64,
    theta_xi=(2500/3)xi<=25/27<1.                         (H3)

Every coefficient is the original coefficient of U26 and V1. Positivity and
ground-state uniqueness identify the assembled function with the same psi_L;
no auxiliary vacuum is used. The tail B_xi theta_xi^P/(1-theta_xi) remains a
proved summable bound for the full series. The curvature formula O13 retains
its own domain; the physical lower bound below is derived independently of
its sign.

## H3. Conditional projections on the original interacting Hilbert space

For an original edge e, let P_e be the actual conditional expectation given
all link variables except U_e, in rho_L dU_L. Its displayed density is

    p_e(U_e|eta)=rho_L(U_e,eta)/int rho_L(V_e,eta)dV_e.      (H4)

Fubini proves P_e=P_e*=P_e^2 on the original L2(rho_L dU_L). The two retained
form identities are

    <f,(I-P_e)f>_rho=||f-P_e f||_rho^2
                   =E_rho Var_(p_e)(f),
    B_L=sum_e(I-P_e).                                    (H5)

This bounded self-adjoint nonnegative B_L uses dimensionless heat-bath rates.
It is related to the original energy operator by the explicit form comparison
H11 below, on the common original state space. The physical kappa is not
assigned to these auxiliary rates or removed from that comparison.

The exact conditional densities from the same support potentials are V5.
Their original influence majorant V6 now satisfies, directly from H3,

    q_xi=(65536/9375)r_xi<=3072/3125<1.                   (H6)

The coefficient calculation is O24. No Haar marginal is substituted here:
c_ef bounds the TV difference of the actual p_e when only the exterior U_f
changes. It is obtained by differentiating the full exponential conditional
ratio; every support containing e and f is counted.

## H4. A complete spectral proof for the actual conditional operator

Write N=|E_L| and P=N^-1 sum_e P_e. For a real continuous f let osc_i f be its
oscillation when only the original edge i is varied. The actual conditional
comparison yields, for i!=e,

    osc_i(P_e f)<=osc_i f+c_ei osc_e f,
    osc_e(P_e f)=0.

To verify the first line, compare the two original conditional integrals.
The change of the integrand with fixed integration variable is bounded by
osc_i f. The change of its conditional probability is bounded by c_ei; a
real function with range length osc_e f pairs against this signed zero-mass
probability difference by at most c_ei osc_e f. This retains the TV convention
one half of the L1 distance and needs no new factor. Averaging gives

    osc(Pf)<=[(1-1/N)I+C^T/N]osc(f).                      (H7)

The sum of the components contracts by at least
1-(1-q_xi)/N, since the row sums of C are at most q_xi. The bounded exponential
has the literal Poisson series

    exp(-t B_L)=e^(-Nt)sum_(k>=0)(Nt)^k P^k/k!.

Positivity, the componentwise inequality H7 and that absolutely convergent
series give

    ||exp(-t B_L)(f-rho_L f)||infinity
        <=e^(-(1-q_xi)t)sum_i osc_i f.                   (H8)

The total oscillation of any function on this finite product is at most the
sum of its single-edge oscillations by telescoping original coordinates;
its mean lies in its real range. These facts prove H8. Complex functions
are handled by their real and imaginary parts; the exponential rate stays
the same. The prefactor is finite for each finite graph, and is not claimed
to be independent of its size.

For a centered continuous f, apply the spectral resolution of the bounded
self-adjoint B_L. Positive spectral mass below 1-q_xi-epsilon would bound
||exp(-t B_L)f||_2^2 below by that mass times
exp(-2(1-q_xi-epsilon)t), contradicting H8 as t increases. Thus its spectral
measure gives zero mass to [0,1-q_xi). Centered continuous functions are
dense in centered L2 of the original smooth positive probability. The same
spectral projection therefore vanishes on that whole space. We have proved

    <f,B_L f>_rho >=(1-q_xi)Var_rho f                     (H9)

for every original L2 function. This proof did not require compact resolvent
of B_L, a finite spin cutoff, or a uniform mixing prefactor.

## H5. Return to the complete original Hamiltonian form

The actual pointwise estimate already proved in the predecessor is

    |X_e log psi_L|<=2r_e xi<=8xi.

The original X-coordinate path diameter of SU(2) is 2pi. Therefore the
logarithm of the actual conditional density H4 has oscillation at most

    beta_xi=32pi xi,
    (sup p_e)/(inf p_e)<=exp(beta_xi).                   (H10)

The conditional denominator is independent of U_e, so it has zero derivative
in this step. The original single-link Haar Casimir has first positive
value 3/4. Completeness of the original matrix coefficients proves its full
Poincare inequality. For a fixed exterior configuration retain m_e=inf p_e,
M_e=sup p_e, and the two actual probability means. Then

    Var_(p_e)f
       =inf_c int p_e |f-c|^2
       <=M_e inf_c int_H |f-c|^2
       <=(4/3)M_e int_H sum_alpha |X_e,alpha f|^2
       <=(4/3)(M_e/m_e)int p_e sum_alpha|X_e,alpha f|^2.

The identities and inequalities use the same original function and both
explicit measures. They do not replace either mean or pairing by the other.
Integrating over all original exterior variables and summing gives

    <f,B_L f>_rho <= [4 exp(beta_xi)/(3kappa)] q_A_L(f).   (H11)

This is the promised typed comparison: the identity on the original smooth
functions, extended to their original form domain, relates the bounded
conditional form and the full ground-relative Hamiltonian form. It preserves
the state Gram and retains the physical factor kappa=2g^2/a.

Combining the two proved inequalities H9 and H11 establishes

    q_A_L(f)>=kappa d_xi^HB Var_rho f,
    d_xi^HB=(3/4)(1-q_xi)exp(-32pi xi)>0.                (H12)

Density extends it from smooth functions to the original H1 form domain.
Multiplication by psi_L is the original Haar-unitary ground-state transform.
Thus H12 is a lower bound for the full scalar excitation spectrum, and also
for the complete physical spectrum. It includes every regulator-dependent
choice of physical state; a finite observation window was not used.

There are two convenient fully rational closed-domain values. On all of H1,
use q_xi<=3072/3125 and 32pi xi<176/1575. The elementary inequality
e^(-x)>=1-x and the original pi<22/7 then give

    d_xi^HB >=(3/4)(53/3125)(1399/1575)
             =74147/6562500 >1/100,       g^2>=15.       (H13)

On the stronger subdomain g>=4, xi<=1/1024. Use R_4=7/64; the same literal
source map has

    B_xi+(8/3)R_4^2<=625/8192+49/1536=2659/24576
                           <2688/24576=R_4,
    (16/3)R_4=7/12<1.

Consequently q_xi<=7168/9375 and 32pi xi<11/112. The same exponential
inequality gives

    d_xi^HB >=(3/4)(2207/9375)(101/112)
             =222907/1400000 >3/20,       g>=4.          (H14)

In original physical units these are

    Delta_L >=kappa/100=g^2/(50a),            g^2>=15,
    Delta_L >=3kappa/20=3g^2/(10a),           g>=4,       (H15)

with the stronger actual value H12 retained at every coupling. Both hold for
every original L>=2 and a>0. No original operator term or energy origin is
changed in any of these comparisons.

## H6. An explicit factorization of the original cohomological primitive

Let d_X f=(X_i f)_i, with the original energy pairing
||d_X f||_1^2=kappa int rho sum|X_i f|^2. Define the bounded conditional
source map on L2(rho)

    d_B f=(f-P_e f)_e,
    ||d_B f||^2=<f,B_L f>_rho.

H9 proves its kernel is exactly the constants and its range is closed.
On that actual range set

    p_B(d_B f)=f-rho f,
    ||p_B||<=(1-q_xi)^(-1/2).

The actual map from the physical gradient source is

    T:ran(d_X|H1)->ran d_B,
    T(d_X f)=d_B f,
    ||T||<=[4exp(beta_xi)/(3kappa)]^(1/2).                (H16)

It is well-defined because changing f by a constant changes neither source;
the norm estimate is exactly H11. Its inverse on its actual image is
z->d_X p_B z. Both inverse laws follow from p_B d_B f=f-rho f. No bounded
inverse on an unspecified larger range is assumed. The primitive of the
original gradient complex now has the exact factorization

    p_X=p_B T,
    ||p_X||^2<=1/(kappa d_xi^HB).                         (H17)

The source and target maps, the kernels and the original physical energy
pairings are explicit. In the support-labelled reconstruction these are the
same incoming original-gradient relations and their actual primitive; the
conditional comparison provides their quantitative bound without deleting
any retained relation or replacing the original Hilbert metric.

## H7. Zero shift, canonical section, and actual numerical return

For the original loop observation, K=ker E consists of zero-mean functions
in rho. Its original restricted closed form therefore represents

    D>=kappa d_xi^HB,
    ||D^-1||<=1/(kappa d_xi^HB).                          (H18)

All moment, residual and primitive formulas U31–50 remain literal identities
for their original functions. The pointwise precursor estimates are proved
for xi<=3/64, which contains H1. To evaluate their error on the whole present
domain, use H18 in place of the baseline inverse bound in a7,E_Z. Specifically

    a7=r_z^2/d_xi^HB,
    E_M^HB=(a1+...+a6+a7)/xi^2,
    E_Z^HB=delta z_*+(eta Z_*)^2
          +2n_z r_z/(d_xi^HB xi)+(r_z/(d_xi^HB xi))^2.     (H19)

Every other quantity is the same original U38–40 value. At the actual
xi=10^-8, g^2=5000, kappa=10000/a, the rational interval evaluation gives

    d_xi^HB>0.74999514999,
    E_M^HB<0.0000094,
    E_Z^HB<0.00000319,
    r_z^2/(d_xi^HB xi^2)<0.0000000000142.                (H20)

Thus

    |M0-(8/39)kappa xi^2|<0.0000094 kappa xi^2,
    |||D^-1W||^2-(196/4563)xi^2|<0.00000319 xi^2.          (H21)

The full nonnegative canonical quotient-plus-section-correction cost U45 is
less than 0.0000000000142 kappa xi^2. This bound retains both its terms and
the actual primitive, not only a support flag.

The raw state G, kinetic K0 and one-state variational upper bound U49–50
remain. The lower bound is now the full-domain H12. Their return is

    0.74999514999 kappa <=Delta_L<(3+5/10^13)kappa         (H22)

at the stated coupling, for every a,L. The endpoint directions have their
separate exact variational justifications; the trial-state lower endpoint
is not used to estimate the whole physical spectrum from below.

## H8. Full spatial-volume return on g^2>=15

The proof of `VOLUME_LIMIT.md` is now applied to the same support series with
the explicitly established source radius at most9/64. Every required estimate
is evaluated here, so the return has no new unproved premise:

    sum_(S containing e)||v_S||infinity <=(16/15)r_xi,
    sum_f c_ef <=q_xi<=3072/3125<1,
    sum_f B_ef <=(384/125)r_xi<=54/125,
    coefficient tail <=B_xi theta_xi^P/(1-theta_xi),
    theta_xi<=25/27<1.                                  (H23)

V1's exact cutoff identity is independent of the auxiliary norm. V5–9 now
have the strict influence factor3072/3125, so their full coupling proof
still gives one unique vacuum measure and full-sequence convergence. V14–18
use the actual complete drift matrix with row bound54/125; their exponential
comparison converges on every finite physical-time interval without needing
positive curvature. The original local pointwise drift bound remains8xi.
Thus the direct full semigroup limit, original generator expression,
reversibility, gauge-invariant physical space and all time-ordered local
correlations V19–22 hold on H1.

In the finite spectral return use the full lower edge kappa d_xi^HB from H12.
The outside free-link gap is3kappa/4, and d_xi^HB<=3/4. The exact tensor
comparison in V20 therefore applies with this value. The limiting physical
vacuum representation has the same positive lower bound, a nonzero centered
loop vector, and zero atoms at both compactified energy endpoints. The
surjective time-symbol unitary is the one explicitly constructed in V22.
The original regulator-sequence kernel is not inferred to vanish from it.

The actual extensive energy estimate and its unique per-plaquette volume
limit V23–25 retain their original coefficients as well. Their pointwise
remainder domain contains H1, and their local drift convergence is H23.

The completed result is thus a fixed-spacing spatial infinite-volume
construction, from the original finite positive vacua, of the vacuum measure,
full original ground-relative dynamics, local time-ordered correlations,
extensive energy density and a positive physical spectral lower edge,
throughout g^2>=15. This supplies no ultraviolet change of the original
physical fields or coupling parameters.

For the retained running path c_n=g0^-2+beta n log2 and g_n^2=1/c_n, the
present closed domain is exactly c_n<=1/15. With beta>0 that is a finite
initial segment. At fixed admissible g and a->0, the physical bound scales
as1/a and the positive-time endpoint calculation U57 applies with d_xi^HB.
No four-dimensional smooth-continuum Yang–Mills field or finite positive
continuum mass is assigned to either parameter limit.

## Verification scope

The checker verifies the fixed-point balls, exact influence constants,
conditional projection matrices in a genuinely interacting rational fixture,
the full noncommuting heat-bath generator and its weighted spectral inequality,
the original single-link Haar factor3/4, exact physical comparison constants,
and the outward rational H20 intervals. The complete analytical proof is
H1–23 together with U1–57, O1–26 and V1–25. These finite checks are not a
formal proof or an independent external mathematical review. The method's
classical conditional-comparison antecedent is recorded in [DC] in the volume
note; the entire spectral and physical return used here is proved above.
