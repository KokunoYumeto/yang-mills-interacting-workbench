from pathlib import Path
import itertools,json
import numpy as np
O=Path(__file__).resolve().parent;rows=[]
def eq(name,a,b,tol=3e-11):
    a=np.asarray(a);b=np.asarray(b);err=float(np.max(np.abs(a-b)));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=bool(err<=tol*scale),error=err))
def yes(name,b):rows.append(dict(name=name,passed=bool(b)))
rng=np.random.default_rng(20261014)
for trial in range(12):
    # Conditional score algebra fixture, not a computed Yang–Mills state.
    M=rng.normal(size=(3,9));G=M@M.T;weights=np.exp(rng.normal(size=17));weights=weights/weights.sum();score=rng.normal(size=(17,9));mean=weights@score;h=score@M.T;hbar=weights@h
    gradlogrho=2*np.linalg.solve(G,hbar);sub=.5*gradlogrho@M;zeta=score-sub;tau=weights@np.sum(zeta*zeta,axis=1);center=h-hbar;Sigma=center.T@(weights[:,None]*center)
    eq(f'full score square identity{trial}',tau,weights@np.sum(score*score,axis=1)-.25*gradlogrho@G@gradlogrho)
    projection=score@M.T@np.linalg.inv(G)@M;perp=score-projection
    eq(f'trace plus perpendicular contribution{trial}',tau,np.trace(np.linalg.solve(G,Sigma))+weights@np.sum(perp*perp,axis=1))
    yes(f'full conditional covariance bound{trial}',np.linalg.eigvalsh(tau*G-Sigma).min()>-1e-10)
    v=rng.normal(size=3)+1j*rng.normal(size=3);kappa=.8
    residual=4*kappa*kappa*(weights@np.abs(center@v)**2)
    eq(f'complete complex residual norm{trial}',residual,4*kappa*kappa*np.vdot(v,Sigma@v))
    yes(f'complete complex residual inequality{trial}',residual<=4*kappa*kappa*tau*np.vdot(v,G@v).real+1e-10)

L=1;kappa=.8;j=1;a=1/(100*j);b=1/(kappa*a*a)
vertices=list(itertools.product(range(-L,L+1),repeat=3));edges=[]
for p in vertices:
    for axis in range(3):
        if p[axis]<L:edges.append((p,axis))
edge_index={e:i for i,e in enumerate(edges)}
def shift(p,axis):q=list(p);q[axis]+=1;return tuple(q)
faces=[]
for p in vertices:
    for i in range(3):
        for m in range(i+1,3):
            if p[i]<L and p[m]<L:
                word=[((p,i),1),((shift(p,i),m),1),((shift(p,m),i),-1),((p,m),-1)]
                faces.append((p,i,m,word))
eq('original link count N1',len(edges),3*(2*L)*(2*L+1)**2);eq('original face count M1',len(faces),3*(2*L)**2*(2*L+1));eq('original regulator coupling',b,1/(kappa*a*a))
selected=[f for f in faces if f[1:3]==(0,1) and f[0] in [(-1,0,0),(0,0,0)]];eq('exact selected face pair',len(selected),2)
outside=((0,0,0),2);incidence=sum(any(e==outside for e,sign in f[3]) for f in faces);eq('all original perpendicular incident faces',incidence,4)
for theta in [0.,.1,.7,1.4,np.pi]:
    links=[np.eye(2,dtype=complex) for _ in edges];links[edge_index[outside]]=np.diag([np.exp(-1j*theta),np.exp(1j*theta)])
    traces=[];selected_traces=[]
    for f in faces:
        prod=np.eye(2,dtype=complex)
        for e,sign in f[3]:
            matrix=links[edge_index[e]];prod=prod@(matrix if sign==1 else matrix.conj().T)
        trace=np.trace(prod).real;traces.append(trace)
        if f in selected:selected_traces.append(trace)
    eq(f'unchanged selected face traces theta{theta}',selected_traces,[2,2])
    eq(f'full remaining potential theta{theta}',2*b*len(faces)-b*sum(traces),4*b*(2-2*np.cos(theta)))
    yes(f'nonnegative original face terms theta{theta}',min(2-np.array(traces))>=-1e-13)
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),rows=rows,scope='Conditional score and full complex covariance algebra on explicit fixtures; actual original j1 link/face counts, unchanged selected holonomies and complete varying remaining Wilson potential. No actual full ground density or score is computed by these fixtures.')
(O/'FULL_MARGINAL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8');print(json.dumps(dict(all_passed=out['all_passed'],checks=len(rows),failed=[r for r in rows if not r['passed']])));assert out['all_passed']
