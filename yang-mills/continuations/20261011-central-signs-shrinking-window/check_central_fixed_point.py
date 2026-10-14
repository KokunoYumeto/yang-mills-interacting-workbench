from pathlib import Path
import json,mpmath as mp,numpy as np
O=Path(__file__).resolve().parent;mp.mp.dps=45;rows=[]
def ck(name,x,y,tol=mp.mpf('1e-30')):
    err=abs(x-y);assert err<tol*max(1,abs(y)),(name,str(err))
    rows.append(dict(name=name,error=str(err)))
pauli=[np.array([[0,1],[1,0]],complex),np.array([[0,-1j],[1j,0]]),np.array([[1,0],[0,-1]],complex)]
for alpha in range(3):
    for beta in range(3):
        if alpha==beta:continue
        g=1j*pauli[beta];T=-.5j*pauli[alpha]
        ck('actual adjoint sign reversal in original basis',np.max(abs(g@T@g.conj().T+T)),0)
sign=np.array([1,1,-1,-1])
H=-.5*np.kron(np.outer(sign,sign),np.eye(3))
ck('full four-link trace Hessian',np.trace(H),-6)
ck('full four-link Hessian contraction',np.sum(H*H),12)
for r in map(mp.mpf,['.01','.2','1','2']):
    actual=mp.quad(lambda x:mp.sin(x/2)**2/mp.pi,[0,r])
    ck('radius-two probability Haar ball',actual,(r-mp.sin(r))/(2*mp.pi))
signs=[(-1)**v.bit_count() for v in range(16)]
weight=lambda u:2/mp.pi*mp.sqrt(1-u*u)
for t in map(mp.mpf,['.2','.7','1.3']):
    k=mp.mpf('1.7');E=mp.mpf('9')
    mass=mp.quad(lambda u:weight(u)*mp.exp(4*t*u),[-1,0,1])
    muT=mp.quad(lambda u:weight(u)*2*u*mp.exp(4*t*u),[-1,0,1])/mass
    A2=lambda T:mp.cosh(2*t*T)/mass
    h=[lambda T,sg=sg:mp.exp(t*sg*T)/mp.sqrt(16*mp.cosh(2*t*T)) for sg in signs]
    moment=lambda T:mp.tanh(2*t*T)
    V=lambda T:E+k*(-3*t*T+t*t*(4-T*T))
    for j in [1,4,13]:
        a=mp.mpf(1)/(100*j)
        for phi in [mp.mpc('1','.3'),mp.mpc('-.7','.9')]:
            # An explicit smooth central-even f tests the local differential
            # identity; it is not asserted to solve the Wilson resolvent.
            f=lambda T:mp.mpc('.3','-.2')*T*T
            Z=[lambda T,sg=sg:a*phi*(muT-sg*T)/2 for sg in signs]
            mean=lambda T:sum(h[i](T)**2*Z[i](T) for i in range(16))
            eta=[lambda T,i=i:h[i](T)*(Z[i](T)-mean(T))+2*k*mp.diff(h[i],T)*mp.diff(f,T)*(4-T*T) for i in range(16)]
            FF=lambda T:A2(T)*sum(abs(v(T))**2 for v in eta)
            T=mp.mpf(2);r=moment(T)
            norm=sum(abs(v(T))**2 for v in eta)
            ck('original central trace and residual covariance',norm,a*a*abs(phi)**2*(1-r*r))
            covV=sum(sg*h[i](T)**2*V(sg*T) for i,sg in enumerate(signs))-r*sum(h[i](T)**2*V(sg*T) for i,sg in enumerate(signs))
            ck('full central moment Laplacian for constructed potential',-6*mp.diff(moment,T),2*covV/k)
            first=2*A2(T)/k*sum(h[i](T)**2*abs(Z[i](T)-mean(T))**2*(V(sg*T)-E) for i,sg in enumerate(signs))
            second=-6*A2(T)*norm
            third=-4*k*a*A2(T)*mp.re(mp.conj(phi)*12*mp.diff(moment,T)*mp.diff(f,T))
            ck('entire central residual Laplacian with Hessian term',-6*mp.diff(FF,T),first+second+third)
rng=np.random.default_rng(141021)
for i in range(30):
    G=rng.normal(size=(8,8))+1j*rng.normal(size=(8,8));G[:,0]=0
    M=G.conj().T@G;v=rng.normal(size=8)+1j*rng.normal(size=8);z=.01+float(rng.random())
    m=np.vdot(v,v).real;e=np.vdot(v,M@v).real
    gain=np.vdot(v,np.linalg.solve(M+z*np.eye(8),v)).real
    assert gain+1e-11>=m*m/(e+z*m)>0
    rows.append(dict(name='full resolvent gain lower bound including zero direction',error=0))
out=dict(all_passed=True,checks=len(rows),scope='Exact original Pauli adjoint and four-link Hessian factors; radius-two Haar volumes; continuous four-link loop fixture with explicitly constructed potential V=E+kappa Delta(psi)/psi and a specified central-even test f, not the Wilson ground state or its resolvent. Finite positive matrices retain their zero direction. No regulator-uniform lower bound or continuum mass assigned.',details=rows)
(O/'CENTRAL_FIXED_POINT_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='details'}))
