from pathlib import Path
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent
fig, ax = plt.subplots(figsize=(12, 7))
fig.patch.set_facecolor('#fbfcff')
ax.set_facecolor('#fbfcff')
vertices = [(0, 1.7), (-2, -0.7), (2, -0.7)]
for i,k in ((0,1),(0,2),(1,2)):
    a,b = vertices[i],vertices[k]
    ax.plot([a[0],b[0]],[a[1],b[1]],color='#6e86a3',lw=2,zorder=1)
for i,(a,b) in enumerate(vertices):
    ax.text(a,b,rf'$A_{i+1}=\chi\lambda_{i+1}T_{i+1}$',ha='center',va='center',fontsize=17,
            bbox=dict(boxstyle='round,pad=.5',facecolor='#e7f1ff',edgecolor='#466888'),zorder=2)
labels = [(-1.23,.64,r'$\frac{\ell^3}{4}|[A_1,A_2]|^2=\chi^4\rho_{12}$'),
          (1.23,.64,r'$\frac{\ell^3}{4}|[A_1,A_3]|^2=\chi^4\rho_{13}$'),
          (0,-.85,r'$\frac{\ell^3}{4}|[A_2,A_3]|^2=\chi^4\rho_{23}$')]
for a,b,label in labels:
    ax.text(a,b,label,ha='center',va='center',fontsize=15,
            bbox=dict(facecolor='#fbfcff',edgecolor='none',pad=5))
ax.text(0,2.4,'Three positive orientation densities determine the three positive amplitudes',
        fontsize=18,ha='center',weight='bold')
ax.text(0,-1.58,r'$\lambda_1=\frac{\sqrt{2}}{\ell^{3/4}}\left(\frac{\rho_{12}\rho_{13}}{\rho_{23}}\right)^{1/4},\quad'
        r'\lambda_2=\frac{\sqrt{2}}{\ell^{3/4}}\left(\frac{\rho_{12}\rho_{23}}{\rho_{13}}\right)^{1/4},\quad'
        r'\lambda_3=\frac{\sqrt{2}}{\ell^{3/4}}\left(\frac{\rho_{13}\rho_{23}}{\rho_{12}}\right)^{1/4}$',
        fontsize=16,ha='center')
ax.text(0,-2.2,'Exact map diagram; the triangle positions have no spatial meaning.\n'
        'Proof: AMPLITUDE_ALGEBRA.md, AA2–AA3 and AA11. All three Lie algebra factors are retained.',
        fontsize=11,ha='center',color='#38475a')
ax.set_xlim(-3.4,3.4)
ax.set_ylim(-2.55,2.75)
ax.axis('off')
fig.tight_layout()
fig.savefig(root/'AMPLITUDE_FACTOR_MAP.svg')
fig.savefig(root/'AMPLITUDE_FACTOR_MAP.png',dpi=180)
print(root/'AMPLITUDE_FACTOR_MAP.png')
