I located **`KokunoYumeto/yang-mills-interacting-workbench`** and **`KokunoYumeto/zeta-function-research-reader`**, including the Split Zero reconstruction, transported-class cohomology, and retained-jet constructions. The Zeta repository’s current reader includes its September 14 continuation. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/AI_READING_INDEX.md))

The work below produces three concrete results: an explicit Split Zero complex for the Yang-Mills cubic vertex; an exact relation between eliminated-variable memory and the raw Gram matrix for the **full finite-lattice Hamiltonian**; and an independently recomputed, strengthened numerical certificate. The new lower constant for the retained cubic boundary primitive is between **1.39 and 1.40 times** the published lower constant.

[Research note, executable verification, and certificate](sandbox:/mnt/data/split_zero_yang_mills_research.zip) · [Read the mathematical note](sandbox:/mnt/data/split_zero_ym/RESEARCH_NOTE.md)

## 1. Apply Split Zero to the actual cubic boundary equation

The relevant Split Zero construction retains the source class, the transition that turns it into a boundary, and the kernel of the induced cohomology map. Its reconstructed quotient sends a relation to the zero carrying that relation’s support label. I instantiate that construction on the workbench’s cubic vacuum equation. ([GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7ea0a49945390eae14d3160a5730858899768b5f/formal/splitzero/DERIVED_MATHEMATICS.md))

Fix the workbench’s original box $L=2$, retaining the physical spacing $a>0$. Write
$$
A_0=H_{\mathrm{osc}}-\mu_0,
\qquad
q=H^{(1)}\Phi_0.
$$

Here $H^{(1)}$ is the workbench’s coefficient of the **complete** chart operator, including its kinetic and magnetic contributions. In its original creation coordinates,
$$
q=\sum_{I\in\Lambda}d_Ib_I,
\qquad
A_0b_I=E_Ib_I,
$$
where
$$
\begin{aligned}
\Lambda&=\{(i,j,k):i<j<k\},\\
b_{ijk}
&=\sum_{\alpha,\beta,\gamma=1}^{3}
\epsilon_{\alpha\beta\gamma}
a^\dagger_{i\alpha}a^\dagger_{j\beta}
a^\dagger_{k\gamma}\Phi_0,\\
E_{ijk}&=\frac{\sigma_i+\sigma_j+\sigma_k}{a},\\
\langle b_I,b_J\rangle&=6\delta_{IJ}.
\end{aligned}
$$
The factor $6$ is the original raw Gram factor. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/NONABELIAN_VERTEX.md))

### The support-indexed complex

Define
$$
U=\operatorname{span}_{\mathbb C}\{b_I:I\in\Lambda\},
\qquad
U_J=\operatorname{span}_{\mathbb C}\{b_I:I\in J\}
$$
for every subset $J\subseteq\Lambda$.

Use the join-semilattice $\mathcal P(\Lambda)$, with join $J\cup K$. At support $J$, define the actual cochain window
$$
C_J^0=U_J
\xrightarrow{\ d_J=A_0|_{U_J}\ }
C_J^1=U
\xrightarrow{\ 0\ }
C_J^2=0.
$$

For $J\subseteq K$, the transition maps are inclusion in degree zero, the identity in degree one, and the unique map between the zero spaces in degree two.

The cochain square commutes coordinate by coordinate:
$$
A_0\left(\sum_{I\in J}z_Ib_I\right)
=
\sum_{I\in J}E_Iz_Ib_I
$$
along both routes.

These windows also map into the workbench’s vacuum-correction equation through the actual inclusions
$$
\iota_J^0:U_J\hookrightarrow
\operatorname{Dom}(A_0)\cap\Phi_0^\perp,
\qquad
\iota^1:U\hookrightarrow\Phi_0^\perp,
$$
with
$$
\iota^1d_J=A_0\iota_J^0.
$$

### Compute the cohomology and the transported-class kernel

The coordinate map
$$
\Theta_J:H^1(C_J)\longrightarrow
\mathbb C^{\Lambda\setminus J},
\qquad
\left[\sum_Iz_Ib_I\right]\longmapsto
(z_I)_{I\notin J}
$$
is a linear isomorphism.

Here is its complete verification. An incoming boundary has the form
$$
d_J\left(\sum_{I\in J}y_Ib_I\right)
=
\sum_{I\in J}E_Iy_Ib_I,
$$
so it changes precisely the $J$-coordinates. Conversely, the portion supported in $J$ has the explicit primitive
$$
\sum_{I\in J}\frac{z_I}{E_I}b_I.
$$
Every $E_I$ is strictly positive. The inverse of $\Theta_J$ therefore sends the omitted-coordinate tuple to the class of its displayed sum.

Consequently, for $J\subseteq K$,
$$
\boxed{
\Psi_{J,K}:
\mathbb C^{K\setminus J}
\xrightarrow{\ \cong\ }
\ker\!\left(H^1(C_J)\to H^1(C_K)\right)
}
$$
is given by
$$
(z_I)_{I\in K\setminus J}
\longmapsto
\left[\sum_{I\in K\setminus J}z_Ib_I\right].
$$

Its inverse reads those same coordinates. The corresponding retained primitive is
$$
\pi_{J,K}(z)
=
\sum_{I\in K\setminus J}\frac{z_I}{E_I}b_I,
$$
and its inherited squared norm is exactly
$$
\boxed{
\|\pi_{J,K}(z)\|^2
=
6\sum_{I\in K\setminus J}\frac{|z_I|^2}{E_I^2}.
}
$$

Applying the Split Zero reconstruction to this diagram gives
$$
(J,[v])+(K,[w])
=
(J\cup K,[v+w]_{J\cup K}),
$$
with supported-zero differential composition
$$
(J,x)\longmapsto(J,0).
$$

For the actual Yang-Mills vector $q$, the transition from empty support to full support sends its class to
$$
(\Lambda,0).
$$
The retained kernel element is the original $[q]$, and its unique primitive in $U$ is
$$
u=A_0^{-1}q
=
\sum_I\frac{d_I}{E_I}b_I.
$$

Thus the construction explicitly retains the vector that produces the workbench’s first vacuum correction, $-u$.

### A numerical invariant attached to that retained primitive

Define, on the real domain $z\leq0$,
$$
M_{\mathrm{vac}}(z)
=
\left\langle q,(A_0|_U-z)^{-1}q\right\rangle
=
6\sum_I\frac{|d_I|^2}{E_I-z}.
$$

Differentiating the finite sum gives
$$
\boxed{
M_{\mathrm{vac}}'(0)
=
6\sum_I\frac{|d_I|^2}{E_I^2}
=
\|u\|^2.
}
$$

The source class, its boundary primitive, and this derivative are now connected by explicit maps and coordinate formulas.

## 2. Independently recompute and strengthen the cubic certificate

I independently evaluated the complete **112 frequency blocks** entering the published three-chord certificate. The calculation also checks their total transverse multiplicity, $176$, and reproduces all eighteen published entry enclosures for the selected $K$ and $Q$ matrices. The original source specifies the block formula, tree-path coefficients, and cubic contraction. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/NONABELIAN_VERTEX.md))

The computation uses integer interval endpoints with denominator $10^{40}$. Addition and negation are exact. Products and quotients use all endpoint pairs and outward rounding. Square-root endpoints are certified by integer-square inequalities. The trigonometric values are generated from
$$
\sin\frac{\pi}{10}=\frac{\sqrt5-1}{4},
\qquad
\cos\frac{\pi}{10}=\sqrt{\frac{5+\sqrt5}{8}}
$$
by angle addition.

The executed code and all retained intervals are available as [the verification program](sandbox:/mnt/data/split_zero_ym/exact_certificate.py) and [the machine-readable certificate](sandbox:/mnt/data/split_zero_ym/certificate.json).

### The original coordinate calculation

Use the displayed chord order
$$
c_1=((-1,1,-2),2),\qquad
c_2=((-1,2,-2),3),\qquad
c_3=((-1,1,-1),2).
$$

Writing $K_{ij}$ and $Q_{ij}$ for the selected entries in that order, the complete cubic coefficient is
$$
\begin{aligned}
ac={}&\frac18\bigl(
-Q_{12}K_{13}+Q_{13}K_{12}
+Q_{21}K_{23}-Q_{23}K_{21}\\
&\hspace{31mm}
-Q_{31}K_{32}+Q_{32}K_{31}
\bigr)-\frac18.
\end{aligned}
$$

The last term retains the magnetic contribution. The program checks it from the ordered face vectors
$$
e_1,\ e_2,\ -e_3,\ 0
$$
using the original cross-product recurrence.

The independent computation yields the strict enclosure
$$
\boxed{
-\frac{242460588472}{10^{12}}
<
ac
<
-\frac{242460588471}{10^{12}}.
}
$$

Set
$$
\beta=\frac{242460588471}{10^{12}}.
$$
The absolute value of the corresponding alternating coefficient is therefore greater than $\beta/a$. Passing between the displayed chord order and the globally ordered coefficient vector multiplies this coefficient by the exact permutation sign.

### Retain the largest-frequency multiplicities

The original open-box frequency formula gives
$$
\Omega=\sqrt{\frac{3(5+\sqrt5)}2},
\qquad
\Omega_2=\sqrt{\frac{13+3\sqrt5}2}.
$$

The largest frequency comes from $(4,4,4)$ and has transverse multiplicity two. The next distinct frequency comes from permutations of $(4,4,3)$. Consequently, the top three frequencies, counted with their actual multiplicities, are
$$
\Omega,\quad\Omega,\quad\Omega_2.
$$
These statements follow directly from the workbench’s boundary-sensitive frequency formula and the strict increase of $\sin(\pi j/10)$ on $j=0,\ldots,4$. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md))

Let $\mathcal S$ be the complete edge spectral matrix, and let
$$
\iota:\mathbb C^{176}\longrightarrow\mathbb C^{300}
$$
insert chord coordinates with zero tree entries. In the original counting inner products,
$$
K=\iota^*\mathcal S\iota.
$$

The exact exterior-power morphism is
$$
\bigwedge\nolimits^3K
=
(\bigwedge\nolimits^3\iota)^*
(\bigwedge\nolimits^3\mathcal S)
(\bigwedge\nolimits^3\iota).
$$

The insertion has Gram matrix $I$. Its third exterior power therefore preserves the counting inner product on the corresponding wedge coordinates. The largest eigenvalue of $\bigwedge^3\mathcal S$ is
$$
\Omega^2\Omega_2.
$$
It follows that
$$
0<\bigwedge\nolimits^3K
\preceq\Omega^2\Omega_2I,
$$
and hence
$$
\bigwedge\nolimits^3(2K^{-1})
=
8(\bigwedge\nolimits^3K)^{-1}
\succeq
\frac8{\Omega^2\Omega_2}I.
$$

Combining this with the workbench’s exact raw identity
$$
\|q\|^2
=
6c^*\bigwedge\nolimits^3(2K^{-1})c
$$
and the independently certified coefficient gives
$$
\boxed{
\|H^{(1)}\Phi_0\|^2
>
\frac{48\beta^2}{\Omega^2\Omega_2\,a^2}.
}
$$

Every $E_I$ sums three distinct spatial-mode frequencies. Therefore
$$
E_I\leq\frac{2\Omega+\Omega_2}{a}.
$$
Applying this inequality term by term to the retained spectral sums proves
$$
\boxed{
M_{\mathrm{vac}}'(0)=\|A_0^{-1}H^{(1)}\Phi_0\|^2
>
\frac{48\beta^2}
{\Omega^2\Omega_2(2\Omega+\Omega_2)^2}.
}
$$
It also proves
$$
\boxed{
M_{\mathrm{vac}}(0)
>
\frac{48\beta^2}
{\Omega^2\Omega_2(2\Omega+\Omega_2)a}.
}
$$

The verification program certifies that the new primitive lower constant divided by the published constant
$$
\frac{14641}{13500000\sqrt3}
$$
lies strictly between $139/100$ and $140/100$.

This improvement uses both a tighter coefficient enclosure and the exact top-frequency multiplicities.

## 3. Carry the construction to the full nonlinear Hamiltonian

Now retain the full original finite-lattice operator
$$
H_g=
\frac{2g^2}{a}\sum_eE_e
+
\frac1{2g^2a}
\sum_p\left(2-\operatorname{tr}U_p\right),
\qquad a>0,\quad g>0.
$$

Let
$$
A=H_g-\mathcal E_0(g)
$$
on the physical Hilbert space $\mathcal H$. The source supplies its self-adjoint physical domain, compact resolvent, and actual lowest eigenvalue, so $A\geq0$. ([GitHub](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_gap_primary_20260908/finite_box_weak_coupling_physical_gap.md))

Use the original six comparison vectors $S_I$, in the fixed order
$$
(11,22,33,12,13,23).
$$
Form the **pre-projection chart frame**
$$
r_I=\mathcal B_g^*\bigl(\chi(gx)S_I\bigr),
\qquad
R:\mathbb C^6\to\mathcal H,
\qquad
Rx=\sum_Ix_Ir_I,
$$
using the workbench’s chart map and invariant cutoff. These are smooth physical vectors. Their independence follows by restricting a vanishing linear combination to the neighbourhood where $\chi=1$: the six quadratic polynomial coefficients then vanish individually. The original six vectors and chart construction are given in the interacting-band source. ([github.com](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/interacting_band_publication_20260909/INTERACTING_TENSOR_BAND.md))

Retain the raw Gram matrix
$$
G=R^*R.
$$
Define the explicitly typed maps
$$
P=RG^{-1}R^*:\mathcal H\to\mathcal H,
\qquad
Q=I-P,
$$
$$
B=QAR:\mathbb C^6\to Q\mathcal H,
$$
and
$$
D=QAQ:
\operatorname{Dom}(A)\cap Q\mathcal H
\to Q\mathcal H.
$$

Direct multiplication proves
$$
P^*=P,\qquad P^2=P,\qquad PR=R,\qquad QR=0.
$$

The compression $D$ is self-adjoint and nonnegative. To verify the domain statement, observe that $AP$ is bounded and finite rank because the range of $P$ consists of finitely many vectors in $\operatorname{Dom}(A)$. Its adjoint is the bounded extension of $PA$. Thus
$$
C=QAP+PAQ
$$
is bounded self-adjoint. For $T>\|C\|$, the operators
$$
I-C(A\pm iT)^{-1}
$$
are invertible by their Neumann series. Hence $A-C$ is self-adjoint on $\operatorname{Dom}(A)$. Its $Q$-block is $D$. Finally,
$$
\langle v,Dv\rangle=\langle v,Av\rangle\geq0
$$
for every $v\in\operatorname{Dom}(D)$.

For $t>0$, write $D_t=D+t$. Its inverse exists and satisfies
$$
\|D_t^{-1}\|\leq t^{-1}.
$$

Define
$$
F(t)=R^*AR+tG-B^*D_t^{-1}B
$$
and the restored-vector map
$$
L_t=R-D_t^{-1}B:
\mathbb C^6\to\operatorname{Dom}(A).
$$

The eliminated relation and its primitive are exactly
$$
D_t(-D_t^{-1}Bx)=-Bx,
\qquad
Q(A+t)L_tx=0.
$$

This gives another literal Split Zero two-support complex: its degree-one space is $Q\mathcal H$ at both supports; its incoming source is $0$ at the first support and $\operatorname{Dom}(D)$, with differential $D_t$, at the second. The retained kernel contains the actual vector $-Bx$, with primitive $-D_t^{-1}Bx$.

### The full-operator memory derivative equals the restored raw Gram matrix

Entry by entry,
$$
F_{IJ}(t)
=
\langle r_I,Ar_J\rangle+tG_{IJ}
-
\langle B_I,D_t^{-1}B_J\rangle,
\qquad B_I=QAr_I.
$$

The resolvent identity gives
$$
\frac{d}{dt}D_t^{-1}=-D_t^{-2}.
$$
Since $R^*Q=0$, differentiation and expansion yield
$$
\boxed{
F'(t)
=
G+B^*D_t^{-2}B
=
L_t^*L_t.
}
$$

In coordinates, this is
$$
F'_{IJ}(t)
=
\left\langle
r_I-D_t^{-1}B_I,\,
r_J-D_t^{-1}B_J
\right\rangle.
$$

The same boundary equation gives
$$
\boxed{
L_t^*(A+t)L_t=F(t),
\qquad
F(t)\succeq tG.
}
$$

Finally, solving the two block equations for
$$
(A+t)(Rx+v)=Ry
$$
gives
$$
F(t)x=Gy,\qquad v=-D_t^{-1}Bx.
$$
Therefore
$$
\boxed{
R^*(A+t)^{-1}R
=
G\,F(t)^{-1}G.
}
$$

These identities retain the original Gram matrix, physical spacing, coupling, full kinetic operator, and full plaquette words.

## 4. Extract the first-band information as a retained Split Zero jet

The workbench’s six-band coefficients are
$$
c_{I,n}
=
\langle h_n\Phi_0,H^{(1)}S_I\rangle,
\qquad
\omega_n=\sum_{i,\alpha}n_{i\alpha}\frac{\sigma_i}{a},
\qquad
\Delta=\frac{2\sigma_*}{a}.
$$

The relevant occupation indices have $|n|=3$ or $5$. The source gives both the energy correction and the raw correction Gram matrix in these coordinates. ([github.com](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/sources/ym_quantum_coarse_graining_astra_20260908/interacting_band_publication_20260909/INTERACTING_TENSOR_BAND.md))

Define the finite memory matrix
$$
\Sigma_{IJ}(z)
=
\sum_{|n|=3,5}
\frac{\overline{c_{I,n}}c_{J,n}}{\omega_n-z}.
$$

All displayed denominators at $z=\Delta$ are at least $\sigma_*/a>0$. Direct differentiation proves
$$
\boxed{
\mathsf K=V-\Sigma(\Delta)-E^{(2)}I,
\qquad
\Sigma'(\Delta)=G_2.
}
$$

Thus the workbench’s energy correction and raw Gram correction are the value and derivative of one retained matrix function, with the vacuum correction $E^{(2)}$ still present.

### The exact typed jet morphism

The Zeta workbench constructs retained first jets by applying its scalar $G$-construction to a coefficient-ring jet map. ([GitHub](https://github.com/KokunoYumeto/zeta-function-research-reader/blob/7ea0a49945390eae14d3160a5730858899768b5f/workbenches/split-support-rees-trace/RESEARCH_NOTE.md))

For this Yang-Mills application, let
$$
\mathcal A=\mathbb C\{h\}
$$
be the algebra of holomorphic germs at zero. Define
$$
j^1:\mathcal A\to
\mathbb C[\varepsilon]/(\varepsilon^2),
\qquad
f\mapsto f(0)+\varepsilon f'(0).
$$

The product rule proves multiplicativity:
$$
j^1(fg)
=
f(0)g(0)+
\varepsilon\bigl(f'(0)g(0)+f(0)g'(0)\bigr)
=
j^1(f)j^1(g).
$$

For each original matrix coordinate $I,J$, set
$$
\mathcal E_{IJ}(h)
=
\Sigma_{IJ}(\Delta+h)-\Sigma_{IJ}(\Delta).
$$

The actual morphism is
$$
G(\mathcal A)
\xrightarrow{G(j^1)}
G\!\left(\mathbb C[\varepsilon]/\varepsilon^2\right)
\xrightarrow{G(\varepsilon\mapsto0)}
G(\mathbb C),
$$
and it acts by
$$
\boxed{
\mathcal E_{IJ}^{\bullet}
\longmapsto
\bigl(\varepsilon(G_2)_{IJ}\bigr)^{\bullet}
\longmapsto
0^{\bullet}.
}
$$

Both arrows preserve supported elements and send $\tau$ to $\tau$. This supplies the requested coefficient-level application of the retained-zero jet construction to the Yang-Mills workbench.

### Recover every energy-grouped residue from finitely many derivatives

Enumerate the distinct positive denominators as
$$
\nu_1<\cdots<\nu_N.
$$
Retain every contribution at a repeated energy in the matrix
$$
(B_j)_{IJ}
=
\sum_{n:\,\omega_n-\Delta=\nu_j}
\overline{c_{I,n}}c_{J,n}.
$$

Define the Taylor coefficients
$$
M_r=\frac{\Sigma^{(r)}(\Delta)}{r!}
=
\sum_{j=1}^{N}\frac{B_j}{\nu_j^{r+1}}.
$$

Form the explicit polynomials
$$
p_j(t)
=
\prod_{k\ne j}
\frac{t-\nu_k^{-1}}{\nu_j^{-1}-\nu_k^{-1}}
=
\sum_{r=0}^{N-1}\ell_{jr}t^r.
$$

Every denominator is nonzero by the strict ordering. Evaluation gives
$$
p_j(\nu_k^{-1})=\delta_{jk}.
$$
Consequently,
$$
\boxed{
B_j
=
\nu_j\sum_{r=0}^{N-1}\ell_{jr}M_r.
}
$$

The proof is entrywise substitution:
$$
\nu_j\sum_r\ell_{jr}M_r
=
\sum_k\frac{\nu_j}{\nu_k}
B_kp_j(\nu_k^{-1})
=
B_j.
$$

The retained finite jet therefore determines every energy-grouped residue matrix by an explicit inverse map.

It also carries exact positivity constraints. For $x\in\mathbb C^6$,
$$
x^*B_jx
=
\sum_{n:\,\omega_n-\Delta=\nu_j}
\left|\sum_Ic_{I,n}x_I\right|^2
\geq0,
$$
which proves
$$
\boxed{
\frac{M_0}{\nu_N}
\preceq
M_1
\preceq
\frac{M_0}{\nu_1}.
}
$$

The research note gives the corresponding positive block-moment identity for all higher derivatives. These are explicit relations between the energy correction, raw metric correction, and higher retained memory coefficients.

## Established result

The completed calculation supplies an exact support-indexed cohomology module for the cubic Yang-Mills boundary equation, its retained primitive and quantitative lower bound, full nonlinear finite-lattice restored-metric and resolvent identities, and a typed Split Zero jet map with explicit residue reconstruction.

The executable independently verifies the **112-block cubic certificate and the strengthened lower constants**. The full occupation-coupling table in the residue formula has been characterized algebraically here; it was not numerically evaluated by that executable.

A proof of the four-dimensional continuum Yang-Mills mass gap has not been established in this response. The displayed finite-regulator results and their verification files are the completed mathematical output; no GitHub repository was modified.

---

**Sources:**

- [https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/AI_READING_INDEX.md](https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/AI_READING_INDEX.md)
