# Original Yang–Mills heat correlations: the complete fourth-degree return

21 September 2026. This is an additive continuation of the recovered cumulative
workbench. The original open-box SU(2) operator, physical units, Haar measure,
gauge constraints and source coordinates remain. The coefficient calculation
uses the complete available fifth-source archive. The separately saved sixth-source
proofs are preserved with their recovery status; their missing catalogues are
not prerequisites for this calculation. General exponential-vacuum and character
methods retain Schütte–Zheng–Hamer (1996) as a human antecedent. The exact finite
calculations here are accompanied by analytic proofs and executable audits;
independent external analytical review and historical priority are not asserted.

## H1. The actual operator and time coordinate

For L>=2 use every vertex n in {-L,...,L}^3, every contained positive edge
(n,i), and every contained elementary face p=(n;i,j), i<j. Put

    W_p=tr(U_i(n) U_j(n+e_i) U_i(n+e_j)^(-1) U_j(n)^(-1)),
    T_alpha=-i sigma_alpha/2,
    X_e,alpha f=d/ds f(...,exp(s T_alpha)U_e,...) at s=0,
    K=-sum_(e,alpha) X_e,alpha^2,
    H(x)=kappa K+kappa sum_p x_p(2-W_p),
    kappa=2g^2/a,   x_p=xi=1/(4g^4) on the homogeneous line.       (H1)

The inner product on the original product Haar probability space is conjugate
linear in its first entry. The physical subspace is invariant under all vertex
gauge transformations, including boundary vertices. The domains are the physical
parts of H^2 and H^1. The original bounded smooth potential preserves these
domains; the compact elliptic operator has a smooth strictly positive unit
ground state psi_x with energy E0(x). These domain and vacuum facts are the
ones in the pinned original finite-box source (SOURCE_INTAKE.json, YM0).

The coefficient operator and its inverse physical return are exactly

    B_x=(H(x)-2kappa sum_p x_p I)/kappa=K-sum_p x_p W_p,
    H(x)=kappa B_x+2kappa sum_p x_p I,
    E0(x)=kappa[2sum_p x_p+e(x)].                              (H2)

Both scalar energy terms remain in the return. Let A_x=H(x)-E0(x) and
r_p=(W_p-<W_p>_rho)psi_x, rho=psi_x^2. Define

    C_pq(t;x)=<r_p,exp(-t A_x)r_q>,
    Chat_pq(tau;x)=C_pq(tau/kappa;x),
    tau=kappa t,   t=tau/kappa.                              (H3)

This is an invertible physical-time change; no link or field coordinate is
changed. The Laplace variable z below is conjugate to this stated tau:

    F_pq(z;x)=int_0^infinity exp(-z tau) Chat_pq(tau;x) dtau
             =kappa <r_p,(A_x+kappa z)^(-1)r_q>.              (H4)

All expressions are initially at real sufficiently small x and z>0. The
separate analytic proof gives their full domains and uniform time remainders.

## H2. The complete coefficient recurrence, including the ground pole

Retain the source section u=psi_x/m_x, m_x=P_H psi_x. Its inverse is
psi_x=m_x u, and its original scalar obeys m_x^2<u,u>_H=1. Thus P_H u=1
and the original norm N(x)=<u,u>_H is kept in every expectation. Expand
u(x)=sum_nu u_nu x^nu, e(x)=sum_(nu!=0)e_nu x^nu, with u_0=1,
P_H u_nu=0 for nu!=0. The exact eigen-equation gives

    e_nu=-sum_(j:nu_j>0) P_H(W_j u_(nu-e_j)),
    K u_nu=sum_j W_j u_(nu-e_j)
              +sum_(0<mu<=nu)e_mu u_(nu-mu).                 (H5)

The last term includes e_nu u_0, and its Haar scalar makes the RHS centered.
Its unique centered inverse is the original K^(-1)Q_H. The recovered coefficient
engine supplies these actual finite coefficients and all their source labels.

For a marked face q, define h_q(z;x)=(B_x-e(x)+z)^(-1)W_q u(x).
Its coefficient equation is

    (K+z)h_(q,nu)=W_q u_nu+sum_j W_j h_(q,nu-e_j)
                         +sum_(0<mu<=nu)e_mu h_(q,nu-mu).     (H6)

The source index may include repeated faces; all multiplicities remain literal
multiindex coefficients. Define

    N_nu=sum_(alpha+beta=nu)<u_alpha,u_beta>_H,
    Mp_nu=sum_(alpha+beta=nu)<u_alpha,W_p u_beta>_H,
    Hpq_nu=sum_(alpha+beta=nu)<u_alpha,W_p h_(q,beta)>_H.        (H7)

Coefficient division by N, with N_0=1, gives the original mean mu_p=Mp/N
and the uncentered resolvent Hpq/N. The complete connected answer is

    F_pq=Hpq/N-mu_p mu_q/z.                                  (H8)

The subtracted term is retained as an actual ground-state contribution. The
source shift e_mu in (H6), both norm divisions and this term are all required.
Every resulting coefficient in the catalogue has zero coefficient at each
power z^(-j), j>0. The original positive free excitation gap also proves this
cancellation analytically near (x,z)=(0,0), after the ground projection is removed.

## H3. Exact original Casimir inversion and time reconstruction

An original invariant trace monomial has a finite tensor representation on its
original edge set. For r_e occurrences on edge e, the allowed doubled spins are
r_e,r_e-2,... . At each original vertex the sum of the doubled spins is even,
and no one exceeds the sum of the others. These are the SU(2) invariant-tensor
conditions: iterated angular-momentum addition supplies every intermediate spin
in the parity-compatible interval, so zero belongs exactly on those conditions.
The resulting finite Casimir list contains all eigenvalues of that monomial.
It retains multiplicities inside every equal-eigenvalue eigenspace.

For its distinct values C, use the literal original operator projectors

    P_c=product_(d in C,d!=c)(K-dI)/(c-d),
    (K+z)^(-1)f=sum_(c in C) P_c f/(z+c).                     (H9)

The full physical operator has all spins. The finite list in (H9) is the complete
representation space reached by that Taylor coefficient and its marked word.
It does not discard a path contributing to the coefficient.

Every response coefficient is stored as exact partial fractions

    F_nu(z)=sum_(c>0,n>=1) a_(c,n)/(z+c)^n.                   (H10)

Their time functions are exactly

    Chat_nu(tau)=sum_(c,n) a_(c,n) tau^(n-1)exp(-c tau)/(n-1)!.(H11)

Indeed direct integration of each finite term gives (H10). The analytic
heat construction in the companion proof shows these are the actual Taylor
coefficients, and uniqueness of the Laplace transform identifies them.
For explicit uniqueness, weighting a vanishing transform by exp(-s0 tau)
produces a finite complex measure; x=exp(-tau) carries its integer Laplace
samples to all polynomial moments on [0,1]. Polynomial approximation forces
the measure to vanish; continuity gives equality of the time functions.

Products in the partial-fraction engine are also exact. For a!=b, the principal
part of (z+a)^(-m)(z+b)^(-n) at -a has coefficients

    (-1)^k binom(n+k-1,k)/(b-a)^(n+k),  k=0,...,m-1,          (H12)

at power (z+a)^(-(m-k)); the analogous -b principal part is retained. Their
sum has the same two principal parts and vanishes at infinity, so the rational
functions are equal. Coincident poles add their orders. This retains every
repeated pole and hence every time-polynomial factor in (H11).

The exact original source equation (H6) is audited as a complete polynomial in
all retained tree/chord quaternion coordinates, separately for every pole.
The map is Z_e=t_s U_e t_t^(-1), with its original inverse
U_e=t_s^(-1)Z_e t_t and the tree variables retained. On each chord,
Z=x0 I-i sum x_a sigma_a and sum_(a=0)^3 x_a^2=1. The remainder basis has
x0 exponent zero or one. The map and injectivity argument are the recovered
fifth-source coordinate proof, unchanged. Every residual coefficient is zero
in this full product-of-spheres algebra, not merely at sampled links.

## H4. Complete support classification and original box assembly

A change U_e -> -U_e multiplies each source or marked trace using e by -1.
Thus a nonzero coefficient has an even total multiplicity on every original
edge, counting both marked traces. At total face multiplicity 2 or 4 this
requires all face multiplicities even. At total multiplicity 6 it permits,
in addition, the six distinct faces of one elementary cube. The original
closed cubical two-chain argument is retained in the sixth-energy proof:
a nonempty closed mod-two face set has at least six faces; at six, each of
the four edges of an extreme face requires its adjacent side face, and closure
of their remaining edges forces the opposite face. The resulting set is the
boundary of that original cube.

A disconnected face source factors over disjoint original edge factors. The
original operators, positive vacua and their means factor accordingly. A source
component containing neither mark cancels between numerator and N; marks in
different components have zero connected correlation. This remains true with
shared graph vertices: the full tensor-product Hamiltonian and the actual
invariant vectors give the same physical expectation. Connectedness therefore
means sharing original edges, exactly as in the source catalogue.

The complete list is:

| heat/source degree | total face multiplicity including marks | coordinate cases | marked responses |
|---|---|---:|---:|
| 0 | 2 | 1 | 1 |
| 2 | 4 | 3 | 7 |
| 4 | 6 | 13 | 76 |

There are 84 full rational time functions. At total degree six the cases are
one single face, two geometries of an ordered 4+2 pair, seven geometries of a
three-face path, one common-edge triple, one cube corner and one cube. All marks
and all allowed diagonal marks are retained. Faces with repeated multiplicity
are never replaced by a factorial convention.

A signed coordinate permutation and translation

    y_i=epsilon_i x_(pi(i))-d_i,
    x_(pi(i))=epsilon_i(y_i+d_i)                              (H13)

transports every actual face multiset and both marked faces to its record.
Each original edge is mapped to the corresponding forward or inverse edge.
The product-Haar map is unitary, carries K to K on that support, and maps the
actual face words to the target face word or its inverse. In SU(2), tr(U^-1)=tr(U)
by the two eigenvalues lambda,lambda^-1; hence the same trace is returned.
The inverse in (H13) returns every source to its original coordinates.

The L=2 assembly retains all 240 original faces, 1,128 adjacent pairs, 6,732
paths, 576 common-edge triples, 512 corners and 64 cubes. The coefficient
matrices have respectively 240, 2,496 and 9,660 nonzero entries. Their entire
time integrals agree entry by entry with the preceding static matrices:

    int_0^infinity Chat_0(tau)dtau=I/3,
    int_0^infinity Chat_2(tau)dtau
      =-(5/36)I+(2/1053)D_degree+(4/1053)A_adj,                (H14)

and the full original Chat_4 integral is the previously calculated R4,
including every boundary row and cube. All complete matrices and all their
coordinate transports are in generated/heat_matrix_L2.json and
heat_transports_L2.json. Those files preserve the original face ordering.

## H5. Explicit time-dependent functions

For one original plaquette with only its own source parameter, the degree-two
coefficient is

    exp(-3tau)[-241/900-(7/15)tau]+(4/225)exp(-8tau).          (H15)

For two different faces sharing one original edge, the coefficient of x_p x_q is

    exp(-3tau)[-409/17199+tau/21]
       +exp(-9tau/2)/36+exp(-13tau/2)/588.                    (H16)

Its integral is 4/1053 and its value at zero is 2/351. The corresponding
diagonal, neighbour-source term replaces -409/17199 by -13/441; its integral
is 2/1053 and its time-zero value is zero. These distinct values retain the
full source and state pairings.

Now take opposite faces

    p=(0,0,0;0,1),  q=(0,0,1;0,1).                          (H17)

Their coefficients at degrees zero and two vanish. Four original three-face
paths and one original cube contribute at degree four. One path gives

    P(tau)=exp(-3tau)[75173779/67612708800
                     -(4441/3611790)tau+tau^2/882]
       -(121/108864)exp(-9tau/2)+(1/11664)exp(-6tau)
       -(197/9988160)exp(-13tau/2)+(1/163800)exp(-8tau)
       +(1/6492304)exp(-10tau).                              (H18)

The cube gives

    B(tau)=exp(-3tau)[-235/648+(10/27)tau]
       +exp(-9tau/2)[1123/2916+(23/81)tau+tau^2/18]
       +(1/648)exp(-6tau).                                  (H19)

Thus the complete actual degree-four coefficient is

    h_4(tau)=4P(tau)+B(tau),
    h_4(0)=8869/365040,
    int_0^infinity h_4(tau)dtau=641033/29568240.               (H20)

All six decay rates and both repeated-pole orders remain. The coefficient
at tau=1 is enclosed by rational exponential bounds in generated/heat_bounds.json;
its numerical size is approximately 0.00859150755. This diagnostic decimal is
not an acceptance test. The companion proof turns (H20) into intervals for the
full actual correlation, retaining every higher Taylor order.

## H6. Independent checks on the same original geometry

The single-plaquette check uses the infinite original character basis chi_(j/2),
where K chi_(j/2)=j(j+2)chi_(j/2) and
W chi_(j/2)=chi_((j-1)/2)+chi_((j+1)/2), with the negative-index term zero.
At order n every contributing insertion path has j<=n+1; the independent
recurrence retains all these indices. It reproduces all three self-source
heat coefficients, with both original norm divisions and the ground pole.
Its integrated coefficients are 1/3,-5/36,289/5184. They also follow by twice
differentiating the retained one-plaquette energy coefficients. The original
radial coordinate return e_one(xi)=b_2(-4xi)/4-1 matches the NIST DLMF 28.6.5
expansion; the map and scalar energy term are in the recovered audit report.
This comparison covers that one-plaquette coefficient convention only.

There is an additional computation for every marked cube pair. Orient the six
faces outward. Original Haar integration yields 2^8/2^12=1/16. For any proper
visited face subset S, each edge already visited twice can never occur in a
later insertion. Its surviving representation is the original spin zero; each
boundary edge carries the remaining spin one-half. Therefore its original
intermediate energy is c(S)=3|boundary S|/4.

For marks p!=q, arrange the other four faces in a permutation and split the
ordered list into right-vacuum, middle-heat and left-vacuum pieces. All 24
permutations and all 15 length triples occur. Right and left vacuum prefixes
contribute 1/c(S); the middle heat state begins at {q} union right and each
middle insertion contributes 1/[z+c(S)]. The original 1/16 remains. Summing
these 360 rational functions gives exactly the cube coefficient in (H10).
All fifteen marked cube pairs were checked: 5,400 complete original insertion
records, including every intermediate boundary energy. This calculation imports
none of the trace-differentiation or Casimir-projection engine.

The time-zero covariance, its first derivative -<Gamma(W_p,W_q)>_rho,
and its second derivative <[K,W_p]u,[K,W_q]u>_H/N are also calculated separately
from the entire original density quotient at each coefficient. All 84 rational
functions reproduce these three values. The full-polynomial source audit and
these moment identities have distinct execution records.

## H7. Sources and present mathematical scope

The original operator/domain and maximal-tree maps are the pinned finite-box
workbench source. The exponential and character/Casimir antecedent is
D. Schütte, Zheng Weihong and C. J. Hamer, arXiv:hep-lat/9603026. The residue
and minimum-section comparison imported from the current Split-Zero heat
work is specified completely in RH_HEAT_TRANSFER.md, with its exact source
revision and read equations. No arithmetic period or Gamma constant is
assigned to a physical Yang–Mills matrix.

These are actual finite-regulator heat coefficients and actual finite-volume
analytic bounds. The Cauchy radius in the companion is 1/M. It therefore
retains dependence on the original volume, and does not supply an ultraviolet
continuum construction. The earlier uniform-gap manuscripts retain their
recorded independent-audit qualification.

## H8. The complete fourth-order first-band return in its original metric

The original free energy-three space is exactly span{Wp}. To see the next
separation, an active invariant graph with four edges is a four-cycle; its
vertex intertwiners force equal edge spins, giving energy 4j(j+1)=3,8,... .
A simple bipartite active graph with five edges and minimum degree at least two
would have one cyclic component with five vertices and five edges, hence an
odd five-cycle, or at most four vertices, where bipartiteness permits at most
four edges. Both cases contradict its assumptions. Therefore any other active
assignment has at least six edges and energy >=9/2. Thus

    spec(K_phys) subset {0,3} union [9/2,infinity),
    P3H_phys=span{Wp},   dim P3=M.                           (H21)

For sufficiently small real xi let Pi_xi be the complete spectral projection
near energy 3 of B_xi-e(xi), and put

    Y_xi c=Pi_xi sum_p c_p r_p,
    Gband=Y_xi*Y_xi,
    (B_xi-e)Y_xi=Y_xi Aband.                                (H22)

The exact quantitative construction below proves invertibility of this frame
onto the actual band. At xi=0, c->sum c_p Wp is the original Haar isometry R0.
Projection of the heat resolvent onto its original energy-three poles gives

    Cband(tau)=Gband exp(-tau Aband),
    Gband=I+xi^2 G2+xi^4 G4+...,
    Aband=3I+xi^2 T2+xi^4 T4+....                            (H23)

The original center symmetry makes both matrices even. For each of the full
heat matrices let A_(n,j) be the coefficient of (z+3)^(-j). Then literal
multiplication of the two series in (H23) proves

    G2=A_(2,1),  G4=A_(4,1),  T2=-A_(2,2),
    A_(4,3)=T2^2,
    T4=-A_(4,2)-G2 T2.                                    (H24)

All matrix factors retain their order. The complete L=2 calculation gives

    T2=(7/15)I-(D_degree+A_adj)/21.                          (H25)

It gives all 9,660 nonzero entries of T4 and all 9,660 entries of G4 in
first_band_L2.json. Every entry of A_(4,3)=T2^2 is checked. Original
self-adjointness returns through the full Gram as

    Gband Aband=Aband* Gband,
    T4-T4* = T2 G2-G2 T2.                                  (H26)

The right side has 1,440 nonzero entries for this open box. For the original
faces (-2,-2,-2;0,1) and (-2,-1,-2;0,1), the displayed difference is exactly
2/7371. This is the explicit correction between the coordinate adjoint and the
original metric adjoint. Its value is retained, rather than forcing a symmetric
coefficient matrix by dropping the mixed product.

Here is a complete analytic remainder for (H23). Work on the complex
homogeneous circle |zeta|=1/(32M). The original ground/complement calculation
in A1--A2 applies with ||W||^2=eta=1/(1024M) and Re D>=47/16. On |e|=eta,
||Z(D-e)^(-1)W||<eta, so the same scalar argument principle gives |e|<=eta.
Consequently

    ||B_zeta-e-K|| <=1/16+1/(1024M)<1/15.                    (H27)

On the spectral circle |lambda-3|=1/2 the original free resolvent has norm
at most 2. Its norm-convergent resolvent series gives

    ||Pi-P3|| <=2/13,
    ||(B_zeta-e-3)Pi||<=1/13.                               (H28)

For the first inequality, integrate the difference of resolvents: the bound
is 2b/(1-2b) with b<=1/15. For the second, integrate that difference multiplied
by lambda-3, obtaining b/(1-2b). The corresponding free integral is zero
because (K-3)P3=0. The circle encloses exactly the original M-dimensional
band, by the same resolvent homotopy and finite rank at zero.

Use the exact Haar section u=1+w, where ||w||<=1/(92sqrt(M)); the denominator
in its block inverse exceeds 23/8. The column map Fu:c->sum c_p Wp u satisfies

    ||Fu-R0||<=2sqrt(M)||w||<=1/46.

Define Yhat=Pi Fu. Its original coefficient map obeys

    ||R0*Yhat-I||<=107/598,
    ||(R0*Yhat)^(-1)||<=598/491.                             (H29)

Indeed the two contributions are Pi-P3 and Pi(Fu-R0), bounded by 2/13 and
(15/13)/46. Its inverse on the band is (R0*Yhat)^(-1)R0*. The actual unit-vacuum
frame is Y=m Yhat, with psi=m u and m^2<u,u>_H=1 retained. Its scalar cancels
from the operator intertwining, not from Gband. Thus

    Aband=(R0*Yhat)^(-1)R0*(B_zeta-e)Yhat,
    ||Aband-3I|| <=(598/491)(1/13)(47/46)=47/491.             (H30)

All these maps are analytic on a neighborhood of the closed source circle.
The original center involution sends Yhat_-zeta=-C Yhat_zeta and R0*C=-R0*,
so Aband is even. Cauchy's formula and the full even tail prove

    ||Aband-3I-xi^2T2-xi^4T4||
      <=(47/491)(32M|xi|)^6/[1-(32M|xi|)^2],
                         |xi|<1/(32M).                    (H31)

Multiplication by kappa returns this to physical energy. This is an actual
finite-volume matrix remainder, with all original band coordinates, the
nonidentity Gram (H23), and the dependence on M retained. No diagonalization
of T4 or uniform-in-volume fourth-order spectral claim is inferred here.
