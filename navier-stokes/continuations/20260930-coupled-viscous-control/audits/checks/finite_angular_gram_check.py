from __future__ import annotations

import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "state" / "FINITE_ANGULAR_GRAM_CHECK.json"

Gaussian = tuple[Fraction, Fraction]
Vector = tuple[Gaussian, ...]


def gadd(x: Gaussian, y: Gaussian) -> Gaussian:
    return x[0] + y[0], x[1] + y[1]


def gneg(x: Gaussian) -> Gaussian:
    return -x[0], -x[1]


def gsub(x: Gaussian, y: Gaussian) -> Gaussian:
    return gadd(x, gneg(y))


def gmul(x: Gaussian, y: Gaussian) -> Gaussian:
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def gscale(q: Fraction, x: Gaussian) -> Gaussian:
    return q * x[0], q * x[1]


def gconj(x: Gaussian) -> Gaussian:
    return x[0], -x[1]


def vzero(dim: int) -> Vector:
    return tuple((Fraction(0), Fraction(0)) for _ in range(dim))


def vadd(x: Vector, y: Vector) -> Vector:
    return tuple(gadd(a, b) for a, b in zip(x, y, strict=True))


def vscale(q: Fraction, x: Vector) -> Vector:
    return tuple(gscale(q, a) for a in x)


def vconj(x: Vector) -> Vector:
    return tuple(gconj(a) for a in x)


def bdot(x: Vector, y: Vector) -> Gaussian:
    out: Gaussian = (Fraction(0), Fraction(0))
    for a, b in zip(x, y, strict=True):
        out = gadd(out, gmul(a, b))
    return out


def hdot_real(x: Vector, y: Vector) -> Fraction:
    return bdot(x, vconj(y))[0]


def real_vector(x: Vector) -> Vector:
    return tuple((a[0], Fraction(0)) for a in x)


def expand_real_modes(carriers: list[int], coeffs: list[Vector]) -> dict[int, Vector]:
    dim = len(coeffs[0])
    modes: dict[int, Vector] = defaultdict(lambda: vzero(dim))
    for n, h in zip(carriers, coeffs, strict=True):
        if n == 0:
            modes[0] = vadd(modes[0], real_vector(h))
        else:
            modes[n] = vadd(modes[n], vscale(Fraction(1, 2), h))
            modes[-n] = vadd(modes[-n], vscale(Fraction(1, 2), vconj(h)))
    return dict(modes)


def constant_dot(left: dict[int, Vector], right: dict[int, Vector]) -> Fraction:
    total: Gaussian = (Fraction(0), Fraction(0))
    for n, x in left.items():
        y = right.get(-n)
        if y is not None:
            total = gadd(total, bdot(x, y))
    assert total[1] == 0
    return total[0]


def fold(carriers: list[int], coeffs: list[Vector]) -> tuple[Vector, dict[int, Vector]]:
    dim = len(coeffs[0])
    zero = vzero(dim)
    blocks: dict[int, Vector] = defaultdict(lambda: vzero(dim))
    for n, h in zip(carriers, coeffs, strict=True):
        if n == 0:
            zero = vadd(zero, real_vector(h))
        elif n > 0:
            blocks[n] = vadd(blocks[n], h)
        else:
            blocks[-n] = vadd(blocks[-n], vconj(h))
    return zero, dict(blocks)


def folded_dot(
    carriers: list[int], left: list[Vector], right: list[Vector]
) -> Fraction:
    l0, lb = fold(carriers, left)
    r0, rb = fold(carriers, right)
    total = hdot_real(l0, r0)
    for ell in sorted(set(lb) | set(rb)):
        total += Fraction(1, 2) * hdot_real(
            lb.get(ell, vzero(len(l0))), rb.get(ell, vzero(len(r0)))
        )
    return total


def kernel(n: int, m: int, x: Gaussian, y: Gaussian) -> Fraction:
    out = Fraction(0)
    if n == m:
        out += Fraction(1, 2) * gmul(x, gconj(y))[0]
    if n == -m:
        out += Fraction(1, 2) * gmul(x, y)[0]
    return out


def scalar_single_average(n: int, m: int, x: Gaussian, y: Gaussian) -> Fraction:
    left = expand_real_modes([n], [((x[0], x[1]),)])
    right = expand_real_modes([m], [((y[0], y[1]),)])
    return constant_dot(left, right)


def affine_add(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]):
    return x[0] + y[0], x[1] + y[1]


def affine_sub(x: tuple[Fraction, Fraction], y: tuple[Fraction, Fraction]):
    return x[0] - y[0], x[1] - y[1]


def affine_scale(q: Fraction, x: tuple[Fraction, Fraction]):
    return q * x[0], q * x[1]


def affine_text(x: tuple[Fraction, Fraction]) -> str:
    a, b = x
    if b == 0:
        return str(a)
    if a == 0:
        return "h" if b == 1 else "-h" if b == -1 else f"{b}*h"
    sign = "+" if b > 0 else "-"
    mag = abs(b)
    tail = "h" if mag == 1 else f"{mag}*h"
    return f"{a}{sign}{tail}"


def make_coeffs(count: int, shift: int) -> list[Vector]:
    out: list[Vector] = []
    for j in range(count):
        row = []
        for c in range(3):
            real = Fraction(((-1) ** (j + c)) * (j + c + 2 + shift), 7 + c)
            imag = Fraction(((-1) ** c) * (2 * j - c + 1 + shift), 11 + j)
            row.append((real, imag))
        out.append(tuple(row))
    return out


def main() -> None:
    carriers = [0, 0, 1, 1, -1, 2, -2, 3, 5]
    h = make_coeffs(len(carriers), 0)
    d = make_coeffs(len(carriers), 3)

    modes_h = expand_real_modes(carriers, h)
    modes_d = expand_real_modes(carriers, d)
    fourier_hh = constant_dot(modes_h, modes_h)
    folded_hh = folded_dot(carriers, h, h)
    fourier_hd = constant_dot(modes_h, modes_d)
    folded_hd = folded_dot(carriers, h, d)

    pair_checks = []
    for j, n in enumerate(carriers):
        for k, m in enumerate(carriers):
            for component in range(3):
                lhs = scalar_single_average(n, m, h[j][component], d[k][component])
                rhs = kernel(n, m, h[j][component], d[k][component])
                pair_checks.append(lhs == rhs)

    h_plus_d = [vadd(x, y) for x, y in zip(h, d, strict=True)]
    h_minus_d = [vadd(x, vscale(Fraction(-1), y)) for x, y in zip(h, d, strict=True)]
    derivative_by_difference = Fraction(1, 2) * (
        folded_dot(carriers, h_plus_d, h_plus_d)
        - folded_dot(carriers, h_minus_d, h_minus_d)
    )
    derivative_by_product = 2 * folded_hd

    A = (Fraction(1, 2), Fraction(1))
    D = (Fraction(1, 2), Fraction(-1))
    alpha_2 = affine_sub((Fraction(3, 4), Fraction(0)), A)
    alpha_1 = affine_sub((Fraction(1, 2), Fraction(0)), A)
    exponents = {
        "velocity_e2": alpha_2,
        "axial_derivative_e2": affine_sub(alpha_2, D),
        "velocity_e1": alpha_1,
        "axial_derivative_e1": affine_sub(alpha_1, D),
        "J2_quadratic": affine_scale(Fraction(2), alpha_2),
        "M2_quadratic": affine_sub(affine_scale(Fraction(2), alpha_2), D),
        "J1_quadratic": affine_scale(Fraction(2), alpha_1),
        "M1_quadratic": affine_sub(affine_scale(Fraction(2), alpha_1), D),
    }
    expected = {
        "velocity_e2": (Fraction(1, 4), Fraction(-1)),
        "axial_derivative_e2": (Fraction(-1, 4), Fraction(0)),
        "velocity_e1": (Fraction(0), Fraction(-1)),
        "axial_derivative_e1": (Fraction(-1, 2), Fraction(0)),
        "J2_quadratic": (Fraction(1, 2), Fraction(-2)),
        "M2_quadratic": (Fraction(0), Fraction(-1)),
        "J1_quadratic": (Fraction(0), Fraction(-2)),
        "M1_quadratic": (Fraction(-1, 2), Fraction(-1)),
    }

    selection = []
    for n in range(-3, 4):
        row = []
        for m in range(-3, 4):
            if n == 0 and m == 0:
                row.append("zero")
            elif n == m:
                row.append("same")
            elif n == -m:
                row.append("opposite")
            else:
                row.append("vanish")
        selection.append(row)

    checks = {
        "fourier_norm_equals_folded_blocks": fourier_hh == folded_hh,
        "fourier_cross_equals_folded_blocks": fourier_hd == folded_hd,
        "all_pairwise_kernel_entries": all(pair_checks),
        "pairwise_kernel_check_count": len(pair_checks),
        "norm_derivative_product_rule": derivative_by_difference == derivative_by_product,
        "zero_nonzero_decoupling": all(
            kernel(0, n, h[0][0], d[2][0]) == 0 for n in (-3, -2, -1, 1, 2, 3)
        ),
        "all_chart_exponents": exponents == expected,
    }
    receipt = {
        "status": "pass" if all(v for k, v in checks.items() if not k.endswith("count")) else "fail",
        "arithmetic": "exact fractions in Q(i)",
        "carriers": carriers,
        "checks": checks,
        "computed_exponents": {k: affine_text(v) for k, v in exponents.items()},
        "selection_carriers": list(range(-3, 4)),
        "selection_matrix": selection,
        "proof_note": "editorial/finite_angular_gram_system.md",
    }
    OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=2))
    if receipt["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()

