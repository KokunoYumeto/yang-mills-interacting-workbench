"""Exact algebra and margins registered with the cumulative reader."""

from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path

import sympy as sp


HERE = Path(__file__).resolve().parent
OUT = HERE / "third_return_persistence_receipt.json"

chi, p, o = sp.symbols("chi p o", nonzero=True)
K, forcing, delta, R = sp.symbols("K forcing delta R")
pprime = K * o - delta * R * p
oprime = forcing * p - delta * R * o
v = o / (chi * p)

quotient_residual = sp.simplify(
    (oprime * p - o * pprime) / (chi * p**2)
    - (forcing / chi - chi * K * v**2)
)
gain_residual = sp.simplify(pprime / p - (chi * K * v - delta * R))
assert quotient_residual == 0
assert gain_residual == 0

Cdelta = Q(1, 4)
v_at_one = (1 - Cdelta) / 2
f0 = v_at_one - Cdelta
f3 = Q(2) - Q(3)
parent0 = Q(1, 3) - Cdelta
gain0 = (1 - Cdelta) * Q(2, 9)

assert (v_at_one, f0, f3, parent0, gain0) == (
    Q(3, 8), Q(1, 8), Q(-1), Q(1, 12), Q(1, 6)
)
assert f0 - Q(1, 16) == Q(1, 16)
assert f3 + Q(1, 16) == Q(-15, 16)
assert parent0 / 2 - Q(1, 48) == Q(1, 48)
assert gain0 / 2 - Q(1, 24) == Q(1, 24)

receipt = {
    "schema": "third-return-persistence-reader-check-v1",
    "status": "pass",
    "exact_pair_to_quotient": True,
    "exact_pair_to_gain": True,
    "source_margins": {
        "F0_at_m0_lower": "1/8",
        "F0_at_m3_upper": "-1",
        "parent_at_root_lower": "1/12",
        "gain_at_root_lower": "1/6",
    },
    "persisted_margins": {
        "Fd_at_m0_lower": "1/16",
        "Fd_at_m3_upper": "-15/16",
        "parent_at_root_lower": "1/48",
        "gain_at_root_lower": "1/24",
    },
    "proof": "third_return/third_return_completion_body.tex",
}
OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt, indent=2))
