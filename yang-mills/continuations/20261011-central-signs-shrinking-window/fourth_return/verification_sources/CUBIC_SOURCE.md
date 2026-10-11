# The complete connected cubic vacuum source in original SU(2) link coordinates

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
