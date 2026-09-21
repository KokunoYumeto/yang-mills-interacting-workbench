# Volume-uniform physical coercivity and the actual zero-shift Wilson response


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
