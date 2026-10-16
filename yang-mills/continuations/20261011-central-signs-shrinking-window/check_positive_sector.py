from pathlib import Path
from fractions import Fraction as F
import itertools, json, math, time
import sympy as sp
import mpmath as mp

O=Path(__file__).resolve().parent
start=time.time(); checks=[]
def ck(name,yes):
    checks.append(dict(name=name,passed=bool(yes)))
    assert yes,name

# Exact original radius-two fields on seven quaternion factors. The two
# oriented faces below share a link with opposite traversal signs.
dim=28; z=(0,)*dim
def add(a,b):
    c=a.copy()
    for p,v in b.items():c[p]=c.get(p,F(0))+v
    return {p:v for p,v in c.items() if v}
def scale(a,v):return {p:x*v for p,x in a.items() if x*v}
def mul(a,b):
    c={}
    for p,v in a.items():
        for q,w in b.items():
            r=tuple(x+y for x,y in zip(p,q));c[r]=c.get(r,F(0))+v*w
    return {p:v for p,v in c.items() if v}
def diff(a,i):
    c={}
    for p,v in a.items():
        if p[i]:
            q=list(p);q[i]-=1;c[tuple(q)]=v*p[i]
    return c
def sm(xs):
    a={}
    for x in xs:a=add(a,x)
    return a
coords=[]
for i in range(dim):
    p=list(z);p[i]=1;coords.append({tuple(p):F(1)})
one={z:F(1)}
def eps(i,j,k):
    return 0 if len({i,j,k})<3 else (1 if (i,j,k) in [(0,1,2),(1,2,0),(2,0,1)] else -1)
def X(i,p):
    edge,col=divmod(i,3);off=4*edge
    a=add(scale(mul(coords[off+col+1],diff(p,off)),-1),
          mul(coords[off],diff(p,off+col+1)))
    for j,k in itertools.product(range(3),repeat=2):
        if eps(col,j,k):a=add(a,scale(mul(coords[off+j+1],diff(p,off+k+1)),eps(col,j,k)))
    return scale(a,F(1,2))
def word(p,J):
    for i in reversed(J):p=X(i,p)
    return p
def qm(a,b):
    return [add(mul(a[0],b[0]),scale(sm(mul(a[i],b[i]) for i in [1,2,3]),-1))]+[
      sm([mul(a[0],b[k+1]),mul(a[k+1],b[0])]+[
        scale(mul(a[i+1],b[j+1]),eps(i,j,k))
        for i,j in itertools.product(range(3),repeat=2) if eps(i,j,k)])
      for k in range(3)]
def face(edges):
    q=[one,{},{},{}]
    for e,sgn in edges:
        u=coords[4*e:4*e+4]
        if sgn<0:u=[u[0]]+[scale(x,-1) for x in u[1:]]
        q=qm(q,u)
    return scale(q[0],2)
faces=[[(0,1),(1,1),(2,-1),(3,-1)],
       [(0,-1),(4,1),(5,1),(6,-1)]]
T=[face(x) for x in faces]
grad=[{e:[X(3*e+a,t) for a in range(3)] for e,sgn in faces[n]} for n,t in enumerate(T)]
for n,t in enumerate(T):
    ck('complete four-link face Casimir '+str(n),
       add(sm(X(3*e+a,X(3*e+a,t)) for e,sgn in faces[n] for a in range(3)),scale(t,3))=={})
points=[
 [F(3,5),F(4,5),F(0),F(0)],
 [F(5,13),F(0),F(12,13),F(0)],
 [F(0),F(0),F(0),F(1)],
 [F(1,2),F(1,2),F(1,2),F(1,2)],
]
def val(p,point):return sum(v*math.prod(x**n for x,n in zip(point,q)) for q,v in p.items())
for shift in [0,1,2]:
    point=sum([points[(e+shift)%4] for e in range(7)],[])
    tv=[val(t,point) for t in T]
    gv=[{e:[val(x,point) for x in vs] for e,vs in g.items()} for g in grad]
    for p in range(2):
        for e in gv[p]:
            ck(f'original oriented edge trace norm {shift} {p} {e}',sum(x*x for x in gv[p][e])==1-tv[p]**2/4)
    lhs=F(32); rem=4*sum(t*t for t in tv)
    for e in range(7):
        vv=[g[e] for g in gv if e in g]
        lhs-=sum(sum(v[a] for v in vv)**2 for a in range(3))
        rem+=(4-len(vv))*sum(sum(x*x for x in v) for v in vv)
        rem+=sum(sum((v[a]-u[a])**2 for a in range(3)) for v,u in itertools.combinations(vv,2))
    ck('full crossing incidence with opposite shared traversal '+str(shift),lhs==rem and rem>=0)

# Ordered receiver PSE15 with B=-3/5 Delta_out+2 acting on link1.
# Both ground and trial have nonzero ordered commutators.
psi=add(one,scale(mul(coords[0],coords[4]),F(1,7)))
t=add(coords[1],mul(coords[2],coords[3]))
def Bpol(p):return add(scale(sm(X(i,X(i,p)) for i in range(3,6)),F(-3,5)),scale(p,2))
for J in [(0,),(1,),(0,1),(1,0),(0,1,2),(2,1,0),(0,0,1,2)]:
    rhs=word(Bpol(mul(psi,t)),J)
    for mask in range(1,1<<len(J)):
        I=tuple(J[k] for k in range(len(J)) if mask&(1<<k))
        C=tuple(J[k] for k in range(len(J)) if not mask&(1<<k))
        rhs=add(rhs,scale(mul(Bpol(word(psi,I)),word(t,C)),-1))
    ck('entire ordered sector receiver '+str(J),rhs==Bpol(mul(psi,word(t,J))))

# Independent positive finite tensor: exact ground, noncommuting K and D,
# complex/dependent raw source columns. This is not the Wilson state.
A=sp.kronecker_product(sp.Matrix([[1,-1],[-1,1]]),sp.eye(2))
B=sp.kronecker_product(sp.eye(2),sp.Matrix([[1,-1],[-1,1]]))
D=A+B; V=sp.diag(1,2,2,0); epsilon=sp.Integer(1)
K=D+V-sp.eye(4); S=sp.eye(4)-V
pv=sp.Matrix([1,1,1,2])/sp.sqrt(7)
ck('positive tensor ground',K*pv==sp.zeros(4,1) and all(x>=0 for x in K.eigenvals()))
ck('tensor noncommutation retained',K*D!=D*K and A*B==B*A)
F0=sp.Matrix([1+2*sp.I,1+2*sp.I,3-sp.I,3-sp.I])
F1=sp.Matrix([2,2,-1+3*sp.I,-1+3*sp.I])
F2=2*F0-sp.I*F1
U=sp.diag(*pv)*sp.Matrix.hstack(F0,F1,F2)
adj=lambda u:u.conjugate().T
zero=lambda m:all(sp.expand(x)==0 for x in m)
G00=adj(K*U)*D*(K*U)
G11=adj(S*U)*D*(S*U)
G01=adj(K*U)*D*(S*U)
ck('full cubic Gram including both mixed matrices',zero(adj(U)*D**3*U-G00-G01-adj(G01)-G11))
ck('first cubic positive remainder',zero(G00-(adj(U)*K**3*U+epsilon*adj(K*U)*(K*U)-adj(K*U)*V*(K*U))))
rem=V*(epsilon**2*sp.eye(4)+epsilon*S+S**2)
ck('second cubic positive polynomial remainder',zero(G11-(adj(S*U)*K*(S*U)+epsilon**3*adj(U)*U-adj(U)*rem*U)))
for m in [1,2,3]:
    full=sum((sp.binomial(m,r)*A**r*B**(m-r) for r in range(m+1)),sp.zeros(4))
    ck('entire joint sector polynomial '+str(m),D**m==full)
    ck('sector complement positive '+str(m),all(x>=0 for x in (D**m-B**m).eigenvals()))
    rho=[sp.Rational(2,7),sp.Rational(5,7)]
    beta=[sum(pv[k]*(B**m*pv)[k] for k in pair)/rho[n] for n,pair in enumerate([(0,1),(2,3)])]
    raw=sp.Matrix([[F0[0],F1[0],F2[0]],[F0[2],F1[2],F2[2]]])
    ck('actual conditional weighted sector matrix '+str(m),zero(adj(U)*B**m*U-adj(raw)*sp.diag(*[rho[n]*beta[n] for n in range(2)])*raw))
ck('dependent source retained',sp.expand((adj(U)*U).det())==0)

mp.mp.dps=80
def constants(j,k,theta):
    j,k,theta=map(mp.mpf,(j,k,theta))
    a=1/(100*j); b=1/(k*a*a); C=12*(100*j)*(100*j+1)
    mx=2*b*C; P=4*b*mp.sqrt(C); zz=theta*k/j
    e1=21*zz/4; e2=21*zz*zz/4; e3=zz**3
    s0=1/e3;s1=1/(2*mp.sqrt(k*e2*e3));sL=1/(2*mp.sqrt(e1*e3));s32=1/(2*mp.sqrt(e3))
    E1=mp.sqrt(k*s1*s1+mx*s0*s0);E2=sL+2*mx*s0
    E3=mp.sqrt(s32*s32+mx*sL*sL)+mp.sqrt(k*(2*mx*s1+P*s0)**2+mx**3*s0*s0)
    return mx,(E1,E2,E3)
evaluations=[]
for k,th in [('0.8','1'),('1.3','0.6')]:
    mm=mp.mpf(2400000000)/mp.mpf(k)
    lead=[mp.sqrt(mm),2*mm,mm**mp.mpf('1.5')]
    lead=[v/(mp.mpf(th)**3*mp.mpf(k)**3) for v in lead]
    for j in [4,16,10**8,10**32]:
        mx,es=constants(j,k,th)
        ck(f'full original crossing count {j} {k}',mp.almosteq(mx,mm*j**4+mp.mpf(24000000)/mp.mpf(k)*j**3))
        vals=[es[n]/mp.mpf(j)**[5,7,9][n]/lead[n] for n in range(3)]
        if j==10**32:
            for n,r in enumerate(vals):ck(f'independent leading sector coefficient {k} {n}',abs(r-1)<mp.mpf('1e-29'))
        evaluations.append(dict(j=j,kappa=k,theta=th,full_E=[str(e) for e in es],ratio_to_leading=[str(v) for v in vals]))
def rise(x,n):
    a=F(1)
    for k in range(n):a*=x+k
    return a
def integral(p):
    out=F(0)
    for powers,value in p.items():
        if any(n%2 for n in powers):continue
        factor=F(1)
        for off in range(0,dim,4):
            ns=[n//2 for n in powers[off:off+4]]
            factor*=math.prod(rise(F(1,2),n) for n in ns)/rise(F(2),sum(ns))
        out+=value*factor
    return out
kap=F(3,5)
for n,f in enumerate([t,add(coords[2],mul(coords[1],coords[3])),mul(coords[0],coords[1])]):
    df=[X(i,f) for i in range(3)]
    lap=sm(X(i,X(i,f)) for i in range(3))
    cc=sm(mul(X(i,psi),df[i]) for i in range(3))
    ln=scale(add(mul(psi,lap),scale(cc,2)),-kap)
    lhs=integral(mul(mul(psi,psi),sm(mul(X(h,df[i]),X(h,df[i])) for h,i in itertools.product(range(3),repeat=2))))
    mixed=sum(integral(mul(mul(psi,X(h,psi)),mul(df[i],X(h,df[i])))) for h,i in itertools.product(range(3),repeat=2))
    rhs=integral(mul(ln,ln))/kap**2+2*integral(mul(cc,ln))/kap-2*mixed
    ck('exact full weighted second-derivative identity '+str(n),lhs==rhs)
    # Here psi>=6/7 and |d_in psi|<=1/14, so |d log psi|<=1/12.
    alpha=F(1,12)
    d1=mp.sqrt(str(integral(mul(mul(psi,psi),sm(mul(x,x) for x in df)))))
    ell=mp.sqrt(str(integral(mul(ln,ln))))/mp.mpf(str(kap))
    ck('second-derivative bound on actual constructed density '+str(n),
       mp.sqrt(str(lhs))<=ell+2*mp.mpf(str(alpha))*d1+mp.mpf('1e-70'))
from evaluate_positive_receiver import constants as receiver_constants
for k,th in [('0.8','1'),('1.3','0.6')]:
    kk=mp.mpf(k);tt=mp.mpf(th)
    aa=mp.mpf(960000)/kk**2;gg=mp.mpf(3840000)*mp.pi**2/kk**2
    u1=mp.sqrt(gg);gam=mp.sqrt(2*mp.pi*(2*aa+gg))
    dd=1/(mp.sqrt(21)*tt**mp.mpf('2.5')*kk**3)
    l02=4*u1*(2*aa+gg)*dd;v30=2*aa*dd;l11=2*aa*dd
    rr=12*aa*l02+8*aa*gam*v30
    ss=kk**3*(6*(aa+3*gg)*l02+12*u1*(4*aa+3*gg)*l11)
    for j in [4,16,10**8]:
        x=receiver_constants(j,k,th)
        ck(f'new complete second derivative degree {k} {j}',x['tr'][2,0].degree==5)
        ck(f'all six received residual degrees {k} {j}',
           [v.degree for v in x['rows'].values()]==[F(33),F(75,2),F(75,2),F(39,2),F(18),F(17,2)])
        ck(f'independent entire direct leading coefficient {k} {j}',mp.almosteq(x['direct'].leading,kk**5*rr**2/tt))
        ck(f'independent entire pair leading coefficient {k} {j}',mp.almosteq(x['pair'].leading,ss**2/(tt*kk)))
        ck(f'previous full bounds retained {k} {j}',x['best'].value<=x['prior']['best'].value)
result=dict(checks=len(checks),all_passed=True,seconds=time.time()-start,
 scope='Exact original oriented SU2 Casimirs, rational edge norms and shared-edge incidence; full ordered sector product formula; independent positive tensor cubic matrices and conditional moments with complex dependent sources; complete weighted second-derivative identity; full finite sector constants and both received residual leading coefficients. No original Wilson spectral moment is evaluated.',
 items=checks,evaluations=evaluations)
(O/'POSITIVE_SECTOR_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['items','evaluations']}))
