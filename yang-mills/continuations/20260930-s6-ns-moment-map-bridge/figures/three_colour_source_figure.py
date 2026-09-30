"""Render the exact curvature and source map for the three-colour lift."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


OUT = Path(__file__).resolve().parent


def panel(ax, x, y, w, h, title, lines, face, edge, body_size=10.0):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.016",
        linewidth=1.6,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(x + 0.02 * w, y + h - 0.12 * h, title, fontsize=12.2, weight="bold", va="top")
    top = y + h - 0.34 * h
    step = min(0.16 * h, 0.48 * h / max(len(lines) - 1, 1))
    for index, line in enumerate(lines):
        ax.text(x + 0.025 * w, top - index * step, line, fontsize=body_size, va="top")
    return patch


def arrow(ax, start, end, colour="#353535"):
    ax.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=16,
            linewidth=1.8,
            color=colour,
        )
    )


fig, ax = plt.subplots(figsize=(16.0, 10.0), dpi=160)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

ax.text(
    0.5,
    0.965,
    "Three-colour Yang--Mills lift: exact curvature and source defect",
    fontsize=18,
    weight="bold",
    ha="center",
    va="top",
)
ax.text(
    0.5,
    0.925,
    r"$T_a=-i\sigma_a/2$, $[T_a,T_b]=\varepsilon_{abc}T_c$, "
    r"$-2\operatorname{tr}(T_aT_b)=\delta_{ab}$, $x^0=ct$",
    fontsize=11.5,
    ha="center",
    va="top",
    color="#404040",
)

colours = ("#DCEAF7", "#E7F4E5", "#FFF0D5")
edges = ("#2A6F9E", "#3B8840", "#C37900")
for a in range(3):
    panel(
        ax,
        0.045 + 0.205 * a,
        0.745,
        0.17,
        0.12,
        rf"Colour {a + 1}",
        [rf"$u^{{({a + 1})}}$, $\nabla\!\cdot u^{{({a + 1})}}=0$", rf"calibration $\lambda_{a + 1}\neq 0$"],
        colours[a],
        edges[a],
    )

panel(
    ax,
    0.71,
    0.725,
    0.245,
    0.16,
    "Connection",
    [r"$A_0=0$", r"$A_i=\sum_{a=1}^{3}\lambda_a u_i^{(a)}T_a$"],
    "#EEE6F7",
    "#78509A",
)
input_centres = (0.13, 0.335, 0.54)
for centre, edge in zip(input_centres, edges):
    ax.plot([centre, centre], [0.745, 0.708], color=edge, linewidth=1.8)
ax.plot([input_centres[0], 0.64], [0.708, 0.708], color="#555555", linewidth=1.8)
arrow(ax, (0.64, 0.708), (0.71, 0.775), "#78509A")

panel(
    ax,
    0.045,
    0.39,
    0.43,
    0.275,
    "Full spatial curvature",
    [
        r"$F_{ij}=\sum_c B_{ij}^cT_c$",
        r"$B_{ij}^c=\lambda_c(\partial_i u_j^{(c)}-\partial_j u_i^{(c)})$",
        r"$\quad+\sum_{a<b}\varepsilon_{abc}\lambda_a\lambda_b$",
        r"$\qquad\cdot(u_i^{(a)}u_j^{(b)}-u_i^{(b)}u_j^{(a)})$",
        r"$-2\sum_{i<j}\operatorname{tr}(F_{ij}^2)=\sum_{i<j,c}(B_{ij}^c)^2$",
    ],
    "#E8F0FA",
    "#376C9A",
    body_size=8.8,
)

panel(
    ax,
    0.525,
    0.39,
    0.43,
    0.275,
    "Full Yang--Mills source defect",
    [
        r"$\mathcal{J}_\nu=D^\mu F_{\mu\nu}=\sum_c\mathcal{J}_\nu^cT_c$",
        r"$\mathcal{J}_0^c=-c^{-1}\sum_{i,a,b}\varepsilon_{abc}\lambda_a\lambda_b$",
        r"$\qquad\cdot u_i^{(a)}\partial_tu_i^{(b)}$",
        r"$\mathcal{J}_j^c=-\lambda_c c^{-2}\partial_t^2u_j^{(c)}+\sum_i\partial_iB_{ij}^c$",
        r"$\qquad+\sum_{i,a,b}\varepsilon_{abc}\lambda_a u_i^{(a)}B_{ij}^b$",
    ],
    "#FBE7E6",
    "#A83A35",
    body_size=8.8,
)

arrow(ax, (0.83, 0.725), (0.35, 0.665), "#78509A")
arrow(ax, (0.83, 0.725), (0.70, 0.665), "#78509A")

panel(
    ax,
    0.045,
    0.155,
    0.275,
    0.19,
    "Interaction witness",
    [
        r"$U=(u_i^{(a)})$",
        r"$\operatorname{rank}U\geq 2$ somewhere",
        r"$\Longrightarrow$ a $2\times2$ minor is nonzero",
        r"$\Longrightarrow$ commutator curvature is present",
    ],
    "#E6F3E5",
    "#3A8440",
)

panel(
    ax,
    0.365,
    0.155,
    0.275,
    0.19,
    "Source-free criterion",
    [
        r"$\mathcal{J}_\nu^c=0$",
        r"for every $\nu=0,1,2,3$",
        r"and every $c=1,2,3$",
        r"twelve coupled coefficient equations",
    ],
    "#FFF0D9",
    "#C27A04",
)

panel(
    ax,
    0.685,
    0.155,
    0.27,
    0.19,
    "One-colour check",
    [
        r"$u^{(2)}=u^{(3)}=0$",
        r"$\Longrightarrow\mathcal{J}_0=0$",
        r"$\mathcal{J}_j=\lambda(\Delta u_j-c^{-2}\partial_t^2u_j)T_1$",
        r"exactly the retained Cartan source",
    ],
    "#ECE9F8",
    "#6656A4",
)

arrow(ax, (0.255, 0.39), (0.18, 0.345), "#376C9A")
arrow(ax, (0.74, 0.39), (0.505, 0.345), "#A83A35")
arrow(ax, (0.76, 0.39), (0.82, 0.345), "#A83A35")

ax.text(
    0.5,
    0.07,
    "The higher-domain frame must preserve the interaction witness and solve the full source equations, "
    "or retain the displayed defect as sourced trial data.",
    ha="center",
    va="center",
    fontsize=11.2,
    color="#333333",
)

fig.savefig(OUT / "THREE_COLOUR_SOURCE_DEFECT.png", dpi=220, bbox_inches="tight")
fig.savefig(OUT / "THREE_COLOUR_SOURCE_DEFECT.svg", bbox_inches="tight")
