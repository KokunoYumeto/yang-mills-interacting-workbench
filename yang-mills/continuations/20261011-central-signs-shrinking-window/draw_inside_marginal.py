"""Reproducible exact map and remainder diagram for IM3-IM25, IM40."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch

root=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(13.4,8.6),dpi=160)
fig.patch.set_facecolor('#f7f8fb'); ax.set_xlim(0,13.4); ax.set_ylim(0,8.6); ax.axis('off')
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',edgecolor=color,facecolor='white',linewidth=1.5))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12,linespacing=1.6,color='#162439')
ax.text(.45,8.12,'The actual inside marginal and its retained energy',fontsize=19,weight='bold',color='#162439')
ax.text(.45,7.65,r'$\psi(x,v)=\sqrt{n(x)}\,\chi(x,v),\quad n(x)=\int\psi(x,v)^2dv,\quad \int\chi(x,v)^2dv=1$',fontsize=14,color='#162439')
box(.55,5.05,4.4,1.8,r'Original ground state $\psi$'+'\n'+r'$S=\Delta_Qw+2|\nabla_Qw|^2$'+'\n'+r'$s(x)=\mathbb{E}_{\mu}[S\mid x]$', '#516c9b')
box(7.0,5.05,5.8,1.8,r'Actual marginal $n=\varphi^2$'+'\n'+r'$-\kappa\Delta_Q\varphi+(bW_Q+R_Q+\kappa T_Q)\varphi=E_Q\varphi$'+'\n'+r'$R_Q\geq0,\quad T_Q=\int|\nabla_Q\chi|^2dv\geq0$', '#206e81')
ax.add_patch(FancyArrowPatch((5.16,5.95),(6.8,5.95),arrowstyle='-|>',mutation_scale=19,linewidth=1.7,color='#34475e'))
ax.text(5.98,6.3,'integrate outside',ha='center',fontsize=10.5,color='#34475e')
box(.55,2.4,12.25,1.65,r'$\mathcal{M}=Y+\mathcal{A}=FW_Q+\alpha F\mathbb{E}_{\mu}[Z_Q\mid x]+(F/b)R_Q=e+\alpha Fs$'+'\n'+r'$\operatorname{Var}(\mathcal{M})+(\alpha F)^2\mathcal{D}_Q=\frac{\alpha F^2}{2}\mu D_Q+4\alpha^{3/2}F^2\mu Z_Q$'+'\n'+r'$D_Q=6M_Q-3W_Q+\frac{3}{2} C_Q-\frac{3}{4} W_{\times}$', '#86506a')
ax.text(.6,1.75,r'$\mathcal{D}_Q=\mu\|H_{\mathrm{mix}}\|^2+2\mu(H_Q+2g_Q/\sqrt{\alpha})(\nabla_Qw,\nabla_Qw)+\mu\operatorname{Var}(S\mid x)\geq0$',fontsize=13,color='#86506a')
ax.text(.6,1.12,r'$\operatorname{Var}(a\mathcal{M})=O(a),\qquad \mu[(\mathcal{M}-e)^2/Y^k]=O(a^{2k-1})$',fontsize=15,color='#162439')
ax.text(.6,.57,'The separate covariance of Y retains Cov(Y, A). No favorable sign or independent law is assigned.',fontsize=11.5,color='#34475e')
ax.text(.6,.19,'Exact operator schematic. Proofs: IM3–IM5, IM15–IM25, IM37–IM40. All outside and crossing terms are retained.',fontsize=10,color='#34475e')
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
for ext in ['png','svg']:fig.savefig(root/f'inside_marginal_receiver.{ext}',facecolor=fig.get_facecolor())
print('inside_marginal_receiver.png and .svg written')
