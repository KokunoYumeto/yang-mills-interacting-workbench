"""Bounded, versioned source comparison; retain untouched Poppler text."""
from pathlib import Path
import hashlib
import json
import re
import subprocess

HERE = Path(__file__).resolve().parent
LANE = HERE.parents[1]
PROGRAM = LANE.parents[1]
POPPLER = Path('<user-root>/.cache/codex-runtimes/codex-primary-runtime/dependencies/native/poppler/Library/bin')
PDFTOTEXT = Path('<user-root>/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe')
PDFS = {
    'old_165p': (LANE / 'ns_bridge/openai_navier_stokes.pdf', '8c8a94ad9ac824c8b605b9827cadf7beaca48bd10b380de3cfc872a2c37afa81'),
    'new_166p': (PROGRAM / 'downloaded_public_release/navier-stokes.pdf', '0e779481c4da40bd28d1e642e1d8ca57447d129610df28dfa5a11e9af8ae228f'),
}
TARGETS = [f'7.{i}' for i in list(range(2,9))+list(range(22,43))]+[f'9.{i}' for i in range(12,15)]
EXTRA_CITATIONS = [f'7.{i}' for i in range(12,22)]+['9.1','9.2']
receipt = {'scope':'Only equations 7.2-7.8, 7.22-7.42, 9.12-9.14 and source page attributions used by the local bridges; no full-manuscript equivalence claim.', 'versions':{}}
for key,(pdf,expected) in PDFS.items():
    digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
    if digest!=expected:
        raise ValueError((key,'hash mismatch',digest,expected))
    dest=HERE/f'{key}_poppler_layout.txt'
    subprocess.run([str(PDFTOTEXT),'-layout','-enc','UTF-8',str(pdf),str(dest)],check=True)
    raw=dest.read_bytes()
    text=raw.decode('utf-8')
    pages=text.split('\f')
    if pages[-1]=='': pages.pop()
    matches={}
    for label in TARGETS+EXTRA_CITATIONS:
        candidates=[]
        pattern=re.compile(r'\('+re.escape(label)+r'\)\s*$')
        for pno,page in enumerate(pages,1):
            for lno,line in enumerate(page.splitlines(),1):
                if pattern.search(line):
                    candidates.append({'pdf_page':pno,'line':lno,'exact_line':line})
        matches[label]=candidates
    receipt['versions'][key]={'pdf':str(pdf),'pdf_sha256':digest,'bytes':pdf.stat().st_size,'pdfinfo':subprocess.check_output([str(POPPLER/'pdfinfo.exe'),str(pdf)],text=True),'text_sha256':hashlib.sha256(raw).hexdigest(),'poppler_pages':len(pages),'equation_occurrences':matches}
(HERE/'extraction_receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
for key,v in receipt['versions'].items():
    print(key,v['pdf_sha256'],v['poppler_pages'])
    for eq,occ in v['equation_occurrences'].items():
        print(eq,[(o['pdf_page'],o['line']) for o in occ])
