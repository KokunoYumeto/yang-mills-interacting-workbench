# Local density-derivative control and exact energy-minimizing refinement

14 September 2026. A continuation of the full SU(2) Yang–Mills workbench.

This note proves statements about the original finite-regulator Hamiltonian at every positive spacing and coupling. It retains the physical constants, interacting vacuum, observation kernel, and both the energy and state-norm pairings. The continuum mass-gap conclusion is not established here. The executable companion checks declared finite algebraic fixtures; the analytic arguments are the written proofs below, not a new Lean certificate. No general priority claim is made.

## 1. Original objects and the precise mass-gap quantity

Fix the workbench's open graph with vertices {-L,...,L}^3, L>=2, its complete positively oriented edges and faces, a>0 and g>0. Use T_alpha=-i sigma_alpha/2 and its original left derivatives X_(e,alpha). Set

    kappa=2g^2/a, v=1/(2g^2 a), xi=v/kappa=1/(4g^4),
    E_e=-sum_alpha X_(e,alpha)^2,
    H=kappa sum_e E_e+v sum_p(2-tr U_p),
    A=H-E_0 I, rho=psi^2.

Here psi is the actual positive unit vacuum and E_0 its energy. [YM1, sections 1–2] supplies self-adjointness, the invariant H^2 operator domain, invariant H^1 form domain, compact resolvent, smooth positivity and uniqueness of this vacuum. Multiplication

    U:L^2_phys(rho dU)->H_phys, f |-> psi f

has inverse u |-> u/psi and satisfies <Uf,Uh>=int rho conjugate(f)h. The original ground-state identity is

    q(f,h):=<Uf,A Uh>=kappa int rho sum conjugate(Xf)Xh.       (L1)

The equality is interpreted as a form identity on H^1. All subsequent q notation uses this transported form, not a newly selected Hamiltonian.

On centered physical H^1 functions let d f=(X_(e,alpha)f), and give its image the pairing kappa int rho sum conjugate(u)v. A zero derivative makes f constant on the connected product group; centering makes that constant zero. Thus the actual primitive p(d f)=f is well-defined. The spectral variational principle, through U, gives

    ||p||^2=sup_(f centered, f!=0) ||f||_rho^2/q(f,f)=1/Delta. (L2)

Delta is the first physical excitation energy of this finite regulator. This identity fixes the quantity to which later estimates return; no numerical value for Delta is inserted.

## 2. A local all-coupling electric bound

Let r_e be the number of original plaquettes incident on e and W_e their trace sum. In this open graph r_e<=4. Retain the exact decomposition from [YM2, section 2]

    A=kappa E_e+K_e-v W_e,
    K_e=H_ext,e+2v r_e-E_0 >=0.                              (L3)

To verify the sign, use a vector constant on e and an exterior ground vector. Every term of W_e has zero Haar integral in that link, so E_0<=inf H_ext,e+2v r_e. K_e acts on exterior variables and strongly commutes with E_e.

The original vacuum equation is (kappa E_e+K_e)psi=v W_e psi. With gamma_e=<psi,E_e psi>, taking its expectation and using ||W_e||<=2r_e proves

    0<=gamma_e<=2r_e xi.                                    (L4)

Joint spectral calculus also gives ||E_e psi||<=2r_e xi. The original single-link eigenvalues j(j+1), j=0,1/2,1,..., give E_e<=(4/3)E_e^2. Therefore

    gamma_e <= (16/3) r_e^2 xi^2,
    gamma_e <= eta_e:=min(2r_e xi,(16/3)r_e^2 xi^2).          (L5)

Every exterior interaction remains in K_e. Equations L4 and L5 hold at all positive g; their different coupling dependence is retained.

## 3. The full conditional score and an exterior-volume-free bound

Use the already specified dyadic spatial refinement r<n, with b=2^(n-r) fine edges in each ordered coarse edge. All objects in this section use the actual fine vacuum rho_n. The global coordinate map Phi_(r,n) sends a chain to its ordered product W_e=U_(e,1)...U_(e,b), its first b-1 links, and all unused fine links. Its inverse retains those links and sets

    U_(e,b)=(U_(e,1)...U_(e,b-1))^(-1) W_e.

Haar translation gives dU_n=dW dz. Write

    m(W)=int rho_n(Phi^(-1)(W,z)) dz,
    (E f)(W)=m(W)^(-1) int f rho_n dz,  Jg=g o pi_(r,n).

E:L^2_phys(rho_n dU_n)->L^2_phys(m dW), J in the opposite direction, obey EJ=I and E=J*. Their projection is P=JE and their retained kernel is K=ker E. Smoothness and positivity hold on these compact manifolds.

For the original prefixes P_(e,j-1), put

    a_(e,j;alpha,beta)=(Ad P_(e,j-1))_(alpha,beta),
    Y_(e,alpha)=b^(-1) sum_(j,beta) a_(e,j;alpha,beta) X_(e,j,beta).

The full coefficient matrices, including the prefix dependence, remain present. Their adjoint-matrix identities give

    Y_(e,alpha) Jg=J X_(e,alpha)g,
    sum_alpha |Y_(e,alpha)psi_n|^2
       <= b^(-1) sum_(j,beta)|X_(e,j,beta)psi_n|^2.          (L6)

Each coefficient is independent of its own differentiated link. Thus Y has Haar divergence zero. Integration by parts against every smooth coarse test function yields

    X_a E f=E(Y_a f)+E(f S_a),
    S_a=Y_a log rho_n-J X_a log m,  E S_a=0.                (L7)

Here a=(e,alpha); this index is unrelated to physical spacing. Substituting f=1 before subtracting proves the last equation and identifies J X_a log m as the conditional mean of Y_a log rho_n. These are the original fields of [YM3, section 3].

For a finite set F of coarse edges, retain the entire conditional matrix

    Gamma_(a,c)(W)=E(S_a S_c)(W), a,c in F x {1,2,3}.

It is positive semidefinite because z*Gamma z=E(|sum_a z_a S_a|^2). Its exact integrated trace is the conditional variance of Y log rho_n. In particular

    I_F:=int m tr Gamma
       =sum_(a in F x {1,2,3}) [int rho_n |Y_a log rho_n|^2
                               -int m |X_a log m|^2]
       <= (4/b) sum_(e in F) sum_(j=1)^b gamma_(e,j)
       <= (4/b) sum_(e in F) sum_(j=1)^b eta_(e,j)
       <= 32 |F| xi_n.                                    (L8)

Proof: conditional variance gives the first inequality after dropping its explicitly displayed nonnegative coarse term. The identity rho_n |Y log rho_n|^2=4|Y psi_n|^2 and L6 give the next expression. L4–5 apply to the original fine links. Finally r_(e,j)<=4 gives eta_(e,j)<=8xi_n, and there are b links in each of the |F| chains.

This replaces an exterior-volume-dependent bound for this local quantity with one depending on the chosen coarse-edge count and actual coupling. It does not give a pointwise bound on Gamma(W). Along the explicit test path g_n^2=(g_0^(-2)+beta n log 2)^(-1), L8 reads

    I_F <= 8|F|(g_0^(-2)+beta n log 2)^2.                   (L9)

That growth is retained; beta remains a prescribed path parameter, not an identified quantum beta-function coefficient.

## 4. The score is the exact off-diagonal Hamiltonian map

First work in the full scalar L^2 spaces and their coarse vector-field space with counting of generator indices. The following operators restrict to the physical scalar and gauge-covariant vector-field spaces: individual generator components rotate by adjoint matrices, and their contractions are invariant.

Define the bounded finite-regulator map

    T:K->L^2(m; coarse generator coordinates),
    (T h)_a=E(h S_a).

Its adjoint is

    T* u=sum_a S_a J u_a,                                  (L10)

which belongs to K because E S_a=0. Direct substitution proves

    T T* u=Gamma u,
    ||T* u||_rho^2=int m u*Gamma u.                         (L11)

The fields S are real smooth functions, so these formulas also retain the conjugations for complex f,u. In particular all mixed entries of Gamma survive. For h in K the pointwise conditional Cauchy–Schwarz identity gives

    (Th)(Th)* <= E(|h|^2) Gamma.                            (L12)

Contraction by any z proves it as the scalar inequality
|E(h z*S)|^2<=E(|h|^2)E(|z*S|^2).

Let q_n be L1 and retain kappa_n=2g_n^2/a_n. For smooth g and h in K, the original horizontal/vertical splitting and L7 give

    q_n(Jg,h)=-kappa_n b <Xg,T h>_m,
    q_n(Jg,Jv)=kappa_n b <Xg,Xv>_m.                         (L13)

For completeness, X_(e,j,beta)Jg=sum_alpha a_(e,j;alpha,beta)JX_(e,alpha)g. Summing its pairing with Xh gives b<Xg,E Yh>; L7 with Eh=0 makes E Yh=-T h. Unused fine-edge derivatives of Jg vanish, proving both identities without removing any face potential from H.

Thus the exact off-diagonal generator on smooth coarse functions is

    C g:=(I-P) U_n^* A_n U_n Jg=-kappa_n b T* Xg.           (L14)

The weak identity L13 proves L14 by testing against smooth kernel vectors, which are dense in K. The coarse component is the represented operator

    A_c g=-kappa_n b m^(-1) sum_a X_a(m X_a g),
    U_n^* A_n U_n Jg=J A_c g+Cg.                            (L15)

This explicitly connects the retained density derivative with the full operator, rather than assigning it only a support label.

For a coarse g whose derivatives are supported in the coordinates of F, L8 and L11 also prove

    ||Cg||_rho^2
       <= (kappa_n b)^2 ||Xg||_(infinity,l2)^2 I_F
       <= 32 |F| b^2/a_n^2 ||Xg||_(infinity,l2)^2.          (L16)

The last equality of coefficients uses (2g_n^2/a_n)^2 xi_n=1/a_n^2. The factor b^2/a_n^2 is retained. This is an explicit smooth-observable bound, not an operator bound obtained from an integral trace bound.

## 5. Exact minimum-energy section, residual Gram, and mass derivative

Let s>0 and q_(n,s)=q_n+s<.,.>_rho. On K restrict q_n to H^1_phys intersect K; call its represented nonnegative self-adjoint operator D. Here are the domain details. Conditional expectation preserves H^1 at fixed regulator: L7, conditional Cauchy–Schwarz, bounded smooth S and the finite coefficients of Y bound each coarse derivative by the fine H^1 norm. J also preserves H^1. Hence (I-P) sends smooth functions to smooth kernel functions and approximates every L^2 kernel vector. The restricted form is densely defined. It is closed because K is L^2 closed and q_(n,s) is equivalent to the original H^1 norm at this fixed positive smooth density. This proves the assertions about D by the representation of closed nonnegative forms. No regulator-uniform norm-equivalence constant is claimed.

For g in coarse H^1 define

    h_s(g)=kappa_n b (D+s)^(-1) T* Xg,
    S_s g=Jg+h_s(g).                                       (L17)

The inverse exists with norm at most 1/s. T*Xg is in K and L^2, so h_s is in Dom(D). Equation L13 extends by H^1 continuity. It proves, for every kernel k in the form domain,

    q_(n,s)(k,S_s g)=0,  E S_s g=g.                         (L18)

Every lift f with Ef=g has the unique expression f=S_sg+k. Therefore

    q_(n,s)(f,f)=q_eff,s(g,g)+q_(n,s)(k,k),
    q_eff,s(g,v)=s<g,v>_m+kappa_n b<Xg,Xv>_m
       -(kappa_n b)^2 <T*Xg,(D+s)^(-1)T*Xv>_rho.            (L19)

These identities prove that S_s is the unique energy-minimizing section on each original observation fiber. The induced form is closed on coarse H^1: the boundedness of E and J in H^1 gives upper and lower equivalence with the coarse H^1 norm at this fixed regulator, and the minimizer supplies the quotient norm. Every mixed family follows by polarization, not by deleting cross entries.

The original state norm has its separate exact expression

    ||f||_rho^2=||g||_m^2+||h_s(g)+k||_rho^2.               (L20)

Thus the state-norm cross term 2 Re<h_s(g),k> is retained. For a rectangular list of lifts X and their observed columns Z, canonical residual R=X-S_s Z satisfies the full Gram identity

    Gram_(q_n,s)(R)=Gram_(q_n,s)(X)-Gram_(q_eff,s)(Z).        (L21)

In finite coordinates with raw state Gram G and raw energy matrix E_mat, use Q_s=E_mat+sG and an onto observation Lambda. Then

    W_s=(Lambda Q_s^(-1) Lambda*)^(-1),
    S_s=Q_s^(-1) Lambda* W_s,
    (X-S_s Lambda X)*Q_s(X-S_s Lambda X)
       =X*Q_s X-(Lambda X)*W_s(Lambda X).                   (L22)

This is the explicit instantiation of [SZ2, OK1–2] with its source Gram mapped to Q_s and its observation mapped to Lambda. A fixed section J differs by S_s-J in ker Lambda; the difference and its full norms remain in L20–22.

Differentiating the actual resolvent in L19 gives

    d/ds q_eff,s(g,v)
       =<g,v>_m+(kappa_n b)^2<T*Xg,(D+s)^(-2)T*Xv>_rho
       =<S_sg,S_sv>_rho.                                  (L23)

The derivative is exactly the state Gram of the restored vectors. This is an infinite-dimensional conditional-observation version of the earlier finite-frame memory identity.

## 6. Exact composition over arbitrarily many finite refinement levels

Fix r<t<n and keep the same fine vacuum rho_n throughout. Let E_(t,n), E_(r,n) be the preceding observations. Let E_(r,t)^(n) be conditional expectation from the marginal m_(t,n) to m_(r,n). Fubini proves

    E_(r,n)=E_(r,t)^(n) E_(t,n).                            (L24)

Define S_(t,n;s) by minimizing q_(n,s), and on the middle space use exactly the induced form q_eff,(t,n;s). Let S_(r,t;s)^(n) be its minimum section for E_(r,t)^(n). Then

    S_(r,n;s)=S_(t,n;s) S_(r,t;s)^(n).                      (L25)

Proof: for f with coarse value g, put y=E_(t,n)f. L19 decomposes its energy as q_eff,(t,n;s)(y)+the nonnegative fine residual energy. The values y range over exactly the fiber E_(r,t)^(n)y=g, since each has its fine lift S_(t,n;s)y. Minimizing the middle fiber and then lifting gives the unique fine minimizer, proving L25 and its inverse observation law. The same argument iterates to every finite chain of levels and retains the sum of the actual residual energies at all levels.

The middle form and density in this identity are written explicitly. In particular, the identity-on-functions comparison to the separately constructed regulator-t vacuum has pairing

    <f,h>_(m_t,n)=int conjugate(f)h (m_(t,n)/rho_t) rho_t.

No equality of those two measures is presumed. No independent Markov property across scales is presumed. The complete state Gram in the energy-section coordinates is transported by the original synthesis map and retains all off-diagonal entries.

The finite algebra behind L25 is precisely the composed-minimum-lift identity [SZ1, AMT7–9]. For onto Lambda_1,Lambda_2 and positive Q,

    Q_1=(Lambda_1 Q^(-1) Lambda_1*)^(-1),
    Q_2=(Lambda_2 Q_1^(-1) Lambda_2*)^(-1),
    S_(Lambda_2 Lambda_1,Q)=S_(Lambda_1,Q) S_(Lambda_2,Q_1).

Substitution of Q_1^(-1)=Lambda_1 Q^(-1) Lambda_1* proves it directly. The exact checker evaluates this on non-diagonal energy and norm matrices, with nonzero kernel corrections.

## 7. Completed advance and current mathematical direction

L8 is a local all-coupling score estimate independent of exterior volume. L14 identifies that score with the original Hamiltonian's off-diagonal map. L17–23 give its complete energy-minimizing section and restored state metric. L24–25 prove their finite refinement composition with the actual induced intermediate forms. These are a connected calculation on the same original vacuum; none of them sets the memory, kernel, or state-metric cross terms to zero.

The next chosen research quantity is the response matrix/form

    (kappa_n b)^2 <T*Xg,(D+s)^(-1)T*Xv>

relative to the full kinetic energy kappa_n b<Xg,Xv> and the restored metric L23, on increasing physical observable families. The integral bound L8 has no asserted pointwise replacement. Its n-dependent coefficient L9 and the ultraviolet coefficient L16 remain explicit. A uniform positive physical lower edge, a nontrivial four-dimensional continuum field, and treatment of every compact simple gauge group are not supplied by these calculations. SU(2) is the present workbench's literal gauge group.

## 8. Sources actually used and review scope

[YM1] KokunoYumeto/yang-mills-interacting-workbench, main fab69fdc4ac197159b8e6ae8d73a82bde2b20d55, yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md, sections 1–2 and 6. Git blob dfee77c0ca0d6ed897c4172fcbfe23cd9d10d313. Original objects, domains, vacuum and gap characterization.

[YM2] Same main, yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md, sections 1–3. Git blob 66a7453a6452c2555a28270efcf53fa1997c26a8. Original local exterior comparison and electric estimates. The new linear expectation bound L4 is proved above from its full equation.

[YM3] Same repository, unmerged PR4 head dc390930a8d2774e93481206602973caff7aa7da, yang-mills/continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md, sections 3 and 5. Git blob 0d79c733ff6209c991dd2b52474b1e399dd812db. Full source is present in this branch; its delivered bytes were matched to that blob and its earlier checker replayed in this session.

[SZ1] KokunoYumeto/zeta-function-research-reader, main 8fd2157e8b41783224b42781699432d824ec0c15, workbenches/splitzero-tandem/continuations/20260914-original-kernel-web/13_ARITHMETIC_MIXED_TRANSFER.tex, AMT1–10 (source lines 1–275 inspected). Git blob b6cfec2ac9517acc378aa02686ada6e7923ef381. Only its explicit finite metric/minimum-section mechanism is instantiated here; its arithmetic constants and later asymptotics are not assigned to Yang–Mills.

[SZ2] Same repository, unmerged PR32 head 9cec8482f2ecf978cf8bdb67b4c080b9dd74f5d6, workbenches/tau-observation-kernel-formal/RESEARCH_NOTE.md, sections 1–7 inspected. Git blob 866ed2f6e8ed9ca544f6ec0af97c5dec3fecedad. Complete rectangular corrected residual and observed-iterate maps. Its reported Lean run was not rerun in this session.

The workflow's peer intake additionally records Collatz, Erdős–Straus and Erdős 817 observations with their exact review scopes. Those independent source identities are not certificates for the analytic results in this note.
