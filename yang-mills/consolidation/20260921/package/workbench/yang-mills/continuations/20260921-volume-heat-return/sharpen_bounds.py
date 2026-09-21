#!/usr/bin/env python3
"""Evaluate the original-Haar split of the heat-row bound, exactly."""
from fractions import Fraction as F
from pathlib import Path
import argparse,json,hashlib
ROOT=Path(__file__).resolve().parent

def need(ok,name):
 if not ok:raise ArithmeticError(name)

def calculate():
 data=json.loads((ROOT/'generated/anchored_coefficients.json').read_text())
 B={(r['kind'],r['degree']):F(r['absolute_motif_bound']) for r in data['bounds']}
 R0=F(3,256);R1=F(45,4096);chi=F(3,8);C=F(6184,25);a=F(15,8)
 need(R1==F(3,64)*chi*(1-chi),'original-radius')
 need(C==(1+255*chi)/(1-chi)**2 and a==3*(1-chi),'original-Haar-bound')
 rows=[]
 targets={10:(F(39,50),F(18,25),F(33,25),F(1,6)),12:(F(97,100),F(243,250),F(103,100),F(1,60)),16:(F(999,1000),F(999,1000),F(1001,1000),F(1,1900))}
 for g,d in ((10,F(14,5)),(12,F(72,25)),(16,F(117,40))):
  x=F(1,4*g*g);t0=(x/R0)**6/(1-(x/R0)**2);t1=(x/R1)**6/(1-(x/R1)**2)
  need((d/F(3,2)-1)**2<1-F(256,3)*x,'full-space-gap:'+str(g))
  w={}
  for k in ('0','1','2','kinetic','leakage'):
   if k.isnumeric():err=min(512*F(2,3)**int(k)*t0,C/a**int(k)*t1)
   elif k=='kinetic':err=606*t0
   else:err=min(4608*t0,C*(1+6/a+9/a**2)*t1)
   w[k]=x*x*B[k,2]+x**4*B[k,4]+err
  l0,u0=1-w['0'],1+w['0'];l1,u1=F(1,3)-w['1'],F(1,3)+w['1'];l2,u2=F(1,9)-w['2'],F(1,9)+w['2'];uK=3+w['kinetic'];beta=w['leakage']
  need(min(l0,l1,l2)>0,'positive-original-Grams')
  obs=l1*l1/(u0*u2);loss=beta/(d*l1);extra=beta/(d*d*l2);sec=u1*uK/(l0*l0)-1
  to,te,tg,ts=targets[g]
  need(obs>to and 1-loss>te and 1+extra<tg and sec<ts,'all-returned-bounds:'+str(g))
  if g==16:
   need(loss<F(1,34**2),'whole-space-mixed-factor')
   for k,v in {'0':124,'1':66,'2':36,'kinetic':205,'leakage':832}.items():need(w[k]<F(v,10**6),'sharp-width:'+k)
  rows.append({'g_squared_min':g,'xi_max':str(x),'physical_gap_over_kappa':str(d),'radii':{k:str(v) for k,v in w.items()},'spectral_intervals':{'G0':[str(l0),str(u0)],'G1':[str(l1),str(u1)],'G2':[str(l2),str(u2)]},'observed_fraction_lower':str(obs),'complement_loss_upper':str(loss),'restored_state_addition_upper':str(extra),'state_section_energy_upper':str(sec),'outer_return':list(map(str,targets[g]))})
 return {'schema':'ym-sharpened-original-Haar-v1','radius':str(R1),'chi':'3/8','heat_prefactor':str(C),'heat_decay_tau':str(a),'benchmarks':rows}

def main():
 p=argparse.ArgumentParser();p.add_argument('--verify-existing',action='store_true');p.add_argument('--output',type=Path);a=p.parse_args();out=a.output or ROOT/'generated/sharp_constants.json';s=json.dumps(calculate(),sort_keys=True,indent=2)+'\n'
 if a.verify_existing:need(out.read_text()==s,'sharp-record-mismatch')
 else:out.write_text(s)
 print('COMPLETE',hashlib.sha256(s.encode()).hexdigest())
if __name__=='__main__':
 try:main()
 except (ValueError,OSError,ArithmeticError) as e:raise SystemExit('FAIL: '+str(e))
