"""Independent exact algebra verification of ZU and WV receiving identities."""
import json
from pathlib import Path
import sympy as s

out=Path(__file__).resolve().parent
alpha,F,A,d,z2,Lambda,Q,R,B,U,S,T,Z=s.symbols(
    'alpha F A d z2 Lambda Q R B U S T Z', nonzero=True)
c=9*alpha/64
J2=36*A*A-36*A*d+9*z2
P=(1+c)*z2-(Lambda+4*c*A)*d+4*c*A*A
energy=z2+B+alpha*F*Z-Lambda*d-3*alpha*F*A+s.Rational(3,2)*alpha*F*d
assert s.expand(energy.subs(Z,Q+R+J2/(64*F)-s.Rational(3,2)*d)
                -(P+B+alpha*F*(Q+R)-3*alpha*F*A))==0

Qstar=Z-(U-3*S)**2/(4*T)
retained=(B+alpha*F*Qstar+3*alpha*(16*F*d-S)/32
          +9*alpha*S*S/(64*U)
          +alpha*(U-3*S)**2*(16*F*U-T)/(64*U*T))
assert s.factor((P+retained-3*alpha*F*A-energy).subs(U,J2))==0

t0=1/(32*F)
tstar=(U-3*S)/(2*T)
Qt0=Z-t0*(U-3*S)+t0*t0*T
assert s.factor(Qt0-Qstar-T*(t0-tstar)**2)==0

old=Lambda*d+4*alpha*F*F
new=((Lambda+4*c*A)*d-4*c*A*A+3*alpha*F*A)/(1+c)
diff=(c*Lambda*d-4*c*A*d+4*c*A*A
      +4*alpha*F*F*(1+c)-3*alpha*F*A)/(1+c)
assert s.factor(old-new-diff)==0

a,k,J,l,da=s.symbols('a k J l da',positive=True)
path={alpha:k*k*a*a,A:3*J/a**3,Lambda:F*l/a**2,d:da/a**2}
limit=s.limit((a**4*diff).subs(path),a,0)
assert limit==81*J*J*k*k/16

n=s.symbols('n',positive=True)
meanP=(1+c)*d*d-(Lambda+4*c*A)*d+4*c*A*A
meanbound=alpha*(6*A-3*d)**2/64-(Lambda-d)*(16*F*d-4*z2/n)/(16*F)
assert s.factor(meanbound-(meanP+(Lambda-d)*z2/(4*F*n)))==0

result={
 'ZU19_complete_defect_identity':True,
 'ZU35_exact_difference':True,
 'ZU35_asymptotic_constant':str(limit),
 'WV7_exact_optimized_defect_identity':True,
 'WV6_square_translation':True,
 'WV11_incidence_refined_mean_inequality_algebra':True,
 'review':'Exact weighted-square and optimized-defect identities; complete receiving proofs are ZU1-ZU44 in SOURCE_ZERO_COVARIANCE_UPPER.md.'
}
(out/'WEIGHTED_COVARIANCE_CHECKS.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
