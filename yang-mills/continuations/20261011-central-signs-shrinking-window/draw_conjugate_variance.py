from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

root=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':11,'mathtext.fontset':'stix','font.family':'DejaVu Sans'})
fig,(ax,bx)=plt.subplots(1,2,figsize=(14,6),gridspec_kw={'width_ratios':[1.05,1]})
fig.subplots_adjust(left=.04,right=.98,top=.86,bottom=.17,wspace=.15)
fig.suptitle('Original rooted soft field and the actual-vacuum variance bound',fontsize=17)
ax.set_xlim(0,10);ax.set_ylim(0,7);ax.axis('off')
nodes={'root':(1,3.7),'s(c)':(5,5.2),'t(c)':(8.8,3.7)}
for label,(x,y) in nodes.items():
 ax.plot(x,y,'o',color='#1e354f',ms=9);ax.text(x,y+.35,label,ha='center',fontsize=12)
for p,q,color,rad in [('root','s(c)','#2369a1',.18),('s(c)','t(c)','#8a3a24',0),('root','t(c)','#46764e',-.27)]:
 ax.add_patch(FancyArrowPatch(nodes[p],nodes[q],connectionstyle=f'arc3,rad={rad}',arrowstyle='->',mutation_scale=15,color=color,lw=2.2))
ax.text(2.4,5.1,r'$t_s,\quad p_s(V)$',color='#2369a1',fontsize=15)
ax.text(7.4,5.15,r'$U_c,\quad V_c$',color='#8a3a24',fontsize=15)
ax.text(4.7,2.35,r'$t_t,\quad p_t(V)$',color='#46764e',fontsize=15)
ax.text(5,1.48,r'$YZ_c=(p_s+V_c)(z\cdot T)Z_c-p_tZ_c(z\cdot T)$',ha='center',fontsize=16)
ax.text(5,.65,r'$B=Y_{V_{23},u_1},\quad \mathrm{div}\,B=0,\quad B|u_1|^2=0$',ha='center',fontsize=15)
ax.set_title('Exact root terms (CV9 and CV15)',fontsize=13)

j=np.linspace(2,30,500);m=2*j**4;n=m+1;hh=np.pi/(2*n);ss=np.sin(hh);cc=np.cos(hh);C=1/np.tan(hh)
N=3*m*n*n;M=3*m*m*n;S1=np.sqrt(2/n)*C*(C-cc);A1=m*np.sqrt(2/n)*C*(5*C-4*cc)
energy=np.minimum(20000*j*j*M,300*j*np.sqrt(N*M));xx=4*S1*S1;xi=10000*j*j
bx.loglog(j,energy*xx,label=r'$(\mathcal{E}_0/\kappa_*)\,4S_1^2$',color='#2369a1',lw=2.5)
bx.loglog(j,2*xi*ss*ss*xx*xx,label=r'$2\xi s_0^2(4S_1^2)^2$ (subtracted)',color='#8a3a24',lw=2.2)
bx.loglog(j,6*S1*A1,label=r'$6S_1A_1$ (Laplacian bound)',color='#46764e',lw=2.2)
bx.set_xlabel(r'Original path integer parameter $j$ (curves interpolate)')
bx.set_ylabel('Computed bound terms')
bx.set_title(r'CV27, $\kappa_*=1$, evaluated at $x=4S_1^2$',fontsize=13)
bx.grid(which='both',alpha=.2);bx.legend(loc='upper left',fontsize=10,framealpha=.95)
fig.text(.5,.065,'Left: schematic tree paths with the exact matrix order; physical coordinates are CV1–CV2.  Right: bound functions, not vacuum samples.\n'
         'The subtracted curvature term is smaller by j^7; the directional kinetic remainder and signed commutator correction remain explicit (CV16, CV24, CV44).',
         ha='center',va='center',fontsize=10)
fig.savefig(root/'CONJUGATE_VARIANCE_FIGURE.png',dpi=180)
fig.savefig(root/'CONJUGATE_VARIANCE_FIGURE.svg')
print(root/'CONJUGATE_VARIANCE_FIGURE.png')
