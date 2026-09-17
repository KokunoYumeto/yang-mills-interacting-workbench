"""Replay the unchanged tangent verifier; normalize only receipt path separators."""
from __future__ import annotations
import argparse
import contextlib
import importlib.util
import io
import json
from pathlib import Path
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--package-root', type=Path, required=True)
    args = ap.parse_args()
    root = args.package_root.resolve()
    spec = importlib.util.spec_from_file_location('preserved_tangent_verifier', root/'checks/verify_signed_tangent.py')
    original = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(original)
    expected = json.loads((root/'results/signed_tangent.json').read_text())
    output = io.StringIO()
    sys.argv = [str(root/'checks/verify_signed_tangent.py'), '--progress']
    with contextlib.redirect_stdout(output):
        original.main()
    fresh = json.loads(output.getvalue())
    fresh['source_sha256'] = {key.replace('\\', '/'): value for key, value in fresh['source_sha256'].items()}
    if fresh != expected:
        raise ArithmeticError('tangent-receipt-mismatch-after-path-normalization')
    count_zero = sum(not any(row['coupling_multiindex']) for item in fresh['results'] for row in item['signed_tangent_identities'])
    print(json.dumps({'schema':'ym-portable-tangent-replay-v1', 'passed':True,
                      'original_verifier_unmodified':True, 'normalized_path_separators_only':True,
                      'complete_receipt_equal_after_path_normalization':True,
                      'classes':fresh['classes'],
                      'zero_polynomial_tangent_identities':fresh['zero_polynomial_tangent_identities'],
                      'degree_zero_identities_including_minus_W':count_zero,
                      'positive_degree_zero_residuals':fresh['zero_polynomial_tangent_identities']-count_zero,
                      'explicit_degree_three_response_entries':fresh['explicit_degree_three_response_entries'],
                      'freshly_verified_source_sha256':fresh['source_sha256']}, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
