from pathlib import Path
from fractions import Fraction as F
from math import factorial as fac
from itertools import product
import json
ROOT=Path(__file__).resolve().parent
checks=[]
def ck(name,got,want):
 assert got==want,(name,got,want)
 checks.append({'name':name,'passed':True})
def hermite(n):
 out={}
 for a in range(n+1):
  for b in range(n-a+1):
   alpha=(a,b,n-a-b);choices=[list(range(x,-1,-2)) for x in alpha]
   for h in product(*choices):
    for k in product(*choices):
     v=F(fac(n),fac(a)*fac(b)*fac(n-a-b))
     for x,y,z in zip(alpha,h,k):
      v*=F(fac(x),2**((x-y)//2)*fac((x-y)//2)*fac(y))
      v*=F(fac(x),2**((x-z)//2)*fac((x-z)//2)*fac(z))
     out[h+k]=out.get(h+k,F(0))+v
 return out
H={n:hermite(n) for n in range(6)}
def weights(n,m):
 result=[F(0)]*6
 for key,v in H[n].items():
  if key in H[m]:
   w=v*H[m][key]
   for x in key:w*=fac(x)
   result[sum(key)//2]+=w
 return result
def moment(n):
 if n%2:return F(0)
 k=n//2;v=F(fac(n),fac(k))
 for j in range(k):v*=F(3,2)+j
 return v
# Independent truncated expansion of the exact determinant generating function.
B={(2,0,0):F(-1),(0,2,0):F(-1),(1,1,1):F(-2),
   (2,2,0):F(1),(2,2,1):F(-2),(2,2,2):F(1)}
def mul(A,B):
 C={}
 for (a,b,c),v in A.items():
  for (d,e,f),w in B.items():
   if a+d<=5 and b+e<=5:
    key=(a+d,b+e,c+f);C[key]=C.get(key,F(0))+v*w
 return {k:v for k,v in C.items() if v}
S={(0,0,0):F(1)};power=dict(S);coef=F(1)
for k in range(1,11):
 power=mul(power,B);coef*=-(F(3,2)+k-1)/k
 for key,v in power.items():S[key]=S.get(key,F(0))+coef*v
for n in range(6):
 for m in range(6):
  W=weights(n,m)
  ck(f'Gram n={n}, m={m}',sum(W),moment(n+m))
  ck(f'Determinant n={n}, m={m}',W,[S.get((n,m,k),F(0))*fac(n)*fac(m) for k in range(6)])
  if n and m:ck(f'Energy n={n}, m={m}',sum(k*v for k,v in enumerate(W)),n*m*(n+m+1)*moment(n+m-2))
ck('q cubic weights',weights(3,3),[F(0),F(675),F(540),F(360),F(0),F(0)])
ck('raw cubic second moment',4*sum(k*k*v for k,v in enumerate(weights(3,3))),F(24300))
ck('raw compression residual',F(21600)-F(8640)**2/F(3600),F(864))
ck('variance ratio',F(864,3600),F(6,25))
# Exact source formula for N acting on q^a u^b.
def N(a,b):
 out={(a,b):F(2*a+2*b)}
 def add(key,v):
  if v:out[key]=out.get(key,F(0))+v
 add((a-2,b+1),-a*(a-1))
 add((a,b-1),-12*b-8*a*b-4*b*(b-1))
 return {k:v for k,v in out.items() if v}
ck('N q',N(1,0),{(1,0):F(2)})
ck('N uq',N(1,1),{(1,1):F(4),(1,0):F(-20)})
ck('N q^3',N(3,0),{(3,0):F(6),(1,1):F(-6)})
receipt={'all_passed':True,'check_count':len(checks),'checks':checks,
 'q3_level_weights':[str(x) for x in weights(3,3)],'raw_cubic_level_weights':['0','2700','2160','1440']}
(ROOT/'PHASE_SPECTRAL_CHECKS.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({'all_passed':True,'check_count':len(checks)}))
