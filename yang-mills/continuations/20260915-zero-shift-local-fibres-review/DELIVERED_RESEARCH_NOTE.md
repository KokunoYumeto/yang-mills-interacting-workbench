# Zero-shift local Yang–Mills response, all-coupling fibre inverses, and the retained exterior

15 September 2026. Continuation of the **actual-loop-moments** delivery, which in turn continues PR6 at `e98b2c3af77f66fb1c1396143ca53daef586404f`. The predecessor is preserved with its original proof and checker in the offline
package. Every analytical input used from it is reproduced below; the Git
contribution and its checker are self-contained. This note uses the full finite-regulator SU(2) Wilson Hamiltonian and its actual vacuum. Written proofs, exact finite checks, and the eventual continuum theory keep their separate evidence records.

The calculation establishes an all-coupling local conditional-kernel lower bound, a quantitative zero-shift inverse along an explicit simultaneous spatial/coupling/volume sequence, and narrow enclosures for the actual zero-shift Wilson response and restored norm. The narrow enclosure uses `xi=10^(-8)`. The all-coupling inverse is a separate result and is evaluated on a path with `g -> 0`. Both domains and the exact map between the new and previous observations are given below. General heat-kernel, conditional Poincare, and Schur techniques retain their antecedents; no historical-priority claim is made.

## 1. Full operator and original forms

The vertices are `{-L,...,L}^3`, `L>=2`, with every contained positive edge and every contained elementary face. Reverse traversal uses the inverse of the same link. With `T_alpha=-i sigma_alpha/2`, retain

\[
 X_{e,\alpha}f(U)=\left.\partial_t f(\ldots,e^{tT_\alpha}U_e,\ldots)\right|_0,
 \quad K=-\sum_{e,\alpha}X_{e,\alpha}^2,
\]
\[
 \kappa=\frac{2g^2}{a},\quad v=\frac1{2g^2a},\quad
 \xi=\frac v\kappa=\frac1{4g^4},\quad
 V=v\sum_p(2-W_p),\quad H=\kappa K+V.                 \tag{Z1}
\]
Here `a,g>0`, and each `W_p` is the original ordered fundamental trace. The scalar `2v|P|` remains. The original metric satisfies `c(T_alpha,T_beta)=delta_alpha,beta/4`, so `Delta^c=4 sum X^2`; all derivatives below are the displayed `X`.

The source [YM] constructs the unique smooth positive unit vacuum `psi`, its energy `E0`, and the `H^2/H^1` operator/form domains on the compact product group. Write

\[
 \rho=\psi^2,\quad u=\log\psi,\quad b_{e,\alpha}=X_{e,\alpha}u,
 \quad\mathcal A=\psi^{-1}(H-E_0)\psi.
\]
The map `f -> psi f` has inverse `F -> F/psi` and preserves the original inner product because `int conjugate(psi f) psi h=int rho conjugate(f) h`. Consequently

\[
 q_\rho(f,h)=\kappa\int\rho\sum\overline{Xf}Xh,
 \qquad \mathcal A=-\kappa\mathscr L,
 \quad\mathscr L=\Delta+2b\cdot X,\quad\Delta=\sum X^2. \tag{Z2}
\]
All scalar estimates are first proved on this full space and then restricted to the gauge-invariant physical space.

We use the predecessor's coordinate estimates and recall their proofs. Differentiating `Delta u+|b|^2=(V-E0)/kappa` gives

\[
 \mathscr L b_{e,\alpha}=\kappa^{-1}X_{e,\alpha}V.       \tag{Z3}
\]
The Casimir commutes with `X_e,alpha`; the commutator correction in differentiating `|b|^2` contracts an antisymmetric epsilon tensor with `b_beta b_gamma` and vanishes. Our bracket is `[X_e,alpha,X_e,beta]=-epsilon_alpha,beta,gamma X_e,gamma`.

For any scalar `h`, the antisymmetric part of the matrix `X_e,beta X_e,alpha h` has squared Frobenius norm `|X_e h|^2/2`. At a maximum of `|b_e|^2`, Z3 and `|X_e V|<=v r_e`, where `r_e<=4` counts incident faces, therefore give

\[
 |b_e|\le2r_e\xi\le8\xi,\qquad |X_e\log\rho|\le16\xi. \tag{Z4}
\]
Let `u_1=(1/3)sum_p W_p`, `b_e^1=X_e u_1`, and `r_e^1=b_e-xi b_e^1`. The original Pauli products give

\[
 |b_e^1|\le B_1=4/3,\qquad
 \sum_f\|X_f b_e^1\|_{op}\le H_1=8/3.
\]
The exact equation is `mathscr L r_e^1=-2xi sum_i b_i X_i b_e^1`. The same maximum argument gives `(1/2-16xi/3) sup|r^1| <=64xi^2/9`. Thus for `0<xi<=3/64`,

\[
 |r_e^1|\le A\xi^2,\quad A=256/9,\qquad
 \sum_\alpha\|\nabla r_{e,\alpha}^1\|_\rho^2
 \le(128A/3)\xi^4.                                   \tag{Z5}
\]
The last inequality follows by integrating the exact equation and using `|mathcal A r_e^1|<=128 kappa xi^2/3` and the preceding supremum bound. All derivative indices range over the full graph.

## 2. A heat-kernel ratio in the original SU(2) time

Let `p_theta` be the Haar-probability density of `exp(theta Delta_e)`. Write a link as `cos r I-i sin r omega.sigma`, `0<=r<=pi`; the path length in the metric making the original `X` orthonormal is `2r`. The exact radial series is

\[
 p_\theta(r)=e^{\theta/4}\sum_{n\ge1}n e^{-n^2\theta/4}
                       \frac{\sin nr}{\sin r}.        \tag{Z6}
\]
The eigenvalue `(n^2-1)/4` and multiplicity `n^2` are those of the original link Casimir; no energy coefficient has been reset.

For comparison with [HK], let `K_t^d` use the unit sphere and its area measure. The actual quaternion map sends the present differential operator to `(1/4)Delta_(S^3)` and Haar to `d sigma_3/(2pi^2)`. Thus `p_theta=2pi^2 K^3_(theta/4)`. Equation (1) of [HK] gives, with `q_theta^5=pi^3 K^5_(theta/4)`,

\[
 \partial_r p_\theta(r)=-4e^{-3\theta/4}\sin r\,q_\theta^5(r)\le0. \tag{Z7}
\]
The sphere heat kernel is positive by its parabolic maximum principle. These explicit time, measure, and derivative identities locate the maximum of `p_theta` at zero and its minimum at `pi`.

Periodizing the one-dimensional Gaussian, differentiating its normally convergent series, and using the same dimension recurrence gives

\[
 p_\theta(r)=\frac{2\sqrt\pi e^{\theta/4}}{\theta^{3/2}\sin r}
 \sum_{k\in\mathbb Z}(r+2\pi k)e^{-(r+2\pi k)^2/\theta}. \tag{Z8}
\]
For `0<theta<=4`, passage to `r=pi` pairs the terms of equal odd absolute index. Every resulting term is positive, because `2pi^2/theta-1>0`. Retaining the first pair gives

\[
 p_\theta(\pi)\ge4\sqrt\pi e^{\theta/4}\theta^{-3/2}
              (2\pi^2/\theta-1)e^{-\pi^2/\theta}.      \tag{Z9}
\]
At zero, use `n^2 exp(-theta n^2/4) <= int_(n-1)^n (x+1)^2 exp(-theta x^2/4) dx`. Summing and integrating the three Gaussian moments proves

\[
 p_\theta(0)\le e^{\theta/4}\theta^{-3/2}
          (2\sqrt\pi+4\sqrt\theta+\sqrt\pi\theta).
\]
Consequently

\[
 \frac{p_\theta(0)}{p_\theta(\pi)}
 \le a(\theta)e^{\pi^2/\theta},\quad
 a(\theta)=\frac{2\sqrt\pi+4\sqrt\theta+\sqrt\pi\theta}
                  {4\sqrt\pi(2\pi^2/\theta-1)}\le1
       \quad(0<\theta\le4).                           \tag{Z10}
\]
For the last inequality, the numerator is at most `6sqrt(pi)+8<=14sqrt(pi)` and the denominator is at least `14sqrt(pi)`, using `pi>3`.

For `theta>=4`, `|sin nr/sin r|<=n` in Z6 gives

\[
 |p_\theta-1|\le q_\theta
 =\sum_{n\ge2}n^2e^{-(n^2-1)\theta/4}
 \le5e^{-3\theta/4}\le1/4.
\]
Indeed, put `n=k+2`, use `n^2-1>=3+5k`, and sum
`sum_(k>=0)(k+2)^2 z^k=(4-3z+z^2)/(1-z)^3<=5` for `0<=z<=1/100`. Finite exponential sums prove `e^5>100` and `e^3>20`. Hence

\[
 \theta\log\frac{p_\theta(0)}{p_\theta(\pi)}
 \le(40/3)\theta e^{-3\theta/4}
 \le(160/3)e^{-3}<8/3<\pi^2.
\]
Together with Z10 this proves at every positive original time

\[
 \boxed{\quad p_\theta(0)/p_\theta(\pi)\le e^{\pi^2/\theta}.
 \quad}                                               \tag{Z11}
\]
The prefactor also matters. For `0<theta<=1`,

\[
 a(\theta)\le a_1\theta,\qquad
 a_1=\frac{3\sqrt\pi+4}{4\sqrt\pi(2\pi^2-1)}.          \tag{Z12}
\]
Every inequality above has its numerical constants explicitly evaluated. The general spherical heat-kernel identities are cited to [HK]; this note does not assert a new general heat-kernel theorem.

## 3. All-coupling local vacuum oscillation with the exterior retained

Fix a nonempty set `S` of `d` original links, and let `m_S` count all contained faces meeting it. The exact decomposition is

\[
 H=\kappa K_S+H_{\rm ext,S}+V_S,\qquad
 0\le V_S\le4v m_S.                                  \tag{Z13}
\]
`H_ext,S` includes every other link derivative and every other face, with their original constants. The two summands in `kappa K_S+H_ext,S` act on different tensor factors.

For `t=theta/kappa`, bounded-potential comparison of positive semigroups gives

\[
 e^{-4m_S\xi\theta}T_t\psi
 \le e^{-tH}\psi\le T_t\psi,
 \quad T_t=e^{\theta\Delta_S}\otimes e^{-tH_{\rm ext,S}}. \tag{Z14}
\]
For a direct proof, write the Trotter product with `exp(-t V_S/N)` between the positive free semigroups. Each multiplier is between `exp(-4vm_S t/N)` and one. Order preservation gives the bound at each product. Strong convergence, followed by a subsequence and continuity of these smooth functions, gives Z14 pointwise. Thus no bound on an omitted exterior vacuum is used.

At two points differing only in the links in S, the exterior heat kernel in `T_t` is the same. The product of the d original link kernels has ratio at most `[p_theta(0)/p_theta(pi)]^d`. The actual ground factor in `e^(-tH)psi=e^(-tE0)psi` cancels on both sides. Z11 therefore proves

\[
 \operatorname{osc}_{S\mid S^c}\log\rho
 \le8m_S\xi\theta+2d\pi^2/\theta.
\]
At the explicitly chosen `theta_*=(pi/2)sqrt(d/(m_S xi))`,

\[
 \boxed{\quad \operatorname{osc}_{S\mid S^c}\log\rho
 \le H_S:=\min\{8\pi\xi\sum_{e\in S}r_e,
                   8\pi\sqrt{d m_S\xi}\}.\quad}      \tag{Z15}
\]
The first entry is Z4 integrated over paths of length at most `2pi` in each original link. The physical heat time in the second entry is
`t_*=theta_*/kappa=(pi a/2)sqrt(d/m_S)`, since `kappa v=1/a^2`.

For the elementary square C based at the origin in directions 1 and 2, `d=4`, `m_C=13`, and `sum r_e=16`. In particular

\[
 H_C\le\min\{128\pi\xi,16\pi\sqrt{13\xi}\}
       =\min\{128\pi\xi,8\pi\sqrt{13}/g^2\}.         \tag{Z16}
\]
Boundary squares have no greater counts, so these same upper bounds cover them.

Set `c=1/g^2` and `B=8pi sqrt(13)`. For `c>=2`, choose
`theta_*=2pi/(sqrt(13)c)<1`. Z12 yields
`a(theta_*)<=1/(8c)`. To check the constant without decimal rounding, use
`pi<22/7`, `pi>157/50`, `sqrt(pi)>177/100`, `sqrt(13)>18/5`; they give

\[
 \frac{2\pi a_1}{\sqrt{13}}
 <\frac{4571875}{37274607}<\frac18.
\]
These elementary bounds are certified in the checker by an alternating Machin formula and integer-square comparisons. Keeping the prefactor in Z10 and squaring the ratio from Z14 gives the sharper all-configuration estimate

\[
 \boxed{\quad
 \frac{\sup_{U_C}\rho(U_C,Z)}{\inf_{U_C}\rho(U_C,Z)}
 \le (8c)^{-8}e^{Bc},\qquad c\ge2.\quad}             \tag{Z17}
\]
The exterior configuration Z is arbitrary and remains fixed in this formula.

## 4. The exact local observation and its zero-shift inverse

Write the original oriented links around C as `V_1,...,V_ell` (`ell=4`) and
`Omega=V_1...V_ell`. Inversely traversed links are related to the positive-link variables by `U -> U^(-1)`, its own Haar-preserving inverse; the original Casimir is preserved by this map. Retain every exterior positive link `Z=U_(C^c)`.

The global coordinate map is

\[
 (V_1,\ldots,V_\ell,Z)\longmapsto
 (\Omega,g_1,\ldots,g_{\ell-1},Z),\quad g_j=V_1\cdots V_j,
\]
\[
 V_1=g_1,\quad V_j=g_{j-1}^{-1}g_j\ (1<j<\ell),\quad
 V_\ell=g_{\ell-1}^{-1}\Omega.                        \tag{Z18}
\]
Successive Haar translations give exactly `dU=dOmega prod_j dg_j dZ`.
Let `E_l` be conditional expectation onto `(Omega,Z)` in the actual measure
`rho dU`, `J_l` its pullback, `P_l=J_l E_l`, `Q_l=I-P_l`, and
`K_l=ker E_l`. The explicit conditional density is the original rho divided
by its integral in the displayed prefix variables. Fubini gives
`E_l J_l=I`, `J_l*=E_l`, and `P_l=P_l*=P_l^2`.

Let `E_S` instead integrate all loop links given Z. Conditional Fubini gives
`E_S=E_Z E_l`; hence every `h in K_l` has zero conditional mean given Z.
The product-Haar gap for the original link Casimirs is `3/4`. At fixed Z,
minimizing over constants and comparing the maximum and minimum of the
actual conditional density give

\[
 \operatorname{Var}_{\rho(\cdot\mid Z)}h
 \le\frac43 e^{H_C}
       \int\sum_{e\in C,\alpha}|X_{e,\alpha}h|^2\rho(dU_C\mid Z).
\]
Only one maximum/minimum ratio enters: use `inf_z int |h-z|^2 rho`, bound it
above by the maximum density times the Haar variance, and bound the Haar
gradient integral by the inverse minimum density. Integrating in the unchanged
exterior marginal proves

\[
 \boxed{q_\rho(h)\ge\delta_C\|h\|_\rho^2\quad(h\in H^1\cap K_l),
 \qquad \delta_C=\tfrac34\kappa e^{-H_C}>0.}           \tag{Z19}
\]
This is true on the full scalar kernel and on its physical invariant part.
The derivative sum on the left contains all exterior derivatives as well.

The form domain `H^1 intersect K_l` is closed in the form norm. Smooth
functions are dense in it: approximate a vector in `H^1` by smooth functions
and apply `Q_l`; the compact smooth positive-density integral defining `E_l`
preserves `H^1` and smoothness. Its derivative formula follows by differentiating
under the compact integral, with finite smooth density coefficients. Thus the
restricted closed form represents a self-adjoint `D_l>=delta_C`. Its resolvent
is compact at each finite regulator by the compact `H^1 -> L^2` embedding.
In particular `D_l^(-1)` exists on all of `K_l` and

\[
 \|D_l^{-1}\|\le\frac4{3\kappa}e^{H_C}.              \tag{Z20}
\]
This supplies the zero-shift inverse used below, rather than postulating a
lower spectral bound for the unresolved conditional kernel.

### 4.1 A fixed simultaneous continuum/coupling/volume sequence

Retain the earlier family

\[
 a_n=a_0 2^{-n},\quad L_n=4\,2^{2n},\quad
 c_n=g_n^{-2}=c_0+\beta n\log2,
 \quad\kappa_n=2^{n+1}/(a_0c_n),\qquad a_0,c_0,\beta>0.
\]
For `c_n>=2`, Z17–19 prove for every elementary square

\[
 \delta_n\ge\frac{3\,8^8}{2a_0}e^{-Bc_0}
             c_n^7 2^{(1-B\beta)n}.                 \tag{Z21}
\]
Now select the actual member `beta=1/B`, keeping `c0,a0` unchanged. Then
`a_n ->0`, `a_n L_n ->infinity`, `g_n ->0`, and

\[
 \boxed{\|D_{l,n}^{-1}\|
 \le\frac{2a_0e^{Bc_0}}{3\,8^8}c_n^{-7}\longrightarrow0.} \tag{Z22}
\]
The threshold is the explicit integer
`n0=max(0,ceil((2-c0)/(beta log2)))`. These kernels describe elementary local
loop fibres at each regulator; their physical loop size is `a_n`. The path's
coefficient is not assigned a quantum beta-function interpretation.

The power seven uses the retained heat prefactor. Replacing Z10 by Z11 alone
would give just `(3/(2a0)) exp(-Bc0)/c_n` as the corresponding lower bound at
this same beta. Both estimates are recorded, and Z17 proves the extra factor
`(8c_n)^8` relating them.

For a finite list of retained smooth physical observations at regulator n,
let K0 be its raw kinetic Gram and W its actual coupling to K_l,n.
Nonnegativity of the original coupled form gives `W*D_l,n^(-1)W<=K0` by
inserting the actual minimizing lift. The exact resolvent identity therefore
supplies on `|z|<delta_n`

\[
 M_n(z)=\sum_{j=0}^d z^j W^*D_{l,n}^{-j-1}W+\mathcal R_{n,d}(z),
\]
\[
 |x^*\mathcal R_{n,d}(z)y|
 \le\frac{(|z|/\delta_n)^{d+1}}{1-|z|/\delta_n}
                 \sqrt{x^*K_0x}\sqrt{y^*K_0y}.        \tag{Z23}
\]
To prove it, factor the remainder through `D^(-1/2)W`, the multiplier
`(zD^(-1))^(d+1)(I-zD^(-1))^(-1)`, and its adjoint source. Every coefficient
is an original inverse moment. In particular this is continuation through
zero spectral shift with quantified remainder. For the elementary trace,
`K0<=4kappa_n`; choosing `d=n` makes the absolute remainder tend to zero on
every fixed complex disk along Z22, since the logarithm of its upper bound
has the term `-7(n+1)log c_n+O(n)`. No value of a limiting inverse moment or
full coupled resolvent pole is assigned by this statement.

## 5. A second-order local logarithmic vacuum with its full remainder

The rest of the note evaluates the actual local zero-shift response on the
stated small-xi domain. This calculation is independent of the specialization
of beta in Z22.

For two adjacent elementary faces p,q sharing edge e, let
`j_pq=sum_alpha (X_e,alpha W_p)(X_e,alpha W_q)`. Orient their traversals
along e consistently by reversing a complete face word when necessary;
SU(2) trace is unchanged under word inversion. With U the shared link and
A,B the two three-link complementary products, the original Pauli identity is

\[
 j_{pq}=-\tfrac14\operatorname{tr}(UAUB)+\tfrac14\operatorname{tr}(AB^{-1}),
 \quad j_{pq}^0=\tfrac38\operatorname{tr}(AB^{-1}),
 \quad j_{pq}^1=j_{pq}-j_{pq}^0.                      \tag{Z24}
\]
Haar integration of the original quaternion U gives `E_U j_pq=j_pq^0`.
The shared-link Casimir on these two components has eigenvalues 0 and 2.
The other six original links each contribute `3/4`. Thus the total original
Casimir eigenvalues are `9/2` and `13/2`. This retains both components and
their original norms `9/64` and `3/64`.

Define the actual local polynomial

\[
 u_2=-\frac1{72}\sum_p(W_p^2-1)
       +\sum_{\{p,q\}\ \mathrm{adjacent}}
            (\tfrac4{81}j_{pq}^0+\tfrac4{117}j_{pq}^1). \tag{Z25}
\]
The pairs are unordered, counted once. Every face in these sums is contained
in the original graph. `K(W_p^2-1)=8(W_p^2-1)`, and expansion of
`|grad u1|^2` gives the exact equality

\[
 Ku_2=|\nabla u_1|^2-|P|/3.                           \tag{Z26}
\]
Indeed the self terms are `(1/9)sum_p(4-W_p^2)` and each adjacent pair occurs
with coefficient `2/9`. The eigenvalues just computed give Z25 term by term.
This fixes an explicit Haar-mean-zero coefficient representative for u2;
the actual u and its ground energy are not changed.

Put `b_e^2=X_e u2`. The following local constants hold for every edge:

\[
 |b_e^2|\le B_2=146/117,\qquad
 \sum_f\|X_f b_e^2\|_{op}\le H_2=476/117.             \tag{Z27}
\]
Here are the counts and bounds. An edge is in at most four self terms, at
most six adjacent pairs sharing that edge, and at most 36 pairs in which it
is unshared. For a trace word with length N and m_e occurrences of e,
unit-direction generator insertions bound its gradient by m_e and its summed
second-derivative block norms by `m_e N/2`. Apply this to the length-eight
and length-six words in Z24, retaining the two occurrences of the shared link.
For j use gradient bounds 1 (shared), 1/2 (unshared), and second-derivative
row bounds 2 and 7/4. For j0 use 0 and 3/8 in the gradient and 0 and 9/8 in
the second-derivative row. The pair in Z25 is `(4/117)j+(16/1053)j0`.
The self contributions to the two totals are 2/9 and 8/9. Therefore

\[
 B_2=2/9+6(4/117)+36(8/351),
 \quad H_2=8/9+6(8/117)+36(9/117).
\]
These are upper bounds on the original differentiated words, not rewritten
independent variables.

Set `u_app=xi u1+xi^2 u2` and `r_e^2=X_e(u-u_app)`. Its retained scalar
energy is `E_app/kappa=2xi|P|-xi^2|P|/3`. Direct expansion proves

\[
 \Delta u_{\rm app}+|\nabla u_{\rm app}|^2
 =V/\kappa-E_{\rm app}/\kappa+R_{\rm app},
 \quad R_{\rm app}=2\xi^3 b^1\cdot b^2+\xi^4|b^2|^2,
\]
\[
 \mathscr Lr_e^2=-X_eR_{\rm app}-2\sum_i r_i^2 X_i b_e^{\rm app}. \tag{Z28}
\]
In differentiating the dot products, the two commutator corrections cancel
against each other, by antisymmetry. Consequently

\[
 |X_eR_{\rm app}|\le2\xi^3(H_1B_2+B_1H_2+\xi B_2H_2).
\]
At an edge and configuration maximizing `|r_e^2|` over the entire finite
graph, the antisymmetric-Hessian argument yields

\[
 (1/2-2\xi H_1-2\xi^2H_2)\sup|r^2|
 \le2\xi^3(H_1B_2+B_1H_2+\xi B_2H_2).
\]
For `0<xi<=1/32`, the left coefficient is at least `4873/14976>1/4`, and
`8(H1 B2+B1 H2+B2 H2/32)=975838/13689<72`. We have proved

\[
 \boxed{|b_e-\xi b_e^1-\xi^2b_e^2|\le72\xi^3
                  \quad(0<\xi\le1/32).}              \tag{Z29}
\]
All constants are independent of the exterior box.

## 6. Exact parity and a second-order marginal estimate

The central link map

\[
 (\mathcal ZU)_{(n,i)}=(-1)^{\sum_{j<i}n_j}U_{(n,i)} \tag{Z30}
\]
is an involution, preserves original Haar, and commutes with every X.
Multiplying its four signs around each contained face gives -1. Therefore
u1 is odd, u2 is even, and differentiation preserves those parities. No
invariance of the interacting vacuum under this map is asserted or used.

For the original elementary loop C, let S0 be its edges and those of the
twelve other faces meeting it; `|S0|=32`. Let S1 contain all edges of every
contained face meeting S0. Infinite-lattice counting gives `|S1|=108` and
`m_(S1)=173`; boundary truncation only reduces these two upper bounds. The
checker enumerates the actual edge and face sets, also on L=2. Derivatives
b2 on C, and b1 on any edge of S0, are supported inside S1.

At a fixed exterior of S1, retain the conditional density mu on its original
Haar variables. Let `t=2xi u_(1,S1)`, where u_(1,S1) contains exactly the
faces meeting S1. Its Haar mean is zero and `|t|<=B_d=4(173)xi/3`.
Z5 integrated along original link paths gives an oscillation at most
`R_d=4pi(108)A xi^2` for `log rho-t`. Comparing the two explicit conditional
density integrals, and using `int exp(t)>=1`, gives

\[
 |\mu-1-2\xi u_{1,S1}|\le E_2,
 \quad E_2=e^{B_d}\left[e^{R_d}-1+\frac{B_d^2}{2}(2+B_d)\right]. \tag{Z31}
\]
For completeness, `|exp(t)-1-t|<=B_d^2 exp(B_d)/2` bounds both the numerator
remainder and `int exp(t)-1`. The factor `(2+B_d)` follows by writing
`exp(t)/int exp(t)-(1+t)` and retaining the denominator. The oscillation
bound compares mu with that exact exponential density by a ratio in
`[exp(-R_d),exp(R_d)]`.

For an even polynomial P supported in S0, the linear contribution of t to
its Haar integral is zero. A face not fully contained in S0 has an unmatched
integrated link in S1; a face contained in S0 is odd under Z30 while P is
even. Thus

\[
 |\langle P\rangle_\rho-\langle P\rangle_H|
       \le E_2\int_H|P|.                             \tag{Z32}
\]
The same proof holds for complex linear combinations with that parity.
For an odd polynomial supported in S1, its Haar mean is zero; Z4 and the
local marginal ratio give

\[
 |\langle P\rangle_\rho|
 \le\delta_1\int_H|P|,\quad
 \delta_1=e^{32\pi(108)\xi}-1.                       \tag{Z33}
\]
More generally, for every polynomial supported in S1 the same original
marginal ratio gives `|<P>_rho-<P>_H|<=delta1 int_H |P|`.
This records the density's contribution, rather than setting the actual
odd expectation to zero.

## 7. Trial vectors and all conditional derivative scores

Let `F=tr Omega`, `J=sum_(12 neighbors p) j_(pC)`, and
`w=(2kappa xi/3)J`. In the local observation of section 4 the actual forcing is

\[
 W=-Q_l\mathcal AF=Q_l(w+2\kappa d),\quad
 d=\sum_{e\in C}(b_e-\xi b_e^1)\cdot X_eF,
 \quad |d|\le\ell A\xi^2.                            \tag{Z34}
\]
The omitted-in-the-kernel own-face term is explicitly
`(xi/3)(4-F^2)`; it is a function of Omega, so applying Q_l to it is zero.
Z29 gives `d=xi^2 d2+r_d`, with `d2=sum_(e in C)b_e^2.X_eF`,
`|d2|<=ell B2`, and `|r_d|<=72ell xi^3`. Under Z30, d2 is odd.

Use `z=kappa omega`, with inverse `omega=z/kappa`, and `|omega|<=1/4`.
In the original face coordinates set

\[
 y_z=\frac{2\xi}{3}\sum_{p=1}^{12}
   \left(\frac{j_p^0}{9/2-\omega}
                   +\frac{j_p^1}{13/2-\omega}\right),
 \qquad (\kappa K-z)y_z=w.                           \tag{Z35}
\]
For the conditional Haar map E0 at fixed `(Omega,Z)`, each summand has zero
mean. Flip the shared loop edge and one other loop edge not in p; the two
central signs preserve Omega and Haar on its fibre, and flip both j_p^0
and j_p^1. Thus `E0 y_z=0`. This also gives `E0 Y y_z=0` and
`E0 X_f y_z=0` for exterior f, by their exact conditional derivative formulas.

The original Haar norms and differentiated words give, throughout the disk,

\[
 \|w\|_H=\kappa\xi,\quad \|y_z\|_H\le J_*\xi,
 \quad\|y_z\|_\infty\le P_*\xi,\quad
 \sum_e\|X_ey_z\|_\infty\le L_*\xi,
\]
\[
 J_*=\sqrt{12/289+4/625},\quad P_*=736/425,\quad L_*=2752/425. \tag{Z36}
\]
To reproduce the last two constants, write a summand of `y_z/xi` as
`a j_p+b j_p^0`. One has `|a|<=8/75`, `|b|<=64/1275`,
`|j_p|<=1`, `|j_p^0|<=3/4`, `sum|Xj_p|<=4`, and
`sum|Xj_p^0|<=9/4`. Summing twelve gives exactly Z36. The first norm is
`12(4/9)(9/64+3/64)=1`; the second retains both denominators and gives
`(3/4)/(17/4)^2+(1/4)/(25/4)^2=12/289+4/625`.

Put `p_z=P_l y_z`, `Y_z=Q_l y_z`, and
`eta=exp(128pi xi)-1`. The actual-to-Haar fibre ratio lies in
`[exp(-128pi xi),exp(128pi xi)]`; therefore
`||p_z||_rho<=eta P_* xi`.

Here is a bound on all derivatives of this projection, including all exterior
links. In oriented loop coordinates use
`Y_alpha=(1/ell)sum_(j,beta)(Ad(V1...V_(j-1)))_(alpha,beta) X_(j,beta)`.
Its Haar divergence is zero and `Y J_l f=J_l X_Omega f`. Set

\[
 S_\Omega=Y\log\rho-J_l(X_\Omega\log m),\qquad
 S_f=X_f\log\rho-J_l(X_f\log m)\quad(f\notin C),
\]
where m is the actual `(Omega,Z)` marginal. Differentiation under the compact
conditional integral gives
`X_Omega E_l h=E_l(Yh)+E_l(h S_Omega)` and
`X_f E_l h=E_l(X_fh)+E_l(h S_f)`. Each score has conditional mean zero.

Prefix variation in g_j, at fixed Omega, has the exact coordinate formula

\[
 Z_{j,\alpha}=\sum_\beta\left[
  (\operatorname{Ad}g_{j-1}^{-1})_{\beta\alpha}X_{V_j,\beta}
 -(\operatorname{Ad}g_j^{-1})_{\beta\alpha}X_{V_{j+1},\beta}\right],
 \qquad g_0=I.
\]
It differentiates the adjacent links `V_j,V_(j+1)` with opposite transported
generators. Define `z_j=(Ad g_(j-1)) X_(V_j) h`; each adjoint is orthogonal
in the original three generator coordinates. Then `Z_j h=z_j-z_(j+1)`.
The path
incidence matrix therefore has squared norm
`c_ell=2+2cos(pi/ell)<=4`. The exact identity
`4 sum|z_j|^2-sum|z_j-z_(j+1)|^2>=0` also suffices. Product-Haar Poincare
on the ell-1 prefixes and the same density ratio prove

\[
 \operatorname{Var}(h\mid\Omega,Z)
 \le\tfrac43 e^{128\pi\xi}\,E_\rho\sum_{j,\alpha}|Z_{j,\alpha}h|^2.
\]
For exterior f, `X_e b_f=X_f b_e` whenever `e in C`, so integration yields

\[
 \int m\left(\ell\operatorname{tr}\Gamma_\Omega+
                   \sum_{f\notin C}\operatorname{tr}\Gamma_f\right)
 \le\xi^2\overline\Gamma(\xi),                       \tag{Z37}
\]
\[
 \overline\Gamma(\xi)=\ell(8/3+2A\xi)^2+
 \frac{16}{3}c_\ell e^{128\pi\xi}\ell
       (\sqrt{7/3}+\sqrt{128A/3}\,\xi)^2.
\]
In this formula Gamma is the actual conditional score covariance. The
`7/3` follows from the original second-derivative Frobenius bound `3/4`:
for fixed e, the incident plaquette multiplicities satisfy
`sum_f t_ef^2=r_e^2+3r_e<=28`, and the factor `(1/3)^2` gives `28/12`.
Z5 bounds the remainder Hessian in the full derivative sum. The Omega
part uses `ell |Y log rho|^2<=sum_(e in C)|X_e log rho|^2` and
`|b_e|<=4xi/3+Axi^2`.

Using the zero conditional Haar means after Z35 and Cauchy–Schwarz for the
score terms gives

\[
 \sqrt{q_\rho(p_z)}\le\sqrt\kappa\,\xi P_E,
 \quad P_E=\eta L_*+P_*\xi\sqrt{\overline\Gamma(\xi)}. \tag{Z38}
\]
The first summand bounds the density difference on every differentiated
trial column. The second is bounded by `||y_z||_infty` times the square root
of the complete score covariance in Z37. The q pairing here contains both
`ell |X_Omega E_l y|^2` and all original exterior derivatives.

## 8. Complex residual identity and an evaluated fourth-order error

For `0<xi<=10^(-5)`, Z16–19 give `D_l>=kappa/2`; e.g.
`exp(128pi/10^5)<3/2`. Thus the disk `|z|<=kappa/4` is in its resolvent set.
All trial and projected functions are smooth at each finite regulator, so
all expressions below have their original operator domains. The same
calculation also holds as a closed-form identity.

Let `R_z=W-(D_l-z)Y_z`. For every `h in H^1 intersect K_l`, direct use of
Z34–35 gives the exact weak residual

\[
 \langle R_{\bar z},h\rangle
 =2\kappa\langle d+b\cdot\nabla y_{\bar z},h\rangle
                              +q_\rho(p_{\bar z},h). \tag{Z39}
\]
Complex conjugation in the first slot is explicit. Set

\[
 B_b=B_1+A\xi,\quad R_0=2(\ell A+B_bL_*),\quad
 E=\sqrt2 R_0\xi+P_E.
\]
Z19 and Z38 give
`||D_l^(-1/2)R_z||<=sqrt(kappa) xi E`. Factoring the actual inverse through
`D_l^(-1/2)` gives `||(I-zD_l^(-1))^(-1)||<=2`. Therefore the exact identity

\[
 M(z):=\langle W,(D_l-z)^{-1}W\rangle
 =B_z+\langle R_{\bar z},(D_l-z)^{-1}R_z\rangle,
\]
\[
 B_z=2\langle W,Y_z\rangle-q_z(Y_{\bar z},Y_z),
 \quad q_z(f,h)=q_\rho(f,h)-z\langle f,h\rangle        \tag{Z40}
\]
has remainder bounded in absolute value by `2kappa xi^2 E^2`.

The complete expansion of B_z is conveniently written as a bilinear
integral `B(f,h)=int rho f h` (ordinary conjugate-linear pairings are still
used in norms):

\[
 \begin{split}
 B_z={}&B(w,y_z)+2\kappa B(b\cdot\nabla y_z,y_z)
                 +4\kappa B(d,y_z)\\
       &-4\kappa B(d+b\cdot\nabla y_z,p_z)
                 -q_z(p_{\bar z},p_z).               \tag{Z41}
 \end{split}
\]
It follows by expanding `Y_z=y_z-p_z`, using
`(mathcal A-z)y_z=w-2kappa b.grad y_z`, and the original symmetry of the
Dirichlet form. Thus every projection and state cross term remains.

The Haar value of the first term is

\[
 M_H(z)=\kappa\xi^2\left[
        \frac{3/4}{9/2-z/\kappa}+\frac{1/4}{13/2-z/\kappa}\right]. \tag{Z42}
\]
This uses the original twelve neighbor integrals and their unmatched-link
cross-pairing witnesses. Both w and y_z are even and supported in S0, so
Z32 bounds their density correction by `kappa xi^2 E2 J_*`.
The cubic terms `b1.grad y_z times y_z` and `d2 y_z` are odd under Z30 and
supported in S1; use Z33 on them. Use Z5 on the remaining b term, Z29 on
the remaining d term, and Z38 on the last line of Z41. These explicit steps
prove

\[
 \boxed{|M(z)-M_H(z)|\le\kappa\xi^4 C(\xi)
                     \quad(|z|\le\kappa/4),}         \tag{Z43}
\]
where, with `H0=1024pi xi`,

\[
\begin{split}
 C(\xi)={}&\frac{E_2J_*}{\xi^2}
 +\frac{\delta_1}{\xi}J_*(2B_1L_*+4\ell B_2)
 +e^{H_0/2}J_*(2AL_*+288\ell)\\
 &+4\frac\eta\xi P_*(\ell A+B_bL_*)
 +(P_E/\xi)^2+\tfrac14(\eta/\xi)^2P_*^2
 +2(E/\xi)^2.                                        \tag{Z44}
\end{split}
\]
No limiting notation conceals a regulator constant in this finite bound.

At `xi=10^(-8)`, exact outward rational arithmetic in the checker gives
`C(xi)<26,000,000`. It uses `c_ell<=4`, the alternating Machin enclosure
for pi, integer-square upper bounds for each square root, and an exponential
Taylor polynomial with its explicit positive tail. A second, independent
arithmetic path uses only `pi<22/7`, six explicit rational square upper
bounds, and `exp(t)-1<=t/(1-t)` for `0<=t<1`; it gives the larger still-valid
integer upper bound `25,222,642`. Z43 therefore yields

\[
 \boxed{\left|M(0)-\frac8{39}\kappa\xi^2\right|
       <26,000,000\,\kappa\xi^4.}                   \tag{Z45}
\]
Both functions in Z43 are holomorphic on a neighborhood of the closed disk.
Cauchy's derivative formula on its original radius `kappa/4` gives

\[
 \boxed{\left|\|D_l^{-1}W\|_\rho^2-
                        \frac{196}{4563}\xi^2\right|
       <104,000,000\,\xi^4.}                        \tag{Z46}
\]
Here `M'(0)=<W,D_l^(-2)W>`, and
`(3/4)/(9/2)^2+(1/4)/(13/2)^2=1/27+1/169=196/4563`.
In coefficient form the error radii are respectively `2.6*10^(-9)` and
`1.04*10^(-8)`. These are errors in the displayed coefficients, not a claim
of relative error with respect to an unspecified small denominator.

## 9. Original coupled energy and the exterior comparison

Write `f=F-<F>_rho`, `G=||f||_rho^2`, and
`K0=q_rho(J_l f)=kappa(4-<F^2>_rho)`. The calculation Z47a–d below implies, at `xi=10^(-8)`,

\[
 |G-1|<1.1\,10^{-13},\qquad |K_0-3\kappa|<1.1\,10^{-13}\kappa. \tag{Z47}
\]
The underlying means are unchanged by retaining the exterior in the
observation: both are the same original rho integrals. In fact the new
second-order calculation gives a substantially sharper description of them.

Write `j_a=sum_(e in C)b_e^a.X_eF` for a=1,2 and
`j=b.grad F=xi j1+xi^2 j2+r_j`, `|r_j|<=72ell xi^3`.
Stationarity of the original weighted Laplacian applied to F and F squared
gives the exact identities

\[
 3\langle F\rangle=2\langle j\rangle,\qquad
 \langle F^2\rangle-1=\tfrac12\langle Fj\rangle.       \tag{Z47a}
\]
Here `j1=(4-F^2+J)/3` is even, `j2` is odd, and
`int_H |j1|<=3/2`. Equations Z32–33 and Z29 give

\[
 |\langle F\rangle-2\xi/3|\le e_\mu,
 \quad e_\mu=\xi E_2+\tfrac23\ell B_2\xi^2\delta_1
                                    +48\ell\xi^3.   \tag{Z47b}
\]
The original finite Haar coefficients needed in the second identity are

\[
 \langle Fj_1 u_{1,S1}\rangle_H=2/9,\qquad
 \langle Fj_2\rangle_H=-1/18.                         \tag{Z47c}
\]
For the first, the own-face term gives
`(4<F^2>_H-<F^4>_H)/9=2/9`. Every other face paired with the own term has
an unmatched exterior link. In the J term, a neighboring trace can cover
its three exterior links only by being that same neighbor. Its contribution
then integrates `W_p X_e W_p=(1/2)X_e(W_p^2)` in the complementary product;
`int W_p^2=1` makes this zero. A different face leaves an unmatched link.
For the second equality, Haar integration by parts gives
`<Fj2>_H=(1/2)<u2 K(F^2)>_H=4<u2(F^2-1)>_H`.
In u2 only the own self term survives: its covariance is `-1/72`.
Every other self term integrates its nonconstant spin-one character to zero;
every adjacent pair has six distinct unshared links, at least one outside
the four-link C. That original link annihilates its pairing. These arguments
account for every term of the global u2 without an extensive error.

The finite error coefficients are

\[
 \begin{split}
 \epsilon_2={}&\frac{E_2}{2\xi}\frac{\sqrt5+3/2}{3}
               +\frac{\delta_1}{2}\frac{\ell B_2}{\sqrt2}
               +72\ell\xi,\\
 \epsilon_G={}&\epsilon_2+
                  \frac{(4\xi/3)e_\mu+e_\mu^2}{\xi^2}.
 \end{split}
\]
Indeed `int |Fj1| <=(sqrt(5)+3/2)/3`, and
`int |Fj2| <=ell B2/sqrt(2)` by
`int F^2 |X_eF|^2=1/2`. Use Z31 for the first linear density contribution,
Z33's simple density bound for the second, and the uniform r_j bound for
the last. Substitution in Z47a proves the actual enclosures

\[
 \boxed{\begin{gathered}
 |\langle F^2\rangle-1-(7/36)\xi^2|\le\epsilon_2\xi^2,\\
 |G-1+(1/4)\xi^2|\le\epsilon_G\xi^2,\qquad
 |K_0-\kappa(3-(7/36)\xi^2)|\le\kappa\epsilon_2\xi^2.
 \end{gathered}}                                      \tag{Z47d}
\]
At `xi=10^(-8)`, the outward rational evaluation gives
`e_mu<1.282*10^(-19)`, `epsilon2<0.000767`, and
`epsilonG<0.000767`. Thus the original raw Gram is quantitatively retained
even at its second interaction order.

Let `h0=D_l^(-1)W`, `Z0=||h0||^2`, and `F0=K0-M(0)`. For arbitrary
`x in C` and `h in K_l`, define `k=h-h0 x`. Expansion of the original
coupled form, with `W=-Q_l mathcal A f`, proves

\[
 q_\rho(xf+h)=F_0|x|^2+q_\rho(k),\qquad
 \|xf+h\|_\rho^2=G|x|^2+\|h_0x+k\|_\rho^2.          \tag{Z48}
\]
At this coupling the exact intervals Z45–47 and Z19 prove

\[
 \boxed{q_\rho(xf+h)\ge(0.74999\,\kappa)\|xf+h\|_\rho^2
                    \quad(h\in H^1\cap K_l).}       \tag{Z49}
\]
For an explicit verification put `m_*=0.74999 kappa` and use
`delta_C>=(3kappa/4)exp(-128pi xi)`. The two by two quadratic form obtained
from Z48 is nonnegative because

\[
 \delta_C-m_*>0,\quad F_0-m_*(G+Z_0)>0,\quad
 [F_0-m_*(G+Z_0)](\delta_C-m_*)-m_*^2Z_0>0.
\]
The checker verifies these inequalities with rational lower/upper endpoints.
The cross term `2 Re <h0 x,k>` is bounded at exactly this step, not deleted.
Thus Z49 covers the entire original local conditional kernel, including its
exterior dependence, together with the observed loop direction.

The corresponding physical restored state is
`Phi=psi(f+D_l^(-1)W)`. Its norm and excitation energy are exactly

\[
 \|\Phi\|^2=G+Z_0,\qquad q_{H-E_0}(\Phi)=K_0-M(0).  \tag{Z50}
\]
It is perpendicular to the actual vacuum because f is centered and the kernel
primitive has conditional mean zero. Its one-dimensional variational
inclusion gives the upper bound `Delta_L<=q(Phi)/||Phi||^2` for the complete
physical gap. The separate lower bound Z49 is on its explicitly stated
form subspace. The new scalar moments also resolve the interaction correction
of this actual restored state's Rayleigh quotient:

\[
 \boxed{\quad
 0.2184<\frac{q_{H-E_0}(\Phi)/(\kappa\|\Phi\|^2)-3}{\xi^2}
                 <0.2248,\qquad \xi=10^{-8}.\quad}    \tag{Z50a}
\]
To verify without discarding the denominator, put
`d0=-1/4+196/4563`, and write the exact numerator and denominator in Z50
using Z45–46 and Z47d. The coefficient at their ratio is

\[
 \frac{337/1521+e}{1+\xi^2(d_0+e_d)},\quad
 |e|\le\epsilon_2+26,000,000\xi^2+
                  3\epsilon_G+312,000,000\xi^2,\quad
 |e_d|\le\epsilon_G+104,000,000\xi^2.
\]
Here `337/1521=3/4-7/36-8/39-3(196/4563)` is exact.
The checker retains the original denominator and obtains Z50a by rational
upper and lower bounds. In particular the lowered energy from kernel
restoration and the change in the physical state norm are both included.

### 9.1 Exact return to the previous Omega-only observation

Let E_C denote the earlier expectation onto Omega alone. The conditional
map E_o from `(Omega,Z)` to Omega satisfies

\[
 E_C=E_oE_l,\qquad J_C=J_lJ_o,\qquad K_l\subset K_C=\ker E_C.
\]
The exact quotient map and inverse are

\[
 K_C/K_l\xrightarrow{\cong}\ker E_o,\quad[h]\mapsto E_lh,
 \qquad k\mapsto[J_lk].                              \tag{Z51}
\]
Fubini and `E_l J_l=I` prove both inverse laws. Thus the local response in
Z45 is not assigned to the old full kernel by dropping its additional
exterior fluctuations; Z51 computes those fluctuations.

For any retained coarse form vector g, let `h_l(g)` minimize the original
energy of `J_lg+h` over `h in K_l`, and put
`S_lg=J_lg+h_l(g)`, `q_eff(g,v)=q_rho(S_lg,S_lv)`. Z19 proves existence
and uniqueness by the energy Riesz theorem. This extends the smooth forcing
formula `h_l(g)=D_l^(-1)(-Q_l mathcal A J_lg)` to its actual form domain.
At a fixed finite regulator the original centered physical gap is positive
by compactness and uniqueness of the vacuum. Consequently there is a unique
`k_* in ker E_o` minimizing `q_eff(J_o f+k)` on this actual form fibre.
No uniform estimate for this second minimization is inserted.

Orthogonality of the two minimum sections proves the exact response and
state formulas

\[
 M_C(0)=M_l(0)+q_{\rm eff}(k_*),\qquad
 h_C=h_l(J_of)+J_lk_*+h_l(k_*),                        \tag{Z52}
\]
\[
 \|f+h_C\|_\rho^2
 =G+\|k_*\|_m^2+\|h_l(J_of)+h_l(k_*)\|_\rho^2.       \tag{Z53}
\]
The last norm retains the cross pairing of the two original kernel lifts.
Equations Z51–53 are the exact map and energy remainder connecting the
present local estimate to the previous wider observation. The additional
quantity `q_eff(k_*)` has not been bounded uniformly here. Nevertheless
Z45 and Z52 already give a zero-shift bound for that previous observation:

\[
 M_C(0)\ge\kappa\xi^2(8/39-2.6\,10^{-9}),\qquad
 M_C(0)\le K_0,\qquad \xi=10^{-8}.
\]
The lower bound is obtained through the exact inclusion of the local
primitive space. No monotonicity of the restored state norm is inferred;
its full cross term is Z53.

## 10. Split Zero primitives and controlled completion

At fixed regulator and loop, choose finite-dimensional nested smooth trial
spaces V_j in K_l. Use the actual support-indexed windows

\[
 V_j\xrightarrow{D_l}K_l\xrightarrow0 0.
\]
Since D_l is invertible, the transported-class kernel and both inverse maps are

\[
 V_{j+1}/V_j\xrightarrow{\cong}
 \ker[K_l/D_lV_j\to K_l/D_lV_{j+1}],\quad[h]\mapsto[D_lh],
 \qquad[D_lh]\mapsto[h].                             \tag{Z54}
\]
Give K_l the original dual-energy pairing `<r,t>_-1=<r,D_l^(-1)t>`.
Then `<D_lh,D_lv>_-1=q_rho(h,v)`. The minimum residual of the forcing W
at support j has quotient squared norm equal to the exact remaining
response error. For a noncanonical trial Y, write
`aY=q(Y)`, `cY=<Y,W>`, `alphaY=cY/aY`. Its correction and norm identity are

\[
 R=W-D_lY=R_{\rm can}+(\alpha_Y-1)D_lY,
\]
\[
 \langle R,D_l^{-1}R\rangle
 =\|[W]\|_{K_l/D_l\operatorname{span}Y}^2
                          +a_Y|\alpha_Y-1|^2.        \tag{Z55}
\]
At Y=Y_0 from Z35, positivity of aY follows from Z19 and Y0 nonzero: its
Haar norm is positive, while the explicit projection bound in section 7 is
smaller than its rho norm at `xi=10^(-8)`. Z55 keeps the canonical correction
in the original incoming image. The reconstruction of [SZ] sends a killed
relation to its receiving support's zero and retains these actual primitives.

For an optional simultaneous-family completion, take one elementary loop at
each n on the exact path Z22 and form
`mathscr K=direct_sum_(n>=n0) K_l,n` with the original counting sum of its
rho_n pairings. The diagonal operator `mathscr D=direct_sum D_l,n` has domain
`{(h_n):h_n in Dom D_l,n, sum||D_l,n h_n||^2<infinity}`. Its inverse is the
literal coordinate map `(r_n)->(D_l,n^(-1)r_n)`. Testing coordinatewise and
using the uniform tail bound proves both inverse laws and self-adjointness.
Its finite-support truncation error is at most

\[
 \|\mathscr D^{-1}-\mathscr D^{-1}P_{\le N}\|
 \le\frac{2a_0e^{Bc_0}}{3\,8^8}c_{N+1}^{-7}.          \tag{Z56}
\]
Each finite block inverse is compact and this tail tends to zero, so the
original family inverse is compact. This completion has regulator-indexed
vectors and the displayed sum pairing. No identification of it with a
four-dimensional physical Hilbert space is part of the construction.


There is also an explicit completion-killed cohomology module on these same
operators. Let `mathscr K_fin` denote the original finite-support vectors and
use the two windows

\[
 \bigoplus_{\mathrm{alg},n}\operatorname{Dom}D_{l,n}
       \xrightarrow{\mathscr D}\mathscr K\longrightarrow0,
 \qquad
 \operatorname{Dom}\mathscr D\xrightarrow{\mathscr D}\mathscr K
       \longrightarrow0.
\]
Their actual first cohomologies are `mathscr K/mathscr K_fin` and zero.
The transition kernel is the full first quotient, with inverse primitive
`[r] -> [mathscr D^(-1)r]` in
`Dom mathscr D/(algebraic direct sum Dom D_l,n)`. Both inverse laws follow
coordinate by coordinate from the already proved inverses D_l,n. Thus no
class is deleted by the completion without its displayed primitive.

For a concrete nonzero class take a fixed original neighboring plaquette at
each regulator, `h_n=Q_l,n W_(p,n)`, and `r_n=2^(-n)h_n`.
Every h_n is nonzero: the two-link central flip preserving Omega and exterior
changes W_p, and the conditional density is everywhere positive. Also
`||h_n||<=2`, so r is square summable and has infinitely many nonzero
coordinates. Hence its class modulo finite support is nonzero. Its completed
primitive is `(2^(-n)D_l,n^(-1)h_n)_n`, and Z56 controls its tail.
The algebraic quotient's induced Hilbert seminorm vanishes because finite
support is dense; the exact quotient and primitive above retain the source
information behind that zero seminorm. This is an independently proved
application of [SZ] to the actual operator family.

## 11. Scope, verification, and the next original quantity

The zero-shift numerical certificate concerns the actual local observation
`(Omega, all exterior links)` at `xi=10^(-8)`, for every a>0 and L>=2.
It is supplied with an exterior-independent finite error, a second-order
log-vacuum remainder, and the exact comparison to the predecessor's
Omega-only observation. The all-coupling heat/conditional-kernel estimates
are evaluated on their separate explicit weak-coupling continuum path.
A physical continuum field and a uniform positive mass lower bound for the
complete physical Hilbert space have not been established.

The checker evaluates exact quaternion identities, original graph supports,
integer and rational constants, complex block identities, and intentionally
false formulas. It does not replace the written semigroup, elliptic-domain,
or limiting arguments by finite tests. Both ordinary and optimized Python
runs and their source-bound receipts are recorded separately.

The next original quantity is the outer effective response in Z52 on growing
retained observations, together with the full norm Z53 and the primitive
norm of the original physical gradient. The local zero-shift inverse and
its actual response are now available as proved inputs. Peer updates found
in this cycle are recorded with their actual reading scopes, without
assigning unexamined arithmetic constants to these Yang–Mills measures.

### Sources actually used

[YM] `KokunoYumeto/yang-mills-interacting-workbench`, main
`fab69fdc4ac197159b8e6ae8d73a82bde2b20d55`,
`yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md`
and `yang-mills/sources/ym_volume_uniform_astra_20260908/VOLUME_UNIFORM_LOCAL_VACUUM_ESTIMATES.md`;
original operator, domains, vacuum and local exterior decomposition.

[ALM] Preserved preceding delivery `yang_mills_actual_loop_moments.zip`,
original `RESEARCH_NOTE.md` and `verify.py`; Z3–5, Pauli identities and the
twelve-face calculation are reproduced here. The exact local byte identities
and replay are in this contribution's records. The complete twenty used
quaternion/Haar/graph/arithmetic blocks are included in `exact_algebra.py`
with their source-block hashes in `algebra-provenance.json`. The offline
package also retains the full preceding delivery; the Git checker requires
only files in its own directory.

[SZ] `KokunoYumeto/zeta-function-research-reader`, revision
`464a0d0c150ca9ed700335385d4892d18922b028`,
`formal/splitzero/DERIVED_MATHEMATICS.md`, sections 1–4,
blob `fe05d32ccd314daac7c59d225c9cac3d4c1bf3d3`, reconstruction and transported-class
kernel construction; the original minimum-section correction is also retained
in the OPR/observation-metric sources read by the preceding workbench cycle.
No new Lean replay is claimed.

[HK] A. Nowak, P. Sjögren, T. Z. Szarek, *Sharp estimates of the spherical heat
kernel*, arXiv:1802.09385v2, equations (1)–(4), and the original sphere measure
convention; J. Math. Pures Appl. 129 (2019), 23–33. The original PDF equations
on pages 2–3 were inspected. Time, measure and quaternion maps are Z6–8.
