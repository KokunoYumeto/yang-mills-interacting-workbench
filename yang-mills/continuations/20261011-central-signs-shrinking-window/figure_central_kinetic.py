from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,9),facecolor='#f8fafb')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.045,.94,'The full original spectral response retains both components',fontsize=21,weight='bold',color='#18354a')
ax.text(.045,.87,r'$\mathcal{T}(Z\psi)=h\overline{Z}+y,\qquad y_\tau=h_\tau(Z_\tau-\overline{Z}),\qquad \overline{Z}=\sum_\tau p_\tau Z_\tau$',fontsize=20)
for x,col in [(.05,'#e3f0ef'),(.60,'#eee8f6')]:
    ax.add_patch(FancyBboxPatch((x,.60),.34,.17,boxstyle='round,pad=.015',fc=col,ec='#587482',lw=1.5))
ax.text(.075,.72,'Central-average component',fontsize=15,weight='bold')
ax.text(.075,.65,r'$P\mathcal{M}(hf)=hL_Af$',fontsize=22)
ax.text(.625,.72,'Conditional fluctuation',fontsize=15,weight='bold')
ax.text(.625,.65,r'$Q\mathcal{M}(hf)=Bf$',fontsize=22)
ax.add_patch(FancyArrowPatch((.405,.69),(.58,.69),arrowstyle='<->',mutation_scale=23,lw=2.3,color='#6c4f9c'))
ax.text(.49,.74,r'$B,\ B^*$',ha='center',fontsize=17)
ax.text(.07,.51,r'$Bf=-2\kappa_*(\langle dh_\tau,df\rangle)_\tau$',fontsize=22,color='#6c4f9c')
ax.text(.07,.42,r'$s_z=L_A+z-B^*(D+z)^{-1}B$',fontsize=22)
ax.text(.07,.33,r'$\ell_z=\overline{Z}-B^*(D+z)^{-1}y$',fontsize=22)
ax.text(.07,.24,r'$\mathcal{W}_{Z,j}(z)=z\,\mathcal{G}_{Z}(z)-z^2\|(\mathcal{M}+z)^{-1}\mathcal{T}(Z\psi)\|^2$',fontsize=21)
ax.text(.05,.15,'The reduced operator and source are interpreted in their full form domains; their z-dependence is retained.',fontsize=12)
ax.text(.05,.10,'Exact orthogonal maps and identities, not sampled dynamics. The arrows are the proved coupling B and its adjoint.',fontsize=12)
ax.text(.05,.05,'Proof: CK9–CK24. Every original shift, coefficient, vacuum energy and boundary is retained. Source: figure_central_kinetic.py.',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/('CENTRAL_KINETIC_RESOLVENT_MAP.'+ext),dpi=170,bbox_inches='tight')
