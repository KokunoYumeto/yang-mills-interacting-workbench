# All real-source inverses of the full original union-labelled Jacobian

11 October 2026. This note retains the entire original labelled space, including its assembly relation kernel and labels that strictly contain their active spin support. It proves a full labelled inverse by a finite Boolean-lattice transformation. The completed [physical response note, GPR1–GPR55](../GLOBAL_PHYSICAL_RESPONSE.md) is a stable input and is not changed. The original labelled definitions are [G1–G13](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/fa79faff2cd697e16cfa3a7953f36810c22c8922/yang-mills/continuations/20260915-gauge-native-band/RESEARCH_NOTE.md). The finite inclusion–exclusion calculation is proved here; no novelty claim is made for Boolean Möbius inversion.

## 1. Every original edge, face, gauge constraint and supported space

Fix \(L\ge2\), the original vertices \(V_L=\{-L,\ldots,L\}^3\), all contained positive coordinate edges \(E=E_L\), and all contained oriented elementary faces \(\mathcal P=\mathcal P_L\). Set
\[
 N=|E|=3(2L)(2L+1)^2,\quad M=|\mathcal P|=3(2L)^2(2L+1),\quad
 Q_L=SU(2)^E.
 \tag{UL1}
\]
Product Haar measure \(dU\) is a probability measure. Keep the original definitions
\[
\begin{split}
 W_{(n;i,j)}(U)
 &=\operatorname{Tr}[U_i(n)U_j(n+e_i)U_i(n+e_j)^{-1}U_j(n)^{-1}],\\
 T_\alpha&=-i\sigma_\alpha/2,\qquad
 X_{e,\alpha}f=\left.\frac d{dt}f(\ldots,e^{tT_\alpha}U_e,\ldots)\right|_{t=0},\\
 K&=-\sum_{e\in E,\alpha=1}^3X_{e,\alpha}^2,\qquad
 \Gamma(f,h)=\sum_{e\in E,\alpha=1}^3(X_{e,\alpha}f)(X_{e,\alpha}h),\\
 H(x)&=\kappa K+\kappa\sum_{p\in\mathcal P}x_p(2-W_p),\qquad
 \kappa>0,\quad x\in\mathbb R^{\mathcal P},\\
 P_Hf&=\int f\,dU,\qquad Q_H=I-P_H.
\end{split}\tag{UL2}
\]
Physical functions are invariant under every original vertex transformation \(U_e\mapsto q_sU_eq_t^{-1}\), including transformations at boundary vertices. Denote their orthogonal Haar projection by \(\Pi\).

For \(A\subseteq E\), let \(\mathsf P_A\) integrate precisely the links outside \(A\). It is a Haar-orthogonal projection, commutes with \(K\), with \(P_H\), and with every vertex gauge action. The last assertion follows by changing the integrated link variables by their left and right vertex factors; their Haar measure is preserved. It acts on Fourier blocks by keeping exactly those with \(j_e=0\) for \(e\notin A\).

The full original product-spin convention is
\[
 c(j)=\sum_{e\in E}j_e(j_e+1),\quad
 \pi_j(U)=\bigotimes_{e\in E}\pi_{j_e}(U_e),\quad
 f_j(U)=\operatorname{Tr}(A_j\pi_j(U)),\quad
 A_j=d_j\int f(U)\pi_j(U)^*dU.
 \tag{UL3}
\]
Here \(d_j=\prod_e(2j_e+1)\) is part of the Fourier coefficient convention. Let
\[
 Y_1(A)=
 \left\{f:\Pi f=f,\ P_Hf=0,\ \mathsf P_Af=f,\
            \|f\|_{Y_1}:=\sum_{j\ne0}c(j)\|A_j\|_1<\infty\right\}.
 \tag{UL4}
\]
This is a closed subspace of the physical Fourier Banach space \(Y_1(E)\). In particular \(Y_1(\varnothing)=\{0\}\). For a real Sobolev index \(s\), also write
\[
 H^s_{\mathrm{ph},0}(A)
 =\{f\in H^s(Q_L):\Pi f=f,\ P_Hf=0,\ \mathsf P_Af=f\},
 \qquad
 \|f\|_{H^s}=\|(I+K)^{s/2}f\|_2.
 \tag{UL5}
\]
The mean for negative \(s\) is pairing with the smooth function \(1\). These definitions keep the full \(K\) and all original gauge constraints. A spin outside \(A\) is the original zero spin, with its original Casimir contribution zero.

Every nonconstant physical block has \(c(j)\ge3\): at a vertex, a single incident nontrivial irreducible representation has no invariant vector; a nonempty active finite graph therefore contains a cycle; the original cubic graph has no cycle shorter than four; and each nonzero link spin costs at least \(3/4\). A fundamental face trace attains \(3\). In particular \(K^{-1}Q_H\) preserves the spaces with support \(A\). The estimate
\[
 \|f\|_{H^2}\le \tfrac43\|f\|_{Y_1}
 \tag{UL6}
\]
follows from \((1+c)/c\le4/3\) and the trace-norm bound on each represented function. Absolute Fourier convergence also gives \(f\in C^2\): two original derivatives of a block have norm at most \(j_ej_f\|A_j\|_1\le c(j)\|A_j\|_1\), including repeated derivatives; the corresponding zeroth and first derivative sums converge as well.

The full original labelled Banach space is
\[
 \mathfrak B
 =\prod_{\varnothing\ne S\subseteq E}Y_1(S),\qquad
 \|F\|_{\mathrm{loc}}
 =\max_{e\in E}\sum_{S\ni e}\|F_S\|_{Y_1}.
 \tag{UL7}
\]
There are finitely many label positions, each of which is an infinite-dimensional function space when it is nonzero. The product is therefore complete. Every nonempty edge label is retained. The space is not restricted to connected labels. In particular an active spin support strictly contained in \(S\) remains in that same \(S\) component.

## 2. The bounded cumulative and Möbius transformations

Set \(F_\varnothing=0\). Define, for every \(A,S\subseteq E\),
\[
 (\zeta F)_A=\sum_{S\subseteq A}F_S,\qquad
 (\mathfrak mG)_S=\sum_{A\subseteq S}(-1)^{|S\setminus A|}G_A,
 \quad G_\varnothing=0.
 \tag{UL8}
\]
These maps have the same supported domains as (UL7): every summand of \((\zeta F)_A\) depends only on links in \(A\), and every summand of \((\mathfrak mG)_S\) depends only on links in \(S\). Both preserve physical invariance and the original Haar mean zero.

For fixed \(T\subseteq S\), the coefficient in \(\mathfrak m\zeta\) is
\[
 \sum_{A:T\subseteq A\subseteq S}(-1)^{|S\setminus A|}
 =(1-1)^{|S\setminus T|}
 =\mathbf1_{\{T=S\}}.
 \tag{UL9}
\]
The same summation with the lower intermediate index gives \(\zeta\mathfrak m=I\). This proves that (UL8) is an actual bounded change of coordinates on the full labelled space, once its norm is estimated; it is not a quotient.

For a fixed anchor \(e\), put \(b_S=\|F_S\|_{Y_1}\). The full finite counting formula is
\[
 \sum_{A\ni e}\|(\zeta F)_A\|_{Y_1}
 \le\sum_{\varnothing\ne S\subseteq E}
        2^{N-|S\cup\{e\}|}b_S.
 \tag{UL10}
\]
Each original \(F_S\) is counted once for each superset of \(S\cup\{e\}\). The same bound holds for \(\mathfrak m\), since its coefficient at each contained pair has absolute value one. Define
\[
 C_N=(N+1)2^{N-2}.
 \tag{UL11}
\]
To prove the claimed bound with this constant, assign weight \(2^{N-1}\) to the singleton anchor \(\{e\}\) and weight \(2^{N-2}\) to each other singleton. For every nonempty \(S\),
\[
 2^{N-|S\cup\{e\}|}
 \le 2^{N-1}\mathbf1_{\{e\in S\}}
       +2^{N-2}\sum_{\substack{f\in S\\f\ne e}}1.
\]
For \(e\in S\) the first term already bounds the left side; for \(e\notin S\) any one of the terms bounds it. Multiplication by \(b_S\), summation, and the original anchor norm give
\[
 \boxed{\|\zeta F\|_{\mathrm{loc}}\le C_N\|F\|_{\mathrm{loc}},\qquad
        \|\mathfrak mG\|_{\mathrm{loc}}\le C_N\|G\|_{\mathrm{loc}}.}
 \tag{UL12}
\]
No claim of sharpness is needed; some singleton supported spaces are in fact zero because of the original gauge constraints. Formula (UL10) retains the exact counting before the displayed bound. The identical estimates hold when each coordinate carries the norm in (UL5), or for a real scalar family with \(\max_e\sum_{S\ni e}|c_S|\). Every constant here is finite at the fixed original volume, and its dependence on \(N\) is explicit.

Keep the original union-label bilinear map
\[
 \mathcal B(F,G)_S
 =K^{-1}Q_H\sum_{\substack{S_1,S_2\ne\varnothing\\S_1\cup S_2=S}}
                       \Gamma(F_{S_1},G_{S_2}).
 \tag{UL13}
\]
The full original estimate is \(\|\mathcal B(F,G)\|_{\mathrm{loc}}\le(2/3)\|F\|_{\mathrm{loc}}\|G\|_{\mathrm{loc}}\), as proved in original G11–G13. In particular all terms are well-defined in (UL7).
The function \(\Gamma(F_{S_1},G_{S_2})\) depends only on \(S_1\cup S_2\). It is physical because
\(2\Gamma(f,h)=fKh+hKf-K(fh)\) and every term on the right commutes with the original gauge action. Both \(Q_H\) and \(K^{-1}Q_H\) preserve that support and those constraints. Thus the full union label in (UL13) is also its exact allowed target space. The exact Boolean identity is
\[
 \boxed{(\zeta\mathcal B(F,G))_A
     =K^{-1}Q_H\Gamma((\zeta F)_A,(\zeta G)_A).}
 \tag{UL14}
\]
Indeed \(S_1\cup S_2\subseteq A\) is equivalent to both \(S_1\subseteq A\) and \(S_2\subseteq A\). Reorder the finite label sums in (UL13); the bilinearity of \(\Gamma\) gives (UL14). Fourier completion is legitimate by the original bilinear bound and (UL6). Every intermediate \(Q_H\), the inverse Casimir and the two ordered inputs are present in this identity.

## 3. Every subset vacuum with the full original Hamiltonian

For every original edge subset \(A\subseteq E\), define the source restriction
\[
 (r_Ax)_p=\mathbf1_{\{\partial p\subseteq A\}}x_p,\qquad
 H_A(x)=H(r_Ax)
       =\kappa K+\kappa\sum_{p\in\mathcal P}
                \mathbf1_{\{\partial p\subseteq A\}}x_p(2-W_p).
 \tag{UL15}
\]
Thus the kinetic operator is the same full \(K\). Each source term, including its scalar \(2\kappa x_p\), is either retained with its displayed indicator or has source zero. The compact product, measure and gauge group are unchanged.

For completeness the real smooth bounded potential in (UL15) has a smooth strictly positive unit ground vector \(\psi_A\) and a simple ground eigenvalue \(E_A\). Minimize the compact-resolvent Rayleigh form, take the modulus, apply the elliptic equation and the maximum principle, and use the identity
\[
 \langle\psi_Ah,(H_A-E_A)\psi_Ah\rangle
 =\kappa\int\psi_A^2\Gamma(\bar h,h)dU
 \tag{UL16}
\]
to prove uniqueness: another ground vector divided by \(\psi_A\) has zero derivatives, hence is constant. These arguments work for all finite real \(x\), including mixed signs. The vertex transformations preserve positivity and norm and commute with \(H_A\), so \(\psi_A\) is physical.

Every arbitrary left translation of an original link outside \(A\) also commutes with \(H_A\). It preserves the positive unit ground vector by the same uniqueness. Therefore
\[
 \mathsf P_A\psi_A=\psi_A,\qquad
 \psi_A(U)=\psi_A(U_A)\prod_{e\notin A}1.
 \tag{UL17}
\]
This does not change \(K\): its outside terms act on the explicitly displayed constant factors and contribute zero. Define
\[
 \rho_A=\psi_A^2,\quad d\mu_A=\rho_AdU,\quad
 v_A=\log\psi_A-P_H\log\psi_A,\quad
 c_A=P_H\log\psi_A=-\tfrac12\log\int e^{2v_A}dU.
 \tag{UL18}
\]
Then \(v_A\in C^\infty\cap Y_1(A)\). The membership in \(Y_1\) follows from the original Peter–Weyl estimate (GPR17), applied with any sufficiently high Sobolev order. These functions depend real analytically on \(x\) in every Sobolev norm and in \(Y_1(A)\): the isolated simple ground projection has a local resolvent Neumann expansion, its positive unit phase is uniquely fixed, the elliptic equation gives every Sobolev order, and the logarithm is analytic on a sufficiently small positive neighbourhood. These local branches agree everywhere on the real source space by uniqueness. At \(A=\varnothing\), the full free vacuum is \(1\), so \(E_\varnothing=v_\varnothing=c_\varnothing=0\).

Dividing the full equation by \(e^{v_A+c_A}\) and taking its Haar mean gives
\[
\begin{split}
 Kv_A&=\sum_{\partial p\subseteq A}x_pW_p
        +\Gamma(v_A,v_A)-C_A,\\
 C_A&=\int\Gamma(v_A,v_A)dU,\qquad
 E_A=2\kappa\sum_{\partial p\subseteq A}x_p-\kappa C_A,\\
 v_A&=\tfrac13\sum_{\partial p\subseteq A}x_pW_p
             +K^{-1}Q_H\Gamma(v_A,v_A).
\end{split}\tag{UL19}
\]
The last formula uses the original equality \(KW_p=3W_p\). Both the potential scalar and the removed Haar scalar are retained.

We will need the complete physical inverse on the same supported space:
\[
 \mathscr L_A=I-2K^{-1}Q_H\Gamma(v_A,\cdot).
 \tag{UL20}
\]
It is a bounded bijection on every \(H^s_{\mathrm{ph},0}(A)\) and on \(Y_1(A)\). Here is the supporting argument, including the support issue. On the full physical Sobolev space, the perturbation of the identity gains one derivative and is compact. A kernel element bootstraps to a smooth solution of
\(\mathcal L_Ah=b\), where \(\mathcal L_A=K-2\Gamma(v_A,\cdot)\) and \(b\) is constant. Its \(\mu_A\) mean forces \(b=0\), and (UL16) makes \(h\) constant; its Haar mean is zero. The index-zero compact perturbation is therefore a bounded bijection. In the Fourier norm, the exact GPR18 estimate maps its perturbation \(Y_1\to Y_{3/2}\); the latter embeds compactly into \(Y_1\) by a finite Casimir cutoff and its \(R^{-1/2}\) tail. Its kernel embeds in the already trivial \(H^2\) kernel. This proves the \(Y_1\) assertion.

The projection \(\mathsf P_A\) commutes with \(H_A\) and the rank-one projection onto \(\psi_A\), and hence with the vacuum-complement inverse. It also commutes with multiplication by \(\psi_A^{\pm1}\), with \(K\), and with \(Q_H\). Thus the inverse preserves precisely the functions supported on \(A\). In full detail, for \(f\in Y_1(A)\), or \(f\in H^s_{\mathrm{ph},0}(A)\),
\[
 \boxed{\mathscr L_A^{-1}f
 =Q_H\kappa\psi_A^{-1}(H_A-E_A)^\dagger\psi_A
                     [Kf-\mu_A(Kf)].}
 \tag{UL21}
\]
The dagger is the actual inverse on the Haar-orthogonal complement of \(\psi_A\), extended by zero on that vector. Its Sobolev extension has domain \(H^{s-2}\) and range \(H^s\). For negative indices the scalar is the exact pairing \(\mu_A(Kf)=\langle f,K\rho_A\rangle\). The bracket multiplied by \(\psi_A\) is orthogonal to \(\psi_A\), the factor \(\kappa\) is retained, and the final \(Q_H\) imposes the required Haar mean. Multiplication by \(\psi_A\) intertwines \(\mathcal L_A\) with \((H_A-E_A)/\kappa\); hence (UL21) solves (UL20), and the previous uniqueness proves it is the inverse. The same construction proves real analytic dependence of these inverses in their fixed supported operator norms.

## 4. The unique real full labelled vacuum and every scalar

Define the original source insertion and the new exact labelled vacuum by
\[
 T(x)_S=\tfrac13\sum_{\substack{p\in\mathcal P\\\partial p=S}}x_pW_p,
 \qquad
 V(x)_S=(\mathfrak m v)_S
       =\sum_{A\subseteq S}(-1)^{|S\setminus A|}v_A(x).
 \tag{UL22}
\]
All labels and functions in this formula have the original meaning. A summand \(v_A\) placed in the larger label \(S\) retains the explicit distinction between that label and its active spin support. There are only finitely many summands; (UL12) and the established \(Y_1(A)\) regularity prove \(V\in\mathfrak B\), with real analytic dependence on all finite real sources.

Equations (UL8)–(UL9) give
\[
 (\zeta V)_A=v_A,\qquad
 (\zeta T)_A=\tfrac13\sum_{\partial p\subseteq A}x_pW_p.
 \tag{UL23}
\]
Apply (UL14) to (UL19), and then the inverse \(\mathfrak m\). The result is the full original labelled nonlinear equation
\[
 \boxed{V(x)=T(x)+\mathcal B(V(x),V(x))}
 \quad\text{in }\mathfrak B,\quad x\in\mathbb R^{\mathcal P}.
 \tag{UL24}
\]
It is the unique real solution in \(\mathfrak B\). Indeed, for any real solution \(F\), each \(w_A=(\zeta F)_A\) is real, \(C^2\), physical, supported on \(A\), and of Haar mean zero. Equation (UL14) makes it solve the last equation in (UL19). Restore the removed scalar \(\int\Gamma(w_A,w_A)dU\) and put
\[
 \widetilde\psi_A=
       e^{w_A}\Big/\left(\int e^{2w_A}dU\right)^{1/2}.
\]
The product rule proves that this positive vector is an eigenvector of the full \(H_A\), with eigenvalue \(2\kappa\sum_{\partial p\subseteq A}x_p-\kappa\int\Gamma(w_A,w_A)dU\). Its version of (UL16) shows that it is a ground vector. Ground uniqueness, and then the original Haar-mean-zero convention, imply \(w_A=v_A\). Möbius inversion gives \(F=V\). No assertion of global uniqueness for complex solutions is made.

For every nonempty original label define the full scalar removed by \(Q_H\),
\[
 \mathcal C_S(x)
 =\int\sum_{S_1\cup S_2=S}
                 \Gamma(V_{S_1},V_{S_2})\,dU.
 \tag{UL25}
\]
The ordered pairs \(S_1,S_2\) are the same as in (UL13). By the finite union identity before removing its constant,
\[
 \sum_{S\subseteq A}\mathcal C_S=C_A,\qquad
 \boxed{\mathcal C_S
    =\sum_{A\subseteq S}(-1)^{|S\setminus A|}
                        \int\Gamma(v_A,v_A)dU.}
 \tag{UL26}
\]
Thus every removed scalar has an exact original-label formula. Each cumulative \(C_A\) is nonnegative, but its individual Möbius coefficients are not assumed nonnegative.

The energy formula in (UL19) gives a second useful expression with the complete potential scalar:
\[
 \boxed{\mathcal C_S
 =2\sum_{\partial p=S}x_p
     -\kappa^{-1}\sum_{A\subseteq S}(-1)^{|S\setminus A|}E_A.}
 \tag{UL27}
\]
To prove the first term, for each fixed face sum its indicator over the Boolean interval:
\[
 \sum_{\partial p\subseteq A\subseteq S}(-1)^{|S\setminus A|}
 =\mathbf1_{\{\partial p=S\}}.
 \tag{UL28}
\]
Define the labelled energy and normalization scalar families by
\[
\begin{split}
 \mathcal E_S&=2\kappa\sum_{\partial p=S}x_p-\kappa\mathcal C_S
          =\sum_{A\subseteq S}(-1)^{|S\setminus A|}E_A,\\
 \mathfrak c_S&=\sum_{A\subseteq S}(-1)^{|S\setminus A|}c_A
 =-\tfrac12\sum_{A\subseteq S}(-1)^{|S\setminus A|}
                      \log\int e^{2v_A}dU .
\end{split}\tag{UL29}
\]
They obey, for every original \(A\),
\[
 E_A=\sum_{S\subseteq A}\mathcal E_S,\qquad
 \log\psi_A=\sum_{S\subseteq A}(V_S+\mathfrak c_S).
 \tag{UL30}
\]
The scalar families are kept separately from the zero-Haar-mean Banach space. The labelled \(\mathcal E_S\) are exact Möbius energy coefficients, not eigenvalues of additional Hamiltonians. At the full label their complete sums recover the actual original energy and vacuum, without dropping a normalization or boundary contribution.

## 5. The full Jacobian inverse, including the entire relation kernel

Differentiate the nonlinear left side of (UL24) in a full labelled direction. Its full original Jacobian is
\[
 \mathfrak L_x=I-2\mathcal B(V(x),\cdot):
              \mathfrak B\longrightarrow\mathfrak B.
 \tag{UL31}
\]
Both orders of the symmetric bilinear derivative contribute the factor two. This direction is an arbitrary element of the entire labelled space, not only a face-source perturbation.

Let \(\mathfrak D_x\) be the coordinatewise map
\[
 (\mathfrak D_xG)_A=\mathscr L_A(x)G_A,\qquad
 G_A\in Y_1(A).
 \tag{UL32}
\]
Equations (UL14) and (UL23) prove the exact conjugacy
\[
 \boxed{\zeta\mathfrak L_x=\mathfrak D_x\zeta,\qquad
         \mathfrak L_x=\mathfrak m\mathfrak D_x\zeta.}
 \tag{UL33}
\]
Every \(\mathscr L_A\) is a bounded bijection by (UL20)–(UL21), on its supported space. There are finitely many \(A\). The diagonal inverse is therefore bounded on (UL7), with norm at most the largest of the finitely many supported inverse norms. Combining it with (UL12) proves
\[
 \boxed{\mathfrak L_x^{-1}
          =\mathfrak m\mathfrak D_x^{-1}\zeta,\qquad
  (\mathfrak L_x^{-1}F)_S
   =\sum_{A\subseteq S}(-1)^{|S\setminus A|}
       \mathscr L_A^{-1}\left(\sum_{T\subseteq A}F_T\right).}
 \tag{UL34}
\]
Inserting (UL21) in each summand is the complete formula in terms of the actual full \(H_A\), their physical vacuum-complement inverses, both original means and the original \(\kappa\). Every output summand is supported on \(A\subseteq S\), but remains in the label \(S\) specified by the outer formula.

Define the established finite quantities
\[
 B_A(x)=\|\mathscr L_A(x)^{-1}\|_{Y_1(A)\to Y_1(A)}.
\]
The zero coordinate is ignored when \(Y_1(A)=\{0\}\). Then the full original local norm satisfies
\[
 \boxed{\|\mathfrak L_x^{-1}\|_{\mathrm{loc}\to\mathrm{loc}}
          \le C_N^2\max_{\varnothing\ne A\subseteq E}B_A(x)<\infty.}
 \tag{UL35}
\]
Finiteness here is proved by (UL20), not left as an assumption. Both \(\mathfrak L_x\) and its inverse are real analytic in the full labelled operator norm, since every diagonal supported inverse is real analytic and the finite transformations are fixed.

There is an identical extension to each labelled Sobolev product
\[
 \mathfrak H^s=\prod_{\varnothing\ne S\subseteq E}H^s_{\mathrm{ph},0}(S),
 \qquad
 \|F\|_{\mathrm{loc},H^s}
 =\max_e\sum_{S\ni e}\|F_S\|_{H^s}.
 \tag{UL36}
\]
The fixed smooth \(V_S\) makes the linear operator (UL31) bounded there; the quadratic map need not be used on two arbitrary low-regularity inputs. Equations (UL33)–(UL35) apply with the corresponding supported Sobolev inverse norms. On intersections they are the same inverse by the exact formula and uniqueness.

The full assembly map is
\[
 \mathsf aF=\sum_{S\subseteq E}F_S=(\zeta F)_E.
 \tag{UL37}
\]
Consequently its original relation kernel has the exact coordinate description
\[
 \boxed{\zeta(\ker\mathsf a)
       =\{G:G_E=0,\ G_A\in Y_1(A)\text{ for every }A\subsetneq E\}.}
 \tag{UL38}
\]
This is an equality with all proper-subset coordinates freely specified in their actual supported spaces. The forward inclusion follows from (UL37); for the reverse inclusion use \(\mathfrak mG\), whose full sum is \(G_E=0\). Thus the kernel has not been removed. The diagonal map and its inverse preserve \(G_E=0\), so (UL34) restricts to a bounded real analytic inverse on the entire relation kernel.

The comparison section \(\iota h\) places \(h\in Y_1(E)\) in its original full edge label \(E\) and puts zero in all proper labels. Then \(\zeta\iota h\) has precisely its \(E\) coordinate equal to \(h\). It follows that
\[
\begin{gathered}
 \mathfrak B=\ker\mathsf a\ \oplus\ \iota Y_1(E),\qquad
 F=(F-\iota\mathsf aF)+\iota\mathsf aF,\\
 \mathfrak L_x\iota=\iota\mathscr L_E,\quad
 \mathsf a\mathfrak L_x=\mathscr L_E\mathsf a,\quad
 \mathsf a\mathfrak L_x^{-1}=\mathscr L_E^{-1}\mathsf a.
\end{gathered}\tag{UL39}
\]
The projection \(F\mapsto F-\iota\mathsf aF\) onto the relation kernel therefore commutes with \(\mathfrak L_x\). Equations (UL38)–(UL39) identify the exact additional inverse that the assembly quotient alone cannot see. They do not identify two different labels: the original relation coefficients remain in the first summand.

## 6. Exact identification with the original source branch

The full source insertion has
\[
 \|T(x)\|_{\mathrm{loc}}
 \le8\max_{e\in E}\sum_{p:e\in\partial p}|x_p|.
 \tag{UL40}
\]
Indeed the original fundamental face coefficient has trace norm \(8\), Casimir \(3\), and source factor \(1/3\); its contribution in the exact norm is therefore \(8|x_p|\), retaining its four-edge label. If \(t=\|T(x)\|_{\mathrm{loc}}<3/8\), the original bilinear bound maps the ball of radius
\[
 r(t)=\tfrac34\left(1-\sqrt{1-\tfrac83t}\right)
 \tag{UL41}
\]
to itself, since \(r=t+(2/3)r^2\). Its difference estimate has factor \((4/3)r=1-\sqrt{1-(8/3)t}<1\). The usual iteration is therefore a convergent labelled solution near zero, with its original union recurrence. On the real neighbourhood it equals \(V\) by the real uniqueness proof after (UL24). Their analytic germs coincide; differentiating yields all original coefficients. Any further real domain on which the original source construction was proved also agrees with \(V\), by that same uniqueness, without a new contraction estimate.

There is a coefficient-level verification that keeps every source union. Let \(v_E(x)=\sum_{\nu\ne0}v_\nu x^\nu\) be its convergent germ, where \(\nu\in\mathbb N_0^{\mathcal P}\) and no factorial convention is inserted. Define the original source union
\[
 U_\nu=\bigcup_{p:\nu_p>0}\partial p.
 \tag{UL42}
\]
Since \(H_A(x)=H_E(r_Ax)\) with the same positive unit normalization,
\[
 [x^\nu]v_A
 =\mathbf1_{\{U_\nu\subseteq A\}}v_\nu,\qquad
 \boxed{[x^\nu]V_S
 =\sum_{U_\nu\subseteq A\subseteq S}
             (-1)^{|S\setminus A|}v_\nu
 =\mathbf1_{\{S=U_\nu\}}v_\nu.}
 \tag{UL43}
\]
If the Fourier active support of \(v_\nu\) is smaller than \(U_\nu\), equation (UL43) still leaves that coefficient at the complete original union label \(U_\nu\). Thus the equality with the old branch is equality in the full labelled space, not merely after assembly.

The map \(x\mapsto V(x)\) is consequently the global real analytic continuation of the original full labelled source germ along the finite real source space. Its Jacobian inverse (UL34) includes all relation directions at every point. This continuation does not state that the original Taylor series at zero converges at all real sources or that its previously proved complex disk has grown. Different complex singularities are not excluded by a real-source argument.

## 7. Original-path applicability and the remaining spectral question

For an explicit labelled Sobolev bound, retain
\[
 s_e(x)=\sum_{p:e\in\partial p}|x_p|,\qquad
 S(x)=2\left(\sum_es_e(x)^2\right)^{1/2},\qquad
 \Omega(x)=32\pi\sum_p|x_p|.
 \tag{UL44}
\]
The signed-source score proof in GPR27–GPR31 gives the actual supported inverse bound in the original Haar energy norm,
\[
 \|\mathscr L_A^{-1}\|_{\dot H^1_H(A)\to\dot H^1_H(A)}
 \le e^{\Omega_A/2}
       \left(1+\frac{2S_A}{\sqrt3}e^{\Omega_A/2}\right).
\]
Here \(s_{e,A}=\sum_{p:e\in\partial p,\ \partial p\subseteq A}|x_p|\), \(S_A=2(\sum_es_{e,A}^2)^{1/2}\), and \(\Omega_A=32\pi\sum_{\partial p\subseteq A}|x_p|\), so \(S_A\le S\) and \(\Omega_A\le\Omega\). The zero-Haar-mean energy norm is a norm on every actual supported physical space, by the same physical Casimir gap \(3\). Equations (UL12) and (UL34) yield
\[
 \boxed{\|\mathfrak L_x^{-1}\|_{\mathrm{loc},\dot H^1_H\to
                                      \mathrm{loc},\dot H^1_H}
 \le C_N^2e^{\Omega/2}
       \left(1+\frac{2S}{\sqrt3}e^{\Omega/2}\right).}
 \tag{UL45}
\]
The original coefficient-norm assertion remains (UL35); (UL45) is explicitly a different, specified Sobolev estimate.

On the unchanged original sequence
\[
 \kappa=\kappa_*>0,\quad L_j=j^4,\quad
 x_p=\xi_j=\frac{10000j^2}{\kappa_*^2},\quad
 N_j=3(2j^4)(2j^4+1)^2,\quad M_j=3(2j^4)^2(2j^4+1),
 \tag{UL46}
\]
one has \(\Omega_j=32\pi\xi_jM_j\) and \(S_j\le8\xi_j\sqrt{N_j}\). Thus the complete full labelled Jacobian, including the assembly relation kernel, is invertible at every finite path point, with
\[
 \|\mathfrak L_{x_j}^{-1}\|_{\mathrm{loc},\dot H^1_H\to
                                      \mathrm{loc},\dot H^1_H}
 \le (N_j+1)^2\,2^{2N_j-4}\,
          e^{\Omega_j/2}
       \left(1+\frac{16\xi_j\sqrt{N_j}}{\sqrt3}e^{\Omega_j/2}\right).
 \tag{UL47}
\]
Every factor arises from the original labels or the actual vacuum estimate. This is not a volume-uniform bound, and it is not the polynomial finite face-response bound proved separately in GPR52. The new result removes the previously untreated full relation-kernel inverse from the finite-source calculation. The asymptotic excitation gap and low-energy spectral weight of the actual original path remain separate mathematical calculations; no limit of (UL47) establishes them.
