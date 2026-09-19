"""Bounded independent rational checks for the 18 September intake.

No archive code is imported or executed.  This is a one-variable original
W-polynomial calculation, not a replay of the spatial source catalogues.
Run with Python's standard library and --source-dir naming the intake folder.
"""

from fractions import Fraction as F
from math import comb
from pathlib import Path
import argparse
import hashlib
import json


SOURCE_SHA256 = {
    "EIGHTH_ENERGY.md": "0b3c1514d93274d8177717e1d087d752398d43c5f8660c85fdc5abb5c1cdb247",
    "SIXTH_SOURCE.md": "41e16538ac98850e5a3c1a01018cf759c7cca10585a866289e97f450e85f1496",
    "yang_mills_cumulative_20260917.zip": "859635f5bb246388b6a831f03847b3a92e693adf1233f01575c3678076c35d21",
}


def require(condition, label):
    if not condition:
        raise ArithmeticError(label)


def plus(a, b):
    result = dict(a)
    for degree, coefficient in b.items():
        result[degree] = result.get(degree, F(0)) + coefficient
    return {degree: coefficient for degree, coefficient in result.items() if coefficient}


def times(a, b):
    result = {}
    for i, x in a.items():
        for j, y in b.items():
            result[i + j] = result.get(i + j, F(0)) + x * y
    return {degree: coefficient for degree, coefficient in result.items() if coefficient}


def scale(a, scalar):
    return {degree: coefficient * scalar for degree, coefficient in a.items() if coefficient * scalar}


def mean(a):
    """Original normalized SU(2) class Haar moments: odd 0, even Catalan."""
    return sum(
        (coefficient * F(comb(degree, degree // 2), degree // 2 + 1)
         for degree, coefficient in a.items() if degree % 2 == 0),
        F(0),
    )


def kinetic(a):
    """K f(W) = (W^2 - 4) f''(W) + 3 W f'(W), W = 2 cos(theta)."""
    result = {}
    for degree, coefficient in a.items():
        result = plus(result, {degree: degree * (degree + 2) * coefficient})
        if degree >= 2:
            result = plus(result, {degree - 2: -4 * degree * (degree - 1) * coefficient})
    return result


def invert(a):
    """Triangular inversion of this one-variable differential operator."""
    remainder = dict(a)
    result = {}
    for degree in range(max(remainder, default=0), 0, -1):
        coefficient = remainder.get(degree, F(0)) / F(degree * (degree + 2))
        if coefficient:
            result[degree] = coefficient
            remainder = plus(remainder, scale(kinetic({degree: coefficient}), -1))
    require(not remainder, "kinetic RHS must have zero Haar mean")
    result = plus(result, {0: -mean(result)})
    require(mean(result) == 0, "inverse Haar section")
    require(kinetic(result) == a, "inverse equation")
    return result


def convolution(a, b, limit):
    result = [{} for _ in range(limit + 1)]
    for i, p in enumerate(a):
        for j, q in enumerate(b):
            if i + j <= limit:
                result[i + j] = plus(result[i + j], times(p, q))
    return result


def calculate():
    u = [{0: F(1)}]
    energy = [F(0)]
    for order in range(1, 9):
        insertion = times({1: F(1)}, u[order - 1])
        energy.append(-mean(insertion))
        rhs = insertion
        for j in range(1, order + 1):
            rhs = plus(rhs, scale(u[order - j], energy[j]))
        u.append(invert(rhs))
        require(max(u[-1], default=0) <= order, "finite coefficient degree")

    target_energy = {2: -F(1, 3), 4: F(5, 216), 6: -F(289, 77760), 8: F(21391, 27993600)}
    for order, expected in target_energy.items():
        require(energy[order] == expected, "one-face energy degree " + str(order))
    require(all(energy[order] == 0 for order in (1, 3, 5, 7)), "odd energy coefficients")

    z = [{}] + u[1:7]
    power = [{0: F(1)}] + [{} for _ in range(6)]
    logarithm = [{} for _ in range(7)]
    for j in range(1, 7):
        power = convolution(power, z, 6)
        for order in range(7):
            logarithm[order] = plus(logarithm[order], scale(power[order], F((-1) ** (j + 1), j)))
    v6 = plus(logarithm[6], {0: -mean(logarithm[6])})
    target_v6 = {
        0: F(132817, 391910400), 2: -F(27383, 65318400),
        4: F(5911, 130636800), 6: -F(797, 391910400),
    }
    require(v6 == target_v6, "S27 one-face sixth logarithmic source")
    characters = plus(
        plus(scale({2: F(1), 0: -F(1)}, -F(11, 36450)),
             scale({4: F(1), 2: -F(3), 0: F(1)}, F(491, 13996800))),
        scale({6: F(1), 4: -F(5), 2: F(6), 0: -F(1)}, -F(797, 391910400)),
    )
    require(characters == v6, "S27/S28 coordinate identity")

    pair = lambda a, b: mean(times(a, b))
    n8 = pair(u[4], kinetic(u[4])) - 2 * pair(u[3], times({1: F(1)}, u[4]))
    d6 = 2 * pair(u[2], u[4]) + pair(u[3], u[3])
    d4 = 2 * pair(u[1], u[3]) + pair(u[2], u[2])
    d2 = pair(u[1], u[1])
    e8_quotient = n8 - energy[2] * d6 - energy[4] * d4 - energy[6] * d2
    e8_simplified = -pair(u[4], kinetic(u[4])) - energy[2] * pair(u[3], u[3]) - energy[4] * d4 - energy[6] * d2
    require(e8_quotient == e8_simplified == energy[8], "E6/E9 one-face return")

    a = [
        F(1703320005700992315276593, 68235298203010622261760000),
        F(421994013280213546390961, 31615192631460259261440000),
        F(14702805516554176523, 16975106412310126080000),
        F(404673359378191, 1312237663289280000),
    ]
    box_l2 = sum(coefficient * 4 ** (3 - index) for index, coefficient in enumerate(a))
    require(box_l2 == F(9876448280610811115073772847, 5441765031690097125375360000), "E17 to E18")
    require(a[0] / 3 == F(1703320005700992315276593, 204705894609031866785280000), "E17 to E19")

    # Both expressions are polynomials of degree at most three.  Five exact
    # evaluations establish equality; these values are not claimed physical boxes.
    for m in range(5):
        faces = 3 * m * m * (m + 1)
        adjacent = 6 * m * (3 * m * m - 1)
        paths = 138 * m ** 3 - 126 * m * m - 24 * m + 12
        common = 12 * m * m * (m - 1)
        corners = 8 * m ** 3
        cubes = m ** 3
        summed = (-F(289, 77760) * faces + F(22285, 23654592) * adjacent
                  - F(4909, 118272960) * paths + F(244, 4312035) * common
                  - F(212, 542997) * corners - F(83, 1944) * cubes)
        compact = -F(211396463 * m ** 3 + 30959193 * m * m + 21845782 * m + 2336684, 4691494080)
        require(summed == compact, "inherited sixth polynomial consistency")

    require(sum((1, 2, 2, 19, 2, 31, 171, 9, 268, 2075, 4650)) == 7230, "sixth representative count sum")
    require(sum((4, 84, 84, 1572, 42, 3144, 27676, 524, 41514, 469360, 1295136)) == 1839140, "sixth anchored count sum")
    require(sum((1, 6, 59, 436, 2056, 4550, 121, 1)) == 7230, "sixth cycle-rank count sum")
    return {
        "schema": "ym-eighth-intake-bounded-check-v1",
        "source_sha256": SOURCE_SHA256,
        "method": "fresh one-variable W-polynomial recurrence with original radial K and Catalan Haar moments; no archive imports or execution",
        "energy_even": {str(order): str(energy[order]) for order in (2, 4, 6, 8)},
        "odd_energy_through_seven_zero": True,
        "sixth_source_W_polynomial": {str(degree): str(coefficient) for degree, coefficient in sorted(v6.items())},
        "S27_S28_identity": True,
        "one_face_E6_and_E9": str(e8_quotient),
        "e8_box_L2_from_E17": str(box_l2),
        "bulk_e8_per_face_from_E17": str(a[0] / 3),
        "inherited_sixth_cubic_polynomial_identity": True,
        "sixth_catalogue_count_sums": True,
        "not_checked": [
            "7230 sixth spatial source identities or their claimed execution records",
            "80 eighth spatial coefficients and embedding counts",
            "sixth local derivative bounds and eight-chord witness",
            "RESPONSE_AND_REMAINDER analytic and response claims",
            "historical uniform-gap or continuum claims",
        ],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--verify-receipt", type=Path)
    args = parser.parse_args()
    for filename, expected in SOURCE_SHA256.items():
        digest = hashlib.sha256()
        with (args.source_dir / filename).open("rb") as stream:
            for chunk in iter(lambda: stream.read(65536), b""):
                digest.update(chunk)
        require(digest.hexdigest() == expected, "source identity: " + filename)
    result = calculate()
    if args.verify_receipt is not None:
        with args.verify_receipt.open(encoding="utf-8") as stream:
            supplied = json.load(stream)
        require(supplied == result, "deterministic receipt mismatch")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
