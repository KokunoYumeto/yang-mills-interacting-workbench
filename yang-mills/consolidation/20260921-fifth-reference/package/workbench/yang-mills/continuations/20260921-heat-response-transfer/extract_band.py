"""Return the original energy-three heat poles to the raw-metric first band."""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
import json
from exact_rational import PF
ROOT=Path(__file__).resolve().parent

def plus(A,B,sign=1):
 d=dict(A)
 for k,v in B.items():
  d[k]=d.get(k,F(0))+sign*v
  if not d[k]:del d[k]
 return d

def mul(A,B):
 br=defaultdict(list)
 for (i,j),v in B.items():br[i].append((j,v))
 C=defaultdict(F)
 for (i,k),a in A.items():
  for j,b in br[k]:C[i,j]+=a*b
 return {k:v for k,v in C.items() if v}

def transpose(A):return {(j,i):v for (i,j),v in A.items()}
def encoded(A):return [[i,j,str(c)] for (i,j),c in sorted(A.items())]
def main():
 data=json.loads((ROOT/'generated/heat_matrix_L2.json').read_text());mat={r['degree']:r['entries'] for r in data['matrices']};M=len(data['faces']);I={(i,i):F(1) for i in range(M)}
 def at(n,power):
  return {(i,j):v for i,j,raw in mat[n] if (v:=PF.from_json(raw).d.get((F(3),power),F(0)))}
 G2=at(2,1);G4=at(4,1);T2={k:-v for k,v in at(2,2).items()};L4={k:-v for k,v in at(4,2).items()};T4=plus(L4,mul(G2,T2),-1)
 if at(0,1)!=I:raise ArithmeticError('original band zero metric')
 if at(4,3)!=mul(T2,T2):raise ArithmeticError('complete quadratic heat time term')
 if T2!=transpose(T2):raise ArithmeticError('second band coefficient symmetry')
 if G2!=transpose(G2) or G4!=transpose(G4):raise ArithmeticError('band Gram symmetry')
 if plus(T4,mul(G2,T2))!=plus(transpose(T4),mul(T2,G2)):raise ArithmeticError('raw fourth band metric adjoint')
 # This validates every original boundary degree independently from the graph.
 def edges(p):
  n=p[:3];i,j=p[3:];a=list(n);a[i]+=1;b=list(n);b[j]+=1
  return {tuple(n)+(i,),tuple(a)+(j,),tuple(b)+(i,),tuple(n)+(j,)}
 ee=[edges(p) for p in data['faces']];expected={};degrees=[]
 for i in range(M):
  neighbors=[j for j in range(M) if j!=i and ee[i]&ee[j]];degrees.append(len(neighbors));expected[i,i]=F(7,15)-F(len(neighbors),21)
  for j in neighbors:expected[i,j]=-F(1,21)
 if T2!=expected:raise ArithmeticError('all original first-band adjacency coefficients')
 defect=plus(T4,transpose(T4),-1)
 if defect!=plus(mul(T2,G2),mul(G2,T2),-1):raise ArithmeticError('non-Euclidean fourth band defect')
 out={'schema':'ym-heat-first-band-v1','faces':data['faces'],'original_degrees':degrees,
      'band_energy':'kappa*(3I+xi^2*T2+xi^4*T4+O(xi^6))',
      'band_metric':'I+xi^2*G2+xi^4*G4+O(xi^6)',
      'G2':encoded(G2),'G4':encoded(G4),'T2':encoded(T2),'T4':encoded(T4),
      'fourth_raw_metric_defect':encoded(defect),
      'checks':{'entire_tau_squared_identity':True,'entire_raw_metric_self_adjointness':True,'all_original_face_degrees':True}}
 (ROOT/'generated/first_band_L2.json').write_text(json.dumps(out,separators=(',',':'))+'\n')
 print(json.dumps({k:len(out[k]) for k in ('G2','G4','T2','T4','fourth_raw_metric_defect')},sort_keys=True))
if __name__=='__main__':main()
