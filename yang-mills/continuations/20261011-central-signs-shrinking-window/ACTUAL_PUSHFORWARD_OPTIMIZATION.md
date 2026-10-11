# The actual pushforward law, complete score projection, and an upper tail at source zero

This note optimizes the coefficient in the retained kinetic square over functions of the original observable. It proves the actual conditional-gradient and conditional-ground equations, including every local outside contribution. It also proves an upper-tail estimate whose squared fluctuation has order \(a\) after multiplication by \(a^2\), centered at an explicit local energy ceiling. The distance of that ceiling from the actual mean is retained. Consequently this tail result does not establish an order-\(a\) upper bound for the full centered covariance.

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
\end{gathered}\tag{FO1}
\]
The metric on each \(\mathrm{SU}(2)\) is the radius-two metric. Product Haar has mass one. All original vertex gauge constraints, including boundary vertices, remain imposed. The smooth positive unit lowest eigenfunction of the full compact operator is \(\psi\), and
\[
H\psi=E_0\psi,\qquad w=\log\psi,\qquad d\mu=\psi^2dU.
\tag{FO2}
\]
The ground transform is obtained by expanding derivatives and using the ground equation:
\[
\langle G\psi,(H-E_0)G\psi\rangle
 =\kappa\mu\Gamma(G,\overline G),\qquad
2\mu\Gamma(w,G)=-\mu\Delta G.
\tag{FO3}
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
\end{gathered}\tag{FO4}
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
\end{gathered}\tag{FO5}
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
\end{gathered}\tag{FO6}
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
\end{gathered}\tag{FO7}
\]
The Laplacian follows from \(\sum_\alpha T_\alpha^2=-3I/4\) on each of the four incident links. In a quaternion representation the squared derivative on one link is \(1-W_p^2/4\); inverse traversals and surrounding links act by signs and orthogonal adjoint transports. Cauchy–Schwarz at each edge, with the actual count \(r_e^f\le4\), gives the first bound. Expanding it bounds \(16FY-\gamma\) below by \(16\sum_p|f_p|(F-|f_p|)D_p+4\sum_p f_p^2D_p^2\), whose last term is at least \(4Y^2/n_f\).

## 2. Exact range, critical sets and the actual pushforward

The complete range of \(Y\) is
\[
I=[0,4A_1].
\tag{FO8}
\]
The lower endpoint occurs at all identity links. More precisely the actual commuting link path
\[
\begin{gathered}
U_d(z;\theta)=\exp\left(\theta T_3\sum_{k<d}z_k\right),
\quad 0\le\theta\le2\pi,\quad
U_p(\theta)=\exp(\theta T_3),\\
Y(\theta)=A_1[2-2\cos(\theta/2)],\qquad
\frac{d}{d\theta}Y(\theta)=A_1\sin(\theta/2),\\
\text{at }\theta=2\pi:\qquad
U_1(z)=I,\qquad U_2(z)=(-1)^{z_1}I,\qquad
U_3(z)=(-1)^{z_1+z_2}I.
\end{gathered}
\tag{FO9}
\]
preserves the original edge domain and every face orientation. The two increments of the exponent in the ordered face word differ by one when \(d<e\), proving the displayed \(U_p(\theta)\). The path attains every value in (FO8), and its derivative is positive in its interior. Hence every interior level contains a regular point, including critical values whose other fiber components contain critical points. Its upper endpoint has \(U_p=-I\) on every face, so every \(D_p=4\). Multiplication by this fixed central link field is a Haar isometry and sends every \(D_p\) to \(4-D_p\). Applying the derivative proof of (FO7) to that nonnegative family gives the additional pointwise bound
\[
\gamma\le
\min\left\{
16FY-\frac{4Y^2}{n_f},\
16F(4A_1-Y)-\frac{4(4A_1-Y)^2}{n_f}
\right\}.
\tag{FO10}
\]
No symmetry of the actual ground measure under this transformation is asserted: the full potential is sent to \(4bM-b\sum_pD_p\).

Let \(\mathcal C=\{U:\gamma(U)=0\}\) and \(\mathcal S=Y(\mathcal C)\). The function \(Y\) is nonconstant real analytic in quaternion coordinates; so is \(\gamma\), and \(\gamma\) is not identically zero. The zero set of a nonzero real analytic function has volume zero. This elementary local fact follows by restricting to coordinate lines, whose nonzero analytic restrictions have discrete zero sets, and applying induction on dimension to the identically vanishing restrictions through their first nonzero transverse derivatives. A countable coordinate cover and Fubini then give the assertion. Hence \(\mu(\mathcal C)=0\). Sard's theorem gives Lebesgue measure zero for the compact critical-value set \(\mathcal S\). All endpoints belong to \(\mathcal S\). Neither the critical points nor critical values are discarded from the distributional equations below.

On a regular value \(y\in I\setminus\mathcal S\), let \(d\Sigma_y\) denote induced hypersurface volume and write
\[
\begin{gathered}
c_N=(16\pi^2)^{-N},\qquad dU=c_N\,d\mathrm{vol},\\
\rho(y)=c_N\int_{\{Y=y\}}\frac{\psi^2}{\sqrt\gamma}\,d\Sigma_y,\qquad
d\mu_y=\frac{c_N\psi^2}{\rho(y)\sqrt\gamma}\,d\Sigma_y,\\
h(y)=\int\gamma\,d\mu_y,\qquad
k(y)=\int\Gamma(w,Y)\,d\mu_y,\qquad
z(y)=\int Z_Q\,d\mu_y,\qquad
u(y)=\int W_Q\,d\mu_y.
\end{gathered}\tag{FO11}
\]
The factor \(16\pi^2\) is the Riemannian volume of the radius-two three-sphere. Every quantity in (FO11) belongs to the actual measure \(\mu\), including its original outside variables.

To prove the pushforward formula, cover the regular set by submersion coordinates \((y,t_1,\ldots,t_{3N-1})\) and a partition of unity. The Gram determinant formula for volume in these coordinates is \(d\mathrm{vol}=d\Sigma_y\,dy/\sqrt\gamma\). Integration in these coordinates, followed by monotone exhaustion away from \(\mathcal C\), gives
\[
\mu[\Phi(Y)G]
 =\int_0^{4A_1}\Phi(y)\left(\int G\,d\mu_y\right)\rho(y)\,dy,
\qquad
Y_\#\mu=\rho(y)\,dy,\qquad \int_I\rho=1.
\tag{FO12}
\]
The zero-volume critical set contributes no singular measure. The regular preimage of \(\mathcal S\) also has measure zero by the same coordinate formula. Thus no atom or singular part is suppressed at any critical value. At regular interior values \(\rho,h>0\), and these conditional functions are smooth on each regular interval by compact submersion coordinates. Their values on \(\mathcal S\) can be chosen arbitrarily for integration; all matching conditions below use distributional representatives instead.

## 3. Distributional flux and the complete functional optimizer

Put \(q=h\rho\) on \(I\), extended by zero to \(\mathbb R\). Applying Haar integration by parts to \(B(Y)\nabla Y\) proves for every smooth \(B\) on a neighborhood of \(I\)
\[
2\int_I Bk\rho
 =-\int_I(B'h+BJ)\rho,\qquad
q'=(J+2k)\rho
\quad\hbox{in distributions on }\mathbb R.
\tag{FO13}
\]
Here \(|k|^2\le hz\) by conditional Cauchy–Schwarz. All fixed-regulator gradients are bounded, so \(q\) and its right-hand derivative are integrable. Consequently \(q\in W^{1,1}(\mathbb R)\), has a continuous representative, and
\[
q(0)=q(4A_1)=0.
\tag{FO14}
\]
There is no delta contribution or flux jump at any interior critical value. The formulas do not require \(\rho\) itself to have finite endpoint limits.

For \(B\) smooth and bounded, the limiting weighted square is
\[
\begin{aligned}
\mathcal Q[B]
&=\lim_{\epsilon\downarrow0}
\mu\left[(Y+\epsilon)
\left|\nabla_Qw+\frac{B(Y)}{Y+\epsilon}\nabla Y\right|^2\right]\\
&=\mu(YZ_Q)+2\int_I Bk\rho+
\int_I \frac{B^2h}{y}\rho\\
&=\mu(YZ_Q)-\int_I(B'h+BJ)\rho+
\int_I\frac{B^2h}{y}\rho.
\end{aligned}\tag{FO15}
\]
The ratio is defined as zero on \(Y=0\). The limit follows by dominated convergence from \(\gamma/Y\le16F\). Define
\[
\begin{gathered}
B_*(y)=-\frac{yk(y)}{h(y)}
 =\frac y2\left(\frac{J(y)}{h(y)}
       -\frac{(h\rho)'(y)}{h(y)\rho(y)}\right),\\
\mathcal I_Y=\int_I\frac{yk(y)^2}{h(y)}\rho(y)\,dy,\qquad
\mathcal T_Y=\mu(YZ_Q)-\mathcal I_Y.
\end{gathered}\tag{FO16}
\]
These expressions are defined on regular intervals and almost everywhere. They are finite: \(0\le\mathcal I_Y\le\mu(YZ_Q)\). In the Hilbert space
\[
\mathcal H_Y=L^2\!\left(I,\frac{h(y)\rho(y)}y\,dy\right)
\tag{FO17}
\]
the optimizer \(B_*\) belongs to \(\mathcal H_Y\). Smooth functions supported in regular intervals are dense: remove small neighborhoods of the measure-zero critical values and the endpoints, truncate the function, and approximate on the remaining compact subintervals by smooth functions. All errors tend to zero in the finite measure of (FO17). Thus optimization over smooth admissible coefficients has the same infimum as optimization over this Hilbert space. Completing its square proves
\[
\boxed{\quad
\mathcal Q[B]=\mathcal T_Y+
\int_I\frac{h\rho}{y}(B-B_*)^2\,dy,\qquad
\inf_B\mathcal Q[B]=\mathcal T_Y\ge0.
\quad}\tag{FO18}
\]
This is the complete functional optimization; no guessed scalar density enters it.

For a direct geometric proof, define \(s=\Gamma(w,Y)\). Off \(\mathcal C\), the score splits as
\[
\begin{gathered}
\nabla_Qw=\frac{s}{\gamma}\nabla Y+
\left(\nabla_Qw-\frac{s}{\gamma}\nabla Y\right),\\
z(y)-\frac{k(y)^2}{h(y)}
=\int\left|\nabla_Qw-\frac{s}{\gamma}\nabla Y\right|^2d\mu_y
+\int\left(\frac{s}{\sqrt\gamma}-\frac{k(y)}{h(y)}\sqrt\gamma\right)^2d\mu_y.
\end{gathered}\tag{FO19}
\]
The two terms are respectively the tangential score energy and the remaining variation of its normal coefficient on the actual level set. Their sum is not assumed to vanish. Multiplication by \(y\rho\) and integration equals \(\mathcal T_Y\).

## 4. The exact covariance receiving map

Set \(B_0=J/(32F)\), and retain
\[
\begin{gathered}
\mathcal R_Y=\mu\left[
\frac3{32F}(16FY-\gamma)+
\frac{J(Y)^2}{1024F^2}\left(16F-\frac\gamma Y\right)\right]\ge0,\\
\mathcal D_{\rm proj}=\int_I\frac{h\rho}{y}(B_0-B_*)^2\,dy\ge0.
\end{gathered}\tag{FO20}
\]
Substitute \(B_0'=-3/(32F)\) in (FO15) and retain the two nonnegative differences in (FO20). This gives, with every scalar retained,
\[
\mu(YZ_Q)
=\mathcal T_Y+\mathcal D_{\rm proj}+\mathcal R_Y
+\frac{\mu J(Y)^2}{64F}-\frac32d.
\tag{FO21}
\]
Thus the earlier fixed-coefficient square is exactly \(\mathcal T_Y+\mathcal D_{\rm proj}\). Functional optimization evaluates it as two separate nonnegative actual quantities.

Define
\[
\begin{gathered}
\delta_Q=b\Lambda_Q-E_Q\ge0,\qquad
\mathcal O_Q(Y)=
\langle\sqrt Y\psi,(H_{\rm out}-E_{\rm out})\sqrt Y\psi\rangle+
b\mu(YW_\times)\ge0,\\
\mathcal B_f=\mu[Y(FW_Q-Y)]
+\frac F b[\mathcal O_Q(Y)+\delta_Qd],\\
c=9\alpha/64,\qquad
P_f(s)=(1+c)s^2-(\Lambda_f+4cA_1)s+4cA_1^2.
\end{gathered}\tag{FO22}
\]
Testing (FO3) by \(\sqrt{Y+\epsilon}\) and using the complete decomposition (FO5) cancels its identical \(\kappa\mu[\gamma/(4(Y+\epsilon))]\) terms. The cross term is \(\kappa\mu\Gamma(w,Y)=-\kappa(3A_1-3d/2)\). Dominated convergence as above proves
\[
b\Lambda_Qd
=b\mu(W_QY)+\kappa\mu(YZ_Q)-\kappa(3A_1-3d/2)
+\mathcal O_Q(Y)+\delta_Qd.
\tag{FO23}
\]
Insert (FO21) and multiply by \(F/b\). The result is the complete optimized identity
\[
\boxed{\quad
\mu P_f(Y)+\mathcal B_f+
\alpha F(\mathcal T_Y+\mathcal D_{\rm proj}+\mathcal R_Y)
=3\alpha FA_1.
\quad}\tag{FO24}
\]
No outside, boundary, scalar, mean or sign contribution has been omitted.

The unchanged signed curvature observable therefore satisfies
\[
\boxed{\begin{aligned}
\operatorname{Var}_\mu C_f
={}&\frac{a^2}{1+c}
\big[(\Lambda_f+4cA_1)d-4cA_1^2+3\alpha FA_1
-\mathcal B_f\\
&\hspace{32mm}-\alpha F(\mathcal T_Y+\mathcal D_{\rm proj}+\mathcal R_Y)\big]
-m_f^2-4a^2\mu(Y_+Y_-).
\end{aligned}}\tag{FO25}
\]
Indeed \(C_f^2=a^2Y^2-4a^2Y_+Y_-\). Formula (FO25) is an identity, not a replacement of a signed variance by a multiple of \(\operatorname{Var}Y\).

## 5. The conditional original-ground equation, including the outside form

Write an inside configuration as \(x\) and an outside configuration as \(v\), with product Haar measures \(dx\,dv\). Put
\[
\begin{gathered}
n(x)=\int\psi(x,v)^2\,dv>0,\\
\mathfrak r(x)=
\int\left[
\kappa|\nabla_{\rm out}\psi(x,v)|^2+
(V_{\rm out}(v)-E_{\rm out})\psi(x,v)^2+
bW_\times(x,v)\psi(x,v)^2
\right]dv,\\
r(y)=\mathbb E_\mu[\mathfrak r(x)/n(x)\mid Y=y].
\end{gathered}\tag{FO26}
\]
Here \(V_{\rm out}=b\sum_{p\ \mathrm{outside}}D_p\) includes its full scalar \(2b(M-M_Q-C_Q)\). For each fixed \(x\), the outside variational inequality proves \(\mathfrak r(x)\ge0\), despite no pointwise sign being claimed for \(V_{\rm out}-E_{\rm out}\). All these functions are smooth or bounded at fixed regulator because the configuration spaces are compact and \(n>0\). In particular \(r\ge0\), and
\[
\mathcal O_Q(\Phi(Y))=\int_I\Phi(y)r(y)\rho(y)\,dy
\quad(\Phi\ge0),
\tag{FO27}
\]
where the left side means the outside quadratic form with multiplier \(\sqrt{\Phi(Y)}\).

Multiply the original ground equation by \(\Phi(Y)\psi\), integrate, and integrate the inside kinetic term once. Its cross term is \(\kappa\mu[\Phi'(Y)\Gamma(w,Y)]\). A second integration by parts gives
\[
E_Q\int_I\Phi\rho
=\int_I\Phi(bu+\kappa z+r)\rho
-\frac\kappa2\int_I(\Phi''h+\Phi'J)\rho.
\tag{FO28}
\]
This holds for all smooth real \(\Phi\), including signed ones by linearity. Combining (FO13) and (FO28) gives the second flux equation
\[
\boxed{\quad
\kappa(k\rho)'=(bu+\kappa z+r-E_Q)\rho
\quad\hbox{on }\mathbb R.
\quad}\tag{FO29}
\]
Its right-hand side is integrable. Therefore \(k\rho\in W^{1,1}(\mathbb R)\), has no interior jumps, and its endpoint values are zero. At \(\Phi=1\), (FO28) gives
\[
e-d=\alpha F\mu Z_Q+
\int_I[F u(y)-y+F r(y)/b]\rho(y)\,dy\ge0.
\tag{FO30}
\]
This is the exact energy-ceiling/mean separation.

On a regular interval, put \(\tau(y)=z(y)-k(y)^2/h(y)\ge0\), \(A(y)=J(y)/h(y)\), and \(v(y)=\sqrt{h(y)\rho(y)}\). Substituting \(k\rho=(q'-Aq)/2\) and \(q=v^2\) into (FO29), with no coordinate change, gives
\[
-\kappa h\,v''+
\left[
bu+r+\kappa\tau+
\kappa h\left(\frac{A'}2+\frac{A^2}4\right)
\right]v=E_Qv,\qquad
\int_I\frac{v^2}{h}\,dy=1.
\tag{FO31}
\]
The coefficient functions are the actual conditional functions in (FO11), (FO26). This exact equation is coupled to them; they are not chosen coefficients. At critical values the governing statements are (FO13) and (FO29), not an invented regular matching condition for \(v'\).

Define the ground-transformed generator \(\mathscr L=\Delta+2\nabla w\cdot\nabla\). Its action on an original multiplier is also exact:
\[
\begin{gathered}
\mathscr L(\Phi(Y))
=\gamma\Phi''(Y)+(J(Y)+2s)\Phi'(Y),\\
\mathbb E_\mu[\mathscr L(\Phi(Y))\mid Y=y]
=h(y)\Phi''(y)+(J(y)+2k(y))\Phi'(y)
=\frac{(h\rho\Phi')'}{\rho},\\
\mathscr L(\Phi(Y))-
\left[\frac{(h\rho\Phi')'}{\rho}\right](Y)
=(\gamma-h(Y))\Phi''(Y)+2(s-k(Y))\Phi'(Y).
\end{gathered}\tag{FO32}
\]
The last line has conditional mean zero and gives the complete defect of closing the full dynamics on \(Y\). No Markov property of the original process \(Y(U_t)\) is assumed.

## 6. A further actual calculation: an upper tail with its center retained

The conditional equations yield a quantitative tail even without knowing \(\rho\). For \(t\ge0\), define
\[
\begin{gathered}
M(t)=\mu e^{tY},\qquad
p=3\alpha F/2,\quad q_0=8\alpha F^2,\quad
A_t=1+pt-q_0t^2,\quad B_t=e+3\alpha FA_1t,\\
R_f(y)=F u(y)-y+F r(y)/b\ge0,\\
D_t=\int_I e^{ty}
\left[
\alpha F z(y)+R_f(y)+\frac{\alpha F}{2}t^2(16Fy-h(y))
\right]\rho(y)\,dy\ge0.
\end{gathered}\tag{FO33}
\]
Applying (FO28) to \(e^{ty}\), retaining \(J=6A_1-3y\) and then moving the exact \(h\)-deficit to the right gives
\[
\boxed{\quad A_tM'(t)=B_tM(t)-D_t.\quad}
\tag{FO34}
\]
In particular \(D_0=e-d\); centering this identity at \(d\) does not remove that term.

Take the explicit positive constants
\[
T=\frac1{4F\sqrt\alpha},\qquad
V=3\alpha FA_1+\frac43 eF\sqrt\alpha.
\tag{FO35}
\]
For \(0\le t\le T\), \(q_0t^2\le1/2\), so \(A_t\ge1/2\). From (FO34),
\[
\frac{d}{dt}\log M(t)\le\frac{B_t}{A_t}.
\]
Keeping every term first, the difference from \(e\) is
\[
\frac{B_t}{A_t}-e
=\frac{(3\alpha FA_1-ep)t+eq_0t^2}{A_t}
\le6\alpha FA_1t+2eq_0t^2.
\]
The last inequality uses only \(e,p\ge0\). Integration and \(q_0T=2F\sqrt\alpha\) prove
\[
\log M(t)\le et+3\alpha FA_1t^2+\frac23eq_0t^3
\le et+Vt^2,\qquad 0\le t\le T.
\tag{FO36}
\]
Markov's inequality with \(t=\min\{r/(2V),T\}\) now gives the actual source-zero bound
\[
\boxed{\quad
\mu(Y\ge e+r)\le
\begin{cases}
\exp[-r^2/(4V)],&0\le r\le2VT,\\
\exp[-Tr+VT^2]\le\exp[-Tr/2],&r\ge2VT.
\end{cases}\quad}
\tag{FO37}
\]
The bound is valid even when a threshold exceeds the exact endpoint \(4A_1\), where the actual probability is zero. Integrating \(2r\) times this bound on its two intervals gives
\[
\boxed{\quad
\mu[(Y-e)_+^2]\le
4V+\frac2{T^2}e^{-VT^2}.
\quad}\tag{FO38}
\]
Both integral endpoints \(r=0\) and \(r=2VT\) have been retained in this expression.

On the original path
\[
L_j=j^4,\quad a_j=(100j)^{-1},\quad
g_j^2=\kappa_*/(200j),\quad \kappa_j=\kappa_*,
\quad b_j=1/(\kappa_*a_j^2),\quad \alpha_j=\kappa_*^2a_j^2,
\tag{FO39}
\]
choose a support cube of side \(R\), with exactly
\[
v_{\ell,j}=L_j+\lfloor(c_\ell-o_\ell)/a_j\rfloor-1,\qquad
q_j=\lceil R/a_j\rceil+3.
\tag{FO40}
\]
All boundary indicators stay in (FO5); for sufficiently large \(j\) this cube is interior. Direct substitution in (FO6) gives
\[
a_j^2\Lambda_{Q_j}\longrightarrow\mathsf L_R
=9\kappa_*R^3+24R^2.
\]
For each original orientation the centers are a translate of \(a_j\mathbb Z^3\). Uniform continuity on a fixed support enlargement bounds the quadrature error by its volume times the modulus of continuity at \(\sqrt3a_j/2\). Hence, for \(J_1=\int|f|>0\),
\[
a_j^3A_{1,j}\longrightarrow3J_1,\quad
\limsup_j a_j^2e_j\le F\mathsf L_R,\quad
V_j=O(a_j^{-1}),\quad T_j=(4F\kappa_*a_j)^{-1}.
\tag{FO41}
\]
The positive first term of \(V_j\) also gives \(V_jT_j^2\to\infty\) at order \(a_j^{-3}\). Consequently
\[
\boxed{\quad
\limsup_j\frac{a_j^2\mu[(Y_j-e_j)_+^2]}{a_j}
\le36\kappa_*^2FJ_1+\frac{16}{3}\kappa_*F^2\mathsf L_R.
\quad}\tag{FO42}
\]
Since \(|C_f|\le aY\), the identical upper bound holds with
\(\mu[(|C_f|-ae)_+^2]\) in the numerator in place of \(a^2\mu[(Y-e)_+^2]\). This conclusion concerns the original interacting state, not a sampling or comparison density.

## 7. What the optimization evaluates, and the exact remaining variance map

The results do not set \(e=d\). Formula (FO30) proves the precise positive difference. For the actual nonnegative \(Y\),
\[
\operatorname{Var}_\mu Y
=\mu[(Y-e)_+^2]+\mu[(e-Y)_+^2]-(e-d)^2.
\tag{FO43}
\]
Thus (FO38) evaluates the first term; the lower-side second moment and exact mean separation remain present. The existing budget permits \(e-d=O(a^{-2})\), so no upper exponent for the centered variance follows by identifying these centers.

There is an exact receiving map for that remaining distributional information. Define
\[
I_d(y)=\int_0^y(s-d)\rho(s)\,ds,\qquad
\mathfrak s(y)=-\frac{I_d(y)}{\rho(y)},\qquad
\mathfrak R(y)=-\frac{I_d(y)}{h(y)\rho(y)}
\tag{FO44}
\]
at regular values. The function \(I_d\) is absolutely continuous, has both endpoint values zero, and is nonpositive: before \(d\) its integrand is nonpositive, and after \(d\) it equals minus the nonnegative integral from \(y\) to \(4A_1\). Therefore \(\mathfrak s,\mathfrak R\ge0\). Integration by parts gives, without boundary terms,
\[
\begin{gathered}
\operatorname{Cov}_\rho(Y,\Phi(Y))
=\int_I\mathfrak s(y)\Phi'(y)\rho(y)\,dy,\\
\operatorname{Var}_\mu Y=\int_I\mathfrak s(y)\rho(y)\,dy
=\int_I\mathfrak R(y)h(y)\rho(y)\,dy,\\
(h\rho\mathfrak R)'=-(y-d)\rho,\qquad
h\mathfrak R'=-(y-d)-(J+2k)\mathfrak R
\quad\hbox{on regular intervals}.
\end{gathered}\tag{FO45}
\]
The first formula follows first for smooth \(\Phi\); boundedness of \(Y\) supplies the case \(\Phi(y)=y\). The weak flux equation is valid across every critical value. At this step its product \(h\rho\mathfrak R=-I_d\) has the asserted absolutely continuous representative; the next calculation proves regularity of the ratio itself for this actual observable. Thus (FO45) computes the exact positive quantity that must enter a variance upper estimate; it is not replaced by a spectral-gap or convexity assumption.

For comparison, using the already proved zero boundary flux of \(q=h\rho\),
\[
\int_I(y-d)(J+2k)\rho=-\int_Ih\rho.
\]
Cauchy–Schwarz therefore gives
\[
\operatorname{Var}_\mu Y\ge
\frac{(\int_Ih\rho)^2}{\int_I(J+2k)^2\rho}.
\tag{FO46}
\]
The denominator is positive, because the preceding identity would otherwise contradict \(h>0\) almost everywhere. This completed use of the scalar score yields a lower variance bound. It supplies no upper inequality of the opposite direction.

## 8. Endpoint inverse-score values and their actual variance contribution

The apparent singularity of the ratio in (FO44) can be resolved for this particular \(Y\). By the path (FO9), every interior value \(y_0\) has a regular point. Choose a nonnegative smooth cutoff supported in a submersion chart at that point, positive on a smaller chart. Its contribution to the coarea flux \(q\) is positive and continuous near \(y_0\), since \(\psi>0\) and \(\gamma>0\) there. The full flux dominates that chart contribution almost everywhere; its continuous representative therefore dominates it everywhere in the smaller interval. This proves
\[
q(y)>0,\qquad 0<y<4A_1,
\tag{FO47}
\]
including every interior critical value, without introducing another probability density. It follows that \(\mathfrak R=-I_d/q\) is continuous across every interior critical value.

Put \(\ell=4A_1\), \(\nu_0(y)=\int_0^y\rho\), and \(\nu_\ell(y)=\int_y^\ell\rho\). The coefficient on the right of (FO29), divided by \(\kappa\), is bounded at a fixed regulator. Its zero boundary flux implies
\[
|k(y)\rho(y)|\le C_j\nu_0(y),\qquad
|k(y)\rho(y)|\le C_j\nu_\ell(y).
\]
Integrate (FO13) from the respective endpoint. The integrals of \(s\rho(s)\) and of \(k(s)\rho(s)\) over \([0,y]\) are bounded by constants times \(y\nu_0(y)\); the upper-endpoint estimates use \((\ell-y)\nu_\ell(y)\). Thus
\[
\begin{aligned}
q(y)&=6A_1\nu_0(y)+O_j(y\nu_0(y)),&&y\downarrow0,\\
q(y)&=6A_1\nu_\ell(y)+O_j((\ell-y)\nu_\ell(y)),&&y\uparrow\ell.
\end{aligned}\tag{FO48}
\]
The constants in these endpoint error estimates are explicitly allowed to depend on the fixed regulator; no uniform asymptotic expansion of \(\rho\) is assumed. The corresponding identities
\(-I_d(y)=d\nu_0(y)+O(y\nu_0(y))\) and
\(-I_d(y)=(\ell-d)\nu_\ell(y)+O((\ell-y)\nu_\ell(y))\)
prove the exact endpoint limits
\[
\boxed{\quad
\mathfrak R(0)=\frac d{6A_1},\qquad
\mathfrak R(4A_1)=\frac{4A_1-d}{6A_1}.
\quad}\tag{FO49}
\]
Consequently \(\mathfrak R\) extends continuously to the whole compact interval. From \(d\le\Lambda_f=O(a^{-2})\) and \(a^3A_1\to3J_1>0\), the original path gives
\[
\mathfrak R_j(0)=O(a_j),\qquad
\mathfrak R_j(4A_{1,j})=\frac23-\frac{d_j}{6A_{1,j}}
\longrightarrow\frac23.
\tag{FO50}
\]
This disproves a uniform pointwise bound \(\mathfrak R_j\le C a_j\), with \(C\) independent of \(j\), as a route to the desired variance upper estimate. It does not disprove the needed weighted bound in (FO45).

The endpoint obstruction has a computable receiving map. In the tail bound replace \(e\) by the proved larger ceiling \(\Lambda_f\), and define
\[
\overline V=3\alpha FA_1+\frac43\Lambda_f F\sqrt\alpha,\qquad
\Xi=\min\left\{\frac{\Lambda_f^2}{4\overline V},
                      \frac{T\Lambda_f}{2}\right\}.
\]
Both terms are retained. Equation (FO36), or monotonicity of its upper constants, gives
\[
\mu(Y\ge2\Lambda_f)\le e^{-\Xi}.
\]
For \(b_0=2\Lambda_f\le\ell\), Fubini in (FO44) now yields exactly
\[
\begin{aligned}
\int_{b_0}^{\ell}\mathfrak R(y)h(y)\rho(y)\,dy
&=\mu[(Y-b_0)_+(Y-d)]\\
&\le\ell^2\,\mu(Y\ge b_0)
\le\ell^2e^{-\Xi}.
\end{aligned}\tag{FO51}
\]
Here \(b_0\ge d\), so all integrands are nonnegative. If \(b_0>\ell\), both the tail integral and the positive-part expectation are zero. There is no conditioning or altered probability density in (FO51).

Let \(\mathsf V=9\kappa_*^2FJ_1+(4/3)\kappa_*F^2\mathsf L_R>0\). The exact original-path constants give
\[
a_j\overline V_j\longrightarrow\mathsf V,\qquad
a_j^3\Xi_j\longrightarrow
\min\left\{\frac{F^2\mathsf L_R^2}{4\mathsf V},
                 \frac{\mathsf L_R}{8\kappa_*}\right\}>0.
\]
Since \(\ell_j=4A_{1,j}=O(a_j^{-3})\), the scaled tail in (FO51) is smaller than every positive power of \(a_j\). For the unchanged signed field, \(|C_f|\le a\ell\) and \(|m_f|\le a\ell\) also give
\[
\boxed{\quad
\mu[(C_f-m_f)^2\mathbf1_{\{Y\ge2\Lambda_f\}}]
\le4a^2\ell^2e^{-\Xi}=o(a^n)
\quad\hbox{for every fixed }n>0.
\quad}\tag{FO52}
\]
Thus the nonzero upper endpoint value in (FO50) contributes a quantitatively negligible tail to the target covariance. The receiving problem remaining in (FO45) is the integral over \(0\le Y\le2\Lambda_f\), with its original measure and actual mean. This is a completed removal of the specific endpoint obstruction, rather than an assumption of a uniform pointwise inequality.

## 9. A completed drift calculation for the remaining central variance

The independent derivation supplies another exact receiving calculation for the original law. Since \(d>0\), define
\[
\beta=\frac{6A_1}{d},\qquad
\lambda=\frac{\beta-3}{2},\qquad
\epsilon(y)=k(y)+\lambda y,\qquad
D_\epsilon=\int_I\epsilon(y)^2\rho(y)\,dy,\qquad
S=\int_Ih\rho.
\tag{FO53}
\]
These quantities retain the actual mean. Equation (FO13) with constant test gives \(\int k\rho=-3A_1+3d/2\), so \(\int\epsilon\rho=0\). In particular
\(J+2k=\beta(d-y)+2\epsilon\).
Multiply (FO13) by \(y-d\), integrate using its zero boundary flux, and obtain
\[
\boxed{\quad
\beta\operatorname{Var}_\mu Y
=S+2\int_I(y-d)\epsilon(y)\rho(y)\,dy.
\quad}\tag{FO54}
\]
Cauchy–Schwarz, followed by solving the resulting quadratic in the nonnegative number \(\sqrt{\operatorname{Var}Y}\), proves
\[
\boxed{\quad
\operatorname{Var}_\mu Y
\le\left[
\frac{\sqrt{D_\epsilon}+\sqrt{D_\epsilon+\beta S}}{\beta}
\right]^2.
\quad}\tag{FO55}
\]
The defect norm itself has the proved finite estimate
\[
D_\epsilon\le32F\,\mu(YZ_Q)+2\lambda^2\mu Y^2.
\tag{FO56}
\]
Indeed \(k^2\le hz\) on the actual fibers, \(h\le16Fy\), and
\((k+\lambda y)^2\le2k^2+2\lambda^2y^2\). Thus the first term integrates to at most \(32F\mu(YZ_Q)\), and the second is exactly the stated second moment.

Here is the full exponent calculation, without assigning a favorable sign to the drift defect. The local budget and \(\mu\Gamma(w,Y)=-3A_1+3d/2\) give
\[
(6A_1-3d)^2\le4\mu Z_Q\,S
\le\frac{64}{\alpha}d(\Lambda_f-d).
\]
Because \(d\le\Lambda_f=O(a^{-2})\) and \(A_1=\Theta(a^{-3})\), one has \(d\le A_1\) at sufficiently fine regulators. The preceding inequality then gives
\(d\ge9\alpha A_1^2/(64\Lambda_f)=\Omega(a^{-2})\).
Consequently \(d=\Theta(a^{-2})\), \(\beta=\Theta(a^{-1})\), and \(\lambda=O(a^{-1})\). Equation (FO23), its nonnegative terms, and \(Y\le FW_Q\) give
\(\mu Y^2=O(a^{-4})\) and \(\mu(YZ_Q)=O(a^{-6})\); also \(S\le16Fd=O(a^{-2})\).
Therefore (FO56) gives \(D_\epsilon=O(a^{-6})\), and the fully evaluated upper estimate (FO55) still has order \(a^{-4}\) for \(\operatorname{Var}Y\). The central drift calculation does not improve the full curvature-variance exponent. It provides an exact evaluated receiver rather than replacing the missing term by an assumption.

The functional optimization (FO18), covariance identity (FO25), two conditional flux equations, actual upper tail (FO37), exact endpoint limits, tail removal and drift identity are the established additions. The unresolved full covariance exponent is localized by (FO43), (FO45), (FO51) and (FO54), with the original mean and all conditional data retained. No missing cancellation is declared proved, and no smooth interacting four-dimensional continuum theory is claimed by these finite-regulator statements.

## 10. Source provenance and verification

The underlying local programme derivation is reproduced in (FO1)–(FO7), (FO22)–(FO25), with its sealed source in [ZU1–ZU44](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/f8f4d548dde98f04429f8b7eea664806399de825/yang-mills/continuations/20261011-central-signs-shrinking-window/SOURCE_ZERO_COVARIANCE_UPPER.md), ZU1–ZU44. The original spatial programme source, Section 12, equations (93)–(100), has its [pinned public TeX at line 1742](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/sources/spatial/spatial_continuum.tex#L1742).

The complete independent proof [PF1–PF53](ACTUAL_PUSHFORWARD.md), PF1–PF53, was read. Its current and projection derivations independently agree with (FO11)–(FO32). It supplied the explicit regular path through every level, the exact endpoint variance-receiver limits, the sharper second Chernoff branch and the conditional drift reception (FO53)–(FO56). Its PF27–PF32 additionally prove a scalar ground-form compression and its exact isometry into the original physical Hilbert space. That enclosed note retains both the original-form equality and the orthogonal operator defect; it does not assume an invariant scalar sector.

The canonical disk literature indexes were queried first; exact queries, source IDs and routing-only results are recorded in [the source-use ledger](PUSHFORWARD_SOURCE_USE_LEDGER.json). No PDF was read. The intact original-author archive for Frédéric Legoll and Tony Lelièvre, [Effective dynamics using conditional expectations, arXiv:0906.4865v1](https://arxiv.org/abs/0906.4865v1), is preserved in the private source archive; the [original author source edition](https://arxiv.org/src/0906.4865v1) is publicly accessible. Its TeX lines 135–168, 393–540 and 680–750 were read: their assumption of a gradient bounded away from zero does not hold for the present \(Y\). Their coarea and conditional-diffusion formulas are compared by the exact dictionary \(\xi=Y\), source equilibrium density replaced explicitly by the original \(\psi^2\), conditional diffusion coefficient \(\sigma^2=h\), and conditional drift \(J+2k\) for the operator \(\mathscr L=\Delta+2\nabla w\cdot\nabla\) used in FO32. The physical-time generator is \(\kappa\mathscr L\), its conditional drift is \(\kappa(J+2k)\), and the source dictionary keeps \(\beta^{-1}=\kappa\), \(V_{\rm density}=-2\kappa\log\psi\), and \(Z_{\rm density}=(16\pi^2)^N\) relative to Riemannian volume. [OP18–OP19](PUSHFORWARD_OPERATOR_RECEIVING.md) prove this comparison with every time and measure factor. Equations (FO11)–(FO14) prove the needed compact-manifold extension across the present critical values. None of their dynamical approximation or convergence results is imported.

The reproducible figure depicts the exact maps and retained terms, rather than a fictitious graph of the unknown density. Symbolic checks validate the projection, conditional-ground, exponential-test and tail-integration algebra. A bounded original open-lattice check verifies the central link field (FO9) in all three orientations. These checks supplement the proofs.

![The actual pushforward, complete score projection, and the proved upper-tail envelope for the original compact tent test. The curve is a probability upper bound from FO37 with the explicit ceiling Lambda_f; it is not a graph or sample of the unknown vacuum density.](actual_pushforward_maps.png)


Complete programme providers: [ZU1–ZU44](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/f8f4d548dde98f04429f8b7eea664806399de825/yang-mills/continuations/20261011-central-signs-shrinking-window/SOURCE_ZERO_COVARIANCE_UPPER.md), [PVI1–PVI24 plus PVI19a](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/f8f4d548dde98f04429f8b7eea664806399de825/yang-mills/continuations/20261011-central-signs-shrinking-window/POTENTIAL_VARIANCE_IDENTITIES.md), [LC1–LC42](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/f8f4d548dde98f04429f8b7eea664806399de825/yang-mills/continuations/20261011-central-signs-shrinking-window/LOCAL_CURVATURE_BUDGET.md), and [CP1–CP50](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/f8f4d548dde98f04429f8b7eea664806399de825/yang-mills/continuations/20261011-central-signs-shrinking-window/CURVATURE_PHASE_RECONSTRUCTION.md). The [source-use ledger](PUSHFORWARD_SOURCE_USE_LEDGER.json) records exact editions, actual reading coverage and the receiving calculations.

## Both potential tails and the complete retained-energy covariance

[LR1–LR58](LOWER_SIDE_RETAINED_ENERGY.md) prove both tails around the original local energy roots, exact negative-moment bounds, and inverse-weighted ground and Bochner identities. The full inside energy, including the actual conditional kinetic and outside terms, has variance O(a^-1), with an explicit constant and a complete nonnegative remainder. For the signed original curvature, LR58 proves the exact compensated map and all of its mean and covariance terms.

[IM1–IM42](INSIDE_MARGINAL_ENERGY.md) independently derive the inside marginal, its conditional-vector equation and full operator residual. They evaluate every mixed-Hessian, shifted-Hessian and conditional-score-variance contribution, including inverse weights. The unchanged potential variance retains its signed covariance with the nonnegative energy remainder. The proved small variance of their sum does not assign a sign to that covariance.
