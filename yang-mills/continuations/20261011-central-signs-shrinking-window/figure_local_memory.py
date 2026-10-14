from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent;rows=json.loads((O/'LOCAL_MEMORY_CHECKS.json').read_text())['evaluated_original_bounds']
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
def save(fig,name):
    fig.savefig(O/(name+'.png'),dpi=160,bbox_inches='tight');fig.savefig(O/(name+'.svg'),bbox_inches='tight');plt.close(fig)
fig=plt.figure(figsize=(10.5,13.5));fig.suptitle('Actual conditional measures and the retained crossing force\nFour crossing links, seven patch links, all spectators retained [LPF1–LPF6]',y=.985,fontsize=16)
ax=fig.add_axes([0,0,1,1]);ax.axis('off')
def box(y,h,title,lines,color='#edf3f7'):
    ax.add_patch(FancyBboxPatch((.075,y),.85,h,boxstyle='round,pad=.008',ec='#91aab8',fc=color))
    ax.text(.10,y+h-.022,title,weight='bold',fontsize=12,va='top',color='#285269')
    for yy,line in zip(np.linspace(y+h-.064,y+.024,len(lines)),lines):ax.text(.5,yy,line,ha='center',va='center',fontsize=13)
box(.77,.15,'Actual ground and exact four-link change of measure [LPF1–LPF2]',[r'$d\mu=\psi^2dU,\quad\rho_{C^c}=\int_C\psi^2dU_C,\quad d\nu=\rho_{C^c}dU$',r'$h=d\nu/d\mu=\rho_{C^c}/\psi^2,\qquad h\leq e^{32\pi^2c}$','C contains the crossing face: one patch edge and three outside edges.'])
box(.55,.18,'Every derivative of the actual marginal remains [LPF3]',[r'$z=\log\rho_{C^c},\quad q=u+v,\quad R=w-q,\quad -b/\kappa_* =\int R\mathcal{B}\,d\nu$',r'$\mathcal{B}=-3T-\langle dT,d(w+q)\rangle$',r'$\qquad+T[\Delta z+|dz|^2-\langle dz,d(w+q)\rangle-\Delta(w+q)]$'])
box(.36,.15,'Actual ground norm and outside marginal [LPF4–LPF5]',[r'$\|R\|_{L^2(\mu)}\geq R_C=b e^{-16\pi^2c}/(\kappa_*Q_C^+)$',r'$\|\varepsilon_P\|_{L^2(\mu_{P^c})}\geq e_C$',r'$\delta_C=\min\{\pi/4,R_C/(8C_4A_4)\},\quad e_C=R_C/[4C_4\log\cot(\delta_C/2)]$'])
box(.13,.19,'Seven original link balls give the full residual floor [LPF6]',[r'$d\mu_{P\mid P^c}/dU_P\geq e^{-56\pi^2c},\qquad v_2(t)=(t-\sin t)/(2\pi)$',r'$B_P=e^{-56\pi^2c}/[4(48\pi)^7(2J_*\sqrt{7})^{21}]$',r'$\|\mathcal{K}x\|^2=\|\mathcal{K}y\|^2\geq m_C=2\kappa_*^2B_Pe_C^{23}$'])
for y in [.75,.53,.34]:ax.annotate('',(.5,y-.01),(.5,y+.01),arrowprops=dict(arrowstyle='->',lw=1.8,color='#58788b'))
fig.text(.5,.055,'The exponent 23 retains two powers from the squared score and 21 from seven 3D links.\nThe original centered observable keeps a²/4. Complete constants and domains: LPF1–LPF7.',ha='center',fontsize=10)
save(fig,'LOCAL_CONDITIONAL_FORCE_AND_MEMORY')

fig=plt.figure(figsize=(10.5,12.5));fig.suptitle('The evaluated bound and its exact original-path asymptotics\nThese curves describe lower-bound formulas, not measured spectral masses',y=.985,fontsize=16)
ax=fig.add_axes([.13,.59,.78,.28]);x=[r['j'] for r in rows[:3]]
ax.semilogy(x,[-float(r['previous_log10_floor']) for r in rows[:3]],'o-',color='#a85b3f',label='QLR9: complete original global bound')
ax.semilogy(x,[-float(r['log10_m_C']) for r in rows[:3]],'o-',color='#256c8b',label='LPF6: actual local conditional bound')
ax.set_xticks(x);ax.set_xlabel('original regulator index j');ax.set_ylabel('−log₁₀ of the proved mass floor');ax.grid(alpha=.25,which='both');ax.legend(fontsize=10,loc='upper left')
fig.text(.5,.525,'κ* = 4/5; aⱼ = 1/(100j), Lⱼ = j⁴, bⱼ = 1/(κ*aⱼ²).\nPoints evaluate the full formulas at 180 decimal digits; segments connect those samples only.',ha='center',fontsize=11)
ax=fig.add_axes([.13,.27,.78,.16]);ax.semilogx([r['j'] for r in rows],[float(r['log_asymptotic_quotient']) for r in rows],'o-',color='#256c8b');ax.axhline(0,color='#777',lw=1)
ax.set_xticks([1,2,3,10,100],[1,2,3,10,100]);ax.set_xlabel('original regulator index j');ax.set_ylabel('logarithm of the\nexact comparison ratio');ax.grid(alpha=.25)
fig.text(.5,.20,r'$\log\!\left[m_C j^{869}e^{84800\pi^2j/\kappa_*}/A_{\kappa_*}\right]\ \longrightarrow\ 0$',ha='center',fontsize=15)
fig.text(.5,.13,r'$A_{\kappa_*}=\dfrac{\kappa_*^2}{2(48\pi)^7(2\sqrt{7}A_J/\kappa_*^2)^{21}}\left[\dfrac{10000}{4C_4d_0A_Q}\right]^{23}$',ha='center',fontsize=13)
fig.text(.5,.055,'A_Q = 207360000 + 1105920000π²;  A_J = 1920000 + 15360000π².\nd₀ = 3200π²/κ*; C₄ = 532082. All boundary terms remain in the finite-j formulas [LPF7].',ha='center',fontsize=10)
save(fig,'LOCAL_MEMORY_ORIGINAL_PATH_BOUNDS')
