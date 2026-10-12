from pathlib import Path
import os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import itertools,json,math
import numpy as np
from scipy.fft import dst
W=Path(__file__).resolve().parent
rows=[]
def check(name,actual,expected,tol=2e-10):
    actual=np.asarray(actual);expected=np.asarray(expected)
    err=float(np.max(np.abs(actual-expected))) if actual.size else 0.
    scale=max(1.,float(np.max(np.abs(expected)))) if expected.size else 1.
    assert err<=tol*scale,(name,err,scale)
    rows.append(dict(name=name,max_abs_error=err,tolerance=tol*scale,passed=True))
def graph(q):
    edges=[(r,d) for d in range(3) for r in itertools.product(*[range(q) if k==d else range(1,q) for k in range(3)])]
    ix={e:i for i,e in enumerate(edges)};G=np.zeros((len(edges),len(edges)))
    for d,k in itertools.combinations(range(3),2):
        for r in itertools.product(*[range(q) if t in (d,k) else range(q+1) for t in range(3)]):
            rd=list(r);rd[d]+=1;rk=list(r);rk[k]+=1
            face=[(r,d),(tuple(rd),k),(tuple(rk),d),(r,k)]
            for e,f in itertools.combinations(face,2):
                if e in ix:G[ix[e],ix[e]]+=1
                if f in ix:G[ix[f],ix[f]]+=1
                if e in ix and f in ix:G[ix[e],ix[f]]-=1;G[ix[f],ix[e]]-=1
    return edges,G
def block(m,q):
    s=np.sin(np.pi*np.array(m)/(2*q))**2;u=np.cos(np.pi*np.array(m)/(2*q))
    D=8+4*(s.sum()-s);K=-4*np.outer(u,u);np.fill_diagonal(K,D)
    det=np.prod(D)-16*(D[0]*u[1]**2*u[2]**2+D[1]*u[0]**2*u[2]**2+D[2]*u[0]**2*u[1]**2)-128*np.prod(u*u)
    inv=np.empty((3,3))
    for d in range(3):
        k,l=[t for t in range(3) if t!=d]
        inv[d,d]=(D[k]*D[l]-16*u[k]**2*u[l]**2)/det
        for k in range(3):
            if k!=d:
                l=3-d-k;inv[d,k]=4*u[d]*u[k]*(D[l]+4*u[l]**2)/det
    return K,inv
def basis(q,edges):
    vectors=[];norms=[];blocks=[];invblocks=[]
    for m in itertools.product(range(1,q),repeat=3):
        K,H=block(m,q);blocks.append(K);invblocks.append(H)
        for d in range(3):
            vectors.append([np.prod([math.sin(math.pi*m[k]*(r[k]+(.5 if k==d else 0))/q) for k in range(3)]) if e==d else 0. for r,e in edges]);norms.append(q**3/8)
    for d in range(3):
        for m in itertools.product(*[[q] if k==d else range(1,q) for k in range(3)]):
            D=8+4*sum(math.sin(math.pi*m[k]/(2*q))**2 for k in range(3) if k!=d)
            blocks.append(np.array([[D]]));invblocks.append(np.array([[1/D]]))
            vectors.append([np.prod([math.sin(math.pi*m[k]*(r[k]+(.5 if k==d else 0))/q) for k in range(3)]) if e==d else 0. for r,e in edges]);norms.append(q**3/4)
    U=np.array(vectors).T;N=np.array(norms)
    K=np.zeros((len(edges),len(edges)));H=K.copy();i=0
    for k,h in zip(blocks,invblocks):
        t=len(k);K[i:i+t,i:i+t]=k;H[i:i+t,i:i+t]=h;i+=t
    return U,N,K,H
rng=np.random.default_rng(12102026)
for q in range(2,7):
    edges,G=graph(q);U,N,K,Hi=basis(q,edges);n=len(edges)
    check(f'q{q}:full-dimension',n,3*q*(q-1)**2)
    check(f'q{q}:raw-mode-norms',U.T@U,np.diag(N))
    check(f'q{q}:full-original-operator',G@U,U@K)
    check(f'q{q}:block-inverse',K@Hi,np.eye(n))
    H=(U@Hi/N)@U.T
    check(f'q{q}:full-Green-inverse',G@H,np.eye(n))
    check(f'q{q}:sharp-minimum',np.linalg.eigvalsh(G)[0],16*np.sin(np.pi/(2*q))**2)
    for trial in range(5):
        keep=np.sort(rng.choice(n,size=max(1,n//2),replace=False));omit=np.setdiff1d(np.arange(n),keep)
        Hkk=H[np.ix_(omit,omit)];Hkj=H[np.ix_(omit,keep)]
        invJ=H[np.ix_(keep,keep)]-Hkj.T@np.linalg.solve(Hkk,Hkj)
        check(f'q{q}:retained-inverse-{trial}',G[np.ix_(keep,keep)]@invJ,np.eye(len(keep)))
        b=rng.normal(size=n)+1j*rng.normal(size=n);err=b[omit]+np.linalg.solve(Hkk,Hkj@b[keep])
        check(f'q{q}:full-cutoff-defect-{trial}',np.vdot(b,H@b)-np.vdot(b[keep],invJ@b[keep]),np.vdot(err,Hkk@err))
edges,G=graph(3);H=np.linalg.inv(G);n=len(edges)
for trial in range(24):
    V=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));Z=V.conj().T@V/n+np.eye(n)
    B=rng.normal(size=(n,4))+1j*rng.normal(size=(n,4));B=np.column_stack([B,B[:,0]+2j*B[:,1]])
    k=rng.normal(size=n)+1j*rng.normal(size=n);c=np.linalg.solve(Z,k)
    eig,Q=np.linalg.eigh(G);Gs=(Q*np.sqrt(eig))@Q.T;Gi=(Q/np.sqrt(eig))@Q.T
    T=Gi@Z@B;w=Gs@c;D=T.conj().T@T;r=B.conj().T@k;Dp=np.linalg.pinv(D,rcond=1e-12)
    res=w-T@Dp@r
    check(f'noncommuting:{trial}:range',D@Dp@r,r,1e-9)
    check(f'noncommuting:{trial}:orthogonal',T.conj().T@res,np.zeros(5),1e-9)
    check(f'noncommuting:{trial}:complete-projection',np.vdot(c,G@c),np.vdot(r,Dp@r)+np.vdot(res,res),1e-9)
    M=Z@H@Z;h=np.linalg.solve(M,k)
    check(f'noncommuting:{trial}:full-dual',2*np.real(np.vdot(h,k))-np.vdot(h,M@h),np.vdot(c,G@c),1e-9)
    assert np.linalg.norm(Z@G-G@Z)>1.
    Qm=V.conj().T@V;Nm=B@B.conj().T;Z0=Z
    Y=[Z0@B,2*Qm@B,Nm@B]
    for z in [.013,.27,1.41]:
        Zz=Z0+2*z*Qm+z*z*Nm
        nine=sum(z**(p+q)*Y[p].conj().T@H@Y[q] for p in range(3) for q in range(3))
        check(f'noncommuting:{trial}:nine-terms:{z}',nine,B.conj().T@Zz@H@Zz@B,2e-9)
def spectral_form(q,arrays):
    hats=[]
    for d,arr in enumerate(arrays):
        v=arr.copy()
        for k in range(3):v=dst(v,type=2 if k==d else 1,axis=k)
        v/=q**3
        sl=[slice(None)]*3;sl[d]=-1;v[tuple(sl)]/=2
        hats.append(v)
    mm=np.meshgrid(*[np.arange(1,q)]*3,indexing='ij')
    s=np.sin(np.pi*np.stack(mm,-1)/(2*q))**2;u=np.cos(np.pi*np.stack(mm,-1)/(2*q))
    D=8+4*(s.sum(-1)[...,None]-s)
    K=-4*u[..., :,None]*u[...,None,:]
    for d in range(3):K[...,d,d]=D[...,d]
    v=np.stack([h[tuple(slice(0,q-1) for _ in range(3))] for h in hats],-1)
    common=(q**3/8)*np.sum(v*np.linalg.solve(K,v[...,None])[...,0])
    boundary=0.
    for d,h in enumerate(hats):
        sl=[slice(None)]*3;sl[d]=-1;vb=h[tuple(sl)]
        ks=[k for k in range(3) if k!=d];x,y=np.meshgrid(np.arange(1,q),np.arange(1,q),indexing='ij')
        den=8+4*(np.sin(np.pi*x/(2*q))**2+np.sin(np.pi*y/(2*q))**2)
        boundary+=(q**3/4)*np.sum(vb*vb/den)
    return float(common+boundary),float(boundary)
for q in [2,3,4]:
    edges,G=graph(q);arrays=[rng.normal(size=tuple(q if k==d else q-1 for k in range(3))) for d in range(3)]
    b=np.concatenate([x.ravel() for x in arrays]);sf,_=spectral_form(q,arrays)
    check(f'FFT-original-norms:q{q}',sf,np.vdot(b,np.linalg.solve(G,b)))
R=.04;kappa=1.;diag=[]
def phi(coords):
    out=np.ones_like(coords[0],dtype=float)
    for x in coords:out*=np.where((x>=0)&(x<=R),np.sin(np.pi*x/R),0)
    return out
for j in [1,2,3,4,6,8,12]:
    a=1/(100*j);q=math.ceil(R/a)+3;arr=[];traceless=[]
    for d in range(3):
        rr=np.meshgrid(*[np.arange(q) if k==d else np.arange(1,q) for k in range(3)],indexing='ij')
        coords=[a*(rr[k]-1+(.5 if k==d else 0)) for k in range(3)]
        ss=np.zeros_like(coords[0],dtype=float);tt=ss.copy()
        for k in range(3):
            if k==d:continue
            # Original test triple (phi,phi,phi), or (phi,-phi,0).
            pair=tuple(sorted((d,k)));weight={(0,1):1,(0,2):-1,(1,2):0}[pair]
            for sign in [-1,1]:
                xp=[x.copy() for x in coords];xp[k]+=sign*a/2
                ss+=phi(xp);tt+=weight*phi(xp)
        arr.append(-3*a**3/8*(2-kappa*a)*ss)
        traceless.append(-3*a**3/8*(2-kappa*a)*tt)
    val,bound=spectral_form(q,arr);tv,_=spectral_form(q,traceless)
    target=27*R**5/(32*np.pi**2)
    diag.append(dict(j=j,a=a,q=q,common_source_Green_over_a=val/a,target=target,ratio=val/a/target,traceless_over_a_over_target=tv/a/target,boundary_contribution_over_a=bound/a))
assert abs(diag[-1]['ratio']-1)<abs(diag[0]['ratio']-1)
assert diag[-1]['traceless_over_a_over_target']<diag[0]['traceless_over_a_over_target']
out=dict(all_passed=True,checks=len(rows),checks_detail=rows,diagnostic_source_description='Explicit original-grid face means 2-kappa*a with kappa=1; test products on R=.04 cube. These are diagnostic arrays, not sampled Yang–Mills vacuum data. Original a_j, fitting floor and ceiling retained.',original_path_diagnostics=diag)
(W/'GRAPH_GREEN_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(all_passed=True,checks=len(rows),original_path_diagnostics=diag)))
