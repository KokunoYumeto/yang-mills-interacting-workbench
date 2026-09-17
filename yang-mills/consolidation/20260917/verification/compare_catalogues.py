"""Exact independent trace-word -> tree-quaternion catalogue comparison.

Reads both preserved packages, uses rational sparse polynomials without importing
either package, and prints one deterministic evidence record. Run under a bounded
process wrapper. The equalities are in Q[q]/(sum(q_i^2)-1), not sampled values.
"""
from __future__ import annotations
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIRST = ROOT / 'continuations/20260917-quartic-cube/generated'
SECOND = ROOT / 'continuations/20260917-quartic-independent/results'
HASHES = {}


def require(ok, message):
    if not ok:
        raise ArithmeticError(message)


def load(path):
    raw = path.read_bytes()
    HASHES[path.relative_to(ROOT).as_posix()] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)


class PolynomialRing:
    def __init__(self, chords):
        self.n = 4 * chords
        self.zero = (0,) * self.n

    def constant(self, c):
        return {self.zero: F(c)} if c else {}

    def variable(self, i):
        a = list(self.zero)
        a[i] = 1
        return {tuple(a): F(1)}

    def add(self, *polys):
        out = defaultdict(F)
        for poly in polys:
            for powers, c in poly.items():
                out[powers] += c
        return {p: c for p, c in out.items() if c}

    def scale(self, c, poly):
        return {p: c*v for p, v in poly.items() if c*v}

    @lru_cache(maxsize=200000)
    def reduce_monomial(self, powers):
        for k in range(0, self.n, 4):
            if powers[k] >= 2:
                p = list(powers)
                p[k] -= 2
                out = defaultdict(int, self.reduce_monomial(tuple(p)))
                for j in range(1, 4):
                    p[k+j] += 2
                    for q, c in self.reduce_monomial(tuple(p)):
                        out[q] -= c
                    p[k+j] -= 2
                return tuple((q, c) for q, c in out.items() if c)
        return ((powers, 1),)

    def multiply(self, left, right):
        raw = defaultdict(F)
        for a, c in left.items():
            for b, d in right.items():
                raw[tuple(x+y for x, y in zip(a, b))] += c*d
        out = defaultdict(F)
        for p, c in raw.items():
            if c:
                for q, v in self.reduce_monomial(p):
                    out[q] += c*v
        return {q: c for q, c in out.items() if c}

    def quaternion_product(self, a, b):
        out = [dict() for _ in range(4)]
        # Hamilton basis 1,i,j,k; i*j=k, j*k=i, k*i=j.
        for i in range(4):
            for j in range(4):
                if i == 0:
                    target, sign = j, 1
                elif j == 0:
                    target, sign = i, 1
                elif i == j:
                    target, sign = 0, -1
                else:
                    target = 6-i-j
                    sign = 1 if (i, j) in ((1,2), (2,3), (3,1)) else -1
                out[target] = self.add(out[target], self.scale(sign, self.multiply(a[i], b[j])))
        return out


def edge_endpoints(edge):
    a = tuple(edge[:3]); b = list(a); b[edge[3]] += 1
    return a, tuple(b)


def face_word(face):
    x, y, z, i, j = face
    n = (x, y, z); ni = list(n); nj = list(n)
    ni[i] += 1; nj[j] += 1
    return ((n+(i,), 1), (tuple(ni)+(j,), 1),
            (tuple(nj)+(i,), -1), (n+(j,), -1))


def check_tree(edges, tree, chords):
    require(set(tree).isdisjoint(chords) and set(tree) | set(chords) == set(edges), 'tree/chord partition')
    vertices = {v for e in edges for v in edge_endpoints(e)}
    require(len(tree) == len(vertices)-1, 'tree size')
    adjacency = defaultdict(set)
    for e in tree:
        a, b = edge_endpoints(e); adjacency[a].add(b); adjacency[b].add(a)
    seen = {min(vertices)}; stack = list(seen)
    while stack:
        for v in adjacency[stack.pop()]:
            if v not in seen:
                seen.add(v); stack.append(v)
    require(seen == vertices, 'tree connectivity')


def trace_word(word, edge_ids, chord_lookup, ring):
    q = [ring.constant(1), {}, {}, {}]
    start = None; previous = None
    for signed in word:
        edge = edge_ids[abs(signed)]
        a, b = edge_endpoints(edge)
        if signed < 0:
            a, b = b, a
        if start is None:
            start = a
        else:
            require(previous == a, 'trace word is not an oriented edge walk')
        previous = b
        if edge in chord_lookup:
            j = chord_lookup[edge]
            z = [ring.variable(4*j+k) for k in range(4)]
            if signed < 0:
                z[1:] = [ring.scale(-1, x) for x in z[1:]]
            q = ring.quaternion_product(q, z)
    require(start == previous, 'trace word is not closed')
    return ring.scale(2, q[0])


def transform_face(face, perm, signs, shift):
    vertices = set(v for edge, _ in face_word(face) for v in edge_endpoints(edge))
    mapped = [tuple(signs[k]*v[perm[k]]-shift[k] for k in range(3)) for v in vertices]
    low = tuple(min(v[k] for v in mapped) for k in range(3))
    axes = tuple(k for k in range(3) if any(v[k] != low[k] for v in mapped))
    return low+axes


def transport_faces(faces, perm, signs, shift):
    require(sorted(perm) == [0,1,2] and set(signs) <= {-1,1}, 'invalid signed permutation')
    return tuple(sorted(transform_face(p, perm, signs, shift) for p in faces))


def main():
    first = load(FIRST / 'quartic_coefficients.json')
    geo = load(SECOND / 'quartic_geometric_classes.json')
    by_faces = {tuple(map(tuple, x['faces'])): x for x in first}
    require(len(by_faces) == len(first) == len(geo['classes']) == 78, 'class counts')
    results = []; trace_terms = 0; quaternion_terms = 0; verified_words = 0
    for index, item in enumerate(geo['classes']):
        second = load(SECOND / f'quartic_coefficients/class_{index:02d}.json')
        faces = tuple(map(tuple, item['faces_with_multiplicity']))
        require(tuple(map(tuple, second['faces_with_multiplicity'])) == faces, 'second geometry cross-reference')
        original = by_faces[faces]
        model = second['model']
        edges = tuple(map(tuple, model['original_edges']))
        tree = tuple(map(tuple, model['original_tree']))
        chords = tuple(map(tuple, model['chords']))
        check_tree(edges, tree, chords)
        edge_ids = {}
        for ident, (a, b) in original['edge_coordinates']:
            a, b = tuple(a), tuple(b)
            delta = tuple(y-x for x, y in zip(a, b))
            require(delta.count(1) == 1 and delta.count(0) == 2, 'positive edge convention')
            edge_ids[ident] = a+(delta.index(1),)
        require(set(edge_ids.values()) == set(edges), 'edge dictionaries differ')
        chord_lookup = {e:j for j, e in enumerate(chords)}
        R = PolynomialRing(len(chords)); words = {}
        converted = {}
        for term in original['coefficients']:
            product = R.constant(F(term['coefficient']))
            for word in term['words']:
                word = tuple(word)
                if word not in words:
                    words[word] = trace_word(word, edge_ids, chord_lookup, R)
                product = R.multiply(product, words[word])
            converted = R.add(converted, product)
        expected = {tuple(x['powers']): F(x['coefficient']) for x in second['coefficient_polynomial']}
        difference = R.add(converted, R.scale(-1, expected))
        require(not difference, f'polynomial mismatch class {index}: {len(difference)} terms')
        # Independently confirm the slice's elementary face traces.
        inverse_ids = {e: ident for ident, e in edge_ids.items()}
        require(tuple(sorted(set(faces))) == tuple(map(tuple, model['faces'])), 'face order')
        for face, stored in zip(model['faces'], model['plaquette_polynomials']):
            word = tuple(sign*inverse_ids[edge] for edge, sign in face_word(face))
            value = trace_word(word, edge_ids, chord_lookup, R)
            require(value == {tuple(x['powers']):F(x['coefficient']) for x in stored}, 'plaquette slice mismatch')
        trace_terms += len(original['coefficients']); quaternion_terms += len(expected); verified_words += len(words)
        results.append({'first_index': original['index'], 'second_index': index,
                        'faces': [list(x) for x in faces], 'chords': len(chords),
                        'trace_terms': len(original['coefficients']), 'quaternion_terms': len(expected),
                        'difference_terms': len(difference)})
        print(f'Exact catalogue identity class {index:02d}: {len(original["coefficients"])} trace terms -> {len(expected)} quaternion monomials', file=__import__('sys').stderr, flush=True)
        R.reduce_monomial.cache_clear()
    ta = load(FIRST / 'quartic_transports.json')
    tb = load(SECOND / 'anchored_quartic_transports.json')
    transports_a = {}; transports_b = {}; same_maps = 0
    for row in ta:
        target = tuple(map(tuple, row['representative']))
        for entry in row['images']:
            source = tuple(map(tuple, entry['original']))
            require(source not in transports_a, 'duplicate first transport')
            require(transport_faces(source, entry['permutation'], entry['signs'], entry['offset']) == target, 'first transport formula')
            transports_a[source] = (target, tuple(entry['permutation']), tuple(entry['signs']), tuple(entry['offset']))
    for row in tb['rows']:
        source = tuple(map(tuple, row['original_face_multiset']))
        target = tuple(map(tuple, geo['classes'][row['class_index']]['faces_with_multiplicity']))
        require(source not in transports_b, 'duplicate second transport')
        require(transport_faces(source, row['coordinate_permutation'], row['coordinate_signs'], row['subtracted_translation']) == target, 'second transport formula')
        transports_b[source] = (target, tuple(row['coordinate_permutation']), tuple(row['coordinate_signs']), tuple(row['subtracted_translation']))
    require(len(transports_a) == len(transports_b) == 8621, 'transport cardinality')
    require(transports_a.keys() == transports_b.keys(), 'anchored families differ')
    for source in transports_a:
        require(transports_a[source][0] == transports_b[source][0], 'orbit assignments differ')
        same_maps += transports_a[source] == transports_b[source]
    require(trace_terms == 743 and quaternion_terms == 4044, 'term total')
    output = {'schema': 'ym-exact-catalogue-bridge-v1', 'passed': True,
              'coefficient_domain': 'Q; exact fractions in the independent product-of-3-spheres coordinate ring',
              'quotient_relations': 'q_(4j)^2 = 1 - q_(4j+1)^2 - q_(4j+2)^2 - q_(4j+3)^2',
              'map': 'first original positive tree edge -> identity; positive chord c_j -> q0 I - i sum(q_a sigma_a); inverse edge -> quaternion conjugate; trace -> twice scalar part',
              'classes': len(results), 'first_trace_terms': trace_terms,
              'second_quaternion_terms': quaternion_terms, 'distinct_closed_words_checked_by_class': verified_words,
              'anchored_multisets': len(transports_a), 'identical_chosen_transports': same_maps,
              'class_results': results, 'input_sha256': HASHES,
              'non_claims': ['Does not certify analytic norm bounds or a continuum limit.', 'Does not replace separate checks that each catalogue solves the original differential recurrence.']}
    print(json.dumps(output, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
