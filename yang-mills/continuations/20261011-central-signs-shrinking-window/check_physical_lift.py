"""Full-block diagnostics and original ordered SU(2) path derivatives.
Finite block models are not samples of the Yang--Mills vacuum.
"""
from pathlib import Path
import json,itertools,math,re
import numpy as np
from scipy.linalg import null_space
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent
rng=np.random.default_rng(20261012003);rows=[]
def check(name,value,tol=3e-8):
    v=float(np.max(np.abs(value)));assert v<=tol,(name,v,tol)
    rows.append(dict(name=name,error=v,tolerance=tol,passed=True))
def le(name,value,tol=3e-8):check(name,max(0.,float(value)),tol)
def beta(l,z):return z*l/(l+z)**2

# Positive finite graph models with a known full ground, varying positive
# fiber lines, and an outside multiplier commuting with the fiber projection.
for trial in range(28):
    nx=3+trial%3;nf=2+trial%2;n=nx*nf
    psi=np.exp(rng.normal(scale=.6,size=n));psi/=np.linalg.norm(psi)
    ph=np.exp(rng.normal(scale=.6,size=(nx,nf)));ph/=np.linalg.norm(ph,axis=1)[:,None]
    J=np.zeros((n,nx))
    for i in range(nx):J[i*nf:(i+1)*nf,i]=ph[i]
    Q=null_space(J.T)
    w=rng.uniform(.02,.6,size=(n,n));w=(w+w.T)/2;np.fill_diagonal(w,0)
    L=np.diag((w@psi)/psi)-w
    evals,U=np.linalg.eigh(L);evals[0]=0
    A=J.T@L@J;B=Q.T@L@J;D=Q.T@L@Q;a=J.T@psi;r=Q.T@psi
    check(f'{trial}: full ground',L@psi)
    le(f'{trial}: complementary lower bound',evals[1]*(a@a)-np.linalg.eigvalsh(D)[0])
    h=rng.normal(size=nx);hh=np.repeat(h,nf);h-=np.dot(psi*psi,hh);hh=np.repeat(h,nf)
    H=np.diag(hh);eta_h=hh*psi;g=Q.T@L@eta_h;ah=a*h;hr=Q.T@eta_h
    check(f'{trial}: outside multiplier commutes',H@J-J@np.diag(h))
    check(f'{trial}: complementary current',D@hr+B@ah-g)
    q=rng.normal(size=n);q-=np.dot(psi*psi,q);q*=.002/(np.max(abs(q))+.01)
    eta_q=q*psi;eta=eta_h+eta_q;bound=np.max(abs(q))
    d=np.linalg.solve(D,g)
    zlist=[0.,.017,.13,1.7,12.]
    for z in zlist:
        Di=np.linalg.inv(D+z*np.eye(len(D)));K=Di@B
        S=A+z*np.eye(nx)-B.T@K;N=np.eye(nx)+K.T@K
        F=J-Q@K;v=a-B.T@Di@r
        f=rng.normal(size=nx)+1j*rng.normal(size=nx);u=F@f-psi*(v@f)
        check(f'{trial},{z}: full physical norm',F.T@F-N)
        check(f'{trial},{z}: full operator lift',(L+z*np.eye(n))@F-J@S)
        check(f'{trial},{z}: vacuum coefficient',psi@F-v)
        check(f'{trial},{z}: ground Schur equation',S@a-z*v)
        check(f'{trial},{z}: lifted ground',F@a-psi+z*Q@Di@r)
        check(f'{trial},{z}: vacuum orthogonality',psi@u)
        check(f'{trial},{z}: centered norm',np.vdot(u,u)-(np.vdot(f,N@f)-abs(v@f)**2))
        check(f'{trial},{z}: full first moment',np.vdot(u,L@u)-np.vdot(f,(S-z*N)@f))
        check(f'{trial},{z}: full second moment',np.vdot(L@u,L@u)-(np.vdot(S@f,S@f)-2*z*np.vdot(f,S@f)+z*z*np.vdot(f,N@f)))
        le(f'{trial},{z}: stronger Schur order',-np.linalg.eigvalsh(S-z*N)[0])
        gplus=g+z*hr
        check(f'{trial},{z}: actual multiplier ground form',ah@S@ah-(eta_h@L@eta_h+z*(eta_h@eta_h)-gplus@Di@gplus))
        k=J.T@eta-B.T@Di@Q.T@eta
        check(f'{trial},{z}: complete source pairing',np.vdot(eta,u)-np.vdot(k,f))
        step=2e-5
        sp=A+(z+step)*np.eye(nx)-B.T@np.linalg.solve(D+(z+step)*np.eye(len(D)),B)
        sm=A+(z-step)*np.eye(nx)-B.T@np.linalg.solve(D+(z-step)*np.eye(len(D)),B)
        check(f'{trial},{z}: Schur derivative',(sp-sm)/(2*step)-N,3e-7)
        if z:
            fz=np.linalg.solve(S,k);rho=Di@(Q.T@eta-B@fz);rz=J@fz+Q@rho
            full=np.linalg.solve(L+z*np.eye(n),eta)
            check(f'{trial},{z}: full resolvent source',rz-full)
            W=np.dot(beta(evals,z),abs(U.T@eta)**2)
            block=z*((Q.T@eta)@Di@(Q.T@eta)+k@fz)-z*z*(fz@fz+rho@rho)
            check(f'{trial},{z}: complete filter',W-block)
            Wh=np.dot(beta(evals,z),abs(U.T@eta_h)**2)
            le(f'{trial},{z}: filter source error',abs(math.sqrt(max(W,0))-math.sqrt(max(Wh,0)))-bound/2)
            kq=J.T@eta_q-B.T@Di@Q.T@eta_q
            qform=(Q.T@eta_q)@Di@(Q.T@eta_q)+kq@np.linalg.solve(S,kq)
            check(f'{trial},{z}: complete source error',qform-eta_q@np.linalg.solve(L+z*np.eye(n),eta_q))
            le(f'{trial},{z}: source error bound',qform-bound*bound/z)
            eps=.07;R=11.
            C=W-4*eps/(1+eps)**2*np.dot(beta(evals,eps*z),abs(U.T@eta)**2)-4*R/(1+R)**2*np.dot(beta(evals,R*z),abs(U.T@eta)**2)
            mass=np.sum(abs(U.T@eta)[(evals>=eps*z)&(evals<=R*z)]**2)
            le(f'{trial},{z}: three-scale raw lower bound',4*max(C,0)-mass)
    F0=J-Q@np.linalg.solve(D,B);v0=a-B.T@np.linalg.solve(D,r)
    N0=F0.T@F0
    check(f'{trial}: zero metric vacuum',v0-N0@a)
    check(f'{trial}: zero metric ground norm',a@N0@a-1)
    check(f'{trial}: actual source lift defect',eta_h-F0@ah-Q@d)
    u=F0@ah+psi*(r@d)
    check(f'{trial}: full centered outside norm',u@u-(eta_h@eta_h-2*hr@d+d@d-(r@d)**2))
    check(f'{trial}: full centered outside energy',u@L@u-(eta_h@L@eta_h-g@d))
    check(f'{trial}: full original source overlap',eta@u-(eta_h@eta_h+eta_q@eta_h-(hr+Q.T@eta_q)@d))

# Scalar kernels including raw masses that diverge toward zero or infinity.
for eps,R in [(.01,100.),(.07,11.),(.25,4.)]:
    for t in np.logspace(-9,9,91):
        C=beta(t,1)-4*eps/(1+eps)**2*beta(t,eps)-4*R/(1+R)**2*beta(t,R)
        le(f'kernel{eps},{R},{t}: signed support bound',C-(.25 if eps<=t<=R else 0))
    for j in [10,100,10000]:
        for t,mass in [(1/j,j),(j,j)]:
            C=mass*(beta(t,1)-4*eps/(1+eps)**2*beta(t,eps)-4*R/(1+R)**2*beta(t,R))
            le(f'escape{eps},{R},{j},{t}: no false lower mass',4*max(C,0)-(mass if eps<=t<=R else 0))

# Original SU(2) ordered plaquette derivatives; no vacuum is substituted.
I=np.eye(2,dtype=complex)
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
T=[-.5j*s for s in sig]
def mat(v):return v[0]*I+1j*sum(v[k+1]*sig[k] for k in range(3))
def prod(fs):
    p=I.copy()
    for v in fs:p=p@v
    return p
def graph(q):
    es=[(z,d) for z in itertools.product(range(q+1),repeat=3) for d in range(3) if z[d]<q];ix={e:i for i,e in enumerate(es)};ps=[]
    for z in itertools.product(range(q+1),repeat=3):
        for d,k in itertools.combinations(range(3),2):
            if z[d]==q or z[k]==q:continue
            zd=list(z);zk=list(z);zd[d]+=1;zk[k]+=1
            ps.append([(ix[(z,d)],1),(ix[(tuple(zd),k)],1),(ix[(tuple(zk),d)],-1),(ix[(z,k)],-1)])
    return es,ps
es,ps=graph(2)
for trial in range(8):
    qq=rng.normal(size=(len(es),4));qq/=np.linalg.norm(qq,axis=1)[:,None];U=[mat(v) for v in qq]
    coeff=rng.uniform(-1,1,len(ps));a=.013;D=[];gr=[];lp=[]
    for p in ps:
        fs=[U[e] if s==1 else U[e].conj().T for e,s in p];wp=np.trace(prod(fs)).real;grad=np.zeros((len(es),3));lap=0.
        for i,(e,sgn) in enumerate(p):
            for k,t in enumerate(T):
                ff=fs.copy();ff[i]=t@U[e] if sgn==1 else -U[e].conj().T@t
                grad[e,k]=-np.trace(prod(ff)).real
                ff[i]=t@t@U[e] if sgn==1 else U[e].conj().T@t@t
                lap-=np.trace(prod(ff)).real
        D.append(2-wp);gr.append(grad);lp.append(lap)
    D=np.array(D);gr=np.array(gr);lp=np.array(lp)
    for e in range(len(es)):
        inc=np.array([any(ell==e for ell,s in p) for p in ps]);m=int(sum(inc));star={ell for p,yes in zip(ps,inc) if yes for ell,s in p}
        gq=a*np.einsum('p,pek->ek',coeff[inc],gr[inc]);t=D[inc]-D[inc]**2/4
        exact=a*a*(np.sum(np.einsum('p,pk->k',coeff[inc],gr[inc,e])**2)+3*np.dot(coeff[inc]**2,t))
        check(f'path{trial},{e}: incident full gradient',np.sum(gq*gq)-exact)
        le(f'path{trial},{e}: incident gradient bound',np.sum(gq*gq)-a*a*(m+3)*np.max(abs(coeff))**2*np.sum(D[inc]))
        check(f'path{trial},{e}: full incident Laplacian',a*np.dot(coeff[inc],lp[inc])-(6*a*np.sum(coeff[inc])-3*a*np.dot(coeff[inc],D[inc])))
        check(f'path{trial},{e}: original star size',len(star)-(1+3*m))
        gh=a*np.einsum('p,pek->ek',coeff[~inc],gr[~inc])
        check(f'path{trial},{e}: outside fiber derivative',gh[e])
        le(f'path{trial},{e}: outside full energy bound',np.sum(gh*gh)-16*a*a*np.max(abs(coeff))**2*np.sum(D[~inc]))
        check(f'path{trial},{e}: full outside Laplacian',a*np.dot(coeff[~inc],lp[~inc])-(6*a*np.sum(coeff[~inc])-3*a*np.dot(coeff[~inc],D[~inc])))

# Two reproducible mathematical figures, with exact formulas and locators.
plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
fig,ax=plt.subplots(figsize=(13,7.2));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,text):
    text=re.sub(r'\\mathcal ([A-Z])',r'\\mathcal{\1}',text)
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.014',facecolor='#f0f5fa',edgecolor='#466884'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',linespacing=1.7)
box(.025,.72,.42,.18,r'$f\in H^2(dx)$'+'\n'+r'$\mathcal F_z f=Jf-\mathcal D_z^{-1}\mathcal B f$'+'\nFull original complementary inverse')
box(.555,.72,.42,.18,r'$(L+z)\mathcal F_z f=J\mathcal S_z f$'+'\n'+r'$\mathcal N_z=\mathcal S_z^\prime=I+(\mathcal D_z^{-1}\mathcal B)^*(\mathcal D_z^{-1}\mathcal B)$')
box(.025,.40,.42,.18,r'$u_z(f)=\mathcal F_z f-\langle v_z,f\rangle\psi$'+'\n'+r'$v_z=a_e-\mathcal B^*\mathcal D_z^{-1}r_e$'+'\nActual physical vacuum subtraction')
box(.555,.40,.42,.18,r'$\|u_z(f)\|^2=\langle f,\mathcal N_z f\rangle-|\langle v_z,f\rangle|^2$'+'\n'+r'$\langle u_z,Lu_z\rangle=\langle f,\mathcal S_z f\rangle-z\langle f,\mathcal N_z f\rangle$')
box(.13,.065,.74,.18,r'$\|Lu_z(f)\|^2=\|\mathcal S_z f\|^2-2z\langle f,\mathcal S_z f\rangle+z^2\langle f,\mathcal N_z f\rangle$'+'\n'+r'$\langle\eta,u_z(f)\rangle=\langle J^*\eta-\mathcal B^*\mathcal D_z^{-1}Q\eta,f\rangle$'+'\nFull second moment and original-source pairing; PLF4–PLF9')
for start,end in [((.45,.81),(.54,.81)),((.23,.70),(.23,.60)),((.45,.49),(.54,.49)),((.76,.38),(.70,.26))]:
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=14,color='#466884',linewidth=1.8))
ax.set_title('The original Hamiltonian: full lift, physical norm and vacuum',fontsize=16,pad=15)
fig.tight_layout()
for ext in ['png','svg']:fig.savefig(O/('PHYSICAL_LIFT_MAP.'+ext),dpi=170)
plt.close(fig)
eps=1/16;R=16;tt=np.logspace(-4,4,1000);ce=4*eps/(1+eps)**2;cr=4*R/(1+R)**2
fig,axes=plt.subplots(2,1,figsize=(11,8),sharex=True)
axes[0].plot(tt,beta(tt,1),label=r'$\beta_s(\lambda)$',lw=2)
axes[0].plot(tt,ce*beta(tt,eps),label=r'$c_\varepsilon\beta_{\varepsilon s}(\lambda)$',lw=1.8)
axes[0].plot(tt,cr*beta(tt,R),label=r'$c_R\beta_{Rs}(\lambda)$',lw=1.8)
axes[0].set_ylabel('Exact filter values');axes[0].legend(ncol=3,fontsize=10)
combined=beta(tt,1)-ce*beta(tt,eps)-cr*beta(tt,R)
axes[1].plot(tt,combined,color='#194d73',lw=2,label='Signed three-scale kernel')
axes[1].axhline(0,color='black',lw=.7);axes[1].axhline(.25,color='#888',ls=':',label='Exact upper bound 1/4')
for ax in axes:
    ax.set_xscale('log');ax.axvspan(eps,R,alpha=.12,color='#2c9b73');ax.axvline(eps,color='#37775e',ls='--');ax.axvline(R,color='#37775e',ls='--');ax.grid(alpha=.2)
axes[1].set_xlabel(r'Comparison coordinate $\lambda/s$; original $s=s_j=100\kappa_*a_j$ retained')
axes[1].set_ylabel('Signed kernel');axes[1].legend(loc='upper right',fontsize=10)
fig.suptitle(r'Original window $[\varepsilon s,Rs]$: $\varepsilon=1/16$, $R=16$',fontsize=15)
fig.text(.5,.012,'PLF25–PLF26. The kernel is nonpositive outside the shaded window.\nIts actual spectral integral is not assigned a positive value; no vacuum samples are plotted.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.06,1,.96))
for ext in ['png','svg']:fig.savefig(O/('THREE_SCALE_PHYSICAL_WINDOW.'+ext),dpi=170)
plt.close(fig)
report=dict(checks=len(rows),all_passed=True,scope='Full-block finite graph diagnostics, actual ordered original SU(2) path derivatives, scalar filter bounds including divergent raw escape examples. No full Yang–Mills vacuum samples.',rows=rows)
(O/'PHYSICAL_LIFT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='rows'}))
