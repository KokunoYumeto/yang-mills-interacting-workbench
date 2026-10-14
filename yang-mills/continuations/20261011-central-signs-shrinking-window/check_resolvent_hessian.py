from pathlib import Path
import json,math
import numpy as np
from scipy.integrate import quad
O=Path(__file__).resolve().parent;checks=[]
def ck(n,p,e=0):
 checks.append(dict(name=n,passed=bool(p),error=float(e)));assert p,(n,e)
def close(n,a,b,tol=2e-8):
 e=abs(a-b);ck(n,e<=tol*(1+abs(b)),e)
def bound(alpha,z):return 1. if alpha<=2*z else alpha**2/(4*z*(alpha-z))
for z in [.03,.4,1.,9.]:
 for alpha in [-20.,0.,z,2*z,2.01*z,3*z,19*z]:
  m=bound(alpha,z);lam=np.r_[0.,np.geomspace(z*1e-7,z*1e7,1500)]
  ratio=(lam*lam+alpha*lam)/(lam+z)**2
  ck(f'spectral alpha{alpha} z{z}',ratio.max()<=m+1e-10)
  if alpha>2*z:
   q=alpha*z/(alpha-2*z);close(f'exact maximizer alpha{alpha} z{z}',(q*q+alpha*q)/(q+z)**2,m)
  for k in [1,2,3]:
   ck(f'derivative k{k} alpha{alpha} z{z}',np.max(ratio/(lam+z)**(2*k))<=m/z**(2*k)*(1+1e-12))
haar=lambda x:math.sqrt(max(0.,4-x*x))/(2*math.pi)
for t in [.2,.7,1.1]:
 norm=quad(lambda x:math.cosh(2*t*x)*haar(x),-2,2,epsabs=1e-11)[0]
 integ=lambda f:quad(lambda x:float(np.real(f(x)))*math.cosh(2*t*x)*haar(x)/norm,-2,2,epsabs=1e-9)[0]
 up=lambda x:t*math.tanh(2*t*x)
 upp=lambda x:2*t*t/math.cosh(2*t*x)**2
 gamma=lambda x:4-x*x
 for coeff in [(1.+.3j,.2-.1j),(.7-.4j,-.05+.06j)]:
  a,b=coeff;mean=integ(lambda x:a.real*x*x+b.real*x**4)+1j*integ(lambda x:a.imag*x*x+b.imag*x**4)
  f=lambda x:a*x*x+b*x**4-mean
  fp=lambda x:2*a*x+4*b*x**3
  fpp=lambda x:2*a+12*b*x*x
  df2=lambda x:abs(fp(x))**2*gamma(x)
  hs=lambda x:abs(fp(x))**2*(6+1.5*x*x)-2*(fp(x).conjugate()*fpp(x)).real*x*gamma(x)+abs(fpp(x))**2*gamma(x)**2
  uh=lambda x:abs(fp(x))**2*(-up(x)*x*gamma(x)+upp(x)*gamma(x)**2)
  D=lambda x:gamma(x)*fpp(x)-3*x*fp(x)+2*up(x)*gamma(x)*fp(x)
  close(f't{t} coeff{coeff} global Bochner',integ(hs),integ(lambda x:abs(D(x))**2+2*uh(x)-.5*df2(x)))
  for power in [2,4]:
   eta=lambda x:1+x**power;ep=lambda x:power*x**(power-1);epp=lambda x:power*(power-1)*x**(power-2)
   De=lambda x:gamma(x)*epp(x)-3*x*ep(x)+2*up(x)*gamma(x)*ep(x)
   rhs=lambda x:eta(x)*(abs(D(x))**2+2*uh(x)-.5*df2(x))+.5*df2(x)*De(x)+(D(x)*ep(x)*fp(x).conjugate()*gamma(x)).real
   close(f't{t} coeff{coeff} localization{power}',integ(lambda x:eta(x)*hs(x)),integ(rhs))
  # Exact resolvent fixture: x_z=(L_A+z)f, so f is the actual
  # resolvent of this constructed source at this original metric.
  # This is not a Wilson ground-state sample or original X_phi sample.
  for kappa in [.7,1.8]:
   c=2*t;G=4*math.pi**2*4*c*c
   C=6*t+4*t*t+G+11*c
   alpha=kappa*(2*C-.5)
   for z in [.1,.8,3.]:
    source=lambda x:-kappa*D(x)+z*f(x)
    source_norm=integ(lambda x:abs(source(x))**2)
    ck(f't{t} k{kappa} z{z} c{coeff} actual resolvent Hessian',integ(hs)<=bound(alpha,z)/kappa**2*source_norm+1e-8)
    ck(f't{t} k{kappa} z{z} c{coeff} exact spectral gradient bound',integ(df2)<=source_norm/(4*kappa*z)+1e-8)
    s=lambda x:t*t/math.cosh(2*t*x)**2*abs(fp(x))**2*gamma(x)**2
    ck(f't{t} k{kappa} z{z} c{coeff} complete coupling',4*kappa*kappa*integ(s)<=kappa*G/z*source_norm+1e-8)
for j in [1,2,5,11]:
 for kappa in [.8,1.7]:
  L=j**4;a=1/(100*j);b=1/(kappa*a*a);N=3*(2*L)*(2*L+1)**2;M=3*(2*L)**2*(2*L+1);c=2/(kappa*a)
  C=4*b*M/kappa+4*math.pi**2*N*c*c+(3*N-1)*c
  expanded=(960000*j**14+480000*j**10+160000*math.pi**2*N*j*j)/kappa**2+200*j*(3*N-1)/kappa
  close(f'j{j} k{kappa} entire original ceiling',C,expanded)
  ck(f'j{j} k{kappa} dimension retained',N==24*j**12+24*j**8+6*j**4)
r=dict(all_passed=all(x['passed'] for x in checks),checks=len(checks),scope='Exact rational spectral multiplier and derivative inequalities; continuous four-link original-radius-two conditional density with constructed potential and complex sources, full Bochner/localization identities, actual resolvent fixture and complete coupling; original regulator counts. Not sampled Wilson vacua and not evaluation of original limiting spectral mass.',results=checks)
(O/'RESOLVENT_HESSIAN_CHECKS.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in r.items() if k!='results'}))
