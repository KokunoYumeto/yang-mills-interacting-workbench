from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
fig=plt.figure(figsize=(11,12),facecolor='white');gs=fig.add_gridspec(3,2,height_ratios=[1.25,.9,1],hspace=.42,wspace=.25)
ax=fig.add_subplot(gs[0,0]);ax.axis('off')
pos={'s':(0,-1),'t':(0,4)}
for i,x in enumerate([-3,-1,1,3]):
 pos[f'b{i}']=(x,0);pos[f'a{i}']=(x,3)
 for u,v,col,lw in [('s',f'b{i}','#81929b',1.6),(f'b{i}',f'a{i}','#b54640',3.5),(f'a{i}','t','#81929b',1.6)]:
  ax.plot([pos[u][0],pos[v][0]],[pos[u][1],pos[v][1]],color=col,lw=lw)
 ax.text(x,1.5,[r'$+y$',r'$-y$',r'$+z$',r'$-z$'][i],ha='center',bbox=dict(fc='white',ec='none'))
ax.plot([0,0],[-1,4],color='#24667e',lw=3);ax.text(.12,1.5,r'$e$',color='#24667e',fontsize=14)
for x,y in pos.values():ax.plot(x,y,'o',color='#263842',ms=5)
ax.text(0,-1.4,r'$s$',ha='center');ax.text(0,4.2,r'$t$',ha='center')
ax.set(xlim=(-3.8,3.8),ylim=(-1.8,4.7));ax.set_title('Original interior edge star\n13 links, 10 vertices')
ax=fig.add_subplot(gs[0,1]);ax.axis('off')
ax.text(0,.96,'Condition on every link except the four red links.\nEach red link belongs to one incident face.\nThe original common link e stays fixed.',va='top',linespacing=1.6)
ax.text(0,.66,r'$\nabla^2 w_{\rm slice}\geq-cg,\quad c=2/(\kappa_*a)$'+'\n\n'+r'$F_e=\sum_{p\ni e}\epsilon_{p,e}\varphi_pv(H_{p,e})$'+'\n\n'+r'$\mathrm{Var}_{\nu}(F_e)\geq\frac{4}{7+16c}\sum_{p\ni e}|\varphi_p|^2$',va='top',linespacing=1.8)
ax.text(0,-.08,'This is the actual conditional density.\nIts links need not be independent.\nSchematic graph layout; no geometric projection\nor field configuration is substituted. [SMP2–SMP5]',va='top',fontsize=10)
ax=fig.add_subplot(gs[1,:]);ax.axis('off')
ax.text(.5,.97,r'$X=\frac{a}{2}\sum_p\varphi_p(D_p-\mu D_p),\quad S_{pq}=\langle Z_p,Z_q\rangle_\mu$',ha='center',va='top',fontsize=15)
ax.text(.5,.7,r'$M_1\geq A_*I,\quad A_*=\frac{4\kappa_*^2a^3}{32+7\kappa_*a}$',ha='center',va='top',fontsize=15)
ax.text(.5,.43,r'$M_2\leq\frac{21\kappa_*^2a^2}{4}I+\kappa_*(\frac{1}{2}+2c)M_1$',ha='center',va='top',fontsize=15)
ax.text(.5,.15,r'$S\geq\sigma_*I,\quad \sigma_*=\frac{64\kappa_*^2a^4}{(32+7\kappa_*a)(736+155\kappa_*a)}$',ha='center',va='top',fontsize=15)
data=json.loads((O/'SPATIAL_MOMENT_CHECKS.json').read_text())['original_path']
for col,key,label,lim in [(0,'first_floor_over_a3',r'$A_*/a^3$',.8**2/8),(1,'covariance_floor_over_a4',r'$\sigma_*/a^4$',.8**2/368)]:
 ax=fig.add_subplot(gs[2,col]);ax.semilogx([r['j'] for r in data],[r[key] for r in data],'o-',color='#24667e',label='exact finite bound')
 ax.axhline(lim,ls='--',color='#b54640',label='proved coefficient limit');ax.set_xlabel('original regulator j');ax.set_ylabel(label);ax.ticklabel_format(axis='y',style='sci',scilimits=(0,0));ax.grid(alpha=.25);ax.legend(fontsize=9)
fig.suptitle('Actual raw spatial covariance has a polynomial floor\nAll original faces, coefficients and shared-link correlations retained [SMP1–SMP13]',fontsize=15,y=.985)
fig.text(.5,.018,'Graphs evaluate bound formulas at κ*=4/5 and a=(100j)⁻¹; they are not measured vacuum covariances.\nThe spectral mass in the shrinking annulus remains to be evaluated.',ha='center',fontsize=10)
fig.savefig(O/'CONDITIONAL_LINKS_AND_SPATIAL_COVARIANCE.png',dpi=150,bbox_inches='tight')
fig.savefig(O/'CONDITIONAL_LINKS_AND_SPATIAL_COVARIANCE.svg',bbox_inches='tight')
plt.close(fig)
