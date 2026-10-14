from pathlib import Path
import itertools,json,math
import numpy as np
from scipy.integrate import quad
O=Path(__file__).resolve().parent
checks=[]
def ck(name,condition,error=0):
 checks.append(dict(name=name,passed=bool(condition),error=float(error)))
 assert condition,(name,error)
def close(name,x,y,tol=2e-9):
 err=np.max(np.abs(np.asarray(x)-np.asarray(y)))
 ck(name,err<=tol*(1+np.max(np.abs(np.asarray(y)))),err)
rng=np.random.default_rng(61014)
sign=np.array(list(itertools.product([-1.,1.],repeat=3)))
characters=np.array([np.prod(sign[:,[k for k in range(3) if s>>k&1]],axis=1) for s in range(1,8)]).T
faces=characters[:,[0,1,3]]
for case in range(24):
 d=4+case%5;kappa=.7+.1*(case%4);b=.4+.2*(case%3);c=2*math.sqrt(b/kappa)
 prob=rng.uniform(.1,2.,8);prob/=prob.sum()
 potential=6*b-2*b*faces.sum(axis=1);E=.3*kappa*c*d
 ts=c*d+(potential-E)/(3*kappa)
 bs=[]
 for t in ts:
  q=rng.normal(size=(d,d));z=q@q.T;bs.append(t*z/np.trace(z))
 bs=np.array(bs);ks=bs-c*np.eye(d);kb=np.einsum('t,tij->ij',prob,ks);bb=kb+c*np.eye(d)
 ds=ks-kb;variance=np.einsum('t,tij,tjk->ik',prob,ds,ds)
 means=prob@faces;centered=faces-means;cov=centered.T@(prob[:,None]*centered)
 kr=2*np.einsum('t,tp,tij->pij',prob,centered,ds)
 tbar=prob@ts;U=c*d+(12*b-E)/(3*kappa)
 remainder=np.einsum('t,tij,tjk->ik',prob,bs,ts[:,None,None]*np.eye(d)-bs)
 formula=tbar*bb-bb@bb-b/(3*kappa)*kr.sum(axis=0)-remainder
 close(f'{case}: full original source remainder',variance,formula)
 ck(f'{case}: remainder positive',np.linalg.eigvalsh(remainder).min()>-1e-8)
 ck(f'{case}: full operator ceiling',np.linalg.eigvalsh(U*bb-bb@bb-variance).min()>-1e-8)
 ck(f'{case}: dimension-free operator ceiling',np.linalg.eigvalsh(U**2/4*np.eye(d)-variance).min()>-1e-8)
 ck(f'{case}: complete trace ceiling',np.trace(variance)<=(1-1/d)*U**2+1e-8)
 traceless=ds-(potential-prob@potential)[:,None,None]*np.eye(d)/(3*kappa*d)
 lower=8*b*b/(3*kappa*kappa*d)*cov.sum()+6*np.einsum('t,tij,tij->',prob,traceless,traceless)
 close(f'{case}: exact traceless defect',6*np.trace(variance),lower)
 inv=np.linalg.inv(cov)
 df=.5*np.einsum('tp,pq,qij->tij',centered,inv,kr);rest=ds-df
 vface=.25*np.einsum('pq,pij,qjk->ik',inv,kr,kr)
 close(f'{case}: full face projection',variance,vface+np.einsum('t,tij,tjk->ik',prob,rest,rest))
 close(f'{case}: omitted-face covariance zero',np.einsum('t,tp,tij->pij',prob,centered,rest),np.zeros((3,d,d)))
 phi=rng.normal(size=3)+1j*rng.normal(size=3);y=np.einsum('p,pij->ij',phi,kr)
 sig=(phi.conj()@cov@phi).real
 ck(f'{case}: complex original-source matrix bound',np.linalg.eigvalsh(4*sig*variance-y.conj().T@y).min()>-1e-7)
 f=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d));f=(f+f.T)/2
 z=sum(phi[p].conjugate()*np.trace(kr[p]@f) for p in range(3))
 ck(f'{case}: full complex contraction',abs(z)<=2*math.sqrt(sig*np.trace(variance))*np.linalg.norm(f)+1e-8)
 # Exact equality fixture for the trace ceiling: every rank-one direction
 # appears with its full equal probability. This is not an assigned vacuum.
 rank=np.array([U*np.diag(np.eye(d)[i]) for i in range(d)])
 rb=rank.mean(axis=0);rv=np.mean((rank-rb)@(rank-rb),axis=0)
 close(f'{case}: sharp trace fixture',np.trace(rv),(1-1/d)*U**2)

# Four original radius-two links, one full ordered loop. Integrating the other
# three Haar variables gives the actual SU(2) trace density, without a metric
# change. psi=exp(t T)/sqrt(Z), V=E+kappa Delta psi/psi is an explicit fixture.
haar=lambda x:math.sqrt(max(0.,4-x*x))/(2*math.pi)
for t in [.1,.3,.8,1.2]:
 for kappa in [.6,1.4]:
  norm=quad(lambda x:math.exp(2*t*x)*haar(x),-2,2,epsabs=1e-11)[0]
  mu=lambda fn:quad(lambda x:math.exp(2*t*x)*haar(x)*fn(x)/norm,-2,2,epsabs=1e-10)[0]
  amu=lambda fn:quad(lambda x:math.cosh(2*t*x)*haar(x)*fn(x)/norm,-2,2,epsabs=1e-10)[0]
  gamma=lambda x:4-x*x
  hnorm=lambda x:6+1.5*x*x
  ground=lambda x:t*t*hnorm(x)+.5*t*t*gamma(x)
  lapv=lambda x:kappa*(9*t*x+8*t*t*(x*x-1))
  tag=f'continuous t={t} kappa={kappa}'
  close(tag+': complete weighted Bochner',mu(ground),mu(lapv)/(2*kappa))
  meanhs=lambda x:t*t*math.tanh(2*t*x)**2*hnorm(x)
  varhs=lambda x:t*t/(math.cosh(2*t*x)**2)*hnorm(x)
  close(tag+': conditional Hessian squares',amu(lambda x:meanhs(x)+varhs(x)),mu(lambda x:t*t*hnorm(x)))
  score=lambda x:t*t*math.tanh(2*t*x)**2*gamma(x)
  fisher=lambda x:t*t/(math.cosh(2*t*x)**2)*gamma(x)
  close(tag+': full score decomposition',amu(lambda x:score(x)+fisher(x)),mu(lambda x:t*t*gamma(x)))
  for power in [2,4]:
   eta=lambda x:1+x**power
   de=lambda x:power*x**(power-1)
   dv=lambda x:kappa*(-3*t-2*t*t*x)
   dz=lambda x:-2*t*t*x
   rhs=mu(lambda x:eta(x)*lapv(x)/(2*kappa)+de(x)*gamma(x)*dv(x)/(2*kappa)-.5*de(x)*gamma(x)*dz(x))
   close(tag+f': full localization weight {power}',mu(lambda x:eta(x)*ground(x)),rhs)
   close(tag+f': central weighted conditional squares {power}',amu(lambda x:eta(x)*(meanhs(x)+varhs(x)+.5*(score(x)+fisher(x)))),mu(lambda x:eta(x)*ground(x)))

for j in [1,2,3,7,19]:
 for kappa in [.7,1.3,2.1]:
  a=1/(100*j);L=j**4;N=3*(2*L)*(2*L+1)**2;M=3*(2*L)**2*(2*L+1);nv=(2*L+1)**3;d=N-nv+1
  b=1/(kappa*a*a);c=2/(kappa*a);E=.25*b*M;U=c*d+(4*b*M-E)/(3*kappa)
  up=(320000*j**14+160000*j**10)/kappa**2+(3200*j**13+2400*j**9)/kappa
  ck(f'j{j} k{kappa}: all original counts',d==16*j**12+12*j**8 and M==24*j**12+12*j**8)
  close(f'j{j} k{kappa}: original-energy ceiling',U,up-E/(3*kappa))
  close(f'j{j} k{kappa}: global square bound',3*b*M/kappa,(720000*j**14+360000*j**10)/kappa**2)
r=dict(all_passed=all(x['passed'] for x in checks),checks=len(checks),scope='Noncommuting positive-matrix and full covariance fixtures, including sharp trace equality; continuous original-radius-two four-link Haar integrals with explicitly constructed potential and every localized derivative term; exact original regulator counts and retained energy constants. None is a sampled Wilson vacuum. Complete written proofs establish original-state claims.',results=checks)
(O/'HESSIAN_BOUNDS_CHECKS.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in r.items() if k!='results'}))
