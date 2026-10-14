from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent;data=json.loads((O/'QUANTITATIVE_LOOP_CHECKS.json').read_text())
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
M=np.array([[1,1,0,0,-1,1,0,1,-1],[-1,1,1,1,0,0,-1,0,0],[0,0,-1,1,1,1,1,1,1],[0,0,0,0,-2,2,0,0,0],[-2,2,0,0,0,0,2,0,0],[0,0,-2,2,0,0,0,2,-2],[-1,-1,0,0,-1,1,0,1,-1],[-1,1,-1,-1,0,0,-1,0,0],[0,0,-1,1,-1,-1,-1,1,1]])/2
def save(fig,name):
    fig.savefig(O/(name+'.png'),dpi=160,bbox_inches='tight');fig.savefig(O/(name+'.svg'),bbox_inches='tight');plt.close(fig)
fig=plt.figure(figsize=(10.5,13));fig.suptitle('Original loop endpoints: explicit control and the L² defect\nEvery coordinate and metric factor retained [QLR1–QLR4]',y=.98,fontsize=17)
ax=fig.add_axes([.20,.47,.61,.39]);ax.imshow(M,cmap='RdBu_r',vmin=-1,vmax=1)
for i in range(9):
    for k in range(9):ax.text(k,i,f'{M[i,k]:g}',ha='center',va='center',fontsize=10,color='white' if abs(M[i,k])==1 else '#15232b')
ax.set_xticks(range(9),['v₁','v₂','v₃','v₄','v₅','v₆','Ad(h)v₂','Ad(h)v₃','Ad(h)v₄'],rotation=50,ha='right')
ax.set_yticks(range(9),[f'P{i}, J{a}' for i in [1,2,3] for a in [1,2,3]])
ax.set_title('Exact 9 × 9 derivative of the original endpoint product',pad=18)
fig.text(.5,.405,r'$\det\mathsf{M}=-4,\quad\|\mathsf{M}\|_F^2=18,\quad\sigma_{\min}\geq1024/6561$',ha='center',fontsize=15)
fig.text(.5,.365,'Fifteen endpoint factors contain a metric ball; at most 266040 factors cover SU(2)³.\nEach factor uses A(K)⁻¹A(J), with A(J)ᵢ = exp(iπJ/4), i = 1, 2, 3.',ha='center',fontsize=11)
ax=fig.add_axes([.13,.15,.76,.14]);theta=np.linspace(0,np.pi,1200);delta=.18
def eta(t):
    if t<=1:return 0
    if t>=2:return 1
    return 1/(1+np.exp(np.clip(-1/(2-t)+1/(t-1),-700,700)))
zz=np.array([eta(t/delta)*eta((np.pi-t)/delta) for t in theta]);ax.plot(theta,zz,color='#276789',lw=2,label=r'$\zeta_\delta(\theta)$, δ = 0.18')
ax.fill_between(theta,0,zz,color='#d1e4ef');ax.axvspan(0,2*delta,color='#d8a58b',alpha=.25);ax.axvspan(np.pi-2*delta,np.pi,color='#d8a58b',alpha=.25)
ax.set_xticks([0,delta,2*delta,np.pi/2,np.pi-2*delta,np.pi-delta,np.pi],['0','δ','2δ','π/2','π−2δ','π−δ','π']);ax.set_ylim(-.05,1.15);ax.set_ylabel('cutoff value');ax.legend(loc='lower center');ax.grid(alpha=.2)
fig.text(.13,.315,'W = I',ha='left',fontsize=12);fig.text(.89,.315,'W = −I',ha='right',fontsize=12)
fig.text(.5,.080,r'$F_\delta=\zeta_\delta\,\mathrm{Tr}Q_1,\qquad\|F_\delta\|_2^2\to1,\qquad\|\mathcal{X}F_\delta\|_2^2\to0$',ha='center',fontsize=14)
fig.text(.5,.035,'The exact Haar factor is (2/π) sin²θ dθ; the four-link flow has θ̇ = −2 sinθ.\nThe cutoff diagnoses the unrestricted function class. Actual state bounds also use its derivatives.',ha='center',fontsize=10)
save(fig,'QUANTITATIVE_LOOP_ENDPOINTS')

fig=plt.figure(figsize=(10.5,14));fig.suptitle('From the original crossing face to a full memory floor\nActual ground-state bounds on every original regulator [QLR5–QLR10]',y=.985,fontsize=16)
ax=fig.add_axes([.10,.78,.32,.13]);xy=np.array([[0,0],[1,0],[1,1],[0,1]])
for i in range(4):
    p=xy[i];q=xy[(i+1)%4];ax.annotate('',q,p,arrowprops=dict(arrowstyle='->',lw=2.5,color='#276789' if i==0 else '#ad6641'))
ax.text(.5,-.20,'selected patch edge e',ha='center',color='#276789');ax.text(.5,1.12,'crossing xz face',ha='center');ax.text(.5,.50,'T = Tr Uₚ',ha='center');ax.set_xlim(-.2,1.2);ax.set_ylim(-.35,1.3);ax.axis('off')
fig.text(.65,.875,r'$\int VT\,dU=-b,\qquad\int T^2dU=1$',ha='center',fontsize=15)
fig.text(.65,.825,'One patch link and three outside links.\nBoth conditional Haar means of T vanish.\nThe entire original Wilson sum is retained.',ha='center',fontsize=11)
ax=fig.add_axes([0,0,1,1]);ax.axis('off')
def box(y,h,title,lines,color='#edf3f7'):
    ax.add_patch(FancyBboxPatch((.08,y),.84,h,boxstyle='round,pad=0.008',ec='#9ab0be',fc=color))
    ax.text(.105,y+h-.022,title,fontsize=12,weight='bold',va='top',color='#294e65')
    for yy,line in zip(np.linspace(y+h-.065,y+.025,len(lines)),lines):ax.text(.5,yy,line,fontsize=13,ha='center',va='center')
box(.625,.125,'Crossing coefficient and the actual conditional factor [QLR6–QLR7]',[r'$R=w-u-v,\qquad\|R\|_2\geq R_* = b/(\kappa_*Q^+)$',r'$Q^+=3+2(1+\sqrt{2})\sqrt{G}+B_w^++3NW^++42G$'])
box(.475,.125,'Finite endpoint control and original ground derivatives [QLR5, QLR8]',[r'$\delta_* = \min\{\pi/4,\ R_*/(16C_4\sqrt{G})\},\qquad C_4=532082$',r'$\|r_x\|_\infty=\|r_y\|_\infty\geq\varepsilon_* = R_*/[4C_4\log\cot(\delta_*/2)]$'])
box(.325,.125,'Original ground density and all N link-ball factors [QLR9]',[r'$m_* = \kappa_*^2\varepsilon_*^2e^{-4\pi\sqrt{NG}}\,[v_2(d_*/\sqrt{N})]^N$',r'$v_2(t)=(t-\sin t)/(2\pi),\qquad d_* = \min\{1,\varepsilon_*/(2J_*)\}$'])
box(.175,.125,'Entire complementary spectral measure [QLR10]',[r'$E_* = 4\kappa_*^3J_*^2,\qquad\langle\mathcal{K}x,e^{-t\mathcal{D}}\mathcal{K}x\rangle\geq m_*e^{-tE_*/m_*}$',r'$\langle\mathcal{K}x,(\mathcal{D}+\sigma)^{-1}\mathcal{K}x\rangle\geq m_*^2/(E_*+\sigma m_*)$'])
for y in [.61,.46,.31]:ax.annotate('',(.5,y-.007),(.5,y+.010),arrowprops=dict(arrowstyle='->',color='#627987',lw=1.5))
fig.text(.5,.115,'Evaluated lower-bound formula at κ* = 4/5 (not a computed ground spectrum):\nlog₁₀ m* ≈ −466826.28 at j = 1; −1.803456057 × 10⁹ at j = 2; −3.337453841 × 10¹¹ at j = 3.',ha='center',fontsize=10)
fig.text(.5,.055,'The centered physical observable retains the exact factor a²/4.\nAll constants are defined and proved in QLR5–QLR10. These floors do not control the signed shrinking window.',ha='center',fontsize=10)
save(fig,'ACTUAL_QUANTITATIVE_MEMORY_FLOOR')
