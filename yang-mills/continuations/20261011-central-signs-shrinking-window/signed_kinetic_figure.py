from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parent
data=json.loads((ROOT/'SIGNED_KINETIC_CHECKS.json').read_text())
fig,axs=plt.subplots(1,3,figsize=(15.5,4.8),layout='constrained')
c=data['enumerated'];n=np.array([r['n'] for r in c]);dm=np.array([r['D_n'] for r in c])
axs[0].plot(n,[r['trace_positive'] for r in c],'o-',label=r'Exact $\operatorname{Tr}B_+$')
axs[0].plot(n,dm,'s--',label=r'$\mathcal{D}_n=(3m-1)/2$')
axs[0].plot(n,dm+np.array([r['R_n'] for r in c]),'^:',label=r'Proved $\mathcal{D}_n+R_n$')
axs[0].set(xlabel=r'Odd $n$; $m=n-1$',ylabel='Deterministic matrix trace',title='All original ancestor rows: SK18–SK20')
axs[0].legend(fontsize=9)
axs[1].plot(n,[r['trace_negative'] for r in c],'o-',label=r'Exact $\operatorname{Tr}B_-$')
axs[1].plot(n,[r['R_n'] for r in c],'^--',label=r'Proved $R_n=p_n+T_n/2$')
axs[1].plot(n,[r['refined_trace_negative_bound'] for r in c],'s:',label='Exact row-nuclear upper function')
axs[1].set(xlabel=r'Odd $n$',ylabel='Negative spectral mass',title='Negative term retained: SK12, SK20')
axs[1].legend(fontsize=9)
p=data['original_path_kappa_star_1'];j=np.array([r['j'] for r in p]);k=np.array([r['kinetic_ratio_j5'] for r in p])
axs[2].plot(j,k,'o-',markersize=3,label=r'$400j(\mathcal{D}_{n_j}+R_{n_j})/j^5$')
axs[2].axhline(1200,color='black',ls='--',label='Proved limit 1200')
axs[2].set(xlabel=r'Original path $j$; $n_j=2j^4+1$',ylabel=r'Kinetic upper function divided by $j^5$',title='Actual-state bound function: SK28')
axs[2].legend(fontsize=9)
for ax in axs:ax.grid(alpha=.25)
fig.suptitle('Signed kinetic matrix of the original soft cochain',fontsize=16)
fig.text(.5,-.06,'Left and centre: exact finite matrix spectra for n=3,5,7. Right: proved upper function, not computed vacuum energy.\nFull constants, signs, physical norm map and raw-window test: SIGNED_KINETIC_TRACE.md, SK1–SK39.',ha='center',fontsize=11)
fig.savefig(ROOT/'SIGNED_KINETIC_TRACE.png',dpi=180,bbox_inches='tight')
fig.savefig(ROOT/'SIGNED_KINETIC_TRACE.svg',bbox_inches='tight')
