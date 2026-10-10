from pathlib import Path
from fractions import Fraction as F
from datetime import datetime, timezone
import json
ROOT=Path(__file__).resolve().parent
now=datetime.now(timezone.utc).isoformat()
m=[F(0),F(64,3),F(5834,39),F(336572872,208845),F(17270702970768271,341697152160),F(1638684)]
t=[F(0),F(16,3),F(137,6),F(225985217,1253070),F(110695177857394584026401,18025447358750832000),F(190128)]
a=[m[i]+4*t[i] for i in range(6)]
def ell(x):return sum(a[i]*x**i for i in range(1,6))
def tail(x):
    e=a[2]*x**2+a[4]*x**4
    o=a[1]*x+a[3]*x**3+a[5]*x**5
    return (e-e*e+o*o)/((1-e)**2-o*o)-(a[2]+a[1]**2)*x*x
assert a[1]==F(128,3)
assert a[2]==F(3132,13)
assert a[3]==F(292337810,125307)
assert a[4]==F(169232115504453213210913,2253180919843854000)
assert a[5]==2399196
beta_lo,beta_hi=F(19,1000),F(21,1000)
assert ell(beta_lo)<1<ell(beta_hi)
for _ in range(100):
    mid=(beta_lo+beta_hi)/2
    if ell(mid)<1:beta_lo=mid
    else:beta_hi=mid
vals=[]
for x in [F(1,100),F(3,256),F(1,64),F(19,1000)]:
    vals.append({'x':str(x),'ell_exact':str(ell(x)),'ell_decimal':float(ell(x)),
                 'inverse_bound_exact':str(1/(1-ell(x))),'inverse_bound_decimal':float(1/(1-ell(x))),
                 'even_tail_exact':str(tail(x)),'even_tail_decimal':float(tail(x))})
assert ell(F(19,1000))<F(93,100)
assert 1/(1-ell(F(19,1000)))<F(100,7)
assert tail(F(1,100))<F(66,1000)
assert tail(F(1,64))<F(3,4)

# A bounded check of the exact sign formula. The proof handles every L.
counts=[]
for L in [2,3,4]:
    def phase(n,i):return sum(n[:i])%2
    faces=0
    for n0 in range(-L,L+1):
      for n1 in range(-L,L+1):
       for n2 in range(-L,L+1):
        n=(n0,n1,n2)
        for i in range(3):
         for j in range(i+1,3):
          if n[i]==L or n[j]==L:continue
          ni=list(n);ni[i]+=1
          nj=list(n);nj[j]+=1
          assert (phase(n,i)+phase(ni,j)+phase(nj,i)+phase(n,j))%2==1
          faces+=1
    assert faces==12*L*L*(2*L+1)
    counts.append({'L':L,'faces_checked':faces})

# Exact reference coefficient checks from J1--J6.
assert F(1,9)*F(1,8)-F(1,39)*F(13,24)==0
assert -F(1,12)*F(8,9)==-F(2,27)
assert -F(1,72)*F(8,3)==-F(1,27)
assert F(1,27)*F(9,2)/3*F(1,4)-F(1,117)*F(13,2)/3*F(3,4)==0
assert F(2,27)+F(1,27)==F(1,9)
result={'verified_utc':now,'a_i':[str(z) for z in a[1:]],'h2':str(a[2]+a[1]**2),
        'beta_lower':str(beta_lo),'beta_upper':str(beta_hi),'beta_decimal':float((beta_lo+beta_hi)/2),
        'interval_bounds':vals,'face_sign_checks':counts,
        'certificates':['ell(19/1000)<93/100','inverse(19/1000)<100/7','tail(1/100)<66/1000','tail(1/64)<3/4','J4=-2P/27','J5=-P/27','Schur second=+P/9'],
        'analytic_proof_status':'Written proof, not certified by finite checks.'}
(ROOT/'EXACT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'beta_decimal':result['beta_decimal'],'interval_bounds':[{k:v for k,v in z.items() if not k.endswith('_exact')} for z in vals],'certificates':result['certificates']},indent=2))
