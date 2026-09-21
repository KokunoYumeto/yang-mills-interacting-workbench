# Full-time heat bounds and the original plaquette response metrics

21 September 2026. This proof uses the unchanged finite-box SU(2) Hamiltonian
and the complete coefficients in PHYSICAL_HEAT_COEFFICIENTS.md. Its analytic
argument is finite-volume and independent of the inherited volume-uniform
source-norm estimates. The original number M of plaquettes appears in every
Cauchy radius. Written arguments and executed finite checks have separate
records. All inner products are conjugate-linear in the first entry.

## A1. Original free spectrum and Haar blocks

Use H1--H3 of the coefficient proof. The original physical free operator K has
its constant eigenvector 1, and every other physical Fourier block has energy
at least 3. Here is the graph argument. In a nonzero invariant representation
assignment, a vertex incident to only one active edge has no invariant tensor.
Thus the finite active graph has minimum degree at least two and contains a
cycle. The original simple cubic graph has no triangles and every cycle has at
least four edges. Each active edge has spin j>=1/2 and Casimir j(j+1)>=3/4.
Hence the complete physical K on the orthogonal complement of 1 is >=3.
The elementary plaquette trace has four spin-one-half edges and energy 3.

Write P0=|1><1| and Q0=I-P0 in the original product Haar space. Integrating
one original link gives P0 Wp=0. Two distinct elementary plaquettes have an
edge occurring in just one of their two words; integration over that link
vanishes. For p=q, the product holonomy has the original Haar law and the
fundamental character has squared norm one. Therefore

    <Wp,Wq>_H=delta_pq.                                      (A1)

For the complex homogeneous coefficient zeta, x_p=zeta, put B_zeta=K-zeta S.
This complex variable retains the physical return H= kappa B_xi+2kappa M xi I
at real xi. On C1 plus Q0 H_phys the full original block operator is

    B_zeta = [[0,Z],[W,D]],
    D=Q0(K-zeta S)Q0 on Dom(K) intersect Q0 H_phys,
    W=-zeta sum_p Wp,   Z=-zeta P0 S Q0.                     (A2)

Z is the original complex-linear row, with no conjugation of its parameter
in the analytic extension. Equation (A1) proves exactly

    ||W||=||Z||=sqrt(M)|zeta|.

On |zeta|<=1/M, Re<Dh,h> >= ||h||^2 since ||zeta S||<=2.
The closed operator D is a bounded perturbation of Q0KQ0 on the same domain.
For Re e<1 its inverse D-e exists with norm <=(1-Re e)^(-1): injectivity and
closed range follow from the real part inequality; the same inequality for
its adjoint gives dense range, hence surjectivity. All finite boxes here have
M=3(2L)^2(2L+1)>=240.

## A2. A complete ground/complement decomposition on the complex disk

The scalar equation for the small eigenvalue is

    f(e)=e+Z(D-e)^(-1)W=0.                                  (A3)

On |e|=2/M the second term has modulus at most 1/(M-2)<2/M. The finite scalar
argument principle, or Rouche's theorem applied to e, gives one simple zero
inside that circle, with multiplicity counted. The contour construction
makes e(zeta) analytic on a neighborhood of the closed |zeta|<=1/M disk and
|e|<=2/M. Define the actual right and left graph coordinates

    w=-(D-e)^(-1)W,
    ell=-Z(D-e)^(-1),
    P=(1,w)(1,ell)/(1+ell w).                               (A4)

They satisfy B(1,w)=e(1,w), (1,ell)B=e(1,ell), ell W=e, and
Z+ell D=e ell. Their norms obey

    ||w||,||ell|| <= sqrt(M)/(M-2),
    M/(M-2)^2 <= 240/238^2 < 1/225.

The last bound decreases with M>=240 by differentiating M/(M-2)^2.
Consequently 1+ell w is nonzero, P^2=P, and

    ||P||_trace <= (1+1/225)/(1-1/225)=113/112.               (A5)

The original complement is ker(1,ell). Its exact coordinate map and inverse are

    J:Q0H -> ker(1,ell),   Jh=(-ell h,h),
    J^(-1)=Q0 restricted to ker(1,ell).                     (A6)

On the unchanged operator domain direct multiplication gives

    (B-e)J=J Bc,   Bc=D-e-Well.                             (A7)

Every factor in the feedback Well is retained. For its real part,

    Re<Bc h,h> >= [1-2/M-1/(M-2)]||h||^2
                 >=[1-1/120-1/238]||h||^2
                 > (49/50)||h||^2.                         (A8)

Bc is again the same self-adjoint free operator plus a bounded perturbation.
The norm-convergent Duhamel series constructs its strongly continuous semigroup;
its derivative on Dom(K), followed by the real-part energy inequality (A8),
proves ||exp(-tau Bc)||<=exp(-49tau/50). Density extends this estimate to all
vectors. Holomorphy in zeta follows locally from the uniformly convergent bounded
perturbation series and the analytic coefficients in (A4).

The exact excited semigroup is therefore

    exp[-tau(B-e)](I-P)=J exp(-tau Bc)Q0(I-P).               (A9)

The bounds on the original graph maps are

    ||J||<=226/225,
    ||Q0P||<=113/1680,
    ||Q0(I-P)||<=1793/1680.                                 (A10)

For example Q0P=w(1,ell)/(1+ell w), and using ||w||<=1/15 and
sqrt(1+1/225)<=226/225 gives 113/1680. No product-space Gram is replaced.

For real xi, B_xi is the full self-adjoint physical operator less its displayed
scalar. Its lowest eigenvalue is <=0 by the original constant trial state.
Equation (A8) leaves the entire remaining spectrum positive after subtracting
e. Thus e is its actual ground eigenvalue. P is its actual orthogonal ground
projection, obtained above on the same domain. This also identifies the analytic
branch without choosing a surrogate vacuum.

## A3. The complete all-time analytic bound

Define the analytic connected heat observable by the literal trace

    Chat_pq(tau;zeta)
      =Tr[P Wp exp[-tau(B-e)](I-P)Wq].                       (A11)

At real xi this equals the original C_pq(tau/kappa;xi), with its actual
vacuum-mean subtraction. The complex trace is its holomorphic continuation;
no conjugation of zeta is inserted. Each original multiplication Wp has norm
at most 2. Equations (A5), (A9), (A10) give

    |Chat_pq(tau;zeta)|
      <=4(113/112)(226/225)(1793/1680)exp(-49tau/50)
      <5 exp(-49tau/50),    |zeta|<=1/M, tau>=0.             (A12)

The original link-center substitution U_(n,i) ->
(-1)^(sum_(j<i)n_j) U_(n,i) sends every plaquette trace to -Wp, preserves Haar,
K and all gauge spaces, and is its own inverse. It carries B_zeta to B_-zeta.
Both marked traces change sign, so (A11) is even in zeta. Cauchy's coefficient
formula on the original circle |zeta|=1/M and summation of the full even tail
now prove

    |Chat_pq(tau;xi)-C0_pq(tau)-xi^2 C2_pq(tau)-xi^4 C4_pq(tau)|
      <=5 exp(-49tau/50)(M|xi|)^6/[1-(M|xi|)^2],
                    |xi|<1/M, tau>=0.                     (A13)

All constants and all higher orders remain. The bound is uniform in positive
time, with its original volume dependence. It also justifies differentiation
in the source before Laplace integration. The finite rational functions in the
coefficient proof are therefore precisely the Taylor coefficients of (A11).
The Laplace uniqueness argument H3 returns their actual time functions.

## A4. A positive original opposite-face correlation on an entire time interval

For the two faces H17, C0=C2=0 and C4=h4=4P+B with H18--H20. Exact rational
Taylor remainder estimates enclose exp(-x) for each x in [0,50]: the even
Taylor sum of degree 240 is an upper bound, and subtracting x^241/241! is a
lower bound. Taylor's Lagrange remainder has the required negative sign and
magnitude <=x^241/241!. The code checks positive lower endpoints. This is
an interval calculation with rational endpoints, including at all cited times.

At L=2, M=240, xi=10^(-10), tau=1, evaluation of H18--H20 and (A13) gives

    85879/10^7 < Chat_pq(1;xi)/xi^4 < 85951/10^7.             (A14)

The complete rational inner endpoints are in generated/heat_bounds.json.
The physical parameters are g^2=50000, kappa=100000/a, and t=1/kappa.

The positivity on 1<=tau<=3 has a continuous proof. In the first bracket of
H18, let a=1/882, b=-4441/3611790, c=75173779/67612708800. Its quadratic
minimum is c-b^2/(4a). Exact rational comparison gives

    c-b^2/(4a) > (121/108864)/4+(197/9988160)/16.              (A15)

Since exp(-3/2)<1/4 and exp(-7/2)<1/16, the two negative exponentials in H18
are bounded by this quantity times exp(-3tau) for tau>=1. Its other terms are
positive. Thus P(tau)>0 throughout tau>=1. In H19 the first bracket is at
least 5/648 at tau=1 and increases, and both other terms are positive. Hence

    h4(tau) >= (5/648)exp(-3tau),    tau>=1.                 (A16)

For tau in [1,3], the ratio of the complete error (A13) to xi^4 times (A16)
is at most

    648 M^6 xi^2 exp(303/50)/[1-(Mxi)^2] < 0.531 < 1         (A17)

at the actual M and xi above. Consequently the full interacting-vacuum
correlation, not just its leading coefficient, is strictly positive on
1/kappa<=t<=3/kappa. Its original integrated value has all physical factors
retained by H4.

## A5. Full inverse-power metrics, including the original state norm

Let R:C^M->H_phys,0 have the original centered columns r_p. For integer k>=1,

    G^(k)=kappa^k R* A^(-k) R
         =int_0^infinity tau^(k-1) Chat(tau)d tau/(k-1)!.     (A18)

The actual finite-regulator spectral theorem and the positive centered gap
established in A2 justify the integral. Equation (A12) gives a uniform
integrable majorant for the analytic Taylor coefficients and their remainder.
For a partial fraction a/(z+c)^n, its exact contribution is

    a (k+n-2)!/[(k-1)!(n-1)! c^(k+n-1)].                    (A19)

Every original pole and multiplicity is used. Integrating (A13) proves the
entrywise bound

    |G^(k)_pq - sum_(j=0)^2 xi^(2j) G^(k)_(2j),pq|
      <=5(50/49)^k (M|xi|)^6/[1-(M|xi|)^2].                 (A20)

The physical energy response is G^(1). For the actual derivative primitive

    Phi=kappa A^(-1)R,
    A Phi=kappa R,    Phi*Phi=G^(2),
    Phi*A Phi=kappa G^(1),                                 (A21)

the original state and energy metrics remain separately specified.

All coefficients for k=1,2 on the original 240-face L=2 box are calculated
entry by entry in generated/native_inverse_metrics_L2.json. Let L_(k,j) be the
maximum absolute row sum of the exact degree-2j coefficient matrix. A real
symmetric M by M error whose entries have magnitude at most e has operator
norm at most M e: apply the row and column bounds and Cauchy--Schwarz. Therefore
(A20), with the complete off-diagonal rows, gives

    [3^(-k)-w_k]I <= G^(k) <= [3^(-k)+w_k]I,
    w_k=xi^2 L_(k,1)+xi^4 L_(k,2)
          +5M(50/49)^k(Mxi)^6/[1-(Mxi)^2].                  (A22)

For 0<xi<=1/1600, all the scalar terms on the right increase with xi, so its
endpoint evaluation bounds the whole interval. Exact rational evaluation gives

    (3/10)I_240 < G^(1) < (11/30)I_240,
    (9/100)I_240 < G^(2) < (13/100)I_240.                    (A23)

This is the original L=2 box, every a>0, and every g^2>=20. The identities use
the original coefficient pairing on C^240; the actual state Gram is the
calculated G^(2), not the identity. The complete original energy form on these
primitive columns is kappa G^(1). The tighter rational endpoints and each
original row-sum certificate are retained in generated/heat_bounds.json.

## A6. Scope and comparison with the preceding analysis

The finite-volume Cauchy circle in (A13) has radius 1/M. Equation (A23) has been
evaluated on the original L=2 family, with all 240 columns. Every dependence on
M, a, g and time is displayed. These statements establish neither a nontrivial
four-dimensional continuum field nor a uniform-in-volume positive mass bound.
They do not independently recertify the earlier uniform-source/gap argument.

The method uses classical bounded perturbation, block resolvents, the scalar
argument principle and the original spectral theorem. A relevant primary
Feshbach--Schur antecedent is Dusson--Sigal--Stamm, arXiv:2105.02058. The present
proof gives all blocks, graph inverses and finite constants on the actual
Hamiltonian instead of supplying a desired spectral gap as an input. The new
Split-Zero heat transfer to the resulting actual Grams is in RH_HEAT_TRANSFER.md.

## A7. The original forcing Gram for the same observation family

The time-zero matrix is the original forcing Gram G^(0)=R*R=Chat(0). It is
computed from exactly the same complete pole coefficients by

    G^(0)_(2j),pq=sum_(c>0) a_(c,1),                        (A24)

because higher pole orders vanish at tau=0. Equation (A13) at zero supplies its
complete entry error 5(Mxi)^6/[1-(Mxi)^2]. The identical full row-sum argument
on the actual L=2 box and 0<xi<=1/1600 proves

    (49/50)I_240 < G^(0) < (51/50)I_240.                    (A25)

No division by a chosen source norm is involved. The tighter rational
interval is retained with G^(1),G^(2) in generated/heat_bounds.json. Thus all
three original Grams R*R, Phi*A Phi/kappa and Phi*Phi are quantitatively
controlled together. Their use in the actual inverse-power observation is
proved in T7 of the source-transfer note.

## A8. The full original kinetic Gram, retaining its local zero entries

The forcing columns have original energy Gram R*A R=kappa Kobs, where

    Kobs_pq=<Gamma(Wp,Wq)>_rho=-Chat'_pq(0).                 (A26)

The ground-state form identity proves the first equality; differentiation of
the original semigroup proves the second. In the coefficient file each simple
pole contributes its energy times its coefficient and each double pole
contributes minus its coefficient. Higher poles contribute zero. This gives
all entries through degree four in native_inverse_metrics_L2.json.

Every off-diagonal entry outside the original face adjacency is zero exactly:
Gamma differentiates a common original edge. On a diagonal,
Gamma(Wp,Wp)=4-Wp^2 has absolute value at most4. On adjacent distinct faces,
their single shared-edge derivative vectors each have Euclidean length at most
one; writing the original SU(2) product as q0I-iq.sigma gives the length
sqrt(1-q0^2). Their scalar product has absolute value at most1. Each face has
at most12 original neighbours. All assertions concern the unchanged original
link derivatives, with their generator factor1/2 retained.

The complex ground projection from (A4)--(A5) therefore bounds the diagonal
expectation by4*113/112 and each adjacent expectation by113/112. Original
center symmetry makes these analytic expectations even. Cauchy's formula on
|zeta|=1/M bounds the entire row of the omitted tail by

    (113/112)*16*(M|xi|)^6/[1-(M|xi|)^2].                   (A27)

This uses the exact local support, rather than a dense-M multiplier on this
particular Gram. The exact degree-two and degree-four row sums and (A27) give,
on the original L=2 box with g^2>=20,

    (29/10)I_240 < Kobs < (31/10)I_240.                     (A28)

The sharper rational endpoints and every nonzero coefficient are retained in
the same records. This is the further original energy input used in T8 to
bound the correction between the actual state-minimum and energy-minimum
sections of the inverse-power family.
