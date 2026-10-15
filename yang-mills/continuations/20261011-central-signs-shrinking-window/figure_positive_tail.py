from pathlib import Path
import numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15,7.3),facecolor='white')
ax=fig.add_axes([.035,.15,.49,.72]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#536577',lw=1.1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=13,linespacing=1.8)
box(.02,.76,.39,.2,r'$h_r=\sum_{s=r}^{L-1}v_s$'+'\n'+r'$h_r\in\mathscr{H}^{5}_{\zeta}$','#e7f1fa')
box(.59,.76,.39,.2,r'$W_r=-\mathscr{A}_{\zeta}h_r$'+'\n'+r'$W_r\in\mathscr{H}^{-1}_{\zeta}$','#eef5e8')
ax.annotate('',xy=(.58,.86),xytext=(.42,.86),arrowprops=dict(arrowstyle='->',lw=1.5))
ax.text(.50,.94,r'$-\mathscr{A}_{\zeta}$',ha='center',fontsize=14)
box(.06,.40,.88,.22,r'$\mathcal{R}_{\zeta}^{1/2}h_r=-\mathcal{N}_{\zeta}^{1/2}W_r$'+'\n'+r'$\|\mathcal{R}_{\zeta}^{1/2}h_r\|^2=\langle W_r,\mathcal{N}_{\zeta}W_r\rangle$','#f7efe2')
for xx in [.21,.79]:ax.annotate('',xy=(xx,.63),xytext=(xx,.75),arrowprops=dict(arrowstyle='->',lw=1.3))
box(.06,.035,.88,.24,r'$\frac{\zeta}{100}\,\mathfrak{b}_r\leq'
    r'\|\mathcal{R}_{\zeta}^{1/2}h_r\|^2'
    r'\leq\frac{43\zeta}{25}\,\mathfrak{b}_r$'
    +'\n'+r'$\mathfrak{b}_r=\langle W_r,(\mathcal{L}+\zeta)^{-1}W_r\rangle$','#f3f3f3')
ax.annotate('',xy=(.5,.285),xytext=(.5,.39),arrowprops=dict(arrowstyle='->',lw=1.3))
ax2=fig.add_axes([.615,.25,.355,.56])
x=np.logspace(-4,3,1600);q=(x+1)*(x+.25)*(x+4)
r=43/25*x**5-.5*x**4-3401/400*x**3+19/4*x*x+697/100*x+1
ratio=(x+1)*r/q**2
ax2.loglog(x,ratio,color='#24577e',lw=2.4,label=r'$(x+1)r(x)/q_1(x)^2$')
ax2.axhline(.01,color='#a55a22',ls='--',lw=1.4,label='Proved lower bound 1/100')
ax2.axhline(43/25,color='#376346',ls='--',lw=1.4,label='Sharp upper bound 43/25')
ax2.set(xlabel=r'$x=\lambda/\zeta$; inverse $\lambda=\zeta x$',ylabel='Complete scalar multiplier ratio',ylim=(.006,2.7))
ax2.grid(alpha=.2,which='both');ax2.legend(loc='upper left',bbox_to_anchor=(0,1.23),fontsize=10)
fig.text(.5,.955,'The complete signed tail and its exact residual map',ha='center',fontsize=20,weight='bold')
fig.text(.5,.07,'PST5–PST8: every annular and face mixed entry is retained. The squared tail norm is the sum of all Gram entries.',ha='center',fontsize=12)
fig.text(.5,.035,'The curve evaluates the exact multiplier; it is not a Yang–Mills spectral measurement. No source or state is rescaled.',ha='center',fontsize=11,color='#444444')
for ext in ['png','svg']:fig.savefig(O/('COMPLETE_TAIL_RESIDUAL_MAP.'+ext),dpi=180)
plt.close(fig)
print('Rendered complete residual-map figure.')
