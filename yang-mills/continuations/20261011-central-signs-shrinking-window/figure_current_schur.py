from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(14,10));ax.set(xlim=(0,14),ylim=(0,10));ax.axis('off')
ax.text(.35,9.55,'Full current span, full complement, original physical response',fontsize=20,weight='bold')
ax.text(.35,9.05,'Exact maps of the actual finite regulator • CSR1–CSR21',fontsize=13,color='#425466')
boxes=[
(.35,6.85,5.5,1.7,'Original currents and energy',r'$C,\quad N=C^*C,\quad Q=C^*LC$'+'\n'+r'$\Pi=CN^{-1}C^*,\quad R=(I-\Pi)LC$', '#e6f0ff'),
(7.8,6.85,5.8,1.7,'Entire complementary space',r'$A_\perp=(I-\Pi)L|_{\mathcal{H}_\perp}$'+'\n'+r'$D_\perp(z)=A_\perp+z,\quad v_\perp=(I-\Pi)v$','#e8f5ee'),
(2.0,4.6,10,1.65,'Exact matrix and corrected source',r'$S(z)=Q+zN-R^*D_\perp(z)^{-1}R$'+'\n'+r'$d(z)=C^*v-R^*D_\perp(z)^{-1}v_\perp,\quad c_z=S(z)^{-1}d(z)$','#fff3de'),
(.35,2.2,6.35,1.8,'Both components of the physical solution',r'$\beta_z=Cc_z+y_z$'+'\n'+r'$y_z=D_\perp(z)^{-1}(v_\perp-Rc_z)$'+'\n'+r'$\mathcal{W}_X(z)=z\kappa_*(c_z^*Nc_z+\|y_z\|^2)$','#e6f0ff'),
(7.35,1.85,6.25,2.15,'Actual coupling measure and its bound',r'$M(B)=R^*E_{A_\perp}(B)R$'+'\n'+r'$\int_{(0,\infty)}\lambda^{-1}\,dM\leq Q$'+'\n'+r'$M([0,\theta s_j])\leq1500\theta a_j^3 I$','#e8f5ee')]
for x,y,w,h,title,body,col in boxes:
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.10',facecolor=col,edgecolor='#697d93',lw=1.2))
 ax.text(x+.18,y+h-.30,title,weight='bold',fontsize=13)
 ax.text(x+.18,y+h-.68,body,va='top',fontsize=14,linespacing=1.45)
for a,b in [((3,6.75),(4.3,6.35)),((10.7,6.75),(9.7,6.35)),((4.3,4.5),(3.7,4.1)),((9.6,4.5),(10.1,4.1))]:
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,color='#44556a',lw=1.6))
ax.text(.4,1.35,r'$s_j=100\kappa_*a_j,\qquad z\in\{\theta s_j,\ \varepsilon\theta s_j,\ R_{\rm win}\theta s_j\}$',fontsize=17)
ax.text(.4,.70,'The exact-form projection is retained separately (CSR20). Every complementary norm enters the signed window (CSR8).',fontsize=12)
ax.text(.4,.27,'This diagram describes proved maps; it does not assign a positive limiting physical window.',fontsize=12,color='#425466')
for e in ['png','svg']:fig.savefig(O/('CURRENT_SCHUR_FULL_MAP.'+e),dpi=150,bbox_inches='tight')
plt.close(fig)
data=json.loads((O/'CURRENT_SCHUR_CHECKS.json').read_text())['model']
fig,axs=plt.subplots(1,2,figsize=(14,6.8))
colors=['#147d92','#bb6819','#793cac']
for theta,col in zip([.2,1,3],colors):
 rows=[x for x in data if x['theta']==theta]
 js=[x['j'] for x in rows]
 axs[0].plot(js,[x['schur'] for x in rows],marker='o',color=col,label=r'$\theta='+str(theta)+'$')
 axs[0].axhline(rows[0]['limit'],color=col,ls='--',alpha=.6)
 axs[1].plot(js,[x['norm_receiver'] for x in rows],marker='o',color=col,label=r'$\theta='+str(theta)+'$')
 axs[1].axhline(rows[0]['norm_limit'],color=col,ls='--',alpha=.6)
for ax in axs:ax.set_xscale('log');ax.set_xlabel('Original regulator index j');ax.grid(alpha=.2);ax.legend()
axs[0].set_ylabel(r'$S(\theta s_j)/a_j^2$');axs[1].set_ylabel(r'$a_j^{-3}|b_j|^2\|T_{\theta s_j}\|^2/a_j^4$')
axs[0].set_title('Full effective energy');axs[1].set_title('Full complementary lift norm')
fig.suptitle('Specified block diagnostic with zero, finite and escaping relative energies',fontsize=18,y=.98)
fig.text(.06,.10,r'$\kappa_*=1.7,\ \tau=1.2,\ K_0/a_j^2=0.4,\ \omega=(0.3,0.5,0.7),\ \lambda/s_j=(a_j,1.6,a_j^{-1})$',fontsize=13)
fig.text(.06,.052,'Dashed lines: exact limits in CSR15 and CSR19. Original cell-volume factor is shown in the right axis.',fontsize=12)
fig.text(.06,.014,'These are fully specified matrix checks, not sampled Yang–Mills vacuum data. Complete formulas accompany the figure.',fontsize=12,color='#425466')
fig.tight_layout(rect=(0,.15,1,.92))
for e in ['png','svg']:fig.savefig(O/('CURRENT_SCHUR_ORIGINAL_SCALE.'+e),dpi=150,bbox_inches='tight')
plt.close(fig)
print('2 reproducible figures written')
