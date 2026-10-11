from pathlib import Path
import re

def escape(text):
    replacements = {'\\': '\\textbackslash{}', '&': '\\&', '%': '\\%', '$': '\\$', '#': '\\#', '_': '\\_', '{': '\\{', '}': '\\}', '~': '\\textasciitilde{}', '^': '\\textasciicircum{}'}
    return ''.join((replacements.get(c, c) for c in text))
tokens = re.compile('(?s)(\\\\\\[.*?\\\\\\]|\\\\\\(.*?\\\\\\)|\\[[^\\]]*\\]\\([^)]+\\))')

def inline(text):
    output = []
    cursor = 0
    for match in tokens.finditer(text):
        output.append(escape(text[cursor:match.start()]))
        item = match.group()
        if item.startswith('\\'):
            output.append(item)
        else:
            m = re.fullmatch('\\[([^\\]]*)\\]\\(([^)]*)\\)', item)
            target = m.group(2)
            if not re.match('^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                target = globals().get('source_base_url', '') + target
            output.append('\\href{' + target + '}{' + escape(m.group(1)) + '}')
        cursor = match.end()
    output.append(escape(text[cursor:]))
    return ''.join(output)

def convert(text):
    mathblocks = []

    def keep(match):
        mathblocks.append(match.group())
        return '@@DISPLAY' + str(len(mathblocks) - 1) + '@@'
    text = re.sub('(?s)\\\\\\[.*?\\\\\\]|\\\\\\(.*?\\\\\\)', keep, text)
    text = re.sub('(?s)(!?\\[[^\\]]*\\]\\([^)]+\\))', lambda match: ' '.join(match.group().splitlines()), text)
    out = []
    table = False
    for line in text.splitlines():
        if line.startswith('|'):
            if re.fullmatch('\\|[\\s:|\\-]+\\|', line):
                continue
            if not table:
                out.append('\\begin{center}\\small\\begin{tabular}{p{.15\\linewidth}p{.23\\linewidth}p{.23\\linewidth}p{.17\\linewidth}}\\toprule')
                table = True
            out.append(' & '.join((inline(x.strip()) for x in line.strip('|').split('|'))) + '\\\\')
            continue
        if table:
            out.append('\\bottomrule\\end{tabular}\\end{center}')
            table = False
        if line.startswith('!['):
            figure = re.fullmatch('!\\[([^\\]]*)\\]\\(([^)]+)\\)', line)
            if figure is None:
                raise ValueError('Unparsed figure: ' + line)
            out.append('\\begin{figure}[htbp]\\centering\\includegraphics[width=\\linewidth,height=.72\\textheight,keepaspectratio]{' + figure.group(2) + '}\\caption{' + inline(figure.group(1)) + '}\\end{figure}')
        elif line.startswith('## '):
            out.append('\\subsection*{' + escape(line[3:]) + '}')
        elif line.startswith('# '):
            out.append('\\section*{' + escape(line[2:]) + '}')
        elif re.fullmatch('@@DISPLAY\\d+@@', line):
            block = mathblocks[int(line[9:-2])]
            if re.search('\\\\tag\\{(?:PK25|PK132|PK158)\\}', block):
                out.append('\\begingroup\\footnotesize' + '\n' + block + '\n' + '\\endgroup')
            else:
                out.append(block)
        else:
            line = re.sub('\\*\\*([^*]*)\\*\\*', '\\1', line)
            out.append(inline(line))
    if table:
        out.append('\\bottomrule\\end{tabular}\\end{center}')
    return re.sub('@@DISPLAY(\\d+)@@', lambda match: mathblocks[int(match.group(1))], '\n'.join(out))
HEADER = '\\documentclass[11pt]{article}\n\\usepackage{iftex}\n\\ifPDFTeX\\usepackage[T1]{fontenc}\\usepackage[utf8]{inputenc}\\usepackage{lmodern}\\else\\usepackage{fontspec}\\setmainfont{Latin Modern Roman}\\fi\n\\usepackage{amsmath,amssymb,mathrsfs,booktabs,graphicx,hyperref}\n\\usepackage[margin=21.5mm]{geometry}\n\\hypersetup{hidelinks,pdftitle={Yang--Mills: complete research proofs}}\n\\allowdisplaybreaks\n\\emergencystretch=3em\n\\setlength{\\parindent}{0pt}\n\\setlength{\\parskip}{6pt}\n\\begin{document}\n'

import json,hashlib
ROOT=Path(__file__).resolve().parent
source_base_url='https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/'
names=json.loads((ROOT/'READER_SOURCES.json').read_text(encoding='utf-8'))
rows=[];bodies=[]
for name in names:
    p=ROOT/name;s=p.read_text(encoding='utf-8')
    source_base_url='https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20261011-central-signs-shrinking-window/'+(p.parent.relative_to(ROOT).as_posix()+'/' if p.parent!=ROOT else '')
    body=convert(s)
    blocks=re.findall(r'(?s)\\\[.*?\\\]|\\\(.*?\\\)',s)
    assert all(x in body for x in blocks)
    rows.append({'source':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'complete_math_blocks':len(blocks)})
    bodies.append(body)
header=HEADER.replace('Yang--Mills: complete research proofs','Yang--Mills central signs and shrinking spectral windows')
out=ROOT/'RESEARCH_CONTINUATION.tex'
out.write_text(header+'\n\\clearpage\n'.join(bodies)+'\n\\end{document}\n',encoding='utf-8',newline='\n')
(ROOT/'TEX_FIDELITY.json').write_text(json.dumps({'sources':rows,'all_math_blocks_preserved':True,
 'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),'compilation_confirmed':False,
 'compile_status':'Compilation has not been confirmed for this source edition; no current PDF is included.'},indent=2)+'\n')
print(json.dumps({'math_blocks':sum(x['complete_math_blocks'] for x in rows),'source_files':len(rows)}))
