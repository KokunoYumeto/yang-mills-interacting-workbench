"""Reproducible mathematical diagram; panel D is an explicit spectral example."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(17,12),facecolor='#f6f8fc')
grid=fig.add_gridspec(2,2,left=.045,right=.975,bottom=.09,top=.9,wspace=.16,hspace=.17)
axs=[fig.add_subplot(grid[i,j]) for i in range(2) for j in range(2)]
blue='#194f88';green='#13624b';red='#9c3343';ink='#1c2b3d';gray='#59697a'
def base(ax,title):
    ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
    ax.add_patch(FancyBboxPatch((0,0),1,1,boxstyle='round,pad=0.006,rounding_size=.018',facecolor='white',edgecolor='#cbd4e0',lw=1.3,clip_on=False))
    ax.text(.04,.935,title,fontsize=16,fontweight='bold',color=ink,va='top')
def box(ax,xy,width,height,content,color=blue,fs=14):
    x,y=xy
    ax.add_patch(FancyBboxPatch((x,y),width,height,boxstyle='round,pad=.012,rounding_size=.02',facecolor=color+'0d',edgecolor=color,lw=1.2))
    ax.text(x+width/2,y+height/2,content,ha='center',va='center',fontsize=fs,color=ink,linespacing=1.7)
def arrow(ax,start,end):
    ax.annotate('',xy=end,xytext=start,arrowprops=dict(arrowstyle='-|>',color=blue,lw=1.8,mutation_scale=16))

base(axs[0],'A  Original local curvature controls all gradient moments')
ax=axs[0]
box(ax,(.05,.61),.9,.19,r'$C_{f,j}=a_j\sum_{p:de} f(x_{p,j})(2-W_p)$'+'\n'+r'$\Gamma(C_{f,j})\leq 8a_j^2\|f\|_\infty^2 W_{Q_j}$')
arrow(ax,(.5,.585),(.5,.52))
box(ax,(.05,.29),.9,.21,r'$\limsup_j\ \mu_j[\Gamma(C_{f,j})^p]\leq\mathcal{G}_f^p$'+'\n'+r'$\mathcal{G}_f=8\|f\|_\infty^2(9\kappa_*R^3+24R^2)$',green)
ax.text(.05,.19,'The crossing-face contribution is the full '+r'$24R^2$'+'.',color=ink,fontsize=12)
ax.text(.05,.11,'Absolute curvature moments may grow; the phase stays unitary.',color=gray,fontsize=11.5)
ax.text(.05,.04,'CP3–CP11: original coefficient, orientations and patch counts.',color=gray,fontsize=10.5)

base(axs[1],'B  Bounded word ratios give an exact cyclic algebra')
ax=axs[1]
box(ax,(.05,.59),.9,.22,r'$w_j=\psi_j h_j,\quad \|h_j\|_\infty\leq H,\quad \sqrt{q_j(w_j)}\leq E$'+'\n'+r'$b:\ (H,E)\mapsto(MH,\ ME+H\sqrt{q_j(b\psi_j)})$',fs=13.5)
arrow(ax,(.5,.565),(.5,.51))
box(ax,(.05,.31),.9,.18,r'$\mathcal{K}=\overline{\mathrm{span}\{[w_j]\}}\ \subset P\mathcal{H}_{\mathcal{U}}$'+'\n'+r'$PBQCP|_{\mathcal{K}}=0$',green)
ax.text(.05,.215,'Products, adjoints and zero-time collisions are retained.',color=ink,fontsize=12)
ax.text(.05,.145,r'$T(t)|_{\mathcal{K}}=e^{-tA_{\mathcal{K}}},\quad A_{\mathcal{K}}\geq0,\quad \|\Omega\|=1$',color=ink,fontsize=15)
ax.text(.05,.04,'CP12–CP20: form bounds on words; no global gradient bound.',color=gray,fontsize=10.5)

base(axs[2],'C  The initial character and real time increments')
ax=axs[2]
box(ax,(.05,.68),.37,.13,r'$\chi(0)\in\mathbb{K}$',fs=17)
box(ax,(.57,.68),.38,.13,r'$Y(0)=0,\quad Y(t)\in\mathcal{Y}$',green,14)
arrow(ax,(.24,.65),(.4,.51));arrow(ax,(.76,.65),(.6,.51))
box(ax,(.05,.32),.9,.18,r'$\chi(t)(g)=\chi(0)(g)\,e^{iY_g(t)}$'+'\n'+r'$\mathbb{E}|Y_f(t)-Y_f(s)|^{2p}\leq(2p-1)!!(2\kappa_*\mathcal{G}_f|t-s|)^p$',fs=13.4)
ax.text(.05,.23,r'$R_f=\mathsf{E}_f(\iota(\mathbb{R}))$: reducing regular-character space.',color=ink,fontsize=12)
ax.text(.05,.16,'Its vacuum weight is retained and remains unevaluated.',color=red,fontsize=12)
ax.text(.05,.10,r'$e^{i\theta Y_f(t)}$ is continuous jointly in real $\theta$ and $t$.',color=green,fontsize=12)
ax.text(.05,.04,'CP21–CP43: tight histories, logarithmic modulus, exact centering.',color=gray,fontsize=10.5)

base(axs[3],'D  Unit norm does not determine positive energy')
ax=axs[3]
ax.text(.05,.82,r'$\nu_j=(1-j^{-1})\delta_0+j^{-1}\delta_j$',fontsize=16,color=ink)
ax.text(.05,.75,'Illustrative spectral measures — not actual vacuum data.',fontsize=11.5,color=red)
inset=ax.inset_axes([.12,.26,.8,.42])
j=np.geomspace(2,10000,160)
inset.loglog(j,np.ones_like(j),color=blue,lw=2.2,label=r'$\int\lambda\,d\nu_j=1$')
inset.loglog(j,(1-np.exp(-j))/j,color=green,lw=2.2,label=r'$1-K_j(1)=(1-e^{-j})/j$')
inset.set_xlabel(r'$j$',labelpad=1)
inset.set_ylim(7e-5,2)
inset.grid(alpha=.18,which='both')
inset.legend(loc='lower left',fontsize=11,framealpha=1)
ax.text(.05,.14,r'$\Delta=\lim_{R\to\infty}\lim_{\mathcal{U}}\int(\lambda-R)_+\,d\nu_j$',fontsize=14,color=ink)
ax.text(.05,.075,'CP44–CP50: exact zero/positive weights and first-energy defect.',fontsize=10.5,color=gray)
ax.text(.05,.025,'No nonzero positive-energy component is inferred from a first moment.',fontsize=10.2,color=red)

fig.suptitle('Actual bounded curvature phases: continuous time, exact algebra, retained defects',fontsize=21,color=ink,y=.965,fontweight='bold')
fig.text(.045,.035,'Proof locators refer to CURVATURE_PHASE_RECONSTRUCTION.md. All displayed constants retain the original path and vacuum form.',fontsize=11,color=gray)
fig.savefig(ROOT/'CURVATURE_PHASE_MAPS.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(ROOT/'CURVATURE_PHASE_MAPS.svg',facecolor=fig.get_facecolor())
print('Rendered CURVATURE_PHASE_MAPS.png and .svg')
