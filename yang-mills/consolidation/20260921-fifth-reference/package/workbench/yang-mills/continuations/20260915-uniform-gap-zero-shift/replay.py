#!/usr/bin/env python3
"""Replay the exact current/parent certificates and named CLI corruptions.

Only local selected source files are copied to a temporary directory. No
network access, Git changes, workflow dispatch, paid runs or remote writes.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
REL=HERE.relative_to(ROOT)
PARENT=Path('yang-mills/continuations/20260915-actual-loop-moments')
CONTROL=Path('yang-mills/research-control/check.py')

def need(condition,code):
    if not condition:raise RuntimeError(code)

def digest(data):return hashlib.sha256(data).hexdigest()

def run(root,args):
    proc=subprocess.run([sys.executable,*args],cwd=root,capture_output=True,timeout=90)
    return proc

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',type=Path)
    ap.add_argument('--progress',action='store_true')
    args=ap.parse_args()
    success=[];rejected=[]
    expected=(ROOT/REL/'verification.json').read_bytes()
    oldexpected=(ROOT/PARENT/'verification.json').read_bytes()
    def positive(root,label,folder,flags,wanted):
        if args.progress: print('RUN '+label,file=sys.stderr,flush=True)
        command=[*flags,'-B',str(folder/'verify.py'),'--verify-receipt',str(folder/'verification.json')]
        p=run(root,command)
        need(p.returncode==0,'positive-exit:'+label+':'+p.stderr.decode())
        need(p.stderr==b'','positive-stderr:'+label)
        need(p.stdout==wanted,'positive-content:'+label)
        success.append({'name':label,'argv':command,'exit_code':p.returncode,'stdout_sha256':digest(p.stdout),'stderr_bytes':len(p.stderr)})
    for mode,flags in [('ordinary',[]),('optimized',['-O'])]:
        positive(ROOT,'current-'+mode,REL,flags,expected)
        positive(ROOT,'parent-'+mode,PARENT,flags,oldexpected)
    with tempfile.TemporaryDirectory(prefix='ym-zero-shift-replay-') as tmp:
        fresh=Path(tmp)
        for folder in (REL,PARENT):
            shutil.copytree(ROOT/folder,fresh/folder,ignore=shutil.ignore_patterns('__pycache__','.git'))
        (fresh/CONTROL).parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT/CONTROL,fresh/CONTROL)
        for mode,flags in [('ordinary',[]),('optimized',['-O'])]:
            positive(fresh,'fresh-'+mode,REL,flags,expected)
        state=json.loads((fresh/REL/'state.json').read_text())
        mutations=fresh/'mutation-controls';mutations.mkdir()
        cases=[]
        for name,key,value,code in [
            ('target','target','unrelated target','wrong-target'),
            ('domain','proved_coupling_domain',{'g_squared_min':'1'},'wrong-proved-domain'),
            ('continuum','continuum_gap_established',True,'unsupported-continuum-promotion'),
            ('response','actual_zero_shift_response_enclosed',False,'missing-actual-response'),
            ('volume','fixed_spacing_volume_limit','unexamined continuum claim','wrong-volume-limit-scope')]:
            candidate=dict(state);candidate[key]=value
            filename=mutations/(name+'.json');filename.write_text(json.dumps(candidate))
            cases.append((name,['--candidate-state',str(filename.relative_to(fresh))],code))
        filename=mutations/'duplicate.json';filename.write_text('{"target":"a","target":"b"}')
        cases.append(('duplicate-key',['--candidate-state',str(filename.relative_to(fresh))],'duplicate-json-key:target'))
        filename=mutations/'receipt.json';filename.write_text('{}')
        cases.append(('receipt',['--verify-receipt',str(filename.relative_to(fresh))],'receipt-mismatch'))
        def negative(label,flags,extra,code):
            if args.progress: print('CONTROL '+label,file=sys.stderr,flush=True)
            command=[*flags,'-B',str(REL/'verify.py'),*extra]
            p=run(fresh,command)
            want='FAIL: '+code+'\n'
            need(p.returncode==1,'negative-exit:'+label)
            need(p.stderr.decode()==want,'negative-code:'+label+':'+p.stderr.decode())
            need(p.stdout==b'','negative-stdout:'+label)
            rejected.append({'name':label,'exit_code':p.returncode,'stderr':want.strip(),'stdout_bytes':len(p.stdout)})
        for label,extra,code in cases:
            for mode,flags in [('ordinary',[]),('optimized',['-O'])]:
                negative(label+'-'+mode,flags,extra,code)
        for path,code in [(REL/'RESEARCH_NOTE.md','receipt-mismatch'),(PARENT/'verify.py','predecessor-hash:verify.py')]:
            file=fresh/path;original=file.read_bytes()
            file.write_bytes(original+b'\n# deliberate copied-source corruption\n')
            try:
                for mode,flags in [('ordinary',[]),('optimized',['-O'])]:
                    negative('source:'+str(path)+':'+mode,flags,
                        ['--verify-receipt',str(REL/'verification.json')],code)
            finally:file.write_bytes(original)
        positive(fresh,'restored-after-corruptions',REL,[],expected)
    current=json.loads(expected);parent=json.loads(oldexpected)
    report={'schema':'ym-zero-shift-full-replay-v1','success':True,
        'positive_executions':success,'named_cli_rejections':rejected,
        'current_exact_checks':len(current['exact_checks']),
        'current_false_controls':len(current['negative_controls']),
        'parent_exact_checks':len(parent['finite_checks']),
        'parent_false_controls':len(parent['negative_controls']),
        'current_receipt_sha256':digest(expected),
        'parent_receipt_sha256':digest(oldexpected),
        'replay_source_sha256':digest(Path(__file__).read_bytes()),
        'scope':'Actual local executions and named rejection codes; finite algebra/rational certificates accompany, rather than formally certify, the written analytical proofs.',
        'remote_write_performed':False,'paid_run_performed':False}
    text=json.dumps(report,sort_keys=True,indent=2)+'\n'
    if args.output:args.output.write_text(text)
    sys.stdout.write(text)

if __name__=='__main__':
    try:main()
    except (OSError,ValueError,RuntimeError,subprocess.TimeoutExpired) as exc:
        print('FAIL: '+str(exc),file=sys.stderr);sys.exit(1)
