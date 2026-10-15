from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np
from evaluate_weighted_cubic import constants
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,8),facecolor='white')
ax=fig.add_axes([.035,.18,.44,.65])
ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(y,text,color):
    ax.add_patch(FancyBboxPatch((.035,y),.93,.16,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#596675'))
    ax.text(.5,y+.08,text,ha='center',va='center',fontsize=13,linespacing=1.6)
box(.80,r'$t=\mathcal{B}_{\zeta}^{-1}F$'+'\n'+r'Original energy, full Hessian and ordered fields','#e9f1f8')
box(.48,r'$D_{3,0}(t),\ D_{2,1}(t)$'+'\n'+r'WKM8–WKM9: all commutator terms retained','#eef4e8')
box(.16,r'$D_{1,2}(t),\ D_{0,3}(t)$'+'\n'+r'WKM10: the entire ten-row cubic equation','#f7eee3')
for y in [.76,.44]:
    ax.annotate('',xy=(.5,y-.10),xytext=(.5,y),arrowprops=dict(arrowstyle='->',lw=1.8))
ax.text(.5,.035,r'$D_{m,r}(t)^2=\sum_{|J|=m}\|X_J\Delta_Q^rt\|_\rho^2$',ha='center',fontsize=14)
bx=fig.add_axes([.56,.22,.40,.56])
js=np.unique(np.rint(np.geomspace(4,1024,70))).astype(int)
direct=[];weighted=[]
for j in js:
    d=constants(str(j))
    direct.append(float(d['direct_energy'].value/d['old']['energy'].value))
    weighted.append(float(d['weighted_energy'].value/d['old']['energy'].value))
bx.loglog(js,direct,color='#176b9c',lw=2,label='Complete six-row bound / full pair bound')
bx.loglog(js,weighted,color='#b76521',lw=2,label='Weighted pair bound / full pair bound')
bx.axhline(1,color='#666666',lw=1,ls='--')
bx.set_xlabel('Original regulator index j')
bx.set_ylabel('Quotient of the complete upper functions')
bx.grid(True,which='both',alpha=.18)
bx.legend(loc='upper right',fontsize=9)
bx.set_title(r'$\kappa_*=4/5,\ \theta=1,\ a=(100j)^{-1},\ L=j^4$',fontsize=13,pad=14)
fig.text(.5,.93,'Trial-weighted variance and the complete cubic derivatives',ha='center',fontsize=21,weight='bold')
fig.text(.5,.13,r'WKM1–WKM7 retain the multiplier $\Delta_Q^2t$, the derivative cost and every variance remainder.',ha='center',fontsize=13)
fig.text(.5,.075,'WKM11–WKM14 retain all six residual rows and every mixed entry. Both upper functions still have power 76.',ha='center',fontsize=12)
fig.text(.5,.035,'WKM15 gives a further exact first-derivative identity. No vanishing error or continuum no-gap result is asserted.',ha='center',fontsize=12)
for ext in ['png','svg']:
    fig.savefig(O/('WEIGHTED_CUBIC_DERIVATIVES.'+ext),dpi=180)
plt.close(fig)
