"""Reproducible BP21–BP27 map and exact lower-bound graph."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
fig=plt.figure(figsize=(13.5,7.5),facecolor='#fbfbf7')
ax=fig.add_axes([.045,.24,.47,.60]);ax.axis('off')
def box(y,text,color):
    ax.text(.5,y,text,ha='center',va='center',fontsize=12,linespacing=1.55,
            bbox=dict(boxstyle='round,pad=.65',fc=color,ec='#263f50'),transform=ax.transAxes)
box(.91,r'Original unit phase vector $[e^{i\theta_j C_j}\psi_j]$'+'\n'+r'$C_j=2a_j\sum_p f_p-a_j\sum_p f_pW_p$', '#e6eef2')
ax.annotate('',xy=(.5,.61),xytext=(.5,.77),xycoords='axes fraction',arrowprops=dict(arrowstyle='->',lw=1.7))
ax.text(.53,.70,r'$P=\mathrm{s}\!-\!\lim_{t\downarrow0}[e^{-tA_j}]$',transform=ax.transAxes,fontsize=12)
box(.48,r'Continuous part $P\zeta$ and discarded part $(I-P)\zeta$'+'\n'+r'$\|P\zeta\|^2+\|(I-P)\zeta\|^2=1$', '#e6f0e8')
ax.text(.04,.22,r'Fixed $\theta$: $\|(I-P)\zeta\|^2=0$.',transform=ax.transAxes,fontsize=12)
ax.text(.04,.08,r'$a_j\theta_j^2\to\ell>0$: $\|(I-P)\zeta\|^2\geq e_f^2/Z_f(\ell)>0$.',transform=ax.transAxes,fontsize=12)
bx=fig.add_axes([.61,.31,.35,.46],facecolor='#fbfbf7')
ell=np.logspace(-8,2,500)
LR=168.;dp=(LR+np.sqrt(LR*LR-1296))/2;e=81/dp;H=56/3;Rf=256*LR*dp
lower=e*e/((H+4*e)/ell+Rf)
bx.loglog(ell,lower,color='#175e78',lw=2.5,label='Proved lower bound')
bx.axhline(e*e/Rf,color='#b56632',ls='--',label=r'$e_f^2/\mathcal{R}_f$')
bx.set_xlabel(r'$\ell=\lim a_j\theta_j^2$');bx.set_ylabel('Lost squared norm, lower bound')
bx.grid(which='both',alpha=.2);bx.legend(loc='lower right',fontsize=10)
fig.suptitle('Bounded curvature phases: an explicit loss in the continuous representation',x=.5,y=.97,fontsize=17)
fig.text(.61,.84,r'$Z_f(\ell)=(H_f+4e_f)/\ell+\kappa_*^2\mathcal{R}_f$',fontsize=12)
fig.text(.055,.155,r'Graph: $f(x)=\prod_{d=1}^{3}(1-|x_d|)_+$, support $[-1,1]^3$, $R=2$, $\kappa_*=1$.',fontsize=11)
fig.text(.055,.105,r'$J_1=1$, $J_2=8/27$, $\mathsf{L}_R=168$, $\mathsf{d}_R^+=(168+\sqrt{26928})/2$, $e_f=81/\mathsf{d}_R^+$, $H_f=56/3$, $\mathcal{R}_f=256\cdot168\mathsf{d}_R^+$.',fontsize=11)
fig.text(.055,.045,'BP21–BP27. The graph evaluates a proved bound; it is not vacuum data. Original curvature, state and energy units are retained.',fontsize=10,color='#33444d')
for suffix in ['png','svg']:fig.savefig(ROOT/('BOUNDED_PHASE_SPECTRAL_RECEIVING.'+suffix),dpi=170,facecolor=fig.get_facecolor())
(ROOT/'BOUNDED_PHASE_FIGURE_VALUES.json').write_text(json.dumps({'L_R':LR,'d_R_plus':float(dp),'e_f':float(e),'H_f':H,'R_f':float(Rf),'supercritical_lower_bound':float(e*e/Rf),'samples':[{'ell':float(ell[i]),'lower_bound':float(lower[i])} for i in [0,100,200,300,400,499]],'scope':'Proved bound function, not interacting vacuum samples.'},indent=2)+'\n',encoding='utf-8')
