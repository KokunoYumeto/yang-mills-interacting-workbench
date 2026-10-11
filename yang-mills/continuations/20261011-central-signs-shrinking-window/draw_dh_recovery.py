"""Exact cutoff section and recovered distribution/Hilbert maps."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

R=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,axs=plt.subplots(1,2,figsize=(16,7),gridspec_kw={'width_ratios':[1,1.15]},facecolor='#f7f9fc')
fig.subplots_adjust(left=.06,right=.965,bottom=.22,top=.8,wspace=.24)
blue='#194f88';green='#13624b';ink='#1c2b3d';red='#9c3343'
def eta(u):
    u=np.asarray(u);a=np.zeros_like(u,dtype=float);b=np.zeros_like(u,dtype=float)
    good=u>.5;a[good]=np.exp(-1/(u[good]-.5))
    good=u<1;b[good]=np.exp(-1/(1-u[good]))
    return a/(a+b)
x=np.linspace(-1,-.7,4001)
e=np.sin(np.pi*(x+1)/2)
ax=axs[0]
ax.plot(x,e,color=ink,lw=2.7,label=r'$e_{(1,1,1),1}(x,0,0)$')
for lv,col in [(1,'#dc883a'),(3,blue),(5,green)]:
    delta=2**(-lv-2)
    cutoff=eta((x+1)/delta)*eta((1-x)/delta)
    ax.plot(x,cutoff*e,color=col,lw=1.8,ls='--',label=fr'$\chi_{{1,{lv}}}\,e,\quad \delta_{{1,{lv}}}=2^{{-{lv+2}}}$')
ax.set_title('A  Interior tests approach the original sine coordinate',loc='left',fontsize=14,color=ink,pad=16)
ax.set_xlabel(r'$x_1$, on the section $x_2=x_3=0$')
ax.set_ylabel('Unchanged sine value and its cutoff')
ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=10.5)
ax.text(0,-.23,r'$\|e_{k,n}-\chi_{n,l}e_{k,n}\|_\infty\leq'
        r'\frac{\pi\max_d k_d}{8n^{3/2}}\,2^{-l}$',
        transform=ax.transAxes,fontsize=15,color=ink)

ax=axs[1];ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.set_title('B  The actual-law section retains the ambient kernel',loc='left',fontsize=14,color=ink,pad=16)
def box(x,y,w,h,text,col=blue,fs=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012,rounding_size=.02',facecolor='white',edgecolor=col,lw=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=fs,color=ink,linespacing=1.6)
def arrow(a,b,label=None):
    ax.annotate('',xy=b,xytext=a,arrowprops=dict(arrowstyle='-|>',color=blue,lw=1.7,mutation_scale=15))
    if label:ax.text((a[0]+b[0])/2,(a[1]+b[1])/2+.035,label,ha='center',color=blue,fontsize=12)
box(.02,.68,.4,.21,r'$\mathcal{S}_{n,s}\subset\mathcal{H}_n^{-s}$'+'\n'+'Actual path representatives',green,13)
box(.59,.68,.39,.21,r'$q(\mathcal{S}_{n,s})$'+'\n'+'Exact quotient classes',green,13)
arrow((.44,.8),(.57,.8),'q')
arrow((.785,.65),(.785,.43))
box(.16,.22,.82,.19,r'$Y_{n,k}(t)=\lim_l\langle\mathscr{Y}(t),\chi_{n,l}e_{k,n}\rangle$'+'\n'+'Uniformly on compact time intervals, almost surely',green,12.6)
arrow((.2,.65),(.2,.43))
ax.text(.04,.10,r'$\mathcal{S}_{n,s}\cap\mathcal{N}_{n,s}=\{0\}$, but '
        r'$\mathcal{N}_{n,s}$ is infinite-dimensional.',fontsize=12.3,color=ink)
ax.text(.04,.015,'The inverse section is measurable and is not continuous.',fontsize=12.3,color=red)
fig.suptitle('Interior-test recovery of the actual spatial curvature histories',fontsize=21,fontweight='bold',color=ink,y=.95)
fig.text(.53,.11,r'$\mathbb{E}\|\Delta Y_n\|_{-s,n}^{2p}\leq(2p-1)!!\,(\mathsf{c}_{s,n}|t-u|)^p$  (DR15)',fontsize=14,color=green)
fig.text(.06,.04,'DR5–DR11 prove recovery; DR2–DR4 exhibit the boundary kernel. DR12–DR14 give the section; DR15–DR17 prove the stronger Hilbert modulus.',fontsize=11,color='#59697a')
fig.savefig(R/'DH_REPRESENTATIVE_RECOVERY.png',dpi=180)
fig.savefig(R/'DH_REPRESENTATIVE_RECOVERY.svg')
print('Rendered DH_REPRESENTATIVE_RECOVERY.png and .svg')
