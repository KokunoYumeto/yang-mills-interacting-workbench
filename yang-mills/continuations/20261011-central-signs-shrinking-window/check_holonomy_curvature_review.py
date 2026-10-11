"""Bounded independent algebra and ODE checks for HCR1-HCR7."""
from pathlib import Path
import json
import numpy as np
from scipy.linalg import expm
from scipy.integrate import solve_ivp,quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE=Path(__file__).resolve().parent
T=np.array([[[0,-.5j],[-.5j,0]],[[0,-.5],[.5,0]],[[-.5j,0],[0,.5j]]])

def op(A):return np.linalg.norm(A,2)
def comm(A,B):return A@B-B@A

def edge(A,x,d,a):
    def rhs(s,y):
        p=x.copy();p[d]+=s
        return (y.reshape(2,2)@A(p)[d]).ravel()
    return solve_ivp(rhs,(0,a),np.eye(2,dtype=complex).ravel(),rtol=1e-12,atol=1e-14).y[:,-1].reshape(2,2)

def main():
    rng=np.random.default_rng(10112026)
    checks={}
    checks['Pauli_bracket']=max(op(comm(T[d],T[(d+1)%3])-T[(d+2)%3]) for d in range(3))
    checks['double_bracket']=max(op(comm(T[d],comm(T[d],T[k]))+T[k]) for d in range(3) for k in range(3) if d!=k)
    finite_residual=0.;taylor_ratio=0.
    for _ in range(40):
        qd,qk=rng.uniform(-4,4,2);delta=rng.uniform(.01,1.5)
        X=qd*T[0];Y=qk*T[1];P=expm(delta*X)@expm(delta*Y)@expm(-delta*X)@expm(-delta*Y)
        deficit=2-np.trace(P).real
        exact=4*np.sin(delta*qd/2)**2*np.sin(delta*qk/2)**2
        finite_residual=max(finite_residual,abs(deficit-exact))
        M=max(op(X),op(Y));bound=32*M**3*delta**3/3
        taylor_ratio=max(taylor_ratio,op(P-np.eye(2)-delta**2*comm(X,Y))/bound)
    checks['finite_homogeneous_deficit']=finite_residual
    checks['maximum_Taylor_remainder_ratio']=taylor_ratio
    assert taylor_ratio<=1
    coeff=rng.normal(size=(3,3,4))*.2
    def A(p):return np.einsum('dkc,c,kab->dab',coeff,np.r_[1,p],T)
    def phi(p):return .17+.2*p[0]-.11*p[1]+.13*p[2]
    grad=np.array([.2,-.11,.13])
    def gauge(p):return expm(phi(p)*T[2])
    def Ah(p):
        h=gauge(p)
        return np.array([h@Ad@h.conj().T-grad[d]*T[2] for d,Ad in enumerate(A(p))])
    x=np.array([.13,-.24,.08]);a=.31;d=1
    end=x.copy();end[d]+=a
    U=edge(A,x,d,a);Uh=edge(Ah,x,d,a)
    checks['gauge_endpoint']=op(Uh-gauge(x)@U@gauge(end).conj().T)
    # Full error expansion HCR2.3, checked independently from r and delta.
    expansion_error=0.
    for _ in range(20):
        M,LA,ell,a=rng.uniform(.1,1.8,4)
        t=(ell/a)**.75;delta=a*t;r=32*M**3*delta**3/3+4*t*a*a*LA
        direct=4*M*M*delta*delta*r+r*r
        expanded=(128*M**5*ell**3.75*a**1.25/3+16*M*M*LA*ell**2.25*a**1.75
                  +1024*M**6*ell**4.5*a**1.5/9+256*M**3*LA*ell**3*a*a/3
                  +16*LA*LA*ell**1.5*a**2.5)
        expansion_error=max(expansion_error,abs(direct-expanded)/max(1,abs(direct)))
    checks['full_error_expansion_relative']=expansion_error
    lam=1.3;ell=.8;x0=.45;Ff=.7;radius=.6;J=Ff*radius**3
    quarter=quad(lambda theta:1/np.sqrt(1+np.sin(theta)**2),0,np.pi/2,epsabs=2e-13,epsrel=2e-13)[0]/lam
    period=4*quarter
    sol=solve_ivp(lambda t,y:[y[1],-2*y[0]**3],(0,period),[lam,0],rtol=2e-12,atol=2e-14,dense_output=True)
    tau=np.linspace(0,period,900);q,p=sol.sol(tau)
    checks['scalar_energy_error']=float(np.max(np.abs(p*p+q**4-lam**4)))
    checks['quarter_period_crossing']=float(abs(sol.sol(quarter)[0]))
    checks['period_return']=float(np.linalg.norm(sol.sol(period)-[lam,0]))
    assert checks['scalar_energy_error']<1e-9 and checks['period_return']<1e-9
    assert finite_residual<1e-12 and checks['gauge_endpoint']<1e-10
    assert expansion_error<1e-12
    js=np.arange(8000,12001,7);aa=1/(100*js);tj=(ell/aa)**.75
    phases=(tj*x0)%period;qj=sol.sol(phases)[0];delta=aa*tj
    receiver=12*J*np.sin(delta*qj/2)**4/aa
    profile=3*ell**3*J*qj**4/4
    checks['sample_receiver_max_remainder']=float(np.max(np.abs(receiver-profile)))
    result={'kind':'Bounded numerical checks of proved identities; no vacuum simulation','checks':checks,
            'figure_parameters':{'lambda':lam,'ell':ell,'fixed_x0':x0,'f_amplitude':Ff,'f_hat_radius':radius,'integral_f':J,'period':period},
            'f':'Ff product_i max(1-|x_i-o_i|/radius,0); radius/a=60j makes all three sampled sums exact',
            'all_assertions_passed':True}
    (HERE/'HOLONOMY_REVIEW_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    plt.rcParams.update({'font.size':10})
    fig,ax=plt.subplots(1,3,figsize=(16,4.7),layout='constrained')
    ax[0].plot(tau,q,label=r'$q_1=q_2=q_3=q$');ax[0].axhline(0,color='gray',lw=.7)
    for k in range(5):ax[0].axvline(k*quarter,color='gray',lw=.5,ls=':')
    ax[0].set(xlabel=r'Original ODE coordinate $\tau$ (length)',ylabel=r'$q(\tau)$',title='Exact periodic solution, illustrated numerically')
    ax[0].text(.05,.1,r'$P=\frac{4}{\lambda}\int_0^1\frac{du}{\sqrt{1-u^4}}$',transform=ax[0].transAxes);ax[0].legend()
    ax[1].plot(tau,3*ell**3*J*q**4/4,label='Proved receiver profile')
    ax[1].scatter(phases,receiver,s=8,alpha=.4,label='Exact original finite face receiver')
    ax[1].set(xlabel=r'Phase of $t_j x^0$ modulo $P$',ylabel=r'$a_j C_{f,j}$',title='Every phase is approached along subsequences')
    ax[1].legend(fontsize=8)
    ax[2].scatter(js,receiver,s=8,color='tab:orange')
    upper=3*ell**3*J*lam**4/4
    ax[2].axhline(0,color='black',ls='--',lw=.7);ax[2].axhline(upper,color='black',ls='--',lw=.7)
    ax[2].set(xlabel='Original regulator index j',ylabel=r'$a_j C_{f,j}$',title='Fixed physical coordinate $x^0=0.45$')
    fig.suptitle('Homogeneous classical comparison: exact faces and physical-time accumulation (HCR6–HCR7)',fontsize=14)
    fig.savefig(HERE/'PERIODIC_RECEIVER.png',dpi=165);fig.savefig(HERE/'PERIODIC_RECEIVER.svg')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
