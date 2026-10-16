"""Exact arithmetic diagnostics for JMO1--JMO12; proofs are in the note."""
from pathlib import Path
from fractions import Fraction as F
import json
import sympy as s

checks = []
def ck(name, condition):
    if not condition:
        raise AssertionError(name)
    checks.append(name)

def add(x,y): return tuple(a+b for a,b in zip(x,y))
def neg(x): return tuple(-a for a in x)
def sub(x,y): return add(x,neg(y))
def scale(c,x): return tuple(c*a for a in x)
def qc(x): return (x[0],-x[1],-x[2],-x[3])
def qm(x,y):
    a,b,c,d=x; e,f,g,h=y
    return (a*e-b*f-c*g-d*h,a*f+b*e+c*h-d*g,
            a*g-b*h+c*e+d*f,a*h+b*g-c*f+d*e)
def oc(x): return qc(x[:4])+neg(x[4:])
def om(x,y):
    a,b=x[:4],x[4:];c,d=y[:4],y[4:]
    return sub(qm(a,c),qm(qc(d),b))+add(qm(d,a),qm(b,qc(c)))
def norm(x): return sum(a*a for a in x)
zero=(0,)*8
basis=[tuple(int(i==j) for i in range(8)) for j in range(8)]
def matzero(): return [[zero for _ in range(3)] for _ in range(3)]
def ma(x,y): return [[add(x[i][j],y[i][j]) for j in range(3)] for i in range(3)]
def ms(c,x): return [[scale(c,x[i][j]) for j in range(3)] for i in range(3)]
def mm(x,y):
    z=matzero()
    for i in range(3):
        for j in range(3):
            for k in range(3): z[i][j]=add(z[i][j],om(x[i][k],y[k][j]))
    return z
def jordan(x,y): return ms(F(1,2),ma(mm(x,y),mm(y,x)))
def E(i,a):
    z=matzero();j,k=[(1,2),(2,0),(0,1)][i]
    z[j][k]=a;z[k][j]=oc(a)
    return z
def diag(v):
    z=matzero()
    for i in range(3):z[i][i]=scale(v[i],basis[0])
    return z
def J(w):
    r,q,p=w
    return ma(ma(E(0,r),E(1,oc(q))),E(2,p))
def P(w):
    r,q,p=w
    return om(oc(p),q),om(p,r),om(q,oc(r))
def B(u,x):return qm(qm(u,x[:4]),qc(u))+x[4:]
def D(u,x):return qm(x[:4],qc(u))+qm(x[4:],qc(u))
def action(u,w):return B(u,w[0]),D(u,w[1]),D(u,w[2])
def invariant(w):return om(om(w[0],oc(w[1])),w[2])[0]
def muq(a,e):return qm(qm(a,e),qc(a))
def M(w):
    q,p=w[1],w[2]
    return (muq(qc(q[:4]),(0,1,0,0)),
            muq(qc(q[4:]),(0,0,1,0)),
            muq(qc(p[:4]),(0,0,0,1)))
for i,j,k in [(0,1,2),(1,2,0),(2,0,1)]:
    for a in basis:
        for b in basis:
            ck(f"Peirce {i} {a.index(1)} {b.index(1)}",
               jordan(E(i,a),E(j,b))==ms(F(1,2),E(k,oc(om(a,b)))))
    for a in basis:
        lam=(F(2),F(5),F(-7));v=diag(lam);ej=diag([int(n==j) for n in range(3)])
        deriv=ms(4,ma(jordan(E(i,a),jordan(ej,v)),
                      ms(-1,jordan(ej,jordan(E(i,a),v)))))
        ck(f"spectral differential {i} {a.index(1)}",deriv==ms(lam[j]-lam[k],E(i,a)))
u=tuple(F(n,5) for n in (1,2,2,4))
ck("original rational subgroup parameter",norm(u)==1)
for i in range(3):
    for a in basis:
        for b in basis:
            w=[zero]*3;w[i]=a;w[(i+1)%3]=b
            ck(f"mixed equivariance {i} {a.index(1)} {b.index(1)}",
               P(action(u,w))==action(u,P(w)))
for a in basis:
    for b in basis:
        for c in basis:
            w=(a,b,c)
            ck(f"tensor equivariance {a.index(1)}{b.index(1)}{c.index(1)}",
               invariant(action(u,w))==invariant(w))
for seed in range(1,9):
    w=tuple(tuple(F(((seed*(i+2)*(n+3))%11)-5,3) for n in range(8)) for i in range(3))
    r,q,p=w
    ck(f"complete square {seed}",mm(J(w),J(w))==
       ma(diag((norm(p)+norm(q),norm(p)+norm(r),norm(q)+norm(r))),J(P(w))))
    ck(f"trace metric {seed}",sum(mm(J(w),J(w))[i][i][0] for i in range(3))==
       2*(norm(r)+norm(q)+norm(p)))
    xi=(F(seed,3),F(seed+2,5),F(1-seed,7))
    full=ma(diag(xi),J(w));full2=jordan(full,full)
    trace=lambda mat:sum(mat[i][i][0] for i in range(3))
    actual=trace(jordan(full,full2))/3-trace(full)*trace(full2)/2+trace(full)**3/6
    expected=xi[0]*xi[1]*xi[2]-xi[0]*norm(r)-xi[1]*norm(q)-xi[2]*norm(p)+2*invariant(w)
    ck(f"complete original trace determinant {seed}",actual==expected)
x=s.symbols('x0:8');y=s.symbols('y0:8')
ck("full symbolic composition norm",s.expand(norm(om(x,y))-norm(x)*norm(y))==0)
inv=om(oc(x),om(x,y))
ck("full symbolic inverse with original parentheses",
   all(s.expand(inv[i]-norm(x)*y[i])==0 for i in range(8)))
t=s.symbols('t',real=True);w=(scale(t,basis[0]),basis[0],basis[0])
ck("fibre invariant",invariant(w)==t)
ck("fibre mixed product",P(w)==(basis[0],scale(t,basis[0]),scale(t,basis[0])))
ck("fibre original profile",M(w)==((0,1,0,0),(0,0,0,0),(0,0,0,1)))
ck("fibre quartic profile",M(P(w))==((0,t*t,0,0),(0,0,0,0),(0,0,0,t*t)))
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
T=[-s.I*m/2 for m in pauli]
curvature=(2*t*t*T[0])*(2*t*t*T[2])-(2*t*t*T[2])*(2*t*t*T[0])
ck("physical core curvature",s.simplify(curvature+4*t**4*T[1])==s.zeros(2))
ck("physical trace coefficient",s.simplify(-2*s.trace(curvature*curvature)-16*t**8)==0)
realblock=s.Matrix([[0,1,1],[1,0,t],[1,t,0]])
imagblock=s.Matrix([[0,1,-1],[1,0,t],[-1,t,0]])
ck("entire differential determinant",
   s.expand(realblock.det()*imagblock.det()**7+(2*t)**8)==0)
z=s.symbols('z0:24')
ww=tuple(tuple(z[8*i:8*i+8]) for i in range(3))
def flatten(y):return [a for x in y for a in x]
substitution=dict(zip(z,flatten(w)))
jac=s.Matrix(flatten(M(ww))+flatten(M(P(ww)))).jacobian(z).subs(substitution)
ck("combined profile differential rank",jac.rank()==10)
u0,v0=s.symbols('u0 v0')
ker=list((0,t*u0,0,-t*v0))+list(z[4:8])
ker+=list((0,u0,0,0))+list(z[12:16])
ker+=list((0,0,0,v0))+list(z[20:24])
ck("entire displayed combined kernel",
   all(s.expand(a)==0 for a in jac*s.Matrix(ker)))
note=Path(__file__).with_name("JORDAN_MARKED_SLOTS_AND_PROFILE_MAP.md").read_text(encoding="utf8")
ck("determinant display retains positive cubic summand",
   "\n+2\\mathcal I(r,q,p)." in note)
receipt=dict(checks=len(checks),all_passed=True,diagnostics=checks,
             scope="Exact algebra diagnostics, not a quantum state or continuum calculation.")
Path(__file__).with_name("JORDAN_MARKED_SLOTS_CHECKS.json").write_text(
    json.dumps(receipt,indent=2)+"\n",encoding="utf8")
print(json.dumps(dict(checks=len(checks),all_passed=True)))
