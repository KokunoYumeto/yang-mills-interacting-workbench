# The complete sixth-order ground energy and its original cube contribution

17 September 2026. This calculation uses the actual fourth source evaluated in `QUARTIC_SOURCE.md`, not a finite Hamiltonian approximation. The original scalar energy and all extensive and boundary factors are retained. The coefficient is reproduced by an independent eigenvector recurrence, and the cube contribution is additionally computed by all720 original face orderings.

## E1. Eliminate the fifth source through its exact equation

Retain the original real Haar pairing and source recurrence. Since

    C(v)=int_H Gamma(v,v), E0=2kappa xi M-kappa C(v),

its sixth energy coefficient is

    e6:= [xi^6](E0/kappa)
       =-2 int Gamma(v1,v5)-2 int Gamma(v2,v4)-int Gamma(v3,v3).

The original fifth equation is Kv5=2Q_H Gamma(v1,v4)+2Q_H Gamma(v2,v3). Integrating against the zero-Haar-mean v1, and using int Gamma(f,h)=int f Kh, gives

    e6=-4 int v1 Gamma(v1,v4)-4 int v1 Gamma(v2,v3)
        -2 int Gamma(v2,v4)-int Gamma(v3,v3).             (E1)

This identity includes all fifth-source contributions; none is estimated or discarded. For a specified original multiset of six faces, expand every product in E1 over ordered allocations of that multiset to the displayed sources. A repeated label is allocated by its actual multiplicity, as in Q11. The resulting coefficients depend only on sources through degree four, all evaluated in the adjoining tables.

## E2. Exact original Haar integration

Each word is evaluated in its original SU(2) edge variables. For an edge of even total occurrence r, its full spin-zero projector on that polynomial is

    P_e,0=product_(j=1,...,r/2)[I-E_e/(j(j+1))].         (E2)

Odd occurrence has zero Haar integral, proved by U_e->-U_e. Formula E2 follows by its values1 on Casimir0 and0 on each original positive spin Casimir in that edge's complete occurrence range. Its output is independent of U_e. Thus replacing U_e by I after E2 is the actual original-edge integration, not a substitution for an unevaluated integral. Repeat over every edge. Q4-Q7 make each step a rational original trace calculation. The code retains the resulting constants, including tr(I)=2.

The integration algorithm is independently checked on the fundamental character moments1,2,5 at powers2,4,6. For every sixth-order coefficient below, the same final number is obtained from the separate Rayleigh-Schrodinger recurrence for the original K-xi S. Its overall vacuum amplitude remains a separate scalar factor; the energy coefficients are independent of that factor because the original eigen-equation is homogeneous in it. The numerical polynomial entries in that recurrence are coefficient multipliers, not an assigned physical vacuum norm. The actual amplitude and original unit Haar norm are returned by R9.

Explicitly, with multivariate face couplings, write those coefficient multipliers as u_C, u_empty=1, int u_C=0 for C nonempty, and keep the overall scalar amplitude a as a separate factor a u_C. The energy coefficients satisfy

    e_C=-sum_(p distinct in C) int W_p u_(C-{p}),
    u_C=K^(-1)Q_H[sum_(p distinct in C)W_p u_(C-{p})
                   +sum_(empty!=A proper submultiset C)e_A u_(C-A)].    (E3)

Both equations follow by comparing each original face-coupling monomial in K(a sum u_C x^C)-sum_p x_p W_p(a sum u_C x^C)=e(x)(a sum u_C x^C). The same scalar a appears on both sides; no energy or coupling is rescaled. E3 and E1 give the same six local coefficients. The first calculation uses the logarithmic-vacuum equation, while E3 uses the original linear eigen-equation.

## E3. Exhaustion of the sixth-order connected supports

For each face p, changing U_e to -U_e on one original edge multiplies a source coefficient by the parity of that edge's total original occurrences. Differentiation and all Casimir inverses commute with this center action. A nonzero Haar scalar therefore requires the set of odd-multiplicity faces to have even boundary over F2.

A nonempty finite even-boundary set of elementary cubic faces has at least six faces. Equality is the six-face boundary of one original cube. Here is an explicit finite filling argument. Let c12,c13,c23 be its binary face arrays. Set the binary cube array

    b(n1,n2,n3)=sum_(k>n3)c12(n1,n2,k) mod2.

The edge-boundary equations imply that the sum over k of c12 is constant in n1 and n2; finite support makes that constant zero. Thus b is finite also toward negative n3. Its upper-minus-lower cube boundary has the required c12 array. The remaining face difference is a finite2-cycle with c12=0. The boundary equations on directions1 and2 force its c13,c23 arrays to be constant in direction3; finite support makes them zero. This proves the finite filling and its exact boundary map.

For a nonempty finite cube array b, each nonempty column along an axis has at least two boundary faces normal to that axis. Therefore its boundary has at least twice the sum of the cardinalities of its three coordinate projections, hence at least six. Equality forces each projection to be a singleton, so b is exactly one cube. This proves the stated six-face classification without deleting nonreduced or repeated face labels.

At total order six, all-even multiplicities are6,4+2,2+2+2. Their connected distinct-face supports are respectively a single face, an adjacent pair, or a path/common-edge/corner triple. The only all-odd surviving support is one complete cube. Disconnected supports have zero logarithmic energy coefficient by Q11 and E1; equivalently the original operator on disjoint active link supports is the sum of its commuting tensor-factor operators, so their scalar eigen-energy has no mixed coefficient. The original scalar and all variables remain in that tensor comparison.

## E4. Complete local coefficient table

The coefficient for each indicated original multiset is

| Original multiset | e_C |
|---|---:|
| {p,p,p,p,p,p} | -289/77760 |
| {p,p,p,p,q,q}, p~q | 22285/47309184 |
| {p,p,q,q,r,r}, distinct path | -4909/118272960 |
| Same multiplicities, common-edge triple | 244/4312035 |
| Same multiplicities, cube corner | -212/542997 |
| Six distinct faces bounding one cube | -83/1944 |

The first pair row has the separate original role exchange p<->q; a sum over unordered adjacent pairs counts both roles. The complete finite evidence includes both pair embeddings (coplanar and perpendicular), all nine original cubic-orbit embeddings of distinct triples, and the exact coefficients computed from both E1 and E3.

For clarity, the four terms in E1 for the cube are

    -43/1458, -7/972, -13/2916, -1/648.

For the single face they are

    -17/5832, -1/1458, 17/46656, -7/14580.

Their sums give the corresponding rows. `sixth_energy.json` retains all four terms for every row, together with their original face words and multiplicities.

## E5. A second, path-resolved cube proof

Orient the six cube faces outward. Reversing a whole SU(2) loop preserves its trace, so this is the exact original trace product. Each of the twelve edges now occurs once as U and once as U^(-1). The original integral

    int U_ij conjugate(U_kl)=delta_ik delta_jl/2

supplies twelve factors1/2. Its delta identifications leave one free fundamental color at each of the eight vertices. Hence

    int product_(six cube faces) W_p=2^8/2^12=1/16.     (E4)

In the independent six-distinct-face perturbation coefficient, each proper subset has zero scalar energy coefficient by E3 and the even-boundary argument. In any original ordering, edges occurring twice in an intermediate subset occur in no later face. Integration of those edges projects them onto spin zero. Every edge occurring once carries spin1/2. The original intermediate Casimir is consequently exactly (3/4)|boundary(subset)|. These projections commute with later independent edge variables and with the original total K. Therefore the full cube coefficient is

    -(1/16) sum_(pi in S6) product_(j=1)^5
                        4/[3 |boundary(first j faces of pi)|].       (E5)

No intermediate denominator is replaced by the plaquette denominator3. The complete path count is

| Five successive boundary lengths | Multiplicity |
|---|---:|
| (4,8,8,8,4) | 48 |
| (4,8,8,6,4) | 96 |
| (4,6,8,8,4) | 96 |
| (4,6,8,6,4) | 192 |
| (4,6,6,6,4) | 288 |

There are720 paths. Their rational sum before the1/16 factor is166/243. Equation E5 therefore gives exactly -83/1944, matching the complete coefficient recurrence. This retains all original intermediate boundaries, their denominators, and the terminal Haar contraction. It is the first closed-surface scalar term on six distinct original faces.

## E6. All original finite-box factors and the complete higher-order remainder

Let m=2L. Denote by M,J,P,T,C,B the numbers of original faces, unordered adjacent pairs, three-face paths, common-edge triples, corners and cubes. Their exact values are

    M=3m^2(m+1), J=6m(3m^2-1),
    P=138m^3-126m^2-24m+12,
    T=12m^2(m-1), C=8m^3, B=m^3.                       (E6)

For T sum binom(r_e,3) over the original edge degrees r_e in {2,3,4}. There are3m(m-1)^2 degree-four edges and12m(m-1) degree-three edges, giving the stated T. Each cube has eight three-face corners. To obtain P, count centered face-adjacency wedges and subtract three for each triangular triple. A face degree is s_i+s_j+4r_k-4, where s_i,s_j are3 at one of the two cell-end positions and4 otherwise, and r_k is1 at either normal boundary and2 internally. The direct count is

    sum_p binom(deg p,2)=198m^3-162m^2-24m+12.

Subtract3(T+C), proving P. These formulas preserve every original open boundary. The verifier independently enumerates the actual boxes L=2,3,4.

Summing all rows in E4 gives

    e6= -289M/77760 +22285J/23654592 -4909P/118272960
                       +244T/4312035 -212C/542997 -83B/1944
       =-(211396463m^3+30959193m^2+21845782m+2336684)/4691494080.   (E7)

Thus the original full ground energy is

    E0,L=2kappa M xi-kappa M xi^2/3
       +kappa(5M/216-2J/1053)xi^4+kappa e6 xi^6+R_ge8.  (E8)

The parent analyticity proof on the complex circle |xi|=1/60 bounds the complete scalar C(v) by49|E_L|/1200 there. The new source agrees coefficientwise with that proved construction. The exact center involution makes E0-2kappa Mxi even. Cauchy's estimate and the full geometric tail therefore give

    |R_ge8| <= (49kappa |E_L|/1200)
                 (60|xi|)^8/[1-(60|xi|)^2],
    0<|xi|<1/60.                                       (E9)

The finite coefficient polynomial is accompanied by all higher orders through this bound. Its validity range remains stated; it is not silently extended past the Cauchy circle.

At L=2, e6=-3528610133/1172873520. Along the original spatial-volume limit m->infinity, the coefficient per face is

    lim e6/M=-211396463/14074482240.                     (E10)

This is a limit of the specified Taylor coefficient with its complete original counts. It does not by itself exchange a spatial or ultraviolet limit with a coupling series beyond the proved domain.

## E7. Literature and scope

Schuette-Zheng-Hamer's coupled-cluster/character method and Llewellyn Smith-Watson's shifted linked-cluster formulation are primary antecedents, arXiv:hep-lat/9603026v1 and hep-lat/9212025v1. The former's operator dictionary to Q1 is R23. The latter explicitly describes its truncation and cluster-shift prescriptions; this calculation keeps the original products and uses the full residual bounds R3-R8 and E9. This establishes the method correspondence and the actual all-order error returned here; it is not a claim that the general expansion method or every displayed coefficient is historically new. The scoped search did not establish an independent published match or global priority for the full spatial sixth coefficient E7.


## E8. Return to an actual measured plaquette observable

For real 0<xi<1/60 at fixed original kappa, the constructed simple vacuum is differentiable in xi. Its original mass is one, hence `2 Re<psi,partial_xi psi>=0`. Differentiating `H psi=E0 psi` and testing with the same psi therefore proves the exact Hellmann-Feynman identity

    dE0/dxi = kappa(2M-sum_p <W_p>_rho).

No derivative of the vacuum is omitted: its two terms cancel through the displayed mass derivative and the actual eigen-equation. Define the original mean half-trace as an explicit observation map

    P_L(xi)=(1/(2M))sum_p <W_p>_rho.

Keeping M and the complete coefficients e4,e6 from E8 gives

    P_L(xi)=xi/3-(2e4/M)xi^3-(3e6/M)xi^5+R_P,L,
    |R_P,L| <= (49|E_L|/(40M))
         (60xi)^7 [8-6(60xi)^2]/[1-(60xi)^2]^2.         (E11)

To prove the tail, the same original Cauchy bound used in E9 gives
`|e_(2n)|<=(49|E_L|/1200)60^(2n)` for every n>=4. Differentiate its absolutely convergent series on |xi|<1/60. The exact scalar sum

    sum_(n>=4)2n r^(2n-1)=r^7(8-6r^2)/(1-r^2)^2

follows by differentiating r^8/(1-r^2). Its factor60 and the factor1/(2M) in the actual observation give precisely E11. The ratio |E_L|/M=(m+1)/m is retained and is at most5/4 for L>=2; consequently the entire error is independent of exterior volume after this explicitly defined spatial average.

For each fixed coefficient, all connected source supports have a finite number of original faces. Their interior translates contribute the same coefficient, and the boundary embeddings have vanishing proportion as m->infinity. The bounds just used are uniform after division by M. Dominated power-series summation therefore proves the full mean-observable limit on |xi|<1/60, as well as differentiation of its energy-density series. Its first terms are

    P_infinity(xi)=xi/3-(11/468)xi^3
                       +(211396463/4691494080)xi^5+R_P,infinity,
    |R_P,infinity| <= (49/40)
         (60xi)^7 [8-6(60xi)^2]/[1-(60xi)^2]^2.         (E12)

This is a fixed-lattice-spacing observable return. No continuum scaling limit is used in the coefficientwise or dominated-series argument.

## E9. Explicit correspondence to a current variational benchmark convention

Spriggs, Greplova, Carrasquilla and Nys, arXiv:2509.12323v1, equation1, use the physical convention

    H_N(g_N,a)=g_N^2/a [K/2+(4/g_N^4)sum_p(1-W_p/2)].

Specialize this formula to the same original edge and face sets as Q1. Then the literal coefficient substitution is

    g_N=2g, lambda_N=4/g_N^4=xi,
    H_N(2g,a)=H_original(g,a),
    (a/g_N^2)H_N=H_original/(2kappa).                   (E13)

The generator commutators and E^2=-Delta_(S3)/4 in their equations1-3 agree with the original T_alpha=-i sigma_alpha/2 coordinates through their Hermitian derivative iX. Direct substitution in E13 gives exactly kappa and kappa xi for the two original coefficients. The trace map in their equation4 is W_p->W_p/2, precisely the measured observation in E11. All energy and trace factors are exhibited.

Their reported finite numerical lattices have their own boundary choice. To retain the comparison on a periodic extension of our same vertex set, let J be pullback from the old edge variables, with inverse adjoint the Haar integral over the additional wrapping links. For side2L+1>=5 its actual operator defect is

    H_periodic J-J H_open
       =kappa xi sum_(p in P_periodic\P_open)(2-W_p)J.  (E14)

The electric terms on the added links annihilate the pullback, and all old terms agree; expansion proves E14. Thus E13 is a convention correspondence on matched index sets, and E14 keeps the added interactions needed for the other boundary choice. No numerical data from that paper are presented as an evaluation or independent verification of E7 or E12. The earlier 1985 perturbative source cited in that paper was identified bibliographically but its full text was not retrieved here. The new coefficients and remainder are offered as explicit original-convention benchmark data, with their written derivation and exact replay.
