#!/usr/bin/env python3
"""Finish a book's graph page after `graphify export html`.

Usage (from the repo root):  python3 tools/graphify-page/finish_html.py books/<slug>

1. Embeds the vis-network library (vendored next to this script) in place of the
   <script src="https://unpkg.com/vis-network..."> tag, so the page draws in the
   claude.ai file preview, which blocks outside scripts.
2. Shows the names of the nodes listed in books/<slug>/graphify-show-labels.txt
   (one node id per line, '#' starts a comment) and of every chapter node
   (ch01..., prologue, interlude, epilogue). graphify only names the most connected
   nodes; the others stay findable by hover, click and search.

Safe to run twice: a page that is already finished is left as it is, apart from labels.
"""
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LIB = os.path.join(HERE, "vis-network-9.1.6.min.js")
CHAPTER = re.compile(r"^(ch\d\d|prologue|interlude|epilogue)$")


def main(book_dir):
    page = os.path.join(book_dir, "graphify-out", "graph.html")
    html = open(page, encoding="utf-8").read()

    tag = re.search(r'<script src="https://unpkg\.com/vis-network[^"]*"[^>]*>\s*</script>', html, re.S)
    if tag:
        lib = open(LIB, encoding="utf-8").read().replace("</script", "<\\/script")
        html = html[: tag.start()] + "<script>" + lib + "</script>" + html[tag.end():]
        print("embedded the vis-network library")

    show = set()
    listing = os.path.join(book_dir, "graphify-show-labels.txt")
    if os.path.exists(listing):
        for line in open(listing, encoding="utf-8"):
            nid = line.split("#", 1)[0].strip()
            if nid:
                show.add(nid)

    m = re.search(r"(const RAW_NODES = )(\[.*?\])(;\n)", html, re.S)
    if not m:
        sys.exit("graph.html: node list not found; the page format may have changed")
    nodes = json.loads(m.group(2))
    named = 0
    for n in nodes:
        if n["id"] in show or CHAPTER.match(n["id"]):
            # Big enough to stay readable when the whole graph is in view (the library hides
            # names that would draw smaller than a few pixels), with a dark outline.
            font = dict(n.get("font") or {})
            font["size"] = 26 if CHAPTER.match(n["id"]) else 22
            font.setdefault("strokeWidth", 4)
            font.setdefault("strokeColor", "rgba(10,10,20,0.85)")
            n["font"] = font
            named += 1
    missing = sorted(show - {n["id"] for n in nodes})
    html = html[: m.start(2)] + json.dumps(nodes, ensure_ascii=False) + html[m.end(2):]
    # Let names draw down to 2 px instead of the library's default 5 px.
    marker = "/* finish_html: label threshold */"
    if marker not in html:
        html = re.sub(r"(const network = new vis\.Network\([\s\S]*?\}\);\n)",
                      lambda mm: mm.group(1) + marker + "\nnetwork.setOptions({ nodes: { scaling: { label: { drawThreshold: 2 } } } });\n",
                      html, count=1)
    open(page, "w", encoding="utf-8").write(html)
    print(f"names shown for {named} listed and chapter nodes")
    if missing:
        print("not in the graph (check graphify-show-labels.txt):", ", ".join(missing))


if __name__ == "__main__":
    main(sys.argv[1])
