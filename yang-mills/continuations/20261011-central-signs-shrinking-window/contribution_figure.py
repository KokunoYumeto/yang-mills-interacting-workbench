from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

root=Path(__file__).parent
labels=[r'$B_{6,\partial}$',r'$B_{6,\mathrm{int}}$',r'$A_{D,\partial}$',r'$A_{D,\mathrm{int}}$',r'$A_{F,\partial,0}$',r'$A_{F,\partial,1}$',r'$A_{F,\mathrm{int},0}$',r'$A_{F,\mathrm{int},1}$']
p=np.array([26,22,24,20,22,24,18,20])
coef=[r'$3V_3/16$',r'$3V_4/32$',r'$3P_3T_{1,2}/16$',r'$3P_4T_{1,3}/32$',r'$P_3/8$',r'$P_3T_{1,2}/16$',r'$P_4/16$',r'$P_4T_{1,3}/32$']
fig=plt.figure(figsize=(13.4,9.0),facecolor='#fbfaf6')
ax=fig.add_axes([.19,.30,.49,.50]);ax.set_facecolor('#fbfaf6')
arr=np.column_stack([p,p+6,p+5])
ax.imshow(arr,cmap='YlGnBu_r',vmin=18,vmax=32,aspect='auto')
for y in range(8):
    for x in range(3):
        ax.text(x,y,str(arr[y,x]),ha='center',va='center',fontsize=18,color='white' if arr[y,x]<23 else '#123042',weight='bold')
ax.set_xticks([0,1,2],['Gradient term\nexponent $p$','Energy term\nexponent $p+6$','Endpoint term\nexponent $p+5$'],fontsize=12)
ax.xaxis.tick_top();ax.tick_params(length=0,pad=12)
ax.set_yticks(range(8),labels,fontsize=14)
for spine in ax.spines.values():spine.set_visible(False)
for line in [1.5,3.5]:ax.axhline(line,color='#fbfaf6',lw=6)
axc=fig.add_axes([.70,.30,.27,.50]);axc.set_xlim(0,1);axc.set_ylim(7.5,-.5);axc.axis('off')
axc.text(.03,-1.30,'Gradient limit coefficient',fontsize=13,weight='bold',color='#123042')
for y,ss in enumerate(coef):axc.text(.03,y,ss,fontsize=15,va='center',color='#123042')
fig.text(.035,.965,'All eight bulk and boundary bound contributions',fontsize=20,weight='bold',color='#123042',va='top')
fig.text(.035,.895,r'Each row records an explicit lower-bound function $f_j$ with $j^p f_j\to A>0$.',fontsize=13,color='#394c59')
fig.text(.035,.22,r'Energy multiplies by $\kappa_*\beta_{0,j}^2$; endpoint correction multiplies by $j\beta_{0,j}^2$.',fontsize=13,color='#123042')
fig.text(.035,.18,r'$j^6\beta_{0,j}^2\to K_\beta=5000\pi^2/\kappa_*^2$: the coefficients become $\kappa_*K_\beta A$ and $K_\beta A$.',fontsize=13,color='#123042')
fig.text(.035,.135,r'Even positive endpoint: $A_{D,\mathrm{int}}$ has exponent 25; the boundary term $B_{6,\mathrm{int}}$ has exponent 27.',fontsize=12,color='#123042')
fig.text(.035,.100,r'Odd negative endpoint: $A_{F,\mathrm{int},0}$ has exponent 23. Every other signed term remains in SR34 / SR70.',fontsize=12,color='#123042')
fig.text(.035,.055,'Proof: SQUARE_ROOT_SCORE_RECEIVING_MAPS.md, SR22–SR35; stronger heat constants: SR66–SR70.\nConstants are defined in SR28; replace them by SR69 hats for the stronger score. These powers do not determine the actual endpoint sign.',fontsize=10,color='#52616b')
fig.savefig(root/'CONTRIBUTION_POWERS.png',dpi=180,facecolor=fig.get_facecolor())
fig.savefig(root/'CONTRIBUTION_POWERS.svg',facecolor=fig.get_facecolor())
plt.close(fig)
print('Created reproducible contribution figure.')
