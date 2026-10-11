# Independent ordered Wilson-action derivation and source review

This review checks OW1–OW23, including the preceding subsequent zero-circulation and positive-defect strengthenings. It reads Sourav Chatterjee's original author TeX, arXiv:1602.01222v6, especially lines 230–248, 781–811 and 1756–1888. It neither reads nor applies the full free-energy proof. The exact downloaded source is identified in ACTUAL_LIMIT_SOURCE_USE_LEDGER.json. The complete original source version and reading coverage are retained in ACTUAL_LIMIT_SOURCE_USE_LEDGER.json.

The coefficients, signs, global integral remainders, exponential chart, full CW configuration potential, and original-path constants of OW1–OW20 are correct in their stated scopes. The original author source has two printed path defects; their correction is included in OW1–OW4. The complete derivations and two further bounds follow.

## 1. What the author source actually prints

Write \(z=x\), \(u=x+e_j\), \(v=x+e_j+e_k\), \(w=x+e_k\). The original Wilson face in author lines 235–238 is the ordered cycle \(z,u,v,w,z\). However, its printed additive definition at lines 1761–1762 is
\[
 H(z,u)+H(u,v)+H(v,u)+H(u,z)=0.
 \tag{UR1}
\]
This is a backtracking path and vanishes by the stipulated antisymmetry of every reverse edge. Its printed Taylor product at line 1832 follows the same backtracking sequence. In contrast, the four matrices at lines 1848–1851 use the genuine face:
\[
 H_1=H(z,u),\quad H_2=H(u,v),\quad
 H_3=H(v,w),\quad H_4=H(w,z).
 \tag{UR2}
\]
Thus the intended map is determined internally by the author's original Wilson definition and the later four matrices. Both printed occurrences of the penultimate vertex \(u\) must be \(w\). This is a correction of the written path, not a commutation or approximation.

For an exact counterexample to the lemma with its literal printed additive definition, set \(H(z,u)=\operatorname{diag}(x,-x)\), let all other positive face matrices be zero, and impose the original reverse-edge rule. The genuine Wilson defect is \(2-2\cos x\), while (UR1) is zero. The maximum Hilbert–Schmidt edge norm is \(\eta=\sqrt2|x|\). Consequently
\[
 \frac{2-2\cos x}{\eta^3}
 \sim\frac{1}{2\sqrt2|x|}\longrightarrow+\infty
       \quad(x\longrightarrow0,\ x\ne0).
 \tag{UR3}
\]
The displayed source lemma therefore cannot hold with the backtracking definition. This identifies a local written defect; it does not assert failure of the intended theorem or of the paper's main free-energy result.

There is also the separate nonunitarity issue at lines 1843–1844. For any square matrix \(R\),
\[
 \frac12\|I-R\|_{\rm HS}^2
 =r-\operatorname{Re}\operatorname{Tr}R
          +\frac12\operatorname{Tr}(R^*R-I).
 \tag{UR4}
\]
For the literal backtracking Taylor product in the example above,
\(R_{\rm back}=(1+x^4/4)I\). Hence
\(\phi(R_{\rm back})=-x^4/2\) and
\(\frac12\|I-R_{\rm back}\|_{\rm HS}^2=x^8/16\).
The missing defect is \(x^4/2+x^8/16\). This verifies the nonunitarity criticism even before the path is repaired. After the path is repaired, the intended four-factor example \(R=I+iH_1-H_1^2/2\) gives precisely OW3's different defect \(x^4/4\).

## 2. Exact positive defect for every ordered quadratic Taylor product

Set \(Q_a=I+iH_a-H_a^2/2\) for the original four Hermitian matrices, and \(R=Q_1Q_2Q_3Q_4\), with no rearrangement. Let \(S_a=Q_{a+1}\cdots Q_4\), where \(S_4=I\). Direct multiplication gives \(Q_a^*Q_a=I+H_a^4/4\). Peeling off the first factor and iterating therefore proves
\[
 R^*R-I=\frac14\sum_{a=1}^4S_a^*H_a^4S_a,\qquad
 \Delta(R):=\frac12\operatorname{Tr}(R^*R-I)
     =\frac18\sum_{a=1}^4\|H_a^2S_a\|_{\rm HS}^2\ge0.
 \tag{UR5}
\]
Every suffix is in its original order. In particular every quadratic factor and their full product are expansive in the sense \(R^*R\ge I\). This is the exact object measured by the source's failed unitary identity.

For \(\|H_a\|_{\rm HS}\le\eta\), the elementary eigenvalue bounds give
\(\|H_a^2\|_{\rm HS}^2=\operatorname{Tr}H_a^4\le\eta^4\) and
\(\|Q_a\|_{\rm op}^2\le1+\eta^4/4\). Inserting them individually in (UR5), then summing the four suffix lengths, proves
\[
 0\le\Delta(R)\le
 \frac{\eta^4}{8}\sum_{k=0}^3(1+\eta^4/4)^k
 =\frac12[(1+\eta^4/4)^4-1].
 \tag{UR6}
\]
The final equality holds by continuity at \(\eta=0\). For a unitary \(P\), the exact repaired signed equation is
\[
 \phi(P)-\phi(R)
 =\tfrac12(\|I-P\|_{\rm HS}^2-\|I-R\|_{\rm HS}^2)+\Delta(R).
\]
Each \(Q_a\) is invertible because \(Q_a^*Q_a\ge I\). Thus each suffix is invertible, and the sum in (UR5) vanishes exactly when all four \(H_a\) are zero. This also checks the preceding final characterization in OW23. Thus, once the path is repaired, the additional defect is nonnegative and fourth order at small radius. This confirms that the intended cubic bound survives. OW4's direct trace bound is also valid and needs none of this intermediate unitary reasoning.

## 3. Ordered coefficients and a dimension-independent remainder bound

Retain \(P(t)=\prod_{a=1}^4e^{itH_a}\), in order, and \(\Phi(t)=r-\operatorname{Re}\operatorname{Tr}P(t)\). Differentiating each exponential gives exactly the multi-index sum OW5. The scalar multinomial formula proves OW6. Selecting total derivative degrees one, two and three gives
\[
 \begin{split}
 \Phi(0)&=\Phi'(0)=0,\\
 \frac{\Phi''(0)}2&=\frac12\operatorname{Tr}\Big(\sum_aH_a\Big)^2,\\
 \frac{\Phi'''(0)}6&=-\sum_{a<b<c}
                     \operatorname{Im}\operatorname{Tr}(H_aH_bH_c).
 \end{split}\tag{UR7}
\]
For the last line, \(P\)'s cubic coefficient is \(-iB_3\) with exactly OW7's full ordered polynomial. Hermitian-cube and repeated-factor traces are real; \(\operatorname{Re}(-iz)=\operatorname{Im}z\), and the minus sign in \(\Phi=r-\operatorname{Re}\operatorname{Tr}P\) gives the displayed negative sign. Four integrations of the fourth derivative give the exact OW8 remainder and the factor \(1/24\); three integrations give OW9 and \(1/6\). These bounds hold globally for all four Hermitian matrices.

There is a useful improvement for the general matrix statement. Define, retaining both norms,
\[
 q_{\rm op}=\sum_a\|H_a\|_{\rm op},\qquad
 q_{\rm HS}=\sum_a\|H_a\|_{\rm HS}.
\]
For \(k\ge2\), in each ordered differentiated product choose two of its \(k\) differentiated factors and use their Hilbert–Schmidt norms; use operator norms for the other \(k-2\) factors and all intervening unitary matrices. The inequality needed is
\(|\operatorname{Tr}(AUBV)|\le\|A\|_{\rm HS}\|B\|_{\rm HS}\|U\|_{\rm op}\|V\|_{\rm op}\), proved by the Hilbert–Schmidt inner-product inequality and submultiplicativity. Cyclicity places the chosen two factors in this form without interchanging any factors.

Index the product rule by its \(k\) derivative labels \(a_1,\ldots,a_k\), which gives each multi-index its correct multiplicity. Choose derivative labels one and two for the two Hilbert–Schmidt factors in every term. Summing their bounds now factors exactly, yielding
\[
 |\Phi^{(k)}(t)|
 \le\min\{r q_{\rm op}^k,\ q_{\rm HS}^2q_{\rm op}^{k-2}\},
 \qquad k\ge2,\quad t\in\mathbb R.
 \tag{UR8}
\]
If all four original Hilbert–Schmidt norms are at most \(\eta\), the quadratic remainder is bounded by \(32\eta^3/3\), independently of the matrix size, rather than \(32r\eta^3/3\). The fourth remainder is bounded by \(q_{\rm HS}^2q_{\rm op}^2/24\). In the traceless \(2\times2\) programme specialization, \(q_{\rm HS}=\sqrt2q_{\rm op}\), so this reproduces, and does not improve, OW14–OW15's stated constants.

## 4. Original SU(2) signs and the exact zero-circulation sector

Retain \(T_\alpha=-i\sigma_\alpha/2\), \(X(y)=\sum y^\alpha T_\alpha\), and \(H(y)=-y\cdot\sigma/2\). Thus \(iH(y)=X(y)\). Pauli multiplication directly gives
\[
 \operatorname{Tr}(H(y)H(z))=y\cdot z/2,\quad
 \operatorname{Tr}(H(y)H(z)H(w))=-i\,y\cdot(z\times w)/4.
 \tag{UR9}
\]
This verifies OW13 and the positive cubic coefficient in OW14. Since \(q_{\rm op}=\sum_a|y_a|/2\), the two remainder constants are
\(2q_{\rm op}^4/24=(\sum_a|y_a|)^4/192\) and
\(2q_{\rm op}^3/6=(\sum_a|y_a|)^3/24\).

Keep the original \(C=\sum_{a=1}^4y_a\), and put \(B=\sum_{a<b}y_a\times y_b\), in that order. Expanding \(C\cdot B\), contributions with a repeated index vanish. For each \(a<b<c\), its three contributions have signs \(+,-,+\), so
\[
 \sum_{a<b<c}y_a\cdot(y_b\times y_c)=C\cdot B.
 \tag{UR10}
\]
Under whole-face reversal \(y'_a=-y_{5-a}\), one has \(C'=-C\) and \(B'=-B\), preserving this scalar. A transposition of only two entries is different and changes the ordered triple sign in OW18. Multiplying the three original exponentials in OW18 gives scalar quaternion parts \(\cos^3(t/2)\mp\sin^3(t/2)\); their defects are exactly the two displayed expressions there.

On the precise subspace \(C=0\), set \(P(t)=\prod_ae^{tX(y_a)}\). Then \(P'(0)=0\). Expanding the second derivative, and using
\((\sum_aX_a)^2=0\), gives
\[
 P''(0)=\sum_aX_a^2+2\sum_{a<b}X_aX_b
       =\sum_{a<b}[X_a,X_b]=X(B).
 \tag{UR11}
\]
The original Lie-bracket convention is \([X(y),X(z)]=X(y\times z)\), as follows from the same Pauli identity. Hence \(P(t)=I+t^2X(B)/2+O(t^3)\). Because the full product is unitary, its exact defect is \(\frac12\|I-P(t)\|_{\rm HS}^2\). The fourth coefficient is therefore
\(\frac18\|X(B)\|_{\rm HS}^2=|B|^2/16\), with all lower coefficients zero. The exact fifth-order Taylor identity is
\[
 D(t)=\frac{t^4|B|^2}{16}
       +\frac1{24}\int_0^t(t-u)^4D^{(5)}(u)\,du,\qquad
 \left|D(t)-\frac{t^4|B|^2}{16}\right|
       \le\frac{|t|^5(\sum_a|y_a|)^5}{1920}.
 \tag{UR12}
\]
For either sign of \(t\), integrate the absolute fifth-derivative bound
\(2q_{\rm op}^5\) over the interval between zero and \(t\). This proves the preceding strengthening with its exact sign, norm, and constant. It is a deterministic statement on the specified original-coordinate subspace; it asserts no probability or vacuum concentration there.

If \(B=0\) as well, the matrix product itself starts at degree three. Its third-order integral bound gives the additional fully proved estimate
\[
 0\le D(t)\le\frac{|t|^6q_{\rm op}^6}{36}
      =\frac{|t|^6(\sum_a|y_a|)^6}{2304}.
 \tag{UR13}
\]
Indeed \(\|P(t)-I\|_{\rm op}\le|t|^3q_{\rm op}^3/6\), and
\(\frac12\|P(t)-I\|_{\rm HS}^2\le\|P(t)-I\|_{\rm op}^2\) for two-dimensional matrices. This follows from the exact two vanishing derivative conditions, not from replacing the original product by a logarithmic approximation.

## 5. Full CW configuration and the unchanged path

The retained CW42 field has commuting link matrices
\(U_1=I\), \(U_2(i,k,l)=e^{\pi iT/m}\),
\(U_3(i,k,l)=e^{\pi kT/m}\).
There are \(m^2n\) faces of each orientation, including all boundary faces. The full 12 and 23 products are \(e^{\pi T/m}\); every 13 product is \(I\). The face half-angle is \(\alpha=\pi/(2m)\). This gives exactly
\[
 W=4m^2n(1-\cos\alpha),\quad
 W_{\rm quad}=2m^2n\alpha^2,\quad
 -m^2n\alpha^4/6\le W-W_{\rm quad}\le0.
 \tag{UR14}
\]
Both scalar inequalities hold for all real \(\alpha\): use the second-order and fourth-order cosine integral bounds. Substituting the unchanged
\(m=2j^4\), \(n=2j^4+1\), \(b=10000j^2/\kappa_*\) gives
\[
 \begin{split}
 bW_{\rm quad}&=5000\pi^2j^2(2j^4+1)/\kappa_*,\\
 -10000\pi^4j^2(2j^4+1)/(384\kappa_*j^8)
        &\le b(W-W_{\rm quad})\le0,\\
 bW/j^6&\longrightarrow10000\pi^2/\kappa_*,\\
 j^2b(W-W_{\rm quad})&\longrightarrow-625\pi^4/(12\kappa_*).
 \end{split}\tag{UR15}
\]
The sixth cosine remainder contributes at most a constant times
\(j^2b\,m^2n\,\alpha^6=O(j^{-8})\) in the last limit, so it vanishes. This also verifies the precise full-boundary constants in OW20. They are configuration values, not actual-vacuum expectations.

The chart and expectation claims require no change to the Hamiltonian. The map
\(x\mapsto e^{X(x)}\) is injective for \(|x|<2\pi\), with image
\(SU(2)\setminus\{-I\}\), by the radius-two sine/cosine formula. The principal representatives are measurable and bounded, and their exceptional link sets are Haar-null and therefore actual-vacuum-null. Thus every term in OW17 is integrable with that choice. More generally the phrase “any selected representatives” in its expectation statement is read with measurability and finite fourth moments; arbitrary unbounded or nonmeasurable selections need not define those expectations. This qualification does not affect the explicitly supplied principal-chart construction.

No further result about the author's Euclidean Wilson Gibbs measure or the programme's Hamiltonian vacuum is used. The source corrections concern exact printed paths and a matrix identity, and the strengthening concerns ordered deterministic products only.


![The dimension-independent derivative bound and the exact sixth-order product estimate; UR8 and UR13.](ORDERED_WILSON_REVIEW.png)

The reproducible source draw_ordered_review.py records the exact norms and coordinate locus. The complete receiving calculation is [OW1–OW25](ORDERED_WILSON_ACTION.md).
