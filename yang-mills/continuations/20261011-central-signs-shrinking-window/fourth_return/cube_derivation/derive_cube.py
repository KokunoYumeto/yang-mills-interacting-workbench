from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from datetime import datetime, timezone
import json, hashlib

ROOT = Path(__file__).resolve().parent

def add(v, i):
    z = list(v)
    z[i] += 1
    return tuple(z)

def face_edges(n, i, j):
    # Exact positive-edge labels and original traversal signs.
    return ((n, i, 1), (add(n, i), j, 1), (add(n, j), i, -1), (n, j, -1))

face_data = {
    'B': ((0, 0, 0), 0, 1),
    'T': ((0, 0, 1), 0, 1),
    'S': ((0, 0, 0), 0, 2),
    'N': ((0, 1, 0), 0, 2),
    'W': ((0, 0, 0), 1, 2),
    'E': ((1, 0, 0), 1, 2),
}
edges = {p: face_edges(*v) for p, v in face_data.items()}
edge_sets = {p: {(n, i) for n, i, s in w} for p, w in edges.items()}
A = frozenset('TSNWE')
subsets = [frozenset(C) for k in range(1, 6) for C in combinations(sorted(A), k)]

def multiplicities(B):
    result = {}
    for p in B:
        for e in edge_sets[p]:
            result[e] = result.get(e, 0) + 1
    return result

def casimir(B):
    # Retain original 3/4 on each singly occurring edge and 0(0+1) on each pair.
    m = multiplicities(B)
    return sum((F(3, 4) if r == 1 else F(0) * (F(0) + 1)) for r in m.values())

a = {}
split_data = {}
for B in subsets:
    if len(B) == 1:
        a[B] = F(1, 3)
        continue
    rows = []
    s = F(0)
    for k in range(1, len(B)):
        for Ct in combinations(sorted(B), k):
            C = frozenset(Ct)
            D = B - C
            weight = casimir(C) + casimir(D) - casimir(B)
            term = weight * a[C] * a[D]
            rows.append({'C': ''.join(sorted(C)), 'D': ''.join(sorted(D)), 'c_C': str(casimir(C)), 'c_D': str(casimir(D)), 'weight': str(weight), 'term_before_denominator': str(term)})
            s += term
    a[B] = s / (2 * casimir(B))
    split_data[''.join(sorted(B))] = rows

all_m = multiplicities(A)
assert len(all_m) == 12
assert sum(r == 1 for r in all_m.values()) == 4
assert sum(r == 2 for r in all_m.values()) == 8
assert {e for e, r in all_m.items() if r == 1} == edge_sets['B']
assert all(casimir(B) > 0 for B in subsets)

# Independent unweighted subset recurrence, derived directly from edge pair counts.
a2 = {}
for B in subsets:
    if len(B) == 1:
        a2[B] = F(1, 3)
        continue
    boundary = sum(r == 1 for r in multiplicities(B).values())
    total = F(0)
    for k in range(1, len(B)):
        for Ct in combinations(sorted(B), k):
            C = frozenset(Ct)
            D = B - C
            shared = len(set(multiplicities(C)) & set(multiplicities(D)))
            total += shared * a2[C] * a2[D]
    a2[B] = total / boundary
assert a == a2

rows = [{'faces': ''.join(sorted(B)), 'cardinality': len(B), 'boundary_edge_count': sum(r == 1 for r in multiplicities(B).values()), 'casimir': str(casimir(B)), 'a': str(a[B])} for B in subsets]
result = {'faces': {p: {'base_vertex': v[0], 'axes_zero_based': v[1:], 'original_word': edges[p]} for p, v in face_data.items()}, 'subset_rows': rows, 'ordered_splits': split_data, 'a_five_faces': str(a[A]), 'haar_multiplier': '1/16', 'projected_fifth_coefficient': str(a[A] / 16), 'inverse_face_pair_coefficient': str(3 * a[A] / 16), 'checks': {'all_31_nonempty_casimirs_positive': True, 'two_exact_recurrences_agree': True, 'original_edge_occurrence_count': {'single': 4, 'double': 8}}}

def qm(q, r):
    w, x, y, z = q
    a0, b0, c0, d0 = r
    return (w*a0-x*b0-y*c0-z*d0, w*b0+x*a0+y*d0-z*c0,
            w*c0-x*d0+y*a0+z*b0, w*d0+x*c0-y*b0+z*a0)

def qc(q):
    return (q[0], -q[1], -q[2], -q[3])

def trace_word(*factors):
    q = (1, 0, 0, 0)
    for r in factors:
        q = qm(q, r)
    return 2*q[0]

# Exact degree-two Haar cubature on the unit-quaternion sphere: the eight
# signed coordinate vectors have the Haar first and second moments.
nodes = [tuple(s if i == k else 0 for i in range(4)) for k in range(4) for s in (-1, 1)]
assert all(sum(q[i] for q in nodes) == 0 for i in range(4))
assert all(sum(q[i]*q[j] for q in nodes) == (2 if i == j else 0) for i in range(4) for j in range(4))
checks = []
boundary_sets = [((1,2,2,0),(2,1,0,2),(0,2,1,2),(2,0,2,1)),
                 ((3,0,0,0),(3,0,0,0),(3,0,0,0),(3,0,0,0)),
                 ((-1,2,2,0),(2,-1,0,2),(0,2,-1,2),(2,0,2,-1))]
for ba, bb, bc, bd in boundary_sets:
    assert all(sum(x*x for x in q) == 9 for q in (ba, bb, bc, bd))
    total = 0
    for ta, tb, tc, td in product(nodes, repeat=4):
        total += (trace_word(ba, qc(ta))*trace_word(bb, qc(tb))*
                  trace_word(bc, qc(tc))*trace_word(bd, qc(td))*
                  trace_word(ta, tb, qc(tc), qc(td)))
    integral = F(total, 3**4 * 8**4)
    expected = F(trace_word(ba, bb, qc(bc), qc(bd)), 3**4 * 16)
    assert integral == expected
    checks.append({'boundary_unit_quaternions_times_3': [ba,bb,bc,bd], 'integral': str(integral), 'missing_trace_divided_by_16': str(expected)})
result['checks']['exact_4096_point_haar_cubatures'] = checks
result['checks']['haar_cubature_scope'] = 'Exact polynomial integration in each of the four gauge-transformed top edge variables, which each have degree at most two; boundary evaluations check the general proof rather than replace it.'
(ROOT / 'CUBE_EXACT_CHECKS.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print('Exact Haar cubatures:', checks)
for row in rows:
    print(row)
print({k: result[k] for k in ('a_five_faces', 'projected_fifth_coefficient', 'inverse_face_pair_coefficient')})
