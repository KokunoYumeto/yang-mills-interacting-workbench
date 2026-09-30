"""Render the exact research-program map for the S6 + NS Yang--Mills route."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUT = Path(__file__).resolve().parent


def box(ax, xy, wh, title, body, face, edge="#202020", title_color="#111111"):
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=1.5,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(x + 0.02 * w, y + h - 0.12 * h, title, fontsize=12, weight="bold", color=title_color, va="top")
    ax.text(x + 0.02 * w, y + h - 0.32 * h, body, fontsize=9.2, color="#202020", va="top", linespacing=1.35)
    return patch


def arrow(ax, start, end, label=None, color="#333333", style="-", rad=0.0, lw=1.8):
    arr = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=15,
        linewidth=lw,
        linestyle=style,
        color=color,
        connectionstyle=f"arc3,rad={rad}",
    )
    ax.add_patch(arr)
    if label:
        mx = (start[0] + end[0]) / 2
        my = (start[1] + end[1]) / 2 + (0.025 if rad >= 0 else -0.025)
        ax.text(mx, my, label, fontsize=8.7, color=color, ha="center", va="center", backgroundcolor="white")


fig, ax = plt.subplots(figsize=(15.5, 9.2), dpi=160)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

ax.text(
    0.5,
    0.965,
    r"Higher-domain + smooth-flow programme toward a reconstructed gapless state",
    ha="center",
    va="top",
    fontsize=17,
    weight="bold",
)
ax.text(
    0.5,
    0.925,
    r"Every lower box is required; the endpoint is the programme goal and has not been proved.",
    ha="center",
    va="top",
    fontsize=10.5,
    color="#444444",
)

box(
    ax,
    (0.035, 0.66),
    (0.255, 0.205),
    r"Structural prototype: $S^6$ cusp line",
    r"period matrix $P_R$ and integral lattice" "\n"
    r"$\lambda_{R,k}=4\pi^2\|P_R^{-T}k\|^2$" "\n"
    r"gauge-equivariant holonomy map" "\n"
    r"vertical operator: $0\in\sigma_c\cap\sigma_{ess}$, $\ker=0$",
    "#DDEBF7",
    edge="#2B6F9E",
)

box(
    ax,
    (0.365, 0.66),
    (0.27, 0.205),
    r"Select the higher domain $\mathfrak{D}$",
    r"integral local system and exact period/Gram map" "\n"
    r"controlled cusp with several soft directions" "\n"
    r"smooth global carrier or compactification" "\n"
    r"frame/triality data for non-Abelian colour",
    "#E4F2E3",
    edge="#3D8B40",
)

box(
    ax,
    (0.705, 0.66),
    (0.26, 0.205),
    r"Candidate state engine: smooth NS data",
    r"$\partial_su+(u\!\cdot\!\nabla)u-\nu\Delta u+\nabla p=f$" "\n"
    r"$\nabla\!\cdot u=0$; support and all norms retained" "\n"
    r"regular global family required for the target state" "\n"
    r"claimed singular endpoint used only as a diagnostic",
    "#FFF1D6",
    edge="#C47A00",
)

box(
    ax,
    (0.22, 0.365),
    (0.26, 0.205),
    r"Exact gauge and regulator map",
    r"Cartan seed: $A_i=\lambda u_iT$" "\n"
    r"multi-colour lift retains $[A_i,A_j]$" "\n"
    r"holonomies $\to$ physical lattice observables/states" "\n"
    r"Gauss law, sources, units and support proved",
    "#F0E5F7",
    edge="#7D4E9D",
)

box(
    ax,
    (0.535, 0.365),
    (0.26, 0.205),
    r"Continuum quantum reconstruction",
    r"one common local gauge-invariant algebra" "\n"
    r"Schwinger-function convergence and reflection positivity" "\n"
    r"strongly continuous $e^{-tH}$; unique vacuum" "\n"
    r"nonzero connected correlation proves interaction",
    "#E8E5F8",
    edge="#5A55A5",
)

box(
    ax,
    (0.365, 0.075),
    (0.30, 0.19),
    r"Programme endpoint: smooth global gapless state",
    r"$\ker H=\mathbb{C}\Omega$" "\n"
    r"$\mu_O(\{0\})=0$ and $\mu_O((0,\varepsilon))>0$ for every $\varepsilon>0$" "\n"
    r"therefore $\inf(\sigma(H)\cap(0,\infty))=0$" "\n"
    r"universality identifies the theory selected by the YM action",
    "#DDF3EF",
    edge="#168777",
)

arrow(ax, (0.29, 0.76), (0.365, 0.76), "extract functional features", color="#2B6F9E")
arrow(ax, (0.50, 0.66), (0.39, 0.57), "domain frame and soft modes", color="#3D8B40")
arrow(ax, (0.80, 0.66), (0.46, 0.51), "smooth flow/profile family", color="#C47A00", rad=0.10)
arrow(ax, (0.48, 0.47), (0.535, 0.47), "regulated state map", color="#6D477F")
arrow(ax, (0.665, 0.365), (0.55, 0.265), "spectral transport", color="#5A55A5")

ax.text(0.035, 0.305, "Exact exclusion tests", fontsize=11.5, weight="bold", color="#A32121")
failures = [
    r"source singularity or failure of global smoothness",
    r"fixed-Cartan/free limit with no non-Abelian interaction",
    r"spectral probability escaping every bounded energy interval",
    r"vacuum-orthogonal mass collapsing to $\delta_0$",
    r"failure of reconstruction axioms or of universality",
]
for i, item in enumerate(failures):
    ax.text(0.04, 0.275 - i * 0.042, "• " + item, fontsize=9.3, color="#7E2020", va="top")

arrow(ax, (0.35, 0.365), (0.18, 0.30), None, color="#A32121", style="--", rad=0.12, lw=1.4)
arrow(ax, (0.69, 0.365), (0.27, 0.25), None, color="#A32121", style="--", rad=0.18, lw=1.4)

fig.savefig(OUT / "S6_NS_SMOOTH_GLOBAL_NO_GAP_PROGRAM.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "S6_NS_SMOOTH_GLOBAL_NO_GAP_PROGRAM.svg", bbox_inches="tight")
