"""Reproduce the exact compact-counterexample estimate shown in PVI24."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

out = Path(__file__).resolve().parent
eps = np.linspace(0, 0.045, 400)
base = -8721/784
upper = base+7935*eps**2
fig, ax = plt.subplots(figsize=(10.4, 5.7), constrained_layout=True)
ax.plot(eps, upper, color='#b3412f', lw=2.8,
        label=r'Proved upper bound $-8721/784+7935\varepsilon^2$')
ax.axhline(0, color='#343e4d', lw=1.3)
ax.axhline(base, color='#77808d', lw=1.0, ls=':',
           label=r'Exact reference covariance $-8721/784$')
ax.scatter([0.01], [base+7935*0.01**2], color='#b3412f', s=65, zorder=4)
ax.annotate(r'$\varepsilon=1/100$'+'\n'+r'upper bound $=-506181/49000<0$',
            xy=(0.01, base+7935*0.01**2), xytext=(0.003, -3.5),
            arrowprops={'arrowstyle':'->', 'color':'#343e4d'}, fontsize=12)
ax.fill_between(eps, upper, 0, where=upper<0, color='#b3412f', alpha=0.10)
ax.set_xlim(0, 0.045)
ax.set_ylim(-13.0, 6)
ax.set_xlabel(r'Parameter $\varepsilon$ in $\psi_\varepsilon\propto(\varepsilon^2+D_{p_1}+D_{p_2}+D_{p_3})^{-3}$', fontsize=12)
ax.set_ylabel(r'Upper bound for $\varepsilon^4\operatorname{Cov}(V_\varepsilon,|\nabla\log\psi_\varepsilon|^2)/\kappa$', fontsize=11)
ax.set_title('Compact gauge-invariant counterexample: the covariance is negative',
             fontsize=15, pad=18)
ax.grid(alpha=0.18)
ax.legend(loc='upper left', frameon=False, fontsize=10)
fig.text(0.01, -0.055,
         'PVI20–PVI24: three edge-disjoint elementary plaquettes; all original vertex constraints.\n'
         'The displayed curve is a proved bound, not sampled covariance. The explicit rational potential differs from the original linear potential.',
         fontsize=9, color='#343e4d')
fig.savefig(out/'compact_covariance_bound.png', dpi=170, bbox_inches='tight')
fig.savefig(out/'compact_covariance_bound.svg', bbox_inches='tight')
