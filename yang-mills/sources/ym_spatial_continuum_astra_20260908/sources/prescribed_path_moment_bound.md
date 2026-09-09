# A uniform fourth electric moment bound for the actual finite-box vacuum

This continuation records a bound needed when testing the original angle on prescribed coupling paths. It is a fixed finite box statement, with every constant and the original Hamiltonian retained. It does not assert a volume-uniform continuum estimate.

Fix \(L\ge2\), \(a>0\), \(0<g\le1\), and use
\[
 H=\kappa H_0+bW,\quad \kappa=2g^2/a,\quad b=(2g^2a)^{-1},
\quad W=\sum_p(2-\operatorname{tr}U_p),\quad 0\le W\le4M .
\]
Let \(\psi\) be the actual positive unit vacuum, \(H\psi=E\psi\), \(E\le K=3\sqrt{N_EM}/a\). The moment recurrence already proved for this same state is
\[
 \langle W^n\rangle_\psi\le B_n(K)g^{2n},\qquad
 B_0=1,\ B_1=2aK,\ B_{n+1}=2aK B_n+16n^2B_{n-1}.
 \tag{PM1}
\]
In particular \(B_2=x^2+16\) and \(B_4=x^4+224x^2+2304\), \(x=2aK\).

The eigen-equation is an equality of smooth functions:
\[
 H_0\psi=f\psi,\qquad f=(E-bW)/\kappa. \tag{PM2}
\]
Applying \(H_0\) once more and using \(E_e=-\sum_\alpha X_{e,\alpha}^2\) gives the exact product identity
\[
 H_0^2\psi=f^2\psi-\frac b\kappa[H_0,W]\psi,\qquad
 [H_0,W]\psi=(H_0W)\psi-2\sum_{e,\alpha}(X_{e,\alpha}W)(X_{e,\alpha}\psi).
 \tag{PM3}
\]
The sign follows by expanding \(H_0(f\psi)=fH_0\psi+(H_0f)\psi-2\sum(Xf)(X\psi)\), with \(H_0f=-(b/\kappa)H_0W\) and \(Xf=-(b/\kappa)XW\).

Every fundamental face trace is an \(H_0\)-eigenfunction with eigenvalue \(3\). Hence
\[
 H_0W=3W-6M. \tag{PM4}
\]
The exact full-face gradient estimate is \(\sum_{e,\alpha}|X_{e,\alpha}W|^2\le16W\). Since \(\langle H_0\rangle_\psi=(E-b\langle W\rangle_\psi)/\kappa\le E/\kappa\), Cauchy--Schwarz and (PM1) imply
\[
\begin{aligned}
\|[H_0,W]\psi\|
&\le3\|W\psi\|+6M
 +2\Big(\int|\nabla W|^2\psi^2\Big)^{1/2}
       \Big(\int|\nabla\psi|^2\Big)^{1/2}\\
&\le3\sqrt{B_2(K)}\,g^2+6M+8aK=:C_{LW}(L,a).
\end{aligned}\tag{PM5}
\]
Indeed the product under the square root is at most
\((16B_1(K)g^2)(Ka/(2g^2))=16aK\,B_1(K)/2\le16a^2K^2\), and the prefactor \(2\) gives \(8aK\) after using \(B_1=2aK\). (Keeping the unsimplified product gives the same displayed bound.)

For real \(r,s\), \((r+s)^4\le8(r^4+s^4)\). Therefore (PM1)--(PM2) give
\[
\|f^2\psi\|
\le\frac{\sqrt{8(K^4+b^4B_4(K)g^8)}}{\kappa^2}
=\frac{a^2}{4g^4}
\sqrt{8\left(K^4+\frac{B_4(K)}{16a^4}\right)}.
\tag{PM6}
\]
Combining (PM3), (PM5), and \(b/\kappa=1/(4g^4)\) proves the explicit actual-vacuum bound
\[
\boxed{\ \|H_0^2\psi\|\le C_2(L,a)\,g^{-4},\quad
C_2(L,a)=\frac{a^2}{4}\sqrt{8\left(K^4+\frac{B_4(K)}{16a^4}\right)}
+\frac14C_{LW}(L,a).\ }\tag{PM7}
\]
No replacement state or unlisted boundary face is used.

Finally \(\Gamma=\sum_{(n,1)}n_2^2E_e\) is a positive joint spectral multiplier of the commuting edge Casimirs and \(0\le n_2^2\le4L^2\). The joint spectral theorem gives
\[
\|\Gamma^2\psi\|\le16L^4\|H_0^2\psi\|
\le16L^4C_2(L,a)\,g^{-4}. \tag{PM8}
\]
This is sharper in \(g\) than the earlier \(g^{-7}\) estimate at each fixed box. Its explicit \(L,a\)-dependence still grows with the regulator, so PM8 alone does not prove the prescribed logarithmic or fixed-electric-coefficient continuum path. It is an exact input for the centered spin/remainder estimate now under construction.
