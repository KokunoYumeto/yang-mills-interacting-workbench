#!/usr/bin/env python3
"""Small exact-arithmetic intake checker; no coefficient regeneration or enumeration.

Usage:
    python check_response_certificates.py --source-dir PATH [--output PATH]

PATH must contain the three unchanged files named in EXPECTED_HASHES.  Uses only
Python's standard library.  The output receipt has no timestamps or local paths.
"""

from __future__ import annotations

import argparse
from fractions import Fraction as Q
import hashlib
import json
from pathlib import Path


EXPECTED_HASHES = {
    "RESPONSE_AND_REMAINDER.md": "7cd5f28c82e1b6c50d1088a4a02862a83489e36ccd8e56e8abec38562e52278e",
    "native_response.json": "3974bafabd00e0f0a565183cfc4bcf6d9f100bddefd5fd2ed71bee67154bb85b",
    "gram_cauchy.json": "0ce79adc26349f0e3b5d89263c2459274c9244b13e7946f28c3f013c965bc8f6",
}


def rational(value: Q | int | str) -> str:
    value = Q(value)
    return f"{value.numerator}/{value.denominator}"


def run(source_dir: Path) -> dict:
    source_manifest = []
    identity_checks = []
    sources = {}
    for name, expected in EXPECTED_HASHES.items():
        raw = (source_dir / name).read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        source_manifest.append({"file": name, "bytes": len(raw), "sha256": digest})
        identity_checks.append({
            "name": f"source_sha256:{name}", "actual": digest,
            "expected": expected, "passed": digest == expected,
        })
        if name.endswith(".json"):
            sources[name] = json.loads(raw.decode("utf-8-sig"))
    native = sources["native_response.json"]
    gram = sources["gram_cauchy.json"]
    checks = []

    def check(name: str, passed: bool, **details) -> None:
        checks.append({"name": name, "passed": bool(passed), **details})

    def eq(name: str, actual, expected) -> None:
        actual, expected = Q(actual), Q(expected)
        check(name, actual == expected, actual=rational(actual), expected=rational(expected))

    def lt(name: str, left, right) -> None:
        left, right = Q(left), Q(right)
        check(name, left < right, left=rational(left), right=rational(right),
              positive_margin=rational(right - left))

    for degree in ("2", "4", "6"):
        rows = [Q(value) for value in native["row_sums"][degree]]
        check(f"row_sum_count_{degree}", len(rows) == 240, actual=len(rows), expected=240)
        maximum = max(rows)
        indices = [index for index, value in enumerate(rows) if value == maximum]
        eq(f"maximum_row_{degree}", maximum, native["row_norms"][degree])
        check(f"maximizing_indices_{degree}",
              indices == native["maximizing_original_rows"][degree],
              actual=indices, expected=native["maximizing_original_rows"][degree])

    M = Q(240)
    xi0 = Q(1, 784)
    gap_over_kappa = 3 - 2 * M * xi0
    t = 280 * xi0
    row_prefactor = Q(98, 39) + 239 * Q(49, 34)
    tail = row_prefactor * t**8 / (1 - t**2)
    shift = sum((Q(native["row_norms"][degree]) * xi0**int(degree)
                 for degree in ("2", "4", "6")), Q(0))
    eq("A65 tail", tail, native["complete_tail_row_bound"])
    eq("A66 coefficient shift", shift, native["computed_coefficient_shift_bound"])
    eq("A66 full error", tail + shift, native["complete_response_error"])
    lt("A66 strict full error", tail + shift, Q(1, 9))
    eq("A69 gap", gap_over_kappa, Q(117, 49))
    eq("A70 state upper", Q(4, 9) / gap_over_kappa, Q(196, 1053))
    eq("A71 state lower", Q(2, 9)**2 / (4 * M), Q(1, 19440))
    eq("source coupling endpoint", 1 / (Q(4) * Q(14)**2), xi0)

    r, a = Q(1, 280), Q(1, 14)
    eta_distinct = M * r**2 + 4 * r * a + 2 * a**2
    eta_same = M * r**2 + 4 * r * a + 4 * a**2
    eq("A57 source budget", M * r + 2 * a, 1)
    eq("A57 distinct Gram", eta_distinct, gram["distinct_source_squared_norm"])
    eq("A57 same Gram", eta_same, gram["same_source_squared_norm"])
    lt("A52 distinct contour", 4 * eta_distinct, 1)
    lt("A52 same contour", 4 * eta_same, 1)
    lt("A58 distinct root comparison", eta_distinct, Q(1, 68) * (1 - Q(1, 68)))
    lt("A58 same root comparison", eta_same, Q(1, 39) * (1 - Q(1, 39)))
    eq("A58 distinct circle", Q(1, 68) / (2 * a**2), gram["response_bound_distinct"])
    eq("A58 same circle", Q(1, 39) / (2 * a**2), gram["response_bound_same"])

    xi, g_squared = Q(gram["xi"]), Q(gram["g_squared"])
    coefficient = Q(gram["degree_six_coefficient"])
    t_gram = xi / r
    error = Q(gram["response_bound_distinct"]) * t_gram**8 / (1 - t_gram**2)
    eq("A60 source coupling", 1 / (4 * g_squared**2), xi)
    eq("A61 absolute error", error, gram["absolute_response_error"])
    lower, upper = coefficient - error / xi**6, coefficient + error / xi**6
    eq("A61 exact lower", lower, gram["exact_divided_response_interval"][0])
    eq("A61 exact upper", upper, gram["exact_divided_response_interval"][1])
    lt("A61 reported lower", gram["reported_divided_response_interval"][0], lower)
    lt("A61 reported upper", upper, gram["reported_divided_response_interval"][1])

    for label, old_xi, old_r, circle, reported_lower, reported_upper in (
        ("A24", Q(1, 10**18), Q(1, 1280), Q(128, 3), Q(81828, 10**10), Q(81835, 10**10)),
        ("A49", Q(1, 10**14), Q(1, 405), Q(54), Q(42744, 10**10), Q(120919, 10**10)),
    ):
        old_t = old_xi / old_r
        divided_error = circle * old_t**8 / (1 - old_t**2) / old_xi**6
        lt(f"{label} lower", reported_lower, coefficient - divided_error)
        lt(f"{label} upper", coefficient + divided_error, reported_upper)

    eq("A42 small root at rho", Q(16, 27) * (3 - 2 * Q(20, 27) - Q(16, 27)), Q(20, 27)**2)
    eq("A43 radii budget", M * Q(1, 405) + 2 * Q(2, 27), Q(20, 27))
    eq("A45 circle bound", Q(16, 27) / (2 * Q(2, 27)**2), 54)
    eq("A50 derivative prefactor", Q(16, 27) / (2 * M * Q(1, 324)), Q(2, 5))
    eq("A63 derivative prefactor", (2 / M) / (2 * M * (1 / M)), 1 / M)
    lt("A62 rational energy root comparison at M=240", 1 / M, (2 / M) * (1 - 2 / M))

    all_checks = identity_checks + checks
    return {
        "schema": "ym-response-intake-independent-rational-check-v1",
        "scope": "Finite-volume supplied-certificate arithmetic; no coefficient reconstruction",
        "source_manifest": source_manifest,
        "source_identity_checks": identity_checks,
        "arithmetic_checks": checks,
        "counts": {
            "source_identity_checks": len(identity_checks),
            "arithmetic_checks": len(checks),
            "passed": sum(check["passed"] for check in all_checks),
            "failed": sum(not check["passed"] for check in all_checks),
        },
        "derived": {
            "complete_response_error": rational(tail + shift),
            "strict_margin_to_one_ninth": rational(Q(1, 9) - tail - shift),
            "A61_lower": rational(lower),
            "A61_upper": rational(upper),
        },
        "limitations": [
            "Stored row sums were checked against their stored maxima; underlying full matrices were not supplied.",
            "The degree-six response coefficient is an input; this script does not regenerate it.",
            "This receipt does not certify an infinite-volume, continuum, or whole-Hilbert-space reconstruction theorem.",
            "Strict quadratic-form bounds apply to nonzero vectors; their zero-vector specializations are equalities.",
        ],
        "passed": all(check["passed"] for check in all_checks),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).resolve().with_name("receipt.json"))
    args = parser.parse_args()
    receipt = run(args.source_dir)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"passed": receipt["passed"], "counts": receipt["counts"]}, sort_keys=True))
    return 0 if receipt["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
