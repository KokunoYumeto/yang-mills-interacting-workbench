from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(13,8),facecolor='#f6f8fa')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.055,.945,'The residual is an original local-energy fluctuation',fontsize=21,weight='bold',color='#17334c')
ax.text(.055,.89,r'$r_\varphi=D_\varphi-V_\varphi,\qquad V_\varphi=\frac{\kappa_*^2 a_j^3}{2}\,\upsilon_c$',fontsize=22)
ax.text(.055,.825,r'$D_\varphi=X_\varphi-\bar X_c,\qquad \|D_\varphi\|\leq \frac{a_j\zeta_{\varphi,j}}{2}\sqrt{\Lambda_Q d_Q+4\kappa_*^2a_j^2}=o(1)$',fontsize=18)
ax.text(.055,.755,'Actual cell averages and original coefficients; SLE1–SLE8.',color='#4a5c69')
ax.text(.055,.68,'One actual source measure, three different moments',fontsize=20,weight='bold',color='#17334c')
ax.text(.055,.618,r'$\Sigma_z(B)_{ef}=\langle z_e,E_0(B)z_f\rangle,\qquad z_e=\alpha_e^{\rm WH}\cdot dw$',fontsize=19)
boxes=[(.055,r'$\mathsf{N}=4\kappa^2b^2\int\lambda^{-2}\,d\Sigma_z$','Ordinary covariance','All spatial pairs retained'),
       (.365,r'$\mathsf{E}=4\kappa^2b^2\int\lambda^{-1}\,d\Sigma_z$','First energy moment','Zero beyond coface distance 2'),
       (.675,r'$\mathsf{Z}=4\kappa^2b^2\int d\Sigma_z$','Second energy moment','All spatial pairs retained')]
for x,formula,title,detail in boxes:
    ax.add_patch(FancyBboxPatch((x,.37),.27,.17,boxstyle='round,pad=0.012',facecolor='#ffffff' if x!=.365 else '#def0e9',edgecolor='#8298a8',lw=1.3))
    ax.text(x+.135,.50,title,ha='center',fontsize=14,weight='bold')
    ax.text(x+.135,.451,formula,ha='center',fontsize=13)
    ax.text(x+.135,.40,detail,ha='center',fontsize=11)
ax.text(.055,.285,r'$\mathsf{E}_{ef}=\frac{1}{2}\langle\psi,[A_e,[H,A_f]]\psi\rangle$',fontsize=21)
ax.text(.055,.22,'Disjoint operator supports give exact zeros; individual spectral cross terms need not vanish.',fontsize=12.5)
ax.text(.055,.145,r'$\nu_{V_\varphi}(B)=\frac{\kappa_*^2a_j^6}{4}\,c^*\Omega_{\rm en}(B)c$',fontsize=19)
ax.text(.055,.075,'Identity map, not a covariance sample. SLE15–SLE22. All boundary incidence is retained.',fontsize=11,color='#4a5c69')
for ext in ['png','svg']:fig.savefig(O/('SCALAR_ENERGY_MAP.'+ext),dpi=170,bbox_inches='tight')
