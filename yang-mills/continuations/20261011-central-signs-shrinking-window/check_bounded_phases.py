"""Exact phase algebra and spectral-inequality diagnostics; no vacuum sampling."""
from pathlib import Path
import hashlib, json, math
import numpy as np
import sympy as sp

ROOT = Path(__file__).resolve().parent
checks = []
def record(name, passed, **data):
    checks.append(dict(name=name, passed=bool(passed), **data))

r, s, D, gamma, k = sp.symbols('r s D gamma k', real=True)
product = (-sp.I*r*D-r*r*gamma)*(sp.I*s*D-s*s*gamma)
expected = r*s*D**2+r*r*s*s*gamma**2+sp.I*r*s*(s-r)*D*gamma
record('BP11 complete mixed second moment', sp.expand(product-expected)==0)
record('BP10 exact diagonal second moment', sp.expand(expected.subs(s,r)-r*r*D**2-r**4*gamma**2)==0)
l, p, Q = sp.symbols('l p Q', positive=True)
R = 2*(Q+p/l)
q = l*l/(p+Q*l)
record('BP14 polynomial receiver exact lower value', sp.simplify(4*l/R-4*(p+Q*l)/R**2-q)==0)
record('BP20 exact first-energy band lower value', sp.simplify(l-l/4-(p+Q*l)/R-l/4)==0)

rng=np.random.default_rng(20261011)
margin=math.inf
for trial in range(768):
    lam=np.exp(rng.uniform(-9,9,24))
    mass=rng.dirichlet(np.ones(24))*rng.uniform(.01,1)
    G=float(mass.sum()); E=float(mass@lam); E2=float(mass@(lam*lam))
    lv=E*rng.uniform(.01,1)
    Qv=rng.uniform(0,1)*E2/E
    pv=max(0,E2-Qv*E)+rng.uniform(0,1)*E2
    Rv=2*(Qv+pv/lv); qv=lv*lv/(pv+Qv*lv)
    spectral=float(mass[lam<=Rv].sum())
    band=float((mass*lam)[(lam>=lv/4)&(lam<=Rv)].sum())
    t=float(np.exp(rng.uniform(-10,4)))
    heat=float(mass@(-np.expm1(-t*lam)))
    lower=qv*(-math.expm1(-t*Rv/2))
    jensen=E*E/E2*(-math.expm1(-t*E2/E))
    scale=max(1,E,E2,Rv)
    record('positive-measure diagnostic %03d'%trial,
           G+1e-12>=qv and spectral+1e-12>=qv and
           band+1e-11*scale>=lv/4 and heat+1e-12>=lower and
           heat+1e-12>=jensen and heat<=min(G,t*E)+1e-12,
           measure='Synthetic positive finite spectral measure, not an interacting vacuum')
    margin=min(margin,heat-lower)

# Exact translated face quadrature for f(x)=product(1-|x_d|)_+,
# o=0, support [-1,1]^3, R=2, kappa_*=1.  Each orientation has
# two half-step coordinates and one integer coordinate.  The finite sums
# below retain those separate coordinates before taking products.
def tent_sum(n,half,power):
    # These are the exact finite sums, evaluated by rational power sums.
    if power==1:
        return sp.Integer(n)
    if half:
        return sp.Rational(2*n,3)-sp.Rational(1,6*n)
    return sp.Rational(2*n,3)+sp.Rational(1,3*n)

for n in [2,3,10,100]:
    for half in [False,True]:
        for power in [1,2]:
            actual=sum(max(0,1-abs(sp.Rational(2*z+int(half),2*n)))**power
                       for z in range(-n-1,n+1))
            record('tent quadrature n=%s half=%s power=%s'%(n,half,power),
                   actual==tent_sum(n,half,power))

LR=168.0; dp=(LR+math.sqrt(LR*LR-1296.0))/2
ef=81/dp; H=56/3; Rf=256*LR*dp
limits=[]
for j in [10,100,1000,10000,100000]:
    a=1/(100*j); n=100*j; patch=2*n+3
    N=3*patch*(patch+1)**2; M=3*patch**2*(patch+1)
    C=12*patch*(patch+1)
    Lambda=min(2*M,3*a*math.sqrt(N*M))+2*C
    xi=1/(a*a); AQ=9+64*xi; BQ=36*M+64*xi*Lambda
    disc=BQ*BQ-144*AQ*M*M
    dminus=72*M*M/(BQ+math.sqrt(disc)); dplus=(BQ+math.sqrt(disc))/(2*AQ)
    A1=3*n**3
    A2=3*(2*n/3-1/(6*n))**2*(2*n/3+1/(3*n))
    # Lipschitz constant sqrt(3) bounds the actual global modulus.
    omega=math.sqrt(3)*a/2
    bj=a*max(0,6*A1-3*dplus-12*M*omega)
    El=bj*bj/(4*xi*(Lambda-dminus)); Eu=16*a*a*dplus
    P=21*a*a*A2; QE=.5+4/a; Rj=256*a**4*(Lambda*dplus+4*a*a)
    record('original-path finite receiver j=%s'%j,
           0<dminus<=dplus<=Lambda and dminus<Lambda and 0<El<=Eu,
           a=a, local_lower_energy=El, local_upper_energy=Eu)
    for ell in [.01,1,100]:
        theta2=ell/a; lv=theta2*El; pv=theta2*P+theta2**2*Rj
        qv=lv*lv/(pv+QE*lv); Z=(H+4*ef)/ell+Rf
        target=ef*ef/Z
        limits.append(dict(j=j,ell=ell,finite=qv,limit=target,ratio=qv/target))
        if j==100000: record('BP24 original-path limit ell=%s'%ell,abs(qv/target-1)<.0001)
record('unit-norm consistency of asymptotic bound', 0<ef*ef/Rf<1)
proof=ROOT/'BOUNDED_PHASE_SPECTRAL_RECEIVING.md'
text=proof.read_text(encoding='utf-8')
record('all BP locators present',all(('\\tag{BP%d}'%i) in text for i in range(1,34)))
output=dict(all_passed=all(c['passed'] for c in checks),checks=checks,
            count=len(checks),minimum_synthetic_heat_margin=margin,
            proof_sha256=hashlib.sha256(proof.read_bytes()).hexdigest(),
            original_path_values=limits,constants=dict(LR=LR,dplus=dp,e_f=ef,H_f=H,R_f=Rf),
            scope='Exact symbolic identities and independent finite positive-measure diagnostics. Original-path numbers evaluate proved bound functions only; no interacting vacuum was sampled.')
(ROOT/'BOUNDED_PHASE_CHECKS.json').write_text(json.dumps(output,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(all_passed=output['all_passed'],count=len(checks),failed=[c for c in checks if not c['passed']])))
assert output['all_passed']
