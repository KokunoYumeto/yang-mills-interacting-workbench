# Unique spatial vacuum and dynamics across the first closed source domain

15 September 2026. This calculation re-evaluates the actual coefficient, conditional and dynamical maps of predecessor V1–22 using G6–23. Physical a>0 and g>0 remain fixed in the volume limit. The stronger physical gap is G26. S10–14 strengthen the conditional route to the full closed domain 0<xi<=3/256 by a direct volume-independent mixing bound and an explicit coupling modulus. The separate simultaneous continuum path is computed in S9 and returned in S14. SECOND_SOURCE.md R4 extends this same original dynamics to the later, larger source endpoint.

## S1. One compatible source family and its exact tails

The coefficient v_(S,[p]) is the SAME coefficient in every original box containing S: the source plaquette, inverse original Casimir, Haar projection and order-p union recurrence depend only on S. Induction proves this equality before summing the series. Connected order-p supports obey |S|<=3p+1 and j_e<=p/2. Let a_p be G16 and v_S=sum_p xi^p v_(S,[p]). Then

\[
 \sup_e\sum_{S\ni e}\sum_jc(j)\|A_{S,j}\|_1\le r,
 \quad \|v_S\|_\infty\le\tfrac13\sum_jc(j)\|A_{S,j}\|_1. \tag{S1}
\]

The factor 1/3 uses the proved physical nonconstant Casimir G8. In each finite box the original density is exactly

\[
 \rho_L=\frac{\exp(2\sum_{S\subset E_L}v_S)}{Z_L},
 \quad Z_L=\int\exp(2\sum_{S\subset E_L}v_S)dU,
 \quad c_L=-\tfrac12\log Z_L.                            \tag{S2}
\]

Each support retains its original union label even after an active Fourier cancellation. Thus an exterior contribution is not reassigned to an interior label.

For theta=256xi/3<1, differentiating the positive scalar majorant gives

\[
 \sum_{p\ge1}p a_p=\xi r'(\xi)=\frac{32\xi}{\sqrt{1-\theta}},
 \quad
 \sum_{p>P}p a_p\le32\xi\theta^P
       \frac{(P+1)-P\theta}{(1-\theta)^2}.              \tag{S3}
\]

Both tails are bounds for the complete original coefficient series. At theta=1 only the different tail G19 is used; S3 does not claim a finite derivative sum there.

## S2. The actual conditional kernels and their sharper influence

For a finite link set Lambda and original exterior configuration eta define

\[
 \gamma_\Lambda(dU_\Lambda\mid\eta)=
 \frac{\exp(2\sum_{S\cap\Lambda\ne\varnothing}v_S(U_\Lambda\eta))dU_\Lambda}
 {\int\exp(2\sum_{S\cap\Lambda\ne\varnothing}v_S(V_\Lambda\eta))dV_\Lambda}.
                                                               \tag{S4}
\]

S1 makes this sum uniformly absolutely convergent, and the denominator is positive. These are the limits of the actual finite-vacuum conditional densities; no independent density is assigned to the infinite Haar product.

Changing only exterior edge f changes the original single-edge log density at e by a function Delta of oscillation at most 8 sum_(S containing e,f)||v_S||_infinity. For the actual interpolating probabilities p_t proportional to exp(t Delta)p_0,

\[
 \frac12\int|\partial_t p_t|
 =\tfrac12 E_{p_t}|\Delta-E_{p_t}\Delta|
 \le\tfrac14\operatorname{osc}\Delta.                  \tag{S5}
\]

To verify the last inequality without omitting its constant, let m<=Delta<=M and mu=E Delta. The chord bound for the convex function |x-mu| yields E|Delta-mu|<=2(mu-m)(M-mu)/(M-m)<=(M-m)/2. The constant case has both sides zero. Consequently an actual influence majorant is

\[
 c_{ef}=2\sum_{S\ni e,f}\|v_S\|_\infty\quad(e\ne f),
 \qquad c_{ee}=0.                                       \tag{S6}
\]

Every denominator of S4 is included in the interpolation derivative. S1, |S|-1<=3p and S3 prove

\[
 \boxed{\sup_e\sum_f c_{ef}\le q(\xi):=
          2\xi r'(\xi)=\frac{64\xi}{\sqrt{1-256\xi/3}}.} \tag{S7}
\]

The actual strict domain q<1 is

\[
 \boxed{0<\xi<(\sqrt{13}-2)/192,
 \qquad g^4>\tfrac{16}{3}(2+\sqrt{13}).}                 \tag{S8}
\]

Every g^2>=11/2 lies in this domain. At its stated closed benchmark,

\[
 q^2\le12288/12947<1.                                   \tag{S9}
\]

The unweighted source is used with its full order-dependent size information; no bound on support cardinality was discarded.

## S3. Uniqueness and convergence of the actual measures

Here is the complete finite comparison underlying the volume statement. In a finite set Lambda, update one original link uniformly using its exact conditional density S4. Each finite conditional measure is invariant under that update by Fubini. Couple two such chains with different exterior configurations, using maximal coupling of their original link conditional densities. The probability of disagreement at the selected link is exactly its total-variation distance. Let p_e(t) be the disagreement probabilities and b_e=sum_(f outside Lambda)c_ef. The complete vector inequality is

\[
 p(t+1)\le[(1-1/|\Lambda|)I+C_\Lambda/|\Lambda|]p(t)+b/|\Lambda|.
                                                               \tag{S10}
\]

The matrix has maximum row sum at most 1-(1-q)/|Lambda|. Telescoping an original cylinder function F over disagreeing links, iterating S10, and taking t to infinity give

\[
 |\gamma_\Lambda F(\eta)-\gamma_\Lambda F(\eta')|
 \le\sum_{e\in\operatorname{supp}F}\operatorname{osc}_e(F)
              [\sum_{j\ge0}C_\Lambda^j b]_e.            \tag{S11}
\]

The initial error tends to zero by the strict row bound; no stationarity of the joint coupling is assumed. As Lambda exhausts the original countable lattice, b_e->0 for every fixed edge and b_e<=q. Every fixed power term tends to zero by dominated convergence of the summable nonnegative rows; the remainder after j=J is bounded by q^(J+2)/(1-q). Thus S11 tends to zero uniformly in the two exterior configurations for each fixed F.

Extend rho_L dU inside its original box by independent original Haar factors outside. Compactness of the countable configuration product supplies weak subsequential limits. The finite-vacuum conditional on Lambda differs from S4 only by original supports not contained in E_L. Its omitted log-density is bounded by 2 sum_(e in Lambda) sum_(S containing e,S not contained E_L)||v_S||, which tends to zero by S1 and coefficient compatibility. S5 then gives uniform convergence of these kernels in total variation. Their action on continuous functions is continuous; conditional integration passes to any weak limit, and a monotone-class argument extends the exterior tests. Every weak limit therefore has S4 as its actual conditional kernels.

Integrate S11 over the exterior laws of two such limiting probabilities. They agree on every cylinder function and hence are equal. This proves a unique measure nu and convergence of the whole sequence rho_L dU to nu on S8. Its gauge action remains the original vertex action, passed through each finite invariant measure.

## S4. Complete drift matrix, including all mixed derivatives

Set b_e^infinity=X_e sum_(S containing e)v_S, with its three original components. The exact order-p spin restriction and G7 give

\[
 3j_e\sum_fj_f\le3(p/2)(2/3)c(j)=p c(j).
\]

Thus the complete derivative majorant

\[
 B_{ef}=3\sum_{p,S\ni e,f,j}\xi^p j_ej_f\|A_{S,j,[p]}\|_1
\]

is symmetric, nonnegative, and obeys

\[
 \boxed{\sup_e\sum_fB_{ef}\le\frac{32\xi}{\sqrt{1-256\xi/3}}.} \tag{S12}
\]

The same bound and the tail S3 retain all cross-link derivatives and their spatial tails. Each X-coordinate group translation is an isometry, and its diameter is 2pi. Integrating the derivative along the original group paths proves

\[
 |b_e(U)-b_e(V)|\le\sum_fB_{ef}\operatorname{dist}_X(U_f,V_f). \tag{S13}
\]

On each coefficient the three-vector derivative has norm at most sqrt(3)j_e||A||_1. G6 bounds this by sqrt(3)c||A||_1/6. If the original line-graph ball of radius 3P around e is contained in E_L, source compatibility therefore gives

\[
 t_e(L):=\|b_e^\infty-b_e^L\|_\infty
 \le\frac{\sqrt3}{6}\sum_{p>P}a_p,
 \qquad t_e(L)\le\frac{\sqrt3}{6}r.                      \tag{S14}
\]

For e outside the box set b_e^L=0. The second bound still applies. All t_e(L) tend to zero at fixed e. No full-volume norm convergence of a density is asserted.

## S5. Direct convergence of the original dynamics

Use the original link diffusion

\[
 dU_e^L=\sqrt{2\kappa}\sum_\alpha T_\alpha U_e^L\circ dB_{e,\alpha}
        +2\kappa\sum_\alpha b_{e,\alpha}^L(U^L)T_\alpha U_e^Ldt,
                                                               \tag{S15}
\]

with free copies outside the box and the same countable Brownian family for all boxes. Its generator is -A_L on inside functions by G2. Let R_e be the free group Brownian solution with R_e(0)=I and write U_e^L=R_e V_e^L. The Stratonovich product rule gives the original random ordinary equation

\[
 \dot V_e^L=2\kappa
      R_e^{-1}\bigl(\sum_\alpha b_{e,\alpha}^L(U^L)T_\alpha\bigr)R_e V_e^L.
                                                               \tag{S16}
\]

Conjugation rotates the three coefficient coordinates orthogonally. Comparing two such ordinary equations by the triangle inequality after a common infinitesimal group translation gives, for z_e=dist_X(U_e^L,U_e^M),

\[
 z_e(t)\le2\kappa\int_0^t
       [(Bz(s))_e+t_e(L)+t_e(M)]ds.                     \tag{S17}
\]

At the cut locus the same upper-Dini-derivative bound follows from the metric triangle inequality. Iterating S17 with w=t(L)+t(M) gives

\[
 \sup_{s\le t}z_e(s)
 \le\sum_{j\ge0}\frac{(2\kappa t)^{j+1}}{(j+1)!}(B^jw)_e. \tag{S18}
\]

The iterated remainder is at most 2pi(2kappa B_*t)^N/N! and vanishes. Every fixed matrix power tends to zero by S12–14, and the exponential tail is uniform on compact time intervals. The convergence is deterministic and uniform in the initial configuration and common Brownian paths. It constructs the limiting process; S17 with w=0 proves its pathwise uniqueness.

For every smooth cylinder F, S18 proves uniform convergence of T_L(t)F to T(t)F on compact physical time intervals. Smooth cylinders are dense in the continuous functions on the compact countable product, so positivity and contraction extend the convergence and the semigroup law to that space. The generator on cylinders is the unchanged expression

\[
 A_\infty F=\kappa K F-2\kappa\sum_{e,\alpha}b_{e,\alpha}^\infty X_{e,\alpha}F.
                                                               \tag{S19}
\]

Its uniform bound on each fixed cylinder also proves strong continuity. On the conditional domain S8, finite reversibility and S3's proved measure convergence pass to the limit, making T(t) a strongly continuous self-adjoint Markov contraction semigroup on L^2(nu). Sections S11 and S13 prove the measure convergence on the remaining subcritical and critical domain, and then use this same reversibility argument. The resulting generator is nonnegative and self-adjoint; its construction uses the displayed finite dynamics and their actual limit.

## S6. Full physical gap in the unique volume limit

For a fixed physical cylinder F, its support is inside every sufficiently large E_L. The original finite semigroup then acts only inside, so the full PHYSICAL estimate G26 applies before passage to the limit. Uniform semigroup convergence and weak measure convergence give

\[
 \|T(t)(F-\nu F)\|_{L^2(\nu)}
 \le e^{-\kappa d_{\rm phys}t}\|F-\nu F\|_{L^2(\nu)}.
\]

Gauge averaging of dense cylinder approximations proves their density in the physical L^2 space. Hence

\[
 \boxed{A_\infty|_{L^2_{\rm phys}(\nu)\cap1^\perp}
           \ge\kappa d_{\rm phys}(\xi).}                 \tag{S20}
\]

The scalar limit retains G27. Its extended finite outside factors have the original free scalar gap 3kappa/4, at least kappa d_sc; this proves the scalar semigroup bound too. No scalar estimate is substituted for S20's sharper physical input.

All original time-ordered local correlations converge by repeated uniform semigroup convergence and the same vacuum measure limit. The exact map from the correlation Hilbert space is [O,t]->T(t)(O-nu O); its pairings equal the original limiting correlations, and its zero-time physical cylinder range is dense. Its inverse is completion of those same cylinder vectors. This identifies the complete constructed physical generator and preserves its raw inner product.

For the elementary loop, the predecessor's original pointwise density comparison and exact gradient give

\[
 \operatorname{Var}_\nu(F)\ge e^{-128\pi\xi},\quad
 q_\infty(F-\nu F)\le4\kappa,
\]
\[
 e^{-128\pi\xi}-4\kappa t\le C_F(t)
       \le C_F(0)e^{-\kappa d_{\rm phys}t}.              \tag{S21}
\]

Thus the constructed centered physical space contains a quantitatively nonzero finite-energy vector. The uniform first moment and the full gap retain, respectively, zero energy-infinity mass and zero zero-energy mass in its centered spectral measure. These endpoint statements are at fixed a,g in S8.

## S7. Source estimates and original response kernels

The source quotient of G4 and the labelled-assembly quotient of G9–12 retain their actual kernels. G30 bounds the original physical gradient primitive after their coefficient estimates are returned through the explicit eigenfunction map. The physical restriction in G31 carries the unchanged Schur residual and minimum-section identities to the stronger inverse bound. This includes the original section correction; a prescribed local trial is not relabelled a minimum section without that correction.

The new finite-band map B24–25 preserves its full original Gram G_xi. The Fourier transform B26 is an additional exact map on the calculated second coefficient, with both inverse laws and its original momentum measure. It does not identify a finite coefficient window with all physical states. Full physical coercivity came from G26 on every eigenfunction and then on the whole form domain.

## S8. The admitted source at the closed endpoint

At xi=3/256 the local coefficient sum and the original finite-box vacuum remain well-defined by G19. It gives a uniform algebraic tail and fixed-edge drift convergence through S14. The derivative series S3 and the Dobrushin bound S7 are not assigned finite values there. The conditional-coupling proof in S2–6 uses exactly S8. The additional full-domain argument S10–14 below uses a different, explicitly derived semigroup estimate; it never assigns a finite value to the divergent derivative series at theta=1.

## S9. Original continuum path and the domains actually reached

Keep a_n=a_0 2^-n and c_n=g_0^-2+beta n log2, with g_n^2=1/c_n and beta>0. The full finite-regulator physical result G22 applies exactly for

\[
 c_n\le\sqrt3/8.                                       \tag{S22}
\]

The conditional-comparison volume construction in S2–6 has c_n^2<3/[16(2+sqrt13)]; its closed benchmark is c_n<=2/11. The stronger construction in S10–14 reaches the full closed domain S22. The isolated physical band has c_n<sqrt3/10. These domains are larger than the preceding c_n<=1/15 domain, but c_n increases without bound, so none is assigned to the full n->infinity path.

At a fixed admissible g, the a_n->0 limit has

\[
 \Delta_n\ge (2g^2/a_n)d_{\rm phys}\longrightarrow\infty. \tag{S23}
\]

The original bounded centered positive-time correlations then vanish by the displayed exponential estimate, with any retained nonzero zero-time mass in the energy-infinity endpoint. The physical second-band propagation coefficients in B29 also keep their actual powers of a and g. No energy multiplier has been selected to force a continuum dispersion.

The completed output is a sharper full physical primitive bound, an actual interacting plaquette band with a uniform analytic error, and unique spatial vacuum/dynamics on an enlarged explicit coupling domain. A nontrivial smooth four-dimensional continuum field and a finite positive continuum mass remain unevaluated. The next selected original quantity is the higher-order physical band/response under the original changing-coupling refinement; all kernels and original energy units remain attached.

## S10. Volume-independent mixing from the original Fourier dynamics

This argument strengthens the preceding conditional route. It holds on the complete CLOSED source domain 0<=xi<=3/256, at each finite box, without a hypothesis on q(xi).

For a smooth cylinder F in a finite box write the actual finite semigroup as

\[
 T_L(t)F=c(t)1+y(t),\quad c(t)=\int_H T_L(t)F,\quad y(t)=Q_H T_L(t)F.
\]

The Fourier spaces X_0,Y_0 are exactly G23. Smoothness of the original finite heat equation makes y(t) differentiable in X_0, with y(t) and its derivative controlled in all finite-volume smooth norms. In particular it is continuous in Y_0. This regularity follows directly from the original self-adjoint compact spectral resolution and elliptic regularity, with a smooth initial function; no volume-uniform regularity constant is required.

Its exact coefficient equation is

\[
 y'(t)=-\kappa K_L y(t)+2\kappa Q_H\sum_i(X_iv_L)X_i y(t).
                                                               \tag{S24}
\]

For f in Y_0, the right derivative at h=0 of sum_j |1-h kappa c(j)| ||A_j(f)||_1 equals -kappa||f||_(Y_0). Dominated convergence is justified by the summable bound kappa c(j)||A_j(f)||_1. Apply the triangle inequality to S24's first-order difference in X_0 and use G23. The upper-right derivative therefore obeys

\[
 D^+\|y(t)\|_{X_0}\le-\kappa(1-\epsilon)\|y(t)\|_{Y_0}. \tag{S25}
\]

The norm is locally absolutely continuous because y is X_0-differentiable. Integrating the inequality and using ||y||_Y>=c_*||y||_X gives

\[
 \|y(t)\|_{X_0}\le e^{-\kappa c_*(1-\epsilon)t}\|Q_HF\|_{X_0},
\]
\[
 \kappa(1-\epsilon)\int_t^\infty\|y(s)\|_{Y_0}ds
       \le\|y(t)\|_{X_0}.                               \tag{S26}
\]

Here c_*=3 for physical F by G8, and c_*=3/4 for unrestricted scalar F. The mean equation retains the original constant contribution:

\[
 c'(t)=2\kappa\int_H\sum_i(X_iv_L)X_i y(t),\qquad
 |c'(t)|\le\kappa\epsilon\|y(t)\|_{Y_0}.                \tag{S27}
\]

The full coefficient product bound before Q_H proves the latter inequality with the same epsilon. S26 proves that c(t) tends to a constant c_infinity and that

\[
 |c_\infty-c(t)|\le\frac{\epsilon}{1-\epsilon}\|y(t)\|_{X_0}.
\]

The actual finite vacuum is invariant under T_L; uniform convergence to c_infinity therefore identifies c_infinity=int rho_L F. Combining these identities proves the volume-independent SUPREMUM-norm estimate

\[
 \boxed{
 \|T_L(t)F-\langle F\rangle_{\rho_L}\|_\infty
 \le\frac{\|Q_HF\|_{X_0}}{1-\epsilon}
        e^{-\kappa c_*(1-\epsilon)t}.}
                                                               \tag{S28}
\]

Every function, original Haar mean, vacuum mean, and constant drift term is retained. The initial Fourier norm of a fixed cylinder is identical in every larger box: all additional spin indices are trivial with dimension one and Haar integral one. Consequently S28 has no volume-dependent prefactor. For the actual elementary plaquette trace its initial norm is exactly 8, by G14.

This proof uses the actual finite semigroup, rather than assuming that an auxiliary Banach semigroup agrees with it. The coefficient estimates were applied to its smooth solution, and S27 reconstructs its constant component explicitly.

## S11. Full subcritical volume convergence without the conditional row restriction

For every theta<1, the drift row bound S12 is finite, regardless of the value of the conditional row bound q. The direct dynamical construction S13–19 therefore gives uniform convergence of T_L(t)F on compact time intervals for every cylinder F throughout 0<=xi<3/256.

Fix a common original configuration U. By S28,

\[
 |\langle F\rangle_{\rho_L}-\langle F\rangle_{\rho_M}|
 \le |T_L(t)F(U)-T_M(t)F(U)|
       +\frac{2\|Q_HF\|_{X_0}}{1-\epsilon}
                          e^{-\kappa c_*(1-\epsilon)t}. \tag{S29}
\]

First let L,M grow at fixed t; the first term tends to zero. Then let t grow. This proves Cauchy convergence of the entire vacuum expectation sequence on every matrix-coefficient cylinder polynomial. Positivity and the uniform supremum bound extend the limit to a probability nu on the compact countable configuration space. The same convergence holds for all continuous functions by density. Passing S28 to the limit gives

\[
 \|T(t)F-\nu F\|_\infty
 \le\frac{\|Q_HF\|_{X_0}}{1-\epsilon}
               e^{-\kappa c_*(1-\epsilon)t}.            \tag{S30}
\]

Every invariant probability of this limiting semigroup has the same expectation of every such F by S30, hence equals nu. This proves uniqueness of its invariant vacuum measure. Reversibility, self-adjointness, physical density, and all time-ordered correlations return by the exact arguments S5–6. Thus S20 holds for every subcritical 0<xi<3/256, not merely on the smaller S8 domain.

## S12. An explicit coupling modulus for the full original semigroup and vacuum

Treat (kappa,xi) as the two retained positive operator coefficients. Their inverse physical parameter map is

\[
 g^2=1/(2\sqrt\xi),\qquad a=1/(\kappa\sqrt\xi).
                                                               \tag{S31}
\]

For xi>0 the two displayed maps are mutual inverses by substitution. At xi=0 only the auxiliary operator kappa K_L is used; no finite physical a,g are assigned by S31. The identity on original link-index configurations compares two such coefficient pairs. It changes neither a link word nor a matrix coefficient, and S31 records its effect on the physical parameters. In the following comparison kappa is fixed and no energy factor is divided out.

For 0<=xi<=eta<=3/256, the full positive coefficient majorant yields

\[
 \|v_L(\eta)-v_L(\xi)\|_{\mathrm{loc},1}
       \le r(\eta)-r(\xi).
                                                               \tag{S32}
\]

Indeed expand each original coefficient in powers and sum (eta^p-xi^p)||v_[p]||. G16 evaluates their entire sum. This also holds at the endpoint by G19.

Differentiate T_(L,eta)(t-s) T_(L,xi)(s)F on the original smooth source. Integrating the product rule gives the full Duhamel formula with difference generator

\[
 2\kappa\sum_i X_i(v_L(\eta)-v_L(\xi))X_i.
\]

The Markov contraction in the target supremum norm, G23 before its mean projection, and S26 on the xi evolution give

\[
 \boxed{
 \sup_{t\ge0}\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
 \le\frac{\epsilon(\eta)-\epsilon(\xi)}{1-\epsilon(\xi)}
                         \|Q_HF\|_{X_0}.}              \tag{S33}
\]

Every density and drift in this expression is its own actual finite vacuum. The bound is independent of the original box size and of t. Sending t to infinity with S28 proves the same bound on |<F>_(rho_L,eta)-<F>_(rho_L,xi)|. This supplies a quantitative coupling comparison, not an assertion of uniform analytic control beyond the constructed interval.

## S13. The closed source endpoint has a unique spatial vacuum and dynamics

Put xi_c=3/256 and s_xi=sqrt(1-256xi/3). The modulus in S33 becomes exactly

\[
 \frac{\epsilon(\xi_c)-\epsilon(\xi)}{1-\epsilon(\xi)}
       =\frac{s_\xi}{1+s_\xi}\longrightarrow0.
                                                               \tag{S34}
\]

For fixed xi<xi_c the complete subcritical volume convergence was just proved. Compare two finite boxes at xi_c by inserting their evolutions at xi; S33 bounds the two outer differences by twice S34 times ||Q_HF||_X, uniformly in physical time. Let L,M grow first, then xi increase to xi_c. This proves uniform convergence on compact time intervals of the entire critical family T_(L,xi_c)(t)F.

The limit preserves the semigroup law, positivity and constants. Its strong continuity follows from the finite generator bound on each cylinder: b_e^L is uniformly bounded by sqrt(3)r/6 even at the endpoint, and the cylinder has finitely many original derivatives. G19 and S14 give convergence of each drift coefficient. Thus the limit generator on cylinders is the original expression S19. This argument does not assign a finite value to the divergent derivative majorant S3 at the endpoint, and does not claim the S16 pathwise-uniqueness proof there. It constructs the critical dynamics as the unique uniform limit of the original finite semigroups.

The finite mixing estimate S28 remains valid at epsilon=1/2. The Cauchy argument S29 now proves the full critical vacuum-measure limit. S30 makes this measure the unique invariant probability of the limiting semigroup. Finite reversibility passes to the limit and supplies the self-adjoint generator and its complete physical representation. The spectral, raw-metric, nontriviality and correlation arguments of S6 apply unchanged.

Consequently the final unique-volume domain is the full CLOSED domain

\[
 \boxed{
 0<\xi\le3/256,\qquad g^2\ge8/\sqrt3,
 \quad A_\infty|_{\mathrm{phys}\cap1^\perp}
           \ge\tfrac32\kappa(1+\sqrt{1-256\xi/3}).}      \tag{S35}
\]

The same supremum-norm mixing and coupling modulus hold on the limiting cylinder algebra by passage through the proved maps. Both the source tail and its physical return are controlled at the endpoint.

## S14. Final continuum scope

The full spatial statement S35 reaches c_n<=sqrt3/8 on the original running path, including equality. S8 remains the smaller domain of the separately proved conditional-influence comparison. The physical band and Cauchy-remainder domains remain those in B1 and B10. For beta>0, c_n still grows beyond sqrt3/8 after finitely many steps. No estimate in this continuation assigns the strong-coupling source or its band to that later part of the path.

The new quantitative coupling estimate S33 is an explicit tool for continuing the original Hamiltonian family; it does not assert extension to g approaching zero. The four-dimensional smooth-continuum field, a finite positive continuum mass, and the required change in physical scaling remain unevaluated. The completed results keep their full physical domains and all original observables, source relations, state norms and generator maps.
