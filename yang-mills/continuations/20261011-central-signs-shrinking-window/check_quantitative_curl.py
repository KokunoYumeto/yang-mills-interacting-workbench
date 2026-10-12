"""Original SU(2) derivative and lattice diagnostics; no vacuum samples."""
from pathlib import Path
import itertools,json,math
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
O=Path(__file__).resolve().parent
rng=np.random.default_rng(61012011);checks=[]
def eq(name,a,b,tol=2e-10):
    err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    scale=max(1.,float(np.max(np.abs(a))),float(np.max(np.abs(b))))
    checks.append(dict(name=name,passed=err<=tol*scale,absolute_error=err))
    assert checks[-1]['passed'],checks[-1]
def le(name,a,b):
    checks.append(dict(name=name,passed=bool(a<=b+2e-10*max(1.,abs(a),abs(b))),lhs=float(a),rhs=float(b)))
    assert checks[-1]['passed'],checks[-1]
I2=np.eye(2,dtype=complex)
pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],complex)
T=-.5j*pauli
def prod(xs):
    z=I2.copy()
    for x in xs:z=z@x
    return z
def derivtrace(W,edits):
    return -np.trace(prod([edits.get(i,W[i]) for i in range(4)])).real
# Arbitrary original ordered faces: both inverse factors are differentiated.
for sample in range(70):
    raw=rng.normal(size=(4,4));raw=raw/np.linalg.norm(raw,axis=1)[:,None]
    U=[r[0]*I2-1j*np.einsum('a,aij->ij',r[1:],pauli) for r in raw]
    W=[U[0],U[1],U[2].conj().T,U[3].conj().T]
    Up=prod(W);xi=float(np.trace(Up).real/2);D=2-2*xi
    dW=[[T[a]@W[i] if i<2 else -W[i]@T[a] for a in range(3)] for i in range(4)]
    grad=np.array([[derivtrace(W,{i:dW[i][a]}) for a in range(3)] for i in range(4)])
    for i in range(4):eq(f'face gradient norm {sample}/{i}',grad[i]@grad[i],D-D*D/4)
    H={}
    for i,j in itertools.combinations(range(4),2):
        M=np.array([[derivtrace(W,{i:dW[i][a],j:dW[j][b]}) for b in range(3)] for a in range(3)])
        H[i,j]=M;H[j,i]=M.T
        eq(f'mixed HS {sample}/{i}/{j}',np.sum(M*M),.75-D/4+D*D/16)
        eq(f'mixed singular values {sample}/{i}/{j}',np.linalg.svd(M,compute_uv=False),[.5,.5,abs(xi)/2])
        lapgrad=np.zeros(3)
        for a in range(3):
            for b in range(3):
                d2=(T[b]@T[b]@W[j] if j<2 else W[j]@T[b]@T[b])
                lapgrad[a]+=derivtrace(W,{i:dW[i][a],j:d2})
        eq(f'full third Casimir derivative {sample}/{i}/{j}',lapgrad,-.75*grad[i])
    c=rng.normal(size=4)+1j*rng.normal(size=4);g=rng.normal(size=(4,3))
    curl2=sum(abs(c[i]-c[j])**2*np.sum(H[i,j]**2) for i,j in itertools.combinations(range(4),2))
    graph=sum(abs(c[i]-c[j])**2 for i,j in itertools.combinations(range(4),2))
    eq(f'exact face curl norm {sample}',curl2,(.75-D/4+D*D/16)*graph)
    eq(f'complete K4 identity {sample}',graph,2*abs(c[0]-c[2])**2+2*abs(c[1]-c[3])**2+abs(c[0]+c[2]-c[1]-c[3])**2)
    delta=np.array([.75*sum(c[i]-c[j] for j in range(4) if j!=i)*grad[i] for i in range(4)])
    eq(f'original unweighted codifferential {sample}',delta,3*(c-c.mean())[:,None]*grad)
    contract=np.array([sum((c[i]-c[j])*(H[i,j]@g[j]) for j in range(4) if j!=i) for i in range(4)])
    driftbound=3*sum(abs(c[i]-c[j])**2*(g[i]@g[i]+g[j]@g[j]) for i,j in itertools.combinations(range(4),2))
    le(f'full drift point bound {sample}',float(np.sum(abs(contract)**2)),driftbound)
def lattice(q):
    edges=[(tuple(r),d) for d in range(3) for r in itertools.product(range(q+1),repeat=3) if r[d]<q]
    faces=[]
    for d,k in itertools.combinations(range(3),2):
        for r in itertools.product(range(q+1),repeat=3):
            if r[d]==q or r[k]==q:continue
            rd=list(r);rd[d]+=1;rk=list(r);rk[k]+=1
            faces.append([(r,d),(tuple(rd),k),(tuple(rk),d),(r,k)])
    inside=[e for e in edges if all(0<e[0][k]<q for k in range(3) if k!=e[1])]
    return edges,faces,inside
graph_data=[]
for q in range(2,9):
    edges,faces,inside=lattice(q);ids={e:i for i,e in enumerate(inside)}
    counts={e:0 for e in edges};paircounts={};rr=[];cc=[];vv=[]
    for face in faces:
        for e in face:counts[e]+=1
        for e,f in itertools.combinations(face,2):
            key=tuple(sorted([e,f]));paircounts[key]=paircounts.get(key,0)+1
            if e in ids:rr.append(ids[e]);cc.append(ids[e]);vv.append(1.)
            if f in ids:rr.append(ids[f]);cc.append(ids[f]);vv.append(1.)
            if e in ids and f in ids:
                rr.extend([ids[e],ids[f]]);cc.extend([ids[f],ids[e]]);vv.extend([-1.,-1.])
    G=coo_matrix((vv,(rr,cc)),shape=(len(inside),len(inside))).tocsr()
    le(f'max original faces per edge q{q}',max(counts.values()),4)
    eq(f'unique coface pairs q{q}',max(paircounts.values()),1)
    neighbors={e:set() for e in edges}
    for e,f in paircounts:neighbors[e].add(f);neighbors[f].add(e)
    le(f'max original coface neighbors q{q}',max(map(len,neighbors.values())),12)
    eq(f'original strict-inside count q{q}',len(inside),3*q*(q-1)**2)
    mode=np.array([math.sin(math.pi*(r[d]+.5)/q)*math.prod(math.sin(math.pi*r[k]/q) for k in range(3) if k!=d) for r,d in inside])
    lam=16*math.sin(math.pi/(2*q))**2
    eq(f'exact attaining eigenvector q{q}',G@mode,lam*mode)
    eigen=float(eigsh(G,k=1,which='SA',return_eigenvectors=False,tol=1e-12)[0])
    eq(f'exact least patch eigenvalue q{q}',eigen,lam)
    graph_data.append(dict(q=q,edges=len(inside),lambda_formula=lam,lambda_numeric=eigen))
    values=dict(zip(inside,mode))
    for idx,face in enumerate(faces):
        c=np.array([values.get(e,0) for e in face])
        eq(f'vanishing face-sum square q{q}/{idx}',c[0]+c[2],c[1]+c[3])
    for trial in range(10):
        c=rng.normal(size=len(inside))+1j*rng.normal(size=len(inside))
        le(f'complete graph floor q{q}/{trial}',lam*np.vdot(c,c).real,np.vdot(c,G@c).real)
        sums=0.;par=0.;full=0.
        for face in faces:
            x=np.array([c[ids[e]] if e in ids else 0 for e in face])
            sums+=abs(x[0]+x[2]-x[1]-x[3])**2
            par+=abs(x[0]-x[2])**2+abs(x[1]-x[3])**2
            full+=sum(abs(x[i]-x[j])**2 for i,j in itertools.combinations(range(4),2))
        eq(f'full boundary matrix q{q}/{trial}',full,np.vdot(c,G@c).real)
        eq(f'complete graph decomposition q{q}/{trial}',full,2*par+sums)
for trial in range(100):
    t=10**rng.uniform(-5,2)
    # Discrete laws here check the moment inequality; they are not vacuum samples.
    vals=rng.uniform(0,min(t,4),30);weights=rng.uniform(size=30);weights/=weights.sum()
    d=weights@vals;v=weights@(vals-vals*vals/4)
    sig=1-max(2-t,0)**2/4;rho=(3-sig)/4
    le(f'full face moment ceiling {trial}',v,sig)
    le(f'full Hessian moment floor {trial}',rho,.75-v/4)
    kap=10**rng.uniform(-1,1);a=10**rng.uniform(-7,-2);C=rng.uniform(kap,1e3);b=1/(kap*a*a)
    sig=1-max(2-C*a,0)**2/4;rho=(3-sig)/4
    A=rho*rho/(9*kap*kap*(math.sqrt(sig)+2*math.sqrt(2/(kap*a)))**2)
    eq(f'exact original b and a factors {trial}',a**4*b*b*rho*rho/(9*(math.sqrt(sig)+2*math.sqrt(2/(kap*a)))**2),A)
# Original fixed test f12=f13=f23=product of4t(1-t) on [0,1]^3.
kap=1.;R=1.;Mf=1.;Jt=12*(8/15)**3
LR=9*kap*R**3+24*R**2
KR=(LR+math.sqrt(LR*LR-81*kap*kap*R**6/4))/2
C=max(kap,64*Mf*Mf*KR/Jt)
def const(j):
    a=1/(100*j);q=math.ceil(R/a)+3;t=C*a
    sig=1-max(2-t,0)**2/4;rho=(3-sig)/4
    A=rho*rho/(9*kap*kap*(math.sqrt(sig)+2*math.sqrt(2/(kap*a)))**2)
    return a,q,A,16*A*math.sin(math.pi/(2*q))**2
for j in [1e5,1e6,1e7]:
    a,q,A,m=const(j)
    le(f'coefficient asymptotic error j{j}',abs(A/a-1/(128*kap)),.1/j)
    le(f'full removed floor asymptotic error j{j}',abs(m/a**3-math.pi**2/(32*kap*R*R)),6/j)
# Reproducible geometry: full face-pair mechanism and a labelled slice of the attaining mode.
plt.rcParams.update({'font.size':11,'axes.titlesize':13})
fig,axes=plt.subplots(1,2,figsize=(13,5.8),gridspec_kw={'width_ratios':[1,1.2]})
ax=axes[0];nodes=np.array([[.5,0],[1,.5],[.5,1],[0,.5]])
ax.plot([0,1,1,0,0],[0,0,1,1,0],color='#667085',lw=1)
for i,j in itertools.combinations(range(4),2):
    opposite=(i,j) in [(0,2),(1,3)]
    ax.plot(nodes[[i,j],0],nodes[[i,j],1],color='#175cd3' if opposite else '#aab5c3',lw=3 if opposite else 1.4)
for i,(x,y) in enumerate(nodes):
    ax.scatter(x,y,s=130,color='#101828',zorder=3)
    dx,dy=[(0,-.1),(.13,0),(0,.12),(-.13,0)][i]
    ax.text(x+dx,y+dy,rf'$c_{i+1}$',ha='center',va='center',fontsize=14)
ax.text(.5,-.24,r'$\mathcal{G}_p=2|c_1-c_3|^2+2|c_2-c_4|^2$'+'\n'+r'$+\,|c_1+c_3-c_2-c_4|^2$',ha='center',va='top',fontsize=12)
ax.set(xlim=(-.3,1.3),ylim=(-.55,1.3),aspect='equal');ax.axis('off')
ax.set_title('All six original face pairs\nQCF10: two parallel terms, one full remainder')
ax=axes[1];q=6;z=3;segments=[];values=[]
for d in [0,1]:
    for x in range(q+1):
        for y in range(q+1):
            r=(x,y,z)
            if r[d]>=q:continue
            end=[x,y];end[d]+=1
            segments.append([(x,y),end])
            good=all(0<r[k]<q for k in range(3) if k!=d)
            values.append(math.sin(math.pi*(r[d]+.5)/q)*math.prod(math.sin(math.pi*r[k]/q) for k in range(3) if k!=d) if good else 0)
lc=LineCollection(segments,array=np.array(values),cmap='viridis',linewidths=3,clim=(0,1))
ax.add_collection(lc);fig.colorbar(lc,ax=ax,pad=.02,label='Original coefficient value')
ax.set(xlim=(-.25,6.25),ylim=(-.25,6.25),aspect='equal',xlabel=r'$r_1$',ylabel=r'$r_2$')
ax.set_title(r'Attaining mode: $q=6$, slice $r_3=3$'+'\n'+r'$c_1,c_2$ shown; all three components in QCF13')
fig.text(.5,.015,'The thin square is the original face; the six internal connections are coefficient pairs. The right panel is an identified slice, not the whole field.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.06,1,1))
for ext in ['png','svg']:fig.savefig(O/('FORCE_CURL_PATCH_GEOMETRY.'+ext),dpi=180)
plt.close(fig)
js=np.unique(np.geomspace(1,1e6,320).astype(int));cs=[const(int(j)) for j in js]
fig,axes=plt.subplots(1,2,figsize=(12,4.7))
axes[0].semilogx(js,[A/a for a,q,A,m in cs],lw=2,label=r'$A_C(a_j)/a_j$')
axes[0].axhline(1/(128*kap),color='#b54708',ls='--',label=r'$1/(128\kappa_*)$')
axes[1].semilogx(js,[m/a**3 for a,q,A,m in cs],lw=2,label=r'$m_{C,Q_j}(a_j)/a_j^3$')
axes[1].axhline(math.pi**2/(32*kap*R*R),color='#b54708',ls='--',label=r'$\pi^2/(32\kappa_*R^2)$')
for ax in axes:
    ax.set_xlabel(r'Original regulator index $j$');ax.grid(alpha=.25);ax.legend(loc='lower right');ax.set_ylim(bottom=0)
axes[0].set_title('Proved coefficient bound, QCF14–QCF15')
axes[1].set_title('Proved full-patch floor, QCF12–QCF15')
fig.suptitle(r'Original $a_j=(100j)^{-1}$, $\kappa_*=R=1$, $q_j=\lceil R/a_j\rceil+3$',fontsize=13)
fig.text(.5,.035,r'$f_{12}=f_{13}=f_{23}=\prod_{d=1}^3 4x_d(1-x_d)$ on $[0,1]^3$, zero outside; $C=\max\{\kappa_*,64M_f^2K_R/J_t\}$.'+'\nThese curves are proved bound constants, not measured Yang–Mills eigenvalues or spectral weight.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.13,1,.95))
for ext in ['png','svg']:fig.savefig(O/('FORCE_CURL_ORIGINAL_PATH.'+ext),dpi=180)
plt.close(fig)
out=dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),scope='Exact original ordered SU(2) derivatives with inverse signs, full third Casimir derivatives, curl and codifferential identities, complete lattice boundary matrices, exact sharp patch eigenvalues and original-path bound constants. No vacuum sampling or no-gap claim.',graph_spectra=graph_data,original_test_constants=dict(kappa=kap,R=R,Mf=Mf,Jt=Jt,LR=LR,KR=KR,C=C),results=checks)
(O/'QUANTITATIVE_FORCE_CURL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='results'}))
