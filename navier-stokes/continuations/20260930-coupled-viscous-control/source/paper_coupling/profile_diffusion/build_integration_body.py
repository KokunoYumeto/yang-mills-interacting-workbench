"""Build a collision-resistant input body and preamble from the standalone TeX."""
from pathlib import Path
import json
import re

HERE = Path(__file__).resolve().parent
source = (HERE / "profile_diffusion.tex").read_text(encoding="utf-8")
body = source.split(r"\begin{document}", 1)[1].split(r"\end{document}", 1)[0]
body = body.replace(r"\maketitle", "").strip() + "\n"
macros = {
    "R": "PDReal", "T": "PDTorus", "dd": "PDd",
    "thd": "PDthermal", "vis": "PDviscosity", "Hs": "PDheat", "av": "PDmean",
}
for old, new in macros.items():
    body = re.sub(r"\\" + old + r"(?![A-Za-z])", lambda match: "\\" + new, body)
body = re.sub(r"\\(label|ref|eqref)\{([^}]+)\}",
              lambda match: "\\" + match.group(1) + "{pd:" + match.group(2) + "}", body)
body = body.replace(r"\begin{proposition}", r"\begin{pdproposition}")
body = body.replace(r"\end{proposition}", r"\end{pdproposition}")
(HERE / "profile_diffusion_body.tex").write_text(body, encoding="utf-8")
preamble = r"""% Load in the master document preamble, before \begin{document}.
\RequirePackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\providecommand{\PDReal}{\mathbb R}
\providecommand{\PDTorus}{\mathbb T}
\providecommand{\PDd}{\mathrm d}
\providecommand{\PDthermal}{\kappa_{\rm th}}
\providecommand{\PDviscosity}{\nu_{\rm phys}}
\providecommand{\PDheat}{\mathcal H}
\providecommand{\PDmean}[1]{\langle #1\rangle}
\newtheorem{pdproposition}{Proposition}
"""
(HERE / "profile_diffusion_preamble.tex").write_text(preamble, encoding="utf-8")
manifest = {
    "body": "profile_diffusion_body.tex",
    "preamble": "profile_diffusion_preamble.tex",
    "source": "profile_diffusion.tex",
    "packages": ["amsmath", "amssymb", "amsthm", "mathtools", "mathrsfs"],
    "macros": ["\\" + name for name in macros.values()],
    "theorem_environments": ["pdproposition"],
    "proof_environment": "proof from amsthm",
    "label_prefix": "pd:",
    "section_commands": "Original section and unnumbered section commands retained; master may choose its hierarchy.",
    "body_contains_document_wrapper": False,
    "body_contains_maketitle": False,
}
(HERE / "integration_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
print(json.dumps(manifest, indent=2))
