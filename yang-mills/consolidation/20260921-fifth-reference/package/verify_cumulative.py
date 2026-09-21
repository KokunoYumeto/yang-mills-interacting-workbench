#!/usr/bin/env python3
"""Verify every delivered cumulative text file against the exact manifest."""
from pathlib import Path,PurePosixPath
import hashlib,json,sys
ROOT=Path(__file__).resolve().parent
class Invalid(RuntimeError):pass
def need(p,name):
 if not p:raise Invalid(name)
def parse(text):
 def pairs(items):
  d={}
  for k,v in items:need(k not in d,'duplicate-json-key:'+k);d[k]=v
  return d
 return json.loads(text,object_pairs_hook=pairs)
def main():
 try:
  m=parse((ROOT/'MANIFEST.json').read_text());need(m.get('schema')=='ym-cumulative-text-v1','manifest-schema')
  found=set();total=0
  for row in m['files']:
   raw=row['path'];rel=PurePosixPath(raw)
   need(not rel.is_absolute() and '..' not in rel.parts and rel.as_posix()==raw,'unsafe-manifest-path')
   need(raw not in found,'duplicate-manifest-path:'+raw);found.add(raw)
   p=ROOT/Path(raw);need(p.is_file() and not p.is_symlink(),'missing-source:'+raw)
   b=p.read_bytes();need(len(b)==row['size'],'size-mismatch:'+raw)
   need(hashlib.sha256(b).hexdigest()==row['sha256'],'sha256-mismatch:'+raw)
   b.decode('utf-8');total+=len(b)
  actual={p.relative_to(ROOT).as_posix() for p in ROOT.rglob('*') if p.is_file() and p!=ROOT/'MANIFEST.json' and '__pycache__' not in p.parts}
  need(actual==found,'manifest-file-membership')
  print(json.dumps({'passed':True,'files':len(found),'text_bytes':total,'schema':m['schema']},sort_keys=True));return 0
 except (Invalid,OSError,ValueError,UnicodeError) as e:
  print('FAIL: '+str(e),file=sys.stderr);return 1
if __name__=='__main__':raise SystemExit(main())
