"""Bounded exact checks for the accompanying mathematical derivation."""
from pathlib import Path
from collections import Counter
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
x = s.symbols("x0:4", real=True)
y = s.symbols("y0:4", real=True)
X, Y = s.Matrix(x), s.Matrix(y)
q2 = 4*sum(t*t for t in x[1:])
chi = 4*x[0]**2-1
checks = []

def haar_moment(exponents):
    if any(e % 2 for e in exponents):
        return s.Integer(0)
    total = sum(exponents)//2
    numerator = s.prod(s.factorial2(e-1) for e in exponents if e)
    denominator = s.prod(4+2*k for k in range(total))
    return s.Rational(numerator, denominator)

def integrate_x(poly):
    return s.expand(sum(coef*haar_moment(exp)
                        for exp, coef in s.Poly(s.expand(poly), *x).terms()))

assert integrate_x(chi**2) == 1
cross = integrate_x(chi*(4*(X.dot(Y))**2-1))
assert s.expand(cross-(4*y[0]**2-sum(t*t for t in y))/3) == 0
assert integrate_x(x[0]**2*q2) == s.Rational(1,2)
assert integrate_x((1-x[0])**4) == s.Rational(21,8)
checks.append({"identity":"S3 second/fourth moments and full harmonic Gram", "status":"exact"})

# Sum of normal-tangent cross vectors, reduced only by the sphere equation.
unit_remainder = s.groebner([sum(t*t for t in x)-1],x[3],x[2],x[1],x[0])
cross_sum = 0
for alpha in range(1,4):
    A = s.zeros(4)
    A[0,alpha] = A[alpha,0] = 1
    Az = A*X
    cross_sum += 4*(Az.dot(Az)-(X.dot(Az))**2)
expected = 3+16*(x[0]**2-s.Rational(1,4))**2
assert unit_remainder.reduce(s.expand(cross_sum-expected))[1] == 0
checks.append({"identity":"all-centre vector sum = 3+16(c^2-1/4)^2", "status":"exact"})

for alpha in range(1,4):
    e = s.zeros(3,1)
    e[alpha-1] = 1
    spatial = s.Matrix(x[1:])
    dx0 = spatial.dot(e)/2
    dx = -x[0]*e/2-spatial.cross(e)/2
    assert s.expand(dx0-x[alpha]/2) == 0
    derivative_q2 = sum(s.diff(q2,x[j])*dx[j-1] for j in range(1,4))
    assert s.expand(derivative_q2+4*x[0]*x[alpha]) == 0
checks.append({"identity":"original right derivative c'=q_alpha/4, (|q|^2)'=-2c q_alpha", "status":"exact"})

z=s.symbols("z")
trig_checks=[]
for n in range(5,34,2):
    # Exact roots-of-unity algebra, without floating-point trigonometry.
    sin4=sum(s.Rational(3,8)-s.Rational(1,4)*(z**(k%n)+z**((-k)%n))
              +s.Rational(1,16)*(z**((2*k)%n)+z**((-2*k)%n))
              for k in range(n))
    assert s.rem(sin4-s.Rational(3*n,8),s.cyclotomic_poly(n,z),z)==0
    cos2=sum(s.Rational(1,2)+s.Rational(1,4)*
              (z**((2*l+1)%(2*n))+z**((-2*l-1)%(2*n)))
              for l in range(n))
    assert s.rem(cos2-s.Rational(n,2),s.cyclotomic_poly(2*n,z),z)==0
    trig_checks.append(n)
checks.append({"identity":"two finite trigonometric sums", "status":"exact",
               "odd_n_tested":trig_checks,
               "general_proof":"PS57 finite geometric series covers every n>=5"})

incidence_checks=[]
for L in (2,3,4,5):
    m=2*L
    faces=Counter()
    for i in range(3):
        for j in range(i+1,3):
            for a in range(m+1):
                for b in range(m+1):
                    for c in range(m+1):
                        base=[a,b,c]
                        if base[i]>=m or base[j]>=m:
                            continue
                        shift_i=base.copy();shift_i[i]+=1
                        shift_j=base.copy();shift_j[j]+=1
                        for start,direction in ((base,i),(shift_i,j),(shift_j,i),(base,j)):
                            faces[tuple(start)+(direction+1,)]+=1
    selected_k=set()
    selected_b=set()
    for row in range(m):
        for height in range(m+1):
            k=(1,row,height,2);b=(m,row,height,2)
            selected_k.add(k);selected_b.add(b)
            assert faces[k] == (3 if height in (0,m) else 4)
            assert faces[b] == (2 if height in (0,m) else 3)
    assert len(selected_k)==m*(m+1)==len(selected_b)
    assert not selected_k.intersection(selected_b)
    incidence_checks.append({"L":L,"selected_k":len(selected_k),
                             "selected_b":len(selected_b),"disjoint":True})
checks.append({"identity":"original physical face incidences and disjoint selected derivatives",
               "status":"exact","boxes":incidence_checks,
               "general_proof":"PS40, PS47 and PS57–PS59"})

result={"status":"all_exact_assertions_passed","checks":checks,
        "limitations":"These bounded certificates accompany the general proofs; no numerical sample is substituted for a quantified mathematical argument."}
(ROOT/"SYMBOLIC_GEOMETRY_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
