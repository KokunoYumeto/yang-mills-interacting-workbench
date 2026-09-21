# The full spatial-volume limit: original vacuum measure and dynamics

15 September 2026. This completes the fixed-spacing volume extension of
`RESEARCH_NOTE.md`, equations U26–29 and U51–55. Throughout this file the
original physical spacing a>0 and coupling g>=8 are fixed,

    kappa=2g^2/a, xi=1/(4g^4), R=2048xi<=1/8,
    d_xi=1/2-6144xi>=1/8.

The original finite-box Hamiltonians, their positive unit vacua and every
local link coordinate remain those of U3–4. No infinite scalar ground energy
or density relative to the infinite Haar product is stipulated. We construct
the limit of the actual finite ground-relative dynamics and its vacuum
representation. `OPTIMIZED_DOMAIN.md`, O23–26, evaluates the same complete proof inputs on
the larger domain g^4>138240/451, retaining all the following maps and replacing
only the stated auxiliary bounds. The continuum change a->0 remains the separate parameter
calculation U56–57.

## V1. Exact compatibility of the retained support coefficients

Let E_infinity be the countable set of positive nearest-neighbor edges of
Z^3. For every nonempty finite label S use the coefficient convention U6–10.
The order-p coefficient with label S in U26 depends only on coefficients
with labels S1,S2 whose union is S, and on source plaquettes with boundary S.
Every such label is a subset of S. The multiplier K^-1 on functions of S
is the same sum-of-original-Casimirs inverse in every box containing S.
The original Haar-constant projection on a function of S is likewise the
integral over those same S variables. Induction in the exact coefficient
recurrence therefore proves

    v_(S,[p])^L=v_(S,[p])^L'                              (V1)

for every two boxes containing S. For each p this is a finite identity:
S is contained in a finite graph, the spin at each edge is at most p/2,
and the recurrence has only finitely many partitions of its order and labels.

U27 is a convergent bound for the full series. Define

    v_S=sum_(p>=1)xi^p v_(S,[p]).

The same v_S occurs in every finite-box vacuum containing S. The finite-box
logarithm and density are exactly

    log psi_L=c_L+sum_(S subset E_L) v_S,
    rho_L=exp(2 sum_(S subset E_L)v_S)/Z_L,
    Z_L=int exp(2 sum_(S subset E_L)v_S)dU_L.               (V2)

The scalar c_L=-(1/2)log Z_L is the original scalar coordinate in U17. The
higher labels remain even when Fourier active support becomes smaller. In
particular, contributions from an outside cluster have not been reassigned
to a smaller label and then mistaken for an inside term.

Set a_(S,j)=||A_(S,j)||_1 in the original trace convention. The full bound is

    sup_e sum_(S containing e)2^|S| sum_j c(j)a_(S,j)<=R.   (V3)

The same estimate holds for the infinite family: for each finite partial
collection take a box containing its supports, apply U16, and take the
increasing supremum of the nonnegative sums. Since c(j)>=3/4 for every
nontrivial representation,

    ||v_S||infinity <= (4/3) sum_j c(j)a_(S,j),
    sup_e sum_(S containing e)||v_S||infinity <= (2/3)R.   (V4)

All local conditional sums below consequently converge absolutely and
uniformly. Their terms are continuous real functions of the original links.

## V2. Actual conditional measures and a quantitative influence bound

For a finite edge set Lambda and an exterior configuration eta, define the
finite conditional kernel by its complete density

    gamma_Lambda(dU_Lambda|eta)
      = exp(2 sum_(S intersects Lambda) v_S(U_Lambda eta)) dU_Lambda
        / int exp(2 sum_(S intersects Lambda) v_S(V_Lambda eta)) dV_Lambda. (V5)

The sum is uniformly absolutely convergent by V4 and the finite number of
anchors in Lambda. The denominator is strictly positive and finite. Terms
entirely outside Lambda would be the same factor in numerator and denominator;
V5 is the explicit conditional formula retaining their exact cancellation.
For an individual edge e, its dependence on an exterior link f is bounded by

    c_ef=4 sum_(S containing e,f)||v_S||infinity (e!=f),
    c_ee=0.                                                (V6)

Here c is an actual nonnegative influence majorant, not an assumed matrix.
To prove the bound, change only the exterior link f. The change Delta(U_e)
in the logarithm before division by the integral is
2 sum_(S containing e,f)(v_S(U_e eta)-v_S(U_e eta')). Its oscillation in U_e
is at most 8 sum ||v_S||infinity. For the interpolation of the two actual
probabilities p_t proportional to exp(t Delta)p_0, differentiation gives

    d p_t/dt=(Delta-E_(p_t)Delta)p_t.

The total-variation speed is at most (1/2)osc(Delta). Integration over
0<=t<=1 proves TV(p_1,p_0)<=c_ef. The differentiation is justified by the
bounded continuous Delta. Changing multiple exterior coordinates follows
by telescoping; countably many changes follow by uniform convergence of
V5 and the summability established next.

The row sums obey

    sup_e sum_f c_ef
      <= (16/3) sup_e sum_(S containing e)(|S|-1) sum_j c(j)a_(S,j)
      <= (4/3)R <= 1/6.                                  (V7)

Indeed (m-1)/2^m<=1/4 for every integer m>=1. This retains the original
factor two in the vacuum density, every link in each support, and the
original Fourier bound. No source mass or physical coupling was changed.

## V3. Complete finite comparison and uniqueness

For completeness we prove the comparison used here, rather than supplying a
uniqueness criterion as an unevaluated premise. Fix Lambda and two exterior
configurations. Their probabilities in V5 are invariant under the operation
which chooses one edge of Lambda uniformly and replaces it by its own exact
conditional probability. This follows by Fubini from V5. Couple two such
chains starting with those two invariant probabilities as their marginals.
On the selected edge, couple the conditional densities maximally: use their
common density min(p,p') on the diagonal and the two residual densities on
the remaining event. This is a measurable coupling in the original Haar
coordinates. The residual event has probability exactly their TV distance.

Let p_e(t) be the probability of unequal links in this joint chain. Put
b_e=sum_(f outside Lambda)c_ef. From V6 and telescoping the remaining inside
coordinates, one update gives

    p(t+1) <= [(1-1/|Lambda|)I+C_Lambda/|Lambda|]p(t)
                       +b/|Lambda|.                      (V8)

The matrix norm of the bracket in the max norm is at most
1-(1-q)/|Lambda|, q=1/6. Both marginals remain their original invariant
probabilities at every time. For a cylinder function F depending on
Delta subset Lambda, define its original single-edge oscillation osc_e F.
Telescoping F on the two configurations bounds the difference of expectations
by sum_(e in Delta)(osc_e F)p_e(t). Iterating V8 and letting t grow gives

    |gamma_Lambda F(eta)-gamma_Lambda F(eta')|
       <= sum_(e in Delta)(osc_e F)
              [sum_(r>=0) C_Lambda^r b]_e.                (V9)

All entries on the right are actual convergent nonnegative sums. The initial
error tends to zero by the strict matrix-norm bound. This proof uses no
assumption about the existence of a stationary joint coupling.

As Lambda exhausts E_infinity, each b_e tends to zero because the row of c is
summable; b_e<=q. For each fixed r and e, C_Lambda^r b tends to zero by the
dominated convergence theorem for the corresponding absolutely summable
countable matrix products. The remainder of the Neumann sum after r=N is
bounded by q^(N+2)/(1-q). Thus the right side of V9 tends to zero for each
fixed F, uniformly over both exterior configurations.

Every weak subsequential limit nu of the original finite-box vacuum measures
satisfies the conditionals V5. To check this assertion precisely, the actual
finite-volume conditional on Lambda uses only S subset E_L in V5. The
supremum of its omitted logarithmic terms is at most

    2 sum_(e in Lambda) sum_(S containing e,S not subset E_L)||v_S||infinity,

which tends to zero by V4. Its conditional kernel therefore converges in TV,
uniformly over exterior configurations, to V5 by the same bounded-exponent
interpolation. The limiting kernel applied to a continuous cylinder function
is continuous on the full compact configuration product: its potentials are
uniform limits of continuous functions, its finite Haar integral is continuous,
and its denominator is bounded away from zero. The finite conditional
integration identity consequently passes to the weak limit, also after
multiplication by any bounded continuous exterior cylinder test. A monotone-
class argument extends those tests to the exterior sigma-algebra. This proves the
stated conditional property without prescribing it to the vacuum.

Any two probabilities with these conditionals have equal expectations of
all cylinder functions by V9, applied inside Lambda and then integrated over
their exterior laws. The cylinder algebra determines the measure. Hence there
is exactly one such nu. Since every subsequential vacuum limit has that
property and the whole family is compact, **the complete sequence of original
finite-box vacuum measures converges to nu**. The original normalized masses
and the constants Z_L have been retained in V2; no infinite product density
has been assumed. The finite marginals remain nontrivial and have the earlier
explicit positive density bounds.

The comparison mechanism is classical Dobrushin theory [DC]. Equations
V1–9 prove its actual input and full application here in the specified
original coordinates and coupling interval.

## V4. A complete majorant for the limiting drift

Let b_e^infinity=X_e sum_(S containing e)v_S, with all three original
components. Termwise differentiation is justified by V3 and U7. At finite
L extend b_e^L to zero outside E_L. The complete derivative majorant is

    B_ef=3 sum_(S containing e,f) sum_j j_e j_f a_(S,j),
    sup_e sum_f B_ef <= (3/2)R=:B_* .                     (V10)

This is the original, generally mixed, derivative matrix estimate before
taking its symmetric part. It is nonnegative and symmetric in e,f. For the
path length defined by dot U=sum_alpha a_alpha T_alpha U and length
int sqrt(sum_alpha a_alpha^2), let dist_X be the induced distance. The
adjoint matrices preserve this coefficient norm, so both group translations
are isometries. The diameter is 2pi in these original T coordinates. Relative
to the source metric c(T_alpha,T_beta)=delta_alpha,beta/4, the exact metric
identity is dist_X=2 dist_c; the physical kappa in every generator is unchanged.

V10 and integration along an original group path prove

    |b_e^infinity(U)-b_e^infinity(V)|
       <= sum_f B_ef dist_X(U_f,V_f).                    (V11)

For countably many changed links this follows from the finite telescoping
formula and the uniform cylinder approximation of b_e^infinity. The summed
majorant is finite. Define

    t_e(L)=sup_U |b_e^infinity(U)-b_e^L(U)|.

U28 proves t_e(L)->0 for each fixed e. The predecessor's actual pointwise
bound gives t_e(L)<=16xi uniformly in e,L. The same derivative construction
can also give its explicit coefficient-tail bound when the required ball is
contained in the box. V10 is an estimate for the same original three-component
drift appearing in the full ground-state-transformed Hamiltonian.

## V5. Direct dynamical limit on the original configurations

For every original edge choose three independent real Brownian motions, using
one fixed countable family for all boxes. At edges in E_L use the original
finite-vacuum diffusion; outside use the free original link diffusion:

    dU_e^L=sqrt(2kappa) sum_alpha T_alpha U_e^L o dB_e,alpha
            +2kappa sum_alpha b_e,alpha^L(U^L)T_alpha U_e^L dt. (V12)

The stochastic integral is Stratonovich. Its generator on smooth cylinders is
kappa sum X_i^2+2kappa sum b_i^L X_i. In a fixed box the coefficients are the
original smooth finite-vacuum coefficients; the outside processes are independent
free copies. Thus this process is defined without a new interaction model.
Its invariant probability is the original rho_L dU_L times outside Haar. For
functions of inside links the inclusion J_L f=f o restriction is an isometry
with Haar-conditional inverse on its range, and its semigroup satisfies

    T_L(t)J_L=J_L exp(-t A_L),
    A_L=psi_L^-1(H_L-E0,L)psi_L.                           (V13)

This proves the exact relation of the extended process to the finite original
quantum correlation, including its original vacuum and energy units.

Here is an explicit convergence proof. Let R_e(t) solve V12's free group
Brownian equation with R_e(0)=I. Write U_e^L=R_e V_e^L. The Stratonovich
product rule gives the ordinary differential equation, path by path,

    dot V_e^L=2kappa [R_e^-1 sum_alpha b_e,alpha^L(U^L)T_alpha R_e]V_e^L. (V14)

The conjugation rotates the original three coefficients orthogonally. The
same R_e is used for two boxes and initial configurations agree. Left
multiplication is an isometry for dist_X. The upper right derivative of the
distance of the two ODE solutions is therefore bounded by twice kappa times
the difference of their rotated coefficients. One proof uses the triangle
inequality after advancing both solutions by the same infinitesimal left
translation, whose contribution to their distance is zero. This remains a
valid upper-Dini-derivative bound at the cut locus.

Set z_e(t)=dist_X(U_e^L(t),U_e^M(t)). Equations V11 and V14 give

    z_e(t)<=2kappa int_0^t
        [sum_f B_ef z_f(s)+t_e(L)+t_e(M)]ds.               (V15)

The original group diameter bounds every z_e by 2pi. Iterating the integral
inequality, with w=t(L)+t(M), gives the complete bound

    sup_(s<=t) z_e(s)
      <= sum_(r>=0) (2kappa t)^(r+1)/(r+1)! (B^r w)_e.   (V16)

The iterated remainder is at most 2pi(2kappa B_*t)^N/N! and tends to zero.
No spatial cross term in B^r is dropped. Since w is uniformly bounded by
32xi and tends to zero at each fixed edge, each fixed matrix product tends
to zero by dominated convergence of its absolutely summable rows. The full
series is dominated by the exponential series with B_*, uniformly on compact
time intervals. V16 therefore tends to zero for every e as L,M grow.

The bound is deterministic and uniform in the initial configuration and in
all common Brownian paths for which the countably many free group processes
exist. Hence the finite processes converge coordinatewise, uniformly on
compact time intervals, to a continuous process on the original countable
configuration product. Passing in V14 proves its drift is b^infinity. The
same inequality with w=0 and the iterated remainder above proves pathwise
uniqueness for that initial configuration and Brownian family.

Let T(t) be its semigroup on continuous functions. For smooth cylinder F,
V16 bounds ||T_L(t)F-T(t)F||infinity by the finite sum of its original edge
Lipschitz constants times the right side. Thus convergence is uniform in
configuration and compact time. Smooth cylinders are uniformly dense in the
continuous functions on the compact product; the contraction property extends
this convergence to that whole space. Positivity and preservation of constants
pass to the limit. The semigroup law follows by taking the limit in
T_L(t+s)=T_L(t)T_L(s), using the two uniform convergences and contraction.

For a fixed smooth cylinder F the exact finite generator satisfies

    ||A_L F||infinity
       <=kappa||K F||infinity+16kappa xi sum_e||X_e F||infinity, (V17)

uniformly in L, including outside links where b^L is zero. Integrating the
finite generator proves ||T_L(t)F-F||infinity<=t times this constant. Passing
to the limit and using density proves strong continuity of T(t). The drift
convergence similarly proves F is in its generator domain and

    A_infinity F=kappa K F-2kappa sum_e,alpha
                             b_e,alpha^infinity X_e,alpha F. (V18)

All derivatives of F here are on its actual finite support; all dependence
of b^infinity on the remaining configuration stays in the formula.

## V6. Actual vacuum representation, spectral gap, and all local correlations

Finite reversibility, V13, uniform semigroup convergence and the full weak
measure limit V3 give, for continuous F,G,

    int conjugate(F) T(t)G dnu = int conjugate(T(t)F) G dnu,
    int T(t)F dnu=int F dnu.                              (V19)

Both sides use the original conjugate-linear first entry. Therefore T(t) extends to a self-adjoint Markov contraction
semigroup on L^2(nu). Strong continuity follows from the already proved
uniform continuity on continuous functions and their L^2 density. Its
nonnegative self-adjoint generator is the ground-relative A_infinity.

The full finite inside scalar gap is at least kappa d_xi. Every free outside
link has original scalar gap 3kappa/4, and d_xi<=1/2. Conditional variance and
the two original product factors show that the extended finite semigroup has
centered norm at most exp(-kappa d_xi t) on cylinder functions. More explicitly,
the product vacuum is one, the two constant/nonconstant decompositions are
orthogonal, and on every nonconstant product component at least one factor
has this decay. Completing the finite-variable tensor expansions proves the
bound without an assumed independence inside the interacting box.

The integrands T_L(t)F converge uniformly, and nu_L converges weakly, so the
squared L^2 inequality passes to the limit. Density gives

    ||T(t)(F-nu F)||_L2(nu)
       <=exp(-kappa d_xi t)||F-nu F||_L2(nu),
    A_infinity|_(1 perpendicular)>=kappa d_xi.            (V20)

The original gauge action commutes with every finite semigroup and preserves
its vacuum. Uniform convergence passes both facts to T(t),nu, so V20 holds
on the complete centered physical subspace as well. This construction has a
unique unit constant vacuum in its Hilbert space, by V20. It concerns the
unique limit of the specified positive finite-box vacua and dynamics; no
unexamined family of other infinite-volume quantum representations is assigned
to this statement.

The vacuum representation is explicit:

    H_infinity=L^2_phys(nu), vacuum=1,
    pi_infinity(O)F=OF,
    T(t)=exp(-t A_infinity).                              (V21)

For a finite time-ordered local list, the original finite vacuum expression
has the exact ground-state transform

    <psi_L, O_0 exp(-t_1(H_L-E0,L)) O_1 ...
                  exp(-t_m(H_L-E0,L)) O_m psi_L>
     =int O_0 T_L(t_1)(O_1 T_L(t_2)(...T_L(t_m)O_m))dnu_L. (V22)

All O_i are the original bounded continuous physical multiplication observables,
and all t_i>=0 are original physical times. Repeated uniform convergence and
the measure limit return V22 to the same formula with nu,T. Thus **all such
local Euclidean-time vacuum correlations converge along the full box sequence**.
The positive-time reflection Gram remains a squared Hilbert norm, by V19–21.
No spatial continuum symmetry or ultraviolet limit is asserted by this fact.

The elementary loop satisfies the nonzero variance and two-sided correlation
bounds U54–55 with this unique limit. In particular the limiting physical
Hilbert space has a nonzero centered vector of finite energy. The two compactified
spectral endpoint atoms remain zero at fixed a,g, by U51–53.

Finally the correlation Hilbert space of U53 has a complete typed identification
with V21. Send its time symbol [O,t] to T(t)(O-nu O). Its pairings are exactly
the limiting original correlations, so it descends through the actual null
space to an isometry. Its range is dense because t=0 includes the entire
centered physical cylinder algebra; gauge averaging proves that algebra is
dense in the physical L^2 space. Thus it extends to a unitary, with inverse
given by completion of the zero-time cylinder vectors. It intertwines time
translations and T(t), and therefore the self-adjoint generators and their
spectral measures. This removes the unspecified closed-range complement that
was retained in the earlier subsequential construction through an actual
surjective map, rather than declaring it absent. This complement is the one inside the
correlation Hilbert space just identified. The original bounded-regulator-
sequence comparison and its kernel remain their separately defined maps;
no vanishing of that whole sequence kernel is inferred here. The finite full-
domain bound U23 already controls energies of every such state sequence.

The cylinder form of U29 is carried into this semigroup form by the original
coordinate identity q(F,G)=kappa int sum conjugate(XF)XG dnu. All closed-form
comparisons made in U53 retain that domain statement. The primary dynamical
realization here is the direct process/semigroup limit V12–22.

## V7. The extensive ground energy and its volume limit

The original scalar ground energy is also retained quantitatively. From U17,
with the original Haar integral,

    E0,L=2kappa xi |P_L|-kappa int_H sum_e |b_e^L|^2.

Write b_e^0=(xi/3)sum_(p containing e)X_e W_p, as in the predecessor. At
xi<=1/16384 its proved actual remainder obeys
|b_e^L-b_e^0|<=A_*xi^2, A_*=256/9. The complete original Haar identity is

    int_H sum_e |b_e^0|^2=xi^2 |P_L|/3.                   (V23)

Indeed int_H W_p W_q=delta_pq: unequal faces have an unmatched original
fundamental link, and the equal trace has second moment one. Integration
by parts and K W_q=3W_q give int_H sum_e X_e W_p.X_e W_q=3delta_pq.
Multiplication by xi^2/9 proves V23, including all cross terms.

The actual local bound |b_e^0|<=r_e xi/3 and the complete squared difference
then give

    |E0,L-kappa |P_L|(2xi-xi^2/3)|
      <=kappa [(2048/27)|P_L|xi^3+(65536/81)|E_L|xi^4].    (V24)

Here sum_e r_e=4|P_L| was used exactly; the two coefficients are
8A_*/3 and A_*^2. With the original counts
|E_L|/|P_L|=(2L+1)/(2L)<=5/4, this also supplies an explicit per-plaquette
remainder while retaining the full energy and its extensive factor.

The energy per plaquette has a unique limit. The coefficient family V1 is
translation invariant on the infinite cubic graph and is invariant under
permutation of the three spatial axes, by its exact source recurrence.
Thus the original infinite Haar product gives the same value

    B_H=int_H |b_(0,1)^infinity|^2

at every bulk edge orientation. This is an integral of a bounded continuous
function supplied by U28; it is not assigned to the vacuum probability nu.
The constant Fourier coefficient in U17 is exactly why this Haar integral
occurs here. Edges a fixed distance from the boundary have b_e^L uniformly
close to that limiting function by U28. Boundary edges are a vanishing
fraction of the total for a fixed collar, and both drifts are bounded by
8xi. Taking first the volume and then the collar width to infinity proves

    E0,L/|P_L| -> kappa(2xi-B_H),
    |B_H-xi^2/3|<=(2048/27)xi^3+(65536/81)xi^4.           (V25)

The last constant uses the exact limiting ratio |E_L|/|P_L|=1 in V24.
All finite corrections remain in V24. This records the actual extensive
vacuum energy alongside the ground-relative gapped dynamics, rather than
silently setting the scalar term to zero.

## Scope and antecedents

The completed limit is spatial infinite volume with lattice spacing a>0 and
g>=8. Both original couplings and the continuous physical time remain.
The mass lower bound is kappa d_xi. The original running path g_n->0 eventually
leaves this proved interval, exactly as U56 records. The fixed-g change a->0
has the divergent physical lower edge and endpoint transport U57. No
four-dimensional smooth-continuum Yang–Mills construction or positive finite
continuum mass has been obtained by replacing either parameter map.

[DC] Patrick Rebeschini and Ramon van Handel, *Comparison Theorems for Gibbs
Measures*, arXiv:1308.4117 (2013), is a modern primary reference for the
Dobrushin/Markov-chain comparison method. Its abstract was inspected for
attribution; V5–9 supply the full elementary coupling proof used here and
evaluate its input on the actual vacuum interaction. No theorem from that
paper is invoked with unchecked hypotheses.

Finite Stratonovich equations on a compact group and their product rule are
used on their usual smooth global coefficient domains. The infinite-volume
step is proved explicitly by the original group-flow transformation V14 and
its complete summable comparison V15–16; no infinite-dimensional SDE existence
assertion is used as a premise. All source Hilbert pairings remain specified.

The exact checker verifies the scalar influence constants, finite conditional
interpolations, signed support compatibility, matrix comparison identities,
majorant rows and full matrix powers. These fixtures accompany the complete
analytic measure/dynamical proof above. No new Lean or independent external
verification is claimed.
