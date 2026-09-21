#!/usr/bin/env python3
"""Regenerate all new bounds and polynomial checks in both Python modes."""
from pathlib import Path
from fractions import Fraction as F
import json,subprocess,sys,hashlib,argparse,time
ROOT=Path(__file__).resolve().parent

def main():
 parser=argparse.ArgumentParser();parser.add_argument('--output-dir',type=Path,required=True);args=parser.parse_args()
 out=args.output_dir.resolve();out.mkdir(parents=True,exist_ok=True)
 if out==ROOT or ROOT in out.parents:raise ValueError('logs-must-be-outside-sealed-continuation')
 records=[]
 def run(name,command,want=0,fragment=None):
  start=time.monotonic();p=subprocess.run(command,cwd=ROOT,text=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
  (out/(name+'.stdout')).write_text(p.stdout);(out/(name+'.stderr')).write_text(p.stderr)
  ok=p.returncode==want and (fragment is None or fragment in p.stderr)
  r={'name':name,'command':command,'returncode':p.returncode,'expected_exit':want,'passed':ok,
     'seconds_diagnostic':round(time.monotonic()-start,3),'stdout_sha256':hashlib.sha256(p.stdout.encode()).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr.encode()).hexdigest()}
  if fragment:r['required_error']=fragment
  records.append(r);(out/'execution.json').write_text(json.dumps({'complete':False,'records':records},indent=2)+'\n')
  if not ok:raise RuntimeError('replay-failed:'+name+' '+p.stderr[-700:])
  print('PASS',name,flush=True)
 def base(opt=False):return [sys.executable]+(['-O'] if opt else [])+['-B']
 for mode in (False,True):
  tag='optimized' if mode else 'normal';b=base(mode)
  run(tag+'-initial-receipt',b+['verify.py','--verify-receipt','verification.json'])
  run(tag+'-full-662-row-producer',b+['evaluate_fifth_bounds.py','--workers','8'])
  run(tag+'-124864-anchor-return',b+['assemble_fifth_bounds.py','--verify-existing'])
  target=out/(tag+'-spin-audit.json')
  run(tag+'-complete-polynomial-dual-audit',b+['audit_spin_channels.py','--workers','8','--output',str(target)])
  if target.read_bytes()!=(ROOT/'generated/spin_audit.json').read_bytes():raise RuntimeError('polynomial-audit-byte-mismatch')
  run(tag+'-tensor-matrices',b+['audit_word_tensors.py','--verify-existing'])
  run(tag+'-source-heat-native-return',b+['return_bounds.py','--verify-existing'])
  run(tag+'-regenerated-receipt',b+['verify.py','--verify-receipt','verification.json'])
 # Each mutation is restored in a finally block. No inherited source is modified.
 idx=next(i for i in range(662) if json.loads((ROOT/'generated/rows'/f'{i:04d}.json').read_text())['spin'])
 path=ROOT/'generated/rows'/f'{idx:04d}.json';original=path.read_bytes()
 for mode in (False,True):
  tag='optimized' if mode else 'normal';b=base(mode)
  # Identity guard: proof and coefficient source mutations.
  note=ROOT/'FIFTH_REFERENCE.md';oldnote=note.read_bytes()
  try:
   note.write_bytes(oldnote+b'\nchanged by the declared rejection test\n')
   run(tag+'-reject-proof-change',b+['verify.py','--verify-receipt','verification.json'],1,'source-identity-mismatch:FIFTH_REFERENCE.md')
  finally:note.write_bytes(oldnote)
  try:
   row=json.loads(original);row['M']='0';path.write_text(json.dumps(row))
   run(tag+'-reject-coefficient-record-change',b+['verify.py','--verify-receipt','verification.json'],1,'source-identity-mismatch:generated/rows/')
  finally:path.write_bytes(original)
  receipt=(ROOT/'verification.json').read_text()
  bad=out/(tag+'-duplicate.json');bad.write_text('{"schema":"duplicate",'+receipt[1:])
  run(tag+'-reject-duplicate-key',b+['verify.py','--verify-receipt',str(bad)],1,'duplicate-json-key:schema')
  rec=json.loads(receipt);rec['passed']=False;bad=out/(tag+'-bad-receipt.json');bad.write_text(json.dumps(rec))
  run(tag+'-reject-false-receipt',b+['verify.py','--verify-receipt',str(bad)],1,'complete-receipt-mismatch')
  # Mathematical guards run the separate audit directly, bypassing identity gates.
  for mutation,expect in [('zero-dual','dual-feasible'),('partial-polynomial','partial-polynomial-'),('channel-weight','original-channel-objective')]:
   try:
    row=json.loads(original);sp=row['spin']
    if mutation=='zero-dual':sp['certificates'][0]['dual']=['0']*len(sp['certificates'][0]['dual'])
    elif mutation=='partial-polynomial':sp['partial_polynomials'][0][0]['coefficient']=str(F(sp['partial_polynomials'][0][0]['coefficient'])+1)
    else:sp['certificates'][0]['weights'][0]=str(F(sp['certificates'][0]['weights'][0])+1)
    path.write_text(json.dumps(row))
    code='from audit_spin_channels import audit; audit('+str(idx)+')'
    run(tag+'-reject-'+mutation,b+['-c',code],1,expect)
   finally:path.write_bytes(original)
  run(tag+'-restored-final-receipt',b+['verify.py','--verify-receipt','verification.json'])
 result={'complete':True,'passed':True,'records':records,'execution_count':len(records),
         'full_channel_identities_per_mode':321,'dual_certificates_per_mode':5726,'input_rows_per_mode':662,'anchored_transports_per_mode':124864,
         'ordinary_optimized_polynomial_records_identical':(out/'normal-spin-audit.json').read_bytes()==(out/'optimized-spin-audit.json').read_bytes(),
         'final_row_restored':path.read_bytes()==original,'analytic_arguments_formalized':False}
 (out/'execution.json').write_text(json.dumps(result,sort_keys=True,indent=2)+'\n')
 print('COMPLETE',len(records),'executions',flush=True)
if __name__=='__main__':main()
