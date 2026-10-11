from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
root=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(figsize=(13,7.8));ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
def box(x,y,w,h,txt,col):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',facecolor=col,edgecolor='#334155',linewidth=1.5));ax.text(x+w/2,y+h/2,txt,ha='center',va='center',linespacing=1.8)
box(.025,.60,.43,.29,'Exact operator domain — OR6\n'+r'$v\in\mathcal{V}_Y,\quad F_v=a_0v^{\prime}\in W^{1,1}(I)$'+'\n'+r'$F_v(0)=F_v(\ell)=0$'+'\n'+r'$m^{-1}[-\kappa F_v^{\prime}+V_Ymv]\in L^2(m\,dy)$','#e0f2fe')
box(.55,.60,.425,.29,'Actual smooth tests — OR9\n'+r'$\chi\phi\in\operatorname{Dom}T_Y$'+'\n'+r'$T_Y(\chi\phi)=\chi[b\Lambda_Q\phi-\kappa L_Y\phi]$'+'\nFlux: '+r'$(t\phi+s\phi^{\prime})/\chi$','#dcfce7')
ax.add_patch(FancyArrowPatch((.47,.745),(.536,.745),arrowstyle='->',mutation_scale=20,lw=1.5))
box(.025,.12,.95,.35,'Exact phase residual — OR13–OR15\n'+r'$\phi_\theta(y)=e^{i\theta y},\quad\mu|R_{\phi_\theta}|^2=\theta^4\int\Sigma_{11}p+4\theta^2\int\Sigma_{22}p$'+'\nThe mixed conditional covariance cancels on the diagonal.\n'+r'$\|(H-E_0)(e^{i\theta Y}\psi)\|^2=\kappa^2\theta^2\mu[(J(Y)+2A)^2]+\kappa^2\theta^4\mu\gamma^2$','#fef3c7')
ax.set_title('The full scalar domain and its exact original phase residual',fontsize=19,pad=15)
fig.text(.5,.025,'Proof: INDEPENDENT_OPERATOR_REVIEW.md, OR6–OR15. All original boundary fluxes, means, physical factors and conditional covariances are retained.',ha='center',fontsize=10)
fig.savefig(root/'operator_domain_maps.png',dpi=180,bbox_inches='tight');fig.savefig(root/'operator_domain_maps.svg',bbox_inches='tight');plt.close(fig)
