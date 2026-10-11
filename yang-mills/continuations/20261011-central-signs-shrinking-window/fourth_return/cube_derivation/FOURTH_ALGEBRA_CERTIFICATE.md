# Independent algebra certificate for the fourth Schur coefficient

The checked input is `../FOURTH_SCHUR_COEFFICIENT.md`, in particular the displayed fifth-source polynomial Q20, the inverse relation Q15--Q16, and the conclusions Q28, Q30, Q34--Q35. `FOURTH_ALGEBRA_CHECKS.json` records its SHA-256 at the time of this calculation. The task is to derive the downstream algebra from the displayed polynomial; this certificate does not claim a second independent derivation of its non-cube fifth-source coefficients from the original recurrence. The cube coefficient has already been independently proved in `CUBE_FIFTH_PROJECTION.md`.

No correction is needed in Q28, Q30, Q34 or Q35.

## A1. The inverse correction and the derivative multiplicities

In the original face space, P is the identity. Write the even expansions as

\[
 G=P+\xi^2G_2+\xi^4G_4+O(\xi^6),\qquad
 S=P+\xi^2S_2+\xi^4S_4+O(\xi^6).
\]

Multiplication in its given order, SG=P, gives

\[
 S_2+G_2=0,\qquad S_4+G_4+S_2G_2=0.
\]

The proved second coefficient G_2=-P/9 therefore gives S_2=P/9 and

\[
 S_4=\frac P{81}-G_4. \tag{A1}
\]

The correction has a positive sign. It is neither omitted nor multiplied by two. This coefficient comparison does not assume that higher coefficient matrices commute.

The exact original source derivative map is G_4 W_q=3P partial_{x_q}V_5(1). Fix one output face p. Its row of the displayed Q20 polynomial contains exactly

\[
 u x_p^5
 +\sum_{r\sim p}(b x_p^3x_r^2+c x_px_r^4)
 +\sum_{T\ni p}\eta_{p,T}x_p\prod_{r\in T\setminus\{p\}}x_r^2
 +d\sum_{C\ni p}\prod_{r\in\partial C\setminus\{p\}}x_r.
 \tag{A2}
\]

All sums in (A2) run over actual contained faces, triples and cubes. The unordered pair sum of Q20 supplies exactly one term of each displayed kind in this fixed output row. In particular it does not supply an additional factor two. Multiplying the following differentiation multiplicities by the original derivative-map factor three gives:

| Original output-p monomial | Derivative in x_p | Derivative in x_q, q different from p |
|---|---:|---:|
| u x_p^5 | 15u | 0 |
| b x_p^3 x_q^2 | 9b | 6b |
| c x_p x_q^4 | 3c | 12c |
| eta x_p x_q^2 x_r^2 | 3 eta | 6 eta for q or r |
| d product over the other five cube faces | 0 | 3d for each other cube face |

Thus, with d_p the actual adjacency degree and c_pq the actual number of contained cubes containing two distinct faces,

\[
\begin{aligned}
 (G_4)_{pp}&=15u+(9b+3c)d_p+3\sum_{T\ni p}\eta_{p,T},\\
 (G_4)_{pq}&=(6b+12c)\mathbf1_{p\sim q}
             +6\sum_{T\supset\{p,q\}}\eta_{p,T}+3d c_{pq}
             \quad(p\ne q). \tag{A3}
\end{aligned}
\]

Substitute the original displayed values, keeping their individual factors:

\[
\begin{aligned}
\frac1{81}-15\frac7{3888}&=-\frac{19}{1296},\\
-\left(9\frac{-301}{2956824}+3\frac{-55}{3639168}\right)
 &=\frac{15163}{15769728},\\
-\left(6\frac{-301}{2956824}+12\frac{-55}{3639168}\right)
 &=\frac{347}{438048},\\
-3\frac{107}{34992}&=-\frac{107}{11664}.
\end{aligned} \tag{A4}
\]

Equations (A1)--(A4) reproduce every term and sign in Q28. The derivative keeps the original union of source-edge labels. The inverse correction acts at the input label because the second return is exactly the scalar multiple -P/9 with all adjacent-pair returns cancelling at their own shared union labels.

## A2. The antisymmetric part

Self terms, the adjacent-pair terms and the cube terms are symmetric under p and q. A common-edge triple or a corner triple gives the same eta at all three output faces. For a path triple with nonadjacent p,q, both are endpoints and again give the same eta. It remains to examine adjacent p,q.

Let m_pq be the number of their common adjacent faces. A third face adjacent to p but not q, and different from p,q, can be chosen in exactly d_p-1-m_pq ways. These paths mark p as center and q as endpoint. A third face adjacent to q but not p can be chosen in exactly d_q-1-m_pq ways, with the roles reversed. Consequently

\[
\begin{aligned}
 (S_4)_{pq}-(S_4)_{qp}
 &=-6\bigl[(d_p-1-m_{pq})-(d_q-1-m_{pq})\bigr](h_c-h_e)\\
 &=-6\left(\frac{19}{3032640}-\frac{19}{59136480}\right)
       (d_p-d_q)\\
 &=-\frac{703}{19712160}(d_p-d_q)
 \qquad(p\sim q). \tag{A5}
\end{aligned}
\]

For nonadjacent p,q the difference is zero. In the actual original Haar-orthonormal face basis,

\[
 S_4-S_4^t=-\frac{703}{19712160}(D_{\rm deg}A_{\rm adj}-A_{\rm adj}D_{\rm deg}), \tag{A6}
\]

which is exactly Q30. The order of the two matrix products and its sign have both been checked. Finite boundary degrees are used throughout.

## A3. Separate absolute row and column bounds

The original infinite-coordinate face graph has twelve neighbors of a fixed face p: each of its four edges has three other incident faces, and no distinct face shares two edges with p. A triangle through p has either a common edge or three distinct pairwise shared edges at one vertex of p. In the common-edge case, choose one of the four edges of p and two of the other three incident faces, giving 4 times binomial(3,2)=12. In the distinct-edge case, choose one of the four vertices of p; the two additional faces use its two face directions and the perpendicular direction with a common positive or negative displacement. This gives 4 times 2=8. No triangle arises from opposite edges of p, since the other two faces then cannot share an edge.

There are therefore 20 adjacent pairs among the twelve neighbors. A path with center p selects an unordered nonadjacent pair of them:

\[
 N_c=\binom{12}{2}-20=46.
\]

A path with endpoint p selects a central neighbor q and then a neighbor r of q different from p and nonadjacent to p. There are 12 times 11 candidates before excluding the triangles. Each of the twenty triangles appears twice, once for either possible q. Hence

\[
 N_e=12\cdot11-2\cdot20=92. \tag{A7}
\]

These are exact counts in the same original face graph, not counts after any boundary completion. Every finite box supplies a subset of these configurations. Each face lies in at most two contained cubes, and each cube supplies five distinct other-face columns or rows.

Retain s=-19/1296, a=15163/15769728 and b_0=347/438048. For a fixed output row, a marked triple contributes 3|eta| in the diagonal column and 6|eta| in each of its other two columns. This gives

\[
 B_{\rm row}=|s|+12(|a|+|b_0|)
 +15(46|h_c|+92|h_e|+12|h_m|+8|h_k|)+30d. \tag{A8}
\]

For a fixed input column, a path marking that input as center has diagonal contribution 3h_c and two endpoint-output contributions 6h_e each. A path marking that input as endpoint has diagonal contribution 3h_e, one other-endpoint output contribution 6h_e and one center-output contribution 6h_c. Here h_c,h_e are positive as displayed in Q20. The common-edge and corner triples contribute 15 times their respective absolute coefficients. Thus

\[
\begin{aligned}
 B_{\rm col}={}&|s|+12(|a|+|b_0|)
 +46(3h_c+12h_e)+92(9h_e+6h_c)\\
 &+15(12|h_m|+8|h_k|)+30d.
\end{aligned} \tag{A9}
\]

The path terms in (A9) equal 690h_c+1380h_e, which are exactly 15(46h_c+92h_e). The two bounds are consequently the same rational number. Substitution without suppressing any term gives

\[
\begin{aligned}
 B_{\rm row}=B_{\rm col}
 ={}&\frac{19}{1296}
 +12\left(\frac{15163}{15769728}+\frac{347}{438048}\right)\\
 &+15\left(46\frac{19}{3032640}+92\frac{19}{59136480}
 +12\frac4{616005}+8\frac{164}{6283251}\right)
 +30\frac{107}{34992}\\
 ={}&\frac{4574447}{33510672}<\frac{137}{1000}.
\end{aligned} \tag{A10}
\]

Each finite box removes configurations from sums of nonnegative absolute bounds, so both bounds remain valid independently of L. For any original face coefficient vector z, weighted Cauchy--Schwarz gives

\[
\begin{aligned}
 \sum_p\left|\sum_q(S_4)_{pq}z_q\right|^2
 &\le\sum_p\left(\sum_q|(S_4)_{pq}|\right)
             \left(\sum_q|(S_4)_{pq}|\,|z_q|^2\right)\\
 &\le B_{\rm row}B_{\rm col}\sum_q|z_q|^2.
\end{aligned}
\]

Since the original face traces are orthonormal in Haar measure, this proves the stated assembled Haar-operator bound in Q35. It does not assert a bound in the different original union-labelled local norm.

## A4. Independent exact implementation check

`check_fourth_algebra.py` imports none of the parent's source or geometry modules. It constructs each face from its four original positive edges and constructs its neighbors by listing the faces containing each of those edges. It independently obtains the counts (46,92,12,8).

For the L=2 open box it builds the 28,596 displayed Q20 monomials on 240 original faces, retaining their input exponents and output face. Literal rational differentiation gives G_4; adding P/81 and subtracting G_4 gives S_4. A separate geometric construction from the proposed entry formula gives the identical matrix. There are 9,660 nonzero entries and 1,440 nonzero ordered antisymmetric entries, and every entry satisfies (A6). The independent construction uses 1,128 unordered adjacent pairs, 7,820 connected triples, and 64 contained cubes.

The actual maximum absolute row sum in this finite box is 6471173/67021344; the actual maximum absolute column sum is 8064839/83776680. They are different, as permitted by the nonsymmetry, and both satisfy (A10). These finite-box values are checks, not replacements for the uniform bounds just proved. The boundary example in Q31 is also reproduced exactly, including its degree pair (6,10) and antisymmetric entry 703/4928040.
