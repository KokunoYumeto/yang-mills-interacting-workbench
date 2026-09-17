#!/usr/bin/env python3
"""Execute the exact calculation in both Python modes and a fresh copied tree.

This records observed processes. It neither runs remote CI nor formalizes
analytic proofs. Execute from any directory with Python's standard library.
"""
from __future__ import annotations
from pathlib import Path
import argparse,hashlib,json,os,shutil,subprocess,sys,tempfile,time,datetime
ROOT=Path(__file__).resolve().parents[1]

def sha(b):return hashlib.sha256(b).hexdigest()

def run_all(output):
    records=[]
    def execute(name,tree,write=False,optimized=False,expected_error=None):
        command=[sys.executable,*(['-O'] if optimized else []),'-B',str(tree/'checks/verify.py')]
        command+=['--write-receipt' if write else '--verify-receipt',str(tree/'results/verification.json')]
        start=time.monotonic();stamp=datetime.datetime.now(datetime.timezone.utc).isoformat()
        p=subprocess.run(command,capture_output=True,timeout=600,env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        elapsed=time.monotonic()-start
        if expected_error is None:
            if p.returncode or p.stderr:raise RuntimeError((name,p.returncode,p.stderr.decode()))
            data=(tree/'results/verification.json').read_bytes()
            if not write and p.stdout!=data:raise RuntimeError((name,'returned receipt differs'))
        else:
            if p.returncode!=1 or p.stdout or p.stderr.decode()!='FAIL: '+expected_error+'\n':
                raise RuntimeError((name,p.returncode,p.stdout[:100],p.stderr.decode()))
            data=b''
        rec={'name':name,'optimized':optimized,'returncode':p.returncode,'started_utc':stamp,'elapsed_seconds':elapsed,
             'stdout_sha256':sha(p.stdout),'stdout_bytes':len(p.stdout),'stderr':p.stderr.decode(),'expected_error':expected_error}
        if expected_error is None:rec['complete_receipt_sha256']=sha(data)
        records.append(rec)
        print(name+': PASS',flush=True)
        return data
    expected=execute('ordinary-final-producer',ROOT,write=True)
    got=execute('optimized-complete-replay',ROOT,optimized=True)
    if got!=expected:raise RuntimeError('optimized bytes differ')
    with tempfile.TemporaryDirectory(prefix='ym-audit-fresh-') as td:
        fresh=Path(td)/'session'
        shutil.copytree(ROOT,fresh,ignore=shutil.ignore_patterns('__pycache__','execution.json','replay_current.log','first_complete_progress.log'))
        for opt in (False,True):
            data=execute('fresh-copy-'+str(opt),fresh,optimized=opt)
            if data!=expected:raise RuntimeError('fresh source result differs')
        cases=[
          ('proof','proofs/FOURTH_ORDER_SOURCE.md','source-identity-mismatch:proofs/FOURTH_ORDER_SOURCE.md'),
          ('helper','calculations/gauge_polynomial.py','source-identity-mismatch:calculations/gauge_polynomial.py'),
          ('source','input/Pasted markdown(6).md','source-identity-mismatch:input/Pasted markdown(6).md'),
          ('schema','results/verification.json','receipt-schema'),
          ('duplicate','results/verification.json','duplicate-json-key:schema'),
          ('global-claim','results/verification.json','unsupported-continuum-claim'),
          ('formal-claim','results/verification.json','unsupported-formal-claim'),
          ('coefficient','results/quartic_coefficients/class_00.json','quartic-complete-rebuilt-coefficient-00')]
        for typ,name,error in cases:
            p=fresh/name;original=p.read_bytes()
            if typ in ('proof','helper','source'):changed=original+b'\n# controlled source alteration\n'
            elif typ=='duplicate':changed=original.replace(b'{',b'{"schema":"wrong",',1)
            else:
                d=json.loads(original)
                if typ=='schema':d['schema']='wrong'
                elif typ=='global-claim':d['scope']['new_continuum_gap_established']=True
                elif typ=='formal-claim':d['scope']['analytic_proofs_machine_formalized']=True
                else:d['coefficient_polynomial'][0]['coefficient']='0'
                changed=(json.dumps(d)+'\n').encode()
            p.write_bytes(changed)
            for opt in (False,True):execute('reject-'+typ+'-'+str(opt),fresh,optimized=opt,expected_error=error)
            p.write_bytes(original)
        data=execute('restored-source-final-replay',fresh)
        if data!=expected:raise RuntimeError('restored result differs')
    record={'schema':'ym-audit-observed-execution-v1','complete_receipt_sha256':sha(expected),'records':records,
            'full_calculation_runs':5,'intentional_corruption_runs':16,'ordinary_optimized_identical':True,
            'fresh_copy_identical':True,'written_analytic_proofs_formalized':False,'prior_unavailable_session_receipts_replayed':False,
            'remote_changes_performed':False,'remote_CI_run':False,'paid_model_run':False}
    output.write_text(json.dumps(record,indent=2,sort_keys=True)+'\n')
    print('COMPLETE REPLAY PASS',len(records),flush=True)

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,default=ROOT/'results/execution.json');args=ap.parse_args()
    try:run_all(args.output)
    except (OSError,RuntimeError,subprocess.TimeoutExpired) as e:raise SystemExit('Replay failed: '+str(e))
if __name__=='__main__':main()
