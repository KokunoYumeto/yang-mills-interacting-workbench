"""Bounded independent checks of SM2, SM4, SM6, SM7 and SM10.

Numerical samples are illustrations. General results are proved in the note.
"""
from pathlib import Path
import hashlib
import json
from datetime import datetime, timezone
import math
import numpy as np
import sympy as sp
from scipy.integrate import quad
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent
checks = []
def exact(expr, name):
    residual = sp.expand(expr)
    assert residual == 0, (name, residual)
    checks.append(name)

# Preserve the fractional powers by checking with a=a4**4 and ell=l4**4.
a4, l4, M, L = sp.symbols('a4 l4 M L', positive=True)
a, ell = a4**4, l4**4
t, delta = (l4/a4)**3, a4*l4**3
R = sp.Rational(32,3)*M**3*delta**3 + 4*t*a**2*L
E = (4*M**2*delta**2*R + R**2)/a
displayed = (sp.Rational(128,3)*M**5*l4**15*a4
             +16*M**2*L*l4**9*a4**3
             +sp.Rational(1024,9)*M**6*l4**18*a4**2
             +sp.Rational(256,3)*M**3*L*l4**12*a4**4
             +16*L**2*l4**6*a4**6)
exact(E-displayed, 'SM4.2 every full-square coefficient')

# Independent local SU(2) colour-vector calculation. The three affine
# amplitudes are exact polynomial probes; they are not compact templates.
x, y, z, s = sp.symbols('x y z s', real=True)
coords = [x,y,z]
amps = [1+x+2*y, 2+y+z, 3+z+x]
B = [sp.Matrix([amps[i] if c == i else 0 for c in range(3)]) for i in range(3)]
zero = sp.zeros(3,1)
def expanded(v):
    return v.applyfunc(sp.expand)
def D(A, i, v):
    return expanded(v.diff(coords[i]) + A[i].cross(v))
def curvature(A,k,i):
    return expanded(A[i].diff(coords[k])-A[k].diff(coords[i])+A[k].cross(A[i]))
F = [[curvature(B,k,i) for i in range(3)] for k in range(3)]
J = [expanded(sum((D(B,k,F[k][i]) for k in range(3)), zero)) for i in range(3)]
C = [v/2 for v in J]
G = [[expanded(D(B,k,C[i])-D(B,i,C[k])) for i in range(3)] for k in range(3)]
H = [[expanded(C[k].cross(C[i])) for i in range(3)] for k in range(3)]
R2 = [expanded(sum((D(B,k,G[k][i])+C[k].cross(F[k][i]) for k in range(3)),zero)) for i in range(3)]
R4 = [expanded(sum((D(B,k,H[k][i])+C[k].cross(G[k][i]) for k in range(3)),zero)) for i in range(3)]
R6 = [expanded(sum((C[k].cross(H[k][i]) for k in range(3)),zero)) for i in range(3)]
Ah = [expanded(B[i]+s*s*C[i]) for i in range(3)]
Fh = [[curvature(Ah,k,i) for i in range(3)] for k in range(3)]
for k in range(3):
    for i in range(k+1,3):
        for c in range(3):
            exact(Fh[k][i][c]-F[k][i][c]-s*s*G[k][i][c]-s**4*H[k][i][c], f'SM10.4 curvature {k}{i} colour {c}')
gauss = expanded(sum((D(Ah,i,s*J[i]) for i in range(3)),zero))
for c in range(3):
    exact(gauss[c], f'SM10.3 exact Gauss colour {c}')
for i in range(3):
    residual = expanded(-Ah[i].diff(s,2)+sum((D(Ah,k,Fh[k][i]) for k in range(3)),zero))
    for c in range(3):
        exact(residual[c]-s*s*R2[i][c]-s**4*R4[i][c]-s**6*R6[i][c], f'SM10.5 full residual {i} colour {c}')
source6 = sum(J[i].dot(R6[i]) for i in range(3))
squareH = sum(H[k][i].dot(H[k][i]) for k in range(3) for i in range(k+1,3))
exact(source6+4*squareH, 'SM10.8 sixth source contraction including coefficient 4')

# Exact algebraic product identities sampled with all three different inputs.
rng = np.random.default_rng(270011)
ell_num = 0.9
sigma = 0.02
density_samples = np.exp(rng.uniform(-12,12,size=(64,3)))
factor_max_relative_error = 0.0
def factors(rhos):
    u,v,w = np.asarray(rhos)
    return np.sqrt(2)*ell_num**(-0.75)*np.array([(u*v/w)**0.25,(u*w/v)**0.25,(v*w/u)**0.25])
for row in density_samples:
    lam = factors(row)
    result = ell_num**3/4*np.array([lam[0]**2*lam[1]**2,lam[0]**2*lam[2]**2,lam[1]**2*lam[2]**2])
    error = np.max(np.abs(result/row-1))
    factor_max_relative_error = max(factor_max_relative_error,float(error))
    assert error < 2e-14

# Product compact mollifier from SM2, with its actual integral retained.
def raw(u):
    return math.exp(-1/(1-u*u)) if abs(u)<1 else 0.0
Z, Zerr = quad(raw,-1,1,epsabs=1e-13,epsrel=1e-13)
def beta(u):
    return raw(float(u))/Z
def tent(v):
    return max(0.0,1-abs(v)/0.6)
def integral_factor(atom,h):
    points = sorted(v for v in [(-0.6-atom)/h,-atom/h,(0.6-atom)/h] if -1<v<1)
    val, err = quad(lambda u: beta(u)*tent(atom+h*u),-1,1,points=points,epsabs=2e-12,epsrel=2e-12)
    return val
stages = [1,2,4,8,16,32,64]
target = np.array([7/12,7/8,0.3*0.6**3])
rows = []
for r in stages:
    h,eps = ell_num/r,sigma/r
    floor = eps*0.6**3
    atomic1 = integral_factor(-0.25,h)*integral_factor(0,h)**2
    atomic2 = 1.5*integral_factor(0.25,h)*integral_factor(0,h)**2
    values = np.array([atomic1+floor,atomic2+floor,(0.3+eps)*0.6**3])
    rows.append({'r':r,'h':h,'epsilon':eps,'test_integrals':values.tolist(),'target':target.tolist()})
assert np.max(np.abs(np.array(rows[-1]['test_integrals'])-target)) < 0.03
assert np.max(np.abs(np.array(rows[-1]['test_integrals'])-target)) < np.max(np.abs(np.array(rows[0]['test_integrals'])-target))

# An intentionally larger sufficient schedule, checked with exact rationals.
# SM12 proves every conservative kernel and root bound used here.
from fractions import Fraction as Q
e=Q(9,10)
sig=Q(1,50)
alpha=[Q(1,4),Q(3,4),Q(1,2),Q(1),Q(3,2),Q(1)]
def ceilq(v):
    return -(-v.numerator//v.denominator)
def ceil_fourth_root(v):
    lo,hi=0,1
    while hi**4*v.denominator < v.numerator: hi*=2
    while hi-lo>1:
        mid=(lo+hi)//2
        if mid**4*v.denominator >= v.numerator: hi=mid
        else: lo=mid
    assert hi**4*v.denominator >= v.numerator
    assert (hi-1)**4*v.denominator < v.numerator
    return hi
schedule=[]
previous=0
exact_schedule_checks=0
for r in [1,2,3,4,5,6,7,8]:
    h=e/r; eps=sig/r
    mass=Q(5,2)+Q(3,10)*(2*(2*r+2)*e)**3
    R0=eps+512*h**(-3)*mass
    R1=8192*h**(-4)*mass
    LL=Q(5,3)*ceil_fourth_root(R0**2/eps)
    Mv=LL/2
    Lv=LL/2*(32/(r*e)+3*R1/(4*eps))
    Gv=4*32/(r*e)*R0+R1
    V=(2*(2*r+2)*e)**3
    tau=sig*e**3/r
    # ell<1 and sqrt(3)/2<1: these rational coefficients bound every beta.
    coeff=[Q(128,3)*Mv**5,16*Mv**2*Lv,Q(1024,9)*Mv**6,
           Q(256,3)*Mv**3*Lv*e**3,16*Lv**2,R0/e+Gv]
    thresholds=[max(1,ceilq(6*V*b/tau)) for b in coeff]
    J=max(previous+1,r,ceilq(1/(100*e)),ceilq(100*(2*r+3)*e),*(v**4 for v in thresholds))
    aj=Q(1,100*J)
    for b,p in zip(coeff,alpha):
        exact_ratio=(6*V*b/tau)**p.denominator*aj**p.numerator
        assert exact_ratio<=1
        exact_schedule_checks+=1
    assert aj<=e and Q(J**3,100)>=(2*r+3)*e
    schedule.append({'r':r,'admissible_J':str(J),'log10_J':math.log10(J),
                     'six_exact_term_bounds':'Each term is at most tau/6; checked by integer cross multiplication.',
                     'limitation':'An intentionally larger sufficient schedule, not the least integer in SM6.2.'})
    previous=J

# Scientific illustration: exact input measures, actual mollified profiles,
# full positive factors, all signed test factors retained, and finite bounds.
fig, axes = plt.subplots(2,2,figsize=(13.8,9.4), constrained_layout=True)
grid=np.linspace(-0.8,0.8,1001)
styles=[(2,'#38598b'),(8,'#ef8354'),(32,'#248277')]
for r,col in styles:
    h,eps=ell_num/r,sigma/r
    rho12=np.array([h**(-3)*beta((v+0.25)/h)*beta(0)**2+eps for v in grid])
    rho13=np.array([1.5*h**(-3)*beta((v-0.25)/h)*beta(0)**2+eps for v in grid])
    rho23=np.full_like(grid,0.3+eps)
    lam=factors([rho12,rho13,rho23])
    axes[0,0].plot(grid,rho12,color=col,label=f'r={r}, channel 12')
    axes[0,0].plot(grid,rho13,color=col,ls='--',label=f'r={r}, channel 13')
    axes[0,1].plot(grid,lam[0],color=col,label=f'r={r}, lambda 1')
    axes[0,1].plot(grid,lam[2],color=col,ls='--',label=f'r={r}, lambda 3')
axes[0,0].set_yscale('log'); axes[0,1].set_yscale('log')
axes[0,0].set_title('SM2: separate atomic supports and a positive floor')
axes[0,1].set_title('SM2.2–SM3: full smooth amplitude factors')
for ax in axes[0]:
    ax.set_xlabel('Original x coordinate on y=z=0'); ax.legend(ncol=2,fontsize=8)
    ax.grid(alpha=0.2)
axes[0,0].set_ylabel('rho on the indicated slice')
axes[0,1].set_ylabel('lambda; cutoff equals one on this slice')
values=np.array([v['test_integrals'] for v in rows])
for k,label in enumerate(['12: one atom','13: mass 3/2 atom','23: density 3/10']):
    line=axes[1,0].plot(stages,values[:,k],'o-',label=label)[0]
    axes[1,0].axhline(target[k],ls=':',color=line.get_color())
axes[1,0].set_xscale('log',base=2)
axes[1,0].set_xlabel('Smoothing stage r'); axes[1,0].set_ylabel('Integral of the original compact tent test')
axes[1,0].set_title('SM7: mollified test integrals approach the measure values')
axes[1,0].legend(fontsize=8);axes[1,0].grid(alpha=0.2)
axes[1,1].plot([v['r'] for v in schedule],[v['log10_J'] for v in schedule],'o-',color='#805a9c')
axes[1,1].set_xlabel('Smoothing stage r');axes[1,1].set_ylabel('log10 of an admissible original lattice index J')
axes[1,1].set_title('SM6: finite sufficient schedule; no practical-size assertion')
axes[1,1].grid(alpha=0.2)
fig.suptitle('Arbitrary positive measures → smooth templates → original Wilson faces\n'
             'Illustration: nu12=delta(-1/4,0,0), nu13=(3/2)delta(1/4,0,0), nu23=(3/10) dx; ell=9/10, sigma*=1/50', fontsize=13)
fig.savefig(HERE/'SMOOTH_MEASURE_RECEIVER.png',dpi=160)
fig.savefig(HERE/'SMOOTH_MEASURE_RECEIVER.svg')
plt.close(fig)

result={'time_utc':datetime.now(timezone.utc).isoformat(),'status':'passed',
        'exact_symbolic_checks':len(checks),'checks':checks,
        'factor_samples':64,'factor_max_relative_error':factor_max_relative_error,
        'exact_schedule_checks':exact_schedule_checks,
        'mollifier_integral':Z,'mollifier_quadrature_error':Zerr,
        'test_samples':rows,'schedule_samples':schedule,
        'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'limits':'Finite symbolic and numerical checks supplement SM1–SM11 proofs. No finite lattice vacuum law or source-free dynamics is asserted.'}
(HERE/'SMOOTH_MEASURE_CHECKS.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','exact_symbolic_checks','factor_samples','factor_max_relative_error']},indent=2))
