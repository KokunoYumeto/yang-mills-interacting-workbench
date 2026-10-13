"""Original SU(2) plaquette derivatives and independent spectral diagnostics.
Configurations and spectral arrays test universal identities, not the vacuum.
"""
from pathlib import Path
import itertools,json,numpy as np
O=Path(__file__).resolve().parent;rng=np.random.default_rng(6131326);rows=[]
def ck(n,x,y):
    err=float(np.linalg.norm(np.asarray(x)-np.asarray(y)));scale=1+float(np.linalg.norm(y))
    assert err<2e-10*scale,(n,err)
    rows.append(dict(name=n,error=err))
def bound(n,x,y):
    assert x<=y+2e-10*(1+abs(y)),(n,x,y)
    rows.append(dict(name=n,left=float(x),right=float(y)))
T=np.array([[[0,-1j/2],[-1j/2,0]],[[0,-.5],[.5,0]],[[-1j/2,0],[0,1j/2]]])
def prod(xs):
    v=np.eye(2,dtype=complex)
    for x in xs:v=v@x
    return v
nside=3;verts=list(itertools.product(range(nside+1),repeat=3))
edges=[(z,d) for z in verts for d in range(3) if z[d]<nside];ind={v:i for i,v in enumerate(edges)}
faces=[]
for z in verts:
    for d,k in itertools.combinations(range(3),2):
        if z[d]>=nside or z[k]>=nside:continue
        zd=list(z);zd[d]+=1;zk=list(z);zk[k]+=1
        ids=[ind[(z,d)],ind[(tuple(zd),k)],ind[(tuple(zk),d)],ind[(z,k)]]
        faces.append((ids,np.array(z)+(np.eye(3)[d]+np.eye(3)[k])/2))
for case in range(3):
    U=[]
    for edge in edges:
        p=rng.normal(size=4);p/=np.linalg.norm(p)
        U.append(p[0]*np.eye(2)+2*sum(p[k+1]*T[k] for k in range(3)))
    if case==2:U=[np.eye(2,dtype=complex) for _ in edges]
    deriv=[];deficits=[]
    for ids,xp in faces:
        fac=[U[ids[0]],U[ids[1]],U[ids[2]].conj().T,U[ids[3]].conj().T]
        deficit=2-np.trace(prod(fac)).real;grad=np.zeros((4,3))
        for p in range(4):
            for k in range(3):
                fs=fac.copy();fs[p]=T[k]@fac[p] if p<2 else -fac[p]@T[k]
                grad[p,k]=-np.trace(prod(fs)).real
        ck('four original edge-gradient norms '+str((case,len(deriv))),np.sum(grad*grad,axis=1),np.repeat(deficit-deficit**2/4,4))
        deriv.append(grad);deficits.append(deficit)
    c=rng.normal(size=len(edges))+1j*rng.normal(size=len(edges))
    a=1/300;kapp=1.7;b=1/(kapp*a*a)
    F=np.zeros((len(edges),3),complex);dW=F.copy();res=F.copy();upper=0
    phi_p=rng.normal(size=len(faces))+1j*rng.normal(size=len(faces))
    v=F.copy();err=F.copy()
    for p,((ids,xp),grad,dp) in enumerate(zip(faces,deriv,deficits)):
        avg=np.mean(c[ids]);dif=c[ids]-avg
        F[ids]+=b*c[ids,None]*grad;dW[ids]+=b*avg*grad;res[ids]+=b*dif[:,None]*grad
        G=sum(abs(c[ids[e]]-c[ids[f]])**2 for e,f in itertools.combinations(range(4),2))
        upper+=b*b*(dp-dp*dp/4)*G
        v[ids]+=a/2*phi_p[p]*grad;err[ids]+=a/2*(phi_p[p]-c[ids,None])*grad
    ck('exact force-gradient defect '+str(case),F-dW,res)
    bound('full force-defect covariance bound '+str(case),np.linalg.norm(res)**2,upper)
    ck('original source-force factor '+str(case),v,kapp*a**3/2*F+err)

for j in [2,5,19]:
    a=1/(100*j);kapp=1.7;s=100*kapp*a
    lam=np.array([s*.07,s*.6,s*1.3,s*4.,.5,3.,1/a,7/a])
    alpha=rng.normal(size=8)+1j*rng.normal(size=8);alpha/=np.linalg.norm(alpha)
    v=rng.normal(size=8)+1j*rng.normal(size=8)
    error=a*(rng.normal(size=8)+1j*rng.normal(size=8))/9
    q=-v-kapp*a/2*lam*alpha+error
    ck('complete signed spectral identity '+str(j),v+q,-kapp*a/2*lam*alpha+error)
    for cutoff in [s,.5,4.]:
        pick=lam<=cutoff
        eta=kapp*a*cutoff/2*np.linalg.norm(alpha)+np.linalg.norm(error)
        bound('full-band vector comparison '+str((j,cutoff)),np.linalg.norm((v+q)[pick]),eta)
        bound('full-band mass comparison '+str((j,cutoff)),abs(np.linalg.norm(v[pick])**2-np.linalg.norm(q[pick])**2),eta*(2*np.linalg.norm(v)+eta))
    theta=.8;eps=.3;win=5.;vals=[];bounds=[]
    for beta in [theta,eps*theta,win*theta]:
        uv=s/(lam+beta*s)*v;uq=s/(lam+beta*s)*q
        D=kapp*a*s/2*np.linalg.norm(alpha)+np.linalg.norm(error)/beta
        B=D*(2*np.linalg.norm(v)+beta*D)
        bound('whole resolvent vector comparison '+str((j,beta)),np.linalg.norm(uv+uq),D)
        bound('whole squared response comparison '+str((j,beta)),abs(beta*(np.linalg.norm(uv)**2-np.linalg.norm(uq)**2)),B)
        vals.append(beta*(np.linalg.norm(uv)**2-np.linalg.norm(uq)**2));bounds.append(B)
    coeff=np.array([1,-4*eps/(1+eps)**2,-4*win/(1+win)**2])
    bound('original three signed shifts '+str(j),abs(coeff@vals),abs(coeff)@bounds)
result=dict(checks=len(rows),all_passed=True,scope=__doc__.strip(),rows=rows)
(O/'COMMON_SOURCE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
