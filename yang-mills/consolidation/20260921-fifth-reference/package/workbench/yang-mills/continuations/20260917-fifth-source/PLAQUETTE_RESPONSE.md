# Full signed plaquette susceptibility and a finite-volume analytic enclosure

17 September 2026. This calculation returns the original source derivatives to the actual vacuum and its zero-energy resolvent. It gives the complete homogeneous response matrix through degree four, including a nonzero entry between opposite cube faces, and an explicit remainder for the actual finite-volume response. Its analytic proof uses only the original free physical spectrum and bounded original plaquette multiplication. Its radius retains its volume dependence.

## P1. Actual Hamiltonian derivatives and original metric

Retain F1-F4 of `FIFTH_SOURCE.md`. Put A=H(x)-E_0(x), rho=psi_x^2, and let the original unitary map U_psi send f to psi_x f. Its inverse is f -> f/psi_x. The equality

    <U_psi f,U_psi h> = int rho conjugate(f)h dU                (P1)

proves both its scalar-product preservation and its stated inverse. The transported excitation operator is

    Atilde=U_psi^* A U_psi=kappa[K-2Gamma(v,.)],
    q_Atilde(f,h)=kappa int rho sum_i conjugate(X_i f)X_i h dU.  (P2)

The potential is the complete original potential in F3. Formula P2 follows from its exact ground-state equation and integration by parts; it retains the original energy coefficient kappa.

Write z_p=partial_xp v. Differentiating the original unit-vacuum mass gives

    partial_xp c=-<z_p>_rho,
    partial_xp psi=psi Z_p,
    Z_p=z_p-<z_p>_rho.                                        (P3)

The derivative of the full Hamiltonian is kappa(2-W_p). Its actual eigen-equation gives

    partial_xp E_0=kappa(2-<W_p>_rho),
    Atilde Z_p=kappa(W_p-<W_p>_rho).                           (P4)

Every operator and derivative in these formulas is on the original compact finite graph. The strictly positive simple vacuum and the isolated branch constructed below justify the differentiations. Define the original centered states

    r_p=(W_p-<W_p>_rho)psi.

Their zero-energy response matrix is

    R_pq(x)=kappa <r_p,A^(-1)r_q>
           =-1/2 partial_xp partial_xq e(x)
           =q_Atilde(Z_p,Z_q)/kappa.                          (P5)

For real source coordinates and trace observables these entries are real. Indeed the ground state and all differentiated states can be chosen real. Differentiating <W_p> and using P3-P4 gives partial_xq<W_p>=2kappa<r_p,A^(-1)r_q>, proving P5 with its full off-diagonal entries. On complex linear combinations the same matrix is Hermitian positive semidefinite by the actual resolvent pairing.

The original integrated connected Euclidean correlation is

    int_0^infinity <r_p,exp(-tA)r_q> dt = R_pq/kappa.            (P6)

The finite positive spectral gap below proves convergence of the integral. The factor 1/kappa remains in the physical return. P3-P5 also give the exact physical minimum-energy primitive of the source: the centered logarithmic derivative is kappa times the inverse applied to the original centered observable. Its raw state and energy norms are unchanged.

## P2. Sixth-order source data, with each original multiplicity

The complete previous sixth-energy calculation is re-evaluated here on its seven geometric input cases using both the logarithmic-source recurrence and the separate linear eigenvector recurrence. Their common trace/Haar dependency is explicitly retained. The inhomogeneous scalar polynomials are

    e_2=-sum_p x_p^2/3,
    e_4=(5/216)sum_p x_p^4-(2/1053)sum_{p,q adjacent} x_p^2x_q^2,
                                                                    (P7)

where the second sum is over unordered original adjacent pairs. At degree six,

    e_6=a sum_p x_p^6
        +b sum_{p,q adjacent}(x_p^4x_q^2+x_p^2x_q^4)
        +sum_{p,q,r connected} c_type x_p^2x_q^2x_r^2
        +d sum_cubes C product_(p in boundary C) x_p,           (P8)

with every triple unordered and consisting of distinct original faces, and

    a=-289/77760,
    b=22285/47309184,
    c_path=-4909/118272960,
    c_common=244/4312035,
    c_corner=-212/542997,
    d=-83/1944.                                               (P9)

The two pair monomials in P8 are exchanged by the literal bijection (p,q,4,2) -> (q,p,4,2). On the homogeneous line their joint contribution is 2b. This is the exact map from the incoming report's unordered-pair total 22285/23654592 to the ordered multiplicity coefficient used in the Hessian.

For completeness of the degree-six support possibilities, the original independent link-center action forces the parity of the face multiplicities to be a cubical two-cycle. A finite such cycle bounds a finite mod-two three-chain: one explicit filling assigns to a cube at (x,y,z) the sum modulo two of the horizontal-face coefficients above it in that column. The two-cycle equations make its other boundary faces exactly the specified vertical faces; the coefficients vanish outside a finite set. A nonempty set of at least two cubes has projections onto at least two coordinate planes of size at least two and onto the third of size at least one. Each occupied column contributes at least two exposed faces. Its boundary therefore has at least ten faces. Thus a nonzero two-cycle with at most six faces is exactly one cube boundary. The other degree-six possibilities have all face multiplicities even and at most three distinct faces. Connectivity leaves precisely the cases P8-P9. No original cube term is omitted.

The cube coefficient has a separate complete calculation. Every one of its twelve edges occurs once in each orientation in the outward face product. Haar contraction yields one factor 1/2 per edge and one free two-dimensional vertex index at each of its eight vertices, giving 2^8/2^12=1/16. For a face insertion order pi, the proper intermediate subset A_j has its original boundary energy 3|boundary A_j|/4. Consequently

    d=-(1/16)sum_(pi in S_6) product_(j=1)^5 [4/(3|boundary A_j|)]
     =-(1/16)(166/243)=-83/1944.                               (P10)

All 720 orders are recomputed in the checker.

## P3. An independent finite-volume analytic disk

The original free physical spectrum has simple eigenvalue zero with vector 1. Every other physical product-representation block has an active edge graph of minimum degree at least two: an isolated nontrivial representation at a vertex admits no invariant vector. A finite graph of minimum degree at least two contains a cycle. The original cubic graph has no triangles and no doubled edges, so the cycle has at least four original edges. Each nonzero spin contributes at least 3/4. Therefore

    K|_{physical, 1-perp} >=3.                                (P11)

Consider the original bounded perturbation B(x)=-sum_p x_p W_p, with complex x. Since |W_p|<=2,

    ||B(x)||<=2||x||_1.                                       (P12)

On the contour |z|=3/2, the original resolvent (K-z)^(-1) has norm at most 2/3. Hence I+B(x)(K-z)^(-1) is invertible by its geometric series for ||x||_1<3/4. The contour projection of K+B(x) is analytic there. Along the radial path from zero its rank is constant and equals one. It defines one analytic eigenvalue e(x) with e(0)=0.

On ||x||_1<=3/8, P12 gives ||B||<=3/4. Outside distance ||B|| from spec K, the same resolvent factorization is invertible. The selected eigenvalue lies inside |z|<3/2 and therefore within distance 3/4 of zero, rather than of the remaining spectrum starting at three. This proves

    |e(x)|<=3/4 for ||x||_1<=3/8.                             (P13)

For real x in this region, the original min-max inequalities give E_1(K+B)-E_0(K+B)>=3-4||x||_1>0. The selected real eigenvalue is the actual ground energy with its original scalar 2kappa sum x restored. These arguments do not use any earlier uniform-volume source-series bound.

Let M be the actual number of original plaquettes, and set

    r=3/(16M),   a_source=3/32.                                (P14)

For |z|<=r and |u|,|w|<=a_source, the original parameter vector z*1+u e_p+w e_q has l1 norm at most 3/8. Cauchy's two-variable integral, including p=q where both variables perturb the same source, gives

    |partial_u partial_w e(z*1+u e_p+w e_q) at (0,0)|
       <=(3/4)/a_source^2=256/3.

Thus P5 has the explicit bound

    |R_pq(z*1)|<=128/3 on |z|<=r.                             (P15)

The original central link substitution F21 sends every W_p to -W_p while preserving K and Haar. It carries K+B(x) to K+B(-x); uniqueness of the analytic eigenvalue gives e(-x)=e(x). Consequently R_pq(z*1) has only even powers. Cauchy's coefficient estimate and the geometric sum give the complete tail

    |R_pq(xi)-R_(0),pq-xi^2 R_(2),pq-xi^4 R_(4),pq|
       <=(128/3) (|xi|/r)^6/[1-(|xi|/r)^2],  |xi|<r.          (P16)

The actual M and physical kappa are retained. For any finite complex coefficient vector h, summing the entry bound gives the corresponding quadratic-form error at most the right side of P16 times (sum_p |h_p|)^2. The complete cross terms are included in this sum.

## P4. The full response matrix through degree four

Twice differentiating each original monomial P7-P8 and then applying P5 gives

    R(xi)=(1/3)I+xi^2 R_(2)+xi^4 R_(4)+remainder,
    R_(2)=-(5/36)I+(2/1053)D_degree+(4/1053)A_adj.              (P17)

Here D_degree contains the original face-adjacency degrees, including boundaries, and A_adj is their actual adjacency matrix. For a face p, let t_p^tau count original connected distinct triples of type tau containing p. Let t_pq^tau count those containing p and q, and c_pq count original cubes containing the two distinct faces. The entire degree-four matrix is

    R_(4),pp=-15a-7b d_p-sum_tau c_tau t_p^tau,
    R_(4),pq=-8b 1_(p adjacent q)-2sum_tau c_tau t_pq^tau
              -(d/2)c_pq,  p!=q.                             (P18)

The coefficient signs, ordered pair multiplicities and all cube cross entries are retained. The cube monomial is linear in each of its individual source variables, so its same-variable second derivative is zero; its two-distinct-source derivatives are the displayed off-diagonal contribution.

`generated/response_L2.json` contains all three matrices on the actual 240-face L=2 box. Its degree-four matrix has 9,660 nonzero entries. `generated/response_L3.json` contains the original 756-face L=3 answer. The complete sums of entries agree with -one-half the second homogeneous derivative of the original finite-volume energy; all boundary terms are included.

An initial implementation comparison used a bulk diagonal for an L=2 entry whose degree-four supports meet the boundary. That comparison was corrected: the full bulk anchor row is used only where all its supports are contained, and the finite L=2 matrix is retained without that replacement. The checker explicitly rejects that substitution. The opposite-face entry below has all of its required supports contained in L=2.

## P5. An actual positive response between opposite faces

Take the original faces

    p=(0,0,0;0,1),   q=(0,0,1;0,1).                           (P19)

They are the opposite horizontal faces of one cube. Their degree-zero and degree-two response entries are zero. There are exactly four connecting three-face paths and one cube. Formula P18 gives

    R_(4),pq=-8c_path-d/2
       =4909/14784120+83/3888
       =641033/29568240.                                     (P20)

This includes both the four path contributions and the complete cube contribution. In the actual L=2 vacuum put

    xi=1/10^13,
    g^2=500000 sqrt(10),
    kappa=1000000 sqrt(10)/a,
    r=1/1280.                                                (P21)

Insert these exact values in P16. Rational arithmetic gives the strict enclosure

    21677/10^6 < R_pq(xi)/xi^4 < 21682/10^6.                   (P22)

Thus the original connected zero-energy integrated correlation in P6 is strictly positive, with bounds obtained from P22 by multiplying by xi^4/kappa. No vacuum sampling or spin cutoff is used. The large coupling and the finite volume of this numerical certificate are explicit; its error radius is not assigned a volume-independent value.

## P6. Complete coefficientwise bulk symbol and its raw orientation frame

Each coefficient through degree four depends on a finite set of original nearby faces. Therefore its spatial coefficient limit is exact once those supports are contained in the box. This constructs a coefficientwise finite-range bulk kernel; it does not invoke convergence of the full interacting infinite-volume response.

Index orientations by a=0,1,2 with original plane axes (1,2),(0,2),(0,1). Their actual centers are c_a=(e_i+e_j)/2. For an original counting-norm coefficient function f_a(n), use the explicit Fourier map and inverse

    fhat_a(k)=sum_n exp[-i k.(n+c_a)] f_a(n),
    f_a(n)=(2pi)^(-3)int_[-pi,pi]^3 exp[i k.(n+c_a)] fhat_a(k) dk. (P23)

Orthogonality of the original exponentials proves both inverse laws on finitely supported coefficients and the Plancherel identity with the displayed measure. An entry connecting (n,a) to (n+d,b) has symbol phase exp[i k.(d+c_b-c_a)]. The archive stores all these rational coefficients and twice-center displacements in `generated/plaquette_response.json`; the full adjoint symmetry is checked by (a,b,d)->(b,a,-d).

At k=0 the three-by-three matrix preserves the scalar orientation direction (1,1,1) and the two-dimensional zero-sum space. Their coefficient polynomials are

    R_scalar(0,xi)=1/3-(11/156)xi^2
                    +(211396463/938298816)xi^4,
    R_zero_sum(0,xi)=1/3-(163/1404)xi^2
                    -(22137985/938298816)xi^4.                 (P24)

These are the coefficients through degree four; no omitted tail is set to zero. The actual coordinate frame

    (1,1,1), (1,-1,0), (1,1,-2)

has original Gram diag(3,2,6). Its inverse coordinate map sends x to

    ((x_1+x_2+x_3)/3, (x_1-x_2)/2, (x_1+x_2-2x_3)/6).          (P25)

Multiplication verifies both inverse laws and the Gram. In particular no change to the original orientation norm is used to obtain P24.

## P7. One-plaquette literature cross-check with its exact operator map

For one original plaquette, gauge reduction leaves its holonomy class angle theta in [0,pi], W=2cos(theta), and Haar class measure (2/pi)sin^2(theta)dtheta. The original kinetic operator is

    K=-(d^2/dtheta^2+2cot(theta)d/dtheta).

Set t=theta/2 and y(t)=sin(2t)F(2t). Its exact inverse is F(theta)=y(theta/2)/sin(theta) on the induced operator domain, and its norm return is

    (2/pi)int_0^pi sin^2(theta)|F(theta)|^2 dtheta
       =(4/pi)int_0^(pi/2)|y(t)|^2 dt.                         (P26)

The original equation (K-xi W)F=e F becomes

    y''+[4(e+1)+8xi cos(2t)]y=0.                              (P27)

The branch starting at y=sin(2t) is the Mathieu b_2 branch, with the exact maps q=-4xi and e=b_2(q)/4-1. The full one-plaquette physical energy retains kappa(2xi+e). NIST DLMF equation28.6.5 gives, under that map,

    e=-xi^2/3+5xi^4/216-289xi^6/77760
          +21391xi^8/27993600+... .                           (P28)

The independently executed character recurrence reproduces each of these coefficients. This literature check verifies the displayed one-plaquette convention and coefficient return. The spatial fifth catalogue and cross-face response have their own complete identities and certificates.

The exponential-vacuum and connected-loop setting is credited to the original Hamiltonian coupled-cluster work of Schuette, Zheng Weihong and Hamer, `hep-lat/9603026v1`. No historical-priority or best-known-bound claim is made.

## P8. Completed scope

The completed results are the entire original fifth coefficient, all of its degree-four plaquette-source derivatives, the full response matrices P17-P18, their coefficientwise bulk symbol, and the actual finite-volume analytic enclosure P22. The unit-vacuum scalar, the original energy pairing, all source labels, cube paths and boundary contributions remain attached.

The independent-session report expressly leaves the earlier uniform-gap analytical chain without independent recertification. Its limitation is preserved in the cumulative reading guide. The present P11-P16 calculation is a separate finite-volume proof with its explicit M-dependent radius. It neither upgrades those older claims by repetition nor establishes a nontrivial four-dimensional continuum Yang-Mills field or a finite positive continuum mass.
