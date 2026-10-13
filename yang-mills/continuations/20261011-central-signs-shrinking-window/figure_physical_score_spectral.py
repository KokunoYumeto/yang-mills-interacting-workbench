from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(14,10));ax.set(xlim=(0,14),ylim=(0,10));ax.axis('off')
ax.text(.3,9.55,'Actual physical norm, score covariance and the original source',fontsize=19,weight='bold')
ax.text(.3,9.12,'PSC1–PSC10 • exact connecting maps; every original factor and both endpoint atoms retained',fontsize=12,color='#425466')
boxes=[
(.3,6.45,6.35,2.12,'Leading equal-time score covariance',
r'$\mathcal{C}_j(B)=a_j^2J_jA^{\rm sc}_j(s_jB)A_j$'+'\n'+r'$\mathcal{C}_j([0,M])\leq100M\Theta_0(a_j)a_j^2I$'+'\n'+r'$\mathcal{C}_j\ \rightharpoonup\ \mathcal{G}\delta_\infty$','#e8eef8'),
(7.15,6.45,6.55,2.12,'Physical current norm: inverse energy retained',
r'$\mathcal{M}_j(B)=\kappa_*a_jJ_j\int_{s_jB}\lambda^{-1}\,dA^{\rm sc}_j\,A_j$'+'\n'+r'$0\leq\mathcal{M}([0,\infty])\leq M_{\mathbf{1}_{Q}\tau}$'+'\n'+r'$\ker\mathcal{M}([0,\infty])\cap L^2(Q;\mathbb{C}^3)=\{0\}$','#e6f2eb'),
(.3,3.55,13.4,2.15,'Exact measure relation and surviving total source',
r'$d\mathcal{C}_j(r)=100a_j^2r\,d\mathcal{M}_j(r),\qquad r=\lambda/s_j,\quad s_j=100\kappa_*a_j$'+'\n'+r'$\mathcal{Z}([0,\infty])\gamma=-\frac{3}{2}\sum_\ell\gamma_\ell t_\ell$'+'\n'+r'$|\langle h,\mathcal{Z}(B)\gamma\rangle|^2\leq\langle h,\mathcal{M}(B)h\rangle\,\gamma^*\mathcal{E}(B)\gamma$','#fff2db'),
(.3,.78,13.4,2.10,'Actual physical receiver and its remaining spectral allocation',
r'$s_j^2\langle u_{j,\theta}(h),u_{j,\eta}(k)\rangle\ \to\ \langle h,\int\frac{d\mathcal{M}(r)}{(r+\theta)(r+\eta)}k\rangle$'+'\n'+r'$\ker\mathcal{N}_\theta=\ker\mathcal{M}([0,\infty)),\qquad\ker\mathcal{K}_\theta=\ker\mathcal{M}((0,\infty))$'+'\n'+'Zero, finite positive relative energies, and infinity remain in the joint measure.','#eef0f8')]
for x,y,w,h,t,body,color in boxes:
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.08',facecolor=color,edgecolor='#768497'))
 ax.text(x+.15,y+h-.30,t,fontsize=12.5,weight='bold')
 ax.text(x+.15,y+h-.66,body,va='top',fontsize=14 if w>10 else 12,linespacing=1.60)
for a,b in [((3.5,6.31),(3.5,5.88)),((10.5,6.31),(10.5,5.88)),((7,3.42),(7,3.05))]:
 ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=18,lw=1.5,color='#445971'))
ax.text(.35,.23,'Complete proofs: PSC1–PSC10. The total measure is injective; positivity of the original signed window remains to be calculated.',fontsize=11,color='#425466')
for ext in ['png','svg']:fig.savefig(O/('PHYSICAL_SCORE_SPECTRAL_MAP.'+ext),dpi=150,bbox_inches='tight')
plt.close(fig);print('Physical spectral map written')
