"""Independent exact algebra for the third-growth held-parent map.

All physical constants remain symbols.  The written audit establishes
the domains and ODE inverse; these checks verify the algebraic identities.
"""
from pathlib import Path
import json
import sympy as S

a,h,hb,b,g0,omega,A1,A0c,A0s,K1,K2,K3,P2,d=S.symbols(
    'a h hb b g0 omega A1 A0c A0s K1 K2 K3 P2 d', positive=True)
chi=S.sqrt(h*h+a*a)
chib=S.sqrt(hb*hb+a*a)
g=g0+b*(h-hb)/a
c=b*hb-a*g0
R=g*g+b*b
y=h*g+a*b
J=S.Matrix([[0,-1],[1,0]])
rot=S.Matrix([[h,-a],[a,h]])/chi
rotb=S.Matrix([[hb,-a],[a,hb]])/chib
shear=S.Matrix([[1,-(h-hb)/a],[0,1]])
z1=S.Matrix([-a,h])/chi
z2=S.Matrix([0,chi])
z3=S.Matrix([c,y])/chi
theta_dot=-a*a*omega/(chi*chi)
D=theta_dot*J+omega*(J*z1)*z1.T
M=rot*shear*rotb.T
checks={}

def zero(name,expr):
    entries=list(expr) if isinstance(expr,S.MatrixBase) else [expr]
    residuals=[S.simplify(S.expand(x)) for x in entries]
    assert all(x==0 for x in residuals),(name,residuals)
    checks[name]=True

zero('z1_unit',z1.dot(z1)-1)
zero('held_z2_phase',a*omega*z2.diff(h)+D.T*z2)
zero('held_z1_phase',a*omega*z1.diff(h)-theta_dot*J*z1)
zero('third_matrix_ODE',a*omega*M.diff(h)-D*M)
zero('third_matrix_identity',M.subs(h,hb)-S.eye(2))
zero('third_matrix_unit_determinant',M.det()-1)
zero('third_phase_rotation_formula',rot*S.Matrix([b,g])-z3)
zero('third_phase_transport',a*omega*z3.diff(h)+D.T*z3)
zero('third_phase_norm',z3.dot(z3)-R)
zero('relative_determinant',b*h-a*g-c)
zero('third_phase_initial_datum',M.T*z3-rotb*S.Matrix([b,g0]))

base=-rot*S.Matrix([-A0s,A0c])
G=base-A1*z1-K2*P2*z2
N=b*(A1+A0c)+g*A0s+c*K2*P2
zero('complete_gradient_coupling',-(J*z3).dot(G)-N)
Ndot=(S.diff(N,h)*a*omega
      +S.diff(N,A1)*(-A0s*omega-d*K1*K1*A1)
      +S.diff(N,P2)*(-d*K2*K2*chi*chi*P2))
zero('evolving_numerator_diffusion',Ndot+d*(b*K1*K1*A1+c*K2**3*chi*chi*P2))
F2=-omega*z1[0]*(J*z1).dot(z2)/z2[1]
F3=-omega*z1[0]*(J*z1).dot(z3)/z3[1]
zero('held_control',F2+a*a*omega/(chi*chi))
zero('third_feedback',F3+a*b*omega/y)
zero('feedback_difference',F3-F2+a*h*c*omega/(chi*chi*y))
zero('controlled_first_phase_component',(F3-F2)*z3[1]-a*omega*S.diff(z3[0],h))
zero('phase_norm_derivative',a*omega*S.diff(R,h)-2*b*g*omega)

t=S.symbols('t',real=True)
Ch,Nf,Rf,Y,Lambda=[S.Function(v)(t) for v in ['chi','N','R','Y','Lambda']]
theta=S.exp(-Lambda)*Ch*S.diff(Y,t)/(K3*c)
vort=S.exp(-Lambda)*Y
damp=d*K3*K3*Rf
subs={S.diff(Lambda,t):damp,
      S.diff(Y,t,2):Nf*c*Y/(Rf*Ch)-S.diff(Ch,t)*S.diff(Y,t)/Ch}
zero('inverse_scalar_equation',
     (S.diff(theta,t)-Nf*vort/(K3*Rf)+damp*theta).subs(subs))
zero('inverse_vorticity_equation',
     (S.diff(vort,t)-K3*c*theta/Ch+damp*vort).subs(subs))

receipt={'scope':'exact algebra only; domains and analytic inverse proved in AUDIT.md',
         'passed':len(checks),'checks':checks}
Path(__file__).with_name('verification.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({'passed':len(checks),'file':str(Path(__file__).with_name('verification.json'))}))
