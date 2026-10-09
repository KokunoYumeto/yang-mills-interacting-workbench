"""Original graph subset and exact per-face upper bound from PK89--PK96."""
from pathlib import Path
import math
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
OUT=Path(__file__).resolve().parent
plt.rcParams.update({"font.family":"DejaVu Sans","font.size":11,"svg.hashsalt":"YM-packet-escape-20261009"})
fig=plt.figure(figsize=(15,9),facecolor="#f7f9fc")
fig.text(.05,.95,"The fixed-heat packet leaves low-energy spectral intervals",fontsize=20,weight="bold",color="#17364a")
fig.text(.05,.905,r"$H_j=\kappa_*H_{0,j}+2b_jM_j^{\rm face}-b_j\mathcal{W}_j$   |   $b_j=10000j^2/\kappa_*$   |   original packet norm $\Gamma_j$ retained",fontsize=13)
ax=fig.add_axes([.055,.365,.36,.45])
L=2
for a in range(-L,L+1):
    ax.plot([a,a],[-L,L],color="#b9c4cf",lw=1)
    ax.plot([-L,L],[a,a],color="#b9c4cf",lw=1)
for u in range(L):
    for v in range(L):
        ax.add_patch(Rectangle((-L+2*u,-L+2*v),1,1,facecolor="#b6dccd",edgecolor="#146a51",lw=3))
ax.set_aspect("equal");ax.set_xticks(range(-2,3));ax.set_yticks(range(-2,3))
ax.set_xlabel(r"$n_1$");ax.set_ylabel(r"$n_2$")
ax.set_title(r"One $n_3$ layer, $L=2$; coordinates $n_i$"+"\nPhysical coordinates are "+r"$o+a n$",fontsize=12)
ax.text(.0,-.29,"Green faces have no common links.\nAll layers give "+r"$n_L=L^2(2L+1)=M_L/12$."+"\nThe full Hamiltonian keeps every face.",transform=ax.transAxes,fontsize=12)
ax2=fig.add_axes([.505,.39,.445,.41])
t=1.;r=.1;R=1.
zbar=(1+math.exp(-t/4))/(1-math.exp(-t/4))**3
cH=8*math.sqrt(2/math.pi)*math.exp(1.5)
cg=32*24*(25*r/math.sqrt(3))**3*(2/(100*math.pi))**8*math.exp(-6*t)
xx=np.linspace(math.log(600),210,600)
inverse_n=np.exp(-12*xx)/(2+np.exp(-4*xx))
yy=2*(12+6*np.exp(-4*xx))*math.log(zbar)+math.log(cH)-.75*xx+(15*xx-math.log(cg))*inverse_n
ax2.axhline(0,color="#8c3c28",lw=1.2)
ax2.plot(xx,yy,color="#234f8e",lw=2.5)
ax2.set_xlabel(r"$\log j$   (envelope of the integer sequence)")
ax2.set_ylabel(r"upper bound for $\log A_j/n_j$")
ax2.set_title("Exact asymptotic estimate; no sampled eigenvalues",fontsize=12)
ax2.grid(alpha=.2)
ax2.text(0,-.30,r"$t_*=1,\ r=1/10,\ R=1;\quad Z_{t_*}\leq(1+e^{-1/4})/(1-e^{-1/4})^3$"+"\nThe complete expression (PK96) is plotted,\nusing the retained constant from (PK49).",transform=ax2.transAxes,fontsize=11)
fig.text(.05,.155,r"$\nu_j((0,\kappa_*j])\leq\Gamma_jR_j,\qquad R_j\longrightarrow0$   (PK93–PK96)",fontsize=18,color="#146a51")
fig.text(.05,.104,"The actual packet loses its fraction of mass below an expanding energy threshold.\nThis does not assert decay of its raw mass or exclude different interacting states.",fontsize=12,color="#17364a")
fig.text(.05,.035,"Proof: PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md, PK79–PK100. Graph and estimates derived there.\nPacket conventions: Bahr–Thiemann, arXiv:0709.4636v1, as compared in PK27–PK36.",fontsize=10,color="#425a6b")
fig.savefig(OUT/"PACKET_ESCAPE.png",dpi=160,facecolor=fig.get_facecolor())
fig.savefig(OUT/"PACKET_ESCAPE.svg",facecolor=fig.get_facecolor(),metadata={"Date":None})
print("Saved packet escape PNG and SVG.")
