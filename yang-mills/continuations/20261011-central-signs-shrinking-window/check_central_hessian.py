from pathlib import Path
import itertools,json,numpy as np
O=Path(__file__).resolve().parent;rows=[]
def ck(name,a,b,tol=1e-8):
    err=float(np.max(abs(np.asarray(a)-np.asarray(b))))
    assert err<=tol*max(1,float(np.max(abs(np.asarray(b))))),(name,err)
    rows.append(dict(name=name,error=err))
j=1;L=j**4;n=2*L
vertices=list(itertools.product(range(n+1),repeat=3));vi={v:i for i,v in enumerate(vertices)}
edges=[(v,d) for v in vertices for d in range(3) if v[d]<n];ei={e:i for i,e in enumerate(edges)}
faces=[(v,d,k) for v in vertices for d in range(3) for k in range(d+1,3) if v[d]<n and v[k]<n];pi={p:i for i,p in enumerate(faces)}
def step(v,d):w=list(v);w[d]+=1;return tuple(w)
N=len(edges);M=len(faces);V=len(vertices)
D=np.zeros((N,V),int);R=np.zeros((N,M),int);T=np.zeros((N,V),int);F=np.zeros((M,N),int)
def path(v):
    cur=(0,0,0);word=[]
    for d in range(3):
        for k in range(v[d]):word.append(ei[cur,d]);cur=step(cur,d)
    assert cur==v
    return word
for e,(v,d) in enumerate(edges):D[e,vi[v]]=1;D[e,vi[step(v,d)]]=-1
for p,(v,d,k) in enumerate(faces):
    for vv,dd,sg in [(v,d,1),(step(v,d),k,1),(step(v,k),d,-1),(v,k,-1)]:R[ei[vv,dd],p]=sg
for v in vertices:
    for e in path(v):T[e,vi[v]]+=1
for e,(v,d) in enumerate(edges):
    word=[k for k in range(3) for unused in range(v[k])]+[d]
    while any(word[i]>word[i+1] for i in range(len(word)-1)):
        i=next(i for i in range(len(word)-1) if word[i]>word[i+1]);base=[0,0,0]
        for k in word[:i]:base[k]+=1
        high,low=word[i:i+2];F[pi[tuple(base),low,high],e]-=1
        word[i],word[i+1]=word[i+1],word[i]
ck('all original boundary-of-boundary signs',D.T@R,np.zeros((V,M)),0)
ck('complete integer monotone filling',R@F,np.eye(N,dtype=int)+T@D.T,0)
tree=set(e for v in vertices for e in path(v));chords=[e for e in range(N) if e not in tree]
C=(np.eye(N,dtype=int)+T@D.T)[:,chords];rank=N-V+1
assert len(tree)==V-1 and len(chords)==rank
ck('all original chord coordinates retained',C[chords],np.eye(rank),0)
ck('all full cycle divergences',D.T@C,np.zeros((V,rank)),0)
Dt=D[:,1:];Pc=np.eye(N)-Dt@np.linalg.solve(Dt.T@Dt,Dt.T)
ck('full cycle projection reconstructed',C@np.linalg.solve(C.T@C,C.T),Pc)
pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
basis=np.array([-.5j*s for s in pauli]);rng=np.random.default_rng(141034)
words=[]
for e in chords:
    v,d=edges[e];words.append([(k,1) for k in path(v)]+[(e,1)]+[(k,-1) for k in reversed(path(step(v,d)))])
def dsecond(word,X):
    first=np.zeros((2,2),complex);second=np.zeros((2,2),complex)
    for e,sg in word:
        term=sg*X[e];second=second+2*first@term+term@term;first=first+term
    return -np.trace(second)
for trial in range(4):
    A=rng.normal(size=(rank,rank));A=(A+A.T)/2
    K=C@A@C.T;S=F@K@F.T;G=R.T@R
    ck('complete Hessian gauge constraints',K@D,0)
    ck('complete Hessian face reconstruction',R@S@R.T,K)
    B=rng.normal(size=(rank,rank));B=(B+B.T)/2;K2=C@B@C.T;S2=F@K2@F.T
    ck('full colour and both face Gram factors',np.sum(np.kron(K,np.eye(3))*np.kron(K2,np.eye(3))),3*np.trace(S.T@G@S2@G))
    recovered=np.linalg.solve(C.T@C,C.T@K@C)@np.linalg.inv(C.T@C)
    ck('complete global realization coefficients',recovered,A)
    for sample in range(3):
        v=rng.normal(size=(N,3));X=np.einsum('ea,aij->eij',v,basis)
        singles=[dsecond(w,X) for w in words]
        got=sum(2*A[i,i]*singles[i] for i in range(rank))
        for i in range(rank):
            for k in range(i+1,rank):got+=2*A[i,k]*(dsecond(words[i]+words[k],X)-singles[i]-singles[k])
        expected=sum(v[:,alpha]@K@v[:,alpha] for alpha in range(3))
        ck('complete Wilson-word realization including repeated links',got,expected)
out=dict(all_passed=True,checks=len(rows),original_regulator=dict(j=j,L=L,a=1/(100*j),vertices=V,edges=N,faces=M,cycle_rank=rank),scope='Exact integer incidence and monotone face filling on the original j=1 open box; complete Hessian/colour/face maps and analytic second derivatives of complete repeated-link Wilson words. Specified arbitrary allowed Hessians, not sampled ground-state Hessians or assigned continuum limits.',details=rows)
(O/'CENTRAL_HESSIAN_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='details'}))
