from pathlib import Path
import subprocess,hashlib,json
from PIL import Image,ImageOps,ImageDraw
import fitz
root=Path(__file__).resolve().parent
pdfs=['axisymmetric_operator_bridge_reader.pdf','pulse_comparison/pulse_comparison.pdf',
      'covariance_bridge/covariance_bridge.pdf','source_bridge_reader.pdf']
out=root/'qa_final';out.mkdir(exist_ok=True)
records=[]
for name in pdfs:
    pdf=root/name; slug=pdf.stem
    dest=out/slug;dest.mkdir(exist_ok=True)
    subprocess.run(['pdftoppm','-png','-r','100',str(pdf),str(dest/'page')],check=True,capture_output=True)
    pages=sorted(dest.glob('page-*.png'),key=lambda p:int(p.stem.split('-')[-1]))
    pairs=[]
    for start in range(0,len(pages),2):
        ims=[Image.open(p).convert('RGB') for p in pages[start:start+2]]
        sheet=Image.new('RGB',(sum(i.width for i in ims)+30*(len(ims)+1),max(i.height for i in ims)+70),'#dddddd')
        draw=ImageDraw.Draw(sheet); x=30
        for p,im in zip(pages[start:start+2],ims):
            draw.text((x,12),slug+' / '+p.stem,fill='black')
            sheet.paste(im,(x,40));x+=im.width+30
        target=dest/f'contact-{start//2+1:02}.png';sheet.save(target)
        pairs.append(str(target.relative_to(root)))
    doc=fitz.open(pdf)
    overflow=[]
    for j,page in enumerate(doc):
        for block in page.get_text('dict')['blocks']:
            for line in block.get('lines',[]):
                for sp in line['spans']:
                    x0,y0,x1,y1=sp['bbox']
                    if x0 < 0 or y0 < 0 or x1 > page.rect.width+0.01 or y1 > page.rect.height+0.01:
                        overflow.append(dict(page=j+1,text=sp['text'],bbox=sp['bbox']))
    assert not overflow,(name,overflow)
    records.append(dict(pdf=name,sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),
                        pages=len(doc),contacts=pairs,text_outside_page=overflow))
(out/'render_receipt.json').write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
