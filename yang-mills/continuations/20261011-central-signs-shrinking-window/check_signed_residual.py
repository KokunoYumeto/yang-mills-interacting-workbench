from pathlib import Path
import json,math
import numpy as np
import sympy as sp
O=Path(__file__).resolve().parent
rows=[]
def eq(name,a,b,tol=2e-10):
 e=float(np.max(np.abs(np.asarray(a)-np.asarray(b))));scale=1+float(np.max(np.abs(np.asarray(a))))+float(np.max(np.abs(np.asarray(b))))
 rows.append(dict(name=name,passed=bool(e<=tol*scale),error=e))
def le(name,a,b,tol=2e-10):
 e=float(a-b);rows.append(dict(name=name,passed=bool(e<=tol*(1+abs(a)+abs(b))),excess=e))
def norm2(v):return float(np.vdot(v,v).real)
z=sp.symbols('z',positive=True)
M=sp.Matrix([[1,sp.Rational(1,2)],[sp.Rational(1,2),1]]);X=sp.Matrix([1,-sp.Rational(1,8)])
gain=(X.T*(M+z*sp.eye(2)).inv()*X)[0]-1/(1+z)
expected=(z+5)**2/(16*(z+1)*(2*z+1)*(2*z+3))
response=sp.factor(z*gain+z*z*sp.diff(gain,z))
rows.append(dict(name='exact full rational gain',passed=sp.cancel(gain-expected)==0))
formula=-z*(z+5)*(28*z**3+38*z**2-9*z-15)/(16*(z+1)**2*(2*z+1)**2*(2*z+3)**2)
rows.append(dict(name='exact full differentiated rational gain',passed=sp.cancel(response-formula)==0))
for t,v in [(sp.Rational(1,4),sp.Rational(11,400)),(sp.Integer(1),-sp.Rational(7,400)),(sp.Integer(4),-sp.Rational(261,12100))]:
 rows.append(dict(name='exact finite response z='+str(t),passed=sp.cancel(response.subs(z,t)-v)==0))
signed=response.subs(z,1)-sp.Rational(16,25)*(response.subs(z,sp.Rational(1,4))+response.subs(z,4))
rows.append(dict(name='exact negative three-shift correction',passed=sp.cancel(signed+sp.Rational(25767,1210000))==0))
v=sp.Matrix([sp.Rational(1,20),-sp.Rational(1,5)])
rows.append(dict(name='exact positive residual term',passed=(v.T*M*v)[0]==sp.Rational(13,400)))
rows.append(dict(name='exact mixed derivative term',passed=2*(sp.Matrix([0,sp.Rational(1,8)]).T*v)[0]==-sp.Rational(1,20)))

# Original four-link Haar metric: T has the semicircle pushforward.
n=800;k=np.arange(1,n+1);theta=np.pi*k/(n+1);T=2*np.cos(theta);weights=2*np.sin(theta)**2/(n+1)
Gamma=4-T*T
eq('original fundamental Haar Casimir 3',np.dot(weights,Gamma),3*np.dot(weights,T*T))
eq('original central-invariant adjoint Haar Casimir 8',np.dot(weights,4*T*T*Gamma),8*np.dot(weights,(T*T-1)**2))
for t in [.07,.3,.8]:
 rho=np.exp(2*t*T);rho/=np.dot(weights,rho)
 marginal=np.cosh(2*t*T);marginal/=np.dot(weights,marginal)
 for p in range(1,7):
  for central,den,rate in [(False,rho,3),(True,marginal,8)]:
   degree=2*p if central else p;f=T**degree;df=degree*T**(degree-1)
   mean=np.dot(weights,den*f);var=np.dot(weights,den*(f-mean)**2);energy=np.dot(weights,den*df*df*Gamma)
   le(f'original weighted Haar comparison t{t} degree{degree} central{central}',rate*np.exp(-8*t)*var,energy)

# Complex finite matrices test all retained operator terms; not Wilson samples.
for seed in range(8):
 rng=np.random.default_rng(1370+seed);dim=5+seed%3;p=2+seed%2
 Q=rng.normal(size=(dim,dim))+1j*rng.normal(size=(dim,dim))
 K=Q.conj().T@Q+(0.2+seed*.03)*np.eye(dim)
 A=K[:p,:p];B=K[p:,:p];source=rng.normal(size=dim)+1j*rng.normal(size=dim)
 x=source[:p];y=source[p:];S=norm2(source)
 ak,au=np.linalg.eigh(A);kinv=(au/np.sqrt(ak))@au.conj().T
 delta=float(np.linalg.eigvalsh(K)[0]);deltaA=float(ak[0]);kappa=.6+seed/10
 G=float(np.linalg.eigvalsh(kinv@B.conj().T@B@kinv)[-1])/(4*kappa)*1.000001
 def calc(z):
  RA=np.linalg.inv(A+z*np.eye(p));R=np.linalg.inv(K+z*np.eye(dim))
  f=RA@x;eta=np.r_[np.zeros(p,dtype=complex),y-B@f]
  prime=np.r_[np.zeros(p,dtype=complex),B@RA@RA@x];v=R@eta
  gf=float((np.vdot(source,R@source)-np.vdot(x,RA@x)).real)
  gain=float(np.vdot(eta,v).real);deriv=2*np.vdot(prime,v).real-norm2(v)
  directderiv=-norm2(R@source)+norm2(f)
  full=float((z*np.vdot(R@source,K@R@source)).real);marginal=float((z*np.vdot(f,A@f)).real)
  positive=float((z*np.vdot(v,K@v)).real);mixed=float(2*z*z*np.vdot(prime,v).real)
  m=norm2(eta);e=float(np.vdot(eta,K@eta).real);minus=float(np.vdot(eta,np.linalg.solve(K,eta)).real)
  l1=max(deltaA,z);l2=max(deltaA,z/3)
  r=math.sqrt(4*kappa*G*l1/(l1+z)**2);d=math.sqrt(4*kappa*G*l2/(l2+z)**4)
  cap=z*z*d*S/(z+delta)*(r+math.sqrt(1+r*r))
  lowpos=z*m*m/(e+(2*z+z*z/delta)*m);uppermass=(1+r*r)*S
  eq(f'{seed} z{z} CK24 gain',gf,gain)
  eq(f'{seed} z{z} complete differentiated gain',deriv,directderiv)
  eq(f'{seed} z{z} full response decomposition',full-marginal,positive+mixed)
  eq(f'{seed} z{z} resolvent derivative response',full-marginal,z*gain+z*z*deriv)
  eq(f'{seed} z{z} exact orientation overlap',np.vdot(prime,v),-np.vdot(f,v[:p]))
  eq(f'{seed} z{z} full trial residual energy orthogonality',np.vdot(np.r_[f,np.zeros(dim-p)],(K+z*np.eye(dim))@v),0)
  eq(f'{seed} z{z} retained central-overlap response',full-marginal,positive-2*z*z*np.vdot(f,v[:p]).real)
  le(f'{seed} z{z} coupling with actual floor',norm2(B@f),r*r*norm2(x))
  le(f'{seed} z{z} derivative with actual floor',norm2(prime),d*d*norm2(x))
  le(f'{seed} z{z} joint residual mass',m,uppermass)
  le(f'{seed} z{z} unconstrained coupling bound',r*r,kappa*G/z)
  le(f'{seed} z{z} unconstrained derivative bound',d*d,27*kappa*G/(64*z**3))
  le(f'{seed} z{z} joint mixed bound',abs(mixed),cap)
  le(f'{seed} z{z} exact three reciprocal moments',z*m*m/(e+2*z*m+z*z*minus),positive)
  le(f'{seed} z{z} retained residual lower term',lowpos,positive)
  le(f'{seed} z{z} residual upper term',positive,m/4)
  le(f'{seed} z{z} response lower',lowpos-cap,full-marginal)
  le(f'{seed} z{z} response upper',full-marginal,uppermass/4+cap)
  return dict(eta=eta,response=full-marginal,lower=lowpos-cap,upper=uppermass/4+cap)
 shifts=[.25,1.,4.];values=[calc(t) for t in shifts]
 signed=values[1]['response']-.64*(values[0]['response']+values[2]['response'])
 le(f'{seed} signed lower',values[1]['lower']-.64*(values[0]['upper']+values[2]['upper']),signed)
 le(f'{seed} signed upper',signed,values[1]['upper']-.64*(values[0]['lower']+values[2]['lower']))
 for i,j in [(0,1),(1,2),(0,2)]:
  z,w=shifts[i],shifts[j];difference=values[j]['eta']-values[i]['eta']
  actual=(w-z)*B@np.linalg.solve(A+w*np.eye(p),np.linalg.solve(A+z*np.eye(p),x))
  eq(f'{seed} cross-shift full vector {i}{j}',difference,np.r_[np.zeros(p),actual])
  critical=(math.sqrt((w+z)**2+12*w*z)-(w+z))/6;floor=max(deltaA,critical)
  bound=4*kappa*G*(w-z)**2*norm2(x)*floor/((floor+z)**2*(floor+w)**2)
  le(f'{seed} cross-shift norm {i}{j}',norm2(difference),bound)
  samples=np.geomspace(deltaA,max(deltaA*1e4,1e5),300)
  vals=samples/((samples+z)**2*(samples+w)**2)
  le(f'{seed} cross-shift scalar maximum {i}{j}',float(vals.max()),floor/((floor+z)**2*(floor+w)**2))

rows.append(dict(name='exact eventual negative-bound coefficient',passed=bool(2*sp.sqrt(27)/9>sp.Rational(1,2))))
for kappa in [.2,1.,10.,1000.,1e6]:
 for beta in [.1,1.,9.]:
  j=8;N=24*j**12+24*j**8+6*j**4;omega=1600*np.pi**2*j*N/kappa
  logratio=math.log(8*j/beta)-omega;r2=160000*np.pi**2*N*j**3/(beta*kappa*kappa)
  le(f'original path log spectral-floor threshold k{kappa} beta{beta}',logratio,math.log(1/3))
  le(f'original path coupling threshold k{kappa} beta{beta}',1.,r2)
  r=math.sqrt(r2);mixlower=math.sqrt(27)/9*r*(r+math.sqrt(1+r2));massupper=(1+r2)/4
  le(f'original path strict negative norm-certificate k{kappa} beta{beta}',massupper,mixlower)
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),scope='Exact rational finite compression with vacuum and both raw source components; original four-link radius-two Haar Casimirs and weighted comparisons; complex finite-matrix derivative, moment, mixed, cross-shift and exact central-overlap identities; original-path negative norm-certificate checks. Finite matrices and constructed densities are not Wilson-vacuum samples. Written proofs establish the original-state statements.',results=rows)
(O/'SIGNED_RESIDUAL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='results'}))
assert out['all_passed'],[r for r in rows if not r['passed']]
