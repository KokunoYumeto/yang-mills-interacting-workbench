# Gauge-native source bounds and the full physical excitation band

15 September 2026. This continuation starts from the original SU(2) Hamiltonian and the delivered `20260915-uniform-gap-zero-shift` source. Its new calculations use the vertex-gauge action before estimating the nonlinear source. All original links, spin labels, Fourier coefficients, physical energy factors, means, relation labels and vacuum scalar remain. `BAND_AND_CERTIFICATE.md` calculates the first physical band and its full second coefficient, with a uniform analytic remainder. `SPATIAL_RETURN.md` gives the unique spatial-volume return on the enlarged domain. The final enlarged source and volume domain is established in SECOND_SOURCE.md R1–16 using the actual second vacuum coefficient. These are written proofs, accompanied by exact finite verification. No four-dimensional continuum mass-gap conclusion, new Lean verification or literature-priority claim is made.

## G1. Original objects and the precise retained quotient

For integer L>=2 take the vertices {-L,...,L}^3, all positive contained nearest-neighbor links E_L, and all contained elementary plaquettes P_L with their original oriented four-link words W_p. Put

\[
 H_L=\kappa K_L+\kappa\xi\sum_{p\in P_L}(2-W_p),\quad
 K_L=-\sum_{e,\alpha}X_{e,\alpha}^{2},\quad
 \kappa=2g^2/a,\quad \xi=1/(4g^4),\quad a,g>0.                 \tag{G1}
\]

Here T_alpha=-i sigma_alpha/2 and X differentiates exp(t T_alpha)U_e. Product Haar probability, the scalar 2 kappa xi |P_L|, and the original physical invariant subspace are retained. Let psi_L>0 be the positive unit vacuum and E_0,L its actual energy. The original multiplication map

\[
 \mathcal U_L:L^2(\rho_LdU)\longrightarrow L^2(dU),\quad
 f\longmapsto\psi_Lf,\quad \rho_L=\psi_L^2
\]

is unitary, with inverse division by psi_L. Its transported form is

\[
 q_{\mathcal A_L}(f,h)=\kappa\int\rho_L\sum_{e,\alpha}
       \overline{X_{e,\alpha}f}X_{e,\alpha}h\,dU,
 \qquad \mathcal A_L=\mathcal U_L^{-1}(H_L-E_{0,L})\mathcal U_L. \tag{G2}
\]

On this finite compact group the operator and form domains are H^2 and H^1, respectively, with their invariant subspaces in the physical calculation. The positive smooth vacuum and the form identity are also proved directly in G8 for the constructed range of couplings.

For product-spin labels j=(j_e), keep

\[
 c(j)=\sum_ej_e(j_e+1),\quad
 f_j(U)=\operatorname{Tr}(A_j\pi_j(U)),\quad
 A_j=d_j\int f(U)\pi_j(U)^*dU.                              \tag{G3}
\]

The representation dimension d_j is part of the coefficient; the matrix trace norm below is that of A_j. Vertex-gauge averaging P_G acts on this original coefficient space, commutes with K_L, and preserves every j block and every local support. The exact quotient map is

\[
 \mathscr C/\operatorname{im}(I-P_G)\xrightarrow{\cong}
 \operatorname{im}P_G,\quad [f]\mapsto P_Gf,
 \quad h\mapsto[h].                                      \tag{G4}
\]

Indeed P_G^2=P_G by Haar multiplication, ker P_G=im(I-P_G), and f-P_G f is that displayed original relation. Each coefficient eliminated by the gauge map is still a vector in this kernel. Only its actual image is used in the next estimate.

## G2. A graph inequality on every nonzero physical Fourier block

At each vertex v of a nonzero physical block, its incident spins obey

\[
 j_e\le\sum_{f\ni v,\,f\ne e}j_f.                        \tag{G5}
\]

For a proof, a nonzero invariant tensor at v gives an intertwiner from V_{j_e} into the tensor product of the other incident representations, with duals for opposite orientations. SU(2) duals have the same spin. Irreducibility makes this intertwiner injective. The highest J_3 weight of the target is at most the sum of those other spins; the image contains weight j_e. This proves G5. A nonzero global Fourier invariant supplies such a local invariant at every vertex, by grouping its original incident matrix indices. Thus no separate spin-network ansatz is assumed.

Fix e={u,v}. Write E_1 for the other edges incident on u or v, and O for their other endpoints. The original cubic graph is simple and triangle-free, so these endpoints are distinct and none is u or v. Each w in O has exactly one edge of E_1 entering {u,v}. Put J_1=sum_{f in E_1}j_f. The two inequalities G5 at u and v give J_1>=2j_e. Summing G5 at the vertices of O gives J_1<=2J_2, where E_2 consists of edges incident on O outside {e} union E_1 and J_2=sum_{f in E_2}j_f. Each such edge is counted at most twice. Hence

\[
 \sum_f j_f\ge j_e+J_1+J_2\ge4j_e.
\]

Every nonzero half-integer spin satisfies j(j+1)>=(3/2)j. Consequently

\[
 \boxed{c(j)\ge6j_e\quad\hbox{for every edge e in every nonzero physical block}.}
                                                               \tag{G6}
\]

The constant 6 is attained by a spin-1/2 elementary plaquette. The separate estimate

\[
 \sum_ej_e\le(2/3)c(j)                                   \tag{G7}
\]

continues to hold for arbitrary product-spin labels, including nonphysical ones. G6 and G7 have different specified domains and will be used at their respective places.

In particular every nonconstant physical block has c(j)>=3. If c(j)<9/2, its active support has at most five edges. No active vertex can have valence one by G5. A finite subgraph with at most five edges and no vertices of valence one in the cubic lattice is a four-cycle: it contains a cycle, the lattice has no triangle or odd cycle, and a fifth edge cannot have both endpoints on a four-cycle without producing a chord absent from the nearest-neighbor lattice. Every four-cycle is an elementary plaquette. The two-edge vertex invariants force the four spins to coincide. Their Casimir is 4j(j+1), equal to 3 at j=1/2 and at least 8 at j>=1. Thus

\[
 \operatorname{spec}(K_L|_{\mathrm{phys}})\subset
 \{0,3\}\cup[9/2,\infty),\qquad
 \ker(K_L-3)=\operatorname{span}\{W_p:p\in P_L\}.          \tag{G8}
\]

At a two-edge spin-1/2 vertex the invariant contraction is unique up to its scalar; following the four actual indices gives W_p. Different p have orthogonal product-spin blocks, and int_H W_p W_q=delta_pq. This proves both equality in the eigenspace statement and its dimension |P_L|.

## G3. The original coefficient source with all relation labels retained

For every nonempty finite edge label S retain a zero-Haar-mean physical function f_S with coefficients A_(S,j), including j whose active support is strictly smaller than S. Define

\[
 \|f\|_{\mathrm{loc},1}
 =\max_e\sum_{S\ni e}\sum_{j\ne0}c(j)\|A_{S,j}\|_1.     \tag{G9}
\]

This is an auxiliary absolute-convergence norm, on the SAME coefficient families as the predecessor. On each finite graph its identity map to the predecessor's weight-5/4 source has both inverse maps and bounds

\[
 \|f\|_{\mathrm{loc},1}\le\|f\|_{\mathrm{loc},5/4}
 \le(5/4)^{|E_L|}\|f\|_{\mathrm{loc},1}.                 \tag{G10}
\]

The volume-dependent comparison is recorded and is never used to assert a uniform bound. The physical pairing is still G2.

Assembly takes A_(S,j) to sum_{S containing supp(j)} A_(S,j). Its kernel is the original coefficient equation that this sum is zero for every j. The relation (B at (S,j))-(B at (supp(j),j)) and the actual coefficient at every S strictly containing supp(j) reconstruct that whole kernel, exactly as in predecessor U9-11. The physical subspace is preserved under this relation. Zero assembly therefore retains the original relation primitive, rather than deleting its supports.

The coefficient product and derivative bounds used here are

\[
 \sum_\ell\|A_\ell(f_jh_k)\|_1\le\|A_j\|_1\|B_k\|_1,
 \qquad\|A(X_{e,\alpha}f_j)\|_1\le j_e\|A_j\|_1.        \tag{G11}
\]

For completeness, the product is Tr((A_j tensor B_k)(pi_j tensor pi_k)). Unitary decomposition into the complete irreducible/multiplicity spaces, pinching to diagonal blocks, and partial trace over multiplicity give its exact output coefficients. Pinching is an average of unitary conjugations. For partial trace, trace-norm duality bounds Tr((Z tensor I)C) by ||C||_1 for ||Z||op<=1. These facts prove the first bound, retaining all output labels. The second follows from the original spin generator norm ||J_alpha||=j and trace-norm duality. All three alpha values remain.

Let Q_H remove only the trivial Haar coefficient. Define the original bilinear source

\[
 \mathcal B(f,h)_S=K_L^{-1}Q_H
 \sum_{S_1\cup S_2=S}\sum_{e,\alpha}
                  (X_{e,\alpha}f_{S_1})(X_{e,\alpha}h_{S_2}). \tag{G12}
\]

The scalar removed at each S is recorded separately. The active product support may become smaller, but the original union label S is retained.

For an anchor a in S_1, G6 on the h block and G7 on f give

\[
 3\sum_{S_1\ni a,j}\|A_{S_1,j}\|_1
       \sum_e j_e\sum_{S_2\ni e,k} k_e\|B_{S_2,k}\|_1
 \le\frac13\|f\|_{\mathrm{loc},1}\|h\|_{\mathrm{loc},1}.
\]

Interchanging f,h gives the other anchor contribution. Counting the overlap twice is an upper bound. The output c(j) cancels the exact inverse Casimir in G12, and therefore

\[
 \boxed{\|\mathcal B(f,h)\|_{\mathrm{loc},1}
           \le(2/3)\|f\|_{\mathrm{loc},1}\|h\|_{\mathrm{loc},1}.} \tag{G13}
\]

G13 is on the gauge-invariant source. Its proof retains the generator sum, graph constraints, and all representation multiplicities.

## G4. Exact plaquette coefficient, convergent source, and the closed endpoint

For the original word Tr(U1 U2 U3^-1 U4^-1), its complete 16 by 16 coefficient in G3 is

\[
 A_{(i_1,i_2,1-i_2,1-i_3),(i_0,i_1,1-i_3,1-i_0)}
       \mathrel{+}=(-1)^{i_0+i_2},\qquad i_0,i_1,i_2,i_3\in\{0,1\}. \tag{G14}
\]

All other entries are zero. The inverse-entry formula (U^-1)_(r,c)=(-1)^(r+c)U_(1-c,1-r) proves the identity in the original coordinates. The four disjoint two-row/two-column blocks have the entries [[1,-1],[-1,1]], with the remaining rows and columns unused. Thus (A* A)^2=4A* A and Tr(A* A)=16. The positive square root is (A* A)/2, giving ||A||_1=8. This independently reproduces predecessor O1-2.

The first source is v_[1]=(1/3)sum_p W_p, with its actual four-link labels. At most four plaquettes meet an edge, so

\[
 \|\xi v_{[1]}\|_{\mathrm{loc},1}\le32\xi.               \tag{G15}
\]

Use the full coefficient recurrence

\[
 v_{[p]}=\sum_{i=1}^{p-1}\mathcal B(v_{[i]},v_{[p-i]}),\quad
 v(\xi)=\sum_{p\ge1}\xi^p v_{[p]}.
\]

With C_n=(2n)!/(n! (n+1)!), G13 proves

\[
 \|\xi^p v_{[p]}\|_{\mathrm{loc},1}
 \le a_p(\xi):=C_{p-1}(2/3)^{p-1}(32\xi)^p.             \tag{G16}
\]

The original union recurrence also gives |S|<=3p+1, connected support, and j_e<=p/2 at order p. These are exact support facts, not alterations of any coefficient.

Set

\[
 \theta=256\xi/3,\quad
 r(\xi)=\frac34(1-\sqrt{1-\theta}),\quad
 \epsilon(\xi)=\frac23r(\xi)=\frac{1-\sqrt{1-\theta}}2.  \tag{G17}
\]

For 0<=theta<1 the Catalan recurrence proves sum_p a_p=r and

\[
 \sum_{p>P}a_p\le\frac{32\xi\theta^P}{1-\theta}.         \tag{G18}
\]

At the endpoint xi=3/256 the series still converges absolutely. The complete scalar tail there is

\[
 \sum_{p>P}a_p(3/256)
   =\frac34\frac{\binom{2P}{P}}{4^P}
   \le\frac{3}{4\sqrt{P+1}}.                            \tag{G19}
\]

To verify the exact equality, put b_P=binom(2P,P)/4^P. Then C_P/4^P=2(b_P-b_(P+1)). Telescoping and b_P->0 give the formula. The bound b_P<=1/sqrt(P+1) follows by induction from ((2P+1)/(2P+2))^2<=(P+1)/(P+2). It also proves b_P->0 without an asymptotic substitution.

For every finite box G9 is complete, and its total c-weighted coefficient sum is at most |E_L| times G9. G11 bounds the original first and second derivatives by that total. Absolute convergence, including G19, therefore gives a C^2 function and permits G12 to be summed. The fixed equation is

\[
 K_Lv=\xi\sum_pW_p+\sum_i(X_iv)^2-C_L,\quad
 C_L=\int_H\sum_i(X_iv)^2.                               \tag{G20}
\]

All removed scalar coefficients are exactly included in C_L. Set

\[
 c_L=-\tfrac12\log\int e^{2v}dU,\quad
 \psi_*=e^{v+c_L},\quad
 E_*=2\kappa\xi|P_L|-\kappa C_L.                         \tag{G21}
\]

Equation G20 and direct differentiation prove H_L psi_*=E_* psi_*. The positive C^2 solution becomes smooth by elliptic bootstrapping. For every smooth h the product rule proves q_(H_L-E_*)(psi_*h)=kappa int psi_*^2 sum|Xh|^2. Multiplication and division by the positive smooth psi_* preserve H^1 on this compact finite group. Hence E_* is the actual lowest energy; dividing any other ground vector by psi_* proves uniqueness. This identifies G21 with the original vacuum, including its full scalar and Haar mass. The completed closed coupling domain is

\[
 \boxed{0<\xi\le3/256,\qquad g^2\ge8/\sqrt3.}           \tag{G22}
\]

No contraction constant smaller than one is asserted at theta=1; G19 supplies that endpoint directly.

## G5. A relative bound for the original drift, and the full physical gap

Let X_0 be the zero-Haar-mean Fourier algebra with norm sum_j ||A_j||_1; let Y_0 carry sum_j c(j)||A_j||_1. Use the physical subspaces when explicitly indicated. For a smooth zero-Haar-mean f, the same original coefficient product gives

\[
 \left\|Q_H\sum_i(X_iv)(X_if)\right\|_{X_0}
 \le 3\sum_k\|A_k(f)\|_1\sum_e k_e
        \sum_{S\ni e,j}j_e\|A_{S,j}(v)\|_1
 \le\frac r3\|f\|_{Y_0}.                                \tag{G23}
\]

Only v uses G6; f uses G7. Thus G23 also holds on the full scalar space. The complete relative perturbation -2 kappa Q_H sum (Xv)X has norm at most kappa epsilon from Y_0 to X_0.

Every smooth function on the finite product belongs to Y_0. One direct proof uses Peter-Weyl Plancherel, ||A_j||_1<=sqrt(d_j)||A_j||_HS, and Cauchy-Schwarz with sufficiently many original Casimir powers. The series sum_j d_j^2(1+c(j))^-M is finite for M>3|E_L|/2; elementary comparison of the product-spin sums proves it. Smoothness supplies all these powers. This step requires no uniform-in-volume regularity constant.

The coefficient projection Q_H is related to the original centered-vacuum space by the two inverse maps

\[
 f\mapsto Q_Hf,\quad y\mapsto y-\langle y\rangle_{\rho_L},
 \quad \langle f\rangle_{\rho_L}=0,\ \int_Hy=0.           \tag{G24}
\]

Both compositions are identities. They intertwine A_L with its literal Haar quotient

\[
 \overline{\mathcal A}_L
 =\kappa K_L-2\kappa Q_H\sum_i(X_iv)X_i.                 \tag{G25}
\]

For the inverse identity in the operator square, int rho_L A_L y=0 gives precisely the constant required in G24. No Haar mean is substituted for a vacuum mean.

Let A_L f=lambda f be a nonzero physical excitation, and y=Q_Hf. For 0<lambda<3kappa, G8 and G23 give

\[
 \|y\|_{Y_0}
 \le\frac{3\kappa\epsilon}{3\kappa-\lambda}\|y\|_{Y_0}.
\]

The vector is nonzero, so lambda>=3kappa(1-epsilon). Every finite-regulator eigenfunction is smooth by the original elliptic equation. Compact spectral resolution consequently extends the result to the whole physical form domain:

\[
 \boxed{\Delta_L\ge d_{\rm phys}(\xi)\kappa,
 \quad d_{\rm phys}=3(1-\epsilon)
       =\tfrac32(1+\sqrt{1-256\xi/3}).}                   \tag{G26}
\]

On the full scalar space replace the free value 3 by its original 3/4. The identical argument proves

\[
 \boxed{\Delta_L^{\rm scalar}\ge d_{\rm sc}(\xi)\kappa,
 \quad d_{\rm sc}=\tfrac34(1-\epsilon)=d_{\rm phys}/4.}   \tag{G27}
\]

The inclusion of the original physical subspace into the scalar space intertwines both Hamiltonians; G26 uses its explicitly computed free Fourier support G8. All physical states, including volume-dependent states, are covered by G26.

For example at every g^2>=5,

\[
 \Delta_L\ge\tfrac32(1+\sqrt{11/75})\kappa
             >2.07445\kappa.                            \tag{G28}
\]

In the original physical units the general bound is

\[
 \Delta_L\ge\frac{3g^2}{a}
          \left(1+\sqrt{1-64/(3g^4)}\right).             \tag{G29}
\]

## G6. The native primitive and the zero-shift response return

On centered physical H^1 define d_X f=(X_i f)_i with its ORIGINAL energy norm kappa int rho sum|X_i f|^2. The inverse on its actual range is p_X(d_X f)=f. The variational characterization, with the G2 unitary, proves

\[
 \|p_X\|^2=1/\Delta_L\le1/(\kappa d_{\rm phys}).          \tag{G30}
\]

This is the primitive of the original gradient window. G4 and the assembly relations retain the sources used to control it. The auxiliary Fourier source norm supplies the spectral estimate; it has not replaced either the physical state norm or the derivative energy norm.

For the predecessor's loop observation, gauge averaging commutes with the actual conditional expectation: change variables in its defining conditional-density integral and use the basepoint conjugation of the original loop holonomy. It therefore commutes with the form compression D. Let I:K_phys->K be the isometric inclusion of its physical reducing subspace. The domain and resolvent identities are

\[
 DI=ID_{\rm phys},\quad (D+s)^{-1}I=I(D_{\rm phys}+s)^{-1}.
\]

The actual forcing W=-Q_C A_L F and the displayed trial and residual are physical. Consequently their unchanged response pairing is

\[
 \langle W,D^{-1}W\rangle
 =\langle I^*W,D_{\rm phys}^{-1}I^*W\rangle,
 \quad \|D_{\rm phys}^{-1}\|\le1/(\kappa d_{\rm phys}).   \tag{G31}
\]

All predecessor minimum-section, quotient-residual and mixed-state identities now use this stronger proven inverse bound on their actual source. The scalar inverse on the whole K retains its separate value G27.

## G7. What was audited and what is continued

The predecessor's Fourier pinching, original union labels, vacuum-scalar return, Haar/physical form maps and conditional comparison have been inspected at their displayed proof steps. The gain here is G6 on the original gauge image, followed by the explicitly re-derived constants G13, G15 and G23. A blanket independent review of every historical artifact is not claimed.

The full next calculation is in BAND_AND_CERTIFICATE.md: the entire first excitation band, the exact boundary-sensitive second-order matrix, and an actual finite-L eigenvalue enclosure with a uniform analytic remainder. SPATIAL_RETURN.md proves the full-volume result on the complete closed source domain, retains its separately calculated conditional-influence subdomain, and computes the original running continuum path. The strong-coupling endpoint G22 and the physical band do not assign a result at g approaching zero.
