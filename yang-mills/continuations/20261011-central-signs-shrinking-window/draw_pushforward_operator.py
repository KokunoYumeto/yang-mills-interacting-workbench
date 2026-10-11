from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
root=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(14,7.6));ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
def box(x,y,w,hh,txt,color):
 ax.add_patch(FancyBboxPatch((x,y),w,hh,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#334155',linewidth=1.5))
 ax.text(x+w/2,y+hh/2,txt,ha='center',va='center',linespacing=1.7)
def arrow(a,b):ax.add_patch(FancyArrowPatch(a,b,arrowstyle='->',mutation_scale=19,linewidth=1.5,color='#334155'))
box(.025,.62,.36,.25,'Closed scalar form — OP6–OP10\n'+r'$-\kappa(hm\chi^{\prime})^{\prime}+V_Ym\chi=b\Lambda_Qm\chi$'+'\n'+r'$hm\chi^{\prime}=t/\chi=0$ at both endpoints','#e0f2fe')
box(.59,.62,.36,.25,'Original physical vectors — OP11\n'+r'$\mathcal{J}(\phi\chi)=\phi(Y)\psi$'+'\nIsometry; exact equality of shifted forms','#dcfce7')
arrow((.40,.745),(.57,.745));ax.text(.485,.805,r'$\mathcal{J}$',ha='center',fontsize=17)
box(.025,.22,.36,.25,'Conditional action — OP12–OP13\n'+r'$L_Y\phi=h\phi^{\prime\prime}+(J+2\eta)\phi^{\prime}$'+'\n'+r'$\mathbb{E}[R_\phi\mid Y]=0$','#fef3c7')
box(.59,.22,.36,.25,'Full action, including coupling — OP13\n'+r'$(H-E_0)(\phi(Y)\psi)$'+'\n'+r'$=-\kappa\psi[(L_Y\phi)(Y)+R_\phi]$','#ffedd5')
arrow((.205,.60),(.205,.49));arrow((.77,.60),(.77,.49));arrow((.57,.35),(.405,.35))
ax.text(.5,.135,r'$E_{2,rs}=\kappa^2\int\overline{L_Y\phi_r}\,L_Y\phi_s\,p\,dy+\kappa^2\int d_r^*\Sigma d_s\,p\,dy$',ha='center',fontsize=16)
ax.text(.5,.058,'Complete second-energy matrix — OP14–OP17. The positive residual matrix retains both conditional fluctuations and their correlation.',ha='center',fontsize=11)
ax.set_title('Exact scalar-to-physical map and its spectral residual',fontsize=20,pad=16)
fig.text(.5,.015,'Proof: PUSHFORWARD_OPERATOR_RECEIVING.md, OP1–OP19. Original couplings, probability Haar and physical time are retained.',ha='center',fontsize=10)
fig.savefig(root/'pushforward_operator_maps.png',dpi=170,bbox_inches='tight');fig.savefig(root/'pushforward_operator_maps.svg',bbox_inches='tight');plt.close(fig)
