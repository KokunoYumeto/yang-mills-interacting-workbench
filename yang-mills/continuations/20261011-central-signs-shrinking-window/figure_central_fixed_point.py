from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,10),facecolor='#f8fafb')
ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.045,.95,'The original central configuration retains a nonzero residual',fontsize=21,weight='bold',color='#18354a')
ax.text(.05,.89,r'$U_e=I,\quad T_p=2,\quad \mathrm{Ad}_{i\sigma_\beta}T_\alpha=-T_\alpha\quad(\beta\ne\alpha)$',fontsize=22)
for x,col in [(.05,'#e3f0ef'),(.57,'#eee8f6')]:
    ax.add_patch(FancyBboxPatch((x,.68),.36,.12,boxstyle='round,pad=.015',fc=col,ec='#587482',lw=1.5))
ax.text(.07,.76,'Original gauge isotropy',fontsize=15,weight='bold')
ax.text(.07,.71,r'$dh_\tau(I)=0$',fontsize=22)
ax.text(.59,.76,'Complete residual at I',fontsize=15,weight='bold')
ax.text(.59,.71,r'$\eta_z(I)=y(I)$',fontsize=22)
ax.add_patch(FancyArrowPatch((.43,.73),(.55,.73),arrowstyle='->',mutation_scale=22,lw=2,color='#6c4f9c'))
ax.text(.49,.81,r'$Bf_z^0(I)=0$',fontsize=16,ha='center')
ax.text(.05,.60,r'$F_0=A(I)^2 a_j^2\sum_{p,r}\overline{\varphi(x_p)}\varphi(x_r)C_{\partial p,\partial r}(I)>0$',fontsize=20)
ax.text(.05,.54,'Every original face sample is retained; strict positivity holds when at least one sample is nonzero.',fontsize=12)
ax.text(.05,.45,r'$m_z=\|\eta_z\|^2\ \geq\ \frac{F_0}{2}\left(\frac{\rho_z-\sin\rho_z}{2\pi}\right)^{N_j}$',fontsize=25)
ax.text(.05,.37,r'$\rho_z=\min\{1,F_0/(2\sqrt{N_j}K_z)\},\quad K_z=\max|d(A^2\sum_\tau|\eta_{z,\tau}|^2)|$',fontsize=18)
ax.text(.05,.32,r'$K_z=0:\ \rho_z=1.\qquad d(U,I)\leq\sqrt{N_j}\rho_z$ in the product of original link balls.',fontsize=15)
ax.text(.05,.23,r'$\mathcal{G}_{X_\varphi}(z)-\langle x,(L_A+z)^{-1}x\rangle\ \geq\ \frac{m_z^2}{e_z+zm_z}>0$',fontsize=23,color='#6c4f9c')
ax.text(.05,.15,r'$e_z=q(\eta_z,\eta_z)$ retains the full derivative square in FPR5; FPR6–FPR8 retain its curvature sources.',fontsize=12)
ax.text(.05,.10,'Exact finite-regulator identities and bounds. The product-volume factor and derivative maxima depend on j.',fontsize=12)
ax.text(.05,.05,'Proof: FPR1–FPR8. Radius-two metric, original a, all central probabilities, full potential and vacuum energy retained.',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/('CENTRAL_FIXED_POINT_RESIDUAL_MAP.'+ext),dpi=170,bbox_inches='tight')
