#!/usr/bin/env python3
"""Export a book folder into the documents the manuscript editor reads.

Usage: python3 tools/manuscript-editor/export_book.py books/<slug> <out_dir>

Writes one JSON file per document under <out_dir>, mirroring the editor's
store paths (see README.md):
  books/<slug>.json                      the book: title, languages, chapters, dimensions
  books/<slug>/paragraphs/<pid>.json     one per paragraph: text per language, voice, tuning
  books/<slug>/voices/<ID>.json          one per voice with a target-profile table
Upload them with the ArtifactData tool (batch, file_path).
"""
import csv, json, os, re, sys, unicodedata

DIMS = [
    ("A", 1, "Narrative distance", "far, panoramic", "inside a head"),
    ("A", 2, "Narrator presence", "invisible", "comments, judges"),
    ("A", 3, "Point of view range", "one viewpoint", "a chorus"),
    ("A", 4, "Orality", "written prose", "told aloud"),
    ("B", 5, "Sentence length", "short, clipped", "long, flowing"),
    ("B", 6, "Register", "plain words", "elevated"),
    ("B", 7, "Figurative density", "literal", "dense imagery"),
    ("B", 8, "Sensory detail", "sparse", "immersive"),
    ("C", 9, "Scene vs summary", "moment by moment", "years in a line"),
    ("C", 10, "Chronology", "linear", "fragmented"),
    ("C", 11, "Dialogue share", "almost none", "dialogue-driven"),
    ("C", 12, "Pace", "slow", "fast"),
    ("D", 13, "Historical texture", "faint backdrop", "documentary"),
    ("D", 14, "Realism", "strict realism", "myth, legend"),
    ("D", 15, "Causality", "will", "chance, fate"),
    ("E", 16, "Moral stance", "judges", "no verdicts"),
    ("E", 17, "Violence rendering", "offstage", "explicit"),
    ("E", 18, "Emotional temperature", "cool, ironic", "openly emotional"),
]
GROUPS = {"A": "Voice and perspective", "B": "Language", "C": "Time and structure",
          "D": "History and reality", "E": "Emotion and ethics"}


def chap_id(title):
    t = "".join(c for c in unicodedata.normalize("NFD", title.lower()) if not unicodedata.combining(c))
    if "prolog" in t: return "00"
    if "epilog" in t: return "99"
    if "interl" in t: return "INT"
    m = re.match(r"\s*(\d+)\.", title)
    return f"{int(m.group(1)):02d}" if m else None


def parse_manuscript(path):
    """Return (book_title, parts, chapters, paragraphs) for one language file."""
    chapters, paras, part = [], {}, None
    cur = None
    pending_id = None
    title = None
    for line in open(path, encoding="utf-8").read().split("\n"):
        if line.startswith("# ") and title is None:
            title = line[2:].strip(); continue
        m = re.match(r"(#{2,3}) (.+)$", line)
        if m:
            lvl, h = len(m.group(1)), m.group(2).strip()
            cid = chap_id(h)
            if cid:
                cur = {"id": cid, "title": h, "part": part}
                chapters.append(cur)
            elif lvl == 2:
                part = h
            continue
        m = re.match(r"<!--\s*([0-9A-Za-z]+\.[0-9]+[a-z]?)\s*-->", line.strip())
        if m:
            pending_id = m.group(1); continue
        if pending_id and line.strip():
            paras[pending_id] = (cur["id"] if cur else None, line.strip())
            pending_id = None
    return title, chapters, paras


def voice_profile(path):
    text = open(path, encoding="utf-8").read()
    m = re.search(r"^# ([A-Z0-9-]+):\s*(.+)$", text, re.M)
    vid, name = (m.group(1), m.group(2).strip()) if m else (os.path.basename(path)[:-3], "")
    sec = re.search(r"## Target profile.*?\n(.*?)(?:\n## |\Z)", text, re.S)
    dims = {}
    if sec:
        for row in sec.group(1).split("\n"):
            c = [x.strip() for x in row.strip().strip("|").split("|")]
            if len(c) >= 3 and re.match(r"^\d+ ", c[0]):
                n = int(c[0].split()[0])
                try:
                    base = int(c[1]); rng = [int(x) for x in re.split(r"\s*[-–]\s*", c[2])]
                    lo, hi = rng[0], rng[-1]
                except ValueError:
                    continue
                dims[str(n)] = {"base": base, "min": lo, "max": hi, "note": c[3] if len(c) > 3 else ""}
    ver = re.search(r"\*\*Version\*\*:\s*([0-9.]+)", text)
    return vid, {"id": vid, "name": name, "version": ver.group(1) if ver else "", "dims": dims}


def main(book_dir, out):
    slug = os.path.basename(os.path.normpath(book_dir))
    profile = open(os.path.join(book_dir, "BOOK.md"), encoding="utf-8").read()
    # Languages from the profile's Languages table: | CODE | Name | `path` | ...
    langs = []
    for code, name, path in re.findall(r"^\| ([A-Z]{2}(?:-[A-Z]{2})?) \| ([^|]+?) \| `([^`]+)` \|", profile, re.M):
        langs.append({"key": code.lower().replace("-", "_"), "code": code, "name": name.strip(), "file": path})
    first = langs[0]["key"]
    chapters, texts, book_title = {}, {}, None
    order_ch = []
    for lg in langs:
        title, chs, paras = parse_manuscript(os.path.join(book_dir, lg["file"]))
        if lg["key"] == first:
            book_title = title
        for c in chs:
            if c["id"] not in chapters:
                chapters[c["id"]] = {"id": c["id"], "titles": {}, "part": {}}
                order_ch.append(c["id"])
            chapters[c["id"]]["titles"][lg["key"]] = c["title"]
            chapters[c["id"]]["part"][lg["key"]] = c["part"]
        for pid, (cid, t) in paras.items():
            texts.setdefault(pid, {"chapter": cid, "text": {}})["text"][lg["key"]] = t
    params = {}
    pp = os.path.join(book_dir, "config/paragraph-parameters.csv")
    if os.path.exists(pp):
        for r in csv.DictReader(open(pp, encoding="utf-8")):
            params[r["Paragraph ID"]] = r
    mc = re.search(r"^- \*\*In one line\*\*:\s*(.+)$", profile, re.M)
    context = mc.group(1).strip() if mc else ""
    anchors = ""
    ap = os.path.join(book_dir, "config/engagement-anchors.md")
    if os.path.exists(ap):
        # Keep only the level sections that hold agreed paragraphs.
        for lvl, body in re.findall(r"^## (\d[^\n]*)\n(.*?)(?=^## |\Z)", open(ap, encoding="utf-8").read(), re.M | re.S):
            if body.strip():
                anchors += f"Level {lvl}:\n{body.strip()}\n"
    m = re.search(r"^- \*\*Working title\*\*:\s*(.+)$", profile, re.M)
    book = {
        "slug": slug, "title": (re.sub(r"\s*\(to decide\)\.?$", "", m.group(1).strip()) if m else book_title),
        "languages": langs,
        "chapters": [chapters[c] for c in order_ch],
        "dims": [{"n": n, "group": g, "groupName": GROUPS[g], "name": nm, "low": lo, "high": hi} for g, n, nm, lo, hi in DIMS],
        "syncedAt": None,
        "context": context, "anchors": anchors,
    }
    write(out, f"books/{slug}.json", book)
    ch_pos = {c: i for i, c in enumerate(order_ch)}
    def key(pid):
        c, r = pid.split(".")
        return (ch_pos.get(c, 999), int(re.match(r"\d+", r).group()), r)
    for i, pid in enumerate(sorted(texts, key=key)):
        p = params.get(pid, {})
        tuning = {}
        for part in filter(None, re.split(r"\s*;\s*", p.get("Tuning", ""))):
            mm = re.match(r"(.+?)\s*([+-]\d+)$", part)
            if mm:
                name = mm.group(1).strip().lower()
                for g, n, nm, *_ in DIMS:
                    if nm.lower().startswith(name) or name.startswith(nm.lower().split()[0]):
                        tuning[str(n)] = int(mm.group(2)); break
        write(out, f"books/{slug}/paragraphs/{pid}.json", {
            "pid": pid, "chapter": texts[pid]["chapter"], "order": (i + 1) * 1000,
            "text": texts[pid]["text"], "voice": p.get("Voice ID", ""), "tuning": tuning,
            "reason": p.get("Reason for tuning", ""), "status": p.get("Review status", "") or "draft",
            "notes": p.get("Open issues", ""), "updatedAt": None,
        })
    # Context for paragraph tuning in the editor: the same files the paragraph-review skill reads.
    def read(rel):
        f = os.path.join(book_dir, rel)
        return open(f, encoding="utf-8").read() if os.path.exists(f) else ""
    write(out, f"books/{slug}/context/book.json", {
        "profile": profile,
        "concept": read("outline/concept.md"),
        "sharedRules": read("voices/00-shared-rules.md"),
        "lexicon": read("voices/00-bilingual-lexicon.md"),
        "characterBible": read("characters/character-bible.md"),
    })
    plan, scenes = section_by_chapter(read("outline/chapters.md"), r"^#{2,3} "), {}
    for head, body in re.findall(r"^## (Chapter[^\n]*)\n(.*?)(?=^## |\Z)", read("outline/scenes.md"), re.M | re.S):
        m = re.match(r"Chapter (\d+|[A-Za-z]+)", head)
        cid = chap_id(m.group(1) + ".") if m and m.group(1).isdigit() else chap_id(head)
        if cid:
            scenes[cid] = "## " + head + "\n" + body.strip()
    for cid in order_ch:
        write(out, f"books/{slug}/context/ch-{cid}.json", {"chapter": cid, "plan": plan.get(cid, ""), "scenes": scenes.get(cid, "")})
    skill = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.claude/skills/paragraph-review/SKILL.md")
    if os.path.exists(skill):
        write(out, "skills/paragraph-review.json", {"text": open(skill, encoding="utf-8").read()})
    vdir = os.path.join(book_dir, "voices")
    for f in sorted(os.listdir(vdir)):
        if f.endswith(".md") and not f.startswith("00-") and re.match(r"[A-Z]", f):
            vid, v = voice_profile(os.path.join(vdir, f))
            v["text"] = open(os.path.join(vdir, f), encoding="utf-8").read()
            write(out, f"books/{slug}/voices/{vid}.json", v)


def section_by_chapter(text, head_re):
    """Split a plan file into {chapter id: section text} by its chapter headings."""
    out, cur, buf = {}, None, []
    for line in text.split("\n"):
        if re.match(head_re, line):
            if cur:
                out[cur] = "\n".join(buf).strip()
            cur = chap_id(line.lstrip("#").strip().replace("\\", ""))
            buf = [line] if cur else []
            continue
        if cur:
            buf.append(line)
    if cur:
        out[cur] = "\n".join(buf).strip()
    return out


def write(out, rel, obj):
    p = os.path.join(out, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(obj, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(rel)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
