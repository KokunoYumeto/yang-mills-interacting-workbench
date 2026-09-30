# Exact finite angular Gram system for the retained curl fields

## Source objects and scope

The receiving source is the finite physical curl field in `moments_body.tex`, equations `nsmom:actual_amplitude` and `nsmom:actual_derivative`, together with the exact angular kernel in `evaluation_flux_body.tex`, equations `eflux:kernel`–`eflux:angular`. For every retained label,

\[
n_j=k_{\beta_j}m_jp_j\in\mathbb Z\setminus\{0\},
\qquad
\psi_j=k_{\beta_j}m_j\Phi_j-n_j\theta,
\tag{1}
\]

and \(\psi_j\) is independent of \(\theta\). The complete coefficient is

\[
\begin{aligned}
t_j&=\chi_jB_jL_jy_j,\\
c_j&=\frac{i\,n_{\Phi,j}\times t_j}
{k_{\beta_j}m_j|n_{\Phi,j}|^2},\\
b_j&=t_j+\operatorname{curl}_{*,\mathrm{coeff}}c_j,\\
d_j&=\partial_Zb_j+i(\partial_Z\psi_j)b_j.
\end{aligned}
\tag{2}
\]

Thus every cutoff, auxiliary-chain, cylindrical-basis, frame, path, and phase derivative remains inside \(b_j\) or \(d_j\). This note supplies the full finite matrix that the earlier feedback memo mentioned but did not write. It changes no source object and makes no infinite-band or endpoint assertion.

## 1. Carrier matrix, including the zero block

Let \(J\) be any finite index set, let \(n_j\in\mathbb Z\), and let \(h_j\in\mathbb C^d\). Define

\[
V_h(\theta)=\sum_{j\in J}\operatorname{Re}(h_je^{in_j\theta}).
\tag{3}
\]

For \(\ell>0\), fold positive and negative carriers into

\[
\mathcal C_\ell(h)
=\sum_{n_j=\ell}h_j+\sum_{n_j=-\ell}\overline{h_j},
\qquad
\mathcal C_0(h)=\sum_{n_j=0}\operatorname{Re}h_j.
\tag{4}
\]

Then the field itself has the exact regrouping

\[
V_h(\theta)=\mathcal C_0(h)+
\sum_{\ell\ge1}\operatorname{Re}
\bigl(\mathcal C_\ell(h)e^{i\ell\theta}\bigr).
\tag{5}
\]

For a second finite array \(g_j\), extended by zero to a common index set when necessary, angular orthogonality gives, component by component,

\[
\left\langle V_{h,a}V_{g,b}\right\rangle_\theta
=\mathcal C_{0,a}(h)\mathcal C_{0,b}(g)
+\frac12\sum_{\ell\ge1}
\operatorname{Re}\left(
\mathcal C_{\ell,a}(h)
\overline{\mathcal C_{\ell,b}(g)}\right).
\tag{6}
\]

In pairwise form the entry is

\[
K_{n,m}(x,y)=\frac12\left[
\mathbf1_{n=m}\operatorname{Re}(x\overline y)
+\mathbf1_{n=-m}\operatorname{Re}(xy)\right].
\tag{7}
\]

Equation (7) also covers \(n=m=0\): both indicators contribute, and their sum is \(\operatorname{Re}x\operatorname{Re}y\). When exactly one carrier is zero, or when \(|n|\ne|m|\), the entry is zero.

The carrier matrix is therefore block diagonal after folding by \(|n|\). Its zero block is \(\mathbf1\mathbf1^T\) acting on the real parts. Every positive absolute carrier has the matrix

\[
G^{(\ell)}=\frac12\mathbf1\mathbf1^T,
\qquad \ell\ge1,
\tag{8}
\]

acting on the folded coefficients in (4), with the real part of the Hermitian component pairing; here \(\mathbf1\) is the all-ones column whose length is the number of folded labels in that block. Each nonempty block is positive semidefinite and rank one. Equal positive carriers use \(\operatorname{Re}(x\overline y)/2\); opposite carriers use \(\operatorname{Re}(xy)/2\); every other pair is exactly zero. The source’s retained new field has no zero-carrier labels, so its zero block is absent. The old angular mean lies in that block and has zero product with every retained new label.

To prove (6), write

\[
\operatorname{Re}(xe^{in\theta})
=\frac12\left(xe^{in\theta}+\overline x e^{-in\theta}\right).
\tag{9}
\]

The four product frequencies are \(n+m,n-m,-n+m,-n-m\). Their normalized circle integrals vanish unless the frequency is zero. The surviving terms give (7), summation gives (6), and (8) follows from (4). This proves the complete matrix without an orthogonality assumption between labels sharing an absolute carrier.

## 2. Exact velocity and axial-derivative norms

Fix one retained band with

\[
0<Q\le1,\qquad A=\frac12+h,\qquad D=\frac12-h,
\qquad r=\sqrt Q\,R,\qquad z=Q^DZ.
\tag{10}
\]

For every \(\ell\ge1\), define the actual folded coefficient blocks

\[
\begin{aligned}
\mathcal B_\ell
&=\sum_{n_j=\ell}b_je^{i\psi_j}
+\sum_{n_j=-\ell}\overline{b_je^{i\psi_j}},\\
\mathcal D_\ell
&=\sum_{n_j=\ell}d_je^{i\psi_j}
+\sum_{n_j=-\ell}\overline{d_je^{i\psi_j}}.
\end{aligned}
\tag{11}
\]

The product rule in (2) gives the exact finite fields

\[
v=\sum_{\ell\ge1}\operatorname{Re}
\left(Q^{-A}\mathcal B_\ell e^{i\ell\theta}\right),
\qquad
\partial_zv=\sum_{\ell\ge1}\operatorname{Re}
\left(Q^{-A-D}\mathcal D_\ell e^{i\ell\theta}\right).
\tag{12}
\]

With the original normalized auxiliary average and

\[
\|X\|_{e,R}^2=\int_0^\infty R^e\langle|X|^2\rangle_Y\,dR,
\qquad e\in\{1,2\},
\tag{13}
\]

equations (6), (10), and \(r^e,dr=Q^{(e+1)/2}R^e,dR\) give

\[
\boxed{
\|v\|_e^2=
\frac12Q^{(e+1)/2-2A}
\sum_{\ell\ge1}\|\mathcal B_\ell\|_{e,R}^2,
}
\tag{14}
\]

\[
\boxed{
\|\partial_zv\|_e^2=
\frac12Q^{(e+1)/2-2A-2D}
\sum_{\ell\ge1}\|\mathcal D_\ell\|_{e,R}^2.
}
\tag{15}
\]

Thus the exact finite-sum norm is

\[
\|v\|_e=2^{-1/2}Q^{(e+1)/4-A}
\left(\sum_{\ell\ge1}\|\mathcal B_\ell\|_{e,R}^2\right)^{1/2},
\tag{16}
\]

and the derivative has the same formula with \(\mathcal D_\ell\) and one additional \(Q^{-D}\). For one isolated harmonic, (16) reduces to the earlier \(2^{-1/2}\) factor. For repeated equal or opposite carriers, it retains their interference inside \(\mathcal B_\ell\); replacing that block by a sum of individual norms is only an upper bound.

The four exact chart powers are

\[
\begin{array}{c|cc}
e&\|v\|_e&\|\partial_zv\|_e\\ \hline
2&Q^{1/4-h}&Q^{-1/4}\\
1&Q^{-h}&Q^{-1/2}.
\end{array}
\tag{17}
\]

For several bands, equation (6) remains exact after inserting each physical factor \(Q_j^{-A}\) or \(Q_j^{-A-D}\) into its own \(h_j\) before folding. A common power may be extracted only inside a fixed band.

## 3. Exact stress blocks

Write the pulled-back old oscillatory field in the same folded form,

\[
w_{*,s}^Q=\sum_{\ell\ge1}
\operatorname{Re}(\mathcal O_{\ell,s}e^{i\ell\theta}),
\qquad s\in\{r,\theta,z\},
\tag{18}
\]

and put \(\dot{\mathcal O}_{\ell,s}=\partial_Z\mathcal O_{\ell,s}\). The old angular mean is a zero-block term and has no cross product with (12). The exact angularly averaged cross and quadratic stress coefficients are

\[
S_{ab}^{\mathrm{old}\times\mathrm{new}}
=\frac12Q^{-A}\sum_{\ell\ge1}
\operatorname{Re}\left(
\mathcal O_{\ell,a}\overline{\mathcal B_{\ell,b}}
+\mathcal B_{\ell,a}\overline{\mathcal O_{\ell,b}}
\right),
\tag{19}
\]

\[
S_{ab}^{\mathrm{new}\times\mathrm{new}}
=\frac12Q^{-2A}\sum_{\ell\ge1}
\operatorname{Re}\left(
\mathcal B_{\ell,a}\overline{\mathcal B_{\ell,b}}
\right).
\tag{20}
\]

These formulas retain every equal-carrier and opposite-carrier contribution. They also retain the zero output harmonic created by those products: (19)–(20) are exactly that angular mean. Products with unequal absolute carriers have nonzero output frequency and therefore make no contribution to this averaged stress.

## 4. Flux and moment propagation

Keep the source definitions

\[
\begin{aligned}
J_2&=\int r^2\langle
w_{*,z}v_\theta+v_zw_{*,\theta}+v_zv_\theta\rangle\,dr,\\
J_1&=\int r\langle2w_{*,z}v_z+v_z^2\rangle\,dr,
\qquad M_e=\partial_zJ_e.
\end{aligned}
\tag{21}
\]

The new quadratic terms are exactly

\[
J_2^{\mathrm{quad}}
=\frac12Q^{3/2-2A}\sum_{\ell\ge1}\int R^2
\left\langle\operatorname{Re}
(\mathcal B_{\ell,z}\overline{\mathcal B_{\ell,\theta}})
\right\rangle_YdR,
\tag{22}
\]

\[
J_1^{\mathrm{quad}}
=\frac12Q^{1-2A}\sum_{\ell\ge1}\int R
\langle|\mathcal B_{\ell,z}|^2\rangle_YdR,
\tag{23}
\]

\[
M_2^{\mathrm{quad}}
=\frac12Q^{3/2-2A-D}\sum_{\ell\ge1}\int R^2
\left\langle\operatorname{Re}\left(
\mathcal D_{\ell,z}\overline{\mathcal B_{\ell,\theta}}
+\mathcal B_{\ell,z}\overline{\mathcal D_{\ell,\theta}}
\right)\right\rangle_YdR,
\tag{24}
\]

\[
M_1^{\mathrm{quad}}
=Q^{1-2A-D}\sum_{\ell\ge1}\int R
\left\langle\operatorname{Re}
(\mathcal D_{\ell,z}\overline{\mathcal B_{\ell,z}})
\right\rangle_YdR.
\tag{25}
\]

The factor in (25) is one, since differentiating the factor \(1/2\) in \(|\mathcal B_{\ell,z}|^2/2\) produces two conjugate terms.

The exact old–new pieces are

\[
\begin{aligned}
J_2^{\mathrm{cross}}
&=\frac12Q^{3/2-A}\sum_\ell\int R^2
\left\langle\operatorname{Re}\left(
\mathcal O_{\ell,z}\overline{\mathcal B_{\ell,\theta}}
+\mathcal B_{\ell,z}\overline{\mathcal O_{\ell,\theta}}
\right)\right\rangle_YdR,\\
J_1^{\mathrm{cross}}
&=Q^{1-A}\sum_\ell\int R
\left\langle\operatorname{Re}
(\mathcal O_{\ell,z}\overline{\mathcal B_{\ell,z}})
\right\rangle_YdR,
\end{aligned}
\tag{26}
\]

\[
\begin{aligned}
M_2^{\mathrm{cross}}
&=\frac12Q^{3/2-A-D}\sum_\ell\int R^2
\Big\langle\operatorname{Re}\big(
\dot{\mathcal O}_{\ell,z}\overline{\mathcal B_{\ell,\theta}}
+\mathcal O_{\ell,z}\overline{\mathcal D_{\ell,\theta}}\\
&\hspace{48mm}
+\mathcal D_{\ell,z}\overline{\mathcal O_{\ell,\theta}}
+\mathcal B_{\ell,z}\overline{\dot{\mathcal O}_{\ell,\theta}}
\big)\Big\rangle_YdR,\\
M_1^{\mathrm{cross}}
&=Q^{1-A-D}\sum_\ell\int R
\left\langle\operatorname{Re}\left(
\dot{\mathcal O}_{\ell,z}\overline{\mathcal B_{\ell,z}}
+\mathcal O_{\ell,z}\overline{\mathcal D_{\ell,z}}
\right)\right\rangle_YdR.
\end{aligned}
\tag{27}
\]

Equations (26)–(27) keep the old field and old axial derivative as different objects. No relation between their orders has been inserted.

The powers in the four quadratic terms are, without alteration,

\[
\begin{array}{c|c}
\text{term}&\text{exact power}\\ \hline
J_2^{\mathrm{quad}}&Q^{1/2-2h}\\
M_2^{\mathrm{quad}}&Q^{-h}\\
J_1^{\mathrm{quad}}&Q^{-2h}\\
M_1^{\mathrm{quad}}&Q^{-1/2-h}.
\end{array}
\tag{28}
\]

## 5. Finite block bounds

For a block component set

\[
B_{\ell,e,s}=\|\mathcal B_{\ell,s}\|_{e,R},
\qquad
D_{\ell,e,s}=\|\mathcal D_{\ell,s}\|_{e,R}.
\tag{29}
\]

Weighted Cauchy–Schwarz in \(R\) and \(Y\) gives

\[
\begin{aligned}
|J_2^{\mathrm{quad}}|
&\le\frac12Q^{3/2-2A}\sum_\ell
B_{\ell,2,z}B_{\ell,2,\theta},\\
|M_2^{\mathrm{quad}}|
&\le\frac12Q^{3/2-2A-D}\sum_\ell
(D_{\ell,2,z}B_{\ell,2,\theta}
+B_{\ell,2,z}D_{\ell,2,\theta}),\\
J_1^{\mathrm{quad}}
&=\frac12Q^{1-2A}\sum_\ell B_{\ell,1,z}^2,\\
|M_1^{\mathrm{quad}}|
&\le Q^{1-2A-D}\sum_\ell
B_{\ell,1,z}D_{\ell,1,z}.
\end{aligned}
\tag{30}
\]

The corresponding cross bounds follow term by term from (26)–(27). They have factor \(1/2\) in the two-component \(J_2,M_2\) formulas and factor one in the doubled axial \(J_1,M_1\) formulas. When an old coefficient-block norm is converted to the angularly averaged physical old-field norm, its coefficient norm contributes the exact factor \(\sqrt2\); this recovers the earlier single-harmonic factors \(2^{-1/2}\) and \(\sqrt2\). The inherited feedback memo’s line for \(J_1^{\mathrm{old}\times\mathrm{new}}\) contains a stray comma after \(\sqrt2\); equation (26) fixes the coefficient unambiguously.

The block bounds can be strictly smaller than the ordered-pair majorant because all equal and opposite carriers are combined before taking a norm. This is a proved finite strengthening. It does not yield a uniform estimate as \(Q\downarrow0\) unless the source supplies uniform bounds for the block coefficients.

## Verification and figure

`checks/finite_angular_gram_check.py` verifies (6)–(8), the zero/nonzero decoupling, same- and opposite-carrier entries, the derivative product rule, and every exponent in (17) and (28) using exact rational arithmetic. Its receipt is `state/FINITE_ANGULAR_GRAM_CHECK.json`.

![Exact carrier Gram blocks](../figures/finite_angular_gram.png)

The figure displays the actual selection law of (7): same carrier, opposite carrier, the combined zero block, and all vanishing entries. Its reproducible source is `figures/finite_angular_gram.py`. The source proof locators are `moments_body.tex` labels `nsmom:actual_amplitude`, `nsmom:actual_derivative`, `nsmom:M2`, and `nsmom:M1`, and `evaluation_flux_body.tex` labels `eflux:kernel`–`eflux:stress-derivative`.

## Disposition

The finite angular matrix, physical norm factors, stress coefficients, and four moment formulas are now explicit and proved. This closes the finite Gram item in the main cursor. It does not close the third shooting return, a uniform infinite modified sequence, or the terminal smooth-force extension.
