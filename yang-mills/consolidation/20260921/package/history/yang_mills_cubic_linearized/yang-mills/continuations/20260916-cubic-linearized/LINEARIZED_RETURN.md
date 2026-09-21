# The full linearized residual and its return to the original physical gap

16 September 2026. This is the second executed calculation, on exactly the original operators and source coordinates of `CUBIC_SOURCE.md`. It evaluates the full residual at xi v_1+xi^2 v_2, bounds the actual linearized inverse and every nonlinear correction, and returns the result to the complete physical form domain. The proof does not assume a spectral gap to construct this inverse.

## L1. Two sharper spin budgets for the evaluated second source

Retain C1–13, including all union labels. The first source has

    m(v_1)<=64/3,   t(v_1)<=16/3.                         (L1)

An anchor meets at most four plaquettes; each has coefficient norm 8/3, total spin two and anchor spin 1/2. This proves both numbers.

For the actual second source C11, its self contributions to m are at most six. On a pair, with the original x<=16, x+y<=64, its total-spin weighted norm is x/9+4y/117<=400/117. There are at most 42 anchored pairs. Thus

    m(v_2)<=6+42*(400/117)=5834/39.                       (L2)

For t(v_2), self terms contribute at most 3/2. At most six pairs share the anchor itself: their spin-zero term has anchor spin zero, and their spin-one contribution is at most 64/117 per pair. In the other at most 36 pairs, the anchor occurs once and its spin is 1/2, giving at most (1/2)(x/27+y/117)<=176/351. Hence

    t(v_2)<=3/2+6*(64/117)+36*(176/351)=137/6.            (L3)

All original boundary patterns inject into these bulk lists. C7 and C5 now prove

    ||B(v_1,h)||loc<=(64/3)||h||loc,
    ||B(v_2,h)||loc<=(1566/13)||h||loc,
    ||B(v_2,v_2)||loc<=799258/39.                        (L4)

For the middle coefficient, 3[m(v_2)/6+(2/3)t(v_2)]=1566/13. For the last, 6m(v_2)t(v_2)=799258/39. The two inputs have their actual separately evaluated budgets; neither is replaced by a generic unknown vector.

## L2. Evaluate the complete residual, including its quartic source

Set x=xi as the same original source parameter, and define

    q_2=xv_1+x^2v_2,
    R_2=xv_1+B(q_2,q_2)-q_2=x^3v_3+x^4b_22,
    b_22=B(v_2,v_2),
    J_2 h=2B(q_2,h),  L_2=I-J_2.                        (L5)

The source v_3 is the complete five-family table C14–20. Here is also a finite formula for every component of b_22, avoiding an unevaluated Casimir inverse. Let mu enumerate the original terms of C11, with functions F_mu and coefficients a_mu. Their Casimirs are respectively 8,9/2,13/2 and their a_mu are -1/72,1/27,-1/117. Each F_mu has definite original edge spins, including its zero shared edge in the P_0 channel. For every ordered (mu,nu), let J_e be all spins from |j_mu,e-j_nu,e| to j_mu,e+j_nu,e in unit steps. These are at most two. With the literal polynomial projectors C13,

    b_22=sum_(mu,nu) a_mu a_nu
          sum_(boldj with c(boldj)>0)
          [c_mu+c_nu-c(boldj)]/[2c(boldj)]
          P_boldj(F_mu F_nu).                           (L6)

Each input, edge-spin range, polynomial projector, coefficient and denominator is now specified in original coordinates. This is a finite full-coefficient formula at every finite L. For disjoint active supports c(boldj)=c_mu+c_nu and the corresponding source is exactly zero at its original union. Output constants are retained outside Q_H, as below. No truncation of the full Hamiltonian is performed.

For example, the self/self term at one original plaquette is

    b_22^(p,p)=chi_1(Omega_p)/10368-chi_2(Omega_p)/31104,
    int Gamma(v_2^(p),v_2^(p))=1/648.                   (L7)

This follows from chi_1^2=1+chi_1+chi_2, with Casimirs 0,8,24 and the original factor 1/72^2. The entire removed scalar for the original q_2 is

    C(q_2)=int Gamma(q_2,q_2)
          =M x^2/3+x^4(M/648+2J/1053).                  (L8)

The odd term is zero by the original center involution in C7. Thus the full residual of the approximate exponential has the exact operator identity on smooth original functions

    e^(-q_2) H e^(q_2)
      =kappa[K-2Gamma(q_2,.)]
       +kappa[2Mx-C(q_2)]I-kappa M_(K R_2).             (L9)

Here M_(K R_2) is multiplication by the displayed original polynomial. To verify L9, expand the original Laplacian on e^(q_2)f and use K R_2=xS+Q_H Gamma(q_2,q_2)-Kq_2. This retains both the scalar energy and every quartic residual term.

## L3. The full linearized inverse and nonlinear correction

For every source h, C23 and L4 give

    ||J_2 h||loc<=ell(x)||h||loc,
    ||R_2||loc<=delta(x),
    ell(x)=(128/3)x+(3132/13)x^2,
    delta(x)=(944984/351)x^3+(799258/39)x^4.             (L10)

No derivative term is omitted: L_2 is the Frechet derivative of v-xv_1-B(v,v) at q_2, because B is bilinear and symmetric. Put

    D(x)=(1-ell(x))^2-(8/3)delta(x)
        =[46457856x^4+183150656x^3+18324072x^2
          -1168128x+13689]/13689.                       (L11)

Let alpha be the unique root of D in (17/1000,171/10000). This is the first positive root. Indeed D(0)=1; D'' has positive coefficients on x>=0, and D'(171/10000)<0. Hence D'<0 on that whole interval. Exact rational endpoint signs give D(17/1000)>0>D(171/10000). In particular D>=0 on [0,alpha], and ell(x)<=ell(171/10000)<1 there.

The Neumann sum of the ACTUAL J_2 constructs

    L_2^(-1)=sum_(j>=0)J_2^j,
    ||L_2^(-1)||<=1/(1-ell(x)).                         (L12)

Its complete source coordinates are unchanged. For w=v-q_2 the full equation is

    L_2 w=R_2+B(w,w).

Define z=L_2^(-1)R_2 and C=L_2^(-1)B. Then

    ||z||loc<=z_*:=delta/(1-ell),
    ||C(f,h)||loc<=c_*||f||loc||h||loc,
    c_*=(2/3)/(1-ell).                                  (L13)

Construct w explicitly by the binary-tree recurrence w_1=z, w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i)). Its terms have bounds

    ||w_n||loc<=Catalan_(n-1) c_*^(n-1) z_*^n.

The discriminant L11 gives theta_*=4c_*z_*<=1. The series converges absolutely on the ENTIRE closed interval, and its sum satisfies the full equation. Its bound is

    w_*(x)=(3/4)[1-ell(x)-sqrt(D(x))],
    ||v-q_2||loc<=w_*(x).                               (L14)

At theta_*=1 the endpoint is obtained from the actual convergent Catalan series, not from a strict nonlinear contraction. Its omitted-tree tail after N>=1 is at most

    [3(1-ell)/4] theta_*^(N+1) binom(2N,N)/4^N
     <=[3(1-ell)/4] theta_*^(N+1)/sqrt(N+1).              (L15)

To prove it, use Catalan_n/4^n=2(b_n-b_(n+1)), b_n=binom(2n,n)/4^n, and telescope. The original linear-source truncation has the independent exact identity and bound

    L_2^(-1)R_2-sum_(j=0)^N J_2^jR_2
        =J_2^(N+1)L_2^(-1)R_2,
    norm <=ell^(N+1)delta/(1-ell).                       (L16)

Thus both infinite operations have explicit residuals. Every application of J_2 adds at most two original plaquettes to its union label, and the initial R_2 has at most four. The finite linear sum in L16 is supported in actual unions of at most 4+2N plaquettes. The tree recurrence retains all further unions and all original coefficient multiplicities.

At each finite L the labelled c-weighted source is complete. Its global c-weighted sum is bounded by |E_L| times the local norm. The original spin-generator estimates bound all first and second link derivatives by that sum. Therefore the series gives a C^2 function v on the compact original product and permits the full source equation to be summed. With C3, direct differentiation gives H psi=E_0 psi. Elliptic regularity makes psi smooth. For every smooth h,

    q_(H-E_0)(psi h)=kappa int psi^2 sum_i |X_i h|^2.

Multiplication and division by the positive smooth psi preserve H^1 at this finite L. This proves E_0 is the actual lowest energy and identifies psi with the original positive unit vacuum; a second ground state divided by psi has zero derivative and is constant. Gauge invariance follows from the invariant source. This identification does not presume a gap.

The convergent construction is analytic for complex |x|<alpha by the same absolute coefficient majorants. At every original power x^n its unique formal coefficient is C2, so the new construction and the earlier source constructions agree coefficient by coefficient on their common domains. Their coefficient identity maps have literal inverse identities. No new source metric or different physical vacuum is selected.

## L4. Numerical endpoint and fully retained benchmark

Exact bisection and integer-square comparisons give

    0.0170787544707772675 < alpha < 0.0170787544707772677,
    3.825973052393385 < 1/(2sqrt(alpha))
                         <3.825973052393386.             (L17)

This is the new sufficient coupling threshold g^2. The cubic coefficient alone, with the old generic recurrence for higher orders, gives the intermediate discriminant

    D_3(x)=1-(256/3)x+(10720/9)x^2+(20714816/1053)x^3

and first root approximately 0.0166569913896066, or g^2 approximately 3.8741080015. The full linearized calculation L10–17 gives the additional improvement. Its source-specific m and t budgets are part of that gain.

At the exact original coupling g^2=4, x=1/64, a>0 and kappa=8/a,

    ell=28973/39936,
    ||L_2^(-1)||<=39936/10963,
    ||z||loc<=33836149/808280064,
    D=10028381/224280576,
    theta_*=439869937/1081686321,
    ||w||loc<=0.047293824576905,
    ||w-z||loc<0.005432.                                 (L18)

The displayed decimal bounds are outward rational bounds checked against L13–14. They bound the ACTUAL linear response and its complete further nonlinear correction. No value of an uncomputed vacuum integral is assigned. The total source satisfies

    ||v||loc<=32x+236x^2+w_*
       =(3/4)(1-sqrt D)+(719/13)x^2.                    (L19)

## L5. Return to the entire physical spectrum, using the evaluated spin budget

Use the actual ground-state transform A=psi^(-1)(H-E_0)psi=kappa(K-D_v), where D_v=2Gamma(v,.). Its physical pairing is int rho conjugate(f)h dU, rho=psi^2. C5, L1 and L3 give the sharper point-spin budget

    t(v)<=(16/3)x+(137/6)x^2+w_*/6.

For an original zero-Haar-mean coefficient family h, C6 and sum_e j_e<=2c(j)/3 yield

    ||D_v h||_X<=4t(v)||Kh||_X<=chi(x)||Kh||_X,
    chi(x)=1/2(1-sqrt D(x))-(1136/39)x^2.                (L20)

Here X is the full sum of original trace coefficient norms after assembly. The scalar output is also bounded by the same complete product estimate. To check L20 without its displayed cancellation, chi is exactly
4[(16/3)x+(137/6)x^2+w_*/6], a positive-coefficient majorant. This form proves its monotonicity. Its closed-endpoint value is strictly less than 1/2.

For an actual physical eigenfunction A f=lambda f with lambda>0, let h=Q_Hf. The source and physical-centered maps are

    f -> Q_Hf,
    h -> h-<h>_rho,
    <f>_rho=0, int_H h=0.                               (L21)

Both compositions are identities, and h is nonzero. The original eigen-equation gives

    (K-lambda/kappa)h=Q_H D_vh.

Every finite-regulator eigenfunction is smooth. Its original Fourier coefficients have summable c(j)||A_j||_1: Peter–Weyl Plancherel followed by Cauchy–Schwarz with sufficiently many Casimir powers gives this, since sum_j dim(j)^2(1+c(j))^(-N)<infinity for large N on the finite product. No volume-uniform smoothness constant is used. For 0<lambda/kappa<3, every actual nonconstant physical block has c(j)>=3, and therefore

    ||(K-lambda/kappa)h||_X
        >=[1-lambda/(3kappa)]||Kh||_X.

Combining with L20 proves lambda>=3kappa(1-chi). For lambda>=3kappa that inequality is automatic. The full compact spectral resolution gives, on the ENTIRE centered physical form domain,

    Delta_L>=kappa d(x),
    d(x)=(3/2)(1+sqrt D(x))+(1136/13)x^2,
    0<x<=alpha, L>=2, a>0.                              (L22)

Equivalently, x=1/(4g^4), kappa=2g^2/a and g^2>=1/(2sqrt(alpha)). The scalar-space version has the original free constant 3/4 and gives one quarter of L22. No excitation is declared physical merely from an unprojected color vector.

Because chi has positive power coefficients and increases on the interval, d decreases to d(alpha). The exact endpoint satisfies

    d(alpha)=3/2+(1136/13)alpha^2
             >61/40=1.525.                              (L23)

At the rational interior point and throughout its lower-x interval,

    g^2>=4 => Delta_L>1.8385 kappa,
    d(1/64)= (3/2)(1+sqrt(10028381/224280576))+71/3328
             =1.8385178195961905... .                    (L24)

Every a and exterior L factor remains in kappa. This is a lower bound for the full original physical spectrum, obtained from a convergent complete source rather than a finite-dimensional trial-space lower estimate.

## L6. The retained source complexes and their exact physical defect

At fixed x in the closed domain, define V_N=span{R_2,J_2R_2,...,J_2^N R_2} in the original labelled coefficient space V. At support N use the actual complex

    V_N --L_2--> V --0-->0,
    H^1_N=V/L_2 V_N.

The source inclusions and target identities commute. Since L_2 is invertible, the exact transported-kernel isomorphism is

    V_(N+1)/V_N -> ker(H^1_N -> H^1_(N+1)),
    [h] -> [L_2 h],
    inverse [L_2 h] -> [h].                             (L25)

Changing representatives by L_2V_N changes h by exactly V_N; this proves both inverse identities. The actual source R_2 has representative J_2^(N+1)R_2 after the primitive sum in L16 is subtracted. The same original support label survives on a zero receiving coefficient. These are the support-indexed quotient maps used by Split Zero; the formula retains the full primitive, not only its support flag.

The linearized source maps to the auxiliary differential operator by the exact square

    K L_2 h=Q_H[K-2Gamma(q_2,.)]h.                       (L26)

Its relation to the actual physical operator is the complete defect

    Q_H A h-kappa K L_2h=-2kappa Q_H Gamma(w,h).          (L27)

The bound from C5–7 is at most (2kappa/3)w_*||Kh||_X on the right. Equation L9 separately retains the multiplication residual and scalar of the approximate exponential. Thus the approximate section and actual physical dynamics are connected by specified maps and controlled, unremoved terms.

On the original centered physical form domain put d_Xf=(X_if)_i with norm squared kappa int rho sum_i |X_if|^2. Its inverse on its actual range is p_X(d_Xf)=f. The ground-state map U:f->psi f is unitary with inverse u->u/psi. The variational definition of the first excitation therefore gives exactly

    ||p_X||^2=1/Delta_L<=1/[kappa d(x)].                 (L28)

For an original physical conditional-expectation kernel, its closed restricted form has D_phys>=kappa d(x). All zero-shift primitive and response errors on that kernel consequently have the same inverse bound. The inclusion into the full scalar kernel intertwines the operators and resolvents when the original conditional expectation commutes with gauge averaging; that commuting property follows by changing variables in its actual vacuum conditional integral. No forcing or state Gram is altered by this return.

## L7. Explicit complete higher-order remainder for the energy coefficient

On the complex circle |x|=1/60, L19 is less than 7/10, verified by rational square bounds on D(1/60)=5458199/462003750. For each original link and each of its three generators, |X_e,alpha v|<=||v||loc/6. Hence

    |C_L(x)|<=|E_L| ||v||loc^2/12<49|E_L|/1200

on that circle. Analyticity inside alpha and the exact evenness from C7 give the Cauchy coefficient estimate and its full geometric tail:

    |E_0-2kappa Mx+kappa Mx^2/3
           -kappa(5M/216-2J/1053)x^4|
      <=(49kappa |E_L|/1200)
             (60|x|)^6/[1-(60|x|)^2],
    0<|x|<1/60.                                        (L29)

The scalar term 2kappa Mx and every extensive factor remain. This bounds all omitted orders, rather than assigning a numerical fourth-order polynomial as the exact energy. The complete finite-box coefficients M,J and the independent coefficient calculation are C24–25.

## L8. Literature crosscheck with the actual parameter maps

The exponential vacuum equation and connected loop expansions have established Hamiltonian lattice-gauge antecedents. The following comparisons are to inspected primary bodies, with their scope retained.

D. Schuette, Zheng Weihong and C.J. Hamer, *The Coupled Cluster Method in Hamiltonian Lattice Field Theory*, Phys. Rev. D55 (1997) 2974–2986, arXiv:hep-lat/9603026v1, equations (17), (21)–(26), (30) and (38), formulate the exponential vacuum and its linear excitation equation using original gauge-invariant loop/representation coefficients. Their dimensionless coefficient is x_C=2/g_C^4 and physical operator g_C^2[K-x_C S]/(2a). At fixed a, g_C=2^(3/4)g gives x_C=xi and

    H_original(a,g)=sqrt(2) H_C(a,2^(3/4)g)
                         +2kappa xi M I.                (L30)

Substituting both coefficients proves the complete identity, including the additive energy. With their Hermitian generator lambda_alpha=sigma_alpha/2, their multiplication commutator derivative is i X_alpha. Hence S_(mu mu)=K v and S_mu S_mu=-Gamma(v,v). Their equation (23) becomes exactly the original scalar equation C2–3 under S=v+c_L. No sign is inferred from an unnamed convention.

B. Dahmen, *Strong coupling expansion for scattering phases in Hamiltonian lattice field theories—II. SU(2) gauge theory in (2+1) dimensions*, arXiv:hep-lat/9412080, equations (1.7), (1.24), gives the original planar coefficient H_D'=(g_D^2/2)[K-h_D S], h_D=2/g_D^4, and the ground coefficient -M h_D^2/3. The exact return is g_D=2^(3/4)g and

    H_plane(a,g)=(sqrt(2)/a) H_D'+2kappa xi M I.          (L31)

This reproduces the -kappa M xi^2/3 term and the actual local Casimir denominators. The inspected second-order calculation does not independently certify our cubic norm or the quartic majorant.

P. Hui, X.-Y. Fang and T.-Y. Shi, *Approximated seventh order calculation of vacuum wave function of 2+1 dimensional SU(2) lattice gauge theory*, arXiv:hep-lat/0408035v1, equations (3), (4), (6), use g_H^2[K-(4/g_H^4)S]/(2a). The map g_H=2g gives

    H_plane(a,g)=H_H(a,2g)+2kappa xi M I.                 (L32)

Their section 2 explicitly defines subsequent finite-order/random-phase replacements. This contribution retains the exact product and every residual term in L5–16 instead. The earlier method and the existence of higher-order loop calculations are attributed; no claim that the general cubic expansion or exponential ansatz is new is made.

For the original planar edge subset inside the spatial cube let J_pi be cylinder pullback, with inverse on its image the original unused-link Haar integral. Fubini proves J_pi^*J_pi=I, and original differentiation gives K_3 J_pi=J_pi K_2. The full operator difference is exactly

    H_3 J_pi-J_pi H_2
      =kappa xi [2(M_3-M_2)-sum_(p outside plane)W_p]J_pi. (L33)

Thus local planar channels are compared by their actual inclusion, and all perpendicular and exterior plaquettes remain in L33. The common-edge and cube-corner contributions in C18–20 are calculated in the spatial graph rather than silently assigned a planar identity.

Primary URLs: https://arxiv.org/html/hep-lat/9603026v1 ; https://arxiv.org/pdf/hep-lat/9412080 ; https://arxiv.org/html/hep-lat/0408035v1 . Their cited formulae were read. The literature check establishes these parameter/equation correspondences; it does not establish a global novelty or best-known coupling-range claim.

## L9. Continuum path, completed scope, and the next actual quantity

The running test path remains a_n=a_0 2^(-n), g_n^2=1/c_n, c_n=g_0^(-2)+beta n log 2. Its exact inclusion in the new domain is

    c_n<=2sqrt(alpha).

For beta>0 it eventually leaves the proved strong-coupling domain. A nontrivial four-dimensional continuum field and a finite positive continuum mass have not been constructed by L22. The original units and this parameter boundary are explicitly retained.

The two requested calculations are complete: the actual cubic source C14–23, and the complete linearized residual/inverse L5–16 with physical return L20–28. The fourth energy coefficient and its all-order remainder are additional consequences. This is written analysis supported by finite exact regressions, not an independent external review or Lean certificate.

A directly specified next computation is the full source v_4=2B(v_1,v_3)+b_22 on its original connected four-face supports, together with a signed, channel-resolved estimate of J_2 on those same supports. The b_22 formula L6 and the cubic table are now evaluated inputs; there is no reason to repeat their generic norm bounds as new work. Any different continuation must retain its exact link to the physical primitive norm L28 and the running parameter boundary above.
