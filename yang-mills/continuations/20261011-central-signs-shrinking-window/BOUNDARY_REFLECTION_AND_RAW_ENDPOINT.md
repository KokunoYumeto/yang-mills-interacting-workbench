# Exact boundary reflection and the original raw endpoint

This continues IP1–IP22 while retaining the actual vacuum, original
polynomial \(F=p-r\), and prescribed simultaneous path. The calculation
locates the full nonlinear reflection correction, computes its entire
normal kinetic form at identity boundary holonomies, and obtains an
actual-vacuum lower bound for the energy of that correction. It does not
settle the sign of the original shrinking-window endpoint.
The strongest evaluated bounds are (JP43) for the even correction
energy and (JP47) for the original odd raw mass and energy. Their
original-path exponential loss is proportional to \(j^2\).

## 1. Original links and the two tree presentations

Retain the original box, root, tree, coefficients and coordinates of
[PK103–PK108](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md#L2440)
and [PK158–PK160](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md#L3500).
Thus \(m=2L\), \(n=m+1\), \(L\ge2\); a vertex `(i,k,l)` represents
the physical point \(o+a(i-L,k-L,l-L)\). The tree contains every
direction-one edge, direction-two edges with \(i=0\), and direction-three
edges with \(i=k=0\). Its root path goes first in direction three, then
two, then one. Every original rooted word is still
\(Z_c=t_sU_ct_t^{-1}\).

Use the exact tree-gauge coordinate map: original tree links equal
identity and chord links equal their original based words \(Z_c\).
This is a coordinate presentation of the gauge-invariant functions,
not a replacement configuration or vacuum. Put
\[
\begin{array}{ll}
 U_2(i,k,l)=Z_{(i,k,l;2)}&(i\ge1),\qquad U_2(0,k,l)=I,\\
 U_3(i,k,l)=Z_{(i,k,l;3)}&((i,k)\ne(0,0)),\quad U_3(0,0,l)=I.
\end{array}\tag{JP1}
\]
The chord families have their original endpoint restrictions:
\(0\le k<m,0\le l\le m\) for direction two and
\(0\le i,k\le m,0\le l<m\) for direction three.

The complete original coefficient rows are as follows:
\[
\begin{gathered}
 h={\pi\over2n},\qquad v_0(l)=n^{-1/2},\qquad
 v_1(l)=\sqrt{2/n}\cos{\pi(l+1/2)\over n},\qquad
 w_1(l)=-\sqrt{2/n}\sin{\pi(l+1)\over n},\\
 a_{(i,k,l;2)}=\mathsf M_{1,(i,k,l;2)}
             =-{v_1(i)w_1(k)v_0(l)\over\sqrt2},\qquad
 a_{(i,k,l;3)}=\mathsf M_{1,(i,k,l;3)}=0,\\
 b_{(i,k,l;2)}=\mathsf M_{3,(i,k,l;2)}
             ={v_0(i)w_1(k)v_1(l)\over\sqrt2},\qquad
 b_{(i,k,l;3)}=\mathsf M_{3,(i,k,l;3)}
             =-{v_0(i)v_1(k)w_1(l)\over\sqrt2},\\
 S_1=\sum_c|a_c|
       =\sqrt{2/n}\cot h(\cot h-\cos h),\\
 S_3=\sum_c|b_c|
       =\sqrt{2/n}\big[(2-1/n)\cot^2h-(\cos h/n)\cot h\big].
\end{gathered}
\]
Here \(v_0,v_1\) have vertex indices \(0,\ldots,m\), and \(w_1\)
has edge indices \(0,\ldots,m-1\). Every row is restricted to the
original chords in (JP1). The absolute sums are evaluated with all
excluded tree edges retained as exclusions; their finite trigonometric
summations are proved in
[IP2–IP4](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/256d0fb1988e810df3fcb796c54077c564d48672/yang-mills/continuations/20261011-central-signs-shrinking-window/PHASE_MOMENTS_AND_ORIGINAL_PATH.md#L108).

Retain \(N=3m(m+1)^2\), \(M=3m^2(m+1)\) and the complete physical
Hamiltonian
\[
 H=\kappa H_0+b_{\rm mag}W,\quad
 H_0=-\sum_{e,\alpha}X_{e,\alpha}^2,\quad
 W=\sum_{\text{all faces }p}(2-\operatorname{tr}U_p),\quad
 \kappa={2g^2\over a},\quad b_{\rm mag}={1\over2g^2a},
 \quad \xi={b_{\rm mag}\over\kappa}={1\over4g^4}.
\]
The positive unit vacuum is \(H\psi=E_0\psi\), \(d\mu=\psi^2dU\);
the term \(2b_{\rm mag}M\) remains in this potential. Define
\[
 \sigma_*=\sqrt8\sin h,\quad\beta_0={\sigma_*\over2g^2},\qquad
 p=\beta_0\mathcal S,\quad r=\beta_0\mathcal S_{\mathcal R},
 \quad F=p-r,\qquad
 \mathcal Q_4=\mu(\mathcal S^2),\
 \mathcal Q_{4,\mathcal R}=\mu(\mathcal S\mathcal S_{\mathcal R}),\
 \mathcal K_1=\mu(|\nabla\mathcal S|^2),\
 \mathcal K_{\mathcal R}
   =\mu(\nabla\mathcal S\cdot\nabla\mathcal S_{\mathcal R}),
\]
where the vectors defining \(\mathcal S\) occur below. The exact
ground-state form is
\(\langle F\psi,(H-E_0)F\psi\rangle
=\kappa\mu(|\nabla F|^2)\).
Its proof multiplies the complete vacuum equation by \(F^2\psi\),
integrates by parts on the compact link product, and subtracts it
from the product-rule expression for
\(\langle F\psi,H F\psi\rangle-E_0\mu(F^2)\).
The two mixed derivatives and the \(F^2|\nabla\psi|^2\) terms then
cancel exactly, as do the full potential and energy terms.
Reflection invariance makes \(F\psi\) odd and vacuum orthogonal.
The original raw shrinking-window expression is
\[
 \mathscr E(s)=\mu(F^2)-{\kappa\over s}\mu(|\nabla F|^2)
 =2\beta_0^2(\mathcal Q_4-\mathcal Q_{4,\mathcal R})
   -{2\kappa\beta_0^2\over s}(\mathcal K_1-\mathcal K_{\mathcal R}).
\]
The spectral theorem gives
\(\langle F\psi,\mathbf1_{(0,s]}(H-E_0)F\psi\rangle
\ge\max\{0,\mathscr E(s)\}\). The requested joint path is
\(L_j=j^4,\ a_j=1/(100j),\
g_j^2=\kappa_*/(200j),\ s_j=\kappa_*/j\), so
\(\kappa_j=\kappa_*>0\). All subsequent path statements concern
this same \(F_j\psi_j\) and these exact coefficients, for \(j\ge2\).

Define the exact boundary set
\[
\mathcal B_2=\{(m,k,l;2):0\le k<m,0\le l\le m\},\qquad
\mathcal B_3=\{(m,0,l;3):0\le l<m\},\qquad
\mathcal B=\mathcal B_2\sqcup\mathcal B_3.
\tag{JP2}
\]
It has \(m(m+1)+m=m(m+2)=n^2-1\) members. These are exactly the
original chords that become tree links under the direction-one
reflection. No boundary face or direction-three member is omitted.

For every `(k,l)` define the ordered matrix products
\[
 B_l=\prod_{r=0}^{l-1}U_3(m,0,r),\qquad
 A_{k,l}=B_l\prod_{b=0}^{k-1}U_2(m,b,l),
\tag{JP3}
\]
where factors occur in increasing index order and empty products equal
identity. In the original tree-gauge coordinates the exact reflected
rooted words are
\[
\boxed{
\begin{split}
 Z^{\mathcal R}_{(i,k,l;2)}
    &=A_{k,l}U_2(m-i,k,l)A_{k+1,l}^{-1},\\
 Z^{\mathcal R}_{(i,k,l;3)}
    &=A_{k,l}U_3(m-i,k,l)A_{k,l+1}^{-1}.
\end{split}}\tag{JP4}
\]
To prove this, reflect each edge of the original root path. Its
direction-three segment lies at \(i=m,k=0\), its direction-two segment
at \(i=m\), and its reversed direction-one segment consists of original
tree links, hence identity in this exact coordinate presentation. The
first two segments are exactly (JP3). The reflected chord is the
corresponding link with first index \(m-i\), in the same orientation
because its direction is two or three. The final root segment is the
inverse of the complete endpoint product, proving both lines. In
particular the direction-three endpoint is \(A_{k,l+1}\), not a
commuted or abbreviated product of the direction-two factors at level
\(l\).

The reflected target link in (JP4) never belongs to \(\mathcal B\).
For direction two that would require \(i=0\), excluded from its chord
set. For direction three it would require \((i,k)=(0,0)\), likewise
excluded. A reflected target may be an original tree link, in which
case (JP1) retains its identity value. Thus all boundary dependence in
(JP4) occurs through its two endpoint transport products. This proves
the exact relation between the original tree coordinates and the
reflected ones on the whole compact configuration space.

## 2. Exact colour-vector transport and the reflection correction

For \(U\in SU(2)\), write
\(U=c(U)I+\sum_\alpha q^\alpha(U)T_\alpha\), with
\(c(U)=\operatorname{tr}U/2\) and \(T_\alpha=-i\sigma_\alpha/2\).
The original coordinate is \(q^\alpha=-2\operatorname{tr}(T_\alpha U)\).
Quaternion multiplication, with all signs retained, is
\[
 q(UV)=c(V)q(U)+c(U)q(V)+\tfrac12q(U)\times q(V).
 \tag{JP5}
\]
Indeed \(T_\alpha T_\beta=-\delta_{\alpha\beta}I/4
+\epsilon_{\alpha\beta\gamma}T_\gamma/2\); multiplying the full
matrices gives precisely this vector coefficient and the scalar
coefficient \(c(U)c(V)-q(U)\cdot q(V)/4\).

For a reflected chord with endpoints \(s=(k,l)\), \(t=(k+1,l)\)
or \((k,l+1)\), define
\[
 V_c=A_sA_t^{-1},\quad v_c=q(V_c),\quad c_c=c(V_c),\quad
 R_c=\operatorname{Ad}_{A_s}\in SO(3),\quad
 U_{\bar c}=U_2(m-i,k,l)\text{ or }U_3(m-i,k,l).
\]
Then (JP4)–(JP5) give the full affine quaternion formula
\[
\boxed{
 q_c^{\mathcal R}
 =c_cR_cq(U_{\bar c})+c(U_{\bar c})v_c
       +\tfrac12[R_cq(U_{\bar c})]\times v_c.}
\tag{JP6}
\]
It includes the scalar component of each original chord. Dropping that
component, either cross product, or an endpoint transport changes the
reflection map.

Use the original coefficients \(a_c=\mathsf M_{1c}\),
\(b_c=\mathsf M_{3c}\), and write
\(u_1^{\mathcal R}=\sum_ca_cq_c^{\mathcal R}\),
\(u_3^{\mathcal R}=\sum_cb_cq_c^{\mathcal R}\).
For clarity, define the errors as exact functions, not assumed small:
\[
\begin{split}
 e_1&=u_1^{\mathcal R}+u_1
   =\sum_ca_c[q_c^{\mathcal R}-q(U_{\bar c})]
       +\sum_{b\in\mathcal B_2}a_bq_b,\\
 e_3&=u_3^{\mathcal R}-u_3
   =\sum_cb_c[q_c^{\mathcal R}-q(U_{\bar c})]
       -\sum_{b\in\mathcal B}b_bq_b.
\end{split}\tag{JP7}
\]
To check every boundary sign, change the index \(i\) to \(m-i\).
The direction-two first-row coefficient changes sign because
\(v_1(m-i)=-v_1(i)\). Its reflected sum misses the original \(i=m\)
row and includes the original identity tree row \(i=0\), giving
\(-u_1+\sum_{\mathcal B_2}a_bq_b\). The third-row coefficient is
independent of \(i\), so its direction-two sum misses exactly
\(\mathcal B_2\). Its direction-three sum misses exactly
\(\mathcal B_3\) and includes the original identity tree links.
Adding the affine errors yields (JP7).

Set \(\mathcal S=u_1\cdot u_3\),
\(\mathcal S_{\mathcal R}=u_1^{\mathcal R}\cdot u_3^{\mathcal R}\),
and retain the complete reflection correction
\[
 D:=\mathcal S+\mathcal S_{\mathcal R}
   =e_1\cdot u_3-u_1\cdot e_3+e_1\cdot e_3.
 \tag{JP8}
\]
The last equality is the full product expansion of
\((-u_1+e_1)\cdot(u_3+e_3)\). All three terms remain.
On the exact fibre
\[
 \mathcal Z_{\mathcal B}
   =\{Z_b=I\text{ for every }b\in\mathcal B\}
\]
every \(A_s,V_c\) is identity, so \(e_1=e_3=0\) and \(D=0\).
Every other original chord on this fibre is arbitrary. Thus the failure
of the global reflection sign has an exact boundary-variable description;
it is not a statement that the reflected and original phase are unrelated.

## 3. The full normal derivative on that fibre

The vanishing of \(D\) on \(\mathcal Z_{\mathcal B}\) does not imply
vanishing physical gradient there. We now compute every normal derivative
and its complete physical kinetic metric.

For a boundary chord \(b\), let \(\epsilon_{s,b}\) equal one if its
matrix occurs in the ordered product \(A_s\) of (JP3), and zero otherwise.
Every such product traverses a boundary edge at most once and in positive
orientation. Put
\(\chi^-_{cb}=\epsilon_{s,b}-\epsilon_{t,b}\),
\(\chi^+_{cb}=\epsilon_{s,b}+\epsilon_{t,b}\).
At \(\mathcal Z_{\mathcal B}\), differentiation of the complete
reflected matrix product in (JP4) gives
\[
 X_{b,\alpha}q_c^{\mathcal R}
   =\chi^-_{cb}c(U_{\bar c})\mathbf e_\alpha
       +\tfrac12\chi^+_{cb}\,\mathbf e_\alpha\times q(U_{\bar c}).
 \tag{JP9}
\]
Here \(X_{b,\alpha}\) is the original left field on the physical chord
link \(b\). The target link is never in \(\mathcal B\), as proved
above. At boundary identity the differentiated left endpoint contributes
\(\epsilon_{s,b}T_\alpha U_{\bar c}\), and the differentiated inverse
right endpoint contributes \(-\epsilon_{t,b}U_{\bar c}T_\alpha\).
The vector coefficients of these products are respectively
\(c(U)\mathbf e_\alpha+\mathbf e_\alpha\times q(U)/2\) and
\(c(U)\mathbf e_\alpha-\mathbf e_\alpha\times q(U)/2\).
Subtract them with their displayed multiplicities to obtain (JP9).

For \(\mu=1,3\), define the original finite sums
\[
 a_{\mu b}^{\partial}
   =\sum_c\mathsf M_{\mu c}\chi^-_{cb}c(U_{\bar c}),\qquad
 v_{\mu b}^{\partial}
   =\tfrac12\sum_c\mathsf M_{\mu c}\chi^+_{cb}q(U_{\bar c}).
\]
Denote by \(n_b\in\mathbb R^3\) the vector with components
\(X_{b,\alpha}D\) on the boundary-identity fibre. Since there
\(u_1^{\mathcal R}=-u_1\), \(u_3^{\mathcal R}=u_3\), the complete
product rule gives
\[
\boxed{
 n_b=(\mathsf M_{1b}+a_{1b}^{\partial})u_3
       +(\mathsf M_{3b}-a_{3b}^{\partial})u_1
       +v_{1b}^{\partial}\times u_3
       -v_{3b}^{\partial}\times u_1.}
\tag{JP10}
\]
The direct derivatives of the original vectors are
\(X_{b,\alpha}u_\mu=\mathsf M_{\mu b}\mathbf e_\alpha\).
For the reflected vectors, insert (JP9); for example
\((\mathbf e_\alpha\times v_{1b}^{\partial})\cdot u_3
=\mathbf e_\alpha\cdot(v_{1b}^{\partial}\times u_3)\).
This proves all four terms and both cross-product signs in (JP10).

Let \(T_{be}\) be the signed sum of all occurrences of physical link
\(e\) in the original full rooted word \(Z_b\), with its inverse
traversals having negative sign. These are exactly the rows of the
original tangent incidence matrix indexed by \(\mathcal B\).
On \(\mathcal Z_{\mathcal B}\), all nonboundary chord derivatives of
\(D\) vanish because its restriction to that entire fibre is zero.
Every original boundary word consists only of original tree links and
its own boundary chord, all identity at this configuration. Therefore
the exact derivative of that word is
\(X_{e,\alpha}Z_b=T_{be}T_\alpha\). It follows that
\[
 X_{e,\alpha}D=\sum_{b\in\mathcal B}T_{be}n_b^\alpha,\qquad
 |\nabla D|^2=\sum_{\alpha=1}^3
   (n^\alpha)^{\mathsf T}G_{\mathcal B}n^\alpha,
 \quad G_{\mathcal B}=T_{\mathcal B}T_{\mathcal B}^{\mathsf T}.
\tag{JP11}
\]
This includes every original physical link, including all tree links.
It is not just the Euclidean chord-gradient norm.

The full matrix in (JP11) can be evaluated exactly. Regard \(\mathcal B\)
as edges of the comb-shaped tree on the \(n^2\) vertices `(k,l)` of the
right wall: it contains every direction-two edge at every height and
the direction-three spine at \(k=0\). Let \(D_{\rm wall}\) be its
oriented edge-to-vertex incidence matrix, with \(-1\) at its starting
vertex and \(+1\) at its ending vertex. Then
\[
\boxed{G_{\mathcal B}=2I+mD_{\rm wall}D_{\rm wall}^{\mathsf T}.}
\tag{JP12}
\]
For proof, expand each original boundary word into signed physical
occurrences before adding them. Common root prefixes occur once forward
and once backward; their signed derivatives cancel exactly. The remaining
cycle consists of its right-wall edge, its oppositely oriented left-wall
tree counterpart, a direction-one path of length \(m\) at the starting
wall vertex, and the reverse direction-one path at the endpoint. Distinct
boundary chords have distinct right- and left-wall edge counterparts,
giving the term \(2I\). Horizontal paths at different wall vertices are
disjoint. Two cycles' shared horizontal contributions therefore have
inner product \(m\) times the corresponding incidence-row inner product.
This proves (JP12) from the entire original words and their signs.

Equivalently the diagonal is \(2m+2\); adjacent direction-two edges
on the same height have entry \(-m\); adjacent spine edges have entry
\(-m\). A direction-two edge `(k,l;2)` and a spine edge `(l';3)` have
entry \(m\mathbf1_{k=0}(\mathbf1_{l=l'}-\mathbf1_{l=l'+1})\).
All other entries vanish. This lists every off-diagonal boundary term.
The tree incidence has full row rank: a putative linear dependence can
be removed successively at a leaf, where its incident coefficient must
be zero. In particular \(G_{\mathcal B}>2I\) as a finite matrix, and
the unconditional inequalities
\[
 2\sum_b|n_b|^2\le |\nabla D|^2
          \le(2+6m)\sum_b|n_b|^2
 \quad\text{on }\mathcal Z_{\mathcal B}
 \tag{JP13}
\]
follow. For the upper bound, every wall-tree vertex has degree at most
three; the sum of squared differences over its edges is at most six
times the vertex squared norm, using \((x-y)^2\le2x^2+2y^2\).
The nonzero singular values of \(D_{\rm wall}\) and its transpose
coincide, proving the required upper matrix bound.

The exact linear receiving map on the normal data space is
\(J_{\mathcal B}=T_{\mathcal B}^{\mathsf T}\otimes I_3\),
from \(\mathbb R^{3|\mathcal B|}\) to the original
\(\mathbb R^{3N}\) of physical link derivatives. Its squared metric
is \(G_{\mathcal B}\otimes I_3\); its inverse on its range is
\((G_{\mathcal B}^{-1}T_{\mathcal B})\otimes I_3\), and the
orthogonal projection onto that range is
\((T_{\mathcal B}^{\mathsf T}G_{\mathcal B}^{-1}T_{\mathcal B})
\otimes I_3\). Multiplication of these matrices proves the inverse
and the self-adjoint idempotent projection, using the positive
invertibility already established. This specifies the complete normal
space and its injection into the physical derivatives.

## 4. A nonzero normal derivative with every original coefficient

We evaluate (JP10) at a concrete original configuration. Set every
physical link to identity except the direction-two chord `(1,0,0;2)`,
whose value is \(K_*=\exp(\pi T_1)=2T_1\). All boundary chords are
identity. Vary only the boundary chord `(m,0,0;2)` through
\(H_b(t)=\exp(tT_1)\), keeping the original physical tree identity.
With \(h=\pi/(2n)\), retain the original cochains
\(v_0(l)=n^{-1/2}\),
\(v_1(l)=\sqrt{2/n}\cos(\pi(l+1/2)/n)\), and
\(w_1(l)=-\sqrt{2/n}\sin(\pi(l+1)/n)\).
Define the exact original coefficients and separate scalar functions
\[
 d_0={v_0(0)w_1(0)v_1(0)\over\sqrt2},\qquad
 A=-{v_1(1)w_1(0)v_0(0)\over\sqrt2},\qquad
 \eta(t)=2\sin(t/2),\quad \zeta_*=2,\quad \omega(t)=2\cos(t/2).
\]
Here \(d_0<0\), \(A>0\), since \(n\ge5\). The original vectors,
all along \(\mathbf e_1\), are
\[
 u_1=d_0\eta(t)+A\zeta_*,\qquad u_3=d_0[\eta(t)+\zeta_*].
\]
For the full reflected vectors one obtains
\[
 u_1^{\mathcal R}=-d_0\eta(t)-A[\omega(t)+\eta(t)],\qquad
 u_3^{\mathcal R}=d_0[2\eta(t)+\omega(t)].\tag{JP14}
\]
To verify these expressions directly from the full words, first omit
the bulk matrix \(K_*\). Every reflected rooted word containing \(H_b\) is
\(I,H_b\), or \(H_b^{-1}\), so its colour vector is exactly \(0,q(H_b)\),
or \(-q(H_b)\). Summing the original coefficients gives
\(u_1^{\mathcal R}=-d_0\eta(t)\), \(u_3^{\mathcal R}=d_0\eta(t)\), as
also follows from the exact single-link calculation in
[PK179–PK180](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md#L4025).
Restoring \(K_*\) changes only the reflected chord based at `(m-1,0,0)`:
its former word \(H_b^{-1}\) becomes \(K_*H_b^{-1}\), changing its colour
vector by \([\omega(t)+\eta(t)]\mathbf e_1\). Its first-row coefficient is
\(-A\) and its third-row coefficient is \(d_0\). This proves (JP14).

Substitute every term into \(D=u_1\cdot u_3+
u_1^{\mathcal R}\cdot u_3^{\mathcal R}\) before differentiating.
At \(t=0\), \(\eta=0,\eta'=1,\omega=2,\omega'=0\). The original product derivative
is \(2d_0(d_0+A)\), while the reflected product derivative is
\(-2d_0^2-6Ad_0\). Thus
\[
 D(0)=0,\qquad
 {d\over dt}D\big|_{t=0}=-4Ad_0=:d_*>0,
 \quad
 d_*={8\cos h\cos(3h)\sin^2(2h)\over n^3},
 \quad n^5d_*\longrightarrow8\pi^2.
 \tag{JP15}
\]
Every factor of the exact two chord coefficients remains in this formula.
It follows that no finite constant \(C\) and no exponent \(\gamma>0\)
can make the pointwise estimate
\[
 |\nabla D|^2\le
 C\left[\sum_{b\in\mathcal B}(2-\operatorname{tr}Z_b)\right]^\gamma
 \tag{JP16}
\]
hold on the whole original configuration space: the right side is zero
at the displayed configuration, while (JP15) makes the left side
positive. This refutes precisely that boundary-only gradient estimate.
It does not refute estimates involving the full plaquette potential,
such as IP12, or expectation estimates using additional actual-vacuum
information.

The exact object determined by this obstruction is the normal derivative
map
\(D\mapsto(n_b)_{b\in\mathcal B}\) on
\(\mathcal Z_{\mathcal B}\), with its physical receiving form
\(G_{\mathcal B}=2I+mD_{\rm wall}D_{\rm wall}^{\mathsf T}\).
Equations (JP9)–(JP12) construct the map, retain the scalar and vector
bulk components, and prove its connection to the complete physical
gradient. The obstruction therefore yields an explicitly calculated
space of normal derivative data, rather than ending the calculation.

## 5. An actual-vacuum contribution from the nonzero normal derivative

The fibre itself has Haar measure zero. We next thicken the evaluated
configuration and calculate a genuine actual-vacuum bound. This avoids
mistaking a pointwise calculation for an expectation estimate.

For the original absolute row sums \(S_1,S_3\), every twice
differentiated word contribution is bounded as in PK151–PK173. A mixed
derivative of a colour vector has norm at most
\(\frac12\sum_c|\mathsf M_{\mu c}|n_{ce}n_{cf}\le2S_\mu\).
This remains valid when the two fields coincide: the full count is
\(n_{ce}+2\binom{n_{ce}}2=n_{ce}^2\).
The complete product rule therefore gives
\[
 |X_{e,\alpha}X_{f,\beta}\mathcal S|
 \le (2S_3)(2S_1)+(2S_1)(2S_3)
       +(2S_1)(2S_3)+(2S_1)(2S_3)
 =16S_1S_3.
\]
The identical count for each reflected physical word, including inverse
traversals, gives the same bound for \(\mathcal S_{\mathcal R}\).
No replacement of a left field by a commuting derivative is used: each
product derivative is taken in its actual matrix order. Thus, for the
fixed original field \(Y=X_{(m,0,0;2),1}D\),
\[
 |\nabla Y|\le32\sqrt{3N}\,S_1S_3=:L_D,
 \quad N=3m(m+1)^2.\tag{JP17}
\]
The product bi-invariant metric has the original three fields as an
orthonormal frame on each radius-two three-sphere.

Let \(U_*\) be the exact configuration in Section 4 and define
\[
 R_*={d_*\over2L_D},\qquad
 r_*={R_*\over\sqrt N}
      ={d_*\over64\sqrt3\,N S_1S_3},\qquad
 v(r)={r-\sin r\over2\pi}.
\]
On the product of one-link balls of radius \(r_*\) around \(U_*\),
the product distance is at most \(R_*\). The bound (JP17) then implies
\(Y\ge d_*/2\). The radius is positive and less than one for all
\(L\ge2\): \(d_*=4|Ad_0|\le4S_1S_3\), hence
\(r_*\le1/(16\sqrt3N)<1\).
The Haar measure of a one-link radius-\(r\) ball on the radius-two
three-sphere is exactly \(v(r)\): integrate its spherical density
from angular radius zero to \(r/2\), giving
\((r/2-\sin(r/2)\cos(r/2))/\pi\).

The proved actual-vacuum floor
[PK212](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md#L4940)
is \(\psi^2\ge e^{-\Omega}\), where
\(\Omega=32\pi\xi M\), \(\xi=1/(4g^4)\),
\(M=3m^2(m+1)\). Integrating the nonnegative full gradient square over
the just-constructed product ball proves the unconditional estimate
\[
\boxed{
 \mu(|\nabla D|^2)
 \ge {d_*^2\over4}\,e^{-\Omega}[v(r_*)]^N>0,\qquad
 \kappa\beta_0^2\mu(|\nabla D|^2)
 \ge {\kappa\beta_0^2d_*^2\over4}\,
                         e^{-\Omega}[v(r_*)]^N.}
\tag{JP18}
\]
The second line is the actual raw energy of the even phase correction
\(\beta_0D\psi\). It is positive at every finite original regulator.
No unknown vacuum estimate has been assumed.

This lower bound becomes small on the required path. In fact
\[
 m_j=2j^4,\quad N_j=3(2j^4)(2j^4+1)^2,\quad
 M_j=24j^{12}+12j^8,\quad
 \Omega_j={320000\pi j^2M_j\over\kappa_*^2}.
\]
With \(S_1S_3/n^3\to64/\pi^4\),
\(d_*n^5\to8\pi^2\), and \(N/n^3\to3\), one has
\[
 n^{11}r_*\longrightarrow{\pi^6\over1536\sqrt3},\qquad
 {\log([v(r_*)]^N)\over n^3\log n}\longrightarrow-99.
\tag{JP19}
\]
Indeed \(v(r)/r^3\to1/(12\pi)\) as \(r\downarrow0\), so
\(\log v(r_*)=-33\log n+O(1)\). Multiplication by
\(N=3(n-1)n^2\) proves the last limit. The additional actual-vacuum
factor has \(\Omega_j\) of order \(j^{14}\), with the full boundary
term retained above. Thus (JP18) is an actual positive finite-regulator
contribution but supplies no positive limiting energy or spectral mass.

## 6. The exact six-term receiving cancellation

Return to the original \(F=\beta_0(\mathcal S-\mathcal S_{\mathcal R})
=\beta_0(2\mathcal S-D)\). The complete raw endpoint, before using
any reflection identity, is
\[
\begin{split}
\mathscr E(s)
=\beta_0^2\big[&4\mu(\mathcal S^2)-4\mu(\mathcal SD)+\mu(D^2)\\
 &-{\kappa\over s}\{
 4\mu(|\nabla\mathcal S|^2)
 -4\mu(\nabla\mathcal S\cdot\nabla D)
 +\mu(|\nabla D|^2)\}\big].
\end{split}\tag{JP20}
\]
All six terms are actual-vacuum expectations, with their original
coefficients. The original \(D\) and every derivative in this formula
are given by the full words (JP3)–(JP8), or directly PK151–PK153.
Reflection invariance and \(D\circ\mathcal R=D\) prove the exact
relations
\[
 2\mu(\mathcal SD)=\mu(D^2),\qquad
 2\mu(\nabla\mathcal S\cdot\nabla D)=\mu(|\nabla D|^2).
\tag{JP21}
\]
For example the first equality adds the equal integrals of
\(\mathcal SD\) and \(\mathcal S_{\mathcal R}D\); their integrand sum
is \(D^2\). The second uses reflection invariance of the original
physical metric in exactly the same addition. Consequently (JP20) also
satisfies, without discarding its expanded form,
\[
\mathscr E(s)=4\beta_0^2
 \left[\mathcal Q_4-{\kappa\over s}\mathcal K_1\right]
 -\beta_0^2\mu(D^2)
 +{\kappa\beta_0^2\over s}\mu(|\nabla D|^2).
\tag{JP22}
\]
In particular the nonzero boundary-normal energy has the positive sign
in this endpoint; the even correction's mass has the negative sign.
Neither one can replace their difference.

For the actual joint path, \(\kappa/s=j\), so (JP18) yields the
unconditional one-sided refinement
\[
\begin{split}
\mathscr E_j(s_j)\ge
&4\beta_{0,j}^2[\mathcal Q_{4,j}-j\mathcal K_{1,j}]
  -\beta_{0,j}^2\mu_j(D_j^2)\\
&+{j\beta_{0,j}^2d_{*,j}^2\over4}\,
                    e^{-\Omega_j}[v(r_{*,j})]^{N_j}.
\end{split}\tag{JP23}
\]
This displays a proved, strictly positive actual correction term, rather
than a cutoff-existence statement. It still contains the actual mass and
gradient expectations in the first line. Applying only their available
global bounds leaves a nonpositive lower estimate, even after the positive
term is included. It does not prove that the true endpoint is negative.

The attempted boundary-only gradient estimate failed by the exact normal
derivative (JP15). The next calculation constructed its full boundary
kinetic form (JP12), then thickened that fibre point and integrated in the
actual vacuum, producing (JP18) and (JP23). What remains unresolved is
control of the complete cancellation in (JP20) or (JP22) at the specified
\(g_j\), particularly the boundary-normal derivative contribution over
the actual vacuum distribution and its relation to the even correction's
raw mass. No selected smaller coupling, normalized vector, Gaussian
replacement, conditional theorem, or continuum conclusion is used.

## 7. A conditional boundary estimate with the complete word degree

The loss in (JP18) integrates a small ball in every original link.
The next calculation instead evaluates the boundary normal data by an
exact finite-dimensional kernel, uses the actual conditional boundary
density, and then extracts a nonzero bulk harmonic. This removes that
small-ball factor and reduces the vacuum exponent.

First make the measure map explicit. For every nonroot vertex \(v\),
use its original root transport \(t_v\) as a tree-coordinate variable.
For every chord use its full word \(Z_c=t_sU_ct_t^{-1}\).
Conversely a tree edge from \(s\) to \(t\) is \(t_s^{-1}t_t\),
and a chord edge is \(t_s^{-1}Z_ct_t\), with \(t_{\rm root}=I\).
Successive invariance of Haar measure under left and right multiplication,
starting at the root and proceeding along the tree, proves that this
change of variables takes product Haar measure exactly to product Haar
measure in the \(t_v,Z_c\). The original gauge-invariant vacuum and the
functions used here are independent of the \(t_v\). Thus their exact
measure is \(\rho(Z)\prod_cdZ_c\), where \(\rho=\psi^2\) in the
tree presentation and \(\int\rho=1\). No vacuum is changed by this map.

Write \(z=(Z_c)_{c\notin\mathcal B}\), \(B=(Z_b)_{b\in\mathcal B}\).
Define the actual marginal and conditional density by
\[
 \rho_{\rm bulk}(z)=\int\rho(B,z)\,dB,\qquad
 p_{\mathcal B}(B\mid z)={\rho(B,z)\over\rho_{\rm bulk}(z)},\qquad
 d\mu_{\rm bulk}(z)=\rho_{\rm bulk}(z)\,dz .
 \tag{JP24}
\]
Positivity and smoothness of the original finite-volume vacuum make
these definitions valid at every \(z\), with no exceptional zero
denominator.

The original local score estimate is
\(\|\nabla_e\log\rho\|_\infty\le4r_e\xi\), where
\(\xi=1/(4g^4)\) and \(r_e\) is the actual number of incident faces.
Its full partial Bochner proof, including the mixed Hessians and the
radius-two metric, is in the original
[TeX, equations (77)–(79) and (113)–(115)](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/485b61423c1f4e1805deb453c1b6b342b27842b6/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/sources/spatial/spatial_continuum.tex#L1415).
Changing an original chord while keeping the original tree identity
is its physical left variation, so the same score bound holds for the
corresponding \(Z_b\) variable. Join two boundary configurations by
shortest one-link geodesics of length at most \(2\pi\). The
normalization in (JP24) is independent of \(B\). Therefore
\[
 {\max_B p_{\mathcal B}(B\mid z)\over
       \min_B p_{\mathcal B}(B\mid z)}
 \le e^{\Omega_{\mathcal B}},\qquad
 p_{\mathcal B}(B\mid z)\ge e^{-\Omega_{\mathcal B}},\qquad
 \Omega_{\mathcal B}=8\pi\xi\sum_{b\in\mathcal B}r_b
                   =24\pi\xi m(m+1).
 \tag{JP25}
\]
Here all face incidences are retained. A member \((m,k,l;2)\)
has \(r_b=1+\mathbf1_{l>0}+\mathbf1_{l<m}\). Their sum is
\(m(3m+1)\). Each \((m,0,l;3)\) has two incident faces, contributing
\(2m\). The total is \(3m(m+1)\). The lower bound follows from the
ratio bound and the fact that the conditional density has integral one;
it is not a claim of conditional independence. The ratio of this exponent
to the earlier \(\Omega=32\pi\xi M=96\pi\xi m^2(m+1)\) is \(1/(4m)\).

For fixed \(z\), each full word (JP4) has boundary polynomial degree
at most \(4m-1\) and degree at most two in any single boundary matrix.
Indeed the endpoint products have respective lengths \(k+l\) and
\(k+l+1\). Their sum is \(2k+2l+1\le4m-1\), using the original
direction-two or direction-three endpoint restrictions. Every inverse
\(SU(2)\) matrix is linear in its four real quaternion coordinates.
Each factor \(q(Z_c^{\mathcal R})\) is therefore a polynomial with
these degrees. The full dot product and the original unreflected dot
product show that \(D(B,z)\), and every \(X_{b,\alpha}D(B,z)\), belong
to the following explicitly finite boundary space:
\[
 \begin{split}
 b_\partial&=|\mathcal B|=m(m+2),\qquad K_m=8m-2,\\
 \mathcal H_{\partial,m}
 &=\bigoplus_{\substack{0\le\ell_b\le4\\
                        \sum_b\ell_b\le K_m}}
       \bigotimes_{b\in\mathcal B}\mathcal Y_{\ell_b},\\
 A_m:=\dim\mathcal H_{\partial,m}
 &=\sum_{r=0}^{K_m}[z^r]
          (1+4z+9z^2+16z^3+25z^4)^{b_\partial}
 \le55^{b_\partial}.
 \end{split}\tag{JP26}
\]
Here \(\mathcal Y_\ell\) is the space of degree-\(\ell\) spherical
harmonics on the unit quaternion three-sphere, with the radius-two
group metric for differentiation. Its dimension is
\(\binom{\ell+3}{3}-\binom{\ell+1}{3}=(\ell+1)^2\), where the second
term is zero for \(\ell<2\). This dimension follows by decomposing
homogeneous polynomials into a harmonic part and the squared radius
times a polynomial two degrees lower. Restriction to the sphere
therefore takes a polynomial of degree \(d\) into harmonics of degrees
at most \(d\). The left fields are infinitesimal orthogonal rotations
of these four real coordinates, so they preserve each harmonic degree
and the stated total-degree restriction. This proves every inclusion
and multiplicity in (JP26) directly for the original words.

The reproducing kernel of \(\mathcal H_{\partial,m}\) has constant
diagonal \(A_m\). In fact the space is invariant under the transitive
left action of the product boundary group, so an orthonormal-basis
sum of squared absolute values is constant; its integral is the
dimension. Cauchy–Schwarz consequently gives
\[
 |h(I_{\mathcal B})|^2\le A_m\int|h(B)|^2\,dB
 \quad(h\in\mathcal H_{\partial,m}).
 \tag{JP27}
\]
Apply this to every component \(X_{b,\alpha}D\), whose value at
boundary identity is precisely \(n_b^\alpha(z)\). Combine (JP25)
with the original full physical gradient, which includes every boundary
chord field. Integrating the unchanged bulk marginal gives the actual
receiving estimate
\[
 \boxed{\displaystyle
 \mu(|\nabla D|^2)\ge
 {e^{-\Omega_{\mathcal B}}\over A_m}
       \int\sum_{b\in\mathcal B}|n_b(z)|^2\,d\mu_{\rm bulk}(z).}
 \tag{JP28}
\]
All \(n_b\) here are the exact scalar-and-vector expressions (JP10).
The full fibre metric \(G_{\mathcal B}\) is not substituted for the
physical metric away from the fibre. Instead only the always valid
subset inequality
\(\sum_{b,\alpha}|X_{b,\alpha}D|^2\le|\nabla D|^2\) is used there.

The dimension in (JP26) has substantially less loss than its displayed
product bound. Coefficientwise,
\(1+4z+9z^2+16z^3+25z^4\le(1-z)^{-4}\);
hence, for every original \(m\ge4\),
\[
 A_m\le {4b_\partial+K_m\choose K_m},\qquad
 \lim_{m\to\infty}{\log A_m\over m\log m}=8 .
 \tag{JP29}
\]
For the upper bound, sum the coefficients of \((1-z)^{-4b_\partial}\)
through \(K_m\). For the limit, once \(b_\partial\ge K_m\), selecting
\(K_m\) distinct degree-one factors also gives
\(A_m\ge4^{K_m}\binom{b_\partial}{K_m}\).
The logarithms of this lower bound and the upper bound are both
\(K_m\log(b_\partial/K_m)+O(K_m+K_m^2/b_\partial)
=8m\log m+O(m)\), by the finite products for the binomial
coefficients and \(\log K_m!=K_m\log K_m-K_m+O(\log K_m)\).
These explicit upper and lower bounds prove the limit.

## 8. A single bulk harmonic removes the remaining expectation

The right side of (JP28) still contains an actual expectation. We now
evaluate a nonzero harmonic component of its integrand, with all other
bulk chords arbitrary. Fix
\[
 b_*=(m,0,0;2),\qquad k_*=(1,0,0;2),
\]
and retain the same exact \(A,d_0,d_*=-4Ad_0\) from (JP14)–(JP15).
In (JP10), only the reflected chord \(c=(m-1,0,0;2)\) has target
\(k_*\). Its original coefficients are \(-A,d_0\), and its boundary
occurrence signs for \(b_*\) are \(\chi^-=-1,\chi^+=1\).
Writing \(c=c(Z_{k_*})\), \(q=q(Z_{k_*})\), the complete dependence is
\[
 \begin{array}{ll}
 u_1=u_1^0+Aq,&u_3=u_3^0+d_0q,\\
 a_{1b_*}^{\partial}=a_1^0+Ac,
   &a_{3b_*}^{\partial}=a_3^0-d_0c,\\
 v_{1b_*}^{\partial}=v_1^0-\tfrac12Aq,
   &v_{3b_*}^{\partial}=v_3^0+\tfrac12d_0q .
 \end{array}\tag{JP30}
\]
Every superscript-zero quantity is independent of \(Z_{k_*}\) but
keeps its complete dependence on all other bulk chords. Substituting
into (JP10), the self cross products vanish by \(q\times q=0\),
and the two \(cq\) coefficients add. Consequently
\[
 n_{b_*}(z)=2Ad_0\,c q+c\,h^0+M^0q+v^0 .
 \tag{JP31}
\]
Here \(h^0,v^0\) are vectors and \(M^0\) is a real matrix, all independent
of \(Z_{k_*}\). This is an equality following from the entire (JP10),
not an approximation at small coupling or near identity.

For unit quaternions \((x_0,x_1,x_2,x_3)\), \(c=x_0\) and
\(q_\alpha=2x_\alpha\). Rotation invariance of Haar measure gives
\[
 \int cq_\alpha=0,\quad
 \int cq_\alpha\,c=0,\quad
 \int cq_\alpha\,q_\beta=0,\quad
 \int cq_\alpha\,cq_\beta={\delta_{\alpha\beta}\over6}.
 \tag{JP32}
\]
For the last constant, let \(a=\int x_0^4\) and
\(b=\int x_0^2x_1^2\). Invariance under the rotation
\(x_0\mapsto(x_0+x_1)/\sqrt2\) gives \(a=3b\).
Integration of \((\sum_{\alpha=0}^3x_\alpha^2)^2=1\) gives
\(4a+12b=1\), hence \(b=1/24\). Multiplication by four proves
the stated \(1/6\); parity gives all other equalities.
The vector field \(2Ad_0cq\) is therefore the orthogonal harmonic
projection of (JP31) onto this quadratic component. For every fixed
choice of the other bulk chords,
\[
 \int |n_{b_*}|^2\,dZ_{k_*}
 \ge (2Ad_0)^2\sum_{\alpha=1}^3{1\over6}
 ={d_*^2\over8}.
 \tag{JP33}
\]

The actual marginal in (JP24) has the same one-link score bound:
differentiation under its finite compact integral gives
\[
 \nabla_{k_*}\log\rho_{\rm bulk}
 ={\int\rho\,\nabla_{k_*}\log\rho\,dB\over
          \int\rho\,dB},
\]
whose norm is at most \(4r_{k_*}\xi=12\xi\).
There are exactly three incident faces: both direction-one faces
because \(1\) is an interior first coordinate, and the positive
direction-three face because the third coordinate is zero.
The conditional density of \(Z_{k_*}\) within the actual bulk marginal
is therefore at least \(e^{-24\pi\xi}\). Applying (JP33) to that
conditional density, then integrating every remaining bulk variable,
proves the entirely evaluated bounds
\[
 \int\sum_b|n_b|^2d\mu_{\rm bulk}
       \ge {d_*^2\over8}e^{-24\pi\xi},\qquad
 \boxed{\displaystyle
 \mu(|\nabla D|^2)\ge
 {d_*^2\over8A_m}
       e^{-24\pi\xi[m(m+1)+1]}>0.}
 \tag{JP34}
\]
The original raw correction energy is bounded below by the second
expression times its full factor \(\kappa\beta_0^2\).
This is an actual-vacuum estimate at every finite original regulator.
It has no unproved vacuum moment or unknown marginal on its right side.

Along the specified original path, no coupling is selected or changed:
\[
 \xi_j={10000j^2\over\kappa_*^2},\quad m_j=2j^4,\qquad
 24\pi\xi_j[m_j(m_j+1)+1]
 ={240000\pi\over\kappa_*^2}
             (4j^{10}+2j^6+j^2),\qquad
 {\log A_{m_j}\over j^4\log j}\longrightarrow64 .
 \tag{JP35}
\]
Thus (JP34) replaces the \(j^{14}\) vacuum exponent and the
all-link small-ball term of (JP18) by this explicit \(j^{10}\)
exponent and an explicitly counted degree space. In the original
endpoint it proves the further unconditional estimate
\[
 \boxed{\begin{split}
 \mathscr E_j(s_j)\ge&
 4\beta_{0,j}^2[\mathcal Q_{4,j}-j\mathcal K_{1,j}]
       -\beta_{0,j}^2\mu_j(D_j^2)\\
 &+{j\beta_{0,j}^2d_{*,j}^2\over8A_{m_j}}\,
    \exp\!\left[-{240000\pi\over\kappa_*^2}
                       (4j^{10}+2j^6+j^2)\right].
 \end{split}}\tag{JP36}
\]
No statement about the sign of the remaining full expression is
inferred from this strictly positive correction.

## 9. The boundary mass-to-energy map and its precise path loss

The preceding energy lower bound does not control the negative even
mass in (JP22). The next calculation derives the direct mass-to-energy
map from the same exact word space. For fixed \(z\), let
\(\overline D(z)=\int D(B,z)dB\) and \(h=D-\overline D\).
The nonconstant part of \(\mathcal H_{\partial,m}\) has reproducing
kernel diagonal \(A_m-1\). Since \(D(I_{\mathcal B},z)=0\),
\(|\overline D|^2=|h(I_{\mathcal B})|^2\le(A_m-1)\int|h|^2dB\).
The product sphere Laplacian on harmonic degree tuple
\((\ell_b)_b\) has eigenvalue
\(\sum_b\ell_b(\ell_b+2)/4\): the denominator four is the original
radius-two metric. Indeed the Euclidean polar-coordinate formula in
four dimensions gives
\(\Delta(r^\ell Y)=r^{\ell-2}
[\ell(\ell+2)Y+\Delta_{S^3}Y]\); a homogeneous harmonic polynomial
makes this zero, and radius two divides the eigenvalue by four.
The product operator sums the individual factor eigenvalues.
Every nonconstant tuple has eigenvalue at least
\(3/4\). Orthogonality of the finite harmonic decomposition therefore
proves, directly for these functions,
\[
 \int D^2dB
 =|\overline D|^2+\int|h|^2dB
 \le {4A_m\over3}
             \int\sum_{b,\alpha}|X_{b,\alpha}D|^2dB .
 \tag{JP37}
\]
Multiply the first integral by the maximum conditional density,
divide the last by its minimum, and use their ratio in (JP25).
Finally integrate the unchanged bulk marginal. The result is
\[
 \boxed{\displaystyle
 \mu(D^2)\le {4A_m\over3}e^{\Omega_{\mathcal B}}
                      \mu(|\nabla D|^2),\qquad
 \kappa\beta_0^2\mu(|\nabla D|^2)
     \ge\delta_{\partial}\,\beta_0^2\mu(D^2),\quad
 \delta_{\partial}={3\kappa\over4A_m}e^{-\Omega_{\mathcal B}}.}
 \tag{JP38}
\]
This is a state-specific inequality for the original even correction;
it is not a claim about the complete physical gap. In particular it
retains a possible vacuum component of \(D\psi\); no centering is
inserted in (JP37) or (JP38).

The estimate has a determinate limitation on the requested window:
\[
 {\delta_{\partial,j}\over s_j}
 ={3j\over4A_{m_j}}
       \exp\!\left[-{240000\pi\over\kappa_*^2}
                         (4j^{10}+2j^6)\right]\longrightarrow0 .
 \tag{JP39}
\]
Accordingly (JP38) bounds the full even contribution in (JP22) by
\[
 {\kappa\beta_0^2\over s}\mu(|\nabla D|^2)
                -\beta_0^2\mu(D^2)
 \ge \left({\delta_\partial\over s}-1\right)
                       \beta_0^2\mu(D^2).
\]
The proved coefficient approaches \(-1\), so this calculation does
not certify a nonnegative even contribution at the shrinking window.
It also does not prove that the actual contribution is negative.
The unresolved issue is the actual cancellation between the complete
four-loop mass and gradient expectations in (JP20)–(JP22) at
\(g_j^2=\kappa_*/(200j)\). The successive calculations above identify
the exact boundary normal defect, evaluate a nonzero bulk harmonic
in the actual vacuum, remove all unknown expectations from the positive
energy correction, and derive the direct even mass-to-energy map.
Their explicit original-path losses, rather than an assumed missing
estimate, determine precisely what these results do and do not settle.

## 10. The global two-link harmonic removes the boundary loss

There is a stronger continuation of (JP30)–(JP34). Keep
\(k=Z_{k_*}\), \(h_b=Z_{b_*}\) with the same two original physical
chords \(k_*=(1,0,0;2)\), \(b_*=(m,0,0;2)\), but now allow every
boundary chord to be arbitrary. The link \(k_*\) occurs as a reflected
target in exactly one chord, \((m-1,0,0;2)\). Its endpoint products
are \(A_{0,0}=I\) and \(A_{1,0}=h_b\). Thus its full reflected word
is \(kh_b^{-1}\). It occurs in no boundary transport product.
Consequently the exact dependence on \(k\), with every other chord
fixed arbitrarily, is
\[
 \begin{array}{ll}
 u_1=U_1+Aq(k),& u_3=U_3+d_0q(k),\\
 u_1^{\mathcal R}=V_1-Aq(kh_b^{-1}),
   &u_3^{\mathcal R}=V_3+d_0q(kh_b^{-1}),
 \end{array}\tag{JP40}
\]
where \(U_1,U_3,V_1,V_3\) retain their full dependence on all
remaining original chords and are independent of \(k\). In particular
they may depend on \(h_b\). Multiplying the original vectors, without
omitting any summand, gives
\[
 \begin{split}
 \mathcal S={}&U_1\cdot U_3
       +(d_0U_1+AU_3)\cdot q(k)+Ad_0|q(k)|^2,\\
 \mathcal S_{\mathcal R}={}&V_1\cdot V_3
       +(d_0V_1-AV_3)\cdot q(kh_b^{-1})
                       -Ad_0|q(kh_b^{-1})|^2 .
 \end{split}\tag{JP41}
\]
Right multiplication by the fixed \(h_b^{-1}\) acts linearly on the
four real quaternion coordinates of \(k\). Therefore all terms in
(JP41) except the two displayed squared norms are affine-linear in
those four coordinates. This remains true after any physical
\(b_*\)-derivative: it differentiates the retained coefficients and
the linear right-multiplication matrix, never raising the \(k\)-degree.

For \(h_b(t)=\exp(tT_\alpha)h_b\), put \(V=kh_b^{-1}\).
Then \(kh_b(t)^{-1}=V\exp(-tT_\alpha)\). The full quaternion
product gives
\[
 {d\over dt}c(V\exp(-tT_\alpha))\big|_0
       ={q_\alpha(V)\over4},\qquad
 {d\over dt}|q(V\exp(-tT_\alpha))|^2\big|_0
       =-2c(V)q_\alpha(V).
\]
Here \(|q(V)|^2=4[1-c(V)^2]\) retains the radius and the original
normalization of \(q\). The unreflected quadratic term in (JP41)
does not depend on \(h_b\). It follows, globally and with every
boundary link arbitrary, that
\[
 X_{b_*,\alpha}D
   =2Ad_0c(kh_b^{-1})q_\alpha(kh_b^{-1})
                  +R_\alpha(k),
 \tag{JP42}
\]
where \(R_\alpha(k)\) is the full affine-linear remainder obtained
by differentiating all other terms of (JP41). Its coefficients
retain every other chord, scalar part, endpoint transport, and
derivative of \(U_\mu,V_\mu\).

The first term in (JP42) is a degree-two harmonic in \(k\).
Right Haar invariance and (JP32) prove that it has mean zero and
is orthogonal to the entire remainder \(R_\alpha\). This is an
orthogonal projection used to establish an inequality; the original
function and remainder remain in (JP42). Summing the exact
quadratic norms gives, for every fixed exterior configuration,
\[
 \int\sum_{\alpha=1}^3|X_{b_*,\alpha}D|^2\,dk
 \ge {d_*^2\over8}.
\]
The actual conditional density of \(k_*\), with every other chord
fixed, is at least \(e^{-24\pi\xi}\), by the same three incident
faces used in Section 8. Integrating that conditional and then its
actual exterior marginal proves the global improvement
\[
 \boxed{\displaystyle
 \mu(|\nabla D|^2)\ge{d_*^2\over8}e^{-24\pi\xi},\qquad
 \kappa\beta_0^2\mu(|\nabla D|^2)
             \ge{\kappa\beta_0^2d_*^2\over8}e^{-24\pi\xi}.}
 \tag{JP43}
\]
Thus the boundary band factor and boundary density penalty in (JP34)
were losses of that particular receiving route. The global exact word
calculation removes both. No boundary link has been set to identity
in this proof.

The resulting bound for the unchanged endpoint is
\[
 \boxed{\begin{split}
 \mathscr E_j(s_j)\ge&
 4\beta_{0,j}^2[\mathcal Q_{4,j}-j\mathcal K_{1,j}]
                  -\beta_{0,j}^2\mu_j(D_j^2)\\
 &+{j\beta_{0,j}^2d_{*,j}^2\over8}
                  \exp\!\left(-{240000\pi j^2\over\kappa_*^2}\right).
 \end{split}}\tag{JP44}
\]
In this expression
\[
 j^3\beta_{0,j}\longrightarrow{50\sqrt2\pi\over\kappa_*},
 \qquad j^{20}d_{*,j}\longrightarrow{\pi^2\over4}.
\]
These follow directly from \(\beta_{0,j}=100j\sqrt8\sin h_j/\kappa_*\),
\(n_j=2j^4+1\), and (JP15). In particular, multiplying the last
positive term in (JP44) by
\(j^{45}\exp(240000\pi j^2/\kappa_*^2)\) gives the exact limit
\(625\pi^6/(16\kappa_*^2)\). This evaluates the scale of the
proved positive contribution, while leaving the actual unbounded
regulator cancellation explicit.

## 11. Actual raw mass and energy of the original odd polynomial

The same global decomposition evaluates a harmonic component of
the original \(F=\beta_0(\mathcal S-\mathcal S_{\mathcal R})\).
For a quaternion \(U\), define only as an auxiliary polynomial
\(\chi_1(U)=4c(U)^2-1\). Since \(|q(U)|^2=3-\chi_1(U)\),
the complete quadratic harmonic parts in \(k\) of (JP41) are
\[
 P_2\mathcal S=-Ad_0\chi_1(k),\qquad
 P_2\mathcal S_{\mathcal R}=Ad_0\chi_1(kh_b^{-1}),
 \tag{JP45}
\]
where \(P_2\) is the degree-two Haar harmonic projection in the
single original chord \(k_*\). The respective constant pieces
\(+3Ad_0\) and \(-3Ad_0\) remain in their affine remainders.
Thus \(P_2\) is not a redefinition of either physical polynomial.

Here are the exact integrals, including their dependence on the
arbitrary boundary link:
\[
 \int\chi_1(k)^2dk=1,\qquad
 \int\chi_1(k)\chi_1(kh_b^{-1})dk
       ={4c(h_b)^2-1\over3}=:\rho_b.
\]
To prove them directly, write \(k=(x_0,\mathbf x)\),
\(h_b=(y_0,\mathbf y)\). Then \(c(kh_b^{-1})=x\cdot y\).
The second- and fourth-order sphere moments calculated in (JP32)
give \(\int x_0^2=1/4\) and
\(\int x_0^2(x\cdot y)^2=(1+2y_0^2)/24\).
Expanding both factors \(4c^2-1\) gives the two formulas.
Consequently the full conditional harmonic Gram matrix of
\((\mathcal S,\mathcal S_{\mathcal R})\) is
\[
 \Gamma_2(h_b)=A^2d_0^2
       \begin{pmatrix}1&-\rho_b\\-\rho_b&1\end{pmatrix}.
 \tag{JP46}
\]
All affine remainders are orthogonal to this harmonic matrix in
the single-link Haar integral. In the odd combination this gives
\[
 \int|P_2F|^2dk
 =\beta_0^2A^2d_0^2(2+2\rho_b)
 ={\beta_0^2d_*^2\over12}[1+2c(h_b)^2]
 \ge{\beta_0^2d_*^2\over12}.
\]
The original \(k_*\)-Laplacian acts on every degree-two harmonic
by the original eigenvalue \(2(2+2)/4=2\). The left derivatives
preserve harmonic degree, so the quadratic derivatives are
orthogonal to the derivatives of the affine remainder, including
the retained constants whose derivatives are zero. Integration by
parts on the single compact group therefore gives
\(\int\sum_\alpha|X_{k_*,\alpha}F|^2dk
\ge2\int|P_2F|^2dk\).
Applying the actual conditional density floor, before integrating
the unchanged exterior marginal, proves
\[
 \boxed{\displaystyle
 G=\mu(F^2)\ge{\beta_0^2d_*^2\over12}e^{-24\pi\xi},\qquad
 C_F=\kappa\mu(|\nabla F|^2)
       \ge{\kappa\beta_0^2d_*^2\over6}e^{-24\pi\xi}.}
 \tag{JP47}
\]
These are evaluated actual-vacuum bounds for the original raw odd
state. In particular the raw state is nonzero at every original
finite regulator. Both bounds retain \(\beta_0\), \(\kappa\), the
actual face count, and the exact two chord coefficients.
They are separate lower bounds: they do not assert
\(C_F\ge2\kappa G\), since the full actual mass includes the
retained remainder and its vacuum-dependent cross terms.

For completeness, the even combination of (JP46) has norm
\[
 \int|P_2D|^2dk
   =2A^2d_0^2(1-\rho_b)
   ={d_*^2\over24}|q(h_b)|^2.
\]
After the \(k_*\) conditional lower bound, integrate all other
variables to obtain the actual marginal of \(h_b\). Its logarithmic
score is at most \(4r_{b_*}\xi=8\xi\), by the same differentiation
under the marginal integral used in Section 8. The boundary link
\((m,0,0;2)\) has exactly two incident faces. Its marginal density
is therefore at least \(e^{-16\pi\xi}\), and
\(\int|q(h_b)|^2dh_b=3\). Thus
\[
 \boxed{\displaystyle
 \mu(D^2)\ge{d_*^2\over8}e^{-40\pi\xi}.}
 \tag{JP48}
\]
More generally the full actual mass Gram matrix of
\((\mathcal S,\mathcal S_{\mathcal R})\) is bounded below by
\(A^2d_0^2e^{-40\pi\xi}I_2\): apply the same two successive
density floors to (JP46) and use \(\int\rho_b\,dh_b=0\).
This follows for every real or complex linear combination, so it
is a matrix inequality, with all original affine terms included.

On the prescribed path, the right sides of (JP47) are respectively
asymptotic to
\[
 {625\pi^6\over24\kappa_*^2}\,
       j^{-46}e^{-240000\pi j^2/\kappa_*^2},
 \qquad
 {625\pi^6\over12\kappa_*}\,
       j^{-46}e^{-240000\pi j^2/\kappa_*^2}.
 \tag{JP49}
\]
These statements concern the proved bounds, not asymptotic
equalities for the unknown actual \(G_j,C_{F,j}\).
The positive even energy (JP43), nonzero even mass (JP48), and
original odd mass and energy (JP47) all arise from the same complete
two-link harmonic calculation. They strengthen the earlier
boundary-restricted route, while (JP38) remains the proved direct
even mass-to-energy comparison. Neither an energy lower bound
nor a total raw mass lower bound determines spectral mass inside
\((0,s_j]\). The actual sign of
\(G_j-C_{F,j}/s_j\), equivalently the full four-loop/gradient
cancellation (JP20)–(JP22), remains unresolved on this path.
