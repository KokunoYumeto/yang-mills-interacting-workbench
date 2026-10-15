from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent;checks=json.loads((O/'JOINT_TRACE_CHECKS.json').read_text());rows=checks['evaluated_original_thresholds']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
def save(fig,name):
    fig.savefig(O/(name+'.png'),dpi=160,bbox_inches='tight');fig.savefig(O/(name+'.svg'),bbox_inches='tight');plt.close(fig)
fig=plt.figure(figsize=(11,13));fig.suptitle('Actual trace compression: moments, signs and the original path\nFull-state identities and evaluated sufficient thresholds [JTR1–JTR10]',y=.98,fontsize=16)
ax=fig.add_axes([0,0,1,1]);ax.axis('off')
def box(y,h,title,lines):
    ax.add_patch(FancyBboxPatch((.07,y),.86,h,boxstyle='round,pad=.008',ec='#829dac',fc='#edf3f7'))
    ax.text(.095,y+h-.02,title,va='top',weight='bold',color='#285269',fontsize=12)
    for yy,line in zip(np.linspace(y+h-.065,y+.025,len(lines)),lines):ax.text(.5,yy,line,va='center',ha='center',fontsize=13)
box(.77,.14,'Original observable and exact second-moment defect [JTR1]',[r'$X_\xi=J F_\xi,\quad F_\xi=a\xi(\mu x-x)/2,\quad \mathcal{L}J=J\mathcal{A}+\mathcal{K}$',r'$m_1=\widetilde m_1,\quad m_2-\widetilde m_2=r=\|\mathcal{K}F_\xi\|^2\geq a^2|\xi|^2m_C/4>0$'])
box(.51,.21,'All three signs hold beyond their stated finite thresholds [JTR5–JTR7]',[r'$\zeta^2\Delta\mathcal{W}(\zeta)\longrightarrow-2r<0$',r'$\zeta^2\Delta\mathcal{C}(\zeta)\longrightarrow 2D_2r>0$',r'$\zeta\mathcal{C}(\zeta)\longrightarrow-D_1m_1<0$',r'$\varepsilon=1/4,\ R_{\rm win}=4:\quad D_1=43/25,\quad D_2=232/25$'])
ax.annotate('',(.5,.735),(.5,.755),arrowprops=dict(arrowstyle='->',color='#58788b',lw=1.7))
ax.text(.5,.475,'Limits keep the original regulator fixed. The full trace baseline remains in the total response.',ha='center',fontsize=10)
plot=fig.add_axes([.14,.23,.76,.18]);plot.loglog([r['j'] for r in rows],[float(r['log10_Zcorr_over_s']) for r in rows],'o-',color='#a85b3f')
plot.set_xticks([1,2,3,10,100],[1,2,3,10,100]);plot.set_xlabel('original regulator index j');plot.set_ylabel(r'$\log_{10}(Z_{\rm corr}/s_j)$');plot.grid(which='both',alpha=.25)
fig.text(.5,.14,r'$Z_{\rm corr}/[j^{897}e^{84800\pi^2j/\kappa_*}]\ \longrightarrow\ '+r'3[4A_J^2+16B_3(960000)^2]/(D_2\kappa_*A_{\kappa_*})$',ha='center',fontsize=12)
fig.text(.5,.07,'κ* = 4/5; a = 1/(100j), L = j⁴, b = 1/(κ*a²), sⱼ = κ*/j; raw ξ = 7/3 retained.\nThe plot evaluates the complete bound formulas at 180 digits, not the actual state spectrum.\nThe sufficient threshold grows while the intended shift shrinks; its full coefficient is proved in JTR10.',ha='center',fontsize=10)
save(fig,'ACTUAL_TRACE_MOMENTS_AND_SIGNS')

fig=plt.figure(figsize=(11,14));fig.suptitle('The original signed spectral filter and its full-state map\nAll three shifts, all five moments and both tails retained [JTR11–JTR13]',y=.98,fontsize=16)
ax=fig.add_axes([.13,.65,.78,.23]);lam=np.geomspace(.015,70,1500);z=1.;c=16/25
kernel=z*lam/(lam+z)**2-c*(z/4)*lam/(lam+z/4)**2-c*(4*z)*lam/(lam+4*z)**2
Y=(25+18*np.sqrt(689))/172;low=(Y-np.sqrt(Y*Y-4))/2;high=(Y+np.sqrt(Y*Y-4))/2
ax.axvspan(low,high,color='#b8d5bf',alpha=.6,label='positive interval');ax.plot(lam,kernel,color='#285269',lw=2);ax.axhline(0,color='#777',lw=1)
ax.axvline(low,color='#719577',ls='--');ax.axvline(high,color='#719577',ls='--');ax.set_xscale('log');ax.set_xlabel('original spectral energy λ (ζ fixed at 1)');ax.set_ylabel('complete signed kernel');ax.grid(alpha=.2);ax.legend(loc='lower right',fontsize=10)
fig.text(.5,.595,r'$\lambda_\pm=\zeta[Y_*\pm\sqrt{Y_*^2-4}]/2,\quad Y_*=(25+18\sqrt{689})/172,\quad\lambda_-\lambda_+=\zeta^2$',ha='center',fontsize=13)
fig.text(.5,.56,'This is the exact scalar filter, not a spectral-density plot. Both negative tails remain in its integral.',ha='center',fontsize=10)
fig.text(.5,.495,r'$f=R_0R_-R_+X_\xi,\quad\widetilde f=S_0S_-S_+F_\xi$',ha='center',fontsize=14)
fig.text(.5,.455,r'$\mathcal{C}=\zeta\sum_{k=0}^{4}p_k\|\mathcal{L}^{(k+1)/2}f\|^2$',ha='center',fontsize=15)
fig.text(.5,.405,r'$(p_0,p_1,p_2,p_3,p_4)=(-43\zeta^4/25,\ \zeta^3/2,\ 3801\zeta^2/400,\ \zeta/2,\ -43/25)$',ha='center',fontsize=13)
fig.text(.5,.345,'Exact difference from the trace vector, with no commutation of the coupling:',ha='center',fontsize=11,weight='bold')
fig.text(.5,.30,r'$f-J\widetilde f=-R_0R_-R_+\mathcal{K}S_+F_\xi$',ha='center',fontsize=15)
fig.text(.5,.255,r'$\qquad-R_0R_-\mathcal{K}S_-S_+F_\xi-R_0\mathcal{K}S_0S_-S_+F_\xi$',ha='center',fontsize=15)
fig.text(.5,.185,r'$R_\beta=(\mathcal{L}+\zeta_\beta)^{-1},\quad S_\beta=(\mathcal{A}+\zeta_\beta)^{-1}$',ha='center',fontsize=13)
fig.text(.5,.145,r'$\zeta_0=\zeta,\quad\zeta_-=\zeta/4,\quad\zeta_+=4\zeta,\qquad X_\xi=JF_\xi$',ha='center',fontsize=13)
fig.text(.5,.075,'The identities also hold at the original ζ = θκ*/j. Actual weights in the positive interval\nand both negative tails remain to be evaluated; total coupling alone does not allocate them.\nComplete original domains, general ε and R coefficients, and proofs: JTR11–JTR13.',ha='center',fontsize=10)
save(fig,'JOINT_FILTER_AND_FULL_STATE_MAP')
