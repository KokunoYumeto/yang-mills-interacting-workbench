#!/usr/bin/env python3
"""Reproduce this finite certificate and its predecessor; record actual exits."""
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile,time
HERE=Path(__file__).resolve().parent
sha=lambda b:hashlib.sha256(b).hexdigest()
def main():
 p=argparse.ArgumentParser(description=__doc__);p.add_argument('--parent',type=Path);p.add_argument('--output',type=Path,default=HERE/'execution.json');a=p.parse_args()
 expected=(HERE/'verification.json').read_bytes();records=[]
 def run(name,script,args=(),opt=False,error=None,wanted=expected):
  cmd=[sys.executable,*(['-O'] if opt else []),'-B',str(script),*map(str,args)]
  t=time.monotonic();r=subprocess.run(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=180,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
  if error is None:
   if r.returncode or r.stderr or r.stdout!=wanted:raise RuntimeError((name,r.returncode,r.stderr.decode(),sha(r.stdout)))
  elif r.returncode!=1 or r.stdout or r.stderr.decode()!='FAIL: '+error+'\n':raise RuntimeError((name,r.returncode,r.stdout[:100],r.stderr))
  records.append({'name':name,'exit_code':r.returncode,'seconds':time.monotonic()-t,'stdout_sha256':sha(r.stdout),'stderr_sha256':sha(r.stderr),'intended_error':error});print(name+': PASS',flush=True)
 for opt in (False,True):run('current-'+str(opt),HERE/'verify.py',['--verify-receipt',HERE/'verification.json'],opt)
 if a.parent:
  parent=a.parent;args=['--verify-receipt',parent/'verification.json','--verify-box-certificate',parent/'BOX_L2_CERTIFICATE.json'];pe=(parent/'verification.json').read_bytes()
  for opt in (False,True):run('unchanged-parent-'+str(opt),parent/'verify.py',args,opt,wanted=pe)
 with tempfile.TemporaryDirectory(prefix='ym-cubic-replay-') as td:
  copy=Path(td)/'copy';shutil.copytree(HERE,copy,ignore=shutil.ignore_patterns('__pycache__','execution.json','replay.log'))
  for opt in (False,True):run('copied-source-'+str(opt),copy/'verify.py',['--verify-receipt',copy/'verification.json'],opt)
  wrong=Path(td)/'wrong.json';wrong.write_text('{"schema":"wrong"}\n')
  duplicate=Path(td)/'duplicate.json';duplicate.write_text('{"schema":"a","schema":"b"}\n')
  for opt in (False,True):
   run('wrong-schema-'+str(opt),copy/'verify.py',['--verify-receipt',wrong],opt,'receipt-schema')
   run('duplicate-json-'+str(opt),copy/'verify.py',['--verify-receipt',duplicate],opt,'duplicate-json-key:schema')
  for name in ('CUBIC_SOURCE.md','geometry.py'):
   f=copy/name;old=f.read_bytes();f.write_bytes(old+b'\n# altered source\n')
   for opt in (False,True):run('modified-'+name+'-'+str(opt),copy/'verify.py',['--verify-receipt',copy/'verification.json'],opt,'source-identity-mismatch:'+name)
   f.write_bytes(old)
  for opt in (False,True):run('restored-source-'+str(opt),copy/'verify.py',['--verify-receipt',copy/'verification.json'],opt)
 result={'schema':'ym-cubic-observed-execution-v1','records':records,'ordinary_optimized_identical':True,'copied_sources_match':True,'parent_replayed':bool(a.parent),'finite_counts':json.loads(expected)['counts'],'receipt_sha256':sha(expected),'analytic_proof_formally_verified':False,'independent_external_review':False,'remote_CI_run':False,'paid_model_run':False}
 a.output.write_text(json.dumps(result,sort_keys=True,indent=2)+'\n');print('REPLAY PASS',len(records),flush=True)
if __name__=='__main__':main()
