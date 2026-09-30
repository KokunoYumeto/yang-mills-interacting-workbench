"""One bounded provenance audit of the two known session JSONL files."""
import hashlib
import json
from pathlib import Path

here=Path(__file__).resolve().parent
sessions=Path('<user-root>/.codex/sessions/2026/09/08')
files=[sessions/'rollout-2026-09-08T15-55-49-01a0814d-b8dd-7350-be89-8d62c08513dd.jsonl',
       sessions/'rollout-2026-09-08T15-57-28-01a0814f-3ca8-79b2-874a-d3fb2c94f341.jsonl']
out=['# Verbatim user inputs recovered by one bounded JSONL audit\n']
manifest=[]
for path in files:
    data=path.read_bytes()
    count=0
    for line_index,line in enumerate(data.decode('utf-8').splitlines(),1):
        entry=json.loads(line)
        payload=entry.get('payload',{})
        if entry.get('type')=='response_item' and payload.get('type')=='message' and payload.get('role')=='user':
            parts=[p.get('text','') for p in payload.get('content',[]) if p.get('type') in ('input_text','text')]
            if parts:
                count+=1
                out.append(f'\n## {path.name}, line {line_index}, {entry.get("timestamp", "")}\n\n')
                out.append('\n'.join(parts)+'\n')
    manifest.append({'file':path.name,'sha256_at_audit':hashlib.sha256(data).hexdigest(),'user_messages':count})
(here/'USER_JSONL_TRANSCRIPT.md').write_text(''.join(out),encoding='utf-8')
(here/'user_input_audit_receipt.json').write_text(json.dumps({'audit':'one bounded pass; only role=user message content copied verbatim','files':manifest},indent=2)+'\n',encoding='utf-8')
print(json.dumps(manifest))
