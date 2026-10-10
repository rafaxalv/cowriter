#!/usr/bin/env python3
"""Write the manuscript editor's store back into a book folder.

Usage: python3 tools/manuscript-editor/sync_back.py books/<slug> <dump_dir>

<dump_dir> holds the store documents as saved by the ArtifactData tool with
`out_dir` (<dump_dir>/books/<slug>/paragraphs/*.json, .../voices/*.json,
.../heatmaps/*.json; the book document itself is not needed).

Updates, in the book folder:
  - every manuscript file listed in BOOK.md: paragraph text, order and IDs
    (removed paragraphs are dropped; chapters with none get the placeholder)
  - config/paragraph-parameters.csv: one row per paragraph
  - config/engagement.csv: the latest heatmap scores of the first language
Everything else in the files (title, intro, part headings) is kept.
Prints a short summary; review with `git diff` before committing.
"""
import csv, datetime, glob, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from export_book import DIMS, chap_id  # noqa: E402

PLACEHOLDER = {"en": "*(to be written)*", "pt_br": "*(a escrever)*"}


def load_docs(folder):
    out = {}
    for f in glob.glob(os.path.join(folder, "*.json")):
        d = json.load(open(f, encoding="utf-8"))
        if isinstance(d, dict) and "data" in d and isinstance(d["data"], dict) and ("version" in d or "id" in d):
            d = d["data"]
        out[os.path.basename(f)[:-5]] = d
    return out


def words(t, n=6):
    w = t.split()
    return " ".join(w[:n]) + (" …" if len(w) > n else "")


def rewrite_manuscript(path, lang_key, paras):
    by_ch = {}
    for p in paras:
        if not p.get("removed"):
            by_ch.setdefault(p["chapter"], []).append(p)
    for v in by_ch.values():
        v.sort(key=lambda p: p["order"])
    lines = open(path, encoding="utf-8").read().split("\n")
    out, skipping, seen = [], False, set()
    for line in lines:
        m = re.match(r"(#{1,3}) (.+)$", line)
        if m:
            cid = chap_id(m.group(2)) if len(m.group(1)) > 1 else None
            if out and out[-1].strip():
                out.append("")
            out.append(line)
            skipping = bool(cid)
            if cid:
                seen.add(cid)
                out.append("")
                ps = by_ch.get(cid, [])
                if not ps:
                    out += [PLACEHOLDER.get(lang_key, "*(to be written)*"), ""]
                for p in ps:
                    out += [f"<!-- {p['pid']} -->", (p.get("text", {}).get(lang_key) or "").strip() or "*(empty)*", ""]
            continue
        if not skipping:
            out.append(line)
    missing = set(by_ch) - seen
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
    open(path, "w", encoding="utf-8").write(text)
    return missing


def main(book_dir, dump):
    slug = os.path.basename(os.path.normpath(book_dir))
    base = os.path.join(dump, "books", slug)
    paras = list(load_docs(os.path.join(base, "paragraphs")).values())
    voices = load_docs(os.path.join(base, "voices"))
    heat = load_docs(os.path.join(base, "heatmaps"))
    profile = open(os.path.join(book_dir, "BOOK.md"), encoding="utf-8").read()
    langs = [(c, c.lower().replace("-", "_"), p) for c, _, p in
             re.findall(r"^\| ([A-Z]{2}(?:-[A-Z]{2})?) \| ([^|]+?) \| `([^`]+)` \|", profile, re.M)]
    for code, key, rel in langs:
        miss = rewrite_manuscript(os.path.join(book_dir, rel), key, paras)
        if miss:
            print(f"warning: {rel} has no heading for chapters {sorted(miss)}; their paragraphs were not written")
        print("updated", rel)

    first = langs[0][1]
    dim_name = {str(n): name for _, n, name, *_ in DIMS}
    pp_path = os.path.join(book_dir, "config/paragraph-parameters.csv")
    header = next(csv.reader(open(pp_path, encoding="utf-8")))
    old = {r["Paragraph ID"]: r for r in csv.DictReader(open(pp_path, encoding="utf-8"))}
    ch_order = {}
    for p in paras:
        ch_order.setdefault(p["chapter"], len(ch_order))
    def key(p):
        return (0 if p["chapter"] == "00" else 2 if p["chapter"] == "99" else 1, p["chapter"], p["order"])
    rows = []
    for p in sorted(paras, key=key):
        r = dict.fromkeys(header, "")
        r.update(old.get(p["pid"], {}))
        r["Paragraph ID"], r["Chapter"] = p["pid"], p["chapter"]
        for col in header:
            m = re.match(r"Opening words \((\w+)\)", col)
            if m:
                k = next((lk for c, lk, _ in langs if c.split("-")[0] == m.group(1).split("-")[0]), None)
                if k:
                    r[col] = words(p.get("text", {}).get(k, ""))
        r["Voice ID"] = p.get("voice", "")
        r["Voice version"] = voices.get(p.get("voice", ""), {}).get("version", "") if p.get("voice") else ""
        r["Tuning"] = "; ".join(f"{dim_name[n]} {'+' if v > 0 else ''}{v}" for n, v in sorted(p.get("tuning", {}).items(), key=lambda kv: int(kv[0])) if v)
        r["Reason for tuning"] = p.get("reason", "")
        r["Review status"] = "removed" if p.get("removed") else p.get("status", "")
        r["Open issues"] = p.get("notes", "")
        if p.get("updatedAt"):
            r["Last reviewed"] = r.get("Last reviewed", "") if p.get("status") in ("", "draft") else datetime.date.fromtimestamp(p["updatedAt"] / 1000).isoformat()
        h = heat.get(f"{p['chapter']}_{first}")
        ss = [s for s in (h or {}).get("sentences", []) if s["pid"] == p["pid"]]
        if ss:
            r["Engagement avg"] = f"{sum(s['e'] for s in ss) / len(ss):.1f}"
            r["Engagement peak"] = str(max(s["e"] for s in ss))
        rows.append(r)
    with open(pp_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=header); w.writeheader(); w.writerows(rows)
    print("updated config/paragraph-parameters.csv:", len(rows), "rows")

    en_path = os.path.join(book_dir, "config/engagement.csv")
    eh = next(csv.reader(open(en_path, encoding="utf-8")))
    keep = [r for r in csv.DictReader(open(en_path, encoding="utf-8"))]
    texts = {p["pid"]: p.get("text", {}).get(first, "") for p in paras}
    scored_ch = set()
    new = []
    for hid, h in sorted(heat.items()):
        if h.get("lang") != first:
            continue
        scored_ch.add(h["chapter"])
        date = datetime.date.fromtimestamp(h["runAt"] / 1000).isoformat()
        for s in h["sentences"]:
            sent = texts.get(s["pid"], "")[s["start"]:s["end"]]
            new.append({"Paragraph ID": s["pid"], "Sentence": s["i"] + 1, "Opening words": words(sent),
                        "Engagement": s["e"], "Tension": s["t"], "Emotion": s["m"], "Pace": s["p"],
                        "Hot words": "; ".join(s.get("hot", [])), "Uncertain": "yes" if s.get("u") else "",
                        "Reason": s.get("r", ""), "Date": date})
    keep = [r for r in keep if r["Paragraph ID"].split(".")[0] not in scored_ch]
    with open(en_path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=eh); w.writeheader(); w.writerows(keep + new)
    print("updated config/engagement.csv:", len(new), "scored sentences from", sorted(scored_ch) or "no chapters")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
