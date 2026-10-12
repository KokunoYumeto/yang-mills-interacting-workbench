"""Original ordered Hessian checks and noncommuting finite operator diagnostics.
Finite models and comparison measures are not Yang--Mills vacuum samples.
"""
from pathlib import Path
import itertools,json,math,re
import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch,FancyArrowPatch
O=Path(__file__).resolve().parent;rng=np.random.default_rng(20261012004);rows=[]
def check(name,error,scale=1.,tol=8e-8):
    error=float(np.max(np.abs(error)));scale=max(1.,float(scale));assert error<=tol*scale,(name,error,scale,tol)
    rows.append(dict(name=name,absolute_error=error,comparison_scale=scale,relative_tolerance=tol,passed=True))
def le(name,excess,scale=1.,tol=8e-8):check(name,max(0.,float(excess)),scale,tol)
def power(A,p):
    e,u=eigh(A);assert np.min(e)>0
    return (u*e**p)@u.T
for trial in range(32):
    n=12;k=6;m=4
    X,_=np.linalg.qr(rng.normal(size=(n,n)));P=X[:,:k]@X[:,:k].T
    kap=[.7,1.,1.8][trial%3];j=[1,3,9,27][trial%4];a=1/(100*j);s=100*kap*a
    eigen=np.r_[s*np.array([.03,.2,.8,1.4,7.,60.]),np.linspace(.4,2.,n-k)/a]
    L=(X*eigen)@X.T
    Y=rng.normal(size=(n,n));T0=L+(kap/2+4/a)*np.eye(n)+Y.T@Y
    v=P@rng.normal(size=n);E=kap*(v@v);alphas=a*a*rng.normal(size=(n,m))
    N=alphas.T@alphas;K=alphas.T@L@alphas;K2=(L@alphas).T@(L@alphas)
    b=alphas.T@v
    # Model scalar coefficients retain the exact spectral isometry.
    hv=(X.T@v)*np.sqrt(kap/eigen)
    for theta in [.07,1.,11.]:
        z=theta*s;D=L+z*np.eye(n);Tz=T0+z*np.eye(n);t=kap/2+4/a+z
        Ti=power(Tz,-.5);Q=Ti@(T0-L)@Ti;I=np.eye(n);q,Uq=eigh(Q)
        C=I-Q;beta=np.linalg.solve(D,v);W=z*kap*(beta@beta)
        direct=np.dot(z*eigen/(eigen+z)**2,abs(hv)**2)
        check(f'{trial},{theta}: exact physical filter',W-direct,W)
        inv=Ti@np.linalg.solve(C,Ti)
        check(f'{trial},{theta}: full noncommuting inverse',inv-np.linalg.inv(D),np.linalg.norm(inv),4e-6)
        R=kap*(v@beta);den=kap*(v@Tz@v)
        le(f'{trial},{theta}: positive response lower bound',E*E/den-R,R)
        le(f'{trial},{theta}: squared response lower bound',z*E**3/den**2-W,W)
        for length in [0,1,4,13]:
            powers=np.eye(n);sumq=powers.copy()
            for step in range(length):powers=powers@Q;sumq+=powers
            wn=Ti@sumq@Ti@v
            tail=Ti@(powers@Q)@np.linalg.solve(C,Ti@v)
            check(f'{trial},{theta},{length}: full finite sum and tail',wn+tail-beta,np.linalg.norm(beta),4e-6)
            le(f'{trial},{theta},{length}: filtered finite sum bound',math.sqrt(z*kap)*np.linalg.norm(wn)-(length+1)*math.sqrt(z*E)/t,math.sqrt(W))
            le(f'{trial},{theta},{length}: complete error bound',abs(math.sqrt(W)-math.sqrt(z*kap)*np.linalg.norm(wn))-math.sqrt(z*kap)*np.linalg.norm(tail),math.sqrt(W),4e-6)
        eps=.07;Rw=11.;mask=(eigen>=eps*s)&(eigen<=Rw*s)
        xi=X@(mask*(X.T@v));y=power(Tz,.5)@xi
        check(f'{trial},{theta}: original window metric',y@C@y-xi@D@xi,np.linalg.norm(y)**2,2e-7)
        le(f'{trial},{theta}: window energy bound',y@C@y-(Rw*s+z)*(xi@xi),y@y)
        for delta in [.02,a,a*a]:
            low=Uq[:,q<1-delta];norm=np.linalg.norm(low.T@y)**2
            le(f'{trial},{theta},{delta}: raw near-one leakage',norm-(Rw*s+z)*(xi@xi)/delta,y@y)
            le(f'{trial},{theta},{delta}: full metric leakage ratio',norm/(y@y)-(Rw*s+z)/(t*delta))
        Z=K2+2*z*K+z*z*N;DzA=D@alphas
        check(f'{trial},{theta}: complete squared matrix',Z-DzA.T@DzA,np.linalg.norm(Z))
        le(f'{trial},{theta}: full matrix lower order',-np.linalg.eigvalsh(Z-z*z*N)[0])
        cs=np.linalg.solve(Z,b);ast=alphas@cs;lower=z*kap*(b@cs);res=beta-D@ast
        check(f'{trial},{theta}: squared-norm optimizer',W-lower-z*kap*(res@res),W)
        check(f'{trial},{theta}: exact form orthogonality',DzA.T@res,np.linalg.norm(DzA)*np.linalg.norm(res))
        pr=beta-P@D@ast;nr=(I-P)@D@ast
        check(f'{trial},{theta}: both physical residuals',W-lower-z*kap*(pr@pr+nr@nr),W)
        for shift in range(3):
            cc=cs+rng.normal(size=m)*100
            val=z*kap*(2*b@cc-cc@Z@cc)
            le(f'{trial},{theta},{shift}: finite variational optimum',val-lower,abs(lower))

# Complete pointwise force/Hessian square with exterior rows retained.
for trial in range(80):
    edges=7;Iedges=[0,2,5];kap=rng.uniform(.3,2);a=1/(100*(trial+1))
    H=rng.normal(size=(3*edges,3*edges));H=(H+H.T)/2
    g=rng.normal(size=(edges,3));force=rng.normal(size=(edges,3))
    cols=[];base=[]
    for ell in Iedges:
        gg=np.zeros(3*edges);ff=np.zeros(3*edges)
        gg[3*ell:3*ell+3]=g[ell];ff[3*ell:3*ell+3]=force[ell]
        cols.append(a*a*(-ff-2*kap*H@gg));base.append(gg)
    cols=np.array(cols).T;direct=cols.T@cols
    for i,ell in enumerate(Iedges):
        for k,emm in enumerate(Iedges):
            Hel=H[3*ell:3*ell+3,3*emm:3*emm+3];Hem=H[3*emm:3*emm+3,3*ell:3*ell+3]
            scalar=(np.dot(force[ell],force[ell]) if ell==emm else 0)
            scalar+=2*kap*(force[ell]@Hel@g[emm]+force[emm]@Hem@g[ell])
            allrows=sum((H[3*r:3*r+3,3*ell:3*ell+3]@g[ell])@(H[3*r:3*r+3,3*emm:3*emm+3]@g[emm]) for r in range(edges))
            scalar+=4*kap*kap*allrows
            check(f'force{trial},{ell},{emm}: all exterior Hessian rows',direct[i,k]-a**4*scalar)
    z=rng.uniform(.1,3);A=a*a*np.array(base).T
    check(f'force{trial}: all six shifted contributions',(cols+z*A).T@(cols+z*A)-(direct+z*(cols.T@A+A.T@cols)+z*z*A.T@A))

# Exact original signed Hessian formula from ordered SU(2) words.
unit=np.eye(2,dtype=complex)
sig=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.diag([1,-1]).astype(complex)]
gens=[-.5j*s for s in sig]
def mat(v):return v[0]*unit+1j*sum(v[k+1]*sig[k] for k in range(3))
def prod(fs):
    p=unit.copy()
    for v in fs:p=p@v
    return p
q=2;es=[(x,d) for x in itertools.product(range(q+1),repeat=3) for d in range(3) if x[d]<q];ix={e:i for i,e in enumerate(es)};faces=[]
for x in itertools.product(range(q+1),repeat=3):
    for d,k in itertools.combinations(range(3),2):
        if x[d]==q or x[k]==q:continue
        xd=list(x);xk=list(x);xd[d]+=1;xk[k]+=1
        faces.append([(ix[(x,d)],1),(ix[(tuple(xd),k)],1),(ix[(tuple(xk),d)],-1),(ix[(x,k)],-1)])
inc=np.array([[any(ell==e for ell,sgn in p) for p in faces] for e in range(len(es))])
chosen=[int(np.flatnonzero(inc.sum(axis=1)==m)[0]) for m in [2,3,4]]
for trial in range(6):
    qs=rng.normal(size=(len(es),4));qs/=np.linalg.norm(qs,axis=1)[:,None];us=[mat(v) for v in qs]
    ff=rng.uniform(-1,1,len(faces));a=.011;blocks=[];traces=[]
    for p in faces:
        fs=[us[e] if sign==1 else us[e].conj().T for e,sign in p]
        wp=np.trace(prod(fs)).real;traces.append(wp);hess=np.zeros((3*len(es),3*len(es)))
        for i,(e,sgn) in enumerate(p):
            for k,(f,sgnf) in enumerate(p):
                for al,ta in enumerate(gens):
                    for be,tb in enumerate(gens):
                        fac=fs.copy()
                        if i==k:
                            sym=(ta@tb+tb@ta)/2
                            fac[i]=sym@us[e] if sgn==1 else us[e].conj().T@sym
                        else:
                            fac[i]=ta@us[e] if sgn==1 else -us[e].conj().T@ta
                            fac[k]=tb@us[f] if sgnf==1 else -us[f].conj().T@tb
                        hess[3*e+al,3*f+be]=-np.trace(prod(fac)).real
        blocks.append(hess)
    traces=np.array(traces);blocks=np.array(blocks)
    for e0 in chosen:
        coeff=ff*(~inc[e0]);full=a*np.einsum('p,pij->ij',coeff,blocks)
        expr=a*a*(3/16*np.sum((inc@(coeff*traces))**2)+np.dot(coeff**2,6+3*traces**2/4))
        check(f'original Hessian{trial},{e0}: complete signed formula',np.sum(full*full)-expr)
        le(f'original Hessian{trial},{e0}: original coefficient21',expr-21*a*a*np.dot(coeff,coeff))

# Original path, all finite constants, and the explicit high-energy comparison.
kap=1.;Rbox=2.;LR=9*kap*Rbox**3+24*Rbox**2;KR=(LR+math.sqrt(LR**2-81*kap**2*Rbox**6/4))/2
ef=81*kap**3/KR;Uf=16*kap*KR;Df=21*kap**2*(8/9)+4*Uf
for j in [4,7,16,64,1000,10000]:
    a=1/(100*j);s=100*kap*a;mass=ef*a;energy=1/a
    for theta in [.07,1,11]:
        W=mass*(theta*s)*energy/(energy+theta*s)**2
        exact=100*theta*kap*ef*a**3/(1+100*theta*kap*a*a)**2
        check(f'comparison{j},{theta}: exact raw filtered mass',W-exact)
        check(f'comparison{j},{theta}: retained first energy',mass*energy-ef)
        check(f'comparison{j},{theta}: retained second energy',a*mass*energy**2-ef)
        le(f'comparison{j},{theta}: allowed second moment',ef-Df)
    check(f'comparison{j}: empty original window',int(.07*s<=energy<=11*s))

plt.rcParams.update({'font.size':11,'svg.fonttype':'none'})
# Exact finite upper functions for the original fitted cube and integer j.
js=np.unique(np.geomspace(4,10000,180).astype(int));aa=1/(100*js)
fig,ax=plt.subplots(figsize=(11.5,6.8))
for p in [0.,1.,1.4,1.5]:
    values=[]
    for j,a in zip(js,aa):
        q=math.ceil(Rbox/a)+3;N=3*q*(q+1)**2;M=3*q*q*(q+1);cross=12*q*(q+1)
        g2=kap*a/2;Lambda=min(2*M,6*g2*math.sqrt(N*M))+2*cross
        Eup=16*kap*a*a*Lambda
        length=math.floor(a**(-p))
        values.append(100*kap*a**3*(length+1)**2*Eup/(4+kap*a/2+100*kap*a*a)**2)
    ax.loglog(js,values,label=rf'$N_j=\lfloor a_j^{{-{p:g}}}\rfloor$')
ax.set(xlabel=r'Original integer regulator $j$; $a_j=(100j)^{-1}$',ylabel='Proved finite upper function for filtered partial-sum norm squared')
ax.set_title(r'Full original finite-sum bound, $\kappa_*=1$, support cube side $R=2$')
ax.legend(ncol=2);ax.grid(alpha=.25,which='both')
fig.text(.5,.01,'FTC13–FTC16. Every original cube count and crossing-face term is retained.\nValues evaluate upper bounds using PLF20; no actual vacuum values are plotted.',ha='center',fontsize=10)
fig.tight_layout(rect=(0,.075,1,1))
for ext in ['png','svg']:fig.savefig(O/('FILTERED_FINITE_SUM_BOUNDS.'+ext),dpi=160)
plt.close(fig)
fig,ax=plt.subplots(figsize=(13,7.4));ax.set(xlim=(0,1),ylim=(0,1));ax.axis('off')
def box(x,y,w,h,text):
    text=re.sub(r'\\mathcal ([A-Z])',r'\\mathcal{\1}',text)
    text=re.sub(r'\\mathsf ([A-Za-z])',r'\\mathsf{\1}',text)
    ax.add_patch(FancyBboxPatch((x,y),w,h,boxstyle='round,pad=.012',facecolor='#edf4f8',edgecolor='#416581'))
    ax.text(x+w/2,y+h/2,text,ha='center',va='center',linespacing=1.6)
box(.025,.73,.42,.17,r'Original current $v=dh_{e_0}$'+'\n'+r'$\beta=(\mathscr{L}_1+z)^{-1}v$'+'\n'+r'$\mathcal W(z)=z\kappa_*\|\beta\|_\mu^2$')
box(.555,.73,.42,.17,r'$\alpha_\ell=a_j^2\Pi_\ell d\log\psi_j$'+'\n'+r'$D_z\alpha_\ell=a_j^2[-\Pi_\ell dV-2\kappa_*H\Pi_\ell dw+z\Pi_\ell dw]$'+'\n'+r'$w=\log\psi_j,\quad H=(\nabla^2w)^\sharp,\quad V=V_{\rm pot}$')
box(.16,.41,.68,.17,r'$\mathsf Z(z)=\mathsf K_2+2z\mathsf K+z^2\mathsf N$'+'\n'+r'$\mathsf Z(z)_{\ell m}=\langle D_z\alpha_\ell,D_z\alpha_m\rangle_\mu$'+'\nFull original force, mixed Hessian and every exterior row')
box(.08,.065,.84,.20,r'$c_*=\mathsf Z(z)^{-1}\mathsf b,\qquad \alpha_*=\sum_\ell(c_*)_\ell\alpha_\ell$'+'\n'+r'$\mathcal W(z)=z\kappa_*\mathsf b^*\mathsf Z(z)^{-1}\mathsf b+z\kappa_*\|\beta-D_z\alpha_*\|_\mu^2$'+'\nFTC21–FTC31: exact physical and nonexact residuals both retained')
for start,end in [((.24,.71),(.32,.60)),((.76,.71),(.68,.60)),((.50,.39),(.50,.28))]:
    ax.add_patch(FancyArrowPatch(start,end,arrowstyle='-|>',mutation_scale=14,linewidth=1.8,color='#416581'))
ax.set_title('Direct optimization of the original filtered response',fontsize=16,pad=15);fig.tight_layout()
for ext in ['png','svg']:fig.savefig(O/('FILTERED_CURRENT_OPTIMIZATION.'+ext),dpi=160)
plt.close(fig)
report=dict(checks=len(rows),all_passed=True,scope='Noncommuting finite-operator diagnostics, exact original ordered SU(2) Hessian checks, complete force/Hessian-square algebra including exterior rows, and explicit comparison measures. No Yang–Mills vacuum samples.',rows=rows)
(O/'FILTERED_CURRENT_CHECKS.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in report.items() if k!='rows'}))
