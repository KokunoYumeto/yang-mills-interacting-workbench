"""Plot the exact occurrence bound and the proved fixed-box receiving map."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

ROOT=Path(__file__).resolve().parent
j=np.arange(2,13,dtype=float);m=2*j**4;n=m+1
h=np.pi/(2*n);c=np.cos(h);C=1/np.tan(h)
S1=np.sqrt(2/n)*C*(C-c)
S3=np.sqrt(2/n)*((2-1/n)*C*C-(c/n)*C)
A1=m*np.sqrt(2/n)*C*(5*C-4*c)
A3=m/n*np.sqrt(2/n)*((9*m+5)*C*C-2*c*C)
Cocc=12*(S3*np.sqrt(S1*A1)+S1*np.sqrt(S3*A3))**2
beta=200*np.sqrt(2)*j*np.sin(np.pi/(4*j**4+2))
tau=19/2+3*np.sqrt(10)
limit=125829120000*tau/np.pi**6
loss=4*j*beta**2*Cocc
fig,axs=plt.subplots(1,2,figsize=(14,5.8),gridspec_kw={'width_ratios':[1,1.12]})
fig.suptitle('Original phase observable: exact path bound and fixed-box spectral weight',fontsize=16,y=.97)
ax=axs[0]
ax.plot(j,loss/(limit*j**23),'o-',color='#267581',label='Exact finite formula / leading term')
ax.axhline(1,color='#ad4b45',ls='--',label='Proved limit: 1')
ax.set_xlabel(r'Original path index $j$; $\kappa_*=1$')
ax.set_ylabel(r'$4j\beta_{0,j}^{\,2}\mathcal{C}_{{\rm occ},j}/(Kj^{23})$')
ax.set_title('Magnitude of the negative endpoint bound',fontsize=12)
ax.grid(alpha=.2);ax.legend(loc='lower right',fontsize=9)
ax.text(.5,-.21,r'$K=125829120000(19/2+3\sqrt{10})/\pi^6$'+'\nThis plots a proved bound, not sampled spectral weight.',
        transform=ax.transAxes,ha='center',va='top',fontsize=10)
ax=axs[1];ax.axis('off')
ax.text(.5,.98,r'Fixed $L,a$; then $g\downarrow0$',ha='center',va='top',fontsize=13,weight='bold')
def box(y,txt):
    ax.text(.5,y,txt,ha='center',va='center',fontsize=13,
            bbox={'boxstyle':'round,pad=.55','fc':'#f0f6f7','ec':'#267581'})
box(.78,r'$(p-r)\psi_g$  in the original physical space')
ax.annotate('',xy=(.5,.51),xytext=(.5,.68),arrowprops={'arrowstyle':'->','lw':2,'color':'#267581'})
ax.text(.53,.595,'Exact Haar density and dilation',fontsize=10,va='center')
box(.42,r'$\sigma_*\,z_1\!\cdot z_3\,\Phi_0=2\sqrt{3}\,O_{13}$')
ax.text(.5,.22,r'Raw squared norm $\longrightarrow12$'+'\n'+
        r'Raw excitation energy $\longrightarrow12\delta_*$'+'\n'+
        r'Weight in the first odd level $\longrightarrow12$',
        ha='center',va='center',fontsize=12,linespacing=1.7)
ax.text(.5,-.08,r'$\delta_*=2\sigma_*/a$; no vector is rescaled.'+'\n'+
        'These fixed-box limits do not interchange the limits in '+r'$L,a,g$.',
        ha='center',va='center',fontsize=10)
fig.text(.5,.018,'Proof: IP5–IP9 and IP14–IP22 in PHASE_MOMENTS_AND_ORIGINAL_PATH.md. Original words, raw norms and coupling factors are retained.',
         ha='center',fontsize=9)
fig.subplots_adjust(left=.07,right=.98,top=.84,bottom=.25,wspace=.32)
for ext in ['png','svg']:fig.savefig(ROOT/('PHASE_MOMENTS_AND_ORIGINAL_PATH.'+ext),dpi=180)
