*GitHub reading copy; only mathematical delimiters have changed. [Unchanged source](../archive/ns-vacuum-propagation/docs/HIGHER_ORDER.md).*

# Complete displayed fifth-order fluid correction and its dimensional map

This appendix retains all terms of Compère, McFadden, Skenderis, and Taylor (2011), equations (6.1)–(6.3), under the map in the current paper. The source calculation uses a flat cutoff and no external force. It is recorded as that source calculation, not presented as the complete fifth-order equation for the curved, forced boundary data of §7.

Let the source variables be $(\tau_B,x^i,v_i^B,P^B,r_c)$ and retain

$$
r_c=\ell^2,\quad \tau_B=ct/\ell,\quad
v_i^B=\ell U_i/c,\quad P^B=\ell^2P/c^2,\quad\ell=\nu/c.
$$

Thus $\partial_{\tau_B}=(\ell/c)\partial_t$. Define, with no factor of one-half,

$$
\mathcal S_{ij}=\partial_iU_j+\partial_jU_i,
\qquad\mathcal W_{ij}=\partial_iU_j-\partial_jU_i.
$$

In particular $\mathcal S=2S$ for the strain tensor in §4. The source tensors satisfy $\sigma^B=(\ell/c)\mathcal S$, $\omega^B=(\ell/c)\mathcal W$. Summed indices range from one to three. Set $\Delta=\partial_k\partial_k$ and $|U|^2=U_kU_k$.

The complete displayed physical fifth-order correction is

$$
\begin{aligned}
\mathcal F_i^{(5)}[U,P]=\frac1{c^2}\Big[&
-\frac{3\nu^3}{2}\Delta^2U_i
+2\nu^2U_k\Delta\partial_kU_i
+\nu^2\mathcal S_{ik}\partial_l\mathcal S_{kl}
-\frac{5\nu^2}{2}\mathcal W_{ik}\partial_l\mathcal S_{kl}\\
&-\frac{3\nu^2}{4}\partial_i(\mathcal S_{kl}\mathcal S_{kl})
-\frac{5\nu^2}{8}\partial_i(\mathcal W_{kl}\mathcal W_{lk})
+\nu^2\mathcal S_{kl}\partial_k\mathcal S_{li}\\
&-2\nu U_k\partial_k\partial_iP
-2\nu(\partial_kU_i)\partial_kP
-\nu P\Delta U_i
-\frac\nu2|U|^2\Delta U_i\\
&-\frac\nu2(\partial_k\mathcal S_{il})U_kU_l
+\frac\nu2(\partial_k\mathcal W_{il})U_kU_l
+2\nu(\partial_kU_i)\mathcal W_{kl}U_l\\
&+(P+|U|^2)\partial_iP-U_i\partial_tP
\Big].
\end{aligned} \tag{H.1}
$$

The reversed order in $\mathcal W_{kl}\mathcal W_{lk}$ is retained. Since $\mathcal W$ is antisymmetric, replacing it by $\mathcal W_{kl}\mathcal W_{kl}$ without a minus sign would change the equation.

If $\mathcal R_B^{(7)}$ denotes the source's unspecified $O(\epsilon^7)$ momentum remainder, its dimensional image is exactly $(c^2/\ell^2)\mathcal R_B^{(7)}$. The displayed equation is

$$
\partial_tU_i+U_j\partial_jU_i-\nu\Delta U_i+\partial_iP
=\mathcal F_i^{(5)}[U,P]+\frac{c^2}{\ell^2}\mathcal R_{B,i}^{(7)}.
\tag{H.2}
$$

No exact numerical bound on that remainder for the NS singular family is supplied by the order symbol alone. The expansion order follows the source's grading $v^B=O(\epsilon)$, $P^B=O(\epsilon^2)$, $\partial_i=O(\epsilon)$, $\partial_{\tau_B}=O(\epsilon^2)$.

The entire displayed incompressibility correction transforms to

$$
\operatorname{div}U
=\frac1{c^2}\left[U_i\partial_iP-\nu U_i\Delta U_i+
\frac\nu2\mathcal S_{ij}\mathcal S_{ij}\right]
+\frac c\ell\mathcal R_B^{(6)}, \tag{H.3}
$$

where $\mathcal R_B^{(6)}$ is the source's $O(\epsilon^6)$ scalar remainder. Thus exact incompressibility of the original NS velocity does not remove the higher-order scalar equation; the higher-order fluid variables and source data also enter the reconstruction.

## The pressure-elimination map for the actual forcing

The source simplifies its fifth-order expression using its equation (6.4), the unforced leading pressure relation. For the physical forced NS equation with exact incompressibility, take a Cartesian divergence directly:

$$
\boxed{\Delta P+(\partial_iU_j)(\partial_jU_i)=\partial_if_i.} \tag{H.4}
$$

All terms in (H.4) follow from the specified differential equation; the time and viscosity divergences vanish because $\operatorname{div}U=0$. The source manuscript also retains the force divergence in its localized pressure formula following (10.5).

Therefore the map from the source's unforced pressure-elimination step to the forced one is the explicit replacement of its zero right-hand side by $\operatorname{div}f$, followed by any derivatives applied to that relation. Equation (H.1) cannot be declared the full forced fifth-order correction by appending an arbitrary $f_i$ alone. The current note uses its linear fourth-derivative sector to quantify the fixed-cutoff scale problem and separately derives the exact leading metric-source map. It does not discard (H.4) or the curved-boundary source terms.

## Source

Compère, G., McFadden, P., Skenderis, K., & Taylor, M. (2011). The holographic fluid dual to vacuum Einstein gravity. *Journal of High Energy Physics, 2011*(07), 050. https://doi.org/10.1007/JHEP07(2011)050. Source equations (6.1)–(6.4), arXiv:1103.3022, PDF page index 15 (printed page 15).

The conversion is a new algebraic derivation from those displayed equations. The accompanying tests verify the full vector conversion on a nontrivial polynomial field, in addition to the pressure-divergence identity.
