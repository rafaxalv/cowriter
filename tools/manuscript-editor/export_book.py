#!/usr/bin/env python3
"""Export a book folder into the documents the manuscript editor reads.

Usage: python3 tools/manuscript-editor/export_book.py books/<slug> <out_dir>

Writes one JSON file per document under <out_dir>, mirroring the editor's
store paths (see README.md):
  books/<slug>.json                      the book: title, languages, chapters, dimensions
  books/<slug>/paragraphs/<pid>.json     one per paragraph: text per language, own voice (if any), status
  books/<slug>/chapterVoice/<id>.json    one per chapter: voice, tuning, reason (config/chapter-voices.csv)
  books/<slug>/voices/<ID>.json          one per voice with a target-profile table
Upload them with the ArtifactData tool (batch, file_path).
"""
import csv, glob, json, os, re, sys, unicodedata

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

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
    ("F", 19, "Event entry", "from the beginning", "in the middle"),
    ("F", 20, "Event exit", "to the aftermath", "cut at the peak"),
    ("F", 21, "Peak treatment", "compressed, skipped", "slowed, beat by beat"),
    ("F", 22, "Action granularity", "outcomes", "every step"),
    ("F", 23, "Feeling rendering", "named, explained", "never named"),
    ("F", 24, "Interior access", "seen from outside", "continuous inner life"),
    ("F", 25, "Reader inference", "spelled out", "much left unsaid"),
    ("F", 26, "Dialogue subtext", "says what it means", "meaning under the words"),
    ("G", 27, "Scene length", "many short scenes", "few long scenes"),
    ("G", 28, "Scene opening", "orientation first", "in the action"),
    ("G", 29, "Scene ending", "resolved", "cut on an image or line"),
    ("G", 30, "Transitions", "bridged by summary", "hard cuts, jumps"),
    ("G", 31, "Scene focus", "one beat", "several threads"),
]
GROUPS = {"A": "Voice and perspective", "B": "Language", "C": "Time and structure",
          "D": "History and reality", "E": "Emotion and ethics",
          "F": "Narrative technique", "G": "Scene architecture"}


def parse_tuning(text):
    """'Narrative distance -1; Pace +1' -> {"1": -1, "12": 1} (names matched loosely against DIMS)."""
    tuning = {}
    for part in filter(None, re.split(r"\s*;\s*", text or "")):
        mm = re.match(r"(.+?)\s*([+-]\d+)$", part)
        if mm:
            name = mm.group(1).strip().lower()
            for g, n, nm, *_ in DIMS:
                if nm.lower().startswith(name) or name.startswith(nm.lower().split()[0]):
                    tuning[str(n)] = int(mm.group(2)); break
    return tuning


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
    chvoices = {}
    cvp = os.path.join(book_dir, "config/chapter-voices.csv")
    if os.path.exists(cvp):
        for r in csv.DictReader(open(cvp, encoding="utf-8")):
            chvoices[r["Chapter"]] = r
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
        "truthLabels": truth_labels(profile), "research": research_files(book_dir),
    }
    write(out, f"books/{slug}.json", book)
    ch_pos = {c: i for i, c in enumerate(order_ch)}
    def key(pid):
        c, r = pid.split(".")
        return (ch_pos.get(c, 999), int(re.match(r"\d+", r).group()), r)
    for i, pid in enumerate(sorted(texts, key=key)):
        p = params.get(pid, {})
        cid = texts[pid]["chapter"]
        own = p.get("Voice ID", "")
        if own == chvoices.get(cid, {}).get("Voice ID", ""):
            own = ""  # same as the chapter's voice: the paragraph follows the chapter
        tun = parse_tuning(chvoices.get(cid, {}).get("Tuning", "")) if not own else {}
        write(out, f"books/{slug}/paragraphs/{pid}.json", {
            "pid": pid, "chapter": cid, "order": (i + 1) * 1000,
            "text": texts[pid]["text"], "voice": own, "appliedTuning": tun,
            "status": p.get("Review status", "") or "draft",
            "notes": p.get("Open issues", ""), "updatedAt": None,
        })
    # Voice settings are per chapter (config/chapter-voices.csv): one voice and one tuning for the whole chapter.
    for cid in order_ch:
        r = chvoices.get(cid, {})
        tun = parse_tuning(r.get("Tuning", ""))
        write(out, f"books/{slug}/chapterVoice/{cid}.json", {
            "chapter": cid, "voice": r.get("Voice ID", ""), "tuning": tun,
            "reason": r.get("Reason for tuning", ""), "updatedAt": None,
        })
    # Context for one-shot rewrites in the editor, kept small: the chapter text itself is the heavy
    # context (the page has it); these are the short briefs the paragraph-review skill asks for.
    def read(rel):
        f = os.path.join(book_dir, rel)
        return open(f, encoding="utf-8").read() if os.path.exists(f) else ""
    book_brief = "\n\n".join(filter(None, [
        md_section(profile, r"People and roles"),
        md_section(profile, r"Standing rules"),
        md_section(read("outline/concept.md"), r"Handle with care"),
        read("voices/00-shared-rules.md").split("## Change log")[0].strip(),
        read("voices/00-bilingual-lexicon.md").strip(),
    ]))
    bible = read("characters/character-bible.md")
    continuity = bible[bible.index("# Continuity"):].strip() if "# Continuity" in bible else ""
    write(out, f"books/{slug}/context/book.json", {"brief": book_brief, "continuity": continuity})
    plan, scenes = section_by_chapter(read("outline/chapters.md"), r"^#{2,3} "), {}
    for head, body in re.findall(r"^## (Chapter[^\n]*)\n(.*?)(?=^## |\Z)", read("outline/scenes.md"), re.M | re.S):
        m = re.match(r"Chapter (\d+)", head)
        cid = chap_id(m.group(1) + ".") if m else chap_id(head)
        if cid:
            scenes[cid] = scene_brief(head, body)
    for cid in order_ch:
        brief = scenes.get(cid) or (("(No scene map yet. Start of the chapter's plan:)\n" + plan[cid][:1500]) if plan.get(cid) else "")
        write(out, f"books/{slug}/context/ch-{cid}.json", {"chapter": cid, "brief": brief})
    skill = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../.claude/skills/paragraph-review/SKILL.md")
    if os.path.exists(skill):
        st = open(skill, encoding="utf-8").read()
        m = re.search(r"^### Rewrite brief[^\n]*\n(.*?)(?=^\*\*From the Manuscript Desk|^#)", st, re.M | re.S)
        write(out, "skills/paragraph-review.json", {"brief": m.group(1).strip() if m else ""})
    # The Chapters file, as items for the editor's Chapters tab.
    export_plan(book_dir, slug, out)
    # Concept, scene maps and research documents, shown read-only in their own tabs.
    export_docs(book_dir, slug, out)
    vdir = os.path.join(book_dir, "voices")
    lab = os.path.join(vdir, "lab")
    deleted = set()
    if os.path.exists(os.path.join(lab, "deleted.json")):
        deleted = set(json.load(open(os.path.join(lab, "deleted.json"), encoding="utf-8")))
    for f in sorted(os.listdir(vdir)):
        if f.endswith(".md") and not f.startswith("00-") and re.match(r"[A-Z]", f):
            vid, v = voice_profile(os.path.join(vdir, f))
            if vid in deleted:
                continue
            v["brief"] = voice_brief(open(os.path.join(vdir, f), encoding="utf-8").read())
            v["origin"] = "file"
            write(out, f"books/{slug}/voices/{vid}.json", v)
    # Voice Lab drafts (voices/lab/<ID>.json) override or add to the voice files until book-voices folds them in.
    if os.path.isdir(lab):
        for f in sorted(os.listdir(lab)):
            if f.endswith(".json") and f != "deleted.json":
                v = json.load(open(os.path.join(lab, f), encoding="utf-8"))
                v["updatedAt"] = None
                write(out, f"books/{slug}/voices/{v['id']}.json", v)
    # Reference authors for the Voice Lab: the book's Author Library table, plus style studies in the shared library.
    for a in reference_authors(book_dir):
        write(out, f"books/{slug}/authors/{a['id']}.json", a)


def reference_authors(book_dir):
    """Authors with scores: the Author Library's comparison table (dimensions as rows) and library/<author>/STYLE.md score tables."""
    out, seen = [], set()
    def slug(x):
        x = unicodedata.normalize("NFKD", x).encode("ascii", "ignore").decode().lower()
        return re.sub(r"[^a-z0-9]+", "-", x).strip("-")
    lib = os.path.join(book_dir, "voices/00-author-library.md")
    if os.path.exists(lib):
        text = open(lib, encoding="utf-8").read()
        rows = [r for r in text.split("\n") if r.startswith("|")]
        if rows:
            names = [re.sub(r"\*", "", c).strip() for c in rows[0].strip().strip("|").split("|")][1:]
            cols = [{"name": n, "scores": {}, "work": ""} for n in names]
            for r in rows[2:]:
                c = [x.strip() for x in r.strip().strip("|").split("|")]
                m = re.match(r"^(\d+)\b", c[0])
                if m:
                    for i, v in enumerate(c[1:len(cols) + 1]):
                        if v.isdigit():
                            cols[i]["scores"][m.group(1)] = int(v)
                elif c[0].lower() == "work":
                    for i, v in enumerate(c[1:len(cols) + 1]):
                        cols[i]["work"] = v
            portraits = dict(re.findall(r"^  - \*\*([^*]+)\*\*:\s*(.+)$", text, re.M))
            for a in cols:
                full = next((k for k in portraits if a["name"].split()[0].lower() in k.lower()), a["name"])
                aid = slug(full)
                seen.add(aid)
                out.append({"id": aid, "name": full, "work": a["work"], "scores": a["scores"],
                            "portrait": portraits.get(full, ""), "source": "voices/00-author-library.md"})
    libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(book_dir))), "library")
    for st in sorted(glob.glob(os.path.join(libdir, "*", "STYLE.md"))):
        text = open(st, encoding="utf-8").read()
        m = re.search(r"^# Style study:\s*(.+)$", text, re.M)
        if not m:
            continue
        name = m.group(1).strip(); aid = slug(name)
        scores = {n: int(v) for n, v in re.findall(r"^\|\s*(\d+)\s*\|[^|]*\|\s*(\d)\s*\|", text, re.M)}
        tech = re.search(r"^## 7\. Techniques a voice can borrow\s*\n(.*?)(?=^## |\Z)", text, re.M | re.S)
        a = next((x for x in out if x["id"] == aid), None)
        rel = os.path.relpath(st, os.path.dirname(libdir))
        if a:
            a["scores"].update(scores); a["styleStudy"] = rel
        else:
            out.append({"id": aid, "name": name, "work": "", "scores": scores, "source": rel, "styleStudy": rel,
                        "portrait": (tech.group(1).strip()[:900] if tech else "")})
    return out


def truth_labels(profile):
    m = re.search(r"\*\*Truth labels\*\*[^:]*:\s*([A-Z][A-Z ,]+[A-Z])", profile)
    return [x.strip() for x in m.group(1).split(",")] if m else []


def research_files(book_dir):
    """Documents in research/ (not images) with their title, for linking sources to them."""
    out = []
    root = os.path.join(book_dir, "research")
    for dirpath, _, files in os.walk(root):
        for f in sorted(files):
            if not f.lower().endswith((".md", ".pdf")):
                continue
            full = os.path.join(dirpath, f)
            rel = os.path.relpath(full, book_dir)
            title = os.path.splitext(f)[0].replace("-", " ")
            if f.endswith(".md"):
                for line in open(full, encoding="utf-8"):
                    if line.startswith("# "):
                        title = re.sub(r"[*_]", "", line[2:]).strip(); break
            out.append({"path": rel, "title": title})
    return sorted(out, key=lambda r: r["path"])


def export_plan(book_dir, slug, out):
    import plan_md
    path = os.path.join(book_dir, "outline/chapters.md")
    if not os.path.exists(path):
        return
    chapters, order = plan_md.parse(open(path, encoding="utf-8").read())
    for cid in order:
        ch = chapters[cid]
        ids = {}
        for i, it in enumerate(ch["items"]):
            ids[id(it)] = f"{cid}-{i + 1:03d}"
        for i, it in enumerate(ch["items"]):
            write(out, f"books/{slug}/plan/{ids[id(it)]}.json", {
                "id": ids[id(it)], "chapter": cid, "order": (i + 1) * 1000, "kind": it["kind"],
                "text": it["text"], "label": it["label"], "verify": it["verify"], "file": it["file"],
                "sources": [ids[id(s)] for s in it["sourceRefs"]], "updatedAt": None,
            })
        write(out, f"books/{slug}/planChapters/{cid}.json", {"chapter": cid, "title": ch["title"], "when": ch["when"], "readiness": ch.get("readiness", ""), "updatedAt": None})


def export_docs(book_dir, slug, out):
    """books/<slug>/docs/<id>: the Concept, the Scenes file's introduction, one scene map per chapter
    (scenes-<chapter>) and each research document (r-<path>), as {id, kind, path, title, chapter, md}."""
    def rd(rel):
        p = os.path.join(book_dir, rel)
        return open(p, encoding="utf-8").read() if os.path.exists(p) else ""
    def doc(did, kind, path, title, md, chapter=None):
        write(out, f"books/{slug}/docs/{did}.json", {"id": did, "kind": kind, "path": path, "title": title, "chapter": chapter, "md": md})
    doc("concept", "concept", "outline/concept.md", "Concept", rd("outline/concept.md"))
    parts = re.split(r"^(?=## )", rd("outline/scenes.md"), flags=re.M)
    doc("scenes", "scenes", "outline/scenes.md", "Scenes", parts[0].strip())
    for part in parts[1:]:
        head = part.split("\n", 1)[0][3:].strip()
        m = re.match(r"Chapter (\d+)", head)
        cid = chap_id(m.group(1) + ".") if m else chap_id(head)
        if cid:
            doc(f"scenes-{cid}", "scenes", "outline/scenes.md", head, part.strip(), cid)
    for r in research_files(book_dir):
        did = "r-" + re.sub(r"[^A-Za-z0-9_.-]+", "-", r["path"][len("research/"):])
        md = rd(r["path"]) if r["path"].endswith(".md") else ""
        doc(did, "research", r["path"], r["title"], md)


def md_section(text, title_re):
    """The body of the first ## section whose title matches, heading included."""
    m = re.search(r"^## (" + title_re + r"[^\n]*)\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return ("## " + m.group(1) + "\n" + m.group(2).strip()) if m else ""


def voice_brief(text):
    """Voice rules, Conveying feeling and the working parts of each language layer; no scores or samples."""
    parts = [md_section(text, r"Voice rules"), md_section(text, r"Conveying feeling")]
    for head, body in re.findall(r"^## (Language layer[^\n]*)\n(.*?)(?=^## |\Z)", text, re.M | re.S):
        body = re.split(r"^\s*- \*\*Reference paragraph", body, flags=re.M)[0]
        body = re.sub(r"^\s*- \*\*References\*\*.*$\n?", "", body, flags=re.M)
        parts.append("## " + head + "\n" + body.strip())
    return "\n\n".join(p for p in parts if p).strip()


def scene_brief(head, body):
    """Per scene: when, where, point of view, beats and Reader feeling; plus the map's header line."""
    keep = ["## " + head]
    intro = body.strip().split("\n\n")[0]
    if not intro.startswith("###"):
        keep.append(intro)
    for line in body.split("\n"):
        s = line.strip()
        if s.startswith("### ") or re.match(r"- (When|Where|POV|Beats|Reader feeling):", s) or (s.startswith("- Scene ") ):
            keep.append(line.rstrip())
    return "\n".join(keep)


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
