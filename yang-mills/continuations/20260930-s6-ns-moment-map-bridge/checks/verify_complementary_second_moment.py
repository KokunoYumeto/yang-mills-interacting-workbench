"""Exact independent Haar, cube-incidence, moment and return checks."""
from collections import Counter,defaultdict
from itertools import combinations,product
from pathlib import Path
import hashlib,json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent if HERE.name=="checks" else HERE
checks={}
def record(name,condition):
    checks[name]=bool(condition)
    assert checks[name],name
def qmul(a,b):
    return [a[0]*b[0]-sum(a[i]*b[i] for i in range(1,4)),
      a[0]*b[1]+a[1]*b[0]+a[2]*b[3]-a[3]*b[2],
      a[0]*b[2]-a[1]*b[3]+a[2]*b[0]+a[3]*b[1],
      a[0]*b[3]+a[1]*b[2]-a[2]*b[1]+a[3]*b[0]]
def sphere_moment(exps):
    if any(n%2 for n in exps):return s.S.Zero
    return s.S.One*s.prod(s.factorial2(n-1) if n else 1 for n in exps)/s.prod(4+2*k for k in range(sum(exps)//2))
def haar(poly,groups):
    variables=sum(map(list,groups),[])
    return s.expand(sum(coeff*s.prod(sphere_moment(exps[i*4:i*4+4]) for i in range(len(groups)))
                       for exps,coeff in s.Poly(s.expand(poly),*variables).terms()))
a,b,u=[s.symbols(c+"0:4",real=True) for c in ["a","b","u"]]
wp=2*qmul(a,u)[0]
wq=2*qmul([u[0],-u[1],-u[2],-u[3]],b)[0]
f=s.expand(wp*wq)
ef=0
for axis in range(1,4):
    generator=[0,0,0,0];generator[axis]=s.Rational(1,2)
    velocity=qmul(generator,u)
    def deriv(poly):return s.expand(sum(velocity[i]*s.diff(poly,u[i]) for i in range(4)))
    ef-=deriv(deriv(f))
record("adjacent_product_norm",haar(f*f,[a,b,u])==1)
record("shared_link_first_moment",haar(f*ef,[a,b,u])==s.Rational(3,2))
record("shared_link_second_moment",haar(ef*ef,[a,b,u])==3)
hf=s.Rational(9,2)*f+ef
record("adjacent_full_first_moment",haar(f*hf,[a,b,u])==6)
record("adjacent_full_second_moment",haar(hf*hf,[a,b,u])==s.Rational(147,4))
# Integrate only the shared quaternion to check the actual map to the boundary.
f0=0
for exps,coeff in s.Poly(f,*u).terms():f0+=coeff*sphere_moment(exps)
expected=s.Rational(1,2)*2*qmul(a,b)[0]
record("shared_constant_projection_exact",s.expand(f0-expected)==0)
record("shared_constant_projection_norm",haar(f0*f0,[a,b])==s.Rational(1,4))
record("shared_spin_one_norm",haar((f-f0)**2,[a,b,u])==s.Rational(3,4))
for power,value in [(2,1),(4,2),(6,5)]:
    record("trace_moment_"+str(power),haar((2*a[0])**power,[a])==value)
pauli=[s.Matrix([[0,1],[1,0]]),s.Matrix([[0,-s.I],[s.I,0]]),s.diag(1,-1)]
U=u[0]*s.eye(2)-s.I*sum((u[i+1]*pauli[i] for i in range(3)),s.zeros(2))
Ui=u[0]*s.eye(2)+s.I*sum((u[i+1]*pauli[i] for i in range(3)),s.zeros(2))
record("all_16_fundamental_Haar_entries",all(haar(U[i,j]*Ui[k,l],[u])==s.Rational(int(i==l and j==k),2) for i,j,k,l in product(range(2),repeat=4)))
Ts=[-s.I*q/2 for q in pauli]
record("spin_one_Casimir_original_generators",all(
    sum((-(t*(t*v-v*t)-(t*v-v*t)*t) for t in Ts),s.zeros(2))==2*v for v in Ts))

def face_vertices(n,i,j):
    ni=list(n);ni[i]+=1
    nij=ni.copy();nij[j]+=1
    nj=list(n);nj[j]+=1
    return [tuple(n),tuple(ni),tuple(nij),tuple(nj)]
def edge(a,b):return tuple(sorted((a,b)))
def lattice(L):
    faces=[]
    for n in product(range(-L,L+1),repeat=3):
        for i,j in combinations(range(3),2):
            if n[i]<L and n[j]<L:
                vs=face_vertices(n,i,j)
                faces.append(((n,i,j),vs,frozenset(edge(vs[k],vs[(k+1)%4]) for k in range(4))))
    lookup={label:i for i,(label,_,_) in enumerate(faces)}
    cubes=[]
    for n in product(range(-L,L),repeat=3):
        ids=[]
        for i,j in combinations(range(3),2):
            k=3-i-j
            for z in (0,1):
                base=list(n);base[k]+=z
                ids.append(lookup[(tuple(base),i,j)])
        cubes.append(tuple(sorted(ids)))
    return faces,cubes
faces,cubes=lattice(1)
edges=sorted(set().union(*(x[2] for x in faces)))
idx={e:i for i,e in enumerate(edges)}
masks=[sum(1<<idx[e] for e in f[2]) for f in faces]
record("original_L1_counts",(len(faces),len(edges),len(cubes))==(36,54,8))
# Meet in the middle: every six-set appears through its ten unordered 3+3 splits.
buckets=defaultdict(list)
for tri in combinations(range(len(faces)),3):
    mask=masks[tri[0]]^masks[tri[1]]^masks[tri[2]]
    buckets[mask].append(tri)
closed=Counter()
for bucket in buckets.values():
    for a3,b3 in combinations(bucket,2):
        if set(a3).isdisjoint(b3):closed[tuple(sorted(a3+b3))]+=1
record("all_six_face_cycles_in_L1_are_original_cubes",set(closed)==set(cubes))
record("each_six_cycle_has_ten_triple_splits",set(closed.values())=={10})

# Explicit oriented face-index contraction on one cube, independently of a surface formula.
n=(-1,-1,-1);oriented=[]
for i,j in combinations(range(3),2):
    k=3-i-j
    normal=int(s.LeviCivita(i,j,k))
    for side in (0,1):
        base=list(n);base[k]+=side
        vs=face_vertices(tuple(base),i,j)
        outward=1 if side else -1
        if normal!=outward:vs=list(reversed(vs))
        oriented.append(vs)
parent=list(range(24))
def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]];x=parent[x]
    return x
def union(x,y):parent[find(x)]=find(y)
occ=defaultdict(list)
for fi,vs in enumerate(oriented):
    for j in range(4):
        v,w=vs[j],vs[(j+1)%4]
        occ[edge(v,w)].append((v,w,4*fi+j,4*fi+(j+1)%4))
for entries in occ.values():
    first,second=entries
    assert first[:2]==second[:2][::-1]
    union(first[2],second[3]);union(first[3],second[2])
free=len(set(find(i) for i in range(24)))
record("cube_twelve_oppositely_oriented_link_pairs",len(occ)==12)
record("cube_eight_free_corner_indices",free==8)
record("cube_integral_exact_entries",s.Rational(2**free,2**len(occ))==s.Rational(1,16))

# Exhaust every ordered internal four-face choice in an actual cube and an extra face.
selected=list(cubes[0])
selected.append(next(i for i in range(36) if i not in selected))
samplecube={tuple(range(6))}
def sixth(indices):
    counts=Counter(indices)
    odd={i for i,n in counts.items() if n%2}
    if not odd:
        return s.prod({2:1,4:2,6:5}[n] for n in counts.values())
    if len(odd)==6 and tuple(sorted(odd)) in samplecube:return s.Rational(1,16)
    return s.S.Zero
size=len(selected)
mag=s.zeros(size)
for p,q in combinations(range(size),2):
    mag[p,q]=mag[q,p]=sum(sixth((p,q)+inds) for inds in product(range(size),repeat=4))
for p in range(size):mag[p,p]=sum(sixth((p,p)+inds) for inds in product(range(size),repeat=4))
NN=s.Matrix(size,size,lambda p,q:1 if p!=q and p<6 and q<6 else 0)
expected=(3*size**2-7*size+5)*s.eye(size)+(12*size-8)*s.ones(size)+s.Rational(3,2)*NN
record("every_sixth_moment_entry_cube_plus_face",mag==expected)

for length in (1,2,3):
    fs,cs=lattice(length)
    mm=len(fs)
    adjacency=[set() for _ in fs]
    for i,j in combinations(range(mm),2):
        overlap=len(fs[i][2]&fs[j][2])
        assert overlap<=1
        if overlap:adjacency[i].add(j);adjacency[j].add(i)
    degree=[len(v) for v in adjacency]
    cube_counts=[0]*mm
    nc=Counter()
    for cube in cs:
        for p in cube:cube_counts[p]+=1
        for p,q in combinations(cube,2):nc[p,q]+=1;nc[q,p]+=1
    record(f"L{length}_degree_bound",max(degree)<=12)
    record(f"L{length}_cube_boundary_counts",set(cube_counts)<= {1,2})
    record(f"L{length}_cube_row_sums",all(sum(nc[p,q] for q in range(mm))==5*cube_counts[p] for p in range(mm)))
    # Reflection acts on geometric vertex sets, including edge reversals.
    byvertices={frozenset(vs):p for p,(_,vs,_) in enumerate(fs)}
    reflect={p:byvertices[frozenset((-v[0],v[1],v[2]) for v in vs)] for p,(_,vs,_) in enumerate(fs)}
    record(f"L{length}_reflection_commutes_adjacency",all({reflect[q] for q in adjacency[p]}==adjacency[reflect[p]] for p in range(mm)))
    record(f"L{length}_reflection_commutes_cube_incidence",all(n==nc[reflect[p],reflect[q]] for (p,q),n in nc.items()))
M,kap,bb,alpha=s.symbols("M kappa b alpha",real=True)
mu=kap*(6*M-4)+alpha*(M-1)
record("full_complement_magnetic_subtraction",s.expand((3*M*M-7*M+5)-(M-1)**2-(2*M*M-5*M+4))==0)
record("variance_all_vacuum_terms_retained_then_cancelled",s.cancel(
 kap**2*(36*M-8)+2*kap*alpha*(6*M-4)+alpha**2*(M-1)-mu**2/(M-1)
 -kap**2*(4-4/(M-1)))==0)
record("variance_lower_at_all_M_ge36",s.Poly((2*M*M-5*M+1).subs(M,M+36),M).all_coeffs()==[2,139,2413])
# Direct finite matrix check of the second Schur return with a nonunit original Gram.
sp=s.symbols("s",positive=True)
Bmat=s.Matrix([[7,2,1],[2,6,1],[1,1,5]])
Cmat=s.Matrix([2,0,0])
m0=4;mu0=(Cmat.T*Bmat*Cmat)[0]
Q2=s.diag(0,1,1)
T=(Q2*Bmat*Cmat)[1:,:]
B2=Bmat[1:,1:]
left=(Cmat.T*(Bmat+sp*s.eye(3)).inv()*Cmat)[0]
right=m0*m0/(mu0+sp*m0-(T.T*(B2+sp*s.eye(2)).inv()*T)[0])
record("PK61_nonunit_Gram_exact_block_identity",s.cancel(left-right)==0)
K20=(Cmat.T*Bmat*Bmat*Cmat)[0]
record("PK58_next_map_Gram",s.cancel((T.T*T)[0]-(K20-mu0**2/s.Integer(m0)))==0)
for sval in [s.Rational(1,10),s.S.One,s.Integer(10)]:
    val=left.subs(sp,sval)
    lower=s.Rational(m0*m0,1)/(mu0+sval*m0)
    upper=m0/sval-mu0**2/(sval*(K20+sval*mu0))
    record("PK62_actual_rational_matrix_bounds_s"+str(sval),lower<=val<=upper<m0/sval)

proof=ROOT/"PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md"
if not proof.exists():proof=ROOT/"COMPLEMENTARY_SECOND_MOMENT_PROOF_20261009.md"
result={"schema":"complete-complement-second-moment-v1","proof":proof.name,
 "proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),"checks":checks,
 "check_count":len(checks),"all_passed":all(checks.values()),
 "scope":"Exact Haar-polynomial coefficients, complete six-face cycles in L=1, oriented cube entry contraction, all sixth-moment entries for a cube plus face, boundary incidence and reflection for L=1,2,3, complete scalar identities and a nonunit-Gram return check. General proofs remain in PK55–PK62."}
target=ROOT/"checks/COMPLEMENTARY_SECOND_MOMENT_CHECK.json" if HERE.name=="checks" else ROOT/"COMPLEMENTARY_SECOND_MOMENT_CHECK.json"
target.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8",newline="\n")
print(json.dumps({"all_passed":result["all_passed"],"checks":len(checks)}))
