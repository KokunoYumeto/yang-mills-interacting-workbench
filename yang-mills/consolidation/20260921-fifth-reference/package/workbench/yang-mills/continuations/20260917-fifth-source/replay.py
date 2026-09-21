#!/usr/bin/env python3
"""Replay the complete new exact checks; record real exits and named failures."""
from pathlib import Path
import subprocess,sys,json,hashlib,tempfile,shutil,time,datetime
ROOT=Path(__file__).resolve().parent
LOG=ROOT/'execution';LOG.mkdir(exist_ok=True)
RECEIPT=ROOT/'generated/verification.json'
records=[]
def run(name,args,cwd=ROOT,wanted=0,message=None):
 cmd=[sys.executable]+args;start=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
 p=subprocess.run(cmd,cwd=cwd,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
 (LOG/(name+'.stdout')).write_bytes(p.stdout);(LOG/(name+'.stderr')).write_bytes(p.stderr)
 ok=p.returncode==wanted and (message is None or message.encode() in p.stderr)
 records.append({'name':name,'command':cmd,'cwd_role':'original' if cwd==ROOT else 'isolated-copy','started_utc':start,'duration_seconds':time.monotonic()-t,'exit_code':p.returncode,'expected_exit':wanted,'expected_error':message,'passed':ok,'stdout_sha256':hashlib.sha256(p.stdout).hexdigest(),'stderr_sha256':hashlib.sha256(p.stderr).hexdigest()})
 (LOG/'replay.json').write_text(json.dumps(records,indent=2)+'\n')
 if not ok:raise RuntimeError(name+': '+p.stderr.decode(errors='replace')[-2000:])
 return p

def main():
 for mode in ([],['-O']):
  tag='optimized' if mode else 'ordinary'
  run('full-polynomial-'+tag,mode+['-B','audit_fifth.py','--verify-existing','--workers','4'])
  run('receipt-'+tag,mode+['-B','verify_fifth.py','--verify-receipt','generated/verification.json'])
  before=(ROOT/'generated/direct_matrix_checks.json').read_bytes()
  run('independent-matrix-'+tag,mode+['-B','direct_matrix_checks.py'])
  if (ROOT/'generated/direct_matrix_checks.json').read_bytes()!=before:raise RuntimeError('independent-matrix-record-changed')
 # An isolated copy includes the complete used predecessor source directories.
 with tempfile.TemporaryDirectory(prefix='ym-fifth-replay-') as td:
  base=Path(td)/'continuations';base.mkdir()
  for name in ('20260916-cubic-linearized','20260917-quartic-cube',ROOT.name):
   shutil.copytree(ROOT.parent/name,base/name,ignore=shutil.ignore_patterns('__pycache__','execution'))
  copy=base/ROOT.name;original=RECEIPT.read_bytes();raw=json.loads(original)
  for mode in ([],['-O']):
   tag='optimized' if mode else 'ordinary'
   run('fresh-copy-'+tag,mode+['-B','verify_fifth.py','--verify-receipt','generated/verification.json'],cwd=copy)
   bad=Path(td)/'bad-receipt.json'
   data=dict(raw);data['schema']='wrong';bad.write_text(json.dumps(data))
   run('bad-schema-'+tag,mode+['-B','verify_fifth.py','--verify-receipt',str(bad)],cwd=copy,wanted=1,message='receipt-schema')
   bad.write_text('{"schema":"a","schema":"b"}')
   run('duplicate-key-'+tag,mode+['-B','verify_fifth.py','--verify-receipt',str(bad)],cwd=copy,wanted=1,message='duplicate-json-key:schema')
   data=json.loads(original);del data['source_sha256'][next(iter(data['source_sha256']))];bad.write_text(json.dumps(data))
   run('missing-manifest-member-'+tag,mode+['-B','verify_fifth.py','--verify-receipt',str(bad)],cwd=copy,wanted=1,message='source-manifest-membership')
   for label,name,change in [('changed-coefficient','generated/fifth/0000.json','coefficient'),('changed-proof','FIFTH_SOURCE.md','append'),('changed-response','generated/response_L2.json','append')]:
    target=copy/name;saved=target.read_bytes()
    if change=='coefficient':
     v=json.loads(saved);v['coefficients'][0]['coefficient']='0';target.write_text(json.dumps(v))
    else:target.write_bytes(saved+b'\ncorruption control\n')
    try:run(label+'-'+tag,mode+['-B','verify_fifth.py','--verify-receipt','generated/verification.json'],cwd=copy,wanted=1,message='source-identity-mismatch:'+name)
    finally:target.write_bytes(saved)
   target=copy/'generated/fifth/0661.json';saved=target.read_bytes();target.unlink()
   try:run('missing-source-row-'+tag,mode+['-B','verify_fifth.py','--verify-receipt','generated/verification.json'],cwd=copy,wanted=1,message='source-manifest-membership')
   finally:target.write_bytes(saved)
   run('restored-copy-'+tag,mode+['-B','verify_fifth.py','--verify-receipt','generated/verification.json'],cwd=copy)
 print(json.dumps({'passed':True,'observed_executions':len(records),'negative_cli_executions':sum(r['expected_exit']!=0 for r in records)},sort_keys=True))
if __name__=='__main__':main()
