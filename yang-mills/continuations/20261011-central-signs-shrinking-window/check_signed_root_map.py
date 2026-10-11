from pathlib import Path
import numpy as np
import json
ROOT=Path(__file__).resolve().parent
rng=np.random.default_rng(6101107)
n=3;m=n-1
edges=[(d,i,k,l) for d in (1,2,3) for i in range(n-(d==1)) for k in range(n-(d==2)) for l in range(n-(d==3))]
pos={e:r for r,e in enumerate(edges)}
sigma=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])]
T=[-1j*x/2 for x in sigma]
I=np.eye(2,dtype=complex)
def path(v):
    i,k,l=v
    return [pos[3,0,0,r] for r in range(l)]+[pos[2,0,r,l] for r in range(k)]+[pos[1,r,k,l] for r in range(i)]
paths={v:path(v) for v in np.ndindex(n,n,n)}
tree=set(sum(paths.values(),[]));chords=[r for r in range(len(edges)) if r not in tree]
def endpoint(e):
    d,i,k,l=e;z=[i,k,l];z[d-1]+=1;return tuple(z)
def coordinates(U):
    roots={}
    for v,word in paths.items():
        t=I.copy()
        for e in word:t=t@U[e]
        roots[v]=t
    Z=[roots[edges[e][1:]]@U[e]@roots[endpoint(edges[e])].conj().T for e in chords]
    return roots,Z
weights=rng.normal(size=len(chords))
def scalar(Z):
    return sum(weights[c]*np.trace(Z[c]).real+.07*np.trace(Z[c]@Z[(c+1)%len(Z)]).real for c in range(len(Z)))
U=[]
for e in edges:
    x=rng.normal(size=4);x/=np.linalg.norm(x)
    U.append(x[0]*I+2*sum(x[a+1]*T[a] for a in range(3)))
roots,Z=coordinates(U);eps=2e-6
rot=[[np.cos(eps/2)*I+sign*2*np.sin(eps/2)*T[a] for sign in [1,-1]] for a in range(3)]
j=np.zeros((len(chords),3));g=np.zeros((len(edges),3))
for c in range(len(chords)):
    for a in range(3):
        vals=[]
        for r in rot[a]:
            Z1=list(Z);Z1[c]=r@Z[c];vals.append(scalar(Z1))
        j[c,a]=(vals[0]-vals[1])/(2*eps)
for e in range(len(edges)):
    t=roots[edges[e][1:]]
    for a in range(3):
        vals=[]
        for r in rot[a]:
            U1=list(U);U1[e]=t.conj().T@r@t@U[e]
            vals.append(scalar(coordinates(U1)[1]))
        g[e,a]=(vals[0]-vals[1])/(2*eps)
Ad=[]
for z in Z:
    Ad.append(np.array([[-2*np.trace(T[a]@z@T[b]@z.conj().T).real for b in range(3)] for a in range(3)]))
pred=np.zeros_like(g)
for c,e in enumerate(chords):pred[e]=j[c]
for f in tree:
    for c,e in enumerate(chords):
        pred[f]+=(f in paths[edges[e][1:]])*j[c]-(f in paths[endpoint(edges[e])])*(Ad[c].T@j[c])
v=np.sqrt(2/n)*np.cos(np.pi*(np.arange(n)+.5)/n);w=-np.sqrt(2/n)*np.sin(np.pi*(np.arange(m)+1)/n)
V=np.array([0 if d==1 else w[k]*v[l]/np.sqrt(2*n) if d==2 else -v[k]*w[l]/np.sqrt(2*n) for d,i,k,l in edges])
soft=np.zeros(3)
for c,e in enumerate(chords):
    ps=sum(V[f] for f in paths[edges[e][1:]]);pt=sum(V[f] for f in paths[endpoint(edges[e])])
    soft+=(V[e]+ps)*j[c]-pt*Ad[c].T@j[c]
gauss=sum((np.eye(3)-Ad[c].T)@j[c] for c in range(len(chords)))
result={'n':n,'original_edges':len(edges),'chords':len(chords),'root_score_map_max_error':float(np.max(np.abs(g-pred))),'soft_score_map_max_error':float(np.max(np.abs(V@g-soft))),'root_Gauss_error':float(np.max(np.abs(gauss))),'finite_difference_step':eps,'test_function':'Explicit globally conjugation-invariant trace polynomial, not a model for the vacuum.'}
assert max(result[k] for k in ['root_score_map_max_error','soft_score_map_max_error','root_Gauss_error'])<1e-7
(ROOT/'SIGNED_ROOT_MAP_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps(result,indent=2))
