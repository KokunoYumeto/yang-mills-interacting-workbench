# The complete fourth coefficient of the original fifth-reference Schur map

11 October 2026. This note evaluates the unchanged original open-box Schur coefficient, including the complementary projection at every intermediate return, every source multiplicity, every original support label, and all boundary incidences. The accepted P1–P45 proof is preserved in the adjacent file [Original J5 parity and tail](../ORIGINAL_J5_PARITY_AND_TAIL.md). The present result supplies its formerly unevaluated fourth coefficient.

The inputs are the original programme recurrence, not a substituted reference. Pinned public definitions are [G1–G31, original coefficient space and bilinear map](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/fa79faff2cd697e16cfa3a7953f36810c22c8922/yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md), [B13–B16, both shared-edge channels](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/fa79faff2cd697e16cfa3a7953f36810c22c8922/yang-mills/continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md#L125), and [F1–F42, full fifth reference](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/33a4c39de32c2c7fdf6f8ce796e40389f766669f/yang-mills/consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md). Verbatim retained originals are the [17 September independent-source proof](verification_sources/FIFTH_SOURCE.md), [physical-response proof](verification_sources/PLAQUETTE_RESPONSE.md), and [sixth-energy proof](verification_sources/SIXTH_ENERGY.md). These originals and the exact differential algebra are identified by complete file digests in PUBLIC_SOURCE_READING_USE_LEDGER.json and VERIFICATION_SOURCE_RECEIPTS.json. They are programme derivations, not human primary papers.

The center-sign symmetry used below has the human antecedent L. Li and Y. Meurice, [Lattice gluodynamics at negative \(g^2\), arXiv:hep-lat/0410029v2](https://arxiv.org/abs/hep-lat/0410029v2), [original author TeX](https://arxiv.org/src/hep-lat/0410029v2), Section IV. The exact open-boundary Hamiltonian and labelled-source maps are proved in the adjacent P1–P45 note. No historical-priority claim is made for that symmetry or for the source recurrence.

## Q1. Original objects and the coefficient to be evaluated

Fix an integer \(L\ge2\). The original vertices are
\[
 V_L=\{-L,\ldots,L\}^3,
\]
the positive edge \((n,i)\) runs from \(n\) to \(n+e_i\) when both vertices lie in \(V_L\), and the original faces are
\[
 \mathcal P_L=\{p=(n;i,j):i<j,\ n,n+e_i,n+e_j,n+e_i+e_j\in V_L\}.
\]
On the product of one \(SU(2)\) per original edge, with product Haar probability measure, keep
\[
 \begin{split}
 W_{(n;i,j)}
 &=\operatorname{Tr}\!\left[
 U_i(n)U_j(n+e_i)U_i(n+e_j)^{-1}U_j(n)^{-1}\right],\\
 T_\alpha&=-i\sigma_\alpha/2,\qquad
 X_{e,\alpha}f=\left.\frac d{dt}f(\ldots,e^{tT_\alpha}U_e,\ldots)\right|_{t=0},\\
 K&=-\sum_{e,\alpha}X_{e,\alpha}^2,\qquad
 \Gamma(f,h)=\sum_{e,\alpha}(X_{e,\alpha}f)(X_{e,\alpha}h).
 \end{split}\tag{Q1}
\]
The physical subspace is invariant under every original vertex gauge transformation, including boundary vertices. Let \(P_H f=\int f\,dU\), \(Q_H=I-P_H\). The full scalar and physical parameters are
\[
 H(x)=\kappa K+\kappa\sum_{p\in\mathcal P_L}x_p(2-W_p),\qquad
 \kappa=2g^2/a,\qquad x_p=\xi=1/(4g^4)
 \tag{Q2}
\]
on the physical homogeneous line. The independent \(x_p\) are coordinates on this same finite-dimensional source family.

The original zero-Haar-mean bilinear map is
\[
 \mathcal B(f,h)_A
 =K^{-1}Q_H\!\!\sum_{A_1\cup A_2=A}\Gamma(f_{A_1},h_{A_2}).
 \tag{Q3}
\]
Here \(A,A_1,A_2\) are original edge labels. A representation component with spin support contained strictly in its edge label keeps the larger label. In particular, projecting a function onto a face trace does not reduce its source label. Assembly sums the components representing the same function. Its kernel is retained until the original assembly quotient is taken.

The ordinary multivariate source coefficients are defined without factorials:
\[
 \begin{split}
 v(x)&=\sum_{\nu\ne0}v_\nu x^\nu,\qquad
 v_{\mathbf e_p}=W_p/3,\\
 v_\nu&=\sum_{\substack{\mu+\eta=\nu\\
                 \mu,\eta\in\mathbb N_0^{\mathcal P_L}\setminus\{0\}}}
                  \mathcal B(v_\mu,v_\eta),\\
 V_n(x)&=\sum_{|\nu|=n}v_\nu x^\nu,\qquad
 v_n=V_n(\mathbf1),\qquad q_5(x)=\sum_{n=1}^5V_n(x).
 \end{split}\tag{Q4}
\]
Both subindices are nonzero and may have zero components; both orders of a nonidentical split occur. Every coefficient has its original union-of-face-edges label. The recurrence is the zero-Haar-mean part of the exact logarithmic ground-state equation. It is also an unambiguous finite algebraic definition at every order.

The Haar face projection and its unchanged complement are
\[
 Pf=\sum_{p\in\mathcal P_L}W_p\langle W_p,f\rangle_H,\qquad R=I-P
 \tag{Q5}
\]
on the original physical zero-mean space. Distinct face traces are orthogonal: a link belonging to one face but not the other has an odd fundamental factor, and its Haar integral is zero. Also \(\int W_p^2=1\), by integrating the face holonomy and fundamental-character orthogonality. Thus (Q5) is the original orthogonal face projection. On the labelled coefficient space it acts on the function component and keeps the label.

Write
\[
 J_i=2\mathcal B(v_i,\cdot),\quad
 \mathcal J_5(\xi)=\sum_{i=1}^5\xi^iJ_i,\quad
 L_5(\xi)=I-\mathcal J_5(\xi).
\]
The original Schur map is exactly
\[
 \mathscr S_5(\xi)
 =P-P\mathcal J_5P
 -P\mathcal J_5R(R-R\mathcal J_5R)^{-1}R\mathcal J_5P .
 \tag{Q6}
\]
All identity operators on the complementary space in this formula mean \(R\).

Expanding only by total degree, the fourth coefficient is the sum of all eight original words:
\[
 \begin{split}
 S_{[4]}={}&-PJ_4P\\
 &-PJ_1RJ_3P-PJ_3RJ_1P-PJ_2RJ_2P\\
 &-PJ_1RJ_1RJ_2P-PJ_1RJ_2RJ_1P-PJ_2RJ_1RJ_1P\\
 &-PJ_1RJ_1RJ_1RJ_1P.
 \end{split}\tag{Q7}
\]
No intermediate \(R\), \(K^{-1}Q_H\), factor 2, or occurrence of an original \(J_i\) in (Q7) will be removed.

## Q2. The exact derivative map that evaluates all eight returns

For completeness, the original parity is immediate from
\[
 z_i(n)=(-1)^{\sum_{k<i}n_k},\qquad Tf(U)=f(zU).
\]
Each \(i,j\) face contains exactly one sign change from the lower to the upper \(i\)-coordinate in \(z_j\), while the two \(z_i\) signs agree. Thus \(TW_p=-W_p\). Central multiplication commutes with every \(X_{e,\alpha}\), the gauge transformations, \(K,Q_H\), and the original support labels. Hence \(Tv_n=(-1)^nv_n\), \(TJ_iT=(-1)^iJ_i\), \(TP=PT=-P\), and \(TR=RT\). Every face-return word of odd total degree is zero, including before assembly. Both \(\mathscr S_5\) and
\[
 G_5(\xi):=PL_5(\xi)^{-1}P
 \tag{Q8}
\]
therefore have only even powers wherever the inverse exists, or as formal series at zero.

Define the exact multivariate residual
\[
 \mathcal R_5(x)=\tfrac13\sum_p x_pW_p+\mathcal B(q_5(x),q_5(x))-q_5(x).
 \tag{Q9}
\]
By (Q4) its degrees are precisely among 6 through 10. Differentiation, with the original factor 2 from symmetry of \(\mathcal B\), gives
\[
 \bigl[I-2\mathcal B(q_5(x),\cdot)\bigr]\partial_{x_q}q_5(x)
 =W_q/3-\partial_{x_q}\mathcal R_5(x).
 \tag{Q10}
\]
Consequently, on setting every \(x_p=\xi\),
\[
 G_5(\xi)W_q
 =3P\partial_{x_q}q_5(\xi\mathbf1)
  +3PL_5(\xi)^{-1}\partial_{x_q}\mathcal R_5(\xi\mathbf1).
 \tag{Q11}
\]
The last summand starts at degree five. Its odd face coefficients vanish because the left side and the displayed derivative polynomial are even. In particular,
\[
 [\xi^4]G_5\,W_q=3P\partial_{x_q}V_5(\mathbf1).
 \tag{Q12}
\]
Equation (Q11), including its residual, is the exact connecting map, not an identification of different polynomial references.

This identity also holds for every enlarged input label \(A_0\supseteq\partial q\). To see this without discarding labels, expand either derivative of each recurrence term or the successive \(J_i\)'s as rooted binary trees. Differentiation marks one leaf carrying \(W_q/3\); its integer multiplicity is the number of possible marked occurrences. At each vertex the original operation is (Q3), so the resulting label is \(A_0\) united with the original face-edge labels of all other leaves. Keeping the differentiated coefficient's full source label gives exactly the same union, because \(A_0\) already contains \(\partial q\). This tree bijection proves (Q10)–(Q12) on the labelled space. It also proves descent through assembly: an assembled zero input remains zero under \(K^{-1}Q_H\Gamma(f,\cdot)\), its projections, and their convergent or formal compositions.

We recall the complete second return so that the inverse correction below retains its original sign. Set \(D_p=W_p^2-1=\chi_1(U_p)\). Then
\[
 KD_p=8D_p,\quad \Gamma(W_p,W_p)=3-D_p,\quad
 J_1W_p=-D_p/12+\sum_{q\sim p}(C_{0,pq}/9-C_{1,pq}/39),
 \tag{Q13}
\]
where, for adjacent faces,
\[
 KC_0=\tfrac92C_0,\quad KC_1=\tfrac{13}2C_1,\quad
 \|C_0\|_H^2=\tfrac14,\quad\|C_1\|_H^2=\tfrac34,\quad
 C_0+C_1=W_pW_q.
 \tag{Q14}
\]
Indeed write the two face words at the common edge as \(\operatorname{Tr}(UA)\), \(\operatorname{Tr}(U^{-1}B)\). Haar projection at that edge is \(C_0=\operatorname{Tr}(AB)/2\); the remaining six fundamental edges contribute \(9/2\), and shared-edge spin one adds 2. Independent Haar integration gives the two stated norms. The Pauli identities in (Q21) below give all coefficients in (Q13).

For a Casimir-\(c\) component \(h_c\), integration by parts in the original product rule gives
\[
 PJ_1h_c=(c/9)P\Bigl(\sum_rW_r\Bigr)h_c.
\]
The only surviving face pair for \(C_0,C_1\) is its original pair: otherwise the difference of at most four faces would be a nonempty mod-two two-cycle, impossible since each edge of one included face requires a distinct further face. For \(D_p\), only \(W_p^2D_p\) contributes. Thus
\[
 PJ_1D_p=8W_p/9,\quad
 PJ_1C_0=(W_p+W_q)/8,\quad
 PJ_1C_1=13(W_p+W_q)/24.
\]
The two adjacent returns are \(1/72\) and \(-1/72\) with the same union label and cancel. The self return is \(-2W_p/27\). Similarly the exact
\[
 v_2=-\sum_pD_p/72+
       \sum_{\{p,q\}:p\sim q}(C_{0,pq}/27-C_{1,pq}/117)
\]
has \(PJ_2P=-P/27\): its adjacent contributions are again \(1/72-1/72\), while its self contribution is \(-1/27\). We have proved
\[
 PJ_1P=0,\quad PJ_1RJ_1P=-2P/27,\quad PJ_2P=-P/27,\quad
 G_{[2]}=-P/9,\quad S_{[2]}=P/9.
 \tag{Q15}
\]

The block inverse identity gives \(\mathscr S_5^{-1}=G_5\). Formally it follows by multiplying the two-by-two block factorization of \(L_5\); analytically all inverses used here are proved on the explicit disk in Q8 below. Comparing the degree-four coefficient in \(\mathscr S_5G_5=P\), and retaining \(G_{[2]}^2=P/81\), gives the central evaluation rule
\[
 \boxed{S_{[4]}W_q=\frac1{81}W_q-3P\partial_{x_q}V_5(\mathbf1).}
 \tag{Q16}
\]
It is exactly the sum (Q7). More explicitly, expand \(G_{[4]}\) into all compositions of 4 with unrestricted internal identities, and insert \(I=P+R\) at each such identity. Terms with an internal face return split into even positive degrees. The only degree-four split is \(2+2\); its sum is \(G_{[2]}^2\). All remaining terms have only \(R\)'s internally and are the negatives of (Q7). This proves the equality word by word after this finite expansion and preserves every support union. The term \(P/81\) is at the original input label \(A_0\), as both surviving quadratic self returns are.

## Q3. Complete list of possible fifth face projections

The independent central substitution \(U_e\mapsto -U_e\) at any one original edge commutes with \(K,Q_H\) and differentiations. Therefore \(v_\nu\) has at that edge the parity of the number of occurrences in its source faces. A nonzero \(\langle W_p,v_\nu\rangle_H\) requires
\[
 \partial\!\left(\sum_r(\nu_r\bmod2)r+p\right)=0
 \quad\text{as a finite cubical two-chain over }\mathbf F_2.
 \tag{Q17}
\]
This condition applies to each coefficient before assembly.

Here is the required finite cubical fact, including its filling. For a finite two-cycle, define the coefficient of a cube in a vertical column to be the sum modulo two of the horizontal face coefficients above it in that column. Differences of successive cube coefficients reproduce the horizontal faces. The two-cycle equation on each horizontal edge says that the corresponding differences between neighbouring columns reproduce the specified vertical faces; their differences have zero vertical difference and finite support, so are zero. Below all nonzero horizontal faces the column sums are independent of the horizontal column, again by the cycle equations. Outside the finite support they vanish, so all these lower sums vanish. The constructed three-chain is finite and its boundary is the given cycle.

A nonempty finite set of cubes has at least two boundary faces in each occupied column in each of the three coordinate directions. If it contains at least two distinct cubes, their projections differ on at least two of the three coordinate planes. The numbers of occupied columns in those directions are therefore at least \(2,2,1\), and the boundary has at least ten faces. It follows that a nonempty finite two-cycle of at most six faces is exactly the boundary of one cube. This proof remains valid for a cycle contained in the original box: the filling is the original union of contained cubes, and the single-cube conclusion in particular has all its six faces contained.

For \(|\nu|=5\), (Q17) has at most six distinct faces. If its chain is zero, the odd-multiplicity face set is exactly \(\{p\}\), leaving the possibilities
\[
 p^5,\qquad p^3q^2,\qquad pq^4,\qquad pq^2r^2.
 \tag{Q18}
\]
If it is a cube boundary, it has exactly six faces. Thus \(p\) is absent from the five distinct source faces, which are the other five faces of that cube. There is no additional case with multiplicities or fewer distinct faces.

A source multiset whose edge-sharing graph is disconnected has zero coefficient. This follows by induction in (Q4): a nonzero proper coefficient lies in one connected component; any split crossing two components has disjoint derivative supports and zero \(\Gamma\). Hence in (Q18), two distinct faces must be adjacent, and the distinct triple must be connected. A connected graph on three faces is either a path, or a triangle. A triangle consists either of three faces sharing one edge, or three faces meeting at a corner with different pairwise shared edges. This is exhaustive: fix one face; each of the other two shares an edge with it. If these edges are opposite, the other two cannot share an edge. If they coincide, all three share it. If they are consecutive and the other two also share an edge, they meet along the line perpendicular to the fixed face through their common vertex.

For a connected triple \(T=\{p,q,r\}\), with \(p\) the marked output, define
\[
 \eta_{p,T}=
 \begin{cases}
 h_c,&T\text{ is a path and }p\text{ its central vertex},\\
 h_e,&T\text{ is a path and }p\text{ an endpoint},\\
 h_m,&T\text{ has a common edge},\\
 h_k,&T\text{ is a corner triangle}.
 \end{cases}\tag{Q19}
\]
Graph vertices in this definition are original faces; adjacency means sharing an original edge.

## Q4. Exact evaluation of all fifth face coefficients

The full projected polynomial, with each monomial's original union label retained, is
\[
 \begin{split}
 PV_5(x)={}&u\sum_p x_p^5W_p\\
 &+\sum_{\{p,q\}:p\sim q}
 \left[
 b(x_p^3x_q^2W_p+x_q^3x_p^2W_q)
 +c(x_px_q^4W_p+x_qx_p^4W_q)\right]\\
 &+\sum_{\substack{T\subset\mathcal P_L\\|T|=3,\ T\ {\rm connected}}}
       \sum_{p\in T}\eta_{p,T}x_p
                     \prod_{r\in T\setminus\{p\}}x_r^2\,W_p\\
 &+d\sum_{\text{contained cubes }C}\sum_{p\in\partial C}
                       \prod_{r\in\partial C\setminus\{p\}}x_r\,W_p .
 \end{split}\tag{Q20}
\]
All pair and triple sums displayed as sets are unordered. The exact values are
\[
 \boxed{
 \begin{gathered}
 u=\frac7{3888},\quad b=-\frac{301}{2956824},\quad
 c=-\frac{55}{3639168},\\
 h_c=\frac{19}{3032640},\quad h_e=\frac{19}{59136480},\quad
 h_m=-\frac4{616005},\quad h_k=\frac{164}{6283251},\quad
 d=\frac{107}{34992}.
 \end{gathered}}
\]

We give the complete finite derivation of the table rather than assign it the status of an uncomputed source estimate. The original Pauli matrices give
\[
 \sum_\alpha\operatorname{Tr}(T_\alpha A)\operatorname{Tr}(T_\alpha B)
 =-\tfrac12\operatorname{Tr}(AB)+\tfrac14\operatorname{Tr}(A)\operatorname{Tr}(B),
\]
\[
 \sum_\alpha T_\alpha A T_\alpha=-\tfrac12\operatorname{Tr}(A)I+\tfrac14A,
 \qquad-\sum_\alpha T_\alpha^2=\tfrac34I .
 \tag{Q21}
\]
For every occurrence of a positive link differentiate as \(T_\alpha U_e\); for an inverse occurrence differentiate as \(-U_e^{-1}T_\alpha\). Apply the product rule to every occurrence, then (Q21). This gives exact \(K\) and \(\Gamma\) of any product of original trace words. The only word identities used are cyclicity of the trace, cancellation of adjacent inverse factors, \(\operatorname{Tr}(U^{-1})=\operatorname{Tr}(U)\) for \(SU(2)\), and
\[
 \operatorname{Tr}(U^n)=\operatorname{Tr}(U)\operatorname{Tr}(U^{n-1})
                         -\operatorname{Tr}(U^{n-2}).
 \tag{Q22}
\]
The last identity follows by multiplying the characteristic equation \(U^2-\operatorname{Tr}(U)U+I=0\) by \(U^{n-2}\). None changes the original union label.

To implement the exact inverse in every lower-order recurrence, if \(r_e\) is the original occurrence count at edge \(e\), its possible spins are \(r_e/2,r_e/2-1,\ldots,(r_e\bmod2)/2\). At each original vertex, retain all assignments with even sum of doubled spins and \(2\max j_e\le\sum j_e\). Every invariant tensor satisfies these tests, so the resulting finite set \(\mathcal C\) of \(c=\sum_e j_e(j_e+1)\) contains every actual Casimir in this coefficient. Define
\[
 q_{\mathcal C}(t)=\prod_{\substack{c\in\mathcal C\\c>0}}(1-t/c),\qquad
 f_{\mathcal C}(t)=\frac{1-q_{\mathcal C}(t)}t
                  -q_{\mathcal C}(t)\sum_{\substack{c\in\mathcal C\\c>0}}\frac1c .
 \tag{Q23}
\]
The first quotient is a polynomial. At zero its first term is \(\sum1/c\), cancelled by its second term; at each positive \(c\in\mathcal C\) it is \(1/c\). Thus \(f_{\mathcal C}(K)=K^{-1}Q_H\) on the entire coefficient, including its constant component. The zero-Casimir functions are constants because their nonnegative electric Dirichlet integral is zero. No spin truncation of the full Hamiltonian has occurred.

Haar integration is equally finite and exact. At an edge with \(r\) fundamental occurrences, odd \(r\) has zero integral by its center sign. For even \(r\), the exact projection onto edge spin zero is
\[
 \prod_{j=1}^{r/2}\left(1-\frac{E_e}{j(j+1)}\right),
 \qquad E_e=-\sum_\alpha X_{e,\alpha}^2.
 \tag{Q24}
\]
After this projection the function is constant in that edge and its value is obtained by setting \(U_e=I\). Repeating over all original edges proves the Haar routine. If a polynomial has terms with different occurrence numbers, apply (Q24) separately to each occurrence group and sum; all operations are linear. These formulas prove termination and exactness of the rational certificate procedure.

In particular, set
\[
 A_{14}(\nu,p)=\sum_{\substack{\mu\le\nu\\|\mu|=1}}
          \int W_p\,\Gamma(v_\mu,v_{\nu-\mu})\,dU,\quad
 A_{23}(\nu,p)=\sum_{\substack{\mu\le\nu\\|\mu|=2}}
          \int W_p\,\Gamma(v_\mu,v_{\nu-\mu})\,dU.
\]
Self-adjointness of \(K^{-1}Q_H\), \(KW_p=3W_p\), and both orders in (Q4) give the complete formula
\[
 \langle W_p,v_\nu\rangle_H=\frac23(A_{14}(\nu,p)+A_{23}(\nu,p)).
 \tag{Q25}
\]
The finite evaluations of these two separate original sums are:

| Source monomial and marked output | \(A_{14}\) | \(A_{23}\) | \((2/3)(A_{14}+A_{23})\) |
|---|---:|---:|---:|
| \(p^5\), output \(p\) | \(17/7776\) | \(1/1944\) | \(7/3888\) |
| \(p^3q^2\), output \(p\) | \(139/23654592\) | \(-3751/23654592\) | \(-301/2956824\) |
| \(pq^4\), output \(p\) | \(-55/1819584\) | \(55/7278336\) | \(-55/3639168\) |
| \(pq^2r^2\), path center \(p\) | \(19/2021760\) | \(0\) | \(19/3032640\) |
| \(pq^2r^2\), path endpoint \(p\) | \(-2021/157697280\) | \(233/17521920\) | \(19/59136480\) |
| \(pq^2r^2\), common edge | \(2/41067\) | \(-4/68445\) | \(-4/616005\) |
| \(pq^2r^2\), corner | \(-10/123201\) | \(28/232713\) | \(164/6283251\) |
| Five cube faces, output missing \(p\) | \(43/11664\) | \(7/7776\) | \(107/34992\) |

Every table entry is obtained from (Q21)–(Q25) and only the original degree-one to degree-four recurrence. The complete list of \(\mu,\nu-\mu\), original oriented words, edge endpoints, output faces and individual rational integrals is retained in PROJECTED_RHS_REDERIVATION.json and FIFTH_FACE_PROJECTIONS.json. The replay script rederive_projected_rhs.py uses the byte-identical original differential and source routines in verification_sources. Thus these files constitute a finite rational certificate with the proof of its operations given above; no external fifth coefficient is required to reproduce the right-hand sums.

Completeness of its geometries is also checked independently of the incoming 662-row catalogue. Fix the output face \(p=(0,0,0;0,1)\) in the infinite coordinate lattice. There are 12 adjacent faces. Enumerate all connected distinct triples containing \(p\) by taking \(q\sim p\) and \(r\sim p\) or \(r\sim q\); this reaches every such triple since a connected graph on three vertices has a spanning path starting at, or passing through, \(p\). Removing duplicates gives 158 marked triples. Together with the self case, the 24 pair cases and the two five-face cube cases, there are exactly 185 candidate source multisets. Enumerating the 48 signed coordinate permutations and a translation maps these to the 25 stored representatives: one self, four pairs, nineteen marked triples, one cube. GEOMETRY_COVERAGE_CHECKS.json records every concrete multiset and its explicit signed-permutation/translation witness. Each transformed face is computed from its four actual vertices, with lower corner and the two varying axes; no implicit drawing convention is used.

These coordinate maps permute original links and sometimes reverse a link orientation. Inversion of an \(SU(2)\) variable preserves Haar measure; it carries a left derivative to a right derivative with a minus sign and an adjoint rotation of the three generators. The adjoint rotation is orthogonal, so the contracted sums defining \(K\) and \(\Gamma\) are preserved, including the two minus signs in \(\Gamma\). Gauge actions are intertwined by the vertex permutation. A reversed full face word has unchanged \(SU(2)\) trace. Thus the coordinate maps preserve (Q3)–(Q4), every rational coefficient, and all original support unions. They prove that the table covers the actual box by using only configurations whose original faces are contained; no exterior faces are added at a boundary.

The cube value has an additional independent calculation in [CUBE_FIFTH_PROJECTION.md](cube_derivation/CUBE_FIFTH_PROJECTION.md), C9, C15–C16 and C18–C20. The original spin-zero projections on its eight twice-occurring edges give coefficient \(107/2187\); the remaining four edges have spin \(1/2\). The projected product of five oriented face traces is \(W_p/16\), proved by four exact fundamental Haar integrations after an explicit vertex gauge transformation. Hence \((107/2187)(1/16)=107/34992\). Its full twelve-edge union label is preserved. The independent subset recurrence and exact Haar cubature certificates accompany that proof.

## Q5. Evaluation on the actual finite box

Let \(d_p=\#\{q\in\mathcal P_L:q\sim p\}\), let \(A_{\rm adj}\) be the actual adjacency matrix, and let \(D_{\rm deg}=\operatorname{diag}(d_p)\). For two distinct faces put
\[
 c_{pq}=\#\{C:\ C\text{ is an original contained cube and }p,q\in\partial C\}.
 \tag{Q26}
\]
All triple sums below range only over contained connected distinct triples.

Differentiate (Q20), retaining the multiplicity of the differentiated source:
\[
 \begin{split}
 G_{[4],pp}&=15u+(9b+3c)d_p+3\sum_{T\ni p}\eta_{p,T},\\
 G_{[4],pq}&=(6b+12c)\mathbf1_{p\sim q}
                 +6\sum_{T\supset\{p,q\}}\eta_{p,T}
                 +3d\,c_{pq}\quad(p\ne q).
 \end{split}\tag{Q27}
\]
For example, the \(b\) monomial giving output \(W_p\) differentiates with factors 3 in column \(p\) and 2 in column \(q\); the \(c\) monomial differentiates with factors 1 and 4. The triple factors are 1 and 2. The cube monomial contains no \(x_p\), so its diagonal derivative is zero, and every other cube-face column has factor 1. The common factor 3 is the exact derivative map (Q12).

Equations (Q16) and (Q27) are the full evaluation of (Q7):
\[
 \boxed{\begin{split}
 S_{[4],pp}
 &=\frac1{81}-15u-(9b+3c)d_p-3\sum_{T\ni p}\eta_{p,T}\\
 &=-\frac{19}{1296}+\frac{15163}{15769728}\,d_p
                          -3\sum_{T\ni p}\eta_{p,T},\\
 S_{[4],pq}
 &=-(6b+12c)\mathbf1_{p\sim q}
                -6\sum_{T\supset\{p,q\}}\eta_{p,T}
                -3d\,c_{pq}\\
 &=\frac{347}{438048}\mathbf1_{p\sim q}
                -6\sum_{T\supset\{p,q\}}\eta_{p,T}
                -\frac{107}{11664}\,c_{pq}\qquad(p\ne q).
 \end{split}}\tag{Q28}
\]
The first expressions retain each original source contribution; the second expressions evaluate their rational sums. They describe the same original map, without a changed reference or boundary completion.

Before assembly, read (Q28) as a sum of labelled maps. The self term carries the input label \(A_0\). A pair term with source faces \(p,q\) carries \(A_0\cup\partial p\cup\partial q\). A triple term carries \(A_0\cup\bigcup_{r\in T}\partial r\). A cube term carries \(A_0\) united with all twelve edges of that cube, since the five source faces already cover them. Distinct geometric occurrences remain distinct labelled contributions even if their projected functions coincide. Formula (Q28) is the assembled matrix; the preceding rules specify the entire original labelled coefficient and hence its quotient.

As a bounded direct check of the original complement, DIRECT_RETURN_WORD_CHECKS.json evaluates each of the eight expressions in (Q7) separately for one face, for two adjacent coplanar faces, and for two adjacent perpendicular faces, with all other independent sources zero. It projects out every intermediate face component to apply \(R\), and uses the full finite Casimir polynomial for each \(K^{-1}Q_H\). The self case sums to \(-19/1296\); both pair cases sum to
\[
 \begin{pmatrix}
 -216029/15769728&347/438048\\
 347/438048&-216029/15769728
 \end{pmatrix}.
 \tag{Q29}
\]
In these two-face supports no other elementary face can occur: their unions contain only seven original edges and the only four-edge face boundaries in those unions are the two original ones. Thus the intermediate face projection in these direct checks is the full original \(P\) on that support. These checks supplement the all-geometries proof (Q10)–(Q28).

## Q6. The exact boundary defect and a longer-range entry

The fourth coefficient is generally not symmetric in the original Haar face basis. Its complete antisymmetric part is
\[
 \boxed{
 S_{[4]}-S_{[4]}^{\,t}
 =-\frac{703}{19712160}
       (D_{\rm deg}A_{\rm adj}-A_{\rm adj}D_{\rm deg}).}
 \tag{Q30}
\]
To prove it, diagonal entries, pair terms and cube terms in (Q28) are symmetric. The two triangle types give equal \(\eta\) for every marked face. For nonadjacent \(p,q\) in a path, both are endpoints and also give equal \(\eta\). For adjacent \(p,q\), a path containing them has a third face attached exclusively to \(p\), or exclusively to \(q\). If \(m_{pq}\) is their number of common neighbours, these possibilities number \(d_p-1-m_{pq}\) and \(d_q-1-m_{pq}\), respectively. Hence their difference is \(d_p-d_q\), with
\[
 -6(h_c-h_e)
 =-6\left(\frac{19}{3032640}-\frac{19}{59136480}\right)
 =-\frac{703}{19712160}.
\]
This proves (Q30) with all finite-boundary degrees. The matrix transpose uses the actual Haar-orthonormal basis in (Q5).

For example in the actual \(L=2\) box,
\[
 p=(-2,-2,-2;0,1),\qquad q=(-1,-2,-2;1,2)
\]
are adjacent with \(d_p=6,d_q=10\), and
\[
 S_{[4],pq}=-\frac{976543}{111702240},\qquad
 S_{[4],qp}=-\frac{2977433}{335106720},\qquad
 S_{[4],pq}-S_{[4],qp}=\frac{703}{4928040}.
 \tag{Q31}
\]
These are exact entries of the complete finite-box matrix. The defect disappears for pairs of equal degree, in particular for the coefficientwise bulk matrix; this observation does not discard it from the original boundary.

There is also a nonzero return between the opposite original cube faces
\[
 p=(0,0,0;0,1),\qquad q=(0,0,1;0,1).
\]
They are nonadjacent. Their connected triples are the four side-face paths, each marking an endpoint, and they belong to one common cube. Therefore
\[
 S_{[4],pq}
 =-24h_e-3d
 =-\frac{19}{2464020}-\frac{107}{11664}
 =-\frac{90491}{9856080}.
 \tag{Q32}
\]
There are no further degree-four sources for this pair by Q3.

## Q7. A uniform Haar bound for this exact coefficient

At a bulk face there are 12 neighbours: each of its four edges lies in three other faces, and distinct faces share at most one edge. There are 12 common-edge triangles containing it, namely four choices of the common edge and three choices of two of the remaining three incident faces. There are eight corner triangles, two choices of side for the perpendicular direction at each of four vertices. These account for the 20 adjacent pairs among the 12 neighbours. Hence the number of paths marking their center is
\[
 N_c=\binom{12}{2}-12-8=46.
\]
For paths marking an endpoint, sum the 11 further neighbours of each of the 12 possible central faces and remove the two counts from each of those 20 triangles:
\[
 N_e=12\cdot11-2(12+8)=92.
 \tag{Q33}
\]
These arguments also prove the 158 total marked triples used in Q4. A fixed face belongs to two cubes, each contributing five other faces.

Put \(s=-19/1296\), \(a=15163/15769728\), \(b_0=347/438048\). Taking absolute values of each separate contribution in (Q28), the absolute row sum is at most
\[
 \begin{split}
 B_4={}&|s|+12(|a|+|b_0|)\\
 &+15\left(46|h_c|+92|h_e|+12|h_m|+8|h_k|\right)+30d\\
 ={}&\frac{4574447}{33510672}.
 \end{split}\tag{Q34}
\]
A triple with marked output \(p\) contributes a diagonal \(3|\eta_{p,T}|\) and two off-diagonal contributions \(6|\eta_{p,T}|\), giving its factor 15. A boundary removes actual configurations from the infinite-coordinate list, so this upper bound also covers every original finite box.

The column bound must be proved separately because (Q30) is nonzero. For a path with the input at its central face, its complete absolute column contribution is \(3h_c+12h_e\). For a path with the input at an endpoint, it is \(9h_e+6h_c\). The two triangle types contribute \(15|h_m|\) and \(15|h_k|\); pair and cube bounds are the same as for rows. Since \(N_e=2N_c\),
\[
 46(3h_c+12h_e)+92(9h_e+6h_c)
 =15(46h_c+92h_e).
\]
Thus every absolute column sum is at most the same \(B_4\). For a coefficient vector \(z\), Cauchy–Schwarz with weights \(|S_{pq}|\) gives
\[
 \sum_p\left|\sum_qS_{pq}z_q\right|^2
 \le\left(\sup_p\sum_q|S_{pq}|\right)
     \left(\sup_q\sum_p|S_{pq}|\right)\sum_q|z_q|^2.
\]
The exact Haar face norm in (Q5) is the unaltered Euclidean coefficient norm, so
\[
 \boxed{\|S_{[4]}\|_{H\to H}\le B_4
 =\frac{4574447}{33510672}<0.137.}\tag{Q35}
\]
This bound concerns this coefficient after assembly. It is not substituted for the different labelled local norm of the full Schur tail.

## Q8. Analytic domain and the complete remainder from degree six

For clarity the original local norm is the supremum over original anchor edges \(e\) of
\[
 \sum_{A\ni e}\sum_{j\ne0}c_j\|A_{A,j}\|_1,\qquad
 c_j=\sum_fj_f(j_f+1);
\]
the physical zero-Haar-mean labelled space and its assembly quotient carry that norm and its quotient norm. The original \(P,R\) are contractions there. The full G13 estimate and original source bounds give
\[
 \|J_i\|\le a_i,\quad
 (a_1,a_2,a_3,a_4,a_5)=
 \left(\frac{128}{3},\frac{3132}{13},\frac{292337810}{125307},
 \frac{169232115504453213210913}{2253180919843854000},2399196\right).
 \tag{Q36}
\]
These are \(a_i=m_i+4t_i\), with every original factor kept; their derivation and all \(m_i,t_i\) are retained in P12–P19 of the adjacent proof.

Let \(\ell(x)=\sum_{i=1}^5a_ix^i\), and let \(\beta\) be its unique positive root at value 1. Positivity of all coefficients proves uniqueness, and \(\beta\approx0.020200392941788888\) is only a display value. For \(|\xi|<\beta\) both \(I-\mathcal J_5\) and the full original complementary block are invertible by norm-convergent Neumann series, with bound
\[
 \|(I-\mathcal J_5)^{-1}\|,\ {}
 \|(R-R\mathcal J_5R)^{-1}\|
 \le\frac1{1-\ell(|\xi|)} .
 \tag{Q37}
\]
The series converge uniformly on compact subdisks, proving the holomorphic block inverse and the analytic use of (Q11), (Q16). No endpoint inverse is asserted.

Set
\[
 e(x)=a_2x^2+a_4x^4,\qquad
 o(x)=a_1x+a_3x^3+a_5x^5.
\]
Every degree-\(n\) return word in (Q6) has norm at most the product of its \(a_i\)'s. Summing all compositions gives the majorant \(\ell/(1-\ell)\). Its even part is exactly
\[
 h_{\rm even}(x)=\frac{e-e^2+o^2}{(1-e)^2-o^2}.
 \tag{Q38}
\]
Its coefficients are nonnegative. Its degree-two and degree-four coefficients, retaining all compositions, are
\[
 \begin{split}
 h_2&=a_2+a_1^2=\frac{241180}{117},\\
 h_4&=a_4+2a_1a_3+a_2^2+3a_1^2a_2+a_1^4\\
 &=\frac{1242256641762604168589657}{250353435538206000}.
 \end{split}\tag{Q39}
\]
Since all odd returns vanish, the complete remaining operator, not just a polynomial truncation error, satisfies
\[
 \boxed{\begin{gathered}
 \mathscr S_5(\xi)=(1+\xi^2/9)P+\xi^4S_{[4]}+\mathscr E_{\ge6}(\xi),\\
 \|\mathscr E_{\ge6}(\xi)\|_{\rm loc}
 \le E_6(|\xi|):=
 h_{\rm even}(|\xi|)-h_2|\xi|^2-h_4|\xi|^4,
 \qquad |\xi|<\beta .
 \end{gathered}}\tag{Q40}
\]
The same statement holds on the original assembly quotient. Subtracting \(h_4x^4\) here subtracts the degree-four majorant coefficient from its nonnegative coefficient series; it does not replace the exact operator (Q28) by that bound. Exact rational checks give
\[
 E_6(1/100)<17/1000,\qquad E_6(1/64)<9/20.
 \tag{Q41}
\]
The evaluated fractions are retained in SIXTH_TAIL_CHECKS.json. Their approximate values are \(0.01615808438\) and \(0.44189205795\); the inequalities themselves use rational arithmetic.

## Q9. The exact map to the physical susceptibility

The nonsymmetry (Q30) has a precise relation to the original physical response. Keep the actual normalized vacuum
\[
 \psi_x=e^{v(x)+c(x)},\qquad
 c(x)=-\tfrac12\log\int e^{2v(x)}dU,\qquad \rho_x=\psi_x^2.
 \tag{Q42}
\]
For real sources in the analytic neighbourhood let \(z_q=\partial_{x_q}v\) and \(Z_q=z_q-\int\rho_xz_q\,dU\). Differentiating the normalization gives \(\partial_{x_q}\psi_x=\psi_xZ_q\). The original ground-state transform is
\[
 \psi_x^{-1}(H(x)-E_0(x))\psi_x
 =\kappa\bigl[K-2\Gamma(v(x),\cdot)\bigr].
 \tag{Q43}
\]
It follows by applying (Q1) to \(e^{v+c}f\) and subtracting the complete original ground-state equation; the scalar \(2\kappa\sum x_p\) in (Q2) remains part of \(E_0\).

Define \(r_p=(W_p-\int\rho_xW_p)\psi_x\), and let the physical inverse below act on the Haar-orthogonal complement of \(\psi_x\). Then
\[
 R^{\rm phys}_{pq}(x)
 :=\kappa\langle r_p,(H(x)-E_0(x))^{-1}r_q\rangle_H
 =\int\rho_x(W_p-\langle W_p\rangle_{\rho_x})z_q\,dU .
 \tag{Q44}
\]
Indeed differentiation of the exact eigen-equation, whose source derivative is \(\kappa(2-W_q)\), gives
\[
 (H-E_0)(\psi_xZ_q)=\kappa r_q,\qquad
 \partial_{x_q}E_0=\kappa(2-\langle W_q\rangle_{\rho_x}),
\]
proving (Q44) with the stated \(\kappa\). This also proves symmetry and positive semidefiniteness of the real response matrix.

The inverse and derivatives just used exist on every real homogeneous \(|\xi|<\alpha\), where the original full-source disk has
\(\alpha\approx0.018424953576117616681\). Here is the needed justification of source differentiation. P45 proves the actual full Jacobian bound
\[
 \|J(\xi)\|\le1-\sqrt{\mathscr D(|\xi|)}<1,\quad
 J=2\mathcal B(v,\cdot),\quad
 \mathscr D(x)=[1-\ell(x)]^2-\tfrac83\delta(x)>0
\]
on that interior, with the full original residual majorant \(\delta\). For each fixed finite box the original source perturbation \(\frac13\sum h_pW_p\) is a bounded map from its finite coordinate space into the labelled source space. The analytic implicit function theorem, or its convergent local contraction proof using this strict Jacobian bound, therefore gives the independent source derivatives near that homogeneous point. The reconstructed positive normalized ground state is the original one. Its simple ground eigenvalue on the compact connected product group is isolated; elliptic positivity and uniqueness give a positive distance to the next eigenvalue at each fixed real point. Thus the inverse on \(\psi_x^\perp\) in (Q44) exists. These are established interior conclusions, not assumptions about an endpoint.

On the original source space set \(L=I-J\) and define the observation map to the original Haar face space by
\[
 \mathcal O_{\rho}h
 =\sum_p W_p\left(\int\rho W_ph\,dU
                      -\int\rho W_p\,dU\int\rho h\,dU\right).
 \tag{Q45}
\]
All means in (Q45) are kept, including the normalization contribution in (Q42). Differentiating the full recurrence gives \(Lz_q=W_q/3\). With the original face basis and its norm one, (Q44) is therefore the exact operator identity
\[
 \boxed{3R^{\rm phys}=\mathcal O_\rho L^{-1}P.}\tag{Q46}
\]
At \(\xi=0\), \(\rho=1\), \(\mathcal O_\rho=P\), and this gives \(R^{\rm phys}(0)=P/3\).

The fifth Schur inverse has a different observation map. The complete connecting operator, including the higher source correction, is
\[
 \boxed{\begin{split}
 3R^{\rm phys}-G_5
 ={}&(\mathcal O_\rho-P)L_5^{-1}P\\
 &+\mathcal O_\rho L_5^{-1}(J-\mathcal J_5)L^{-1}P,\\
 J-\mathcal J_5={}&2\mathcal B(v-q_5,\cdot).
 \end{split}}\tag{Q47}
\]
This follows by adding and subtracting \(\mathcal O_\rho L_5^{-1}P\) and using the exact resolvent identity
\[
 L^{-1}-L_5^{-1}=L_5^{-1}(J-\mathcal J_5)L^{-1}.
\]
All maps are defined on the original spaces, and assembly is performed before the Haar observations. The identity holds throughout the real interior \(|\xi|<\alpha\); its Taylor-coefficient identity holds near zero. It explicitly relates the boundary defect to the physical pairing without inferring Hermiticity of the original Schur block.

Since \(v-q_5\) starts at degree six, its resolvent contribution in (Q47) starts at degree six. In particular, through degree four the observation change alone accounts for the difference. The original fourth energy is proved in [CUBIC_SOURCE, C7, equations C24–C25](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/33a4c39de32c2c7fdf6f8ce796e40389f766669f/yang-mills/consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260916-cubic-linearized/CUBIC_SOURCE.md#L214); its independent-source polynomial is [PLAQUETTE_RESPONSE, P7](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/33a4c39de32c2c7fdf6f8ce796e40389f766669f/yang-mills/consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260917-fifth-source/PLAQUETTE_RESPONSE.md#L47), and its Hessian is P17 at line 120. Differentiating that full polynomial gives the exact degree-two physical response
\[
 R^{\rm phys}_{[2]}
 =-\tfrac5{36}P+\tfrac2{1053}D_{\rm deg}
                   +\tfrac4{1053}A_{\rm adj}.
\]
Together with \(G_{[2]}=-P/9\), this gives the explicit first difference
\[
 [\xi^2](3R^{\rm phys}-G_5)
 =-\tfrac{11}{36}P+\tfrac2{351}D_{\rm deg}
                         +\tfrac4{351}A_{\rm adj}.
 \tag{Q48}
\]
For the fourth coefficient, the complete exact difference is obtained directly from (Q27) and [SIXTH_ENERGY, E1–E4, especially the complete coefficient table at line 55](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/33a4c39de32c2c7fdf6f8ce796e40389f766669f/yang-mills/consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260917-quartic-cube/SIXTH_ENERGY.md#L55). The full independent-source polynomial and its Hessian are also [PLAQUETTE_RESPONSE, P8–P9 and P18](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/33a4c39de32c2c7fdf6f8ce796e40389f766669f/yang-mills/consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260917-fifth-source/PLAQUETTE_RESPONSE.md#L47). The exact original sixth-energy coefficients are
\[
 a_E=-289/77760,\quad b_E=22285/47309184,\quad
 c_E^{\rm path}=-4909/118272960,\quad
 c_E^{\rm common}=244/4312035,\quad
 c_E^{\rm corner}=-212/542997,\quad d_E=-83/1944.
\]
Writing \(t_p^\tau,t_{pq}^\tau\) for the counts of contained triples of type \(\tau\), it is
\[
 \begin{split}
 [\xi^4](3R^{\rm phys}-G_5)_{pp}
 ={}&-45a_E-15u
       +(-21b_E-9b-3c)d_p\\
 &-3\sum_\tau c_E^\tau t_p^\tau
       -3\sum_{T\ni p}\eta_{p,T},\\
 [\xi^4](3R^{\rm phys}-G_5)_{pq}
 ={}&(-24b_E-6b-12c)\mathbf1_{p\sim q}\\
 &-6\sum_\tau c_E^\tau t_{pq}^\tau
       -6\sum_{T\supset\{p,q\}}\eta_{p,T}
       +(-3d_E/2-3d)c_{pq},\quad p\ne q.
 \end{split}\tag{Q49}
\]
The physical energy coefficients in this last comparison are the previously proved original sixth-energy calculation, whose source and coverage are recorded in the reading ledger; their Hessian map is proved by (Q44) and \(\partial_{x_p}E_0=\kappa(2-\langle W_p\rangle_\rho)\). They are not estimates assumed in the derivation of (Q28). In particular \([\xi^4](3R^{\rm phys}-G_5)-[\xi^4](3R^{\rm phys}-G_5)^t=S_{[4]}-S_{[4]}^t\), exactly the commutator (Q30).

There is a further exact consequence of the degeneracy of the free and quadratic coefficients. There is no family of positive Hermitian metrics \(M(\xi)\) on the original Haar face space tending to \(P\) as real \(\xi\to0\) that makes this original Schur map self-adjoint for every sufficiently small nonzero real \(\xi\). No differentiability of this metric family is needed. Indeed
\[
 \lim_{\xi\to0}\xi^{-4}
 \left[M(\xi)\mathscr S_5(\xi)-\mathscr S_5(\xi)^*M(\xi)\right]
 =S_{[4]}-S_{[4]}^t .
 \tag{Q50}
\]
The scalar terms \((1+\xi^2/9)P\) commute with \(M(\xi)\); divide the remaining terms in (Q40) by \(\xi^4\) and use \(M(\xi)\to P\) and the degree-six remainder to prove the limit. At a fixed finite box the remainder also tends to zero in the matrix norm because each face coefficient is a continuous functional on the original source quotient. The limit is nonzero: in every \(L\ge2\), the adjacent pair \(p=(-L,-L,-L;0,1)\), \(q=(-L+1,-L,-L;1,2)\) has degrees 6 and 10 by direct counting of contained faces at its four edges. Thus (Q30) rules out the asserted self-adjointness. The same argument shows that a similarity tending to \(P\) at zero preserves the first non-scalar coefficient in this limit and cannot make the map Hermitian. The precise object defined by this defect is the nonzero skew matrix \(-703[D_{\rm deg},A_{\rm adj}]/19712160\), supported on adjacent pairs of unequal original degree. The additive observation-and-resolvent map (Q47) is the established connection to the physical response.

## Q10. Reproducibility and scope

The original 662-row fifth catalogue was routed through the existing source index and source-use ledger before this derivation. Its independent link parity leaves exactly 25 rows; all other 637 have no face projection. The 25 retained projections were first obtained by exact Haar integration of the original saved coefficients, then independently rederived from degrees one through four by (Q25). The standalone geometry enumeration reaches all 25 representatives. The byte-identical kernel copies and their hashes let the latter computation run without the private corpus paths. project_fifth.py retains the original-catalogue replay as an optional provenance comparison; rederive_projected_rhs.py, direct_return_words.py, check_geometry_coverage.py, fourth_matrix.py and sixth_tail.py require only the retained local files.

The complete matrices in FOURTH_SCHUR_L2.json and FOURTH_SCHUR_L3.json have respectively 240 and 756 original faces and 9,660 and 35,472 nonzero entries. Every entry obeys (Q30); there are respectively 1,440 and 3,600 nonzero ordered antisymmetric entries. These exhaustive finite checks preserve the actual degree and cube incidence at each boundary. They verify implementation of the all-\(L\) proof, without substituting a finite sample for that proof.

The completed mathematical results are the full labelled coefficient (Q7), evaluated by (Q20), (Q28) and the explicit union-label rule; its exact boundary commutator (Q30); the longer-range coefficient (Q32); the uniform coefficient bound (Q35); the full analytic degree-six remainder (Q40); the physical-response connecting operator (Q47); and the resulting metric obstruction (Q50). The accepted earlier P1–P45 statements are unchanged. No new nonlinear convergence endpoint, full-Haar tail estimate, uniform physical spectral gap or continuum Yang–Mills conclusion is inferred from this coefficient.
