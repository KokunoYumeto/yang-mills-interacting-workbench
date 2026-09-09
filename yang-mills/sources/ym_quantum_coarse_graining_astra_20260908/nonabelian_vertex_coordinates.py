"""Full original L=2 tree, cochain and first interaction coordinates."""
from pathlib import Path
from itertools import product,combinations
import json,math
import numpy as np

ROOT=Path(__file__).resolve().parent
def geometry(L=2):
    N=2*L+1
    vertices=list(product(range(-L,L+1),repeat=3))
    def shifted(n,i):
        r=list(n);r[i]+=1;return tuple(r)
    edges=[(n,i) for n in vertices for i in range(3) if n[i]<L]
    eid={e:i for i,e in enumerate(edges)}
    tree=[];paths={(-L,-L,-L):[]}
    for n in sorted(vertices,key=lambda v:sum(v)):
        if n==(-L,-L,-L):continue
        d=next(i for i in range(3) if n[i]>-L)
        parent=list(n);parent[d]-=1;parent=tuple(parent)
        e=eid[(parent,d)];tree.append(e);paths[n]=paths[parent]+[e]
    tree=set(tree);chords=[e for e in range(len(edges)) if e not in tree]
    cid={e:c for c,e in enumerate(chords)}
    T=np.zeros((len(chords),len(edges)),dtype=int)
    B=np.zeros_like(T)
    for c,e in enumerate(chords):
        n,i=edges[e];target=shifted(n,i)
        T[c,e]=1;B[c,e]=-1
        for f in paths[n]:T[c,f]+=1;B[c,f]-=1
        for f in paths[target]:T[c,f]-=1;B[c,f]-=1
    faces=[(n,i,k) for n in vertices for i in range(3) for k in range(i+1,3) if n[i]<L and n[k]<L]
    words=[[(eid[(n,i)],1),(eid[(shifted(n,i),k)],1),
            (eid[(shifted(n,k),i)],-1),(eid[(n,k)],-1)] for n,i,k in faces]
    V=[];sig=[]
    for jj in product(range(N),repeat=3):
        active=[i for i in range(3) if jj[i]>0]
        if len(active)<2:continue
        sv=2*np.sin(np.pi*np.array(jj)/(2*N))
        _,_,vt=np.linalg.svd(sv[active].reshape(1,-1),full_matrices=True)
        for base in vt[1:]:
            eps=np.zeros(3);eps[active]=base;col=[]
            for n,i in edges:
                if i not in active:col.append(0.);continue
                val=-math.sqrt(2/N)*math.sin(math.pi*jj[i]*(n[i]+L+1)/N)*eps[i]
                for d in range(3):
                    if d!=i:val*=math.sqrt((2-(jj[d]==0))/N)*math.cos(math.pi*jj[d]*(n[d]+L+.5)/N)
                col.append(val)
            V.append(col);sig.append(float(np.linalg.norm(sv)))
    V=np.array(V).T;sig=np.array(sig)
    return dict(L=L,N=N,vertices=vertices,edges=edges,chords=chords,cid=cid,T=T,B=B,faces=faces,words=words,V=V,sig=sig)

def evaluate_triple(data,indices):
    V=data['V'];sig=data['sig'];chords=data['chords'];B=data['B']
    VI=V[np.array(chords)[list(indices)],:]
    KK=(VI*sig)@VI.T
    QQ=((B[list(indices),:]@V)*sig)@VI.T
    kin=sum(np.dot(QQ[b],np.cross(np.eye(3)[b],KK[b])) for b in range(3))/8
    selected={chords[c]:np.eye(3)[b] for b,c in enumerate(indices)}
    mag=0.
    for word in data['words']:
        zz=[sign*selected.get(e,np.zeros(3)) for e,sign in word]
        A=sum(zz)
        BB=sum((np.cross(zz[l],zz[m])/2 for l in range(4) for m in range(l+1,4)),np.zeros(3))
        mag+=np.dot(A,BB)/4
    return float(kin),float(mag),KK,QQ

if __name__=='__main__':
    d=geometry();candidates=[]
    for face,word in zip(d['faces'],d['words']):
        cs=[d['cid'][e] for e,_ in word if e in d['cid']]
        if len(cs)>=3:
            for triple in combinations(cs,3):
                kin,mag,_,_=evaluate_triple(d,triple)
                candidates.append((abs(kin+mag),triple,kin,mag,face))
    best=max(candidates)
    kin,mag,K,Q=evaluate_triple(d,best[1])
    out=dict(scope='Exploration only; exact interval certificate still required.',
             chord_indices=best[1],original_edges=[d['edges'][d['chords'][c]] for c in best[1]],
             face=best[4],a_times_cubic_kinetic=kin,a_times_cubic_magnetic=mag,
             a_times_full_cubic=kin+mag,K=K.tolist(),Q=Q.tolist(),candidates=len(candidates))
    (ROOT/'NONABELIAN_VERTEX_EXPLORATION.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))
