# Volume scaling of the fixed-box scaled-angle kernel

This note extracts a uniform consequence of the fixed-box limit \(\theta_g/g\to\tau\) from Section 26.9. It does not assert a joint \(L\to\infty\) theorem. All estimates below concern the exact Gaussian kernel obtained after the fixed-box limit.

Let \(P=\mathscr R\mathscr R^{\mathsf T}\) and \(K=\mathscr R\Lambda\mathscr R^{\mathsf T}\), acting separately on each of the three colour components. Thus \(0\le K\le\sqrt{12}\,P\), and \(\operatorname{tr}(KW)=3\operatorname{tr}(\Lambda D)\), where \(W=\operatorname{diag}(n_2^2)\) on direction-one edges. Write
\[
 \eta(q)=\sum_e n_2\,\operatorname{Ad}_{q_e}T_3\,\mathbf e_e,
 \qquad Y_\tau(q)=\delta(q)^{\mathsf T}\Lambda\delta(q)
        =4\tau^2\eta(q)^{\mathsf T}K\eta(q).
\]
All expectations below use normalized product Haar probability. With the normalization \(\|T_3\|=1\), Haar invariance gives
\[
 \mathbb E\eta_e=0,
 \qquad \mathbb E(\eta_{e,\alpha}\eta_{e,\beta})
     =\frac{n_2^2}{3}\,\delta_{\alpha\beta},
 \qquad \|\eta_e\|^2=n_2^2.
\]
Consequently
\[
 \mathbb E Y_\tau=4\tau^2\operatorname{tr}(\Lambda D). \tag{V1}
\]

The exact trace count from (232) and \(\sigma_\nu<\sqrt{12}\) imply
\[
 \frac{\mathcal A_L}{\sqrt{12}}\le \operatorname{tr}(\Lambda D)
 \le\sqrt{12}\operatorname{tr}D,
 \qquad
 \mathcal A_L=\frac{4}{3}L^2(2L+1)(4L^2+2L+1). \tag{V2}
\]
For \(L\ge2\), \(\mathcal A_L\ge(32/3)L^5\) and \(\sum_e n_2^4\le18L^7\). In particular
\[
 \mathbb E Y_\tau\ge \frac{128}{3\sqrt{12}}\tau^2L^5,
 \qquad \operatorname{tr}(\Lambda D)\le72L^5. \tag{V3}
\]

We use the following elementary quadratic-form estimate. If \(\xi_e\) are independent centred vectors with \(\|\xi_e\|^2\le w_e\), \(\mathbb E\xi_e\xi_e^{\mathsf T}=(w_e/3)I_3\), and \(0\le K\le\sqrt{12}I\), then expansion into diagonal and off-diagonal terms, followed by independence and Cauchy--Schwarz, gives
\[
 \operatorname{Var}(\sum_{e,f}\xi_e^{\mathsf T}K_{ef}\xi_f)
 \le 768\,\operatorname{tr}(K W K W)
 \le 27648\sum_e w_e^2. \tag{V4}
\]
The constant is deliberately enlarged: the first inequality uses only \(\mathbb E\|\xi_e\|^4\le w_e^2\), and the second uses \(\|K\|\le\sqrt{12}\) and \(\operatorname{tr}(W^2)=3\sum_e w_e^2\) for the three-colour block.
Applying (V4) to \(\eta\) and multiplying by \(16\tau^4\) yields
\[
 \operatorname{Var}Y_\tau\le 442368\tau^4\sum_e n_2^4
 \le 7{,}962{,}624\,\tau^4L^7. \tag{V5}
\]
Chebyshev and (V3) therefore imply, for every fixed \(\tau\ne0\),
\[
 \mathbb P\left(Y_\tau\le {1\over2}\mathbb EY_\tau\right)
 \le 10^6L^{-3}. \tag{V6}
\]

Let \(q,q'\) be independent and put \(Y_\tau^\Delta=(\delta(q)-\delta(q'))^{\mathsf T}\Lambda(\delta(q)-\delta(q'))\). The same argument applies to \(\eta(q)-\eta(q')\): its covariance is doubled and its fourth moments are at most \(16n_2^4\). Enlarging the constant in (V6) by a factor 32 gives
\[
 \mathbb P\left(Y_\tau^\Delta\le {1\over2}\mathbb E Y_\tau^\Delta\right)
 \le 3.2\cdot10^7L^{-3},
 \qquad
 \mathbb E Y_\tau^\Delta=8\tau^2\operatorname{tr}(\Lambda D). \tag{V7}
\]

The two-twirl kernel in (S9) is \(J_{L,\tau}=\mathbb E\exp(-Y_\tau^\Delta/16)\), and \(d_{L,\tau}=J_{L,\tau}-c_{L,\tau}^2\le J_{L,\tau}\). Since \(e^{-x}\le1\) and \(e^{-x}\le e^{-\mathbb EY_\tau^\Delta/32}\) on the complementary event,
\[
 J_{L,\tau}
 \le 3.2\cdot10^7L^{-3}
   +\exp\!\left[-\frac{\tau^2\operatorname{tr}(\Lambda D)}{4}\right]
 \le 3.2\cdot10^7L^{-3}+e^{-\tau^2L^5/(\sqrt{12})}. \tag{V8}
\]
Thus the fixed-\(\tau\) Gaussian native mass satisfies
\[
 d_{L,\tau}\longrightarrow0\qquad(L\to\infty,\ \tau\ne0\ \text{fixed}). \tag{V9}
\]
This is a genuine volume obstruction: the fixed-box limit has positive mass for every \(L\), but that mass is not uniformly positive in volume.

There is also a small-angle bound useful for the original cusp scales. From \(1-e^{-x}\le x\), \(c_{L,\tau}\ge1-\mathbb EY_\tau/16\), hence
\[
 d_{L,\tau}\le1-c_{L,\tau}^2
 \le\frac{\mathbb EY_\tau}{8}
 \le36\tau^2L^5. \tag{V10}
\]
On the retained sequence \(L_j=j^2\), \(\theta_j\sim(2\pi/10^4)j^{-6}\). Therefore the ideal oscillator parameter \(\tau_j=\theta_j/g_j\) obeys
\[
 \tau_j^2L_j^5=O(j^{-2}\log j)\quad(g_j^2=1/\log j),\qquad
 \tau_j^2L_j^5=O(j^{-1})\quad(g_j^2=\kappa_*/(200j)). \tag{V11}
\]
The right side of (V10) consequently tends to zero on both prescribed trajectories. Equation (V11) is an oscillator-kernel statement only; the fixed-box convergence (S11) supplies no uniform error in \(L\), so it cannot by itself be promoted to a theorem for the exact simultaneous lattice sequence. Any such promotion would require a new uniform, centred, finite-volume graph estimate.



