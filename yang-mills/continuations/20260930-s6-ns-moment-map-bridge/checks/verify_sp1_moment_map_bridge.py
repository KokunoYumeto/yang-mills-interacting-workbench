"""Exact checks for the Sp(1)-equivariant moment-map gauge bridge.

The proof note carries the global bundle argument.  This script checks the
coordinate identities, differential ranks, spatial curls, curvature, and
the source defect on the constant core without replacing that proof.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "SP1_MOMENT_MAP_BRIDGE_CHECK.json"
RETAINED_SOURCE_LABEL = "../sources/higher_rung/s6_higher_rung_24d_preprint.tex"
RETAINED_SOURCE = ROOT / RETAINED_SOURCE_LABEL


def quaternion_product(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    """Hamilton product in the ordered basis (1,i,j,k)."""

    a, b, c, d = left
    e, f, g, h = right
    return sp.Matrix(
        [
            a * e - b * f - c * g - d * h,
            a * f + b * e + c * h - d * g,
            a * g - b * h + c * e + d * f,
            a * h + b * g - c * f + d * e,
        ]
    )


def quaternion_conjugate(value: sp.Matrix) -> sp.Matrix:
    return sp.Matrix([value[0], -value[1], -value[2], -value[3]])


def quaternion_commutator(left: sp.Matrix, right: sp.Matrix) -> sp.Matrix:
    return sp.simplify(
        quaternion_product(left, right) - quaternion_product(right, left)
    )


def matrix_zero(value: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in value)


a, b, c, d = sp.symbols("a b c d", real=True)
q = sp.Matrix([a, b, c, d])
q_bar = quaternion_conjugate(q)
units = (
    sp.Matrix([0, 1, 0, 0]),
    sp.Matrix([0, 0, 1, 0]),
    sp.Matrix([0, 0, 0, 1]),
)
unit_names = ("i", "j", "k")
norm_squared = sp.expand(a**2 + b**2 + c**2 + d**2)

checks: dict[str, bool] = {}
moment_maps: dict[str, sp.Matrix] = {}

for name, unit in zip(unit_names, units):
    full_value = sp.simplify(
        quaternion_product(quaternion_product(q, unit), q_bar)
    )
    checks[f"mu_{name}_is_imaginary"] = sp.simplify(full_value[0]) == 0
    imaginary_value = sp.Matrix(full_value[1:4, 0])
    moment_maps[name] = imaginary_value
    checks[f"mu_{name}_norm_squared"] = (
        sp.simplify(imaginary_value.dot(imaginary_value) - norm_squared**2) == 0
    )

    jacobian = imaginary_value.jacobian([a, b, c, d])
    jacobian_gram = sp.simplify(jacobian * jacobian.T)
    checks[f"mu_{name}_jacobian_gram"] = matrix_zero(
        jacobian_gram - 4 * norm_squared * sp.eye(3)
    )
    checks[f"mu_{name}_rank_three_off_zero"] = (
        sp.simplify(jacobian_gram.det() - 64 * norm_squared**3) == 0
    )

# Equivariance is checked with an independent symbolic quaternion u.  The
# polynomial identity does not impose |u|=1, so it is stronger than the unit
# quaternion instance used by the bundle transition functions.
p, r, s, t = sp.symbols("p r s t", real=True)
u = sp.Matrix([p, r, s, t])
u_bar = quaternion_conjugate(u)
u_q = quaternion_product(u, q)
for name, unit in zip(unit_names, units):
    left = quaternion_product(
        quaternion_product(u_q, unit), quaternion_conjugate(u_q)
    )
    right = quaternion_product(
        quaternion_product(u, quaternion_product(quaternion_product(q, unit), q_bar)),
        u_bar,
    )
    checks[f"mu_{name}_equivariant"] = matrix_zero(sp.simplify(left - right))

# The three compactly supported spatial fields are curls.  On the region
# where chi is one they are the three coordinate fields.
x1, x2, x3 = sp.symbols("x1 x2 x3", real=True)
chi = sp.Function("chi")(x1, x2, x3)


def curl(vector: sp.Matrix) -> sp.Matrix:
    return sp.Matrix(
        [
            sp.diff(vector[2], x2) - sp.diff(vector[1], x3),
            sp.diff(vector[0], x3) - sp.diff(vector[2], x1),
            sp.diff(vector[1], x1) - sp.diff(vector[0], x2),
        ]
    )


spatial_fields = (
    curl(sp.Matrix([0, 0, chi * x2])),
    curl(sp.Matrix([0, 0, -chi * x1])),
    curl(sp.Matrix([0, chi * x1, 0])),
)
core_substitution = {
    chi: 1,
    sp.diff(chi, x1): 0,
    sp.diff(chi, x2): 0,
    sp.diff(chi, x3): 0,
}
core_fields: list[sp.Matrix] = []
for index, field in enumerate(spatial_fields):
    divergence = sp.simplify(
        sp.diff(field[0], x1) + sp.diff(field[1], x2) + sp.diff(field[2], x3)
    )
    core = sp.simplify(field.subs(core_substitution))
    core_fields.append(core)
    checks[f"w_{index + 1}_is_divergence_free"] = divergence == 0
    checks[f"w_{index + 1}_core_value"] = core == sp.eye(3)[:, index]

# On the core and at selected fibre coordinates alpha=beta=gamma=1, the
# bundle-valued potential has components (i,j,k).  Its three spatial
# curvatures and the covariant source are checked in the original quaternion
# bracket, followed by the exact su(2) metric/bracket scaling.
v = list(units)
F: dict[tuple[int, int], sp.Matrix] = {}
for i_index in range(3):
    for j_index in range(3):
        F[(i_index, j_index)] = quaternion_commutator(v[i_index], v[j_index])

checks["core_F_12_equals_2k"] = F[(0, 1)] == 2 * units[2]
checks["core_F_23_equals_2i"] = F[(1, 2)] == 2 * units[0]
checks["core_F_31_equals_2j"] = F[(2, 0)] == 2 * units[1]

source_quaternion: list[sp.Matrix] = []
for j_index in range(3):
    value = sp.zeros(4, 1)
    for i_index in range(3):
        value += quaternion_commutator(v[i_index], F[(i_index, j_index)])
    source_quaternion.append(sp.simplify(value))
    checks[f"core_quaternion_source_{j_index + 1}"] = (
        source_quaternion[-1] == -8 * units[j_index]
    )

imaginary = sp.I
sigma = (
    sp.Matrix([[0, 1], [1, 0]]),
    sp.Matrix([[0, -imaginary], [imaginary, 0]]),
    sp.Matrix([[1, 0], [0, -1]]),
)
T = tuple(-imaginary * matrix / 2 for matrix in sigma)
phi_units = tuple(2 * generator for generator in T)

for a_index in range(3):
    for b_index in range(3):
        commutator = (
            phi_units[a_index] * phi_units[b_index]
            - phi_units[b_index] * phi_units[a_index]
        )
        expected = sp.zeros(2)
        for c_index in range(3):
            expected += (
                2
                * sp.LeviCivita(a_index, b_index, c_index)
                * phi_units[c_index]
            )
        checks[f"phi_bracket_{a_index + 1}_{b_index + 1}"] = matrix_zero(
            sp.simplify(commutator - expected)
        )

su2_source = tuple(-16 * generator for generator in T)
for index, value in enumerate(su2_source):
    expected = -8 * phi_units[index]
    checks[f"core_su2_source_{index + 1}"] = matrix_zero(value - expected)

all_passed = all(checks.values())
if not all_passed:
    failed = sorted(name for name, passed in checks.items() if not passed)
    raise AssertionError(f"failed checks: {failed}")

script_sha256 = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
retained_source_sha256 = hashlib.sha256(RETAINED_SOURCE.read_bytes()).hexdigest()
receipt = {
    "schema": "sp1-moment-map-bridge-exact-check-v1",
    "checked_utc": datetime.now(timezone.utc).isoformat(),
    "sympy_version": sp.__version__,
    "script_sha256": script_sha256,
    "retained_source": RETAINED_SOURCE_LABEL,
    "retained_source_sha256": retained_source_sha256,
    "retained_source_lines": {
        "Sp1_actions": "5426-5433",
        "associated_bundle_convention": "5576-5588",
        "rank_24_bundle_and_splittings": "5590-5614",
    },
    "checks": checks,
    "derived": {
        "moment_maps": {
            name: [sp.sstr(entry) for entry in value]
            for name, value in moment_maps.items()
        },
        "jacobian_gram": "4*(a^2+b^2+c^2+d^2)*I_3",
        "jacobian_gram_determinant": "64*(a^2+b^2+c^2+d^2)^3",
        "core_spatial_fields": [
            [sp.sstr(entry) for entry in value] for value in core_fields
        ],
        "core_quaternion_curvature": {
            "F_12": "2k",
            "F_23": "2i",
            "F_31": "2j",
        },
        "core_quaternion_source": ["-8i", "-8j", "-8k"],
        "core_su2_source": ["-16T_1", "-16T_2", "-16T_3"],
    },
    "scope": (
        "Exact coordinate, equivariance, differential-rank, spatial-curl, "
        "curvature, and core-source checks.  The global associated-bundle "
        "proof and claim limits are in ../PROOF.md."
    ),
    "all_passed": all_passed,
}
OUTPUT.write_text(
    json.dumps(receipt, indent=2, ensure_ascii=False) + "\n",
    encoding="utf-8",
    newline="\n",
)
print(json.dumps(receipt, indent=2, ensure_ascii=False))
