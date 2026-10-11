from pathlib import Path
import json,math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

root=Path(__file__).resolve().parent
data=json.loads((root/'WILSON_COVARIANCE_CHECKS.json').read_text())
rows=data['original_path_kappa_star_1'];j=np.array([r['j'] for r in rows])
Q=np.array([r['Q_lower'] for r in rows]);sigma=np.array([r['sigma_squared'] for r in rows])
I=data['integral']['I'];blue='#205b9b';red='#b74438';green='#247d57'
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig=plt.figure(figsize=(17.8,9.2))
gs=fig.add_gridspec(2,3,height_ratios=[1.6,1],left=.07,right=.985,bottom=.11,top=.84,hspace=.53,wspace=.34)
axes=[fig.add_subplot(gs[0,k]) for k in range(3)]
axes[0].semilogy(j,Q,'o-',color=blue,label=r'Actual-vacuum lower function $Q_{n_j}(\xi_j)$')
axes[0].semilogy(j,sigma,'s--',color=green,label=r'Original ordinary curl $\sigma_{*,j}^2$')
axes[0].set(title='A proved signed Wilson bound',xlabel=r'Original path index $j$',ylabel='Exact finite bound functions')
axes[0].legend(fontsize=9,loc='lower left');axes[0].grid(alpha=.2,which='both')
axes[1].plot(j[1:],j[1:]*Q[1:],'o-',color=blue,label=r'$jQ_{n_j}(\xi_j)$, $j\geq2$')
axes[1].axhline(I/200,color=red,linestyle=':',label=r'Proved limit $\mathcal{I}/200$')
axes[1].set(title='The full coefficient is evaluated',xlabel=r'Original path index $j$',ylabel=r'$jQ_{n_j}(\xi_j)$',ylim=(.0051,.00555))
axes[1].legend(fontsize=9,loc='lower right');axes[1].grid(alpha=.2)
axes[2].plot(j,[r['C_upper'] for r in rows],'o-',color=blue,label=r'Actual character upper function $U_{n_j}$')
axes[2].plot(j,[2*r['B_n'] for r in rows],'s--',color='#666666',label=r'Previous coefficient $2B_{n_j}$')
axes[2].axhline(data['C_upper_limit'],color=blue,linestyle=':')
axes[2].set(title='The upper receiving coefficient improves',xlabel=r'Original path index $j$',ylabel=r'Upper functions for $\mathcal{C}_{V,j}$',ylim=(1.7,4.9))
axes[2].legend(fontsize=9,loc='lower right');axes[2].grid(alpha=.2)
bottom=fig.add_subplot(gs[1,:]);bottom.set_axis_off()
boxes=[
(.02,'Original Wilson words',r'$G_1^{-1}G_2=BC,\quad G_1^{-1}G_3=BCD$'+'\n'+r'$G_2^{-1}G_3=D$'+'\nAll repeated-edge terms: WC7–WC18'),
(.35,'Actual conditional Haar fibre',r'$B(t)=Be^{tZ},\quad D(t)=C^{-1}e^{-tZ}CD$'+'\n'+r'$BCD$ fixed; squared speed $2|z|^2$'+'\nExact metric and score: WC25–WC30'),
(.68,'Original covariance receives the bound',r'$\mathcal{C}_V-\sigma_*^2\geq Q_n-\sigma_*^2$'+'\n'+r'$\mathcal{K}\succeq (Q_n/2)[C_{rs}]$'+'\nActual-state inequalities: WC33–WC45')]
for xpos,title,body in boxes:
    bottom.add_patch(FancyBboxPatch((xpos,.15),.30,.77,boxstyle='round,pad=.01',transform=bottom.transAxes,facecolor='#f2f6fa',edgecolor='#91a9bf',linewidth=1.2))
    bottom.text(xpos+.15,.76,title,transform=bottom.transAxes,ha='center',va='center',fontsize=11,weight='bold')
    bottom.text(xpos+.15,.45,body,transform=bottom.transAxes,ha='center',va='center',fontsize=10.5,linespacing=1.8)
for xpos in [.33,.66]:
    bottom.annotate('',xy=(xpos+.012,.535),xytext=(xpos-.012,.535),xycoords='axes fraction',arrowprops={'arrowstyle':'->','lw':1.8,'color':blue})
fig.suptitle('Actual-vacuum root transport eventually exceeds the ordinary soft curl',fontsize=17,y=.965)
fig.text(.5,.906,r'Original path: $\kappa_*=1$, $n_j=2j^4+1$. Curves are proved bound functions, not sampled vacuum moments.',ha='center',fontsize=12)
fig.text(.5,.045,r'$\mathcal{I}\approx1.0966548043$ is the exact integral in WC39–WC42; $jQ_{n_j}\to\mathcal{I}/200$.'+'\nThe raw phase, its norm, and its shrinking-window certificate remain unchanged (WC54–WC55).',ha='center',fontsize=11)
fig.savefig(root/'ACTUAL_WILSON_COVARIANCE.png',dpi=170)
fig.savefig(root/'ACTUAL_WILSON_COVARIANCE.svg')
print(json.dumps({'figure':'ACTUAL_WILSON_COVARIANCE.png','path_points':len(rows),'bound_functions_only':True}))
