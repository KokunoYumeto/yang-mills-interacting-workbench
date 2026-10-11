"""Exact finite algebra checks and numerical illustrations for HP1–HP40."""
from pathlib import Path
import json,datetime,hashlib
import sympy as S
import numpy as np
from scipy.integrate import quad,solve_ivp
from scipy.special import beta,betainc
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
checks=[]
def zero(name,expr):
    assert S.cancel(expr)==0,(name,S.cancel(expr))
    checks.append(name)
q,p,lam,ell,a,t,b,omega,A,Lambda=S.symbols(
    "q p lam ell a t b omega A Lambda",positive=True)
der=lambda f:p*S.diff(f,q)-2*q**3*S.diff(f,p)
def energy_reduce(expr):
    num,den=S.fraction(S.cancel(expr))
    return S.rem(num,S.Poly(p*p+q**4-lam**4,p),p).as_expr()/den
r=lam*p/(lam**2+q**2)
zero("HP13 first derivative",energy_reduce(der(r)+2*lam**3*q/(lam**2+q**2)))
zero("HP13 complete shifted ODE",energy_reduce(der(der(r))+2*r**3))
zero("HP13 squared quarter map",energy_reduce(r*r-lam**2*(lam**2-q**2)/(lam**2+q**2)))
zero("HP10 beta first moment",S.Rational(1,4)/S.Rational(3,4)-S.Rational(1,3))
zero("HP10 beta second moment",S.Rational(1,3)*S.Rational(5,4)/S.Rational(7,4)-S.Rational(5,21))
zero("HP10 full density variance",(ell**3/4)**2*lam**8*(S.Rational(5,21)-S.Rational(1,9))-ell**6*lam**8/126)
zero("HP24 covariance to squared-mean ratio",(ell**6*lam**8/126)/(ell**3*lam**4/12)**2-S.Rational(8,7))
for power in [8,9,10,12,14]:
    zero(f"HP29–HP36 uniform amplitude integral {power}",
         S.integrate(lam**power/Lambda,(lam,0,Lambda))-Lambda**power/(power+1))
zero("HP31 original window exponent",9*(-1-S.Rational(3,4))+S.Rational(63,4))
zero("HP33 relative error exponent",-S.Rational(1,2)+2*(-1-S.Rational(3,4))+4)
zero("HP31 raw observable exponent",-S.Rational(63,4)+2+S.Rational(55,4))
cut=b*Lambda/(2*omega*t)
err=ell**S.Rational(9,2)*S.sqrt(a)/24*S.sqrt(cut**13/(13*Lambda))
ref=S.sqrt(A)/3*(b/(omega*t))**S.Rational(9,2)
ratio=ell**S.Rational(9,2)*Lambda**6/(8*2**S.Rational(13,2)*S.sqrt(13*A))*S.sqrt(a)*(b/(omega*t))**2
zero("HP33 exact full relative coefficient",S.powdenest(err/ref-ratio,force=True))
zero("HP36 energy-error product",
     ell**S.Rational(9,2)*S.sqrt(a)*Lambda**6/(24*S.sqrt(13))
     *t*ell**S.Rational(9,2)*S.sqrt(a)*Lambda**7/(4*S.sqrt(15))
     -t*ell**9*a*Lambda**13/(96*S.sqrt(195)))

exact_algebra_checks=len(checks)
# All numerical values below are diagnostics or explicitly labeled samples.
ellv=1.;kappav=1.;lv=12.**.25
Iv,Ierr=quad(lambda u:1/np.sqrt(1-u**4),0,1,epsabs=1e-12,epsrel=1e-12)
period=4*Iv/lv;freq=2*np.pi/period
sol=solve_ivp(lambda x,y:[y[1],-2*y[0]**3],[0,period],[lv,0],
              rtol=2e-12,atol=2e-13,dense_output=True,max_step=period/2048)
assert sol.success
N=16384;phase=np.arange(N)*period/N;qq,pp=sol.sol(phase)
hv=ellv**3*qq**4/4
coef=np.fft.fft(hv)/N
var_exact=ellv**6*lv**8/126
assert abs(hv.mean()-ellv**3*lv**4/12)<2e-10
assert abs(np.var(hv)-var_exact)<2e-10
assert abs((pp*pp+qq**4-lv**4)).max()<2e-8
assert np.linalg.norm(sol.y[:,-1]-[lv,0])<2e-8
checks.extend(["HP2 numerical full-period and conserved energy",
               "HP10 independent phase quadrature of both moments"])
shift=np.roll(hv,-N//4)
quarter=ellv**3/4*lv**4*((lv*lv-qq**2)/(lv*lv+qq**2))**2
assert abs(shift-quarter).max()<2e-8
assert np.mean((hv-hv.mean())*(shift-hv.mean()))<0
checks.append("HP13–HP14 numerical quarter map and negative covariance")
samples=0;max_face_ratio=0.;max_derivative_ratio=0.
for jv in [4,9,37,103,509]:
    av=1/(100*jv);tv=(ellv/av)**.75;dv=av*tv
    for scale in [.07,.3,.85,1.]:
        qv=scale*qq[::97];pv=scale**2*pp[::97]
        z=dv*qv/2;h0=ellv**3*qv**4/4
        finite=h0*np.sinc(z/np.pi)**4
        hprime=(8*dv/av)*np.sin(z)**3*np.cos(z)*pv
        h0prime=ellv**3*qv**3*pv
        bound=ellv**4.5*np.sqrt(av)*(scale*lv)**6/24
        dbound=ellv**4.5*np.sqrt(av)*(scale*lv)**7/4
        max_face_ratio=max(max_face_ratio,float(np.max(abs(finite-h0))/bound))
        max_derivative_ratio=max(max_derivative_ratio,float(np.max(abs(hprime-h0prime))/dbound))
        assert np.max(abs(finite-h0))<=bound*(1+1e-8)
        assert np.max(abs(hprime-h0prime))<=dbound*(1+1e-8)
        samples+=len(qv)
checks.append("HP8 and HP35 amplitude-sensitive finite face and derivative samples")
n=np.arange(1,129)
AL=2*np.sum(abs(coef[n])**2/n**9)
BL=2*np.sum(n*abs(coef[n])**2)
DL=2*np.sum(n*n*abs(coef[n])**2)
tail_A=128/12*ellv**6*lv**12/(freq**4*128**12)
assert coef[2].real>0 and max(abs(coef[1:128:2]))<1e-10
hminus=3*kappav/4*(2-np.sqrt(3))
hplus=3*kappav/4*(2+np.sqrt(3))
cstar=min(betainc(.25,.5,hminus/(2*hplus)),1-betainc(.25,.5,.5))
assert cstar>0
cov=np.fft.ifft(abs(coef)**2*N).real-hv.mean()**2
av=1/3700;dv=ellv**.75*av**.25
finite=hv*np.sinc((dv*qq/2)/np.pi)**4
finite_cov=np.mean((finite-finite.mean())*(np.roll(finite,-N//4)-finite.mean()))
reflection_bound=4*(ellv**3*lv**4/4)*ellv**4.5*np.sqrt(av)*lv**6/24
assert abs(finite_cov-cov[N//4])<=reflection_bound
assert reflection_bound < -cov[N//4] and finite_cov<0
checks.append("HP39 finite original Wilson negative reflection square and retained error certificate")

fig,axes=plt.subplots(2,2,figsize=(13.6,9.1),constrained_layout=True)
ax=axes[0,0]
ax.plot(phase,hv,label=r"$h_\Lambda(\theta)=\ell^3q_\Lambda(\theta)^4/4$",color="#355e8b")
ax.axhline(hminus,color="#b55440",ls="--",label=r"CM necessary lower $h_-$")
ax.axhline(hplus,color="#b55440",ls=":",label=r"CM necessary upper $h_+$")
ax.axhline(1,color="#468465",ls="-.",label="Exact phase mean = 1")
ax.set(xlabel="Original phase coordinate theta",ylabel="Original orientation density",
       title="HP9–HP21: stationary phase crosses both vacuum bounds")
ax.legend(fontsize=8);ax.grid(alpha=.2)
ax=axes[0,1]
ax.plot(phase,cov,color="#705287")
ax.scatter([0,period/4],[var_exact,cov[N//4]],color="#b55440",zorder=3)
ax.axhline(0,color="gray",lw=.7)
ax.set(xlabel="Original phase displacement v",ylabel=r"$C_\Lambda(v)$",
       title="HP12–HP14: full covariance and exact quarter-period sign")
ax.grid(alpha=.2)
ax=axes[1,0]
js=np.geomspace(4,1e4,140);av=1/(100*js);tv=(ellv/av)**.75
window=kappav/js
J=1/8
mass=J*J*AL/9*(window/(freq*tv))**9
ax.loglog(js,mass,label=r"Reference weight for $a_jC$: $j^{-63/4}$",color="#355e8b")
ax.loglog(js,mass/av**2,label=r"Reference weight for raw $C$: $j^{-55/4}$",color="#ce8544")
ax.set(xlabel="Original lattice index j",ylabel="Window spectral mass under the specified phase law",
       title="HP29–HP33: original window kappa / j; positive mass tends to zero")
ax.legend(fontsize=8);ax.grid(alpha=.2,which="both")
ax.text(.03,.06,"Uniform amplitudes 0 < lambda < Lambda.\nFourier quadrature; exact series and finite-Wilson error in HP30–HP33.",
        transform=ax.transAxes,fontsize=8,bbox=dict(facecolor="white",alpha=.9,edgecolor="none"))
ax=axes[1,1];ax.axis("off")
ax.text(.03,.95,"Actual and comparison receiving maps",fontsize=13,fontweight="bold",va="top")
ax.text(.03,.83,
    "HP18: actual CM state gives zero to the witness;\n"
    "the stationary phase law gives strictly positive weight.\n\n"
    "HP34–HP36: positive phase-generator energy grows as t_j.\n"
    "HP37: actual quantum leading energy is O(a_j²).\n\n"
    "Phase averaging removes the exact covariance ell⁶ lambda⁸ / 126.\n"
    "The actual stationary leading CM law retains its own full covariance.\n\n"
    "HP39: direct Euclidean phase histories have a negative reflection form.\n"
    "These maps test the stationary construction.\n"
    "They do not identify the phase state or its generator with the vacuum.",
    fontsize=11,va="top",linespacing=1.55)
fig.suptitle("Stationary smooth solutions: exact measure, time and energy comparisons\n"
    "Illustration: ell = kappa = 1; Lambda = 12^(1/4). Window panel uses one orientation's compact tent test, J_j = 1/8 for j >= 4.",
    fontsize=13)
fig.savefig(ROOT/"STATIONARY_PHASE_MAP.png",dpi=155)
fig.savefig(ROOT/"STATIONARY_PHASE_MAP.svg")
plt.close(fig)
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),passed=True,
    exact_algebra_checks=exact_algebra_checks,checks=checks,numerical_face_samples=samples,
    maximum_face_error_to_bound=max_face_ratio,maximum_derivative_error_to_bound=max_derivative_ratio,
    illustration=dict(ell=ellv,kappa=kappav,Lambda=lv,I=Iv,I_quadrature_error=Ierr,period=period,
        coefficient_A_sample=AL,coefficient_B_sample=BL,coefficient_D_sample=DL,
        analytic_A_tail_bound_above_mode128=tail_A,
        caution="Tail bound excludes numerical quadrature error. Figures are numerical samples of fully proved formulas.",
        vacuum_interval=[hminus,hplus],uniform_violation_lower_bound_sample=cstar),
    script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    scope="Diagnostics supplement HP1–HP40; no actual quantum window coefficient is numerically assigned.")
(ROOT/"STATIONARY_PHASE_CHECKS.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf8")
print(json.dumps({k:out[k] for k in ['passed','exact_algebra_checks','numerical_face_samples','maximum_face_error_to_bound','maximum_derivative_error_to_bound']}))
