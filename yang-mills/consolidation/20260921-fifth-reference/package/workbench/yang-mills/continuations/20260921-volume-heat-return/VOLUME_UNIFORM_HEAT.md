# Original Yang–Mills heat: a box-independent analytic radius and row-sum remainder

21 September 2026. This continuation addresses the two quantities left by the heat edition: its radius 1/M and the coupling of its observed states to the full physical complement. All operator coefficients, Haar masses, original link and plaquette coordinates, and state and energy pairings are retained. This note proves the local-source-to-heat argument used here in full. It does not certify every earlier stronger-coupling assertion. Its coefficient tables are the inherited, separately replayed heat tables; new constant and matrix calculations have their own records. No continuum mass-gap conclusion, historical-priority determination, or external analytical review is asserted.

## U1. Original operator, physical time, and coefficient maps

For each L>=2 take vertices {-L,...,L}^3, all contained positive nearest-neighbor links e=(n,i), and all elementary faces p=(n;i,j), i<j. Retain

    Wp=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)),
    T_a=-i sigma_a/2,  X_e,a f=d/dt f(...,exp(t T_a)U_e,...)|0,
    K=-sum_(e,a) X_e,a^2,
    H(x)=kappa K+kappa sum_p x_p(2-Wp),
    kappa=2g^2/a,   x_p=xi=1/(4g^4),   a,g>0.                 (U1)

The physical Hilbert space is the invariant subspace of original product Haar probability L2(dU), with every vertex including boundary vertices averaged. H has physical H2 domain and H1 form domain, since the original potential is smooth bounded on this finite compact group. Its smooth positive unit ground vector psi and simple bottom energy E0 follow from the modulus form inequality, elliptic regularity, the maximum principle, and the identity

    q_(H-E0)(psi f)=kappa int psi^2 sum_i |X_i f|^2.         (U2)

The multiplication map f -> psi f and inverse division by psi are unitary between L2(rho dU) and original L2(dU), rho=psi^2. The time coordinates are tau=kappa t and t=tau/kappa. No field variable is rescaled.

For a product-spin label j=(j_e), define pi_j(U)=tensor_e pi_(j_e)(U_e), d_j=product_e(2j_e+1), c_j=sum_e j_e(j_e+1), and the actual coefficient

    A_j=d_j int f(U) pi_j(U)^* dU,
    f(U)=sum_j Tr(A_j pi_j(U)).                             (U3)

This Fourier map and its inverse follow from the original Haar matrix-coefficient orthogonality. The trace-coefficient norm is ||f||_X=sum_j ||A_j||_1. Let X0 be its zero-Haar physical part, and Y0 its dense domain sum_(j!=0)c_j||A_j||_1<infinity. The actual K maps Y0 bijectively onto X0 by multiplying each coefficient by c_j; its inverse divides it by that same c_j. These are auxiliary convergence estimates on the original coefficients, not replacements for (U2).

The compact-group Fourier algebra and its product norm are classical (Eymard, 1964). Here their required inequalities are proved directly. In a product of two coefficient functions, decompose pi_j tensor pi_k into its full irreducible and multiplicity spaces by a unitary intertwiner. Pinching to all its diagonal representation blocks and tracing each multiplicity space returns the exact output coefficients. Pinching is an average of unitary conjugations. For a partial trace, trace-norm duality gives |Tr[(Z tensor I)C]|<=||C||_1 when ||Z||<=1. Hence

    ||fh||_X<=||f||_X||h||_X,
    ||A(X_e,a f_j)||_1<=j_e||A_j||_1.                      (U4)

Every representation dimension and every multiplicity is included in this argument.

## U2. The graph bound that enters the source estimate

A nonzero gauge-invariant coefficient has an invariant tensor on the original incident indices at every vertex. Grouping the factors gives an intertwiner from the dual spin-j_e factor into the tensor product of the others. The maximum target weight is their summed spin, so

    j_e<=sum_(f incident v, f!=e) j_f.                      (U5)

Fix e={u,v}, and let E1 be the other edges at its endpoints. Because the graph is simple and triangle-free, their outer endpoints are distinct. Put J1=sum_(f in E1)j_f. The two endpoint inequalities give J1>=2j_e. Sum the outer-endpoint inequalities: every edge outside E1 and {e} is counted at most twice, so J1<=2J2, where J2 counts these outer edges once. Therefore sum_f j_f>=j_e+J1+J2>=4j_e. The original half-integer spectrum obeys j(j+1)>=(3/2)j, and consequently

    c_j>=6j_e on every physical block;
    sum_e j_e<=(2/3)c_j on every product block.             (U6)

In particular c_j>=3 on each nonconstant physical block. The fundamental elementary plaquette has c_j=3. This argument includes active bridges and boundary vertices; no cycle decomposition of every active edge is presumed.

## U3. Local labelled source and its exact assembly kernel

For every nonempty finite edge label S retain a zero-Haar physical coefficient family A_(S,j), with supp(j) contained in S; the label may exceed the active support. Put

    ||v||loc=sup_e sum_(S containing e,j!=0)c_j||A_(S,j)||_1. (U7)

On a finite graph this is a complete space, and its total c-weighted coefficient sum is at most |E_L| ||v||loc. Assembly sends A_(S,j) to sum_(S containing supp(j)) A_(S,j). Its kernel is exactly the family equations that all those sums vanish. For each S strictly containing supp(j), the relation with coefficient A at (S,j) and -A at (supp(j),j) has zero assembly. The actual coefficients at all enlarged S give a unique decomposition of every assembly-kernel element into these relations. Its inverse reads those same enlarged-label coefficients. This supplies the support-preserving quotient map and both inverse laws.

Define, retaining the original union label,

    B(v,h)_S=K^(-1) Q_H sum_(S1 union S2=S) Gamma(v_S1,h_S2),
    Gamma(f,h)=sum_(e,a)(X_e,a f)(X_e,a h),  Q_H=I-P_H.     (U8)

Each Haar scalar removed by Q_H is recorded separately. For an anchor in S1, (U4) and (U6) bound the output before K inversion by

    3 sum_(S1 containing anchor,j) ||A_(S1,j)||_1
        sum_e j_e sum_(S2 containing e,k) k_e||B_(S2,k)||_1
      <=(1/3)||v||loc||h||loc.

The anchor-in-S2 contribution gives the other 1/3. The original output Casimir cancels precisely against its nonzero inverse Casimir in (U8). Thus

    ||B(v,h)||loc<=(2/3)||v||loc||h||loc.                   (U9)

## U4. Exact elementary coefficient and convergent complex source

For the original four-link word, the coefficient matrix on (C2)^tensor4 has entries

    A_(i1,i2,1-i2,1-i3 ; i0,i1,1-i3,1-i0) += (-1)^(i0+i2),
    i0,i1,i2,i3 in {0,1}.                                  (U10)

The identity (U^(-1))_(r,c)=(-1)^(r+c) U_(1-c,1-r) proves its trace formula. Its four nonzero 2-by-2 blocks, up to row/column order, are [[1,-1],[-1,1]]. Direct multiplication gives (A* A)^2=4A* A and Tr(A* A)=16. Thus |A|=A* A/2 and ||Wp||_X=8. At most four original plaquettes meet an edge.

Allow independent complex x_p with max_p|x_p|<=r. The source equation is

    v=(1/3)sum_p x_p Wp+B(v,v).                            (U11)

Its homogeneous order-n coefficient obeys the original binary recurrence, giving

    a_n(r)=Cat_(n-1)(2/3)^(n-1)(32r)^n,
    sum_(n>=1) a_n(r)=r_v(r)=(3/4)(1-sqrt(1-256r/3)).       (U12)

The radius used throughout the new bound is exactly

    R0=3/256.                                              (U13)

For r<R0 the series is norm-analytic. It converges absolutely also at r=R0, where its tail is (3/4)binom(2N,N)/4^N<=3/(4sqrt(N+1)). The finite coefficient proof is Cat_N/4^N=2(b_N-b_(N+1)), b_N=binom(2N,N)/4^N. No strict contraction at the boundary is used.

Each order-n label is an edge-connected union of at most n plaquettes. The coefficients agree literally in every original box containing that union. This follows inductively from (U8): derivatives require a shared original edge, and K inversion acts on the same coefficients.

On a finite graph the norm convergence controls every first and second coordinate derivative, since j_e j_f<=c_j. Thus the actual assembled function solves

    Kv=sum_p x_pWp+Gamma(v,v)-C(x),
    C(x)=P_H Gamma(v,v).                                   (U14)

For real x, psi=exp(v)/sqrt(int exp(2v)) is positive and solves the original eigen-equation with

    E0=kappa[2sum_p x_p-C(x)].                              (U15)

Equation (U2) then proves it is the actual ground vector and fixes every scalar. Elliptic bootstrapping makes it smooth. For complex x the nonzero function exp(v) is still a smooth solution of that eigen-equation. Its squared integral is addressed below, rather than presumed nonzero.

## U5. The full drift, including its scalar row

Set D_v f=2 Gamma(v,f). Equations (U4),(U6) give, on the original coefficient spaces,

    ||D_v h||_X<=chi(r)||Kh||_X,
    chi(r)=(2/3)r_v(r)=(1-sqrt(1-256r/3))/2<=1/2.           (U16)

Both the constant and nonconstant outputs are included. Indeed the sum over generators is at most 6 sum_j ||A_j(h)||_1 sum_e j_e [r_v/6], and sum_ej_e<=(2/3)c_j. Define

    T=Q_H D_v K^(-1):X0->X0,
    p=P_H D_v K^(-1):X0->C,
    S=(I-T)^(-1)=sum_(n>=0)T^n.                            (U17)

The stacked bound is |py|+||Ty||_X<=chi||y||_X; in particular ||S||<=1/(1-chi). Define the actual mean functional by

    mu_x(F)=P_HF+p S Q_HF.                                 (U18)

For chi<=1/2, |mu_x(F)|<=||F||_X and |mu_x(Q_HF)|<=chi||Q_HF||_X/(1-chi). The associated source inverse is h=K^(-1)S Q_HF in Y0, with

    (K-D_v)h=F-mu_x(F).                                    (U19)

All maps are analytic for r<R0.

Here (U18) equals the actual complex density functional as well. Put Z_x=int exp(2v). Integration by parts gives int exp(2v)(K-D_v)h=0 for h in Y0, since its first and second derivatives converge. Equation (U19) therefore gives

    int exp(2v)F=mu_x(F) Z_x.                               (U20)

If Z_x vanished, the left side would vanish for every physical Fourier polynomial. Their uniform closure contains the conjugate of the nonzero smooth gauge-invariant exp(2v). Its squared modulus would then have zero integral, a contradiction. Hence Z_x is nonzero, and mu_x(F)=int exp(2v)F/Z_x. For real x it is precisely expectation in rho. The exact bilinear integration identity is

    mu_x((K-D_v)h . G)=mu_x(Gamma(h,G)).                    (U21)

Complex x uses the bilinear analytic continuation; the physical real-coupling Hilbert pairing retains conjugation in its first entry.

## U6. Closed generator and heat flow in the same coefficients

Let L_x=K-Q_H D_v on X0, Dom(L_x)=Y0. The graph norms of K and L_x are equivalent because ||Q_H D_vh||<=chi||Kh||, chi<1. Thus L_x is closed and densely defined. For h>0,

    I+hL_x=[I-hQ_H D_v(I+hK)^(-1)](I+hK),                 (U22)

and the square bracket is invertible by a Neumann series of norm ratio at most chi. The original sum of trace norms also gives

    ||(I+hL_x)f||_X
      >=||f||_X+h(1-chi)||Kf||_X
      >=[1+3h(1-chi)]||f||_X.                              (U23)

All powers of the actual resolvent obey the corresponding product bound. The Hille–Yosida/Lumer–Phillips generation theorem applies to this explicitly closed dense domain and the proved surjectivity (U22). It gives

    E_x(tau)=exp(-tau L_x),
    ||E_x(tau)||<=exp[-d(r)tau],  d(r)=3(1-chi(r))>=3/2.    (U24)

For completeness, the shifted operator L_x-d(r) is dissipative with the negative-generator convention: the directional norm derivative of -Kf is -||Kf||, and its perturbation is at most chi||Kf||. Its sufficiently large positive resolvent is obtained by (U22) and the resolvent identity. This proves the decay constant, rather than using a norm for one inverse as a substitute for a semigroup estimate. Lumer–Phillips (1961), Theorem3.1, pp686–687, is the primary generation reference.

Each resolvent in (U22) is analytic in x. Its exponential Euler powers are uniformly bounded on compact complex source polydisks and converge strongly to (U24). Here the latter assertion has a direct integral proof: (I+hL)^(-1)f=int_0^infinity exp(-u)E_x(hu)f du, by integration on the original generator domain and density. The m-fold product at h=tau/m is the average of E_x(tau Y_m/m)f, where Y_m has the convolution density exp(-u)u^(m-1)/(m-1)!, mean m and variance m. The nonnegative scalar density has mass one. Chebyshev's inequality outside a fixed neighborhood of tau, strong continuity inside it, and the contraction bound give the stated strong convergence. No spectral diagonalization of the perturbed coefficient generator is presumed. Applying scalar Vitali convergence to every bounded functional and then the locally bounded weak-to-strong holomorphy principle proves analytic dependence of E_x(tau). Equivalently the sectorial resolvent obtained from (U16) gives the same contour construction. This concerns source analyticity, not a holomorphic continuation of physical time across arbitrary rays.

For real x the full physical heat return is

    T_x(tau)F=E_x(tau)Q_HF+mu_x(F)-mu_x(E_x(tau)Q_HF).      (U25)

On the dense smooth domain it solves the actual equation with generator K-D_v, preserves its original mean, and agrees with the physical Hilbert semigroup by uniqueness. Its positive physical time is tau/kappa. The same formula defines the analytic continuation for complex x. In particular

    ||T_x(tau)F-mu_x(F)||_X
      <=exp[-d(r)tau]||Q_HF||_X/(1-chi).                   (U26)

Every physical eigenfunction in a finite box is smooth and belongs to Y0 after subtracting its Haar constant. This last membership follows from Plancherel and Cauchy–Schwarz with a sufficiently high original Casimir power: sum_j d_j^2(1+c_j)^(-s)<infinity for s>3|E_L|/2. Thus (U24) applied to the exact eigen-equation proves A=H-E0>=kappa d(r) on the complete centered physical Hilbert space. Compact spectral resolution gives the full form-domain statement. This is a rederivation of the elementary strong-coupling lower bound on this explicit domain, not of every stronger historical source estimate.

## U7. The row-sum estimate that removes the volume factor

For fixed original p put q_tau=E_x(tau)Wp and h_tau=K^(-1)S q_tau. The exact mean equation gives

    (K-D_v)h_tau=T_x(tau)Wp-mu_x(Wp).                      (U27)

For arbitrary complex coefficients z_q with max_q|z_q|<=1, set G_z=sum_q z_qWq. The original edge incidences and trace coefficient 8 give

    sup_e sum_(q containing e) (1/2)||z_q Wq||_X<=16.

Consequently, with every generator retained,

    ||Gamma(h,G_z)||_X
      <=3*16 sum_j sum_e j_e||A_j(h)||_1
      <=32||Kh||_X.                                       (U28)

Use (U21), ||mu_x||<=1, ||S||<=1/(1-chi), and ||Wp||_X=8. The connected analytic heat matrix satisfies

    Chat_pq(tau;x)=mu_x[(T_x(tau)Wp-mu_xWp)Wq],
    sum_q |Chat_pq(tau;x)|
      <=[256/(1-chi(r))] exp[-d(r)tau]
      <=512 exp(-3tau/2).                                  (U29)

The sum equality to a supremum over phases z_q is exact in every original finite face set. At real x this is precisely <r_p,exp(-tau A/kappa)r_q>. Its transpose symmetry extends to complex x by analyticity from the real multivariate polydisk. Thus the same bound holds for columns and for the coefficient-space operator norm. No M is introduced.


There is a useful sharper bound that uses the original Haar projection before estimating the returned mean. The physical Fourier block with spin one-half on the four edges of a specified elementary plaquette and zero on all other edges is one-dimensional: at each two-edge vertex the invariant contraction is unique, and following the original indices gives Wp. Consequently, for physical h in Y0,

    |P_H Gamma(h,G_z)| <= (1/8)||Kh||_X.

Indeed the contributing block is a_p Wp, has norm8|a_p| and Casimir3, and its Haar pairing with Wp is a_p. All other product-spin labels integrate to zero. On the nonconstant output, (U18) gives |(mu-P_H)QF|<=chi||QF||_X/(1-chi). Retaining both terms in this mean decomposition and using (U28) yields the additional full-row bound

    ||Chat(tau;x)||row
       <=[(1+255chi)/(1-chi)^2] exp[-3(1-chi)tau].        (U29a)

The original bound(U29) remains available. Take the exact original source radius and its derived constants

    R1=45/4096,  chi(R1)=3/8,
    C1=6184/25,  d1=15/8.

Then (U29a) supplies

    ||Chat-C0-xi^2 C2-xi^4 C4||row
      <=(6184/25) exp(-15tau/8)
             (|xi|/R1)^6/[1-(|xi|/R1)^2], |xi|<R1.        (U29b)

This second circle has its stated smaller radius and sharper prefactor and decay. A scalar minimum of the two error bounds is permitted; no minimum of noncommuting matrices is introduced. For the kth inverse moment its prefactor is (6184/25)(8/15)^k. These are used in the strengthened numerical return M10.

## U8. Uniform analytic remainder and all inverse-energy moments

Now restrict x_p=zeta homogeneously. The original central link map U_(n,i) -> (-1)^(sum_(j<i)n_j)U_(n,i) preserves Haar, K and every gauge constraint and sends all Wp to -Wp. Both marked traces change sign, so Chat(tau;zeta) is even. Let theta=|xi|/R0. Cauchy's formula using (U29), first at radius r<R0 and then letting r increase to R0, proves in maximum absolute row-sum norm

    ||Chat(tau;xi)-C0(tau)-xi^2 C2(tau)-xi^4 C4(tau)||row
       <=512 exp(-3tau/2) theta^6/(1-theta^2),
       |xi|<R0, tau>=0.                                    (U30)

The original coefficients C0,C2,C4 are exactly the inherited full heat tables: uniqueness of the local analytic eigen/heat equation at x=0 gives the identical recurrence and ground-pole subtraction. Their source and original time coordinates are unchanged.

For the original centered columns R and A=H-E0 put

    G0=R*R,  Gk=kappa^k R*A^(-k)R (k>=1),
    Phi=kappa A^(-1)R,  Phi*Phi=G2,  Phi*A Phi=kappa G1.

The physical spectral theorem and (U30) justify all integrals, including their complete tails:

    Gk=int_0^infinity tau^(k-1) Chat(tau)d tau/(k-1)!,
    ||Gk-sum_(j=0)^2 xi^(2j) Gk_(2j)||row
       <=512(2/3)^k theta^6/(1-theta^2), k>=1.              (U31)

For G0, (U30) at tau=0 supplies the same formula with k=0. A pole a/(z+c)^n contributes a(k+n-2)!/[(k-1)!(n-1)!c^(k+n-1)]. These maps use the original kappa in both the heat-time integral and every inverse energy.

## U9. Spatial tails and the actual volume limit

The preceding estimates also specify their spatial return. Set all couplings outside a given finite list to zero. The scalar Hilbert tensor factors on disjoint active link components factorize, as do the positive vacuum and semigroup. Their restrictions to the original invariant observables agree with that scalar calculation. A connected marked correlation therefore has zero multivariate coefficient unless its original marks and source faces lie in one edge-connected component. In particular, if the original face-adjacency distance is d(p,q), a degree-n coefficient connecting distinct marks needs n>=d(p,q)-1. Both marks retain their original links.

At degree n, the same coefficient depends only on the n-neighborhood of the union of marked links, where two links are adjacent when they share an original plaquette. This follows either from the tensor factorization or directly from (U8),(U17),(U25): every source insertion attaches its original connected plaquette union through a differentiated edge, K and its resolvent preserve link support, and all orders add to n. The constant and disconnected products are retained until the connected subtraction.

For two boxes containing the N-neighborhood of the same marks, every homogeneous coefficient through N is identical. Equation(U30)'s coefficient bound gives

    |Chat_L-Chat_L'|
       <=1024 exp(-3tau/2) theta^(2(floor(N/2)+1))/(1-theta^2). (U32)

The identical reasoning gives a row tail outside face-distance D by omitting every coefficient with n<D-1; n is even. These are explicit spatial bounds, with the physical link length a unaltered.

For clarity the limiting state and dynamics are also constructed. The coefficient mean (U18) is analytic and bounded by ||F||X, and its Taylor coefficients depend on finite original neighborhoods. Cauchy tails prove full-sequence convergence mu_L(F)->mu(F) for every cylinder Fourier polynomial on |xi|<R0. Real-coupling positivity and mass one pass from the original vacua. For an arbitrary cylinder function use the actual finite vertex Haar average P_G on its incident vertices; the equality mu_L(F)=mu_L(P_G F) extends the limiting physical functional consistently to all cylinder functions. Uniform cylinder approximation then gives its gauge-invariant probability lift on the product of original link groups. Both positivity and this gauge extension are the original finite-volume ones.

Equation(U25) has norm at most3||F||X and localized Taylor coefficients. Hence T_L(tau)F converges uniformly, first on cylinder Fourier polynomials and then on their continuous uniform completion by the real Markov contraction. The resulting T is positive, unital, strongly continuous, and preserves mu. Its semigroup and symmetry laws pass by approximating the intermediate continuous function uniformly with cylinder polynomials. Equations(U24)–(U26) prove uniqueness of its invariant probability on the gauge-invariant observable algebra: integrate the uniform mixing bound and use density. This claim concerns physical observables; it does not assign a unique gauge-variant probability from those observations alone.

The symmetric Markov semigroup has its self-adjoint generator A_infty on L2(mu)_phys. The finite real bounds pass on cylinder functions by the uniform convergence and then by L2 density, giving

    A_infty|_(1 perp)>=kappa d(|xi|).                       (U33)

On an original cylinder Fourier polynomial F, the functions (K-D_v,L)F converge in X to their infinite-label sum: at each source order they involve finite neighborhoods, and the full drift tails are bounded by the convergent local-source tail times ||KF||_X. Passing to the semigroup integral equation proves F belongs to the limiting generator domain with A_infty F=kappa(K-D_v,infty)F. In particular q_infty(F,G)=kappa mu Gamma(conjugate(F),G) on this cylinder core. This also fixes the kinetic moment in the limiting original energy pairing.

All local time-ordered correlations pass through the same product/semigroup limits. The row tails above construct bounded infinite plaquette Gram operators on l2(P_Z3), with the same bounds (U29)–(U31). Their coefficientwise local limit and norm-bounded convergence on finitely supported vectors give strong convergence on that l2 space. This is a fixed-a spatial-volume construction on the displayed coupling domain. It makes no assertion of an ultraviolet field or finite continuum mass.

## U10. Primary sources and scope

G. Lumer and R. S. Phillips, Dissipative operators in a Banach space, Pacific J. Math.11(1961),679–698, Theorem3.1, pp686–687: dense-domain dissipativity plus actual range surjectivity gives the contraction semigroup. The original theorem pages were inspected. The coefficient-domain verification is (U22)–(U24).

P. Eymard, L'algebre de Fourier d'un groupe localement compact, Bull. Soc. Math. France92(1964),181–236: Fourier-algebra antecedent. The needed compact coefficient product and domain estimates are proved here in (U3)–(U9); no claim is made to have re-audited the complete historical paper.

D. Schuette, Zheng Weihong and C. J. Hamer, The Coupled Cluster Method in Hamiltonian Lattice Field Theory, hep-lat/9603026: exponential-vacuum, gauge-invariant character, and excitation antecedents. The original constants and new heat row-sum return are derived above. The predecessor heat catalogue and the point-of-use source paths are in SOURCE_INTAKE.json. Numerical checks certify their declared finite algebra and endpoints, not the written analytical arguments as a formal proof.
