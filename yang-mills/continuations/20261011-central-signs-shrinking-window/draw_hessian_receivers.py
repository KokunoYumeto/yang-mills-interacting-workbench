from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':13,'svg.fonttype':'none'})
fig,axs=plt.subplots(1,2,figsize=(15,9),facecolor='#f7fafc')
fig.subplots_adjust(left=.08,right=.96,bottom=.46,top=.77,wspace=.25)
fig.text(.08,.935,'Sharper actual-moment receiving bounds',fontsize=24,weight='bold',color='#173f56')
fig.text(.08,.88,r'$G=\int d\nu,\quad E=\int\lambda\,d\nu,\quad E_2=\int\lambda^2\,d\nu$'+'   ·   original raw spectral measure',fontsize=19)
x=np.linspace(0,6,601);rr=4.
axs[0].plot(x,4*x/rr*(1-x/rr),lw=2,color='#16848a',label=r'$4\lambda/R-4\lambda^2/R^2$')
axs[0].plot([0,0,4,4,6],[0,1,1,0,0],lw=2,color='#3b6280',label=r'$\mathbf{1}_{(0,R]}(\lambda)$')
axs[0].axhline(0,color='gray',lw=.7);axs[0].set_ylim(-3.1,1.25);axs[0].set_xlim(0,6)
axs[0].set_title('Exact spectral minorant · HVR26–HVR28',loc='left',fontsize=14,weight='bold')
axs[0].set_xlabel(r'original energy $\lambda$; illustrated $R=4$');axs[0].legend(loc='lower left',fontsize=11);axs[0].grid(alpha=.2)
tt=np.linspace(0,2,401)
axs[1].plot(tt,1-np.exp(-2*tt),lw=2,color='#16848a',label=r'Jensen: $1-e^{-2t}$')
axs[1].plot(tt,2*tt-2*tt**2,lw=2,color='#b25345',label=r'Taylor: $2t-2t^2$')
axs[1].set_ylim(-1.1,1.15);axs[1].set_xlabel(r'original time $t$');axs[1].grid(alpha=.2);axs[1].legend(loc='lower left',fontsize=11)
axs[1].set_title('All positive times · HVR29–HVR30',loc='left',fontsize=14,weight='bold')
fig.text(.08,.33,r'$\nu((0,2E_2/E])\geq E^2/E_2,$'+'    '+r'$G-C(t)\geq(E^2/E_2)(1-e^{-tE_2/E})$',fontsize=19,color='#173f56')
fig.text(.08,.265,r'$\liminf_j G_{f,j}/a_j\geq(e_f^*)^2/(63\kappa_*^2\int f^2+4e_f^*),$'+'   HVR25',fontsize=18)
fig.text(.08,.20,r'$a_j\,\mu_j\|\nabla^2C_{f,j}\|^2\longrightarrow63\int f^2$'+'   ·   HVR31–HVR33',fontsize=19)
fig.text(.08,.14,'HVR34 keeps the full actual ground-state Hessian contraction in the second energy moment.',fontsize=14)
fig.text(.08,.08,'The plots illustrate the exact inequalities at R=4 and the moment extremizer ν=δ₂ (E=2, E₂=4).',fontsize=11,color='#496472')
fig.text(.08,.05,'They are algebraic examples, not Yang–Mills vacuum data. All actual finite-volume factors and limits remain in HVR1–HVR34.',fontsize=11,color='#496472')
fig.savefig(R/'HESSIAN_RECEIVING_MAPS.png',dpi=150);fig.savefig(R/'HESSIAN_RECEIVING_MAPS.svg');plt.close(fig)
