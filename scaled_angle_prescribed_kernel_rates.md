## 26.13 Exact prescribed-path rates for the fixed-box oscillator kernel

This source derives only the exact finite-box Gaussian scaled-angle kernel from Sections 26.9, 26.11 and 26.12. It does not identify that kernel with the simultaneous exact interacting lattice state.

## Data retained exactly

Set \(L_j=j^2\), \(a_j=(100j)^{-1}\),
\[
 c_*:=\frac{2\pi}{10^4},\qquad
 D_j=L_{j^2}q_{j^2}+6m_{j^2}^2,\qquad
 \theta_j=\frac{c_*}{j^2D_j},
\]
so the proved cusp asymptotic is \(D_j/j^4\to1\). Let
\[
 Q_L:=\operatorname{tr}(\Lambda D\Lambda D),
 \qquad
 C_L^\Gamma=\frac3{32}Q_L.
\]
The exact bounds already proved in Sections 24--26 imply
\[
 \frac{128}{297}L^7\le Q_L\le264L^7. \tag{PK1}
\]
The exact small-angle bound in Section 26.12 uses
\[
 U_L=4\sqrt{12}\,S_{2,L}
 =\frac{16\sqrt3}{3}L^2(L+1)(2L+1)^2,
\]
therefore \(U_L/L^5\to64\sqrt3/3\).

For any \(\tau\in\mathbb R\), put \(t=\tau^2\). The sign-controlled cosh identity gives the exact two-sided inequality
\[
 e^{-tU_L/8}\frac{t^2Q_L}{128}
 \le d_{L,\tau}
 \le\frac{t^2Q_L}{128}. \tag{PK2}
\]
Thus, for \(\tau\ne0\), \(d_{L,\tau}>0\), and with \(x=tU_L/8\),
\[
0\le1-\frac{d_{L,\tau}}{t^2Q_L/128}
 \le1-e^{-x}\le x. \tag{PK3}
\]

## Substitution along the two prescribed paths

Use the ideal oscillator parameter \(\tau_j=\theta_j/g_j\), with \(g_j>0\). Since \(L_j^7=j^{14}\), (PK1)--(PK2) give the exact finite-\(j\) bounds
\[
 e^{-x_j}\,\frac{c_*^4g_j^{-4}j^6}{297D_j^4}
 \le d_{L_j,\tau_j}
 \le \frac{33}{16}\,\frac{c_*^4g_j^{-4}j^6}{D_j^4},
 \qquad
 x_j:=\frac{\theta_j^2U_{L_j}}{8g_j^2}. \tag{PK4}
\]
No replacement \(D_j=j^4\) is made in (PK4). Also
\[
 x_j=\frac{2\sqrt3}{3}\,
 \frac{c_*^2(L_j+1)(2L_j+1)^2}{D_j^2g_j^2}. \tag{PK5}
\]

### Logarithmic path

For \(g_j^2=1/\log j\), (PK5) and \(D_j/j^4\to1\) give
\[
 x_j=\frac{8\sqrt3}{3}c_*^2\frac{\log j}{j^2}(1+o(1))
 \longrightarrow0. \tag{PK6}
\]
Consequently (PK3)--(PK4) prove the relative oscillator-kernel estimate
\[
 d_{L_j,\tau_j}
 =\frac{c_*^4(\log j)^2j^6}{128D_j^4}Q_{L_j}
 \,[1+O(\log j/j^2)], \tag{PK7}
\]
where the \(O(\cdot)\) is an explicit one-sided bound from (PK3). Using only (PK1), the strongest asymptotic constants currently justified are
\[
 \frac{c_*^4}{297}
 \le\liminf_{j\to\infty}\frac{j^{10}d_{L_j,\tau_j}}{(\log j)^2},
 \qquad
 \limsup_{j\to\infty}\frac{j^{10}d_{L_j,\tau_j}}{(\log j)^2}
 \le\frac{33}{16}c_*^4. \tag{PK8}
\]
The bounds are strict-positive at every finite \(j\) and show \(d_{L_j,\tau_j}=\Theta\big(j^{-10}(\log j)^2\big)\) in the two-sided-bound sense.

### Fixed-electric-coefficient path

For \(g_j^2=\kappa_*/(200j)\), with fixed \(\kappa_*>0\), (PK5) gives
\[
 x_j=\frac{1600\sqrt3}{3\kappa_*}c_*^2\frac1j(1+o(1))
 \longrightarrow0. \tag{PK9}
\]
The exact relative estimate and (PK1) imply
\[
 d_{L_j,\tau_j}
 =\frac{40000c_*^4j^8}{128\kappa_*^2D_j^4}Q_{L_j}
 \,[1+O(1/j)], \tag{PK10}
\]
and hence
\[
 \frac{40000c_*^4}{297\kappa_*^2}
 \le\liminf_{j\to\infty}j^8d_{L_j,\tau_j},
 \qquad
 \limsup_{j\to\infty}j^8d_{L_j,\tau_j}
 \le\frac{82500c_*^4}{\kappa_*^2}. \tag{PK11}
\]
Here \(82500=40000\cdot(264/128)=40000\cdot(33/16)\). Thus \(d_{L_j,\tau_j}=\Theta(j^{-8})\) for this oscillator kernel in the two-sided-bound sense.

## What this does and does not prove for the exact lattice

Equations (PK4)--(PK11) are exact finite-box/oscillator conclusions. They prove positivity and the leading small-\(\tau_j\) scaling after taking the fixed-box \(g\to0\) limit. They do **not** imply the same estimates for the exact positive-vacuum vector at the simultaneous pair \((L_j,g_j)\): (S11) is pointwise in fixed \(L,a\), with no rate uniform in \(L\), while \(L_j\to\infty\) and \(g_j\to0\) together. In particular, no bound currently controls the difference between the exact normalized native spectral measure and the oscillator measure after division by the vanishing mass \(d_{L_j,\tau_j}\). The independent centered Taylor estimate (P5) is volume-vacuous, \(O(j^4\log j)\) and \(O(j^5)\), and the sixth/mixed moments have no volume-uniform bound. Thus the new cosh inequality closes the oscillator-kernel relative error but leaves the simultaneous exact-lattice and interacting-continuum bridge obstructed by the missing uniform fixed-box convergence rate.

This is a precise obstruction, not a claim that either prescribed path has zero native low-energy weight.
