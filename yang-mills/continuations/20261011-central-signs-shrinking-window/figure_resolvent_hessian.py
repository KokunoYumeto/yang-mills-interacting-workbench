from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent
fig,ax=plt.subplots(figsize=(12,7.3),facecolor='#f7f9fc')
ax.set_facecolor('white');lam=np.geomspace(1e-3,1e18,2000)
for j,color in [(1,'#345ca8'),(2,'#a45c26'),(3,'#6a3990')]:
 k=1.;a=1/(100*j);L=j**4;N=3*(2*L)*(2*L+1)**2;M=3*(2*L)**2*(2*L+1);b=1/(k*a*a);c=2/(k*a)
 G=4*np.pi**2*N*c*c;C=4*b*M/k+G+(3*N-1)*c;alpha=k*(2*C-.5);z=k/j
 value=(lam*lam+alpha*lam)/(lam+z)**2;peak=alpha*z/(alpha-2*z);cap=alpha*alpha/(4*z*(alpha-z))
 ax.loglog(lam,value,color=color,lw=2.2,label=f'j={j}, z=1/{j}, maximum ≈ {cap:.8g}')
 ax.scatter([peak],[cap],color=color,zorder=5)
ax.axhline(1,color='#66727f',ls=':',lw=1)
ax.set_xlabel(r'Original spectral variable $\lambda$ (no rescaling)',fontsize=13)
ax.set_ylabel(r'$(\lambda^2+\alpha_j^+\lambda)/(\lambda+z)^2$',fontsize=14)
ax.set_title('The Hessian multiplier in the original metric has an evaluated upper bound',fontsize=14,pad=16)
ax.legend(loc='upper right',fontsize=10,framealpha=.95);ax.grid(alpha=.15,which='major')
fig.text(.08,.045,r'Original path: $\kappa_*=1$, $a_j=(100j)^{-1}$, $L_j=j^4$, $z=s_j=1/j$. All $N_j,M_j,c_j,G_j,C_j^+$ factors retained.',fontsize=10)
fig.text(.08,.015,r'RHB3–RHB5. Dots are exact scalar maximizers. These are upper-bound functions, not sampled vacuum spectra; the value at $\lambda=0$ is exactly zero.',fontsize=9)
fig.tight_layout(rect=[0,.075,1,1])
for ext in ['png','svg']:fig.savefig(O/('RESOLVENT_HESSIAN_MULTIPLIER.'+ext),dpi=180)
plt.close(fig)

fig=plt.figure(figsize=(14,10),facecolor='#f7f9fc')
ax=fig.add_axes([0,0,1,1]);ax.set_axis_off()
def tx(x,y,s,size=17,bold=False):
 ax.text(x,y,s,fontsize=size,color='#182b40',weight='bold' if bold else None,va='top',transform=ax.transAxes)
def box(x,y,w,h,color):
 ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',facecolor=color,edgecolor='#71859d',transform=ax.transAxes))
tx(.04,.966,'An explicit original-state residual mass and resolvent gain',22,True)
tx(.04,.918,r'Original metric, source samples and all $2^{N_j}$ conditional components remain.  $\Phi_2=\sum_p|\varphi(x_p)|^2>0$.',14)
box(.04,.63,.43,.23,'#e5f0f0');box(.52,.63,.44,.23,'#eee9f7')
tx(.06,.836,'Global state and actual resolvent',17,True)
tx(.06,.789,r'$\psi^2,A^2\geq e^{-\Omega_j},\quad p_\tau\geq e^{-\Omega_j}/2^{N_j}$',17)
tx(.06,.738,r'$\Omega_j=8\pi^2c_jN_j,\quad \Vert df_z^0\Vert_\infty\leq\mathcal{L}_{j,z}$',17)
tx(.06,.684,'RHB9–RHB10 evaluate every constant.',13)
tx(.54,.836,'Retained central configuration',17,True)
tx(.54,.789,r'$dh(\mathbf{I})=0,\quad \Vert y(\mathbf{I})\Vert\geq v_j$',18)
tx(.54,.738,r'$v_j=a_je^{-\Omega_j/2}\sqrt{\Phi_2}$',18)
tx(.54,.684,r'$\Vert Bf_z^0(U)\Vert\leq2\kappa_*\widehat{H}_j\mathcal{L}_{j,z}\,d(U,\mathbf{I})$',14)
box(.04,.345,.92,.23,'#ffffff')
tx(.06,.552,'Original radius-two product balls give the full residual mass',17,True)
tx(.06,.504,r'$\rho_{j,z}=\min\left\{1,\frac{v_j}{2\sqrt{N_j}(L_j^y+2\kappa_*\widehat{H}_j\mathcal{L}_{j,z})}\right\}$',20)
tx(.06,.419,r'$m_z=\Vert y-Bf_z^0\Vert^2\geq m^-_{j,z}=\frac{a_j^2\Phi_2 e^{-2\Omega_j}}{4}\left(\frac{\rho_{j,z}-\sin\rho_{j,z}}{2\pi}\right)^{N_j}>0$',20)
box(.04,.105,.92,.18,'#edf2e6')
tx(.06,.262,'The full physical residual energy is bounded in RHB12',17,True)
tx(.06,.213,r'$e_z=q(\eta_z,\eta_z)\leq\mathcal{E}_{j,z}^+,\qquad \mathcal{G}_{X_\varphi}(z)-\langle x,(L_A+z)^{-1}x\rangle\geq\frac{(m^-_{j,z})^2}{\mathcal{E}_{j,z}^++z\,m^-_{j,z}}>0$',18)
tx(.04,.069,'Proof: RHB9–RHB13. The entire density exponential and N-fold Haar volume are retained.',12)
tx(.04,.037,'Each finite-regulator gain is explicit. The differentiated three-shift response and limiting annular mass remain to be evaluated.',12)
for ext in ['png','svg']:fig.savefig(O/('EXPLICIT_ORIGINAL_RESIDUAL_GAIN.'+ext),dpi=180,facecolor=fig.get_facecolor())
plt.close(fig)
