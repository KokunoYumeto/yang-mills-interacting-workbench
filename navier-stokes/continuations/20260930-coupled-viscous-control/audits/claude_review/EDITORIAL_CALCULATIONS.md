# Exact editorial comparisons for the Claude review

These calculations accompany the preserved Claude sources. They do not establish the imported Navier–Stokes existence theorem. The source TeX and translations remain unchanged.

## The original Bessel function and its auxiliary series

Fix a simply connected open domain of nonzero complex \(q\), with one branch of \(\operatorname{Log}(q/2)\). Define the Bessel function with that same branch. For \(|\alpha|<1\), retain
\[
F(\alpha,q)=I'_\alpha(q),\quad x=q^2/4,\quad
G(\alpha,x)=\sum_{m=0}^\infty\frac{(\alpha+2m)x^m}{m!\prod_{j=1}^m(j+\alpha)}.
\]
The empty product is \(1\). Termwise differentiation of the locally uniformly convergent Bessel series gives
\[
qF(\alpha,q)=\frac{\exp(\alpha\operatorname{Log}(q/2))}{\Gamma(1+\alpha)}G(\alpha,q^2/4).
\]
Define
\[
H=\frac{\exp(\alpha\operatorname{Log}(q/2))}{q\Gamma(1+\alpha)},\qquad
L=\operatorname{Log}(q/2)-\psi(1+\alpha).
\]
Every derivative contribution is
\[
\begin{aligned}
F&=HG,\\
F_\alpha&=H(G_\alpha+LG),\\
F_{\alpha\alpha}&=H\{G_{\alpha\alpha}+2LG_\alpha+
[L^2-\psi_1(1+\alpha)]G\},\\
F_q&=H\{(\alpha-1)G/q+(q/2)G_x\}.
\end{aligned}
\]
Here \(\psi=\Gamma'/\Gamma\) and \(\psi_1=\psi'\). Since \(H\) is finite and nonzero, \(F=F_\alpha=0\) is equivalent to \(G=G_\alpha=0\). At that double zero the complete identities give \(F_{\alpha\alpha}=HG_{\alpha\alpha}\) and \(F_q=H(q/2)G_x\). Multiplication by this nonvanishing factor preserves zero multiplicity. Thus the derivative and Gamma contributions have been evaluated at the zero, rather than suppressed from the working object.

At \(q=0\) this comparison is unavailable. The powers, logarithm and \(1/q\) do not define the same regular chart. The auxiliary series has its own analytic extension, \(G(\alpha,0)=\alpha\), \(G_\alpha(0,0)=1\), defining the germ \(\alpha_h(0)=0\) by the implicit function theorem. Its Bessel interpretation uses the comparison at nonzero \(q\); no value of \(F\) at the degenerate endpoint is asserted.

Keep the physical map
\[
\rho_c=2\nu/c,\quad q=k\rho_c,\quad
\alpha=-i\omega\rho_c/c,\quad
\omega(k)=i(c/\rho_c)\alpha_h(k^2\rho_c^2/4),\qquad \nu,c>0.
\]
The branch point \(x_*=q_*^2/4\) has both preimages \(k=\pm q_*/\rho_c\). At each preimage the derivative of \(k^2\rho_c^2/4\) is nonzero, so the square-root branch point persists at both signs. The exact radius in \(k\) is \(q_*c/(2\nu)\), and the frequency at either preimage is \(i\alpha_*c^2/(2\nu)\). All original physical factors remain explicit.

## Navier–Stokes scaling and the norm terminology

Claude's Proposition \(\mathrm{prop:typeII}\), in n3_rates.tex line 46, calls the range \(p_h<p<3\) subcritical. The correct term is supercritical. Its exponent formulas are unaffected.

For fields \(u,p,f\) on \(\mathbb R^3\times[0,T)\), positive viscosity \(\nu\), and \(a>0\), the exact parabolic map is
\[
u^{(a)}(x,t)=a u(ax,a^2t),\quad
p^{(a)}(x,t)=a^2p(ax,a^2t),\quad
f^{(a)}(x,t)=a^3f(ax,a^2t),\qquad 0\le t<T/a^2.
\]
Its inverse has parameter \(a^{-1}\). At \((ax,a^2t)\), direct differentiation gives
\[
\begin{aligned}
\partial_tu^{(a)}&=a^3\partial_tu,&
(u^{(a)}\cdot\nabla)u^{(a)}&=a^3(u\cdot\nabla)u,\\
-\nu\Delta u^{(a)}&=-a^3\nu\Delta u,&
\nabla p^{(a)}&=a^3\nabla p,\\
\nabla\cdot u^{(a)}&=a^2\nabla\cdot u.
\end{aligned}
\]
Every momentum term transforms with the force. A fixed support \(K\) becomes \(a^{-1}K\); the time domain and force support transform by the displayed time map.

The substitution \(y=ax\), \(dx=a^{-3}dy\), gives
\[
\|u^{(a)}(\cdot,t)\|_p^p
=a^p a^{-3}\int_{\mathbb R^3}|u(y,a^2t)|^pdy
=a^{p-3}\|u(\cdot,a^2t)\|_p^p,\qquad 1\le p<\infty.
\]
The norm factor is \(a^{1-3/p}\); the supremum norm factor is \(a\). Thus \(p=3\) is critical, \(p<3\) is supercritical (concentration can reduce the norm), and \(p>3\) is subcritical.

This is a different map from the manuscript's viscosity map:
\[
u_\nu(x,t)=\sqrt\nu\,u(x/\sqrt\nu,t),\quad
p_\nu(x,t)=\nu p(x/\sqrt\nu,t),\quad
f_\nu(x,t)=\sqrt\nu\,f(x/\sqrt\nu,t),\quad K_\nu=\sqrt\nu K.
\]
That map leaves the terminal time unchanged. Its full amplitude and Jacobian factors are
\[
\|u_\nu\|_p^p=\nu^{p/2}\nu^{3/2}\|u\|_p^p,\quad
\|\partial_tu_\nu\|_2^2=\nu\,\nu^{3/2}\|\partial_tu\|_2^2,\quad
\|\operatorname{curl}u_\nu\|_2^2=\nu^{3/2}\|\operatorname{curl}u\|_2^2.
\]
The source exponent \(3/2-h-p(1/2+h)\) vanishes at \(p_h=(3-2h)/(1+2h)\), with \(3-p_h=8h/(1+2h)>0\). Its reported divergence for \(p_h<p<3\) therefore lies in the supercritical range. Correcting this term does not validate the source profile inputs.

## A weaker profile input gives interior nonvanishing

The earlier bridge ns_inner_profile_curvature_current_bridge.md, §5, already proves nonvanishing without requiring a positive axis coefficient. The following function-class argument also supplies a positive interior value.

Let \(A>0\), \(b>0\), and let \(E\) be continuous on \([0,b]\), differentiable on \((0,b)\), with \(E(0)=0\) and \(E(X)>0\) for \(0<X\le b\). The additional function \(B(X)=X^AE(X)\), \(B(0)=0\), is continuous on \([0,b]\). The mean value theorem yields \(X_0\in(0,b)\) with
\[
B'(X_0)=b^{A-1}E(b)>0.
\]
The full product derivative
\[
B'(X)=AX^{A-1}E(X)+X^AE_X(X)
=X^{A-1}\{AE(X)+XE_X(X)\}
\]
then gives \(AE(X_0)+X_0E_X(X_0)>0\). This proves the stated function-class result completely.

The original coefficient in the source coordinates is
\[
\mathcal H(X,\eta)=
\frac{AE(X,\eta)+XE_X(X,\eta)+D\eta E_\eta(X,\eta)}{1-2h\eta^2},
\quad A=1/2+h,\quad D=1/2-h.
\]
At \(\eta=0\) it is positive at the constructed point. Continuity of the displayed derivatives supplies a rectangle with a positive lower bound. This proves a coefficient property; it does not construct the manuscript's profile or establish its error estimates, support conditions, force extension or PDE singularity. It also clarifies that the weaker H1 digest is sufficient for this particular step even when a positive axis coefficient has not been stated.

## Certificate presentation details

The radius proof calls \(Y\) real at n2_rindler.tex line 74, while the program computes the complex preconditioner \(Y=\operatorname{mid}(1/G_\alpha(c,x_0))\). Any nonzero complex \(Y\) for which the displayed inclusion holds is valid. Indeed, \(N_x(\alpha)=\alpha-YG(\alpha,x)\) maps the convex rectangle \(A\) into \(K\subset\operatorname{int}A\) by the complex mean-value integral. Brouwer's theorem supplies a fixed point, and nonzero \(Y\) makes it a zero. Two distinct zeros would make the integral of \(G_\alpha\) on their connecting segment zero, placing zero in its convex rectangular enclosure. A multiple zero would do the same directly. Either puts \(1\) in \(1-YG_\alpha(A,x)\), so the computed rectangle \(K\) contains a translate of \(A-c\). Such a translate cannot fit strictly inside the equal-sized rectangle \(A\). This proves uniqueness and simplicity for the actual complex preconditioner.

The collision script uses machine math.pi to partition a Cauchy circle. The fresh replay uses Arb's enclosing value of \(\pi\) at every endpoint \(2\pi k/256\), covering the complete exact interval \([0,2\pi]\). The unchanged interpolation and Cauchy-remainder calculations then certify the same collision. The two-line adaptation and both source hashes are in replay/COLLISION_EXECUTION_ADAPTATION.json; the fresh result is in replay/collision_OUTPUT.txt. This repairs the enclosure workflow without changing the object, circle radius, constants or theorem.

These editorial corrections have been propagated to the receiving review and claim ledger. They have not been silently substituted into the preserved Claude source.

## Independent transfer derivation and fresh replay

The 30 September redo at `reaudit_20260930/WRITTEN_PROOF_AUDIT.md` now derives the coefficient transfer directly from
\[
[z^n](1-z)^{1/2}=
\frac{\Gamma(n-1/2)}{\Gamma(-1/2)\Gamma(n+1)}
\]
and a Cauchy-contour deformation in the certified dented domain. It proves the `O(n^{-5/2})` contribution of the `O((1-z)^{3/2})` remainder and therefore the stated `n^{-3/2}` leading term, absolute boundary convergence, and boundary sum. The same redo reruns collision, radius, exact cell geometry, sign, rate algebra, and 60 exact coefficients from fresh source copies. Its accepted scope and remaining dependencies are stated in that proof audit.
