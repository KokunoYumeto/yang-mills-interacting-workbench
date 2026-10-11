from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import json,hashlib,sqlite3,random
import mpmath as mp

ROOT=Path(__file__).resolve().parent
mp.mp.dps=90

def inv(word): return [(e,-sgn) for e,sgn in word[::-1]]
def reduce(word):
    out=[]
    for e,sgn in word:
        if out and out[-1]==(e,-sgn): out.pop()
        else: out.append((e,sgn))
    return out
def edge(i,k,l,d): return [((i,k,l,d),1)]
def t(i,k,l):
    return sum((edge(0,0,r,3) for r in range(l)),[])+sum((edge(0,b,l,2) for b in range(k)),[])+sum((edge(a,k,l,1) for a in range(i)),[])
def face(i,k,l,d,e):
    x=[i,k,l];xd=x.copy();xe=x.copy();xd[d-1]+=1;xe[e-1]+=1
    return edge(*x,d)+edge(*xd,e)+inv(edge(*xe,d))+inv(edge(*x,e))
def rooted_face(i,k,l,d,e): return t(i,k,l)+face(i,k,l,d,e)+inv(t(i,k,l))
def chord(i,k,l,d):
    target=[i,k,l];target[d-1]+=1
    return t(i,k,l)+edge(i,k,l,d)+inv(t(*target))
def factor(i,k,l,d):
    if d==2:
        return sum((rooted_face(a,k,l,1,2) for a in reversed(range(i))),[])
    return sum((rooted_face(a,k,l,1,3) for a in reversed(range(i))),[])+sum((rooted_face(0,b,l,2,3) for b in reversed(range(k))),[])
def reflect(word,m):
    out=[]
    for (i,k,l,d),sgn in word:
        if d==1: out.append(((m-i-1,k,l,d),-sgn))
        else: out.append(((m-i,k,l,d),sgn))
    return out

counts={'rooted_factorizations':0,'reflected_factorizations':0,'orientation_reflection_formulas':0,'reversed_factorizations':0}
for m in [4,6]:
    for i in range(m+1):
      for k in range(m+1):
       for l in range(m+1):
        for d in [2,3]:
          if [i,k,l][d-1]==m: continue
          original=chord(i,k,l,d);filled=factor(i,k,l,d)
          assert reduce(original)==reduce(filled),(m,i,k,l,d)
          counts['rooted_factorizations']+=1
          assert reduce(reflect(original,m))==reduce(reflect(filled,m))
          counts['reflected_factorizations']+=1
          assert reduce(inv(original))==reduce(inv(filled))
          counts['reversed_factorizations']+=1
        for d,e in [(1,2),(1,3),(2,3)]:
          if [i,k,l][d-1]==m or [i,k,l][e-1]==m: continue
          reflected=reflect(face(i,k,l,d,e),m)
          if d==1:
            y=m-i-1
            claimed=inv(edge(y,k,l,1))+inv(face(y,k,l,d,e))+edge(y,k,l,1)
          else: claimed=face(m-i,k,l,d,e)
          assert reduce(reflected)==reduce(claimed)
          counts['orientation_reflection_formulas']+=1

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def neg(a):return tuple(-x for x in a)
def sub(a,b):return add(a,neg(b))
def mul(a,b):
    aa,bb,cc,dd=a;ee,ff,gg,hh=b
    return (aa*ee-bb*ff-cc*gg-dd*hh,aa*ff+bb*ee+cc*hh-dd*gg,aa*gg+cc*ee+dd*ff-bb*hh,aa*hh+dd*ee+bb*gg-cc*ff)
def qi(a):return (a[0],-a[1],-a[2],-a[3])
def qv(a):return tuple(2*x for x in a[1:])
I=(F(1),F(0),F(0),F(0))
rng=random.Random(20261011)
def rational_unit():
    r=[F(rng.randint(-4,4),rng.randint(1,5)) for _ in range(3)]
    ss=sum(x*x for x in r)
    return ((1-ss)/(1+ss),*(2*x/(1+ss) for x in r))
for trial in range(36):
    A,B,C,D=[rational_unit() for _ in range(4)]
    P=mul(mul(mul(A,B),qi(C)),qi(D))
    lhs=qv(add(sub(C,A),sub(D,B)))
    rhs=qv(add(neg(mul(sub(P,I),mul(D,C))),sub(mul(sub(A,I),sub(B,I)),mul(sub(D,I),sub(C,I)))))
    assert lhs==rhs
counts['exact_rational_nonlinear_curl_identities']=36

def vecsum(vectors):
    out=[mp.mpf(0)]*3
    for v in vectors:out=[a+b for a,b in zip(out,v)]
    return out
def scale(c,v):return [c*x for x in v]
def norm2(v):return sum(x*x for x in v)

coefficient_checks=[]
for m in [4,6,8,20]:
    n=m+1;h=mp.pi/(2*n);s=mp.sin(h);c=mp.cos(h);C=mp.cot(h)
    v=[mp.sqrt(mp.mpf(2)/n)*mp.cos(mp.pi*(r+mp.mpf('.5'))/n) for r in range(n)]
    w=[-mp.sqrt(mp.mpf(2)/n)*mp.sin(mp.pi*(r+1)/n) for r in range(m)]
    we=lambda r:w[r] if 0<=r<m else mp.mpf(0)
    assert abs(sum(v))<mp.mpf('1e-85')
    assert abs(sum(x*x for x in w)-1)<mp.mpf('1e-85')
    for a in range(m): assert abs(sum(v[a+1:])-w[a]/(2*s))<mp.mpf('1e-85')
    H2=sum((m-a)**2 for a in range(m))*sum(x*x for x in w)*sum((abs(we(r))+abs(we(r-1)))**2 for r in range(n))/(8*s*s*n)
    Hclaimed=mp.mpf(m)*(2*m+1)*c*c/(12*s*s)
    assert abs(H2/Hclaimed-1)<mp.mpf('1e-85')
    A=2*mp.sqrt(mp.mpf(2)/n)*sum(mp.cos(mp.pi*(r+mp.mpf('.5'))/n)*mp.sin(mp.pi*r/(2*m)) for r in range(n))
    alpha=mp.pi/(2*m);bb=mp.pi/n
    Aclosed=mp.cos(n*alpha/2)/mp.sqrt(n)*(mp.csc((alpha+bb)/2)+mp.csc((alpha-bb)/2))
    assert abs(A/Aclosed-1)<mp.mpf('1e-85')
    coefficient_checks.append({'m':m,'signed_tail_squared_weight_sum':mp.nstr(1/(8*s*s),25),'nonlinear_weight_H':mp.nstr(H2,25),'A_m':mp.nstr(A,25),'smooth_configuration_W':mp.nstr(4*m*m*n*(1-mp.cos(alpha)),25)})

# Original rows in a noncommuting tree-gauge configuration; no omitted corner.
m=4;n=m+1;h=mp.pi/(2*n);s=mp.sin(h)
v=[mp.sqrt(mp.mpf(2)/n)*mp.cos(mp.pi*(r+mp.mpf('.5'))/n) for r in range(n)]
w=[-mp.sqrt(mp.mpf(2)/n)*mp.sin(mp.pi*(r+1)/n) for r in range(m)]
u2={};u3={}
for i in range(n):
 for k in range(n):
  for l in range(n):
   if k<m:u2[i,k,l]=I if i==0 else rational_unit()
   if l<m:u3[i,k,l]=I if i==0 and k==0 else rational_unit()
mpq=lambda a:[mp.mpf(x.numerator)/x.denominator for x in qv(a)]
original1=vecsum(scale(-v[i]*w[k]/mp.sqrt(2*n),mpq(u2[i,k,l])) for i in range(1,n) for k in range(m) for l in range(n))
summed1=vecsum(scale(-w[a]*w[k]/(2*s*mp.sqrt(2*n)),[x-y for x,y in zip(mpq(u2[a+1,k,l]),mpq(u2[a,k,l]))]) for a in range(m) for k in range(m) for l in range(n))
assert mp.sqrt(norm2([x-y for x,y in zip(original1,summed1)]))<mp.mpf('1e-80')
original3=vecsum([*list(scale(w[k]*v[l]/mp.sqrt(2*n),mpq(u2[i,k,l])) for i in range(1,n) for k in range(m) for l in range(n)),*list(scale(-v[k]*w[l]/mp.sqrt(2*n),mpq(u3[i,k,l])) for i in range(n) for k in range(n) for l in range(m) if (i,k)!=(0,0))])
summed3=vecsum(scale(w[k]*w[l]/(2*s*mp.sqrt(2*n)),[aa-bb-cc+dd for aa,bb,cc,dd in zip(mpq(u2[i,k,l+1]),mpq(u2[i,k,l]),mpq(u3[i,k+1,l]),mpq(u3[i,k,l]))]) for i in range(n) for k in range(m) for l in range(m))
assert mp.sqrt(norm2([x-y for x,y in zip(original3,summed3)]))<mp.mpf('1e-80')
W12=sum(F(2)-2*mul(u2[i+1,k,l],qi(u2[i,k,l]))[0] for i in range(m) for k in range(m) for l in range(n))
W12mp=mp.mpf(W12.numerator)/W12.denominator
assert norm2(original1)<=W12mp/(2*s*s)
counts['noncommuting_original_row_identity_checks']=3

asymptotic=[]
for j in [2,4,8,16,64,256]:
    m=2*j**4;n=m+1;h=mp.pi/(2*n);s=mp.sin(h);c=mp.cos(h);C=mp.cot(h);g2=mp.mpf(1)/(200*j)
    S1=mp.sqrt(mp.mpf(2)/n)*C*(C-c);S3=mp.sqrt(mp.mpf(2)/n)*((2-mp.mpf(1)/n)*C*C-c*C/n)
    N=3*m*n*n;M=3*m*m*n;Budget=min(2*M,6*g2*mp.sqrt(N*M))
    point=16*S1*S1*S3*S3;linear=2*S3*S3*Budget/(3*s*s)
    alpha=mp.pi/(2*m);bb=mp.pi/n
    A=mp.cos(n*alpha/2)/mp.sqrt(n)*(mp.csc((alpha+bb)/2)+mp.csc((alpha-bb)/2))
    SS=A*A*C*C
    exampleW=4*m*m*n*(1-mp.cos(alpha))
    assert exampleW<=Budget
    asymptotic.append({'j':j,'kappa_star':1,'linear_over_j7_point':mp.nstr(linear/(j**7*point),25),'target_3pi2_over1600':mp.nstr(3*mp.pi**2/1600,25),'example_S_squared_over_point':mp.nstr(SS*SS/point,25),'target_1_over324':mp.nstr(mp.mpf(1)/324,25),'example_W_over_mean_budget':mp.nstr(exampleW/Budget,25)})

out={'generated_utc':datetime.now(timezone.utc).isoformat(),'status':'passed','counts':counts,'precision_digits':mp.mp.dps,'coefficient_checks':coefficient_checks,'original_row_test':'Noncommuting rational link matrices on complete m=4 tree-gauge box; original finite rows and signed telescoping forms compared at 90 digits.','asymptotic_samples':asymptotic,'scope':'Free-group and rational checks are exact; trigonometric and limiting samples supplement CW1–CW48.'}
(ROOT/'CURVATURE_WORD_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')

proof=(ROOT/'CURVATURE_ROOTED_WORDS.md').read_text(encoding='utf-8')
assert not [c for c in proof if ord(c)<32 and c not in '\r\n\t']
print(json.dumps({'status':'passed','counts':counts},indent=2))
