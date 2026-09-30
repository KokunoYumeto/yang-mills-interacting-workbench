from pathlib import Path
import hashlib, json
import sympy as s

root = Path(__file__).resolve().parent
checks = {}
def equal(name, left, right=0):
    residual = s.simplify(s.expand_complex(left-right))
    checks[name] = residual == 0
    if residual != 0:
        raise AssertionError((name, residual))
def real(value):
    return s.expand_complex(value).as_real_imag()[0]
def kernel(n, m, x, y):
    return (int(n == m)*real(x*s.conjugate(y))+
            int(n == -m)*real(x*y))/2
def wave(n, x):
    return {n: x/2, -n: s.conjugate(x)/2}
def constant_product(a, b):
    return s.expand(sum(value*b.get(-n, 0) for n, value in a.items()))
def add_waves(data):
    result = {}
    for n, x in data:
        for k, value in wave(n, x).items():
            result[k] = result.get(k, 0)+value
    return result

xr, xi, yr, yi, z, y, h, omega, dotomega = s.symbols(
    "xr xi yr yi z y h omega dotomega", real=True)
x, yy = xr+s.I*xi, yr+s.I*yi
for name, n, m in [("equal", 3, 3), ("opposite", 3, -3),
                    ("unmatched", 3, 2)]:
    equal("angular_"+name, constant_product(wave(n, x), wave(m, yy)),
          kernel(n, m, x, yy))
    for signx, signy in [(1, -1), (1, 1), (-1, -1)]:
        equal(f"reflection_{name}_{signx}_{signy}",
              kernel(-n, -m, signx*x, signy*yy),
              signx*signy*kernel(n, m, x, yy))
    xp = x+z*(1+s.I*z)
    yp = yy+z**2*(2-s.I)
    equal("product_derivative_"+name,
          s.diff(kernel(n,m,xp,yp),z),
          kernel(n,m,s.diff(xp,z),yp)+kernel(n,m,xp,s.diff(yp,z)))
equal("negative_kernel", kernel(2,2,s.Integer(1),s.Integer(-1)), -s.Rational(1,2))

# Independent Laurent coefficient assembly of all cross and ordered new pairs.
old = [(-2, [1+z+s.I*y, 2-z+s.I]), (1, [z-s.I*y, y+2*s.I])]
new = [(1, [z**2+s.I*y, 1-z*s.I]),
       (-1, [y+s.I*z, 2+z]), (2, [1-z, y+z*s.I])]
qA = s.symbols("qA", real=True)
for component, sign in [(0, 1), (1, -1)]:
    oz = add_waves([(n,c[0]) for n,c in old])
    os = add_waves([(n,c[component]) for n,c in old])
    vz = add_waves([(n,c[0]) for n,c in new])
    vs = add_waves([(n,c[component]) for n,c in new])
    direct = qA*(constant_product(oz,vs)+constant_product(vz,os))+constant_product(vz,vs)
    expanded = qA*sum(kernel(n,m,a[0],b[component])+kernel(m,n,b[0],a[component])
                       for n,a in old for m,b in new)
    expanded += sum(kernel(n,m,a[0],b[component]) for n,a in new for m,b in new)
    equal(f"full_stress_{component}", direct, expanded)
    differentiated = qA*sum(
        kernel(n,m,s.diff(a[0],z),b[component])+
        kernel(n,m,a[0],s.diff(b[component],z))+
        kernel(m,n,s.diff(b[0],z),a[component])+
        kernel(m,n,b[0],s.diff(a[component],z))
        for n,a in old for m,b in new)
    differentiated += sum(
        kernel(n,m,s.diff(a[0],z),b[component])+
        kernel(n,m,a[0],s.diff(b[component],z))
        for n,a in new for m,b in new)
    equal(f"full_stress_derivative_{component}", s.diff(direct,z), differentiated)
    reflected = qA*sum(
        kernel(-n,-m,a[0],sign*b[component])+
        kernel(-m,-n,b[0],sign*a[component])
        for n,a in old for m,b in new)
    reflected += sum(kernel(-n,-m,a[0],sign*b[component])
                     for n,a in new for m,b in new)
    equal(f"full_stress_reflection_{component}", reflected, sign*direct)
    mean = s.integrate(direct,(y,0,1))
    centered = direct-mean
    equal(f"centering_derivative_{component}", s.diff(centered,z),
          s.diff(direct,z)-s.integrate(s.diff(direct,z),(y,0,1)))

A, D = s.Rational(1,2)+h, s.Rational(1,2)-h
for e in [1,2]:
    alpha = s.Rational(e+1,4)-A
    gamma = s.Rational(e+1,2)-2*A-D
    equal(f"radial_exponent_{e}", gamma, s.Rational(e,2)-2*A+h)
    equal(f"old_derivative_exponent_{e}",
          gamma+A+D-s.Rational(e+1,4)+dotomega,alpha+dotomega)
    equal(f"old_field_exponent_{e}",
          gamma+A-s.Rational(e+1,4)+omega,alpha+omega-D)
    equal(f"quadratic_exponent_{e}", gamma, -h if e == 2 else -s.Rational(1,2)-h)

psi = z**3+2*z
b = (1+z)+s.I*(2-z*z)
current = b
for m in range(1,4):
    current = s.diff(current,z)+s.I*s.diff(psi,z)*current
    # Factor out the nonvanishing phase before exact polynomial comparison.
    expression = s.expand(s.diff(b*s.exp(s.I*psi),z,m)/s.exp(s.I*psi))
    equal(f"phase_recurrence_{m}", expression, current)
f = z**2*s.cos(2*s.pi*y)
equal("zero_haar_mean", s.integrate(f,(y,0,1)))
equal("nonzero_evaluated_derivative", s.diff(f,z).subs(y,0), 2*z)

def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
receipt = {
    "schema": "evaluated-flux-symbolic-v2", "all_passed": all(checks.values()),
    "checks_total": len(checks), "checks": checks,
    "body_sha256": sha(root/"evaluation_flux_body.tex"),
    "script_sha256": sha(Path(__file__)),
    "scope": "Exact algebra replay complements the complete written finite proofs; no complete source theorem certification or uniform infinite estimate."
}
(root/"replay_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({"all_passed":receipt["all_passed"],"checks_total":len(checks)}))
