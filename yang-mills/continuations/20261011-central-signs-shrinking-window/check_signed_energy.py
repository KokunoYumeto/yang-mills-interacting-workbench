from pathlib import Path
import sympy as s,json,time
start=time.perf_counter();rows=[]
def ck(name,truth):
    ok=bool(truth);rows.append(dict(name=name,passed=ok));assert ok,name
def psd2(a):return a==a.T and a[0,0]>=0 and a[1,1]>=0 and a.det()>=0
x=s.symbols('x',positive=True);Q=s.Rational
q=(x+1)*(x+Q(1,4))*(x+4)
k=x/(x+1)**2-Q(4,25)*x/(x+Q(1,4))**2-Q(64,25)*x/(x+4)**2
rem=Q(1881,16)*x*x+Q(1233,8)*x+Q(63,2)
c0=Q(908209,68800);c1=Q(146,25)**2
ck('Complete signed rational division',s.cancel(q*k-(-Q(43,25)*x*x+Q(953,100)*x-Q(63,2)+rem/q))==0)
ck('Exact positive rational remainder difference',s.expand(Q(63,2)*q-rem)==Q(63,2)*x**3+Q(765,16)*x*x+Q(45,4)*x)
ck('Exact retained quadratic square',s.expand(c0-(-Q(43,25)*x*x+Q(953,100)*x)-Q(43,25)*(x-Q(953,344))**2)==0)
ck('Full three-term square bound coefficient',2+Q(4,25)*8+Q(64,25)==Q(146,25))
J=s.eye(4)[:,:3];F=s.Matrix([[0,0],[1,0],[0,1]]);Z=J*F;I=s.eye(4)
for n in range(1,13):
    r=s.Matrix([[1,Q(n,5),Q(1,3)],[Q(1,4),2,Q(n+1,7)],[Q(n,9),Q(1,5),3]])
    L=s.zeros(4);L[1:,1:]=r.T*r;z=Q(n+1,7)
    A=(L+z*I)*(L+z*I/4)*(L+4*z*I)
    B=J.T*A*J;t=B.inv()*F;u=J*t;Y=A*u;W=Y-Z;h=A.inv()*Z-u
    D=Z.T*A.inv()*Z-F.T*B.inv()*F
    K=z*L*(L+z*I).inv()**2-Q(16,25)*(z/4)*L*(L+z*I/4).inv()**2-Q(16,25)*(4*z)*L*(L+4*z*I).inv()**2
    C=Z.T*K*Z;T=Y.T*K*Y;M1=Z.T*L*Z
    ck(f'{n}: exact full inverse correction',h==-A.inv()*W)
    ck(f'{n}: actual form orthogonality',u.T*A*h==s.zeros(2))
    ck(f'{n}: two exact defect formulas',D==h.T*A*h and D==W.T*A.inv()*W)
    ck(f'{n}: positive full inverse-energy defect',psd2(D))
    ck(f'{n}: retained source energy floor',psd2(z**-3*(Z.T*Z)-F.T*B.inv()*F-D))
    ck(f'{n}: complete signed cross identity',C==T+Z.T*K*A*h+h.T*A*K*Z-h.T*A*K*A*h)
    eta=z**-3
    ck(f'{n}: full matrix signed lower bound',psd2(C-T+eta*c1*z*z*M1+(eta**-1+c0*z**3)*D))
out=dict(checks=len(rows),all_passed=all(r['passed'] for r in rows),seconds=time.perf_counter()-start,scope='Exact rational multiplier identities and twelve noncommuting positive matrix compressions with a retained vacuum. These are algebra diagnostics, not Wilson-state samples.',details=rows)
(Path(__file__).parent/'SIGNED_ENERGY_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:v for k,v in out.items() if k!='details'}))
