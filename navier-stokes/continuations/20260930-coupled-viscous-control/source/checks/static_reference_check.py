"""Check labels, references, and figure paths in the exported TeX body."""

from pathlib import Path
import hashlib
import json
import re


HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
BODY = ROOT / "integration/coupled_viscous_control_body.tex"
OUT = HERE / "static_reference_receipt.json"

text = BODY.read_text(encoding="utf-8-sig")
labels = re.findall(r"\\label\{([^}]+)\}", text)
references = []
for command in ("ref", "eqref", "pageref"):
    references.extend(re.findall(rf"\\{command}\{{([^}}]+)\}}", text))
references.extend(re.findall(r"\\hyperref\[([^]]+)\]", text))

label_set = set(labels)
missing = sorted(set(references) - label_set)
duplicate_labels = sorted(label for label in label_set if labels.count(label) > 1)

figure_paths = re.findall(r"\\includegraphics(?:\[[^]]*\])?\s*\{([^}]+)\}", text)
missing_figures = sorted(path for path in figure_paths if not (ROOT / "integration" / path).is_file())

assert not duplicate_labels, duplicate_labels
assert not missing, missing
assert not missing_figures, missing_figures

receipt = {
    "schema": "coupled-viscous-control-static-reference-check-v1",
    "status": "pass",
    "body": "integration/coupled_viscous_control_body.tex",
    "body_sha256": hashlib.sha256(BODY.read_bytes()).hexdigest(),
    "label_count": len(labels),
    "reference_count": len(references),
    "unique_referenced_labels": len(set(references)),
    "duplicate_labels": duplicate_labels,
    "missing_references": missing,
    "figure_paths": figure_paths,
    "missing_figures": missing_figures,
}
OUT.write_text(json.dumps(receipt, indent=2) + "\n", encoding="utf-8")
print(json.dumps(receipt))
