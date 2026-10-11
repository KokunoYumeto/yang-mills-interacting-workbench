from fractions import Fraction as F
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parent
a={1:F(128,3),2:F(3132,13),3:F(292337810,125307),4:F(169232115504453213210913,2253180919843854000),5:F(2399196)}
h2=a[2]+a[1]**2
h4=a[4]+2*a[1]*a[3]+a[2]**2+3*a[1]**2*a[2]+a[1]**4
def values(x):
    ell=sum(a[i]*x**i for i in a)
    e=a[2]*x**2+a[4]*x**4;o=a[1]*x+a[3]*x**3+a[5]*x**5
    h=(e-e*e+o*o)/((1-e)**2-o*o)
    tail=h-h2*x*x-h4*x**4
    assert ell<1 and tail>=0
    return {'x':str(x),'ell':str(ell),'h_even':str(h),'E6':str(tail),'E6_decimal':float(tail)}
rows=[values(x) for x in [F(1,100),F(1,64),F(19,1000)]]
assert F(rows[0]['E6'])<F(17,1000)
assert F(rows[1]['E6'])<F(9,20)
out={'a':{str(i):str(v) for i,v in a.items()},'h2':str(h2),'h4':str(h4),'rational_checks':rows,'strict_bounds':{'E6(1/100)':'17/1000','E6(1/64)':'9/20'}}
(ROOT/'SIXTH_TAIL_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
