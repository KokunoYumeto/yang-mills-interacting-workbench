#!/usr/bin/env python3
"""Offline exact checks for the continuum continuation.

Uses Python's standard library only. Test matrices are declared finite algebraic
fixtures, not a numerical Yang--Mills spectrum. The analytic proofs are in the
accompanying RESEARCH_NOTE.md. No floating-point arithmetic is used.
"""
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path

CHECKS: dict[str, int] = {}


def checked(name: str, statement: bool) -> None:
    if not statement:
        raise AssertionError(name)
    CHECKS[name] = CHECKS.get(name, 0) + 1


# Matrices, with their input coordinates retained.
def zero(n: int, m: int) -> list[list[F]]:
    return [[F(0) for _ in range(m)] for _ in range(n)]


def eye(n: int) -> list[list[F]]:
    a = zero(n, n)
    for i in range(n):
        a[i][i] = F(1)
    return a


def tr(a):
    return [list(x) for x in zip(*a)]


def add(a, b):
    return [[x + y for x, y in zip(ar, br)] for ar, br in zip(a, b)]


def scale(c, a):
    return [[F(c) * x for x in row] for row in a]


def sub(a, b):
    return add(a, scale(-1, b))


def mul(a, b):
    if len(a[0]) != len(b):
        raise ValueError('Matrix dimensions do not compose')
    bt = tr(b)
    return [[sum((x*y for x, y in zip(ar, bc)), F(0))
             for bc in bt] for ar in a]


def inv(a):
    n = len(a)
    if any(len(row) != n for row in a):
        raise ValueError('Inverse requires a square matrix')
    aug = [list(row) + ident for row, ident in zip(a, eye(n))]
    for j in range(n):
        pivot = next((i for i in range(j, n) if aug[i][j]), None)
        if pivot is None:
            raise ValueError('Singular matrix')
        aug[j], aug[pivot] = aug[pivot], aug[j]
        p = aug[j][j]
        # Exact Gaussian elimination only computes the inverse; it does not
        # change any state vector, Gram matrix, operator, or coefficient frame.
        aug[j] = [x/p for x in aug[j]]
        for i in range(n):
            if i == j:
                continue
            c = aug[i][j]
            aug[i] = [x-c*y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


# Quaternion representation q -> q0 I - i sum(qj sigma_j).
def qadd(a, b):
    return tuple(x+y for x, y in zip(a, b))


def qscale(c, a):
    return tuple(F(c)*x for x in a)


def qmul(a, b):
    w, x, y, z = a
    v, r, s, t = b
    return (w*v-x*r-y*s-z*t,
            w*r+x*v+y*t-z*s,
            w*s-x*t+y*v+z*r,
            w*t+x*s-y*r+z*v)


def qinv(a):
    norm = sum(x*x for x in a)
    if not norm:
        raise ValueError('Zero quaternion')
    return (a[0]/norm, -a[1]/norm, -a[2]/norm, -a[3]/norm)


def product(qs):
    out = (F(1), F(0), F(0), F(0))
    for q in qs:
        out = qmul(out, q)
    return out


def quaternion_checks():
    qs = [tuple(map(F, q)) for q in [
        (F(3, 5), F(4, 5), 0, 0),
        (F(5, 13), 0, F(12, 13), 0),
        (F(8, 17), 0, 0, F(15, 17)),
        (F(7, 25), F(24, 25), 0, 0),
    ]]
    for q in qs:
        checked('unit_quaternion_fixture', sum(x*x for x in q) == 1)
    checked('ordered_refinement_composition',
            product(qs) == qmul(product(qs[:2]), product(qs[2:])))
    checked('inverse_oriented_path',
            qinv(product(qs)) == product([qinv(q) for q in reversed(qs)]))
    hs, hm, ht = qs[0], qs[1], qs[2]
    u, v = qs[2], qs[3]
    lhs = qmul(product([hs, u, qinv(hm)]), product([hm, v, qinv(ht)]))
    checked('gauge_cancellation_at_midpoint', lhs == product([hs, u, v, qinv(ht)]))
    checked('negative_control_reordered_word', qmul(u, v) != qmul(v, u))


# Sparse polynomials: exact monomial exponent tuples -> rational coefficients.
def clean(p):
    return {k: v for k, v in p.items() if v}


def padd(p, q):
    out = dict(p)
    for k, v in q.items():
        out[k] = out.get(k, F(0)) + v
    return clean(out)


def pscale(c, p):
    return clean({k: F(c)*v for k, v in p.items()})


def pmul(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            k = tuple(ai+bi for ai, bi in zip(a, b))
            out[k] = out.get(k, F(0)) + x*y
    return clean(out)


def pconst(n, c):
    return {} if not c else {(0,)*n: F(c)}


def pvar(n, i):
    k = [0]*n
    k[i] = 1
    return {tuple(k): F(1)}


def pdiff(p, i):
    out = {}
    for a, c in p.items():
        if a[i]:
            b = list(a)
            b[i] -= 1
            out[tuple(b)] = c*a[i]
    return out


def xleft(p, n, offset, axis):
    w, x, y, z = [pvar(n, offset+i) for i in range(4)]
    fields = [
        [pscale(-F(1, 2), x), pscale(F(1, 2), w),
         pscale(-F(1, 2), z), pscale(F(1, 2), y)],
        [pscale(-F(1, 2), y), pscale(F(1, 2), z),
         pscale(F(1, 2), w), pscale(-F(1, 2), x)],
        [pscale(-F(1, 2), z), pscale(-F(1, 2), y),
         pscale(F(1, 2), x), pscale(F(1, 2), w)],
    ]
    out = {}
    for i, coeff in enumerate(fields[axis]):
        out = padd(out, pmul(coeff, pdiff(p, offset+i)))
    return out


def casimir(p, n, offset):
    out = {}
    for axis in range(3):
        out = padd(out, pscale(-1, xleft(xleft(p, n, offset, axis),
                                         n, offset, axis)))
    return out


def compose(p, values, target_n):
    out = {}
    for powers, c in p.items():
        term = pconst(target_n, c)
        for value, power in zip(values, powers):
            for _ in range(power):
                term = pmul(term, value)
        out = padd(out, term)
    return out


def polynomial_casimir_checks():
    v = [pvar(8, i) for i in range(8)]
    # Original ordered quaternion product, as four polynomials.
    signs_pairs = [
        [(1, 0, 4), (-1, 1, 5), (-1, 2, 6), (-1, 3, 7)],
        [(1, 0, 5), (1, 1, 4), (1, 2, 7), (-1, 3, 6)],
        [(1, 0, 6), (-1, 1, 7), (1, 2, 4), (1, 3, 5)],
        [(1, 0, 7), (1, 1, 6), (-1, 2, 5), (1, 3, 4)],
    ]
    values = []
    for terms in signs_pairs:
        p = {}
        for sign, i, j in terms:
            p = padd(p, pscale(sign, pmul(v[i], v[j])))
        values.append(p)
    for exponents in itertools.product(range(4), repeat=4):
        if sum(exponents) > 3:
            continue
        p = {exponents: F(1)}
        pulled = compose(p, values, 8)
        lhs = padd(casimir(pulled, 8, 0), casimir(pulled, 8, 4))
        rhs = pscale(2, compose(casimir(p, 4, 0), values, 8))
        checked('two_subedge_Casimir_monomial_degree_at_most_3', lhs == rhs)
    p = pvar(4, 0)
    pulled = compose(p, values, 8)
    checked('negative_control_missing_kinetic_factor_two',
            padd(casimir(pulled, 8, 0), casimir(pulled, 8, 4)) !=
            compose(casimir(p, 4, 0), values, 8))


def trace_energy_checks():
    coords = [pvar(4, i) for i in range(4)]
    trace = pscale(2, coords[0])
    gamma = {}
    for axis in range(3):
        dx = xleft(trace, 4, 0, axis)
        checked('loop_trace_original_generator_derivative',
                dx == pscale(-1, coords[axis+1]))
        gamma = padd(gamma, pmul(dx, dx))
    sphere = {}
    for coord in coords:
        sphere = padd(sphere, pmul(coord, coord))
    # Exact polynomial identity in all four raw quaternion coordinates.
    # Restriction to the original SU(2) sphere uses sphere == 1.
    checked('loop_trace_derivative_squares_plus_trace_square',
            padd(gamma, pscale(F(1, 4), pmul(trace, trace))) == sphere)
    checked('fundamental_trace_original_Casimir',
            casimir(trace, 4, 0) == pscale(F(3, 4), trace))


def series_product(a, b, order):
    zq = (F(0),)*4
    out = [zq for _ in range(order+1)]
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            if i+j <= order:
                out[i+j] = qadd(out[i+j], qmul(ai, bj))
    return out


def exp_series(q, order):
    out = []
    power = (F(1), F(0), F(0), F(0))
    for k in range(order+1):
        out.append(qscale(F(1, math.factorial(k)), power))
        power = qmul(power, q)
    return out


def plaquette_checks():
    X = (F(0), F(1, 2), F(0), F(0))
    Y = (F(0), F(0), F(1, 2), F(0))
    out = [(F(1), F(0), F(0), F(0))]
    for q in [X, Y, qscale(-1, X), qscale(-1, Y)]:
        out = series_product(out, exp_series(q, 6), 6)
    comm = qadd(qmul(X, Y), qscale(-1, qmul(Y, X)))
    checked('plaquette_positive_commutator_coefficient', out[2] == comm)
    checked('magnetic_trace_fourth_order_coefficient', -2*out[4][0] == F(1, 4))
    checked('magnetic_trace_lower_orders', all(out[k][0] == 0 for k in [1, 2, 3]))
    checked('negative_control_commutator_sign', out[2] != qscale(-1, comm))


def schur_checks():
    # A = 0 (vacuum) direct-sum C^T C on seven other coordinates.
    lower = zero(7, 7)
    for i in range(7):
        lower[i][i] = F(i+1)
        if i:
            lower[i][i-1] = F(1)
    positive = mul(tr(lower), lower)
    A = zero(8, 8)
    for i in range(7):
        for j in range(7):
            A[i+1][j+1] = positive[i][j]
    R = zero(8, 6)
    for i in range(6):
        R[i+1][i] = F(i+1)
        R[7][i] = F(1)
    G = mul(tr(R), R)
    checked('raw_Gram_retained_nonidentity_fixture', G != eye(6))
    P = mul(mul(R, inv(G)), tr(R))
    Q = sub(eye(8), P)
    checked('raw_projection_idempotence', mul(P, P) == P)
    checked('raw_projection_self_adjoint', tr(P) == P)
    checked('raw_projection_range', mul(P, R) == R)
    B = mul(mul(Q, A), R)
    for s in [F(3, 7), F(11, 5)]:
        As = add(A, scale(s, eye(8)))
        # This inverse equals (D+s)^-1 on Q and identity on P.
        extended = inv(add(mul(mul(Q, As), Q), P))
        W = mul(mul(Q, extended), Q)
        lift = sub(R, mul(W, B))
        memory = mul(mul(tr(B), W), B)
        red = sub(add(mul(mul(tr(R), A), R), scale(s, G)), memory)
        derivative = add(G, mul(mul(tr(B), mul(W, W)), B))
        checked('Schur_eliminated_boundary', mul(mul(Q, As), lift) == zero(8, 6))
        checked('Schur_raw_derivative_Gram', mul(tr(lift), lift) == derivative)
        checked('Schur_restored_energy', mul(mul(tr(lift), As), lift) == red)
        checked('Schur_full_compressed_resolvent',
                mul(mul(tr(R), inv(As)), R) == mul(mul(G, inv(red)), G))
        checked('negative_control_omitted_raw_Gram_factors',
                mul(mul(tr(R), inv(As)), R) != inv(red))
    return {'A': [[str(x) for x in row] for row in A],
            'R': [[str(x) for x in row] for row in R],
            'G': [[str(x) for x in row] for row in G]}


def composition_and_jet_checks():
    As = [
        [[F(2), F(1)], [F(1), F(3)]],
        [[F(5), F(2), F(1)], [F(2), F(4), F(0)], [F(1), F(0), F(6)]],
        [[F(7), F(1), F(0), F(0)], [F(1), F(8), F(2), F(0)],
         [F(0), F(2), F(9), F(1)], [F(0), F(0), F(1), F(10)]],
    ]
    J01 = [[F(1), F(0)], [F(0), F(1)], [F(0), F(0)]]
    J12 = [[F(1), F(0), F(0)], [F(0), F(1), F(0)],
           [F(0), F(0), F(1)], [F(0), F(0), F(0)]]
    D01 = sub(mul(As[1], J01), mul(J01, As[0]))
    D12 = sub(mul(As[2], J12), mul(J12, As[1]))
    J02 = mul(J12, J01)
    checked('complete_refinement_defect_composition',
            sub(mul(As[2], J02), mul(J02, As[0])) ==
            add(mul(D12, J01), mul(J12, D01)))
    s = F(2, 3)
    R0 = inv(add(As[0], scale(s, eye(2))))
    R1 = inv(add(As[1], scale(s, eye(3))))
    checked('complete_refinement_resolvent_defect',
            sub(mul(R1, J01), mul(J01, R0)) == scale(-1, mul(mul(R1, D01), R0)))
    # Compare the derivative product rule with multiplication of retained jets.
    f = [F(2), F(-3), F(5), F(7), F(-11), F(13), F(17)]
    g = [F(-1), F(4), F(6), F(-2), F(9), F(8), F(3)]
    for k in range(7):
        ordinary = sum((f[j]*g[k-j] for j in range(k+1)), F(0))
        product_rule = sum((F(math.comb(k, j))*math.factorial(j)*f[j]*
                            math.factorial(k-j)*g[k-j]
                            for j in range(k+1)), F(0))/math.factorial(k)
        checked('retained_jet_product_coefficient', ordinary == product_rule)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('verification.json'))
    args = parser.parse_args()
    quaternion_checks()
    polynomial_casimir_checks()
    trace_energy_checks()
    plaquette_checks()
    fixture = schur_checks()
    composition_and_jet_checks()
    source_hash = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    report = {
        'status': 'passed',
        'arithmetic': 'exact fractions, sparse polynomials, finite formal series',
        'total_assertions': sum(CHECKS.values()),
        'checks': CHECKS,
        'finite_matrix_fixture': fixture,
        'script_sha256': source_hash,
        'scope': 'Finite algebraic sign, domain-coordinate, and raw-Gram checks; '
                 'not a numerical Yang-Mills spectrum or a formal proof of the analytic limits.',
    }
    args.output.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': report['status'],
                      'total_assertions': report['total_assertions'],
                      'check_families': len(CHECKS),
                      'report': str(args.output)}, indent=2))


if __name__ == '__main__':
    main()
