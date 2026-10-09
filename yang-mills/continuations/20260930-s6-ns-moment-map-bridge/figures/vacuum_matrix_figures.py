"""Reproducible plots of proved bounds, preserving the original regulator."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
W=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"svg.fonttype":"none"})
fig,axes=plt.subplots(1,2,figsize=(13.2,5.4),layout="constrained")
j=np.arange(2,61,dtype=float);k=1
M=3*(2*j**4)**2*(2*j**4+1);N=3*(2*j**4)*(2*j**4+1)**2
alpha=np.minimum(1,3*k/(100*j)*np.sqrt(N/M))
B=np.minimum(1,(np.sqrt(alpha)+np.exp(-M/416))**2)
axes[0].plot(j,B,color="#126e82",lw=2.5)
axes[0].set(xlabel="Original path index j",ylabel="Proved upper bound",
            title="Actual vacuum mass in the electric cutoff")
axes[0].text(.04,.92,r"$\|{\mathsf{P}}_{M_j/4096}\psi_j\|^2\leq B_{{\rm el},j}$",
             bbox=dict(facecolor="white",edgecolor="none",alpha=.9),transform=axes[0].transAxes,va="top",fontsize=14)
axes[0].grid(alpha=.25)
axes[1].plot(j,k*M*(1-B)/(4096*j**12),color="#925023",lw=2.5,label="Finite lower bound / $j^{12}$")
axes[1].axhline(3*k/512,color="#374151",ls="--",label=r"$3\kappa_*/512$")
axes[1].set(xlabel="Original path index j",ylabel="Proved lower bound",
            title="Full vacuum energy with its scalar retained")
axes[1].legend(loc="lower right");axes[1].grid(alpha=.25)
fig.suptitle("PK207-PK211: electric vacuum concentration on the unchanged path",fontsize=16)
fig.supxlabel(r"$L_j=j^4,\ a_j=1/(100j),\ g_j^2=\kappa_*/(200j),\ \kappa_*=1$."
              "\nCurves are proved bounds; they are not measured eigenvalues or excitation gaps.",fontsize=10)
for ext in ["png","svg"]:fig.savefig(W/("ACTUAL_VACUUM_ELECTRIC_CONCENTRATION."+ext),dpi=180)
plt.close(fig)
fig,ax=plt.subplots(figsize=(13.2,6.2),layout="constrained");ax.axis("off")
rows=[
("Original actual state",r"$H=\kappa H_0+b(2M-\mathcal{W}),\quad H\psi=E_0\psi,\quad \int\psi^2dU=1$"),
("Complete finite provider",r"$H_\Lambda=\mathsf{P}_\Lambda H\mathsf{P}_\Lambda,\quad H_\Lambda\phi_\Lambda=u_\Lambda\phi_\Lambda$"),
("Proved vacuum error",r"$\delta_{\rm v}=3\kappa e^{-32\pi(b/\kappa)M},\quad \eta_\Lambda=(u_\Lambda-e_\Lambda)/\delta_{\rm v}$"),
("All three actual matrices",r"$\|\mathcal{G}-\mathcal{G}^\Lambda\|\leq\epsilon_G,\quad"
 r"\|\mathcal{C}-\mathcal{C}^\Lambda\|\leq\epsilon_C,\quad"
 r"\|\mathcal{Q}-\mathcal{Q}^\Lambda\|\leq\epsilon_Q$"),
("Full complementary return",r"$\Sigma_R=\mathcal{Q}_R-\mathcal{C}_R\mathcal{G}_R^{-1}\mathcal{C}_R\ \geq0$"),
("Original raw spectral weight",r"$\nu_c((0,s])\geq\max\{0,\ c^*(\mathcal{G}^\Lambda-\epsilon_G I)c"
 r"-s^{-1}c^*(\mathcal{C}^\Lambda+\epsilon_C I)c\}$")]
for i,(title,formula) in enumerate(rows):
    yy=.94-i*.147
    ax.text(.02,yy,title,weight="bold",fontsize=12,color="#126e82",transform=ax.transAxes,va="top")
    ax.text(.30,yy,formula,fontsize=12.5,transform=ax.transAxes,va="top")
    if i<5:ax.plot([.02,.98],[yy-.095,yy-.095],color="#d5dde0",lw=1,transform=ax.transAxes)
fig.suptitle("PK212-PK227: certified matrices retain the actual vacuum and the full residual",fontsize=15)
fig.supxlabel("Every cutoff contains all permitted electric sectors and every original magnetic face."
              "\nThe shrinking-window lower endpoint still has to be evaluated; a positive limit is not assumed.",fontsize=10)
for ext in ["png","svg"]:fig.savefig(W/("ACTUAL_VACUUM_MATRIX_RECEIVING_MAP."+ext),dpi=180)
plt.close(fig)
