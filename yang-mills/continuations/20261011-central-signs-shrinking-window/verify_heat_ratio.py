from pathlib import Path
from datetime import datetime, timezone
import json, hashlib, math
import mpmath as mp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
mp.mp.dps=160
pi=mp.pi

def multiplier(t):
    return 2*mp.sqrt(pi)*mp.exp(t/4)/t**mp.mpf('1.5')

def spectral(t,theta):
    nmax=int(mp.ceil(mp.sqrt(4*(180*mp.log(10))/t+1)))+3
    if theta==0:
        return mp.fsum(n*n*mp.exp(-t*(n*n-1)/4) for n in range(1,nmax+1))
    if theta==pi:
        return mp.fsum((-1)**(n-1)*n*n*mp.exp(-t*(n*n-1)/4) for n in range(1,nmax+1))
    return mp.fsum(n*mp.exp(-t*(n*n-1)/4)*mp.sin(n*theta)/mp.sin(theta) for n in range(1,nmax+1))

def images(t,theta):
    kmax=int(mp.ceil(mp.sqrt(t*(180*mp.log(10)))/(2*pi)))+4
    if theta==0:
        val=1+2*mp.fsum((1-8*pi*pi*k*k/t)*mp.exp(-4*pi*pi*k*k/t) for k in range(1,kmax+1))
    elif theta==pi:
        val=2*mp.fsum((2*(2*k+1)**2*pi*pi/t-1)*mp.exp(-(2*k+1)**2*pi*pi/t) for k in range(kmax+1))
    else:
        val=mp.fsum((theta+2*pi*k)*mp.exp(-(theta+2*pi*k)**2/t) for k in range(-kmax,kmax+1))/mp.sin(theta)
    return multiplier(t)*val

def stable_log_ratio(t):
    if t<=4:
        return mp.log(images(t,0))-mp.log(images(t,pi))
    nmax=int(mp.ceil(mp.sqrt(4*(180*mp.log(10))/t+1)))+3
    tailplus=mp.fsum(n*n*mp.exp(-t*(n*n-1)/4) for n in range(2,nmax+1))
    tailminus=mp.fsum((-1)**(n-1)*n*n*mp.exp(-t*(n*n-1)/4) for n in range(2,nmax+1))
    return mp.log1p(tailplus)-mp.log1p(tailminus)

def fmt(x):
    return mp.nstr(x,30)

comparisons=[]
for ts in ['0.3','0.5','1','2','4','6','8']:
    t=mp.mpf(ts)
    for factor in [0,mp.mpf('0.1'),mp.mpf('0.5'),mp.mpf('0.9'),1]:
        theta=pi*factor
        a,b=spectral(t,theta),images(t,theta)
        error=abs(a-b)/b
        assert error<mp.mpf('1e-120'), (t,theta,error)
        comparisons.append({'tau':ts,'theta_over_pi':fmt(factor),'relative_error':fmt(error)})

ratio_samples=[]
for i in range(181):
    t=mp.power(10,-3+mp.mpf(i)/30)
    logr=stable_log_ratio(t)
    assert 0<logr<pi*pi/t
    if t<=pi*pi:
        # The strict image-series improvement is exponentially smaller than
        # 160-digit arithmetic at the smallest times. Record finite precision.
        sharp_upper=pi*pi/t-mp.log(2*(2*pi*pi/t-1))
        assert logr<=sharp_upper+mp.mpf('1e-145')*max(1,abs(sharp_upper))
    if t>=4:
        assert logr<4/t
    ratio_samples.append({'tau':fmt(t),'log_R':fmt(logr),'pi_squared_over_tau':fmt(pi*pi/t)})

endpoint_checks=[]
for ts in ['0.5','1','4','8']:
    t=mp.mpf(ts)
    eps=mp.mpf('1e-30')
    for endpoint in [0,pi]:
        near=eps if endpoint==0 else pi-eps
        error=abs(images(t,near)/images(t,endpoint)-1)
        assert error<mp.mpf('1e-55')
        endpoint_checks.append({'tau':ts,'endpoint_angle':fmt(endpoint),'angle_offset':fmt(eps),'relative_difference':fmt(error)})

haar_checks=[]
for ts in ['0.5','2','8']:
    t=mp.mpf(ts)
    integral=(2/pi)*mp.quad(lambda theta:images(t,theta)*mp.sin(theta)**2,[0,pi/4,pi/2,3*pi/4,pi])
    assert abs(integral-1)<mp.mpf('1e-130')
    haar_checks.append({'tau':ts,'integral':fmt(integral),'absolute_error':fmt(abs(integral-1))})

asymptotics=[]
for ts in ['0.1','0.01','0.001','0.0001']:
    t=mp.mpf(ts)
    asymptotics.append({'tau':ts,'tau_log_R':fmt(t*stable_log_ratio(t)),'pi_squared':fmt(pi*pi)})

source=ROOT.parent/'independent_jacobian'/'local_score_improvement'/'private_sources'/'0802.3320v1'
source_hashes={name:hashlib.sha256((source/name).read_bytes()).hexdigest() for name in ['original_author_source.tex','original_source_download']}
ledger={
    'source_id':'arXiv:0802.3320v1',
    'canonical_index_status':'No exact identifier hit in the two existing canonical indexes; indexed neighboring works remain routing records only.',
    'authors':['Fabrice Baudoin','Michel Bonnefont'],
    'title':'The subelliptic heat kernel on SU(2): Representations, Asymptotics and Gradient bounds',
    'source_url':'https://arxiv.org/src/0802.3320v1',
    'local_directory':str(source),
    'hashes':source_hashes,
    'structure_read':'Sections 1–4 identified; exact needed portions below read.',
    'reading_coverage':[{'lines':'155–200','content':'Pauli matrices and complete Riemannian versus two-field generators'},{'lines':'414–496','content':'Chebyshev spectral kernel, Haar factor, identification as Riemannian kernel, first and second Gaussian image expressions'}],
    'receiving_result':'HEAT_RATIO_PROOF.md HR2–HR10, HR24–HR25',
    'comparison_proved':'Source full Riemannian generator is 4 Delta; p_tau(theta)=q_(tau/4)(cos theta).',
    'source_correction':'v1 line 494 has a plus sign in its second image expression where pairing the first expression proves a minus sign; HR25 proves the exact corrected identity. The first source image expression is correct.',
    'unread':'All source results on subelliptic asymptotics and subelliptic gradient inequalities; no use made.',
    'archive_preserved':True,
}
(ROOT/'SOURCE_READING_LEDGER.json').write_text(json.dumps(ledger,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')

checks={
    'generated_utc':datetime.now(timezone.utc).isoformat(),
    'precision_decimal_digits':mp.mp.dps,
    'status':'all numerical assertions passed; analytic proof is HR2–HR25',
    'truncation':'Spectral n ceiling sqrt(4*180*log(10)/tau+1)+3; image |k| ceiling sqrt(tau*180*log(10))/(2*pi)+4. Only verification uses these finite sums.',
    'small_time_strictness':'HR11 checked with relative tolerance 1e-145 because its strictly positive remainder can be smaller than the 160-digit rounding scale. Strictness is proved analytically.',
    'series_comparisons':comparisons,
    'ratio_samples':ratio_samples,
    'endpoint_checks':endpoint_checks,
    'haar_integrals':haar_checks,
    'sharp_coefficient_samples':asymptotics,
}
(ROOT/'HEAT_RATIO_CHECKS.json').write_text(json.dumps(checks,indent=2)+'\n',encoding='utf-8')

plt.rcParams.update({'font.size':10,'axes.spines.top':False,'axes.spines.right':False})
fig,ax=plt.subplots(1,2,figsize=(12.8,4.8),layout='constrained')
theta_values=[pi*i/200 for i in range(201)]
for ts in ['1','4','10']:
    t=mp.mpf(ts)
    values=[float(mp.log(images(t,q) if t<=4 else spectral(t,q))) for q in theta_values]
    ax[0].plot([float(2*q) for q in theta_values],values,label=rf'$\tau={ts}$')
ax[0].set(xlabel=r'Physical distance $d=2\theta$',ylabel=r'$\log p_\tau(d/2)$',title='Original probability-Haar kernel (HR2–HR10)')
ax[0].set_xticks([0,float(pi),float(2*pi)],['0',r'$\pi$',r'$2\pi$'])
ax[0].legend()
plot_t=[mp.power(10,-1+mp.mpf(i)*mp.log10(300)/220) for i in range(221)]
ax[1].loglog([float(t) for t in plot_t],[float(stable_log_ratio(t)) for t in plot_t],label=r'$\log[p_\tau(0)/p_\tau(\pi)]$ (exact series)',lw=2)
ax[1].loglog([float(t) for t in plot_t],[float(pi*pi/t) for t in plot_t],'--',label=r'$\pi^2/\tau$ (proved bound)')
ax[1].set(xlabel=r'Original heat time $\tau$',ylabel='Logarithm of the global ratio',title='All-time inequality and sharp short-time coefficient')
ax[1].legend(fontsize=9)
for a in ax:
    a.grid(alpha=.2)
fig.suptitle(r'Radius-two $SU(2)$: $T_\alpha=-i\sigma_\alpha/2$, $\Delta=\sum_\alpha X_\alpha^2$',fontsize=13)
fig.savefig(ROOT/'HEAT_RATIO_FIGURE.png',dpi=170)
plt.close(fig)
print(json.dumps({'series_comparisons':len(comparisons),'ratio_checks':len(ratio_samples),'endpoint_checks':len(endpoint_checks),'haar_checks':len(haar_checks),'maximum_series_relative_error':max(float(x['relative_error']) for x in comparisons),'result':'passed'},indent=2))

proof=(ROOT/'HEAT_RATIO_PROOF.md').read_text(encoding='utf-8')
bad=[(i,ord(c)) for i,c in enumerate(proof) if ord(c)<32 and c not in '\n\r\t']
assert not bad,bad
