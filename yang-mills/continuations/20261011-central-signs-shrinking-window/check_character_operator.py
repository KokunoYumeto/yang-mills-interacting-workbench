from pathlib import Path
import json
import numpy as np
from scipy.special import iv, roots_jacobi
O=Path(__file__).resolve().parent;rows=[]
def eq(name,a,b,tol=2e-9):
    err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))))
    scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=bool(err<tol*scale),error=err))
def chars(N):
    return np.array([[(-1.)**((s&t).bit_count()) for s in range(1,2**N)] for t in range(2**N)])
def jets(H,l,li,lij):
    p=np.exp(l-l.max());p/=p.sum();h=np.sqrt(p);k=li.shape[0]
    v=li-(li@p)[:,None]
    pi=v*p
    pij=np.array([[p*(v[i]*v[j]+lij[i,j]-lij[i,j]@p-(v[i]*p)@v[j]) for j in range(k)] for i in range(k)])
    hi=pi/(2*h);hij=pij/(2*h)-pi[:,None,:]*pi[None,:,:]/(4*h**3)
    r=H.T@p;ri=pi@H;rij=pij@H;Z=H-r;Xi=h[:,None]*Z
    Xi_i=hi[:,:,None]*Z-h[None,:,None]*ri[:,None,:]
    Xi_ij=np.array([[hij[i,j,:,None]*Z-hi[i,:,None]*ri[j]-hi[j,:,None]*ri[i]-h[:,None]*rij[i,j] for j in range(k)] for i in range(k)])
    C=H.T@(p[:,None]*H)-np.outer(r,r);Ci=np.array([H.T@(pi[i,:,None]*H)-np.outer(ri[i],r)-np.outer(r,ri[i]) for i in range(k)])
    Cij=np.array([[H.T@(pij[i,j,:,None]*H)-np.outer(rij[i,j],r)-np.outer(ri[i],ri[j])-np.outer(ri[j],ri[i])-np.outer(r,rij[i,j]) for j in range(k)] for i in range(k)])
    inv=np.linalg.inv(C);conn=np.array([.5*inv@c for c in Ci])
    dc=np.array([[.5*(-inv@Ci[j]@inv@Ci[i]+inv@Cij[i,j]) for j in range(k)] for i in range(k)])
    return locals()
for seed in range(6):
    rng=np.random.default_rng(1800+seed);N=2+seed%2;H=chars(N);n=2**N;k=2;m=n-1
    l=.2*rng.normal(size=n);li=.3*rng.normal(size=(k,n));lij=.1*rng.normal(size=(k,k,n));lij=(lij+lij.transpose(1,0,2))/2
    j=jets(H,l,li,lij);p,h,r,ri,C,inv,Xi,conn=[j[x] for x in ['p','h','r','ri','C','inv','Xi','conn']]
    Q=np.eye(n)-np.outer(h,h);Ci=j['Ci'];Xi_i=j['Xi_i'];hi=j['hi']
    eq(f'{seed} covariance Gram',Xi.T@Xi,C);eq(f'{seed} full projector',Xi@inv@Xi.T,Q)
    eq(f'{seed} full inverse n squared',inv,H.T@((1/p)[:,None]*H)/n**2)
    c=rng.normal(size=m)+1j*rng.normal(size=m);di=rng.normal(size=(k,m))+1j*rng.normal(size=(k,m))
    for i in range(k):
        eq(f'{seed} dh {i}',hi[i],.5*Xi@inv@ri[i])
        eq(f'{seed} full frame derivative {i}',Xi_i[i],Xi@conn[i]-.5*np.outer(h,ri[i]))
        eq(f'{seed} metric compatibility {i}',Ci[i],conn[i].T@C+C@conn[i])
        dv=Xi_i[i]@c+Xi@di[i];cov=di[i]+conn[i]@c
        eq(f'{seed} normal energy {i}',np.vdot(dv,dv),np.vdot(cov,C@cov)+abs(ri[i]@c)**2/4)
    curvature=j['dc'][1,0]-j['dc'][0,1]+conn[0]@conn[1]-conn[1]@conn[0]
    eq(f'{seed} spherical curvature sign',curvature,.25*inv@(np.outer(ri[0],ri[1])-np.outer(ri[1],ri[0])))
    eq(f'{seed} matrix wedge curvature',curvature,-.25*(inv@Ci[0]@inv@Ci[1]-inv@Ci[1]@inv@Ci[0]))
    eq(f'{seed} full normal integrability',ri[0]@conn[1]-ri[1]@conn[0],np.zeros(m))
    R=np.einsum('ia,ib->ab',ri,ri);kappa=.7;ui=np.array([.13,-.27]);F=np.sum(hi**2)
    # An actual component ground equation at this jet; not a Wilson vacuum.
    v=kappa*(np.einsum('iin->n',j['hij'])+2*ui@hi)/h
    V=Xi.T@(v[:,None]*Xi)
    zero=-kappa*sum(j['dc'][i,i]+conn[i]@conn[i]+2*ui[i]*conn[i] for i in range(k))+inv@(kappa*R/4+V)
    eq(f'{seed} complete zero order comparison',zero,kappa*inv@R)
    cii=rng.normal(size=(k,m))+1j*rng.normal(size=(k,m))
    vv=Xi@c;vfirst=Xi_i@c+di@Xi.T
    vsecond=np.array([j['Xi_ij'][i,i]@c+2*Xi_i[i]@di[i]+Xi@cii[i] for i in range(k)])
    direct=inv@Xi.T@(-kappa*(vsecond.sum(axis=0)+2*ui@vfirst)+v*vv)
    evaluated=-kappa*(cii.sum(axis=0)+2*ui@di+sum(inv@Ci[i]@di[i] for i in range(k)))+kappa*inv@R@c
    eq(f'{seed} complete differential action',direct,evaluated)
    # Independent Wilson-potential algebra, with every original character.
    face_ids=[1,n-1];tr=np.array([.4,-1.2]);b=2.3;M=2
    Wpot=2*b*M-b*H[:,np.array(face_ids)-1]@tr;mean=p@Wpot
    third=np.zeros((m,m));rf=np.r_[1,r]
    for Ridx,Tp in zip(face_ids,tr):
        formula=np.array([[rf[S^T^Ridx]-rf[S]*rf[T^Ridx]-rf[T]*rf[S^Ridx]-rf[Ridx]*rf[S^T]+2*rf[S]*rf[T]*rf[Ridx] for T in range(1,n)] for S in range(1,n)])
        actual=H-r;actual=actual.T@((p*(H[:,Ridx-1]-r[Ridx-1]))[:,None]*(H-r))
        eq(f'{seed} third moment {Ridx}',formula,actual);third+=Tp*formula
    eq(f'{seed} original Wilson potential matrix',Xi.T@((Wpot-mean-kappa*F)[:,None]*Xi),-b*third-kappa*F*C)

# Continuous gauge-invariant four-link radius-two fixture. Its ground potential
# is constructed exactly and is explicitly different from the Wilson potential.
H=chars(4);chi=H[:,-1];kappa=.8;a=.017;phi=.6+.2j;E0=1.7;lam=.23;Znorm=iv(1,4*lam)/(2*lam)
def oneface(T,record=False):
    j=jets(H,2*lam*chi*T,(2*lam*chi)[None,:],np.zeros((1,1,16)))
    h,r,ri,C,inv,Xi,conn=[j[x] for x in ['h','r','ri','C','inv','Xi','conn']]
    rp=ri[0];G=4-T*T;lapT=-3*T;up=lam*np.tanh(2*lam*T);A2=np.cosh(2*lam*T)/Znorm
    Vtau=E0+kappa*(lam*lapT*chi+lam*lam*G);barV=j['p']@Vtau;F=G*np.sum(j['hi']**2);pot=Vtau-barV-kappa*F
    R=G*np.outer(rp,rp);K=conn[0];Kp=j['dc'][0,0];Ci=j['Ci'][0]
    c=np.zeros(15,dtype=complex);cp=c.copy();cpp=c.copy()
    c[-1]=T+.25j*T**3;cp[-1]=1+.75j*T*T;cpp[-1]=1.5j*T
    v=Xi@c;vp=j['Xi_i'][0]@c+Xi@cp;vpp=j['Xi_ij'][0,0]@c+2*j['Xi_i'][0]@cp+Xi@cpp
    ambient=inv@Xi.T@(-kappa*(G*vpp+(lapT+2*G*up)*vp)+pot*v)
    full=-kappa*(G*cpp+lapT*cp+2*G*K@cp+(G*Kp+lapT*K)@c+G*K@K@c+2*G*up*cp+2*G*up*K@c)+inv@(kappa*R/4+Xi.T@(pot[:,None]*Xi))@c
    exact=-kappa*(G*cpp+(lapT+2*G*up)*cp+G*inv@Ci@cp)+kappa*inv@R@c
    fprime=2*T+.8*T**3;beta=-kappa*inv@(G*rp*fprime)
    dx=np.zeros(15,dtype=complex);dx[-1]=-a*phi*T/2;dxp=np.zeros(15,dtype=complex);dxp[-1]=-a*phi/2
    source=-kappa*((lapT+2*G*up)*dxp+G*inv@Ci@dxp)+kappa*inv@R@dx
    explicit=3*kappa*dx-2*kappa*G*up*dxp-kappa*G*inv@Ci@dxp+kappa*inv@R@dx
    # The original coefficient law under a single link sign is tested in all 15 coordinates.
    if record:
        tag=f'four-link T{T}'
        eq(tag+' component ground equation',-kappa*(G*j['hij'][0,0]+(lapT+2*G*up)*j['hi'][0])+pot*h,np.zeros(16))
        eq(tag+' full connection Hamiltonian',ambient,full);eq(tag+' evaluated Hamiltonian',ambient,exact)
        eq(tag+' original face source',source,explicit)
        eq(tag+' all noncycle moments retained as zero',r[:-1],np.zeros(14));eq(tag+' physical zero coefficients',beta[:-1],np.zeros(14))
        eq(tag+' original source map',Xi@dx,h*(-a*phi*T*(chi-r[-1])/2))
        eq(tag+' original gradient map',Xi@beta,-2*kappa*G*j['hi'][0]*fprime)
        zero=-kappa*(G*Kp+lapT*K+G*K@K+2*G*up*K)+inv@(kappa*R/4+Xi.T@(pot[:,None]*Xi))
        eq(tag+' full zero order coefficient',zero,kappa*inv@R)
        for eps in [1,3,15]:
            perm=np.arange(16)^eps;E=H[eps]
            jt=jets(H,2*lam*chi*(chi[eps]*T),(2*lam*chi)[None,:],np.zeros((1,1,16)))
            eq(tag+f' frame transformation {eps}',jt['Xi'],Xi[perm]*E)
            eq(tag+f' covariance transformation {eps}',jt['C'],E[:,None]*C*E)
    qambient=kappa*G*np.vdot(vp,vp)+np.vdot(v,pot*v)
    qeval=kappa*(G*np.vdot(cp,C@cp)+G*abs(rp@c)**2)
    # Complete source energy, not a pointwise equality of the two densities.
    return A2*qambient,A2*qeval
for T in [-1.8,-.7,0.,.43,1.6]:oneface(T,True)
nodes,weights=roots_jacobi(120,.5,.5);both=np.array([oneface(2*t) for t in nodes])
eq('four-link complete integrated energy with radius-two Haar density',(2/np.pi)*weights@both[:,0],(2/np.pi)*weights@both[:,1])
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),scope='Full sign-character jets, covariance inverse, curvature, third moments, full zero-order identity and operator. Continuous four-link radius-two gauge-invariant constructed ground-state fixture retains every one of its 16 signs, 15 nonempty characters, ground-state normalization, E0, trace Casimir and Haar density. Its potential is constructed, not the Wilson potential; separate exact algebra diagnostics retain the full Wilson potential. No actual Wilson-vacuum samples, continuum limit or cross-source sign is inferred.',results=rows)
(O/'CHARACTER_OPERATOR_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='results'}))
print(json.dumps([r for r in rows if not r['passed']]))
assert out['all_passed']
