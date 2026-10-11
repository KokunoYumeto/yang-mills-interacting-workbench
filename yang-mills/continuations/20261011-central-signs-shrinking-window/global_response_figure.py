from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
ROOT=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,2,figsize=(14,6.8))
def box(ax,x,y,w,h,text,color='#e5f0f1'):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.014',facecolor=color,edgecolor='#47727a',lw=1.2))
 ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12)
for ax in axs:ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax=axs[0];ax.set_title('Every finite real source: the exact inverse',fontsize=14,pad=20)
box(ax,.03,.78,.94,.15,r'$H(x)\psi_x=E(x)\psi_x,\quad\rho_x=\psi_x^2,\quad\int\rho_x=1$')
box(ax,.03,.51,.94,.16,r'$L_x=K^{-1}Q_H[K-2\Gamma(v_x,\cdot)]$'+'\n'+r'$L_x:H^s_{\rm ph,0}\longrightarrow H^s_{\rm ph,0}$')
ax.annotate('',xy=(.5,.68),xytext=(.5,.77),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#47727a'})
ax.text(.5,.40,r'$L_x^{-1}f=Q_H\kappa\psi_x^{-1}(H-E)^{\dagger}\psi_x$'+'\n'+r'$\times\,[Kf-\mu_x(Kf)]$',ha='center',va='center',fontsize=13)
box(ax,.03,.08,.94,.17,r'$3R^{\rm phys}=\mathcal{O}_{\rho_x}L_x^{-1}P$'+'\n'+r'$D_xm=2R^{\rm phys}>0$',color='#f5ece4')
ax.text(.5,-.025,r'$m:\mathbb{R}^{M}\longrightarrow\operatorname{int}\mathcal{C}_L$ is an analytic diffeomorphism.',ha='center',fontsize=11)
ax=axs[1];ax.set_title('Averaging every two-link coordinate cube',fontsize=14,pad=20)
box(ax,.03,.78,.94,.15,r'$D_r:\ t\in[-r,r]^3\longmapsto U(t)$'+'\n'+r'$dU=(4/\pi^2)(1+|t|^2)^{-3}\,d^3t$')
box(ax,.03,.51,.94,.16,r'$\int I_r(U_e^0,U_f^0;c)\,dU_e^0dU_f^0$'+'\n'+r'$=v_r^2\int p_{ef}|F_a-c|^2\,dU_edU_f$')
ax.annotate('',xy=(.5,.68),xytext=(.5,.77),arrowprops={'arrowstyle':'->','lw':1.8,'color':'#47727a'})
ax.text(.5,.40,r'$\sum_{\alpha,\beta}|b_{t_\alpha t^{\prime}_\beta}|^2$'+'\n'+r'$=|a_p|^2[128+16(w_p^0)^2]\geq128|a_p|^2$',ha='center',va='center',fontsize=13)
box(ax,.03,.08,.94,.17,r'$\operatorname{Var}(F_a\mid y)\geq$'+'\n'+r'$\frac{2}{8^6}\,\frac{r^4e^{-16\sqrt{3}r(s_e+s_f)}}{(1+3r^2)^{10}}\,|a_p|^2$',color='#f5ece4')
ax.text(.5,-.025,'The exact Haar cube volume cancels; all exterior links remain.',ha='center',fontsize=11)
fig.suptitle('Global finite-source response with the original scalar, means and metric',fontsize=17,y=.97)
fig.text(.5,.055,'Proof: GPR1–GPR26 and GPR35–GPR52. The dagger removes only the actual vacuum. C_L is the convex hull of the full original Wilson image.',ha='center',fontsize=10)
fig.text(.5,.02,'Original joint path: the proved inverse susceptibility bound is O(j⁴⁰). This is a finite-source map and bound; continuum reconstruction remains unfinished.',ha='center',fontsize=10)
fig.subplots_adjust(left=.04,right=.97,bottom=.18,top=.83,wspace=.12)
for ext in ['png','svg']:
 p=ROOT/('GLOBAL_PHYSICAL_RESPONSE.'+ext);fig.savefig(p,dpi=180)
 if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
