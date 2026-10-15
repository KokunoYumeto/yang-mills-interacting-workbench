from pathlib import Path
import json,math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
O=Path(__file__).resolve().parent
rows=json.loads((O/'INVERSE_UNITARY_CHECKS.json').read_text(encoding='utf8'))['path']
fig=plt.figure(figsize=(13,13));ax=fig.add_axes([0,0,1,1]);ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
blue='#24495e';light='#eef5fa';orange='#b26123'
ax.text(.5,.965,'Exact marginal unitary and the entire residual',ha='center',fontsize=22,color=blue)
ax.text(.5,.937,'CIT14–CIT20 • original fields, density, source, and complementary state retained',ha='center',fontsize=11)
for x in [.06,.54]:ax.add_patch(Rectangle((x,.765),.40,.13,facecolor=light,edgecolor=blue,lw=.9))
ax.text(.26,.869,r'$t\in L^2(\rho\,dx)$',ha='center',fontsize=19)
ax.text(.26,.829,r'$\mathcal{B}_\zeta t=F$',ha='center',fontsize=19)
ax.text(.26,.792,r'$\rho(x)=\int\psi(x,y)^2\,dy$',ha='center',fontsize=16)
ax.text(.74,.869,r'$v=\alpha t\in L^2(dx),\quad\alpha=\sqrt{\rho}$',ha='center',fontsize=17)
ax.text(.74,.829,r'$(\alpha\mathcal{B}_\zeta\alpha^{-1})v=\alpha F$',ha='center',fontsize=17)
ax.text(.74,.792,r'$\|v\|_{L^2(dx)}=\|t\|_{L^2(\rho\,dx)}$',ha='center',fontsize=16)
ax.annotate('',xy=(.54,.85),xytext=(.46,.85),arrowprops=dict(arrowstyle='->',color=blue))
ax.annotate('',xy=(.46,.805),xytext=(.54,.805),arrowprops=dict(arrowstyle='->',color=blue))
ax.text(.5,.75,r'Inverse: $t=\alpha^{-1}v$; every derivative of $\alpha^{-1}$ through order six is retained.',ha='center',fontsize=12)
ax.text(.5,.706,r'$\alpha X_J(\alpha^{-1}v)=\sum_{S\subseteq\{1,\ldots,m\}}(\alpha X_{J_S}\alpha^{-1})X_{J_{S^c}}v$',ha='center',fontsize=19)
ax.text(.5,.669,'Subwords preserve their original order; the link fields need not commute.  CIT15–CIT17',ha='center',fontsize=11)
ax.add_patch(Rectangle((.06,.565),.88,.085,facecolor=light,edgecolor=blue,lw=.9))
ax.text(.5,.624,r'$q_\zeta(\mathcal{L})Jt=JF+\mathcal{W}_\zeta t,\qquad J^*\mathcal{W}_\zeta t=0$',ha='center',fontsize=17)
ax.text(.5,.585,r'$\|\mathcal{W}_\zeta\mathcal{B}_\zeta^{-1}F\|_\mu\leq\mathfrak{P}_\zeta\|F\|_\rho$',ha='center',fontsize=18)
ax.text(.5,.517,r'$\mathfrak{P}_\zeta=\sum_{m=1}^{5}w_m\sum_{r=0}^{m}\binom{m}{r}A_r^-\widetilde{\Theta}_{m-r}$',ha='center',fontsize=18)
ax.text(.5,.472,'All coefficients are evaluated in CIT1–CIT18; the entire complementary residual remains.  CIT19',ha='center',fontsize=11)
p=fig.add_axes([.12,.143,.78,.28])
xx=[math.log10(float(r['j'])) for r in rows];yy=[float(r['log10_beta']) for r in rows]
lead=float(rows[0]['log10_leading_coefficient'])
p.plot(xx,yy,'o-',color=blue,label='Complete finite upper function (CIT19)')
p.plot(xx,[lead+60*x for x in xx],'--',color=orange,label='Leading asymptotic term (CIT20)')
p.set_xlabel(r'$\log_{10}j$');p.set_ylabel(r'$\log_{10}$ of upper function');p.grid(alpha=.25);p.legend(loc='upper left',fontsize=10)
ax.text(.5,.439,r'$q=100j,\ v_d=j^4-50j,\ \kappa_*=4/5,\ \theta=1,\ \varepsilon=1/4,\ R_{\rm win}=4$',ha='center',fontsize=11)
ax.text(.5,.092,'At j = 4, the complete bound is about 38 orders of magnitude above its leading term.',ha='center',fontsize=11)
ax.text(.5,.062,'These are bounds, not measured residuals. They do not prove spectral survival or gaplessness.',ha='center',fontsize=12,color=blue)
for ext in ['png','svg']:fig.savefig(O/('EXACT_MARGINAL_UNITARY_AND_RESIDUAL.'+ext),dpi=150,facecolor='white')
