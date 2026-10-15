from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
O=Path(__file__).resolve().parent
fig=plt.figure(figsize=(14,14));ax=fig.add_axes([0,0,1,1]);ax.axis('off');ax.set_xlim(0,1);ax.set_ylim(0,1)
blue='#24495e';light='#eef5fa'
ax.text(.5,.97,'Full residual in the original link fields',ha='center',fontsize=21,color=blue)
ax.text(.5,.942,'CDE1–CDE8 • original radius-two SU(2) • all ordered terms retained',ha='center',fontsize=11)
ax.add_patch(Rectangle((.055,.825),.89,.09,facecolor=light,edgecolor=blue,lw=.8))
ax.text(.5,.887,r'$H=-\kappa_*\Delta+2bM-b\sum_p T_p,\quad H\psi=E_0\psi,\quad \mathcal{L}=\psi^{-1}(H-E_0)\psi$',ha='center',fontsize=15)
ax.text(.5,.852,r'$[\Delta,X_i]=0,\quad a_i=X_i\psi/\psi,\quad a_{ji}=X_jX_i\psi/\psi,\quad a_{kji}=X_kX_jX_i\psi/\psi$',ha='center',fontsize=14)
ax.text(.5,.796,'Ground equation reduces the complete cubic expansion to third ground derivatives.',ha='center',fontsize=12)
ax.text(.5,.768,r'$\Delta V_i=-3V_i,\quad V_i=X_i V,\quad V_{ji}=X_jX_iV,\quad \delta f=f-\mathbb{E}_\mu[f\mid x]$',ha='center',fontsize=14)
ax.text(.5,.744,r'$e_1=\zeta(1+\varepsilon+R_{\rm win}),\quad e_2=\zeta^2(\varepsilon+R_{\rm win}+\varepsilon R_{\rm win}),\quad\zeta=\theta\kappa_*/j$',ha='center',fontsize=11)
ax.text(.08,.725,'Original derivative of t(x)',fontsize=13,weight='bold')
ax.text(.34,.725,r'Coefficient in $\mathcal{W}_\zeta t=Q_cq_\zeta(\mathcal{L})Jt$',fontsize=13,weight='bold')
rows=[
(.675,r'$X_i\Delta_Q^2t$',r'$-6\kappa_*^3\,\delta a_i$'),
(.615,r'$X_jX_i\Delta_Qt$',r'$-12\kappa_*^3\,\delta a_{ji}$'),
(.555,r'$X_kX_jX_it$',r'$-8\kappa_*^3\,\delta a_{kji}$'),
(.495,r'$X_i\Delta_Qt$',r'$-6\kappa_*^2\,\delta V_i+4e_1\kappa_*^2\,\delta a_i$'),
(.425,r'$X_jX_it$',r'$-8\kappa_*^2\,\delta V_{ji}-4\kappa_*^2\,\delta(V_j a_i+2V_i a_j)$'),
(.399,'',r'$+\,4e_1\kappa_*^2\,\delta a_{ji}$'),
(.329,r'$X_it$',r'$6\kappa_*^2\,\delta V_i-4\kappa_*^2\,\delta(\sum_{j\in\mathcal{I}}a_jV_{ji})$'),
(.303,'',r'$+\,2e_1\kappa_*\,\delta V_i-2e_2\kappa_*\,\delta a_i$')]
for y,left,right in rows:
    ax.text(.08,y,left,fontsize=15)
    ax.text(.34,y,right,fontsize=15)
for y in [.704,.645,.585,.525,.465,.365,.282]:ax.plot([.07,.93],[y,y],color='#cddce6',lw=.7)
ax.text(.5,.255,'Unqualified indices run over original inside link/color pairs. The explicitly full j sum stays.',ha='center',fontsize=10.5)
ax.text(.5,.23,r'$V_{ji}=0$ outside the exact face neighborhood $Q^+$; the ground still depends on the full configuration.',ha='center',fontsize=10.5)
ax.add_patch(Rectangle((.055,.09),.89,.11,facecolor=light,edgecolor=blue,lw=.8))
ax.text(.5,.169,r'$I_3=\sum_{i,j,k}\|X_kX_jX_i\psi\|^2_{L^2(dU)}=\kappa_*^{-2}\,\mu|dV+(V-E_0)dw|^2$',ha='center',fontsize=14)
ax.text(.5,.134,r'$\sqrt{I_3}\leq\kappa_*^{-1}\,[4b\sqrt{M}+(4bM-E_0)\sqrt{E_0/\kappa_*}]$',ha='center',fontsize=14)
ax.text(.5,.064,'CDE8 applies these actual coefficient bounds to the full residual matrix, retaining every cross term.',ha='center',fontsize=11)
ax.text(.5,.041,r'CIT1–CIT20 derive an explicit polynomial bound for the matched inverse trial and its complete residual.',ha='center',fontsize=11,color=blue)
for ext in ['png','svg']:fig.savefig(O/('ORIGINAL_FRAME_CUBIC_RESIDUAL.'+ext),dpi=160,facecolor='white')
