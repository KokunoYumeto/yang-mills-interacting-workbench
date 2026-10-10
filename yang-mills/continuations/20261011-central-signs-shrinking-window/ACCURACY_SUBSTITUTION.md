# Receiving accuracy for the original shrinking window

This is a calculation from already published PK216, PK220–PK222 and PK227,
not a positive-weight claim or a replacement for evaluating the actual
matrices. The current public proof is pinned at
485b61423c1f4e1805deb453c1b6b342b27842b6.

Keep the original path
\[
 L_j=j^4,\quad a_j=\frac1{100j},\quad
 g_j^2=\frac{\kappa_*}{200j},\quad \kappa_j=\kappa_*>0,\quad
 M_j=24j^{12}+12j^8,\qquad s_j=\frac{\kappa_*}{j}.
\]
Choose any stated finite degree \(R_j\) and retain the original coefficient
vector \(c_j\). No coefficient or physical state is rescaled. Set
\[
 D_j=1+\|c_j\|^2,\quad
 \varepsilon_j=\frac1{2j^3Z_{R_j}D_j},\quad
 \delta_j=\frac1{2j^3D_j},
\]
using exactly the \(Z_{R_j}\), \(A_{R_j}\), \(T_{R_j}\), original word
coefficients \(U_a,V_a,W_a\) and summation range of PK217–PK222. In particular,
\[
 \Omega_j=\frac{320000\pi j^2M_j}{\kappa_*^2},\quad
 \delta_{{\rm v},j}=3\kappa_*e^{-\Omega_j},\quad
 \overline E_j=\ell_j=\frac{20000j^2M_j}{\kappa_*},
\]
and the unchanged cutoff formula receives the new accuracy:
\[
 \Lambda_j=
 1+\left\lceil\max\left\{3,
 \frac{\overline E_j+
       \ell_j^2/(\delta_{{\rm v},j}\varepsilon_j^2)}{\kappa_*}
                      \right\}\right\rceil.
\]
PK216 gives \(\eta\leq\varepsilon_j^2\) and
\(w\leq\delta_{{\rm v},j}\varepsilon_j^2\). Thus PK220 gives
\(E_{R_j}\leq\varepsilon_jT_{R_j}\). The three errors in PK221 are at most
\[
 2\varepsilon_j\sum_aU_a^2,\qquad
 2\kappa_*\varepsilon_j\sum_aV_a^2,\qquad
 2A_{R_j}\varepsilon_jT_{R_j}
                 +\varepsilon_j^2T_{R_j}^2.
\]
Since \(0<\varepsilon_j\leq1\), each is at most
\(\varepsilon_jZ_{R_j}=\delta_j\). Consequently the complete raw
PK227 certificate is
\[
 \nu_{c_j}((0,s_j])\geq
 \max\left\{0,\
 c_j^*\left(\mathcal G^{\Lambda_j}_{R_j}
                 -\frac{\mathcal C^{\Lambda_j}_{R_j}}{\kappa_*/j}\right)c_j
 -\frac{\|c_j\|^2}{2j^3(1+\|c_j\|^2)}
                     \left(1+\frac{j}{\kappa_*}\right)\right\}.
\]
All coefficients and both matrix terms are retained. Its entire
approximation loss is at most
\[
 \frac1{2j^3}+\frac1{2\kappa_*j^2}\longrightarrow0,
\]
even when the original coefficient norms are unbounded. This is achieved
by increasing the electric cutoff, not by changing the state.

For the original first polynomial \(P_{10}=x-y\) and its coefficient
\(c_j=(1)\), the target expression remains the exact PK202 expression
\[
 2\beta_{0,j}^2(\mathcal Q_{4,j}-\mathcal Q_{4,\mathcal R,j})
 -\frac{2\kappa_*\beta_{0,j}^2
                  (\mathcal K_{1,j}-\mathcal K_{\mathcal R,j})}{\kappa_*/j}.
\]
The symbols denote the complete original four-loop and gradient
differences of PK202, including reflection, all repeated words and the
actual interacting vacuum. Here \(D_j=2\), so the explicit certificate's
loss is
\(\frac1{4j^3}+\frac1{4\kappa_*j^2}\).
The full \(H-E_{0,j}\) operator and complementary residual in PK223–PK225
remain the spectral objects.

This finishes the accuracy substitution only. The displayed actual
four-loop/gradient difference has not been proved positive in the
shrinking window. The next substantive calculation must evaluate or
bound that difference; another cutoff statement alone will not do so.
