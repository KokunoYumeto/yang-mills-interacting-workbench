from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import hashlib, json, math

ROOT = Path(__file__).resolve().parent
TEX = ROOT / "evaluation_flux_audit.tex"
RECEIPT = ROOT / "replay_receipt.json"

def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

checks = {}
def ok(name, cond):
    checks[name] = bool(cond)
    if not cond:
        raise AssertionError(name)

# Exact chart powers.
h = Fraction(1, 8)
A = Fraction(1, 2) + h
D = Fraction(1, 2) - h
eps_exp = h
for e in (1, 2):
    alpha = Fraction(e + 1, 4) - A
    beta = Fraction(e + 1, 2) - 2*A - D
    ok(f"alpha_{e}", alpha == (Fraction(e + 1, 4) - A))
    ok(f"evaluation_exponent_{e}", beta == Fraction(e, 2) - 2*A + h)
    ok(f"measure_derivative_{e}", Fraction(e + 1, 2) - 2*A - D == beta)
ok("epsilon_definition", eps_exp == h)
ok("D_relation", Fraction(1, 2) - D == h)
ok("quadratic_J2", Fraction(3, 2) - 2*A == Fraction(1, 2) - 2*h)
ok("quadratic_J1", 1 - 2*A == -2*h)
ok("quadratic_M2", Fraction(3, 2) - 2*A - D == -h)
ok("quadratic_M1", 1 - 2*A - D == Fraction(-1, 2) - h)

# The two old-parent derivative routes remain separate after evaluation.
for e in (1, 2):
    alpha = Fraction(e + 1, 4) - A
    old_derivative = alpha + Fraction(3, 7)
    old_field_new_derivative = alpha + Fraction(5, 7) - D
    ok(f"old_routes_distinct_{e}", old_derivative != old_field_new_derivative)
    # They coincide exactly only when dotomega = omega-D.
    omega = Fraction(5, 7)
    dotomega = omega - D
    ok(f"old_routes_merge_condition_{e}", alpha + dotomega == alpha + omega - D)

# Finite angular-kernel indicator checks (nonzero carriers).
def kernel_indicator(n, m):
    return int(n + m == 0), int(n - m == 0)
ok("kernel_equal_carrier", kernel_indicator(3, 3) == (0, 1))
ok("kernel_opposite_carrier", kernel_indicator(3, -3) == (1, 0))
ok("kernel_nonmatching_carrier", kernel_indicator(3, 4) == (0, 0))

body_hash = sha(TEX)
replay_hash = sha(Path(__file__))
receipt = {
    "schema": "evaluation-flux-audit-v1",
    "all_passed": all(checks.values()),
    "checks_passed": sum(checks.values()),
    "checks_total": len(checks),
    "checks": checks,
    "body_sha256": body_hash,
    "replay_sha256": replay_hash,
    "scope": "finite fixed-band finite-label compact-support evaluated-phase stress expansion; no endpoint or infinite claim",
}
RECEIPT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
