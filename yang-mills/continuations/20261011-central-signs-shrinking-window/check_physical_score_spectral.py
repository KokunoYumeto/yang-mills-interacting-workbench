from pathlib import Path
import json,numpy as np
O=Path(__file__).resolve().parent
rng=np.random.default_rng(130203);rows=[]
def check(name,x,y,tol=2e-9):
 err=float(np.linalg.norm(x-y));scale=1+float(np.linalg.norm(x))+float(np.linalg.norm(y))
 assert err<=tol*scale,(name,err,scale)
 rows.append(dict(name=name,relative_error=err/scale))
for kappa in [.3,1.7,4.]:
 for j in [1,10,100,10000]:
  a=1/(100*j);s=100*kappa*a
  rr=np.array([a,1.3,1/a,1/a**2]);lam=s*rr
  C0=(rng.normal(size=(4,3))+1j*rng.normal(size=(4,3)))/30
  C=a**1.5*C0
  d=np.diag(np.sqrt(lam/kappa))
  B=-a**-2*d.conj().T@C
  V=(rng.normal(size=(4,2))+1j*rng.normal(size=(4,2)))/4
  X=np.diag(np.sqrt(kappa/lam))@V
  mp=[];cp=[];zp=[];ep=[]
  for q in range(4):
   outer=lambda row:np.outer(row.conj(),row)
   Asc=outer(B[q]);F=outer(C[q])
   M=a**-3*F;Cov=a*a*Asc
   Z=a**-1.5*np.outer(C[q].conj(),V[q]);E=outer(V[q])
   check('original physical scalar weight',kappa*a**4*Asc/lam[q],F)
   check('complete original measure ratio',Cov,100*a*a*rr[q]*M)
   check('source cross scalar map',Z,-a**.5*np.outer(B[q].conj(),X[q]))
   block=np.block([[M,Z],[Z.conj().T,E]])
   assert np.linalg.eigvalsh(block).min()>-1e-11
   rows.append(dict(name='joint block positivity',minimum=float(np.linalg.eigvalsh(block).min())))
   mp.append(M);cp.append(Cov);zp.append(Z);ep.append(E)
  check('complete first relative-energy moment',sum(cp),100*a*a*sum(r*m for r,m in zip(rr,mp)))
  for theta in [.11,1,7]:
   eta=2.3*theta
   U=np.diag(1/(lam+theta*s))@C
   ZU=np.diag(1/(lam+eta*s))@C
   # Cell-orthonormal matrix coordinates J=a^(3/2)I, A=a^(-3/2)I.
   check('mixed physical norm',s*s*a**-3*U.conj().T@ZU,sum(m/((r+theta)*(r+eta)) for r,m in zip(rr,mp)))
   check('mixed physical energy',s*a**-3*U.conj().T@np.diag(lam)@ZU,sum(r*m/((r+theta)*(r+eta)) for r,m in zip(rr,mp)))
   check('full source resolvent',s*a**-1.5*C.conj().T@np.diag(1/(lam+theta*s))@V,sum(z/(r+theta) for r,z in zip(rr,zp)))
   RX=kappa*V.conj().T@np.diag(1/(lam+theta*s))@V
   WX=theta*s*kappa*V.conj().T@np.diag(1/(lam+theta*s)**2)@V
   check('original physical response factors',s/kappa*RX,sum(e/(r+theta) for r,e in zip(rr,ep)))
   check('original physical window factors',s/kappa*WX,sum(theta*e/(r+theta)**2 for r,e in zip(rr,ep)))
   eps=.2;rw=8.
   def W(z):return z*kappa*V.conj().T@np.diag(1/(lam+z)**2)@V
   signed=W(theta*s)-4*eps/(1+eps)**2*W(eps*theta*s)-4*rw/(1+rw)**2*W(rw*theta*s)
   fun=lambda r:theta/(r+theta)**2-4*eps**2*theta/((1+eps)**2*(r+eps*theta)**2)-4*rw**2*theta/((1+rw)**2*(r+rw*theta)**2)
   check('all three signed original shifts',s/kappa*signed,sum(fun(r)*e for r,e in zip(rr,ep)))
out=dict(checks=len(rows),all_passed=True,scope='Exact finite spectral and cell-adjoint algebra for specified complex arrays; all raw powers, full cross blocks, two shifts and original signed three-shift expression. These arrays are not actual Yang–Mills state data. Analytic source comparison and injectivity are proved in PSC5–PSC7, not tested by a substitute state.',rows=rows)
(O/'PHYSICAL_SCORE_SPECTRAL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(dict(checks=len(rows),all_passed=True)))
