"""Independent polynomial differentiation and original-edge geometry checks."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from collections import Counter, defaultdict
from datetime import datetime, timezone
import json, hashlib

ROOT = Path(__file__).resolve().parent
INPUT = ROOT.parent / 'FOURTH_SCHUR_COEFFICIENT.md'
u, b, c = F(7,3888), -F(301,2956824), -F(55,3639168)
hc, he, hm, hk = F(19,3032640), F(19,59136480), -F(4,616005), F(164,6283251)
d = F(107,34992)
H = {'path_center':hc, 'path_endpoint':he, 'common_edge':hm, 'corner':hk}

def shift(n, i, delta=1):
    q = list(n)
    q[i] += delta
    return tuple(q)

def edges(p):
    n, i, j = p[:3], p[3], p[4]
    return frozenset(((n, i), (shift(n,i), j), (shift(n,j), i), (n, j)))

def neighbors(p):
    out = set()
    for n, i in edges(p):
        for j in range(3):
            if j == i:
                continue
            axes = tuple(sorted((i,j)))
            out.add(n + axes)
            out.add(shift(n,j,-1) + axes)
    out.remove(p)
    return frozenset(out)

def all_triples(p):
    out = set()
    for q in neighbors(p):
        for r in neighbors(p) | neighbors(q):
            if r not in (p,q):
                out.add(tuple(sorted((p,q,r))))
    return out

def triple_type(p, triple):
    counts = {q: sum(bool(edges(q) & edges(r)) for r in triple if r != q) for q in triple}
    if sum(counts.values()) == 4:
        return 'path_center' if counts[p] == 2 else 'path_endpoint'
    assert sum(counts.values()) == 6
    common = set(edges(triple[0])) & set(edges(triple[1])) & set(edges(triple[2]))
    assert len(common) <= 1
    return 'common_edge' if common else 'corner'

anchor = (0,0,0,0,1)
counts = Counter(triple_type(anchor, t) for t in all_triples(anchor))
assert len(neighbors(anchor)) == 12
assert counts == {'path_center':46, 'path_endpoint':92, 'common_edge':12, 'corner':8}
s, pair_diag, pair_off = F(1,81)-15*u, -(9*b+3*c), -(6*b+12*c)
anti = -6*(hc-he)
assert s == -F(19,1296)
assert pair_diag == F(15163,15769728)
assert pair_off == F(347,438048)
assert anti == -F(703,19712160)
row_bound = abs(s)+12*(abs(pair_diag)+abs(pair_off))+15*sum(counts[k]*abs(v) for k,v in H.items())+30*d
column_bound = abs(s)+12*(abs(pair_diag)+abs(pair_off))
column_bound += 46*(3*hc+12*he)+92*(9*he+6*hc)+15*(12*abs(hm)+8*abs(hk))+30*d
assert row_bound == column_bound == F(4574447,33510672)
assert row_bound < F(137,1000)

def in_box(p,L):
    return all(-L <= n[k] <= L for n,i in edges(p) for k in range(3)) and all(-L <= shift(n,i)[k] <= L for n,i in edges(p) for k in range(3))

def cube_faces(n):
    out = []
    for i,j in combinations(range(3),2):
        k = 3-i-j
        out.extend((n+(i,j), shift(n,k)+(i,j)))
    return tuple(out)

def evaluate_box(L):
    faces = tuple(n+(i,j) for n in product(range(-L,L+1),repeat=3) for i,j in combinations(range(3),2) if n[i] < L and n[j] < L)
    face_set = frozenset(faces)
    assert all(in_box(p,L) for p in faces)
    pairs = {tuple(sorted((p,q))) for p in faces for q in neighbors(p) if q in face_set}
    triples = set()
    for p in faces:
        triples.update(t for t in all_triples(p) if set(t) <= face_set)
    cubes = [cube_faces(n) for n in product(range(-L,L),repeat=3)]
    polynomial = []
    for p in faces:
        polynomial.append((p,{p:5},u))
    for p,q in pairs:
        polynomial.extend(((p,{p:3,q:2},b),(q,{q:3,p:2},b),(p,{p:1,q:4},c),(q,{q:1,p:4},c)))
    for t in triples:
        for p in t:
            polynomial.append((p,{q:(1 if q == p else 2) for q in t},H[triple_type(p,t)]))
    for cub in cubes:
        for p in cub:
            polynomial.append((p,{q:1 for q in cub if q != p},d))
    # This is literal differentiation of each displayed degree-five monomial,
    # followed by evaluation at all source parameters equal to one.
    G4 = defaultdict(F)
    multiplicities = Counter()
    for output, powers, coefficient in polynomial:
        assert sum(powers.values()) == 5
        for input_face, exponent in powers.items():
            G4[output,input_face] += 3*exponent*coefficient
            multiplicities[exponent] += 1
    S4 = {pair:-value for pair,value in G4.items()}
    for p in faces:
        S4[p,p] += F(1,81)
    S4 = {pair:value for pair,value in S4.items() if value}
    degree = {p:len(neighbors(p) & face_set) for p in faces}
    # Assemble Q28 by geometry rather than differentiating source monomials.
    formula = defaultdict(F)
    for p in faces:
        formula[p,p] = s+degree[p]*pair_diag
        for q in neighbors(p) & face_set:
            formula[p,q] += pair_off
    for t in triples:
        for p in t:
            eta = H[triple_type(p,t)]
            formula[p,p] -= 3*eta
            for q in t:
                if q != p:
                    formula[p,q] -= 6*eta
    for cub in cubes:
        for p,q in product(cub,repeat=2):
            if p != q:
                formula[p,q] -= 3*d
    formula = {pair:value for pair,value in formula.items() if value}
    assert S4 == formula
    row_sums, column_sums = defaultdict(F), defaultdict(F)
    defects = 0
    for (p,q),value in S4.items():
        expected = anti*(degree[p]-degree[q]) if q in neighbors(p) else F(0)
        actual = value-S4.get((q,p),F(0))
        assert actual == expected
        defects += bool(actual)
        row_sums[p] += abs(value)
        column_sums[q] += abs(value)
    assert max(row_sums.values()) <= row_bound
    assert max(column_sums.values()) <= column_bound
    p,q = (-2,-2,-2,0,1),(-1,-2,-2,1,2)
    example = {'p':p,'q':q,'degrees':[degree[p],degree[q]],'pq':str(S4[p,q]),'qp':str(S4[q,p]),'difference':str(S4[p,q]-S4[q,p])}
    assert S4[p,q]-S4[q,p] == F(703,4928040)
    return {'L':L,'original_faces':len(faces),'unordered_adjacent_pairs':len(pairs),'connected_triples':len(triples),'contained_cubes':len(cubes),'displayed_polynomial_monomials':len(polynomial),'derivative_multiplicity_counts':dict(multiplicities),'nonzero_S4_entries':len(S4),'nonzero_ordered_antisymmetric_entries':defects,'max_absolute_row_sum':str(max(row_sums.values())),'max_absolute_column_sum':str(max(column_sums.values())),'derivative_and_entry_formulas_agree':True,'every_commutator_entry_agrees':True,'boundary_example':example}

result = {'observed_at':datetime.now(timezone.utc).isoformat(),'source_file':'../FOURTH_SCHUR_COEFFICIENT.md','source_sha256':hashlib.sha256(INPUT.read_bytes()).hexdigest(),'scope':'Independent algebra from displayed Q20 coefficients; does not rederive other fifth-source coefficients from the original recurrence.','inverse_correction':'1/81','self_entry':str(s),'pair_diagonal':str(pair_diag),'pair_offdiagonal':str(pair_off),'antisymmetric_factor':str(anti),'bulk_geometry_counts':dict(counts),'row_bound':str(row_bound),'column_bound':str(column_bound),'bound_less_than_137_over_1000':True,'finite_box_check':evaluate_box(2)}
(ROOT/'FOURTH_ALGEBRA_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
