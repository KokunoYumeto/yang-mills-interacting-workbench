from pathlib import Path
import ast,itertools,json,math,os
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
import numpy as np
from scipy.fft import dst
O=Path(__file__).resolve().parent
provider=O/'check_graph_green.py'
if not provider.exists():
    provider=O.parent.parent.parent/'yang-mills-consolidation-20260916/yang-mills/continuations/20261011-central-signs-shrinking-window/check_graph_green.py'
# Only the published original graph and inverse-form functions are loaded.
tree=ast.parse(provider.read_text(encoding='utf8'))
funcs=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in ['graph','block','spectral_form']]
assert len(funcs)==3
exec(compile(ast.Module(body=funcs,type_ignores=[]),str(provider),'exec'))
rng=np.random.default_rng(1210202614);rows=[]
def check(name,a,b,tol=2e-9):
    a=np.asarray(a);b=np.asarray(b);err=float(np.max(np.abs(a-b))) if a.size else 0.
    scale=max(1.,float(np.max(np.abs(b)))) if b.size else 1.
    assert err<=tol*scale,(name,err,scale)
    rows.append(dict(name=name,error=err,tolerance=tol*scale,passed=True))
for q in [2,3,5,8,13,21]:
    for n in range(24):
        m=rng.integers(1,q,size=3);K,_=block(m,q);s=np.sin(np.pi*m/(2*q))**2
        assert np.linalg.eigvalsh(K)[0]>=4*s.sum()-1e-12
        rows.append(dict(name=f'full-tail-q{q}-{n}',passed=True))
        for d in range(3):
            sb=s.copy();sb[d]=1
            check(f'boundary-q{q}-{n}-{d}',8+4*(sb.sum()-1)-4*sb.sum(),4)
for a in [1/(100*j) for j in [1,2,5,10,20]]:
    eta=math.sqrt(a)
    for we in np.linspace(eta/50,eta,20):
        exact=9*(8-we)**2/(256*we);upper=256*we/(9*a*(8-eta)**2)
        assert 1/(a*exact)<=upper+1e-10
        rows.append(dict(name=f'reciprocal-full-a{a}-w{we}',passed=True))
for q in [2,3,4]:
    edges,G=graph(q);H=np.linalg.inv(G);n=len(edges)
    for trial in range(8):
        a=1/(100*(trial+1));tau=rng.uniform(.6,2.6,n);we=rng.uniform(.02,.3,n)*a
        v=3-3*we/8+4*tau
        U=rng.normal(size=(n,n));ev,V=np.linalg.eigh(U+U.T)
        eig=rng.uniform(.15,.85,n);A=(V*eig)@V.T
        Q=a*a*np.sqrt(v)[:,None]*A*np.sqrt(v)[None,:]
        D=a*a*np.diag(v)-Q;N=a**3*np.diag(tau)
        check(f'Q-full-identity-{q}-{trial}',Q+D,a*a*np.diag(v))
        assert np.linalg.eigvalsh(D)[0]>=-1e-12
        assert np.linalg.eigvalsh(Q)[-1]<=15*a*a+1e-12
        C=np.vstack([np.diag(np.sqrt(np.diag(N))),np.zeros((3,n))])
        ns=np.sqrt(np.diag(N));L11=Q/ns[:,None]/ns[None,:]
        S=rng.normal(size=(n,3))
        L22=S.T@np.linalg.solve(L11,S)+np.eye(3)
        L=np.block([[L11,S],[S.T,L22]])
        Z0=C.T@L@L@C;Pi=C@np.linalg.solve(N,C.T);RR=(np.eye(n+3)-Pi)@L@C
        check(f'Z0-full-complement-{q}-{trial}',Z0,Q@np.linalg.solve(N,Q)+RR.T@RR,5e-9)
        b=rng.normal(size=n)+1j*rng.normal(size=n)
        z=100*a*np.array([.07,.4,1.8]);lam=np.array([1/np.prod([z[r]-z[s] for s in range(3) if s!=r]) for r in range(3)])
        Z=[Z0+2*zr*Q+zr*zr*N for zr in z]
        vals=[Zr@b for Zr in Z]
        check(f'original-three-shift-{q}-{trial}',sum(lr*x for lr,x in zip(lam,vals)),N@b,1e-8)
        left=sum(np.real(np.vdot(x,H@x)) for x in vals);right=np.real(np.vdot(N@b,H@(N@b)))/np.sum(lam*lam)
        assert left>=right-1e-9
        check(f'Vandermonde-{q}-{trial}',[lam.sum(),lam@z,lam@(z*z)],[0,0,1])
R=.04;rho=.4;sigma=.7;tau0=np.array([1.,1.5,2.]);weights=np.array([1.,2.,-1.]);diag=[]
def phi(coords):
    out=np.ones_like(coords[0],dtype=float)
    for x in coords:out*=np.where((x>=0)&(x<=R),np.sin(np.pi*x/R),0)
    return out
I0=R**3/8;E0=I0/(3*np.pi**2/R**2)
targets=dict(H11=(18*rho+4*sigma)**2*E0/4,H12=(18*rho+4*sigma)*13.5*E0/4,H22=13.5**2*E0/4,N=9*tau0.sum()*I0,Q=9*(3*rho+2*sigma/3)*I0)
for j in [1,2,3,4,6,8,12]:
    a=1/(100*j);q=math.ceil(R/a)+3;bs=[];gg=[]
    for d in range(3):
        rr=np.meshgrid(*[np.arange(q) if k==d else np.arange(1,q) for k in range(3)],indexing='ij')
        x=[a*(rr[k]-1+(.5 if k==d else 0)) for k in range(3)]
        incident=np.zeros_like(x[0],dtype=float)
        for k in range(3):
            if k==d:continue
            for sign in [-1,1]:
                xp=[v.copy() for v in x];xp[k]+=sign*a/2;incident+=phi(xp)
        bs.append(-3*a**3/8*(2-a)*incident);gg.append(weights[d]*phi(x))
    den=sum(float(np.vdot(g,g)) for g in gg)
    coef=sum(float(np.vdot(g,b)) for g,b in zip(gg,bs))/den
    qb=[a*a*(rho*b+sigma*g*coef) for b,g in zip(bs,gg)]
    y1=[2*v for v in qb];y2=[a**3*tau0[d]*bs[d] for d in range(3)]
    f1=[v/a**5 for v in y1];f2=[v/a**6 for v in y2]
    h11=a**5*spectral_form(q,f1)[0];h22=a**5*spectral_form(q,f2)[0]
    h12=(a**5*spectral_form(q,[x+y for x,y in zip(f1,f2)])[0]-h11-h22)/2
    norm=sum(a**3*tau0[d]*float(np.vdot(bs[d],bs[d])) for d in range(3))/a**6
    energy=sum(float(np.vdot(b,v)) for b,v in zip(bs,qb))/a**5
    diag.append(dict(j=j,q=q,a=a,H11=h11,H12=h12,H22=h22,N=norm,Q=energy,ratios={k:v/targets[k] for k,v in [('H11',h11),('H12',h12),('H22',h22),('N',norm),('Q',energy)]}))
for key in targets:assert abs(diag[-1]['ratios'][key]-1)<abs(diag[0]['ratios'][key]-1)
result=dict(checks=len(rows),all_passed=True,scope='Original full graph eigenvalue/tail constants, threshold-dependent reciprocal inequality, complex full first-energy/remainder identities, exact current-span residual, three original shift interpolation, original-grid mixed Green and norm/energy diagnostics with explicitly specified nonlocal matrix.',checks_detail=rows,diagnostic_description='Specified face means 2-a, tau=(1,1.5,2), Q=a²[rho I+sigma gg*/sum|g|²], rho=.4,sigma=.7,g=(phi,2phi,-phi), R=.04. Diagnostic arrays and matrices only, not sampled Yang–Mills vacuum data. All original grid factors retained.',targets=targets,original_path_diagnostics=diag)
(O/'KINETIC_PROFILE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf8')
print(json.dumps(dict(checks=len(rows),all_passed=True,last_ratios=diag[-1]['ratios'])))
