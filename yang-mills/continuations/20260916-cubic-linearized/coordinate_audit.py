"""Exact original-link test of the cubic source; no vacuum sampling."""
from fractions import Fraction as F
from itertools import product,combinations
from functools import lru_cache
from geometry import pword,pedges,adjacent,incident,anchored,type3,cycle,boundary,union

ZERO=(F(0),)*4
ONE=(F(1),F(0),F(0),F(0))
AXES=tuple(tuple(F(int(a==b)) for a in range(4)) for b in range(4))
CELL=tuple(tuple(s*x for x in a) for a in AXES for s in (-1,1))+tuple(tuple(F(s,2) for s in ss) for ss in product((-1,1),repeat=4))
POOL=CELL+((F(3,5),F(4,5),F(0),F(0)),(F(0),F(3,5),F(0),F(4,5)))

def mul(q,r):
 a,b,c,d=q;e,f,g,h=r
 return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def conj(q):return(q[0],-q[1],-q[2],-q[3])
def neg(q):return tuple(-x for x in q)
def gen(a):return tuple(F(int(i==a+1),2) for i in range(4))
def wordval(word,U):
 q=ONE
 for e,s in word:q=mul(q,U[e] if s==1 else conj(U[e]))
 return 2*q[0]
def loop(p,U):return wordval(pword(p),U)
def dloop(p,U,e,a):
 word=pword(p)
 if e not in pedges(p):return F(0)
 q=ONE
 for f,s in word:
  t=U[f] if s==1 else conj(U[f])
  if f==e:t=mul(gen(a),U[e]) if s==1 else neg(mul(conj(U[e]),gen(a)))
  q=mul(q,t)
 return 2*q[0]
def pzero_pair(p,q,U,der=None):
 common=pedges(p)&pedges(q)
 if len(common)!=1:raise ValueError('pair must have one original shared edge')
 edge=next(iter(common))
 if der and der[0]==edge:return F(0)
 V=dict(U);out=F(0)
 for u in AXES:
  V[edge]=u
  if der:
   e,a=der;out+=dloop(p,V,e,a)*loop(q,V)+loop(p,V)*dloop(q,V,e,a)
  else:out+=loop(p,V)*loop(q,V)
 return out/4

def inner2(p,q,U,der=None):
 if p==q:
  w=loop(p,U)
  return -F(1,72)*(2*w*dloop(p,U,*der) if der else w*w-1)
 if not pedges(p)&pedges(q):return F(0)
 z=pzero_pair(p,q,U,der)
 f=(dloop(p,U,*der)*loop(q,U)+loop(p,U)*dloop(q,U,*der)) if der else loop(p,U)*loop(q,U)
 return F(1,27)*z-F(1,117)*(f-z)

def source_rhs(ps,U):
 # Each distinct outer-plaquette choice occurs once in 2 B(v1,v2).
 total=F(0)
 for p in sorted(set(ps)):
  rest=list(ps);rest.remove(p);q,r=rest
  for e in pedges(p)&(pedges(q)|pedges(r)):
   for a in range(3):total+=F(2,3)*dloop(p,U,e,a)*inner2(q,r,U,(e,a))
 return total

def projected3(ps,U):
 typ=type3(ps);edges=sorted(union(ps));ans=[]
 if typ=='self':
  w=loop(ps[0],U)
  return[(F(3),-F(1,81),w),(F(15),F(1,810),w**3-2*w)]
 if typ=='repeat':
  p=next(p for p in set(ps) if ps.count(p)==2);q=next(q for q in set(ps) if q!=p)
  z=pzero_pair(p,q,U);w=loop(p,U);v=loop(q,U)
  h=F(4,3)*w*z-F(1,3)*v;f=(w*w-1)*v
  return[(F(9),-F(11,4212),h),(F(12),F(11,11232),f-h)]
 if typ=='disconnected':return[]
 if typ=='common':
  f=F(1)
  for p in ps:f*=loop(p,U)
  h=sum(loop(ps[i],U)*pzero_pair(ps[(i+1)%3],ps[(i+2)%3],U) for i in range(3))*F(2,3)
  return[(F(15,2),-F(2,1755),h),(F(21,2),F(2,2457),f-h)]
 shared=sorted(e for e in edges if sum(e in pedges(p) for p in ps)==2)
 @lru_cache(None)
 def integ(sub):
  V=dict(U);total=F(0)
  for vals in product(AXES,repeat=len(sub)):
   V.update(zip(sub,vals));f=F(1)
   for p in ps:f*=loop(p,V)
   total+=f
  return total/(4**len(sub))
 for bits in product((0,1),repeat=len(shared)):
  zs=tuple(shared[i] for i,b in enumerate(bits) if not b)
  os=tuple(shared[i] for i,b in enumerate(bits) if b)
  val=F(0)
  for extra in product((0,1),repeat=len(os)):
   sub=tuple(sorted(zs+tuple(e for e,t in zip(os,extra) if t)))
   val+=(-1)**sum(extra)*integ(sub)
  n=sum(bits)
  if typ=='path':
   c=F(6+2*n);coef={0:F(1,162),1:-F(11,8424),2:F(1,3510)}[n]
  else:
   c=F(9,2)+2*n
   coef={0:F(2,81),1:F(34,13689),2:-F(38,17901),3:F(2,2457)}[n]
   if n==1 and val!=0:raise ArithmeticError('one-spin corner failed')
  ans.append((c,coef,val))
 return ans

def assignment(ps,seed):
 U={}
 for j,e in enumerate(sorted(union(ps))):
  U[e]=POOL[(17*j+7*seed+sum((k+3)*n for k,n in enumerate(e)))%len(POOL)]
 return U

def half_projection(fun,U,e):
 V=dict(U);r=F(0);q=U[e]
 for u in CELL:
  V[e]=u;r+=sum(q[i]*u[i] for i in range(4))*fun(V)
 return r/6 # 4/24

def run_coordinate_tests():
 anchor,pairs,triples=anchored();rows=[]
 pp=incident(anchor)
 motifs=[(pp[0],)*3]+[(p,p,q) for p,q in pairs[:3]]
 for typ in ('path','common','corner'):
  xs=triples[typ]
  motifs += [xs[j] for j in (0,len(xs)//3,2*len(xs)//3,len(xs)-1)]
 for idx,ps in enumerate(motifs):
  for seed in range(3):
   U=assignment(ps,seed);rhs=source_rhs(ps,U)
   kv=sum(c*a*v for c,a,v in projected3(ps,U))
   if kv!=rhs:raise ArithmeticError((type3(ps),idx,seed,ps,kv,rhs,kv-rhs))
   rows.append({'type':type3(ps),'seed':seed,'K_v3':str(kv)})
 # Independent harmonic projections verify the recoupling step.
 for p,q in pairs[::10]:
  ps=(p,p,q);U=assignment(ps,5);e=next(iter(pedges(p)&pedges(q)))
  fun=lambda V:(loop(p,V)**2-1)*loop(q,V)
  explicit=F(4,3)*loop(p,U)*pzero_pair(p,q,U)-F(1,3)*loop(q,U)
  got=half_projection(fun,U,e)
  if got!=explicit:raise ArithmeticError('repeated harmonic projection')
  rows.append({'type':'repeat-harmonic','value':str(got)})
 for ps in triples['common'][::10]:
  U=assignment(ps,6);e=next(iter(set.intersection(*(set(pedges(p)) for p in ps))))
  fun=lambda V:loop(ps[0],V)*loop(ps[1],V)*loop(ps[2],V)
  h=projected3(ps,U)[0][2]
  if half_projection(fun,U,e)!=h:raise ArithmeticError('common-edge harmonic projection')
  rows.append({'type':'common-harmonic','value':str(h)})
 return rows
if __name__=='__main__':
 import json,time
 t=time.monotonic();rows=run_coordinate_tests();print(json.dumps({'passed':len(rows),'elapsed':time.monotonic()-t,'rows':rows},indent=2))
