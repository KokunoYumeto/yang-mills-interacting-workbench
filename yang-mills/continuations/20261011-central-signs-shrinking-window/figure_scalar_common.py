from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,axes=plt.subplots(2,2,figsize=(16,11),layout='constrained')
fig.suptitle('Original common scalar observable: exact reconstruction and physical spectral mass',
             fontsize=21,weight='bold')
blue='#24577d';green='#24684d';red='#ac492d'
for ax in axes.flat:ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
ax=axes[0,0]
ax.text(.02,.93,'Exact mean-zero scalar identity',fontsize=18,weight='bold')
ax.text(.02,.73,r'$X_{\varphi,j}+Q_{\varphi,j}=\frac{\kappa_*^2a_j^3}{2}B_c+r_{\varphi,j}$',fontsize=22,color=blue)
ax.text(.02,.52,r'$r_{\varphi,j}=\kappa_*L_0^{-1}\delta_\mu e_{\varphi,j},\qquad dr_{\varphi,j}=Pe_{\varphi,j}$',fontsize=18)
ax.text(.02,.31,r'$\left\|\frac{\kappa_*^2a_j^3}{2}B_c\right\|^2=\frac{\kappa_*^3a_j}{4}\chi_{\varphi,j}$',fontsize=22,color=green)
ax.text(.02,.09,'The original scalar inverse is on mean-zero functions.\nAll centering constants and factors remain. TSC1–TSC3.',fontsize=12)
ax=axes[0,1]
ax.text(.02,.93,'Full positive-energy band',fontsize=18,weight='bold')
ax.annotate('',xy=(.95,.68),xytext=(.06,.68),arrowprops={'arrowstyle':'->','lw':2,'color':blue})
ax.plot([.31,.31],[.65,.71],color=blue,lw=2)
ax.text(.04,.57,'0',fontsize=15)
ax.text(.25,.54,r'$\epsilon s_j$',fontsize=17)
ax.text(.85,.55,r'$\lambda$',fontsize=18)
ax.text(.39,.74,'Every Borel subset; no upper cutoff',fontsize=12,color=green)
ax.text(.02,.35,r'$\|E_0(B)(X_{\varphi,j}+Q_{\varphi,j})\|\leq d_{\varphi,j}(\epsilon s_j)$',fontsize=18,color=green)
ax.text(.02,.19,r'$d_{\varphi,j}(\epsilon s_j)=O(\sqrt{a_j}),\qquad s_j=100\kappa_*a_j$',fontsize=17)
ax.text(.02,.04,'Fixed common test; full finite bound in TSC4–TSC5.',fontsize=12)
ax=axes[1,0]
ax.text(.02,.93,'Original physical mass and all three shifts',fontsize=18,weight='bold')
ax.text(.02,.73,r'$|\sqrt{\nu_{X,j}(B)}-\sqrt{\nu_{Q,j}(B)}|\leq d_{\varphi,j}(u)$',fontsize=21,color=green)
ax.text(.02,.53,r'$\mathcal{W}_{Z,j}(z)=\left\|\frac{\sqrt{zL_0}}{L_0+z}Z\right\|^2$',fontsize=21,color=blue)
ax.text(.02,.33,r'$z=\theta s_j,\quad\varepsilon\theta s_j,\quad R_{\rm win}\theta s_j$',fontsize=20)
ax.text(.02,.09,'The original annulus has equal lower and upper mass limits\nfor X and Q. Its positive value remains to be evaluated.\nFull signed bounds: TSC6, TSC8–TSC9.',fontsize=12)
ax=axes[1,1]
ax.text(.02,.93,'The zero-energy residual stays explicit',fontsize=18,weight='bold')
ax.text(.02,.73,r'$\langle r_{\varphi,j},L_0r_{\varphi,j}\rangle\leq\kappa_*\mathfrak{e}_{\varphi,j}^{\,2}$',fontsize=21,color=blue)
ax.text(.02,.52,r'$\nu_{r,j}([\epsilon s_j,\infty))\leq\frac{\mathfrak{e}_{\varphi,j}^{\,2}}{100\epsilon a_j}=O(a_j)$',fontsize=21,color=green)
ax.text(.02,.31,'Total residual variance at zero is unresolved.\nThe exact B/r cross covariances remain.',fontsize=14,color=red)
ax.text(.02,.09,'TSC10–TSC11 evaluate the actual mixed density/score sum.\nTSC12 gives a whole-variance floor of order a; it does not\nallocate that mass to the physical annulus.',fontsize=12)
fig.text(.5,-.02,'Proof: SCALAR_COMMON_SOURCE_RECONSTRUCTION.md, TSC1–TSC12. '
         'Schematic spectral axis; no numerical ground state is shown.',ha='center',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/('SCALAR_COMMON_RECONSTRUCTION.'+ext),dpi=170,bbox_inches='tight')
