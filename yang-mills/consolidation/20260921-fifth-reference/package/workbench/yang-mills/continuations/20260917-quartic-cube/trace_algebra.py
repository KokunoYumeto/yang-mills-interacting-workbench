"""Rational SU(2) trace algebra in original oriented edge words.
Representatives use proved cyclic, inverse-word, and inverse-pair identities.
All arithmetic retains every scalar. A separate cluster label is never changed.
"""
from fractions import Fraction as F
from functools import lru_cache
from collections import defaultdict, Counter
from itertools import product

@lru_cache(None)
def cyclic(word):
    # U U^-1 cancellation followed by tr rotation / tr(W^-1)=tr(W).
    stack=[]
    for x in word:
        if stack and stack[-1]==-x:stack.pop()
        else:stack.append(x)
    while len(stack)>1 and stack[0]==-stack[-1]:stack=stack[1:-1]
    if not stack:return ()
    w=tuple(stack);v=tuple(-x for x in w[::-1])
    return min(w[i:]+w[:i] for w in (w,v) for i in range(len(w)))

@lru_cache(None)
def chebtrace(n):
    if n==0:return (2,)
    if n==1:return (0,1)
    a=list(chebtrace(n-1)); b=chebtrace(n-2)
    z=[0]+a
    for i,c in enumerate(b):z[i]-=c
    return tuple(z)
@lru_cache(None)
def monomial(words):
    terms={():1}
    for word in words:
        w=cyclic(word)
        if not w:terms={m:2*c for m,c in terms.items()};continue
        k=1;u=w
        for d in range(1,len(w)):
            if len(w)%d==0 and w[:d]*(len(w)//d)==w:
                u=cyclic(w[:d]);k=len(w)//d;break
        out=defaultdict(int)
        for m,c in terms.items():
            for j,b in enumerate(chebtrace(k)):
                if b:out[tuple(sorted(m+(u,)*j))]+=c*b
        terms={m:c for m,c in out.items() if c}
    return tuple(terms.items())

def addterm(out,words,c):
    if not c:return
    for w,k in monomial(tuple(words)):
        out[w]+=k*c
        if not out[w]:del out[w]

def clean(out):return dict(out)
def const(c):return {():F(c)} if c else {}
def trace(w):
    out=defaultdict(F);addterm(out,(tuple(w),),F(1));return dict(out)
def scale(p,c):return {m:v*c for m,v in p.items() if v*c}
def add(*ps):
    out=defaultdict(F)
    for p in ps:
        for m,c in p.items():out[m]+=c
    return {m:c for m,c in out.items() if c}
def multiply(p,q):
    out=defaultdict(F)
    for m,c in p.items():
        for n,d in q.items():addterm(out,m+n,c*d)
    return dict(out)

@lru_cache(None)
def cuts(w,e):
    # X_e tr(w)=sum s tr(T word_rot), cuts are original occurrences.
    return tuple(((i if x>0 else (i+1)%len(w)),1 if x>0 else -1)
                 for i,x in enumerate(w) if abs(x)==e)
@lru_cache(None)
def gamma_loops(a,b,e):
    out=defaultdict(F)
    for i,s in cuts(a,e):
        ar=a[i:]+a[:i]
        for j,t in cuts(b,e):
            br=b[j:]+b[:j]
            addterm(out,(ar+br,),-F(s*t,2))
            addterm(out,(a,b),F(s*t,4))
    return tuple(out.items())
@lru_cache(None)
def Eloop(w,e):
    out=defaultdict(F);cs=cuts(w,e)
    addterm(out,(w,),F(3*len(cs),4))
    for z,(i,s) in enumerate(cs):
        for j,t in cs[z+1:]:
            if i<=j:a,b=w[i:j],w[j:]+w[:i]
            else:a,b=w[j:i],w[i:]+w[:j]
            addterm(out,(a,b),F(s*t))
            addterm(out,(w,),-F(s*t,2))
    return tuple(out.items())
@lru_cache(None)
def Emon(m,e):
    out=defaultdict(F)
    for i,w in enumerate(m):
        other=m[:i]+m[i+1:]
        for t,c in Eloop(w,e):addterm(out,other+t,c)
        for j in range(i):
            other2=tuple(m[k] for k in range(len(m)) if k not in (i,j))
            for t,c in gamma_loops(w,m[j],e):addterm(out,other2+t,-2*c)
    return tuple(out.items())
def electric(p,e=None):
    out=defaultdict(F)
    for m,c in p.items():
        es={abs(x) for w in m for x in w} if e is None else (e,)
        for f in es:
            for t,d in Emon(m,f):addterm(out,t,c*d)
    return dict(out)
def gamma(p,q):
    out=defaultdict(F)
    for m,c in p.items():
        for n,d in q.items():
            for i,a in enumerate(m):
                for j,b in enumerate(n):
                    oth=m[:i]+m[i+1:]+n[:j]+n[j+1:]
                    for e in set(map(abs,a))&set(map(abs,b)):
                        for z,t in gamma_loops(a,b,e):addterm(out,oth+z,c*d*t)
    return dict(out)

def eigenvalues(words):
    occ=Counter(abs(x) for w in words for x in w)
    spectrum={F(0)}
    for e,k in occ.items():
        js=range(k%2,k+1,2)
        spectrum={a+F(j*(j+2),4) for a in spectrum for j in js}
    return sorted(spectrum)
@lru_cache(None)
def inverse_coeffs(spectrum):
    # Interpolation f(0)=0, f(c)=1/c on all original allowed eigenvalues.
    nonzero=[F(c) for c in spectrum if c]
    # q(x)=prod(1-x/c); (1-q(x))/x equals 1/c at nonzero eigenvalues.
    # subtract q(x)*sum(1/c) to set f(0)=0.
    p=[F(1)]
    for c in nonzero:
        a=[F(0)]*(len(p)+1)
        for i,v in enumerate(p):a[i]+=v;a[i+1]-=v/c
        p=a
    k=sum(1/c for c in nonzero)
    inv=[-p[i+1] if i+1<len(p) else F(0) for i in range(len(p))]
    inv=[a-k*b for a,b in zip(inv,p)]
    return tuple(inv)
def apply_poly(p,coeff):
    ans={}
    for c in reversed(coeff):ans=add(electric(ans),scale(p,c))
    return ans
def inverse(p,spectrum):return apply_poly(p,inverse_coeffs(tuple(spectrum)))

def qmul(q,r):
 a,b,c,d=q;e,f,g,h=r
 return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def qconj(q):return(q[0],-q[1],-q[2],-q[3])
def value(p,U):
 out=F(0)
 for m,c in p.items():
    v=c
    for w in m:
      q=(F(1),F(0),F(0),F(0))
      for x in w:q=qmul(q,U[abs(x)] if x>0 else qconj(U[-x]))
      v*=2*q[0]
    out+=v
 return out

def physical_spectrum(words,edges):
    # edges map positive coordinate labels -> (source vertex,target vertex)
    occ=Counter(abs(x) for w in words for x in w)
    es=sorted(occ);verts={v for e in es for v in edges[e]}
    vedges={v:[i for i,e in enumerate(es) if v in edges[e]] for v in verts}
    accepted=[]
    for js in product(*(range(occ[e]%2,occ[e]+1,2) for e in es)):
      if any(sum(js[i] for i in idx)%2 or 2*max(js[i] for i in idx)>sum(js[i] for i in idx) for idx in vedges.values()):continue
      accepted.append(js)
    return sorted({sum(F(j*(j+2),4) for j in js) for js in accepted}),accepted

def set_identity(p,e):
    out=defaultdict(F)
    for m,c in p.items():addterm(out,tuple(tuple(x for x in w if abs(x)!=e) for w in m),c)
    return dict(out)

def haar(p):
    """Exact original-edge integration through Casimir polynomial projections."""
    current=p
    while any(m for m in current):
        es={abs(x) for m in current for w in m for x in w}
        # eliminate the least-occurring link, with original trace powers retained
        e=min(es,key=lambda e:max(sum(abs(x)==e for w in m for x in w) for m in current))
        groups=defaultdict(dict)
        for m,c in current.items():
            k=sum(abs(x)==e for w in m for x in w)
            if k%2==0:groups[k][m]=c
        projected={}
        for k,poly in groups.items():
            v=poly
            for j in range(1,k//2+1):v=add(v,scale(electric(v,e),-F(1,j*(j+1))))
            projected=add(projected,set_identity(v,e))
        current=projected
    return current.get((),F(0))
