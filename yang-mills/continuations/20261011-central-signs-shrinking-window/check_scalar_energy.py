"""Diagnostics for SLE; finite matrix/configuration samples are not YM vacuum samples."""
from pathlib import Path
import itertools,json,math
import numpy as np
O=Path(__file__).resolve().parent
rng=np.random.default_rng(610132)
checks=[]
def ck(name,x,y,atol=2e-9):
    err=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
    scale=max(1.,float(np.max(np.abs(y))))
    assert err<=atol*scale,(name,err,scale)
    checks.append(dict(name=name,max_error=err))
# Independent real local tensor Hamiltonians, with their computed actual grounds.
X=np.array([[0.,1.],[1.,0.]]);Z=np.diag([1.,-1.]);I=np.eye(2)
def local(mats,n=6):
    out=np.array([[1.]])
    for i in range(n):out=np.kron(out,mats.get(i,I))
    return out
comm=lambda a,b:a@b-b@a
for trial in range(5):
    n=6
    kinetic=[-(.7+rng.random())*local({i:X},n) for i in range(n)]
    bonds=[(.2+rng.random())*local({i:Z,i+1:Z},n) for i in range(n-1)]
    onsite=[.1*rng.normal()*local({i:Z},n) for i in range(n)]
    A=[kinetic[i]+onsite[i]+sum((bonds[k]/2 for k in range(n-1) if i in [k,k+1]),np.zeros((2**n,2**n))) for i in range(n)]
    H=sum(A);lam,U=np.linalg.eigh(H);psi=U[:,0]
    if psi.sum()<0:psi=-psi
    assert min(psi)>0
    K=H-lam[0]*np.eye(2**n)
    V=np.column_stack([a@psi-(psi@a@psi)*psi for a in A])
    N=V.T@V;E=V.T@K@V;ZZ=V.T@K@K@V
    for i in range(n):
        for j in range(n):
            ck('double commutator',E[i,j],.5*psi@comm(A[i],comm(H,A[j]))@psi)
            if abs(i-j)>2:ck('range two',E[i,j],0)
    c=rng.normal(size=n)+1j*rng.normal(size=n)
    for M in [N,E,ZZ]:
        ck('row sums',M@np.ones(n),np.zeros(n))
        ck('raw complex differences',c.conj()@M@c,-.5*np.sum(abs(c[:,None]-c[None,:])**2*M))
        assert np.linalg.eigvalsh(M).min()>-2e-9
    source=K@V;spec=U[:,1:].T@source;energy=lam[1:]-lam[0]
    for M,power in [(N,2),(E,1),(ZZ,0)]:
        ck('inverse spectral moments',M,spec.T@(spec/energy[:,None]**power))
        ck('kernel rank',np.linalg.matrix_rank(M,tol=1e-8),np.linalg.matrix_rank(source,tol=1e-8))
# Original SU(2) ordered words, including inverse differentiated factors.
T=np.array([[[0,-1j/2],[-1j/2,0]],[[0,-.5],[.5,0]],[[-1j/2,0],[0,1j/2]]])
def su2():
    q=rng.normal(size=4);q=q/np.linalg.norm(q)
    return q[0]*np.eye(2)+2*sum(q[k+1]*T[k] for k in range(3))
def prod(f):
    ans=np.eye(2,dtype=complex)
    for u in f:ans=ans@u
    return ans
vertices=list(itertools.product(range(4),repeat=3));edges=[]
for z in vertices:
    for d in range(3):
        if z[d]<3:edges.append((z,d))
eid={e:i for i,e in enumerate(edges)};faces=[]
for z in vertices:
    for d,k in itertools.combinations(range(3),2):
        if z[d]>=3 or z[k]>=3:continue
        zd=list(z);zk=list(z);zd[d]+=1;zk[k]+=1
        faces.append(([eid[(z,d)],eid[(tuple(zd),k)],eid[(tuple(zk),d)],eid[(z,k)]],[1,1,-1,-1]))
inc=[[] for e in edges]
for p,(es,sgn) in enumerate(faces):
    for e in es:inc[e].append(p)
neigh=[set([e])|{g for p in inc[e] for g in faces[p][0]} for e in range(len(edges))]
dist2=[set().union(*(neigh[g] for g in neigh[e])) for e in range(len(edges))]
for e in range(len(edges)):
    for f in range(len(edges)):
        if f not in dist2[e]:assert not neigh[e]&neigh[f]
checks.append(dict(name='entire open cube coface supports',max_error=0))
for trial in range(3):
    links=[su2() for e in edges];gr={};hol={};deficits=[]
    for p,(es,signs) in enumerate(faces):
        fac=[links[e] if s==1 else links[e].conj().T for e,s in zip(es,signs)]
        D=2-np.trace(prod(fac)).real;deficits.append(D)
        for i,(e,s) in enumerate(zip(es,signs)):
            A=prod(fac[i+1:]+fac[:i])
            hol[p,e]=fac[i]@A if s==1 else A@fac[i]
            grad=[]
            for t in T:
                ff=list(fac);ff[i]=t@fac[i] if s==1 else -fac[i]@t
                grad.append(-np.trace(prod(ff)).real)
            gr[p,e]=np.array(grad)
            ck('edge Casimir gradient norm',np.dot(grad,grad),D-D*D/4)
    c=rng.normal(size=len(edges))+1j*rng.normal(size=len(edges))
    bar=[sum(c[e] for e in es)/4 for es,s in faces]
    for p,(es,ss) in enumerate(faces):
        ck('full face divergence',sum(c[e]-bar[p] for e in es)*.75*(2-deficits[p]),0)
    allpairs=[(e,p,q) for e in range(len(edges)) for p,q in itertools.combinations(inc[e],2)]
    for e,p,q in allpairs:
        Hp,Hq=hol[p,e],hol[q,e]
        ep=faces[p][1][faces[p][0].index(e)];eq=faces[q][1][faces[q][0].index(e)]
        sigma=ep*eq
        G=Hp@(Hq.conj().T if sigma==1 else Hq)
        R=Hp@(Hq if sigma==1 else Hq.conj().T)
        ck('six-eight ordered trace',gr[p,e]@gr[q,e],.25*np.trace(G-R).real)
    # Actual no-coface coefficient of the potential double commutator.
    kappa=1.7;a=1/(100*(trial+1));b=1/(kappa*a*a)
    candidates=[(e,f) for e in range(len(edges)) for f in dist2[e] if f not in neigh[e]]
    for e,f in candidates[::max(1,len(candidates)//55)]:
        alpha={g:sum(((float(g==f)-.25)*gr[p,g] for p in inc[f] if g in faces[p][0]),np.zeros(3)) for g in neigh[f]}
        contraction=sum(alpha[g]@sum((gr[q,g] for q in inc[e] if g in faces[q][0]),np.zeros(3)) for g in alpha)
        direct=-kappa*b*b/4*contraction
        expanded=kappa*b*b/16*sum(gr[p,g]@gr[q,g] for p in inc[f] for q in inc[e] for g in set(faces[p][0])&set(faces[q][0]))
        ck('distance two coefficient',direct,expanded,atol=2e-12)
# Exact original box and face averages for a general complex quadratic polynomial.
for j in [1,3,11,70]:
    a=1/(100*j);kappa=1.3;b=1/(kappa*a*a);t=kappa*kappa*a**3/2
    ck('original receiver factor',t*b/kappa,a/2)
    H=rng.normal(size=(3,3))+1j*rng.normal(size=(3,3));H=(H+H.T)/2
    lin=rng.normal(size=3)+1j*rng.normal(size=3);x=rng.normal(size=3)
    fun=lambda y:.5*y@H@y+lin@y+(2+.4j)
    cell=lambda y:fun(y)+a*a*np.trace(H)/24
    for d,k in itertools.combinations(range(3),2):
        ed=np.eye(3)[d];ek=np.eye(3)[k]
        avg=sum(cell(x+a*v/2) for v in [ed,-ed,ek,-ek])/4
        exact=a*a*(np.trace(H)/24+(H[d,d]+H[k,k])/16)
        ck('quadratic interpolation both contributions',avg-fun(x),exact,atol=2e-12)
    N=2.3;iso=lambda y:N*np.dot(y,y)/2
    avg=sum(iso(x+a*v/2)+N*a*a/8 for v in [np.eye(3)[0],-np.eye(3)[0],np.eye(3)[1],-np.eye(3)[1]])/4
    ck('sharp local interpolation constant',avg-iso(x),N*a*a/4)
    c=rng.normal(size=16)
    vals=sorted(set(c));levels=[((u+v)/2,v-u) for u,v in zip(vals[:-1],vals[1:])]
    ck('signed level raw edge reconstruction',np.min(c)+sum(width*(c>r) for r,width in levels),c)
    es=[0,2,7,11];bar=np.mean(c[es]);mn=min(c[es]);mx=max(c[es])
    ck('signed level raw face reconstruction',min(c)+sum(width*all(c[es]>r) for r,width in levels)+(bar-mn),bar)
    ck('mixed-face level length',sum(width*(any(c[es]>r) and not all(c[es]>r)) for r,width in levels),mx-mn)
for p,(es,signs) in enumerate(faces):
    ck('four distinct-edge derivative with inverse signs',-np.trace(prod([s*T[0] for s in signs])), -.125)
    for e in es:
        for q in inc[e]:
            if q!=p:assert not (set(es)-{e})<=set(faces[q][0])
rows=[]
for es,signs in faces:
    for e in es:
        row=np.zeros(len(edges));row[e]=1
        for f in es:row[f]-=.25
        rows.append(row)
ck('geometric kernel consists of constants',np.linalg.matrix_rank(np.asarray(rows),tol=1e-9),len(edges)-1)
result=dict(all_passed=True,checks=len(checks),scope='Original SU2 configurations and cubic incidence test operator algebra, ordered traversals and coefficients; independent finite tensor Hamiltonians test spectral identities. None is a sample of the Yang–Mills vacuum or evidence of physical annulus positivity.',max_absolute_error=max(x['max_error'] for x in checks),details=checks)
(O/'SCALAR_ENERGY_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='details'}))
