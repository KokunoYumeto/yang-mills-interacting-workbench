from pathlib import Path
import itertools,json,math
import numpy as np
from scipy.integrate import quad
import mpmath as mp
O=Path(__file__).resolve().parent;checks=[]
def ck(n,p,e=0):
 checks.append(dict(name=n,passed=bool(p),error=float(e)));assert p,(n,e)
def close(n,a,b,tol=2e-8):
 err=abs(a-b);ck(n,err<=tol*(1+abs(b)),err)
mp.mp.dps=65
q0=math.sqrt(1-math.exp(-1))
def M(alpha,z):return 1. if alpha<=2*z else alpha*alpha/(4*z*(alpha-z))
for kap in [.4,1.2,2.]:
 for omega in [.5,3.,17.]:
  time=1/(2*kap*omega)
  # Substitute s=v^2 to resolve the original square-root endpoint.
  value=quad(lambda v:math.sqrt(omega/(-math.expm1(-2*kap*omega*v*v)))*2*v if v else math.sqrt(2/kap),0,math.sqrt(time),epsabs=1e-10)[0]
  close(f'heat integral k{kap} w{omega}',value,math.atanh(q0)/(kap*math.sqrt(omega)))
  for time in [.01,.2,2.]:
   trace=np.linspace(-2,2,101)
   variance=1+np.exp(-8*kap*time)*(trace*trace-1)-np.exp(-6*kap*time)*trace*trace
   lower=-math.expm1(-2*kap*omega*time)/omega*np.exp(-6*kap*time)*(4-trace*trace)
   ck(f'original Haar heat reverse variance k{kap} w{omega} t{time}',np.min(variance-lower)>-1e-10)
haar=lambda x:math.sqrt(max(0.,4-x*x))/(2*math.pi)
for t in [.1,.3,.8]:
 norm=quad(lambda x:math.cosh(2*t*x)*haar(x),-2,2,epsabs=1e-11)[0]
 integ=lambda f:quad(lambda x:float(np.real(f(x)))*math.cosh(2*t*x)*haar(x)/norm,-2,2,epsabs=1e-9)[0]
 mean2=integ(lambda x:x*x)
 for kap in [.7,1.6]:
  N=4;nf=1;b=kap*(3*t+2*t*t);E=2*b;c=2*math.sqrt(b/kap)
  # V=E+kappa[-3tT+t^2(4-T^2)] is explicitly constructed,
  # lies in [0,4b], and is not the Wilson potential.
  G=4*math.pi**2*N*c*c;W=4*b/kap+(3*N-1)*c;C=W+G;Hh=2*W+5*G
  omega=2*C+.5;Omega=8*math.pi**2*c*N
  a=.01;phi=.8+.3j;beta=-a*phi/2;nu=.03+.01j
  f=lambda x:nu*(x*x-mean2)
  fp=lambda x:2*nu*x
  fpp=lambda x:2*nu
  gamma=lambda x:4-x*x
  up=lambda x:t*math.tanh(2*t*x)
  upp=lambda x:2*t*t/math.cosh(2*t*x)**2
  D=lambda x:gamma(x)*fpp(x)-3*x*fp(x)+2*up(x)*gamma(x)*fp(x)
  Dp=lambda x:-2*x*fpp(x)-3*fp(x)-3*x*fpp(x)+2*upp(x)*gamma(x)*fp(x)-4*up(x)*x*fp(x)+2*up(x)*gamma(x)*fpp(x)
  for z in [.08,.7,2.]:
   xfun=lambda x:-kap*D(x)+z*f(x)
   xd=lambda x:-kap*Dp(x)+z*fp(x)
   # Z=x+beta(T-T tanh(2tT)) has conditional mean exactly x.
   # Therefore f is its actual marginal resolvent at z.
   Z=lambda x:xfun(x)+beta*x*(1-math.tanh(2*t*x))
   Zd=lambda x:xd(x)+beta*(1-math.tanh(2*t*x)-2*t*x/math.cosh(2*t*x)**2)
   Zcap=abs(nu)*(kap*(32+32*t)+4*z)+4*abs(beta)
   Dcap=2*(abs(nu)*(kap*(32+48*t+64*t*t)+4*z)+abs(beta)*(2+4*t))
   gradcap=Zcap*(math.sqrt(omega)/(z*q0)+2*math.atanh(q0)/(kap*math.sqrt(omega)))
   alpha=kap*(2*C-.5)
   energycap=kap*(2*Dcap+2*Zcap*math.sqrt(G)+Zcap*(W+C)*math.sqrt(kap/z)+2*Zcap*math.sqrt(G*M(alpha,z)))**2
   def ys(x,sgn):
    return beta*x*(sgn-math.tanh(2*t*x))+2*kap*(sgn*t-up(x))*fp(x)*gamma(x)
   def dys(x,sgn):
    return beta*(sgn-math.tanh(2*t*x)-2*t*x/math.cosh(2*t*x)**2)+2*kap*(-upp(x)*fp(x)*gamma(x)+(sgn*t-up(x))*(fpp(x)*gamma(x)-2*x*fp(x)))
   def cond(x,fn):
    return sum(math.exp(2*sgn*t*x)/(2*math.cosh(2*t*x))*fn(sgn) for sgn in [-1,1])
   mass=integ(lambda x:cond(x,lambda s:abs(ys(x,s))**2))
   energy=kap*integ(lambda x:cond(x,lambda s:abs(dys(x,s))**2)*gamma(x))
   tag=f'continuous t{t} k{kap} z{z}'
   ck(tag+' energy ceiling',0<=energy<=energycap)
   close(tag+' original conditional source',integ(lambda v:abs(cond(v,lambda s:Z(s*v))-xfun(v))**2),0)
   samples=np.linspace(-2,2,201)
   ck(tag+' source supremum',max(abs(Z(v)) for v in samples)<=Zcap)
   ck(tag+' source derivative',max(abs(Zd(v))*math.sqrt(gamma(v)) for v in samples)<=Dcap)
   ck(tag+' actual resolvent gradient',max(abs(fp(v))*math.sqrt(gamma(v)) for v in samples)<=gradcap)
   # Evaluate the full original ball-volume bound in logarithmic arithmetic;
   # rho-sin(rho)=rho^3/6 sum_{m>=0}(-1)^m 6rho^(2m)/(2m+3)!.
   vfloor=mp.mpf(a)*mp.exp(-mp.mpf(Omega)/2)*abs(phi)
   Ly=2*Dcap+4*Zcap*math.sqrt(G)
   rho=min(mp.mpf(1),vfloor/(2*mp.sqrt(N)*(Ly+2*kap*Hh*gradcap)))
   series=mp.fsum([(-1)**m*6*rho**(2*m)/mp.factorial(2*m+3) for m in range(8)])
   tail=6*rho**16/mp.factorial(19)
   logball=3*mp.log(rho)-mp.log(12*mp.pi)+mp.log(series)
   loglower=2*mp.log(a)+mp.log(abs(phi)**2)-2*Omega-mp.log(4)+N*logball
   ck(tag+' retained exact Haar-series tail',tail<mp.mpf('1e-50'))
   ck(tag+' positive actual residual mass',mass>0 and mp.log(mass)>loglower)
   lowergain_log=2*loglower-mp.log(mp.mpf(energycap)+z*mp.exp(loglower))
   # FPR Cauchy lower bound from the actual fixture mass and energy.
   ck(tag+' full monotone gain comparison',mp.log(mass*mass/(energy+z*mass))>=lowergain_log)
   # Full sixteen sign components have eight copies of each parity.
   for value in [-2.,-.5,0.,1.,2.]:
    pp=np.array([math.exp(2*np.prod(s)*t*value)/(16*math.cosh(2*t*value)) for s in itertools.product([-1,1],repeat=4)])
    char=np.array([np.prod(s) for s in itertools.product([-1,1],repeat=4)])
    close(tag+f' full sixteen probability at{value}',pp.sum(),1)
    ck(tag+f' density/covariance floors at{value}',np.log(pp.min())>=-Omega-math.log(16) and math.log(1-(pp@char)**2)>=-Omega)
for rho in [.01,.2,1.]:
 exact=(mp.mpf(rho)-mp.sin(rho))/(2*mp.pi)
 ck(f'original ball-volume lower envelope {rho}',mp.mpf(19)/20*mp.mpf(rho)**3/(12*mp.pi)<=exact<=mp.mpf(rho)**3/(12*mp.pi))
r=dict(all_passed=all(x['passed'] for x in checks),checks=len(checks),scope='Original radius-two Haar heat multipliers and exact gradient-integral constants; continuous four-link constructed ground potential with actual conditional marginal resolvent of an explicitly specified source, full energy, density/covariance factors, all16signs and exact Haar-series remainder; explicit lower-mass/gain comparison. These fixtures are not Wilson vacua or evaluation of the limiting spectral window.',results=checks)
(O/'LOCAL_RESIDUAL_CHECKS.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in r.items() if k!='results'}))
