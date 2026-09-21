#!/usr/bin/env python3
"""Execute recorded heat calculations in both Python modes; retain actual exits.
The output directory should be outside a sealed cumulative archive.
"""
from pathlib import Path
import subprocess,sys,json,time,tempfile,hashlib,argparse
ROOT=Path(__file__).resolve().parent

def hashes():
 return {p.name:hashlib.sha256(p.read_bytes()).hexdigest() for p in (ROOT/'generated').glob('*.json')}
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--fast',action='store_true');ap.add_argument('--output-dir',type=Path);args=ap.parse_args()
 out=args.output_dir or Path(tempfile.mkdtemp(prefix='ym-heat-replay-'));out.mkdir(parents=True,exist_ok=True)
 steps=[]
 if not args.fast:
  steps += [('coefficient',['produce_heat.py','--verify-existing']),('polynomial',['audit_heat_polynomials.py','--verify-existing']),('assembly',['assemble_heat.py'])]
 steps += [('independent',['independent_heat.py']),('bounds',['certified_bounds.py']),('band',['extract_band.py']),('record',['verify.py','--verify-receipt','verification.json'])]
 records=[]
 for name,tail in steps:
  for optimized in (False,True):
   flags=['-O','-B'] if optimized else ['-B'];cmd=[sys.executable,*flags,*tail];tag=name+('-optimized' if optimized else '-ordinary');before=hashes();t=time.monotonic()
   with (out/(tag+'.log')).open('wb') as log:r=subprocess.run(cmd,cwd=ROOT,stdout=log,stderr=subprocess.STDOUT)
   after=hashes();record={'name':tag,'command':['python',*flags,*tail],'returncode':r.returncode,'seconds':time.monotonic()-t,'all_generated_bytes_unchanged':before==after,'log_sha256':hashlib.sha256((out/(tag+'.log')).read_bytes()).hexdigest(),'source_program_sha256':hashlib.sha256((ROOT/tail[0]).read_bytes()).hexdigest()};records.append(record)
   (out/'execution.json').write_text(json.dumps({'schema':'ym-heat-execution-v1','mode':'fast' if args.fast else 'full','records':records},indent=2)+'\n')
   print(tag,r.returncode,'unchanged',before==after,flush=True)
   if r.returncode or before!=after:return 1
 print('COMPLETE',len(records),str(out),flush=True);return 0
if __name__=='__main__':raise SystemExit(main())
