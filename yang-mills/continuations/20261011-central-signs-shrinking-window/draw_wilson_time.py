from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
W=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(15,8),facecolor='#f7fafc');ax.set(xlim=(0,15),ylim=(0,8));ax.axis('off')
ax.text(.35,7.7,'Actual Wilson histories: exact drift cancellation and temporal regularity',fontsize=21,weight='bold',color='#19354f')
def box(x,y,w,h,title,lines,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',facecolor=color,edgecolor='#6b8298'))
 ax.text(x+.2,y+h-.4,title,fontsize=12,weight='bold',color='#19354f')
 ax.text(x+.2,y+h-.9,lines,fontsize=11,va='top',linespacing=1.3,color='#19354f')
box(.4,4.1,6.6,2.7,'1   Actual process, forward and backward',r'$\mathcal{L}_j=\kappa_*\Delta+2\kappa_*\nabla\log\psi_j\cdot\nabla$'+'\n'+r'$\Delta b=M_t+\int_0^t\mathcal{L}_jb\,dr$'+'\n'+r'$-\Delta b=N_t+\int_0^t\mathcal{L}_jb\,dr$'+'\n'+r'$\Delta b=(M_t-N_t)/2$  ·  TR2–TR7','#e4eef8')
box(7.6,4.1,6.7,2.7,'2   Full moment estimate',r'$d\langle M\rangle,\ d\langle N\rangle\leq 2\kappa_*D^2dt$'+'\n'+r'$\mathbb{E}|\Delta b|^{2p}\leq(2p-1)!!(2\kappa_*D^2|t-u|)^p$'+'\n'+r'Face trace: $D^2\leq4$; fourth coefficient $192\kappa_*^2$'+'\n'+'No independence or uniform drift bound · TR8–TR10','#e0f2eb')
box(.4,1.0,6.6,2.5,'3   Continuous-path limit',r'$d=p-1-2p\alpha>0$'+'\n'+r'$\mathbb{P}(H_{\alpha,T}>R)\leq CT^p/[R^{2p}(1-2^{-d})]$'+'\n'+r'Every local exponent $\alpha<1/2$'+'\n'+'One actual subsequence; countable fixed Wilson family\nFull proof: TR12–TR14','#fff1d7')
box(7.6,1.0,6.7,2.5,'4   Uniform orientation-average collapse',r'$\mathbb{E}\sup_{0\leq t\leq T}|2-\overline{W}_{de,j}(t)|^2$'+'\n'+r'$\qquad\leq8\epsilon_j+320\kappa_*T/(m_j^2n_j)\longrightarrow0$'+'\n'+r'$\epsilon_j=\min\{2,(3\kappa_*/100j)\sqrt{n_j/m_j}\}$'+'\n'+'Every original face and boundary count retained · TR15–TR17','#e4eef8')
ax.text(.45,.45,'Proof: WILSON_TIME_REGULARITY.md · TR1–TR17. Schematic of exact maps; no simulated vacuum paths.',fontsize=11,color='#496379')
ax.text(.45,.12,'Temporal Hölder continuity does not establish global smoothness of a four-dimensional field or the no-gap endpoint.',fontsize=11,color='#496379')
fig.savefig(W/'WILSON_TIME_REGULARITY.png',dpi=180,bbox_inches='tight');fig.savefig(W/'WILSON_TIME_REGULARITY.svg',bbox_inches='tight');plt.close(fig)
