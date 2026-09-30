"""Verify the exact standalone proof and record completed visual review."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re
import fitz

HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
pdf=HERE/'standalone.pdf'
body=HERE/'third_transition_spatial_body.tex'
log=(HERE/'standalone.log').read_text(errors='replace')
warnings=[l for l in log.splitlines() if any(s in l for s in ['Warning','Overfull','Underfull','Undefined'])]
doc=fitz.open(pdf)
outside=[]
for n,page in enumerate(doc):
    for block in page.get_text('dict')['blocks']:
        for line in block.get('lines',[]):
            for span in line['spans']:
                r=fitz.Rect(span['bbox'])
                if r.x0<0 or r.y0<0 or r.x1>page.rect.width or r.y1>page.rect.height:
                    outside.append({'page':n+1,'text':span['text'],'bounds':list(r)})
pngs=sorted((HERE/'qa').glob('page-*.png'))
assert len(pngs)==len(doc)==10
assert not warnings, warnings
assert not outside, outside
replay=json.loads((HERE/'replay_receipt.json').read_text())
assert replay['all_passed'] and replay['checks_total']==34
assert replay['source_sha256']['third_transition_spatial_body.tex']==sha(body)
labels=re.findall(r'\\label\{(tts:[^}]+)\}',body.read_text())
assert len(labels)==len(set(labels))
receipt={
 'generated_at':datetime.now(timezone.utc).isoformat(),
 'pages':len(doc),'body_sha256':sha(body),'pdf_sha256':sha(pdf),
 'standalone_tex_sha256':sha(HERE/'standalone.tex'),
 'latex_log_sha256':sha(HERE/'standalone.log'),
 'replay_receipt_sha256':sha(HERE/'replay_receipt.json'),
 'primary_checks':34,'primary_all_passed':True,
 'labels_count':len(labels),'labels':labels,
 'latex_warnings':warnings,'text_out_of_page':outside,
 'rendering':{'tool':'pdftoppm','dpi':100,'images':{p.name:sha(p) for p in pngs}},
 'visual_review':{'reviewer':'third_transition_spatial agent','pages_inspected':list(range(1,len(doc)+1)),
   'method':'All ten rendered pages inspected as five full-resolution two-page contact sheets.',
   'clipping':False,'overlap':False,'illegible_equations':False,'bad_page_breaks':False},
 'scope':'Complete added spatial proof through actual third transition; no third-return claim.'
}
(HERE/'qa_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:receipt[k] for k in ['pages','body_sha256','pdf_sha256','primary_checks','labels_count']}))
