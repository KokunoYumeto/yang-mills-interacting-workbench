"""Exact fixed-box odd-state weights and the full-domain receiving map."""
from pathlib import Path
from fractions import Fraction
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

HERE=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":12,"svg.hashsalt":"ym-odd-observable-20261009"})

def weight(l):
    correction=Fraction(0)
    if l%2==0:
        n=l//2
        correction=Fraction((-1)**n)
        for j in range(n):
            correction*=Fraction(3+2*j,2*(j+1))
    return (Fraction((l+1)*(l+2),2)-correction)/2**(l+4)

fig=plt.figure(figsize=(13,10),facecolor="#f6f8fb")
gs=fig.add_gridspec(3,2,height_ratios=[1.05,1.6,1.0],hspace=.43,wspace=.3)
ax=fig.add_subplot(gs[0,:]);ax.axis("off")
ax.text(0,1,"A bounded odd observable on the interacting vacuum",fontsize=20,weight="bold",va="top")
ax.text(0,.77,r"Fixed $L\geq2$, $a>0$; actual coupling limit $g\to0$.",fontsize=14)
ax.text(0,.54,r"$\upsilon_g=\frac{1}{2}(f_g-\mathscr{S}_{\mathcal{R}}f_g)\psi_g\quad\longrightarrow\quad"
        r"\sin[(\sigma_*/2)\,z_1\!\cdot z_3]\,\Phi_0$",fontsize=17)
ax.text(0,.29,r"$\sigma_*=\sqrt{8}\sin[\pi/(4L+2)],\qquad \delta_*=2\sigma_*/a$"
        "\nFull tree, Haar-density, cutoff and reflection maps: PK102–PK116.",fontsize=12)

ax=fig.add_subplot(gs[1,0]);ax.axis("off")
ax.text(0,1.08,"Exact first-cluster reflection",weight="bold",fontsize=15)
table=ax.table(cellText=[
    [r"$z_1\ (V_{12})$",r"$-$",r"$D_1,D_2,D_3$",r"$+$"],
    [r"$z_2\ (V_{13})$",r"$-$",r"$O_{12}$",r"$+$"],
    [r"$z_3\ (V_{23})$",r"$+$",r"$O_{13},O_{23}$",r"$-$"]],
    colLabels=["Mode label","Sign","Physical singlets","Sign"],
    cellLoc="center",colWidths=[.28,.12,.44,.12],bbox=[0,.42,1,.52])
table.auto_set_font_size(False);table.set_fontsize(12)
for (row,col),cell in table.get_celld().items():
    cell.set_edgecolor("#ccd5e0")
    cell.set_facecolor("#e6ecf5" if row==0 else "white")
ax.text(0,.25,"Two odd vectors form the actual lowest odd cluster\nfor sufficiently small g at each fixed box.",fontsize=12)
ax.text(0,.03,r"Raw first weight $\to3/32$; supported bottom $\to\delta_*$."
        "\nProof: PK108–PK112 and PK117–PK120.",fontsize=12)

ax=fig.add_subplot(gs[1,1])
levels=np.arange(1,13);ws=np.array([float(weight(int(l))) for l in levels])
ax.vlines(levels,0,ws,color="#1b5689",lw=2);ax.scatter(levels,ws,color="#1b5689",s=35,zorder=3)
ax.annotate(r"$w_1=3/32$",xy=(1,ws[0]),xytext=(3.4,.095),arrowprops={"arrowstyle":"->","color":"#1b5689"})
ax.annotate(r"$w_2=15/128$",xy=(2,ws[1]),xytext=(4.2,.126),arrowprops={"arrowstyle":"->","color":"#1b5689"})
ax.set_title("Full comparison measure: first 12 atoms",fontsize=14,loc="left",pad=18)
ax.set_xlabel(r"Atom index $l$; physical energy is $2l\sigma_*/a$")
ax.set_ylabel(r"Raw mass $w_l$")
ax.set_ylim(0,.145);ax.set_xticks([1,2,4,6,8,10,12]);ax.grid(axis="y",alpha=.22)
ax.text(.98,.65,r"$\sum_{l\geq1}w_l=\frac{1}{2}(1-5^{-3/2})$",transform=ax.transAxes,ha="right",fontsize=13)
ax.text(.98,.47,"Exact coefficients and entire tail:\nPK121–PK126; no numerical eigenvalues.",transform=ax.transAxes,ha="right",fontsize=10)

ax=fig.add_subplot(gs[2,:]);ax.axis("off")
ax.text(0,1.08,"Global map from the retained higher carrier",fontsize=15,weight="bold")
ax.text(0,.79,r"$Y=\operatorname{Tot}(E_D),\quad D=F_4/\rho(\mathrm{Sp}(1))"
        r"\ \longrightarrow\ A=|\alpha|^2+|\beta|^2+|\gamma|^2"
        r"\ \longrightarrow\ \mathfrak{V}_g(y)$",fontsize=15)
ax.text(0,.51,r"All 24 fibre coordinates retained; $A^{-1}(0)$ is the original rank-12 zero subbundle."
        "\nThis particular receiving map factors through A. Full formulas and proof: PK127–PK129.",fontsize=12)
ax.text(0,.13,r"Joint path $L_j=j^4,\ a_j=1/(100j),\ g_j^2=\kappa_*/(200j)$:"
        "\nThe actual odd energy and raw weight still require estimates uniform along this path (PK130–PK131).",
        fontsize=12,color="#963a26")
fig.subplots_adjust(top=.97,bottom=.065,left=.065,right=.975)
fig.savefig(HERE/"ODD_OBSERVABLE.png",dpi=170)
fig.savefig(HERE/"ODD_OBSERVABLE.svg",metadata={"Date":None})
plt.close(fig)
print("Rendered exact odd-observable diagram and raw spectral weights.")
