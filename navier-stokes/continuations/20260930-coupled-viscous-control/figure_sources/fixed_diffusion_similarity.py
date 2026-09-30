"""Render the exact fixed-diffusion similarity and force-jet budget."""

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch


ROOT = Path(__file__).resolve().parents[1]
OUT = (
    ROOT
    / "corpus/artifacts/math/output/navier_stokes_research_2026-09-08"
    / "lanes/coupled_viscous_control/infinite_modified/figures"
    / "fixed_diffusion_similarity.png"
)


def box(ax, xy, width, height, title, lines, edge, face):
    patch = FancyBboxPatch(
        xy,
        width,
        height,
        boxstyle="round,pad=0.018,rounding_size=0.025",
        linewidth=2.2,
        edgecolor=edge,
        facecolor=face,
    )
    ax.add_patch(patch)
    ax.text(
        xy[0] + 0.025,
        xy[1] + height - 0.06,
        title,
        ha="left",
        va="top",
        fontsize=13.5,
        fontweight="bold",
        color=edge,
    )
    ax.text(
        xy[0] + 0.025,
        xy[1] + height - 0.135,
        "\n".join(lines),
        ha="left",
        va="top",
        fontsize=11.2,
        linespacing=1.45,
        color="#172033",
    )


plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "mathtext.fontset": "dejavusans",
        "axes.titleweight": "bold",
    }
)

fig = plt.figure(figsize=(16, 10), facecolor="#f7f4ed")
grid = fig.add_gridspec(2, 2, height_ratios=[0.9, 1.1], hspace=0.19, wspace=0.18)

ax_flow = fig.add_subplot(grid[0, :])
ax_flow.set_xlim(0, 1)
ax_flow.set_ylim(0, 1)
ax_flow.axis("off")
ax_flow.text(
    0.5,
    0.98,
    "Fixed physical diffusion: exact finite return versus the infinite force budget",
    ha="center",
    va="top",
    fontsize=20,
    fontweight="bold",
    color="#12213a",
)

box(
    ax_flow,
    (0.035, 0.17),
    0.265,
    0.62,
    "1  Normalized finite packet",
    [
        r"common diffusion $\delta_*>0$",
        r"$Z(T)=0,\ \Omega_3(T)=0$",
        r"$\Theta_3(T)<0$",
        r"$\Omega_2/\sigma_2\geq 1/48$",
        r"$\log(-\Theta_3(T)/-\Theta_3(0))\geq 1/24$",
    ],
    "#245b8a",
    "#e8f1f8",
)
box(
    ax_flow,
    (0.37, 0.17),
    0.265,
    0.62,
    "2  Similarity at radius r",
    [
        r"$y=(x-x_*)/r$",
        r"$\tau=(t-t_*)/c$",
        r"$c=(\delta_*/d)r^2$",
        r"$d=(r^2/c)\delta_*$",
        r"fixed physical $d>0$ at every $r$",
    ],
    "#5a3d91",
    "#eee9f8",
)
box(
    ax_flow,
    (0.705, 0.17),
    0.26,
    0.62,
    "3  Exact receiving weights",
    [
        r"$\partial_x^\gamma\partial_t^b f_u:$",
        r"$(d/\delta_*)^{2+b}r^{-3-|\gamma|-2b}$",
        r"$\partial_x^\gamma\partial_t^b f_\theta:$",
        r"$(d/\delta_*)^{3+b}r^{-5-|\gamma|-2b}$",
        r"all derivatives retained",
    ],
    "#1f7158",
    "#e4f3ed",
)

for start, end in [((0.305, 0.48), (0.365, 0.48)), ((0.64, 0.48), (0.70, 0.48))]:
    ax_flow.add_patch(
        FancyArrowPatch(
            start,
            end,
            arrowstyle="-|>",
            mutation_scale=22,
            linewidth=2.4,
            color="#253552",
        )
    )

ax_plot = fig.add_subplot(grid[1, 0], facecolor="#fffdf8")
q = np.arange(1, 19)
raw_vector = 3 * q
corrected_vector = -(q**2) + 3 * q
corrected_scalar = -(q**2) + 5 * q
ax_plot.plot(q, raw_vector, color="#b4333b", linewidth=2.8, marker="o", label=r"raw vector term: $2^{3q}$")
ax_plot.plot(
    q,
    corrected_vector,
    color="#246a9a",
    linewidth=2.8,
    marker="s",
    label=r"target vector term: $2^{-q^2+3q}$",
)
ax_plot.plot(
    q,
    corrected_scalar,
    color="#24815f",
    linewidth=2.8,
    marker="^",
    label=r"target scalar term: $2^{-q^2+5q}$",
)
ax_plot.axhline(0, color="#6b7280", linewidth=1.1)
ax_plot.set_title(r"Zeroth-order variable exponents for $r_q=2^{-q}$", fontsize=14)
ax_plot.set_xlabel(r"packet index $q$")
ax_plot.set_ylabel(r"base-2 logarithm (fixed constants omitted)")
ax_plot.grid(True, alpha=0.23)
ax_plot.legend(loc="lower left", fontsize=10.5, frameon=True)
ax_plot.text(
    8.8,
    44,
    "raw copies grow",
    color="#9e2931",
    fontsize=11.5,
    fontweight="bold",
)
ax_plot.text(
    8.7,
    -123,
    "force-flat targets decay",
    color="#1d654e",
    fontsize=11.5,
    fontweight="bold",
)

ax_text = fig.add_subplot(grid[1, 1])
ax_text.set_xlim(0, 1)
ax_text.set_ylim(0, 1)
ax_text.axis("off")
box(
    ax_text,
    (0.035, 0.53),
    0.93,
    0.41,
    "Raw-copy obstruction",
    [
        r"at a retained nonzero force point:",
        r"$|f_{u,q}(x_q,s_q)|=a_\dagger(d/\delta_*)^2r_q^{-3}$",
        r"$\longrightarrow\infty$ as $r_q\downarrow0$",
        "the packet terms fail the local uniform term test",
    ],
    "#a12f38",
    "#fae9e8",
)
box(
    ax_text,
    (0.035, 0.02),
    0.93,
    0.43,
    "Force-flat target space",
    [
        r"for every $m$, sum the weighted jet maxima",
        r"a sufficient normalized size is $2^{-q^2}$",
        r"vector exponent: $-q^2+(3+2m)q$",
        r"scalar exponent: $-q^2+(5+2m)q$",
        "both series converge; state gluing is separate",
    ],
    "#1f7158",
    "#e5f4ed",
)

fig.text(
    0.5,
    0.016,
    "The similarity preserves the finite return.  The exact force weights identify the correction required for an infinite accumulation.",
    ha="center",
    va="bottom",
    fontsize=11.5,
    color="#35415a",
)

OUT.parent.mkdir(parents=True, exist_ok=True)
fig.savefig(OUT, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close(fig)
print(OUT)
