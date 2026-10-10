---
name: "voice-generator"
description: "Use when Rafael wants to create a new voice or update an existing one for his book: it checks the current voices with book-voices first, then compares reference authors with a fixed style framework, rewrites sample paragraphs, and blends and adjusts the style, with a shared core and a layer per language (English and Portuguese)."
---

# Voice generator: from reference authors to a finished voice

This skill (formerly called writer-comparison) compares authors' styles with a fixed framework and helps Rafael turn the styles he likes into a **voice** for his book, or update a voice that already exists. It never works in isolation: it always starts and ends by exchanging information with the **book-voices** skill, which governs all voices. It runs in a check-in step plus six stages. Each stage ends by showing the result and waiting for Rafael. He can jump into any stage directly ("rewrite this paragraph as Allende", "generate the voice rules"), but the check-in step always runs first.

Every voice is **multilingual**: one shared core that defines the voice, plus one language layer per language of the book (English and Brazilian Portuguese; more can be added). See "Multilingual voices".

## The book (context for every stage)

- A novel based on his great-great-grandfather, a Brazilian soldier in the Paraguayan War (1864-1870), who later settled in Mato Grosso do Sul (Jacadigo, Corumba). Slavery, war, migration, family.
- History is blended into the fiction, with no factual step-outs from the story.
- Tone: events driven largely by luck and chance. No morals pushed on the reader. No pure heroes or villains. Show contradictions and the reasons behind choices instead of judging.
- Core themes: luck, freedom, violence, money. Freedom is questioned: life after freedom is not much better.
- Framed as a story his grandma used to tell (prologue and epilogue).
- Written in English and Brazilian Portuguese, side by side. Rafael's mom writes parts in Portuguese.

## Where the work is saved

In the **Voices** folder (inside Configuration) in the book's Google Drive (layout defined in the book-voices skill):

- Every author analyzed goes into **00 Author Library** (tags, 18 scores with reasons, portrait). Check the library first and reuse analyses instead of redoing them. Until an author is in the library in Drive, use the analyzed authors recorded at the end of this skill, and copy them in.
- Language-wide word and translation decisions go into **00 Bilingual Lexicon** (owned by book-voices).
- Voice files and the Voice Index are owned by book-voices. This skill never writes them directly; it hands a finished voice package to book-voices (Stage 6).

---

## The style framework (fixed, use it every time)

### Fixed tags (record for every author, voice and paragraph; not scored)

- **Narrative person**: 1st / 2nd / 3rd / mixed (say which parts use which).
- **Addressed to**: no one / the reader / a specific person inside the story (a son, a sister, an interviewer).
- **Form**: plain narration / spoken telling / letter / diary / testimony or interview / document / mixed.
- **Literacy** of the voice: cannot write (spoken or dictated) / barely literate / basic / educated / formal or official, plus the first language and regional or period speech. For authors, note the literacy of the voices they write (for example Alexievich: ordinary people speaking, mostly plain and unschooled).
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

Do not add, drop or rename tags or dimensions on the fly. If Rafael wants to change the framework itself, propose an update to this skill.

---

## Multilingual voices

The approach is the same in every language; the means differ. A reader of the English and a reader of the Portuguese should meet the same character, the same distance, the same tone, the same effect, built with what each language does naturally. Never produce one language as a word-for-word translation of the other.

### The core (shared by all languages)

Tags, literacy level, the 18-dimension target profile with base values and tuning ranges, the voice rules, the conveying-feeling rules, the neighbour voices. The core is what makes it the same voice.

### The language layer (one per language: EN, PT-BR, and any added later)

1. **Reference authors for this language**, with weights. They can differ from the core references: the best model for how a voice sounds in Portuguese is usually a writer who writes in Portuguese (for example Gonçalves, Vieira Junior or Guimarães Rosa for Brazilian orality), and in English a writer who writes in English. When a core reference is a translated author, name which translation serves as the model.
2. **Profile offsets**: small, deliberate differences from the core on the language-sensitive dimensions only (4 Orality, 5 Sentence length and rhythm, 6 Register, 7 Figurative density, 11 Dialogue share), at most ±1, each with a reason (for example "PT +1 sentence length: Portuguese carries long subordinate chains naturally; the same effect in English needs shorter sentences"). All other dimensions stay identical to the core.
3. **Vocabulary strategy**: which word stock carries the voice (in English, plain Anglo-Saxon words vs Latinate ones; in Portuguese, everyday Brazilian words, words of Tupi, Bantu and Yoruba origin, regionalisms from Bahia or Mato Grosso, period words of the 1800s); words to avoid (anachronisms, modern slang, Portugal-only usage in PT-BR); which story words stay untranslated in the English (for example senzala, engenho, sucuri, carta de alforria) and how they are made clear by context, never by a footnote.
4. **Phrase-building strategies**: how sentences are built to get the voice's effect in this language. Examples: in English, chains of "and", parataxis, phrasal verbs, contractions or none; in Portuguese, inversions, gerunds, diminutives and augmentatives, pronoun placement (colloquial proclisis vs formal enclisis), dropped subjects, repetition as in speech.
5. **Address and dialogue**: forms of address and their period weight (sinhô, sinhá, vosmecê, senhor, você, tu; in English, how to carry the same distance: "master", "senhor" kept, titles, first names); dialogue punctuation (English quotation marks; Portuguese travessão).
6. **Literacy markers in this language**: how this character's level of schooling shows in this language without caricature (in Portuguese, for example, "pra", dropped plural agreement, missing accents in letters; in English, for example, simple tenses, run-on sentences, phonetic spellings used sparingly). The level is the same in both languages; the markers are native to each.
7. **Rhythm note**: Portuguese usually runs longer than English; judge rhythm by the effect on the reader, not by word count.
8. **Language rules**: 2-5 extra rules that only apply in this language, each with a do and don't example.
9. **Reference paragraph** written natively in this language.

Decisions that apply across all voices (glossary terms, words kept untranslated, spelling of place names, period terms) go to **00 Bilingual Lexicon** through book-voices, not into a single voice.

---

## Stage 0: Check in with book-voices (always first)

Before any author search or rewriting, follow the book-voices skill to read the **00 Voice Index** and the voice files that could be relevant. Then decide, and tell Rafael in one or two lines, which of these applies:

- **Update**: a voice for this need already exists. Work on that voice. Start from its current core, language layers, ranges, rules and reference paragraphs; do not start from zero.
- **Derive**: a close voice exists (for example the base voice for letters from women in desperate conditions, and a new character needs her own letter voice). Create a new voice that starts as a copy of the close one, then adjust it.
- **New**: nothing similar exists. Create a voice from scratch.

Also say which part is being worked on: the core, one language layer (for example "only the Portuguese sounds wrong") or both. If it is unclear, show the candidate voices and ask. Then get a **voice brief** from book-voices:

- voice ID (existing, or a proposed new ID following the naming in book-voices) and status;
- who it belongs to and when it is used (from the Character Bible and the Index);
- the tags and literacy profile, with the literacy markers per language (book-voices builds or checks these before any samples are written);
- the current core and language layers, ranges, rules and reference paragraphs (for Update or Derive);
- the relevant entries of the 00 Bilingual Lexicon;
- the chapters and paragraphs that already use it (from Paragraph Parameters), so the effect of changes is known;
- the **neighbour voices**: other voices it must stay clearly different from (for example the main narrator vs the grandma frame) or consistent with (the same character speaking vs writing).

For an **Update**, Rafael may not need all stages: often Stage 3 (rewrite a sample) and Stage 5 (adjust by hand) are enough. Offer the shortest path.

## Stage 1: Find reference authors

First check the Author Library and the reference authors the voice already uses. If new authors are needed, search the web; do not rely on memory for who is popular now. Propose 12-15 candidates in three groups, with one line each on why they fit, the language they write in, and a source:

- **Popular now**: current bestsellers and recent prize winners (NYT, Publishers Weekly, PublishNews Brasil, Booker, International Booker, Pulitzer, Jabuti, Oceanos, Goodreads/BookTok trends) writing historical, war, family-saga or Latin American fiction.
- **Classics with similar stories**: important past writers of war, slavery, frontier, family sagas and oral storytelling, from Brazilian, Latin American and world literature.
- **Wildcards**: 2-3 authors whose style is very different, to stretch the comparison.

Make sure each language has at least two candidates who write natively in it, so each language layer has a native model. When the voice being built has a specific form or literacy (letters, testimony, an unschooled speaker), also suggest authors known for that form or those kinds of voices. Add any new sources to the References section of this skill by proposing an update.

Ask Rafael to pick 4-7 for the next stages, and which of them should guide each language.

## Stage 2: Analyze the selected authors

For each author not already in the library: record the tags (including language and whether read in translation), score all 18 dimensions with reasons, and write a short style portrait (5-8 lines) covering signature techniques, how they work history in without info-dumping, and their hook. For authors who write in English or Portuguese, add a short note on their vocabulary and phrase-building habits in that language. Then show the comparison table, say where the authors differ most, what fits or clashes with the book's tone, and which kinds of voices (narrator, letters, testimony...) and which language layer each would suit. Save new analyses to the Author Library.

**Example passages.**
- For public-domain authors (for example, works by authors who died more than 70 years ago), quote a short representative passage and name the work.
- For authors still in copyright, do not reproduce their text. Name 1-2 specific books and chapters where the style shows best, describe what happens on the page, and rely on Stage 3 to show the style in action.

## Stage 3: Rewrite one of Rafael's paragraphs in each style

Use a paragraph from his book (pasted, or from the Book doc, ideally one that already uses this voice), or one written for the voice being built. Keep the same events, facts and characters. Apply the literacy profile from the voice brief to every version, so each sample already sounds like the character. Rewrite it once per selected author, matching that author's tags and scores (a first-person author's version is in the first person; for a letter voice, write it as a letter). For an Update, also show the paragraph in the voice's current form, so the change is visible. Original writing only, never copied phrases from the author. Under each version, 2-3 notes on which dimensions changed most, and flag any version where the style adds invented details. When the paragraph belongs to a scene that has a **Reader feeling** in the Scenes doc, aim every version at that feeling and note how each style gets the reader there (senses, implication, statement, rhythm).

Write each sample in the language of the layer being worked on. When working on both, write the English and the Portuguese **each natively** (not one translated from the other) and add a line on what each language does differently to get the same effect. Default: English first; offer Portuguese for any he likes.

## Stage 4: Choose or blend

Rafael picks one style, or two to combine (for an Update, the current voice can be one of the two). For a blend: set the tags (person, addressed to, form, literacy), start from the average of the two scores, then ask which should lead on each dimension where they differ by 2 or more. This becomes the **core**. Then, for each language, pick the language references and propose the offsets, vocabulary strategy and phrase-building strategies. Show the core next to the **neighbour voices** from the brief, flag any neighbour that is now too similar (most dimensions within 1 point) or a consistency conflict, and rewrite the paragraph in both languages.

## Stage 5: Adjust by hand

Rafael changes the voice in plain words or by setting numbers, either for the whole voice ("less metaphor", "violence stays offstage") or for one language ("in Portuguese, more regional words from Bahia", "the English sounds too formal"). Change the core for whole-voice requests and the language layer for language requests; keep offsets within ±1 and tell him if a request would push a language too far from the core (then it is really a core change). Rewrite the paragraph, show what changed, and keep checking against the neighbour voices. Repeat until he is happy with both languages. Keep a short change log. Rafael's mom's Portuguese is a strong signal for how the Portuguese layer should sound; when she has written in this voice, use her text as a model and ask before changing her habits.

## Stage 6: Hand the voice package to book-voices (when Rafael says "generate rules" or "save the voice")

Build a **voice package** and give it to book-voices, which validates and saves it:

- **Mode and ID**: New, Derive (from which voice) or Update (with the version it updates).
- **Core**: tags and literacy level; reference authors with weights; the 18 dimensions with base values and allowed tuning ranges (ask Rafael where he wants room to vary); voice rules (5-12, each checkable on one paragraph, written as rule, why, do example, don't example; not vague); **conveying-feeling rules** (2-4: how the voice makes the reader feel a scene's Reader feeling: senses or statement, implied or shown, whether feelings are named, how a shift is marked, how far it goes with disgust, horror or tenderness; consistent with dimensions 8, 17 and 18 and with the handle-with-care notes; each with do and don't examples).
- **One language layer per language** (EN and PT-BR at least): language references, offsets with reasons, vocabulary strategy, phrase-building strategies, address and dialogue, literacy markers, language rules, and a reference paragraph written natively in that language.
- **Proposed lexicon entries**: words and translation decisions that should apply across voices, for 00 Bilingual Lexicon.
- **For an Update**: a short before/after of what changed (core and/or which layer), and the chapters and paragraphs that use the voice and may need a new chapter-review.
- **Proposed shared rules**: any rule that applies to every voice, proposed for **00 Shared Rules** instead.

If book-voices finds a problem (too close to another voice, a literacy detail that does not fit the period, a clash with shared rules, layers that no longer feel like the same voice), go back to Stage 5 with Rafael, then hand over again. book-voices saves the voice file, the Voice Index, the version and the change log after Rafael approves.

---

## General notes

- Be honest: if a style clashes with the book's tone (for example, a moralizing narrator), say so.
- Never reproduce long passages from in-copyright books, and do not imitate an author by copying their sentences. Style is shown through original writing.
- When Rafael writes in Portuguese, answer about the Portuguese text in Portuguese if he prefers, and make sure every core rule works in both languages.
- Keep questions to Rafael short; offer sensible defaults.

---

## References and records

### Author search, October 2026: sources

- Folha de S.Paulo ranking of the best Brazilian books of the 21st century (1. Um defeito de cor, 2. Torto Arado, 3. O avesso da pele): https://www.publishnews.com.br/materias/2025/05/26/apanhadao-folha-elabora-lista-de-melhores-livros-da-literatura-brasileira-no-seculo-21
- Nielsen-PublishNews bestseller list, 22 Feb 2026 (Torto Arado at #1): https://www.publishnews.com.br/nielsen/1/2026/2/22/360/0
- Prêmio Jabuti 2025 winners (literary novel: Tony Bellotto, Vento em setembro; not analyzed): https://www.publishnews.com.br/materias/2025/10/27/ruy-castro-e-tony-bellotto-sao-os-grandes-vencedores-do-67-premio-jabuti
- Prêmio Oceanos 2025 (prose: Silvana Tavano, Ressuscitar Mamutes; not analyzed): https://observador.pt/2025/12/10/brasileiras-ana-maria-vasconcelos-e-silvana-tavano-vencem-premio-oceanos-2025/
- Booker Prize 2025 (David Szalay, Flesh): https://www.drishtiias.com/daily-updates/daily-news-analysis/booker-prize-2025/print_manually
- International Booker Prize 2026 (Yáng Shuāng-zǐ, Taiwan Travelogue, tr. Lin King): https://www.drishtiias.com/state-pcs-current-affairs/international-booker-prize-2026/print_manually
- Pulitzer Prize for Fiction 2026 (Daniel Kraus, Angel Down; not analyzed): https://lithub.com/here-are-the-2026-pulitzer-prize-winners/
- Book Riot, best historical fiction of 2026 so far (includes Maggie O'Farrell, Land): https://bookriot.com/best-historical-fiction-books-of-the-year-so-far-2026/

### Shortlist proposed (October 2026)

- **Popular now**: Itamar Vieira Junior (Torto Arado); Ana Maria Gonçalves (Um defeito de cor); David Szalay (Flesh); Yáng Shuāng-zǐ (Taiwan Travelogue); Maggie O'Farrell (Land).
- **Classics**: Euclides da Cunha (Os Sertões, public domain); Machado de Assis (Memórias Póstumas de Brás Cubas, public domain); Gabriel García Márquez (One Hundred Years of Solitude); Augusto Roa Bastos (Hijo de hombre, Yo el Supremo); Mario Vargas Llosa (The War of the End of the World); João Guimarães Rosa (Grande Sertão: Veredas); Jorge Amado (Terras do Sem-Fim); Isabel Allende (The House of the Spirits).
- **Wildcards**: Cormac McCarthy (Blood Meridian); Svetlana Alexievich (The Unwomanly Face of War).

### Analyzed authors (seed for the 00 Author Library)

Selected by Rafael: Gonçalves, Vieira Junior, García Márquez, Roa Bastos, Szalay, McCarthy, Alexievich.

Language of writing: Gonçalves and Vieira Junior write in Brazilian Portuguese (native models for the PT layer); Szalay and McCarthy write in English (native models for the EN layer); García Márquez and Roa Bastos write in Spanish, and Alexievich in Russian, so they reach both languages through translation.

| | Gonçalves | Vieira Jr | García Márquez | Roa Bastos | Szalay | McCarthy | Alexievich |
|---|---|---|---|---|---|---|---|
| Person | 1st | 1st (3 narrators in turn) | 3rd, all-seeing | mixed 1st and 3rd | 3rd, external | 3rd, distant | 1st, many speakers |
| Addressed to | her lost son | no one | no one | no one | no one | no one | an interviewer |
| Form | life story told to someone | narration | narration that feels told aloud | linked episodes | narration | narration | testimony |
| Literacy of voices | self-educated, plain, Yoruba words | rural Bahia, plain | varied, plain-spoken | Guaraní-inflected, literary | plain modern | archaic, biblical | ordinary, unschooled speech |
| Language | PT-BR | PT-BR | Spanish | Spanish | English | English | Russian |
| 1 Distance | 5 | 4 | 1 | 3 | 2 | 1 | 5 |
| 2 Narrator presence | 4 | 2 | 3 | 3 | 1 | 2 | 2 |
| 3 POV range | 1 | 3 | 4 | 4 | 1 | 2 | 5 |
| 4 Orality | 4 | 3 | 5 | 4 | 1 | 2 | 5 |
| 5 Sentences | 3 | 3 | 5 | 4 | 1 | 5 | 2 |
| 6 Register | 2 | 3 | 3 | 4 | 1 | 5 | 1 |
| 7 Figurative | 2 | 4 | 4 | 4 | 1 | 4 | 2 |
| 8 Sensory | 4 | 5 | 4 | 4 | 2 | 5 | 4 |
| 9 Scene/summary | 3 | 3 | 5 | 3 | 2 | 3 | 3 |
| 10 Chronology | 2 | 3 | 4 | 4 | 2 | 1 | 5 |
| 11 Dialogue | 2 | 2 | 1 | 2 | 4 | 2 | 2 |
| 12 Pace | 2 | 2 | 3 | 2 | 4 | 3 | 3 |
| 13 Historical texture | 5 | 2 | 2 | 3 | 2 | 4 | 3 |
| 14 Realism | 2 | 3 | 5 | 3 | 1 | 2 | 1 |
| 15 Causality | 2 | 3 | 5 | 3 | 5 | 4 | 3 |
| 16 Moral stance | 2 | 3 | 4 | 4 | 5 | 5 | 4 |
| 17 Violence | 4 | 3 | 3 | 4 | 3 | 5 | 4 |
| 18 Emotion | 4 | 3 | 2 | 3 | 1 | 1 | 5 |

Where to read each style: Gonçalves, opening chapters (childhood and the slave-ship crossing). Vieira Junior, chapter 1 (the knife) and the opening of Part III (the spirit narrator). García Márquez, chapter 1 and the banana-company massacre (chapter 15). Roa Bastos, Hijo de hombre, the Chaco War chapter "Sed". Szalay, Flesh, chapter 1. McCarthy, Blood Meridian, chapter 1 and the Comanche attack on Captain White's company. Alexievich, any group of monologues and the author's opening notes.

Suggested fit by voice (not yet decided): grandma frame, García Márquez or Alexievich; main narration, García Márquez blended with Szalay or Vieira Junior; documents and voices, Alexievich.

### Rafael's decisions

- Svetlana Alexievich is the reference for letters from female characters in desperate conditions, adjusted to each character's literacy.
- Voices are multilingual: the same approach in every language, with references and style allowed to vary slightly per language, especially vocabulary and phrase-building strategies.