"""Independent exact/curved and operator diagnostics, not Yang--Mills samples."""
from pathlib import Path
import json,math,itertools
import numpy as np
import sympy as sp
from scipy.special import roots_jacobi
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
O=Path(__file__).resolve().parent;checks=[]
rng=np.random.default_rng(61012010)
def eq(name,l,r):
    err=float(np.max(np.abs(np.asarray(l)-np.asarray(r))))
    scale=max(1.,float(np.max(np.abs(l))),float(np.max(np.abs(r))))
    ok=err<=6e-9*scale
    checks.append(dict(name=name,passed=bool(ok),absolute_error=err));assert ok,checks[-1]
def le(name,l,r):
    ok=bool(l<=r+6e-9*max(1.,abs(l),abs(r)))
    checks.append(dict(name=name,passed=ok,lhs=float(l),rhs=float(r)));assert ok,checks[-1]

# Exact radius-two product geometry with a genuinely coupled smooth density.
x,y,t1,t2,eps,kappa=sp.symbols('x y t1 t2 eps kappa',real=True)
coords=(x,y);metric=((1-x*x)/4,(1-y*y)/4)
w=t1*x+t2*y+eps*x*y
lap=lambda f:sum(metric[i]*sp.diff(f,c,2)-sp.Rational(3,4)*c*sp.diff(f,c) for i,c in enumerate(coords))
dot=lambda u,v:sum(metric[i]*u[i]*v[i] for i in range(2))
grad=lambda f:tuple(sp.diff(f,c) for c in coords)
g=grad(w)
div=lambda q:sum(metric[i]*sp.diff(q[i],c)-sp.Rational(3,4)*c*q[i]+2*metric[i]*g[i]*q[i] for i,c in enumerate(coords))
V=kappa*(lap(w)+dot(g,g))
Gs=[metric[i]*g[i]**2 for i in range(2)]
taus=[-sp.Rational(3,4)*coords[i]*g[i] for i in range(2)]
Rs=[3*g[i]**2*coords[i]**2/16+eps**2*metric[0]*metric[1] for i in range(2)]
forces=[(sp.diff(V,x),0),(0,sp.diff(V,y))]
Qs=[];Ps=[];Ks=[]
for e in range(2):
    ce=coords[e]
    Ke=metric[e]*sp.diff(V,ce,2)-sp.Rational(3,4)*ce*sp.diff(V,ce)-kappa*(2*Rs[e]+Gs[e])
    qe=tuple(forces[e][i]-kappa*sp.diff(Gs[e],coords[i]) for i in range(2))
    pe=tuple(kappa*sp.diff(taus[e],c) for c in coords)
    assert sp.expand(kappa*div(grad(taus[e]))-Ke)==0
    assert sp.expand(div(qe)-Ke)==0
    assert sp.expand(div(tuple(qe[i]-pe[i] for i in range(2))))==0
    checks.extend([dict(name=f'exact partial Bochner {e}',passed=True),dict(name=f'exact density divergence {e}',passed=True),dict(name=f'exact projection divergence {e}',passed=True)])
    Qs.append(qe);Ps.append(pe);Ks.append(Ke)
symbols=(x,y,t1,t2,eps,kappa)
num=lambda f:sp.lambdify(symbols,f,'numpy',cse=True)
nf=[[num(z) for z in f] for f in forces]
nq=[[num(z) for z in q] for q in Qs]
npq=[[num(z) for z in q] for q in Ps]
ng=[num(z) for z in Gs];nr=[num(z) for z in Rs];nk=[num(z) for z in Ks]
nj=[num(g[e]*forces[e][e]*metric[e]) for e in range(2)]
ndv=[num(metric[e]*sp.diff(V,coords[e],2)-sp.Rational(3,4)*coords[e]*sp.diff(V,coords[e])) for e in range(2)]
nodes,weights=roots_jacobi(168,.5,.5)
xx=nodes[:,None];yy=nodes[None,:];mx=(1-xx*xx)/4;my=(1-yy*yy)/4
for trial,(aa,bb,ee,kk) in enumerate([(1,2,.2,.4),(3,4,1,1.3),(8,6,2,2.),(15,9,-3,.7)]):
    ww=aa*xx+bb*yy+ee*xx*yy
    prob=weights[:,None]*weights[None,:]*np.exp(2*(ww-ww.max()));prob/=prob.sum()
    mu=lambda f:float(np.sum(prob*f))
    args=(xx,yy,aa,bb,ee,kk)
    ev=lambda funcs:[f(*args) for f in funcs]
    F=[ev(f) for f in nf];Q=[ev(q) for q in nq];Pq=[ev(q) for q in npq]
    G=ev(ng);RR=ev(nr);K=ev(nk);JV=ev(nj);DV=ev(ndv)
    ip=lambda u,v:mu(u[0]*v[0]*mx+u[1]*v[1]*my)
    Qco=[[Q[e][i]-Pq[e][i] for i in range(2)] for e in range(2)]
    for e in range(2):
        eq(f'mean density defect {trial}/{e}',mu(K[e]),0)
        eq(f'orthogonal flux decomposition {trial}/{e}',ip(Q[e],Q[e]),ip(Pq[e],Pq[e])+ip(Qco[e],Qco[e]))
        for ux,uy,uxy in [(1,1,0),(1,-2,.4),(-.3,.8,-.6)]:
            raw=ux*xx+uy*yy+uxy*xx*yy;X=raw-mu(raw)
            dx=(ux+uxy*yy,uy+uxy*xx)
            eq(f'full density flux pairing {trial}/{e}/{ux}',-mu(K[e]*X),ip(Q[e],dx))
            eq(f'explicit partial-Laplacian receiver {trial}/{e}/{ux}',ip(Q[e],dx),ip(Pq[e],dx))
        for f in range(2):
            formula=(ip(F[e],F[e]) if e==f else 0)
            formula+=kk*mu(G[f]*DV[e]+G[e]*DV[f])+kk*mu(G[f]*JV[e]+G[e]*JV[f])
            formula-=kk*kk*mu(G[e]*RR[f]+G[f]*RR[e]+G[e]*G[f])
            eq(f'complete signed flux Gram {trial}/{e}/{f}',ip(Q[e],Q[f]),formula)
            eq(f'full projected Gram decomposition {trial}/{e}/{f}',ip(Q[e],Q[f]),ip(Pq[e],Pq[f])+ip(Qco[e],Qco[f]))

# Algebraic original-path constants, with all original factors present.
for trial in range(30):
    kap=rng.uniform(.2,3);a=10**rng.uniform(-5,-1);C=rng.uniform(kap,30);b=1/(kap*a*a)
    first=math.sqrt(C*a)/3
    second=(35**.25/(3*math.sqrt(b*a)))*(3*C/kap)**.25
    eq(f'exact finite flux constant {trial}',first+second,math.sqrt(a)/3*(math.sqrt(C)+(105*kap*C)**.25))

# Exact signed original-face incidences and connectivity in finite open cubes.
for side in [1,2,3]:
    verts=list(itertools.product(range(side+1),repeat=3))
    edges=[(v,d) for v in verts for d in range(3) if v[d]<side]
    index={e:i for i,e in enumerate(edges)};faces=[]
    for v in verts:
        for d,k in itertools.combinations(range(3),2):
            if v[d]==side or v[k]==side:continue
            vd=list(v);vd[d]+=1;vk=list(v);vk[k]+=1
            faces.append([(index[(v,d)],1),(index[(tuple(vd),k)],1),(index[(tuple(vk),d)],-1),(index[(v,k)],-1)])
    incidence=np.zeros((len(faces),len(edges)),dtype=int)
    adjacency=np.zeros((len(edges),len(edges)),dtype=int)
    for p,face in enumerate(faces):
        for e,sg in face:incidence[p,e]=sg
        for (e,se),(f,sf) in itertools.combinations(face,2):
            adjacency[e,f]+=1;adjacency[f,e]+=1
    assert adjacency.max()==1
    seen={0};todo=[0]
    while todo:
        e=todo.pop()
        for f in np.flatnonzero(adjacency[e]):
            if int(f) not in seen:seen.add(int(f));todo.append(int(f))
    assert len(seen)==len(edges)
    Hess=incidence.T@incidence
    off=Hess.copy();np.fill_diagonal(off,0)
    assert np.array_equal(abs(off),adjacency)
    lapg=np.diag(adjacency.sum(axis=1))-adjacency
    vals=np.linalg.eigvalsh(lapg)
    assert abs(vals[0])<1e-10 and vals[1]>0
    assert np.linalg.eigvalsh(lapg[:-1,:-1])[0]>0
    checks.extend([dict(name=f'original cube unique coface {side}',passed=True),dict(name=f'original force graph connectivity {side}',passed=True),dict(name=f'exact identity Hessian signs {side}',passed=True),dict(name=f'full constant kernel and proper patch {side}',passed=True)])

# A reducing Hodge-type Hilbert decomposition; projected columns are dependent.
# These finite matrices test identities only, not actual vacuum values.
gains=[]
for trial in range(35):
    n=25;m=8;rank=5
    P=np.diag([1.]*rank+[0.]*(n-rank));Pc=np.eye(n)-P
    eigen=np.geomspace(.03,40,n);L=np.diag(eigen)
    Cmat=rng.normal(size=(n,m));N=Cmat.T@Cmat;Nhat=Cmat.T@P@Cmat;Nc=Cmat.T@Pc@Cmat
    v=P@rng.normal(size=n);kap=rng.uniform(.3,3);z=10**rng.uniform(-2,0)
    lowers=[];uppers=[];truth=[]
    for shift in [z,.1*z,20*z]:
        D=L+shift*np.eye(n);A=D@Cmat;Z=A.T@A
        B=np.vstack((P@A,shift*Pc@Cmat));Zs=B.T@B;k=A.T@v;vv=np.concatenate((v,np.zeros(n)))
        c0=np.linalg.solve(Z,k);cs=np.linalg.solve(Zs,k);M=Z-Zs
        rs=v-P@A@cs;Ds=v@v-k@cs;D0=v@v-k@c0
        eq(f'augmented source {trial}/{shift}',B.T@vv,k)
        eq(f'complete removed matrix {trial}/{shift}',M,Cmat.T@Pc@(L@L+2*shift*L)@Pc@Cmat)
        eq(f'augmented residual {trial}/{shift}',Ds,rs@rs+shift**2*(cs@Nc@cs))
        eq(f'full exact gain {trial}/{shift}',D0-Ds,c0@M@c0+(cs-c0)@Zs@(cs-c0))
        le(f'strict finite removal {trial}/{shift}',1e-12,np.linalg.eigvalsh(M)[0])
        le(f'original norm floor {trial}/{shift}',-1e-9,np.linalg.eigvalsh(Zs-shift*shift*N)[0])
        beta=np.linalg.solve(D,v)
        eq(f'projected physical residual {trial}/{shift}',beta-P@Cmat@cs,np.linalg.solve(D,rs))
        amp=math.sqrt(max(0,shift*kap*(cs@Nhat@cs)));delta=math.sqrt(kap/shift)*np.linalg.norm(rs)
        W=shift*kap*(beta@beta);lo=max(amp-delta,0)**2;up=(amp+delta)**2
        le(f'projected physical lower {trial}/{shift}',lo,W);le(f'projected physical upper {trial}/{shift}',W,up)
        # Independently controlled column perturbation; the original CTI cutoff
        # supplies this norm error in the actual programme.
        gamma=shift*shift*np.linalg.eigvalsh(N)[0]
        E=rng.normal(size=A.shape);E*=math.sqrt(gamma)/(30*np.linalg.norm(E))
        At=A+E;Bt=np.vstack((P@At,shift*Pc@Cmat));Zt=Bt.T@Bt;kt=At.T@v
        ct=np.linalg.solve(Zt,kt);rt=vv-Bt@ct;err=np.linalg.norm(E)
        le(f'projected cutoff error {trial}/{shift}',np.linalg.norm(B-Bt),err)
        le(f'cutoff inverse floor {trial}/{shift}',gamma/2,np.linalg.eigvalsh(Zt)[0])
        le(f'raw coefficient bound {trial}/{shift}',np.linalg.norm(ct),math.sqrt(2/gamma)*math.sqrt(max(0,v@v-rt@rt)))
        measured=v-P@At@ct
        eq(f'cutoff residual correction {trial}/{shift}',rt@rt-shift*shift*(ct@Nc@ct),measured@measured)
        actual=v-P@A@ct
        le(f'complete cutoff physical residual {trial}/{shift}',np.linalg.norm(actual),np.linalg.norm(measured)+err*np.linalg.norm(ct))
        lowers.append(lo);uppers.append(up);truth.append(W)
        if shift==z:gains.append((D0,Ds,rs@rs))
    signed=lowers[0]-4*.1/1.1**2*uppers[1]-4*20/21**2*uppers[2]
    nu=kap*v*v/eigen
    window=nu[(eigen>=.1*z)&(eigen<=20*z)].sum()
    le(f'original three-shift receiving inequality {trial}',4*max(signed,0),window)

out=dict(checks=len(checks),all_passed=True,scope='Symbolic curved geometry and coupled positive densities verify the explicit partial-Laplacian potential, full flux Gram and signs. Original cube incidence checks verify force Hessian signs and graph connectivity. Reducing finite Hilbert models, deliberately with dependent projected columns, verify full augmented residual, strict removed cost, original norm floor, cutoff controls and signed window receiver. These are diagnostics, not Yang-Mills spectral data.',results=checks)
(O/'DENSITY_FLUX_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')

plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(14,8));ax.set_xlim(0,14);ax.set_ylim(0,8);ax.axis('off')
def box(x,y,w,h,title,lines,color):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.10',facecolor=color,edgecolor='#334155'))
    ax.text(x+.15,y+h-.2,title,va='top',weight='bold',fontsize=13)
    ax.text(x+.15,y+h-.67,'\n'.join(lines),va='top',linespacing=1.6,fontsize=11)
box(.2,4.9,6.3,2.1,'Explicit positive-density flux [DF1–7]',[
    r'$\eta_e=d\nu_e/d\mu-1=d_\mu^*q_e$',
    r'$q_e=(F_e^\uparrow-\kappa\,dG_e)/(6b)$',
    r'$Pq_e=\kappa\,d(\Delta_e w)/(6b)$'], '#e0f2fe')
box(7.1,4.9,6.3,2.1,'Original growing observable [DF2–7]',[
    r'$\nu_eX-\mu X=\kappa\,\mu\langle d(\Delta_ew),dX\rangle/(6b)$',
    r'$|\nu_eX-\mu X|\leq\sqrt{a}\sqrt{E_X/\kappa}\,[\sqrt{C}+(105\kappa C)^{1/4}]/3$',
    'Uniform on I(C), at the original observable scale.'], '#dcfce7')
box(.2,1.35,6.3,2.7,'Complete collective trial [DF10–15]',[
    r'$\mathsf{B}_zc=(PD_z\mathsf{C}c,\ zP^\perp\mathsf{C}c)$',
    r'$z^2\mathsf{N}\leq\mathsf{Z}_\star=\mathsf{B}_z^*\mathsf{B}_z\leq\mathsf{Z}$',
    r'$\mathsf{Z}-\mathsf{Z}_\star=36\mathsf{H}^\perp/\kappa^2+2z\mathsf{K}^\perp$',
    'Every original coefficient and exterior Hessian pair remains.'], '#fef3c7')
box(7.1,1.35,6.3,2.7,'Physical residual and three shifts [DF16–21]',[
    r'$\mathcal{D}_\star=\|r_\star\|^2+z^2\|P^\perp\mathsf{C}c_\star\|^2$',
    r'$\mathcal{D}_0-\mathcal{D}_\star=c_0^*\mathsf{M}_\perp c_0+\|\mathsf{B}_z(c_\star-c_0)\|^2$',
    'Strict finite gains at at least two of the three window shifts.',
    'The signed window still depends on the full residual.'], '#ffe4e6')
ax.annotate('',xy=(7,6),xytext=(6.6,6),arrowprops=dict(arrowstyle='->',lw=2))
ax.annotate('',xy=(7,2.7),xytext=(6.6,2.7),arrowprops=dict(arrowstyle='->',lw=2))
ax.text(.2,7.55,'Exact density potential and removal of the full finite curl cost',fontsize=18,weight='bold')
ax.text(.2,.5,'All maps use the original radius-two configuration metric, ground density and physical energy. No uniform spectral gap is assumed.',fontsize=10)
fig.savefig(O/'DENSITY_FLUX_AND_PROJECTION.png',dpi=170,bbox_inches='tight');fig.savefig(O/'DENSITY_FLUX_AND_PROJECTION.svg',bbox_inches='tight');plt.close(fig)

fig,axes=plt.subplots(1,2,figsize=(12,5.7))
ax=axes[0];ax.set_aspect('equal');ax.set_xlim(-.45,1.55);ax.set_ylim(-.45,1.5);ax.axis('off')
points=np.array([[0,0],[1,0],[1,1],[0,1]])
for i in range(4):
    p=points[i];q=points[(i+1)%4]
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',lw=2,color='#0369a1'))
labels=[('e : +1',(.5,-.15)),('f : +1',(1.22,.5)),('r : -1',(.5,1.15)),('s : -1',(-.25,.5))]
for txt,pt in labels:ax.text(*pt,txt,ha='center',va='center')
ax.scatter(points[:,0],points[:,1],s=35,color='#0f172a')
for txt,pt in [(r'$z$',(-.09,-.04)),(r'$z+e_d$',(1.13,-.06)),(r'$z+e_d+e_k$',(1.23,1.05)),(r'$z+e_k$',(-.12,1.05))]:
    ax.text(*pt,txt,ha='center',va='center',fontsize=9)
ax.text(.5,.6,r'$U_p=U_eU_fU_r^{-1}U_s^{-1}$',ha='center',fontsize=12)
ax.text(.5,.4,r'$(\nabla^2V)_{e\alpha,f\beta}=b\,\epsilon_e\epsilon_f\delta_{\alpha\beta}/2$',ha='center',fontsize=10)
ax.set_title('Original oriented face at the identity\nDF13–DF15; no changed metric',fontsize=12)
ax.text(.5,-.37,'Coface connectivity forces the full zero-curl\ncoefficient list to be constant.',ha='center',fontsize=10)
ax=axes[1]
vv=np.array(gains);order=np.argsort(vv[:,0]);xx=np.arange(1,len(vv)+1)
ax.plot(xx,vv[order,0],label=r'Original residual $\mathcal{D}_0$',color='#be123c')
ax.plot(xx,vv[order,1],label=r'Augmented residual $\mathcal{D}_\star$',color='#2563eb')
ax.plot(xx,vv[order,2],label=r'Physical residual $\|r_\star\|^2$',color='#047857',ls='--')
ax.set(xlabel='Finite algebraic example, ordered by original residual',ylabel='Actual squared norms in the stated auxiliary model',title='DF16: complete nonnegative improvement\nDiagnostic matrices; not Yang–Mills data')
ax.legend(fontsize=9);ax.grid(alpha=.2)
fig.suptitle('Original force geometry and the exact residual comparison',fontsize=15)
fig.tight_layout(rect=(0,.02,1,.92))
fig.savefig(O/'FORCE_GRAPH_AND_RESIDUAL_GAIN.png',dpi=170);fig.savefig(O/'FORCE_GRAPH_AND_RESIDUAL_GAIN.svg');plt.close(fig)
print(json.dumps(dict(checks=len(checks),all_passed=True,figures=2)))
