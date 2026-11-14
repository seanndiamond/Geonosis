#!/usr/bin/env python3
import hashlib
from pathlib import Path
import sys

if len(sys.argv) != 3:
    raise SystemExit("usage: seal_blind_key.py PRIVATE_KEY.csv OUTPUT_HASH.txt")

src = Path(sys.argv[1])
out = Path(sys.argv[2])
digest = hashlib.sha256(src.read_bytes()).hexdigest()
out.write_text(digest + "\n", encoding="utf-8")
print(digest)
