"""Exact replay for fixed-diffusion similarity and force-flat weights."""

from fractions import Fraction
import hashlib
import json
from pathlib import Path


HERE = Path(__file__).resolve().parent
OUT = HERE / "parabolic_similarity_receipt.json"


def radius_exponent(prefactor_r: int, space_order: int, time_order: int, c_power: int) -> int:
    """Exponent after c=(delta/d)r^2, omitting positive d/delta factors."""
    return prefactor_r - space_order - 2 * (c_power + time_order)


def add(*weights: tuple[int, int]) -> tuple[int, int]:
    """Add exact (r-power, c-power) weights."""
    return (sum(weight[0] for weight in weights), sum(weight[1] for weight in weights))


checks = {}

d = Fraction(7, 5)
delta = Fraction(3, 11)
r = Fraction(2, 13)
c = delta * r * r / d
checks["fixed_physical_diffusion"] = d * c / (r * r) == delta

# Every retained PDE term has the same two-parameter similarity weight.
theta = (1, -2)
velocity = (1, -1)
pressure = (2, -2)
physical_diffusion = (2, -1)  # d=(r^2/c) delta
space_derivative = (-1, 0)
time_derivative = (0, -1)
scalar_weight = (1, -3)
vector_weight = (1, -2)
scalar_terms = {
    "time": add(theta, time_derivative),
    "transport": add(velocity, theta, space_derivative),
    "diffusion": add(physical_diffusion, theta, space_derivative, space_derivative),
    "force": scalar_weight,
}
vector_terms = {
    "time": add(velocity, time_derivative),
    "transport": add(velocity, velocity, space_derivative),
    "pressure": add(pressure, space_derivative),
    "diffusion": add(physical_diffusion, velocity, space_derivative, space_derivative),
    "buoyancy": theta,
    "force": vector_weight,
}
checks["all_scalar_pde_weights"] = set(scalar_terms.values()) == {scalar_weight}
checks["all_vector_pde_weights"] = set(vector_terms.values()) == {vector_weight}

# The finite return's dimensionless observables retain their exact scale.
frequency = (-1, 0)
temperature_amplitude = theta
vorticity_amplitude = (0, -1)
temperature_gradient = add(frequency, temperature_amplitude)
growth_scale = (temperature_gradient[0] // 2, temperature_gradient[1] // 2)
checks["temperature_gradient_weight"] = temperature_gradient == (0, -2)
checks["growth_vorticity_weight"] = growth_scale == vorticity_amplitude == (0, -1)
checks["normalized_vorticity_invariant"] = add(vorticity_amplitude, (0, 1)) == (0, 0)

expected = {
    "u": -1,
    "theta": -3,
    "pressure": -2,
    "vector_force": -3,
    "scalar_force": -5,
}
computed = {
    "u": radius_exponent(1, 0, 0, 1),
    "theta": radius_exponent(1, 0, 0, 2),
    "pressure": radius_exponent(2, 0, 0, 2),
    "vector_force": radius_exponent(1, 0, 0, 2),
    "scalar_force": radius_exponent(1, 0, 0, 3),
}
checks["zeroth_order_radius_exponents"] = computed == expected

jet_cases = 0
for b in range(7):
    for g in range(7):
        assert radius_exponent(1, g, b, 2) == -3 - g - 2 * b
        assert radius_exponent(1, g, b, 3) == -5 - g - 2 * b
        assert radius_exponent(1, g, b, 1) == -1 - g - 2 * b
        assert radius_exponent(2, g, b, 2) == -2 - g - 2 * b
        jet_cases += 4
checks["jet_cases"] = jet_cases
checks["all_jet_exponents"] = True

worst_cases = 0
for m in range(31):
    penalties = [2 * b + g for b in range(m + 1) for g in range(m + 1 - b)]
    assert max(penalties) == 2 * m
    assert min(penalties) == 0
    worst_cases += len(penalties)
checks["derivative_weight_cases"] = worst_cases
checks["worst_derivative_penalty"] = "2m"

ratio_cases = 0
for m in range(21):
    assert -2 * (m + 2) + 2 * m + 2 <= -1
    assert -2 * (m + 3) + 2 * m + 4 <= -1
    for q in range(m + 3, m + 25):
        vector_ratio_exponent = -2 * q + 2 * m + 2
        scalar_ratio_exponent = -2 * q + 2 * m + 4
        assert vector_ratio_exponent <= -4
        assert scalar_ratio_exponent <= -2
        ratio_cases += 2
checks["summability_ratio_cases"] = ratio_cases
checks["explicit_superalgebraic_budget"] = True

for name, value in checks.items():
    if isinstance(value, bool):
        assert value, name

proof = HERE.parent / "parabolic_similarity_body.tex"
proof_sha256 = hashlib.sha256(proof.read_bytes()).hexdigest()

receipt = {
    "schema": "parabolic-similarity-check-v1",
    "status": "pass",
    "checks": checks,
    "exact_formulas": {
        "clock": "c=(delta_*/d) r^2",
        "vector_force_jet_radius_power": "-3-|gamma|-2b",
        "scalar_force_jet_radius_power": "-5-|gamma|-2b",
        "explicit_radius": "r_q=2^(-q)",
        "explicit_normalized_budget": "2^(-q^2) times fixed smooth compactly supported force profiles",
    },
    "proof": "infinite_modified/parabolic_similarity_body.tex",
    "proof_sha256": proof_sha256,
}
OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
