from fractions import Fraction as F
from math import comb


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mscale(c, A):
    return [[c * A[i][j] for j in range(len(A[0]))] for i in range(len(A))]


def mmul(A, B):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def mt(A):
    return [list(row) for row in zip(*A)]


def eye(n):
    return [[F(int(i == j)) for j in range(n)] for i in range(n)]


def inv2(A):
    d = A[0][0] * A[1][1] - A[0][1] * A[1][0]
    return [[A[1][1] / d, -A[0][1] / d],
            [-A[1][0] / d, A[0][0] / d]]


# Two exact positive-semidefinite atomic matrix weights on x in (0,1].
xs = [F(1, 2), F(1, 3)]
weights = [
    [[F(1), F(1, 2)], [F(1, 2), F(1)]],
    [[F(2), F(-1, 3)], [F(-1, 3), F(1)]],
]


def moment(m):
    out = [[F(0), F(0)], [F(0), F(0)]]
    for x, W in zip(xs, weights):
        out = madd(out, mscale(x ** m, W))
    return out


# Coordinate-level Bernstein-moment identity from the research note.
N = 7

def f(x):
    return 3 + 2 * x + x * x

lhs = [[F(0), F(0)], [F(0), F(0)]]
for x, W in zip(xs, weights):
    BN = F(0)
    for k in range(N + 1):
        BN += f(F(k, N)) * comb(N, k) * x ** k * (1 - x) ** (N - k)
    lhs = madd(lhs, mscale(BN, W))

rhs = [[F(0), F(0)], [F(0), F(0)]]
for k in range(N + 1):
    for j in range(N - k + 1):
        c = f(F(k, N)) * comb(N, k) * comb(N - k, j) * ((-1) ** j)
        rhs = madd(rhs, mscale(c, moment(k + j)))

assert lhs == rhs

# Smooth raw-frame congruence and its explicit inverse preserve every matrix atom.
T = [[F(2), F(1)], [F(1), F(1)]]
Ti = inv2(T)
assert mmul(Ti, T) == eye(2)
assert mmul(T, Ti) == eye(2)

for W in weights:
    WT = mmul(mt(T), mmul(W, T))
    recovered = mmul(mt(Ti), mmul(WT, Ti))
    assert recovered == W

# Zero atoms are preserved in both directions by the same typed maps.
Z = [[F(0), F(0)], [F(0), F(0)]]
ZT = mmul(mt(T), mmul(Z, T))
assert ZT == Z
assert mmul(mt(Ti), mmul(ZT, Ti)) == Z

print("PASS: exact Bernstein-moment identity and raw-frame inverse congruence")
