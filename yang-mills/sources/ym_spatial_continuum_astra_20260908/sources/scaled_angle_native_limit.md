# Fixed-box native angle scaled as theta_g = g tau

This note proves the finite spatial regulator limit of the actual vacuum native state when the background angle is \(\theta_g=g\tau+o(g)\), with \(L\ge2\), \(a>0\), and fixed nonzero real \(\tau\). It is a fixed-box theorem; no interchange with \(L\to\infty\) is asserted.

## 1. Exact finite operator and chart

Keep the full physical Hamiltonian
\[
 H_g=\frac{2g^2}{a}H_0+\frac{1}{2g^2a}W,\qquad
 H_0=\sum_eE_e,\quad E_e=-\sum_{\alpha=1}^3X_{e,\alpha}^2,
\]
with every edge and face, and let \(\psi_g\) be its strictly positive unit physical vacuum. Let \(K_\theta\) be the exact independent conjugacy twirl on the \(m=4L^2(2L+1)\) direction-one edges with \(n_2\ne0\), as in (452), and put \(\chi_{\theta,g}=K_\theta\psi_g-c_{\theta,g}\psi_g\), \(c_{\theta,g}=\langle\psi_g,K_\theta\psi_g\rangle\).

Use the exact maximal-tree, chord, logarithm and Haar-density isometry \(\mathcal B_g\) of (194)--(197), followed by \(x=G^{1/2}Oz\) in every colour. Write \(R=T^*G^{-1/2}O\), an isometry from chord modes onto the original transverse edge space. The actual-vacuum theorem gives
\[
 f_g:=\mathcal B_g\psi_g\to\Phi_0,\qquad
 \Phi_0(z)=\prod_\nu(\sigma_\nu/4\pi)^{3/4}e^{-\sigma_\nu|z_\nu|^2/8}
\]
strongly in \(L^2\), together with convergence of every fixed finite physical spectral projection and of the required weighted graph vectors.

For each twirled edge let \(\eta_e(q)=n_2\,\operatorname{Ad}_{q_e}T_3\) for direction one and \(\eta_e=0\) otherwise. Since \(H_c=-2T_3\) and \(h_e=\exp(-\theta n_2H_c)=\exp(2\theta n_2T_3)\), the inverse translated link is
\[
 (h_e^q)^{-1}U_e=\exp(-2\theta n_2\operatorname{Ad}_{q_e}T_3)U_e.
\]
Thus the tangent displacement in original edge coordinates is \(-2\tau\eta(q)\) when \(\theta_g/g\to\tau\). The transverse chord displacement is exactly
\[
 \delta(q):=-2\tau R^*\eta(q). \tag{S1}
\]
The sign follows from the inverse left action.

## 2. Strong convergence of the twirl, including tails

Let \(u\in C_c^\infty(\mathbb R^{3r})\) be invariant under the residual simultaneous adjoint color rotation; such functions form a dense physical core. For each fixed \(q\), apply the exact inverse chart to the configuration with tree links equal to the identity and chord links \(Z=\exp(gG^{1/2}Oz)\). Every translated chord word is a product of finitely many links. Bi-invariance of the SU(2) metric and \(d(\exp(Y),I)\le |Y|\) give, uniformly in \(q\) and on the support of \(u\),
\[
 z'_g(z,q)=z+\delta(q)+o(1),\qquad
 \partial_z^\alpha z'_g(z,q)\to\partial_z^\alpha(z+\delta(q)). \tag{S2}
\]
The exact words retain all source/target tree factors; the only first-order term is the edge displacement \(-2\tau\eta\), transported by \(R^*\). Haar factors satisfy
\(\mathcal J(gG^{1/2}Oz)^{1/2}/\mathcal J(gG^{1/2}Oz'_g)^{1/2}\to1\)
uniformly on this compact set.

The same word estimate supplies tails rather than merely local convergence. A path through the rooted box has at most \(6L\) tree links, so each chord word in (194) has at most \(\ell_*:=12L+1\) factors. Every translated factor has \(d(h_e^q,I)\le2|g\tau+o(g)|L\). Hence, with \(C_L^{\rm edge}:=2L\ell_*\), bi-invariance gives a uniform word displacement at most \(C_L^{\rm edge}|g\tau+o(g)|\). If \( |z|\le R\), the unshifted chord logarithms are bounded by \(g\|G^{1/2}\|R\), and the translated ones by \(g(\|G^{1/2}\|R+C_L^{\rm edge}(|\tau|+1))\) for small \(g\). The inverse translation has the same bound. Since \(R^*\) is an isometry and \(\|G^{-1/2}\|\) is fixed, this gives a common rescaled support ball of radius \(C(R+1)\), uniformly in \(q\). Thus the exact twirl of \(\mathcal B_g^*u\) has compact support independent of sufficiently small \(g\). Dominated convergence in the finite Haar average proves
\[
 \mathcal B_gK_{\theta_g}\mathcal B_g^*u\to A_\tau u,\qquad
 (A_\tau u)(z)=\int u(z+\delta(q))\,dq \tag{S3}
\]
in \(L^2\). This uses the original-chart pullback and word tails; it does not assert that a fixed-\(q\) quotient pullback is a contraction.

The operators \(K_{\theta_g}\) are self-adjoint positive contractions on the exact physical Hilbert space. Choose smooth compact cutoffs \(u_R\) with \(u_R\to\Phi_0\) in Gaussian graph norm. The contraction bounds, (203), and (S3), first with fixed \(R\) and then with \(R\to\infty\), imply
\[
 \mathcal B_gK_{\theta_g}\psi_g\to A_\tau\Phi_0\quad\hbox{strongly},\qquad
 c_{\theta_g,g}\to c_\tau:=\langle\Phi_0,A_\tau\Phi_0\rangle. \tag{S4}
\]
Consequently
\[
 \mathcal B_g\chi_{\theta_g,g}\to w_\tau:=A_\tau\Phi_0-c_\tau\Phi_0,\quad
 d_{\theta_g,g}:=\|\chi_{\theta_g,g}\|^2\to d_\tau=\|w_\tau\|^2. \tag{S5}
\]

## 3. Exact Gaussian translation and centered spectral kernel

Define \(\beta(q)=-\sqrt{\Lambda/8}\,\delta(q)\), where \(\Lambda=\operatorname{diag}(\sigma_\nu)\) acts on each colour. Translation of the product Gaussian is the coherent vector
\[
 U_{\delta(q)}\Phi_0(z):=\Phi_0(z+\delta(q)),\qquad
 U_{\delta(q)}\Phi_0=e^{-\|\beta(q)\|^2/2}\sum_{N\in\mathbb N^{3r}}
 \frac{\beta(q)^N}{\sqrt{N!}}\Phi_N . \tag{S6}
\]
The oscillator excitation energy of \(\Phi_N\) is
\(E_N=\sum_{\nu,\alpha}\sigma_\nu N_{\nu\alpha}/a\). Therefore the uncentered limiting spectral measure of \(A_\tau\Phi_0\) is
\[
 \widetilde\mu_\tau=\sum_N |b_N(\tau)|^2\delta_{E_N},\qquad
 b_N(\tau)=\int e^{-\|\beta(q)\|^2/2}\frac{\beta(q)^N}{\sqrt{N!}}\,dq. \tag{S7}
\]
The centered measure is
\[
 \mu_\tau=\widetilde\mu_\tau-c_\tau^2\delta_0,\qquad
 c_\tau=b_0(\tau)=\int e^{-\|\beta(q)\|^2/2}dq. \tag{S8}
\]
The subtraction is exact because all nonzero oscillator levels are orthogonal to \(\Phi_0\). Its total mass is
\[
 d_\tau=\iint e^{-\frac1{16}(\delta(q)-\delta(q'))^T\Lambda(\delta(q)-\delta(q'))}dq\,dq'-c_\tau^2. \tag{S9}
\]
The exact two-twirl Euclidean-time kernel, for \(t\ge0\), is
\[
 \langle A_\tau\Phi_0,e^{-tA_{\rm osc}}A_\tau\Phi_0\rangle
 =\iint\exp\!\left[-\frac{\|\beta(q)\|^2+\|\beta(q')\|^2}{2}
 +e^{-t\Lambda/a}\beta(q)\!\cdot\!\beta(q')\right]dq\,dq'. \tag{S10}
\]
For the centered state subtract \(c_\tau^2\). These formulas retain all modes and colours.

If \(\tau\ne0\), then \(d_\tau>0\). The random vector \(R^*\eta(q)\) is not almost surely constant: vary one independent \(q_e\) on an edge with \(n_2\ne0\), and pair with a plaquette curl containing that edge; the transverse projection cannot vanish for every such variation. Hence \(\beta\) is nonconstant and strict Cauchy--Schwarz in (S9) gives \(d_\tau>0\). Equivalently, reflection invariance kills linear coefficients while
\[
 \sum_{\nu,\alpha}|b_{2e_{\nu\alpha}}|^2>0,
\]
because \(\int\|\Lambda^{1/2}R^*\eta(q)\|^2dq>0\). For \(\tau=0\), \(A_0=I\), \(w_0=0\).

## 4. Transfer of the full physical spectral measure

Let \(A_g=H_g-E_g\). Fixed-box spectral-projection convergence from Section 17 applies to bounded intervals whose boundaries avoid the oscillator eigenvalues. Combining it with (S5), for every bounded continuous \(F\) on \([0,\infty)\),
\[
 \langle\chi_{\theta_g,g},F(A_g)\chi_{\theta_g,g}\rangle
 \longrightarrow\int F(\lambda)\,d\mu_\tau(\lambda). \tag{S11}
\]
First use a finite oscillator spectral cutoff, where projection convergence is in norm and vectors converge strongly; bound the complementary vector norm by the coherent Gaussian tail uniformly in \(q\), and send the cutoff to infinity. For \(F\equiv1\) this is (S5), so normalized native probabilities converge weakly to \(\mu_\tau/d_\tau\) whenever \(\tau\ne0\). Every finite oscillator interval has the exact mass obtained by summing (S7)--(S8), and some finite positive level has nonzero mass whenever \(\tau\ne0\). No simultaneous infinite-volume conclusion is made.

