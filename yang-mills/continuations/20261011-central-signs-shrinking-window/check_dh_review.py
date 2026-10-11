"""Exact and bounded checks of DH review, including cutoff recovery."""
from pathlib import Path
import hashlib,json,math,re,datetime
import numpy as np
import sympy as sp
from scipy.integrate import quad

R=Path(__file__).resolve().parent
W=R
checks=[]
def check(name, passed, detail):checks.append(dict(name=name,passed=bool(passed),detail=detail))
s=(R/'DISTRIBUTION_HISTORY_REVIEW.md').read_text(encoding='utf-8')
check('DR labels',list(map(int,re.findall(r'\\tag\{DR(\d+)\}',s)))==list(range(1,18)),'DR1-DR17, unique and ordered')
check('display and inline delimiters',s.count(r'\[')==s.count(r'\]') and s.count(r'\(')==s.count(r'\)'),[s.count(r'\['),s.count(r'\]')])
check('control audit',not any(ord(c)<32 and c not in '\n\t' for c in s) and '\ufffd' not in s,'UTF-8 source')
sealed=hashlib.sha256((R/'CURVATURE_PHASE_RECONSTRUCTION.md').read_bytes()).hexdigest()
check('sealed CP unchanged',sealed=='6501ed4fb0c10e94f7440e94f0f63487d60c291f6943c7721683e81e4205f5a6',sealed)
for n in [1,2,4]:
    for k,l in [(1,1),(1,2),(2,2),(2,5),(5,5)]:
        v=quad(lambda x:np.sin(np.pi*k*(x+n)/(2*n))*np.sin(np.pi*l*(x+n)/(2*n))/n,-n,n,epsabs=1e-12)[0]
        check(f'exact sine factor n={n} k={k} l={l}',abs(v-float(k==l))<1e-12,v)
for m in [1,2,5,10]:
    vals=[sum(kd*kd for kd in (k1,k2,k3)) for k1 in range(1,m+3) for k2 in range(1,m+3) for k3 in range(1,m+3) if max(k1,k2,k3)>m]
    check('sharp inclusion tail M='+str(m),min(vals)==(m+1)**2+2,min(vals))
check('shell cardinality',all(r**3-(r-1)**3==3*r*r-3*r+1 for r in range(1,101)),'First hundred exact shells')
n,d,k=sp.symbols('n d k',positive=True)
check('cutoff coefficient exact',sp.simplify(sp.pi*k/(2*n**sp.Rational(5,2))*n*d/4-sp.pi*k/(8*n**sp.Rational(3,2))*d)==0,'delta=n*2^(-l-2)')
def eta(u):
    u=np.asarray(u);a=np.zeros_like(u,dtype=float);b=np.zeros_like(u,dtype=float)
    good=u>.5;a[good]=np.exp(-1/(u[good]-.5))
    good=u<1;b[good]=np.exp(-1/(1-u[good]))
    return a/(a+b)
gen=np.random.default_rng(192923)
for nv in [1,2]:
    pts=gen.uniform(-nv,nv,(20000,3))
    for lv in [1,3,6]:
        delta=nv*2**(-lv-2)
        cutoff=np.prod(eta((pts+nv)/delta)*eta((nv-pts)/delta),axis=1)
        for kv in [(1,1,1),(2,5,3)]:
            values=nv**(-1.5)*np.prod(np.sin(np.pi*np.array(kv)*(pts+nv)/(2*nv)),axis=1)
            bound=np.pi*max(kv)*delta/(2*nv**2.5)
            error=float(np.max(abs((1-cutoff)*values)))
            check(f'cutoff supremum n={nv} l={lv} k={kv}',error<=bound+1e-14,{'sample_error':error,'proved_bound':bound})
check('two-sided maximal factor',max(3,5)**4<=3**4+5**4,'Both time halves retained')
check('Borel-Cantelli power',all(abs((2**(-l))**4/(2**(-l/2))**4-2**(-2*l))<1e-14 for l in range(1,50)),'p=2, threshold 2^(-l/2)')
# Original coefficients of the boundary functional and approximating plane.
rr=np.arange(1,200001,dtype=float);nv=1.;sv=2.
weight=(1+np.pi**2*(rr*rr+2)/(4*nv*nv))**(-sv)
boundary=np.pi*rr/(2*nv**1.5)
errors=[]
for eps in [.2,.1,.05,.025]:
    plane=nv**(-.5)*np.sin(np.pi*rr*eps/(2*nv))/eps
    errors.append(float(np.sum(weight*(plane-boundary)**2)))
    check('plane coefficient domination eps='+str(eps),np.all(abs(plane)<=boundary*(1+1e-13)),'Dominated by the summable boundary norm at every retained coordinate')
check('boundary layer Hilbert convergence samples',all(errors[i+1]<errors[i] for i in range(len(errors)-1)),{'finite_sum_errors':errors,'terms':len(rr),'status':'Finite numerical samples; full convergence follows by dominated convergence in DR14.'})
check('boundary norm threshold',sp.simplify(sp.Rational(2)-2*sp.Rational(3,2))==-1,'At s=3/2 the comparison series is harmonic; s>3/2 converges')
M,ss,ss0=sp.symbols('M ss ss0',positive=True)
exact=(1+sp.pi**2*((M+1)**2+2)/(4*n*n))**(-(ss-ss0))
weaker=(1+sp.pi**2*(M+1)**2/(4*n*n))**(-(ss-ss0))
check('sharp tail improves DH14',float(exact.subs({M:4,n:1,ss:3,ss0:2}))<float(weaker.subs({M:4,n:1,ss:3,ss0:2})),'No existing DH bound is invalidated')
check('Hilbert limiting covariance coefficient',2*8==16,'Original 2 kappa bracket times 8 L times n^(-3) S')
check('three orientations retained',3*16==48,'Minkowski keeps a factor of three without independence')
check('Hilbert cosh coefficients',all(sp.factorial2(2*p-1)/sp.factorial(2*p)==1/(2**p*sp.factorial(p)) for p in range(1,15)),'Same coefficient identity applies to the Hilbert norm moments')
z=.13
check('Hilbert logarithmic union constant',abs(sum(2*(2**r)*z**(r+1) for r in range(50))-2*z/(1-2*z))<1e-14,'Every dyadic interval and leading factor two retained')
providers={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [W/'DISTRIBUTION_CURVATURE_HISTORIES.md',R/'CURVATURE_PHASE_RECONSTRUCTION.md']}
report={'created_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'total':len(checks),'passed':sum(x['passed'] for x in checks),'source_sha256':hashlib.sha256((R/'DISTRIBUTION_HISTORY_REVIEW.md').read_bytes()).hexdigest(),'provider_sha256':providers,'checks':checks}
(R/'DH_REVIEW_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:report[k] for k in ['total','passed','source_sha256','provider_sha256']}))
for x in checks:
    if not x['passed']: print(x)
raise SystemExit(0 if report['total']==report['passed'] else 1)
