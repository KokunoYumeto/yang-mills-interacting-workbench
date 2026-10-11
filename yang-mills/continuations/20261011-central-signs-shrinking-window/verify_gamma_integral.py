"""Exact rational certificate for the assigned C_gamma integral.

Uses Python standard-library integer and Fraction arithmetic only.
No floating-point operation contributes to the certificate.
The mathematics and all remainder bounds are proved in GAMMA_INTEGRAL.md.
"""

from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

HERE = Path(__file__).resolve().parent


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def neg(a):
    return -a[1], -a[0]


def sub(a, b):
    return add(a, neg(b))


def mul(a, b):
    products = [x * y for x in a for y in b]
    return min(products), max(products)


def inv(a):
    assert a[0] > 0
    return 1 / a[1], 1 / a[0]


def div(a, b):
    return mul(a, inv(b))


def point(q):
    return F(q), F(q)


def scale(a, q):
    return mul(a, point(q))


def atan_interval(x, terms):
    assert F(0) < x < F(1)
    assert terms > 0
    total = sum(((-1) ** k * x ** (2 * k + 1) / (2 * k + 1)
                 for k in range(terms)), F(0))
    first_omitted = x ** (2 * terms + 1) / (2 * terms + 1)
    if terms % 2 == 0:
        return total, total + first_omitted
    return total - first_omitted, total


def positive_log_interval(t, terms):
    """Enclose log((1+t)/(1-t)) for positive rational-interval t."""
    assert 0 < t[0] <= t[1] < 1
    low = 2 * sum((t[0] ** (2 * k + 1) / (2 * k + 1)
                   for k in range(terms)), F(0))
    high = 2 * sum((t[1] ** (2 * k + 1) / (2 * k + 1)
                    for k in range(terms)), F(0))
    high += (2 * t[1] ** (2 * terms + 1)
             / ((2 * terms + 1) * (1 - t[1] ** 2)))
    return low, high


def dilog_interval(z, terms):
    assert 0 < z[0] <= z[1] < 1
    low = sum((z[0] ** k / (k * k) for k in range(1, terms + 1)), F(0))
    high = sum((z[1] ** k / (k * k) for k in range(1, terms + 1)), F(0))
    high += z[1] ** (terms + 1) / ((terms + 1) ** 2 * (1 - z[1]))
    return low, high


def decimal_floor(q, digits):
    factor = 10 ** digits
    integer = (q.numerator * factor) // q.denominator
    sign = "-" if integer < 0 else ""
    integer = abs(integer)
    return f"{sign}{integer // factor}.{integer % factor:0{digits}d}"


def decimal_ceiling(q, digits):
    factor = 10 ** digits
    integer = -((-q.numerator * factor) // q.denominator)
    sign = "-" if integer < 0 else ""
    integer = abs(integer)
    return f"{sign}{integer // factor}.{integer % factor:0{digits}d}"


def certificate():
    sqrt_digits = 50
    factor = 10 ** sqrt_digits
    root_floor = isqrt(2 * factor * factor)
    root = F(root_floor, factor), F(root_floor + 1, factor)
    assert root[0] ** 2 < 2 < root[1] ** 2

    # Machin identity: pi = 16 atan(1/5) - 4 atan(1/239).
    pi = sub(scale(atan_interval(F(1, 5), 40), 16),
             scale(atan_interval(F(1, 239), 12), 4))
    pi_squared = mul(pi, pi)

    # tau = 3 - 2 sqrt(2), r = (sqrt(2)-1)/(sqrt(2)+3).
    tau = sub(point(3), scale(root, 2))
    r = div(sub(root, point(1)), add(root, point(3)))
    log_ratio = neg(positive_log_interval(r, 20))
    dilog = dilog_interval(tau, 50)
    numerator = add(point(2), scale(root, F(1, 2)))
    numerator = add(numerator, scale(log_ratio, 3))
    numerator = sub(numerator, div(dilog, scale(root, 2)))
    enclosed = sub(div(numerator, pi_squared), inv(scale(root, 24)))

    announced = (F("0.181178439743214882282299233973"),
                 F("0.181178439743214882282299233974"))
    assert announced[0] < enclosed[0] < enclosed[1] < announced[1]

    # Independent exact-series enclosure. It uses a different integral
    # evaluation, proved in Section 7, with a geometric remainder.
    N = 110
    zeta2 = scale(pi_squared, F(1, 6))
    total = sub(point(F(23, 32)), scale(zeta2, F(1, 16)))
    coefficient = F(1)
    harmonic = F(0)
    for j in range(1, N):
        coefficient *= F(2 * j - 1, 4 * j)
        harmonic += F(1, j)
        if j >= 3:
            H_previous = harmonic - F(1, j)
            moment = F(j * H_previous - 2 * (j - 1), (j - 2) * (j - 1))
            assert moment > 0
            total = add(total, point(coefficient * moment))
    series = mul(div(scale(root, 2), pi_squared),
                 (total[0], total[1] + F(1, 2 ** N)))
    assert series[0] <= enclosed[1] and enclosed[0] <= series[1]
    assert announced[0] < series[0] < series[1] < announced[1]

    result = {
        "integral": "(2/pi^2) integral_[0,pi]^2 |a*b*(b-a)|/sqrt(a^2+b^2) dx dy",
        "a": "-sin(x)*cos(y)",
        "b": "cos(x)*sin(y)",
        "simultaneous_zero_value": 0,
        "closed_form": "[2+sqrt(2)/2+3*log(2/(1+sqrt(2)))-Li2(3-2*sqrt(2))/(2*sqrt(2))]/pi^2-1/(24*sqrt(2))",
        "certified_strict_lower": str(announced[0]),
        "certified_strict_upper": str(announced[1]),
        "certified_decimal_lower": "0.181178439743214882282299233973",
        "certified_decimal_upper": "0.181178439743214882282299233974",
        "closed_form_internal_outward_36_digits": [
            decimal_floor(enclosed[0], 36), decimal_ceiling(enclosed[1], 36)],
        "independent_series_internal_outward_33_digits": [
            decimal_floor(series[0], 33), decimal_ceiling(series[1], 33)],
        "parameters": {
            "sqrt_decimal_digits": sqrt_digits,
            "arctan_1_over_5_terms": 40,
            "arctan_1_over_239_terms": 12,
            "log_terms": 20,
            "dilog_terms": 50,
            "independent_series_terms": N,
        },
        "arithmetic": "Exact Python integers and fractions.Fraction; displayed decimal endpoints rounded outward by integer division.",
        "all_assertions_passed": True,
        "proof": "GAMMA_INTEGRAL.md, Sections 1-8",
    }
    (HERE / "GAMMA_INTEGRAL_CERTIFICATE.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    certificate()
