# Exact fifth-source return across an elementary cube

This is an independent calculation in the original open three-dimensional SU(2) lattice. The sources are the retained programme formulas [G1--G14](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/fa79faff2cd697e16cfa3a7953f36810c22c8922/yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md) and [F14--F20](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/33a4c39de32c2c7fdf6f8ce796e40389f766669f/yang-mills/consolidation/20260921-fifth-reference/package/workbench/yang-mills/continuations/20260921-fifth-reference-return/FIFTH_REFERENCE.md#L139). The parent task has verified these public source identities. Their exact local versions, reading coverage and hashes are retained in this directory's PUBLIC_SOURCE_READING_USE_LEDGER.json. The present proof is a new calculation from those formulas, with no historical-priority claim.

## C1. Original coordinates, operators and source coefficients

For an integer L>=2, retain the vertices {-L,...,L}^3, each contained positive edge (n,i), and each contained face p=(n;i,j), i<j. Every edge variable U_i(n) lies in SU(2), with Haar probability on each factor. The original face word is

\[
 W_{(n;i,j)}=\operatorname{Tr}\bigl(U_i(n)U_j(n+e_i)
 U_i(n+e_j)^{-1}U_j(n)^{-1}\bigr). \tag{C1}
\]

The original generators are T_a=-i sigma_a/2 and X_{e,a}f=d/ds f(...,exp(sT_a)U_e,...) at s=0. Retain

\[
 K=-\sum_{e,a}X_{e,a}^2,\quad
 \Gamma(f,h)=\sum_{e,a}(X_{e,a}f)(X_{e,a}h),\quad
 \mathcal B(f,h)=K^{-1}Q_H\Gamma(f,h). \tag{C2}
\]

Here Q_H removes the Haar scalar and K^{-1} is the inverse on nonconstant physical blocks. In the labelled source every product retains the complete union of its input edge labels, even if its active product-spin support is smaller.

Introduce independent face parameters t_p solely to identify coefficients of the original recurrence:

\[
 v(t)=\frac13\sum_pt_pW_p+\mathcal B(v(t),v(t)),\qquad
 v(t)=\sum_{n\ge1}v_n(t). \tag{C3}
\]

The degree-n polynomial v_n satisfies the original recurrence v_n=sum_{i=1}^{n-1} B(v_i,v_{n-i}). A coefficient [prod_{p in D}t_p]v_|D| is an ordinary polynomial coefficient, with no division by |D|! and with every ordered split present.

Fix the cube with vertices {0,1}^3. Denote its faces

\[
 B=(0;1,2),\quad T=(e_3;1,2),\quad
 S=(0;1,3),\quad N=(e_2;1,3),\quad
 W=(0;2,3),\quad E=(e_1;2,3). \tag{C4}
\]

The missing face is B; the five input faces form A={T,S,N,W,E}. Their original union contains all twelve cube edges. Its four singly occurring edges are exactly the four edges of B. Its other eight edges each occur twice. The target product-spin assignment has spin 1/2 on the four edges of B and spin zero on the other eight edges. Denote the corresponding projection by P_b. Its total original Casimir is 4(3/4)+8[0(0+1)]=3.

Every other product-spin assignment of the product of these five face traces has the same four spin-1/2 single edges and at least one spin-1 repeated edge, so its total Casimir is at least 3+2. Consequently the full face-space projection P=1_{K=3} agrees with P_b on this five-face coefficient. The four two-edge vertex invariant spaces on the missing boundary have dimension one, and their contraction is precisely W_B; thus this target block is one-dimensional. Its original label remains all twelve cube edges.

## C2. The recurrence with all original edge Casimirs

For a nonempty subset D of A, let r_e(D) count occurrences of the original edge e in its faces. With b_e=0 on every repeated edge, set

\[
 c_b(D)=\sum_{r_e(D)=1}\frac34+
 \sum_{r_e(D)=2}0(0+1). \tag{C5}
\]

The five-face adjacency graph has a vertex T joined to S,N,W,E, and the side cycle S-E-N-W-S. It has no other edges. An adjacency records one shared original edge. If D has k faces and m internal adjacencies, it has 4k-2m singly occurring edges. Formula (C5), including the zero terms on all repeated edges, gives c_b(D)=(3/4)(4k-2m). The table below enumerates all nonempty subsets and proves c_b(D)>0 for each; there is no Haar-scalar subtraction to alter these channels.

The exact scalar recurrence is

\[
 a_b(\{p\})=\frac13,\qquad
 a_b(D)=\frac1{2c_b(D)}\sum_{\varnothing\ne C\subsetneq D}
 \bigl[c_b(C)+c_b(D\setminus C)-c_b(D)\bigr]
 a_b(C)a_b(D\setminus C). \tag{C6}
\]

For completeness, this follows directly from the original differential operators. The Leibniz rule gives

\[
 2\Gamma(f,h)=(Kf)h+f(Kh)-K(fh). \tag{C7}
\]

On an edge already repeated within C, there is no occurrence in D\C. Its final spin-zero projector therefore commutes with multiplication by that second input. On an edge split between the two inputs, each input has exactly one fundamental occurrence, whose Casimir is 3/4. On an edge occurring only once in D, the same 3/4 remains. Projectors on different original edges commute. Applying the final edge projectors to (C7) therefore replaces the three K terms by c_b(C), c_b(D\C) and c_b(D), respectively, after the child coefficients have been projected on their internally repeated edges. The induction starts from W_p/3, proves (C6) for every ordered split, and gives

\[
 P_b[\prod_{p\in A}t_p]v_5
 =a_b(A)P_b\prod_{p\in A}W_p. \tag{C8}
\]

No intermediate channel capable of reaching the final channel has been removed: when both fundamental occurrences on an edge are already in a child, there is no further occurrence on that edge and its spin cannot change in a later multiplication.

In the following table, the numerator is the entire ordered sum in (C6), before division by 2c_b(D). The eight rows account for 5+8+2+4+6+1+4+1=31 subsets.

| Subset type | Multiplicity | k | m | Single edges | c_b(D) | Ordered numerator | a_b(D) |
|---|---:|---:|---:|---:|---:|---:|---:|
| One face | 5 | 1 | 0 | 4 | 3 | initial coefficient | 1/3 |
| Adjacent pair | 8 | 2 | 1 | 6 | 9/2 | 1/3 | 1/27 |
| Opposite side pair | 2 | 2 | 0 | 8 | 6 | 0 | 0 |
| T and adjacent sides, triangle | 4 | 3 | 3 | 6 | 9/2 | 2/9 | 2/81 |
| Three-face path | 6 | 3 | 2 | 8 | 6 | 2/27 | 1/162 |
| Four side faces | 1 | 4 | 4 | 8 | 6 | 16/243 | 4/729 |
| T and three side faces | 4 | 4 | 5 | 6 | 9/2 | 13/81 | 13/729 |
| All five faces A | 1 | 5 | 8 | 4 | 3 | 214/729 | 107/2187 |

Here are the complete arithmetic steps producing the last row. For a singleton split, deleting T leaves the four-side row; deleting any of the other four faces leaves the T-and-three-sides row. For a pair split, the eight nonzero pairs divide into four T-and-side pairs and four adjacent-side pairs; the two opposite-side pairs have zero coefficient. Retaining their zero terms gives

\[
\begin{aligned}
 a_b(A)=\frac1{2\cdot3}\Biggl\{&
 2\left[6\frac13\frac4{729}
       +4\frac92\frac13\frac{13}{729}\right]\\
 &+2\left[4\frac{15}2\frac1{27}\frac1{162}
       +4\cdot6\frac1{27}\frac2{81}
       +2\cdot9\cdot0\cdot\frac1{162}\right]\Biggr\}\\
 &=\frac1{6}\left(\frac{172}{729}+\frac{42}{729}\right)
 =\frac{107}{2187}. \tag{C9}
\end{aligned}
\]

The factor 2 in each bracket retains both input orderings. The exact check file records all 31 subsets and every individual ordered split, including those with zero contribution.

## C3. The exact Haar projection with the original face orientations

Write the four bottom positive edges as

\[
 a=U_1(0,0,0),\quad b=U_2(1,0,0),\quad
 c=U_1(0,1,0),\quad d=U_2(0,0,0),
\]

and the corresponding top edges as

\[
 A_1=U_1(0,0,1),\quad A_2=U_2(1,0,1),\quad
 A_3=U_1(0,1,1),\quad A_4=U_2(0,0,1).
\]

The four vertical edges are h_{xy}=U_3(x,y,0), x,y in {0,1}. The six original words, without any changed edge traversal, are

\[
\begin{array}{ll}
 W_B=\operatorname{Tr}(abc^{-1}d^{-1}),&
 W_T=\operatorname{Tr}(A_1A_2A_3^{-1}A_4^{-1}),\\
 W_S=\operatorname{Tr}(ah_{10}A_1^{-1}h_{00}^{-1}),&
 W_N=\operatorname{Tr}(ch_{11}A_3^{-1}h_{01}^{-1}),\\
 W_W=\operatorname{Tr}(dh_{01}A_4^{-1}h_{00}^{-1}),&
 W_E=\operatorname{Tr}(bh_{11}A_2^{-1}h_{10}^{-1}).
\end{array} \tag{C10}
\]

The spin-zero projection on an original edge is exactly Haar integration on that edge. Therefore P_b of this product is the integral over the four h variables and the four A variables, while a,b,c,d remain arbitrary and unchanged. For fixed h, perform the explicit change of variables

\[
\begin{array}{ll}
 A'_1=h_{00}A_1h_{10}^{-1},& A'_2=h_{10}A_2h_{11}^{-1},\\
 A'_3=h_{01}A_3h_{11}^{-1},& A'_4=h_{00}A_4h_{01}^{-1}.
\end{array} \tag{C11}
\]

Left and right Haar invariance preserve the product measure. Substitution in (C10) and cancellation of adjacent inverse factors give the unchanged traces as

\[
 W_T=\operatorname{Tr}(A'_1A'_2(A'_3)^{-1}(A'_4)^{-1}),
\]

\[
 W_S=\operatorname{Tr}(a(A'_1)^{-1}),\quad
 W_E=\operatorname{Tr}(b(A'_2)^{-1}),\quad
 W_N=\operatorname{Tr}(c(A'_3)^{-1}),\quad
 W_W=\operatorname{Tr}(d(A'_4)^{-1}). \tag{C12}
\]

The integrand is now independent of all four h variables, whose probability integrals are each 1. This is an integration identity on the original eight variables, not a replacement of the configuration space or its labels.

Fundamental matrix orthogonality gives, for M in SU(2),

\[
 \int\operatorname{Tr}(MU^{-1})U\,dU=\frac M2,\qquad
 \int\operatorname{Tr}(MU^{-1})U^{-1}\,dU=\frac{M^{-1}}2. \tag{C13}
\]

Here is a direct derivation of the matrix orthogonality used in the first identity. Identify SU(2) with the unit quaternions q=(w,x,y,z), whose matrix is

\[
 U(q)=\begin{pmatrix}w+ix&y+iz\\-y+iz&w-ix\end{pmatrix}.
\]

Left and right multiplication by fixed unit quaternions are orthogonal maps of the real four-dimensional quaternion space. Spherical probability on S^3 is therefore left and right invariant and equals Haar probability. Reflection of one quaternion coordinate preserves spherical probability, so distinct coordinate products have zero integral. Permutation of coordinates preserves that probability, and w^2+x^2+y^2+z^2=1, so each coordinate square has integral 1/4. Substituting these sixteen second moments in the displayed matrix gives int U_{ij}(U^{-1})_{kl} dU=(1/2)delta_{il}delta_{jk}. Summing the trace indices proves the first identity in (C13). For the second, every SU(2) matrix satisfies Tr(V)=Tr(V^{-1}); this follows from its characteristic polynomial lambda^2-Tr(V)lambda+1 and the identity V+V^{-1}=Tr(V)I. Hence Tr(MU^{-1})=Tr(UM^{-1}). The change U to U^{-1}, followed by the first identity with M^{-1}, gives the second identity. Thus the inverse traversals contribute no sign.

Integrating successively in A'_1,A'_2,A'_3,A'_4 changes the top trace, with its multiplying side trace consumed at each step, into

\[
\begin{aligned}
 &\frac12\operatorname{Tr}(aA'_2(A'_3)^{-1}(A'_4)^{-1}),\\
 &\frac14\operatorname{Tr}(ab(A'_3)^{-1}(A'_4)^{-1}),\\
 &\frac18\operatorname{Tr}(abc^{-1}(A'_4)^{-1}),\\
 &\frac1{16}\operatorname{Tr}(abc^{-1}d^{-1}).
\end{aligned} \tag{C14}
\]

Consequently the exact operator identity on the original four boundary variables is

\[
 \boxed{P_b(W_TW_SW_NW_WW_E)=\frac1{16}W_B.} \tag{C15}
\]

There is no remaining scalar component: W_B has spin 1/2 on each of its four distinct edges and has Haar mean zero. Combining (C8), (C9) and (C15) proves

\[
 \boxed{P[\prod_{r\in\partial C\setminus\{p\}}t_r]v_5
       =\frac{107}{34992}W_p,} \tag{C16}
\]

where C is the original elementary cube and p its missing face, with the complete twelve-edge source label retained.

Equation (C16) holds for all six choices of the missing face and every contained translated cube. To prove this, translate the displayed coordinates and apply a signed coordinate permutation sending the selected missing face to B. The resulting bijection of original edge variables sends a reversed edge to its inverse. Haar probability is invariant under inversion. The edge Laplace operator from the bi-invariant metric, and its associated bilinear form Gamma, are invariant under this inversion, since left invariant generators are sent to right invariant generators with the same quadratic Casimir. The original face word becomes a cyclic conjugate of either the displayed word or its inverse. Trace is invariant under conjugation and, for SU(2), under inversion by the preceding characteristic-polynomial identity. Thus every Casimir, recurrence factor, Haar factor and trace sign in (C16) is preserved. All edges used belong to the contained cube; no exterior edge is introduced at a box boundary.

## C4. The exact face-pair term of the original Jacobian inverse

On the original source define

\[
 \mathcal L(t)=I-2\mathcal B(v(t),\cdot). \tag{C17}
\]

Its formal power-series inverse exists because its constant coefficient is I. On any of the retained analytic domains where the bilinear source converges and the Jacobian is invertible, the same coefficient identities hold for the analytic inverse. Differentiate (C3) in one original parameter t_q. The symmetry of Gamma and B gives

\[
 \mathcal L(t)\partial_{t_q}v(t)=\frac13W_q,
 \qquad
 P\mathcal L(t)^{-1}W_q=3\partial_{t_q}(Pv(t)). \tag{C18}
\]

Differentiation keeps the original union label of each coefficient. On assembly, the left-hand side is the q-th column of P L(t)^{-1}P in the orthonormal original face basis. For a fixed cube C and two distinct faces p,q of C, (C16) gives

\[
 \boxed{
 \left[\prod_{r\in\partial C\setminus\{p,q\}}t_r\right]
 \bigl\langle W_p,\mathcal L(t)^{-1}W_q\bigr\rangle_H
 =3\frac{107}{34992}=\frac{107}{11664}.} \tag{C19}
\]

The original face norm is one: successive Haar integration of W_p^2 gives int_{SU(2)}(Tr U)^2 dU=1, by the same fundamental character orthogonality. There is therefore no extra norm factor in (C19). No factor 5 occurs, because the differentiated coefficient contains t_q exactly once. If q=p, this particular cube-complement coefficient contains no t_q and contributes zero.

On the original uniform line t_r=xi, the contribution for this cube and ordered pair is (107/11664)xi^4. Summing actual contained cubes gives the additive cube contribution

\[
 \frac{107}{11664}\,\xi^4 N_{pq},\qquad
 N_{pq}=\#\{C:\ C\text{ is a contained elementary cube},\ p,q\in\partial C,\ p\ne q\}. \tag{C20}
\]

Equation (C20) is the cube contribution, not a statement that all other degree-four terms vanish. It includes adjacent face pairs and opposite face pairs with the same per-cube coefficient. Labels of different original cubes remain separate until assembly.

For the fifth-reference Jacobian L_5=I-2B(q_5,.) with q_5=sum_{n=1}^5 v_n, the coefficient in (C19) is identical: all coefficients of inverse degree at most four depend only on the Jacobian coefficients through degree four. Thus the computed term applies both to the full source and to the retained fifth-reference inverse at this order. Computing the fourth Schur coefficient also requires its lower-order inverse correction; that complete calculation belongs to the parent derivation.

## C5. Exact finite checks and their scope

`derive_cube.py` constructs the twelve original edge labels from (C1), verifies the single and repeated occurrences, computes all 31 positive subset Casimirs, and evaluates all ordered terms of (C6) using integer fractions. It independently evaluates the equivalent edge-count identity

\[
 c_b(C)+c_b(D\setminus C)-c_b(D)
   =\frac32\#\{e:\ r_e(C)=r_e(D\setminus C)=1\},
\]

and obtains the same coefficient at every subset. The original recurrence and its complete factors are retained in the primary calculation.

The script also checks (C15) with exact Haar cubature at three rational SU(2) boundary configurations. Write a unit quaternion as (w,x,y,z). The eight signed coordinate vectors have the same first moments and second moments as Haar probability on the unit sphere S^3: each first moment is zero and the second-moment matrix is I_4/4. Each integrated top variable in (C12) occurs in exactly two fundamental matrix factors, so its integrand is a polynomial of degree at most two in that quaternion. The product of the eight-node rules therefore integrates it exactly. The 8^4=4096 terms are evaluated with integer quaternion multiplication; the three exact integral values are 7/72, 1/8 and 7/72 and match W_B/16. These checks supplement the all-boundary-variable proof (C10)--(C15); they do not replace it.

`CUBE_EXACT_CHECKS.json` preserves every subset, every ordered split, all original word labels, the exact three coefficients 107/2187, 107/34992 and 107/11664, and each exact cubature result.
