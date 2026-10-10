# The original center-sign involution, all odd Schur coefficients, and a complete even tail

11 October 2026. Independent derivation for the original open three-dimensional box. The Hamiltonian, its scalar, link orientations, all vertex constraints, product-spin blocks and union labels are retained.

The center-change mechanism has a human antecedent: L. Li and Y. Meurice, [*Lattice gluodynamics at negative \(g^2\)*, arXiv:hep-lat/0410029v2](https://arxiv.org/abs/hep-lat/0410029v2), [original author TeX](https://arxiv.org/src/hep-lat/0410029v2), Section IV, source lines 301–353, especially the labelled equations eq:su2id and eq:parity. They prove a negative-coupling identity for the Wilson action on even periodic lattices and perturbative parity consequences. Below the exact map is proved on the programme's open-box Hamiltonian and labelled Jacobian source. No novelty claim is made for the center-sign mechanism.

The original programme inputs have verified pinned sources: [G1–G31, original objects and labelled bilinear bound](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/fa79faff2cd697e16cfa3a7953f36810c22c8922/yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md); [F1–F42, the full fifth reference](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/33a4c39de32c2c7fdf6f8ce796e40389f766669f/yang-mills/consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md), especially F10 at source line 98, F26 at 272 and F31 at 319; and [B13–B16, every original two-face channel](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/fa79faff2cd697e16cfa3a7953f36810c22c8922/yang-mills/continuations/20260915-gauge-native-band/BAND_AND_CERTIFICATE.md#L125). The earlier J1–J7 second-coefficient calculation is reproduced as P27–P30 below. The full [original provider](BASELINE_J5.md), including its outgoing Gram calculation, is also retained.

## P1. Original objects and domains

Let \(L\ge2\) be an integer,
\[
 V_L=\{-L,\ldots,L\}^3,\qquad
 E_L=\{(n,i):n,n+e_i\in V_L,\ 1\le i\le3\}.
\]
The original configuration space is \(SU(2)^{E_L}\) with product Haar probability \(dU\). Every positive edge \(e=(n,i)\) carries \(U_i(n)\). The physical Hilbert space is the invariant part of this Haar \(L^2\) under every vertex gauge transformation, including boundary vertices. The contained faces are \(p=(n;i,j)\), \(i<j\), and
\[
 M=3(2L)^2(2L+1)=12L^2(2L+1).
\]
Keep the original oriented words and generator convention:
\[
 W_p(U)=\operatorname{Tr}\{U_i(n)U_j(n+e_i)
 U_i(n+e_j)^{-1}U_j(n)^{-1}\},\quad S=\sum_pW_p,
\]
\[
 T_a=-i\sigma_a/2,\quad
 X_{e,a}f(U)=\left.\frac{d}{dt}f(\ldots,e^{tT_a}U_e,\ldots)\right|_{t=0},
 \quad K=-\sum_{e,a}X_{e,a}^2,
 \quad\Gamma(f,h)=\sum_{e,a}(X_{e,a}f)(X_{e,a}h).
 \tag{P1}
\]
The original Hamiltonian remains
\[
 H_L(\xi)=\kappa K+\kappa\xi(2M-S),\qquad
 \kappa=2g^2/a,\quad\xi=1/(4g^4),\quad a,g>0. \tag{P2}
\]
For the comparison \(\xi\leftrightarrow-\xi\), fix the actual positive value of \(\kappa\) and extend only the coefficient \(\xi\) to real or complex values. This does not assign negative \(\xi\) to the original positive-\(g\) physical path.

The original operator domain is the physical part of \(H^2(SU(2)^{E_L})\), and the form domain is its physical \(H^1\). The potential is bounded and smooth, so these domains are unchanged for every complex \(\xi\). This is an analytic closed-operator family on a fixed domain; for real \(\xi\) it is self-adjoint with compact resolvent. These are the original domains of F1–F3.

## P2. Explicit involution, gauge constraints and boundaries

For every original positive edge define
\[
 a_i(n)=\sum_{k<i}n_k\in\mathbb Z,\quad
 z_i(n)=(-1)^{a_i(n)}I_2,\quad
 (\tau U)_i(n)=z_i(n)U_i(n),\quad
 (Tf)(U)=f(\tau U). \tag{P3}
\]
Negative integer coordinates have their usual parity. Each \(z_i(n)^2=I_2\), so \(\tau^2=I\). Haar invariance in each edge gives \(T^*=T^{-1}=T\) and \(T1=1\).

For \(i<j\), the four center factors in the original oriented face word are
\[
 z_i(n)z_j(n+e_i)z_i(n+e_j)^{-1}z_j(n)^{-1}.
\]
Since \(a_i(n+e_j)=a_i(n)\) and \(a_j(n+e_i)=a_j(n)+1\), their exponent is
\[
 a_i(n)+[a_j(n)+1]-a_i(n)-a_j(n)=1.
\]
Thus the actual face holonomy acquires \(-I_2\), with its order and inverses unchanged:
\[
 TW_p=-W_p,\qquad TS=-S. \tag{P4}
\]
Only the four contained edges were used, so this proves the statement on every boundary face without adding exterior edges.

For an original vertex gauge transformation \(G=(G_v)\),
\[
 (G\cdot U)_i(n)=G_nU_i(n)G_{n+e_i}^{-1}.
\]
Centrality proves \(\tau(G\cdot U)=G\cdot(\tau U)\) at every edge, including boundary endpoints. Hence \(T\) commutes with the full gauge action and gauge averaging and restricts to a unitary involution on the physical Hilbert space.

The same centrality gives \(z_e e^{tT_a}U_e=e^{tT_a}z_eU_e\), so
\[
 X_{e,a}T=TX_{e,a},\quad KT=TK,\quad
 T\Gamma(f,h)=\Gamma(Tf,Th). \tag{P5}
\]
These identities first hold on smooth functions. The smooth measure-preserving map \(\tau\), and its commutation with every original derivative, preserve \(H^1,H^2\) and extend the domain identities. Haar invariance also gives \(TP_H=P_HT=P_H\), where \(P_Hf=\int f\,dU\). Therefore \(T\) commutes with \(Q_H=I-P_H\), every original \(K\)-spectral projection and \(K^{-1}\) on the nonconstant physical blocks.

## P3. Every support label and the assembly quotient

For the original product-spin label \(j=(j_e)\), keep
\[
 c_j=\sum_ej_e(j_e+1),\quad
 \pi_j(U)=\bigotimes_e\pi_{j_e}(U_e),\quad
 A_j(f)=d_j\int f(U)\pi_j(U)^*\,dU.
\]
Since \(\pi_{j_e}(-I_2)=(-1)^{2j_e}I\),
\[
 \chi(j)=\prod_{e=(n,i)}(-1)^{2j_ea_i(n)}\in\{1,-1\},\quad
 \pi_j(\tau U)=\chi(j)\pi_j(U),\quad
 A_j(Tf)=\chi(j)A_j(f). \tag{P6}
\]
No spin block or active edge is moved.

Write \(\mathscr V_L\) for the completed original physical zero-Haar-mean labelled coefficient space. An entry \(A_{A,j}\) retains its nonempty edge label \(A\supseteq\operatorname{supp}(j)\), including strict containments. Its norm is
\[
 \|f\|_{\rm loc}=\max_{b\in E_L}
 \sum_{A\ni b}\sum_{j\ne0}c_j\|A_{A,j}\|_1. \tag{P7}
\]
Define \(T\) by \(A_{A,j}\mapsto\chi(j)A_{A,j}\). The actual label, matrix dimensions and Casimir remain. This is an isometric involution on the completion.

Assembly has coefficients
\[
 (\operatorname{Asm}A)_j=\sum_{A\supseteq\operatorname{supp}(j)}A_{A,j}.
\]
Its total \(c_j\)-weighted coefficient norm is at most \(|E_L|\|A\|_{\rm loc}\): every nonempty label occurs at least once in the sum over all anchors. Its kernel is therefore the closed subspace
\[
 \mathscr N_L=\left\{A:
 \sum_{A\supseteq\operatorname{supp}(j)}A_{A,j}=0
 \text{ for every }j\right\}. \tag{P8}
\]
The character \(\chi(j)\) does not depend on the enlarged label, so \(T\mathscr N_L=\mathscr N_L\). It induces an isometric involution on the Banach quotient \(\widehat{\mathscr V}_L=\mathscr V_L/\mathscr N_L\), with exact intertwining \(T\operatorname{Asm}=\operatorname{Asm}T\).

Keep the original union-labelled bilinear map
\[
 \mathcal B(f,h)_A=K^{-1}Q_H
 \sum_{A_1\cup A_2=A}\sum_{e,a}
 (X_{e,a}f_{A_1})(X_{e,a}h_{A_2}). \tag{P9}
\]
Equation (P5) proves the label-by-label identity
\[
 T\mathcal B(f,h)=\mathcal B(Tf,Th). \tag{P10}
\]
The removed scalar remains the separately recorded energy scalar and is fixed by \(T\).

Here are the original estimates needed for completion and inversion. A nonzero physical block contains a singlet at every vertex, so \(j_e\le\sum_{f\ne e,\ f\ni v}j_f\). At the endpoints of one edge, the sum \(J_1\) of the other incident spins obeys \(J_1\ge2j_e\). Their outer endpoints are distinct because the cubic graph is simple and triangle-free. The vertex inequalities at those endpoints give \(J_1\le2J_2\), counting each further edge at most twice. Thus \(\sum_fj_f\ge4j_e\). Since \(j(j+1)\ge3j/2\) at every nonzero half-integer,
\[
 c_j\ge6j_e,\qquad \sum_ej_e\le\tfrac23c_j. \tag{P11}
\]
The full original coefficient product obeys \(\|fh\|_X\le\|f\|_X\|h\|_X\): unitarily decompose the tensor-product representation with all multiplicities, pinch to irreducible blocks, and partially trace their multiplicity spaces. Pinching contracts trace norm; the partial trace contracts it by duality against \(Z\otimes I\), \(\|Z\|\le1\). The original spin generator has norm \(j_e\), yielding the derivative bound \(j_e\|A_j\|_1\). Define the unchanged F6 norms
\[
 m(f)=\max_b\sum_{A\ni b,j}\Big(\sum_ej_e\Big)\|A_{A,j}\|_1,\qquad
 t(f)=\max_e\sum_{A\ni e,j}j_e\|A_{A,j}\|_1.
\]
An output anchor belongs to at least one input union label. Sum first over anchors in the first input and then those in the second. The possible double counting only increases the nonnegative bound. The three generators give factor 3, while the actual output Casimir cancels its inverse in (P9). Therefore
\[
 \|\mathcal B(f,h)\|_{\rm loc}
 \le3\{m(f)t(h)+m(h)t(f)\}
 \le\tfrac23\|f\|_{\rm loc}\|h\|_{\rm loc}. \tag{P12}
\]
The last inequality uses \(m(f)\le2\|f\|_{\rm loc}/3\) and \(t(f)\le\|f\|_{\rm loc}/6\), proved by (P11). In particular,
\[
 \|2\mathcal B(q,\cdot)\|\le m(q)+4t(q). \tag{P13}
\]
The bounds include every boundary anchor and are independent of \(L\).

Assembly of (P9) is \(K^{-1}Q_H\Gamma(\operatorname{Asm}f,\operatorname{Asm}h)\). This follows first for finite coefficients, then by continuity: at fixed finite \(L\), the total \(c_j\)-weighted norm controls every first and second derivative, since \(j_e\le c_j\), \(j_e^2\le c_j\), and \(j_ej_f\le[j_e(j_e+1)+j_f(j_f+1)]/2\le c_j\). Thus \(\mathcal B(\mathscr N_L,\mathscr V_L)\) and \(\mathcal B(\mathscr V_L,\mathscr N_L)\) lie in \(\mathscr N_L\). Equations (P10)–(P13) descend to the quotient by taking infima over representatives.

## P4. Original face space and coefficient parity

Let \(P\) be the original physical spectral projection onto \(\ker(K-3)\), acting blockwise while retaining every label \(A\), and \(R=I-P\). These projections contract (P7), preserve (P8), and commute with \(T\).

The exact face-space identification follows in the original blocks. If \(c_j=3\), there are at most four active edges, because each contributes at least \(3/4\). The singlet inequalities exclude valence-one active vertices. Such a finite graph contains a cycle. The cubic graph has no triangle or odd cycle, so all four edges form one elementary face and there are no others. The singlet at each two-edge vertex forces equal spins, and \(4j(j+1)=3\) forces \(j=1/2\). Each such vertex invariant is one-dimensional; contracting the four original indices gives \(W_p\). Conversely \(W_p\) is physical and \(KW_p=3W_p\). Distinct faces have distinct product-spin supports and are orthogonal; successive Haar integration gives \(\int W_p^2\,dU=1\). This proves the G8 identity and, by (P4),
\[
 \ker(K-3)=\operatorname{span}\{W_p\},\qquad TP=PT=-P. \tag{P14}
\]
An enlarged label does not change its spin character.

Retain the complete original recurrence
\[
 v_1=S/3,\qquad v_n=\sum_{i=1}^{n-1}\mathcal B(v_i,v_{n-i})\quad(n\ge2).
 \tag{P15}
\]
The base case is \(Tv_1=-v_1\). If \(Tv_i=(-1)^iv_i\) for all \(i<n\), then (P10) gives
\[
 Tv_n=\sum_{i=1}^{n-1}\mathcal B((-1)^iv_i,(-1)^{n-i}v_{n-i})
 =(-1)^nv_n.
\]
Hence, on the original labelled source,
\[
 \boxed{Tv_n=(-1)^nv_n\quad(n\ge1).} \tag{P16}
\]
In particular an actual coefficient at \((A,j)\) is zero when \(\chi(j)\ne(-1)^n\); the recurrence and every original label remain intact.

For the fifth reference define
\[
 q_5(\xi)=\sum_{i=1}^5\xi^iv_i,\quad
 J_i=2\mathcal B(v_i,\cdot),\quad
 J_5(\xi)=\sum_{i=1}^5\xi^iJ_i.
\]
Here \(J_i\) denotes the coefficient called \(J_{[i]}\) in the earlier J1–J7, whereas \(J_5(\xi)\) denotes the fifth-reference polynomial. Equations (P10),(P16) imply
\[
 Tq_5(\xi)=q_5(-\xi),\quad TJ_iT=(-1)^iJ_i,\quad
 TJ_5(\xi)T=J_5(-\xi). \tag{P17}
\]

## P5. Certified analytic disk and full complementary inverse

The original F26 supplies proved upward bounds \(m(v_i)\le m_i\), \(t(v_i)\le t_i\):
\[
\begin{array}{c|cc}
i&m_i&t_i\\\hline
1&64/3&16/3\\
2&5834/39&137/6\\
3&336572872/208845&225985217/1253070\\
4&17270702970768271/341697152160&110695177857394584026401/18025447358750832000\\
5&1638684&190128 .
\end{array}\tag{P18}
\]
They concern the full original coefficients, including all source rows and boundary anchors. This derivation reads the proofs and receiving estimates; it does not claim a fresh replay of the inherited 662-representative catalogue. Their exact source versions and hashes are in `SOURCE_READING_USE_LEDGER.json`.

By (P13), \(\|J_i\|\le a_i=m_i+4t_i\), explicitly
\[
\begin{split}
a_1&=128/3,\quad a_2=3132/13,\quad a_3=292337810/125307,\\
a_4&=169232115504453213210913/2253180919843854000,\quad
a_5=2399196.
\end{split}\tag{P19}
\]
Put \(\ell(x)=\sum_{i=1}^5a_ix^i\) and let \(\beta\) be the unique positive root of \(\ell(\beta)=1\). All \(a_i>0\), so \(\ell\) is strictly increasing on \([0,\infty)\), starts at zero and tends to infinity, proving existence and uniqueness. Exact rational bisection is retained in `EXACT_CHECKS.json`; \(\beta\approx0.020200392941788888\) is only a display value.

For every complex \(\xi\) with \(x=|\xi|<\beta\),
\[
 \|J_5(\xi)\|\le\ell(x)<1.
\]
Since \(R\) contracts, on the full original complement of either the labelled source or its quotient,
\[
 D_5(\xi)=R-RJ_5(\xi)R,\qquad
 \boxed{D_5(\xi)^{-1}=\sum_{k=0}^\infty(RJ_5(\xi)R)^k,\quad
 \|D_5(\xi)^{-1}\|\le\frac1{1-\ell(x)}.} \tag{P20}
\]
The constant term is the identity \(R\) of that complementary space. The tail after \(k=N\) is bounded by \(\ell(x)^{N+1}/(1-\ell(x))\). Convergence is uniform on each compact subdisk, proving operator holomorphy on the full certified disk \(D_\beta\). No maximal-radius claim is made.

Exact rational evaluation gives
\[
 \ell(19/1000)<93/100,\qquad
 \|D_5(\xi)^{-1}\|<100/7\quad(|\xi|\le19/1000). \tag{P21}
\]
Thus this bound covers the entire original fifth-source interval \(x\le\alpha\), since F29 gives
\[
 0.018424953576117616681<\alpha
 <0.018424953576117616682<19/1000 .
\]
This estimates the full complementary operator, not a face compression. From (P17),
\[
 TD_5(\xi)T=D_5(-\xi),\qquad
 TD_5(\xi)^{-1}T=D_5(-\xi)^{-1}. \tag{P22}
\]
The same relations hold coefficientwise as formal series.

## P6. Every odd Schur coefficient vanishes before assembly

The original Schur map is
\[
 \mathscr S_5(\xi)=P-PJ_5(\xi)P
 -PJ_5(\xi)R D_5(\xi)^{-1}RJ_5(\xi)P. \tag{P23}
\]
It is a bounded holomorphic face-range map on \(D_\beta\). Equations (P17),(P22) give \(T\mathscr S_5(\xi)T=\mathscr S_5(-\xi)\). By (P14), both its endpoint actions of \(T\) are \(-I\). Therefore
\[
 \boxed{\mathscr S_5(-\xi)=\mathscr S_5(\xi).} \tag{P24}
\]

More strongly, for \(k\ge1\) and \(i_s\in\{1,\ldots,5\}\), define the literal word
\[
 F_{i_1,\ldots,i_k}=PJ_{i_1}RJ_{i_2}R\cdots RJ_{i_k}P,
 \quad F_i=PJ_iP\text{ if }k=1.
\]
Conjugating each factor gives
\[
 TF_{i_1,\ldots,i_k}T=(-1)^{i_1+\cdots+i_k}F_{i_1,\ldots,i_k},
\]
whereas its endpoints and (P14) give \(TF_{i_1,\ldots,i_k}T=F_{i_1,\ldots,i_k}\). Consequently
\[
 \boxed{F_{i_1,\ldots,i_k}=0
 \quad\text{whenever }i_1+\cdots+i_k\text{ is odd}.} \tag{P25}
\]
This is a labelled-source identity, for every original union label, and therefore descends to the quotient. No cancellation between different words is required.

In particular the full third coefficient is
\[
 [\xi^3]\mathscr S_5
 =-PJ_3P-PJ_1RJ_2P-PJ_2RJ_1P-PJ_1RJ_1RJ_1P=0. \tag{P26}
\]
Each of these four summands is zero separately. Every \([\xi^{2r+1}]\mathscr S_5\), \(r\ge0\), vanishes; no higher even channel is discarded.

## P7. The retained complete second coefficient

To combine the original J1–J6 with this result, keep all their intermediate channels. Put \(D_p=\chi_1(U_p)\). From \(W_p^2=1+D_p\),
\[
 KD_p=8D_p,\quad\|D_p\|_H^2=1,\quad
 \Gamma(W_p,W_p)=3-D_p.
\]
For adjacent faces \(p\sim q\), let \(C_{0,pq},C_{1,pq}\) be the original shared-edge spin-zero and spin-one projections of \(W_pW_q\). Cyclic trace and inversion of a whole SU(2) trace put the ordered words at that edge into \(\operatorname{Tr}(UA),\operatorname{Tr}(U^{-1}B)\), retaining the two three-link paths. The six nonshared links are independent Haar factors; successive integration makes \(A,B\) independent Haar variables, also independent of \(U\). Thus \(\|W_pW_q\|_H^2=1\), while \(\|\operatorname{Tr}(AB)/2\|_H^2=1/4\). Orthogonality of the two shared-edge spin projections gives the remaining norm \(3/4\). In full,
\[
 C_0=\tfrac12\operatorname{Tr}(AB),\quad C_0+C_1=W_pW_q,\quad
 KC_0=\tfrac92C_0,\quad KC_1=\tfrac{13}2C_1,
\]
\[
 \|C_0\|_H^2=\tfrac14,\quad\|C_1\|_H^2=\tfrac34,\quad
 \langle C_0,C_1\rangle_H=0.
\]
The product rule \(K(fh)=(Kf)h+f(Kh)-2\Gamma(f,h)\) gives
\(\Gamma(W_p,W_q)=3C_0/4-C_1/4\). Nonadjacent derivative supports are disjoint. The self-face scalar 3 is removed only by the original \(Q_H\). Thus the complete outgoing map is
\[
 J_1W_p=-\tfrac1{12}D_p+
 \sum_{q\sim p}\left(\tfrac19C_{0,pq}-\tfrac1{39}C_{1,pq}\right).
 \tag{P27}
\]
Its Casimirs imply \(PJ_1P=0\).

Two different unordered face pairs have different independent link-center characters. Otherwise the mod-two sum of at most four distinct faces would have zero edge boundary. Each of the four edges of an included face would require a different other face, since distinct elementary faces share at most one edge. At least five faces would be required, a contradiction. The pair characters are also distinct from the completely even spin-one face character. Haar substitution therefore gives exactly the pair-selection rules below.

For a Casimir-\(c\) component \(h_c\), integration by parts and the product rule give
\[
 \Gamma(S,\cdot)^*=3S-\Gamma(S,\cdot),\quad
 \langle h_c,\Gamma(S,W_r)\rangle_H
 =\tfrac{6-c}{2}\langle h_c,SW_r\rangle_H .
\]
Keeping \(PK^{-1}Q_H=P/3\) yields
\[
 PJ_1h_c=\tfrac c9PSh_c. \tag{P28}
\]
Indeed its scalar factor is \((2/9)[3-(6-c)/2]=c/9\).
The selection rules force the two fundamental face factors in \(PSD_p\) to coincide. If their common face is \(r\ne p\), then \(\int W_r^2D_p=\int(1+D_r)D_p=0\) by the distinct spin-one supports. The surviving integral is \(\int W_p^2D_p=1\), giving \(PSD_p=W_p\). For the two shared-edge channels only the original unordered pair survives, and its face integrals are exactly their squared Haar norms. Hence
\[
 PJ_1D_p=\tfrac89W_p,\quad
 PJ_1C_0=\tfrac18(W_p+W_q),\quad
 PJ_1C_1=\tfrac{13}{24}(W_p+W_q).
\]
The adjacent return keeps the two terms
\[
 \tfrac19\tfrac18(W_p+W_q)
 -\tfrac1{39}\tfrac{13}{24}(W_p+W_q)
 =(\tfrac1{72}-\tfrac1{72})(W_p+W_q)=0.
\]
The self-face return is \(-\tfrac1{12}\tfrac89W_p=-2W_p/27\). Therefore
\[
 PJ_1RJ_1P=PJ_1^2P=-\tfrac2{27}P. \tag{P29}
\]

The complete second source is
\[
 v_2=-\tfrac1{72}\sum_pD_p+
 \sum_{\{p,q\}:p\sim q}
 \left(\tfrac1{27}C_{0,pq}-\tfrac1{117}C_{1,pq}\right).
\]
For a Casimir-\(c\) part \(f_c\), projecting the product rule gives
\(P\Gamma(f_c,W_q)=cP(f_cW_q)/2\); its contribution to \(PJ_2W_q\) is \(cP(f_cW_q)/3\). The self coefficient is
\(-\tfrac1{72}\tfrac83=-1/27\). The two adjacent coefficients to either face are
\[
 \tfrac1{27}\frac{9/2}{3}\tfrac14=\tfrac1{72},\qquad
 -\tfrac1{117}\frac{13/2}{3}\tfrac34=-\tfrac1{72}.
\]
Thus, preserving both contributions,
\[
 PJ_2P=-\tfrac1{27}P,\qquad
 -PJ_2P-PJ_1RJ_1P=\tfrac19P. \tag{P30}
\]
For an input face carrying an enlarged label \(A_0\), the self-return label is \(A_0\), and the two cancelling adjacent contributions both have label \(A_0\cup\partial p\cup\partial q\). Hence these identities hold on the entire labelled face range, before quotienting.

## P8. A rational bound for the complete remaining even tail

The Neumann series makes the original Schur expression exactly
\[
 \mathscr S_5(\xi)=P-
 \sum_{k\ge1}\sum_{1\le i_1,\ldots,i_k\le5}
 \xi^{i_1+\cdots+i_k}F_{i_1,\ldots,i_k}. \tag{P31}
\]
For \(x=|\xi|<\beta\), the sum of the operator norms is bounded by
\[
 h(x)=\sum_{k\ge1}\ell(x)^k=\frac{\ell(x)}{1-\ell(x)}.
\]
Thus regrouping by total degree is valid. Write \(h(x)=\sum_{n\ge1}h_nx^n\); all \(h_n\ge0\), and
\(\|[\xi^n](P-\mathscr S_5)\|\le h_n\). In particular
\[
 h_2=a_2+a_1^2=\frac{241180}{117}. \tag{P32}
\]
Put \(e(x)=a_2x^2+a_4x^4\), \(o(x)=a_1x+a_3x^3+a_5x^5\). The full even part is
\[
 \frac{h(x)+h(-x)}2
 =\frac12\left\{\frac{e+o}{1-e-o}+\frac{e-o}{1-e+o}\right\}
 =\frac{e-e^2+o^2}{(1-e)^2-o^2}. \tag{P33}
\]
For \(x<\beta\), both denominator factors \(1-e-o\) and \(1-e+o\) are positive. Retain the entire numerator and denominator and define
\[
 \mathcal E_4(x)=
 \frac{e(x)-e(x)^2+o(x)^2}{[1-e(x)]^2-o(x)^2}
 -(a_2+a_1^2)x^2
 =\sum_{r\ge2}h_{2r}x^{2r}. \tag{P34}
\]
Its nonnegative series proves nonnegativity, monotonicity and order four. Combining (P25),(P30),
\[
 \boxed{\mathscr S_5(\xi)=
 (1+\xi^2/9)P+\mathcal R_4(\xi),\quad
 \mathcal R_4(-\xi)=\mathcal R_4(\xi),\quad
 \|\mathcal R_4(\xi)\|\le\mathcal E_4(|\xi|).} \tag{P35}
\]
Every even order at least four and every complementary spin and union label is included. The bound is independent of \(L\) in the original local source norm and the assembly quotient norm.

Exact rational evaluation in `EXACT_CHECKS.json` proves
\[
 \mathcal E_4(1/100)<66/1000,\qquad
 \mathcal E_4(1/64)<3/4. \tag{P36}
\]
For size only, the corresponding decimals are \(0.06577819999898235\) and \(0.737650994481419\). Since \(x^{2k}\le(x/r)^4r^{2k}\) for \(k\ge2\), \(0\le x\le r<\beta\),
\[
 \mathcal E_4(x)\le(x/r)^4\mathcal E_4(r). \tag{P37}
\]
In particular the entire remainder has bound \((66/1000)(100|\xi|)^4\) on \(|\xi|\le1/100\).

The full \(I-J_5(\xi)\) also has its complete Neumann inverse on \(D_\beta\). Solving its two block equations gives
\[
 \mathscr S_5(\xi)^{-1}=P(I-J_5(\xi))^{-1}P,\qquad
 \|\mathscr S_5(\xi)^{-1}\|\le\frac1{1-\ell(|\xi|)}. \tag{P38}
\]
For a face forcing \(f\), the complementary equation gives \(u_R=D_5^{-1}RJ_5Pu_P\). Substituting it into the face equation gives exactly (P23); conversely this substitution solves both equations. This proves the block identity and its inverse, including points where (P34) is too large for a small-perturbation estimate.

One further direct consequence of (P36), on the complete complex disk \(|\xi|\le1/64\), is
\[
 |1+\xi^2/9|\ge1-1/36864,\quad
 \|\mathscr S_5(\xi)^{-1}\|<
 \frac1{1-1/36864-3/4}.
\]
No Haar self-adjointness, Schur positivity, new physical gap or enlarged nonlinear source endpoint is inferred from these auxiliary Banach bounds.

## P9. Full Hamiltonian and retained vacuum scalar

Equations (P4),(P5) prove, on the original fixed domain and for every complex \(\xi\),
\[
 \boxed{TH_L(\xi)T
 =\kappa K+\kappa\xi(2M+S)
 =H_L(-\xi)+4\kappa M\xi I.} \tag{P39}
\]
The scalar is the difference of the two original \(2\kappa M\xi\) terms; neither Hamiltonian has lost its scalar.

For real \(\xi\), list the physical eigenvalues in increasing order with multiplicity. Unitary conjugation gives for every \(n\ge0\)
\[
 \boxed{E_{n,L}(\xi)=E_{n,L}(-\xi)+4\kappa M\xi.} \tag{P40}
\]
Subtracting the exact original ground energies consequently yields
\[
 E_{n,L}(\xi)-E_{0,L}(\xi)
 =E_{n,L}(-\xi)-E_{0,L}(-\xi),
\]
\[
 T[H_L(\xi)-E_{0,L}(\xi)]T=H_L(-\xi)-E_{0,L}(-\xi). \tag{P41}
\]
Thus the physical gap on every original finite box is even in the auxiliary real coefficient \(\xi\) at fixed \(\kappa\).

The positive unit ground vector exists and is unique for every real \(\xi\). The original argument F3 applies: compactness supplies a ground minimizer; the derivative modulus inequality makes it nonnegative; elliptic regularity and the strong maximum principle make it smooth and strictly positive. For this vector \(\psi\), integration by parts in its exact eigen-equation gives
\[
 q_{H-E_0}(\psi f)=
 \kappa\int\psi^2\sum_{e,a}|X_{e,a}f|^2\,dU.
\]
Division by the smooth positive \(\psi\) preserves \(H^1\). The quotient of any other ground vector by \(\psi\) has every derivative zero, hence is constant on the connected configuration space. Positivity and unit norm fix that constant. Gauge transformations preserve all these conditions, so uniqueness makes the scalar-space ground vector physical.

Define the original vacuum density \(\rho_L(\xi)=\psi_L(\xi)^2\). Since \(T\) preserves positivity and norm, (P39) and uniqueness give
\[
 \psi_L(-\xi)=T\psi_L(\xi),\qquad
 \rho_L(-\xi)=T\rho_L(\xi). \tag{P42}
\]
The exact zero-Haar logarithm
\[
 v_L(\xi)=\log\psi_L(\xi)-P_H\log\psi_L(\xi)
\]
satisfies \(v_L(-\xi)=Tv_L(\xi)\). The original normalization constant and scalar are
\[
 c_L(\xi)=-\tfrac12\log\int e^{2v_L(\xi)}\,dU,\quad
 C_L(\xi)=P_H\Gamma(v_L(\xi),v_L(\xi)).
\]
Haar invariance and (P5) prove \(c_L(-\xi)=c_L(\xi)\), \(C_L(-\xi)=C_L(\xi)\), with
\[
 E_{0,L}(\xi)=2\kappa M\xi-\kappa C_L(\xi). \tag{P43}
\]
Every original removed scalar is present in this energy equation.

The original multiplication map \(\mathcal U_\xi f=\psi_L(\xi)f\) from \(L^2(\rho_L(\xi)dU)\) to Haar \(L^2\) has the exact intertwining
\[
 \mathcal U_{-\xi}T=T\mathcal U_\xi.
\]
Here \(T:L^2(\rho_L(\xi)dU)\to L^2(\rho_L(-\xi)dU)\) is unitary by Haar substitution. Combining with (P41) proves covariance of the original ground-transformed operators and their forms. For each integrable observable \(f\),
\[
 \int\rho_L(-\xi)f\,dU=\int\rho_L(\xi)Tf\,dU.
\]
Each original face expectation is therefore odd. This uses the exact different interacting measures and does not replace them by Haar measure.

## P10. The complete nonlinear source and its interior inverse

The parity extends to the full fifth-reference correction by its proved construction. Retain
\[
 R_5(\xi)=\xi v_1+\mathcal B(q_5(\xi),q_5(\xi))-q_5(\xi),\qquad
 L_5(\xi)=I-J_5(\xi).
\]
Equations (P10),(P17) give \(TR_5(\xi)=R_5(-\xi)\) and \(TL_5(\xi)^{-1}T=L_5(-\xi)^{-1}\) on \(D_\beta\). For the complete original tree series,
\[
 w_1=L_5^{-1}R_5,\qquad
 w_n=L_5^{-1}\sum_{i+j=n}\mathcal B(w_i,w_j),
\]
induction gives \(Tw_n(\xi)=w_n(-\xi)\). Its proved F30–F32 absolute convergence on \(|\xi|\le\alpha\) gives
\[
 T[q_5(\xi)+\sum_{n\ge1}w_n(\xi)]
 =q_5(-\xi)+\sum_{n\ge1}w_n(-\xi). \tag{P44}
\]
Absolute convergence includes the closed boundary. On the real interval, the original positive-ground reconstruction identifies this source with the logarithm in (P43).

Retain every scalar in
\[
 b_{ij}=3(m_it_j+m_jt_i),\quad
 \delta(x)=\sum_{1\le i,j\le5,\ i+j\ge6}b_{ij}x^{i+j},
\]
\[
 \mathscr D(x)=[1-\ell(x)]^2-\tfrac83\delta(x),\qquad
 w_*(x)=\tfrac34[1-\ell(x)-\sqrt{\mathscr D(x)}].
\]
Original F31 proves \(\|v-q_5\|\le w_*(x)\), and \(\mathscr D(x)>0\) for \(0\le x<\alpha\). For the actual full Jacobian \(J(\xi)=2\mathcal B(v(\xi),\cdot)\), (P12) therefore gives
\[
 \|J(\xi)\|\le\ell(x)+\tfrac43w_*(x)
 =1-\sqrt{\mathscr D(x)}<1.
\]
Consequently the full nonlinear complementary inverse exists on that interior disk and
\[
 \boxed{\|(R-RJ(\xi)R)^{-1}\|
 \le1/\sqrt{\mathscr D(x)}\quad(0\le x<\alpha).} \tag{P45}
\]
Its Schur map is even by the same conjugation proof. At \(x=\alpha\), this estimate has zero denominator and asserts no endpoint inverse. The polynomial-reference inverse (P20) remains finite there. Their exact connecting perturbation is
\[
 J-J_5=2\mathcal B(v-q_5,\cdot),\qquad
 \|J-J_5\|\le\tfrac43w_*.
\]

## P11. Exact human-source comparison and receiving calculation

Li–Meurice's Section II, original source lines 162–198, uses the \(SU(2)\) action
\(\beta_{\rm LM}\sum_p(1-W_p/2)\) on symmetric periodic lattices with even side length. Here \(\beta_{\rm LM}\) denotes their original variable \(\beta\), distinguished from the inverse-radius root in P5. The original potential here is exactly
\[
 \kappa\xi\sum_p(2-W_p)=2\kappa\xi\sum_p(1-W_p/2).
\]
For a static weight \(e^{-tV}\), the full parameter map is \(\beta_{\rm LM}=2t\kappa\xi\); their scalar \(2\beta_{\rm LM}M\) becomes \(4t\kappa M\xi\). The explicit open-box assignment (P3) proves the local action identity on the present geometry, and commutation with every original derivative proves the additional kinetic-operator relation (P39). Thus the quantum heat traces satisfy
\[
 \operatorname{Tr}_{\rm phys}e^{-tH_L(-\xi)}
 =e^{4t\kappa M\xi}\operatorname{Tr}_{\rm phys}e^{-tH_L(\xi)}
 \quad(t>0,\ \xi\in\mathbb R).
\]
This follows by exponentiating (P39) and unitary invariance of trace. For completeness, \(|2M-S|\le4M\), so the min-max principle bounds the full heat trace by
\[
 e^{4t\kappa M|\xi|}
 \left[\sum_{j=0,1/2,\ldots}(2j+1)^2e^{-t\kappa j(j+1)}\right]^{|E_L|}<\infty.
\]
Each one-link sum converges by its Gaussian decay, proving trace class; restriction to the physical reducing subspace preserves it. No equality between the static integral and quantum heat trace is asserted.

Their lines 339–353 explicitly derive perturbative parity and Wilson-loop parity; those results are an antecedent, not a new finding here. Their lines 267–288 discuss gauge equivalence within their constructed collections of special link-line configurations. This note does not use those passages as a classification of all periodic flat central twists.

The previously unfinished J7 calculation is strengthened by (P26), (P20), and (P35): the third coefficient is exactly zero; every higher odd return is zero before assembly; the complete complementary inverse has an explicit uniform bound; and the complete remaining even tail has an explicit rational majorant. The fourth coefficient is now the first unevaluated coefficient that can change this face Schur map. Its value is not replaced by the majorant, and no new nonlinear endpoint or physical gap is inferred. The original fourth return with every spin channel is the next concrete calculation; the full fifth residual and the bounds above supply rigorous remainders while that coefficient is evaluated.
