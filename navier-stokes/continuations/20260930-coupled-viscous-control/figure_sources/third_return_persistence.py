"""Render the exact logical structure of the third-return persistence proof."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


HERE = Path(__file__).resolve().parent
OUT = (
    HERE.parent
    / "corpus"
    / "artifacts"
    / "math"
    / "output"
    / "navier_stokes_research_2026-09-08"
    / "lanes"
    / "coupled_viscous_control"
    / "third_return"
    / "figures"
    / "third_return_persistence.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "mathtext.fontset": "dejavusans",
    "figure.facecolor": "#f8fafc",
    "axes.facecolor": "#f8fafc",
})

fig, ax = plt.subplots(figsize=(13.2, 7.4), dpi=180)
ax.set_xlim(0, 13.2)
ax.set_ylim(0, 7.4)
ax.axis("off")


def box(x, y, w, h, title, lines, color):
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.035,rounding_size=0.11",
        linewidth=1.7, edgecolor=color, facecolor="white",
    )
    ax.add_patch(patch)
    ax.text(x + 0.18, y + h - 0.28, title, fontsize=12.2, weight="bold",
            color=color, va="top")
    for i, line in enumerate(lines):
        ax.text(x + 0.18, y + h - 0.72 - 0.36 * i, line,
                fontsize=10.2, color="#172033", va="top")
    return patch


def arrow(x1, y1, x2, y2, label=""):
    ar = FancyArrowPatch((x1, y1), (x2, y2), arrowstyle="-|>",
                         mutation_scale=15, linewidth=1.6,
                         color="#475569")
    ax.add_patch(ar)
    if label:
        ax.text((x1+x2)/2, (y1+y2)/2 + 0.16, label,
                ha="center", va="bottom", fontsize=9.6,
                color="#334155")


box(0.35, 4.45, 3.55, 2.25,
    "Earlier selected returns",
    [r"closed root graph $\mathcal{R}\subset[0,d_{3,\max}]\times[0,3]^2$",
     r"all roots retained; least-root jumps allowed",
     r"entry fibres $\mathcal{E}_d$ approach $\mathcal{E}_0$ as $d\downarrow0$"],
    "#1d4ed8")

box(4.75, 4.45, 3.7, 2.25,
    "Inviscid trial family",
    [r"$\mathcal{T}_0\Subset\mathcal{D}$ with safety margin $\rho>0$",
     r"$p\geq p_*>0$ for every $m\in[0,3]$",
     r"full source geometry and linear pair on $[0,T]$"],
    "#047857")

box(9.25, 4.45, 3.6, 2.25,
    "Uniform positive diffusion",
    [r"choose $0<d\leq d_{\mathrm{ret}}\leq d_{3,\max}$",
     r"all trials remain in $\mathcal{D}$ and $p\geq p_*/2$",
     r"full damped pair retained; coefficients evolve"],
    "#7c3aed")

arrow(3.92, 5.58, 4.7, 5.58)
arrow(8.47, 5.58, 9.2, 5.58)

box(0.55, 0.55, 3.5, 2.65,
    "Exact source margins at $d=0$",
    [r"$F_0(0)\geq 1/8$", r"$F_0(3)\leq-1$",
     r"at every root: $W_0\geq1/12$",
     r"$G_0\geq1/6$, $\mathcal{C}_0\geq c_W$"],
    "#0f766e")

box(4.85, 0.55, 3.55, 2.65,
    "Persisting endpoint signs",
    [r"$F_d(0)\geq1/16$", r"$F_d(3)\leq-15/16$",
     r"continuity in $m$ gives a compact zero set",
     r"select its least member $m_{3,*}(d)$"],
    "#b45309")

box(9.15, 0.55, 3.75, 2.65,
    "Actual third return",
    [r"$Z(T)=0$, $\Omega_3(T)=0$, $\Theta_3(T)<0$",
     r"$\Omega_2(T)/\sigma_2\geq1/48$",
     r"$\log\!\left(\frac{-\Theta_3(T)}{-\Theta_3(0)}\right)\geq1/24$",
     r"origin curl $/\sigma_2\geq c_W/4$"],
    "#be123c")

arrow(4.08, 1.88, 4.8, 1.88)
arrow(8.43, 1.88, 9.1, 1.88)
arrow(11.05, 4.4, 11.05, 3.27, r"same $d_{\mathrm{ret}}$")

ax.text(6.6, 7.15, "Finite third shooting return: compact persistence with every diffusion term retained",
        ha="center", va="top", fontsize=16, weight="bold", color="#0f172a")
ax.text(6.6, 0.13, "The argument uses strict margins and compactness; it does not assume monotonicity or uniqueness of any later-stage root.",
        ha="center", va="bottom", fontsize=10.5, color="#334155")

fig.tight_layout(pad=0.4)
fig.savefig(OUT, bbox_inches="tight")
print(OUT)
