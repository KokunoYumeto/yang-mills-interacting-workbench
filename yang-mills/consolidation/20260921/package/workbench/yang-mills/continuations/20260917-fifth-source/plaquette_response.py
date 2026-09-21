"""Exact full plaquette response through homogeneous degree four.
All source multiplicities and original finite-box faces remain attached.
The returned matrix is kappa*<r_p,(H-E0)^(-1)r_q>=-e''[p,q]/2.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict,Counter
from itertools import combinations,product,permutations
from functools import lru_cache
import sys,json
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT.parent/'20260916-cubic-linearized'))
import geometry as g
A6=-F(289,77760);B6=F(22285,47309184)
TRIPLE={'path':-F(4909,118272960),'common':F(244,4312035),'corner':-F(212,542997)}
CUBE=-F(83,1944)
A4=F(5,216);B4=-F(2,1053)
@lru_cache(None)
def adj(p):return g.adjacent(p)

def faces_box(L):
 return tuple(n+(i,j) for n in product(range(-L,L+1),repeat=3)
  for i,j in combinations(range(3),2) if n[i]<L and n[j]<L)
def cube(n):
 ps=[]
 for i,j in combinations(range(3),2):
  k=3-i-j;ps += [tuple(n)+(i,j),g.add(n,k)+(i,j)]
 return tuple(sorted(ps))
def cubes_containing(p):
 k=3-p[3]-p[4]
 return (cube(p[:3]),cube(g.add(p[:3],k,-1)))
def triples_containing(p):
 out=set()
 for q in adj(p):
  for r in adj(p)|adj(q):
   if r not in (p,q):out.add(tuple(sorted((p,q,r))))
 return tuple(sorted(out))

def matrix_for_faces(ps):
 ps=tuple(ps);p_set=set(ps);ids={p:i for i,p in enumerate(ps)}
 E={2:defaultdict(F),4:defaultdict(F),6:defaultdict(F)}
 # Add -one half the exact Hessian of a labelled monomial.
 def term(deg,coeff,exps):
  for p,np in exps.items():
   for q,nq in exps.items():
    factor=np*(nq-int(p==q))
    if factor:E[deg][(ids[p],ids[q])]-=coeff*factor/2
 for p in ps:
  term(2,-F(1,3),{p:2});term(4,A4,{p:4});term(6,A6,{p:6})
 pairs={tuple(sorted((p,q))) for p in ps for q in adj(p) if q in p_set}
 for p,q in sorted(pairs):
  term(4,B4,{p:2,q:2});term(6,B6,{p:4,q:2});term(6,B6,{p:2,q:4})
 triples={t for p in ps for t in triples_containing(p) if set(t)<=p_set}
 type_counts=Counter()
 for t in sorted(triples):
  typ=g.type3(t);type_counts[typ]+=1
  if typ not in TRIPLE:raise ArithmeticError('disconnected-triple')
  term(6,TRIPLE[typ],dict.fromkeys(t,2))
 cubes={c for p in ps for c in cubes_containing(p) if set(c)<=p_set}
 for c in sorted(cubes):term(6,CUBE,dict.fromkeys(c,1))
 for n in E:E[n]={k:v for k,v in E[n].items() if v}
 return E,{'faces':len(ps),'pairs':len(pairs),'triples':dict(type_counts),'cubes':len(cubes)}

def bulk_row(p):
 rows={0:defaultdict(F),2:defaultdict(F),4:defaultdict(F)}
 rows[0][p]=F(1,3);rows[2][p]-=6*A4;rows[4][p]-=15*A6
 for q in adj(p):
  rows[2][p]-=B4;rows[2][q]-=2*B4
  rows[4][p]-=7*B6;rows[4][q]-=8*B6
 for t in triples_containing(p):
  c=TRIPLE[g.type3(t)];rows[4][p]-=c
  for q in t:
   if q!=p:rows[4][q]-=2*c
 for c in cubes_containing(p):
  for q in c:
   if q!=p:rows[4][q]-=CUBE/2
 return {j:{q:c for q,c in row.items() if c} for j,row in rows.items()}

def generate():
 (ROOT/'generated').mkdir(exist_ok=True)
 p=(0,0,0,0,1);row=bulk_row(p);op=(0,0,1,0,1)
 coef=row[4][op];expected=-8*TRIPLE['path']-CUBE/2
 if coef!=expected:raise ArithmeticError('opposite-cube-row')
 # Three orientation rows at the original origin; keep centre phases explicit.
 orientations=((1,2),(0,2),(0,1));symbols={}
 for i,aa in enumerate(orientations):
  rr=bulk_row((0,0,0)+aa)
  for degree,row0 in rr.items():
   for q,c in row0.items():
    j=orientations.index(q[3:]);dp=tuple(2*q[k]+int(k in q[3:])-int(k in aa) for k in range(3))
    symbols[degree,i,j,dp]=c
 zero={degree:[[sum(c for (d,a,b,_),c in symbols.items() if (d,a,b)==(degree,i,j))
                  for j in range(3)] for i in range(3)] for degree in (0,2,4)}
 bands={}
 for d,A in zero.items():
  if any(A[i][i]!=A[0][0] for i in range(3)) or any(A[i][j]!=A[0][1] for i in range(3) for j in range(3) if i!=j):raise ArithmeticError('cubic-orientation-symmetry')
  bands[d]={'scalar':str(A[0][0]+2*A[0][1]),'traceless':str(A[0][0]-A[0][1]),'diagonal':str(A[0][0]),'off_diagonal':str(A[0][1])}
 cases=[]
 for L in (2,3):
  ps=faces_box(L);mat,counts=matrix_for_faces(ps)
  m=2*L;M=3*m*m*(m+1);J=6*m*(3*m*m-1)
  e6=-F(211396463*m**3+30959193*m*m+21845782*m+2336684,4691494080)
  target={2:F(M,3),4:-6*(A4*M+B4*J),6:-15*e6}
  for d in (2,4,6):
   if sum(mat[d].values())!=target[d]:raise ArithmeticError('homogeneous-Hessian-total:'+str((L,d)))
   if any(mat[d].get((j,i))!=c for (i,j),c in mat[d].items()):raise ArithmeticError('matrix-adjoint:'+str((L,d)))
  ids={x:i for i,x in enumerate(ps)}
  for degree in (0,2,4):
   for q,c in row[degree].items():
    if L>=3 and mat[degree+2].get((ids[p],ids[q]),F(0))!=c:raise ArithmeticError('bulk-finite-row:'+str((L,degree,q)))
  if mat[6].get((ids[p],ids[op]))!=coef:raise ArithmeticError('finite-opposite-cube-row')
  out={'schema':'ym-original-response-matrix-v1','L':L,'faces':ps,'counts':counts,
       'matrices':[{'degree':d-2,'entries':[[i,j,str(c)] for (i,j),c in sorted(mat[d].items())]} for d in (2,4,6)]}
  path=ROOT/f'generated/response_L{L}.json';path.write_text(json.dumps(out,separators=(',',':'))+'\n')
  cases.append({'L':L,'counts':counts,'total_coefficients':{str(d-2):str(v) for d,v in target.items()},'nonzero_entries':{str(d-2):len(mat[d]) for d in mat}})
 # Actual finite-volume Cauchy tail at M=240, xi=1e-13.
 xi=F(1,10**13);radius=F(3,16*240);t=xi/radius
 error=F(128,3)*t**6/(1-t*t)
 lo,hi=coef-error/xi**4,coef+error/xi**4
 if lo<=0:raise ArithmeticError('opposite-response-positive-enclosure')
 out={'schema':'ym-signed-response-calculation-v1','exact_sixth_weights':{'self':str(A6),'ordered_pair_4_2':str(B6),**{k:str(v) for k,v in TRIPLE.items()},'cube':str(CUBE)},
      'bulk_anchor':p,'bulk_rows':{str(d):[[q,str(c)] for q,c in sorted(r.items())] for d,r in row.items()},
      'Fourier_symbol':[{'degree':d,'source_orientation':a,'target_orientation':b,'twice_centre_displacement':dp,'coefficient':str(c)} for (d,a,b,dp),c in sorted(symbols.items())],
      'orientation_axes':orientations,'zero_momentum':bands,
      'opposite_faces':{'p':p,'q':op,'path_count':4,'cube_count':1,'xi4_path_term':str(-8*TRIPLE['path']),'xi4_cube_term':str(-CUBE/2),'xi4_total':str(coef)},
      'finite_boxes':cases,'actual_opposite_enclosure':{'L':2,'M':240,'xi':str(xi),'g_squared':'500000*sqrt(10)','kappa':'1000000*sqrt(10)/a','analytic_radius':str(radius),'absolute_error':str(error),'C_over_xi4_interval':[str(lo),str(hi)]}}
 (ROOT/'generated/plaquette_response.json').write_text(json.dumps(out,indent=2,sort_keys=True)+'\n')
 print(json.dumps({'opposite_coefficient':str(coef),'opposite_decimal':float(coef),'zero_momentum':bands,'finite_boxes':cases,'opposite_interval':[float(lo),float(hi)]},indent=2),flush=True)
if __name__=='__main__':generate()
