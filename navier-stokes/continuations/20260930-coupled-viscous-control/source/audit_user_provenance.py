"""One bounded, append-only audit of literal user response items in this task."""
from pathlib import Path
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('session_jsonl', type=Path)
args = parser.parse_args()
here = Path(__file__).resolve().parent
target = here / 'USER_INPUTS_VERBATIM.md'
existing = target.read_text(encoding='utf-8-sig')
def comparable(text):
    # Compare newline conventions only; preserve the original text when appending.
    return text.replace('\r\n', '\n').replace('\r', '\n')
existing_comparable = comparable(existing)
seen = 0
added = []
with args.session_jsonl.open(encoding='utf-8') as stream:
    for raw in stream:
        event = json.loads(raw)
        if event.get('type') != 'response_item':
            continue
        item = event.get('payload', {})
        if item.get('role') != 'user':
            continue
        chunks = [c['text'] for c in item.get('content', [])
                  if c.get('type') in ('input_text', 'text') and 'text' in c]
        text = '\n'.join(chunks)
        if not text:
            continue
        seen += 1
        if comparable(text) in existing_comparable or any(
                comparable(text) == comparable(x) for x in added):
            continue
        added.append(text)
if added:
    with target.open('a', encoding='utf-8', newline='\n') as stream:
        for text in added:
            stream.write('\n\n---\n\n' + text + '\n')
receipt = dict(user_response_items_seen=seen, items_appended=len(added),
               bounded_single_read=True, output=target.name)
(here/'checks'/'provenance_audit.json').write_text(
    json.dumps(receipt, indent=2)+'\n', encoding='utf-8')
print(json.dumps(receipt))
