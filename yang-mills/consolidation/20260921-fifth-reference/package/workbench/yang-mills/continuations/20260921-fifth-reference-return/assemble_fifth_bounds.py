"""Assemble every original anchored fifth-source support and its marked edge."""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,argparse
ROOT=Path(__file__).resolve().parent

def need(t,msg):
 if not t:raise ArithmeticError(msg)

def assemble():
 g=json.loads((ROOT.parent/'20260917-fifth-source/generated/geometry_fifth.json').read_text())
 rows={i:json.loads((ROOT/'generated/rows'/f'{i:04d}.json').read_text()) for i in range(662)}
 hist={i:Counter() for i in rows};edge_maps={i:{frozenset(map(tuple,uv)):int(e) for e,uv in row['edge_coordinates']} for i,row in rows.items()}
 for tr in g['transports']:
  i=tr['class'];pm,ss=g['signed_operations'][tr['operation']];off=tr['translation']
  u=tuple(-off[j] for j in range(3));v=tuple(ss[j]*int(pm[j]==0)-off[j] for j in range(3))
  e=edge_maps[i][frozenset((u,v))];hist[i][e]+=1
 C=M=T=F(0);contributions=[]
 for row in g['classes']:
  i=row['index'];n=row['anchored_count'];rr=rows[i]
  need(sum(hist[i].values())==n,'marked-count-'+str(i))
  c=n*F(rr['C']);m=n*F(rr['M']);t=sum(k*F(rr['T'][str(e)]) for e,k in hist[i].items())
  C+=c;M+=m;T+=t
  contributions.append({'index':i,'count':n,'C':str(c),'M':str(m),'T':str(t),'marked_edges':{str(e):k for e,k in sorted(hist[i].items())}})
 need(sum(r['count'] for r in contributions)==124864,'complete-original-anchored-count')
 return {'schema':'ym-complete-fifth-source-budgets-v1','C5':str(C),'M5':str(M),'T5':str(T),'contributions':contributions}

def main():
 p=argparse.ArgumentParser();p.add_argument('--verify-existing',action='store_true');args=p.parse_args();out=ROOT/'generated/fifth_budgets.json';data=assemble();s=json.dumps(data,sort_keys=True,indent=2)+'\n'
 if args.verify_existing:need(out.read_text()==s,'budget-record')
 else:out.write_text(s)
 print(json.dumps({k:{'rational':data[k],'decimal_diagnostic':float(F(data[k]))} for k in ('C5','M5','T5')},indent=2))
if __name__=='__main__':main()
