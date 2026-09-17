"""Independent exact one-face character recurrence, through degree six."""
from fractions import Fraction as Q
import json
from platform import python_version

N = 6
A = [[Q(0) for _ in range(N + 1)] for _ in range(N + 2)]
A[0][0] = Q(1)
E = [Q(0) for _ in range(N + 1)]
for n in range(1, N + 1):
    E[n] = -A[1][n - 1]
    for m in range(1, N + 1):
        A[m][n] = (
            A[m - 1][n - 1] + A[m + 1][n - 1]
            + sum(E[k] * A[m][n - k] for k in range(1, n + 1))
        ) / Q(m * (m + 2))

def add(a, b, scale=Q(1)):
    z = dict(a)
    for m, c in b.items():
        z[m] = z.get(m, Q(0)) + scale * c
    return {m: c for m, c in z.items() if c}

def mul(a, b):
    z = {}
    for m, c in a.items():
        for p, d in b.items():
            for q in range(abs(m - p), m + p + 1, 2):
                z[q] = z.get(q, Q(0)) + c * d
    return {m: c for m, c in z.items() if c}

u = [{}] + [{m: A[m][n] for m in range(N + 1) if A[m][n]}
            for n in range(1, N + 1)]
power = [{0: Q(1)}] + [{} for _ in range(N)]
S = [{} for _ in range(N + 1)]
for k in range(1, N + 1):
    next_power = [{} for _ in range(N + 1)]
    for n in range(N + 1):
        for a in range(n + 1):
            next_power[n] = add(next_power[n], mul(power[a], u[n - a]))
    power = next_power
    for n in range(N + 1):
        S[n] = add(S[n], power[n], Q((-1) ** (k + 1), k))

assert E[6] == -Q(289, 77760)
assert S[4] == {0: Q(55, 10368), 2: Q(17, 10368), 4: -Q(7, 51840)}
for n in range(N + 1):
    for m in range(N + 1):
        potential = Q(0)
        if n:
            potential = (A[m - 1][n - 1] if m else Q(0)) + A[m + 1][n - 1]
        assert Q(m * (m + 2)) * A[m][n] - potential == sum(
            E[k] * A[m][n - k] for k in range(n + 1)
        )
print(json.dumps({
    'python': python_version(),
    'energy': [str(e) for e in E],
    'wavefunction': [{str(m): str(A[m][n]) for m in range(N + 1) if A[m][n]}
                     for n in range(N + 1)],
    'log_quartic': {str(m): str(c) for m, c in sorted(S[4].items())},
    'all_equations_through_degree_six': True,
}, indent=2))
