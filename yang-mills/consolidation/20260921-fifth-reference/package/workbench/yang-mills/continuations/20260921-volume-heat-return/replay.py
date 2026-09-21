#!/usr/bin/env python3
"""Replay the exact new calculations, fresh copies and named corruption checks.
Outputs belong outside the sealed cumulative archive. No network calls.
"""
from pathlib import Path
import argparse,hashlib,json,shutil,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parent
WB=ROOT.parents[2]

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def snapshot(base):
 return {str(p.relative_to(base)):sha(p) for p in base.rglob('*') if p.is_file() and '__pycache__' not in p.parts}
def encoded(x):return json.dumps(x,sort_keys=True,indent=2)+'\n'

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',type=Path);ap.add_argument('--skip-copy-and-mutations',action='store_true');a=ap.parse_args()
 out=a.output_dir or Path(tempfile.mkdtemp(prefix='ym-volume-replay-'));out.mkdir(parents=True,exist_ok=True)
 records=[]
 def execute(label,cwd,tail,opt=False,expected=0,contains=None):
  flags=['-O','-B'] if opt else ['-B'];command=[sys.executable,*flags,*tail];start=time.monotonic();before=snapshot(cwd)
  with (out/(label+'.log')).open('wb') as log:p=subprocess.run(command,cwd=cwd,stdout=log,stderr=subprocess.STDOUT)
  after=snapshot(cwd);text=(out/(label+'.log')).read_text()
  ok=p.returncode==expected and (contains is None or contains in text) and before==after
  records.append({'label':label,'command':['python',*flags,*tail],'exit_code':p.returncode,'expected_exit':expected,'expected_error':contains,'bytes_unchanged':before==after,'passed':ok,'seconds':time.monotonic()-start,'log_sha256':sha(out/(label+'.log'))})
  (out/'execution.json').write_text(encoded({'schema':'ym-volume-replay-v1','records':records,'all_passed':all(r['passed'] for r in records)}))
  print(label,p.returncode,ok,flush=True)
  if not ok:raise RuntimeError('execution-failed:'+label)
 for opt in (False,True):
  suf='optimized' if opt else 'ordinary'
  execute('producer-'+suf,ROOT,['produce_bounds.py','--verify-existing'],opt)
  execute('sharpened-'+suf,ROOT,['sharpen_bounds.py','--verify-existing'],opt)
  execute('route-'+suf,ROOT,['route_check.py','--verify-existing'],opt)
  execute('auditor-'+suf,ROOT,['audit_bounds.py','--verify-receipt','verification.json'],opt)
 if not a.skip_copy_and_mutations:
  scratch=out/'fresh';shutil.copytree(WB,scratch,ignore=shutil.ignore_patterns('__pycache__'),dirs_exist_ok=True)
  fresh=scratch/ROOT.relative_to(WB)
  for opt in (False,True):
   suf='optimized' if opt else 'ordinary'
   execute('fresh-producer-'+suf,fresh,['produce_bounds.py','--verify-existing'],opt)
   execute('fresh-sharpened-'+suf,fresh,['sharpen_bounds.py','--verify-existing'],opt)
   execute('fresh-route-'+suf,fresh,['route_check.py','--verify-existing'],opt)
   execute('fresh-auditor-'+suf,fresh,['audit_bounds.py','--verify-receipt','verification.json'],opt)
  receipt=fresh/'verification.json';original=receipt.read_bytes()
  def mutation(label,file,changed,error,rebind=False,missing=False):
   saved=file.read_bytes()
   try:
    if missing:file.unlink()
    else:file.write_bytes(changed)
    if rebind:
     obj=json.loads(original);obj['sha256'][file.relative_to(fresh).as_posix()]=sha(file);receipt.write_text(encoded(obj))
    for opt in (False,True):execute(label+('-optimized' if opt else '-ordinary'),fresh,['audit_bounds.py','--verify-receipt','verification.json'],opt,1,error)
   finally:
    file.write_bytes(saved);receipt.write_bytes(original)
  proof=fresh/'VOLUME_UNIFORM_HEAT.md'
  mutation('proof-identity',proof,proof.read_bytes()+b'\nchanged\n','source-identity-mismatch')
  anchor=fresh/'generated/anchored_coefficients.json'
  mutation('missing-coefficients',anchor,b'','missing-source:generated/anchored_coefficients.json',missing=True)
  mutation('duplicate-receipt-key',receipt,b'{"schema":"wrong",'+original.lstrip()[1:],'duplicate-json-key:schema')
  obj=json.loads(original);obj['count']=0
  mutation('wrong-complete-receipt',receipt,encoded(obj).encode(),'receipt-mismatch')
  obj=json.loads(anchor.read_text());obj['contributions'][0]['values']['0']='2'
  mutation('rebound-original-moment',anchor,encoded(obj).encode(),'all-original-moments-0',rebind=True)
  obj=json.loads(anchor.read_text());obj['transports']=obj['transports'][1:]
  mutation('rebound-missing-support',anchor,encoded(obj).encode(),'complete-199-original-clusters',rebind=True)
  sharp=fresh/'generated/sharp_constants.json';obj=json.loads(sharp.read_text());obj['benchmarks'][-1]['complement_loss_upper']='0'
  mutation('rebound-complement-loss',sharp,encoded(obj).encode(),'sharp-all-original-return-values-16',rebind=True)
  parent=fresh.parent/'20260921-heat-response-transfer/generated/heat_matrix_L2.json'
  mutation('missing-parent-matrix',parent,b'','missing-predecessor:heat_matrix_L2.json',missing=True)
  for opt in (False,True):execute('restored-'+('optimized' if opt else 'ordinary'),fresh,['audit_bounds.py','--verify-receipt','verification.json'],opt)
  # Preserve a compact exact identity of the fresh replay tree, not a duplicate payload.
  (out/'fresh_tree_sha256.json').write_text(encoded(snapshot(scratch)))
  shutil.rmtree(scratch)
 print('COMPLETE',len(records),str(out),flush=True)

if __name__=='__main__':
 try:main()
 except (RuntimeError,OSError,ValueError) as e:print('FAIL:',e,file=sys.stderr);raise SystemExit(1)
