# The Split-Zero heat comparison transferred to the original Yang–Mills Grams

21 September 2026. This is a source-specific transfer, accompanied by a new
calculation of actual Yang–Mills heat correlations. The inspected Riemann
workbench revision is 128aa308dd2a70ba6e073816a957d1ee6414ba2c. The exact read
ranges and source blobs are in SOURCE_INTAKE.json. Its arithmetic quantities
remain attached to their own source; the Yang–Mills quantities below are
computed from the original Hamiltonian and its physical vacuum.

## T1. What was read and what is transferred

The complete argument used from the Riemann workbench is HM6--HM14 and
HM19--HM24 of HEAT_TO_ORIGINAL_QUOTIENT_METRICS.tex (19 September). It constructs
its original coefficient column map Rcal and a finite heat replacement
Rcal_J=Rcal-T_s Pcal. The physical arithmetic source pairing is unchanged and
T_s* T_s=s^(-1)I. From the complete original Gram, including both relation
cross blocks, HM13 proves the relative column error. Triangle inequalities
give (1-delta)^2 G <= G_J <=(1+delta)^2 G. Completing the square on the same
coefficient fibers carries these bounds through their actual restrictions and
quotient minima. HM22--HM24 retain every determinant rank and give the finite
heat depth for a prescribed return error.

HG6--HG10 of ORIGINAL_HEAT_AND_SOURCE_ENDPOINT.tex were also read. They expand
actual observation/kernel currents with both mixed products and give their
error under a relative change of the same original Gram. The fixed-divisor
subexponential estimate HG1--HG5 is retained as an inspected arithmetic result;
no value of its divisor-dependent constants is assigned to a Yang–Mills bound.

The common column-map calculation is instantiated below, on actual Yang–Mills
spaces. Its input error is supplied by the original physical semigroup rather
than by the arithmetic dilation. A source-specific map between arithmetic
zeta packets and physical gauge fields is not asserted. The explicit shared
interface and each new map are the displayed linear maps below.

## T2. The original physical heat columns and their entire forcing defect

Fix the original L=2 open box, M=240, a>0, and g^2>=20. Let A=H-E0 on the
centered physical Hilbert space H0, with its unchanged inner product. The
source columns R have entries rp=(Wp-<Wp>_rho)psi. From A23,

    Phi=kappa A^(-1)R,
    G2=Phi*Phi,   E=Phi*A Phi=kappa G1,
    (9/100)I<G2<(13/100)I,
    (3kappa/10)I<E<(11kappa/30)I.                           (T1)

All original coefficient axes p are retained. In particular Phi is injective.
The finite-regulator inverse and the original source identity A Phi=kappa R
are established in the analytic proof, not assumed as an observation metric.

The physical gap needed here has an independent short derivation. In the
original Haar space, minmax applied to B_xi=K-xi S gives its second physical
eigenvalue >=3-2Mxi. Its ground eigenvalue is <=0 by the original constant
trial vector. Therefore, for the actual centered A,

    A >=kappa(3-2Mxi)I >=(27kappa/10)I                       (T2)

because xi<=1/1600. This is a bound for this original box and coupling domain.
Every volume factor in its derivation is explicit.

For T>0 define the actual map and its convergent inverse on H0

    C_T=I-exp(-TA),
    C_T^(-1)=sum_(j>=0)exp(-jTA),
    ||C_T^(-1)|| <=[1-exp(-27kappa T/10)]^(-1).              (T3)

They commute with A on Dom(A); convergence in the graph norm follows by
commuting A through each term and applying the same geometric bound. Put

    Phi_T=C_T Phi=kappa int_0^T exp(-tA)R dt,
    E_T=Phi_T*A Phi_T,  G2_T=Phi_T*Phi_T.                   (T4)

Both state and energy errors retain their complete mixed products. Specifically,

    E_T-E =-Phi*A exp(-TA)Phi
            -Phi*exp(-TA)A Phi
            +Phi*exp(-TA)A exp(-TA)Phi,                     (T5)

with the analogous identity omitting A for G2. The two cross products are
equal here because the original A and its heat semigroup commute; their
origin in the expansion remains explicit. The source equation is

    A Phi_T=kappa R-kappa exp(-TA)R.                        (T6)

Thus the original forcing defect and its primitive are exactly
-kappa exp(-TA)R and -exp(-TA)Phi, respectively.

For epsilon=exp(-27kappa T/10), spectral calculus applied on the complete
centered physical space gives

    (1-epsilon)^2 G2 <= G2_T <= G2,
    (1-epsilon)^2 E <= E_T <= E.                            (T7)

For the energy inequality one applies C_T to A^(1/2)Phi; for the state
inequality one applies it to Phi. These are the actual column-map instances
of HM11, with a sharper one-sided upper bound supplied by the semigroup.
The norm of the omitted column is bounded relatively in its own original
state/energy pairing. All constants are independent of a after the exact
physical time T is inserted; T itself retains its factor 1/kappa.

## T3. Original support quotients and the corrected minimum

For an original face subset F, put V_F=Phi(C^F), U_F=A V_F=kappa R(C^F).
The complex is

    V_F --A--> H0 --0--> 0.                                 (T8)

Its support transition F subset G is the actual inclusion in degree zero and
identity on H0. The differential square commutes by the same original A.
For J=G\F, the transported cohomology kernel is exactly

    V_G/V_F -> ker[H0/U_F -> H0/U_G],
    [h] -> [Ah].                                           (T9)

Surjectivity follows by writing a killed class as Ah with h in V_G.
Changing h by V_F changes Ah by U_F, and conversely the injectivity of A on
H0 implies that a change by U_F has exactly a change by V_F. The inverse is
[Ah] -> [h]. The heat complexes use V_F^T=C_TV_F with the same target H0
and differential A. The actual pair (C_T,C_T) intertwines their differentials
and is invertible by (T3). It commutes with every support inclusion. Applying
the Split-Zero support reconstruction therefore retains F and its receiving
zero, together with the original killed representative and its primitive.

The energy-minimum representative of [Phi_J y] in V_G/V_F has the old-support
coordinate

    x_F=-E_FF^(-1)E_FJ y.

All blocks are taken in the fixed original face coordinates. Its exact quotient
Gram is

    Q_E(F,G)=E_JJ-E_JF E_FF^(-1)E_FJ.                       (T10)

Completing the square in x_F proves this formula and both inverse coordinate
maps to the quotient. The removed primitive Phi_F x_F remains. The state
minimum has the separately calculated formula with G2; it is not substituted
for the energy minimum.

Equation (T7) holds at every vector (x_F,y) in the same original coefficient
fiber. Taking the infimum in x_F on both sides proves

    (1-epsilon)^2 Q_E(F,G)<=Q_(E_T)(F,G)<=Q_E(F,G),           (T11)

and the state counterpart. The same proof applies successively to every finite
chain of fixed restrictions and quotient maps, retaining the same two bounds,
not multiplying an error factor at each stage. This is the actual HM19--HM21
minimum-fiber argument in the physical metric. A rank-zero quotient retains
its unique zero vector and determinant one.

To retain the surrounding physical space, put P_Phi=Phi G2^(-1)Phi*. Its
multiplication identities give P_Phi^2=P_Phi=P_Phi*. For any original form-domain
h perpendicular to im(Phi), the full energy is

    q_A(Phi c+h)=kappa c*G1 c
                +2kappa Re<Rc,h>+q_A(h).                  (T12)

This is the complete original coupling to the remaining physical functions.
No reducing-subspace property of the finite observation family is used.

## T4. A finite heat horizon for every four-return determinant

For a rank-r positive form G and its same-coordinate heat comparison satisfying
(T7), its relative eigenvalues belong to [(1-epsilon)^2,1]. The determinant
ratio is invariant under the displayed congruence with G^(-1/2), including its
inverse G^(1/2). Hence

    |log det G_T-log det G| <=2r[-log(1-epsilon)].           (T13)

The difference uses the same original frame and, for energy Grams, the same
kappa^r factor, which cancels exactly in the ratio. For any four prescribed
restriction/quotient returns with coefficients +1,+1,-1,-1 and ranks r_j<=240,

    |L_T-L| <=2 sum_j r_j [-log(1-epsilon)]
              <=1920 epsilon/(1-epsilon).                 (T14)

The final inequality follows by integrating 1/(1-x) from zero to epsilon.
Take the actual physical horizon

    T=10/kappa=5a/g^2.                                     (T15)

Then epsilon=exp(-27). The exact rational exponential enclosure gives

    epsilon<19/10^13,
    1920 epsilon/(1-epsilon)<4/10^9.                        (T16)

The calculated inner upper bound is approximately 3.608695327762*10^(-9).
The complete rational fraction is in generated/heat_bounds.json. This is one
common finite heat horizon for all four original returns and all original
support choices in this 240-column family. It requires no estimate of a newly
selected arithmetic comparison constant or observation angle.

## T5. Every signed observation current retains its mixed terms

Fix a surjection Lambda from the original C^240 onto its actual chosen
observation image; for example its rows can read a fixed subset of original
face coordinates. From the energy Gram E define

    Q=(Lambda E^(-1)Lambda*)^(-1),
    Omega=Lambda*Q Lambda,
    L=E-Omega.                                             (T17)

The minimum representative S=E^(-1)Lambda*Q satisfies Lambda S=I and
E S=Lambda*Q. Direct expansion proves that y*L y is the squared E-norm of
(1-S Lambda)y. Thus both the kernel residual and boundary Gram are the original
canonical ones, with every rectangular mixed entry preserved. Define the heat
versions using E_T and the identical Lambda.

Put eta=2epsilon-epsilon^2. Equation (T7) gives
(1-eta)E<=E_T<=E. Minimize on the identical Lambda fibers to get the same bounds
for Q. For fixed original columns a1,a2,v and omega>0 let

    K_i=a_i*L v, B_i=a_i*Omega v,
    d_i=a_i*E a_i, E_v=v*E v,
    Phi_K=2Re(conj(K1)K2)/omega,
    Phi_B=2Re(conj(B1)B2)/omega,
    Phi_cross=2Re(conj(K1)B2+conj(B1)K2)/omega.              (T18)

The same-fiber bounds and Cauchy--Schwarz give
|Delta K_i|<=2eta sqrt(d_i E_v), |Delta B_i|<=eta sqrt(d_i E_v), while each
original |K_i| and |B_i| is at most sqrt(d_i E_v). Expanding every linear and
quadratic product in (T18) proves the HG8 receiving inequalities

    |Delta Phi_K|<=2sqrt(d1 d2)E_v(4eta+4eta^2)/omega,
    |Delta Phi_B|<=2sqrt(d1 d2)E_v(2eta+eta^2)/omega,
    |Delta Phi_cross|<=2sqrt(d1 d2)E_v(6eta+4eta^2)/omega.    (T19)

These estimates contain the original phases and both cross products. The
actual source/target numerical values in this application are the calculated
Yang–Mills Grams, and their relative error is (T16). No sign of a current is
inferred from its norm alone.

## T6. Source and execution scope

This contribution reads the original HM/HG heat and metric proofs and proves
the displayed Yang–Mills instances in full. The arithmetic dilation T_s, its
Mellin variables, zeta-zero jets, original source masses and period-dependent
constants remain in the cited RH construction. Here exp(-TA) is the physical
ground-relative semigroup, with T (T15) in the original time units.

The heat coefficients, original box matrices, graph constants and rational
bounds are independently exercised by the executable tests described in
VERIFICATION.md. Their complete analytic proofs are supplied as written
arguments for review. The tests do not give a Lean proof, independently audit
every older source estimate, or establish the four-dimensional continuum gap.
The standing continuum path and the growing-volume problem still require
bounds beyond the explicitly finite M-dependent domain proved here.

## T7. The latest inverse-power observation has a concrete receiving instance

After the heat-source intake, the complete 21 September source
INVERSE_POWER_CONDUCTOR_OBSERVABILITY.tex was read at the same pinned commit.
Its IK9--IK10 construct a literal left inverse of selected original conductor
rows on their inverse-power space. IK12 returns that inverse through the
original source and observation Grams, retaining their eigenvalue factors.
IK13 explicitly permits its lower bound to tend to zero with its cutoff.
Those coefficients, root differences and guards remain in that construction.

In the present Yang–Mills family the actual inverse-power source is

    Phi=kappa A^(-1)R:C^240->H0,
    O=R*:H0->C^240,
    O Phi=G^(1).                                           (T20)

The independent computed bound (A23) makes this original response matrix
invertible, so its exact coefficient left inverse is

    W=(G^(1))^(-1) R*,
    W Phi=I_240,   ||(G^(1))^(-1)||<=10/3.                  (T21)

This is a proved inverse on these specific columns, not an assumed observation
angle. The original quotient metric for the observation O is (G^(0))^(-1):
minimizing the physical Hilbert norm over R*h=z has the representative
R(G^(0))^(-1)z. Its full residual is perpendicular to im(R), as multiplication
by R* verifies. Thus P_R=R(G^(0))^(-1)R* is the actual orthogonal projection,
and every nonzero coefficient vector c satisfies

    ||P_R Phi c||^2=c*G^(1)(G^(0))^(-1)G^(1)c,
    ||Phi c||^2=c*G^(2)c.                                  (T22)

Returning the three computed original metrics (A23),(A25) gives

    G^(1)(G^(0))^(-1)G^(1) >= (3/34)I,
    ||P_R Phi c||^2 / ||Phi c||^2 > 150/221.                 (T23)

Indeed the first coefficient is (3/10)^2/(51/50)=3/34, and dividing by the
upper state coefficient 13/100 gives 150/221. Every source metric and its
inverse has been retained. This is the IK12 left-inverse/minimum argument
applied to the original physical inverse-power family, with the needed Gram
bounds actually calculated here. It detects all 240 columns simultaneously
at L=2, every a>0 and g^2>=20. It does not supply an infinite-volume fraction or
an independence assertion for an uncomputed concatenation of higher powers.

The portion outside this observation is the exact vector
(I-P_R)Phi c. Its squared norm is

    c*[G^(2)-G^(1)(G^(0))^(-1)G^(1)]c,                       (T24)

and is positive semidefinite by the original orthogonal decomposition. No
component is removed from the energy formula (T12). The maps (T20)--(T24)
state the entire receiving construction; they make no identification of
arithmetic zeta zeros with physical spectral points.

## T8. The actual residual between the state and energy sections is bounded

Retain the original orthogonal state projection P_R from T7 and define

    h=(I-P_R)Phi,
    B0=(G^(0))^(-1)G^(1),   P_R Phi=R B0.                  (T25)

All columns of h satisfy R*h=0. Since A Phi=kappa R, the mixed energy
q_A(Phi c,h d) vanishes for every coefficient pair c,d, by the original
Hilbert adjoint identity. Thus Phi is the actual minimum-energy section
of the affine fibers R*f=G^(1)c. The state-minimum section of that same
fiber is R B0 c. They have the exact comparison

    h*Ah=kappa[G^(1)(G^(0))^(-1)Kobs(G^(0))^(-1)G^(1)-G^(1)],
    (P_R Phi)*A(P_R Phi)=Phi*A Phi+h*Ah.                    (T26)

To verify the first identity, expand the whole expression
(Phi-RB0)*A(Phi-RB0). Both cross products are kappa G^(1), while the last
term is kappa B0* Kobs B0; their signed sum is (T26). This also proves
nonnegativity of the right side. The state residual remains the matrix (T24).

The three raw bounds (A23),(A25),(A28) give the strict original energy bound

    0<=h*Ah < (1322/7203) Phi*A Phi.                        (T27)

Indeed congruence by (G^(1))^(-1/2), with its explicitly inverse square root,
puts the bracket in (T26) below

    [(31/10)(50/49)^2(11/30)-1]I = (1322/7203)I.

Returning that congruence proves (T27) in the original coefficient coordinates.
Thus the state-section correction has at most this fraction (less than0.184)
of the original primitive's energy, and (T23) retains more than150/221 of its
state norm in the actual observed force span. The difference itself remains
an element of ker(R*) with its complete state and energy Grams, rather than
being dropped. Both conclusions hold simultaneously for all240 original
columns on the specified finite box and coupling domain.

For a prescribed observation z, the two exact sections are
Phi(G^(1))^(-1)z and R(G^(0))^(-1)z, and their difference is
h(G^(1))^(-1)z. Their source-to-observation compositions are both the identity.
This supplies the explicit section-correction morphism and its quantitative
energy return in the original metric. It is the same minimum-section mechanism
read in the Split-Zero source, now with all physical Grams evaluated and the
entire correction bounded on its stated domain.
