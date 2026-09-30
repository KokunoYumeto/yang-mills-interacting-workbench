"""Inspect the completed component's reader range and prepare visual sheets.

This is scoped to the new spatial component. The reader's earlier entry section
is owned elsewhere; any layout issues there are recorded and sent to its owner.
"""
from pathlib import Path
import hashlib
import json
import re
import fitz
from PIL import Image, ImageDraw

HERE = Path(__file__).resolve().parent
BUILD = HERE/'audit/preview_build'
pdf = BUILD/'preview.pdf'
doc = fitz.open(pdf)
aux = (BUILD/'preview.aux').read_text(encoding='utf-8')
start = int(re.search(r'\\newlabel\{tgs:section\}\{\{[^}]*\}\{(\d+)\}', aux)[1])
end = len(doc)
log = (BUILD/'preview.log').read_text(encoding='utf-8')
component_log = log.split('(third_growth_spatial/third_growth_spatial_body.tex', 1)[1]
component_log = component_log.split('***********', 1)[0]
bad = re.findall(r'(?:Overfull|Underfull|LaTeX Warning:|Package .* Warning:).*', component_log)
if bad:
    raise AssertionError(bad)
labels = re.findall(r'\\label\{(tgs:[^}]+)\}', (HERE/'third_growth_spatial_body.tex').read_text(encoding='utf-8'))
if len(labels) != len(set(labels)):
    raise AssertionError('Duplicate spatial labels')
bounds = []
for number in range(start, end+1):
    page = doc[number-1]
    for b in page.get_text('dict')['blocks']:
        for line in b.get('lines', []):
            for span in line.get('spans', []):
                if span['text'].strip():
                    rect = fitz.Rect(span['bbox'])
                    if not page.rect.contains(rect):
                        bounds.append({'page': number, 'text': span['text'], 'bbox': list(rect)})
if bounds:
    raise AssertionError(bounds)
files = [BUILD/f'page-{number:02d}.png' for number in range(start,end+1)]
if not all(path.exists() for path in files):
    raise AssertionError('Render every component page first')
for index in range(0,len(files),2):
    ims = [Image.open(p).convert('RGB') for p in files[index:index+2]]
    sheet = Image.new('RGB', (sum(im.width for im in ims), max(im.height for im in ims)+32), '#dddddd')
    draw = ImageDraw.Draw(sheet)
    x = 0
    for im,path in zip(ims, files[index:index+2]):
        sheet.paste(im, (x,32))
        draw.text((x+15,10), path.stem, fill='black')
        x += im.width
    sheet.save(BUILD/f'contact-{index//2+1:02d}.png')
replay = json.loads((HERE/'replay_report.json').read_text(encoding='utf-8'))
body_hash = hashlib.sha256((HERE/'third_growth_spatial_body.tex').read_bytes()).hexdigest()
assert replay['body_sha256'] == body_hash
assert replay['status'] == 'passed' and all(item['passed'] for item in replay['checks'])
receipt = {
    'schema_version':1, 'scope':'Third-growth spatial component, not the full parent release',
    'body_sha256': body_hash,
    'replay_script_sha256': replay['script_sha256'],
    'replay_check_count': replay['check_count'],
    'reader_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'reader_pages':len(doc), 'component_page_range':[start,end],
    'component_label_count':len(labels),
    'component_latex_warnings':bad, 'component_text_out_of_page':bounds,
    'render_tool':'Poppler pdftoppm', 'render_dpi':90,
    'rendered_pages':[{'file':str(p.relative_to(HERE)), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files],
    'visual_review':'pending model inspection',
    'earlier_owner_layout_issues': re.findall(r'Overfull \\hbox.*', log.split('(third_growth_spatial/third_growth_spatial_body.tex', 1)[0]),
}
(HERE/'verification_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k: receipt[k] for k in ['component_page_range','component_label_count','replay_check_count','component_latex_warnings','component_text_out_of_page','earlier_owner_layout_issues']}))
