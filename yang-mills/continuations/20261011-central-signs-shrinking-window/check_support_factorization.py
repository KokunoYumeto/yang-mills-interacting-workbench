from pathlib import Path
from fractions import Fraction as Q
import hashlib,json,re
ROOT=Path(__file__).resolve().parent
count=0
for n in range(4,11):
 for e in range(n):
  for s in range(1,1<<n):
   if s.bit_count()<4:continue
   lhs=Q(2)**(n-(s|(1<<e)).bit_count())
   rhs=Q(2)**(n-7)*(5*bool(s&(1<<e))+(s&~(1<<e)).bit_count())
   assert lhs<=rhs;count+=1
norm_count=count
P=sum(1<<i for i in [0,1,2,3]);R=sum(1<<i for i in [1,4,5,6]);U=P|R
def subs(s):
 a=s
 while True:
  yield a
  if a==0:break
  a=(a-1)&s
def mobius(f,s):return sum((-1)**((s^a).bit_count())*f[a] for a in subs(s))
for values in [(Q(2,3),Q(-3,5),Q(11,7)),(Q(0),Q(13,2),Q(-5,9))]:
 vp,vq,vu=values
 f={a:(vp if P&a==P else 0)+(vq if R&a==R else 0)+(vu-vp-vq if U&a==U else 0) for a in range(128)}
 for s in range(128):
  expected=vp if s==P else vq if s==R else vu-vp-vq if s==U else 0
  assert mobius(f,s)==expected;count+=1
for n in range(2,9):
 for split in range(1,n):
  left=(1<<split)-1;right=((1<<n)-1)^left
  # Arbitrary additive set functions, not a substitute physical vacuum.
  f={a:Q((a&left)**3,7)+Q((a&right)**2,11) for a in range(1<<n)}
  assert mobius(f,(1<<n)-1)==0;count+=1
note=(ROOT/'SUPPORT_AND_SCALAR_FACTORIZATION.md').read_text(encoding='utf-8')
assert note.count(r'\(')==note.count(r'\)') and note.count(r'\[')==note.count(r'\]')
assert re.findall(r'\\tag\{([^}]+)\}',note)==['UF'+str(i) for i in range(1,18)]
out={'checks':count,'gauge_support_norm_inequalities':norm_count,'two_face_and_factorization_checks':count-norm_count,'all_passed':True,'proof_sha256':hashlib.sha256(note.encode()).hexdigest(),'scope':'Exact finite checks of the counting, two-face and additive Boolean identities. Product ground-state and gauge assertions are proved in UF1–UF8.'}
(ROOT/'SUPPORT_FACTORIZATION_CHECKS.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(out))
