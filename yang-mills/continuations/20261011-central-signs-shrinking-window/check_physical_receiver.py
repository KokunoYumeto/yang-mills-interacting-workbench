from pathlib import Path
import json
import numpy as np
rng=np.random.default_rng(20261013);rows=[]
def test(name,x,y):
 err=float(np.linalg.norm(x-y));scale=max(1e-30,float(np.linalg.norm(x)),float(np.linalg.norm(y)))
 rows.append(dict(name=name,error=err,scale=scale,passed=bool(err<2e-8*scale)));assert rows[-1]['passed'],rows[-1]
def rand(n,m):return rng.normal(size=(n,m))+1j*rng.normal(size=(n,m))
for case in range(12):
 kappa=1.7;a=1/(100*(case+1));ns=4;no=3;nc=3
 scalar=np.diag(np.geomspace(.1,6,ns));outside=np.diag(np.geomspace(.07,4,no))
 L=np.block([[scalar,np.zeros((ns,no))],[np.zeros((no,ns)),outside]])
 deriv=np.vstack([np.diag(np.sqrt(np.diag(scalar)/kappa)),np.zeros((no,ns))])
 P=np.diag([1]*ns+[0]*no)
 C=a*a*rand(ns+no,nc);N=C.conj().T@C;Q=C.conj().T@L@C
 Pi=C@np.linalg.solve(N,C.conj().T)
 # A complete orthogonal complement basis from a full SVD.
 UU,_,_=np.linalg.svd(C,full_matrices=True);V=UU[:,nc:]
 Aperp=V.conj().T@L@V;R=V.conj().T@L@C
 Bsc=-deriv.conj().T@C/a**2
 X=rand(ns,1)[:,0];v=deriv@X;b=C.conj().T@v;vp=V.conj().T@v
 Y=.1*a*a*rand(ns,nc);bpot=1/(kappa*a*a);G0=(Bsc-6*bpot*Y)/2
 data={}
 for z in [.003,.14,1.7]:
  Di=np.linalg.inv(Aperp+z*np.eye(no+ns-nc))
  S=Q+z*N-R.conj().T@Di@R;h=np.linalg.solve(N,S);Phi=Bsc@h
  T=C-V@Di@R;project=P@T;scalarinv=np.linalg.inv(scalar+z*np.eye(ns));scalarzero=np.linalg.inv(scalar)
  predicted=-kappa*a*a*deriv@scalarzero@scalarinv@Phi
  test(f'{case},{z}: full lift equation',(L+z*np.eye(ns+no))@T,C@h)
  test(f'{case},{z}: physical scalar lift',project,predicted)
  d=b-R.conj().T@Di@vp
  test(f'{case},{z}: physical source',d,-a*a*S@np.linalg.solve(N,Bsc.conj().T@scalarinv@X))
  test(f'{case},{z}: raw source',b,-a*a*Bsc.conj().T@X)
  test(f'{case},{z}: full current coefficient',np.linalg.solve(S,d),-a*a*np.linalg.solve(N,Bsc.conj().T@scalarinv@X))
  test(f'{case},{z}: cross resolvent',R.conj().T@Di@vp,-a*a*Bsc.conj().T@X+a*a*S@np.linalg.solve(N,Bsc.conj().T@scalarinv@X))
  test(f'{case},{z}: actual density split',Phi,(6*bpot*Y+2*G0)@h)
  Spr=N+R.conj().T@Di@Di@R
  Nphys=kappa*a**4*Phi.conj().T@scalarzero@scalarinv@scalarinv@Phi
  Ephys=kappa*a**4*Phi.conj().T@scalarinv@scalarinv@Phi
  perp=(np.eye(ns+no)-P)@T
  test(f'{case},{z}: physical complement norm',Spr-Nphys,perp.conj().T@perp)
  test(f'{case},{z}: physical complement energy',S-z*Spr-Ephys,perp.conj().T@L@perp)
  data[z]=(Phi,project,h,scalarinv)
 for z,(Phi,project,h,invz) in data.items():
  for r,(Phir,projectr,hr,invr) in data.items():
   for typ,K in [('norm',np.linalg.inv(scalar)@invz@invr),('energy',invz@invr)]:
    direct=project.conj().T@(np.eye(ns+no) if typ=='norm' else L)@projectr
    test(f'{case},{z},{r}: mixed {typ}',direct,kappa*a**4*Phi.conj().T@K@Phir)
    expanded=h.conj().T@(36*bpot*bpot*Y.conj().T@K@Y+12*bpot*Y.conj().T@K@G0+12*bpot*G0.conj().T@K@Y+4*G0.conj().T@K@G0)@hr
    test(f'{case},{z},{r}: four complete {typ} terms',kappa*a**4*Phi.conj().T@K@Phir,kappa*a**4*expanded)

# Exact original-metric trace defects and improved roots.
def bound(name,x,tol=1e-9):
 rows.append(dict(name=name,violation=float(max(0,x)),passed=bool(x<=tol)));assert rows[-1]['passed'],rows[-1]
plots=[]
for kappa in [.2,1.,3.7]:
 for j in [1,2,10,100,10000]:
  a=1/(100*j);bp=1/(kappa*a*a)
  theta0=(-1.5*a+np.sqrt(2.25*a*a+144/kappa**2))/8
  U=theta0/a;Af=9+16*U
  ell=18/(Af+4*np.sqrt(U*Af))
  old=24*kappa*a/(12*kappa*a+64+np.sqrt((12*kappa*a+64)**2-144*kappa*kappa*a*a))
  test(f'root {kappa},{j}: kinetic quadratic',np.array([4*theta0**2+1.5*a*theta0]),np.array([9/kappa**2]))
  test(f'root {kappa},{j}: face quadratic',np.array([Af*ell*ell+36]),np.array([4*Af*ell]))
  bound(f'root {kappa},{j}: half ceiling',theta0-1.5/kappa)
  bound(f'root {kappa},{j}: floor strengthening',old-ell)
  for m in [2,3,4]:
   for w in [0,.3,1.1]:
    rhs=9*bp/(8*kappa)*(2*m-w)
    root=(-1.5+np.sqrt(2.25+16*rhs))/8
    for frac in [.1,.6,.99]:
     T=frac*root;Rbar=3*bp/(8*kappa)*(2*m-w)-T/2
     defect=3*Rbar-4*T*T;sig=np.sqrt(defect/3);tf=np.diag([np.sqrt(defect/18),-np.sqrt(defect/18),0])
     Hee=[-2*T/3*np.eye(3)+sgn*sig/3*np.eye(3)+sgn*tf for sgn in [-1,1]]
     outside=np.diag([np.sqrt(defect/9),0,0])
     measured=sum(np.linalg.norm(H)**2 for H in Hee)/2+np.linalg.norm(outside)**2
     trvar=sum((np.trace(H)+2*T)**2 for H in Hee)/2
     result=3*np.linalg.norm(outside)**2+3*np.linalg.norm(tf)**2+trvar
     test(f'defect {kappa},{j},{m},{w},{frac}: full row',np.array([measured]),np.array([Rbar]))
     test(f'defect {kappa},{j},{m},{w},{frac}: three retained parts',np.array([result]),np.array([rhs-1.5*T-4*T*T]))
     bound(f'defect {kappa},{j},{m},{w},{frac}: actual-root ceiling',a*T-theta0)
     Yvariance=trvar/(36*bp*bp)
     bound(f'defect {kappa},{j},{m},{w},{frac}: density variance',Yvariance-defect/(36*bp*bp))
  for Rside in [.01,.2,1,12,100]:
   LR=9*kappa*Rside**3+24*Rside**2
   KR=(LR+np.sqrt(LR*LR-81*kappa*kappa*Rside**6/4))/2
   r=9*kappa*Rside**3/8;c=81*kappa*kappa*Rside**6/16
   test(f'budget {kappa},{j},{Rside}: strict comparison',np.array([r*(LR-r)-c]),np.array([243*kappa*kappa*Rside**6/64+27*kappa*Rside**5]))
   bound(f'budget {kappa},{j},{Rside}: residual bound stronger',(LR-r-KR)/max(1,KR))
   bound(f'budget {kappa},{j},{Rside}: separate kinetic coefficient',(4.5*kappa*Rside**3-(LR-r))/max(1,LR))
  plots.append(dict(kappa=kappa,j=j,a=a,theta=theta0,old_ceiling=3/kappa,new_limit=1.5/kappa,old_floor=old/a,new_floor=ell/a,floor_limit=3*kappa/8))
# Full original block-Hessian graph identity, every exterior pair included.
# These algebraic arrays are not ground-state Hessian samples.
for case in range(30):
 n=5;ni=3
 H=rand(3*n,3*n).real;H=(H+H.T)/2;g=rand(3*n,1).real[:,0]
 T=np.array([np.dot(g[3*e:3*e+3],g[3*e:3*e+3]) for e in range(n)])
 K=np.array([[np.linalg.norm(H[3*e:3*e+3,3*f:3*f+3])**2 for f in range(n)] for e in range(n)])
 GH=np.array([[g[3*e:3*e+3]@H[3*e:3*e+3,3*f:3*f+3]@g[3*f:3*f+3] for f in range(n)] for e in range(n)])
 Q=np.diag(K.sum(axis=1)+.5*T)-2*GH
 graph=np.diag(K.sum(axis=1))-K
 Gamma=K+np.diag(.5*T)-2*GH
 test(f'Hessian {case}: covariance and curl',Q[:ni,:ni]-graph[:ni,:ni],Gamma[:ni,:ni])
 coeff=np.r_[rand(ni,1)[:,0],np.zeros(n-ni)]
 direct=sum(abs(coeff[e]-coeff[f])**2*K[e,f] for e in range(n) for f in range(e+1,n))
 test(f'Hessian {case}: all exterior pairs',np.array([coeff.conj()@graph@coeff]),np.array([direct]))
 bound(f'Hessian {case}: graph row norm',np.linalg.eigvalsh(graph[:ni,:ni]).max()-2*K.sum(axis=1).max())
v=dict(checks=len(rows),all_passed=all(r['passed'] for r in rows),scope='Exact scalar/current intertwining, every mixed kernel, original-metric trace defects and roots, improved original-path constants, full exterior Hessian graph. Diagnostic arrays are not Yang–Mills vacuum samples.',details=rows,plots=plots)
Path(__file__).with_name('PHYSICAL_RECEIVER_CHECKS.json').write_text(json.dumps(v,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v[k] for k in ['checks','all_passed','scope']}))
