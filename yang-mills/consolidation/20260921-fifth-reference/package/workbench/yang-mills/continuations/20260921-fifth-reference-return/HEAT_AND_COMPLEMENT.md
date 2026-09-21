# Fifth-reference heat bounds and the complete complementary physical space

21 September 2026. This note applies the completed fifth-reference correction in FIFTH_REFERENCE.md to the original Yang–Mills heat, plaquette moments and complementary minimization. The improvement comes from evaluating that source, not from changing a physical norm. It uses the unchanged exact heat coefficients through degree four and constructs a new box-independent analytic remainder. All exterior-volume, observation-rank and physical-time scopes are stated explicitly.

## H1. Complete coefficient generator and original mean

Retain F1--F42 of the companion, in particular kappa=2g^2/a, xi=1/(4g^4), rho=psi^2 and A=H-E0. Fix a complex radius r<alpha. The fifth construction gives a local analytic source v(zeta) and a drift D_v=2Gamma(v,.), satisfying

\[
\|D_vh\|_X\le\chi(r)\|Kh\|_X,\quad
\chi(r)=1-d_5(r)/3<1/2.
\tag{H1}
\]

Let X0 be the nonconstant physical Fourier space with norm sum ||A_j||1, and Y0 its domain sum c_j||A_j||1<infinity. Define the actual maps

\[
T=Q_HD_vK^{-1}:X_0\to X_0,\quad p=P_HD_vK^{-1}:X_0\to\mathbb C,
\quad S=(I-T)^{-1},\quad
\mu(F)=P_HF+pSQ_HF.
\tag{H2}
\]

The complete scalar-and-nonconstant output obeys |py|+||Ty||X<=chi||y||X. Thus ||S||<=1/(1-chi), ||mu||<=1, and |(mu-P_H)Q_HF|<=chi||Q_HF||X/(1-chi). The last bound and chi<=1/2 prove the full mean norm, using the additive original constant/nonconstant coefficient norm. The exact Poisson equation is

\[
(K-D_v)K^{-1}SQ_HF=F-\mu(F).
\tag{H3}
\]

This constructs the scalar as well as the primitive. Integration by parts against exp(2v) gives int exp(2v)F=mu(F)int exp(2v). The latter integral cannot vanish: a vanishing value would make the left side zero for every physical Fourier polynomial, whose uniform closure contains the conjugate of the nonzero smooth gauge-invariant exp(2v). Their paired integral would then be zero. Consequently

\[
\mu(F)=\frac{\int e^{2v}F\,dU}{\int e^{2v}\,dU}.
\tag{H4}
\]

On real coupling this is the original vacuum expectation. The complex formula keeps its full nonzero scalar denominator.

The coefficient operator L=(I-T)K on Y0 is closed, since I-T has a bounded inverse and K is closed. Finite Fourier polynomials give a dense domain. For h>0 the factorization of I+hL through I+hK has remaining factor I-hQ_HD_v(I+hK)^{-1}, whose norm difference from I is at most chi. It is therefore onto with bounded inverse. For f in Y0,

\[
\|(I+hL)f\|_X\ge\|f\|_X+h(1-\chi)\|Kf\|_X
\ge[1+3h(1-\chi)]\|f\|_X.
\tag{H5}
\]

Here the identity ||(I+hK)f||=||f||+h||Kf|| follows coefficient by coefficient. The same derivative estimate proves dissipativity after shifting by 3(1-chi); range surjectivity at a sufficiently large positive parameter follows from the displayed factorization. The Hille--Yosida/Lumer--Phillips generation theorem thus gives

\[
E(\tau)=e^{-\tau L},\qquad \|E(\tau)\|\le e^{-3(1-\chi)\tau}.
\tag{H6}
\]

Both the domain and actual range were verified, rather than inferring a semigroup bound from a single inverse. Analytic parameter dependence follows from the locally analytic resolvents and their exponential Euler powers: each power is a positive scalar gamma-time average of E, has the same contraction bound, and converges strongly by its mean and variance. Bounded weak holomorphic convergence, tested against every continuous linear functional, gives the analytic continuation on every smaller source disk.

The original full heat is

\[
\mathcal T(\tau)F=E(\tau)Q_HF+\mu(F)-\mu(E(\tau)Q_HF).
\tag{H7}
\]

It solves the original transformed equation K-D_v, preserves the actual mean, and on real coupling agrees with the physical Hilbert semigroup by uniqueness. The physical time map and inverse are tau=kappa t and t=tau/kappa.

## H2. New box-independent heat circle

For original marked faces define

\[
r_p=(W_p-\mu W_p)\psi,\quad
\widehat C_{pq}(\tau;\xi)=\langle r_p,e^{-\tau A/\kappa}r_q\rangle.
\tag{H8}
\]

At complex parameter use its bilinear analytic continuation mu[(T(tau)Wp-mu Wp)Wq]. For arbitrary original face coefficients |z_q|<=1 put G_z=sum_q z_qWq. At most four faces meet an edge. Their fundamental coefficient norm 8 and edge spin 1/2 give

\[
\|\Gamma(h,G_z)\|_X\le32\|Kh\|_X.
\tag{H9}
\]

For the original Haar scalar there is a sharper exact selection rule. A physical representation block with spin 1/2 on one elementary face and zero elsewhere is the one-dimensional line C Wp. Its Casimir is 3, coefficient norm is 8|a_p|, and Haar norm of Wp is 1. Integration by parts and Haar orthogonality therefore give

\[
|P_H\Gamma(h,G_z)|\le\frac18\|Kh\|_X.
\tag{H10}
\]

Take h_tau=K^{-1}S E(tau)Wp. Equation H3, followed by integration by parts in H4, proves

\[
\sum_qz_q\widehat C_{pq}(\tau)=\mu\Gamma(h_\tau,G_z),\quad
\|Kh_\tau\|_X\le\frac8{1-\chi}e^{-3(1-\chi)\tau}.
\]

Retaining the Haar contribution (H10) and the full returned-mean contribution in H2 proves

\[
\boxed{\|\widehat C(\tau;\zeta)\|_{\rm row}
\le\frac{1+255\chi}{(1-\chi)^2}e^{-3(1-\chi)\tau}.}
\tag{H11}
\]

The row norm is max_p sum_q|C_pq|, obtained exactly by maximizing over the phases z_q. Transpose symmetry extends from real coupling by analytic continuation, so columns have the same bound. No face count M enters this estimate.

The exact source calculation F28--F35 verifies

\[
\boxed{R=1/55<\alpha,\quad d_5(R)>13/8,\quad
\chi(R)<11/24,\quad C=\frac{1+255(11/24)}{(1-11/24)^2}
=\frac{67896}{169}.}
\tag{H12}
\]

This circle strictly exceeds the saved fourth-reference endpoint 0.018104972231644127076, and the preceding volume-heat radius 3/256. The inequalities are certified by integer-square and rational polynomial bounds in physical_return.json.

The original link-center map U_(n,i) -> (-1)^(sum_(j<i)n_j) U_(n,i) preserves Haar, K and the full gauge action and sends every Wp to -Wp. Therefore the homogeneous connected two-mark heat is even. Applying Cauchy's formula to (H11) on the same circle gives

\[
\boxed{
\|\widehat C(\tau;\xi)-C_0(\tau)-\xi^2C_2(\tau)-\xi^4C_4(\tau)\|_{\rm row}
\le\frac{67896}{169}e^{-13\tau/8}
\frac{(55|\xi|)^6}{1-(55|\xi|)^2},\quad |\xi|<1/55.}
\tag{H13}
\]

This holds for every original L>=2 and every tau>=0. C0,C2,C4 are the complete unchanged inherited heat coefficient matrices; the original source/heat recurrence fixes them uniquely. The new result evaluates an infinite tail beyond those coefficients; it does not relabel a new finite heat coefficient as calculated.

## H3. Original moments and a signed leakage remainder

Let R_col have the original columns r_p and set Phi=kappa A^{-1}R_col. Keep

\[
G_0=R_{\rm col}^*R_{\rm col},\quad
G_1=\kappa R_{\rm col}^*A^{-1}R_{\rm col},\quad
G_2=\Phi^*\Phi,\quad
E=\Phi^*A\Phi=\kappa G_1,\quad
K_o=\kappa^{-1}R_{\rm col}^*AR_{\rm col}.
\tag{H14}
\]

The spectral theorem gives G_k=int_0^infinity tau^(k-1)Chat(tau)d tau/(k-1)! for k>=1. Thus (H13) has moment prefactor C/d^k, d=13/8, retaining every power of kappa in H14. G0 uses tau=0.

The complete kinetic function is <Gamma(Wp,Wq)>rho. A diagonal has coefficient norm at most30, from Gamma(Wp,Wp)=4-Wp^2=3-chi_1 and ||chi_1||X=27. An adjacent off-diagonal has norm at most48. Every face has at most twelve adjacent faces; every other entry is zero. Since ||mu||<=1, its full complex row bound is 606. It consequently has the same even tail factor, with prefactor606.

The actual nonnegative leakage trial is

\[
J=(R_{\rm col}-3\Phi)^*(R_{\rm col}-3\Phi)=G_0-6G_1+9G_2.
\tag{H15}
\]

Keep the sign of the time weight before estimating its remainder:

\[
J=\widehat C(0)+\int_0^\infty(9\tau-6)\widehat C(\tau)\,d\tau.
\tag{H16}
\]

Splitting the scalar integral at tau=2/3 gives the exact expression

\[
1+\int_0^\infty|9\tau-6|e^{-d\tau}d\tau
=1+\frac6d-\frac9{d^2}+\frac{18}{d^2}e^{-2d/3}.
\tag{H17}
\]

For d=13/8, the even 120th Taylor sum of exp(-13/12) is less than339/1000. Taylor's integral remainder is negative at that order, giving a rigorous upper bound for the exponential. Hence the complete leakage-tail prefactor is at most

\[
\boxed{C_J=C\left[1+\frac6d-\frac9{d^2}+\frac{18(339/1000)}{d^2}\right]
=\frac{5156090136}{3570125}.}
\tag{H18}
\]

This is smaller than C(1+6/d+9/d^2). All signed time weights and mixed moment entries remain in H15--H18.

The complete inherited original-support coefficient bounds are

|Matrix|degree two row bound|degree four row bound|
|---|---:|---:|
|G0|149/468|2361994073/4691494080|
|G1|97/468|376882691/938298816|
|G2|73313/657072|982069718963833/3919180324550400|
|Ko|187/468|586668421/1563831360|
|J|6779/73008|152338674005989/435464480505600|

Their actual absolute-motif assembly retains all 199 original supports and559 marked contributions in the preceding volume directory. Boundary rows use subsets; no claim that a signed bulk row is the worst boundary row is used.

For x=xi and u=(55x)^6/[1-(55x)^2], define the explicit widths

\[
\begin{split}
w_k&=B_{k,2}x^2+B_{k,4}x^4+(C/d^k)u\quad(k=0,1,2),\\
w_K&=B_{K,2}x^2+B_{K,4}x^4+606u,\\
\beta&=B_{J,2}x^2+B_{J,4}x^4+C_Ju.
\end{split}\tag{H19}
\]

The original real symmetric matrices therefore satisfy

\[
\|G_k-3^{-k}I\|\le w_k,\quad\|K_o-3I\|\le w_K,
\qquad0\preceq J\preceq\beta I.
\tag{H20}
\]

The operator estimate follows from both row and column bounds. Each width increases with x. Their exact rational values at the original coupling benchmarks, with all square-root enclosures for d5, are in generated/physical_return.json.

## H4. Whole physical observation and complementary coupling

Put l_k=3^(-k)-w_k, u_k=3^(-k)+w_k for k=0,1,2, and u_K=3+w_K. Each benchmark below has l_k>0. Thus R_col and Phi are injective and have closed ranges, with the original Grams H14. The actual state projection is

\[
P_R=R_{\rm col}G_0^{-1}R_{\rm col}^*,\quad
\|P_R\Phi c\|^2=c^*G_1G_0^{-1}G_1c.
\]

Consequently

\[
\frac{\|P_R\Phi c\|^2}{\|\Phi c\|^2}
\ge\frac{l_1^2}{u_0u_2}\quad(c\ne0).
\tag{H21}
\]

This is observation of the actual inverse-energy vectors, with both original state metrics retained.

For the complete physical complement define

\[
P=\Phi G_2^{-1}\Phi^*,\quad Q=I-P,\quad B_\Phi=QR_{\rm col}.
\tag{H22}
\]

Completing the original state-norm square gives

\[
B_\Phi^*B_\Phi=G_0-G_1G_2^{-1}G_1\preceq J\preceq\beta I.
\tag{H23}
\]

The comparison with J follows by inserting the specific admissible coefficient3c into the same state minimum. Every centered physical form-domain vector has the decomposition Phi c+h, h in QH0. Its complete pairing and energy are

\[
\begin{split}
\|\Phi c+h\|^2&=c^*G_2c+\|h\|^2,\\
q_A(\Phi c+h)&=\kappa c^*G_1c
+2\kappa\operatorname{Re}\langle B_\Phi c,h\rangle+q_A(h).
\end{split}\tag{H24}
\]

Take d_ph as any displayed rational lower endpoint for d5(x); then A>=kappa d_ph on H0 by F37. The product A Phi=kappa R_col is bounded. Hence AP is bounded, PA has its bounded adjoint extension, and QAP+PAQ is bounded self-adjoint. Subtraction of this operator from A leaves a self-adjoint block-diagonal operator on Dom(A). Its Q restriction is

\[
D_Q=QAQ,\quad\operatorname{Dom}D_Q=\operatorname{Dom}A\cap Q\mathcal H_0,
\quad D_Q\succeq\kappa d_{\rm ph}I.
\tag{H25}
\]

This proves its operator domain and inverse on the complete complementary space, rather than just a trial subspace. Direct substitution minimizes H24 at

\[
h_{\min}=-\kappa D_Q^{-1}B_\Phi c.
\]

The restored columns and metrics are exactly

\[
\begin{split}
\Phi_{\rm full}&=\Phi-\kappa D_Q^{-1}B_\Phi,\\
E_{\rm full}&=\kappa G_1-\kappa^2B_\Phi^*D_Q^{-1}B_\Phi,\\
G_{\rm full}&=G_2+\kappa^2B_\Phi^*D_Q^{-2}B_\Phi.
\end{split}\tag{H26}
\]

Define the explicit positive numbers

\[
\eta_E=\frac{\beta}{d_{\rm ph}l_1},\quad
\eta_G=\frac{\beta}{d_{\rm ph}^2l_2}.
\tag{H27}
\]

Then

\[
(1-\eta_E)E\preceq E_{\rm full}\preceq E,\qquad
G_2\preceq G_{\rm full}\preceq(1+\eta_G)G_2.
\tag{H28}
\]

The full mixed form H24 also lies between (1-sqrt(eta_E)) and (1+sqrt(eta_E)) times kappa c*G1c+q_A(h), by Cauchy--Schwarz in the actual D_Q energy. The cross term has been bounded, not discarded.

The state minimum section P_R Phi differs from the energy minimum section Phi by h_R=(I-P_R)Phi. The original equation A Phi=kappa R_col gives q_A(Phi c,h_Rd)=0. Expanding both mixed terms gives

\[
h_R^*Ah_R=\kappa[G_1G_0^{-1}K_oG_0^{-1}G_1-G_1]
\preceq\left(\frac{u_1u_K}{l_0^2}-1\right)E.
\tag{H29}
\]

## H5. Explicit improved domains

The rational evaluation of H19--H29 proves, simultaneously for all original boxes L>=2 and a>0:

|Original coupling|Observed state fraction exceeds|Complementary energy loss below|Restored state increase below|
|---|---:|---:|---:|
|g²>=10|977/1000|11/1000|12/1000|
|g²>=12|997/1000|12/10000|12/10000|
|g²>=25/2|998/1000|1/1000|1/1000|
|g²>=13|999/1000|1/2000|1/2000|
|g²>=16|9999/10000|1/25000|1/25000|

“Loss below eta” in this table means E_full>(1-eta)E; “increase below eta” means G_full<(1+eta)G2. All identities and quotients are the original H14,H26, not substituted metrics. At g²=13, the exact diagnostic values of the three respective bounds are approximately0.99904459483,0.00043585425,0.00045023706; the conclusions in the table use strict rational tests. For g²>=16 the corresponding original section-energy change H29 is below1/20000.

For example at g²>=13 the full original Gram bounds include

\[
\|G_0-I\|<119\cdot10^{-6},\quad
\|G_1-I/3\|<73\cdot10^{-6},\quad
\|G_2-I/9\|<45\cdot10^{-6},\quad
\|K_o-3I\|<178\cdot10^{-6}.
\tag{H30}
\]

The physical gap used there has d_ph=29047/10000. Every estimate for larger g² follows because xi decreases, the widths increase with xi, and d5 decreases with xi.

## H6. Support quotients, heat horizon, and spatial limit

For original face sets F subset G, keep V_F=Phi(C^F), U_F=A V_F. The cochain windows are V_F --A--> H0 --0-->0. The exact transported-kernel isomorphism is

\[
V_G/V_F\longrightarrow\ker[\mathcal H_0/U_F\to\mathcal H_0/U_G],
\qquad[h]\mapsto[Ah].
\tag{H31}
\]

Its inverse is induced by the actual A^{-1}; changing a representative by U_F changes its inverse by V_F. For J=G minus F, its original energy quotient is the attained minimum

\[
Q_E(F,G)=E_{JJ}-E_{JF}E_{FF}^{-1}E_{FJ},\qquad
c_F^{\min}=-E_{FF}^{-1}E_{FJ}c_J.
\tag{H32}
\]

Every mixed block and the removed primitive remain in the formula. The finite-time columns

\[
\Phi_T=(I-e^{-TA})\Phi=\kappa\int_0^Te^{-tA}R_{\rm col}\,dt
\]

satisfy A Phi_T=kappa R_col-kappa e^{-TA}R_col. With epsilon=e^(-kappa d_ph T), the original state and energy Grams lie between (1-epsilon)^2 and1 times the original Grams. This follows spectrally from A>=kappa d_ph and commutation with exp(-TA). Taking infima over the identical coefficient fibers in H32 preserves these inequalities.

For a prescribed finite signed determinant return sum_j a_j logdet Q_j of total absolute rank B=sum_j|a_j|rank Q_j, the error is at most2B[-log(1-epsilon)]. A finite physical choice is

\[
\boxed{T=(\kappa d_{\rm ph})^{-1}\log(1+2B/\eta),}
\tag{H33}
\]

which gives error<=eta by -log(1-epsilon)<=epsilon/(1-epsilon). Both rank and physical time factors are explicit.

The same construction also supplies the spatial limit at fixed a,g with xi<1/55. Every original Taylor coefficient of v has a connected original face support, and a degree-n marked heat coefficient depends only on its finite n-neighborhood. This is proved by the actual source/heat recurrences: a derivative product joins supports only at an original common edge; K inversion and its unperturbed resolvent preserve link support. The scalar and disconnected terms remain until the connected subtraction. On disjoint active components the original compact-group operator and positive vacuum factor, giving the same zero coefficients.

On two boxes containing the same N-neighborhood of the marks, all heat coefficients through N coincide. Equation H13 consequently gives

\[
|\widehat C_L-\widehat C_{L'}|
\le2Ce^{-d\tau}\frac{(55|\xi|)^{2(\lfloor N/2\rfloor+1)}}{1-(55|\xi|)^2}.
\tag{H34}
\]

The mean H2 and full heat H7 have analogous local Taylor tails. They converge on cylinder Fourier polynomials, and for real coupling their actual Markov contractions extend convergence to the uniform closure. Positivity, unit mass, semigroup composition and symmetry pass by cylinder approximation. Their unique invariant physical state follows by integrating the uniform decay of H7 on centered cylinders. This is uniqueness on the gauge-invariant observable algebra; the original vertex Haar average supplies its gauge-invariant probability lift.

The resulting self-adjoint generator on L2(mu)_phys has its actual cylinder domain and A_infinity F=kappa(K-D_v,infinity)F: pass the finite semigroup integral equation using the absolute local derivative tails. The finite gap passes by L2 density, yielding A_infinity>=kappa d5(xi) on the centered space. The moment matrices are bounded positive operators on the original l2 infinite face coefficient space, because the row estimates and spatial tails give strong convergence on finite coefficient vectors, then on all l2. Their positive lower bounds remain.

Consequently R_col and Phi extend as closed-range maps and A_infinity Phi=kappa R_col. In particular A_infinity P_Phi is bounded even for this infinite family. The same bounded-off-diagonal domain argument in H25, and the complete H26 minimization, therefore hold for the full infinite complementary physical space. The benchmark table H5 carries over at fixed spacing and coupling.

## H7. Continuum scope and next original quantity

The standing simultaneous path keeps a_n=a0*2^(-n), g_n²=1/c_n, c_n=g0^(-2)+beta*n*log2 and xi_n=c_n²/4. Its exact inclusion in the fifth-source domain is c_n<=2sqrt(alpha); its inclusion in this heat circle is c_n<2/sqrt(55). For beta>0 it eventually leaves both. No positive finite continuum mass or nontrivial smooth four-dimensional field is concluded from these fixed-spacing estimates.

This tranche completes the selected fifth-reference correction and its return to the full physical complement. Merely re-centering the elementary norm inequality reproduces its old endpoint, as the preserved ROUTE_ASSESSMENT calculation proves. A further extension has to use actual additional coefficient or signed inverse information. The concrete next candidate is the same-support linearized action J5 and its preconditioned residual, using the now stored complete edge-channel coefficients; any replacement of the inverse must retain its exact residual operator. The missing sixth-source catalogue remains missing in the delivered source chain and has not been declared reconstructed by these estimates.

## H8. Evidence and attribution

All old heat coefficients and absolute support sums are preserved byte-for-byte. New algebra evaluates the fifth reference; new rational calculations verify its root, heat circle, signed time integral and the benchmark matrix inequalities. The written source-domain and semigroup argument is supplied in F1--F42 and H1--H34; exact finite checks are not represented as formal proof of the analytic passage.

G. Lumer and R. S. Phillips, Dissipative operators in a Banach space, Pacific J. Math.11 (1961),679--698, Theorem3.1, is used only after the domain, dissipativity and range checks H5. P. Eymard's compact Fourier algebra and Schuette--Zheng--Hamer's exp-S/Casimir construction are credited as in the companion. This contribution is on the original Yang–Mills objects. No arithmetic Gamma measure, RH root packet, or Riemann activation asymptotic is imported.
