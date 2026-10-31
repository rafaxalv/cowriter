"""Strip a Project Gutenberg plain-text file (or a GITenberg clone's .txt) down to the book itself.

Usage: python3 -I gutenberg2txt.py <in.txt> <out.txt> "<Title>" "<Author>" "<language>" "<source line>"

Removes the Project Gutenberg header and license (between the *** START / *** END markers),
so the file no longer carries the Project Gutenberg name, as their license asks. Detects UTF-8
or Latin-1.
"""
import re, sys

src, out, title, author, lang, source = sys.argv[1:7]
raw = open(src, "rb").read()
try:
    t = raw.decode("utf-8")
except UnicodeDecodeError:
    t = raw.decode("latin-1")
t = t.replace("\r\n", "\n").lstrip("﻿")
m = re.search(r"\*\*\* ?START OF.*?\*\*\*\n", t)
e = re.search(r"\n\*\*\* ?END OF", t) or re.search(r"\nEnd of (the )?Project Gutenberg", t)
body = t[m.end() if m else 0:e.start() if e else len(t)].strip()
head = (f"# {title}\n\nBy {author}. {lang}.\n\nPublic-domain text. Source: {source} "
        "(header and license block removed).\nKept as a style reference for the book voices.\n\n---\n\n")
open(out, "w", encoding="utf-8").write(head + body + "\n")
print(len(body.split()), "words", title, "" if m and e else "(WARNING: start/end markers not found, check it)")
