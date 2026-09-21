# Sixth logarithmic vacuum source: complete original coefficients, scalars and signed derivatives

18 September 2026. Continuation of the cumulative text edition dated 17 September. The objects below are the original finite open SU(2) lattice Hamiltonian and its Taylor coefficients. The earlier source and coefficient files are preserved. In particular, the independent-session report's limitation concerning independent recertification of the historical volume-uniform gap arguments remains in force. This note establishes finite coefficient identities. `EIGHTH_ENERGY.md` and `RESPONSE_AND_REMAINDER.md` supply new energy calculations and a separate, explicitly finite-volume analytic return.

## S1. Original graph, operator, scalar and pairing

Fix L>=2. Vertices are n in {-L,...,L}^3; the positive edge e=(n,i) runs from n to n+e_i whenever both vertices occur. All contained elementary faces p=(n;i,j), i<j, occur with

    W_p=tr[U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)].       (S1)

An inverse traversal always uses that same original link variable. The generators, vector fields, Haar pairing and kinetic operator are

    T_alpha=-i sigma_alpha/2,
    X_e,alpha f=(d/dt)f(...,exp(t T_alpha)U_e,...) at t=0,
    <f,h>_H=int conjugate(f)h dU,
    K=-sum_(e,alpha) X_e,alpha^2.                               (S2)

Here dU is the original product Haar probability measure. Physical functions are invariant under every vertex transformation U_e -> h_s U_e h_t^(-1), including all boundary vertices. Independent original face parameters give

    H(x)=kappa K+kappa sum_p x_p(2-W_p),
    kappa=2g^2/a,  a,g>0,
    x_p=xi=1/(4g^4) on the original homogeneous line.            (S3)

The original unit vacuum and its energy are written

    psi_x=exp(v(x)+c(x)),    P_H v=0,
    c(x)=-1/2 log int exp(2v(x))dU,
    E_0(x)=kappa[2 sum_p x_p+e(x)].                            (S4)

The function c and the scalar 2 kappa sum x_p are retained. On real parameters sufficiently close to zero, the analytic rank-one ground branch and its positive eigenfunction are constructed in `RESPONSE_AND_REMAINDER.md`, A1–A3. Its analytic finite-degree coefficients are the objects calculated here.

Put Q_H=1-P_H and

    Gamma(f,h)=sum_(e,alpha)(X_e,alpha f)(X_e,alpha h),
    B(f,h)=K^(-1)Q_H Gamma(f,h).                               (S5)

The inverse in S5 is on the actual zero-Haar-mean physical coefficient image. Integration by parts and the original eigen-equation yield

    Kv=sum_p x_p W_p+Q_H Gamma(v,v),
    e(x)=-P_H Gamma(v,v).                                     (S6)

Write v=sum_(nu!=0) v_nu x^nu in ordinary monomial coefficients, without divided-power factorials. The equations are

    v_(e_p)=W_p/3,
    Kv_nu=Q_H sum_(0<mu<nu) Gamma(v_mu,v_(nu-mu)),
    P_Hv_nu=0.                                               (S7)

Every multiindex and every ordered split occurs. On the homogeneous line the complete sixth coefficient is

    v_[6]=2B(v_[1],v_[5])+2B(v_[2],v_[4])+B(v_[3],v_[3]).      (S8)

The factor two is the explicit pairing of the ordered indices (i,j) and (j,i) in the symmetric bilinear map Gamma. The two occurrences of the degree-three input remain ordered inside B(v_[3],v_[3]).

## S2. Exact differential and Casimir maps

For the specified Pauli matrices, direct multiplication gives

    sum_alpha tr(T_alpha A)tr(T_alpha B)
       =-tr(AB)/2+tr(A)tr(B)/4,
    sum_alpha T_alpha A T_alpha=-tr(A)I/2+A/4,
    -sum_alpha T_alpha^2=3I/4.                                (S9)

An occurrence of U_e differentiates to T_alpha U_e and an occurrence of U_e^(-1) to -U_e^(-1)T_alpha. The product rule over every occurrence and S9 calculate Gamma and K on complete original trace words. These formulas are the declared inherited `trace_algebra.py` dependency; all shared-edge terms are retained.

The coefficient words are represented using the literal matrix identities: cyclicity of trace, tr(U^(-1))=tr(U) for U in SU(2), cancellation of an adjacent U_e U_e^(-1), and

    tr(U^n)=tr(U)tr(U^(n-1))-tr(U^(n-2)),                       (S10)

which follows by multiplication of U^2-tr(U)U+I=0. Their coordinate kernels are checked in S4 rather than treating a nonempty trace expression as automatically nonzero.

For an original face multiset nu, let r_e count all occurrences of its original edge e. Its complete finite coefficient representation lies in the tensor products with edge-spin lists

    j_e=r_e/2,r_e/2-1,...,(r_e mod 2)/2.                       (S11)

At each original vertex an invariant tensor requires integral total spin and max(j_e)<=sum_(f!=e)j_f. These tests include every actual invariant representation, with its multiplicity. The resulting candidate values

    c=sum_e j_e(j_e+1)                                        (S12)

are stored in each source row. Extra candidates would only add interpolation nodes; none of the actual values is removed.

For their distinct positive values define

    q_C(t)=product_(c>0)(1-t/c),
    f_C(t)=(1-q_C(t))/t-q_C(t)sum_(c>0)1/c.                    (S13)

The numerator 1-q_C has zero constant term. Substitution proves f_C(0)=0 and f_C(c)=1/c for each positive candidate c. The original Casimir action thus proves on this coefficient space

    K f_C(K)=Q_H.                                             (S14)

The zero-Casimir space consists of constants: its energy is int sum|Xf|^2, so every link derivative vanishes. Consequently f_C(K) selects the unique solution of S7 with its original zero Haar mean. The finite spin list is the list of one Taylor coefficient. No projection of the full Hamiltonian onto a finite spin space is performed.

## S3. Complete sixth-order geometry and original coordinate transports

The input is the entire fifth-degree catalogue. Extend each of its original coordinate representatives by one repeated face or one face sharing an original edge, then take its explicit signed-permutation/translation representative. This covers every connected sixth multiset. Indeed a repeated occurrence can be removed; when all faces are distinct, removal of a leaf from a spanning tree of the face-adjacency graph leaves a connected lower multiset. Induction reaches the one-face source.

Every signed coordinate operation is retained as

    y_i=s_i x_(pi(i))-d_i,
    x_(pi(i))=s_i(y_i+d_i),   s_i in {-1,1}.                    (S15)

An original edge goes to the corresponding target edge, or its inverse traversal when the positive orientation reverses. The face word is carried to its target word up to cyclic starting point and reversal, whose traces agree by S9–S10. Variable permutation and inversion preserve product Haar measure. Left and right link Casimirs coincide, so the same operation intertwines K and Gamma.

Each representative is returned to every original multiset containing the anchor edge (0,0,0;0). For a signed image of the representative, translate each positive axis-zero edge to that actual anchor. Duplicates are removed by equality of the complete original face multisets, retaining a specified inverse witness. This enumerates precisely all placements: any placement sends a representative edge to the anchor and therefore occurs in this list. Distinct representatives cannot share an original multiset, since S15 is invertible. No factorial or orbit-size division changes a coefficient.

The complete counts are:

| Original multiplicities | Representatives | Anchored multisets |
|---|---:|---:|
| 6 | 1 | 4 |
| 5+1 | 2 | 84 |
| 4+2 | 2 | 84 |
| 4+1+1 | 19 | 1,572 |
| 3+3 | 2 | 42 |
| 3+2+1 | 31 | 3,144 |
| 3+1+1+1 | 171 | 27,676 |
| 2+2+2 | 9 | 524 |
| 2+2+1+1 | 268 | 41,514 |
| 2+1+1+1+1 | 2,075 | 469,360 |
| 1+1+1+1+1+1 | 4,650 | 1,295,136 |
| Total | 7,230 | 1,839,140 |

Every witness and the original anchored-multiset digest are in `generated/geometry_sixth.json`. `geometry_core.json` is its explicitly indexed view omitting only the large placement lists; it supplies the same coefficient representatives to the worker processes.

The original graph cycle ranks |E|-|V|+1 have distribution

    1:1; 2:6; 3:59; 4:436; 5:2056; 6:4550; 7:121; 8:1.        (S16)

Representative 1906 retains eight independent original chords. All eight enter the coefficient and identity calculations.

Disconnected coefficient supports vanish by S7: its nonzero lower sources have connected face support; two factors in different edge-adjacency components have no common differentiated link, hence Gamma=0. The enumeration therefore covers every nonzero sixth coefficient in every original open box. Boundary return selects exactly the multisets whose original faces are contained in that box.

## S4. Complete tree/quaternion polynomial identities

On each original connected edge union choose the tree obtained by processing its stored edges and accepting each edge that joins two components. Root it at its smallest original vertex. Let t_v be its ordered original tree-path holonomy. For each chord e=(s,t), retain

    Z_e=t_s U_e t_t^(-1).                                     (S17)

The full map from original links to (original tree links, all Z_e) has inverse

    U_e=t_s^(-1)Z_et_t on chords,
    original tree links unchanged.                            (S18)

Both identities follow by substitution. Left/right Haar invariance on each chord and Fubini prove the exact product measure return. The gauge transformation h_v=t_v makes every tree link I. Residual simultaneous conjugation of all chords remains; it removes no chord coordinate.

For every chord c use

    Z_c=x_(c,0)I-i sum_(a=1)^3 x_(c,a)sigma_a,
    sum_(a=0)^3 x_(c,a)^2=1.                                  (S19)

The target is the original coefficient algebra

    A_S=Q[x_(c,a)]/(sum_a x_(c,a)^2-1 for every original chord). (S20)

Its stored polynomial remainder has exponent zero or one in each x_(c,0); the three remaining exponents are retained. The defining monic relations involve different leading variables, so the reductions commute. The original trace algebra maps to A_S by S17–S19 and ordinary quaternion multiplication. Its inverse on the physical-function image substitutes the original Z_e(U).

For completeness, this target is faithful on those functions. A remainder is linear in x_(c,0). Evaluating at both signs of sqrt(1-|y_c|^2), with y_c in the open three-ball, forces both coefficients to vanish on that ball. Iterating over every chord forces the remaining polynomials to vanish on a product of open balls; their coefficients are all zero. Therefore the ideal in S20 is exactly the polynomial relation ideal relevant to these original functions. A zero complete target polynomial proves a zero original physical function, with its source expression and support retained.

For the compiled evaluation, the original free-group map sends each tree-edge letter to 1 and each original chord letter to itself. Its section inserts the chord letters, and their composite on the chord free group is the identity. The word evaluation square commutes with S17–S19: deleting a tree letter substitutes its identity matrix; cancelling adjacent inverse letters uses U U^(-1)=I in the sphere coefficient ring; trace cyclicity and tr(U^(-1))=tr(U) follow from the original determinant-one matrix identity. Every original chord remains a separate generator. The target coefficient at exponent a is exactly sum_m c_m Phi(m)[a] in either evaluation implementation. The compiled program accumulates that same finite rational sum and caches the same chord-word image. Selected output comparisons, including the cube and eight-chord examples, are byte-identical; the complete current replay uses this explicit factorization.

The eighth-chord test retains the actual specialization A_8 -> A_7 given by Z_last=I and the section A_7 -> A_8 inserting the other seven original coordinates. On representative 1906, a specified rational unit-quaternion assignment gives the nonzero difference

    64707599699535109/123037171363830566406250000.

The original and specialized values, all eight quaternion coordinates and their complete map are stored in `generated/eight_chord_witness.json`. Thus the retained coordinate participates in the actual coefficient; its specialization is recorded as a map with a concrete changed value.

The complete source catalogue contains 347,653 rational trace monomials. Every original trace coefficient is delivered in `generated/sixth/0000.json` through `7229.json`. The polynomial audit actually expands every source and its complete residual in S20. Its output stores the coefficient count and SHA-256 of each full sorted expansion, the exact scalar, all signed identities, and the original source-file hash. The full quaternion expansions are additionally exposed for the single-face, closed-cube and eight-chord examples. The complete original trace polynomials and executable map suffice to regenerate every other expansion without accepting any stored digest as a proof.

The audit integrates each full coefficient independently in the chord spheres. For a single original Haar sphere,

    int x^a =0 if any a_i is odd,
    int x^a =product_i (a_i-1)!! / product_(j=0)^(|a|/2-1)(4+2j)
       for every even exponent vector a.                     (S21)

This follows from rotation invariance, sum_i x_i^2=1, and the resulting moment recurrence (equivalently its elementary Gaussian radial integral). Independent chord measures multiply. Every sixth coefficient has exactly zero original Haar mean under this calculation.

## S5. Original sixth scalar and every signed derivative

For degree six the actual raw equation is

    Kv_nu-r_nu=e_nu 1,
    r_nu=sum_(0<mu<nu)Gamma(v_mu,v_(nu-mu)),
    e_nu=-P_Hr_nu.                                            (S22)

The audit retains this scalar before projecting. Its nonzero values reproduce the independently calculated sixth energy: -289/77760 for one face six times; 22285/47309184 for one adjacent 4+2 multiplicity; -4909/118272960, 244/4312035 and -212/542997 for doubled path/common-edge/corner triples; and -83/1944 for the six distinct faces of a cube. All other classes have scalar zero. Each stored raw trace residual is mapped through S17–S20 to its exact displayed constant. Nonempty trace-relation representatives remain in their original rows.

For a distinguished original face p and |rho|=5 define

    Z_(p,rho)=(rho_p+1)v_(rho+e_p).                            (S23)

Differentiating S6 in the same original source coordinate gives

    KZ_(p,rho)-2sum_(0<mu<=rho)
       Gamma(v_mu,Z_(p,rho-mu))
       =(rho_p+1)e_(rho+e_p)1.                               (S24)

Applying Q_H makes the displayed scalar zero at its receiving support; its value is retained upstream. There are 40,221 specified (representative, face-direction) equations.

The two audit implementations prove S24 by equivalent explicit routes. The first expands every signed residual in S20. The second independently assembles the same raw signed RHS and checks the complete trace-coefficient identity

    signed_RHS=(rho_p+1)r_(rho+e_p).                           (S25)

It then carries that exact scalar multiple through the already evaluated full source polynomial. To prove S25 algebraically, put nu=rho+e_p, pair the ordered terms mu and nu-mu using symmetry of Gamma, and add their distinguished exponents: mu_p+(nu_p-mu_p)=nu_p. Both implementations keep all ordered terms before this equality. The second changes repeated evaluation of the same target polynomial, not the equation being certified. Its selected comparison and full replays are separately recorded in `execution/`.

The original center-link substitution

    U_(n,i) -> (-1)^(sum_(j<i)n_j)U_(n,i)                      (S26)

reverses each plaquette trace. Every degree-six monomial therefore has even center parity. This is checked on every original trace monomial; it does not replace the independent Haar-mean calculation S21.

## S6. A completely explicit coefficient

For six occurrences of one original face p,

    v_(6e_p)=132817/391910400
              -27383 W_p^2/65318400
              +5911 W_p^4/130636800
              -797 W_p^6/391910400.                          (S27)

The original character substitution and its triangular inverse give

    v_(6e_p)= -11 chi_1/36450
              +491 chi_2/13996800
              -797 chi_3/391910400,                           (S28)

where chi_1=W^2-1, chi_2=W^4-3W^2+1, and chi_3=W^6-5W^4+6W^2-1. The independent one-plaquette linear-character recurrence followed by its formal logarithm reproduces every coefficient in S28. Its scalar logarithm component and the scalar restoring the original unit vacuum are separately recorded. The raw equation S22 has scalar -289/77760.

## S7. Actual supported source complex and its scalar energy class

For a finite original edge support S and a nonnegative integer N, let E_N(S) be the finite-dimensional space spanned by the original physical polynomial matrix coefficients of total entry degree at most N. Include all coefficient parities and the original constant. Under inclusion of supports and increase of N, maps insert identity functions on additional original links. They preserve P_H and intertwine K. Consequently the actual cochain diagram is

    C^0_N(S)=ker(P_H:E_N(S)->C)
       -- K --> C^1_N(S)=E_N(S) --0-->0.                      (S29)

K preserves each space and is invertible on its mean-free part by S12–S14. Thus its first cohomology has the explicit inverse maps

    H^1(C_N(S)) -> C,  [r] -> P_Hr,
    C -> H^1(C_N(S)),  c -> [c1].                            (S30)

Their compositions are identities: r-(P_Hr)1=K f_C(K)r, and P_HK=0. The inverse primitive is the original f_C(K)Q_Hr. The support transitions commute with S30. Applying the Split Zero support reconstruction retains each original label and represents its relation by the zero in that receiving fibre.

For the actual sixth source r_nu, its retained scalar class is -e_nu. Its mean-free primitive is v_nu. Equation S24 supplies the corresponding derivative of that same class; it does not erase the scalar ground-energy contribution. As a formal trace observation, the map to S20 has the explicitly identified trace-relation kernel, so an original supported expression and its receiving zero are both available.

The remaining source terms are also recorded. Put q_6=sum_(i=1)^6 V_i(x). Its complete defect is

    R_6=sum_p x_p W_p/3+B(q_6,q_6)-q_6
       =sum_(7<=i+j<=12,1<=i,j<=6)B(V_i,V_j).                 (S31)

The signed defect is exactly

    K partial_p q_6-W_p-2Q_H Gamma(q_6,partial_p q_6)
        =-K partial_p R_6.                                   (S32)

The degree-five derivative calculation closes precisely the displayed coefficients; S31 retains all higher degrees. The formal parameter observation modulo m^6 has kernel m^6, with its original face labels and coefficients. The physical inverse and response norms used in the subsequent note are returned through the actual unit vacuum, not assigned from the coefficient norm of this source complex.

## S8. Evidence and attribution

The catalogue is complete by S3, and its complete-function equation checks use S9–S21. Ordinary and optimized execution records state exactly which commands and files were replayed. Finite exact polynomial certificates, the written analytic proof of a separate finite-volume radius, and historical claims have distinct scopes. No new Lean run, external analytical review, improved volume-uniform coupling threshold, or four-dimensional continuum mass-gap result is asserted.

The exponential-vacuum and linked character/Casimir methods retain their Hamiltonian coupled-cluster antecedents, including Schütte, Zheng Weihong and Hamer, hep-lat/9603026v1. The original Split Zero coefficient/support framework and all inherited trace, geometry and sphere-map files remain identified in `SOURCE_INTAKE.json`. The new complete coefficient catalogue and its energy/response return are offered for review without a global priority claim.

The separate direct original-matrix check evaluates K and Gamma by quaternion matrix jets, rather than by the Fierz-contracted trace differential routines. In its retained-gradient implementation, each finite original gradient vector (X_(e,alpha)v_mu)_(e,alpha) is evaluated once at the declared rational link assignment. Every ordered pair (mu,nu-mu), including zero contributions, then returns its complete dot product. Derivatives on links absent from an original word are exactly zero by the original coordinate definition; these positions remain in the full gradient vector. The implementation comparison checks the same K value, Gamma sum, scalar and source hash against the direct non-cached routine. The complete per-row ordered pairing list is stored. These single-point derivative regressions accompany the full function identities proved in S4–S5; they are not used in place of the polynomial identity test.

## S9. Direct local derivative bounds without an exterior-volume factor

There is an additional bound using only the newly calculated original trace polynomials, independent of the older Fourier-source norm arguments. For one term

    c_m product_(w in m) tr(U_w)

let k(m) be its number of original trace factors, r_e(m) its number of occurrences of original edge e, and ell(m)=sum_e r_e(m) its total original entry count. All monomials in the sixth source have ell(m)<=24.

For any original unitary SU(2) product A, the same Pauli identity gives

    sum_alpha |tr(T_alpha A)|^2=1-(tr A)^2/4<=1.             (S33)

Cyclically moving the differentiated occurrence inside its original trace therefore bounds its three-component derivative vector by one. The other k-1 original traces have absolute value at most two. Applying the triangle inequality to all differentiated occurrences proves

    |X_e v_nu|_(three components)
       <= sum_m |c_m| r_e(m) 2^(k(m)-1)=C_(nu,e).             (S34)

For an ordered second derivative, the original matrix norm of each generator is 1/2. Two differentiated occurrences, including two on the same original link, have product norm at most 1/4. The trace bound gives

    |X_(f,beta) X_(e,alpha) v_nu|
       <= sum_m |c_m| r_e(m) r_f(m) 2^(k(m)-2).               (S35)

Every occurrence remains; the order of two generators is not interchanged. Summing over all original f and beta at a fixed e,alpha gives the row bound

    D_(nu,e)=3 sum_m |c_m| r_e(m) ell(m)2^(k(m)-2)
       <=36 C_(nu,e).                                        (S36)

For every original anchored placement in S3, use the inverse coordinate map S15 to read the exact representative edge mapped to the anchor. If its operation is (pi,s) and translation d, the first endpoint has x_(pi(i))=s_i d_i; the positive lower endpoint is decreased by one in coordinate pi(0) precisely when s_0=-1. This constructs its actual edge label, counted in the stored anchor-preimage register. Reversal of an edge is handled by differentiating the transported original inverse word in S9; it has the same bounds in S34–S35. No derivative of an unrecorded frame change is discarded.

Summing C_(nu,e) and D_(nu,e) over all 1,839,140 original anchored multisets proves, on every original box and every original link,

    sup_U (sum_alpha |X_(e,alpha)v_[6](U)|^2)^(1/2)
        <=C_6<1085503440,

    max_(e,alpha) sum_(f,beta)
         ||X_(f,beta)X_(e,alpha)v_[6]||_infinity
        <=D_6<35700643605,
    D_6<=36 C_6.                                              (S37)

The exact rational values, all 7,230 per-representative rows, every original edge budget and anchor-preimage count are in `generated/local_derivative_bounds.json`. An open boundary selects a subset of the positive bounding contributions, so the constants contain no exterior-volume factor. They bound the sixth Taylor coefficient only. Its contribution to the actual drift 2kappa Xv is multiplied by the original factor 2kappa xi^6; no estimate for all remaining orders is inferred from this one coefficient. These concrete quantities are retained inputs for the next original residual calculation S31.
