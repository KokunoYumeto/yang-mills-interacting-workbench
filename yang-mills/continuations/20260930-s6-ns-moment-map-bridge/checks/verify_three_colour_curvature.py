"""Exact symbolic checks for the three-colour Yang--Mills lift."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


I = sp.I
sigma = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -I], [I, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(-I * matrix / 2 for matrix in sigma)


def bracket(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return left * right - right * left


def coefficient(matrix: sp.Matrix, colour: int) -> sp.Expr:
    return sp.expand(-2 * sp.trace(T[colour] * matrix))


def is_zero(expression: sp.Expr) -> bool:
    return sp.simplify(sp.expand(expression)) == 0


lam = sp.symbols("lambda_1:4", nonzero=True)
c_light = sp.symbols("c", nonzero=True)

structure_checks: dict[str, bool] = {}
for a in range(3):
    for b in range(3):
        expected = sp.zeros(2)
        for colour in range(3):
            expected += sp.LeviCivita(a, b, colour) * T[colour]
        structure_checks[f"[{a + 1},{b + 1}]"] = bracket(T[a], T[b]) == expected

# One fixed spatial pair (i,j) verifies the general pair formula because all
# component symbols are algebraically independent.
u_i = sp.symbols("u_i_1:4")
u_j = sp.symbols("u_j_1:4")
d_i_u_j = sp.symbols("d_i_u_j_1:4")
d_j_u_i = sp.symbols("d_j_u_i_1:4")

A_i = sum((lam[a] * u_i[a] * T[a] for a in range(3)), sp.zeros(2))
A_j = sum((lam[a] * u_j[a] * T[a] for a in range(3)), sp.zeros(2))
derivative_part = sum(
    (lam[a] * (d_i_u_j[a] - d_j_u_i[a]) * T[a] for a in range(3)),
    sp.zeros(2),
)
F_ij = derivative_part + bracket(A_i, A_j)

B_expected: list[sp.Expr] = []
curvature_checks: dict[str, bool] = {}
for colour in range(3):
    value = lam[colour] * (d_i_u_j[colour] - d_j_u_i[colour])
    for a in range(3):
        for b in range(a + 1, 3):
            value += (
                sp.LeviCivita(a, b, colour)
                * lam[a]
                * lam[b]
                * (u_i[a] * u_j[b] - u_i[b] * u_j[a])
            )
    value = sp.expand(value)
    B_expected.append(value)
    curvature_checks[f"B_{colour + 1}"] = is_zero(coefficient(F_ij, colour) - value)

magnetic_density_check = is_zero(
    -2 * sp.trace(F_ij * F_ij) - sum(value * value for value in B_expected)
)

# Verify the time component after the divergence-free derivative term has
# vanished.  Three spatial indices are retained independently.
u = [[sp.symbols(f"u_{a + 1}_{i + 1}") for i in range(3)] for a in range(3)]
u_t = [[sp.symbols(f"u_t_{a + 1}_{i + 1}") for i in range(3)] for a in range(3)]
A = [
    sum((lam[a] * u[a][i] * T[a] for a in range(3)), sp.zeros(2))
    for i in range(3)
]
A_t = [
    sum((lam[a] * u_t[a][i] * T[a] for a in range(3)), sp.zeros(2))
    for i in range(3)
]
J0_matrix = sum((-bracket(A[i], A_t[i]) / c_light for i in range(3)), sp.zeros(2))

charge_checks: dict[str, bool] = {}
for colour in range(3):
    expected = 0
    for i in range(3):
        for a in range(3):
            for b in range(3):
                expected -= (
                    sp.LeviCivita(a, b, colour)
                    * lam[a]
                    * lam[b]
                    * u[a][i]
                    * u_t[b][i]
                    / c_light
                )
    charge_checks[f"J_0_{colour + 1}"] = is_zero(
        coefficient(J0_matrix, colour) - expected
    )

# Verify the spatial source coefficients with independent symbols for every
# retained term in sum_i(partial_i B_ij + [A_i,F_ij]).
B = [[sp.symbols(f"B_{i + 1}_{b + 1}") for b in range(3)] for i in range(3)]
dB = [[sp.symbols(f"dB_{i + 1}_{b + 1}") for b in range(3)] for i in range(3)]
u_tt = sp.symbols("u_tt_1:4")
Jj_matrix = sum(
    (-lam[colour] * u_tt[colour] * T[colour] / c_light**2 for colour in range(3)),
    sp.zeros(2),
)
for i in range(3):
    F_i_j = sum((B[i][b] * T[b] for b in range(3)), sp.zeros(2))
    Jj_matrix += sum((dB[i][b] * T[b] for b in range(3)), sp.zeros(2))
    Jj_matrix += bracket(A[i], F_i_j)

spatial_source_checks: dict[str, bool] = {}
for colour in range(3):
    expected = -lam[colour] * u_tt[colour] / c_light**2
    expected += sum(dB[i][colour] for i in range(3))
    for i in range(3):
        for a in range(3):
            for b in range(3):
                expected += (
                    sp.LeviCivita(a, b, colour)
                    * lam[a]
                    * u[a][i]
                    * B[i][b]
                )
    spatial_source_checks[f"J_j_{colour + 1}"] = is_zero(
        coefficient(Jj_matrix, colour) - expected
    )

one_colour_charge = [
    sp.simplify(
        coefficient(J0_matrix, colour).subs(
            {
                lam[1]: 0,
                lam[2]: 0,
            }
        )
    )
    for colour in range(3)
]
one_colour_charge_check = all(value == 0 for value in one_colour_charge)

checks = {
    "su2_structure_constants": structure_checks,
    "curvature_coefficients": curvature_checks,
    "magnetic_density": magnetic_density_check,
    "charge_coefficients": charge_checks,
    "spatial_source_coefficients": spatial_source_checks,
    "one_colour_charge_vanishes": one_colour_charge_check,
}


def every_boolean(value: object) -> list[bool]:
    if isinstance(value, bool):
        return [value]
    if isinstance(value, dict):
        result: list[bool] = []
        for child in value.values():
            result.extend(every_boolean(child))
        return result
    return []


result = {
    "schema": "three-colour-yang-mills-symbolic-check-v1",
    "date": "2026-09-29",
    "computer_algebra": f"sympy-{sp.__version__}",
    "normalization": {
        "generators": "T_a=-i sigma_a/2",
        "bracket": "[T_a,T_b]=epsilon_abc T_c",
        "trace": "-2 tr(T_a T_b)=delta_ab",
        "metric": "diag(-1,1,1,1)",
        "time_coordinate": "x^0=c t",
    },
    "checks": checks,
}
result["all_passed"] = all(every_boolean(checks))

output = Path(__file__).with_name("THREE_COLOUR_CURVATURE_CHECK.json")
output.write_text(
    json.dumps(result, indent=2, sort_keys=True) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(result, indent=2, sort_keys=True))

if not result["all_passed"]:
    raise SystemExit(1)
