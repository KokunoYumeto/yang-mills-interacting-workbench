"""Generate GitHub-math reading copies; preserve every supplied source byte.

Only math delimiters outside fenced code blocks are changed. --check verifies
the reading copies and their source/derived hashes without writing files.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SOURCES = (
    "manuscripts/IDENTITY_AND_COMPLETION.md",
    "manuscripts/RESEARCH.md",
    "archive/er-epr-continuation/docs/ER_EPR_CONTINUATION.md",
    "archive/ns-bh-interior/docs/INTERIOR_CONTINUATION.md",
    "archive/ns-vacuum-propagation/docs/HIGHER_ORDER.md",
    "archive/ns-vacuum-propagation/docs/PROPAGATION.md",
    "archive/vacuum-hydrodynamics/RESEARCH_NOTE.md",
)


def github_math(text):
    lines = []
    fence = None
    for line in text.splitlines(keepends=True):
        stripped = line.lstrip()
        if fence is None and stripped.startswith(("```", "~~~")):
            fence = stripped[:3]
        elif fence is not None and stripped.startswith(fence):
            fence = None
        elif fence is None:
            line = line.replace(r"\(", "$").replace(r"\)", "$")
            line = line.replace(r"\[", "$$").replace(r"\]", "$$")
        lines.append(line)
    return "".join(lines)


def generated():
    outputs, records = {}, []
    for source in SOURCES:
        data = (ROOT / source).read_bytes()
        target = "readers/" + Path(source).name
        prefix = ("*GitHub reading copy; only mathematical delimiters have changed. "
                  f"[Unchanged source](../{source}).*\n\n")
        body = (prefix + github_math(data.decode("utf-8").replace("\r\n", "\n"))).encode("utf-8")
        outputs[target] = body
        records.append({"source": source, "source_sha256": hashlib.sha256(data).hexdigest(),
                        "reader": target, "reader_sha256": hashlib.sha256(body).hexdigest()})
    outputs["readers/manifest.json"] = (json.dumps({
        "transformation": "Math delimiters outside fenced code: backslash parentheses to dollar; backslash brackets to double dollar. LF reading-copy line endings. No mathematical edits.",
        "generator": "../build_github_readers.py", "files": records
    }, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    return outputs


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for relative, body in generated().items():
        target = ROOT / relative
        if args.check:
            if not target.exists() or target.read_bytes() != body:
                raise SystemExit("Reading copy differs: " + relative)
        else:
            target.parent.mkdir(exist_ok=True)
            target.write_bytes(body)
    print(("Verified" if args.check else "Generated") + " seven complete GitHub reading copies and source/reader hashes.")


if __name__ == "__main__":
    main()
