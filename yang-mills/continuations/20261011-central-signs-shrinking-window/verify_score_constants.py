"""Exact algebra and bounded high-precision checks for LS1–LS57."""
from pathlib import Path
from fractions import Fraction
import json
import sympy as s
import mpmath as mp

ROOT=Path(__file__).resolve().parent
beta,tau,kappa,a,g,r,j,K,C=s.symbols("beta tau kappa a g r j K C",positive=True)
Cstar=2+2*s.sqrt(4+2*s.pi)
score_u=s.sqrt(4*s.pi*s.sqrt(beta)/tau+4*beta)+beta*tau/2
assert s.simplify(score_u.subs(tau,2/s.sqrt(beta))-
                  (1+s.sqrt(4+2*s.pi))*s.sqrt(beta))==0
assert s.simplify(2*score_u.subs(tau,2/s.sqrt(beta))-Cstar*s.sqrt(beta))==0
beta_actual=r/(4*g**4)
kappa_actual=2*g**2/a
assert s.simplify(2/(kappa_actual*s.sqrt(beta_actual))-2*a/s.sqrt(r))==0
assert s.simplify(s.pi/(2*kappa_actual*s.sqrt(beta_actual))-s.pi*a/(2*s.sqrt(r)))==0
assert s.simplify(4*beta*tau+s.pi**2/tau).subs(tau,s.pi/(2*s.sqrt(beta)))==4*s.pi*s.sqrt(beta)

# Original quaternion fields: physical radius two, with fundamental Casimir 3/4.
def left_matrix(w):
    c,x,y,z=w
    return s.Matrix([[c,-x,-y,-z],[x,c,-z,y],[y,z,c,-x],[z,-y,x,c]])
fields=[]
for alpha in range(3):
    w=[s.Integer(0)]*4
    w[alpha+1]=s.Rational(1,2)
    fields.append(left_matrix(w))
assert sum((M*M for M in fields),s.zeros(4))==-s.Rational(3,4)*s.eye(4)
v=s.Matrix(s.symbols("v1:4",real=True))
ad=s.Matrix([[0,-v[2],v[1]],[v[2],0,-v[0]],[-v[1],v[0],0]])
assert ad*v==s.zeros(3,1)
assert ad.T==-ad

# Derivative and endpoint signs of the complete Gaussian image summand.
b,T=s.symbols("b T",real=True,positive=True)
derivative=s.diff(b*s.exp(-b*b/T),b)
assert s.simplify(derivative-(1-2*b*b/T)*s.exp(-b*b/T))==0
assert s.simplify(-derivative.subs(b,s.pi)-
                  (2*s.pi**2/T-1)*s.exp(-s.pi**2/T))==0

# Original path and optimization factors.
xi=10000*j**2/K**2
new_score=s.simplify(C*s.sqrt(r*xi))
assert new_score==100*C*s.sqrt(r)*j/K
for power in (2,6,8):
    cap=(s.Integer(power)/(s.E*new_score))**power
    expected=(s.Integer(power)*K/(100*C*s.E*s.sqrt(r)))**power*j**(-power)
    assert s.simplify(cap-expected)==0
assert Fraction(5000)*Fraction(3,32)==Fraction(1875,4)
assert Fraction(5000,12)==Fraction(1250,3)

# The proof supplies all infinite-series bounds. This is a finite, high-precision
# comparison of its two exact kernel representations, not a substitute for it.
mp.mp.dps=100
def character_kernel(time,theta):
    if theta==0:
        return mp.fsum(n*n*mp.exp(-time*(n*n-1)/4) for n in range(1,121))
    if theta==mp.pi:
        return mp.fsum((-1)**(n-1)*n*n*mp.exp(-time*(n*n-1)/4) for n in range(1,121))
    return mp.fsum(n*mp.exp(-time*(n*n-1)/4)*mp.sin(n*theta)/mp.sin(theta)
                   for n in range(1,121))
def image_kernel(time,theta):
    pref=2*mp.sqrt(mp.pi)*mp.exp(time/4)/time**mp.mpf("1.5")
    if theta==0:
        summ=1+2*mp.fsum((1-8*mp.pi**2*k*k/time)*mp.exp(-4*mp.pi**2*k*k/time)
                         for k in range(1,21))
    elif theta==mp.pi:
        summ=2*mp.fsum((2*(2*k+1)**2*mp.pi**2/time-1)*
                       mp.exp(-(2*k+1)**2*mp.pi**2/time) for k in range(21))
    else:
        summ=mp.fsum((theta+2*mp.pi*k)*mp.exp(-(theta+2*mp.pi*k)**2/time)
                     for k in range(-20,21))/mp.sin(theta)
    return pref*summ

rows=[]
for time in [mp.mpf(1)/4,mp.mpf(1)/2,mp.mpf(1),mp.mpf(2),mp.pi**2/2,mp.pi**2]:
    errs=[]
    for theta in [mp.mpf(0),mp.pi/7,mp.pi/2,mp.pi]:
        spectral=character_kernel(time,theta)
        images=image_kernel(time,theta)
        assert spectral>0 and images>0
        err=abs(spectral-images)/images
        assert err<mp.mpf("1e-70")
        errs.append(err)
    ratio=image_kernel(time,0)/image_kernel(time,mp.pi)
    bound=mp.exp(mp.pi**2/time)/(2*(2*mp.pi**2/time-1))
    assert ratio<=bound*(1+mp.mpf("1e-80"))
    rows.append({"tau":mp.nstr(time,18),
                 "maximum_relative_representation_difference":mp.nstr(max(errs),8),
                 "endpoint_ratio":mp.nstr(ratio,18),
                 "proved_endpoint_ratio_upper_bound":mp.nstr(bound,18)})

result={"status":"all_checks_passed","exact_checks":[
    "Cstar from the full entropy and potential-gradient formula",
    "original physical times pi*a/(2*sqrt(r)) and 2*a/sqrt(r)",
    "original quaternion Casimir 3/4 and skew adjoint-rotation axis",
    "complete Gaussian image endpoint derivative signs",
    "unchanged path score and optimized cap powers",
    "exact rational mass/energy prefactors"],
    "Cstar_exact":"2+2*sqrt(4+2*pi)","Cstar_decimal":str(s.N(Cstar,25)),
    "kernel_check_precision_decimal_digits":100,"kernel_checks":rows,
    "path_powers":{"odd_raw_mass":-38,"even_raw_mass":-34,
                   "boundary_gradient":-22,"odd_and_even_energy_lower_bounds":-28,
                   "positive_endpoint_correction":-27},
    "scope":"Exact algebra plus bounded numerical comparison; infinite-series and stochastic arguments are proved in SQUARE_ROOT_LOCAL_SCORE.md."}
(ROOT/"SCORE_CHECKS.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps(result,indent=2))
