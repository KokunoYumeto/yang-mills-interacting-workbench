from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
W=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(14,7.5),facecolor='#f7fafc');ax.set(xlim=(0,14),ylim=(0,7.5));ax.axis('off')
ax.text(.4,7.1,'Ordered action: two verified strengthenings',fontsize=24,weight='bold',color='#19354f')
for x,color in [(.4,'#e4eef8'),(7.25,'#e0f2eb')]:ax.add_patch(FancyBboxPatch((x,1.25),6.1,5.1,boxstyle='round,pad=.12',facecolor=color,edgecolor='#688097'))
ax.text(.65,5.95,'Original ordered Hermitian factors',fontsize=13,weight='bold')
ax.text(.65,5.25,r'$P(t)=\prod_{a=1}^4 e^{itH_a},\quad\Phi(t)=r-\mathrm{Re\,Tr}\,P(t)$'+'\n'+r'$q_{\rm op}=\sum_a\|H_a\|_{\rm op},\quad q_{\rm HS}=\sum_a\|H_a\|_{\rm HS}$'+'\n'+r'$|\Phi^{(k)}(t)|\leq\min\{r q_{\rm op}^{k},q_{\rm HS}^{2}q_{\rm op}^{k-2}\}$'+'\n'+r'$k\geq2$; two exact Hilbert–Schmidt factors'+'\n'+r'Cubic remainder $\leq32\eta^3/3$ if $\|H_a\|_{\rm HS}\leq\eta$'+'\n'+'Matrix-size factor removed · UR8',fontsize=12,va='top',linespacing=1.5)
ax.text(7.5,5.95,'Original SU(2) coordinate subspaces',fontsize=13,weight='bold')
ax.text(7.5,5.25,r'$X(y)=-iy\cdot\sigma/2,\quad P(t)=\prod_a e^{tX(y_a)}$'+'\n'+r'$C=\sum_a y_a,\quad B=\sum_{a<b}y_a\times y_b$'+'\n'+r'$C=0:\quad P^{\prime}(0)=0,\quad P^{\prime\prime}(0)=X(B)$'+'\n'+r'$C=B=0:\quad 0\leq 2-\mathrm{Tr}\,P(t)$'+'\n'+r'$\qquad\leq |t|^6(\sum_a|y_a|)^6/2304$'+'\n'+'Exact product bound · UR13',fontsize=12,va='top',linespacing=1.5)
ax.text(.4,.65,'Proof: ORDERED_WILSON_INDEPENDENT_REVIEW.md · UR7–UR13; propagated in ORDERED_WILSON_ACTION.md.',fontsize=11,color='#496379')
ax.text(.4,.3,'Source comparison: Chatterjee, arXiv:1602.01222v6, Section 16. Ordered factors, original norms and signs retained.',fontsize=11,color='#496379')
fig.savefig(W/'ORDERED_WILSON_REVIEW.png',dpi=180,bbox_inches='tight');fig.savefig(W/'ORDERED_WILSON_REVIEW.svg',bbox_inches='tight');plt.close(fig)
