"""Independent one-plaquette character/eigenvector/logarithm recurrence.

The index n is twice the original SU(2) spin.  At coefficient order N only
n<=N can occur, because multiplication by the fundamental character changes
n by one.  This is a statement about a Taylor coefficient, not an operator
spin truncation.
"""
from fractions import Fraction as F
from collections import defaultdict

def add(*ps):
 r=defaultdict(F)
 for p in ps:
  for n,c in p.items():r[n]+=c
 return {n:c for n,c in r.items() if c}
def scale(p,c):return {n:a*c for n,a in p.items() if a*c}
def mul(p,q):
 r=defaultdict(F)
 for m,a in p.items():
  for n,b in q.items():
   for j in range(abs(m-n),m+n+1,2):r[j]+=a*b
 return {n:c for n,c in r.items() if c}
def conv(a,b,N):
 out=[{} for _ in range(N+1)]
 for i,p in enumerate(a):
  for j,q in enumerate(b):
   if i+j<=N:out[i+j]=add(out[i+j],mul(p,q))
 return out

def calculate(N=8):
 u=[{} for _ in range(N+1)];u[0]={0:F(1)};e=[F(0)]*(N+1)
 for n in range(1,N+1):
  e[n]=-u[n-1].get(1,F(0));rhs=mul({1:F(1)},u[n-1])
  for j in range(1,n+1):rhs=add(rhs,scale(u[n-j],e[j]))
  u[n]={k:c/F(k*(k+2)) for k,c in rhs.items() if k and c}
  if any(k>n for k in u[n]):raise ArithmeticError('character-order-support')
 z=[dict(p) for p in u];z[0]={};power=[{0:F(1)}]+[{} for _ in range(N)];log=[{} for _ in range(N+1)]
 for j in range(1,N+1):
  power=conv(power,z,N)
  for n in range(N+1):log[n]=add(log[n],scale(power[n],F((-1)**(j+1),j)))
 v=[{k:c for k,c in p.items() if k} for p in log]
 target={1:F(49,27216),3:-F(23,97200),5:F(11,680400)}
 if v[5]!=target:raise ArithmeticError('fifth-character-recurrence')
 dlmf={2:-F(1,3),4:F(5,216),6:-F(289,77760),8:F(21391,27993600)}
 for n,c in dlmf.items():
  if e[n]!=c:raise ArithmeticError('Mathieu-source-map:'+str(n))
 return {'fifth_characters':{str(k):str(c) for k,c in sorted(v[5].items())},
         'energy_through_eight':[str(c) for c in e],
         'Haar_scalar_in_log_eigenvector_through_five':[str(p.get(0,F(0))) for p in log[:6]],
         'original_unit_vacuum_log_scalar_degree_two':'-1/9',
         'Mathieu_map':{'q':'-4*xi','energy':'b_2(q)/4-1','physical_full_energy':'kappa*(2*xi+energy)'}}
if __name__=='__main__':
 import json
 print(json.dumps(calculate(),indent=2,sort_keys=True))
