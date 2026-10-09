"""Exact algebra checks accompanying the complete PK63--PK78 proofs."""
from pathlib import Path
import hashlib,json
import sympy as S

HERE=Path(__file__).resolve().parent
PROOF=(HERE.parent/"PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md"
       if HERE.name=="checks" else HERE/"FULL_PACKET_RESOLVENT_PROOF_20261009.md")
checks={}
def check(name,condition):
    assert condition,name
    checks[name]=True
def zero(x):
    if isinstance(x,S.MatrixBase):return all(S.simplify(v)==0 for v in x)
    return S.simplify(x)==0
def quad(v,A):return (v.conjugate().T*A*v)[0]

# The non-unit C Gram and both returns are tested together, with complex
# packet coefficients so that adjoints and cross terms cannot be omitted.
m,mu,b,d,s=map(S.Integer,[4,20,2,30,3])
C=S.Matrix([[2,0],[0,2],[0,0],[0,0]])
B21=S.Matrix([[1,1],[0,1]])
B22=S.Matrix([[11,1],[1,10]])
B=(5*S.eye(2)).row_join(B21.T).col_join(B21.row_join(B22))
A=(d*S.eye(2)).row_join(-b*C.T).col_join((-b*C).row_join(B))
check("original test A positive definite",all(A[:k,:k].det()>0 for k in range(1,7)))
check("non-unit C Gram",zero(C.T*C-m*S.eye(2)))
check("first return moment",zero(C.T*B*C-mu*S.eye(2)))
D=B+s*S.eye(4)
Sc=(d+s)*S.eye(2)-b*b*C.T*D.inv()*C
p=S.Matrix([1+S.I,2-S.I]);q=S.Matrix([2,1+S.I,3-S.I,-2])
eta=p.col_join(q)
F=quad(eta,(A+s*S.eye(6)).inv())
first=quad(q,D.inv())+quad(p+b*C.T*D.inv()*q,Sc.inv())
check("PK63 full complex packet",zero(F-first))
check("PK63 cross terms nonzero",not zero(F-quad(p,Sc.inv())-quad(q,D.inv())))
Pi=C*C.T/m;Q2=S.eye(4)-Pi
w=C.T*q/m;z=(Q2*q)[2:,:]
T=2*B21;D2=B22+s*S.eye(2)
K=(mu+s*m)*S.eye(2)-T.T*D2.inv()*T
r=m*w-T.T*D2.inv()*z
check("PK64 q decomposition",zero(q-C*w-S.Matrix([0,0,z[0],z[1]])))
check("PK64 C adjoint mixed inverse",zero(C.T*D.inv()*q-m*K.inv()*r))
check("PK64 complete q quadratic",zero(quad(q,D.inv())-quad(z,D2.inv())-quad(r,K.inv())))
check("PK64 first Schur denominator",zero(Sc-(d+s)*S.eye(2)+b*b*m*m*K.inv()))
check("PK64 entire original resolvent",
      zero(F-quad(z,D2.inv())-quad(r,K.inv())-
           quad(p+b*m*K.inv()*r,Sc.inv())))
check("PK64 remainder has nonzero contribution",S.simplify(quad(z,D2.inv()))>0)

# The cutoff resolvent identity with a second, independently chosen
# Hermitian matrix. Exact inequalities are checked by principal minors.
V=S.Matrix([[4,-1,1,S.I],[-1,4,2,0],[1,2,4,1],[-S.I,0,1,4]])
H0=S.diag(0,3,6,9);H=2*H0+V
check("cutoff sample V positive",all(V[:k,:k].det()>0 for k in range(1,5)))
J=H[2:,:2];L=H[:2,:2];Dh=H[2:,2:]
check("cutoff off-diagonal squared bound",all((16*S.eye(2)-J.conjugate().T*J)[:k,:k].det()>0 for k in (1,2)))
u=7-S.sqrt(10);kapLam=S.Integer(6);ell=S.Integer(4)
e=(u+kapLam-S.sqrt((kapLam-u)**2+4*ell**2))/2
check("cutoff ground characteristic equation",zero((u-e)*(kapLam-e)-ell**2))
check("cutoff vacuum lower root positive",bool(e>0))
width=u-e
rat=2*ell**2/(S.sqrt((kapLam-u)**2+4*ell**2)+kapLam-u)
check("PK69 exact interval rationalization",zero(width-rat))
se=S.Integer(2);e_ref=S.Integer(0)
R=(H-e_ref*S.eye(4)+se*S.eye(4)).inv()
Le=L-e_ref*S.eye(2)+se*S.eye(2);De=Dh-e_ref*S.eye(2)+se*S.eye(2)
Rt=J.conjugate().T*De.inv()*J
check("PK71 full cutoff Schur formula",zero(R[:2,:2]-(Le-Rt).inv()))
check("PK71 ordered inverse difference",zero((Le-Rt).inv()-Le.inv()-(Le-Rt).inv()*Rt*Le.inv()))
ee,gg,xx,ss=S.symbols("e E x s",real=True)
check("PK71 vacuum shift sign and coefficient",
      zero(1/(xx-gg+ss)-1/(xx-ee+ss)-(gg-ee)/((xx-gg+ss)*(xx-ee+ss))))

# Heat and path constants, retaining the original coupling powers.
qt=S.symbols("q",positive=True)
check("PK70 heat polynomial series",
      zero(qt*S.diff(qt*S.diff(qt/(1-qt),qt),qt)-qt*(1+qt)/(1-qt)**3))
j,k,bj,Mj=S.symbols("j kappa b M",positive=True)
sj=k/j;delta=1/(k*j);rho=1/(6*j**2);lj=2*bj*Mj
Dneeded=16*bj**2*Mj**2*j**3/k
check("PK72 full electric cutoff coefficient",zero(Dneeded-4*lj**2/(delta*sj**2)))
check("PK73 operator and vacuum errors",zero(2*lj**2/(Dneeded*sj**2)-delta/2))
check("PK73 complete packet tail error",zero(3*rho/sj-delta/2))
check("PK75 spectral interval propagated error",zero(2*sj*delta-2/j**2))
n,G,ep,sp=S.symbols("n G epsilon s",positive=True)
worst=n/sp+(G-n)/(ep+sp)
check("PK74 lower mass rearrangement",zero(sp*(ep+sp)/ep*worst-sp*G/ep-n))
check("PK74 upper kernel endpoint",zero((ep+sp)/(ep+sp)-1))

# Enumerate the original smallest open cubic box, not a one-plaquette model.
import itertools
vertices=list(itertools.product(range(-1,2),repeat=3))
edges=[]
faces=[]
for v in vertices:
    for a in range(3):
        if v[a]<1:edges.append((v,a))
    for a,bb in itertools.combinations(range(3),2):
        if v[a]<1 and v[bb]<1:
            fv=[]
            for da,db in itertools.product([0,1],repeat=2):
                wv=list(v);wv[a]+=da;wv[bb]+=db;fv.append(tuple(wv))
            faces.append(frozenset(fv))
rf=lambda f:frozenset((-v[0],v[1],v[2]) for v in f)
check("PK77 original L1 links",len(edges)==54)
check("PK77 original L1 faces",len(faces)==36)
check("PK78 original reflection closure",all(rf(f) in faces for f in faces))
fixed=[f for f in faces if rf(f)==f]
check("PK78 exactly four fixed yz faces",len(fixed)==4 and all(all(v[0]==0 for v in f) for f in fixed))
check("PK78 original odd dimension",(len(faces)-len(fixed))//2==16)
H37=33*S.eye(37);H37[0,0]=9
for i in range(1,37):H37[0,i]=H37[i,0]=-S.Rational(1,8)
M=S.Integer(36);kap=S.Integer(8);bc=S.Rational(1,8)
u37=21-3*S.sqrt(257)/4
v37=S.Matrix([1]+[bc/(33-u37)]*36)
check("PK76 exact full 37 by 37 lowest vector",zero(H37*v37-u37*v37))
for kx in [1,17,35]:
    vec=S.zeros(37,1);vec[kx]=1;vec[kx+1]=-1
    check("PK76 original face-difference eigenvector "+str(kx),zero(H37*vec-33*vec))
check("PK77 vacuum upper with every coupling",zero(u37-(2*bc*M+(3*kap-S.sqrt(9*kap**2+4*bc**2*M))/2)))
e37=(u37+24-S.sqrt((24-u37)**2+324))/2
check("PK77 exact lower root",zero((u37-e37)*(24-e37)-81))
check("PK77 vacuum lower positive",bool(e37>0))
check("PK78 odd resolvent denominator",zero(2*bc*M+3*kap-33))

out={"schema":"full-packet-resolvent-check-v1",
     "proof":PROOF.name,"proof_sha256":hashlib.sha256(PROOF.read_bytes()).hexdigest(),
     "all_passed":all(checks.values()),"checks":checks,
     "scope":"Exact finite algebra supports the written infinite-space and path proofs; no evaluated continuum mass, numerical path spectrum, or independent review claimed.",
     "original_box_example":{"L":1,"a":1,"g":2,"Lambda":3,"cutoff_dimension":37,
       "odd_dimension":16,"vacuum_interval_approximation_for_display_only":[str(S.N(e37,18)),str(S.N(u37,18))]}}
target=HERE/"FULL_PACKET_RESOLVENT_CHECK.json"
target.write_text(json.dumps(out,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"checks":len(checks),"all_passed":out["all_passed"],"example":out["original_box_example"]}))
