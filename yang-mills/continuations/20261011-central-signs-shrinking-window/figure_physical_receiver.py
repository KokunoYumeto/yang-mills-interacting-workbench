from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(14,10));ax.set(xlim=(0,14),ylim=(0,10));ax.axis('off')
ax.text(.3,9.55,'Original Hessian defect and complete physical covariance',fontsize=21,weight='bold')
ax.text(.3,9.04,'PFR1–PFR19 • original state, radius-two edge metric and all exterior rows',fontsize=13,color='#425466')
items=[
(.3,6.65,13.4,1.83,'Exact nonnegative defect, before taking any limit',
r'$\frac{9b_{\rm pot}}{8\kappa_*}(2m_e-w_e)-\frac{3}{2}T_e-4T_e^2$'+'\n'+r'$=3\sum_{f\ne e}\mu\|H_{ef}\|^2+3\mu\|H_{ee}^{\rm tf}\|^2+\mathrm{Var}_\mu(\Delta_e w)\ \geq 0$','#e5f2ed'),
(.3,4.0,6.15,2.15,'Actual kinetic and face bounds',
r'$a_jT_e\leq\Theta_0(a_j)<\frac{3}{2\kappa_*}$'+'\n'+r'$\mu D_p\geq\ell_\dagger(a_j),\quad\frac{\ell_\dagger(a_j)}{a_j}\to\frac{3\kappa_*}{8}$','#e6f0ff'),
(7.0,4.0,6.7,2.15,'Original matrix and energy receivers',
r'$0\leq Q_j<\frac{9a_j^2}{\kappa_*}I$'+'\n'+r'$\liminf E_{X,j}\geq\frac{3}{2}\kappa_*^2J_t$'+'\n'+r'$\liminf\mathcal{R}_{X,j}(\theta s_j)/a_j\geq\kappa_*^2J_t/4$','#fff1d9'),
(.3,1.53,13.4,2.02,'Full physical scalar receiver: both mixed covariances retained',
r'$\widehat{T}_z=-\kappa_*a_j^2\,d\,L_0^{-1}(L_0+z)^{-1}B_{\rm sc}N^{-1}S(z)$'+'\n'+r'$B_{\rm sc}=6b_{\rm pot}Y+2G_0,\qquad (G_0)_e=|d_ew|^2-T_e$'+'\n'+r'$B_{\rm sc}^*KB_{\rm sc}=36b_{\rm pot}^2Y^*KY+12b_{\rm pot}Y^*KG_0+12b_{\rm pot}G_0^*KY+4G_0^*KG_0$','#eef0f8')]
for x,y,w,h,title,body,col in items:
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.10',facecolor=col,edgecolor='#758399'))
 ax.text(x+.18,y+h-.31,title,fontsize=13,weight='bold')
 ax.text(x+.18,y+h-.65,body,fontsize=15 if w>10 else 14,va='top',linespacing=1.42)
for a,b in [((3.5,6.53),(3.5,6.30)),((10.5,6.53),(10.5,6.30)),((3.5,3.87),(4.0,3.65)),((10.5,3.87),(10.,3.65))]:
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,lw=1.6,color='#415269'))
ax.text(.35,.83,r'$a_j=(100j)^{-1},\quad b_{\rm pot}=(\kappa_*a_j^2)^{-1},\quad s_j=100\kappa_*a_j$',fontsize=17)
ax.text(.35,.28,'All displayed bounds concern the actual regulator state. Surviving physical window mass remains to be established.',fontsize=12,color='#425466')
for e in ['png','svg']:fig.savefig(O/('PHYSICAL_RECEIVER_DEFECT_MAP.'+e),dpi=150,bbox_inches='tight')
plt.close(fig)
v=json.loads((O/'PHYSICAL_RECEIVER_CHECKS.json').read_text())['plots'];v=[x for x in v if x['kappa']==1]
fig,axs=plt.subplots(1,2,figsize=(14,6.6))
x=[r['j'] for r in v]
axs[0].plot(x,[r['old_ceiling'] for r in v],color='#8b919b',ls='--',label='Previous uniform ceiling')
axs[0].plot(x,[r['theta'] for r in v],color='#176d8e',marker='o',label=r'$\Theta_0(a_j)$, PFR10')
axs[0].set_ylim(1.3,3.2);axs[0].set_ylabel(r'Upper bound for $a_jT_e$')
axs[1].plot(x,[r['old_floor'] for r in v],color='#8b919b',ls='--',label=r'Previous $\ell(a_j)/a_j$')
axs[1].plot(x,[r['new_floor'] for r in v],color='#39784d',marker='o',label=r'$\ell_\dagger(a_j)/a_j$, PFR12')
axs[1].set_ylim(.15,.41);axs[1].set_ylabel(r'Lower bound for $\mu D_p/a_j$')
for ax in axs:ax.set_xscale('log');ax.set_xlabel('Original regulator index j');ax.grid(alpha=.2);ax.legend(loc='center right')
axs[0].set_title('Kinetic ceiling halved');axs[1].set_title('Individual plaquette floor doubled')
fig.suptitle('Proved bounds on the unchanged original path',fontsize=20,y=.98)
fig.text(.065,.09,r'Illustrative coupling $\kappa_*=1$; $a_j=(100j)^{-1}$. Full finite roots and original counts are in PFR9–PFR14.',fontsize=13)
fig.text(.065,.035,'Curves show proved bounds, not vacuum measurements. Complete second face moments and all mixed covariances remain in the proof.',fontsize=12,color='#425466')
fig.tight_layout(rect=(0,.14,1,.92))
for e in ['png','svg']:fig.savefig(O/('KINETIC_CEILING_AND_FACE_FLOOR.'+e),dpi=150,bbox_inches='tight')
plt.close(fig);print('2 physical receiver figures written')
