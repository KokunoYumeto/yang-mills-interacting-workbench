from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
O=Path(__file__).resolve().parent
blue='#24495e';light='#eef5fa';orange='#b26123'
fig=plt.figure(figsize=(14,13));ax=fig.add_axes([0,0,1,1]);ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(.5,.965,'Original contractions and actual marginal geometry',ha='center',fontsize=22,color=blue)
ax.text(.5,.936,'CCJ3–CCJ14 • original radius-two SU(2) fields • every outside contribution retained',ha='center',fontsize=11)
ax.add_patch(Rectangle((.055,.79),.89,.11,facecolor=light,edgecolor=blue,lw=.8))
ax.text(.5,.867,r'$\tau=\Delta w=(V-E_0)/\kappa_*-|dw|^2,\quad B_w=\nabla^2w+cg\geq0$',ha='center',fontsize=17)
ax.text(.5,.831,r'$\|\nabla^2w\|_{\rm HS}^2\leq A^2+2(d_{\rm all}-1)cA+d_{\rm all}(d_{\rm all}-1)c^2$',ha='center',fontsize=17)
ax.text(.5,.764,'The original trace controls the full Hessian array; its bound grows as j¹⁴.  CCJ3',ha='center',fontsize=12)
ax.text(.5,.708,r'$\Delta^r(fg)=\sum_{a+b+c=r}\frac{r!\,2^c}{a!b!c!}\sum_K(D_K\Delta^af)(D_K\Delta^bg)$',ha='center',fontsize=21)
ax.text(.5,.659,'Every shared index remains contracted. Each word K keeps its original noncommuting order.  CCJ5',ha='center',fontsize=11.5)
ax.add_patch(Rectangle((.055,.49),.89,.12,facecolor=light,edgecolor=blue,lw=.8))
ax.text(.5,.578,r'$\rho(x)=\int\psi(x,y)^2dy,\quad\alpha=\sqrt{\rho},\quad M_\alpha:t\mapsto\alpha t$',ha='center',fontsize=17)
ax.text(.5,.539,r'$\rho^{-1}\Delta_Q\rho=2\mathbb{E}_\mu[(V-E_0)/\kappa_*+|dw|^2\mid x]$',ha='center',fontsize=17)
ax.text(.5,.466,'The full score includes outside derivatives; the outside Haar Laplacian integrates to zero.  CCJ8',ha='center',fontsize=11.5)
ax.text(.5,.414,r'$\widetilde{\mathcal{B}}_\zeta=M_\alpha\mathcal{B}_\zeta M_\alpha^{-1}$',ha='center',fontsize=20)
rows=[(.361,'Order six',r'$-\kappa_*^3\Delta_Q^3$'),(.305,'Order five',r'$6\kappa_*^3b_iX_i\Delta_Q^2-6\kappa_*^3b_iX_i\Delta_Q^2=0$'),(.246,'Order four',r'$(e_1\kappa_*^2+3\kappa_*^2\mathscr{U}_\rho)\Delta_Q^2+12\kappa_*^3\Sigma_{ji}X_jX_i\Delta_Q$')]
for y,label,formula in rows:
    ax.text(.075,y,label,fontsize=14,weight='bold');ax.text(.255,y,formula,fontsize=16)
ax.text(.5,.2,'Every term of orders zero through three is given by the complete finite sum in CCJ10–CCJ13.',ha='center',fontsize=11)
ax.text(.5,.151,r'$b_i=\mathbb{E}_\mu[X_iw\mid x],\quad\chi=\psi/\alpha,\quad\Sigma_{ji}=\int(X_j\chi)(X_i\chi)dy$',ha='center',fontsize=16)
ax.text(.5,.108,r'$\mathscr{U}_\rho=\kappa_*\Delta_Q\alpha/\alpha=bW_Q+R_Q+\kappa_*T_Q-(E_0-E_{\rm out})$',ha='center',fontsize=16)
ax.text(.5,.065,'The fourth-order covariance and potential belong to the actual conditional state.  CCJ13–CCJ14',ha='center',fontsize=11.5,color=blue)
for ext in ['png','svg']:fig.savefig(O/('CONTRACTED_LAPLACIAN_AND_MARGINAL_CUBIC.'+ext),dpi=150,facecolor='white')

new=json.loads((O/'CONTRACTED_CUBIC_CHECKS.json').read_text(encoding='utf8'))['path']
oldpath=O.parent/'cubic_differential_owner_20261015/INVERSE_UNITARY_CHECKS.json'
if not oldpath.exists():oldpath=O/'INVERSE_UNITARY_CHECKS.json'
old=json.loads(oldpath.read_text(encoding='utf8'))['path']
old={r['j']:r for r in old};xx=[math.log10(float(r['j'])) for r in new]
fig=plt.figure(figsize=(13,11));ax=fig.add_axes([0,0,1,1]);ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
ax.text(.5,.96,'Complete residual bounds on the original parameter path',ha='center',fontsize=20,color=blue)
ax.text(.5,.918,r'$a=(100j)^{-1},\ L=j^4,\ q=100j,\ v_d=j^4-50j,\ \zeta=\theta\kappa_*/j$',ha='center',fontsize=16)
ax.text(.5,.883,r'$\kappa_*=4/5,\quad\theta=1,\quad\varepsilon=1/4,\quad R_{\rm win}=4$',ha='center',fontsize=14)
ax.text(.5,.83,r'$\|\mathcal{W}_\zeta\mathcal{B}_\zeta^{-1}F\|_\mu\leq\widehat{\mathfrak{P}}_\zeta\|F\|_\rho$',ha='center',fontsize=21)
p=fig.add_axes([.12,.32,.78,.44])
p.plot(xx,[float(old[r['j']]['log10_beta']) for r in new],'s-',color=orange,label='Complete CIT19 bound; asymptotic power 60')
p.plot(xx,[float(r['log10_beta']) for r in new],'o-',color=blue,label='Complete CCJ17 bound; asymptotic power 45')
p.set_xlabel(r'$\log_{10}j$');p.set_ylabel(r'$\log_{10}$ of explicit upper function');p.grid(alpha=.25);p.legend(loc='upper left',fontsize=10)
ax.text(.5,.25,'At j = 4: log₁₀ of the previous bound is 132.0418; the contracted bound is 56.3301.',ha='center',fontsize=12)
ax.text(.5,.209,'Every point uses the complete finite formula. No finite contribution is replaced by a leading term.',ha='center',fontsize=11)
ax.text(.5,.151,r'$R\leq\widehat{\mathfrak{P}}_\zeta^{\,2}S,\qquad E\leq\frac{\widehat{\mathfrak{P}}_\zeta^{\,2}}{1+\widehat{\mathfrak{P}}_\zeta^{\,2}}S$',ha='center',fontsize=20)
ax.text(.5,.096,'Both curves are upper bounds, not actual residuals. Their growth does not prove residual divergence.',ha='center',fontsize=11)
ax.text(.5,.061,'The guaranteed captured fraction still tends to zero. Spectral survival and the no-gap goal remain open.',ha='center',fontsize=11.5,color=blue)
for ext in ['png','svg']:fig.savefig(O/('ORIGINAL_PATH_CONTRACTED_BOUND.'+ext),dpi=150,facecolor='white')
