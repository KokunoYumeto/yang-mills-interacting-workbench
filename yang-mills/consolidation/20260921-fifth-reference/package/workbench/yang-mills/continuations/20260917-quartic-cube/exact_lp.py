from fractions import Fraction as F

def maximize(A,b,c):
    """Primal simplex with Bland rule, feasible origin; returns exact dual witness."""
    m=len(A);n=len(c)
    T=[[F(v) for v in r]+[F(i==j) for j in range(m)]+[F(b[i])] for i,r in enumerate(A)]
    if any(x[-1]<0 for x in T):raise ValueError('negative RHS')
    obj=[-F(x) for x in c]+[F(0)]*(m+1);basis=list(range(n,n+m));steps=0
    while any(x<0 for x in obj[:-1]):
        j=next(j for j,x in enumerate(obj[:-1]) if x<0)
        eligible=[i for i in range(m) if T[i][j]>0]
        if not eligible:raise ValueError('unbounded')
        i=min(eligible,key=lambda i:(T[i][-1]/T[i][j],basis[i]))
        div=T[i][j];T[i]=[x/div for x in T[i]]
        for k in range(m):
            if k==i:continue
            a=T[k][j]
            if a:T[k]=[x-a*y for x,y in zip(T[k],T[i])]
        a=obj[j];obj=[x-a*y for x,y in zip(obj,T[i])];basis[i]=j;steps+=1
        if steps>10000:raise RuntimeError('too many pivots')
    x=[F(0)]*n
    for i,j in enumerate(basis):
        if j<n:x[j]=T[i][-1]
    y=obj[n:n+m]
    if not(all(t>=0 for t in x+y) and all(sum(a*z for a,z in zip(r,x))<=v for r,v in zip(A,b)) and all(sum(y[i]*A[i][j] for i in range(m))>=c[j] for j in range(n))):raise ArithmeticError('dual failure')
    val=sum(a*z for a,z in zip(c,x))
    if val!=sum(a*z for a,z in zip(b,y)):raise ArithmeticError('objective mismatch')
    return val,x,y,steps


def solve_square(A,b):
    n=len(b);T=[[F(v) for v in r]+[F(x)] for r,x in zip(A,b)]
    for j in range(n):
        idx=next((i for i in range(j,n) if T[i][j]),None)
        if idx is None:return None
        T[idx],T[j]=T[j],T[idx]
        d=T[j][j];T[j]=[v/d for v in T[j]]
        for i in range(n):
            if i==j:continue
            d=T[i][j]
            if d:T[i]=[a-d*c for a,c in zip(T[i],T[j])]
    return tuple(r[-1] for r in T)
