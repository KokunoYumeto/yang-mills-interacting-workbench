#!/usr/bin/env python3
"""Observed ordinary/optimized replay of the independently derived signed tangent."""
from pathlib import Path
import argparse,datetime,hashlib,json,os,shutil,subprocess,sys,tempfile,time
ROOT=Path(__file__).resolve().parents[1]
def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'results/signed_tangent_execution.json');args=ap.parse_args()
    expected=(ROOT/'results/signed_tangent.json').read_bytes();records=[]
    with tempfile.TemporaryDirectory(prefix='ym-tangent-fresh-') as td:
        fresh=Path(td)/'session';shutil.copytree(ROOT,fresh,ignore=shutil.ignore_patterns('__pycache__','replay_current.log','tangent_optimized_output.json','signed_tangent_execution.json'))
        for opt in (False,True):
            cmd=[sys.executable,*(['-O'] if opt else []),'-B',str(fresh/'checks/verify_signed_tangent.py'),'--verify-receipt',str(fresh/'results/signed_tangent.json')]
            stamp=datetime.datetime.now(datetime.timezone.utc).isoformat();t=time.monotonic()
            p=subprocess.run(cmd,capture_output=True,timeout=600,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
            if p.returncode or p.stderr or p.stdout!=expected:raise RuntimeError(('tangent-fresh-mismatch',opt,p.returncode,p.stderr.decode()))
            records.append({'mode':'optimized' if opt else 'ordinary','fresh_copy':True,'returncode':p.returncode,'started_utc':stamp,'elapsed_seconds':time.monotonic()-t,'output_sha256':hashlib.sha256(p.stdout).hexdigest(),'output_bytes':len(p.stdout)})
            print('FRESH SIGNED TANGENT PASS',opt,flush=True)
    data=json.loads(expected)
    result={'schema':'ym-signed-tangent-observed-execution-v1','records':records,'source_hashed_in_receipt':data['source_sha256'],'classes':data['classes'],'exact_polynomial_tangent_identities':data['zero_polynomial_tangent_identities'],'explicit_degree_three_entries':data['explicit_degree_three_response_entries'],'analytic_proofs_formalized':False,'full_linearized_operator_norm_bound':False}
    args.output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
if __name__=='__main__':
    try:main()
    except (RuntimeError,OSError,subprocess.TimeoutExpired) as e:raise SystemExit('FAIL: '+str(e))
