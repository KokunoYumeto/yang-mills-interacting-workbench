"""Exact receiving diagram; all curves are stated integration kernels."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans", "font.size":12,
                     "mathtext.fontset":"dejavusans", "svg.fonttype":"none"})
fig = plt.figure(figsize=(14,11), facecolor="#f7f9fc")
gs = fig.add_gridspec(3,2,height_ratios=[.8,2.3,1.6],
                     hspace=.64,wspace=.3,left=.07,right=.96,top=.96,bottom=.07)
title = fig.add_subplot(gs[0,:]); title.axis("off")
title.text(0,1,"Original physical curvature: exact maps and proved bounds",
           fontsize=21,weight="bold",va="top",color="#163b58")
title.text(0,.56,r"$C_{f,j}=a_j\sum_p f(x_p)(2-W_p)$"
           r"$\qquad X_{f,j}=C_{f,j}-\mu_jC_{f,j}$"
           r"$\qquad d\mu_j=\psi_j^2\,dU$", fontsize=16)
title.text(0,.17,r"$H_j(t)=\kappa_*K+\sum_p(b_j+t\,a_jf(x_p))(2-W_p)$"
           r"$\qquad a_j=(100j)^{-1},\quad b_j=10000j^2/\kappa_*$",
           fontsize=14)

ax = fig.add_subplot(gs[1,0],facecolor="white")
u = np.linspace(-1,1,501)
w = 1-np.abs(u)
ax.plot(u,w,color="#237a87",lw=3,label=r"$1-|u|$")
ax.fill_between(u,0,w,color="#237a87",alpha=.18)
ax.axhline(0,color="#516573",lw=.7)
ax.set_xlim(-1.08,1.08); ax.set_ylim(-.08,1.27)
ax.set_xticks([-1,0,1],["−1\n$t=-h$","0\n$t=0$","1\n$t=h$"])
ax.set_yticks([0,1])
ax.set_title("Actual source-average covariance · PVC42–46",loc="left",
             fontsize=14,weight="bold",pad=13)
ax.text(0,1.1,r"$h=b/(2a\|f\|_\infty),\quad u=t/h$",ha="center",fontsize=12)
ax.set_ylabel("Exact probability kernel")
ax.text(.5,-.27,r"$\overline{G}=\int_{-1}^1(1-|u|)\,G(hu)\,du=O(a_j)$",
        transform=ax.transAxes,ha="center",fontsize=13)
ax.grid(alpha=.15)

ax2 = fig.add_subplot(gs[1,1],facecolor="white")
k = np.sign(u)*(1-np.abs(u))**2
ax2.plot(u[u<0],k[u<0],color="#b24b43",lw=3)
ax2.plot(u[u>0],k[u>0],color="#276b9c",lw=3)
ax2.fill_between(u,0,k,where=u<0,color="#b24b43",alpha=.15)
ax2.fill_between(u,0,k,where=u>0,color="#276b9c",alpha=.15)
ax2.axhline(0,color="#516573",lw=.7)
ax2.set_xlim(-1.08,1.08); ax2.set_ylim(-1.22,1.25)
ax2.set_xticks([-1,0,1],["−1\n$t=-h$","0\n$t=0$","1\n$t=h$"])
ax2.set_yticks([-1,0,1])
ax2.set_title("Exact original-source defect · PVC47–50",loc="left",
              fontsize=14,weight="bold",pad=13)
ax2.text(0,1.08,r"$G(0)=\overline{G}+\mathcal{D}_f$",ha="center",fontsize=14)
ax2.set_ylabel("Signed response kernel")
ax2.text(.5,-.27,r"$\mathcal{D}_f=h\int_{-1}^1"
         r"\mathrm{sgn}(u)(1-|u|)^2\mathcal{T}_f(hu)\,du$",
         transform=ax2.transAxes,ha="center",fontsize=13)
ax2.grid(alpha=.15)

foot = fig.add_subplot(gs[2,:]); foot.axis("off")
foot.text(0,.9,"Original vacuum · PVC28–39",color="#163b58",
          weight="bold",fontsize=15)
foot.text(0,.66,r"$f\geq0,\ f\neq0:\quad \mu_jC_{f,j}\asymp a_j^{-1}$",
          fontsize=14)
foot.text(0,.44,r"$\int f\neq0:\quad"
          r"0<\liminf_j\mathcal{E}_{ff,j}\leq"
          r"\limsup_j\mathcal{E}_{ff,j}<\infty$",fontsize=14)
foot.text(0,.21,"Equal-time covariance: bounds leave its limit undetermined.",
          fontsize=12)
foot.text(.55,.9,"Short original face-source pulses · PVC16–20, 40–41",
          color="#163b58",weight="bold",fontsize=13)
foot.text(.55,.64,r"$|G_{fg}-\mathcal{G}_{fg}^{(\epsilon)}|"
          r"\leq \frac{\epsilon}{3}\sqrt{\mathcal{E}_{ff}\mathcal{E}_{gg}}$",
          fontsize=15)
foot.text(.55,.34,r"$|\mathcal{E}_{fg}-\mathcal{E}_{fg}^{(\epsilon_j)}|"
          r"\leq3/(16j)$",fontsize=15)
foot.text(0,-.12,"Curves show exact integration kernels; no actual covariance or response curve is sampled. "
          "The full proof retains all three face orientations and actual means.",
          fontsize=10,color="#516573")
fig.savefig(root/"PHYSICAL_LOCAL_COVARIANCE.png",dpi=180)
fig.savefig(root/"PHYSICAL_LOCAL_COVARIANCE.svg")
plt.close(fig)
print("Created the PNG and reproducible SVG receiving diagram.")
