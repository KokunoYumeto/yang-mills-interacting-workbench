from pathlib import Path
import datetime,hashlib,json,math,re
import numpy as np
import sympy as s
R=Path(__file__).resolve().parent
rows=[]
def check(name,ok,detail=None):
 rows.append({'name':name,'passed':bool(ok),'detail':detail});assert ok,name
E,P,Q,t=s.symbols('E P Q t',positive=True)
check('monotone variance certificate',s.simplify(s.diff(E**2/(P+Q*E),E)-E*(2*P+Q*E)/(P+Q*E)**2)==0)
RR=2*(P/E+Q)
check('explicit window certificate',s.simplify(4*E/RR-4*(P+Q*E)/RR**2-E**2/(P+Q*E))==0)
rng=np.random.default_rng(150011)
for k in range(200):
 lam=rng.uniform(.001,40,30);mass=rng.uniform(0,1,30)
 e=float(mass@lam);e2=float(mass@(lam*lam));g=float(mass.sum());r=2*e2/e
 check('raw variance moments '+str(k),g>=e*e/e2-1e-12)
 check('restricted raw window '+str(k),float(mass[lam<=r].sum())>=e*e/e2-1e-12)
 for tt in (.001,.05,.5,5):
  dec=float(mass@(-np.expm1(-tt*lam)));lower=e*e/e2*(-math.expm1(-tt*e2/e))
  check('all-time Jensen '+str((k,tt)),dec>=lower-1e-11)
for dp in np.linspace(0,4,41):
 for dq in np.linspace(0,4,41):
  check('full Wilson product defect '+str((dp,dq)),abs(abs((2-dp)*(2-dq)-4)-(2*(dp+dq)-dp*dq))<1e-12)
for k in range(100):
 # Original four-face diagonal interference, with arbitrary signed coefficients.
 f=rng.uniform(-2,2,4);d=rng.uniform(0,4,4);F=max(abs(f));W=2-d
 err=abs((f@W)**2-4*f.sum()**2)
 check('retained diagonal interference '+str(k),err<=16*F*F*d.sum()+1e-12)
for e,e2 in ((2.,4.),(.7,2.3),(5.,70.)):
 m=e*e/e2;lam=e2/e
 check('moment extremizer '+str((e,e2)),abs(m*lam-e)<1e-12 and abs(m*lam*lam-e2)<1e-11)
for fname,prefix,count in [('HESSIAN_RECEIVING_REVIEW.md','HVR',34)]:
 text=(R/fname).read_text(encoding='utf-8');tags=re.findall(r'\\tag\{'+prefix+r'(\d+)\}',text)
 check('complete unique proof locators',list(map(int,tags))==list(range(1,count+1)))
 check('balanced TeX',text.count(r'\[')==text.count(r'\]') and text.count(r'\(')==text.count(r'\)'))
out={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'proof_sha256':hashlib.sha256((R/'HESSIAN_RECEIVING_REVIEW.md').read_bytes()).hexdigest(),'check_count':len(rows),'all_passed':True,'scope':'Independent algebraic and finite-sample checks of proved raw-moment inequalities, exact interference bounds and extremizers; no substitute physical vacuum.','checks':rows}
(R/'HESSIAN_RECEIVING_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='checks'}))
