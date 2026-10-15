from pathlib import Path
import json,itertools
import numpy as np
import sympy as s
from scipy.special import roots_chebyu,roots_legendre
O=Path(__file__).resolve().parent;rows=[];rng=np.random.default_rng(2026101503)
def yes(name,b):rows.append(dict(name=name,passed=bool(b)))
def eq(name,x,y,tol=2e-10):
 err=float(np.max(abs(np.asarray(x)-np.asarray(y))));scale=1+float(np.max(abs(x)))+float(np.max(abs(y)))
 rows.append(dict(name=name,passed=err<=tol*scale,error=err))
a,k,c=s.symbols('a k c',positive=True);t,d=s.symbols('t d',positive=True)
alpha=4*k*a*a/(7+16*c);cov=alpha**2/(21*k*k*a*a/4+k*(s.Rational(1,2)+2*c)*alpha)
yes('exact covariance constant',s.cancel(cov-64*a*a/((7+16*c)*(155+368*c)))==0)
yes('full original parameter dictionary',s.cancel(cov.subs(c,2/(k*a))-64*k*k*a**4/((32+7*k*a)*(736+155*k*a)))==0)
yes('full covariance floor coefficient',s.limit(cov.subs(c,2/(k*a))/a**4,a,0)==k*k/368)
fun=(3*t-d)**2/((s.Rational(3,2)+6*c)*t+(s.Rational(1,4)-2*c)*d)
yes('retained deficit monotonic derivative',s.cancel(s.diff(fun,d)+4*(3*t-d)*((15+24*c)*t+(1-8*c)*d)/((6+24*c)*t+(1-8*c)*d)**2)==0)
yes('universal first moment substitution',s.cancel(k*a*a*fun.subs(d,t)/4-alpha*t)==0)
yes('smooth coefficient limit',s.limit((k*a*a*fun.subs({c:2/(k*a),t:1/a**3,d:1/a**2})/4),a,0)==3*k*k/16)
# Coupled positive densities on two radius-two factors; these are not Yang-Mills vacua.
nodes,weights=roots_chebyu(70);u,wu=roots_legendre(80)
r1=np.sqrt(1-nodes[:,None,None]**2);r2=np.sqrt(1-nodes[None,:,None]**2)
dot=r1*r2*u[None,None,:];base=(2/np.pi)**2*weights[:,None,None]*weights[None,:,None]*wu[None,None,:]/2
samples=[]
for strength in [.2,1.,4.,12.]:
 density=np.exp(2*strength*dot);norm=np.sum(base*density);prob=base*density/norm;cval=strength/2
 for gam in [-1.,1.,.3+.7j]:
  F2=r1*r1+abs(gam)**2*r2*r2+2*np.real(gam)*dot
  A=((3-r1*r1)+abs(gam)**2*(3-r2*r2))/4
  B=3*(r1*r1+abs(gam)**2*r2*r2)/16
  coeff=.75+strength*dot/2;p=coeff-gam*strength/2;q=gam*coeff-strength/2
  DF2=abs(p)**2*r1*r1+abs(q)**2*r2*r2+2*np.real(np.conj(p)*q)*dot
  inner=np.real(p*r1*r1+np.conj(gam)*q*r2*r2+(q+np.conj(gam)*p)*dot)
  hess=-strength*dot*((3-r1*r1)+abs(gam)**2*(3-r2*r2))/16+strength*np.real(gam)*(3-r1*r1-r2*r2+dot*dot)/8
  mean=lambda f:float(np.sum(prob*f))
  va,aa,bb,dd=map(mean,[F2,A,B,DF2])
  eq(f'coupled {strength} {gam} integration by parts',mean(inner),aa,2e-9)
  eq(f'coupled {strength} {gam} full weighted Bochner',dd,mean(B+A/2-2*hess),2e-9)
  yes(f'coupled {strength} {gam} Hessian upper receiver',dd<=bb+(.5+2*cval)*aa+1e-8)
  yes(f'coupled {strength} {gam} exact conditional variance bound',va+1e-10>=aa*aa/(bb+(.5+2*cval)*aa))
  floor=4*(1+abs(gam)**2)/(7+16*cval)
  yes(f'coupled {strength} {gam} polynomial raw coefficient floor',va+1e-10>=floor)
  samples.append(dict(strength=strength,gamma=str(gam),partition=norm,actual_fixture_variance=va,proved_floor=floor))
# Original box geometry and full source derivative tensors.
pauli=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]]);gen=-.5j*pauli
def su():
 v=rng.normal(size=4);v/=np.linalg.norm(v);return v[0]*np.eye(2)-1j*np.einsum('i,ijk->jk',v[1:],pauli)
def mul(items):
 out=np.eye(2,dtype=complex)
 for v in items:out=out@v
 return out
for side in [2,3]:
 verts=list(itertools.product(range(side+1),repeat=3));edges=[]
 for v in verts:
  for ax in range(3):
   if v[ax]<side:edges.append((v,ax))
 idx={e:i for i,e in enumerate(edges)};faces=[]
 for v in verts:
  for d1,d2 in itertools.combinations(range(3),2):
   if v[d1]<side and v[d2]<side:
    vd=list(v);vd[d1]+=1;ve=list(v);ve[d2]+=1
    faces.append([(idx[(v,d1)],1),(idx[(tuple(vd),d2)],1),(idx[(tuple(ve),d1)],-1),(idx[(v,d2)],-1)])
 incident=[[] for e in edges]
 for p,f in enumerate(faces):
  for e,sg in f:incident[e].append(p)
 yes(f'box{side} exact edge count',len(edges)==3*side*(side+1)**2)
 yes(f'box{side} exact face count',len(faces)==3*side**2*(side+1))
 yes(f'box{side} all four incidence contributions',sum(map(len,incident))==4*len(faces))
 yes(f'box{side} every noncommon star edge disjoint',all(len({e2 for p in ps for e2,sg in faces[p] if e2!=e})==3*len(ps) for e,ps in enumerate(incident)))
 for case in range(3):
  us=[su() for e in edges];phi=rng.normal(size=len(faces))+1j*rng.normal(size=len(faces));aj=.07
  grad=np.zeros((len(edges),3),complex);hess=np.zeros((len(edges),3,len(edges),3),complex);traces=[];gg=0.
  for p,f in enumerate(faces):
   mats=[us[e] if sg==1 else us[e].conj().T for e,sg in f];T=float(np.trace(mul(mats)).real);traces.append(T)
   ders=[np.array([g@mats[r] if sg==1 else -mats[r]@g for g in gen]) for r,(e,sg) in enumerate(f)]
   for r,(e,sg) in enumerate(f):
    for al in range(3):
     qmat=mats.copy();qmat[r]=ders[r][al];grad[e,al]-=aj*phi[p]*np.trace(mul(qmat)).real/2
    hess[e,:,e,:]+=aj*phi[p]*T*np.eye(3)/8
    for ss,(ef,sgf) in enumerate(f):
     if r==ss:continue
     for al in range(3):
      for be in range(3):
       qmat=mats.copy();qmat[r]=ders[r][al];qmat[ss]=ders[ss][be]
       hess[e,al,ef,be]-=aj*phi[p]*np.trace(mul(qmat)).real/2
  traces=np.array(traces)
  exact=aj*aj/4*(3/16*sum(abs(sum(phi[p]*traces[p] for p in ps))**2 for ps in incident)+sum(abs(phi)**2*(6+.75*traces**2)))
  eq(f'box{side}case{case} full complex Hessian identity',np.sum(abs(hess)**2),exact)
  eq(f'box{side}case{case} covariant Hessian symmetry',hess,hess.transpose(2,3,0,1))
  yes(f'box{side}case{case} retained Hessian upper bound',exact<=21*aj*aj*np.sum(abs(phi)**2)/4+1e-10)
  yes(f'box{side}case{case} complete gradient upper bound',np.sum(abs(grad)**2)<=4*aj*aj*np.sum(abs(phi)**2)+1e-10)
# Finite positive spectral moment fixtures with all matrix mixed terms.
for case in range(15):
 n=5;dim=13;ev=np.r_[0.,rng.uniform(.05,5,dim-1)];Z=rng.normal(size=(dim,n))+1j*rng.normal(size=(dim,n));Z[0]=0
 S=Z.conj().T@Z;M1=Z.conj().T@(ev[:,None]*Z);M2=Z.conj().T@(ev[:,None]**2*Z)
 lo=np.linalg.eigvalsh(M1).min();bb=.7;aa=max(.01,np.linalg.eigvalsh(M2-bb*M1).max())
 yes(f'matrix{case} energy-dependent covariance lower floor',np.linalg.eigvalsh(S-lo*lo/(aa+bb*lo)*np.eye(n)).min()>-1e-8)
 Y=rng.normal(size=(dim,3))+1j*rng.normal(size=(dim,3));Y[0]=0;Y=np.c_[Y,Y[:,0]-2*Y[:,1]]
 G=Y.conj().T@Y;H=Y.conj().T@Z;E=S-H.conj().T@np.linalg.pinv(G)@H
 _,sv,Vh=np.linalg.svd(H,full_matrices=True);rank=np.sum(sv>1e-9);ker=Vh.conj().T[:,rank:]
 eq(f'matrix{case} complete missing-trial covariance',ker.conj().T@E@ker,ker.conj().T@S@ker)
 yes(f'matrix{case} missing-trial trace lower bound',np.trace(E).real+1e-8>=(n-np.linalg.matrix_rank(G))*np.linalg.eigvalsh(S).min())
paths=[]
for j in [1,5,10,100,1000]:
 kap=.8;aj=1/(100*j);cv=2/(kap*aj);AA=4*kap*aj*aj/(7+16*cv);sigma=64*aj*aj/((7+16*cv)*(155+368*cv))
 paths.append(dict(j=j,a=aj,c=cv,first_floor_per_coefficient=AA,covariance_floor_per_coefficient=sigma,first_floor_over_a3=AA/aj**3,covariance_floor_over_a4=sigma/aj**4))
out=dict(checks=len(rows),all_passed=all(r['passed'] for r in rows),scope='Exact algebra; constructed coupled positive densities, not Yang-Mills ground samples; full original link Hessian fixtures; finite spectral moment matrices; original bound formulas.',conditional_samples=samples,original_path=paths,rows=rows)
(O/'SPATIAL_MOMENT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ['checks','all_passed']}));assert out['all_passed'],[r for r in rows if not r['passed']]
