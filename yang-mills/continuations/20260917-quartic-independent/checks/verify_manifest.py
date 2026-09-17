#!/usr/bin/env python3
"""Verify every declared session artifact; permit newly generated replay files."""
from pathlib import Path
import hashlib,json,sys
ROOT=Path(__file__).resolve().parents[1]
def main():
    try:
        manifest=json.loads((ROOT/'SHA256_MANIFEST.json').read_text())
        for name,meta in manifest['files'].items():
            relative=Path(name)
            if relative.is_absolute() or '..' in relative.parts:raise ValueError('unsafe manifest path')
            p=ROOT/relative
            if p.is_symlink() or not p.is_file():raise ValueError('missing/linked artifact: '+name)
            data=p.read_bytes()
            if len(data)!=meta['bytes'] or hashlib.sha256(data).hexdigest()!=meta['sha256']:
                raise ValueError('artifact mismatch: '+name)
        print('PASS:',len(manifest['files']),'declared session artifacts match their original bytes.')
        return 0
    except (OSError,ValueError,KeyError) as e:
        sys.stderr.write('FAIL: '+str(e)+'\n');return 1
if __name__=='__main__':raise SystemExit(main())
