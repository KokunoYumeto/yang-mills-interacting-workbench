"""Outward rational heat bounds and original 240-column metric certificates."""
from fractions import Fraction as F
from math import factorial
from pathlib import Path
from functools import lru_cache
from collections import defaultdict
import json
from exact_rational import PF
ROOT=Path(__file__).resolve().parent
@lru_cache(None)
def exp_minus(x):
    x=F(x)
    if x<0:raise ValueError('negative input to positive-time exponential enclosure')
    if x>50:raise ValueError('exponential certificate input outside declared interval')
    N=240;t=F(1);s=t
    for j in range(1,N+1):t*=-x/j;s+=t
    remainder=abs(t)*x/(N+1)
    lo,hi=s-remainder,s
    if not (0<lo<=hi):raise ArithmeticError('exponential bracket sign')
    return lo,hi

def heat_interval(R,t):
    lo=hi=F(0);t=F(t)
    for a,n,c in R.heat_terms():
      l,h=exp_minus(a*t);c*=t**n
      if c>=0:lo+=c*l;hi+=c*h
      else:lo+=c*h;hi+=c*l
    return lo,hi

def row_norm(entries,M):
    a=[F(0)]*M
    for i,j,c in entries:a[i]+=abs(c)
    return max(a)

def inverse_power(R,k):
    if k==0:return sum(c for (a,n),c in R.d.items() if n==1)
    # ∫ t^(k-1) e^(-a t) t^(n-1)/(n-1)!/(k-1)! dt.
    return sum(c*F(factorial(k+n-2),factorial(k-1)*factorial(n-1))/a**(k+n-1)
               for (a,n),c in R.d.items())

def run():
    M=240;beta=F(49,50);x=F(1,1600);u=M*x
    full=json.loads((ROOT/'generated/heat_matrix_L2.json').read_text());results={};series={}
    for k in (0,1,2):
      series[k]=[];norms={}
      for row in full['matrices']:
        deg=row['degree'];E=[(i,j,inverse_power(PF.from_json(v),k)) for i,j,v in row['entries']]
        E=[(i,j,c) for i,j,c in E if c];norms[deg]=row_norm(E,M)
        series[k].append({'degree':deg,'entries':[[i,j,str(c)] for i,j,c in E]})
      err=5/beta**k*u**6/(1-u*u);width=x*x*norms[2]+x**4*norms[4]+M*err
      lo,hi=F(1,3**k)-width,F(1,3**k)+width
      targets={0:(F(49,50),F(51,50)),1:(F(3,10),F(11,30)),2:(F(9,100),F(13,100))}[k]
      if not (targets[0]<lo<hi<targets[1]):raise ArithmeticError('native metric interval:'+str((k,float(lo),float(hi))))
      results[k]={'row_norms':{str(a):str(b) for a,b in norms.items()},'entry_remainder':str(err),
                  'eigenvalue_enclosure':[str(lo),str(hi)],'outer_interval':list(map(str,targets))}
    # The original first energy moment has exact edge support: diagonal <=4,
    # at most12 original neighbours of size<=1. Cauchy keeps that support.
    kin_series=[];knorm={}
    for row in full['matrices']:
      vals=[]
      for i,j,raw in row['entries']:
        rr=PF.from_json(raw)
        kk=sum(a*c for (a,n),c in rr.d.items() if n==1)-sum(c for (a,n),c in rr.d.items() if n==2)
        if kk:vals.append((i,j,kk))
      knorm[row['degree']]=row_norm(vals,M)
      kin_series.append({'degree':row['degree'],'entries':[[i,j,str(c)] for i,j,c in vals]})
    kerr=F(113,112)*16*u**6/(1-u*u)
    kwidth=x*x*knorm[2]+x**4*knorm[4]+kerr
    if not kwidth<F(1,10):raise ArithmeticError('original kinetic moment bound')
    kin={'row_norms':{str(k):str(v) for k,v in knorm.items()},'tail_row_bound':str(kerr),
         'eigenvalue_enclosure':[str(3-kwidth),str(3+kwidth)],'outer_interval':['29/10','31/10']}
    qmax=F(240,238**2)
    if not qmax<F(1,225):raise ArithmeticError('graph angle bound')
    pref=4*F(113,112)*F(226,225)*F(1793,1680)
    if not pref<5:raise ArithmeticError('heat prefactor')
    decay=1-F(1,120)-F(1,238)
    if not decay>beta:raise ArithmeticError('heat decay')
    epslo,epshi=exp_minus(27)
    determinant_error=1920*epshi/(1-epshi)
    if not determinant_error<F(4,10**9):raise ArithmeticError('finite heat determinant budget')
    R=PF.from_json(json.loads((ROOT/'generated/opposite_combined.json').read_text())['resolvent'])
    xi=F(1,10**10);tau=F(1);hl,hh=heat_interval(R,tau)
    _,eh=exp_minus(beta*tau);error=5*eh*(M*xi)**6/(1-(M*xi)**2)
    lo,hi=hl-error/xi**4,hh+error/xi**4
    if not (F(85879,10**7)<lo<hi<F(85951,10**7)):raise ArithmeticError('actual pointwise heat interval:'+str((float(lo),float(hi))))
    path=PF.from_json(json.loads((ROOT/'generated/opposite_path.json').read_text())['resolvent'])
    aa=path.d[(F(3),3)]/2;bb=path.d[(F(3),2)];cc=path.d[(F(3),1)];pmin=cc-bb*bb/(4*aa)
    neg=abs(path.d[(F(9,2),1)])/4+abs(path.d[(F(13,2),1)])/16
    if not pmin>neg:raise ArithmeticError('entire time interval path lower bound')
    if not exp_minus(F(3,2))[1]<F(1,4):raise ArithmeticError('exp3/2 bound')
    if not exp_minus(F(7,2))[1]<F(1,16):raise ArithmeticError('exp7/2 bound')
    cap=648*M**6*xi**2/(1-(M*xi)**2)/exp_minus(F(303,50))[0]
    if not cap<1:raise ArithmeticError('whole [1,3] time-interval positivity')
    out={'schema':'ym-rational-heat-bounds-v1','graph_constants':{'qmax':str(qmax),'prefactor':str(pref),'decay_lower':str(decay),'used_decay':str(beta)},
         'L2_native':{'M':M,'xi_max':str(x),'g_squared_min':'20','metrics':results,
                      'physical_gap_lower':'27*kappa/10','heat_horizon':'10/kappa','original_observation_fraction_lower':'150/221','original_kinetic_Gram':kin,'energy_residual_fraction_upper':'1322/7203',
                      'epsilon_upper':str(epshi),'four_quotient_determinant_error':str(determinant_error)},
         'opposite_pointwise':{'xi':str(xi),'g_squared':'50000','kappa':'100000/a','tau':'1',
                              'leading_coefficient_interval':[str(hl),str(hh)],'relative_to_xi4_error':str(error/xi**4),
                              'actual_C_over_xi4_interval':[str(lo),str(hi)],'outer_interval':['85879/10000000','85951/10000000']},
         'opposite_time_interval':{'tau':['1','3'],'path_quadratic_min':str(pmin),'negative_bound':str(neg),'remainder_to_cube_lower_ratio_upper':str(cap)}}
    (ROOT/'generated/heat_bounds.json').write_text(json.dumps(out,indent=2)+'\n')
    (ROOT/'generated/native_inverse_metrics_L2.json').write_text(json.dumps({'faces':full['faces'],'inverse_power_series':series,'original_kinetic_series':kin_series},separators=(',',':'))+'\n')
    print(json.dumps({'native':{k:list(map(float,[F(a) for a in v['eigenvalue_enclosure']])) for k,v in results.items()},
                     'pointwise':[float(lo),float(hi)],'time_interval_margin_ratio':float(cap),'det_error':float(determinant_error)},indent=2))
    return out
if __name__=='__main__':run()
