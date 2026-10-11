from pathlib import Path
import json,math
import sympy as s
import mpmath as mp
W=Path(__file__).resolve().parent
t=s.symbols('t',real=True)
checks=[]
def record(name,ok):
 assert bool(ok),name
 checks.append(name)
def mult(r,l2):
 if (r-l2)%2 or l2>r:return 0
 k=(r-l2)//2
 return s.binomial(r,k)-(s.binomial(r,k-1) if k else 0)
def corr(r,q):
 return sum(mult(r,l)*mult(q,l)*s.exp(-l*(l+2)*t) for l in range(min(r,q)+1))
# Independent exact calibration: four independent radius-two SU(2) Haar heat links.
# This is a calibration model, not the interacting vacuum.
mp.mp.dps=80
for p in range(1,6):
 moment=s.expand(sum((-1)**k*s.binomial(2*p,k)*corr(2*p-k,k) for k in range(2*p+1)))
 for k in range(p):record(f'Haar four-link increment 2p={2*p}: Taylor order {k}',s.simplify(s.diff(moment,t,k).subs(t,0))==0)
 rawgradient=sum((-1)**k*s.binomial(p,k)*4**(p-k)*s.catalan(k) for k in range(p+1))
 target=s.factorial2(2*p-1)*2**p*rawgradient
 record(f'Haar exact leading moment 2p={2*p}',s.simplify(s.diff(moment,t,p).subs(t,0)/s.factorial(p)-target)==0)
 bound=s.factorial2(2*p-1)*8**p
 record(f'Gradient moment bound 2p={2*p}',0<target<=bound)
 f=s.lambdify(t,moment,'mpmath')
 for h in [mp.mpf('0.0001'),mp.mpf('0.01'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('4')]:
  record(f'Exact heat increment inequality p={p},h={h}',-mp.mpf('1e-60')<=f(h)<=int(bound)*h**p+mp.mpf('1e-60'))
record('Fourth moment exact full heat expression',s.simplify(sum((-1)**k*s.binomial(4,k)*corr(4-k,k) for k in range(5))-(10-16*s.exp(-3*t)+6*s.exp(-8*t)))==0)
# Independent full open-box enumeration of the original orientation incidences.
for m in [2,4,6,8]:
 n=m+1;inc={}
 for i in range(m):
  for k in range(m):
   for l in range(n):
    for edge in [(i,k,l,1),(i,k+1,l,1),(i,k,l,2),(i+1,k,l,2)]:inc[edge]=inc.get(edge,0)+1
 record(f'Full orientation sum squares m={m}',sum(v*v for v in inc.values())==4*m*n*(2*m-1))
 record(f'Full orientation degree sum m={m}',sum(inc.values())==4*m*m*n)
for p in range(2,9):
 alpha=s.Rational(p-1,4*p)
 d=p-1-2*p*alpha
 record(f'Dyadic summability exponent p={p}',d>0)
 q=mp.power(2,-mp.mpf(str(alpha.p))/int(alpha.q))
 ca=2/q/(1-q);exact=(1/q)*(1+2*q/(1-q))
 record(f'Complete two-chain coefficient p={p}',ca>=exact)
r={'count':len(checks),'passed':len(checks),'checks':checks,'scope':'Exact independent Haar heat calibration and full open-box incidence enumeration; not evaluation of interacting vacuum moments.'}
(W/'WILSON_TIME_CHECKS.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'scope':r['scope']}))
