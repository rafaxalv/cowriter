"""Convert a Standard Ebooks source repo (git clone of github.com/standardebooks/<repo>) into one plain-text file.

Usage: python3 -I standardebooks2txt.py <cloned-repo-dir> <out.txt>
Translators are read from the repo name (author_title_translator1_translator2)."""
import sys, re, os
from html.parser import HTMLParser
import xml.etree.ElementTree as ET

SKIP = {"imprint", "colophon", "uncopyright", "titlepage", "loi", "toc"}
BLOCK = {"p", "div", "section", "article", "blockquote", "br", "li", "tr", "header", "footer", "hr"}
HEAD = {"h1", "h2", "h3", "h4", "h5", "h6", "hgroup"}


class T(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, a):
        a = dict(a)
        if tag in ("style", "script", "head") or "noteref" in (a.get("epub:type") or ""):
            self.skip += 1
            return
        if tag in HEAD:
            self.out.append("\n\n## ")
        elif tag in BLOCK:
            self.out.append("\n\n" if tag != "br" else "\n")

    def handle_endtag(self, tag):
        if tag in ("style", "script", "head") or (self.skip and tag == "a"):
            if self.skip:
                self.skip -= 1
            return
        if tag in HEAD or tag in BLOCK:
            self.out.append("\n\n")

    def handle_data(self, d):
        if not self.skip:
            self.out.append(re.sub(r"\s+", " ", d))


def convert(repo, out):
    epub = os.path.join(repo, "src", "epub")
    ns = {"o": "http://www.idpf.org/2007/opf", "dc": "http://purl.org/dc/elements/1.1/"}
    opf = ET.parse(os.path.join(epub, "content.opf")).getroot()
    title = opf.find(".//dc:title", ns).text
    creators = [c.text for c in opf.findall(".//dc:creator", ns)]
    slug = os.path.basename(repo.rstrip('/')).split('_')[2:]
    contribs = [" ".join(w.upper() + "." if len(w) == 1 else w.title() for w in x.split("-")) for x in slug]
    man = {i.get("id"): i.get("href") for i in opf.find("o:manifest", ns)}
    parts = []
    for ref in opf.find("o:spine", ns):
        href = man[ref.get("idref")]
        if os.path.splitext(os.path.basename(href))[0] in SKIP:
            continue
        p = T()
        p.feed(open(os.path.join(epub, href), encoding="utf-8").read())
        parts.append("".join(p.out))
    body = "\n".join(parts)
    body = re.sub(r"[ \t]+\n", "\n", body)
    body = re.sub(r"\n[ \t]+", "\n", body)
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    head = (f"# {title}\n\nBy {', '.join(creators)}. Translated by {', '.join(contribs)}.\n\n"
            f"Public-domain translation. Source: Standard Ebooks (https://github.com/standardebooks/{os.path.basename(repo.rstrip('/'))}), "
            f"based on Project Gutenberg transcriptions; dedicated to the public domain (CC0).\n"
            f"Kept as a style reference for the book voices. Plain text converted from the Standard Ebooks source.\n\n---\n\n")
    open(out, "w", encoding="utf-8").write(head + body + "\n")
    return title, len(body.split())


if __name__ == "__main__":
    t, n = convert(sys.argv[1], sys.argv[2])
    print(f"{n:>8} words  {t}")
