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
registry = json.loads((HERE/'checks/replay_registry.json').read_text(encoding='utf-8'))
scripts = [item['script'] for item in registry['replays']]
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
result = subprocess.run([sys.executable, str(HERE/'checks/static_reference_check.py')], cwd=HERE,
                        capture_output=True, text=True, encoding='utf-8')
(HERE/'checks'/'static_reference_check.log').write_text(result.stdout+result.stderr, encoding='utf-8')
operations.append(dict(kind='static_reference_check', exit_code=result.returncode))
if result.returncode:
    raise RuntimeError('Static reference check failed.')
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
files += [HERE/'checks/replay_registry.json']
files += [HERE/item['receipt'] for item in registry['replays']]
files += [HERE/'checks/static_reference_check.py', HERE/'checks/static_reference_receipt.json']
files += [HERE/'build_and_verify.py', HERE/'build_integration.py']
integration_manifest = json.loads((HERE/'integration_manifest.json').read_text(encoding='utf-8'))
files += [HERE/item['file'] for item in integration_manifest['input_sections']]
for item in integration_manifest.get('assets', []):
    files += [HERE/item['source'], HERE/item['integration']]
files += [HERE/rel for rel in (
    'coupled_viscous_control.tex',
    'paper_coupling/profile_diffusion/profile_diffusion_preamble.tex',
    'integration/coupled_viscous_control_body.tex',
    'integration/coupled_viscous_control_preamble.tex',
    'integration/integration_check.tex', 'integration_manifest.json')]
files += [HERE/'sources'/'alpoge_buckmaster_boussinesq.pdf']
if not args.skip_pdf:
    files += [HERE/'coupled_viscous_control.pdf', HERE/'integration/integration_check.pdf']
receipt = dict(schema='coupled-viscous-control-build-v1', all_passed=True,
               operations=operations,
               files_sha256={p.relative_to(HERE).as_posix():sha(p) for p in files},
               lean_used=False,
               proved_scope=integration_manifest['mathematics_scope'],
               infinite_viscous_sequence_proved=False)
(HERE/'checks'/'build_receipt.json').write_text(json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(dict(all_passed=True, operations=len(operations),
                     receipt='checks/build_receipt.json')))
