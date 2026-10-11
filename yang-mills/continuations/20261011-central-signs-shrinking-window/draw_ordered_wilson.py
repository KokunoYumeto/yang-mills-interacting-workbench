from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
R=Path(__file__).resolve().parent
t=np.linspace(-.8,.8,401);p=2-2*np.cos(t/2)**3+2*np.sin(t/2)**3;n=2-2*np.cos(t/2)**3-2*np.sin(t/2)**3
q=3*t*t/4;c=t**3/4
fig,axs=plt.subplots(2,2,figsize=(12,8.2),layout='constrained');axs=axs.ravel()
ax=axs[0];ax.plot(t,p,label=r'Order $(te_1,te_2,te_3,0)$');ax.plot(t,n,label=r'Order $(te_1,te_3,te_2,0)$');ax.plot(t,q,':',color='black',label=r'Quadratic term $3t^2/4$');ax.set(title='Original face defect, OW18',xlabel=r'Original coordinate $t$',ylabel=r'$2-\mathrm{Tr}(P)$');ax.legend(fontsize=8)
ax=axs[1];ax.plot(t,p-q,label='First order: exact defect minus quadratic');ax.plot(t,n-q,label='Exchanged order: exact defect minus quadratic');ax.plot(t,c,':',color='#1565c0',label=r'Ordered cubic $+t^3/4$');ax.plot(t,-c,':',color='#ef6c00',label=r'Ordered cubic $-t^3/4$');ax.set(title='The cubic term retains matrix order',xlabel=r'Original coordinate $t$');ax.legend(fontsize=8)
ax=axs[2];bound=81*t**4/192;ax.fill_between(t,-bound,bound,color='#c8d8e8',label=r'Proved bound $|R_4|\leq 81t^4/192$');ax.plot(t,p-q-c,color='#1565c0',label='Full fourth-order remainder');ax.set(title='Complete remainder retained, OW8 and OW14',xlabel=r'Original coordinate $t$');ax.legend(fontsize=8)
ax=axs[3];ax.plot(t,4*np.sin(t/2)**4,label='Exact commutator face defect');ax.plot(t,t**4/4,':',label=r'Quartic term $t^4/4$');ax.set(title=r'Zero linear circulation, $C_p=0$: OW21–OW22',xlabel=r'Original coordinate $t$',ylabel=r'$2-\mathrm{Tr}(P)$');ax.legend(fontsize=8)
for ax in axs:ax.grid(alpha=.2)
fig.suptitle('Ordered SU(2) Wilson action: exact deterministic faces, not vacuum samples',fontsize=14)
fig.savefig(R/'ORDERED_WILSON_ACTION.png',dpi=170);fig.savefig(R/'ORDERED_WILSON_ACTION.svg');plt.close(fig)
