from pathlib import Path
import hashlib
import json
import subprocess
from PIL import Image, ImageChops

HERE=Path(__file__).resolve().parent
extraction=json.loads((HERE/'extraction_receipt.json').read_text(encoding='utf-8'))
targets=[f'7.{i}' for i in list(range(2,9))+list(range(22,43))]+[f'9.{i}' for i in range(12,15)]
rows=[]
for label in targets:
    row={'equation':label,'formula_comparison':'No displayed formula change found by visual review of both complete source pages.'}
    for key,version in extraction['versions'].items():
        matches=[r for r in version['equation_occurrences'][label] if (74<=r['pdf_page']<=87 if label.startswith('7.') else 108<=r['pdf_page']<=110)]
        assert len(matches)==1,(label,key,matches)
        row[key+'_pdf_page']=matches[0]['pdf_page']
    rows.append(row)
assert len(rows)==31
images=[]
for page in list(range(74,88))+list(range(108,111)):
    p=HERE/'render'/f'comparison-{page:03}.png'
    item={'pdf_page':page,'comparison_image':str(p.relative_to(HERE)),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'complete_pair_visually_reviewed':True}
    if page>=108:
        old=Image.open(HERE/'render'/f'old_165p-{page:03}.png').convert('RGB')
        new=Image.open(HERE/'render'/f'new_166p-{page:03}.png').convert('RGB')
        item['pixel_identical_at_85_dpi']=old.size==new.size and ImageChops.difference(old,new).getbbox() is None
    images.append(item)
files={}
for p in HERE.glob('*'):
    if p.is_file() and p.name not in ['receipt.json','REPORT.md']:
        files[p.name]={'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'bytes':p.stat().st_size}
old=(HERE/'old_165p_poppler_layout.txt').read_bytes().split(b'\x0c')
new=(HERE/'new_166p_poppler_layout.txt').read_bytes().split(b'\x0c')
page_eq={str(p):old[p-1]==new[p-1] for p in [108,109,110]}
tool_version=subprocess.run(['<user-root>/AppData/Local/Programs/MiKTeX/miktex/bin/x64/pdftotext.exe','-v'],capture_output=True,text=True,check=True)
receipt={'scope':extraction['scope'],'source_pdfs':{key:{field:v[field] for field in ['pdf','pdf_sha256','bytes','poppler_pages','text_sha256']} for key,v in extraction['versions'].items()},'pdftotext_version':tool_version.stdout+tool_version.stderr,'extraction_arguments':['-layout','-enc','UTF-8'],'target_equation_count':31,'target_equations':rows,'pages_108_110_raw_bytes_identical':page_eq,'visual_review':images,'artifact_files':files,'limitations':['No mathematical theorem verification is asserted.','No full-manuscript equivalence is asserted.','Visual equality is a bounded formula inspection, not equality of the PDFs.','Unnormalized full Poppler outputs are retained; line reflow and glyph placement differences remain in the saved diffs.']}
(HERE/'receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'target_count':len(rows),'page_moves':[r for r in rows if r['old_165p_pdf_page']!=r['new_166p_pdf_page']],'identical_raw_pages':page_eq,'identical_rendered_pages':{i['pdf_page']:i['pixel_identical_at_85_dpi'] for i in images if 'pixel_identical_at_85_dpi' in i}},indent=2))
