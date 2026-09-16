\frontmatter
\begin{titlepage}
\centering
\vspace*{25mm}
{\large Research source reader\par}
\vspace{12mm}
{\Huge\bfseries Yang--Mills\par}
\vspace{8mm}
{\LARGE Complete web-session continuation\par}
\vspace{5mm}
{\Large 14--16 September 2026\par}
\vfill
{\large Complete mathematical source bodies,\par
source provenance, and accompanying review records\par}
\vspace{12mm}
{\normalsize Consolidated 16 September 2026\par}
\end{titlepage}

\chapter*{About this source reader}
\addcontentsline{toc}{chapter}{About this source reader}

This volume brings together the complete mathematical Markdown source bodies
of the Yang--Mills continuation delivered on 14--16 September 2026. It is a
documentary consolidation: it does not replace the original source files and
does not confer blanket certification on their mathematical claims. Each
chapter records its exact repository-relative source path and SHA-256 digest.
The accompanying machine-readable manifest records source sizes and ordering.

The sources retain their original hypotheses, constants, coordinates, signs,
orientations, domains, codomains, proofs, and research status. Original TeX
mathematics is typeset as mathematics. Original plain-text formulas remain in
monospaced blocks; long lines may wrap typographically without changing their
content. Original source headings and all source-body paragraphs are retained.
No new mathematical simplification or normalization is performed by the build.

These continuations primarily concern original finite-lattice SU(2) Hamiltonians,
their interacting vacua, physical excitation estimates, Wilson observables,
and specified spatial-volume or reconstruction limits. Coupling and regulator
hypotheses belong to the individual statements. A finite-lattice estimate or a
fixed-spacing spatial-volume statement is not by itself a proof of the
four-dimensional continuum Yang--Mills mass-gap problem. Source claims should
be read with their exact hypotheses and with any later review chapters in this
edition. Finite executable checks verify the fixtures they test; they are not
a formal verification of all analytic arguments.

Earlier foundational source volumes and their readable PDFs remain in the
repository under \texttt{yang-mills/sources/} and
\texttt{yang-mills/readers/}. References to those earlier sources are retained
as written. This continuation volume preserves the full new source bodies,
rather than replacing them with summaries.

Where an additional chapter is explicitly labelled as a transcript-derived
mathematical final response, it recovers only that public final response. It
does not imply that a missing attachment has been recovered. User messages
and model thinking are not included in this volume. An independent review,
when included, is identified separately from the source it reviews.

\tableofcontents
\mainmatter


# Local density-derivative control and exact energy-minimizing refinement

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/research-control/RESEARCH_NOTE.md}

\textbf{SHA-256:} \path{67454e30bc6a0a5f24ef2b63aac16ea05cd4b9fcc087688d351f7b0191a016ec}
\end{quote}


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


# Coupled Hamiltonians, retained response classes, and two-sided energy enclosures

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260914-coupled-response/RESEARCH_NOTE.md}

\textbf{SHA-256:} \path{b787a444d6c3995ac39fbc71a4f114478cad824172c40e33a32930661a771433}
\end{quote}


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


# Continuum spectral reconstruction from retained smooth correlation kernels

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260914-spectral-reconstruction/RESEARCH_NOTE.md}

\textbf{SHA-256:} \path{5fffd882e97df0499263875d344f40935561106f0389077b2f832a7c3c568ba0}
\end{quote}


Date: 14 September 2026

This continuation starts from the full finite-regulator Hamiltonians and Wilson/Schur maps already retained in `yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_WILSON_SCHUR_MEMORY.md`, together with the smooth-frame lesson supplied by the explicit S6 normal-line trivialization in `s6/27_s6_key_advances_frozen_2026-09-06.tex`. Every Gram matrix and every spectral measure below is kept in its original coordinates.

## 1. Countable gauge-invariant observable system

For each finite open lattice `n`, let `A_n=H_n-E_{0,n}I` on the physical Hilbert space and let `psi_n` be the positive unit vacuum. Let `mathscr O` be the countable union, over all lattice levels, of gauge-invariant spin-network functions obtained from finite SU(2) representation labels and fixed finite intertwiner bases. Pull a member born at level `N(i)` to every finer level by the exact ordered edge-product refinement map. Denote the resulting bounded multiplication observable by `O_{i,n}`.

For `n>=N(i)` set

\[
 r_{i,n}=(O_{i,n}-\langle\psi_n,O_{i,n}\psi_n\rangle)\psi_n
\]

and

\[
 C^{(n)}_{ij}(t)=\langle r_{i,n},e^{-tA_n}r_{j,n}\rangle,\qquad t>0.
\]

For every fixed pair `(i,j)` and every integer `q>=0`, spectral calculus gives

\[
 \left|\frac{d^q}{dt^q}C^{(n)}_{ij}(t)\right|
 \le 4\|O_i\|_\infty\|O_j\|_\infty
 \left(\frac{q}{et}\right)^q,
\]

with the `q=0` factor interpreted as one. Indeed

\[
 \frac{d^q}{dt^q}C^{(n)}_{ij}(t)
 =(-1)^q\langle r_{i,n},A_n^qe^{-tA_n}r_{j,n}\rangle,
\]

`||r_{i,n}||<=2||O_i||_infty`, and

\[
 \|A_n^qe^{-tA_n}\|=\sup_{\lambda\in\sigma(A_n)}\lambda^qe^{-t\lambda}
 \le\sup_{\lambda\ge0}\lambda^qe^{-t\lambda}
 =\left(\frac{q}{et}\right)^q.
\]

Diagonal extraction over the countable triples `(i,j,q)` and rational compact positive-time intervals therefore supplies one regulator subsequence `n_k` and smooth limits

\[
 C_{ij}(t)=\lim_{k\to\infty}C^{(n_k)}_{ij}(t)
\]

in `C^infty_loc((0,infty))` for every `i,j`.

For every finite set of labels, every positive times `s_a`, and every complex coefficients `z_a`,

\[
 \sum_{a,b}\overline{z_a}z_b C_{i_ai_b}(s_a+s_b)\ge0
\]

because this is the limit of the corresponding finite-regulator squared norms.

## 2. Reconstructed continuum observable Hilbert space and generator

Let `D` be the complex vector space generated by symbols `[i,s]`, `i in mathbb N`, `s>0`, and define

\[
 \langle[i,s],[j,t]\rangle=C_{ij}(s+t).
\]

Quotient by the exact null space of this sesquilinear form and complete. Call the resulting Hilbert space `H_obs`. Define

\[
 T(u)[i,s]=[i,s+u],\qquad u\ge0.
\]

The kernel identity gives `T(u+v)=T(u)T(v)`. Positivity and the spectral-calculus derivative bounds inherited above give strong continuity on the dense symbol span. The operators `T(u)` are positive self-adjoint contractions. Hence there is a nonnegative self-adjoint generator `A_obs` with

\[
 T(u)=e^{-uA_{obs}}.
\]

The limits

\[
 \xi_i=\lim_{s\downarrow0}[i,s]
\]

exist exactly when the finite-energy zero-time matrix

\[
 G^f_{ij}=\lim_{t\downarrow0}C_{ij}(t)
\]

is finite; the bounded-observable estimates above give finiteness. Their spectral matrix measure is

\[
 \mu_{ij}(B)=\langle\xi_i,E_{A_{obs}}(B)\xi_j\rangle,
\]

and

\[
 \boxed{C_{ij}(t)=\int_{[0,\infty)}e^{-t\lambda}\,d\mu_{ij}(\lambda).}
\]

The closure of the union of the diagonal supports is exactly the spectrum:

\[
 \boxed{\sigma(A_{obs})=
 \overline{\bigcup_i\operatorname{supp}\mu_{ii}}.}
\]

Proof. A Borel open set `U` with `mu_ii(U)=0` for every `i` has

\[
 \|E(U)\xi_i\|^2=\mu_{ii}(U)=0.
\]

Therefore `E(U)e^{-sA_obs}\xi_i=0` for every `i,s`; these vectors span a dense subspace by construction, so `E(U)=0`. Conversely a point in `supp mu_ii` has nonzero spectral projection in every open neighbourhood. The spectral characterization of a self-adjoint operator then gives the displayed equality.

This identifies the exact spectral object reconstructed by the continuum correlation system.

## 3. Constructive recovery from positive time only

Fix `h>0` and put

\[
 x=e^{-h\lambda}\in(0,1].
\]

Push `mu_ij` forward by this map and denote the resulting matrix measure on `(0,1]` by `nu_ij`. Set

\[
 M_0=\lim_{t\downarrow0}C(t),\qquad M_m=C(mh)\quad(m\ge1).
\]

Then, entry by entry,

\[
 M_m=\int_{(0,1]}x^m\,d\nu(x),\qquad m\ge0.
\]

For every continuous scalar function `f` on `[0,1]`, define its Bernstein polynomial

\[
 B_Nf(x)=\sum_{k=0}^N f(k/N){N\choose k}x^k(1-x)^{N-k}.
\]

Expansion in monomials gives the coordinate-level recovery formula

\[
 \boxed{
 \int B_Nf\,d\nu
 =\sum_{k=0}^N\sum_{j=0}^{N-k}
 f(k/N){N\choose k}{N-k\choose j}(-1)^jM_{k+j}.
 }
\]

Bernstein uniform convergence on `[0,1]` and finiteness of the matrix measure give

\[
 \boxed{
 \int f\,d\nu
 =\lim_{N\to\infty}
 \sum_{k=0}^N\sum_{j=0}^{N-k}
 f(k/N){N\choose k}{N-k\choose j}(-1)^jM_{k+j}.
 }
\]

Thus the complete finite-energy matrix spectral measure is determined constructively by the retained positive-time values `C(mh)` together with `C(0+)`. No frequency discretization is introduced.

For a continuous function `phi` on the one-point compactification `[0,infty]` whose value at infinity is fixed to zero, take

\[
 f(x)=\begin{cases}
 \phi(-h^{-1}\log x),&x>0,\\
 0,&x=0.
 \end{cases}
\]

The preceding formula then reconstructs `int phi(lambda) dmu(lambda)` directly from the positive-time continuum kernel.

## 4. Resolvent and exact interval masses

Define the positive-half-line Stieltjes matrix

\[
 S(s)=\int_0^\infty e^{-st}C(t)\,dt
 =\int_{[0,\infty)}\frac{d\mu(\lambda)}{\lambda+s},\qquad s>0.
\]

Every entry is finite and analytic on `Re s>0`. Let

\[
 R(z)=\int_{[0,\infty)}\frac{d\mu(\lambda)}{\lambda-z},
 \qquad z\in\mathbb C\setminus[0,\infty).
\]

On the negative real axis `R(-s)=S(s)`, so the analytic function `R` is uniquely fixed by the retained positive-time data.

Use the matrix imaginary part `Im R(z)=(R(z)-R(z)^*)/(2i)`, which retains the complex off-diagonal entries of the spectral measure. For `0<a<b<infty`, entrywise integration of the Poisson kernel gives

\[
 \boxed{
 \lim_{\eta\downarrow0}\frac1\pi
 \int_a^b\operatorname{Im}R(x+i\eta)\,dx
 =\mu((a,b))+\frac12\mu(\{a\})+\frac12\mu(\{b\}).
 }
\]

The atom at `lambda_0>=0` is recovered by

\[
 \boxed{
 \mu(\{\lambda_0\})
 =\lim_{\eta\downarrow0}
 \eta\,\operatorname{Im}R(\lambda_0+i\eta).
 }
\]

Both identities hold as matrix identities because they hold after contraction by every finite coefficient vector and polarization recovers each entry.

## 5. Exact gap readout on the reconstructed observable sector

For every nonzero diagonal measure define

\[
 m_i=\inf\operatorname{supp}\mu_{ii}.
\]

The Laplace principle here requires no density. The upper estimate

\[
 C_{ii}(t)\le \mu_{ii}([0,\infty))e^{-m_it}
\]

and, for every `epsilon>0`, the support property

\[
 C_{ii}(t)\ge
 \mu_{ii}([m_i,m_i+\epsilon))e^{-(m_i+\epsilon)t}
\]

prove

\[
 \boxed{
 m_i=\lim_{t\to\infty}-\frac1t\log C_{ii}(t).
 }
\]

Combining this with the spectral-support equality yields the exact observable-sector spectral bottom

\[
 \boxed{
 \inf\sigma(A_{obs})
 =\inf_i\lim_{t\to\infty}-\frac1t\log C_{ii}(t).
 }
\]

All centered Wilson/spin-network labels remain present. The spectral-support and large-time formulas determine the reconstructed fixed-label observable sector. The regulator-state comparison has the retained kernel `K/N` constructed in [the vacuum-refinement continuation, Section 6](../20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md#6-the-regulator-state-comparison-and-the-escaping-label-kernel); its equation (6.6) computes an escaping-label class together with its norm and energy sequence.

## 6. Retaining the energy-infinity endpoint

The positive-time map annihilates a compactified atom at `lambda=infty`. Let the weak compactified regulator measure have endpoint matrix `E_infty`. Let `G^c` denote its complete zero-time Gram limit before applying the positive-time multiplier. Then

\[
 \boxed{E_\infty=G^c-\lim_{t\downarrow0}C(t).}
\]

This is the same retained Split-Zero endpoint class already isolated in the previous continuation. The finite-energy measure reconstructed in Sections 3--5 and `E_infty` together give the complete compactified matrix measure.

## 7. Smooth frames and the S6 continuation mechanism

The S6 finite filling has the explicit nowhere-zero smooth section

\[
 H_j(x)=\exp(-2\pi i\varepsilon_j\gamma(x))
\]

and the mutually inverse smooth maps

\[
 [x,n]\mapsto([x],n/H_j(x)),\qquad
 ([x],z)\mapsto[x,zH_j(x)].
\]

The operation needed for the Yang--Mills smooth observable family is the corresponding finite-coordinate frame transport. Let `T(theta)` be an invertible smooth matrix relating two retained raw observable frames. Their correlation kernels and spectral measures obey

\[
 C^{T}(t,\theta)=T(\theta)^*C(t,\theta)T(\theta),
\]

\[
 \mu^{T}(B,\theta)=T(\theta)^*\mu(B,\theta)T(\theta).
\]

The inverse map is written explicitly:

\[
 \mu(B,\theta)=T(\theta)^{-*}\mu^T(B,\theta)T(\theta)^{-1}.
\]

Therefore

\[
 \mu^T(B,\theta)=0\quad\Longleftrightarrow\quad\mu(B,\theta)=0.
\]

The spectral support recovered from a complete retained frame is invariant under this smooth invertible transport while the full raw Gram matrices remain stored. This is the precise continuation mechanism used here; no orthonormalization is performed.

## 8. What this advances

The continuum programme now contains a direct spectral extraction layer rather than only variational quotients:

1. a single subsequence carries all correlations of a countable gauge-invariant cylindrical family;
2. those kernels construct a positive self-adjoint continuum observable generator;
3. its complete finite-energy matrix spectral measure is reconstructible from positive-time data by an explicit Bernstein-moment formula;
4. Stieltjes inversion recovers interval masses and atoms;
5. the bottom of its spectrum is exactly the infimum of the large-time exponential edges of the diagonal correlations;
6. the compactified energy-infinity class remains separately retained by the zero-time Gram defect;
7. smooth invertible frame transport preserves spectral support by the displayed typed inverse.

The remaining mass-gap task is concentrated into the continuum-limit dynamics of these exact measures: proving a strictly positive lower edge for the full reconstructed gauge-invariant observable sector and identifying this sector with the four-dimensional Yang--Mills Hilbert space required by the target theorem. This note does not assert either conclusion.


# Vacuum-aware refinement, smooth holonomy sections, and an infrared Schur budget

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md}

\textbf{SHA-256:} \path{0874d0d59e0fecec8d5fcd88b33918515e635fe22c27b3bd56ae0b3c4cb782c0}
\end{quote}


14 September 2026. Additive research continuation against Yang–Mills commit
`fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`.

This note proves five connected statements for the retained programme: smooth local sections of the complete finite-link holonomy map with their exact curvature cost; refinement in the actual interacting vacuum measure with a complete Dirichlet square identity; a projective equal-time vacuum limit; a regulator-uniform inverse-energy Schur budget; and the exact kernel comparing regulator-state sequences to the reconstructed observable space. The last construction corrects the escaping-label inference in the preceding spectral-reconstruction note. No positive continuum mass lower bound is asserted.

## 1. Source objects and conventions

[YM] is `yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`, §§1–2, at the commit above. [SR] is `yang-mills/continuations/20260914-spectral-reconstruction/RESEARCH_NOTE.md` at the same commit. [S6] is `s6/27_s6_key_advances_frozen_2026-09-06.tex`, §3, at the same commit. [SZ] is `formal/splitzero/DERIVED_MATHEMATICS.md`, §§1–4, in `KokunoYumeto/zeta-function-research-reader` at `7ea0a49945390eae14d3160a5730858899768b5f`. These source bodies were inspected. The S6 source supplies explicit formulas and locations of its longer proofs; the elementary quotient-map verification used below is written here.

Keep the original generators `T_alpha=-i sigma_alpha/2`, product Haar probability `dU_n`, and all oriented plaquette words. Fix the actual sequence

\[
a_n=a_0 2^{-n},\quad L_n=4\,2^{2n},\quad
g_n^2=(g_0^{-2}+\beta n\log 2)^{-1},\qquad a_0,g_0,\beta>0.
\tag{1.1}
\]

The displayed beta is a prescribed path parameter. On the open graph with vertices `{-L_n,...,L_n}^3`, let `Q_n=SU(2)^{E_n}` and

\[
\kappa_n=2g_n^2/a_n,\quad
H_n=-\kappa_n\sum_{e,\alpha}X_{e,\alpha}^2+
\frac1{2g_n^2a_n}\sum_p(2-\operatorname{tr}U_p),\quad
A_n=H_n-E_{0,n}I.
\tag{1.2}
\]

The positive unit vacuum `psi_n`, its exact energy `E_{0,n}`, and the invariant `H^2` and `H^1` operator/form domains are those of [YM]. Write `rho_n=psi_n^2`. Multiplication

\[
\mathscr U_n:L^2(Q_n,\rho_n dU_n)\longrightarrow L^2(Q_n,dU_n),
\qquad f\longmapsto\psi_n f
\tag{1.3}
\]

has inverse `u -> u/psi_n` and preserves the displayed inner products. Both maps preserve the physical invariant subspaces. The full ground-state identity is

\[
q_{A_n}(\mathscr U_n f)=\kappa_n\int\rho_n
\sum_{e,\alpha}|X_{e,\alpha}f|^2dU_n.
\tag{1.4}
\]

Its polarized form follows by expanding the kinetic derivatives and using the exact equation `H_n psi_n=E_{0,n} psi_n`. Every magnetic term enters that vacuum equation and the actual density `rho_n`.

## 2. Smooth extension with the complete curvature cost

### 2.1 The inspected S6 map

The source's retained data obey `gamma(Lambda) subset Z`, `gamma A=gamma`, `gamma(v)=epsilon in {1,-1}`, and `zeta=exp(-2 pi i/m)`. Set

\[
H(x)=e^{-2\pi i\epsilon\gamma(x)}.
\]

Then `H(x+lambda)=H(x)` and

\[
H(Ax+v/m)=e^{-2\pi i\epsilon(\gamma(x)+\epsilon/m)}=\zeta H(x).
\]

The retained deck actions on the total line are `(x,z) -> (x+lambda,z)` and `(x,z) -> (Ax+v/m,zeta z)`. Consequently the quotient-line maps

\[
[x,z]\longmapsto([x],z/H(x)),\qquad
([x,w])\longmapsto[x,wH(x)]
\tag{2.1}
\]

are invariant under both displayed deck generators, are smooth, and compose to the respective identities. The factor `H` remains in the inverse. The source uses `m=3,4`. The following Yang–Mills sections are constructed with their own explicit domains, inverses, and energy factors.

### 2.2 Smooth local sections at every finite-link configuration

Fix level `r` and a reference configuration `U^0 in Q_r`. For each positive edge `e=(x,x+a_r e_i)`, choose two real smooth profiles `p_0,p_1` with disjoint compact supports in `(1/4,3/8)` and `(5/8,3/4)`. Retain their actual nonzero integrals and squared integrals

\[
I_j=\int p_j(t)dt,\qquad J_j=\int p_j(t)^2dt\quad(j=0,1).
\]

Choose `chi in C_c^infty(R^2;R)` supported in the unit disk with `chi(0)=1`, and retain `J_chi=int |grad chi|^2`. Choose `0<epsilon<1/16`. The tubes of transverse radius `epsilon a_r` about these central edge segments are disjoint, including between edges in different coordinate directions.

Choose `K_e^0 in su(2)` with `exp K_e^0=U_e^0`. On the open neighborhood where the spectrum of `(U_e^0)^{-1}U_e` avoids the negative real axis, use the analytic matrix logarithm

\[
K_e(U)=\log((U_e^0)^{-1}U_e).
\]

For `x'=x+a_r t e_i+y`, `y perpendicular e_i`, define the one-form in the edge tube by

\[
\mathcal A_e(U)(x')=
\frac1{a_r}\left(\frac{p_0(t)}{I_0}K_e^0+
\frac{p_1(t)}{I_1}K_e(U)\right)
\chi\!\left(\frac{y}{\epsilon a_r}\right)dx_i,
\qquad \mathcal A(U)=\sum_e\mathcal A_e(U).
\tag{2.2}
\]

Every profile and every integral stays in (2.2). Extending each summand by zero gives a compactly supported smooth connection. It depends smoothly on `U` in the displayed neighborhood. In the original transport convention `V'=V mathcal A(dot gamma)`, the exact edge transport is

\[
\operatorname{Hol}_e(\mathcal A(U))=
\exp K_e^0\,\exp K_e(U)=U_e.
\tag{2.3}
\]

Indeed the two longitudinal supports are ordered and disjoint, and their integrals are respectively `K_e^0,K_e(U)`. The transverse cutoff equals one on the edge; every other edge misses that tube. Thus (2.2) is a smooth local right inverse of the **whole** finite-link holonomy map at every `U^0`, including reference links equal to `-I`.

All products between connection components in one tube have the same differential `dx_i`, and distinct tubes are disjoint. Therefore `mathcal A wedge mathcal A=0` for this constructed connection. The curvature in a tube is its exact transverse derivative. With the original matrix Frobenius norm,

\[
\boxed{
\int_{\mathbb R^3}\sum_{i<j}\|F_{ij}(\mathcal A(U))\|_F^2dx
=\frac{J_\chi}{a_r}\sum_{e\in E_r}
\left(\frac{J_0}{I_0^2}\|K_e^0\|_F^2+
\frac{J_1}{I_1^2}\|K_e(U)\|_F^2\right).
}
\tag{2.4}
\]

To verify the coefficient, a transverse derivative contributes `(epsilon a_r)^{-1}`, the connection contributes `a_r^{-1}`, and `dx=a_r(epsilon a_r)^2 dt dz`. Their squared factors leave `a_r^{-1}`. The disjoint longitudinal supports remove precisely the cross product of the two displayed profiles. The magnetic curvature functional retains the additional factor `1/(4g_r^2)` when (2.4) is inserted into that functional.

The maps (2.2)–(2.3) supply smooth local continuation. Equation (2.4) simultaneously retains its ultraviolet energy cost; none of its `a_r`, `g_r`, or profile factors is removed.

## 3. Refinement in the actual fine-vacuum measure

Fix `r<n` and `b=2^{n-r}`. Each coarse edge consists of `b` ordered fine links. Fine links outside those chains remain as variables. Put

\[
\pi_{r,n}(U)_e=U_{e,1}\cdots U_{e,b}.
\tag{3.1}
\]

An explicit global coordinate map is

\[
\Phi_{r,n}:Q_n\longrightarrow Q_r\times Z_{r,n},\quad
U\longmapsto(W,(U_{e,j})_{j<b},U_{\rm unused}),
\]

where `Z_{r,n}` is the product group with exactly `(b-1)|E_r|+|E_n|-b|E_r|` factors. Its inverse retains the displayed first `b-1` links and unused links and sets

\[
U_{e,b}=(U_{e,1}\cdots U_{e,b-1})^{-1}W_e.
\tag{3.2}
\]

Both compositions are identities. Haar translation in the last link on each chain proves `dU_n=dW dz` in these coordinates. Gauge equivariance is the cancellation of every intermediate vertex factor in (3.1).

Define the actual marginal and conditional map

\[
m_{r,n}(W)=\int_{Z_{r,n}}\rho_n(\Phi_{r,n}^{-1}(W,z))dz,
\]
\[
(\mathsf E f)(W)=\frac{1}{m_{r,n}(W)}
\int f(\Phi_{r,n}^{-1}(W,z))\rho_n(\Phi_{r,n}^{-1}(W,z))dz,
\quad \mathsf Jg=g\circ\pi_{r,n}.
\tag{3.3}
\]

These formulas retain the fine vacuum. The density `m=m_{r,n}` is smooth, strictly positive, gauge invariant, and has integral one. Fubini proves

\[
\mathsf J:L^2(m\,dW)\to L^2(\rho_n dU_n),\quad
\mathsf J^*\mathsf J=I,\quad\mathsf J^*=\mathsf E.
\tag{3.4}
\]

Thus `mathsf E mathsf J=I` and `mathsf P=mathsf J mathsf E` is an orthogonal projection. The maps commute with gauge averaging. Their comparison with the original coarse vacuum is also explicit: the identity-on-functions map from `L^2(rho_r dW)` to `L^2(m dW)` has squared norm pairing

\[
\langle f,g\rangle_m=\int\overline f g\frac{m}{\rho_r}\rho_r dW.
\tag{3.5}
\]

Both densities and their ratio remain recorded.

### 3.1 Exact horizontal fields and the retained density derivative

Write `P_{e,j-1}=U_{e,1}...U_{e,j-1}`, with the empty product `I`, and

\[
a_{e,j;\alpha\beta}=(\operatorname{Ad}_{P_{e,j-1}})_{\alpha\beta},\qquad
Y_{e,\alpha}=\frac1b\sum_{j=1}^b\sum_\beta
 a_{e,j;\alpha\beta}X_{e,j,\beta}.
\tag{3.6}
\]

Differentiation gives `X_{e,j,beta} mathsf Jg=sum_alpha a_{e,j;alpha beta} mathsf J X_{e,alpha}g`. Orthogonality of each adjoint matrix consequently proves

\[
Y_{e,\alpha}\mathsf Jg=\mathsf JX_{e,\alpha}g,
\qquad \langle Y_{e,\alpha},Y_{f,\gamma}\rangle
=b^{-1}\delta_{ef}\delta_{\alpha\gamma}.
\tag{3.7}
\]

The inner product in (3.7) is the generator-coordinate coefficient inner product of the original sum of squares. Each coefficient in a summand of (3.6) is independent of the differentiated link `U_{e,j}`. Each `X` has Haar divergence zero. Hence every `Y` has Haar divergence zero.

Define the actual centered density derivative

\[
S_{e,\alpha}=Y_{e,\alpha}\log\rho_n-
\mathsf J(X_{e,\alpha}\log m).
\tag{3.8}
\]

All these functions are smooth at each finite regulator. Integration by parts against a coarse smooth test function gives

\[
X_{e,\alpha}(m\mathsf E f)
=m\mathsf E(Y_{e,\alpha}f+fY_{e,\alpha}\log\rho_n).
\]

Applying this to `f=1` and then substituting back proves

\[
\boxed{\mathsf E S_{e,\alpha}=0,\qquad
X_{e,\alpha}\mathsf E f=
\mathsf E(Y_{e,\alpha}f)+\mathsf E(fS_{e,\alpha}).}
\tag{3.9}
\]

These component formulas hold on the full scalar spaces. Under gauge transformations their generator indices rotate by the endpoint adjoint matrices; the contracted expressions below preserve the physical invariant subspace.

### 3.2 The full Dirichlet square identity

For smooth physical `f`, put `g=mathsf E f`, `h=f-mathsf Jg`, and
`v_{e,alpha}=mathsf E(hS_{e,alpha})`. Then `mathsf E h=0` and (3.9) gives `mathsf E Y_{e,alpha}h=-v_{e,alpha}`.

Let `nabla_v` be the orthogonal complement of the fields in (3.7) in the original fine generator coordinates. More explicitly its chain component is

\[
(\nabla_v f)_{e,j,\beta}=X_{e,j,\beta}f-
\sum_\alpha a_{e,j;\alpha\beta}Y_{e,\alpha}f,
\tag{3.10}
\]

and its unused-edge components are the original `X f`. Squaring (3.10), using the adjoint identities, proves
`sum |Xf|^2=b sum |Yf|^2+|nabla_v f|^2` pointwise. Also `nabla_v mathsf Jg=0`. Conditional expansion of each horizontal square now proves

\[
\boxed{\begin{aligned}
q_{A_n}(\psi_n f)
={}&\kappa_n b\int m\sum_{e,\alpha}|X_{e,\alpha}g-v_{e,\alpha}|^2dW\\
&+\kappa_n b\int\rho_n\sum_{e,\alpha}
 |Y_{e,\alpha}h+\mathsf Jv_{e,\alpha}|^2dU_n\\
&+\kappa_n\int\rho_n|\nabla_vh|^2dU_n.
\end{aligned}}
\tag{3.11}
\]

The second line is exactly the conditional variance of `Yh`. The cross term retained in the expanded form is
`-2 kappa_n b Re int m sum overline{Xg} mathsf E(hS)`.
In particular the coarse cylindrical form is

\[
q_{A_n}(\psi_n\mathsf Jg)=\kappa_n b\int m\sum|Xg|^2dW,
\quad
\kappa_n b=\frac{2a_r}{a_n^2(g_0^{-2}+\beta n\log2)}.
\tag{3.12}
\]

The represented coarse operator on smooth functions is
`-kappa_n b m^{-1} sum X(m X)`; integrating by parts proves this expression directly. Equations (3.8) and (3.11) retain the entire fine-vacuum drift and the cross terms with fiber fluctuations.

There is also a completely evaluated global bound for the density derivative. Orthogonality in (3.7) and conditional variance give

\[
\int\rho_n\sum|S|^2\le\frac4b\int\sum|X\psi_n|^2
\le\frac{4E_{0,n}}{b\kappa_n}
\le\frac{2|P_n|}{b g_n^4}.
\tag{3.13}
\]

For the last step, the constant trial function has energy `|P_n|/(g_n^2 a_n)`: integrating any plaquette trace over one of its four distinct link variables gives zero. The potential is nonnegative, so the kinetic vacuum energy is at most `E_{0,n}`. The graph has `|P_n|=3(2L_n)^2(2L_n+1)`. Thus every regulator factor in this global bound is explicit.

### 3.3 Split Zero and the full hierarchy

Use the two cochain windows `0 -> H_f -> 0` and `ker mathsf E -> H_f -> 0`, with the second incoming map the actual inclusion. Here `H_f=L^2(rho_n dU_n)`, or its physical invariant subspace. The transition is the identity in the middle degree. The map

\[
H_f/\ker\mathsf E\longrightarrow H_c=L^2(m dW),
\quad[f]\longmapsto\mathsf E f
\tag{3.14}
\]

has inverse `g -> [mathsf Jg]`. Their compositions follow from `mathsf E mathsf J=I` and `f-mathsf J mathsf E f in ker mathsf E`. The transported-class kernel is exactly `ker mathsf E`; its boundary primitive is the original fluctuation `h`. Applying [SZ]'s two-support reconstruction records `(1,0)` together with that primitive. Equation (3.11) retains its full energy interaction.

For fixed `n`, the projections for all coarse levels obey `mathsf P_r mathsf P_s=mathsf P_min(r,s)`: test the conditional integrals against an arbitrary function of the coarser ordered products and use Fubini. Therefore, with `d_0=mathsf P_0 f` and `d_r=(mathsf P_r-mathsf P_{r-1})f`,

\[
f=\sum_{r=0}^n d_r,\quad
\operatorname{Var}_{\rho_n} f=\operatorname{Var}_{\rho_n}d_0+
\sum_{r=1}^n\|d_r\|_{\rho_n}^2,
\]
\[
q_{A_n}(\psi_n f)=\sum_{r,s=0}^n
\kappa_n\int\rho_n\sum_{e,\alpha}
\overline{X_{e,\alpha}d_r}X_{e,\alpha}d_s.
\tag{3.15}
\]

The first identity uses orthogonal projections. The second retains every off-diagonal energy entry.

## 4. A projective equal-time vacuum and its smooth sections

Let `nu_{r,n}=(pi_{r,n})_*(rho_n dU_n)`. At every finite `n`, the exact product law gives
`(pi_{r,s})_*nu_{s,n}=nu_{r,n}` for `r<s<=n`. Every `Q_r` is compact metric. Select a countable uniformly dense algebra of matrix-entry polynomials on each `Q_r`; diagonal subsequence selection for their bounded integrals gives one sequence `n_k` with weak limits `nu_r` for every `r`. Positivity and the bound by the uniform norm extend each limit functional to `C(Q_r)`, and its representing probability measure is `nu_r`. Testing against a continuous function proves `(pi_{r,s})_*nu_s=nu_r`.

The inverse limit

\[
\mathfrak Q=\{(W_r)_{r\ge0}:\pi_{r,r+1}W_{r+1}=W_r\}
\tag{4.1}
\]

is compact metric. Surjectivity of each (3.1) follows from (3.2). Compatible integration against `nu_r` defines a positive functional on its cylinder algebra. This algebra contains constants, is closed under conjugation, and separates points; uniform polynomial approximation and the representation of positive functionals therefore give a probability measure `nu` with all these marginals. Gauge invariance follows by change of variables at each finite level and passage to the same limits.

Smooth connections map into `mathfrak Q` by their complete ordered edge holonomies. ODE concatenation proves compatibility. This image is dense: a nonempty cylinder neighborhood is detected at some finite level `r`, and (2.2) realizes any chosen configuration at that level by a smooth compactly supported connection. For each finite level the local section and its exact curvature cost remain (2.2) and (2.4).

For any fixed cylindrical observables `O_i,O_j`, the complete equal-time Gram limit is consequently

\[
G^c_{ij}=\int\overline{O_i}O_j\,d\nu-
\overline{\int O_i d\nu}\int O_jd\nu.
\tag{4.2}
\]

The same diagonal selection can retain the positive-time correlations in [SR]. Their endpoint equation stays
`E_infty=G^c-C(0+)`. Thus the equal-time measure, the finite-energy correlations, and the exact endpoint defect have now been put on one actual refinement subsequence. No value of `E_infty` is assigned by this construction.

## 5. A regulator-uniform infrared Schur budget

Take a fixed finite list of smooth bounded physical observables. Write

\[
r_{i,n}=(O_{i,n}-\langle\psi_n,O_{i,n}\psi_n\rangle)\psi_n,
\quad R_{0,n}x=\sum_i x_i r_{i,n},\quad
K_*=\sum_i\|O_i\|_\infty^2.
\]

The exact variance identity gives `R_{0,n}^*R_{0,n} preceq K_* I`.
For a concrete six-vector frame, take the six positively oriented squares of physical side `a_0` in the `x^1,x^2` plane at `x^3=0`, with lower-left corners `a_0(-3,-3,0)`, `a_0(-1,-3,0)`, `a_0(1,-3,0)`, `a_0(-3,1,0)`, `a_0(-1,1,0)`, and `a_0(1,1,0)`. They lie in the original boxes and have disjoint edge sets; each loop uses exactly `4*2^n` fine edges. Take their complete ordered fundamental traces. Then `K_*=24`; independence follows by varying one edge in each loop while fixing all other links. Fix `tau>0`, set `R=e^{-tau A_n/2}R_{0,n}`, and use the following constructions for that six-vector frame. The heat multiplier is injective, so its raw Gram matrix `G=R^*R` is positive definite.

Set

\[
P=RG^{-1}R^*,\quad Q=I-P,\quad K=R^*A_nR,\quad
B=QA_nR,\quad D=QA_nQ\big|_{\operatorname{Dom}(A_n)\cap Q\mathcal H_n}.
\tag{5.1}
\]

`D` is self-adjoint and nonnegative. Indeed `A_nP` is bounded finite rank since the range of `R` lies in every power domain of `A_n`. Its adjoint is the bounded extension of `PA_n`. Subtracting `QA_nP+PA_nQ` from `A_n` is a bounded self-adjoint perturbation with reducing subspaces `P,Q`; its Q restriction is `D`, and its quadratic form there equals that of `A_n`.

For `s>0` define

\[
M(s)=B^*(D+s)^{-1}B,\quad F(s)=K+sG-M(s),\quad
L(s)=R-(D+s)^{-1}B,
\]
\[
d\sigma(\lambda)=B^*dE_D(\lambda)B.
\tag{5.2}
\]

Substitution gives `Q(A_n+s)L=0`. Orthogonality to the range of R proves

\[
F=L^*(A_n+s)L,\quad F'=L^*L=G+B^*(D+s)^{-2}B,
\quad R^*(A_n+s)^{-1}R=GF^{-1}G.
\tag{5.3}
\]

In particular `F>=sG`, so `M(s)<=K` for every `s>0`. This also follows directly by inserting `Rx-(D+s)^{-1}Bx` into the positive quadratic form of `A_n`; its value is `x^*[K-M(s)-sB^*(D+s)^{-2}B]x`.

Monotone convergence of the positive scalar contractions as `s downarrow0` now proves

\[
\boxed{\sigma(\{0\})=0,\qquad
M(0):=\int_{(0,\infty)}\lambda^{-1}d\sigma(\lambda)\preceq K.}
\tag{5.4}
\]

This proves inverse-energy integrability rather than imposing it. The heat multiplier maximum gives `K preceq K_* /(e tau) I`; for the six loops this is `24/(e tau) I`. It follows that

\[
\boxed{\sigma([0,\epsilon])\preceq\epsilon K
\preceq\frac{24\epsilon}{e\tau}I\quad(\epsilon>0).}
\tag{5.5}
\]

For `r>=1`, differentiation under the resolvent and (5.4) give the sharper bounds

\[
\boxed{
0\preceq(-1)^rM^{(r)}(s)
\preceq
\frac{r!r^r}{(r+1)^{r+1}s^r}K
\preceq\frac{24r!r^r}{e\tau(r+1)^{r+1}s^r}I,
\qquad 0\preceq M(s)\preceq K.
}
\tag{5.6}
\]

Indeed write `d alpha=lambda^{-1}d sigma`. The derivative integrand is `r! lambda/(lambda+s)^{r+1}`. The derivative of `lambda/(lambda+s)^{r+1}` in lambda is `(s-r lambda)/(lambda+s)^{r+2}`, so the maximum of the derivative integrand occurs at `lambda=s/r` and has precisely the displayed value. In particular

\[
\boxed{G\preceq F'(s)\preceq G+\frac{K}{4s},\qquad
sF'(s)\preceq F(s).}
\tag{5.7}
\]

The latter inequality also follows at once from (5.3) and `A_n>=0`.

### 5.1 The inverse-energy endpoint and its exact retained class

Restore the regulator suffix. Spectral calculus gives the additional bound
`B_n^*B_n preceq 4K_* /(e^2 tau^2) I`. Let
`d alpha_n=lambda^{-1}d sigma_n` on `(0,infty)`, with zero endpoint atoms initially. Its total matrix is at most `K_n`, and

\[
\alpha_n([\Lambda,\infty))\preceq
\frac{4K_*}{e^2\tau^2\Lambda}I.
\tag{5.8}
\]

Weak subsequence selection on `[0,infty]`, jointly with the previous selection, gives `alpha_n -> alpha`, `sigma_n -> sigma_infty`, `G_n -> G_infty`, `K_n -> K_infty`, and `S_n:=K_n-alpha_n([0,infty]) -> S_infty>=0`. Formula (5.8), tested with continuous tail cutoffs, proves `alpha({infty})=0`. Its possible atom at zero is retained as `Z_alpha=alpha({0})`.

For `s>0` the function `lambda/(lambda+s)`, extended by zero at zero and by one at infinity, is continuous on this compactification. Hence

\[
M_\infty(s)=\int\frac{\lambda}{\lambda+s}d\alpha(\lambda),
\qquad
\boxed{F_\infty(0+)=S_\infty+Z_\alpha.}
\tag{5.9}
\]

To prove the second equality, use `alpha(X)=lim M_n(0)`, `M_infty(0+)=alpha(X)-Z_alpha`, and `sG_n ->0` after the fixed-s regulator limit. Thus the endpoint correction is the exact difference between the two displayed zero-energy limit orders.

For clarity, the ordinary memory limit satisfies `sigma_infty({0})=0` and `int_(0,infty) lambda^{-1}d sigma_infty<=K_infty`. The first assertion follows by testing (5.5) with shrinking continuous cutoffs. On each compact finite-energy interval, `d sigma_infty=lambda d alpha`; monotone cutoff integration proves the second. The atom `Z_alpha` remains visible in (5.9).

On the vector space of finite complex measures on `[0,infty)`, the observation map

\[
\mathcal T\alpha(s)=\int\frac{\lambda}{\lambda+s}d\alpha(\lambda)
\tag{5.10}
\]

has kernel exactly `C delta_0`. Here is the converse proof. Vanishing for every `s>0` and bounded convergence as `s downarrow0` show that the restriction to `(0,infty)` has total mass zero. Then `lambda/(lambda+s)=1-s/(lambda+s)` shows that its Stieltjes transform vanishes. Differentiation at `s=1` gives all integrals `(lambda+1)^{-k}`, `k>=1`; the total mass supplies k=0. The explicit coordinate `x=(1+lambda)^{-1}`, with inverse `lambda=x^{-1}-1`, transports these to all polynomial moments on `[0,1]`. Polynomial approximation proves that the restricted measure is zero. This argument applies entry by entry.

The two-support windows `0 -> M ->0` and `C -> M ->0`, with incoming map `c -> c delta_0`, consequently have transported kernel `C delta_0`. Its actual primitive for the limit in (5.9) is each original matrix coordinate `(Z_alpha)_{ij}`. This is the inverse-energy Split Zero record.

## 6. The regulator-state comparison and the escaping-label kernel

Use one of the actual subsequences from [SR], jointly selected with §4. Let `z_{i,t,n}=e^{-tA_n}r_{i,n}` for positive rational times. The limiting symbols `z_{i,t}` span densely in the separable reconstructed space `H_obs`. Let `B_lim` be the vector space of bounded regulator-state sequences `(v_n)` for which every scalar limit
`lim <z_{i,t,n},v_n>` exists. Omit finitely many indices preceding an observable's birth. Let `N` be its subspace with `||v_n|| ->0`.

For a finite symbol sum z, define

\[
\ell_v(z)=\lim_n\langle z_n,v_n\rangle.
\]

Cauchy–Schwarz and convergence of `||z_n||` prove
`|ell_v(z)|<=limsup ||v_n|| ||z||`. Therefore the Riesz representation theorem defines an actual linear map

\[
\boxed{\mathfrak b:B_{\rm lim}\longrightarrow H_{\rm obs},\qquad
\langle z,\mathfrak b(v)\rangle=\ell_v(z),\quad
\|\mathfrak b(v)\|\le\limsup_n\|v_n\|.}
\tag{6.1}
\]

Its kernel is exactly

\[
\mathcal K=\{v:\lim_n\langle z_{i,t,n},v_n\rangle=0
\text{ for every fixed }i,t\}.
\tag{6.2}
\]

The map is onto. To prove this, approximate any `w in H_obs` by finite symbol sums `w_j` with error at most `2^{-j}`. Enumerate the rational-time test symbols. Choose increasing regulator thresholds `N_j` after all births in `w_j` so that, for all later regulators, the squared norm of its regulator counterpart differs from `||w_j||^2` by at most `2^{-j}`, and its first j test pairings differ from the limiting pairings by at most `2^{-j}`. Set `v_n` equal to the counterpart of `w_j` for `N_j<=n<N_{j+1}`, and zero before `N_1`. This sequence is bounded, has every test-pairing limit equal to that of w, and satisfies `||v_n|| -> ||w||`. Hence `mathfrak b(v)=w`.

The exact cochain comparison is

\[
C_0:\quad\mathcal N\hookrightarrow B_{\rm lim}\longrightarrow0,
\qquad C_1:\quad\mathcal K\hookrightarrow B_{\rm lim}\longrightarrow0.
\]

Use inclusion in degree zero and identity in degree one. Then

\[
\boxed{
H^1(C_0)=B_{\rm lim}/\mathcal N,
\quad H^1(C_1)\xrightarrow{\cong}H_{\rm obs},\ [v]\mapsto\mathfrak b(v),
\quad\ker H^1(C_0\to C_1)=\mathcal K/\mathcal N.
}
\tag{6.3}
\]

The inverse is the class of any lift constructed above; two lifts differ by an element of `mathcal K`, which proves independence. The norm bound in (6.1) proves `N subset K`. This is a full typed comparison from regulator sequences, including its retained source relations, rather than an inference from density at each separate regulator.

### 6.1 An exact commuting-observable test of escaping labels

Define a finite test system `Omega_n={-1,1}^n` with its original product probability `2^{-n}`. Let `F_j` flip coordinate j and put

\[
A_n^{\rm test}=\sum_{j=1}^n\frac{c_{j,n}}2(I-F_j),\qquad
c_{j,n}=1\ (j<n),\quad c_{n,n}=1/n.
\tag{6.4}
\]

Constants are the unique vacuum. The ordered refinement map forgets the last coordinate, and its pullback preserves these product inner products. Multiplication by the Walsh functions
`chi_S(omega)=prod_(j in S) omega_j`, for fixed finite nonempty S, is a bounded commuting observable of norm one. The exact identities are

\[
\langle\chi_S,\chi_T\rangle=\delta_{ST},\qquad
A_n^{\rm test}\chi_S=\left(|S\setminus\{n\}|+
\frac{\mathbf1_{n\in S}}n\right)\chi_S.
\tag{6.5}
\]

The character basis spans the full space at each finite n. For every fixed S, its energy equals `|S|` at every `n>max S`; all fixed-label limiting correlations are consequently
`delta_ST exp(-t |S|)`. The reconstructed centered generator has spectral bottom one. The actual regulator states

\[
v_n=\chi_{\{n\}},\quad \|v_n\|=1,\quad
\langle v_n,A_n^{\rm test}v_n\rangle=1/n,
\quad \mathfrak b(v)=0
\tag{6.6}
\]

satisfy the last equality because every fixed-label pairing is eventually zero. Thus their class is an explicitly nonzero element of `mathcal K/N`, with its complete energy sequence retained. Equations (6.4)–(6.6) are algebraic test data; they assign no numerical value to a Yang–Mills gap.

In [SR] §5 replace the sentence beginning “A sequence of low-energy states approaching zero is therefore recorded” by the exact statement: “The spectral-support and large-time formulas determine the reconstructed fixed-label observable sector. The regulator-state comparison has the retained kernel `K/N` constructed in the vacuum-refinement continuation, §6; equation (6.6) computes an escaping-label class together with its norm and energy sequence.” The previous spectral-support and Laplace-principle formulas remain as written.

Two further notation corrections are recorded for [SR]: in §1 use
`||A_n^q exp(-tA_n)||=sup_(lambda in sigma(A_n)) lambda^q exp(-t lambda) <= sup_(lambda>=0) lambda^q exp(-t lambda)`; and in §4 define the matrix imaginary part as `(R(z)-R(z)^*)/(2i)`. The latter retains complex off-diagonal spectral entries in the stated polarization argument.

## 7. Verification and mathematical scope

`verify.py` checks exact rational SU(2) chain and adjoint identities, the raw nonorthogonal Schur formulas and inverse-energy budget on declared finite fixtures, the derivative constants, a conditional-density square calculation, and the full Walsh escaping-label calculation. Its finite fixtures check specified algebraic identities. The measure, domain, smooth-section, and limit statements are proved in the text above; they are not claimed as outputs of those finite tests.

This continuation supplies explicit smooth extensions with an energy cost, an actual vacuum-marginal refinement hierarchy with all cross terms, a projective equal-time limit, uniform infrared memory bounds, and the complete regulator-state comparison kernel. The quantities `rho_n`, the zero-energy inverse-memory matrix `Z_alpha`, and the interacting low-energy state content of `K/N` have not been numerically determined here. A nontrivial four-dimensional continuum Yang–Mills field and a positive physical continuum mass lower bound have not been established by this contribution.


# Actual Wilson-loop response moments from the full interacting vacuum

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-actual-loop-moments/RESEARCH_NOTE.md}

\textbf{SHA-256:} \path{0ac4afbec39b2e878d5555af85a86803d9ba6ac5505dc7817f231e5533c0dd2b}
\end{quote}


15 September 2026. Additive continuation of the SU(2) Yang–Mills workbench,
parent `e98b2c3af77f66fb1c1396143ca53daef586404f` (PR6).

This contribution evaluates response quantities of the original interacting
vacuum with finite errors independent of the exterior box. It proves
all-coupling pointwise logarithmic-derivative and response-moment bounds;
a gauge-covariant inverse estimate with a regulator-independent coefficient
and its full physical kappa dependence; an exact
local SU(2) calculation of three response-moment coefficients; and finite
intervals for the actual response and restored metric. The narrow intervals
are on the explicitly stated small-xi domain. The simultaneous continuum
path remains explicit in section 11. A positive physical continuum gap and a
nontrivial four-dimensional continuum field have not been established here.

The executable checks actual quaternion polynomial identities, local lattice
incidence, Haar integrals, and rational endpoints for the proved error bounds.
It does not numerically solve for the vacuum or formally verify the analytic
proofs. No general historical-priority claim is made.

## 1. Original operator, coordinates, and derivative identities

Use the original open graph with vertices `{-L,...,L}^3`, integer `L>=2`,
all contained positive edges, and every contained elementary face. Physical
spacing `a>0` and coupling `g>0` remain. Write

\[
 T_\alpha=-i\sigma_\alpha/2,\quad
 X_{e,\alpha}f(U)=\left.\frac d{dt}f(\ldots,e^{tT_\alpha}U_e,\ldots)\right|_{0},
 \quad K=-\sum_{e,\alpha}X_{e,\alpha}^2,
\]
\[
 \kappa=\frac{2g^2}{a},\qquad v=\frac1{2g^2a},\qquad
 \xi=\frac v\kappa=\frac1{4g^4},\qquad
 V=v\sum_p(2-W_p),\qquad H=\kappa K+V.                 \tag{A1}
\]
Here `W_p` is the trace of its complete oriented four-link word. The scalar
`2v|P|` is present. The original generator metric has
`c(T_alpha,T_beta)=delta_alpha,beta/4`; thus `Delta^c=4 sum X^2`, exactly as
in the primary source. Every formula below uses the original `X` and `kappa`.

The primary source [YM] proves that the full scalar compact-group operator
has a smooth positive unit ground vector `psi`, unique and gauge invariant,
with ground energy `E0`. Its operator domain is `H^2`, form domain `H^1`;
physical spaces are their gauge-invariant parts. Set

\[
 u=\log\psi,\quad \rho=\psi^2,\quad b_{e,\alpha}=X_{e,\alpha}u,
 \quad \Delta=\sum X^2,\quad
 \mathscr L=\Delta+2\sum b_{e,\alpha}X_{e,\alpha}.
\]
Multiplication `f -> psi f` is a unitary from `L^2(rho dU)` to the original
Haar Hilbert space, with inverse `F -> F/psi`. Direct differentiation gives

\[
 \Delta u+\sum b_{e,\alpha}^2=V/\kappa-E_0/\kappa,
 \qquad \mathcal A:=\psi^{-1}(H-E_0)\psi=-\kappa\mathscr L,
\]
\[
 \langle f,\mathcal A h\rangle_\rho
 =\kappa\int\rho\sum\overline{Xf}Xh.                 \tag{A2}
\]
The displayed energy offset is retained in the first equation; the derivative
of that scalar is zero in the next calculation.

Our fields have bracket
`[X_e,alpha,X_e,beta]=-epsilon_alpha,beta,gamma X_e,gamma`.
This sign follows by differentiating `U -> T_alpha U` twice. The Casimir
commutes with every `X_e,alpha`. Also
`X_e,alpha(sum_i b_i^2)=2 sum_i b_i X_i b_e,alpha`: the commutator correction
is a contraction of an antisymmetric epsilon tensor with `b_i b_j` and is
zero. Differentiating the first equation in A2 consequently proves

\[
 \boxed{\mathscr L b_{e,\alpha}=\kappa^{-1}X_{e,\alpha}V,
 \qquad \mathcal A b_{e,\alpha}=-X_{e,\alpha}V.}       \tag{A3}
\]
This is an equality of the actual smooth functions on the complete graph.
Its components may be gauge covariant; A2 and A3 also hold on the full scalar
space before restriction to the physical subspace.

For a single loop trace `F=tr U_C` in which each edge occurs once, Pauli
multiplication gives, at every link in its word,

\[
 \sum_\alpha|X_{e,\alpha}F|^2=1-F^2/4\le1,
 \quad \|[X_{f,\beta}X_{e,\alpha}F]_{\beta,\alpha}\|_{op}\le\tfrac12,
\]
\[
 \sum_{\alpha,\beta}|X_{f,\beta}X_{e,\alpha}F|^2
 =\tfrac12+F^2/16\le\tfrac34.                        \tag{A4}
\]
The last two formulas concern edges in the word. To verify them, move each
inserted generator to a common end of the word by conjugation, retaining its
orthogonal adjoint matrix. In coordinates `Q=q0 I-i sum q_alpha sigma_alpha`,
`sum q_i^2=1`, one has `tr(T_alpha Q)=-q_alpha` and
`tr(T_alpha T_beta Q)=-(delta_alpha,beta q0+epsilon_alpha,beta,gamma q_gamma)/2`.
For the three by three matrix M in the last trace formula, multiplication
gives `M^T M=(I_3-q_vec q_vec^T)/4`; its positive outer-product deficit
proves the operator bound. Summing its diagonal gives the Frobenius identity.
Inversely traversed links use
`d(U^{-1})=-U^{-1}(dU)U^{-1}` and the same adjoint rotations. No edge is
replaced by an independent inverse variable: the coordinate map `U -> U^{-1}`
is its own Haar-preserving inverse and intertwines the Casimir sum.

## 2. All-coupling pointwise vacuum control

Let `r_e` count the original faces incident on edge e, so `r_e<=4`.
For the three by three matrix `B_beta,alpha=X_e,beta X_e,alpha u`, its
antisymmetric part has squared Frobenius norm

\[
 \sum_{\alpha,\beta}|(B_{\beta\alpha}-B_{\alpha\beta})/2|^2
 =\tfrac12\sum_\alpha|b_{e,\alpha}|^2.
\]
Therefore `sum_(i,alpha)|X_i b_e,alpha|^2 >= |b_e|^2/2` pointwise.
At a maximum of `w_e=sum_alpha b_e,alpha^2` on the compact product group,
A3 and the product rule imply

\[
 0\ge\tfrac12\mathscr L w_e
 =\sum_{i,\alpha}|X_i b_{e,\alpha}|^2
  +\kappa^{-1}\sum_\alpha b_{e,\alpha}X_{e,\alpha}V
 \ge\tfrac12 w_e-r_e\xi\sqrt{w_e}.
\]
We used `|X_e V|<=v r_e`, proved from A4. The quadratic inequality at the
maximum proves

\[
 \boxed{\sup_U|X_e\log\psi|\le2r_e\xi\le8\xi,
 \qquad \sup_U|X_e\log\rho|\le4r_e\xi\le16\xi.}     \tag{A5}
\]
There is no exterior-volume constant, and A5 holds at every positive coupling.

Integrating A3 against `rho b_e,alpha`, followed by Haar integration by parts,
also gives an exact differentiated-vacuum sum rule:

\[
 \boxed{\int\rho\sum_{i,\alpha}|X_i b_{e,\alpha}|^2
 =\frac1{2\kappa}\langle\Delta_e V\rangle_\rho
 =\frac{3\xi}{8}\left\langle\sum_{p\ni e}W_p\right\rangle_\rho
 \le\frac{3r_e\xi}{4}.}                              \tag{A6}
\]
All derivative indices i in A6 range over the full graph. The identity uses
`Delta_e W_p=-3W_p/4`. The primary local exterior-operator comparison further
supplies

\[
 \gamma_e:=\int\rho|b_e|^2\le2r_e\xi\le8\xi.         \tag{A7}
\]
For completeness, write
`H-E0=kappa E_e+K_e-v sum_(p containing e) W_p`, where `K_e>=0` acts on
exterior links. This follows by testing H on the constant in e times an
exterior ground vector; each incident trace has zero Haar integral in e.
Taking the vacuum expectation gives A7. Every exterior term stays in K_e.

## 3. A gauge-covariant inverse and a quantitative local drift expansion

### 3.1 The inverse is proved on its exact source sector

At vertex v let `G_v,alpha` be the infinitesimal vertex gauge action. It is
the sum of outgoing left generators and incoming negative right generators.
Right generators are related to the displayed left generators by the actual
adjoint matrices of their links. If `d_v` is the vertex degree, pointwise
Cauchy–Schwarz gives

\[
 \sum_\alpha|G_{v,\alpha}h|^2
 \le d_v\sum_{e\ni v,\alpha}|X_{e,\alpha}h|^2,
 \qquad d_v\le6.                                    \tag{A8}
\]
The difference of the two sides of the vector inequality
`d_v sum|z_e|^2-|sum z_e|^2` is exactly `sum_(e<f)|z_e-z_f|^2`.

Use the spin-one gauge-Casimir subspace
`E_v={h: -sum_alpha G_v,alpha^2 h=2h}`, with its closed Hilbert realization
from the compact unitary gauge action on `L^2(rho dU)`. Haar averaging in the
vertex gauge variable supplies this closed sector; equivalently it is the
range of `3 int chi_1(g) U_v(g) dg`, where
`chi_1(g)=(tr g)^2-1`. Matrix-coefficient orthogonality proves the projection
formula. The original H and rho commute with this action, so A reduces E_v.
Integration by parts in the gauge variable and A8 give

\[
 q_{\mathcal A}(h)\ge\frac{2\kappa}{d_v}\|h\|_\rho^2
 \ge\frac\kappa3\|h\|_\rho^2\quad(h\in E_v),
\]
\[
 \boxed{\| (\mathcal A|_{E_v}+s)^{-1}\|
 \le\frac1{s+2\kappa/d_v}\le\frac1{s+\kappa/3},
 \qquad s\ge0.}                                      \tag{A9}
\]
The form inequality extends from smooth vectors by closure. Self-adjointness
then gives the inverse on exactly this sector.

For an edge e starting at v, the vector `b_e` transforms by the adjoint
three-dimensional representation at v. Indeed `G_v u=0`, and commuting G_v
with X_e gives `G_v,alpha b_e,beta=-epsilon_alpha,beta,gamma b_e,gamma`.
The other vertex gauge generators commute with this derivative. Thus each
component of b_e is in E_v; contracting twice with epsilon gives its Casimir
2. This proves that A9 applies to the actual derivative in A3.

The physical contraction in a Wilson-loop forcing is the map
`(h_alpha,c_alpha) -> sum_alpha h_alpha c_alpha`. Both factors transform
by the same orthogonal adjoint matrix at the edge source, so this product
is invariant there. Its derivative is the full product rule
`X_i sum h_alpha c_alpha=sum [(X_i h_alpha)c_alpha+h_alpha(X_i c_alpha)]`.
The cross terms in its energy are retained below. A9 is used on its specified
covariant sources through this map, rather than assigned to the invariant
contraction without its energy calculation.

### 3.2 First local drift and its remainder

Set

\[
 u_0=\frac\xi3\sum_p W_p,\qquad b_e^0=X_eu_0,
 \qquad \mathfrak r_e=X_e(u-u_0).                              \tag{A10}
\]
The scalar E0 is still in A2. The derivative formula here follows because
`Delta u0=-xi sum_p W_p`, so `Delta b_e^0=kappa^{-1}X_e V`.
Consequently

\[
 \mathscr L \mathfrak r_{e,\alpha}
 =-2\sum_i b_i X_i b^0_{e,\alpha}.                   \tag{A11}
\]
Each block `J^0_ef=[X_f,beta b^0_e,alpha]` satisfies, by A4,

\[
 \sum_f\|J^0_{ef}\|_{op}\le\frac{2r_e\xi}{3}\le\frac{8\xi}{3},
 \quad |b_e^0|\le\frac{4\xi}{3},
 \quad |\mathcal A \mathfrak r_e|\le\frac{128\kappa\xi^2}{3}.  \tag{A12}
\]
In the first sum only edges sharing a plaquette with e occur. Each such
plaquette has four original edges and contributes at most `xi/(3*2)` per
block; multiplicities are counted.

The residual vectors in A10 have the same spin-one covariance as b_e.
A9 and A12 give,
at **every** xi>0,

\[
 \boxed{\|\mathfrak r_e\|_{L^2(\rho;\mathbb R^3)}\le128\xi^2,
 \qquad \sum_\alpha\|\nabla \mathfrak r_{e,\alpha}\|_\rho^2
 \le\frac{16384}{3}\xi^4.}                          \tag{A13}
\]
The second inequality is A2 paired with the residual vector and A12, using the first.

On the stated range `0<xi<=3/64`, the pointwise constant is sharper. Take a
maximum over all edges and configurations of `|r_e^rem|=R`. The antisymmetric
second-derivative calculation in section 2 applies to `X_e(u-u0)` too.
At that maximum A11 and A12 give

\[
 (\tfrac12-\tfrac{16\xi}{3})R^2
 \le\tfrac{64\xi^2}{9}R.
\]
The coefficient on the left is at least 1/4. Hence, putting `A_*=256/9`,

\[
 \boxed{|\mathfrak r_e|\le A_*\xi^2,\quad
 \sum_\alpha\|\nabla \mathfrak r_{e,\alpha}\|_\rho^2
 \le\frac{128A_*}{3}\xi^4,
 \quad \|\mathcal A \mathfrak r_e\|_\infty\le\frac{128\kappa}{3}\xi^2.} \tag{A14}
\]
The middle inequality follows by pairing A11 with the residual vector and using the row
bound and A5; it sums derivatives over every fine link. This is a proved
remainder bound on the full interacting vacuum, not a formal series premise.

## 4. The loop observation and its exact relation to the earlier refinement

Let C be an axis-aligned square of side b lattice edges in the x1,x2 plane,
with a one-plaquette collar inside the box. Set `ell=4b`, and let
`Omega=U_C` be its ordered group holonomy, including every inverse traversal.
For b=1 one may take the face with base (0,0,0), directions (1,2); L>=2
contains its collar. Denote `F=tr Omega`.

In oriented link variables V_j along C, the map

\[
 (V_1,\ldots,V_\ell,U_{C^c})
 \mapsto(\Omega=V_1\cdots V_\ell,V_1,\ldots,V_{\ell-1},U_{C^c}) \tag{A15}
\]
has inverse `V_ell=(V_1...V_(ell-1))^{-1}Omega`. Product Haar is exactly
`dOmega dz`, by translation in the last link. Inverse traversals are carried
by the explicit involution in A4. Let

\[
 m(\Omega)=\int\rho(\Omega,z)dz,\quad
 \mathsf Eh=m^{-1}\int\rho h\,dz,\quad
 \mathsf Jf=f(\Omega),\quad P=\mathsf J\mathsf E,\quad Q=I-P. \tag{A16}
\]
Fubini gives `EJ=I`, `E=J*` in the actual rho and m pairings. These maps
intertwine the original gauge action with conjugation at the loop base.
Their physical subspaces therefore use the actual conjugation-invariant
functions on the observed SU(2) variable.

For the earlier full coarse-edge observation pi_all, a square born on that
coarse grid has `pi_C=chi_C pi_all`, where chi_C is the same four-coarse-edge
word. On the same fine vacuum the conditional expectations obey
`E_C=E_chi E_all`, by testing both sides against functions of Omega. Hence
`P_C<=P_all`. Their kernel comparison is the actual isomorphism

\[
 \ker E_C/\ker E_{all}\longrightarrow\ker E_\chi,
 \quad[h]\mapsto E_{all}h,
 \qquad k\mapsto[J_{all}k].                           \tag{A17}
\]
Both compositions follow from `E_all J_all=I` and
`h-J_all E_all h in ker E_all`. In particular the new observation retains
the additional coarse kernel in A17. Its forcing decomposes orthogonally as
`-Q_C A F=-Q_all A F-(P_all-P_C)A F`. Thus its zeroth forcing norm is the
sum of the two original squared norms. Higher energy entries use the full
coupled form, as in the parent's minimum-section composition. They are not
silently assigned to the old, smaller kernel.

The original horizontal fields now average all ell original links:
`Y_alpha=ell^{-1}sum_(j,beta)(Ad prefix_(j-1))_(alpha,beta)X_(j,beta)`.
They satisfy `Y_alpha J=J X_alpha` and
`sum_alpha|Y_alpha h|^2<=ell^{-1}sum_(j,beta)|X_(j,beta)h|^2`.
Each coefficient is independent of its differentiated link, giving Haar
divergence zero. Set

\[
 S_\alpha=Y_\alpha\log\rho-\mathsf J X_\alpha\log m,
 \quad (Th)_\alpha=\mathsf E(hS_\alpha),
 \quad \Gamma_{\alpha\beta}=\mathsf E(S_\alpha S_\beta).
\]
Integration by parts gives `ES=0`, `X Eh=E(Yh)+E(hS)` and
`T* z=sum S_alpha J z_alpha`. A5 gives `|Y log rho|<=16xi`, and thus

\[
 \boxed{\Gamma\preceq256\xi^2 I_3,\quad
 \|T\|\le16\xi,\quad
 \|X\mathsf Eh\|_m\le\ell^{-1/2}\|\nabla h\|_\rho+16\xi\|h\|_\rho.} \tag{A18}
\]
For Gamma the exact covariance is
`E[(Y log rho)(Y log rho)^T]-(E Y log rho)(E Y log rho)^T`.
The second term is retained in the equality and bounded by positivity.

Let D represent the restriction of the form A2 to `H^1_phys intersect ker E`.
At each finite regulator, E and J preserve H^1 by A18 and their finite smooth
coordinate formulas. Smooth kernel functions are dense, the restricted form
is closed, and D is nonnegative self-adjoint. On smooth physical kernel
functions `Dh=Q A h`. These facts also follow by the parent's same closed-form
argument after A15. All functions below are smooth, so every used power of D
has its stated domain. The off-diagonal action is

\[
 Q\mathcal A\mathsf Jg=-\kappa\ell T^*Xg.             \tag{A19}
\]
It follows by pairing A2 against a kernel function and using A18.

Define the ACTUAL scalar forcing and its three moments by

\[
 j=\sum_{e\in C,\alpha}b_{e,\alpha}X_{e,\alpha}F,
 \quad W=2\kappa Qj=-Q\mathcal AF,
\]
\[
 \boxed{N_0=\|W\|_\rho^2,\quad
 N_1=\langle W,DW\rangle_\rho,\quad N_2=\|DW\|_\rho^2.} \tag{A20}
\]
Indeed `KF=(3ell/4)F`, so the Casimir term is killed by Q and A20 follows
from A2. The actual response is `M(s)=<W,(D+s)^{-1}W>_rho`.

## 5. Actual moment bounds at every positive coupling

Set

\[
 J_\ell(\xi)=\min(8\ell\xi,\sqrt8\,\ell\sqrt\xi),
\]
\[
 \begin{split}
 P_\ell(\xi)={}&3\ell^{3/2}\sqrt\xi+(4\ell+6\ell^2)\xi
 +16\sqrt3\ell^{3/2}\xi^{3/2}\\
 &+128\sqrt3\ell^2\xi^2+2048\ell^2\xi^3.
 \end{split}
\]
Then the original interacting moments satisfy

\[
 \boxed{0\le N_0\le4\kappa^2J_\ell(\xi)^2,\quad
 0\le N_1\le4\kappa^3J_\ell(\xi)P_\ell(\xi),\quad
 0\le N_2\le4\kappa^4P_\ell(\xi)^2.}                \tag{A21}
\]
Here ell, kappa, and xi retain their values; the exterior box is arbitrary.

Proof: A4, A5 and A7 give `||j||<=J_ell`. For `c_e,alpha=X_e,alpha F`,
A4 gives `||c||_infty<=sqrt(ell)` and
`||grad c||_infty,HS<=sqrt(3)ell/2`. A6, summed over e in C, gives
`sum_(e,alpha)||grad b_e,alpha||^2<=3ell xi`. The product rule therefore gives

\[
 \|\nabla j\|_\rho\le\sqrt3\ell\sqrt\xi
                      +4\sqrt3\ell^{3/2}\xi.          \tag{A22}
\]
A3 and `Kc=(3ell/4)c` give, keeping all three product-rule terms,

\[
 \mathcal A j=\sum c_i\mathcal A b_i
              +\sum b_i\mathcal A c_i
              -2\kappa\sum_{i,k}(X_kb_i)(X_kc_i),
\]
\[
 \|\mathcal Aj\|_\rho
 \le\kappa\{(4\ell+6\ell^2)\xi
       +64\sqrt3\ell^2\xi^2+3\ell^{3/2}\sqrt\xi\}.   \tag{A23}
\]
The respective bounds use `|X_e V|<=4kappa xi`, A5, and A6. A18 and A22 give
`||X E j||<=sqrt(3ell)sqrt(xi)+4sqrt(3)ell xi+128ell xi^2`.
Finally A19 gives
`DW=2kappa[Q A j+kappa ell T* X E j]`. Substitution proves
`||DW||<=2kappa^2 P_ell`, and Cauchy–Schwarz proves all three inequalities
in A21. No pointwise-to-integrated replacement is used.

## 6. Local density comparison, including the conditional fiber

Let S be any finite edge set containing C and the local polynomials under
consideration; write d=|S|. A5 and the original group diameter `2pi` in the
X-generator coordinates show that changing S while fixing its exterior
changes `log rho` by at most `32pi d xi`. After integrating the exterior,
the exact Haar marginal density rho_S consequently satisfies

\[
 e^{-32\pi d\xi}\le\rho_S\le e^{32\pi d\xi}.          \tag{A24}
\]
To prove the bounds from the oscillation, note that its Haar integral is one:
its minimum is at most one, its maximum at least one, and their ratio is
at most the displayed exponential. This uses the existing Haar probability
mass, without changing the physical state.

At fixed Omega in A15, varying a first-chain link also changes the final
chain link by left and right translations. Each such pair has total path
length at most `4pi`; every other S link has path length at most `2pi`.
Thus the conditional local density relative to its original Haar fiber has
ratio bounded by `exp(32pi(d+ell-2)xi)`. Put

\[
 \delta=e^{32\pi d\xi}-1,\qquad
 \eta=e^{32\pi(d+\ell-2)\xi}-1.                     \tag{A25}
\]
For a local polynomial P whose conditional Haar average E_H P is zero,

\[
 \|\mathsf EP\|_\infty\le\eta\|P\|_\infty,
 \quad
 \|X\mathsf EP\|_m
 \le\eta\ell^{-1/2}\|\nabla P\|_\infty+16\xi\|P\|_\infty. \tag{A26}
\]
For the second formula `E_H YP=X E_H P=0` follows from A18 with constant
density; apply the conditional density comparison to YP, then A18 to the
score term. For arbitrary local P,Q, A24 also gives
`|<P,Q>_rho-<P,Q>_H|<=delta ||P||_H ||Q||_H`.

## 7. Exact original neighboring-plaquette calculation

Let p range over elementary faces meeting C, excluding p=C when b=1. Define

\[
 J_p=\sum_{e\in C\cap\partial p,\alpha}(X_{e,\alpha}W_p)(X_{e,\alpha}F),
 \quad J=\sum_pJ_p,\quad s_p=|C\cap\partial p|.        \tag{A27}
\]
For b=1 there are twelve faces, all s_p=1. Four are coplanar with bases
`(-1,0,0),(1,0,0),(0,-1,0),(0,1,0)` and directions (1,2); four have directions
(1,3) with x1=0, x2 in {0,1}, x3 in {-1,0}; four have directions (2,3) with
x1 in {0,1}, x2=0, x3 in {-1,0}. Their union with C has 12 direction-1,
12 direction-2 and 8 direction-3 edges: d=32.
For b>=2 the four inner corner faces have s_p=2 and every other meeting face
has s_p=1. Counting four incidences per C edge gives `4ell-8` faces of type
1 and four of type 2. These statements use the actual contained face words.
An exterior-independent support bound is `d<=13ell`. Here is also the exact
count. Vertical edges have their horizontal coordinates on the square's ell
vertices and their z base in {-1,0}, giving 2ell edges. Direction-1 edges at
z=+1 or -1 lie on the two horizontal sides, giving 4b edges in total. At z=0
their (x,y) bases form the union

    {0,...,b-1} x {-1,0,1,b-1,b,b+1}
      union {-1,0,b-1,b} x {0,...,b}.

For b>=3 its count is 6b+4(b+1)-8=10b-4. At b=2 its count is
10+12-6=16, the same formula. At b=1 it is 4+6-2=8.
Direction-2 edges have the transposed count. Hence d=32 at b=1 and
`d=2(14b-4)+8b=36b-8=9ell-8` at every b>=2. All these edge sets
come from the displayed original adjacent faces; the weaker bound suffices
for the general error estimates.

Each overlap is a connected path. Orient p to traverse this common path in
the same direction as C; `tr U_p^{-1}=tr U_p` proves equality of the original
trace functions under that operation. Let U be the common path product, A
and B the two remaining products, so `F=tr(UA)`, `W_p=tr(UB)`. The product
Haar pushforward to U,A,B is independent Haar, proved by repeated translations
in disjoint link sets. Every shared-edge contraction equals

\[
 j_p=\sum_\alpha\operatorname{tr}(T_\alpha UA)
                         \operatorname{tr}(T_\alpha UB)
 =-\tfrac14\operatorname{tr}(UAUB)+\tfrac14\operatorname{tr}(AB^{-1}),
 \qquad J_p=s_pj_p.                                  \tag{A28}
\]
The equality follows from Pauli multiplication (Fierz) and
`tr X tr Y=tr(XY)+tr(XY^{-1})`, verified in the same quaternion coordinates.
Integration of U yields

\[
 j_p^{(0)}=\tfrac38\operatorname{tr}(AB^{-1}),\quad
 j_p^{(1)}=j_p-j_p^{(0)},\quad
 \|j_p^{(0)}\|_H^2=\tfrac9{64},\quad
 \|j_p^{(1)}\|_H^2=\tfrac3{64},\quad
 \langle j_p^{(0)},j_p^{(1)}\rangle_H=0.              \tag{A29}
\]
For a direct check, `int tr(UAUB)dU=-tr(AB^{-1})/2`. Integrating B in
`j_p^2` first gives `(1/4)sum_alpha|X_alpha tr(UA)|^2`, whose mean is 3/16.
The first norm in A29 is `9/64` because the remaining trace has Haar square
mean one; subtracting it from 3/16 gives the second.

Every unshared edge occurs once in a fundamental representation, contributing
3/4 to K. The shared U-singlet has Casimir zero and the shared triplet has
Casimir 2 on each of its s_p original links. Equivalently direct Pauli
second differentiation gives K_U j_p^(0)=0 and K_U j_p^(1)=2j_p^(1), and
ordered product pullback supplies the factor s_p. Thus, with

\[
 \nu_p=\tfrac34(\ell+4-2s_p),
 \qquad Kj_p^{(0)}=\nu_pj_p^{(0)},\quad
 Kj_p^{(1)}=(\nu_p+2s_p)j_p^{(1)}.                   \tag{A30}
\]
For distinct p,q there is an edge in `partial p \ (C union partial q)`:
p has at least two exterior edges and distinct elementary faces share at
most one edge. Central sign change at that edge makes every cross product
between their components and their K iterates integrate to zero. This proves
all cross-face Haar cancellations with their actual unmatched-edge witnesses.

Also `E_H J=E_H KJ=0`, by integration in an exterior edge of each face.
A4 and the product rule give the following local suprema, with
`S1=sum_p s_p`, `S2=sum_p s_p^2`:

\[
 \|J\|_\infty\le S_1,\quad
 \sum_e\|X_eJ\|_\infty\le L_J:=\tfrac{\ell+4}{2}S_1,
 \quad \|KJ\|_\infty\le K_J:=(3+3\ell/4)S_1+\tfrac32S_2. \tag{A31}
\]
For the last inequality, apply K to each original product in A27. The two
Casimirs give `(3+3ell/4)J_p`; the mixed second derivatives are at most
`2*(3/4)s_p^2` by A4. For the first derivative, each pair of shared-edge
factors contributes at most 1/2 at each of its four plus ell differentiated
edges. For b=1, `(S1,S2,LJ,KJ)=(12,12,48,90)`.

Define w and z1 (the latter is an energy vector, not a spectral parameter) by

\[
 w=\tfrac{2\kappa\xi}{3}J,\qquad
 z_1=\tfrac{2\kappa^2\xi}{3}KJ.
\]
Equations A29–30 prove the exact coefficients

\[
 \|w\|_H^2=\kappa^2\xi^2 c_0,\quad
 \langle w,z_1\rangle_H=\kappa^3\xi^2 c_1,\quad
 \|z_1\|_H^2=\kappa^4\xi^2 c_2,
\]
\[
 c_j=\sum_p\frac{s_p^2}{48}
            \{3\nu_p^j+(\nu_p+2s_p)^j\},\quad j=0,1,2. \tag{A32}
\]
For an elementary loop these are `(1,5,103/4)`. For b>=2 they are

\[
 \boxed{c_0=\frac{\ell+2}{3},\quad
 c_1=\frac{\ell(3\ell+14)}{12},\quad
 c_2=\frac{9\ell^3+66\ell^2+76\ell+104}{48}.}        \tag{A33}
\]
These coefficients have now been evaluated; the return to the interacting
vacuum and its conditional D is the next, quantitative step.

## 8. Full finite remainders for the interacting moments

Use `0<xi<=3/64` and `A_*=256/9`. Write
`d_j=sum_(e in C,alpha)r^rem_e,alpha X_e,alpha F`. Then

\[
 j=\frac\xi3 J+d_j+\frac\xi3(4-F^2)\,\mathbf1_{b=1},
 \quad \|d_j\|_\rho\le\ell A_*\xi^2.               \tag{A34}
\]
The last term is an actual function of Omega and is killed exactly by Q.
Let `t=(xi/3)J+d_j`, so `W=2kappa Qt`.

For complete finite constants put

\[
 B_d=\ell\sqrt{128A_*/3}+\frac{\sqrt3}{2}\ell^{3/2}A_*,
\]
\[
 C_d(\xi)=\frac{128\ell}{3}+\frac{3\ell^2A_*}{4}
              +8\sqrt3\ell^2A_*\xi
              +\sqrt{128}\ell^{3/2}\sqrt{A_*}.
\]
A4 and A14, applied to the full product rule, give

\[
 \|\nabla d_j\|_\rho\le B_d\xi^2,
 \qquad \|\mathcal A d_j\|_\rho\le\kappa C_d(\xi)\xi^2. \tag{A35}
\]
For explicit verification, the derivative terms are bounded by
`ell sqrt(128A_*/3)xi^2` and `(sqrt(3)/2)ell^(3/2)A_*xi^2`.
In A d_j the terms `c A r`, `r kappa(3ell/4)c`,
`-2kappa r b grad c`, and `-2kappa grad r grad c` have respective bounds
`128ell/3`, `3ell^2 A_*/4`, `8sqrt(3)ell^2 A_*xi`, and
`sqrt(128)ell^(3/2)sqrt(A_*)`, all multiplied by `kappa xi^2`.

Define

\[
 H_t=\frac\xi3\{\eta L_J/\sqrt\ell+16\xi S_1\}
              +B_d\xi^2/\sqrt\ell+16\ell A_*\xi^3,
\]
\[
 e_0=2\{\ell A_*\xi^2+(\xi/3)\eta S_1\},
\]
\[
 e_1=2\{(\xi/3)\eta K_J+(16\xi^2/3)L_J
                   +C_d(\xi)\xi^2+16\ell\xi H_t\}.    \tag{A36}
\]
A26 and A35 give `||X E t||<=H_t`. The identities

\[
 W-w=2\kappa Qd_j-\tfrac{2\kappa\xi}{3}PJ,
 \quad
 DW=2\kappa\{Q\mathcal At+\kappa\ell T^*X\mathsf Et\}
\]
now give

\[
 \boxed{\|W-w\|_\rho\le\kappa e_0,\qquad
 \|DW-z_1\|_\rho\le\kappa^2 e_1.}                  \tag{A37}
\]
For the second identity the unprojected leading term is `(kappa xi/3)KJ`;
its projection error is bounded by `(kappa xi/3)eta KJ`. Its drift error is
bounded by `(16kappa xi^2/3)LJ`, using A5. A35 bounds the remainder and
A18 bounds the final conditional coupling. These are precisely all four
terms in e1.

Here are explicit error radii epsilon_j (distinct from the ground energy E_0),
solely as coefficient functions retaining
the full original kappa and xi factors:

\[
 \epsilon_0=\delta c_0+2\sqrt{(1+\delta)c_0}\,e_0/\xi+(e_0/\xi)^2,
\]
\[
 \epsilon_1=\delta\sqrt{c_0c_2}+\sqrt{(1+\delta)c_0}\,e_1/\xi
       +\sqrt{(1+\delta)c_2}\,e_0/\xi+e_0e_1/\xi^2,
\]
\[
 \epsilon_2=\delta c_2+2\sqrt{(1+\delta)c_2}\,e_1/\xi+(e_1/\xi)^2.
\]
A24, A32, A37 and expansion of each inner product prove

\[
 \boxed{|N_j-\kappa^{j+2}\xi^2c_j|
          \le\kappa^{j+2}\xi^2\epsilon_j,\qquad j=0,1,2.}     \tag{A38}
\]
For fixed loop, all displayed epsilon_j tend to zero with xi, uniformly over every
exterior box containing the collar. The complete finite formulas, rather
than just this asymptotic statement, determine the actual certificate below.

## 9. The actual response and restored metric are also enclosed

Specialize only the loop to the elementary face; retain arbitrary L>=2 and
a>0. Let `J0=sum_p j_p^(0)`, `J1=sum_p j_p^(1)`, so `J=J0+J1`. At the actual
positive shift `s=kappa`, use the explicit LOCAL polynomial

\[
 Z=\frac4{33}J_0+\frac4{45}J_1
   =\frac4{45}J+\frac{16}{495}J_0,
 \quad z=\xi Z,\quad Y=Qz.                           \tag{A39}
\]
A30 gives `(K+1)Z=(2/3)J=:U`, and the twelve exact Haar contributions give

\[
 \langle U,Z\rangle_H=m_*:=\frac{28}{165},\qquad
 \|Z\|_H^2=z_*:=\frac{796}{27225}.                    \tag{A40}
\]
Each fused trace in J0 has six original edges. Thus
`||J0||_infty<=9`, `sum_e||X_eJ0||_infty<=27`, and A31 gives

\[
 \|U\|_\infty\le8,\quad \|Z\|_\infty\le Z_*:=\frac{224}{165},
 \quad \sum_e\|X_eZ\|_\infty\le L_*:=\frac{848}{165}. \tag{A41}
\]
Both `E_H Z` and `E_H Y_alpha Z` are zero. Put

\[
 h_z=\xi\{\eta L_*/2+16\xi Z_*\},\quad
 r_z=8A_*\xi^2+16\xi^2L_*+64\xi h_z,\quad
 n_z=\sqrt{(1+\delta)z_*}.                            \tag{A42}
\]
Then `||X E z||<=h_z`, `||Pz||<=xi eta Z_*`, and `||Y||<=xi n_z`.
The ORIGINAL response residual is

\[
 R=W-(D+\kappa)Y
   =2\kappa Qd_j+2\kappa\xi Q\sum_i b_iX_iZ
                  -\kappa\ell T^*X\mathsf Ez,
 \quad \|R\|_\rho\le\kappa r_z.                    \tag{A43}
\]
All three terms are retained. In particular no inverse of D at zero is used.

The parent residual identity, proved again by expanding the square, is

\[
 M(\kappa)=2\langle W,Y\rangle_\rho-q_{\mathcal A+\kappa}(Y)
             +\langle R,(D+\kappa)^{-1}R\rangle_\rho. \tag{A44}
\]
Define the following seven nonnegative terms:

\[
\begin{array}{ll}
 a_1=\delta\xi^2\sqrt{z_*}, &a_2=16\xi^3 Z_*L_*,\\
 a_3=16\xi^2\eta^2 Z_*, &a_4=16A_*\xi^3 n_z,\\
 a_5=4h_z^2+(\xi\eta Z_*)^2,
 &a_6=128\xi^2 n_z h_z,\\
 a_7=r_z^2.&
\end{array}
\]
Set `E_M=(sum a_i)/xi^2` and

\[
 E_Z=\delta z_*+(\eta Z_*)^2+2n_zr_z/\xi+(r_z/\xi)^2.
\]
Then

\[
 \boxed{|M(\kappa)-\kappa\xi^2m_*|\le\kappa\xi^2E_M,
 \quad |\|(D+\kappa)^{-1}W\|_\rho^2-\xi^2z_*|
                                      \le\xi^2E_Z.} \tag{A45}
\]
Here is the full expansion proving the first estimate. Writing p=Pz, A44's
first two terms equal

\[
 2\langle w,z\rangle-q_{\mathcal A+\kappa}(z)
 -2\langle Pw,p\rangle+4\kappa\langle d_j,Y\rangle
 +q_{\mathcal A+\kappa}(p)+2q_{\mathcal A}(Y,p).
\]
Weighted integration by parts and `(K+1)Z=U` turn the first pair into
`kappa xi^2 <U,Z>_rho+2kappa xi^2 int rho Z sum_i b_i X_iZ`.
A24 and A40 bound its first error by kappa a1. A5 and A41 bound its drift
term by kappa a2. Conditional comparison bounds the removed projection
by kappa a3. A14 bounds the d_j term by kappa a4. A18 bounds the coarse
energy by kappa a5 and the mixed energy by kappa a6. Finally the positive
residual term in A44 is at most `||R||^2/kappa<=kappa a7`.
For the second estimate, `||Y||^2=||z||^2-||Pz||^2` and
`||(D+kappa)^{-1}W-Y||<=r_z`; expand the squared norm and apply A24 and A42.

These are direct enclosures of the interacting response and restored metric,
using a specified original Wilson-polynomial trial, not a fit to vacuum data.
The exact section correction in the Split Zero application is as follows.
In the parent's complex `V_j --(D+kappa)--> ker E`, take the actual
one-dimensional source `V_1=span{Y}`. Its forcing representative is R and
its remaining primitive is `(D+kappa)^{-1}R`. Define

\[
 a_Y=q_{\mathcal A+\kappa}(Y),\quad c_Y=\langle Y,W\rangle_\rho,
 \quad \alpha_Y=c_Y/a_Y,\quad
 R_{\rm can}=W-(D+\kappa)(\alpha_Y Y).
\]
The number a_Y is strictly positive. Indeed the Haar-mean-zero local
polynomial z has positive Haar norm A40, so it is not a function of Omega:
applying E_H to such a function would fix it and hence force z=0.
The actual density rho is everywhere positive, so the same equality of
functions cannot hold in L2(rho). Thus Y=Qz is nonzero and
`a_Y>=kappa ||Y||^2>0`.

In the original pairing `\langle h,k\rangle_{dual}=
\langle h,(D+\kappa)^{-1}k\rangle_\rho`, direct multiplication gives
`\langle (D+\kappa)Y,R_can\rangle_dual=0`. Therefore R_can is the
minimum-norm representative of [W], and the complete identities are

\[
 \boxed{\begin{aligned}
 \|[W]\|_{\mathcal K/(D+\kappa)V_1,dual}^2
     &=M(\kappa)-|c_Y|^2/a_Y,\\
 R&=R_{\rm can}+(\alpha_Y-1)(D+\kappa)Y,\\
 \langle R,(D+\kappa)^{-1}R\rangle_\rho
     &=\|[W]\|_{\mathcal K/(D+\kappa)V_1,dual}^2
                         +a_Y|\alpha_Y-1|^2.
 \end{aligned}}                                                   \tag{A45a}
\]
The cross term is zero by the just-proved orthogonality. The correction has
its original primitive `(alpha_Y-1)Y`; neither this vector nor its energy is
dropped. Both nonnegative terms in A45a are at most `kappa r_z^2` by A43–44.
This is the precise map between the chosen trial residual and the canonical
cohomological residual. It bounds the original quotient class on an actual
Yang–Mills source while retaining the section correction.

## 10. Finite evaluated certificate and the raw state metric

Take the exact value `xi=1/100000000`, equivalently `g^2=5000`, while keeping
`a>0` arbitrary, hence `kappa=10000/a`. These conditions are within A14's
proved domain. Evaluate A25–45 with `ell=4`, `d=32`. The standard-library
checker obtains rigorous rational upper endpoints, giving for every L>=2

\[
 \boxed{\begin{aligned}
 0.9994\,\kappa^2\xi^2&<N_0<1.0006\,\kappa^2\xi^2,\\
 4.9963\,\kappa^3\xi^2&<N_1<5.0037\,\kappa^3\xi^2,\\
 25.728\,\kappa^4\xi^2&<N_2<25.772\,\kappa^4\xi^2,
 \end{aligned}}                                                   \tag{A46}
\]
\[
 \boxed{\left|M(\kappa)-\frac{28}{165}\kappa\xi^2\right|
                  <0.0000075\,\kappa\xi^2,\qquad
 \left|\|(D+\kappa)^{-1}W\|_\rho^2-\frac{796}{27225}\xi^2\right|
                  <0.0000021\,\xi^2.}                            \tag{A47}
\]
No finite-volume vacuum integral was numerically substituted: these are
bounds for the actual vacuum, proved using A5–45, with exact arithmetic
for the final constants. The sharpness of the constants is not claimed.

The original centered state has raw Gram `G=<F^2>-<F>^2` and kinetic entry
`K0=kappa(4-<F^2>)`. Their control also improves to order xi^2. The exact
weighted identities, obtained by integrating K F=3F and
K(F^2)=8(F^2-1), are

\[
 3\langle F\rangle=2\langle j\rangle,\qquad
 \langle F^2\rangle-1=\tfrac12\langle Fj\rangle.      \tag{A48}
\]
Let `delta_C=exp(128pi xi)-1` and define

\[
 B_2=\xi\delta/4+(\sqrt5\xi/6)\delta_C+4A_*\xi^2,
 \quad e_\mu=(2\xi/9)(B_2+3\delta/2)+(8A_*/3)\xi^2.
\]
A34, A48 and the exact Haar moments
`<F^2>_H=1,<F^4>_H=2,<F^6>_H=5` give

\[
 |\langle F^2\rangle-1|\le B_2,\quad
 |\langle F\rangle-2\xi/3|\le e_\mu,\quad
 |G-1|\le B_2+(2\xi/3+e_\mu)^2,\quad |K_0-3\kappa|\le\kappa B_2. \tag{A49}
\]
For verification of B2, the Haar means of FJ and F(4-F^2) vanish;
`||F||_H||J||_H=3/2` and `||F(4-F^2)||_H=sqrt(5)`. Their expectation
errors are at most `3delta/2` and `sqrt(5)delta_C`, respectively, and
`|<F d_j>|<=8A_*xi^2`. Substitute into A48. The mean estimate follows
by retaining `<J>`, `4-<F^2>`, and `<d_j>` in its first equation.
At A46's exact coupling both Gram and kinetic relative radii are below
`11/10^14`. The restored lift Gram is the actual sum
`G+||(D+kappa)^{-1}W||^2`; G is retained rather than reset to one.

There is also a direct return to the original physical energy. Put
`h_kappa=(D+kappa)^{-1}W`, `f=F-<F>`, and
`Phi=psi(J f+h_kappa)`. Its mean is zero since `E h_kappa=0`, so
`Phi` is in the original physical space and perpendicular to psi. It is
nonzero since G>0. The original excitation form is used on its H1 domain.
The exact norm and form energy are

\[
 \|\Phi\|^2=G+\|h_\kappa\|_\rho^2,\qquad
 q_{H-E_0}(\Phi,\Phi)
       =K_0-M(\kappa)-\kappa\|h_\kappa\|_\rho^2.
\]
Indeed the two mixed form entries are each `-M(kappa)`, and
`q_D(h_kappa)=M(kappa)-kappa||h_kappa||^2`. Both entries are retained
in this calculation. Substitution of A47 and A49 gives, at the exact
coupling A46,

\[
 \boxed{(3-5\cdot10^{-13})\kappa
 <\frac{q_{H-E_0}(\Phi,\Phi)}{\|\Phi\|^2}
 <(3+5\cdot10^{-13})\kappa.}                       \tag{A49a}
\]
The actual map from this state to the finite-volume spectral assertion is
the inclusion of `span{Phi}` in `psi^perp intersect H^1_phys` and the exact
variational formula
`Delta_L=inf_(0!=v perpendicular psi) q_(H-E0)(v)/||v||^2`.
It gives `Delta_L` at most the middle expression in A49a. The lower bound
in A49a concerns the displayed state, with its own source and norm; no
inequality with the reverse variational direction is used.

For an additional arithmetic check, the single-column trial `Y=W/(6kappa)`
has leading response lower coefficient 1/6 and residual coefficient 1/48,
yielding the leading interval [1/6,3/16]. The exactly evaluated coefficient
28/165 lies strictly inside it. A39–47 give the tighter certified return.

## 11. Physical refinement, scope, and the next quantitative target

On the retained simultaneous path

\[
 a_n=a_0 2^{-n},\quad L_n=4\,2^{2n},\quad
 g_n^2=(g_0^{-2}+\beta n\log2)^{-1},\quad
 c_n=g_0^{-2}+\beta n\log2,
\]
\[
 \kappa_n=2^{n+1}/(a_0c_n),\quad \xi_n=c_n^2/4,
 \quad \ell_n=4\,2^{n-r}\quad\hbox{for a fixed level-r square}. \tag{A50}
\]
The all-coupling A5, A9, A13, A18 and A21 apply with these literal values.
For instance `|X_e log psi_n|<=2c_n^2` and the gauge-covariant inverse has

\[
 \| (\mathcal A_n|_{E_v})^{-1}\|
 \le\frac{3a_0c_n}{2^{n+1}}\longrightarrow0,           \tag{A51}
\]
uniformly in the vertex and exterior volume, including vertices changing
with n. The limit follows from `(constant+linear n)/2^n ->0`.
The physical contraction and all its cross derivatives remain those proved
in section 3; A51 is an estimate on that specified source sector.

The narrow interval A46 uses g^2=5000. Along A50, xi_n grows. A14's sharper
pointwise remainder is applicable precisely on `xi_n<=3/64`; A13's L2
remainder remains available at all xi_n with its displayed larger constant.
No substitution between those domains is made. Physical loop length grows
as ell_n, and the exact A21 constants retain that growth. A33 also quantifies
the loop-size growth of the small-xi coefficients. These facts locate the
remaining infrared problem in the full singlet contraction and its retained
conditional-kernel response, rather than conceal it in source coordinates.

The next quantitative calculation is the zero-shift physical response and
its smallest generalized energy relative to the restored Gram on coupled
loop families, with the exact A17 additional kernel retained. This cycle has
completed the three-moment task and one positive-shift response evaluation
on the above actual sources. It has also supplied all-coupling source inverse
and moment bounds. It has not evaluated a physical continuum mass lower edge.

## 12. Verification, source pins, and failures retained

`verify.py` uses original real quaternion coordinates and exact rational
polynomials. Its Haar integration uses
`int prod q_i^(2a_i)=prod(2a_i-1)!! / prod_(j=0)^(sum a-1)(4+2j)`, and odd
monomials integrate to zero. This identity follows by expressing four
independent real Gaussian coordinates in polar coordinates and cancelling
the identical radial moments; no physical measure is replaced by that
Gaussian auxiliary integral. The coordinate identity tested is on
`sum q_i^2=1` via explicit polynomial division with its retained remainder.
Original graph words and unique unmatched-edge witnesses are checked for
square sides 1 through 12. These finite cases accompany the incidence proof
for every side in section 7.

For numerical endpoints, Machin's identity
`pi=16 atan(1/5)-4 atan(1/239)` is verified by the tangent addition formula
and its interval (0,pi/2). Alternating rational sums prove `pi<355/113`.
The exponential upper bound uses thirty positive Taylor terms plus the
geometric bound on the remaining term ratios; square-root bounds use integer
squares at scale 10^50. Every inequality A46–47 and A49's reported radius is
then checked with rational upper endpoints. Ordinary and optimized Python
must produce identical records; errors use explicit exceptions.

An initial development run failed the Machin tangent check because the test
applied a redundant angle doubling to the already quadrupled tangent 120/119.
The test was corrected to `(120/119-1/239)/(1+(120/119)(1/239))=1`.
The analytic statements and source bounds were unchanged. The final written
proof audit also corrected the interpretation of the noncanonical trial
residual: A45a now retains its exact difference from the canonical quotient
norm. The response and moment inequalities A38 and A45 retain their values;
a new exact regression rejects the false identification. Notational review
separates the residual vector mathfrak r_e from the plaquette count r_e, and
the error radii epsilon_j from the ground energy E_0. No failed run or earlier
file is represented as a certificate for these final bytes.

[YM] `KokunoYumeto/yang-mills-interacting-workbench`, primary source at
`fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`,
`yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md`,
Git blob `66a7453a6452c2555a28270efcf53fa1997c26a8`, sections 1–3.
The original full operator, ground-state domain and local exterior comparison
are used. All new derivative and response estimates are proved above.

[Parent] Same repository, PR6 at
`e98b2c3af77f66fb1c1396143ca53daef586404f`,
`yang-mills/continuations/20260914-coupled-response/RESEARCH_NOTE.md`,
blob `1f6bfb085a626f3b1aa693e86a619e81af41529a`, especially C13–22.
Its full delivered body was read. A15–20 prove the additional observation map
and its kernel; A43–45 instantiate its actual residual-cohomology certificate.
Earlier workbench attribution and the primary SU(2) conventions are preserved.
No new number-theoretic asymptotic or peer formal certificate is imported.


# Gauge-native source bounds and the full physical excitation band

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md}

\textbf{SHA-256:} \path{c24f5235b8c25daa1ee20fb81a13d8db94b88cb99b298ac7d10c8b4e5faafebd}
\end{quote}


15 September 2026. This continuation starts from the original SU(2) Hamiltonian and the delivered `20260915-uniform-gap-zero-shift` source. Its new calculations use the vertex-gauge action before estimating the nonlinear source. All original links, spin labels, Fourier coefficients, physical energy factors, means, relation labels and vacuum scalar remain. `BAND_AND_CERTIFICATE.md` calculates the first physical band and its full second coefficient, with a uniform analytic remainder. `SPATIAL_RETURN.md` gives the unique spatial-volume return on the enlarged domain. The final enlarged source and volume domain is established in SECOND_SOURCE.md R1–16 using the actual second vacuum coefficient. These are written proofs, accompanied by exact finite verification. No four-dimensional continuum mass-gap conclusion, new Lean verification or literature-priority claim is made.

## G1. Original objects and the precise retained quotient

For integer L>=2 take the vertices {-L,...,L}^3, all positive contained nearest-neighbor links E_L, and all contained elementary plaquettes P_L with their original oriented four-link words W_p. Put

\[
 H_L=\kappa K_L+\kappa\xi\sum_{p\in P_L}(2-W_p),\quad
 K_L=-\sum_{e,\alpha}X_{e,\alpha}^{2},\quad
 \kappa=2g^2/a,\quad \xi=1/(4g^4),\quad a,g>0.                 \tag{G1}
\]

Here T_alpha=-i sigma_alpha/2 and X differentiates exp(t T_alpha)U_e. Product Haar probability, the scalar 2 kappa xi |P_L|, and the original physical invariant subspace are retained. Let psi_L>0 be the positive unit vacuum and E_0,L its actual energy. The original multiplication map

\[
 \mathcal U_L:L^2(\rho_LdU)\longrightarrow L^2(dU),\quad
 f\longmapsto\psi_Lf,\quad \rho_L=\psi_L^2
\]

is unitary, with inverse division by psi_L. Its transported form is

\[
 q_{\mathcal A_L}(f,h)=\kappa\int\rho_L\sum_{e,\alpha}
       \overline{X_{e,\alpha}f}X_{e,\alpha}h\,dU,
 \qquad \mathcal A_L=\mathcal U_L^{-1}(H_L-E_{0,L})\mathcal U_L. \tag{G2}
\]

On this finite compact group the operator and form domains are H^2 and H^1, respectively, with their invariant subspaces in the physical calculation. The positive smooth vacuum and the form identity are also proved directly in G8 for the constructed range of couplings.

For product-spin labels j=(j_e), keep

\[
 c(j)=\sum_ej_e(j_e+1),\quad
 f_j(U)=\operatorname{Tr}(A_j\pi_j(U)),\quad
 A_j=d_j\int f(U)\pi_j(U)^*dU.                              \tag{G3}
\]

The representation dimension d_j is part of the coefficient; the matrix trace norm below is that of A_j. Vertex-gauge averaging P_G acts on this original coefficient space, commutes with K_L, and preserves every j block and every local support. The exact quotient map is

\[
 \mathscr C/\operatorname{im}(I-P_G)\xrightarrow{\cong}
 \operatorname{im}P_G,\quad [f]\mapsto P_Gf,
 \quad h\mapsto[h].                                      \tag{G4}
\]

Indeed P_G^2=P_G by Haar multiplication, ker P_G=im(I-P_G), and f-P_G f is that displayed original relation. Each coefficient eliminated by the gauge map is still a vector in this kernel. Only its actual image is used in the next estimate.

## G2. A graph inequality on every nonzero physical Fourier block

At each vertex v of a nonzero physical block, its incident spins obey

\[
 j_e\le\sum_{f\ni v,\,f\ne e}j_f.                        \tag{G5}
\]

For a proof, a nonzero invariant tensor at v gives an intertwiner from V_{j_e} into the tensor product of the other incident representations, with duals for opposite orientations. SU(2) duals have the same spin. Irreducibility makes this intertwiner injective. The highest J_3 weight of the target is at most the sum of those other spins; the image contains weight j_e. This proves G5. A nonzero global Fourier invariant supplies such a local invariant at every vertex, by grouping its original incident matrix indices. Thus no separate spin-network ansatz is assumed.

Fix e={u,v}. Write E_1 for the other edges incident on u or v, and O for their other endpoints. The original cubic graph is simple and triangle-free, so these endpoints are distinct and none is u or v. Each w in O has exactly one edge of E_1 entering {u,v}. Put J_1=sum_{f in E_1}j_f. The two inequalities G5 at u and v give J_1>=2j_e. Summing G5 at the vertices of O gives J_1<=2J_2, where E_2 consists of edges incident on O outside {e} union E_1 and J_2=sum_{f in E_2}j_f. Each such edge is counted at most twice. Hence

\[
 \sum_f j_f\ge j_e+J_1+J_2\ge4j_e.
\]

Every nonzero half-integer spin satisfies j(j+1)>=(3/2)j. Consequently

\[
 \boxed{c(j)\ge6j_e\quad\hbox{for every edge e in every nonzero physical block}.}
                                                               \tag{G6}
\]

The constant 6 is attained by a spin-1/2 elementary plaquette. The separate estimate

\[
 \sum_ej_e\le(2/3)c(j)                                   \tag{G7}
\]

continues to hold for arbitrary product-spin labels, including nonphysical ones. G6 and G7 have different specified domains and will be used at their respective places.

In particular every nonconstant physical block has c(j)>=3. If c(j)<9/2, its active support has at most five edges. No active vertex can have valence one by G5. A finite subgraph with at most five edges and no vertices of valence one in the cubic lattice is a four-cycle: it contains a cycle, the lattice has no triangle or odd cycle, and a fifth edge cannot have both endpoints on a four-cycle without producing a chord absent from the nearest-neighbor lattice. Every four-cycle is an elementary plaquette. The two-edge vertex invariants force the four spins to coincide. Their Casimir is 4j(j+1), equal to 3 at j=1/2 and at least 8 at j>=1. Thus

\[
 \operatorname{spec}(K_L|_{\mathrm{phys}})\subset
 \{0,3\}\cup[9/2,\infty),\qquad
 \ker(K_L-3)=\operatorname{span}\{W_p:p\in P_L\}.          \tag{G8}
\]

At a two-edge spin-1/2 vertex the invariant contraction is unique up to its scalar; following the four actual indices gives W_p. Different p have orthogonal product-spin blocks, and int_H W_p W_q=delta_pq. This proves both equality in the eigenspace statement and its dimension |P_L|.

## G3. The original coefficient source with all relation labels retained

For every nonempty finite edge label S retain a zero-Haar-mean physical function f_S with coefficients A_(S,j), including j whose active support is strictly smaller than S. Define

\[
 \|f\|_{\mathrm{loc},1}
 =\max_e\sum_{S\ni e}\sum_{j\ne0}c(j)\|A_{S,j}\|_1.     \tag{G9}
\]

This is an auxiliary absolute-convergence norm, on the SAME coefficient families as the predecessor. On each finite graph its identity map to the predecessor's weight-5/4 source has both inverse maps and bounds

\[
 \|f\|_{\mathrm{loc},1}\le\|f\|_{\mathrm{loc},5/4}
 \le(5/4)^{|E_L|}\|f\|_{\mathrm{loc},1}.                 \tag{G10}
\]

The volume-dependent comparison is recorded and is never used to assert a uniform bound. The physical pairing is still G2.

Assembly takes A_(S,j) to sum_{S containing supp(j)} A_(S,j). Its kernel is the original coefficient equation that this sum is zero for every j. The relation (B at (S,j))-(B at (supp(j),j)) and the actual coefficient at every S strictly containing supp(j) reconstruct that whole kernel, exactly as in predecessor U9-11. The physical subspace is preserved under this relation. Zero assembly therefore retains the original relation primitive, rather than deleting its supports.

The coefficient product and derivative bounds used here are

\[
 \sum_\ell\|A_\ell(f_jh_k)\|_1\le\|A_j\|_1\|B_k\|_1,
 \qquad\|A(X_{e,\alpha}f_j)\|_1\le j_e\|A_j\|_1.        \tag{G11}
\]

For completeness, the product is Tr((A_j tensor B_k)(pi_j tensor pi_k)). Unitary decomposition into the complete irreducible/multiplicity spaces, pinching to diagonal blocks, and partial trace over multiplicity give its exact output coefficients. Pinching is an average of unitary conjugations. For partial trace, trace-norm duality bounds Tr((Z tensor I)C) by ||C||_1 for ||Z||op<=1. These facts prove the first bound, retaining all output labels. The second follows from the original spin generator norm ||J_alpha||=j and trace-norm duality. All three alpha values remain.

Let Q_H remove only the trivial Haar coefficient. Define the original bilinear source

\[
 \mathcal B(f,h)_S=K_L^{-1}Q_H
 \sum_{S_1\cup S_2=S}\sum_{e,\alpha}
                  (X_{e,\alpha}f_{S_1})(X_{e,\alpha}h_{S_2}). \tag{G12}
\]

The scalar removed at each S is recorded separately. The active product support may become smaller, but the original union label S is retained.

For an anchor a in S_1, G6 on the h block and G7 on f give

\[
 3\sum_{S_1\ni a,j}\|A_{S_1,j}\|_1
       \sum_e j_e\sum_{S_2\ni e,k} k_e\|B_{S_2,k}\|_1
 \le\frac13\|f\|_{\mathrm{loc},1}\|h\|_{\mathrm{loc},1}.
\]

Interchanging f,h gives the other anchor contribution. Counting the overlap twice is an upper bound. The output c(j) cancels the exact inverse Casimir in G12, and therefore

\[
 \boxed{\|\mathcal B(f,h)\|_{\mathrm{loc},1}
           \le(2/3)\|f\|_{\mathrm{loc},1}\|h\|_{\mathrm{loc},1}.} \tag{G13}
\]

G13 is on the gauge-invariant source. Its proof retains the generator sum, graph constraints, and all representation multiplicities.

## G4. Exact plaquette coefficient, convergent source, and the closed endpoint

For the original word Tr(U1 U2 U3^-1 U4^-1), its complete 16 by 16 coefficient in G3 is

\[
 A_{(i_1,i_2,1-i_2,1-i_3),(i_0,i_1,1-i_3,1-i_0)}
       \mathrel{+}=(-1)^{i_0+i_2},\qquad i_0,i_1,i_2,i_3\in\{0,1\}. \tag{G14}
\]

All other entries are zero. The inverse-entry formula (U^-1)_(r,c)=(-1)^(r+c)U_(1-c,1-r) proves the identity in the original coordinates. The four disjoint two-row/two-column blocks have the entries [[1,-1],[-1,1]], with the remaining rows and columns unused. Thus (A* A)^2=4A* A and Tr(A* A)=16. The positive square root is (A* A)/2, giving ||A||_1=8. This independently reproduces predecessor O1-2.

The first source is v_[1]=(1/3)sum_p W_p, with its actual four-link labels. At most four plaquettes meet an edge, so

\[
 \|\xi v_{[1]}\|_{\mathrm{loc},1}\le32\xi.               \tag{G15}
\]

Use the full coefficient recurrence

\[
 v_{[p]}=\sum_{i=1}^{p-1}\mathcal B(v_{[i]},v_{[p-i]}),\quad
 v(\xi)=\sum_{p\ge1}\xi^p v_{[p]}.
\]

With C_n=(2n)!/(n! (n+1)!), G13 proves

\[
 \|\xi^p v_{[p]}\|_{\mathrm{loc},1}
 \le a_p(\xi):=C_{p-1}(2/3)^{p-1}(32\xi)^p.             \tag{G16}
\]

The original union recurrence also gives |S|<=3p+1, connected support, and j_e<=p/2 at order p. These are exact support facts, not alterations of any coefficient.

Set

\[
 \theta=256\xi/3,\quad
 r(\xi)=\frac34(1-\sqrt{1-\theta}),\quad
 \epsilon(\xi)=\frac23r(\xi)=\frac{1-\sqrt{1-\theta}}2.  \tag{G17}
\]

For 0<=theta<1 the Catalan recurrence proves sum_p a_p=r and

\[
 \sum_{p>P}a_p\le\frac{32\xi\theta^P}{1-\theta}.         \tag{G18}
\]

At the endpoint xi=3/256 the series still converges absolutely. The complete scalar tail there is

\[
 \sum_{p>P}a_p(3/256)
   =\frac34\frac{\binom{2P}{P}}{4^P}
   \le\frac{3}{4\sqrt{P+1}}.                            \tag{G19}
\]

To verify the exact equality, put b_P=binom(2P,P)/4^P. Then C_P/4^P=2(b_P-b_(P+1)). Telescoping and b_P->0 give the formula. The bound b_P<=1/sqrt(P+1) follows by induction from ((2P+1)/(2P+2))^2<=(P+1)/(P+2). It also proves b_P->0 without an asymptotic substitution.

For every finite box G9 is complete, and its total c-weighted coefficient sum is at most |E_L| times G9. G11 bounds the original first and second derivatives by that total. Absolute convergence, including G19, therefore gives a C^2 function and permits G12 to be summed. The fixed equation is

\[
 K_Lv=\xi\sum_pW_p+\sum_i(X_iv)^2-C_L,\quad
 C_L=\int_H\sum_i(X_iv)^2.                               \tag{G20}
\]

All removed scalar coefficients are exactly included in C_L. Set

\[
 c_L=-\tfrac12\log\int e^{2v}dU,\quad
 \psi_*=e^{v+c_L},\quad
 E_*=2\kappa\xi|P_L|-\kappa C_L.                         \tag{G21}
\]

Equation G20 and direct differentiation prove H_L psi_*=E_* psi_*. The positive C^2 solution becomes smooth by elliptic bootstrapping. For every smooth h the product rule proves q_(H_L-E_*)(psi_*h)=kappa int psi_*^2 sum|Xh|^2. Multiplication and division by the positive smooth psi_* preserve H^1 on this compact finite group. Hence E_* is the actual lowest energy; dividing any other ground vector by psi_* proves uniqueness. This identifies G21 with the original vacuum, including its full scalar and Haar mass. The completed closed coupling domain is

\[
 \boxed{0<\xi\le3/256,\qquad g^2\ge8/\sqrt3.}           \tag{G22}
\]

No contraction constant smaller than one is asserted at theta=1; G19 supplies that endpoint directly.

## G5. A relative bound for the original drift, and the full physical gap

Let X_0 be the zero-Haar-mean Fourier algebra with norm sum_j ||A_j||_1; let Y_0 carry sum_j c(j)||A_j||_1. Use the physical subspaces when explicitly indicated. For a smooth zero-Haar-mean f, the same original coefficient product gives

\[
 \left\|Q_H\sum_i(X_iv)(X_if)\right\|_{X_0}
 \le 3\sum_k\|A_k(f)\|_1\sum_e k_e
        \sum_{S\ni e,j}j_e\|A_{S,j}(v)\|_1
 \le\frac r3\|f\|_{Y_0}.                                \tag{G23}
\]

Only v uses G6; f uses G7. Thus G23 also holds on the full scalar space. The complete relative perturbation -2 kappa Q_H sum (Xv)X has norm at most kappa epsilon from Y_0 to X_0.

Every smooth function on the finite product belongs to Y_0. One direct proof uses Peter-Weyl Plancherel, ||A_j||_1<=sqrt(d_j)||A_j||_HS, and Cauchy-Schwarz with sufficiently many original Casimir powers. The series sum_j d_j^2(1+c(j))^-M is finite for M>3|E_L|/2; elementary comparison of the product-spin sums proves it. Smoothness supplies all these powers. This step requires no uniform-in-volume regularity constant.

The coefficient projection Q_H is related to the original centered-vacuum space by the two inverse maps

\[
 f\mapsto Q_Hf,\quad y\mapsto y-\langle y\rangle_{\rho_L},
 \quad \langle f\rangle_{\rho_L}=0,\ \int_Hy=0.           \tag{G24}
\]

Both compositions are identities. They intertwine A_L with its literal Haar quotient

\[
 \overline{\mathcal A}_L
 =\kappa K_L-2\kappa Q_H\sum_i(X_iv)X_i.                 \tag{G25}
\]

For the inverse identity in the operator square, int rho_L A_L y=0 gives precisely the constant required in G24. No Haar mean is substituted for a vacuum mean.

Let A_L f=lambda f be a nonzero physical excitation, and y=Q_Hf. For 0<lambda<3kappa, G8 and G23 give

\[
 \|y\|_{Y_0}
 \le\frac{3\kappa\epsilon}{3\kappa-\lambda}\|y\|_{Y_0}.
\]

The vector is nonzero, so lambda>=3kappa(1-epsilon). Every finite-regulator eigenfunction is smooth by the original elliptic equation. Compact spectral resolution consequently extends the result to the whole physical form domain:

\[
 \boxed{\Delta_L\ge d_{\rm phys}(\xi)\kappa,
 \quad d_{\rm phys}=3(1-\epsilon)
       =\tfrac32(1+\sqrt{1-256\xi/3}).}                   \tag{G26}
\]

On the full scalar space replace the free value 3 by its original 3/4. The identical argument proves

\[
 \boxed{\Delta_L^{\rm scalar}\ge d_{\rm sc}(\xi)\kappa,
 \quad d_{\rm sc}=\tfrac34(1-\epsilon)=d_{\rm phys}/4.}   \tag{G27}
\]

The inclusion of the original physical subspace into the scalar space intertwines both Hamiltonians; G26 uses its explicitly computed free Fourier support G8. All physical states, including volume-dependent states, are covered by G26.

For example at every g^2>=5,

\[
 \Delta_L\ge\tfrac32(1+\sqrt{11/75})\kappa
             >2.07445\kappa.                            \tag{G28}
\]

In the original physical units the general bound is

\[
 \Delta_L\ge\frac{3g^2}{a}
          \left(1+\sqrt{1-64/(3g^4)}\right).             \tag{G29}
\]

## G6. The native primitive and the zero-shift response return

On centered physical H^1 define d_X f=(X_i f)_i with its ORIGINAL energy norm kappa int rho sum|X_i f|^2. The inverse on its actual range is p_X(d_X f)=f. The variational characterization, with the G2 unitary, proves

\[
 \|p_X\|^2=1/\Delta_L\le1/(\kappa d_{\rm phys}).          \tag{G30}
\]

This is the primitive of the original gradient window. G4 and the assembly relations retain the sources used to control it. The auxiliary Fourier source norm supplies the spectral estimate; it has not replaced either the physical state norm or the derivative energy norm.

For the predecessor's loop observation, gauge averaging commutes with the actual conditional expectation: change variables in its defining conditional-density integral and use the basepoint conjugation of the original loop holonomy. It therefore commutes with the form compression D. Let I:K_phys->K be the isometric inclusion of its physical reducing subspace. The domain and resolvent identities are

\[
 DI=ID_{\rm phys},\quad (D+s)^{-1}I=I(D_{\rm phys}+s)^{-1}.
\]

The actual forcing W=-Q_C A_L F and the displayed trial and residual are physical. Consequently their unchanged response pairing is

\[
 \langle W,D^{-1}W\rangle
 =\langle I^*W,D_{\rm phys}^{-1}I^*W\rangle,
 \quad \|D_{\rm phys}^{-1}\|\le1/(\kappa d_{\rm phys}).   \tag{G31}
\]

All predecessor minimum-section, quotient-residual and mixed-state identities now use this stronger proven inverse bound on their actual source. The scalar inverse on the whole K retains its separate value G27.

## G7. What was audited and what is continued

The predecessor's Fourier pinching, original union labels, vacuum-scalar return, Haar/physical form maps and conditional comparison have been inspected at their displayed proof steps. The gain here is G6 on the original gauge image, followed by the explicitly re-derived constants G13, G15 and G23. A blanket independent review of every historical artifact is not claimed.

The full next calculation is in BAND_AND_CERTIFICATE.md: the entire first excitation band, the exact boundary-sensitive second-order matrix, and an actual finite-L eigenvalue enclosure with a uniform analytic remainder. SPATIAL_RETURN.md proves the full-volume result on the complete closed source domain, retains its separately calculated conditional-influence subdomain, and computes the original running continuum path. The strong-coupling endpoint G22 and the physical band do not assign a result at g approaching zero.


# Development and audit record

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-gauge-native-band/DEVELOPMENT.md}

\textbf{SHA-256:} \path{eec8333d56cd32321e10a97e1166e7ba0fe7b997d96fd919731d4383a0b5dfe7}
\end{quote}


The proof was developed in successive additive layers: gauge-constrained coefficient control; actual band and its integer spectral certificate; conditional volume return; direct full-domain mixing and coupling comparison; actual second-source evaluation beyond the first majorant endpoint.

The final audit explicitly checked: the local vertex intertwiner and graph shell count in G5–6; the Haar/vacuum mean inverse G24; the one-insertion Riesz cancellation B6; the extensive vacuum subtraction B11–16; the complete state metric B24–25; the constant equation S27; the source endpoint extension without a finite derivative row; and every factor in R2 and R15–16. The physical running-domain rationalization in R5 retains the required factor three; an omission was corrected before the final receipt and is now a negative control.

The original six-link loop trace norm was derived from its actual orientation contractions. Inverting just one tensor link was not presumed trace-norm preserving. The checker constructs all twenty three-forward/three-reverse words and the spin-one plaquette Gram exactly. This is the source of the bounded second coefficient, rather than an estimate inferred solely from its Haar norm.

The initial conditional-volume subdomain remains in S2–9 as its complete proved route. S10–14 and R4 extend it using an explicitly different estimate on the same original semigroup. The finite source endpoint, isolated-band contour and numerical remainder disks retain separate numerical domains.

The final literature cross-check read Dahmen's original operator definitions and second-order planar diagrams, then computed the full energy/coupling dictionary B30 and the planar-to-spatial coefficient maps B31–32. It agrees with the independently derived local channels. It does not constitute an external review of the three-dimensional convergence proof.

The published checker uses no NumPy, numerical eigensolver, Monte Carlo vacuum, spin cutoff or fitted remainder. Its named negative controls are deliberate false inputs, not evidence about the status of the continuum mass-gap problem. The written infinite-dimensional and limit proofs remain available for independent mathematical review.


# The actual second vacuum source and continuation beyond the first endpoint

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-gauge-native-band/SECOND_SOURCE.md}

\textbf{SHA-256:} \path{044279aa33cc6a53ea933ebe0aa903741653b4964883d7ea40b14b6bf5b9ff14}
\end{quote}


15 September 2026. This calculation uses the actual plaquette pair channels B12–14 to evaluate the second logarithmic-vacuum source before estimating higher orders. It improves the source endpoint further, while every original coefficient, relation label, Hamiltonian term, physical Gram and energy unit stays fixed. The previous estimates remain valid on their stated domains. R10–14 below supply the final enlarged finite- and infinite-volume domains of this continuation.

## R1. Evaluate the entire second source, including its zero coefficients

Use S=sum_p W_p and v_[1]=S/3. The original Casimir product rule gives

\[
 \sum_i(X_iS)^2=3S^2-\tfrac12K_LS^2,
 \qquad
 v_{[2]}=\left(\tfrac13K_L^{-1}-\tfrac1{18}I\right)Q_HS^2.
                                                               \tag{R1}
\]

The inverse acts only on the original nonconstant Haar coefficients. The scalar removed here remains in G20–21, whose second ground-energy term is exactly -kappa |P_L| xi^2/3.

For a single plaquette, W_p^2=1+chi_1(Omega_p), and the nonconstant term has Casimir 8. For distinct faces without a shared edge, the product has Casimir 6, so its coefficient in R1 is exactly zero. For an unordered adjacent pair {p,q}, let P_0 and P_1 be its actual shared-edge spin-zero and spin-one projections from B13. Their original Casimirs are 9/2 and 13/2. Substitution into R1 proves

\[
 \boxed{
 v_{[2]}=-\frac1{72}\sum_p\chi_1(\Omega_p)
   +\sum_{\{p,q\}:p\sim q}
      \left[\frac1{27}P_0(W_pW_q)-\frac1{117}P_1(W_pW_q)\right].}
                                                               \tag{R2}
\]

The factor two for an unordered pair comes from the two ordered terms of S^2. The labels remain the original plaquette or pair union. In particular P_0 has six active links but retains its seven-link union label. Every disjoint-pair coefficient is explicitly zero at its original union; it is not relabelled as an absent source.

## R2. Trace norms in the original link orientations

For a simple closed loop of length ell in the original positively oriented cubic links, let t be the number of local maxima of height x_1+x_2+x_3 around the loop. It also has exactly t local minima and ell-2t other vertices. At a maximum or minimum the original fundamental index contraction is the SU(2) alternating two-index vector, of Euclidean norm sqrt(2); at the other vertices it is a two-dimensional identity contraction. After separate permutations of the original row and column tensor indices, the Fourier coefficient is exactly a tensor product of those rectangular contractions. Row and column permutations preserve its singular values. Tensor-product singular values therefore give

\[
 \|A_{\rm loop}\|_1=(\sqrt2)^{2t}2^{\ell-2t}
                    =2^{\ell-t}\le2^{\ell-1}.         \tag{R3}
\]

The height cannot be strictly increasing around a closed loop, so t>=1. This also proves the original coefficient's full rank and singular values: rank 2^(ell-2t), with each nonzero singular value 2^t. These are original oriented coefficients; inversion of a single link is not assumed to preserve a tensor matrix's trace norm.

For the original spin-one plaquette the same four contractions have dimension three, with one maximum and one minimum. Its norm is exactly 3^3=27. Equivalently, the literal G14 matrix with indices in {0,1,2}, complements 2-i, and the same signs has nine rank-one three-by-three blocks. Each nonzero singular value is three.

For an adjacent pair, P_0(W_pW_q)=Tr(Omega_6)/2 on the actual simple six-link boundary. Equation R3 proves

\[
 x:=\|A(P_0(W_pW_q))\|_1\le16,
 \quad x+y\le64,\quad y:=\|A(P_1(W_pW_q))\|_1.          \tag{R4}
\]

The second bound is the full coefficient-product inequality G11 applied to the two original norm-eight plaquettes, including both irreducible outputs. No norm is assigned to P_1 from its Haar mass alone.

In the unchanged Casimir-weighted source G9, an adjacent pair's complete R2 contribution is at most

\[
 (9/2)x/27+(13/2)y/117
       =x/6+y/18\le16/3.                              \tag{R5}
\]

A spin-one self contribution is at most 8*27/72=3. For an anchored edge e, write r_e<=4 for its original face incidence. Counting each adjacent pair containing a face at e and subtracting its exact double count when both faces contain e gives

\[
 \#\{\{p,q\}:p\sim q,\ e\in\partial p\cup\partial q\}
 =\sum_{p\ni e}d_p-\binom{r_e}{2}
 \le12r_e-\binom{r_e}{2}\le42.
\]

Together with at most four self terms this proves the volume-independent bound on the ACTUAL second source:

\[
 \boxed{\|v_{[2]}\|_{\rm loc,1}\le4\cdot3+42\cdot16/3=236.} 
                                                               \tag{R6}
\]

The earlier purely bilinear estimate was (2/3)*32^2=2048/3. R6 uses the evaluated original pair channels and their complete coefficient norms.

## R3. A larger convergent source, with an explicit endpoint tail

Set a_1=32, a_2=236, and for n>=3 define the positive numbers

\[
 a_n=\frac23\sum_{i=1}^{n-1}a_i a_{n-i}.
\]

G13 and R6 prove ||v_[n]||loc<=a_n by induction, on the same original support-labelled coefficients. Their generating function r_2=sum_(n>=1)a_n xi^n satisfies

\[
 r_2=32\xi+236\xi^2+\frac23(r_2^2-1024\xi^2),
\]
\[
 \boxed{
 P_2(\xi)=1-\frac{256}{3}\xi+\frac{10720}{9}\xi^2,
 \qquad r_2(\xi)=\frac34(1-\sqrt{P_2(\xi)}),
 \qquad \epsilon_2=\frac23r_2.}                         \tag{R7}
\]

The branch has value zero at xi=0. Its positive coefficient recurrence proves the absolute majorant before any endpoint is taken. The first positive root is

\[
 \alpha=\frac3{4(32+\sqrt{354})},\qquad
 \beta_2=\frac3{4(32-\sqrt{354})},\qquad
 P_2=(1-\xi/\alpha)(1-\xi/\beta_2).                    \tag{R8}
\]

Write gamma=alpha/beta_2, so 0<gamma<1. In sqrt(1-z)=1-sum_(n>=1)b_n z^n the numbers b_n=C_(n-1)/(2*4^(n-1)) are positive. Multiplication of the two square-root series gives

\[
 0\le a_n\alpha^n
 \le\frac34 b_n(1+\gamma^n).
\]

The subtracted convolution has positive terms; the lower sign follows independently from the a_n recurrence. The exact binomial tail sum_(n>P)b_n=binom(2P,P)/4^P, already proved in G19, yields

\[
 \boxed{
 \sum_{n>P}a_n\xi^n
 \le\frac34(\xi/\alpha)^{P+1}(1+\gamma^{P+1})
                 \frac{\binom{2P}{P}}{4^P}
 \le\frac34(\xi/\alpha)^{P+1}
                    \frac{1+\gamma^{P+1}}{\sqrt{P+1}}}
 \quad(0\le\xi\le\alpha).                            \tag{R9}
\]

Thus the complete original source converges absolutely also at alpha. Monotone convergence of its positive majorant gives r_2(alpha)=3/4 and epsilon_2(alpha)=1/2. The same finite-box derivative summability and positive eigenfunction argument G20–21 identify the sum with the actual vacuum, retaining its scalar. On the common earlier domain both constructions sum identical original coefficients; their identity map and its inverse are literally the identity coefficient by coefficient.

## R4. Return to the complete physical spectrum and the unique volume limit

The original drift bound G23 now has r_2 in place of r, because its proof uses the same coefficient sum. Apply G24–27 to every actual physical eigenfunction, then the full compact spectral resolution. This proves on the closed enlarged domain

\[
 \boxed{
 \Delta_L\ge\frac{3\kappa}{2}(1+\sqrt{P_2(\xi)}),
 \quad 0<\xi\le\alpha,
 \quad g^2\ge\sqrt{(32+\sqrt{354})/3}.}                 \tag{R10}
\]

There is no dependence on L. The full scalar bound is one quarter of R10. In original physical units R10 is

\[
 \Delta_L\ge\frac{3g^2}{a}
       \left(1+\sqrt{1-\frac{64}{3g^4}+\frac{670}{9g^8}}\right).
                                                               \tag{R11}
\]

At the rational benchmark g^2>=17/4,

\[
 \Delta_L\ge\frac{3\kappa}{2}
           \left(1+\sqrt{35401/751689}\right)>1.8255\kappa.
                                                               \tag{R12}
\]

For xi<alpha the complete drift row sum is bounded by

\[
 \sum_{n\ge1}n a_n\xi^n
   =\xi r_2'(\xi)
   =\frac{32\xi-(2680/3)\xi^2}{\sqrt{P_2(\xi)}}<\infty.
\]

Coefficient compatibility and this row sum give exactly the finite-dynamics comparison S13–19 on that domain. The direct finite-semigroup proof S24–28 uses only G23 and now proves the full uniform mixing estimate with epsilon_2. In particular the whole vacuum-measure sequence converges by S29–30; a conditional-influence row smaller than one is not used in this return.

The actual coupling difference is bounded by r_2(eta)-r_2(xi), by the positive recurrence. The same complete Duhamel formula S31–33 consequently gives

\[
 \sup_{t\ge0}\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
 \le\frac{\epsilon_2(\eta)-\epsilon_2(\xi)}{1-\epsilon_2(\xi)}
          \|Q_HF\|_{X_0},\qquad0\le\xi\le\eta\le\alpha. 
                                                               \tag{R13}
\]

At eta=alpha this ratio is sqrt(P_2(xi))/(1+sqrt(P_2(xi))) and tends to zero. Inserting an interior coupling between two endpoint finite boxes, as in S13, proves the whole endpoint dynamics limit. Equation R9 supplies its actual drift convergence; no finite derivative row is assigned at alpha. Uniform mixing makes its limiting vacuum the unique invariant probability of this constructed semigroup, and finite reversibility and physical cylinder density give

\[
 \boxed{A_\infty|_{L^2_{\rm phys}(\nu)\cap1^\perp}
       \ge\frac{3\kappa}{2}(1+\sqrt{P_2(\xi)}),
       \qquad0<\xi\le\alpha.}                         \tag{R14}
\]

The raw physical primitive G30 and physical conditional inverse G31 receive the same stronger bound. The original response pairing and minimum-section correction remain unchanged. The complete band coefficient and its analytic error B10–32 remain valid on their already stated domains; no further band radius is assigned here.

## R5. Actual continuation scope

The final endpoint is approximately g^2=4.1156161030. The old g^2>=15 bound, the first gauge-native g^2>=8/sqrt(3) bound, and R10 refer to the same original Hamiltonian; the explicit coefficient inequalities and their physical return prove the successive gains. The construction at the old source-majorant endpoint is continued by the actual second source rather than by declaring that endpoint a physical singularity.

On the retained path g_n^2=1/c_n, c_n=g_0^-2+beta n log2, the final domain is c_n^2<=3(32-sqrt(354))/670. This follows by rationalizing 3/(32+sqrt(354)); both physical parameters stay those of S31. For beta>0 the path eventually leaves this domain. A nontrivial four-dimensional continuum field and a finite positive continuum mass along that path remain unevaluated.

The next selected source calculation is the actual order-three connected coefficient and full linearized remainder at xi v_[1]+xi^2 v_[2], with its original union labels. The present R2, R6, R9 and R14 are completed inputs to that calculation, not presumed estimates for it.

## R6. Return the coupling comparison to both original physical coefficients

For positive kappa_1,kappa_2 and 0<xi_1,xi_2<=alpha, set
xi_-=min(xi_1,xi_2), xi_+=max(xi_1,xi_2), kappa_+=max(kappa_1,kappa_2),
and e_-=epsilon_2(xi_-), e_+=epsilon_2(xi_+). The full physical inverse
is always g_j^2=1/(2sqrt(xi_j)), a_j=1/(kappa_j sqrt(xi_j)).
The actual vacuum density depends on xi_j; its dependence follows directly
from G20–21, whose energy scalar retains its factor kappa_j.

At one fixed xi the original generators satisfy

\[
 \mathcal A_{\kappa_2,\xi}-\mathcal A_{\kappa_1,\xi}
  =(\kappa_2-\kappa_1)
       \left[K_L-2\sum_i(X_iv_L(\xi))X_i\right].        \tag{R15}
\]

On the nonconstant evolved coefficient y, the full supremum norm of the
bracketed expression is at most (1+epsilon_2(xi))||y||Y. Duhamel's formula,
Markov supremum contraction, and S26 applied to the evolution with kappa_+
therefore bound the integrated coefficient change by
|kappa_2-kappa_1|(1+epsilon_2)/(kappa_+(1-epsilon_2))||Q_HF||X.
Insert the common intermediate coupling xi_- and use R13 for the other
change. This proves the explicit full-parameter estimate

\[
 \boxed{
 \sup_{t\ge0}\|T_{L,\kappa_2,\xi_2}(t)F
                 -T_{L,\kappa_1,\xi_1}(t)F\|_\infty
 \le\left[
      \frac{e_+-e_-}{1-e_-}
      +\frac{|\kappa_2-\kappa_1|}{\kappa_+}
                  \frac{1+e_-}{1-e_-}
      \right]\|Q_HF\|_{X_0}.}                         \tag{R16}
\]

The two evolutions use the same original physical time t. The result holds
for the constructed infinite-volume semigroups by their proved uniform
convergence. All four physical parameters are recovered by the displayed
inverse maps. This comparison has the exact domain R10; it does not assign
itself to the unproved later portion of the running continuum path.


# Unique spatial vacuum and dynamics across the first closed source domain

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-gauge-native-band/SPATIAL_RETURN.md}

\textbf{SHA-256:} \path{b7c24b984cf19ac793ae6df532bfa9fb9db98d6319e1a02bb3b92607366f626e}
\end{quote}


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


# The complete plaquette band, its interaction matrix, and a certified first eigenvalue

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md}

\textbf{SHA-256:} \path{0e02c37b3ecc51f04d2f3c18cca686cc96bc7a8b5fd3bb467b143970a02d7887}
\end{quote}


15 September 2026. All notation is from RESEARCH_NOTE.md G1–31. Energies below retain kappa=2g^2/a. Fourier norms are auxiliary estimates on the original coefficients; the raw physical band Gram is written explicitly in B6. No spin truncation of the Hamiltonian is used.

## B1. Spectral exclusion and an isolated physical band

Let epsilon=(1-sqrt(1-256xi/3))/2 on 0<=xi<=3/256. The estimate G23 yields, on the physical Haar-mean-zero Fourier source,

\[
 \| (\kappa K_L-z)^{-1} V_\xi \|_{Y_0\to Y_0}
 \le\epsilon\sup_{c\in\operatorname{spec}(K_L|_{\rm phys})\setminus\{0\}}
            \frac{\kappa c}{|\kappa c-z|},
 \quad V_\xi=-2\kappa Q_H\sum_i(X_iv(\xi))X_i.            \tag{B1}
\]

All positive physical eigenvalues consequently belong to the union of the intervals

\[
 [\kappa c(1-\epsilon),\kappa c(1+\epsilon)],
 \qquad c\in\operatorname{spec}(K_L|_{\rm phys})\setminus\{0\}. \tag{B2}
\]

For a real point outside the union, the right side of B1 is strictly smaller than one; at large c the quotient tends to one. The same eigenfunction contradiction as G26 proves B2, including the endpoints by closure.

For 0<=xi<3/400, epsilon<1/5. The c=3 interval is separated from all c>=9/2 intervals. The fixed contour

\[
 \mathcal C:\quad |z-3\kappa|=3\kappa/5                 \tag{B3}
\]

has sup kappa c/|kappa c-z|<=5, attained in its free bound at c=3 or c=9/2. It therefore lies in the resolvent set throughout this interval. The entire first physical excitation band is inside this contour and contains exactly |P_L| eigenvalues, including multiplicities. In particular the spectral gap is the lowest eigenvalue in this band. The coupling range is g^2>10/sqrt(3); the endpoint xi=0 is an auxiliary spectral parameter used to fix the rank.

Here is a precise operator justification including that endpoint. On X_0, K_L with domain Y_0 is closed and has compact inverse, since 1/c tends to zero and only finitely many product-spin labels have bounded c. G23 makes V_xi a relatively bounded perturbation with relative bound epsilon<1. The resolvent of kappa K_L+V_xi on the physical mean-zero space is supplied on B3 by the convergent operator Neumann series; its compactness follows from the compact free inverse. Its eigenvectors and generalized eigenvectors are C^2 by the Fourier domain, then smooth by elliptic bootstrapping. The exact G24 map identifies them with the original centered physical operator for real xi. The latter is self-adjoint, so no generalized eigenspace enlargement is introduced by this Banach realization. Conversely all original physical eigenfunctions belong to Y_0 by G23's regularity argument.

The coefficients of v(zeta) are holomorphic for |zeta|<3/256, with the same absolute majorant at |zeta|. Thus the resolvent on B3 and its Riesz projection vary analytically wherever 5epsilon(|zeta|)<1. At zero the projection is the original Haar projection P onto span{W_p}; its rank is |P_L| by G8. Contour-resolvent continuity fixes that finite rank on the stated real interval. This proves the asserted band for the actual Hamiltonian, without requiring a finite spectral cutoff.

## B2. The exact coefficient map and a uniform analytic remainder

Work first on the closed complex disk |zeta|<=rho_*=1/320. Put eta=epsilon(|zeta|). The exact scalar inequality sqrt(11/15)>107/125 gives

\[
 \eta<9/125,\qquad 5\eta<9/25.                           \tag{B4}
\]

Let P_zeta be the Riesz projection from B3, E_zeta=P P_zeta P on the original plaquette space, and

\[
 U_\zeta=P_\zeta P E_\zeta^{-1},\qquad
 A_{\rm band}(\zeta)=P(\kappa K_L+V_\zeta)U_\zeta.        \tag{B5}
\]

No arbitrary frame is chosen: P U_zeta=I, and the original plaquette coefficient vector is the retained coordinate. On this frame the X_0 norm is 8 sum_p|x_p| and the Y_0 norm is 24 sum_p|x_p|, by G14 and orthogonality of the distinct product-spin blocks. Thus induced matrix 1-norms have no omitted frame factor.

To prove E_zeta invertible and compute the remainder constant, expand the contour resolvent using the complete V_zeta. Its zeroth contribution to E_zeta is I. Its one-insertion contribution is the integral of P V_zeta P/(z-3kappa)^2 and is exactly zero. Every term with at least two insertions is bounded on X_0 by its geometric bound. Hence

\[
 \|E_\zeta-I\|_1\le\frac{(5\eta)^2}{1-5\eta},\qquad
 \|E_\zeta^{-1}\|_1\le
       \frac{1-5\eta}{1-5\eta-25\eta^2}.                 \tag{B6}
\]

The denominator is positive by B4. Also

\[
 \|(I-P)P_\zeta P\|_{X_0\to Y_0}
          \le\frac{15\eta}{1-5\eta}.                   \tag{B7}
\]

Indeed its free term is zero. Integrate R_0 V_zeta R_zeta P around the contour: the radius is 3kappa/5, the Q-free resolvent norm into Y_0 is at most 5/kappa, V has norm kappa eta, and the full resolvent on P has norm at most 5/[kappa(1-5eta)] into Y_0. These four factors give B7.

Write b=64/3. The source recurrence implies that V_zeta's first Taylor coefficient has norm at most kappa b, and its higher-coefficient tail at |zeta| has norm at most kappa(eta-b|zeta|), from Y_0 into X_0. Section B3 below proves P V_[1] P=0. Since P U_zeta=I, equations B5–7 give

\[
 \|A_{\rm band}(\zeta)-3\kappa I\|_1
 \le\kappa\left[3(\eta-b|\zeta|)
            +\frac{15\eta^2}{1-5\eta-25\eta^2}\right].  \tag{B8}
\]

For Cauchy's coefficient estimate evaluate B8 on the boundary |zeta|=1/320. There b|zeta|=1/15 and eta<9/125, so

\[
 \|A_{\rm band}(\zeta)-3\kappa I\|_1
 \le\kappa B_*,\quad
 B_*:=3(9/125-1/15)+
       \frac{15(9/125)^2}{1-5(9/125)-25(9/125)^2}
       =\frac{6713}{39875}.                             \tag{B9}
\]

All denominators and signs in this bound are retained. Matrix-valued Cauchy integration now gives the exact expansion

\[
 A_{\rm band}(\xi)=3\kappa I+\kappa\xi^2T_L+\mathcal R_L(\xi),
 \quad
 \boxed{\|\mathcal R_L(\xi)\|_1
       \le\kappa B_*\frac{(320|\xi|)^3}{1-320|\xi|}}
 \quad (|\xi|<1/320).                                   \tag{B10}
\]

This is uniform in the original box size. The first coefficient is exactly zero, and T_L is calculated next. The estimate sums every higher order; it is not a finite-spin replacement or an assumed remainder. The underlying square-root source radius remains 3/256; 1/320 is the explicitly chosen interior contour radius for this numerical bound.

## B3. The full second coefficient with the extensive cancellation retained

Let S=sum_p W_p and M=|P_L|. The unchanged scalar vacuum-energy expansion is

\[
 E_{0,L}(\xi)=2\kappa M\xi-\kappa M\xi^2/3+O_L(\xi^3).
                                                               \tag{B11}
\]

It follows directly from G20–21: v_[1]=S/3, int_H W_pW_q=delta_pq and K_L W_p=3W_p imply int_H sum|Xv_[1]|^2=M/3. The O_L notation in this identity describes its fixed finite box Taylor tail; the band tail itself is the explicit volume-uniform B10.

The first band coefficient vanishes. For all p,q,r, int_H W_p W_q W_r=0. If exactly two indices coincide, an unmatched link of the third face makes the integral zero. If all three coincide, the third fundamental character moment is zero. If three distinct faces occurred without an unmatched edge, each edge of one face would need a different neighboring face; only two others are present. This is impossible because distinct elementary plaquettes share at most one edge. Thus P S P=0. Integration by parts with the three original plaquette Casimirs also proves P V_[1]P=0 in the ground-transformed coefficient system.

On the full original Haar physical space, let Q_3=I-P, so Q_3 includes the constant. Matching the second Taylor coefficient in the original Schrödinger equation gives

\[
 \boxed{T_L=\frac M3 I-P S Q_3
              (K_L-3)^{-1}Q_3 S P.}                    \tag{B12}
\]

The inverse is on Q_3, where its original eigenvalues include -1/3 on the constant and positive inverses for c>=9/2. The term M/3 in B12 is precisely B11's vacuum-energy contribution.

To verify that B12 is also the B5 coefficient, the literal multiplier e^{v(zeta)} intertwines the original Schrödinger operator H_L(zeta)-E_*(zeta) and its ground-transformed operator. Its first multiplier coefficient is v_[1]=S/3, and P v_[1] P=0 by the just-proved triple integral. The additional scalar in G24 lands in the constant block. Thus the P coefficient of this intertwining map is I+O(zeta^2). Conjugating a band matrix whose zeroth coefficient is 3kappa I and whose first coefficient is zero by I+O(zeta^2) changes no second coefficient. Alternatively, its order-one equation is (K_L-3)phi_1=Q_3 Sx for x in P, and projecting its order-two equation gives B12 directly. This proves the complete map and its coefficient-level return rather than assigning the two source formulas the same name.

## B4. Evaluate every intermediate channel

The identities F_p^2=1+chi_1(Omega_p) give two original intermediate components: the constant of Haar norm one and energy zero, and the spin-one plaquette character of Haar norm one and Casimir 8. Distinct spin-one plaquette components are orthogonal.

For p!=q with no shared edge, F_pF_q is an original Casimir eigenfunction of value 6 and Haar norm one, regardless of a shared vertex.

For p,q sharing one edge, retain its original link U. Cyclic trace and inversion of a whole SU(2) trace put the two original words into the form Tr(UA), Tr(U^-1 B), where A and B are their respective ordered three-link path products. Both transformations are literal word identities. The Haar map U,A,B retains independent product Haar, by integrating the original remaining path links successively. Therefore the spin-zero projection at U is

\[
 P_{U,0}(F_pF_q)=\tfrac12\operatorname{Tr}(AB),\qquad
 \|P_{U,0}(F_pF_q)\|_H^2=1/4.                           \tag{B13}
\]

The product has total norm one. The complementary spin-one component at the shared edge consequently has norm squared 3/4, and the two components are orthogonal. The six other original spin-1/2 edges contribute 9/2 to K_L; the shared spin-one edge adds 2. Their exact energies are thus 9/2 and 13/2. Their total resolvent weight at the original band energy 3 is

\[
 \frac{1/4}{9/2-3}+\frac{3/4}{13/2-3}
       =\frac16+\frac3{14}=\frac8{21}.                  \tag{B14}
\]

No pair channel has been omitted. To prove orthogonality for distinct unordered pairs, use independent central sign changes of the original links. The half-integer spin support of F_pF_q is the mod-two symmetric difference of the two face boundaries. Equality for two different unordered pairs would yield a nonzero mod-two sum of at most four elementary faces with zero boundary. Each of the four edges of any included face would require a different other face, giving at least five faces. Hence equality is impossible. Orthogonality follows from the actual sign-changing Haar substitution. The self-pair channels have even center parity and are separated from these distinct-pair channels; their nonconstant parts were already separated by their spin support.

Write p~q for shared-edge adjacency and d_p=#{q:q~p}. Substituting all channels into B12 gives

\[
 \boxed{(T_L)_{pp}=\frac7{15}-\frac{d_p}{21},\qquad
 (T_L)_{pq}=\begin{cases}-1/21,&p\sim q,\\0,&p\not\sim q,\ p\ne q.
 \end{cases}}                                          \tag{B15}
\]

For clarity, the unreduced diagonal calculation is

\[
 \frac M3+\frac13-\frac15
   -\frac{M-1-d_p}{3}-\frac{8d_p}{21}.
\]

For a nonadjacent off-diagonal pair its terms are +1/3 from the constant and -1/3 from the actual two-plaquette intermediate. For an adjacent pair they are +1/3 and -8/21. These equalities retain each canceled extensive or off-diagonal contribution as its original intermediate channel.

Let A_adj be this adjacency matrix and D_deg=diag(d_p). The exact operator statement is

\[
 T_L=\frac7{15}I-\frac1{21}(D_{\rm deg}+A_{\rm adj}).     \tag{B16}
\]

All open-boundary degrees remain; replacing d_p by twelve changes the actual finite matrix.

## B5. Boundary-sensitive bounds, the full physical lower edge, and one original-box certificate

Each elementary plaquette has d_p<=12. The complete column sum of the absolute entries in T_L is at most 71/105. Indeed at degree d the sum is |7/15-d/21|+d/21; for d<=9 it equals 7/15 and for 10<=d<=12 its largest value is 71/105. Gershgorin's bound for B10, with its whole column residual, consequently proves

\[
 \boxed{\Delta_L\ge\kappa\left[
       3-\frac{71}{105}\xi^2
         -B_*\frac{(320\xi)^3}{1-320\xi}\right],
       \quad 0<\xi<1/320.}                              \tag{B17}
\]

The gap belongs to the band by B1. This lower bound uses the entire actual physical spectrum, not the Rayleigh quotient of one observed vector. G26 remains simultaneously available. At xi=10^-8, integer/rational evaluation gives

\[
 \boxed{\Delta_L>\kappa(3-7.314\,10^{-17})
          \quad\hbox{for every }L\ge2.}                 \tag{B18}
\]

No matrix minimum is formed between the two different lower-bound arguments.

The degree count is exact. Put m=2L. There are M=3m^2(m+1) faces, and the edge incidence values 4,3,2 occur respectively 3m(m-1)^2, 12m(m-1), 12m times. Since a pair of distinct faces shares at most one edge,

\[
 \sum_p d_p=12m(3m^2-1),\qquad
 \overline d=\frac{4(3m^2-1)}{m(m+1)}.                   \tag{B19}
\]

The original constant coefficient vector on all M plaquettes has squared Haar norm M. In B16 it therefore gives

\[
 -\frac{71}{105}\le\lambda_{\min}(T_L)
 \le\frac7{15}-\frac{2\overline d}{21}
 =-\frac{71}{105}+\frac{8(3m+1)}{21m(m+1)}.              \tag{B20}
\]

This evaluates the large-box limit of the actual second coefficient with an explicit boundary remainder. It does not interchange that coefficient limit with a varying-coupling spectral limit.

The checker additionally computes the full original L=2 matrix, containing 240 plaquettes. Let Q_L=D_deg+A_adj. Starting with the original vector x_0=(1,...,1), it computes x_100=Q_L^100 x_0 by integer multiplication. All entries are positive. The minimum and maximum of (Q_L x_100)_p/(x_100)_p enclose its largest eigenvalue: the upper bound is the row-sum bound after diagonal conjugation by diag(x_100); the lower bound follows either by the positive Perron vector or by the Rayleigh quotient. Q_L is symmetric nonnegative and its graph is connected. Direct exact computation returns

\[
 21.86319640514<\lambda_{\max}(Q_L)<21.86319641826,
\]
\[
 -0.57443792469<\lambda_{\min}(T_L)<-0.57443792405.        \tag{B21}
\]

A separate fraction-free symmetric congruence of Q_L-21I has inertia (1 positive,239 negative,0 zero). Every integer division and all 240 pivot determinants are retained in BOX_L2_CERTIFICATE.json. At stage k the exact symmetric Schur step is

\[
 a_{ij}^{\rm new}=(a_{kk}a_{ij}-a_{ik}a_{jk})/d_{k-1},
\]

with d_-1=1 and d_k the current pivot; the actual pivot of the ordinary Schur complement is d_k/d_(k-1). Congruence by unit triangular elimination proves that their signs give the stated inertia. No numerical eigenvalue routine is used for this certificate. It proves that every other eigenvalue of T_L is greater than -8/15.

On 240 by 240 matrices, ||R||_2<=sqrt(240)||R||_1<16||R||_1. At the actual coupling xi=10^-10, B10 therefore bounds the perturbation in (A_band-3kappa)/(kappa xi^2) by

\[
 \delta_*:=16B_*\frac{320^3\xi}{1-320\xi}<0.008827.       \tag{B22}
\]

Use the fixed contour of radius 1/50 around -574438/10^6. B21 and the just-certified other-eigenvalue bound put this contour at distance greater than delta_* from the spectrum of the Hermitian T_L. Resolvent Neumann expansion along the finite interpolation T_L+t(A_band-3kappa-kappa xi^2T_L)/(kappa xi^2) preserves its rank-one spectral projection. The actual band eigenvalues are real by Section B6 below. Normal-resolvent distance bounds place the single eigenvalue in the B21 interval enlarged by delta_*, while every other band eigenvalue is above -8/15-delta_*. The single eigenvalue is thus the original spectral gap. The final outward rational bounds are

\[
 \boxed{
 \kappa(3-0.5833\xi^2)<\Delta_{L=2}<\kappa(3-0.5656\xi^2),
 \quad \xi=10^{-10},\quad g^2=50000,\quad\kappa=100000/a.
 }                                                        \tag{B23}
\]

This certificate concerns the full interacting Hamiltonian in the original L=2 box, for every a>0. Its analytic remainder contains every Fourier spin and every higher perturbative order. The auxiliary 240 by 240 matrix is the exact second Taylor coefficient, not a truncation declared to equal the Hamiltonian.

## B6. The original band metric and its intertwining map

For real xi in B5's domain, let y=U_xi x in the original Haar coefficient source, and define

\[
 \mathcal R_\xi x
   =\psi_L\left[y-\langle y\rangle_{\rho_L}\right],\quad
 G_\xi=\mathcal R_\xi^*\mathcal R_\xi.                    \tag{B24}
\]

The map is injective because P U_xi=I and the only removed functions are constants. It is onto the complete first physical band: the Riesz range and G24 give the inverse by taking its original Haar plaquette coefficients after dividing by psi_L. Thus G_xi is the actual positive Gram in these prescribed coefficient coordinates. At zero its value is I because int_H W_pW_q=delta_pq, a calculated source identity.

The exact operator and energy identities are

\[
 (H_L-E_{0,L})\mathcal R_\xi=\mathcal R_\xi A_{\rm band}(\xi),
 \quad E_\xi=\mathcal R_\xi^*(H_L-E_{0,L})\mathcal R_\xi
             =G_\xi A_{\rm band}(\xi)
             =A_{\rm band}(\xi)^*G_\xi.                 \tag{B25}
\]

The inverse on the Riesz image and all physical pairings are retained. This proves the claimed reality of the actual band spectrum and exhibits the self-adjoint Hamiltonian comparison without replacing G_xi by an identity matrix.

## B7. Complete second-order spatial propagation in the original lattice coordinates

On the infinite cubic plaquette graph, index a plaquette by its normal axis a in {1,2,3} and base n in Z^3. Its center is n+c_a, with c_a=(e_b+e_c)/2 for the other axes b,c. The Fourier map and inverse are

\[
 (\mathcal F x)_a(k)=\sum_nx_{a,n}e^{-ik\cdot(n+c_a)},\quad
 x_{a,n}=\frac1{(2\pi)^3}\int_{[-\pi,\pi]^3}
            e^{ik\cdot(n+c_a)}(\mathcal Fx)_a(k)\,dk.     \tag{B26}
\]

Orthogonality of the original exponentials proves the isometry with the displayed measure. The components retain their boundary phase under k_i->k_i+2pi: e^(-2pi i(c_a)_i). This records the half-link center coordinates rather than discarding them.

Counting the actual shared links gives Q(k)=12I+A(k), with

\[
 A_{aa}(k)=2\cos k_b+2\cos k_c,\qquad
 A_{ab}(k)=4\cos(k_a/2)\cos(k_b/2)\quad(a\ne b),
 \quad T(k)=\frac7{15}I-\frac1{21}Q(k).                 \tag{B27}
\]

For the four perpendicular neighbors of a,b their relative center displacements are (+/-e_a+/-e_b)/2; summing their four exponential factors proves the off-diagonal formula. The four coplanar displacements are +/-e_b,+/-e_c, proving the diagonal formula. These are the actual adjacency maps of B16, now at every retained spatial momentum.

At k=0 the raw vector (1,1,1), of squared norm 3, has T-eigenvalue -71/105. Its coefficient-orthogonal plane x_1+x_2+x_3=0 has eigenvalue -11/105. On the fundamental cube all cos(k_a/2)>=0 and every row sum of Q(k) is at most 24; the maximum 24 is attained at k=0. Hence the bottom of the complete second-coefficient spatial operator is exactly -71/105.

The simple lowest branch has the Taylor expansion

\[
 t_{\rm low}(k)=-\frac{71}{105}+\frac4{63}|k|^2+O(|k|^4). \tag{B28}
\]

For a direct calculation, the diagonal quadratic change of A is -(k_b^2+k_c^2), and its a,b off-diagonal change is -(k_a^2+k_b^2)/2. Their full sum divided by the raw squared norm 3 is -(4/3)|k|^2. The other two eigenvalues are separated at zero, all matrix first derivatives there vanish, and the finite eigenvalue equation consequently gives B28; the eigenvector correction first contributes at fourth order. All original spatial directions remain.

With physical momentum p and k=ap, the corresponding exact Taylor coefficients of the energy band are

\[
 3\kappa-\frac{71}{105}\kappa\xi^2
       =\frac{6g^2}{a}-\frac{71}{840g^6a},\qquad
 \frac4{63}\kappa\xi^2a^2|p|^2=\frac{a}{126g^6}|p|^2.  \tag{B29}
\]

These are coefficients of the original strong-coupling band. B10 controls its full finite-box analytic remainder; B20 controls the large-box second coefficient. Neither a relativistic dispersion relation nor an exchange of the small-xi, volume and a->0 limits is asserted.

## B8. A primary-source coefficient check with the physical dictionary retained

A separate final source check located the planar coefficient in Bernd Dahmen,
*Strong coupling expansion for scattering phases in hamiltonian lattice field
theories. II. SU(2) gauge theory in (2+1) dimensions*, DESY 94-236,
arXiv:hep-lat/9412080, equations (1.7)–(1.11), Figure 1.3 and (1.26)–(1.29).
The original PDF pages 3, 4, 9 and 10 were inspected, including the graph signs.
This is a local-coefficient comparison; no three-dimensional remainder bound
is imported from that paper.

On the same planar graph, write its hopping coefficient as h_D, its coupling
as g_D, and its unscaled Hamiltonian as H_D'. The exact physical dictionary is

\[
 h_D=\xi,\qquad g_D=2^{3/4}g,\qquad
 H_{\rm plane}(a,g)=\frac{\sqrt2}{a}H_D'(g_D)
                        +2\kappa\xi M I.               \tag{B30}
\]

Indeed h_D=2/g_D^4=1/(4g^4), while
(sqrt(2)/a)(g_D^2/2)=2g^2/a=kappa. The Casimir identity
(n^2-1)/4=j(j+1) uses n=2j+1, and the original plaquette word is
identical under the original link labels. Thus B30 is equality of the
operators on the common planar-link domain, retaining its energy multiplier
and additive scalar. Ground-energy differences retain the multiplier.
The comparison at a periodic planar graph uses that graph on both sides;
it assigns no periodic boundary to the original open three-dimensional box.

On the planar plaquette graph the bulk degree is four. Repeating B12–16
with those actual incidences gives

\[
 T_{\rm plane}=\frac{29}{105}I-\frac1{21}A_{\mathbb Z^2},
 \qquad
 t_{\rm plane}(k)=\frac3{35}
                   +\frac{4-2\cos k_1-2\cos k_2}{21}.  \tag{B31}
\]

These are precisely the source's second coefficient and momentum coefficient
under B30. The common self and neighboring contributions have the original
values 2/15 and -8/21 in its Figure 1.3, as calculated in B12–14.

For the relation to the three-dimensional coefficient, let J_plane insert the
coefficients of one fixed plane and orientation into the full infinite
plaquette array, with zero on all other faces. Its adjoint reads precisely
those coordinates, so J_plane* J_plane=I. Each such face has its four planar
neighbors and eight perpendicular neighbors. Consequently

\[
 J_{\rm plane}^*T_{\mathbb Z^3}J_{\rm plane}
           =T_{\rm plane}-\frac8{21}I,
 \quad
 ((I-J_{\rm plane}J_{\rm plane}^*)T_{\mathbb Z^3}J_{\rm plane}x)_q
       =-\frac1{21}\sum_{\substack{p\ {
m in\ plane}\p\sim q}}x_p.
                                                               \tag{B32}
\]

The second equation retains the complete coupling to the other plaquettes.
The three-dimensional lowest coefficient -71/105 comes from B27's complete
three-component matrix, not from deleting that coupling. This source check
supports the local matrix arithmetic and preserves the antecedent's credit.


# Volume-uniform physical coercivity and the actual zero-shift Wilson response

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-uniform-gap-zero-shift/RESEARCH_NOTE.md}

\textbf{SHA-256:} \path{83d4de98b7b3e5de85efd747f56f1a42261cc55570e419c0d8fe62ccab93bad8}
\end{quote}



**Final completed estimate.** `HEAT_BATH_GAP.md` proves the full original
physical bound Delta_L>=kappa/100 for g^2>=15, and the stronger
Delta_L>=(3/20)kappa for g>=4. Its coupling-dependent value H12 controls
the actual zero-shift response and the unique full spatial-volume dynamics.
All physical constants and the actual conditional measure remain explicit.

**Independent curvature estimate.** `OPTIMIZED_DOMAIN.md` evaluates the exact original
plaquette Fourier coefficient and the full scalar majorant. It proves the
stronger full physical lower bound O13 for g^4>138240/451, including
Delta_L>=(3/20)kappa for every g>=9/2. Its zero-shift and full spatial-volume
returns are O19–26. The baseline constants below are preserved for audit.

15 September 2026. Additive continuation of the delivered
`20260915-actual-loop-moments` calculation. Its remote ancestor is Yang–Mills
PR6, `e98b2c3af77f66fb1c1396143ca53daef586404f`. The delivered predecessor is
identified by its own SHA-256 and is not assigned an invented remote commit.

## Results and exact scope

For every original open box L>=2, every a>0, and every **g>=8**, retain

    kappa=2g^2/a, v=1/(2g^2 a), xi=1/(4g^4).

The complete physical excitation gap satisfies

    Delta_L >= kappa(1/2-6144 xi) >= kappa/8.                  (U1)

The proof constructs the actual vacuum logarithm in a support-labelled
Fourier source, controls its full mixed second-derivative matrix, and returns
that bound to the original physical energy. No finite spin or observable
cutoff supplies the lower bound.

At xi=10^-8, equivalently g^2=5000 and kappa=10000/a, the elementary-loop
forcing W and full conditional-kernel operator D of the predecessor satisfy

    |<W,D^-1 W>_rho - (8/39) kappa xi^2|
         < 0.0000094 kappa xi^2,
    | ||D^-1 W||_rho^2 - (196/4563) xi^2 |
         < 0.0000041 xi^2.                                  (U2)

These are enclosures of the **actual zero-shift response**, uniform over all
exterior boxes L>=2. The finite remainder formulas are in U36–43. Section 9
controls both spectral endpoints in the volume limit at fixed a and g>=8,
producing a nonzero gapped limiting correlation generator. The spacing and
coupling path of the four-dimensional continuum program remains explicit in
section 10; no continuum mass lower bound is asserted here.

Fourier-algebra multiplication, contraction mapping, and the integrated
second-derivative spectral argument are classical methods. The present
calculation supplies the original-operator maps, support estimates, constants,
and physical response enclosures. No historical-priority claim is made.
Executable finite checks accompany the written analytic proof; they do not
constitute a formal verification of its infinite-dimensional assertions.

## 1. The unchanged operator, state, and energy form

The vertices are {-L,...,L}^3. E is the set of all contained positive edges
and P the set of all contained elementary faces. Use the original matrices
T_alpha=-i sigma_alpha/2 and derivatives

    X_e,alpha f(U)=d/dt f(...,exp(t T_alpha)U_e,...) at t=0,
    K=-sum_(e,alpha)X_e,alpha^2,
    V=v sum_(p in P)(2-W_p), H=kappa K+V.                   (U3)

W_p is its complete oriented four-link fundamental trace. Reverse traversal
uses the inverse of that same link. The scalar 2v|P| is retained. Every dU
below is the original product Haar probability measure. In the source metric
c(T_alpha,T_beta)=delta_alpha,beta/4 the operator uses its original factor;
all following derivatives continue to be the original X with coefficient kappa.

The full scalar compact-group operator has domain H^2, form domain H^1,
compact resolvent and a unique smooth positive unit ground state psi [YM].
It is gauge invariant; the physical spaces are the invariant parts. Put
u=log psi, rho=psi^2 and b_i=X_i u, where i=(e,alpha). Multiplication f->psi f
and its inverse h->h/psi give

    A=psi^-1(H-E0)psi=-kappa L,
    L=sum_i X_i^2+2 sum_i b_i X_i,
    q_A(f,h)=kappa int rho sum_i conjugate(X_i f)X_i h.      (U4)

The scalar ground energy E0 and unit state are those of the complete H.
No new state or energy pairing replaces U4.

## 2. Original Fourier coefficients, labelled supports, and a local product bound

### 2.1 All original representation labels

For each edge keep j_e in {0,1/2,1,...}. The product representation pi_j has

    d_j=product_e(2j_e+1), c_e(j)=j_e(j_e+1),
    c(j)=sum_e c_e(j), S(j)={e:j_e>0}.                      (U5)

For explicit generator coordinates let J_3|m>=m|m>,
J_+|m>=sqrt((j-m)(j+m+1))|m+1>, J_-=J_+^*,
J_1=(J_++J_-)/2 and J_2=(J_+-J_-)/(2i). Then d pi_j(T_alpha)=-i J_alpha.
Multiplication gives sum J_alpha^2=j(j+1)I; rotations in this same unitary
representation give ||J_alpha||op=j. Thus the original K acts by c(j),
retaining its 3/4 value on a spin-1/2 factor.

Use the coefficient convention

    f(U)=sum_j Tr(A_j pi_j(U)),
    A_j=d_j int f(U)pi_j(U)^*dU.                           (U6)

Matrix-entry orthogonality proves the inverse formulas and uniqueness.
In particular the trivial coefficient is int f dU. Write a_j=||A_j||_1,
the trace norm of the complete coefficient matrix. Then

    |Tr(A_j pi_j(U))|<=a_j,
    ||X_e,alpha Tr(A_j pi_j)||Fourier<=j_e a_j,
    ||X_f,beta X_e,alpha Tr(A_j pi_j)||Fourier<=j_e j_f a_j. (U7)

The Fourier norm here is sum_j ||A_j||_1, with the d_j already present in U6.
These standard compact-group Fourier coordinates are described in [FA].
Their use here estimates derivatives of the original state and does not
alter the physical measure or inner product.

Here is a coefficient proof of the product bound used below. A product of
two summands is

    Tr((A_j tensor B_k)(pi_j tensor pi_k)(U)).

A unitary decomposition of pi_j tensor pi_k into irreducibles retains all
multiplicity spaces. The coefficient of an output irreducible is the partial
trace over its multiplicity space of the corresponding diagonal block.
For such a block C, trace-norm duality gives

    ||Tr_m C||_1=sup_(||Z||op<=1)|Tr((Z tensor I_m)C)|<=||C||_1.

Pinching into all diagonal blocks is an average of unitary conjugations
using the roots of unity as block phases. Its trace norm is at most the
original one by the triangle inequality. Since the trace norm of a tensor
product is the product of its trace norms, the full coefficients satisfy

    sum_output ||C_output||_1<=a_j b_k.                    (U8)

Every output active support is contained in S(j) union S(k). All its
coefficients and multiplicities remain. Absolute summability extends U8 to
the stated Fourier series by norm and uniform convergence.

### 2.2 The support source and its exact assembly kernel

For every nonempty edge label S retain a local zero-Haar-mean function
f_S=sum_(j nontrivial, S(j) subset S)Tr(A_(S,j)pi_j). An inactive edge may
remain in S after a coefficient cancellation. The declared observation is

    Assembly((f_S))=sum_S f_S,
    (Assembly A)_j=sum_(S containing S(j)) A_(S,j).          (U9)

Use the auxiliary source norm

    ||f||loc=max_(e in E) sum_(S containing e)
                      2^|S| sum_(j nontrivial)c(j)||A_(S,j)||_1. (U10)

For the finite graph this is a complete norm on the coefficient families.
The total c-weighted coefficient sum is at most |E| ||f||loc; U7 therefore
supplies uniform convergence of the assembled function and of all original
first and second derivatives. The physical form remains U4.

The kernel of Assembly consists exactly of the coefficient equations
sum_S A_(S,j)=0 for every nontrivial j. Its complete primitive presentation
is explicit. For S strictly containing S(j), define

    d(S,j,B)=(B at (S,j))-(B at (S(j),j)).                  (U11)

Assembly d=0. Given a kernel family, use its A_(S,j) as incoming coefficients
at every S != S(j). Their boundaries recover those components. The remaining
S(j) component is their negative sum, which is exactly its original component
by the kernel equation. This constructs an inverse presentation and proves
ker Assembly=im d, without erasing any old label. The sums converge in the
finite-graph source norm: there are finitely many labels and lowering a label
only lowers its exponential weight.

### 2.3 The nonlinear bound without an exterior-volume factor

Let P_H be the original Haar-constant projection, Q_H=I-P_H, and let K^-1 on
the nontrivial Fourier source multiply its j coefficient by 1/c(j). Define

    B(f,h)_S=K^-1 Q_H sum_(S1 union S2=S) sum_(e,alpha)
                      (X_e,alpha f_S1)(X_e,alpha h_S2).    (U12)

Each output has its actual union label. The removed trivial Fourier coefficient
is retained as a scalar at that label; the sum of those scalar coefficients
will determine the original ground energy in U17.

For every spin label,

    j_e<=(2/3)c(j), sum_e j_e<=(2/3)c(j).                   (U13)

Indeed j(j+1)*(2/3)-j=j(2j-1)/3>=0 for every nonzero spin.
For an anchor a in S1, U7–8 and 2^|S1 union S2|<=2^|S1|2^|S2| give the bound

    3 sum_(S1 containing a,j)2^|S1| ||A_(S1,j)||_1
       sum_e j_e sum_(S2 containing e,k)2^|S2| k_e||B_(S2,k)||_1
      <=(4/3)||f||loc ||h||loc.

The inner sum is at most (2/3)||h||loc by U13, and sum_e j_e is at most
(2/3)c(j). The factor three retains every generator component. Contributions
with a in S2 have the same bound with f and h exchanged. Counting both is an
upper bound also on their overlap. Finally, the c(output) in U10 cancels
exactly its inverse multiplier in U12. Thus

    ||B(f,h)||loc<=(8/3)||f||loc ||h||loc.                  (U14)

All sums are absolutely convergent under these estimates. No constant depends
on |E|, and every active and retained support is present.

## 3. Construction of the actual vacuum and its full Hessian bound

Assign (xi/3)W_p to its four-edge label boundary(p). Its Casimir is 3.
The original four-link trace expands into sixteen signed products of fundamental
entries. The exact inverse formula U^-1=epsilon U^T epsilon^-1,
epsilon=[[0,1],[-1,0]], expresses every inverse entry as a signed original
entry. Each product is a coefficient matrix unit in the tensor product of four
spin-1/2 representations and has trace norm one. Thus ||W_p||Fourier<=16.
At most four plaquettes meet an original edge. The complete labelled source is

    f^(1)=(xi/3)sum_p W_p, ||f^(1)||loc<=4*2^4*16*xi
         =1024 xi=:b_0.                                  (U15)

Its assembly is precisely the predecessor's first local term u_0. Keep the
full nonlinear iteration

    F(f)=f^(1)+B(f,f), f^(0)=0, f^(m+1)=F(f^(m)),
    R=2048 xi=2b_0.

For 0<xi<=1/16384, R<=1/8. U14 gives, on the closed R-ball,

    ||F(f)||loc<=R/2+(8/3)R^2<=(5/6)R,
    ||F(f)-F(h)||loc<=(16/3)R||f-h||loc<=(2/3)||f-h||loc.   (U16)

The iterates are Cauchy by summing their geometric successive differences.
Completeness gives the fixed point in this ball, unique there. Every iterate
is real and gauge invariant: the source, Casimir, Haar projection and the
complete generator contraction commute with the original gauge action.
Their assembled limit v_* has the same properties and original derivatives.

Let C_S be the removed scalar of U12 at this fixed point, and let
C=sum_S C_S=int sum_i(X_i v_*)^2dU. The actual assembled equation is
K v_*=xi sum_p W_p+sum_i(X_i v_*)^2-C. Retain the scalar coordinate

    c_*=-(1/2)log int exp(2v_*)dU,
    psi_*=exp(v_*+c_*), E_*=2v|P|-kappa C.                 (U17)

The original constant 2v|P| and all removed scalar contributions remain.
The coordinate map on a positive unit function is
psi -> (Q_H log psi,P_H log psi); U17 reconstructs this particular solution
with its original unit norm and measure. No scalar from that state is dropped.

Uniform convergence of second derivatives gives a C^2 solution v_* of the
assembled equation. The right side is C^1, hence locally Hölder. Elliptic
regularity gives C^(2,alpha) and repeated regularity of this same equation
gives smoothness. Direct differentiation proves H psi_*=E_* psi_*. Moreover
for every smooth h,

    q_(H-E_*)(psi_*h)=kappa int psi_*^2 sum_i |X_i h|^2>=0.

Multiplication by psi_* and its inverse preserve H^1 on this compact finite
graph. The identity proves E_* is the lowest energy. The source uniqueness
therefore identifies psi_*=psi, E_*=E0 and v_*+c_*=log psi. The iteration has
constructed the original interacting vacuum, rather than an auxiliary one.

Let J_(e,f) have entries X_e,alpha X_f,beta u and S_u=(J+J^T)/2. U7 implies

    ||J_(e,f)||op<=3 sum_(S containing e,f,j)j_e j_f||A_(S,j)||_1.

For n active edges of a coefficient, applying 2ab<=a^2+b^2 to each f != e gives

    j_e sum_f j_f<=((n+1)/2)sum_f j_f^2<=((|S|+1)/2)c(j).

The same symmetric block majorant controls J and its symmetric part. Since
(|S|+1)/2^|S|<=1 for every nonempty label, each full block-row sum is at most
(3/2)R. The symmetric Schur row bound follows directly from
2|x_e||x_f|<=|x_e|^2+|x_f|^2. It proves the pointwise, full-matrix estimate

    ||S_u||op<=(3/2)R=3072 xi.                            (U18)

The construction's nonzero labels are connected in the line graph of original
edges. Plaquette boundaries are connected and a nonzero product in U12 has
a shared derivative edge. Thus for integer d>=0, the same estimate restricted
to f at line-graph distance at least d from e gives

    sum_(f:dist(e,f)>=d)||(S_u)_(e,f)||op
      <=(3/2)R (d+2)/2^(d+1).                            (U19)

Each contributing connected S has |S|>=d+1; (m+1)/2^m decreases for m>=1.
This spatial estimate keeps every cross-link block and its original support.

## 4. Coordinate-level proof of full physical coercivity

For real smooth f set Gamma(f)=sum_i(X_i f)^2. The original bracket is
[X_e,alpha,X_e,beta]=-epsilon_alpha,beta,gamma X_e,gamma and the Casimir
commutes with each X_j. Differentiating L in U4 gives exactly

    Gamma_2(f):=(1/2)L Gamma(f)-sum_j(X_j f)X_j Lf
      =sum_(i,j)(X_i X_j f)^2
         -2 sum_(i,j)(X_j f)(X_j X_i u)(X_i f).             (U20)

The intermediate bracket term is
2 sum_(i,j,k)b_i(X_j f)c_(ij)^k(X_k f). On each edge its epsilon coefficient
is antisymmetric in j,k while the derivative product is symmetric, so the
term is exactly zero. The antisymmetric part of J_u also contracts to zero;
the retained part is S_u with its entire mixed matrix.

For each original edge the antisymmetric part of [X_e,alpha X_e,beta f]
has squared Frobenius norm (1/2)sum_alpha(X_e,alpha f)^2, by the same bracket
calculation. The symmetric parts and all other blocks contribute nonnegative
squares. Therefore U18–20 give

    Gamma_2(f)>=(1/2-6144 xi)Gamma(f)=:d_xi Gamma(f),
    d_xi>=1/8 on 0<xi<=1/16384.                           (U21)

This retains the original curvature coefficient 1/2 and the full drift cost.
Integration in the actual invariant density rho gives
int rho Lh=0, int rho conjugate(f)Lh=-int rho sum conjugate(Xf)Xh, hence

    int rho Gamma_2(f)=int rho(Lf)^2.                      (U22)

Every nonconstant eigenfunction of the original scalar A is smooth; use a real
basis of its eigenspace, or apply the identity to real and imaginary parts.
For A f=lambda f, U22 reads int Gamma_2=(lambda/kappa)int Gamma. The latter
integral is positive. Thus lambda>=kappa d_xi. The complete compact spectral
resolution then gives on the full original form domain

    q_A(f)>=kappa d_xi (||f||_rho^2-|<1,f>_rho|^2).         (U23)

Restricting this inequality to the gauge-invariant domain proves U1, or in
unchanged physical parameters

    Delta_L>=(g^2-3072/g^2)/a, g>=8.                      (U24)

The centered gradient primitive p(df)=f uses the original source norm
||df||energy^2=kappa int rho sum|Xf|^2. Its exact variational characterization is

    ||p||^2=1/Delta_L<=1/(kappa d_xi).                     (U25)

This includes all centered physical vectors and regulator-dependent choices
of vector, as well as the previously retained finite observation families.

## 5. Support tails and a genuine volume extension

Keep a>0,g>=8 fixed. The fixed point has the completely specified coefficient
series

    v_[1]=K^-1 sum_p W_p (with original plaquette labels),
    v_[p]=sum_(j=1)^(p-1)B(v_[j],v_[p-j]),
    v_*=sum_(p>=1)xi^p v_[p].                             (U26)

Each order-p label is a union of p original plaquettes joined by shared edges.
The union recursion proves |S|<=3p+1. Each representation has j_e<=p/2 by
tensor-product decomposition; there are finitely many terms touching a fixed
edge at this fixed order. Let C_m=binom(2m,m)/(m+1). Its quadratic recurrence,
U14 and U15 prove

    ||xi^p v_[p]||loc<=C_(p-1)(8/3)^(p-1)(1024xi)^p.

Since C_m<=4^m, theta=(32768/3)xi<=2/3 gives the actual convergent tail

    ||sum_(p>P)xi^p v_[p]||loc
       <=1024xi theta^P/(1-theta).                        (U27)

No finite order replaces the full Hamiltonian. At a fixed edge all coefficients
through order P are identical in every box containing its line-graph ball of
radius 3P. This follows from U26's support unions. The original derivatives
b_e^L=X_e log psi_L consequently have a uniform limit on the full countable
configuration product. The finite/infinite difference has the explicit bound

    |b_e^L-b_e^infinity| <= (4/sqrt(3))1024xi theta^P/(1-theta) (U28)

when that ball is contained. Each of the two tails uses
|X_e f|<=(2/sqrt(3))||f||loc from U7 and U13.

Extend the finite vacuum probability by original independent Haar factors
outside its box. Compactness of the countable SU(2) product and diagonal
selection on its matrix-entry cylinder algebra give weak subsequential limits
nu. The original gauge invariance passes to every limit. For smooth cylinders,
finite-volume integration by parts and U28 prove

    int X_i f dnu=-2 int b_i^infinity f dnu.                (U29)

Each limiting drift is bounded and continuous, being a uniform limit of the
specified local functions. No density relative to the infinite Haar product
is asserted or needed for U29.

The original cylinder form has a closed realization. Define df=(X_i f)_i
with target the Hilbert direct sum of the original L^2(nu) components. For
f_n->0 in L^2 and df_n->h in the direct sum, U29 against a cylinder test w gives

    <w,h_i>=-lim_n<X_i w+2 b_i^infinity w,f_n>=0.

Density of cylinders proves h=0. Thus d is closable. The form
q_infinity=kappa||closure(d)||^2 is closed and nonnegative; the chain rule and
closure give its Markov property. Passing U23 on cylinders to nu and closing
gives its full centered lower bound kappa d_xi. Section 9 constructs the
limiting correlation generator directly from finite-vacuum observations and
gives an explicit form comparison with this realization.

## 6. The full conditional kernel now has an inverse at zero

Use the elementary square at the origin, its ordered holonomy Omega, and
F=tr Omega from [ALM, A15–20]. The coordinate map

    (V1,V2,V3,V4,U_out)->(Omega=V1 V2 V3 V4,V1,V2,V3,U_out)

has inverse V4=(V1 V2 V3)^-1 Omega and preserves product Haar. Its actual maps are

    m(Omega)=int rho(Omega,z)dz,
    E f=m^-1 int rho f dz, Jf=f(Omega), Q=I-JE.             (U30)

E=J*, EJ=I in the original pairings. Every member of Kcal=ker E has global
rho mean zero. The closed restricted form from [ALM, A18–20] represents D.
U23 therefore proves on that full kernel

    D>=kappa d_xi I,
    ||(D+s)^-1||<=1/(kappa d_xi+s), s>=0.                  (U31)

Exterior and additional coarse fluctuations are included. This proves the
zero-shift inverse on the actual Hilbert kernel, without replacing it by a
trial subspace. Define W=-Q A F=2kappa Qj, where
j=sum_(e in C,alpha)b_e,alpha X_e,alpha F. For any actual Y in Dom(D), set
R=W-DY. Expanding the full residual square gives

    M0:=<W,D^-1W>=2 Re<W,Y>-q_D(Y)+<R,D^-1R>,
    0<=<R,D^-1R><=||R||^2/(kappa d_xi),
    ||D^-1W-Y||^2=<R,D^-2R><=||R||^2/(kappa d_xi)^2.        (U32)

These are full Gram identities for any finite family of columns as well.
On the actual spectrum lambda>=kappa d_xi the resolvent multipliers give

    0<=M0-Ms<=[s/(kappa d_xi)]M0,
    ||(D+s)^-1W-D^-1W||
       <=[s/(kappa d_xi+s)]||D^-1W||, s>=0.                (U33)

Thus the positive shift can be taken to zero with a uniform error on the
stated coupling domain.

## 7. Original local zero-shift trial and every error term

Retain the twelve neighboring plaquettes and their full original contractions
j_p from [ALM, A27–30]. The explicit singlet/triplet components sum to J0,J1,
and J=J0+J1, with

    KJ0=(9/2)J0, KJ1=(13/2)J1,
    ||J0||_H^2=27/16, ||J1||_H^2=9/16, <J0,J1>_H=0.        (U34)

Each unequal-plaquette cross term has an original unmatched-link Haar witness.
These are exact local polynomial identities; their interacting measure return
is bounded below. Define

    U=(2/3)J,
    Z=(4/27)J0+(4/39)J1=(4/39)J+(16/351)J0,
    z=xi Z, Y=Qz.                                        (U35)

U34 gives KZ=U and the complete coefficients

    <U,Z>_H=m_*=8/39,
    ||Z||_H^2=z_*=196/4563.                               (U36)

For example m_*=(3/4)/(9/2)+(1/4)/(13/2), retaining both components.
The original local suprema in [ALM, A31,A41] give

    ||U||infinity<=8,
    ||Z||infinity<=Z_*=64/39,
    sum_e||X_e Z||infinity<=L_*=80/13.                     (U37)

The support is the same 32 original links. Both the conditional Haar mean
of Z and that of each horizontal derivative vanish.

Put A_*=256/9, ell=4, and retain

    delta=exp(1024 pi xi)-1, eta=exp(1088 pi xi)-1,
    hz=xi(eta L_*/2+16xi Z_*),
    rz=8A_*xi^2+16xi^2 L_*+64xi hz,
    nz=sqrt((1+delta)z_*).                               (U38)

The exponential factors are the predecessor's actual marginal and constrained-
fiber comparisons. Its remainder r_e=X_e(u-u0) satisfies |r_e|<=A_*xi^2 on
xi<=3/64, which contains our entire new domain. Set
dj=sum_(e in C,alpha)r_e,alpha X_e,alpha F. Then

    W=(2kappa xi/3)QJ+2kappa Qdj, ||dj||_rho<=4A_*xi^2,
    ||X E z||_m<=hz, ||J E z||_rho<=xi eta Z_*, ||Y||_rho<=xi nz,
    R=W-DY=2kappa Qdj+2kappa xi Q sum_i b_i X_i Z
                           -4kappa T* X E z,
    ||R||_rho<=kappa rz.                                 (U39)

Here T is the original score operator with ||T||<=16xi. The signs follow
from DQz=QAz-QAJEz, A=kappa K-2kappa b.X, KZ=U, and
QAJf=-4kappa T*Xf. The conditional coupling stays in the residual.

The seven nonnegative response errors are exactly

    a1=delta xi^2 sqrt(z_*), a2=16xi^3 Z_* L_*,
    a3=16xi^2 eta^2 Z_*, a4=16A_*xi^3 nz,
    a5=4hz^2, a6=128xi^2 nz hz, a7=rz^2/d_xi.

Set

    E_M=(a1+a2+a3+a4+a5+a6+a7)/xi^2,
    E_Z=delta z_*+(eta Z_*)^2+2nz rz/(d_xi xi)+(rz/(d_xi xi))^2. (U40)

The actual values satisfy

    |M0-kappa xi^2 m_*|<=kappa xi^2 E_M,
    | ||D^-1W||_rho^2-xi^2 z_* |<=xi^2 E_Z.                (U41)

To verify the entire response error, put w=kappa xi U and p=JEz. The
variational part of U32 expands to

    2 Re<w,z>-q_A(z)-2 Re<Pw,p>+4kappa Re<dj,Y>
                           +q_A(p)+2 Re q_A(Y,p).

KZ=U and weighted integration by parts turn its first pair into
kappa xi^2<U,Z>_rho+2kappa xi^2 int rho Z sum_i b_i X_i Z.
The marginal comparison bounds its first error by kappa a1. The actual
|b_e|<=8xi bounds the drift term by kappa a2. Both conditional Haar means are
zero, so the removed projection costs kappa a3. The differentiated-vacuum
remainder costs kappa a4. The coarse form is 4kappa||XEz||^2, giving kappa a5.
The complete mixed form and ||T||<=16xi give kappa a6. Finally U31–32 give
kappa a7. Every term is included with its original sign before estimation.
For the metric use ||Y||^2=||z||^2-||p||^2 and
||D^-1W-Y||<=rz/d_xi, expanding the squared norm and keeping its cross term.
This yields exactly E_Z in U40.

## 8. Evaluated certificate, cohomological correction, and physical return

At the exact original value xi=1/100000000,

    d_xi=1/2-6144/100000000=0.49993856.                    (U42)

The checker uses rational pi<355/113, positive exponential series with explicit
remainder, and upper square roots certified by integer squares. It evaluates
U38–40 outward and gives

    E_M<0.0000094, E_Z<0.0000041,
    rz^2/(d_xi xi^2)<0.000000000022.                       (U43)

These are U2's stated enclosures for the actual vacuum. The preceding forcing
and three moments retain their own certified values and domains.

In the actual cochain window span{Y} --D--> Kcal --0-->0, define

    aY=q_D(Y), cY=<Y,W>_rho, alphaY=cY/aY,
    Rcan=W-D(alphaY Y).                                  (U44)

Y is nonzero: positive rho would turn z=JEz into an equality of the same
smooth functions under Haar, whose conditional Haar mean would force z=0,
contradicting U36. Hence aY>=kappa d_xi||Y||^2>0. In the original dual pairing
<r,D^-1t>, the equality <DY,D^-1Rcan>=0 follows by multiplication. Therefore

    ||[W]||_(Kcal/Dspan{Y},dual)^2=M0-|cY|^2/aY,
    R=Rcan+(alphaY-1)DY,
    <R,D^-1R>=||[W]||^2+aY|alphaY-1|^2<=kappa rz^2/d_xi.   (U45)

This retains the complete quotient norm, the original boundary primitive
(alphaY-1)Y and its separate energy. For nested actual spaces Vj in Dom(D),

    V_(j+1)/Vj <--> ker(Kcal/DVj -> Kcal/DV_(j+1)),
    [h] -> [Dh], [Dh] -> [h]                              (U46)

are well-defined inverse maps: a change by DVj changes the primitive by Vj.
U31 supplies the uniform completed inverse. The Split Zero reconstruction
keeps these supported relations, primitives, and original energy pairings.

Retain the actual observed variance G and kinetic entry K0. From [ALM, A48–49],
put

    deltaC=exp(128pi xi)-1,
    B2=xi delta/4+(sqrt(5)xi/6)deltaC+4A_*xi^2,
    emu=(2xi/9)(B2+3delta/2)+(8A_*/3)xi^2,
    EG=B2+(2xi/3+emu)^2.                                 (U47)

Then |G-1|<=EG and |K0-3kappa|<=kappa B2; at U42 both radii are below 11/10^14.
For h0=D^-1W and f=F-<F>_rho, the actual physical state
Phi0=psi(Jf+h0) is centered, nonzero, and in the full form domain. Its exact
pairings are

    ||Phi0||^2=G+||h0||^2,
    q_(H-E0)(Phi0)=K0-M0.                                (U48)

Both mixed entries are -M0 and q_D(h0)=M0. Substitution of U41,U47 proves

    (3-5*10^-13)kappa < q_(H-E0)(Phi0)/||Phi0||^2
                                      < (3+5*10^-13)kappa. (U49)

The complete-domain lower bound U23 and the variational inclusion of span{Phi0}
give, with their respective proved maps,

    0.49993856 kappa <= Delta_L < (3+5*10^-13)kappa          (U50)

for every a>0, L>=2 at g^2=5000.

## 9. Both spectral endpoints at fixed spacing and coupling

Keep a>0,g>=8 fixed and let L grow. For each finite list of smooth bounded
physical cylinder observables O_i use their actual centered vectors
r_i,L=(O_i-<O_i>_rhoL)psi_L. Their matrix spectral measure mu_L satisfies by U23

    mu_L([0,kappa d_xi))=0.                               (U51)

For every coefficient vector x the original first-moment identity is

    int lambda d(x*mu_L x)(lambda)
       =kappa int rho_L sum_e,alpha |X_e,alpha sum_i x_i O_i|^2
       <=kappa sum_e,alpha ||sum_i x_i X_e,alpha O_i||infinity^2. (U52)

Only the original finite supports occur on the right. Dividing this bound
by Lambda controls all mass above Lambda, uniformly in L. Thus weak selection
on [0,infinity], jointly with the equal-time vacuum selection, gives

    mu({0})=0, mu({infinity})=0,
    supp mu subset [kappa d_xi,infinity),
    G^c=C(0+), C(t)=int exp(-t lambda)dmu(lambda).           (U53)

Polarization gives the full matrix statement. A countable gauge-invariant
cylinder algebra and diagonal selection retain it for every finite list.
For the conditional memory, D_L>=kappa d_xi similarly excludes zero-energy
mass. Its inverse-energy measure has no atom at zero. U33 controls the two
limit orders down to zero shift. Thus the previously retained Z_alpha is
proved zero in this fixed-spacing, fixed-coupling volume limit.

The limiting elementary-loop vector survives quantitatively. The predecessor's
four-link marginal bound proves

    Var_rhoL F=inf_c int rho_L |F-c|^2
        >=exp(-128pi xi) inf_c int_H |F-c|^2
        =exp(-128pi xi).                                 (U54)

Also q_A(F)<=4kappa. Spectral integration of exp(-t lambda)>=1-t lambda and
U51 yields in the limit

    C_F(t)>=exp(-128pi xi)-4kappa t,
    0<=C_F(t)<=C_F(0)exp(-kappa d_xi t).                   (U55)

In particular the lower bound is positive for the explicitly stated interval
0<t<exp(-128pi xi)/(4kappa).

For the limiting generator use symbols [i,t], t>=0, paired by C_ij(t+s),
quotient the complete null space, and complete. Time translation
T(u)[i,t]=[i,t+u] retains the finite-volume positive self-adjoint contraction
Gram inequality. U52 gives continuity at zero, hence strong continuity on
the dense span. Equivalently realize each symbol as exp(-t lambda)e_i in the
Hilbert space of the positive matrix measure; its closed cyclic span reduces
the multiplication semigroup and its generator. The generator is multiplication
by lambda with domain int lambda^2|h|^2 dmu<infinity on that reducing span.
Its lower bound is kappa d_xi and its Hilbert space is nonzero by U54–55.
This is a nontrivial gapped infinite-volume correlation generator at fixed
lattice spacing, obtained from the actual vacuum correlations.

The comparison with section 5's cylinder form is explicit. The map sending a
centered cylinder f in L^2(nu) to its zero-time correlation vector xi_f is an
isometry, since U53 identifies its Gram with the original limiting covariance.
It extends to a closed-range isometry U. For each such f the predecessor's
all-coupling derivative estimate |b_e^L|<=8xi gives a volume-uniform bound on

    ||A_L f||infinity<=kappa||Kf||infinity
                  +16kappa xi sum_e||X_e f||infinity.

Thus its spectral second moments are uniformly bounded. This supplies uniform
integrability of its first moments, so polarization and U52 give
q_obs(Uf,Uh)=q_infinity(f,h) on cylinders. Closure extends the isometric form
inclusion to the closed cylinder form domain. This is the declared map between
the two constructions; any orthogonal complement of its range remains in the
correlation Hilbert space with the same lower bound. The further argument in `VOLUME_LIMIT.md`, V1–25, proves a unique original
vacuum measure and a direct dynamical limit, and constructs the surjective
unitary between this correlation space and its full physical vacuum
representation. The cylinder-form inclusion here retains its stated domain;
that subsequent identification is proved through the semigroups.

## 10. Exact comparison with the running continuum path

The earlier path remains

    a_n=a_0 2^-n, L_n=4*2^(2n),
    c_n=g_0^-2+beta n log2, g_n^2=c_n^-1,
    xi_n=c_n^2/4, kappa_n=2^(n+1)/(a_0 c_n).               (U56)

The newly proved domain is exactly c_n<=1/64. It contains only finitely many
indices on that path for beta>0. The predecessor's all-coupling derivative and
gauge-sector estimates remain available with their complete c_n dependence;
U1 is not asserted outside its proved domain.

There is a precise further path calculation at any fixed g>=8. Along a_n->0,
U1 gives Delta_n>=2g^2 d_xi/a_n->infinity, independently of the box sequence.
For uniformly bounded centered observables,

    |C_ij,n(t)|<=||r_i,n|| ||r_j,n||exp(-2g^2 d_xi t/a_n)->0 (t>0). (U57)

For every fixed finite energy Lambda the excited spectral mass in [0,Lambda]
is eventually exactly zero. The compactified zero-time mass is retained at
energy infinity. Consequently the fixed-spacing volume limit U53 and this
change of spacing U57 have explicitly different parameter maps and endpoint
formulas. Neither is substituted for the original g_n->0 path.

This cycle has supplied full-domain physical coercivity, a quantitatively
controlled inverse at zero, actual zero-shift response values with finite
errors, and the fixed-spacing volume extension. Extending control of the
complete vacuum Hessian and conditional response beyond the stated xi range,
while retaining the physical spacing and growing support, is the next original
quantity in the workbench. No desired continuum estimate is inserted as a
premise. The four-dimensional continuum field and positive physical mass remain
unestablished by this contribution.

## 11. Provenance and verification scope

[YM] KokunoYumeto/yang-mills-interacting-workbench, original source commit
`fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`,
`yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md`,
blob `66a7453a6452c2555a28270efcf53fa1997c26a8`, sections 1–3. Original operator,
positive ground state and domains. The source's Hamiltonian antecedents and
original physical conventions retain their attribution.

[ALM] The complete delivered `20260915-actual-loop-moments/RESEARCH_NOTE.md`
and checker. Used equations A4–5, A14–20, A24–31, A34, A48–49. The complete
file was read and its exact original checker replayed. The positive-shift
response of that source is preserved; U31 justifies the new zero-shift inverse.

[CR] PR6 `e98b2c3af77f66fb1c1396143ca53daef586404f`,
`20260914-coupled-response/RESEARCH_NOTE.md`, especially C13–22: actual support
windows and full residual identities. The completed zero-shift instance is
U31–33,U44–46, with its physical norm explicitly retained.

[FA] Hun Hee Lee, Ebrahim Samei, Nico Spronk, *p-Fourier algebras on compact
groups*, arXiv:1411.2336v2, sections 0.1–0.2 and 1.1, public HTML
https://arxiv.org/html/1411.2336v2 . These are the standard Fourier-coefficient
antecedents. U7–14 prove the precise derivative and support estimates used here.

The current peer PR descriptions and Zeta head were inspected for continuation
intake. New Collatz completion and ES cofactor developments are recorded as
candidates; they supply no premise to this proof. No unread peer theorem or
reported CI count is presented as new verification here.

`verify.py` checks coordinate Gamma_2 identities on original SU(2) polynomials,
representation/support and contraction constants, raw-Gram zero-shift matrix
identities, corrected cohomological residuals, and rational endpoint evaluation.
Finite matrix examples are declared fixtures. The full analytic contraction,
regularity, spectral and limit arguments are written above. Receipts identify
the executed source bytes and exit codes; no new Lean, remote CI, independent
external review, or historical-priority conclusion is claimed.


# Execution diagnostics retained

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-uniform-gap-zero-shift/DEVELOPMENT.md}

\textbf{SHA-256:} \path{a7d245e85e1f21af51c8c024adef5c0381847a1823c8c7b23eccba8381781022}
\end{quote}


A source-corruption CLI test expected FAIL: predecessor-hash:verify.py; the checker instead rejected with exit1 and an uncaught pre-main ValueError bearing that same exact code.

Catch the explicit source-pin ValueError/OSError before import and emit the same named FAIL line with exit1. Regenerate and replay the complete final receipt.

Diagnostic guard only; no mathematical statement, tested formula, source pin or validation rule changed.

Earlier outer harness attempts reached their execution limit without a complete receipt; they are not counted as passed. The final complete finite replay returned exit0 and produced execution.json. All spawned replay processes have finished.

Earlier checker SHA-256: `45bc148e184b95e35f214bd9fe71f80b58aebc5fa0db7bb82462a35c6689d766`.
Final checker SHA-256: `d78432d5eeab097efa7aa018de30932d67c4c77edcc4ceeeae843b955f60f655`.


# Full-domain gap through the actual vacuum conditionals

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-uniform-gap-zero-shift/HEAT_BATH_GAP.md}

\textbf{SHA-256:} \path{e37b1864544e0857c2dbc984d048ab8f1e0a567bead7d86c54a6ccc4870581fd}
\end{quote}


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


# The full spatial-volume limit: original vacuum measure and dynamics

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-uniform-gap-zero-shift/VOLUME_LIMIT.md}

\textbf{SHA-256:} \path{3952922cfa7802d12796efe714bb469ddeb80fa3957f1ef51223b1884e94d4ad}
\end{quote}


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


# Exact plaquette coefficient and the sharper full-gap domain

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-uniform-gap-zero-shift/OPTIMIZED_DOMAIN.md}

\textbf{SHA-256:} \path{33acc63d3789f900854519500a59ba2bb033eabf8783238df34f0381033989fd}
\end{quote}


15 September 2026. This sharpens, on the same original coefficients and
physical operators, the fully written construction in `RESEARCH_NOTE.md`.
It also returns the sharpened constants through every step of
`VOLUME_LIMIT.md`. The baseline estimates are preserved in those files for
comparison; the present formulas give the stronger domain and lower bound.

The actual coefficient recurrence, plaquette words, representations, product
Haar coordinates, vacuum, physical energy and observation maps are unchanged.

## O1. The original plaquette coefficient has trace norm exactly eight

Write the four independent original link variables in their word order:

    W_p=Tr(U1 U2 U3^-1 U4^-1).

The inverse entry of an SU(2) matrix is

    (U^-1)_(r,c)=(-1)^(r+c) U_(1-c,1-r), r,c in {0,1}.

It follows directly from det(U)=1, or from multiplication by the original
matrix epsilon=[[0,1],[-1,0]]. Keeping all four trace indices gives the
coefficient A in W_p=Tr(A(U1 tensor U2 tensor U3 tensor U4)):

    A_[(i1,i2,1-i2,1-i3),(i0,i1,1-i3,1-i0)]
        +=(-1)^(i0+i2),  i0,i1,i2,i3 in {0,1}.             (O1)

Every unlisted entry is zero. This formula is the complete original Fourier
coefficient, with the trace convention U6; there is no change in source mass.
For each fixed pair (i1,i3), the two possible rows (i2=0,1) and columns
(i0=0,1) form the block [[1,-1],[-1,1]]. Different pairs have disjoint row
sets and disjoint column sets. There are four such blocks and eight unused
rows and columns. These are explicitly permuted original row and column
indices, not chosen singular vectors.

Consequently A* A is positive, (A* A)^2=4A* A, and Tr(A* A)=16. The matrix
(A* A)/2 is positive and its square is A* A. Uniqueness of the positive
square root proves

    ||A||_1=Tr sqrt(A* A)=8.                              (O2)

The Haar norm check is Tr(A* A)/16=1, agreeing with the original plaquette
second moment. Any permutation into the fixed global order of edge tensor
factors conjugates A by the explicitly corresponding tensor permutation,
preserving O2. This proves the value for every original plaquette in the box.

## O2. A second auxiliary support norm, with its complete comparison

Put w=5/4. On the same labelled coefficient families in U9 define

    ||f||_w=max_e sum_(S containing e) w^|S|
                            sum_(j nontrivial)c(j)||A_(S,j)||_1. (O3)

The map between this coefficient space and U10 is the identity on each
original A_(S,j); its inverse is the same identity. On each finite original
graph their exact estimates are

    ||f||_w <= ||f||_2 <= (8/5)^|E_L| ||f||_w.             (O4)

This follows by comparing the displayed positive weights at each original
support label. The second factor retains its volume dependence. It is not
used to transfer a volume-uniform estimate. The physical L2 and energy
pairings have not been changed; O3 is an auxiliary absolute-convergence norm
for the exact same source coefficients and their assembly map.

Since w^|S union T|<=w^|S|w^|T|, the entire anchored calculation U12–14 gives,
with its original matrices and all generator components,

    ||B(f,h)||_w <= (8/3)||f||_w||h||_w.                  (O5)

O2 and the actual maximum of four incident plaquettes give the improved
source estimate

    ||v_[1] xi||_w <= B_xi,
    B_xi=4 w^4 *8 xi=(625/8)xi.                          (O6)

The factor c(j)=3 still cancels the original inverse Casimir 1/3. Every
weight and each of the four plaquette links remains explicit.

## O3. Sum the convergent majorant instead of replacing it by twice its input

Define the following actual scalars from the original coupling:

    theta_xi=(2500/3)xi,
    r_xi=(3/16)(1-sqrt(1-theta_xi)),
    0<xi<451/552960.                                    (O7)

This interval lies strictly inside theta_xi<1. Direct multiplication gives

    r_xi=B_xi+(8/3)r_xi^2,
    (16/3)r_xi=1-sqrt(1-theta_xi)<125/288<1.              (O8)

The closed r_xi ball is therefore preserved by the literal nonlinear map
f->v_[1]xi+B(f,f), and its difference bound is the strict constant in O8.
Starting at zero, the successive differences are bounded by that constant
to their iteration power times B_xi. Their sum converges in the complete
labelled norm. Passing in the bounded bilinear map proves the fixed equation;
the same difference inequality proves uniqueness in that ball.

Equivalently, the complete order coefficients satisfy the already proved
Catalan recurrence and now obey

    ||xi^p v_[p]||_w <= C_(p-1)(8/3)^(p-1) B_xi^p,
    sum_(p>=1) C_(p-1)(8/3)^(p-1) B_xi^p=r_xi.            (O9)

The equality follows from the scalar generating equation c=1+z c^2 and the
branch with constant coefficient one, on 4z<1. For a direct justification,
the Catalan convolution proves the equation coefficient by coefficient;
C_n<=4^n gives absolute convergence, and the positive solution continuous
at z=0 is (1-sqrt(1-4z))/(2z). Its omitted tail after order P is at most

    B_xi theta_xi^P/(1-theta_xi).                         (O10)

Every coefficient is the same exact coefficient as in U26. Thus on the
common convergence interval the labelled families themselves agree, including
the assembly-kernel data. The improved radius extends that original family;
it does not select another observation or another vacuum. The C2 convergence,
elliptic bootstrap, recovered scalar c_L and ground energy E0,L are precisely
the constructions U17–18, now applied to this convergent same-source series.
Their proofs identify the actual positive unit vacuum at every g in O7.

## O4. The complete second derivative and the full physical gap

The elementary integer maximum needed in the original row estimate is

    sup_(m>=1) (m+1)/(5/4)^m=256/125, attained at m=3,4.  (O11)

The ratio of successive terms is (4/5)(m+2)/(m+1): it exceeds one at m=1,2,
equals one at m=3, and is smaller afterwards. Substitution into the full
mixed-block estimate U18, before any diagonal entry is removed, gives

    ||S_u||op <= (384/125)r_xi.                          (O12)

The same bound holds for the nonnegative full derivative row majorant used
for the drift comparison. The original group coordinate Gamma2 calculation
U20–22 is unchanged. It consequently proves on the full centered scalar
form domain, and hence on its complete physical invariant subspace,

    Delta_L >= kappa d_xi^sharp,
    d_xi^sharp=1/2-(768/125)r_xi
             =(144/125)sqrt(1-(2500/3)xi)-163/250 >0.    (O13)

This is valid for every L>=2 and a>0 on the explicit domain O7. The upper
endpoint of O7 is obtained by exact squaring:

    1-(2500/3)(451/552960)=(163/288)^2,
    r_(451/552960)=125/1536.                             (O14)

No strict estimate is asserted at that endpoint. In the original coupling
coordinate the proved positive-gap interval is

    g^4>138240/451.                                     (O15)

A useful closed subinterval with a simple physical constant is

    g>=9/2  => xi<=4/6561,
    Delta_L >= (3/20)kappa =3g^2/(10a).                 (O16)

For this explicit domain the inequality is proved, rather than inserted as
an assumption: 1-theta_xi>=9683/19683, and
9683/19683>(401/576)^2. Multiplying the latter square-root bound by 144/125
and subtracting 163/250 gives a number strictly greater than 3/20.
The weak endpoint notation in O16 is therefore safe throughout the closed
g-domain. At larger g the original formula O13 retains its stronger value.

The exact primitive relation remains

    ||p_L||^2=1/Delta_L <=1/(kappa d_xi^sharp),
    p_L((X_i f)_i)=f, int rho_L f=0.                    (O17)

Its source/target pairing is the original physical one in U25, not O3.
All physical states, including regulator-dependent choices, are included in
O13. No finite trial-space lower bound has been substituted.

## O5. Return to the actual zero-shift moments and the canonical residual

The actual D of U31 is the same original conditional-kernel form restriction.
Every element of that kernel has zero mean in rho_L. Therefore

    D>=kappa d_xi^sharp,
    ||D^-1||<=1/(kappa d_xi^sharp).                       (O18)

The actual elementary-loop constructions U33–40 retain their original
forcing W, trial Y, remainder R=W-DY, raw G, kinetic K0, and coefficients
8/39 and 196/4563. The predecessor's pointwise log-vacuum remainder is proved
on xi<=3/64, which contains the entire domain O7. Thus the same explicit
expressions delta,eta,h_z,r_z,n_z and a1,...,a6 remain applicable. In a7 and
the restored-state error, replace the inverse bound by the proved O18:

    a7=r_z^2/d_xi^sharp,
    E_M^sharp=(a1+...+a6+a7)/xi^2,
    E_Z^sharp=delta z_*+(eta Z_*)^2
          +2n_z r_z/(d_xi^sharp xi)+(r_z/(d_xi^sharp xi))^2. (O19)

These are estimates in the original physical Hilbert pairing. They give

    |M0-(8/39)kappa xi^2|<=kappa xi^2 E_M^sharp,
    |||D^-1W||^2-(196/4563)xi^2|<=xi^2 E_Z^sharp.          (O20)

The exact canonical quotient/primitive energy identity U45 is unchanged,
and its full nonnegative error is at most kappa r_z^2/d_xi^sharp.

At the already specified actual coupling xi=10^-8, g^2=5000, kappa=10000/a,
outward rational square-root bounds prove

    d_xi^sharp>0.49999519998,
    E_M^sharp<0.0000094,
    E_Z^sharp<0.0000041,
    r_z^2/(d_xi^sharp xi^2)<0.000000000022.               (O21)

Thus all zero-shift intervals U41–50 remain valid with this sharper full-gap
lower endpoint. In particular the actual complete physical gap satisfies

    0.49999519998 kappa <= Delta_L < (3+5/10^13)kappa.    (O22)

The upper bound is still the actual one-state variational upper bound U49;
its direction and scope have not changed. The lower bound is from the full-
domain argument O13. The polynomial coefficients and actual-vacuum remainder
estimates have been retained separately in O19–20.

## O6. Complete return through the spatial-volume construction

The proof in `VOLUME_LIMIT.md` uses the actual coefficient recurrence,
absolute support bounds, a summed conditional influence below one, and a
summable drift derivative row bound. Each input is now evaluated explicitly
on O7; the following formulas replace only the auxiliary bounds in that
proof, on the exact same finite-volume vacua.

First, labelled coefficients are cutoff-compatible by V1, independently of
the auxiliary norm. Their complete w-weighted bound is r_xi. Thus

    sup_e sum_(S containing e)||v_S||infinity<=(16/15)r_xi. (O23)

Here c(j)>=3/4 and w^|S|>=5/4 were used directly. The original conditional
densities V5 consequently have the same uniformly absolutely convergent
meaning. Their original influence majorant V6 now obeys

    sup_e sum_f c_ef<=(65536/9375)r_xi<128/225<1.         (O24)

Indeed sup_(m>=1)(m-1)/(5/4)^m=4096/3125, attained at m=5,6, and multiplying
by 16/3 gives the first coefficient. Its endpoint value at r=125/1536 is
128/225. The finite heat-bath comparison V8–9 is therefore the same actual
comparison, with q=128/225 and its complete Neumann powers. The proof gives
uniqueness and full-sequence convergence of the original vacuum measure on
the entire sharper interval O7.

The full mixed drift matrix in V10 has row sum at most

    B_*=(384/125)r_xi<1/4.                               (O25)

Its long-distance rows are bounded by
(3/2)r_xi (m_d+1)/(5/4)^m_d, with m_d=max(3,d+1), by O11 and the original
connected-support argument. The drift approximation is supplied by the
complete coefficient tail O10. All original variables, vector fields and
Brownian coefficients in V12–18 remain fixed. Hence the direct dynamics,
its invariant measure, and every local time-ordered correlation converge
along the full box sequence just as proved there. In V20 substitute the
proved full-domain lower value kappa d_xi^sharp. This constructs the same
physical vacuum representation and gives its self-adjoint generator that
positive lower edge. Both compactified spectral endpoint atoms are zero at
fixed a,g, using the same local first-moment bound U51.

The scalar vacuum energy identity V23–25 is also unchanged: its pointwise
input xi<=3/64 contains O7, and its local drift convergence now uses O10.
Thus the original energy-per-plaquette limit and its finite explicit error
remain established on this larger domain.

Finally, the original simultaneous path keeps

    a_n=a0 2^-n, c_n=g0^-2+beta n log2, g_n^2=1/c_n,
    xi_n=c_n^2/4.

The exact new validity interval on that path is

    c_n < sqrt(451/138240).                              (O26)

For beta>0 only a finite initial part of that unbounded c_n path lies in this
proved domain. With fixed admissible g and a->0, the original physical lower
bound kappa d_xi^sharp diverges as 1/a; the positive-time collapse and the
retained infinite-energy endpoint in U57 follow with this same exact value.
No finite continuum mass or smooth four-dimensional field construction is
assigned to these parameter maps.

## Scope of verification

The checker constructs the complete original 16 by 16 Fourier coefficient,
checks its positive-square-root identity, and verifies the trace convention
against literal four-link SU(2) words using exact rational quaternions. It
checks the finite support norm comparisons, all extremal weight constants,
the exact quadratic majorant, domain endpoints, original physical factors,
and O21 with integer-square outward bounds. The general analytic arguments
and infinite-limit proofs are the written proofs U1–57 and V1–25 with the
explicit substitutions O1–26 above. Exact finite checks do not constitute a
new Lean build or an independent mathematical audit. No general-priority
claim is made for the Fourier, contraction, curvature or Gibbs methods.


# Zero-shift local Yang–Mills response, all-coupling fibre inverses, and the retained exterior

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260915-zero-shift-local-fibres-review/DELIVERED_RESEARCH_NOTE.md}

\textbf{SHA-256:} \path{42aa9ab14a4b42ba9d170803fb0f9ce9f0d1d763d10139b3a15f9ba317543e55}
\end{quote}


15 September 2026. Continuation of the **actual-loop-moments** delivery, which in turn continues PR6 at `e98b2c3af77f66fb1c1396143ca53daef586404f`. The predecessor is preserved with its original proof and checker in the offline
package. Every analytical input used from it is reproduced below; the Git
contribution and its checker are self-contained. This note uses the full finite-regulator SU(2) Wilson Hamiltonian and its actual vacuum. Written proofs, exact finite checks, and the eventual continuum theory keep their separate evidence records.

The calculation establishes an all-coupling local conditional-kernel lower bound, a quantitative zero-shift inverse along an explicit simultaneous spatial/coupling/volume sequence, and narrow enclosures for the actual zero-shift Wilson response and restored norm. The narrow enclosure uses `xi=10^(-8)`. The all-coupling inverse is a separate result and is evaluated on a path with `g -> 0`. Both domains and the exact map between the new and previous observations are given below. General heat-kernel, conditional Poincare, and Schur techniques retain their antecedents; no historical-priority claim is made.

## 1. Full operator and original forms

The vertices are `{-L,...,L}^3`, `L>=2`, with every contained positive edge and every contained elementary face. Reverse traversal uses the inverse of the same link. With `T_alpha=-i sigma_alpha/2`, retain

\[
 X_{e,\alpha}f(U)=\left.\partial_t f(\ldots,e^{tT_\alpha}U_e,\ldots)\right|_0,
 \quad K=-\sum_{e,\alpha}X_{e,\alpha}^2,
\]
\[
 \kappa=\frac{2g^2}{a},\quad v=\frac1{2g^2a},\quad
 \xi=\frac v\kappa=\frac1{4g^4},\quad
 V=v\sum_p(2-W_p),\quad H=\kappa K+V.                 \tag{Z1}
\]
Here `a,g>0`, and each `W_p` is the original ordered fundamental trace. The scalar `2v|P|` remains. The original metric satisfies `c(T_alpha,T_beta)=delta_alpha,beta/4`, so `Delta^c=4 sum X^2`; all derivatives below are the displayed `X`.

The source [YM] constructs the unique smooth positive unit vacuum `psi`, its energy `E0`, and the `H^2/H^1` operator/form domains on the compact product group. Write

\[
 \rho=\psi^2,\quad u=\log\psi,\quad b_{e,\alpha}=X_{e,\alpha}u,
 \quad\mathcal A=\psi^{-1}(H-E_0)\psi.
\]
The map `f -> psi f` has inverse `F -> F/psi` and preserves the original inner product because `int conjugate(psi f) psi h=int rho conjugate(f) h`. Consequently

\[
 q_\rho(f,h)=\kappa\int\rho\sum\overline{Xf}Xh,
 \qquad \mathcal A=-\kappa\mathscr L,
 \quad\mathscr L=\Delta+2b\cdot X,\quad\Delta=\sum X^2. \tag{Z2}
\]
All scalar estimates are first proved on this full space and then restricted to the gauge-invariant physical space.

We use the predecessor's coordinate estimates and recall their proofs. Differentiating `Delta u+|b|^2=(V-E0)/kappa` gives

\[
 \mathscr L b_{e,\alpha}=\kappa^{-1}X_{e,\alpha}V.       \tag{Z3}
\]
The Casimir commutes with `X_e,alpha`; the commutator correction in differentiating `|b|^2` contracts an antisymmetric epsilon tensor with `b_beta b_gamma` and vanishes. Our bracket is `[X_e,alpha,X_e,beta]=-epsilon_alpha,beta,gamma X_e,gamma`.

For any scalar `h`, the antisymmetric part of the matrix `X_e,beta X_e,alpha h` has squared Frobenius norm `|X_e h|^2/2`. At a maximum of `|b_e|^2`, Z3 and `|X_e V|<=v r_e`, where `r_e<=4` counts incident faces, therefore give

\[
 |b_e|\le2r_e\xi\le8\xi,\qquad |X_e\log\rho|\le16\xi. \tag{Z4}
\]
Let `u_1=(1/3)sum_p W_p`, `b_e^1=X_e u_1`, and `r_e^1=b_e-xi b_e^1`. The original Pauli products give

\[
 |b_e^1|\le B_1=4/3,\qquad
 \sum_f\|X_f b_e^1\|_{op}\le H_1=8/3.
\]
The exact equation is `mathscr L r_e^1=-2xi sum_i b_i X_i b_e^1`. The same maximum argument gives `(1/2-16xi/3) sup|r^1| <=64xi^2/9`. Thus for `0<xi<=3/64`,

\[
 |r_e^1|\le A\xi^2,\quad A=256/9,\qquad
 \sum_\alpha\|\nabla r_{e,\alpha}^1\|_\rho^2
 \le(128A/3)\xi^4.                                   \tag{Z5}
\]
The last inequality follows by integrating the exact equation and using `|mathcal A r_e^1|<=128 kappa xi^2/3` and the preceding supremum bound. All derivative indices range over the full graph.

## 2. A heat-kernel ratio in the original SU(2) time

Let `p_theta` be the Haar-probability density of `exp(theta Delta_e)`. Write a link as `cos r I-i sin r omega.sigma`, `0<=r<=pi`; the path length in the metric making the original `X` orthonormal is `2r`. The exact radial series is

\[
 p_\theta(r)=e^{\theta/4}\sum_{n\ge1}n e^{-n^2\theta/4}
                       \frac{\sin nr}{\sin r}.        \tag{Z6}
\]
The eigenvalue `(n^2-1)/4` and multiplicity `n^2` are those of the original link Casimir; no energy coefficient has been reset.

For comparison with [HK], let `K_t^d` use the unit sphere and its area measure. The actual quaternion map sends the present differential operator to `(1/4)Delta_(S^3)` and Haar to `d sigma_3/(2pi^2)`. Thus `p_theta=2pi^2 K^3_(theta/4)`. Equation (1) of [HK] gives, with `q_theta^5=pi^3 K^5_(theta/4)`,

\[
 \partial_r p_\theta(r)=-4e^{-3\theta/4}\sin r\,q_\theta^5(r)\le0. \tag{Z7}
\]
The sphere heat kernel is positive by its parabolic maximum principle. These explicit time, measure, and derivative identities locate the maximum of `p_theta` at zero and its minimum at `pi`.

Periodizing the one-dimensional Gaussian, differentiating its normally convergent series, and using the same dimension recurrence gives

\[
 p_\theta(r)=\frac{2\sqrt\pi e^{\theta/4}}{\theta^{3/2}\sin r}
 \sum_{k\in\mathbb Z}(r+2\pi k)e^{-(r+2\pi k)^2/\theta}. \tag{Z8}
\]
For `0<theta<=4`, passage to `r=pi` pairs the terms of equal odd absolute index. Every resulting term is positive, because `2pi^2/theta-1>0`. Retaining the first pair gives

\[
 p_\theta(\pi)\ge4\sqrt\pi e^{\theta/4}\theta^{-3/2}
              (2\pi^2/\theta-1)e^{-\pi^2/\theta}.      \tag{Z9}
\]
At zero, use `n^2 exp(-theta n^2/4) <= int_(n-1)^n (x+1)^2 exp(-theta x^2/4) dx`. Summing and integrating the three Gaussian moments proves

\[
 p_\theta(0)\le e^{\theta/4}\theta^{-3/2}
          (2\sqrt\pi+4\sqrt\theta+\sqrt\pi\theta).
\]
Consequently

\[
 \frac{p_\theta(0)}{p_\theta(\pi)}
 \le a(\theta)e^{\pi^2/\theta},\quad
 a(\theta)=\frac{2\sqrt\pi+4\sqrt\theta+\sqrt\pi\theta}
                  {4\sqrt\pi(2\pi^2/\theta-1)}\le1
       \quad(0<\theta\le4).                           \tag{Z10}
\]
For the last inequality, the numerator is at most `6sqrt(pi)+8<=14sqrt(pi)` and the denominator is at least `14sqrt(pi)`, using `pi>3`.

For `theta>=4`, `|sin nr/sin r|<=n` in Z6 gives

\[
 |p_\theta-1|\le q_\theta
 =\sum_{n\ge2}n^2e^{-(n^2-1)\theta/4}
 \le5e^{-3\theta/4}\le1/4.
\]
Indeed, put `n=k+2`, use `n^2-1>=3+5k`, and sum
`sum_(k>=0)(k+2)^2 z^k=(4-3z+z^2)/(1-z)^3<=5` for `0<=z<=1/100`. Finite exponential sums prove `e^5>100` and `e^3>20`. Hence

\[
 \theta\log\frac{p_\theta(0)}{p_\theta(\pi)}
 \le(40/3)\theta e^{-3\theta/4}
 \le(160/3)e^{-3}<8/3<\pi^2.
\]
Together with Z10 this proves at every positive original time

\[
 \boxed{\quad p_\theta(0)/p_\theta(\pi)\le e^{\pi^2/\theta}.
 \quad}                                               \tag{Z11}
\]
The prefactor also matters. For `0<theta<=1`,

\[
 a(\theta)\le a_1\theta,\qquad
 a_1=\frac{3\sqrt\pi+4}{4\sqrt\pi(2\pi^2-1)}.          \tag{Z12}
\]
Every inequality above has its numerical constants explicitly evaluated. The general spherical heat-kernel identities are cited to [HK]; this note does not assert a new general heat-kernel theorem.

## 3. All-coupling local vacuum oscillation with the exterior retained

Fix a nonempty set `S` of `d` original links, and let `m_S` count all contained faces meeting it. The exact decomposition is

\[
 H=\kappa K_S+H_{\rm ext,S}+V_S,\qquad
 0\le V_S\le4v m_S.                                  \tag{Z13}
\]
`H_ext,S` includes every other link derivative and every other face, with their original constants. The two summands in `kappa K_S+H_ext,S` act on different tensor factors.

For `t=theta/kappa`, bounded-potential comparison of positive semigroups gives

\[
 e^{-4m_S\xi\theta}T_t\psi
 \le e^{-tH}\psi\le T_t\psi,
 \quad T_t=e^{\theta\Delta_S}\otimes e^{-tH_{\rm ext,S}}. \tag{Z14}
\]
For a direct proof, write the Trotter product with `exp(-t V_S/N)` between the positive free semigroups. Each multiplier is between `exp(-4vm_S t/N)` and one. Order preservation gives the bound at each product. Strong convergence, followed by a subsequence and continuity of these smooth functions, gives Z14 pointwise. Thus no bound on an omitted exterior vacuum is used.

At two points differing only in the links in S, the exterior heat kernel in `T_t` is the same. The product of the d original link kernels has ratio at most `[p_theta(0)/p_theta(pi)]^d`. The actual ground factor in `e^(-tH)psi=e^(-tE0)psi` cancels on both sides. Z11 therefore proves

\[
 \operatorname{osc}_{S\mid S^c}\log\rho
 \le8m_S\xi\theta+2d\pi^2/\theta.
\]
At the explicitly chosen `theta_*=(pi/2)sqrt(d/(m_S xi))`,

\[
 \boxed{\quad \operatorname{osc}_{S\mid S^c}\log\rho
 \le H_S:=\min\{8\pi\xi\sum_{e\in S}r_e,
                   8\pi\sqrt{d m_S\xi}\}.\quad}      \tag{Z15}
\]
The first entry is Z4 integrated over paths of length at most `2pi` in each original link. The physical heat time in the second entry is
`t_*=theta_*/kappa=(pi a/2)sqrt(d/m_S)`, since `kappa v=1/a^2`.

For the elementary square C based at the origin in directions 1 and 2, `d=4`, `m_C=13`, and `sum r_e=16`. In particular

\[
 H_C\le\min\{128\pi\xi,16\pi\sqrt{13\xi}\}
       =\min\{128\pi\xi,8\pi\sqrt{13}/g^2\}.         \tag{Z16}
\]
Boundary squares have no greater counts, so these same upper bounds cover them.

Set `c=1/g^2` and `B=8pi sqrt(13)`. For `c>=2`, choose
`theta_*=2pi/(sqrt(13)c)<1`. Z12 yields
`a(theta_*)<=1/(8c)`. To check the constant without decimal rounding, use
`pi<22/7`, `pi>157/50`, `sqrt(pi)>177/100`, `sqrt(13)>18/5`; they give

\[
 \frac{2\pi a_1}{\sqrt{13}}
 <\frac{4571875}{37274607}<\frac18.
\]
These elementary bounds are certified in the checker by an alternating Machin formula and integer-square comparisons. Keeping the prefactor in Z10 and squaring the ratio from Z14 gives the sharper all-configuration estimate

\[
 \boxed{\quad
 \frac{\sup_{U_C}\rho(U_C,Z)}{\inf_{U_C}\rho(U_C,Z)}
 \le (8c)^{-8}e^{Bc},\qquad c\ge2.\quad}             \tag{Z17}
\]
The exterior configuration Z is arbitrary and remains fixed in this formula.

## 4. The exact local observation and its zero-shift inverse

Write the original oriented links around C as `V_1,...,V_ell` (`ell=4`) and
`Omega=V_1...V_ell`. Inversely traversed links are related to the positive-link variables by `U -> U^(-1)`, its own Haar-preserving inverse; the original Casimir is preserved by this map. Retain every exterior positive link `Z=U_(C^c)`.

The global coordinate map is

\[
 (V_1,\ldots,V_\ell,Z)\longmapsto
 (\Omega,g_1,\ldots,g_{\ell-1},Z),\quad g_j=V_1\cdots V_j,
\]
\[
 V_1=g_1,\quad V_j=g_{j-1}^{-1}g_j\ (1<j<\ell),\quad
 V_\ell=g_{\ell-1}^{-1}\Omega.                        \tag{Z18}
\]
Successive Haar translations give exactly `dU=dOmega prod_j dg_j dZ`.
Let `E_l` be conditional expectation onto `(Omega,Z)` in the actual measure
`rho dU`, `J_l` its pullback, `P_l=J_l E_l`, `Q_l=I-P_l`, and
`K_l=ker E_l`. The explicit conditional density is the original rho divided
by its integral in the displayed prefix variables. Fubini gives
`E_l J_l=I`, `J_l*=E_l`, and `P_l=P_l*=P_l^2`.

Let `E_S` instead integrate all loop links given Z. Conditional Fubini gives
`E_S=E_Z E_l`; hence every `h in K_l` has zero conditional mean given Z.
The product-Haar gap for the original link Casimirs is `3/4`. At fixed Z,
minimizing over constants and comparing the maximum and minimum of the
actual conditional density give

\[
 \operatorname{Var}_{\rho(\cdot\mid Z)}h
 \le\frac43 e^{H_C}
       \int\sum_{e\in C,\alpha}|X_{e,\alpha}h|^2\rho(dU_C\mid Z).
\]
Only one maximum/minimum ratio enters: use `inf_z int |h-z|^2 rho`, bound it
above by the maximum density times the Haar variance, and bound the Haar
gradient integral by the inverse minimum density. Integrating in the unchanged
exterior marginal proves

\[
 \boxed{q_\rho(h)\ge\delta_C\|h\|_\rho^2\quad(h\in H^1\cap K_l),
 \qquad \delta_C=\tfrac34\kappa e^{-H_C}>0.}           \tag{Z19}
\]
This is true on the full scalar kernel and on its physical invariant part.
The derivative sum on the left contains all exterior derivatives as well.

The form domain `H^1 intersect K_l` is closed in the form norm. Smooth
functions are dense in it: approximate a vector in `H^1` by smooth functions
and apply `Q_l`; the compact smooth positive-density integral defining `E_l`
preserves `H^1` and smoothness. Its derivative formula follows by differentiating
under the compact integral, with finite smooth density coefficients. Thus the
restricted closed form represents a self-adjoint `D_l>=delta_C`. Its resolvent
is compact at each finite regulator by the compact `H^1 -> L^2` embedding.
In particular `D_l^(-1)` exists on all of `K_l` and

\[
 \|D_l^{-1}\|\le\frac4{3\kappa}e^{H_C}.              \tag{Z20}
\]
This supplies the zero-shift inverse used below, rather than postulating a
lower spectral bound for the unresolved conditional kernel.

### 4.1 A fixed simultaneous continuum/coupling/volume sequence

Retain the earlier family

\[
 a_n=a_0 2^{-n},\quad L_n=4\,2^{2n},\quad
 c_n=g_n^{-2}=c_0+\beta n\log2,
 \quad\kappa_n=2^{n+1}/(a_0c_n),\qquad a_0,c_0,\beta>0.
\]
For `c_n>=2`, Z17–19 prove for every elementary square

\[
 \delta_n\ge\frac{3\,8^8}{2a_0}e^{-Bc_0}
             c_n^7 2^{(1-B\beta)n}.                 \tag{Z21}
\]
Now select the actual member `beta=1/B`, keeping `c0,a0` unchanged. Then
`a_n ->0`, `a_n L_n ->infinity`, `g_n ->0`, and

\[
 \boxed{\|D_{l,n}^{-1}\|
 \le\frac{2a_0e^{Bc_0}}{3\,8^8}c_n^{-7}\longrightarrow0.} \tag{Z22}
\]
The threshold is the explicit integer
`n0=max(0,ceil((2-c0)/(beta log2)))`. These kernels describe elementary local
loop fibres at each regulator; their physical loop size is `a_n`. The path's
coefficient is not assigned a quantum beta-function interpretation.

The power seven uses the retained heat prefactor. Replacing Z10 by Z11 alone
would give just `(3/(2a0)) exp(-Bc0)/c_n` as the corresponding lower bound at
this same beta. Both estimates are recorded, and Z17 proves the extra factor
`(8c_n)^8` relating them.

For a finite list of retained smooth physical observations at regulator n,
let K0 be its raw kinetic Gram and W its actual coupling to K_l,n.
Nonnegativity of the original coupled form gives `W*D_l,n^(-1)W<=K0` by
inserting the actual minimizing lift. The exact resolvent identity therefore
supplies on `|z|<delta_n`

\[
 M_n(z)=\sum_{j=0}^d z^j W^*D_{l,n}^{-j-1}W+\mathcal R_{n,d}(z),
\]
\[
 |x^*\mathcal R_{n,d}(z)y|
 \le\frac{(|z|/\delta_n)^{d+1}}{1-|z|/\delta_n}
                 \sqrt{x^*K_0x}\sqrt{y^*K_0y}.        \tag{Z23}
\]
To prove it, factor the remainder through `D^(-1/2)W`, the multiplier
`(zD^(-1))^(d+1)(I-zD^(-1))^(-1)`, and its adjoint source. Every coefficient
is an original inverse moment. In particular this is continuation through
zero spectral shift with quantified remainder. For the elementary trace,
`K0<=4kappa_n`; choosing `d=n` makes the absolute remainder tend to zero on
every fixed complex disk along Z22, since the logarithm of its upper bound
has the term `-7(n+1)log c_n+O(n)`. No value of a limiting inverse moment or
full coupled resolvent pole is assigned by this statement.

## 5. A second-order local logarithmic vacuum with its full remainder

The rest of the note evaluates the actual local zero-shift response on the
stated small-xi domain. This calculation is independent of the specialization
of beta in Z22.

For two adjacent elementary faces p,q sharing edge e, let
`j_pq=sum_alpha (X_e,alpha W_p)(X_e,alpha W_q)`. Orient their traversals
along e consistently by reversing a complete face word when necessary;
SU(2) trace is unchanged under word inversion. With U the shared link and
A,B the two three-link complementary products, the original Pauli identity is

\[
 j_{pq}=-\tfrac14\operatorname{tr}(UAUB)+\tfrac14\operatorname{tr}(AB^{-1}),
 \quad j_{pq}^0=\tfrac38\operatorname{tr}(AB^{-1}),
 \quad j_{pq}^1=j_{pq}-j_{pq}^0.                      \tag{Z24}
\]
Haar integration of the original quaternion U gives `E_U j_pq=j_pq^0`.
The shared-link Casimir on these two components has eigenvalues 0 and 2.
The other six original links each contribute `3/4`. Thus the total original
Casimir eigenvalues are `9/2` and `13/2`. This retains both components and
their original norms `9/64` and `3/64`.

Define the actual local polynomial

\[
 u_2=-\frac1{72}\sum_p(W_p^2-1)
       +\sum_{\{p,q\}\ \mathrm{adjacent}}
            (\tfrac4{81}j_{pq}^0+\tfrac4{117}j_{pq}^1). \tag{Z25}
\]
The pairs are unordered, counted once. Every face in these sums is contained
in the original graph. `K(W_p^2-1)=8(W_p^2-1)`, and expansion of
`|grad u1|^2` gives the exact equality

\[
 Ku_2=|\nabla u_1|^2-|P|/3.                           \tag{Z26}
\]
Indeed the self terms are `(1/9)sum_p(4-W_p^2)` and each adjacent pair occurs
with coefficient `2/9`. The eigenvalues just computed give Z25 term by term.
This fixes an explicit Haar-mean-zero coefficient representative for u2;
the actual u and its ground energy are not changed.

Put `b_e^2=X_e u2`. The following local constants hold for every edge:

\[
 |b_e^2|\le B_2=146/117,\qquad
 \sum_f\|X_f b_e^2\|_{op}\le H_2=476/117.             \tag{Z27}
\]
Here are the counts and bounds. An edge is in at most four self terms, at
most six adjacent pairs sharing that edge, and at most 36 pairs in which it
is unshared. For a trace word with length N and m_e occurrences of e,
unit-direction generator insertions bound its gradient by m_e and its summed
second-derivative block norms by `m_e N/2`. Apply this to the length-eight
and length-six words in Z24, retaining the two occurrences of the shared link.
For j use gradient bounds 1 (shared), 1/2 (unshared), and second-derivative
row bounds 2 and 7/4. For j0 use 0 and 3/8 in the gradient and 0 and 9/8 in
the second-derivative row. The pair in Z25 is `(4/117)j+(16/1053)j0`.
The self contributions to the two totals are 2/9 and 8/9. Therefore

\[
 B_2=2/9+6(4/117)+36(8/351),
 \quad H_2=8/9+6(8/117)+36(9/117).
\]
These are upper bounds on the original differentiated words, not rewritten
independent variables.

Set `u_app=xi u1+xi^2 u2` and `r_e^2=X_e(u-u_app)`. Its retained scalar
energy is `E_app/kappa=2xi|P|-xi^2|P|/3`. Direct expansion proves

\[
 \Delta u_{\rm app}+|\nabla u_{\rm app}|^2
 =V/\kappa-E_{\rm app}/\kappa+R_{\rm app},
 \quad R_{\rm app}=2\xi^3 b^1\cdot b^2+\xi^4|b^2|^2,
\]
\[
 \mathscr Lr_e^2=-X_eR_{\rm app}-2\sum_i r_i^2 X_i b_e^{\rm app}. \tag{Z28}
\]
In differentiating the dot products, the two commutator corrections cancel
against each other, by antisymmetry. Consequently

\[
 |X_eR_{\rm app}|\le2\xi^3(H_1B_2+B_1H_2+\xi B_2H_2).
\]
At an edge and configuration maximizing `|r_e^2|` over the entire finite
graph, the antisymmetric-Hessian argument yields

\[
 (1/2-2\xi H_1-2\xi^2H_2)\sup|r^2|
 \le2\xi^3(H_1B_2+B_1H_2+\xi B_2H_2).
\]
For `0<xi<=1/32`, the left coefficient is at least `4873/14976>1/4`, and
`8(H1 B2+B1 H2+B2 H2/32)=975838/13689<72`. We have proved

\[
 \boxed{|b_e-\xi b_e^1-\xi^2b_e^2|\le72\xi^3
                  \quad(0<\xi\le1/32).}              \tag{Z29}
\]
All constants are independent of the exterior box.

## 6. Exact parity and a second-order marginal estimate

The central link map

\[
 (\mathcal ZU)_{(n,i)}=(-1)^{\sum_{j<i}n_j}U_{(n,i)} \tag{Z30}
\]
is an involution, preserves original Haar, and commutes with every X.
Multiplying its four signs around each contained face gives -1. Therefore
u1 is odd, u2 is even, and differentiation preserves those parities. No
invariance of the interacting vacuum under this map is asserted or used.

For the original elementary loop C, let S0 be its edges and those of the
twelve other faces meeting it; `|S0|=32`. Let S1 contain all edges of every
contained face meeting S0. Infinite-lattice counting gives `|S1|=108` and
`m_(S1)=173`; boundary truncation only reduces these two upper bounds. The
checker enumerates the actual edge and face sets, also on L=2. Derivatives
b2 on C, and b1 on any edge of S0, are supported inside S1.

At a fixed exterior of S1, retain the conditional density mu on its original
Haar variables. Let `t=2xi u_(1,S1)`, where u_(1,S1) contains exactly the
faces meeting S1. Its Haar mean is zero and `|t|<=B_d=4(173)xi/3`.
Z5 integrated along original link paths gives an oscillation at most
`R_d=4pi(108)A xi^2` for `log rho-t`. Comparing the two explicit conditional
density integrals, and using `int exp(t)>=1`, gives

\[
 |\mu-1-2\xi u_{1,S1}|\le E_2,
 \quad E_2=e^{B_d}\left[e^{R_d}-1+\frac{B_d^2}{2}(2+B_d)\right]. \tag{Z31}
\]
For completeness, `|exp(t)-1-t|<=B_d^2 exp(B_d)/2` bounds both the numerator
remainder and `int exp(t)-1`. The factor `(2+B_d)` follows by writing
`exp(t)/int exp(t)-(1+t)` and retaining the denominator. The oscillation
bound compares mu with that exact exponential density by a ratio in
`[exp(-R_d),exp(R_d)]`.

For an even polynomial P supported in S0, the linear contribution of t to
its Haar integral is zero. A face not fully contained in S0 has an unmatched
integrated link in S1; a face contained in S0 is odd under Z30 while P is
even. Thus

\[
 |\langle P\rangle_\rho-\langle P\rangle_H|
       \le E_2\int_H|P|.                             \tag{Z32}
\]
The same proof holds for complex linear combinations with that parity.
For an odd polynomial supported in S1, its Haar mean is zero; Z4 and the
local marginal ratio give

\[
 |\langle P\rangle_\rho|
 \le\delta_1\int_H|P|,\quad
 \delta_1=e^{32\pi(108)\xi}-1.                       \tag{Z33}
\]
More generally, for every polynomial supported in S1 the same original
marginal ratio gives `|<P>_rho-<P>_H|<=delta1 int_H |P|`.
This records the density's contribution, rather than setting the actual
odd expectation to zero.

## 7. Trial vectors and all conditional derivative scores

Let `F=tr Omega`, `J=sum_(12 neighbors p) j_(pC)`, and
`w=(2kappa xi/3)J`. In the local observation of section 4 the actual forcing is

\[
 W=-Q_l\mathcal AF=Q_l(w+2\kappa d),\quad
 d=\sum_{e\in C}(b_e-\xi b_e^1)\cdot X_eF,
 \quad |d|\le\ell A\xi^2.                            \tag{Z34}
\]
The omitted-in-the-kernel own-face term is explicitly
`(xi/3)(4-F^2)`; it is a function of Omega, so applying Q_l to it is zero.
Z29 gives `d=xi^2 d2+r_d`, with `d2=sum_(e in C)b_e^2.X_eF`,
`|d2|<=ell B2`, and `|r_d|<=72ell xi^3`. Under Z30, d2 is odd.

Use `z=kappa omega`, with inverse `omega=z/kappa`, and `|omega|<=1/4`.
In the original face coordinates set

\[
 y_z=\frac{2\xi}{3}\sum_{p=1}^{12}
   \left(\frac{j_p^0}{9/2-\omega}
                   +\frac{j_p^1}{13/2-\omega}\right),
 \qquad (\kappa K-z)y_z=w.                           \tag{Z35}
\]
For the conditional Haar map E0 at fixed `(Omega,Z)`, each summand has zero
mean. Flip the shared loop edge and one other loop edge not in p; the two
central signs preserve Omega and Haar on its fibre, and flip both j_p^0
and j_p^1. Thus `E0 y_z=0`. This also gives `E0 Y y_z=0` and
`E0 X_f y_z=0` for exterior f, by their exact conditional derivative formulas.

The original Haar norms and differentiated words give, throughout the disk,

\[
 \|w\|_H=\kappa\xi,\quad \|y_z\|_H\le J_*\xi,
 \quad\|y_z\|_\infty\le P_*\xi,\quad
 \sum_e\|X_ey_z\|_\infty\le L_*\xi,
\]
\[
 J_*=\sqrt{12/289+4/625},\quad P_*=736/425,\quad L_*=2752/425. \tag{Z36}
\]
To reproduce the last two constants, write a summand of `y_z/xi` as
`a j_p+b j_p^0`. One has `|a|<=8/75`, `|b|<=64/1275`,
`|j_p|<=1`, `|j_p^0|<=3/4`, `sum|Xj_p|<=4`, and
`sum|Xj_p^0|<=9/4`. Summing twelve gives exactly Z36. The first norm is
`12(4/9)(9/64+3/64)=1`; the second retains both denominators and gives
`(3/4)/(17/4)^2+(1/4)/(25/4)^2=12/289+4/625`.

Put `p_z=P_l y_z`, `Y_z=Q_l y_z`, and
`eta=exp(128pi xi)-1`. The actual-to-Haar fibre ratio lies in
`[exp(-128pi xi),exp(128pi xi)]`; therefore
`||p_z||_rho<=eta P_* xi`.

Here is a bound on all derivatives of this projection, including all exterior
links. In oriented loop coordinates use
`Y_alpha=(1/ell)sum_(j,beta)(Ad(V1...V_(j-1)))_(alpha,beta) X_(j,beta)`.
Its Haar divergence is zero and `Y J_l f=J_l X_Omega f`. Set

\[
 S_\Omega=Y\log\rho-J_l(X_\Omega\log m),\qquad
 S_f=X_f\log\rho-J_l(X_f\log m)\quad(f\notin C),
\]
where m is the actual `(Omega,Z)` marginal. Differentiation under the compact
conditional integral gives
`X_Omega E_l h=E_l(Yh)+E_l(h S_Omega)` and
`X_f E_l h=E_l(X_fh)+E_l(h S_f)`. Each score has conditional mean zero.

Prefix variation in g_j, at fixed Omega, has the exact coordinate formula

\[
 Z_{j,\alpha}=\sum_\beta\left[
  (\operatorname{Ad}g_{j-1}^{-1})_{\beta\alpha}X_{V_j,\beta}
 -(\operatorname{Ad}g_j^{-1})_{\beta\alpha}X_{V_{j+1},\beta}\right],
 \qquad g_0=I.
\]
It differentiates the adjacent links `V_j,V_(j+1)` with opposite transported
generators. Define `z_j=(Ad g_(j-1)) X_(V_j) h`; each adjoint is orthogonal
in the original three generator coordinates. Then `Z_j h=z_j-z_(j+1)`.
The path
incidence matrix therefore has squared norm
`c_ell=2+2cos(pi/ell)<=4`. The exact identity
`4 sum|z_j|^2-sum|z_j-z_(j+1)|^2>=0` also suffices. Product-Haar Poincare
on the ell-1 prefixes and the same density ratio prove

\[
 \operatorname{Var}(h\mid\Omega,Z)
 \le\tfrac43 e^{128\pi\xi}\,E_\rho\sum_{j,\alpha}|Z_{j,\alpha}h|^2.
\]
For exterior f, `X_e b_f=X_f b_e` whenever `e in C`, so integration yields

\[
 \int m\left(\ell\operatorname{tr}\Gamma_\Omega+
                   \sum_{f\notin C}\operatorname{tr}\Gamma_f\right)
 \le\xi^2\overline\Gamma(\xi),                       \tag{Z37}
\]
\[
 \overline\Gamma(\xi)=\ell(8/3+2A\xi)^2+
 \frac{16}{3}c_\ell e^{128\pi\xi}\ell
       (\sqrt{7/3}+\sqrt{128A/3}\,\xi)^2.
\]
In this formula Gamma is the actual conditional score covariance. The
`7/3` follows from the original second-derivative Frobenius bound `3/4`:
for fixed e, the incident plaquette multiplicities satisfy
`sum_f t_ef^2=r_e^2+3r_e<=28`, and the factor `(1/3)^2` gives `28/12`.
Z5 bounds the remainder Hessian in the full derivative sum. The Omega
part uses `ell |Y log rho|^2<=sum_(e in C)|X_e log rho|^2` and
`|b_e|<=4xi/3+Axi^2`.

Using the zero conditional Haar means after Z35 and Cauchy–Schwarz for the
score terms gives

\[
 \sqrt{q_\rho(p_z)}\le\sqrt\kappa\,\xi P_E,
 \quad P_E=\eta L_*+P_*\xi\sqrt{\overline\Gamma(\xi)}. \tag{Z38}
\]
The first summand bounds the density difference on every differentiated
trial column. The second is bounded by `||y_z||_infty` times the square root
of the complete score covariance in Z37. The q pairing here contains both
`ell |X_Omega E_l y|^2` and all original exterior derivatives.

## 8. Complex residual identity and an evaluated fourth-order error

For `0<xi<=10^(-5)`, Z16–19 give `D_l>=kappa/2`; e.g.
`exp(128pi/10^5)<3/2`. Thus the disk `|z|<=kappa/4` is in its resolvent set.
All trial and projected functions are smooth at each finite regulator, so
all expressions below have their original operator domains. The same
calculation also holds as a closed-form identity.

Let `R_z=W-(D_l-z)Y_z`. For every `h in H^1 intersect K_l`, direct use of
Z34–35 gives the exact weak residual

\[
 \langle R_{\bar z},h\rangle
 =2\kappa\langle d+b\cdot\nabla y_{\bar z},h\rangle
                              +q_\rho(p_{\bar z},h). \tag{Z39}
\]
Complex conjugation in the first slot is explicit. Set

\[
 B_b=B_1+A\xi,\quad R_0=2(\ell A+B_bL_*),\quad
 E=\sqrt2 R_0\xi+P_E.
\]
Z19 and Z38 give
`||D_l^(-1/2)R_z||<=sqrt(kappa) xi E`. Factoring the actual inverse through
`D_l^(-1/2)` gives `||(I-zD_l^(-1))^(-1)||<=2`. Therefore the exact identity

\[
 M(z):=\langle W,(D_l-z)^{-1}W\rangle
 =B_z+\langle R_{\bar z},(D_l-z)^{-1}R_z\rangle,
\]
\[
 B_z=2\langle W,Y_z\rangle-q_z(Y_{\bar z},Y_z),
 \quad q_z(f,h)=q_\rho(f,h)-z\langle f,h\rangle        \tag{Z40}
\]
has remainder bounded in absolute value by `2kappa xi^2 E^2`.

The complete expansion of B_z is conveniently written as a bilinear
integral `B(f,h)=int rho f h` (ordinary conjugate-linear pairings are still
used in norms):

\[
 \begin{split}
 B_z={}&B(w,y_z)+2\kappa B(b\cdot\nabla y_z,y_z)
                 +4\kappa B(d,y_z)\\
       &-4\kappa B(d+b\cdot\nabla y_z,p_z)
                 -q_z(p_{\bar z},p_z).               \tag{Z41}
 \end{split}
\]
It follows by expanding `Y_z=y_z-p_z`, using
`(mathcal A-z)y_z=w-2kappa b.grad y_z`, and the original symmetry of the
Dirichlet form. Thus every projection and state cross term remains.

The Haar value of the first term is

\[
 M_H(z)=\kappa\xi^2\left[
        \frac{3/4}{9/2-z/\kappa}+\frac{1/4}{13/2-z/\kappa}\right]. \tag{Z42}
\]
This uses the original twelve neighbor integrals and their unmatched-link
cross-pairing witnesses. Both w and y_z are even and supported in S0, so
Z32 bounds their density correction by `kappa xi^2 E2 J_*`.
The cubic terms `b1.grad y_z times y_z` and `d2 y_z` are odd under Z30 and
supported in S1; use Z33 on them. Use Z5 on the remaining b term, Z29 on
the remaining d term, and Z38 on the last line of Z41. These explicit steps
prove

\[
 \boxed{|M(z)-M_H(z)|\le\kappa\xi^4 C(\xi)
                     \quad(|z|\le\kappa/4),}         \tag{Z43}
\]
where, with `H0=1024pi xi`,

\[
\begin{split}
 C(\xi)={}&\frac{E_2J_*}{\xi^2}
 +\frac{\delta_1}{\xi}J_*(2B_1L_*+4\ell B_2)
 +e^{H_0/2}J_*(2AL_*+288\ell)\\
 &+4\frac\eta\xi P_*(\ell A+B_bL_*)
 +(P_E/\xi)^2+\tfrac14(\eta/\xi)^2P_*^2
 +2(E/\xi)^2.                                        \tag{Z44}
\end{split}
\]
No limiting notation conceals a regulator constant in this finite bound.

At `xi=10^(-8)`, exact outward rational arithmetic in the checker gives
`C(xi)<26,000,000`. It uses `c_ell<=4`, the alternating Machin enclosure
for pi, integer-square upper bounds for each square root, and an exponential
Taylor polynomial with its explicit positive tail. A second, independent
arithmetic path uses only `pi<22/7`, six explicit rational square upper
bounds, and `exp(t)-1<=t/(1-t)` for `0<=t<1`; it gives the larger still-valid
integer upper bound `25,222,642`. Z43 therefore yields

\[
 \boxed{\left|M(0)-\frac8{39}\kappa\xi^2\right|
       <26,000,000\,\kappa\xi^4.}                   \tag{Z45}
\]
Both functions in Z43 are holomorphic on a neighborhood of the closed disk.
Cauchy's derivative formula on its original radius `kappa/4` gives

\[
 \boxed{\left|\|D_l^{-1}W\|_\rho^2-
                        \frac{196}{4563}\xi^2\right|
       <104,000,000\,\xi^4.}                        \tag{Z46}
\]
Here `M'(0)=<W,D_l^(-2)W>`, and
`(3/4)/(9/2)^2+(1/4)/(13/2)^2=1/27+1/169=196/4563`.
In coefficient form the error radii are respectively `2.6*10^(-9)` and
`1.04*10^(-8)`. These are errors in the displayed coefficients, not a claim
of relative error with respect to an unspecified small denominator.

## 9. Original coupled energy and the exterior comparison

Write `f=F-<F>_rho`, `G=||f||_rho^2`, and
`K0=q_rho(J_l f)=kappa(4-<F^2>_rho)`. The calculation Z47a–d below implies, at `xi=10^(-8)`,

\[
 |G-1|<1.1\,10^{-13},\qquad |K_0-3\kappa|<1.1\,10^{-13}\kappa. \tag{Z47}
\]
The underlying means are unchanged by retaining the exterior in the
observation: both are the same original rho integrals. In fact the new
second-order calculation gives a substantially sharper description of them.

Write `j_a=sum_(e in C)b_e^a.X_eF` for a=1,2 and
`j=b.grad F=xi j1+xi^2 j2+r_j`, `|r_j|<=72ell xi^3`.
Stationarity of the original weighted Laplacian applied to F and F squared
gives the exact identities

\[
 3\langle F\rangle=2\langle j\rangle,\qquad
 \langle F^2\rangle-1=\tfrac12\langle Fj\rangle.       \tag{Z47a}
\]
Here `j1=(4-F^2+J)/3` is even, `j2` is odd, and
`int_H |j1|<=3/2`. Equations Z32–33 and Z29 give

\[
 |\langle F\rangle-2\xi/3|\le e_\mu,
 \quad e_\mu=\xi E_2+\tfrac23\ell B_2\xi^2\delta_1
                                    +48\ell\xi^3.   \tag{Z47b}
\]
The original finite Haar coefficients needed in the second identity are

\[
 \langle Fj_1 u_{1,S1}\rangle_H=2/9,\qquad
 \langle Fj_2\rangle_H=-1/18.                         \tag{Z47c}
\]
For the first, the own-face term gives
`(4<F^2>_H-<F^4>_H)/9=2/9`. Every other face paired with the own term has
an unmatched exterior link. In the J term, a neighboring trace can cover
its three exterior links only by being that same neighbor. Its contribution
then integrates `W_p X_e W_p=(1/2)X_e(W_p^2)` in the complementary product;
`int W_p^2=1` makes this zero. A different face leaves an unmatched link.
For the second equality, Haar integration by parts gives
`<Fj2>_H=(1/2)<u2 K(F^2)>_H=4<u2(F^2-1)>_H`.
In u2 only the own self term survives: its covariance is `-1/72`.
Every other self term integrates its nonconstant spin-one character to zero;
every adjacent pair has six distinct unshared links, at least one outside
the four-link C. That original link annihilates its pairing. These arguments
account for every term of the global u2 without an extensive error.

The finite error coefficients are

\[
 \begin{split}
 \epsilon_2={}&\frac{E_2}{2\xi}\frac{\sqrt5+3/2}{3}
               +\frac{\delta_1}{2}\frac{\ell B_2}{\sqrt2}
               +72\ell\xi,\\
 \epsilon_G={}&\epsilon_2+
                  \frac{(4\xi/3)e_\mu+e_\mu^2}{\xi^2}.
 \end{split}
\]
Indeed `int |Fj1| <=(sqrt(5)+3/2)/3`, and
`int |Fj2| <=ell B2/sqrt(2)` by
`int F^2 |X_eF|^2=1/2`. Use Z31 for the first linear density contribution,
Z33's simple density bound for the second, and the uniform r_j bound for
the last. Substitution in Z47a proves the actual enclosures

\[
 \boxed{\begin{gathered}
 |\langle F^2\rangle-1-(7/36)\xi^2|\le\epsilon_2\xi^2,\\
 |G-1+(1/4)\xi^2|\le\epsilon_G\xi^2,\qquad
 |K_0-\kappa(3-(7/36)\xi^2)|\le\kappa\epsilon_2\xi^2.
 \end{gathered}}                                      \tag{Z47d}
\]
At `xi=10^(-8)`, the outward rational evaluation gives
`e_mu<1.282*10^(-19)`, `epsilon2<0.000767`, and
`epsilonG<0.000767`. Thus the original raw Gram is quantitatively retained
even at its second interaction order.

Let `h0=D_l^(-1)W`, `Z0=||h0||^2`, and `F0=K0-M(0)`. For arbitrary
`x in C` and `h in K_l`, define `k=h-h0 x`. Expansion of the original
coupled form, with `W=-Q_l mathcal A f`, proves

\[
 q_\rho(xf+h)=F_0|x|^2+q_\rho(k),\qquad
 \|xf+h\|_\rho^2=G|x|^2+\|h_0x+k\|_\rho^2.          \tag{Z48}
\]
At this coupling the exact intervals Z45–47 and Z19 prove

\[
 \boxed{q_\rho(xf+h)\ge(0.74999\,\kappa)\|xf+h\|_\rho^2
                    \quad(h\in H^1\cap K_l).}       \tag{Z49}
\]
For an explicit verification put `m_*=0.74999 kappa` and use
`delta_C>=(3kappa/4)exp(-128pi xi)`. The two by two quadratic form obtained
from Z48 is nonnegative because

\[
 \delta_C-m_*>0,\quad F_0-m_*(G+Z_0)>0,\quad
 [F_0-m_*(G+Z_0)](\delta_C-m_*)-m_*^2Z_0>0.
\]
The checker verifies these inequalities with rational lower/upper endpoints.
The cross term `2 Re <h0 x,k>` is bounded at exactly this step, not deleted.
Thus Z49 covers the entire original local conditional kernel, including its
exterior dependence, together with the observed loop direction.

The corresponding physical restored state is
`Phi=psi(f+D_l^(-1)W)`. Its norm and excitation energy are exactly

\[
 \|\Phi\|^2=G+Z_0,\qquad q_{H-E_0}(\Phi)=K_0-M(0).  \tag{Z50}
\]
It is perpendicular to the actual vacuum because f is centered and the kernel
primitive has conditional mean zero. Its one-dimensional variational
inclusion gives the upper bound `Delta_L<=q(Phi)/||Phi||^2` for the complete
physical gap. The separate lower bound Z49 is on its explicitly stated
form subspace. The new scalar moments also resolve the interaction correction
of this actual restored state's Rayleigh quotient:

\[
 \boxed{\quad
 0.2184<\frac{q_{H-E_0}(\Phi)/(\kappa\|\Phi\|^2)-3}{\xi^2}
                 <0.2248,\qquad \xi=10^{-8}.\quad}    \tag{Z50a}
\]
To verify without discarding the denominator, put
`d0=-1/4+196/4563`, and write the exact numerator and denominator in Z50
using Z45–46 and Z47d. The coefficient at their ratio is

\[
 \frac{337/1521+e}{1+\xi^2(d_0+e_d)},\quad
 |e|\le\epsilon_2+26,000,000\xi^2+
                  3\epsilon_G+312,000,000\xi^2,\quad
 |e_d|\le\epsilon_G+104,000,000\xi^2.
\]
Here `337/1521=3/4-7/36-8/39-3(196/4563)` is exact.
The checker retains the original denominator and obtains Z50a by rational
upper and lower bounds. In particular the lowered energy from kernel
restoration and the change in the physical state norm are both included.

### 9.1 Exact return to the previous Omega-only observation

Let E_C denote the earlier expectation onto Omega alone. The conditional
map E_o from `(Omega,Z)` to Omega satisfies

\[
 E_C=E_oE_l,\qquad J_C=J_lJ_o,\qquad K_l\subset K_C=\ker E_C.
\]
The exact quotient map and inverse are

\[
 K_C/K_l\xrightarrow{\cong}\ker E_o,\quad[h]\mapsto E_lh,
 \qquad k\mapsto[J_lk].                              \tag{Z51}
\]
Fubini and `E_l J_l=I` prove both inverse laws. Thus the local response in
Z45 is not assigned to the old full kernel by dropping its additional
exterior fluctuations; Z51 computes those fluctuations.

For any retained coarse form vector g, let `h_l(g)` minimize the original
energy of `J_lg+h` over `h in K_l`, and put
`S_lg=J_lg+h_l(g)`, `q_eff(g,v)=q_rho(S_lg,S_lv)`. Z19 proves existence
and uniqueness by the energy Riesz theorem. This extends the smooth forcing
formula `h_l(g)=D_l^(-1)(-Q_l mathcal A J_lg)` to its actual form domain.
At a fixed finite regulator the original centered physical gap is positive
by compactness and uniqueness of the vacuum. Consequently there is a unique
`k_* in ker E_o` minimizing `q_eff(J_o f+k)` on this actual form fibre.
No uniform estimate for this second minimization is inserted.

Orthogonality of the two minimum sections proves the exact response and
state formulas

\[
 M_C(0)=M_l(0)+q_{\rm eff}(k_*),\qquad
 h_C=h_l(J_of)+J_lk_*+h_l(k_*),                        \tag{Z52}
\]
\[
 \|f+h_C\|_\rho^2
 =G+\|k_*\|_m^2+\|h_l(J_of)+h_l(k_*)\|_\rho^2.       \tag{Z53}
\]
The last norm retains the cross pairing of the two original kernel lifts.
Equations Z51–53 are the exact map and energy remainder connecting the
present local estimate to the previous wider observation. The additional
quantity `q_eff(k_*)` has not been bounded uniformly here. Nevertheless
Z45 and Z52 already give a zero-shift bound for that previous observation:

\[
 M_C(0)\ge\kappa\xi^2(8/39-2.6\,10^{-9}),\qquad
 M_C(0)\le K_0,\qquad \xi=10^{-8}.
\]
The lower bound is obtained through the exact inclusion of the local
primitive space. No monotonicity of the restored state norm is inferred;
its full cross term is Z53.

## 10. Split Zero primitives and controlled completion

At fixed regulator and loop, choose finite-dimensional nested smooth trial
spaces V_j in K_l. Use the actual support-indexed windows

\[
 V_j\xrightarrow{D_l}K_l\xrightarrow0 0.
\]
Since D_l is invertible, the transported-class kernel and both inverse maps are

\[
 V_{j+1}/V_j\xrightarrow{\cong}
 \ker[K_l/D_lV_j\to K_l/D_lV_{j+1}],\quad[h]\mapsto[D_lh],
 \qquad[D_lh]\mapsto[h].                             \tag{Z54}
\]
Give K_l the original dual-energy pairing `<r,t>_-1=<r,D_l^(-1)t>`.
Then `<D_lh,D_lv>_-1=q_rho(h,v)`. The minimum residual of the forcing W
at support j has quotient squared norm equal to the exact remaining
response error. For a noncanonical trial Y, write
`aY=q(Y)`, `cY=<Y,W>`, `alphaY=cY/aY`. Its correction and norm identity are

\[
 R=W-D_lY=R_{\rm can}+(\alpha_Y-1)D_lY,
\]
\[
 \langle R,D_l^{-1}R\rangle
 =\|[W]\|_{K_l/D_l\operatorname{span}Y}^2
                          +a_Y|\alpha_Y-1|^2.        \tag{Z55}
\]
At Y=Y_0 from Z35, positivity of aY follows from Z19 and Y0 nonzero: its
Haar norm is positive, while the explicit projection bound in section 7 is
smaller than its rho norm at `xi=10^(-8)`. Z55 keeps the canonical correction
in the original incoming image. The reconstruction of [SZ] sends a killed
relation to its receiving support's zero and retains these actual primitives.

For an optional simultaneous-family completion, take one elementary loop at
each n on the exact path Z22 and form
`mathscr K=direct_sum_(n>=n0) K_l,n` with the original counting sum of its
rho_n pairings. The diagonal operator `mathscr D=direct_sum D_l,n` has domain
`{(h_n):h_n in Dom D_l,n, sum||D_l,n h_n||^2<infinity}`. Its inverse is the
literal coordinate map `(r_n)->(D_l,n^(-1)r_n)`. Testing coordinatewise and
using the uniform tail bound proves both inverse laws and self-adjointness.
Its finite-support truncation error is at most

\[
 \|\mathscr D^{-1}-\mathscr D^{-1}P_{\le N}\|
 \le\frac{2a_0e^{Bc_0}}{3\,8^8}c_{N+1}^{-7}.          \tag{Z56}
\]
Each finite block inverse is compact and this tail tends to zero, so the
original family inverse is compact. This completion has regulator-indexed
vectors and the displayed sum pairing. No identification of it with a
four-dimensional physical Hilbert space is part of the construction.


There is also an explicit completion-killed cohomology module on these same
operators. Let `mathscr K_fin` denote the original finite-support vectors and
use the two windows

\[
 \bigoplus_{\mathrm{alg},n}\operatorname{Dom}D_{l,n}
       \xrightarrow{\mathscr D}\mathscr K\longrightarrow0,
 \qquad
 \operatorname{Dom}\mathscr D\xrightarrow{\mathscr D}\mathscr K
       \longrightarrow0.
\]
Their actual first cohomologies are `mathscr K/mathscr K_fin` and zero.
The transition kernel is the full first quotient, with inverse primitive
`[r] -> [mathscr D^(-1)r]` in
`Dom mathscr D/(algebraic direct sum Dom D_l,n)`. Both inverse laws follow
coordinate by coordinate from the already proved inverses D_l,n. Thus no
class is deleted by the completion without its displayed primitive.

For a concrete nonzero class take a fixed original neighboring plaquette at
each regulator, `h_n=Q_l,n W_(p,n)`, and `r_n=2^(-n)h_n`.
Every h_n is nonzero: the two-link central flip preserving Omega and exterior
changes W_p, and the conditional density is everywhere positive. Also
`||h_n||<=2`, so r is square summable and has infinitely many nonzero
coordinates. Hence its class modulo finite support is nonzero. Its completed
primitive is `(2^(-n)D_l,n^(-1)h_n)_n`, and Z56 controls its tail.
The algebraic quotient's induced Hilbert seminorm vanishes because finite
support is dense; the exact quotient and primitive above retain the source
information behind that zero seminorm. This is an independently proved
application of [SZ] to the actual operator family.

## 11. Scope, verification, and the next original quantity

The zero-shift numerical certificate concerns the actual local observation
`(Omega, all exterior links)` at `xi=10^(-8)`, for every a>0 and L>=2.
It is supplied with an exterior-independent finite error, a second-order
log-vacuum remainder, and the exact comparison to the predecessor's
Omega-only observation. The all-coupling heat/conditional-kernel estimates
are evaluated on their separate explicit weak-coupling continuum path.
A physical continuum field and a uniform positive mass lower bound for the
complete physical Hilbert space have not been established.

The checker evaluates exact quaternion identities, original graph supports,
integer and rational constants, complex block identities, and intentionally
false formulas. It does not replace the written semigroup, elliptic-domain,
or limiting arguments by finite tests. Both ordinary and optimized Python
runs and their source-bound receipts are recorded separately.

The next original quantity is the outer effective response in Z52 on growing
retained observations, together with the full norm Z53 and the primitive
norm of the original physical gradient. The local zero-shift inverse and
its actual response are now available as proved inputs. Peer updates found
in this cycle are recorded with their actual reading scopes, without
assigning unexamined arithmetic constants to these Yang–Mills measures.

### Sources actually used

[YM] `KokunoYumeto/yang-mills-interacting-workbench`, main
`fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`,
`yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`
and `yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md`;
original operator, domains, vacuum and local exterior decomposition.

[ALM] Preserved preceding delivery `yang_mills_actual_loop_moments.zip`,
original `RESEARCH_NOTE.md` and `verify.py`; Z3–5, Pauli identities and the
twelve-face calculation are reproduced here. The exact local byte identities
and replay are in this contribution's records. The complete twenty used
quaternion/Haar/graph/arithmetic blocks are included in `exact_algebra.py`
with their source-block hashes in `algebra-provenance.json`. The offline
package also retains the full preceding delivery; the Git checker requires
only files in its own directory.

[SZ] `KokunoYumeto/zeta-function-research-reader`, revision
`464a0d0c150ca9ed700335385d4892d18922b028`,
`formal/splitzero/DERIVED_MATHEMATICS.md`, sections 1–4,
blob `fe05d32ccd314daac7c59d225c9cac3d4c1bf3d3`, reconstruction and transported-class
kernel construction; the original minimum-section correction is also retained
in the OPR/observation-metric sources read by the preceding workbench cycle.
No new Lean replay is claimed.

[HK] A. Nowak, P. Sjögren, T. Z. Szarek, *Sharp estimates of the spherical heat
kernel*, arXiv:1802.09385v2, equations (1)–(4), and the original sphere measure
convention; J. Math. Pures Appl. 129 (2019), 23–33. The original PDF equations
on pages 2–3 were inspected. Time, measure and quaternion maps are Z6–8.


# The complete connected cubic vacuum source in original SU(2) link coordinates

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260916-cubic-linearized/CUBIC_SOURCE.md}

\textbf{SHA-256:} \path{d1e8fa24ce573ad1adfdaeecbb2ee6bfa1631717f9ce22b0f66d838981d5f240}
\end{quote}


16 September 2026. This note executes the first of the two tasks retained in the delivered gauge-native checkpoint: calculate the connected third logarithmic-vacuum coefficient. `LINEARIZED_RETURN.md` executes the second task on the same coefficients. The preceding delivered second-source result had endpoint g^2 = sqrt((32+sqrt(354))/3); that stronger saved result is the comparison here. No historical-priority claim or independent analytical-review claim is made.

## C1. Original operator and source

Fix L>=2, vertices {-L,...,L}^3, every contained positively oriented nearest-neighbor edge e=(n,i), and every contained plaquette p=(n;i,j), i<j. Its actual word is

    W_p=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)).

Put T_alpha=-i sigma_alpha/2, X_e,alpha f=d/dt f(...,exp(t T_alpha)U_e,...) at zero, E_e=-sum_alpha X_e,alpha^2, and K=sum_e E_e. The Hilbert space has original product Haar probability dU; the physical subspace consists of vertex-gauge invariant functions, including all boundary vertices. Retain

    H=kappa K+kappa xi(2M-S),  S=sum_p W_p,  M=|P_L|,
    kappa=2g^2/a,  xi=1/(4g^4),  a,g>0.                         (C1)

Operator and form domains are the physical parts of H^2 and H^1 on the original compact product. The potential is smooth and bounded at each finite L. The actual vacuum is smooth and strictly positive. These original domains and the ground-state identity are supplied in `finite_box_weak_coupling_physical_gap.md` at Git fab69fdc4ac197159b8e6ae8d73a82bde2b20d55, blob dfee77c0ca0d6ed897c4172fcbfe23cd9d10d313, section 1.

Let P_H f=int f dU, Q_H=I-P_H, and Gamma(f,h)=sum_(e,alpha) (X_e,alpha f)(X_e,alpha h). Define, on zero-Haar-mean physical coefficients,

    B(f,h)=K^(-1) Q_H Gamma(f,h),
    v=xi v_1+B(v,v),   v_1=S/3,
    v_n=sum_(i=1)^(n-1) B(v_i,v_(n-i)).                     (C2)

The inverse K^(-1) acts only on actual nonconstant representation blocks. Scalars removed by Q_H remain recorded. Once the series is summed, set

    c_L=-(1/2)log int exp(2v)dU,
    psi=exp(v+c_L),  C_L=int Gamma(v,v)dU,
    E_0=2kappa xi M-kappa C_L.                             (C3)

The companion proof constructs convergence and proves that these are the original vacuum and energy. No vacuum, measure, or coupling is assigned from the auxiliary coefficient norm below.

## C2. Original Fourier coefficients and the two spin budgets

In the original product spin basis write f_j(U)=Tr(A_j pi_j(U)), and c(j)=sum_e j_e(j_e+1). For each original nonempty union label S_0 retain A_(S_0,j), even when its active spin support is smaller. A zero coefficient at a present union is retained at that union. Assembly sums these matrices for each j. Its kernel consists exactly of coefficient families with sum_(S_0) A_(S_0,j)=0 for every j. The differences between an occurrence at S_0 and its occurrence at the actual active support span this kernel and retain the original coefficient matrices.

The auxiliary coefficient norm and budgets are

    ||f||loc=max_a sum_(S_0 contains a,j!=0) c(j)||A_(S_0,j)||_1,
    m(f)=max_a sum_(S_0 contains a,j!=0) (sum_e j_e)||A_(S_0,j)||_1,
    t(f)=sup_e sum_(S_0 contains e,j!=0) j_e||A_(S_0,j)||_1.       (C4)

Every nonzero physical Fourier block obeys c(j)>=6j_e. To verify the gauge input, at each endpoint v of e the actual invariant vertex tensor gives j_e<=sum_(f incident v,f!=e)j_f. The other edges A_e at both endpoints therefore have total spin at least 2j_e. Their remote endpoints are distinct because the cubic graph has no triangles. At these remote endpoints the same invariant inequality gives sum_(f in A_e)j_f<=2 sum_(f outside A_e union {e})j_f; each exterior edge is counted at most twice. Thus sum_f j_f>=4j_e. For every nonzero half-integer spin, j(j+1)>=3j/2. This proves

    c(j)>=6j_e,  sum_e j_e<=2c(j)/3,
    t(f)<=||f||loc/6,  m(f)<=2||f||loc/3.                 (C5)

The gauge tensor exists in every physical coefficient block: decomposing at a vertex is an orthogonal decomposition under that vertex's unitary representation, and the invariant projection kills a block without an invariant intertwiner. This proves the use of the spin inequalities for the actual coefficients. In particular every nonconstant physical block has c(j)>=3.

The full coefficient-product inequality is

    sum_output ||A_output(f_j h_k)||_1<=||A_j||_1||A_k||_1,
    ||A(X_e,alpha f_j)||_1<=j_e||A_j||_1.                 (C6)

For the first, the product coefficient is A_j tensor A_k. Unitary decomposition of the original tensor representations, pinching to all diagonal irreducible blocks, and partial trace over their multiplicity spaces give the actual product coefficients. Pinching is an average of unitary conjugations and has trace-norm bound one. The partial-trace bound follows from |Tr((Z tensor I)A)|<=||A||_1 for ||Z||op<=1. This retains every output multiplicity. The second bound uses the original spin-generator operator norm j_e; all three generator indices remain in Gamma.

For an anchor in the first input union, the absolute product sum is at most 3m(f)t(h). Anchoring in the other input gives 3m(h)t(f); double counting their intersection is a bound. Output c(j) cancels the exact inverse Casimir in C2. Hence

    ||B(f,h)||loc<=3[m(f)t(h)+m(h)t(f)],
    ||B(f,h)||loc<= (2/3)||f||loc||h||loc.                 (C7)

These are estimates on the original labelled coefficient source. The physical pairing is still int rho conjugate(f)h dU, with rho=psi^2, and its energy pairing is kappa int rho sum conjugate(Xf)Xh dU.

## C3. Original loop norms and the complete second coefficient

For a simple original closed link loop of length ell, let t be the number of local maxima of n_1+n_2+n_3 along the loop; the number of minima is also t. At extrema the fundamental coefficient tensor has the original alternating two-index contraction, of Euclidean norm sqrt(2). At each other vertex it has the two-dimensional identity contraction. Separate permutations of original row and column tensor indices expose their tensor product. Their singular values give ||A_loop||_1=2^(ell-t)<=2^(ell-1). No inversion of one link is asserted to preserve a tensor trace norm. For a spin-j plaquette, the same four contractions have dimension 2j+1 and one maximum/minimum pair, giving norm (2j+1)^3. In particular

    ||A(W_p)||_1=8, ||A(chi_1(Omega_p))||_1=27,
    ||A(chi_(3/2)(Omega_p))||_1=64.                       (C8)

These formulas also follow from the literal plaquette index matrix: for spin 1/2 its nonzero entries are

    A_[(i1,i2,1-i2,1-i3),(i0,i1,1-i3,1-i0)] += (-1)^(i0+i2).

There are four nonzero singular values, each two. Keeping indices 0,...,2j and the invariant alternating spin-j form gives (2j+1)^2 singular values, each 2j+1, for the character plaquette.

For adjacent p,q, write P_0 for Haar integration of their shared edge in W_pW_q and P_1=I-P_0 on that product. The two actual Casimirs are 9/2 and 13/2. If x,y denote the two original trace coefficient norms, the exact six-link boundary formula and C6 give

    P_0(W_pW_q)=(1/2)W_boundary(p,q),
    x<=16, x+y<=64.                                      (C9)

It follows either by integrating the original shared matrix entries, int U_ab conjugate(U_cd)=delta_ac delta_bd/2, or by the equivalent SU(2) alternating contraction in its inverse traversal. The boundary orientation is the original oriented concatenation after that contraction.

The Casimir product rule is

    2Gamma(f,h)=(c_f+c_h)fh-K(fh)                         (C10)

for actual Casimir eigenfunctions f,h. Since W_p^2=1+chi_1(Omega_p), its nonconstant self component has Casimir 8. Distinct nonadjacent plaquette products have Casimir 6. Applying C10 to C2 evaluates the entire second source:

    v_2=-(1/72)sum_p chi_1(Omega_p)
       +sum_{unordered adjacent {p,q}}
         [(1/27)P_0(W_pW_q)-(1/117)P_1(W_pW_q)].           (C11)

Nonadjacent terms have the exact multiplier 1/(3*6)-1/18=0 at their original union. Each edge lies in at most four self plaquettes and 42 unordered adjacent pair unions. The latter count is sum_(p contains e) deg(p)-binom(r_e,2)<=12r_e-binom(r_e,2)<=42. Thus

    ||v_1||loc<=32,   ||v_2||loc<=236.                    (C12)

Indeed each self term contributes at most 8*27/72=3; each pair at most x/6+y/18<=16/3.

## C4. All projectors have explicit original-coordinate formulas

For an edge carrying a finite product of the specified spin functions, let J_e be its complete allowed Clebsch-Gordan spin list. On that product space set

    P_(e,j)=product_(l in J_e,l!=j)
        [E_e-l(l+1)I]/[j(j+1)-l(l+1)],
    P_boldj=product_e P_(e,j_e).                          (C13)

Every denominator is a displayed nonzero rational number. The original compact SU(2) decomposition proves that C13 projects onto exactly that spin eigenspace, including its full multiplicity. Different-edge projectors commute. This is a finite polynomial in the original link derivatives, so all coefficient formulas below are effective coordinate formulas. In particular an explicit eigenvalue denominator is not an unspecified inverse problem.

For the cubic product there are five connected types: a self triple; a repeated adjacent pair; three distinct faces with two adjacency edges (path); three distinct faces sharing one edge (common-edge); or three faces forming a cube corner with three different shared edges. This exhausts the original coordinates: coplanar face adjacency is the square grid; two perpendicular faces determine their shared coordinate edge; a third face adjacent to both either contains that same edge or is the third face at one endpoint, with its other two shared edges. All other multisets are disconnected in edge adjacency.

## C5. The full cubic table

Each triple below is an unordered multiset of original faces. Each distinct choice of the outer face in 2B(v_1,v_2) occurs once, with the second coefficient already carrying its original unordered-pair multiplicity.

**Self {p,p,p}.** The contribution is

    -(1/81)W_p+(1/810)chi_(3/2)(Omega_p).                 (C14)

Its Casimirs are 3 and 15. The character product W_p chi_1=chi_(3/2)+W_p and C10 give K times C14 as chi_(3/2)/54-W_p/27.

**Repeated adjacent {p,p,q}.** Let F=(W_p^2-1)W_q. On the shared edge its allowed spins are 1/2 and 3/2. Then the contribution is

    -(11/4212)P_(1/2)F+(11/11232)P_(3/2)F.              (C15)

The respective total Casimirs are 9 and 12. Here the first projector has the concrete recoupling identity

    P_(1/2)F=(4/3)W_p P_0(W_pW_q)-(1/3)W_q.             (C16)

To prove C16, expose the shared original unit quaternion u. The two traces can be written 2u dot v, 2u dot w with v,w unit quaternions formed from the unchanged remaining path products (inverse orientations use their exact quaternion conjugates). Original Haar moments are int u_i u_j=delta_ij/4 and
int u_i u_j u_k u_l=(delta_ij delta_kl+delta_ik delta_jl+delta_il delta_jk)/24. The linear harmonic part of (u dot v)^2(u dot w) is [u dot w+2(v dot w)(u dot v)]/6. Also P_0(W_pW_q)=v dot w. These equations give C16 pointwise, for every original remaining path product.

For full coefficient verification, put H=P_(1/2)F, J=P_(3/2)F, z=P_0(W_pW_q). Then
W_p z=(3H+W_q)/4 and W_p P_1(W_pW_q)=H/4+J+3W_q/4. The two W_q coefficients in K v_3 from the adjacent source are 1/72 and -1/72; they cancel exactly. The self-source product has only H,J. The H coefficient in K v_3 is -1/72-1/2808-1/108=-11/468; the J coefficient is 5/702+1/216=11/936. Division by the original 9 and 12 gives C15. The cancelled W_q component remains a present zero at the original seven-link union.

**Distinct path.** Let F=W_pW_qW_r. On its two distinct shared edges, use P_(s,t), s,t in {0,1}. With n=s+t, its total Casimir and coefficient are

    c=6+2n;
    n=0: 1/162;  n=1: -11/8424;  n=2: 1/3510.          (C17)

The entire contribution is the sum of those four projected functions times their specified coefficients. For a selected channel, there are exactly two nonzero outer-face terms. With (c_0,a_0)=(9/2,1/27) and (c_1,a_1)=(13/2,-1/117), their sum is

    [a_s(3+c_s-c)+a_t(3+c_t-c)]/(3c),

which evaluates to C17. This verifies each factor without a coordinate replacement.

**Distinct common-edge triple.** On the single shared edge, retain the whole spin-1/2 multiplicity space and spin-3/2 space. Their Casimirs and coefficients are

    c=15/2: -2/1755;  c=21/2: 2/2457.                  (C18)

On the original tensor (C^2)^(tensor 3), the three pair singlet projectors obey

    P_0^(12)+P_0^(13)+P_0^(23)=(3/2)P_(total 1/2).       (C19)

One verification is P_0^(ij)=1/4-J_i dot J_j, followed by expansion of (J_1+J_2+J_3)^2. The eigenvalues are 3/4 and 15/4. Thus the total singlet sum has values 3/2 and zero; this proves C19 including both copies of spin 1/2. The pair projectors need not commute, and no product of them is used. Under the original trace map,

    P_(1/2)F=(2/3)sum_outer W_r P_0(W_pW_q).

In C10 the summed pair-spin-zero multiplicity is 3/2 on total spin 1/2 and zero on spin 3/2; the pair-spin-one multiplicities are 3/2 and three. Substitution gives C18.

**Distinct cube corner.** On its three different shared edges use P_(s,t,u), n=s+t+u. The coefficients and Casimirs are

    c=9/2+2n;
    n=0: 2/81; n=1: 34/13689; n=2: -38/17901;
    n=3: 2/2457.                                       (C20)

The entire n=1 projection is exactly zero. At the central original vertex it would have one spin-one edge and two spin-zero edges, which has no invariant vector. We retain the displayed pre-zero coefficient and its zero projected function. The channel coefficient before that zero follows from

    [(3-n)a_0(3+c_0-c)+n a_1(3+c_1-c)]/(3c).

Moreover P_(0,0,0)F=(1/4)W_boundary, a six-link loop. Write the original three face traces as tr(U_a A U_b^-1), tr(U_b B U_c^-1), tr(U_c C U_a^-1). Integrating U_b and U_c supplies two factors 1/2 and leaves tr(U_a ABC U_a^-1)=tr(ABC); integration of U_a leaves this same trace. This proves the complete factor 1/4 and its original boundary product.

Every disconnected triple has zero source because either its second coefficient is zero by C11 or the outer derivative has no original edge in common with that second coefficient. Thus C14–20 calculate all of v_3, with all original union labels and all cancelled or zero channels retained.

## C6. Evaluate the whole cubic source bound

For one cluster the following are bounds in the original Casimir-weighted trace norm:

    self: 40/27;
    repeated adjacent: 66/13;
    path: 1408/351;
    common-edge: 512/117;
    corner: 3504/351.                                   (C21)

For self use 3*8/81+15*64/810=40/27. For repeated adjacent, the two output norms have sum at most 27*8=216. Their largest absolute Casimir-weighted coefficient is 11/468, giving 66/13.

For a path let x_st denote the original norms of its four projections. C6, C9 and the actual boundary integration give

    sum x_st<=512, x_00<=32,
    x_00+x_01<=128, x_00+x_10<=128.

The double spin-zero component is (1/4) times the original eight-link boundary loop, so C8 gives 32. Each single spin-zero projection is the original six-link boundary times the remaining plaquette, divided by two, giving 16*8=128. The absolute Casimir-weighted norm is exactly bounded by

    [3 sum x_st+8(x_00+x_01)+8(x_00+x_10)+20x_00]/1053
    <=4224/1053=1408/351.

For a common-edge triple, sum of both complete projected coefficient norms is at most 8^3=512. Both absolute Casimir-weighted coefficients are 1/117. For a corner the total is at most 512, x_000<=8 by its six-link boundary divided by four, and the other nonzero weighted coefficients are at most 19/1053. Therefore its bound is

    (19*512+98*8)/1053=3504/351.

For each original anchor edge the numbers of clusters in C21 are bounded respectively by

    4, 84, 460, 40, 24.                                 (C22)

Here is a counting proof of the three distinct-face counts. In a cubic periodic counting grid of side at least nine, the two-neighbor patterns are in bijection with their original infinite-grid local coordinates. This is only a finite combinatorial enumeration; no Hamiltonian or measure is transported to that grid. There are three faces per cell, twelve neighbors per face, twelve common-edge triples per cell, and eight corner triples per cell. The number of centered adjacency wedges per cell is 3*binom(12,2)=198. Subtracting three for every triangle leaves 138 paths. Their unions contain ten original edges; common-edge unions also contain ten, and corner unions nine. Translation and axis permutation are explicit bijections of this incidence count. Division of total incidences by three edges per cell gives 460,40,24. Equivalently `geometry.py` enumerates all four anchor faces, all first neighbors, and all second neighbors and retains the resulting original coordinates. The 42 adjacent pairs each have two repeated-face choices. Any finite-box cluster injects into the corresponding original infinite-grid list, proving the same upper counts at boundaries.

Summing all five contributions proves

    ||v_3||loc <= 4*(40/27)+84*(66/13)+460*(1408/351)
                  +40*(512/117)+24*(3504/351)
               =944984/351.                             (C23)

The predecessor's bound obtained before evaluating this source was 30208/3. C23 is less than 2693. The sharper bound follows from the actual channel coefficients and original support geometry; the complete norm remains an upper bound rather than an assigned equality.

## C7. Original fourth vacuum-energy coefficient, with an independent calculation

The link-center involution

    (Zf)(U)=f((s_e U_e)_e), s_(n,i)=(-1)^(sum_(j<i)n_j)

preserves Haar, the gauge action and K, and changes the sign of every original plaquette trace. Hence Z v_n=(-1)^n v_n by C2. It also gives the literal signed-parameter operator identity Z H(xi) Z=H(-xi)+4kappa xi M I. Negative xi is used here solely as the algebraic/analytic source coordinate; no negative physical g is introduced. Thus E_0-2kappa xi M is even.

Let J be the original number of unordered adjacent plaquette pairs. The complete coefficient is

    E_0=2kappa M xi-kappa M xi^2/3
         +kappa(5M/216-2J/1053)xi^4+O(xi^6).            (C24)

To verify it directly from the vacuum source, the only v_3 component pairing with v_1 in Haar energy is the self -W_p/81 in C14. The repeated lower component cancels as proved in C15–16. A product of three distinct faces and one testing face has an edge with odd occurrence: a nonempty set of at most four distinct squares cannot have every edge even, because each other square shares at most one of a chosen square's four edges. Its Haar integral is zero by the center change on that edge. Distinct v_2 labels have the same unmatched-edge argument or different spin sectors. The actual component masses are ||chi_1||_H^2=1, ||P_0(W_pW_q)||_H^2=1/4 and ||P_1(W_pW_q)||_H^2=3/4. Therefore

    int Gamma(v_1,v_3)=-M/81,
    int Gamma(v_2,v_2)=M/648+2J/1053,
    [xi^4]C_L=2*(-M/81)+M/648+2J/1053
              =-5M/216+2J/1053.

Equation C3 proves C24, including its sign.

An independent Rayleigh–Schrodinger coefficient calculation for the original K-xi S gives

    [xi^4](E_0/kappa)=M^2/27
          -(1/9)<Q_H S^2,K^(-1)Q_H S^2>_H,
    <Q_H S^2,K^(-1)Q_H S^2>_H
       =M/8+(2/3)binom(M,2)+(2/117)J.                  (C25)

For completeness, with Haar-constant vacuum coefficient fixed at one, the first two wavefunction coefficients are u_1=S/3 and u_2=K^(-1)Q_H S^2/3. The second energy coefficient is -M/3. Testing the order-three eigen-equation against S and then the order-four constant equation gives the first line of C25. The nonconstant self sector is chi_1/8; a disjoint pair contributes 2/3; an adjacent pair contributes 4[(1/4)/(9/2)+(3/4)/(13/2)]=80/117=2/3+2/117. Cross terms vanish by the same original edge parity. Substitution reproduces C24 exactly.

With m=2L the complete box counts are M=3m^2(m+1), J=6m(3m^2-1). At L=2, C24's fourth coefficient is 1198/351. As L increases, J/M tends to six and its fourth coefficient per plaquette tends to 11/936. On a planar square array the corresponding ratio tends to two, giving 163/8424; the plane-to-space operator defect is recorded in the companion literature section. These are source coefficients, with the exact finite-box counts kept before their limits. The companion note supplies an explicit all-higher-order remainder for C24.

## C8. Verification scope

The independent original-link checker differentiates the actual oriented plaquette products in 2Gamma(v_1,v_2), while the receiving calculation uses C14–20 and Haar projectors. It checks all 612 anchored multisets at two exact rational quaternion assignments. The 24-cell separately verifies the harmonic recouplings using all Haar moments through degree five. The original eight-by-eight singlet matrices verify C19 and reject their false commutation. These finite tests accompany the full coordinate and representation proofs above; they do not replace them or certify a continuum limit.


# The full linearized residual and its return to the original physical gap

\begin{quote}\footnotesize
\textbf{Source classification:} complete delivered mathematical source

\textbf{Repository source:} \path{yang-mills/continuations/20260916-cubic-linearized/LINEARIZED_RETURN.md}

\textbf{SHA-256:} \path{931d8d2824062c6435dfe324cb9145bc6d8e7a450d37aa5f86a94f1190190453}
\end{quote}


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


\part{Historical mathematical final responses}

# Historical final response 1: Split Zero and cubic memory

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/01_split_zero_cubic_memory_20260914.md}

\textbf{SHA-256:} \path{567cc7470ff218a2c8d9b8f058c1f1cb64225f7d3e4c4c7854d2a3175eaa7684}

\textbf{Editorial provenance notice:} The linked standalone mathematical attachment has not been recovered. This chapter preserves the complete mathematical final response only; it is not a recovery of the missing attachment.
\end{quote}

I located **`KokunoYumeto/yang-mills-interacting-workbench`** and **`KokunoYumeto/zeta-function-research-reader`**, including the Split Zero reconstruction, transported-class cohomology, and retained-jet constructions. The Zeta repository’s current reader includes its September 14 continuation. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/AI_READING_INDEX.md))

The work below produces three concrete results: an explicit Split Zero complex for the Yang-Mills cubic vertex; an exact relation between eliminated-variable memory and the raw Gram matrix for the **full finite-lattice Hamiltonian**; and an independently recomputed, strengthened numerical certificate. The new lower constant for the retained cubic boundary primitive is between **1.39 and 1.40 times** the published lower constant.

[Research note, executable verification, and certificate](sandbox:/mnt/data/split_zero_yang_mills_research.zip) · [Read the mathematical note](sandbox:/mnt/data/split_zero_ym/RESEARCH_NOTE.md)

## 1. Apply Split Zero to the actual cubic boundary equation

The relevant Split Zero construction retains the source class, the transition that turns it into a boundary, and the kernel of the induced cohomology map. Its reconstructed quotient sends a relation to the zero carrying that relation’s support label. I instantiate that construction on the workbench’s cubic vacuum equation. ([GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7ea0a49945390eae14d3160a5730858899768b5f/formal/splitzero/DERIVED_MATHEMATICS.md))

Fix the workbench’s original box $L=2$, retaining the physical spacing $a>0$. Write
$$
A_0=H_{\mathrm{osc}}-\mu_0,
\qquad
q=H^{(1)}\Phi_0.
$$

Here $H^{(1)}$ is the workbench’s coefficient of the **complete** chart operator, including its kinetic and magnetic contributions. In its original creation coordinates,
$$
q=\sum_{I\in\Lambda}d_Ib_I,
\qquad
A_0b_I=E_Ib_I,
$$
where
$$
\begin{aligned}
\Lambda&=\{(i,j,k):i<j<k\},\\
b_{ijk}
&=\sum_{\alpha,\beta,\gamma=1}^{3}
\epsilon_{\alpha\beta\gamma}
a^\dagger_{i\alpha}a^\dagger_{j\beta}
a^\dagger_{k\gamma}\Phi_0,\\
E_{ijk}&=\frac{\sigma_i+\sigma_j+\sigma_k}{a},\\
\langle b_I,b_J\rangle&=6\delta_{IJ}.
\end{aligned}
$$
The factor $6$ is the original raw Gram factor. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/NONABELIAN_VERTEX.md))

### The support-indexed complex

Define
$$
U=\operatorname{span}_{\mathbb C}\{b_I:I\in\Lambda\},
\qquad
U_J=\operatorname{span}_{\mathbb C}\{b_I:I\in J\}
$$
for every subset $J\subseteq\Lambda$.

Use the join-semilattice $\mathcal P(\Lambda)$, with join $J\cup K$. At support $J$, define the actual cochain window
$$
C_J^0=U_J
\xrightarrow{\ d_J=A_0|_{U_J}\ }
C_J^1=U
\xrightarrow{\ 0\ }
C_J^2=0.
$$

For $J\subseteq K$, the transition maps are inclusion in degree zero, the identity in degree one, and the unique map between the zero spaces in degree two.

The cochain square commutes coordinate by coordinate:
$$
A_0\left(\sum_{I\in J}z_Ib_I\right)
=
\sum_{I\in J}E_Iz_Ib_I
$$
along both routes.

These windows also map into the workbench’s vacuum-correction equation through the actual inclusions
$$
\iota_J^0:U_J\hookrightarrow
\operatorname{Dom}(A_0)\cap\Phi_0^\perp,
\qquad
\iota^1:U\hookrightarrow\Phi_0^\perp,
$$
with
$$
\iota^1d_J=A_0\iota_J^0.
$$

### Compute the cohomology and the transported-class kernel

The coordinate map
$$
\Theta_J:H^1(C_J)\longrightarrow
\mathbb C^{\Lambda\setminus J},
\qquad
\left[\sum_Iz_Ib_I\right]\longmapsto
(z_I)_{I\notin J}
$$
is a linear isomorphism.

Here is its complete verification. An incoming boundary has the form
$$
d_J\left(\sum_{I\in J}y_Ib_I\right)
=
\sum_{I\in J}E_Iy_Ib_I,
$$
so it changes precisely the $J$-coordinates. Conversely, the portion supported in $J$ has the explicit primitive
$$
\sum_{I\in J}\frac{z_I}{E_I}b_I.
$$
Every $E_I$ is strictly positive. The inverse of $\Theta_J$ therefore sends the omitted-coordinate tuple to the class of its displayed sum.

Consequently, for $J\subseteq K$,
$$
\boxed{
\Psi_{J,K}:
\mathbb C^{K\setminus J}
\xrightarrow{\ \cong\ }
\ker\!\left(H^1(C_J)\to H^1(C_K)\right)
}
$$
is given by
$$
(z_I)_{I\in K\setminus J}
\longmapsto
\left[\sum_{I\in K\setminus J}z_Ib_I\right].
$$

Its inverse reads those same coordinates. The corresponding retained primitive is
$$
\pi_{J,K}(z)
=
\sum_{I\in K\setminus J}\frac{z_I}{E_I}b_I,
$$
and its inherited squared norm is exactly
$$
\boxed{
\|\pi_{J,K}(z)\|^2
=
6\sum_{I\in K\setminus J}\frac{|z_I|^2}{E_I^2}.
}
$$

Applying the Split Zero reconstruction to this diagram gives
$$
(J,[v])+(K,[w])
=
(J\cup K,[v+w]_{J\cup K}),
$$
with supported-zero differential composition
$$
(J,x)\longmapsto(J,0).
$$

For the actual Yang-Mills vector $q$, the transition from empty support to full support sends its class to
$$
(\Lambda,0).
$$
The retained kernel element is the original $[q]$, and its unique primitive in $U$ is
$$
u=A_0^{-1}q
=
\sum_I\frac{d_I}{E_I}b_I.
$$

Thus the construction explicitly retains the vector that produces the workbench’s first vacuum correction, $-u$.

### A numerical invariant attached to that retained primitive

Define, on the real domain $z\leq0$,
$$
M_{\mathrm{vac}}(z)
=
\left\langle q,(A_0|_U-z)^{-1}q\right\rangle
=
6\sum_I\frac{|d_I|^2}{E_I-z}.
$$

Differentiating the finite sum gives
$$
\boxed{
M_{\mathrm{vac}}'(0)
=
6\sum_I\frac{|d_I|^2}{E_I^2}
=
\|u\|^2.
}
$$

The source class, its boundary primitive, and this derivative are now connected by explicit maps and coordinate formulas.

## 2. Independently recompute and strengthen the cubic certificate

I independently evaluated the complete **112 frequency blocks** entering the published three-chord certificate. The calculation also checks their total transverse multiplicity, $176$, and reproduces all eighteen published entry enclosures for the selected $K$ and $Q$ matrices. The original source specifies the block formula, tree-path coefficients, and cubic contraction. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/NONABELIAN_VERTEX.md))

The computation uses integer interval endpoints with denominator $10^{40}$. Addition and negation are exact. Products and quotients use all endpoint pairs and outward rounding. Square-root endpoints are certified by integer-square inequalities. The trigonometric values are generated from
$$
\sin\frac{\pi}{10}=\frac{\sqrt5-1}{4},
\qquad
\cos\frac{\pi}{10}=\sqrt{\frac{5+\sqrt5}{8}}
$$
by angle addition.

The executed code and all retained intervals are available as [the verification program](sandbox:/mnt/data/split_zero_ym/exact_certificate.py) and [the machine-readable certificate](sandbox:/mnt/data/split_zero_ym/certificate.json).

### The original coordinate calculation

Use the displayed chord order
$$
c_1=((-1,1,-2),2),\qquad
c_2=((-1,2,-2),3),\qquad
c_3=((-1,1,-1),2).
$$

Writing $K_{ij}$ and $Q_{ij}$ for the selected entries in that order, the complete cubic coefficient is
$$
\begin{aligned}
ac={}&\frac18\bigl(
-Q_{12}K_{13}+Q_{13}K_{12}
+Q_{21}K_{23}-Q_{23}K_{21}\\
&\hspace{31mm}
-Q_{31}K_{32}+Q_{32}K_{31}
\bigr)-\frac18.
\end{aligned}
$$

The last term retains the magnetic contribution. The program checks it from the ordered face vectors
$$
e_1,\ e_2,\ -e_3,\ 0
$$
using the original cross-product recurrence.

The independent computation yields the strict enclosure
$$
\boxed{
-\frac{242460588472}{10^{12}}
<
ac
<
-\frac{242460588471}{10^{12}}.
}
$$

Set
$$
\beta=\frac{242460588471}{10^{12}}.
$$
The absolute value of the corresponding alternating coefficient is therefore greater than $\beta/a$. Passing between the displayed chord order and the globally ordered coefficient vector multiplies this coefficient by the exact permutation sign.

### Retain the largest-frequency multiplicities

The original open-box frequency formula gives
$$
\Omega=\sqrt{\frac{3(5+\sqrt5)}2},
\qquad
\Omega_2=\sqrt{\frac{13+3\sqrt5}2}.
$$

The largest frequency comes from $(4,4,4)$ and has transverse multiplicity two. The next distinct frequency comes from permutations of $(4,4,3)$. Consequently, the top three frequencies, counted with their actual multiplicities, are
$$
\Omega,\quad\Omega,\quad\Omega_2.
$$
These statements follow directly from the workbench’s boundary-sensitive frequency formula and the strict increase of $\sin(\pi j/10)$ on $j=0,\ldots,4$. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md))

Let $\mathcal S$ be the complete edge spectral matrix, and let
$$
\iota:\mathbb C^{176}\longrightarrow\mathbb C^{300}
$$
insert chord coordinates with zero tree entries. In the original counting inner products,
$$
K=\iota^*\mathcal S\iota.
$$

The exact exterior-power morphism is
$$
\bigwedge\nolimits^3K
=
(\bigwedge\nolimits^3\iota)^*
(\bigwedge\nolimits^3\mathcal S)
(\bigwedge\nolimits^3\iota).
$$

The insertion has Gram matrix $I$. Its third exterior power therefore preserves the counting inner product on the corresponding wedge coordinates. The largest eigenvalue of $\bigwedge^3\mathcal S$ is
$$
\Omega^2\Omega_2.
$$
It follows that
$$
0<\bigwedge\nolimits^3K
\preceq\Omega^2\Omega_2I,
$$
and hence
$$
\bigwedge\nolimits^3(2K^{-1})
=
8(\bigwedge\nolimits^3K)^{-1}
\succeq
\frac8{\Omega^2\Omega_2}I.
$$

Combining this with the workbench’s exact raw identity
$$
\|q\|^2
=
6c^*\bigwedge\nolimits^3(2K^{-1})c
$$
and the independently certified coefficient gives
$$
\boxed{
\|H^{(1)}\Phi_0\|^2
>
\frac{48\beta^2}{\Omega^2\Omega_2\,a^2}.
}
$$

Every $E_I$ sums three distinct spatial-mode frequencies. Therefore
$$
E_I\leq\frac{2\Omega+\Omega_2}{a}.
$$
Applying this inequality term by term to the retained spectral sums proves
$$
\boxed{
M_{\mathrm{vac}}'(0)=\|A_0^{-1}H^{(1)}\Phi_0\|^2
>
\frac{48\beta^2}
{\Omega^2\Omega_2(2\Omega+\Omega_2)^2}.
}
$$
It also proves
$$
\boxed{
M_{\mathrm{vac}}(0)
>
\frac{48\beta^2}
{\Omega^2\Omega_2(2\Omega+\Omega_2)a}.
}
$$

The verification program certifies that the new primitive lower constant divided by the published constant
$$
\frac{14641}{13500000\sqrt3}
$$
lies strictly between $139/100$ and $140/100$.

This improvement uses both a tighter coefficient enclosure and the exact top-frequency multiplicities.

## 3. Carry the construction to the full nonlinear Hamiltonian

Now retain the full original finite-lattice operator
$$
H_g=
\frac{2g^2}{a}\sum_eE_e
+
\frac1{2g^2a}
\sum_p\left(2-\operatorname{tr}U_p\right),
\qquad a>0,\quad g>0.
$$

Let
$$
A=H_g-\mathcal E_0(g)
$$
on the physical Hilbert space $\mathcal H$. The source supplies its self-adjoint physical domain, compact resolvent, and actual lowest eigenvalue, so $A\geq0$. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md))

Use the original six comparison vectors $S_I$, in the fixed order
$$
(11,22,33,12,13,23).
$$
Form the **pre-projection chart frame**
$$
r_I=\mathcal B_g^*\bigl(\chi(gx)S_I\bigr),
\qquad
R:\mathbb C^6\to\mathcal H,
\qquad
Rx=\sum_Ix_Ir_I,
$$
using the workbench’s chart map and invariant cutoff. These are smooth physical vectors. Their independence follows by restricting a vanishing linear combination to the neighbourhood where $\chi=1$: the six quadratic polynomial coefficients then vanish individually. The original six vectors and chart construction are given in the interacting-band source. ([github.com](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/interacting_band_publication_20260909/INTERACTING_TENSOR_BAND.md))

Retain the raw Gram matrix
$$
G=R^*R.
$$
Define the explicitly typed maps
$$
P=RG^{-1}R^*:\mathcal H\to\mathcal H,
\qquad
Q=I-P,
$$
$$
B=QAR:\mathbb C^6\to Q\mathcal H,
$$
and
$$
D=QAQ:
\operatorname{Dom}(A)\cap Q\mathcal H
\to Q\mathcal H.
$$

Direct multiplication proves
$$
P^*=P,\qquad P^2=P,\qquad PR=R,\qquad QR=0.
$$

The compression $D$ is self-adjoint and nonnegative. To verify the domain statement, observe that $AP$ is bounded and finite rank because the range of $P$ consists of finitely many vectors in $\operatorname{Dom}(A)$. Its adjoint is the bounded extension of $PA$. Thus
$$
C=QAP+PAQ
$$
is bounded self-adjoint. For $T>\|C\|$, the operators
$$
I-C(A\pm iT)^{-1}
$$
are invertible by their Neumann series. Hence $A-C$ is self-adjoint on $\operatorname{Dom}(A)$. Its $Q$-block is $D$. Finally,
$$
\langle v,Dv\rangle=\langle v,Av\rangle\geq0
$$
for every $v\in\operatorname{Dom}(D)$.

For $t>0$, write $D_t=D+t$. Its inverse exists and satisfies
$$
\|D_t^{-1}\|\leq t^{-1}.
$$

Define
$$
F(t)=R^*AR+tG-B^*D_t^{-1}B
$$
and the restored-vector map
$$
L_t=R-D_t^{-1}B:
\mathbb C^6\to\operatorname{Dom}(A).
$$

The eliminated relation and its primitive are exactly
$$
D_t(-D_t^{-1}Bx)=-Bx,
\qquad
Q(A+t)L_tx=0.
$$

This gives another literal Split Zero two-support complex: its degree-one space is $Q\mathcal H$ at both supports; its incoming source is $0$ at the first support and $\operatorname{Dom}(D)$, with differential $D_t$, at the second. The retained kernel contains the actual vector $-Bx$, with primitive $-D_t^{-1}Bx$.

### The full-operator memory derivative equals the restored raw Gram matrix

Entry by entry,
$$
F_{IJ}(t)
=
\langle r_I,Ar_J\rangle+tG_{IJ}
-
\langle B_I,D_t^{-1}B_J\rangle,
\qquad B_I=QAr_I.
$$

The resolvent identity gives
$$
\frac{d}{dt}D_t^{-1}=-D_t^{-2}.
$$
Since $R^*Q=0$, differentiation and expansion yield
$$
\boxed{
F'(t)
=
G+B^*D_t^{-2}B
=
L_t^*L_t.
}
$$

In coordinates, this is
$$
F'_{IJ}(t)
=
\left\langle
r_I-D_t^{-1}B_I,\,
r_J-D_t^{-1}B_J
\right\rangle.
$$

The same boundary equation gives
$$
\boxed{
L_t^*(A+t)L_t=F(t),
\qquad
F(t)\succeq tG.
}
$$

Finally, solving the two block equations for
$$
(A+t)(Rx+v)=Ry
$$
gives
$$
F(t)x=Gy,\qquad v=-D_t^{-1}Bx.
$$
Therefore
$$
\boxed{
R^*(A+t)^{-1}R
=
G\,F(t)^{-1}G.
}
$$

These identities retain the original Gram matrix, physical spacing, coupling, full kinetic operator, and full plaquette words.

## 4. Extract the first-band information as a retained Split Zero jet

The workbench’s six-band coefficients are
$$
c_{I,n}
=
\langle h_n\Phi_0,H^{(1)}S_I\rangle,
\qquad
\omega_n=\sum_{i,\alpha}n_{i\alpha}\frac{\sigma_i}{a},
\qquad
\Delta=\frac{2\sigma_*}{a}.
$$

The relevant occupation indices have $|n|=3$ or $5$. The source gives both the energy correction and the raw correction Gram matrix in these coordinates. ([github.com](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/interacting_band_publication_20260909/INTERACTING_TENSOR_BAND.md))

Define the finite memory matrix
$$
\Sigma_{IJ}(z)
=
\sum_{|n|=3,5}
\frac{\overline{c_{I,n}}c_{J,n}}{\omega_n-z}.
$$

All displayed denominators at $z=\Delta$ are at least $\sigma_*/a>0$. Direct differentiation proves
$$
\boxed{
\mathsf K=V-\Sigma(\Delta)-E^{(2)}I,
\qquad
\Sigma'(\Delta)=G_2.
}
$$

Thus the workbench’s energy correction and raw Gram correction are the value and derivative of one retained matrix function, with the vacuum correction $E^{(2)}$ still present.

### The exact typed jet morphism

The Zeta workbench constructs retained first jets by applying its scalar $G$-construction to a coefficient-ring jet map. ([GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7ea0a49945390eae14d3160a5730858899768b5f/workbenches/split-support-rees-trace/RESEARCH_NOTE.md))

For this Yang-Mills application, let
$$
\mathcal A=\mathbb C\{h\}
$$
be the algebra of holomorphic germs at zero. Define
$$
j^1:\mathcal A\to
\mathbb C[\varepsilon]/(\varepsilon^2),
\qquad
f\mapsto f(0)+\varepsilon f'(0).
$$

The product rule proves multiplicativity:
$$
j^1(fg)
=
f(0)g(0)+
\varepsilon\bigl(f'(0)g(0)+f(0)g'(0)\bigr)
=
j^1(f)j^1(g).
$$

For each original matrix coordinate $I,J$, set
$$
\mathcal E_{IJ}(h)
=
\Sigma_{IJ}(\Delta+h)-\Sigma_{IJ}(\Delta).
$$

The actual morphism is
$$
G(\mathcal A)
\xrightarrow{G(j^1)}
G\!\left(\mathbb C[\varepsilon]/\varepsilon^2\right)
\xrightarrow{G(\varepsilon\mapsto0)}
G(\mathbb C),
$$
and it acts by
$$
\boxed{
\mathcal E_{IJ}^{\bullet}
\longmapsto
\bigl(\varepsilon(G_2)_{IJ}\bigr)^{\bullet}
\longmapsto
0^{\bullet}.
}
$$

Both arrows preserve supported elements and send $\tau$ to $\tau$. This supplies the requested coefficient-level application of the retained-zero jet construction to the Yang-Mills workbench.

### Recover every energy-grouped residue from finitely many derivatives

Enumerate the distinct positive denominators as
$$
\nu_1<\cdots<\nu_N.
$$
Retain every contribution at a repeated energy in the matrix
$$
(B_j)_{IJ}
=
\sum_{n:\,\omega_n-\Delta=\nu_j}
\overline{c_{I,n}}c_{J,n}.
$$

Define the Taylor coefficients
$$
M_r=\frac{\Sigma^{(r)}(\Delta)}{r!}
=
\sum_{j=1}^{N}\frac{B_j}{\nu_j^{r+1}}.
$$

Form the explicit polynomials
$$
p_j(t)
=
\prod_{k\ne j}
\frac{t-\nu_k^{-1}}{\nu_j^{-1}-\nu_k^{-1}}
=
\sum_{r=0}^{N-1}\ell_{jr}t^r.
$$

Every denominator is nonzero by the strict ordering. Evaluation gives
$$
p_j(\nu_k^{-1})=\delta_{jk}.
$$
Consequently,
$$
\boxed{
B_j
=
\nu_j\sum_{r=0}^{N-1}\ell_{jr}M_r.
}
$$

The proof is entrywise substitution:
$$
\nu_j\sum_r\ell_{jr}M_r
=
\sum_k\frac{\nu_j}{\nu_k}
B_kp_j(\nu_k^{-1})
=
B_j.
$$

The retained finite jet therefore determines every energy-grouped residue matrix by an explicit inverse map.

It also carries exact positivity constraints. For $x\in\mathbb C^6$,
$$
x^*B_jx
=
\sum_{n:\,\omega_n-\Delta=\nu_j}
\left|\sum_Ic_{I,n}x_I\right|^2
\geq0,
$$
which proves
$$
\boxed{
\frac{M_0}{\nu_N}
\preceq
M_1
\preceq
\frac{M_0}{\nu_1}.
}
$$

The research note gives the corresponding positive block-moment identity for all higher derivatives. These are explicit relations between the energy correction, raw metric correction, and higher retained memory coefficients.

## Established result

The completed calculation supplies an exact support-indexed cohomology module for the cubic Yang-Mills boundary equation, its retained primitive and quantitative lower bound, full nonlinear finite-lattice restored-metric and resolvent identities, and a typed Split Zero jet map with explicit residue reconstruction.

The executable independently verifies the **112-block cubic certificate and the strengthened lower constants**. The full occupation-coupling table in the residue formula has been characterized algebraically here; it was not numerically evaluated by that executable.

A proof of the four-dimensional continuum Yang-Mills mass gap has not been established in this response. The displayed finite-regulator results and their verification files are the completed mathematical output; no GitHub repository was modified.

---

**Sources:**

- [https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/AI_READING_INDEX.md](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/AI_READING_INDEX.md)


# Historical final response 2: Smooth continuum

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/02_smooth_continuum_20260914.md}

\textbf{SHA-256:} \path{395076eee107abeab39b21ad91585497c8011457c5690b8526c71a8a566a4a15}

\textbf{Editorial provenance notice:} The linked standalone mathematical attachment has not been recovered. This chapter preserves the complete mathematical final response only; it is not a recovery of the missing attachment.
\end{quote}

I continued on an **explicit simultaneous spatial-refinement, coupling, and infinite-volume sequence**. The new contribution establishes uniform positive-time bounds for the full interacting Hamiltonians, smooth subsequential limits of their correlation and Schur-memory matrices, and exact records of spectral mass reaching either energy endpoint.

The Yang-Mills update is prepared as an additive contribution:

[Full research note](sandbox:/mnt/data/yang_mills_smooth_continuum_note.md) · [Workbench contribution and verification files](sandbox:/mnt/data/yang_mills_smooth_continuum_continuation.zip) · [Git patch](sandbox:/mnt/data/yang_mills_smooth_continuum.patch)

The S6 reader and research ledger locate its smooth normal-line trivialization and inverse, with theorem references in the frozen project. Fetches of the linked proof bodies failed. Consequently, the smooth continuation below is proved directly from the retrieved Yang-Mills transport equations and the Zeta workbench’s retained-jet construction; I have not used an unexamined S6 theorem as a premise. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/s6/README.md))

## 1. Put the full operator on an actual continuum-volume sequence

Fix $a_0,g_0,\beta>0$, and define
$$
a_n=a_0\,2^{-n},\qquad
L_n=4\,2^{2n},\qquad
g_n^2=\frac1{g_0^{-2}+\beta n\log2}.
$$
Then
$$
a_n\longrightarrow0,
\qquad
a_nL_n=4a_0\,2^n\longrightarrow\infty.
$$

This specifies the coupling path completely. Its parameter $\beta$ has not been identified with a quantum beta-function coefficient.

On the original open graph, retain
$$
H_n=\frac{2g_n^2}{a_n}K_n+V_n,
\quad
K_n=-\sum_{e,\alpha}X_{e,\alpha}^2,
\quad
V_n=\frac1{2g_n^2a_n}\sum_p(2-\operatorname{tr}U_p).
$$
Let $\psi_n$ be its actual positive unit vacuum, $E_{0,n}$ its ground energy, and
$$
A_n=H_n-E_{0,n}I.
$$
The physical domain, gauge action, and ground-state identity used here are the workbench’s original ones. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md))

### Exact refinement and its complete defect

A coarse edge consists of two consecutive fine edges. Define
$$
\pi_n:SU(2)^{E_{n+1}}\to SU(2)^{E_n},
\qquad
(\pi_nU)_e=U_{e,1}U_{e,2},
$$
and
$$
J_n:\mathcal H_n\to\mathcal H_{n+1},
\qquad J_nf=f\circ\pi_n.
$$

Haar invariance proves $J_n^*J_n=I$. Gauge covariance follows from the exact cancellation
$$
(h_sU_{e,1}h_m^{-1})(h_mU_{e,2}h_t^{-1})
=h_s(U_{e,1}U_{e,2})h_t^{-1}.
$$

Differentiation of the ordered product gives
$$
X_{e,1,\alpha}J_nf=J_nX_{e,\alpha}f,
$$
$$
X_{e,2,\alpha}J_nf
=\sum_\gamma
(\operatorname{Ad}_{U_{e,1}})_{\gamma\alpha}
J_nX_{e,\gamma}f.
$$
The adjoint matrix preserves the original generator metric. Squaring and summing therefore proves
$$
K_{n+1}J_n=2J_nK_n.
$$

The **complete Hamiltonian transition defect** is consequently
$$
\boxed{
\begin{aligned}
\mathcal D_n
&:=A_{n+1}J_n-J_nA_n\\
&=\frac{8g_{n+1}^2-2g_n^2}{a_n}J_nK_n
+M_{V_{n+1}-V_n\circ\pi_n}J_n
+(E_{0,n}-E_{0,n+1})J_n .
\end{aligned}}
$$
Here $M_f$ is multiplication by the displayed fine-configuration function. Every additional fine plaquette remains in $V_{n+1}$.

For $s>0$, this produces the bounded-operator identity
$$
\boxed{
(A_{n+1}+s)^{-1}J_n-J_n(A_n+s)^{-1}
=-(A_{n+1}+s)^{-1}\mathcal D_n(A_n+s)^{-1}.
}
$$
The note proves the graph-domain mapping and the telescoping composition law across arbitrarily many levels.

Thus refinement now carries its full kinetic, magnetic, and vacuum-energy discrepancy as explicit data.

## 2. Smooth continuation retains the entire smooth germ

The workbench specifies ordered continuum transport through
$$
U'(r)=U(r)\mathcal A(\dot\gamma(r)),\qquad U(0)=I.
$$
Its interval concatenations agree exactly with the link-product refinement above. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_WILSON_SCHUR_MEMORY.md))

For a smooth parameter-dependent connection, the first derivative is
$$
\partial_\theta U_\theta(\ell)
=
\int_0^\ell
U_\theta(0,r)\,
\partial_\theta\mathcal A_\theta(\dot\gamma(r))\,
U_\theta(r,\ell)\,dr.
$$
The note writes every higher derivative as an ordered simplex integral, retaining every derivative allocation and multinomial coefficient. Unitarity bounds those integrals in terms of the total physical path length and connection-derivative suprema, independently of the number of subdivisions.

There is an important additional piece of retained information when extending the Zeta workbench’s jet construction to smooth germs. The source supplies the typed first-jet algebra morphism; the following construction computes the smooth kernel explicitly. ([GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7ea0a49945390eae14d3160a5730858899768b5f/workbenches/split-support-rees-trace/RESEARCH_NOTE.md))

Let $\mathcal A_{\mathrm{sm}}$ be the algebra of complex smooth germs at $\theta=0$. Define
$$
j^qf=\sum_{k=0}^q\frac{f^{(k)}(0)}{k!}\eta^k
\quad\text{in }\mathbb C[\eta]/(\eta^{q+1}).
$$
The product rule proves multiplicativity. Taylor’s integral formula proves
$$
\ker j^q=\theta^{q+1}\mathcal A_{\mathrm{sm}}.
$$
Retaining all jets gives the exact sequence
$$
\boxed{
0\longrightarrow\mathcal F_{\mathrm{flat}}
\longrightarrow\mathcal A_{\mathrm{sm}}
\xrightarrow{J_\infty}\operatorname{im}J_\infty
\longrightarrow0,
}
$$
where $\mathcal F_{\mathrm{flat}}$ consists precisely of germs whose derivatives of every order vanish at zero.

An actual Yang-Mills holonomy realizes that kernel. Take
$$
\eta_0(\theta)=
\begin{cases}
e^{-1/\theta^2},&\theta\ne0,\\
0,&\theta=0,
\end{cases}
$$
and
$$
\mathcal A_2=b\,x^1\chi(x)\eta_0(\theta)T_3,
\qquad \mathcal A_1=\mathcal A_3=0.
$$
For a rectangle of sides $\ell_1,\ell_2$ contained in $\chi=1$,
$$
\boxed{
2-\operatorname{tr}U_C(\theta)
=
2-2\cos\!\left(\frac{b\ell_1\ell_2\eta_0(\theta)}2\right).
}
$$
Every jet is zero, while the displayed value is strictly positive for sufficiently small nonzero $\theta$.

The source germ, its holonomy, and its exact kernel membership all remain recorded.

### A quantitative full magnetic remainder

For smooth connections supported in $(-2a_0,2a_0)^3$, put
$$
Q=[-3a_0,3a_0]^3,
\qquad
F_{ij}=\partial_i\mathcal A_j-\partial_j\mathcal A_i+
[\mathcal A_i,\mathcal A_j].
$$
Define
$$
M_A=\max_i\sup\|\mathcal A_i\|_{\mathrm{op}},\quad
M_F=\max_{i<j}\sup\|F_{ij}\|_F,\quad
M_{\partial F}=\max_{k,i<j}\sup\|\partial_kF_{ij}\|_F,
$$
and
$$
C=M_{\partial F}+2M_AM_F+\frac{a_0}{2}M_F^2.
$$

An axial gauge constructed from the original ordered transports gives
$$
U_p-I=a_n^2F_{ij}(x_p)+R_p,
\qquad
\|R_p\|_F\le a_n^3C.
$$
Using the exact identity
$$
\|U-I\|_F^2=4-2\operatorname{tr}U
$$
and counting the original plaquettes proves
$$
\boxed{
V_n(U[\mathcal A])
=
\frac1{4g_n^2}\int_Q\sum_{i<j}\|F_{ij}\|_F^2\,dx+\varepsilon_n,
}
$$
with
$$
\boxed{
|\varepsilon_n|
\le
\frac{3|Q|}{4g_n^2}
\left(
2a_nM_FC+a_n^2C^2+
6a_nM_FM_{\partial F}
\right).
}
$$

Along the specified path, this error tends to zero because $n2^{-n}\to0$. The complete leading curvature term retains its factor
$$
\frac{g_0^{-2}+\beta n\log2}{4}.
$$
Its growth remains explicit.

## 3. Uniform control for the actual interacting quantum vacua

Choose six edge-disjoint square loops of side $a_0$, with lower-left corners
$$
a_0(-3,-3,0),\ a_0(-1,-3,0),\ a_0(1,-3,0),
$$
$$
a_0(-3,1,0),\ a_0(-1,1,0),\ a_0(1,1,0).
$$
At level $n$, every loop contains exactly $4\,2^n$ original edges.

Let $W_{i,n}$ be its complete ordered trace, and define
$$
r_{i,n}=
\bigl(W_{i,n}-\langle\psi_n,W_{i,n}\psi_n\rangle\bigr)\psi_n,
$$
$$
R_nx=\sum_{i=1}^6x_ir_{i,n},
\qquad
G_n=R_n^*R_n,
\qquad
C_n(t)=R_n^*e^{-tA_n}R_n.
$$
Because each trace lies in $[-2,2]$,
$$
\operatorname{tr}G_n\le24.
$$

For every $r\ge1$ and $t>0$,
$$
\boxed{
0\preceq(-1)^rC_n^{(r)}(t)
\preceq24\left(\frac r{et}\right)^rI_6.
}
$$
The proof is the spectral multiplier identity
$$
(-1)^rC_n^{(r)}(t)=R_n^*A_n^re^{-tA_n}R_n
$$
and the exact maximum
$$
\sup_{\lambda\ge0}\lambda^re^{-t\lambda}
=\left(\frac r{et}\right)^r.
$$

For the explicit heat-transported vectors
$$
R_{\tau,n}=e^{-\tau A_n/2}R_n,
$$
the high-energy tail satisfies
$$
\boxed{
0\preceq
R_{\tau,n}^*\mathbf1_{[\Lambda,\infty)}(A_n)R_{\tau,n}
\preceq24e^{-\tau\Lambda}I_6.
}
$$

These right-hand sides are independent of lattice spacing, coupling, and volume.

### The zero-time energy matrix is also explicit

For one original loop edge, write
$$
U_C=q_0I-i\sum_{\alpha=1}^3q_\alpha\sigma_\alpha.
$$
Direct multiplication gives
$$
\sum_\alpha|X_{e,\alpha}W_C|^2
=\sum_{\alpha=1}^3q_\alpha^2
=1-\frac{W_C^2}{4}.
$$
Polarizing the full ground-state identity and using edge-disjointness therefore proves
$$
\boxed{
-C_n'(0)
=
\frac{8g_n^2a_0}{a_n^2}
\operatorname{diag}_{i=1}^6
\left(
1-\frac{\langle\psi_n,W_{i,n}^2\psi_n\rangle}{4}
\right).
}
$$

Thus the complete first spectral moment has a known regulator factor and an exact interacting-vacuum multiplier. The note also expresses that multiplier through the original means and diagonal Gram entries.

## 4. The retained Schur memory now has uniform bounds and smooth limits

The workbench already supplies full nonlinear transport and retained state maps. The continuation applies its Schur construction to the heat-transported physical vectors above. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/FABEL_TENSOR_TRANSFER.md))

For fixed $\tau>0$, abbreviate $R=R_{\tau,n}$, $G=R^*R$, and define
$$
P=RG^{-1}R^*,\qquad Q=I-P,
$$
$$
B=Q A_nR,\qquad
D=QA_nQ
\quad\text{on }\operatorname{Dom}(A_n)\cap Q\mathcal H_n.
$$
The note proves self-adjointness and nonnegativity of this compression through the bounded finite-rank off-diagonal operator.

Set
$$
\mathcal M_{\tau,n}(s)=B^*(D+s)^{-1}B,
$$
$$
F_{\tau,n}(s)=R^*A_nR+sG-\mathcal M_{\tau,n}(s),
$$
$$
L_{\tau,n}(s)=R-(D+s)^{-1}B.
$$

The heat multiplier gives
$$
\|A_nR\|^2\le\frac{96}{e^2\tau^2}.
$$
Consequently, for every $r\ge0$,
$$
\boxed{
0\preceq(-1)^r\mathcal M_{\tau,n}^{(r)}(s)
\preceq
\frac{96r!}{e^2\tau^2s^{r+1}}I_6.
}
$$

The exact metric and resolvent identities remain
$$
\boxed{
F_{\tau,n}'(s)
=G+B^*(D+s)^{-2}B
=L_{\tau,n}(s)^*L_{\tau,n}(s),
}
$$
$$
\boxed{
R^*(A_n+s)^{-1}R
=G\,F_{\tau,n}(s)^{-1}G.
}
$$

The contribution then constructs **one subsequence** for a countable separating supply of physical observables and a countable supply of positive heat times such that
$$
C_{n_k}\longrightarrow C_\infty,
\qquad
\mathcal M_{\tau,n_k}\longrightarrow\mathcal M_{\tau,\infty}
$$
in $C^\infty_{\mathrm{loc}}((0,\infty))$.

The memory limit has the retained measure representation
$$
\mathcal M_{\tau,\infty}(s)
=\int_{[0,\infty]}\frac{d\sigma_\tau(\lambda)}{\lambda+s},
$$
with the multiplier defined as zero at infinity. In particular,
$$
\boxed{
\lim_kL_{\tau,n_k}(s)^*L_{\tau,n_k}(s)
=
C_\infty(\tau)+
\int_{[0,\infty]}
\frac{d\sigma_\tau(\lambda)}{(\lambda+s)^2}.
}
$$

The original finite-regulator matrix product also converges:
$$
\boxed{
\lim_k
G_{\tau,n_k}F_{\tau,n_k}(s)^{-1}G_{\tau,n_k}
=
\int_0^\infty e^{-st}C_\infty(\tau+t)\,dt.
}
$$
This formula requires no inverse of a limiting Gram matrix.

## 5. Split Zero now records the spectral infinity itself

Let
$$
X=[0,\infty]
$$
retain the original finite energy coordinate and one endpoint at infinite energy. The original vectors define positive matrix measures
$$
\mu_{n,ij}(S)
=
\langle r_{i,n},\mathbf1_S(A_n)r_{j,n}\rangle.
$$
Along the constructed subsequence, retain their weak limit $\mu$, and set
$$
E_\infty=\mu(\{\infty\}),
\qquad
Z_0=\mu(\{0\}).
$$

Monotone convergence gives the exact endpoint identities
$$
\boxed{
G_\infty=\lim_{t\downarrow0}C_\infty(t)+E_\infty,
\qquad
Z_0=\lim_{t\to\infty}C_\infty(t).
}
$$

There is a literal two-support cochain construction for the first endpoint:
$$
C_0:\quad 0\longrightarrow\mathcal M(X)\longrightarrow0,
$$
$$
C_1:\quad
\mathbb C\xrightarrow{\,c\mapsto c\delta_\infty\,}
\mathcal M(X)\longrightarrow0,
$$
where $\mathcal M(X)$ is the vector space of finite complex Borel measures.

Restriction to finite energies induces
$$
H^1(C_1)\xrightarrow{\cong}\mathcal M([0,\infty)).
$$
Its inverse extends a measure by zero at infinity and takes its class. The two compositions differ from the original measure by exactly
$$
\nu(\{\infty\})\delta_\infty.
$$
Therefore
$$
\boxed{
\ker\!\left(H^1(C_0)\to H^1(C_1)\right)
=\mathbb C\delta_\infty,
}
$$
and the boundary primitive is the coefficient of $\delta_\infty$.

This is also exactly the kernel of the positive-time observation map
$$
\mathcal L\nu(t)=\int_Xe^{-t\lambda}\,d\nu(\lambda),
$$
with its multiplier zero at infinity. To prove the converse kernel inclusion, use
$$
x=e^{-t_*\lambda},\qquad
\lambda=-\frac{\log x}{t_*}.
$$
Vanishing Laplace observations annihilate every $x^j$, $j\ge1$. Polynomial approximation then annihilates every continuous function vanishing at infinity, forcing $\nu=c\delta_\infty$.

Entry by entry, the actual retained boundary primitive is $(E_\infty)_{ij}$.

### A reconstructed positive generator and an infrared measurement formula

The limiting kernels define
$$
\langle[i,t],[j,s]\rangle=C_{\infty,ij}(t+s).
$$
Quotienting its explicitly defined null space and completing gives a Hilbert space with
$$
T(h)[i,t]=[i,t+h].
$$
The note proves that $T$ is a strongly continuous positive self-adjoint contraction semigroup and constructs its nonnegative generator $A_{\mathrm{lim}}$, with
$$
\langle[i,t],A_{\mathrm{lim}}[j,s]\rangle
=-C_{\infty,ij}'(t+s).
$$

For the actual low-energy matrix
$$
N_\tau(m)=\int_{[0,m]}e^{-\tau\lambda}\,d\mu(\lambda),
$$
direct integration of scalar exponential inequalities gives
$$
\boxed{
\frac{C_\infty(\tau+t)-e^{-tm}C_\infty(\tau)}
{1-e^{-tm}}
\preceq N_\tau(m)
\preceq e^{tm}C_\infty(\tau+t).
}
$$

This relates the infrared spectral content directly to the retained continuum-time correlations, while keeping the zero-energy and infinite-energy atoms explicit.

## Verification and workbench status

The new checker passed **76 exact assertions across 26 check families**, including ordered non-Abelian products, the two-subedge Casimir factor, the loop-energy identity, Schur metric and resolvent identities with their raw Gram factors, and refinement-defect signs. The earlier **112-block cubic certificate reproduced byte-for-byte**. The finite test matrices are declared algebraic fixtures; the analytic results are supplied as written proofs.

The patch adds
```text
yang-mills/continuations/20260914-splitzero-smooth-continuum/
```
with the note, executable, verification reports, provenance, and research-log entry. It was applied and retested in a fresh local tree. **No remote GitHub modification occurred**; publishing requires the GitHub connection shown above.

The completed advance is a connected continuation construction with exact refinement defects, controlled smooth magnetic remainders, regulator-uniform positive-time bounds, smooth correlation and memory subsequences, and retained spectral endpoints. The endpoint matrices and low-energy measures have not been numerically determined. A nontrivial four-dimensional continuum Yang-Mills theory and a positive continuum mass lower bound have not been established by this contribution.

---

**Sources:**

- [https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/s6/README.md](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/s6/README.md)


# Historical final response 3: Vacuum refinement

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/03_vacuum_refinement_20260914.md}

\textbf{SHA-256:} \path{7c30038c955f6f4aa1902d7ef3152abe3a61dd9fbae5ce611eb13136203e5fe0}

\textbf{Editorial provenance notice:} The complete final response is preserved for historical mathematical coverage. The standalone mathematical source chapters remain separately identifiable above.
\end{quote}

I advanced the continuum mathematics and opened **pull request #4: “Continue continuum control: vacuum refinement, infrared Schur budget, retained state kernel.”** Its final commit is `dc390930a8d2774e93481206602973caff7aa7da`. The pull request is open; nothing has been merged into `main`. 

[Full mathematical note](sandbox:/mnt/data/yang_mills_vacuum_refinement_note.md) · [Research package and executable verification](sandbox:/mnt/data/yang_mills_vacuum_refinement_research.zip) · [Exact Git patch](sandbox:/mnt/data/yang_mills_vacuum_refinement.patch)

The strongest added estimate is **inverse-energy integrability of the full interacting Hamiltonian’s Schur memory, uniformly over the regulator sequence**:
$$
\boxed{
\int_{(0,\infty)}\frac{d\sigma_n(\lambda)}{\lambda}
\preceq K_n
\preceq \frac{24}{e\tau}I_6.
}
$$
It supplies a quantitative infrared bound, an exact zero-energy limit-order correction, and sharper bounds on every memory derivative. The contribution also constructs refinement in the interacting vacuum measure and corrects a spectral-detection inference in the preceding note through an explicit cohomological comparison.

## 1. Uniform infrared control for the full interacting Hamiltonian

Retain the sequence
$$
a_n=a_0\,2^{-n},\qquad
L_n=4\,2^{2n},\qquad
g_n^2=(g_0^{-2}+\beta n\log2)^{-1},
$$
and the original operator
$$
H_n=
-\frac{2g_n^2}{a_n}\sum_{e,\alpha}X_{e,\alpha}^2
+\frac1{2g_n^2a_n}\sum_p(2-\operatorname{tr}U_p),
\qquad
A_n=H_n-E_{0,n}I.
$$
Here $E_{0,n}$ is its actual ground energy, and $\psi_n$ is its positive unit vacuum. The prescribed parameter $\beta$ remains explicit; no quantum beta-function coefficient is assigned to it. The operator, physical domains, and vacuum are those of the inspected finite-box source. 

Use six positively oriented square loops of physical side $a_0$, in the $x^1,x^2$ plane at $x^3=0$, with lower-left corners
$$
a_0\{(-3,-3,0),(-1,-3,0),(1,-3,0),
(-3,1,0),(-1,1,0),(1,1,0)\}.
$$
Their edge sets are disjoint. Let $O_{i,n}$ be their complete ordered fundamental traces, and define
$$
r_{i,n}=
\bigl(O_{i,n}-\langle\psi_n,O_{i,n}\psi_n\rangle\bigr)\psi_n,
\qquad
R_{0,n}x=\sum_{i=1}^6x_i r_{i,n}.
$$
Each trace lies in $[-2,2]$, so the exact variance formula gives
$$
R_{0,n}^*R_{0,n}\preceq
\operatorname{tr}(R_{0,n}^*R_{0,n})I_6
\preceq24I_6.
$$

Fix a physical heat time $\tau>0$, and put
$$
R_n=e^{-\tau A_n/2}R_{0,n},\qquad G_n=R_n^*R_n.
$$
The six vectors are independent: varying one edge in each loop forces the corresponding coefficient of any constant linear combination to vanish. The heat multiplier is injective, so $G_n$ remains positive definite.

For the following calculation suppress only the written subscript $n$, and define the typed operators
$$
P=RG^{-1}R^*,\qquad Q=I-P,
$$
$$
K=R^*AR:\mathbb C^6\to\mathbb C^6,
\qquad B=QAR:\mathbb C^6\to Q\mathcal H,
$$
$$
D=QAQ:
\operatorname{Dom}(A)\cap Q\mathcal H\to Q\mathcal H.
$$

The domain argument is retained in the note. Since the range of $R$ lies in every power domain of $A$, $AP$ is bounded and finite rank. Its adjoint is the bounded extension of $PA$. Subtracting $QAP+PAQ$ from $A$ gives a self-adjoint operator with reducing subspaces $P\mathcal H,Q\mathcal H$. Its restriction to $Q\mathcal H$ is $D$, and
$$
\langle v,Dv\rangle=\langle v,Av\rangle\ge0.
$$

For $s>0$, set
$$
M(s)=B^*(D+s)^{-1}B,\qquad
F(s)=K+sG-M(s),
$$
$$
L(s)=R-(D+s)^{-1}B.
$$
Substitution proves
$$
Q(A+s)L(s)=0,
$$
and expansion with the original inner products gives
$$
\boxed{
F(s)=L(s)^*(A+s)L(s),\qquad
F'(s)=L(s)^*L(s)
=G+B^*(D+s)^{-2}B.
}
$$
Consequently,
$$
F(s)\succeq sL(s)^*L(s)\succeq sG,
$$
which proves
$$
\boxed{0\preceq M(s)\preceq K.}
$$

This bound remains finite as $s\downarrow0$.

Let
$$
\sigma(S)=B^*E_D(S)B.
$$
Applying monotone convergence to every scalar contraction $x^*\sigma x$ proves
$$
\sigma(\{0\})=0,\qquad
\int_{(0,\infty)}\lambda^{-1}\,d\sigma(\lambda)\preceq K.
$$
Moreover,
$$
K=R_0^*Ae^{-\tau A}R_0
\preceq
\left(\sup_{\lambda\ge0}\lambda e^{-\tau\lambda}\right)R_0^*R_0
\preceq\frac{24}{e\tau}I_6.
$$
Thus, for every regulator and every $\epsilon>0$,
$$
\boxed{
\sigma_n([0,\epsilon])
\preceq\epsilon K_n
\preceq\frac{24\epsilon}{e\tau}I_6.
}
$$

The same inverse-energy measure yields, for every integer $r\ge1$,
$$
\boxed{
0\preceq(-1)^rM_n^{(r)}(s)
\preceq
\frac{r!\,r^r}{(r+1)^{r+1}s^r}K_n.
}
$$
Indeed, writing $d\alpha_n=\lambda^{-1}d\sigma_n$, the derivative integrand is
$$
\frac{r!\lambda}{(\lambda+s)^{r+1}}.
$$
The derivative of its scalar factor without $r!$ is
$$
\frac{s-r\lambda}{(\lambda+s)^{r+2}},
$$
so its maximum occurs at $\lambda=s/r$, giving exactly the displayed constant.

In particular,
$$
G_n\preceq F_n'(s)\preceq G_n+\frac{K_n}{4s},
\qquad
sF_n'(s)\preceq F_n(s).
$$
The original resolvent coordinates remain
$$
\boxed{
R_n^*(A_n+s)^{-1}R_n
=G_nF_n(s)^{-1}G_n.
}
$$

## 2. Refinement now retains the interacting vacuum and every cross term

The second calculation supplies the measure-level refinement underlying those spectral quantities.

Fix $r<n$, let $b=2^{n-r}$, and use the ordered coarse-link map
$$
\pi_{r,n}(U)_e=U_{e,1}\cdots U_{e,b}.
$$
An explicit global coordinate map retains the coarse product $W_e$, the first $b-1$ links in every chain, and every unused fine link. Its inverse sets
$$
U_{e,b}=(U_{e,1}\cdots U_{e,b-1})^{-1}W_e.
$$
Haar translation in the last link proves
$$
dU_n=dW\,dz
$$
in these coordinates.

Write $\rho_n=\psi_n^2$. The actual coarse marginal and conditional map are
$$
m_{r,n}(W)=
\int\rho_n\!\left(\Phi_{r,n}^{-1}(W,z)\right)dz,
$$
$$
(\mathsf Ef)(W)=
\frac{\int f(\Phi_{r,n}^{-1}(W,z))
\rho_n(\Phi_{r,n}^{-1}(W,z))\,dz}{m_{r,n}(W)},
\qquad
\mathsf Jg=g\circ\pi_{r,n}.
$$
Fubini proves the typed identities
$$
\mathsf J:L^2(m_{r,n}dW)\to L^2(\rho_n dU_n),
\qquad
\mathsf J^*=\mathsf E,\qquad
\mathsf E\mathsf J=I.
$$
The comparison with the original coarse vacuum retains the density ratio:
$$
\langle f,g\rangle_{m_{r,n}}
=
\int\overline f g\,
\frac{m_{r,n}}{\rho_r}\,\rho_r\,dW.
$$

### The density derivative

For the prefix $P_{e,j-1}=U_{e,1}\cdots U_{e,j-1}$, define
$$
a_{e,j;\alpha\beta}
=(\operatorname{Ad}_{P_{e,j-1}})_{\alpha\beta},
\qquad
Y_{e,\alpha}
=\frac1b\sum_{j,\beta}
a_{e,j;\alpha\beta}X_{e,j,\beta}.
$$
Direct differentiation and the adjoint-matrix identities prove
$$
Y_{e,\alpha}\mathsf Jg=\mathsf JX_{e,\alpha}g,
\qquad
\langle Y_{e,\alpha},Y_{f,\gamma}\rangle
=b^{-1}\delta_{ef}\delta_{\alpha\gamma}.
$$
Each coefficient is independent of its differentiated link, so $Y_{e,\alpha}$ has Haar divergence zero.

The exact centered density derivative is
$$
S_{e,\alpha}
=
Y_{e,\alpha}\log\rho_n
-\mathsf J(X_{e,\alpha}\log m_{r,n}).
$$
Integration by parts gives
$$
\boxed{
\mathsf ES_{e,\alpha}=0,\qquad
X_{e,\alpha}\mathsf Ef
=
\mathsf E(Y_{e,\alpha}f)
+\mathsf E(fS_{e,\alpha}).
}
$$

For a smooth physical $f$, define
$$
g=\mathsf Ef,\qquad h=f-\mathsf Jg,\qquad
v_{e,\alpha}=\mathsf E(hS_{e,\alpha}).
$$
Then $\mathsf Eh=0$ and $\mathsf EY_{e,\alpha}h=-v_{e,\alpha}$.

The vertical derivative retains the fine-link components
$$
(\nabla_vf)_{e,j,\beta}
=
X_{e,j,\beta}f
-\sum_\alpha a_{e,j;\alpha\beta}Y_{e,\alpha}f,
$$
together with every unused-edge derivative. Squaring this expression proves
$$
\sum|Xf|^2=b\sum|Yf|^2+|\nabla_vf|^2.
$$

Applying the workbench’s full ground-state identity therefore gives the **complete three-square formula**
$$
\boxed{
\begin{aligned}
q_{A_n}(\psi_nf)
={}&\kappa_nb\int m_{r,n}
 \sum_{e,\alpha}|X_{e,\alpha}g-v_{e,\alpha}|^2\,dW\\
&+\kappa_nb\int\rho_n
 \sum_{e,\alpha}|Y_{e,\alpha}h+\mathsf Jv_{e,\alpha}|^2\,dU_n\\
&+\kappa_n\int\rho_n|\nabla_vh|^2\,dU_n,
\end{aligned}}
$$
where
$$
\kappa_n=\frac{2g_n^2}{a_n},
\qquad
\kappa_nb=
\frac{2a_r}{a_n^2(g_0^{-2}+\beta n\log2)}.
$$

In its expanded form, the interaction between retained variables and fiber fluctuations includes exactly
$$
-2\kappa_nb\,\operatorname{Re}
\int m_{r,n}\sum_{e,\alpha}
\overline{X_{e,\alpha}g}\,
\mathsf E(hS_{e,\alpha})\,dW.
$$
That term remains in the identity.

The Split Zero comparison is now literal:
$$
L^2(\rho_n dU_n)/\ker\mathsf E
\xrightarrow{\;\cong\;}
L^2(m_{r,n}dW),
\qquad
[f]\longmapsto\mathsf Ef,
$$
with inverse $g\mapsto[\mathsf Jg]$. The killed-class primitive is the original $h\in\ker\mathsf E$, whose full energy interaction appears above. This uses the inspected transported-class construction with its actual incoming map and quotient. 

## 3. Smooth continuation with its exact ultraviolet cost

I recovered the S6 formula
$$
H(x)=e^{-2\pi i\varepsilon\gamma(x)}
$$
and checked its deck equivariance and mutually inverse maps
$$
[x,z]\longmapsto([x],z/H(x)),
\qquad
([x],w)\longmapsto[x,wH(x)].
$$
The computation retains $\gamma A=\gamma$, $\gamma(v)=\varepsilon$, and
$$
H(Ax+v/m)=e^{-2\pi i/m}H(x).
$$
These are the actual formulas in the S6 finite-filling source. 

For Yang-Mills, the contribution constructs a smooth local right inverse of the **entire finite-link holonomy map at every reference configuration**.

Fix $U^0\in SU(2)^{E_r}$. Choose
$$
e^{K_e^0}=U_e^0,\qquad
K_e(U)=\log((U_e^0)^{-1}U_e)
$$
on its explicit relative-logarithm neighborhood. In disjoint central tubes around the original edges, set
$$
\mathcal A_e(U)=
\frac1{a_r}
\left(
\frac{p_0(t)}{I_0}K_e^0+
\frac{p_1(t)}{I_1}K_e(U)
\right)
\chi\!\left(\frac{y}{\epsilon a_r}\right)dx_i,
$$
where the two longitudinal supports are ordered and disjoint,
$$
I_j=\int p_j(t)\,dt\ne0,\qquad
J_j=\int p_j(t)^2dt,\qquad
J_\chi=\int_{\mathbb R^2}|\nabla\chi|^2.
$$
The note specifies the supports and tube radii.

The original transport equation gives, edge by edge,
$$
\boxed{
\operatorname{Hol}_e(\mathcal A(U))
=e^{K_e^0}e^{K_e(U)}=U_e.
}
$$
This also covers reference links $U_e^0=-I$, because the varying logarithm is taken at the relative identity.

For the same constructed connection, direct differentiation gives
$$
\boxed{
\int_{\mathbb R^3}\sum_{i<j}\|F_{ij}\|_F^2\,dx
=
\frac{J_\chi}{a_r}\sum_{e\in E_r}
\left(
\frac{J_0}{I_0^2}\|K_e^0\|_F^2+
\frac{J_1}{I_1^2}\|K_e(U)\|_F^2
\right).
}
$$
The magnetic curvature functional retains its additional factor $1/(4g_r^2)$.

Thus the smooth extension and its ultraviolet energy cost are established together.

The exact product maps also produce a projective equal-time limit of the interacting vacuum marginals:
$$
\mathfrak Q=
\{(W_r)_{r\ge0}:\pi_{r,r+1}W_{r+1}=W_r\}.
$$
A single subsequence yields compatible probabilities $\nu_r$ and a probability $\nu$ on $\mathfrak Q$. The smooth holonomy image is dense, proved by the finite-level right inverses above. The same subsequence retains the positive-time correlations, with
$$
G^c_{ij}
=
\int\overline{O_i}O_j\,d\nu
-\overline{\int O_i\,d\nu}\int O_j\,d\nu,
\qquad
E_\infty=G^c-C(0+).
$$
The value of $E_\infty$, and support of $\nu$ in smooth connections, have not been established here.

## 4. The inverse-energy endpoint is retained exactly

The new infrared estimate permits
$$
d\alpha_n(\lambda)=\lambda^{-1}d\sigma_n(\lambda),
\qquad
\alpha_n([0,\infty])\preceq K_n.
$$
It also gives
$$
\alpha_n([\Lambda,\infty))
\preceq
\frac{96}{e^2\tau^2\Lambda}I_6.
$$
A joint subsequence therefore has a weak limit $\alpha$ with
$$
\alpha(\{\infty\})=0.
$$
Retain its zero-energy atom
$$
Z_\alpha=\alpha(\{0\}),
$$
and the limit
$$
S_\infty=\lim_n\bigl(K_n-M_n(0)\bigr)\succeq0.
$$
Then
$$
M_\infty(s)
=\int\frac{\lambda}{\lambda+s}\,d\alpha(\lambda),
$$
and direct evaluation of the two limit orders proves
$$
\boxed{F_\infty(0+)=S_\infty+Z_\alpha.}
$$

The associated typed observation map is
$$
\mathcal T:
\mathcal M([0,\infty))\to C^\infty((0,\infty)),
\qquad
(\mathcal T\alpha)(s)
=\int\frac{\lambda}{\lambda+s}\,d\alpha(\lambda).
$$
Its kernel is exactly
$$
\boxed{\ker\mathcal T=\mathbb C\delta_0.}
$$

For the converse inclusion, vanishing observations first give zero total mass on $(0,\infty)$, then a vanishing Stieltjes transform there. Differentiation at $s=1$ gives every moment $(1+\lambda)^{-k}$. The coordinate map
$$
x=(1+\lambda)^{-1},
\qquad
\lambda=x^{-1}-1
$$
transports these to polynomial moments; polynomial approximation forces the restricted measure to vanish.

The corresponding two-support complex uses the actual incoming map
$$
\mathbb C\to\mathcal M([0,\infty)),\qquad c\mapsto c\delta_0.
$$
Its retained boundary primitive is each original matrix entry $(Z_\alpha)_{ij}$.

## 5. A necessary correction: retain states whose labels move with refinement

The preceding spectral note asserted that a sequence of low-energy states approaching zero would be detected in at least one fixed-label diagonal continuum measure. I replaced that assertion with an explicit comparison map and computed its kernel. The earlier spectral-support and Laplace-principle formulas for the reconstructed sector remain. 

Let $\mathcal B_{\lim}$ consist of bounded regulator-state sequences $v=(v_n)$ whose pairings with every fixed positive-time observable vector converge. Define
$$
\langle z,\mathfrak b(v)\rangle
=
\lim_n\langle z_n,v_n\rangle.
$$
Cauchy-Schwarz proves that this defines
$$
\mathfrak b:\mathcal B_{\lim}\twoheadrightarrow\mathcal H_{\mathrm{obs}},
\qquad
\|\mathfrak b(v)\|\le\limsup_n\|v_n\|.
$$
The note proves surjectivity by a diagonal construction of finite-symbol lifts.

Let
$$
\mathcal N=\{v:\|v_n\|\to0\},\qquad
\mathcal K=\ker\mathfrak b.
$$
The cochain comparison
$$
\mathcal N\hookrightarrow\mathcal B_{\lim}\to0
\quad\longrightarrow\quad
\mathcal K\hookrightarrow\mathcal B_{\lim}\to0
$$
has the exact transported kernel
$$
\boxed{\mathcal K/\mathcal N.}
$$

An explicit commuting-observable test computes a nonzero class in this kernel. On
$$
\Omega_n=\{-1,1\}^n
$$
with product probability $2^{-n}$, let $F_j$ flip coordinate $j$, and set
$$
A_n^{\mathrm{test}}
=\sum_{j=1}^n\frac{c_{j,n}}2(I-F_j),
\qquad
c_{j,n}=1\ (j<n),\quad c_{n,n}=1/n.
$$
The Walsh functions
$$
\chi_S(\omega)=\prod_{j\in S}\omega_j
$$
satisfy
$$
A_n^{\mathrm{test}}\chi_S
=
\left(
|S\setminus\{n\}|+\frac{\mathbf1_{n\in S}}n
\right)\chi_S.
$$
Every fixed nonempty $S$ eventually has energy $|S|$, so the reconstructed centered fixed-label generator has spectral bottom one. Yet
$$
v_n=\chi_{\{n\}},
\qquad
\|v_n\|=1,
\qquad
\langle v_n,A_n^{\mathrm{test}}v_n\rangle=1/n,
\qquad
\mathfrak b(v)=0.
$$
Every fixed-label pairing is eventually zero. The sequence therefore gives an explicit nonzero element of $\mathcal K/\mathcal N$, with its norm and energy sequence retained.

This calculation corrects the inference through its exact morphism. It assigns no numerical value to the Yang-Mills gap.

## Verification and completed scope

The new checker passed **181 named exact integer, rational, and symbolic checks**. The existing Bernstein-reconstruction checker was recovered byte-for-byte and passed unchanged. The downloadable patch was applied to a fresh local tree and reproduced all six changed files exactly.

[Full verification log](sandbox:/mnt/data/yang_mills_vacuum_refinement_verification.json)

The analytic domain, measure, smooth-section, and limit arguments are written proofs in the note; the finite executable checks verify their declared algebraic test cases.

The completed advance is **uniform infrared memory control, interacting-vacuum refinement with every cross term, smooth holonomy extension with its full energy cost, and explicit cohomological records of both zero-energy limit-order effects and escaping regulator states**. A nontrivial four-dimensional continuum Yang-Mills field and a positive physical continuum mass lower bound have not been established by this contribution.


# Historical final response 4: Energy primitive strategy

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/04_energy_primitive_strategy_20260914.md}

\textbf{SHA-256:} \path{7712186a2f12aa13d8693cb706cbfc6f899cd200eb1c1fc63fe5fc0530387baa}

\textbf{Editorial provenance notice:} The complete final response is preserved for historical mathematical coverage. The standalone mathematical source chapters remain separately identifiable above.
\end{quote}

**The route I would pursue is to make Split Zero’s retained kernels quantitative in the original Yang-Mills energy norm, and then follow those quantities through spatial refinement and the continuum limit.** That connects the cohomology directly to the spectral gap.

I take “Spitzer” here to refer to the **Split Zero cohomology** we have been using. I checked the current Zeta sources, particularly the newest **original-observation addendum, OPG1-26 and OPR1-5**. Its important additions are the actual observation columns, minimum-section corrections, coupled observed/kernel dynamics, and the quotient recording every observed iterate. These give a considerably more specific starting point than the earlier support labels and finite jets alone. 

Here is the proposed mathematical strategy, with the existing results and the intended calculations kept explicit.

## 1. Put the mass gap into the language of quantitative primitives

Retain the actual finite-regulator Hamiltonian, ground energy, and vacuum:
$$
A_n=H_n-E_{0,n}I,\qquad
\rho_n=\psi_n^2,\qquad
\kappa_n=\frac{2g_n^2}{a_n}.
$$

The workbench proves the exact ground-state identity
$$
q_{A_n}(\psi_nf)
=
\kappa_n\int\rho_n
\sum_{e,\alpha}|X_{e,\alpha}f|^2\,dU_n.
$$
The multiplication map
$$
\mathcal U_n:
L^2_{\mathrm{phys}}(\rho_n\,dU_n)
\longrightarrow\mathcal H_{\mathrm{phys},n},
\qquad
f\longmapsto\psi_nf
$$
is unitary because
$$
\langle\mathcal U_nf,\mathcal U_ng\rangle
=\int\rho_n\overline f g\,dU_n.
$$
Its inverse is $u\mapsto u/\psi_n$. The full interaction remains in $\psi_n$ and therefore in $\rho_n$. 

On the centered physical form domain, define
$$
d_nf=(X_{e,\alpha}f)_{e,\alpha},
$$
with the original energy pairing on its target:
$$
\langle v,w\rangle_{1,n}
=
\kappa_n\int\rho_n
\sum_{e,\alpha}\overline{v_{e,\alpha}}w_{e,\alpha}\,dU_n.
$$

Its inverse on its actual image is
$$
p_n:\operatorname{ran}d_n\longrightarrow
L^2_{\mathrm{phys}}(\rho_n\,dU_n)\cap1^\perp,
\qquad
p_n(d_nf)=f.
$$
Uniqueness follows because a function with every original link derivative zero is constant, and the source is centered.

The physical finite-regulator gap consequently satisfies the exact identity
$$
\boxed{
\|p_n\|^2
=
\sup_{\substack{f\ne0\\ \int\rho_nf=0}}
\frac{\int\rho_n|f|^2}
{\kappa_n\int\rho_n\sum|Xf|^2}
=
\frac1{\Delta_n}.
}
$$
The last equality is the variational characterization of the first excitation, transported by $\mathcal U_n$.

**This is the direct connection to the mass-gap problem:** the size of the energy-controlled primitive is the reciprocal square root of the gap. Split Zero’s retained primitives can therefore be studied with a norm that already belongs to the original Hamiltonian.

That is the quantity I would make central. Each refinement step should carry the primitive, its energy, and its original state norm.

## 2. Apply the newest minimum-section machinery to energy matrices

The newest Zeta calculation supplies an exact minimum section and the correction between sections defined by different source metrics. In OPR2-3, that correction lands in the original kernel, and its squared norm is computed in the original kernel Gram matrix. 

There is a direct Yang-Mills application.

Take linearly independent centered smooth physical functions
$$
f_1,\ldots,f_N
$$
at regulator $n$, and retain their two matrices:
$$
G_{ij}=\int\rho_n\overline{f_i}f_j\,dU_n,
$$
$$
E_{ij}
=
\kappa_n\int\rho_n
\sum_{e,\alpha}
\overline{X_{e,\alpha}f_i}\,
X_{e,\alpha}f_j\,dU_n.
$$
Thus $G$ measures state norm and $E$ measures the full excitation energy on this window.

Let
$$
\Lambda:\mathbb C^N\twoheadrightarrow B
$$
be the matrix of the **actual observation or conditional-expectation map**, with $B$ its actual finite-dimensional image. For $s>0$, define
$$
Q_s=E+sG,
\qquad
C_s=\Lambda Q_s^{-1}\Lambda^*,
\qquad
S_s=Q_s^{-1}\Lambda^*C_s^{-1}.
$$
Here $*$ denotes coordinate conjugate transpose. Surjectivity onto $B$ makes $C_s$ positive definite.

Direct multiplication proves
$$
\Lambda S_s=I_B.
$$
For an original coefficient vector $x$, set
$$
y=\Lambda x,\qquad k=x-S_sy.
$$
Then
$$
\Lambda k=0,\qquad
k^*Q_sS_sy=k^*\Lambda^*C_s^{-1}y=0.
$$
Therefore
$$
\boxed{
x^*(E+sG)x
=
y^*C_s^{-1}y+k^*(E+sG)k.
}
$$

This is the energy-metric instance of the newest minimum-section construction. It retains both the observed energy and the energy of the class killed by observation.

The state norm remains
$$
\boxed{
x^*Gx
=
y^*S_s^*GS_sy
+2\operatorname{Re}(y^*S_s^*Gk)
+k^*Gk.
}
$$
The mixed norm term remains part of the comparison.

This gives a concrete calculation to pursue: **compare these complete energy and norm expressions across refinement, including the section-corrected kernel.**

The relevant spectral quantity on the window is
$$
\inf_{x\ne0}\frac{x^*Ex}{x^*Gx}.
$$
Taking the infimum over all finite windows in the centered form domain returns exactly $\Delta_n$: every nonzero form-domain vector belongs to its own one-dimensional window.

### Where the new exterior-volume calculations enter

The newest Zeta volume calculations supply exact Gram and determinant factorizations, including the individual observed and kernel factors and their denominators. 

For the Yang-Mills matrices above, the generalized eigenvalues satisfy
$$
\frac{\det E}{\det G}=\prod_{j=1}^N\lambda_j,
\qquad
\operatorname{tr}(G^{-1}E)=\sum_{j=1}^N\lambda_j.
$$
For $N\ge2$, the arithmetic-geometric mean inequality applied to the $N-1$ eigenvalues above the smallest gives
$$
\boxed{
\lambda_{\min}
\ge
\frac{\det E}{\det G}
\left(
\frac{N-1}{\operatorname{tr}(G^{-1}E)}
\right)^{N-1}.
}
$$

That formula explains a possible quantitative use of the exterior machinery. Every dimension factor remains visible. The newest section-corrected kernel formulas also provide more targeted information about individual weak directions.

The original Zeta Gamma constants stay attached to their original measures and period maps. The Yang-Mills inputs to this application are the displayed $E,G,\Lambda$, evaluated from its actual vacuum.

## 3. Concentrate the calculation on the interacting refinement kernel

The most promising existing Yang-Mills structure is the conditional refinement in the actual vacuum measure.

For a coarse-to-fine pair $r<n$, the contribution in PR #4 constructs
$$
\mathsf E:
L^2(\rho_n\,dU_n)\to L^2(m_{r,n}\,dW),
\qquad
\mathsf Jg=g\circ\pi_{r,n},
$$
with
$$
\mathsf E\mathsf J=I,\qquad \mathsf E=\mathsf J^*.
$$
For
$$
g=\mathsf Ef,\qquad h=f-\mathsf Jg,
$$
the exact decomposition is
$$
\|f\|_{\rho_n}^2=\|g\|_{m_{r,n}}^2+\|h\|_{\rho_n}^2,
\qquad
h\in\ker\mathsf E.
$$
The corresponding cohomology quotient and inverse are
$$
L^2(\rho_n\,dU_n)/\ker\mathsf E
\xrightarrow{\;\cong\;}
L^2(m_{r,n}\,dW),
\qquad
[f]\mapsto\mathsf Ef,\quad
g\mapsto[\mathsf Jg].
$$
The exact energy formula retains every cross term involving $h$. 

The interaction between retained variables and kernel variables is explicitly located in
$$
S_{e,\alpha}
=
Y_{e,\alpha}\log\rho_n
-\mathsf J(X_{e,\alpha}\log m_{r,n}),
$$
through
$$
v_{e,\alpha}=\mathsf E(hS_{e,\alpha}).
$$
In particular, the energy contains
$$
\kappa_nb\int m_{r,n}\sum_{e,\alpha}
|X_{e,\alpha}g-v_{e,\alpha}|^2\,dW,
\qquad b=2^{n-r},
$$
together with the two retained fluctuation-energy terms.

This identifies an actual quantity to investigate:
$$
\Gamma_{ab}(W)=\mathsf E(S_aS_b)(W),
$$
where $a,b$ denote the original coarse-edge/generator indices. Conditional Cauchy-Schwarz proves
$$
\boxed{
v(W)v(W)^*
\preceq
\mathsf E(|h|^2)(W)\,\Gamma(W).
}
$$
Indeed, contraction by any coefficient vector $z$ gives
$$
|\mathsf E(h\,z^*S)|^2
\le
\mathsf E(|h|^2)\,\mathsf E(|z^*S|^2).
$$

**I would focus the next substantial continuation here:** evaluate the actual conditional density-derivative covariance and its interaction with the kernel energy, using the newest energy-dependent minimum sections.

This uses specifically interacting Yang-Mills information. It also addresses the complete multiscale form already recorded in PR #4:
$$
q_{A_n}(\psi_nf)
=
\sum_{r,s}
\kappa_n\int\rho_n
\sum_{e,\alpha}
\overline{X_{e,\alpha}d_r}\,
X_{e,\alpha}d_s.
$$
The off-diagonal entries are retained throughout the proposed analysis. 

## 4. Use the newest dynamical quotient to track hidden states

OPG23-24 constructs
$$
\mathcal K_\infty
=
\bigcap_a\ker(\Lambda Y^a)
$$
and an explicit action-preserving quotient carrying every observed iterate. Its coupled recurrence also retains the contribution from the original kernel back into the observed variables. 

For the full Yang-Mills operator, use the bounded resolvent
$$
T_{n,s}=(A_n+sI)^{-1},\qquad s>0,
$$
and an actual observation map $\Lambda_n$. Define
$$
\mathcal O_{n,s}:
\mathcal H_{\mathrm{phys},n}\to
\prod_{j=0}^{\infty}B_n,
\qquad
u\mapsto
\bigl(\Lambda_nT_{n,s}^{\,j}u\bigr)_{j\ge0}.
$$
Its kernel is exactly
$$
\mathcal D_{n,s}
=
\bigcap_{j\ge0}\ker(\Lambda_nT_{n,s}^{\,j}).
$$
The identity
$$
\mathcal O_{n,s}T_{n,s}
=
\operatorname{Shift}\,\mathcal O_{n,s}
$$
follows component by component. Hence
$$
\boxed{
\mathcal H_{\mathrm{phys},n}/\mathcal D_{n,s}
\xrightarrow{\;\cong\;}
\operatorname{im}\mathcal O_{n,s},
\qquad
[u]\mapsto\mathcal O_{n,s}u
}
$$
intertwines the original resolvent with the shift.

This supplies a principled way to enlarge the observation while retaining its full dynamical kernel.

At the regulator-sequence level, our preceding contribution also retains
$$
\mathcal K/\mathcal N,
$$
the classes of bounded state sequences invisible to the reconstructed fixed-label observations, modulo sequences whose norms tend to zero. The explicit moving-label example in that contribution shows why this quotient deserves an energy calculation of its own. 

Thus the intended continuum analysis follows **both** observed states and retained kernel states, with their energies. It does not stop at the six initial loop observables.

## 5. What the existing estimates contribute-and where to aim next

The existing infrared Schur estimate is useful:
$$
M_n(0)=\int\lambda^{-1}\,d\sigma_n(\lambda)
\preceq K_n.
$$
For the six heat-transported loops,
$$
K_n\preceq\frac{24}{e\tau}I_6.
$$
The same calculation retains the endpoint correction
$$
F_\infty(0+)=S_\infty+Z_\alpha.
$$
These provide control of memory and of the order of the zero-energy limits. 

The next target should be a **strict quantitative energy margin**, including the retained kernel. The following exact block calculation explains that choice.

For $0<\varepsilon<1$, take
$$
A_\varepsilon=
\begin{pmatrix}
1&\sqrt{1-\varepsilon}\\
\sqrt{1-\varepsilon}&1
\end{pmatrix},
\qquad
Rz=(z,0).
$$
The associated blocks are
$$
G=1,\quad K=1,\quad D=1,\quad B=\sqrt{1-\varepsilon},
$$
so
$$
M(0)=1-\varepsilon\le K,\qquad F(0)=\varepsilon.
$$
Direct evaluation of the characteristic polynomial gives
$$
\lambda_{\min}(A_\varepsilon)
=
1-\sqrt{1-\varepsilon}\longrightarrow0.
$$
Thus the present memory inequality accommodates arbitrarily small spectral edges. The exact amount left after memory subtraction is a natural next quantity.

Two features of the original workbench also determine the scope of that investigation.

**The fixed-box oscillator calculation supplies exact local spectral and interaction data.** Its comparison gap is
$$
\delta_{\mathrm{osc}}(L,a)
=
\frac{4\sqrt2}{a}\sin\frac{\pi}{4L+2}.
$$
On our displayed refinement sequence $L_n=4\,2^{2n}$, $a_n=a_0\,2^{-n}$, this quantity tends to zero. The source theorem keeps $L,a$ fixed when taking $g\downarrow0$. I would therefore use its cubic vertex and tensor-band calculations to evaluate the original coupling entries, while directing the physical lower-edge calculation through the full interacting multiscale form. 

**The volume-uniform vacuum results supply local resolvent identities and explicit covariance estimates.** Their parameter is
$$
\xi=\frac1{4g^4}.
$$
On the current test path,
$$
\xi_n=
\frac{(g_0^{-2}+\beta n\log2)^2}{4}\longrightarrow\infty.
$$
An estimate stated for $0<\xi\le1/64$ enters precisely on that parameter range. The all-coupling identities remain available with their displayed dependence on $\xi_n$. This parameter accounting has to remain visible in the refinement calculation. 

## The research direction I recommend

The next contribution should be a connected **energy-controlled Split Zero refinement calculation**.

Its primary object should be the primitive norm $ \|p_n\| $, evaluated through the original conditional refinement, the full density derivative, and the newest section-corrected kernel machinery. Its dynamical companion should be the all-iterate observation quotient, retaining the energy of state sequences whose labels move with the regulator. The exterior-volume machinery should support quantitative estimates on those actual energy and Gram matrices.

Smooth continuation remains part of this construction through explicit coordinate and frame transports. For an invertible retained frame map $T$,
$$
G^T=T^*GT,\qquad E^T=T^*ET,
$$
and the substitution $x=Tz$ proves
$$
\inf_{z\ne0}\frac{z^*E^Tz}{z^*G^Tz}
=
\inf_{x\ne0}\frac{x^*Ex}{x^*Gx}.
$$
That gives smooth frame changes an exact role in the same spectral calculation.

**The ambitious target remains one physical four-dimensional continuum theory with a strictly positive excitation-energy edge.** The reviewed calculations have not established that endpoint. They now identify a focused place to work toward it: the energy of the retained multiscale kernels and their coupling to the observed sector, measured in the original physical units.

No repository changes were made during this review.


# Historical final response 5: Local score workflow

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/05_local_score_workflow_20260914.md}

\textbf{SHA-256:} \path{a31c9ebd6c4a5414c47ece5e3bd5410f63fbfee12e58a114fdc9803d3207aa28}

\textbf{Editorial provenance notice:} The complete final response is preserved for historical mathematical coverage. The standalone mathematical source chapters remain separately identifiable above.
\end{quote}

I’ve implemented the workflow, run its first research-and-verification cycle, and opened **draft pull request #5, “Add research workflow and exact local-score energy refinement.”** It is based on the existing PR #4 branch, preserves that work, and adds eight files. Neither pull request has been merged. The new commit is `f583ed5ddb13b3ca517c1bab2958f6a4be612d78`. 

[Complete workflow, mathematics, checker, and execution records](sandbox:/mnt/data/yang_mills_workflow_and_energy_refinement.zip) · [Read the workflow](sandbox:/mnt/data/yang_mills_research_workflow.md) · [Read the mathematical continuation](sandbox:/mnt/data/yang_mills_local_score_energy_note.md)

## 1. The workflow now lives in the workbench

The entry point is `yang-mills/AGENTS.md`. It directs an active research session to read the current mathematical state, inspect relevant developments in the other workbenches, select a connected calculation, execute the checks, and leave an explicit mathematical checkpoint.

The governing quantity is the original energy-controlled primitive:
$$
p_n(d_nf)=f,
\qquad
d_nf=(X_{e,\alpha}f)_{e,\alpha},
$$
on centered physical functions, with the original energy pairing
$$
\|d_nf\|_{1,n}^{2}
=
\frac{2g_n^2}{a_n}
\int\rho_n\sum_{e,\alpha}|X_{e,\alpha}f|^2\,dU_n.
$$
The ground-state transform and variational characterization give
$$
\boxed{\|p_n\|^2=\frac1{\Delta_n}.}
$$
Thus the workflow has an actual spectral quantity to return to, rather than using the number of calculations or checker assertions as a progress measure. The original Hamiltonian and ground-state identity remain the source of this pairing. 

The active loop has four connected stages:

| Stage | What it records or does |
|---|---|
| **Source intake** | Reads current default branches **and open pull requests**, records exact revisions and file identities, and distinguishes proof reading from discovery through a PR description. |
| **Mathematical selection** | Names the original quantity to improve and the maps, norms, domains, parameters, and retained kernels involved. |
| **Derivation and checking** | Writes the argument, runs exact tests and deliberately false formulas, and keeps analytical proof review separate from executable evidence. |
| **Continuation and publication** | Updates the mathematical state and attempt account, checks the dependency revisions, and submits an additive review branch with a precise next calculation. |

The machine-readable `state.json` contains the completed result identifiers, their dependencies, eight source records, explicit cross-workbench transfers, unevaluated quantities, and the next selected calculation. The workflow and checker are stored with the proof and execution record. 

**Source freshness has an explicit interface:** the active session gathers current GitHub revisions; the checker compares that snapshot with the recorded intake. A changed revision causes a named failure until its changes have been read and classified. The Python checker itself makes no network calls.

## 2. I checked the other number-theory workbenches

This produced useful input immediately, including developments on unmerged branches.

### Split Zero / Zeta: applied in this continuation

The current arithmetic-to-Gamma source-transfer calculation, **AMT7-10**, proves minimum-section composition on the same observation fibers while retaining the quotient and kernel metrics. The newer **PR #32** supplies the complete rectangular residual identity
$$
(X-S_G\Lambda X)^*G(X-S_G\Lambda X)
=
X^*GX-(\Lambda X)^*Q(\Lambda X),
$$
including the section correction and all off-diagonal entries. I read those arguments and instantiated their maps with the original Yang-Mills energy and state forms. Their arithmetic constants remain attached to their original measures. 

This was a substantive update to our earlier intake: the workflow now follows both the analytical source development and the independent formalization branches.

### Collatz: an exact regression against losing source information

The inspected history construction retains the explicit specialization fiber
$$
X_v(q)-X_u(q)=\frac{(q-3)(q+4)}{32},
\qquad
X_u(3)=X_v(3)=\frac{19}{32}.
$$
The checker now uses this actual example to reject reconstruction of the original history from the specialized value alone. The polynomial difference and its kernel membership remain recorded. 

The newer stopped, residual, and anchored continuations were also found through the open-PR scan. Their new descriptions are recorded as candidates for further source reading, rather than treated as already imported Yang-Mills results.

### Erdős-Straus: retained as a specific candidate

I inspected the new original-state construction in PR #6: its prime-labelled denominator defects, highest-degree kernel classes, and augmentation map that returns the actual success projector. That supplies a concrete candidate for later endpoint-observation work. The later moment estimates were discovered in the PR description; their proof bodies have not been imported into the present Yang-Mills calculation. 

### Erdős 817: used to strengthen the verification workflow

Its workbench validator provided a useful model for binding claims and receipts to exact source files, rejecting duplicate keys and invalid paths, and retaining the scope of each verification record. I used that design precedent for the independently written Yang-Mills checker. The newer outer-controller work is recorded separately as a mathematical candidate. 

This gives later sessions a maintained exchange record: **what was found, what was actually read, what was transferred by an explicit map, and what remains only a candidate.**

## 3. The mathematical advance from this cycle

The connected calculation follows the original interacting vacuum through

$$
\text{local electric expectations}
\longrightarrow
\text{conditional density derivatives}
\longrightarrow
\text{Hamiltonian coupling}
\longrightarrow
\text{minimum-energy refinement}.
$$

### A local bound without an exterior-volume factor

Retain
$$
\rho_n=\psi_n^2,\qquad
\kappa_n=\frac{2g_n^2}{a_n},
\qquad
\xi_n=\frac1{4g_n^4}.
$$
For refinement from level $r$ to level $n$, let
$$
b=2^{n-r}
$$
be the number of original fine links in each coarse link.

Let $\mathsf E$ be conditional expectation in the **actual fine vacuum**, $\mathsf J$ the ordered-holonomy pullback, and $m$ the actual coarse marginal. The original horizontal derivative is
$$
Y_{e,\alpha}
=
\frac1b\sum_{j,\beta}
\bigl(\operatorname{Ad}P_{e,j-1}\bigr)_{\alpha\beta}
X_{e,j,\beta}.
$$
Define the retained logarithmic density derivative
$$
S_{e,\alpha}
=
Y_{e,\alpha}\log\rho_n
-\mathsf J(X_{e,\alpha}\log m).
$$
It has conditional mean zero. Its conditional covariance is the complete matrix
$$
\Gamma_{ac}(W)=\mathsf E(S_aS_c)(W).
$$

For a finite set $F$ of coarse links, the new estimate is
$$
\boxed{
\begin{aligned}
I_F
&:=\int m\,\operatorname{tr}\Gamma\\
&\le
\frac4b
\sum_{e\in F}\sum_{j=1}^{b}
\min\!\left(
2r_{e,j}\xi_n,\,
\frac{16}{3}r_{e,j}^{\,2}\xi_n^2
\right)\\
&\le 32|F|\xi_n .
\end{aligned}}
$$
Here $r_{e,j}$ is the number of original plaquettes incident on the fine link.

The proof retains the full exterior operator. The original local vacuum equation is
$$
(\kappa_nE_e+K_e)\psi_n=v_nW_e\psi_n,
\qquad
K_e\ge0,\qquad
v_n=\frac1{2g_n^2a_n}.
$$
Taking its expectation gives
$$
\langle\psi_n,E_e\psi_n\rangle
\le 2r_e\xi_n.
$$
Conditional variance, the identity
$$
\rho_n|Y\log\rho_n|^2=4|Y\psi_n|^2,
$$
and the adjoint-matrix coefficients of the original horizontal fields then give the displayed bound.

**The exterior volume has disappeared from this local estimate. The coupling dependence remains.** On the current test path,
$$
g_n^2=(g_0^{-2}+\beta n\log2)^{-1},
$$
the resulting bound is
$$
I_F\le8|F|(g_0^{-2}+\beta n\log2)^2.
$$
That growth is recorded explicitly in the mathematical state.

### The same quantity gives the exact Hamiltonian coupling

Put
$$
\mathcal K=\ker\mathsf E,
\qquad
(Th)_a=\mathsf E(hS_a).
$$
The actual adjoint and covariance identities are
$$
T^*u=\sum_a S_a\,\mathsf Ju_a,
\qquad
TT^*=\Gamma.
$$

For a smooth coarse function $f$, the component of the full transported Hamiltonian landing in the retained kernel is exactly
$$
\boxed{
Cf=-\kappa_nb\,T^*Xf.
}
$$

Thus the density derivative being bounded is precisely part of the original interaction between retained variables and fiber fluctuations. It enters the energy calculation through an explicitly derived operator.

### Minimum-energy sections now compose through refinement

Let $D$ be the nonnegative self-adjoint operator represented by the original energy form restricted to $\mathcal K$. The note proves its closed-form domain and defines, for $s>0$,
$$
h_s(f)=\kappa_nb(D+s)^{-1}T^*Xf,
\qquad
\mathcal S_sf=\mathsf Jf+h_s(f).
$$

This is the minimum-energy lift of $f$ in its original conditional-expectation fiber. Its complete effective form is
$$
\boxed{
\begin{aligned}
q_{\mathrm{eff},s}(f,v)
={}&s\langle f,v\rangle_m
+\kappa_nb\langle Xf,Xv\rangle_m\\
&-(\kappa_nb)^2
\left\langle
T^*Xf,(D+s)^{-1}T^*Xv
\right\rangle_{\rho_n}.
\end{aligned}}
$$

The derivative retains the restored state metric:
$$
\boxed{
\frac{d}{ds}q_{\mathrm{eff},s}(f,v)
=
\langle\mathcal S_sf,\mathcal S_sv\rangle_{\rho_n}.
}
$$
For a residual $k\in\mathcal K$, the original state norm remains
$$
\|\mathcal S_sf+k\|_{\rho_n}^2
=
\|f\|_m^2+\|h_s(f)+k\|_{\rho_n}^2,
$$
including the mixed term inside the last square.

Finally, for $r<t<n$,
$$
\boxed{
\mathcal S_{r,n;s}
=
\mathcal S_{t,n;s}\,
\mathcal S_{r,t;s}^{(n)}.
}
$$
The middle section uses the **actual induced intermediate energy form and the marginal of the same fine vacuum**. The proof minimizes over those same fibers in two stages. It extends through every finite refinement chain.

This is where the newly inspected Split Zero minimum-section machinery has been applied to the Yang-Mills program.

## 4. What the checker actually checks

The new program passed **56 named exact checks and 17 named negative controls**. Ordinary and optimized Python produced byte-identical output; a fresh copied-source directory reproduced it. The previous PR #4 checker also passed its 181 checks separately. The complete records are included in the package. 

[Inspect the new verification record](sandbox:/mnt/data/yang_mills_research_control_verification.json)

The mathematical tests compare the section formula with an independently assembled constrained linear system, retain full mixed Gram matrices, verify refinement composition, and exercise both delayed and permanently invisible observations.

The negative controls include replacing the original Gram matrix by an identity matrix, dropping state-norm cross terms, substituting the uncorrected middle form, and converting an integrated score bound into a pointwise bound. Four additional command-line corruption tests were executed in both Python modes; each returned a nonzero exit status at its intended named failure.

A complete replay from the repository or archive root is:

```sh
python -B yang-mills/research-control/check.py \
  --verify-receipt yang-mills/research-control/verification.json
```

The receipt comparison binds the result to the actual proof, workflow, registry, and checker bytes. **The analytical proofs remain written arguments for review; these finite tests do not certify them as formal proofs.** No new Lean run or peer-CI replay was claimed.

## 5. The recorded continuation point

The next selected quantity is now explicit:
$$
\boxed{
(\kappa_nb)^2
\left\langle
T^*Xf,(D+s)^{-1}T^*Xv
\right\rangle_{\rho_n}.
}
$$
The intended calculation compares this actual response with the original kinetic form and the restored state metric on growing physical observation families, retaining every residual energy in the refinement composition.

The present work has not evaluated those interacting-vacuum response integrals or established a positive continuum mass lower bound. It has supplied a local estimate and an exact refinement mechanism through which that quantitative investigation can proceed.

The workflow, source intake, proofs, tests, and next calculation are now available to later sessions and Codex on the PR branch. No Codex job was started, and no research process is running between sessions.


# Historical final response 6: Coupled response

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/06_coupled_response_20260914.md}

\textbf{SHA-256:} \path{7d53dbd71c80304abecc2cb6f60ddd8652ab45d99dee1f9bfd35b2fb3a71e894}

\textbf{Editorial provenance notice:} The complete final response is preserved for historical mathematical coverage. The standalone mathematical source chapters remain separately identifiable above.
\end{quote}

**The Hamiltonian/self-adjointness connection is now recorded in the workbench, and I developed it into a concrete continuation of the Yang-Mills response calculation.** I opened **draft PR #6, “Coupled Hamiltonian response: retained cohomology and two-sided energy certificates,”** at commit `e98b2c3af77f66fb1c1396143ca53daef586404f`. It adds nine files on top of PR #5, preserving the earlier sources and receipts; nothing has been merged. 

[Full mathematical note](sandbox:/mnt/data/yang_mills_coupled_response_note.md) · [Proofs, checker, and execution records](sandbox:/mnt/data/yang_mills_coupled_response.zip) · [Git patch](sandbox:/mnt/data/yang_mills_coupled_response.patch)

The main advance is **an exact connection between the retained cohomology class and the error in the Hamiltonian response**. That supplies two-sided bounds for the effective energy and bounds for the restored state metric.

## 1. The coupling has an explicit self-adjoint realization

At a fixed original regulator, retain the conditional-expectation kernel
$$
\mathcal K=\ker\mathsf E,
$$
and its nonnegative self-adjoint energy operator $D$. For a finite independent family of centered smooth coarse observables $f_i$, retain
$$
G_{ij}=\langle f_i,f_j\rangle_m,
\qquad
(K_0)_{ij}=\kappa_n b\langle Xf_i,Xf_j\rangle_m,
$$
and the actual coupling
$$
Wx=\kappa_n b\,T^*X\!\left(\sum_i x_if_i\right).
$$
Here $m$ is the marginal of the interacting fine vacuum, and $T$ is the conditional density-derivative operator from the preceding calculation. These are the same physical quantities already used in PR #5. 

On $\mathbb C^m\oplus\mathcal K$, keep the pairing
$$
\langle(x,h),(y,k)\rangle_G=x^*Gy+\langle h,k\rangle_{\rho_n}.
$$
The coupled operator is
$$
\boxed{
\mathcal H_F
\begin{pmatrix}x\\h\end{pmatrix}
=
\begin{pmatrix}
G^{-1}(K_0x-W^*h)\\
Dh-Wx
\end{pmatrix},
\qquad
\operatorname{Dom}\mathcal H_F
=
\mathbb C^m\oplus\operatorname{Dom}D.
}
$$

Its diagonal operator is self-adjoint in this pairing. Its two off-diagonal terms are bounded and are each other’s adjoints in that same pairing. The note proves self-adjointness on the displayed domain by factoring the resolvents through the diagonal operator. The map back to the original physical functions is
$$
V(x,h)=\mathsf J\!\left(\sum_i x_if_i\right)+h,
$$
with
$$
q_F(u,v)=q_n(Vu,Vv).
$$
The energy coupling to the remaining coarse functions is also retained explicitly. 

For the complex spectral parameter, define
$$
M(z)=W^*(D-z)^{-1}W,\qquad
F(z)=K_0-zG-M(z),
$$
$$
L_zx=\bigl(x,(D-z)^{-1}Wx\bigr).
$$
The resolvent identity gives the complete two-parameter formula
$$
\boxed{
-\frac{F(z)-F(w)^*}{z-\overline w}
=
G+W^*(D-\overline w)^{-1}(D-z)^{-1}W
=
L_w^*L_z.
}
$$
In particular,
$$
\boxed{
-\frac{\operatorname{Im}F(z)}{\operatorname{Im}z}=L_z^*L_z,
\qquad
\operatorname{Im}F=\frac{F-F^*}{2i}.
}
$$

That is a reusable connection between **a coupled self-adjoint operator, its complex response, and the original state inner product**. The general elimination mechanism belongs to established Feshbach-Schur machinery; the contribution here spells out its domains, raw Gram factors, and retained conditional kernel for this workbench.  ([arXiv](https://arxiv.org/abs/2105.02058))

## 2. The unresolved response now carries an exact error certificate

This is the part most directly useful for continuing the mass-gap calculation.

For $s>0$, let
$$
M_s=W^*(D+s)^{-1}W.
$$
Take trial columns
$$
Y:\mathbb C^m\longrightarrow\operatorname{Dom}D
$$
and retain their residual
$$
R_Y=W-(D+s)Y.
$$
Define
$$
B_Y=W^*Y+Y^*W-Y^*(D+s)Y.
$$

Expanding the complete residual expression proves
$$
\boxed{
M_s=B_Y+R_Y^*(D+s)^{-1}R_Y.
}
$$
Since $D\ge0$,
$$
\boxed{
B_Y\preceq M_s
\preceq B_Y+\frac1sR_Y^*R_Y.
}
$$
Consequently, the effective energy matrix satisfies
$$
\boxed{
K_0+sG-B_Y-\frac1sR_Y^*R_Y
\preceq F_s
\preceq K_0+sG-B_Y.
}
$$

The restored-state error is controlled by the same original residual:
$$
\boxed{
\bigl((D+s)^{-1}W-Y\bigr)^*
\bigl((D+s)^{-1}W-Y\bigr)
=
R_Y^*(D+s)^{-2}R_Y
\preceq\frac1{s^2}R_Y^*R_Y.
}
$$
The note carries this through to bounds on the restored state metric, retaining its mixed terms. 

### Its Split Zero interpretation is literal

For nested finite trial spaces $V_j\subset\operatorname{Dom}D$, use the actual complexes
$$
V_j\xrightarrow{D+s}\mathcal K\xrightarrow0 0.
$$
Their cohomology is
$$
H_j^1=\mathcal K/(D+s)V_j.
$$
The transported-class kernel has the explicit isomorphism
$$
\boxed{
V_{j+1}/V_j
\longrightarrow
\ker(H_j^1\to H_{j+1}^1),
\qquad
[h]\longmapsto[(D+s)h].
}
$$
Its inverse sends the class represented by $(D+s)h$ to $[h]$. Changing that representative by $(D+s)V_j$ changes the inverse by precisely $V_j$.

With the original resolvent pairing
$$
\langle r,t\rangle_{\mathrm{dual},s}
=
\langle r,(D+s)^{-1}t\rangle,
$$
the canonical residual represents the unresolved forcing class, and its **full quotient Gram matrix is exactly**
$$
M_s-B_Y.
$$

Thus enlarging the admitted primitive space comes with a computable energy-error matrix. The support transition, killed class, primitive, and quantitative cost remain connected by their actual maps. 

## 3. The next physical inputs are now three specific matrices

The calculation reaches a finite-moment interface:
$$
\boxed{
N_0=W^*W,\qquad
N_1=W^*DW,\qquad
N_2=W^*D^2W.
}
$$

For the first trial space $\operatorname{ran}W$, the coefficient equation is
$$
(N_1+sN_0)X=N_0,\qquad Y=WX.
$$
The complete solution fiber is retained when the coefficient matrix is singular. Indeed,
$$
\ker(N_1+sN_0)=\ker W,
$$
because its quadratic form is
$$
\|D^{1/2}Wx\|^2+s\|Wx\|^2.
$$
Thus different coefficient solutions produce the same actual trial vector $Y$.

Higher trial spaces retain
$$
W,\ DW,\ldots,D^dW,
$$
and moments through order $2d+2$ determine the corresponding response and residual matrices. The shifted cross moments
$$
N_{i+1}+sN_i
$$
remain in the residual formula; the checker explicitly rejects replacing them by unshifted moments. 

**The actual Yang-Mills entries of $N_0,N_1,N_2$ have not been evaluated in this cycle.** They are now the recorded next calculation, with a precise route from their enclosures to the effective energy, restored norm, and original primitive norm.

## 4. The workflow and peer exchange were exercised

The new checker passed **189 exact checks and 12 deliberately false-formula controls**, with identical results in ordinary and optimized Python. A fresh copied-source replay reproduced the receipt, and the additive patch was applied to the delivered parent and reproduced it again. The unchanged parent checker also passed against its original receipt. The tests include raw-metric self-adjointness, an independently assembled block inverse, complex spectral parameters, singular moment fibers, and full residual Grams. These are declared finite fixtures; the analytical arguments remain written proofs for review. 

[Inspect the complete verification record](sandbox:/mnt/data/yang_mills_coupled_response_verification.json)

The source refresh also detected further Zeta exterior-conductor developments and a new Erdős-Straus higher-support/Green-norm continuation. Those were recorded at their actual reading scope. The mathematical import used here is the pinned Zeta finite-resolvent identity, instantiated by
$$
H\mapsto(\sigma-s)(D+\sigma)^{-1},
\qquad
T\mapsto(D+\sigma)^{-1},
\qquad
X\mapsto(D+s)^{-1}.
$$
The newer asymptotic and higher-support claims remain candidates for proof-body inspection. 

The active checkpoint is now `yang-mills/research-control/CURRENT.md`. It preserves your Hamiltonian/self-adjointness observation as a cross-project direction while keeping the next execution focused on the original Yang-Mills response matrices. **A positive continuum mass lower bound remains unestablished; this cycle supplies the coupled-operator and residual certificates needed to assess that next calculation quantitatively.**


# Historical final response 7: Actual loop moments

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/07_actual_loop_moments_20260915.md}

\textbf{SHA-256:} \path{0c2d397cc674a8ac40efd3f8098e1ade659a3c83f7ef088ad5b9220f6be941b7}

\textbf{Editorial provenance notice:} The complete final response is preserved for historical mathematical coverage. The standalone mathematical source chapters remain separately identifiable above.
\end{quote}

I have now obtained **explicit enclosures for the actual interacting-vacuum moments $N_0,N_1,N_2$, the Schur response, and the restored state norm**. The calculation also gives new all-coupling estimates with constants independent of the exterior volume.

[Full mathematical proof](sandbox:/mnt/data/yang_mills_actual_loop_moments_note.md) · [Complete research and verification package](sandbox:/mnt/data/yang_mills_actual_loop_moments.zip) · [Workbench patch](sandbox:/mnt/data/yang_mills_actual_loop_moments.patch)

The narrow numerical enclosures below are proved at
$$
\xi=\frac1{4g^4}=10^{-8},
\qquad g^2=5000,
\qquad \kappa=\frac{10000}{a},
$$
for **every $a>0$ and every exterior box $L\ge2$**. This is a large-$g$ domain. The all-coupling results are stated separately, with their actual dependence on $g,a$, and loop length retained.

## 1. The previously unevaluated response quantities now have values enclosed

Keep the full original operator
$$
H=\kappa K+V,\qquad
K=-\sum_{e,\alpha}X_{e,\alpha}^{\,2},
$$
$$
V=\frac1{2g^2a}\sum_p(2-\operatorname{tr}U_p),
\qquad
\kappa=\frac{2g^2}{a}.
$$
Let $\psi$ be its actual positive unit vacuum, $E_0$ its ground energy, and $\rho=\psi^2$. The transported excitation operator is
$$
\mathcal A=\psi^{-1}(H-E_0)\psi,
$$
with the original form
$$
q_{\mathcal A}(f,h)
=\kappa\int\rho\sum_{e,\alpha}
\overline{X_{e,\alpha}f}\,X_{e,\alpha}h\,dU.
$$
These are the workbench’s original Hamiltonian, vacuum, and physical coefficients. 

Take the elementary square based at the origin in directions $1,2$, with its complete holonomy
$$
\Omega=
U_1(0)\,U_2(\mathbf e_1)\,
U_1(\mathbf e_2)^{-1}\,U_2(0)^{-1},
\qquad F=\operatorname{tr}\Omega.
$$

Let $\mathsf E$ be conditional expectation onto this holonomy **in the actual measure $\rho\,dU$**, let $\mathsf J$ be pullback, and put
$$
Q=I-\mathsf J\mathsf E,\qquad \mathcal K=\ker\mathsf E.
$$
The operator $D$ is represented by the original closed energy form restricted to $\mathcal K$. Thus its domain retains the full conditional kernel, including exterior degrees of freedom.

The actual forcing and moments are
$$
W=-Q\mathcal AF,
$$
$$
N_0=\|W\|_\rho^2,\qquad
N_1=\langle W,DW\rangle_\rho,\qquad
N_2=\|DW\|_\rho^2.
$$

The new bounds are
$$
\boxed{
0.9994\,\kappa^2\xi^2<N_0<1.0006\,\kappa^2\xi^2,
}
$$
$$
\boxed{
4.9963\,\kappa^3\xi^2<N_1<5.0037\,\kappa^3\xi^2,
}
$$
$$
\boxed{
25.728\,\kappa^4\xi^2<N_2<25.772\,\kappa^4\xi^2.
}
$$

In particular, the forcing is quantitatively nonzero in the actual interacting vacuum.

For the actual response at the physical shift $s=\kappa$,
$$
M(\kappa)=\langle W,(D+\kappa)^{-1}W\rangle_\rho,
$$
the calculation proves
$$
\boxed{
\left|M(\kappa)-\frac{28}{165}\kappa\xi^2\right|
<0.0000075\,\kappa\xi^2.
}
$$
For the restored kernel primitive,
$$
\boxed{
\left|
\|(D+\kappa)^{-1}W\|_\rho^2
-\frac{796}{27225}\xi^2
\right|
<0.0000021\,\xi^2.
}
$$

The raw observed Gram and kinetic entry remain present:
$$
G=\langle F^2\rangle_\rho-\langle F\rangle_\rho^2,
\qquad
K_0=\kappa\bigl(4-\langle F^2\rangle_\rho\bigr).
$$
At the same coupling,
$$
|G-1|<1.1\times10^{-13},
\qquad
|K_0-3\kappa|<1.1\times10^{-13}\kappa.
$$

These intervals come from explicit analytical remainder bounds evaluated with rational arithmetic. They use no sampled vacuum, fitted density, or spin cutoff. The complete calculations are equations A37-A49 of the attached proof.

### The observation change is explicitly retained

The loop observation is connected to the preceding coarse-edge observation by
$$
\pi_C=\chi_C\circ\pi_{\mathrm{edges}},
\qquad
\mathsf E_C=\mathsf E_\chi\mathsf E_{\mathrm{edges}},
$$
where $\chi_C$ multiplies the original four coarse links with their original orientations.

The additional kernel has the exact isomorphism
$$
\boxed{
\ker\mathsf E_C/\ker\mathsf E_{\mathrm{edges}}
\longrightarrow\ker\mathsf E_\chi,
\qquad
[h]\longmapsto\mathsf E_{\mathrm{edges}}h,
}
$$
with inverse
$$
k\longmapsto[\mathsf J_{\mathrm{edges}}k].
$$
The identities $\mathsf E_{\mathrm{edges}}\mathsf J_{\mathrm{edges}}=I$ and
$h-\mathsf J_{\mathrm{edges}}\mathsf E_{\mathrm{edges}}h
\in\ker\mathsf E_{\mathrm{edges}}$ prove both inverse laws. The moments above are attached to this specified loop observation, and the additional kernel remains part of the energy calculation.

## 2. The key new estimate comes from the actual vacuum equation

Write
$$
u=\log\psi,\qquad b_{e,\alpha}=X_{e,\alpha}u,
\qquad
\mathscr L=\sum_iX_i^2+2\sum_i b_iX_i.
$$
The vacuum equation gives
$$
\sum_iX_i^2u+\sum_i b_i^2=\frac{V-E_0}{\kappa},
\qquad
\mathcal A=-\kappa\mathscr L.
$$

Commutation of the original Casimir with each $X_{e,\alpha}$, together with the antisymmetric generator coefficients, gives the exact differentiated equation
$$
\boxed{
\mathcal A b_{e,\alpha}=-X_{e,\alpha}V.
}
$$

This provides a direct equation for the vacuum derivatives entering the response.

For
$$
w_e=\sum_\alpha b_{e,\alpha}^2,
$$
the original commutators
$$
[X_{e,\alpha},X_{e,\beta}]
=-\epsilon_{\alpha\beta\gamma}X_{e,\gamma}
$$
give
$$
\sum_{i,\alpha}|X_i b_{e,\alpha}|^2\ge\frac12w_e.
$$
The term on the right is the squared norm of the antisymmetric part of the original second-derivative matrix.

At a maximum of $w_e$,
$$
0\ge\frac12\mathscr Lw_e
\ge\frac12w_e-r_e\xi\sqrt{w_e},
$$
where $r_e\le4$ is the actual number of incident plaquettes. Therefore, at **every positive coupling**,
$$
\boxed{
\|X_e\log\psi\|_\infty\le2r_e\xi\le8\xi,
\qquad
\|X_e\log\rho\|_\infty\le16\xi.
}
$$

There is also an exact derivative-energy identity:
$$
\boxed{
\int\rho\sum_{i,\alpha}|X_i b_{e,\alpha}|^2
=
\frac{3\xi}{8}
\left\langle\sum_{p\ni e}W_p\right\rangle_\rho
\le\frac{3r_e\xi}{4}.
}
$$
The index $i$ here runs over **all fine-link derivatives**.

Both results have constants independent of the number of exterior links and faces. They provide the control needed to differentiate the actual forcing and bound $N_1,N_2$.

### A controlled local term and its retained remainder

Set
$$
u_0=\frac{\xi}{3}\sum_pW_p,
\qquad
\mathfrak r_e=X_e(u-u_0).
$$
The full Hamiltonian remains unchanged. The remainder satisfies its own exact equation,
$$
\mathscr L\mathfrak r_{e,\alpha}
=-2\sum_i b_iX_i(X_{e,\alpha}u_0).
$$

For $0<\xi\le3/64$, the proof establishes
$$
\boxed{
|\mathfrak r_e|\le\frac{256}{9}\xi^2,
\qquad
\|\mathcal A\mathfrak r_e\|_\infty
\le\frac{128\kappa}{3}\xi^2,
}
$$
together with an explicit bound on the complete derivative energy of $\mathfrak r_e$.

This controls the difference between the actual vacuum derivative and the displayed local term uniformly over the exterior box. It is the remainder estimate used to return the exact local calculations to the interacting vacuum.

## 3. The coefficients $1,5,103/4$ were calculated from the original neighboring faces

The elementary square has twelve neighboring plaquettes other than itself. Their union with the square uses exactly 32 original links.

For a neighboring plaquette $p$, sharing edge $e$, define
$$
j_p=\sum_\alpha(X_{e,\alpha}W_p)(X_{e,\alpha}F).
$$
The original Pauli identities split $j_p$ into two explicitly constructed components. Their Haar squared norms are
$$
\frac9{64},\qquad \frac3{64},
$$
their cross term is zero, and their original electric Casimir energies are
$$
\frac92\kappa,\qquad \frac{13}{2}\kappa.
$$

The proof obtains these facts by writing the shared path product and the two remaining path products explicitly, applying the Pauli trace identity, and integrating the original Haar variables. Every cross-face pairing has an unmatched exterior link whose integral is zero; the checker constructs those link witnesses.

After retaining the forcing factor $2\kappa\xi/3$ and all twelve neighbors, the exact first local term gives
$$
1,\qquad 5,\qquad \frac{103}{4}
$$
for the three moment coefficients.

Its response is
$$
M_{\mathrm{local}}(s)
=
\kappa^2\xi^2
\left[
\frac{3/4}{s+9\kappa/2}
+
\frac{1/4}{s+13\kappa/2}
\right].
$$
At $s=\kappa$, this gives $28\kappa\xi^2/165$. The actual response differs by the certified remainder stated above.

The same calculation was completed for every square of side $b\ge2$, with original perimeter $\ell=4b$. Its coefficients are
$$
\boxed{
c_0=\frac{\ell+2}{3},\qquad
c_1=\frac{\ell(3\ell+14)}{12},\qquad
c_2=\frac{9\ell^3+66\ell^2+76\ell+104}{48}.
}
$$
The proof supplies explicit finite bounds
$$
|N_j-\kappa^{j+2}\xi^2c_j|
\le\kappa^{j+2}\xi^2\epsilon_j(\ell,\xi),
$$
retaining the loop-size dependence. It also supplies all-coupling upper bounds for the three moments.

The return to the actual vacuum uses the proved local-density comparison
$$
e^{-32\pi d\xi}\le\rho_S\le e^{32\pi d\xi},
$$
for a specified $d$-link support $S$, and the separately derived conditional-fiber comparison. For the elementary square, the two error factors are
$$
e^{1024\pi\xi}-1,
\qquad
e^{1088\pi\xi}-1.
$$
They are retained in the finite error formulas and evaluated with outward rational bounds.

## 4. There is also an all-coupling inverse estimate on the actual derivative source

Let $G_{v,\alpha}$ be the original vertex-gauge generators, and $d_v\le6$ the vertex degree. Their original link coefficients give
$$
\sum_\alpha|G_{v,\alpha}h|^2
\le d_v\sum_{e\ni v,\alpha}|X_{e,\alpha}h|^2.
$$

On the spin-one gauge sector $\mathcal E_v$,
$$
-\sum_\alpha G_{v,\alpha}^2h=2h.
$$
Gauge invariance of the actual vacuum permits integration in $\rho\,dU$, yielding
$$
\mathcal A|_{\mathcal E_v}\ge\frac{2\kappa}{d_v}\ge\frac{\kappa}{3},
$$
and hence
$$
\boxed{
\|(\mathcal A|_{\mathcal E_v}+s)^{-1}\|
\le\frac1{s+\kappa/3},\qquad s\ge0.
}
$$

The vacuum derivatives are actual members of this source:
$$
G_{s(e),\alpha}b_{e,\beta}
=-\epsilon_{\alpha\beta\gamma}b_{e,\gamma}.
$$
The estimate is therefore applied to the forcing equation above and to its remainder.

On the retained running path
$$
c_n=g_0^{-2}+\beta n\log2,\qquad
a_n=a_0\,2^{-n},\qquad g_n^2=c_n^{-1},
$$
it gives
$$
\boxed{
\sup_v\|(\mathcal A_n|_{\mathcal E_v})^{-1}\|
\le\frac{3a_0c_n}{2^{n+1}}\longrightarrow0.
}
$$

The map into the physical forcing is the original contraction
$$
(b_e,X_eF)\longmapsto
\sum_\alpha b_{e,\alpha}X_{e,\alpha}F.
$$
Both factors transform by the same adjoint matrix, so the contraction is gauge invariant. Its energy is carried through the complete product identity
$$
\mathcal A(bc)
=(\mathcal Ab)c+b(\mathcal Ac)
-2\kappa\sum_i(X_ib)(X_ic).
$$
Those last terms remain in the moment estimates. The source inverse estimate and the physical contraction are thus related by an explicit map and its complete energy defect.

## 5. Split Zero now controls an actual response error, including the section correction

For the calculated local trial $Y\in\mathcal K$, retain
$$
R=W-(D+\kappa)Y.
$$
The response identity is
$$
M(\kappa)
=
2\operatorname{Re}\langle W,Y\rangle
-q_{\mathcal A+\kappa}(Y)
+\langle R,(D+\kappa)^{-1}R\rangle.
$$

The final proof audit caught an important point: the chosen trial requires a correction to reach the canonical minimum section. I computed that correction explicitly.

Put
$$
a_Y=q_{\mathcal A+\kappa}(Y),\qquad
c_Y=\langle Y,W\rangle,\qquad
\alpha_Y=c_Y/a_Y.
$$
The proof establishes $a_Y>0$. In the actual complex
$$
\operatorname{span}\{Y\}
\xrightarrow{D+\kappa}\mathcal K
\xrightarrow0 0,
$$
the canonical representative is
$$
R_{\mathrm{can}}
=W-(D+\kappa)(\alpha_YY).
$$

In the original resolvent pairing,
$$
\boxed{
\begin{aligned}
\|[W]\|_{\mathcal K/(D+\kappa)\operatorname{span}\{Y\}}^2
&=M(\kappa)-\frac{|c_Y|^2}{a_Y},\\
R&=R_{\mathrm{can}}+(\alpha_Y-1)(D+\kappa)Y,\\
\langle R,(D+\kappa)^{-1}R\rangle
&=\|[W]\|^2+a_Y|\alpha_Y-1|^2.
\end{aligned}}
$$

The final term retains the exact primitive $(\alpha_Y-1)Y$ and its energy. Both nonnegative terms receive the proved residual bound. This is the quantitative cohomological calculation underlying the response certificate, with the full minimum-section correction retained.

### Return to the original physical state

Let
$$
h_\kappa=(D+\kappa)^{-1}W,
\qquad
\Phi=\psi\bigl(\mathsf J(F-\langle F\rangle_\rho)+h_\kappa\bigr).
$$
This is a nonzero physical form-domain vector perpendicular to the actual vacuum. Its original norm and energy are exactly
$$
\|\Phi\|^2=G+\|h_\kappa\|_\rho^2,
$$
$$
q_{H-E_0}(\Phi,\Phi)
=K_0-M(\kappa)-\kappa\|h_\kappa\|_\rho^2.
$$
Both mixed energy entries are included in this equality.

The verified intervals give
$$
\boxed{
(3-5\cdot10^{-13})\kappa
<
\frac{q_{H-E_0}(\Phi,\Phi)}{\|\Phi\|^2}
<
(3+5\cdot10^{-13})\kappa.
}
$$
The inclusion of $\operatorname{span}\{\Phi\}$ into the full centered physical form domain gives
$$
\Delta_L\le
\frac{q_{H-E_0}(\Phi,\Phi)}{\|\Phi\|^2}
$$
by the exact variational infimum. The lower endpoint displayed for this particular state is retained at that scope.

## Verification and workbench delivery

The final verifier passes **134 exact checks and 12 false-formula controls**, including the corrected section identity and the variational direction. Ordinary Python, optimized Python, fresh copied-source runs, and fresh patch application produced matching results. The unchanged parent checker also passed against its original receipt. The executable checks cover the quaternion identities, Haar integrals, original graph counts, and rational evaluation of the error bounds; the analytical arguments are supplied as written proofs for independent review.

[Complete verification record](sandbox:/mnt/data/yang_mills_actual_loop_moments_verification.json)

The patch adds the proof, verifier, receipt, execution record, and mathematical checkpoint, and updates `CURRENT.md` against the verified PR6 head `e98b2c3af77f66fb1c1396143ca53daef586404f`. PR6 remains open at that revision.  No new remote PR was opened: this session’s exposed GitHub actions provide reads and searches but no write action. The attached package includes the tested patch and its proposed PR description.

**The completed advance is actual interacting-vacuum moment and response control, together with all-coupling control of the derivative source.** The physical zero-shift response and a uniform positive continuum mass lower bound remain unevaluated. The narrow certificate stays on its specified large-$g$ domain; the all-coupling estimates retain the full growth factors along the existing continuum path.


# Historical final response 8: Uniform gap and zero-shift response

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/08_uniform_gap_zero_shift_20260915.md}

\textbf{SHA-256:} \path{6ed53e9bd4caea40d505c8c105cef17fe980f81c30b8466480a9f2daa7aa9737}

\textbf{Editorial provenance notice:} The complete final response is preserved for historical mathematical coverage. The standalone mathematical source chapters remain separately identifiable above.
\end{quote}

**The calculation now gives a positive lower bound for the full physical SU(2) spectrum, uniformly in the box size, on the explicit range $g^2\ge15$.** I used that bound to complete the actual **zero-shift Wilson-loop response**, and then proved convergence to a **unique spatial infinite-volume vacuum and dynamics at fixed lattice spacing**.

[Complete mathematical proof](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift_note.md) · [Full sources, checker, and execution records](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift.zip) · [Tested workbench patch](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift.patch)

The lattice spacing and physical coupling remain explicit throughout. The smooth four-dimensional continuum limit is still outside the completed result.

## 1. A lower bound on the entire physical form domain

Retain the original operator
$$
H_L=\kappa K_L+v\sum_{p\in\mathsf P_L}(2-W_p),
\qquad
\kappa=\frac{2g^2}{a},\quad
v=\frac1{2g^2a},\quad
\xi=\frac{v}{\kappa}=\frac1{4g^4}.
$$
Here $K_L=-\sum_{e,\alpha}X_{e,\alpha}^2$, and every $W_p$ is the complete original oriented plaquette trace. Let $\psi_L$ be the actual positive unit vacuum, $\rho_L=\psi_L^2$, and
$$
\mathcal A_L=\psi_L^{-1}(H_L-E_{0,L})\psi_L.
$$

Define
$$
r_\xi=\frac3{16}\left(1-\sqrt{1-\frac{2500}{3}\xi}\right),
\qquad
q_\xi=\frac{65536}{9375}r_\xi,
$$
$$
d_\xi=\frac34(1-q_\xi)e^{-32\pi\xi}.
$$

For **every $L\ge2$, every $a>0$, and every $g^2\ge15$**, the proof establishes
$$
\boxed{
q_{\mathcal A_L}(f)
\ge
\kappa d_\xi
\left(
\int\rho_L|f|^2\,dU
-
\left|\int\rho_Lf\,dU\right|^2
\right)
}
$$
on the complete original scalar form domain. Restricting this inequality to the physical invariant subspace gives
$$
\boxed{\Delta_L\ge\kappa d_\xi>0.}
$$

Two convenient explicit consequences are
$$
\boxed{
\Delta_L\ge\frac{\kappa}{100}
=\frac{g^2}{50a},
\qquad g^2\ge15,
}
$$
and
$$
\boxed{
\Delta_L\ge\frac{3\kappa}{20}
=\frac{3g^2}{10a},
\qquad g\ge4.
}
$$

The constants contain **no exterior-volume factor**. The inequality covers every centered physical state, including states and observable labels that change with the regulator. The complete strongest argument is [H1-H23 in the gap proof](sandbox:/mnt/data/yang_mills_full_physical_gap.md).

### How the stronger bound was obtained

The first improvement came from calculating the original plaquette’s Fourier coefficient exactly. In the original four-link tensor coordinates,
$$
W_p(U)=\operatorname{Tr}\!\left[
A\,(U_1\otimes U_2\otimes U_3\otimes U_4)
\right],
$$
where all sixteen trace-index contributions, including inverse-link signs, remain in $A$.

Its matrix satisfies
$$
(A^*A)^2=4A^*A,\qquad \operatorname{Tr}(A^*A)=16.
$$
Consequently,
$$
|A|=\frac12A^*A,
\qquad
\boxed{\|A\|_1=8.}
$$

I then used the same coefficient families with the auxiliary support estimate
$$
\|f\|_{\mathrm{loc}}
=
\sup_e
\sum_{S\ni e}
\left(\frac54\right)^{|S|}
\sum_{\mathbf j\ne0}
c(\mathbf j)\,\|A_{S,\mathbf j}\|_1,
$$
where
$$
c(\mathbf j)=\sum_e j_e(j_e+1).
$$
The label $S$ is retained even when a product’s active Fourier support becomes smaller.

The actual logarithmic-vacuum equation gives the source and nonlinear bounds
$$
\|f^{(1)}\|_{\mathrm{loc}}\le\frac{625}{8}\xi,
\qquad
\|\mathcal B(f,h)\|_{\mathrm{loc}}
\le\frac83\|f\|_{\mathrm{loc}}\|h\|_{\mathrm{loc}},
$$
with
$$
\mathcal B(f,h)=K_L^{-1}Q_H\sum_{e,\alpha}
(X_{e,\alpha}f)(X_{e,\alpha}h).
$$
The Haar-constant terms removed by $Q_H$ are separately recorded and returned to $E_{0,L}$.

The complete support series converges on the stated domain. Its summed coefficient bound is exactly $r_\xi$. The reconstructed function is identified with the **actual** vacuum through
$$
\psi_L=e^{v_L+c_L},
\qquad
c_L=-\frac12\log\int e^{2v_L}\,dU,
$$
and the original eigen-equation and ground-state form identity. Its scalar coordinate and original Haar mass remain present.

The final improvement uses the actual single-link conditional expectations
$$
(\mathsf P_e f)(U_{e^c})
=
\frac{\int \rho_L(U_e,U_{e^c})f(U_e,U_{e^c})\,dU_e}
{\int \rho_L(U_e,U_{e^c})\,dU_e}.
$$
The convergent support series bounds their complete influence matrix by $q_\xi<1$. A bounded-operator spectral calculation then proves
$$
(1-q_\xi)\operatorname{Var}_{\rho_L}(f)
\le
\sum_e\|f-\mathsf P_e f\|_{\rho_L}^2.
$$

The original pointwise vacuum-derivative estimate supplies the second comparison:
$$
\sum_e\|f-\mathsf P_e f\|_{\rho_L}^2
\le
\frac{4e^{32\pi\xi}}{3\kappa}\,
q_{\mathcal A_L}(f).
$$
Combining these two inequalities gives the full physical gap above, with the original $\kappa$ and the single-link Casimir factor $3/4$ retained.

The general Fourier-algebra and conditional-comparison methods have established antecedents. The new proof supplies their explicit coefficient, support, domain, and energy return for this original Hamiltonian. 

## 2. The actual zero-shift response is now enclosed

For the elementary square at the origin, retain its ordered holonomy $\Omega$, the trace $F=\operatorname{tr}\Omega$, and conditional expectation $\mathsf E_C$ onto $\Omega$ in the actual vacuum measure. Put
$$
Q_C=I-\mathsf J_C\mathsf E_C,\qquad
\mathcal K_C=\ker\mathsf E_C,
$$
and let $D$ be the operator represented by the original energy form restricted to $\mathcal K_C$.

Every vector in this kernel has zero vacuum mean. The full-domain estimate therefore proves
$$
\boxed{
D\ge\kappa d_\xi I,
\qquad
\|D^{-1}\|\le\frac1{\kappa d_\xi}.
}
$$
This includes the complete conditional kernel, with its exterior degrees of freedom.

For the original forcing
$$
W=-Q_C\mathcal A_LF,
$$
the zero-shift response is
$$
M_0=\langle W,D^{-1}W\rangle_{\rho_L}.
$$

At the actual coupling
$$
\xi=10^{-8},\qquad g^2=5000,\qquad \kappa=\frac{10000}{a},
$$
the new certificate proves, for every exterior box,
$$
\boxed{
\left|M_0-\frac8{39}\kappa\xi^2\right|
<
0.0000094\,\kappa\xi^2,
}
$$
and
$$
\boxed{
\left|
\|D^{-1}W\|_{\rho_L}^2-\frac{196}{4563}\xi^2
\right|
<
0.00000319\,\xi^2.
}
$$

The centers are calculated from the original twelve neighboring plaquettes. Their two retained components have electric energies $9\kappa/2$ and $13\kappa/2$, giving
$$
\frac{3/4}{9/2}+\frac{1/4}{13/2}=\frac8{39},
$$
$$
\frac{3/4}{(9/2)^2}+\frac{1/4}{(13/2)^2}
=\frac{196}{4563}.
$$
The full analytic remainder returns these local Haar calculations to the actual interacting-vacuum pairing.

The same calculation now supplies a two-sided enclosure for the **full physical gap**:
$$
\boxed{
0.74999514999\,\kappa
\le
\Delta_L
<
\left(3+\frac5{10^{13}}\right)\kappa.
}
$$
The lower bound is the full-domain estimate. The upper bound follows from the explicit inclusion of the restored physical trial state into the complete centered form domain.

### The retained cohomology has a quantified zero-shift primitive

For the actual trial $Y\in\mathcal K_C$, retain
$$
R=W-DY,
\qquad
a_Y=q_D(Y)>0,
\qquad
c_Y=\langle Y,W\rangle_{\rho_L},
\qquad
\alpha_Y=\frac{c_Y}{a_Y}.
$$
The canonical representative is
$$
R_{\mathrm{can}}=W-D(\alpha_YY).
$$

In the original pairing $\langle r,D^{-1}t\rangle_{\rho_L}$,
$$
\boxed{
\|[W]\|_{\mathcal K_C/D\operatorname{span}\{Y\}}^2
=
M_0-\frac{|c_Y|^2}{a_Y},
}
$$
and
$$
\boxed{
\langle R,D^{-1}R\rangle_{\rho_L}
=
\|[W]\|^2+a_Y|\alpha_Y-1|^2.
}
$$
The second term retains the actual boundary primitive $(\alpha_Y-1)Y$. The calculated bound on their complete nonnegative sum is
$$
\boxed{
\|[W]\|^2+a_Y|\alpha_Y-1|^2
<
0.0000000000142\,\kappa\xi^2.
}
$$

There is also a full-domain primitive factorization. On the original smooth physical source, define
$$
d_Xf=(X_if)_i,
\qquad
d_Bf=(f-\mathsf P_ef)_e,
$$
$$
T(d_Xf)=d_Bf,\qquad
p_B(d_Bf)=f-\langle f\rangle_{\rho_L}.
$$
The inverse of $T$ on its actual image is $z\mapsto d_Xp_Bz$, and
$$
\boxed{p_X=p_BT.}
$$
With the derivative range carrying its original energy pairing,
$$
\boxed{
\|p_X\|^2=\frac1{\Delta_L}
\le
\frac1{\kappa d_\xi}.
}
$$
Thus the support construction is now connected to a bounded primitive for the complete physical energy problem.

## 3. The spatial-volume limit is unique, including its dynamics

The support calculation gives more than a uniform estimate: each labelled coefficient is **exactly the same in every box containing its original support**. Its convergent series therefore defines a fixed summable interaction family.

I used those coefficients to prove convergence of the entire sequence of finite-box vacuum measures to a unique measure $\nu$. The proof retains the original conditional densities and the complete influence matrix; it does not choose a subsequence and then assign uniqueness to it.

The same coefficients control the original drift $b_e^L=X_e\log\psi_L$. Their full mixed derivative matrix has a summable row bound, which permits a direct comparison of the finite-volume ground-relative dynamics. With common original link Brownian motions, the pathwise comparison retains every matrix power:
$$
z_e(t)
\le
\sum_{r\ge0}
\frac{(2\kappa t)^{r+1}}{(r+1)!}
\left(B^r\bigl(t(L)+t(M)\bigr)\right)_e.
$$
Here $B$ is the actual drift-derivative majorant and $t_e(L)$ the actual omitted-support drift error. The row bound, pointwise vanishing of $t_e(L)$, and factorial tail prove convergence of the dynamics on every finite set of original links.

This gives a unique limiting semigroup and a self-adjoint generator on the constructed vacuum space, with
$$
\boxed{
A_\infty\big|_{1^\perp}\ge\kappa d_\xi.
}
$$

It also proves convergence of **all local time-ordered vacuum correlations**:
$$
\begin{aligned}
&\langle\psi_L,
O_0e^{-t_1(H_L-E_{0,L})}O_1
\cdots
e^{-t_m(H_L-E_{0,L})}O_m\psi_L\rangle\\
&\qquad\longrightarrow
\int O_0T(t_1)\!\left(O_1T(t_2)(\cdots O_m)\right)\,d\nu .
\end{aligned}
$$
Every observable, time interval, and ground-energy subtraction in this expression is retained.

The map from the correlation construction to the physical Hilbert space is explicit:
$$
\boxed{
[O,t]\longmapsto T(t)(O-\nu O).
}
$$
Its pairing is exactly the limiting correlation kernel. The time-zero physical cylinder functions are dense, giving the full unitary rather than an identification based on a finite loop frame.

### The limiting theory is quantitatively nonzero

For the original elementary-loop observable,
$$
\operatorname{Var}_{\nu}(F)\ge e^{-128\pi\xi},
\qquad
q_\infty(F-\nu F)\le4\kappa.
$$
Its limiting correlation consequently obeys
$$
\boxed{
e^{-128\pi\xi}-4\kappa t
\le C_F(t)
\le C_F(0)e^{-\kappa d_\xi t}.
}
$$
The lower bound is positive on an explicitly nonempty time interval.

At fixed $a,g$ in this domain, the first-moment estimate prevents spectral mass from escaping to infinite energy, while the full gap excludes a zero-energy atom in the centered sector. Both endpoint terms from the earlier reconstruction are therefore controlled in this spatial-volume limit.

The complete argument is in the [unique-volume-limit proof, V1-V25](sandbox:/mnt/data/yang_mills_unique_volume_limit.md), with its final coupling constants returned in H23.

### The extensive vacuum energy is retained too

The original finite-volume energy satisfies
$$
\boxed{
\begin{aligned}
\left|
E_{0,L}
-\kappa|\mathsf P_L|
\left(2\xi-\frac{\xi^2}{3}\right)
\right|
\le\kappa\left[
\frac{2048}{27}|\mathsf P_L|\xi^3
+
\frac{65536}{81}|\mathsf E_L|\xi^4
\right].
\end{aligned}}
$$
The energy per plaquette has a unique limit, with that finite remainder. The scalar contribution $2v|\mathsf P_L|$ has remained in the calculation throughout.

## 4. Exact relation to the continuum objective

This completes spatial infinite-volume control on the stated strong-coupling domain, with $a>0$ fixed.

The earlier simultaneous path remains
$$
a_n=a_02^{-n},\qquad
g_n^2=\frac1{g_0^{-2}+\beta n\log2}.
$$
Writing $c_n=g_0^{-2}+\beta n\log2$, the new theorem applies exactly on
$$
\boxed{c_n\le\frac1{15}.}
$$
For $\beta>0$, that is only a finite initial portion of the path.

The other limit order is now explicit too. At any fixed admissible $g$,
$$
\Delta_n\ge\frac{2g^2d_\xi}{a_n}\longrightarrow\infty
\qquad(a_n\to0).
$$
Bounded centered positive-time correlations then tend to zero, and retained zero-time spectral mass moves to the energy-infinity endpoint. This calculation stays attached to its fixed-$g$ path.

**A nontrivial smooth four-dimensional continuum field and a positive finite continuum mass have not been established here.** The completed result supplies a full physical lower bound, a quantified zero-shift primitive, and unique spatial vacuum/dynamics limits from which to continue the original coupling-dependent analysis.

## Verification and delivery

The final checker passed **273 named exact checks and 35 false-formula controls**. The complete replay records ordinary and optimized execution, the unchanged predecessor in both modes, copied-source execution, and restoration after deliberate corruption. All **18 additional command-line corruption cases** failed at their intended named errors.

Both the combined and incremental patches were applied independently to fresh selected source trees. Their complete target bytes matched, and their ordinary/optimized verification outputs reproduced the final receipt.

[Verification record](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift_verification.json) · [Complete execution record](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift_execution.json) · [Incremental patch after the previous delivery](sandbox:/mnt/data/yang_mills_uniform_gap_zero_shift_incremental.patch)

The analytical arguments are supplied as complete written proofs. The executable checks their stated finite algebra, original coordinate identities, and rational endpoints; no independent analytical review, Lean certificate, sampled vacuum, or spin-cutoff approximation is claimed.

The combined patch targets the exact PR6 revision `e98b2c3af77f66fb1c1396143ca53daef586404f`, includes the previously unpublished actual-loop-moment contribution, and updates the active mathematical checkpoint. **No new remote PR or merge was performed.** The package contains the proposed PR description, complete sources, and a single-command replay.


# Historical final response 9: Gauge-native second source and band

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/09_gauge_native_second_source_band_20260915.md}

\textbf{SHA-256:} \path{ef5fc894d8d582a64138dbb796ba54c0b554f2dfd7172ec64bbafe577e92b504}

\textbf{Editorial provenance notice:} The complete final response is preserved for historical mathematical coverage. The standalone mathematical source chapters remain separately identifiable above.
\end{quote}

**I audited the source-to-spectrum argument and extended its proved coupling range from $g^2\ge15$ to**
$$
\boxed{
g^2\ge\sqrt{\frac{32+\sqrt{354}}3}
=4.1156161030\ldots .
}
$$
The new estimate applies to the **entire original physical SU(2) spectrum**, uniformly in the open-box size. I also calculated the complete first excitation band, bounded every higher-order contribution, and obtained a certified interval for the actual first excitation of the original $L=2$ box.

[Complete proofs, sources, and verification package](sandbox:/mnt/data/yang_mills_gauge_native_continuation.zip) · [Strongest coupling-domain proof](sandbox:/mnt/data/yang_mills_second_source_continuation.md) · [Cumulative workbench patch](sandbox:/mnt/data/yang_mills_gauge_native_continuation.patch)

## 1. The stronger full physical gap

Keep the original Hamiltonian
$$
H_L=\kappa K_L+\kappa\xi\sum_{p\in\mathsf P_L}(2-W_p),
\qquad
K_L=-\sum_{e,\alpha}X_{e,\alpha}^{\,2},
$$
with
$$
\kappa=\frac{2g^2}{a},
\qquad
\xi=\frac1{4g^4}.
$$
Every original link, oriented plaquette word, Haar factor, and scalar contribution $2\kappa\xi|\mathsf P_L|$ remains present.

Define
$$
P_2(\xi)=1-\frac{256}{3}\xi+\frac{10720}{9}\xi^2,
\qquad
\alpha_*=\frac3{4(32+\sqrt{354})}.
$$

For every $L\ge2$, every $a>0$, and every $0<\xi\le\alpha_*$, the new proof gives
$$
\boxed{
\Delta_L\ge
\frac{3\kappa}{2}\bigl(1+\sqrt{P_2(\xi)}\bigr).
}
$$
Equivalently, in the original physical parameters,
$$
\boxed{
\Delta_L\ge
\frac{3g^2}{a}
\left(
1+\sqrt{1-\frac{64}{3g^4}+\frac{670}{9g^8}}
\right).
}
$$

This covers the closed endpoint. There the lower bound is $3\kappa/2$.

For a convenient rational benchmark,
$$
g^2\ge\frac{17}{4}
\quad\Longrightarrow\quad
\boxed{
\Delta_L\ge
\frac{3\kappa}{2}
\left(1+\sqrt{\frac{35401}{751689}}\right)
>1.8255\,\kappa.
}
$$

The proof reaches the complete physical form domain through the actual compact spectral resolution. It therefore covers volume-dependent physical states as well as fixed local observables. The full argument is in [R10-R14](sandbox:/mnt/data/yang_mills_second_source_continuation.md), using the source and domain constructions in [G1-G31](sandbox:/mnt/data/yang_mills_gauge_native_source_note.md).

### The gauge constraint supplies a sharper constant

For an original product-representation label $\mathbf j=(j_e)$, write
$$
c(\mathbf j)=\sum_ej_e(j_e+1).
$$
Every nonzero physical Fourier block satisfies
$$
\boxed{c(\mathbf j)\ge6j_e\qquad\text{for every edge }e.}
$$

The proof uses the actual vertex intertwiners. At either endpoint of $e$, their highest-weight constraint gives
$$
j_e\le\sum_{\substack{f\ni v\\f\ne e}}j_f.
$$
Let $J_1$ be the total spin on the other edges meeting the two endpoints. Then $J_1\ge2j_e$. Applying the same constraint at their outer endpoints gives $J_1\le2J_2$, where $J_2$ is the total spin on the next edge set. The original cubic graph is triangle-free, so these counts give
$$
\sum_fj_f\ge j_e+J_1+J_2\ge4j_e.
$$
Finally,
$$
j(j+1)\ge\frac32j
$$
for each nonzero half-integer spin, proving the stated constant.

It is attained by an elementary fundamental plaquette. The same original support calculation gives
$$
\operatorname{spec}(K_L|_{\mathrm{phys}})
\subset\{0,3\}\cup[9/2,\infty),
$$
and
$$
\ker(K_L-3)=\operatorname{span}\{W_p:p\in\mathsf P_L\},
\qquad
\langle W_p,W_q\rangle_H=\delta_{pq}.
$$

These statements sharpen the actual source estimate and the return to physical energy.

## 2. I evaluated the second vacuum source before estimating the remaining series

Write the actual logarithmic vacuum in its retained coefficient expansion,
$$
\log\psi_L=c_L+\sum_{n\ge1}\xi^n v_{[n]},
\qquad
v_{[1]}=\frac13\sum_pW_p.
$$
The scalar $c_L$ remains fixed by the original vacuum mass.

The complete second coefficient is
$$
\boxed{
v_{[2]}
=
-\frac1{72}\sum_p\chi_1(\Omega_p)
+
\sum_{\{p,q\}:p\sim q}
\left[
\frac1{27}P_0(W_pW_q)
-\frac1{117}P_1(W_pW_q)
\right].
}
$$
Here $p\sim q$ means the original plaquettes share an edge. The maps $P_0,P_1$ are the actual spin-zero and spin-one projections on that shared edge.

The calculation retains the original intermediate energies:
$$
8,\qquad \frac92,\qquad \frac{13}{2}.
$$
For distinct plaquettes without a shared edge, the product has Casimir $6$, and its second-source coefficient is exactly zero. Its original union label remains recorded.

The source norm uses the original Fourier coefficient matrices:
$$
\|v\|_{\mathrm{loc}}
=
\max_e
\sum_{S\ni e}\sum_{\mathbf j\ne0}
c(\mathbf j)\|A_{S,\mathbf j}\|_1.
$$
This is an auxiliary absolute-convergence estimate on the retained coefficients. The physical state and energy pairings remain the original ones.

The complete coefficient calculation gives
$$
\boxed{\|v_{[2]}\|_{\mathrm{loc}}\le236.}
$$
The earlier bound obtained by estimating the bilinear recurrence before evaluating its inputs was $2048/3$.

The improvement has explicit local ingredients. The original spin-one plaquette coefficient has trace norm $27$. For an adjacent pair, the spin-zero coefficient has norm at most $16$, and the sum of both channel norms is at most $64$. An original edge belongs to at most $42$ unordered adjacent pairs. Thus the entire anchored contribution is bounded by
$$
4\cdot3+42\cdot\frac{16}{3}=236.
$$

### The evaluated source extends convergence

For the same original coefficients, the gauge constraint proves
$$
\|\mathcal B(f,h)\|_{\mathrm{loc}}
\le\frac23\|f\|_{\mathrm{loc}}\|h\|_{\mathrm{loc}},
$$
where
$$
\mathcal B(f,h)
=
K_L^{-1}Q_H\sum_{e,\alpha}
(X_{e,\alpha}f)(X_{e,\alpha}h).
$$
Each product retains its original union support; each removed scalar returns to the ground energy.

Set
$$
a_1=32,\qquad a_2=236,\qquad
a_n=\frac23\sum_{i=1}^{n-1}a_i a_{n-i}\quad(n\ge3).
$$
The full coefficient series is bounded by
$$
r_2(\xi)=\sum_{n\ge1}a_n\xi^n
=\frac34\left(1-\sqrt{P_2(\xi)}\right).
$$

There is an explicit tail bound, including at $\xi=\alpha_*$:
$$
\boxed{
\sum_{n>N}a_n\xi^n
\le
\frac34
\left(\frac{\xi}{\alpha_*}\right)^{N+1}
(1+\gamma^{N+1})
\frac{\binom{2N}{N}}{4^N}
\le
\frac34
\left(\frac{\xi}{\alpha_*}\right)^{N+1}
\frac{1+\gamma^{N+1}}{\sqrt{N+1}},
}
$$
where
$$
\gamma=\frac{32-\sqrt{354}}{32+\sqrt{354}}\in(0,1).
$$

At the endpoint, $r_2(\alpha_*)=3/4$. Absolute convergence supplies the endpoint directly.

Summing the original source equation gives
$$
K_Lv=\xi\sum_pW_p+\sum_i(X_iv)^2-C_L,
\qquad
C_L=\int_H\sum_i(X_iv)^2.
$$
Consequently,
$$
\psi_L=e^{v+c_L},
\qquad
E_{0,L}=2\kappa\xi|\mathsf P_L|-\kappa C_L.
$$
The positive eigenfunction and the full ground-state form identity identify this summed solution with the actual vacuum. [The complete second-source proof](sandbox:/mnt/data/yang_mills_second_source_continuation.md) includes every coefficient, channel, support count, and endpoint estimate.

## 3. The complete first physical excitation band is now calculated

The free first physical band contains one original plaquette state per face. I calculated its full second-order matrix, including boundary faces and coupling between different plaquettes.

Let $d_p$ be the actual number of plaquettes sharing an edge with $p$, and let $A_{\mathrm{adj}}$ be that adjacency matrix. The coefficient is
$$
\boxed{
T_L=\frac7{15}I-\frac1{21}(D_{\deg}+A_{\mathrm{adj}}).
}
$$
Thus
$$
(T_L)_{pp}=\frac7{15}-\frac{d_p}{21},
$$
$$
(T_L)_{pq}=
\begin{cases}
-1/21,&p\sim q,\\
0,&p\ne q,\ p\not\sim q.
\end{cases}
$$

The calculation starts from the complete expression
$$
T_L=
\frac{|\mathsf P_L|}{3}I
-
P S Q_3(K_L-3)^{-1}Q_3SP,
\qquad S=\sum_pW_p.
$$
The inverse includes $-1/3$ on the original constant state. The extensive term $|\mathsf P_L|/3$ comes from the actual ground-energy coefficient. All scalar and intermediate-sector contributions are written before their cancellation.

### Every higher order has a uniform bound

The actual band matrix in its specified original coefficient frame satisfies
$$
\boxed{
A_{\mathrm{band}}(\xi)
=
3\kappa I+\kappa\xi^2T_L+\mathcal R_L(\xi),
}
$$
with
$$
\boxed{
\|\mathcal R_L(\xi)\|_1
\le
\kappa\frac{6713}{39875}
\frac{(320|\xi|)^3}{1-320|\xi|},
\qquad |\xi|<\frac1{320}.
}
$$

This bounds the complete higher-order tail of the full Hamiltonian. The proof constructs the actual analytic spectral projection and its inverse coefficient map. No finite spin cutoff enters the operator.

The raw physical band Gram is retained through
$$
\mathcal R_\xi x
=
\psi_L\left(U_\xi x-\langle U_\xi x\rangle_{\rho_L}\right),
\qquad
G_\xi=\mathcal R_\xi^*\mathcal R_\xi,
$$
and
$$
(H_L-E_{0,L})\mathcal R_\xi
=
\mathcal R_\xi A_{\mathrm{band}},
\qquad
G_\xi A_{\mathrm{band}}
=
A_{\mathrm{band}}^*G_\xi.
$$

The full band and its analytic remainder are proved in [B1-B32](sandbox:/mnt/data/yang_mills_physical_excitation_band.md).

### A sharper full-spectrum lower bound at the earlier test coupling

Since every $d_p\le12$,
$$
\lambda_{\min}(T_L)\ge-\frac{71}{105}.
$$
The spectral isolation and all-order estimate therefore give
$$
\boxed{
\Delta_L\ge
\kappa\left[
3-\frac{71}{105}\xi^2
-\frac{6713}{39875}
\frac{(320\xi)^3}{1-320\xi}
\right],
\qquad 0<\xi<\frac1{320}.
}
$$

At
$$
\xi=10^{-8},\qquad g^2=5000,\qquad \kappa=\frac{10000}{a},
$$
this proves, for every original box,
$$
\boxed{
\Delta_L>\kappa\left(3-7.314\times10^{-17}\right).
}
$$

This improves the earlier lower bound near $0.75\kappa$ to a bound near the actual physical free-band energy $3\kappa$, with an explicit interaction correction and remainder.

### A certified actual first excitation for $L=2$

The original $L=2$ box has $240$ plaquettes. I constructed its complete integer matrix
$$
Q=D_{\deg}+A_{\mathrm{adj}}.
$$

An exact positive-vector certificate and an independent fraction-free inertia calculation give
$$
21.86319640514
<
\lambda_{\max}(Q)
<
21.86319641826,
$$
hence
$$
-0.57443792469
<
\lambda_{\min}(T_{L=2})
<
-0.57443792405.
$$

The inertia certificate also separates this coefficient from the other $239$ directions. Combining that separation with the full analytic remainder proves
$$
\boxed{
\kappa(3-0.5833\,\xi^2)
<
\Delta_{L=2}
<
\kappa(3-0.5656\,\xi^2),
\qquad \xi=10^{-10}.
}
$$
Here the original physical parameters are
$$
g^2=50000,\qquad \kappa=\frac{100000}{a}.
$$

The [complete box certificate](sandbox:/mnt/data/yang_mills_L2_band_certificate.json) retains the original face ordering, all degrees, the integer vector $Q^{100}\mathbf1$, every pivot determinant, and all **2,303,960 exact divisions**.

## 4. The interaction matrix also gives explicit spatial propagation

On the infinite cubic face array, the complete second-order coefficient has a three-by-three Fourier symbol, one coordinate for each plaquette orientation. With the original plaquette-center phases retained,
$$
Q(k)=12I+A(k),
$$
$$
A_{aa}(k)=2\cos k_b+2\cos k_c,
\qquad
A_{ab}(k)=4\cos(k_a/2)\cos(k_b/2)\quad(a\ne b).
$$
Its lowest coefficient near $k=0$ is
$$
\boxed{
t_{\mathrm{low}}(k)
=
-\frac{71}{105}+\frac4{63}|k|^2+O(|k|^4).
}
$$

Returning through the physical coordinate map $k=ap$, the displayed second-order energy terms are
$$
\frac{6g^2}{a}-\frac{71}{840g^6a},
\qquad
\frac{a}{126g^6}|p|^2.
$$
Their scope is the calculated second-order band coefficient; the complete finite-box energy has the separately stated analytic remainder.

I also checked the planar coefficient against Dahmen’s original strong-coupling calculation. The explicit parameter map is
$$
g_D=2^{3/4}g,\qquad h_D=\xi,
$$
$$
H_{\mathrm{plane}}(a,g)
=
\frac{\sqrt2}{a}H'_D+2\kappa\xi M I.
$$
It reproduces the planar coefficient
$$
T_{\mathrm{plane}}=\frac{29}{105}I-\frac1{21}A_{\mathbb Z^2},
$$
including its $3/35$ zero-momentum value. The three-dimensional restriction retains the additional diagonal term $-8I/21$ and its coupling to perpendicular plaquettes. This supplies an external check of the local channel arithmetic with all parameter factors present. ([arXiv](https://arxiv.org/pdf/hep-lat/9412080))

## 5. Unique spatial-volume dynamics now reach the same closed endpoint

The previous volume argument used a conditional-influence restriction. I derived a direct bound on the actual finite-volume dynamics that covers the full new source domain.

Let $T_L(t)=e^{-t\mathcal A_L}$, and define
$$
\epsilon_2(\xi)=\frac12\left(1-\sqrt{P_2(\xi)}\right).
$$
For every original physical cylinder polynomial $F$,
$$
\boxed{
\|T_L(t)F-\langle F\rangle_{\rho_L}\|_\infty
\le
\frac{\|Q_HF\|_{X_0}}{1-\epsilon_2(\xi)}
e^{-3\kappa(1-\epsilon_2(\xi))t}.
}
$$
Here $X_0$ is the sum of the trace norms of the original nonconstant Fourier coefficients. For an elementary plaquette trace, its initial value is exactly $8$.

The proof applies the coefficient estimate to the **actual** smooth finite-volume evolution. It retains and integrates the equation for its original Haar-constant component, recovering the actual vacuum mean. The prefactor has no exterior-volume dependence.

This gives convergence of the entire sequence of original finite-box vacuum measures and dynamics, together with all local time-ordered correlations. Uniform mixing proves uniqueness of the invariant probability of the constructed limiting semigroup.

### The endpoint is controlled by an explicit coupling modulus

At fixed $\kappa$, for $0\le\xi\le\eta\le\alpha_*$,
$$
\boxed{
\sup_{t\ge0}
\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
\le
\frac{\epsilon_2(\eta)-\epsilon_2(\xi)}
{1-\epsilon_2(\xi)}
\|Q_HF\|_{X_0}.
}
$$
The physical parameter map and inverse are
$$
\kappa=\frac{2g^2}{a},\quad \xi=\frac1{4g^4},
\qquad
g^2=\frac1{2\sqrt\xi},\quad
a=\frac1{\kappa\sqrt\xi}.
$$
The proof also treats changes in both $\kappa$ and $\xi$, retaining the original physical time.

At $\eta=\alpha_*$, the ratio in the bound becomes
$$
\frac{\sqrt{P_2(\xi)}}{1+\sqrt{P_2(\xi)}}\longrightarrow0.
$$
Inserting an interior coupling between two endpoint finite boxes proves convergence at the closed endpoint. This avoids assigning a finite value to the derivative majorant that diverges there.

The resulting physical infinite-volume generator satisfies
$$
\boxed{
A_\infty|_{1^\perp}
\ge
\frac{3\kappa}{2}\left(1+\sqrt{P_2(\xi)}\right),
\qquad 0<\xi\le\alpha_*.
}
$$
The full construction, original drift comparison, mean restoration, and endpoint passage are in the [spatial-return proof](sandbox:/mnt/data/yang_mills_spatial_coupling_return.md), with the final enlarged constants returned in R13-R16.

## 6. Return to the original primitive and the continuum program

On centered physical functions, retain
$$
d_Xf=(X_if)_i,
\qquad
p_X(d_Xf)=f,
$$
with the original derivative energy pairing
$$
\|d_Xf\|_1^2
=
\kappa\int\rho_L\sum_i|X_if|^2.
$$
The new full-spectrum estimate gives
$$
\boxed{
\|p_X\|^2
=
\frac1{\Delta_L}
\le
\frac{2}
{3\kappa(1+\sqrt{P_2(\xi)})}.
}
$$

The gauge quotient, support-assembly relations, and their inverse maps are retained in the source proof. The actual loop forcing and its canonical residual belong to the physical conditional kernel. Its inclusion $I$ satisfies
$$
DI=ID_{\mathrm{phys}},
\qquad
(D+s)^{-1}I=I(D_{\mathrm{phys}}+s)^{-1}.
$$
Consequently, the earlier zero-shift response and Split Zero quotient-residual estimates receive this stronger inverse bound on their actual source. Their raw metric and minimum-section correction remain unchanged.

For the standing simultaneous path
$$
a_n=a_02^{-n},\qquad
g_n^2=\frac1{c_n},\qquad
c_n=g_0^{-2}+\beta n\log2,
$$
the newly proved domain is exactly
$$
\boxed{
c_n^2\le\frac3{32+\sqrt{354}}.
}
$$
For $\beta>0$, that path eventually leaves the domain. A nontrivial four-dimensional continuum field and a finite positive continuum mass remain unestablished.

The next selected calculation is now the **actual connected third vacuum coefficient and the full linearized residual at**
$$
\xi v_{[1]}+\xi^2v_{[2]}.
$$
The second coefficient, its bound $236$, the enlarged endpoint, and the physical spectral return are completed inputs to that calculation.

## Verification and delivery

The final checker passed **642 uniquely named exact checks and 27 false-formula controls**. The complete replay includes the unchanged predecessor, ordinary and optimized Python, fresh copied sources, and **20 command-line corruption executions**, each rejected at its intended named error.

Both delivery patches were independently applied to fresh selected source trees. Every target byte matched, and all four post-application ordinary/optimized runs reproduced the original receipt.

[Verification record](sandbox:/mnt/data/yang_mills_gauge_native_verification.json) · [Complete execution record](sandbox:/mnt/data/yang_mills_gauge_native_execution.json) · [Patch-restoration checks](sandbox:/mnt/data/yang_mills_gauge_native_patch_validation.json) · [Incremental patch](sandbox:/mnt/data/yang_mills_gauge_native_continuation_incremental.patch)

The analytical arguments are written in full in the four proof files. The executable verifies the stated original-coordinate algebra, graph counts, coefficient matrices, exact divisions, and rational endpoints; no new independent analytical review or Lean certification is claimed.

The cumulative patch targets the confirmed PR6 head `e98b2c3af77f66fb1c1396143ca53daef586404f`, preserves the previous delivered proofs and receipts, and updates the active mathematical checkpoint. PR6 remains open and unmerged; no new remote PR or merge was performed.

---

**Sources:**

- [master.dvi](https://arxiv.org/pdf/hep-lat/9412080)


# Historical final response 10: Gauge-resolved programme

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/10_gauge_resolved_prose_20260915.md}

\textbf{SHA-256:} \path{1a49b0b4a1df4e5b23f0ff43328594ce26f5cb53eb6069fd0f2186559729c58f}

\textbf{Editorial provenance notice:} The linked standalone mathematical attachment has not been recovered. This chapter preserves the complete mathematical final response only; it is not a recovery of the missing attachment.
\end{quote}

**The revised argument gives a stronger physical gap on a substantially larger coupling range, and the same inverse now controls the entire spatial-volume limit-including the endpoint.**

The new bound, for every original open box $L\ge2$ and every $a>0$, is
$$
\boxed{
\Delta_L\ge
\frac{3g^2}{a}
\left(1+\sqrt{1-\frac{64}{3g^4}}\right),
\qquad
g^2\ge\frac8{\sqrt3}.
}
$$

This extends the previous domain $g^2\ge15$ to $g^2\ge8/\sqrt3$. The improvement comes from the original gauge constraints on the Fourier coefficients. It applies to the complete physical form domain.

[Physical-gap proof](sandbox:/mnt/data/yang_mills_gauge_resolved_gap.md) · [Spatial-volume and resolvent proof](sandbox:/mnt/data/yang_mills_gauge_volume_resolvent.md) · [Complete research package](sandbox:/mnt/data/yang_mills_gauge_resolved_gap.zip)

## 1. The decisive improvement is in the actual gauge projection

Keep the original operator and parameters:
$$
H_L=\kappa K_L+\kappa\xi\sum_p(2-W_p),
\qquad
\kappa=\frac{2g^2}{a},
\qquad
\xi=\frac1{4g^4},
$$
$$
K_L=-\sum_{e,\alpha}X_{e,\alpha}^2.
$$
Every original link, oriented plaquette word, and vertex gauge transformation-including boundary vertices-remains.

For a full Fourier representation label $\mathbf j=(j_e)_e$, its original electric eigenvalue is
$$
c(\mathbf j)=\sum_ej_e(j_e+1).
$$

A nonzero physical Fourier coefficient contains an invariant tensor at every vertex. At an edge $e$ incident on $v$, this forces
$$
j_e\le\sum_{\substack{f\ni v\\f\ne e}}j_f.
$$
The reason is explicit: the invariant tensor gives an intertwiner from the dual spin-$j_e$ representation into the tensor product of the other incident representations, whose maximum weight is their summed spin.

Now fix $e=\{v,w\}$. Let $A_e$ be the other edges incident on $v$ or $w$. The two endpoint inequalities give
$$
\sum_{f\in A_e}j_f\ge2j_e.
$$
The original cubic graph has no triangles. The remote endpoints of those edges are consequently distinct. Applying the same invariant-tensor inequality at those endpoints gives
$$
\sum_{f\notin A_e\cup\{e\}}j_f
\ge\frac12\sum_{f\in A_e}j_f.
$$
The factor $1/2$ retains the fact that an exterior edge can be counted at most twice.

Therefore
$$
\sum_fj_f\ge4j_e.
$$
Since $j(j+1)\ge3j/2$ for the original half-integer spins,
$$
\boxed{
c(\mathbf j)\ge6j_e,
\qquad
\frac{j_e}{c(\mathbf j)}\le\frac16.
}
$$

Every nontrivial physical coefficient thus has $c(\mathbf j)\ge3$, attained by the original four-edge plaquette with spin $1/2$ on each edge.

That inequality improves both the actual vacuum series and the operator acting on the excitation source. The proof and checker retain an active-bridge example; they also retain the triangle and unprojected single-link examples that prevent extending the bound beyond its stated graph and gauge domains.

## 2. The endpoint vacuum series and the physical inverse are now controlled separately

Write the actual positive vacuum as
$$
\psi_L=e^{v_L+c_L},
\qquad
c_L=-\frac12\log\int e^{2v_L}\,dU.
$$
The scalar energy is retained through
$$
E_{0,L}
=
2\kappa\xi|\mathsf P_L|
-\kappa\int\sum_i(X_iv_L)^2\,dU.
$$

On the same support-labelled Fourier coefficients used in the preceding calculation, the new gauge inequality improves the quadratic estimate to
$$
\|\mathcal B(f,h)\|_0
\le\frac23\|f\|_0\|h\|_0.
$$
The original plaquette coefficient has trace norm $8$, so the actual first source is bounded by $32\xi$.

Set
$$
\theta=\frac{256}{3}\xi,
\qquad
r=\frac34\left(1-\sqrt{1-\theta}\right).
$$
The complete vacuum series converges for
$$
0<\xi\le\frac3{256},
$$
including the closed endpoint. At that endpoint, its exact omitted-order bound is
$$
\boxed{
\sum_{p>P}n_p
=
\frac34\,\frac{\binom{2P}{P}}{4^P}
\le\frac{3}{4\sqrt{P+1}}.
}
$$

The nonlinear difference estimate reaches one there. I have kept that value. Convergence at the endpoint is proved by this explicit summable Catalan series.

For the excitation operator, put
$$
u_L=\log\psi_L,
\qquad
\mathcal A_L
=\psi_L^{-1}(H_L-E_{0,L})\psi_L
=\kappa(K_L-\mathscr D_u),
$$
$$
\mathscr D_uf
=
2\sum_{e,\alpha}(X_{e,\alpha}u_L)X_{e,\alpha}f.
$$
The gauge-resolved coefficient bound gives
$$
\boxed{
\|\mathscr D_uh\|_{\mathcal A}
\le\chi\|K_Lh\|_{\mathcal A},
\qquad
\chi=\frac{2r}{3}
=\frac{1-\sqrt{1-\theta}}2
\le\frac12.
}
$$
Here $\|\cdot\|_{\mathcal A}$ is the explicitly specified trace-coefficient norm. The physical state pairing remains $\int\rho_L\overline f h\,dU$.

For an actual positive-energy physical eigenfunction, subtract its Haar scalar to obtain $h$. Its original eigen-equation becomes
$$
(K_L-\epsilon)h=Q_H\mathscr D_uh,
\qquad \epsilon=\lambda/\kappa.
$$
On the physical Fourier coefficients, for $0<\epsilon<3$,
$$
\|(K_L-\epsilon)h\|_{\mathcal A}
\ge
\left(1-\frac{\epsilon}{3}\right)
\|K_Lh\|_{\mathcal A}.
$$
Consequently $\epsilon\ge3(1-\chi)$. The complete physical spectral resolution returns this estimate to the original form domain:
$$
\boxed{
q_{\mathcal A_L}(f)
\ge
\kappa d_{\mathrm p}\operatorname{Var}_{\rho_L}(f),
\qquad
d_{\mathrm p}
=
\frac32\left(1+\sqrt{1-\theta}\right).
}
$$

The scalar-space constant is separately
$$
d_{\mathrm s}=\frac{d_{\mathrm p}}4.
$$

At the endpoint, the physical lower bound is $3\kappa/2$. A convenient interior consequence is
$$
\boxed{
\Delta_L\ge2\kappa=\frac{4g^2}{a},
\qquad g^2\ge5.
}
$$

## 3. Split Zero now carries a bounded inverse back to the original physical source

On the zero-Haar-mean coefficient space, define
$$
T=Q_H\mathscr D_uK_L^{-1},
\qquad
p=P_H\mathscr D_uK_L^{-1}.
$$
The complete bound includes the scalar output:
$$
|py|+\|Ty\|_{\mathcal A}
\le\chi\|y\|_{\mathcal A}.
$$
Thus
$$
S=(I-T)^{-1}=\sum_{m\ge0}T^m
$$
exists on the closed coupling domain.

For an original smooth physical observable $F$, put $q=Q_HF$. The inverse gives both the primitive and the actual vacuum expectation:
$$
\boxed{
h_F=K_L^{-1}Sq,
\qquad
\langle F\rangle_{\rho_L}
=
P_HF+pSq.
}
$$
Indeed,
$$
\mathcal A_Lh_F
=
\kappa\bigl(F-P_HF-pSq\bigr),
$$
and integration in the actual vacuum proves the scalar-return identity. The physical inverse is therefore
$$
\boxed{
\mathcal A_L^{-1}
\bigl(F-\langle F\rangle_{\rho_L}\bigr)
=
\kappa^{-1}
\bigl(h_F-\langle h_F\rangle_{\rho_L}\bigr).
}
$$

The proof checks its original operator-domain membership through coefficient convergence and the actual elliptic equation.

For the finite admitted source
$$
V_N=\operatorname{span}\{q,Tq,\ldots,T^Nq\},
$$
use the actual complexes
$$
V_N\xrightarrow{I-T}\mathcal A_0\xrightarrow0 0.
$$
The primitive
$$
y_N=\sum_{m=0}^NT^mq
$$
has the exact retained residual
$$
q-(I-T)y_N=T^{N+1}q.
$$
The transported-class kernel is computed by
$$
V_{N+1}/V_N
\longrightarrow
\ker\!\left(
\mathcal A_0/(I-T)V_N
\to
\mathcal A_0/(I-T)V_{N+1}
\right),
\quad
[v]\longmapsto[(I-T)v],
$$
with inverse supplied by $S$.

Its chain map to the physical equation retains $\kappa$:
$$
J_0y
=
\kappa^{-1}
\left(K_L^{-1}y-\langle K_L^{-1}y\rangle_{\rho_L}\right),
\qquad
J_1z=z-\langle z\rangle_{\rho_L},
$$
$$
\boxed{\mathcal A_LJ_0=J_1(I-T).}
$$

The resulting state error is
$$
\boxed{
\left\|
\mathcal A_L^{-1}(F-\langle F\rangle_{\rho_L})-J_0y_N
\right\|_{\rho_L}
\le
\frac{\chi^{N+1}\|Q_HF\|_{\mathcal A}}{\kappa d_{\mathrm p}}.
}
$$
The corresponding energy-error bound has denominator $\sqrt{\kappa d_{\mathrm p}}$.

This is a quantitative primitive on the original physical source, with its support transitions, scalar return, and residual retained.

## 4. The spatial-volume construction now reaches the same closed endpoint

Every support-labelled vacuum coefficient is exactly identical in every box containing its original support. The summable coefficient bounds therefore give an infinite local drift and strong convergence of the source operators $T_L,p_L$.

The scalar-return formula above proves convergence of the **entire** sequence of actual vacuum measures:
$$
\nu_L\longrightarrow\nu.
$$
Positivity and unit mass pass from the actual finite vacua. The construction makes no assumption of an infinite density relative to product Haar measure.

The positive-shift inverse also retains its scalar term. With
$$
\sigma=s/\kappa,\quad
k_\sigma=(K+\sigma)^{-1},
$$
$$
T_\sigma=Q_H\mathscr D_uk_\sigma,
\quad
p_\sigma=P_H\mathscr D_uk_\sigma,
\quad
X_\sigma=(I-T_\sigma)^{-1}Q_HF,
$$
the exact returned resolvent is
$$
\boxed{
R_sF
=
\kappa^{-1}k_\sigma X_\sigma
+
\frac{P_HF+p_\sigma X_\sigma}{s}\,1.
}
$$

This provides full-sequence convergence of the original dynamics at the endpoint as well. For the finite ground-relative semigroup $T_L(t)$, the proof derives the uniform approximation
$$
\boxed{
\left\|
T_L(t)F-
\left[\frac mtR_{m/t}^{\,L}\right]^mF
\right\|_\infty
\le
\frac{t\,\kappa(1+\chi)\|KF\|_{\mathcal A}}{\sqrt m}.
}
$$
It comes from the exact mean and variance of the original exponential-time resolvent averages. Convergence of the resolvents then determines the limiting semigroup.

The completed argument establishes the original cylinder core, the unique stationary and conditional vacuum measure, and the full physical Hilbert-space realization. Its generator satisfies
$$
\boxed{
A_\infty\big|_{1^\perp}\ge\kappa d_{\mathrm p}
}
$$
at fixed $a>0$. All bounded local time-ordered vacuum correlations converge through the original ground-state transform.

### Explicit control of the omitted spatial supports

For $\theta<1$, let $R$ be the distance from an observable’s original link support to the exterior of the box, measured in the original edge adjacency graph. Then
$$
\boxed{
|\nu_L(F)-\nu(F)|
\le
\theta^{R/3}\|Q_HF\|_{\mathcal A}.
}
$$
For the original plaquette at $g^2=5$, this gives
$$
R\ge192:
\quad
|\nu_L(W_p)-\nu(W_p)|
\le8(64/75)^{64}<0.000313.
$$

At the closed endpoint, the separate source and inverse truncations give
$$
\boxed{
|\nu_L(F)-\nu(F)|
\le
\left[
4\frac{\binom{2P}{P}}{4^P}+2^{1-M}
\right]\|Q_HF\|_{\mathcal A}
}
$$
once the box contains the radius-$3PM$ neighbourhood of the original support. Both terms tend to zero under the displayed truncations.

The limiting physical space is quantitatively nonzero. For the original elementary plaquette $F$,
$$
\operatorname{Var}_\nu(F)\ge e^{-16r/3}\ge e^{-4},
\qquad
q_\infty(F-\nu F)\le4\kappa.
$$
Its correlation therefore obeys
$$
\boxed{
e^{-16r/3}-4\kappa t
\le C_F(t)
\le C_F(0)e^{-\kappa d_{\mathrm p}t}.
}
$$

## 5. Return to the actual zero-shift response

The conditional kernel retains its scalar bound. Its gauge-invariant part is a reducing subspace, with the explicit inclusion $I$ satisfying
$$
DI=ID_{\mathrm{phys}},
\qquad
D^{-1}I=ID_{\mathrm{phys}}^{-1},
\qquad
D_{\mathrm{phys}}\ge\kappa d_{\mathrm p}.
$$
The original loop forcing, trial, and residual belong to this physical part.

Using that map, the unchanged local calculations at
$$
\xi=10^{-8},\qquad g^2=5000,\qquad\kappa=10000/a
$$
now give
$$
\boxed{
\left|
\langle W,D^{-1}W\rangle_{\rho_L}
-\frac8{39}\kappa\xi^2
\right|
<
0.00000931\,\kappa\xi^2,
}
$$
$$
\boxed{
\left|
\|D^{-1}W\|_{\rho_L}^2
-\frac{196}{4563}\xi^2
\right|
<
0.00000184\,\xi^2.
}
$$
The complete canonical cohomology-class error plus the retained minimum-section correction is less than
$$
0.00000000000355\,\kappa\xi^2.
$$

Combining the new full-domain lower estimate with the preceding explicit physical trial gives
$$
\boxed{
2.99999935999\,\kappa
\le\Delta_L
<
\left(3+\frac5{10^{13}}\right)\kappa
}
$$
at that coupling, uniformly in the exterior box.

## Scope, verification, and workbench delivery

The original simultaneous path remains
$$
a_n=a_02^{-n},
\qquad
g_n^2=\frac1{c_n},
\qquad
c_n=g_0^{-2}+\beta n\log2.
$$
The enlarged proved domain is exactly
$$
\boxed{c_n\le\frac{\sqrt3}{8}.}
$$
For $\beta>0$, the path eventually leaves that domain.

Every path that stays in the proved domain while $a_n\to0$ obeys
$$
\Delta_n\ge\frac{8\sqrt3}{a_n}\longrightarrow\infty.
$$
The original plaquette retains a positive zero-time norm while its bounded positive-time correlations vanish. The proof follows that norm to the energy-infinity atom of the compactified spectral measure. **A nontrivial four-dimensional ultraviolet field and a finite positive continuum mass remain unestablished.**

The new verifier completed **360 named exact checks and 17 false-formula controls**. The replay includes ordinary and optimized execution, the unchanged predecessor, fresh copied sources, and **16 named command-line corruption rejections**. Both patches were applied to fresh selected source trees and their verification outputs reproduced.

[Verification record](sandbox:/mnt/data/yang_mills_gauge_verification.json) · [Execution record](sandbox:/mnt/data/yang_mills_gauge_execution.json) · [Patch-validation record](sandbox:/mnt/data/yang_mills_gauge_patch_validation.json)

These executable checks cover the finite representation identities, original graph constraints, scalar-return equations, and rational bounds. The analytical arguments are complete written proofs supplied for review; independent external review and Lean verification have not been performed.

[Combined patch against PR6](sandbox:/mnt/data/yang_mills_gauge_resolved_gap.patch) · [Incremental patch after the previous delivery](sandbox:/mnt/data/yang_mills_gauge_resolved_incremental.patch)

The active checkpoint now records the enlarged domain, the full physical inverse, and the coupling-response calculation at its endpoint. No new remote PR or merge was performed; the available GitHub actions remain read-only.


# Historical final response 11: Cubic source and linearized return

\begin{quote}\footnotesize
\textbf{Source classification:} historical transcript-derived mathematical final response

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/transcript-mathematics/11_cubic_linearized_20260916.md}

\textbf{SHA-256:} \path{843823e303253843d0c5fbee28d50500e1d24d73c3b1cdef80729640d8577470}

\textbf{Editorial provenance notice:} The complete final response is preserved for historical mathematical coverage. The standalone mathematical source chapters remain separately identifiable above.
\end{quote}

**Both calculations are complete: the connected cubic vacuum source and the full linearized residual around the first two source coefficients.** Together they extend the proved coupling range from the saved bound $g^2\ge4.115616\ldots$ to
$$
\boxed{g^2\ge3.825973052393386,}
$$
with a lower bound for the **entire physical spectrum**, uniform in the original open-box size.

I published the complete proofs and checkers in **draft PR #8**, “Evaluate cubic vacuum source and full linearized Yang-Mills gap return,” at commit `91434b6962062bd80439d4cb2cae9d2479264dde`. It is stacked on PR #6; nothing has been merged. 

[Complete research package](sandbox:/mnt/data/yang_mills_cubic_linearized.zip) · [Cubic-source proof](sandbox:/mnt/data/yang_mills_cubic_source.md) · [Linearized-return proof](sandbox:/mnt/data/yang_mills_linearized_return.md)

## 1. The resulting physical lower bound

Retain the original Hamiltonian
$$
H_L=\kappa K_L+\kappa\xi(2M-S),
\qquad
S=\sum_{p\in\mathsf P_L}W_p,
$$
$$
K_L=-\sum_{e,\alpha}X_{e,\alpha}^{\,2},
\qquad
\kappa=\frac{2g^2}{a},
\qquad
\xi=\frac1{4g^4}.
$$
Here $M=|\mathsf P_L|$, and every $W_p$ is the original oriented four-link trace. The additive energy $2\kappa\xi M$ remains in $H_L$.

Define the explicit polynomial
$$
\mathscr D(x)=
\frac{
46457856x^4+183150656x^3+18324072x^2-1168128x+13689
}{13689}.
$$
Let $\alpha$ be its first positive root. Exact rational calculations give
$$
0.0170787544707772675
<
\alpha
<
0.0170787544707772677.
$$

For every original box $L\ge2$, every $a>0$, and every $0<\xi\le\alpha$, the new proof establishes
$$
\boxed{
\Delta_L\ge
\kappa\left[
\frac32\left(1+\sqrt{\mathscr D(\xi)}\right)
+\frac{1136}{13}\xi^2
\right].
}
$$
The exact coupling threshold is $g^2\ge1/(2\sqrt\alpha)$; its value lies strictly between
$$
3.825973052393385
\quad\text{and}\quad
3.825973052393386.
$$

At the closed endpoint, the coefficient of $\kappa$ is greater than $61/40$. A convenient interior consequence is
$$
\boxed{
g^2\ge4
\quad\Longrightarrow\quad
\Delta_L>1.8385\,\kappa
=3.677\,\frac{g^2}{a}.
}
$$

This result improves the **coupling domain** of the saved second-source argument. The preceding sharper small-$\xi$ excitation-band estimates retain their own scope; I have not replaced them by this bound. The complete spectral return is in equations L20-L28 of the [linearized proof](sandbox:/mnt/data/yang_mills_linearized_return.md).

## 2. First calculation: every connected cubic source term

Write the logarithmic vacuum in the original source coordinates:
$$
\psi_L=e^{v+c_L},
\qquad
c_L=-\frac12\log\int e^{2v}\,dU.
$$
With
$$
\Gamma(f,h)=\sum_{e,\alpha}(X_{e,\alpha}f)(X_{e,\alpha}h),
\qquad
B(f,h)=K_L^{-1}Q_H\Gamma(f,h),
$$
where $Q_H$ removes the original Haar constant, the exact equation is
$$
v=\xi v_1+B(v,v),
\qquad
v_1=\frac13\sum_pW_p.
$$
Every removed scalar is retained in the original ground energy
$$
E_{0,L}=2\kappa\xi M-\kappa\int\Gamma(v,v)\,dU.
$$

The complete second coefficient remains
$$
v_2=
-\frac1{72}\sum_p\chi_1(\Omega_p)
+
\sum_{\{p,q\}:p\sim q}
\left[
\frac1{27}P_0(W_pW_q)
-\frac1{117}P_1(W_pW_q)
\right].
$$
Here $p\sim q$ means the original plaquettes share an edge, and $P_0,P_1$ project its two fundamental factors onto their spin-zero and spin-one components.

I evaluated
$$
v_3=2B(v_1,v_2)
$$
on **all five connected configurations**, including repeated faces.

### Complete coefficient table

For the three-distinct-face configurations, the projected function is $W_pW_qW_r$. For the repeated configuration, it is $(W_p^2-1)W_q$.

| Original configuration | Retained spin component | Original total Casimir | Coefficient in $v_3$ |
|---|---|---:|---:|
| One face repeated three times | $\chi_{1/2}=W_p$ | $3$ | $-1/81$ |
| Same | $\chi_{3/2}$ | $15$ | $1/810$ |
| Repeated adjacent pair $\{p,p,q\}$ | Shared-edge spin $1/2$ | $9$ | $-11/4212$ |
| Same | Shared-edge spin $3/2$ | $12$ | $11/11232$ |
| Three-face path | $n=0,1,2$ spin-one shared edges | $6+2n$ | $1/162,\,-11/8424,\,1/3510$ |
| Three faces sharing one edge | Total shared spin $1/2,3/2$ | $15/2,\,21/2$ | $-2/1755,\,2/2457$ |
| Three faces at a cube corner | $n=0,1,2,3$ spin-one shared edges | $9/2+2n$ | $2/81,\,34/13689,\,-38/17901,\,2/2457$ |

These projectors have explicit formulas in the original edge Casimirs:
$$
P_{e,j}
=
\prod_{\ell\in J_e,\ \ell\ne j}
\frac{E_e-\ell(\ell+1)I}{j(j+1)-\ell(\ell+1)}.
$$
The finite list $J_e$ is the actual allowed tensor-product spin list. All multiplicities remain, including the two copies of total spin $1/2$ for three fundamentals.

Three exact cancellations are important.

For the repeated adjacent pair,
$$
P_{1/2}\!\left[(W_p^2-1)W_q\right]
=
\frac43W_pP_0(W_pW_q)-\frac13W_q.
$$
The two lower-$W_q$ contributions to $Kv_3$ are $1/72$ and $-1/72$, so they cancel at their original seven-link support.

For the common-edge triple, the original eight-dimensional tensor space gives
$$
P_0^{(12)}+P_0^{(13)}+P_0^{(23)}
=
\frac32P_{\mathrm{total}\,1/2}.
$$
This retains the full multiplicity. The calculation uses the sum of those projectors, with their complete matrix products recorded.

For the cube corner, the $n=1$ projected function is exactly zero: its central vertex would carry one spin-one edge and two spin-zero edges, and the original invariant tensor space there has dimension zero. Its coefficient and original support label remain recorded. The all-spin-zero component is
$$
P_{000}(W_pW_qW_r)=\frac14W_{\partial(p,q,r)},
$$
with the original six-link boundary word.

The product identity
$$
2\Gamma(f,h)=(c_f+c_h)fh-K(fh)
$$
and these explicit recouplings prove every entry in the table. Disconnected triples contribute zero because their differentiated factors have no common original edge. Equations C13-C20 of the [cubic proof](sandbox:/mnt/data/yang_mills_cubic_source.md) give the complete calculation.

### The evaluated coefficient improves the quantitative bound

Using the original Casimir-weighted trace-coefficient norm, the per-configuration bounds and the numbers meeting an original anchor edge are
$$
\begin{array}{c|ccccc}
&\text{self}&\text{repeated}&\text{path}&\text{common edge}&\text{corner}\\
\hline
\text{bound}&40/27&66/13&1408/351&512/117&3504/351\\
\text{count}&4&84&460&40&24.
\end{array}
$$
Thus
$$
\boxed{
\|v_3\|_{\mathrm{loc}}
\le
\frac{944984}{351}
<2693.
}
$$
The previous estimate obtained before evaluating this coefficient was
$$
\frac{30208}{3}=10069\frac13.
$$

The improvement comes from the actual channel coefficients, shared-edge integrations, gauge constraints, and original geometry. The physical state and energy pairings remain unchanged.

## 3. Second calculation: the complete linearized residual and its infinite tail

Set
$$
q_2=\xi v_1+\xi^2v_2.
$$
The residual is exactly
$$
\boxed{
R_2=\xi v_1+B(q_2,q_2)-q_2
=\xi^3v_3+\xi^4B(v_2,v_2).
}
$$
The quartic term remains present. The proof supplies a finite original-coordinate formula for every one of its components, using the Casimir projectors above.

The derivative of the source equation at $q_2$ is
$$
\mathscr L_2=I-\mathscr J_2,
\qquad
\mathscr J_2h=2B(q_2,h).
$$

Evaluating the separate total-spin and single-edge-spin contributions of $v_2$ gives
$$
m(v_2)\le\frac{5834}{39},
\qquad
t(v_2)\le\frac{137}{6}.
$$
These improve the actual operator and residual estimates to
$$
\|\mathscr J_2\|
\le
\ell(\xi)
=
\frac{128}{3}\xi+\frac{3132}{13}\xi^2,
$$
$$
\|R_2\|_{\mathrm{loc}}
\le
\delta(\xi)
=
\frac{944984}{351}\xi^3
+\frac{799258}{39}\xi^4.
$$
Their discriminant is precisely
$$
\mathscr D(\xi)=(1-\ell(\xi))^2-\frac83\delta(\xi).
$$

Throughout $0<\xi\le\alpha$, the proof establishes $\ell(\xi)<1$. Hence the **actual** linearized inverse is
$$
\mathscr L_2^{-1}
=
\sum_{j=0}^{\infty}\mathscr J_2^j,
\qquad
\|\mathscr L_2^{-1}\|
\le\frac1{1-\ell(\xi)}.
$$

For the complete correction $w=v-q_2$,
$$
\mathscr L_2w=R_2+B(w,w).
$$
The full binary-tree expansion converges, including at the closed endpoint, and gives
$$
\boxed{
\|w\|_{\mathrm{loc}}
\le
w_*(\xi)
=
\frac34\left[1-\ell(\xi)-\sqrt{\mathscr D(\xi)}\right].
}
$$

There are explicit error bounds for both infinite operations. The linear inverse has the exact residual
$$
\mathscr L_2^{-1}R_2-\sum_{j=0}^{N}\mathscr J_2^jR_2
=
\mathscr J_2^{N+1}\mathscr L_2^{-1}R_2.
$$
For the nonlinear expansion, put
$$
\vartheta_*=\frac{8\delta}{3(1-\ell)^2}\le1.
$$
Its tail after $N$ tree orders is at most
$$
\boxed{
\frac34(1-\ell)\,
\vartheta_*^{N+1}
\frac{\binom{2N}{N}}{4^N}
\le
\frac34(1-\ell)\,
\frac{\vartheta_*^{N+1}}{\sqrt{N+1}}.
}
$$
That summable endpoint calculation supplies convergence even where the nonlinear contraction estimate reaches one.

### An explicit value inside the enlarged domain

At the original coupling $g^2=4$,
$$
\xi=\frac1{64},
\qquad
\kappa=\frac8a.
$$
The complete bounds are
$$
\|\mathscr L_2^{-1}\|
\le\frac{39936}{10963},
\qquad
\|\mathscr L_2^{-1}R_2\|_{\mathrm{loc}}
\le\frac{33836149}{808280064},
$$
$$
\boxed{
\|v-q_2\|_{\mathrm{loc}}<0.047293824576905,
}
$$
and
$$
\boxed{
\|v-q_2-\mathscr L_2^{-1}R_2\|_{\mathrm{loc}}<0.005432.
}
$$
These bounds include all further nonlinear terms.

## 4. Returning that correction to the physical spectrum

The returned operator is the original ground-state transform
$$
\mathcal A
=
\psi^{-1}(H-E_0)\psi
=
\kappa\bigl(K-2\Gamma(v,\cdot)\bigr).
$$

The evaluated spin contributions give
$$
t(v)\le
\frac{16}{3}\xi+\frac{137}{6}\xi^2+\frac{w_*}{6}.
$$
Consequently, on the original Fourier coefficients,
$$
\|2\Gamma(v,h)\|_X
\le
\chi(\xi)\|Kh\|_X,
$$
where
$$
\chi(\xi)
=
\frac12\left(1-\sqrt{\mathscr D(\xi)}\right)
-\frac{1136}{39}\xi^2.
$$

For an actual positive-energy physical eigenfunction, subtraction of its Haar scalar gives
$$
(K-\lambda/\kappa)h=Q_H\,2\Gamma(v,h).
$$
Every nonconstant physical Fourier component has $c(\mathbf j)\ge3$. The coefficient estimate therefore gives
$$
\lambda\ge3\kappa(1-\chi(\xi)).
$$
The complete compact physical spectral resolution returns this to the full form-domain inequality stated at the beginning.

The approximation’s full operator defect remains explicit:
$$
\boxed{
Q_H\mathcal Ah-\kappa K\mathscr L_2h
=
-2\kappa Q_H\Gamma(w,h).
}
$$
It has bound
$$
\frac{2\kappa}{3}w_*\|Kh\|_X.
$$
Thus the approximate source, its correction, and the actual physical operator are connected by an exact equation with a quantified remainder.

The corresponding Split Zero source windows are
$$
V_N\xrightarrow{\mathscr L_2}V\xrightarrow0 0,
\qquad
V_N=\operatorname{span}\{R_2,\mathscr J_2R_2,\ldots,\mathscr J_2^NR_2\}.
$$
Their transported kernel has the explicit isomorphism
$$
V_{N+1}/V_N
\longrightarrow
\ker\!\left(V/\mathscr L_2V_N\to V/\mathscr L_2V_{N+1}\right),
\qquad
[h]\longmapsto[\mathscr L_2h],
$$
with inverse supplied by $\mathscr L_2^{-1}$. The original residual, primitive, and support label all remain.

For the physical derivative primitive, with its original energy pairing,
$$
\boxed{
\|p_X\|^2=\frac1{\Delta_L}
\le
\frac1{\kappa d(\xi)},
\qquad
d(\xi)=3(1-\chi(\xi)).
}
$$

## 5. An additional completed calculation: the fourth vacuum-energy coefficient

The two source calculations also determine
$$
\boxed{
E_{0,L}
=
2\kappa M\xi-\frac{\kappa M}{3}\xi^2
+
\kappa\left(\frac{5M}{216}-\frac{2J}{1053}\right)\xi^4
+\mathcal E_{\ge6},
}
$$
where $J$ is the **actual number of unordered adjacent plaquette pairs**.

For the original box, writing $m=2L$,
$$
M=3m^2(m+1),
\qquad
J=6m(3m^2-1).
$$
At $L=2$, the fourth coefficient divided by $\kappa$ is
$$
\frac{1198}{351}.
$$

I checked this through an independent Rayleigh-Schrödinger coefficient calculation:
$$
\frac{E_{[4]}}{\kappa}
=
\frac{M^2}{27}
-
\frac19\left\langle Q_HS^2,K^{-1}Q_HS^2\right\rangle_H,
$$
$$
\left\langle Q_HS^2,K^{-1}Q_HS^2\right\rangle_H
=
\frac M8+\frac23\binom M2+\frac2{117}J.
$$
Substitution reproduces the same coefficient, including the boundary-dependent $J$.

The remaining orders have a complete bound:
$$
\boxed{
|\mathcal E_{\ge6}|
\le
\frac{49\kappa|\mathsf E_L|}{1200}
\frac{(60|\xi|)^6}{1-(60|\xi|)^2},
\qquad
0<|\xi|<\frac1{60}.
}
$$
Every extensive factor remains. This comes from the analytic source construction and the exact link-center involution that makes $E_0-2\kappa M\xi$ even.

## 6. What the literature comparison actually establishes

The exponential-vacuum equation, connected loop expansion, and linear excitation equation have established Hamiltonian lattice-gauge antecedents. Schütte, Zheng Weihong, and Hamer explicitly formulate these equations and their gauge-invariant loop/Casimir construction. Their work is credited in the proof. ([arXiv](https://arxiv.org/html/hep-lat/9603026v1))

The comparison retains the exact parameter and energy map:
$$
g_C=2^{3/4}g,
\qquad
\boxed{
H_{\mathrm{original}}(a,g)
=
\sqrt2\,H_C(a,2^{3/4}g)+2\kappa\xi M I.
}
$$
Their original commutator derivative is $iX$ in our generator coordinates, which returns their vacuum equation to the signs in $K v-\Gamma(v,v)-\xi S$. ([arXiv](https://arxiv.org/html/hep-lat/9603026v1))

The proof also compares Dahmen’s planar strong-coupling calculation and Hui-Fang-Shi’s higher-order vacuum construction using their respective parameter maps. The latter paper explicitly states its later finite-order and random-phase approximations; this contribution instead retains the complete residual and bounds the ensuing infinite correction. ([arXiv](https://arxiv.org/abs/hep-lat/9412080))

The planar-to-spatial comparison has its own exact original-link inclusion $J_\pi$:
$$
K_3J_\pi=J_\pi K_2,
$$
$$
\boxed{
H_3J_\pi-J_\pi H_2
=
\kappa\xi
\left[
2(M_3-M_2)-\sum_{p\text{ outside the plane}}W_p
\right]J_\pi.
}
$$
All perpendicular plaquettes remain in that defect.

**The specific contribution submitted here is the complete spatial cubic coefficient calculation, its evaluated source bounds, and the full linearized infinite-tail return to an explicit physical gap domain.** The literature reading establishes the displayed correspondences and antecedents. It does not establish a global priority claim or an independently confirmed best coupling threshold.

## Verification and present scope

The checker passed **2,246 named exact checks and 15 false-formula controls**. It evaluates all **612 anchored cubic multisets at two exact rational quaternion assignments**, comparing direct differentiation of the original link products with the separately constructed projected formulas.

The full replay includes the unchanged saved predecessor, ordinary and optimized Python, copied sources, intended corruption rejections, and restored sources. Fresh patch application reproduced every target file and the complete verification output. The publication source-identity check also caught and corrected a transcription error before the final commit. 

[Complete verification record](sandbox:/mnt/data/yang_mills_cubic_linearized_verification.json) · [Execution record](sandbox:/mnt/data/yang_mills_cubic_linearized_execution.json) · [Patch-validation record](sandbox:/mnt/data/yang_mills_cubic_patch_validation.json) · [Workbench patch](sandbox:/mnt/data/yang_mills_cubic_linearized.patch)

The analytical proofs are written in full and submitted for review. The finite tests verify their specified coordinate identities and numerical certificates; no new Lean formalization or independent external analytical review has been performed.

The standing continuum path remains
$$
a_n=a_02^{-n},
\qquad
g_n^2=\frac1{c_n},
\qquad
c_n=g_0^{-2}+\beta n\log2.
$$
Its exact inclusion in the enlarged domain is
$$
\boxed{c_n\le2\sqrt\alpha.}
$$
For $\beta>0$, it eventually leaves that domain. **A nontrivial four-dimensional continuum field and a finite positive continuum mass remain unestablished.**

The two requested calculations are now completed inputs in the workbench. The active checkpoint records the next original coefficient
$$
v_4=2B(v_1,v_3)+B(v_2,v_2),
$$
together with the signed action of the linearized operator on those same connected four-face supports.


\part{Independent bounded reviews}

# Bounded audit of the early and middle Yang–Mills continuations

\begin{quote}\footnotesize
\textbf{Source classification:} independent bounded mathematical audit

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/audits/early_mid.md}

\textbf{SHA-256:} \path{8c6737e4ebd6979216269d9512363976e91dbc745cbfb888f54631ace243b5e2}

\textbf{Editorial provenance notice:} This review has the exact scope stated in its body. Its inclusion is not exhaustive certification of all sources or a proof of the continuum mass-gap problem.
\end{quote}


Audit date: 16 September 2026. This is a read-only mathematical audit of the source notes listed below. No source note was edited, no Lean process was started, and no execution receipt was treated as a proof of an analytic assertion. The `mathbox:proof-audit` skill and its general logic, representation, computation, and source checklists were used. This report concerns the retained September 14–15 notes, not the strongest status of the later continuations.

## Claim card and primary verdict

**Primary verdict: proved as written for the bounded claim card in this paragraph.** For the original finite open SU(2) lattice Hamiltonian with positive spacing and coupling, smooth positive unit vacuum, original Haar measure, and derivative convention printed in the sources, the inspected conditional-expectation maps and energy identities, finite-source Schur response and residual identities, local vacuum-derivative and spin-one-sector estimates, and the stated comparison from bounded regulator-state sequences to the fixed-label reconstructed observable space have the displayed domains, signs, constants, and directions of inequality. The explicit elementary-loop Haar coefficients agree with the retained local representation decomposition. This verdict does not certify every numerical endpoint, every external analytic theorem, the geometric S6 filling theorem, any later continuation, or a four-dimensional continuum mass-gap theorem. These exclusions are specified below.

No new counterexample or concrete algebraic error was found in that bounded target. Two distinctions that would invalidate stronger conclusions are already explicitly corrected in the retained notes: escaping-label classes lie in the nonzero possible kernel `K/N`, and a chosen trial residual is not generally the canonical minimum-norm representative of its quotient class.

Objects and variance: inner products are conjugate-linear in their first entry; physical scalar functions are invariant under the original vertex gauge group; conditional score coordinates transform covariantly and are contracted using the original three generator coordinates. The finite source coefficient space has its original positive state Gram `G`, rather than an implicit identity Gram. The spectral construction uses a countable cylindrical observable family, a single common regulator subsequence, and positive times. Its target is `H_obs`, not an asserted complete four-dimensional Yang–Mills Hilbert space.

## Exact source scope

All five following research notes were read in full. Line locators in this report refer to these copied bytes, before any later source revision.

| Short name | Repository-relative source | Lines | SHA-256 |
|---|---|---:|---|
| SR | `yang-mills/continuations/20260914-spectral-reconstruction/RESEARCH_NOTE.md` | 324 | `5fffd882e97df0499263875d344f40935561106f0389077b2f832a7c3c568ba0` |
| VR | `yang-mills/continuations/20260914-vacuum-refinement-infrared/RESEARCH_NOTE.md` | 549 | `0874d0d59e0fecec8d5fcd88b33918515e635fe22c27b3bd56ae0b3c4cb782c0` |
| RC | `yang-mills/research-control/RESEARCH_NOTE.md` | 249 | `67454e30bc6a0a5f24ef2b63aac16ea05cd4b9fcc087688d351f7b0191a016ec` |
| CR | `yang-mills/continuations/20260914-coupled-response/RESEARCH_NOTE.md` | 218 | `b787a444d6c3995ac39fbc71a4f114478cad824172c40e33a32930661a771433` |
| AM | `yang-mills/continuations/20260915-actual-loop-moments/RESEARCH_NOTE.md` | 981 | `0ac4afbec39b2e878d5555af85a86803d9ba6ac5505dc7817f231e5533c0dd2b` |

Additional targeted source reads were the finite-box primary note, `yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`, lines 1–175, and the local S6 frozen companion, `s6/27_s6_key_advances_frozen_2026-09-06.tex`, especially lines 138–195. For the literal deck-action check, the local full-source export `private intake/S6_CURRENT_FULL_TEX_FOR_AI_20260906_SPECTRAL_UMBRAL_FINAL.md` was read at lines 112246–112274, 112423–112427, and 112625–112645. The finite-box weak-coupling asymptotics after the initial source region were not audited. No `.mathbox` ledger exists at this consolidation root.

## Dependency graph

1. Original compact-product SU(2) Hamiltonian, gauge action, and positive vacuum → multiplication by `psi` is unitary between the actual vacuum-weighted and Haar Hilbert spaces → exact ground-state Dirichlet form. The primary note lines 17–51 gives the initial domain and positivity argument; RC L1 and AM A2 retain the same constants.
2. Ordered edge-product map plus its explicit last-link inverse → Haar factorization → actual vacuum marginal `m`, pullback `J`, conditional expectation `E=J*`, and `EJ=I` → horizontal derivative identity with the score `S` → VR (3.11), RC L13–15, and exact minimum-energy sections RC L17–25.
3. Closed restriction of that original form to `ker E` → nonnegative self-adjoint `D` → raw-`G` block form CR C4–5 → Schur response CR C7–12 → exact residual square CR C16 → two-sided finite-source response/metric enclosures and the singular normal-equation fibres CR C20–22.
4. Actual logarithmic-vacuum equation AM A2 → differentiated equation A3 → pointwise bound A5 and integrated identity A6 → covariant inverse A9 on the explicitly typed spin-one sector → actual local remainder A13–14 → neighboring-plaquette Haar decomposition A28–33 → quantitative return to the actual weighted measure and conditional `D` in A34–45.
5. Uniform bounded-observable spectral estimates → common positive-time kernel subsequence → semigroup on the exact kernel quotient → `H_obs`, `A_obs`, and their matrix measure → spectral-support and Laplace-edge identities. Regulator-state sequences map onto this space through VR (6.1), and the exact source-kernel quotient is VR (6.3), not an injectivity inference from finite-level density.

The general spectral theorem, compact-manifold elliptic regularity/maximum principle, representation of closed nonnegative forms, Riesz representation, and polynomial approximation are standard analytic leaves invoked by the sources. Their applications were checked for the relevant positivity, compactness, domains, and finiteness here; this audit did not reprove those general theorems or perform a new literature audit. The S6 global geometric filling construction and the historical Split Zero/arithmetic constructions are external provenance leaves, not premises supplying a missing Yang–Mills inequality: the actual linear maps needed in these notes are written and checked locally.

## Obligation matrix

| Obligation | Status | Exact locus and finding |
|---|---|---|
| Common subsequence and positive-time derivative estimate | passed | SR 23–60. `sup` over the spectrum is bounded by the nonnegative half-line supremum; the latter is not falsely stated as the former. |
| Semigroup descends through the exact nullspace, is a positive contraction, and is strongly continuous | passed | SR 64–104. The finite-regulator quadratic forms give each property; the expanded proof is recorded below. |
| Spectral-support equality and diagonal Laplace edge | passed | SR 106–119 and 225–259, for the nonzero diagonal measures specified there. A zero diagonal contributes no support; the zero observable space has no positive-gap assertion. |
| Complex matrix Stieltjes inversion | passed | SR 201–221. The actual matrix imaginary part `(R-R*)/(2i)` retains complex off-diagonal entries. |
| Escaping-label inference | passed after the already-integrated correction | SR 261; VR 457–543. The notes now retain an explicit nonzero possible kernel `K/N`. |
| Smooth finite-link holonomy section and curvature coefficient | passed | VR 76–125. Disjoint ordered supports give `exp(K0)exp(K)=U`; the transverse derivative and volume powers leave exactly `J_chi/a_r`. |
| Vacuum marginal, horizontal fields, and score square | passed | VR 129–279 and RC L6–16. Prefix dependence is retained; coefficients are independent of the differentiated link, and all density and energy cross terms remain. |
| Closed kernel form and minimum-energy section | passed | RC 157–225. Smoothness and H1 continuity are only asserted at each finite regulator; the actual induced middle form is used in composition. |
| Raw-Gram block self-adjointness and response metric | passed | CR C4–12. The finite off-diagonal map is bounded; the source adjoint is `i*(x,h)=Gx`, giving `G F(z)^(-1) G`. |
| Singular moment coefficient fibres | passed | CR C20–22. `ker H_d=ker Z_d`, compatibility of `B_d`, and independence of the state `Y_d` from the coefficient solution are proved. |
| All-coupling vacuum derivative and covariant inverse | passed | AM A3–9. The inverse is on the spin-one gauge-Casimir sector; it is not assigned to its invariant contraction without a product-rule calculation. |
| Local neighboring-loop Haar coefficients | passed | AM A28–33 and A39–40. Shared-path singlet/triplet channels and unmatched-edge cancellations give the displayed coefficients. |
| Return from Haar coefficients to actual response | passed | AM A24–38 and A43–45. The actual conditional density and the `Q`-projection errors are retained. |
| Trial residual equals canonical quotient norm without a section correction | failed as a general assertion; corrected in the inspected source | AM A45a, lines 761–798, explicitly writes the extra nonnegative term `a_Y |alpha_Y-1|^2`; no such false identification is used in the retained conclusion. |
| Exact rational endpoint code and archived execution receipts | out of scope for this audit | AM A46–47, A49 radii, and the checker claims at 934–965 were read, but their programs/receipts were not independently replayed here. |
| Later zero-shift, gauge-native, uniform-gap, volume-limit, cubic, and linearized proofs | out of scope | These are later branches of the consolidated result history and are not downgraded by an earlier note's historical `next task` paragraph. |
| Four-dimensional continuum identification or physical continuum mass lower edge | not addressed by the audited contribution | The sources explicitly do not assert these conclusions. This is not a newly imposed proof obligation or an inferred theorem. |

## Decisive checks and exact maps

### 1. Positive-time reconstruction and escaping states

For a finite symbol sum `z=sum c_a[i_a,s_a]`, take its exact finite-regulator counterpart `z_n=sum c_a exp(-s_a A_n)r_(i_a,n)`. Its limiting squared norm is the displayed kernel quadratic form. At the regulator,

`||exp(-u A_n)z_n||^2 <= ||z_n||^2`,

`<z_n,exp(-u A_n)z_n> >= 0`,

and the semigroup is self-adjoint. Passing these inequalities to the common subsequence proves that the symbol shift descends through null vectors to a positive self-adjoint contraction. For each symbol its difference norm at `u=0` is

`C_ii(2s+2u)-2 C_ii(2s+u)+C_ii(2s)`,

which tends to zero by positive-time continuity. Finite sums and the contraction bound extend this to strong continuity on the completion. The bounded diagonal kernels then imply a finite zero-time norm and the Cauchy property of `[i,s]` as `s↓0`. This fills the semigroup details condensed into SR line 76 without altering any source definition.

VR (6.1) has source the vector space of norm-bounded regulator-state sequences for which all fixed rational-positive-time symbol pairings converge. Its target vector is the Riesz representative of those limits. Its exact kernel is `K`, the vanishing-pairing sequences. The diagonal lifting construction in VR line 486 proves surjectivity and produces a lift with norm tending to the target norm. Consequently the map on the two printed cochain windows has kernel `K/N`, where `N` consists of sequences whose norms tend to zero. These are algebraic quotient statements; the source does not silently assert an isometry from every regulator-state class.

For the literal test `v_n=chi_{ {n} }` in VR (6.4)–(6.6), the finite norm is one and energy is `1/n`, but every fixed Walsh label is eventually orthogonal to `v_n`. The fixed-label limiting generator has eigenvalues `|S|` for nonempty finite `S`, hence bottom one. This is a complete counterexample to the earlier unrestricted escaping-state inference and a valid nonzero element of `K/N`. SR line 261 now links to exactly this correction. The early error must not be reported as an unfixed claim in the consolidated SR note.

### 2. Literal retained deck action

VR lines 52–72 print `gamma(Lambda)⊂Z`, `gamma A=gamma`, `gamma(v)=epsilon∈{±1}`, `zeta=exp(-2pi i/m)`, and the total-line action generated by

`(x,z) -> (x+lambda,z)` and `(x,z) -> (Ax+v/m,zeta z)`.

For this literal action, with `H(x)=exp(-2pi i epsilon gamma(x))`,

`H(x+lambda)/H(x)=exp(-2pi i epsilon gamma(lambda))=1`,

`H(Ax+v/m)/H(x)=exp(-2pi i epsilon^2/m)=zeta`.

Therefore `z/H(x)` is invariant under both generators, and the inverse `([x],w)->[x,wH(x)]` is well-defined because replacing `x` by `Ax+v/m` multiplies its fibre value by precisely `zeta`. Both compositions are the identity. The local S6 companion lines 183–193 prints the same equivariance and the same maps. No inverse sign error occurs for the action actually retained here.

The literal cover action was also checked beyond that companion. In the full-source export named above, the embedded `finite_filling_certificates.tex` FF24–25, lines 112254–112274, retains the varying map

`Ghat(z,zeta)=(g_j z,R_(g_j)(z) zeta+Pi(g_j z)v_j/m_j)`

and covariance `R_(g_j)(z)Pi(z)=Pi(g_j z)A_j`. Hence the marking `Xi(z,x)=(z,Pi(z)x)` conjugates it to `(g_j z,A_jx+v_j/m_j)`. FF32, lines 112423–112427, prints the actual marked-cover action `(s,x)->(zeta_j s,A_jx+v_j/m_j)`. Passing its derivative to the tangent-space quotient normal to `s=0` multiplies that quotient by `zeta_j`, giving exactly FF42, lines 112625–112632, and the normal action used in VR. FF43, lines 112634–112645, explicitly explains that the positive section-character exponent corresponds to this quotient, whereas its negative describes the dual normal line.

Under the additional frame change `w=n/H_j(x)`, the action becomes `(x,w)->(A_jx+v_j/m_j,w)`. Its fibre multiplier disappears by that exact conjugation; the matrix `A_j` remains. A translation-only formula in the original unchanged normal coordinate would therefore be a different action, not a justification of the displayed descent. No such conflicting action was found in the inspected passages. This check proves the actual action-to-normal-quotient-to-smooth-frame morphisms; it does not certify all global geometric statements about the S6 filling or claim holomorphic triviality.

### 3. Score coupling and finite-source response

For the ordered refinement map, differentiation in fine link `j` gives `X_(j,beta) Jg=sum_alpha a_(j;alpha,beta) J X_alpha g`. Orthogonality of the retained adjoint matrices yields `Y_alpha Jg=J X_alpha g`. Their own-link independence makes the horizontal field divergence-free. Integration by parts first at `f=1` identifies the conditional mean of `Y log rho`; at general `f` it gives `X Ef=E Yf+E(fS)`. For `h=f-JEf`, this gives `E Yh=-E(hS)` and therefore exactly the three nonnegative squares in VR (3.11), with coefficient `kappa_n b`. In particular the mixed sign in RC L13 and CR C4 is negative.

In CR the raw coefficient pairing is `x*G y`, so the printed block operator is `H_F(x,h)=(G^(-1)(K0 x-W*h),Dh-Wx)`. Eliminating the second component gives `F(z)=K0-zG-W*(D-z)^(-1)W`, with the first-component inverse `F(z)^(-1)G`. Multiplying by the actual source adjoint on the left gives exactly `G F(z)^(-1)G`. The mixed-parameter resolvent identity gives `-(F(z)-F(w)*)/(z-conj(w))=L_w*L_z`, preserving the source Gram.

For an actual trial map `Y`, expansion with `R=W-(D+s)Y` gives

`R*(D+s)^(-1)R = M_s-W*Y-Y*W+Y*(D+s)Y`.

This proves C16 and both directions of C17. In C22 the cross moment is necessarily `N_(i+1)+s N_i`, not the unshifted `N_(i+1)`. The source's attempts record already identifies this repair. Singular `H_d` causes no gap: its nullspace equals `ker Z_d`, and every forcing column is orthogonal to it, so every normal-equation solution produces the same actual `Y_d`.

### 4. Vacuum derivative and local response constants

AM A3 follows by differentiating the full logarithmic-vacuum equation: the Casimir commutes with `X_(e,alpha)`, and the extra first-derivative commutator contracts an antisymmetric epsilon tensor against the symmetric product of the gradient components. At a maximum of `|X_e u|^2`, the squared antisymmetric part of the same-link second-derivative matrix contributes `|X_e u|^2/2`; `|X_e V|<=v r_e` then gives `|X_e u|<=2r_e xi`. This proves A5 with the stated all-coupling domain.

The spin-one-sector estimate has its actual source and target: the vertex gauge-Casimir equals two on `E_v`, while the pointwise sum-of-generators inequality gives `sum |G_v h|^2<=d_v sum_(e incident v)|X_e h|^2`. After integration in the gauge-invariant vacuum measure, `q_A(h)>=2 kappa ||h||^2/d_v`. Thus A9 is valid on `E_v`; the invariant contraction is a different vector whose product derivatives are explicitly calculated in A22–23 and A35. No physical-sector gap follows solely from A9.

In AM A28–30, every shared-path contraction has singlet norm `9/64` and triplet norm `3/64`; the unshared links contribute `nu_p=3(ell+4-2s_p)/4`, while the triplet adds `2s_p`. For `ell=4`, twelve faces have `s_p=1`, hence

`c_j=12 [3(9/2)^j+(13/2)^j]/48`,

which gives `(c0,c1,c2)=(1,5,103/4)`. The trial coefficients `4/33` and `4/45` are exactly `(2/3)/(9/2+1)` and `(2/3)/(13/2+1)`. Thus `(K+1)Z=(2/3)J`, and its two Haar pairings are the printed `28/165` and `796/27225`.

The density comparison is with the actual interacting local marginal and conditional fibre, not a replacement of the vacuum by Haar measure. The pointwise bound is integrated along paths of length `2pi` per ordinary link and `4pi` for each free loop-chain coordinate at fixed product; this gives precisely the exponents `32pi d xi` and `32pi(d+ell-2)xi`. These enter A36–38 and A42–45, including the conditional projection terms.

For the canonical-residual distinction, let `a_Y=<Y,(D+kappa)Y>`, `c_Y=<Y,W>`, and `alpha_Y=c_Y/a_Y`. Then `R_can=W-(D+kappa)alpha_Y Y` is orthogonal to `(D+kappa)Y` in the dual pairing. Consequently

`<R,(D+kappa)^(-1)R> = ||[W]||_dual^2 + a_Y |alpha_Y-1|^2`.

AM A45a retains this exact term. A45 is a valid enclosure from the chosen trial residual without identifying that residual with the minimizing one.

## Remaining scope and consolidation consequence

There is no newly isolated missing algebraic implication in the bounded claim card. The sources expressly leave the continuum physical identification unresolved; an audit of these earlier notes must not replace the later current results by those historical status paragraphs. Conversely, the named later notes cannot be certified by this audit merely because they were imported in the same consolidation.

The strongest safe consolidation statement from this pass is: these retained early and middle notes provide an exact chain of vacuum-weighted refinement, response, residual, spectral reconstruction, and local Wilson-loop estimates in their printed domains; the explicit escaping-state and noncanonical-residual corrections are present and should be linked from the cumulative result history. The numerical certificates remain claims with separate executable verification evidence until the dedicated replay pass checks them. The prescribed continuum path has `xi_n=(g0^(-2)+beta n log 2)^2/4`, so the small-`xi` elementary-loop intervals must retain their coupling domain rather than be extrapolated along that path.

The cheapest follow-up checks are the already separate standard-library checker replay and the later-continuation audit; no Lean run or new research theorem is required by this bounded consolidation audit.

## Commands and audit provenance

Source discovery used `rg --files` and `rg -n` over the named continuation paths; complete reads used `Get-Content` with numbered lines; source pins used `Get-FileHash -Algorithm SHA256`. The first file-discovery call omitted the existing `yang-mills/` path component and returned only path errors; it read or modified no source. One PowerShell hash-list command had a parser error from a pipeline after `foreach`; the corrected read-only command produced the hashes above. These failures are not execution receipts for any proof checker.

A separate bounded subagent checked the printed S6 equivariance and quotient inverse, then located the full-source FF24–25, FF32, and FF42–43 passages. Those exact passages were subsequently read by this audit agent. That is an additional derivation of the action calculation, not a certificate of every S6 global geometric statement. No checker program was executed by this audit agent, and no broad external literature search was performed.


# Independent bounded audit: gauge-native physical gap and spatial return

\begin{quote}\footnotesize
\textbf{Source classification:} independent bounded mathematical audit

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/audits/gauge_native.md}

\textbf{SHA-256:} \path{b2e296d8186287efbf778a5612814af8e081a7b1f34bb67c0a1596e66eae4d77}

\textbf{Editorial provenance notice:} This review has the exact scope stated in its body. Its inclusion is not exhaustive certification of all sources or a proof of the continuum mass-gap problem.
\end{quote}


Date: 2026-09-16.

## Claim and primary verdict

The selected claim is the analytical implication from the written, absolutely convergent, gauge-invariant logarithmic-vacuum coefficient construction to the physical spectral gap of the original finite-box Hamiltonian, and then to the physical gap of the explicitly constructed fixed-spacing infinite-volume semigroup. The selected finite-box statement is SECOND_SOURCE.md R10:

\[
\Delta_L\ge\frac{3\kappa}{2}\bigl(1+\sqrt{P_2(\xi)}\bigr),\qquad
P_2(\xi)=1-\frac{256}{3}\xi+\frac{10720}{9}\xi^2,
\]
\[
L\ge2,\quad a,g>0,\quad\kappa=2g^2/a,\quad\xi=1/(4g^4),
\quad0<\xi\le\alpha=\frac3{4(32+\sqrt{354})}.
\]

The selected spatial statement is R14 for the generator and measure actually constructed by SPATIAL_RETURN.md, at fixed original \(a,g\):

\[
A_\infty\big|_{L^2_{\rm phys}(\nu)\cap1^\perp}
\ge\frac{3\kappa}{2}\bigl(1+\sqrt{P_2(\xi)}\bigr).
\]

**Primary verdict for this selected implication: proved as written.** This is a bounded mathematical audit of the explicit analytical inference, not a certification of every statement or fixture in the delivered package. No concrete analytical failure was found in that inference. In particular, it would be incorrect to classify the physical gap argument as merely extrapolating from a finite spin census or a finite coefficient matrix: the written proof treats every smooth physical eigenfunction and returns to the original Hilbert form. This report does not change any repository theorem status.

The following are outside this verdict: the four-dimensional continuum problem; claims of literature priority; every predecessor response error constant; exact replay of the 240-by-240 integer certificate; and the primary-source comparison in BAND_AND_CERTIFICATE.md B8. The files expressly leave the continuum problem unevaluated. No missing continuum theorem is silently supplied here.

## Source identity and method

All paths below are relative to:

`yang-mills/`.

The main four files were read in full with numbered lines. Relevant precursor norm, vacuum, form, conditional-kernel, and local-density passages were also read. The package's archived workflow instructions were treated as historical evidence, not as authority to perform remote publication or new research.

| Source | SHA-256 |
|---|---|
| `continuations/20260915-gauge-native-band/RESEARCH_NOTE.md` | `c24f5235b8c25daa1ee20fb81a13d8db94b88cb99b298ac7d10c8b4e5faafebd` |
| `continuations/20260915-gauge-native-band/SECOND_SOURCE.md` | `044279aa33cc6a53ea933ebe0aa903741653b4964883d7ea40b14b6bf5b9ff14` |
| `continuations/20260915-gauge-native-band/SPATIAL_RETURN.md` | `b7c24b984cf19ac793ae6df532bfa9fb9db98d6319e1a02bb3b92607366f626e` |
| `continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md` | `0e02c37b3ecc51f04d2f3c18cca686cc96bc7a8b5fd3bb467b143970a02d7887` |
| `continuations/20260915-uniform-gap-zero-shift/RESEARCH_NOTE.md` | `83d4de98b7b3e5de85efd747f56f1a42261cc55570e419c0d8fe62ccab93bad8` |
| `continuations/20260915-actual-loop-moments/RESEARCH_NOTE.md` | `0ac4afbec39b2e878d5555af85a86803d9ba6ac5505dc7817f231e5533c0dd2b` |

Skill used: `mathbox:proof-audit`; relevant checklist portions: logic and typing, representation and symmetry, computation-dependent claims, and external sources. An additional read-only subagent independently inspected SPATIAL_RETURN.md S10–S13 and its supporting S5–S6, and SECOND_SOURCE.md R4, without being given a proposed defect or substitute model. That check reported no concrete failure. Agreement is not treated as mathematical evidence in place of the derivations below.

## Objects, norms, and exact return maps

The finite graph consists of the vertices \(\{-L,\ldots,L\}^3\), all positively oriented contained nearest-neighbor links, and all contained elementary faces. The Hilbert space before restriction is \(L^2(SU(2)^{E_L},dU)\) with product Haar probability; the physical subspace is fixed by the original vertex gauge action. The original operator is

\[
H_L=\kappa K_L+\kappa\xi\sum_p(2-W_p),\qquad
K_L=-\sum_{e,\alpha}X_{e,\alpha}^2.
\]

Its finite compact-group operator/form domains are respectively \(H^2\) and \(H^1\), restricted to invariant functions in the physical case. The actual positive unit vacuum \(\psi_L\) supplies \(\rho_L=\psi_L^2\). Multiplication by \(\psi_L\) is the unitary map from \(L^2(\rho_LdU)\) to the original Haar Hilbert space. Its inverse divides by \(\psi_L\). The transported form is exactly

\[
q_{\mathcal A_L}(f,h)=\kappa\int\rho_L\sum_{e,\alpha}
\overline{X_{e,\alpha}f}X_{e,\alpha}h\,dU.
\]

These assertions are at gauge-native RESEARCH_NOTE.md lines 7–30. The positive-vacuum construction retaining the energy scalar is lines 204–219; it is not a change of physical measure made without a map.

For original product-spin labels, \(c(j)=\sum_ej_e(j_e+1)\) and \(A_j=d_j\int f\pi_j^*dU\), so that \(f=\sum_j\operatorname{Tr}(A_j\pi_j)\). The auxiliary spaces used in the spectral inference are

\[
X_0=\{f:\ A_0=0,\ \sum_{j\ne0}\|A_j\|_1<\infty\},\qquad
Y_0=\{f:\ A_0=0,\ \sum_{j\ne0}c(j)\|A_j\|_1<\infty\}.
\]

Here \(\|\cdot\|_1\) is the trace norm of the full coefficient matrix, including the original \(d_j\). The local source norm is a different norm on labelled coefficient families:

\[
\|v\|_{\mathrm{loc},1}
=\max_e\sum_{S\ni e}\sum_{j\ne0}c(j)\|A_{S,j}\|_1.
\]

The support label \(S\) contains the active spin support and is retained after cancellation. None of these norms is identified with the physical \(L^2\) norm. The finite-box total \(c\)-weighted coefficient sum is at most \(|E_L|\|v\|_{\mathrm{loc},1}\); that factor is used for finite-box regularity, not for the uniform spectral estimate.

The exact map from centered-vacuum functions to Haar-mean-zero functions is

\[
f\longmapsto Q_Hf,\qquad
y\longmapsto y-\langle y\rangle_{\rho_L}.
\]

On their respective centered domains these maps are inverses. They intertwine \(\mathcal A_L\) with \(\kappa K_L-2\kappa Q_H\sum_i(X_iv)X_i\). This is the decisive bridge, given explicitly at RESEARCH_NOTE.md lines 242–256. No volume-uniform bound on the norms of those inverse maps is needed for the eigenvalue exclusion argument.

## Dependency graph and obligation matrix

The audited chain is:

1. Vertex invariance implies the incident-spin inequalities G5; the cubic graph then gives \(c(j)\ge6j_e\), and every nonconstant physical block has \(c(j)\ge3\).
2. The full coefficient product inequality and original generator bounds imply G13 and G23, retaining all output irreducibles and union labels.
3. The original first and second sources give the positive majorant R7; the endpoint tail R9 proves convergence also at \(\alpha\).
4. Finite-box second-derivative summability identifies the assembled positive eigenfunction with the actual vacuum, including \(E_{0,L}\).
5. G23 plus the inverse mean-change map gives an exclusion interval for every physical eigenfunction; complete compact spectral resolution gives R10 on the full physical form domain.
6. Interior drift-row summability constructs the actual semigroup volume limit. Fourier norm dissipation gives uniform mixing and a coupling modulus. The endpoint is reached by the modulus, without assigning a finite derivative row there.
7. Uniform cylinder-semigroup convergence and weak vacuum-measure convergence pass the finite physical \(L^2\) estimate to R14; gauge averaging gives density in the complete physical Hilbert space.

| Obligation | Result | Precise location / scope |
|---|---|---|
| Physical spin restriction and free spectral minimum | Passed | RESEARCH_NOTE.md 52–89; includes all physical blocks, not a sampled spin range |
| Complete Fourier multiplication/derivative estimates | Passed | RESEARCH_NOTE.md 111–145; predecessor U7–U14 at 112–209 |
| Original coefficient source and endpoint convergence | Passed | RESEARCH_NOTE.md 158–219; SECOND_SOURCE.md 7–123 |
| Auxiliary-to-physical eigenfunction return | Passed | RESEARCH_NOTE.md 229–280; reconstruction below |
| No missing volume factor in spectral inequality | Passed | Its relative drift bound uses an edge anchor; regularity is only needed separately for each finite volume |
| Infinite-volume dynamics and mixing | Passed | SPATIAL_RETURN.md 110–185 and 250–333 |
| Endpoint extension without divergent row bound | Passed | SPATIAL_RETURN.md 335–398; SECOND_SOURCE.md 152–176 |
| Physical Hilbert-space gap passage | Passed | SPATIAL_RETURN.md 187–205; original finite gap is applied before taking limits |
| Band contour and all-order remainder, as written analytical argument | Passed in bounded inspection | BAND_AND_CERTIFICATE.md 7–99, 243–264; no rank-to-continuum inference |
| All entries of the integer L=2 certificate | Out of scope for execution | No checker or certificate was executed in this audit |
| External planar-paper comparison | Out of scope | BAND_AND_CERTIFICATE.md 308–369 is corroboration, not an input to R10/R14 |
| Four-dimensional continuum conclusion | Out of scope; source explicitly does not assert it | SECOND_SOURCE.md 181–185; SPATIAL_RETURN.md 230–248, 400–404 |

## Decisive analytical reconstruction

### 1. The original gauge restriction really improves the drift constant

For a nonzero physical Fourier block, a vertex invariant intertwines each incident spin into the tensor product of the others, giving \(j_e\le\sum_{f\ni v,f\ne e}j_f\). For an edge with endpoints \(u,v\), let \(J_1\) be the spin sum on other edges incident on those endpoints. Then \(J_1\ge2j_e\). On the cubic graph the other endpoints of these edges are distinct. Summing the same vertex inequality there gives \(J_1\le2J_2\), where \(J_2\) counts the remaining neighboring edges once. Consequently \(\sum_fj_f\ge j_e+J_1+J_2\ge4j_e\). Since \(j(j+1)\ge(3/2)j\) for every nonzero half-integer spin, \(c(j)\ge6j_e\). This proof uses the stated open cubic graph, so it does not assume a graph inequality valid on arbitrary graphs.

For a source satisfying \(\|v\|_{\mathrm{loc},1}\le r\),

\[
\sum_{S\ni e,j}j_e\|A_{S,j}\|_1\le r/6.
\]

The coefficient product and derivative inequalities therefore give, for arbitrary scalar \(f\in Y_0\),

\[
\left\|Q_H\sum_i(X_iv)(X_if)\right\|_{X_0}
\le3\sum_k\|A_k(f)\|_1\sum_e k_e\frac r6
\le\frac r3\|f\|_{Y_0}.
\]

The last inequality uses \(\sum_ek_e\le(2/3)c(k)\), which holds on the full scalar space. Thus the source needs physical gauge invariance, but \(f\) need not be physical for this particular drift estimate. With \(\epsilon=2r/3\), the full perturbation has norm at most \(\kappa\epsilon\) from \(Y_0\) to \(X_0\). This distinguishes the hypotheses needed on the two factors.

### 2. Every physical eigenfunction is covered

Let \(\mathcal A_Lf=\lambda f\), \(\lambda>0\), in the physical Hilbert space. The compact smooth elliptic problem makes \(f\) smooth. For each fixed finite box its Fourier coefficients belong to \(Y_0\); no uniform-in-volume regularity constant is required. Set \(y=Q_Hf\ne0\). The exact mean-change map gives

\[
(\kappa K_L-\lambda)y=-V_\xi y.
\]

For \(0<\lambda<3\kappa\), every physical coefficient has \(c\ge3\), and

\[
\sup_{c\ge3}\frac{c}{\kappa c-\lambda}
=\frac3{3\kappa-\lambda}.
\]

Hence

\[
\|y\|_{Y_0}
\le\frac{3\kappa\epsilon}{3\kappa-\lambda}\|y\|_{Y_0}.
\]

Because \(y\ne0\), this excludes \(0<\lambda<3\kappa(1-\epsilon)\). Eigenvalues already at least \(3\kappa\) satisfy the same lower bound. The full compact spectral expansion then gives the form inequality for every physical \(H^1\) vector centered in the actual vacuum measure. Substituting \(r_2=(3/4)(1-\sqrt{P_2})\) gives R10. This is an exact spectral argument on the original operator, not an estimate only on the coefficient window.

### 3. The endpoint spatial argument does not require a hidden finite derivative row

Write the actual finite evolution as \(T_L(t)F=c(t)+y(t)\), where \(c\) is its Haar mean. Its smooth finite solution is differentiable in \(X_0\), and

\[
y'=-\kappa K_Ly-V_\xi y.
\]

For \(y\in Y_0\), dominated convergence applied to the individual coefficient norms gives

\[
\left.\frac d{dh}\right|_{h=0+}\|(I-h\kappa K_L)y\|_{X_0}
=-\kappa\|y\|_{Y_0}.
\]

The domination is \(\kappa c(j)\|A_j\|_1\). The perturbation estimate proves

\[
D^+\|y(t)\|_{X_0}\le-\kappa(1-\epsilon)\|y(t)\|_{Y_0}.
\]

The same coefficient estimate *before* removing the constant coefficient bounds \(|c'|\le\kappa\epsilon\|y\|_{Y_0}\). Integrating both inequalities reconstructs the vacuum mean and yields

\[
\|T_L(t)F-\langle F\rangle_{\rho_L}\|_\infty
\le\frac{\|Q_HF\|_{X_0}}{1-\epsilon}
e^{-\kappa c_*(1-\epsilon)t},
\]

with \(c_*=3\) for physical \(F\) and \(3/4\) on the scalar space. A fixed cylinder has the same original Fourier norm in all larger boxes. That fact supplies the volume-independent prefactor.

For interior couplings the full derivative matrix has a finite row sum, so the finite SDE comparison constructs the uniform cylinder-semigroup volume limit on compact time intervals. The displayed mixing estimate then makes the entire sequence of vacuum expectations Cauchy: first send the box sizes to infinity at fixed \(t\), then send \(t\) to infinity. Duhamel's formula, the same full coefficient drift estimate, and integrated \(Y_0\) dissipation give

\[
\sup_{t\ge0}\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
\le\frac{\epsilon_2(\eta)-\epsilon_2(\xi)}{1-\epsilon_2(\xi)}
\|Q_HF\|_{X_0}.
\]

For \(\eta=\alpha\), the scalar quotient is
\(\sqrt{P_2(\xi)}/(1+\sqrt{P_2(\xi)})\to0\). Inserting an interior coupling between two endpoint finite-volume evolutions proves that the endpoint family is Cauchy. This uses the convergent original source and its coupling modulus, not the divergent endpoint derivative series. Finite reversibility, uniform semigroup convergence, weak measure convergence, and density of gauge-averaged cylinders then give the physical \(L^2\) inequality R14.

## Concrete non-load-bearing document defects

These are transcription/cross-reference defects, not missing mathematical implications:

1. `RESEARCH_NOTE.md:30` says the direct positive-vacuum/form proof is in “G8.” The proof is at G20–G21, lines 204–219. Equation G8 is the free physical Casimir spectrum.
2. `SPATIAL_RETURN.md:3` and `:228` call the later additions “S10–14” as sections; equations S10–S14 elsewhere already denote conditional/drift statements. The later section titles are numbered 10–14 and the endpoint calculation itself is at equations S31–S35. Readers should use the section locator, not the earlier equation labels.
3. `BAND_AND_CERTIFICATE.md:360–362` has malformed TeX in the summation subscript of B32 (`p\ {` / `m in\ plane}\p\sim q`). The preceding paragraph and the left side determine the intended sum over plaquettes in the fixed plane sharing an edge with \(q\). The finite and infinite spectral gap derivations do not depend on this rendering.

## Computation/source checks and limitations

Commands used here were read-only PowerShell `Get-Content` with line enumeration, `rg` searches, and `Get-FileHash -Algorithm SHA256`. No Lean, Lake, Elan, external source program, or supplied Python checker was run by this audit agent. The Python checker was inspected sufficiently to locate its actual scope; its final result explicitly says “Exact finite algebra, integer graph/inertia calculations and rational evaluation of written analytic estimates” and states that the analytic proofs are not formally certified (`verify.py:775–782`). That disclosure is accurate as to what such a checker can establish.

The local-density input used for the nonzero Wilson vector was traced past the uniform-gap note's U54 to `20260915-actual-loop-moments/RESEARCH_NOTE.md:107–134,420–434`: a maximum-principle argument proves \(\sup|X_e\log\rho|\le16\xi\) at all positive couplings, and the original group diameter \(2\pi\) gives the four-link marginal lower bound \(e^{-128\pi\xi}\). This check avoids importing a small-coupling bound into the enlarged domain without examining its stated range.

No external literature theorem is being imported from BAND_AND_CERTIFICATE.md B8 into the selected claim. Its planar paper comparison was not independently fetched or verified. Standard compact elliptic regularity, Peter–Weyl decomposition, and compact self-adjoint spectral resolution are the analytical background used in the written proof; this bounded audit checked their stated finite compact-manifold setting and their role, rather than reconstructing those background theories.

## Remaining work and strongest safe consolidation wording

No smallest missing implication was identified in the selected coefficient-to-fixed-spacing-physical-gap chain. The independent spatial cross-check reached the same bounded conclusion. This is not a claim that an exhaustive proof audit of the entire historical package has been completed.

A safe consolidation description is: “Written strong-coupling results for the original SU(2) lattice Hamiltonian, including an explicit volume-uniform physical gap, its fixed-spacing infinite-volume return, and a finite-band calculation with an analytic remainder; exact finite fixtures and execution receipts are tracked separately. The four-dimensional continuum limit remains unevaluated.”

The source's retained running path \(a_n=a_0 2^{-n}\), \(g_n^2=1/c_n\), \(c_n=g_0^{-2}+\beta n\log2\) with \(\beta>0\) eventually leaves the admissible domain. In particular the displayed strong-coupling theorem cannot be presented as a continuum mass-gap solution. This is an explicit limitation already proved and stated by the sources, not a newly invented condition.


# Bounded mathematical audit of the local-fibre continuation

\begin{quote}\footnotesize
\textbf{Source classification:} independent bounded mathematical audit

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/audits/local_fibres.md}

\textbf{SHA-256:} \path{e0c7ef70174d2550b3e9a1d3a729a2c179f20bd6652389dd70011fffba6f53e3}

\textbf{Editorial provenance notice:} This review has the exact scope stated in its body. Its inclusion is not exhaustive certification of all sources or a proof of the continuum mass-gap problem.
\end{quote}


Date: 2026-09-16. This is a read-only audit report, not a source correction,
independent mathematical certification, or a replay of the delivery's checker.
The complete research note and its README were read. The fresh derivations
below concentrate on conditional variance, the zero-shift inverse, the retained
exterior, and the nested minimum sections. No Lean process was started.

## Exact target and primary verdict

**Primary verdict: proved as written**, for the following bounded claim:
at every finite original regulator, the conditional kernel for observation
`(Omega, every exterior link)` has the form lower bound Z19 and inverse Z20;
the stated heat comparison gives the explicit inverse estimate Z22 along the
specified sequence; and the maps and response/norm identities Z51–Z53 connect
that kernel to the earlier Omega-only observation on their actual form domains.

This verdict does **not** certify all numerical constants in Z27–Z50a or the
408-check execution claim. Those have been read and their role examined, but
the absent branch checker and its full exact-arithmetic implementation were
not independently replayed in this audit. No substantive counterexample was
found to the bounded target. Two minor domain qualifications and the material
publication/continuum limitations are recorded below rather than hidden.

Authoritative artifact:

- Repository-relative path:
  `yang-mills/continuations/20260915-zero-shift-local-fibres-review/DELIVERED_RESEARCH_NOTE.md`.
- SHA-256 observed locally:
  `42aa9ab14a4b42ba9d170803fb0f9ce9f0d1d763d10139b3a15f9ba317543e55`.
- This equals the hash printed in README lines 41–42.
- Source locators below refer to the 1,031-line delivered note with this hash.
  README locators refer to its 61-line companion.

The original compact configuration manifold is
`M = SU(2)^E` for the contained positive links of `{-L,...,L}^3`, `L>=2`.
Haar measure is probability measure. All scalar spaces here are complex.
`a,g>0`, `kappa=2g^2/a`, `v=1/(2g^2 a)`, `xi=v/kappa=1/(4g^4)`.
The original derivatives use `T_alpha=-i sigma_alpha/2`, with their original
Casimir eigenvalues and original ordered Wilson words; no coefficients,
orientations, or physical spacings are changed in this audit.

Let `psi` be the smooth strictly positive unit ground state, `rho=psi^2`,
`H_rho=L^2(M,rho dU)`, and `V=H^1(M)`. The weighted and Haar Sobolev spaces
have equivalent norms at this fixed regulator because `rho` is smooth and
bounded above and below by positive numbers. The original form is

\[
 q_\rho(f,h)=\kappa\int_M\rho\sum_{e,\alpha}
                    \overline{X_{e,\alpha}f}X_{e,\alpha}h.
\]

Its multiplication map `f -> psi f` is unitary onto the original physical
configuration Hilbert space before gauge restriction, and maps this form to
the original `H-E0` form. These are the objects audited, rather than a surrogate
matrix or a Haar replacement for the interacting vacuum.

## Dependency graph and obligation matrix

The central implication graph is:

1. Positive smooth vacuum and its original closed form
   -> actual weighted conditional expectations and Sobolev form domains.
2. Original SU(2) heat identity + bounded original local potential
   -> all-configuration conditional-density ratio Z15/Z17.
3. Haar product gap `3/4` + this single density ratio + conditional Fubini
   -> Z19 -> represented self-adjoint `D_l` and bounded inverse Z20.
4. Z17 + the specified original `a_n,c_n,L_n`
   -> Z21/Z22 -> resolvent expansion and direct-sum inverse estimates.
5. Nested conditional expectations + closed coercive kernel forms
   -> minimum sections -> exact additional response Z52 and state norm Z53.

| Obligation | Result | Evidence/limit |
|---|---|---|
| Original heat time, sphere measure, and derivative coefficient | passed | Z6–Z8, lines 68–88; exact [HK] v2 equations inspected and translated below |
| Local/exterior tensor decomposition and semigroup comparison | passed | Z13–Z17, lines 143–200; bounded positive multiplication comparison keeps the entire exterior operator |
| Conditional-mean implication and one-ratio Poincare comparison | passed | Z18–Z19, lines 204–245; reconstructed below |
| Restricted form density, closedness, operator inverse and compactness | passed | lines 247–257; `H^1` stability follows in the displayed global coordinates |
| Sequence exponent, coefficient, and asymptotic inverse bound | passed | Z21–Z22, lines 264–292; direct substitution below |
| Zero-shift resolvent identity and energy-relative remainder | passed | Z23, lines 294–315; reconstructed below |
| Nested observation quotient, second minimizer, response and norm | passed | Z51–Z53, lines 844–893; full derivation below |
| Restriction to gauge-invariant physical vectors | passed | equivariance and uniqueness argument below |
| All individual quaternion/Hessian/support and outward-arithmetic constants | not addressed in full | source read; no independent exhaustive checker replay here |
| Claimed 408 tests, optimization replay, corruption controls | not addressed | historical execution reports, README 48–56; not executions observed by this audit |
| Physical continuum Hilbert space or complete uniform mass gap | out of scope | explicitly not established by source lines 981–988 |
| General [SZ] attribution and historical priority | out of scope | the operator quotient construction is elementary to verify; no broader attribution audit |

## Conditional variance and the actual inverse

Write `C` for the four original loop links and `Z=U_(C^c)`. The global map
Z18 is invertible by the displayed prefix formulas and sends original Haar
measure to `dOmega prod_j dg_j dZ`. Thus it is a genuine global product
coordinate map, including inversely traversed links through their
Haar-preserving inversion maps.

Let `m(Omega,Z)=int rho(Omega,g,Z) dg`. The conditional expectation is

\[
 E_lh(\Omega,Z)=\frac{\int h(\Omega,g,Z)\rho(\Omega,g,Z)\,dg}
                         {m(\Omega,Z)}.
\]

It maps `H_rho` to `H_l=L^2(m dOmega dZ)`; its adjoint is pullback `J_l`.
Fubini proves `E_l J_l=I`, hence `P_l=J_l E_l` is an orthogonal projection
and `K_l=ker E_l` is a closed Hilbert subspace. Smoothness and positivity on
the compact product make every coefficient in the first derivative of this
conditional integral bounded. Differentiating in the global coordinates
proves that `E_l,J_l,P_l,Q_l` preserve the respective `H^1` spaces and smooth
functions. Consequently `V_l=H^1(M) intersect K_l` is form closed, and
`Q_l` applied to smooth approximations proves its form density by smooth
members of `K_l`.

Conditional Fubini gives `E[h|Z]=E[E_lh|Z]=0` for `h in K_l`.
At each fixed `Z`, write `mu_Z=rho(U_C,Z)/int rho(U_C,Z)dU_C` and let
`m_Z,M_Z` be its minimum and maximum. For each complex `H^1` function `h`,

\[
\begin{aligned}
 \operatorname{Var}_{\mu_Z}(h)
 &=\inf_{b\in\mathbb C}\int|h-b|^2\mu_Z\,dU_C\\
 &\le M_Z\operatorname{Var}_{Haar}(h)\\
 &\le\frac{4M_Z}{3}\int\sum_{e\in C,\alpha}|X_{e,\alpha}h|^2\,dU_C\\
 &\le\frac{4M_Z}{3m_Z}
       \int\sum_{e\in C,\alpha}|X_{e,\alpha}h|^2\mu_Z\,dU_C.
\end{aligned}
\]

This uses exactly one density ratio `M_Z/m_Z`. Since `E[h|Z]=0`, integrate
against the unchanged exterior marginal and add the nonnegative exterior
derivative contribution to obtain

\[
 q_\rho(h)\ge\frac34\kappa e^{-H_C}\|h\|_\rho^2
 \qquad(h\in V_l).
\]

No claim that `h` is a function only of the loop was used. In particular,
its dependence on every exterior link survives this inequality.

The operator represented by this restricted form has the exact domain

\[
 \operatorname{Dom}D_l=
 \{h\in V_l:\ \exists r\in K_l\text{ such that }
       q_\rho(v,h)=\langle v,r\rangle_\rho\ \forall v\in V_l\},
 \qquad D_lh=r.
\]

It is positive self-adjoint on `K_l`, with `D_l>=delta_C I` and
`||D_l^(-1)||<=delta_C^(-1)`. Compactness of the finite-regulator embedding
`H^1(M)->L^2(M)` gives its compact resolvent. For smooth `h in K_l`,
`D_lh=Q_l A h`; the form definition is the one needed for nonsmooth vectors.

## Heat comparison, original units, and sequence

The source decomposition `H=kappa K_C+H_ext,C+V_C` has
`0<=V_C<=4v m_C`; `H_ext,C` retains every other derivative and every face
not touching `C`. Positivity of the product heat semigroup and its bounded
potential Trotter factors gives the pointwise comparison Z14. At fixed `Z`
its exterior kernel is common to both loop configurations. Its ratio is
therefore bounded by the product of four original link-kernel ratios, and
the common ground energy factor cancels. Squaring for `rho=psi^2` gives

\[
 \operatorname{osc}_{C\mid C^c}\log\rho
 \le 8m_C\xi\theta+8\pi^2/\theta.
\]

Here `m_C=13`, and the optimized physical time is
`t_*=theta_*/kappa=(pi a/2)sqrt(4/13)`, using the unchanged identity
`kappa v=1/a^2`. Thus the statement retains the original energy and time
scales. Keeping the Z12 heat prefactor yields exactly

\[
 \frac{\sup_{U_C}\rho(U_C,Z)}{\inf_{U_C}\rho(U_C,Z)}
 \le (8c)^{-8}e^{Bc},\quad c=g^{-2}\ge2,
 \quad B=8\pi\sqrt{13}.
\]

For `a_n=a0 2^(-n)`, `c_n=c0+beta n log 2`,
`kappa_n=2^(n+1)/(a0 c_n)`, direct substitution into the preceding
Poincare inequality gives

\[
 \delta_n\ge\frac34\frac{2^{n+1}}{a_0c_n}
                  (8c_n)^8e^{-Bc_n}
 =\frac{3\,8^8}{2a_0}e^{-Bc_0}c_n^7 2^{(1-B\beta)n}.
\]

At exactly `beta=1/B` and `n>=n0` this proves Z22, including its coefficient
and its power seven. The loops have physical side `a_n`; the estimate says
neither that their physical size stays fixed nor that these Hilbert spaces
have already been identified with a continuum field Hilbert space.

For a finite family of smooth retained observations, put
`T=D_l^(-1/2)W`. The original nonnegative coupled form implies
`T^*T=W^*D_l^(-1)W<=K0`: minimize its kernel variable at `D_l^(-1)W x`.
Spectral calculus gives, for `|z|<delta`,

\[
 W^*(D_l-z)^{-1}W=T^*(I-zD_l^{-1})^{-1}T.
\]

Subtract the finite geometric sum inside this formula. The remaining
multiplier has operator norm at most
`(|z|/delta)^(d+1)/(1-|z|/delta)`. Cauchy–Schwarz and `T^*T<=K0` give
exactly Z23. This proves the stated continuation through zero shift; it
does not supply a limit of the individual moments or a physical resolvent
pole. For the elementary trace `K0<=4kappa_n`; at `d=n`, the bound has
logarithm at most `-7(n+1)log c_n+O(n)` on a fixed complex disk. It tends
to minus infinity even while the raw kinetic scale grows.

## Exact exterior map and minimum sections

Let `nu(Omega)=int m(Omega,Z)dZ`, let `E_o:H_l->L^2(nu dOmega)` be
conditional expectation in the exterior variables, and let `J_o` be its
pullback. The Omega-only expectation is `E_C=E_o E_l` and its pullback is
`J_C=J_l J_o`. For every `h in K_C=ker E_C`,

\[
 h=Q_lh+J_lE_lh,\qquad E_lh\in\ker E_o.
\]

Conversely `J_lk in K_C` for `k in ker E_o`. These are orthogonal summands,
so

\[
 K_C=K_l\mathbin{\oplus_{H_\rho}}J_l(\ker E_o).
\]

This proves both inverse laws in Z51; it also proves that the induced map
from the Hilbert quotient `K_C/K_l` is isometric. The same maps preserve
the form domains by the compact smooth-density derivative argument above.

For `g in H_l` with `J_lg in V`, Z19 and closedness make `q_rho` a complete
inner product on `V_l`. Riesz gives the unique `h_l(g) in V_l` satisfying

\[
 q_\rho(v,h_l(g))=-q_\rho(v,J_lg)\quad(v\in V_l).
\]

Thus `S_lg=J_lg+h_l(g)` is form orthogonal to `V_l`, the section is linear,
and it minimizes the energy of the original affine fibre. If `J_lg` is
in `Dom A`, this identity is exactly
`h_l(g)=D_l^(-1)(-Q_l A J_lg)`, including the minus sign.

The second minimizer exists at fixed regulator without assuming any
uniform estimate. Indeed, on the compact original product let
`rho_min=min rho>0`, `rho_max=max rho`. The same single-ratio comparison
with the full product Haar gap proves

\[
 q_\rho(u)\ge\lambda\|u\|_\rho^2,
 \qquad\lambda=\frac{3\kappa}{4}\frac{\rho_{\min}}{\rho_{\max}}>0,
 \qquad\int\rho u=0.
\]

Every `u in K_C` is centered. Riesz on `V intersect K_C` therefore gives
the unique full correction `h_C` minimizing `q_rho(J_Cf+h)` for the
centered loop trace `f`. Define `k_*=E_lh_C`. The orthogonal decomposition
and the first minimum section give

\[
 h_C=J_lk_*+h_l(J_of+k_*).
\]

Hence `k_*` is precisely the minimizing exterior form vector in the note.
For `k in ker E_o` in that coarse form domain,
`q_eff(k)=q_rho(S_lk)>=lambda ||S_lk||^2>=lambda ||k||_m^2`, which also
proves its uniqueness. This argument supplies the full domain/coercivity
justification behind the concise existence assertion at lines 865–868.

Set `x=J_of`. Stationarity gives
`q_eff(x+k_*,k_*)=0`. Expansion, with its complex conjugate, therefore gives

\[
 q_{\rm eff}(x+k_*)=q_{\rm eff}(x)-q_{\rm eff}(k_*).
\]

Subtract from the unchanged `K0=q_rho(J_Cf)` to prove

\[
 M_C(0)=M_l(0)+q_{\rm eff}(k_*),\qquad
 h_C=h_l(J_of)+J_lk_*+h_l(k_*).
\]

For the norm, the vector `a=h_l(J_of)+h_l(k_*)` lies in `K_l`, whereas
`J_Cf` and `J_lk_*` lie in its orthogonal complement. Moreover
`<J_Cf,J_lk_*>_rho=<f,E_ok_*>_nu=0`. Therefore

\[
 \|J_Cf+h_C\|_\rho^2
 =G+\|k_*\|_m^2+
       \|h_l(J_of)+h_l(k_*)\|_\rho^2.
\]

This is Z53 with the source's pullback convention made explicit. The last
term includes its actual cross pairing. The identities prove
`M_l(0)<=M_C(0)<=K0`, but do not imply a monotonicity statement for the
restored state norm.

Gauge transformations act on the observation by conjugating `Omega` at
its base vertex and applying the original endpoint actions to `Z`. On
prefixes they act by `g_j -> h_base g_j h_vertex_j^(-1)`.
These formulas show equivariance of the exact coordinate map. Haar
invariance and gauge invariance of the unique positive vacuum imply that
the conditional expectations intertwine the gauge actions. The original
form is invariant as well, so uniqueness makes both minimum sections
intertwine them. Consequently the entire derivation restricts to the
physical invariant subspaces, and the restored trace state is physical.

## Locatable qualifications and limitations

1. **Form-domain qualification, note lines 782–788, Z48.** The sentence says
   “arbitrary ... h in K_l” before writing two form values. If these are
   finite form values, the domain is `h in H^1 intersect K_l`, as explicitly
   stated for Z49 immediately below. Otherwise both sides require the
   extended-value closed-form convention. This is a local wording omission,
   not a failure of the subsequent bound: `h0 in Dom D_l` and the translation
   `k=h-h0 x` preserve the required form domain.

2. **Nonzero trial qualification, note lines 913–926, Z55.** The formula
   `alpha_Y=<Y,W>/q(Y)` requires a nonzero trial `Y` in the stated smooth
   kernel trial domain. Z19 then gives `q(Y)>0`. The note explicitly checks
   this for its actual `Y0` at lines 924–926, so this does not invalidate
   that application. The general sentence is not meaningful at `Y=0`.

3. **Finite-sector lower bound, note lines 793–819.** Z49 concerns
   `span{f}+(H^1 intersect K_l)`, not the entire physical centered form
   domain. Z50 gives a variational *upper* bound on the complete finite-box
   physical gap. Its direction is correct in the source. The omitted coarse
   directions are explicitly represented by `ker E_o` through Z51; they
   are not proved irrelevant by retaining the exterior.

4. **Different coupling regimes, note lines 319–321 and 981–988.** The
   coefficient enclosures at `xi=10^(-8)` occur at the original
   `g=50 sqrt(2)` and `c=1/5000`. Along the weak-coupling path Z22,
   `c_n -> infinity` and `xi_n=c_n^2/4 -> infinity`. The small-xi
   numerical coefficients therefore do not hold eventually along that
   path by the argument given. The note already separates the two domains;
   consolidation must preserve that separation and the exact dictionaries.

5. **Uncontrolled outer quantity, note lines 860–893 and 996–999.** The
   exact additional response is `q_eff(k_*)>=0`. Its uniform control and
   the corresponding complete restored-state norm on growing physical
   observation families are absent. The calculation above establishes
   an exact relationship, not the desired uniform estimate. No continuum
   physical Hilbert-space or complete positive mass lower bound is claimed.

6. **Publication scope, README 32–39 versus note 3–5 and 1015–1018.** The
   note's inherited description says its Git contribution/checker is
   self-contained, but the companion README expressly limits this branch
   to the proof and guide and says the runnable dependency set is absent.
   Read literally in isolation, the note's checker statement is not true
   of this two-file publication. The README discloses the distinction.
   Checker availability and historical execution success must remain
   distinct from the mathematical derivations in a consolidated reader.

## Source and computation checks

The vacuum/domain dependency was checked in the local original source
`yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`,
section 1. Its compact elliptic ground-state argument, positivity, gauge
invariance, and multiplication-form identity apply with exactly the Z1
operator and coefficients.

The external heat-kernel leaf was checked against the exact cited primary
version: A. Nowak, P. Sjogren, T. Z. Szarek,
[*Sharp estimates of the spherical heat kernel*, arXiv:1802.09385v2](https://arxiv.org/pdf/1802.09385v2),
dated 2 September 2018, page 2 equations (1)–(2), with the unit-sphere area
measure convention on page 1. The dimension recurrence and periodized
one-dimensional Gaussian translate using `t=theta/4`,
`p_theta=2 pi^2 K^3_(theta/4)`, and
`q_theta^5=pi^3 K^5_(theta/4)`. They give the exact derivative coefficient
`-4 exp(-3 theta/4) sin(r)` in Z7 and the prefactor in Z8. Thus this source
leaf and its measure/time translation pass; no wider novelty claim was
investigated. No third-party source file was added or changed.

Simple rational arithmetic in the response formulas was also recomputed:

\[
 \frac{3/4}{9/2}+\frac{1/4}{13/2}=\frac8{39},\qquad
 \frac{3/4}{(9/2)^2}+\frac{1/4}{(13/2)^2}
 =\frac1{27}+\frac1{169}=\frac{196}{4563},
\]
\[
 \frac34-\frac7{36}-\frac8{39}-3\frac{196}{4563}
 =\frac{337}{1521}.
\]

The Cauchy derivative step Z45 -> Z46 preserves the original disk radius
`kappa/4`, so multiplying the Z43 supremum by `4/kappa` gives the displayed
`104,000,000 xi^4` bound. This confirms the implication between the
displayed enclosures, not an independent derivation of every input to their
constant `C(xi)`.

Commands used for audit were bounded `Get-Content` line reads, `rg --files`
and `rg -n` discovery, and `Get-FileHash -Algorithm SHA256` on the note.
The primary paper was opened through the web tool at the exact version URL.
No original checker, numerical solver, source mutation, or Lean run was
performed. A separate subagent freshly derived Z51–Z53 from the raw source
definitions and form domains; its agreement is supporting review work, not
a mathematical certification by an independent institution.

## Strongest safe statement and next check

The preserved finite-regulator calculation provides an exterior-uniform
local conditional-kernel inverse, an explicit shrinking-loop weak-coupling
sequence on which that inverse tends to zero, and exact response/norm maps
to the larger Omega-only kernel. The numerical response certificate belongs
to its separately stated small-xi regime and to the historical delivery's
own proof/checker evidence record.

For consolidation, the cheapest additional verification is to locate the
complete named local-fibres archive, authenticate its source/checker and
receipt identities against the preserved note, and replay its exact checks
without relabeling that replay as independent analytic proof. The next
mathematical estimate required beyond this branch remains uniform control
of `q_eff(k_*)` and the full Z53 norm on the growing observation families;
the exact operators and maps involved have been exhibited above.


# Independent audit of the cubic source and linearized finite-box return

\begin{quote}\footnotesize
\textbf{Source classification:} independent bounded mathematical audit

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/audits/cubic_linearized.md}

\textbf{SHA-256:} \path{6ad5e5044cfdd252469736260fde013ea3881fdf2978fc9f6f126a97b7982e1a}

\textbf{Editorial provenance notice:} This review has the exact scope stated in its body. Its inclusion is not exhaustive certification of all sources or a proof of the continuum mass-gap problem.
\end{quote}


Date: 2026-09-16. Audit actor: an isolated subagent, supplied the raw source files and asked to derive the critical implications. The delivered numerical checker was read as evidence; it was not used as the definition of the mathematical objects. No imported source was edited, and no Lean process was started. This is a mathematical audit with exact finite calculations, not an external peer review or a formal proof-assistant certificate.

## Claim and primary verdict

**Verdict: proved as written**, for the central claim specified here: the original finite-box SU(2) operator C1 has the complete third logarithmic-vacuum coefficient C14–20, the bound C23, and the closed-interval physical spectral estimate L22 with the stated parameter transformation. The fourth energy coefficient C24 and the analytic remainder L29 follow from the same construction. The verdict does not extend to a continuum mass gap, historical priority, or the external bibliographical comparisons in L8.

The quantified objects are every integer L >= 2; the original edges and plaquettes contained in {-L,...,L}^3; the original product Haar probability; invariance under every vertex gauge transformation, including boundary vertices; a > 0; g > 0; kappa=2g^2/a; and x=xi=1/(4g^4). Let alpha be the first positive zero of

    D(x)=[46457856x^4+183150656x^3+18324072x^2
          -1168128x+13689]/13689.

Then, for 0 < x <= alpha, the bottom of the original physical spectrum above its unit positive vacuum obeys

    Delta_L >= kappa[(3/2)(1+sqrt(D(x)))+(1136/13)x^2].

In particular, 0.0170787544707772675 < alpha < 0.0170787544707772677 and

    3.825973052393385 < 1/(2sqrt(alpha)) < 3.825973052393386.

All norms on coefficients below are the auxiliary norms of C4; none is substituted for the physical vacuum pairing. The actual physical ground-state transform and its weighted form supply the return to the physical spectrum.

## Exact source identity and locators

Source directory:

    yang-mills/continuations/20260916-cubic-linearized/

SHA-256 identities at audit time:

| File | SHA-256 |
| --- | --- |
| CUBIC_SOURCE.md | d1e8fa24ce573ad1adfdaeecbb2ee6bfa1631717f9ce22b0f66d838981d5f240 |
| LINEARIZED_RETURN.md | 931d8d2824062c6435dfe324cb9145bc6d8e7a450d37aa5f86a94f1190190453 |
| coordinate_audit.py | de1d9841ebd4655194801cc053bc1f71393433e8c241d0d88cdae65fc82f7c9f |
| geometry.py | bd878efd339f05f320d051bee760bff0934ccfca10e9a2c1e6f26941a128cc1e |

Important locators: CUBIC_SOURCE.md lines 5–61 (operator, source, coefficient norms, spin budgets), 63–97 (loop norms and second coefficient), 113–172 (complete cubic table), 174–210 (cubic bound), 214–245 (fourth energy coefficient). LINEARIZED_RETURN.md lines 5–27 (evaluated spin budgets), 29–63 (exact residual), 65–123 (inverse, convergence, vacuum identification), 155–195 (entire physical spectrum), 211–235 (source quotients and physical defect), 237–249 (energy remainder), and 285–295 (explicit continuum limitation).

## Dependency graph

1. Original SU(2) product representation and invariant vertex tensors -> c(j)>=6j_e, total-spin bound, and physical nonconstant c(j)>=3.
2. Original trace-matrix multiplication, irreducible decomposition, and generator norm -> C6 -> bilinear bounds C7.
3. Original four-link characters and Haar edge integration -> C8–11 -> complete v_2.
4. The original Casimir product rule, quaternion harmonic decomposition, and three-spin singlet sum -> all five connected v_3 families C14–20.
5. Original loop norm bounds plus an exhaustive finite enumeration of original local incidences -> C21–23.
6. Evaluated v_1/v_2 spin budgets and v_3 -> ell and delta -> Neumann inverse and convergent Catalan correction, including the endpoint.
7. Finite-box coefficient convergence -> C^2 original source -> positive smooth original vacuum and exact ground-state form identity.
8. Original point-spin budget plus Peter–Weyl regularity of every finite-box eigenfunction -> blockwise eigenvalue inequality -> full physical form gap L22.
9. Center symmetry, Haar orthogonality, and the constructed analytic vacuum -> C24 and L29.

The leaves in this graph are internal coordinate/representation calculations, standard compact-group Fourier and elliptic facts, and the explicit finite incidence calculation. L8 literature comparisons are not dependencies of this graph and were not independently verified in this bounded audit.

## Obligation matrix

| Obligation | Status | Evidence |
| --- | --- | --- |
| Original orientations, signs and generator scaling | Passed | C1 and the exact identity K(fh)=(Kf)h+f(Kh)-2Gamma(f,h). |
| Gauge restriction and physical free Casimir floor | Passed | Endpoint intertwiner inequalities and triangle-free cubic incidence, reconstructed below. |
| Complete spin multiplicities and coefficient product bounds | Passed | Unitary decomposition, pinching, partial trace, and trace-norm duality. |
| Repeated-pair lower-spin cancellation | Passed | Exact three-channel calculation below. |
| Common-edge multiplicity space | Passed | Singlet sum uses the full total-spin-1/2 isotypic space; no false commutativity assumption. |
| All cubic support types and incidence counts | Passed | Original face geometry and a separate exhaustive finite original-coordinate enumeration. |
| Endpoint convergence | Passed | Catalan series has summable endpoint coefficients and the displayed telescoping tail. |
| Vacuum versus coefficient majorant | Passed | Direct original-operator differentiation and the full ground-state form identity. |
| Return to every physical excitation | Passed | Smooth eigenfunctions have the required weighted Fourier summability; no trial-space lower bound is used. |
| L6 conditional-kernel terminology | Passed with definition clarification | Operators must mean the operators of the respective restricted forms; the statement does not assert invariance under the full scalar generator. |
| Quartic energy sign and extensive factors | Passed | Independent Rayleigh–Schrodinger derivation below. |
| Exact interval arithmetic in L17 | Passed | Separate Fraction calculation; source checker not imported. |
| Primary-source parameter comparisons in L8 | Out of scope | Not needed for the central theorem; do not upgrade these citations from this audit. |
| Continuum existence or finite positive continuum mass | Out of scope | Explicitly disclaimed in L9; the running weak-coupling path eventually leaves this domain. |

## Independent derivation of the critical steps

### 1. Gauge spin budgets and the bilinear operation

Fix an edge e with endpoint vertices v and w in a nonzero gauge-invariant Fourier block. At v, the tensor factor of spin j_e must couple with the other incident spins to spin zero. Thus j_e is at most their sum. The same holds at w. The set A_e of all those other incident edges has total spin at least 2j_e. Their remote endpoints are pairwise distinct: otherwise either two graph edges coincide or a triangle occurs, and neither is possible in the original cubic graph. Apply the invariant-tensor inequality at each remote endpoint. Every edge outside A_e union {e} is counted at most twice. Consequently

    sum_(f in A_e) j_f <= 2 sum_(f outside A_e union {e}) j_f.

Adding j_e, the A_e sum, and its exterior sum gives sum_f j_f >= 4j_e. Every nonzero half-integer spin satisfies j(j+1)>=3j/2. Hence c(j)>=6j_e, sum_f j_f<=2c(j)/3, and any nonconstant physical block has c(j)>=3.

For multiplication, A tensor B is transformed unitarily into the irreducible decomposition. Pinching retains the diagonal irreducible blocks, and partial trace retains all multiplicity contributions. The aggregate output trace norm is at most ||A||_1||B||_1. The partial-trace estimate holds for arbitrary matrices, not only positive ones: by trace-norm duality,

    |Tr[Z Tr_m(A)]|=|Tr[(Z tensor I_m)A]|<=||A||_1

for every ||Z||op<=1. The spin-j generator has operator norm j, so a link derivative costs j. Sum all three generator indices. For an anchor in the first input union, the derivative-pair sum costs at most 3m(f)t(h); interchanging inputs covers anchors in the second union. The output Casimir weight cancels the exact nonconstant inverse Casimir. This proves C7 and its constant 2/3 without assuming an equivalence with the physical Hilbert norm.

### 2. Original second coefficient and cubic channels

The original Leibniz rule gives

    2Gamma(f,h)=(c_f+c_h)fh-K(fh)

for original Casimir eigenfunctions. A plaquette has c=3. Its square is 1+chi_1 with nonconstant c=8. For an adjacent pair the two shared-edge channels have c=9/2,13/2. Applying K^(-1)Q_H to Gamma(S/3,S/3), retaining the two ordered appearances of distinct plaquettes, gives exactly

    v_2=-(1/72)sum_p chi_1(Omega_p)
         +sum_{unordered adjacent {p,q}}[(1/27)P_0(W_pW_q)
                                         -(1/117)P_1(W_pW_q)].

For a self triple, W chi_1=chi_(3/2)+W. The multiplier in 2B(W/3,-chi_1/72) on an output Casimir c is -(11-c)/(216c). At c=3 and c=15 this is -1/81 and 1/810, respectively.

For a repeated adjacent triple, write F=(W_p^2-1)W_q and z=P_0(W_pW_q). In an original shared-edge quaternion u, write W_p=2u dot v and W_q=2u dot w, with v,w unit. The degree-one harmonic projection of (u dot v)^2(u dot w) is [u dot w+2(v dot w)(u dot v)]/6. Therefore

    H=P_(1/2)F=(4/3)W_p z-(1/3)W_q,
    J=P_(3/2)F=F-H,
    W_p z=(3H+W_q)/4,
    W_p P_1(W_pW_q)=H/4+J+3W_q/4.

The K v_3 coefficients are

    H: -1/72-1/2808-1/108=-11/468,
    J: 5/702+1/216=11/936,
    W_q: 1/72-1/72=0.

Dividing the nonzero channels by their original Casimirs 9 and 12 gives C15. The zero lower component is an actual cancellation, not an omitted support.

For a distinct path, the two inner-pair possibilities give, on channel (s,t),

    [a_s(3+c_s-c)+a_t(3+c_t-c)]/(3c),
    (c_0,a_0)=(9/2,1/27), (c_1,a_1)=(13/2,-1/117),
    c=6+2(s+t).

This produces 1/162, -11/8424, -11/8424, 1/3510 on (0,0),(0,1),(1,0),(1,1).

For a common edge, the three original spin-1/2 pair-singlet projectors satisfy

    sum_(i<j) P_0^(ij)=3/4-sum_(i<j)J_i dot J_j
                       =9/8-(1/2)J_total^2.

It therefore has eigenvalues 3/2 and 0 on the complete total-spin-1/2 and total-spin-3/2 spaces. The complementary pair-triplet sum has eigenvalues 3/2 and 3. Substitution in the same Casimir multiplier gives -2/1755 at c=15/2 and 2/2457 at c=21/2. This preserves both spin-1/2 copies and does not multiply noncommuting pair projectors.

For a cube corner, the three independent shared-edge channels give c=9/2+2n. There are 3-n pair-singlet contributions and n pair-triplet contributions. The coefficient is

    [(3-n)a_0(3+c_0-c)+n a_1(3+c_1-c)]/(3c),

which yields 2/81,34/13689,-38/17901,2/2457. At n=1 the central vertex would carry spins (1,0,0), so the gauge-invariant projection is identically zero. For n=0, integrate the original shared-edge words successively: two integrations give factors 1/2 and the last trace is conjugation invariant. The surviving boundary loop therefore has coefficient 1/4.

Disconnected triples contribute zero because their outer and inner active derivative supports do not meet, or their inner second coefficient is zero. The connected three-face adjacency graph is a path or a triangle. Original cubic geometry gives only common-edge triangles and three-face cube corners. Together with repeated faces, these are precisely the five displayed families.

### 3. Norm bounds and exhaustive original incidences

For a simple loop with ell edges and t extrema pairs relative to n_1+n_2+n_3, row/column index permutations expose ell-2t identity contractions and 2t alternating contractions. The identities each contribute trace norm 2, while each alternating contraction has its single nonzero singular value sqrt(2). Thus the trace norm is 2^(ell-t). For spin j plaquettes the same calculation gives (2j+1)^3. The particular values 8,27,64 and the six/eight-link bounds in C8–9 follow with the original edge orientations retained.

For path projections x_st, aggregate pinching gives sum x_st<=512; one shared-edge integration gives x_00+x_01<=128 and x_00+x_10<=128; two give x_00<=32. The channel-weighted absolute sum equals

    [3 sum x_st+8(x_00+x_01)+8(x_00+x_10)+20x_00]/1053
    <=1408/351.

For a corner, the all-zero channel has norm at most 8; the n=1 channel is zero; and the n=2,3 weighted absolute coefficients are at most 19/1053. This gives (19*512+98*8)/1053=3504/351. The remaining family bounds are directly 40/27,66/13,512/117.

The separate calculation file constructs each original plaquette from four endpoint pairs. It does not import geometry.py. A connected triple whose edge union contains the anchor contains an anchor plaquette p, an adjacent q, and a third plaquette adjacent to p or q. Conversely that generation produces a connected triple. Every such face lies within two face-adjacency steps of an anchor face; coordinate bases in [-3,3]^3 include every possibility. Exact set enumeration therefore exhausts the infinite-grid local problem, and finite-box clusters inject into it. The resulting counts are four anchor self triples, 42 adjacent pairs and their two repeated choices, 460 paths, 40 common-edge triples, and 24 corners. It follows that

    ||v_3||loc <=4*(40/27)+84*(66/13)+460*(1408/351)
                 +40*(512/117)+24*(3504/351)=944984/351.

### 4. Nonlinear source at the closed endpoint

The second-source budgets follow directly from the same channels: m(v_2)<=5834/39 and t(v_2)<=137/6. In particular the shared-edge spin-zero channel contributes zero to the anchor's point-spin budget. The resulting constants are

    ell=(128/3)x+(3132/13)x^2,
    delta=(944984/351)x^3+(799258/39)x^4.

These are bounds on the actual J_2=2B(q_2,.) and R_2=x^3v_3+x^4B(v_2,v_2). Expanding (1-ell)^2-(8/3)delta gives the displayed D exactly. D'' is positive for x>=0, D'(171/10000)<0, and D has opposite signs at 17/1000 and 171/10000; hence its first zero is unique in that interval, D>=0 before it, and ell<1 there.

The Neumann series of the actual J_2 is therefore absolutely convergent. After applying its inverse, the equation is w=z+C(w,w), with ||z||<=delta/(1-ell) and bilinear norm at most c_*=(2/3)/(1-ell). The binary-tree series has term bound Catalan_(n-1)c_*^(n-1)z_*^n. With theta=4c_*z_*<=1, its total equals the stated w_* bound. At theta=1, Catalan_n/4^n=2(b_n-b_(n+1)), where b_n=binom(2n,n)/4^n. The tail after N terms is bounded by

    [3(1-ell)/4]theta^(N+1)b_N.

This proves endpoint convergence directly. No strict-contraction assertion at the endpoint is needed.

At fixed finite L, the coefficient space is a finite collection of support-labelled weighted trace-matrix l1 spaces; the physical subspace is closed. Its global c-weighted sum is bounded by |E_L| times its local norm. First derivatives cost j_e<=c and second derivatives cost j_e j_f<=c, including both derivatives on one edge. Thus the source sum is C^2 on the original compact product. Direct differentiation proves H exp(v+c_L)=E_0 exp(v+c_L). Real source coefficients give a real v and hence a positive exponential. Elliptic regularity makes it smooth. The exact identity

    q_(H-E_0)(psi h)=kappa integral psi^2 sum_i |X_i h|^2

extends from smooth functions to the original form domain because multiplication and division by positive smooth psi preserve H^1. It proves that E_0 is the lowest energy and that its eigenspace is one-dimensional: equality forces all derivatives of h to vanish on the connected compact product. No gap was presumed to construct the vacuum.

### 5. Return to every physical spectral block

For the original drift D_v=2Gamma(v,.), the complete trace-norm product inequality gives

    ||D_v h||_X <=6t(v) sum_j(sum_e j_e)||A_j(h)||_1
                 <=4t(v)||Kh||_X.

The evaluated v_1/v_2 budgets and w_* give exactly

    4t(v)<=chi(x)=(1/2)(1-sqrt(D(x)))-(1136/39)x^2.

Let A f=lambda f be any actual physical eigenfunction with lambda>0, where A=psi^(-1)(H-E_0)psi. It has rho-mean zero. Then h=Q_Hf is nonzero and f=h-<h>rho. These maps are literal inverse maps on the stated centered spaces. They give

    (K-lambda/kappa)h=Q_H D_vh.

Every such eigenfunction is smooth by compact elliptic regularity. For completeness, if f_j=Tr(A_j pi_j) and d_j=dim(pi_j), Peter–Weyl gives the weighted square sum sum_j (1+c(j))^s||A_j||HS^2/d_j<infinity for every s. Since ||A_j||_1<=sqrt(d_j)||A_j||HS, Cauchy–Schwarz bounds sum c(j)||A_j||_1 by that square sum times the square root of sum c(j)^2d_j^2(1+c(j))^(-s). The latter is finite for sufficiently large s on this fixed finite product. Thus the X-norm inequalities apply to every actual eigenfunction.

For 0<lambda/kappa<3, each nonconstant physical block has c>=3, and therefore

    ||(K-lambda/kappa)h||_X
      >=[1-lambda/(3kappa)]||Kh||_X.

The drift bound forces lambda>=3kappa(1-chi). Eigenvalues already at least 3kappa satisfy that inequality automatically. Compact spectral resolution then gives the same lower bound on the entire centered physical form domain, which is exactly L22. The equality ||p_X||^2=1/Delta_L in L28 follows from the variational characterization of that first positive eigenvalue, with the original weighted gradient norm.

### 6. Fourth energy coefficient and all higher terms

In an intermediate-normalized wavefunction u=1+xu_1+x^2u_2+..., the original K-xS eigen-equation gives u_1=S/3, e_2=-M/3, and u_2=K^(-1)Q_HS^2/3. The order-three equation is K u_3-Su_2=e_2u_1; test it against S, using KS=3S. The constant order-four equation is e_4=-<S,u_3>. Together these give

    e_4=M^2/27-(1/9)<Q_H S^2,K^(-1)Q_H S^2>.

The self term contributes M/8. A distinct nonadjacent unordered pair contributes 4/6=2/3. An adjacent pair contributes

    4[(1/4)/(9/2)+(3/4)/(13/2)]=80/117=2/3+2/117.

Cross terms vanish by an odd-occurrence original edge, or by distinct spin sectors. Hence the inner product is M/8+(2/3)binom(M,2)+(2/117)J, and substitution yields e_4=5M/216-2J/1053 with its original sign and extensive factors.

The original link-center sign changes every plaquette trace, commutes with K, and preserves Haar. It sends v_n to (-1)^nv_n, so the nontrivial vacuum energy part is even. On |x|=1/60, the majorant gives ||v||loc<7/10 and |X_(e,alpha)v|<=||v||loc/6. Consequently |C_L(x)|<49|E_L|/1200. Cauchy bounds on the even coefficients and a geometric sum from order six give exactly L29. This is a bound on every omitted order, not an identification of a truncated polynomial with the exact energy.

## Conditional-kernel clarification in L6

LINEARIZED_RETURN.md:235 should be interpreted with its own phrase “closed restricted form.” For P the original vacuum conditional expectation and G gauge averaging, let K_0=ker P. The scalar operator is the operator D associated with the restriction of the weighted Dirichlet form to K_0; the physical operator is the corresponding restriction to K_0 intersect Ran G. If PG=GP and the conditional coordinate algebra is gauge stable, gauge invariance of the form makes G a reducing projection for this restricted form, so the inclusion I obeys DI=ID_phys and intertwines the corresponding resolvents. This is the exact relation that supports the text. It does not claim that K_0 is invariant under the unrestricted scalar generator A. Gauge covariance of the original conditional integrals supplies PG=GP for the original loop-observation setting; an arbitrary unspecified conditional expectation would not automatically have that property. This clarification is ancillary to, and does not weaken, the full physical spectral bound L22.

Here is the full original-coordinate proof, independently checked in a subsidiary audit. For the original loop edges V_1,...,V_ell, use the global smooth coordinates

    Omega=V_1...V_ell, g_j=V_1...V_j (1<=j<ell), Z=U_(C^c).

Their inverse is V_1=g_1, V_j=g_(j-1)^(-1)g_j for 2<=j<ell, and V_ell=g_(ell-1)^(-1)Omega, retaining the actual traversed-link inversions in V_j. Successive Haar changes of variables give product measure dOmega product_j dg_j dZ. For the observation (Omega,Z), the actual conditional integral is

    Ef(Omega,Z)= [integral f(Omega,g,Z)rho(Omega,g,Z) product_j dg_j]
                 /[integral rho(Omega,g,Z) product_j dg_j].

Under an original vertex gauge transformation a, the coordinates transform as

    Omega -> a_(v_0) Omega a_(v_0)^(-1),
    g_j -> a_(v_0)g_j a_(v_j)^(-1),

and Z transforms by its unchanged original edge action. Every fiber map preserves product Haar measure. Since rho is invariant, changing those variables proves E T_a=T_a^base E. For cylinder inclusion J, direct composition gives J T_a^base=T_a J. Consequently P=JE commutes with T_a and therefore with G. The same proof applies when the observation is Omega alone, by including Z in the integrated variables.

The coordinate transformation and rho are smooth, rho is strictly positive, and all manifolds here are compact. Differentiating numerator and denominator under the compact fiber integral, followed by Cauchy–Schwarz and finite upper/lower smooth coefficient bounds, proves that P preserves smooth functions and is bounded on H^1. Thus (I-P)C^infinity is dense in H^1 intersect K_0; G(I-P)C^infinity is dense in its physical part. The corresponding restricted forms are densely defined and closed. This resolves the domain point needed for their self-adjoint associated operators.

Let q denote the original weighted Dirichlet form. Gauge invariance implies q(Gu,v)=q(u,Gv). For u in Dom(D_phys) and v in H^1 intersect K_0, the defining form identity gives

    q(Iu,v)=q(u,Gv)=<D_phys u,Gv>rho=<I D_phys u,v>rho.

The characterization of the operator associated with q restricted to K_0 proves Iu in Dom(D) and DIu=I D_phys u. Conversely, testing the defining identity for D only against physical vectors proves

    Dom(D_phys)=Dom(D) intersect K_phys.

It follows that the physical part reduces D and

    (D+s)^(-1)I=I(D_phys+s)^(-1)

whenever those inverses exist. At zero shift, every h in K_0 has rho-mean zero, and the original compact scalar Poincare inequality with smooth positive rho ensures the scalar inverse exists. For the physical part, L22 gives D_phys>=kappa d(x), so

    ||D_phys^(-1)r||rho <=||r||rho/[kappa d(x)],
    q(D_phys^(-1)r,D_phys^(-1)r)<=||r||rho^2/[kappa d(x)].

The corresponding gradient primitive norm is bounded by 1/sqrt(kappa d(x)); its square is the inverse-gap bound in L28. Thus the distinction between the primitive norm and its square is retained.

The exact relation to the unrestricted original transformed generator is instead

    u in Dom(A) intersect K_0 => u in Dom(D), D u=(I-P)A u.

There is no assertion here that P commutes with A. The antecedent definition explicitly uses this form compression: yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md:306–314. This subsidiary check did not change imported source files.

## Computation and verification scope

Separate calculation:

    python yang-mills/consolidation/20260916/audits/cubic_calculations.py

The script imports no supplied code. It uses exact Fraction arithmetic for channel coefficients, the cubic norm sum, D(1/64), endpoint signs, and rational squared comparisons for the g^2 bracket. It reconstructs plaquettes as endpoint-pair edges and exhaustively counts local connected triples. Its output is saved as cubic_calculations.json.

The supplied coordinate_audit.py itself samples selected motifs in its direct entry point; verify.py is the separate driver responsible for the claimed 612-multiset exhaustive finite geometry regression. Even two exact assignments per support are not a polynomial-identity proof. The universal identities above follow from the full Casimir, Haar, and spin arguments; the finite source-checker assignments are additional regressions. Fresh replay of the full supplied checker is recorded separately in ../VALIDATION.md.

## Strongest supported content and remaining scope

No counterexample or failed implication was found in the central finite-box cubic/linearized proof, and the critical implications have been reconstructed above. The supported statement is the explicit strong-coupling finite-box theorem, uniform in L through its original kappa=2g^2/a factor, with the analytic vacuum and energy estimates. It does not construct a nontrivial continuum field or a finite positive continuum mass. The asserted running path with positive beta eventually violates x<=alpha exactly as L9 records.

For consolidation, retain the raw files and their hashes, include the exact finite-check outputs as computational evidence, and keep the literature-comparison and continuum labels separate from the proved finite-box result. The cheapest useful additional verification is the already-assigned full supplied-checker replay; this audit does not require a new mathematical assumption or a human approval gate.


# Yang–Mills artifact checker scope — static inspection, 2026-09-16

\begin{quote}\footnotesize
\textbf{Source classification:} executable-check scope and reproducibility review

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/audits/checker_scope.md}

\textbf{SHA-256:} \path{1a624bdd0b6ec507af8f50f3f67d97bbc87161c1da5c8e89800bba54fc9677e3}

\textbf{Editorial provenance notice:} This review has the exact scope stated in its body. Its inclusion is not exhaustive certification of all sources or a proof of the continuum mass-gap problem.
\end{quote}


This report records read-only inspection of delivered source code and historical receipts under `work/ym-web-artifacts-20260916`. No bundled Python source was executed and no original artifact was edited by this subaudit. Fresh replay results belong to the parent audit. The computation-audit skill was used to distinguish exact finite assertions from the mathematical claims they accompany. Historical bundled instruction files were treated as source data.

## Receipt counts and arithmetic

| Continuation/checker | Historical positive checks | Negative controls | Arithmetic |
|---|---:|---:|---|
| Gauge-native band | 642 | 27 | Integers, `fractions.Fraction`, sparse polynomials over Q; explicit Q(sqrt(2)) and Q(sqrt(354)) pairs; rational square-root enclosures |
| Uniform gap / zero shift | 273 | 35 | `Fraction` matrices and sparse Q-polynomials imported from hash-pinned predecessors; exact principal-minor PSD tests; rational outward endpoints |
| Actual loop moments | 134 | 12 | Sparse polynomials in 12 original quaternion coordinates over Q, integer incidence, rational Haar moments and error endpoints |
| Cubic / linearized | 2246 | 15 | Integer incidence, `Fraction` quaternion evaluations and projectors, rational polynomial evaluations and bisection |
| Research-control | 56 | 17 | `Fraction` matrices |
| Coupled response | 189 | 12 | `Fraction` matrices; complex matrices represented as pairs of rational matrices |
| Vacuum / refinement / infrared | 181 | None recorded | Exact SymPy integer, rational, complex and symbolic expressions |

Check counts are named aggregate assertions, not counts of all individual identities or an independently established theorem count. Each may contain many scalar comparisons. The vacuum JSON is a summary, not a literal full checker-output receipt.

## Gauge-native band

Authoritative inspected files: `yang_mills_gauge_native_continuation/yang-mills/continuations/20260915-gauge-native-band/{verify.py,verification.json,BOX_L2_CERTIFICATE.json,execution.json}`.

- `graph_spin_checks` exhausts all 3^12 = 531441 edge-label assignments on the original unit cube, with q_e = 2j_e in {0,1,2}; vertex parity and triangle inequalities accept 1013. Six accepted assignments have Casimir 3 and are precisely the six original face supports. This is a bounded label census, not all representations on all boxes. Original open-box counts and incidences are checked at L = 1,2,3,4 for vertices in [-L,L]^3.
- The fundamental plaquette coefficient is constructed as a 16 by 16 integer matrix; its Gram polynomial and trace norm 8 are checked. Eight deterministic rational majorant fixtures use all six face loops with spins 1/2,1,3/2 (18 records per fixture). These are examples of the written norm estimate.
- Catalan convolution is checked for n = 1,...,50, endpoint-tail identities for P = 0,...,80, and exact full partial-plus-tail mass for P in {1,3,12,80}. The source root identity is evaluated at s in {1,4/5,3/5,2/5,0}. Cauchy quantities are returned exactly: B = 6713/39875 and B*320^3 = 1759772672/319.
- Sparse Q-polynomial Haar calculations on three S^3 factors retain 12 coordinates. Adjacent channels have Casimirs 9/2,13/2, squared norms 1/4,3/4 and shifted resolvent weight 8/21. Complete pair-channel band matrices are constructed on boxes [0,1]^3, [-1,1]^3 and [-2,2]^3, with 6,36,240 faces; all unordered pair parity signatures are checked. Degree bounds use d = 0,...,12; boundary formulas use even m = 4,...,40.
- Spatial fixtures test weighted mean deviations for n = 1,...,14, drift rows p = 1,...,64 and all 27 points of {0,1/2,1}^3 for the three-component Bloch symbol. Matrix intertwining fixtures have dimensions four and two. Resolvent/dissipation fixtures use two three-entry Casimir lists, epsilon in {1/10,3/10,1/2}, h in {1/100,1/5,1}, and kappa = 7/5. Two-state Markov fixtures use eta in {0,1/8,1/4,1/2}, xi in {0,eta/2,eta}, x in {0,1/5,3/4,1}; source-coupling series comparisons stop at order 30.
- The L = 2 box certificate uses the exact 240 by 240 signless face-adjacency Laplacian. A positive integer power vector after 100 iterations gives rational Collatz bounds. Fraction-free elimination of Q-21I executes 2303960 exact divisions and records inertia (1,239,0). The final all-order error evaluation is at xi = 10^-10, g^2 = 50000, kappa = 100000/a, returning a safe first-gap second-coefficient interval [-0.5833,-0.5656]. The error inequality used there comes from the written analytic argument.
- The second-source section checks an 81 by 81 spin-one plaquette coefficient matrix; all 20 six-edge words with three positive and three negative traversals give 64 by 64 matrices. Pair-anchor counts use L = 1,2,3. Generating coefficients are checked through order 60, endpoint tails through P = 35. Explicit Q(sqrt(354)) arithmetic verifies the proposed second-source root and factorization. Benchmark g^2 values are 17/4,5,9/2; the receipt reports critical xi = 3/[4(32+sqrt(354))] and second-source bound 236.
- Square-root brackets use a 10^40 denominator. The physical numerical return at xi = 10^-8 retains g^2 = 5000 and kappa = 10000/a. Historical replay records 28 executions, of which 20 are named CLI corruption rejections, and ordinary/optimized equality.

## Uniform gap / zero shift

Files: the same package's `continuations/20260915-uniform-gap-zero-shift/{verify.py,verification.json,execution.json}`. Hash-pinned imports are actual-loop `verify.py`, its research note and research-control `check.py`.

- Spin bounds test j = n/2 for n = 1,...,80. Anchored norm fixtures use all seven nonempty subsets of three labels and 18 deterministic assignments; Hessian fixtures have n = 1,...,9; support-weight inequalities use m = 1,...,80.
- Catalan terms cover n = 0,...,39; seven fixed-point iterates and tail cutoffs P = 1,...,7 are checked, with finite tail sums ending at p = 29. Connected-label algebra uses i,j = 1,...,9. The initial source endpoint is xi = 1/16384.
- Gamma2 identities are symbolic polynomial checks for two specified pairs (u,f) on two original S^3 factors with six vector-field indices. They are not an exhaustive family of test functions. Zero-shift source/response identities use the literal three-quaternion polynomials and return coefficients 8/39 and 196/4563.
- Raw residual fixtures use a three-dimensional kernel, two observations and a five-dimensional full block. Positive shifts are 1/10,1,5/2; PSD is tested by every principal minor of each stated matrix. Volume fixtures are three-dimensional matrix comparison, seven Neumann partial sums, three fixed four-element cluster seeds at orders 1,...,6 on label sets {0,...,6} and {0,...,9}, and eight time-ordered partial sums of a two-dimensional drift matrix. Exponential-tilt examples use p in {1/7,2/7,1/2,5/7}, ratio r in {3/2,2,5}.
- The optimized plaquette coefficient uses a 16 by 16 rational matrix and four cyclic assignments of four specified rational unit quaternions. Auxiliary norm comparisons use 1 <= m <= n <= 11; sharp support weights use m <= 80 and distance d = 0,...,7. Energy-count examples use L = 2,3,4,10,50.
- The heat-bath calibration is one four-point probability law with weights (10,11,11,10), two noncommuting conditional projectors and exact full weighted PSD tests. Poisson-rate identities use N = 1,...,8. These finite calibrations do not execute a lattice vacuum.
- Numerical error returns use xi = 10^-8, g^2 = 5000, kappa = 10000/a. Pi is bounded using 55 arctangent terms at 1/5 and 16 at 1/239; the exponential majorant uses 30 terms and an explicit geometric tail. Square roots use the imported 10^50 enclosure, and selected source square roots use 10^30. Final receipt domain is g^2 >= 15, xi <= 1/900; stronger subdomain g >= 4. Historical replay contains seven successful executions and 18 CLI rejections.

## Actual loop moments

Files: `yang_mills_actual_loop_moments/yang-mills/continuations/20260915-actual-loop-moments/{verify.py,verification.json,execution.json}`; identical predecessor bytes are present in the gauge-native package.

- Exact symbolic checks retain (u0,...,u3,a0,...,a3,b0,...,b3), quaternion multiplication, derivatives with generators of size 1/2, the three sphere relations and Haar integration. They test the displayed shared-link force, Casimir and Hessian identities, and trace moments of degrees 2,4,6. Bracket tests act on the scalar coordinate of each of three factors for three cyclic generator pairs.
- Geometry enumerates square loops of side 1,...,12, lengths 4,...,48. Side one has 12 one-edge neighbors, support size 32 and 66 pairwise cross witnesses; sides >=2 have 4*ell-8 one-edge neighbors, four two-edge neighbors and support size 9*ell-8. Every exterior-face pair gets an explicit unmatched-edge witness. The leading moments of the elementary loop are (1,5,103/4); orders 0,1,2 are checked for every side.
- Further fixtures include a two-coordinate residual correction and the three-dimensional adjoint Casimir. Rational arithmetic evaluation occurs at xi = 10^-8, g^2 = 5000, kappa = 10000/a, using the pi, square-root and exponential enclosures described above. Returned response center is 28/165 with radius 0.0000075 times kappa*xi^2; restored center is 796/27225 with radius 0.0000021 times xi^2.
- The trial-energy enclosure (3 +/- 5/10^13)*kappa is an upper bound on the full gap via a trial state, not a lower bound. Historical execution data records four successful and six deliberately failed current-checker executions, plus ordinary/optimized coupled-response predecessor replay.

## Cubic / linearized

Files: `yang_mills_cubic_linearized (1)/yang-mills/continuations/20260916-cubic-linearized/{geometry.py,coordinate_audit.py,verify.py,verification.json,execution.json}`.

- Anchored geometry exhausts 42 adjacent pairs and 524 distinct connected triples: 460 paths, 40 common-edge triples and 24 corners. Adding four self triples and 84 repeated triples gives 612 anchored multisets. Open-box enumeration uses L = 2,3,4, returning (faces,pairs) = (240,1128),(756,3852),(1728,9168).
- **The main cubic coordinate check is finite evaluation, not a symbolic identity proof:** it evaluates each of 612 multisets at seeds 1 and 7 only, with a deterministic assignment drawn from 26 rational unit quaternions (the 24-cell plus two specified fifth-denominator points). Thus there are 1224 exact evaluations. Receipt nonzero counts are self 4, repeat 108, path 879, common 59, corner 38. Additional harmonic projection checks cover all 42 repeated pair motifs and all 40 common-edge triples, each at one specified assignment; two disconnected examples are tested. Several negative controls search at most 20 seeds or stop at the first usable motif.
- The 24-cell moment check exhausts all four-variable monomials of total degree <=5 (126 monomials). Three 8 by 8 pair-singlet projectors and their sum are checked exactly, including rank four and noncommutativity. Source-channel scalar recurrences check all four path spin combinations, four corner channels and two common-edge channels.
- Cubic bound 944984/351 and quartic residual 799258/39 are exact rational budget evaluations. Quartic expansion equality is sampled at x = k/1000, k = 0,...,29. Root enclosure starts at [17/1000,171/10000] and uses 150 rational bisections; it reports xi in [0.0170787544707772675,0.0170787544707772677], g^2 in [3.825973052393385,3.825973052393386]. Benchmark xi values are 1/64,1/60,10^-8, with square-root brackets of denominator 10^28. Catalan tail identities use N = 1,...,49.
- The independent single-plaquette eigenvector recurrence stops at formal order six and spin index k = 6 (j = k/2), returning E = (0,0,-1/3,0,5/216,0,-289/77760). It does not diagonalize the full lattice operator. Fourth-energy scalar checks include arbitrary (M,J) pairs (1,0),(2,1),(240,1128),(882,3816); the final pair is an algebra fixture, not the L = 3 geometry reported above. Historical replay contains 16 executions and reports ordinary/optimized equality and predecessor replay.

## Inherited checkers

- **Research-control:** six-point probability weights w_i = i/21, i = 1,...,6; a six-vertex weighted graph at shift 2/3; partitions 6 -> 3 -> 2; rectangular 6 by 3 fixtures; empty observation; three conditional Cauchy–Schwarz checks. Twenty coefficient cases use b in {1,2,4,8,16}, xi in {1/128,1/64,1,7}. A four-dimensional polynomial observation fixture, Collatz substitutions q in {-2,0,1,3,5} and rare-fiber weights (1/100,1/100,49/50) are included.
- **Coupled response:** D = ((3,1,0),(1,4,1),(0,1,2)), G = ((2,1),(1,3)), W = ((1,2),(0,1),(2,-1)); full block dimension five. Shifts 1/4,2/3,2 each use trial dimensions 0,1,2,3. Moments W^T D^j W use j = 0,...,4; a 4 by 4 moment matrix has rank three. Complex points are z = 1/3+2i/3 and w = -1/2+3i/4. Geometric truncations n = 0,...,4 use s in {1/4,1,2}, sigma = 2; zero-energy forcing uses s in {1/10,1,2}. Twelve coefficient cases use b in {1,2,8}, a in {1/2,2/3}, g^2 in {1/5,2}.
- **Vacuum / refinement / infrared:** 61 SU(2)/scaling, 11 conditional-density, 65 Schur/infrared and 44 Walsh checks. Chain lengths b = 1,...,4 use four fixed rational links. One torus fixture has density rho = 1+cos(w)cos(z)/3 and observable sin(w)+cos(z), with exact Haar integrals. One 4 by 4 Schur fixture has kernel energies 2,5; infrared cutoffs are 1/2,2,3,5,7 and shifts 1/3,1,4. Derivative identities cover r = 1,...,8 with symbolic positive s,lambda; one symbolic endpoint limit places mass 3/(7n) at energy 1/n. Walsh configurations are exhausted for n = 2,...,6 but only the four characters empty,{1},{n},{1,n}; pullback examples use n = 2,...,5. PSD tests use all principal minors.

## Limitations and implementation observations

1. These checkers neither compute an interacting Yang–Mills vacuum nor prove a continuum mass gap. Their own receipts explicitly deny formal or independent certification of the accompanying analytic proofs. Strong-coupling domain labels and spectral return labels in JSON do not supply those proofs. Exact finite identities, sample values, and code-exit statuses must retain their stated scopes in consolidation.
2. **Windows path serialization:** research-control uses `str(p.relative_to(ROOT.parent))` for `local_inputs`; uniform uses `str(p.relative_to(YM))` for `predecessor_sha256`. Windows emits backslashes while the archived receipts use forward slashes. Exact receipt comparison can therefore fail despite source-byte identity and successful finite checks. Preserve originals; report or repair portability separately in any derived runner.
3. **Windows output serialization:** actual-loop, uniform, cubic and several inherited scripts use text stdout, while historical replay scripts compare raw stdout with archived LF bytes. Default Windows newline translation can cause byte differences. Gauge-native uses binary stdout and avoids that particular issue. This is a static portability finding; the fresh replay audit must determine actual observed behavior.
4. Research-control validates source-pin syntax; source bytes are checked only when `--source-cache` is supplied. Its archived receipt has `cached_sources: []`. `compare_intake` checks changes/removals of watched revision keys, ignores newly added keys, and does not query remote revisions. Coupled-response parent-pin validation runs before its main exception handler, so a pin failure can have a different error envelope.
5. Vacuum verification has `--output` but no receipt comparison option or negative-control suite. Its archived summary omits the 181 names and adds historical predecessor status. Do not present the summary as a byte-replay target for the full output.
6. The static inherited subaudit found matching SHA-256 values for all 12 inspected local inputs/receipt files. That is byte agreement, not fresh execution. No obvious false identity was identified in the stated finite fixtures during static inspection; this is not an independent implementation proof.
7. Cubic central-sign expressions `(-1)**negative_integer` can briefly produce Python floats +/-1; these values are exactly representable, so no demonstrated rounding defect follows. Gauge-native matrix multiplication initializes accumulation with `Fraction(0)`, retaining exact rational trace divisions. Matrix helper methods often rely on controlled fixture shapes. No numerical tolerance, random vacuum sampling or hidden adaptive truncation was found in the principal verification code.


\part{Reader production record}

# Reader rendering record

\begin{quote}\footnotesize
\textbf{Source classification:} editorial rendering record

\textbf{Repository source:} \path{yang-mills/consolidation/20260916/reader/RENDERING_ERRATA.md}

\textbf{SHA-256:} \path{e9545870846c1b304af2f26672cf457fed9849c3c0e9efce84333cb6da5dd346}
\end{quote}


This record describes presentation changes made only in the generated reader.
The original mathematical Markdown files remain byte-for-byte unchanged and
are identified by their source SHA-256 hashes in `CHAPTER_MANIFEST.json`.

## B32: repair of malformed TeX in the displayed adjacency sum

Source: `yang-mills/continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md`, equation B32.

The source contains the following malformed TeX substring. Its line break is
shown explicitly in this literal block:

```text
p\ {
m in\ plane}\p\sim q
```

The generated TeX renders that substring as:

```tex
p\ {\rm in\ plane}\\p\sim q
```

Thus the summation subscript is displayed on two lines: the plaquette is in
the stated plane, and it is adjacent to the external plaquette. This is the
index set specified by the surrounding compression and complementary-coupling
formula. No coefficient, operator, sign, adjacency condition, or mathematical
claim is changed. The bounded gauge-native audit independently records this
same source-formatting defect. The assembled Markdown retains the malformed
source string; the repair occurs only in the Pandoc presentation tree.

## Typographic treatment of retained source formulas

Original TeX display formulas are scaled down only if they exceed the available
line width, with their original equation tags retained. Whitespace that would
create an empty paragraph inside a boxed equation is removed during rendering.
Comma-separated inline coefficient lists may break across lines inside table
columns. Original plain-text formulas are retained as plain text, with line
wrapping in monospaced blocks and long inline literals. Wrapping inserts no
mathematical operation, renaming, or coordinate change.

The generated TeX is editable and the builder is rerunnable. The chapter
manifest is the authority for which source version each chapter reproduces.

