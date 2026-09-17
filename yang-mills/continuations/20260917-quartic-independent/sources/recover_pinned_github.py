#!/usr/bin/env python3
"""Optional, explicit network recovery of the immutable cubic PR8 text sources.

This is a recovery helper, not an executed receipt for this session. It only
reads public GitHub content, validates every original Git blob, and writes files.
It never executes downloaded programs and never overwrites conflicting files.
"""
from __future__ import annotations
import argparse,hashlib,json,time
from pathlib import Path
from urllib.error import HTTPError,URLError
from urllib.parse import quote
from urllib.request import Request,urlopen
REPO='KokunoYumeto/yang-mills-interacting-workbench'
REV='91434b6962062bd80439d4cb2cae9d2479264dde'
DIRECTORY='yang-mills/continuations/20260916-cubic-linearized'
ALLOWED={'.md','.py','.json','.txt','.tex','.patch'}
LIMIT=4*1024*1024

def get(url):
    request=Request(url,headers={'User-Agent':'pinned-Yang-Mills-source-recovery','Accept':'application/vnd.github+json'})
    with urlopen(request,timeout=30) as response:
        data=response.read(LIMIT+1)
        if len(data)>LIMIT:raise ValueError('source-response-too-large')
        return data

def gitblob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()

def recover(destination):
    listing=json.loads(get(f'https://api.github.com/repos/{REPO}/contents/{DIRECTORY}?ref={REV}'))
    if not isinstance(listing,list) or len(listing)>100:raise ValueError('unexpected-source-listing')
    destination.mkdir(parents=True,exist_ok=True);records=[]
    for row in listing:
        name=row.get('name','');p=Path(name)
        if row.get('type')!='file' or p.name!=name or p.is_absolute() or '..' in p.parts:raise ValueError('unsafe-source-path')
        if p.suffix not in ALLOWED:continue
        path=f'{DIRECTORY}/{name}';url=f'https://raw.githubusercontent.com/{REPO}/{REV}/{quote(path,safe="/")}'
        data=get(url)
        data.decode('utf-8')
        if gitblob(data)!=row['sha']:raise ValueError('Git-blob-mismatch:'+name)
        out=destination/name
        if out.exists() and out.read_bytes()!=data:raise ValueError('existing-file-conflict:'+name)
        out.write_bytes(data);records.append({'path':path,'commit':REV,'git_blob':row['sha'],'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
        print('Verified original source:',name,flush=True)
    report={'repository':REPO,'commit':REV,'retrieved_at_unix_time':time.time(),'downloaded_code_executed':False,'files':records}
    (destination/'RECOVERY_RECEIPT.json').write_text(json.dumps(report,indent=2,sort_keys=True)+'\n')

if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('destination',type=Path);args=parser.parse_args()
    try:recover(args.destination)
    except (OSError,HTTPError,URLError,ValueError,KeyError) as e:raise SystemExit('Recovery failed: '+str(e))
