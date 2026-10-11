"""Reproducible proof diagram. All formulas and scopes refer to ASL locators."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root=Path(__file__).resolve().parent
fig=plt.figure(figsize=(16,10),facecolor='#fafbfd')
fig.text(.04,.955,'Actual vacuum limits on the prescribed path',fontsize=25,weight='bold',color='#142b45')
fig.text(.04,.918,'A proved continuous sector, its retained escape sector, and exact original-observable maps',fontsize=14,color='#45596e')
axes=[fig.add_axes([.035,.105,.30,.77]),fig.add_axes([.353,.105,.30,.77]),fig.add_axes([.671,.105,.295,.77])]
for ax in axes:
    ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(ax,x,y,w,h,text,color='#e5edf7',size=13):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.013,rounding_size=.015',facecolor=color,edgecolor='#6a7f97',linewidth=1.2))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=size,color='#122b45',linespacing=1.5)
def arrow(ax,a,b,label=None):
    ax.add_patch(FancyArrowPatch(a,b,arrowstyle='-|>',mutation_scale=16,color='#395775',linewidth=1.6))
    if label: ax.text((a[0]+b[0])/2+.035,(a[1]+b[1])/2,label,fontsize=11,va='center',color='#395775')

ax=axes[0]
ax.text(.01,.985,'1  Exact Hilbert-space split',fontsize=17,weight='bold',va='top')
box(ax,.04,.79,.92,.13,'Original physical spaces and vacua\n'+r'$A_j=H_j-E_j^{\rm vac}\geq0,\quad\|\psi_j\|=1$'+'\nASL1–4',size=12.5)
arrow(ax,(.5,.775),(.5,.705),'one common ultrafilter')
box(ax,.04,.535,.43,.155,r'$\mathcal{H}_c=P\mathcal{H}_{\mathcal{U}}$'+'\n'+r'$T(t)=e^{-tA}$'+'\n'+r'$\Omega\in\mathcal{H}_c,\ \|\Omega\|=1$',color='#dff1e8',size=12)
box(ax,.53,.535,.43,.155,r'$\mathcal{H}_{\rm esc}=Q\mathcal{H}_{\mathcal{U}}$'+'\n'+r'$Q=I-P\ne0$'+'\n'+r'$T(t)Q=0\quad(t>0)$',color='#ffebd8',size=12)
box(ax,.04,.32,.92,.15,r'$P=\mathrm{s}\!\lim_{t\downarrow0}T(t)$'+'\n'+r'$E_b=[\mathbf{1}_{[0,b]}(A_j)]\ \longrightarrow\ P$'+'\nStrong limits proved, not assumed · ASL8–15',size=12)
box(ax,.04,.095,.92,.16,'The full escaping norm remains\n'+r'$\|Q[v_j]\|^2=$'+'\n'+r'$\lim_{b\to\infty}\lim_{\mathcal{U}}\|\mathbf{1}_{(b,\infty)}(A_j)v_j\|^2$'+'\nThe order of limits is essential · ASL15',color='#ffebd8',size=12)

ax=axes[1]
ax.text(.01,.985,'2  Original observable products',fontsize=17,weight='bold',va='top')
box(ax,.04,.735,.92,.185,'General bounded original multipliers\n'+r'$\Phi(B)=PBP|_{\mathcal{H}_c}$'+'\n'+r'$\Phi(BC)-\Phi(B)\Phi(C)=PBQCP$'+'\nEvery missing product passes through Q · ASL20',size=12)
box(ax,.04,.47,.92,.195,'Fixed finite Wilson words\n'+r'$\|W_p\|_\infty\leq2,\quad\|\nabla W_p\|_\infty\leq2$'+'\n'+r'$q_j(W_pv)\leq8q_j(v)+8\kappa_*\|v\|^2$'+'\n'+r'$BP=PB:\quad\Phi(BC)=\Phi(B)\Phi(C)$'+'\nASL23–29',color='#dff1e8',size=12)
box(ax,.04,.195,.92,.205,'An actual escaping multiplier\n'+r'$b_j=e^{ik_jW_{p_j}}$'+'\n'+r'$\|\mathbf{1}_{[0,j]}(A_j)b_j\psi_j\|\leq1/j$'+'\n'+r'$QB\Omega=B\Omega,\quad\|B\Omega\|=1$'+'\n'+r'$PB^*QBP\Omega=\Omega$'+'\nASL30–32',color='#ffebd8',size=12)
ax.text(.5,.095,'Fixed physical loops can have growing length.\nTheir full multiplicity and curvature bounds\nare retained separately in ASL39–45.',ha='center',va='center',fontsize=11.5,color='#45596e',linespacing=1.5)

ax=axes[2]
ax.text(.01,.985,'3  Concrete receiving results',fontsize=17,weight='bold',va='top')
box(ax,.04,.65,.92,.27,'Orientation averages keep every face\n'+r'$\overline{W}_{de,j}=(m_j^2n_j)^{-1}\sum_{p:\,de}W_p$'+'\n'+r'$\|(2-\overline{W}_{de,j})\psi_j\|^2\leq4\epsilon_j\to0$'+'\n'+r'$\|\nabla\overline{W}_{de,j}\|_\infty^2\leq8/(m_j^2n_j)$'+'\n'+r'$\overline{W}_{de}=2I\ \mathrm{on}\ \mathcal{H}_{\rm rec}$'+'\nExact scalar collapse · ASL46–52',color='#dff1e8',size=12)
box(ax,.04,.40,.92,.17,'Actual positive-time correlations\nReflection-positive word Gram matrices\nA nonnegative generator and unit vacuum\nASL33–38; common subsequence ASL64–66',size=12)
box(ax,.04,.10,.92,.225,'Original raw phase remains unchanged\n'+r'$v_j=F_j\psi_j=u_{j,a,b}+z_{j,a,b}+r_{j,a}$'+'\n'+r'$G_j=\|u_{j,a,b}\|^2+\|z_{j,a,b}\|^2+\tau_j(a)$'+'\nRaw norms and tails remain explicit.\nAll correlation cross terms are retained.\nASL53–63',color='#fff3d5',size=11.8)

fig.text(.04,.055,'Scope: the actual prescribed finite-volume vacua. These results do not identify the intended interacting four-dimensional theory.',fontsize=12,color='#45596e')
fig.text(.04,.025,'Proof: ACTUAL_SEMIGROUP_LIMIT.md, ASL1–66. Diagram is schematic: the two sectors are Hilbert summands, not spatial regions.',fontsize=11,color='#45596e')
fig.savefig(root/'ACTUAL_SEMIGROUP_LIMIT.png',dpi=180,bbox_inches='tight')
fig.savefig(root/'ACTUAL_SEMIGROUP_LIMIT.svg',bbox_inches='tight')
print(str(root/'ACTUAL_SEMIGROUP_LIMIT.png'))
