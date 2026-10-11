"""Bounded independent algebra checks; no replacement of the interacting law."""
from pathlib import Path
import json
import math
import sympy as s

root = Path(__file__).resolve().parent
checks = []

def exact(label, expression):
    reduced = s.simplify(expression)
    assert reduced == 0, (label, reduced)
    checks.append(label)

def ordered(label, lower, upper):
    assert lower <= upper + 2e-10 * max(1.0, abs(lower), abs(upper)), (label, lower, upper)
    checks.append(label)

r, z, D, gamma = s.symbols('r z D gamma', real=True)
mixed = (s.I*r*D + r**2*gamma)*(-s.I*z*D + z**2*gamma)
exact('mixed phase second moment sign', mixed - (r*z*D**2 + r**2*z**2*gamma**2 + s.I*r*z*(z-r)*D*gamma))
exact('diagonal second moment', mixed.subs(z,r) - (r**2*D**2 + r**4*gamma**2))

l, p, Q, x, M = s.symbols('l p Q x M', positive=True)
R = 2*(Q+p/l)
q = l**2/(p+Q*l)
exact('spectral minorant receiving coefficient', 4*((R-Q)*l-p)/R**2-q)
exact('finite interval first moment', l-l/4-(p+Q*l)/R-l/4)
exact('mass monotonicity derivative', s.diff(x*x/(p+Q*x),x)-x*(2*p+Q*x)/(p+Q*x)**2)
exact('tail monotonicity derivative', s.diff((x-M)**2/(p+Q*x),x)-(x-M)*(2*p+Q*x+Q*M)/(p+Q*x)**2)
rr, ss = s.symbols('rr ss', positive=True)
Rband = R/(1-rr)
exact('moving band mass', ((1-rr)*l-(p+Q*l)/Rband)/Rband-q*(1-rr)**2/4)
exact('band optimizer derivative', s.diff((1-rr)/ss-1/ss**2,ss).subs(ss,2/(1-rr)))

a, ell, ef, Hf, k, Rf, theta = s.symbols('a ell ef Hf k Rf theta', positive=True)
ce, cp, cq, cr = s.symbols('ce cp cq cr', positive=True)
Elow = ef+ce*a
Pval = Hf/a+cp
Qval = 4/a+cq
Rval = Rf+cr*a
for name, theta2 in [('critical',ell/a),('supercritical',1/a**2)]:
    lv = theta2*Elow
    pv = theta2*Pval+k*k*theta2**2*Rval
    qv = lv**2/(pv+Qval*lv)
    rv = 2*(Qval+pv/lv)
    Z = ((Hf+4*ef)/ell if name == 'critical' else 0)+k*k*Rf
    exact(name+' loss coefficient limit', s.limit(qv,a,0,dir='+')-ef**2/Z)
    exact(name+' energy-window limit', s.limit(rv/(2*theta2),a,0,dir='+')-Z/ef)
lv = theta**2*Elow
pv = theta**2*Pval+k*k*theta**4*Rval
exact('fixed phase mass limit', s.limit((lv**2/(pv+Qval*lv))/a,a,0,dir='+')-theta**2*ef**2/(Hf+4*ef))
exact('fixed phase window limit', s.limit(a*2*(Qval+pv/lv),a,0,dir='+')-2*(Hf/ef+4))

# Finite measures only test the universal moment-receiver inequalities.
# No such measure is asserted to be the original Yang--Mills law or spectrum.
spectra = [
    ([0.01,0.3,4.0,50.0],[0.2,0.3,0.1,0.1]),
    ([1.0,2.0,3.0],[0.1,0.2,0.7]),
    ([0.1,1.0,1000.0],[0.9,0.01,0.001]),
    ([4.0],[0.8]),
    ([0.0001,0.1,3.0],[0.01,0.01,0.01]),
]
for si,(lam,weights) in enumerate(spectra):
    G = sum(weights)
    E = sum(w*v for w,v in zip(weights,lam))
    E2 = sum(w*v*v for w,v in zip(weights,lam))
    for lf in [0.05,0.4,0.9,1.0]:
        lv = lf*E
        for qf in [0.01,0.3,0.99,1.1]:
            Qv = qf*E2/E
            pv = max(0.0,E2-Qv*E)+0.001*E2
            den = pv+Qv*lv
            qv = lv*lv/den
            rv = 2*den/lv
            key = f'{si}/{lf}/{qf}'
            ordered('total mass '+key,qv,G)
            window = sum(w for w,v in zip(weights,lam) if v <= rv)
            ordered('spectral window '+key,qv,window)
            for tv in [0.00001,0.01,0.3,10.0]:
                dec = sum(w*(-math.expm1(-tv*v)) for w,v in zip(weights,lam))
                lower = qv*(-math.expm1(-tv*rv/2))
                ordered('Jensen lower '+key+'/'+str(tv),lower,dec)
                ordered('heat upper '+key+'/'+str(tv),dec,min(G,tv*E))
            for mv in [0.0,0.1*lv,0.9*lv,lv,2*lv]:
                tail = sum(w for w,v in zip(weights,lam) if v>mv)
                ordered('finite tail '+key+'/'+str(mv),max(lv-mv,0.0)**2/den,tail)
            for rrval in [0.1,0.25,0.75]:
                lower_endpoint = rrval*lv
                upper_endpoint = rv/(1-rrval)
                mass = sum(w for w,v in zip(weights,lam) if lower_endpoint<=v<=upper_endpoint)
                ordered('moving band '+key+'/'+str(rrval),(1-rrval)**2*qv/4,mass)
            bandenergy = sum(w*v for w,v in zip(weights,lam) if lv/4<=v<=rv)
            ordered('BP20 energy '+key,lv/4,bandenergy)

# Exact finite-dimensional compression check tests the operator sign and domains.
U = s.Matrix([[0,1,0],[0,0,1],[1,0,0]])
Vfull = s.diag(1,s.I,-1)
Proj = s.diag(1,1,0)
Inc = s.Matrix([[1,0],[0,1],[0,0]])
IncD = s.Matrix([[0],[0],[1]])
compress = lambda mat: Inc.T*mat*Inc
Kmap = lambda mat: IncD.T*mat*Inc
def exact_matrix(label, mat):
    for i in range(mat.rows):
        for j in range(mat.cols):
            exact(f'{label} [{i},{j}]',mat[i,j])
exact_matrix('compression multiplication sign',compress(U*Vfull)-compress(U)*compress(Vfull)-Kmap(U.adjoint()).adjoint()*Kmap(Vfull))
exact_matrix('inverse positive defect',s.eye(2)-compress(U).adjoint()*compress(U)-Kmap(U).adjoint()*Kmap(U))

result = {'status':'passed','check_count':len(checks),'checks':checks,
          'scope':'Symbolic coefficients and limits, finite moment measures, exact compression matrix; analytic proofs are in BR15-BR27.',
          'original_state_replaced':False}
(root/'BOUNDED_PHASE_REVIEW_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:result[k] for k in ['status','check_count','original_state_replaced']}))
