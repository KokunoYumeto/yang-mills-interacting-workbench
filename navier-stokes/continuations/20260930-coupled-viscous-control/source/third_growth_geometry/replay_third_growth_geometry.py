"""Exact replay of the complete saved third-growth geometry section.

The original independent twenty-check audit is executed unchanged.  Additional
checks cover the newly written operator, inverse-coordinate and affine-force
identities. Analytic convergence, domains and signs are proved in the TeX body.
"""
from pathlib import Path
import hashlib
import json
import runpy
import sympy as S

HERE = Path(__file__).resolve().parent
old = runpy.run_path(str(HERE / 'audit' / 'verify_third_map.py'))
checks = dict(old['checks'])
globals().update({k: old[k] for k in
                 ['a','h','hb','b','g0','omega','A1','A0c','A0s','K1','K2',
                  'K3','P2','d','chi','chib','g','c','R','J','rot','rotb',
                  'z1','z2','z3','theta_dot','D','M','G','N','Ndot']})

def zero(name, expression):
    print('checking '+name,flush=True)
    values = list(expression) if isinstance(expression, S.MatrixBase) else [expression]
    residuals = [S.simplify(S.cancel(S.together(v))) for v in values]
    assert all(v == 0 for v in residuals), (name, residuals)
    checks[name] = True

Mi = rotb * S.Matrix([[1,(h-hb)/a],[0,1]]) * rot.T
zero('material_inverse_left', Mi*M-S.eye(2))
zero('material_inverse_right', M*Mi-S.eye(2))
zero('first_third_oriented_determinant', S.det(S.Matrix.hstack(z1,z3))+b)
zero('second_third_oriented_determinant', S.det(S.Matrix.hstack(z2,z3))+c)
zero('actual_scale_full_gradient_norm',
     G.dot(G)-(A1+A0c+K2*P2*h)**2-(A0s-a*K2*P2)**2)

Adot = -A0s*omega-d*K1**2*A1
Pdot = -d*K2**2*chi**2*P2
odot = a*A1/chi-d*K1**2*omega
def Dt(expr):
    return (S.diff(expr,h)*a*omega+S.diff(expr,A1)*Adot+
            S.diff(expr,P2)*Pdot+S.diff(expr,omega)*odot)

ac = N/(K3*R)
bc = K3*c/chi
E = b*K1**2*A1+c*K2**3*chi**2*P2
zero('temperature_coefficient_log_rate', Dt(ac)/ac+d*E/N+2*b*g*omega/R)
zero('buoyancy_coefficient_log_rate', Dt(bc)/bc+a*h*omega/chi**2)
zero('instantaneous_eigenline_log_rate',
     (Dt(bc)/bc-Dt(ac)/ac)/2-
     (b*g*omega/R-a*h*omega/(2*chi**2)+d*E/(2*N)))

T,O,kap,eps = S.symbols('T O kap eps', nonzero=True)
Td = ac*O-kap*K3**2*R*T
Od = bc*T-eps*K3**2*R*O
qd = Od/T-O*Td/T**2
zero('unequal_diffusion_quotient',
     qd-(bc-ac*(O/T)**2+(kap-eps)*K3**2*R*O/T))
zero('equal_diffusion_quotient', qd.subs({kap:d,eps:d})-(bc-ac*(O/T)**2))
sig,ss,P,v = S.symbols('sigma2 sin_s3 P v', positive=True)
Gamma = sig*ss
# The oriented constant c=chib*sin(s3) is imposed only for this rescaling.
rho_v = (sig*qd/(K3*Gamma)).subs({kap:d,eps:d,T:-P,O:-K3*P*v/sig})
zero('source_time_normalized_quotient',
     (rho_v-(chib/chi-N*v**2/(sig**2*ss*R))).subs(g0,(b*hb-chib*ss)/a))
gain = ac*K3*v/sig-d*K3**2*R
zero('normalized_log_gain', gain/Gamma-(N*v/(sig**2*ss*R)-d*K3**2*R/Gamma))
gamma,us,Z = S.symbols('gamma ustar Z', positive=True)
ud = S.symbols('ustar_dot', real=True)
# Verify independently in generic positive coefficient coordinates; no
# expression-level substitution of the actual rational coefficients is needed.
A,B=S.symbols('coupling_a coupling_b', positive=True)
zero('instantaneous_eigenline_quotient',
     ((B-A*(us*Z)**2)/us-Z*ud/us).subs({B:gamma*us,A:gamma/us})
     -(gamma*(1-Z**2)-Z*ud/us))

t=S.symbols('t',real=True)
Ch,Om,lam,NN,RR=[S.Function(n)(t) for n in ['chi','omega3','lambda3','N3','R3']]
inner=Ch*(S.diff(Om,t)+lam*Om)
op=S.diff(inner,t)+lam*inner-c*NN*Om/RR
expanded=(Ch*S.diff(Om,t,2)+(S.diff(Ch,t)+2*Ch*lam)*S.diff(Om,t)+
          (Ch*S.diff(lam,t)+S.diff(Ch,t)*lam+Ch*lam**2-c*NN/RR)*Om)
zero('full_physical_damped_scalar_operator',op-expanded)
zero('varying_diagonal_damping_rate',Dt(d*K3**2*R)-2*d*K3**2*b*g*omega)

f1,f2,g1,g2,A,B=S.symbols('f1 f2 g1 g2 A B')
H=S.Matrix([[f1,f2],[g1,g2]])
Hdot=S.Matrix([[A*g1,A*g2],[B*f1,B*f2]])
wr=f1*g2-f2*g1
zero('fundamental_wronskian_rate',
     sum(S.diff(wr,x)*dx for x,dx in zip(list(H),list(Hdot))))
adj=S.Matrix([[g2,-f2],[-g1,f1]])
zero('fundamental_inverse_left',adj*H-wr*S.eye(2))
zero('fundamental_inverse_right',H*adj-wr*S.eye(2))

B1=-A1*z1
B2=-K2*P2*z2
zero('full_affine_gradient_transport',
     Dt(G)+D.T*G+d*K1**2*B1+d*K2**2*chi**2*B2)
zero('affine_velocity_trace',S.trace(D))
C=D[1,0]-D[0,1]
zero('affine_curl_original_parent',C-(2*theta_dot+omega))
base_horizontal=(A0s*h+A0c*a)/chi
zero('affine_vorticity_force',
     Dt(C)-G[0]-(2*Dt(theta_dot)-base_horizontal-d*K1**2*omega))
momentum=Dt(D)+D*D-S.Matrix([0,1])*G.T
sym=(momentum+momentum.T)/2
zero('full_vector_pressure_residual',
     momentum-sym-(Dt(C)-G[0])*J/2)

body=HERE/'third_growth_geometry_body.tex'
receipt={
    'scope':'Exact identities in the complete third-growth geometry body. '
            'Analytic claims are proved in the body and reviewed in COMPLETION_AUDIT.md.',
    'passed':len(checks),'checks':checks,
    'source_sha256':hashlib.sha256(body.read_bytes()).hexdigest(),
    'independent_original_checks':len(old['checks']),
    'additional_checks':len(checks)-len(old['checks'])}
dest=HERE/'replay_receipt.json'
dest.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'passed':len(checks),'file':str(dest)}))
