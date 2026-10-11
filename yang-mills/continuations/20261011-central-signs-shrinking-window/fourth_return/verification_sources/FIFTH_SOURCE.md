# The complete fifth logarithmic source and its signed plaquette derivatives

17 September 2026. This continuation uses the original finite open SU(2) Hamiltonian. It extends the available fourth-source calculation by one complete order. The incoming independent-session report is retained verbatim in the cumulative archive. Its separately linked calculation ZIP was not present among the mounted files; the report is therefore recorded as a report, rather than assigned the verification status of unavailable programs.

The result here is an exact Taylor-coefficient calculation with complete polynomial-identity certificates. The finite-volume analytic response estimate is proved separately in `PLAQUETTE_RESPONSE.md`. No new uniform-in-volume coupling threshold or continuum mass-gap theorem is asserted. The earlier written gap arguments remain preserved historical sources; this calculation does not independently recertify their full analytical chain.

## F1. Original operator, scalar and independent source parameters

Fix an integer L>=2. The vertices are {-L,...,L}^3. The positively oriented edge e=(n,i) runs from n to n+e_i whenever both endpoints occur. Every contained elementary face p=(n;i,j), i<j, has the original trace

    W_p(U)=tr[U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)].       (F1)

Each inverse is the inverse of that same original edge variable. The original generators, derivatives and kinetic operator are

    T_alpha=-i sigma_alpha/2,
    X_e,alpha f=(d/dt) f(...,exp(t T_alpha)U_e,...) at t=0,
    K=-sum_(e,alpha) X_e,alpha^2.                                (F2)

The scalar product is the original product-Haar probability integral. Physical functions are invariant under every original vertex gauge action U_e -> h_s U_e h_t^(-1), including boundary vertices.

Introduce independent real parameters x_p in the actual potential:

    H(x)=kappa K+kappa sum_p x_p(2-W_p),
    kappa=2g^2/a,
    x_p=xi=1/(4g^4) on the original homogeneous line.             (F3)

The parameters x_p are bookkeeping coordinates for derivatives of this same family. At a fixed finite box its real ground state is smooth, strictly positive, unique and physical. For a neighbourhood of the origin it has a smooth real-analytic choice, proved by the isolated spectral projection and elliptic bootstrapping. Indeed the contour construction in P3 gives an analytic eigenvector in L2. The eigen-equation and bounded smooth multiplication then give analytic dependence in each fixed Sobolev space, using the inverse of K+1; choosing a Sobolev order above half the finite manifold dimension plus two gives analytic dependence in C2. At the origin the vector is the constant 1, so the real logarithm is defined in a neighbourhood of the origin.

Write

    psi_x=exp(v(x)+c(x)),  P_H v(x)=0,
    c(x)=-1/2 log int exp(2v(x)) dU,
    E_0(x)=kappa[2 sum_p x_p+e(x)].                              (F4)

Here P_H is the original Haar integral and Q_H=I-P_H. Product differentiation of exp(v) in the original generators gives

    K v=sum_p x_p W_p+Q_H Gamma(v,v),
    e(x)=-P_H Gamma(v,v),
    Gamma(f,h)=sum_(e,alpha) (X_e,alpha f)(X_e,alpha h).           (F5)

The scalar removed from the source in F5 is exactly the displayed contribution to the original energy. The scalar c(x) retains the original unit-vacuum mass.

Use ordinary multivariate monomial coefficients, with the explicit derivative rule

    v(x)=sum_(nu!=0) v_nu x^nu,
    partial_xp[x^nu]=nu_p x^(nu-e_p).                            (F6)

There is no extra factorial in v_nu. For a single nonzero entry nu=e_p, v_nu=W_p/3. Equating the complete coefficients of F5 gives

    K v_nu=Q_H sum_(0<mu<nu) Gamma(v_mu,v_(nu-mu)),
    P_H v_nu=0.                                                (F7)

The inequalities on multiindices in this formula mean componentwise inclusion, with zero and nu excluded. Thus every ordered split is retained. On the homogeneous line the fifth coefficient is the full expression

    v_[5]=2B(v_[1],v_[4])+2B(v_[2],v_[3]),
    B(f,h)=K^(-1)Q_H Gamma(f,h).                                (F8)

Every proper split in F7 for degree five uses only already specified degrees one through four.

## F2. Exact original differential algebra and finite inverse

The elementary Pauli identities in F2 are

    sum_alpha tr(T_alpha A)tr(T_alpha B)
       =-tr(AB)/2+tr(A)tr(B)/4,
    sum_alpha T_alpha A T_alpha=-tr(A)I/2+A/4,
    -sum_alpha T_alpha^2=3I/4.                                 (F9)

They follow by multiplying the three displayed two-by-two Pauli matrices. Every occurrence of U_e differentiates as T_alpha U_e; every occurrence of U_e^(-1) differentiates as -U_e^(-1)T_alpha. Applying the product rule to every original occurrence and then F9 gives the complete trace-word formulas for Gamma and K implemented in the inherited `trace_algebra.py`. In particular, no interaction at a shared edge is replaced by a diagonal pairing.

Each trace word is retained with its original edge labels. The identities tr(AB)=tr(BA), tr(U^(-1))=tr(U) for U in SU(2), and cancellation of an adjacent U_e U_e^(-1) have their literal matrix proofs. The trace-power recurrence is

    tr(U^n)=tr(U)tr(U^(n-1))-tr(U^(n-2)),                       (F10)

obtained by multiplying U^2-tr(U)U+I=0 by U^(n-2). The raw representative files expose every resulting rational trace term. Their image as an original function is what enters the equations.

For a face multiset nu, let r_e be the number of occurrences of e in its original face words. Its edge representation factors have the finite spin list

    j_e=r_e/2, r_e/2-1, ..., (r_e mod 2)/2.                    (F11)

This list belongs to the particular Taylor coefficient. The full Hamiltonian retains its entire spin spectrum. At each vertex, an invariant tensor requires sum_e 2j_e even and 2 max_e j_e <= sum_e j_e. The lists accepted by these tests contain all actual physical representations, including their multiplicities. Every such tensor has original Casimir sum

    c=sum_e j_e(j_e+1).                                       (F12)

Let C be the set of those values, as explicitly stored in every row. Define

    q_C(t)=product_(c in C,c>0)(1-t/c),
    f_C(t)=(1-q_C(t))/t-q_C(t) sum_(c in C,c>0) 1/c.             (F13)

The numerator of the first term has zero constant coefficient. Direct substitution proves f_C(0)=0 and f_C(c)=1/c at each positive c. On this coefficient space the actual spectral action consequently gives

    K f_C(K)=Q_H.                                             (F14)

The possible zero-Casimir functions are constants, as follows either from the product representation or from int sum|Xf|^2=0. This identifies Q_H in F14 and proves uniqueness of the zero-Haar-mean solution of F7. All rational divisions in the producer are by the displayed positive Casimir values.

## F3. Complete enumeration and exact coordinate transports

Anchor the original edge at (0,0,0;0). Start with the four faces incident on it. At each subsequent order append either a face already present or a face sharing an original edge with one of the present faces. Retain the sorted multiset, with multiplicity. Induction proves completeness: a connected multiset with at least two distinct faces has a non-root leaf in a spanning tree of its face-adjacency graph; remove one occurrence there, or remove a repeated occurrence first. The remaining multiset still admits the construction. A one-face multiset is generated by repetition.

The consecutive anchored counts are 46, 612, 8,621 and 124,864 at degrees two, three, four and five. The degree-five pattern counts are

| Multiplicities | Anchored multisets | Coordinate representatives |
|---|---:|---:|
| 5 | 4 | 1 |
| 4+1 | 84 | 2 |
| 3+2 | 84 | 2 |
| 3+1+1 | 1,572 | 19 |
| 2+2+1 | 1,572 | 19 |
| 2+1+1+1 | 27,676 | 171 |
| 1+1+1+1+1 | 93,872 | 448 |
| Total | 124,864 | 662 |

Each of the 48 signed coordinate permutations is an explicit map

    y_i=s_i x_(pi(i))-d_i,
    x_(pi(i))=s_i(y_i+d_i),  s_i in {-1,1}.                     (F15)

The translation d and the chosen permutation/signs are stored for every anchored original multiset in `generated/geometry_fifth.json`. A positive original edge maps to its corresponding positive edge variable or to that variable's inverse when its orientation reverses. The image of a face word is the target face word up to cyclic starting point and reversal; its SU(2) trace is preserved by F9-F10's elementary matrix identities. Haar measure is preserved by variable permutation and inversion, and K is carried to the target K because the original left/right Casimirs agree.

Returning a representative to its original multiset therefore uses F15's inverse and the same oriented link substitution. Every original multiset appears once. There is no division by an orbit size or multiplication by a factorial. The original anchor edge is retained in the transport record even when its representative position moves.

A disconnected source coefficient vanishes by induction in F7: all nonzero lower inputs are connected; factors on disjoint edge-adjacency components have Gamma=0. Thus the table accounts for every nonzero coefficient at degree five in every original finite open box. Near a boundary one uses precisely the multisets whose original faces are contained in that box.

## F4. The tree/quaternion morphism used for full identities

For a connected original edge union choose the tree obtained by adding original edges in their stored order whenever they join two distinct vertex components. Its root is the smallest original vertex. Let t_v be the ordered original tree-path holonomy from the root to v, including inverse traversals. For each original chord e=(s,t), put

    Z_e=t_s U_e t_t^(-1).                                     (F16)

The full coordinate map U -> (original tree links, Z_e) has the inverse

    U_e=t_s^(-1)Z_e t_t on chords; original tree links unchanged. (F17)

F16-F17 are inverse maps by substitution. Fubini and left/right Haar invariance prove preservation of the product Haar measure. The gauge action h_v=t_v sends the tree links to I and the chords to Z_e. Every original physical function is thereby determined by its values on this tree section. Residual simultaneous conjugation of the chords remains; no chord is removed on that account.

Write every chord in the original quaternion coordinates

    Z_c=x_(c,0)I-i sum_(a=1)^3 x_(c,a) sigma_a,
    x_(c,0)^2+x_(c,1)^2+x_(c,2)^2+x_(c,3)^2=1.                (F18)

The target coefficient algebra is

    A_C=Q[x_(c,a)]/(sum_a x_(c,a)^2-1 for every chord c).        (F19)

The original trace-word algebra maps to A_C by replacing tree links with I and chords with F18, applying ordinary quaternion multiplication, and retaining the polynomial remainder with exponent zero or one in each x_(c,0). The defining monic relations have distinct leading variables, so their reductions commute. Every intermediate rational coefficient and every variable is retained in the map record.

This is an identity test on complete functions. To prove faithfulness, a remainder has degree at most one in each x_(c,0). For a fixed chord, evaluate x_(c,0) at both signs of sqrt(1-|y_c|^2), with y_c in its open unit ball. A remainder vanishing on the sphere gives zero for both its coefficient of 1 and its coefficient of x_(c,0). Repeat for each chord. The resulting polynomials vanish on products of open balls, hence have all coefficients zero. Thus F19 is exactly the coordinate relation ideal of the product of these real spheres for these polynomial identities.

The inverse on the image of the physical trace algebra is the explicit substitution of the original Z_e(U) from F16. Therefore zero of the complete target polynomial proves zero of the original physical function. As a map from formal trace expressions, the kernel is exactly the trace expressions whose tree-quaternion image lies in the ideal F19. Both the raw expressions and their target polynomial are stored, so this kernel is exposed rather than treated as missing support.

The degree-five representatives have cycle-rank distribution

    rank 1: 1; rank 2: 4; rank 3: 38;
    rank 4: 170; rank 5: 444; rank 6: 5.                        (F20)

Every rank is the actual |E|-|V|+1. In particular five representatives retain six chords. `generated/quotient/0176.json` is an explicit six-chord case. Its specialization Z_6=I and the original polynomial have a nonzero difference, retained as a negative-control calculation.

## F5. The complete fifth catalogue and its checks

The full answer is in `generated/fifth/0000.json` through `0661.json`: 14,063 rational trace monomials, with original faces, multiplicities, edge coordinates, words, Casimir values and every signed coefficient. The same functions are completely expanded in F19 in `generated/quotient/`, with 300,821 rational monomials.

For every representative the checker recomputes the entire right side of F7 from the lower coefficients, applies the original K to the new coefficient, and proves that their difference is the zero polynomial in F19. It also checks the stored raw RHS and stored raw residual against those recomputed expressions. There are 281 raw residual trace expressions which have nonempty formal representatives; all 281 map to the zero polynomial through F16-F19. The remaining 381 are already zero in the retained trace representation.

The explicit central link action

    U_(n,i) -> (-1)^(sum_(j<i)n_j) U_(n,i)                     (F21)

multiplies every original plaquette trace by -1. The coefficient v_nu of total degree five changes sign under this Haar-preserving action. Its Haar mean is exactly zero. The script verifies this sign on every original trace monomial. This supplies the mean condition accompanying F7, not merely its differentiated equation.

The independent directional audit `direct_matrix_checks.py` also recomputes K and Gamma directly from quaternion matrix jets at a declared rational original-link assignment for each of the 662 representatives. Its derivative engine uses matrix multiplication and the original generators, without calling the Fierz-contracted K/Gamma routines. Those finite-point regressions accompany, rather than replace, the complete polynomial tests.

## F6. A fully explicit single-face coefficient and an independent recurrence

For the multiset containing the same original face five times, the table is

    v_(5e_p)=79 W_p/34020-41 W_p^3/136080+11 W_p^5/680400.       (F22)

The original character substitutions

    chi_(1/2)=W,
    chi_(3/2)=W^3-2W,
    chi_(5/2)=W^5-4W^3+3W                                    (F23)

and their triangular inverse give

    v_(5e_p)=49 chi_(1/2)/27216
             -23 chi_(3/2)/97200+11 chi_(5/2)/680400.           (F24)

`character_check.py` supplies a separate calculation. Write chi_n for spin n/2, so K chi_n=n(n+2)chi_n and W chi_n=chi_(n-1)+chi_(n+1). Solve the original linear eigenvector recurrence with original Haar coefficient one, then take its complete formal logarithm and remove only its explicitly computed Haar scalar. At order N only indices n<=N can occur because each original fundamental insertion changes n by one. This recurrence returns F24 exactly and also the original energy coefficients through degree eight. The subsequent scalar restoring the unit vacuum starts at -xi^2/9; it remains recorded separately.

## F7. Every signed degree-four source response

For each face p define z_p(x)=partial_xp v(x). In the original monomial coordinates,

    Z_(p,rho)=(rho_p+1)v_(rho+e_p).                            (F25)

Differentiating the full equation F5 gives

    K z_p=W_p+2Q_H Gamma(v,z_p).                               (F26)

For every degree-four multiindex rho, the complete coefficient is

    K Z_(p,rho)
      -2Q_H sum_(0<mu<=rho) Gamma(v_mu,Z_(p,rho-mu))=0.         (F27)

All 3,047 distinct pairs (representative, face-direction) supplied by the fifth table are checked as complete zero polynomials. The derivative weights, both ordered product contributions, and every original source label are retained. The files also contain each full trace-polynomial response; the stored multiplication factor records its map to the same fifth coefficient.

For comparison with the incoming report, this session independently checked all 78 available fourth coefficients and their 282 degree-three derivative directions in the same original sphere-quotient method, including their nonzero Haar RHS constants. Our particular stored tree section produces 6,048 monomials at degree four. The other session reports 4,044 in its own unavailable coordinate files. The present comparison is of the original equations and the explicit available coordinate maps; no bytewise equality of those unavailable polynomials is claimed.

## F8. Higher terms and their exact retained defect

Define V_i(x)=sum_(|nu|=i) v_nu x^nu and q_5(x)=sum_(i=1)^5 V_i(x). Its residual is the complete original polynomial

    R_5=sum_p x_p W_p/3+B(q_5,q_5)-q_5
       =sum_(6<=i+j<=10, 1<=i,j<=5) B(V_i(x),V_j(x)).          (F28)

On x_p=xi, each summand in F28 carries its original xi^(i+j). No term in F28 is set to zero merely because the first five source equations have been solved.

The signed derivative has exactly the defect

    K partial_xp q_5-W_p-2Q_H Gamma(q_5,partial_xp q_5)
       =-K partial_xp R_5.                                    (F29)

Its coefficients through degree four vanish by F27; its retained degrees five through nine are the displayed derivative of F28. The observation onto degrees <=4 is the coefficient map modulo the original parameter ideal m^5, with kernel exactly m^5. The original face labels and the coefficients of F28 remain upstream of that receiving supported zero. This is the literal finite-source jet use of the Split Zero retention convention. It supplies no claim that q_5 is the full vacuum.

The map to the actual physical inverse, including the unit-vacuum scalar and the full energy pairing, is calculated in P1-P2 of `PLAQUETTE_RESPONSE.md`.

## F9. Verification scope and attribution

The new finite calculation uses the preserved cubic/quartic exact trace engines, whose inputs and hashes are recorded. Both complete symbolic fifth-source replays were executed, in ordinary Python and under -O, without cached-row acceptance. Each reconstructed polynomial file matched the delivered bytes. The separate direct-matrix audit covers all 662 representatives. Named false controls preserve the incoming v1/v4 term, derivative multiplicity, factor two, original sixth chord, support, and vacuum scalar.

These are exact rational computational certificates backed by the algebraic proofs F9-F19. They are not a new Lean elaboration or an independent audit of every earlier analytical argument. The original connected exponential-vacuum framework is credited to the Hamiltonian coupled-cluster literature, including Schuette, Zheng Weihong and Hamer, hep-lat/9603026v1. The present exhaustive coefficients, source response records and proof scope are stated without a historical-priority claim.
