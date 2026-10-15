"""Check the reading PDF and the explicitly listed editable-source package."""
from pathlib import Path, PurePosixPath
import hashlib,json,zipfile
ROOT=Path(__file__).resolve().parent
ARCHIVE_SHA256='623e0e226e1e8b3198cc5168be57e953ec6b6bec32a509df2a5ce93f7f724b8a'
PDF_SHA256='702b7aa1538d4d9648bae41385654a74aeacf21ab86b42182e745496f9c8bebe'
def sha(b):return hashlib.sha256(b).hexdigest()
def main():
    source=ROOT/'upstream';manifest=(ROOT/'PACKAGE_MANIFEST.sha256').read_bytes();rows={}
    for line in manifest.decode().splitlines():
        if not line or line.startswith('#'):continue
        digest,size,name=line.split('\t',2);p=PurePosixPath(name)
        assert not p.is_absolute() and '..' not in p.parts and '\\' not in name
        assert name not in rows
        data=(source/name).read_bytes();assert len(data)==int(size) and sha(data)==digest,name
        rows[name]=digest
    archive=ROOT/'full-source-release.zip';assert sha(archive.read_bytes())==ARCHIVE_SHA256
    with zipfile.ZipFile(archive) as package:
        names=package.namelist();assert len(names)==len(set(names))
        assert set(names)==set(rows)|{'MANIFEST.sha256'}
        assert package.read('MANIFEST.sha256')==manifest
        for name in rows:assert package.read(name)==(source/name).read_bytes(),name
    assert sha((source/'output/pdf/source-faithful-reconstruction.pdf').read_bytes())==PDF_SHA256
    print(json.dumps({'status':'passed','package_files':len(names),'exact_archive_source_match':True,'scope':'Package identities only; no fidelity or theorem certificate'}))
if __name__=='__main__':main()
