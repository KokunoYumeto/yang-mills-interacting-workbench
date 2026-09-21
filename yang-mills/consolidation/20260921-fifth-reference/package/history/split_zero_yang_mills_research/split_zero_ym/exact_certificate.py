#!/usr/bin/env python3
"""Recompute the L=2 Yang--Mills cubic certificate with integer intervals.

Python 3.10+; standard library only. No network, floating point, or third-party
packages are used in any enclosure or assertion. Coordinates are the original
n in {-2,...,2}^3, with direction indices 0,1,2 corresponding to paper 1,2,3.

Sources and mathematical provenance are recorded in RESEARCH_NOTE.md.
This checks the 112 frequency blocks and the stated cubic coefficient; it does
not execute a continuum construction or assert a four-dimensional mass gap.
"""
from __future__ import annotations
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from math import isqrt
from pathlib import Path
import json

M = 10**40

def ceil_div(n: int, d: int) -> int:
    if d == 0:
        raise ZeroDivisionError("integer interval division by zero")
    return -((-n) // d)

@dataclass(frozen=True)
class Interval:
    lo: int
    hi: int

    def __post_init__(self) -> None:
        if self.lo > self.hi:
            raise ValueError("interval endpoints out of order")

    @classmethod
    def integer(cls, x: int) -> Interval:
        return cls(x*M, x*M)

    @classmethod
    def rational(cls, p: int, q: int) -> Interval:
        if q <= 0:
            raise ValueError("rational denominator must be positive")
        return cls((p*M)//q, ceil_div(p*M,q))

    def __add__(self, other: Interval) -> Interval:
        return Interval(self.lo+other.lo, self.hi+other.hi)

    def __neg__(self) -> Interval:
        return Interval(-self.hi,-self.lo)

    def __sub__(self, other: Interval) -> Interval:
        return self + (-other)

    def __mul__(self, other: Interval) -> Interval:
        p = [x*y for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        return Interval(min(p)//M, ceil_div(max(p),M))

    def __truediv__(self, other: Interval) -> Interval:
        if other.lo <= 0 <= other.hi:
            raise ZeroDivisionError("divisor interval contains zero")
        pairs = [(x*M,y) for x in (self.lo,self.hi) for y in (other.lo,other.hi)]
        return Interval(min(n//d for n,d in pairs), max(ceil_div(n,d) for n,d in pairs))

    def sqrt(self) -> Interval:
        if self.lo < 0:
            raise ValueError("square root requires a nonnegative interval")
        a = isqrt(self.lo*M)
        b0 = isqrt(self.hi*M)
        b = b0 + int(b0*b0 < self.hi*M)
        assert a*a <= self.lo*M < (a+1)*(a+1)
        assert (b-1)*(b-1) < self.hi*M <= b*b or self.hi == 0
        return Interval(a,b)

    def record(self) -> dict[str,str]:
        return {"lower_numerator":str(self.lo),"upper_numerator":str(self.hi),"denominator":str(M)}

ZERO = Interval.integer(0)
ONE = Interval.integer(1)
TWO = Interval.integer(2)
FIVE = Interval.integer(5)
L = 2
N = 5
Edge = tuple[tuple[int,int,int], int]
CHORDS: tuple[Edge,...] = (((-1,1,-2),1),((-1,2,-2),2),((-1,1,-1),1))
K_SHORT = ((1273974,432279,-317748),(432279,1273974,-386480),(-317748,-386480,1563504))
Q_SHORT = ((-845265,-977768,417911),(473487,-1342407,1208367),(421454,840903,-1200597))


def tree_path(v: tuple[int,int,int]) -> list[Edge]:
    """Edges of the original root-to-v path, stored in reverse order."""
    n = list(v)
    edges: list[Edge] = []
    while any(x > -L for x in n):
        d = next(d for d in range(3) if n[d] > -L)
        n[d] -= 1
        edges.append((tuple(n),d))
    return edges


def retained_b_rows() -> list[dict[Edge,int]]:
    rows: list[dict[Edge,int]] = []
    for n,d in CHORDS:
        target = list(n)
        target[d] += 1
        row = {(n,d):-1}  # r-l on the chord itself
        for e in tree_path(n) + tree_path(tuple(target)):
            row[e] = row.get(e,0)-1
        rows.append(row)
    return rows


def compute() -> dict:
    root5 = FIVE.sqrt()
    sin_theta = (root5-ONE)/Interval.integer(4)
    cos_theta = ((FIVE+root5)/Interval.integer(8)).sqrt()
    sins = [ZERO]
    coses = [ONE]
    for _ in range(1,20):
        sins.append(sins[-1]*cos_theta+coses[-1]*sin_theta)
        # Read the previous sine, not the newly appended sine.
        coses.append(coses[-1]*cos_theta-sins[-2]*sin_theta)
    root_one_fifth = Interval.rational(1,5).sqrt()
    root_two_fifths = Interval.rational(2,5).sqrt()
    v = {(j,l):root_one_fifth if j == 0 else root_two_fifths*coses[(j*(2*l+1))%20]
         for j in range(N) for l in range(N)}
    w = {(j,l):ZERO if j == 0 else -root_two_fifths*sins[(2*j*(l+1))%20]
         for j in range(N) for l in range(N-1)}
    b = retained_b_rows()
    needed_edges = set(CHORDS)
    for row in b:
        needed_edges.update(row)
    K = [[ZERO for _ in range(3)] for _ in range(3)]
    Q = [[ZERO for _ in range(3)] for _ in range(3)]
    block_count = 0
    polarization_count = 0
    for j in product(range(N),repeat=3):
        positive = sum(k > 0 for k in j)
        if positive < 2:
            continue
        block_count += 1
        polarization_count += positive-1
        s = [TWO*sins[k] for k in j]
        sigma2 = sum((u*u for u in s),ZERO)
        sigma = sigma2.sqrt()
        phi: dict[Edge,Interval] = {}
        for e in needed_edges:
            n,d = e
            value = ONE
            for h in range(3):
                value = value*(w[j[h],n[h]+L] if h == d else v[j[h],n[h]+L])
            phi[e] = value
        S: dict[tuple[Edge,Edge],Interval] = {}
        for e in needed_edges:
            for f in CHORDS:
                d,h = e[1],f[1]
                projection = (ONE if d == h else ZERO) - s[d]*s[h]/sigma2
                S[e,f] = sigma*phi[e]*phi[f]*projection
        for u in range(3):
            for vindex in range(3):
                K[u][vindex] = K[u][vindex]+S[CHORDS[u],CHORDS[vindex]]
                Q[u][vindex] = Q[u][vindex]+sum(
                    (Interval.integer(weight)*S[e,CHORDS[vindex]] for e,weight in b[u].items()),ZERO)
    assert block_count == 112
    assert polarization_count == 176
    for computed,short in ((K,K_SHORT),(Q,Q_SHORT)):
        for i in range(3):
            for j in range(3):
                assert short[i][j]*M < computed[i][j].lo*10**6
                assert computed[i][j].hi*10**6 < (short[i][j]+1)*M
    # Full kinetic expression (183): sum_j Q_j dot (e_j cross K_j).
    terms = ((-1,0,1,0,2),(1,0,2,0,1),(1,1,0,1,2),
             (-1,1,2,1,0),(-1,2,0,2,1),(1,2,1,2,0))
    kinetic_eight = sum((Interval.integer(sign)*Q[qr][qc]*K[kr][kc]
                         for sign,qr,qc,kr,kc in terms),ZERO)
    coefficient = kinetic_eight/Interval.integer(8)-Interval.rational(1,8)
    # Strict rational outward enclosure at 12 decimal places.
    short_den = 10**12
    short_lo = (coefficient.lo*short_den)//M
    short_hi = ceil_div(coefficient.hi*short_den,M)
    assert short_lo*M < coefficient.lo*short_den
    assert coefficient.hi*short_den < short_hi*M
    assert -243*M < coefficient.lo*1000
    assert coefficient.hi*1000 < -242*M
    beta = Fraction(-short_hi,short_den)
    assert beta > Fraction(121,500)

    # Exact magnetic term from the ordered vectors e1,e2,-e3,0.
    vectors = ((1,0,0),(0,1,0),(0,0,-1),(0,0,0))
    A = [Fraction(0)]*3
    B = [Fraction(0)]*3
    def cross(x, y):
        return [x[1]*y[2]-x[2]*y[1],x[2]*y[0]-x[0]*y[2],x[0]*y[1]-x[1]*y[0]]
    for z in vectors:
        cr = cross(A,z)
        B = [B[d]+cr[d]/2 for d in range(3)]
        A = [A[d]+z[d] for d in range(3)]
    magnetic = sum((A[d]*B[d] for d in range(3)),Fraction(0))/4
    assert magnetic == Fraction(-1,8)

    omega = (Interval.integer(3)*(FIVE+root5)/TWO).sqrt()
    omega2 = ((Interval.integer(13)+Interval.integer(3)*root5)/TWO).sqrt()
    delta = TWO*omega+omega2
    beta_interval = Interval.rational(beta.numerator,beta.denominator)
    vertex_bound = Interval.integer(48)*beta_interval*beta_interval/(omega*omega*omega2)
    primitive_bound = vertex_bound/(delta*delta)
    memory_bound = vertex_bound/delta
    published_primitive_bound = Interval.integer(14641)/(Interval.integer(13500000)*Interval.integer(3).sqrt())
    improvement_ratio = primitive_bound/published_primitive_bound
    assert improvement_ratio.lo*100 > 139*M
    assert improvement_ratio.hi*100 < 140*M

    return {
        "status":"all exact assertions passed",
        "arithmetic":"integer endpoints at denominator 10^40; every operation rounded outward",
        "box":{"L":L,"vertices":125,"edges":300,"chords":176,"frequency_blocks":block_count,"polarizations":polarization_count},
        "direction_index_map":"code 0,1,2 corresponds to manuscript 1,2,3",
        "chords":[{"start":list(n),"direction_in_manuscript":d+1} for n,d in CHORDS],
        "K_enclosures":[[x.record() for x in row] for row in K],
        "Q_enclosures":[[x.record() for x in row] for row in Q],
        "published_10e6_enclosures_verified":True,
        "a_times_c_enclosure":coefficient.record(),
        "strict_readable_enclosure":{"lower_numerator":str(short_lo),"upper_numerator":str(short_hi),"denominator":str(short_den)},
        "beta":{"numerator":str(beta.numerator),"denominator":str(beta.denominator)},
        "magnetic_coefficient_times_a":str(magnetic),
        "new_bounds":{
            "Omega":"sqrt(3*(5+sqrt(5))/2)",
            "Omega2":"sqrt((13+3*sqrt(5))/2)",
            "vertex_norm_squared":"strictly greater than 48*beta^2/(Omega^2*Omega2*a^2)",
            "primitive_norm_squared":"strictly greater than 48*beta^2/(Omega^2*Omega2*(2*Omega+Omega2)^2)",
            "vacuum_memory_at_zero":"strictly greater than 48*beta^2/(Omega^2*Omega2*(2*Omega+Omega2)*a)"
        },
        "bound_constant_enclosures":{
            "vertex_norm_squared_times_a_squared":vertex_bound.record(),
            "primitive_norm_squared":primitive_bound.record(),
            "vacuum_memory_at_zero_times_a":memory_bound.record(),
            "new_primitive_bound_divided_by_published_bound":improvement_ratio.record(),
            "ratio_strictly_between_139_over_100_and_140_over_100":True
        },
        "scope":"Finite-box coefficient and certificate. Other derivations are proved in the accompanying note; no four-dimensional continuum theorem is claimed."
    }


def main() -> None:
    result = compute()
    out = Path(__file__).resolve().with_name("certificate.json")
    out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(result["status"])
    print("frequency blocks:",result["box"]["frequency_blocks"])
    print("physical spatial modes:",result["box"]["polarizations"])
    r = result["strict_readable_enclosure"]
    print(f'{r["lower_numerator"]}/{r["denominator"]} < a*c < {r["upper_numerator"]}/{r["denominator"]}')
    print("certificate:",out)

if __name__ == "__main__":
    main()
