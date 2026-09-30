"""Illustrate the proved support cones and the core curvature invariant."""
import json
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

ROOT=Path(__file__).resolve().parent
r,R,T=1.0,2.0,2.2
fig,axes=plt.subplots(1,2,figsize=(13,6),gridspec_kw={"width_ratios":[1,1.15]})
ax=axes[0]
ss=np.linspace(-T,T,1201)
ax.fill_betweenx(ss,0,R+np.abs(ss),color="#dce9f4",label="proved support upper bound")
ax.plot(R+np.abs(ss),ss,color="#24547a",lw=2)
inner=np.maximum(0,r-np.abs(ss))
ax.fill_betweenx(ss,0,inner,where=np.abs(ss)<r,color="#efb15f",label="exact homogeneous core")
ax.plot(inner[np.abs(ss)<=r],ss[np.abs(ss)<=r],color="#a85b08",lw=2)
ax.axhline(0,color="#64748b",lw=0.8)
ax.axvline(0,color="#64748b",lw=0.8)
ax.text(2.5,1.15,r"$\rho=R+|s|$",color="#24547a",rotation=44,fontsize=11)
ax.text(0.54,0.52,r"$\rho+|s|=r$",color="#764009",rotation=-42,fontsize=10)
ax.text(3.5,0.1,"zero field",ha="center",fontsize=11)
ax.set(xlim=(0,R+T+.12),ylim=(-T,T),xlabel=r"$\rho=|x|$",ylabel=r"$s=x^0=ct$",
       title="Finite-energy solution through the cutoff")
ax.set_xticks([0,r,R,R+T],["0","r = 1","R = 2","R + T"])
ax.legend(loc="lower right",fontsize=8,framealpha=.96)
ax.set_aspect("equal",adjustable="box")

positive=np.linspace(0,r,2001)
sol=solve_ivp(lambda t,u:[u[1],-8*u[0]**3],(0,r),[1,0],
              rtol=1e-11,atol=1e-12,dense_output=True)
assert sol.success
times=np.linspace(-r,r,2401)
f,fp=sol.sol(np.abs(times))
fp=fp*np.sign(times)
magnetic=256*f**8
electric=16*fp**4
total=magnetic+electric
ax=axes[1]
ax.plot(times,magnetic,color="#b66a0b",lw=1.7,label=r"$|[F_{12},F_{23}]|^2=256 f^8$")
ax.plot(times,electric,color="#276d9e",lw=1.7,label=r"$|[F_{01},F_{02}]|^2=16(f')^4$")
ax.plot(times,total,color="#293a2c",lw=2.4,label=r"$\mathcal{I}=$ sum of both")
ax.axhline(128,color="#6b6770",ls="--",lw=1.3,label=r"proved bound $\mathcal{I}\geq128$")
ax.set(xlim=(-r,r),ylim=(0,280),xlabel=r"$s$ along $x=0$, within $|s|<r$",
       ylabel="original matrix trace squared norm",
       title="Non-Abelian curvature persists through magnetic zeros")
ax.set_yticks([0,128,256])
ax.grid(alpha=.15)
ax.legend(loc="lower center",bbox_to_anchor=(.5,-.42),fontsize=9,ncol=2)
fig.subplots_adjust(left=.065,right=.98,top=.87,bottom=.29,wspace=.29)
fig.suptitle("Original compact support → global smooth classical evolution",fontsize=17,y=.98)
fig.text(.065,.15,
    "Left: a radial spacetime section, with illustrative r = 1, R = 2. "
    "The theorems retain arbitrary 0 < r < R.\n"
    "Right: numerical rendering of the exact core ODE f″ + 8f³ = 0; "
    "f(0) = 1, f′(0) = 0. The bound is proved algebraically.",
    fontsize=9,linespacing=1.5)
fig.text(.065,.04,
    "Proof: COMPACT_SUPPORT_CAUCHY_EVOLUTION.md, Proposition 3.1, Corollary 3.2, CE12–CE17.\n"
    "Global analytical input: Sung-Jin Oh, arXiv:1210.1557v2. "
    "No quantum spectral-gap conclusion is asserted.",fontsize=8,color="#4b5563",linespacing=1.4)
for ext in ("png","svg"):
    fig.savefig(ROOT/("COMPACT_CAUCHY_EVOLUTION."+ext),dpi=190,facecolor="white")
receipt={"scope":"numerical rendering only; analytic support law and invariant bound are proved in the note",
         "illustrative_r":r,"illustrative_R":R,
         "max_ODE_energy_residual":float(np.max(np.abs(fp**2+4*f**4-4))),
         "sampled_min_invariant":float(total.min()),
         "proved_bound":128}
(ROOT/"COMPACT_CAUCHY_FIGURE_CHECK.json").write_text(json.dumps(receipt,indent=2)+"\n",
    encoding="utf-8",newline="\n")
print(json.dumps(receipt))
