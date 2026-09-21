# The complete plaquette band, its interaction matrix, and a certified first eigenvalue

15 September 2026. All notation is from RESEARCH_NOTE.md G1–31. Energies below retain kappa=2g^2/a. Fourier norms are auxiliary estimates on the original coefficients; the raw physical band Gram is written explicitly in B6. No spin truncation of the Hamiltonian is used.

## B1. Spectral exclusion and an isolated physical band

Let epsilon=(1-sqrt(1-256xi/3))/2 on 0<=xi<=3/256. The estimate G23 yields, on the physical Haar-mean-zero Fourier source,

\[
 \| (\kappa K_L-z)^{-1} V_\xi \|_{Y_0\to Y_0}
 \le\epsilon\sup_{c\in\operatorname{spec}(K_L|_{\rm phys})\setminus\{0\}}
            \frac{\kappa c}{|\kappa c-z|},
 \quad V_\xi=-2\kappa Q_H\sum_i(X_iv(\xi))X_i.            \tag{B1}
\]

All positive physical eigenvalues consequently belong to the union of the intervals

\[
 [\kappa c(1-\epsilon),\kappa c(1+\epsilon)],
 \qquad c\in\operatorname{spec}(K_L|_{\rm phys})\setminus\{0\}. \tag{B2}
\]

For a real point outside the union, the right side of B1 is strictly smaller than one; at large c the quotient tends to one. The same eigenfunction contradiction as G26 proves B2, including the endpoints by closure.

For 0<=xi<3/400, epsilon<1/5. The c=3 interval is separated from all c>=9/2 intervals. The fixed contour

\[
 \mathcal C:\quad |z-3\kappa|=3\kappa/5                 \tag{B3}
\]

has sup kappa c/|kappa c-z|<=5, attained in its free bound at c=3 or c=9/2. It therefore lies in the resolvent set throughout this interval. The entire first physical excitation band is inside this contour and contains exactly |P_L| eigenvalues, including multiplicities. In particular the spectral gap is the lowest eigenvalue in this band. The coupling range is g^2>10/sqrt(3); the endpoint xi=0 is an auxiliary spectral parameter used to fix the rank.

Here is a precise operator justification including that endpoint. On X_0, K_L with domain Y_0 is closed and has compact inverse, since 1/c tends to zero and only finitely many product-spin labels have bounded c. G23 makes V_xi a relatively bounded perturbation with relative bound epsilon<1. The resolvent of kappa K_L+V_xi on the physical mean-zero space is supplied on B3 by the convergent operator Neumann series; its compactness follows from the compact free inverse. Its eigenvectors and generalized eigenvectors are C^2 by the Fourier domain, then smooth by elliptic bootstrapping. The exact G24 map identifies them with the original centered physical operator for real xi. The latter is self-adjoint, so no generalized eigenspace enlargement is introduced by this Banach realization. Conversely all original physical eigenfunctions belong to Y_0 by G23's regularity argument.

The coefficients of v(zeta) are holomorphic for |zeta|<3/256, with the same absolute majorant at |zeta|. Thus the resolvent on B3 and its Riesz projection vary analytically wherever 5epsilon(|zeta|)<1. At zero the projection is the original Haar projection P onto span{W_p}; its rank is |P_L| by G8. Contour-resolvent continuity fixes that finite rank on the stated real interval. This proves the asserted band for the actual Hamiltonian, without requiring a finite spectral cutoff.

## B2. The exact coefficient map and a uniform analytic remainder

Work first on the closed complex disk |zeta|<=rho_*=1/320. Put eta=epsilon(|zeta|). The exact scalar inequality sqrt(11/15)>107/125 gives

\[
 \eta<9/125,\qquad 5\eta<9/25.                           \tag{B4}
\]

Let P_zeta be the Riesz projection from B3, E_zeta=P P_zeta P on the original plaquette space, and

\[
 U_\zeta=P_\zeta P E_\zeta^{-1},\qquad
 A_{\rm band}(\zeta)=P(\kappa K_L+V_\zeta)U_\zeta.        \tag{B5}
\]

No arbitrary frame is chosen: P U_zeta=I, and the original plaquette coefficient vector is the retained coordinate. On this frame the X_0 norm is 8 sum_p|x_p| and the Y_0 norm is 24 sum_p|x_p|, by G14 and orthogonality of the distinct product-spin blocks. Thus induced matrix 1-norms have no omitted frame factor.

To prove E_zeta invertible and compute the remainder constant, expand the contour resolvent using the complete V_zeta. Its zeroth contribution to E_zeta is I. Its one-insertion contribution is the integral of P V_zeta P/(z-3kappa)^2 and is exactly zero. Every term with at least two insertions is bounded on X_0 by its geometric bound. Hence

\[
 \|E_\zeta-I\|_1\le\frac{(5\eta)^2}{1-5\eta},\qquad
 \|E_\zeta^{-1}\|_1\le
       \frac{1-5\eta}{1-5\eta-25\eta^2}.                 \tag{B6}
\]

The denominator is positive by B4. Also

\[
 \|(I-P)P_\zeta P\|_{X_0\to Y_0}
          \le\frac{15\eta}{1-5\eta}.                   \tag{B7}
\]

Indeed its free term is zero. Integrate R_0 V_zeta R_zeta P around the contour: the radius is 3kappa/5, the Q-free resolvent norm into Y_0 is at most 5/kappa, V has norm kappa eta, and the full resolvent on P has norm at most 5/[kappa(1-5eta)] into Y_0. These four factors give B7.

Write b=64/3. The source recurrence implies that V_zeta's first Taylor coefficient has norm at most kappa b, and its higher-coefficient tail at |zeta| has norm at most kappa(eta-b|zeta|), from Y_0 into X_0. Section B3 below proves P V_[1] P=0. Since P U_zeta=I, equations B5–7 give

\[
 \|A_{\rm band}(\zeta)-3\kappa I\|_1
 \le\kappa\left[3(\eta-b|\zeta|)
            +\frac{15\eta^2}{1-5\eta-25\eta^2}\right].  \tag{B8}
\]

For Cauchy's coefficient estimate evaluate B8 on the boundary |zeta|=1/320. There b|zeta|=1/15 and eta<9/125, so

\[
 \|A_{\rm band}(\zeta)-3\kappa I\|_1
 \le\kappa B_*,\quad
 B_*:=3(9/125-1/15)+
       \frac{15(9/125)^2}{1-5(9/125)-25(9/125)^2}
       =\frac{6713}{39875}.                             \tag{B9}
\]

All denominators and signs in this bound are retained. Matrix-valued Cauchy integration now gives the exact expansion

\[
 A_{\rm band}(\xi)=3\kappa I+\kappa\xi^2T_L+\mathcal R_L(\xi),
 \quad
 \boxed{\|\mathcal R_L(\xi)\|_1
       \le\kappa B_*\frac{(320|\xi|)^3}{1-320|\xi|}}
 \quad (|\xi|<1/320).                                   \tag{B10}
\]

This is uniform in the original box size. The first coefficient is exactly zero, and T_L is calculated next. The estimate sums every higher order; it is not a finite-spin replacement or an assumed remainder. The underlying square-root source radius remains 3/256; 1/320 is the explicitly chosen interior contour radius for this numerical bound.

## B3. The full second coefficient with the extensive cancellation retained

Let S=sum_p W_p and M=|P_L|. The unchanged scalar vacuum-energy expansion is

\[
 E_{0,L}(\xi)=2\kappa M\xi-\kappa M\xi^2/3+O_L(\xi^3).
                                                               \tag{B11}
\]

It follows directly from G20–21: v_[1]=S/3, int_H W_pW_q=delta_pq and K_L W_p=3W_p imply int_H sum|Xv_[1]|^2=M/3. The O_L notation in this identity describes its fixed finite box Taylor tail; the band tail itself is the explicit volume-uniform B10.

The first band coefficient vanishes. For all p,q,r, int_H W_p W_q W_r=0. If exactly two indices coincide, an unmatched link of the third face makes the integral zero. If all three coincide, the third fundamental character moment is zero. If three distinct faces occurred without an unmatched edge, each edge of one face would need a different neighboring face; only two others are present. This is impossible because distinct elementary plaquettes share at most one edge. Thus P S P=0. Integration by parts with the three original plaquette Casimirs also proves P V_[1]P=0 in the ground-transformed coefficient system.

On the full original Haar physical space, let Q_3=I-P, so Q_3 includes the constant. Matching the second Taylor coefficient in the original Schrödinger equation gives

\[
 \boxed{T_L=\frac M3 I-P S Q_3
              (K_L-3)^{-1}Q_3 S P.}                    \tag{B12}
\]

The inverse is on Q_3, where its original eigenvalues include -1/3 on the constant and positive inverses for c>=9/2. The term M/3 in B12 is precisely B11's vacuum-energy contribution.

To verify that B12 is also the B5 coefficient, the literal multiplier e^{v(zeta)} intertwines the original Schrödinger operator H_L(zeta)-E_*(zeta) and its ground-transformed operator. Its first multiplier coefficient is v_[1]=S/3, and P v_[1] P=0 by the just-proved triple integral. The additional scalar in G24 lands in the constant block. Thus the P coefficient of this intertwining map is I+O(zeta^2). Conjugating a band matrix whose zeroth coefficient is 3kappa I and whose first coefficient is zero by I+O(zeta^2) changes no second coefficient. Alternatively, its order-one equation is (K_L-3)phi_1=Q_3 Sx for x in P, and projecting its order-two equation gives B12 directly. This proves the complete map and its coefficient-level return rather than assigning the two source formulas the same name.

## B4. Evaluate every intermediate channel

The identities F_p^2=1+chi_1(Omega_p) give two original intermediate components: the constant of Haar norm one and energy zero, and the spin-one plaquette character of Haar norm one and Casimir 8. Distinct spin-one plaquette components are orthogonal.

For p!=q with no shared edge, F_pF_q is an original Casimir eigenfunction of value 6 and Haar norm one, regardless of a shared vertex.

For p,q sharing one edge, retain its original link U. Cyclic trace and inversion of a whole SU(2) trace put the two original words into the form Tr(UA), Tr(U^-1 B), where A and B are their respective ordered three-link path products. Both transformations are literal word identities. The Haar map U,A,B retains independent product Haar, by integrating the original remaining path links successively. Therefore the spin-zero projection at U is

\[
 P_{U,0}(F_pF_q)=\tfrac12\operatorname{Tr}(AB),\qquad
 \|P_{U,0}(F_pF_q)\|_H^2=1/4.                           \tag{B13}
\]

The product has total norm one. The complementary spin-one component at the shared edge consequently has norm squared 3/4, and the two components are orthogonal. The six other original spin-1/2 edges contribute 9/2 to K_L; the shared spin-one edge adds 2. Their exact energies are thus 9/2 and 13/2. Their total resolvent weight at the original band energy 3 is

\[
 \frac{1/4}{9/2-3}+\frac{3/4}{13/2-3}
       =\frac16+\frac3{14}=\frac8{21}.                  \tag{B14}
\]

No pair channel has been omitted. To prove orthogonality for distinct unordered pairs, use independent central sign changes of the original links. The half-integer spin support of F_pF_q is the mod-two symmetric difference of the two face boundaries. Equality for two different unordered pairs would yield a nonzero mod-two sum of at most four elementary faces with zero boundary. Each of the four edges of any included face would require a different other face, giving at least five faces. Hence equality is impossible. Orthogonality follows from the actual sign-changing Haar substitution. The self-pair channels have even center parity and are separated from these distinct-pair channels; their nonconstant parts were already separated by their spin support.

Write p~q for shared-edge adjacency and d_p=#{q:q~p}. Substituting all channels into B12 gives

\[
 \boxed{(T_L)_{pp}=\frac7{15}-\frac{d_p}{21},\qquad
 (T_L)_{pq}=\begin{cases}-1/21,&p\sim q,\\0,&p\not\sim q,\ p\ne q.
 \end{cases}}                                          \tag{B15}
\]

For clarity, the unreduced diagonal calculation is

\[
 \frac M3+\frac13-\frac15
   -\frac{M-1-d_p}{3}-\frac{8d_p}{21}.
\]

For a nonadjacent off-diagonal pair its terms are +1/3 from the constant and -1/3 from the actual two-plaquette intermediate. For an adjacent pair they are +1/3 and -8/21. These equalities retain each canceled extensive or off-diagonal contribution as its original intermediate channel.

Let A_adj be this adjacency matrix and D_deg=diag(d_p). The exact operator statement is

\[
 T_L=\frac7{15}I-\frac1{21}(D_{\rm deg}+A_{\rm adj}).     \tag{B16}
\]

All open-boundary degrees remain; replacing d_p by twelve changes the actual finite matrix.

## B5. Boundary-sensitive bounds, the full physical lower edge, and one original-box certificate

Each elementary plaquette has d_p<=12. The complete column sum of the absolute entries in T_L is at most 71/105. Indeed at degree d the sum is |7/15-d/21|+d/21; for d<=9 it equals 7/15 and for 10<=d<=12 its largest value is 71/105. Gershgorin's bound for B10, with its whole column residual, consequently proves

\[
 \boxed{\Delta_L\ge\kappa\left[
       3-\frac{71}{105}\xi^2
         -B_*\frac{(320\xi)^3}{1-320\xi}\right],
       \quad 0<\xi<1/320.}                              \tag{B17}
\]

The gap belongs to the band by B1. This lower bound uses the entire actual physical spectrum, not the Rayleigh quotient of one observed vector. G26 remains simultaneously available. At xi=10^-8, integer/rational evaluation gives

\[
 \boxed{\Delta_L>\kappa(3-7.314\,10^{-17})
          \quad\hbox{for every }L\ge2.}                 \tag{B18}
\]

No matrix minimum is formed between the two different lower-bound arguments.

The degree count is exact. Put m=2L. There are M=3m^2(m+1) faces, and the edge incidence values 4,3,2 occur respectively 3m(m-1)^2, 12m(m-1), 12m times. Since a pair of distinct faces shares at most one edge,

\[
 \sum_p d_p=12m(3m^2-1),\qquad
 \overline d=\frac{4(3m^2-1)}{m(m+1)}.                   \tag{B19}
\]

The original constant coefficient vector on all M plaquettes has squared Haar norm M. In B16 it therefore gives

\[
 -\frac{71}{105}\le\lambda_{\min}(T_L)
 \le\frac7{15}-\frac{2\overline d}{21}
 =-\frac{71}{105}+\frac{8(3m+1)}{21m(m+1)}.              \tag{B20}
\]

This evaluates the large-box limit of the actual second coefficient with an explicit boundary remainder. It does not interchange that coefficient limit with a varying-coupling spectral limit.

The checker additionally computes the full original L=2 matrix, containing 240 plaquettes. Let Q_L=D_deg+A_adj. Starting with the original vector x_0=(1,...,1), it computes x_100=Q_L^100 x_0 by integer multiplication. All entries are positive. The minimum and maximum of (Q_L x_100)_p/(x_100)_p enclose its largest eigenvalue: the upper bound is the row-sum bound after diagonal conjugation by diag(x_100); the lower bound follows either by the positive Perron vector or by the Rayleigh quotient. Q_L is symmetric nonnegative and its graph is connected. Direct exact computation returns

\[
 21.86319640514<\lambda_{\max}(Q_L)<21.86319641826,
\]
\[
 -0.57443792469<\lambda_{\min}(T_L)<-0.57443792405.        \tag{B21}
\]

A separate fraction-free symmetric congruence of Q_L-21I has inertia (1 positive,239 negative,0 zero). Every integer division and all 240 pivot determinants are retained in BOX_L2_CERTIFICATE.json. At stage k the exact symmetric Schur step is

\[
 a_{ij}^{\rm new}=(a_{kk}a_{ij}-a_{ik}a_{jk})/d_{k-1},
\]

with d_-1=1 and d_k the current pivot; the actual pivot of the ordinary Schur complement is d_k/d_(k-1). Congruence by unit triangular elimination proves that their signs give the stated inertia. No numerical eigenvalue routine is used for this certificate. It proves that every other eigenvalue of T_L is greater than -8/15.

On 240 by 240 matrices, ||R||_2<=sqrt(240)||R||_1<16||R||_1. At the actual coupling xi=10^-10, B10 therefore bounds the perturbation in (A_band-3kappa)/(kappa xi^2) by

\[
 \delta_*:=16B_*\frac{320^3\xi}{1-320\xi}<0.008827.       \tag{B22}
\]

Use the fixed contour of radius 1/50 around -574438/10^6. B21 and the just-certified other-eigenvalue bound put this contour at distance greater than delta_* from the spectrum of the Hermitian T_L. Resolvent Neumann expansion along the finite interpolation T_L+t(A_band-3kappa-kappa xi^2T_L)/(kappa xi^2) preserves its rank-one spectral projection. The actual band eigenvalues are real by Section B6 below. Normal-resolvent distance bounds place the single eigenvalue in the B21 interval enlarged by delta_*, while every other band eigenvalue is above -8/15-delta_*. The single eigenvalue is thus the original spectral gap. The final outward rational bounds are

\[
 \boxed{
 \kappa(3-0.5833\xi^2)<\Delta_{L=2}<\kappa(3-0.5656\xi^2),
 \quad \xi=10^{-10},\quad g^2=50000,\quad\kappa=100000/a.
 }                                                        \tag{B23}
\]

This certificate concerns the full interacting Hamiltonian in the original L=2 box, for every a>0. Its analytic remainder contains every Fourier spin and every higher perturbative order. The auxiliary 240 by 240 matrix is the exact second Taylor coefficient, not a truncation declared to equal the Hamiltonian.

## B6. The original band metric and its intertwining map

For real xi in B5's domain, let y=U_xi x in the original Haar coefficient source, and define

\[
 \mathcal R_\xi x
   =\psi_L\left[y-\langle y\rangle_{\rho_L}\right],\quad
 G_\xi=\mathcal R_\xi^*\mathcal R_\xi.                    \tag{B24}
\]

The map is injective because P U_xi=I and the only removed functions are constants. It is onto the complete first physical band: the Riesz range and G24 give the inverse by taking its original Haar plaquette coefficients after dividing by psi_L. Thus G_xi is the actual positive Gram in these prescribed coefficient coordinates. At zero its value is I because int_H W_pW_q=delta_pq, a calculated source identity.

The exact operator and energy identities are

\[
 (H_L-E_{0,L})\mathcal R_\xi=\mathcal R_\xi A_{\rm band}(\xi),
 \quad E_\xi=\mathcal R_\xi^*(H_L-E_{0,L})\mathcal R_\xi
             =G_\xi A_{\rm band}(\xi)
             =A_{\rm band}(\xi)^*G_\xi.                 \tag{B25}
\]

The inverse on the Riesz image and all physical pairings are retained. This proves the claimed reality of the actual band spectrum and exhibits the self-adjoint Hamiltonian comparison without replacing G_xi by an identity matrix.

## B7. Complete second-order spatial propagation in the original lattice coordinates

On the infinite cubic plaquette graph, index a plaquette by its normal axis a in {1,2,3} and base n in Z^3. Its center is n+c_a, with c_a=(e_b+e_c)/2 for the other axes b,c. The Fourier map and inverse are

\[
 (\mathcal F x)_a(k)=\sum_nx_{a,n}e^{-ik\cdot(n+c_a)},\quad
 x_{a,n}=\frac1{(2\pi)^3}\int_{[-\pi,\pi]^3}
            e^{ik\cdot(n+c_a)}(\mathcal Fx)_a(k)\,dk.     \tag{B26}
\]

Orthogonality of the original exponentials proves the isometry with the displayed measure. The components retain their boundary phase under k_i->k_i+2pi: e^(-2pi i(c_a)_i). This records the half-link center coordinates rather than discarding them.

Counting the actual shared links gives Q(k)=12I+A(k), with

\[
 A_{aa}(k)=2\cos k_b+2\cos k_c,\qquad
 A_{ab}(k)=4\cos(k_a/2)\cos(k_b/2)\quad(a\ne b),
 \quad T(k)=\frac7{15}I-\frac1{21}Q(k).                 \tag{B27}
\]

For the four perpendicular neighbors of a,b their relative center displacements are (+/-e_a+/-e_b)/2; summing their four exponential factors proves the off-diagonal formula. The four coplanar displacements are +/-e_b,+/-e_c, proving the diagonal formula. These are the actual adjacency maps of B16, now at every retained spatial momentum.

At k=0 the raw vector (1,1,1), of squared norm 3, has T-eigenvalue -71/105. Its coefficient-orthogonal plane x_1+x_2+x_3=0 has eigenvalue -11/105. On the fundamental cube all cos(k_a/2)>=0 and every row sum of Q(k) is at most 24; the maximum 24 is attained at k=0. Hence the bottom of the complete second-coefficient spatial operator is exactly -71/105.

The simple lowest branch has the Taylor expansion

\[
 t_{\rm low}(k)=-\frac{71}{105}+\frac4{63}|k|^2+O(|k|^4). \tag{B28}
\]

For a direct calculation, the diagonal quadratic change of A is -(k_b^2+k_c^2), and its a,b off-diagonal change is -(k_a^2+k_b^2)/2. Their full sum divided by the raw squared norm 3 is -(4/3)|k|^2. The other two eigenvalues are separated at zero, all matrix first derivatives there vanish, and the finite eigenvalue equation consequently gives B28; the eigenvector correction first contributes at fourth order. All original spatial directions remain.

With physical momentum p and k=ap, the corresponding exact Taylor coefficients of the energy band are

\[
 3\kappa-\frac{71}{105}\kappa\xi^2
       =\frac{6g^2}{a}-\frac{71}{840g^6a},\qquad
 \frac4{63}\kappa\xi^2a^2|p|^2=\frac{a}{126g^6}|p|^2.  \tag{B29}
\]

These are coefficients of the original strong-coupling band. B10 controls its full finite-box analytic remainder; B20 controls the large-box second coefficient. Neither a relativistic dispersion relation nor an exchange of the small-xi, volume and a->0 limits is asserted.

## B8. A primary-source coefficient check with the physical dictionary retained

A separate final source check located the planar coefficient in Bernd Dahmen,
*Strong coupling expansion for scattering phases in hamiltonian lattice field
theories. II. SU(2) gauge theory in (2+1) dimensions*, DESY 94-236,
arXiv:hep-lat/9412080, equations (1.7)–(1.11), Figure 1.3 and (1.26)–(1.29).
The original PDF pages 3, 4, 9 and 10 were inspected, including the graph signs.
This is a local-coefficient comparison; no three-dimensional remainder bound
is imported from that paper.

On the same planar graph, write its hopping coefficient as h_D, its coupling
as g_D, and its unscaled Hamiltonian as H_D'. The exact physical dictionary is

\[
 h_D=\xi,\qquad g_D=2^{3/4}g,\qquad
 H_{\rm plane}(a,g)=\frac{\sqrt2}{a}H_D'(g_D)
                        +2\kappa\xi M I.               \tag{B30}
\]

Indeed h_D=2/g_D^4=1/(4g^4), while
(sqrt(2)/a)(g_D^2/2)=2g^2/a=kappa. The Casimir identity
(n^2-1)/4=j(j+1) uses n=2j+1, and the original plaquette word is
identical under the original link labels. Thus B30 is equality of the
operators on the common planar-link domain, retaining its energy multiplier
and additive scalar. Ground-energy differences retain the multiplier.
The comparison at a periodic planar graph uses that graph on both sides;
it assigns no periodic boundary to the original open three-dimensional box.

On the planar plaquette graph the bulk degree is four. Repeating B12–16
with those actual incidences gives

\[
 T_{\rm plane}=\frac{29}{105}I-\frac1{21}A_{\mathbb Z^2},
 \qquad
 t_{\rm plane}(k)=\frac3{35}
                   +\frac{4-2\cos k_1-2\cos k_2}{21}.  \tag{B31}
\]

These are precisely the source's second coefficient and momentum coefficient
under B30. The common self and neighboring contributions have the original
values 2/15 and -8/21 in its Figure 1.3, as calculated in B12–14.

For the relation to the three-dimensional coefficient, let J_plane insert the
coefficients of one fixed plane and orientation into the full infinite
plaquette array, with zero on all other faces. Its adjoint reads precisely
those coordinates, so J_plane* J_plane=I. Each such face has its four planar
neighbors and eight perpendicular neighbors. Consequently

\[
 J_{\rm plane}^*T_{\mathbb Z^3}J_{\rm plane}
           =T_{\rm plane}-\frac8{21}I,
 \quad
 ((I-J_{\rm plane}J_{\rm plane}^*)T_{\mathbb Z^3}J_{\rm plane}x)_q
       =-\frac1{21}\sum_{\substack{p\ {
m in\ plane}\p\sim q}}x_p.
                                                               \tag{B32}
\]

The second equation retains the complete coupling to the other plaquettes.
The three-dimensional lowest coefficient -71/105 comes from B27's complete
three-component matrix, not from deleting that coupling. This source check
supports the local matrix arithmetic and preserves the antecedent's credit.
