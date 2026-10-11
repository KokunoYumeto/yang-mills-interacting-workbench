"""Replay the exact fourth-return mathematics using only retained local files."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,subprocess,sys,time
ROOT=Path(__file__).resolve().parent
start=time.monotonic()
for receipt in json.loads((ROOT/'VERIFICATION_SOURCE_RECEIPTS.json').read_text()):
    actual=hashlib.sha256((ROOT/receipt['retained_file']).read_bytes()).hexdigest()
    assert actual==receipt['sha256'],receipt['retained_file']
scripts=['rederive_projected_rhs.py','check_geometry_coverage.py','direct_return_words.py','fourth_matrix.py','sixth_tail.py','cube_derivation/derive_cube.py','cube_derivation/check_fourth_algebra.py']
results=[]
for script in scripts:
    result=subprocess.run([sys.executable,'-B',str(ROOT/script)],cwd=ROOT,capture_output=True,text=True)
    results.append({'script':script,'exit_code':result.returncode})
    if result.returncode:
        print(result.stdout);print(result.stderr);raise SystemExit(result.returncode)
    print('PASS',script,flush=True)
receipt={'completed_utc':datetime.now(timezone.utc).isoformat(),'source_hashes_match':True,'scripts':results,'elapsed_seconds':time.monotonic()-start,'proof_sha256':hashlib.sha256((ROOT/'FOURTH_SCHUR_COEFFICIENT.md').read_bytes()).hexdigest()}
(ROOT/'REPLAY_RESULT.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8',newline='\n')
print('All exact mathematical replay checks passed.')
