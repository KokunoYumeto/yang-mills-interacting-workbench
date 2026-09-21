# Coupled Hamiltonians, retained response classes, and two-sided energy enclosures

14 September 2026. Written continuation of the original SU(2) finite-regulator Yang–Mills calculation. Parent: `f583ed5ddb13b3ca517c1bab2958f6a4be612d78`, PR5, unmerged at intake. Original physical units and all state/energy Grams remain. The statements below concern each actual finite regulator and its specified form restrictions. No continuum mass lower bound or arithmetic spectral realization is asserted. Exact finite fixtures accompany, rather than certify, the analytic proofs. General Schur elimination and residual variational identities are established operator techniques; no general-priority claim is made.

## 1. The original form and its actual coupled realization

Retain the parent notation: `A_n=H_n-E_0,n`, `kappa_n=2g_n^2/a_n`, `rho_n=psi_n^2`, and the unitary `U_n f=psi_n f`. Its transported closed form is

    q_n(f,v)=kappa_n int rho_n sum_(e,alpha) conjugate(X_e,alpha f) X_e,alpha v.       (C1)

For a fixed refinement r<n use the same fine vacuum, its marginal m, conditional expectation E, pullback J=E*, b=2^(n-r), and kernel K=ker E from parent L6–L15. D is the nonnegative self-adjoint operator of q_n restricted to H^1_phys intersect K, constructed by the closed-form proof in parent L17. The score operator T and its actual adjoint obey

    (Th)_a=E(h S_a),   T*u=sum_a S_a J u_a,
    q_n(Jf,h)=-kappa_n b <Xf,Th>_m.                                             (C2)

Choose a finite independent list of centered smooth coarse physical functions f_1,...,f_m0. Define R x=sum_i x_i f_i. The original coarse state and kinetic Grams and kernel forcing columns are

    G=R*R,   K0_ij=kappa_n b <Xf_i,Xf_j>_m,
    W:C^m0 -> K,    W x=kappa_n b T* X(Rx).                                    (C3)

All entries are the original interacting-vacuum integrals. G is positive definite by independence. W is bounded because its domain is finite dimensional and its smooth columns are in K. On smooth kernel functions D h=(I-JE) U_n* A_n U_n h: testing C1 against the dense smooth kernel functions proves this formula. Conditional expectation preserves smoothness at fixed regulator by its compact smooth positive-density formula. Thus W and every D^j W have smooth columns in Dom(D).

Give C^m0 plus K the ORIGINAL pairing

    <(x,h),(y,k)>_G=x*G y+<h,k>_rho.

The map V(x,h)=JRx+h is an isometry onto H_F=J ran(R) plus K. Indeed the cross terms vanish by E h=E k=0 and EJ=I. Its inverse on H_F is f -> (G^-1 R* E f, f-JE f). The restriction of C1 to H_F has the block energy

    q_F((x,h),(y,k))=x*K0 y-x*W*k-<h,Wy>+q_D(h,k).                             (C4)

The operator representing it is exactly

    H_F(x,h)=(G^-1(K0 x-W*h), D h-Wx),
    Dom(H_F)=C^m0 plus Dom(D).                                                (C5)

For a domain proof, diag(G^-1 K0,D) is self-adjoint in the displayed pairing. The off-diagonal map (-G^-1 W*h,-Wx) is bounded and self-adjoint there, since its two mixed pairings are conjugates. For a real t greater than that bounded map's norm, factor H_F +/- it through diag(G^-1 K0,D) +/- it. Its resolvent has norm at most 1/t, so the remaining factor is invertible by the norm-convergent geometric series. Both ranges are the whole Hilbert space. This proves self-adjointness on exactly C5. Nonnegativity follows from C4=q_n(V.,V.) and C1.

The map to the unrestricted operator is a FORM restriction, explicitly q_F=q_n(V.,V.). It retains an additional coarse complement. For a smooth g perpendicular to ran(R) in L^2(m), a general vector in H_F plus Jg has norm

    ||JRx+h+Jg||^2=x*Gx+||h||^2+||g||_m^2,

and its energy has, in addition to q_F((x,h)) and q_n(Jg), the exact mixed term

    2 Re { kappa_n b <X(Rx),Xg>_m - kappa_n b <Th,Xg>_m }.                      (C6)

No invariance of H_F under the full operator is used. Growing coarse lists retain this complement and its displayed coupling.

## 2. Complex response and its complete Gram kernel

For z outside [0,infinity), use the existing resolvent of D and set

    M(z)=W*(D-z)^-1 W,
    F(z)=K0-zG-M(z),
    L_z x=(x,(D-z)^-1Wx).                                                     (C7)

The second block of (H_F-z)L_z is zero. The first is G^-1 F(z). The full self-adjoint resolvent of H_F exists, so F(z) is invertible: a kernel vector would give a kernel vector L_z x of H_F-z, and surjectivity follows by solving (H_F-z)(x,h)=(G^-1 y,0). With i x=(x,0) and its ACTUAL adjoint i*(x,h)=Gx,

    i*(H_F-z)^-1 i=G F(z)^-1 G.                                               (C8)

Here i* is the adjoint from the raw-G Hilbert space into the ordinary coefficient dual identified by its specified coordinates.

The resolvent identity (D-z)^-1-(D-bar(w))^-1=(z-bar(w))(D-bar(w))^-1(D-z)^-1 gives, for z,w in the upper half-plane,

    -(F(z)-F(w)*)/(z-bar(w))
       =G+W*(D-bar(w))^-1(D-z)^-1W
       =L_w* L_z.                                                            (C9)

Adjoints of the lift use the raw-G pairing. The block array with (i,j)-entry L_zi* L_zj is positive: contracting it by x_1,...,x_N gives ||sum_j L_zj x_j||_G^2. In particular

    -Im F(z)/(Im z)=L_z*L_z,
    Im F=(F-F*)/(2i).                                                        (C10)

At the negative real coordinate z=-s, s>0, write M_s=M(-s), F_s=F(-s). Then

    dF_s/ds=G+W*(D+s)^-2W=L_-s*L_-s.                                         (C11)

Thus the complex response, the restored real state metric and the coupled self-adjoint operator are connected by the stated maps. C9 also retains off-diagonal parameter pairings, not only the diagonal imaginary part. It generalizes the parent's real derivative identity on its exact finite coarse form restriction.

Positivity of C4, evaluated at (x,(D+s)^-1Wx), gives

    0 <= K0-M_s-sW*(D+s)^-2W.

Spectral monotone convergence therefore proves

    M_0 := int_(0,infinity) lambda^-1 W*dE_D(lambda)W <= K0,
    E_D({0})W=0.                                                             (C12)

## 3. Split Zero source windows and an exact response-error certificate

Let V_j be nested finite-dimensional spaces of smooth vectors in K. At support j use the actual cochain window

    V_j --(D+s)--> K --0--> 0.                                                (C13)

The transition j->j+1 is inclusion in degree zero and identity in degree one. The square commutes by restriction of the SAME D+s. The induced first cohomology is K/(D+s)V_j. Invertibility of D+s gives the exact transported-kernel isomorphism

    V_(j+1)/V_j -> ker[ K/(D+s)V_j -> K/(D+s)V_(j+1) ],
    [h] -> [(D+s)h].                                                        (C14)

For surjectivity write a killed representative as (D+s)h with h in V_(j+1). Its inverse is [(D+s)h] -> [h]; changing representative by (D+s)V_j changes h by exactly V_j. This proves both inverse laws. Applying the original Split Zero reconstruction to these windows preserves their support labels and sends each relation to the zero at its own support.

For ANY actual trial-column map Y:C^m0 -> Dom(D), put

    R_Y=W-(D+s)Y,
    B_Y=W*Y+Y*W-Y*(D+s)Y.                                                    (C15)

Expand R_Y*(D+s)^-1R_Y, with every term retained. Since (D+s)(D+s)^-1=I on K and the inverse sends K to Dom(D), the result is exactly

    M_s=B_Y+R_Y*(D+s)^-1R_Y.                                                 (C16)

In particular, for every s>0,

    B_Y <= M_s <= B_Y+s^-1 R_Y*R_Y,
    K0+sG-B_Y-s^-1 R_Y*R_Y <= F_s <= K0+sG-B_Y.                              (C17)

These are whole-matrix inequalities in the original coordinates. The independently proved F_s>=sG remains available at the same time; no matrix minimum of noncommuting bounds is introduced.

Give the forcing space K the positive pairing <r,t>_dual,s=<r,(D+s)^-1t>. Each finite boundary (D+s)V_j has an orthogonal projection for this pairing. The Galerkin columns Y_j with range in V_j are the unique solutions of

    <v,(D+s)Y_j x>=<v,Wx> for every v in V_j.

Then R_j is orthogonal in the dual pairing to (D+s)V_j and represents the original class [Wx] at support j. C16 identifies its ENTIRE quotient Gram as M_s-B_j. On the source, <(D+s)h,(D+s)v>_dual,s=q_D(h,v)+s<h,v>. Hence C14 is an isometry of these quotient pairings; the primitive, support transition and energy cost all remain explicit. Minimization over V_j subset V_(j+1) proves B_j<=B_(j+1)<=M_s. The coefficient source at support j is the chosen actual V_j, without an assumed completeness claim about a finite family.

The restoration error also has an exact norm:

    ((D+s)^-1W-Y)*((D+s)^-1W-Y)=R_Y*(D+s)^-2R_Y <= s^-2 R_Y*R_Y.              (C18)

For 0<eta<1, expansion of ||Yx+((D+s)^-1W-Y)x||^2 and 2|<u,v>|<=eta||u||^2+eta^-1||v||^2 gives

    (1-eta)Y*Y-(eta^-1-1)s^-2 R_Y*R_Y
       <= W*(D+s)^-2W
       <= (1+eta)Y*Y+(1+eta^-1)s^-2 R_Y*R_Y.                                 (C19)

Adding G encloses the restored state metric C11. The exact cross terms in C18's expansion are retained in its proof; the two inequalities are bounds on them.

## 4. Finite moment inputs, including every singular coefficient fiber

Smoothness from section 1 makes the following literal kernel moments well-defined at each finite regulator:

    N_j=W*D^jW,  j>=0,
    Z_d(x_0,...,x_d)=sum_(j=0)^d D^jW x_j.

Use V_d=ran Z_d and keep all original columns, including linear dependencies. Its state, energy-plus-shift and forcing matrices are

    J_d=[N_(i+j)]_(i,j=0)^d,
    H_d(s)=[N_(i+j+1)+sN_(i+j)]_(i,j=0)^d,
    B_d=[N_i]_(i=0)^d.                                                       (C20)

They equal Z_d*Z_d, Z_d*(D+s)Z_d and Z_d*W, respectively. Positivity gives ker H_d=ker Z_d: a zero quadratic form is q_D(Z_dx)+s||Z_dx||^2, forcing Z_dx=0. Every column of B_d is orthogonal to this kernel because x*B_d=(Z_dx)*W. For the finite Hermitian matrix H_d, range H_d=(ker H_d)^perp, so its actual normal-equation fiber is nonempty:

    H_d(s) X=B_d,  Y_d=Z_d X.                                               (C21)

Any two solutions differ by columns in ker H_d=ker Z_d, making Y_d and every formula below independent of the coefficient solution. No inverse of a singular H_d is requested. Galerkin orthogonality now yields

    B_(Y_d)=B_d*X=X*H_dX,
    R_d*R_d=N_0-C_d(s)*X-X*C_d(s)+X*J_d^(2)(s)X,
    C_d(s)=[N_(i+1)+sN_i]_(i=0)^d,
    J_d^(2)(s)=[N_(i+j+2)+2sN_(i+j+1)+s^2N_(i+j)].                           (C22)

Thus moments through order 2d+2 give both sides of C17, retaining all ranks, source fibers and physical units. C19 uses Y_d*Y_d=X*J_dX. This is a direct finite input for the response and its mass metric, not a numerical evaluation of the Yang–Mills moments in this contribution.

## 5. Exact shift recurrence and inherited resolvent mechanism

Fix a physical sigma>0 and s in (0,sigma]. Put

    T_sigma=(D+sigma)^-1,  H_(s,sigma)=(sigma-s)T_sigma,
    X_s=(D+s)^-1.

Their actual bounded-operator identity is (I-H_(s,sigma))X_s=T_sigma. This is the typed instance of source [SZ-R, SR6], whose finite ring identity retains both the constant term and exponent N+1. No arithmetic metric or scalar source mass is transferred to K.

For N>=0 let

    P_N=sum_(j=0)^N (sigma-s)^j W*(D+sigma)^(-j-1)W.

Multiplying the finite sum gives

    M_s-P_N=(sigma-s)^(N+1) W*(D+sigma)^(-N-1)(D+s)^-1W >=0.                 (C23)

Writing theta=1-s/sigma and using the spectral multiplier with C12 proves BOTH bounds

    0<=M_s-P_N<=theta^(N+1) K0,
    0<=M_s-P_N<=theta^(N+1)s^-1 N_0.                                        (C24)

All coefficients and the physical sigma remain. These estimates apply to the unbounded original D because the displayed resolvents are bounded functions of its proved self-adjoint spectral resolution. For fixed s0>0 and s in [s0,sigma], theta<=1-s0/sigma<1, explicitly controlling the iteration count for this actual source. The endpoint s=0 is retained through C12 and the parent's inverse-energy endpoint analysis; C24 makes no uniform-in-s positive lower-edge assertion.

## 6. Evaluated original parameter bounds and the active next calculation

For F containing the coarse edges on which the chosen f_i depend, put

    B_F=ess sup_W sum_i sum_a |X_a f_i(W)|^2.

It is finite for the chosen smooth list. Conditional Cauchy–Schwarz and parent L8 give

    N_0 <= (kappa_n b)^2 B_F I_F I_m0
        <= (32 |F| b^2/a_n^2) B_F I_m0,
    K0 <= kappa_n b B_F I_m0.                                               (C25)

The exact coefficient identity is kappa_n^2 xi_n=1/a_n^2. In C25 the scalar I_F is the parent's INTEGRATED score trace; it is used only after the explicit supremum B_F, never substituted for a pointwise score bound. Consequently C24 supplies explicit response-error bounds

    M_s-P_N <= theta^(N+1) kappa_n b B_F I_m0,
    M_s-P_N <= theta^(N+1) (32 |F| b^2/(s a_n^2)) B_F I_m0.                  (C26)

These have no exterior-volume factor. The ultraviolet, coupling, source-family and s dependence stays in the displayed expressions.

The next selected task is evaluation/enclosure of the actual N_0,N_1,N_2 in C20–22 for the original loop/energy observables, including conditional vacuum derivatives, followed by comparison of the C17 energy interval with the C19 restored metric on growing lists. The first degree already uses a specified finite triple of matrices. No vacuum integrals in those three matrices have been numerically evaluated here. The independent coarse complement C6, the parent's escaping-state quotient, and the full four-dimensional identification remain recorded quantities. A strict positive continuum physical edge has not been established.

## 7. Cross-workbench source and result record

[YM] Parent PR5, commit f583ed5ddb13b3ca517c1bab2958f6a4be612d78, `yang-mills/research-control/RESEARCH_NOTE.md`, blob d138482ac7b40017560cef5a93b21ada4440ce13. Complete delivered body read; original conditional score coupling, closed kernel form and energy section used.

[SZ-R] Zeta PR31 commit b4060b25c21f1a49a5e7730e9aff76d4c93c820d, `workbenches/tau-signed-resolvent-formal/RESEARCH_NOTE.md`, blob 7166debc7724f6805aac125a012e3a59d594dc84, sections 1–6 read. SR6 is instantiated by the EXACT map H->(sigma-s)(D+sigma)^-1, T->(D+sigma)^-1, X->(D+s)^-1. Its finite algebraic identity is rederived in C23. Its historical Lean execution was not rerun here.

[SZ-M] Zeta PR32 commit 9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6, observation-metric note blob 866ed2f6e8ed9ca544f6ec0af97c5dec3fecedad, already proof-read in the parent. Its original-metric section identity is instantiated by source metric <r,(D+s)^-1t>, relation map (D+s)|V_j and source columns W in C13–18. Both identities are proved above in their actual spaces.

[F] G. Dusson, I. M. Sigal, B. Stamm, *The Feshbach-Schur map and perturbation theory*, arXiv:2105.02058 (2021). Abstract consulted for method attribution, not as a premise supplying Yang–Mills estimates. The general coupling/elimination mechanism is an established method. All domain and coefficient calculations used here are written above.

Current peer intake: Zeta main advanced to 91ed3b7c358a1f444d0d48c292e4a400ca509eff. Its current README lines 1–80 and the four-commit comparison were read for orientation. Its new conductor/arithmetic asymptotics are not imported as proved estimates here. A search of tracked open peer PRs updated since the parent's intake found Erdős–Straus PR7, with higher-support and uniform Green-norm calculations; only its description was read, and it is a candidate for actual proof inspection. Collatz, Erdős 817 and Erdős–Straus main refs were refreshed and retain their previous revisions.

The user's Hamiltonian/self-adjointness suggestion is retained as a cross-workbench research direction. C5–11 provide the actual transferable operator construction and metric identity; no unspecified arithmetic spectrum is assigned to it. No personal-memory feature, autonomous watcher, paid model job or automatic merge is activated.
