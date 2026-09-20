"""Verify the complete pinned public reconstruction without executing its code."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import zipfile

ROOT = Path(__file__).resolve().parent
ARCHIVE_SHA256 = '997e825e34fa825d189bd301edaa6251e5505710fe294bec99c83a9712558e4c'
PDF_SHA256 = '67bca97d638868c2fcb34b0ef1acdc4918cfcbb1a210afe98f0019a3c93fe8d9'


def require(condition, message):
    if not condition:
        raise RuntimeError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    source = ROOT / 'upstream'
    rows = {}
    for line in (source / 'MANIFEST.sha256').read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#'):
            continue
        digest, size, name = line.split('\t', 2)
        path = PurePosixPath(name)
        require(not path.is_absolute() and '..' not in path.parts and '\\' not in name,
                'Unsafe manifest path')
        require(name not in rows, 'Duplicate manifest path: ' + name)
        data = (source / name).read_bytes()
        require(len(data) == int(size) and sha(data) == digest, 'Source differs: ' + name)
        rows[name] = digest
    archive = ROOT / 'full-source-release.zip'
    require(sha(archive.read_bytes()) == ARCHIVE_SHA256, 'Archive identity differs')
    with zipfile.ZipFile(archive) as package:
        entries = [entry for entry in package.infolist() if not entry.is_dir()]
        names = {entry.filename for entry in entries}
        require(len(entries) == len(names), 'Duplicate archive path')
        require(names == set(rows) | {'MANIFEST.sha256'}, 'Archive/manifest file set differs')
        for entry in entries:
            require(package.read(entry) == (source / entry.filename).read_bytes(),
                    'Extracted file differs: ' + entry.filename)
    actual = {p.relative_to(source).as_posix() for p in source.rglob('*') if p.is_file()}
    require(actual == names, 'Unexpected file in preserved snapshot')
    require(sha((source/'output/pdf/source-faithful-reconstruction.pdf').read_bytes()) == PDF_SHA256,
            'PDF identity differs')
    print(json.dumps({'status':'passed', 'source_commit':'5e162f34cd2d3581f890660e81fbf063509085d0',
                      'manifest_files':len(rows), 'complete_snapshot_files':len(names),
                      'archive_sha256':ARCHIVE_SHA256, 'pdf_sha256':PDF_SHA256,
                      'scope':'File identities and complete mirror; no rebuild or mathematical re-audit.'}, indent=2))


if __name__ == '__main__':
    main()
