"""Independent symbolic verification of third-transition spatial identities."""
from pathlib import Path
import hashlib
import json
import sympy as s

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[1]
checks=[]
def check(name, expression):
    if isinstance(expression,s.MatrixBase):
        value=expression.applyfunc(lambda x:s.simplify(s.expand(x)))
        passed=value==s.zeros(*value.shape)
    elif isinstance(expression,bool):
        value=expression; passed=value
    else:
        value=s.simplify(s.expand(expression)); passed=value==0
    checks.append({"name":name,"passed":bool(passed),"residual":str(value)})
    if not passed: raise AssertionError((name,value))

x,y=s.symbols('x y',real=True)
xx=s.Matrix([x,y])
k1,k2,p,q,r,T,Q,U,Qr,d=s.symbols('k1 k2 p q r T Q U Qr d',real=True)
k=s.Matrix([k1,k2]); rho=k.dot(k)
J=s.Matrix([[0,-1],[1,0]])
D=s.Matrix([[p,q],[r,-p]])
G=s.Matrix(s.symbols('G1 G2',real=True))
P0,phasevar=s.symbols('P0 phasevar',real=True)
# These polynomials retain the primitive constant and make every envelope
# Laplacian group nonzero before cancellation. Other checks below are tensorial.
Ppoly=P0+phasevar**2/2+phasevar**4/4
phase=k.dot(xx)
P=Ppoly.subs(phasevar,phase)
F=s.diff(Ppoly,phasevar).subs(phasevar,phase)
Fp=s.diff(Ppoly,phasevar,2).subs(phasevar,phase)
Fpp=s.diff(Ppoly,phasevar,3).subs(phasevar,phase)
g=1+x+2*y+x*y+x**3+y**4+x**2*y**2
def grad(A): return s.Matrix([s.diff(A,x),s.diff(A,y)])
def lap(A):
    if isinstance(A,s.MatrixBase): return A.applyfunc(lap)
    return s.diff(A,x,2)+s.diff(A,y,2)
gg=grad(g); Hg=s.hessian(g,(x,y))
v=Q*J*grad(P*g)
temp=T*F*g
Vlap=T*(rho*Fpp*g+2*Fp*k.dot(gg)+F*lap(g))
vlap=Q*J*(rho*k*Fpp*g+rho*Fp*gg+2*Fp*k*k.dot(gg)
              +2*F*Hg*k+F*k*lap(g)+P*grad(lap(g)))
check('complete scalar Laplacian',lap(temp)-Vlap)
check('six-group vector Laplacian',lap(v)-vlap)
vjac=Q*J*(k*k.T*Fp*g+F*(k*gg.T+gg*k.T)+P*Hg)
check('full velocity Jacobian',v.jacobian(xx)-vjac)
nonlin=Q*T*(F**2-P*Fp)*g*(J*k).dot(gg)
check('exact scalar self-interaction sign',v.dot(grad(temp))-nonlin)
check('trace-free gradient transport identity',D*J+J*D.T)
kdot=-D.T*k
gdot=-(D*xx).dot(gg)
phasedot=kdot.dot(xx)
Tdot=U-Q*(J*k).dot(G)-d*rho*T
tempdot=Tdot*F*g+T*(Fp*phasedot*g+F*gdot)
scalarraw=tempdot+(D*xx).dot(grad(temp))+v.dot(G)+v.dot(grad(temp))-d*lap(temp)
scalardisplay=U*F*g+Q*P*(J*gg).dot(G)+nonlin-d*T*(rho*(F+Fpp)*g+2*Fp*k.dot(gg)+F*lap(g))
check('full scalar residual including coupling and modal damping',scalarraw-scalardisplay)
Qdot=Qr-d*rho*Q
psidot=Qdot*P*g+Q*(F*phasedot*g+P*gdot)
vdot=J*grad(psidot)
vectorraw=vdot+v.jacobian(xx)*(D*xx)+D*v+v.jacobian(xx)*v-temp*s.Matrix([0,1])-d*lap(v)
vectordisplay=2*D*v+Qr*J*(k*F*g+P*gg)+v.jacobian(xx)*v-temp*s.Matrix([0,1])-d*(rho*v+lap(v))
check('full vector residual and both parent interaction directions',vectorraw-vectordisplay)

w,wdot,Om,Th,rhodot=s.symbols('w wdot Om Th rhodot',real=True)
OmDot=k1*Th-d*rho*Om
Qactual=w*Om/rho
Qactualdot=wdot*Om/rho+w*OmDot/rho-w*Om*rhodot/rho**2
Qrest=(wdot*Om+w*k1*Th)/rho-Qactual*rhodot/rho
check('Q derivative including phase metric and damping',Qactualdot-(Qrest-d*rho*Qactual))
check('phase length derivative',2*k.dot(kdot)+2*k.dot(D.T*k))

K,sig1,sig2,Gamma,Pstar,N3,R,X,Y,N2,Fstate,Dt,Vstate=s.symbols('K sig1 sig2 Gamma Pstar N3 R X Y N2 Fstate Dt Vstate',positive=True)
Theta=-Pstar*X; Omega=-K*Pstar*Y/sig2
physicalThetaDot=N3*Omega/(K*R)-d*K**2*R*Theta
physicalOmegaDot=K*k1*Theta-d*K**2*R*Omega
check('linear third X coordinate and physical time factor',-physicalThetaDot/(Pstar*Gamma)-(N3*Y/(sig2*Gamma*R)-d*K**2*R*X/Gamma))
check('linear third Y coordinate and physical time factor',-sig2*physicalOmegaDot/(K*Pstar*Gamma)-(sig2*k1*X/Gamma-d*K**2*R*Y/Gamma))
K2,NN=s.symbols('K2 NN',positive=True)
theta2=-sig2**2*Fstate/K2
theta2dot=sig1**2*NN*(sig2*Vstate)/(K2*Dt)-d*K2**2*Dt*theta2
Fdot=-K2*theta2dot/(sig2**2*Gamma)
check('second-temperature full q epsilon scaling',Fdot-(-(sig1/sig2)*(sig1/Gamma)*NN*Vstate/Dt-d*K2**2*Dt*Fstate/Gamma))
a,h,hdot,udot,sangle,Phi=s.symbols('a h hdot udot sangle Phi',positive=True)
alphaDot=-sangle*udot-a*hdot/(h**2+a**2)
check('angle inverse differential and physical feedback',alphaDot.subs({udot:(-Phi-a*a*Om/(h*h+a*a))/sangle,hdot:a*Om})-Phi)
check('control bound first coefficient',10*18*s.Rational(3,2)-270)
check('control bound revived-parent coefficient',4*s.Rational(3,2)-6)
check('Q3 exact frequency coefficient',3/s.Rational(63,64)-s.Rational(64,21))
check('phase lower bound rational margin',1-s.Rational(1,64)-s.Rational(63,64))
check('collar u bound',bool(s.Rational(1,1024)+s.Rational(1,100)<s.Rational(1,50)))
check('collar g bound',bool(s.Rational(3,4)-s.Rational(1,100)>s.Rational(7,10)))
check('collar strict feedback denominator',bool(s.Rational(7,10)*s.Rational(15,16)-4*s.Rational(1,512)**2/50>s.Rational(3,5)))
check('Picard displacement fits cube',bool(s.Rational(1,400)<s.Rational(1,100)))

body=ROOT/'third_transition_spatial/third_transition_spatial_body.tex'
receipt={"scope":"Polynomial replay exercises all residual terms, including primitive constant; general proofs and remaining analytic checks are in FULL_BODY_AUDIT.md.",
         "check_count":len(checks),"all_passed":all(c['passed'] for c in checks),
         "body_sha256":hashlib.sha256(body.read_bytes()).hexdigest(),"checks":checks}
(HERE/'full_body_replay_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({"check_count":len(checks),"all_passed":receipt['all_passed']}))
