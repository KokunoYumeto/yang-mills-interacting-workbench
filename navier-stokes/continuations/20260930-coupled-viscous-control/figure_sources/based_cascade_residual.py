"""Render the exact reset obstruction and based-cascade interfaces."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "corpus/artifacts/math/output/navier_stokes_research_2026-09-08"
    / "lanes/coupled_viscous_control/infinite_modified/figures"
    / "based_cascade_residual.png"
)
OUT.parent.mkdir(parents=True, exist_ok=True)


COLORS = {
    "ink": "#17243a",
    "muted": "#526176",
    "red": "#b7394b",
    "red_fill": "#fdebed",
    "green": "#17795e",
    "green_fill": "#e8f7f1",
    "blue": "#255da8",
    "blue_fill": "#edf4ff",
    "gold": "#9b6a00",
    "gold_fill": "#fff6dc",
    "line": "#aeb8c6",
    "paper": "#fbfcfe",
}


def box(ax, x, y, w, h, title, body, edge, fill, title_size=12.5, body_size=11.0):
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        linewidth=1.7,
        edgecolor=edge,
        facecolor=fill,
        zorder=2,
    )
    ax.add_patch(patch)
    ax.text(
        x + 0.025 * w,
        y + h - 0.20 * h,
        title,
        fontsize=title_size,
        fontweight="bold",
        color=edge,
        va="center",
        zorder=3,
    )
    ax.text(
        x + 0.5 * w,
        y + 0.42 * h,
        body,
        fontsize=body_size,
        color=COLORS["ink"],
        ha="center",
        va="center",
        linespacing=1.35,
        zorder=3,
    )


def arrow(ax, start, end, color, text=None, curve=0.0, text_offset=(0.0, 0.0)):
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=15,
        linewidth=1.8,
        color=color,
        connectionstyle=f"arc3,rad={curve}",
        zorder=4,
    )
    ax.add_patch(patch)
    if text:
        ax.text(
            (start[0] + end[0]) / 2 + text_offset[0],
            (start[1] + end[1]) / 2 + text_offset[1],
            text,
            fontsize=10.3,
            color=color,
            ha="center",
            va="center",
            bbox=dict(boxstyle="round,pad=0.22", facecolor=COLORS["paper"], edgecolor="none"),
            zorder=5,
        )


fig, ax = plt.subplots(figsize=(16, 11), dpi=180)
fig.patch.set_facecolor(COLORS["paper"])
ax.set_facecolor(COLORS["paper"])
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")

ax.text(
    0.5,
    0.965,
    "From the reset obstruction to the exact based-cascade problem",
    fontsize=22,
    fontweight="bold",
    color=COLORS["ink"],
    ha="center",
    va="center",
)
ax.text(
    0.5,
    0.925,
    "Every scale factor, parent cross term, and residual derivative remains visible",
    fontsize=12.5,
    color=COLORS["muted"],
    ha="center",
    va="center",
)

# Reset obstruction.
ax.text(0.04, 0.872, "1  Complete-packet reset fails", fontsize=15, fontweight="bold", color=COLORS["red"])
box(
    ax,
    0.055,
    0.705,
    0.33,
    0.125,
    "Returned endpoint",
    r"$\omega_{\rm out}(0)\geq c^{-1}c_W\sigma_2/4>0$" + "\n" + r"$Z(T)=0,\ \Omega_3(T)=0$",
    COLORS["red"],
    COLORS["red_fill"],
)
box(
    ax,
    0.615,
    0.705,
    0.33,
    0.125,
    "Fresh complete packet",
    r"$u_{\rm in}\equiv0$" + "\n" + r"$\omega_{\rm in}\equiv0$ at every centre",
    COLORS["red"],
    COLORS["red_fill"],
)
arrow(ax, (0.39, 0.767), (0.61, 0.767), COLORS["red"])
ax.plot([0.485, 0.515], [0.735, 0.799], color=COLORS["red"], lw=4.2, solid_capstyle="round", zorder=6)
ax.plot([0.485, 0.515], [0.799, 0.735], color=COLORS["red"], lw=4.2, solid_capstyle="round", zorder=6)
ax.text(0.5, 0.680, r"curl mismatch $\Longrightarrow$ no $C^1$ join", fontsize=12.5, color=COLORS["red"], ha="center", fontweight="bold")

# Based state flow.
ax.text(0.04, 0.635, "2  Retain the parent and add a left-flat relative increment", fontsize=15, fontweight="bold", color=COLORS["green"])
box(
    ax,
    0.055,
    0.475,
    0.26,
    0.12,
    "Physical parent",
    r"$(\theta^{<q},u^{<q},p^{<q})$" + "\n" + "complete returned state",
    COLORS["green"],
    COLORS["green_fill"],
)
box(
    ax,
    0.37,
    0.475,
    0.26,
    0.12,
    "Relative increment",
    r"$(\vartheta_q,v_q,\pi_q)$" + "\n" + r"flat and zero at its birth time",
    COLORS["green"],
    COLORS["green_fill"],
)
box(
    ax,
    0.685,
    0.475,
    0.26,
    0.12,
    "Updated parent",
    r"$(\theta^{[q]},u^{[q]},p^{[q]})$" + "\n" + "retained for stage $q+1$",
    COLORS["green"],
    COLORS["green_fill"],
)
ax.text(0.342, 0.535, "+", fontsize=28, fontweight="bold", color=COLORS["green"], ha="center", va="center")
arrow(ax, (0.635, 0.535), (0.68, 0.535), COLORS["green"])

# Exact scale and residual interfaces.
ax.text(0.04, 0.415, "3  Exact normalization, residual array, and receiving bound", fontsize=15, fontweight="bold", color=COLORS["blue"])
box(
    ax,
    0.04,
    0.205,
    0.255,
    0.17,
    "State interface",
    r"$c_q=(\delta_*/d)\rho_q^2$" + "\n"
    + r"$\mathcal{U}_q=(c_q/\rho_q)u^{<q}$" + "\n"
    + r"$\mathcal{D}_q=c_q\nabla u^{<q}$" + "\n"
    + r"$\mathcal{G}_q=c_q^2\nabla\theta^{<q}$",
    COLORS["blue"],
    COLORS["blue_fill"],
    body_size=10.8,
)
box(
    ax,
    0.365,
    0.205,
    0.285,
    0.17,
    "Normalized residual",
    r"$\widetilde e_\theta=\partial_\tau\widetilde\vartheta$" + "\n"
    + r"$+(\mathcal{U}+\widetilde v)\!\cdot\!\nabla\widetilde\vartheta$" + "\n"
    + r"$+\widetilde v\!\cdot\!\mathcal{G}-\delta_*\Delta\widetilde\vartheta$" + "\n"
    + r"$\widetilde e_u=\partial_\tau\widetilde v+(\mathcal{U}+\widetilde v)\!\cdot\!\nabla\widetilde v$" + "\n"
    + r"$+\mathcal{D}\widetilde v+\nabla\widetilde\pi-\delta_*\Delta\widetilde v-\widetilde\vartheta e_2$",
    COLORS["blue"],
    COLORS["blue_fill"],
    body_size=9.8,
)
box(
    ax,
    0.72,
    0.205,
    0.24,
    0.17,
    "Required bound",
    r"$\rho_q=2^{-q}$" + "\n"
    + r"$\|\partial^\alpha\widetilde e_\theta\|_\infty\leq2^{-q^2}$" + "\n"
    + r"$\|\partial^\alpha\widetilde e_{u,k}\|_\infty\leq2^{-q^2}$" + "\n"
    + r"$|\alpha|\leq q,\ k=1,2$: all jets summable",
    COLORS["gold"],
    COLORS["gold_fill"],
    body_size=10.2,
)
arrow(
    ax,
    (0.30, 0.29),
    (0.36, 0.29),
    COLORS["blue"],
)
arrow(
    ax,
    (0.655, 0.29),
    (0.715, 0.29),
    COLORS["gold"],
)

ax.text(
    0.5,
    0.137,
    r"A fixed nonzero entry profile demands physical scales "
    r"$u\sim\rho_q^{-1}$, $\nabla u\sim\rho_q^{-2}$, "
    r"$\nabla\theta\sim\rho_q^{-4}$ (with the displayed $d/\delta_*$ factors).",
    fontsize=12.2,
    color=COLORS["ink"],
    ha="center",
    va="center",
    bbox=dict(boxstyle="round,pad=0.42", facecolor="#f2f4f8", edgecolor=COLORS["line"]),
)
ax.text(
    0.5,
    0.075,
    "The remaining theorem is the based return-renormalization map that realizes both the state interface and these residual bounds.",
    fontsize=12.3,
    color=COLORS["muted"],
    ha="center",
    va="center",
)

fig.savefig(OUT, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close(fig)
print(OUT)
