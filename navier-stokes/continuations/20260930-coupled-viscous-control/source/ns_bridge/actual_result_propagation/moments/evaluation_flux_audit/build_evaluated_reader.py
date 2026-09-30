from pathlib import Path
import hashlib, json, re, subprocess
import fitz
from PIL import Image, ImageOps, ImageDraw

root = Path(__file__).resolve().parent
qdir = root.parent / "quantitative_extension"
def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()
def run(args, cwd=root):
    proc = subprocess.run(args, cwd=cwd, capture_output=True, encoding="utf-8", errors="replace")
    if proc.returncode:
        raise RuntimeError(proc.stdout[-6000:] + proc.stderr[-2000:])
    return proc.stdout
run(["python", str(qdir/"replay_quantitative_extension.py")], qdir)
run(["python", str(qdir/"build_quantitative_reader.py")], qdir)
run(["python", "replay_evaluated_exact.py"])
run(["python", "draw_flux_maps.py"])

base = (qdir/"current_quantitative_reader.tex").read_text(encoding="utf-8")
assert base.count(r"\end{document}") == 1
base = base.replace(r"\usepackage{mathrsfs}", r"\usepackage{mathrsfs,graphicx,mathtools}")
base = base.replace(
    "identities with finite path constants, not uniform endpoint or infinite-cycle\nestimates.",
    "identities with finite path constants, not uniform endpoint or infinite-cycle\nestimates. "
    "The final part proves the full evaluated-flux coefficient expansion,\n"
    "its required auxiliary supremum norms, every axial derivative,\n"
    "and the exact signs under physical reflection.")
body = (root/"evaluation_flux_body.tex").read_text(encoding="utf-8")
tex = base.replace(r"\end{document}",
    "\\clearpage\\part{Evaluated flux: complete coefficients and signed propagation}\n"
    +body+"\n\\end{document}\n")
(root/"current_evaluated_reader.tex").write_text(tex, encoding="utf-8")
labels = re.findall(r"\\label\{([^{}]+)\}",tex)
refs = re.findall(r"\\(?:ref|eqref|pageref)\{([^{}]+)\}",tex)
assert len(labels) == len(set(labels))
assert set(refs) <= set(labels), set(refs)-set(labels)
records = {}
qa = root/"qa"
qa.mkdir(exist_ok=True)
for name in ["evaluation_flux_audit", "current_evaluated_reader"]:
    for passnum in range(1,4):
        (root/f"{name}_pass_{passnum}.txt").write_text(
            run(["pdflatex","-interaction=nonstopmode","-halt-on-error",name+".tex"]),
            encoding="utf-8")
    log = (root/(name+".log")).read_text(encoding="utf-8", errors="replace")
    warnings = [line for line in log.splitlines()
                if re.search(r"Overfull|Underfull|undefined|multiply defined|Warning",line)]
    assert not warnings, warnings
    pdf = root/(name+".pdf")
    doc = fitz.open(pdf)
    out = []
    for i,page in enumerate(doc,1):
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines",[]):
                for span in line["spans"]:
                    x0,y0,x1,y1 = span["bbox"]
                    if x0 < 0 or y0 < 0 or x1 > page.rect.width+.01 or y1 > page.rect.height+.01:
                        out.append((i,span["text"]))
    assert not out,out
    records[name] = {"pages":len(doc), "pdf_sha256":sha(pdf),
                     "tex_sha256":sha(root/(name+".tex")),
                     "warnings":warnings,"out_of_page_text":out}
    # Full-size images for local visual inspection.
    for i,page in enumerate(doc,1):
        page.get_pixmap(matrix=fitz.Matrix(1.35,1.35),alpha=False).save(
            qa/f"{name}_{i:03}.png")
    # Contact sheets aid inspection; exact prefix comparisons below preserve prior review.
    paths = list(sorted(qa.glob(name+"_*.png")))
    for start in range(0,len(paths),6):
        selected = paths[start:start+6]
        sheet = Image.new("RGB",(1260,3*620),"#dddddd")
        draw = ImageDraw.Draw(sheet)
        for j,p in enumerate(selected):
            im = Image.open(p).convert("RGB")
            im.thumbnail((600,580))
            x=(j%2)*630+(630-im.width)//2
            y=(j//2)*620+27
            sheet.paste(im,(x,y))
            draw.text(((j%2)*630+10,(j//2)*620+5),p.stem,fill="black")
        sheet.save(qa/f"{name}_contact_{start//6+1:02}.jpg",quality=94)
    doc.close()

# Compare unchanged inherited mathematical pages, not metadata or timestamps.
oldpath = root/"prior_20260909/quantitative_extension_current_quantitative_reader.pdf"
old = fitz.open(oldpath)
new = fitz.open(root/"current_evaluated_reader.pdf")
matched, changed = [], []
for i in range(min(len(old),len(new))):
    p,q=old[i].get_pixmap(),new[i].get_pixmap()
    (matched if p.width==q.width and p.height==q.height and p.samples==q.samples else changed).append(i+1)
receipt = {
    "schema":"evaluated-flux-cumulative-v2",
    "build_passed":True,
    "visual_review":"pending",
    "standalone":records["evaluation_flux_audit"],
    "cumulative":records["current_evaluated_reader"],
    "body_sha256":sha(root/"evaluation_flux_body.tex"),
    "figure_sha256":sha(root/"flux_maps.pdf"),
    "replay":json.loads((root/"replay_receipt.json").read_text(encoding="utf-8")),
    "inherited_unchanged_pixel_pages":matched,
    "inherited_changed_pixel_pages":changed,
    "new_pages":list(range(len(old)+1,len(new)+1)),
    "prior_pdf_sha256":sha(oldpath),
    "scope":"Finite original coefficient expansion, all axial derivatives, and exact reflection signs; source theorem remains attributed."
}
(root/"build_receipt.json").write_text(json.dumps(receipt,indent=2)+"\n",encoding="utf-8")
print(json.dumps({k:receipt[k] for k in ["build_passed","visual_review","inherited_unchanged_pixel_pages","inherited_changed_pixel_pages","new_pages"]}))
print(json.dumps(records))
