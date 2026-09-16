#!/usr/bin/env python3
"""Build the cumulative available Yang-Mills source packet, without prior ZIPs.

Includes every ordinary Yang-Mills file, the local S6 companion, and portable
builder/integrity tools. Excludes Git internals, caches, build intermediates,
this output ZIP and its receipt. Raw missing attachments are not invented.
"""
from pathlib import Path
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parents[1]
EDITION = ROOT / 'yang-mills/consolidation/20260916'
OUTPUT = EDITION / 'yang_mills_complete_available_sources_20260916.zip'
RECEIPT = EDITION / 'PACKAGE_MANIFEST.json'


def main():
    paths = []
    for base in (ROOT / 'yang-mills', ROOT / 's6'):
        for path in base.rglob('*'):
            if not path.is_file() or any(p in ('.build', '__pycache__') for p in path.parts):
                continue
            if path.suffix.lower() == '.zip' or path == RECEIPT:
                continue
            paths.append(path)
    paths += [ROOT / 'tools' / name for name in (
        'build_ym_continuation_reader.py', 'verify_ym_consolidation.py',
        'package_ym_consolidation.py')]
    payload = {path.relative_to(ROOT).as_posix(): path.read_bytes()
               for path in sorted(paths)}
    payload['README.md'] = (
        '# Complete available Yang-Mills source packet, 16 September 2026\n\n'
        'Start at yang-mills/consolidation/20260916/README.md. The 297-page '
        'PDF, editable TeX, full available source notes, foundation papers, '
        'scoped checkers, historical receipts, fresh validation and bounded '
        'mathematical reviews are included. Earlier downloaded ZIPs are not '
        'needed for the available mathematical source closure.\n\n'
        'SOURCE_COVERAGE.md records the four missing attachment families; '
        'their absence is not hidden by the word cumulative. FOLLOWUP_PROMPT.md '
        'is the prepared source-recovery and unfinished-continuation prompt. '
        'The s6/ directory preserves the repository companion referenced by '
        'the early refinement note; its externally hosted full archive is '
        'identified by its existing guide. No private transcript or credential '
        'is included.\n\n'
        'Run python -B tools/verify_ym_consolidation.py for source identity. '
        'Read the reader README for Pandoc/XeLaTeX build dependencies, and '
        'VALIDATION.md for original Linux/WSL replay commands and scope. '
        'PACKET_CONTENTS.json lists every other ZIP member and its SHA-256.\n'
    ).encode('utf-8')
    inventory = [{'path': name, 'bytes': len(data),
                  'sha256': hashlib.sha256(data).hexdigest()}
                 for name, data in sorted(payload.items())]
    payload['PACKET_CONTENTS.json'] = (json.dumps({
        'schema': 'ym-cumulative-packet-v1',
        'scope': 'Complete available repository source closure; explicit missing-attachment list retained.',
        'excluded': ['prior nested ZIPs', 'build intermediates', 'Git internals',
                     'this packet and its outer receipt', 'private source transcript'],
        'files': inventory,
    }, indent=2, ensure_ascii=False) + '\n').encode('utf-8')
    with zipfile.ZipFile(OUTPUT, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, data in sorted(payload.items()):
            info = zipfile.ZipInfo(name, date_time=(2026, 9, 16, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)
    with zipfile.ZipFile(OUTPUT) as archive:
        if archive.testzip() is not None:
            raise ValueError('ZIP CRC failure')
        for row in inventory:
            data = archive.read(row['path'])
            if len(data) != row['bytes'] or hashlib.sha256(data).hexdigest() != row['sha256']:
                raise ValueError('ZIP member identity mismatch: ' + row['path'])
    result = {'schema': 'ym-cumulative-packet-receipt-v1',
              'filename': OUTPUT.name, 'bytes': OUTPUT.stat().st_size,
              'sha256': hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),
              'members': len(payload), 'member_hashes_verified': len(inventory),
              'file_inventory': inventory}
    RECEIPT.write_text(json.dumps(result, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'file_inventory'}, indent=2))


if __name__ == '__main__':
    main()
