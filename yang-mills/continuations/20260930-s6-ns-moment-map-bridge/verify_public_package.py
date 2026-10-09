"""Verify the public S6/NS-to-Yang--Mills continuation package."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parent
MANIFEST = ROOT / "PUBLIC_MANIFEST.json"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def collect_boole(value: object) -> list[bool]:
    if isinstance(value, bool):
        return [value]
    if isinstance(value, dict):
        result: list[bool] = []
        for child in value.values():
            result.extend(collect_boole(child))
        return result
    if isinstance(value, list):
        result = []
        for child in value:
            result.extend(collect_boole(child))
        return result
    return []


required = [
    "README.md",
    "PROOF.md",
    "HIGHER_CARRIER_AND_EVOLUTION.md",
    "HIGHER_CARRIER_AND_EVOLUTION.tex",
    "COMPACT_SUPPORT_CAUCHY_EVOLUTION.md",
    "COMPACT_SUPPORT_CAUCHY_EVOLUTION.tex",
    "COMPACT_CAUCHY_TEX_COMPILE_STATUS.json",
    "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md",
    "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.tex",
    "PERIOD_PHYSICAL_TEX_COMPILE_STATUS.json",
    "RESULTS_20261008.md",
    "checks/verify_period_physical_kernels.py",
    "checks/PERIOD_PHYSICAL_KERNEL_CHECK.json",
    "checks/COMPLEMENTARY_SECOND_MOMENT_CHECK.json",
    "checks/verify_complementary_second_moment.py",
    "RESULTS_20261009.md",
    "figures/COMPLEMENTARY_SECOND_MOMENT.png",
    "figures/COMPLEMENTARY_SECOND_MOMENT.svg",
    "figures/complementary_moment_figure.py",
    "figures/COMPLEMENTARY_SECOND_MOMENT_FIGURE_CHECK.json",
    "figures/PERIOD_PHYSICAL_KERNELS.png",
    "figures/PERIOD_PHYSICAL_KERNELS.svg",
    "figures/period_physical_figure.py",
    "figures/PERIOD_PHYSICAL_FIGURE_CHECK.json",
    "checks/verify_compact_cauchy.py",
    "checks/COMPACT_CAUCHY_CHECK.json",
    "figures/COMPACT_CAUCHY_EVOLUTION.png",
    "figures/COMPACT_CAUCHY_EVOLUTION.svg",
    "figures/compact_cauchy_figure.py",
    "figures/COMPACT_CAUCHY_FIGURE_CHECK.json",
    "checks/HIGHER_CARRIER_EVOLUTION_CHECK.json",
    "figures/HIGHER_CARRIER_EVOLUTION.png",
    "figures/HIGHER_CARRIER_EVOLUTION.svg",
    "SP1_BUNDLE_BRIDGE.md",
    "HIGHER_DOMAIN_PROGRAM.md",
    "SPECTRAL_PROGRAM.md",
    "CLAIM_LEDGER.md",
    "SOURCE_PROVENANCE.md",
    "checks/SP1_BUNDLE_BRIDGE_CHECK.json",
    "checks/SP1_MOMENT_MAP_BRIDGE_CHECK.json",
    "checks/THREE_COLOUR_CURVATURE_CHECK.json",
    "sources/higher_rung/s6_higher_rung_24d_preprint.tex",
    "figures/S6_NS_MOMENT_MAP_BRIDGE.png",
    "figures/S6_NS_MOMENT_MAP_BRIDGE.svg",
    "PUBLIC_VALIDATION.json",
    "PUBLIC_MANIFEST.json",
]

checks: dict[str, bool] = {}
for relative in required:
    checks[f"required:{relative}"] = (ROOT / relative).is_file()

receipt_paths = [
    ROOT / "checks" / "SP1_BUNDLE_BRIDGE_CHECK.json",
    ROOT / "checks" / "SP1_MOMENT_MAP_BRIDGE_CHECK.json",
    ROOT / "checks" / "THREE_COLOUR_CURVATURE_CHECK.json",
    ROOT / "checks" / "HIGHER_CARRIER_EVOLUTION_CHECK.json",
    ROOT / "checks" / "COMPACT_CAUCHY_CHECK.json",
    ROOT / "checks" / "PERIOD_PHYSICAL_KERNEL_CHECK.json",
    ROOT / "checks" / "COMPLEMENTARY_SECOND_MOMENT_CHECK.json",
    ROOT / "checks" / "FULL_PACKET_RESOLVENT_CHECK.json",
    ROOT / "checks" / "PACKET_MOMENTS_ESCAPE_CHECK.json",
    ROOT / "checks" / "ODD_VACUUM_OBSERVABLE_CHECK.json",
    ROOT / "checks" / "JOINT_PATH_GLOBAL_OBSERVABLE_CHECK.json",
    ROOT / "checks" / "GLOBAL_FOUR_POINT_CHECK.json",
    ROOT / "checks" / "PHASE_VARIATIONAL_CHECK.json",
]
for receipt_path in receipt_paths:
    receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
    checks[f"receipt:{receipt_path.name}:all_passed"] = receipt.get("all_passed") is True
    receipt_booleans = collect_boole(receipt.get("checks", {}))
    checks[f"receipt:{receipt_path.name}:every_check_true"] = bool(receipt_booleans) and all(
        receipt_booleans
    )

packet_receipt = json.loads((ROOT / "checks/FULL_PACKET_RESOLVENT_CHECK.json").read_text(encoding="utf-8"))
checks["full_packet_receipt_matches_current_proof"] = packet_receipt["proof_sha256"] == sha256(ROOT / "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md")
packet_figure = json.loads((ROOT / "figures/FULL_PACKET_RESOLVENT_FIGURE_CHECK.json").read_text(encoding="utf-8"))
checks["full_packet_figure_inspection_recorded"] = "inspected" in packet_figure["visual_inspection"]
for row in packet_figure["files"]:
    checks["full_packet_figure_hash:" + row["file"]] = row["sha256"] == sha256(ROOT / "figures" / row["file"])

escape_receipt = json.loads((ROOT / "checks/PACKET_MOMENTS_ESCAPE_CHECK.json").read_text(encoding="utf-8"))
checks["escape_receipt_matches_current_proof"] = escape_receipt["proof_sha256"] == sha256(ROOT / "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md")
escape_figure = json.loads((ROOT / "figures/PACKET_ESCAPE_FIGURE_CHECK.json").read_text(encoding="utf-8"))
checks["escape_figure_inspection_recorded"] = "inspected" in escape_figure["visual_inspection"]
for row in escape_figure["files"]:
    checks["escape_figure_hash:" + row["file"]] = row["sha256"] == sha256(ROOT / "figures" / row["file"])

odd_receipt = json.loads((ROOT / "checks/ODD_VACUUM_OBSERVABLE_CHECK.json").read_text(encoding="utf-8"))
checks["odd_receipt_matches_current_proof"] = odd_receipt["proof_sha256"] == sha256(ROOT / "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md")
odd_figure = json.loads((ROOT / "figures/ODD_OBSERVABLE_FIGURE_CHECK.json").read_text(encoding="utf-8"))
checks["odd_figure_inspection_recorded"] = "inspected" in odd_figure["visual_inspection"]
for row in odd_figure["files"]:
    checks["odd_figure_hash:" + row["file"]] = row["sha256"] == sha256(ROOT / "figures" / row["file"])
source_bindings = json.loads((ROOT / "checks/ODD_OBSERVABLE_SOURCE_BINDINGS.json").read_text(encoding="utf-8"))
repository_root = ROOT.parents[2]
for row in source_bindings["bindings"]:
    checks["odd_source_binding:" + row["source_id"]] = row["sha256"] == sha256(repository_root / row["path"])

joint_receipt = json.loads((ROOT / "checks/JOINT_PATH_GLOBAL_OBSERVABLE_CHECK.json").read_text(encoding="utf-8"))
checks["joint_receipt_matches_current_proof"] = joint_receipt["proof_sha256"] == sha256(ROOT / "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md")
joint_figure = json.loads((ROOT / "figures/JOINT_PATH_FIGURE_CHECK.json").read_text(encoding="utf-8"))
checks["joint_figure_inspection_recorded"] = "inspected" in joint_figure["visual_inspection"]
for row in joint_figure["files"]:
    checks["joint_figure_hash:" + row["file"]] = row["sha256"] == sha256(ROOT / "figures" / row["file"])
joint_bindings = json.loads((ROOT / "checks/JOINT_PATH_SOURCE_BINDINGS.json").read_text(encoding="utf-8"))
for row in joint_bindings["bindings"]:
    if row["current_file_unchanged"]:
        checks["joint_source_binding:" + row["source_id"]] = row["sha256"] == sha256(ROOT.parents[2] / row["path"])

global_receipt = json.loads((ROOT / "checks/GLOBAL_FOUR_POINT_CHECK.json").read_text(encoding="utf-8"))
checks["global_receipt_matches_current_proof"] = global_receipt["proof_sha256"] == sha256(ROOT / "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md")
global_figure = json.loads((ROOT / "figures/GLOBAL_MOMENTS_FIGURE_CHECK.json").read_text(encoding="utf-8"))
checks["global_figure_inspection_recorded"] = "inspected" in global_figure["visual_inspection"]
for row in global_figure["files"]:
    checks["global_figure_hash:" + row["file"]] = row["sha256"] == sha256(ROOT / "figures" / row["file"])
global_bindings = json.loads((ROOT / "checks/GLOBAL_MOMENTS_SOURCE_BINDINGS.json").read_text(encoding="utf-8"))
for row in global_bindings["bindings"]:
    if row["current_file_unchanged"]:
        checks["global_source_binding:" + row["source_id"]] = row["sha256"] == sha256(ROOT.parents[2] / row["path"])

reader_status = json.loads((ROOT / "PERIOD_PHYSICAL_TEX_COMPILE_STATUS.json").read_text(encoding="utf-8"))
checks["reader_pdf_matches_compiled_source"] = reader_status["source_sha256"] == sha256(ROOT / reader_status["source"])
checks["reader_pdf_bytes_verified"] = reader_status["pdf_sha256"] == sha256(ROOT / reader_status["pdf"])
checks["reader_pdf_compiled_and_inspected"] = reader_status["source_compilation_confirmed"] and "inspected" in reader_status["visual_inspection"]

phase_receipt = json.loads((ROOT / "checks/PHASE_VARIATIONAL_CHECK.json").read_text(encoding="utf-8"))
checks["phase_receipt_matches_current_proof"] = phase_receipt["proof_sha256"] == sha256(ROOT / "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md")
phase_figure = json.loads((ROOT / "figures/PHASE_VARIATIONAL_FIGURE_CHECK.json").read_text(encoding="utf-8"))
checks["phase_figure_inspection_recorded"] = "inspected" in phase_figure["visual_inspection"]
for row in phase_figure["files"]:
    checks["phase_figure_hash:" + row["file"]] = row["sha256"] == sha256(ROOT / "figures" / row["file"])
phase_bindings = json.loads((ROOT / "checks/PHASE_VARIATIONAL_SOURCE_BINDINGS.json").read_text(encoding="utf-8"))
for row in phase_bindings["bindings"]:
    if row["current_file_unchanged"]:
        checks["phase_source_binding:" + row["source_id"]] = row["sha256"] == sha256(ROOT.parents[2] / row["path"])

source_path = ROOT / "sources" / "higher_rung" / "s6_higher_rung_24d_preprint.tex"
period_receipt = json.loads((ROOT / "checks/PERIOD_PHYSICAL_KERNEL_CHECK.json").read_text(encoding="utf-8"))
checks["period_receipt_matches_current_proof"] = period_receipt["proof_sha256"] == sha256(ROOT / "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md")
complement_receipt = json.loads((ROOT / "checks/COMPLEMENTARY_SECOND_MOMENT_CHECK.json").read_text(encoding="utf-8"))
checks["complement_receipt_matches_current_proof"] = complement_receipt["proof_sha256"] == sha256(ROOT / "PERIOD_COUPLING_AND_PHYSICAL_KERNELS.md")
complement_figure = json.loads((ROOT / "figures/COMPLEMENTARY_SECOND_MOMENT_FIGURE_CHECK.json").read_text(encoding="utf-8"))
checks["complement_figure_inspection_recorded"] = "inspected" in complement_figure["visual_inspection"]
for row in complement_figure["files"]:
    checks["complement_figure_hash:" + row["file"]] = row["sha256"] == sha256(ROOT / "figures" / row["file"])
period_figure = json.loads((ROOT / "figures/PERIOD_PHYSICAL_FIGURE_CHECK.json").read_text(encoding="utf-8"))
checks["period_figure_inspection_recorded"] = "inspected" in period_figure["visual_inspection"]
for row in period_figure["files"]:
    checks["period_figure_hash:" + row["file"]] = row["sha256"] == sha256(ROOT / "figures" / row["file"])
checks["retained_source_sha256"] = (
    sha256(source_path)
    == "8c526746de9b56a4fcd0a274df0c470092cc82a16e49857df539a1c9d033956f"
)

png = (ROOT / "figures" / "S6_NS_MOMENT_MAP_BRIDGE.png").read_bytes()
svg = (ROOT / "figures" / "S6_NS_MOMENT_MAP_BRIDGE.svg").read_text(encoding="utf-8")
checks["figure_png_signature"] = png.startswith(b"\x89PNG\r\n\x1a\n")
checks["figure_svg_signature"] = "<svg" in svg[:1000]

cauchy_png = (ROOT / "figures/COMPACT_CAUCHY_EVOLUTION.png").read_bytes()
checks["cauchy_figure_png_signature"] = cauchy_png.startswith(b"\x89PNG\r\n\x1a\n")
cauchy_svg = (ROOT / "figures/COMPACT_CAUCHY_EVOLUTION.svg").read_text(encoding="utf-8")
checks["cauchy_figure_svg_signature"] = "<svg" in cauchy_svg[:1000]

proof = (ROOT / "PROOF.md").read_text(encoding="utf-8")
for token in [
    r"\operatorname{Hom}_{\operatorname{Sp}(1)}",
    r"D\mu_e(a)D\mu_e(a)^{\mathsf T}=4|a|^2I_3",
    r"\mathcal M_H",
    r"\mathcal J_j=-8e_j",
    r"J_j=-16T_j/g^2",
]:
    checks[f"proof_token:{token}"] = token in proof

text_suffixes = {".md", ".json", ".py", ".tex", ".svg"}
local_path_hits: list[str] = []
windows_account_prefix = "C:" + chr(92) + "Users" + chr(92)
slash_account_prefix = "C:/" + "Users/"
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in text_suffixes:
        continue
    text = path.read_text(encoding="utf-8", errors="strict")
    if windows_account_prefix in text or slash_account_prefix in text:
        local_path_hits.append(path.relative_to(ROOT).as_posix())
checks["no_machine_local_paths"] = not local_path_hits

manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
listed = {entry["path"]: entry for entry in manifest["files"]}
actual = {
    path.relative_to(ROOT).as_posix()
    for path in ROOT.rglob("*")
    if path.is_file() and path.name != MANIFEST.name
}
checks["manifest_covers_every_other_file"] = set(listed) == actual
for relative, entry in listed.items():
    path = ROOT / relative
    checks[f"manifest:{relative}:bytes"] = path.stat().st_size == entry["bytes"]
    checks[f"manifest:{relative}:sha256"] = sha256(path) == entry["sha256"]

failed = sorted(name for name, passed in checks.items() if not passed)
result = {
    "schema": "s6-ns-moment-map-public-package-verification-v1",
    "file_count_excluding_manifest": len(actual),
    "check_count": len(checks),
    "local_path_hits": local_path_hits,
    "all_passed": not failed,
    "failed": failed,
}
print(json.dumps(result, indent=2, ensure_ascii=False))
if failed:
    raise SystemExit(1)
