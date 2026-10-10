---
name: "book-voices"
description: "Use when Rafael wants to create, list, adjust or assign the narrative voices of his book (narrators, characters, letters), each kept as its own file in the Voices folder in Drive."
---

# Book voices (the voice governor)

This skill governs every voice used in Rafael's book. A voice is a complete, written definition of how one narrator or one character sounds on the page, in every language of the book. Each voice lives in its own file in the **Voices** folder (inside Configuration) in the book's Google Drive. The chapter-review and paragraph-review skills read voices from there; only this skill creates or changes them. The **voice-generator** skill does the creative work of building or updating a voice, always in exchange with this skill (see "Exchange with voice-generator").

## The book (short context)

A novel about Rafael's great-great-grandfather, a Brazilian soldier in the Paraguayan War (1864-1870) who settled in Mato Grosso do Sul (Jacadigo, Corumba). Slavery, war, migration, family. History blended into fiction. Events driven by luck and chance; no morals pushed on the reader; no pure heroes or villains. Themes: luck, freedom, violence, money. Framed as a story his grandma used to tell. Written in English and Brazilian Portuguese side by side; Rafael's mom writes parts in Portuguese.

## Drive layout (shared by all book skills)

This is the single source of truth for where the book files live. All book skills (co-writer, voice-generator, chapter-review, paragraph-review, engagement-heatmap) use these locations. One copy of each file only; search before creating anything.

**Projeto Livro** (main folder, ID 1C7YhM6J1grSaYlVgElY3ikeomTmzPXsF): overarching files

- **Book** (doc): the prose, English and Portuguese.
- **Chapters** (doc): per chapter, bullet points of the stories to tell and their sources.
- **Character Bible** (doc).
- **Book Concept — Detailed Summary** (doc).
- **Continuity Log** (doc): facts established so far (see chapter-review).

**Projeto Livro / Configuration** (ID 1tt7FuK8x-Ze4KNbzYHMCtUrJqIYfdcuO): parameters used by the skills

- **Paragraph Parameters** (sheet): one row per paragraph (see chapter-review).
- **Engagement** (sheet) and **Engagement Anchors** (doc): used by the engagement-heatmap skill.
- **Voices/** (folder, ID 10v0_gpo0OvYGOFcp5bA7AHfwjUH4Lu9s), owned by this skill:
  - **00 Voice Index** (sheet): all voices: ID, name, type, whose voice, when to use it, based on (for derived voices), languages covered, current version, status (draft / active / retired).
  - **00 Shared Rules** (doc): rules every voice follows (the book's tone: no morals, chance, ambiguity, how history is woven in), plus bilingual notes.
  - **00 Bilingual Lexicon** (doc, create the first time it is needed): decisions that apply across all voices: words kept untranslated in English (for example senzala, engenho, sucuri, carta de alforria) and how context makes them clear; agreed translations of recurring terms; spelling of places and names; period terms to use or avoid in each language; forms of address and how each is carried into English.
  - **00 Author Library** (doc): the reference authors analyzed with the voice-generator framework (tags, language, 18 scores, portraits), so they are not re-analyzed each time.
  - **One doc per voice**, named "[ID] Name", for example "NARR-MAIN Main narrator", "NARR-GRANDMA Grandma's telling", "CHAR-<NAME>-LETTERS <Name>'s letters".

**Projeto Livro / Registros historicos** (ID 14ULqXY716bdAe0EJacurVX5MoU0rtyyc): research and family records (sources for chapters and fact checks), for example the Paraguayan War research notes, slavery timeline and research compilation, Região, Dados gerais, Contos familiares, Memórias de Família, the family chart, and the **Timelines** subfolder.

**Projeto Livro / Imagens**: images.

New overarching book files go in the main folder; new skill parameters go in Configuration; new research goes in Registros historicos. If a file is not where this layout says, search Drive by title before concluding it is missing, and tell Rafael if it has moved.

## Types of voices

- **Narrator voices**: one or two (for example the main narrator and the grandma frame).
- **Character voices**: one per character who needs a distinct voice: their dialogue, letters, inner speech or testimony. A character can have more than one voice if the form differs a lot (speech vs letters), or if they change over the book (as a child vs as an old woman).
- **Base voices**: a shared starting point that several character voices are derived from (for example the base for letters from women in desperate conditions). A base voice is not used directly in the text.
- **Document voices**: newspapers, official records, gossip and legends told by a random person.

## What a voice file contains

Every voice has a **core**, shared by all languages, and a **language layer** for each language of the book (EN and PT-BR; more can be added). The approach is the same in every language; references, vocabulary and phrase building may vary slightly so that each language reaches the same effect natively. See "Multilingual voices" in the voice-generator skill for the details of a language layer.

**Core**

1. **ID, name, type, version, status**, and "based on" if derived from another voice.
2. **Who and when**: whose voice it is (link to the Character Bible entry), and exactly when it is used ("letters written by X to her sister, chapters 6-9").
3. **Tags** (from the voice-generator framework): narrative person, addressed to, form, and **literacy**.
4. **Literacy profile** (essential for character voices): the level (from cannot write, through barely literate and basic, to educated and formal), and what it means on the page: vocabulary range, spelling, punctuation, sentence length, grammar, regional and period speech, first language (Portuguese, Spanish, Guaraní, Yoruba...). If the character cannot write, say how their letters exist (dictated to someone, so the scribe's hand shows) or whether they only speak. Check plausibility for the period, place, gender, class and status of the character, and flag anything that seems historically unlikely. The level is the same in every language; how it shows is in each language layer.
5. **Reference authors** with weights (for example 70% Alexievich, 30% Gonçalves).
6. **Target profile**: each of the 18 dimensions with a **base value** and an **allowed tuning range** (for example Violence: base 3, range 2-5). Paragraph-level tuning must stay inside the range.
7. **Neighbour voices**: the voices this one must stay clearly different from, and the ones it must stay consistent with (the same character in another form).
8. **Voice rules**: 5-12 rules, each checkable on one paragraph in any language, with a short do and don't example set in the story.
9. **Conveying feeling**: how this voice makes the reader feel what a scene's **Reader feeling** asks for (every scene map in Scenes carries one): through the senses or through statement, implied or shown, whether feelings are ever named, how a shift of feeling within a scene is marked, and how far the voice goes with disgust, horror or tenderness (always inside 00 Shared Rules and the Concept's handle-with-care notes). 2-4 rules, each checkable on one paragraph, with a do and don't example. They must fit the voice's scores on Sensory detail (8), Violence rendering (17) and Emotional temperature (18).

**Language layer (one section per language: EN, PT-BR)**

10. **Language references** with weights (native writers of that language where possible; name the translation if a translated author is the model).
11. **Profile offsets** from the core on language-sensitive dimensions only (Orality, Sentence length, Register, Figurative density, Dialogue share), at most ±1, each with a reason.
12. **Vocabulary strategy**: word stock, regional and period words, words to avoid, untranslated words (following 00 Bilingual Lexicon).
13. **Phrase-building strategies**: how sentences are built in this language to get the voice's effect.
14. **Address and dialogue**: forms of address and dialogue punctuation.
15. **Literacy markers** in this language, without caricature.
16. **Language rules**: 2-5 rules that only apply in this language, with do and don't examples.
17. **Reference paragraph**, written natively in this language.

**Change log**: date, version, what changed (core or which layer) and why.

## Exchange with voice-generator

Every creation or update of a voice goes through this exchange, whether Rafael starts from this skill or asks voice-generator directly.

**1. Voice brief (book-voices to voice-generator).** When voice-generator checks in, read the Voice Index and the relevant voice files, and say whether the request is an **Update** (a voice for this need exists), a **Derive** (a close voice exists, for example a base voice) or **New**, and whether it concerns the core, one language layer or both. Then provide the brief:

- voice ID (existing, or a proposed new ID following the naming above) and status;
- who it belongs to and when it is used (from the Character Bible and the Index);
- the tags and literacy profile with literacy markers per language, built or checked here before any samples are written (ask Rafael what is unknown about the character);
- for Update or Derive: the current core, language layers, ranges, rules and reference paragraphs;
- the relevant entries of 00 Bilingual Lexicon;
- the chapters and paragraphs that already use the voice (from Paragraph Parameters);
- the neighbour voices with their profiles.

**2. Voice package (voice-generator to book-voices).** When voice-generator hands back a finished voice, validate it before saving:

- **Distinct**: compare it with every neighbour voice; flag any that is now too similar (most dimensions within 1 point, same tags) unless that is intended.
- **Consistent**: the same character's voices (speech vs letters, young vs old) differ only where the form or time explains it.
- **Same voice across languages**: language offsets stay within ±1 on the allowed dimensions; the two reference paragraphs read as the same character and tone; the literacy level is the same in both.
- **Lexicon**: the layers follow 00 Bilingual Lexicon; proposed new lexicon entries are reviewed with Rafael and added to the lexicon, not only to this voice.
- **Literacy**: plausible for the character, period and place.
- **Shared rules**: no voice rule contradicts 00 Shared Rules; proposed shared rules are reviewed separately.
- **Feeling**: the Conveying feeling rules are present and consistent with the voice's scores on dimensions 8, 17 and 18, and with the handle-with-care notes.
- **Complete**: every core field and every field of each language layer is filled.

If something fails, send it back to voice-generator with the problem described. When it passes, show Rafael the result (for an Update, the before/after and the affected chapters), and after his OK save the voice file, update the Voice Index, raise the version and add the change log line. For an Update, list the chapters that use the voice so Rafael can decide whether to re-run chapter-review on them.

## What this skill does

- **List voices**: read the 00 Voice Index and summarize.
- **Create a voice**: start the exchange above; voice-generator builds the voice with Rafael, this skill validates and saves it. Always do the literacy profile before the writing samples, so the samples already sound like the character.
- **Adjust a voice**: same exchange in Update mode. Small changes (one range, one rule, one vocabulary note in a language layer) can be made here directly, with Rafael's OK, a version bump and a change log line.
- **Compare voices**: check that voices that should sound different really do (show their profiles side by side), and that one character's voice is consistent across forms and languages.
- **Maintain the lexicon**: add or change entries in 00 Bilingual Lexicon with Rafael's OK, and list the voices and chapters a change affects.
- **Retire or merge voices**: mark them retired in the Index; never delete a voice file that paragraphs still use.

## Starting voices (Rafael's decisions so far)

- Main narrator (to be defined).
- Grandma's telling, for the prologue, epilogue and frame passages (to be defined).
- **Base voice: letters from female characters in desperate conditions** (BASE-LETTERS-DESPERATE, draft): reference author Svetlana Alexievich (broken, oral, raw testimony). Each such character gets her own letter voice derived from this base and adjusted to her literacy.
- Existing voice files written before language layers were introduced get EN and PT-BR layers the next time they are updated.
- Existing voice files without Conveying feeling rules get them the next time they are updated, or before the co-writer first writes prose in that voice.

## Notes

- Never change a voice file without Rafael's OK; show the change first.
- Keep voice files short enough to read quickly; the reference paragraphs and the rules matter more than long explanations.
- Research sources for the reference authors are in the References section of the voice-generator skill; sources for engagement scoring are in the engagement-heatmap skill.