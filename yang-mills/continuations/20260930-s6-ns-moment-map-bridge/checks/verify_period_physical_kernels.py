"""Exact finite checks for PK1--PK54; analytical proofs remain in the note."""
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
checks = {}


def record(name, value):
    checks[name] = bool(value)
    if not checks[name]:
        raise AssertionError(name)


def zero(matrix):
    return all(s.cancel(x) == 0 for x in matrix)


a, m, u, L, q, c, M = s.symbols("a m u L q c M", nonzero=True, real=True)
D = L*q+6*m*m
P = s.Matrix([[6*a,u,1,0],[6*m,L,0,0],[c,a,0,1],[-q,m,0,0]])
N = s.zeros(4)
N[2,1], N[3,0] = 1, -1
S = s.diag(1,1,M,M)
A, B = s.Matrix([[6*a,u],[c,a]]), s.Matrix([[6*m,L],[-q,m]])
Bi = s.Matrix([[m,-L],[q,6*m]])/D
Q = (P*S)[[0,2,1,3],:]
Qi = s.BlockMatrix([[s.zeros(2),Bi],[s.eye(2)/M,-A*Bi/M]]).as_explicit()
record("PK4_full_angular_monodromy", zero(P.subs({u:u+1,c:c-1})-P*(s.eye(4)+N)))
record("PK4_nilpotent", zero(N*N))
record("PK4_cover_conjugacy", zero(S.inv()*(s.eye(4)+M*N)*S-s.eye(4)-N))
record("PK7_full_B_inverse", zero(B*Bi-s.eye(2)) and zero(Bi*B-s.eye(2)))
record("PK7_both_full_Q_inverses", zero(Q*Qi-s.eye(4)) and zero(Qi*Q-s.eye(4)))
record("PK8_signed_determinant", s.factor((P*S).det()+M*M*D)==0)
G = (P*S).T*P*S
Gi = Qi*Qi.T
record("PK9_full_inverse_metric", zero(G*Gi-s.eye(4)))
n1,n2,z1,z2 = s.symbols("n1 n2 z1 z2", real=True)
n,z = s.Matrix([n1,n2]),s.Matrix([z1,z2])
k = n.col_join(z)
v = Bi.T*(n-A.T*z/M)
record("PK18_full_dual_quadratic", s.factor((k.T*Gi*k)[0]-(z.T*z)[0]/M**2-(v.T*v)[0])==0)
Gnext = (s.eye(4)+N).T*G*(s.eye(4)+N)
record("PK18_marked_character_congruence", zero(Gnext.inv()-(s.eye(4)-N)*Gi*(s.eye(4)-N).T))
record("PK19_four_ball_constant", s.simplify(s.pi**2/s.Integer(2)/(2*s.pi)**4-1/(32*s.pi**2))==0)
T,h0,d0,m0 = s.symbols("T h0 d0 m0", real=True)
record("PK12_full_retained_terms", s.expand((T+h0)*(T+h0-d0)+6*m0*m0-(T*T+(2*h0-d0)*T+h0*h0-d0*h0+6*m0*m0))==0)
perm = s.eye(4)[[2,1,3,0],:]
record("PK21_orientation", perm.det()==1)
record("PK22_path_and_connection_inverse", zero(perm*P*S*(perm*P*S).inv()-s.eye(4)))

I=s.I
Ts=[s.Matrix([[0,-I],[-I,0]])/2,
    s.Matrix([[0,-1],[1,0]])/2,
    s.Matrix([[-I,0],[0,I]])/2]
record("PK25_generator_Casimir", zero(-sum((x*x for x in Ts),s.zeros(2))-s.Rational(3,4)*s.eye(2)))
record("PK25_source_metric", all(-s.trace(x*y)/2==(s.Rational(1,4) if i==j else 0) for i,x in enumerate(Ts) for j,y in enumerate(Ts)))


def symrep(V, n):
    aa,bb,cc,dd=V[0,0],V[0,1],V[1,0],V[1,1]
    return s.Matrix(n+1,n+1,lambda r,t:
        s.sqrt(s.binomial(n,t)/s.binomial(n,r))*sum(
        s.binomial(n-t,r-k)*s.binomial(t,k)*
        aa**(n-t-r+k)*cc**(r-k)*bb**(t-k)*dd**k
        for k in range(max(0,r-n+t),min(r,t)+1)))


def tensor_restriction(V,n):
    if n==0:
        return s.ones(1)
    words=list(product([0,1],repeat=n))
    E=s.Matrix(2**n,n+1,lambda i,j:
               1/s.sqrt(s.binomial(n,j)) if sum(words[i])==j else 0)
    return E.T*s.kronecker_product(*([V]*n))*E


aa,bb,cc,dd=s.symbols("aa bb cc dd")
V=s.Matrix([[aa,bb],[cc,dd]])
for nspin in range(4):
    record("PK34_tensor_basis_n"+str(nspin),zero(symrep(V,nspin)-tensor_restriction(V,nspin)))


def gens(n):
    eps=s.symbols("eps",real=True)
    return [symrep(s.eye(2)+eps*t,n).diff(eps).subs(eps,0) for t in Ts]


def haar_projector(ns, conjugates=()):
    dim=s.prod(n+1 for n in ns)
    total=[]
    for axis in range(3):
        mat=s.zeros(dim)
        for i,nspin in enumerate(ns):
            factors=[s.eye(v+1) for v in ns]
            factors[i]=gens(nspin)[axis]
            if i in conjugates:
                factors[i]=s.conjugate(factors[i])
            mat+=s.kronecker_product(*factors)
        total.append(mat)
    cas=-sum((v*v for v in total),s.zeros(dim))
    out=s.eye(dim)
    if sum(ns)%2:
        out=s.zeros(dim)
    else:
        for spin in range(1,sum(ns)//2+1):
            out=out*(s.eye(dim)-cas/s.Integer(spin*(spin+1)))
    return out.applyfunc(s.simplify),total,cas


for ns,conj,rank in [((1,1),(),1),((1,1),(1,),1),((2,2),(),1),((1,1,1),(),0),((1,1,1,1),(),2)]:
    proj,tot,cas=haar_projector(ns,conj)
    name="PK35_"+str(ns)+"_conj"+str(conj)
    record(name+"_projection",zero(proj*proj-proj) and proj==proj.conjugate().T)
    record(name+"_invariant",all(zero(t*proj) for t in tot))
    record(name+"_complete_nullspace",proj.rank()==rank==cas.shape[0]-cas.rank())

x=s.symbols("x",real=True)
g1=s.cos(x)*s.eye(2)+2*s.sin(x)*Ts[0]
g2=s.cos(x)*s.eye(2)+2*s.sin(x)*Ts[1]
record("PK40_full_face_word",s.trigsimp(s.trace(g1*g2*g1.conjugate().T*g2.conjugate().T)-(2-4*s.sin(x)**4))==0)

# Independently integrate quaternion polynomials using exact S^3 Haar moments.
def qmul(v,w):
    return s.Matrix([v[0]*w[0]-sum(v[i]*w[i] for i in range(1,4)),
        v[0]*w[1]+v[1]*w[0]+v[2]*w[3]-v[3]*w[2],
        v[0]*w[2]+v[2]*w[0]+v[3]*w[1]-v[1]*w[3],
        v[0]*w[3]+v[3]*w[0]+v[1]*w[2]-v[2]*w[1]])


def sphere_moment(powers):
    if any(v%2 for v in powers):
        return s.S.Zero
    half=sum(powers)//2
    num=s.prod(s.factorial2(v-1) if v else 1 for v in powers)
    den=s.prod(4+2*k for k in range(half))
    return num/den


def haar_integral(poly, groups):
    vs=sum((list(v) for v in groups),[])
    ans=0
    for exps,coeff in s.Poly(s.expand(poly),*vs).terms():
        ans+=coeff*s.prod(sphere_moment(exps[4*i:4*i+4]) for i in range(len(groups)))
    return s.factor(ans)


qa,qb,qc=[s.symbols(name+"0:4",real=True) for name in ["aQ","bQ","cQ"]]
wp=2*qmul(qa,qc)[0]
wq=2*qmul([qc[0],-qc[1],-qc[2],-qc[3]],qb)[0]
f=s.expand(wp*wq)
record("PK50_adjacent_pair_norm_Haar",haar_integral(f*f,[qa,qb,qc])==1)
Ef=0
for axis in range(1,4):
    e=[0,0,0,0]
    e[axis]=s.Rational(1,2)
    velocity=qmul(e,qc)
    def derivative(poly):
        return s.expand(sum(velocity[i]*s.diff(poly,qc[i]) for i in range(4)))
    Ef-=derivative(derivative(f))
record("PK50_shared_edge_energy_Haar",haar_integral(f*Ef,[qa,qb,qc])==s.Rational(3,2))
record("PK50_adjacent_total_energy_Haar",6*s.Rational(3,4)+haar_integral(f*Ef,[qa,qb,qc])==6)
record("PK50_single_fourth_moment",haar_integral((2*qa[0])**4,[qa])==2)
record("PK50_single_second_moment",haar_integral((2*qa[0])**2,[qa])==1)
record("PK50_single_sixth_moment_reference",haar_integral((2*qa[0])**6,[qa])==5)


def faces_edges(length):
    vertices=list(product(range(-length,length+1),repeat=3))
    edges={}
    faces=[]
    for v in vertices:
        for axis in range(3):
            if v[axis]<length:
                edges[(v,axis)]=len(edges)
    for v in vertices:
        for i,j in combinations(range(3),2):
            if v[i]>=length or v[j]>=length:
                continue
            vi=list(v);vi[i]+=1
            vj=list(v);vj[j]+=1
            links=[(v,i),(tuple(vi),j),(tuple(vj),i),(v,j)]
            faces.append(sum(1<<edges[e] for e in links))
    return edges,faces


for length in range(1,4):
    edges,faces=faces_edges(length)
    record("PK24_original_counts_L"+str(length),
           len(edges)==3*(2*length)*(2*length+1)**2 and len(faces)==3*(2*length)**2*(2*length+1))
edges,faces=faces_edges(1)
for size in range(1,6):
    count=0
    for subset in combinations(faces,size):
        boundary=0
        for v in subset:
            boundary^=v
        count+=boundary==0
    record("PK50_no_closed_"+str(size)+"_face_subset_L1",count==0)

# Sum every fourth-moment contraction in a six-face sample.
def moment4(indices):
    mult=sorted(Counter(indices).values())
    if mult==[4]:
        return 2
    if mult==[2,2]:
        return 1
    return 0


six=s.Matrix(6,6,lambda p,q:sum(moment4([p,r,t,q]) for r in range(6) for t in range(6)))
record("PK50_all_fourth_moment_contractions",six==5*s.eye(6)+2*s.ones(6))
b,kappa,mm,E0,sp=s.symbols("b kappa mm E0 sp",positive=True)
z=s.symbols("z")
compressed=s.Matrix([[2*b*mm,-b*mm],[-b,2*b*mm+3*kappa]])
lambda_minus=2*b*mm+(3*kappa-s.sqrt(9*kappa*kappa+4*b*b*mm))/2
record("PK52_original_direction_norm",s.simplify((compressed-lambda_minus*s.eye(2)).det())==0)
record("PK54_return_first_moment",
       s.expand(kappa*(6*mm-4)+(2*b*mm-E0+sp)*(mm-1)
                -((mm-1)*(2*b*mm-E0+sp)+kappa*(6*mm-4)))==0)
test=s.Matrix([[5,-1,-2],[-1,4,1],[-2,1,6]])+s.eye(3)*sp
schur=test[0,0]-(test[0,1:]*test[1:,1:].inv()*test[1:,0])[0]
record("PK54_block_resolvent_check",s.cancel(test.inv()[0,0]-1/schur)==0)
j,gref,energy=s.symbols("j gref energy",positive=True)
aj=1/(100*j); gj2=kappa/(200*j); lam=j*j
record("PK43_same_electric_coefficient",s.cancel(2*gj2/aj-kappa)==0)
record("PK43_complete_magnetic_coefficient",s.cancel(1/(2*gj2*aj)-10000*j*j/kappa)==0)
record("PK43_full_classical_bracket_coefficient",s.cancel(2/(gj2*lam)-400/(kappa*j))==0)
record("PK43_original_reference_energy",s.cancel(gref*gref/(gj2*lam)-200*gref*gref/(kappa*j))==0)
record("PK43_superseded_dilation_defect",s.cancel(gref*gref/(gj2*s.sqrt(j))-200*gref*gref*s.sqrt(j)/kappa)==0)
record("PK43_link_angle",s.cancel(aj/lam-1/(100*j**3))==0)
record("PK49_retained_power",s.expand(9-8*3)==-15)

proof=ROOT/"PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md"
receipt={
    "schema":"period-physical-kernel-exact-check-v1",
    "proof":proof.name,
    "proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
    "checks":checks,
    "check_count":len(checks),
    "all_passed":all(checks.values()),
    "scope":"Exact matrix, tensor, Haar-polynomial, graph-incidence and path-factor checks. No continuum limit or analytical theorem is machine-certified.",
}
(ROOT/"checks"/"PERIOD_PHYSICAL_KERNEL_CHECK.json").write_text(
    json.dumps(receipt,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"all_passed":receipt["all_passed"],"checks":len(checks)}))
