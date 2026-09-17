#!/usr/bin/env python3
"""Rebuild finite exact coefficients, original-link tests and complete receipts.

Uses standard-library rational arithmetic. Written analytic proofs are not
machine-formalized, and earlier continuum/gap claims are not recertified.
"""
from __future__ import annotations
import argparse,ast,hashlib,json,math,sys
from collections import Counter
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'calculations'),str(ROOT/'recovered')]
from gauge_polynomial import Cluster,Ring,left_right_terms
from quartic_catalogue import enumerate_classes
from build_quartic import compute
from original_link_audit import check_one
from sixth_energy import WEIGHTS,cube_data,coefficients,counts,enumerate_box,small_cluster_energy6
from audit_inherited import ell,discriminant,polynomial
from geometry import pedges,type3
from reconstruct import transformed_multiset,transform_edge

class Failure(RuntimeError):pass
CHECKS=[];NEGATIVE=[]
def require(test,name):
    if not test:raise Failure(name)
def check(name,test,value=None):
    require(name not in {x['name'] for x in CHECKS},'duplicate-check-name:'+name)
    require(bool(test),name);row={'name':name,'passed':True}
    if value is not None:row['value']=str(value)
    CHECKS.append(row)
def rejected(name,false_formula):
    require(not bool(false_formula),'false-formula-accepted:'+name)
    NEGATIVE.append({'name':name,'false_formula_accepted':False})
def no_duplicates(pairs):
    d={}
    for k,v in pairs:require(k not in d,'duplicate-json-key:'+k);d[k]=v
    return d
def load(p):return json.loads(p.read_text(),object_pairs_hook=no_duplicates)
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git_blob(p):
    b=p.read_bytes();return hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest()
def source_files():
    paths=[ROOT/'input/Pasted markdown(6).md',ROOT/'recovered/geometry.py',Path(__file__),ROOT/'proofs/FOURTH_ORDER_SOURCE.md',ROOT/'proofs/SIXTH_ORDER_ENERGY.md']
    paths+=sorted((ROOT/'calculations').glob('*.py'))
    return {str(p.relative_to(ROOT)):digest(p) for p in paths}

def independent_character():
    degree=8;u=[[Q(0)]*(degree+1) for _ in range(degree+1)];u[0][0]=1;e=[Q(0)]*(degree+1)
    for n in range(1,degree+1):
        e[n]=-u[n-1][1]
        for k in range(1,degree+1):
            src=u[n-1][k-1]+(u[n-1][k+1] if k<degree else 0)
            src+=sum(e[j]*u[n-j][k] for j in range(1,n+1))
            u[n][k]=src/Q(k*(k+2))
    published={2:-Q(1,12),4:Q(5,13824),6:-Q(289,79626240),8:Q(21391,458647142400)}
    for n,a in published.items():check('Mathieu-original-parameter-return-'+str(n),e[n]==a*Q(-4)**n/4,e[n])
    check('one-face-original-center-parity',all(e[n]==0 for n in (1,3,5,7)))
    return [str(x) for x in e]

def full_box_from_vector_data(L):
    x=counts(L);M=x['M'];J=x['J'];m=2*L;dc=Counter()
    for boundary,numplanes in [(True,2),(False,m-1)]:
        for b,num in [(0,(m-2)**2),(1,4*(m-2)),(2,4)]:dc[(8 if boundary else 12)-b]+=3*numplanes*num
    require(sum(dc.values())==M,'degree-total')
    norm2=Q(M,576)+(Q(M*(M-1),2)-J)/81+J*Q(1648,123201)
    norm3=3*sum(num*(-Q(5,216)+Q(d,1053))**2 for d,num in dc.items())+Q(M,8640)
    norm3+=(M*(M-1)-2*J)*Q(11,5184)+2*J*Q(110453,47309184)
    n1=J*(M-2)-2*x['path']-3*(x['common']+x['corner'])
    n0=math.comb(M,3)-n1-x['path']-x['common']-x['corner']
    norm3+=Q(n0,81)+n1*Q(4768,369603)+x['path']*Q(1595629,118272960)
    norm3+=x['common']*Q(20032,1437345)+x['corner']*Q(210880,14660919)+x['cube']*Q(83,1944)
    e2=-Q(M,3);e4=Q(5*M,216)-Q(2*J,1053)
    return -norm3-e4*Q(M,9)-e2*norm2

def main_checks(progress=False):
    check('restored-geometry-original-Git-blob',git_blob(ROOT/'recovered/geometry.py')=='c8d385b276909ea1e885747c42773e64e9553c87')
    ast.parse((ROOT/'recovered/geometry.py').read_text());check('restored-geometry-parses',True)
    stats,orbits=enumerate_classes(4);expected=load(ROOT/'results/quartic_geometric_classes.json')
    regenerated={'anchored_counts_by_order':stats,'class_count':len(orbits),'classes':[{'faces_with_multiplicity':[list(p) for p in key],'anchored_multiplicity':len(v),'partition':sorted(Counter(key).values(),reverse=True)} for key,v in sorted(orbits.items())]}
    check('full-geometry-catalogue-exact',regenerated==expected)
    check('all-anchored-orders',stats==[4,46,612,8621]);check('all-quartic-orbits',len(orbits)==78)
    check('all-partition-types',Counter(tuple(e['partition']) for e in expected['classes'])=={(4,):1,(3,1):2,(2,2):2,(2,1,1):19,(1,1,1,1):54})
    terms=0;downsets=0;chord_counts=Counter();jets=[];certificate_hashes={}
    for i,entry in enumerate(expected['classes']):
        fresh,_=compute(i,entry);stored=load(ROOT/f'results/quartic_coefficients/class_{i:02d}.json')
        check(f'quartic-complete-rebuilt-coefficient-{i:02d}',fresh==stored)
        check(f'quartic-mean-zero-{i:02d}',fresh['coefficient_Haar_mean']=='0');check(f'quartic-nonzero-{i:02d}',fresh['nonzero'])
        c=Cluster(tuple(tuple(p) for p in stored['model']['faces']));R=c.ring
        f={tuple(t['powers']):Q(t['coefficient']) for t in stored['coefficient_polynomial']}
        for a in range(3):
            field=[]
            for j in range(R.m):
                field+=left_right_terms(j,a);field +=[(p,q,-t) for p,q,t in left_right_terms(j,a,True)]
            check(f'quartic-exact-physical-conjugation-{i:02d}-{a}',not R.linear_field(f,field))
        jet=check_one(i);jets.append(jet)
        check(f'original-link-kinetic-and-gauge-return-{i:02d}',jet['K_from_original_edge_jets']==jet['K_from_returned_polynomial_fields'] and jet['original_value']==jet['value_after_original_vertex_gauge_map'])
        terms+=len(f);downsets+=fresh['symbolic_certificate']['downset_coefficients'];chord_counts[R.m]+=1
        certificate_hashes[f'class_{i:02d}.json']=digest(ROOT/f'results/quartic_coefficients/class_{i:02d}.json')
        if i==0:
            F=c.W[0];F2=R.mul(F,F);chi1=R.add(F2,R.const(-1));chi2=R.add(R.mul(F2,F2),R.scale(-3,F2),R.const(1))
            self4=R.add(R.scale(Q(17,10368),chi1),R.scale(-Q(7,51840),chi2));check('complete-self-quartic-character-formula',f==self4)
            b22=R.add(R.scale(Q(1,10368),chi1),R.scale(-Q(1,31104),chi2));rejected('quartic-residual-b22-is-full-v4',b22==f)
            check('missing-two-B-v1-v3-exact',R.add(f,R.scale(-1,b22))==R.add(R.scale(Q(1,648),chi1),R.scale(-Q(1,9720),chi2)))
            failed=False
            try:c.inv(f,counts=(2,))
            except ArithmeticError:failed=True
            check('incomplete-spin-list-rejected-by-polynomial-residual',failed)
        if i==1:
            only=[]
            for j in range(R.m):
                for a in range(3):
                    fld=left_right_terms(j,a);only.append(R.linear_field(R.linear_field(f,fld),fld))
            rejected('erase-original-tree-edge-kinetic-terms',R.scale(-1,R.add(*only))==c.K(f))
        if i==25:
            check('annular-four-face-cluster-keeps-five-chords',len(c.faces)==4 and R.m==5);rejected('one-chord-per-face-assumption',R.m==len(c.faces))
        if progress:print(f'quartic {i:02d} exact polynomial and original-link audit passed',file=sys.stderr,flush=True)
    check('entire-quartic-monomial-count',terms==4044,terms);check('entire-recomputed-downset-count',downsets==1053,downsets)
    check('original-link-jet-receipt-exact',jets==load(ROOT/'results/original_link_jet_audit.json'))
    check('all-8621-assigned-once',sum(len(x) for x in orbits.values())==8621)
    transport=load(ROOT/'results/anchored_quartic_transports.json');seen=set()
    for row in transport['rows']:
        fs=tuple(tuple(p) for p in row['original_face_multiset']);i=row['class_index'];image,shift=transformed_multiset(fs,row['transform_index'])
        require(fs not in seen,'duplicate-transported-source');seen.add(fs)
        require(image==tuple(tuple(p) for p in expected['classes'][i]['faces_with_multiplicity']) and list(shift)==row['subtracted_translation'],'wrong-source-transport')
        for edge in set().union(*(pedges(p) for p in fs)):
            mapped,sign=transform_edge(edge,row['coordinate_permutation'],row['coordinate_signs'],row['subtracted_translation'])
            require(sign in (-1,1) and mapped in set().union(*(pedges(p) for p in image)),'wrong-original-link-transport')
    check('all-explicit-signed-coordinate-transports',len(seen)==8621 and seen==set().union(*(set(v) for v in orbits.values())))
    clusters=[];allsets=set()
    for n in (1,2,3):
        _,classes=enumerate_classes(n)
        for fs in classes:
            if len(set(fs))==n:allsets.add(tuple(sorted(fs)))
    for i,fs in enumerate(sorted(allsets,key=lambda x:(len(x),x))):
        c=Cluster(fs);raw=c.sixth();value=Q(raw['coefficients'][2]);N=len(fs)
        edges=[(a,b) for a,b in combinations(range(N),2) if pedges(fs[a])&pedges(fs[b])]
        typ='single' if N==1 else 'adjacent_pair' if N==2 else type3(fs)
        check(f'original-small-cluster-sixth-independent-{i}-{typ}',value==small_cluster_energy6(N,edges,[typ] if N==3 else []))
        linked=value-N*WEIGHTS['single']
        if N==1:linked=value
        if N==3:linked-=len(edges)*WEIGHTS['adjacent_pair']
        check(f'original-small-cluster-linked-sixth-{i}-{typ}',linked==WEIGHTS[typ])
        clusters.append({'faces':[list(p) for p in fs],'type':typ,'energy_coefficients':raw['coefficients'],'linked_sixth':str(linked)})
    cube=cube_data();check('all-720-cube-orders',len(cube['paths'])==720)
    check('cube-complete-saved-certificate',cube==load(ROOT/'results/cube_sixth_paths.json'))
    check('original-cube-Haar-factor',cube['Haar_six_trace_product']=='1/16')
    check('cube-two-independent-time-orders',cube['linked_sixth_weight']==cube['independent_half_path_value']=='-83/1944')
    check('cube-five-resolvent-product-sum',cube['ordered_insertion_sum']=='166/243')
    rejected('delete-original-cube-surface',WEIGHTS['cube']==0)
    rejected('drop-twelve-original-Haar-edge-integrals',-Q(cube['ordered_insertion_sum'])==WEIGHTS['cube'])
    boxes=[]
    for L in (2,3,4):check('entire-original-box-counts-'+str(L),enumerate_box(L)==counts(L))
    for L in (2,3,4,5,7,10):
        row=coefficients(L);boxes.append(row);check('full-unsubtracted-sixth-vector-return-'+str(L),full_box_from_vector_data(L)==Q(row['ground_energy_over_kappa_coefficients']['xi6']))
    check('original-L2-sixth-value',Q(boxes[0]['ground_energy_over_kappa_coefficients']['xi6'])==-Q(3528610133,1172873520))
    rejected('only-up-to-three-face-supports-suffice-for-sixth',full_box_from_vector_data(2)-64*WEIGHTS['cube']==full_box_from_vector_data(2))
    chars=independent_character();check('original-Haar-fourth-mixed',Ring.moment4((2,2,0,0))==Q(1,24))
    rejected('Gaussian-Haar-fourth-moment-replacement',Q(1,16)==Q(1,24))
    for n in range(21):check('inherited-discriminant-arithmetic-'+str(n),discriminant(Q(n,1000))==polynomial(Q(n,1000)))
    check('inherited-exact-benchmark',ell(Q(1,64))==Q(28973,39936) and discriminant(Q(1,64))==Q(10028381,224280576))
    rejected('omit-inherited-quartic-residual',(1-ell(Q(1,64)))**2-Q(8,3)*Q(944984,351)*Q(1,64)**3==discriminant(Q(1,64)))
    M=240;R=Q(3,8*M);check('independent-L2-analytic-radius',R==Q(1,640));check('finite-volume-resolvent-ratio',R*2*M*Q(2,3)==Q(1,2))
    rejected('volume-independent-analytic-radius',Q(1,64)*2*M*Q(2,3)<1)
    return {'quartic_classes':78,'anchored_multisets':8621,'polynomial_monomials':terms,'exact_downset_inverse_checks':downsets,'exact_log_source_checks':downsets,'original_chord_count_distribution':{str(k):v for k,v in sorted(chord_counts.items())},'original_generator_jet_count':sum(x['original_link_generator_tests'] for x in jets),'small_cluster_sixth_results':clusters,'independent_single_character_coefficients':chars,'finite_boxes':boxes,'quartic_file_sha256':certificate_hashes}

def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--write-receipt',type=Path);parser.add_argument('--verify-receipt',type=Path);parser.add_argument('--progress',action='store_true');args=parser.parse_args()
    try:
        sources=source_files();saved=None
        if args.verify_receipt:
            saved=load(args.verify_receipt);require(saved.get('schema')=='ym-audit-completion-verification-v1','receipt-schema')
            require(saved.get('scope',{}).get('new_continuum_gap_established') is False,'unsupported-continuum-claim')
            require(saved.get('scope',{}).get('analytic_proofs_machine_formalized') is False,'unsupported-formal-claim')
            for name,sha in sources.items():require(saved.get('source_sha256',{}).get(name)==sha,'source-identity-mismatch:'+name)
        result=main_checks(args.progress)
        record={'schema':'ym-audit-completion-verification-v1','passed':True,'scope':{'finite_exact_polynomial_identities':True,'original_link_regressions':True,'inherited_scalar_arithmetic_checked':True,'inherited_analytic_gap_proof_independently_certified':False,'analytic_proofs_machine_formalized':False,'new_continuum_gap_established':False,'vacuum_sampling':False,'finite_spin_cutoff_of_full_Hamiltonian':False},'counts':{'named_checks':len(CHECKS),'false_formula_controls':len(NEGATIVE)},'results':result,'checks':CHECKS,'negative_controls':NEGATIVE,'source_sha256':sources}
        if saved is not None:require(record==saved,'complete-receipt-mismatch')
        text=json.dumps(record,indent=2,sort_keys=True)+'\n'
        if args.write_receipt:args.write_receipt.write_text(text)
        else:sys.stdout.write(text)
        return 0
    except (Failure,ArithmeticError,ValueError,OSError,KeyError) as e:
        sys.stderr.write('FAIL: '+str(e)+'\n');return 1
if __name__=='__main__':raise SystemExit(main())
