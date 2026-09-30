"""Build the component reader using authoritative cumulative cross references.

Writes only beside this script. The master aux/PDF and source sections are
read-only. Run after the parent has compiled the updated cumulative master.
"""
from pathlib import Path
import hashlib
import json
import re
import shutil
import subprocess
import sys

HERE = Path(__file__).resolve().parent
PARENT = HERE.parent
operations = []


def run(name, command):
    result = subprocess.run(command, cwd=HERE, capture_output=True,
                            text=True, encoding="utf-8", errors="replace")
    (HERE/f"{name}.log").write_text(result.stdout+result.stderr, encoding="utf-8")
    operations.append({"name": name, "exit_code": result.returncode})
    if result.returncode:
        raise RuntimeError(f"{name} failed; see its local log")
    return result.stdout


run("exact_replay", [sys.executable, str(HERE/"replay_spatial.py")])
required = ["ave:complete_entry", "ave:nesting", "ave:amplitude_sup", "sr:origin_vorticity"]
source_aux = (PARENT/"coupled_viscous_control.aux").read_text(encoding="utf-8")
lines = []
for label in required:
    matching = [line for line in source_aux.splitlines()
                if line.startswith("\\newlabel{"+label+"}")]
    if len(matching) != 1:
        raise RuntimeError(f"Updated master aux must contain exactly one {label}")
    lines.extend(matching)
(HERE/"context_refs.aux").write_text("\n".join(lines)+"\n", encoding="utf-8")
for pass_number in range(1, 4):
    run(f"latex_pass_{pass_number}",
        [shutil.which("pdflatex"), "-interaction=batchmode", "-halt-on-error", "standalone.tex"])
latex_log = (HERE/"standalone.log").read_text(encoding="utf-8", errors="replace")
for forbidden in ["Overfull", "undefined references", "multiply defined", "LaTeX Warning"]:
    if forbidden in latex_log:
        raise RuntimeError(f"Final LaTeX log contains {forbidden}")
info = run("pdfinfo", [shutil.which("pdfinfo"), "standalone.pdf"])
pages = int(re.search(r"^Pages:\s+(\d+)", info, re.MULTILINE).group(1))
run("render", [shutil.which("pdftoppm"), "-scale-to", "1500", "-png", "standalone.pdf", "page"])
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
replay = json.loads((HERE/"replay_report.json").read_text(encoding="utf-8"))
receipt = {"schema": "modified-spatial-component-v1", "all_checks_passed": True,
           "symbolic_checks": replay["check_count"], "pages": pages,
           "operations": operations, "cross_reference_source": "../coupled_viscous_control.aux",
           "cross_reference_labels": required,
           "files_sha256": {p.name: sha(p) for p in
                            [HERE/"modified_spatial_body.tex", HERE/"replay_spatial.py",
                             HERE/"standalone.tex", HERE/"standalone.pdf", HERE/"audit.md"]},
           "scope": "Full compact realization of the actual finite damped two-stage coefficients, p=0 full scalar/vector residual forces, all derivative costs, finite hold and slab-only compact timeforce extension.",
           "infinite_viscous_sequence_proved": False,
           "visual_inspection": "Required separately after this build; see final_qa_receipt.json."}
(HERE/"build_receipt.json").write_text(json.dumps(receipt, indent=2)+"\n", encoding="utf-8")
print(json.dumps({"passed": True, "checks": replay["check_count"], "pages": pages}))
