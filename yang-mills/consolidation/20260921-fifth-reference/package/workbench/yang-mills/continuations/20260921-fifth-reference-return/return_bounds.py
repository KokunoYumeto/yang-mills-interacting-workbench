"""Exact fifth-reference endpoint, heat-circle, and physical-complement bounds."""
from pathlib import Path
from fractions import Fraction as F
import math,json,argparse
ROOT=Path(__file__).resolve().parent

def need(t,s):
 if not t:raise ArithmeticError(s)

def sqrt_box(x,digits=35):
 x=F(x);need(x>=0,'sqrt-domain');scale=10**digits;n=math.isqrt(x.numerator*scale*scale//x.denominator)
 lo,hi=F(n,scale),F(n+1,scale);need(lo*lo<=x<hi*hi,'sqrt-endpoints');return lo,hi

def exponential_upper(x):
 # e^(-x) lies below every even Taylor sum, by its signed integral remainder.
 x=F(x);term=F(1);s=term
 for n in range(1,121):term*=-x/n;s+=term
 need(s>0,'exp-upper-positive');return s

M=[F(0),F(64,3),F(5834,39),F(336572872,208845),F(17270702970768271,341697152160),F(1638684)]
T=[F(0),F(16,3),F(137,6),F(225985217,1253070),F(110695177857394584026401,18025447358750832000),F(190128)]
L=[m+4*t for m,t in zip(M,T)]
B={(i,j):3*(M[i]*T[j]+M[j]*T[i]) for i in range(1,6) for j in range(1,6)}
DCO={n:sum(B[i,j] for i in range(1,6) for j in range(1,6) if i+j==n) for n in range(6,11)}

def ell(x):return sum(L[i]*x**i for i in range(1,6))
def delta(x):return sum(c*x**n for n,c in DCO.items())
def disc(x):return (1-ell(x))**2-F(8,3)*delta(x)
def gap_interval(x):
 sl,sh=sqrt_box(disc(x));pol=sum((F(3,2)*M[i]-6*T[i])*x**i for i in range(1,6))
 return F(3,2)*(1+sl)+pol,F(3,2)*(1+sh)+pol

def calculate():
 data=json.loads((ROOT/'generated/fifth_budgets.json').read_text())
 need(F(data['M5'])<M[5] and F(data['T5'])<T[5],'rounded-actual-fifth-budgets')
 need(all(F(3,2)*M[i]-6*T[i]>=0 for i in range(1,6)),'positive-physical-return-coefficients')
 lo,hi=F(18,1000),F(19,1000)
 need(disc(lo)>0>disc(hi) and ell(hi)<1,'first-root-isolation')
 # ell and delta have positive coefficients.  While ell<1, D is strictly decreasing.
 for _ in range(180):
  mid=(lo+hi)/2
  if disc(mid)>0:lo=mid
  else:hi=mid
 rootbr=[lo,hi]
 glo=sqrt_box(1/(4*hi))[0];ghi=sqrt_box(1/(4*lo))[1]
 benchmarks=[]
 for g in (F(37,10),F(15,4),F(4),F(8),F(10),F(12),F(25,2),F(13),F(16)):
  x=1/(4*g*g);need(disc(x)>0,'benchmark-domain-'+str(g));gl,gh=gap_interval(x)
  sl,sh=sqrt_box(disc(x));wl=F(3,4)*(1-ell(x)-sh);wh=F(3,4)*(1-ell(x)-sl)
  benchmarks.append({'g_squared_min':str(g),'xi_max':str(x),'gap_over_kappa':[str(gl),str(gh)],'correction_norm':[str(wl),str(wh)]})
 radius=F(1,55);decay=F(13,8);chi=1-decay/3;pref=(1+255*chi)/(1-chi)**2
 need(gap_interval(radius)[0]>decay and ell(radius)<1,'new-heat-circle')
 need(radius>F(3,256),'heat-radius-strict-growth')
 # Retain the sign of 9*tau-6 until the final absolute integral.
 eupper=F(339,1000);need(exponential_upper(F(2,3)*decay)<eupper,'signed-heat-weight-exponential')
 signed_pref=pref*(1+6/decay-9/decay**2+18*eupper/decay**2)
 need(signed_pref<pref*(1+6/decay+9/decay**2),'signed-weight-improvement')
 prev=ROOT.parent/'20260921-volume-heat-return/generated/anchored_coefficients.json'
 A={(r['kind'],r['degree']):F(r['absolute_motif_bound']) for r in json.loads(prev.read_text())['bounds']}
 native=[]
 for g in (F(8),F(10),F(12),F(25,2),F(13),F(16)):
  x=1/(4*g*g);tail=(x/radius)**6/(1-(x/radius)**2)
  gl=gap_interval(x)[0];d=F((gl*10000).numerator//(gl*10000).denominator,10000)
  widths={}
  for k in ('0','1','2','kinetic','leakage'):
   c=pref/decay**int(k) if k.isnumeric() else (606 if k=='kinetic' else signed_pref)
   widths[k]=A[k,2]*x*x+A[k,4]*x**4+c*tail
  l0,u0=1-widths['0'],1+widths['0'];l1,u1=F(1,3)-widths['1'],F(1,3)+widths['1'];l2,u2=F(1,9)-widths['2'],F(1,9)+widths['2']
  need(min(l0,l1,l2)>0,'native-original-Grams-'+str(g))
  beta=widths['leakage'];obs=l1*l1/(u0*u2);loss=beta/(d*l1);extra=beta/(d*d*l2)
  kinU=3+widths['kinetic'];sec=u1*kinU/(l0*l0)-1
  native.append({'g_squared_min':str(g),'xi_max':str(x),'physical_gap_over_kappa':str(d),'widths':{k:str(v) for k,v in widths.items()},
                 'observation_fraction_lower':str(obs),'complement_loss_upper':str(loss),'state_increase_upper':str(extra),'section_energy_upper':str(sec),
                 'G0':[str(l0),str(u0)],'G1':[str(l1),str(u1)],'G2':[str(l2),str(u2)]})
 return {'schema':'ym-fifth-reference-physical-return-v1','M':list(map(str,M[1:])),'T':list(map(str,T[1:])),
         'linear_coefficients':{str(i):str(L[i]) for i in range(1,6)},'residual_coefficients':{str(n):str(c) for n,c in DCO.items()},
         'alpha_bracket':list(map(str,rootbr)),'g_squared_threshold_bracket':[str(glo),str(ghi)],'benchmarks':benchmarks,
         'heat_circle':{'radius':str(radius),'decay':str(decay),'chi_upper':str(chi),'prefactor':str(pref),
                        'signed_leakage_prefactor':str(signed_pref),'exp_upper':str(eupper)},'native':native}

def main():
 p=argparse.ArgumentParser();p.add_argument('--verify-existing',action='store_true');a=p.parse_args();out=ROOT/'generated/physical_return.json';d=calculate();s=json.dumps(d,sort_keys=True,indent=2)+'\n'
 if a.verify_existing:need(out.read_text()==s,'return-record')
 else:out.write_text(s)
 print('alpha',*(float(F(v)) for v in d['alpha_bracket']),'g^2',*(float(F(v)) for v in d['g_squared_threshold_bracket']))
 for n in d['native']:print(n['g_squared_min'],*[k+'='+str(float(F(n[k]))) for k in ('observation_fraction_lower','complement_loss_upper','state_increase_upper','section_energy_upper')])
 print('heat',d['heat_circle'])
if __name__=='__main__':main()
