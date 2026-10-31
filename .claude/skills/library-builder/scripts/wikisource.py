"""Polite Wikisource downloader: one book, chapter by chapter, saved as plain text.

Usage:
  python3 -I wikisource.py search <host> "<query>"            # list matching page titles
  python3 -I wikisource.py book <host> "<Page title>" <out.txt> "<Author>" "<language>"

<host> is e.g. pt.wikisource.org or es.wikisource.org. Wikimedia throttles shared cloud
addresses, so every request is paced (PACE seconds) and a 429 backs off (60 s, 120 s, ...).
Run long books in the background; the script resumes from <out.txt>.parts/ if interrupted.
"""
import json, os, re, sys, time, urllib.error, urllib.parse, urllib.request
from html.parser import HTMLParser

UA = "CowriterLibrary/1.0 (personal reference library; contact via github.com/rafaxalv) python-urllib"
PACE = 6
DROP = ("ws-noexport", "noprint", "pagenum", "mw-editsection", "reference", "ws-header",
        "navbox", "mw-references", "cabecalho", "cabeçalho", "headertemplate", "licensecontainer")
VOID = {"br", "img", "hr", "input", "meta", "link", "wbr", "col", "area", "source"}
BLOCK = ("p", "div", "h1", "h2", "h3", "h4", "li", "dd", "tr", "blockquote", "poem")


def get(url, tries=8):
    for k in range(tries):
        time.sleep(PACE)
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA})
            with urllib.request.urlopen(req, timeout=40) as r:
                body = r.read().decode("utf-8", "replace")
            if "Wikimedia Error" in body[:3000] and "Too many requests" in body[:3000]:
                raise urllib.error.HTTPError(url, 429, "rate limited", None, None)
            return body
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return None
            wait = 60 * (k + 1) if e.code == 429 else 20
            print(f"  HTTP {e.code}, waiting {wait}s", flush=True)
            time.sleep(wait)
        except Exception as e:
            print(f"  error {e}, waiting 20s", flush=True)
            time.sleep(20)
    raise SystemExit(f"gave up on {url}")


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.stack, self.skip = [], [], 0

    def handle_starttag(self, tag, attrs):
        if tag in VOID:
            if tag == "br" and not self.skip:
                self.out.append("\n")
            return
        a = dict(attrs)
        cls = ((a.get("class") or "") + " " + (a.get("id") or "")).lower()
        drop = tag in ("style", "script") or (tag == "sup" and "reference" in cls) \
            or any(d in cls for d in DROP)
        self.stack.append(drop)
        if drop:
            self.skip += 1
        elif not self.skip and tag in BLOCK:
            self.out.append("\n\n" + ("## " if tag in ("h2", "h3", "h4") else ""))

    def handle_endtag(self, tag):
        if tag in VOID or not self.stack:
            return
        if self.stack.pop():
            self.skip -= 1
        elif not self.skip and tag in BLOCK:
            self.out.append("\n\n")

    def handle_data(self, d):
        if not self.skip:
            self.out.append(re.sub(r"\s+", " ", d))


def text_of(html):
    p = Text()
    p.feed(html)
    t = "".join(p.out)
    t = re.sub(r"[ \t]+\n", "\n", t)
    t = re.sub(r"\n[ \t]+", "\n", t)
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def render(host, title):
    q = urllib.parse.quote(title.replace(" ", "_"))
    return get(f"https://{host}/w/index.php?title={q}&action=render")


def subpages(host, title, html):
    pref = title.replace(" ", "_") + "/"
    out = []
    for m in re.finditer(r'href="[^"]*?/wiki/([^"#?]+)"', html):
        t = urllib.parse.unquote(m.group(1))
        if t.startswith(pref) and t.replace("_", " ") not in out:
            out.append(t.replace("_", " "))
    return out


def search(host, q):
    b = get(f"https://{host}/w/api.php?action=opensearch&limit=10&namespace=0&format=json&search="
            + urllib.parse.quote(q))
    for t in json.loads(b)[1]:
        print(t)


def book(host, title, out, author, lang):
    parts_dir = out + ".parts"
    os.makedirs(parts_dir, exist_ok=True)
    html = render(host, title)
    if html is None:
        raise SystemExit(f"not found: {title}")
    subs = subpages(host, title, html)
    sections = []
    if not subs:
        sections.append((title, text_of(html)))
    for i, s in enumerate(subs):
        cache = os.path.join(parts_dir, f"{i:03d}.txt")
        if os.path.exists(cache):
            sections.append((s, open(cache, encoding="utf-8").read()))
            continue
        print(f"  [{i + 1}/{len(subs)}] {s}", flush=True)
        h = render(host, s)
        inner = subpages(host, s, h or "")
        if inner:  # an edition or part page that lists its own chapters
            t = "\n\n".join(f"## {c.split('/')[-1]}\n\n{text_of(render(host, c) or '')}" for c in inner)
        else:
            t = text_of(h or "")
        open(cache, "w", encoding="utf-8").write(t)
        sections.append((s, t))
    body = "\n\n".join(f"## {s.split('/')[-1]}\n\n{t}" if len(sections) > 1 else t for s, t in sections)
    words = len(body.split())
    head = (f"# {title}\n\nBy {author}. Original {lang}.\n\n"
            f"Public domain (check the library README for where). Source: https://{host}/wiki/"
            f"{urllib.parse.quote(title.replace(' ', '_'))}\nKept as a style reference for the book voices.\n\n---\n\n")
    open(out, "w", encoding="utf-8").write(head + body + "\n")
    print(f"saved {words} words -> {out}" + ("  (WARNING: short, check it)" if words < 3000 else ""), flush=True)


if __name__ == "__main__":
    if sys.argv[1] == "search":
        search(sys.argv[2], sys.argv[3])
    else:
        book(*sys.argv[2:7])
