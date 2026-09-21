"""Independent original single-face and six-face-cube heat recurrences.
No imported trace differentiation or K-polynomial projection engine.
"""
from fractions import Fraction as F
from functools import lru_cache
from itertools import permutations,combinations
from pathlib import Path
from collections import Counter
from exact_rational import PF,pole
import json
ROOT=Path(__file__).resolve().parent

def single_face(order=4):
    # Infinite original character coordinates chi_(j/2). All paths contributing
    # at this order have j<=order+1; no path beyond that index can return here.
    J=order+2;u=[[F(0) for _ in range(J)] for _ in range(order+1)];u[0][0]=F(1)
    e=[F(0)]*(order+1)
    for n in range(1,order+1):
      e[n]=-u[n-1][1]
      for j in range(1,J):
        source=(u[n-1][j-1] if j else 0)+(u[n-1][j+1] if j+1<J else 0)
        source+=sum(e[k]*u[n-k][j] for k in range(1,n+1))
        u[n][j]=source/F(j*(j+2))
    norm=[sum(sum(a*b for a,b in zip(u[k],u[n-k])) for k in range(n+1)) for n in range(order+1)]
    means=[]
    for n in range(order+1):
      num=sum(sum(u[k][j]*(u[n-k][j-1] if j else 0)+u[k][j]*(u[n-k][j+1] if j+1<J else 0) for j in range(J)) for k in range(n+1))
      means.append(num-sum(norm[k]*means[n-k] for k in range(1,n+1)))
    h=[[PF() for _ in range(J)] for _ in range(order+1)]
    for n in range(order+1):
      for j in range(J):
        rhs=PF((u[n][j-1] if j else 0)+(u[n][j+1] if j+1<J else 0))
        if n:rhs+=(h[n-1][j-1] if j else 0)+(h[n-1][j+1] if j+1<J else 0)
        rhs+=sum((e[k]*h[n-k][j] for k in range(1,n+1)),PF())
        h[n][j]=pole(j*(j+2))*rhs
    raw=[];cor=[]
    for n in range(order+1):
      num=PF()
      for k in range(n+1):
       for j in range(J):num+=u[k][j]*((h[n-k][j-1] if j else 0)+(h[n-k][j+1] if j+1<J else 0))
      raw.append(num-sum((norm[k]*raw[n-k] for k in range(1,n+1)),PF()))
      cor.append(raw[n]-pole(0)*sum(means[k]*means[n-k] for k in range(n+1)))
    return cor

def face_edges(face):
    n=face[:3];i,j=face[3:];a=list(n);a[i]+=1;b=list(n);b[j]+=1
    return (tuple(n)+(i,),tuple(a)+(j,),tuple(b)+(i,),tuple(n)+(j,))
def boundary_energy(faces):
    cnt=Counter(e for p in faces for e in face_edges(p))
    return F(3,4)*sum(v%2 for v in cnt.values())

def cube_heat(faces,p,q):
    others=tuple(i for i in range(6) if i not in (p,q));ans=PF();rows=[]
    for perm in permutations(others):
      for nr in range(5):
        for nm in range(5-nr):
          right=perm[:nr];middle=perm[nr:nr+nm];left=perm[nr+nm:]
          coeff=F(1,16);vr=[];vl=[];rates=[]
          for seq,target in ((right,vr),(left,vl)):
            for j in range(1,len(seq)+1):
              en=boundary_energy(tuple(faces[i] for i in seq[:j]));coeff/=en;target.append(str(en))
          occ=(q,)+right;en=boundary_energy(tuple(faces[i] for i in occ));v=coeff*pole(en);rates.append(str(en))
          for i in middle:
            occ+= (i,);en=boundary_energy(tuple(faces[j] for j in occ));v*=pole(en);rates.append(str(en))
          ans+=v
          rows.append({'right_order':right,'middle_order':middle,'left_order':left,
                       'right_vacuum_energies':vr,'left_vacuum_energies':vl,'heat_energies':rates,
                       'vacuum_and_Haar_factor':str(coeff)})
    return ans,rows

def main():
    data=json.loads((ROOT/'generated/heat_coefficients.json').read_text())['cases'];orig=single_face()
    checks=[]
    for row in data:
      if row['type']=='self':
        r=PF.from_json(row['responses'][0]['resolvent']);n=row['degree']
        if r!=orig[n]:raise ArithmeticError('independent single-face heat mismatch')
        checks.append({'name':'original-character-heat-'+str(n),'passed':True})
    cube=next(row for row in data if row['type']=='cube');paths=[]
    for row in cube['responses']:
      val,records=cube_heat(tuple(map(tuple,cube['faces'])),row['p'],row['q'])
      if val!=PF.from_json(row['resolvent']):raise ArithmeticError('independent cube boundary-order mismatch')
      if len(records)!=360:raise ArithmeticError('missing original cube insertion orders')
      paths.append({'p':row['p'],'q':row['q'],'resolvent':val.to_json(),'orders':records})
      checks.append({'name':'original-cube-heat-'+str((row['p'],row['q'])),'passed':True})
    (ROOT/'generated/independent_heat.json').write_text(json.dumps({'schema':'ym-independent-heat-v1','checks':checks,'single_face':[r.to_json() for r in orig]},indent=2)+'\n')
    (ROOT/'generated/cube_heat_orders.json').write_text(json.dumps({'faces':cube['faces'],'marked_cases':paths},separators=(',',':'))+'\n')
    print('independent original-character and 5400 cube orders passed',flush=True)
if __name__=='__main__':main()
