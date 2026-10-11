from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).parent
fig=plt.figure(figsize=(12,7.4),layout="constrained")
gs=fig.add_gridspec(2,2,width_ratios=[1.45,1])
flow=fig.add_subplot(gs[:,0]); flow.set_xlim(0,1);flow.set_ylim(0,1);flow.axis("off")
flow.text(.02,.98,"The original vacuum law and its exact conditionals",fontsize=14,weight="bold",va="top")
def box(y,title,formula,height=.13):
    flow.add_patch(FancyBboxPatch((.035,y),.93,height,boxstyle="round,pad=0.01",fc="#edf4fa",ec="#557a98",lw=1.2))
    flow.text(.5,y+height-.027,title,ha="center",va="top",fontsize=11,weight="bold")
    flow.text(.5,y+.038,formula,ha="center",va="center",fontsize=12)
def arrow(top,bottom,label):
    flow.annotate("",xy=(.50,bottom),xytext=(.50,top),arrowprops={"arrowstyle":"->","lw":1.5,"color":"#34556f"})
    flow.text(.52,(top+bottom)/2,label,fontsize=10,va="center")
box(.78,"Independent original edge noise and outside paths",r"$\mathbb{P}_e\otimes\mathbb{P}_{\bar e}$")
arrow(.77,.64,r"multiply by $Z_t^{\mathrm{vac}}$  [ID8–ID10]")
box(.49,"The complete tilted vacuum law",r"$d\mathbb{Q}_x=q_y\,d\mathbb{P}_e\,d\mathbb{Q}_{\bar e}(y)$",.15)
arrow(.48,.35,"condition on the entire outside path  [ID21–ID24]")
box(.19,"The conditional edge-noise law",r"$q_y=R_y/Z_y,\quad R_y=e^{-\int_0^tV_e\,ds}\psi(X_t^e,y_t)$",.16)
flow.text(.035,.125,r"$D_t=\omega_e+4\kappa\beta t,\qquad I_y\leq J(D_t)\leq D_t$",fontsize=13)
flow.text(.035,.065,"The terminal vacuum and every outside path remain.\nFull entropy also contains the outside-marginal entropy [ID28].",fontsize=10,linespacing=1.5)

ax=fig.add_subplot(gs[0,1])
d=np.linspace(0,8,400)
a=np.ones_like(d)
a[1:]=d[1:]/(-np.expm1(-d[1:]))
j=a-1-np.log(a)
ax.plot(d,d,color="#909ba3",ls="--",label=r"$D$")
ax.plot(d,j,color="#126782",lw=2.2,label=r"$J(D)=A(D)-1-\log A(D)$")
ax.set(xlabel="Logarithmic range D",ylabel="Entropy upper bound",title="Exact range bounds [ID55–ID56]")
ax.grid(alpha=.22);ax.legend(fontsize=9,loc="upper left")
ax.text(.03,.45,r"$A(D)=D/(1-e^{-D}),\quad J(0)=0$",transform=ax.transAxes,fontsize=10)
note=fig.add_subplot(gs[1,1]);note.axis("off")
note.text(.01,.95,"The exact mixture identity [ID53–ID54]",va="top",fontsize=12,weight="bold")
note.text(.01,.78,r"$\int I_y\,d\mathbb{Q}_{\bar e}$",fontsize=14)
note.text(.01,.61,r"$=\mathrm{Ent}(\mathbb{Q}_e\mid\mathbb{P}_e)$",fontsize=14)
note.text(.01,.43,r"$\quad+\mathrm{Ent}(\mathbb{Q}_x\mid\mathbb{Q}_e\otimes\mathbb{Q}_{\bar e})$",fontsize=13)
note.text(.01,.18,"The nonnegative second term is mutual information.\nDiscarding it yields the proved edge-marginal bound.\nThe right plot shows formulas, not a sampled vacuum.",fontsize=10,linespacing=1.6)
fig.suptitle("Conditional edge entropy — original radius-two SU(2) metric",fontsize=16,weight="bold")
fig.savefig(root/"CONDITIONAL_ENTROPY.png",dpi=160)
fig.savefig(root/"CONDITIONAL_ENTROPY.svg")
print(str(root/"CONDITIONAL_ENTROPY.png"))
