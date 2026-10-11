"""Reproducible diagram of exact LEM maps and proved bound functions."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'font.family':'DejaVu Sans'})
fig,axs=plt.subplots(2,2,figsize=(15,10),layout='constrained')
blue='#205d91'; orange='#bd601a'; green='#257d67'; purple='#7952a5'
ax=axs[0,0];ax.axis('off');ax.set_title('A. Original shrinking states become zero-energy states',loc='left',weight='bold',pad=14)
boxes=[(.04,.70,.19,.15,'Vacuum\n'+r'$V$',blue),(.25,.70,.24,.15,'Strict window\n'+r'$L^{<}$',green),(.51,.70,.20,.15,'Endpoint\n'+r'$J$',orange),(.73,.70,.23,.15,'Rate defect\n'+r'$D_0$',purple)]
for x,y,w,h,label,color in boxes:
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.01',facecolor=color,edgecolor='none',alpha=.16))
    ax.text(x+w/2,y+h/2,label,ha='center',va='center',color=color)
ax.text(.50,.94,r'$\ker A=V\mathcal{H}\ \oplus\ L^{<}\mathcal{H}\ \oplus\ J\mathcal{H}\ \oplus\ D_0\mathcal{H}$',ha='center')
ax.annotate('',xy=(.37,.44),xytext=(.47,.69),arrowprops={'arrowstyle':'->','color':green,'lw':2})
ax.text(.37,.38,r'$C:\operatorname{ran}L\longrightarrow\ker A_{\rm rec}\cap\Omega^\perp$',ha='center',color=green)
ax.text(.50,.24,r'$\|v\|^2=\|Cv\|^2+\|(I-C)v\|^2$',ha='center')
ax.text(.50,.12,r'$CLC-(CLC)^2=CL(I-C)LC$',ha='center')
ax.text(.02,.01,'Exact projections and cyclic defect: LEM2–LEM9.\nNo nonzero raw norm is assumed.',va='bottom',fontsize=10)

ax=axs[0,1];ax.axis('off');ax.set_title('B. Every endpoint keeps three approach spaces',loc='left',weight='bold',pad=14)
for x,label,color in [(.18,r'$D_c^{-}$',blue),(.50,r'$J_c$',orange),(.82,r'$D_c^{+}$',purple)]:
    ax.text(x,.78,label,ha='center',fontsize=20,color=color)
    ax.annotate('',xy=(.50,.44),xytext=(x,.68),arrowprops={'arrowstyle':'->','color':color,'lw':2})
ax.text(.50,.38,r'$Z_c=\mathbf{1}_{\{c\}}(A)$',ha='center',fontsize=18)
ax.text(.18,.91,'below',ha='center');ax.text(.50,.91,'exact',ha='center');ax.text(.82,.91,'above',ha='center')
ax.text(.50,.23,r'$[\,\mathbf{1}_{(\alpha,\beta)}(A_j)\,]$',ha='center',fontsize=14)
ax.text(.50,.13,r'$=\mathbf{1}_{(\alpha,\beta)}(A)P+D_\alpha^{+}+D_\beta^{-}$',ha='center',fontsize=14)
ax.text(.02,.01,'Heat correlations recover the total atom.\nOriginal endpoint membership retains more data: LEM17–LEM20.',va='bottom',fontsize=10)

ax=axs[1,0];ax.set_title('C. Actual spatial face average: positive-energy upper bound',loc='left',weight='bold',pad=13)
js=np.arange(2,65); vals=[]
for j in js:
    a=1/(100*j);ks=np.arange(-100*j-1,100*j+2)
    one=lambda off:a*np.sum(np.maximum(1-np.abs(a*(ks+off)),0)**2)
    vals.append(8*a**3*one(.5)**2*one(0))
ax.loglog(js,vals,color=blue,lw=2,label=r'$8a_j^6\sum_p|f(x_{p,j})|^2$')
ax.loglog(js,8/(27*125000)*js.astype(float)**-3,'--',color=orange,label=r'$\frac{8}{27\cdot125000}\,j^{-3}$')
ax.set_xlabel(r'Original path index $j$');ax.set_ylabel('Proved bound, not measured spectral mass')
ax.grid(alpha=.22,which='both');ax.legend(fontsize=10)
ax.text(.04,.07,r'$\kappa_*=\alpha=1,\quad f(x)=\prod_{i=1}^3(1-|x_i|)_+$'+'\n'+r'$B_{f,j}=a_j^3\sum_p f(x_{p,j})W_p$; LEM28–LEM29',transform=ax.transAxes,fontsize=10)

ax=axs[1,1];ax.set_title('D. A physical-time detector retains positive energy',loc='left',weight='bold',pad=13)
lam=np.linspace(0,5,500);t=np.log(2); h=np.exp(-t*lam)-np.exp(-2*t*lam)
ax.plot(lam,h*h,color=green,lw=2,label=r'$h_t(\lambda)^2,\ t=\log2$')
ax.scatter([0,1],[0,1/16],color=[purple,orange],s=45,zorder=5)
ax.annotate(r'$h_t(1)^2=1/16$',xy=(1,1/16),xytext=(2,.064),arrowprops={'arrowstyle':'->'},fontsize=11)
ax.set_xlabel(r'Original physical energy $\lambda$');ax.set_ylabel('Exact filter weight')
ax.set_ylim(0,.095);ax.grid(alpha=.22)
ax.text(.04,.87,r'$d_{t,j}=(e^{-tA_j}-e^{-2tA_j})B_j\psi_j$'+'\n'+r'$\|d_t\|^2=\lim_{\mathcal{U}}(K_j(2t)-2K_j(3t)+K_j(4t))$',transform=ax.transAxes,fontsize=10,bbox={'facecolor':'white','alpha':.9,'edgecolor':'none'})
ax.text(.52,.47,'Zero energy and escape\nare killed exactly.\nNo state weight is assumed.\nLEM42–LEM47.',transform=ax.transAxes,fontsize=10)
fig.suptitle('Actual low-energy receiving maps on the unchanged Yang–Mills path',fontsize=18,weight='bold')
fig.savefig(ROOT/'ACTUAL_LOW_ENERGY_MAPS.png',dpi=180)
fig.savefig(ROOT/'ACTUAL_LOW_ENERGY_MAPS.svg')
print('Rendered PNG and SVG from the exact displayed definitions.')
