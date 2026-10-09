# Full cusp coupling and physical kernels of the classical holonomy family

**Reviewed edition, 8 October 2026:** complete finite-scale proofs, the corrected
same-coupling path and sixty passing exact checks. The results stop at the
specified finite physical vectors and operators. The continuum construction
and programme endpoint remain active.

30 September 2026. This note constructs the full angular cusp pullback of
the retained bundle and its actual classical solution family. It then maps
the actual link configurations to nonzero gauge-invariant quantum vectors
on the original finite lattice, computes their Gram and full Hamiltonian
kernels, and constructs a nonzero vector orthogonal to the actual vacuum.
Sections 8–9 fix a joint path and compute its first electric projection and
the exact interacting return through the complementary space.
No continuum spectral conclusion is claimed here.

![Actual fields, reflected core cubes and the complete interacting return](figures/PERIOD_PHYSICAL_KERNELS.png)

*The coordinate drawing is a schematic projection of the original core and its
reflection at \(s=0\). It retains both cubes and their complete face count.
The operator diagram is the exact identity PK54 on the reflection-odd physical
space. The full hypotheses and proofs are PK38–PK54; the complete classical
energy bracket is PK43f. Reproducible source:
[period_physical_figure.py](figures/period_physical_figure.py).*

## 1. Inputs, coordinates and source conventions

The original objects are the bundle \(P_H\to X\), its rank-24 associated
bundle \(\mathcal W_H\), the map \(\mathcal M_H\), and its global
classical Cauchy solution \(A(v;s,x)\), with \(s=ct\). Complete proofs are
in [the Cauchy continuation, CE1–CE45](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/7d5681ed53835433a5fb72d880b6292832f2efbf/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/COMPACT_SUPPORT_CAUCHY_EVOLUTION.md)
and [the higher-carrier continuation, HC1–HC12](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/7d5681ed53835433a5fb72d880b6292832f2efbf/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/HIGHER_CARRIER_AND_EVOLUTION.md).
The complete period input and the original lattice Hamiltonian are retained
in [Spatial continuum, Sections 1–2](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/7d5681ed53835433a5fb72d880b6292832f2efbf/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/sources/spatial/spatial_continuum.tex#L113).
Its radial formulas are now extended through the entire angular coordinate.

To avoid confusing the physical support radius \(R\) with cusp depth,
write the original cusp depth as \(T\). Keep
\[
 t_c=e^{-2\pi T+i\phi},\qquad
 \sigma=\frac{\phi}{2\pi}+iT,\qquad
 \mu=\mu(t_c),\quad \tau=\sigma+h(t_c),\quad
 \beta=b_{\rm per}(t_c)-\sigma-h(t_c).
 \tag{PK1}
\]
Here \(h,\mu,b_{\rm per}\) are the original holomorphic functions,
including every bounded correction. Define
\[
 \begin{gathered}
 a=\operatorname{Re}\mu,\ m=\operatorname{Im}\mu,
 u=\operatorname{Re}\tau,\ L=\operatorname{Im}\tau,
 d=\operatorname{Im}b_{\rm per},\ q=L-d,
 c_0=\operatorname{Re}\beta,\\
 P=\begin{pmatrix}6a&u&1&0\\6m&L&0&0\\c_0&a&0&1\\-q&m&0&0\end{pmatrix},
 \quad D=Lq+6m^2>0,
 \quad A_{\rm per}=\begin{pmatrix}6a&u\\c_0&a\end{pmatrix},
 \quad B=\begin{pmatrix}6m&L\\-q&m\end{pmatrix}.
 \end{gathered}\tag{PK2}
\]
The source's \(p\) is exactly \(-q\); its \(\delta\) is exactly \(D\).
This dictionary preserves the original real coordinate order
\((\operatorname{Re}z_1,\operatorname{Im}z_1,
\operatorname{Re}z_2,\operatorname{Im}z_2)\).

The finite-state construction is the real-label part of the heat-kernel
construction of [Brian C. Hall, arXiv:1707.02355v1, Sections 1.2–1.3](https://arxiv.org/abs/1707.02355v1),
and its gauge average is the construction in
[Benjamin Bahr and Thomas Thiemann, arXiv:0709.4636v1, Sections 2, 3 and 4.2](https://arxiv.org/abs/0709.4636v1).
The exact convention comparison is supplied in Section 5. Complex labels,
their additional identifications, and semiclassical asymptotics from those
papers are not imported. All arguments needed for the results here follow
below. Original author TeX, reading coverage and exact hashes are recorded
in SOURCE_PROVENANCE.md and the private reading ledger.

## 2. Angular monodromy, determinant and the complete covered metric

Put
\[
 N_0=\begin{pmatrix}0&0&0&0\\0&0&0&0\\0&1&0&0\\-1&0&0&0\end{pmatrix},
 \quad M_0=I+N_0,\qquad S_M=\operatorname{diag}(1,1,M,M),\quad M\in\mathbb N.
 \tag{PK3}
\]
Directly from (PK1), continuation of the logarithm by
\(\phi\mapsto\phi+2\pi\) changes \(\tau\) to \(\tau+1\) and
\(\beta\) to \(\beta-1\), while leaving all three holomorphic functions
unchanged. Consequently
\[
 P(T,\phi+2\pi)=P(T,\phi)M_0,\quad N_0^2=0,\quad
 M_0^M=I+MN_0,\quad S_M^{-1}M_0^MS_M=M_0.
 \tag{PK4}
\]
These equations fix the orientation by the displayed logarithm change.
The earlier source calls its printed matrix clockwise and later refers to
a positive loop. No conclusion here relies on that verbal convention:
reversing the displayed logarithm change replaces \(M_0\) by its inverse.

On the covering base use
\(v_c=e^{-2\pi T/M+i\theta}\), so \(t_c=v_c^M\) and
\(\phi=M\theta\). The covered marked torus is
\[
 \widetilde F_{T,\theta,M}=\mathbb R^4/P(T,M\theta)S_M\mathbb Z^4.
 \tag{PK5}
\]
Its marked presentation identifies
\[
 (T,\theta,y)\sim(T,\theta+2\pi,M_0^{-1}y),\qquad
 y\in\mathbb R^4/\mathbb Z^4.
 \tag{PK6}
\]
Indeed \(P(T,M\theta+2\pi M)S_MM_0^{-1}y=P(T,M\theta)S_My\).
This proves the gluing, not just invariance of a determinant. The map
\([P S_My]\mapsto[P S_My]\) to the original fibre has degree \(M^2\)
and deck group \((\mathbb Z/M\mathbb Z)^2\), since the lattice quotient
is \(\mathbb Z^4/S_M\mathbb Z^4\).

Reorder covering rows only as \((x^1,x^3;x^2,x^4)\). The row permutation
has sign \(-1\). In this order
\[
 Q=\begin{pmatrix}A_{\rm per}&MI_2\\B&0\end{pmatrix},\quad
 Q^{-1}=\begin{pmatrix}0&B^{-1}\\M^{-1}I_2&-M^{-1}A_{\rm per}B^{-1}\end{pmatrix},
 \quad B^{-1}=D^{-1}\begin{pmatrix}m&-L\\q&6m\end{pmatrix}.
 \tag{PK7}
\]
Multiplying both ways proves the inverse. Thus in the original order
\[
 \det(PS_M)=-M^2D,\quad
 G_M=S_M^{\mathsf T}P^{\mathsf T}PS_M,\quad
 \sqrt{\det G_M}=M^2D,
 \tag{PK8}
\]
with inverse metric, in the unchanged marked-column order,
\[
 G_M^{-1}=Q^{-1}Q^{-\mathsf T}
 =\begin{pmatrix}
 B^{-1}B^{-\mathsf T}&-M^{-1}B^{-1}B^{-\mathsf T}A_{\rm per}^{\mathsf T}\\
 -M^{-1}A_{\rm per}B^{-1}B^{-\mathsf T}&
 M^{-2}(I_2+A_{\rm per}B^{-1}B^{-\mathsf T}A_{\rm per}^{\mathsf T})
 \end{pmatrix}.
 \tag{PK9}
\]
Every angular real-part term survives in this formula. Re-marking by
(PK6) gives the congruence law for \(G_M\); it does not identify the
matrix entries in two different markings.

Here are uniform bounds with explicit roles for the constants. Fix a
sufficiently small closed cusp disk on which the three holomorphic
functions are bounded, and then \(T\ge T_0\). There are finite constants
\(C_B,C_A\), defined respectively as bounds on
\(\|B-TJ\|\) and
\(\|A_{\rm per}-(\phi/(2\pi))J\|\), where
\(J=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\).
Enlarge \(T_0\) so that \(T_0>C_B\); the preceding fixed disk bounds
remain valid on the smaller end.
On \(0\le\theta\le2\pi\),
\[
 T-C_B\le\sigma_{\min}(B)\le\sigma_{\max}(B)\le T+C_B,
 \qquad \|A_{\rm per}\|\le M+C_A.
 \tag{PK10}
\]
The first inequalities follow from \(|TJz|=T|z|\) and the triangle
inequality. They imply
\[
 \begin{split}
 \sigma_{\min}(PS_M)&\ge
 \left[M^{-1}+\frac{1+\|A_{\rm per}\|/M}{T-C_B}\right]^{-1},\\
 \sigma_{\max}(PS_M)&\le \|A_{\rm per}\|+M+T+C_B,\\
 \operatorname{sys}(\widetilde F_{T,\theta,M})&\ge\min(T-C_B,M).
 \end{split}\tag{PK11}
\]
For the first use (PK7) and bound its three nonzero blocks separately;
\(\sigma_{\min}=\|Q^{-1}\|^{-1}\). The second uses the three blocks of
\(Q\). For the third, a period has the exact form
\((A_{\rm per}n+Mz,Bn)\), \(n,z\in\mathbb Z^2\). If \(n\ne0\),
its second block has length at least \(T-C_B\); otherwise its first
block has length at least \(M\). No real-part correction is discarded.

Holomorphy also gives, uniformly in the original angular variable,
\[
 D=T^2+(2h_0-d_0)T+(h_0^2-d_0h_0+6m_0^2)
       +O(Te^{-2\pi T}),
 \tag{PK12}
\]
where \(h_0=\operatorname{Im}h(0)\),
\(d_0=\operatorname{Im}b_{\rm per}(0)\),
\(m_0=\operatorname{Im}\mu(0)\). Substitution of
\(L=T+\operatorname{Im}h(t_c)\), \(q=L-\operatorname{Im}b_{\rm per}(t_c)\)
in (PK2) proves every term.

## 3. Exact bundle pullback and low modes on the full end

Let \(\mathcal C\subset X\) be the original regular cusp
\(0<|t_c|<\epsilon\). Let \(\mathcal C_M\) be its covered family (PK5)–(PK6),
and \(c_M:\mathcal C_M\to\mathcal C\hookrightarrow X\) the actual
cover map, including the base change. Define
\[
 P_M=c_M^*P_H,\quad \mathcal W_M=c_M^*\mathcal W_H,\quad
 \mathcal A_M=c_M^*\mathcal A_H,\quad
 r_M=r_Hc_M:\mathcal C_M\to F_4/\rho(\operatorname{Sp}(1)).
 \tag{PK13}
\]
The bundle isomorphism in HC4 pulls back to
\(P_M\cong r_M^*(F_4\to F_4/\rho(\operatorname{Sp}(1)))\).
Explicitly \((z,p)\mapsto(z,a(p))\), with \(a(p)\) from HC5, is the
map, with inverse supplied by that same fibrewise bijection. This proves
the relation to the higher carrier on the whole covered end.

The original Hopf coordinate, on its open cell, remains
\[
 z_H=-\cot(\pi r_c/\epsilon)-\cot(\phi/2)\mathbf i
       -\cot(\pi u_1)\mathbf j-\cot(\pi u_2)\mathbf k,
 \quad r_c=e^{-2\pi T},\quad \phi=M\theta,
 \quad u_1=y_1,\ u_2=y_2.
 \tag{PK14}
\]
The last two equalities use the first two entries of \(S_My\).
Those entries are fixed by \(M_0\). Hence (PK14), its based extension,
and the exact transition \(g(z_H)=\overline z_H/|z_H|\) respect (PK6).
The entire angle is retained; it is not identified with a half-angle
rotation in the structure group. The nonzero global clutching class over
\(X\) remains the one proved by `rettri:bundleclass` in the
[retained source](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/7d5681ed53835433a5fb72d880b6292832f2efbf/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/sources/higher_rung/s6_higher_rung_24d_preprint.tex#L5281).

There is a useful strengthening about the end itself. Restrict to
\(r_c<\epsilon/2\). On the open cell
\[
 |z_H|\ge\cot(\pi r_c/\epsilon)>0,\qquad
 w_H=z_H^{-1}=\overline z_H/|z_H|^2.
 \tag{PK15}
\]
At every collapsed angular or torus seam set \(w_H=0\). This is
continuous: approaching a seam makes at least one squared cotangent
diverge, hence \(|w_H|=|z_H|^{-1}\to0\). It also tends uniformly to zero
as \(r_c\to0\), by (PK15). Therefore the literal Hopf section
\[
 s_\infty(w_H)=\frac{(w_H,1)}{\sqrt{1+|w_H|^2}}
 \tag{PK16}
\]
is a global continuous section of \(P_M\) on this end. Its pullback
transition to \(s_0(z_H)\) is precisely the original \(g(z_H)\).
Thus the restriction to this noncompact end is trivial, even though the
bundle over the whole \(X\) is nontrivial. This is proved by a section;
it does not erase the global clutching class.

The smooth bundle structure constructed in HC4 can be used on the end.
A smooth trivialization exists as well: view (PK16) as a continuous unit
section of its associated quaternionic line; a locally finite smooth
partition of unity and local approximation give a smooth section within
fibre norm \(1/2\) of it. Dividing that section by its displayed positive
norm gives a smooth unit section. The straight interpolation with (PK16),
divided by its norm, is a continuous homotopy of nowhere-zero sections.
It is an isomorphism of the same bundle, not a differentiability assertion
about the literal collapsed source coordinates. Formula (PK14) remains
the topological comparison map.

Pullback of CE34 now gives, without a newly assumed evolution theorem,
\[
 \mathfrak E_M:\mathcal W_M\longrightarrow P_M\times_{\operatorname{Sp}(1)}\mathscr S,
 \quad [p,v]\longmapsto[p,A(v;s,x)].
 \tag{PK17}
\]
Its equivariance is CE33; both pullback compositions agree pointwise.
The zero subbundle and vertical ranks remain \(12\) and \(0,3,6,9\).
The same statement applies to the dilation family of CE38–CE45 for every
\(\lambda>0\), including its support \(|x|\le\lambda R+|s|\).
Smoothness is in the retained smooth bundle coordinates. It is not an
unproved uniform derivative estimate at the completed cusp.

The full dual spectrum also descends. Write \(k=(n,z)\in\mathbb Z^2\oplus\mathbb Z^2\).
Equations (PK7)–(PK9) give
\[
 \Lambda_{T,\theta,M;k}=4\pi^2\left[
  M^{-2}|z|^2+
  \left|B^{-\mathsf T}(n-M^{-1}A_{\rm per}^{\mathsf T}z)\right|^2\right].
 \tag{PK18}
\]
The corresponding character is
\(\exp(2\pi i\langle P^{-\mathsf T}S_M^{-1}k,x\rangle)\).
The transformation \(y\mapsto M_0^{-1}y\) transports its label to
\(k\mapsto M_0^{\mathsf T}k\); inserting this in the transformed metric
proves spectral invariance. The original fibre characters are exactly
the covered labels with \(k_3,k_4\) divisible by \(M\).

For completeness, an explicit full low-mode count follows from the
singular-value estimate. Fix \(E>0\), set
\(\rho_E=\sqrt E/(2\pi)\),
\(s_* =\sigma_{\min}(PS_M)\), and suppose \(\rho_Es_*>1\).
Let \(N(E)\) count the nonzero labels with eigenvalue at most \(E\).
Then
\[
 (1-(\rho_Es_*)^{-1})^4\frac{E^2M^2D}{32\pi^2}
 \le N(E)+1\le
 (1+(\rho_Es_*)^{-1})^4\frac{E^2M^2D}{32\pi^2}.
 \tag{PK19}
\]
Indeed the ellipsoid of allowed real labels is
\((PS_M)^{\mathsf T}\overline B_{\rho_E}\), of volume
\(M^2D\,\pi^2\rho_E^4/2\). Each point in a unit lattice cube is within
distance one of its centre in four dimensions. The ellipsoid contains
\(B_{\rho_Es_*}\). Its outer unit neighbourhood is contained in its
\(1+1/(\rho_Es_*)\) dilate; its inner such dilate lies in the union
of cubes whose centres it contains. Comparing volumes proves (PK19).
Boundary cubes can be made half-open, so they do not change the count.

For the joint path \(T=j^6,M=j^4\) prescribed in Section 8,
(PK10)–(PK11) give \(s_*\ge j^4/2\) at the explicit threshold there.
Consequently (PK19) retains the full factor
\(E^2j^8D/(32\pi^2)\), with multiplicative bounds
\((1-2/(\rho_Ej^4))^4\) and \((1+2/(\rho_Ej^4))^4\)
when \(\rho_Ej^4>2\). In particular no bounded correction inside \(D\)
is discarded. Also
\[
 \frac{4\pi^2}{(T+C_B+M+\|A_{\rm per}\|)^2}
 \le\Lambda_1\le\frac{4\pi^2}{(T-C_B)^2}.
 \tag{PK20}
\]
The lower bound uses \(|k|\ge1\); for the upper bound use a unit label
\((n,0)\) and (PK10). These are scalar geometric modes. The quantum
Hamiltonian below is a different operator whose connection to these
scales must be tested using its actual kernels.

## 4. Receiving the actual fields in the original lattice

The physical coordinate permutation from the source is
\[
 (y^0,y^1,y^2,y^3)=(x^3,x^2,x^4,x^1).
 \tag{PK21}
\]
It has determinant \(+1\). Denote its matrix by \(\mathsf S\).
On any ball of radius \(b_*\) with
\(4b_*<\min(T-C_B,M)\), the quotient to (PK5) is an isometric embedding.
The proof is \(|x-x'+\ell|\ge|\ell|-2b_*>2b_*\) for every nonzero
period. A physical path \(\gamma\) in this patch has marked coordinates
\[
 \eta=(PS_M)^{-1}\mathsf S^{-1}\gamma.
 \tag{PK22}
\]
The pulled-back one-form has components
\(\widetilde A_a=\sum_\mu(\mathsf S PS_M)_{\mu a}
A_\mu(\mathsf S PS_M\eta)\); its curvature is the exterior-square
pullback. The chain rule retains each derivative and bracket. Along
(PK22), the period matrix and its inverse cancel in the transport ODE,
proving equality of its holonomy with the actual physical path holonomy.
This cancellation is a proved map with all matrices present, not deletion
of the period data. Equations (PK4)–(PK6) prove angular compatibility.

This construction uses physical patches of the Euclidean torus carrier.
The physical evolution remains the Lorentzian Cauchy solution on
\(\mathbb R^{1+3}\). It does not identify physical time periodically or
assert that the solution closes around a torus time cycle. Its entire
curvature is pulled back on every patch where it is used.

Fix a positive integer \(L\ge1\) and the original open cubic graph with
vertices \(\{-L,\ldots,L\}^3\),
spacing \(a>0\), and a specified physical origin \(o\), so an edge
is \(\gamma_{n,i}(t)=o+a(n+te_i)\). Let \(H_e(A)\) be CE42's forward
transport. Define the lattice centre
\[
 h_e=H_e(A)^{-1}.
 \tag{PK23}
\]
CE43 gives \(h_e(A^q)=q_{s(e)}h_eq_{t(e)}^{-1}\), exactly the original
lattice action. This inverse is essential. All reversed edges are the
inverses of the same variables; they are not independent variables.

Put
\[
 N_L=3(2L)(2L+1)^2,\quad M_L=3(2L)^2(2L+1),\quad Q_L=SU(2)^{N_L},
 \quad dU=\prod_e dU_e,
 \tag{PK24}
\]
where each Haar measure has total mass one. For \(T_a=-i\sigma_a/2\),
let \(X_{e,a}\) differentiate \(U_e\mapsto e^{tT_a}U_e\). The complete
Hamiltonian is
\[
 H=\kappa\sum_e E_e+b\sum_p(2-W_p),\quad
 E_e=-\sum_aX_{e,a}^2,\quad \kappa=\frac{2g^2}{a},\quad
 b=\frac1{2g^2a},\quad W_p=\operatorname{tr}
 (U_i(n)U_j(n+e_i)U_i(n+e_j)^{-1}U_j(n)^{-1}).
 \tag{PK25}
\]
Its domains are \(H^2(Q_L)\) and form domain \(H^1(Q_L)\), because
the potential is smooth and \(0\le V\le4bM_L\). The physical Hilbert
space is the range of the orthogonal Haar projection
\[
 (\Pi f)(U)=\int_{SU(2)^{V_L}}f(q\cdot U)\,dq,\qquad
 (q\cdot U)_e=q_sU_eq_t^{-1}.
 \tag{PK26}
\]
Haar invariance proves self-adjointness and idempotence; the image is
exactly the invariant functions. Each \(E_e\) commutes with the action,
and every \(W_p\) is conjugated at its base vertex, so \(H\Pi=\Pi H\).
The source Lie metric is \(-\operatorname{tr}(XY)/2\), for which
\(\Delta^c=4\sum_aX_a^2\). It is one quarter of CE4's matrix metric.
Thus (PK25) retains the original electric coefficient; none is transferred
silently into a metric or a coupling.

## 5. Nonzero physical vectors and their exact Gram kernel

For \(t>0\) define the heat kernel in the original \(T_a\) convention
\[
 p_t(U)=\sum_{j\in\frac12\mathbb Z_{\ge0}}(2j+1)e^{-tj(j+1)}\chi_j(U).
 \tag{PK27}
\]
Every derivative series converges uniformly: derivatives of a spin-\(j\)
matrix are bounded by powers of \(j\), whereas the exponential is
quadratic in \(j\). Orthogonality of matrix coefficients proves
\(p_t*p_s=p_{t+s}\), \(\int p_t=1\), and
\(\partial_tp_t=-E p_t\). The compact connected-group heat equation
and the strong maximum principle give \(p_t>0\). In particular all
packets below are smooth vectors in every Sobolev domain.

The exact source comparisons are as follows. Bahr–Thiemann's real-label
packet with parameter \(2t\) is \(p_t(Uh^{-1})\), using trace cyclicity
and \(\chi_j(k^{-1})=\chi_j(k)\) on \(SU(2)\). Hall uses
\(\partial_t\rho=\Delta^c\rho/2=-2E\rho\) with his displayed
\(SU(2)\) metric \(-\operatorname{tr}(XY)/2\); hence
\(\rho_{t/2}=p_t\). These factors refer to smoothing parameters,
not to the coupling or Planck's constant of (PK25).

For positive edge parameters \(\mathbf t=(t_e)\), set
\[
 f_{h,\mathbf t}(U)=\prod_e p_{t_e}(U_eh_e^{-1}),\qquad
 \Phi_{h,\mathbf t}=\Pi f_{h,\mathbf t}
 =\int dq\prod_e p_{t_e}(U_e(q\cdot h)_e^{-1}).
 \tag{PK28}
\]
The second equality follows by substituting inverse vertex variables and
using conjugation invariance of \(p_t\). It proves that \(\Phi\) depends
only on the gauge orbit of \(h\). Positivity and unit integral give
\[
 \Phi_{h,\mathbf t}>0,\qquad \int\Phi_{h,\mathbf t}\,dU=1,
 \qquad \|\Phi_{h,\mathbf t}\|_2^2\ge1.
 \tag{PK29}
\]
Thus physical projection does not annihilate any of these actual
classical configurations. In particular simultaneous colour conjugation
from a change of frame in \(P_M\) disappears under \(\Pi\); (PK28)
therefore gives a well-defined map on the entire associated bundle.
The equal-field circles and all spectator directions of CE34a retain
exactly equal vectors. No parameter labels have been made orthogonal.

The exact raw Gram kernel is
\[
 G(h,k;\mathbf t,\mathbf s)
 =\langle\Phi_{h,\mathbf t},\Phi_{k,\mathbf s}\rangle
 =\int dq\prod_e p_{t_e+s_e}(h_e(q\cdot k)_e^{-1}).
 \tag{PK30}
\]
To prove it, use \(\Pi^*=\Pi^2=\Pi\), integrate the two heat kernels
on each original link, and apply their convolution law. The same result
comes from the two vertex integrals in (PK28), followed by their relative
vertex change. It is real, strictly positive, symmetric under exchanging
the two labelled packets, and positive semidefinite as a Gram kernel.

There are no further identifications for real labels at a fixed
\(\mathbf t\), apart from gauge orbits. Indeed (PK28) is the product heat
operator applied to the orbit probability measure \(\nu_h\). Every
Peter–Weyl coefficient is multiplied by the nonzero number
\(\exp(-\sum_et_ej_e(j_e+1))\). Equality of packets gives equality of
all Fourier coefficients of the two measures. Matrix coefficients form a
self-adjoint algebra separating points, so their uniform density gives
equality of the measures. The support of \(\nu_h\) is exactly the
compact orbit of \(h\): every nonempty open set meeting the orbit has
positive Haar preimage. Equality of the measures therefore gives equality
of their orbits. This argument also proves that distinct-orbit packets
cannot be proportional, since their integrals are both one. More strongly,
a finite collection of packets at distinct gauge orbits and fixed heat
parameters is linearly independent. A vanishing linear combination, after
the same injective heat operation, gives a vanishing linear combination of
orbit measures. Their compact supports are disjoint. Restricting the measure
to each of those Borel supports gives its coefficient zero. Thus the Gram
matrix is strictly positive definite on each such finite collection.

## 6. Full Hamiltonian kernel, including every magnetic face

Write \(x_e=(q\cdot h)_e\), \(y_e=(r\cdot k)_e\). Define one-link
scalar and matrix functions
\[
 Z_e(x,y)=p_{t_e+s_e}(xy^{-1}),\qquad
 R_e^{\pm}(x,y)=\int_{SU(2)}p_{t_e}(Ux^{-1})p_{s_e}(Uy^{-1})U^{\pm1}\,dU.
 \tag{PK31}
\]
For each oriented face with ordered distinct edges
\((e_1^{\epsilon_1},\ldots,e_4^{\epsilon_4})\), put
\[
 B_p(h,k)=\int dq\,dr\;
 \left(\prod_{e\notin\partial p}Z_e(x_e,y_e)\right)
 \operatorname{tr}\left(
 R_{e_1}^{\epsilon_1}(x_{e_1},y_{e_1})
 R_{e_2}^{\epsilon_2}(x_{e_2},y_{e_2})
 R_{e_3}^{\epsilon_3}(x_{e_3},y_{e_3})
 R_{e_4}^{\epsilon_4}(x_{e_4},y_{e_4})\right).
 \tag{PK32}
\]
The order in this trace is the original face order. Link integration in
\(\langle\Phi_h,W_p\Phi_k\rangle\) proves precisely (PK32); no
commuting replacement of the four matrices is made. Differentiating the
right packet in (PK28) proves the full answer
\[
 K(h,k;\mathbf t,\mathbf s)
 :=\langle\Phi_{h,\mathbf t},H\Phi_{k,\mathbf s}\rangle
 =-\kappa\sum_e\partial_{s_e}G
       +2bM_LG-b\sum_pB_p.
 \tag{PK33}
\]
Every original boundary face, scalar Wilson term and electric coefficient
is retained. All differentiations are justified by the uniformly
convergent series following (PK27).

The integrals in these formulas have a completely specified convergent
algebraic evaluation. Here is one that also fixes their representation
conventions. Let \(D^j=\operatorname{Sym}^{2j}(U)\) in the orthonormal
symmetric-tensor basis, with indices \(0\le r,s\le n=2j\). For
\(U=\left(\begin{smallmatrix}a&b\\c&d\end{smallmatrix}\right)\),
\[
 D^j(U)_{rs}=\sqrt{\frac{\binom ns}{\binom nr}}
 \sum_{k=\max(0,r-n+s)}^{\min(r,s)}
 \binom{n-s}{r-k}\binom sk
 a^{n-s-r+k}c^{r-k}b^{s-k}d^k.
 \tag{PK34}
\]
This follows by expanding the two factors
\((az_1+cz_2)^{n-s}(bz_1+dz_2)^s\), with the displayed symmetric
basis factors. Thus it is an explicit finite matrix, including its signs.

For a list of these representations or their complex conjugates, let
\(T_a^{\rm tot}\) be the sum of their infinitesimal matrices in the
corresponding tensor slots, and \(C=-\sum_a(T_a^{\rm tot})^2\).
Let \(J_{\max}\) be the sum of their spins. Their Haar matrix is
\[
 Q^{\rm list}=\int \bigotimes_\ell D^{j_\ell}(U)\,dU
 =\begin{cases}
 0,&J_{\max}\in\mathbb Z+\tfrac12,\\
 \displaystyle\prod_{J=1}^{J_{\max}}\left(I-\frac{C}{J(J+1)}\right),
      &J_{\max}\in\mathbb Z.
 \end{cases}\tag{PK35}
\]
Conjugated slots use the conjugated matrices in this equation; the empty
product is the identity. To prove it, Haar averaging is the orthogonal
projection onto invariant tensors. The finite-dimensional unitary
\(SU(2)\) representation decomposes orthogonally by its highest weights:
starting with a largest eigenvector of \(iT_3^{\rm tot}\), repeated
lowering gives the spin-\(J\) string with Casimir \(J(J+1)\); its
orthogonal complement is invariant, so induction exhausts the tensor
space. Its weights have the parity of \(J_{\max}\) and absolute value
at most \(J_{\max}\). Thus the polynomial in (PK35) is one on the
spin-zero space and zero on every possible nonzero spin. For half-integral
parity there is no zero spin. This proves the formula, even when some of
the listed integer spins do not occur.

In particular, the entries of (PK31) are exactly
\[
 \begin{split}
 (R^+)_{ab}(x,y)
 &=\sum_{j,k}d_jd_ke^{-t j(j+1)-s k(k+1)}
   \sum_{m,n,p,q}D^j(x^{-1})_{nm}D^k(y^{-1})_{qp}
   Q^{j,k,1/2}_{(m,p,a),(n,q,b)},\\
 (R^-)_{ab}(x,y)
 &=\sum_{j,k}d_jd_ke^{-t j(j+1)-s k(k+1)}
   \sum_{m,n,p,q}D^j(x^{-1})_{nm}D^k(y^{-1})_{qp}
   Q^{j,k,\overline{1/2}}_{(m,p,b),(n,q,a)},
 \qquad d_j=2j+1.
 \end{split}\tag{PK36}
\]
Expanding each heat trace proves the first equation. The second uses
\((U^{-1})_{ab}=\overline U_{ba}\), hence the transposed indices shown.
The remaining vertex averages in (PK30) and (PK32) are evaluated by the
same (PK35) at each vertex, with the exact incoming conjugated slots.
The polynomial growth in dimensions and the heat exponential give absolute
convergence of these sums and all finite derivatives. Thus (PK30)–(PK36)
specify actual computable kernels, including the entire nonlinear
magnetic interaction, rather than a diagonal assignment to labels.

## 7. A nonzero vector exactly orthogonal to the actual vacuum

We now construct an excitation, not merely a positive physical packet.
The original \(H\) has compact resolvent. A ground minimizer can be
chosen nonnegative because \(|\nabla|f||\le|\nabla f|\); the functions
\((|f|^2+\varepsilon^2)^{1/2}\) justify this at zeros. Elliptic regularity
and the strong maximum principle give a smooth strictly positive minimizer
\(\psi\), with eigenvalue \(E_0\) and \(\int\psi^2=1\).
The exact identity
\[
 \langle\psi F,(H-E_0)\psi F\rangle
 =\kappa\sum_{e,a}\int\psi^2|X_{e,a}F|^2dU
 \tag{PK37}
\]
follows by the product rule and integration by parts. Another ground
vector divided by \(\psi\) has all derivatives zero, so it is constant
on connected \(Q_L\). This proves uniqueness. Gauge actions and graph
reflections preserve \(H\), positivity and norm, so they fix \(\psi\).
The bounds \(0\le E_0\le2bM_L\) follow from positivity and the unit
constant trial vector, whose mean Wilson trace is zero on every face.

Let \(\mathcal R\) be the graph reflection \(n_1\mapsto-n_1\).
For reversed edges it also inverts the link; the other edges are permuted.
It is an involution preserving product Haar measure, \(\sum E_e\),
and the sum of all face traces. With a common heat parameter \(t>0\),
it sends \(\Phi_{h,t}\) to \(\Phi_{\mathcal Rh,t}\). Define
\[
 \eta_{h,t}=\Phi_{h,t}-\Phi_{\mathcal Rh,t}.
 \tag{PK38}
\]
It is gauge invariant and reflection odd, so
\(\langle\psi,\eta_{h,t}\rangle=0\) exactly. Its complete kernels are
\[
 \begin{split}
 G^- (h,k)&=G(h,k)-G(h,\mathcal Rk)-G(\mathcal Rh,k)+G(\mathcal Rh,\mathcal Rk),\\
 K^- (h,k)&=K(h,k)-K(h,\mathcal Rk)-K(\mathcal Rh,k)+K(\mathcal Rh,\mathcal Rk),\\
 \Gamma(h)&=G^-(h,h)=2[G(h,h)-G(h,\mathcal Rh)].
 \end{split}\tag{PK39}
\]
No norm division or vacuum overlap has been omitted.

Here is an actual field and graph for which \(\Gamma>0\). Use the
equal-colour initial input, dilated by \(\lambda>0\), at \(s=0\).
Choose \(a\) with \(\sqrt2a<\lambda r\) and \(0<a/\lambda<\pi\).
Let \(K\) be an integer with \(aK>2\lambda R\), choose \(L>K+2\),
and set the physical origin \(o=(aK,0,0)\). The face starting at
\(n=(-K,0,0)\) lies in the original core. There
\(\varphi(A_i)=2T_i/\lambda\), so (PK23) gives its exact face word
\[
 h_p=e^{2aT_1/\lambda}e^{2aT_2/\lambda}
              e^{-2aT_1/\lambda}e^{-2aT_2/\lambda},\qquad
 W_p(h)=2-4\sin^4(a/\lambda)<2.
 \tag{PK40}
\]
To verify the trace, insert
\(e^{2aT_i/\lambda}=\cos(a/\lambda)I+2T_i\sin(a/\lambda)\),
multiply the four matrices using
\(T_iT_j=-\delta_{ij}I/4+\epsilon_{ijk}T_k/2\), and take the trace.
Every point of the reflected face has first coordinate at least
\(2aK-a>\lambda R\) after enlarging \(K\), if necessary, by one.
There \(C=0\), hence all four links are the identity and
\(W_p(\mathcal Rh)=2\). Thus the two configurations are not gauge
equivalent. The real-label injectivity proved after (PK30) gives
\(\eta_{h,t}\ne0\). This proves a nonzero, smooth, finite-energy
physical vector orthogonal to the actual interacting finite-lattice vacuum.

There is also a quantitative raw-norm lower bound. A face Wilson trace
is an electric eigenfunction with eigenvalue
\(4\cdot(3/4)=3\); each of its four links occurs in the fundamental
representation. Equations (PK27)–(PK28) therefore give
\[
 \int W_p(U)\Phi_{h,t}(U)dU=e^{-3t}W_p(h).
\]
Its Haar squared norm is one: integrating three links reduces its
holonomy to a single Haar element, and character orthogonality gives
\(\int\chi_{1/2}^2=1\). Cauchy–Schwarz applied to (PK38) proves
\[
 \Gamma(h)\ge e^{-6t}|W_p(h)-W_p(\mathcal Rh)|^2
       =16e^{-6t}\sin^8(a/\lambda)>0.
 \tag{PK41}
\]
This bound retains the decreasing amplitude; it is not a uniform
positive lower bound in a limit with \(a/\lambda\to0\).

For an explicit finite energy control put
\(D_h=-\sum_e\partial_{s_e}G(h,h;\mathbf t,\mathbf s)|_{\mathbf s=\mathbf t}\).
This is \(\sum_{e,a}\|X_{e,a}\Phi_{h,t}\|_2^2\ge0\). Reflection
invariance and \(|u-v|^2\le2|u|^2+2|v|^2\) give
\[
 0<\frac{K^-(h,h)-E_0\Gamma(h)}{\Gamma(h)}
 \le \frac{4\kappa D_h}{\Gamma(h)}+4bM_L.
 \tag{PK42}
\]
The strict inequality follows from uniqueness of the ground state and
\(\eta\ne0\); all vectors are in the operator domain. The upper bound
is finite and explicit in the kernels. It is not claimed to tend to zero.

## 8. One fixed joint path and the next actual spectral calculation

Fix \(\kappa_*>0\), \(t_*>0\), the original cutoff \(\chi,r,R\), and
the original physical unit \(\ell_*=1\), the length of its real period
vector. Use the same \(g_j\) in the classical physical energy and the
quantum Hamiltonian. Before estimating any spectral limit, prescribe
\[
 \begin{gathered}
 T_j=j^6,\quad M_j=j^4,\quad v_{c,j}=e^{-2\pi j^2},\quad
 a_j=\frac1{100j},\quad L_j=j^4,\quad
 g_j^2=\frac{\kappa_*}{200j},\quad t_j=t_*,\quad \lambda_j=j^2,\\
 K_j=\left\lceil\frac{3\lambda_jR}{a_j}\right\rceil+1,\qquad
 o_j=(a_jK_j,0,0),\quad h_j=H(A^{[\lambda_j]}(0))^{-1},
 \quad \eta_j=\Phi_{h_j,t_*}-\Phi_{\mathcal Rh_j,t_*}.
 \end{gathered}\tag{PK43}
\]
The base identity remains exact:
\(v_{c,j}^{M_j}=e^{-2\pi j^6}\). The full graph and Hamiltonian constants are
\[
 \begin{gathered}
 N_{L_j}=3(2j^4)(2j^4+1)^2,\qquad
 M_{L_j}=3(2j^4)^2(2j^4+1),\\
 \kappa_j=\kappa_*,\qquad b_j=\frac{10000j^2}{\kappa_*},\qquad
 \xi_j=\frac{10000j^2}{\kappa_*^2},\qquad
 \frac{a_j}{\lambda_j}=\frac1{100j^3},\qquad
 K_j=\lceil300Rj^3\rceil+1 .
 \end{gathered}\tag{PK43a}
\]
In particular every original edge and face remains in (PK25).

Here is one sufficient threshold, including the small-core condition.
Increase the already fixed \(T_0\), if needed, so (PK10) holds and
\(e^{-2\pi T_0}<\epsilon/2\). Take every integer \(j\) satisfying
\[
 j\ge 1+\left\lceil\max\left\{
 2,\ T_0^{1/6},\ (2C_B)^{1/6},\
 \sqrt{4+2C_A},\ \sqrt{32(3R+1)},\
 100(4R+2),\ \left(\frac{\sqrt3}{25r}\right)^{1/3}
 \right\}\right\rceil.
 \tag{PK43b}
\]
The constants here are those of the original cutoff and full period matrix.
Since \(j^6-C_B\ge j^6/2\ge j^4\), (PK11) gives
\(\operatorname{sys}\ge j^4\). Its inverse-matrix estimate also gives
\[
 \sigma_{\min}(PS_{M_j})
 \ge\left[j^{-4}+2j^{-6}(2+C_Aj^{-4})\right]^{-1}
 \ge \frac{j^4}{2}.
 \tag{PK43c}
\]
The last inequality follows from \(j^2\ge4+2C_A\) and \(j\ge1\).
All bounds hold uniformly for \(0\le\theta\le2\pi\).

The spatial box has half-width \(a_jL_j=j^3/100\), and
\[
 3Rj^2<a_jK_j<3Rj^2+2a_j.
\]
Consequently it exhausts \(\mathbb R^3\). For the entire physical time
slab \(|s|\le j^2\), its image in \(\mathbb R^4\) is contained in the ball
of radius
\[
 B_j=\frac{\sqrt3j^3}{100}+(3R+1)j^2+\frac1{50j}
 <\frac{j^4}{8}.
 \tag{PK43d}
\]
Indeed each of the three terms is at most \(j^4/32\) under (PK43b):
for the first and third it suffices that \(j\ge1\), while the middle
term uses \(j^2\ge32(3R+1)\). Thus the slightly larger open ball of
radius \(j^4/8\) embeds isometrically in the covered torus by (PK22).
This leaves a collar around the entire slab.

The complete evolved support also lies inside this box on the stated slab.
CE39 gives its radius at most \((R+1)j^2\), whereas
\[
 (R+1)j^2+a_jK_j
 <(4R+1)j^2+\frac1{50j}<\frac{j^3}{100}.
 \tag{PK43e}
\]
The last inequality follows from \(j\ge100(4R+2)\). This verifies the
boundary condition with the actual translated origin, including the
negative \(x^1\) boundary. Moreover \(L_j>K_j+2\), since
\(j>300R+4\), and \(\sqrt2a_j<\lambda_jr\). The reflected face has
first coordinate at least \(2a_jK_j-a_j>6Rj^2+a_j>\lambda_jR\).
Hence the nonzero-vector construction in Section 7 applies at every
integer in (PK43b).

The complete classical energy comparison, with the original coefficients
of CE18–CE22, is
\[
 \begin{aligned}
 \mathscr E_{g_j}^{[\lambda_j]}(v)
 &=\frac{2}{g_j^2\lambda_j}\left[
   \sum_{a,b}\langle c_a,c_b\rangle I_{ab}
   +2\sum_{a,\ b<c}\langle c_a,[c_b,c_c]\rangle J_{a,bc}
   +\sum_{a<b,\ c<d}\langle[c_a,c_b],[c_c,c_d]\rangle K_{ab,cd}
   \right]\\
 &=\frac{400}{\kappa_*j}\left[
   \sum_{a,b}\langle c_a,c_b\rangle I_{ab}
   +2\sum_{a,\ b<c}\langle c_a,[c_b,c_c]\rangle J_{a,bc}
   +\sum_{a<b,\ c<d}\langle[c_a,c_b],[c_c,c_d]\rangle K_{ab,cd}
   \right]\\
 &=\frac{200g_{\rm ref}^2}{\kappa_*j}\mathscr E_{g_{\rm ref}}(v)
 \end{aligned}\tag{PK43f}
\]
for any fixed reference \(g_{\rm ref}>0\). The first equality is CE39
together with the explicit \(g^{-2}\) in CE22. Thus no coupling change
has been hidden in a classical norm. This energy tends to zero for each
fixed original \(v\), and its zero inputs remain exactly the rank-12
zero subbundle. At the equal-colour input, CE23 retains the lower bound
\[
 \mathscr E_{g_j}^{[\lambda_j]}
 \ge\frac{6400\pi r^3}{\kappa_*j}>0.
 \tag{PK43g}
\]
The annulus contribution remains in (PK43f); (PK43g) is only its core
lower bound. The superseded choice \(\lambda_j=\sqrt j\), with the same
\(g_j\), would instead give
\(200g_{\rm ref}^2\sqrt j\,\mathscr E_{g_{\rm ref}}/\kappa_*\).
It increases for every nonzero input. This is the exact defect corrected
by (PK43), before any quantum spectral asymptotics are inferred.

The exact finite raw spectral measure is now a definite object:
\[
 \nu_j(I)=\langle\eta_j,\mathbf1_I(H_j-E_{0,j})\eta_j\rangle,
 \quad \nu_j(\{0\})=0,\quad \nu_j([0,\infty))=\Gamma_j>0.
 \tag{PK44}
\]
The finite-volume heat kernel or spectral resolution of the actual
operator (PK25) computes its Laplace transform. Equivalently expand the
bounded magnetic perturbation around its electric heat semigroup:
\[
 e^{-uH_j}=\sum_{n=0}^{\infty}(-1)^n
 \int_{0<s_1<\cdots<s_n<u}
 e^{-(u-s_n)\kappa_*H_0}V_j e^{-(s_n-s_{n-1})\kappa_*H_0}
 \cdots V_j e^{-s_1\kappa_*H_0}\,d^ns.
 \tag{PK45}
\]
The \(n=0\) term is the electric semigroup. The operator norm of the
\(n\)-th term is at most \((4b_jM_{L_j}u)^n/n!\); hence the series
converges in operator norm for every fixed \(j,u\). Its matrix elements
are computed by the same heat kernels and face insertions in Section 6,
retaining every face word. Multiplication by \(e^{uE_{0,j}}\) gives
\(\int e^{-u\omega}\,d\nu_j(\omega)\). This specifies a convergent
calculation of the full nonlinear dynamics on the constructed vectors.

The next calculation is to estimate these actual raw masses, energy
moments and Laplace transforms uniformly along (PK43), including
\(\Gamma_j\), whose lower bounds in (PK41) and (PK49) decrease. Fixed-scale
scalar low modes (PK18)–(PK20) and decreasing classical energy do not
provide that estimate. In particular the present finite-state construction
does not establish persistence of positive spectral mass near zero,
continuum vacuum uniqueness, reconstruction, or the theory-identification
map. Those remain the active programme calculations on this specified path.

## 9. The complete first electric layer and its interacting return

The original cubic graph supplies a finite subspace on which the following
computations are exact. Write \(M=M_L\) in this section only; the covering
integer remains \(M_{\rm cov}\) when both occur in one formula. Keep
\(\mathcal W=\sum_pW_p\), \(H_0=\sum_eE_e\), and the original identity
\[
 H=\kappa H_0+2bM I-b\mathcal W.
 \tag{PK46}
\]
Here \(\mathcal W\) means multiplication by the complete face sum.

**Theorem 9.1 (first physical electric layer).** On the original physical
Hilbert space, the first positive eigenvalue of \(H_0\) is \(3\). Its
eigenspace is exactly
\(\mathcal F=\operatorname{span}\{W_p:p\text{ an elementary face}\}\).
The displayed \(M\) functions form an orthonormal basis of \(\mathcal F\).
On the orthogonal complement of the constants and \(\mathcal F\), the
electric operator has lowest eigenvalue exactly \(9/2\).

**Proof.** The integral of a matrix entry of \(U\) or \(U^{-1}\) against
Haar measure is zero: replacing \(U\) by \(-U\) reverses its sign. Hence
\(\int W_p=0\). Integrating any one link in a face reduces its squared
trace to \(\int_{SU(2)}(\operatorname{tr}U)^2dU=1\). One can see this last
constant without a character convention: \(SU(2)\) is the unit quaternion
three-sphere, \(\operatorname{tr}\Psi(a)=2a_0\), its Haar probability is
the rotation-invariant sphere probability, and each of the four squared
coordinates has mean \(1/4\). If \(p\ne q\), there is an edge of \(p\)
absent from \(q\); integration in that edge gives
\(\langle W_p,W_q\rangle=0\). There are exactly \(M\) original faces.
For every edge of \(p\),
\(E_eW_p=(3/4)W_p\), because \(-\sum_aT_a^2=3I/4\).
The same calculation holds for an inverse link. Thus \(H_0W_p=3W_p\).

For the completeness and lower spectral bounds, decompose the product
matrix coefficients into edge spins \(j_e\). On this finite spin block,
\(H_0\) is the scalar \(\sum_ej_e(j_e+1)\). These blocks span a dense
subspace: polynomials in fundamental matrix entries and their conjugates
separate points on the compact product group, their algebra contains the
constants, and uniform density followed by the finite-dimensional
highest-weight decomposition used in (PK35) gives the claimed matrix
coefficient density. Averaging at a vertex acts only on its incident
representation slots. A vertex incident to exactly one nonzero spin has
zero invariant part, because a nontrivial irreducible representation has
no fixed vector. Therefore the support graph of any nonconstant physical
spin block has minimum degree at least two.

A nonempty finite graph of minimum degree at least two contains a cycle:
extend a nonbacktracking path until a vertex repeats. The cubic graph is
simple and bipartite, so this cycle has at least four edges. Each nonzero
spin contributes at least \(3/4\), giving the lower bound \(3\). Equality
requires exactly four spin-\(1/2\) edges. Four such edges form a unit
coordinate square; at its degree-two vertices, the invariant pairing is
one-dimensional. Contracting those pairings is precisely its Wilson trace.
The dimension statement also follows directly from Schur's lemma: an
intertwiner between the two irreducible incident slots is scalar when their
spins agree and zero otherwise. This proves that no other vector occurs
at eigenvalue \(3\).

There is no five-edge nonempty support graph of minimum degree at least
two in the cubic graph. It would be connected, since two components would
require at least eight edges. With at most four vertices a simple bipartite
graph has at most four edges; with five vertices and five edges, minimum
degree two forces every degree to be two, giving an odd cycle. A four-edge
support is a square, whose successive degree-two invariant pairings force
one common spin \(j\); after \(j=1/2\), its energy is at least
\(4\cdot1(1+1)=8\). Every support with at least six edges has energy at
least \(6\cdot3/4=9/2\). This proves the complementary bound. It is
attained: the rectangle with corners
\((-1,-1,0),(1,-1,0),(1,0,0),(-1,0,0)\) lies in every box \(L\ge1\).
Its ordered boundary uses six distinct links. The fundamental trace of
that holonomy has Haar squared norm one by integrating one boundary link,
and each of its six link Casimirs contributes \(3/4\). It is therefore a
nonzero eigenvector at \(9/2\), orthogonal to the constants and the
eigenvalue-\(3\) face space by self-adjointness. The arguments
extend from the dense finite spin sums to the form domain by their
orthogonal spectral expansion. \(\square\)

Let \(P_{\mathcal F}\) be this electric spectral projection. Applying
(PK28) to each gauge-invariant electric eigenfunction gives the full
projection, with every original face retained:
\[
 \begin{aligned}
 P_{\mathcal F}\eta_{h,t}
 &=e^{-3t}\sum_p\bigl(W_p(h)-W_p(\mathcal Rh)\bigr)W_p,\\
 S(h,t)&=e^{-6t}\sum_p\bigl|W_p(h)-W_p(\mathcal Rh)\bigr|^2,\\
 \Gamma(h)&=S(h,t)+\|\eta_{h,t}-P_{\mathcal F}\eta_{h,t}\|_2^2,\\
 \langle\eta_{h,t},H_0\eta_{h,t}\rangle
 &\ge3S(h,t)+\frac92\bigl(\Gamma(h)-S(h,t)\bigr).
 \end{aligned}\tag{PK47}
\]
The constant coefficient of \(\eta\) is zero since its two integrals equal
one. This is why Theorem 9.1 applies to the remainder. These are electric
spectral statements; the magnetic terms in (PK46) are still present.

Here is the resulting strengthened lower bound for the actual field.
Set
\[
 m=\left\lfloor\frac{\lambda r}{2\sqrt3\,a}\right\rfloor,\qquad
 M_m=3(2m)^2(2m+1).
\]
Use all faces of the coordinate cube
\((-K,0,0)+\{-m,\ldots,m\}^3\), assuming \(m\ge1\) and
\(L>K+m\). Every point of this cube has physical norm at most
\(\sqrt3am\le\lambda r/2\), so every one of its \(M_m\) face traces is
the value (PK40). Their reflected cube lies outside the original support:
its first physical coordinate is at least \(2aK-am>\lambda R\).
The two face sets are disjoint. Their coefficients in (PK47) have equal
magnitudes and opposite signs, which proves
\[
 \Gamma(h)\ge32M_m e^{-6t}\sin^8(a/\lambda).
 \tag{PK48}
\]
The single-face-plus-reflection case already improves (PK41)'s constant
from \(16\) to \(32\). Equation (PK48) retains every face of the selected
core cube; all remaining face coefficients and the orthogonal remainder
remain in the exact identity (PK47).

On (PK43), \(m_j=\lfloor50rj^3/\sqrt3\rfloor\), and (PK43b) gives
\(m_j\ge25rj^3/\sqrt3\ge1\) and \(L_j>K_j+m_j\).
For the second assertion, \(m_j\le50rj^3/\sqrt3<30Rj^3\), whereas
\(K_j<300Rj^3+2\) and \(j\ge100(4R+2)>330R+2\).
Concavity of sine on \([0,\pi/2]\), or its second derivative, gives
\(\sin x\ge2x/\pi\) on that interval. Consequently the completely
specified lower bound along the corrected path is
\[
 \begin{aligned}
 \Gamma_j
 &\ge32\,[3(2m_j)^2(2m_j+1)]e^{-6t_*}
                  \sin^8\!\left(\frac1{100j^3}\right)\\
 &\ge32\cdot24
    \left(\frac{25r}{\sqrt3}\right)^3
    \left(\frac2{100\pi}\right)^8e^{-6t_*}\,j^{-15}>0.
 \end{aligned}\tag{PK49}
\]
This is a lower bound for the raw norm, not an assertion that its actual
asymptotic size is \(j^{-15}\), and not a limiting quantum spectral mass.

To calculate the interaction with this electric layer, we need a small
geometric fact. A nonempty collection of at most five distinct elementary
faces in the cubic lattice has an edge incident to an odd number of the
selected faces. Here is a proof retaining the ambient graph. For a finite
collection with every edge even, define the occupation of a unit cube,
modulo two, by the number of selected horizontal faces crossed by the
vertical ray from its centre to positive infinity. Across a horizontal
face the occupation changes exactly when that face is selected. Across
a vertical face, sum the edge-even equations in the finite vertical strip
between the two rays; internal terms cancel in pairs and give that same
change law. Above all selected faces every occupation is zero. Below
all selected faces, the vertical-face change law makes the occupations
equal in every horizontal column; a column outside the finite horizontal
support has occupation zero. Thus the occupations also vanish below all
selected faces. Only finitely many columns can meet the selected horizontal
faces, so the occupied cube set is finite. Its boundary is exactly the
selected face collection. If it is nonempty,
choose a cube at the maximum and minimum in each of the three coordinate
directions. Its outward face is a boundary face. These six faces are
distinct by their directions and supporting coordinate planes. Thus the
boundary contains at least six faces, proving the assertion. The open
finite box embeds in this infinite lattice, so the fact applies to its
face subsets without a periodic-boundary assumption.

Replacing one link \(U_e\) by \(-U_e\) changes the sign of each trace using
that edge and preserves Haar measure. It follows that a product of at most
five Wilson traces has zero integral whenever the collection of faces with
odd multiplicity is nonempty. Thus
\(\int W_pW_rW_q=0\) and every product of five traces has zero integral.
For fourth moments, the only nonzero cases are pairs of equal faces or four
copies of one face. Distinct squared traces have integral one: first
integrate an edge unique to one of the two faces, making its squared trace
equal to one, then integrate the other. A single fourth power has integral
two. For this last constant, the spin decomposition
\(\chi_{1/2}^2=1+\chi_1\) follows by separating symmetric and antisymmetric
tensors of two fundamental vectors, and character orthogonality gives
\(\int(1+\chi_1)^2=2\).

These identities determine three complete finite matrices in the original
orthonormal face basis. Let \({\bf 1}\) be the \(M\)-component column of ones.
Then
\[
 \begin{aligned}
 P_{\mathcal F}\mathcal W P_{\mathcal F}&=0,\\
 P_{\mathcal F}\mathcal W^2 P_{\mathcal F}
   &=(M-1)I_M+2{\bf1}{\bf1}^{\mathsf T},\\
 P_{\mathcal F}\mathcal W H_0\mathcal W P_{\mathcal F}
   &=(6M-4)I_M+6{\bf1}{\bf1}^{\mathsf T},\\
 P_{\mathcal F}\mathcal W^3 P_{\mathcal F}&=0.
 \end{aligned}\tag{PK50}
\]
For the second matrix its diagonal is \(2+(M-1)=M+1\) and its off-diagonal
entries are \(2\), from the two pairings of two different faces. For the
third, first observe
\[
 \langle W_p^2,H_0W_p^2\rangle=8,\quad
 \langle W_p^2,H_0W_q^2\rangle=0\ (p\ne q),\quad
 \langle W_pW_q,H_0W_pW_q\rangle=6\ (p\ne q).
\]
The first two follow from \(W_p^2=1+\chi_1(U_p)\), whose nonconstant
part has electric energy \(4\cdot2=8\); distinct such face characters
are orthogonal by their unique edges. For the third, expand the gradient
of the product. Each individual face has Dirichlet energy \(3\);
integrating an edge unique to the other face removes its squared trace
with factor one. Every cross term vanishes: integrate an edge unique to
one face to obtain
\(\int W_p X_{e,a}W_p= \tfrac12X_{e,a}\int W_p^2=0\).
This proves the total \(3+3=6\), including adjacent faces sharing an edge.
Consequently the third matrix has diagonal \(8+6(M-1)=6M+2\) and
off-diagonal \(6\). Haar link sign changes commute with \(H_0\), so the
same parity argument eliminates all other terms. The first and fourth
matrices are respectively the triple and quintuple moments proved above.

Compression of the *full* Hamiltonian to constants plus faces is therefore
\[
 \begin{pmatrix}
 2bM&-b{\bf1}^{\mathsf T}\\
 -b{\bf1}&(2bM+3\kappa)I_M
 \end{pmatrix}.
 \tag{PK51}
\]
Restricting this matrix to the constant vector and the direction
\(\sum_pW_p\), with its squared norm \(M\) retained, gives the ground
variational upper bound
\[
 E_0\le2bM+\frac{3\kappa-\sqrt{9\kappa^2+4b^2M}}2.
 \tag{PK52}
\]
This is an upper bound for the actual interacting ground energy; it is
not an identification of the compressed eigenvalue with \(E_0\).

Now use the reflection-odd subspace \(\mathcal H_-\). Put
\(P_-=P_{\mathcal F}|_{\mathcal H_-}\) and
\(Q_-=I_{\mathcal H_-}-P_-\). Every face coefficient vector in this
subspace has sum zero. Equations (PK50)–(PK52) give
\[
 \begin{gathered}
 P_-HP_-=(2bM+3\kappa)P_-,\qquad
 d:=2bM+3\kappa-E_0
 \ge\frac{3\kappa+\sqrt{9\kappa^2+4b^2M}}2,\\
 C:=Q_-\mathcal WP_-=\mathcal WP_-,\qquad
 C^*C=(M-1)P_-,\\
 C^*H_0C=(6M-4)P_-,\qquad C^*\mathcal WC=0.
 \end{gathered}\tag{PK53}
\]
The equality for \(C\) uses both reflection invariance and
\(P_-\mathcal WP_-=0\). Every nonzero vector confined to this first
odd electric layer has excitation-energy mean exactly \(d\). On
(PK43) its proved lower bound in (PK53) grows at least as
\(b_j\sqrt{M_{L_j}}\), rather than tending to zero.

This calculation identifies and evaluates the next return through the
complement instead of stopping at that limitation. Let \(s>0\), and define
the self-adjoint operator
\[
 B_-=Q_-(H-E_0)Q_-
\]
on \(Q_-\mathcal H_-\) by its closed quadratic form. Since \(H-E_0\ge0\),
\(B_-\ge0\), and \(B_-+s\) is invertible without a gap assumption. All
vectors in the range of \(C\) are smooth finite polynomials. The exact
block resolvent and its first-return bounds are
\[
 \begin{aligned}
 P_-(H-E_0+s)^{-1}P_-
 &=\left[(d+s)P_--b^2 C^*(B_-+s)^{-1}C\right]^{-1}_{P_-\mathcal H_-},\\
 \frac{(M-1)^2}
 {\kappa(6M-4)+(2bM-E_0+s)(M-1)}P_-
 &\le C^*(B_-+s)^{-1}C\le\frac{M-1}{s}P_-.
 \end{aligned}\tag{PK54}
\]
To prove the first identity, solve the \(Q_-\) component of the block
equation for \(H-E_0+s\); its off-diagonal block is \(-bC\).
Substitution into the \(P_-\) equation gives the displayed Schur
complement. It is strictly positive: minimizing the full positive form
over the \(Q_-\) variable gives a value at least \(s\|f\|^2\) for
each \(f\in P_-\mathcal H_-\). The finite inverse therefore exists.
The upper bound follows from \(B_-\ge0\) and \(C^*C=(M-1)P_-\).
For the lower bound, Cauchy–Schwarz applied to
\((B_-+s)^{1/2}Cf\) and \((B_-+s)^{-1/2}Cf\), together with (PK53), gives
\[
 (M-1)^2\|f\|^4\le
 \left[\kappa(6M-4)+(2bM-E_0+s)(M-1)\right]\|f\|^2
 \langle Cf,(B_-+s)^{-1}Cf\rangle.
\]
This proves (PK54), retaining the actual vacuum shift and both couplings.
No artificial orthogonality between geometric parameters or omitted
magnetic interaction enters the calculation.

The full packet \(\eta_{h,t}\) also has its complementary part in
(PK47). Its actual spectral measure remains (PK44), evaluated by (PK33),
(PK45) and the full complementary operator in (PK54). The first electric
projection alone cannot supply a decreasing excitation-energy mean on the
chosen path. The exact complementary return above is the next receiving
operator; further uniform estimates of that operator and of the packet's
complementary coefficients remain active calculations.

## 9.2. The complete second complementary moment

Continue with the original open box and every face in (PK24). In this
subsection write \(P=P_-\), \(Q=Q_-\), \(B=B_-\), and
\(\mathcal W=\sum_pW_p\), with exactly the definitions of (PK53)–(PK54).
No change of spatial scale, coupling, inner product or Hamiltonian is made.
Put
\[
 m=M-1,\qquad \alpha=2bM-E_0,\qquad
 \mu=\kappa(6M-4)+\alpha(M-1).
 \tag{PK55}
\]
Thus \(C^*C=mP\) and \(C^*BC=\mu P\). The latter identity follows
from (PK53), since \(C\) has range in \(Q\mathcal H_-\).
The ground-energy bound (PK52) gives
\(\alpha\ge(\sqrt{9\kappa^2+4b^2M}-3\kappa)/2>0\).
Consequently \(m>0\) and \(\mu>0\).

For two distinct original faces, define \(A_{pq}=1\) when they share a
link and \(A_{pq}=0\) otherwise; set \(A_{pp}=0\).
Let \(D_{pp}=\sum_qA_{pq}\), \(D_{pq}=0\) for \(p\ne q\).
Let \(N_{pq}\), for \(p\ne q\), count elementary cubes in the original box
whose boundaries contain both \(p\) and \(q\), and set \(N_{pp}=0\).
All three matrices act on the full original face coefficient space
\(\mathbb C^M\), identified isometrically with \(\mathcal F\) by
\((z_p)\mapsto\sum_pz_pW_p\). Their definitions include faces on the box
boundary. Reflection permutes faces, links and cubes, so these matrices
commute with the reflection and preserve \(P\mathcal H_-\).

**Theorem 9.2.** In the original orthonormal face basis,
\[
\begin{aligned}
 P_{\mathcal F}\mathcal W H_0^2\mathcal WP_{\mathcal F}
   &=(36M-8)I_M+36{\bf1}{\bf1}^{\mathsf T}
                       +\frac34(D+A),\\
 P_{\mathcal F}\mathcal W^4P_{\mathcal F}
   &=(3M^2-7M+5)I_M+(12M-8){\bf1}{\bf1}^{\mathsf T}
                       +\frac32N.
\end{aligned}\tag{PK56}
\]
The full complementary second moment is
\[
\begin{aligned}
 K_2:=C^*B^2C={}&
 \kappa^2P\left[(36M-8)I_M+\frac34(D+A)\right]P\\
 &+\left[2\kappa\alpha(6M-4)+\alpha^2(M-1)
                        +b^2(2M^2-5M+4)\right]P
 +\frac32b^2PNP.
\end{aligned}\tag{PK57}
\]
Here \(B\) is the entire complementary operator, with the actual vacuum
energy \(E_0\), not a finite compression substituted for that energy.

**Proof of the geometry needed for (PK56).**
The vertical-ray occupation construction before (PK50) maps every finite
edge-even face set \(S\) to a finite cube set \(K\) with boundary \(S\),
over \(\mathbb Z/2\mathbb Z\). To make the change law explicit, for a cube
with lower corner \(n=(n_1,n_2,n_3)\) let its occupation be the parity of
selected horizontal faces above its centre. The difference of occupations
above and below a horizontal face is that face's indicator. For a vertical
face between two horizontally adjacent columns, sum the edge-even equations
on the common vertical strip from its lower edge to a height beyond \(S\).
Each internal vertical-face indicator occurs twice. The surviving terms
are the two horizontal-ray counts and the indicator of that vertical face.
Thus the occupation difference across it is again precisely its indicator.
At sufficiently high height all occupations are zero. At sufficiently low
height these change laws make occupations equal across all horizontal
columns, and an exterior column has value zero. Occupied cubes are therefore
finite in both height and horizontal extent, and their boundary is exactly
\(S\). A cube outside the open box has occupation zero: its column is exterior,
or it is above or below all box faces. Thus the filling respects the original
box when \(S\) lies there.

In integer coordinates, write \(s_{ij}(n)\in\{0,1\}\) for the indicator of
the face with lower corner \(n\) in coordinate directions \(i,j\), and let
\(e_1,e_2,e_3\) be the integer coordinate vectors. The construction and all
three boundary components are exactly
\[
\begin{aligned}
 k(n)&=\sum_{t=n_3+1}^{\infty}s_{12}(n_1,n_2,t)\pmod2,\\
 s_{12}(n)&=k(n-e_3)+k(n),\\
 s_{23}(n)&=k(n-e_1)+k(n),\\
 s_{13}(n)&=k(n-e_2)+k(n).
\end{aligned}
\]
The last two equations follow by summing, respectively, the edge equations
\[
\begin{aligned}
 s_{12}(n)+s_{12}(n-e_1)+s_{23}(n)+s_{23}(n-e_3)&=0,\\
 s_{12}(n)+s_{12}(n-e_2)+s_{13}(n)+s_{13}(n-e_3)&=0
\end{aligned}
\]
over heights \(t\ge n_3+1\). The vertical-face terms telescope to the
face at height \(n_3\); the face at infinity is zero by finite support.
All additions in these five boundary equations are modulo two.

Let \(\pi_{23}K,\pi_{13}K,\pi_{12}K\) be the sets of unit cells obtained by
projecting the occupied cubes in the three coordinate directions. Every
nonempty line of cubes parallel to the first axis has two end faces
normal to that axis; these end faces are distinct for different projected
cells. The same statement holds for the second and third axes. Hence
\[
 |\partial K|\ge
 2\bigl(|\pi_{23}K|+|\pi_{13}K|+|\pi_{12}K|\bigr)\ge6.
\]
If \(|\partial K|=6\), each of these three projections consists of one cell.
Any two cubes of \(K\) then have the same pair of second/third coordinates,
the same first/third coordinates and the same first/second coordinates.
They coincide. Conversely one cube has six boundary faces. We have proved
that every six-face nonempty edge-even set is exactly one cube boundary,
including at the box boundary.

There are two further elementary geometric facts used below. Distinct unit
squares of the cubic lattice share at most one edge. Therefore in a set
of at most three distinct faces, each face has an edge unused by the other
faces. Integrating such an edge makes any power of its trace equal to the
corresponding single-group Haar moment, independently of all remaining
link variables. Repeating proves factorization of trace powers for these
sets; no independence of larger face collections is assumed.

**Haar coefficients.**
For \(U=q_0I-i_{\mathbb C}\sum_{a=1}^3q_a\sigma_a\), with
\(\sum_{a=0}^3q_a^2=1\), Haar probability is uniform measure on \(S^3\) and
\(\operatorname{tr}U=2q_0\). Its even coordinate moment is
\[
 \int q_0^{2r}\,dU
 =\frac{1\cdot3\cdots(2r-1)}{4\cdot6\cdots(2r+2)}.
\]
For completeness, integrate a rotationally invariant Gaussian in
\(\mathbb R^4\) in Cartesian and polar coordinates. Integration by parts
gives the one-coordinate Gaussian recursion
\(\int_{\mathbb R}t^{2r}e^{-t^2/2}dt
=(2r-1)\int_{\mathbb R}t^{2r-2}e^{-t^2/2}dt\).
Radial integration gives the recursion by \(2r+2\) for the corresponding
four-dimensional radial moment. Dividing the Cartesian moment by that radial
moment yields the displayed ratio, including the initial moment one.
Thus the trace moments at powers \(2,4,6\) are respectively \(1,2,5\).

The integral of one trace on each of the six cube faces is exactly \(1/16\).
Orient the six faces outward. The two traversals of each of the twelve
edges then have opposite orientations. Reversing any original face
orientation does not change its trace, since for \(SU(2)\) the trace of
the inverse equals the trace. The entry identity is
\[
 \int U_{ij}(U^{-1})_{kl}\,dU
       =\frac12\delta_{il}\delta_{jk}.
\]
One can prove it directly from the displayed quaternion matrix and the
second coordinate moments \(\int q_aq_b=\delta_{ab}/4\).
Expand all six traces into matrix entries and integrate every edge.
Each contributes \(1/2\) and identifies the corner indices at its two
ends. At each cube vertex its three incident face-corner indices are
identified cyclically; no equality joins distinct vertices. There remain
eight free indices, each taking two values. The integral is therefore
\(2^8/2^{12}=1/16\). This also proves positivity and the orientation sign
without a surface approximation.

For a diagonal entry of the second matrix in (PK56), the two external
traces are both \(W_p\). The four internal choices have nonzero integrals
only when every face has even multiplicity. A nonempty odd-multiplicity
set would have at most four faces and is excluded by the proved geometry.
The four possibilities, with their multiplicities retained, give
\[
 5+2(M-1)+6\cdot2(M-1)+6\binom{M-1}{2}
       =3M^2+5M-3.
\]
They are respectively four further copies of \(p\); four copies of another
face; two further copies of \(p\) and two of another face; and two each
of two other faces. Each integral uses at most three distinct faces, so
the factorization proved above applies.

For distinct external faces \(p,q\), the even-multiplicity cases have
internal multiplicities \((3p,1q)\), \((1p,3q)\), or
\((1p,1q,2r)\) with \(r\ne p,q\). Their sum is
\[
 4\cdot2+4\cdot2+12(M-2)=12M-8.
\]
If the odd-multiplicity set is nonempty, it must contain six distinct faces,
each appearing once in the full product, and must be a cube boundary.
For each cube containing \(p,q\), the remaining four faces have \(4!=24\)
orders. The additional contribution is \(24/16=3/2\) per such cube.
This proves the magnetic matrix in (PK56), including every entry of \(N\).

**Electric coefficients.**
The single-face identity \(W_p^2=1+\chi_1(U_p)\) gives
\[
 H_0W_p^2=8\chi_1(U_p),\qquad
 \|H_0W_p^2\|_2^2=64,\qquad
 \langle H_0W_p^2,H_0W_q^2\rangle=0\quad(p\ne q).
\]
The last assertion follows by integrating an edge unique to one of the
two faces: a spin-one character has zero average. The eigenvalue eight
retains all four link Casimirs \(1(1+1)=2\).

For faces \(p\ne q\) with no common link, \(W_pW_q\) is an electric
eigenfunction with eigenvalue \(8\cdot3/4=6\), and its squared norm is one.
Its second moment is therefore \(36\).
For adjacent faces let \(U\) be the shared link, and write the two traces,
after cyclic permutation and permitted inversion, as
\(\operatorname{tr}(AU)\) and \(\operatorname{tr}(U^{-1}B)\).
The other six links are distinct. Haar projection onto constants in the
shared link is
\[
 F_0(A,B)=\int\operatorname{tr}(AU)\operatorname{tr}(U^{-1}B)\,dU
                  =\frac12\operatorname{tr}(AB).
\]
Its squared norm over the other six links is \(1/4\).
The full product has squared norm one by the two-face integration argument.
The complementary part \(F_1\) consequently has squared norm \(3/4\).
Its shared-link representation is spin one: the tensor product of the
fundamental representation and its dual splits into the scalar identity
matrix and the three traceless matrices. Conjugation on the traceless
matrices is the spin-one representation. Its Casimir for the original
\(T_a=-i_{\mathbb C}\sigma_a/2\) is two, as follows by applying
\(-\sum_a[T_a,[T_a,V]]\) to each \(V=T_b\).
On the scalar part the shared-link Casimir is zero. Each of the other
six links contributes \(3/4\) to both parts. Hence
\[
 H_0F_0=\frac92F_0,\qquad H_0F_1=\frac{13}2F_1,\qquad
 \|H_0(W_pW_q)\|_2^2
  =\frac14\left(\frac92\right)^2
       +\frac34\left(\frac{13}2\right)^2=\frac{147}4.
\]
This is \(36+3/4\), not \(36\). Keeping the shared-link tensor sector is
essential for the second moment even though its first moment is six.

For an arbitrary matrix entry, expand
\(\langle H_0(\mathcal WW_p),H_0(\mathcal WW_q)\rangle\).
Changing one link to its negative commutes with \(H_0\); therefore a term
vanishes if its four face factors have a nonempty odd-multiplicity set.
The diagonal terms are \(64\) for the repeated face, \(147/4\) for every
adjacent face and \(36\) for every other face. Their sum is
\(36M+28+(3/4)D_{pp}\).
For \(p\ne q\), one remaining pairing gives the squared moment of
\(W_pW_q\); the other gives
\(\langle H_0W_p^2,H_0W_q^2\rangle=0\).
Thus the off-diagonal entry is \(36+(3/4)A_{pq}\).
This proves the first matrix in (PK56).

**Passage to the entire complement.**
All face polynomials, and their images under any finite word in \(H_0\)
and \(\mathcal W\), are smooth on the compact product of link groups.
They lie in the domain of every required power of the elliptic operator.
The projections \(P\) and \(Q\) preserve this domain, since \(P\) has smooth
finite-dimensional range. Thus the following expressions are operator
identities between finite-dimensional maps, with no form-domain
substitution:
\[
\begin{aligned}
 C^*B^2C
 &=C^*(H-E_0)Q(H-E_0)C\\
 &=C^*(H-E_0)^2C-C^*(H-E_0)P(H-E_0)C.
\end{aligned}
\]
Since \(PH_0=3P\), \(PC=0\), and \(P\mathcal WC=mP\),
\(P(H-E_0)C=-bmP\). The second term is exactly \(b^2m^2P\).
Expand the first term using \(H-E_0=\kappa H_0+\alpha-b\mathcal W\):
\[
\begin{aligned}
 C^*(H-E_0)^2C={}&
 \kappa^2C^*H_0^2C+2\kappa\alpha C^*H_0C+\alpha^2 C^*C
 +b^2C^*\mathcal W^2C\\
 &-\kappa b C^*(H_0\mathcal W+\mathcal WH_0)C
 -2\alpha b C^*\mathcal WC.
\end{aligned}
\]
The last term vanishes by (PK53). Each mixed electric/magnetic term on
the preceding line has five total face factors, and \(H_0\) preserves
each edge parity. Five factors cannot have all face multiplicities even;
the nonempty odd set has at most five faces and is excluded. Hence both
mixed terms vanish. Insert (PK56), (PK53), and the exact \(b^2m^2P\)
subtraction. The all-ones matrix annihilates the odd subspace. The remaining
magnetic scalar is
\(b^2[(3M^2-7M+5)-(M-1)^2]=b^2(2M^2-5M+4)\).
This proves (PK57). \(\square\)

## 9.3. A second exact return and a stronger resolvent bound

The calculated moment supplies the next connecting map, not only a finite
matrix comparison. Define projections and operators on the original
complementary Hilbert space by
\[
\begin{gathered}
 \Pi=\frac1mCC^*,\qquad Q_2=Q-\Pi,\qquad
 T=Q_2BC,\qquad B_2=Q_2BQ_2,\\
 V:=T^*T=K_2-\frac{\mu^2}{m}P .
\end{gathered}\tag{PK58}
\]
The operator \(B_2\) is defined by restriction of the closed nonnegative
form to \(Q_2\mathcal H_-\); it is self-adjoint and nonnegative.
Indeed \(C^*C=mP\) proves \(\Pi^*=\Pi\), \(\Pi^2=\Pi\) and that its
range is exactly \(\operatorname{ran}C\). This finite-dimensional range
consists of smooth vectors. Its orthogonal complement preserves the form
domain; restriction is therefore dense and closed.
In the last identity of (PK58), subtract
\(C^*B\Pi BC=(C^*BC)^2/m=(\mu^2/m)P\).

The full expression, retaining both its previous form and its exact
evaluated comparison, is
\[
\begin{aligned}
 V={}&K_2-\frac{[\kappa(6M-4)+\alpha(M-1)]^2}{M-1}P\\
 ={}&\kappa^2P\left[
     \left(4-\frac4{M-1}\right)I_M+\frac34(D+A)\right]P\\
 &+b^2P\left[(2M^2-5M+4)I_M+\frac32N\right]P .
\end{aligned}\tag{PK59}
\]
The cancellation of \(\alpha\) follows by expanding its entire square:
the \(\alpha^2(M-1)\) and \(2\kappa\alpha(6M-4)\) terms cancel exactly.
Also
\((6M-4)^2/(M-1)=36M-12+4/(M-1)\), giving the displayed electric scalar.
No vacuum energy has been removed from \(B\), \(B_2\), or \(\mu\).

These matrices give explicit nonzero bounds for the next map. For any face
vector \(z\),
\[
 z^*(D+A)z=\sum_{\{p,q\}:A_{pq}=1}|z_p+z_q|^2.
\]
Every face has four edges, and each edge belongs to at most four faces.
Different faces share at most one edge, so \(D_{pp}\le12\). Thus
\(0\le D+A\le24I_M\).
Let \(J_{pc}=1\) if face \(p\) belongs to cube \(c\), and zero otherwise.
With \(k_p=\sum_cJ_{pc}\in\{1,2\}\), the exact identity is
\(N=JJ^{\mathsf T}-\operatorname{diag}(k_p)\). Therefore \(N\ge-2I_M\).
Its row sum is \(5k_p\le10\), and
\(\left|z^*Nz\right|\le\sum_{p<q}N_{pq}(|z_p|^2+|z_q|^2)
\le10\|z\|^2\), so \(N\le10I_M\).
Consequently
\[
\begin{aligned}
 \left[\kappa^2\left(4-\frac4m\right)
                  +b^2(2M^2-5M+1)\right]P
 &\le V\\
 &\le
 \left[\kappa^2\left(22-\frac4m\right)
                  +b^2(2M^2-5M+19)\right]P.
\end{aligned}\tag{PK60}
\]
Here \(L\ge1\) gives \(M=3(2L)^2(2L+1)\ge36\), so the lower bound is
strictly positive. In particular \(T\) is injective on the actual odd face
space: the next return is not zero.

For every \(s>0\), the exact second return is
\[
 C^*(B+s)^{-1}C
 =m^2\left[(\mu+sm)P-T^*(B_2+s)^{-1}T\right]^{-1}_{P\mathcal H_-}.
 \tag{PK61}
\]
To prove it without changing the metric, solve
\((B+s)(Cf+y)=Cu\), where \(y\in Q_2\mathcal H_-\).
The \(Q_2\) equation gives \(y=-(B_2+s)^{-1}Tf\).
Applying \(C^*\) to the other equation gives
\([(\mu+sm)P-T^*(B_2+s)^{-1}T]f=mu\).
Finally \(C^*(Cf+y)=mf\), producing both factors \(m\) in (PK61).
Its denominator is strictly positive: minimizing the quadratic form of
\(B+s\) over \(y\) leaves at least \(sm\|f\|^2\). These arguments extend
from smooth vectors by the closed form and resolvent; the finite off-diagonal
map \(T\) is bounded.

There is also an upper bound using the complete second moment:
\[
 \frac{m^2}{\mu+sm}P
 \ \le\ C^*(B+s)^{-1}C
 \ \le\ \frac m sP-\frac{\mu^2}{s}(K_2+s\mu P)^{-1}.
 \tag{PK62}
\]
The first inequality is (PK54). For the second put
\[
 X=[B(B+s)]^{1/2}C,\qquad
 Y=[B(B+s)^{-1}]^{1/2}C .
 \]
These maps are defined since \(C\) has range in the domain of \(B\).
The spectral functional calculus gives
\[
 X^*X=K_2+s\mu P,\quad
 X^*Y=\mu P,\quad
 Y^*Y=mP-sC^*(B+s)^{-1}C.
\]
The first matrix is positive definite because \(s\mu>0\).
Expanding
\([Y-X(X^*X)^{-1}X^*Y]^*[Y-X(X^*X)^{-1}X^*Y]\ge0\)
gives \(Y^*Y\ge\mu^2(K_2+s\mu P)^{-1}\). Rearrangement proves
(PK62). Its positive subtracted matrix makes the upper bound strictly
stronger than \(mP/s\) for every finite box and every \(s>0\).

Equations (PK57)–(PK62) retain the exact relation of the full complementary
operator to the original first electric layer. They do not substitute a
finite-level spectrum for the spectrum of \(H\).
For the actual corrected path (PK43), \(M=3(2j^4)^2(2j^4+1)\) and
\(b=10000j^2/\kappa_*\); the nonzero term
\(b^2(2M^2-5M+1)\) in (PK60) explicitly prevents treating the next map
as a uniformly small perturbation. The next calculation is the entire
\(T^*(B_2+s)^{-1}T\), together with the complementary coefficients of
the actual heat packet in (PK47). Its small-energy measure remains the
quantity (PK44); neither a shrinking classical energy nor these finite
moments replace that calculation.


![Original cube integration and the complete next return](figures/COMPLEMENTARY_SECOND_MOMENT.png)

The figure shows the coordinate projection of an actual side-a lattice cube, the two shared-link electric sectors, and the exact composition T=Q2 B C. Complete proofs and all factors are PK55–PK62. Its [reproducible source](figures/complementary_moment_figure.py) retains the original operators. The finite Haar calculation is derived here; no novelty claim is made for character integration or Schur inversion.

## 10. Reproducibility and scope

The original symbolic checker verifies the full angular period law, both matrix
inverses, every inverse-metric block, cover conjugacy, the complete dual
quadratic form, representation matrices and Haar projectors in the
smallest relevant tensor sectors, the original plaquette trace and all
path factors. Finite checks support these algebraic identities. The
bundle, analytical convergence, injectivity, positivity, vacuum and
nonzero-vector arguments are the written proofs above.

The heat-packet source conventions were read in the original author TeX;
no PDF reading or whole-paper recertification is asserted. No novelty
claim is made for heat-kernel coherent states, group averaging, or the
finite-lattice ground-state facts. Their application here receives the
actual corrected moment-map field, full cusp covering, and original
interacting lattice Hamiltonian with the indicated exact factors.

The complementary-moment checker adds 43 exact checks for PK55–PK62: direct Haar polynomial integration, oriented cube matrix-entry contraction, exhaustive six-face cycles in the smallest original box, every sixth-moment entry on a cube plus another face, boundary incidence and reflection in three boxes, and the full projection and resolvent identities. General proofs, including the exact cubical filling map, are given in Sections 9.2–9.3. A finite check is not a continuum estimate.
