"""Download and verify the five pinned November 16 release inputs."""
from pathlib import Path
import hashlib,json,requests
ROOT=Path(__file__).resolve().parent
for s in json.loads((ROOT/'releases/source-lock-2026-11-16.json').read_text())['sources']:
 target=ROOT/'data/raw-2026-11-16'/s['file'];target.parent.mkdir(parents=True,exist_ok=True)
 if not target.exists():
  with requests.get(s['url'],stream=True,timeout=(15,60)) as r,target.open('xb') as f:
   r.raise_for_status();received=0
   for chunk in r.iter_content(1024*1024):
    received+=len(chunk)
    if received>s['bytes']:raise ValueError('Input exceeds pinned size')
    f.write(chunk)
 with target.open('rb') as f:digest=hashlib.file_digest(f,'sha256').hexdigest()
 assert target.stat().st_size==s['bytes'] and digest==s['sha256'],'Input identity mismatch'
 print(s['file'],'verified')
