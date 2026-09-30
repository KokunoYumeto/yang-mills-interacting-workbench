"""Exact local algebra checks for the retained Sp(1) bundle bridge."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "SP1_BUNDLE_BRIDGE_CHECK.json"


def matrix_zero(matrix: sp.Matrix) -> bool:
    return all(sp.simplify(value) == 0 for value in matrix)


imaginary = sp.I
sigma = [
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -imaginary], [imaginary, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
]
T = [sp.simplify(-imaginary * value / 2) for value in sigma]
phi_basis = [2 * value for value in T]

epsilon = sp.LeviCivita
checks: dict[str, bool] = {}

for a in range(3):
    for b in range(3):
        commutator = phi_basis[a] * phi_basis[b] - phi_basis[b] * phi_basis[a]
        expected = sp.zeros(2)
        for c in range(3):
            expected += 2 * epsilon(a, b, c) * phi_basis[c]
        checks[f"phi_bracket_{a + 1}_{b + 1}"] = matrix_zero(
            sp.simplify(commutator - expected)
        )

for a in range(3):
    for b in range(3):
        metric = sp.simplify(-2 * sp.trace(phi_basis[a] * phi_basis[b]))
        checks[f"phi_metric_{a + 1}_{b + 1}"] = metric == 4 * int(a == b)

beta = sp.symbols("beta", real=True)
local_commutator = sp.simplify(
    (beta * phi_basis[0]) * (beta * phi_basis[1])
    - (beta * phi_basis[1]) * (beta * phi_basis[0])
)
expected_local = sp.simplify(2 * beta**2 * phi_basis[2])
checks["local_nonabelian_curvature_coefficient"] = matrix_zero(
    local_commutator - expected_local
)
checks["local_su2_curvature_is_4_beta2_T3"] = matrix_zero(
    local_commutator - 4 * beta**2 * T[2]
)

x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
chi = sp.Function("chi")(x1, x2, x3)
f = chi * x2
h = -chi * x1
w = sp.Matrix([sp.diff(f, x2), -sp.diff(f, x1), 0])
z = sp.Matrix([sp.diff(h, x2), -sp.diff(h, x1), 0])
div_w = sp.simplify(sp.diff(w[0], x1) + sp.diff(w[1], x2) + sp.diff(w[2], x3))
div_z = sp.simplify(sp.diff(z[0], x1) + sp.diff(z[1], x2) + sp.diff(z[2], x3))
checks["w_is_divergence_free"] = div_w == 0
checks["z_is_divergence_free"] = div_z == 0

constant_substitution = {
    chi: 1,
    sp.diff(chi, x1): 0,
    sp.diff(chi, x2): 0,
    sp.diff(chi, x3): 0,
}
w_core = sp.simplify(w.subs(constant_substitution))
z_core = sp.simplify(z.subs(constant_substitution))
checks["w_core_is_e1"] = w_core == sp.Matrix([1, 0, 0])
checks["z_core_is_e2"] = z_core == sp.Matrix([0, 1, 0])

all_passed = all(checks.values())
if not all_passed:
    failed = sorted(name for name, value in checks.items() if not value)
    raise AssertionError(f"failed checks: {failed}")

source_bytes = Path(__file__).read_bytes()
receipt = {
    "schema": "sp1-bundle-bridge-exact-check-v1",
    "checked_utc": datetime.now(timezone.utc).isoformat(),
    "sympy_version": sp.__version__,
    "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
    "normalization": {
        "T_a": "-i sigma_a / 2",
        "phi_quaternion_basis": "(i,j,k) -> 2(T_1,T_2,T_3)",
        "quaternion_bracket": "[i,j]=2k and cyclic permutations",
    },
    "checks": checks,
    "derived_local_values": {
        "w_on_chi_equals_one_region": [str(value) for value in w_core],
        "z_on_chi_equals_one_region": [str(value) for value in z_core],
        "phi_curvature_matrix": sp.sstr(local_commutator),
    },
    "all_passed": all_passed,
    "scope": (
        "Exact local Lie-algebra, metric-factor, curl-divergence, and "
        "commutator-curvature checks. Topological bundle results are proved "
        "in the retained TeX source and the bridge note."
    ),
}
OUTPUT.write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(receipt, indent=2, ensure_ascii=False))
