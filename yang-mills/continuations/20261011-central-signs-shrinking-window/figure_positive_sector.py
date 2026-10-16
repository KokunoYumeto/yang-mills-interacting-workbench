from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11})
fig=plt.figure(figsize=(15,10),facecolor='white')
ax=fig.add_axes([.035,.05,.93,.87]);ax.set_xlim(0,1);ax.set_ylim(0,1);ax.axis('off')
fig.suptitle('Original sector energies, complete cubic moment and weighted receiver',fontsize=17,y=.97)
def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#607181',linewidth=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',linespacing=1.7)
def arrow(x,y,a,b):
    ax.add_patch(FancyArrowPatch((x,y),(a,b),arrowstyle='->',mutation_scale=18,linewidth=1.4,color='#253849'))
box(.025,.81,.25,.13,r'$t=\mathcal{B}_{\zeta}^{-1}F$'+'\n'+r'$J:L^2(\rho\,dx)\to L^2(\mu)$'+'\nOriginal raw source coefficients','#edf4fb')
box(.365,.81,.25,.13,r'$\Phi=\psi Jt$'+'\n'+r'$\mathcal{M}_{\psi}:L^2(\mu)\to L^2(dU)$'+'\nUnitary; inverse multiplication by '+r'$\psi^{-1}$','#edf4fb')
box(.715,.81,.25,.13,r'$D=A+B=K+s$'+'\n'+r'$K=H-E_0,\quad s=\varepsilon-V_\times$'+'\nEvery potential scalar and energy retained','#f8f1e6')
arrow(.29,.875,.345,.875);arrow(.63,.875,.695,.875)
ax.text(.5,.75,'PSE5–PSE7: full operator domains are transported with the inverse map',ha='center',fontsize=11,color='#30495e')
box(.045,.525,.91,.155,
    r'$\|D^{3/2}\Phi\|^2=\|A^{3/2}\Phi\|^2+\|B^{3/2}\Phi\|^2$'+'\n'
    r'$+\,3\|AB^{1/2}\Phi\|^2+3\|A^{1/2}B\Phi\|^2$'+'\n'
    'PSE11–PSE12: all four positive components, plus the original vector in the graph map',
    '#edf5eb')
arrow(.84,.795,.84,.695)
box(.045,.285,.43,.17,
    r'$x_0=D^{1/2}K\Phi,\quad x_1=D^{1/2}(s\Phi)$'+'\n'
    r'$\|D^{3/2}\Phi\|^2=\|x_0\|^2$'+'\n'
    r'$+\,2\operatorname{Re}\langle x_0,x_1\rangle+\|x_1\|^2$'+'\n'
    'PSE8–PSE10 retain the potential remainders\nand both source cross matrices',
    '#f8f1e6')
box(.53,.285,.425,.17,
    r'$\|B^{m/2}\Phi\|^2=\int\rho\,\beta_m|t|^2\,dx$'+'\n'
    r'$m=1,2,3;\quad\int\rho\,\beta_m|t|^2\,dx\leq E_m^2\|F\|^2$'+'\n'
    'PSE14: actual conditional energy weights\nwith the inverse trial inside each integral',
    '#edf4fb')
arrow(.26,.51,.26,.47);arrow(.74,.51,.74,.47)
box(.045,.055,.91,.155,
    r'$B^{m/2}(\psi X_Jt)=X_J(B^{m/2}\Phi)$'+'\n'
    r'$-\sum_{\varnothing\ne I\subseteq\{1,\ldots,n\}}'
    r'(B^{m/2}X_{J|I}\psi)\,X_{J|I^c}t$'+'\n'
    'PSE15–PSE16: original field order, every product term and every squared cross pairing',
    '#f3eef8')
arrow(.74,.27,.74,.225)
ax.text(.5,.005,'Exact operator and norm diagram. No physical Hilbert-space factorization or continuum no-gap conclusion is asserted.',
        ha='center',fontsize=10,color='#46545f')
fig.savefig(O/'POSITIVE_SECTOR_ENERGY.png',dpi=160)
fig.savefig(O/'POSITIVE_SECTOR_ENERGY.svg')
plt.close(fig)
