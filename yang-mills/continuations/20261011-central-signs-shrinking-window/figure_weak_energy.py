from pathlib import Path
import numpy as np,matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
from weak_energy_constants import constants,mp
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(15,8),facecolor='white')
ax=fig.add_axes([.03,.15,.51,.72]);ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,text,color,size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#536577',lw=1.1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,linespacing=1.8)
box(.02,.79,.39,.16,r'$(G,S)\in\mathscr{V}$'+'\n'+r'$\kappa_*^{-1}\|G\|^2+\zeta^{-1}\|S\|^2$','#e7f1fa')
box(.59,.79,.39,.16,r'$W\in\mathscr{H}^{-1}_{\zeta}$'+'\n'+r'$W=-d^{*,\mu}G-S$','#eef5e8')
ax.annotate('',xy=(.58,.87),xytext=(.42,.87),arrowprops=dict(arrowstyle='->',lw=1.5))
ax.text(.5,.94,r'$\mathfrak{D}$',ha='center',fontsize=15)
box(.07,.47,.86,.19,r'$\xi=(\mathcal{L}+\zeta)^{-1}W$'+'\n'+r'$\mathfrak{J}W=(-\kappa_*d\xi,-\zeta\xi),\quad\mathfrak{D}\mathfrak{J}W=W$','#f7efe2')
ax.annotate('',xy=(.5,.68),xytext=(.77,.78),arrowprops=dict(arrowstyle='->',lw=1.4))
box(.07,.12,.86,.22,r'$(G,S)=\mathfrak{J}W+K,\quad K\in\ker\mathfrak{D}$'+'\n'+r'$\mathfrak{b}_r=\|(G,S)\|_{\mathscr{V}}^2-\|K\|_{\mathscr{V}}^2$','#f3f3f3')
ax.annotate('',xy=(.5,.355),xytext=(.5,.46),arrowprops=dict(arrowstyle='->',lw=1.4))
ax.text(.5,.025,'The complete kernel component remains in the identity.',ha='center',fontsize=11)
ax2=fig.add_axes([.63,.23,.34,.58])
js=sorted(set(int(j) for j in np.geomspace(4,10**6,50)))
rows=[constants(j) for j in js]
ax2.semilogx(js,[float(mp.log10(r['oldenergy'].value)) for r in rows],color='#a65b2a',ls='--',lw=2,label=r'Inherited $\widehat{\mathfrak{P}}_\zeta^2/\zeta$')
ax2.semilogx(js,[float(mp.log10(r['energy'].value)) for r in rows],color='#24577e',lw=2.4,label=r'Complete new $\Xi_\zeta$')
ax2.set(xlabel=r'Original regulator index $j$',ylabel=r'$\log_{10}$(complete coefficient of $\|F\|_\rho^2$)')
ax2.grid(alpha=.25);ax2.legend(loc='upper left',fontsize=11)
fig.text(.5,.95,'Full cubic flux and the original residual energy',ha='center',fontsize=20,weight='bold')
fig.text(.5,.095,'WCR4–WCR7: exact typed maps and kernel norm. WCR13–WCR14: every finite coefficient and cross term is evaluated.',ha='center',fontsize=11)
fig.text(.5,.045,'Upper functions on the original path, with '+r'$\kappa_*=4/5,\ \theta=1$'+'. No measured state energy or vanishing tail error is claimed.',ha='center',fontsize=11,color='#444444')
for ext in ['png','svg']:fig.savefig(O/('FULL_CUBIC_FLUX_ENERGY.'+ext),dpi=180)
plt.close(fig)
print('Rendered the full flux and finite-energy figure.')
