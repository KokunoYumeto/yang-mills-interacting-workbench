"""Audit the explicit scalar formulas present in the uploaded transcript.

Passing this arithmetic audit does not prove the inherited analytic norm bounds.
"""
from fractions import Fraction as Q
from pathlib import Path
from decimal import Decimal,localcontext
import json,re,hashlib
ROOT=Path(__file__).resolve().parents[1]
A3=Q(944984,351);B22=Q(799258,39)
def ell(x):return Q(128,3)*x+Q(3132,13)*x*x
def delta(x):return A3*x**3+B22*x**4
def discriminant(x):return (1-ell(x))**2-Q(8,3)*delta(x)
def polynomial(x):return (46457856*x**4+183150656*x**3+18324072*x*x-1168128*x+13689)/13689

def main():
 checks=[]
 def check(name,test):
  if not test:raise ArithmeticError(name)
  checks.append(name)
 check('second-source-total-spin',6+42*Q(400,117)==Q(5834,39))
 check('second-source-edge-spin',Q(3,2)+6*Q(64,117)+36*Q(176,351)==Q(137,6))
 check('linear-v2-bound',3*(Q(5834,39)/6+Q(2,3)*Q(137,6))==Q(1566,13))
 check('quadratic-v2-bound',6*Q(5834,39)*Q(137,6)==B22)
 for n in range(21):
  x=Q(n,1000);check('discriminant-expanded-'+str(n),discriminant(x)==polynomial(x))
 lo,hi=Q(17,1000),Q(171,10000)
 check('root-bracket-sign',discriminant(lo)>0>discriminant(hi))
 for _ in range(160):
  mid=(lo+hi)/2
  if discriminant(mid)>0:lo=mid
  else:hi=mid
 a0=Q(170787544707772675,10**19);a1=Q(170787544707772677,10**19)
 check('uploaded-root-digits',a0<lo<hi<a1)
 g0=Q(3825973052393385,10**15);g1=Q(3825973052393386,10**15)
 check('uploaded-coupling-digits',4*hi*g0*g0<1<4*lo*g1*g1)
 x=Q(1,64)
 check('uploaded-ell-benchmark',ell(x)==Q(28973,39936))
 check('uploaded-inverse-benchmark',1/(1-ell(x))==Q(39936,10963))
 check('uploaded-linear-response-benchmark',delta(x)/(1-ell(x))==Q(33836149,808280064))
 check('uploaded-discriminant-benchmark',discriminant(x)==Q(10028381,224280576))
 check('uploaded-Catalan-benchmark',Q(8,3)*delta(x)/(1-ell(x))**2==Q(439869937,1081686321))
 for N in range(1,35):
  from math import comb
  b=Q(comb(2*N,N),4**N);c=Q(comb(2*N+2,N+1),4**(N+1))
  check('Catalan-tail-telescope-'+str(N),Q(comb(2*N,N),(N+1)*4**N)==2*(b-c))
 raw=(ROOT/'input/Pasted markdown(6).md').read_text()
 # The input is preserved separately; the excerpt is explicitly marked incomplete.
 start=raw.index('# The full linearized residual');stop=raw.index('\\---ZIP---',start)
 excerpt=raw[start:stop].replace('\\_','_').replace('\\<','<')
 excerpt=excerpt.replace('Construct w explicitly by the binary-tree recurrence w*1=z, w_n=sum*(i=1)^(n-1) C(w*i,w*(n-i)).','Construct w explicitly by the binary-tree recurrence w_1=z, w_n=sum_(i=1)^(n-1) C(w_i,w_(n-i)).')
 excerpt=excerpt.replace('theta*\\*=4cz_*','theta_*=4 c_* z_*').replace('theta_\\*','theta_*')
 (ROOT/'recovered/linearized_excerpt_clean.md').write_text('# Recovered excerpt only\n\nThis is the portion actually present in the upload; it ends mid-proof. Escaped Markdown underscores and the damaged tree-recursion notation have been restored. The original upload remains unchanged.\n\n'+excerpt)
 inventory=[]
 for line in raw.splitlines():
  if line.startswith('-rw'):
   name=line.split()[-1].replace('\\_','_').replace('\\.','.')
   inventory.append({'historical_name':name,'current_runtime_original_bytes_available':False,'basis':'printed historical listing in supplied attachment, not an attached file'})
 (ROOT/'sources/historical_artifact_inventory.json').write_text(json.dumps(inventory,indent=2)+'\n')
 result={'scope':'Only the explicit finite scalar identities and numeric endpoint arithmetic, using the input coefficient bounds as given. It is not an independent validation of their uniform operator estimates or mass-gap conclusion.',
         'passed':True,'checks':checks,'count':len(checks),'inherited_alpha_rational_enclosure':[str(a0),str(a1)],
         'inherited_g_squared_enclosure':[str(g0),str(g1)],
         'quarter_order_residual_distinction':'R2=xi^3 v3+xi^4 B(v2,v2), whereas v4=2B(v1,v3)+B(v2,v2)',
         'source_issue':'The upload records a status phrase about sixth-order coefficients but supplies no sixth-order formula, source table or receipt.'}
 (ROOT/'results/inherited_scalar_audit.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print(json.dumps(result,indent=2))
if __name__=='__main__':main()
