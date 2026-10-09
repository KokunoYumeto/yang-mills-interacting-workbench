"""Reproduce the exact Haar fourth moment and original-path receiving scale."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
plt.rcParams.update({"font.size":11,"mathtext.fontset":"dejavusans"})
fig,axes=plt.subplots(1,2,figsize=(13.4,6.7))
fig.subplots_adjust(left=.075,right=.975,top=.79,bottom=.34,wspace=.25)
fig.suptitle("The global observable: exact chord moment and actual-vacuum scale",
             fontsize=16,y=.96)
fig.text(.5,.89,r"Original path: $L_j=j^4,\ a_j=1/(100j),\ g_j^2=\kappa_*/(200j)$; displayed $\kappa_*=1,\ A=1$",
         ha="center",fontsize=12)
m=2*np.arange(2,101);n=m+1;c=np.cos(np.pi/(2*n))
H=3*(.5-c*c/n)*(1-1/(2*n)-c*c/n**2)-15/(8*n**3)*(1-2*c*c/n)
axes[0].plot(m,H,color="#185e93",lw=2.4,label=r"Full $\mathcal{H}_m$ (PK166)")
axes[0].axhline(1.5,color="#475569",ls="--",label=r"Proved limit $3/2$")
axes[0].set(xlabel=r"$m=2L$ (all original boundary terms retained)",
            ylabel=r"$\mathbb{E}_\lambda (u_1\!\cdot u_3)^2$",
            title="Haar measure: complete fourth moment")
axes[0].legend(loc="lower right",fontsize=10)
j=np.arange(2,101,dtype=float)
beta=200*np.sqrt(2)*j*np.sin(np.pi/(4*j**4+2))
factor=1/beta**2
axes[1].loglog(j,factor,color="#92400e",lw=2.4,label=r"Exact $\beta_j^{-2}$ (PK169)")
axes[1].loglog(j,j**6/(5000*np.pi**2),color="#475569",ls="--",
               label=r"Asymptote $j^6/(5000\pi^2)$")
axes[1].set(xlabel=r"Original path index $j$",
            ylabel=r"Factor multiplying actual raw norm $\widehat\Gamma_j$",
            title="Actual vacuum: necessary fourth-moment scale")
axes[1].legend(loc="upper left",fontsize=10)
for ax in axes:
    ax.grid(alpha=.2)
    ax.spines[["top","right"]].set_visible(False)
fig.text(.075,.23,r"$\mathcal{H}_m=3(\frac{1}{2}-\frac{c^2}{n})(1-\frac{1}{2n}-\frac{c^2}{n^2})"
         r"-\frac{15}{8n^3}(1-\frac{2c^2}{n}),\quad n=m+1,\quad c=\cos\frac{\pi}{2n}$",
         fontsize=13)
fig.text(.075,.13,r"$\mathcal{Q}_{4,j}=\int (u_1\!\cdot u_3)^2\psi_j^2\,dU"
         r"\ \geq\ \beta_j^{-2}\widehat\Gamma_j,\qquad"
         r"\beta_j=200\sqrt{2}\,j\sin\frac{\pi}{4j^4+2}\quad(\kappa_*=1)$",fontsize=13)
fig.text(.075,.045,"PK158–PK177 contain the complete proofs. The curves evaluate proved formulas; they are not vacuum samples.\n"
         "Actual fourth-moment growth and nonvanishing limiting spectral weight remain to be established.",fontsize=10,color="#334155")
for ext in ["png","svg"]:
    fig.savefig(ROOT/("GLOBAL_FOUR_POINT_ESTIMATES."+ext),dpi=180)
