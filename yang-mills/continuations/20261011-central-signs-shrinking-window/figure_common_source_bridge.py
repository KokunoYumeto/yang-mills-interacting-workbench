from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,axes=plt.subplots(2,2,figsize=(16,10),layout='constrained')
fig.suptitle('Common spatial coefficient: force defect and the physical source',fontsize=23,weight='bold')
blue='#24577d';green='#24684d';red='#ac492d'
for ax in axes.flat:ax.set_axis_off();ax.set_xlim(0,1);ax.set_ylim(0,1)
a=axes[0,0]
a.text(.02,.92,'Exact force-gradient defect',fontsize=18,weight='bold')
a.text(.02,.73,r'$F_c=dW_c+R_c,\quad W_c=b_j\sum_p\bar c_pD_p$',fontsize=20,color=blue)
a.text(.02,.52,r'$R_c=b_j\sum_p\sum_{e\in\partial p}(c_e-\bar c_p)\Pi_edD_p$',fontsize=19,color=blue)
a.text(.02,.29,r'$z_{\varphi,j}\leq\frac{4a_j^2M_\varphi^2d_Q}{\kappa_*^2}=O(1)$',fontsize=21,color=green)
a.text(.02,.12,'Full face-pair covariance retained. The removed current\nhas a bounded second moment at the original energy λ.\nTFC21–TFC22.',fontsize=12)
a=axes[0,1]
a.text(.02,.92,'Two original centered observables',fontsize=18,weight='bold')
a.text(.02,.73,r'$X_{\varphi,j}=\frac{a_j}{2}\sum_p\varphi(x_p)D_p'
       r'-\mu_j\!\left(\frac{a_j}{2}\sum_p\varphi(x_p)D_p\right)$',fontsize=17,color=blue)
a.text(.02,.50,r'$Q_{\varphi,j}=\frac{\kappa_*^2a_j^3}{2}(G_c-\mu_jG_c)$',fontsize=21,color=green)
a.text(.02,.29,r'$G_c=\sum_ec_e|d_ew|^2,\quad c=\mathcal{A}_j(\varphi,\varphi,\varphi)$',fontsize=18)
a.text(.02,.12,'The actual state, amplitudes, centers and centering\nconstants stay explicit. TFC23.',fontsize=12)
a=axes[1,0]
a.text(.02,.92,'Exact bridge and shrinking physical bands',fontsize=18,weight='bold')
a.text(.02,.73,r'$dX_{\varphi,j}+dQ_{\varphi,j}'
       r'=-\frac{\kappa_*a_j}{2}L_1P\mathsf{C}c+Pe_{\varphi,j}$',fontsize=18,color=blue)
a.text(.02,.51,r'$\|e_{\varphi,j}\|=O(a_j)$',fontsize=21,color=green)
a.text(.02,.32,r'$\|E_1([0,\theta s_j])(dX_{\varphi,j}+dQ_{\varphi,j})\|=O(a_j)$',fontsize=16,color=green)
a.text(.02,.12,'Energy-weighted masses are compared. The full signed\nthree-shift response has an explicit error. TFC24–TFC25.',fontsize=12)
a=axes[1,1]
a.text(.02,.92,'Leading Hessian remainder on common fields',fontsize=18,weight='bold')
a.text(.02,.73,r'$\mathcal{H}_jh\longrightarrow0,\qquad'
       r'h=(\varphi,\varphi,\varphi)$',fontsize=21,color=green)
a.text(.02,.52,r'$\mathcal{Q}h=\kappa_*\mathcal{G}h$',fontsize=23,color=blue)
a.text(.02,.30,'TFC26 identifies the exact common-subspace kernel\nand all its cross pairings.',fontsize=13)
a.text(.02,.11,'Positive physical window mass and reconstruction\nstill require the next calculations.',fontsize=13,color=red)
fig.text(.5,-.018,'Proof: TWO_FORM_FORCE_AND_COMMON_SPECTRUM.md, TFC21–TFC26. '
         'Full original formulas, gauge projection and exterior edges retained.',ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/('COMMON_SOURCE_BRIDGE.'+ext),dpi=170,bbox_inches='tight')
