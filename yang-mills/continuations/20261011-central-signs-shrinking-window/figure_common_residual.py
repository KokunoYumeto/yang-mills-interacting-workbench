from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent;data=json.loads((O/'COMMON_RESIDUAL_CHECKS.json').read_text());beta=float(data['constants']['beta']);km=float(data['constants']['kminus']);kp=113/2500
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,'svg.fonttype':'none'})
def save(fig,name):
    fig.savefig(O/(name+'.png'),dpi=160,bbox_inches='tight');fig.savefig(O/(name+'.svg'),bbox_inches='tight');plt.close(fig)
fig=plt.figure(figsize=(11,14));fig.suptitle('The complete signed filter and its common-equation residual\nExact constants, all original factors and the full state [SCR1–SCR6]',y=.98,fontsize=16)
ax=fig.add_axes([.12,.67,.8,.23]);lam=np.geomspace(.01,100,1800);kernel=lam/(lam+1)**2-(16/25)*(.25*lam/(lam+.25)**2+4*lam/(lam+4)**2)
ax.plot(lam,kernel,color='#285269',lw=2);ax.axhline(kp,color='#4e8b59',ls='--',label='k₊ = 113/2500');ax.axhline(-km,color='#a85b3f',ls='--',label='−k₋ = F(β) ≈ −0.06326515')
mins=[(beta-np.sqrt(beta*beta-4))/2,(beta+np.sqrt(beta*beta-4))/2];ax.scatter(mins,[-km,-km],color='#a85b3f');ax.scatter([1],[kp],color='#4e8b59');ax.set_xscale('log');ax.set_xlabel('original spectral energy λ (ζ fixed at 1)');ax.set_ylabel('original three-shift kernel');ax.grid(alpha=.2);ax.legend(fontsize=10,loc='lower center',bbox_to_anchor=(.5,1.0),ncol=2)
fig.text(.5,.61,'β is the unique root in (9,10) of 2752β³ − 13296β² − 110508β − 164041 = 0.\nThe curve is the scalar filter, not the actual spectral density.',ha='center',fontsize=10)
fig.text(.5,.54,r'$q_\zeta(t)=(t+\zeta)(t+\zeta/4)(t+4\zeta)$',ha='center',fontsize=15)
fig.text(.5,.49,r'$Y_u=q_\zeta(\mathcal{L})u,\quad e=X-Y_u,\quad \mathcal{T}(u)=\langle Y_u,k_\zeta(\mathcal{L})Y_u\rangle$',ha='center',fontsize=13)
fig.text(.5,.43,r'$|\mathcal{C}_X-\mathcal{T}(u)|\leq k_-\,\|e\|(2\|X\|+\|e\|)$',ha='center',fontsize=16)
fig.text(.5,.385,'No explicit inverse-shift factor; the full equation residual is retained.',ha='center',fontsize=11)
fig.text(.5,.33,r'$u=Jt,\quad q_\zeta(\mathcal{A})t=F,\quad e=-Jv_\zeta-w_\zeta,\quad\mathcal{V}=\mathcal{K}^*\mathcal{K}$',ha='center',fontsize=13)
fig.text(.5,.28,r'$v_\zeta=(\mathcal{A}\mathcal{V}+\mathcal{V}\mathcal{A}+\mathcal{K}^*\mathcal{D}\mathcal{K}+e_1\mathcal{V})t$',ha='center',fontsize=14)
fig.text(.5,.23,r'$w_\zeta=(\mathcal{K}\mathcal{A}^2+\mathcal{D}\mathcal{K}\mathcal{A}+\mathcal{K}\mathcal{V}+\mathcal{D}^2\mathcal{K}$',ha='center',fontsize=14)
fig.text(.5,.19,r'$\qquad+e_1(\mathcal{K}\mathcal{A}+\mathcal{D}\mathcal{K})+e_2\mathcal{K})t$',ha='center',fontsize=14)
fig.text(.5,.135,r'$e_1=21\zeta/4,\quad e_2=21\zeta^2/4,\quad e_3=\zeta^3$',ha='center',fontsize=13)
fig.text(.5,.07,'The marginal, mixed and complementary terms are all actual full-state terms.\nThe original cubic constant e₃ remains in the equation for t.\nComplete domains, covariance derivatives and proof: SCR1–SCR6.',ha='center',fontsize=10)
save(fig,'COMMON_FILTER_AND_CUBIC_RESIDUAL')

fig=plt.figure(figsize=(11,14));fig.suptitle('The full spatial source, overlapping patches and optimal residual\nEvery original raw coefficient and cross-face entry retained [SCR7–SCR13]',y=.98,fontsize=16)
fig.text(.5,.91,r'$X=Z\varphi,\quad Y_p=q_\zeta(\mathcal{L})u_p=Z_p+R_p$',ha='center',fontsize=15)
fig.text(.5,.855,r'$\mathsf{S}=Z^*Z,\quad \mathsf{G}=Y^*Y,\quad\mathsf{H}=Y^*Z,\quad c=\mathsf{G}^{\dagger}\mathsf{H}\varphi$',ha='center',fontsize=15)
fig.text(.5,.80,r'$\mathsf{E}=\mathsf{S}-\mathsf{H}^*\mathsf{G}^{\dagger}\mathsf{H},\quad0\leq\mathsf{E}\leq\mathsf{S}$',ha='center',fontsize=15)
fig.text(.5,.745,r'$s_\varphi=\varphi^*\mathsf{S}\varphi,\quad r_\varphi^2=\varphi^*\mathsf{E}\varphi,\quad \alpha=(k_+-k_-)/2,\quad d=(k_++k_-)/2$',ha='center',fontsize=12)
fig.text(.5,.68,r'$|\mathcal{C}_X-c^*\mathsf{T}c-\alpha r_\varphi^2|\leq d\,r_\varphi\sqrt{4s_\varphi-3r_\varphi^2}$',ha='center',fontsize=17)
fig.text(.5,.635,'T is the full signed five-moment matrix. Zero eigenvalues of G are retained.\nThe formula does not assume that the actual residual is small.',ha='center',fontsize=10)
ax=fig.add_axes([.14,.35,.77,.21]);rows=data['original_spatial_bounds'];x=[r['j'] for r in rows];ax.loglog(x,[float(r['original_Z']) for r in rows],'o-',color='#a85b3f',label='earlier 2a Φ₁');ax.loglog(x,[float(r['improved_Z']) for r in rows],'o-',color='#285269',label='complete local bound Z_Q');ax.set_xticks(x,x);ax.set_xlabel('original regulator index j');ax.set_ylabel('evaluated source-norm bound');ax.grid(which='both',alpha=.2);ax.legend(fontsize=10)
fig.text(.5,.285,'κ* = 4/5; a = 1/(100j); q = 100j, with all 3q²(q+1) face samples equal to 1.\nThese are bounds for an original fitting cube, not sampled vacuum norms.',ha='center',fontsize=10)
fig.text(.5,.22,r'$Z_Q^2=\min\{a^2\Phi_1^2,\ a^2\Phi_2B_Q,\ a^2\Phi_\infty^2U_{2,Q}/4\}$',ha='center',fontsize=14)
fig.text(.5,.16,r'$a^2\Lambda_Q\longrightarrow 9\kappa_*\ell^3+24\ell^2,\qquad aZ_Q\leq \Phi_\infty a^2\sqrt{U_{2,Q}}/2$',ha='center',fontsize=13)
fig.text(.5,.085,'The term 24ℓ² comes from every original crossing face. Full finite counts and caps remain.\nActual conditional covariance and all cross-patch source terms determine G, H and T.\nComplete proofs and original limits: SCR7–SCR13.',ha='center',fontsize=10)
save(fig,'SPATIAL_COMMON_RESIDUAL_AND_SOURCE_BOUNDS')
