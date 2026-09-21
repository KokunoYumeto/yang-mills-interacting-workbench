# The actual second vacuum source and continuation beyond the first endpoint

15 September 2026. This calculation uses the actual plaquette pair channels B12–14 to evaluate the second logarithmic-vacuum source before estimating higher orders. It improves the source endpoint further, while every original coefficient, relation label, Hamiltonian term, physical Gram and energy unit stays fixed. The previous estimates remain valid on their stated domains. R10–14 below supply the final enlarged finite- and infinite-volume domains of this continuation.

## R1. Evaluate the entire second source, including its zero coefficients

Use S=sum_p W_p and v_[1]=S/3. The original Casimir product rule gives

\[
 \sum_i(X_iS)^2=3S^2-\tfrac12K_LS^2,
 \qquad
 v_{[2]}=\left(\tfrac13K_L^{-1}-\tfrac1{18}I\right)Q_HS^2.
                                                               \tag{R1}
\]

The inverse acts only on the original nonconstant Haar coefficients. The scalar removed here remains in G20–21, whose second ground-energy term is exactly -kappa |P_L| xi^2/3.

For a single plaquette, W_p^2=1+chi_1(Omega_p), and the nonconstant term has Casimir 8. For distinct faces without a shared edge, the product has Casimir 6, so its coefficient in R1 is exactly zero. For an unordered adjacent pair {p,q}, let P_0 and P_1 be its actual shared-edge spin-zero and spin-one projections from B13. Their original Casimirs are 9/2 and 13/2. Substitution into R1 proves

\[
 \boxed{
 v_{[2]}=-\frac1{72}\sum_p\chi_1(\Omega_p)
   +\sum_{\{p,q\}:p\sim q}
      \left[\frac1{27}P_0(W_pW_q)-\frac1{117}P_1(W_pW_q)\right].}
                                                               \tag{R2}
\]

The factor two for an unordered pair comes from the two ordered terms of S^2. The labels remain the original plaquette or pair union. In particular P_0 has six active links but retains its seven-link union label. Every disjoint-pair coefficient is explicitly zero at its original union; it is not relabelled as an absent source.

## R2. Trace norms in the original link orientations

For a simple closed loop of length ell in the original positively oriented cubic links, let t be the number of local maxima of height x_1+x_2+x_3 around the loop. It also has exactly t local minima and ell-2t other vertices. At a maximum or minimum the original fundamental index contraction is the SU(2) alternating two-index vector, of Euclidean norm sqrt(2); at the other vertices it is a two-dimensional identity contraction. After separate permutations of the original row and column tensor indices, the Fourier coefficient is exactly a tensor product of those rectangular contractions. Row and column permutations preserve its singular values. Tensor-product singular values therefore give

\[
 \|A_{\rm loop}\|_1=(\sqrt2)^{2t}2^{\ell-2t}
                    =2^{\ell-t}\le2^{\ell-1}.         \tag{R3}
\]

The height cannot be strictly increasing around a closed loop, so t>=1. This also proves the original coefficient's full rank and singular values: rank 2^(ell-2t), with each nonzero singular value 2^t. These are original oriented coefficients; inversion of a single link is not assumed to preserve a tensor matrix's trace norm.

For the original spin-one plaquette the same four contractions have dimension three, with one maximum and one minimum. Its norm is exactly 3^3=27. Equivalently, the literal G14 matrix with indices in {0,1,2}, complements 2-i, and the same signs has nine rank-one three-by-three blocks. Each nonzero singular value is three.

For an adjacent pair, P_0(W_pW_q)=Tr(Omega_6)/2 on the actual simple six-link boundary. Equation R3 proves

\[
 x:=\|A(P_0(W_pW_q))\|_1\le16,
 \quad x+y\le64,\quad y:=\|A(P_1(W_pW_q))\|_1.          \tag{R4}
\]

The second bound is the full coefficient-product inequality G11 applied to the two original norm-eight plaquettes, including both irreducible outputs. No norm is assigned to P_1 from its Haar mass alone.

In the unchanged Casimir-weighted source G9, an adjacent pair's complete R2 contribution is at most

\[
 (9/2)x/27+(13/2)y/117
       =x/6+y/18\le16/3.                              \tag{R5}
\]

A spin-one self contribution is at most 8*27/72=3. For an anchored edge e, write r_e<=4 for its original face incidence. Counting each adjacent pair containing a face at e and subtracting its exact double count when both faces contain e gives

\[
 \#\{\{p,q\}:p\sim q,\ e\in\partial p\cup\partial q\}
 =\sum_{p\ni e}d_p-\binom{r_e}{2}
 \le12r_e-\binom{r_e}{2}\le42.
\]

Together with at most four self terms this proves the volume-independent bound on the ACTUAL second source:

\[
 \boxed{\|v_{[2]}\|_{\rm loc,1}\le4\cdot3+42\cdot16/3=236.} 
                                                               \tag{R6}
\]

The earlier purely bilinear estimate was (2/3)*32^2=2048/3. R6 uses the evaluated original pair channels and their complete coefficient norms.

## R3. A larger convergent source, with an explicit endpoint tail

Set a_1=32, a_2=236, and for n>=3 define the positive numbers

\[
 a_n=\frac23\sum_{i=1}^{n-1}a_i a_{n-i}.
\]

G13 and R6 prove ||v_[n]||loc<=a_n by induction, on the same original support-labelled coefficients. Their generating function r_2=sum_(n>=1)a_n xi^n satisfies

\[
 r_2=32\xi+236\xi^2+\frac23(r_2^2-1024\xi^2),
\]
\[
 \boxed{
 P_2(\xi)=1-\frac{256}{3}\xi+\frac{10720}{9}\xi^2,
 \qquad r_2(\xi)=\frac34(1-\sqrt{P_2(\xi)}),
 \qquad \epsilon_2=\frac23r_2.}                         \tag{R7}
\]

The branch has value zero at xi=0. Its positive coefficient recurrence proves the absolute majorant before any endpoint is taken. The first positive root is

\[
 \alpha=\frac3{4(32+\sqrt{354})},\qquad
 \beta_2=\frac3{4(32-\sqrt{354})},\qquad
 P_2=(1-\xi/\alpha)(1-\xi/\beta_2).                    \tag{R8}
\]

Write gamma=alpha/beta_2, so 0<gamma<1. In sqrt(1-z)=1-sum_(n>=1)b_n z^n the numbers b_n=C_(n-1)/(2*4^(n-1)) are positive. Multiplication of the two square-root series gives

\[
 0\le a_n\alpha^n
 \le\frac34 b_n(1+\gamma^n).
\]

The subtracted convolution has positive terms; the lower sign follows independently from the a_n recurrence. The exact binomial tail sum_(n>P)b_n=binom(2P,P)/4^P, already proved in G19, yields

\[
 \boxed{
 \sum_{n>P}a_n\xi^n
 \le\frac34(\xi/\alpha)^{P+1}(1+\gamma^{P+1})
                 \frac{\binom{2P}{P}}{4^P}
 \le\frac34(\xi/\alpha)^{P+1}
                    \frac{1+\gamma^{P+1}}{\sqrt{P+1}}}
 \quad(0\le\xi\le\alpha).                            \tag{R9}
\]

Thus the complete original source converges absolutely also at alpha. Monotone convergence of its positive majorant gives r_2(alpha)=3/4 and epsilon_2(alpha)=1/2. The same finite-box derivative summability and positive eigenfunction argument G20–21 identify the sum with the actual vacuum, retaining its scalar. On the common earlier domain both constructions sum identical original coefficients; their identity map and its inverse are literally the identity coefficient by coefficient.

## R4. Return to the complete physical spectrum and the unique volume limit

The original drift bound G23 now has r_2 in place of r, because its proof uses the same coefficient sum. Apply G24–27 to every actual physical eigenfunction, then the full compact spectral resolution. This proves on the closed enlarged domain

\[
 \boxed{
 \Delta_L\ge\frac{3\kappa}{2}(1+\sqrt{P_2(\xi)}),
 \quad 0<\xi\le\alpha,
 \quad g^2\ge\sqrt{(32+\sqrt{354})/3}.}                 \tag{R10}
\]

There is no dependence on L. The full scalar bound is one quarter of R10. In original physical units R10 is

\[
 \Delta_L\ge\frac{3g^2}{a}
       \left(1+\sqrt{1-\frac{64}{3g^4}+\frac{670}{9g^8}}\right).
                                                               \tag{R11}
\]

At the rational benchmark g^2>=17/4,

\[
 \Delta_L\ge\frac{3\kappa}{2}
           \left(1+\sqrt{35401/751689}\right)>1.8255\kappa.
                                                               \tag{R12}
\]

For xi<alpha the complete drift row sum is bounded by

\[
 \sum_{n\ge1}n a_n\xi^n
   =\xi r_2'(\xi)
   =\frac{32\xi-(2680/3)\xi^2}{\sqrt{P_2(\xi)}}<\infty.
\]

Coefficient compatibility and this row sum give exactly the finite-dynamics comparison S13–19 on that domain. The direct finite-semigroup proof S24–28 uses only G23 and now proves the full uniform mixing estimate with epsilon_2. In particular the whole vacuum-measure sequence converges by S29–30; a conditional-influence row smaller than one is not used in this return.

The actual coupling difference is bounded by r_2(eta)-r_2(xi), by the positive recurrence. The same complete Duhamel formula S31–33 consequently gives

\[
 \sup_{t\ge0}\|T_{L,\eta}(t)F-T_{L,\xi}(t)F\|_\infty
 \le\frac{\epsilon_2(\eta)-\epsilon_2(\xi)}{1-\epsilon_2(\xi)}
          \|Q_HF\|_{X_0},\qquad0\le\xi\le\eta\le\alpha. 
                                                               \tag{R13}
\]

At eta=alpha this ratio is sqrt(P_2(xi))/(1+sqrt(P_2(xi))) and tends to zero. Inserting an interior coupling between two endpoint finite boxes, as in S13, proves the whole endpoint dynamics limit. Equation R9 supplies its actual drift convergence; no finite derivative row is assigned at alpha. Uniform mixing makes its limiting vacuum the unique invariant probability of this constructed semigroup, and finite reversibility and physical cylinder density give

\[
 \boxed{A_\infty|_{L^2_{\rm phys}(\nu)\cap1^\perp}
       \ge\frac{3\kappa}{2}(1+\sqrt{P_2(\xi)}),
       \qquad0<\xi\le\alpha.}                         \tag{R14}
\]

The raw physical primitive G30 and physical conditional inverse G31 receive the same stronger bound. The original response pairing and minimum-section correction remain unchanged. The complete band coefficient and its analytic error B10–32 remain valid on their already stated domains; no further band radius is assigned here.

## R5. Actual continuation scope

The final endpoint is approximately g^2=4.1156161030. The old g^2>=15 bound, the first gauge-native g^2>=8/sqrt(3) bound, and R10 refer to the same original Hamiltonian; the explicit coefficient inequalities and their physical return prove the successive gains. The construction at the old source-majorant endpoint is continued by the actual second source rather than by declaring that endpoint a physical singularity.

On the retained path g_n^2=1/c_n, c_n=g_0^-2+beta n log2, the final domain is c_n^2<=3(32-sqrt(354))/670. This follows by rationalizing 3/(32+sqrt(354)); both physical parameters stay those of S31. For beta>0 the path eventually leaves this domain. A nontrivial four-dimensional continuum field and a finite positive continuum mass along that path remain unevaluated.

The next selected source calculation is the actual order-three connected coefficient and full linearized remainder at xi v_[1]+xi^2 v_[2], with its original union labels. The present R2, R6, R9 and R14 are completed inputs to that calculation, not presumed estimates for it.

## R6. Return the coupling comparison to both original physical coefficients

For positive kappa_1,kappa_2 and 0<xi_1,xi_2<=alpha, set
xi_-=min(xi_1,xi_2), xi_+=max(xi_1,xi_2), kappa_+=max(kappa_1,kappa_2),
and e_-=epsilon_2(xi_-), e_+=epsilon_2(xi_+). The full physical inverse
is always g_j^2=1/(2sqrt(xi_j)), a_j=1/(kappa_j sqrt(xi_j)).
The actual vacuum density depends on xi_j; its dependence follows directly
from G20–21, whose energy scalar retains its factor kappa_j.

At one fixed xi the original generators satisfy

\[
 \mathcal A_{\kappa_2,\xi}-\mathcal A_{\kappa_1,\xi}
  =(\kappa_2-\kappa_1)
       \left[K_L-2\sum_i(X_iv_L(\xi))X_i\right].        \tag{R15}
\]

On the nonconstant evolved coefficient y, the full supremum norm of the
bracketed expression is at most (1+epsilon_2(xi))||y||Y. Duhamel's formula,
Markov supremum contraction, and S26 applied to the evolution with kappa_+
therefore bound the integrated coefficient change by
|kappa_2-kappa_1|(1+epsilon_2)/(kappa_+(1-epsilon_2))||Q_HF||X.
Insert the common intermediate coupling xi_- and use R13 for the other
change. This proves the explicit full-parameter estimate

\[
 \boxed{
 \sup_{t\ge0}\|T_{L,\kappa_2,\xi_2}(t)F
                 -T_{L,\kappa_1,\xi_1}(t)F\|_\infty
 \le\left[
      \frac{e_+-e_-}{1-e_-}
      +\frac{|\kappa_2-\kappa_1|}{\kappa_+}
                  \frac{1+e_-}{1-e_-}
      \right]\|Q_HF\|_{X_0}.}                         \tag{R16}
\]

The two evolutions use the same original physical time t. The result holds
for the constructed infinite-volume semigroups by their proved uniform
convergence. All four physical parameters are recovered by the displayed
inverse maps. This comparison has the exact domain R10; it does not assign
itself to the unproved later portion of the running continuum path.
