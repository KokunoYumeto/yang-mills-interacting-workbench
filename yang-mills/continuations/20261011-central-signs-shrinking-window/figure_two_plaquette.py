from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch,Circle
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'font.family':'DejaVu Sans','svg.fonttype':'none'})
fig=plt.figure(figsize=(10.5,12.5));grid=fig.add_gridspec(2,2,height_ratios=[1.2,1],hspace=.63,wspace=.35)
axes=[fig.add_subplot(grid[0,0]),fig.add_subplot(grid[0,1]),fig.add_subplot(grid[1,:])]
fig.suptitle('Two adjacent Wilson plaquettes\nThe shared link and its exact receiving coordinates',fontsize=17,y=.975)
ax=axes[0];nodes={'00':(0,0),'10':(1,0),'20':(2,0),'01':(0,1),'11':(1,1),'21':(2,1)}
edges=[('A','00','10'),('B','10','11'),('C','01','11'),('D','00','01'),('E','10','20'),('F','20','21'),('G','11','21')]
for name,src,dst in edges:
    p=np.array(nodes[src]);q=np.array(nodes[dst]);color='#aa3730' if name=='B' else '#245674'
    ax.add_patch(FancyArrowPatch(p,q,arrowstyle='-|>',mutation_scale=17,linewidth=3 if name=='B' else 2,color=color,shrinkA=8,shrinkB=8))
    m=(p+q)/2;offset=np.array([-.13,0]) if p[0]==q[0] else np.array([0,.12])
    ax.text(*(m+offset),name,color=color,ha='center',va='center',weight='bold')
for name,p in nodes.items():
    ax.plot(*p,'o',color='#172936',ms=7);ax.text(p[0],p[1]+(.12 if p[1]==1 else -.15),name,ha='center',fontsize=11)
ax.text(.5,.5,'left face',ha='center');ax.text(1.5,.5,'right face',ha='center')
ax.text(1,-.45,r'$U=BC^{-1}D^{-1}A$',ha='center',fontsize=12)
ax.text(1,-.69,r'$V=EFG^{-1}B^{-1}$',ha='center',fontsize=12)
ax.text(1,-.93,r'$VU=EFG^{-1}C^{-1}D^{-1}A$',ha='center',fontsize=12)
ax.set_title('Original seven-link graph\n[TPL1]',pad=18,fontsize=13);ax.set_xlim(-.35,2.35);ax.set_ylim(-1.1,1.25);ax.set_aspect('equal');ax.axis('off')
ax=axes[1];q=np.linspace(-2,2,501);X,Z=np.meshgrid(q,q);mask=X*X+Z*Z<=4;k=.8
values=np.ma.masked_where(~mask,16*Z/(351*k*k));im=ax.pcolormesh(X,Z,values,cmap='RdBu',shading='auto',vmin=-32/(351*k*k),vmax=32/(351*k*k),rasterized=True)
ax.add_patch(Circle((0,0),2,fill=False,linewidth=1.5,color='#182b3a'));ax.axhline(0,color='#253747',lw=.8)
ax.set_aspect('equal');ax.set_xlim(-2.15,2.15);ax.set_ylim(-2.15,2.15);ax.set_xlabel(r'$x=\mathrm{Tr}\,U$');ax.set_ylabel(r'$z=\mathrm{Tr}(UV)$');ax.set_title('Exact section y=0\n[TPL2, TPL12]',pad=18,fontsize=13)
cb=fig.colorbar(im,ax=ax,orientation='horizontal',pad=.21,fraction=.045);cb.set_label(r'$b^2$ coefficient of $C_{12}$: $16z/(351\kappa_*^2)$',fontsize=11)
ax=axes[2];a=10;b=1/(k*a*a);shift=.7;t=np.linspace(0,2,400);leading=-4*a*a*b*b*np.exp(-3*k*t)*2/(9*k*(8*k+shift))
ax.plot(t,leading,color='#8a2d49',lw=2.8);ax.axhline(0,color='#253747',lw=.8);ax.fill_between(t,leading,0,color='#ead0d7',alpha=.6)
ax.set_xlabel('time t');ax.set_ylabel('complete mixed leading term');ax.set_title('Leading term, with all factors  [TPL14]',pad=18);ax.ticklabel_format(axis='y',style='sci',scilimits=(-2,2));ax.grid(alpha=.2)
ax.text(.97,.2,r'$\kappa_*=0.8,\ a=10,\ b=0.0125$'+'\n'+r'$s=0.7,\ (\varphi_1,\varphi_2)=(1,1)$',transform=ax.transAxes,ha='right',va='top',fontsize=12)
fig.text(.5,.035,'Exact graph and domain section. The curve is the proved leading term;\nthe analytic remainder is retained in TPL14. Full-lattice maps and remaining\nconditional score covariance: TPL15–TPL17. No continuum claim is made.',ha='center',fontsize=12)
fig.subplots_adjust(left=.1,right=.96,top=.88,bottom=.15)
fig.savefig(O/'TWO_PLAQUETTE_GEOMETRY.png',dpi=160,facecolor='white');fig.savefig(O/'TWO_PLAQUETTE_GEOMETRY.svg',facecolor='white');plt.close(fig)
print('Saved reproducible two-plaquette figure.')
