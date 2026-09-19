"""Small independent checks of recovered formulas; not the historical test suites."""
import json

import mpmath as mp
import sympy as sp


def require(value, name):
    if not value:
        raise RuntimeError(name)


def main():
    # Tracefree strain eigenvalues: exact constraint and inverse identities.
    x, y, z = sp.symbols("x y z", real=True)
    strain = [x, y, -x-y]
    chi = sp.sqrt(1 + sp.Rational(4, 3)*sum(v*v for v in strain))
    pw = sp.Rational(1, 4)-sp.Rational(3, 4)/chi
    pt = [sp.Rational(1, 4)+(sp.Rational(1, 4)+v)/chi for v in strain]
    require(sp.simplify(pw+sum(pt)-1) == 0, "Kasner trace")
    require(sp.simplify(pw**2+sum(v*v for v in pt)-1) == 0, "Kasner norm")
    for p, b in zip(pt, strain):
        require(sp.simplify((3*p+pw-1)/(1-4*pw)-b) == 0, "Kasner inverse")

    # Hydrodynamic pole recursion through q^10, with z=q^2.
    aa = -z/2-3*z**2/sp.Integer(16)-29*z**3/sp.Integer(192)
    aa -= 2843*z**4/sp.Integer(18432)+392029*z**5/sp.Integer(2211840)
    series = sum((aa+2*j)*(z/4)**j/sp.factorial(j)/sp.rf(1+aa, j)
                 for j in range(6))
    require(sp.series(series, z, 0, 6).removeO() == 0, "Bessel pole series")

    # Independent multiprecision collision. These are floating point checks.
    mp.mp.dps = 65
    F = lambda a, q: (mp.besseli(a-1, q)+mp.besseli(a+1, q))/2
    a, q = mp.findroot((lambda a, q: F(a, q),
                       lambda a, q: mp.diff(lambda u: F(u, q), a)),
                      (mp.mpf("-.57"), mp.mpf(".778")))
    fa = mp.diff(lambda u: F(u, q), a)
    f2 = mp.diff(lambda u: F(u, q), a, 2)
    f3 = mp.diff(lambda u: F(u, q), a, 3)
    fq = mp.diff(lambda u: F(a, u), q)
    I = mp.besseli(a, q)
    Ia = mp.diff(lambda u: mp.besseli(u, q), a)
    A2 = -2*I/(q*f2)
    A1 = 2j*Ia/(q*f2)-2j*I*f3/(3*q*f2**2)
    cluster = (-1j*A1-A2)*mp.exp(a)
    require(abs(F(a, q)) < mp.mpf("1e-55"), "collision residual")
    require(abs(fa) < mp.mpf("1e-55"), "collision order derivative")
    require(fq > 0 and f2 > 0, "numerical nondegeneracy")
    require(abs(cluster-mp.mpf("0.890541413053366943423735889253")) < mp.mpf("1e-29"),
            "cluster limit")
    print(json.dumps({
        "status": "passed",
        "scope": "Exact Kasner identities and five series coefficients; floating point collision and Laurent data.",
        "working_decimal_precision": mp.mp.dps,
        "qc": mp.nstr(q, 44), "alpha_c": mp.nstr(a, 44),
        "Fq": mp.nstr(fq, 44), "F_alpha_alpha": mp.nstr(f2, 44),
        "A_minus_2": mp.nstr(A2, 44), "A_minus_1": mp.nstr(A1, 44),
        "cluster_at_time_one": mp.nstr(cluster, 44),
        "residual": mp.nstr(abs(F(a, q)), 8),
        "limitations": "Not interval certified, not a spectral enumeration, not a PDE or upstream NS proof."
    }, indent=2))


if __name__ == "__main__":
    main()
