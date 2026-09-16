#!/usr/bin/env python3
"""Replay the exact current and predecessor certificates, with corruption controls.

Standard library only. The receipt records observed subprocess exit codes and
byte identities; it does not turn finite regressions into an analytic proof.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent

def require(ok: bool, code: str) -> None:
    if not ok: raise ValueError(code)

def sha(b:bytes)->str:return hashlib.sha256(b).hexdigest()
def canon(x)->bytes:return (json.dumps(x,sort_keys=True,indent=2)+'\n').encode()

def main()->None:
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--parent-root',type=Path,default=HERE.parents[2])
    p.add_argument('--output',type=Path,default=HERE/'execution.json')
    args=p.parse_args()
    expected=(HERE/'verification.json').read_bytes()
    box=(HERE/'BOX_L2_CERTIFICATE.json').read_bytes()
    records=[]
    def run(name,script,flags=(),extra=(),error=None,stdout=None):
        command=[sys.executable,*flags,'-B',str(script),*map(str,extra)]
        out=subprocess.run(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=120,
                           env={**os.environ,'PYTHONDONTWRITEBYTECODE':'1'})
        print(name+': '+str(out.returncode),file=sys.stderr,flush=True)
        if error is None:
            require(out.returncode==0,'execution-failed:'+name+':'+out.stderr.decode(errors='replace'))
            require(out.stderr==b'','unexpected-stderr:'+name)
            if stdout is not None:require(out.stdout==stdout,'output-difference:'+name)
        else:
            require(out.returncode==1,'corruption-exit:'+name)
            require(out.stdout==b'','corruption-produced-success-output:'+name)
            require(('FAIL: '+error+'\n').encode()==out.stderr,'wrong-corruption-failure:'+name+':'+out.stderr.decode(errors='replace'))
        records.append({'name':name,'exit_code':out.returncode,'stdout_sha256':sha(out.stdout),
                        'stderr_sha256':sha(out.stderr),'expected_named_error':error})
        return out.stdout
    own_args=['--verify-receipt',HERE/'verification.json','--verify-box-certificate',HERE/'BOX_L2_CERTIFICATE.json']
    for flags,suffix in (((),'ordinary'),(('-O',),'optimized')):
        run('current-'+suffix,HERE/'verify.py',flags,own_args,stdout=expected)
    parent=args.parent_root/'yang-mills/continuations/20260915-uniform-gap-zero-shift'
    require((parent/'verify.py').is_file(),'missing-delivered-parent')
    parent_expected=(parent/'verification.json').read_bytes()
    for flags,suffix in (((),'ordinary'),(('-O',),'optimized')):
        run('unchanged-parent-'+suffix,parent/'verify.py',flags,
            ['--verify-receipt',parent/'verification.json'],stdout=parent_expected)
    with tempfile.TemporaryDirectory(prefix='ym-gauge-replay-') as td:
        root=Path(td);copy=root/'copied-source'
        shutil.copytree(HERE,copy,ignore=shutil.ignore_patterns('__pycache__','execution.json'))
        copied_args=['--verify-receipt',copy/'verification.json','--verify-box-certificate',copy/'BOX_L2_CERTIFICATE.json']
        for flags,suffix in (((),'ordinary'),(('-O',),'optimized')):
            run('copied-source-'+suffix,copy/'verify.py',flags,copied_args,stdout=expected)
        state=json.loads((copy/'state.json').read_bytes())
        mutations=[('target','finite numerical experiment','wrong-target'),
            ('finite_domain','all g>0','wrong-finite-domain'),
            ('spatial_domain','all xi>=0','wrong-spatial-domain'),
            ('continuum_gap_established',True,'unsupported-continuum-promotion'),
            ('band_is_spin_truncation',True,'false-truncation-identification'),
            ('raw_band_metric','I','missing-original-band-Gram')]
        for key,value,error in mutations:
            candidate=root/(key+'.json');new=dict(state);new[key]=value;candidate.write_bytes(canon(new))
            for flags,suffix in (((),'ordinary'),(('-O',),'optimized')):
                run('state-'+key+'-'+suffix,copy/'verify.py',flags,['--candidate-state',candidate],error=error)
        duplicate=root/'duplicate.json';duplicate.write_text('{"target":1,"target":2}\n')
        false_receipt=root/'false-receipt.json';false_receipt.write_text('{}\n')
        bad_box=root/'bad-box.json';altered=json.loads(box);altered['inertia']=[2,238,0];bad_box.write_bytes(canon(altered))
        for flags,suffix in (((),'ordinary'),(('-O',),'optimized')):
            run('duplicate-state-'+suffix,copy/'verify.py',flags,['--candidate-state',duplicate],error='duplicate-json-key:target')
            run('wrong-receipt-'+suffix,copy/'verify.py',flags,['--verify-receipt',false_receipt],error='receipt-mismatch')
            run('wrong-inertia-record-'+suffix,copy/'verify.py',flags,['--verify-box-certificate',bad_box],error='box-certificate-mismatch')
        proof=copy/'SECOND_SOURCE.md';original=proof.read_bytes();proof.write_bytes(original+b'\nAltered source control.\n')
        for flags,suffix in (((),'ordinary'),(('-O',),'optimized')):
            run('modified-proof-'+suffix,copy/'verify.py',flags,copied_args,error='receipt-mismatch')
        proof.write_bytes(original)
        for flags,suffix in (((),'ordinary'),(('-O',),'optimized')):
            run('restored-source-'+suffix,copy/'verify.py',flags,copied_args,stdout=expected)
    receipt=json.loads(expected)
    inputs=['RESEARCH_NOTE.md','BAND_AND_CERTIFICATE.md','SPATIAL_RETURN.md','SECOND_SOURCE.md',
            'verify.py','replay.py','state.json','SOURCE_INTAKE.json','verification.json','BOX_L2_CERTIFICATE.json']
    result={'schema':'ym-gauge-native-observed-execution-v1','records':records,
        'exact_named_checks':len(receipt['checks']),'named_false_formula_controls':len(receipt['negative_controls']),
        'named_cli_corruption_executions':sum(r['expected_named_error'] is not None for r in records),
        'input_sha256':{n:sha((HERE/n).read_bytes()) for n in inputs},
        'parent_receipt_sha256':sha(parent_expected),'ordinary_and_optimized_outputs_identical':True,
        'fresh_source_copy_reproduced':True,'new_Lean_execution':False,'remote_CI_replayed':False,
        'remote_write_performed':False,'analytic_proof_independently_certified':False}
    data=canon(result);args.output.write_bytes(data);sys.stdout.buffer.write(data)

if __name__=='__main__':
    try:main()
    except (ValueError,OSError,subprocess.TimeoutExpired,json.JSONDecodeError) as exc:
        print('FAIL: '+str(exc),file=sys.stderr);raise SystemExit(1)
