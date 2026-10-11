# Both original-energy roots and the retained source-zero covariance

This note proves lower and upper source-zero tails around the two roots of the actual local energy equation. It derives actual negative moments and then evaluates the inverse-multiplier equation, retaining local kinetic, outside and crossing energies. The centered covariance is calculated with its exact signed retained-energy contraction. The new bounds do not identify the actual mean with either root.

## 1. The original objects and their finite-regulator identities

The vertices are \(z\in\{0,\ldots,m\}^3\), \(m=2L\); positive edges have both endpoints in this set. For \(d<e\), the face word, trace, scalar deficit, metric, and Hamiltonian are
\[
\begin{gathered}
U_p=U_d(z)U_e(z+e_d)U_d(z+e_e)^{-1}U_e(z)^{-1},\qquad
W_p=\operatorname{Tr}U_p,\qquad D_p=2-W_p,\\
T_\alpha=-i\sigma_\alpha/2,\qquad
\Delta=\sum_{e,\alpha}X_{e,\alpha}^2,\quad K=-\Delta,\quad
\Gamma(G,H)=\sum_{e,\alpha}X_{e,\alpha}G\,X_{e,\alpha}H,\\
\kappa=2g^2/a,\qquad b=1/(2g^2a),\qquad
H=\kappa K+b\sum_pD_p=\kappa K+2bM-b\sum_pW_p,\\
N=3m(m+1)^2,\qquad M=3m^2(m+1).
\end{gathered}\tag{LR1}
\]
The metric on each \(\mathrm{SU}(2)\) is the radius-two metric. Product Haar has mass one. All original vertex gauge constraints, including boundary vertices, remain imposed. The smooth positive unit lowest eigenfunction of the full compact operator is \(\psi\), and
\[
H\psi=E_0\psi,\qquad w=\log\psi,\qquad d\mu=\psi^2dU.
\tag{LR2}
\]
The ground transform is obtained by expanding derivatives and using the ground equation:
\[
\langle G\psi,(H-E_0)G\psi\rangle
 =\kappa\mu\Gamma(G,\overline G),\qquad
2\mu\Gamma(w,G)=-\mu\Delta G.
\tag{LR3}
\]
It proves uniqueness of the positive unit ground vector, because any second ground vector divided by \(\psi\) has zero gradient on the connected configuration space. Every original gauge transformation preserves the operator, metric, Haar measure and positivity, hence fixes \(\psi\). The full ground energy is therefore the physical ground energy; no product decomposition of the physical Hilbert space is assumed.

For the original real compactly supported continuous \(f\), retain all three orientations and centers
\[
\begin{gathered}
x_p=o+a(z-L\mathbf1+(e_d+e_e)/2),\quad f_p=f(x_p),\quad
F=\|f\|_\infty,\quad A_1=\sum_p|f_p|,\\
C_f=a\sum_pf_pD_p,\quad
Y=\sum_p|f_p|D_p,\quad d=\mu Y,\quad m_f=\mu C_f,\\
Y_+=\sum_{f_p>0}f_pD_p,\quad Y_-=\sum_{f_p<0}(-f_p)D_p,\quad
C_f=a(Y_+-Y_-),\quad Y=Y_++Y_-.
\end{gathered}\tag{LR4}
\]
The case \(A_1=0\) has \(Y=C_f=0\). Assume \(A_1>0\), so \(F>0\). Every displayed quantity is evaluated at source zero.

Let \(Q=v+\{0,\ldots,q\}^3\) contain all edges of every face with nonzero sampled coefficient. Inside edges have both endpoints in \(Q\); inside faces use four inside edges. Define
\[
\begin{gathered}
N_Q=3q(q+1)^2,\quad M_Q=3q^2(q+1),\quad
\eta_Q=\sum_{\ell=1}^3
[\mathbf1_{\{v_\ell>0\}}+\mathbf1_{\{v_\ell+q<m\}}],\\
C_Q=2q(q+1)\eta_Q,\qquad
W_Q=\sum_{p\ \mathrm{inside}}D_p,\qquad
Z_Q=|\nabla_Qw|^2,\\
H=\kappa K_Q+bW_Q+H_{\rm out}+bW_\times,\qquad
H_{\rm out}\ge E_{\rm out}I,\qquad E_Q=E_0-E_{\rm out}.
\end{gathered}\tag{LR5}
\]
A mixed face has one inside edge: two adjacent inside edges force its four vertices into the interval product \(Q\), and two opposite inside edges already contain the four vertices. The crossing count is thus the stated exact \(C_Q\). The inside, outside and mixed scalar potential terms are \(2bM_Q\), \(2b(M-M_Q-C_Q)\), and \(2bC_Q\).

For completeness, the local energy comparison and its constants are as follows:
\[
\begin{gathered}
0\le E_Q\le b\Lambda_Q,\quad
\Lambda_Q=\min\{2M_Q,6g^2\sqrt{N_QM_Q}\}+2C_Q,\\
\kappa\mu Z_Q+b\mu W_Q\le E_Q,\quad
\alpha=\kappa/b=4(g^2)^2=\kappa^2a^2,\quad
e=FE_Q/b\le\Lambda_f:=F\Lambda_Q.
\end{gathered}\tag{LR6}
\]
Here is a proof of the upper comparison, so its boundary contribution is not an unproved input. The positive outside ground is invariant under every restricted original vertex gauge action. Starting a crossing face at its inside edge leaves an outside three-edge path with distinct endpoints; the central gauge element \(-I\) at one endpoint negates its matrix expectation. Thus an inside/outside tensor comparison has crossing energy exactly \(2bC_Q\). For an inside link write \(x=\operatorname{Tr}U/2\), \(h_t=Z_t^{-1/2}e^{tx}\), \(Z_t=\int e^{2tx}dU\), and \(q_t=\int xh_t^2dU\). The radius-two identities \(\Gamma(x)=(1-x^2)/4\), \(\Delta x=-3x/4\), give kinetic energy \(3\kappa tq_t/8\). The Haar marginal is \((2/\pi)\sqrt{1-x^2}\,dx\). With \(z=1-x\), its tilted density is proportional to \(e^{-2tz}z^{1/2}\sqrt{2-z}\mathbf1_{[0,2]}\). The extra factor relative to the gamma density \(e^{-2tz}z^{1/2}\) is decreasing. Its covariance with \(z\) is nonpositive, as follows by integrating \((z-z')(r(z)-r(z'))\le0\). Hence \(1-q_t\le3/(4t)\); symmetry also gives \(0<q_t<1\). Centrality gives both matrix means \(q_tI\), so the inside product comparison has energy at most \(3\kappa N_Qt/8+6bM_Q/t\). Set \(t=4\sqrt{bM_Q/(\kappa N_Q)}\), or take the constant vector. This proves the upper bound. The lower bounds follow from the nonnegative inside kinetic, inside potential, crossing potential and \(H_{\rm out}-E_{\rm out}\).

The face identities and exact incidence bounds are
\[
\begin{gathered}
J(y)=6A_1-3y,\qquad \Delta Y=J(Y),\qquad
\gamma=\Gamma(Y),\\
\sum_\alpha(X_{e,\alpha}D_p)^2=D_p-D_p^2/4\quad(e\in p),\\
\gamma\le
\sum_e r_e^f\sum_{p\ni e}|f_p|^2(D_p-D_p^2/4)
\le16FY-\frac4{n_f}Y^2,\qquad
n_f=\#\{p:f_p\ne0\}.
\end{gathered}\tag{LR7}
\]
The Laplacian follows from \(\sum_\alpha T_\alpha^2=-3I/4\) on each of the four incident links. In a quaternion representation the squared derivative on one link is \(1-W_p^2/4\); inverse traversals and surrounding links act by signs and orthogonal adjoint transports. Cauchy–Schwarz at each edge, with the actual count \(r_e^f\le4\), gives the first bound. Expanding it bounds \(16FY-\gamma\) below by \(16\sum_p|f_p|(F-|f_p|)D_p+4\sum_p f_p^2D_p^2\), whose last term is at least \(4Y^2/n_f\).

## 2. Actual weighted energy and its complete score square

Write the original inside and outside coordinates as \(x,v\), with their unchanged product Haar measures. Define
\[
\begin{gathered}
n(x)=\int\psi(x,v)^2\,dv>0,\qquad
\overline Z(x)=n(x)^{-1}\int|\nabla_Q\psi(x,v)|^2\,dv,\\
R_Q(x)=n(x)^{-1}\int\left[\kappa|\nabla_{\rm out}\psi|^2+
(V_{\rm out}-E_{\rm out})\psi^2+bW_\times\psi^2\right]dv,\\
V_{\rm out}=b\sum_{p\ \mathrm{outside}}(2-W_p),\qquad
R_0(x)=FW_Q(x)-Y(x)+(F/b)R_Q(x)\ge0.
\end{gathered}\tag{LR8}
\]
The outside form inequality, applied separately to the smooth function \(v\mapsto\psi(x,v)\) for each fixed \(x\), gives \(R_Q\ge0\). It does not give a pointwise sign to \(V_{\rm out}-E_{\rm out}\). Smoothness and compactness show that all functions in (LR8) are smooth and bounded at each fixed regulator. The complete outside scalar \(2b(M-M_Q-C_Q)\), the crossing scalar \(2bC_Q\), and the outside ground energy remain present.

For every real smooth inside function \(\Phi(x)\), multiplying the original ground equation by \(\Phi\psi\) and integrating gives
\[
e\mu\Phi=\mu\left[\Phi\{Y+R_0+\alpha F\overline Z\}\right]
-\frac{\alpha F}{2}\mu\Delta_Q\Phi.
\tag{LR9}
\]
Indeed the inside kinetic cross term is \(\kappa\mu\Gamma_Q(w,\Phi)=-\kappa\mu\Delta_Q\Phi/2\); the other inside kinetic term is \(\kappa\mu(\Phi\overline Z)\), while integration over the outside coordinates gives exactly \(R_Q\). This proves (LR9) for signed functions too. Gauge transformations of the original vertices act by Haar isometries separately on the inside and outside link sets, so their conditional changes of variables preserve (LR8) and (LR9). No quotient volume or product decomposition of the physical subspace is substituted.

For all real \(t\), put
\[
\begin{gathered}
M(t)=\mu e^{tY}>0,\qquad \langle G\rangle_t=\mu(Ge^{tY})/M(t),\\
d_t=\langle Y\rangle_t,\quad h_t=\langle\gamma\rangle_t,
\quad z_t=\langle Z_Q\rangle_t,\quad
s_t=\langle\Gamma_Q(w,Y)\rangle_t,\\
J_t=6A_1-3d_t,\qquad R_t=\langle R_0\rangle_t,\qquad
\delta_t=16Fd_t-h_t\ge4\langle Y^2\rangle_t/n_f.
\end{gathered}\tag{LR10}
\]
These are ratios of actual source-zero moments, not ground states for a source-deformed Hamiltonian. The function \(Y\) is nonconstant: on the original commuting link path
\(U_d(z;\theta)=\exp(\theta T_3\sum_{k<d}z_k)\), every oriented face equals \(\exp(\theta T_3)\), whence \(Y=A_1[2-2\cos(\theta/2)]\). Thus \(0<d_t<4A_1\) and \(h_t>0\), because the original positive measure has full support and \(\gamma\) is positive on an open set. All derivatives of \(M\) exist. Haar integration by parts and (LR9) give
\[
2s_t=-J_t-th_t,\qquad
e=d_t+R_t+\alpha Fz_t-\frac{\alpha F}{2}(t^2h_t+tJ_t).
\tag{LR11}
\]
Complete the actual score square, with no coordinate change:
\[
\begin{aligned}
Q_t&=\left\langle\left|\nabla_Qw+
\left(\frac t2+\frac{J_t}{2h_t}\right)\nabla_QY\right|^2\right\rangle_t\ge0,\\
&=z_t+ts_t+\frac{t^2h_t}{4}-\frac{J_t^2}{4h_t},\\
e&=d_t+\frac{\alpha J_t^2}{64d_t}-4\alpha F^2t^2d_t
+R_t+\alpha FQ_t+
\frac{\alpha J_t^2\delta_t}{64d_th_t}
+\frac{\alpha Ft^2\delta_t}{4}.
\end{aligned}\tag{LR12}
\]
For the second line, the cross term between \(\nabla_Qw+t\nabla_QY/2\) and \(\nabla_QY\) has mean \(-J_t/2\) by (LR11). Substituting the second line in the second equation (LR11) cancels both terms linear in \(tJ_t\). The remaining identity is
\(e=d_t+R_t+\alpha FQ_t+\alpha FJ_t^2/(4h_t)-\alpha Ft^2h_t/4\).
Using \(h_t=16Fd_t-\delta_t\) proves the third line with all four nonnegative remainders retained.

Define positive constants and the complete polynomial remainder
\[
\begin{gathered}
c=9\alpha/64,\quad A_0=1+c,\quad \beta_0=4\alpha F^2,\quad
B=e+4cA_1,\quad C=4cA_1^2,\\
P_t(s)=(A_0-\beta_0t^2)s^2-Bs+C,\\
\mathcal D_t=d_tR_t+\alpha Fd_tQ_t+
\frac{\alpha J_t^2\delta_t}{64h_t}
+\frac{\alpha Ft^2d_t\delta_t}{4}\ge0.
\end{gathered}\tag{LR13}
\]
Multiplication of (LR12) by \(d_t\), followed by the literal expansion \(J_t^2=36A_1^2-36A_1d_t+9d_t^2\), proves
\[
\boxed{\quad P_t(d_t)+\mathcal D_t=0.\quad}
\tag{LR14}
\]

## 3. Both roots and a lower-tail bound for every parameter

Put \(D=B^2-4A_0C\). At \(t=0\), (LR14) gives \(D\ge0\) and brackets the actual mean. In fact \(D>0\). If \(D=0\), (LR14) forces its third remainder to vanish. Since \(\delta_0>0\), this forces \(J_0=0\), so \(d=2A_1\). A double root would then require \(B=4A_0A_1\), whereas \(P_0(2A_1)=0\) requires \(e=2A_1\), hence \(B=(2+4c)A_1\). The difference is \(2A_1>0\), a contradiction. Therefore
\[
\begin{gathered}
D>0,\qquad
r_-={2C\over B+\sqrt D},\quad
r_+={B+\sqrt D\over2A_0},\qquad
0<r_-\le d\le r_+\le e,\\
r_-r_+=C/A_0,\qquad
e\ge4A_1\{\sqrt{c(1+c)}-c\}.
\end{gathered}\tag{LR15}
\]
The lower bound for \(e\) is the inequality \(B\ge2\sqrt{A_0C}\). To justify \(r_+\le e\), (LR9) at \(\Phi=1\) gives \(d\le e\), while \(P_0(e)=c(e-2A_1)^2\ge0\). Thus \(e\) is on or beyond the right root, unless \(e=d=r_-\). In that exceptional possibility \(P_0(e)=0\) forces \(e=2A_1\); but \(P_0'(2A_1)=2A_1>0\), so it is the right root after all.

For every real \(t\) define
\[
r_-(t)={2C\over B+\sqrt{D+4\beta_0Ct^2}}.
\tag{LR16}
\]
Then \(d_t\ge r_-(t)\) for every \(t\), including when \(A_0-\beta_0t^2\le0\). If that coefficient is positive, (LR16) is the smaller positive root. If it vanishes, the inequality \(P_t(d_t)\le0\) says \(d_t\ge C/B\), which equals (LR16). If it is negative, the polynomial is strictly decreasing on \([0,\infty)\), starts at \(C>0\), and has one positive root, again given by (LR16). This proves the global assertion without extending a two-positive-root argument beyond its domain.

Set
\[
p_0={\sqrt C\over\sqrt{\beta_0}}={3A_1\over8F},\qquad
\lambda_-={r_-\over p_0}>0.
\tag{LR17}
\]
The inequality \(\sqrt{D+4\beta_0Ct^2}\le\sqrt D+2\sqrt{\beta_0C}|t|\) gives
\(r_-(-t)\ge r_-/(1+\lambda_-t)\) for \(t\ge0\). Since
\(d(\log M(-t))/dt=-d_{-t}\), integration from zero proves the global actual Laplace bound
\[
\boxed{\quad M(-t)\le(1+\lambda_-t)^{-p_0},\qquad t\ge0.\quad}
\tag{LR18}
\]
This is an inequality for the original ground-state law. No density appearing on the right is assigned to \(Y\).

For \(0<u<1\), use Markov's inequality with \(t=(u^{-1}-1)/\lambda_-\) in (LR18). Retaining the original threshold gives
\[
\boxed{\quad
\mu(Y\le ur_-)\le\exp\{p_0(1-u+\log u)\}
\le\exp[-p_0(1-u)^2/2].\quad}
\tag{LR19}
\]
The second inequality follows by integrating
\(1/u-1\ge1-u\) from \(u\) to 1. The threshold zero has probability zero: \(Y\) is a nonzero real analytic function of the links and its zero set has Haar measure zero. Alternatively (LR18) and monotone convergence give \(\mu(Y=0)=0\). Thus integration of \(2r\) times the second bound, extending its nonnegative upper estimate from \(0\le r\le r_-\) to infinity, proves
\[
\boxed{\quad
\mu[(r_--Y)_+^2]\le4V_-,\qquad
V_-={r_-^2\over2p_0}
={F\sqrt\alpha\,r_-^2\over\sqrt C}
\le{3F\alpha A_1\over4(1+c)}.\quad}
\tag{LR20}
\]
The last inequality uses the exact product \(r_-r_+=C/A_0\) and \(r_-\le r_+\).

## 4. Upper root and the remaining interval

Let
\[
T={1\over4F\sqrt\alpha},\qquad A_{\min}=3/4+c,\qquad
V_+={F\sqrt\alpha(2\sqrt C+r_+)\over2A_{\min}}.
\tag{LR21}
\]
For \(0\le t\le T\), \(A_0-\beta_0t^2\ge A_{\min}>0\), and (LR14) gives
\[
d_t\le r_+(t):={B+\sqrt{D+4\beta_0Ct^2}\over2(A_0-\beta_0t^2)}
\le r_++2V_+t.
\tag{LR22}
\]
Indeed subtracting \(r_+\) before taking any bound gives
\[
r_+(t)-r_+
={\sqrt{D+4\beta_0Ct^2}-\sqrt D\over2(A_0-\beta_0t^2)}
+{r_+\beta_0t^2\over A_0-\beta_0t^2}.
\]
The first numerator is at most \(2\sqrt{\beta_0C}t\), and \(\beta_0T=F\sqrt\alpha\). These two inequalities give precisely (LR22). Integrating the logarithmic derivative of \(M\), then optimizing the Markov parameter in \([0,T]\), yields
\[
\begin{gathered}
\log M(t)\le r_+t+V_+t^2,\quad0\le t\le T,\\
\mu(Y\ge r_++r)\le
\begin{cases}
\exp[-r^2/(4V_+)],&0\le r\le2V_+T,\\
\exp[-Tr+V_+T^2],&r\ge2V_+T,
\end{cases}\\
\boxed{\quad\mu[(Y-r_+)_+^2]\le4V_++2T^{-2}e^{-V_+T^2}.\quad}
\end{gathered}\tag{LR23}
\]
For the last line, the integrals are
\(4V_+(1-e^{-V_+T^2})\) on the first interval and
\((4V_++2T^{-2})e^{-V_+T^2}\) on the second. Their joining terms cancel exactly.

Every root, Laplace and tail proof also applies with an explicitly declared comparison ceiling \(e'\ge e\). In (LR13) replace \(e\) by \(e'\) in the polynomial and add \((e'-e)d_t\) to its remainder. The exact equation (LR14) and its nonnegative remainder are preserved, so the later inequalities follow with the corresponding roots and constants. In particular the illustrated choice \(e'=F\Lambda_Q\) uses the proved local comparison and leaves the original measure unchanged. The identities involving the actual energy observable \(Y+\mathcal A\) continue to use the actual \(e\), not \(e'\).

No estimate above removes the interval \([r_-,r_+]\). Let
\(\Pi(Y)=\min\{r_+,\max\{r_-,Y\}\}\) be clipping in the original scalar coordinate, and \(E=Y-\Pi(Y)\). Its two parts have disjoint support. The reverse triangle inequality and the covariance triangle inequality in \(L^2(\mu)\) give the concrete receiver
\[
\begin{gathered}
\mu E^2=\mu[(r_--Y)_+^2]+\mu[(Y-r_+)_+^2]
\le4V_-+4V_++2T^{-2}e^{-V_+T^2}=:\mathcal E,\\
|d-\mu\Pi(Y)|\le\sqrt{\mathcal E},\qquad
\operatorname{Var}Y\le
\left({r_+-r_-\over2}+\sqrt{\mathcal E}\right)^2.
\end{gathered}\tag{LR24}
\]
For the interval variance used here, \((\Pi-r_-)(r_+-\Pi)\ge0\) implies
\(\operatorname{Var}\Pi\le(\mu\Pi-r_-)(r_+-\mu\Pi)\le(r_+-r_-)^2/4\).
This proves the receiver and identifies its precise remaining interval term.

## 5. Negative moments and an actual inverse-energy equation

For every \(0<p<p_0\), Tonelli's theorem and the integral
\(y^{-p}=\Gamma(p)^{-1}\int_0^\infty t^{p-1}e^{-ty}\,dt\) give
\[
\boxed{\quad
\mu Y^{-p}\le\lambda_-^{-p}{\Gamma(p_0-p)\over\Gamma(p_0)}.
\quad}\tag{LR25}
\]
Here \(\Gamma(s)=\int_0^\infty x^{s-1}e^{-x}\,dx\) for \(s>0\). To verify the beta integral used after (LR18), multiply the two gamma integrals for \(p\) and \(p_0-p\), substitute \(x=ru,y=r(1-u)\), whose Jacobian is \(r\), and then substitute \(t=u/(1-u)\). This proves the stated coefficient without an imported comparison measure. In particular, for each positive integer \(k<p_0\),
\[
\mu Y^{-k}\le r_-^{-k}\prod_{\ell=1}^k(1-\ell/p_0)^{-1}.
\tag{LR26}
\]

Define the smooth nonnegative inside observable
\[
\mathcal A(x)=R_0(x)+\alpha F\overline Z(x),\qquad
\mu\mathcal A=e-d.
\tag{LR27}
\]
At a fixed regulator with \(p_0>2\), apply (LR9) first to \((Y+\varepsilon)^{-1}\), then let \(\varepsilon\downarrow0\). Every integrand is dominated: \(\mathcal A\) is bounded, (LR25) gives \(\mu Y^{-2}<\infty\), and \(\gamma\le16FY\) bounds the second-derivative term by \(32FY^{-2}\). The endpoints and critical values require no regular-coordinate integration, since the identity was proved on the full compact configuration space before this limit. Put
\[
u=\mu Y^{-1},\qquad v=\mu Y^{-2},\qquad
\delta(U)=16FY(U)-\gamma(U)\ge4Y(U)^2/n_f.
\tag{LR28}
\]
The full retained inverse equation is
\[
\boxed{\quad
1+(3\alpha FA_1-16\alpha F^2)v-(e+3\alpha F/2)u
+\mu(\mathcal A/Y)+\alpha F\mu(\delta/Y^3)=0.
\quad}\tag{LR29}
\]
To check every sign, the unsplit formula is
\(\mu(\mathcal A/Y)=(e+3\alpha F/2)u-1
+\alpha F\mu(\gamma/Y^3)-3\alpha FA_1v\).
Substitution of \(\gamma=16FY-\delta\) gives (LR29). Since \(p_0>2\) implies \(3A_1>16F\), all terms retained after the linear term in (LR29) are nonnegative. Consequently
\[
\begin{gathered}
(3\alpha FA_1-16\alpha F^2)u^2-(e+3\alpha F/2)u+1\le0,\\
0\le\alpha F\mu(Z_Q/Y)
\le\mu(\mathcal A/Y)
\le(e+3\alpha F/2)u-1.
\end{gathered}\tag{LR30}
\]
The first line also uses \(v\ge u^2\). This is a new receiver for the local kinetic energy with its inverse potential weight; both the outside energy and incidence deficit remain in the exact equation (LR29).

The next singular contraction can also be evaluated. For \(p_0>1\), test (LR9) with \(\log(Y+\varepsilon)\) and take the limit. A bound by \(1+Y^{-p}\), with any \(0<p<p_0\), controls the logarithm, while \(\gamma/Y^2\le16F/Y\) and (LR25) control its Laplacian when \(p_0>1\). Since \(\mu(Y+\mathcal A)=e\), the result is
\[
\boxed{\quad
\operatorname{Cov}(Y,\log Y)+\operatorname{Cov}(\mathcal A,\log Y)
=3\alpha FA_1u-\frac{3\alpha F}{2}
-\frac{\alpha F}{2}\mu(\gamma/Y^2).
\quad}\tag{LR31}
\]
The first covariance is nonnegative, as follows by integrating
\((Y-Y')(\log Y-\log Y')/2\) under the product of the actual measure with itself. No sign is assigned to the second covariance.

## 6. Exact centered contractions and their next equation

The original identity (LR9) is stronger than a scalar pushforward identity: it holds for every smooth inside multiplier. Applying it to \(Y-d\), to \((Y-d)^2\), and to \(\mathcal A-\mu\mathcal A\), respectively, gives
\[
\boxed{\begin{aligned}
\operatorname{Var}Y+\operatorname{Cov}(Y,\mathcal A)
 &=\alpha F(3A_1-3d/2),\\
\mu(Y-d)^3+\operatorname{Cov}((Y-d)^2,\mathcal A)
 &=\alpha F\{\mu\gamma-3\operatorname{Var}Y\},\\
\operatorname{Cov}(Y,\mathcal A)+\operatorname{Var}\mathcal A
 &=\frac{\alpha F}{2}\mu\Delta_Q\mathcal A.
\end{aligned}}\tag{LR32}
\]
The middle line uses the literal Laplacian
\(\Delta(Y-d)^2=2\gamma+2(Y-d)(6A_1-3Y)\). The last line is a further signed contraction, not a sign assertion about the first covariance. The use of \(\overline Z\) in (LR27) is essential: the full \(Z_Q(x,v)\) is not an inside observable and would produce omitted outside derivatives in this test.

For comparison with every signed contribution in the original test, put \(G=C_f\). The same identity gives
\[
\operatorname{Cov}(G,Y)+\operatorname{Cov}(G,\mathcal A)
=\frac{\alpha F}{2}\{6a\sum_pf_p-3m_f\},\qquad
\operatorname{Var}C_f=a^2\mu Y^2-m_f^2-4a^2\mu(Y_+Y_-).
\tag{LR33}
\]
Thus neither a signed variance nor its mean is silently replaced by the variance of \(Y\).

To evaluate the derivatives in the last line of (LR32), factor the actual inside marginal, not another measure:
\[
\varphi(x)=\sqrt{n(x)},\quad w_Q=\log\varphi,\\
\chi(x,v)=\psi(x,v)/\varphi(x),\quad\int\chi(x,v)^2dv=1,
\quad \mathcal T_Q(x)=\int|\nabla_Q\chi|^2dv\ge0.
\tag{LR34}
\]
Differentiating the unit-slice identity gives \(\int\chi\nabla_Q\chi=0\) and
\(\int\chi\Delta_Q\chi=-\mathcal T_Q\). Multiply the full ground equation by \(\chi\), integrate over \(v\), and expand \(\Delta_Q(\varphi\chi)\). The resulting exact equation and decomposition are
\[
\begin{gathered}
-\kappa\Delta_Q\varphi+V_{\rm eff}\varphi=E_Q\varphi,
\qquad V_{\rm eff}=bW_Q+R_Q+\kappa\mathcal T_Q,\\
\overline Z=|\nabla_Qw_Q|^2+\mathcal T_Q,\qquad
Y+\mathcal A=e+\alpha F s_Q,\qquad
s_Q=\Delta_Qw_Q+2|\nabla_Qw_Q|^2,\quad\mu s_Q=0.
\end{gathered}\tag{LR35}
\]
These identities hold pointwise in the original inside coordinates. The map
\(J:L^2(dx)\to L^2(dx\,dv)\), \((J\xi)(x,v)=\xi(x)\chi(x,v)\), is an isometry because \(\int\chi^2dv=1\). Its exact quadratic form is
\(\langle J\xi,(H-E_{\rm out})J\xi\rangle
=\kappa\int|\nabla_Q\xi|^2dx+\int V_{\rm eff}|\xi|^2dx\).
The derivative cross term vanishes by \(\int\chi\nabla_Q\chi=0\); all outside and crossing terms give exactly \(R_Q\). Thus (LR35) has an explicit map to the original Hamiltonian and retains its conditional kinetic energy.

Put \(Z=|\nabla_Qw_Q|^2\), \(H_Q=\operatorname{Hess}_Qw_Q\). Product radius-two \(\mathrm{SU}(2)\) has \(\operatorname{Ric}=g/2\). Weighted integration by parts and the Bochner identity give
\[
\begin{gathered}
\mu s_Q^2=-\mu\Gamma_Q(w_Q,s_Q)
=\mu\|H_Q\|^2+\frac12\mu Z
-2\mu H_Q(\nabla_Qw_Q,\nabla_Qw_Q),\\
\mu\|H_Q\|^2+\frac12\mu Z
={1\over2\kappa}\mu\Delta_Q V_{\rm eff},\\
\Delta_QV_{\rm eff}=b(6M_Q-3W_Q)+\Delta_QR_Q+\kappa\Delta_Q\mathcal T_Q.
\end{gathered}\tag{LR36}
\]
For the first line, \(\mu\Phi s_Q=-\mu\Gamma_Q(w_Q,\Phi)\) for every smooth inside \(\Phi\), by two integrations by parts with density \(e^{2w_Q}\). Also
\(\Delta_Q Z/2=\|H_Q\|^2+\Gamma_Q(w_Q,\Delta_Qw_Q)+Z/2\).
Using \(\mu\Delta_QZ=-2\mu\Gamma_Q(w_Q,Z)\) proves the first line. For the second, differentiate the scalar equation
\(V_{\rm eff}-E_Q=\kappa(\Delta_Qw_Q+Z)\), substitute the Bochner identity, and integrate; equivalently
\(\mu\Delta_Q V_{\rm eff}/\kappa
=-2\mu\Gamma_Q(w_Q,\Delta_Qw_Q)-2\mu\Gamma_Q(w_Q,Z)
=2\mu\|H_Q\|^2+\mu Z\).
The last line retains the actual derivative contributions from the outside form and the conditional kinetic energy. Neither has a pointwise or averaged sign here.

In particular the next signed contraction is explicitly
\[
\begin{gathered}
\operatorname{Cov}(Y,\mathcal A)=-\operatorname{Var}Y+\frac{\alpha F}{2}\mu J(Y),\\
\operatorname{Var}\mathcal A=
\operatorname{Var}Y-\alpha F\mu J(Y)+\alpha^2F^2\mu s_Q^2,\\
\mu\Delta_Q\mathcal A=-\mu J(Y)+2\alpha F\mu s_Q^2.
\end{gathered}\tag{LR37}
\]
The identity \(\mu Ys_Q=\mu J(Y)/2\), needed in these expansions, follows from (LR35) by weighted integration by parts. The last line follows from \(\mu\Delta_Qs_Q=2\mu s_Q^2\). It verifies the third equation (LR32) with its full derivative contraction, rather than declaring that equation a closing estimate.

## 7. Evaluating the retained sum by the original local Hessian

Here the derivative contraction can in fact be bounded without dropping \(\Delta_QR_Q\) or \(\Delta_Q\mathcal T_Q\). We give the needed ground-state Hessian proof so this evaluation has no unproved convexity input. On the full original product, use the curvature convention
\[
R(v,z,v,z)=\frac14\sum_e\{|v_e|^2|z_e|^2-\langle v_e,z_e\rangle^2\}\ge0,
\qquad \operatorname{Ric}=g/2,\quad\nabla R=0.
\tag{LR38}
\]
Let \(H=\nabla^2w\) in this paragraph only, and let \(V=b\sum_pD_p\) retain its scalar. Differentiating \(\Delta w+|\nabla w|^2=(V-E_0)/\kappa\) gives
\[
\begin{aligned}
\kappa^{-1}(\nabla^2V)_{ij}
={}&(\mathscr LH)_{ij}+2H_{ik}H_{kj}+2R_{ikjl}H_{kl}
-\operatorname{Ric}_{ik}H_{kj}-\operatorname{Ric}_{jk}H_{ik}
+2R_{ikjl}w_kw_l,\\
\mathscr L&=\Delta+2\nabla w\cdot\nabla.
\end{aligned}\tag{LR39}
\]
The tensor Laplacian and drift here are covariant. To verify signs, at a normal frame the covector commutator is
\(\nabla_iH_{jk}-\nabla_kH_{ij}=R_{ikjl}w_l\).
Consequently
\(\nabla_i\nabla_j|\nabla w|^2=2H_{ik}H_{jk}+2w_k\nabla_kH_{ij}+2R_{ikjl}w_kw_l\).
For the other term the contractions are
\(\nabla_kH_{kj}=\nabla_j\Delta w+\operatorname{Ric}_{j\ell}w_\ell\),
\((\nabla_k\nabla_i-\nabla_i\nabla_k)H_{kj}=\operatorname{Ric}_{i\ell}H_{\ell j}-R_{ikj\ell}H_{k\ell}\), and
\(\Delta H_{ij}=\nabla_k\nabla_iH_{kj}-\nabla_k(R_{ikj\ell}w_\ell)\).
Substitution, with \(\nabla R=0\), gives
\(\nabla_i\nabla_j\Delta w=(\Delta H)_{ij}+2R_{ikjl}H_{kl}-\operatorname{Ric}_{ik}H_{kj}-\operatorname{Ric}_{jk}H_{ik}\).
Their sum proves (LR39).

The least eigenvalue \(\zeta\) of \(H\) is attained on the compact unit tangent bundle. At a negative minimum, extend its eigenvector by radial parallel transport; first derivatives and the second derivatives along those radial geodesics vanish at the chosen point. Hence \((\mathscr LH)(v,v)\ge0\). The curvature/Ricci contraction is
\(2\operatorname{tr}\{R(v,\cdot,v,\cdot)(H-\zeta g)\}\ge0\), and the final curvature term in (LR39) is nonnegative. Thus \(2\zeta^2\le\kappa^{-1}\nabla^2V(v,v)\).
For a product geodesic with velocities \(Y_e=\sum_\alpha y_{e,\alpha}T_\alpha\), each original face word has four same-factor and twelve ordered distinct-factor second derivatives. The inequalities \(\|Y_e\|_{\rm op}=|y_e|/2\), \(|\operatorname{Tr}A|\le2\|A\|_{\rm op}\) give
\(|\nabla^2D_p(y,y)|\le\tfrac12(\sum_{e\in p}|y_e|)^2\le2\sum_{e\in p}|y_e|^2\).
Each edge belongs to at most four original faces, including the boundary. Thus \(\nabla^2V\le8bg\), and
\[
\nabla^2w\ge-2\alpha^{-1/2}g.
\tag{LR40}
\]
Differentiating the actual marginal also gives
\(\nabla^2w_Q=\mathbb E_\mu[\nabla_Q^2w\mid x]+2\operatorname{Cov}_\mu(\nabla_Qw\mid x)\ge-2\alpha^{-1/2}g_Q\).
This identity keeps its positive conditional covariance; no marginal log-concavity is assumed.

Define the full-configuration inside divergence and the exact local potential trace
\[
\begin{gathered}
S_Q=\Delta_Qw+2Z_Q,\qquad
\mathcal V_Q=6M_Q-3\mu W_Q+\frac32C_Q-\frac34\mu W_\times,\\
G_Q=\nabla_Qw,\quad H_{QQ}=\nabla_Q^2w,\quad
H_{{\rm out},Q}=\nabla_{\rm out}\nabla_Qw.
\end{gathered}\tag{LR41}
\]
The pointwise identity \(\psi^2S_Q=\Delta_Q(\psi^2)/2\), integrated in \(v\), proves
\(s_Q=\mathbb E_\mu[S_Q\mid x]\). Partial Bochner and weighted integration by parts in just the inside coordinates give
\[
\mu S_Q^2=\mu\|H_{QQ}\|^2+\frac12\mu Z_Q
-2\mu H_{QQ}(G_Q,G_Q).
\tag{LR42}
\]
This is the same calculation as the first line of (LR36), performed with the full \(w(x,v)\) while keeping \(v\) fixed before integration. Differentiating the full original ground equation once, and using that the inside tangent projection is parallel, also gives
\[
\begin{gathered}
\mathscr L Z_Q=2\|\nabla\nabla_Qw\|^2+Z_Q
+{2\over\kappa}\langle\nabla_Qw,\nabla_QV\rangle,\\
\mu\|\nabla\nabla_Qw\|^2+\frac12\mu Z_Q
={1\over2\alpha}\mathcal V_Q.
\end{gathered}\tag{LR43}
\]
For the second line integrate the first against \(\mu\) and use
\(\mu\Delta_QV=-2\mu\langle\nabla_Qw,\nabla_QV\rangle\).
Each inside face has four inside edges and contributes \(b(6-3D_p)\) to \(\Delta_QV\); each crossing face has exactly one and contributes \(b(3/2-3D_p/4)\); outside faces contribute zero. This proves precisely the complete \(\mathcal V_Q\), and also proves \(\mathcal V_Q\ge0\).

Set
\[
\begin{gathered}
\mathcal B=(\alpha F)^2\mu s_Q^2
=\operatorname{Var}(Y+\mathcal A),\\
\mathcal B_{\rm up}={\alpha F^2\over2}\mathcal V_Q
+4\alpha^{3/2}F^2\mu Z_Q.
\end{gathered}\tag{LR44}
\]
Equations (LR40)–(LR43) and conditional variance give not just an upper bound but its complete nonnegative difference:
\[
\boxed{\begin{aligned}
\mathcal B_{\rm up}-\mathcal B
=\alpha^2F^2\big[&\mu\|H_{{\rm out},Q}\|^2
+2\mu(H_{QQ}+2\alpha^{-1/2}g_Q)(G_Q,G_Q)\\
&+\mu\operatorname{Var}_\mu(S_Q\mid x)\big]\ge0.
\end{aligned}}\tag{LR45}
\]
To see the equality directly, subtract (LR42) from
\(\mu\|\nabla\nabla_Qw\|^2+\mu Z_Q/2+4\alpha^{-1/2}\mu Z_Q\).
The difference is exactly the first two bracketed terms. Subtracting \(\mu s_Q^2\) from \(\mu S_Q^2\) adds the third. This evaluates the previously retained derivative contraction through the original operator; it does not presume signs for its two marginal potential derivatives.

Write \(c_Y=\alpha F(3A_1-3d/2)\). The exact covariance matrix is therefore
\[
\boxed{\quad
\operatorname{Cov}\begin{pmatrix}Y\\\mathcal A\end{pmatrix}
=\begin{pmatrix}
\operatorname{Var}Y&c_Y-\operatorname{Var}Y\\
c_Y-\operatorname{Var}Y&\operatorname{Var}Y+\mathcal B-2c_Y
\end{pmatrix},\qquad0\le\mathcal B\le\mathcal B_{\rm up}.
\quad}\tag{LR46}
\]
In particular
\(\operatorname{Cov}(Y,\mathcal A)+\operatorname{Var}\mathcal A=\mathcal B-c_Y\)
lies in \([-c_Y,\mathcal B_{\rm up}-c_Y]\), and
\(\operatorname{Var}\mathcal A-\operatorname{Var}Y=\mathcal B-2c_Y\).
The determinant is \(\mathcal B\operatorname{Var}Y-c_Y^2\ge0\). Thus the exact evaluated next equation constrains a positive covariance matrix and proves a lower variance bound when \(c_Y\ne0\); it does not reverse that determinant inequality into an upper bound.

## 8. Original-path limits, constants and scope

Retain
\[
\begin{gathered}
L_j=j^4,\quad a_j=(100j)^{-1},\quad g_j^2=\kappa_*/(200j),
\quad\kappa_j=\kappa_*,\quad b_j=1/(\kappa_*a_j^2),
\quad\alpha_j=\kappa_*^2a_j^2,\\
v_{\ell,j}=L_j+\lfloor(c_\ell-o_\ell)/a_j\rfloor-1,
\qquad q_j=\lceil R/a_j\rceil+3,\\
\mathsf L_R=9\kappa_*R^3+24R^2,\qquad J_1=\int_{\mathbb R^3}|f|>0.
\end{gathered}\tag{LR47}
\]
The cube of side \(R\) contains the physical support of \(f\). For sufficiently large \(j\), the displayed patch lies inside the original box. All six original boundary indicators were retained before this limit. Direct substitution in the exact counts gives
\(a_j^3M_{Q_j}\to3R^3\), \(a_j^2\Lambda_{Q_j}\to\mathsf L_R\).
Each face orientation is a translated cubic mesh of step \(a_j\); the Riemann-sum error is bounded by a fixed support-enlargement volume times the modulus of continuity of \(|f|\) at \(\sqrt3a_j/2\). Hence
\(a_j^3A_{1,j}\to3J_1\).
The lower energy inequality in (LR15), together with \(e\le F\Lambda_Q\), proves
\(e_j=\Theta(a_j^{-2})\). The product of the roots and their upper bound by \(e_j\) then prove
\(r_{-,j},r_{+,j},d_j=\Theta(a_j^{-2})\).
Thus \(p_{0,j}=\Theta(a_j^{-3})\), \(\lambda_{-,j}=\Theta(a_j)\), and (LR26) proves
\[
\mu Y_j^{-k}=O(a_j^{2k})\quad\text{for every fixed positive integer }k,
\qquad \mu(Z_{Q_j}/Y_j)=O(a_j^{-2}).
\tag{LR48}
\]
The latter follows from (LR30), because \((e_j+3\alpha_jF/2)\mu Y_j^{-1}=O(1)\). Nonintegral fixed negative powers follow from a larger integer power by Hölder. The threshold \(p_{0,j}>k\) holds for all sufficiently large \(j\); no claim of that inequality is made at earlier meshes.

The two squared excess bounds have the explicit original-scale consequences
\[
\boxed{\begin{aligned}
\limsup_j a_j\mu[(r_{-,j}-Y_j)_+^2]&\le9F\kappa_*^2J_1,\\
\limsup_j a_j\mu[(Y_j-r_{+,j})_+^2]&\le
12F\kappa_*^2J_1+\frac83\kappa_*F^2\mathsf L_R.
\end{aligned}}\tag{LR49}
\]
These are exactly bounds on \(a_j^2\) times the squared excess divided by \(a_j\); no observable was rescaled in their derivation. The first is (LR20) and \(a_j\alpha_jA_{1,j}\to3\kappa_*^2J_1\). For the second, \(\sqrt C=(3/4)\sqrt\alpha A_1\), \(r_+\le e\le F\Lambda_Q\), and (LR21) give
\(\limsup a_jV_{+,j}\le3F\kappa_*^2J_1+(2/3)\kappa_*F^2\mathsf L_R\).
Also \(V_{+,j}=\Theta(a_j^{-1})\), \(T_j=\Theta(a_j^{-1})\), so the exponential remainder in (LR23) vanishes after multiplication by \(a_j\).

For the sharper kinetic constant, use (LR14) for \(Y=W_Q\), \(F=1\), \(A_1=M_Q\). The inequality \(e_Q=E_Q/b\le\Lambda_Q\) preserves the nonpositive polynomial value when the coefficient \(e_Q\) is enlarged to \(\Lambda_Q\). Thus both roots bracket \(\mu W_Q\). Their original-scale limits are
\[
\mathfrak d_R^\pm={\mathsf L_R\pm\sqrt{\mathsf L_R^2-81\kappa_*^2R^6/4}\over2},
\quad 0<\mathfrak d_R^-<\mathfrak d_R^+<\mathsf L_R,
\quad\mathsf K_R=\mathfrak d_R^+=\mathsf L_R-\mathfrak d_R^-.
\tag{LR50}
\]
Indeed the leading coefficient tends to 1, \(a_j^2(\Lambda_Q+4cM_Q)\to\mathsf L_R\), and \(a_j^4(4cM_Q^2)\to81\kappa_*^2R^6/16\). The discriminant is strictly positive because \(\mathsf L_R\ge9\kappa_*R^3\). The lower root gives
\(\limsup a_j^2(\Lambda_Q-\mu W_Q)\le\mathsf K_R\).
Using the exact budget \(\mu Z_Q\le(\Lambda_Q-\mu W_Q)/\alpha\) in (LR44), while retaining all finite negative trace terms there, proves
\[
\boxed{\quad
\limsup_j a_j\operatorname{Var}(Y_j+\mathcal A_j)
\le F^2\{9\kappa_*^2R^3+4\kappa_*\mathsf K_R\}.
\quad}\tag{LR51}
\]
The crossing term contributes zero to this particular leading limit since \(a_j\alpha_jC_{Q_j}=O(a_j)\); it remains in (LR44)–(LR45). The negative inside and crossing means remain in the finite bound, and were only removed when obtaining the displayed explicit limit. Moreover
\(a_jc_{Y_j}\to9\kappa_*^2FJ_1\).
Therefore (LR46) evaluates both
\(\operatorname{Cov}(Y_j,\mathcal A_j)+\operatorname{Var}\mathcal A_j\)
and \(\operatorname{Var}\mathcal A_j-\operatorname{Var}Y_j\) at order \(a_j^{-1}\), including the exact signs and means.

The bounds in (LR24) still permit \(\operatorname{Var}Y_j=O(a_j^{-4})\), since their root interval has only the proved width \(O(a_j^{-2})\). Formula (LR46) precisely describes the remaining cancellation: large variances of \(Y\) and \(\mathcal A\) would have covariance \(c_Y-\operatorname{Var}Y\), while their sum has the proved small variance. This is a statement about the actual original covariance matrix and its complete nonnegative defect (LR45). It supplies no absent sign of \(\operatorname{Cov}(Y,\mathcal A)\), and no centered order-\(a\) upper bound for the unchanged signed \(C_f\) is claimed. Equations (LR29), (LR31), (LR32), (LR45) and (LR46) are completed next contractions using the actual moments; none replaces the ground law.

## 9. Further inverse-weighted contraction and the original signed map

The inverse equation (LR29) extends to every positive integer \(k\) with \(p_0>k+1\). Write \(m_k=\mu Y^{-k}\), \(m_0=1\), and retain \(\delta=16FY-\gamma\). Testing (LR9) by \((Y+\varepsilon)^{-k}\) and taking the justified limit gives
\[
\boxed{\begin{aligned}
0={}&m_{k-1}+\alpha Fk[3A_1-8F(k+1)]m_{k+1}
-(e+3\alpha Fk/2)m_k\\
&+\mu(\mathcal A/Y^k)+{\alpha Fk(k+1)\over2}\mu(\delta/Y^{k+2}).
\end{aligned}}\tag{LR52}
\]
Indeed \(\Delta Y^{-k}=k(k+1)\gamma Y^{-k-2}-6kA_1Y^{-k-1}+3kY^{-k}\). The derivatives are dominated by a constant times \(Y^{-k-1}\), using \(\gamma\le16FY\), and (LR25) supplies its integrability. The coefficient in square brackets is positive for the stated domain. Since
\(Y+\mathcal A=FW_Q+\alpha F\overline Z+(F/b)R_Q\), (LR52) also yields evaluated bounds
\[
\begin{gathered}
\overline m_k=r_-^{-k}\prod_{h=1}^k(1-h/p_0)^{-1},\quad
t_k=\mu(Z_Q/Y^k)\le\overline t_k=(E_Q/\kappa+3k/2)\overline m_k,\\
w_k=\mu(W_Q/Y^k)\le\overline w_k=(E_Q/b+3\alpha k/2)\overline m_k,\\
\alpha Ft_k\le(e+3\alpha Fk/2)m_k-m_{k-1},\qquad
t_{k,j}=O(a_j^{2k-4}),\quad w_{k,j}=O(a_j^{2k-2}).
\end{gathered}\tag{LR53}
\]
The last retained subtraction uses \(FW_Q\ge Y\); the other nonnegative terms were not assigned a sign different from their proved one.

To use these actual moments in the next equation, put \(U_Q=W_Q+W_\times\), and keep \(S_Q,G_Q,H_{QQ},H_{{\rm out},Q}\) from (LR41). For every smooth positive inside weight \(\Phi\), full and partial Bochner integration give the exact identity
\[
\begin{aligned}
&\mu(\Phi S_Q^2)+\mu(\Phi\|H_{{\rm out},Q}\|^2)
+2\mu[\Phi(H_{QQ}+2\alpha^{-1/2}g_Q)(G_Q,G_Q)]\\
&\quad={1\over2\alpha}\mu\!\left[\Phi\{6M_Q-3W_Q+3C_Q/2-3W_\times/4\}
+\Gamma_Q(\Phi,U_Q)\right]
+{4\over\sqrt\alpha}\mu(\Phi Z_Q)-\mu[S_Q\Gamma_Q(\Phi,w)].
\end{aligned}\tag{LR54}
\]
For a verification of the signed terms, weighted full Bochner gives
\(\mu\Phi(\|\nabla\nabla_Qw\|^2+Z_Q/2)
=(2\kappa)^{-1}\mu[\Phi\Delta_QV+\Gamma_Q(\Phi,V)]
-\mu H_{QQ}(G_Q,\nabla_Q\Phi)\).
Weighted partial Bochner gives
\(\mu\Phi S_Q^2=\mu\Phi(\|H_{QQ}\|^2+Z_Q/2-2H_{QQ}(G_Q,G_Q))
+\mu H_{QQ}(G_Q,\nabla_Q\Phi)-\mu S_Q\Gamma_Q(\Phi,w)\).
Their Hessian-gradient terms cancel. Inserting the exact inside trace of \(V\) and \(\nabla_QV=b\nabla_QU_Q\) proves (LR54), including the two terms of undetermined sign on its right.

Now fix an integer \(k\ge1\) with \(p_0>k+2\), and use \(\Phi=(Y+\varepsilon)^{-k}\). The inverse moments and fixed-regulator smoothness dominate every term, so (LR54) holds in the limit with \(\Phi=Y^{-k}\). The complete incidence count gives
\(\Gamma_Q(U_Q)\le16W_Q+4W_\times\): inside faces have four inside incidences, crossing faces one, and each inside edge belongs to at most four faces. Since \(W_\times\le4C_Q\), Cauchy–Schwarz proves
\[
\begin{gathered}
\left|\mu\{\Gamma(Y,U_Q)/Y^{k+1}\}\right|
\le16\sqrt F\sqrt{(w_k+C_Qm_k)m_{k+1}}
\le\overline G_k:=16\sqrt F\sqrt{(\overline w_k+C_Q\overline m_k)\overline m_{k+1}},\\
\overline D_k={6M_Q+3C_Q/2\over2\alpha}\overline m_k
+{k\over2\alpha}\overline G_k+{4\over\sqrt\alpha}\overline t_k,
\qquad\overline L_k=16Fk^2\overline t_{k+1}.
\end{gathered}\tag{LR55}
\]
The first inequality applies Cauchy–Schwarz to
\(4\sqrt F\sqrt{16W_Q+4W_\times}/Y^{k+1/2}\), retaining both weights. The final signed score term in (LR54) has absolute value at most
\(\sqrt{16Fk^2t_{k+1}X_k}\), where \(X_k=\mu(S_Q^2/Y^k)\), because \(\Gamma(w,Y)^2\le Z_Q\gamma\le16FY Z_Q\). Thus
\(X_k\le\overline D_k+\sqrt{\overline L_kX_k}\).
Solving this quadratic inequality in \(\sqrt{X_k}\), and using conditional Jensen \(s_Q=\mathbb E[S_Q\mid x]\), proves the fully evaluated receiver
\[
\boxed{\begin{gathered}
\mu\{(Y+\mathcal A-e)^2/Y^k\}
\le{\alpha^2F^2\over4}
\left(\sqrt{\overline L_k}+\sqrt{\overline L_k+4\overline D_k}\right)^2
=O(a^{2k-1}),\\
\mu\{((e-Y)_+-\mathcal A)^2/Y^k\}=O(a^{2k-1}).
\end{gathered}}\tag{LR56}
\]
All constants are explicit in the actual energy, roots, patch and original couplings. To check the limit, (LR53) gives
\(\overline D_k=O(a^{2k-5})\), \(\overline L_k=O(a^{2k-2})\), and \(\alpha^2=\kappa_*^4a^4\). The potential-gradient and signed-score corrections have been bounded, not presumed favorable. The second line follows pointwise from positive-part contraction:
\(|(e-Y)_+-\mathcal A|=|(e-Y)_+-(\mathcal A)_+|\le|e-Y-\mathcal A|\), since \(\mathcal A\ge0\). At \(k=0\), the same contraction with (LR44) gives
\[
\mu[((e-Y)_+-\mathcal A)^2]\le\mathcal B,\qquad
\mu[(Y-e)_+^2]\le\mathcal B,\qquad
c_Y^2\le\mathcal B\operatorname{Var}Y.
\tag{LR57}
\]
The second bound uses \((Y-e)_+\le(Y+\mathcal A-e)_+\); the third is the determinant in (LR46). In particular the latter and (LR51) prove the additional actual consequence
\(\liminf_j a_j\operatorname{Var}Y_j\ge81\kappa_*^4J_1^2/(9\kappa_*^2R^3+4\kappa_*\mathsf K_R)\).
This concerns \(aY\), and hence the unchanged \(C_f\) only for a test of one sign; a signed test retains (LR33).

There is nevertheless an exact map for every original signed test. Define the nonnegative inside observable \(\mathcal A_f=\mathcal A+2Y_-\). Then
\[
\boxed{\begin{gathered}
C_f+a\mathcal A_f=a(Y+\mathcal A),\qquad
\mu\mathcal A_f=e-m_f/a,\qquad
\operatorname{Var}(C_f+a\mathcal A_f)=a^2\mathcal B,\\
\operatorname{Cov}(C_f,a(Y+\mathcal A))
={a\alpha F\over2}\{6a\sum_pf_p-3m_f\},\\
\operatorname{Var}(a\mathcal A_f)-\operatorname{Var}C_f
=a^2\mathcal B-a\alpha F\{6a\sum_pf_p-3m_f\}.
\end{gathered}}\tag{LR58}
\]
The first line is pointwise with the unchanged \(C_f\). The second follows by testing (LR9) with \(C_f\); expanding the first-line variance gives the third. For any sequence of multipliers \(G_j\) with \(\sup_j\|G_j\|_\infty<\infty\), the original Hilbert-space norm satisfies
\(\|(C_{f,j}+a_j\mathcal A_{f,j}-a_je_j)G_j\psi_j\|^2
\le\|G_j\|_\infty^2a_j^2\mathcal B_j=O(a_j)\).
This proves the precise vanishing compensated map on every such family; it does not replace \(C_f\) by the compensated observable or claim a separate upper variance bound for it. The original signed covariance and all of its means remain explicit in (LR33) and (LR58).

## 10. Provenance and reproducibility

The local disk-literature routes were read before this continuation; the exact queried canonical database records remain in [the prior source-use ledger](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/458d7cc7dbac2f4b7ee77cd9630a5b79b4344f5c/yang-mills/continuations/20261011-central-signs-shrinking-window/PUSHFORWARD_SOURCE_USE_LEDGER.json). The actual-law comparison source is Frédéric Legoll and Tony Lelièvre, *Effective dynamics using conditional expectations*, original author arXiv:0906.4865v1, [intact author source](https://arxiv.org/src/0906.4865v1). The archive and included TeX remain under the preserved private original-author archive identified by [the prior source-use ledger](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/458d7cc7dbac2f4b7ee77cd9630a5b79b4344f5c/yang-mills/continuations/20261011-central-signs-shrinking-window/PUSHFORWARD_SOURCE_USE_LEDGER.json); lines 135–168, 393–540 and 680–750 of the author TeX were read for the preceding exact conditional map. No theorem from that paper whose noncritical-gradient hypotheses fail here is imported, and no new reading or novelty claim is made. The present exponential, inverse and inside-energy equations were derived on the original compact configuration space, so no critical-value or endpoint current has been omitted.

The full finite-object/local-budget derivation is reproduced from the sealed FO1–FO7, and the Hessian argument (LR38)–(LR40) reproduces the checked provider OS17–OS21 with its curvature and derivative signs. The independent mathematical derivation in [IM1–IM42](INSIDE_MARGINAL_ENERGY.md), IM1–IM42, supplies a second verification of (LR34)–(LR46) and (LR52)–(LR58), including the mixed Hessian and conditional-variance terms. Its complete sealed source was read: SHA256 `e083cd162010a7c5fb364ef347f4ff710b01e7288282c3ab2b8102893fad42ee`. Its 88 bounded checks were replayed from an unchanged script copy in `independent_check_replay`, and its figure was inspected. All sealed providers remain unchanged.

`check_lower_side.py` verifies the polynomial/square identities, the finite parameter domains, the root-envelope inequalities, negative-moment coefficients, covariance determinants and the stated asymptotic coefficients. Its figure plots proved root-tail bounds using the explicit comparison ceiling \(F\Lambda_Q\), with the exact original-path counts and the same compact tent test stated in the caption. It does not plot or fit the unknown ground density. The complete mathematical proof is the present source; finite checks and diagrams support its inspection.

![Both original-coordinate tail bounds and the retained-energy map. The curves use the proved comparison ceiling, exact original-path lattice counts, and the compact tent test stated in the figure. They are probability upper bounds, not samples of the ground density.](lower_side_and_energy.png)



Complete programme providers: [FO1–FO56](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/458d7cc7dbac2f4b7ee77cd9630a5b79b4344f5c/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PUSHFORWARD_OPTIMIZATION.md), [PF1–PF53](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/458d7cc7dbac2f4b7ee77cd9630a5b79b4344f5c/yang-mills/continuations/20261011-central-signs-shrinking-window/ACTUAL_PUSHFORWARD.md), [OP1–OP19](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/458d7cc7dbac2f4b7ee77cd9630a5b79b4344f5c/yang-mills/continuations/20261011-central-signs-shrinking-window/PUSHFORWARD_OPERATOR_RECEIVING.md), [OS1–OS40](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/458d7cc7dbac2f4b7ee77cd9630a5b79b4344f5c/yang-mills/continuations/20261011-central-signs-shrinking-window/ORIGINAL_SOURCE_COVARIANCE.md) and [LC1–LC42](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/458d7cc7dbac2f4b7ee77cd9630a5b79b4344f5c/yang-mills/continuations/20261011-central-signs-shrinking-window/LOCAL_CURVATURE_BUDGET.md). Exact editions and actual use appear in the [source-use ledger](RETAINED_ENERGY_SOURCE_USE_LEDGER.json).

## Actual bounded energy and complete signed covariance

[BM1–BM69](BOUNDED_ENERGY_MULTIPLIER.md) and the independent [IB1–IB46](BOUNDED_MULTIPLIER_RECEIVING.md) construct the original shrinking-window vector and its central, visible and hidden limiting maps. The complete retained energy gives two-root support and exact heat-word receivers. BM66–BM68 receive the full signed observable and companion covariance with every cross term. Its limiting Gram remains to be evaluated; the original operator and signed observable are retained throughout.
