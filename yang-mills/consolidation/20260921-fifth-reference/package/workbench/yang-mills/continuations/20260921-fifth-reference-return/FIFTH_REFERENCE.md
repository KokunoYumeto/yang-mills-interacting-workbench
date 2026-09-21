# The complete fifth reference: original spin channels, a convergent correction, and physical energy

21 September 2026. This continues the actual Yang–Mills checkpoint in the cumulative volume/heat edition. The fifth coefficient catalogue is an input already calculated there. Here its complete signed channel action is evaluated for quantitative source control, then the entire remaining nonlinear equation is solved on an explicit disk. The Riemann attachments have no mathematical role in this calculation. The proof supplies written analytic arguments and exact finite certificates; it does not assert an independent external analytical review, a formal-assistant proof, historical priority, or a continuum mass gap.

## F1. Original coordinates, spaces, and coefficient norms

Fix an integer L>=2. The original vertices are {-L,...,L}^3, with every contained positively oriented nearest-neighbor edge e=(n,i) and every contained elementary face p=(n;i,j), i<j. Keep

\[
W_p=\operatorname{tr}\{U_i(n)U_j(n+e_i)U_i(n+e_j)^{-1}U_j(n)^{-1}\},\quad
T_a=-i\sigma_a/2,\quad X_{e,a}f=\left.\partial_t f(\ldots,e^{tT_a}U_e,\ldots)\right|_0.
\tag{F1}
\]

The physical Hilbert space is the invariant part of original product-Haar-probability L2, with all vertex transformations, including boundary vertices, included. The original operator is

\[
H_L=\kappa K+\kappa\xi(2M-S),\quad K=-\sum_{e,a}X_{e,a}^2,
\quad S=\sum_pW_p,\quad M=|\mathsf P_L|,
\quad\kappa=\frac{2g^2}{a},\quad\xi=\frac1{4g^4},\quad a,g>0.
\tag{F2}
\]

The physical operator domain is H2 and the form domain H1 on this compact product. Its smooth bounded potential preserves self-adjointness and compact resolvent. Write P_H f=int f dU, Q_H=I-P_H. For the actual positive ground vector psi,

\[
q_{H-E_0}(\psi f)=\kappa\int\psi^2\sum_i|X_if|^2dU.
\tag{F3}
\]

Integration by parts using H psi=E0 psi proves this identity. The modulus inequality, elliptic regularity and the maximum principle give a positive ground vector; (F3) gives uniqueness. Gauge transformations consequently fix this positive unit vector.

For the original product representation pi_j, with d_j=product_e(2j_e+1), retain

\[
A_j(f)=d_j\int f(U)\pi_j(U)^*dU,\quad
f=\sum_j\operatorname{Tr}(A_j(f)\pi_j),\quad
c_j=\sum_e j_e(j_e+1),\quad \|f\|_X=\sum_j\|A_j(f)\|_1.
\tag{F4}
\]

The norm on the right is an auxiliary coefficient estimate; the physical pairing remains (F3). Original Haar matrix-coefficient orthogonality proves the Fourier map and inverse. Decomposing a product representation with all multiplicities, pinching its coefficient matrix, and tracing its multiplicity spaces gives

\[
\|fh\|_X\le\|f\|_X\|h\|_X,
\qquad \|A_j(X_{e,a}f_j)\|_1\le j_e\|A_j(f_j)\|_1.
\tag{F5}
\]

Pinching is an average of unitary conjugations. For the partial trace, duality with Z tensor I, ||Z||<=1, proves contraction of trace norm. This proves the needed compact-group Fourier-algebra estimates directly; Eymard's Fourier algebra is the antecedent.

Each original coefficient also retains a finite edge label S containing its active representation support. Set

\[
\begin{split}
\|v\|_{\rm loc}&=\sup_a\sum_{S\ni a,j\ne0}c_j\|A_{S,j}\|_1,\\
m(v)&=\sup_a\sum_{S\ni a,j\ne0}\Big(\sum_ej_e\Big)\|A_{S,j}\|_1,\\
t(v)&=\sup_e\sum_{S\ni e,j\ne0}j_e\|A_{S,j}\|_1.
\end{split}\tag{F6}
\]

Assembly sums A_(S,j) over all labels containing supp(j). Its kernel consists exactly of the equations that these sums vanish. For each enlarged S, move its actual A_(S,j) to supp(j) and retain the two-entry relation (+A at S,-A at supp(j)). Reading the enlarged-label entries is the inverse decomposition on this kernel. Hence enlarged zero-function labels remain represented.

## F2. Gauge estimate and bilinear source

At each original vertex, a nonzero physical coefficient contains a singlet intertwiner. Grouping the j_e factor gives j_e<=sum_(f incident v,f!=e)j_f by the highest weight of the remaining tensor factors. For a fixed edge e={u,v}, the other edges at u,v have total spin J1>=2j_e. Their outer endpoints are distinct: a common endpoint would form a triangle in the original cubic graph. Summing their own singlet inequalities gives J1<=2J2, counting every further edge at most twice. Thus sum_f j_f>=j_e+J1+J2>=4j_e. Since j(j+1)>=(3/2)j at every nonzero half-integer,

\[
c_j\ge6j_e\quad\hbox{on physical blocks},\qquad
\sum_e j_e\le\frac23c_j,\qquad
m(v)\le\frac23\|v\|_{\rm loc},\quad t(v)\le\frac16\|v\|_{\rm loc}.
\tag{F7}
\]

This proves c_j>=3 on the nonconstant physical space. The fundamental elementary plaquette attains 3. Active bridges and open boundaries remain in this argument.

Define the original bilinear differential and its zero-Haar inverse,

\[
\Gamma(f,h)=\sum_{e,a}(X_{e,a}f)(X_{e,a}h),\qquad
B(f,h)=K^{-1}Q_H\Gamma(f,h).
\tag{F8}
\]

Every input pair retains its union label. Every removed Haar scalar is stored as a scalar energy contribution. Bounding anchors in each input separately, (F5) gives

\[
\|B(f,h)\|_{\rm loc}\le3\{m(f)t(h)+m(h)t(f)\}
\le\frac23\|f\|_{\rm loc}\|h\|_{\rm loc}.
\tag{F9}
\]

The factor three is the complete generator sum. The output c_j cancels exactly against K^{-1} on the nonconstant output. Two useful consequences are

\[
\|2B(q,\cdot)\|_{\rm loc\to loc}\le m(q)+4t(q),\qquad
\|2\Gamma(v,h)\|_X\le4t(v)\|Kh\|_X.
\tag{F10}
\]

The latter includes the full scalar output.

## F3. Orientation-resolved trace coefficient and its exact transport

Here is a new finite coefficient bound used before absolute summation. First regard each of the l occurrences in a trace word as an independent d-dimensional representation variable, with orientation signs s_i=+1 or -1. Replace each inverse by its actual invariant-dual transpose C pi(U)^T C^{-1}, where C is unitary (for fundamental SU(2), C is the alternating two-index matrix). These coefficient-side unitary matrices preserve the singular values. In the remaining integer index tensor, the cyclic trace indices r_i contribute

\[
A_{(b_i),(a_i)}=\sum_{r_1,\ldots,r_l}
\prod_i\mathbf1\{(a_i,b_i)=(r_i,r_{i+1})\text{ for }s_i=+1;
\ (a_i,b_i)=(r_{i+1},r_i)\text{ for }s_i=-1\},\quad r_{l+1}=r_1.
\tag{F11}
\]

Let 2k be the number of cyclic sign changes. At a vertex with equal consecutive signs, r_i appears once in a row and once in a column; this gives an identity factor. A + to - transition gives a two-row delta vector; a - to + transition gives a two-column delta vector. There are k of each, each of norm sqrt(d), and l-2k identity factors. Separate row and column permutations consequently give

\[
A^*A\text{ has nonzero eigenvalue }d^{2k}
\text{ of multiplicity }d^{l-2k},\qquad
\boxed{\|A\|_1=d^{l-k}.}
\tag{F12}
\]

Equivalently (A* A)^2=d^(2k)A* A and Tr(A* A)=d^l. This includes every original color sum. The checker constructs the actual integer matrices for all signs through length seven at d=2 and length five at d=3: 316 cases, with both complete matrix identities checked.

Repeated occurrences of a link are now identified by the diagonal compact-group homomorphism sending the one original U_e to its occurrence tuple. The representation on that tuple decomposes unitarily with all multiplicities. The pinching and partial-trace argument of (F5) proves that this actual pullback contracts the Fourier trace norm. Thus 2^(l-k) is a rigorous upper bound for an original fundamental trace word, and products multiply these bounds.

The original lattice coordinate transport is y_i=epsilon_i x_(pi(i))-d_i, with inverse x_(pi(i))=epsilon_i(y_i+d_i). It sends the original U_e to the mapped U or its inverse according to orientation. The underlying physical Haar norm and Casimir intertwine through that map. For the coefficient estimate, instead of assigning invariance to every partial transpose, we explicitly retain all eight sign reflections. For an original trace polynomial P=sum_m c_m product_(w in m)Tr(w), put

\[
\mathfrak b(P)=
\max_{\epsilon\in\{\pm1\}^3}
\sum_m|c_m|\,2^{\sum_{w\in m}(|w|-k_\epsilon(w))}.
\tag{F13}
\]

Here k_epsilon(w) counts half the cyclic sign changes after the original axis reflection. The axes permutation only relabels the three reflected coordinates. This proves a bound simultaneously on every original signed transport. Every nonempty closed cubic word has both signs after any reflection, since its net displacement in each coordinate is zero. Hence k_epsilon>=1 and (F13) is at most the preceding length-only sum sum_m|c_m|2^(total length-number of traces).

For clarity, on four independent factors, partial transpose of the last two tensor coordinates sends the all-positive coefficient matrix of trace norm 16 to the ++-- matrix of trace norm 8. The executable checks this exact map and both costs. No norm identity under that partial transpose is inserted.

## F4. Full fifth-source inputs and signed spin-channel recurrence

The preserved fifth catalogue contains 662 representatives, 124864 anchored original multisets and 14063 rational trace-monomial terms. Every coefficient v_nu has its complete original edges, words and multiplicities. The original coefficient equation is

\[
v_1=\frac13\sum_pW_p,\quad
v_n=\sum_{i=1}^{n-1}B(v_i,v_{n-i}),\qquad
v_5=2B(v_1,v_4)+2B(v_2,v_3).
\tag{F14}
\]

For 321 of the fifth representatives all five faces are distinct and each original edge occurs at most twice. Let E_s be the repeated edges; each carries final spin b_e=0 or 1. A singly occurring edge carries 1/2. For a subset A of those five faces, let r_e(A) count its original occurrences and define

\[
c_b(A)=\sum_{r_e(A)=1}\frac34+
\sum_{r_e(A)=2}b_e(b_e+1).
\tag{F15}
\]

The complete admissible spin assignments retain every original vertex singlet constraint. For c_b(A)>0 define

\[
a_b(\{p\})=\frac13,\qquad
a_b(A)=\frac1{2c_b(A)}
\sum_{\varnothing\ne B\subsetneq A}
[c_b(B)+c_b(A\setminus B)-c_b(A)]a_b(B)a_b(A\setminus B).
\tag{F16}
\]

The empty coefficient and zero-Casimir coefficient are zero in the zero-Haar source. For these distinct-face proper subsets there is no nonempty closed surface. Each intermediate shared edge has either the same final pair of fundamental occurrences, or one fundamental occurrence. Therefore its pair projector and its actual intermediate Casimir intertwine with the final projector. Projectors on different edges commute. Applying

\[
2\Gamma(f,h)=(c_f+c_h)fh-K(fh)
\tag{F17}
\]

to every ordered input split proves

\[
\boxed{v_\nu=\sum_b a_b(A_{\rm all})P_b\prod_{p\in A_{\rm all}}W_p.}
\tag{F18}
\]

Every scalar in (F16) is evaluated as a rational number before taking its absolute value. The formula retains all input orderings and zero channels. Complete original quaternion polynomial identities verify (F18) against the inherited fifth coefficient for all 321 representatives, rather than testing only values at selected configurations.

For a set Z of repeated edges,

\[
P_{0,Z}=\prod_{e\in Z}(I-E_e/2),\qquad E_e=-\sum_aX_{e,a}^2.
\tag{F19}
\]

This is the original spin-zero projector on the degree-two occurrence space. Let x_b be the nonnegative trace norm of the coefficient block of P_b product W_p. Pinching into the complete edge-spin blocks gives

\[
\sum_{b:\ b_e=0\ (e\in Z)}x_b
=\|P_{0,Z}\prod_pW_p\|_X
\le\mathfrak b(P_{0,Z}\prod_pW_p).
\tag{F20}
\]

Each right side is calculated from the complete projected trace polynomial and all eight reflection bounds. The 321 families contain 6240 such constraints; 3498 are strictly tighter than their length-only predecessors.

The three objective families are

\[
\sum_b|a_b|c_bx_b,\quad
\sum_b|a_b|(\sum_ej_e(b))x_b,\quad
\sum_b|a_b|j_e(b)x_b\quad\text{for every original edge }e.
\tag{F21}
\]

Each supplied rational dual lambda>=0 satisfies A^T lambda>=the actual objective and has cost b^T lambda. Hence its cost bounds that objective for the actual x. The records also give feasible primal vectors with the same value. A separate auditor reconstructs the constraints, objectives, original Casimirs and polynomial projections, then verifies all 5726 primal/dual certificates without invoking the optimization solver. They certify bounds on the actual coefficients, not an assumption that the actual coefficient masses attain the finite polytope maximum.

## F5. The remaining original configurations and complete anchored return

For every ordered split of a fifth multiset into original submultisets A,B, the complete cubic channel polytopes and the exact saved fourth coefficients give

\[
\|B(v_A,v_B)\|_{\rm loc,one\ label}
\le3\sum_e t_e(v_A)t_e(v_B).
\tag{F22}
\]

For a (2,3) split the record also maximizes the full bilinear expression over the two actual finite input-channel polytopes. Its variables, original edge spins, signed scalar coefficients and all polytope vertices are retained in the inherited channel source. For a (1,4) split, t_e(v_1)=4/3 on that face; hence the sharper joint bound is

\[
4\sup\left\{\sum_j\sum_{e\in\partial p\cap\operatorname{supp}B}
 j_e\|A_j(v_B)\|_1\right\}.
\tag{F23}
\]

This simultaneous edge objective is evaluated on the actual fourth channel polytope where available. On every fourth row it is bounded as well by its saved local-Casimir bound times max_j(sum_selected j_e/c_j), by the complete raw trace estimate, and by the sum of its saved individual edge bounds. For a repeated single face its complete spin-one and spin-two characters give the additional exact coefficient-norm bound. Each of these is a bound on the same scalar objective, so the minimum of the scalar upper bounds is valid.

Summing every ordered split proves an upper bound C_nu for the actual fifth coefficient on its original union. Its total and marked-spin bounds also follow from the full admissible output-spin list:

\[
m_\nu\le C_\nu\max_j\frac{\sum_ej_e}{c_j},\qquad
t_{\nu,e}\le C_\nu\max_j\frac{j_e}{c_j}.
\tag{F24}
\]

The complete inherited trace expression supplies independent raw upper bounds; the explicit one-face fifth character supplies its own further bound. On the 321 rows of F4, the complete signed channel objectives (F21) are also used. Thus all 662 rows are covered, including the other 341 original multiplicity/shared-edge configurations. No generic distinct-face recurrence is applied to an edge with three or more occurrences.

The original anchor is the edge from (0,0,0) to (1,0,0). For every one of the 124864 original anchored multisets the saved signed-coordinate map sends both endpoints into the representative edge set. Summing that representative's actual marked-edge bound, rather than a freely selected representative edge, proves

\[
\begin{split}
\|v_5\|_{\rm loc}&\le
\frac{1141532378446937587064431}{460877915422606500}<2476866,\\
m(v_5)&\le
\frac{6682496758630785752687413327666759}{4077966203261057899505463750}<1638684,\\
t(v_5)&\le
\frac{126023896114060026308152742875366210205679497747117260778732756243249}
{662840019461690772503734890389307666881000651173392960000000000}<190128.
\end{split}\tag{F25}
\]

Every boundary box uses a subset of these original labels, so the same bounds hold independently of L. The complete per-row and per-anchor sums are in generated/rows and generated/fifth_budgets.json. The 124864 coordinate transports and full fifth-source polynomials are preserved in the preceding directory.

## F6. Full fifth-reference residual, inverse, and nonlinear correction

For the following closed formulas use the proved upward bounds

\[
\begin{split}
(m_1,t_1)&=(64/3,16/3),\\
(m_2,t_2)&=(5834/39,137/6),\\
(m_3,t_3)&=(336572872/208845,225985217/1253070),\\
(m_4,t_4)&=(17270702970768271/341697152160,
110695177857394584026401/18025447358750832000),\\
(m_5,t_5)&=(1638684,190128).
\end{split}\tag{F26}
\]

Each coefficient is a bound on the same original source norms in F6. Set q5=sum_(i=1)^5 xi^i v_i. Its complete residual is

\[
\begin{split}
R_5={}&\xi v_1+B(q_5,q_5)-q_5\\
={}&\xi^6[2B(v_1,v_5)+2B(v_2,v_4)+B(v_3,v_3)]\\
&+\xi^7[2B(v_2,v_5)+2B(v_3,v_4)]\\
&+\xi^8[2B(v_3,v_5)+B(v_4,v_4)]
+2\xi^9B(v_4,v_5)+\xi^{10}B(v_5,v_5).
\end{split}\tag{F27}
\]

No coefficient above degree five is treated as zero. Define

\[
b_{ij}=3(m_it_j+m_jt_i),\quad
\ell(x)=\sum_{i=1}^5(m_i+4t_i)x^i,\quad
\delta(x)=\sum_{\substack{1\le i,j\le5\\i+j\ge6}}b_{ij}x^{i+j},\quad
\mathscr D(x)=(1-\ell(x))^2-\frac83\delta(x).
\tag{F28}
\]

All coefficients of ell and delta are positive. On [0,19/1000], ell<1, so D'= -2(1-ell)ell'-(8/3)delta'<0. The signs at 18/1000 and 19/1000 are opposite. Therefore there is exactly one root alpha in that interval and it is the first positive root. Exact rational bisection and integer-square bounds give

\[
\begin{split}
0.018424953576117616681&<\alpha<0.018424953576117616682,\\
3.683551983985727304439&<\frac1{2\sqrt\alpha}
<3.683551983985727304440.
\end{split}\tag{F29}
\]

For any complex |xi|<=alpha, J5=2B(q5,.) satisfies ||J5||<=ell<1. Thus L5=I-J5 has the actual bounded inverse sum_(n>=0)J5^n, on the original local labelled source. The full correction w=v-q5 solves

\[
L_5w=R_5+B(w,w).
\tag{F30}
\]

Put w1=L5^{-1}R5 and w_n=L5^{-1}sum_(i+j=n)B(w_i,w_j). Its nth norm is bounded by Cat_(n-1)[(2/3)/(1-ell)]^(n-1)[delta/(1-ell)]^n. This complete series converges even at the endpoint, and

\[
\boxed{\|w\|_{\rm loc}\le w_*(x)
=\frac34[1-\ell(x)-\sqrt{\mathscr D(x)}],\qquad x=|\xi|\le\alpha.}
\tag{F31}
\]

With theta=8delta/[3(1-ell)^2]<=1, its omitted tree orders satisfy

\[
\left\|\sum_{n>N}w_n\right\|_{\rm loc}
\le\frac34(1-\ell)\theta^{N+1}\frac{\binom{2N}{N}}{4^N}
\le\frac34(1-\ell)\frac{\theta^{N+1}}{\sqrt{N+1}}.
\tag{F32}
\]

The identity Cat_N/4^N=2[binom(2N,N)/4^N-binom(2N+2,N+1)/4^(N+1)] proves the tail exactly; the central binomial bound follows by induction after squaring. Thus the endpoint uses an explicit convergent tail rather than a strict endpoint contraction.

On every finite graph, the total c-weighted coefficient sum is at most |E_L| times the local norm. First and second derivatives converge because j_e and j_e j_f are bounded by constant multiples of c_j. The assembled source therefore solves

\[
Kv=\xi S+\Gamma(v,v)-P_H\Gamma(v,v).
\tag{F33}
\]

For real xi, exp(v) is positive and gives

\[
\psi=e^{v+c_L},\quad c_L=-\frac12\log\int e^{2v}dU,
\quad E_0=2\kappa M\xi-\kappa P_H\Gamma(v,v).
\tag{F34}
\]

Substitution into the original H gives its exact eigen-equation. Equation F3 proves this eigenvalue is the bottom, and uniqueness identifies the actual vacuum. Elliptic bootstrapping gives all higher derivatives. For complex xi the same nonzero exponential solves the complex equation; the mean functional and its nonvanishing denominator are proved in the heat companion.

## F7. Actual physical spectral and primitive return

Let t_* =sum_i t_i x^i+w_*/6 and chi=4t_*. Equations F10 and F31 give ||2Gamma(v,h)||X<=chi||Kh||X. Direct algebra, with every term retained, yields

\[
\boxed{d_5(x)=3(1-\chi)
=\frac32(1+\sqrt{\mathscr D(x)})
+\sum_{i=1}^5(\tfrac32m_i-6t_i)x^i.}
\tag{F35}
\]

Every last coefficient is nonnegative; 0<=chi<1/2 on [0,alpha]. The correction w_* increases on the open interval because differentiation of (1-ell)w-(2/3)w^2=delta gives w'=(delta'+ell'w)/sqrt(D)>0. Therefore chi increases and d5 decreases to its positive endpoint.

Take an actual positive-energy physical eigenvector of H-E0. Division by psi, then subtraction of its Haar scalar, gives a nonzero smooth h with

\[
(K-\lambda/\kappa)h=Q_H2\Gamma(v,h).
\tag{F36}
\]

Smoothness implies sum_j c_j||A_j(h)||1<infinity: Plancherel and Cauchy--Schwarz with a sufficiently high original Casimir power give this on the finite compact product. For 0<lambda/kappa<3,

\[
\|(K-\lambda/\kappa)h\|_X
\ge(1-\lambda/(3\kappa))\|Kh\|_X.
\]

Combining with F35 proves lambda>=kappa d5. Values lambda/kappa>=3 satisfy the same bound since d5<=3. The complete compact physical spectral resolution consequently gives

\[
\boxed{\Delta_L\ge\kappa d_5(\xi),\qquad
q_{H-E_0}(\psi f)\ge\kappa d_5(\xi)\operatorname{Var}_{\psi^2}(f)}
\tag{F37}
\]

for every L>=2, a>0 and 0<xi<=alpha, on the whole physical form domain. In particular

\[
\begin{array}{c|c|c}
g^2\text{ at least}&\Delta_L/\kappa\text{ exceeds}&\|v-q_5\|_{\rm loc}\text{ below}\hline
37/10&1.6207&0.046581\\
15/4&1.6993&0.026352\\
4&1.9068&0.005752
\end{array}\tag{F38}
\]

The exact rational brackets, rather than these displayed rounded consequences, are in physical_return.json.

The approximate exponential retains its complete operator defect:

\[
e^{-q_5}He^{q_5}
=\kappa[K-2\Gamma(q_5,\cdot)]
+\kappa[2M\xi-P_H\Gamma(q_5,q_5)]I-\kappa M_{KR_5}.
\tag{F39}
\]

In particular, for the actual transformed operator Atilde,

\[
Q_H\widetilde Ah-\kappa KL_5h
=-2\kappa Q_H\Gamma(w,h),\qquad
\|\text{right side}\|_X\le\frac{2\kappa}{3}w_*\|Kh\|_X.
\tag{F40}
\]

Thus the reference linearization and physical operator have their exact comparison, including scalar and multiplication terms.

For source windows V_N=span{R5,J5R5,...,J5^N R5}, the actual complexes are V_N --L5--> V --0-->0. Inclusion and identity give their transitions. The map

\[
V_{N+1}/V_N\longrightarrow
\ker[V/L_5V_N\to V/L_5V_{N+1}],\quad [h]\mapsto[L_5h]
\tag{F41}
\]

has inverse induced by L5^{-1}: changing a representative by L5V_N changes its inverse by exactly V_N. The finite primitive sum_(j=0)^N J5^jR5 has residual J5^(N+1)R5. Its omitted norm is at most ell^(N+1)delta/(1-ell). Both the original relation and its support label remain.

On centered physical functions let d_X f=(X_if)_i with the original range pairing kappa int rho sum conjugate(v_i)w_i. The inverse on its actual image is p_X(d_X f)=f. Its uniqueness follows because all derivatives zero force a constant and centering fixes that constant. The exact variational identity is

\[
\boxed{\|p_X\|^2=1/\Delta_L\le1/[\kappa d_5(\xi)].}
\tag{F42}
\]

## F8. Sources and evidence

The original LaTeX was located at repository commit add590f78d0f6a1bdcc6e83cc9e0301cfc9b0f5d, yang-mills/consolidation/20260917/reader/yang_mills_quartic_cube_reader.tex. Its introductory original equations and six-appendix inventory were compared with the mounted source chain. No exhaustive new review of that whole LaTeX reader is claimed. The complete original fifth catalogue, fourth input channel bounds and prior heat proof are retained unchanged in this cumulative archive.

The explicit lower-order input polytopes occur in ../20260917-quartic-cube/channel_bounds.py and its QUARTIC_SOURCE.md/PHYSICAL_RETURN.md proof. The full fifth source is ../20260917-fifth-source/FIFTH_SOURCE.md and its generated catalogue. This continuation's new algebra checks F11--F25; the endpoint and physical-return arithmetic are separately replayed. Analytic Banach-space and elliptic arguments are written above, rather than represented as certified by finite matrix tests.

Human antecedents: D. Schuette, Zheng Weihong and C. J. Hamer, The Coupled Cluster Method in Hamiltonian Lattice Field Theory, arXiv:hep-lat/9603026v1, especially Sections 2--5, provide the exponential vacuum, character and Casimir framework. Their convention is connected by g_C=2^(3/4)g and H_ours=sqrt(2)H_C+2kappa xi M I, with their commutator derivative iX. P. Eymard, L'algebre de Fourier d'un groupe localement compact, Bull. Soc. Math. France 92 (1964),181--236, is the Fourier-algebra antecedent; the needed compact coefficient bounds are proved here. No human reference is asserted to verify the new finite catalogue or coupling threshold.
