"""Exact replay for the based-cascade residual and state interface."""

from __future__ import annotations

from fractions import Fraction
from itertools import product
import hashlib
import json
import math
from pathlib import Path
import re


HERE = Path(__file__).resolve().parent
PROOF = HERE.parent / "based_cascade_body.tex"
OUT = HERE / "based_cascade_receipt.json"


Weight = tuple[int, int]  # exact powers of (rho,c)
MultiIndex = tuple[int, int, int]
Polynomial = dict[MultiIndex, int]


def add(*weights: Weight) -> Weight:
    return tuple(sum(weight[j] for weight in weights) for j in range(2))  # type: ignore[return-value]


def clock_radius_power(weight: Weight) -> int:
    """Substitute c=(delta_*/d)rho^2 and return the rho exponent."""
    return weight[0] + 2 * weight[1]


def multiindices(max_total: int) -> list[MultiIndex]:
    return [
        (a, b, c)
        for a in range(max_total + 1)
        for b in range(max_total + 1 - a)
        for c in range(max_total + 1 - a - b)
    ]


def falling(n: int, k: int) -> int:
    if k > n:
        return 0
    value = 1
    for j in range(k):
        value *= n - j
    return value


def derivative_value(poly: Polynomial, alpha: MultiIndex,
                     point: tuple[Fraction, Fraction, Fraction]) -> Fraction:
    total = Fraction(0)
    for exponent, coefficient in poly.items():
        factors = [falling(exponent[j], alpha[j]) for j in range(3)]
        if 0 in factors:
            continue
        term = Fraction(coefficient)
        for j in range(3):
            term *= factors[j] * point[j] ** (exponent[j] - alpha[j])
        total += term
    return total


def multiply(left: Polynomial, right: Polynomial) -> Polynomial:
    answer: Polynomial = {}
    for left_exp, left_coefficient in left.items():
        for right_exp, right_coefficient in right.items():
            exponent = tuple(left_exp[j] + right_exp[j] for j in range(3))
            answer[exponent] = answer.get(exponent, 0) + left_coefficient * right_coefficient
    return answer


def differentiate(poly: Polynomial, coordinate: int, times: int = 1) -> Polynomial:
    answer = dict(poly)
    for _ in range(times):
        next_answer: Polynomial = {}
        for exponent, coefficient in answer.items():
            if exponent[coordinate] == 0:
                continue
            new_exponent = list(exponent)
            multiplier = new_exponent[coordinate]
            new_exponent[coordinate] -= 1
            key = tuple(new_exponent)
            next_answer[key] = next_answer.get(key, 0) + multiplier * coefficient
        answer = next_answer
    return answer


def subindices(alpha: MultiIndex) -> list[MultiIndex]:
    return list(product(*(range(component + 1) for component in alpha)))  # type: ignore[return-value]


def multi_binomial(alpha: MultiIndex, beta: MultiIndex) -> int:
    return math.prod(math.comb(alpha[j], beta[j]) for j in range(3))


checks: dict[str, object] = {}

# Exact physical similarity weights.  Diffusion retains its full rho^2/c factor.
theta = (1, -2)
velocity = (1, -1)
pressure = (2, -2)
diffusion = (2, -1)
space = (-1, 0)
time = (0, -1)
scalar_residual = (1, -3)
vector_residual = (1, -2)
parent_velocity = velocity
parent_gradient_velocity = add(velocity, space)
parent_gradient_theta = add(theta, space)

scalar_terms = {
    "time": add(theta, time),
    "parent_transport": add(parent_velocity, theta, space),
    "parent_gradient": add(velocity, parent_gradient_theta),
    "self_transport": add(velocity, theta, space),
    "diffusion": add(diffusion, theta, space, space),
}
vector_terms = {
    "time": add(velocity, time),
    "parent_transport": add(parent_velocity, velocity, space),
    "parent_gradient": add(velocity, parent_gradient_velocity),
    "self_transport": add(velocity, velocity, space),
    "pressure": add(pressure, space),
    "diffusion": add(diffusion, velocity, space, space),
    "buoyancy": theta,
}
checks["scalar_residual_terms"] = scalar_terms
checks["vector_residual_terms"] = vector_terms
checks["all_scalar_weights_exact"] = set(scalar_terms.values()) == {scalar_residual}
checks["all_vector_weights_exact"] = set(vector_terms.values()) == {vector_residual}

# U=(c/rho)u, D=c grad u, and G=c^2 grad theta are dimensionless.
normalized_parent = {
    "U": add((-1, 1), parent_velocity),
    "D": add((0, 1), parent_gradient_velocity),
    "G": add((0, 2), parent_gradient_theta),
}
checks["normalized_parent_weights"] = normalized_parent
checks["normalized_parent_dimensionless"] = set(normalized_parent.values()) == {(0, 0)}

parent_jet_cases = 0
force_jet_cases = 0
for b in range(7):
    for g in range(7):
        u_parent_weight = (g - 1, b + 1)
        d_parent_weight = (g, b + 1)
        g_parent_weight = (g, b + 2)
        assert clock_radius_power(u_parent_weight) == g + 2 * b + 1
        assert clock_radius_power(d_parent_weight) == g + 2 * b + 2
        assert clock_radius_power(g_parent_weight) == g + 2 * b + 4
        parent_jet_cases += 3

        scalar_jet = add(scalar_residual, (-g, -b))
        vector_jet = add(vector_residual, (-g, -b))
        assert clock_radius_power(scalar_jet) == -5 - g - 2 * b
        assert clock_radius_power(vector_jet) == -3 - g - 2 * b
        force_jet_cases += 2
checks["parent_jet_cases"] = parent_jet_cases
checks["force_jet_cases"] = force_jet_cases
checks["all_parent_and_force_jet_powers"] = True

# The inverse state interface has the three exact physical scale factors.
inverse_interface = {
    "velocity": (1, -1),
    "velocity_gradient": (0, -1),
    "temperature_gradient": (0, -2),
}
checks["state_interface_radius_powers"] = {
    name: clock_radius_power(weight) for name, weight in inverse_interface.items()
}
checks["state_interface_exact"] = checks["state_interface_radius_powers"] == {
    "velocity": -1,
    "velocity_gradient": -2,
    "temperature_gradient": -4,
}

# Replay the three-index Leibniz convolution against exact polynomial derivatives.
polynomial_pairs: list[tuple[Polynomial, Polynomial]] = [
    (
        {(0, 0, 0): 2, (7, 1, 0): -3, (2, 6, 2): 5, (3, 2, 7): 11},
        {(1, 0, 5): 7, (0, 7, 1): -2, (5, 3, 2): 13, (2, 1, 0): -5},
    ),
    (
        {(6, 2, 1): 4, (1, 5, 4): -9, (0, 0, 3): 6, (4, 4, 4): 1},
        {(3, 6, 0): -8, (5, 0, 3): 3, (2, 2, 6): 10, (0, 1, 1): 12},
    ),
    (
        {(7, 7, 0): 1, (0, 4, 7): 2, (5, 1, 5): -4, (1, 1, 1): 9},
        {(4, 0, 6): 5, (6, 5, 1): -7, (1, 7, 3): 8, (0, 0, 0): -6},
    ),
]
evaluation_point = (Fraction(2, 3), Fraction(-3, 5), Fraction(5, 7))
convolution_cases = 0
for left, right in polynomial_pairs:
    full_product = multiply(left, right)
    for alpha in multiindices(6):
        direct = derivative_value(full_product, alpha, evaluation_point)
        replay = Fraction(0)
        for beta in subindices(alpha):
            complement = tuple(alpha[j] - beta[j] for j in range(3))
            replay += (
                multi_binomial(alpha, beta)
                * derivative_value(left, beta, evaluation_point)
                * derivative_value(right, complement, evaluation_point)
            )
        assert direct == replay
        convolution_cases += 1
checks["leibniz_convolution_cases"] = convolution_cases
checks["all_three_index_convolutions"] = True

# Replay first and second derivative shifts used for gradient and Laplacian arrays.
shift_cases = 0
probe = multiply(polynomial_pairs[0][0], polynomial_pairs[1][1])
for alpha in multiindices(5):
    for coordinate in range(3):
        first_shift = list(alpha)
        first_shift[coordinate] += 1
        first_shift_tuple = tuple(first_shift)
        assert derivative_value(
            differentiate(probe, coordinate), alpha, evaluation_point
        ) == derivative_value(
            probe, first_shift_tuple, evaluation_point
        )
        shift_cases += 1
        if coordinate < 2:
            second_shift = list(alpha)
            second_shift[coordinate] += 2
            second_shift_tuple = tuple(second_shift)
            assert derivative_value(
                differentiate(probe, coordinate, times=2), alpha, evaluation_point
            ) == derivative_value(
                probe, second_shift_tuple, evaluation_point
            )
            shift_cases += 1
checks["shift_cases"] = shift_cases
checks["first_and_second_shifts"] = True

# Verify that the written theorem contains every exact term and no malformed row ending.
proof_text = PROOF.read_text(encoding="utf-8-sig")
required_fragments = [
    r"+u^{<q}\!\cdot\nabla\vartheta_q",
    r"+v_q\!\cdot\nabla\theta^{<q}",
    r"+(v_q\!\cdot\nabla)u^{<q}",
    r"-\vartheta_qe_2",
    r"+\widetilde v_q\cdot\mathcal G_q",
    r"+\mathcal D_q\widetilde v_q",
    r"(\mathsf U_i+\mathsf V_i)\star S_i\mathsf T",
    r"\mathsf V_i\star\mathsf G_i",
    r"\mathsf D_{ki}\star\mathsf V_i",
    r"S_i^2=S_i\circ S_i",
    r"\mathbf1_{k=2}\mathsf T",
]
missing_fragments = [fragment for fragment in required_fragments if fragment not in proof_text]
checks["required_formula_fragments"] = len(required_fragments)
checks["missing_formula_fragments"] = missing_fragments
checks["formula_inventory_complete"] = not missing_fragments

single_backslash_lines = [
    number
    for number, line in enumerate(proof_text.splitlines(), start=1)
    if line.rstrip().endswith("\\") and not line.rstrip().endswith("\\\\")
]
checks["single_backslash_line_endings"] = single_backslash_lines
checks["tex_row_endings_well_formed"] = not single_backslash_lines
checks["missing_qquad_typo_absent"] = ",qquad" not in proof_text

labels = re.findall(r"\\label\{([^}]+)\}", proof_text)
checks["label_count"] = len(labels)
checks["labels_unique"] = len(labels) == len(set(labels))

for name, value in checks.items():
    if isinstance(value, bool):
        assert value, name

proof_sha256 = hashlib.sha256(PROOF.read_bytes()).hexdigest()
receipt = {
    "schema": "based-cascade-check-v1",
    "status": "pass",
    "checks": checks,
    "exact_formulas": {
        "clock": "c_q=(delta_*/d) rho_q^2",
        "normalized_parent": ["U=(c/rho)u", "D=c grad u", "G=c^2 grad theta"],
        "parent_radius_powers": ["|gamma|+2b+1", "|gamma|+2b+2", "|gamma|+2b+4"],
        "state_interface_radius_powers": [-1, -2, -4],
        "target_normalized_residual": "max_{|alpha|<=q} ||partial^alpha actual signed residual||_infty <= 2^(-q^2); unsigned E is sufficient only",
    },
    "proof": "infinite_modified/based_cascade_body.tex",
    "proof_sha256": proof_sha256,
}
OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
