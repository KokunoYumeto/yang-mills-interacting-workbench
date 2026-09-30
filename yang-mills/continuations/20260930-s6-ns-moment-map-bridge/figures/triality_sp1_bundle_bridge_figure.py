"""Render the exact retained-cusp to bundle-valued SU(2) bridge."""

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch


ROOT = Path(__file__).resolve().parent
PNG = ROOT / "TRIALITY_SP1_BUNDLE_BRIDGE.png"
SVG = ROOT / "TRIALITY_SP1_BUNDLE_BRIDGE.svg"


def box(ax, xy, wh, text, face, edge="#243447", fontsize=10.5, lw=1.5):
    x, y = xy
    w, h = wh
    patch = FancyBboxPatch(
        (x, y),
        w,
        h,
        boxstyle="round,pad=0.012,rounding_size=0.018",
        facecolor=face,
        edgecolor=edge,
        linewidth=lw,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fontsize)
    return patch


def arrow(ax, start, end, label=None, color="#34495e", bend=0.0, fontsize=9.5):
    patch = FancyArrowPatch(
        start,
        end,
        arrowstyle="-|>",
        mutation_scale=13,
        linewidth=1.5,
        color=color,
        connectionstyle=f"arc3,rad={bend}",
    )
    ax.add_patch(patch)
    if label:
        mx = (start[0] + end[0]) / 2
        my = (start[1] + end[1]) / 2 + (0.035 if bend >= 0 else -0.04)
        ax.text(
            mx,
            my,
            label,
            ha="center",
            va="center",
            fontsize=fontsize,
            color=color,
            bbox=dict(facecolor="white", edgecolor="none", alpha=0.92, pad=1.5),
        )


fig, ax = plt.subplots(figsize=(15.2, 9.2), dpi=180)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
fig.patch.set_facecolor("#fbfcfe")
ax.set_facecolor("#fbfcfe")

ax.text(
    0.5,
    0.965,
    r"Retained $S^6$ cusp class $\longrightarrow$ bundle-valued non-Abelian $SU(2)$ family",
    ha="center",
    va="center",
    fontsize=18,
    fontweight="bold",
    color="#17202a",
)
ax.text(
    0.5,
    0.925,
    "Green boxes are proved at the stated scope; amber boxes are the next calculations.",
    ha="center",
    va="center",
    fontsize=10.5,
    color="#566573",
)

green = "#dff3e4"
blue = "#dceeff"
red = "#f9dddd"
amber = "#fff0c7"

box(
    ax,
    (0.035, 0.72),
    (0.24, 0.14),
    r"$H=p_3q_2:X\cong S^6\to S^4$" "\n" r"$[Hd]=\eta_4\eta_5\ne0\in\pi_6(S^4)$",
    green,
)
box(
    ax,
    (0.38, 0.72),
    (0.24, 0.14),
    r"$P_H=(\chi H)^*S^7\to X$" "\n" r"$c(P_H)\ne0\in\pi_5(\mathrm{Sp}(1))\cong\mathbf{Z}/2$",
    green,
)
box(
    ax,
    (0.72, 0.72),
    (0.245, 0.14),
    r"$\rho:\mathrm{Sp}(1)\hookrightarrow\mathrm{Spin}(8)$" "\n" r"$Q_H=P_H\times_\rho\mathrm{Spin}(8)$ is trivial" "\n" "the specified reduction is nontrivial",
    green,
    fontsize=9.8,
)
arrow(ax, (0.275, 0.79), (0.38, 0.79), "pull back Hopf")
arrow(ax, (0.62, 0.79), (0.72, 0.79), r"extend by $\rho$")

box(
    ax,
    (0.22, 0.47),
    (0.28, 0.15),
    r"$\mathcal{A}_H=P_H\times_{\mathrm{Ad}}\mathrm{Im}\,\mathbf{H}$" "\n" "oriented rank 3; order-two clutching" "\n" r"$[v,w]=2(v\times w)$",
    green,
)
box(
    ax,
    (0.56, 0.47),
    (0.30, 0.15),
    "No global fixed colour frame" "\n" r"$\mathcal{A}_H\not\cong X\times\mathbf{R}^3$" "\n" "no nowhere-zero section",
    red,
)
arrow(ax, (0.50, 0.72), (0.38, 0.62), r"associate by $\rm Ad$", bend=0.08)
arrow(ax, (0.50, 0.545), (0.56, 0.545), "exact obstruction", color="#a93226")

box(
    ax,
    (0.035, 0.22),
    (0.29, 0.15),
    r"$v\in\mathcal{U}_H$ on $X\times\mathbf{R}^3$" "\n" "compact spatial support" "\n" r"$\sum_i\partial_i v_i=0$",
    blue,
)
box(
    ax,
    (0.365, 0.22),
    (0.29, 0.15),
    "Explicit two-direction seed" "\n" r"$v_1=\beta\mathbf{i},\ v_2=\beta\mathbf{j}$ locally" "\n" r"$\mathcal{F}_{12}=2\beta^2\mathbf{k}\ne0$",
    green,
)
box(
    ax,
    (0.695, 0.22),
    (0.27, 0.15),
    r"$\varphi(\mathbf{i},\mathbf{j},\mathbf{k})=2(T_1,T_2,T_3)$" "\n" r"$F_{ij}=\varphi(\mathcal{F}_{ij})$" "\n" r"$-2\mathrm{tr}(F_{ij}^2)=4\|\mathcal{F}_{ij}\|^2$",
    green,
    fontsize=9.8,
)
arrow(ax, (0.34, 0.47), (0.18, 0.37), "pull back to product", bend=0.08)
arrow(ax, (0.325, 0.295), (0.365, 0.295), "construct")
arrow(ax, (0.655, 0.295), (0.695, 0.295), r"Lie map $\varphi$")

box(
    ax,
    (0.11, 0.035),
    (0.23, 0.105),
    "Attach the soft-period end" "\n" "and prove cusp compatibility",
    amber,
)
box(
    ax,
    (0.385, 0.035),
    (0.23, 0.105),
    r"Solve $D^\mu F_{\mu\nu}=0$" "\n" "or retain the exact source defect",
    amber,
)
box(
    ax,
    (0.66, 0.035),
    (0.23, 0.105),
    "Build physical states" "\n" "and test low positive spectrum",
    amber,
)
arrow(ax, (0.51, 0.22), (0.225, 0.14), color="#b9770e", bend=-0.09)
arrow(ax, (0.51, 0.22), (0.50, 0.14), color="#b9770e")
arrow(ax, (0.80, 0.22), (0.775, 0.14), color="#b9770e")

plt.tight_layout(pad=0.6)
fig.savefig(PNG, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
fig.savefig(SVG, bbox_inches="tight", facecolor=fig.get_facecolor())
plt.close(fig)

print(PNG)
print(SVG)
