from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
ROOT=Path(__file__).resolve().parent
fig,axs=plt.subplots(1,3,figsize=(15,5.7),gridspec_kw={'width_ratios':[1,1,1.3]})
ax=axs[0]
for l in range(5):
 for k in range(4):ax.annotate('',xy=(k+1,l),xytext=(k,l),arrowprops={'arrowstyle':'->','color':'#267581','lw':1.8})
for l in range(4):ax.annotate('',xy=(0,l+1),xytext=(0,l),arrowprops={'arrowstyle':'->','color':'#a55642','lw':2})
ax.scatter([k for l in range(5) for k in range(5)],[l for l in range(5) for k in range(5)],color='#33444f',s=16,zorder=5)
ax.set(xlim=(-.3,4.3),ylim=(-.3,4.3),aspect='equal',xlabel='k',ylabel='l',xticks=range(5),yticks=range(5))
ax.set_title(r'Boundary coordinates at $i=m=4$',fontsize=12,pad=15)
ax.text(.5,-.2,r'$|\mathcal{B}|=m(m+2)=24$ chords',transform=ax.transAxes,ha='center',fontsize=11)
ax=axs[1]
for k in [0,1]:
 for i in range(4):ax.annotate('',xy=(i+1,k) if k==0 else (i,k),xytext=(i,k) if k==0 else (i+1,k),arrowprops={'arrowstyle':'->','color':'#6d7981','lw':2})
ax.annotate('',xy=(4,1),xytext=(4,0),arrowprops={'arrowstyle':'->','color':'#267581','lw':3})
ax.annotate('',xy=(0,0),xytext=(0,1),arrowprops={'arrowstyle':'->','color':'#a55642','lw':3})
ax.scatter([i for k in [0,1] for i in range(5)],[k for k in [0,1] for i in range(5)],s=22,color='#33444f',zorder=5)
ax.text(2,-.43,r'$m$ original links: $+1$',ha='center',fontsize=11)
ax.text(2,1.2,r'$m$ original links: $-1$',ha='center',fontsize=11)
ax.text(-.15,.5,'−1',ha='right',va='center',fontsize=12,color='#a55642')
ax.text(4.15,.5,'+1',ha='left',va='center',fontsize=12,color='#267581')
ax.set(xlim=(-.7,4.7),ylim=(-1.8,2.8),aspect='equal',xlabel='i',ylabel='k',xticks=range(5),yticks=[0,1])
ax.set_title(r'One full boundary cycle, $l=0$',fontsize=12,pad=15)
ax.text(.5,-.2,r'Diagonal metric: $2+2m=10$',transform=ax.transAxes,ha='center',fontsize=11)
ax=axs[2];ax.axis('off');ax.set_title('Exact physical receiving map',fontsize=12,pad=15)
rows=[(r'$D=\mathcal{S}+\mathcal{S}_{\mathcal{R}}$',r'$D=0$ when every $Z_b=I$.'),
 (r'$n_b^\alpha=X_{b,\alpha}D$',r'The normal derivative can be nonzero.'),
 (r'$G_{\mathcal{B}}=2I+mD_{\rm wall}D_{\rm wall}^{T}$',r'$|\nabla D|^2=\sum_\alpha(n^\alpha)^TG_{\mathcal{B}}n^\alpha$'),
 (r'$D(0)=0,\quad D^{\prime}(0)=-4Ad_0>0$',r'All coefficients retained in JP14–JP15.')]
for y,(a,b) in zip([.93,.71,.49,.23],rows):
 ax.text(.01,y,a,fontsize=12,va='top',color='#267581');ax.text(.01,y-.095,b,fontsize=11,va='top')
fig.suptitle('The original reflection correction and its full boundary kinetic form',fontsize=16,y=.97)
fig.text(.5,.055,'Exact coordinate projections, m=4. Boundary comb: right wall; cycle: l=0 section. Original physical point: o + a(i−L,k−L,l−L).',ha='center',fontsize=10)
fig.text(.5,.017,'Proofs: JP1–JP23. Fibre vanishing does not remove the normal energy. No limiting spectral weight is inferred from this drawing.',ha='center',fontsize=10)
fig.subplots_adjust(left=.045,right=.985,top=.8,bottom=.24,wspace=.35)
for ext in ['png','svg']:
 p=ROOT/('BOUNDARY_REFLECTION.'+ext);fig.savefig(p,dpi=180)
 if ext=='svg':p.write_text('\n'.join(x.rstrip() for x in p.read_text().splitlines())+'\n',encoding='utf-8',newline='\n')
