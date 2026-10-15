from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':13,'mathtext.fontset':'dejavusans'})
fig=plt.figure(figsize=(14,9),facecolor='white')
ax=fig.add_axes([.035,.12,.93,.77]);ax.set(xlim=(-.015,1.015),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,text,color,size=14):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.012',facecolor=color,edgecolor='#536577',lw=1.1))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,linespacing=1.7)
box(.01,.80,.28,.17,r'$P=(G_{\rm in},G_{\rm out},S)\in\mathscr{V}$'+'\n'+r'$\mathfrak{D}P=W$','#e7f1fa')
box(.36,.80,.28,.17,r'$\Pi_{\rm out}P$'+'\n'+r'$\mathfrak{D}\Pi_{\rm out}P=W$','#eef5e8')
box(.71,.80,.28,.17,r'$\mathfrak{J}W=(-\kappa_*d\xi_{\rm res},-\zeta\xi_{\rm res})$'+'\n'+r'$\xi_{\rm res}=(\mathcal{L}+\zeta)^{-1}W$','#f7efe2',11)
for xx in [.30,.65]:ax.annotate('',xy=(xx+.05,.885),xytext=(xx,.885),arrowprops=dict(arrowstyle='->',lw=1.6))
ax.text(.325,.93,r'$\Pi_{\rm out}$',ha='center',fontsize=11)
ax.text(.675,.93,r'$\mathfrak{J}\mathfrak{D}$',ha='center',fontsize=11)
box(.06,.53,.88,.17,r'$\|P\|_{\mathscr{V}}^2=\mathfrak{b}_r'
    r'+\|\Pi_{\rm out}P-\mathfrak{J}W\|_{\mathscr{V}}^2'
    r'+\|(I-\Pi_{\rm out})P\|_{\mathscr{V}}^2$'
    +'\n'+'Both complete, orthogonal kernel components remain.','#f3f3f3',15)
for xx in [.15,.5,.85]:ax.annotate('',xy=(xx,.715),xytext=(xx,.785),arrowprops=dict(arrowstyle='->',lw=1.1))
box(.06,.19,.88,.21,r'$q^{(2)}_v=-6\kappa_*^3(k_Q+r_Q)\,\Delta_Q^2t_v$'
    +'\n'+r'$\mathcal{L}_{\rm out}(k_Q+r_Q)'
    r'=bJ_\times-2b\,\xi_Q\cdot u_\times-2\kappa_*X_\times$'
    +'\n'+r'$\xi_Q=d_Q\log\psi-d_Q\log\sqrt{\rho}$; all six rows and mixed entries remain.','#e9eff6',15)
ax.text(.5,.455,'The original leading row receives the existing boundary-current identities',ha='center',fontsize=13)
ax.text(.5,.08,r'The factor $\Delta_Q^2t_v$ remains inside every weighted moment integral.',ha='center',fontsize=14)
fig.text(.5,.95,'Outside flux and the full residual-energy projection',ha='center',fontsize=21,weight='bold')
fig.text(.5,.065,'ROF1–ROF4: exact maps and kernel norms. ROF10–ROF14: complete coefficient and matrix expressions.',ha='center',fontsize=12)
fig.text(.5,.03,'ROF15–ROF17: original weighted boundary receiver. This diagram does not assert a vanishing spectral error.',ha='center',fontsize=12)
for ext in ['png','svg']:fig.savefig(O/('OUTSIDE_FLUX_PROJECTION.'+ext),dpi=180)
plt.close(fig)
