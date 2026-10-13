from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
O=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'mathtext.fontset':'dejavusans'})
fig,ax=plt.subplots(2,2,figsize=(16,11),layout='constrained')
fig.suptitle('Original force curl: spatial modes and their spectral receiver',fontsize=22,weight='bold')
blue='#24577d';red='#ac492d';green='#24684d';muted='#57616c'
for a in ax.flat:a.set_axis_off()
a=ax[0,0];a.set_xlim(-1.4,1.4);a.set_ylim(-1.2,1.4)
a.text(-1.32,1.25,'Original face and all six edge pairs',fontsize=16,weight='bold')
a.plot([-0.7,0.7,0.7,-0.7,-0.7],[-0.7,-0.7,0.7,0.7,-0.7],color=muted,lw=2)
pts=np.array([[0,-.7],[0,.7],[-.7,0],[.7,0]])
for i in range(4):
    for k in range(i+1,4):
        a.plot(pts[[i,k],0],pts[[i,k],1],color=green,ls='--',alpha=.5,lw=1)
a.scatter(pts[:,0],pts[:,1],s=95,c=[blue,blue,red,red],zorder=3)
a.scatter([0],[0],s=35,c='black');a.text(.04,.05,r'$x_p$',fontsize=14)
a.text(0,-.84,r'$x_p-\frac{a_j}{2}e_k$',ha='center')
a.text(0,.84,r'$x_p+\frac{a_j}{2}e_k$',ha='center')
a.text(-.78,0,r'$x_p-\frac{a_j}{2}e_d$',ha='right',va='center')
a.text(.78,0,r'$x_p+\frac{a_j}{2}e_d$',ha='left',va='center')
a.text(-1.32,-1.08,'Blue: direction d edges. Red: direction k edges.\nEvery dashed pair is retained. TFC12, TFC15.',fontsize=11)

a=ax[0,1];a.set_xlim(0,1);a.set_ylim(0,1)
a.text(.02,.95,'Two spatial contributions',fontsize=16,weight='bold')
a.text(.03,.80,r'$\mathcal{F}_\infty=\frac{3}{\kappa_*^2}(3I-\mathbf{1}\mathbf{1}^*)'
       r'=\frac{9}{\kappa_*^2}P_{\mathrm{diff}}$',fontsize=21,color=blue)
a.text(.03,.68,'Inside the original support cube; zero outside.',fontsize=11,color=muted)
a.text(.03,.55,r'$h_1+h_2+h_3=0:\quad 9/\kappa_*^2$',fontsize=19,color=blue)
a.text(.03,.42,r'$h=(\varphi,\varphi,\varphi):\quad \mathcal{F}_\infty h=0$',fontsize=18,color=green)
a.text(.03,.24,r'$a_j^{-2}\langle h,\mathcal{F}_j h\rangle'
       r'\ \longrightarrow\ \frac{3}{\kappa_*^2}\int_{\mathcal{Q}}|\nabla\varphi|^2$',fontsize=18,color=green)
a.text(.03,.08,'Actual interacting-state limits. Full deficit moments\ncontrol the comparison error. TFC12–TFC15.',fontsize=11)

a=ax[1,0];a.set_xlim(0,1);a.set_ylim(0,1)
a.text(.02,.95,'Exact differential and projection maps',fontsize=16,weight='bold')
a.text(.03,.80,r'$\alpha_c=a_j^2D_cdw\quad\longmapsto\quad\zeta_c=d\alpha_c$',fontsize=18,color=blue)
a.annotate('',(.45,.62),(.45,.74),arrowprops=dict(arrowstyle='->',lw=2,color=blue))
a.text(.03,.56,r'$L_2\zeta_c=-a_j^2\omega_c,\qquad\omega_c=d(D_cdV)$',fontsize=18,color=blue)
a.text(.03,.39,r'$\mathsf{N}^\perp=\kappa_*a_j^4'
       r'\int_{(0,\infty)}\lambda^{-3}\,d\Omega_j(\lambda)$',fontsize=19,color=green)
a.text(.03,.21,r'$\mathscr{R}\zeta_c=\mathscr{R} L_2\zeta_c=0$',fontsize=18)
a.text(.03,.08,'The next contraction retains the full score/force\nHessian commutator. TFC4–TFC10.',fontsize=11)

a=ax[1,1];a.set_xlim(0,1);a.set_ylim(0,1)
a.text(.02,.95,'The same spectrum in two original scales',fontsize=16,weight='bold')
a.text(.03,.80,r'$r=\lambda/s_j,\quad s_j=100\kappa_*a_j$',fontsize=17,color=red)
a.text(.03,.69,r'$\mathcal{F}_j\ \longrightarrow\ \mathcal{F}_\infty\delta_\infty$',fontsize=18,color=red)
a.text(.03,.53,r'$u=a_j\lambda:\quad'
       r'\widehat{\mathcal{F}}(\{0,\infty\})=0$',fontsize=18,color=blue)
a.text(.03,.36,r'$\widehat{\mathcal{M}}^{\perp}'
       r'=\widehat{\mathcal{M}}^{\perp}(\{0\})\delta_0'
       r'+\kappa_*u^{-3}\widehat{\mathcal{F}}$',fontsize=18,color=green)
a.text(.03,.18,'The zero atom of removed current norm stays explicit.\nThese identities do not assign the physical window sign.',fontsize=11)
a.text(.03,.07,'TFC11, TFC14, TFC16–TFC18.',fontsize=11,color=muted)
fig.text(.5,-.015,'Proof source: TWO_FORM_FORCE_AND_COMMON_SPECTRUM.md, TFC1–TFC18. '
         'Original SU(2) radius-two metric, full lattice and interacting ground state retained.',
         ha='center',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/('TWO_FORM_FORCE_RECEIVER.'+ext),dpi=170,bbox_inches='tight')
