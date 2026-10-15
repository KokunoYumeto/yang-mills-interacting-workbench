from pathlib import Path
import itertools,json,math
import numpy as np
from scipy.linalg import eigh
O=Path(__file__).resolve().parent;rng=np.random.default_rng(20261015);checks=[]
def ck(name,condition,**kw):
    checks.append(dict(name=name,passed=bool(condition),**kw));assert condition,(name,kw)
# Original finite boxes: enumerate every inside, outside and crossing face.
def geometry(side):
    vertices=list(itertools.product(range(side+1),repeat=3));edges=[]
    for v in vertices:
        for d in range(3):
            if v[d]<side:edges.append((v,d))
    faces=[]
    for v in vertices:
        for d in range(3):
            for k in range(d+1,3):
                if v[d]<side and v[k]<side:
                    vd=list(v);vd[d]+=1;vk=list(v);vk[k]+=1
                    faces.append({(v,d),(tuple(vd),k),(tuple(vk),d),(v,k)})
    return edges,faces
for side in [2,4]:
 E,F=geometry(side);inc={e:sum(e in p for p in F) for e in E}
 for q in range(1,min(side,3)+1):
  for base in sorted(set([(0,0,0),(side-q,)*3,((side-q)//2,)*3])):
   QE=set()
   for e in E:
    v,d=e;end=list(v);end[d]+=1
    if all(base[h]<=v[h]<=base[h]+q and base[h]<=end[h]<=base[h]+q for h in range(3)):QE.add(e)
   inside=[p for p in F if p<=QE];cross=[p for p in F if p&QE and not p<=QE];plus=QE|set().union(*cross) if cross else QE
   Nq=3*q*(q+1)**2;Mq=3*q*q*(q+1);Cq=2*q*(q+1)*sum(int(base[d]>0)+int(base[d]+q<side) for d in range(3))
   label=f'side{side}/q{q}/v{base}'
   ck(label+' exact original counts',(len(QE),len(inside),len(cross))==(Nq,Mq,Cq))
   ck(label+' one inside edge per crossing face',all(len(p&QE)==1 for p in cross))
   r={e:inc[e] for e in QE};rx={e:sum(e in p for p in cross) for e in QE}
   ns=sum(sum(e in p and f in p for p in F)**2 for e in QE for f in QE)
   nxs=sum(sum(e in p and f in p for p in cross)**2 for e in QE for f in QE)
   nps=sum(sum(e in p and f in p for p in F)**2 for e in QE for f in plus)
   ck(label+' complete incidence ceilings',sum(v*v for v in r.values())<=4*(4*Mq+Cq) and sum(v*v for v in rx.values())<=4*Cq and ns<=64*Mq+4*Cq and nxs<=4*Cq and nps<=64*Mq+16*Cq and len(plus)<=Nq+3*Cq)
# Exact scalar maximizer and full spectral-norm interpolation.
for m in range(1,6):
 a=m/6
 for eta in [.001,.02,1,31]:
  bm=(1-a)*(a/eta)**(a/(1-a));maximizer=(a/eta)**(1/(1-a))
  ck(f'interpolation m{m} eta{eta}',np.isclose(maximizer**a-eta*maximizer,bm) and np.all(np.linspace(0,3*maximizer,1001)**a-eta*np.linspace(0,3*maximizer,1001)<=bm*(1+1e-12)+1e-12))
  lam=np.r_[0,np.geomspace(1e-5,1e4,71)];weights=rng.random(len(lam))
  hs=[np.sqrt(np.sum(weights*lam**k)) for k in range(7)]
  ck(f'full norm interpolation m{m} eta{eta}',hs[m]<=eta*hs[6]+bm*hs[0]+1e-7 and hs[m]<=hs[6]**a*hs[0]**(1-a)*(1+1e-12))
for k in range(20):
 A,G,U2,B=np.exp(rng.uniform(-3,4,4));T=A+G;tau=2*T+A+B/U2
 exact=np.sqrt(2*np.pi*U2*((2*A+G)*U2+B))
 obj=lambda z:((z+A)*U2+B)*np.sqrt(np.pi/(2*(z-T)))
 ck(f'heat-resolvent optimum {k}',np.isclose(obj(tau),exact) and min(obj(T+(tau-T)*fac) for fac in [.25,.5,1,2,4])>=exact*(1-1e-12))
# Radius-two SU2 heat comparison on psi=1+h.x; retain its actual nonconstant density.
h=np.array([1/5,1/7,0,0]);hn=np.linalg.norm(h);A=.75*hn/(1-hn);G=hn**2/(4*(1-hn)**2);T=A+G
x=rng.normal(size=(120,4));x/=np.linalg.norm(x,axis=1)[:,None];ell=x@h
for time in [.001,.03,.2,1,4]:
 density_heat=1+2*np.exp(-.75*time)*ell+hn**2/4+np.exp(-2*time)*(ell**2-hn**2/4)
 ck(f'original heat actual-density comparison t{time}',np.all(density_heat<=np.exp(2*T*time)*(1+ell)**2+1e-12))
 # F is a four-component linear quaternion array with arbitrary real coefficient matrix.
 C=rng.normal(size=(4,4));Fx=x@C.T;sq=np.sum(Fx**2,axis=1);mean=np.sum(C*C)/4
 heat_sq=mean+np.exp(-2*time)*(sq-mean);sq_heat=np.exp(-1.5*time)*sq
 grad_sq=np.exp(-1.5*time)*(np.sum(C*C)-sq)/4
 ck(f'full vector heat variance t{time}',np.all(heat_sq-sq_heat>=2*time*grad_sq-1e-11))
# Original noncommuting raw source/Gram receiver, including singular R.
for n in [2,4,7]:
 for rep in range(12):
  A=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));S=A.conj().T@A+.2*np.eye(n)
  U=rng.normal(size=(max(1,n-2),n))+1j*rng.normal(size=(max(1,n-2),n));R=U.conj().T@U
  beta2=max(0,float(eigh(R,S,eigvals_only=True)[-1]))*(1+1e-10)
  E=S-S@np.linalg.solve(S+R,S)
  ck(f'raw residual matrix {n}/{rep}',np.linalg.eigvalsh(beta2*S-R).min()>-1e-8 and np.linalg.eigvalsh(beta2/(1+beta2)*S-E).min()>-1e-8 and np.linalg.eigvalsh(S-E-S/(1+beta2)).min()>-1e-8)
# Logarithms of the complete finite formula, without exponent overflow.
def constants(j,k=.8,theta=1,eps=.25,Rwin=4):
 q=100*j;N=3*(2*j**4)*(2*j**4+1)**2;M=3*(2*j**4)**2*(2*j**4+1)
 Nq=3*q*(q+1)**2;Mq=3*q*q*(q+1);Cq=12*q*(q+1);a=1/(100*j);b=1/(k*a*a);c=2/(k*a)
 z=theta*k/j;e1=z*(1+eps+Rwin);e2=z*z*(eps+Rwin+eps*Rwin);e3=eps*Rwin*z**3
 A=4*b*M/k;G=4*np.pi**2*N*c*c;Wp=A+(3*N-1)*c;AQ=2*np.pi*c*np.sqrt(Nq);Ap=2*np.pi*c*np.sqrt(Nq+3*Cq)
 p1=2*b*np.sqrt(4*Mq+Cq);px=2*b*np.sqrt(Cq);p2=3*b*np.sqrt(16*Mq+Cq);p2x=3*b*np.sqrt(Cq);p2p=6*b*np.sqrt(4*Mq+Cq)
 U1=AQ;U2=np.sqrt(3*Nq)*Wp+AQ**2+AQ/np.sqrt(2);B=(2*p1*AQ+p2)/k;U3=np.sqrt(2*np.pi*U2*((2*A+G)*U2+B))
 def rows(pf,p2f):
  return {5:6*k**3*U1,4:12*k**3*U2,3:8*k**3*U3+6*k*k*pf+4*e1*k*k*U1,2:8*k*k*p2f+12*k*k*p1*AQ+4*e1*k*k*U2,1:6*k*k*pf+4*k*k*p2p*Ap+2*k*e1*pf+2*k*e2*U1}
 d=rows(p1,p2);r=rows(px,p2x);K=0
 for m in range(1,6):
  alpha=m/6;eta=k**3/(10*d[m]);bm=(1-alpha)*(alpha/eta)**(alpha/(1-alpha));K+=2/k**3*d[m]*bm
 L=2/k**3+K/e3;terms={m:r[m]*L**(m/6)*e3**(-(1-m/6)) for m in range(1,6)}
 omega=4*np.pi**2*c*Nq;logb=omega+np.log(sum(terms.values()))
 return dict(j=j,N=N,M=M,Nq=Nq,Mq=Mq,Cq=Cq,omega=omega,log_residual_ceiling=logb,log10_residual_ceiling=logb/np.log(10),log_polynomial_factor=np.log(sum(terms.values())),kappa=k,source_cube_side=q*a)
path=[constants(j) for j in [4,5,6,8,12,16,24,32,64,128]]
for row in path:
 j=row['j'];ck(f'original path exponent j{j}',np.isclose(row['omega'],240000*np.pi**2*j*j*(100*j+1)**2/.8) and row['source_cube_side']==1 and j**4-50*j>0 and all(math.isfinite(float(v)) for v in row.values()))
ck('original explicit ceiling logarithmic rate',abs(path[-1]['log_residual_ceiling']/128**4/(2400000000*np.pi**2/.8)-1)<.0002)
res=dict(checks=len(checks),all_passed=all(c['passed'] for c in checks),details=checks,path=path,scope='Original incidence enumeration; scalar and norm inequalities; exact polynomial heat formulas evaluated on original SU2 constructed-density fixtures, not Wilson samples; noncommuting matrix consequences including singular residuals; original-j substitution of the complete upper function.')
(O/'INVERSE_TRIAL_CHECKS.json').write_text(json.dumps(res,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=res['checks'],all_passed=res['all_passed'],log10_ceiling_j4=path[0]['log10_residual_ceiling'])))
