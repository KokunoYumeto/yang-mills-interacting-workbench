from pathlib import Path
import subprocess
from PIL import Image, ImageDraw
from check_source_revision import PDFS, POPPLER, HERE

out=HERE/'render'
out.mkdir(exist_ok=True)
for key,(pdf,_) in PDFS.items():
    for first,last in [(74,87),(108,110)]:
        subprocess.run([str(POPPLER/'pdftoppm.exe'),'-f',str(first),'-l',str(last),'-r','85','-png',str(pdf),str(out/key)],check=True)
for page in list(range(74,88))+list(range(108,111)):
    ims=[Image.open(out/f'{key}-{page:03}.png').convert('RGB') for key in PDFS]
    combined=Image.new('RGB',(sum(im.width for im in ims),max(im.height for im in ims)+36),'#eeeeee')
    draw=ImageDraw.Draw(combined)
    x=0
    for key,im in zip(PDFS,ims):
        draw.text((x+10,10),f'{key} / PDF page {page}',fill='black')
        combined.paste(im,(x,36));x+=im.width
    combined.save(out/f'comparison-{page:03}.png')
print('17 full-page comparison images rendered.')
