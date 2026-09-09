# Exact finite-box small-angle expansion of the centered Gaussian native mass

This is a fixed-box consequence of the exact Gaussian kernel in Section 26.9. Fix \(L\ge2\) and \(a>0\), and write \(\delta(q)=\tau d(q)\), where \(d(q)=-2R^*\eta(q)\). Put
\[
u(q)=d(q)^{\mathsf T}\Lambda d(q),\quad z(q,q')=d(q)^{\mathsf T}\Lambda d(q'),\quad \mu=\mathbb E u,\quad \nu=\mathbb E u^2,\quad \zeta=\mathbb E z^2.
\]
Since \(R^*\) has operator norm \(1\), \(\|\Lambda\|<\sqrt{12}\), and
\(\sum_{e=(n,1)}n_2^2=:S_{2,L}=\frac23L^2(L+1)(2L+1)^2\), we may take the
fully explicit bound
\[
 U_L:=4\sqrt{12}\,S_{2,L},
\]
so \(0\le u\le U_L\), \(|z|\le U_L\), and
\(0\le u(q)+u(q')-2z(q,q')\le4U_L\). For \(x\ge0\), \(|e^{-x}-(1-x+x^2/2)|\le x^3/6\). Applying this bound to the two-twirl kernel and to \(c(\tau)=\mathbb E e^{-\tau^2u/16}\), uniformly for \(|\tau|\le1\), gives
\[
J(\tau)=1-\frac{\mu}{8}\tau^2+\frac{\nu+\mu^2+2\zeta}{256}\tau^4+R_J,
\qquad |R_J|\le\frac{U_L^3}{384}|\tau|^6,
\]
\[
c(\tau)=1-\frac{\mu}{16}\tau^2+\frac{\nu}{512}\tau^4+r_c,
\qquad |r_c|\le\frac{U_L^3}{24576}|\tau|^6.
\]
Writing \(a_0=\mu/16\), \(b_0=\nu/512\), and \(R_c=U_L^3/24576\), direct multiplication yields
\[
\left|c(\tau)^2-\left(1-2a_0\tau^2+(a_0^2+2b_0)\tau^4\right)\right|
\le C_{c,L}|\tau|^6,
\]
where \(C_{c,L}=2a_0b_0+b_0^2+2(1+a_0+b_0)R_c+R_c^2\). Therefore
\[
d_{L,\tau}=J(\tau)-c(\tau)^2=\frac{\zeta}{128}\tau^4+R_{d,L}(\tau),
\qquad |R_{d,L}(\tau)|\le\left(\frac{U_L^3}{384}+C_{c,L}\right)|\tau|^6.
\]

All expectations use normalized product Haar probability. In the retained
\(T_\alpha\)-coordinate norm \(-2\operatorname{tr}(XY)\), \(\|T_3\|=1\);
the physical metric \(c=-\operatorname{tr}(XY)/2\) is unchanged. Haar
invariance gives covariance \(\mathbb E[(\operatorname{Ad}_qT_3)_\alpha(\operatorname{Ad}_qT_3)_\beta]=\delta_{\alpha\beta}/3\). Thus each colour block of \(d\) has covariance \((4/3)D\); summing the
three colour blocks, whose cross-colour covariances vanish, gives
\[
\zeta=\frac{16}{3}\operatorname{tr}(\Lambda D\Lambda D).
\]
Consequently
\[
\boxed{d_{L,\tau}=\frac{\tau^4}{24}\operatorname{tr}(\Lambda D\Lambda D)+R_{d,L}(\tau)},
\qquad |R_{d,L}(\tau)|\le\left(\frac{U_L^3}{384}+C_{c,L}\right)|\tau|^6.
\]
Since \(C_L^\Gamma=(3/32)\operatorname{tr}(\Lambda D\Lambda D)\), the leading term is \((4/9)\tau^4C_L^\Gamma\). On \(L_j=j^2\) and \(\theta_j\asymp j^{-6}\), its leading scale \(\tau_j^4L_j^7\) is \(O(j^{-10}(\log j)^2)\) for \(g_j^2=1/\log j\), and \(O(j^{-8})\) for \(g_j^2=\kappa_*/(200j)\). The preceding Taylor remainder is regulator-dependent. A sharper exact
finite-box identity gives a useful uniform relative statement. Choose a fixed \(r\in\mathrm{SU}(2)\) with
\(\operatorname{Ad}_rT_3=-T_3\) and right-multiply every \(q'_e\) by \(r\).
Product Haar is invariant, \(u'\) is unchanged and \(z\mapsto-z\); hence,
with \(t=\tau^2\),
\[
 d_{L,\tau}=\mathbb E\!\left[e^{-t(u(q)+u(q'))/16}
 \left(\cosh\!\frac{t\,z(q,q')}{8}-1\right)\right].
\]
Writing \(b=t(u+u')/16\) and \(v=tz/8\), Cauchy--Schwarz gives
\(|v|\le b\). Therefore
\[
 e^{-tU_L/8}\frac{t^2\zeta}{128}
 \le d_{L,\tau}\le\frac{t^2\zeta}{128},
 \qquad
 0\ge R_{d,L}(\tau)\ge
 -\frac{\tau^6U_L}{192}\operatorname{tr}(\Lambda D\Lambda D).
\]
Thus on \(L_j=j^2\), whenever \(\tau_j^2L_j^5\to0\), the oscillator kernel
satisfies
\[
 d_{L_j,\tau_j}\sim\frac{\tau_j^4}{24}
 \operatorname{tr}(\Lambda D\Lambda D).
\]
For the two retained paths this condition follows from (V11), but the
fixed-box convergence (S11) still has no uniform-in-\(L\) error. Consequently
this remains an oscillator-kernel result and gives no simultaneous exact-lattice
or interacting-continuum theorem.
