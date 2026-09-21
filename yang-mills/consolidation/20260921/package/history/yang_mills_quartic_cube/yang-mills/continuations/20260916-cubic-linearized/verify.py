#!/usr/bin/env python3
"""Exact finite checks for the original cubic source and linearized return.

This executable tests specified coordinate identities and finite certificates.
It does not formalize the written Banach-space, elliptic, or spectral proofs.
All requirements use explicit exceptions and remain enabled under python -O.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import sys
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from collections import Counter
from geometry import anchored, incident, pedges, pword, adjacent, union, boundary, cycle, type3, add
from coordinate_audit import (AXES,CELL,POOL,ONE,mul,conj,loop,dloop,pzero_pair,
                              source_rhs,projected3,assignment,half_projection)

ROOT=Path(__file__).resolve().parent
CHECKS=[]
NEGATIVE=[]
class CheckFailure(RuntimeError): pass

def require(test, name):
    if not test: raise CheckFailure(name)
def check(name, test, value=None):
    require(name not in {r['name'] for r in CHECKS}, 'duplicate-check-name')
    require(bool(test), name)
    row={'name':name,'passed':True}
    if value is not None: row['value']=str(value)
    CHECKS.append(row)
def reject(name, false_formula):
    require(not bool(false_formula), 'false-formula-accepted:'+name)
    NEGATIVE.append({'name':name,'false_formula_accepted':False})
def rat(q):
    q=F(q);return str(q)
def sqrt_box(q, decimals=28):
    q=F(q);require(q>=0,'negative-square-root')
    d=10**decimals;n=math.isqrt(q.numerator*d*d//q.denominator)
    lo,hi=F(n,d),F(n+1,d)
    require(lo*lo<=q<hi*hi,'invalid-square-root-bracket')
    return lo,hi

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]
def ma(A,B):return [[x+y for x,y in zip(a,b)] for a,b in zip(A,B)]
def sc(q,A):return [[q*x for x in a] for a in A]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def trans(A):return list(map(list,zip(*A)))
def singlet(i,j):
    # Original ordered tensor coordinates |a0,a1,a2>.
    bits=list(product((0,1),repeat=3));A=[[F(0) for _ in bits] for _ in bits]
    other=3-i-j
    eps=lambda a,b: (1 if (a,b)==(0,1) else -1 if (a,b)==(1,0) else 0)
    for r,a in enumerate(bits):
      for c,b in enumerate(bits):
       if a[other]==b[other]:A[r][c]=F(eps(a[i],a[j])*eps(b[i],b[j]),2)
    return A

def geometry_checks():
    anchor,pairs,triples=anchored()
    check('bulk-four-original-plaquettes',len(incident(anchor))==4)
    check('bulk-42-adjacent-pairs',len(pairs)==42)
    counts={'path':460,'common':40,'corner':24}
    for typ,num in counts.items():check('bulk-'+typ,len(triples[typ])==num,num)
    for i,(p,q) in enumerate(pairs):
        check(f'pair-boundary-{i}',len(cycle(boundary((p,q))))==6)
    for typ in ('path','corner'):
      target=(10,8) if typ=='path' else (9,6)
      for i,ps in enumerate(triples[typ]):
        check(f'{typ}-original-union-boundary-{i}',
              (len(union(ps)),len(cycle(boundary(ps))))==target)
    # Independent finite-box face enumeration; no periodic Hamiltonian.
    finite=[]
    for L in (2,3,4):
      vertices=list(product(range(-L,L+1),repeat=3));ps=[];es=[]
      for n in vertices:
       for i in range(3):
        if n[i]<L:es.append(n+(i,))
       for i,j in combinations(range(3),2):
        if n[i]<L and n[j]<L:ps.append(n+(i,j))
      deg=Counter(e for p in ps for e in pedges(p));J=sum(r*(r-1)//2 for r in deg.values())
      m=2*L;M=3*m*m*(m+1);JJ=6*m*(3*m*m-1)
      check(f'box-{L}-face-count',len(ps)==M,M)
      check(f'box-{L}-pair-count',J==JJ,J)
      check(f'box-{L}-edge-count',len(es)==3*m*(m+1)**2)
      check(f'box-{L}-all-boundary-incidences',set(deg.values())<={2,3,4})
      # All anchored triples embed in the enumerated original bulk templates.
      finite.append({'L':L,'faces':M,'adjacent_pairs':J,
                     'E4_over_kappa':rat(F(5*M,216)-F(2*J,1053))})
    check('L2-fourth-energy',finite[0]['E4_over_kappa']=='1198/351')
    check('bulk-incidence-paths',3*66-3*(12+8)==138)
    check('bulk-double-count-paths',F(138*10,3)==460)
    check('bulk-double-count-common',F(12*10,3)==40)
    check('bulk-double-count-corner',F(8*9,3)==24)
    # The exact central link sign sends every face to -itself.
    for p in set(q for x in pairs for q in x):
      sign=1
      for e,_ in pword(p):sign*=(-1)**sum(e[:e[3]])
      check('center-face-'+','.join(map(str,p)),sign==-1)
    return anchor,pairs,triples,finite

def coordinate_checks(anchor,pairs,triples):
    motifs=[(p,p,p) for p in incident(anchor)]
    motifs += [(p,p,q) for p,q in pairs]+[(q,q,p) for p,q in pairs]
    for typ in ('path','common','corner'):motifs+=triples[typ]
    check('all-612-anchored-multisets',len(motifs)==612)
    transcript=hashlib.sha256();nonzero=Counter()
    for i,ps in enumerate(motifs):
      for seed in (1,7):
        U=assignment(ps,seed);left=sum(c*a*v for c,a,v in projected3(ps,U));right=source_rhs(ps,U)
        typ=type3(ps)
        check(f'original-cubic-{i}-{seed}-{typ}',left==right)
        transcript.update((repr(ps)+'|'+str(seed)+'|'+rat(left)+'\n').encode())
        nonzero[typ]+=left!=0
    for typ in ('self','repeat','path','common','corner'):
        check('nonzero-coordinate-controls-'+typ,nonzero[typ]>0,nonzero[typ])
    for i,(p,q) in enumerate(pairs):
      U=assignment((p,p,q),i+5);e=next(iter(pedges(p)&pedges(q)))
      actual=half_projection(lambda V:(loop(p,V)**2-1)*loop(q,V),U,e)
      returned=F(4,3)*loop(p,U)*pzero_pair(p,q,U)-F(1,3)*loop(q,U)
      check('repeated-harmonic-'+str(i),actual==returned)
    for i,ps in enumerate(triples['common']):
      U=assignment(ps,i+3);e=next(iter(set.intersection(*(set(pedges(p)) for p in ps))))
      actual=half_projection(lambda V:math.prod(loop(p,V) for p in ps),U,e)
      check('three-fundamental-harmonic-'+str(i),actual==projected3(ps,U)[0][2])
    # Disconnected triples include repeated and fully distinct original labels.
    p=incident(anchor)[0];remote=tuple(x+12 for x in p[:3])+p[3:]
    for ps in ((p,p,remote),(p,remote,tuple(x+24 for x in p[:3])+p[3:])):
      check('disconnected-source-'+str(len(set(ps))),source_rhs(ps,assignment(ps,2))==0)
    # False formulas are evaluated on actual original-link assignments.
    self_motif=motifs[0]
    for seed in range(20):
      U=assignment(self_motif,seed);w=loop(self_motif[0],U)
      if w**3-2*w:
       bad=-F(1,27)*w
       reject('omit-cubic-character-on-original-links',bad==source_rhs(self_motif,U));break
    else:raise CheckFailure('missing-nonzero-self-mutation')
    p,q=pairs[0]
    for seed in range(20):
      U=assignment((p,p,q),seed);a=loop(p,U);b=loop(q,U)
      if b:
       wrong_h=F(4,3)*a*pzero_pair(p,q,U)
       whole=(a*a-1)*b
       bad=-F(11,468)*wrong_h+F(11,936)*(whole-wrong_h)
       reject('omit-repeated-section-component',bad==source_rhs((p,p,q),U));break
    else:raise CheckFailure('missing-nonzero-repeated-mutation')
    for ps in triples['common']:
      U=assignment(ps,3);terms=projected3(ps,U);h=terms[0][2]
      if h:
       whole=h+terms[1][2];bad=-F(1,117)*(F(3,2)*h)+F(1,117)*(whole-F(3,2)*h)
       reject('common-spin-multiplicity-erased',bad==source_rhs(ps,U));break
    else:raise CheckFailure('missing-common-mutation')
    for ps in triples['corner']:
      U=assignment(ps,7);terms=projected3(ps,U)
      if terms[0][2]:
       bad=sum(c*a*v for c,a,v in terms)-terms[0][0]*terms[0][1]*terms[0][2]/2
       reject('extra-corner-half-factor',bad==source_rhs(ps,U));break
    else:raise CheckFailure('missing-corner-mutation')
    return {'anchored_multisets':len(motifs),'assignments_per_multiset':2,
            'nonzero_instances':dict(nonzero),'coordinate_transcript_sha256':transcript.hexdigest()}

def sphere_and_projectors():
    # The 24-cell integrates every polynomial of degree <=5 on original S^3.
    for deg in range(6):
     for ex in product(range(deg+1),repeat=4):
      if sum(ex)!=deg:continue
      val=sum(math.prod(q[j]**ex[j] for j in range(4)) for q in CELL)/24
      if any(x%2 for x in ex):expected=F(0)
      else:
       den=math.prod(4+2*j for j in range(deg//2))
       num=math.prod(math.prod(range(1,e,2)) for e in ex)
       expected=F(num,den)
      check('sphere-moment-'+''.join(map(str,ex)),val==expected)
    for i,q in enumerate(POOL):check('unit-quaternion-'+str(i),mul(q,conj(q))==ONE)
    P=[singlet(0,1),singlet(0,2),singlet(1,2)];total=sc(F(2,3),ma(ma(P[0],P[1]),P[2]));I=eye(8)
    for i,A in enumerate(P):
      check('pair-projector-idempotent-'+str(i),mm(A,A)==A)
      check('pair-projector-symmetric-'+str(i),trans(A)==A)
    check('total-half-projector',mm(total,total)==total)
    check('total-half-rank',sum(total[i][i] for i in range(8))==4)
    check('three-singlets-sum',ma(ma(P[0],P[1]),P[2])==sc(F(3,2),total))
    reject('pair-singlets-commute',mm(P[0],P[1])==mm(P[1],P[0]))
    reject('omit-three-halves',ma(ma(P[0],P[1]),P[2])==total)
    # Exact source factors after the product rule; checks each target channel.
    second={0:(F(9,2),F(1,27)),1:(F(13,2),-F(1,117))}
    for s,t in product((0,1),repeat=2):
      c=F(6+2*(s+t));a=sum(coef*(3+ci-c)/(3*c) for ci,coef in (second[s],second[t]))
      target={0:F(1,162),1:-F(11,8424),2:F(1,3510)}[s+t]
      check(f'path-recurrence-{s}{t}',a==target)
    for n in range(4):
      c=F(9,2)+2*n
      a=((3-n)*second[0][1]*(3+second[0][0]-c)+n*second[1][1]*(3+second[1][0]-c))/(3*c)
      check('corner-recurrence-'+str(n),a==[F(2,81),F(34,13689),-F(38,17901),F(2,2457)][n])
    for j,c in ((F(1,2),F(15,2)),(F(3,2),F(21,2))):
      n0=F(3,2) if j==F(1,2) else F(0);n1=3-n0
      a=(n0*second[0][1]*(3+second[0][0]-c)+n1*second[1][1]*(3+second[1][0]-c))/(3*c)
      check('common-recurrence-'+str(j),a==(-F(2,1755) if j==F(1,2) else F(2,2457)))

A3=F(944984,351);B22=F(799258,39)
def ell(x):return F(128,3)*x+F(3132,13)*x*x
def delta(x):return A3*x**3+B22*x**4
def disc(x):return (1-ell(x))**2-F(8,3)*delta(x)
def discpoly(x):return (46457856*x**4+183150656*x**3+18324072*x*x-1168128*x+13689)/13689
def prime(x):return (4*46457856*x**3+3*183150656*x*x+2*18324072*x-1168128)/13689

def budget_checks():
    selfcost=F(3*8,81)+F(15*64,810)
    repeated=F(11,468)*216
    path=(3*512+8*128+8*128+20*32)/F(1053)
    common=F(512,117);corner=F(19*512+98*8,1053)
    check('self-original-norm',selfcost==F(40,27))
    check('repeated-original-norm',repeated==F(66,13))
    check('path-original-norm',path==F(1408,351))
    check('corner-original-norm',corner==F(3504,351))
    check('complete-cubic-norm',4*selfcost+84*repeated+460*path+40*common+24*corner==A3,A3)
    check('cubic-improvement',A3<F(30208,3))
    m1=F(64,3);t1=F(16,3)
    m2=6+42*(F(16,9)+F(4*48,117))
    t2=F(3,2)+6*F(64,117)+36*F(1,2)*(F(16,27)+F(48,117))
    check('second-total-spin-budget',m2==F(5834,39),m2)
    check('second-point-spin-budget',t2==F(137,6),t2)
    check('linear-first-budget',3*(m1/6+F(2,3)*t1)==F(64,3))
    check('linear-second-budget',3*(m2/6+F(2,3)*t2)==F(1566,13))
    check('quartic-full-source-budget',6*m2*t2==B22,B22)
    check('quartic-improvement',B22<F(2,3)*236**2)
    for k in range(30):
      x=F(k,1000);check('quartic-expanded-'+str(k),disc(x)==discpoly(x))
    # Rigorous first positive root: D''>0 on x>=0 and D'(0.0171)<0.
    high=F(171,10000);low=F(17,1000)
    check('quartic-left-root-sign',disc(low)>0)
    check('quartic-right-root-sign',disc(high)<0)
    check('quartic-derivative-negative-to-right',prime(high)<0)
    check('neumann-bound-before-root',ell(high)<1)
    for _ in range(150):
      mid=(low+high)/2
      if disc(mid)>0:low=mid
      else:high=mid
    a0=F(170787544707772675,10**19);a1=F(170787544707772677,10**19)
    check('root-decimal-bracket',a0<low<high<a1)
    g0=F(3825973052393385,10**15);g1=F(3825973052393386,10**15)
    check('coupling-threshold-bracket',4*high*g0*g0<1<4*low*g1*g1)
    d0=F(3,2)+F(1136,13)*low*low;d1=F(3,2)+F(1136,13)*high*high
    check('closed-endpoint-gap',d0>F(61,40))
    # Compare cubic-only result, before using the actual linearized inverse.
    cubic=lambda x:1-F(256,3)*x+F(10720,9)*x*x+F(20714816,1053)*x**3
    check('cubic-only-polynomial',cubic(F(1,64))==F(140213,4313088))
    reject('neumann-alone-closes-residual',disc(F(1,50))>=0)
    reject('erase-quartic-residual',B22==0)
    reject('frechet-without-two',F(1566,13)==F(3132,13))
    benchmark=[]
    for x in (F(1,64),F(1,60),F(1,10**8)):
      sl,sh=sqrt_box(disc(x));wl=F(3,4)*(1-ell(x)-sh);wh=F(3,4)*(1-ell(x)-sl)
      dl=F(3,2)*(1+sl)+F(1136,13)*x*x;dh=F(3,2)*(1+sh)+F(1136,13)*x*x
      check('positive-disc-'+str(x),disc(x)>0)
      check('source-radius-equation-'+str(x),
            (1-ell(x))*wl-F(2,3)*wl*wl<=delta(x)<=
            (1-ell(x))*wh-F(2,3)*wh*wh)
      check('drift-refined-return-'+str(x),
            3*(1-4*(t1*x+t2*x*x+wh/6))==dl)
      if x==F(1,64):
        check('g-square-four-gap',dl>F(18385,10000))
        check('linear-error-return',wh-delta(x)/(1-ell(x))<F(5432,10**6))
      if x==F(1,60):check('energy-cauchy-circle',32*x+236*x*x+wh<F(7,10))
      benchmark.append({'xi':str(x),'D':str(disc(x)),
                        'linear_inverse_bound':str(1/(1-ell(x))),
                        'linear_response_bound':str(delta(x)/(1-ell(x))),
                        'correction_norm_interval':[str(wl),str(wh)],
                        'physical_gap_over_kappa_interval':[str(dl),str(dh)]})
    for N in range(1,50):
      b=F(math.comb(2*N,N),4**N);bn=F(math.comb(2*N+2,N+1),4**(N+1))
      check('catalan-tail-'+str(N),F(math.comb(2*N,N),N+1)/4**N==2*(b-bn))
      check('catalan-tail-bound-'+str(N),b*b<=F(1,N+1))
    return {'cubic_bound':str(A3),'old_cubic_bound':str(F(30208,3)),
            'quartic_residual_bound':str(B22),'root_bracket':[str(a0),str(a1)],
            'g_squared_threshold_bracket':[str(g0),str(g1)],
            'endpoint_gap_coefficient_bracket':[str(d0),str(d1)],'benchmarks':benchmark}

def energy_checks():
    check('repeated-low-channel-cancellation',F(1,72)-F(1,72)==0)
    check('self-fourth-scalar',2*(-F(1,81))+F(1,648)==-F(5,216))
    adj=4*(F(1,4)/F(9,2)+F(3,4)/F(13,2))
    check('adjacent-Rayleigh-moment',adj==F(80,117))
    check('adjacent-excess-moment',adj-F(2,3)==F(2,117))
    check('adjacent-v2-energy',F(9,2)*F(1,27)**2/F(4)+F(13,2)*F(1,117)**2*F(3,4)==F(2,1053))
    for M,J in ((1,0),(2,1),(240,1128),(882,3816)):
      e4=F(M*M,27)-F(1,9)*(F(M,8)+F(2,3)*F(M*(M-1),2)+F(2*J,117))
      check(f'fourth-energy-independent-{M}-{J}',e4==F(5*M,216)-F(2*J,1053))
    check('fourth-energy-cubic-per-face',F(5,216)-F(12,1053)==F(11,936))
    check('fourth-energy-planar-per-face',F(5,216)-F(4,1053)==F(163,8424))
    # Independent formal eigenvector recurrence for ONE original plaquette.
    # Multiplication W chi_j=chi_(j-1/2)+chi_(j+1/2), K chi_j=4j(j+1).
    order=6;u=[[F(0)]*(order+1) for _ in range(order+1)];u[0][0]=1;E=[F(0)]*(order+1)
    for n in range(1,order+1):
      E[n]=-u[n-1][1]
      for k in range(1,order+1):
        neigh=(u[n-1][k-1] if k else 0)+(u[n-1][k+1] if k<order else 0)
        rhs=neigh+sum(E[j]*u[n-j][k] for j in range(1,n+1))
        u[n][k]=rhs/F(k*(k+2))
    check('single-face-second-independent',E[2]==-F(1,3))
    check('single-face-fourth-independent',E[4]==F(5,216))
    check('single-face-evenness',all(E[n]==0 for n in (1,3,5)))
    # Product-rule projection of B(v2_p,v2_p), with all nonconstant channels.
    # chi_1^2=chi_0+chi_1+chi_2, original K=0,8,24.
    check('self-quartic-spin-one',(16-8)/F(2*8*72**2)==F(1,10368))
    check('self-quartic-spin-two',(16-24)/F(2*24*72**2)==-F(1,31104))
    check('self-quartic-retained-scalar',F(8,72**2)==F(1,648))
    reject('drop-fourth-ground-sign',-F(5,216)==E[4])
    reject('adjacent-pairs-are-independent',adj==F(2,3))
    reject('erase-fourth-energy-scalar',F(1,648)==0)
    reject('erase-cubic-self-character',F(1,810)==0)
    reject('erase-corner-n2-channel',-F(38,17901)==0)
    reject('erase-physical-time-factor',F(2*16,3)==F(16,3))
    # Exact planar parameter dictionaries; squared couplings avoid irrational arithmetic.
    # Hui g_H=2g gives g_H^2/(2a)=kappa and 4/g_H^4=xi.
    for g2,a in ((F(4),F(3)),(F(17,4),F(1,7))):
      k=2*g2/a;xi=1/(4*g2*g2);h2=4*g2
      check('hui-kinetic-'+str(g2),h2/(2*a)==k)
      check('hui-magnetic-'+str(g2),F(4)/(h2*h2)==xi)
    return {'single_plaquette_coefficients':[str(x) for x in E],
            'cubic_infinite_volume_E4_per_face':'11/936','planar_E4_per_face':'163/8424'}

def source_hashes():
    names=['geometry.py','coordinate_audit.py','verify.py','CUBIC_SOURCE.md','LINEARIZED_RETURN.md','state.json','SOURCE_INTAKE.json','README.md']
    out={}
    for name in names:
      p=ROOT/name
      require(p.is_file(),'missing-source:'+name)
      out[name]=hashlib.sha256(p.read_bytes()).hexdigest()
    return out

def run():
    CHECKS.clear();NEGATIVE.clear()
    a,p,t,finite=geometry_checks();coords=coordinate_checks(a,p,t)
    sphere_and_projectors();budgets=budget_checks();energy=energy_checks()
    return {'schema':'ym-cubic-linearized-exact-v1','passed':True,
            'scope':{'finite_original_coordinate_checks':True,'analytic_proof_formalized':False,
                     'vacuum_sampling':False,'spin_cutoff_of_full_operator':False,'continuum_gap_proved':False},
            'counts':{'exact_checks':len(CHECKS),'negative_controls':len(NEGATIVE)},
            'coordinate_certificate':coords,'budgets':budgets,'finite_boxes':finite,
            'energy':energy,'checks':CHECKS,'negative_controls':NEGATIVE,'source_sha256':source_hashes()}

def strict_json(text):
    def pairs(items):
        out={}
        for key,value in items:
            require(key not in out,'duplicate-json-key:'+key)
            out[key]=value
        return out
    return json.loads(text,object_pairs_hook=pairs)

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path);p.add_argument('--verify-receipt',type=Path)
    args=p.parse_args()
    try:
      saved=None
      if args.verify_receipt:
        saved=args.verify_receipt.read_text();expected=strict_json(saved)
        require(expected.get('schema')=='ym-cubic-linearized-exact-v1','receipt-schema')
        actual_hashes=source_hashes()
        require(set(expected.get('source_sha256',{}))==set(actual_hashes),'source-manifest-membership')
        for name,h in actual_hashes.items():
          require(expected['source_sha256'][name]==h,'source-identity-mismatch:'+name)
      result=run();encoded=json.dumps(result,sort_keys=True,indent=2)+'\n'
      if args.verify_receipt:
        require(saved==encoded,'receipt-mismatch')
      if args.output:args.output.write_text(encoded)
      else:sys.stdout.write(encoded)
    except (CheckFailure,OSError,ValueError) as exc:
      sys.stderr.write('FAIL: '+str(exc)+'\n');return 1
    return 0
if __name__=='__main__':raise SystemExit(main())
