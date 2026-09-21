"""Finite partial fractions in the original resolvent variable z, over Q.
A record (a,n):q represents q/(z+a)^n. The (0,0) record is a scalar.
"""
from fractions import Fraction as F
from math import comb, factorial
from functools import lru_cache
class PF:
    __slots__=('d',)
    def __init__(self,x=0):
        if isinstance(x,PF): self.d=x.d.copy()
        elif isinstance(x,dict): self.d={(F(a),int(n)):F(c) for (a,n),c in x.items() if c}
        else: self.d={(F(0),0):F(x)} if x else {}
    def __bool__(self):return bool(self.d)
    def __add__(self,o):
        if not isinstance(o,PF):o=PF(o)
        d=self.d.copy()
        for k,v in o.d.items():
            d[k]=d.get(k,F(0))+v
            if not d[k]: del d[k]
        return PF(d)
    __radd__=__add__
    def __neg__(self):return PF({k:-c for k,c in self.d.items()})
    def __sub__(self,o):return self+-PF(o)
    def __rsub__(self,o):return PF(o)+-self
    def __mul__(self,o):
        if not isinstance(o,PF):o=PF(o)
        d={}
        for (a,m),c in self.d.items():
            for (b,n),e in o.d.items():
                for k,w in product_poles(a,m,b,n):
                    d[k]=d.get(k,F(0))+c*e*w
        return PF(d)
    __rmul__=__mul__
    def __truediv__(self,q):return self*F(1,F(q))
    def __eq__(self,o):return self.d==PF(o).d
    def __repr__(self):return 'PF('+repr(self.d)+')'
    def value(self,z):
        z=F(z);return sum(c/(z+a)**n for (a,n),c in self.d.items())
    def at_zero(self):
        if any(a==0 and n>0 for a,n in self.d):raise ValueError('uncancelled zero-energy pole')
        return self.value(0)
    def heat_terms(self):
        if (F(0),0) in self.d:raise ValueError('distributional polynomial term')
        return [(a,n-1,c/F(factorial(n-1))) for (a,n),c in sorted(self.d.items())]
    def to_json(self):
        return [{'energy':str(a),'power':n,'coefficient':str(c)} for (a,n),c in sorted(self.d.items())]
    @classmethod
    def from_json(cls,rows):return cls({(F(r['energy']),r['power']):F(r['coefficient']) for r in rows})
@lru_cache(None)
def product_poles(a,m,b,n):
    if m==0:return (((b,n),F(1)),)
    if n==0:return (((a,m),F(1)),)
    if a==b:return (((a,m+n),F(1)),)
    out=[]
    for k in range(m):out.append(((a,m-k),F((-1)**k*comb(n+k-1,k))/(b-a)**(n+k)))
    for k in range(n):out.append(((b,n-k),F((-1)**k*comb(m+k-1,k))/(a-b)**(m+k)))
    return tuple(out)
def pole(a,n=1):return PF({(F(a),n):F(1)})
