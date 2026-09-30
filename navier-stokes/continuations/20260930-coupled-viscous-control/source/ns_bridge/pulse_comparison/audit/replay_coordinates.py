import sympy as S

# Moving-frame symbols.  A prime denotes d/dv; rho is allowed to move.
s, sp, rho, rhop = S.symbols('s sp rho rhop', nonzero=True)
kt, kz, ktp, kzp = S.symbols('k_theta k_z k_theta_p k_z_p', real=True)
F, gt, gz = S.symbols('F g_theta g_z', real=True)
fr, ft, fz = S.symbols('f_r f_theta f_z')
x, y = S.symbols('x y')

K = S.Matrix([kt, kz])
N = S.Matrix([kz, -kt])
Kp = S.Matrix([ktp, kzp])
Np = S.Matrix([kzp, -ktp])
e = S.Matrix([1, -s*kt, -s*kz])
n = rho*S.Matrix([s, kt, kz])
ep = S.Matrix([0, -sp*kt-s*ktp, -sp*kz-s*kzp])
Np3 = S.Matrix([0, kzp, -ktp])
nprime = rhop*S.Matrix([s,kt,kz]) + rho*S.Matrix([sp,ktp,kzp])
U = S.Matrix.hstack(e, S.Matrix([0,kz,-kt]))
Ul = S.diag(1/(1+s**2), 1) * U.T
MatK = S.Matrix([[0,-2*F,0],[2*F+gt,0,0],[gz,0,0]])
Up = S.Matrix.hstack(ep, Np3)

# Reduce polynomial numerators modulo the two exact unit-frame identities.
# Rational denominators in this replay are independent of kt,kz,ktp,kzp.
unit_groebner = S.groebner(
    [kt**2 + kz**2 - 1, kt*ktp + kz*kzp], ktp, kzp, kz, kt, order="lex", domain=S.EX
)
def red(q):
    q = S.cancel(q)
    num, den = S.fraction(q)
    rem = unit_groebner.reduce(S.expand(num))[1]
    return S.factor(rem / den)


assert all(red((Ul*U-S.eye(2))[i,j]) == 0 for i in range(2) for j in range(2))
assert red((Ul*n)[0]) == 0 and red((Ul*n)[1]) == 0

C = Ul*(-MatK*U-Up)
C_expected = S.Matrix([
    [(s*(kt*gt+kz*gz)-s*sp)/(1+s**2),
     (2*F*kz + s*(kt*kzp-kz*ktp))/(1+s**2)],
    [-(2*F*kz + gt*kz-gz*kt) + s*(kz*ktp-kt*kzp), 0],
])
for i in range(2):
    for j in range(2):
        assert red(C[i,j]-C_expected[i,j]) == 0, (i,j,red(C[i,j]-C_expected[i,j]))


# Projected source coordinates; orthogonal projection may be omitted after Ul.
f = S.Matrix([fr,ft,fz])
f_expected = S.Matrix([
    (fr-s*(kt*ft+kz*fz))/(1+s**2),
    kz*ft-kt*fz,
])
assert all(red(v)==0 for v in (Ul*f-f_expected))

# Pressure numerator S = n.K t - n'.t + n.f, with t=x e+y N.
t = U*S.Matrix([x,y])
pressure_bracket = S.expand((n.T*MatK*t)[0] - (nprime.T*t)[0] + (n.T*f)[0])
pressure_expected = rho*(
    x*(2*F*(1+s**2)*kt + kt*gt+kz*gz-sp)
    + y*(-2*F*s*kz + (kt*kzp-kz*ktp))
    + s*fr + kt*ft+kz*fz
)
assert red(pressure_bracket-pressure_expected) == 0

# Stress/energy identity (real amplitudes; for complex amplitudes take Re).
gN = gt*kz-gz*kt
gK = gt*kt+gz*kz
Kt = MatK*t
stress = S.expand((t.T*Kt)[0])
assert red(stress - (-s*gK*x**2 + gN*x*y)) == 0

print('PASS moving-frame coordinate identities')
print('C=', C_expected)
print('fhat=', f_expected)
print('pressure_bracket=', pressure_expected)
print('stress=', -s*gK*x**2+gN*x*y)
