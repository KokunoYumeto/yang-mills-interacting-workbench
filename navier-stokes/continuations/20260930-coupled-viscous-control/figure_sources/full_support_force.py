"""Reproducible schematic of the exact physical force and annulus bound."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle

BASE=Path(__file__).resolve().parents[1]
LANE=BASE/'source'
fig,axes=plt.subplots(1,2,figsize=(12,5),gridspec_kw={'width_ratios':[1,1.35]})
ax=axes[0]
ax.add_patch(Circle((0,0),1,facecolor='#e7c49a',edgecolor='#885526',linewidth=2))
ax.add_patch(Circle((0,0),.5,facecolor='#d0ebdf',edgecolor='#267354',linewidth=2))
ax.text(0,.07,'Exact affine core',ha='center',fontsize=12)
ax.text(0,-.13,r'$\chi=1,\quad |x|\leq r/2$',ha='center',fontsize=11)
ax.text(0,.74,'Cutoff annulus',ha='center',fontsize=12)
ax.text(0,-.78,r'$d\Delta h,\ d\Delta z$ retained',ha='center',fontsize=11)
ax.text(0,1.22,'Full retained parent is affine on this support',ha='center',fontsize=10)
ax.text(0,-1.28,'Outside the ball: state and force equal the parent',ha='center',fontsize=10)
ax.set(xlim=(-1.7,1.7),ylim=(-1.55,1.55),aspect='equal')
ax.axis('off')
ax=axes[1]
rad=np.linspace(.12,1,300)
ax.plot(rad,2/rad-3*rad,color='#9a352b',linewidth=2.3)
ax.axhline(0,color='#777777',linewidth=.8)
ax.fill_between(rad,2/rad-3*rad,18,color='#edd9d6',alpha=.5)
ax.set(xlim=(.12,1),ylim=(-1,18),xlabel='Support radius r',ylabel='Force lower bound')
ax.set_title(r'$\|e^u\|_\infty\geq 2d\|L\|/r-rV_{0,0}$',fontsize=13)
ax.grid(alpha=.2)
ax.text(.97,.94,'Illustrative parameter values only:\nd = 1, ‖L‖ = 1, V₀,₀ = 3',ha='right',va='top',transform=ax.transAxes,fontsize=10)
fig.suptitle('Shrinking the cutoff requires additional signed cancellation',fontsize=15)
fig.text(.5,.015,'Proof: ifs:physical-vector-jets, ifs:cutoff-diffusion-lower-bound, ifs:force-lower-bounds. The graph is a bound, not a computed trajectory.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.06,1,.93))
dest=LANE/'infinite_modified/figures/full_support_force.png'
fig.savefig(dest,dpi=170)
plt.close(fig)
print(str(dest))
