"""Diagnostics of original SU(2) paths and metrics, exact Haar integrals and fiber projection identities. No original full-vacuum samples."""
from pathlib import Path
import itertools,json,math
import numpy as np
from scipy.special import beta,roots_jacobi
from scipy.linalg import eigh_tridiagonal
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent;rows=[]
def check(name,error,tol=2e-8):
    error=float(error);assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
I=np.eye(2,dtype=complex);Z=np.zeros((2,2),complex)
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
T=[-.5j*s for s in sig];rng=np.random.default_rng(20261012001)
def prod(fs):
    p=I.copy()
    for u in fs:p=p@u
    return p
def graph(q):
    edges=[(z,d) for z in itertools.product(range(q+1),repeat=3) for d in range(3) if z[d]<q]
    idx={e:i for i,e in enumerate(edges)};faces=[]
    for z in itertools.product(range(q+1),repeat=3):
        for d,k in itertools.combinations(range(3),2):
            if z[d]>=q or z[k]>=q:continue
            zd=list(z);zk=list(z);zd[d]+=1;zk[k]+=1
            faces.append([(idx[(z,d)],1),(idx[(tuple(zd),k)],1),(idx[(tuple(zk),d)],-1),(idx[(z,k)],-1)])
    return edges,faces
def invword(word):return [(e,-s) for e,s in reversed(word)]
def word(word,U):return prod([U[e] if s==1 else U[e].conj().T for e,s in word])
def Bword(face,e):
    i=next(i for i,(ee,s) in enumerate(face) if ee==e);sgn=face[i][1]
    p=face[i+1:]+face[:i]
    return p if sgn==1 else invword(p)
edges,faces=graph(2)
stars=[[p for p,f in enumerate(faces) if e in [ee for ee,s in f]] for e in range(len(edges))]
for e,star in enumerate(stars):
    paths=[Bword(faces[p],e) for p in star]
    assert len(star) in [2,3,4]
    assert len(set(ee for w in paths for ee,s in w))==3*len(star)
    for kind in ['zero','aligned']:
        U=[I.copy() for _ in edges];m=len(star)
        for k,path in enumerate(paths):
            target=np.diag([np.exp(2j*np.pi*k/m),np.exp(-2j*np.pi*k/m)]) if kind=='zero' else I
            ee,s=path[0];U[ee]=target if s==1 else target.conj().T
        S=sum(word(path,U) for path in paths)
        check(f'edge{e}: actual {kind} surrounding links',np.linalg.norm(S-(Z if kind=='zero' else m*I)))
for trial in range(8):
    U=[]
    for _ in edges:
        q=rng.normal(size=4);q/=np.linalg.norm(q)
        U.append(q[0]*I+1j*sum(q[k+1]*sig[k] for k in range(3)))
    D=[];grad=[]
    for face in faces:
        fs=[U[e] if s==1 else U[e].conj().T for e,s in face];g=np.zeros((len(edges),3))
        for i,(e,s) in enumerate(face):
            for k,t in enumerate(T):
                dfs=fs.copy();dfs[i]=t@U[e] if s==1 else -U[e].conj().T@t
                g[e,k]=-np.trace(prod(dfs)).real
        D.append(2-np.trace(prod(fs)).real);grad.append(g)
    D=np.array(D);grad=np.array(grad);f=rng.normal(size=len(faces));source=0.
    for e,star in enumerate(stars):
        m=len(star);bs=[word(Bword(faces[p],e),U) for p in star];S=sum(bs)
        rho2=np.trace(S.conj().T@S).real/2;rho=math.sqrt(max(rho2,0))
        glued=[np.trace(bs[p]@bs[q].conj().T).real for p,q in itertools.combinations(range(m),2)]
        check(f'path{trial},{e}: full six-edge loop sum',rho2-m-sum(glued))
        check(f'path{trial},{e}: full surrounding deficit',m*m-rho2-sum(2-v for v in glued))
        check(f'path{trial},{e}: original star potential',sum(D[star])-2*m+np.trace(U[e]@S).real)
        check(f'path{trial},{e}: matrix modulus',np.linalg.norm(S.conj().T@S-rho2*I))
        alpha=np.zeros((len(edges),3))
        for p in star:
            for ee,s in faces[p]:alpha[ee]+=(.75 if ee==e else -.25)*grad[p,ee]
        exact=9/16*(rho2-np.trace(U[e]@S).real**2/4)+3/16*sum(D[p]-D[p]**2/4 for p in star)
        check(f'path{trial},{e}: complete original force square',np.sum(alpha*alpha)-exact)
        check(f'path{trial},{e}: force bound',max(0.,exact-(9*m+3)/16*sum(D[star])))
        meanf=np.mean(f[star]);res=sum((f[p]-meanf)*bb for p,bb in zip(star,bs))
        aligned=0 if rho<1e-14 else rho*(2-np.trace(U[e]@(S/rho)).real)
        term=2*meanf*(m-rho)+meanf*aligned-np.trace(U[e]@res).real
        source+=term/4
    check(f'path{trial}: original signed observable receiving sum',source-np.dot(f,D))
# Exact interior edge/face multiplicities, including the q=1 empty set.
for q in range(1,7):
    es,ps=graph(q);inside={i for i,(z,d) in enumerate(es) if all(0<z[k]<q for k in range(3) if k!=d)}
    check(f'cube{q}: strict transverse-edge count',len(inside)-3*q*(q-1)**2)
    for e in inside:assert sum(e in [ee for ee,s in p] for p in ps)==4
    assert max(sum(e in inside for e,s in p) for p in ps)<=4
    check(f'cube{q}: original face incidence budget',0)
# Independent Jacobi quadrature on the actual Haar class-coordinate density.
x,wt=roots_jacobi(100,.5,.5);wt=wt*2/np.pi;chi=2*x;tt=(1+x)/2
check('Haar full trace mean',np.dot(wt,chi))
check('Haar full trace square',np.dot(wt,chi*chi)-1)
check('Haar full trace cube',np.dot(wt,chi**3))
for n in range(0,25):
    norm=np.dot(wt,(4*tt)**(2*n));exact=4.**(2*n)*8/np.pi*beta(2*n+1.5,1.5)
    check(f'Haar polynomial{n}: original full norm',norm/exact-1)
    kin=0. if n==0 else np.dot(wt,n*n*4.**(2*n-1)*tt**(2*n-1)*(1-tt))/norm
    pot=np.dot(wt,4*(1-tt)*(4*tt)**(2*n))/norm
    check(f'Haar polynomial{n}: radius-two kinetic',kin-3*n*n/(4*(4*n+1)))
    check(f'Haar polynomial{n}: complete deficit',pot-6/(2*n+3))
# A finite character Rayleigh space: checked as a compression, not an exact vacuum.
for kap,b in [(.7,.2),(1.,2.),(1.3,120.),(1.,10000.)]:
    for m in [2,3,4]:
        old=None
        for rho in np.linspace(0,m,13):
            ell=np.arange(96,dtype=float)
            eig=eigh_tridiagonal(b*m/2+kap*ell*(ell+2)/4,np.full(95,-b*rho/4),select='i',select_range=(0,0))[0][0]
            delta=math.sqrt(9*kap*kap/64+b*b*rho*rho/16)-3*kap/8
            check(f'character{kap},{b},{m},{rho}: two-character trial upper',max(0.,eig-(b*m/2-delta)),tol=2e-7)
            check(f'character{kap},{b},{m},{rho}: original potential minimum',max(0.,b*(m-rho)/2-eig),tol=2e-7)
            n=0 if rho==0 else math.ceil(2*math.sqrt(b*rho/kap))
            trial=b*(m-rho)/2+3*kap*n*n/(4*(4*n+1))+3*b*rho/(2*(2*n+3))
            bound=b*(m-rho)/2+min(b*rho/2,.75*math.sqrt(kap*b*rho)+3*kap/16)
            check(f'character{kap},{b},{m},{rho}: explicit polynomial bound',max(0.,min(trial,b*m/2)-bound),tol=2e-7)
            if old is not None:
                r0,l0=old
                check(f'character{kap},{b},{m},{rho}: strict profile separation',max(0.,(1-r0/rho)*delta-l0+eig),tol=2e-7)
            old=(rho,eig)
# Exact fiber orthogonal decompositions in finite self-adjoint diagnostic spaces.
for trial in range(32):
    nx,nu=7,5
    psi=rng.uniform(.1,1.,size=(nx,nu));psi/=np.linalg.norm(psi)
    As=[];gs=[];ls=[]
    for i in range(nx):
        a=rng.uniform(.1,1.,size=(nu,nu));a=-(a+a.T)/2
        a[np.diag_indices(nu)]=rng.uniform(1.,4.,nu)
        ev,Q=np.linalg.eigh(a);g=Q[:,0]
        if g.sum()<0:g=-g
        assert min(g)>0
        As.append(a);gs.append(g);ls.append(ev[0])
    ls=np.array(ls);gs=np.array(gs);As=np.array(As)
    ap=np.einsum('ijk,ik->ij',As,psi);ce=np.sum(psi*ap);v=ap-ce*psi
    aa=np.sum(gs*psi,axis=1);mass=np.sum(aa*aa)
    rr=psi-aa[:,None]*gs;er=np.einsum('ijk,ik->ij',As,rr)-ce*rr
    var=np.sum(v*v)
    ground=np.sum((ls-ce)**2*aa*aa)
    pair=np.sum((ls[:,None]-ls[None,:])**2*(aa*aa)[:,None]*(aa*aa)[None,:])/(2*mass)
    mean=(np.sum(ls*aa*aa)-ce*mass)**2/mass
    check(f'fiber{trial}: raw full mass bound',max(0,mass-1))
    check(f'fiber{trial}: complete variance remainder',var-ground-np.sum(er*er))
    check(f'fiber{trial}: raw pair and retained mean',ground-pair-mean)
    C=rng.normal(size=(nx,nu));F=C-np.sum(psi*psi*C);source=F*psi
    bb=np.sum(gs*source,axis=1);zz=source-bb[:,None]*gs
    check(f'fiber{trial}: original source covariance',np.sum(source*v)-np.sum((ls-ce)*aa*bb)-np.sum(zz*er))
    vv=rng.normal(size=(4,nx,nu));vv[-1]=-vv[:-1].sum(axis=0)
    weights=rng.normal(size=4);vh=np.einsum('f,fij->ij',weights,vv)
    bf=np.einsum('ij,fij->fi',gs,vv);zf=vv-bf[:,:,None]*gs[None,:,:]
    gram=np.einsum('fij,gij->fg',vv,vv)
    proj=np.sum(np.einsum('f,fi->i',weights,bf)**2)+np.sum(np.einsum('f,fij->ij',weights,zf)**2)
    check(f'fiber{trial}: full smooth-weight projection',np.sum(vh*vh)-proj)
    check(f'fiber{trial}: row-sum covariance relation',weights@gram@weights+.5*np.sum((weights[:,None]-weights[None,:])**2*gram))
# Figure of original star paths and exact raw remainder.
fig=plt.figure(figsize=(16,8),layout='constrained')
ax=fig.add_subplot(121,projection='3d')
v=np.array([0.,0.,0.]);w=np.array([1.,0.,0.])
ax.plot([0,1],[0,0],[0,0],color='#cb4b40',lw=4,label='original edge e')
colors=['#356aa0','#d08024','#48976a','#8158a0']
for k,z in enumerate([np.array([0.,1.,0.]),np.array([0.,-1.,0.]),np.array([0.,0.,1.]),np.array([0.,0.,-1.])]):
    points=np.array([w,w+z,v+z,v])
    ax.plot(points[:,0],points[:,1],points[:,2],color=colors[k],lw=2.5)
    mid=(w+v)/2+z;ax.text(*mid,f'B{k+1}',fontsize=13,color=colors[k])
ax.text(*v,'tail',fontsize=11);ax.text(*w,'head',fontsize=11)
ax.set_xlabel('edge direction');ax.set_ylabel('first transverse coordinate');ax.set_zlabel('second transverse coordinate')
ax.set_xticks([0,1]);ax.set_yticks([-1,0,1]);ax.set_zticks([-1,0,1]);ax.set_box_aspect((1,2,2));ax.view_init(elev=18,azim=-63)
ax.set_title('Four actual three-edge paths, each from head to tail\nAll noncommon links are distinct; boundary stars retain 2 or 3 paths',fontsize=11)
bx=fig.add_subplot(122);bx.axis('off');bx.set_xlim(0,1);bx.set_ylim(0,1)
def box(y,txt,col):
    bx.add_patch(FancyBboxPatch((.035,y),.93,.17,boxstyle='round,pad=.012',facecolor=col,edgecolor='#8294a0'))
    bx.text(.5,y+.085,txt,ha='center',va='center',fontsize=11)
box(.77,r'$S_e=\sum_{p\ni e}B_{p,e},\quad \rho_e^2=m_e+\sum_{p<q}\mathrm{Tr}\,G_{pq,e}$'+'\n'+r'$A_e(x)=-\kappa\Delta_U+\frac{bm_e}{2}-\frac{b}{4}\mathrm{Tr}(US_e)$'+'\nEvery original factor and scalar remains. EV3–EV6.','#e8eff8')
box(.48,'Actual surrounding configurations realize both endpoints:\n'+r'$\rho_e=0\quad\mathrm{and}\quad\rho_e=m_e$'+'\nTheir conditional energies differ strictly. EV8–EV12.','#e6f2e8')
box(.19,r'$\mathcal{C}_{ee}=\frac{1}{2M_e}\iint(\lambda_e-\lambda_e^\prime)^2\,d\nu_e\,d\nu_e^\prime$'+'\n+ the full mean square + the excited-fiber remainder.\n'+r'$d\nu_e=|\langle\phi_{e,x},\psi_x\rangle|^2dx,\quad M_e=\int d\nu_e$'+'\nThe raw full-vacuum overlap mass is retained. EV10–EV11.','#fff1db')
for a,b in [(.76,.66),(.47,.37)]:bx.add_patch(FancyArrowPatch((.5,a),(.5,b),arrowstyle='->',mutation_scale=16,color='#647482'))
bx.text(.5,.05,'Strict finite variance is proved in the original state.\nThe full smooth-weight and source covariances remain. EV24–EV29.',ha='center',fontsize=10)
fig.suptitle('Original edge energy: surrounding loops and complete vacuum variance',fontsize=16)
for ext in ['png','svg']:fig.savefig(O/f'EDGE_VARIANCE_MAP.{ext}',dpi=160)
plt.close(fig)
# Only proved upper/lower functions, never computed original vacuum energies.
fig,axs=plt.subplots(1,3,figsize=(16,5.4),layout='constrained')
rho=np.linspace(0,4,501)
for ax,j in zip(axs,[2,10,100]):
    a=1/(100*j);b=1/(a*a);kap=1.;m=4.
    lo=(m-rho)/2
    hi=lo+np.minimum(rho/2,.75*a*np.sqrt(rho)+3*a*a/16)
    ax.plot(rho,lo,color='#326b9a',label='proved potential lower bound')
    ax.plot(rho,hi,color='#c37529',ls='--',label='proved polynomial upper bound')
    ax.fill_between(rho,lo,hi,color='#d3e3ea',alpha=.8)
    ax.set_title(f'Original regulator j = {j}, a = 1/{100*j}')
    ax.set_xlabel(r'Original surrounding modulus $\rho_e$');ax.set_ylabel(r'$a_j^2\lambda_e$')
    ax.grid(alpha=.2);ax.legend(fontsize=8,loc='upper right')
    ins=ax.inset_axes([.10,.12,.52,.28])
    ins.plot(rho,(hi-lo)/a,color='#c37529',lw=1.5)
    ins.set_title(r'Bound on $a_j\varepsilon_e$',fontsize=8)
    ins.set_xticks([0,2,4]);ins.set_yticks([0,.75,1.5]);ins.tick_params(labelsize=7);ins.grid(alpha=.15)
fig.suptitle('Original conditional-energy bounds; κ* = 1 and interior incidence m = 4',fontsize=15)
fig.supxlabel('EV15–EV19. The plotted region contains the true fiber energy. It is not an original-vacuum probability or spectral-mass plot.',fontsize=10)
for ext in ['png','svg']:fig.savefig(O/f'EDGE_ENERGY_PROFILE_BOUNDS.{ext}',dpi=160)
plt.close(fig)
result=dict(description=__doc__,checks=len(rows),all_passed=True,rows=rows)
(O/'EDGE_VARIANCE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'}))
