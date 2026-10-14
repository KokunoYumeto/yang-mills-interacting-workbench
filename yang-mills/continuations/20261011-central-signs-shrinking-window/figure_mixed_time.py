from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','mathtext.fontset':'dejavusans','svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(12,10));fig.patch.set_facecolor('#f6f8fb');ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
ax.text(.04,.96,'The actual conditional state and its full operator',fontsize=21,weight='bold',color='#16334a')
ax.text(.04,.922,'All original signs, character indices, metrics and source coefficients retained',fontsize=12,color='#42586b')
def box(x,y,w,h,title,lines):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',fc='white',ec='#9bb1c5',lw=1.3))
    ax.text(x+.018,y+h-.04,title,fontsize=15,weight='bold',color='#16334a',va='top')
    for n,line in enumerate(lines):ax.text(x+.018,y+h-.10-.055*n,line,fontsize=14,color='#172c3c',va='top')
box(.04,.65,.43,.23,'Original state → spherical tangent space',[
    r'$h_\tau=\sqrt{p_\tau},\quad \sum_\tau h_\tau^2=1,\quad n=2^{N_j}$',
    r'$\mathrm{Ran}\,Q(U)=T_{h(U)}S^{n-1}\otimes\mathbb{C}$',
    r'$\Xi_{\tau S}=h_\tau(\chi_S-r_S),\quad S\ne\varnothing$'])
box(.53,.65,.43,.23,'Exact metric and inverse maps  [MTO8]',[
    r'$v=\Xi c,\quad c=C^{-1}\Xi^*v$',
    r'$\Xi^*\Xi=C,\quad \Xi C^{-1}\Xi^*=Q$',
    r'$\|v\|^2=c^*Cc,\quad C_{ST}=r_{S\triangle T}-r_Sr_T$'])
ax.annotate('',xy=(.525,.76),xytext=(.482,.76),arrowprops=dict(arrowstyle='<->',lw=2,color='#1b6b83'))
box(.04,.35,.92,.25,'Full derivative, connection and curvature  [MTO9–MTO10]',[
    r'$d(\Xi c)=\Xi(dc+\mathcal{A}c)-\frac{1}{2}h\,dr^Tc,\qquad \mathcal{A}=\frac{1}{2}C^{-1}dC$',
    r'$\mathcal{R}^C=-\frac{1}{4}C^{-1}dC\wedge C^{-1}dC=\frac{1}{4}C^{-1}dr\wedge dr^T$',
    'The normal derivative remains in the energy and the curvature calculation.'])
box(.04,.055,.92,.24,'Original ground equation evaluates the full complementary energy  [MTO16–MTO18]',[
    r'$q(\Xi c,\Xi d)=\kappa_*\int A^2\sum_i[(X_ic)^*C(X_id)+\overline{r_i^Tc}(r_i^Td)]\,dU$',
    r'$K(t;g,f)=\langle\beta_g,e^{-tD_C}\beta_f\rangle_C,\quad \beta_f=-\kappa_*C^{-1}q_f$',
    r'$\langle Bg,e^{-tD}y\rangle=\langle\beta_g,e^{-tD_C}d^X\rangle_C\quad$ [MTO14]'])
ax.text(.04,.018,'Exact maps of the original conditional state; no continuum limit or sign of the mixed correlation is asserted.',fontsize=11,color='#42586b')
fig.subplots_adjust(left=.01,right=.99,top=.99,bottom=.01)
for ext in ['png','svg']:fig.savefig(O/f'ACTUAL_CHARACTER_MEMORY_MAP.{ext}',dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
