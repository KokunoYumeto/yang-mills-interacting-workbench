# Full corrections at the cubic and fourth sources in the original physical energy

17 September 2026. All operators, parameters, coefficient spaces and source maps are those of `QUARTIC_SOURCE.md` (Q1-Q26). R24-R34 give the strongest result, using the complete fourth source; R1-R23 preserve the cubic-reference calculation and its explicit maps. This argument constructs the full correction rather than truncating the Hamiltonian. The final estimate is for the original finite-regulator physical spectrum, uniformly in L. The smooth four-dimensional continuum mass is not determined by this contribution.

## R1. The actual cubic reference and its whole residual

Write x=xi without changing its physical value, and set

    q3=x v1+x^2 v2+x^3 v3,
    R3=x v1+B(q3,q3)-q3
      =x^4 v4+2x^5 B(v2,v3)+x^6 B(v3,v3),
    J3 h=2B(q3,h), L3=I-J3.                              (R1)

Every term is an original function. Q11 evaluates all of v4. The fifth and sixth terms remain as the displayed complete bilinear functions, with the independent bounds below. The Frechet factor two follows by expansion of B(q3+h,q3+h) using symmetry of the original Gamma.

Put

    A4=2296826751679/30073680,
    m3=336572872/208845, t3=225985217/1253070,
    m2=5834/39, t2=137/6,
    l3=m3+4t3=292337810/125307,
    b23=3(m2*t3+m3*t2)=222621900791/1163565,
    b33=6m3*t3=76060493515233224/43616234025.              (R2)

The exact Q17 source estimate and the three evaluated lower coefficients give

    ||J3|| <= ell(x)=(128/3)x+(3132/13)x^2+l3*x^3,
    ||R3||loc <= delta(x)=A4*x^4+2b23*x^5+b33*x^6.        (R3)

For the cubic part of J3, Q17 and Q16 give
`2*3[m3/6+(2/3)t3]=m3+4t3`; this retains the two different spin budgets. The fifth residual coefficient is twice b23, not b23. All sixth-order residual terms are included in b33.

Define the explicitly specified rational polynomial

    D4(x)=(1-ell(x))^2-(8/3)delta(x).                    (R4)

Let alpha4 be its unique root between 178/10000 and 179/10000. Exact rational evaluation proves opposite signs at these endpoints and ell(179/10000)<1. On [0,179/10000], ell and delta are increasing, and

    D4'(x)=-2(1-ell(x))*ell'(x)-(8/3)delta'(x)<0.

Thus alpha4 is also the first positive root; D4>=0 and ell<1 on [0,alpha4]. The full constants in R2-R4 define the polynomial without rounded coefficients.

## R2. Both infinite constructions and their actual residuals

The actual source operator L3 has the norm-convergent inverse

    L3^(-1)=sum_(j>=0)J3^j,
    ||L3^(-1)||<=1/(1-ell(x)).                           (R5)

Let z=L3^(-1)R3 and C=L3^(-1)B. Define w_1=z and
`w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i))`. From R3 and Q17,

    ||w_n||loc <= Cat_(n-1) c_*^(n-1) z_*^n,
    z_*=delta/(1-ell), c_*=(2/3)/(1-ell),
    theta=4 c_* z_*<=1.

The complete series w=sum_n w_n is absolutely convergent, including x=alpha4, and satisfies L3w=R3+B(w,w). Its bound is

    ||w||loc<=w_*(x)=(3/4)(1-ell(x)-sqrt(D4(x))).         (R6)

At theta=1 the convergence comes from the Catalan series itself. With b_N=binom(2N,N)/4^N, the exact identity Cat_N/4^N=2(b_N-b_(N+1)) gives the full nonlinear tail

    ||sum_(n>N)w_n||loc
       <=(3/4)(1-ell)theta^(N+1)b_N
       <=(3/4)(1-ell)theta^(N+1)/sqrt(N+1).              (R7)

The final inequality follows from b_N^2<=1/(N+1), proved by induction from the displayed ratio b_(N+1)/b_N=(2N+1)/(2N+2). Independently, the finite linear sum has the exact original residual

    L3^(-1)R3-sum_(j=0)^N J3^j R3
       =J3^(N+1)L3^(-1)R3.                             (R8)

Its norm is at most ell^(N+1)delta/(1-ell). Each J3 operation adjoins at most three original faces to the union label, and R3 has at most six; the finite linear sums therefore retain supports of at most6+3N faces. R7 retains every subsequent nonlinear union.

## R3. Identification with the original positive vacuum and its scalar

At each finite L the labelled normed coefficient source is complete, and its global c-weighted sum is at most |E_L| times its local norm. The original spin-generator bounds control every first and second derivative by that global sum. Thus the convergent v=q3+w is C^2 on the original compact product group. The source equation can be summed with its full derivatives. Retain

    C(v)=int_H Gamma(v,v),
    c_L=-(1/2)log int_H exp(2v),
    psi_L=exp(v+c_L),
    E0,L=2kappa x M-kappa C(v).                         (R9)

The original product rule gives H psi_L=E0,L psi_L. Elliptic regularity makes psi_L smooth and strictly positive. Multiplication and division by psi_L preserve the original finite-volume H^1 domain. Integration by parts gives, for every smooth f,

    q_(H-E0,L)(psi_L f)=kappa int psi_L^2 sum_i|X_i f|^2. (R10)

This proves E0,L is the actual ground energy. A second ground state divided by psi_L has every original derivative zero and is constant. The source construction is gauge invariant, so this is the actual physical vacuum. The argument does not assume an excitation gap.

The approximate exponential has a separate exact identity, which retains its multiplication defect:

    exp(-q3) H exp(q3)
      =kappa[K-2Gamma(q3,.)]
       +kappa[2Mx-C(q3)]I-kappa M_(K R3).                (R11)

Here M_(K R3) means multiplication by the full original polynomial K R3. Q1-Q2 and a direct differentiation prove R11. Its scalar C(q3) and the multiplication operator remain; they are not replaced by the actual E0,L before R9 is proved.

The same absolute coefficient arguments give analyticity for complex |x|<alpha4. At every original power the unique coefficient recurrence is Q2. Consequently this solution agrees, by its actual coefficients and the ground-state identification, with the preceding constructions on their common domain. No competing vacuum or comparison measure is substituted.

## R4. Return to the complete physical spectral problem

The original transported operator is

    A=psi_L^(-1)(H-E0,L)psi_L=kappa[K-2Gamma(v,.)].      (R12)

The complete actual point-spin budget is

    t(v)<= (16/3)x+(137/6)x^2+t3*x^3+w_*/6.

For a physical Fourier function h, the three original generator indices and sum_e j_e<=2c(j)/3 give

    ||2Gamma(v,h)||_X<=chi(x)||Kh||_X,
    chi(x)=4[(16/3)x+(137/6)x^2+t3*x^3+w_*/6].           (R13)

The norm X is the sum of the original trace norms of Fourier coefficients. The scalar output is included in this bound. Substitution of R6 gives the exact identity

    3(1-chi(x))=d4(x)
      =(3/2)(1+sqrt(D4(x)))+(1136/13)x^2+p3*x^3,
    p3=(3/2)m3-6t3=278874091/208845>0.                 (R14)

In particular chi<1 throughout the entire closed domain. At alpha4, d4 exceeds3/2.

Let lambda>0 be an actual physical excitation eigenvalue, and h the zero-Haar-mean part of its eigenfunction after division by the actual vacuum. A constant transported eigenfunction has eigenvalue zero, so h is nonzero. The original eigen-equation gives

    (K-lambda/kappa)h=Q_H 2Gamma(v,h).                  (R15)

Smoothness on this fixed finite product implies absolute summability of its c-weighted Fourier trace coefficients: applying arbitrarily high powers of the elliptic K gives rapid decay, while the number and dimensions of product-spin representations grow polynomially in c at this fixed L. Cauchy-Schwarz then gives the required trace-norm summability. Hence R13 applies to the actual eigenfunction. Q16 gives c>=3 on every nonconstant physical block. For 0<lambda/kappa<3,

    ||(K-lambda/kappa)h||_X
       >=(1-lambda/(3kappa))||Kh||_X.

Combining this with R13 proves lambda>=kappa d4(x). Excitations with lambda/kappa>=3 obey the same bound because d4(x)=3(1-chi(x))<=3. The compact physical spectral resolution returns this to the full original physical form domain:

    Delta_L>=kappa d4(x),
    q_A(f)>=kappa d4(x) Var_(rho_L)(f),
    L>=2, a>0, 0<x<=alpha4.                             (R16)

Thus the result includes states whose original labels depend on L. It is a lower bound on all physical excitations, not a lower bound only on a chosen finite trace family.

## R5. Exact numerical enclosures in original physical units

Rational bisection and integer-square comparisons give

    0.01781868048538520630 < alpha4 < 0.01781868048538520631,
    3.745693472404566975 < 1/(2sqrt(alpha4))
                        < 3.745693472404566976.          (R17)

The exact condition on the original coupling is g^2>=1/(2sqrt(alpha4)). A sufficient rounded condition is g^2>=3.745693472404566976. The parent threshold was about3.825973052393386; the comparison retains that stronger saved value, not an earlier weaker summary.

At g^2=15/4, x=4/225, the bound is

    d4(4/225)>1.5794.

The same rational bound holds for all g^2>=15/4. To verify the required monotonicity, for 0<=x<=4/225 use D4<=1, ell'>=128/3 and R4 to bound

    d4'(x)<=-(3/2)(1-ell(4/225))(128/3)
             +2(1136/13)(4/225)+3p3(4/225)^2<0.

Every number in this final test is rational. Therefore

    Delta_L>1.5794*kappa=3.1588*g^2/a,
    g^2>=15/4.                                        (R18)

At g^2=4, x=1/64,

    d4(1/64)>1.88578,
    ||v-q3||loc<0.019533267617373.                      (R19)

The unchanged physical scale is kappa=8/a there. These bounds include the complete linear and nonlinear tails in R7-R8. The generated verification record contains exact rational brackets, not only these decimal renderings.

## R6. Retained source kernels, complete operator defect, and physical primitive

For the actual finite windows

    V_N=span{R3,J3R3,...,J3^N R3},
    V_N --L3--> V --0--> 0,

the inclusion in degree zero and the identity in degree one give the commuting support transitions. R5 supplies the explicit isomorphism

    V_(N+1)/V_N -> ker[V/L3 V_N -> V/L3 V_(N+1)],
    [h] -> [L3h],   inverse [L3h] -> [h].               (R20)

Changing a representative by L3 V_N changes the inverse by exactly V_N, proving both inverse laws. Subtraction of the actual finite primitive sum leaves J3^(N+1)R3 as the representative. The source label remains attached at a receiving zero. This is the actual Split Zero support-indexed complex and its retained primitive, with the same original coefficient domain throughout.

The map from this source to the physical equation has the exact identities

    K L3 h=Q_H[K-2Gamma(q3,.)]h,
    Q_H A h-kappa K L3h=-2kappa Q_H Gamma(w,h).           (R21)

The right side has X norm at most(2kappa/3)w_*||Kh||_X by the original spin bounds. R11 separately retains the entire multiplication residual and scalar of the reference exponential. Thus no identity between the linearized source and the full physical operator is asserted without its displayed defect.

On centered original physical functions let d_X f=(X_i f)_i, with squared derivative norm kappa int rho_L sum_i |X_i f|^2. The inverse on its actual range is p_X(d_X f)=f. Its uniqueness follows from the derivative-zero functions being constants and the centering condition. The original ground-state map f->psi_L f and its inverse h->h/psi_L preserve the specified pairings. The variational characterization and R16 give

    ||p_X||^2=1/Delta_L<=1/(kappa d4(x)).                 (R22)

An actual gauge-invariant conditional-expectation kernel is a centered subspace. Restriction of R16 to its original closed form consequently gives the same lower bound for its physical restricted operator. This returns the stronger inverse estimate to the previously computed zero-shift response without changing its forcing or Gram matrix.

## R7. Continuum scope and literature correspondence

The standing path is a_n=a0*2^(-n), g_n^2=1/c_n, c_n=g0^(-2)+beta*n*log2. Its inclusion in R16 is exactly c_n<=2sqrt(alpha4). For beta>0 the path eventually leaves this proved domain. This finite-regulator, volume-uniform result does not assign a finite continuum mass or a nontrivial ultraviolet field to that path.

The exponential vacuum and linear excitation equations have established antecedents. In Schuette, Zheng Weihong and Hamer, arXiv:hep-lat/9603026v1, the coefficient x_C=2/g_C^4 and physical operator H_C=g_C^2[K-x_C S]/(2a) have the exact original-coordinate return

    g_C=2^(3/4)g,
    H_original=sqrt(2)H_C(a,g_C)+2kappa xi M I.           (R23)

Substitution verifies both coefficients and the additive energy. Their Hermitian-generator commutator derivative corresponds to iX here, giving the original signs K v-Gamma(v,v)-xi S. The exact physical Haar/energy pairings and complete source residuals in R1-R22 are kept after this comparison. The general method and existence of higher-order calculations are not claimed as new. No global priority or best-known-threshold statement follows from this scoped literature reading.


## R8. Execute the full correction at the calculated fourth source

The fourth table is now used as an actual reference, rather than left as a remainder estimate. Put

    q4=x v1+x^2 v2+x^3 v3+x^4 v4,
    J_[4]h=2B(q4,h), L_[4]=I-J_[4].

Expansion of the unchanged source equation Q2 gives the entire residual, with all ordered contributions:

    R_[4]=x v1+B(q4,q4)-q4
      =x^5[2B(v1,v4)+2B(v2,v3)]
       +x^6[2B(v2,v4)+B(v3,v3)]
       +2x^7 B(v3,v4)+x^8 B(v4,v4).                   (R24)

Each displayed B is the original function with its full union support. The fifth source is not claimed to have been separately expanded into its final channel table. R24 is an exact expression for every part of the reference residual, including the sixth, seventh and eighth degrees.

Use the exact m4,t4 from Q26, together with the earlier m_i,t_i. Define

    l4=m4+4t4,
    b14=3(m1*t4+m4*t1), b24=3(m2*t4+m4*t2),
    b34=3(m3*t4+m4*t3), b44=6m4*t4,
    ell_[4](x)=ell(x)+l4*x^4,
    delta_[4](x)=(2b14+2b23)x^5+(2b24+b33)x^6
                       +2b34*x^7+b44*x^8,
    D_[4](x)=(1-ell_[4](x))^2-(8/3)delta_[4](x).        (R25)

All of these constants are rational and positive. The underlying estimates are exactly Q17:

    ||J_[4]||<=ell_[4], ||R_[4]||loc<=delta_[4].

In particular the fourth contribution to the derivative is
`2*3[m4/6+(2/3)t4]=m4+4t4`, and the factor two in each unequal reference pair is retained.

Let alpha_[4] be the first positive root of the polynomial D_[4]. On [0,182/10000], ell_[4]<1, ell_[4] and delta_[4] are increasing, and

    D_[4]'=-2(1-ell_[4])ell_[4]'-(8/3)delta_[4]'<0.

Exact signs at 181/10000 and 182/10000 therefore prove existence and uniqueness of this root in that interval, and its first-positive-root status. Integer-square comparisons and rational bisection give

    0.018104972231644127075 < alpha_[4]
                           < 0.018104972231644127076,
    3.715960362535435236 < 1/(2sqrt(alpha_[4]))
                        < 3.715960362535435237.         (R26)

For every 0<x<=alpha_[4], L_[4] has its actual norm-convergent Neumann inverse and the complete correction w^[4]=v-q4 is constructed by the same explicit binary-tree series as R5-R7, with the R25 data. Thus

    ||L_[4]^(-1)||<=1/(1-ell_[4]),
    ||w^[4]||loc <= w_[4]*(x)
       =(3/4)(1-ell_[4](x)-sqrt(D_[4](x))).             (R27)

For clarity, set z=L_[4]^(-1)R_[4], C=L_[4]^(-1)B, w_1=z and
`w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i))`. Its scalar majorants are
`z_*=delta_[4]/(1-ell_[4])` and `c_*=(2/3)/(1-ell_[4])`.
The parameter theta_[4]=4c_*z_* lies in [0,1]. The exact complete tail is bounded by

    ||sum_(n>N)w_n||loc
       <=(3/4)(1-ell_[4]) theta_[4]^(N+1)
                          binom(2N,N)/4^N
       <=(3/4)(1-ell_[4]) theta_[4]^(N+1)/sqrt(N+1).    (R28)

At alpha_[4] this converges to zero by the central-binomial bound. The inverse truncation separately has residual
`J_[4]^(N+1)L_[4]^(-1)R_[4]` and norm at most
`ell_[4]^(N+1)delta_[4]/(1-ell_[4])`. These equations control both infinities without replacing their actual coefficient sources. A finite inverse term has original support in at most8+4N faces, and every nonlinear union remains recorded.

The resulting v=q4+w^[4] is C^2 in the original finite-volume coordinates by the same global c-summability proof in R3. Its full equation proves R9-R10 with this v, hence identifies the same actual positive physical vacuum and its scalar. The exact approximate exponential formula is R11 with q3,R3 replaced by q4,R_[4]; the full multiplication defect K R_[4] and the scalar C(q4) remain.

## R9. Strongest full physical lower bound and retained inverse

The actual point-spin bound is now

    t(v)<=t1*x+t2*x^2+t3*x^3+t4*x^4+w_[4]*/6.

The complete physical excitation argument R12-R16 applies to this actual v. Its returned margin is exactly

    d_[4](x)=(3/2)(1+sqrt(D_[4](x)))
             +(1136/13)x^2+p3*x^3+p4*x^4,
    p4=(3/2)m4-6t4
       =32092619324045301088/823531037954625>0.          (R29)

Indeed expanding `3[1-4(t1*x+t2*x^2+t3*x^3+t4*x^4+w_[4]*/6)]` using R27 proves R29 term by term. In particular d_[4]>3/2 on the full closed positive-coupling interval. The exact original theorem is

    Delta_L>=kappa d_[4](xi),
    q_A(f)>=kappa d_[4](xi) Var_(rho_L)(f),
    L>=2, a>0, 0<xi<=alpha_[4].                        (R30)

The proof includes every physical form-domain vector through the complete compact spectral resolution as in R15-R16. No preassigned missing excitation gap is used in the source construction. A sufficient rounded original coupling condition is
`g^2>=3.715960362535435237`; the exact condition is `g^2>=1/(2sqrt(alpha_[4]))`.

At the concrete original parameters,

    g^2=15/4, xi=4/225: d_[4](xi)>1.6584,
    g^2=4, xi=1/64:     d_[4](xi)>1.89811.              (R31)

The first bound holds throughout g^2>=15/4. For x0=4/225 the exact rational inequality

    -(3/2)(1-ell_[4](x0))(128/3)
       +2(1136/13)x0+3p3*x0^2+4p4*x0^3<0

bounds d_[4]' from above for 0<x<=x0, because sqrt(D_[4])<=1 and ell_[4]' >=128/3. Thus d_[4] decreases on that interval. It follows in original physical units that

    Delta_L>1.6584*kappa=3.3168*g^2/a,
    g^2>=15/4.                                        (R32)

At g^2=4 the complete reference error obeys
`||v-q4||loc<0.011169768000312`. The generated receipt retains full rational brackets for the correction, discriminant, and original energy factors.

For the actual source windows `V_N=span{R_[4],J_[4]R_[4],...,J_[4]^N R_[4]}`, the two degree maps and inverse in R20 are now the explicit maps

    [h] -> [L_[4]h], inverse [L_[4]h] -> [h].

They are well-defined on `V_(N+1)/V_N` and the corresponding transported cohomology kernel because L_[4] is injective and its inverse is R27. Both inverse compositions remain literal. The receiving scalar, support and full physical defect are

    K L_[4]h=Q_H[K-2Gamma(q4,.)]h,
    Q_H A h-kappa K L_[4]h=-2kappa Q_H Gamma(w^[4],h),
    ||p_X||^2=1/Delta_L<=1/(kappa d_[4](xi)).             (R33)

The defect norm is at most `(2kappa/3)w_[4]*||Kh||_X`. The physical derivative norm and ground-state multiplication/division maps are exactly those in R22. Thus the stronger inverse also restricts to the original physical conditional kernel, without changing a forcing vector or its raw Gram matrix.

The standing simultaneous path has the exact domain

    a_n=a0*2^(-n), g_n^2=1/c_n,
    c_n=g0^(-2)+beta*n*log2 <= 2sqrt(alpha_[4]).          (R34)

For beta>0 it eventually leaves the certified interval. The root in R26 is the endpoint of this particular proved majorant, not an assigned singularity of the actual theory. This contribution gives no ultraviolet continuum field or finite positive continuum mass. The complete fourth table and its q4 correction are now finished inputs; the next unevaluated coefficient is the original channel-resolved v5.
