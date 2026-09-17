# Recovered excerpt only

This is the portion actually present in the upload; it ends mid-proof. Escaped Markdown underscores and the damaged tree-recursion notation have been restored. The original upload remains unchanged.

# The full linearized residual and its return to the original physical gap

16 September 2026. This is the second executed calculation, on exactly the original operators and source coordinates of `CUBIC_SOURCE.md`. It evaluates the full residual at xi v_1+xi^2 v_2, bounds the actual linearized inverse and every nonlinear correction, and returns the result to the complete physical form domain. The proof does not assume a spectral gap to construct this inverse.

## L1. Two sharper spin budgets for the evaluated second source

Retain C1–13, including all union labels. The first source has

```
m(v_1)<=64/3,   t(v_1)<=16/3.                         (L1)

```

An anchor meets at most four plaquettes; each has coefficient norm 8/3, total spin two and anchor spin 1/2. This proves both numbers.

For the actual second source C11, its self contributions to m are at most six. On a pair, with the original x<=16, x+y<=64, its total-spin weighted norm is x/9+4y/117<=400/117. There are at most 42 anchored pairs. Thus

```
m(v_2)<=6+42*(400/117)=5834/39.                       (L2)

```

For t(v_2), self terms contribute at most 3/2. At most six pairs share the anchor itself: their spin-zero term has anchor spin zero, and their spin-one contribution is at most 64/117 per pair. In the other at most 36 pairs, the anchor occurs once and its spin is 1/2, giving at most (1/2)(x/27+y/117)<=176/351. Hence

```
t(v_2)<=3/2+6*(64/117)+36*(176/351)=137/6.            (L3)

```

All original boundary patterns inject into these bulk lists. C7 and C5 now prove

```
||B(v_1,h)||loc<=(64/3)||h||loc,
||B(v_2,h)||loc<=(1566/13)||h||loc,
||B(v_2,v_2)||loc<=799258/39.                        (L4)

```

For the middle coefficient, 3[m(v_2)/6+(2/3)t(v_2)]=1566/13. For the last, 6m(v_2)t(v_2)=799258/39. The two inputs have their actual separately evaluated budgets; neither is replaced by a generic unknown vector.

## L2. Evaluate the complete residual, including its quartic source

Set x=xi as the same original source parameter, and define

```
q_2=xv_1+x^2v_2,
R_2=xv_1+B(q_2,q_2)-q_2=x^3v_3+x^4b_22,
b_22=B(v_2,v_2),
J_2 h=2B(q_2,h),  L_2=I-J_2.                        (L5)

```

The source v_3 is the complete five-family table C14–20. Here is also a finite formula for every component of b_22, avoiding an unevaluated Casimir inverse. Let mu enumerate the original terms of C11, with functions F_mu and coefficients a_mu. Their Casimirs are respectively 8,9/2,13/2 and their a_mu are -1/72,1/27,-1/117. Each F_mu has definite original edge spins, including its zero shared edge in the P_0 channel. For every ordered (mu,nu), let J_e be all spins from |j_mu,e-j_nu,e| to j_mu,e+j_nu,e in unit steps. These are at most two. With the literal polynomial projectors C13,

```
b_22=sum_(mu,nu) a_mu a_nu
      sum_(boldj with c(boldj)>0)
      [c_mu+c_nu-c(boldj)]/[2c(boldj)]
      P_boldj(F_mu F_nu).                           (L6)

```

Each input, edge-spin range, polynomial projector, coefficient and denominator is now specified in original coordinates. This is a finite full-coefficient formula at every finite L. For disjoint active supports c(boldj)=c_mu+c_nu and the corresponding source is exactly zero at its original union. Output constants are retained outside Q_H, as below. No truncation of the full Hamiltonian is performed.

For example, the self/self term at one original plaquette is

```
b_22^(p,p)=chi_1(Omega_p)/10368-chi_2(Omega_p)/31104,
int Gamma(v_2^(p),v_2^(p))=1/648.                   (L7)

```

This follows from chi_1^2=1+chi_1+chi_2, with Casimirs 0,8,24 and the original factor 1/72^2. The entire removed scalar for the original q_2 is

```
C(q_2)=int Gamma(q_2,q_2)
      =M x^2/3+x^4(M/648+2J/1053).                  (L8)

```

The odd term is zero by the original center involution in C7. Thus the full residual of the approximate exponential has the exact operator identity on smooth original functions

```
e^(-q_2) H e^(q_2)
  =kappa[K-2Gamma(q_2,.)]
   +kappa[2Mx-C(q_2)]I-kappa M_(K R_2).             (L9)

```

Here M_(K R_2) is multiplication by the displayed original polynomial. To verify L9, expand the original Laplacian on e^(q_2)f and use K R_2=xS+Q_H Gamma(q_2,q_2)-Kq_2. This retains both the scalar energy and every quartic residual term.

## L3. The full linearized inverse and nonlinear correction

For every source h, C23 and L4 give

```
||J_2 h||loc<=ell(x)||h||loc,
||R_2||loc<=delta(x),
ell(x)=(128/3)x+(3132/13)x^2,
delta(x)=(944984/351)x^3+(799258/39)x^4.             (L10)

```

No derivative term is omitted: L_2 is the Frechet derivative of v-xv_1-B(v,v) at q_2, because B is bilinear and symmetric. Put

```
D(x)=(1-ell(x))^2-(8/3)delta(x)
    =[46457856x^4+183150656x^3+18324072x^2
      -1168128x+13689]/13689.                       (L11)

```

Let alpha be the unique root of D in (17/1000,171/10000). This is the first positive root. Indeed D(0)=1; D'' has positive coefficients on x>=0, and D'(171/10000)<0. Hence D'<0 on that whole interval. Exact rational endpoint signs give D(17/1000)>0>D(171/10000). In particular D>=0 on [0,alpha], and ell(x)<=ell(171/10000)<1 there.

The Neumann sum of the ACTUAL J_2 constructs

```
L_2^(-1)=sum_(j>=0)J_2^j,
||L_2^(-1)||<=1/(1-ell(x)).                         (L12)

```

Its complete source coordinates are unchanged. For w=v-q_2 the full equation is

```
L_2 w=R_2+B(w,w).

```

Define z=L_2^(-1)R_2 and C=L_2^(-1)B. Then

```
||z||loc<=z_*:=delta/(1-ell),
||C(f,h)||loc<=c_*||f||loc||h||loc,
c_*=(2/3)/(1-ell).                                  (L13)

```

Construct w explicitly by the binary-tree recurrence w_1=z, w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i)). Its terms have bounds

```
||w_n||loc<=Catalan_(n-1) c_*^(n-1) z_*^n.

```

The discriminant L11 gives theta_*=4 c_* z_*<=1. The series converges absolutely on the ENTIRE closed interval, and its sum satisfies the full equation. Its bound is

```
w_*(x)=(3/4)[1-ell(x)-sqrt(D(x))],
||v-q_2||loc<=w_*(x).                               (L14)

```

At theta_*=1 the endpoint is obtained from the actual convergent Catalan series, not from a strict nonlinear contraction. Its omitted-tree tail after N>=1 is at most

```
[3(1-ell)/4] theta_*^(N+1) binom(2N,N)/4^N
 <=[3(1-ell)/4] theta_*^(N+1)/sqrt(N+1).              (L15)

```

To prove it, use Catalan*n/4^n=2(b_n-b*(n+1)), b_n=binom(2n,n)/4^n, and telescope. The original linear-source truncation has the independent exact identity and bound

```
L_2^(-1)R_2-sum_(j=0)^N J_2^jR_2
    =J_2^(N+1)L_2^(-1)R_2,
norm <=ell^(N+1)delta/(1-ell).                       (L16)

```

Thus both infinite operations have explicit residuals. Every application of J_2 adds at most two original plaquettes to its union label, and the initial R_2 has at most four. The finite linear sum in L16 is supported in actual unions of at most 4+2N plaquettes. The tree recurrence retains all further unions and all original coefficient multiplicities.

At each finite L the labelled c-weighted source is complete. Its global c-weighted sum is bounded by |E_L| times the local norm. The original spin-generator estimates bound all first and second link derivatives by that sum. Therefore the series gives a C^2 function v on the compact original product and permits the full source equation to be summed. With C3, direct differentiation gives H psi=E_0 psi. Elliptic regularity makes psi smooth. For every smooth h,

```
q_(H-E_0)(psi h)=kappa int psi^2 sum_i |X_i h|^2.

```

Multiplication and division by the positive smooth psi preserve H^1 at this finite L. This proves E_0 is the actual lowest energy and identifies psi with the original positive unit vacuum; a second ground state divided by psi has zero derivative and is constant. Gauge invariance follows from the invariant source. This identification does not presume a gap.

The convergent construction is analytic for complex |x|<alpha by the same absolute coefficient majorants. At every original power x^n its unique formal coefficient is C2, so the new construction and the earlier source constructions agree coefficient by coefficient on their common domains. Their coefficient identity maps have literal inverse identities. No new source metric or different physical vacuum is selected.

## L4. Numerical endpoint and fully retained benchmark

Exact bisection and integer-square comparisons give

```
0.0170787544707772675 < alpha < 0.0170787544707772677,
3.825973052393385 < 1/(2sqrt(alpha))
                     <3.825973052393386.             (L17)

```

This is the new sufficient coupling threshold g^2. The cubic coefficient alone, with the old generic recurrence for higher orders, gives the intermediate discriminant

```
D_3(x)=1-(256/3)x+(10720/9)x^2+(20714816/1053)x^3

```

and first root approximately 0.0166569913896066, or g^2 approximately 3.8741080015. The full linearized calculation L10–17 gives the additional improvement. Its source-specific m and t budgets are part of that gain.

At the exact original coupling g^2=4, x=1/64, a>0 and kappa=8/a,

```
ell=28973/39936,
||L_2^(-1)||<=39936/10963,
||z||loc<=33836149/808280064,
D=10028381/224280576,
theta_*=439869937/1081686321,
||w||loc<=0.047293824576905,
||w-z||loc<0.005432.                                 (L18)

```

The displayed decimal bounds are outward rational bounds checked against L13–14. They bound the ACTUAL linear response and its complete further nonlinear correction. No value of an uncomputed vacuum integral is assigned. The total source satisfies

```
||v||loc<=32x+236x^2+w_*
   =(3/4)(1-sqrt D)+(719/13)x^2.                    (L19)

```

## L5. Return to the entire physical spectrum, using the evaluated spin budget

Use the actual ground-state transform A=psi^(-1)(H-E_0)psi=kappa(K-D_v), where D_v=2Gamma(v,.). Its physical pairing is int rho conjugate(f)h dU, rho=psi^2. C5, L1 and L3 give the sharper point-spin budget

```
t(v)<=(16/3)x+(137/6)x^2+w_*/6.

```

For an original zero-Haar-mean coefficient family h, C6 and sum_e j_e<=2c(j)/3 yield

```
||D_v h||_X<=4t(v)||Kh||_X<=chi(x)||Kh||_X,
chi(x)=1/2(1-sqrt D(x))-(1136/39)x^2.                (L20)

```

Here X is the full sum of original trace coefficient norms after assembly. The scalar output is also bounded by the same complete product estimate. To check L20 without its displayed cancellation, chi is exactly

4[(16/3)x+(137/6)x^2+w_\*/6], a positive-coefficient majorant. This form proves its monotonicity. Its closed-endpoint value is strictly less than 1/2.

For an actual physical eigenfunction A f=lambda f with lambda>0, let h=Q_Hf. The source and physical-centered maps are

```
f -> Q_Hf,
h -> h-<h>_rho,
<f>_rho=0, int_H h=0.                               (L21)

```

Both compositions are identities, and h is nonzero. The original eigen-equation gives

```
(K-lambda/kappa)h=Q_H D_vh.

```

Every finite-regulator eigenfunction is smooth. Its original Fourier coefficients have summable c(j)||A_j||_1: Peter–Weyl Plancherel followed by Cauchy–Schwarz with sufficiently many Casimir powers gives this, since sum_j dim(j)^2(1+c(j))^(-N)<infinity for large N on the finite product. No volume-uniform smoothness constant is used. For 0<lambda/kappa<3, every actual nonconstant physical block has c(j)>=3, and therefore

