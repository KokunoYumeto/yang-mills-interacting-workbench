"""Independent finite algebra and original-coordinate spatial diagnostics.

No finite array here approximates the interacting Yang--Mills ground state.
The actual-state deficit bounds and operator limits are proved in the note.
"""
from pathlib import Path
import itertools,json,math
import numpy as np
from numpy.polynomial import Polynomial
O=Path(__file__).resolve().parent
rng=np.random.default_rng(6131013)
checks=[]
def ck(name,ok,**data):
    assert bool(ok),(name,data)
    checks.append(dict(name=name,passed=True,**data))
def close(name,x,y,tol=2e-10):
    err=float(np.max(np.abs(np.asarray(x)-np.asarray(y))))
    scale=max(1.,float(np.max(np.abs(np.asarray(y)))))
    ck(name,err<=tol*scale,error=err,scale=scale)

# Adjoint Casimir in the original orthonormal Pauli frame.
for n in range(24):
    v=rng.normal(size=3)+1j*rng.normal(size=3)
    close('Pauli adjoint Casimir '+str(n),
          sum(np.linalg.norm(np.cross(t,v))**2 for t in np.eye(3)),
          2*np.linalg.norm(v)**2)

# Full exterior Hessian action compared with the block formula, complex lists.
for n in range(20):
    m=5;dim=3*m
    h=rng.normal(size=(dim,dim));h=(h+h.T)/2
    v=rng.normal(size=(dim,dim));v=(v+v.T)/2
    c=rng.normal(size=m)+1j*rng.normal(size=m)
    kapp=0.3+2*rng.random()
    delta=np.repeat(c,3)[None,:]-np.repeat(c,3)[:,None]
    for source,label in [(h,'current'),(v,'force')]:
        omega=delta*source
        action=-2*kapp*(h@omega+omega@h)
        for e in range(m):
            sl=slice(3*e,3*e+3); expected=np.zeros((3,3),complex)
            for f in range(m):
                if f==e:continue
                sf=slice(3*f,3*f+3)
                hef=h[sl,sf];wef=omega[sl,sf]
                expected+=2*kapp*(hef@wef.T-wef@hef.T)
            close(label+' full diagonal action '+str((n,e)),action[sl,sl],expected)
            if label=='current':close('current diagonal cancellation '+str((n,e)),expected,0)
        close(label+' antisymmetry '+str(n),omega.T,-omega)

# All six pairs, including the last parity-sum term.
for n in range(24):
    v=rng.normal(size=4)+1j*rng.normal(size=4)
    total=sum(abs(v[e]-v[f])**2 for e,f in itertools.combinations(range(4),2))
    exact=2*abs(v[0]-v[1])**2+2*abs(v[2]-v[3])**2+abs(v[0]+v[1]-v[2]-v[3])**2
    close('six-pair identity '+str(n),total,exact)

# Positive spectral measures test inverse moments, both scale maps and Jensen.
for j in [2,3,4,6]:
    a=1/(100*j);kapp=1.7;s=100*kapp*a
    for n in range(10):
        lam=np.exp(rng.uniform(-5,6,size=15));weights=np.exp(rng.normal(size=15))
        omega=float(weights.sum());energy=float(weights@lam)
        raw_n=kapp*a**4*float(weights@(lam**-3))
        ck('inverse-third Jensen '+str((j,n)),raw_n+1e-16>=kapp*a**4*omega**4/energy**3)
        # Cell quadratic factor is a^3 times the displayed operator coefficient.
        force_atoms=a**7*weights
        removed_atoms=kapp*a**4*weights*lam**-3
        close('time-scale factor '+str((j,n)),force_atoms,1e6*kapp*kapp*a**6*(lam/s)**3*removed_atoms)
        close('force-scale factor '+str((j,n)),force_atoms,(a*lam)**3/kapp*removed_atoms)
        third=float(removed_atoms@(lam**3))
        mass=float(removed_atoms.sum())
        first=float(removed_atoms@lam);second=float(removed_atoms@(lam**2))
        ck('first-moment Holder '+str((j,n)),first<=mass**(2/3)*third**(1/3)*(1+1e-12))
        ck('second-moment Holder '+str((j,n)),second<=mass**(1/3)*third**(2/3)*(1+1e-12))
        close('common cubic scale '+str((j,n)),removed_atoms@((a**(1/3)*lam)**3),kapp*a**-2*force_atoms.sum())
        eps=float(np.median(a*lam))
        ck('force small-energy estimate '+str((j,n)),
           force_atoms[a*lam<=eps].sum()<=eps**3/kapp*removed_atoms.sum()+1e-16)

# Original physical coordinates and original path. Q=[-.05,.05]^3.
# The polynomial C1 bump has compact support [-.04,.04]^3.
length=.04;kapp=1.7;R=.1
f=Polynomial([1,0,-2,0,1]);integral_f2=(f*f).integ()
integral_df2=(f.deriv()*f.deriv()).integ()
i0=length*(integral_f2(1)-integral_f2(-1))
i1=(integral_df2(1)-integral_df2(-1))/length
gradient_integral=3*i1*i0*i0
phi2_integral=i0**3
primitive=f.integ()
def phi(x,a,averaged):
    if averaged:
        upper=np.clip((x+a/2)/length,-1,1)
        lower=np.clip((x-a/2)/length,-1,1)
        factors=length/a*(primitive(upper)-primitive(lower))
    else:
        t=x/length
        factors=np.where(np.abs(t)<1,(1-t*t)**2,0)
    return np.prod(factors,axis=-1)
direction=np.array([1+.2j,-.4+.3j,.8-.7j])
orientation_target=3/kapp**2*sum(abs(direction[d]-direction[k])**2 for d,k in itertools.combinations(range(3),2))*phi2_integral
common_target=3/kapp**2*gradient_integral
spatial=[]
for j in [2,3,4,6]:
    a=1/(100*j);L=j**4;q=math.ceil(R/a)+3
    vq=L+math.floor(-.05/a)-1
    ck('original fitting cube '+str(j),vq>0 and vq+q<2*L,a=a,L=L,q=q,vq=vq)
    energies=dict(common_sample=0.,common_average=0.,direction_average=0.)
    for d,k in itertools.combinations(range(3),2):
        other=3-d-k
        lengths=[q+1 if axis==other else q for axis in range(3)]
        z=np.stack(np.meshgrid(*(np.arange(t)+vq for t in lengths),indexing='ij'),axis=-1).reshape(-1,3)
        xp=a*(z-L+(np.eye(3)[d]+np.eye(3)[k])/2)
        centers=[xp-a*np.eye(3)[k]/2,xp+a*np.eye(3)[k]/2,xp-a*np.eye(3)[d]/2,xp+a*np.eye(3)[d]/2]
        sam=np.stack([phi(x,a,False) for x in centers],axis=-1)
        avg=np.stack([phi(x,a,True) for x in centers],axis=-1)
        orient=avg*np.array([direction[d],direction[d],direction[k],direction[k]])
        for name,values in [('common_sample',sam),('common_average',avg),('direction_average',orient)]:
            total=sum(float(np.sum(np.abs(values[:,e]-values[:,f])**2)) for e,f in itertools.combinations(range(4),2))
            energies[name]+=.75*a**3/kapp**2*total
    row=dict(j=j,a=a,common_sample=energies['common_sample']/a**2,
             common_average=energies['common_average']/a**2,
             common_target=common_target,direction_average=energies['direction_average'],
             direction_target=orientation_target)
    spatial.append(row)
for name,target in [('common_sample',common_target),('common_average',common_target),('direction_average',orientation_target)]:
    errs=[abs(row[name]-target)/target for row in spatial]
    ck(name+' convergence on original meshes',all(errs[i+1]<errs[i] for i in range(3)) and errs[-1]<.006,relative_errors=errs)
close('orientation operator eigenvalues',np.linalg.eigvalsh(3/kapp**2*(3*np.eye(3)-np.ones((3,3)))),[0,9/kapp**2,9/kapp**2])
close('orientation kernel', (3*np.eye(3)-np.ones((3,3)))@np.ones(3),np.zeros(3))
result=dict(checks=len(checks),all_passed=True,scope=__doc__.strip(),rows=checks,spatial_convergence=spatial,
            spatial_method='Exact full six-pair sums on original fitting face grids, with original a_j and L_j; exact cell averages of a specified C1 polynomial bump. Comparison face weight 3/4 only. Actual interacting-state convergence follows from the written retained deficit estimate, not these samples.')
(O/'TWO_FORM_FORCE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(checks),all_passed=True,spatial=spatial)))
