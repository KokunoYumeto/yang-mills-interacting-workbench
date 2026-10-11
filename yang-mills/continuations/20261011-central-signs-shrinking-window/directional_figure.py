from pathlib import Path
import json, math
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root=Path(__file__).resolve().parent
data=json.loads((root/'DIRECTIONAL_CHECKS.json').read_text())
rows=[r for r in data['records'] if r['n']>=5]; n=np.array([r['n'] for r in rows])
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'axes.spines.top':False,'axes.spines.right':False})
fig,axes=plt.subplots(1,3,figsize=(17.4,6.2),gridspec_kw={'width_ratios':[1,1.1,1]})
blue='#205b9b'; red='#b74438'; green='#247d57'
axes[0].loglog(n,[r['single_face_defect'] for r in rows],'o-',color=blue,label=r'Every nonzero face defect $D_{23}$')
axes[0].loglog(n,[r['sigma_squared']/2 for r in rows],'s--',color=green,label=r'Ordinary soft value $\sigma_*^2/2$')
axes[0].set(title='Small elementary curvature',xlabel=r'Original box size $n=2L+1$',ylabel='Exact configuration values')
axes[0].legend(fontsize=9,loc='upper right');axes[0].grid(alpha=.2,which='both')
axes[0].text(.04,.08,r'$D_{23}\sim\pi^2/(4m^2)$'+'\n'+r'$\sigma_*^2/2\sim\pi^2/n^2$',transform=axes[0].transAxes,fontsize=10,bbox={'facecolor':'white','edgecolor':'none','alpha':.85})
axes[1].semilogx(n,[r['transverse_hessian'] for r in rows],'o-',color=red,label=r'$Y_{e_1}^2W=Y_{e_2}^2W$')
axes[1].semilogx(n,[r['parallel_hessian'] for r in rows],'s-',color=green,label=r'$Y_{e_3}^2W$')
axes[1].axhline(.5,color=red,linestyle=':',label=r'Proved transverse limit $1/2$')
axes[1].set(title='Retained root transports',xlabel=r'Original box size $n=2L+1$',ylabel='Exact directional potential Hessian',ylim=(-.02,.55))
axes[1].legend(fontsize=9,loc='center right');axes[1].grid(alpha=.2)
axes[2].semilogx(n,[r['B_n'] for r in rows],'o-',color=blue,label=r'Three-insertion bound $B_n$')
axes[2].semilogx(n,[r['B_full23'] for r in rows],'s--',color='#666666',label=r'Four-letter bound $B_n^{\mathrm{four}}$')
axes[2].axhline(data['B_limit'],color=blue,linestyle=':')
axes[2].set(title='Uniform soft-direction coefficient',xlabel=r'Original box size $n=2L+1$',ylabel=r'$|Y_z^2W|\leq B_n|z|^2$',ylim=(1.1,3.0))
axes[2].legend(fontsize=9,loc='lower right');axes[2].grid(alpha=.2)
axes[2].text(.16,.10,r'$B_n\longrightarrow\frac{3}{2}+\frac{8}{\pi^2}$'+'\nDP20–DP22',transform=axes[2].transAxes,fontsize=12)
fig.suptitle('Elementary face defects do not remove the transported soft curl',fontsize=17,y=.97)
fig.text(.5,.895,r'Exact original links: $U_1=U_2=I$, $U_3(i,k,l)=\exp((\pi k/m)T_3)$, $m=n-1$ (DP29)',ha='center',fontsize=12)
fig.text(.5,.045,'This is an explicit configuration family, not a vacuum sample. The actual-vacuum receiving map is DP23–DP28.\nThe original path is nⱼ = 2j⁴ + 1; every plotted value retains the complete finite-box coefficients.',ha='center',fontsize=11)
fig.subplots_adjust(left=.065,right=.985,bottom=.21,top=.79,wspace=.34)
fig.savefig(root/'DIRECTIONAL_ROOT_DEFECT.png',dpi=170)
fig.savefig(root/'DIRECTIONAL_ROOT_DEFECT.svg')
print(json.dumps({'figure':'DIRECTIONAL_ROOT_DEFECT.png','points_per_curve':len(n),'source':'CHECKS.json','limits_proved_at':'DP22 and DP35'}))
