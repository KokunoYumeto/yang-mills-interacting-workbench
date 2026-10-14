from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm
from scipy.integrate import quad_vec
O=Path(__file__).resolve().parent;rows=[]
def eq(name,a,b,tol=5e-10):
 error=float(np.max(np.abs(np.asarray(a)-np.asarray(b))));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
 rows.append(dict(name=name,passed=bool(error<=tol*scale),error=error))
def le(name,a,b,tol=5e-10):
 excess=float(a-b);rows.append(dict(name=name,passed=bool(excess<=tol*(1+abs(a)+abs(b))),excess=excess))
def n2(v):return float(np.vdot(v,v).real)
for seed in range(5):
 rng=np.random.default_rng(980+seed);n=5+seed%2;p=2
 q=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));M=q.conj().T@q+.4*np.eye(n)
 A=M[:p,:p];B=M[p:,:p];D=M[p:,p:];delta=float(np.linalg.eigvalsh(M)[0])
 source=rng.normal(size=n)+1j*rng.normal(size=n);x=source[:p];y=source[p:];z=.2+.4*seed
 f=np.linalg.solve(A+z*np.eye(p),x);eta=y-B@f;eta_full=np.r_[np.zeros(p),eta];Jf=np.r_[f,np.zeros(n-p)]
 def u(t):return expm(-t*M)@eta_full
 def a(t):return u(t)[:p]
 def memory(t):return B.conj().T@expm(-t*D)@B
 eq(f'{seed} initial first derivative',-np.vdot(Jf,M@eta_full),n2(B@f)-np.vdot(B@f,y))
 eq(f'{seed} initial second derivative',np.vdot(M@Jf,M@eta_full),np.vdot(B@x-z*B@f,eta)+np.vdot(B@f,D@eta))
 for t in [.03,.2,.8]:
  current=u(t);av=current[:p];bv=current[p:];du=-M@current
  eq(f'{seed} t{t} central strong equation',du[:p],-A@av-B.conj().T@bv)
  eq(f'{seed} t{t} conditional strong equation',du[p:],-B@av-D@bv)
  integral=quad_vec(lambda r:expm(-(t-r)*D)@B@a(r),0,t,epsabs=1e-11,epsrel=1e-11)[0]
  eq(f'{seed} t{t} full variation of constants',bv,expm(-t*D)@eta-integral)
  history=quad_vec(lambda r:memory(t-r)@a(r),0,t,epsabs=1e-11,epsrel=1e-11)[0]
  eq(f'{seed} t{t} full memory equation',du[:p],-A@av-B.conj().T@expm(-t*D)@eta+history)
  eq(f'{seed} t{t} retained source split',B.conj().T@expm(-t*D)@eta,B.conj().T@expm(-t*D)@y-memory(t)@f)
  diag=float(np.vdot(f,memory(t)@f).real);le(f'{seed} t{t} memory positivity',0.,diag)
  le(f'{seed} t{t} retained physical gap',diag,np.exp(-delta*t)*n2(B@f))
  cross=np.vdot(B@f,expm(-t*D)@y);yy=float(np.vdot(y,expm(-t*D)@y).real)
  le(f'{seed} t{t} cross-source bound',abs(cross)**2,diag*yy)
  first=np.vdot(B@f,D@y)
  remainder=quad_vec(lambda r:(t-r)*np.vdot(D@B@f,expm(-r*D)@D@y),0,t,epsabs=1e-11,epsrel=1e-11)[0]
  eq(f'{seed} t{t} full cross-source Taylor remainder',cross,np.vdot(B@f,y)-t*first+remainder)
  bound=(delta*t-1+np.exp(-delta*t))/delta**2*np.linalg.norm(D@B@f)*np.linalg.norm(D@y)
  le(f'{seed} t{t} complete remainder bound',abs(remainder),bound)
  for k in range(1,4):
   value=float(np.vdot(B@f,np.linalg.matrix_power(D,k)@expm(-t*D)@B@f).real)
   le(f'{seed} t{t} alternating derivative {k}',0.,value)
 for sigma in [.3,1.1]:
  T=.7;resD=np.linalg.inv(D+sigma*np.eye(n-p));resM=np.linalg.inv(M+sigma*np.eye(n))
  kernel_integral=quad_vec(lambda t:np.exp(-sigma*t)*memory(t),0,T,epsabs=1e-11,epsrel=1e-11)[0]
  kernel_tail=B.conj().T@expm(-T*(D+sigma*np.eye(n-p)))@resD@B
  eq(f'{seed} sigma{sigma} memory Laplace with entire tail',kernel_integral+kernel_tail,B.conj().T@resD@B)
  evolution=quad_vec(lambda t:np.exp(-sigma*t)*a(t),0,T,epsabs=1e-11,epsrel=1e-11)[0]
  tail=(expm(-T*(M+sigma*np.eye(n)))@resM@eta_full)[:p]
  actual=(resM@eta_full)[:p];eq(f'{seed} sigma{sigma} actual Laplace with entire tail',evolution+tail,actual)
  schur=A+sigma*np.eye(p)-B.conj().T@resD@B
  eq(f'{seed} sigma{sigma} full Schur receiver',schur@actual,-B.conj().T@resD@eta)
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),scope='Complex finite positive matrices with both original source components and full coupling; all time-history integrals, initial derivatives, diagonal memory, cross-source terms and Laplace tails retained. A vacuum zero direction can be adjoined independently; these are not Wilson-vacuum samples or numerical evaluations of the original positive-time correlation.',results=rows)
(O/'MIXED_TIME_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='results'}));assert out['all_passed']
