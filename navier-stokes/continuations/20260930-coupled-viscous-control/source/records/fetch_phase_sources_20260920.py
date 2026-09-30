from pathlib import Path
import hashlib, json, urllib.request
root = Path(__file__).resolve().parents[1]
out = root / "sources/reconstruction_5e162f34"
record_path = out / "source_record.json"
record = json.loads(record_path.read_text(encoding="utf-8"))
base = "https://raw.githubusercontent.com/KokunoYumeto/openai-navier-stokes-latex/" + record["version"] + "/"
for name in ["reconstruction/sections/pp043-048.tex", "reconstruction/sections/pp013-018.tex"]:
    target = out / name
    if not target.exists():
        target.write_bytes(urllib.request.urlopen(base + name, timeout=25).read())
    data = target.read_bytes()
    record["fetched_files"][name] = {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}
record_path.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
print("Two version-pinned reconstructed TeX sections saved; reading coverage unchanged until inspected.")
