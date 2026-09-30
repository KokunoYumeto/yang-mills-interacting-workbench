from pathlib import Path

import matplotlib.colors as colors
import matplotlib.pyplot as plt
import numpy as np


OUT = Path(__file__).with_suffix(".png")


def main() -> None:
    carriers = np.arange(-3, 4)
    matrix = np.zeros((len(carriers), len(carriers)), dtype=int)
    labels = np.full(matrix.shape, "0", dtype=object)
    for i, n in enumerate(carriers):
        for j, m in enumerate(carriers):
            if n == 0 and m == 0:
                matrix[i, j] = 3
                labels[i, j] = "Z"
            elif n == m:
                matrix[i, j] = 1
                labels[i, j] = "S"
            elif n == -m:
                matrix[i, j] = 2
                labels[i, j] = "O"

    cmap = colors.ListedColormap(["#f6f3ec", "#447da0", "#a9658c", "#d18b37"])
    norm = colors.BoundaryNorm([-0.5, 0.5, 1.5, 2.5, 3.5], cmap.N)
    fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(13.5, 6.2), gridspec_kw={"width_ratios": [1.25, 1]})
    fig.patch.set_facecolor("#fbfaf6")

    ax0.imshow(matrix, cmap=cmap, norm=norm, origin="lower")
    ax0.set_xticks(range(len(carriers)), carriers)
    ax0.set_yticks(range(len(carriers)), carriers)
    ax0.set_xlabel(r"second carrier $m$")
    ax0.set_ylabel(r"first carrier $n$")
    ax0.set_title("Unfolded carrier selection matrix", pad=12)
    for i in range(len(carriers)):
        for j in range(len(carriers)):
            color = "white" if matrix[i, j] else "#8c8c8c"
            ax0.text(j, i, labels[i, j], ha="center", va="center", color=color, fontsize=11, weight="bold")
    ax0.text(
        0.5,
        -0.16,
        r"S: $\frac{1}{2}\Re(x\bar y)$   O: $\frac{1}{2}\Re(xy)$   Z: $\Re x\,\Re y$",
        transform=ax0.transAxes,
        ha="center",
        fontsize=11,
    )

    ax1.axis("off")
    ax1.set_xlim(0, 1)
    ax1.set_ylim(0, 1)
    ax1.set_title(r"Folding by $|n|$", pad=12)
    y_values = [0.82, 0.62, 0.42, 0.22]
    block_labels = [
        (r"$n=0$", r"$G^{(0)}=J_{r_0}$", "#d18b37"),
        (r"$n=\pm1$", r"$G^{(1)}=\frac{1}{2}J_{r_1}$", "#447da0"),
        (r"$n=\pm2$", r"$G^{(2)}=\frac{1}{2}J_{r_2}$", "#447da0"),
        (r"$n=\pm3$", r"$G^{(3)}=\frac{1}{2}J_{r_3}$", "#447da0"),
    ]
    for y, (left, right, color) in zip(y_values, block_labels, strict=True):
        ax1.add_patch(plt.Rectangle((0.05, y - 0.07), 0.90, 0.14, facecolor=color, alpha=0.16, edgecolor=color, lw=2))
        ax1.text(0.10, y, left, va="center", fontsize=14, color="#222222")
        ax1.text(0.90, y, right, va="center", ha="right", fontsize=14, color=color)
    ax1.text(0.5, 0.075, r"$J_r$ is the $r\times r$ all-ones matrix.", ha="center", fontsize=11)
    ax1.text(0.5, 0.025, "Different absolute carriers have exactly zero angular product.", ha="center", fontsize=11)

    fig.suptitle("Exact finite angular Gram blocks", fontsize=18, y=0.98)
    fig.tight_layout(rect=(0, 0.03, 1, 0.94))
    fig.savefig(OUT, dpi=180, bbox_inches="tight", facecolor=fig.get_facecolor())
    print(OUT)


if __name__ == "__main__":
    main()
