from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'svg.fonttype':'none'})
fig=plt.figure(figsize=(16,12),facecolor='#f7fafc')
fig.text(.06,.955,'Original curvature increments as spatial distributions',fontsize=23,weight='bold',color='#153f59')
fig.text(.06,.913,r'$\mathscr{Y}^{de}_j(t)=a_j\sum_{p:de}[D_p(U_j(t))-D_p(U_j(0))]\delta_{x_{p,j}}$'+'   ·   DH1–DH4',fontsize=20)
ax=fig.add_axes([.05,.46,.9,.4]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
boxes=[(.01,.55,.28,.36,'Original atomic history',r'$a_j,\ x_{p,j},\ D_p=2-W_p$'+'\nAll coefficients and positions retained\nActual stationary Yang–Mills law'),(.36,.55,.28,.36,'Exact local coordinates',r'$y_k(t)=\langle\mathscr{Y}_j(t),e_{k,n}\rangle$'+'\n'+r'$e_{k,n}=n^{-3/2}\prod_d\sin\frac{\pi k_d(x_d+n)}{2n}$'+'\nDH8: exact orthonormal sine basis'),(.71,.55,.28,.36,'Weighted Hilbert paths',r'$\|y\|_{-s,n}^2=\sum_k(1+\lambda_{k,n})^{-s}|y_k|^2$'+'\n'+r'$s>3/2,\quad\lambda_{k,n}=\pi^2|k|^2/(4n^2)$'+'\nDH11–DH15: moments and tightness'),(.25,.05,.5,.29,'Interior distribution map and compatible cubes',r'$I_{n,s}:\mathcal{H}_n^{-s}\to\mathcal{D}\prime(O_n)$'+'\n'+r'$\mathcal{N}_{n,s}=\ker I_{n,s}$'+'  ·  boundary-invisible part retained\nDH9a, DH16: quotient, overlap maps and global distribution')]
for x,y,w,h,title,body in boxes:
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.007',facecolor='white',edgecolor='#5693ae',linewidth=1.5))
    ax.text(x+w/2,y+h-.055,title,ha='center',va='top',fontsize=13,weight='bold',color='#153f59')
    ax.text(x+w/2,y+h-.13,body,ha='center',va='top',fontsize=11,linespacing=1.8)
for start,end in [((.295,.72),(.351,.72)),((.645,.72),(.701,.72)),((.85,.535),(.68,.35))]:
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=18,color='#153f59',linewidth=1.8))
left=fig.add_axes([.08,.13,.39,.25]);right=fig.add_axes([.59,.13,.34,.25])
M=np.arange(1,201,dtype=float)
for s,color in [(2.,'#18848a'),(2.5,'#b35544')]:
    bound=(4/np.pi**2)**s*3*M**(3-2*s)/(2*s-3)
    left.loglog(M,bound,color=color,lw=2,label=fr'$s={s:g}$')
left.set_title('Proved series-tail envelope · DH10',loc='left',weight='bold',fontsize=14)
left.set_xlabel(r'cutoff $\max k_d\leq M$');left.set_ylabel('upper bound for omitted weights')
left.legend(title=r'$n=1$');left.grid(alpha=.2)
right.axis('off')
right.text(0,1,'Continuous distribution histories',weight='bold',fontsize=14,color='#153f59',va='top')
right.text(0,.80,r'$\mathbb{E}\|Y(t)-Y(u)\|_{-s,n}^{2p}$'+'\n'+r'$\leq K_{p,n}n^{-3p}S_{s,n}^p|t-u|^p$'+'\n\n'+r'Every time Hölder exponent $\gamma<1/2$'+'\n\nSpatial distribution regularity;\nno smooth-function or nonzero claim.',fontsize=14,va='top',linespacing=1.5)
fig.text(.06,.045,'The plot is the exact proved weight-tail bound for the indicated cube and exponents; it is not sampled Yang–Mills data.',fontsize=11,color='#4c6775')
fig.text(.06,.023,'Full proof: DH1–DH19, including DH9a. Human source comparison: Grothaus et al., math/0211323, Section 6.1.',fontsize=11,color='#4c6775')
fig.savefig(root/'DISTRIBUTION_CURVATURE_HISTORIES.png',dpi=150)
fig.savefig(root/'DISTRIBUTION_CURVATURE_HISTORIES.svg')
plt.close(fig)
