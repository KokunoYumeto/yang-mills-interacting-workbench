## 26.10 Prescribed paths: the centered fourth and sixth remainders remain volume uncontrolled

This note isolates what the exact centered spin expansion and the proved
actual-vacuum moments do, and do not, imply on the two prescribed coupling
paths.  The state is always the positive ground vector of the full finite-box
Hamiltonian; no Gaussian replacement is made.

Write
\[
 v_\Gamma=(\Gamma-\langle\Gamma\rangle_\psi)\psi,
 \qquad
 \chi_\theta=P_\psi^\perp(K_\theta-I)\psi .
\]
The exact joint-spin expansion gives
\[
 \chi_\theta=-\frac23\theta^2v_\Gamma+P_\psi^\perp R_{4,\theta}\psi,
 \qquad
 \|R_{4,\theta}\psi\|\le\frac29\theta^4\|\Gamma^2\psi\| .
 \tag{P1}
\]
The centered fourth coefficient is more precise blockwise:
\[
 r_\theta=\frac29\theta^4\gamma^2
 -\frac4{45}\theta^4\sum_e n_2^4\lambda_e^2
 -\frac2{45}\theta^4\sum_e n_2^4\lambda_e+R_{6,\theta},
 \tag{P2}
\]
where the deterministic part of the first term disappears under
\(P_\psi^\perp\), but the variance of \(\Gamma^2\), the two diagonal spin
terms, and the sixth remainder remain.  Thus (1) is a valid graph estimate,
while replacing its \(\Gamma^2\)-norm by the variance of \(\Gamma\) is not a
consequence of scalar variance alone.

For the original regulator take \(L=j^2\), \(a=(100j)^{-1}\), and
\(\theta_j=2\pi/(10^4j^2D_j)\), with \(D_j=j^4+O(j^2)\).  Hence
\(\theta_j\asymp j^{-6}\).  Put
\[
 M=12L^2(2L+1),\qquad
 A_L=\frac{4L^2(2L+1)}3(4L^2+2L+1).
\]
The exact covariance estimate from the actual vacuum is
\[
 \|v_\Gamma\|\ge
 \frac{\sqrt\xi\,A_L^2}{720L^2M^2\sqrt r},
 \qquad r=1+\frac1{2L},\qquad \sqrt\xi=\frac1{2g^2},
 \tag{P3}
\]
provided \(6g^2\sqrt r\,L^2M\le A_L/2\).  This condition holds eventually on
both prescribed paths, since its left/right ratio is \(O(g^2)\).

The proved fourth electric moment estimate (the preceding (C_2(L,a)) bound)
gives
\[
 \|\Gamma^2\psi\|\le16L^4C_2(L,a)g^{-4},
 \tag{P4}
\]
with that explicit \(C_2\).  Along the displayed regulator,
\(K=3\sqrt{NM}/a=O(L^{7/2})\), \(a=O(L^{-1/2})\), and the exact recurrence
for \(B_4\) gives \(C_2(L,a)=O(L^6)\).  Combining (1), (3), and (4), the
certified relative fourth-order error obeys
\[
 \frac{\|P_\psi^\perp R_{4,\theta_j}\psi\|}
      {(2/3)\theta_j^2\|v_\Gamma\|}
 \le
 7680\,\frac{\theta_j^2L^6M^2C_2(L,a)\sqrt r}{A_L^2}\,g^{-2}
 =O(j^4g^{-2}).
 \tag{P5}
\]
The power follows from \(L^6M^2C_2/A_L^2=O(L^8)=O(j^{16})\) and
\(\theta_j^2=O(j^{-12})\).  Consequently, on
\[
 g_j^2=\frac1{\log j},
 \qquad\text{or}\qquad
 g_j^2=\frac{\kappa_*}{200j},
 \tag{P6}
\]
the right side of (5) is respectively \(O(j^4\log j)\) and
\(O(j^5)\).  Both diverge.  Therefore the available exact bounds do not
prove that the centered fourth term is small relative to the covariance term;
they become quantitatively vacuous precisely in the simultaneous
volume/coupling limits under consideration.

The sixth term is strictly less controlled.  Taylor's scalar remainder is of
order \(\theta^6\gamma^3\) on a spin block, so a global estimate requires a
uniform bound for \(\|\Gamma^3\psi\|\) (and the centered diagonal terms in (2)
require corresponding mixed moments).  The recurrence for moments of \(W\)
at a fixed box supplies finite constants for every fixed order, but its
constants grow with \(L\); it supplies no volume-uniform concentration of the
joint-spin coefficients.  In particular, a bound on \(\operatorname{Var}(\Gamma)\)
alone cannot control \(\operatorname{Var}(\Gamma^2)\) or the sixth moment:
probability measures with the same second moment can have arbitrarily large
fourth and sixth moments.  Hence the exact cancellation in (2) does not close
without a new, volume-uniform weighted fourth/sixth-moment theorem for the
actual interacting vacuum.

This is a rigorous obstruction to the prescribed-path Taylor argument, not a
claim that the native low-energy weight vanishes there.  The finite-box
scaled-angle theorem and the selected original-cusp sequence remain valid,
while nonzero native low-energy weight on either path and an interacting
four-dimensional continuum remain unproved.
