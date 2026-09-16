#!/usr/bin/env python3
"""Verify imported Yang-Mills source identities and transcript-extract closure.

This checks source provenance and packaging integrity, not mathematical truth.
No network access, Lean invocation, source mutation or subprocess is used.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
EDITION = ROOT / 'yang-mills/consolidation/20260916'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def checked_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT.resolve()):
        raise ValueError('path escapes repository: ' + relative)
    if not path.is_file():
        raise ValueError('missing file: ' + relative)
    return path


def main():
    intake = json.loads((EDITION / 'provenance/SOURCE_INTAKE.json').read_text(encoding='utf-8'))
    pinned = {}
    for record in intake['file_origins']:
        if 'origin' not in record:
            continue
        rel = record['destination']
        path = checked_path(rel)
        if digest(path) != record['sha256'] or path.stat().st_size != record['bytes']:
            raise ValueError('imported source identity mismatch: ' + rel)
        if rel in pinned and pinned[rel] != record['sha256']:
            raise ValueError('conflicting origin records: ' + rel)
        pinned[rel] = record['sha256']
    delivery = json.loads((EDITION / 'transcript-mathematics/DELIVERY_MAP.json').read_text(encoding='utf-8'))
    for record in delivery['responses']:
        path = EDITION / 'transcript-mathematics' / record['extracted_file']
        if digest(path) != record['sha256'] or path.stat().st_size != record['bytes']:
            raise ValueError('transcript extraction mismatch: ' + record['extracted_file'])
    result = {
        'schema': 'ym-consolidation-integrity-v1',
        'source_destinations_verified': len(pinned),
        'full_response_extractions_verified': len(delivery['responses']),
        'baseline_commit': intake['baseline_commit'],
        'mathematical_truth_certified': False,
        'result': 'pass',
    }
    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == '__main__':
    main()
