from pathlib import Path
import itertools,numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,8),facecolor='#f8fafb')
ax=fig.add_axes([.02,.17,.46,.70],projection='3d');ax.set_proj_type('ortho')
coord=lambda v:.01*(np.array(v,float)-1)
vertices=list(itertools.product(range(3),repeat=3))
for v in vertices:
    for d in range(3):
        if v[d]==2:continue
        w=list(v);w[d]+=1;points=np.array([coord(v),coord(w)])
        ax.plot(*points.T,color='#a9b7c0',lw=.8,alpha=.6)
for base,d,k in [((0,0,0),0,1),((0,1,0),0,2)]:
    z=np.array(base);ed=np.eye(3,dtype=int)[d];ek=np.eye(3,dtype=int)[k]
    points=np.array([coord(z),coord(z+ed),coord(z+ed+ek),coord(z+ek)])
    ax.add_collection3d(Poly3DCollection([points],facecolor='#efb757',edgecolor='#b57918',alpha=.35))
    center=coord(z+(ed+ek)/2);ax.text(*center,'−',fontsize=23,color='#855500')
cycle=[(0,0,0),(0,1,0),(0,1,1),(1,1,1),(1,1,0),(1,0,0),(0,0,0)]
for v,w in zip(cycle,cycle[1:]):
    a=coord(v);b=coord(w);delta=b-a
    ax.quiver(*a,*delta,color='#6c4f9c',linewidth=2.3,arrow_length_ratio=.2)
for v,label in [((0,0,0),'root'),((0,1,1),'s(e)'),((1,1,1),'t(e)')]:
    a=coord(v);ax.scatter(*a,color='#18354a',s=28);ax.text(*(a+np.array([0,0,.0025])),label,fontsize=11)
ax.view_init(24,-53);ax.set(xlabel='x',ylabel='y',zlabel='z')
for axis in [ax.xaxis,ax.yaxis,ax.zaxis]:axis.set_ticks([-.01,0,.01])
fig.text(.04,.94,'The complete central Hessian has an exact face-boundary map',fontsize=20,weight='bold',color='#18354a')
fig.text(.51,.82,r'$\mathscr{H}^f_{e\alpha,k\beta}=K^f_{e,k}\delta_{\alpha\beta},\qquad K^fD=0$',fontsize=20)
fig.text(.51,.71,r'$RF=I+TD^{\mathsf{T}}$',fontsize=23)
fig.text(.51,.60,r'$K^f=R\,S^fR^{\mathsf{T}},\qquad S^f=FK^fF^{\mathsf{T}}$',fontsize=20)
fig.text(.51,.49,r'$G=R^{\mathsf{T}}R$',fontsize=23)
fig.text(.51,.38,r'$\langle\mathrm{Hess}\,f,\mathrm{Hess}\,g\rangle$',fontsize=20)
fig.text(.54,.31,r'$=3\,\mathrm{Tr}((S^f)^{\mathsf{T}}G\,S^gG)$',fontsize=20,color='#6c4f9c')
fig.text(.04,.12,'Exact j=1 example: L=1, a=0.01, o=(0,0,0); all 54 original positive links are shown.',fontsize=12)
fig.text(.04,.08,'Purple boundary: t_s + e − t_t. Orange filling: −(0;1,2) −((0,1,0);1,3), in one-based axis labels.',fontsize=12)
fig.text(.04,.04,'x=o+a(v−L1). Hessians evaluated at the original central configuration I. CHM1–CHM6 retain the full face Gram and boundaries.',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/('CENTRAL_HESSIAN_FACE_MAP.'+ext),dpi=170,bbox_inches='tight')
plt.close(fig)
fig=plt.figure(figsize=(14,9),facecolor='#f8fafb');ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.04,.94,'The actual conditional kinetic curvature retains a positive matrix variance',fontsize=20,weight='bold',color='#18354a')
ax.text(.05,.86,r'$K_\tau=K^{\log(\psi\circ D_\tau)},\qquad \overline{K}=\sum_\tau p_\tau K_\tau,\qquad \mathscr{D}_\tau=K_\tau-\overline{K}$',fontsize=20)
for x,col in [(.06,'#e3f0ef'),(.58,'#eee8f6')]:ax.add_patch(FancyBboxPatch((x,.62),.34,.14,boxstyle='round,pad=.015',fc=col,ec='#587482',lw=1.5))
ax.text(.08,.71,'All original conditional components',fontsize=13,weight='bold')
ax.text(.08,.65,r'$K^{r_S}=2\sum_\tau\chi_Sp_\tau\mathscr{D}_\tau$',fontsize=19)
ax.text(.60,.71,'Full conditional kinetic term',fontsize=13,weight='bold')
ax.text(.60,.65,r'$K^{\mathcal{F}}=2\mathfrak{V}$',fontsize=22)
ax.add_patch(FancyArrowPatch((.42,.68),(.56,.68),arrowstyle='->',mutation_scale=22,lw=2,color='#6c4f9c'))
ax.text(.05,.52,r'$\mathfrak{V}=\sum_\tau p_\tau\mathscr{D}_\tau^2=\frac{1}{4}\sum_{S,T\ne\varnothing}(\mathcal{C}^{-1})_{S,T}K^{r_S}K^{r_T}\ \geq0$',fontsize=22)
ax.text(.05,.40,r'$\Delta\mathcal{F}(I)=6\,\mathrm{Tr}\,\mathfrak{V}$',fontsize=24,color='#6c4f9c')
ax.text(.05,.29,r'$\Delta\mathcal{F}(I)\geq \frac{8b_j^2}{3\kappa_*^2d_j}\sum_{p,r}\mathcal{C}_{\partial p,\partial r}(I)>0$',fontsize=24)
ax.text(.05,.19,r'$d_j=N_j-V_j+1,\quad b_j=(\kappa_*a_j^2)^{-1},\quad\mathcal{F}=\sum_\tau|dh_\tau|^2$',fontsize=18)
ax.text(.05,.11,'All matrices and probabilities are evaluated at the original central configuration. Matrix products retain their order.',fontsize=12)
ax.text(.05,.06,'Proof: CHM7–CHM13. The full covariance and its regulator dependence remain; no positive limiting spectral weight is assigned.',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/('ACTUAL_CENTRAL_HESSIAN_VARIANCE.'+ext),dpi=170,bbox_inches='tight')
