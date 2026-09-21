# Growing original plaquette families and their full physical complement

21 September 2026. This is the quantitative return of VOLUME_UNIFORM_HEAT.md, with its source, graph, domain and semigroup proofs. Every finite open box L>=2, spacing a>0, and coupling g^2>=16 is included below. All coefficient axes are original plaquettes. Every Hilbert, energy and quotient pairing is stated explicitly. The static and time-dependent coefficient tables are the inherited original calculations, replayed unchanged; the boundary-safe assembly and rational endpoints below are new calculations. The analytic proof is written for review, not a formal certificate.

## M1. Boundary-safe full-family constants

Write R0=3/256, theta=xi/R0, and t6=theta^6/(1-theta^2). The complete marked heat tables have 199 connected multisets containing the anchor face (0,0,0;0,1): one degree-zero self term; one self and twelve adjacent-pair terms at degree two; and one self, twenty-four ordered repeated-pair, 138 path, twelve common-edge, eight corner and two cube terms at degree four. Their 559 marked-row contributions are all retained.

For each contribution, integrate its actual partial fractions as in U31, or take the original time-zero value. Sum absolute values before different original supports can cancel. Every finite box contains a subset of these original contributions at a specified anchor. Thus the following are bounds for every original row, including every boundary row, independent of box size:

| Original matrix | degree2 bound | degree4 bound |
|---|---:|---:|
|G0|149/468|2361994073/4691494080|
|G1|97/468|376882691/938298816|
|G2|73313/657072|982069718963833/3919180324550400|
|Kobs|187/468|586668421/1563831360|
|J3=G0-6G1+9G2|6779/73008|152338674005989/435464480505600|

Call these numbers B_(k,2),B_(k,4), and similarly B_K,B_J. The exact transport for every contribution is the original signed coordinate permutation and translation. The independent audit constructs the 199 original multisets without calling that transport producer, verifies its inverse coordinate formula, and reintegrates each original pole directly. The exact row entries of the existing full L2 matrix lie below these bounds; no assertion that the bulk signed row is the largest boundary row is used.

The kinetic matrix is Kobs=kappa^(-1)R*AR=<Gamma(Wp,Wq)>rho. Only p=q or faces sharing an original edge can contribute. At p=q the exact function is 4-Wp^2=3-chi_1(Wp). Its trace-coefficient norm is at most30: the original four-edge spin-one contraction has norm27, as can be obtained by contracting its three-dimensional indices, or bounded by the original tensor coefficient with one turn. For adjacent faces the direct derivative estimate U4 gives norm at most3*(8/2)^2=48. There are at most twelve neighbors. Therefore, on the full complex source disk,

    ||Kobs(zeta)||row<=30+12*48=606.                        (M1)

The spin-one contraction used for30 has the same four-link index formula as U10 with the SU(2) invariant dual matrix in dimension3; its nonzero singular values are3 with total trace norm27. In the original magnetic-weight basis its fixed dual matrix is C_(mn)=(-1)^(j-m) delta_(m,-n), m,n=-j,...,j. Thus pi_j(U^(-1))=C pi_j(U)^T C^(-1); both coefficient-side unitary factors are retained. For the trace of four general d-by-d factors with its last two transposed, the coefficient has A_(b,c,c,e ; a,b,e,a) +=1. Direct multiplication gives (A* A)^2=d^2 A* A and Tr(A* A)=d^4, so its trace norm is d^3. Taking d=3 proves27. Its inverse-link signs are represented by the stated dual matrix, not omitted. The accompanying finite check verifies the dimension2 and dimension3 contraction directly. Alternatively the bound4+8^2=68 would give644 and slightly wider kinetic endpoints.

Combining U30–U31, M1, and the table proves

    ||Gk-3^(-k)I|| <= xi^2 B_(k,2)+xi^4 B_(k,4)
                         +512(2/3)^k t6 = w_k, k=0,1,2,
    ||Kobs-3I|| <= xi^2 B_(K,2)+xi^4 B_(K,4)+606 t6=w_K,
    0<=J3<=beta I,
    beta=xi^2 B_(J,2)+xi^4 B_(J,4)+4608 t6.                 (M2)

The whole-matrix bound follows from equality of row and column absolute norm for the original symmetric real matrices, followed by the l2 Schur bound. The remainder4608=512+6*512*(2/3)+9*512*(2/3)^2 includes all three original moment errors. The matrix J3 is positive because it is exactly (R-3Phi)*(R-3Phi), with Phi=kappa A^(-1)R.

## M2. Actual numerical bounds for every original box

For xi<=1/1024, equivalently g^2>=16, theta<=1/12. Every term in (M2) is increasing in xi. Evaluation at the endpoint by exact rational arithmetic gives

    w_0<173/10^6,     w_1<116/10^6,
    w_2<77/10^6,      w_K<205/10^6,
    beta<1555/10^6.                                        (M3)

The sharper fractions, not these rounded values, are retained in generated/uniform_constants.json. Set

    l0=1-w0, u0=1+w0,
    l1=1/3-w1, u1=1/3+w1,
    l2=1/9-w2, u2=1/9+w2,
    lK=3-wK, uK=3+wK,                                     (M4)

using the endpoint rational w values. They are positive. The full physical source proof U26 gives A>=kappa d I with

    d=117/40,                                             (M5)

since at xi=1/1024 its square-root argument is11/12>(19/20)^2. This is a lower bound on the entire centered physical space, proved without selecting an observation family. All physical dimensions and original energies in (M3)–(M5) remain.

## M3. The original observation and its inverse-energy family

Let R:C^M->H0 have columns rp=(Wp-<Wp>rho)psi. On its literal coefficient coordinates put

    Phi=kappa A^(-1)R,
    G0=R*R, G1=R*Phi, G2=Phi*Phi, E=Phi*A Phi=kappa G1.

The inequalities above prove R and Phi injective and their ranges closed. The original observation O=R* has exact left inverse on the primitive family

    W=G1^(-1)R*,  W Phi=I.                                (M6)

The state projection P_R=R G0^(-1)R* retains

    ||P_R Phi c||^2=c*G1 G0^(-1)G1 c.

Using l1,l2,u0,u2 from the original matrices proves

    ||P_R Phi c||^2 >= [l1^2/(u0 u2)]||Phi c||^2
                      >(624/625)||Phi c||^2.              (M7)

This is the inverse-power observation/minimum-section mechanism of the RH workbench's IK9–12, instantiated here by the exact matrix G1^(-1)R* and the calculated physical Grams. No arithmetic constant or conductor coefficient enters (M7).

The correction between the minimum-state and minimum-energy sections of this observation is h_R=(I-P_R)Phi. Its original energy is

    h_R*A h_R
       =kappa[G1 G0^(-1)Kobs G0^(-1)G1-G1].               (M8)

Indeed expansion has two cross terms -kappa G1 and the positive section term; both are retained. Also q_A(Phi c,h_R d)=kappa<Rc,h_R d>=0. Consequently

    0<=h_R*A h_R
       <=[u1 uK/l0^2-1] E <(1/1250)E.                    (M9)

## M4. The complete surrounding physical space

The state projection onto the primitive family is instead

    P=Phi G2^(-1)Phi*, Q=I-P,
    B=QR:C^M->QH0.                                        (M10)

It gives the exact leakage Gram

    B*B=G0-G1 G2^(-1)G1.                                  (M11)

For each c, P Rc is the state minimum over Phi x. Inserting the particular original-coordinate trial x=3c gives

    0<=B*B<=(R-3Phi)*(R-3Phi)=J3<=beta I.                  (M12)

No commutativity of G0,G1,G2 is used in this argument.

Every original form vector decomposes as Phi c+h, h in QH0. Its state norm and complete energy are

    ||Phi c+h||^2=c*G2 c+||h||^2,
    q_A(Phi c+h)=c*E c+2kappa Re<Bc,h>+q_A(h).             (M13)

Since q_A(h)>=kappa d||h||^2, the complete mixed term satisfies

    |2kappa Re<Bc,h>|
       <=2 sqrt(beta/(d l1)) sqrt(c*E c . q_A(h)).          (M14)

The actual endpoint fractions give beta/(d l1)<1/625. Thus every vector in the entire physical form domain satisfies the coupled comparison

    (24/25)[c*E c+q_A(h)]
       <=q_A(Phi c+h)
       <=(26/25)[c*E c+q_A(h)].                            (M15)

The off-diagonal term is controlled, not set equal to zero. This is a full-space comparison, not a Ritz lower bound on a selected finite subspace.

## M5. The original complementary inverse and complete Schur loss

A Phi=kappa R is bounded as a coefficient map. Hence AP is bounded and PA is its adjoint. Subtract the bounded self-adjoint off-diagonal QAP+PAQ from A. The resulting self-adjoint operator has reducing subspaces PH0,QH0. Its Q restriction is

    D_Q=QAQ, Dom(D_Q)=Dom(A) intersect QH0,
    D_Q>=kappa d I.                                       (M16)

The inverse is therefore supplied by the full physical estimate, including every vector of the complementary space. Minimizing M13 over that whole space gives

    h_min(c)=-kappa D_Q^(-1)Bc,
    E_full=E-kappa^2 B*D_Q^(-1)B.                          (M17)

Testing the residual against all complementary form vectors proves this is the actual minimum, not only a finite-column stationary point. The full loss and restored state metric obey

    0<=kappa^2 B*D_Q^(-1)B
       <=(kappa beta/d)I <(1/625)E,
    (624/625)E<E_full<=E,                                 (M18)

    G_restored=G2+kappa^2 B*D_Q^(-2)B,
    G2<=G_restored<(601/600)G2.                            (M19)

The second bound uses beta/(d^2 l2)<1/600. All signs, kappa factors, original Grams and complementary feedback are retained. The graph map c->Phi c+h_min(c) has these exact energy and state forms. These estimates address the full complementary coupling left by the predecessor heat construction, with constants independent of both the number of plaquettes and the exterior box.

## M6. Fixed supports, their quotients, and a common physical heat horizon

For original face sets F subset G put V_F=Phi(C^F), U_F=A V_F=kappa R(C^F). The original complexes are

    V_F --A--> H0 --0-->0.

Their support transitions are inclusion in degree0 and identity in degree1. The exact transported kernel is

    V_G/V_F -> ker[H0/U_F -> H0/U_G], [h]->[Ah].            (M20)

Its inverse sends [Ah] to [h]. Injectivity of A on H0 proves the inverse is independent of representatives. Its coefficient-energy minimum, with J=G\F, is

    c_F=-E_FF^(-1)E_FJ c_J,
    Q_E=E_JJ-E_JF E_FF^(-1)E_FJ.                           (M21)

The removed old-support primitive Phi_F c_F and both mixed entries remain. The bounds kappa l1 I<=E<=kappa u1 I imply exactly the same bounds for every such quotient minimum in its original J coordinates. They follow by minimizing the two complete inequalities on the identical affine fiber.

For T>0 the actual heat columns and forcing defect are

    Phi_T=(I-exp(-TA))Phi=kappa int_0^T exp(-tA)Rdt,
    A Phi_T=kappa R-kappa exp(-TA)R.                       (M22)

The omitted primitive is -exp(-TA)Phi. On the complete centered physical space, I-exp(-TA) has inverse sum_(n>=0)exp(-nTA), also on the graph domain, and commutes with A. Thus it gives a cochain isomorphism of every original support diagram. Applying the Split Zero support reconstruction retains its support label and receiving zero together with this actual primitive.

Set epsilon=exp(-kappa d T). Expanding all three heat Gram terms and then applying spectral calculus yields

    (1-epsilon)^2 G2<=Phi_T*Phi_T<=G2,
    (1-epsilon)^2 E<=Phi_T*A Phi_T<=E.                     (M23)

Taking minima over the same fixed fibers carries these inequalities through every finite sequence of original restrictions and quotients, without multiplying a constant for each step. This is precisely the HM19–24 minimum-fiber argument of the RH source, whose coefficient maps remain fixed before the metric comparison. Each rank remains in the determinant bound:

    |L_T-L|<=2 B[-log(1-epsilon)]<=2B epsilon/(1-epsilon),
    B=sum_j |a_j| rank_j, L=sum_j a_j log det Q_j.          (M24)

Rank-zero terms keep determinant1. For four signed returns of rank at most240, the single physical horizon T=10/kappa=5a/g^2 gives an error below4*10^(-10), in every exterior volume. For ranks that grow with M, a specified tolerance eta>0 is reached at the explicit original physical time

    T=(kappa d)^(-1)log(1+2B/eta).                         (M25)

Thus no growing determinant rank has been discarded. The original kappa^rank factors cancel only between the two determinants in the identical energy frame.

## M7. The actual opposite-face result in every exterior box

Keep p=(0,0,0;0,1), q=(0,0,1;0,1), xi=10^(-10), g^2=50000 and kappa=100000/a. Their inherited complete coefficient h4(tau) has zero degrees0 and2. All original supports contributing to degree4 lie inside the L=2 box; hence the same h4 applies in every L>=2. The new uniform tail U30 gives

    85910/10^7 < C_pq(1/kappa;xi)/xi^4 < 85920/10^7.        (M26)

The previously proved exact coefficient lower bound h4(tau)>=5 exp(-3tau)/648, tau>=1, is kept. On 1<=tau<=3 the ratio of U30's full remainder to that lower bound is at most

    (512*648/5) xi^2 R0^(-6)
       exp(9/2)/[1-(xi/R0)^2] <24/1000.                   (M27)

Thus the actual connected heat correlation is strictly positive throughout 1/kappa<=t<=3/kappa, uniformly over the original exterior volume. The result also passes to the constructed spatial-volume limit U33. These statements use all higher orders, not only the sign of h4.

## M8. Infinite plaquette families and the original continuum path

The row-tail and local-limit constructions U9 give bounded operators G0,G1,G2,Kobs on l2 of all original plaquettes, with exactly the same numerical intervals (M2)–(M5). On finitely supported c, R c is the original centered local observable in L2(mu)_phys. In this infinite-family statement Kobs denotes the closed-form pairing kappa^(-1)q_(A_infty)(R.,R.), whose boundedness follows from U33 and the cylinder-generator identity after it. It does not require asserting that A_infty R is a bounded operator on all l2 coefficients. G0 proves this map extends boundedly and is bounded below. Define Phi=kappa A_infty^(-1)R. Then G1,G2 are its original mixed and state Grams by the convergent physical heat integrals. They are bounded and bounded below, so P=Phi G2^(-1)Phi* is again an actual orthogonal projection.

A_infty Phi=kappa R is bounded; hence A_infty P and PA_infty have the same bounded off-diagonal argument as M16. All maps, complementary minima and inequalities M6–M19 therefore pass to the complete infinite plaquette coefficient space and its full physical complement. This passage uses proved bounded operators, not a formal limit of inverses without a lower bound.

At fixed admissible g,a this controls the spatial-volume limit. For the original simultaneous path a_n=a0*2^(-n), g_n^2=1/(g0^(-2)+beta n log2), the source disk used in U13 is entered exactly when c_n=g0^(-2)+beta n log2<sqrt(3)/8. The narrower numerical metric domain is c_n<=1/16. For beta>0 the path eventually leaves each of them. The current result removes the 1/M heat radius and the unbounded observation-rank loss on a specified strong-coupling domain; it does not establish a smooth four-dimensional continuum field or finite continuum mass. No universal conclusion is inferred merely from a support kernel or an auxiliary norm.

## M9. What is new in this continuation

The older elementary local source argument U3–U6 has been rederived at its own conservative radius. The new calculation combines its full scalar return with the Poisson identity U21 to bound an entire heat-matrix row, not just one entry. This produces the original box-independent analytic remainder U30–U31. The 199-support absolute assembly then gives original state/response/kinetic metrics for growing families, and M12–M19 controls their full complementary coupling. The spatial and physical maps are explicit throughout. No larger coupling threshold or previously unaudited historical theorem is assigned a new verification status.

## M10. Sharper original-Haar return and broader family domains

The additional bound U29b gives the same complete inverse-moment errors with the smaller circle R1=45/4096 and prefactors (6184/25)(8/15)^k. For a fixed real x in that disk put t0=(x/R0)^6/[1-(x/R0)^2], t1=(x/R1)^6/[1-(x/R1)^2]. Define the actual scalar error bounds

    w_k^sharp=x^2 B_(k,2)+x^4 B_(k,4)
       +min(512(2/3)^k t0,(6184/25)(8/15)^k t1), k=0,1,2,
    beta^sharp=x^2 B_(J,2)+x^4 B_(J,4)
       +min(4608t0,(6184/25)[1+6(8/15)+9(8/15)^2]t1).

The kinetic w_K from M2 is retained. Each scalar expression is increasing in x. Replacing the endpoint l and u values in the already proved M7–M19 inequalities by these evaluated sharper endpoints gives the following complete original-family bounds, all uniform over L>=2 and a>0:

|g^2 at least|observed fraction in M7 exceeds|E_full/E exceeds|G_restored/G2 is less than|h_R energy / E is less than|
|---|---:|---:|---:|---:|
|10|39/50|18/25|33/25|1/6|
|12|97/100|243/250|103/100|1/60|
|16|999/1000|999/1000|1001/1000|1/1900|

Here every entry with matrix forms means the displayed Loewner inequality in the same original coefficient coordinates. The full-space gap lower constants used in those three rows are respectively d=14/5,72/25,117/40 times kappa. Each follows directly from U26 by squaring its positive rational comparison. The file generated/sharp_constants.json contains every rational input, interval endpoint and returned fraction; the independent auditor recomputes each from the original marked coefficients.

At g^2>=16 the absolute Gram widths obey

    ||G0-I||<124/10^6,
    ||G1-I/3||<66/10^6,
    ||G2-I/9||<36/10^6,
    ||Kobs-3I||<205/10^6,
    B*B< (832/10^6) I.

The exact unrounded beta^sharp/(d l1^sharp) is smaller than 1/34^2. Accordingly the full mixed-space comparison M15 sharpens to

    (33/34)[c*E c+q_A(h)] <= q_A(Phi c+h)
                            <=(35/34)[c*E c+q_A(h)].       (M28)

The full complementary minimization loses less than 1/1000 of E and adds less than 1/1000 of G2 to the restored state norm. No complementary vector or source-kernel direction is removed. The same bounded-operator argument in M8 carries these stronger constants to the infinite original plaquette family. The earlier M2–M27 endpoints remain valid and have their own exact records; this paragraph retains an additional, explicitly proved original-Haar estimate rather than silently replacing their coefficients.
