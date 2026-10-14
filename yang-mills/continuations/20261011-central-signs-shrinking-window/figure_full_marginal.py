from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,FancyBboxPatch,Polygon
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none'})
def save(fig,name):
    fig.savefig(O/(name+'.png'),dpi=160,facecolor='white');fig.savefig(O/(name+'.svg'),facecolor='white');plt.close(fig)
def box(ax,xywh,title,lines,color='#eef4f7',size=14,top_gap=.09):
    x,y,w,h=xywh;ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',facecolor=color,edgecolor='#7893a5',lw=1.2));ax.text(x+.025,y+h-.045,title,ha='left',va='top',fontsize=size,weight='bold',color='#244459')
    n=len(lines)
    positions=np.linspace(y+h-top_gap,y+.035,n) if n>1 else [y+h/2-.015]
    for line,pos in zip(lines,positions):ax.text(x+w/2,pos,line,ha='center',va='center',fontsize=size-1)
fig=plt.figure(figsize=(10.5,12.5));fig.suptitle('The actual full-state marginal ground equation\nAll remaining faces and gradient contributions retained',fontsize=17,y=.98)
grid=fig.add_gridspec(2,2,height_ratios=[1,1.1],hspace=.37,wspace=.38);ax=fig.add_subplot(grid[0,0])
def proj(p):x,y,z=p;return np.array([x+9*y/20,z+3*y/10])
corners=[(-1,0,0),(0,0,0),(1,0,0),(-1,1,0),(0,1,0),(1,1,0),(0,0,1),(1,0,1)]
for pts,col in [([(-1,0,0),(0,0,0),(0,1,0),(-1,1,0)],'#d7e7ed'),([(0,0,0),(1,0,0),(1,1,0),(0,1,0)],'#d7e7ed'),([(0,0,0),(1,0,0),(1,0,1),(0,0,1)],'#f7d9c0')]:ax.add_patch(Polygon([proj(p) for p in pts],color=col,alpha=.55))
patch=[((-1,0,0),(0,0,0)),((0,0,0),(1,0,0)),((-1,1,0),(0,1,0)),((0,1,0),(1,1,0)),((-1,0,0),(-1,1,0)),((0,0,0),(0,1,0)),((1,0,0),(1,1,0))]
outer=[((0,0,0),(0,0,1)),((0,0,1),(1,0,1)),((1,0,0),(1,0,1))]
for p,q in patch+outer:
    color='#be4e32' if (p,q)==outer[0] else ('#bd793e' if (p,q) in outer else '#245874')
    ax.add_patch(FancyArrowPatch(proj(p),proj(q),arrowstyle='-|>',mutation_scale=15,lw=2.1,color=color,shrinkA=5,shrinkB=5))
for p in corners:ax.plot(*proj(p),'o',color='#1d3342',ms=5)
ax.text(.5,-.15,r'$e: U_e=e^{\theta J_3}$',ha='center',fontsize=12);ax.text(-.16,.65,r'$f: U_f=e^{\eta J_3}$',rotation=90,ha='center',va='center',fontsize=12)
ax.text(.56,.64,'crossing face\n'+r'$T_p=2\cos(\theta-\eta)$',ha='center',fontsize=12)
ax.text(-.7,.5,'selected\nleft',ha='center',fontsize=11);ax.text(1.35,.45,'right',fontsize=11)
ax.text(.1,-.38,r'$J_3=-i\sigma_3$',fontsize=12);ax.set_xlim(-1.25,1.7);ax.set_ylim(-.48,1.4);ax.set_aspect('equal');ax.axis('off');ax.set_title('Original patch and crossing face\n[FMP10, FMP12]',fontsize=13)
ax=fig.add_subplot(grid[0,1]);t=np.linspace(0,np.pi/2,400);k=.8;j=1;a=1/(100*j);b=1/(k*a*a)
ax.plot(t,4*b*(np.cos(t)-1),color='#9a3e49',lw=2.8);ax.axhline(0,color='#435260',lw=.8);ax.grid(alpha=.2);ax.set_xlabel(r'$\theta=\eta=t$');ax.set_ylabel('full mixed potential difference');ax.ticklabel_format(axis='y',style='sci',scilimits=(0,0));ax.set_title('Exact four-configuration difference\n[FMP12]',fontsize=13)
ax.text(.05,.05,r'$4b(\cos t-1)<0$'+'\n'+r'$j=1,\ \kappa_*=0.8,\ a=0.01$'+'\n'+r'$b=1/(\kappa_*a^2)=12500$',transform=ax.transAxes,va='bottom',fontsize=11)
ax=fig.add_subplot(grid[1,:]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
box(ax,(.015,.73,.97,.24),'Actual conditional factorization  [FMP1-FMP4]',[r'$\rho=\Pi_0(\psi^2),\quad \alpha=\sqrt{\rho},\quad \psi=(\alpha\circ\pi)\chi$',r'$\Pi_0(\chi^2)=1,\qquad \tau=\Pi_0|d\chi|^2$'],size=14,top_gap=.14)
box(ax,(.015,.4,.97,.27),'Exact marginal ground equation  [FMP5-FMP6]',[r'$[-\kappa_*\Delta_7+4b-b(x+y)+W_{\rm eff}]\alpha=E_0\alpha$',r'$W_{\rm eff}=\mathbb{E}_\mu[V_{\rm rest}\mid\pi]+\kappa_*\tau$'],size=14,top_gap=.14)
box(ax,(.015,.055,.97,.28),'Both score contributions remain  [FMP8-FMP9]',[r'$\tau=\mathrm{Tr}(\Gamma^{-1}\Sigma)+\mathbb{E}_\mu[|(dw)_\perp|^2\mid\pi]$',r'$\Sigma\leq\tau\Gamma,\quad \|\mathcal{K}F\|^2=4\kappa_*^2\int\rho\,\partial F^*\Sigma\partial F\,d\nu_\Omega$'],size=14,top_gap=.14)
fig.text(.5,.025,'Spatial projection in the upper-left view: (X,Y,Z) → (X+9Y/20, Z+3Y/10).\nThe orange face uses one selected edge and one outside edge; its mixed term\nprevents additive separation of the original full Wilson potential.',ha='center',fontsize=11)
fig.subplots_adjust(left=.07,right=.96,top=.88,bottom=.1);save(fig,'FULL_MARGINAL_AND_CROSSING_FACE')

fig,ax=plt.subplots(figsize=(10.5,12.5));ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off');fig.suptitle('Original loop-gradient rigidity and actual lattice memory\nFour-link specialization of the weighted-loop proof',fontsize=17,y=.97)
box(ax,(.04,.76,.92,.19),'Original gradient flow  [FMP11]',[r'$T=\mathrm{Tr}(V_1V_2V_3V_4),\quad T_a=-i\sigma_a/2$',r'$P_i=V_1\cdots V_i,\quad \dot\theta=-2\sin\theta,\quad P_i(\theta)=e^{i\theta J/4}Q_i$'],size=14)
box(ax,(.04,.515,.92,.185),'Both critical holonomies constrain a global first integral',[r'$W=I:\ Q\quad\longrightarrow\quad W=-I:\ A_JQ$',r'$A_J=(e^{\pi J/4},e^{\pi J/2},e^{3\pi J/4}),\qquad J^2=-I$'],color='#eef2e7',size=14)
box(ax,(.04,.26,.92,.195),'Endpoint transports generate every original fiber direction',[r'$\mathbf{a}=(1/2,0,-1/2),\quad \mathbf{b}=(1/2,1,1/2)$',r'$\mathbf{a}^2=(1/4,0,1/4),\quad \det[\ \mathbf{a}\ \mathbf{b}\ \mathbf{a}^2\ ]=1/4$',r'$[\mathbf{a}\otimes J_1,\mathbf{a}\otimes J_2]=2\mathbf{a}^2\otimes J_3$'],size=14)
box(ax,(.04,.015,.92,.19),'Actual full-state consequence  [FMP12-FMP13]',[r'$\|\mathcal{K}x\|^2=\|\mathcal{K}y\|^2>0\qquad(j\geq1)$',r'$\langle\mathcal{K}x,e^{-t\mathcal{D}}\mathcal{K}x\rangle>0\quad(t\geq0)$',r'$X_x=a(\mu x-x)/2:\quad\mathrm{quadratic\ factor}=a^2/4$'],color='#f4ebee',size=14)
for top,bottom in [(.76,.7),(.515,.455),(.26,.205)]:ax.add_patch(FancyArrowPatch((.5,top-.01),(.5,bottom+.01),arrowstyle='-|>',mutation_scale=17,lw=1.8,color='#627c8d'))
fig.text(.5,.02,'The endpoint diagram records exact maps, not a projection of the full fiber.\nNonzero memory is proved at every regulator; a uniform shrinking-window bound remains open.',ha='center',fontsize=11)
fig.subplots_adjust(left=.04,right=.96,top=.9,bottom=.085);save(fig,'LOOP_RIGIDITY_AND_FULL_MEMORY')
print('Saved two exact-map figures.')
