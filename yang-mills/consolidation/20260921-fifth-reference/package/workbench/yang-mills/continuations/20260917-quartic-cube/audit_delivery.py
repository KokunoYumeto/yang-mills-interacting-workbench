#!/usr/bin/env python3
"""Fresh-copy and intended-failure tests for the delivered certificate.
These tests exercise the checker, not the analytical proofs.
"""
from __future__ import annotations
import argparse,hashlib,json,shutil,subprocess,sys,tempfile,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent/'20260916-cubic-linearized'

def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--phase',required=True,choices=['copy','negative','mathematical-negative'])
    ap.add_argument('--optimized',action='store_true')
    ap.add_argument('--record',type=Path,required=True)
    args=ap.parse_args();records=[]
    with tempfile.TemporaryDirectory(prefix='ym-original-replay-') as tmp:
        base=Path(tmp);now=base/ROOT.name
        shutil.copytree(ROOT,now,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        shutil.copytree(PARENT,base/PARENT.name,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
        receipt=now/'generated'/'verification.json';original_receipt=receipt.read_bytes()
        options=['-O','-B'] if args.optimized else ['-B']
        def run(label,expected=None):
            start=time.monotonic();p=subprocess.run([sys.executable,*options,'verify.py','--verify-receipt','generated/verification.json'],cwd=now,capture_output=True)
            text=p.stderr.decode(errors='replace')
            passed=p.returncode==0 if expected is None else p.returncode==1 and ('FAIL: '+expected) in text
            records.append({'label':label,'optimized':args.optimized,'exit_code':p.returncode,'expected_named_failure':expected,'passed':passed,'elapsed_seconds':time.monotonic()-start,'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr),'stderr':text})
            if not passed:raise RuntimeError('unexpected checker result: '+label+' '+text)
        if args.phase=='copy':run('fresh-copy-replay')
        elif args.phase=='mathematical-negative':
            d=json.loads(original_receipt);d['counts']['exact_checks']+=1
            receipt.write_text(json.dumps(d,sort_keys=True,indent=2)+'\n')
            run('altered-mathematical-count','mathematical-receipt-mismatch');receipt.write_bytes(original_receipt)
        else:
            d=json.loads(original_receipt);d['schema']='false-schema';receipt.write_text(json.dumps(d));run('wrong-schema','receipt-schema');receipt.write_bytes(original_receipt)
            receipt.write_text('{"schema":"ym-quartic-cube-v1",'+original_receipt.decode().lstrip()[1:]);run('duplicate-key','duplicate-json-key:schema');receipt.write_bytes(original_receipt)
            d=json.loads(original_receipt);d['source_sha256'].pop('series.py');receipt.write_text(json.dumps(d));run('missing-source-entry','source-manifest-membership');receipt.write_bytes(original_receipt)
            d=json.loads(original_receipt);d['generated_sha256'].pop('quartic_spin_budgets.json');receipt.write_text(json.dumps(d));run('missing-table-entry','table-manifest-membership');receipt.write_bytes(original_receipt)
            for name,expected in [('PHYSICAL_RETURN.md','source-identity:PHYSICAL_RETURN.md'),('generated/quartic_spin_budgets.json','table-identity:quartic_spin_budgets.json')]:
                p=now/name;raw=p.read_bytes()
                try:
                    p.write_bytes(raw+b'\n');run('changed-bytes:'+name,expected)
                finally:p.write_bytes(raw)
            need=all(sha((now/name).read_bytes())==h for name,h in json.loads(original_receipt)['source_sha256'].items())
            if not need:raise RuntimeError('failed source restoration')
    data={'schema':'ym-quartic-delivery-audit-v1','passed':all(r['passed'] for r in records),'phase':args.phase,'optimized':args.optimized,'runner_sha256':sha(Path(__file__).read_bytes()),'original_receipt_sha256':sha(original_receipt),'records':records}
    args.record.parent.mkdir(parents=True,exist_ok=True);args.record.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    print(json.dumps({'passed':data['passed'],'phase':args.phase,'optimized':args.optimized,'executions':len(records)}));return 0
if __name__=='__main__':raise SystemExit(main())
