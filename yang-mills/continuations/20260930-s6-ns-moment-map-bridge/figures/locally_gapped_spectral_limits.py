"""Reproduce the spectral-limit trichotomy used by the Yang--Mills program.

The curves are exact cumulative distribution functions:

* escape:       mu_j = delta_j;
* zero collapse: mu_j = delta_{1/j};
* accumulation: mu_j = j^{-1} sum_{k=1}^j delta_{k/j}.

The last family is the spectral measure of the vector
j^{-1/2} sum_k e_k for the finite Hamiltonian with eigenvalues k/j.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).resolve().parent
JS = (4, 8, 16)
COLORS = ("#D55E00", "#0072B2", "#009E73")


def right_step(x: np.ndarray, threshold: float) -> np.ndarray:
    return (x >= threshold).astype(float)


def empirical_uniform_cdf(x: np.ndarray, j: int) -> np.ndarray:
    return np.clip(np.floor(j * x) / j, 0.0, 1.0)


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10.5,
        "axes.titlesize": 11.5,
        "axes.labelsize": 10.5,
        "legend.fontsize": 9.0,
        "figure.dpi": 160,
    }
)

fig, axes = plt.subplots(1, 3, figsize=(13.5, 4.2), constrained_layout=True)

# A. A normalized state moves to arbitrarily large physical energy.
x = np.linspace(0.0, 18.0, 1801)
for j, color in zip(JS, COLORS):
    axes[0].step(x, right_step(x, float(j)), where="post", color=color, lw=2, label=rf"$j={j}$")
axes[0].set_title(r"A. High-energy escape: $\mu_j=\delta_j$")
axes[0].set_xlabel(r"energy $E$")
axes[0].set_ylabel(r"$F_j(E)=\mu_j([0,E])$")
axes[0].set_xlim(0, 18)
axes[0].set_ylim(-0.03, 1.08)
axes[0].annotate(
    r"jump moves to $+\infty$",
    xy=(16, 0.72),
    xytext=(8.0, 0.72),
    arrowprops={"arrowstyle": "->", "lw": 1.2},
    ha="center",
)
axes[0].legend(loc="lower right", frameon=False)

# B. A vacuum-orthogonal state becomes a second zero-energy vector.
x = np.linspace(0.0, 0.30, 1501)
for j, color in zip(JS, COLORS):
    axes[1].step(x, right_step(x, 1.0 / j), where="post", color=color, lw=2, label=rf"$j={j}$")
axes[1].set_title(r"B. Zero collapse: $\mu_j=\delta_{1/j}$")
axes[1].set_xlabel(r"energy $E$")
axes[1].set_xlim(0, 0.30)
axes[1].set_ylim(-0.03, 1.08)
axes[1].annotate(
    r"jump moves to $0$",
    xy=(1 / 16, 0.72),
    xytext=(0.20, 0.72),
    arrowprops={"arrowstyle": "->", "lw": 1.2},
    ha="center",
)
axes[1].legend(loc="lower right", frameon=False)

# C. The finite measures converge to Lebesgue measure on (0,1).
x = np.linspace(0.0, 1.0, 2001)
for j, color in zip(JS, COLORS):
    axes[2].step(x, empirical_uniform_cdf(x, j), where="post", color=color, lw=1.8, label=rf"$j={j}$")
axes[2].plot(x, x, color="#222222", lw=2.2, ls="--", label=r"limit $F(E)=E$")
axes[2].set_title(r"C. Continuous accumulation: $j^{-1}\sum_{k=1}^j\delta_{k/j}$")
axes[2].set_xlabel(r"energy $E$")
axes[2].set_xlim(0, 1)
axes[2].set_ylim(-0.03, 1.08)
axes[2].legend(loc="lower right", frameon=False)

for ax in axes:
    ax.grid(True, alpha=0.22, lw=0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

fig.suptitle(
    r"Three limits compatible with finite-regulator gaps $\Delta_j=1/j$",
    fontsize=14,
    y=1.035,
)

fig.savefig(OUT / "LOCALLY_GAPPED_SPECTRAL_LIMITS.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "LOCALLY_GAPPED_SPECTRAL_LIMITS.svg", bbox_inches="tight")
