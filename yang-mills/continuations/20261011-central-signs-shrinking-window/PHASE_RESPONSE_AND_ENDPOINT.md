# Full vacuum response and a direct bound for the original raw phase quotient

11 October 2026. The result below keeps the original finite open box, rooted words, reflection, raw phase, Hamiltonian, and simultaneous path. It proves an exact response representation of the complete endpoint and a direct quantitative estimate for its energy-to-mass quotient. The new estimate is \(O(j^{16})\), compared with the \(O(j^{68})\) estimate obtained by dividing the preceding independent energy and mass bounds. Neither estimate proves positivity in the window \(s_j=\kappa_*/j\).

The receiving programme sources are [the original phase and endpoint, PK158–PK160 and PK199–PK202](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md#L3500), [IP1–IP22](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/442786391ab942ad0c829c0ebf32e952585915e0/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_MOMENTS_AND_ORIGINAL_PATH.md), [JP1–JP49](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/442786391ab942ad0c829c0ebf32e952585915e0/yang-mills/continuations/20261011-central-signs-shrinking-window/BOUNDARY_REFLECTION_AND_RAW_ENDPOINT.md), [PC1–PC52](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/442786391ab942ad0c829c0ebf32e952585915e0/yang-mills/continuations/20261011-central-signs-shrinking-window/POLYNOMIAL_CONDITIONAL_BOUNDS.md), and [the full physical inverse, GPR1–GPR31](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/442786391ab942ad0c829c0ebf32e952585915e0/yang-mills/continuations/20261011-central-signs-shrinking-window/GLOBAL_PHYSICAL_RESPONSE.md). The actual vacuum score is proved in the retained original [spatial TeX, equations (77)–(79)](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/sources/spatial/spatial_continuum.tex#L1415); its proof is reproduced below. These are programme derivations, not attributed human-paper results. The source ledger records the bounded source-index routing and actual reading coverage. No novelty or exhaustive-literature claim is made.

## 1. Every original object and the actual centered inverse

Let \(L\ge2\), \(m=2L\), \(n=m+1\). Vertices \((i,k,l)\in\{0,\ldots,m\}^3\) stand for the original physical points \(o+a(i-L,k-L,l-L)\). Positive edges join consecutive vertices, and every positively oriented face has its original ordered holonomy
\[
 U_{(z;i,j)}=U_i(z)U_j(z+e_i)U_i(z+e_j)^{-1}U_j(z)^{-1},
 \quad W_p=\operatorname{tr}U_p,\quad
 N=3m(m+1)^2,\quad M=3m^2(m+1).
 \tag{PRE1}
\]
Write \(Q_L=SU(2)^{E_L}\), with product Haar probability \(dU\), and retain
\[
 T_\alpha=-i\sigma_\alpha/2,\quad
 X_{e,\alpha}f=\left.\frac d{dt}f(\ldots,e^{tT_\alpha}U_e,\ldots)\right|_0,
 \quad K=-\sum_{e,\alpha}X_{e,\alpha}^2,\quad
 \Gamma(f,h)=\sum_{e,\alpha}X_{e,\alpha}f\,X_{e,\alpha}h.
 \tag{PRE2}
\]
The three fields give the radius-two metric on each group factor. The gauge constraint is invariance under \(U_{(s,t)}\mapsto q_sU_{(s,t)}q_t^{-1}\) at every vertex, including the boundary vertices. Denote the gauge average by \(\Pi\). The complete original Hamiltonian, including its scalar potential, is
\[
 H=\kappa K+b_{\rm mag}\sum_p(2-W_p),\qquad
 \kappa=\frac{2g^2}{a}>0,\quad b_{\rm mag}=\frac1{2g^2a},\quad
 \xi=\frac{b_{\rm mag}}{\kappa}=\frac1{4g^4},\qquad
 H\psi=E_0\psi,\quad \int\psi^2dU=1.
 \tag{PRE3}
\]
The ground state is strictly positive, smooth, gauge invariant, and unique with this positive phase. One proof is the positive heat kernel on the connected compact link product, preserved by multiplication with the bounded real potential through the product formula; the lowest spectral eigenspace is consequently simple and positive. Elliptic regularity makes it smooth. Gauge invariance follows by uniqueness. Put
\[
 d\mu=\rho\,dU=\psi^2dU,\quad A=H-E_0,\quad
 P_Hf=\int f\,dU,\quad v=\log\psi-P_H\log\psi,\quad
 c=P_H\log\psi=-\tfrac12\log\int e^{2v}dU.
 \tag{PRE4}
\]
Thus the constant \(2\kappa\xi M\), the scalar \(E_0\), and the logarithmic scalar \(c\) have all been retained.

Use the unchanged Sobolev scale
\[
 H^s(Q_L)=\{f:(I+K)^{s/2}f\in L^2(dU)\},\quad
 H^s_{{\rm ph},\mu0}=\{f\in H^s:\Pi f=f,\ \langle f,\rho\rangle=0\}.
 \tag{PRE5}
\]
For negative \(s\), the bracket is the distribution pairing with the smooth positive density. Smooth multiplication and its smooth reciprocal act boundedly on every \(H^s\). Multiplication \(U_\psi f=\psi f\) is unitary from \(L^2(\mu)_{\rm ph}\) to \(L^2(dU)_{\rm ph}\), with respective operator and form domains \(H^2_{\rm ph}\) and \(H^1_{\rm ph}\). Its exact conjugate is
\[
 \mathcal L=K-2\Gamma(v,\cdot)
   =\kappa^{-1}\psi^{-1}A\psi,\qquad
 \mu(\mathcal Lh)=0,\qquad
 \mu(f\mathcal Lh)=\mu\Gamma(f,h).
 \tag{PRE6}
\]
The last two identities hold for smooth functions by integration by parts, since \(X\rho=2\rho Xv\), and extend to the indicated Sobolev dualities. Expanding \(H(f\psi)\) proves the conjugation with the entire potential and \(E_0\) present. The vacuum equation cancels precisely their multiplication terms and the \(fK\psi\) term.

The only distributional kernel elements of \(\mathcal L\) are constants: elliptic regularity makes such an element smooth, and the last identity in (PRE6) makes every derivative zero. The compact manifold is connected. Consequently
\[
 \mathcal L:H^{s+2}_{{\rm ph},\mu0}\longrightarrow
 H^s_{{\rm ph},\mu0}
 \quad\hbox{is a bounded isomorphism for every real }s.
 \tag{PRE7}
\]
For completeness, \(K^{-1}Q_H\mathcal L=I-2K^{-1}Q_H\Gamma(v,\cdot)\) on the zero-Haar-mean space is identity minus an operator gaining one derivative, hence a Fredholm operator of index zero. Its kernel is zero: \(\mathcal Lh\) is then constant; its \(\mu\) mean makes that constant zero, and the Haar mean removes the remaining constant in \(h\). Its bounded inverse solves \(\mathcal Lh=f-\mu f\), with a subsequent subtraction of \(\mu h\). Compact Sobolev inclusions follow by cutting off the product-spin spectrum of \(K\). Smooth multiplication, differentiation, and the spectral Sobolev interpolation give the claimed mappings at every real index. This proves (PRE7), including the distribution extension, without a small-source restriction.

For a real physical \(f\in H^s\), define its centered Poisson response
\[
 f^\circ=f-\mu f,\qquad
 u_f=\mathcal L^{-1}f^\circ
       =\kappa\psi^{-1}A^\dagger(\psi f^\circ),\qquad \mu u_f=0.
 \tag{PRE8}
\]
Here \(A^\dagger\) is the full inverse on the physical \(\psi^\perp\), extended to annihilate \(\psi\). It maps \(H^s_{\rm ph}\) to \(H^{s+2}_{\rm ph}\) after its vacuum projection. Its extension follows from (PRE7) by multiplication with \(\psi\). Thus no compressed operator has replaced \(A\).

The exact connection with the earlier Haar-mean Jacobian is
\[
 h_f=(I-2K^{-1}Q_H\Gamma(v,\cdot))^{-1}K^{-1}Q_Hf,\quad
 h_f=u_f-P_Hu_f,\quad
 u_f=h_f-\mu h_f.
 \tag{PRE9}
\]
Indeed both \(h_f\) and \(u_f\) solve \(\mathcal Lh=f-\mu f\); the two specified means fix their difference. In particular the scalar removed by \(Q_H\) is not confused with the actual-vacuum mean.

## 2. The complete phase, its reflection, and its affine terms

The original tree is rooted at \((0,0,0)\). Root paths proceed in directions three, two, one; the tree contains every direction-one edge, direction-two edges at \(i=0\), and direction-three edges at \(i=k=0\). Every chord remains the full word \(Z_c=t_sU_ct_t^{-1}\). The two original chord sets are
\[
 \mathcal C_2=\{(i,k,l;2):1\le i\le m,\ 0\le k<m,\ 0\le l\le m\},
 \quad
 \mathcal C_3=\{(i,k,l;3):0\le i,k\le m,\ (i,k)\ne(0,0),\
                                  0\le l<m\}.
 \tag{PRE10}
\]
Keep the original rows and every excluded tree edge:
\[
 \begin{gathered}
 h=\frac{\pi}{2n},\quad
 v_0(l)=n^{-1/2},\quad
 v_1(l)=\sqrt{2/n}\cos\frac{\pi(l+1/2)}n,\quad
 w_1(l)=-\sqrt{2/n}\sin\frac{\pi(l+1)}n,\\
 a_{(i,k,l;2)}=-v_1(i)w_1(k)v_0(l)/\sqrt2,\quad a_{(i,k,l;3)}=0,\\
 b_{(i,k,l;2)}=v_0(i)w_1(k)v_1(l)/\sqrt2,\quad
 b_{(i,k,l;3)}=-v_0(i)v_1(k)w_1(l)/\sqrt2,\\
 q^\alpha(U)=-2\operatorname{tr}(T_\alpha U),\quad
 u_1=\sum_ca_cq(Z_c),\quad u_3=\sum_cb_cq(Z_c),\quad
 \mathcal S=u_1\cdot u_3,\\
 \sigma_*=\sqrt8\sin h,\quad\beta_0=\frac{\sigma_*}{2g^2},\quad
 p=\beta_0\mathcal S,\quad r=\beta_0\mathcal S_{\mathcal R},\quad
 F=p-r,\quad D=\mathcal S+\mathcal S_{\mathcal R}.
 \end{gathered}\tag{PRE11}
\]
The direction-one graph reflection \(\mathcal R\) includes the reflected root and every inverse edge orientation. It is a Haar-preserving isometry, preserves the full potential, and acts on gauge constraints by permuting vertices. Hence it commutes with \(H,K,\mathcal L,A^\dagger\), and uniqueness gives \(\psi\circ\mathcal R=\psi\). Therefore
\[
 F\circ\mathcal R=-F,\quad D\circ\mathcal R=D,\quad
 \mu F=P_HF=0,\quad
 \mu D=2\mu\mathcal S,\quad P_HD=2P_H\mathcal S.
 \tag{PRE12}
\]
These statements do not center or alter the original raw \(D\).

The exact tree-coordinate presentation sets original tree links to identity and keeps each chord equal to its full \(Z_c\). It preserves product Haar after inclusion of all tree transports, by successive left and right invariance; gauge-invariant functions are independent of these transports. In this presentation put
\[
 A_{k,l}=\left(\prod_{t=0}^{l-1}U_3(m,0,t)\right)
          \left(\prod_{b=0}^{k-1}U_2(m,b,l)\right).
 \tag{PRE13}
\]
Both products are in increasing index order, empty products equal identity, and \(U_2(0,k,l)=U_3(0,0,l)=I\). The full reflected words are
\[
 Z^{\mathcal R}_{(i,k,l;2)}
   =A_{k,l}U_2(m-i,k,l)A_{k+1,l}^{-1},\qquad
 Z^{\mathcal R}_{(i,k,l;3)}
   =A_{k,l}U_3(m-i,k,l)A_{k,l+1}^{-1}.
 \tag{PRE14}
\]
Reflection of each of the three original root segments gives the two endpoint products and the target in exactly this order; its direction-one segments are tree links in this presentation. No endpoints are commuted.

For example retain the stronger receiving chord already present in PC48,
\[
 v^\circ=(1,L-1,0;2),\quad e_\partial^\circ=(m,L-1,0;2),\quad
 K_\circ=Z_{v^\circ},\quad H_\partial=Z_{e_\partial^\circ},\quad
 \mathcal T=A_{L-1,0},\quad
 a^\circ=\frac{\sqrt2}{n^{3/2}}\cos(3h)\cos h,\quad
 b^\circ=-\frac{\sqrt2}{n^{3/2}}\cos^2h.
 \tag{PRE15}
\]
The unique reflected target of \(K_\circ\) is
\(\mathcal T K_\circ H_\partial^{-1}\mathcal T^{-1}\).
Writing \(R_\mathcal T=\operatorname{Ad}_{\mathcal T}\), define
\(U_\mu=\sum_{c\ne v^\circ}\mathsf M_{\mu c}q(Z_c)\) and
\(V_\mu=\sum_{c\ne(m-1,L-1,0;2)}\mathsf M_{\mu c}q(Z_c^{\mathcal R})\).
They are independent of \(K_\circ\), retain all other variables, and may depend on \(H_\partial\). The complete two products are
\[
 \begin{split}
 \mathcal S={}&U_1\cdot U_3
       +(b^\circ U_1+a^\circ U_3)\cdot q(K_\circ)
       +a^\circ b^\circ|q(K_\circ)|^2,\\
 \mathcal S_{\mathcal R}={}&V_1\cdot V_3
       +(b^\circ V_1-a^\circ V_3)\cdot
                          R_\mathcal Tq(K_\circ H_\partial^{-1})
       -a^\circ b^\circ|q(K_\circ H_\partial^{-1})|^2 .
 \end{split}\tag{PRE16}
\]
The second equality uses the original reflected coefficient \(-a^\circ\) and the unchanged coefficient \(b^\circ\); the orthogonal adjoint action preserves the displayed squared norm. All affine terms and constants in (PRE16) will remain in every subsequent operator and integral.

## 3. Actual source response, including every scalar

For any fixed smooth real physical observable \(f\), freeze its entire function at the given regulator and introduce the auxiliary source only for differentiation:
\[
 H(t)=H-\kappa t f,\qquad
 H(t)\psi_t=E(t)\psi_t,\quad \int\psi_t^2dU=1,\quad\psi_t>0.
 \tag{PRE17}
\]
This is a response probe of the full Hamiltonian. Evaluation is always at \(t=0\); it does not change the prescribed path. The isolated simple vacuum and a resolvent contour yield real analytic \(E(t),\psi_t\), locally at every finite real \(t\). The resolvent Neumann series is valid on that contour for small bounded perturbations, and Sobolev regularity then gives analytic dependence in every \(C^k\). This also proves analytic dependence on all the original finite real face sources.

Differentiating the complete eigenvalue equation, and differentiating its unit norm, gives
\[
 E'(0)=-\kappa\mu f,\quad
 \dot\psi_0=\kappa A^\dagger(\psi f^\circ)=\psi u_f,\quad
 \mu u_f=0,\quad
 \left.\frac d{dt}\mu_t g\right|_0
       =2\mu(g^\circ u_f).
 \tag{PRE18}
\]
The last formula assumes \(g\) fixed; otherwise the additional term is \(\mu\dot g_0\). The full potential in (PRE3) remains when deriving (PRE18). The subtraction \(E'(0)\psi=-\kappa\mu(f)\psi\) is exactly what centers the source.

For \(v_t=\log\psi_t-P_H\log\psi_t\), \(c_t=P_H\log\psi_t\), the complete logarithmic and scalar equations are
\[
 \begin{split}
 Kv_t&=\xi\sum_pW_p+tQ_Hf+\Gamma(v_t,v_t)-P_H\Gamma(v_t,v_t),\\
 E(t)&=2\kappa\xi M-\kappa tP_Hf
                         -\kappa P_H\Gamma(v_t,v_t),\\
 c_t&=-\tfrac12\log\int e^{2v_t}dU,\qquad
 \dot v_0=h_f,\qquad \dot c_0=-\mu h_f=P_Hu_f.
 \end{split}\tag{PRE19}
\]
These identities follow by dividing the eigenvalue equation by \(\psi_t\), using \(K(e^v)=e^v(Kv-\Gamma(v,v))\), and then taking Haar means. In particular
\[
 E''(0)=-2\kappa\,\mu(f^\circ u_f),\qquad
 \ddot c_0=-\mu\ddot v_0
      -2\{\mu(h_f^2)-(\mu h_f)^2\}.
 \tag{PRE20}
\]
For the second scalar differentiate \(\dot c_t=-\mu_t\dot v_t\) and use \(\partial_t\log\psi_t=\dot v_t-\mu_t\dot v_t\). This proves all normalization contributions.

Define the full response bilinear form
\[
 \mathfrak R(f,g)
  =\kappa\langle \psi f^\circ,A^\dagger\psi g^\circ\rangle_{L^2(dU)}
  =\mu(f^\circ u_g)=\mu\Gamma(u_f,u_g).
 \tag{PRE21}
\]
It is positive on nonconstant physical observables modulo constants, symmetric for real functions, and retains the complete inverse. The equalities follow from (PRE6) and (PRE8). For \(f=F\), reflection maps \(H(t)\) to \(H(-t)\), so \(E(t)=E(-t)\), \(E'(0)=0\), and \(u_F=h_F\) is odd with both Haar and actual means zero. In particular \(\dot c_0=0\). No such zero scalar is imposed for \(\mathcal S\) or \(D\).

For a general real smooth \(f\), \(u_{\mathcal L f}=f-\mu f\). Thus the exact receiving identities are
\[
 \operatorname{Cov}_\mu(f,g)
       =\mu\Gamma(u_f,g)=\mathfrak R(f,\mathcal Lg),\qquad
 \mu\Gamma(f,g)=\mathfrak R(\mathcal Lf,\mathcal Lg).
 \tag{PRE22}
\]
The mean \(\mu(\mathcal Lf)=0\) is part of this statement. Both equalities follow by applying (PRE6), not by replacing the full operator with a finite observable matrix.

## 4. The complete endpoint as a response and a cancellation identity

Let
\[
 G=\mu(F^2)>0,\quad
 C_F=\kappa\mu\Gamma(F,F)>0,\quad
 J_F=\mathcal LF=KF-2\Gamma(v,F).
 \tag{PRE23}
\]
All terms in (PRE16), and all their physical derivatives, occur in \(J_F\). In particular
\[
 K\mathcal S=(Ku_1)\cdot u_3+u_1\cdot Ku_3
                   -2\sum_{e,\alpha}(X_{e,\alpha}u_1)
                                      \cdot(X_{e,\alpha}u_3),
 \quad
 J_F=\beta_0(I-\mathcal R^*)\{K\mathcal S-2\Gamma(v,\mathcal S)\}.
 \tag{PRE24}
\]
To verify the strict inequalities in (PRE23) directly, set every original physical link to identity except \(K_\circ=\exp(\pi T_1)\). The boundary products are identity; the two original mode vectors are \(a^\circ q(K_\circ),b^\circ q(K_\circ)\), while their reflected counterparts have coefficients \(-a^\circ,b^\circ\). Thus \(F=8\beta_0a^\circ b^\circ\ne0\), whereas at the identity configuration \(F=0\). Positivity of the smooth vacuum makes \(G>0\). If \(C_F=0\), every derivative of \(F\) would vanish, contradicting this nonconstancy.
Each \(Ku_\mu\) differentiates every occurrence in its full rooted words. For an ordered word \(\prod_{r=1}^{\ell}B_r(t)\), the second derivative is
\(\sum_rB_1\cdots B_r''\cdots B_\ell+
2\sum_{r<s}B_1\cdots B_r'\cdots B_s'\cdots B_\ell\).
For a positive occurrence the first and second differentiated factors are \(T_\alpha U_e,T_\alpha^2U_e\); for an inverse occurrence they are \(-U_e^{-1}T_\alpha,U_e^{-1}T_\alpha^2\). Summing this formula over all three colours and all physical edges with the minus sign of \(K\) specifies every derivative in (PRE24), including repeated occurrences and inverse signs.

The exact response matrix of the two complete sources \(F,J_F\) is
\[
 \begin{pmatrix}
 \mathfrak R(F,F)&\mathfrak R(F,J_F)\\
 \mathfrak R(J_F,F)&\mathfrak R(J_F,J_F)
 \end{pmatrix}
 =
 \begin{pmatrix}
 T_F&G\\G&C_F/\kappa
 \end{pmatrix},
 \qquad T_F=\mu\Gamma(u_F,u_F)=\mu(Fu_F)>0.
 \tag{PRE25}
\]
Therefore the original raw endpoint is, exactly,
\[
 \mathscr E(s)=G-\frac{C_F}{s}
 =\mathfrak R(F,J_F)-\frac{\kappa}{s}\mathfrak R(J_F,J_F)
 =\mu\Gamma\left(F,u_F-\frac{\kappa}{s}F\right).
 \tag{PRE26}
\]
This is an identity for the original unscaled vector \(F\psi\). Its spectral measure is \(\nu_F(B)=\langle F\psi,\mathbf1_B(A)F\psi\rangle\); since this vector is odd and vacuum orthogonal,
\(\nu_F((0,s])\ge\max(0,\mathscr E(s))\).
Indeed \(1-\lambda/s\le\mathbf1_{(0,s]}(\lambda)\) for every \(\lambda>0\), and integration proves the claim.

The complete reflection cancellation remains visible in this representation:
\[
 \begin{split}
 \mathscr E(s)=\beta_0^2[&
 4\mu(\mathcal S^2)-4\mu(\mathcal SD)+\mu(D^2)\\
 &-\frac{\kappa}{s}\{4\mu\Gamma(\mathcal S,\mathcal S)
           -4\mu\Gamma(\mathcal S,D)+\mu\Gamma(D,D)\}]\\
 ={}&4\beta_0^2\left[\mu(\mathcal S^2)
                     -\frac{\kappa}{s}\mu\Gamma(\mathcal S,\mathcal S)\right]
       -\beta_0^2\mu(D^2)+\frac{\kappa\beta_0^2}{s}\mu\Gamma(D,D).
 \end{split}\tag{PRE27}
\]
To prove the second equality, reflect and add the first mixed expectation to obtain \(2\mu(\mathcal SD)=\mu(D^2)\). Reflection preserves the metric, so the same calculation gives \(2\mu\Gamma(\mathcal S,D)=\mu\Gamma(D,D)\). No term of the affine formula (PRE16) is removed.

The constant contributions are also exact. If \(m_{\mathcal S}=\mu\mathcal S\), then
\[
 4\mu(\mathcal S^2)-\mu(D^2)
  =4\operatorname{Var}_\mu\mathcal S-\operatorname{Var}_\mu D
       +(4m_{\mathcal S}^2-(2m_{\mathcal S})^2).
 \tag{PRE28}
\]
The last parenthesis equals zero by the proved mean relation; it is not suppressed by an independent centering choice. With \(P_\pm=(I\pm\mathcal R^*)/2\),
\[
 u_D=2P_+u_{\mathcal S},\quad
 u_F=2\beta_0P_-u_{\mathcal S},\quad
 u_F=\beta_0(2u_{\mathcal S}-u_D).
 \tag{PRE29}
\]
These follow by applying the centered Poisson inverse, which commutes with reflection. They give an exact morphism from the entire even correction and its means to the odd physical response.

The first attempt to turn positivity of (PRE25) into an upper quotient bound has the opposite direction. Its precise defect is
\[
 \frac{C_F}{\kappa}-\frac{G^2}{T_F}
  =\mu\Gamma\left(F-\frac{G}{T_F}u_F,\,
                       F-\frac{G}{T_F}u_F\right)\ge0.
 \tag{PRE30}
\]
Expanding the square uses \(\mu\Gamma(F,u_F)=G\) and
\(\mu\Gamma(u_F,u_F)=T_F\). Equality holds exactly when
\(F=(G/T_F)u_F\), since both are odd and constants have been removed.
Applying \(\mathcal L\) then shows that equality means precisely that the entire \(F\psi\) is an eigenvector of \(A\), of energy \(\kappa G/T_F\). Thus susceptibility positivity alone gives a lower bound for \(C_F/G\).

Completing the square retains the remaining cancellation explicitly:
\[
 \mathscr E(s)
 =\frac{s}{4\kappa}T_F-\frac{\kappa}{s}
       \mu\Gamma\left(F-\frac{s}{2\kappa}u_F,\,
                         F-\frac{s}{2\kappa}u_F\right).
 \tag{PRE31}
\]
This formula proves the exact deficit of the response-only upper bound
\(\mathscr E(s)\le sT_F/(4\kappa)\). It contains the full physical Poisson solution and the original raw phase.

## 5. The exact tree cancellation lowers the physical-link degree

The next estimate controls the quotient directly, rather than dividing unrelated lower bounds. First a complete word cancellation improves the elementary degree count on every original physical link, including tree links.

For \(U,V\in SU(2)\), the original quaternion multiplication gives
\[
 q(U)\cdot q(V)=\operatorname{tr}(UV^{-1})-\operatorname{tr}(UV).
 \tag{PRE32}
\]
Indeed \(U=c_UI+q(U)\cdot T\) and
\(\operatorname{tr}(T_\alpha T_\beta)=-\delta_{\alpha\beta}/2\).
The two traces are \(2c_Uc_V+q(U)\cdot q(V)/2\) and
\(2c_Uc_V-q(U)\cdot q(V)/2\), respectively. Their scalar terms cancel in their displayed difference. Consequently the full original product is
\[
 \mathcal S=\sum_{c,d}a_cb_d
        [\operatorname{tr}(Z_cZ_d^{-1})
                    -\operatorname{tr}(Z_cZ_d)].
 \tag{PRE33}
\]
Every ordered pair and both trace terms remain.

Fix a physical tree edge \(e\), remove it from the original tree, and let \(\epsilon_z\in\{0,1\}\) indicate whether the root path to \(z\) uses that edge. Under its physical variation \(U_e(t)=e^{tT_\alpha}U_e\), all root transports satisfy
\[
 t_z(t)=C(t)^{\epsilon_z}t_z,\qquad
 C(t)=A_e e^{tT_\alpha}A_e^{-1}.
 \tag{PRE34}
\]
Here \(A_e\) is the unchanged root transport to the starting vertex of \(e\). This holds because the tree root path uses \(e\) exactly once in positive orientation when \(\epsilon_z=1\). For an arbitrary oriented tree, including the reflected one, the same identity holds with a conjugate of \(e^{-tT_\alpha}\) when the traversal is inverse; it is still a one-parameter subgroup. Hence a chord from \(s\) to \(t\) changes exactly as \(Z_c(t)=C(t)^{\epsilon_s}Z_cC(t)^{-\epsilon_t}\).

For a second chord \(d\) from \(u\) to \(w\), cyclicity of trace gives both complete identities
\[
 \begin{split}
 \operatorname{tr}(Z_c(t)Z_d(t)^{-1})
   &=\operatorname{tr}\!\left[
       Z_cC(t)^{\epsilon_w-\epsilon_t}
       Z_d^{-1}C(t)^{\epsilon_s-\epsilon_u}\right],\\
 \operatorname{tr}(Z_c(t)Z_d(t))
   &=\operatorname{tr}\!\left[
       Z_cC(t)^{\epsilon_u-\epsilon_t}
       Z_dC(t)^{\epsilon_s-\epsilon_w}\right].
 \end{split}\tag{PRE35}
\]
Each displayed exponent belongs to \(\{-1,0,1\}\). Thus each trace is a polynomial of total degree at most two in \(\cos(t/2)\) and \(\sin(t/2)\). This proves the cancellation even when a full rooted word originally contains the same tree edge twice, and when the two full words contain it four times in total.

If \(e\) is a chord, only its own rooted word contains it, exactly once. A product in (PRE33) therefore again has at most two factors depending linearly on \(\cos(t/2),\sin(t/2)\), including \(c=d=e\). Applying precisely the same proof to the reflected tree and root covers every term of \(\mathcal S_{\mathcal R}\). Thus
\[
 t\longmapsto F(\ldots,e^{tT_\alpha}U_e,\ldots),\
 D(\ldots,e^{tT_\alpha}U_e,\ldots)
 \quad\hbox{have trigonometric degree at most two in }t/2
 \tag{PRE36}
\]
for every original \(e,\alpha,U\). The same holds for \(\mathcal S,\mathcal S_{\mathcal R}\). This is a property proved for the complete functions, including every affine remainder, not a projection to their conditional quadratic pieces.

## 6. A quantitative weighted derivative estimate with only the actual score

We prove the required estimate directly. Let \(f\) be any real smooth function on the original product satisfying the degree property (PRE36) for a specified \(X=X_{e,\alpha}\). Let \(\rho>0\) be any smooth probability density with \(|X\log\rho|\le B\). In the application these are the actual full \(F\) and actual full vacuum density.

At a fixed configuration \(U\), put \(f_U(t)=f(e^{tT_\alpha}U_e,\ldots)\). The exact stereographic circle substitution is
\[
 z=\tan(t/4),\quad t=4\arctan z,\quad
 \cos(t/2)=\frac{1-z^2}{1+z^2},\quad
 \sin(t/2)=\frac{2z}{1+z^2},\qquad
 f_U(4\arctan z)=\frac{P_U(z)}{(1+z^2)^2},
 \quad \deg P_U\le4.
 \tag{PRE37}
\]
This is an exact change of the integration variable along the original physical one-parameter subgroup, not a change of any physical coordinate or raw function.

For a real polynomial \(P\) of degree at most four and \(0<r\le1/4\), its linear coefficient satisfies
\[
 |P'(0)|^2\le\frac{\gamma_2}{r^3}\int_{-r}^r|P(z)|^2dz,
 \qquad
 \gamma_2=\frac32+\frac72\left(\frac32\right)^2=\frac{75}{8}.
 \tag{PRE38}
\]
To prove this without an unspecified norm constant, expand \(P(ry)\) in the five polynomials \(1,y,(3y^2-1)/2,(5y^3-3y)/2,(35y^4-30y^2+3)/8\). Direct multiplication and \(\int_{-1}^1y^kdy=0\) for odd \(k\), \(2/(k+1)\) for even \(k\), give their orthogonality and squared norms \(2,2/3,2/5,2/7,2/9\). Only degrees one and three have a nonzero derivative at zero, with values \(1,-3/2\). Cauchy–Schwarz for that linear functional gives exactly the displayed sum \(\gamma_2\). The change of variable contributes \(r^{-3}\). Equivalently, the coefficient Gram matrix \(G_{ab}=\int_{-1}^1y^{a+b}dy\), \(0\le a,b\le4\), has \((G^{-1})_{11}=75/8\); direct rational inversion independently checks the same value.

At zero \(P_U'(0)=4Xf(U)\). Since \(dt=4\,dz/(1+z^2)\), keeping the full denominator gives
\[
 |Xf(U)|^2
 \le\frac{\gamma_2(1+r^2)^5}{64r^3}
       \int_{-4\arctan r}^{4\arctan r}|f_U(t)|^2dt .
 \tag{PRE39}
\]
Indeed the integral on the right before estimating its denominator is
\(4\int_{-r}^r|P_U(z)|^2(1+z^2)^{-5}dz\).
Combining it with (PRE38) and dividing by \(16\) proves every factor of (PRE39).

Multiply by \(\rho(U)\) and integrate over every original link. The score gives \(\rho(U)\le e^{B|t|}\rho(e^{tT_\alpha}U_e,\ldots)\). Haar invariance under this same physical left translation then gives the averaged inequality
\[
 \mu(|Xf|^2)\le b_2(B;r)\,\mu(f^2),\qquad
 b_2(B;r)=\frac{75}{64}
      (1+r^2)^5 e^{4B\arctan r}\frac{\arctan r}{r^3},
 \qquad 0<r\le\frac14.
 \tag{PRE40}
\]
The interval length is \(8\arctan r\); it multiplies the coefficient in (PRE39). This is why no lower bound for the raw mass, conditional Haar floor, or full-volume density ratio enters (PRE40). Every exterior correlation remains in \(\rho\).

Two entirely explicit choices are useful:
\[
 \begin{gathered}
 r_B=\frac1{2(B+2)},\quad b_2(B)=b_2(B;r_B),\\
 b_2(B;[4(1+B)]^{-1})
      \le C_2(1+B)^2,\qquad
 C_2=\frac{75e}{4}\left(\frac{17}{16}\right)^5,\\
 \lim_{B\to\infty}\frac{b_2(B)}{B^2}
      =\frac{75e^2}{16}.
 \end{gathered}\tag{PRE41}
\]
For the middle bound use \(r\le1/4\), \(\arctan r\le r\), and
\(4Br\le1\) in (PRE40). The last limit follows from
\(Br_B\to1/2\), \(\arctan r_B/r_B\to1\), and \(r_BB\to1/2\).
One may use the minimum of the two explicit bounds, or any smaller value obtained by minimizing the displayed one-variable function in (PRE40). None is an assertion about the unknown vacuum.

## 7. Application to the actual vacuum and unchanged path

The required score bound follows from the full vacuum equation. Write \(u=\log\psi\), \(\Delta=-K\), and \(w_e=|\nabla_eu|^2\). The product Bochner identity in the radius-two metric is
\[
 (\Delta+2\nabla u\cdot\nabla)w_e
 =2\sum_f|\nabla_f\nabla_eu|_{\rm HS}^2+w_e
                  +2\xi\langle\nabla_eu,\nabla_e W\rangle,\qquad
 W=\sum_p(2-W_p).
 \tag{PRE42}
\]
To obtain it, differentiate
\(\Delta u+|\nabla u|^2=\xi W-E_0/\kappa\).
Commuting factor-\(e\) covariant derivatives contributes
\(2\operatorname{Ric}_e=w_e\); different factors have zero mixed curvature. Substituting the differentiated vacuum equation cancels the drift term and retains all mixed Hessian squares. For a face incident to \(e\), its trace gradient has norm at most one: bi-invariance and inversion reduce it to \(2c(U)\), whose squared gradient on the radius-two sphere is \(1-c(U)^2\). If \(r_e\) is the actual number of incident faces, then \(|\nabla_eW|\le r_e\). At a maximum of \(w_e\), (PRE42) gives \(0\ge w_e-2r_e\xi\sqrt{w_e}\). Hence
\[
 |\nabla_e\log\psi|\le2r_e\xi,\qquad
 |\nabla_e\log\rho|\le4r_e\xi=:B_e.
 \tag{PRE43}
\]
This proof uses the full Hamiltonian and includes its unchanged scalar through the vacuum equation.

Apply (PRE40) to the full \(F\), using (PRE36), and sum all three colour fields of every original physical edge. Since \(G>0\), the result is the direct quotient estimate
\[
 \boxed{\displaystyle
 \frac{C_F}{G}\le\kappa\,\mathcal B_L(\xi),\qquad
 \mathcal B_L(\xi)
 =3\left[
 12m\,b_2(8\xi)
 +12m(m-1)b_2(12\xi)
 +3m(m-1)^2b_2(16\xi)\right].}
 \tag{PRE44}
\]
The finite count is exact. For each of three edge directions, there are \(m\) longitudinal positions and \(n^2\) transverse vertices. Four transverse corners have \(r_e=2\), \(4(m-1)\) noncorner boundary positions have \(r_e=3\), and \((m-1)^2\) interior positions have \(r_e=4\). Multiplying by \(3m\) gives the three multiplicities in (PRE44). All positive edge orientations and boundary incidences are present.

There is also a proved extension with the means retained: for every real \(f\) in the span of \(1,\mathcal S,\mathcal S_{\mathcal R}\), the same proof applied to \(f-\mu f\) gives \(\mu\Gamma(f,f)\le\mathcal B_L(\xi)\{\mu(f^2)-(\mu f)^2\}\). Subtraction of a constant preserves (PRE36). In particular the actual even correction obeys \(\kappa\mu\Gamma(D,D)\le\kappa\mathcal B_L(\xi)\{\mu(D^2)-4(\mu\mathcal S)^2\}\). This explicitly keeps its vacuum component and proves the upper energy comparison complementary to JP38; it makes no assumption that \(\mu D\) vanishes.

The alternate estimate with elementary polynomial dependence on \(\xi\) is
\[
 \boxed{\displaystyle
 \frac{C_F}{G}\le
 3\kappa C_2\left[
 N+32\xi M+192\xi^2m(4m^2+m-1)\right].}
 \tag{PRE45}
\]
Indeed the exact sums are
\[
 \sum_er_e=4M,\qquad
 \sum_er_e^2=12m(4m^2+m-1),\qquad
 \sum_e(1+4r_e\xi)^2=N+32\xi M+192\xi^2m(4m^2+m-1).
 \tag{PRE46}
\]
Expanding the three counts proves these equalities. Equation (PRE45) follows by applying the middle choice in (PRE41) independently to each field before summation. In particular both (PRE44) and (PRE45) are evaluated estimates for the ratio itself.

On the unchanged path,
\[
 L_j=j^4,\quad a_j=\frac1{100j},\quad
 g_j^2=\frac{\kappa_*}{200j},\quad
 \kappa_j=\kappa_*,\quad \xi_j=\frac{10000j^2}{\kappa_*^2},\quad
 s_j=\frac{\kappa_*}{j},\quad m_j=2j^4,\quad n_j=2j^4+1,
 \qquad j\ge2,\quad\kappa_*>0,
 \tag{PRE47}
\]
formula (PRE44) proves
\[
 \frac{C_{F,j}}{G_j}\le\kappa_*\mathcal B_{L_j}(\xi_j),\qquad
 \lim_{j\to\infty}
 \frac{\kappa_*\mathcal B_{L_j}(\xi_j)}{j^{16}}
       =\frac{8640000000000\,e^2}{\kappa_*^3}.
 \tag{PRE48}
\]
For the limit, the \(r_e=4\) multiplicity is
\(3m_j(m_j-1)^2\sim24j^{12}\);
its score is \(16\xi_j=160000j^2/\kappa_*^2\).
The other multiplicities are of orders \(j^4,j^8\), so after their squared-score factors they have orders \(j^8,j^{12}\). Inserting the last limit in (PRE41), including the three colour directions, gives
\(3\cdot24\cdot(75e^2/16)\cdot160000^2/\kappa_*^3
=8640000000000e^2/\kappa_*^3\).

The precise comparison with the previously evaluated separate bounds is
\[
 \frac{C_F}{G}
 \le U_{\rm sep}(L,\xi):=
 \frac{48\kappa\,\mathcal C_{\rm occ}}
 {(d^\circ)^2c_{\rm cap}(1+12\xi)^{-8}},
 \qquad
 d^\circ=\frac8{n^3}\cos(3h)\cos^3h.
 \tag{PRE49}
\]
Here IP7 gives \(C_F\le4\kappa\beta_0^2\mathcal C_{\rm occ}\);
PC49 gives \(G\ge\beta_0^2(d^\circ)^2
c_{\rm cap}(1+12\xi)^{-8}/12\), with
\(c_{\rm cap}=\cos^{14}(1/4)/(1024\cdot105041\cdot\pi\cdot3^{9/2})\).
The factor \(\beta_0^2\) cancels only in this quotient calculation; the original state is unchanged.
For an explicit comparison keep all the earlier constants:
\[
 \begin{gathered}
 S_1=\sqrt{2/n}\cot h(\cot h-\cos h),\\
 S_3=\sqrt{2/n}\left[(2-1/n)\cot^2h-(\cos h/n)\cot h\right],\\
 A_1=m\sqrt{2/n}\cot h(5\cot h-4\cos h),\\
 A_3=(m/n)\sqrt{2/n}\left[(9m+5)\cot^2h-2\cos h\cot h\right],\\
 \mathcal C_{\rm occ}
  =12\left[S_3\sqrt{S_1A_1}+S_1\sqrt{S_3A_3}\right]^2,\qquad
 \frac{\mathcal C_{\rm occ}}{n^7}
       \longrightarrow\frac{12288(38+12\sqrt{10})}{\pi^8}.
 \end{gathered}\tag{PRE50}
\]
The limit follows from \(\cot h/n\to2/\pi\), giving
\(S_1/n^{3/2}\to4\sqrt2/\pi^2\),
\(S_3/n^{3/2}\to8\sqrt2/\pi^2\),
\(A_1/n^{5/2}\to20\sqrt2/\pi^2\), and
\(A_3/n^{5/2}\to36\sqrt2/\pi^2\).
Thus \(U_{{\rm sep},j}\) has a positive finite leading coefficient times \(j^{68}\), whereas (PRE48) has order \(j^{16}\). Their ratio tends to zero. The minimum of (PRE44), (PRE45), and (PRE49) is a valid bound at every finite regulator, and the new first bound is strictly smaller than (PRE49) for all sufficiently large \(j\).

The same calculation gives the exact receiving inequality
\[
 \boxed{\displaystyle
 \mathscr E_j(s_j)\ge
       [\,1-j\mathcal B_{L_j}(\xi_j)\,]G_j.}
 \tag{PRE51}
\]
Its limitation is evaluated, rather than left as an unspecified constant:
\[
 \frac{j\mathcal B_{L_j}(\xi_j)}{j^{17}}
       \longrightarrow\frac{8640000000000\,e^2}{\kappa_*^4}>0.
 \tag{PRE52}
\]
The coefficient in (PRE51) is therefore negative for all sufficiently large \(j\). This estimate does not decide the sign of the actual endpoint. The unscaled raw vector, the positive PC52 correction, the entire six-term cancellation (PRE27), and the original spectral measure all remain available; no substitution of separate lower bounds for their ratio is made.

## 8. A precise obstruction to using the inverse response alone

The remaining defect in (PRE30) is not bounded above by the two numbers \(G,T_F\). This can be proved on the same original full Hamiltonian, retaining its potential and vacuum. Work in its physical odd subspace. It is infinite dimensional: the powers \(F,F^3,F^5,\ldots\) are linearly independent. Otherwise a nonzero polynomial would vanish on the image of the nonconstant continuous \(F\); that image contains an interval because the connected configuration space has a connected nontrivial real image, and full support turns an almost-everywhere polynomial equality into a pointwise one. Compact resolvent thus supplies infinitely many distinct positive dimensionless eigenvalues
\(\lambda_1<\lambda_2<\cdots\to\infty\) of \(\mathcal L\), with real orthonormal smooth physical odd eigenfunctions \(\phi_k\) in \(L^2(\mu)\). Here one may choose a subsequence if multiplicities occur.

Fix two such eigenvalues and put
\[
 t_*=\frac{\lambda_2-\lambda_1}{2\lambda_2}>0,\quad
 a_k=t_*\frac{\lambda_2^{-1}-\lambda_k^{-1}}
                    {\lambda_1^{-1}-\lambda_2^{-1}},\quad
 f_k=\sqrt{1+a_k}\,\phi_1
       +\sqrt{1-t_*-a_k}\,\phi_2+\sqrt{t_*}\,\phi_k,\quad k\ge3.
 \tag{PRE53}
\]
The coefficients are real: \(a_k\ge0\) and
\(t_*+a_k\le t_*\lambda_2/(\lambda_2-\lambda_1)=1/2\).
Each \(f_k\) is a complete actual physical odd test function. Direct orthogonality gives
\[
 \mu(f_k^2)=2,\qquad
 \mathfrak R(f_k,f_k)=\lambda_1^{-1}+\lambda_2^{-1},\qquad
 \mu\Gamma(f_k,f_k)
   =(1+a_k)\lambda_1+(1-t_*-a_k)\lambda_2+t_*\lambda_k
       \longrightarrow\infty.
 \tag{PRE54}
\]
The response equality follows by inserting (PRE53): its increment is
\(a_k(\lambda_1^{-1}-\lambda_2^{-1})
-t_*(\lambda_2^{-1}-\lambda_k^{-1})=0\).
Thus, on the domain of nonzero smooth real physical odd functions, the exact map into \((0,\infty)^2\times[0,\infty)\) given by
\[
 f\longmapsto
 \bigl(\mu f^2,\ \mathfrak R(f,f),\
             \mu\Gamma(f-(\mu f^2/\mathfrak R(f,f))u_f,\,
                         f-(\mu f^2/\mathfrak R(f,f))u_f)\bigr)
 \tag{PRE55}
\]
has an unbounded third component on the explicitly constructed fibre of its first two components. Equations (PRE30) and (PRE54) identify this fibre with the unresolved energy defect. This is an obstruction to a proposed inference from mass and susceptibility alone, with an exact connecting map on the original operator. It does not replace \(F\) by \(f_k\) in the requested endpoint and does not show that the actual phase has a large quotient.

The next concrete estimate after that obstruction was the weighted derivative estimate (PRE40), applied through the exact all-link degree cancellation (PRE35). It bounds precisely that previously uncontrolled energy for the original \(F\), yielding (PRE44)–(PRE52). A positive shrinking-window conclusion would require sharper information about the actual alignment in (PRE30) or (PRE31), or the complete six-term expectations in (PRE27). No such conclusion, closing gap, or continuum result follows from the present bounds.
