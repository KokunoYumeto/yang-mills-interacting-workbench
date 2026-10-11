from pathlib import Path
import json
import sympy as s
root=Path(__file__).resolve().parent
checks=[]
def check(name,expr):
    value=s.simplify(expr)
    assert value==0,(name,value)
    checks.append(name)

r,t=s.symbols('r t',real=True)
v11,v12,v22=s.symbols('v11 v12 v22',real=True)
Sigma=s.Matrix([[v11,v12],[v12,v22]])
dr=s.Matrix([-r*r,2*s.I*r]); dt=s.Matrix([-t*t,2*s.I*t])
mixed=(s.conjugate(dr).T*Sigma*dt)[0]
check('mixed phase residual sign',mixed-(r*r*t*t*v11+4*r*t*v22+2*s.I*r*t*(t-r)*v12))
check('diagonal phase residual cancellation',mixed.subs(t,r)-(r**4*v11+4*r*r*v22))
J,eta,h,Ag,gg=s.symbols('J eta h Ag gg',real=True)
scalar=r*r*(J+2*eta)**2+r**4*h*h
residual=r**4*(gg-h*h)+4*r*r*(Ag-eta*eta)
check('full phase second moment',scalar+residual-(r*r*(J*J+4*J*eta+4*Ag)+r**4*gg))

y=s.symbols('y',real=True)
aa=s.Function('a')(y); chi=s.Function('chi')(y); phi=s.Function('phi')(y)
kap,V,E,m=s.symbols('kap V E m',positive=True)
full=-kap*s.diff(aa*s.diff(chi*phi,y),y)+V*m*chi*phi
ground=phi*(-kap*s.diff(aa*s.diff(chi,y),y)+V*m*chi)
check('ground product differential action',full-ground+kap*(aa*chi*s.diff(phi,y,2)+(s.diff(aa,y)*chi+2*aa*s.diff(chi,y))*s.diff(phi,y)))
ss=s.Function('s')(y); tt=s.Function('t')(y)
flux=aa*s.diff(chi*phi,y)
check('smooth-test flux',flux.subs(s.diff(chi,y),tt/(aa*chi)).subs(aa,ss/chi**2)-(tt*phi+ss*s.diff(phi,y))/chi)

beta,kappa,w=s.symbols('beta kappa w',positive=True)
check('density exponent',-(-2*kappa*w)/kappa-2*w)
check('noise diffusion factor',s.Rational(1,2)*(s.sqrt(2*kappa)*s.sqrt(h))**2-kappa*h)
check('conditional original drift',2*kappa*eta+kappa*J-kappa*(J+2*eta))

# Finite conditional covariance examples retain their full off-diagonal values.
for gamma_values,A_values in [([1,2,4],[3,-1,2]),([0,1,2],[0,3,-2]),([1,1,1],[-2,0,2])]:
    probs=[s.Rational(1,6),s.Rational(1,3),s.Rational(1,2)]
    mh=sum(p*g for p,g in zip(probs,gamma_values)); ma=sum(p*a for p,a in zip(probs,A_values))
    cov=s.zeros(2)
    for p,g,a in zip(probs,gamma_values,A_values):
        v=s.Matrix([g-mh,a-ma]);cov+=p*v*v.T
    assert cov[0,0]>=0 and cov[1,1]>=0 and cov.det()>=0
    for rr,ts in [(1,1),(-2,3),(0,4)]:
        d1=s.Matrix([-rr**2,2*s.I*rr]);d2=s.Matrix([-ts**2,2*s.I*ts])
        exact_sum=sum(p*s.conjugate((g-mh)*d1[0]+(a-ma)*d1[1])*((g-mh)*d2[0]+(a-ma)*d2[1]) for p,g,a in zip(probs,gamma_values,A_values))
        check('finite conditional matrix '+str((gamma_values,rr,ts)),exact_sum-(s.conjugate(d1).T*cov*d2)[0])

result={'status':'passed','check_count':len(checks),'checks':checks,'scope':'Bounded symbolic coefficients and finite conditional covariance algebra; analytic domain proofs are OR4-OR10.'}
(root/'OPERATOR_REVIEW_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'status':'passed','check_count':len(checks)}))
