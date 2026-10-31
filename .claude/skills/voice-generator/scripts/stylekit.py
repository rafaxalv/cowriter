"""Stylistic measurements and passage sampling for library texts (standard library only).

Usage:
  python3 -I stylekit.py metrics --lang en|pt|es FILE [FILE ...]      # comparison table (markdown)
  python3 -I stylekit.py metrics --lang pt --json FILE ...             # same, as JSON
  python3 -I stylekit.py sample --lang en FILE --out passages.md [--n 12] [--size 450]

"metrics" measures the observable surface of a text: sentence and paragraph shape, dialogue share,
punctuation, chaining, vocabulary range, and rates of word families that signal how a writer handles
feeling, interiority, perception, the body and explanation. The word lists are deliberately small and
editable (LEX below); treat the rates as comparisons between authors in the same language, not as
absolute truths. Translations measure the translator's surface as much as the author's.

"sample" picks passages for close reading (the event analysis in the voice-generator skill): chapter
openings and endings, dialogue-heavy, action/violence-heavy, feeling-heavy and quiet passages, spread
across the whole book. The output is a working file; do not commit it.
"""
import argparse, json, math, re, statistics, sys

LEX = {
    "en": {
        "emotion": "afraid fear feared fright terror terrified angry anger rage furious happy happiness glad joy joyful sad sadness sorrow grief grieved ashamed shame guilt guilty proud pride jealous envy hate hated hatred love loved lonely loneliness anxious anxiety nervous despair hope hoped hopeless disgust disgusted horror horrified delight delighted miserable misery worried worry upset relief relieved bitter bitterness tender tenderness pity",
        "cognition": "thought think thinking knew know known realized realised understood understand wondered wonder remembered remember forgot forget believed believe supposed imagined imagine decided felt feel feeling seemed considered meant guessed doubted",
        "perception": "saw see seen looked look watched watch noticed heard hear listened listen smelled smelt smell tasted taste touched touch glimpsed stared",
        "body": "hand hands eyes eye face mouth lips throat heart chest stomach belly skin blood breath back shoulders legs feet fingers head hair teeth tongue neck knees arm arms sweat",
        "explain": "because since therefore thus so-that hence consequently which-meant in-order-to that-is reason why",
        "violence": "blood kill killed killing dead death shot shoot gun knife whip whipped beat beaten struck hit wound wounded fire burned scream screamed fight fought bayonet corpse bodies",
        "and": "and",
        "adverb_suffix": "ly",
    },
    "pt": {
        "emotion": "medo temor terror raiva ódio odio fúria furia alegria feliz felicidade contente tristeza triste mágoa magoa dor vergonha culpa orgulho ciúme ciume inveja amor amava saudade solidão solidao angústia angustia ansiedade aflição aflicao desespero esperança esperanca nojo horror pavor alívio alivio pena ternura rancor desgosto susto",
        "cognition": "pensou pensava pensar pensamento sabia saber soube percebeu percebia compreendeu entendeu entendia lembrou lembrava lembrar esqueceu acreditava julgou julgava imaginou imaginava decidiu sentiu sentia sentir parecia achava achou desconfiou duvidava",
        "perception": "viu via ver olhou olhava olhar enxergou notou ouviu ouvia ouvir escutou escutava cheirou cheiro provou tocou sentiu-se avistou fitou",
        "body": "mão mãos mao maos olhos olho cara rosto boca lábios labios garganta coração coracao peito barriga pele sangue fôlego folego costas ombros pernas pés pes dedos cabeça cabeca cabelo dentes língua lingua pescoço pescoco joelhos braço braços suor",
        "explain": "porque pois porquanto portanto por-isso já-que visto-que de-modo-que a-fim-de ou-seja razão motivo",
        "violence": "sangue matar matou morto morte tiro faca chicote açoite acoite surra bateu pancada ferida ferido fogo queimou grito gritou briga brigou baioneta cadáver cadaver",
        "and": "e",
        "adverb_suffix": "mente",
    },
    "es": {
        "emotion": "miedo temor terror rabia ira odio furia alegría alegria feliz felicidad tristeza triste pena dolor vergüenza verguenza culpa orgullo celos envidia amor amaba soledad angustia ansiedad desesperación desesperacion esperanza asco horror pavor alivio ternura rencor susto",
        "cognition": "pensó penso pensaba pensar sabía sabia saber supo comprendió comprendio entendió entendio recordó recordo recordaba olvidó olvido creía creia imaginó imagino decidió decidio sintió sintio sentía sentia parecía parecia",
        "perception": "vio veía veia ver miró miro miraba mirar notó noto oyó oyo oía oia escuchó escucho olió olio probó tocó toco divisó",
        "body": "mano manos ojos ojo cara rostro boca labios garganta corazón corazon pecho vientre piel sangre aliento espalda hombros piernas pies dedos cabeza pelo dientes lengua cuello rodillas brazo brazos sudor",
        "explain": "porque pues puesto-que ya-que por-eso por-lo-tanto así-que de-modo-que para-que es-decir razón motivo",
        "violence": "sangre matar mató mato muerto muerte tiro cuchillo látigo latigo golpe golpeó herida herido fuego quemó grito gritó pelea peleó bayoneta cadáver cadaver",
        "and": "y",
        "adverb_suffix": "mente",
    },
}

WORD = re.compile(r"[^\W\d_]+(?:[-'’][^\W\d_]+)*", re.UNICODE)
ABBREV = re.compile(r"\b(Mr|Mrs|Ms|Dr|St|Sr|Sra|Srta|Dn|Dna|D|Sto|Sta|Gen|Col|Capt|Lt|Rev|etc|vs|p)\.", re.I)


def load_body(path):
    t = open(path, encoding="utf-8").read()
    if "\n---\n" in t[:3000]:  # skip the library header
        t = t.split("\n---\n", 1)[1]
    return t


def paragraphs(t):
    return [p.strip() for p in re.split(r"\n\s*\n", t) if p.strip()]


def is_heading(p):
    return p.startswith("#") or (len(p) < 60 and p.upper() == p and len(WORD.findall(p)) <= 8)


def sentences(p):
    p = ABBREV.sub(lambda m: m.group(0).replace(".", "§"), p)
    parts = re.split(r"(?<=[.!?…])[\"”’»)]*\s+(?=[\"“‘«(—–-]?\s*[A-ZÀ-Ý¿¡])", p)
    return [s.replace("§", ".").strip() for s in parts if WORD.search(s)]


def dialogue_words(p):
    """Words inside dialogue: quoted speech, or paragraphs that open with a dialogue dash."""
    if re.match(r"^\s*[—–]", p) or re.match(r"^\s*-\s", p):
        # dash dialogue: speech minus the narrator's tag between dashes
        tags = re.findall(r"[—–]\s*(?:disse|perguntou|respondeu|gritou|dijo|preguntó|respondió|gritó)[^—–]*", p)
        return max(0, len(WORD.findall(p)) - sum(len(WORD.findall(x)) for x in tags))
    q = re.findall(r"[“\"«]([^”\"»]+)[”\"»]", p)
    return sum(len(WORD.findall(x)) for x in q)


def lexset(lang, key):
    return {w.replace("-", " ") for w in LEX[lang][key].split()}


def rate(tokens, text_lower, words, n):
    single = {w for w in words if " " not in w}
    multi = [w for w in words if " " in w]
    c = sum(1 for t in tokens if t in single) + sum(text_lower.count(" " + m + " ") for m in multi)
    return 1000 * c / max(n, 1)


def mattr(tokens, w=500):
    if len(tokens) < w:
        return len(set(tokens)) / max(len(tokens), 1)
    vals = [len(set(tokens[i:i + w])) / w for i in range(0, len(tokens) - w, w // 2)]
    return statistics.mean(vals)


def metrics(path, lang):
    t = load_body(path)
    paras = [p for p in paragraphs(t) if not is_heading(p)]
    sents = [s for p in paras for s in sentences(p)]
    slen = [len(WORD.findall(s)) for s in sents]
    tokens = [w.lower() for w in WORD.findall(t)]
    n = len(tokens)
    low = " " + " ".join(tokens) + " "
    plen = [len(WORD.findall(p)) for p in paras]
    psent = [len(sentences(p)) for p in paras]
    dlg = sum(dialogue_words(p) for p in paras)
    punct = lambda ch: 100 * t.count(ch) / max(n, 1)
    andw = LEX[lang]["and"]
    suf = LEX[lang]["adverb_suffix"]
    return {
        "file": path.split("/")[-1],
        "words": n,
        "sentence length: mean": round(statistics.mean(slen), 1),
        "sentence length: median": statistics.median(slen),
        "sentence length: spread (sd)": round(statistics.pstdev(slen), 1),
        "short sentences (<=6 words) %": round(100 * sum(1 for x in slen if x <= 6) / len(slen), 1),
        "long sentences (>=35 words) %": round(100 * sum(1 for x in slen if x >= 35) / len(slen), 1),
        "paragraph length: mean words": round(statistics.mean(plen), 1),
        "one-sentence paragraphs %": round(100 * sum(1 for x in psent if x == 1) / len(psent), 1),
        "dialogue share of words %": round(100 * dlg / max(n, 1), 1),
        "commas per 100 words": round(punct(","), 2),
        "semicolons+colons per 100 words": round(punct(";") + punct(":"), 2),
        "dashes per 100 words": round(punct("—") + punct("–"), 2),
        "questions+exclamations per 100 words": round(punct("?") + punct("!"), 2),
        f"'{andw}' per sentence": round(sum(1 for x in tokens if x == andw) / len(sents), 2),
        "vocabulary range (MATTR-500)": round(mattr(tokens), 3),
        f"-{suf} adverbs per 1000": round(1000 * sum(1 for x in tokens if x.endswith(suf) and len(x) > len(suf) + 3) / n, 1),
        "named emotions per 1000": round(rate(tokens, low, lexset(lang, "emotion"), n), 2),
        "thinking/knowing/feeling verbs per 1000": round(rate(tokens, low, lexset(lang, "cognition"), n), 2),
        "perception verbs per 1000": round(rate(tokens, low, lexset(lang, "perception"), n), 2),
        "body words per 1000": round(rate(tokens, low, lexset(lang, "body"), n), 2),
        "explanation markers per 1000": round(rate(tokens, low, lexset(lang, "explain"), n), 2),
        "violence words per 1000": round(rate(tokens, low, lexset(lang, "violence"), n), 2),
    }


def sample(path, lang, n, size, out):
    t = load_body(path)
    raw = paragraphs(t)
    chunks, cur, start_flags = [], [], []
    chapter_start = True
    for p in raw:
        if is_heading(p):
            if cur:
                chunks.append((cur, start_flag, True)); cur = []
            chapter_start = True
            continue
        if not cur:
            start_flag = chapter_start; chapter_start = False
        cur.append(p)
        if sum(len(WORD.findall(x)) for x in cur) >= size:
            chunks.append((cur, start_flag, False)); cur = []
    if cur:
        chunks.append((cur, start_flag, True))
    emo, vio, body = lexset(lang, "emotion"), lexset(lang, "violence"), lexset(lang, "body")
    rows = []
    for i, (ps, is_open, is_end) in enumerate(chunks):
        text = "\n\n".join(ps)
        toks = [w.lower() for w in WORD.findall(text)]
        k = max(len(toks), 1)
        rows.append({"i": i, "text": text, "open": is_open, "end": is_end,
                     "dlg": sum(dialogue_words(p) for p in ps) / k,
                     "vio": sum(1 for x in toks if x in vio) / k,
                     "emo": sum(1 for x in toks if x in emo or x in body) / k})
    total = len(rows)
    picked, used = [], set()

    def far(i):  # keep picks spread across the book
        return all(abs(i - j) > max(2, total // (n * 2)) for j in used)

    def take(kind, cands, k):
        for r in cands:
            if len([p for p in picked if p[0] == kind]) >= k:
                break
            if r["i"] not in used and far(r["i"]) and len(r["text"].split()) > size * 0.5:
                picked.append((kind, r)); used.add(r["i"])

    per = max(1, n // 6)
    take("chapter opening", [r for r in rows if r["open"]][::max(1, len([r for r in rows if r["open"]]) // (per * 2) or 1)], per)
    take("chapter ending", [r for r in rows if r["end"]][::-1], per)
    take("dialogue scene", sorted(rows, key=lambda r: -r["dlg"]), per)
    take("action / violence", sorted(rows, key=lambda r: -r["vio"]), per)
    take("feeling / body", sorted(rows, key=lambda r: -r["emo"]), per)
    take("quiet / transition", sorted(rows, key=lambda r: r["dlg"] + r["vio"] + r["emo"]), n - len(picked))
    picked.sort(key=lambda p: p[1]["i"])
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"# Passages for close reading: {path.split('/')[-1]}\n\nWorking file, not for the repo. "
                f"{len(picked)} passages of about {size} words, spread across the book.\n\n")
        for k, (kind, r) in enumerate(picked, 1):
            f.write(f"## P{k:02d} · {kind} · position {100 * r['i'] // max(total, 1)}% of the book\n\n{r['text']}\n\n")
    print(f"{len(picked)} passages -> {out}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["metrics", "sample"])
    ap.add_argument("files", nargs="+")
    ap.add_argument("--lang", required=True, choices=list(LEX))
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--out", default="passages.md")
    ap.add_argument("--n", type=int, default=12)
    ap.add_argument("--size", type=int, default=450)
    a = ap.parse_args()
    if a.cmd == "sample":
        return sample(a.files[0], a.lang, a.n, a.size, a.out)
    res = [metrics(f, a.lang) for f in a.files]
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=1)); return
    keys = list(res[0])
    print("| Measure | " + " | ".join(r["file"].replace(".txt", "") for r in res) + " |")
    print("| --- |" + " --- |" * len(res))
    for k in keys[1:]:
        print(f"| {k} | " + " | ".join(str(r[k]) for r in res) + " |")


if __name__ == "__main__":
    main()
