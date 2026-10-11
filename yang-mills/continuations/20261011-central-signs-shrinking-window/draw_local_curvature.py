from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, Rectangle
import numpy as np

HERE=Path(__file__).resolve().parent
fig=plt.figure(figsize=(15,10),facecolor="#f8f9fb")
fig.text(.045,.957,"Local curvature in the actual vacuum",fontsize=24,fontweight="bold",color="#163553")
fig.text(.045,.917,"Exact patch partition, gauge cancellation and the original physical smearing",
         fontsize=14,color="#516070")
ax=fig.add_axes([.03,.445,.43,.415],projection="3d")
q=3
for d in range(3):
    for u in range(q+1):
        for v in range(q+1):
            xx=np.zeros((2,3)); xx[:,d]=[0,q]
            rest=[e for e in range(3) if e!=d]
            xx[:,rest[0]]=u; xx[:,rest[1]]=v
            ax.plot(xx[:,0],xx[:,1],xx[:,2],color="#7896af",alpha=.63,lw=1)
ax.set_xlim(-.2,3.5);ax.set_ylim(-.2,3.5);ax.set_zlim(-.2,3.5)
ax.set_box_aspect([1,1,1])
ax.view_init(elev=22,azim=-53)
ax.set_xticks([0,1,2,3]);ax.set_yticks([0,1,2,3]);ax.set_zticks([0,1,2,3])
ax.set_xlabel("direction 1");ax.set_ylabel("direction 2");ax.set_zlabel("direction 3")
ax.set_title("A strict interior vertex patch, q = 3\nNQ = 144 edges; MQ = 108 inside faces",fontsize=13,pad=12)
fig.text(.055,.387,"Each of 6 sides contributes 2q(q+1) outward faces.\n"
         r"Total crossing faces: $C_Q=12q(q+1)$, including corners.",fontsize=12,color="#233c52")

ar=fig.add_axes([.55,.445,.40,.35])
ar.set_xlim(-.55,1.8);ar.set_ylim(-.4,1.45);ar.set_aspect("equal");ar.axis("off")
ar.add_patch(Rectangle((-.5,-.25),.5,1.5,facecolor="#dcebf6",edgecolor="none"))
vertices=[(0,0),(1,0),(1,1),(0,1)]
for a,b,label,color in [
    ((0,0),(1,0),r"$U_d(z)$","#b2681d"),
    ((1,0),(1,1),r"$U_e(z+e_d)$","#b2681d"),
    ((1,1),(0,1),r"$U_d(z+e_e)^{-1}$","#b2681d"),
    ((0,1),(0,0),r"$U_e(z)^{-1}$","#156b9a")]:
    ar.add_patch(FancyArrowPatch(a,b,arrowstyle="-|>",mutation_scale=18,lw=3,color=color))
for x,y in vertices: ar.plot(x,y,"o",color="#163553",ms=6)
ar.text(.5,-.15,r"$U_d(z)$",ha="center",fontsize=13,color="#995813")
ar.text(1.09,.5,r"$U_e(z+e_d)$",va="center",fontsize=12,color="#995813")
ar.text(.5,1.12,r"$U_d(z+e_e)^{-1}$",ha="center",fontsize=13,color="#995813")
ar.text(-.13,.5,r"$U_e(z)^{-1}$",ha="right",va="center",fontsize=13,color="#156b9a")
ar.text(-.08,1.35,"Inside",ha="right",fontsize=12,color="#156b9a")
ar.text(.55,1.35,"Outside",ha="center",fontsize=12,color="#995813")
fig.text(.545,.837,"Every crossing face: one inside edge, three outside",fontsize=14,fontweight="bold",color="#163553")
fig.text(.545,.425,r"$W_p=\mathrm{Tr}(U_e^{-1}P),\quad \mathbb{E}_{\psi_{\rm out}^2}P=0$",
         fontsize=18,color="#163553")
fig.text(.545,.380,"Gauge sign −I at one endpoint flips P.\n"
         "The actual outside ground measure is invariant.  [LC9–LC11]",
         fontsize=12,color="#233c52")

ab=fig.add_axes([.045,.09,.91,.235]);ab.axis("off")
ab.add_patch(Rectangle((0,0),1,1,facecolor="#edf4eb",edgecolor="#b7c9b4",lw=1))
ab.text(.025,.79,r"$\kappa\langle K_Q\rangle+b\,\mu W_Q\leq b\Lambda_Q,"
        r"\qquad\Lambda_Q=\min\{2M_Q,6g^2\sqrt{N_QM_Q}\}+2C_Q$",
        fontsize=18,color="#173b28")
ab.text(.025,.51,r"$B_{f,j}^{de}=a_j^3\sum_p f(x_{p,j})W_p"
        r"\quad\longrightarrow\quad 2\int_{\mathbb{R}^3}f(x)\,d^3x\,I$",
        fontsize=20,color="#173b28")
ab.text(.025,.25,"Actual-vacuum norm, every original cyclic word and bounded time interval.\n"
        "No translation invariance or uniform individual-face expectation is used.",
        fontsize=13,color="#314a38")
fig.text(.045,.045,"Proof: LOCAL_CURVATURE_BUDGET.md, LC1–LC42. "
         "Original energy comparison: retained spatial author TeX, §12, (93)–(99).",
         fontsize=11,color="#516070")
fig.savefig(HERE/"LOCAL_CURVATURE_BUDGET.png",dpi=160)
fig.savefig(HERE/"LOCAL_CURVATURE_BUDGET.svg")
plt.close(fig)
