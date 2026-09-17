#!/usr/bin/env python3
"""Construct the log source directly and verify every cubic signed tangent entry.

This is independent of the eigenvector-to-log recurrence used by the main
catalogue producer. Equality is tested as a full rational quotient polynomial.
"""
from __future__ import annotations
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import argparse,hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'calculations'))
from gauge_polynomial import Cluster
from build_quartic import serialize_poly

def source_and_tangent(entry):
    fs=tuple(tuple(p) for p in entry['model']['faces']);nu=tuple(entry['coupling_multiindex']);c=Cluster(fs);r=c.ring
    indices=sorted(product(*(range(n+1) for n in nu)),key=lambda x:(sum(x),x));zero=(0,)*len(nu)
    sub=lambda a,b:tuple(x-y for x,y in zip(a,b))
    leq=lambda a,b:all(x<=y for x,y in zip(a,b))
    v={};kinetic={};identities=[]
    def gamma(a,b):return r.scale(Q(1,2),r.add(r.mul(c.K(a),b),r.mul(a,c.K(b)),r.scale(-1,c.K(r.mul(a,b)))))
    for mu in indices[1:]:
        rhs={}
        if sum(mu)==1:rhs=c.W[mu.index(1)]
        else:
            for t,a in v.items():
                if leq(t,mu) and sub(mu,t) in v:rhs=r.add(rhs,gamma(a,v[sub(mu,t)]))
        v[mu]=c.inv(rhs,counts=mu);kinetic[mu]=c.K(v[mu])
    actual={tuple(x['powers']):Q(x['coefficient']) for x in entry['coefficient_polynomial']}
    if v[nu]!=actual:raise ArithmeticError('direct-log-source-catalogue-mismatch:'+str(entry['index']))
    rows=[]
    for p in range(len(nu)):
        limit=list(nu);limit[p]-=1
        if limit[p]<0:continue
        for a in sorted(product(*(range(n+1) for n in limit)),key=lambda x:(sum(x),x)):
            ap=list(a);ap[p]+=1;ap=tuple(ap);z=r.scale(a[p]+1,v[ap]);rhs={}
            if sum(a)==0:rhs=c.W[p]
            else:
                for mu,h in v.items():
                    if 1<=sum(mu)<=3 and leq(mu,a):
                        b=sub(a,mu);bp=list(b);bp[p]+=1;bp=tuple(bp)
                        rhs=r.add(rhs,r.scale(2*(b[p]+1),gamma(h,v[bp])))
            rhs=r.add(rhs,r.const(-r.mean(rhs)))
            if r.add(c.K(z),r.scale(-1,rhs)):raise ArithmeticError(('signed-tangent-source-residual',entry['index'],p,a))
            identities.append({'face_index':p,'coupling_multiindex':list(a),'full_polynomial_residual':'zero'})
        degree_three=list(nu);degree_three[p]-=1
        rows.append({'class_index':entry['index'],'differentiated_original_face':list(fs[p]),'coupling_multiindex':degree_three,
                     'retained_original_multiset':entry['faces_with_multiplicity'],'source_prefactor':nu[p],
                     'chords':entry['model']['chords'],'coefficient_polynomial':serialize_poly(r.scale(nu[p],actual))})
    return {'class_index':entry['index'],'independent_log_source_matches':True,'signed_tangent_identities':identities,'degree_three_entries':rows}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--write-receipt',type=Path);ap.add_argument('--verify-receipt',type=Path);ap.add_argument('--progress',action='store_true');args=ap.parse_args()
    entries=[]
    for p in sorted((ROOT/'results/quartic_coefficients').glob('class_*.json')):
        e=source_and_tangent(json.loads(p.read_text()));entries.append(e)
        if args.progress:print('signed tangent',e['class_index'],'passed',file=sys.stderr,flush=True)
    hashes={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [Path(__file__),ROOT/'calculations/gauge_polynomial.py',ROOT/'calculations/build_quartic.py']}
    record={'schema':'ym-signed-tangent-certificate-v1','classes':len(entries),
            'complete_log_source_reconstructions':len(entries),
            'zero_polynomial_tangent_identities':sum(len(x['signed_tangent_identities']) for x in entries),
            'explicit_degree_three_response_entries':sum(len(x['degree_three_entries']) for x in entries),
            'scope':'Full formal-source and tangent polynomial identities on each retained original cluster; no infinite-operator norm or uniform gap bound is inferred.',
            'source_sha256':hashes,'results':entries}
    if args.verify_receipt and record!=json.loads(args.verify_receipt.read_text()):raise ArithmeticError('tangent-receipt-mismatch')
    raw=json.dumps(record,indent=2,sort_keys=True)+'\n'
    if args.write_receipt:args.write_receipt.write_text(raw)
    else:sys.stdout.write(raw)
if __name__=='__main__':
    try:main()
    except (ArithmeticError,OSError,ValueError) as e:raise SystemExit('FAIL: '+str(e))
