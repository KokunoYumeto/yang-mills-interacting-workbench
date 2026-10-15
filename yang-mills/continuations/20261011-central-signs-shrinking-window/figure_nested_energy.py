from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import numpy as np
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'mathtext.fontset':'dejavusans'})
blue='#234c63';light='#eef6fb';orange='#b95e19'
fig=plt.figure(figsize=(13,12));ax=fig.add_axes([0,0,1,1]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.5,.97,'Nested original cubes and the complete inverse-energy tail',ha='center',va='top',fontsize=21,color=blue)
ax.text(.5,.932,'NSE7–NSE13 • original conditional measures • every outside link retained',ha='center',fontsize=12)
for x0,w,label in [(.08,.84,r'$Q_L$'),(.15,.70,r'$Q_s$'),(.23,.54,r'$Q_r$')]:
    y0=.65+(x0-.08)*.34;h=.23-2*(x0-.08)*.34
    ax.add_patch(Rectangle((x0,y0),w,h,fill=False,lw=1.5,ec=blue));ax.text(x0+.012,y0+h-.025,label,color=blue,fontsize=15)
ax.text(.5,.765,r'Original source support $\subset Q_{50j}$',ha='center',fontsize=15)
ax.text(.5,.625,'Schematic of the actual inclusions, not to scale. The terminal cube is the full original box.',ha='center',fontsize=11)
ax.text(.5,.587,r'$I_{rs}:L^2(\rho_r\,dx_r)\longrightarrow L^2(\rho_s\,dx_s),\qquad I_{rs}t(x_r,z)=t(x_r)$',ha='center',fontsize=15)
ax.text(.5,.552,r'$I_{rs}^{*}f=\rho_r^{-1}\int\rho_s f\,dz,\qquad J_sI_{rs}=J_r,\qquad \mathcal{B}_r=I_{rs}^{*}\mathcal{B}_sI_{rs}$',ha='center',fontsize=15)
ax.add_patch(Rectangle((.06,.344),.88,.187,facecolor=light,edgecolor=blue))
ax.text(.5,.505,r'$\mathscr{A}_\zeta=q_\zeta(\mathcal{L}),\quad u_r=J_r\mathcal{B}_r^{-1}F_r,\quad h_r=\mathscr{A}_\zeta^{-1}Z-u_r$',ha='center',fontsize=16)
ax.text(.5,.443,r'$v_r=u_{r+1}-u_r,\qquad h_r=\sum_{s=r}^{L-1}v_s,\qquad h_L=0$',ha='center',fontsize=17)
ax.text(.5,.376,r'$\delta_r=\|\mathscr{A}_\zeta^{1/2}h_r\|^2=\sum_{s=r}^{L-1}\|\mathscr{A}_\zeta^{1/2}v_s\|^2$',ha='center',fontsize=17)
ax.text(.5,.307,r'$\langle v_s,\mathscr{A}_\zeta v_t\rangle=0\quad(s\ne t)$',ha='center',fontsize=17,color=blue)
ax.text(.5,.274,'This exact energy orthogonality retains the full original cubic polynomial.',ha='center',fontsize=11)
ax.text(.5,.228,r'$C-T_r=2\,\operatorname{Re}\sum_s\langle Z,k_\zeta(\mathcal{L})\mathscr{A}_\zeta v_s\rangle$',ha='center',fontsize=16)
ax.text(.5,.180,r'$-\sum_{s,t}\langle\mathscr{A}_\zeta v_s,k_\zeta(\mathcal{L})\mathscr{A}_\zeta v_t\rangle$',ha='center',fontsize=16)
ax.text(.5,.130,'Both sums run over every remaining increment. The filtered mixed terms stay.',ha='center',fontsize=12,color=orange)
ax.text(.5,.078,r'$C\geq T_r-\frac{86}{25}\zeta\sqrt{m_1\delta_r}-\zeta^3\delta_r$',ha='center',fontsize=19,color=blue)
ax.text(.5,.030,'The lower bound does not assert a positive signed response or a no-gap result.',ha='center',fontsize=12)
for ext in ['png','svg']:fig.savefig(O/('NESTED_CUBES_AND_SIGNED_TAIL.'+ext),dpi=160)
plt.close(fig)

data=json.loads((O/'NESTED_ENERGY_CHECKS.json').read_text())['original_path_bounds']
xs=np.array([float(v['j']) for v in data]);cs=np.array([float(v['cross']) for v in data]);qs=np.array([float(v['quadratic']) for v in data])
fig,axs=plt.subplots(2,1,figsize=(12,10),sharex=True);fig.subplots_adjust(top=.83,bottom=.23,hspace=.27)
fig.suptitle('Complete bounds for a selected actual annular correction',fontsize=19,color=blue,y=.97)
fig.text(.5,.92,r'$a=(100j)^{-1},\ L=j^4,\ r_0=50j,\ \zeta=\kappa_*/j,\ \kappa_*=4/5$',ha='center',fontsize=15)
fig.text(.5,.876,'All original source faces in the side-one cube, with coefficients one. K = j⁴ − 50j.',ha='center',fontsize=12)
for ax,ys,col in [(axs[0],cs,blue),(axs[1],qs,orange)]:
    ax.loglog(xs,ys,'o-',color=col,lw=2,ms=5);ax.grid(alpha=.25,which='both')
axs[0].set_ylabel('Upper bound on absolute coupling')
axs[0].set_title(r'$|\langle Z,k_\zeta(\mathcal{L})\mathscr{A}_\zeta v_{r_*}\rangle| \leq \frac{43}{25}\sqrt{\overline{m}_1 Z_Q^2/(\zeta K)}$',fontsize=14,pad=13)
axs[1].set_ylabel('One-sided quadratic upper bound')
axs[1].set_title(r'$\langle\mathscr{A}_\zeta v_{r_*},k_\zeta(\mathcal{L})\mathscr{A}_\zeta v_{r_*}\rangle \leq Z_Q^2/K$',fontsize=14,pad=13)
axs[1].set_xlabel('Original integer regulator j')
fig.text(.5,.135,r'Every point uses the entire finite formula. Proved upper rates: $j^{-1/2}$ and $j^{-2}$ (NSE10–NSE11).',ha='center',fontsize=11)
fig.text(.5,.085,'The lower graph bounds a signed quantity from above; it is not an absolute-value bound.',ha='center',fontsize=11)
fig.text(.5,.045,'The selected index is defined by the actual state. These curves are bounds, not Wilson-state measurements.',ha='center',fontsize=11,color=blue)
for ext in ['png','svg']:fig.savefig(O/('ORIGINAL_ANNULAR_SOURCE_BOUNDS.'+ext),dpi=160)
plt.close(fig)
print('Two figures rendered.')
