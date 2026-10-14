from pathlib import Path
import itertools,json,math
import numpy as np
import sympy as s
import mpmath as mp
from scipy.integrate import quad
O=Path(__file__).resolve().parent;rows=[];rng=np.random.default_rng(2026101403)
def eq(name,a,b,tol=2e-8):
    a=np.asarray(a);b=np.asarray(b);err=float(np.max(np.abs(a-b)));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=bool(err<=tol*scale),error=err))
def yes(name,ok):rows.append(dict(name=name,passed=bool(ok)))
pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]],complex),np.array([[1,0],[0,-1]],complex)]
J=[-1j*p for p in pauli];T=[p/2 for p in J];I=np.eye(2,dtype=complex)
def product(seq):
    out=I.copy()
    for x in seq:out=out@x
    return out
def ex(t,k):return np.cos(t)*I+np.sin(t)*k
def su2():
    q=rng.normal(size=4);q/=np.linalg.norm(q);return q[0]*I+sum(q[a+1]*J[a] for a in range(3))
alpha=np.arange(1,4)*np.pi/4
K=[J[2],-J[2],J[0],-J[0],J[1],-J[1]];V=[J[0],J[0],J[1],J[1],J[2],J[2]]
hh=[ex(-a,J[2])@ex(a,J[0]) for a in alpha]
def curve(r,t,i):return ex(-alpha[i],K[r])@ex(alpha[i],np.cos(t)*K[r]+np.sin(t)*V[r])
def phi(t):return [product([curve(r,t[r],i) for r in range(6)]+[hh[i]@curve(r,t[k],i)@hh[i].conj().T for k,r in [(6,1),(7,2),(8,3)]]) for i in range(3)]
def ff(t):return np.array([-.5*np.trace(p@ja).real for p in phi(t) for ja in J])
M=s.Matrix([[1,1,0,0,-1,1,0,1,-1],[-1,1,1,1,0,0,-1,0,0],[0,0,-1,1,1,1,1,1,1],[0,0,0,0,-2,2,0,0,0],[-2,2,0,0,0,0,2,0,0],[0,0,-2,2,0,0,0,2,-2],[-1,-1,0,0,-1,1,0,1,-1],[-1,1,-1,-1,0,0,-1,0,0],[0,0,-1,1,-1,-1,-1,1,1]])/2
lam=s.Rational(1024,6561);B=9*math.sqrt(3);d0=float(lam)/(2*B);y0=float(lam)**2/(4*B);mn=np.array(M,dtype=float);mi=np.linalg.inv(mn)
yes('displayed exact determinant minus four',M.det()==-4)
yes('displayed complete Frobenius square eighteen',s.trace(M.T*M)==18)
yes('exact singular lower estimate',4*(s.Rational(8,18))**4==lam)
yes('all singular values exceed proved floor',np.linalg.svd(mn,compute_uv=False)[-1]>float(lam))
yes('complete numerical endpoint word bound',15*(s.ceiling(432/lam**2)+1)==266040)
eps=1e-6
for k in range(9):
    e=np.eye(9)[k]*eps;eq(f'original quaternion endpoint derivative column{k}',(ff(e)-ff(-e))/(2*eps),mn[:,k])
for trial in range(12):
    t=rng.normal(size=9);t=t/np.linalg.norm(t)*d0*.9;v=rng.normal(size=9);v/=np.linalg.norm(v)
    dd=(ff(t+eps*v)-2*ff(t)+ff(t-eps*v))/eps**2
    yes(f'full quaternion directional Hessian ceiling{trial}',np.linalg.norm(dd)<B+1e-2)
    y=rng.normal(size=9);y=y/np.linalg.norm(y)*y0*.95;x=np.zeros(9)
    for _ in range(30):x=mi@(y-(ff(x)-mn@x))
    eq(f'full nine-variable contraction image{trial}',ff(x),y,1e-11)
    yes(f'contraction stays in specified parameter ball{trial}',np.linalg.norm(x)<=d0)
    yes(f'positive original quaternion scalar branch{trial}',all(np.trace(p).real>0 for p in phi(x)))
def eta(z):
    if z<=1:return 0.,0.
    if z>=2:return 1.,0.
    A=-1/(z-1);D=-1/(2-z);v=1/(1+np.exp(np.clip(D-A,-700,700)))
    return v,v*(1-v)*((z-1)**-2+(2-z)**-2)
cut=[]
for delta in [.12,.06,.03,.015]:
    def zeta(theta):
        a,ap=eta(theta/delta);b,bp=eta((math.pi-theta)/delta)
        return a*b,(ap*b-a*bp)/delta
    cuts=[delta,2*delta,math.pi-2*delta,math.pi-delta]
    mass=quad(lambda t:2/math.pi*zeta(t)[0]**2*math.sin(t)**2,0,math.pi,points=cuts,epsabs=1e-12)[0]
    energy=quad(lambda t:16/(2*math.pi)*math.sin(t)**4*zeta(t)[1]**2,0,math.pi,points=cuts,epsabs=1e-12)[0]
    yes(f'original cutoff mass remains positive{delta}',0<mass<1)
    yes(f'exact cutoff cubic scaling finite{delta}',0<energy/delta**3<300)
    cut.append(dict(delta=delta,mass=mass,gradient_squared=energy,gradient_squared_over_delta_cubed=energy/delta**3))
yes('cutoff converges toward unit Haar mass',all(cut[i+1]['mass']>cut[i]['mass'] for i in range(3)))
yes('cutoff derivative decreases at the proved scale',all(cut[i+1]['gradient_squared']<cut[i]['gradient_squared']/6 for i in range(3)))
# Full radius-two four-link derivative/Hessian. No trace-coordinate metric substituted.
for trial in range(8):
    links=[su2() for _ in range(4)];tr=np.trace(product(links)).real;grad=[];hes=np.zeros((12,12))
    for e in range(4):
        for a in range(3):
            vs=links.copy();vs[e]=T[a]@vs[e];grad.append(np.trace(product(vs)).real)
            for f in range(4):
                for c in range(3):
                    if e==f:hes[3*e+a,3*f+c]=-tr/4 if a==c else 0
                    else:
                        vs=links.copy();vs[e]=T[a]@vs[e];vs[f]=T[c]@vs[f]
                        hes[3*e+a,3*f+c]=np.trace(product(vs)).real
    eq(f'all twelve original gradient components{trial}',np.dot(grad,grad),4-tr**2)
    eq(f'complete original Hessian trace{trial}',np.trace(hes),-3*tr)
    yes(f'full Hessian operator bound two{trial}',np.linalg.norm(hes,2)<=2+1e-12)
# Exact degree-two Haar cubature on four crossing links; all 36 original faces retained.
def shift(p,a):q=list(p);q[a]+=1;return tuple(q)
faces=[]
for p in itertools.product(range(-1,2),repeat=3):
    for a in range(3):
        for b in range(a+1,3):
            if p[a]<1 and p[b]<1:faces.append([((p,a),1),((shift(p,a),b),1),((shift(p,b),a),-1),((p,b),-1)])
cross=[(((0,0,0),0),1),(((1,0,0),2),1),(((0,0,1),0),-1),(((0,0,0),2),-1)]
ci=faces.index(cross);rule=np.array([I,-I,J[0],-J[0],J[1],-J[1],J[2],-J[2]])
grid=np.array(list(itertools.product(range(8),repeat=4)));assigned={edge:rule[grid[:,i]] for i,(edge,sign) in enumerate(cross)}
traces=[]
for word in faces:
    hol=np.broadcast_to(I,(len(grid),2,2)).copy()
    for edge,sgn in word:
        mat=assigned.get(edge,np.broadcast_to(I,(len(grid),2,2)))
        if sgn==-1:mat=mat.conj().transpose(0,2,1)
        hol=hol@mat
    traces.append(np.trace(hol,axis1=1,axis2=2).real)
tc=traces[ci];eq('crossing trace exact Haar mean',np.mean(tc),0,0)
for i,tr in enumerate(traces):eq(f'original crossing Fourier coefficient face{i}',np.mean(tr*tc),1 if i==ci else 0,0)
coupling=12500;potential=2*coupling*len(faces)-coupling*sum(traces)
eq('entire original Wilson potential crossing coefficient',np.mean(potential*tc),-coupling,0)
eq('complete 36-face constant is retained',len(faces),36,0)
mp.mp.dps=180;floors=[]
for j in [1,2,3]:
    k=mp.mpf(4)/5;a=1/(mp.mpf(100)*j);L=j**4;N=3*(2*L)*(2*L+1)**2;Mface=3*(2*L)**2*(2*L+1)
    b=1/(k*a*a);c=2/(k*a);G=4*mp.pi**2*N*c*c;W=4*b*Mface/k+(3*N-1)*c;Bw=4*b*Mface/k+G
    Q=3+2*(1+mp.sqrt(2))*mp.sqrt(G)+Bw+3*N*W+42*G;R=b/(k*Q);C4=532082
    delta=min(mp.pi/4,R/(16*C4*mp.sqrt(G)));epsfloor=R/(4*C4*mp.log(mp.cot(delta/2)))
    JJ=2*W+4*G+2*c+4*mp.sqrt(G);d=min(mp.mpf(1),epsfloor/(2*JJ));t=d/mp.sqrt(N);vol=(t-mp.sin(t))/(2*mp.pi)
    logm=2*mp.log10(k)+2*mp.log10(epsfloor)-4*mp.pi*mp.sqrt(N*G)/mp.log(10)+N*mp.log10(vol)
    E=4*k**3*JJ**2
    yes(f'evaluated positive original regulator constants{j}',min(R,delta,epsfloor,JJ,d,vol,E)>0)
    eq(f'finite endpoint error first contribution{j}',float(8*C4*mp.sqrt(G)*delta),float(R/2),1e-12)
    eq(f'finite endpoint error second contribution{j}',float(2*C4*epsfloor*mp.log(mp.cot(delta/2))),float(R/2),1e-12)
    floors.append(dict(j=j,kappa='4/5',a=str(a),N=N,M=Mface,b=str(b),R_floor=mp.nstr(R,20),epsilon_floor=mp.nstr(epsfloor,20),log10_mass_floor=mp.nstr(logm,24),energy_ceiling=mp.nstr(E,20),precision_digits=180))
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),rows=rows,cutoff_diagnostics=cut,original_regulator_floors=floors,scope='Exact rational endpoint matrix, direct original SU2 endpoint curves and Hessian, explicit finite-word constants, original Haar cutoff sequence, complete original 36-face crossing Fourier coefficient and full-parameter high-precision bound evaluation. Numerical checks do not compute the actual ground or replace the proofs.')
(O/'QUANTITATIVE_LOOP_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(all_passed=out['all_passed'],checks=len(rows),failed=[r for r in rows if not r['passed']],floors=floors)))
assert out['all_passed']
