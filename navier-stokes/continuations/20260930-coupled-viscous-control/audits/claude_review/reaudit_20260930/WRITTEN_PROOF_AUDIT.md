# Independent audit of Claude’s Navier–Stokes additions

## Evidence and accepted scope

The audited source is commit

\[
f41c6273497b88e58f345b9dd65735db0afa9237
\]

of the preserved Claude branch. The separate source ZIP passed a fresh whole-file and member-level verification. The six computations in this directory were then run from fresh copies of the preserved programs. They certify:

1. existence and nondegeneracy of the real double zero of \(I'_\alpha(q)\), after replacing machine-angle endpoints by enclosing Arb values of \(\pi\);
2. the \(42{,}650\)-cell Krawczyk tiling, all \(168{,}301\) overlap checks, the two winding calculations, and the fold patch;
3. exact lattice coverage and cell geometry;
4. identification of the hydrodynamic branch as the upper real branch near the fold;
5. the displayed rate algebra;
6. the first \(60\) rational coefficients and the exact residual \(G(\alpha_h(x),x)=O(x^{61})\).

The old and new outputs agree in mathematical content. Differences in the radius and coefficient outputs are timing lines only.

This audit accepts the collision theorem, the exact radius theorem, and the coefficient asymptotic for the specified Bessel spectral curve. It does not accept the imported Navier–Stokes construction, the source paper’s reports about a second interval library, its \(240\)- and \(320\)-coefficient runs, or a novelty claim as newly verified facts.

## 1. The original Bessel function is retained

Fix a simply connected nonzero-\(q\) chart and one branch of \(\operatorname{Log}(q/2)\). Starting with the full Bessel series,

\[
I_\alpha(q)=
\sum_{m=0}^{\infty}
\frac{(q/2)^{2m+\alpha}}{m!\,\Gamma(m+\alpha+1)},
\tag{1}
\]

termwise differentiation gives

\[
qI'_\alpha(q)
=
\frac{\exp(\alpha\operatorname{Log}(q/2))}{\Gamma(1+\alpha)}
G\!\left(\alpha,\frac{q^2}{4}\right),
\tag{2}
\]

where

\[
G(\alpha,x)=
\sum_{m=0}^{\infty}
\frac{(\alpha+2m)x^m}
{m!\prod_{j=1}^{m}(j+\alpha)}.
\tag{3}
\]

The empty product is one. Define

\[
H(\alpha,q)=
\frac{\exp(\alpha\operatorname{Log}(q/2))}
{q\Gamma(1+\alpha)},
\qquad
L(\alpha,q)=\operatorname{Log}(q/2)-\psi(1+\alpha).
\tag{4}
\]

Then the complete derivative identities are

\[
\begin{aligned}
F&:=I'_\alpha(q)=HG,\\
F_\alpha&=H(G_\alpha+LG),\\
F_{\alpha\alpha}
&=H\!\left(G_{\alpha\alpha}+2LG_\alpha+
\bigl[L^2-\psi_1(1+\alpha)\bigr]G\right),\\
F_q&=H\left(\frac{\alpha-1}{q}G+\frac q2G_x\right).
\end{aligned}
\tag{5}
\]

At a simultaneous zero \(G=G_\alpha=0\),

\[
F_{\alpha\alpha}=HG_{\alpha\alpha},
\qquad
F_q=H\frac q2G_x.
\tag{6}
\]

Thus the prefactor, Gamma function, logarithm, and all their derivatives have been evaluated rather than removed. Since \(H\ne0\) on the certified positive-\(q\) box, the zero multiplicity is unchanged.

At \(q=0\), equations (2), (4), and (5) are not a regular chart. The hydrodynamic germ is instead defined directly by

\[
G(\alpha,0)=\alpha,\qquad G_\alpha(0,0)=1,
\tag{7}
\]

and the implicit function theorem.

## 2. What the collision certificate proves

Let

\[
I=[a_0-1.5\cdot10^{-10},a_0+1.5\cdot10^{-10}],
\qquad
J=[q_0-10^{-20},q_0+10^{-20}],
\tag{8}
\]

with the centers printed in the collision output. The fresh Arb computation proves:

\[
F>0\quad\text{on }\partial I\times J,
\tag{9}
\]

\[
F(a_0,q_0-10^{-20})<0,
\qquad
F>0\quad\text{on }I\times\{q_0+10^{-20}\},
\tag{10}
\]

and, throughout \(I\times J\),

\[
F_q>0,\qquad F_{\alpha\alpha}>0.
\tag{11}
\]

The second \(\alpha\)-derivative enclosure uses a central divided difference and a fourth-derivative Cauchy remainder. The revised angular endpoints

\[
\theta_k=\frac{2\,\operatorname{arb}(\pi)\,k}{256}
\tag{12}
\]

cover the complete circle by enclosing intervals. The earlier machine values of \(\pi\) did not by themselves certify exact endpoint coverage.

Define

\[
g(q)=\min_{\alpha\in I}F(\alpha,q).
\tag{13}
\]

Continuity and (10) give a \(q_*\in J\) with \(g(q_*)=0\). Condition (9) places its minimizer \(\alpha_*\) in the interior of \(I\), so

\[
F(\alpha_*,q_*)=F_\alpha(\alpha_*,q_*)=0.
\tag{14}
\]

Equation (11) makes the zero exactly double in \(\alpha\). Since \(F_q\ne0\), the implicit function theorem solves \(F=0\) for \(q=q(\alpha)\), and Taylor expansion gives

\[
q-q_*=
-\frac{F_{\alpha\alpha}(\alpha_*,q_*)}
{2F_q(\alpha_*,q_*)}
(\alpha-\alpha_*)^2
+O((\alpha-\alpha_*)^3).
\tag{15}
\]

Hence the two roots are real on the \(q<q_*\) side and a conjugate pair on the \(q>q_*\) side, locally.

## 3. Why the radius certificate closes the whole disk

The Krawczyk calculation evaluates the full series (3) with a \(30\)-term sum and explicit tails on

\[
|\alpha|\le0.95,\qquad |x|\le0.2.
\tag{16}
\]

For every certified \(x\)-cell \(X_i\), it supplies an \(\alpha\)-rectangle \(A_i\), center \(c_i\), nonzero complex preconditioner \(Y_i\), and enclosure

\[
K_i=
c_i-Y_iG(c_i,X_i)
+\bigl(1-Y_iG_\alpha(A_i,X_i)\bigr)(A_i-c_i)
\subset\operatorname{int}A_i.
\tag{17}
\]

The source paper calls \(Y_i\) real, but the program uses a complex number. Reality is unnecessary. For fixed \(x\in X_i\), the map

\[
N_x(\alpha)=\alpha-Y_iG(\alpha,x)
\tag{18}
\]

maps the convex set \(A_i\) into \(K_i\), by the complex mean-value integral. Brouwer gives a fixed point, and \(Y_i\ne0\) makes it a zero of \(G\).

If two zeros lay in \(A_i\), their divided difference would put \(0\) in the convex enclosure \(G_\alpha(A_i,X_i)\). The same is immediate for a multiple zero. Then \(1\) would belong to \(1-Y_iG_\alpha(A_i,X_i)\), causing \(K_i\) to contain a translate of the full equal-sized rectangle \(A_i\), which cannot lie in \(\operatorname{int}A_i\). The zero is therefore unique and simple.

The independent exact-geometry program verifies:

\[
42{,}650\text{ cells},\qquad
168{,}301\text{ touching pairs},\qquad
0\text{ coverage or consistency failures}.
\tag{19}
\]

On an overlap, one zero enclosure is contained in the neighboring uniqueness rectangle, so the local zeros agree. The cells containing \(x=0\) contain \(\alpha=0\); hence the patched function is the hydrodynamic root.

The fold square contains exactly two roots, counted with multiplicity. Their symmetric discriminant

\[
\Delta(x)=(\beta_1(x)-\beta_2(x))^2
\tag{20}
\]

is analytic. The winding computation on the fold-square boundary gives one zero of \(\Delta\), counted with multiplicity. The certified collision lies inside, so that zero is \(x_*=q_*^2/4\) and is simple.

The certified tiling together with the fold square covers the closed disk \(|x|\le x_*\). The overlap checks select one of the two fold roots as \(\alpha_h\). Away from \(x_*\), the root is simple and therefore analytic. At \(x_*\),

\[
\alpha_h(x)=\frac{p_1(x)+\sqrt{\Delta(x)}}2
\tag{21}
\]

on the branch selected by the real chain. A simple zero of \(\Delta\) makes (21) nonanalytic at \(x_*\). Thus the Taylor series at zero has radius exactly \(x_*\).

## 4. Coefficient asymptotics without an unexamined transfer step

The certified sign chain identifies \(\alpha_h\) as the upper real fold root. Taylor expansion of \(F\) at the double zero, using \(q=2\sqrt x\), gives

\[
\alpha_h(x)
=\alpha_*+
\kappa\sqrt{x_*-x}
+c_1(x_*-x)
+c_2(x_*-x)^{3/2}
+O((x_*-x)^2),
\tag{22}
\]

where

\[
\kappa^2=
\frac{4F_q(\alpha_*,q_*)}
{q_*F_{\alpha\alpha}(\alpha_*,q_*)},
\qquad \kappa>0.
\tag{23}
\]

Compactness of the certified cells on the circle away from \(x_*\), together with the local fold square, supplies an open neighborhood of the circle cut to the right of \(x_*\). After \(z=x/x_*\), this contains a standard dented neighborhood of \(z=1\). No other point on \(|z|=1\) is singular.

For \(n\ge1\), the generalized binomial identity is

\[
[z^n](1-z)^{1/2}
=(-1)^n\binom{1/2}{n}
=\frac{\Gamma(n-1/2)}
{\Gamma(-1/2)\Gamma(n+1)}.
\tag{24}
\]

Since \(\Gamma(-1/2)=-2\sqrt\pi\), the Gamma-ratio expansion gives

\[
[z^n](1-z)^{1/2}
=-\frac1{2\sqrt\pi}\,
n^{-3/2}\bigl(1+O(n^{-1})\bigr).
\tag{25}
\]

For completeness, the remainder estimate follows directly from Cauchy’s coefficient formula. Deform the contour into the dented domain: away from \(z=1\) it may be pushed to radius \(1+\varepsilon\); on the two sides of the cut and on a circle of radius \(1/n\) around \(1\), set \(s=n(1-z)\). A term \(O((1-z)^{3/2})\) then contributes

\[
O(n^{-5/2})
\tag{26}
\]

after the contour length and \(z^{-n-1}\) factor are included. Terms analytic through \(z=1\) are pushed across the unit circle and are exponentially smaller.

Equations (22), (25), and (26) therefore give

\[
a_n=
-\frac{\kappa\sqrt{x_*}}{2\sqrt\pi}\,
x_*^{-n}n^{-3/2}
\bigl(1+O(n^{-1})\bigr).
\tag{27}
\]

The bound \(|a_nx_*^n|=O(n^{-3/2})\) proves absolute convergence at every point of \(|x|=x_*\). Radial convergence to \(\alpha_*\) and absolute convergence then give

\[
\sum_{n\ge1}a_nx_*^n=\alpha_*.
\tag{28}
\]

This independently closes the transfer step used in Claude’s corollary.

## 5. Physical factors and both momentum preimages

Retain

\[
\rho_c=\frac{2\nu}{c},\qquad
q=k\rho_c,\qquad
\alpha=-i\frac{\omega\rho_c}{c}.
\tag{29}
\]

Therefore

\[
\omega(k)=i\frac c{\rho_c}\,
\alpha_h\!\left(\frac{k^2\rho_c^2}{4}\right).
\tag{30}
\]

The branch point \(x_*\) has two momentum preimages

\[
k=\pm\frac{q_*}{\rho_c}
=\pm\frac{q_*c}{2\nu}.
\tag{31}
\]

At both points the derivative of \(k^2\rho_c^2/4\) is nonzero, so the square-root singularity persists. The frequency is

\[
\omega_*=i\alpha_*\frac{c^2}{2\nu}.
\tag{32}
\]

No viscosity, speed, Gamma, endpoint, or sign factor is absorbed in this map.

## 6. Conditional Navier–Stokes rates

Claude’s rate formulas retain their stated dependence on H1–H4. With

\[
A=\frac12+h,\qquad D=\frac12-h,
\tag{33}
\]

the inner volume factor is \(q\tau^D\), while \(u_\theta\) has amplitude \(q^{-A}\). Hence

\[
D-2A=-\frac12-3h,
\qquad
D-2A-1=-\frac32-3h,
\tag{34}
\]

which gives the displayed squared-vorticity and squared-time-derivative exponents.

For \(L^p\),

\[
1+D-pA=
\frac32-h-p\left(\frac12+h\right),
\tag{35}
\]

and the zero is

\[
p_h=\frac{3-2h}{1+2h},
\qquad
3-p_h=\frac{8h}{1+2h}>0.
\tag{36}
\]

The source paper calls \(p_h<p<3\) subcritical. Under the exact forced Navier–Stokes scaling

\[
u^{(a)}(x,t)=a\,u(ax,a^2t),
\tag{37}
\]

the norm factor is \(a^{1-3/p}\). Thus \(p=3\) is critical, \(p<3\) is supercritical, and \(p>3\) is subcritical. The numerical lower bound is unchanged; its descriptive term must be corrected.

The paper’s first proof of time-derivative nonvanishing also needs repair. H1 gives \(E(0)=0\) and \(E(X)>0\) for \(X>0\), but those facts alone do not justify

\[
(1+h)E(X,0)+O(X^{3/2})>0
\tag{38}
\]

for every sufficiently small \(X\). The needed interior point follows without an axis lower bound. For any \(b>0\), define

\[
B(X)=X^AE(X,0),\qquad B(0)=0.
\tag{39}
\]

The mean value theorem supplies \(X_0\in(0,b)\) with

\[
B'(X_0)=b^{A-1}E(b,0)>0.
\tag{40}
\]

Since

\[
B'(X)=X^{A-1}\bigl(AE(X,0)+XE_X(X,0)\bigr),
\tag{41}
\]

the coefficient

\[
\mathcal H(X,\eta)=
\frac{AE+XE_X+D\eta E_\eta}{1-2h\eta^2}
\tag{42}
\]

is positive at \((X_0,0)\). Continuity gives the positive rectangle needed for integration. This repairs the argument using H1 itself; it does not prove H1 or construct the profile.

Finally, the viscosity map

\[
u_\nu(x,t)=\sqrt\nu\,u(x/\sqrt\nu,t)
\tag{43}
\]

gives, with the complete Jacobian,

\[
\|\operatorname{curl}u_\nu\|_2^2
=\nu^{3/2}\|\operatorname{curl}u\|_2^2,
\qquad
\|\partial_tu_\nu\|_2^2
=\nu^{5/2}\|\partial_tu\|_2^2.
\tag{44}
\]

The finite magnetic time integral uses the full forced energy estimate and the identity \(\|\operatorname{curl}u\|_2=\|\nabla u\|_2\) for divergence-free compactly supported fields. It does not follow from the lower rate alone.

## Findings and propagation

The re-audit confirms the central spectral additions and the coefficient corollary. Four repairs remain attached to the preserved Claude source:

1. exact Cauchy-circle coverage uses Arb enclosures of \(\pi\);
2. the Krawczyk preconditioner is complex and nonzero, rather than real;
3. the range \(p_h<p<3\) is supercritical;
4. the time-derivative coefficient follows from the mean value theorem, rather than the unproved small-\(X\) comparison in (38).

None of these repairs establishes H1–H4. The curvature and norm results remain conditional on those source statements, and the global forced Navier–Stokes singularity theorem remains unverified.
