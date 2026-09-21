# Full sixth-degree plaquette response and a certified two-spacing correlation

18 September 2026. This note returns the complete eighth energy coefficient to the original state, energy and time pairings. It proves its own finite-volume analytic remainder from the original free physical gap and bounded plaquette multiplication. The radius depends on the actual number M of plaquettes. No historical uniform-coupling estimate is used to remove that dependence.

## A1. Original analytic branch on an explicit finite-volume domain

Retain H(x), K, W_p, kappa, the original product Haar measure and all vertex gauge constraints from S1–S4 of `SIXTH_SOURCE.md`. The free physical constant is the unique zero eigenvector of K. A nonconstant physical Fourier component has an active edge graph whose vertices have no degree one: a single nonzero SU(2) representation at a vertex has no invariant vector. Every finite active component therefore contains a cycle. The original cubic graph has neither doubled edges nor triangles, so at least four nonzero edges occur. Their original Casimirs are each at least 3/4. Hence

    K|_(physical,1-perp)>=3.                                 (A1)

The invariant part of the original compact product-group Laplacian has domain H^2_phys, compact resolvent and form domain H^1_phys. This follows from its product representation decomposition, or equivalently the compact elliptic Laplacian. Original smooth bounded plaquette multiplication preserves the operator domain.

For the complex original source vector x, set B(x)=-sum_p x_p W_p. Its bound is

    ||B(x)||<=2||x||_1.                                      (A2)

On |z|=3/2, A1 gives ||(K-z)^(-1)||<=2/3. Thus I+B(x)(K-z)^(-1) has its convergent Neumann inverse for ||x||_1<3/4. The contour projection of K+B(x) is analytic throughout that ball; along the radial path from zero it has constant rank one. Its unique enclosed eigenvalue is the analytic e(x) with e(0)=0.

For ||x||_1<=3/8, the perturbation norm is at most 3/4. The same resolvent factorization outside the ||B||-neighbourhood of spec(K) confines the enclosed eigenvalue to |e|<=3/4: points inside |z|<3/2 cannot be within 3/4 of the remaining spectrum starting at three. Therefore

    |e(x)|<=3/4 on ||x||_1<=3/8.                             (A3)

For real x in this region, the min-max principle on the same physical domain gives

    gap(K+B(x))>=3-4||x||_1>=3/2.                            (A4)

The contour branch is consequently the actual ground energy, and its strictly positive smooth unit eigenvector psi_x exists by the elliptic maximum principle and the modulus form inequality. Ground-state simplicity also follows directly from the original identity

    q_(H-E0)(psi_x f)=kappa int psi_x^2 sum_i|X_i f|^2.        (A5)

This identifies the branch and the physical vacuum used below. It proves each inverse below on the actual centered space; no unknown mass-gap lower bound is imposed as a hypothesis.

The analytic source coefficients also have their original smooth domains. Near x=0, the contour projection applied to 1 has a nonzero Haar coefficient. Dividing by that retained scalar gives the section u of E1, and its inverse multiplies by the same scalar. The equation Ku=(e+S(x))u first gives graph-norm analyticity. Each original W_p is smooth, and multiplication by it is bounded on every fixed Sobolev space of this compact product. Repeating the equation and elliptic regularity gives analyticity in H^{2r} for every finite r. Sobolev embedding at a sufficiently large r gives C^k analyticity for any chosen k. For real sources near zero, u remains positive in C^0, so its original logarithm is analytic there as well. Subtracting its explicitly retained Haar scalar gives precisely v and S6. This establishes that the unique finite coefficient solutions calculated in the source catalogue are the actual Taylor coefficients of this original vacuum.


## A2. Scalar symmetry and the full physical energy remainder

Let C be the original Haar-unitary link-center substitution

    U_(n,i) -> (-1)^(sum_(j<i)n_j)U_(n,i).

It preserves K and reverses every original W_p. In the complete Hamiltonian,

    C H(x) C^(-1)=H(-x)+4kappa sum_p x_p I.                   (A6)

The original scalar 2 kappa sum_p x_p is retained on both sides. After using its specified decomposition E0(x)=kappa[2 sum x_p+e(x)], uniqueness of the analytic branch gives e(-x)=e(x).

Put M=|P_L| and

    R=3/(8M).                                                (A7)

The homogeneous line x_p=z satisfies ||x||_1=M|z|. A3 and Cauchy's coefficient formula bound the nth coefficient of e(z*1) by (3/4)R^(-n). Summing the even terms from degree ten yields

    |e(xi)-e2,L xi^2-e4,L xi^4-e6,L xi^6-e8,L xi^8|
      <=(3/4)(|xi|/R)^10/[1-(|xi|/R)^2],  |xi|<R.            (A8)

Multiplication by kappa returns the physical energy remainder. The complete coefficients e2,L through e8,L, with their original boundary terms, are in E16–E21 of `EIGHTH_ENERGY.md`. At L=2, M=240, R=1/640.

## A3. Actual source derivatives and the original zero-energy response

Write A=H-E0, rho=psi_x^2. The multiplication map

    U_psi:L^2(rho dU)->L^2(dU),  f->psi_x f,
    U_psi^(-1)h=h/psi_x

has both inverse identities and pairing

    <U_psi f,U_psi h>=int rho conjugate(f)h dU.               (A9)

Let z_p=partial_(x_p)v and Z_p=z_p-<z_p>_rho. Differentiating the original unit mass in S4 gives

    partial_p c=-<z_p>_rho,    partial_p psi=psi Z_p.          (A10)

The original derivative of the Hamiltonian is kappa(2-W_p). Differentiating its actual eigen-equation, with the original scalar included, yields

    partial_p E0=kappa(2-<W_p>_rho),
    Atilde Z_p=kappa(W_p-<W_p>_rho),
    Atilde=U_psi^(-1) A U_psi.                               (A11)

For the actual centered physical states r_p=(W_p-<W_p>_rho)psi, define

    mathcal R_pq(x)=kappa<r_p,A^(-1)r_q>
                  =-1/2 partial_p partial_q e(x)
                  =q_Atilde(Z_p,Z_q)/kappa.                 (A12)

The real positive vacuum and real trace functions make these real symmetric entries; complex combinations give the full Hermitian positive semidefinite form. To prove the middle equality, differentiate <W_p> using A10 and use A11 to write its derivative as 2kappa<r_p,A^(-1)r_q>. This keeps all off-diagonal pairings.

The full finite-volume gap A4 proves convergence of the physical time integral

    int_0^infinity <r_p,exp(-tA)r_q>dt=mathcal R_pq/kappa.     (A13)

The factor 1/kappa remains attached to the original physical time. Neither a coefficient matrix nor its source norm replaces the actual pairing in A12.

## A4. A separate analytic bound for the response through degree six

Set

    r=3/(16M),    a_src=3/32.                                 (A14)

For |z|<=r and |u|,|w|<=a_src, the original vector z*1+u e_p+w e_q has l1 norm at most 3/8. The two-source Cauchy integral applied to A3 gives

    |partial_u partial_w e(z*1+u e_p+w e_q)|_(u=w=0)
      <=(3/4)/a_src^2=256/3.                                 (A15)

This includes p=q: u and w are two independent variables for the same original face coordinate, so partial_u partial_w is exactly partial_p^2. By A12, |mathcal R_pq(z*1)|<=128/3. A6 makes this homogeneous response even. Thus

    |mathcal R_pq(xi)-(R0)_pq-xi^2(R2)_pq-xi^4(R4)_pq-xi^6(R6)_pq|
      <=(128/3)(|xi|/r)^8/[1-(|xi|/r)^2],   |xi|<r.           (A16)

The actual M remains in r. Contracting by any finite coefficient vector h gives a quadratic-form error bounded by the right side times (sum_p |h_p|)^2, which keeps all mixed terms.

## A5. Complete original response matrices through degree six

The retained lower matrices are R0=I/3 and

    R2=-(5/36)I+(2/1053)D_degree+(4/1053)A_adj.                (A17)

The complete original R4, including all three-face and cube contributions, is preserved in the predecessor `20260917-fifth-source/PLAQUETTE_RESPONSE.md` and its finite-box tables. No bulk diagonal is substituted for an original boundary row.

For the complete eighth energy monomials sum_(|nu|=8)e_nu x^nu, the new coefficient is

    (R6)_pq=-1/2 sum_(|nu|=8) e_nu nu_p(nu_q-delta_pq).        (A18)

The sum is over the actual original embeddings in the specified box. Each face, multiplicity, and pair of derivative directions remains in A18. The 80 complete coefficients are classified and calculated in E3–E4.

The producer independently enumerates every fitting translate and checks membership in the original box face list before applying A18. For L=2, `generated/response6_L2.json` contains the original ordering of 240 faces and all 20,796 nonzero entries. It verifies the exact adjoint symmetry and the complete scalar return

    sum_(p,q)(R6)_pq=-28 e8,L.                                (A19)

The factor 28 is 8*7/2 from twice differentiating the same homogeneous energy, not a discarded count of mixed derivatives. Each individual matrix entry has the analytic error A16 when combined with R0,R2,R4.

## A6. A positive actual response across two original lattice spacings

Use the original horizontal faces

    p=(0,0,0;0,1),    q=(0,0,2;0,1).                         (A20)

Their centers differ by the original displacement 2e_2. In the L=2 box both faces and all contributing intermediate faces are contained. R0 and R2 give zero. A pair of these faces cannot lie in one elementary cube or a connected triple of faces, so the complete previous R4 entry is also zero; the retained finite matrix verifies this directly.

At degree six, A18 has exactly four nonzero original contributions. Each consists of p,q and the two successive side plaquettes on one side of the two-cell column. All four doubled face-multisets are explicitly listed in `energy8_response.json`. Their actual coefficient is E15. The two cube families E13–E14 cannot span A20 at this total order: an attached face shares an original cube edge, whereas the second horizontal face in A20 is one complete spacing beyond the nearest cube face.

Thus

    (R6)_pq=-8 c_path4=41237423/5039315143200.                 (A21)

The same value is obtained from the complete 240-face matrix and independently from all original bulk translates containing p. The original four individual contributions remain in the record.

Take the actual parameters

    xi=1/10^18,  g^2=500000000,  kappa=1000000000/a,
    M=240, r=1/1280, a>0.                                   (A22)

Let

    E_R=(128/3)(1280xi)^8/[1-(1280xi)^2].                     (A23)

The exact rational certificate evaluates c_path_response-E_R/xi^6 and c_path_response+E_R/xi^6, proving

    81828/10^10 < mathcal R_pq(xi)/xi^6 < 81835/10^10.         (A24)

All endpoints are rational and checked without floating acceptance tests. In decimals these are 8.1828*10^(-6) and 8.1835*10^(-6). The original integrated connected correlation is strictly positive, with bounds obtained by multiplying A24 by xi^6/kappa. This states the sign of its full time integral; no pointwise-in-time sign is assigned from that calculation.

A22 is a large-coupling finite-volume certificate. Its error radius is the actual A14. No infinite-volume or continuum analytic conclusion is assigned to this particular bound.

## A7. Coefficientwise spatial Fourier return with the original orientation norm

Every degree-six response coefficient has a finite original support. Once that support is inside a box, its coefficient is unchanged. This gives a coefficientwise bulk finite-range kernel. Its complete anchor rows for orientations a=0,1,2, with planes (1,2),(0,2),(0,1), are stored in `generated/response6_bulk.json`.

For an original counting-norm coefficient sequence f_a(n), let c_a=(e_i+e_j)/2 be the actual face-center offset. The Fourier map and inverse are

    fhat_a(k)=sum_n exp[-i k.(n+c_a)]f_a(n),
    f_a(n)=(2pi)^(-3)int_[-pi,pi]^3 exp[i k.(n+c_a)]fhat_a(k)dk. (A25)

Orthogonality of the original exponentials proves both inverse laws on finite sequences and the same Plancherel pairing with the displayed measure. A matrix entry from (n,a) to (n+d,b) has the original phase exp[i k.(d+c_b-c_a)]. The full transpose/negative-displacement involution gives the Hermitian symbol.

At k=0, the sixth coefficient on the original scalar orientation direction (1,1,1) is

    -1703320005700992315276593/7310924807465423813760000.       (A26)

On the zero-sum orientation plane it is

    347891210081791900228897/20470589460903186678528000.        (A27)

The complete original frame (1,1,1),(1,-1,0),(1,1,-2) has Gram diag(3,2,6). Its inverse coordinate map is

    x -> ((x0+x1+x2)/3,(x0-x1)/2,(x0+x1-2x2)/6).              (A28)

Multiplication proves both inverse identities and the stated Gram. Equations A26–A27 do not change that metric. A26 also equals -28 times the eighth energy per original plaquette in E19, as the full scalar Hessian sum requires.

The complete two original orientation coefficient series through xi^6 are

    R_scalar(0,xi)=1/3-(11/156)xi^2
       +(211396463/938298816)xi^4
       -(1703320005700992315276593/7310924807465423813760000)xi^6,

    R_zero_sum(0,xi)=1/3-(163/1404)xi^2
       -(22137985/938298816)xi^4
       +(347891210081791900228897/20470589460903186678528000)xi^6,
                                                                    (A29)

with the higher coefficients still to be determined. These are exact coefficientwise spatial returns, not an assignment of the finite-volume analytic radius to infinite volume.

## A8. Original plaquette readout through seventh degree

Define the actual original average half-trace

    P_L(xi)=(1/(2M))sum_p <W_p>_rho.                          (A30)

The map from the original trace expectation to this specified readout retains its factor 1/(2M). Differentiating the complete physical energy at fixed kappa gives

    dE0/dxi=kappa[2M-sum_p<W_p>_rho].                         (A31)

The derivative of the original unit-vacuum mass cancels the two eigenvector derivative terms; no change of physical pairing is made. Consequently

    P_L=xi/3-(2e4,L/M)xi^3-(3e6,L/M)xi^5-(4e8,L/M)xi^7
          +retained tail.                                   (A32)

Differentiating the absolutely convergent scalar coefficient series from A3, with t=|xi|/R, proves

    |tail in A32| <= t^9(10-8t^2)/(1-t^2)^2,   |xi|<R.       (A33)

Indeed the coefficient factor is (3/4)/(2MR)=1 for the specified R=3/(8M); the entire dependence on M remains in t. This derivative estimate comes from the full Cauchy coefficient bound, not differentiation of an unsigned pointwise remainder alone.

Its coefficientwise spatial seventh coefficient is -4 times E19. The existing third and fifth coefficients remain -11/468 and 211396463/4691494080, respectively. E17 supplies every boundary correction for finite L.

## A9. Scope, next original quantity and evidence

The completed outputs are every sixth source coefficient, its original scalar and signed derivative equations, all 80 eighth energy coefficients, the complete sixth-degree response matrix and symbol, and the actual finite-volume bound A24. The archive retains the source-to-physical equations A9–A13 and the finite-volume parameter range A14–A16.

The standing simultaneous continuum path has a_n=a_0*2^(-n) and g_n^2=1/(g_0^(-2)+beta*n*log 2). This note derives no lower bound on the full continuum spectrum along that path. In particular M enters A7 and A14. The historical volume-uniform gap claims remain at their prior audit scope; neither the new finite coefficients nor their checksum records recertify those analytical arguments.

The next source coefficient is the original v_[7]=2B(v_[1],v_[6])+2B(v_[2],v_[5])+2B(v_[3],v_[4]). The sixth table is a completed input, while S31 retains the full residual of the current q_6. A quantitatively useful next response task is to evaluate that original residual and its energy pairing on growing supports, keeping the finite-volume radius and all scalar returns explicit. No automatic continuation, paid model job or remote merge is started by this checkpoint.

## A10. A sharper original-Haar Schur bound and its complete Cauchy return

The exact original Haar matrix elements give more information than A2 alone. Let P_H be the original rank-one projection onto 1, and Q_H=I-P_H. For distinct elementary faces p,q, at least one original link belongs to just one of them; its central sign makes the Haar integral of W_p W_q zero. For one face, retain U_1,U_2,U_3 and set Omega=U_1 U_2 U_3^(-1) U_4^(-1). The inverse is U_4=Omega^(-1)U_1 U_2 U_3^(-1). Fubini and original Haar translation/inversion invariance carry its measure to the Haar measure of Omega and the three retained links. In the quaternion coordinates Omega=q_0 I-i sum q_a sigma_a, the four second moments are equal and their sum is one; hence int q_0^2=1/4. Since tr(Omega)=2q_0, its squared Haar norm is exactly one. Thus

    P_H W_p=0,   <W_p,W_q>_H=delta_pq.                       (A34)

The map U:C plus Q_H H_phys -> H_phys, U(c,h)=c*1+h, has inverse (P_H f,Q_H f) and preserves the original pairing |c|^2+<h,h>_H. In this exact decomposition put

    V_x=-sum_p x_p W_p,
    W_x=Q_H V_x i,   Z_x=i* V_x Q_H,
    D_x=Q_H K Q_H+Q_H V_x Q_H,
    i:C->H_phys, i(c)=c*1,  i*f=P_H f.                      (A35)

Its block matrix is [[0,Z_x],[W_x,D_x]], with original domain C plus (H^2_phys intersect Q_H H_phys). Both original off-diagonal norms satisfy

    ||W_x||=||Z_x||=(sum_p |x_p|^2)^(1/2)<=||x||_1.          (A36)

For the row this follows by applying the original adjoint to 1: V_x*1=-sum_p conjugate(x_p)W_p. Thus A36 holds for the complex sources used by the Cauchy integrals, as well as for real parameters.

Fix 0<rho<3/4 and ||x||_1<=rho. The already constructed analytic ground eigenvalue obeys |e(x)|<=2rho by the original resolvent factorization. Since 3-2rho-|e|>=3-4rho>0, the same factorization on the full Q_H block gives

    ||(D_x-e)^(-1)||<=1/(3-2rho-|e|).                       (A37)

The eigenvector's P_H component is nonzero: otherwise it would be a kernel vector of the invertible D_x-e. Solving the second block and substituting in the first therefore proves the literal scalar relation

    e(x)=-Z_x(D_x-e(x))^(-1)W_x.                            (A38)

Every physical Q_H direction remains in this inverse. Equations A36–A38 give

    |e|(3-2rho-|e|)<=rho^2.                                 (A39)

The two roots of t(3-2rho-t)=rho^2 are

    h_-(rho)=(3-2rho-sqrt(9-12rho))/2,
    h_+(rho)=(3-2rho+sqrt(9-12rho))/2.                       (A40)

Along the actual path x -> s*x, 0<=s<=1, the same fixed-rho estimate holds and |e(s*x)| is continuous, starting at zero. The interval (h_-,h_+) is excluded by A39. It follows that

    |e(x)|<=h_-(rho) on ||x||_1<=rho<3/4.                   (A41)

This is a proved bound on the original analytic branch, not a supplied spectral assumption. At the explicit value rho=20/27, the two roots are 16/27 and 25/27. Hence

    |e(x)|<=16/27 on ||x||_1<=20/27.                        (A42)

For real sources in this ball, the original min-max gap is at least 3-4rho=1/27, so the branch remains the actual simple physical ground energy. The positive-source example below lies far inside this finite-volume region.

The following Cauchy radii keep the same original parameter coordinates:

    R_*=20/(27M),
    r_*=16/(27M),   a_*=2/27,
    M r_*+2a_*=20/27.                                       (A43)

Using A42 on the original homogeneous line improves the complete energy tail to

    |E0,L-kappa[2Mxi+sum_(j=1)^4 e_(2j),L xi^(2j)]|
      <=(16kappa/27)(|xi|/R_*)^10/[1-(|xi|/R_*)^2].         (A44)

Using the two original source circles of radius a_* gives

    |mathcal R_pq(z*1)|<=(16/27)/(2a_*^2)=54,
       |z|<=r_*,                                           (A45)

and the full response remainder is consequently

    |mathcal R_pq(xi)-sum_(j=0)^3 xi^(2j)(R_(2j))_pq|
      <=54(|xi|/r_*)^8/[1-(|xi|/r_*)^2].                    (A46)

Every inequality retains M and kappa. The earlier A8 and A16 remain valid independent bounds; A44 and A46 use the additional exact off-diagonal information A34.

The choice in A43 has an explicit optimality statement within this family of first-omitted-coefficient estimates. For fixed rho, with M r+2a=rho, the product a^2 r^8 is maximized at M r=4rho/5 and a=rho/10, by differentiation of 2log a+8log r. The constant to minimize is then h_-(rho)/rho^10 times the fixed factors 50(5M/4)^8. Introduce gamma=sqrt(9-12rho), with inverse rho=(9-gamma^2)/12. Direct substitution gives

    h_-(rho)/rho^10
      =12^9/[(3-gamma)^8(3+gamma)^10], 0<gamma<3.            (A47)

The logarithm of the denominator has derivative -8/(3-gamma)+10/(3+gamma) and strictly negative second derivative. Its unique maximum is at gamma=1/3, which gives rho=20/27. This optimizes the leading coefficient constant inside the displayed Cauchy family. The geometric tail factor in A46 is retained separately, rather than assigned the same optimization claim.

For the actual two-spacing faces A20, take the larger source and its original physical parameters

    xi=1/10^14,  g^2=5000000,  kappa=10000000/a,
    L=2, M=240, R_*=1/324, r_*=1/405.                      (A48)

Set E_*=54(405xi)^8/[1-(405xi)^2]. Inserting the complete calculated coefficient A21 into A46 gives the exact rational interval

    42744/10^10 < mathcal R_pq(xi)/xi^6 < 120919/10^10.       (A49)

The exact unrounded endpoints are stored in `generated/schur_remainder.json`. They are approximately 4.2744258723*10^(-6) and 1.2091854794*10^(-5). The original integrated connected correlation therefore lies strictly between the two bounds in A49 multiplied by xi^6/kappa. The same positivity holds for every smaller positive xi on this same finite graph, because E_*/xi^6 is increasing with xi in (0,r_*). The squared coupling in A48 is one hundredth of the earlier conservative example A22; the Hamiltonian, lattice spacing variable, and physical time are unchanged.

Finally, the improved scalar coefficient bound returns to the original plaquette readout A30. With t_*=|xi|/R_*, its uncomputed terms after xi^7 obey

    |tail in A32|
      <=(2/5)t_*^9(10-8t_*^2)/(1-t_*^2)^2.                 (A50)

The factor 2/5 is exactly (16/27)/(2M R_*). Thus the derivative estimate retains both the original readout factor 1/(2M) and the actual M-dependent analytic radius.

## A11. Retaining the exact source Gram enlarges the analytic domain

Equation A36 is an equality before its final l1 bound. Retaining it gives an additional independent estimate, including outside the original l1 ball of radius 3/4. For the original complex source define

    rho=||x||_1,  sigma=||x||_2,  d=3-2rho.

Consider the explicit open domain

    D={x: ||x||_1+||x||_2<3/2}.                             (A51)

On any fixed closed source set with ||x||_1<=rho0, ||x||_2^2<=eta0 and 4eta0<(3-2rho0)^2, put d0=3-2rho0>0. In the original blocks A35, the contour |z|=d0/2 has

    ||(D_x-z)^(-1)||<=2/d0,
    |Z_x(D_x-z)^(-1)W_x|<=2eta0/d0<|z|.                    (A52)

The first bound follows from K on Q_H being at least three and ||Q_H V_x Q_H||<=2rho0. The second uses the actual row and column norms sigma, including the conjugate coefficients in the row adjoint. The original block elimination therefore makes the full resolvent invertible on that contour. Along s*x, 0<=s<=1, the same bounds hold. Its contour projection has constant rank one, equal to the original constant projection at zero. This constructs an analytic simple branch on each such source set, without assuming a physical gap. The local branches agree on overlaps: their circles are concentric, each encloses exactly one eigenvalue, and the smaller circle's eigenvalue must also be the larger one's single eigenvalue. They give the same analytic branch throughout A51.

The selected eigenvalue satisfies |e|<d0/2. Applying the exact A38 to it now gives |e|(d0-|e|)<=eta0. The function t(d0-t) is strictly increasing on [0,d0/2], so

    |e(x)|<=h(d0,eta0):=(d0-sqrt(d0^2-4eta0))/2.            (A53)

In particular one may take the actual source norms by a limiting choice of the closed bounds. This proves |e(x)|<=h(3-2||x||_1,||x||_2^2) on A51. Every Q_H direction and every original plaquette remains in D_x; A52 estimates its full inverse.

For real sources, Q_H(K+V_x)Q_H>=d0. The original variational characterization with the one-dimensional excluded subspace span{1} gives lambda_1(K+V_x)>=d0. Its actual ground energy is at most <1,(K+V_x)1>=0. Thus the selected branch is that ground energy and

    gap(H(x))>=kappa d0.                                   (A54)

This is a finite-source estimate in the original physical space. On the homogeneous line its analytic domain is |xi|(M+sqrt(M))<3/2. It is not assigned a volume-independent xi radius. The min-max step and the analytic contour have their separate displayed source domains.

The two-source Cauchy calculation can retain this Gram instead of bounding it by rho0^2. For p!=q and |z|<=r, |u|,|w|<=a, the original source x=z*1+u e_p+w e_q obeys

    ||x||_1<=M r+2a=:rho0,
    ||x||_2^2<=M r^2+4ra+2a^2=:eta_distinct.                (A55)

Indeed the exact squared norm is M|z|^2+2Re(conjugate(z)(u+w))+|u|^2+|w|^2. For p=q its last two source terms combine, and the retained upper bound is instead

    eta_same=M r^2+4ra+4a^2.                                (A56)

There is no identification of the two source Grams. Their two inverse cases are the original distinct- and same-coordinate insertions. A53 and the Cauchy formula give respectively the response-circle constants h(d0,eta_distinct)/(2a^2) and h(d0,eta_same)/(2a^2), whenever the displayed closed-source inequalities in A52 hold. These apply to the actual original source polydiscs just constructed, and retain the full geometric tail on returning to xi.

For every original L>=2, M>=240. Choose the explicit common radii

    rho0=1,  d0=1,  r_**=6/(7M),  a_**=1/14.

Their original source budgets and Gram estimates are

    M r_**+2a_**=1,
    eta_distinct=48/(49M)+1/98<=1/70,
    eta_same=48/(49M)+1/49<=6/245.                           (A57)

Both satisfy 4eta<1. Direct rational multiplication gives

    (1/68)(1-1/68)>1/70,
    (1/39)(1-1/39)>6/245,
    1/68<1/2, 1/39<1/2.

Thus the exact smaller-root comparison A53 and the original two-source derivative give

    |R_pq(z*1)|<=49/34   for p!=q,
    |R_pp(z*1)|<=98/39,
    |z|<=6/(7M).                                           (A58)

The first constant is (1/68)/(2a_**^2); the second is (1/39)/(2a_**^2). These are two proved full-operator circle bounds, not replacements of an original norm by a chosen coefficient metric. The earlier optimized family A47 retained only the l1 source bound; A55–A58 use additional information from the exact original Haar Gram.

By the same exact source parity and Cauchy sum as A16, for distinct p,q the complete response tail after degree six is now

    |R_pq(xi)-sum_(j=0)^3 xi^(2j)(R_(2j))_pq|
       <=(49/34)(|xi|/r_**)^8/[1-(|xi|/r_**)^2].            (A59)

For a diagonal entry use 98/39. The complete quadratic-form error is bounded using the larger of the two constants and the original sum of coefficient absolute values, with all mixed entries retained.

For the original two-spacing faces A20 in the complete L=2 box, set

    xi=1/(4*10^12),  g^2=1000000,
    kappa=2000000/a,  a>0,  r_**=1/280.                     (A60)

The source equation xi=1/(4g^4) is exact. Let E_**=(49/34)(280xi)^8/[1-(280xi)^2]. The full coefficient A21 and A59 yield the rational interval

    47801/10^10 < R_pq(xi)/xi^6 <115862/10^10.               (A61)

The unrounded endpoints are approximately 4.7801443923*10^(-6) and 1.1586136274*10^(-5). Multiplication by xi^6/kappa returns the strict positive bounds on the original integrated connected correlation. This is a certificate of the complete finite-volume quantity. Its coupling, spacing, all 240 original plaquettes, and full spin spectrum remain. It supplies no pointwise-in-time positivity or volume-uniform analytic radius.

The same original-Gram calculation also sharpens the homogeneous energy circle. For |z|<=1/M, one has ||z*1||_1<=1 and ||z*1||_2^2<=1/M. Since M>=240, the full A52 contour applies. Moreover (2/M)(1-2/M)>=1/M and 2/M<1/2, so A53 gives |e(z*1)|<=2/M. Consequently the complete physical energy tail after degree eight satisfies

    |E0,L-kappa[2Mxi+sum_(j=1)^4 e_(2j),L xi^(2j)]|
      <=(2kappa/M)(M|xi|)^10/[1-(M|xi|)^2],  |xi|<1/M.     (A62)

The corresponding original average-half-trace tail after degree seven is at most

    (1/M)t^9(10-8t^2)/(1-t^2)^2,  t=M|xi|<1.              (A63)

The factor 1/M is exactly (2/M)/(2M*(1/M)), from the original readout derivative. The constant could also retain the exact smaller root h(1,1/M); A62–A63 use its displayed rational upper bound. The physical and volume factors have not been removed.

## A12. A two-sided native-energy bound for the full original plaquette family

The same circle also returns a quantitative bound for the entire 240-dimensional original observation family at a much wider real coupling range than the small off-diagonal sign certificate. Retain the complete original L=2 face order in `response6_L2.json` and the inherited degree-zero-through-four matrix. Their face arrays are exactly identical. The full absolute row sums give

    ||R_(2)||_2<=227/1404,
    ||R_(4)||_2<=3451329067/14074482240,
    ||R_(6)||_2<=43015053233874982762407882061
                 /130602360760562331009008640000.            (A64)

Here the norm is on the fixed original coefficient space C^240 with its counting pairing. Every row sum and every maximizing original face index is stored in `generated/native_response.json`. To justify the bound without a matrix-frame change, Hermiticity and 2|c_i c_j|<=|c_i|^2+|c_j|^2 give

    |sum_(i,j) conjugate(c_i) A_ij c_j|
       <=max_i sum_j |A_ij| * sum_i |c_i|^2.

Every original matrix cross term remains in this inequality.

For the complete tail matrix, A58--A59 give the absolute-row bound

    B_tail(xi)=[98/39+239*(49/34)]
                  * (280xi)^8/[1-(280xi)^2].                (A65)

The diagonal and off-diagonal constants have not been interchanged. At xi0=1/784, corresponding to the original g^2=14, exact rational calculation proves

    (227/1404)xi0^2+(3451329067/14074482240)xi0^4
    +(43015053233874982762407882061
      /130602360760562331009008640000)xi0^6+B_tail(xi0)
       <1/9.                                                (A66)

Every term is increasing on 0<=xi<=xi0. Returning to the complete physical response, for every a>0 and g^2>=14 in this original box,

    (2/9)I_240 < R(xi) < (4/9)I_240.                        (A67)

The inequalities mean positive definite differences in the displayed source-coordinate pairing. They do not replace the actual physical source-state Gram. That original Gram is

    G_pq=<r_p,r_q>,  r_p=(W_p-<W_p>_rho)psi.

The original source-to-state map is c -> r(c)=sum_p c_p r_p, with inverse on its image given by the unique original plaquette coefficient vector. Its injectivity also follows from A67 and R=kappa r* A^(-1)r. There is no replacement of G by I in this statement.

The actual centered logarithmic derivative primitive is

    Z(c)=sum_p c_p[partial_(x_p)v-<partial_(x_p)v>_rho],
    Atilde Z(c)=kappa sum_p c_p(W_p-<W_p>_rho).

Equations A2--A3 return its full energy pairing:

    (2kappa/9)||c||^2
       <q_Atilde(Z(c))<(4kappa/9)||c||^2.                    (A68)

This bound is in the actual interacting-vacuum energy, on the entire original plaquette source image. The coupling domain is g^2>=14 on L=2; no extension of this finite matrix bound to all volumes is asserted.

Its original state norm also has explicit bounds. The constant trial state has zero expectation for K+V_x. The original min-max inequality for its first physical excitation gives, throughout this real source range,

    gap(H_L)>=kappa(3-2Mxi)>=kappa*(117/49).                 (A69)

This follows from K on its nonconstant physical subspace being at least three, ||V_x||<=2Mxi, and the ground energy being at most zero before restoring the scalar. Combining A68 with A69 gives

    ||Z(c)||_rho^2 < (196/1053)||c||^2.                     (A70)

For the lower bound, the actual original source variance satisfies

    ||r(c)||^2
       =Var_rho(sum_p c_p W_p)
       <=4(sum_p|c_p|)^2<=4M||c||^2.

The original pairing is <sum c_p(W_p-<W_p>),Z(c)>_rho=c*R c. Cauchy--Schwarz, with all source coefficients retained, and A67 therefore give

    ||Z(c)||_rho^2 > (1/19440)||c||^2                       (A71)

for nonzero c. Together, in the original plaquette coordinate frame,

    (1/19440)I_240 < Z*Z < (196/1053)I_240,
    (2kappa/9)I_240 < Z*Atilde Z < (4kappa/9)I_240.          (A72)

The adjoints in these formulas use the original rho-Hilbert pairing. The same primitive, its source labels, its energy and its restored state metric thus have two-sided bounds. These are results about a specified finite original observation family inside the full physical Hamiltonian, not a new continuum mass or a removal of the orthogonal physical complement.

## A13. Quantitative support-transition primitives in the same physical space

Retain the original 240 face labels and the same real vacuum at L=2, a>0, g^2>=14. Define the actual coefficient maps into the centered rho-Hilbert space

    Bc=sum_p c_p(W_p-<W_p>_rho),
    Zc=kappa Atilde^(-1)Bc.

They are injective by A67, have their original adjoints, and satisfy Atilde Z=kappa B. For each subset F of the 240 original labels put V_F=Z(C^F) and U_F=B(C^F). Use the actual cochain window

    V_F --(Atilde/kappa)--> U_all --0--> 0.                  (A73)

For F contained in G, the transition is inclusion in degree zero and the identity on U_all. The original operator restriction proves its cochain square. Its first cohomology is U_all/U_F. The exact transported-kernel map and inverse are

    V_G/V_F -> ker(U_all/U_F -> U_all/U_G),
    [h] -> [(Atilde/kappa)h],
    [By] -> [Zy] for y supported in G.                      (A74)

Changing By by an element of U_F changes Zy by its exact image in V_F because B and Z are injective with Atilde Z=kappa B. These statements prove well-definedness, both inverse laws, and the full receiving kernel. Source labels are subsets of the original plaquettes and their join is their union. Applying the original Split Zero reconstruction retains every receiving zero at its support; the physical orthogonal complement is kept below.

Let J=G minus F, in the original face order. The primitive class with remaining coefficient y in C^J has all representatives Z_F z+Z_J y. Its actual energy is the full quadratic form

    kappa*(z,y)* R_GG (z,y),

including R_FJ and R_JF. Since R_FF>(2/9)I, direct differentiation in the original coefficients, or completing this exact quadratic form, gives the unique minimum

    z_min=-R_FF^(-1)R_FJ y,
    Q_(F,G)=kappa[R_JJ-R_JF R_FF^(-1)R_FJ].                 (A75)

Every inverse is on the indicated original nonempty block; for empty F the term involving F has its unique empty value. To bound the quotient, minimize the lower inequality A67 over z; it gives Q_(F,G)>(2kappa/9)I. For the upper bound use the actual lift z=0 in the same fibre and A67. Therefore, on every nonempty receiving kernel,

    (2kappa/9)I_J < Q_(F,G) < (4kappa/9)I_J.                (A76)

For J empty the space and quadratic form are the original zero space and its unique form. No nonzero direction is manufactured there.

The minimum primitive h_y=Z_F z_min+Z_J y also retains its original state norm. A71 and ||(z_min,y)||^2>=||y||^2 give its lower bound. A69 and the upper bound in A76 give its upper bound. Thus

    (1/19440)||y||^2 < ||h_y||_rho^2
                         < (196/1053)||y||^2               (A77)

for y nonzero. These statements control every subset support transition of this actual original observation family. Their energy and state pairings are distinct displayed forms, with the exact map and coefficients A75 connecting their common primitive; neither form is replaced by the other.

The rest of the physical Hilbert space remains explicit. Let G_Z=Z*Z with the bounds A72 and define

    P_Z=Z G_Z^(-1)Z*,  S_Z=G_Z^(-1)Z*.

Multiplication proves P_Z*=P_Z, P_Z^2=P_Z, S_Z Z=I, Z S_Z=P_Z and ker S_Z=im(Z)^perp. For a form-domain h perpendicular to im Z, the full original norm and energy of Zc+h are

    ||Zc+h||_rho^2=c*G_Z c+||h||_rho^2,
    q_Atilde(Zc+h)=kappa c*R c
          +2kappa Re< Bc,h>_rho+q_Atilde(h).                (A78)

The mixed term follows from Atilde Z=kappa B and has not been removed by the state-orthogonal decomposition. In particular the maps above do not presume that im Z is a reducing subspace. The complement and its displayed forcing are retained when this finite source family is used in further physical refinement. The continuum and growing-volume conclusions remain outside the domain of A67–A78.
