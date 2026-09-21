#!/usr/bin/env python3
"""Replay current and unchanged parent certificates; record actual exits and bytes."""
from __future__ import annotations
import argparse,hashlib,json,subprocess,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parent
PARENT=ROOT.parent/'20260916-cubic-linearized'

def sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def main()->int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--record',type=Path,default=ROOT/'generated'/'replay_execution.json')
    ap.add_argument('--part',choices=['current-ordinary','current-optimized','parent-ordinary','parent-optimized'])
    args=ap.parse_args();records=[];outputs={}
    for label,folder,script,receipt in (
        ('current',ROOT,'verify.py',ROOT/'generated'/'verification.json'),
        ('parent',PARENT,'verify.py',PARENT/'verification.json')):
        for optimized in (False,True):
            runlabel=label+('-optimized' if optimized else '-ordinary')
            if args.part and args.part!=runlabel:continue
            options=['-O','-B'] if optimized else ['-B']
            command=[sys.executable,*options,script,'--verify-receipt',str(receipt)]
            start=time.monotonic();p=subprocess.run(command,cwd=folder,capture_output=True)
            record={'label':label+('-optimized' if optimized else '-ordinary'),
                'command':['python',*options,script,'--verify-receipt',str(receipt.relative_to(folder))],
                'exit_code':p.returncode,'elapsed_seconds':time.monotonic()-start,
                'stdout_sha256':sha(p.stdout),'stderr_sha256':sha(p.stderr)}
            records.append(record);outputs[(label,optimized)]=p.stdout
            print(record['label'],p.returncode,record['stdout_sha256'],flush=True)
            if p.returncode:
                record['stderr']=p.stderr.decode(errors='replace')
                args.record.parent.mkdir(parents=True,exist_ok=True)
                args.record.write_text(json.dumps({'passed':False,'records':records},sort_keys=True,indent=2)+'\n')
                return 1
    complete=not args.part
    equal=all(outputs[(label,False)]==outputs[(label,True)] for label in ('current','parent')) if complete else None
    data={'schema':'ym-quartic-replay-v1','passed':all(r['exit_code']==0 for r in records) and equal is not False,'python':sys.version,
          'normal_optimized_mathematical_bytes_equal':equal,'records':records,
          'scope':'Executed finite original-coordinate certificates; analytic arguments remain written proofs.'}
    args.record.parent.mkdir(parents=True,exist_ok=True)
    args.record.write_text(json.dumps(data,sort_keys=True,indent=2)+'\n')
    return 0 if data['passed'] else 1
if __name__=='__main__':raise SystemExit(main())
