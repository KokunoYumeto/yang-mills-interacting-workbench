"""Exact schematic of BR16, BR21 and BR24-BR27; no numerical vacuum sampling."""
from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

root = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(12.6,7.5),dpi=160)
fig.patch.set_facecolor('#f6f8fc')
ax.set_facecolor('#f6f8fc')
ax.set_xlim(0,12.6)
ax.set_ylim(0,7.5)
ax.axis('off')

def box(x,y,w,h,text,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=0.12',linewidth=1.4,edgecolor=color,facecolor='white'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=12,color='#142238',linespacing=1.6)

ax.text(.4,7.05,'Original phase vector and its exact continuous projection',fontsize=18,weight='bold',color='#142238')
ax.text(.4,6.63,r'$A_j=H_j-E_{0,j},\quad \zeta=[e^{i\theta_j C_j}\psi_j],\quad \|\zeta\|=1$',fontsize=14,color='#142238')
box(.5,3.05,3.55,2.15,r'$\mathcal{H}_{\mathcal{U}}$'+'\n'+r'$\zeta=U_{\boldsymbol{\theta}}\Omega$'+'\n'+'All original gauge constraints', '#556b92')
box(6.35,4.0,5.45,1.65,r'$\mathcal{H}_c=P\mathcal{H}_{\mathcal{U}}$'+'\n'+r'$P\zeta=V_{\boldsymbol{\theta}}\Omega$'+'\n'+r'$P=\mathrm{s}\!-\!\lim_{M\to\infty}[\mathbf{1}_{[0,M]}(A_j)]$', '#156a81')
box(6.35,1.6,5.45,1.65,r'$\mathcal{H}_d=(I-P)\mathcal{H}_{\mathcal{U}}$'+'\n'+r'$(I-P)\zeta=K_{\boldsymbol{\theta}}\Omega$'+'\n'+r'$E_M\mathcal{H}_d=0,\quad T(t)\mathcal{H}_d=0\ (t>0)$', '#8c3a65')
for end,label,pos in [((6.18,4.78),r'$P$',(5.07,4.78)),((6.18,2.42),r'$I-P$',(5.12,2.9))]:
    ax.add_patch(FancyArrowPatch((4.2,4.07),end,arrowstyle='-|>',mutation_scale=18,linewidth=1.5,color='#34465d'))
    ax.text(*pos,label,fontsize=14,ha='center',color='#34465d')
ax.text(.55,2.17,r'$a_j\theta_j^2\to\ell\in(0,\infty]$',fontsize=15,color='#142238')
ax.text(.55,1.57,r'$Z_f(\ell)=(H_f+4e_f)/\ell+\kappa_*^2\mathcal{R}_f$',fontsize=12.5,color='#142238')
ax.text(.55,.77,r'$\|(I-P)\zeta\|^2=\lim_{M\to\infty}\lim_{\mathcal{U}}\|\mathbf{1}_{(M,\infty)}(A_j)e^{i\theta_jC_j}\psi_j\|^2\ \geq\ e_f^2/Z_f(\ell)>0$',fontsize=13,color='#8c3a65')
ax.text(.55,.24,'Exact operator schematic. Proofs: BR16, BR21, BR24–BR27. No vacuum density or spectrum is simulated.',fontsize=10,color='#34465d')
fig.subplots_adjust(left=0,right=1,bottom=0,top=1)
for ext in ['png','svg']:
    fig.savefig(root/f'projection_receiver.{ext}',facecolor=fig.get_facecolor())
print('projection_receiver.png and projection_receiver.svg written')
