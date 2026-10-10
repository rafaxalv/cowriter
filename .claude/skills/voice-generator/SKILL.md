---
name: "voice-generator"
description: "Use when the author wants to create a new voice or update an existing one for a book in this repo: it checks the current voices with book-voices first, then compares reference authors with a fixed style framework, rewrites sample paragraphs, and blends and adjusts the style, with a shared core and a layer per language of the book."
---

# Voice generator: from reference authors to a finished voice

This skill compares authors' styles with a fixed framework and helps the author turn the styles they like into a **voice** for their book, or update a voice that already exists. It never works in isolation: it always starts and ends by exchanging information with the **book-voices** skill, which governs all voices. It runs in a check-in step plus six stages. Each stage ends by showing the result and waiting for the author. They can jump into any stage directly ("rewrite this paragraph as author X", "generate the voice rules"), but the check-in step always runs first.

Every voice is **multilingual** when the book is: one shared core that defines the voice, plus one language layer per language of the book. See "Multilingual voices".

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask.
2. Read `BOOK.md`: languages, people and roles (for example a co-author whose wording is the source in one language), the voices folder and its files, voice decisions so far, and the profile's notes for the skills (vocabulary, untranslated words, native models per language).
3. Read the Concept: its story, how it is told, tone and handle-with-care notes are the context for every stage below.

## Where the work is saved

In the book's voices folder (owned by book-voices; paths from the profile):

- Every author analyzed goes into the **Author Library** (tags, 18 scores with reasons, portrait). Check the library first and reuse analyses instead of redoing them.
- Author searches (sources, shortlists, the author's selections and decisions) are recorded in an **author search** file in the voices folder (for example `author-search-YYYY-MM.md`), and the file is listed in the profile.
- Language-wide word and translation decisions go into the **Bilingual Lexicon** (through book-voices).
- Voice files and the Voice Index are owned by book-voices. This skill never writes them directly; it hands a finished voice package to book-voices (Stage 6).

---

## The style framework (fixed, use it every time)

### Fixed tags (record for every author, voice and paragraph; not scored)

- **Narrative person**: 1st / 2nd / 3rd / mixed (say which parts use which).
- **Addressed to**: no one / the reader / a specific person inside the story (a son, a sister, an interviewer).
- **Form**: plain narration / spoken telling / letter / diary / testimony or interview / document / mixed.
- **Literacy** of the voice: cannot write (spoken or dictated) / barely literate / basic / educated / formal or official, plus the first language and regional or period speech. For authors, note the literacy of the voices they write (for example: ordinary people speaking, mostly plain and unschooled).
- **Language**: for authors, the language they write in, and whether they were read in the original or in translation (a translation is partly the translator's style; say so). For voices and paragraphs, which language layer applies.

### The 18 scored dimensions

Each is a spectrum from 1 to 5 with a named pole at each end; 3 means balanced or mixed. Always give a one-line reason for each score, based on observed features of the text, not on reputation.

#### A. Voice and perspective
1. **Narrative distance**: 1 = far away, panoramic, chronicle-like / 5 = deep inside a character's head
2. **Narrator presence**: 1 = invisible narrator / 5 = narrator comments, judges, addresses the reader
3. **Point of view range**: 1 = one fixed viewpoint / 5 = many shifting viewpoints, a chorus
4. **Orality**: 1 = written, literary prose / 5 = sounds like a story told aloud (repetition, digressions, "they say")

#### B. Language
5. **Sentence length and rhythm**: 1 = short, clipped / 5 = long, flowing, many clauses
6. **Register**: 1 = plain, everyday words / 5 = elevated, ornate, rare vocabulary
7. **Figurative density**: 1 = literal / 5 = dense with metaphor and image, lyrical
8. **Sensory detail**: 1 = sparse, only what is needed / 5 = immersive smells, textures, sounds

#### C. Time and structure
9. **Scene vs summary**: 1 = moment-by-moment scenes / 5 = summary, years in a sentence
10. **Chronology**: 1 = strictly linear / 5 = fragmented, jumps back and forth
11. **Dialogue share**: 1 = almost no dialogue / 5 = dialogue-driven
12. **Pace**: 1 = slow, contemplative / 5 = fast, plot-forward

#### D. History and reality
13. **Historical texture**: 1 = history as a faint backdrop / 5 = dense documentary detail (dates, ranks, objects, places)
14. **Realism**: 1 = strict realism / 5 = myth, legend, magical realism
15. **Causality**: 1 = events driven by characters' will / 5 = events driven by chance, fate, luck

#### E. Emotion and ethics
16. **Moral stance**: 1 = text clearly judges right and wrong / 5 = fully ambiguous, no verdicts
17. **Violence rendering**: 1 = offstage, implied / 5 = explicit, close up
18. **Emotional temperature and irony**: 1 = understated, cool, ironic / 5 = openly emotional, earnest

Present scores as a table (authors as columns, the tags at the top, then the dimensions as rows) and, when useful, offer a visual comparison (a radar or heat-map chart, or an interactive page with sliders).

Do not add, drop or rename tags or dimensions on the fly. If the author wants to change the framework itself, propose an update to this skill (it applies to every book).

---

## Multilingual voices

The approach is the same in every language; the means differ. A reader of each language version should meet the same character, the same distance, the same tone, the same effect, built with what each language does naturally. Never produce one language as a word-for-word translation of another.

### The core (shared by all languages)

Tags, literacy level, the 18-dimension target profile with base values and tuning ranges, the voice rules, the conveying-feeling rules, the neighbour voices. The core is what makes it the same voice.

### The language layer (one per language of the book)

1. **Reference authors for this language**, with weights. They can differ from the core references: the best model for how a voice sounds in a language is usually a writer who writes natively in it. When a core reference is a translated author, name which translation serves as the model.
2. **Profile offsets**: small, deliberate differences from the core on the language-sensitive dimensions only (4 Orality, 5 Sentence length and rhythm, 6 Register, 7 Figurative density, 11 Dialogue share), at most ±1, each with a reason (for example "+1 sentence length: this language carries long subordinate chains naturally; the same effect in the other needs shorter sentences"). All other dimensions stay identical to the core.
3. **Vocabulary strategy**: which word stock carries the voice (for example, in English, plain Anglo-Saxon words vs Latinate ones); regional and period words; words to avoid (anachronisms, modern slang, usage from the wrong country or region); which story words stay untranslated in the other languages and how they are made clear by context, never by a footnote. Start from the profile's notes and the Bilingual Lexicon.
4. **Phrase-building strategies**: how sentences are built to get the voice's effect in this language (for example chains of "and", parataxis, contractions or none; inversions, gerunds, diminutives, pronoun placement, dropped subjects, repetition as in speech).
5. **Address and dialogue**: forms of address and their period weight, and how the same distance is carried into the other languages; dialogue punctuation (for example quotation marks vs dashes).
6. **Literacy markers in this language**: how this character's schooling shows in this language without caricature (non-standard forms, dropped agreement, missing accents in letters, simple tenses, run-on sentences, phonetic spellings used sparingly). The level is the same in every language; the markers are native to each.
7. **Rhythm note**: languages differ in length; judge rhythm by the effect on the reader, not by word count.
8. **Language rules**: 2-5 extra rules that only apply in this language, each with a do and don't example.
9. **Reference paragraph** written natively in this language.

Decisions that apply across all voices (glossary terms, words kept untranslated, spelling of place names, period terms) go to the Bilingual Lexicon through book-voices, not into a single voice.

---

## Stage 0: Check in with book-voices (always first)

Before any author search or rewriting, follow the book-voices skill to read the Voice Index and the voice files that could be relevant. Then decide, and tell the author in one or two lines, which of these applies:

- **Update**: a voice for this need already exists. Work on that voice. Start from its current core, language layers, ranges, rules and reference paragraphs; do not start from zero.
- **Derive**: a close voice exists (for example a base voice, and a new character needs their own version). Create a new voice that starts as a copy of the close one, then adjust it.
- **New**: nothing similar exists. Create a voice from scratch.

Also say which part is being worked on: the core, one language layer (for example "only one language sounds wrong") or both. If it is unclear, show the candidate voices and ask. Then get a **voice brief** from book-voices (its contents are listed in the book-voices skill).

For an **Update**, the author may not need all stages: often Stage 3 (rewrite a sample) and Stage 5 (adjust by hand) are enough. Offer the shortest path.

## Stage 1: Find reference authors

First check the Author Library, the author search records and the reference authors the voice already uses. If new authors are needed, search the web; do not rely on memory for who is popular now. Propose 12-15 candidates in three groups, with one line each on why they fit, the language they write in, and a source:

- **Popular now**: current bestsellers and recent prize winners in the book's languages and genre (national bestseller lists, the main literary prizes of each language, Goodreads/BookTok trends).
- **Classics with similar stories**: important past writers of the book's subjects, settings and forms, from the literatures of the book's languages and world literature.
- **Wildcards**: 2-3 authors whose style is very different, to stretch the comparison.

Make sure each language has at least two candidates who write natively in it, so each language layer has a native model. When the voice being built has a specific form or literacy (letters, testimony, an unschooled speaker), also suggest authors known for that form or those kinds of voices. Record the search (sources and shortlist) in the book's author search file.

Ask the author to pick 4-7 for the next stages, and which of them should guide each language.

## Stage 2: Analyze the selected authors

For each author not already in the library: record the tags (including language and whether read in translation), score all 18 dimensions with reasons, and write a short style portrait (5-8 lines) covering signature techniques, how they work history or the world in without info-dumping, and their hook. For authors who write in one of the book's languages, add a short note on their vocabulary and phrase-building habits in that language. Then show the comparison table, say where the authors differ most, what fits or clashes with the book's tone (from the Concept), and which kinds of voices (narrator, letters, testimony...) and which language layer each would suit. Save new analyses to the Author Library.

**Example passages.**
- For public-domain authors (for example, works by authors who died more than 70 years ago), quote a short representative passage and name the work.
- For authors still in copyright, do not reproduce their text. Name 1-2 specific books and chapters where the style shows best, describe what happens on the page, and rely on Stage 3 to show the style in action.

## Stage 3: Rewrite one of the author's paragraphs in each style

Use a paragraph from the book (pasted, or from the manuscript, ideally one that already uses this voice), or one written for the voice being built. Keep the same events, facts and characters. Apply the literacy profile from the voice brief to every version, so each sample already sounds like the character. Rewrite it once per selected author, matching that author's tags and scores (a first-person author's version is in the first person; for a letter voice, write it as a letter). For an Update, also show the paragraph in the voice's current form, so the change is visible. Original writing only, never copied phrases from the author. Under each version, 2-3 notes on which dimensions changed most, and flag any version where the style adds invented details. When the paragraph belongs to a scene that has a **Reader feeling** in Scenes, aim every version at that feeling and note how each style gets the reader there (senses, implication, statement, rhythm).

Write each sample in the language of the layer being worked on. When working on several, write each language **natively** (not one translated from another) and add a line on what each language does differently to get the same effect. Default: the language the profile marks as written first; offer the others for any version the author likes.

## Stage 4: Choose or blend

The author picks one style, or two to combine (for an Update, the current voice can be one of the two). For a blend: set the tags (person, addressed to, form, literacy), start from the average of the two scores, then ask which should lead on each dimension where they differ by 2 or more. This becomes the **core**. Then, for each language, pick the language references and propose the offsets, vocabulary strategy and phrase-building strategies. Show the core next to the **neighbour voices** from the brief, flag any neighbour that is now too similar (most dimensions within 1 point) or a consistency conflict, and rewrite the paragraph in every language.

## Stage 5: Adjust by hand

The author changes the voice in plain words or by setting numbers, either for the whole voice ("less metaphor", "violence stays offstage") or for one language ("more regional words", "this language sounds too formal"). Change the core for whole-voice requests and the language layer for language requests; keep offsets within ±1 and say so if a request would push a language too far from the core (then it is really a core change). Rewrite the paragraph, show what changed, and keep checking against the neighbour voices. Repeat until the author is happy with every language. Keep a short change log. If the profile names a co-author whose wording is the source in a language, their text is a strong signal for how that layer should sound: when they have written in this voice, use their text as a model and ask before changing their habits.

## Stage 6: Hand the voice package to book-voices (when the author says "generate rules" or "save the voice")

Build a **voice package** and give it to book-voices, which validates and saves it:

- **Mode and ID**: New, Derive (from which voice) or Update (with the version it updates).
- **Core**: tags and literacy level; reference authors with weights; the 18 dimensions with base values and allowed tuning ranges (ask the author where they want room to vary); voice rules (5-12, each checkable on one paragraph, written as rule, why, do example, don't example; not vague); **conveying-feeling rules** (2-4: how the voice makes the reader feel a scene's Reader feeling: senses or statement, implied or shown, whether feelings are named, how a shift is marked, how far it goes with disgust, horror or tenderness; consistent with dimensions 8, 17 and 18 and with the handle-with-care notes; each with do and don't examples).
- **One language layer per language of the book**: language references, offsets with reasons, vocabulary strategy, phrase-building strategies, address and dialogue, literacy markers, language rules, and a reference paragraph written natively in that language.
- **Proposed lexicon entries**: words and translation decisions that should apply across voices, for the Bilingual Lexicon.
- **For an Update**: a short before/after of what changed (core and/or which layer), and the chapters and paragraphs that use the voice and may need a new chapter-review.
- **Proposed shared rules**: any rule that applies to every voice, proposed for the Shared Rules instead.

If book-voices finds a problem (too close to another voice, a literacy detail that does not fit the period, a clash with shared rules, layers that no longer feel like the same voice), go back to Stage 5 with the author, then hand over again. book-voices saves the voice file, the Voice Index, the version and the change log after the author approves.

---

## General notes

- Be honest: if a style clashes with the book's tone (for example, a moralizing narrator in a book with no verdicts), say so.
- Never reproduce long passages from in-copyright books, and do not imitate an author by copying their sentences. Style is shown through original writing.
- When the author writes in another of the book's languages, answer about that text in that language if they prefer, and make sure every core rule works in every language.
- Keep questions short; offer sensible defaults.
