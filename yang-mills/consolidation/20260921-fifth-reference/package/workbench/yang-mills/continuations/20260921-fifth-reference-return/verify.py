#!/usr/bin/env python3
"""Verify the exact fifth-reference certificate and all of its sealed inputs.

This fast replay repeats arithmetic, word-tensor identities and the anchored
assembly; the complete polynomial audit is repeated by replay.py. No Python
assert statement controls acceptance.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse,json,hashlib,sys
import assemble_fifth_bounds as assembled
import audit_word_tensors as tensors
import return_bounds as returned
ROOT=Path(__file__).resolve().parent

class Failure(RuntimeError):pass

def need(ok,name):
 if not ok:raise Failure(name)

def strict(text):
 def pairs(rows):
  out={}
  for k,v in rows:
   need(k not in out,'duplicate-json-key:'+k);out[k]=v
  return out
 return json.loads(text,object_pairs_hook=pairs)

def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def sources():
 names=['FIFTH_REFERENCE.md','HEAT_AND_COMPLEMENT.md','README.md','SOURCE_INTAKE.json','state.json','ATTEMPTS.md',
        'evaluate_fifth_bounds.py','assemble_fifth_bounds.py','audit_spin_channels.py','audit_word_tensors.py','oriented_word_bounds.py','return_bounds.py','verify.py','replay.py',
        'generated/fifth_budgets.json','generated/physical_return.json','generated/spin_audit.json','generated/word_tensor_audit.json']
 names += ['generated/rows/'+f'{i:04d}.json' for i in range(662)]
 result={}
 for name in names:
  p=ROOT/name;need(p.is_file(),'missing-source:'+name);result[name]=sha(p)
 return result

def check_inputs():
 intake=strict((ROOT/'SOURCE_INTAKE.json').read_text())
 for r in intake['inputs']:
  p=ROOT/r['path'];need(p.is_file(),'missing-inherited-input:'+r['path'])
  need(p.stat().st_size==r['bytes'] and sha(p)==r['sha256'],'inherited-input-identity:'+r['path'])
 return len(intake['inputs'])

def run():
 checks=[];neg=[]
 def ck(name,test,value=None):
  need(name not in {r['name'] for r in checks},'duplicate-check-name')
  need(test,name);r={'name':name,'passed':True}
  if value is not None:r['value']=value
  checks.append(r)
 def reject(name,test):
  need(not test,'false-formula-accepted:'+name);neg.append(name)
 count=check_inputs();ck('all-pinned-inherited-inputs',count==676,count)
 b=assembled.assemble();ck('complete-original-anchored-assembly',b==strict((ROOT/'generated/fifth_budgets.json').read_text()))
 ck('all124864-original-transports',sum(r['count'] for r in b['contributions'])==124864)
 ck('rounded-m5',F(b['M5'])<1638684);ck('rounded-t5',F(b['T5'])<190128);ck('rounded-c5',F(b['C5'])<2476866)
 audit=strict((ROOT/'generated/spin_audit.json').read_text());ck('complete-channel-count',audit['passed'] and audit['full_channel_identities']==321)
 ck('complete-dual-count',audit['dual_certificates']==5726)
 totals=improved=0
 for r in audit['rows']:
  if r['channel_expansion_used']:
   p=ROOT/'generated/rows'/f"{r['index']:04d}.json";need(sha(p)==r['row_sha256'],'audited-row-identity:'+p.name)
   s=strict(p.read_text())['spin'];totals+=len(s['partial_bounds'])
   improved+=sum(F(x)<F(y) for x,y in zip(s['partial_bounds'],s['length_only_bounds']))
 ck('all6240-partial-projections',totals==6240,totals);ck('3498-strict-reflection-improvements',improved==3498,improved)
 t=tensors.run();ck('complete-word-tensor-replay',t==strict((ROOT/'generated/word_tensor_audit.json').read_text()))
 ck('316-independent-occurrence-matrices',t['sign_patterns']==316)
 d=returned.calculate();ck('complete-physical-return-replay',d==strict((ROOT/'generated/physical_return.json').read_text()))
 lo,hi=map(F,d['alpha_bracket']);glo,ghi=map(F,d['g_squared_threshold_bracket'])
 ck('outward-original-source-endpoint',F('0.018424953576117616681')<lo<hi<F('0.018424953576117616682'))
 ck('outward-original-coupling-endpoint',F('3.683551983985727304439')<glo<ghi<F('3.683551983985727304440'))
 ck('source-endpoint-improves-saved-quartic',lo>F('0.018104972231644127076'))
 ck('complete-residual-degrees-six-through-ten',set(d['residual_coefficients'])==set(map(str,range(6,11))))
 ck('tenth-degree-is-retained',F(d['residual_coefficients']['10'])==returned.B[5,5]>0)
 ck('first-linear-factor-two',returned.L[1]==F(128,3))
 h=d['heat_circle'];ck('original-heat-radius',F(h['radius'])==F(1,55))
 ck('original-heat-decay',F(h['decay'])==F(13,8));ck('original-heat-prefactor',F(h['prefactor'])==F(67896,169))
 ck('complete-signed-heat-weight',F(h['signed_leakage_prefactor'])==F(5156090136,3570125))
 benchmark={r['g_squared_min']:r for r in d['benchmarks']}
 for g,lower,upper in [('37/10',F('1.6207'),F('0.046581')),('15/4',F('1.6993'),F('0.026352')),('4',F('1.9068'),F('0.005752'))]:
  r=benchmark[g];ck('physical-gap-'+g,F(r['gap_over_kappa'][0])>lower);ck('full-correction-'+g,F(r['correction_norm'][1])<upper)
 for r in d['native']:
  g=r['g_squared_min'];O=F(r['observation_fraction_lower']);E=F(r['complement_loss_upper']);G=F(r['state_increase_upper'])
  if g=='8':bounds=(F(717,1000),F(177,1000),F(208,1000))
  elif g=='10':bounds=(F(977,1000),F(11,1000),F(12,1000))
  elif g=='12':bounds=(F(997,1000),F(12,10000),F(12,10000))
  elif g=='25/2':bounds=(F(998,1000),F(1,1000),F(1,1000))
  elif g=='13':bounds=(F(999,1000),F(1,2000),F(1,2000))
  else:bounds=(F(9999,10000),F(1,25000),F(1,25000))
  ck('actual-observation-'+g,O>bounds[0]);ck('full-complement-energy-'+g,E<bounds[1]);ck('full-complement-state-'+g,G<bounds[2])
  if g=='16':ck('actual-section-energy-16',F(r['section_energy_upper'])<F(1,20000))
 # False identities use explicit original coefficient constants or the actual tensor map.
 reject('erase-tenth-residual',F(d['residual_coefficients']['10'])==0)
 reject('erase-fifth-reference-spin',returned.T[5]==0)
 reject('Frechet-without-two',returned.L[1]==F(64,3))
 reject('partial-transpose-coefficient-norm-isometry',t['partial_transpose_trace_norms'][0]==t['partial_transpose_trace_norms'][1])
 reject('erase-reflection-supremum',improved==totals)
 reject('erase-Catalan-endpoint-tail',F(1,2)==0)
 # Exact inverse-energy diagonal example retains the mixed factor -6.
 energy=F(4);g0=F(1);g1=1/energy;g2=1/energy**2
 ck('original-leakage-three-term-identity',(1-3/energy)**2==g0-6*g1+9*g2)
 reject('drop-leakage-cross-term',(1-3/energy)**2==g0+9*g2)
 reject('drop-leakage-factor-two',(1-3/energy)**2==g0-3*g1+9*g2)
 reject('new-source-domain-is-all-couplings',returned.disc(F(19,1000))>=0)
 for k2,a in [(F(4),F(3)),(F(13),F(7))]:
  kappa=2*k2/a;xi=1/(4*k2*k2);ck('physical-parameter-inverse-'+str(k2),1/(2*k2)==2*k2*xi)
  reject('drop-original-kappa-'+str(k2),kappa==k2/a)
 return {'schema':'ym-fifth-reference-verification-v1','passed':True,'named_checks':len(checks),'false_formula_controls':len(neg),
  'scope':{'analytic_arguments_formalized':False,'external_analytical_review':False,'full_new_channel_polynomials_in_separate_replay':321,
           'exact_dual_certificates':5726,'inherited_rows':662,'original_anchored_transports':124864,'word_tensor_matrices':316,
           'sixth_catalogue_recovered':False,'continuum_mass_gap_established':False},
  'results':{'M5':b['M5'],'T5':b['T5'],'C5':b['C5'],'heat_circle':h,'g_squared_threshold_bracket':d['g_squared_threshold_bracket']},
  'checks':checks,'negative_controls':neg,'source_sha256':sources()}

def main():
 p=argparse.ArgumentParser();p.add_argument('--verify-receipt',type=Path);p.add_argument('--output',type=Path);a=p.parse_args()
 try:
  if a.verify_receipt:
   expected_text=a.verify_receipt.read_text();expected=strict(expected_text)
   need(expected.get('schema')=='ym-fifth-reference-verification-v1','receipt-schema')
   cur=sources();need(set(cur)==set(expected['source_sha256']),'source-manifest-membership')
   for name,h in cur.items():need(expected['source_sha256'][name]==h,'source-identity-mismatch:'+name)
  obj=run();encoded=json.dumps(obj,sort_keys=True,indent=2)+'\n'
  if a.verify_receipt:need(expected_text==encoded,'complete-receipt-mismatch')
  if a.output:a.output.write_text(encoded)
  else:sys.stdout.write(encoded)
  return 0
 except (OSError,ValueError,Failure,ArithmeticError) as e:
  print('FAIL: '+str(e),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
