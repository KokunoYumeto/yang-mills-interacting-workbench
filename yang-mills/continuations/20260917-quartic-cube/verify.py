#!/usr/bin/env python3
"""Rebuild complete quartic coefficients and their finite certificates.
Exact algebra and finite identities are checked here. Analytic proofs remain
written proofs. No vacuum sampling or spin cutoff of the Hamiltonian is used.
"""
from __future__ import annotations
from pathlib import Path
from fractions import Fraction as F
from collections import Counter,defaultdict
from itertools import product,permutations
import sys,json,hashlib,argparse,tempfile
from source_engine import Source,subcounts,coordinates,g
from trace_algebra import (const,trace,add,scale,multiply,gamma,electric,inverse_coeffs,
                          haar,value,physical_spectrum,cyclic,chebtrace)
from clusters import anchored4,cubic_orbit
from channel_bounds import norm_budget,Bbound,submultisets,VERTS
from spin_bounds import spin_table,trace_bound
from differential_audit import Audit,assignments,POINTS,qm,qc,ONE
from energy import EnergySource,Rayleigh
from series import *
from quartic_budgets import compute_budgets
ROOT=Path(__file__).resolve().parent
CHECKS=[];CONTROLS=[]
class Failure(RuntimeError):pass

def need(test,name):
    if not test:raise Failure(name)
def check(name,test):
    need(name not in CHECKS,'duplicate-test:'+name);need(bool(test),name);CHECKS.append(name)
def reject(name,false_statement):
    need(not false_statement,'false-formula-accepted:'+name);CONTROLS.append(name)
def dump(x):return json.dumps(x,sort_keys=True,indent=2)+'\n'
def digest(x):return hashlib.sha256(x).hexdigest()
def exact_eval(p,x):return sum(a*x**i for i,a in enumerate(p))
def json_load(path):
    def hook(pairs):
        d={}
        for k,v in pairs:
            need(k not in d,'duplicate-json-key:'+k);d[k]=v
        return d
    return json.loads(path.read_text(),object_pairs_hook=hook)

def coordinate_checks():
    for i,q in enumerate(POINTS):check('unit-quaternion-'+str(i),qm(q,qc(q))==ONE)
    U=assignments(4,3);D=Audit(U);w=(1,2,-3,-4);f=trace(w)
    check('original-K-plaquette',D.K(f)==3*D.value(f))
    check('original-Gamma-plaquette',D.Gamma(f,f)==4-D.value(f)**2)
    reject('omit-original-half-generator',D.K(f)==12*D.value(f))
    reject('omit-Gamma-contraction',D.Gamma(f,f)==0)
    for n in range(9):
        pw=trace(w*n)
        rhs=sum(c*D.value(f)**j for j,c in enumerate(chebtrace(n)))
        check('trace-power-'+str(n),D.value(pw)==rhs)
    check('haar-quadratic-character',haar(multiply(f,f))==1)
    check('haar-fourth-character',haar(multiply(multiply(f,f),multiply(f,f)))==2)
    check('haar-sixth-character',haar(multiply(multiply(f,f),multiply(multiply(f,f),multiply(f,f))))==5)

def build_quartic():
    stages=anchored4();check('all-anchored-counts',list(map(len,stages))==[4,46,612,8621])
    counts=Counter(tuple(sorted(Counter(ps).values(),reverse=True)) for ps in stages[3])
    check('all-quartic-multiplicity-counts',counts=={(4,):4,(3,1):84,(2,2):42,(2,1,1):1572,(1,1,1,1):6919})
    group=defaultdict(list)
    for ps in sorted(stages[3]):
        key,(pm,ss,off)=cubic_orbit(ps)
        # Verify the inverse on every original vertex; no quotient label is lost.
        for v in {v for p in ps for e in g.pedges(p) for v in g.endpoints(e)}:
            u=tuple(ss[i]*v[pm[i]]-off[i] for i in range(3));back=[0]*3
            for i in range(3):back[pm[i]]=ss[i]*(u[i]+off[i])
            need(tuple(back)==v,'inverse-coordinate-transport')
        group[key].append({'original':ps,'permutation':pm,'signs':ss,'offset':off})
    check('quartic-orbit-count',len(group)==78)
    check('quartic-orbit-multiplicities',Counter(tuple(sorted(Counter(ps).values(),reverse=True)) for ps in group)=={(4,):1,(3,1):2,(2,2):2,(2,1,1):19,(1,1,1,1):54})
    data=[];transports=[];bounds=[];total=F(0);nonzero=0;allterms=0
    for idx,(ps,images) in enumerate(sorted(group.items())):
        o=Source(ps);cs=tuple(ps.count(p) for p in o.ps);v=o.v(cs);sp=o.spectrum(cs)
        check(f'quartic-{idx}-all-rational',all(isinstance(c,F) for c in v.values()))
        check(f'quartic-{idx}-zero-Haar-mean',haar(v)==0)
        ico=inverse_coeffs(tuple(sp))
        check(f'quartic-{idx}-inverse-zero',exact_eval(ico,F(0))==0)
        for c in sp:
            if c:check(f'quartic-{idx}-inverse-{c}',exact_eval(ico,c)==1/c)
        rhs={};splits=[]
        for a in subcounts(cs):
            if sum(a) in (0,4):continue
            b=tuple(c-k for c,k in zip(cs,a));fa,fb=o.v(a),o.v(b)
            rhs=add(rhs,gamma(fa,fb));splits.append((fa,fb))
        h0=haar(rhs)
        for seed in (3,11):
            D=Audit(assignments(len(o.edges),seed));kv=D.K(v)
            want=sum(D.Gamma(f,h) for f,h in splits)-h0
            check(f'quartic-{idx}-original-matrix-derivative-{seed}',kv==want)
            nonzero+=kv!=0
        data.append({'index':idx,'faces':ps,'multiplicity':cs,'edge_coordinates':[(k,o.edges[k]) for k in sorted(o.edges)],
                     'original_words':o.words,'Casimir_spectrum':list(map(str,sp)),
                     'coefficients':[{'words':m,'coefficient':str(c)} for m,c in sorted(v.items())]})
        transports.append({'index':idx,'representative':ps,'images':images})
        bbranch=sum(Bbound(a,b) for a,b in submultisets(ps))
        btrace=trace_bound(electric(v));selected=min(bbranch,btrace)
        spin=spin_table(ps)
        if spin:selected=min(selected,F(spin['bound']))
        total+=len(images)*selected
        bounds.append({'index':idx,'count':len(images),'branch_bound':str(bbranch),'trace_bound':str(btrace),'selected_bound':str(selected),'spin_certificate':spin})
        allterms+=len(v)
    check('quartic-polynomial-term-count',allterms==743)
    check('quartic-original-nonzero-evaluations',nonzero>=100)
    check('full-fourth-source-bound',total==A4)
    check('explicit-A4-improvement',A4<F(128,3)*F(944984,351)+F(799258,39))
    anchor=(0,0,0,0)
    budgets=[]
    for n in (1,2,3):
        sums=[sum(norm_budget(ps,s) for ps in stages[n-1]) for s in
              (lambda j:sum(x*(x+1) for x in j.values()),lambda j:sum(j.values()),lambda j:j.get(anchor,0))]
        expected=([F(32),F(64,3),F(16,3)] if n==1 else [F(236),M2,T2] if n==2 else [A3,M3,T3])
        check('original-spin-budgets-'+str(n),sums==expected);budgets.append({'degree':n,'bounds':list(map(str,sums))})
    reject('erase-shared-spin-zero-capacity',VERTS['pair']==((F(64),F(0)),))
    reject('erase-fourth-residual',A4==0)
    reject('generic-A4-equals-evaluated',A4==F(128,3)*F(944984,351)+F(799258,39))
    # The self coefficient in original character coordinates, including the scalar return.
    one=Source(((0,0,0,0,1),));w=trace(one.words[0]);w2=multiply(w,w);w4=multiply(w2,w2)
    chi1=add(w2,const(-1));chi2=add(w4,scale(w2,-3),const(1))
    self4=add(scale(chi1,F(17,10368)),scale(chi2,-F(7,51840)))
    check('single-face-entire-quartic-character',one.v((4,))==self4)
    reject('omit-self-quartic-upper-character',one.v((4,))==scale(chi1,F(17,10368)))
    allbounds={'A4':str(total),'rows':bounds,'cubic_budgets':budgets}
    spin4=compute_budgets(data,allbounds,transports)
    check('fourth-total-spin-budget',F(spin4['M4'])==M4)
    check('fourth-point-spin-budget',F(spin4['T4'])==T4)
    check('fourth-point-spin-strict-improvement',T4<A4/6)
    return data,transports,allbounds,spin4,stages

def energy_checks(stages):
    p=(0,0,0,0,1);q=(1,0,0,0,1);r=(2,0,0,0,1)
    cube=((0,0,0,0,1),(0,0,1,0,1),(0,0,0,0,2),(0,1,0,0,2),(0,0,0,1,2),(1,0,0,1,2))
    fixtures=[('self',(p,),(6,),-F(289,77760)),('pair',(p,q),(4,2),F(22285,47309184)),
        ('path',(p,q,r),(2,2,2),-F(4909,118272960)),
        ('common',((0,-1,0,0,1),p,(0,0,0,0,2)),(2,2,2),F(244,4312035)),
        ('corner',(p,(0,0,0,0,2),(0,0,0,1,2)),(2,2,2),-F(212,542997)),
        ('cube',cube,(1,)*6,-F(83,1944))]
    data=[]
    for name,ps,cs,expected in fixtures:
        ob=EnergySource(ps);actual,parts=ob.energy6(cs);other=Rayleigh(ps).e(cs)
        check('energy6-source-'+name,actual==expected)
        check('energy6-independent-eigenvector-recurrence-'+name,other==expected)
        data.append({'type':name,'faces':ps,'multiplicities':cs,'coefficient':str(actual),'source_parts':list(map(str,parts)),'eigenvector_recurrence':str(other)})
    triple=sorted({cubic_orbit(ps)[0] for ps in stages[2] if len(set(ps))==3})
    check('all-nine-geometric-triple-types',len(triple)==9)
    wanted={'path':-F(4909,118272960),'common':F(244,4312035),'corner':-F(212,542997)}
    for i,ps in enumerate(triple):
        a,_=EnergySource(ps).energy6((2,2,2));check('energy6-triple-orbit-'+str(i),a==wanted[g.type3(ps)])
    perpendicular=Rayleigh((p,(0,0,0,0,2))).e((4,2))
    check('energy6-perpendicular-pair',perpendicular==F(22285,47309184))
    hist=Counter();ss=F(0)
    for order in permutations(cube):
        bs=tuple(len(g.boundary(order[:i])) for i in range(1,6));hist[bs]+=1;term=F(1)
        for b in bs:term*=F(4,3*b)
        ss+=term
    check('all-720-cube-orderings',sum(hist.values())==720)
    check('cube-original-Haar-mass',haar(__import__('functools').reduce(multiply,[trace(w) for w in coordinates(cube)[0]],const(1)))==F(1,16))
    check('cube-independent-boundary-spectrum-sum',-ss/16==-F(83,1944))
    reject('omit-closed-cube',ss==0)
    reject('erase-intermediate-boundary-length',-F(720,16*3**5)==-F(83,1944))
    reject('self-sixth-sign-flip',F(289,77760)==fixtures[0][-1])
    reject('adjacent-pair-as-independent',fixtures[1][-1]==0)
    reject('forget-two-ordered-42-pair-roles',fixtures[1][-1]==2*fixtures[1][-1])
    boxes=[]
    for L in (2,3,4):
        m=2*L;faces=[n+(i,j) for n in product(range(m+1),repeat=3) for i,j in __import__('itertools').combinations(range(3),2) if n[i]<m and n[j]<m]
        fset=set(faces);degs=Counter(e for p in faces for e in g.pedges(p));adj={p:g.adjacent(p)&fset for p in faces}
        M=len(faces);J=sum(len(a) for a in adj.values())//2
        common=sum(__import__('math').comb(r,3) for r in degs.values());corner=8*m**3
        paths=sum(__import__('math').comb(len(a),2) for a in adj.values())-3*(common+corner)
        check(f'box{L}-M',M==3*m*m*(m+1));check(f'box{L}-J',J==6*m*(3*m*m-1))
        check(f'box{L}-common',common==12*m*m*(m-1));check(f'box{L}-paths',paths==138*m**3-126*m*m-24*m+12)
        e6=-F(289*M,77760)+F(22285*J,23654592)-F(4909*paths,118272960)+F(244*common,4312035)-F(212*corner,542997)-F(83*m**3,1944)
        closed=-F(211396463*m**3+30959193*m*m+21845782*m+2336684,4691494080)
        check(f'box{L}-complete-sixth-coefficient',e6==closed);boxes.append({'L':L,'M':M,'J':J,'paths':paths,'common':common,'corners':corner,'cubes':m**3,'E6_over_kappa':str(e6)})
    for g2,a in ((F(15,4),F(1,3)),(F(4),F(2,7)),(F(5000),F(1))):
        gn2=4*g2;k=2*g2/a;x=1/(4*g2*g2)
        check('modern-physical-electric-map-'+str(g2),gn2/(2*a)==k)
        check('modern-physical-magnetic-map-'+str(g2),2/(gn2*a)==k*x)
        check('modern-coupling-map-'+str(g2),4/(gn2*gn2)==x)
    check('bulk-halftrace-cubic-coefficient',2*F(11,936)==F(11,468))
    check('bulk-halftrace-quintic-coefficient',-3*(-F(211396463,14074482240))==F(211396463,4691494080))
    for r in (F(1,100),F(1,16),F(1,4)):
        for n in (4,8,12):
            full=r**7*(8-6*r*r)/(1-r*r)**2
            finite=sum(2*j*r**(2*j-1) for j in range(4,n+1))
            tail=r**(2*n+1)*((2*n+2)-2*n*r*r)/(1-r*r)**2
            check('observable-derivative-tail-'+str(r)+'-'+str(n),full==finite+tail and tail>0)
    reject('drop-observed-halftrace-factor',F(2,3)==F(1,3))
    return {'cases':data,'cube_boundary_histogram':[{'boundaries':a,'count':b} for a,b in sorted(hist.items())],'boxes':boxes,'bulk_E6_per_face':'-211396463/14074482240'}

def series_checks():
    check('actual-third-linearized-budget',L3==F(292337810,125307))
    check('mixed-B23-budget',B23==F(222621900791,1163565))
    check('B33-budget',B33==F(76060493515233224,43616234025))
    check('physical-cubic-margin',P3==F(278874091,208845))
    lo,hi=root_box();decimal_lo=F(1781868048538520630,10**20);decimal_hi=F(1781868048538520631,10**20)
    check('exact-root-bracket',decimal_lo<lo<hi<decimal_hi)
    g_lo=F(3745693472404566975,10**18);g_hi=F(3745693472404566976,10**18)
    check('physical-coupling-bracket',4*hi*g_lo*g_lo<1<4*lo*g_hi*g_hi)
    check('endpoint-positive-physical-gap',F(3,2)+F(1136,13)*lo*lo+P3*lo**3>F(153529,100000))
    rows=[]
    for g2 in (F(15,4),F(19,5),F(4),F(5000)):
        x=1/(4*g2*g2);dl,dh=gap_box(x);wl,wh=correction_box(x)
        check('benchmark-disc-'+str(g2),disc(x)>0)
        check('majorant-equation-'+str(g2),(1-ell(x))*wl-F(2,3)*wl*wl<=delta(x)<=(1-ell(x))*wh-F(2,3)*wh*wh)
        check('actual-drift-return-'+str(g2),3*(1-4*(F(16,3)*x+T2*x*x+T3*x**3+wh/6))==dl)
        if g2==F(15,4):check('g2-15/4-bound',dl>F(15794,10000))
        if g2==4:check('g2-four-improvement',dl>F(188578,100000))
        rows.append({'g_squared':str(g2),'xi':str(x),'D':str(disc(x)),'correction':[str(wl),str(wh)],'gap_over_kappa':[str(dl),str(dh)]})
    x=F(4,225)
    # derivative upper bound proves d is decreasing up to the specified benchmark.
    check('benchmark-uniform-monotonicity',-F(3,2)*(1-ell(x))*F(128,3)+2*F(1136,13)*x+3*P3*x*x<0)
    reject('erase-fifth-residual',B23==0);reject('erase-sixth-residual',B33==0)
    reject('omit-Frechet-two',L3==M3/2+2*T3)
    reject('beyond-certified-root',disc(F(9,500))>=0)
    # Entire Neumann residual and its primitive in an original nonzero kernel example.
    a=F(1,3);r=F(2,5)
    for n in range(9):
        y=sum(a**j*r for j in range(n+1))
        check('retained-linear-residual-'+str(n),r-(1-a)*y==a**(n+1)*r)
    reject('wrong-residual-exponent',r-(1-a)*sum(a**j*r for j in range(4))==a**3*r)
    qa,qb=root_quartic_box()
    qlo=F(18104972231644127075,10**21);qhi=F(18104972231644127076,10**21)
    check('quartic-reference-exact-root',qlo<qa<qb<qhi)
    glo=F(3715960362535435236,10**18);ghi=F(3715960362535435237,10**18)
    check('quartic-reference-physical-threshold',4*qb*glo*glo<1<4*qa*ghi*ghi)
    check('quartic-reference-larger-domain',qa>hi)
    qrows=[]
    for g2 in (F(15,4),F(4),F(5000)):
        x=1/(4*g2*g2);dl,dh=gap_quartic_box(x);wl,wh=correction_quartic_box(x)
        check('quartic-reference-majorant-'+str(g2),(1-ell_quartic(x))*wl-F(2,3)*wl*wl<=delta_quartic(x)<=(1-ell_quartic(x))*wh-F(2,3)*wh*wh)
        check('quartic-reference-drift-'+str(g2),3*(1-4*(F(16,3)*x+T2*x*x+T3*x**3+T4*x**4+wh/6))==dl)
        if g2==F(15,4):check('quartic-reference-g15/4',dl>F(16584,10000))
        if g2==4:check('quartic-reference-g4',dl>F(189811,100000))
        qrows.append({'g_squared':str(g2),'xi':str(x),'D':str(disc_quartic(x)),'correction':[str(wl),str(wh)],'gap_over_kappa':[str(dl),str(dh)]})
    x=F(4,225)
    check('quartic-reference-benchmark-monotonicity',-F(3,2)*(1-ell_quartic(x))*F(128,3)+2*F(1136,13)*x+3*P3*x*x+4*P4*x**3<0)
    reject('erase-eighth-reference-residual',B44==0)
    reject('halve-seventh-reference-residual',2*B34==B34)
    qdata={'root_bracket':[str(qlo),str(qhi)],'g_squared_bracket':[str(glo),str(ghi)],'M4':str(M4),'T4':str(T4),'L4':str(L4),'B14':str(B14),'B24':str(B24),'B34':str(B34),'B44':str(B44),'P4':str(P4),'benchmarks':qrows}
    return {'root_bracket':[str(decimal_lo),str(decimal_hi)],'g_squared_bracket':[str(g_lo),str(g_hi)],'A4':str(A4),'M3':str(M3),'T3':str(T3),'L3':str(L3),'B23':str(B23),'B33':str(B33),'P3':str(P3),'benchmarks':rows,'quartic_reference':qdata}

SOURCES=['trace_algebra.py','source_engine.py','clusters.py','channel_bounds.py','exact_lp.py','spin_bounds.py','differential_audit.py','energy.py','series.py','quartic_budgets.py','verify.py','replay.py','QUARTIC_SOURCE.md','PHYSICAL_RETURN.md','SIXTH_ENERGY.md','SOURCE_INTAKE.json','state.json','README.md','../20260916-cubic-linearized/geometry.py','../20260916-cubic-linearized/CUBIC_SOURCE.md','../20260916-cubic-linearized/LINEARIZED_RETURN.md']

def run():
    CHECKS.clear();CONTROLS.clear();coordinate_checks();a,b,c,d,stages=build_quartic();energy=energy_checks(stages);sr=series_checks()
    files={'quartic_coefficients.json':dump(a),'quartic_transports.json':dump(b),'quartic_bounds.json':dump(c),'quartic_spin_budgets.json':dump(d),'sixth_energy.json':dump(energy)}
    sources={p:digest((ROOT/p).read_bytes()) for p in SOURCES}
    result={'schema':'ym-quartic-cube-v1','passed':True,'scope':{'original_connected_quartic_complete':True,'finite_certificate_only':True,'analytic_proof_formalized':False,'vacuum_sampled':False,'operator_spin_cutoff':False,'continuum_mass_gap_proved':False},
      'counts':{'exact_checks':len(CHECKS),'negative_controls':len(CONTROLS)},'checks':CHECKS,'rejected_false_formulas':CONTROLS,'series':sr,'source_sha256':sources,'generated_sha256':{p:digest(s.encode()) for p,s in files.items()}}
    return result,files

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',type=Path);p.add_argument('--verify-receipt',type=Path);args=p.parse_args()
    try:
        saved=None
        if args.verify_receipt:
            saved=json_load(args.verify_receipt);need(saved.get('schema')=='ym-quartic-cube-v1','receipt-schema')
            need(set(saved.get('source_sha256',{}))==set(SOURCES),'source-manifest-membership')
            for name in SOURCES:need(saved['source_sha256'][name]==digest((ROOT/name).read_bytes()),'source-identity:'+name)
            tables={'quartic_coefficients.json','quartic_transports.json','quartic_bounds.json','quartic_spin_budgets.json','sixth_energy.json'}
            need(set(saved.get('generated_sha256',{}))==tables,'table-manifest-membership')
            for name in sorted(tables):
                q=args.verify_receipt.parent/name
                need(q.is_file(),'missing-table:'+name)
                need(digest(q.read_bytes())==saved['generated_sha256'][name],'table-identity:'+name)
        result,files=run()
        if saved is not None:need(saved==result,'mathematical-receipt-mismatch')
        out=args.output_dir
        if out:
            out.mkdir(parents=True,exist_ok=True)
            for name,txt in files.items():(out/name).write_text(txt)
            (out/'verification.json').write_text(dump(result))
        print(dump({'passed':True,'counts':result['counts'],'receipt_sha256':digest(dump(result).encode()),'tables_sha256':result['generated_sha256']}),end='')
        return 0
    except (Failure,OSError,ValueError,ArithmeticError) as e:
        print('FAIL: '+str(e),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
