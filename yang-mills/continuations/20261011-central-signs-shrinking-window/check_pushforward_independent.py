"""Exact algebra checks; the analytic coarea and endpoint proofs are in PF1-PF49."""
import json
from pathlib import Path
import sympy as s

out=Path(__file__).resolve().parent
y,F,alpha,A1,t,e,M,Mp,H,Z,R=s.symbols('y F alpha A1 t e M Mp H Z R')
At=1+s.Rational(3,2)*alpha*F*t-8*alpha*F**2*t*t
Bt=e+3*alpha*F*A1*t
D=alpha*F*Z+R+alpha*F*t*t*(16*F*Mp-H)/2
ground=e*M-(Mp+R+alpha*F*Z-alpha*F*(t*t*H+t*(6*A1*M-3*Mp))/2)
assert s.expand(ground+(At*Mp-Bt*M+D))==0

rr,h,J,ta,kappa,b,u,o,delta,Lambda=s.symbols('rr h J ta kappa b u o delta Lambda')
rp=s.symbols('rp')
# t_current = rr*s_current; s_current'=(J+2*rr*h)*density.
tprime_over_p=rp*h+rr*(J+2*rr*h)
z=rr*rr*h+ta
conditional=kappa*tprime_over_p-(kappa*z+b*(u-Lambda)+o+delta)
riccati=kappa*(h*(rp+rr*rr)+J*rr-ta)-b*(u-Lambda)-o-delta
assert s.expand(conditional-riccati)==0

B,eta,zz=s.symbols('B eta zz', real=True)
square=y*zz+2*B*eta+B*B*h/y
star=-y*eta/h
assert s.factor(square-(y*(zz-eta*eta/h)+h*(B-star)**2/y))==0

V,T,r=s.symbols('V T r',positive=True)
first=s.integrate(2*r*s.exp(-r*r/(4*V)),(r,0,2*V*T))
second=s.integrate(2*r*s.exp(-T*r+V*T*T),(r,2*V*T,s.oo))
tail=s.simplify(first+second)
assert s.simplify(tail-(4*V+2*s.exp(-V*T*T)/(T*T)))==0

central_checks=0
for z1 in range(3):
 for z2 in range(3):
  for z3 in range(3):
   zz=(z1,z2,z3)
   for dd in range(3):
    for ee in range(dd+1,3):
     zpd=list(zz);zpd[dd]+=1
     zpe=list(zz);zpe[ee]+=1
     coeff=lambda z,d:sum(z[:d])
     word=coeff(zz,dd)+coeff(zpd,ee)-coeff(zpe,dd)-coeff(zz,ee)
     assert word==1
     central_checks+=1

result={
 'PF40_exponential_ground_identity':True,
 'PF29_conditional_scalar_ground_equation':True,
 'PF20_PF21_all_function_square_completion':True,
 'PF43_improved_tail_integral':str(tail),
 'PF1_original_orientations_checked':central_checks,
 'scope':'Exact algebra and finite orientation checks supplement the analytic proof; the actual density is not replaced or numerically sampled.'
}
(out/'PUSHFORWARD_INDEPENDENT_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
