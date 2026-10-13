from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none'})
fig=plt.figure(figsize=(15,10));fig.suptitle('Both original gauge endpoints constrain the full Hessian row',fontsize=20,y=.97)
ax=fig.add_axes([.045,.47,.44,.40],projection='3d')
a=1/200;v=np.zeros(3);w=np.array([a,0,0])
dirs=np.eye(3)
for center,exclude,color in [(v,np.array([1,0,0]),'#2b6caa'),(w,np.array([-1,0,0]),'#30826c')]:
 for d in list(dirs)+list(-dirs):
  if np.array_equal(d,exclude):continue
  end=center+a*d;ax.plot(*np.array([center,end]).T,color=color,lw=2.3);ax.scatter(*end,color=color,s=17)
ax.plot(*np.array([v,w]).T,color='#c97822',lw=4);ax.scatter(*v,color='#2b6caa',s=48);ax.scatter(*w,color='#30826c',s=48)
ax.text(*v,r'$v_-$',fontsize=14);ax.text(*w,r'$v_+$',fontsize=14);ax.text(a/2,0,.001,r'$e$',color='#9a561a',fontsize=14)
ax.set_xlabel(r'$x_1$');ax.set_ylabel(r'$x_2$');ax.set_zlabel(r'$x_3$')
ax.set_xticks([-.005,0,.005,.01]);ax.set_yticks([-.005,0,.005]);ax.set_zticks([-.005,0,.005])
ax.tick_params(labelsize=9);ax.view_init(elev=23,azim=-58);ax.set_box_aspect((1.5,1,1))
ax.set_title('Two disjoint five-edge stars; each endpoint has degree six',fontsize=12,pad=14)
bx=fig.add_axes([.53,.46,.44,.43]);bx.set(xlim=(0,1),ylim=(0,1));bx.axis('off')
bx.add_patch(FancyBboxPatch((.015,.025),.97,.94,boxstyle='round,pad=.01',facecolor='#e8f1ed',edgecolor='#788d87'))
bx.text(.04,.90,'Exact row defect, GWH2–GWH5',weight='bold',fontsize=14)
bx.text(.04,.79,r'$\chi_e=\frac{1}{\deg(v_-)-1}+\frac{1}{\deg(v_+)-1}=\frac{2}{5}$',fontsize=14)
bx.text(.04,.62,r'$\sum_f\|H_{ef}\|^2=(1+\chi_e)\|H_{ee}\|^2+\frac{\chi_e}{2}G_e+Z_e$',fontsize=13)
bx.text(.04,.50,r'$Z_e\geq0$ retains every other original edge.',fontsize=12)
bx.text(.04,.36,r'$4(a_jT_e)^2+\frac{3}{2}a_j^2T_e\leq\frac{9}{(7/5)\kappa_*^2}(1-w_e/8)$',fontsize=14)
bx.text(.04,.18,r'$a_jT_e\leq\Theta_G(a_j)<\frac{3}{2\kappa_*}\sqrt{\frac{5}{7}}$',fontsize=18)
cx=fig.add_axes([.055,.13,.91,.28]);cx.set(xlim=(0,1),ylim=(0,1));cx.axis('off')
cx.add_patch(FancyBboxPatch((.01,.02),.98,.96,boxstyle='round,pad=.008',facecolor='#e8edf7',edgecolor='#788596'))
cx.text(.03,.86,'Complete covariant graph and physical norm correction, GWH7–GWH11',weight='bold',fontsize=14)
cx.text(.03,.67,r'$(K_U\xi)_f=\xi_{s(f)}-\mathrm{Ad}_{U_f}\xi_{t(f)},\qquad H_UK_U=B_g$',fontsize=16)
cx.text(.03,.46,r'$\sum_f\|H_{ef}\|^2=\|H_{ee}\|^2+\mathrm{Tr}\!\left(Y_e(\mathbb{L}^{(e)}_U)^\dagger Y_e^*\right)+\|A_e\|^2$',fontsize=16)
cx.text(.03,.23,r'$\mathcal{M}([0,\infty])+\mathcal{V}_g\leq M_{\mathbf{1}_Q\tau}$',fontsize=17)
cx.text(.48,.24,'All gauge zero modes remain in the pseudoinverse.',fontsize=12)
fig.text(.055,.073,r'Exact displayed instance: $j=2$, $L_j=16$, $a_j=1/200$, $o=0$; $v_-=(16,16,16)$, $v_+=(17,16,16)$; $x=a_j(z-L_j\mathbf{1})$.',fontsize=12)
fig.text(.055,.032,'The picture shows the two incident stars. The proof and full graph formula retain every edge outside them and every boundary vertex.',fontsize=12,color='#425466')
for ext in ['png','svg']:fig.savefig(O/('GAUGE_HESSIAN_ORIGINAL_STARS.'+ext),dpi=150,bbox_inches='tight')
plt.close(fig);print('Original gauge-star figure written')
