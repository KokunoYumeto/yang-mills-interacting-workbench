"""Portable local replay and LaTeX build; requires Python, SymPy, and pdflatex."""
from pathlib import Path
import argparse
import hashlib
import json
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
parser = argparse.ArgumentParser()
parser.add_argument('--skip-pdf', action='store_true')
args = parser.parse_args()
(HERE/'checks').mkdir(exist_ok=True)
scripts = [
    'replay_exact.py',
    'finite_stage/replay_first_stage.py',
    'paper_coupling/replay_coupled.py',
    'paper_coupling/profile_diffusion/replay_profile_diffusion.py',
    'entry_audit/replay_actual_entry.py',
    'second_return/replay_second_return.py',
    'modified_spatial/replay_spatial.py',
]
operations = []
for i, rel in enumerate(scripts):
    result = subprocess.run([sys.executable, str(HERE/rel)], cwd=HERE,
                            capture_output=True, text=True, encoding='utf-8')
    (HERE/'checks'/f'replay_{i+1}.log').write_text(result.stdout+result.stderr, encoding='utf-8')
    operations.append(dict(kind='exact_replay', file=rel, exit_code=result.returncode))
    if result.returncode:
        raise RuntimeError(f'{rel} failed; inspect checks/replay_{i+1}.log')
result = subprocess.run([sys.executable, str(HERE/'build_integration.py')], cwd=HERE,
                        capture_output=True, text=True, encoding='utf-8')
(HERE/'checks'/'integration_export.log').write_text(result.stdout+result.stderr, encoding='utf-8')
operations.append(dict(kind='integration_export', exit_code=result.returncode))
if result.returncode:
    raise RuntimeError('Integration export failed.')
if not args.skip_pdf:
    latex = shutil.which('pdflatex')
    if not latex:
        raise RuntimeError('pdflatex is required for PDF build; exact replays have completed.')
    for i in range(3):
        result = subprocess.run([latex, '-interaction=nonstopmode', '-halt-on-error',
                                 'coupled_viscous_control.tex'], cwd=HERE,
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
        (HERE/'checks'/f'latex_pass_{i+1}.log').write_text(result.stdout+result.stderr, encoding='utf-8')
        operations.append(dict(kind='latex', pass_number=i+1, exit_code=result.returncode))
        if result.returncode:
            raise RuntimeError(f'LaTeX pass {i+1} failed.')
    log = (HERE/'coupled_viscous_control.log').read_text(encoding='utf-8', errors='replace')
    bad = [s for s in ('Overfull', 'undefined references', 'multiply defined') if s in log]
    if bad:
        raise RuntimeError(f'Final LaTeX log requires inspection: {bad}')
    for i in range(2):
        result = subprocess.run([latex, '-interaction=nonstopmode', '-halt-on-error',
                                 'integration_check.tex'], cwd=HERE/'integration',
                                capture_output=True, text=True, encoding='utf-8', errors='replace')
        (HERE/'checks'/f'integration_latex_pass_{i+1}.log').write_text(result.stdout+result.stderr, encoding='utf-8')
        operations.append(dict(kind='integration_latex', pass_number=i+1, exit_code=result.returncode))
        if result.returncode:
            raise RuntimeError(f'Integration LaTeX pass {i+1} failed.')
    ilog = (HERE/'integration'/'integration_check.log').read_text(encoding='utf-8', errors='replace')
    bad = [s for s in ('Overfull', 'undefined references', 'multiply defined') if s in ilog]
    if bad:
        raise RuntimeError(f'Integration LaTeX log requires inspection: {bad}')

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

files = [HERE/rel for rel in scripts]
files += [p for p in HERE.rglob('*.tex')
          if '.git' not in p.parts and 'releases' not in p.parts]
files += [HERE/'sources'/'alpoge_buckmaster_boussinesq.pdf']
if not args.skip_pdf:
    files += [HERE/'coupled_viscous_control.pdf']
receipt = dict(schema='coupled-viscous-control-build-v1', all_passed=True,
               operations=operations,
               files_sha256={p.relative_to(HERE).as_posix():sha(p) for p in files},
               lean_used=False,
               proved_scope='Complete compact first stage and actual modified two-stage original growth thresholds, evolved-parent second return and hold, explicit positive equal-diffusion range and all compact profile forces/costs; source infinite estimates explicitly attributed.',
               infinite_viscous_sequence_proved=False)
(HERE/'checks'/'build_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(dict(all_passed=True, operations=len(operations),
                     receipt='checks/build_receipt.json')))
