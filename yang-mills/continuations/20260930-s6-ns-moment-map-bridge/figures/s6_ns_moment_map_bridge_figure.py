"""Render the corrected Sp(1) triality-to-profile morphism and its defect."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parent
PNG = ROOT / "S6_NS_MOMENT_MAP_BRIDGE.png"
SVG = ROOT / "S6_NS_MOMENT_MAP_BRIDGE.svg"


def box(
    axis: plt.Axes,
    x: float,
    y: float,
    width: float,
    height: float,
    text: str,
    *,
    face: str,
    edge: str,
    fontsize: float = 11,
) -> None:
    patch = FancyBboxPatch(
        (x, y),
        width,
        height,
        boxstyle="round,pad=0.014,rounding_size=0.018",
        linewidth=1.7,
        facecolor=face,
        edgecolor=edge,
    )
    axis.add_patch(patch)
    axis.text(
        x + width / 2,
        y + height / 2,
        text,
        ha="center",
        va="center",
        fontsize=fontsize,
        linespacing=1.34,
        color="#13233a",
    )


def arrow(
    axis: plt.Axes,
    start: tuple[float, float],
    end: tuple[float, float],
    *,
    color: str = "#27496d",
    label: str | None = None,
    label_offset: tuple[float, float] = (0.0, 0.02),
) -> None:
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=14,
        linewidth=1.8,
        color=color,
        connectionstyle="arc3,rad=0.0",
    )
    axis.add_patch(patch)
    if label:
        x = (start[0] + end[0]) / 2 + label_offset[0]
        y = (start[1] + end[1]) / 2 + label_offset[1]
        axis.text(
            x,
            y,
            label,
            ha="center",
            va="bottom",
            fontsize=9.5,
            color=color,
        )


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "axes.titleweight": "bold",
    }
)

fig = plt.figure(figsize=(18, 10.5), facecolor="#f7f4ed")
grid = fig.add_gridspec(
    2,
    3,
    height_ratios=[0.76, 0.24],
    width_ratios=[1.1, 1.0, 1.08],
    hspace=0.08,
    wspace=0.07,
)
axes = [fig.add_subplot(grid[0, index]) for index in range(3)]
footer = fig.add_subplot(grid[1, :])

for axis in axes + [footer]:
    axis.set_xlim(0, 1)
    axis.set_ylim(0, 1)
    axis.axis("off")

fig.suptitle(
    r"Corrected $S^6$ triality-to-profile morphism: quadratic bridge and exact source defect",
    fontsize=20,
    color="#102a43",
    y=0.985,
)
fig.text(
    0.5,
    0.947,
    r"Retained base $X\cong S^6$; no soft-period end, quantum state, or mass-gap conclusion is asserted",
    ha="center",
    fontsize=12,
    color="#486581",
)

# Panel 1: source bundle and the linear obstruction.
axis = axes[0]
axis.text(
    0.5,
    0.965,
    "1. Retained rank-24 bundle",
    ha="center",
    va="top",
    fontsize=14,
    color="#102a43",
    weight="bold",
)
box(
    axis,
    0.08,
    0.71,
    0.84,
    0.16,
    r"$\mathcal{W}_H=\mathcal{V}_{r,H}\oplus\mathcal{V}_{q,H}\oplus\mathcal{V}_{p,H}$"
    "\n"
    r"$\cong(\mathbb{R}^5\oplus\mathcal{A}_H)\oplus"
    r"(\mathcal{L}_{q,1}\oplus\mathcal{L}_{q,2})\oplus"
    r"(\mathcal{L}_{p,1}\oplus\mathcal{L}_{p,2})$",
    face="#d9eaf7",
    edge="#2f6690",
    fontsize=11.2,
)
box(
    axis,
    0.08,
    0.43,
    0.84,
    0.15,
    r"$\mathrm{Hom}_{\mathrm{Sp}(1)}"
    r"(W,\mathrm{Im}\,\mathbb{H})=\mathbb{R}\,\pi_{\mathrm{Ad}}$"
    "\n"
    r"one linear colour channel $\Longrightarrow [A_i,A_j]=0$",
    face="#fde6d2",
    edge="#c65d20",
)
arrow(axis, (0.5, 0.705), (0.5, 0.59), color="#c65d20", label="linear audit")
box(
    axis,
    0.08,
    0.13,
    0.84,
    0.17,
    r"$\mu_e(a)=ae\bar a,\quad e\in\{\mathbf{i},\mathbf{j},\mathbf{k}\}$"
    "\n"
    r"$\mu_e(ua)=u\mu_e(a)\bar u,\quad|\mu_e(a)|=|a|^2$"
    "\n"
    r"$\operatorname{rank}D\mu_e(a)=3$ for $a\ne0$",
    face="#dff3e4",
    edge="#2f855a",
)
arrow(
    axis,
    (0.5, 0.425),
    (0.5, 0.305),
    color="#2f855a",
    label="quadratic correction",
)

# Panel 2: exact \mathcal{M}_H and rank strata.
axis = axes[1]
axis.text(
    0.5,
    0.965,
    "2. Global polynomial map",
    ha="center",
    va="top",
    fontsize=14,
    color="#102a43",
    weight="bold",
)
box(
    axis,
    0.06,
    0.7,
    0.88,
    0.18,
    r"$\mathcal{M}_H=\mu_{\mathbf{i}}(\alpha)\otimes w^{(1)}$"
    "\n"
    r"$\quad+\mu_{\mathbf{j}}(\beta)\otimes w^{(2)}$"
    "\n"
    r"$\quad+\mu_{\mathbf{k}}(\gamma)\otimes w^{(3)}$",
    face="#e8e1f4",
    edge="#6b46a1",
)
box(
    axis,
    0.06,
    0.43,
    0.88,
    0.15,
    r"$\nabla\!\cdot w^{(a)}=0,\quad"
    r"\mathrm{supp}\,w^{(a)}\subset\overline{B_R}$"
    "\n"
    r"$(w^{(1)},w^{(2)},w^{(3)})=(e_1,e_2,e_3)$ on $B_r$",
    face="#fff3c4",
    edge="#b7791f",
)
arrow(axis, (0.5, 0.695), (0.5, 0.585), color="#6b46a1")
box(
    axis,
    0.06,
    0.14,
    0.88,
    0.17,
    r"$\mathcal{M}_H^{-1}(0)=\mathcal{V}_{r,H}\oplus\mathcal{L}_{p,2}$"
    "\n"
    r"real rank $12$"
    "\n"
    r"vertical rank strata: $0,\ 3,\ 6,\ 9$",
    face="#dff3e4",
    edge="#2f855a",
)
arrow(axis, (0.5, 0.425), (0.5, 0.315), color="#2f855a", label="proved")

# Panel 3: core curvature and source obstruction.
axis = axes[2]
axis.text(
    0.5,
    0.965,
    "3. Three-direction core",
    ha="center",
    va="top",
    fontsize=14,
    color="#102a43",
    weight="bold",
)
box(
    axis,
    0.07,
    0.72,
    0.86,
    0.14,
    r"on $B_r$: $(v_1,v_2,v_3)=(\mathbf{i},\mathbf{j},\mathbf{k})$"
    "\n"
    r"$\mathcal{F}_{12}=2\mathbf{k},\ "
    r"\mathcal{F}_{23}=2\mathbf{i},\ "
    r"\mathcal{F}_{31}=2\mathbf{j}$",
    face="#d9eaf7",
    edge="#2f6690",
)
box(
    axis,
    0.07,
    0.46,
    0.86,
    0.13,
    r"$F_{12}=4T_3,\quad F_{23}=4T_1,\quad F_{31}=4T_2$"
    "\n"
    r"$-2\sum_{i<j}\mathrm{tr}(F_{ij}^2)=48$",
    face="#dff3e4",
    edge="#2f855a",
)
arrow(axis, (0.5, 0.715), (0.5, 0.595), color="#2f855a", label="interaction")
box(
    axis,
    0.07,
    0.16,
    0.86,
    0.16,
    r"$\mathcal{J}_0=0,\qquad\mathcal{J}_j=-8e_j$"
    "\n"
    r"$D^\mu F_{\mu j}=-16T_j$"
    "\n"
    r"$\Longrightarrow$ outside the source-free locus",
    face="#f8d7da",
    edge="#b8323a",
)
arrow(axis, (0.5, 0.455), (0.5, 0.325), color="#b8323a", label="exact obstruction")

# Footer: what is proved and what follows.
footer.add_patch(
    FancyBboxPatch(
        (0.025, 0.12),
        0.95,
        0.72,
        boxstyle="round,pad=0.015,rounding_size=0.015",
        linewidth=1.6,
        facecolor="#eef2f6",
        edgecolor="#486581",
    )
)
footer.text(
    0.05,
    0.7,
    "Proved",
    fontsize=12.5,
    weight="bold",
    color="#2f855a",
    va="center",
)
footer.text(
    0.14,
    0.7,
    r"global equivariant $\mathcal{M}_H$; support; divergence; zero set; rank strata; non-Abelian core; exact source defect",
    fontsize=11.2,
    color="#13233a",
    va="center",
)
footer.text(
    0.05,
    0.46,
    "Next equation",
    fontsize=12.5,
    weight="bold",
    color="#b8323a",
    va="center",
)
footer.text(
    0.16,
    0.46,
    r"construct $\alpha$ with $D^\mu_{\mathcal{M}_H+\alpha}F_{\mu\nu}(\mathcal{M}_H+\alpha)=0$ while retaining nonzero commutator curvature",
    fontsize=11.2,
    color="#13233a",
    va="center",
)
footer.text(
    0.05,
    0.23,
    "Still required",
    fontsize=12.5,
    weight="bold",
    color="#6b46a1",
    va="center",
)
footer.text(
    0.16,
    0.23,
    r"soft-period extension; full connection; physical projection; continuum reconstruction; spectral support; theory identification",
    fontsize=11.2,
    color="#13233a",
    va="center",
)

fig.text(
    0.015,
    0.012,
    "Proof: PROOF.md, Theorem 7.1 and Sections 8–9. "
    "Source: sources/higher_rung/s6_higher_rung_24d_preprint.tex, lines 5205–5792.  "
    "Reproducible source: figures/s6_ns_moment_map_bridge_figure.py.",
    fontsize=9.3,
    color="#486581",
)

fig.savefig(PNG, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
fig.savefig(SVG, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"wrote {PNG}")
print(f"wrote {SVG}")
