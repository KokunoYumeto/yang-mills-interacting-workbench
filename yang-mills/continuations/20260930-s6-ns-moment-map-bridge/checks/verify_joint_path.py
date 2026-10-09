"""Exact support-mass factors, global trace coordinates and complete word derivatives."""
from pathlib import Path
import hashlib,itertools,json
import sympy as s
HERE=Path(__file__).resolve().parent;checks={}
def eq(name,a,b=0):
    delta=a-b
    if isinstance(delta,s.MatrixBase):
        assert all(s.simplify(s.expand(x))==0 for x in delta),name
    else:assert s.simplify(s.expand(delta))==0,name
    checks[name]=True
x,t,kappa,a,j,m,d,N,M,R=s.symbols("x t kappa a j m d N M R",positive=True)
eq("heat x squared integral",s.integrate(x*x*s.exp(-t*x*x/4),(x,0,s.oo)),2*s.sqrt(s.pi)/t**s.Rational(3,2))
eq("heat twice x integral",s.integrate(2*x*s.exp(-t*x*x/4),(x,0,s.oo)),4/t)
eq("heat scalar integral",s.integrate(s.exp(-t*x*x/4),(x,0,s.oo)),s.sqrt(s.pi)/s.sqrt(t))
eq("original Casimir shift",(m*m-1)/4,m*s.Rational(1,2)*(m*s.Rational(1,2))-s.Rational(1,4))
B=3*s.sqrt(N*M)/a;opt_t=N/(2*B)
eq("full vacuum exponential at chosen time",2*opt_t*B,N)
eq("full heat time",2*kappa*opt_t,kappa*a*s.sqrt(N/M)/3)
eq("Haar ball density and full dimension",(16*s.pi**2)**(-d)*s.pi**(3*d/2)*R**(3*d),R**(3*d)/(16**d*s.pi**(d/2)))
n=3*m*(m+1)**2;faces=3*m*m*(m+1);chords=2*m**3+3*m*m
eq("tree count with all boundary vertices",n-(m+1)**3+1,chords)
eq("full link face ratio",n/faces,1+1/m)
eq("full link chord ratio",n/chords,3*(m+1)**2/(m*(2*m+3)))
eq("limiting link chord ratio",s.limit(n/chords,m,s.oo),s.Rational(3,2))
nj=n.subs(m,2*j**4);mj=faces.subs(m,2*j**4);dj=chords.subs(m,2*j**4)
eq("retained chord polynomial",dj,16*j**12+12*j**8)
eq("retained link polynomial",nj,24*j**12+24*j**8+6*j**4)
eq("retained face polynomial",mj,24*j**12+12*j**8)
eq("original heat time on joint path",(kappa*a*s.sqrt(N/M)/3).subs({a:1/(100*j),N:nj,M:mj}),kappa/(300*j)*s.sqrt(1+1/(2*j**4)))
g=s.symbols("g",positive=True)
eq("original kinetic coefficient",(2*g*g/a).subs({g:s.sqrt(kappa/(200*j)),a:1/(100*j)}),kappa)
eq("original magnetic coefficient",(1/(2*g*g*a)).subs({g:s.sqrt(kappa/(200*j)),a:1/(100*j)}),10000*j*j/kappa)
eq("exact factorial dimension",3*dj/2,24*j**12+18*j**8)
eq("support exponent",s.Rational(3,2)*s.Rational(3,2)-s.Rational(3,2)*12,-s.Rational(63,4))
eq("support radius growth threshold",s.Rational(63,4)/3,s.Rational(21,4))
for L in range(1,5):
    verts=list(itertools.product(range(-L,L+1),repeat=3))
    edges=[(v,axis) for v in verts for axis in range(3) if v[axis]<L]
    plaquettes=[(v,i,h) for v in verts for i in range(3) for h in range(i+1,3) if v[i]<L and v[h]<L]
    eq(f"all original edges L={L}",len(edges),n.subs(m,2*L))
    eq(f"all original faces L={L}",len(plaquettes),faces.subs(m,2*L))
    eq(f"all original chords L={L}",len(edges)-len(verts)+1,chords.subs(m,2*L))
I=s.eye(2);pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.Matrix([[1,0],[0,-1]])]
T=[-s.I*p/2 for p in pauli]
for alpha in range(3):
    eq("fundamental generator square "+str(alpha),T[alpha]**2,-I/4)
    for beta in range(3):
        eq(f"complete trace metric {alpha},{beta}",-2*s.trace(T[alpha]*T[beta]),int(alpha==beta))
q0,q1,q2,q3=s.symbols("q0 q1 q2 q3",real=True)
U=q0*I+sum((2*q*T0 for q,T0 in zip([q1,q2,q3],T)),s.zeros(2))
for alpha,q in enumerate([q1,q2,q3]):
    eq("global real group coordinate "+str(alpha),-2*s.trace(T[alpha]*U),2*q)
eq("full norm constraint",sum((-2*s.trace(T0*U))**2 for T0 in T)-4*(1-(s.trace(U)/2)**2),4*(q0*q0+q1*q1+q2*q2+q3*q3-1))
theta=s.symbols("theta",real=True)
for alpha in range(3):
    expU=s.cos(theta/2)*I+2*s.sin(theta/2)*T[alpha]
    eq("global coordinate on full group circle "+str(alpha),-2*s.trace(T[alpha]*expU),2*s.sin(theta/2))
    eq("retained original coordinate derivative "+str(alpha),s.diff(-2*s.trace(T[alpha]*expU),theta).subs(theta,0),1)
matrices=[(I+2*T[0])/s.sqrt(2),(3*I+8*T[1])/5,(12*I+10*T[2])/13]
for i,U0 in enumerate(matrices):
    eq("exact word-test unitarity "+str(i),U0.H*U0,I);eq("exact word-test determinant "+str(i),s.det(U0),1)
word=[(0,1),(1,-1),(0,-1),(2,1),(1,1),(0,1)]
def prod(mats):
    ans=I
    for mat in mats:ans=ans*mat
    return ans
base=[matrices[e] if orient==1 else matrices[e].inv() for e,orient in word]
for edge in range(3):
    for alpha in range(3):
        X=T[alpha];first=[];second=[];curve=[]
        for (e,orient),A0 in zip(word,base):
            D=s.zeros(2) if e!=edge else X*A0 if orient==1 else -A0*X
            DD=s.zeros(2) if e!=edge else X*X*A0 if orient==1 else A0*X*X
            first.append(D);second.append(DD);curve.append(A0+t*D+t*t*DD/2)
        p=prod(curve)
        f=sum((prod([first[r] if k==r else base[k] for k in range(len(word))]) for r in range(len(word))),s.zeros(2))
        ff=sum((prod([second[r] if k==r else base[k] for k in range(len(word))]) for r in range(len(word))),s.zeros(2))
        ff+=2*sum((prod([first[k] if k in [r,h] else base[k] for k in range(len(word))]) for r in range(len(word)) for h in range(r+1,len(word))),s.zeros(2))
        eq(f"all repeated word first derivatives {edge},{alpha}",p.diff(t).subs(t,0),f)
        eq(f"all repeated word second derivatives {edge},{alpha}",p.diff(t,2).subs(t,0),ff)
F=s.Function("F")(x);psi=s.Function("psi")(x);E=s.symbols("E",real=True)
potential=E+kappa*s.diff(psi,x,2)/psi
eq("full actual ground-state transform",-kappa*s.diff(F*psi,x,2)+potential*F*psi-E*F*psi,kappa*psi*(-s.diff(F,x,2)-2*s.diff(psi,x)/psi*s.diff(F,x)))
eq("full integration by parts cancellation",-F*psi**2*s.diff(F,x,2)-2*F*psi*s.diff(psi,x)*s.diff(F,x),psi**2*s.diff(F,x)**2-s.diff(F*psi**2*s.diff(F,x),x))
phase=s.Function("theta")(x);phaseR=s.Function("thetaR")(x);half=(s.sin(phase)-s.sin(phaseR))/2
eq("full antisymmetrized first derivative",s.diff(half,x),(s.cos(phase)*s.diff(phase,x)-s.cos(phaseR)*s.diff(phaseR,x))/2)
eq("full antisymmetrized second derivative",s.diff(half,x,2),(s.cos(phase)*s.diff(phase,x,2)-s.sin(phase)*s.diff(phase,x)**2-s.cos(phaseR)*s.diff(phaseR,x,2)+s.sin(phaseR)*s.diff(phaseR,x)**2)/2)
proof=HERE.parent/("PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md" if HERE.name=="checks" else "JOINT_PATH_CUTOFF_AND_GLOBAL_OBSERVABLE_20261009.md")
out={"all_passed":True,"checks":checks,"check_count":len(checks),"proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
     "scope":"Exact original heat/Haar/path constants, boundary counts, SU(2) signs, repeated inverse-word derivatives and full ground-state product rule. Complete asymptotic and operator proofs are in PK132–PK157.","independent_review":False}
(HERE/"JOINT_PATH_GLOBAL_OBSERVABLE_CHECK.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"all_passed":True,"checks":len(checks),"support_exponent":"-63/4","radius_threshold":"21/4"}))
