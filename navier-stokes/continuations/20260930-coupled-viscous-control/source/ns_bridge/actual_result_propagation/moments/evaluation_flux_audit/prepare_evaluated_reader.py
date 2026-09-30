from pathlib import Path
import shutil

root = Path(__file__).resolve().parent
qdir = root.parent / "quantitative_extension"
archive = root / "prior_20260909"
archive.mkdir(exist_ok=True)
for path in [root / "evaluation_flux_audit.tex",
             root / "evaluation_flux_audit.pdf",
             root / "replay_evaluation_flux.py",
             root / "replay_receipt.json",
             qdir / "quantitative_extension.tex",
             qdir / "current_quantitative_reader.tex",
             qdir / "current_quantitative_reader.pdf",
             qdir / "build_receipt.json",
             qdir / "replay_receipt.json"]:
    destination = archive / (path.parent.name + "_" + path.name)
    if path.exists() and not destination.exists():
        shutil.copy2(path, destination)
wrapper = r"""\documentclass[11pt]{article}
\usepackage[a4paper,margin=1in]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,graphicx}
\usepackage[hidelinks]{hyperref}
\title{Evaluated radial flux: exact finite coefficients and signs}
\author{}\date{20 September 2026}
\begin{document}
\maketitle
\input{evaluation_flux_body.tex}
\end{document}
"""
(root / "evaluation_flux_audit.tex").write_text(wrapper, encoding="utf-8")
path = qdir / "quantitative_extension.tex"
tex = path.read_text(encoding="utf-8")
tex = tex.replace(
    r"For \(e=1,2\), with \(\|a\|_e^2=\int R^e\langle|a|^2\rangle\,dR\),",
    r"For \(e=1,2\), put \(\alpha_e=(e+1)/4-A\). With "
    r"\(\|a\|_e^2=\int R^e\langle|a|^2\rangle\,dR\),")
tex = tex.replace(
    r"e&\|v_j\|_e&\|\partial_zv_j\|_e\\ \hline",
    r"e&\text{factor multiplying }\|b_j\|_e&"
    r"\text{factor multiplying }\|d_j\|_e\\ \hline")
tex = tex.replace(
    "as upper bounds, before summing the finite retained harmonics.",
    "as the factors multiplying the actual coefficient norms in the "
    "preceding bounds, before summing the finite retained harmonics.")
start = tex.find("For equal old and new orders")
end = tex.find("The evaluated-phase correction", start)
if start >= 0:
    assert end > start
    tex = tex[:start] + (
        "The old field and old derivative orders stay independent in all "
        "four cross terms. No equal-order cross-term table is inferred "
        "from the quadratic powers.\n\n") + tex[end:]
tex = tex.replace(
    r"\left|\partial_Z(S^\circ_{z,\tau_e})^*(R,Z,T,Y)\right|",
    r"\left|\partial_Z\bigl[Q^{2A}(\mathcal S^\circ_{z,\tau_e})^Q\bigr]"
    r"(R,Z,T,Y)\right|")
tex = tex.replace("The harmless factors (1,2)", "The factors (1,2)")
path.write_text(tex, encoding="utf-8")
print("Prior files preserved; wrapper and affected quantitative body corrected.")
