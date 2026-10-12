"""Read and write a book's Chapters file (the plan of record) as items.

A chapter entry in the Chapters file has this shape once organized by the editor:

    ### 1\\. Good Teeth

      - When / where: before and around his birth (1846) · Salvador and the Recôncavo
      - Stories:

          - An event of the chapter. (Sources: S2)
      - Facts:

          - [DOCUMENTED] A historical fact the chapter relies on. (Sources: S1, S2) (to verify)
      - Sources:

          - [S1] Author, title, link. (Research file: `research/paraguayan-war/slavery-timeline.md`)
      - Notes:

          - An open question or option.

Older entries keep everything under "Stories:" (and the interlude uses top-level bullets);
on reading, bullets that start with "Sources" / "Further reading" become sources and bullets
that start with "IMPORTANT" / "The laws that shape" become facts. Text outside chapter entries
(the file's introduction, part introductions, the arc brainstorm) is never touched.
"""
import re
import unicodedata

KINDS = {"event": "Stories", "fact": "Facts", "source": "Sources", "note": "Notes"}
SECTION_KIND = {v.lower(): k for k, v in KINDS.items()}
SECTION_KIND.update({"story": "event", "events": "event", "open items": "note", "open": "note"})


def chap_id(title):
    t = "".join(c for c in unicodedata.normalize("NFD", title.lower()) if not unicodedata.combining(c))
    t = t.replace("\\", "")
    if "prolog" in t: return "00"
    if "epilog" in t: return "99"
    if "interl" in t: return "INT"
    m = re.match(r"\s*(\d+)\.", t)
    return f"{int(m.group(1)):02d}" if m else None


def classify(text):
    t = text.lstrip("*_ ").lower()
    if re.match(r"(sources?\b|further reading|reading\b|bibliograph)", t):
        return "source"
    if re.match(r"(important\b|the laws that shape|historical ground\b|fact\b)", t):
        return "fact"
    return "event"


SRC_REF = re.compile(r"\s*\(Sources?:\s*((?:S\d+\s*,?\s*)+)\)")
VERIFY = re.compile(r"\s*\(to verify\)\s*$", re.I)
LABEL = re.compile(r"^\[([A-Z][A-Z ]+)\]\s*")
SRC_ID = re.compile(r"^\[S(\d+)\]\s*")
FILE = re.compile(r"\s*\(Research file:\s*`([^`]+)`\)")


def parse(text):
    """Return {chapter id: {"title", "when", "items": [...]}} in file order."""
    chapters, cur, kind_ctx, order = {}, None, None, []
    for line in text.split("\n"):
        h = re.match(r"(#{2,3}) (.+)$", line)
        if h:
            cid = chap_id(h.group(2))
            cur = None
            if cid and not h.group(2).lower().startswith("arc brainstorm"):
                cur = chapters.setdefault(cid, {"title": h.group(2).strip(), "when": "", "items": []})
                order.append(cid)
            kind_ctx = None
            continue
        if cur is None:
            continue
        m1 = re.match(r"  - (.+)$", line)
        m2 = re.match(r"      - (.+)$", line)
        if m1:
            body = m1.group(1).strip()
            w = re.match(r"When\s*/\s*where:\s*(.*)$", body)
            if w:
                cur["when"] = w.group(1).strip(); kind_ctx = None; continue
            sec = re.match(r"([A-Za-z ]+):\s*$", body)
            if sec and sec.group(1).strip().lower() in SECTION_KIND:
                kind_ctx = SECTION_KIND[sec.group(1).strip().lower()]; continue
            cur["items"].append(item_from(body, classify(body)))  # top-level bullet (interlude style)
            kind_ctx = None
        elif m2:
            body = m2.group(1).strip()
            k = kind_ctx if kind_ctx and kind_ctx != "event" else classify(body)
            cur["items"].append(item_from(body, k))
        elif line.strip() and cur["items"] and line.startswith("        "):
            cur["items"][-1]["text"] += "\n" + line.strip()
    # resolve "S1" references to source positions within each chapter
    for ch in chapters.values():
        srcs = [it for it in ch["items"] if it["kind"] == "source"]
        for i, s in enumerate(srcs):
            s["_n"] = s.pop("_sid", None) or i + 1
        by_n = {s["_n"]: s for s in srcs}
        for it in ch["items"]:
            it["sourceRefs"] = [by_n[n] for n in it.pop("_refs", []) if n in by_n]
    return chapters, order


def item_from(body, kind):
    it = {"kind": kind, "text": body, "label": "", "verify": False, "file": "", "_refs": []}
    if VERIFY.search(it["text"]):
        it["verify"] = True; it["text"] = VERIFY.sub("", it["text"])
    m = SRC_REF.search(it["text"])
    if m:
        it["_refs"] = [int(x) for x in re.findall(r"\d+", m.group(1))]
        it["text"] = SRC_REF.sub("", it["text"]).rstrip()
    if kind == "fact":
        m = LABEL.match(it["text"])
        if m:
            it["label"] = m.group(1).strip(); it["text"] = it["text"][m.end():]
    if kind == "source":
        m = SRC_ID.match(it["text"])
        if m:
            it["_sid"] = int(m.group(1)); it["text"] = it["text"][m.end():]
        m = FILE.search(it["text"])
        if m:
            it["file"] = m.group(1); it["text"] = FILE.sub("", it["text"]).rstrip()
    return it


def render_chapter(when, items):
    """Markdown body for one chapter entry (without its heading)."""
    srcs = [it for it in items if it["kind"] == "source"]
    num = {it["id"]: i + 1 for i, it in enumerate(srcs)}
    out = [""]
    if when:
        out.append(f"  - When / where: {when}")
    for kind, title in KINDS.items():
        group = [it for it in items if it["kind"] == kind]
        if not group:
            continue
        out += [f"  - {title}:", "      "]
        for it in group:
            t = " ".join(it["text"].split("\n")).strip()
            if kind == "fact" and it.get("label"):
                t = f"[{it['label']}] {t}"
            if kind == "source":
                t = f"[S{num[it['id']]}] {t}"
                if it.get("file"):
                    t += f" (Research file: `{it['file']}`)"
            refs = [num[s] for s in it.get("sources", []) if s in num]
            if refs and kind != "source":
                t += " (Sources: " + ", ".join(f"S{n}" for n in sorted(refs)) + ")"
            if it.get("verify"):
                t += " (to verify)"
            out.append(f"      - {t}")
    out.append("")
    return out


def rewrite(text, chapters):
    """Replace each chapter entry's body in `text` with the items in `chapters` (by chapter id)."""
    out, skipping = [], False
    for line in text.split("\n"):
        h = re.match(r"(#{1,3}) (.+)$", line)
        if h:
            cid = chap_id(h.group(2)) if len(h.group(1)) > 1 and not h.group(2).lower().startswith("arc brainstorm") else None
            if cid and cid in chapters:
                ch = chapters[cid]
                out.append(f"{h.group(1)} {ch.get('title') or h.group(2)}")
                out += render_chapter(ch.get("when", ""), ch["items"])
                skipping = True
                continue
            skipping = False
            out.append(line)
            continue
        if not skipping:
            out.append(line)
    t = "\n".join(out)
    return re.sub(r"\n{3,}", "\n\n", t).rstrip() + "\n"
