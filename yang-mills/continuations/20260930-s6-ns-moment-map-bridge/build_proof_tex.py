"""Build complete standalone TeX without losing multiline formulas."""
from pathlib import Path
import re

def escape(text):
    replacements = {'\\':r'\textbackslash{}','&':r'\&','%':r'\%',
                    '$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}',
                    '~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
    return ''.join(replacements.get(c,c) for c in text)

tokens = re.compile(r'(?s)(\\\[.*?\\\]|\\\(.*?\\\)|\[[^\]]*\]\([^)]+\))')

def inline(text):
    output = []
    cursor = 0
    for match in tokens.finditer(text):
        output.append(escape(text[cursor:match.start()]))
        item = match.group()
        if item.startswith('\\'):
            output.append(item)
        else:
            m = re.fullmatch(r'\[([^\]]*)\]\(([^)]*)\)',item)
            target = m.group(2)
            if not re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
                target = globals().get('source_base_url', '') + target
            output.append(r'\href{'+target+r'}{'+escape(m.group(1))+'}')
        cursor = match.end()
    output.append(escape(text[cursor:]))
    return ''.join(output)

def convert(text):
    # Complete display blocks are replaced temporarily so headings and tables
    # never reinterpret a formula or change its line breaks.
    mathblocks = []
    def keep(match):
        mathblocks.append(match.group())
        return '@@DISPLAY'+str(len(mathblocks)-1)+'@@'
    text = re.sub(r'(?s)\\\[.*?\\\]|\\\(.*?\\\)',keep,text)
    # A link may span several Markdown lines. Rejoin its prose before
    # line-based layout; the saved math blocks remain byte-identical.
    text = re.sub(r'(?s)(!?\[[^\]]*\]\([^)]+\))',
                  lambda match: ' '.join(match.group().splitlines()),text)
    out = []; table = False
    for line in text.splitlines():
        if line.startswith('|'):
            if re.fullmatch(r'\|[\s:|\-]+\|',line): continue
            if not table:
                out.append(r'\begin{center}\small\begin{tabular}{p{.15\linewidth}p{.23\linewidth}p{.23\linewidth}p{.17\linewidth}}\toprule')
                table = True
            out.append(' & '.join(inline(x.strip()) for x in line.strip('|').split('|'))+r'\\')
            continue
        if table:
            out.append(r'\bottomrule\end{tabular}\end{center}')
            table = False
        if line.startswith('!['):
            figure = re.fullmatch(r'!\[([^\]]*)\]\(([^)]+)\)',line)
            if figure is None: raise ValueError("Unparsed figure: "+line)
            out.append(r'\begin{figure}[htbp]\centering\includegraphics[width=\linewidth,height=.72\textheight,keepaspectratio]{'
                       +figure.group(2)+r'}\caption{'+inline(figure.group(1))+r'}\end{figure}')
        elif line.startswith('## '):
            out.append(r'\subsection*{'+escape(line[3:])+'}')
        elif line.startswith('# '):
            out.append(r'\section*{'+escape(line[2:])+'}')
        elif re.fullmatch(r'@@DISPLAY\d+@@',line):
            block = mathblocks[int(line[9:-2])]
            if re.search(r'\\tag\{(?:PK25|PK132|PK158)\}',block):
                out.append(r'\begingroup\footnotesize'+'\n'+block+'\n'+r'\endgroup')
            else:
                out.append(block)
        else:
            line = re.sub(r'\*\*([^*]*)\*\*',r'\1',line)
            out.append(inline(line))
    if table: out.append(r'\bottomrule\end{tabular}\end{center}')
    return re.sub(r'@@DISPLAY(\d+)@@',
                  lambda match: mathblocks[int(match.group(1))],
                  '\n'.join(out))

ROOT=Path(__file__).resolve().parent
source_base_url="https://github.com/KokunoYumeto/yang-mills-interacting-workbench/blob/main/yang-mills/continuations/20260930-s6-ns-moment-map-bridge/"
HEADER='\\documentclass[11pt]{article}\n\\usepackage{iftex}\n\\ifPDFTeX\\usepackage[T1]{fontenc}\\usepackage[utf8]{inputenc}\\usepackage{lmodern}\\else\\usepackage{fontspec}\\setmainfont{Latin Modern Roman}\\fi\n\\usepackage{amsmath,amssymb,mathrsfs,booktabs,graphicx,hyperref}\n\\usepackage[margin=21.5mm]{geometry}\n\\hypersetup{hidelinks,pdftitle={Yang--Mills: complete research proofs}}\n\\allowdisplaybreaks\n\\emergencystretch=3em\n\\setlength{\\parindent}{0pt}\n\\setlength{\\parskip}{6pt}\n\\begin{document}\n'
for name in ["HIGHER_CARRIER_AND_EVOLUTION","COMPACT_SUPPORT_CAUCHY_EVOLUTION","PERIOD_COUPLING_AND_PHYSICAL_KERNELS"]:
    source=(ROOT/(name+".md")).read_text(encoding="utf-8")
    body=convert(source)
    blocks=re.findall(r"(?s)\\\[.*?\\\]|\\\(.*?\\\)",source)
    assert all(block in body for block in blocks)
    (ROOT/(name+".tex")).write_text(HEADER+body+"\n\\end{document}\n",encoding="utf-8",newline="\n")
print("Complete standalone TeX sources rebuilt; all original math blocks retained.")
