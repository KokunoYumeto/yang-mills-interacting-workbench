"""Independent scalar audit of PHYSICAL_RETURN.md R24--R32.

Only the displayed rational inputs in QUARTIC_SOURCE.md Q17/Q18/Q26
and PHYSICAL_RETURN.md R2 are used. No author receipt or producer is read.
This checks implications of the supplied spin budgets, not their derivation.
All mathematical comparisons use fractions and integers, never floats.
"""

from decimal import Decimal, localcontext
from fractions import Fraction as F
from math import isqrt


def decimal(value, precision=36):
    with localcontext() as context:
        context.prec = precision
        return str(Decimal(value.numerator) / Decimal(value.denominator))


def emit(name, value):
    print(f"{name} = {value} [decimal {decimal(value)}]")


def require(name, predicate):
    assert predicate, name
    print(f"PASS {name}")


def sign_certificate(name, value, sign):
    require(name, value * sign > 0)
    # A Fraction always has positive denominator: its integer numerator
    # is an exact, independently reproducible sign certificate.
    print(f"  numerator = {value.numerator}")
    print(f"  denominator = {value.denominator}")


def sqrt_enclosure(value, places=30):
    assert value >= 0
    scale = 10**places
    integer = isqrt(value.numerator * scale**2 // value.denominator)
    lower, upper = F(integer, scale), F(integer + 1, scale)
    assert lower**2 <= value < upper**2
    return lower, upper


m1, t1 = F(64, 3), F(16, 3)
m2, t2 = F(5834, 39), F(137, 6)
m3, t3 = F(336572872, 208845), F(225985217, 1253070)
m4 = F(17270702970768271, 341697152160)
t4 = F(110695177857394584026401, 18025447358750832000)
A4 = F(2296826751679, 30073680)

l1, l2, l3, l4 = F(128, 3), F(3132, 13), m3 + 4*t3, m4 + 4*t4
b14 = 3*(m1*t4 + m4*t1)
b23 = 3*(m2*t3 + m3*t2)
b24 = 3*(m2*t4 + m4*t2)
b33 = 6*m3*t3
b34 = 3*(m3*t4 + m4*t3)
b44 = 6*m4*t4
residual = {5: 2*b14 + 2*b23, 6: 2*b24 + b33, 7: 2*b34, 8: b44}
p2 = F(1136, 13)
p3 = F(3, 2)*m3 - 6*t3
p4 = F(3, 2)*m4 - 6*t4

require("l1 from m1,t1", l1 == m1 + 4*t1)
require("l2 from m2,t2", l2 == m2 + 4*t2)
ordered_residual_pairs = {
    degree: [(i, j) for i in range(1, 5) for j in range(1, 5) if i+j == degree]
    for degree in range(5, 9)
}
require("all ordered degree 5--8 residual pairs", ordered_residual_pairs == {
    5: [(1, 4), (2, 3), (3, 2), (4, 1)],
    6: [(2, 4), (3, 3), (4, 2)], 7: [(3, 4), (4, 3)], 8: [(4, 4)]
})
require("l3 displayed fraction", l3 == F(292337810, 125307))
require("b23 displayed fraction", b23 == F(222621900791, 1163565))
require("b33 displayed fraction", b33 == F(76060493515233224, 43616234025))
require("p3 displayed fraction", p3 == F(278874091, 208845))
require("p4 displayed fraction", p4 == F(32092619324045301088, 823531037954625))
require("Q26 t4 < A4/6", t4 < A4/6)
require("all residual, derivative and margin constants positive", all(
    value > 0 for value in [l1, l2, l3, l4, p2, p3, p4, *residual.values()]
))

for name in ["m4", "t4", "l4", "b14", "b23", "b24", "b33", "b34", "b44", "p3", "p4"]:
    emit(name, globals()[name])
for degree, coefficient in residual.items():
    emit(f"delta coefficient of x^{degree}", coefficient)


def ell(x):
    return l1*x + l2*x**2 + l3*x**3 + l4*x**4


def delta(x):
    return sum(coefficient*x**degree for degree, coefficient in residual.items())


def discriminant(x):
    return (1 - ell(x))**2 - F(8, 3)*delta(x)


def margin_polynomial(x):
    return p2*x**2 + p3*x**3 + p4*x**4


# Reconstruct every coefficient of 3*(1-chi) after substituting w_*.
require("linear margin term cancels", F(3, 2)*l1 - 12*t1 == 0)
require("quadratic margin coefficient", F(3, 2)*l2 - 12*t2 == p2)
require("cubic margin coefficient", F(3, 2)*l3 - 12*t3 == p3)
require("quartic margin coefficient", F(3, 2)*l4 - 12*t4 == p4)

coarse_lower, coarse_upper = F(181, 10000), F(182, 10000)
sign_certificate("ell(0.0182) < 1", 1 - ell(coarse_upper), 1)
sign_certificate("D(0.0181) > 0", discriminant(coarse_lower), 1)
sign_certificate("D(0.0182) < 0", discriminant(coarse_upper), -1)
alpha_lower = F("0.018104972231644127075")
alpha_upper = F("0.018104972231644127076")
sign_certificate("D(alpha lower endpoint) > 0", discriminant(alpha_lower), 1)
sign_certificate("D(alpha upper endpoint) < 0", discriminant(alpha_upper), -1)
coupling_lower = F("3.715960362535435236")
coupling_upper = F("3.715960362535435237")
# The displayed alpha interval is not narrow enough to imply both displayed
# coupling endpoints. Check each transformed endpoint directly instead.
inverse_lower = 1/(4*coupling_lower**2)
inverse_upper = 1/(4*coupling_upper**2)
require("transformed coupling endpoints in monotonic interval", coarse_lower < inverse_upper < inverse_lower < coarse_upper)
sign_certificate("lower coupling bound from D(1/(4*g_lower^2)) < 0", discriminant(inverse_lower), -1)
sign_certificate("upper coupling bound from D(1/(4*g_upper^2)) > 0", discriminant(inverse_upper), 1)

for x, threshold in [(F(4, 225), F("1.6584")), (F(1, 64), F("1.89811"))]:
    value = discriminant(x)
    require(f"benchmark x={x} inside proved interval", 0 < x < alpha_lower)
    sqrt_lower, sqrt_upper = sqrt_enclosure(value)
    lower = F(3, 2)*(1 + sqrt_lower) + margin_polynomial(x)
    upper = F(3, 2)*(1 + sqrt_upper) + margin_polynomial(x)
    emit(f"D({x})", value)
    emit(f"d({x}) lower enclosure", lower)
    emit(f"d({x}) upper enclosure", upper)
    require(f"d({x}) > {threshold}", lower > threshold)
    report_lower, report_upper = {
        F(4, 225): (F("1.658436438755717813174"), F("1.658436438755717813175")),
        F(1, 64): (F("1.898117961144383174256"), F("1.898117961144383174257")),
    }[x]
    require(f"reported decimal enclosure x={x}", report_lower < lower < upper < report_upper)
    square_threshold = F(2, 3)*(threshold - margin_polynomial(x)) - 1
    require(f"benchmark square threshold positive x={x}", square_threshold > 0)
    sign_certificate(f"benchmark direct square difference x={x}", value - square_threshold**2, 1)

x0 = F(4, 225)
monotone_upper = -F(3, 2)*(1 - ell(x0))*l1 + 2*p2*x0 + 3*p3*x0**2 + 4*p4*x0**3
emit("claimed derivative upper bound", monotone_upper)
require("strictly negative derivative upper bound", monotone_upper < 0)
require("original xi at g^2=15/4", 1/(4*F(15, 4)**2) == F(4, 225))
require("original xi at g^2=4", 1/(4*F(4)**2) == F(1, 64))
require("original energy factor", 2*F("1.6584") == F("3.3168"))

x = F(1, 64)
sqrt_lower, sqrt_upper = sqrt_enclosure(discriminant(x))
w_lower = F(3, 4)*(1 - ell(x) - sqrt_upper)
w_upper = F(3, 4)*(1 - ell(x) - sqrt_lower)
emit("w_*(1/64) lower enclosure", w_lower)
emit("w_*(1/64) upper enclosure", w_upper)
require("reported decimal correction enclosure", F("0.011169768000311862078") < w_lower < w_upper < F("0.011169768000311862079"))
claimed_error = F("0.011169768000312")
require("claimed complete correction upper bound", w_upper < claimed_error)
square_threshold = 1 - ell(x) - F(4, 3)*claimed_error
require("correction square threshold positive", square_threshold > 0)
sign_certificate("correction direct square difference", discriminant(x) - square_threshold**2, 1)

print("All exact scalar checks passed. Analytical source/spectral hypotheses are outside this script.")
