from pathlib import Path
from fractions import Fraction as F
import random,json,hashlib
import mpmath as mp
R=Path(__file__).resolve().parent;mp.mp.dps=90
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def cross(a,b):return (a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0])
def mul(a,b):
 s,v=a[0],a[1:];t,w=b[0],b[1:];c=cross(v,w)
 return (s*t-dot(v,w),*(s*w[k]+t*v[k]+c[k] for k in range(3)))
def add(a,b):return tuple(x+y for x,y in zip(a,b))
zero=(F(0),)*4;one=(F(1),F(0),F(0),F(0))
def ep(x):
 n=dot(x,x)
 return [one,(F(0),*(z/2 for z in x)),(-n/8,F(0),F(0),F(0)),(F(0),*(-n*z/48 for z in x)),(n*n/384,F(0),F(0),F(0))]
def product(xs):
 p=[one]+[zero]*4
 for x in xs:
  a=ep(x);p=[tuple(sum(mul(p[k],a[d-k])[i] for k in range(d+1)) for i in range(4)) for d in range(5)]
 return p
rng=random.Random(20261011);checks=0
for trial in range(80):
 xs=[tuple(F(rng.randint(-3,3),rng.randint(1,5)) for k in range(3)) for a in range(4)]
 p=product(xs);total=tuple(sum(x[k] for x in xs) for k in range(3))
 cubic=sum(dot(xs[a],cross(xs[b],xs[c])) for a in range(4) for b in range(a+1,4) for c in range(b+1,4))/4
 assert -2*p[2][0]==dot(total,total)/4
 assert -2*p[3][0]==cubic
 rev=product([tuple(-z for z in x) for x in xs[::-1]])
 assert [x[0] for x in p]==[x[0] for x in rev]
 checks+=3
 B=tuple(sum(cross(xs[a],xs[b])[k] for a in range(4) for b in range(a+1,4)) for k in range(3))
 assert cubic==dot(total,B)/4;checks+=1
for trial in range(50):
 xs=[tuple(F(rng.randint(-3,3),rng.randint(1,5)) for k in range(3)) for a in range(3)]
 xs.append(tuple(-sum(x[k] for x in xs) for k in range(3)))
 p=product(xs);B=tuple(sum(cross(xs[a],xs[b])[k] for a in range(4) for b in range(a+1,4)) for k in range(3))
 assert p[2][0]==0 and p[3][0]==0
 assert -2*p[4][0]==dot(B,B)/16;checks+=2
def expq(x):
 n=mp.sqrt(dot(x,x));return (mp.cos(n/2),*(mp.sin(n/2)*z/n for z in x)) if n else (mp.mpf(1),mp.mpf(0),mp.mpf(0),mp.mpf(0))
for trial in range(100):
 xs=[tuple(mp.mpf(rng.randint(-20,20))/10 for k in range(3)) for a in range(4)]
 p=one
 for x in xs:p=mul(p,expq(x))
 defect=2-2*p[0];total=tuple(sum(x[k] for x in xs) for k in range(3));quad=dot(total,total)/4
 cubic=sum(dot(xs[a],cross(xs[b],xs[c])) for a in range(4) for b in range(a+1,4) for c in range(b+1,4))/4
 size=sum(mp.sqrt(dot(x,x)) for x in xs)
 assert abs(defect-quad-cubic)<=size**4/192+mp.mpf('1e-75')
 assert abs(defect-quad)<=size**3/24+mp.mpf('1e-75')
 checks+=2
for x in [F(1,7),F(2,3),F(4)]:
 # OW3's nonunitarity defect for diag(x,-x).
 real=1-x*x/2;imag=x;assert real*real+imag*imag==1+x**4/4
 assert ((1-real)**2+imag*imag)-2*(1-real)==x**4/4;checks+=2
 back=1+x**4/4;assert 2*(1-back)==-x**4/2 and (1-back)**2==x**8/16;checks+=1
samples=[]
for j in [2,8,32,128]:
 m=mp.mpf(2)*j**4;n=m+1;alpha=mp.pi/(2*m);b=10000*mp.mpf(j)**2
 W=4*m*m*n*(1-mp.cos(alpha));Q=2*m*m*n*alpha*alpha
 assert -m*m*n*alpha**4/6<=W-Q<=0
 assert abs(b*Q-5000*mp.pi**2*j**2*(2*j**4+1))<mp.mpf('1e-50')
 samples.append({'j':j,'j2_potential_remainder':mp.nstr(j*j*b*(W-Q),35),'target':mp.nstr(-625*mp.pi**4/12,35),'potential_over_j6':mp.nstr(b*W/j**6,35),'target_leading':mp.nstr(10000*mp.pi**2,35)})
 checks+=2
proof=R/'ORDERED_WILSON_ACTION.md';s=proof.read_text(encoding='utf-8');assert not [c for c in s if ord(c)<32 and c not in '\n\r\t']
v={'status':'passed','checks':checks,'exact_rational_coefficient_and_orientation_checks':240,'exact_cubic_and_quartic_cancellation_checks':180,'explicit_source_defect_checks':9,'numerical_global_remainder_checks':200,'original_path_checks':8,'precision_digits':90,'samples':samples,'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest()}
(R/'ORDERED_WILSON_CHECKS.json').write_text(json.dumps(v,indent=2)+'\n',encoding='utf-8');print(json.dumps({'status':'passed','checks':checks}))
