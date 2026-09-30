"""Reproduce the carrier square and a numerical rendering of its core evolution."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from scipy.integrate import quad, solve_ivp

OUT=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,11),layout="constrained")
grid=fig.add_gridspec(3,2,height_ratios=[1.35,1,0.25])
ax=fig.add_subplot(grid[0,:])
ax.set(xlim=(0,1),ylim=(0,1))
ax.axis("off")
ax.set_title("The retained reduction has a higher carrier and an exact core evolution",
             fontsize=17,pad=15)

def box(x,y,w,h,label,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle="round,pad=0.012",
                 linewidth=1.5,edgecolor=color,facecolor=color+"18"))
    ax.text(x+w/2,y+h/2,label,ha="center",va="center",fontsize=12,linespacing=1.5)
def arrow(a,b,label,offset=(0,0.025)):
    ax.annotate("",xy=b,xytext=a,arrowprops=dict(arrowstyle="->",lw=1.6,color="#444444"))
    ax.text((a[0]+b[0])/2+offset[0],(a[1]+b[1])/2+offset[1],label,
            ha="center",va="center",fontsize=11,backgroundcolor="white")
box(.05,.66,.22,.22,r"$P_H$"+"\n"+r"retained $\operatorname{Sp}(1)$ bundle","#206090")
box(.48,.66,.24,.22,r"$L=F_4$"+"\n"+r"principal $K=\rho(\operatorname{Sp}(1))$ bundle","#206090")
box(.05,.19,.22,.22,r"$X\simeq S^6$"+"\n"+r"nonzero order-two clutching","#297b50")
box(.48,.19,.24,.22,r"$D=F_4/K$"+"\n"+r"$\dim D=49$","#297b50")
box(.80,.19,.17,.22,r"$M=F_4/G$"+"\n"+r"$\dim M=24$","#75509a")
arrow((.27,.77),(.48,.77),r"$p\mapsto a_p$")
arrow((.16,.65),(.16,.43),r"pullback",offset=(.065,0))
arrow((.60,.65),(.60,.43),r"bundle",offset=(.06,0))
arrow((.27,.30),(.48,.30),r"$r_H=jf_H$")
arrow((.73,.30),(.79,.30),r"$\pi$",offset=(0,.08))
ax.text(.80,.72,r"$G=\operatorname{Spin}(8)$"+"\n"+r"$\pi^{-1}(G)=G/K$"+"\n"+r"$\dim(G/K)=25$",
        ha="left",va="center",fontsize=12,linespacing=1.6)
ax.text(.49,.06,r"$r_H^*(L\to D)\cong P_H,\qquad r_H^*E_D\cong\mathcal{W}_H,\qquad E_D\cong\pi^*TM$",
        ha="center",va="center",fontsize=13)
ax.text(.50,.96,r"$\pi r_H$ is constant; the nontrivial retained class lies in the reduction fibre.",
        ha="center",fontsize=11,color="#444444")

quarter=quad(lambda u:1/(2*np.sqrt(1-u**4)),0,1,epsabs=1e-11)[0]
ts=np.linspace(0,4*quarter,1000)
sol=solve_ivp(lambda t,y:[y[1],-8*y[0]**3],[0,ts[-1]],[1,0],
              t_eval=ts,rtol=2e-11,atol=2e-13)
assert sol.success
f,fp=sol.y
left=fig.add_subplot(grid[1,0])
left.plot(ts,f,color="#206090",lw=2,label=r"$f(s)$")
left.axhline(0,color="#999999",lw=.7)
left.set(xlabel=r"$s=x^0=ct$",ylabel=r"$f(s)$",
         title=r"$A_j=2f(s)T_j,\quad f''+8f^3=0$")
left.grid(alpha=.2)
right=fig.add_subplot(grid[1,1])
right.plot(ts,48*f**4,lw=2,label=r"magnetic: $48f^4$")
right.plot(ts,12*fp**2,lw=2,label=r"electric: $12(f')^2$")
right.axhline(48,color="#333333",ls="--",label="sum = 48")
right.set(xlabel=r"$s=x^0=ct$",ylabel="Retained curvature density",
          title=r"$\varepsilon=24/g^2$; torus energy $=24\ell_1\ell_2\ell_3/g^2$")
right.set_ylim(-1,52)
right.legend(fontsize=10,loc="upper right")
right.grid(alpha=.2)
caption=fig.add_subplot(grid[2,:])
caption.axis("off")
caption.text(.5,.65,
    "Proof: HIGHER_CARRIER_AND_EVOLUTION.md, Theorem 2.1 and equations HC25–HC27.\n"
    "Curves are numerical renderings of the proved homogeneous ODE. The original compact-support boundary remains to be solved.\n"
    "Human sources: Yokota (2009), Theorems 1.16.2 and 2.7.1; Tsapalis et al. (2016), equation B8.",
    ha="center",va="center",fontsize=10,linespacing=1.5)
fig.savefig(OUT/"HIGHER_CARRIER_EVOLUTION.png",dpi=180)
fig.savefig(OUT/"HIGHER_CARRIER_EVOLUTION.svg")
print({"quarter_period_rendering":quarter,
       "maximum_numeric_energy_residual":float(np.max(abs(12*fp**2+48*f**4-48)))})
