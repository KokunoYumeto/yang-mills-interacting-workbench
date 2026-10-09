"""Exact checks supporting the complete written packet-moment and escape proof."""
from pathlib import Path
import hashlib,json,math
import sympy as s
W=Path(__file__).resolve().parent
checks=[]
def eq(name,a,b=0):
    assert s.simplify(a-b)==0,name
    checks.append(name)
k,b,M,E0=s.symbols("k b M E0",positive=True)
T,V=s.symbols("T V",commutative=False)
H=k*T+2*b*M-b*V
expanded=k*k*T*T+4*k*b*M*T-k*b*(T*V+V*T)+4*b*b*M*M-4*b*b*M*V+b*b*V*V
eq("full noncommuting Hamiltonian square",s.expand(H*H-expanded))
eq("both actual vacuum-shift terms",s.expand((H-E0)**2-(H*H-2*E0*H+E0**2)))
eq("mixed heat derivative signs",s.expand(k*b*(-T*V-V*T)-(-k*b*(T*V+V*T))))
x=s.symbols("x0:4",real=True)
I=s.I
U=s.Matrix([[x[0]-I*x[3],-x[2]-I*x[1]],[x[2]-I*x[1],x[0]+I*x[3]]])
Ui=U.conjugate().T
eq("original trace",s.trace(U),2*x[0])
assert s.simplify(U*Ui-s.eye(2)*sum(z*z for z in x))==s.zeros(2)
checks.append("original quaternion inverse numerator")
def haar(expr):
    result=0
    for powers,coeff in s.Poly(s.expand(expr),*x).terms():
        if any(p%2 for p in powers):continue
        ks=[p//2 for p in powers]
        weight=s.prod(s.factorial(2*q)/(4**q*s.factorial(q)) for q in ks)/s.factorial(1+sum(ks))
        result+=coeff*weight
    return s.simplify(result)
eq("Haar probability",haar(1),1)
eq("one face mean",haar(s.trace(U)),0)
eq("two identical face slots",haar(s.trace(U)**2),1)
eq("four original face slots",haar(s.trace(U)**4),2)
eps=s.Matrix([[0,1],[-1,0]])
for a in range(2):
 for c in range(2):
  for d in range(2):
   for e in range(2):
    eq(f"shared positive slots {a}{c}{d}{e}",haar(U[a,c]*U[d,e]),eps[a,d]*eps[c,e]/2)
    eq(f"shared inverse slots {a}{c}{d}{e}",haar(U[a,c]*Ui[d,e]),s.Rational(int(a==e and c==d),2))
r,y=s.symbols("r y",positive=True)
z=s.symbols("z",real=True)
eq("trial Ward derivative",s.diff((1-z*z)**s.Rational(3,2)*s.exp(4*r*z),z)/(s.sqrt(1-z*z)*s.exp(4*r*z)),
   -3*z+4*r*(1-z*z))
eq("gamma mean with all scale factors",s.gamma(s.Rational(5,2))/(4*r*s.gamma(s.Rational(3,2))),3/(8*r))
m=s.symbols("m",real=True)
eq("all four mean-link factors",1-m**4,(1-m)*(1+m+m*m+m**3))
N=s.symbols("N",positive=True)
opt=2*s.sqrt(b*M/(k*N))
eq("full variational optimum",3*k*N*opt/4+3*b*M/opt,3*s.sqrt(k*b*N*M))
q=s.symbols("q",positive=True)
eq("Haar Laplace constant",2*s.sqrt(2)/s.pi*s.gamma(s.Rational(3,2))/(2*q)**s.Rational(3,2),
   1/(2*s.sqrt(s.pi)*q**s.Rational(3,2)))
delta=s.symbols("delta",positive=True)
eq("optimized small-potential bound",s.exp(s.Rational(3,2))/(2*s.sqrt(s.pi)*(1/(8*delta))**s.Rational(3,2)),
   8*s.sqrt(2/s.pi)*s.exp(s.Rational(3,2))*delta**s.Rational(3,2))
for L in [1,2,3,5]:
    used=set();faces=0
    for u in range(L):
     for v in range(L):
      for w in range(2*L+1):
       a,c,d=-L+2*u,-L+2*v,-L+w
       edges={(0,a,c,d),(1,a+1,c,d),(0,a,c+1,d),(1,a,c,d)}
       assert used.isdisjoint(edges)
       used.update(edges);faces+=1
    assert faces==L*L*(2*L+1) and 12*faces==3*(2*L)**2*(2*L+1)
    checks.append(f"actual edge-disjoint selected faces L={L}")
j,ks=s.symbols("j ks",positive=True)
Nj=3*(2*j**4)*(2*j**4+1)**2
Mj=3*(2*j**4)**2*(2*j**4+1)
nj=j**8*(2*j**4+1)
bj=10000*j*j/ks
eq("exact face subset count",Mj,12*nj)
eq("exact link to subset ratio",Nj/nj,12+6/j**4)
eq("exact link to whole-face ratio",Nj/Mj,1+1/(2*j**4))
eq("full original path vacuum ratio",3*s.sqrt(ks*bj*Nj*Mj)/(bj*Mj/s.sqrt(j)),
   3*ks/(100*s.sqrt(j))*s.sqrt(Nj/Mj))
eq("full original excitation threshold ratio",ks*j/(bj*Mj/s.sqrt(j)),
   ks**2/(10000*Mj*s.sqrt(j)))
eq("resolvent outside expanding interval",(ks/j)/(ks*j+ks/j),1/(j*j+1))
eq("retained cutoff error after multiplication",(ks/j)/(ks*j),1/(j*j))
for eigenvalues,coeffs in [([s.Rational(1,3),2,7],[2,3,5]),([1,1,4],[1,4,2])]:
    # Set u=log(2)/2; the exact weights are 2^{-lambda}.
    weights=[c*s.Integer(2)**(-v) for v,c in zip(eigenvalues,coeffs)]
    q0=sum(weights);q1=sum(v*w for v,w in zip(eigenvalues,weights));q2=sum(v*v*w for v,w in zip(eigenvalues,weights))
    double=sum((a-c)**2*wa*wc for a,wa in zip(eigenvalues,weights) for c,wc in zip(eigenvalues,weights))/2
    eq("interacting energy-flow variance "+str(eigenvalues),q2*q0-q1*q1,double)
    assert s.N(double)>=0
    checks.append("interacting energy-flow sign "+str(eigenvalues))
proof=W.parent/("PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md" if W.name=="checks" else "PACKET_MOMENTS_AND_ESCAPE_PROOF_20261009.md")
out={"status":"passed","all_passed":True,"check_count":len(checks),"checks":{name:True for name in checks},
     "proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
     "scope":"Exact algebra, original graph counts, Haar slot contractions and constants. Infinite-volume escape is proved in the written argument, not certified by finite samples.",
     "independent_review":False}
(W/"PACKET_MOMENTS_ESCAPE_CHECK.json").write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"status":out["status"],"check_count":len(checks)}))
