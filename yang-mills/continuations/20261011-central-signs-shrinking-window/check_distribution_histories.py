from pathlib import Path
import datetime, hashlib, json, math, re
import numpy as np
from scipy.integrate import quad

root=Path(__file__).resolve().parent
checks=[]
def check(name, condition, detail=None):
    checks.append(dict(name=name,passed=bool(condition),detail=detail))
    assert condition, name

for n in (1,2,5):
    for k in (1,2,5):
        for l in (1,2,5):
            value=quad(lambda x:math.sin(math.pi*k*(x+n)/(2*n))*math.sin(math.pi*l*(x+n)/(2*n))/n,-n,n,epsabs=1e-11)[0]
            check(f'sine orthogonality n{n} k{k} l{l}',abs(value-(k==l))<1e-10,value)
for r in range(1,32):
    count=r**3-(r-1)**3
    check(f'exact shell {r}',count==3*r*r-3*r+1,count)
for s in (1.6,2.0,2.7):
    for n in (1,3):
        for M in (1,3,10,30):
            # Every omitted shell has at least one coordinate > M.
            rr=np.arange(M+1,200001,dtype=float)
            partial=np.sum((3*rr**2-3*rr+1)*(1+math.pi**2*rr**2/(4*n*n))**(-s))
            bound=(4*n*n/math.pi**2)**s*3*M**(3-2*s)/(2*s-3)
            check(f'shell majorant tail n{n} s{s} M{M}',partial<bound,dict(partial=partial,bound=bound))
for kap in (.1,1.,7.):
    for n in (1,2,5):
        a2=1/200; R=2*n
        B=9*kap*(R+4*a2)**1.5*(R+5*a2)**1.5+24*(R+4*a2)*(R+5*a2)
        for j in (2,3,9,31):
            a=1/(100*j); g2=kap*a/2; q=math.ceil(R/a)+3
            N=3*q*(q+1)**2; M=3*q*q*(q+1); C=12*q*(q+1)
            lam=min(2*M,6*g2*math.sqrt(N*M))+2*C
            check(f'complete patch constant k{kap} n{n} j{j}',a*a*lam<=B*(1+1e-13),dict(actual=a*a*lam,bound=B))
for p in (2,3,7,20):
    gamma=(p-1)/(4*p)
    check(f'dyadic Holder exponent p{p}',p-1-2*p*gamma>0)
    r=2**(-(p-1)/(2*p))
    check(f'maximal sum p{p}',abs(sum(r**i for i in range(10000))-1/(1-r))<1e-10)
rng=np.random.default_rng(4412)
ks=np.array([(a,b,c) for a in range(1,8) for b in range(1,8) for c in range(1,8)])
lam=math.pi**2*np.sum(ks**2,axis=1)/4
for s0,s in ((1.6,2.0),(2.0,3.0),(3.0,4.1)):
    y=rng.normal(size=len(ks))+1j*rng.normal(size=len(ks))
    norm0=np.sum((1+lam)**(-s0)*abs(y)**2)
    for M in (1,2,4):
        tail=np.sum((1+lam[np.max(ks,axis=1)>M])**(-s)*abs(y[np.max(ks,axis=1)>M])**2)
        bound=norm0*(1+math.pi**2*(M+1)**2/4)**(-(s-s0))
        check(f'compact inclusion tail s0{s0} s{s} M{M}',tail<=bound,dict(tail=tail,bound=bound))
source=root/'DISTRIBUTION_CURVATURE_HISTORIES.md'
text=source.read_text(encoding='utf-8')
for a,b in ((r'\[',r'\]'),(r'\(',r'\)')):
    check(f'complete delimiters {a}',text.count(a)==text.count(b))
tags=re.findall(r'\\tag\{(DH\d+[a-z]?)\}',text)
check('unique equation locators',len(tags)==len(set(tags)))
check('boundary kernel retained','\\mathcal N_{n,s}' in text and 'No boundary trace' in text)
result=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),proof_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),scope='Exact shell counts, orthogonality, full original patch constants, quantitative tails and source structure. Numerical checks do not replace the proof.',count=len(checks),all_passed=True,checks=checks)
(root/'DISTRIBUTION_HISTORY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'}))
