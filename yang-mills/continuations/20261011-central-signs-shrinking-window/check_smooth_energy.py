"""WH diagnostics: original SU(2) face algebra, manufactured curved states, finite central-spin sector models and positive operators; no original Yang–Mills vacuum samples."""
from pathlib import Path
import json,math,itertools
import numpy as np
import sympy as sp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent;rows=[]
def check(name,error,tol=2e-8):
    error=float(error);assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
rng=np.random.default_rng(20261011071)
# Original face words, inverse traversals and radius-two generators.
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
T=[-.5j*s for s in sig]
edges=[(z,d) for z in itertools.product(range(2),repeat=3) for d in range(3) if z[d]==0]
idx={e:i for i,e in enumerate(edges)};faces=[]
for z in itertools.product(range(2),repeat=3):
    for d,e in itertools.combinations(range(3),2):
        if z[d] or z[e]:continue
        zd=list(z);ze=list(z);zd[d]+=1;ze[e]+=1
        faces.append([(idx[(z,d)],1),(idx[(tuple(zd),e)],1),(idx[(tuple(ze),d)],-1),(idx[(z,e)],-1)])
def prod(v):
    a=np.eye(2,dtype=complex)
    for b in v:a=a@b
    return a
spacing=.13;centers=np.array([np.array(z)+np.eye(3)[d]/2 for z,d in edges])*spacing
h=.3+.05*centers.sum(axis=1);lh=math.sqrt(3)*.05;ch=(1+math.sqrt(2))*lh/4
for trial in range(22):
    U=[]
    for _ in edges:
        q=rng.normal(size=4);q/=np.linalg.norm(q)
        U.append(q[0]*np.eye(2)+1j*sum(q[i+1]*sig[i] for i in range(3)))
    vals=[];grads=[]
    for face in faces:
        fs=[U[e] if sign==1 else U[e].conj().T for e,sign in face];D=2-np.trace(prod(fs)).real;G=np.zeros((len(edges),3))
        for pos,(ed,sign) in enumerate(face):
            for k,t in enumerate(T):
                dfs=fs.copy();dfs[pos]=t@U[ed] if sign==1 else -U[ed].conj().T@t
                G[ed,k]=-np.trace(prod(dfs)).real
            check(f'SU2{trial}: full face norm{len(vals)} edge{ed}',G[ed]@G[ed]-D+D*D/4)
        vals.append(D);grads.append(G)
    D=np.array(vals);gd=np.array(grads);tv=np.array([np.mean([h[e] for e,s in f]) for f in faces])
    alpha=sum((h[:,None]-t)*g for t,g in zip(tv,gd))
    f=rng.normal(size=len(faces));dC=spacing*np.einsum('p,pek->ek',f,gd)
    paired=0
    for ed in range(len(edges)):
        for p,q in itertools.combinations(range(len(faces)),2):
            paired+=spacing*(f[p]*(h[ed]-tv[q])+f[q]*(h[ed]-tv[p]))*(gd[p,ed]@gd[q,ed])
    diag=sum(f[p]*sum((h[e]-tv[p])*(gd[p,e]@gd[p,e]) for e,s in faces[p]) for p in range(len(faces)))
    check(f'SU2{trial}: same-face source cancellation',diag)
    check(f'SU2{trial}: complete distinct-face source pairing',np.sum(dC*alpha)-paired)
    check(f'SU2{trial}: retained spatial difference bound',max(0,np.sum(alpha*alpha)-16*ch*ch*spacing*spacing*sum(D)))
    trace=sum(sum(h[e]-tv[p] for e,s in face)*.75*(2-D[p]) for p,face in enumerate(faces))
    check(f'SU2{trial}: exact complete trace cancellation',trace)
for mask in range(1<<len(edges)):
    for face in faces:
        selected=[ed for ed,sign in face if mask>>ed&1]
        if not selected or len(selected)==4:continue
        deg={}
        for ed in selected:
            z,d=edges[ed];target=list(z);target[d]+=1
            for v in [z,tuple(target)]:deg[v]=deg.get(v,0)+1
        assert any(n%2 for n in deg.values())
check('all4096 cube edge subsets: every mixed face has an odd selected vertex',0)
# Continuous curved comparison for full weighted quotient and source covariance.
# Its manufactured potential is not a plaquette potential; its divergence is retained.
x,y,aa,bb,cc,kap,hx,hy=sp.symbols('x y aa bb cc kap hx hy',real=True)
tx=(1-x*x)/4;ty=(1-y*y)/4;wx=aa+cc*y;wy=bb+cc*x
Kx=-3*x*wx/4+tx*wx**2;Ky=-3*y*wy/4+ty*wy**2
V=5+kap*(Kx+Ky);tt=(hx+hy)/2;raw=hx*Kx+hy*Ky-tt*V/kap
alx=(hx-tt)*sp.diff(V,x);aly=(hy-tt)*sp.diff(V,y)
L=lambda q:-kap*(tx*sp.diff(q,x,2)-3*x*sp.diff(q,x)/4+2*tx*wx*sp.diff(q,x)+ty*sp.diff(q,y,2)-3*y*sp.diff(q,y)/4+2*ty*wy*sp.diff(q,y))
delta=-(tx*sp.diff(alx,x)-3*x*alx/4+ty*sp.diff(aly,y)-3*y*aly/4+2*tx*wx*alx+2*ty*wy*aly)
assert sp.expand(L(raw)-delta)==0
check('symbolic weighted quotient with complete manufactured divergence',0)
Gh=hx*tx*wx*wx+hy*ty*wy*wy;J=Gh+tt*V/kap;C=x*y;dhC=-3*(hx+hy)*x*y/4
fn=sp.lambdify((x,y,aa,bb,cc,kap,hx,hy),[raw,J,dhC,L(raw),sp.diff(raw,x),sp.diff(raw,y)],'numpy')
theta=np.arange(1,101)*np.pi/101;nodes=np.cos(theta);wt=2/101*np.sin(theta)**2
xx=nodes[:,None];yy=nodes[None,:];base=wt[:,None]*wt[None,:]
for i in range(18):
    a,b,c=rng.uniform(-.3,.3,3);kappa=.6+.07*i;hh=rng.uniform(.1,.9,2)
    rho=np.exp(2*(a*xx+b*yy+c*xx*yy));Z=np.sum(base*rho);mu=base*rho/Z
    avg=lambda q:np.sum(mu*q)
    r,j,dc,force,dx,dy=[np.asarray(q)+np.zeros_like(mu) for q in fn(xx,yy,a,b,c,kappa,*hh)]
    ups=r-avg(r);F=xx*yy-avg(xx*yy)
    check(f'curved{i}: complete original source covariance',avg(F*ups)-.5*avg(dc)+avg(F*j))
    check(f'curved{i}: full physical first moment',avg(ups*force)-kappa*avg((1-xx*xx)/4*dx*dx+(1-yy*yy)/4*dy*dy))
    check(f'curved{i}: retained vacuum orthogonality',avg(ups))
# Finite central-spin models test the actual sector comparison and level integrals.
for model,face_sets in [('one',[(0,1,2,3)]),('two',[(0,1,2,3),(2,4,5,6)])]:
    ne=max(max(f) for f in face_sets)+1;dim=1<<ne;states=np.arange(dim);kappa=.9;b=.7
    spins=np.array([1-2*((states>>e)&1) for e in range(ne)])
    D=np.array([2-2*np.prod(spins[list(f)],axis=0) for f in face_sets])
    T=[kappa*(np.eye(dim)-np.eye(dim)[states^(1<<e)]) for e in range(ne)]
    H=sum(T)+np.diag(b*D.sum(axis=0));lam,U=np.linalg.eigh(H);E0=lam[0];psi=U[:,0]
    if psi.sum()<0:psi=-psi
    assert min(psi)>0
    mu=psi*psi;Te=np.array([t@psi for t in T])
    Ae=np.array([Te[e]+b/4*sum((D[p]*psi for p,f in enumerate(face_sets) if e in f),np.zeros(dim)) for e in range(ne)])
    me=Ae@psi;center=Ae-me[:,None]*psi;cov=center@center.T
    check(model+': exact full energy covariance row kernel',np.linalg.norm(cov@np.ones(ne)))
    def sector(mask):
        selected=[e for e in range(ne) if mask>>e&1];d=1<<len(selected);st=np.arange(d)
        index={e:i for i,e in enumerate(selected)}
        sec=sum((kappa*(np.eye(d)-np.eye(d)[st^(1<<i)]) for i in range(len(selected))),np.zeros((d,d)))
        pot=np.zeros(d)
        for f in face_sets:
            if all(e in index for e in f):
                ss=np.prod([1-2*((st>>index[e])&1) for e in f],axis=0);pot+=b*(2-2*ss)
        return np.linalg.eigvalsh(sec+np.diag(pot))[0]
    energies={mask:sector(mask) for mask in range(1<<ne)}
    sectors={}
    for mask in range(1<<ne):
        sin=[e for e in range(ne) if mask>>e&1];sout=[e for e in range(ne) if not mask>>e&1]
        fin=[p for p,f in enumerate(face_sets) if all(mask>>e&1 for e in f)]
        fout=[p for p,f in enumerate(face_sets) if not any(mask>>e&1 for e in f)]
        mixed=[p for p in range(len(face_sets)) if p not in fin+fout];M=2*b*len(mixed)
        hs=sum((Te[e] for e in sin),np.zeros(dim))+b*sum((D[p]*psi for p in fin),np.zeros(dim))
        ho=sum((Te[e] for e in sout),np.zeros(dim))+b*sum((D[p]*psi for p in fout),np.zeros(dim))
        es=energies[mask];eo=energies[((1<<ne)-1)^mask];eps=E0-es-eo
        ap=hs-es*psi;bp=ho-eo*psi;cross=b*sum((D[p] for p in mixed),np.zeros(dim));mean=psi@ap
        ups=-(hs-(psi@hs)*psi)/kappa;rema=[(M-eps)*(M+eps-2*(mu@cross)),mu@(cross*(2*M-cross)),bp@bp,2*ap@bp,mean*mean]
        check(f'{model} subset{mask}: complete sector variance',kappa*kappa*(ups@ups)-M*M+sum(rema))
        check(f'{model} subset{mask}: every retained remainder nonnegative',max(0,-min(rema)))
        sectors[mask]=(ups,len(mixed))
    for j in range(18):
        h=rng.uniform(0,1,ne);tv=np.array([np.mean(h[list(f)]) for f in face_sets]);lo=np.array([min(h[list(f)]) for f in face_sets]);hi=np.array([max(h[list(f)]) for f in face_sets])
        Hhp=h@Ae;mh=psi@Hhp;ups=-(Hhp-mh*psi)/kappa;n=ups@ups
        Z=(tv-lo)@D;zc=(Z-mu@Z)*psi
        levels=sorted(set([0.,1.,*h]));parts=[];ct=0
        for l,u in zip(levels[:-1],levels[1:]):
            mask=sum((1<<e) for e in range(ne) if h[e]>(l+u)/2);v,Ccross=sectors[mask];parts.append((u-l)*v);ct+=(u-l)*Ccross
        total=sum(parts,np.zeros(dim))
        check(f'{model} weights{j}: full level vector identity',np.linalg.norm(ups-total+b/kappa*zc))
        check(f'{model} weights{j}: exact face ranges',ct-sum(hi-lo))
        exact=sum(v@w for v in parts for w in parts)-2*b/kappa*(total@zc)+(b/kappa)**2*(zc@zc)
        check(f'{model} weights{j}: all nested-sector cross terms',n-exact)
        check(f'{model} weights{j}: whole original norm bound',max(0,math.sqrt(n)-b/kappa*(2*ct+np.linalg.norm(zc))))
        check(f'{model} weights{j}: complete covariance graph',n+.5/kappa**2*np.sum((h[:,None]-h[None,:])**2*cov))
        comp=(E0*psi-Hhp)-(E0-mh)*psi
        check(f'{model} weights{j}: signed noncommuting sector covariance',(Hhp-mh*psi)@comp+kappa*kappa*n)
        if model=='one':check(f'one-face weights{j}: exact zero physical vector',math.sqrt(n))
for i in range(32):
    d=10;Y=rng.normal(size=(14,d));Y[:,0]=0;L=Y.T@Y
    F=rng.normal(size=d);F[0]=0;v=rng.normal(size=d);v[0]=0
    if i%8==0:v=.37*F
    z=.04+i*.014;m=F@F;p=F@v;n=v@v;df=F@L@F;r=F@L@v;e=v@L@v
    G=np.array([[m,p],[p,n]]);En=np.array([[df,r],[r,e]]);Q=np.array([[F@L@L@F,F@L@L@v],[v@L@L@F,v@L@L@v]])
    A=df+z*m;B=r+z*p;tz=e+z*n-B*B/A;N=p*df-m*r
    if i%8==0:beta=0.;gamma=m/A;gain=0
    else:beta=N/(A*tz);gamma=(m-B*beta)/A;gain=N*N/(A*A*tz)
    X=gamma*F+beta*v;Tz=L+z*np.eye(d);inv=np.linalg.solve(Tz,F);error=inv-X
    check(f'full Gram{i}: exact source gain and all residual states',F@inv-m*m/A-gain-error@Tz@error)
    cv=np.array([gamma,beta]);rs=F-Tz@X
    check(f'full Gram{i}: complete equation residual',rs@rs-m+2*cv@np.array([df+z*m,r+z*p])-cv@(Q+2*z*En+z*z*G)@cv)
    if i%8==0:check(f'full Gram{i}: degenerate-span source cancellation',N)
Cheat=2+2*math.sqrt(4+2*math.pi);ch=(1+math.sqrt(2))/4
def bounds(j):
    a=1/(100*j);q=100*j+3;N=3*q*(q+1)**2;M=3*q*q*(q+1);C=12*q*(q+1)
    Lam=min(2*M,3*a*math.sqrt(N*M))+2*C;G=min(8/a**2,Cheat/a)
    n=(2*M+ch*math.sqrt(Lam**2+4*a*a))**2/a**2
    en=16*ch*ch*Lam/a**2;qn=64*ch*ch*N*G*G*Lam/a**2;tail=en/(100*a)
    return a,n,en,qn,tail
a,n,en,qn,tail=bounds(10**11)
for name,ratio in [('actual norm upper',a**8*n/36),('full first moment',a**4*en/(16*ch*ch*33)),('full second moment',a**9*qn/(192*ch*ch*Cheat*Cheat*33)),('original physical tail',a**5*tail/(4*ch*ch*33/25))]:check(name+' coefficient',ratio-1,1e-9)
fig,ax=plt.subplots(figsize=(13,7));ax.set_xlim(0,13);ax.set_ylim(0,7);ax.axis('off')
def box(x,y,w,h,text,col):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.12',facecolor=col,edgecolor='#52667c'));ax.text(x+w/2,y+h/2,text,ha='center',va='center',fontsize=11)
def arrow(p,q):ax.add_patch(FancyArrowPatch(p,q,arrowstyle='->',mutation_scale=17,color='#33465c'))
ax.text(6.5,6.6,'Original weighted energy: exact levels and retained covariances',ha='center',fontsize=16,weight='bold')
box(.4,4.1,3.6,1.7,r'$h_e=h(x_{e,j}),\quad t_p=\frac{1}{4}\sum h_e$'+'\n'+r'$H_h=-\kappa\Delta_h+b\sum t_pD_p$'+'\nEvery original scalar retained\nWH1–WH3','#e6eef6')
box(4.7,4.1,3.6,1.7,r'$S_r=\{e:h_e>r\}$'+'\n'+r'$H_h=\int_0^1H_{S_r}\,dr+bZ_h$'+'\nExact finite edge-level sum\nWH16–WH21','#e6f2ed')
box(9.,4.1,3.6,1.7,r'$\upsilon_h=\int\upsilon_{S_r}dr$'+'\n'+r'$-(b/\kappa)(Z_h-\mu Z_h)$'+'\nAll level covariances retained\nWH22–WH24','#fff2da')
arrow((4.15,5),(4.55,5));arrow((8.45,5),(8.85,5))
box(.5,1.45,5.5,1.9,r'$\operatorname{div}\alpha_h=0$'+'\n'+r'$\mathscr{L}_0\upsilon_h=-2b\,g\cdot\alpha_h$'+'\nComplete physical moments; WH4, WH10–WH11\nWhole weighted sectors do not generally commute.','#e6eef6')
box(6.95,1.45,5.5,1.9,r'$p_h=\frac{1}{2}\mu\Delta_h C-\operatorname{Cov}(C,J_h)$'+'\nSame-face source terms cancel exactly.\nDistinct-face terms and the full residual remain.\nWH25–WH30','#e6f2ed')
arrow((2.2,3.95),(2.8,3.5));arrow((10.8,3.95),(9.7,3.5))
ax.text(6.5,.4,'The exact one-face physical vector is zero (WH33). Surviving mass requires the actual coupling between faces.',ha='center',fontsize=10)
fig.savefig(O/'SMOOTH_ENERGY_LEVEL_MAP.png',dpi=170,bbox_inches='tight');fig.savefig(O/'SMOOTH_ENERGY_LEVEL_MAP.svg',bbox_inches='tight');plt.close(fig)
js=np.unique(np.rint(np.logspace(1,9,150)).astype(np.int64));vals=[bounds(int(j)) for j in js]
fig,axs=plt.subplots(1,3,figsize=(14,5.2))
for ax,k,pow in zip(axs,[1,2,4],[8,4,8]):ax.loglog(js,[v[0]**pow*v[k] for v in vals],color='#326fa3');ax.grid(alpha=.2);ax.set_xlabel('Original regulator j')
axs[0].set_ylabel(r'Upper function for $a_j^8n_h$')
axs[1].set_ylabel(r'Upper function for $a_j^4e_h$')
axs[2].set_ylabel(r'Upper function for $a_j^8e_h/s_j$')
fig.suptitle('Actual norm bound and full physical energy bounds',weight='bold')
fig.text(.5,.02,r'WH7–WH11, WH24 and WH32; $R=\kappa_*=L_h=1$, all integer counts and original $s_j=100\kappa_*a_j$ retained.'+'\nUpper functions only: no measured quantum variance or surviving spectral mass is assigned.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.10,1,.93))
fig.savefig(O/'SMOOTH_ENERGY_WINDOW_BOUNDS.png',dpi=170,bbox_inches='tight');fig.savefig(O/'SMOOTH_ENERGY_WINDOW_BOUNDS.svg',bbox_inches='tight');plt.close(fig)
(O/'SMOOTH_ENERGY_CHECKS.json').write_text(json.dumps(dict(description=__doc__,checks=len(rows),all_passed=True,results=rows),indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
