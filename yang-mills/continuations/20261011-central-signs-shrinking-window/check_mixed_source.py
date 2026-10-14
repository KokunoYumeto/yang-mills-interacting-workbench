from pathlib import Path
import json
import numpy as np
from scipy.special import iv,ivp
from scipy.linalg import expm
from scipy.integrate import quad_vec
O=Path(__file__).resolve().parent;rows=[]
def eq(name,a,b,tol=2e-9):
    err=float(np.max(np.abs(np.asarray(a)-np.asarray(b))));scale=1+float(np.max(np.abs(a)))+float(np.max(np.abs(b)))
    rows.append(dict(name=name,passed=bool(err<=tol*scale),error=err))
def le(name,a,b):rows.append(dict(name=name,passed=bool(a<=b+1e-9*(1+abs(a)+abs(b))),excess=float(a-b)))
chi=np.array([(-1.)**t.bit_count() for t in range(16)]);k=.8;lam=.23;E0=1.7;a=.017;phi=.6+.2j
Z=iv(1,4*lam)/(2*lam);Zp=2*ivp(1,4*lam)/lam-iv(1,4*lam)/(2*lam**2);meanT=Zp/(2*Z)
for T in [-1.95,-1.4,-.7,0,.3,.8,1.6,1.97]:
    G=4-T*T;Gp=-2*T;Gpp=-2.;lap=-3*T;up=lam*np.tanh(2*lam*T);upp=2*lam**2/np.cosh(2*lam*T)**2;uppp=-8*lam**3*np.tanh(2*lam*T)/np.cosh(2*lam*T)**2
    h=np.exp(lam*chi*T)/(4*np.sqrt(np.cosh(2*lam*T)));hp=h*(lam*chi-up);hpp=h*((lam*chi-up)**2-upp);hppp=h*((lam*chi-up)**3-3*(lam*chi-up)*upp-uppp)
    p=h*h;Q=np.eye(16)-np.outer(h,h);r=p@chi;rp=2*(h*hp)@chi;rpp=2*(hp*hp+h*hpp)@chi
    V=E0+k*(lam*lap*chi+lam**2*G);Vp=k*(-3*lam*chi-2*lam**2*T);v=V-p@V-k*G*np.dot(hp,hp)
    f=(1+.2j)*(T*T+.15*T**4);fp=(1+.2j)*(2*T+.6*T**3);fpp=(1+.2j)*(2+1.8*T*T);fppp=(1+.2j)*3.6*T
    drift=lap+2*G*up;driftp=-3+2*Gp*up+2*G*upp
    LAfp=-k*(Gp*fpp+G*fppp+driftp*fp+drift*fpp)
    b=-2*k*G*hp*fp;bp=-2*k*(Gp*hp*fp+G*hpp*fp+G*hp*fpp)
    bpp=-2*k*(Gpp*hp*fp+2*Gp*(hpp*fp+hp*fpp)+G*(hppp*fp+2*hpp*fpp+hp*fppp))
    direct=Q@(-k*(G*bpp+drift*bp)+v*b)
    Hcontract=hpp*fpp*G**2+(hpp*fp+hp*fpp)*(-T*G)+hp*fp*(6+1.5*T*T)
    Kcontract=hp*fp*(.5*G-2*upp*G**2+2*up*T*G)
    rhs=-2*k*G*hp*LAfp+2*k*Q@(h*Vp*G*fp)+4*k*k*Q@(Hcontract+Kcontract)
    eq(f'T{T} complete radius-two DB commutator',direct,rhs)
    # Actual centered face source for this explicitly constructed ground state.
    Ztau=a*phi*(meanT-chi*T)/2;x=p@Ztau;xp=-a*phi*(r+T*rp)/2;xpp=-a*phi*(2*rp+T*rpp)/2
    y=h*(Ztau-x);yp=hp*(Ztau-x)+h*(-a*phi*chi/2-xp)
    ypp=hpp*(Ztau-x)+2*hp*(-a*phi*chi/2-xp)-h*xpp
    Dy=Q@(-k*(G*ypp+drift*yp)+v*y)
    bx=-2*k*G*hp*xp;xi=h*(chi-r)
    proposed=3*k*y-bx+k*a*phi*(xi*G*up+Q@(chi*hp*G))
    eq(f'T{T} complete original face-source Dy',Dy,proposed)
    eq(f'T{T} preserved normalization',p.sum(),1.)
    eq(f'T{T} radius-two Hessian trace comparison',.5*(8*T*T-8),-3*G+(6+1.5*T*T)+.5*G)

for seed in range(8):
    rng=np.random.default_rng(2900+seed);n=5;q=rng.normal(size=(n,n))+1j*rng.normal(size=(n,n));D=q.conj().T@q+.3*np.eye(n);delta=np.linalg.eigvalsh(D)[0]
    b=rng.normal(size=n)+1j*rng.normal(size=n);y=rng.normal(size=n)+1j*rng.normal(size=n)
    for sigma in [.2,1.,2.7]:
        R=np.linalg.inv(D+sigma*np.eye(n));tail=np.vdot(D@b,R@D@y)/sigma**2
        eq(f'{seed} sigma{sigma} full resolvent tail',np.vdot(b,R@y),np.vdot(b,y)/sigma-np.vdot(b,D@y)/sigma**2+tail)
        le(f'{seed} sigma{sigma} entire tail bound',abs(tail),np.linalg.norm(D@b)*np.linalg.norm(D@y)/(sigma**2*(sigma+delta)))
    for t in [.07,.5]:
        remainder=quad_vec(lambda r:(t-r)*np.vdot(D@b,expm(-r*D)@D@y),0,t,epsabs=1e-11,epsrel=1e-11)[0]
        eq(f'{seed} t{t} exact mixed remainder',np.vdot(b,expm(-t*D)@y),np.vdot(b,y)-t*np.vdot(b,D@y)+remainder)
        le(f'{seed} t{t} full mixed bound',abs(remainder),(delta*t-1+np.exp(-delta*t))/delta**2*np.linalg.norm(D@b)*np.linalg.norm(D@y))

# Original j=1 open box, every boundary vertex/link and all oriented faces.
from itertools import product
L=1;vertices=list(product(range(2*L+1),repeat=3));edges=[]
for x in vertices:
    for d in range(3):
        if x[d]<2*L:edges.append((x,d))
lookup={v:i for i,v in enumerate(edges)};faces=[]
for x in vertices:
    for d in range(3):
        for e in range(d+1,3):
            if x[d]<2*L and x[e]<2*L:
                xd=list(x);xd[d]+=1;xe=list(x);xe[e]+=1
                faces.append([(lookup[x,d],1),(lookup[tuple(xd),e],1),(lookup[tuple(xe),d],-1),(lookup[x,e],-1)])
eq('original N count',len(edges),3*(2*L)*(2*L+1)**2);eq('original M count',len(faces),3*(2*L)**2*(2*L+1))
incidence=np.zeros(len(edges),dtype=int)
for face in faces:
    for i,sgn in face:incidence[i]+=1
le('all original boundary incidences',incidence.max(),4)
sigma=[np.array([[0,1],[1,0]]),np.array([[0,-1j],[1j,0]]),np.diag([1,-1])];generators=[-.5j*s for s in sigma]
rng=np.random.default_rng(381);U=[]
for edge in edges:
    q=rng.normal(size=4);q/=np.linalg.norm(q);U.append(q[0]*np.eye(2)-1j*sum(q[i+1]*sigma[i] for i in range(3)))
Tvals=[];derivs=[]
for ip,face in enumerate(faces):
    factors=[U[i] if s==1 else U[i].conj().T for i,s in face]
    value=np.trace(factors[0]@factors[1]@factors[2]@factors[3]).real;grad=np.zeros((len(edges),3))
    for kf,(edge,sgn) in enumerate(face):
        for alpha,Ta in enumerate(generators):
            ff=factors.copy();ff[kf]=Ta@U[edge] if sgn==1 else -U[edge].conj().T@Ta
            grad[edge,alpha]=np.trace(ff[0]@ff[1]@ff[2]@ff[3]).real
        eq(f'face{ip} original link{kf} gradient',np.dot(grad[edge],grad[edge]),1-value*value/4)
    eq(f'face{ip} full trace gradient',np.sum(grad**2),4-value*value)
    Tvals.append(value);derivs.append(grad)
derivs=np.array(derivs);bWilson=10000/k
for sample in range(5):
    eps=rng.choice([-1,1],size=len(edges));face_signs=np.array([np.prod([eps[i] for i,sgn in face]) for face in faces]);dV=-bWilson*np.einsum('p,pea->ea',face_signs,derivs)
    le(f'original sign sample{sample} full potential gradient',np.linalg.norm(dV),4*bWilson*np.sqrt(len(edges)))
    le(f'original sign sample{sample} every link potential gradient',np.linalg.norm(dV,axis=1).max(),4*bWilson)
out=dict(all_passed=all(r['passed'] for r in rows),checks=len(rows),scope='Full radius-two four-link constructed-ground commutator and original centered face source, including the complete 12-dimensional Hessian/Ricci contractions; full complex operator time/resolvent tails; every face, link and boundary incidence in the original j=1 open box. The continuous ground potential is explicitly constructed, not the Wilson vacuum. Original Wilson potential derivatives are checked separately without claiming a sampled ground state.',results=rows)
(O/'MIXED_SOURCE_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='results'}));print(json.dumps([r for r in rows if not r['passed']]));assert out['all_passed']
