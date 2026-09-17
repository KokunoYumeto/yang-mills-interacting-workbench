"""Portable replay of the preserved verifier, without requiring a raw transcript.

Default public mode excludes only input/Pasted markdown(6).md from fresh source
hash verification and records that exception explicitly. Its historical hash is
not a fresh provenance check. --include-private-provenance also hashes that file
for a strict local replay. No supplied file or historical receipt is modified.
"""
from __future__ import annotations
import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import sys

EXCLUDED = 'input/Pasted markdown(6).md'


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--package-root', type=Path, required=True)
    ap.add_argument('--include-private-provenance', action='store_true')
    ap.add_argument('--progress', action='store_true')
    args = ap.parse_args()
    root = args.package_root.resolve()
    path = root/'checks/verify.py'
    spec = importlib.util.spec_from_file_location('preserved_catalogue_verifier', path)
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    saved = original.load(root/'results/verification.json')
    original.require(saved.get('schema') == 'ym-audit-completion-verification-v1', 'receipt-schema')
    inputs = [root/'recovered/geometry.py', path, root/'proofs/FOURTH_ORDER_SOURCE.md', root/'proofs/SIXTH_ORDER_ENERGY.md']
    inputs += sorted((root/'calculations').glob('*.py'))
    if args.include_private_provenance:
        inputs += [root/EXCLUDED]
    sources = {p.relative_to(root).as_posix(): original.digest(p) for p in inputs}
    expected_sources = saved['source_sha256']
    excluded = set() if args.include_private_provenance else {EXCLUDED}
    original.require(set(sources) == set(expected_sources)-excluded, 'source-inventory-mismatch')
    for name, sha in sources.items():
        original.require(sha == expected_sources[name], 'source-identity-mismatch:'+name)
    result = original.main_checks(args.progress)
    fresh = {'schema':'ym-audit-completion-verification-v1', 'passed':True,
             'scope':{'finite_exact_polynomial_identities':True, 'original_link_regressions':True,
                      'inherited_scalar_arithmetic_checked':True,
                      'inherited_analytic_gap_proof_independently_certified':False,
                      'analytic_proofs_machine_formalized':False, 'new_continuum_gap_established':False,
                      'vacuum_sampling':False, 'finite_spin_cutoff_of_full_Hamiltonian':False},
             'counts':{'named_checks':len(original.CHECKS), 'false_formula_controls':len(original.NEGATIVE)},
             'results':result, 'checks':original.CHECKS, 'negative_controls':original.NEGATIVE}
    original.require(fresh == {k:v for k,v in saved.items() if k != 'source_sha256'}, 'complete-mathematical-receipt-mismatch')
    fresh['source_sha256'] = sources
    record = {'schema':'ym-public-portable-replay-v1', 'passed':True,
              'original_verifier_unmodified':True,
              'historical_receipt_sha256':original.digest(root/'results/verification.json'),
              'all_mathematical_receipt_fields_exactly_equal':True,
              'freshly_verified_source_sha256':sources,
              'excluded_provenance_inputs':[{'path':name, 'historical_sha256':expected_sources[name],
                                             'freshly_checked':False,
                                             'reason':'Raw input transcript is excluded from the public edition; it is not read by main_checks.'}
                                            for name in sorted(excluded)],
              'reproduced_record':fresh}
    print(json.dumps(record, indent=2, sort_keys=True))


if __name__ == '__main__':
    try:
        main()
    except (ArithmeticError, RuntimeError, OSError, ValueError) as exc:
        raise SystemExit('FAIL: '+str(exc))
