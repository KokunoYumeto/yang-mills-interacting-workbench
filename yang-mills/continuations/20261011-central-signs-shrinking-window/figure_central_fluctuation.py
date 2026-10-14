from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,10),facecolor='#f8fafb')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.045,.95,'Exact conditional energy and the complete response residual',fontsize=21,weight='bold',color='#18354a')
ax.text(.05,.89,r'$p_\tau>0,\quad \sum_\tau p_\tau=1,\quad h_\tau=\sqrt{p_\tau},\quad x=\sum_\tau p_\tau Z_\tau$',fontsize=20)
for xpos,col in [(.05,'#e3f0ef'),(.57,'#eee8f6')]:
    ax.add_patch(FancyBboxPatch((xpos,.67),.36,.14,boxstyle='round,pad=.015',fc=col,ec='#587482',lw=1.5))
ax.text(.07,.77,'Original conditional derivative',fontsize=14,weight='bold')
ax.text(.07,.71,r'$t_Z=dx-\sum_\tau p_\tau dZ_\tau$',fontsize=19)
ax.text(.59,.77,'Original physical fluctuation',fontsize=14,weight='bold')
ax.text(.59,.71,r'$y_\tau=h_\tau(Z_\tau-x)$',fontsize=20)
ax.add_patch(FancyArrowPatch((.43,.72),(.55,.72),arrowstyle='<-',mutation_scale=22,lw=2,color='#6c4f9c'))
ax.text(.49,.80,r'$t_Z=2\sum_\tau y_\tau dh_\tau$',fontsize=16,ha='center')
ax.text(.05,.60,r'$q(y,y)=\kappa_*\int A^2\left[\sum_\tau p_\tau|dZ_\tau-v_Z|^2+|t_Z|^2\right]dU$',fontsize=20)
ax.text(.05,.54,r'$v_Z=\sum_\tau p_\tau dZ_\tau,\qquad B^*y=-\kappa_*\delta_A t_Z$',fontsize=19)
ax.text(.05,.45,r'$C_{S,T}=r_{S\triangle T}-r_Sr_T,\qquad (C^{-1})_{S,T}=n^{-2}\sum_\tau\chi_S(\tau)\chi_T(\tau)/p_\tau$',fontsize=18)
ax.text(.05,.37,r'$f_z^0=(L_A+z)^{-1}x,\quad q_T(z)=\langle dr_T,df_z^0\rangle,\quad c=\widehat Z+\kappa_*C^{-1}q(z)$',fontsize=18)
ax.text(.05,.28,r'$\eta_z=y-Bf_z^0,\qquad \|\eta_z\|^2=\int A^2 c^* C c\,dU$',fontsize=23,color='#6c4f9c')
ax.text(.05,.20,r'$|\sqrt{\mathcal{W}_Z(z)}-\sqrt{\mathcal{W}_x^A(z)}|\leq \|\eta_z\|/2$',fontsize=21)
ax.text(.05,.13,'C and c include every nonempty original edge subset. The empty coefficient remains in x.',fontsize=12)
ax.text(.05,.09,'Exact identities; no state samples or assigned continuum rates. Apply at all three original positive shifts.',fontsize=12)
ax.text(.05,.045,'Proof: CFE1–CFE14 and CK9–CK24. Original metric, signs, factors and boundaries retained.',fontsize=12)
for ext in ['png','svg']:fig.savefig(O/('CENTRAL_FLUCTUATION_ENERGY_MAP.'+ext),dpi=170,bbox_inches='tight')
