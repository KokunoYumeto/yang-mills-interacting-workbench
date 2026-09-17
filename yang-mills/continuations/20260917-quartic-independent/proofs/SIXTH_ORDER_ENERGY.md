# Completed sixth-order ground-energy calculation, including the cube surface

Audit and continuation, 17 September 2026. This result is derived in this
session. The uploaded status line about sixth-order coefficients contained
no such coefficient table, proof, or execution record. The formulas below
retain the original Hamiltonian and open-box geometry. They are finite-order
coefficients with a separately proved finite-volume remainder, not a new
uniform-coupling or continuum mass-gap theorem.

## 1. Original parameters and exact coefficient convention

Use Q1 of `FOURTH_ORDER_SOURCE.md`:

\[
 H=\kappa\{K+\xi(2M-S)\},\qquad S=\sum_p W_p,
 \quad\kappa=2g^2/a,\quad\xi=1/(4g^4).
\tag{E1}
\]
Write the ground eigenvalue of `K-xi S` as
`e(xi)=e2 xi^2+e4 xi^4+e6 xi^6+...`. Then the original physical energy is
`E0=kappa(2M xi+e(xi))`. The additive original scalar stays in this equation.
A link-center transformation
`U_(n,i) -> (-1)^(sum_(j<i)n_j) U_(n,i)` preserves Haar and K and changes
every W_p to -W_p. It intertwines `K-xi S` with `K+xi S`; the ground
branch near zero is simple, so e is even.

Use the formal eigenline representative
`u=1+xi u1+xi^2 u2+...`, `P_H un=0`. The exact scalar return to the
original unit vacuum is Q2 and Q12 of the companion. The low-order equations
are

\[
 u_1=K^{-1}S=S/3,\qquad
 u_2=K^{-1}Q_H(Su_1),\qquad
 u_3=K^{-1}Q_H(Su_2+e_2u_1),
\]
\[
 e_2=-\langle S,u_1\rangle_H=-M/3,\qquad
 e_4=-\langle S,u_3\rangle_H=5M/216-2J/1053.
\tag{E2}
\]
Here J counts original unordered pairs of plaquettes sharing an edge.
All pairings are original Haar pairings.

The complete sixth coefficient depends only on these three actual
wavefunction coefficients:

\[
 \boxed{e_6=-\langle u_3,Ku_3\rangle_H
             -e_4\|u_1\|_H^2-e_2\|u_2\|_H^2.}
\tag{E3}
\]
For an explicit proof, use `e6=-<S,u5>=-<u1,Ku5>`.
The order-five equation is `Ku5=Q_H S u4+e2 u3+e4 u1`.
Move K through `<S u1,u4>` by `Ku2=Su1+e2`, and then use
`Ku4=Q_H S u3+e2 u2+e4`. Finally substitute
`Su2=Ku3-e2 u1`. The two cross terms `e2<u1,u3>` cancel; the remaining
terms are precisely E3. This also shows why the two state-denominator
corrections in E3 must be retained.

## 2. Complete third-vector spectral data

For one face the spin-3/2 character component of u3 is
`chi_(3/2)(Omega_p)/360`. Its kinetic norm contribution is 1/8640.
The coefficient of the original W_p in the assembled u3 is

\[
 a_p=-5/216+d_p/1053,
\tag{E4}
\]
where d_p is its original plaquette adjacency degree. This is obtained by
multiplying the self and adjacent components of u2 by each possible outer
face in `S u2+e2 u1`. It is also the coefficient required by
`e4=-sum_p a_p` and `sum_p d_p=2J`.

For the repeated multiset p,p,q on adjacent faces, put
`F=(W_p^2-1)W_q`. The two actual shared-edge spins are 1/2 and 3/2,
with Casimirs 9 and 12. The coefficients in u3 are

\[
 r_{1/2}=\frac{1/24+1/9+1/39}{9}=\frac{167}{8424},
 \qquad
 r_{3/2}=\frac{1/24+4/39}{12}=\frac5{416}.
\tag{E5}
\]
Their Haar squared masses are 1/3 and 2/3. To verify the lower mass,
write the original shared unit quaternion u and complementary unit
quaternions v,w. The harmonic projection is
`H=(8/3)(u dot v)(v dot w)-(2/3)(u dot w)`.
Using `int u_i u_j=delta_ij/4` and independent Haar in v,w gives
`<H^2>=4/9+1/9-2/9=1/3`. The full `<F^2>=1`, giving the other mass.
Thus each oriented repeated-adjacent contribution to `<u3,Ku3>` is

\[
 R_{\mathrm{adj}}=3r_{1/2}^{2}+8r_{3/2}^{2}
                 =110453/47309184.
\]
A repeated nonadjacent pair has coefficient `1/72`, Casimir 11, Haar
squared norm one, hence contribution `R_dis=11/5184`.

For a distinct pair in u2 the adjacent coefficients are
`u_0=4/27`, `u_1=4/39`, with shared-edge masses 1/4 and 3/4.
The adjacent-pair squared norm in u2 is therefore

\[
 P_2=\tfrac14(4/27)^2+\tfrac34(4/39)^2=1648/123201.
\tag{E6}
\]
The nonadjacent-pair value is 1/81, and the self value is 1/576.

For three distinct faces the original projection masses and Casimirs are
as follows. Each coefficient is the sum of its three possible outer-face
sources from E2, divided by that actual Casimir.

* No adjacency: coefficient 1/27, Casimir 9, squared mass one.
* One adjacent pair: `u_s/3`, Casimir `15/2+2s`, masses 1/4,3/4.
* Two-edge path: coefficient `(1/9+u_s+u_t)/(6+2s+2t)`, with masses
  `(1,3,3,9)/16` for shared-edge spins `(0,0),(0,1),(1,0),(1,1)`.
* Common-edge triple: coefficients
  `(3/2)(u_0+u_1)/(15/2)` and `3u_1/(21/2)`; squared masses 1/2,1/2.
* Cube corner: coefficient `[(3-n)u_0+n u_1]/(9/2+2n)`;
  the n=0,2,3 squared masses, with n=2 aggregated, are `1/16,9/16,3/8`.
  The n=1 subspace is killed by the original vertex invariant projection.

Here is a derivation of all nontrivial masses. For a path, one shared-edge
Haar projection is one half of the original two-face boundary times the
third trace, with squared norm 1/4. Both such projections give one quarter
of the eight-link boundary trace, with squared norm 1/16. Orthogonality of
the commuting original edge projections gives the remaining three masses.
For a common edge, expose three independent complementary unit quaternions
and the shared original unit quaternion. Each pair singlet term has squared
norm 1/4, and each distinct cross pairing is 1/16. The identity
`P_(1/2)F=(2/3)sum W_r P_0(W_p W_q)` gives mass
`(4/9)(3/4+6/16)=1/2`; its complement has the other half.
For a corner, the triple-singlet projection is one quarter of the six-link
boundary, of squared mass 1/16. Each single-edge-singlet projection has
squared mass 1/4. Its only additional component is one of the three n=2
channels, of mass 3/16. The full mass is one, so the n=3 remainder is 3/8.
All simple-loop Haar squared norms here equal one by integrating one of
its original links. Unique exterior links justify the stated product masses.

These give the following exact kinetic contributions for each distinct
triple in u3:

| Adjacency type | Contribution to `<u3,K u3>` |
|---|---:|
| none | 1/81 |
| one pair | 4768/369603 |
| path | 1595629/118272960 |
| common edge | 20032/1437345 |
| cube corner | 210880/14660919 |

The direct original-generator calculation in `gauge_polynomial.py` constructs
u1,u2,u3 without this table, using the exact K fields and inverse residuals.
It agrees with E3 and the table for every geometric orbit of a connected
one-, two-, or three-face set. That calculation also verifies the complete
Rayleigh numerator and denominator identity, preserving all cross terms.

## 3. Linked contributions and why six distinct cube faces occur

With independent formal face couplings, an energy coefficient with support
split into edge-disjoint components is additive in those components. The
full Haar space, electric operator and potential factor over the disjoint
edge sets; their positive vacuum product is already gauge invariant at any
shared vertices. Thus mixed connected-energy coefficients vanish on an
edge-disconnected set. Subtracting proper subcluster energies gives the
following linked sixth-order weights:

| Support | Weight |
|---|---:|
| One plaquette | `-289/77760` |
| Adjacent pair, with all sixth-order powers on that support | `22285/23654592` |
| Distinct path of three plaquettes | `-4909/118272960` |
| Three plaquettes sharing an edge | `244/4312035` |
| Three faces at a cube corner | `-212/542997` |
| All six faces of an elementary cube, each once | `-83/1944` |

For example, the original two-adjacent-face energy has
`e6=-767713/118272960`. Subtracting twice the one-face value gives the
pair weight. The original path/common/corner three-face e6 values are
`-183461/19712160`, `-5281/638820`, and `-2555051/293218380` respectively.
Subtracting the three one-face values and the actual number of adjacent
pair weights gives the table. These are rational identities, executed both
from E3 and from the independently constructed polynomial states.

The last row needs an explicit additional calculation. Let Z_e multiply
one original link by -I. It commutes with K and preserves Haar. The operator

\[
 \Pi_{\mathrm{even}}=\prod_e(I+Z_e)/2
\tag{E7}
\]
projects the original polynomial source onto the edge-even subspace. A
monomial in face couplings can contribute to the scalar energy only if its
set of odd-multiplicity faces is a mod-two closed cubical surface. For total
order six, either every face has even multiplicity (supports of at most
three faces), or the six distinct faces form an elementary cube surface.

For completeness, every finite cubical two-cycle in this open cubic box
bounds a finite mod-two set of cubes. This can be constructed by assigning
cube membership from the exterior along one coordinate: the cycle condition
ensures the assignments obtained from the other faces agree. For a nonempty
cube set, each occupied coordinate line has two boundary faces. Two distinct
cubes give at least five occupied two-dimensional projection cells in the
three directions, hence at least ten boundary faces. A boundary with at most
six faces therefore comes from exactly one cube. This proves the stated
exhaustion at order six.

### Exact cube calculation

Orient the six original face words outward. Complete face reversal leaves
an SU(2) fundamental trace unchanged. Each of the twelve original edges is
then traversed once in each direction. The identity
`int U_ab conjugate(U_cd)dU=delta_ac delta_bd/2` supplies one factor 1/2
per edge. The remaining trace-index identifications have eight independent
vertex-color loops, each of dimension two. Consequently

\[
 \left\langle\prod_{p\in\partial c}W_p\right\rangle_H
 =2^8/2^{12}=1/16.
\tag{E8}
\]
The coordinate union-find audit retains all twelve edge gluings and verifies
the eight color classes.

For an order of the six distinct face insertions, let A_k be its first k
faces. Every edge internal to A_k has both its insertions already present.
Any nontrivial spin on that edge is killed by final Haar expectation,
because no later face contains it. Its singlet projector commutes with the
remaining insertions and the Casimir. Each boundary edge carries its
original spin 1/2, so the retained intermediate energy is
`(3/4)|partial A_k|`. No proper A_k is a closed surface, so no intermediate
vacuum subtraction occurs. Therefore the full linked coefficient is

\[
 -\frac1{16}\sum_{\pi\in S_6}
   \prod_{k=1}^{5}\frac4{3|\partial A_k(\pi)|}
 =-\frac1{16}\frac{166}{243}
 =\boxed{-83/1944}.
\tag{E9}
\]
All 720 original orders and their five boundary counts are in
`results/cube_sixth_paths.json`.

There is also an independent three-plus-three calculation. Of the twenty
three-face cube subsets, twelve are paths and eight are corners. Their
all-internal-singlet u3 coefficients are 11/162 and 8/81, with boundary
energies 6 and 9/2. The cross pairing with the complementary triple is E8.
Thus the contribution to E3 is

\[
 -\frac1{16}\left[12\cdot6(11/162)^2
                   +8\cdot(9/2)(8/81)^2\right]=-83/1944.
\tag{E10}
\]
The cube term is a required original three-dimensional contribution. It
cannot be assigned a planar value by deleting the extra faces.

## 4. The complete finite-box coefficient

Let M count original plaquettes, J adjacent pairs, P3 three-face paths,
T_e common-edge triples, T_v cube-corner triples, and C cubes. The result is

\[
 \boxed{\begin{aligned}
 e_6={}&-\frac{289}{77760}M
 +\frac{22285}{23654592}J
 -\frac{4909}{118272960}P_3\\
 &+\frac{244}{4312035}T_e
 -\frac{212}{542997}T_v
 -\frac{83}{1944}C.
 \end{aligned}}
\tag{E11}
\]
This formula can also be verified before linked subtraction. The full
`||u2||^2` is
`M/576+(choose(M,2)-J)/81+J*(1648/123201)`.
The full `<u3,Ku3>` has: `3 sum_p a_p^2+M/8640`; the repeated contributions
`[M(M-1)-2J]*(11/5184)+2J*(110453/47309184)`; the distinct-triple table
in section2; and the positive norm cross term `(83/1944)C`.
Inserting these into E3 cancels every disconnected term and gives E11.

For `m=2L>=4`, the original open-box counts are

\[
 \begin{gathered}
 M=3m^2(m+1),\quad J=6m(3m^2-1),\quad C=m^3,\\
 T_e=12m^2(m-1),\quad T_v=8m^3,\\
 P_3=138m^3-126m^2-24m+12.
 \end{gathered}
\tag{E12}
\]
Here `T_e=sum_e choose(r_e,3)` for the original incidence r_e; each cube
has eight different corner triples. For paths, count the wedges centered
at an original face, then subtract three per adjacency triangle:
`P3=sum_p choose(d_p,2)-3(T_e+T_v)`.
In one orientation, faces in each boundary coordinate plane have degrees
`8-b_x-b_y`, and those in an interior plane have `12-b_x-b_y`, where
`b_x,b_y` indicate whether the face interval touches its corresponding
boundary. The numbers for `b_x+b_y=0,1,2` are `(m-2)^2,4(m-2),4`.
There are two boundary and m-1 interior planes and three orientations.
Their exact sum is `198m^3-162m^2-24m+12`, giving E12. The executable also
enumerates all original faces and triples directly for L=2,3,4.

Substitution yields the closed finite-box coefficient

\[
 \boxed{e_6=
 -\frac{211396463m^3+30959193m^2+21845782m+2336684}
        {4691494080}.}
\tag{E13}
\]
In particular, at L=2,

\[
 \boxed{\frac{E_0}{\kappa}
 =480\xi-80\xi^2+\frac{1198}{351}\xi^4
 -\frac{3528610133}{1172873520}\xi^6+R_8(\xi).}
\tag{E14}
\]
The limit of this exact coefficient divided by M is
`-211396463/14074482240`. This is a limit of a finite-order coefficient;
no interchange with an infinite-volume perturbative sum is asserted.

## 5. An independently proved finite-volume remainder

The original physical free Casimir has lowest nonconstant eigenvalue 3.
A physical nonconstant spin support has no degree-one active vertex;
a finite graph of minimum active degree two contains a cycle, and the
original cubic graph has no cycle shorter than four. Each active spin has
Casimir at least 3/4. Four spin-one-half edges around one original face
attain 3. This proves the free value used here.

On the physical space, `||S||<=2M`. On the contour `|z|=3/2`, the free
resolvent `(K-z)^-1` has norm at most 2/3. Set

\[
 R=\frac3{8M}.
\tag{E15}
\]
For `|xi|<=R`, the bounded perturbation `-xi S` has norm at most 3/4.
The contour resolvent Neumann series is thus bounded by a ratio at most
1/2, and its isolated spectral projection has the same rank one as at zero.
This gives an analytic ground branch e(xi). The elementary resolvent
inclusion `dist(z,spec K)>||xi S|| => z in resolvent(K-xi S)` puts its
single enclosed eigenvalue in `|e(xi)|<=3/4`; the other free eigenvalues
are at least 3 away from zero. On the real interval this branch is the
original ground energy after subtracting the explicit scalar 2Mxi.

Cauchy's estimate on the displayed radius and the exact parity in E1 give

\[
 \boxed{|R_8(\xi)|\le\frac34
 \frac{(|\xi|/R)^8}{1-(|\xi|/R)^2},\qquad |\xi|<R.}
\tag{E16}
\]
The physical remainder is kappa times E16. For L=2, `R=1/640`.
This complete remainder is volume dependent. It uses no unverified
uniform logarithmic-source bound and does not extend an earlier coupling
threshold or prove a continuum mass gap.

## 6. Primary-literature check with explicit conventions

For one original plaquette, K acts on class functions of
`Omega=cos(theta)I-i sin(theta)n.sigma` as
`-(partial_theta^2+2cot(theta)partial_theta)`.
Put `u(theta)=sin(theta)f(theta)` and `theta=2z`. The equation for
`K-xi W` becomes the Mathieu equation with
`a=4(e+1)` and `q=-4xi`, with zero boundary values at z=0,pi/2.
Thus the original ground branch is

\[
 e_{\mathrm{one}}(\xi)=\tfrac14b_2(-4\xi)-1.
\tag{E17}
\]
NIST DLMF 28.6.5 gives
`b2(q)=4-q^2/12+5q^4/13824-289q^6/79626240+...`.
The exact return in E17 is

\[
 e_{\mathrm{one}}=-\xi^2/3+5\xi^4/216
                         -289\xi^6/77760+\cdots,
\]
matching the independent original character recurrence and the single-face
row above. A modern original-source treatment of the single-plaquette
Mathieu spectrum is Jakobs et al., EPJC85 (2025)1418, equation39; its
Hamiltonian convention must be transported before numerical comparison.
This literature check verifies the one-plaquette convention and coefficient.
It does not claim that the full cubic-box E13 or the catalogue is new to
the literature, nor supply an independent review of those results.

Sources: https://dlmf.nist.gov/28.6.E5 ;
https://link.springer.com/article/10.1140/epjc/s10052-025-15120-x .
For the established exponential-vacuum and linked-source framework see
Schütte, Zheng Weihong and Hamer, arXiv:hep-lat/9603026, section3.
