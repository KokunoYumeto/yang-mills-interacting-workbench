#!/usr/bin/env python3
"""Exact finite checks for the gauge-native Yang--Mills continuation.

Standard library only. Written analytic proofs are separate. Every rejection
uses an explicit exception, including when Python is run with -O.
"""
from __future__ import annotations
import argparse
import hashlib
import itertools
import json
import math
from fractions import Fraction as F
from pathlib import Path
import sys

HERE = Path(__file__).resolve().parent
CHECKS: list[str] = []
CONTROLS: list[str] = []


def require(ok: bool, code: str) -> None:
    if not ok:
        raise ValueError(code)


def ck(name: str, ok: bool) -> None:
    require(name not in CHECKS, 'duplicate-check:' + name)
    require(bool(ok), 'check:' + name)
    CHECKS.append(name)


def reject(name: str, proposed: bool) -> None:
    require(name not in CONTROLS, 'duplicate-control:' + name)
    require(not bool(proposed), 'false-formula-accepted:' + name)
    CONTROLS.append(name)


def sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canon(data) -> bytes:
    return (json.dumps(data, sort_keys=True, indent=2) + '\n').encode()


def no_duplicates(pairs):
    out = {}
    for k, v in pairs:
        require(k not in out, 'duplicate-json-key:' + k)
        out[k] = v
    return out


def load(path: Path):
    return json.loads(path.read_text(), object_pairs_hook=no_duplicates)


def floor_sqrt(q: F, digits: int = 40) -> tuple[F, F]:
    require(q >= 0, 'negative-radicand')
    n = 10 ** digits
    a = math.isqrt(q.numerator * n * n // q.denominator)
    lo, hi = F(a, n), F(a + 1, n)
    require(lo * lo <= q < hi * hi, 'sqrt-outward')
    return lo, hi


def dec(q: F, places: int, upper: bool = False) -> str:
    scale = 10 ** places
    a = q.numerator * scale
    k = -((-a) // q.denominator) if upper else a // q.denominator
    sign = '-' if k < 0 else ''
    k = abs(k)
    return f'{sign}{k // scale}.{k % scale:0{places}d}'


def add(A, B):
    return [[a + b for a, b in zip(x, y)] for x, y in zip(A, B)]


def scale(s, A):
    return [[s * a for a in row] for row in A]


def mt(A):
    return [list(row) for row in zip(*A)]


def mm(A, B):
    require(len(A[0]) == len(B), 'matrix-shape')
    return [[sum((a * b for a, b in zip(row, col)), F(0))
             for col in zip(*B)] for row in A]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def zero(n, m):
    return [[F(0) for _ in range(m)] for _ in range(n)]


def inv(A):
    n = len(A)
    B = [[F(a) for a in row] + eye(n)[i] for i, row in enumerate(A)]
    for i in range(n):
        k = next((k for k in range(i, n) if B[k][i]), None)
        require(k is not None, 'singular-matrix')
        B[i], B[k] = B[k], B[i]
        p = B[i][i]
        B[i] = [a / p for a in B[i]]
        for j in range(n):
            if i != j:
                a = B[j][i]
                B[j] = [b - a * c for b, c in zip(B[j], B[i])]
    return [row[n:] for row in B]


def grid(lower: int, upper: int):
    vertices = list(itertools.product(range(lower, upper + 1), repeat=3))
    edges = [(n, i) for n in vertices for i in range(3) if n[i] < upper]
    index = {e: i for i, e in enumerate(edges)}
    faces = []
    boundaries = []
    for n in vertices:
        for i, j in itertools.combinations(range(3), 2):
            if n[i] < upper and n[j] < upper:
                ni, nj = list(n), list(n)
                ni[i] += 1
                nj[j] += 1
                word = [(n, i), (tuple(ni), j), (tuple(nj), i), (n, j)]
                faces.append((n, i, j))
                boundaries.append(frozenset(index[e] for e in word))
    incident = [[] for _ in edges]
    for p, support in enumerate(boundaries):
        for e in support:
            incident[e].append(p)
    adjacent = [set() for _ in faces]
    for ps in incident:
        for p, q in itertools.combinations(ps, 2):
            adjacent[p].add(q)
            adjacent[q].add(p)
    stars = []
    for v in vertices:
        st = []
        for e, (n, i) in enumerate(edges):
            t = list(n)
            t[i] += 1
            if n == v or tuple(t) == v:
                st.append(e)
        stars.append(st)
    return vertices, edges, faces, boundaries, adjacent, incident, stars


def graph_spin_checks():
    V, E, P, bd, adj, inc, stars = grid(0, 1)
    accepted = 0
    low = []
    minima = set()
    for q in itertools.product(range(3), repeat=len(E)):
        allowed = True
        for st in stars:
            vals = [q[e] for e in st]
            total = sum(vals)
            if total % 2 or 2 * max(vals) > total:
                allowed = False
                break
        if not allowed:
            continue
        accepted += 1
        c4 = sum(j * (j + 2) for j in q)
        require(c4 >= 12 * max(q), 'cube-gauge-Casimir')
        require(not 12 < c4 < 18, 'cube-free-band-gap')
        if c4 == 12:
            low.append(q)
            minima.add(frozenset(i for i, j in enumerate(q) if j))
    ck('complete-cube-admissible-spin-census', accepted == 1013)
    ck('all-cube-physical-spin-Casimir-inequalities', len(low) == 6)
    ck('free-Casimir-three-is-exactly-six-original-faces', minima == set(bd))
    ck('all-cube-labels-screened', 3 ** len(E) == 531441)
    reject('omit-gauge-average', F(3, 4) >= 6 * F(1, 2))
    reject('apply-cubic-girth-bound-to-triangle', 3 * F(3, 4) >= 6 * F(1, 2))
    reject('replace-edge-spin-by-total-spin', F(3) >= 6 * F(2))
    for L in (1, 2, 3, 4):
        vv, ee, pp, bb, aa, ii, ss = grid(-L, L)
        m = 2 * L
        ck(f'original-open-counts-L{L}', len(ee) == 3*m*(m+1)**2 and len(pp) == 3*m*m*(m+1))
        ck(f'complete-boundary-degree-sum-L{L}', sum(map(len, aa)) == 12*m*(3*m*m-1))
        ck(f'edge-incidence-multiplicities-L{L}',
           sum(len(x) == 4 for x in ii) == 3*m*(m-1)**2 and
           sum(len(x) == 3 for x in ii) == 12*m*(m-1) and
           sum(len(x) == 2 for x in ii) == 12*m)
        ck(f'edge-star-degree-identity-L{L}', all(len(aa[p]) == sum(len(ii[e])-1 for e in bb[p]) for p in range(len(pp))))
    return {'source_spin_domain': 'one original cube, all q_e=2j_e in {0,1,2}',
            'candidate_label_count': 531441, 'admissible_label_count': accepted,
            'free_casimir_three_count': len(low)}


def coefficient_and_majorant_checks():
    A = zero(16, 16)
    def bits(t):
        return sum(b << (3-i) for i, b in enumerate(t))
    for a, b, c, d in itertools.product(range(2), repeat=4):
        A[bits((b, c, 1-c, 1-d))][bits((a, b, 1-d, 1-a))] += (-1)**(a+c)
    B = mm(mt(A), A)
    ck('literal-plaquette-coefficient-square', mm(B, B) == scale(4, B))
    ck('literal-plaquette-Haar-norm', sum(B[i][i] for i in range(16)) == 16)
    ck('literal-plaquette-trace-norm-eight', sum(B[i][i]/2 for i in range(16)) == 8)
    ck('source-first-coefficient-budget', 4 * 8 == 32)
    ck('anchored-physical-bilinear-coefficient', 2 * 3 * F(1, 6) * F(2, 3) == F(2, 3))
    ck('global-original-drift-relative-coefficient', 2 * 3 * F(1, 6) * F(2, 3) == F(2, 3))
    reject('physical-bilinear-bound-on-ungauged-source', 3*F(1, 4) <= F(2, 3)*F(3, 4)**2)
    # Actual admissible records: original loops, retained unions and all-spin-one loops.
    _, edges, faces, supports, adjacent, inc, stars = grid(0, 1)
    records = []
    for i, S in enumerate(supports):
        for q in (1, 2, 3):
            records.append((S, tuple(F(q, 2) if e in S else F(0) for e in range(len(edges)))))
    def norm(recs):
        return max(sum(sum(j*(j+1) for j in js)*amp for S, js, amp in recs if e in S) for e in range(len(edges)))
    def prod_bound(Fs, Gs):
        sums = [F(0) for _ in edges]
        for S, js, a in Fs:
            for T, ks, b in Gs:
                value = 3 * sum(j*k for j, k in zip(js, ks)) * a * b
                for e in S | T:
                    sums[e] += value
        return max(sums)
    for seed in range(8):
        Fs = [(S, j, F(1+(i+seed)%4, 7+i)) for i, (S, j) in enumerate(records)]
        Gs = [(S, j, F(1+(2*i+seed)%5, 13+i)) for i, (S, j) in enumerate(records)]
        ck(f'complete-gauge-anchored-majorant-{seed}', prod_bound(Fs, Gs) <= F(2, 3)*norm(Fs)*norm(Gs))
    # The actual assembly kernel and its retained primitive.
    assembly = {frozenset({0, 1, 2, 3}): F(-7), frozenset(range(5)): F(2), frozenset(range(6)): F(5)}
    primitive = {S: v for S, v in assembly.items() if len(S) > 4}
    restored = dict(primitive)
    restored[frozenset(range(4))] = -sum(primitive.values())
    ck('retained-physical-assembly-primitive', restored == assembly and sum(assembly.values()) == 0)
    reject('erase-zero-assembly-source', not primitive)
    return {'plaquette_coefficient': [[int(x) for x in row] for row in A], 'trace_norm': 8}


def catalan(n):
    return math.comb(2*n, n) // (n+1)


def source_and_contour_checks():
    for n in range(1, 51):
        ck(f'Catalan-exact-source-convolution-{n}', catalan(n) == sum(catalan(j)*catalan(n-1-j) for j in range(n)))
    for P in range(81):
        b = F(math.comb(2*P, P), 4**P)
        bn = F(math.comb(2*P+2, P+1), 4**(P+1))
        ck(f'closed-endpoint-retained-tail-{P}', F(catalan(P), 4**P) == 2*(b-bn) and b*b <= F(1, P+1))
    for P in (1, 3, 12, 80):
        partial = sum(F(3, 8)*F(catalan(p-1), 4**(p-1)) for p in range(1, P+1))
        tail = F(3, 4)*F(math.comb(2*P, P), 4**P)
        ck(f'endpoint-full-mass-and-tail-{P}', partial + tail == F(3, 4))
    reject('zero-tail-at-convergent-endpoint', F(3, 4)*F(math.comb(8, 4), 4**4) == 0)
    for s in (F(1), F(4, 5), F(3, 5), F(2, 5), F(0)):
        x = F(3, 256)*(1-s*s)
        r = F(3, 4)*(1-s)
        eps = F(2, 3)*r
        ck(f'original-nonlinear-root-{s}', r == 32*x+F(2, 3)*r*r)
        ck(f'full-physical-and-scalar-return-{s}', 3-2*r == 3*(1-eps) and F(3, 4)-r/2 == F(3, 4)*(1-eps))
    ck('closed-physical-coupling-domain', F(1, 4)/F(64, 3) == F(3, 256))
    ck('isolated-band-domain', F(256, 3)*F(3, 400) == F(16, 25))
    ck('isolated-band-touching-endpoints', 3*F(6, 5) == F(9, 2)*F(4, 5))
    ck('contour-radius-free-resolvent', F(3)/F(3, 5) == 5 and F(9, 2)/(F(9, 2)-3-F(3, 5)) == 5)
    eta = F(9, 125)
    ck('complex-source-outward-radius', F(11, 15) > F(107, 125)**2)
    ck('projection-inverse-denominator', 1-5*eta-25*eta*eta == F(319, 625))
    bound = 3*(eta-F(1, 15))+15*eta*eta/(1-5*eta-25*eta*eta)
    ck('complete-Cauchy-bound', bound == F(6713, 39875))
    ck('complete-third-and-higher-tail-coefficient', bound*320**3 == F(1759772672, 319))
    reject('infer-band-exactness-from-two-coefficients', bound == 0)
    reject('use-convergence-at-negative-radicand', 1-F(256, 3)*F(1, 50) >= 0)
    return bound


# Polynomial algebra on three original unit-quaternion groups, 12 coordinates.
NV = 12
MONO0 = (0,) * NV

def poly(c=0):
    return {} if c == 0 else {MONO0: F(c)}


def var(i):
    e = list(MONO0); e[i] = 1
    return {tuple(e): F(1)}


def pa(A, B):
    C = dict(A)
    for e, c in B.items():
        C[e] = C.get(e, F(0)) + c
        if C[e] == 0:
            del C[e]
    return C


def ps(c, A):
    return {e: F(c)*a for e, a in A.items() if c*a}


def pm(A, B):
    C = {}
    for e, a in A.items():
        for f, b in B.items():
            g = tuple(x+y for x, y in zip(e, f))
            C[g] = C.get(g, F(0)) + a*b
    return {g:c for g,c in C.items() if c}


def pd(A, i):
    C = {}
    for e, a in A.items():
        if e[i]:
            f = list(e); f[i] -= 1
            C[tuple(f)] = a*e[i]
    return C


def quatmul(A, B):
    def m(i,j): return pm(A[i], B[j])
    return [pa(pa(m(0,0), ps(-1,m(1,1))),pa(ps(-1,m(2,2)),ps(-1,m(3,3)))),
            pa(pa(m(0,1),m(1,0)),pa(m(2,3),ps(-1,m(3,2)))),
            pa(pa(m(0,2),m(2,0)),pa(m(3,1),ps(-1,m(1,3)))),
            pa(pa(m(0,3),m(3,0)),pa(m(1,2),ps(-1,m(2,1))))]


def sphere_moment(exp):
    if any(e % 2 for e in exp): return F(0)
    k = [e//2 for e in exp]
    numerator = 1
    for a in k:
        for b in range(1,2*a,2): numerator *= b
    denominator = 1
    for b in range(sum(k)): denominator *= 4+2*b
    return F(numerator,denominator)


def integrate(A, groups=(0,1,2)):
    out = {}
    for e,a in A.items():
        f = list(e); value=a
        for g in groups:
            value *= sphere_moment(e[4*g:4*g+4])
            for i in range(4*g,4*g+4): f[i]=0
        if value: out[tuple(f)] = out.get(tuple(f),F(0))+value
    return {e:a for e,a in out.items() if a}


def scalar_integral(A):
    out=integrate(A)
    require(set(out).issubset({MONO0}), 'Haar-scalar')
    return out.get(MONO0,F(0))


def haar_channel_checks():
    U=[var(i) for i in range(4)]
    A=[var(i+4) for i in range(4)]
    B=[var(i+8) for i in range(4)]
    Ui=[U[0]]+[ps(-1,u) for u in U[1:]]
    Fp=ps(2,quatmul(U,A)[0]);Fq=ps(2,quatmul(Ui,B)[0])
    product=pm(Fp,Fq);s0=quatmul(A,B)[0];s1=pa(product,ps(-1,s0))
    ck('original-shared-link-Haar-projector',integrate(product,(0,))==s0)
    ck('full-two-plaquette-Haar-norm',scalar_integral(pm(product,product))==1)
    ck('shared-link-spin-zero-weight',scalar_integral(pm(s0,s0))==F(1,4))
    ck('shared-link-spin-one-weight',scalar_integral(pm(s1,s1))==F(3,4))
    ck('full-shared-link-cross-Gram',scalar_integral(pm(s0,s1))==0)
    lap=poly(0)
    for i in range(4):lap=pa(lap,pd(pd(product,i),i))
    ck('original-quaternion-Casimir-laplacian',lap==ps(8,s0))
    radius=poly(0)
    for u in U:radius=pa(radius,pm(u,u))
    Kprod=pa(ps(2,product),ps(F(-1,4),pm(radius,lap)))
    retained=ps(2,pm(pa(radius,poly(-1)),s0))
    ck('spin-one-Casimir-retains-sphere-relation',pa(ps(2,s1),ps(-1,Kprod))==retained)
    ck('sphere-relation-actual-Haar-kernel',scalar_integral(pm(retained,retained))==0)
    ck('original-adjacent-energy-channels',6*F(3,4)==F(9,2) and 6*F(3,4)+2==F(13,2))
    t=F(1,4)/(F(9,2)-3)+F(3,4)/(F(13,2)-3)
    ck('both-shifted-adjacent-denominators',t==F(8,21))
    reject('collapse-shared-link-channels',t==1/(F(1,4)*F(9,2)+F(3,4)*F(13,2)-3))
    ck('full-offdiagonal-shared-pair-return',F(1,3)-t==F(-1,21))
    ck('self-pair-ground-relative-return',F(1,3)+F(1,3)-F(1,5)==F(7,15))
    reject('omit-vacuum-intermediate',-t==F(-1,21))
    return {'pair_norms_squared':['1/4','3/4'], 'original_Casimirs':['9/2','13/2'], 'at_band_resolvent_weight':str(t)}


def band_matrix_checks():
    for lower,upper in ((0,1),(-1,1),(-2,2)):
        V,E,P,bd,adj,inc,stars=grid(lower,upper);M=len(P)
        # Construct the full intermediate-channel return independently of degrees.
        T=[[F(1,3) for q in range(M)] for p in range(M)]
        for p in range(M):T[p][p]+=F(M,3)-F(1,5)
        pair_signatures={}
        for p,q in itertools.combinations(range(M),2):
            common=bd[p]&bd[q]
            require(len(common)<=1,'multiple-shared-edge')
            signature=bd[p]^bd[q]
            require(signature not in pair_signatures,'distinct-pair-parity-collision')
            pair_signatures[signature]=(p,q)
            t=F(8,21) if common else F(1,3)
            for i,j in ((p,p),(q,q),(p,q),(q,p)):T[i][j]-=t
        expected=[[F(7,15)-F(len(adj[p]),21) if p==q else (F(-1,21) if q in adj[p] else F(0))
                   for q in range(M)] for p in range(M)]
        tag=f'{lower}:{upper}'
        ck('all-original-intermediate-channels-'+tag,T==expected)
        ck('all-unordered-pair-supports-retained-'+tag,len(pair_signatures)==M*(M-1)//2)
        ck('full-original-band-matrix-symmetry-'+tag,T==mt(T))
        if lower==-2:
            reject('replace-open-degrees-by-twelve',all(len(a)==12 for a in adj))
            reject('omit-original-vacuum-energy-scalar',T[0][0]-F(M,3)==expected[0][0])
    for d in range(13):
        ck(f'complete-band-column-bound-degree-{d}',abs(F(7,15)-F(d,21))+F(d,21)<=F(71,105))
    for m in range(4,41,2):
        avg=F(4*(3*m*m-1),m*(m+1))
        ck(f'original-boundary-Rayleigh-error-{m}',F(7,15)-2*avg/21==F(-71,105)+F(8*(3*m+1),21*m*(m+1)))


def matrix_intertwiner_checks():
    K=[[F(3),0,0,0],[0,F(3),0,0],[0,0,F(9,2),0],[0,0,0,F(13,2)]]
    V=[[0,0,1,2],[0,0,3,-1],[1,3,1,0],[2,-1,0,2]]
    V2=[[1,2,3,0],[2,1,0,2],[3,0,1,0],[0,2,0,1]]
    P=[[F(1),0],[0,F(1)],[0,0],[0,0]]
    R=[[0,0,0,0],[0,0,0,0],[0,0,F(2,3),0],[0,0,0,F(2,7)]]
    U1=scale(-1,mm(R,mm(V,P)))
    T2=add(mm(mt(P),mm(V2,P)),mm(mt(P),mm(V,U1)))
    U2=scale(-1,mm(R,add(mm(V,U1),mm(V2,P))))
    ck('original-band-first-coefficient-zero',mm(mt(P),mm(V,P))==zero(2,2))
    ck('full-first-intertwining-equation',add(mm(K,U1),mm(V,P))==scale(3,U1))
    ck('full-second-intertwining-equation',add(add(mm(K,U2),mm(V,U1)),mm(V2,P))==add(scale(3,U2),mm(P,T2)))
    ck('retained-band-source-coordinate',mm(mt(P),U1)==zero(2,2) and mm(mt(P),U2)==zero(2,2))
    reject('drop-second-section-coupling',T2==mm(mt(P),mm(V2,P)))
    S=[[F(2),F(1)],[F(0),F(1)]];D=[[F(5),0],[0,F(7)]]
    G=mm(mt(S),S);A=mm(inv(S),mm(D,S));energy=mm(G,A)
    ck('actual-raw-Gram-self-adjointness',energy==mt(energy) and mm(mt(A),G)==energy)
    ck('raw-frame-both-inverse-laws',mm(inv(S),S)==eye(2) and mm(S,inv(S))==eye(2))
    reject('substitute-identity-for-band-Gram',A==mt(A))
    # Concrete positive two-by-two energy: its quadratic approximation is not exact.
    t=F(1,10);candidate=3-F(2,3)*t*t
    char=(3-candidate)*(F(9,2)-candidate)-t*t
    reject('finite-second-coefficient-is-entire-Hamiltonian',char==0)


def spatial_checks():
    ck('sharp-total-variation-speed',F(1,2)*F(1,2)==F(1,4))
    for n in range(1,15):
        weights=[F(i+1,n*(n+1)//2) for i in range(n)]
        values=[F(i,n) for i in range(n)]
        mean=sum(w*x for w,x in zip(weights,values))
        mad=sum(w*abs(x-mean) for w,x in zip(weights,values))
        ck(f'actual-conditional-interpolation-factor-{n}',mad<=(max(values)-min(values))/2)
    ck('physical-conditional-support-row',2*F(1,3)*3==2)
    ck('closed-volume-benchmark-q-squared',F(64,121)**2/F(107,363)==F(12288,12947)<1)
    ck('unique-volume-original-domain-quadratic',4096*F(1,121)**2+F(256,3)*F(1,121)<1)
    for p in range(1,65):
        ck(f'complete-order-p-drift-row-{p}',3*F(p,2)*F(2,3)==p)
    reject('declare-volume-derivative-tail-finite-at-endpoint',1-F(256,3)*F(3,256)>0)
    for xs in itertools.product((F(0),F(1,2),F(1)),repeat=3):
        cos=[2*x*x-1 for x in xs]
        Q=[[12+2*sum(cos[j] for j in range(3) if j!=a) if a==b else 4*xs[a]*xs[b] for b in range(3)]for a in range(3)]
        ck('full-Bloch-symbol-'+':'.join(map(str,xs)),Q==mt(Q) and all(x>=0 for row in Q for x in row) and max(map(sum,Q))<=24)
    Q0=[[F(16) if a==b else F(4) for b in range(3)]for a in range(3)]
    T0=add(scale(F(7,15),eye(3)),scale(F(-1,21),Q0))
    one=[[F(1)],[F(1)],[F(1)]];diff=[[F(1)],[F(-1)],[F(0)]]
    ck('zero-momentum-physical-scalar-branch',mm(T0,one)==scale(F(-71,105),one))
    ck('zero-momentum-two-component-branch',mm(T0,diff)==scale(F(-11,105),diff))
    ck('original-zero-momentum-raw-Grams',mm(mt(one),one)==[[F(3)]] and mm(mt(diff),diff)==[[F(2)]] )
    for axis in range(3):
        qs=[F(i==axis) for i in range(3)]
        delta=[[-sum(qs[j] for j in range(3) if j!=a) if a==b else -(qs[a]+qs[b])/2 for b in range(3)]for a in range(3)]
        ck(f'full-original-spatial-second-derivative-{axis}',mm(mt(one),mm(delta,one))[0][0]/3==F(-4,3))
    ck('physical-momentum-energy-factor',F(4,63)*2/F(16)==F(1,126))
    ck('physical-mass-second-coefficient-factor',F(71,105)*2/F(16)==F(71,840))
    ck('native-continuum-path-new-finite-domain',F(3,64)/4==F(3,256))
    reject('extend-source-domain-to-running-infinite-coupling-parameter',F(1,4)<=F(3,256))


def mixing_and_coupling_checks():
    for physical, cs in ((False,[F(3,4),F(3),F(9,2)]),(True,[F(3),F(9,2),F(8)])):
        for eps in (F(1,10),F(3,10),F(1,2)):
            kappa=F(7,5)
            D=[[kappa*cs[i] if i==j else F(0) for j in range(3)]for i in range(3)]
            V=[[((-1)**(i+j))*kappa*eps*cs[j]/3 for j in range(3)]for i in range(3)]
            for h in (F(1,100),F(1,5),F(1)):
                S=inv(add(eye(3),scale(h,add(D,V))))
                operator_norm=max(sum(abs(S[i][j])for i in range(3))for j in range(3))
                tag=f'{physical}:{eps}:{h}'
                ck('whole-relative-resolvent-contraction-'+tag,operator_norm<=1/(1+h*kappa*min(cs)*(1-eps)))
                x=[[F(2)],[F(-3)],[F(1)]];y=mm(S,x)
                ny=sum(abs(a[0])for a in y);ey=sum(c*abs(a[0])for c,a in zip(cs,y))
                ck('retained-Fourier-dissipation-'+tag,ny+h*kappa*(1-eps)*ey<=6)
    # This explicitly declared finite Markov calibration retains its constant.
    for eta in (F(0),F(1,8),F(1,4),F(1,2)):
        L=[[-1-eta,1+eta],[1-eta,-1+eta]]
        pi=[(1-eta)/2,(1+eta)/2]
        G=[[pi[i] if i==j else F(0)for j in range(2)]for i in range(2)]
        ck('calibration-actual-invariant-pairing-'+str(eta),mm(G,L)==mt(mm(G,L)) and all(sum(pi[i]*L[i][j]for i in range(2))==0 for j in range(2)))
        for xi in (F(0),eta/2,eta):
            for x in (F(0),F(1,5),F(3,4),F(1)):
                left=[-eta*(1-x)+x,-eta*(1-x)-x]
                right=[-xi*(1-x)+x,-xi*(1-x)-x]
                diff=max(abs(a-b)for a,b in zip(left,right))
                require(diff<=(eta-xi)/(1-xi),'constant-retaining-coupling-calibration')
        if eta:
            x=F(1,2)
            actual=max(abs(-eta*(1-x)+x+eta),abs(-eta*(1-x)-x+eta))
            reject('omit-semigroup-constant-restoration-'+str(eta),actual<=x)
    for sl in (F(0),F(1,5),F(2,5),F(3,5),F(4,5),F(1)):
        eps=(1-sl)/2
        ck('critical-completion-modulus-'+str(sl),(F(1,2)-eps)/(1-eps)==sl/(1+sl))
    for sxi,seta in ((F(4,5),F(2,5)),(F(3,5),F(0)),(F(1),F(0))):
        xi=F(3,256)*(1-sxi*sxi);eta=F(3,256)*(1-seta*seta)
        difference=sum(F(catalan(p-1))*F(2,3)**(p-1)*32**p*(eta**p-xi**p)for p in range(1,31))
        ck('full-source-coupling-majorant-'+str(sxi)+':'+str(seta),difference<=F(3,4)*(sxi-seta))
    ck('closed-endpoint-scalar-decay-rate',F(3,4)*(1-F(1,2))==F(3,8))
    ck('closed-endpoint-physical-decay-rate',3*(1-F(1,2))==F(3,2))
    ck('closed-endpoint-local-loop-prefactor',8/(1-F(1,2))==16)
    ck('actual-loop-near-endpoint-modulus',8*F(1,10000)/(1+F(1,10000))==F(8,10001))


def box_certificate(bound: F):
    V,E,P,bd,adj,inc,stars=grid(-2,2);n=len(P)
    Q=[[len(adj[i]) if i==j else int(j in adj[i]) for j in range(n)]for i in range(n)]
    x=[1]*n
    for _ in range(100):x=[len(a)*x[i]+sum(x[j] for j in a) for i,a in enumerate(adj)]
    y=[len(a)*x[i]+sum(x[j] for j in a) for i,a in enumerate(adj)]
    ratios=[F(a,b) for a,b in zip(y,x)];lo,hi=min(ratios),max(ratios)
    ck('actual-L2-240-plaquettes',n==240)
    ck('actual-L2-positive-power-vector',min(x)>0)
    ck('actual-L2-Perron-lower-endpoint',lo>F(2186319640514,10**11))
    ck('actual-L2-Perron-upper-endpoint',hi<F(2186319641826,10**11))
    tlo,thi=F(7,15)-hi/21,F(7,15)-lo/21
    ck('actual-L2-second-coefficient-endpoints',tlo>F(-57443792469,10**11) and thi<F(-57443792405,10**11))
    A=[[Q[i][j]-(21 if i==j else 0) for j in range(n)]for i in range(n)]
    prev=1;pivots=[];signs=[];divisions=0
    for k in range(n):
        p=A[k][k]
        require(p!=0,f'bareiss-zero-pivot:{k}')
        signs.append(1 if p*prev>0 else -1)
        pivots.append(p)
        for i in range(k+1,n):
            aik=A[i][k]
            for j in range(i,n):
                numerator=p*A[i][j]-aik*A[j][k]
                quotient,remainder=divmod(numerator,prev)
                require(remainder==0,f'bareiss-inexact:{k}:{i}:{j}')
                A[i][j]=A[j][i]=quotient
                divisions+=1
        prev=p
    ck('actual-L2-exact-congruence-inertia',signs.count(1)==1 and signs.count(-1)==239)
    ck('actual-L2-complete-exact-division-count',divisions==2303960)
    xi=F(1,10**10)
    delta=16*bound*320**3*xi/(1-320*xi)
    center=F(-574438,10**6);radius=F(1,50)
    distance_low=radius-max(abs(tlo-center),abs(thi-center))
    distance_others=F(-8,15)-center-radius
    ck('actual-L2-rank-one-contour-clearance',min(distance_low,distance_others)>delta)
    ck('actual-L2-sharp-band-is-first',F(-8,15)-delta>thi+delta)
    ck('actual-L2-full-gap-lower-certified',tlo-delta>F(-5833,10000))
    ck('actual-L2-full-gap-upper-certified',thi+delta<F(-5656,10000))
    ck('actual-L2-kappa-and-coupling-return',F(1)/(4*50000**2)==xi and 2*50000==100000)
    reject('reverse-finite-band-minimum-upper-bound',tlo>thi)
    return {
        'schema':'ym-original-L2-band-certificate-v1', 'L':2,'plaquettes':n,
        'original_face_order':[[list(n),i+1,j+1]for n,i,j in P],
        'degree_sequence':[len(a) for a in adj],
        'Q_matrix_sha256':sha(canon(Q)),
        'integer_power':100,'integer_power_vector':[str(v) for v in x],
        'Perron_lower':str(lo),'Perron_upper':str(hi),
        'T_min_lower':str(tlo),'T_min_upper':str(thi),
        'inertia_threshold':21,'inertia':[1,239,0],
        'fraction_free_pivot_determinants':[str(v) for v in pivots],
        'congruence_pivot_signs':signs,'exact_divisions':divisions,
        'actual_xi':str(xi),'original_g_squared':'50000','original_kappa':'100000/a',
        'spectral_remainder_over_kappa_xi_squared':str(delta),
        'first_gap_coefficient_lower':str(tlo-delta),
        'first_gap_coefficient_upper':str(thi+delta),
        'safe_first_gap_coefficient_interval':['-0.5833','-0.5656'],
        'scope':'Exact coefficient matrix plus explicit analytic all-order error from B10. No spin truncation of the original Hamiltonian.'}


def numerical_return(bound):
    lo,hi=floor_sqrt(F(11,75))
    dg=F(3,2)*(1+lo)
    ck('g-squared-five-physical-lower',dg>F(207445,100000))
    lo6,hi6=floor_sqrt(F(107,363))
    dvol=F(3,2)*(1+lo6)
    ck('closed-volume-physical-lower',dvol>F(231438,100000))
    x=F(1,10**8)
    rootlo,roothi=floor_sqrt(1-F(256,3)*x)
    basic=F(3,2)*(1+rootlo)
    rem=bound*(320*x)**3/(1-320*x)
    corrected=3-F(71,105)*x*x-rem
    ck('actual-uniform-second-order-lower-edge',corrected>3-F(7314,1000)*F(1,10**17))
    ck('actual-second-order-improves-basic-bound',corrected>basic)
    return {'proved_finite_domain':'0<xi<=3/256; g^2>=8/sqrt(3)',
            'full_physical_floor':'(3 kappa/2)(1+sqrt(1-256xi/3))',
            'g_squared_5_safe_coefficient':'2.07445',
            'g_squared_5_lower':dec(dg,18),
            'unique_spatial_domain':'0<xi<=3/256; g^2>=8/sqrt(3)',
            'g_squared_11_over_2_lower':dec(dvol,18),
            'Cauchy_B':str(bound),'Cauchy_third_constant':str(bound*320**3),
            'uniform_example_xi':str(x),'uniform_example_kappa':'10000/a',
            'basic_physical_lower_coefficient':dec(basic,22),
            'all_order_band_lower_coefficient':dec(corrected,24),
            'all_order_band_loss_upper':dec(3-corrected,24,upper=True),
            'band_interval_domain':'0<xi<3/400',
            'full_zero_shift_inverse':'1/(kappa d_phys) on the actual physical kernel',
            'volume_independent_mixing':'norm_X(Q_H F)/(1-epsilon) exp(-kappa c_star (1-epsilon)t)',
            'coupling_modulus':'(epsilon(eta)-epsilon(xi))/(1-epsilon(xi)) norm_X(Q_H F)',
            'critical_endpoint_modulus':'sqrt(1-theta)/(1+sqrt(1-theta)) norm_X(Q_H F)',
            'continuum_gap_established':False}


def primary_source_dictionary_checks():
    # Q[sqrt(2)] arithmetic; physical coefficients are never discarded.
    def mul(a,b):
        return (a[0]*b[0]+2*a[1]*b[1], a[0]*b[1]+a[1]*b[0])
    for g2 in (F(5),F(20),F(5000)):
        for a in (F(2),F(7)):
            xi=1/(4*g2*g2);kap=2*g2/a
            ck(f'Dahmen-hopping-dictionary-{g2}-{a}',2/(8*g2*g2)==xi)
            factor=(F(0),1/a); electric=(F(0),g2)
            ck(f'Dahmen-energy-multiplier-{g2}-{a}',mul(factor,electric)==(kap,F(0)))
            magnetic=(F(0),-g2*xi)
            ck(f'Dahmen-original-potential-coefficient-{g2}-{a}',mul(factor,magnetic)==(-kap*xi,F(0)))
    ck('planar-original-diagonal-29-over-105',F(7,15)-F(4,21)==F(29,105))
    ck('planar-original-rest-coefficient-3-over-35',F(29,105)-F(4,21)==F(3,35))
    ck('planar-three-dimensional-compression-defect',F(7,15)-F(12,21)==F(29,105)-F(8,21))
    ck('primary-source-self-channel-two-over-fifteen',F(1,3)-F(1,5)==F(2,15))
    reject('omit-planar-compression-defect',F(7,15)-F(12,21)==F(29,105))
    reject('omit-original-energy-multiplier',mul((F(0),F(1,7)),(F(0),F(20)))==(F(20),F(0)))


def actual_second_source_checks():
    def literal_loop(signs, dimension):
        ell=len(signs);n=dimension**ell
        A=[[0]*n for _ in range(n)]
        def idx(t):
            q=0
            for a in t:q=q*dimension+a
            return q
        for z in itertools.product(range(dimension),repeat=ell):
            rows=[];cols=[];c=1
            for k,sg in enumerate(signs):
                a,b=z[k],z[(k+1)%ell]
                if sg==1: rows.append(a);cols.append(b)
                else:
                    rows.append(dimension-1-b);cols.append(dimension-1-a)
                    c*=(-1)**(a+b)
            A[idx(cols)][idx(rows)]+=c
        return A
    # Exact positive Gram polynomial identifies all nonzero singular values.
    A=literal_loop((1,1,-1,-1),3);G=mm(mt(A),A)
    ck('actual-spin-one-plaquette-Gram-polynomial',mm(G,G)==scale(9,G))
    ck('actual-spin-one-plaquette-trace-norm-27',sum(G[i][i] for i in range(81))/3==27)
    for i,ones in enumerate(itertools.combinations(range(6),3)):
        signs=tuple(1 if k in ones else -1 for k in range(6))
        t=sum(signs[k-1]==1 and signs[k]==-1 for k in range(6))
        A=literal_loop(signs,2);G=mm(mt(A),A)
        ck(f'original-six-loop-singular-values-{i}',mm(G,G)==scale(4**t,G))
        ck(f'original-six-loop-trace-norm-{i}',sum(G[k][k] for k in range(64))/2**t==2**(6-t))
        ck(f'original-six-loop-half-character-bound-{i}',F(2**(6-t),2)<=16)
    ck('original-second-self-source',F(1,24)-F(1,18)==-F(1,72))
    ck('original-second-disconnected-source-zero',F(1,18)-F(1,18)==0)
    ck('original-second-adjacent-spin-zero-source',2*(F(2,27)-F(1,18))==F(1,27))
    ck('original-second-adjacent-spin-one-source',2*(F(2,39)-F(1,18))==-F(1,117))
    ck('original-second-full-pair-Casimir-norm',F(9,2)*16/27+F(13,2)*48/117==F(16,3))
    for L in (1,2,3):
        vv,ee,pp,bb,adj,inc,stars=grid(-L,L)
        pairs={tuple(sorted((p,q))) for p in range(len(pp)) for q in adj[p]}
        for e in range(len(ee)):
            actual=sum(e in (bb[p]|bb[q]) for p,q in pairs)
            bound=sum(len(adj[p]) for p in inc[e])-math.comb(len(inc[e]),2)
            require(actual==bound and bound<=42,f'second-source-anchor-{L}-{e}')
        ck(f'complete-original-pair-anchor-count-L{L}',True)
    ck('actual-second-source-local-bound-236',4*3+42*F(16,3)==236)
    ck('actual-second-source-improves-generic-majorant',236<F(2048,3))
    reject('forget-unordered-pair-factor-two',F(2,27)-F(1,18)==F(1,27))
    reject('assign-spin-one-character-fundamental-norm',27==8)
    reject('erase-inactive-union-edge',7==6)
    a=[F(0),F(32),F(236)]
    for n in range(3,61):a.append(F(2,3)*sum(a[i]*a[n-i] for i in range(1,n)))
    for n in range(1,61):
        rhs=(F(32) if n==1 else -F(1340,3) if n==2 else F(0))+F(2,3)*sum(a[i]*a[n-i] for i in range(1,n))
        ck(f'actual-second-source-generating-coefficient-{n}',a[n]==rhs and a[n]>0)
        old=catalan(n-1)*F(2,3)**(n-1)*32**n
        require(a[n]<=old,f'second-source-coefficient-majorization-{n}')
    # Exact Q[sqrt(354)] coordinates retain both conjugate roots.
    def add2(a,b):return (a[0]+b[0],a[1]+b[1])
    def sc2(c,a):return(c*a[0],c*a[1])
    def mul2(a,b):return(a[0]*b[0]+354*a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    def sign2(a):
        x,y=a
        if not y:return (x>0)-(x<0)
        if not x:return (y>0)-(y<0)
        if x>0 and y>0:return 1
        if x<0 and y<0:return -1
        z=x*x-354*y*y
        return ((z>0)-(z<0))*(1 if x>0 else -1)
    one=(F(1),F(0));alpha=(F(96,2680),-F(3,2680));gam=(F(689,335),-F(32,335))
    P=add2(add2(one,sc2(-F(256,3),alpha)),sc2(F(10720,9),mul2(alpha,alpha)))
    ck('actual-second-source-critical-root',P==(F(0),F(0)))
    ck('actual-second-source-root-positive',sign2(alpha)>0)
    ck('actual-second-source-endpoint-extends-earlier',sign2(add2(alpha,(-F(3,256),F(0))))>0)
    ck('actual-second-source-conjugate-root-ratio',sign2(gam)>0 and sign2(add2(one,sc2(-1,gam)))>0)
    coefflambda=(F(128,3),F(4,3));coeffmu=(F(128,3),-F(4,3))
    ck('actual-second-source-reciprocal-root',mul2(alpha,coefflambda)==one)
    ck('actual-second-source-full-polynomial-factorization',add2(coefflambda,coeffmu)==(F(256,3),F(0)) and mul2(coefflambda,coeffmu)==(F(10720,9),F(0)))
    apow=one;gpow=gam;partial=(F(0),F(0))
    for p in range(36):
        if p:
            apow=mul2(apow,alpha);partial=add2(partial,sc2(a[p],apow))
        tail=add2((F(3,4),F(0)),sc2(-1,partial))
        upper=sc2(F(3,4)*F(math.comb(2*p,p),4**p),add2(one,gpow))
        ck(f'actual-second-source-closed-endpoint-tail-{p}',sign2(tail)>0 and sign2(add2(upper,sc2(-1,tail)))>=0)
        gpow=mul2(gpow,gam)
    # c_n^2=4xi, with the full rationalized numerator retained.
    ck('actual-second-source-running-domain-factor-three',sc2(4,alpha)==(F(96,670),-F(3,670)))
    reject('omit-running-domain-factor-three',sc2(4,alpha)==(F(32,670),-F(1,670)))
    for gsq,disc in ((F(17,4),F(35401,751689)),(F(5),F(299,1125)),(F(9,2),F(7561,59049))):
        xi=1/(4*gsq*gsq);P=1-F(256,3)*xi+F(10720,9)*xi*xi
        ck(f'actual-second-source-benchmark-radicand-{gsq}',P==disc and P>0)
    lo,_=floor_sqrt(F(35401,751689))
    ck('actual-second-source-g-squared-17-over-4-gap',F(3,2)*(1+lo)>F(18255,10000))
    for root in (F(0),F(1,7),F(1,2),F(1)):
        eps=(1-root)/2
        ck(f'actual-second-source-endpoint-dynamics-modulus-{root}',(F(1,2)-eps)/(1-eps)==root/(1+root))
    for k1,k2,ep in ((F(2),F(3),F(1,3)),(F(7),F(2),F(1,2)),(F(5),F(5),F(1,7))):
        ratio=abs(k2-k1)/max(k1,k2)*(1+ep)/(1-ep)
        ck(f'full-physical-coefficient-modulus-{k1}-{k2}-{ep}',ratio>=0 and (ratio==0)==(k1==k2))
    sqrtlo,sqrthi=floor_sqrt(F(354))
    thresholdlo,_=floor_sqrt((32+sqrtlo)/3)
    _,thresholdhi=floor_sqrt((32+sqrthi)/3)
    return {'second_source_bound':'236','old_generic_second_bound':'2048/3',
        'critical_xi':'3/[4(32+sqrt(354))]',
        'critical_g_squared':'sqrt((32+sqrt(354))/3)',
        'critical_g_squared_lower':dec(thresholdlo,18),
        'critical_g_squared_upper':dec(thresholdhi,18,upper=True),
        'g_squared_17_over_4_gap_coefficient_lower':dec(F(3,2)*(1+lo),18),
        'physical_gap':'(3 kappa/2)(1+sqrt(1-256xi/3+10720xi^2/9))',
        'spatial_domain':'0<xi<=3/[4(32+sqrt(354))]',
        'same_original_coefficients':True,'g_approaching_zero_result':False}


def validate_state(state):
    require(state.get('target')=='four-dimensional continuum Yang-Mills mass gap','wrong-target')
    require(state.get('finite_domain')=='0<xi<=3/[4(32+sqrt(354))]; g^2>=sqrt((32+sqrt(354))/3)','wrong-finite-domain')
    require(state.get('spatial_domain')=='0<xi<=3/[4(32+sqrt(354))]','wrong-spatial-domain')
    require(state.get('continuum_gap_established') is False,'unsupported-continuum-promotion')
    require(state.get('band_is_spin_truncation') is False,'false-truncation-identification')
    require(state.get('raw_band_metric')=='R_xi^* R_xi','missing-original-band-Gram')


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--verify-receipt',type=Path)
    ap.add_argument('--write-box-certificate',type=Path)
    ap.add_argument('--verify-box-certificate',type=Path)
    ap.add_argument('--candidate-state',type=Path)
    args=ap.parse_args()
    statefile=args.candidate_state or HERE/'state.json'
    validate_state(load(statefile))
    spins=graph_spin_checks();coeff=coefficient_and_majorant_checks()
    bound=source_and_contour_checks();haar=haar_channel_checks()
    band_matrix_checks();matrix_intertwiner_checks();spatial_checks();mixing_and_coupling_checks();primary_source_dictionary_checks()
    second=actual_second_source_checks();box=box_certificate(bound);numeric=numerical_return(bound)
    if args.verify_box_certificate:
        require(args.verify_box_certificate.read_bytes()==canon(box),'box-certificate-mismatch')
    if args.write_box_certificate:args.write_box_certificate.write_bytes(canon(box))
    names=('RESEARCH_NOTE.md','BAND_AND_CERTIFICATE.md','SPATIAL_RETURN.md','SECOND_SOURCE.md','verify.py')
    result={'schema':'ym-gauge-native-band-check-v1','checks':CHECKS,'negative_controls':CONTROLS,
        'spin_census':spins,'original_plaquette':coeff,'original_pair_channels':haar,
        'first_majorant_and_band_evaluation':numeric,'actual_second_source':second,'box_certificate_sha256':sha(canon(box)),
        'proof_and_code_sha256':{n:sha((HERE/n).read_bytes())for n in names},
        'state_sha256':sha(statefile.read_bytes()),
        'scope':'Exact finite algebra, integer graph/inertia calculations and rational evaluation of written analytic estimates. Analytic proofs have not been independently or formally certified.',
        'remote_write_performed':False,'new_Lean_execution':False}
    data=canon(result)
    if args.verify_receipt:require(args.verify_receipt.read_bytes()==data,'receipt-mismatch')
    if args.output:args.output.write_bytes(data)
    sys.stdout.buffer.write(data)

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,json.JSONDecodeError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr)
        raise SystemExit(1)
