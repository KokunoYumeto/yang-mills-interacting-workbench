"""Render the local section preview with Poppler; make full-page pairs."""
from pathlib import Path
import hashlib
import json
import subprocess
from PIL import Image, ImageDraw
import fitz

HERE=Path(__file__).resolve().parent
QA=HERE/'qa'
QA.mkdir(exist_ok=True)
pdf=HERE/'standalone.pdf'
subprocess.run(['pdftoppm','-r','110','-png',str(pdf),str(QA/'page')],check=True)
pages=sorted(QA.glob('page-*.png'))
pairs=[]
for start in range(0,len(pages),2):
    group=[Image.open(p).convert('RGB') for p in pages[start:start+2]]
    pair=Image.new('RGB',(sum(im.width for im in group),max(im.height for im in group)+32),'#ddd')
    draw=ImageDraw.Draw(pair)
    x=0
    for off,im in enumerate(group):
        draw.text((x+12,10),f'Local section page {start+off+1}',fill='black')
        pair.paste(im,(x,32))
        x+=im.width
    dest=QA/f'pair-{start//2+1}.png'
    pair.save(dest)
    pairs.append(str(dest))
doc=fitz.open(pdf)
outside=[]
for i,page in enumerate(doc):
    for word in page.get_text('words'):
        if word[0]<0 or word[1]<0 or word[2]>page.rect.width or word[3]>page.rect.height:
            outside.append({'page':i+1,'word':word[4],'box':list(word[:4])})
record={'pdf_sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'pages':len(doc),'renderer':'pdftoppm','dpi':110,
        'page_images':[str(p) for p in pages],'page_pairs':pairs,
        'out_of_page_text':outside,'visual_review':'pending'}
(QA/'render_receipt.json').write_text(json.dumps(record,indent=2)+'\n',encoding='utf-8')
print(json.dumps(record,indent=2))
