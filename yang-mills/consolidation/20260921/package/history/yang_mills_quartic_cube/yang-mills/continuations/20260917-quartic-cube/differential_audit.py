"""Independent directional differentiation of original matrix products.
No Fierz contraction or symbolic electric-operator routine is called here.
Triples carry actual value, first derivative, second derivative at zero.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import product, permutations

def qm(q,r):
 a,b,c,d=q;e,f,g,h=r
 return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def qc(q):return(q[0],-q[1],-q[2],-q[3])
def qs(q,c):return tuple(c*x for x in q)
def qa(*qs_):return tuple(sum(q[i] for q in qs_) for i in range(4))
ONE=(F(1),F(0),F(0),F(0));ZERO=(F(0),)*4

POINTS=tuple(sorted({tuple(F(s*x,5) for s,x in zip(signs,coords))
    for coords in permutations((1,2,2,4)) for signs in product((-1,1),repeat=4)}))
def assignments(n,seed):
    # Exact unit quaternions with one common denominator; no floating operations.
    return {i:POINTS[(37*i+53*seed+7*i*i)%len(POINTS)] for i in range(1,n+1)}

def product_jet(a,b):
    x,dx,ddx=a;y,dy,ddy=b
    return (x*y,dx*y+x*dy,ddx*y+2*dx*dy+x*ddy)

class Audit:
    def __init__(self,U):self.U=U
    @lru_cache(None)
    def word(self,w):
        q=ONE
        for x in w:q=qm(q,self.U[x] if x>0 else qc(self.U[-x]))
        return q
    @lru_cache(None)
    def trace(self,w,e,a):
        v=2*self.word(w)[0]
        cs=[((i if x>0 else (i+1)%len(w)),1 if x>0 else -1)
            for i,x in enumerate(w) if abs(x)==e]
        if not cs:return v,F(0),F(0)
        gen=tuple(F(int(k==a+1),2) for k in range(4))
        dv=sum(s*2*qm(gen,self.word(w[i:]+w[:i]))[0] for i,s in cs)
        ddv=-F(len(cs),4)*v
        for k,(i,ss) in enumerate(cs):
            for j,tt in cs[k+1:]:
                lo,hi=sorted((i,j))
                u=self.word(w[lo:hi]);vv=self.word(w[hi:]+w[:lo])
                ddv+=4*ss*tt*qm(qm(qm(gen,u),gen),vv)[0]
        return v,dv,ddv
    @lru_cache(None)
    def mono(self,m,e,a):
        v=(F(1),F(0),F(0))
        for w in m:v=product_jet(v,self.trace(w,e,a))
        return v
    def jet(self,p,e,a):
        out=[F(0)]*3
        for m,c in p.items():
            v=self.mono(m,e,a)
            for i in range(3):out[i]+=c*v[i]
        return tuple(out)
    def value(self,p):return self.jet(p,0,0)[0]
    def K(self,p):return -sum(self.jet(p,e,a)[2] for e in self.U for a in range(3))
    def Gamma(self,p,q):return sum(self.jet(p,e,a)[1]*self.jet(q,e,a)[1] for e in self.U for a in range(3))
