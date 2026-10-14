from pathlib import Path
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

O=Path(__file__).resolve().parent
plt.rcParams.update({'font.size':12,'text.color':'#18354a','axes.labelcolor':'#18354a'})
fig=plt.figure(figsize=(14,7.6),facecolor='#f8fafb')
fig.text(.045,.93,'The actual vacuum retains its central characters',fontsize=22,weight='bold')
fig.text(.045,.82,r'Original state: $\rho=\psi^2>0,\quad \int\rho\,dU=1$',fontsize=19)
fig.text(.045,.70,r'$\rho_{S_A}=\Pi_{S_A}\rho$',fontsize=22,color='#6c4f9c')
fig.text(.49,.70,r'$\sigma_A\rho_{\varnothing}=\Pi_{S_A}(\sigma_A\rho)$',fontsize=22,color='#137d78')
fig.text(.045,.56,r'$\|\rho_{S_A}-\sigma_A\rho_{\varnothing}\|_1=2\mu(\mathcal{T}_A<0)\leq\sum_{p\in A}\mu D_p$',fontsize=23)
fig.text(.045,.44,r'$\mathcal{T}_A=\prod_{p\in A}\operatorname{Tr}U_p,\quad \sigma_A=\operatorname{sgn}\mathcal{T}_A,\quad S_A=\bigtriangleup_{p\in A}\partial p$',fontsize=18)
fig.text(.045,.31,r'$[1-\frac{1}{2}\sum_{p\in A}\mu D_p]_+\leq\|\rho_{S_A}\|_1\leq1$',fontsize=23)
fig.text(.045,.20,'Small actual deficits control the alignment error; the character density can remain large.',fontsize=14,weight='bold')
fig.text(.045,.12,'The full central average is retained. It is generally nonconstant and is not replaced by Haar probability.',fontsize=13)
fig.text(.045,.045,'Exact map and inequalities, not a sampled vacuum. Proof: DCH3, DCH6–DCH9; local averages: DCH13–DCH14.',fontsize=11)
for ext in ['png','svg']:fig.savefig(O/('DENSITY_CHARACTER_MAP.'+ext),dpi=170,bbox_inches='tight')
plt.close(fig)

j=np.arange(1,41,dtype=float)
kappa=1.;Rwin=1.;delta=.25
a=1/(100*j);L=j**4
N=3*(2*L)*(2*L+1)**2;M=3*(2*L)**2*(2*L+1)
b=1/(kappa*a*a);s=100*kappa*a;C=4*b*M
Lam=np.minimum(2*M,3*kappa*a*np.sqrt(N*M))
m2bound=Lam*Lam+4*kappa*kappa*a*a
low=4*b*b*m2bound/(C-Rwin*s)**2
outside=m2bound/(4*delta*delta*M*M)
fig,axes=plt.subplots(1,2,figsize=(14,6),facecolor='#f8fafb')
fig.subplots_adjust(top=.79,bottom=.31,wspace=.28,left=.075,right=.97)
fig.suptitle('Central reversal: quantified escape to original high energy',fontsize=21,weight='bold',y=.96)
fig.text(.075,.86,r'Original path: $a_j=(100j)^{-1},\ L_j=j^4,\ b_j=(\kappa_*a_j^2)^{-1},\ s_j=100\kappa_*a_j$; here $\kappa_*=1$.',fontsize=13)
axes[0].loglog(j,low,label=r'Bound on $\nu_-([0,s_j])$',color='#137d78',lw=2.5)
axes[0].loglog(j,outside,label=r'Bound outside $[0.75C_j,1.25C_j]$',color='#6c4f9c',lw=2.5)
axes[0].set(xlabel='Original integer regulator j',ylabel='Upper bound on spectral probability')
axes[0].legend(fontsize=11,loc='upper right');axes[0].grid(alpha=.22,which='both')
axes[1].loglog(j,C,label=r'$C_j=4b_jM_j$',color='#bb5d20',lw=2.5)
axes[1].loglog(j,s,label=r'$s_j$',color='#137d78',lw=2.5)
axes[1].set(xlabel='Original integer regulator j',ylabel='Original Hamiltonian energy')
axes[1].legend(fontsize=12,loc='center right');axes[1].grid(alpha=.22,which='both')
fig.text(.075,.14,r'$\nu_-(B)=\|E_{H-E_0}(B)\psi^-\|^2,\quad \psi^-=\mathcal{U}\psi,\quad C_j=4b_jM_j$.  Every full-box boundary count is retained.',fontsize=13)
fig.text(.075,.075,'Curves are proved upper bounds and exact energy scales, not computed vacuum spectra. Proof: DCH17–DCH21.',fontsize=12)
fig.text(.075,.025,'Central multiplication: Li and Meurice, hep-lat/0410029v2, Sections II–IV and Appendix; exact programme map: CS6.',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/('CENTRAL_REVERSAL_SPECTRAL_BOUNDS.'+ext),dpi=170,bbox_inches='tight')
(O/'CENTRAL_REVERSAL_FIGURE_DATA.json').write_text(json.dumps(dict(kappa=kappa,Rwin=Rwin,delta=delta,rows=[dict(j=int(j[k]),a=float(a[k]),N=int(N[k]),M=int(M[k]),C=float(C[k]),s=float(s[k]),low_upper=float(low[k]),outside_upper=float(outside[k])) for k in range(len(j))]),indent=2)+'\n',encoding='utf8')
