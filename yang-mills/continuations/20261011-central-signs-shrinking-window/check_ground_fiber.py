"""Original path/metric identities, character-compression diagnostics and finite block models. No full Yang–Mills vacuum samples."""
from pathlib import Path
import itertools,json,math
import numpy as np
from scipy.linalg import eigh_tridiagonal,null_space
from scipy.special import roots_jacobi
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent;rows=[];rng=np.random.default_rng(20261012002)
def check(name,error,tol=3e-8):
    error=float(error);assert abs(error)<=tol,(name,error,tol)
    rows.append(dict(name=name,error=error,tolerance=tol,passed=True))
I=np.eye(2,dtype=complex);Z=I*0
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
T=[-.5j*s for s in sig]
def mat(q):return q[0]*I+1j*sum(q[k+1]*sig[k] for k in range(3))
def coeff(a):return np.array([np.trace(a).real/2]+[(np.trace(s@a)/(2j)).real for s in sig])
def prod(fs):
    p=I.copy()
    for x in fs:p=p@x
    return p
def graph(q):
    es=[(z,d) for z in itertools.product(range(q+1),repeat=3) for d in range(3) if z[d]<q]
    ix={e:i for i,e in enumerate(es)};ps=[]
    for z in itertools.product(range(q+1),repeat=3):
        for d,k in itertools.combinations(range(3),2):
            if z[d]==q or z[k]==q:continue
            zd=list(z);zk=list(z);zd[d]+=1;zk[k]+=1
            ps.append([(ix[(z,d)],1),(ix[(tuple(zd),k)],1),(ix[(tuple(zk),d)],-1),(ix[(z,k)],-1)])
    return es,ps
def bw(face,e):
    i=next(k for k,(ee,s) in enumerate(face) if ee==e);p=face[i+1:]+face[:i]
    return p if face[i][1]==1 else [(ee,-s) for ee,s in reversed(p)]
def word(w,U):return prod([U[e] if s==1 else U[e].conj().T for e,s in w])
def jet(w,U,e,t):
    fs=[U[ee] if s==1 else U[ee].conj().T for ee,s in w]
    i=next(k for k,(ee,s) in enumerate(w) if ee==e);s=w[i][1]
    d=fs.copy();dd=fs.copy()
    d[i]=t@U[e] if s==1 else -U[e].conj().T@t
    dd[i]=t@t@U[e] if s==1 else U[e].conj().T@t@t
    return prod(d),prod(dd)
es,ps=graph(2);paths=[[bw(p,e) for p in ps if e in [ee for ee,s in p]] for e in range(len(es))]
quad=np.concatenate([np.eye(4),-np.eye(4),np.array(list(itertools.product([-.5,.5],repeat=4)))])
uq=np.array([mat(q) for q in quad]);wq=np.ones(24)/24
check('exact Haar fourth moment',np.dot(wq,quad[:,0]**4)-1/8)
check('exact Haar mixed fourth moment',np.dot(wq,quad[:,0]**2*quad[:,1]**2)-1/24)
fixtures={}
for trial in range(4):
    qr=rng.normal(size=(len(es),4));qr/=np.linalg.norm(qr,axis=1)[:,None];U=[mat(q) for q in qr]
    for e,pp in enumerate(paths):
        m=len(pp);bs=[word(p,U) for p in pp];S=sum(bs);sv=coeff(S);rho=np.linalg.norm(sv);q=sv/rho
        ai=[];ddi=[]
        for p in pp:
            for ell,sgn in p:
                for t in T:
                    d,dd=jet(p,U,ell,t);ai.append(coeff(d));ddi.append(dd)
        ai=np.array(ai);rp=ai@q;cs=np.array([coeff(bb)@q for bb in bs]);trp=rp@rp
        check(f'path{trial},{e}: derivative coefficient norm',np.sum(ai*ai)-9*m/4)
        check(f'path{trial},{e}: exact radial derivatives',trp-.75*(m-cs@cs))
        check(f'path{trial},{e}: actual outside Casimir',np.linalg.norm(sum(ddi)+2.25*S))
        check(f'path{trial},{e}: radial bound',max(0.,trp-.75*(m-rho*rho/m)))
        fixtures.setdefault(m,(bs,ai,rho,q))
# Original character Rayleigh compressions; no claim of exact vacuum sampling.
xx,ww=roots_jacobi(180,.5,.5);ww*=2/np.pi;chi=2*xx
def chars(x,n):
    v=np.ones((len(x),n));dv=np.zeros_like(v)
    if n>1:v[:,1]=x;dv[:,1]=1
    for k in range(2,n):
        v[:,k]=x*v[:,k-1]-v[:,k-2]
        dv[:,k]=v[:,k-1]+x*dv[:,k-1]-dv[:,k-2]
    return v,dv
ch,dch=chars(chi,96);cc=np.arange(96)*(np.arange(96)+2)/4
def ground(kap,b,rho,n=96,full=False):
    nn=np.arange(n);vals,vs=eigh_tridiagonal(kap*nn*(nn+2)/4,np.full(n-1,-b*rho/4))
    if vs[0,0]<0:vs[:,0]*=-1
    return (vals,vs) if full else vs[:,0]
for kap,b in [(.7,.4),(1.,3.),(1.3,50.)]:
    for m,(bs,ai,rho,q) in fixtures.items():
        ev,V=ground(kap,b,rho,full=True);c=V[:,0]
        mult=np.diag(np.ones(95),1)+np.diag(np.ones(95),-1)
        cr=-(V[:,1:]@((V[:,1:].T@(-b/4*mult@c))/(ev[1:]-ev[0])))
        kval=np.dot(cc,c*c);aval=np.dot(cr,cr);fun=ch@c;rad=ch@cr;der=dch@c
        df=ground(kap,b,rho+1e-5)-ground(kap,b,rho-1e-5)
        check(f'character{kap},{b},{m}: radial response',np.linalg.norm(df/(2e-5)-cr),3e-7)
        check(f'character{kap},{b},{m}: metric kinetic',np.dot(ww,(1-chi**2/4)*der**2)-kval)
        dval=np.dot(ww,(2-chi)*fun**2);qval=np.dot(ww,(1-chi**2/4)*fun**2)
        check(f'character{kap},{b},{m}: full energy decomposition',ev[0]+b*rho/2-kap*kval-b*rho*dval/4)
        check(f'character{kap},{b},{m}: uncertainty lower bound',max(0.,9*(2-dval)**2/(64*qval)-kval))
        trp=np.sum((ai@q)**2);pred=aval*trp+4*kval/(3*rho*rho)*(9*m/4-trp)
        direct=0.
        qm=mat(q)
        for direction in np.concatenate([np.eye(3),-np.eye(3)]):
            vv=np.column_stack([xx,np.sqrt(1-xx*xx)[:,None]*direction]);uu=np.array([mat(v)@qm.conj().T for v in vv])
            for a in ai:
                rp=a@q;da=np.array([np.trace(u@mat(a)).real for u in uu])
                ff=rad*rp+der*(da-chi*rp)/rho
                direct+=np.dot(ww,ff*ff)/6
        check(f'character{kap},{b},{m}: full radial-angular derivative metric',direct-pred,3e-7)
# Exact zero-sum paths and actual link perturbations, including all traversal signs.
for m in [2,3,4]:
    e=next(e for e,pp in enumerate(paths) if len(pp)==m);pp=paths[e];U=[I.copy() for _ in es]
    for k,p in enumerate(pp):
        bb=np.diag([np.exp(2j*np.pi*k/m),np.exp(-2j*np.pi*k/m)])
        ell,sgn=p[0];U[ell]=bb if sgn==1 else bb.conj().T
    bs=[word(p,U) for p in pp];S=sum(bs);check(f'zero{m}: actual matrix sum',np.linalg.norm(S))
    chi_p=np.array([[np.trace(u@bb).real for bb in bs] for u in uq]);vp=np.array([coeff(bb) for bb in bs]);gram=vp.T@vp
    variance=np.dot(wq,(np.sum(chi_p**2,axis=1)-m)**2)
    check(f'zero{m}: exact fourth moment variance',variance-(4*np.trace(gram@gram)-m*m)/3)
    check(f'zero{m}: rank lower bound',max(0.,m*m*(5-m)/(3*(m-1))-variance))
    kap=1.3;b=.7;h=1e-4;lap=np.zeros(24);metric=0.
    for p in pp:
        for ell,sgn in p:
            for t in T:
                d,dd=jet(p,U,ell,t);aa=coeff(d);cy=np.array([np.trace(u@d).real for u in uq])
                responses=[];energies=[]
                for sign in [-1,1]:
                    Ut=U.copy();Ut[ell]=(math.cos(h/2)*I+sign*2*math.sin(h/2)*t)@U[ell]
                    St=sum(word(path,Ut) for path in pp);rh=np.linalg.norm(coeff(St));Qs=St/rh
                    vals,vecs=ground(kap,b,rh,n=16,full=True);cv=vecs[:,0];energies.append(vals[0])
                    cchi=np.array([np.trace(u@Qs).real for u in uq]);cx,_=chars(cchi,16);responses.append(cx@cv)
                fd=(responses[1]-responses[0])/(2*h)
                check(f'zero{m},{ell},{len(rows)}: actual first ground derivative',np.linalg.norm(fd-b*cy/(3*kap)),2e-7)
                check(f'zero{m},{ell},{len(rows)}: actual energy Hessian',(energies[0]+energies[1])/h**2+b*b*np.dot(aa,aa)/(6*kap),2e-7)
                lap+=(responses[0]+responses[1]-2)/h**2
                metric+=np.dot(wq,fd*fd)
    full_lap=b*b/(16*kap*kap)*(m-np.sum(chi_p**2,axis=1))-b*b*m/(4*kap*kap)
    check(f'zero{m}: complete second derivative with unit-norm term',np.max(np.abs(lap-full_lap)),2e-5)
    check(f'zero{m}: complete derivative potential',kap*metric-b*b*m/(4*kap),2e-7)
    check(f'zero{m}: nonzero complement on constant',max(0.,b**4*m*m*(5-m)/(768*kap*kap*(m-1))-b**4*variance/(256*kap*kap)))
simplexes={
2:np.array([[1,0,0,0],[-1,0,0,0]],float),
3:np.array([[1,0,0,0],[-.5,np.sqrt(3)/2,0,0],[-.5,-np.sqrt(3)/2,0,0]]),
4:np.array([[0,1,1,1],[0,1,-1,-1],[0,-1,1,-1],[0,-1,-1,1]],float)/np.sqrt(3)}
for m,v in simplexes.items():
    chi_p=np.array([[np.trace(u@mat(p)).real for p in v] for u in uq])
    check(f'simplex{m}: exact zero sum',np.linalg.norm(v.sum(axis=0)))
    check(f'simplex{m}: sharp complement bound',np.dot(wq,(np.sum(chi_p**2,axis=1)-m)**2)-m*m*(5-m)/(3*(m-1)))
# Exact finite-dimensional analogues of the full coupled operator, raw mass and source.
for trial in range(24):
    psi=rng.uniform(.2,1.,12);psi/=np.linalg.norm(psi);perp=null_space(psi[None,:])
    eig=np.linspace(.2,3.,11);L=(perp*eig)@perp.T
    J=np.zeros((12,4))
    for k in range(4):
        p=rng.uniform(.2,1.,3);p/=np.linalg.norm(p);J[3*k:3*k+3,k]=p
    Qb=null_space(J.T);aa=J.T@psi;rr=Qb.T@psi;M=aa@aa
    A=J.T@L@J;B=Qb.T@L@J;D=Qb.T@L@Qb;Di=np.linalg.inv(D)
    S0=A-B.T@Di@B
    check(f'block{trial}: raw mass',M+rr@rr-1)
    check(f'block{trial}: complement lower bound',max(0.,.2*M-np.linalg.eigvalsh(D)[0]))
    check(f'block{trial}: actual ground complement',np.linalg.norm(rr+Di@B@aa))
    check(f'block{trial}: scalar ground equation',np.linalg.norm(S0@aa))
    check(f'block{trial}: full derivative residue',aa@(np.eye(4)+B.T@Di@Di@B)@aa-1)
    F=rng.normal(size=12);F-=np.dot(psi*psi,F);eta=F*psi;bb=J.T@eta;zz=Qb.T@eta
    check(f'block{trial}: complete source orthogonality',aa@bb+rr@zz)
    check(f'block{trial}: corrected source zero pole',aa@(bb-B.T@Di@zz))
    for z in [.0001,.1,2.]:
        Dzi=np.linalg.inv(D+z*np.eye(8));Sz=A+z*np.eye(4)-B.T@Dzi@B
        kz=bb-B.T@Dzi@zz;f=np.linalg.solve(Sz,kz);r=Dzi@(zz-B@f)
        actual=np.linalg.solve(L+z*np.eye(12),eta)
        check(f'block{trial},{z}: full inverse vector',np.linalg.norm(actual-J@f-Qb@r),3e-7)
        check(f'block{trial},{z}: complete source resolvent',eta@actual-zz@Dzi@zz-kz@f,3e-7)
        check(f'block{trial},{z}: raw residue bound',max(0.,np.linalg.norm(z*np.linalg.inv(Sz)-np.outer(aa,aa),2)-z/(.2+z)),3e-7)
for kap,rr,eta in itertools.product([.2,1.7],[.23,2.1],[.25,1.,3.9]):
    aa=1e-9;dd=3*kap*aa/np.sqrt(4-eta)+3*kap*kap*aa*aa/(4*(4-eta))
    hh=27*kap/256*(2-dd)**2/dd;qq=np.ceil(rr/aa)+3
    nn=3*qq*(qq+1)**2;mm=3*qq*qq*(qq+1);cx=12*qq*(qq+1)
    ll=min(2*mm,3*kap*aa*np.sqrt(nn*mm))+2*cx
    low=aa**4*hh*(3*qq*(qq-1)**2-2*ll/eta)
    target=27*np.sqrt(4-eta)*rr**3/64
    check(f'path{kap},{rr},{eta}: retained finite expression limit',low/target-1,2e-5)
# Reproducible bounds along the original regulator path.
plt.rcParams.update({'font.size':10,'svg.fonttype':'none'})
fig,axs=plt.subplots(1,2,figsize=(12,4.8))
js=np.unique(np.rint(np.geomspace(4,10000,240))).astype(int);a=1/(100*js);kap=1.
for m,col in [(2,'#126c9b'),(3,'#b55e22'),(4,'#507d35')]:
    d=3*kap*a/np.sqrt(m)+3*kap*kap*a*a/(4*m)
    lower=a*27*kap/(64*m)*(2-d)**2/d;upper=9/(4*np.sqrt(m))+9*kap*a/(16*m)
    axs[0].fill_between(js,lower,upper,color=col,alpha=.12)
    axs[0].plot(js,lower,color=col,label=f'm = {m}: lower and upper')
    axs[0].plot(js,upper,color=col,ls='--')
    axs[0].axhline(9/(8*np.sqrt(m)),color=col,ls=':',lw=1.5)
axs[0].set(xscale='log',xlabel='Original regulator j; a = 1/(100j)',ylabel=r'Bounds on $a\,\mathcal{G}_e$ at alignment',title='GF30 bounds; dotted exact limit from RO17')
R=.23;m=4
for eta,col in [(2.,'#126c9b'),(1.,'#b55e22'),(.25,'#507d35')]:
    d=3*a/np.sqrt(4-eta)+3*a*a/(4*(4-eta));h=27/256*(2-d)**2/d
    q=np.ceil(R/a)+3;N=3*q*(q+1)**2;MP=3*q*q*(q+1);C=12*q*(q+1)
    lam=np.minimum(2*MP,3*a*np.sqrt(N*MP))+2*C
    finite=a**4*h*(3*q*(q-1)**2-2*lam/eta)
    axs[1].plot(js,np.maximum(0,finite),color=col,label=rf'$\eta={eta:g}$; finite lower bound')
axs[1].axhline(27*R**3/16,color='#313d4b',ls=':',label=r'Stronger limit lower bound $27R^3/16$ (RO17)')
axs[1].set(xscale='log',xlabel='Original regulator j; R = 0.23',ylabel=r'Lower bound on $a^4\sum_e\mu\mathcal{G}_e$',title='GF31 finite estimates and RO17 strengthening')
for ax in axs:ax.grid(alpha=.2);ax.legend(fontsize=8)
fig.suptitle('Full outside derivative contribution; original radius-two SU(2), κ* = 1')
fig.text(.5,.015,'Integer regulators joined by guides. Proved bounds; no vacuum samples. The full complementary inverse remains in GF8–GF14.',ha='center',fontsize=9)
fig.tight_layout(rect=[0,.05,1,.95]);fig.savefig(O/'GROUND_FIBER_DERIVATIVE_BOUNDS.png',dpi=170);fig.savefig(O/'GROUND_FIBER_DERIVATIVE_BOUNDS.svg');plt.close(fig)
fig,ax=plt.subplots(figsize=(11,5.7));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,txt,col):
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.014',facecolor=col,edgecolor='#67798a'))
    ax.text(x+w/2,y+h/2,txt,ha='center',va='center',fontsize=11)
box(.04,.62,.39,.23,'Original ground family  φ(U,x)\nJf = φ f;  ψ = J aₑ + rₑ\nRaw mass Mₑ + ‖rₑ‖² = 1','#e8f0fa')
box(.57,.62,.39,.23,'Full original Hamiltonian\nA(x) − κΔₓ + Vout + 3bWₑ/4\nAll surrounding-link derivatives retained','#e8f0fa')
box(.04,.25,.39,.24,'Diagonal block  '+r'$\mathcal{A}=J^*HJ-E_0$'+'\nContains '+r'$\mathcal{G}_e=\kappa\sum\|X\phi\|^2$'+'\nExact radial + angular formula: GF17','#eaf3e7')
box(.57,.25,.39,.24,'Complement '+r'$\mathcal{D}=Q(H-E_0)Q$'+'\nCoupling '+r'$\mathcal{B}=QHJ$'+' includes Xφ and Δₓφ\n'+r'$\mathcal{D}\geq\delta_H M_e$'+'; finite regulator only','#faefdc')
ax.add_patch(FancyArrowPatch((.235,.62),(.235,.49),arrowstyle='->',mutation_scale=15,color='#526675'))
ax.add_patch(FancyArrowPatch((.765,.62),(.765,.49),arrowstyle='->',mutation_scale=15,color='#526675'))
ax.add_patch(FancyArrowPatch((.43,.37),(.57,.37),arrowstyle='<->',mutation_scale=15,color='#526675'))
ax.text(.5,.13,'Exact scalar operator:  '+r'$\mathcal{S}_z=\mathcal{A}+z-\mathcal{B}^*(\mathcal{D}+z)^{-1}\mathcal{B}$',ha='center',fontsize=14)
ax.text(.5,.055,'Source correction and raw zero-pole residue retained: GF11–GF14. No decoupling approximation.',ha='center',fontsize=10)
ax.set_title('One original edge and all of its surrounding-link coupling',fontsize=15,pad=15)
fig.tight_layout();fig.savefig(O/'GROUND_FIBER_FULL_OPERATOR_MAP.png',dpi=170);fig.savefig(O/'GROUND_FIBER_FULL_OPERATOR_MAP.svg');plt.close(fig)
result=dict(all_passed=True,checks=len(rows),scope=__doc__,diagnostics=rows)
(O/'GROUND_FIBER_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(all_passed=True,checks=len(rows),figures=2)))
