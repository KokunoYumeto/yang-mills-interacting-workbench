from pathlib import Path
import datetime, json, re
import sympy as S

root=Path(__file__).resolve().parent
x=S.symbols('x',real=True)
kap,lam=S.symbols('kappa lambda',positive=True)
h,p,r,J,z,U=[S.Function(a)(x) for a in ['h','p','r','J','z','U']]
chi=S.Function('chi')(x)
# Actual-current algebra, retaining the physical kappa and potential U.
subs={S.diff(p,x):(J+2*r*h-S.diff(h,x))*p/h,
      S.diff(chi,x):r*chi}
m=p/chi**2
assert S.simplify(S.diff(h*m,x).subs(subs)-J*m)==0
assert S.simplify(h*m*S.diff(chi,x).subs(subs)-r*h*p/chi)==0
rp=(z+(U-lam)/kap-r*J-2*r*r*h)/h
lhs=(-kap*S.diff(h*m*r*chi,x)+U*m*chi+kap*(z-r*r*h)*m*chi)
assert S.simplify(lhs.subs(subs).subs(S.diff(r,x),rp)-lam*m*chi)==0
# Ground transform differential expression and residual conditioning.
f=S.Function('f')(x)
expr=-kap*(h*S.diff(f*chi,x,2)+J*S.diff(f*chi,x))
expr+=kap*(h*(S.diff(r,x)+r*r)+J*r)*f*chi
expr=expr.subs(S.diff(chi,x,2),(S.diff(r,x)+r*r)*chi).subs(subs)
assert S.simplify(expr+kap*chi*(h*S.diff(f,x,2)+(J+2*r*h)*S.diff(f,x)))==0

# Exact finite correlated fibers check the orthogonal second-moment split.
# These are algebra diagnostics, never substitute vacuum samples.
weights=[S.Rational(1,6),S.Rational(1,3),S.Rational(1,2)]
gam=[S.Rational(1),S.Rational(3),S.Rational(5)]
score=[S.Rational(-2),S.Rational(1),S.Rational(4)]
zg=[score[i]**2/gam[i]+1 for i in range(3)]
mean=lambda v:sum(q*v0 for q,v0 in zip(weights,v))
hh,aa,zz=mean(gam),mean(score),mean(zg)
cov=S.Matrix([[mean([(g-hh)**2 for g in gam]),mean([(gam[i]-hh)*(score[i]-aa) for i in range(3)])],
              [mean([(gam[i]-hh)*(score[i]-aa) for i in range(3)]),mean([(a-aa)**2 for a in score])]])
assert cov.det()>=0 and all(cov[i,i]>=0 for i in range(2))
gmax=max(gam)
assert cov[0,0]<=gmax*hh-hh*hh and cov[1,1]<=gmax*zz-aa*aa
derivs=[(S.Rational(2)+S.I,S.Rational(-1)),(S.Rational(-3),S.Rational(4)-2*S.I)]
res=[]; cond=[]; total=[]
jj=S.Rational(7)
for d1,d2 in derivs:
 c=hh*d2+(jj+2*aa)*d1
 rv=[(gam[i]-hh)*d2+2*(score[i]-aa)*d1 for i in range(3)]
 assert S.simplify(mean(rv))==0
 res.append(rv);cond.append(c);total.append([c+a for a in rv])
for i in range(2):
 for j in range(2):
  rhs=S.conjugate(cond[i])*cond[j]+mean([S.conjugate(res[i][k])*res[j][k] for k in range(3)])
  lhs=mean([S.conjugate(total[i][k])*total[j][k] for k in range(3)])
  assert S.simplify(lhs-rhs)==0
  vi=S.Matrix([derivs[i][1],2*derivs[i][0]])
  vj=S.Matrix([derivs[j][1],2*derivs[j][0]])
  assert S.simplify((S.conjugate(vi).T*cov*vj)[0]-mean([S.conjugate(res[i][k])*res[j][k] for k in range(3)]))==0

doc=(root/'PUSHFORWARD_OPERATOR_RECEIVING.md').read_text(encoding='utf-8')
assert re.findall(r'\\tag\{(OP\d+)\}',doc)==['OP'+str(i) for i in range(1,20)]
assert doc.count(r'\[')==doc.count(r'\]') and doc.count(r'\(')==doc.count(r'\)')
assert not any(ord(c)<32 and c not in '\n\t' for c in doc)
out=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),actual_current_algebra=True,
 ground_transform_factor_and_sign=True,correlated_complex_second_moment_entries=4,
 conditional_residual_matrix_entries=4,conditional_covariance_geometric_bounds=True,
 all_OP1_to_OP19_present=True,scope='Symbolic identities and exact correlated-fiber diagnostics; no numerical ground-state or continuum claim.')
(root/'PUSHFORWARD_OPERATOR_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out))
