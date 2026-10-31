"""Usage: python3 -I rda2txt.py <file.rda> <out.txt> "<Author>" "<source line>"

Extract a literaturaBR .rda (columns book_name, chapter_name, url, paragraph_number, text) to plain text."""
import bz2, gzip, lzma, struct, sys


def strings(b):
    out, i = [], 0
    while i < len(b) - 8:
        flags = struct.unpack('>I', b[i:i + 4])[0]
        if flags & 0xff == 9:
            n = struct.unpack('>i', b[i + 4:i + 8])[0]
            if n == -1:  # NA_STRING
                out.append(None); i += 8; continue
            if n == 0:
                out.append(''); i += 8; continue
            if 0 < n < 500000 and i + 8 + n <= len(b):
                try:
                    t = b[i + 8:i + 8 + n].decode('utf-8')
                    if flags != 9 or not any(ord(c) < 9 for c in t):
                        out.append(t); i += 8 + n; continue
                except UnicodeDecodeError:
                    pass
        i += 1
    return out


def load(f):
    raw = open(f, 'rb').read()
    for d in (bz2.decompress, gzip.decompress, lzma.decompress):
        try:
            return d(raw)
        except Exception:
            pass
    return raw


src, dst, author, source = sys.argv[1:5]
s = strings(load(src))
title = max(set(x for x in s if x), key=s.count)
start = s.index(title)
n = 0
while s[start + n] == title:
    n += 1
chapters = s[start + n:start + 2 * n]
end = next(k for k in range(len(s) - 1) if s[k] == 'names' and s[k + 1] == 'book_name')
clean = [x for x in s[start + 3 * n:end] if x is None or not any(ord(c) < 9 for c in x)]
clean = [x for x in clean if x not in ('class', 'data.frame', 'row.names', 'tbl_df', 'tbl')]
texts = clean[-n:]
print('extra strings dropped:', len(clean) - n)
assert len(texts) == n and 'names' not in texts[:5], 'layout mismatch'
lines, last = [], None
for ch, t in zip(chapters, texts):
    if ch != last:
        lines.append(f"\n## {ch}\n"); last = ch
    if t and t.strip():
        lines.append(t.strip() + "\n")
head = (f"# {title}\n\nBy {author}. Original Portuguese.\n\nPublic domain. Source: {source}\n"
        "Kept as a style reference for the book voices.\n\n---\n")
open(dst, 'w', encoding='utf-8').write(head + "\n".join(lines))
print(n, 'paragraphs', sum(len((t or '').split()) for t in texts), 'words', title)
