---
name: "book-voices"
description: "Use when the author wants to create, list, adjust, compare or assign the narrative voices of a book in this repo (narrators, characters, letters, documents), each kept as its own file in the book's voices folder."
---

# Book voices (the voice governor)

This skill governs every voice used in a book. A voice is a complete, written definition of how one narrator or one character sounds on the page, in every language of the book. Each voice lives in its own file in the book's **voices folder**. chapter-review, paragraph-review and the co-writer read voices from there; only this skill creates or changes them. The **voice-generator** skill does the creative work of building or updating a voice, always in exchange with this skill (see "Exchange with voice-generator").

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask.
2. Read `BOOK.md`: it gives the paths of the voices folder and its files, the languages, the people and roles (for example a co-author whose wording is the source in one language), the voice ID convention and any voice decisions made so far.
3. Read the Concept for the book's tone, how it is told and what to handle with care.

## The voices folder

Owned by this skill. Paths come from the profile; the usual layout is:

- **Voice Index** (`00-voice-index.csv`): all voices: ID, name, type, whose voice, when used, based on (for derived voices), version, status (draft / active / retired), notes.
- **Shared Rules** (`00-shared-rules.md`): rules every voice follows (the book's tone and how history or the world is woven in), plus bilingual notes.
- **Bilingual Lexicon** (`00-bilingual-lexicon.md`, multilingual books; create the first time it is needed): decisions that apply across all voices: words kept untranslated and how context makes them clear; agreed translations of recurring terms; spelling of places and names; period terms to use or avoid in each language; forms of address and how each is carried into the other languages.
- **Author Library** (`00-author-library.md`): the reference authors analyzed with the voice-generator framework (tags, language, 18 scores, portraits), so they are not re-analyzed each time.
- **One file per voice**, named by its ID (for example `NARR-MAIN.md`, `CHAR-<NAME>-LETTERS.md`), following the profile's ID convention.

One copy of each file only; look before creating anything. If a file is not where the profile says, search the book folder before concluding it is missing, and tell the author if it has moved.

## Types of voices

- **Narrator voices**: usually one or two (for example the main narrator and a frame narrator).
- **Author voice**: the author speaking as themselves (a prologue, an author's note), when the book has one.
- **Character voices**: one per character who needs a distinct voice: their dialogue, letters, inner speech or testimony. A character can have more than one voice if the form differs a lot (speech vs letters), or if they change over the book (as a child vs as an old person).
- **Base voices**: a shared starting point that several character voices are derived from. A base voice is not used directly in the text.
- **Document voices**: newspapers, official records, gossip and legends told by a passer-by.

## What a voice file contains

Every voice has a **core**, shared by all languages, and a **language layer** for each language of the book (listed in the profile). The approach is the same in every language; references, vocabulary and phrase building may vary slightly so that each language reaches the same effect natively. See "Multilingual voices" in the voice-generator skill for the details of a language layer. A single-language book has one layer.

**Core**

1. **ID, name, type, version, status**, and "based on" if derived from another voice.
2. **Who and when**: whose voice it is (link to the Character Bible entry), and exactly when it is used ("letters written by X to her sister, chapters 6-9").
3. **Tags** (from the voice-generator framework): narrative person, addressed to, form, and **literacy**.
4. **Literacy profile** (essential for character voices): the level (from cannot write, through barely literate and basic, to educated and formal), and what it means on the page: vocabulary range, spelling, punctuation, sentence length, grammar, regional and period speech, first language. If the character cannot write, say how their letters exist (dictated to someone, so the scribe's hand shows) or whether they only speak. Check plausibility for the period, place, gender, class and status of the character, and flag anything that seems unlikely. The level is the same in every language; how it shows is in each language layer.
5. **Reference authors** with weights (for example 70% author A, 30% author B).
6. **Target profile**: each of the 18 dimensions with a **base value** and an **allowed tuning range** (for example Violence: base 3, range 2-5). Paragraph-level tuning must stay inside the range.
7. **Neighbour voices**: the voices this one must stay clearly different from, and the ones it must stay consistent with (the same character in another form).
8. **Voice rules**: 5-12 rules, each checkable on one paragraph in any language, with a short do and don't example set in the story.
9. **Conveying feeling**: how this voice makes the reader feel what a scene's **Reader feeling** asks for (every scene map carries one): through the senses or through statement, implied or shown, whether feelings are ever named, how a shift of feeling within a scene is marked, and how far the voice goes with disgust, horror or tenderness (always inside the Shared Rules and the Concept's handle-with-care notes). 2-4 rules, each checkable on one paragraph, with a do and don't example. They must fit the voice's scores on Sensory detail (8), Violence rendering (17) and Emotional temperature (18).

**Language layer (one section per language)**

10. **Language references** with weights (native writers of that language where possible; name the translation if a translated author is the model).
11. **Profile offsets** from the core on language-sensitive dimensions only (Orality, Sentence length, Register, Figurative density, Dialogue share), at most ±1, each with a reason.
12. **Vocabulary strategy**: word stock, regional and period words, words to avoid, untranslated words (following the Bilingual Lexicon).
13. **Phrase-building strategies**: how sentences are built in this language to get the voice's effect.
14. **Address and dialogue**: forms of address and dialogue punctuation.
15. **Literacy markers** in this language, without caricature.
16. **Language rules**: 2-5 rules that only apply in this language, with do and don't examples.
17. **Reference paragraph**, written natively in this language.

**Change log**: date, version, what changed (core or which layer) and why.

## Exchange with voice-generator

Every creation or update of a voice goes through this exchange, whether the author starts from this skill or asks voice-generator directly.

**1. Voice brief (book-voices to voice-generator).** When voice-generator checks in, read the Voice Index and the relevant voice files, and say whether the request is an **Update** (a voice for this need exists), a **Derive** (a close voice exists, for example a base voice) or **New**, and whether it concerns the core, one language layer or both. Then provide the brief:

- voice ID (existing, or a proposed new ID following the profile's convention) and status;
- who it belongs to and when it is used (from the Character Bible and the Index);
- the tags and literacy profile with literacy markers per language, built or checked here before any samples are written (ask the author what is unknown about the character);
- for Update or Derive: the current core, language layers, ranges, rules and reference paragraphs;
- the relevant entries of the Bilingual Lexicon;
- the chapters and paragraphs that already use the voice (from Paragraph Parameters);
- the neighbour voices with their profiles;
- the profile's notes for the skills that concern voices (vocabulary, untranslated words, native models per language).

**2. Voice package (voice-generator to book-voices).** When voice-generator hands back a finished voice, validate it before saving:

- **Distinct**: compare it with every neighbour voice; flag any that is now too similar (most dimensions within 1 point, same tags) unless that is intended.
- **Consistent**: the same character's voices (speech vs letters, young vs old) differ only where the form or time explains it.
- **Same voice across languages**: language offsets stay within ±1 on the allowed dimensions; the reference paragraphs read as the same character and tone; the literacy level is the same in every language.
- **Lexicon**: the layers follow the Bilingual Lexicon; proposed new lexicon entries are reviewed with the author and added to the lexicon, not only to this voice.
- **Literacy**: plausible for the character, period and place.
- **Shared rules**: no voice rule contradicts the Shared Rules; proposed shared rules are reviewed separately.
- **Feeling**: the Conveying feeling rules are present and consistent with the voice's scores on dimensions 8, 17 and 18, and with the handle-with-care notes.
- **Complete**: every core field and every field of each language layer is filled.

If something fails, send it back to voice-generator with the problem described. When it passes, show the author the result (for an Update, the before/after and the affected chapters), and after their OK save the voice file, update the Voice Index, raise the version, add the change log line, and save the change the way the profile says (by default: commit and push). For an Update, list the chapters that use the voice so the author can decide whether to re-run chapter-review on them.

## What this skill does

- **List voices**: read the Voice Index and summarize.
- **Create a voice**: start the exchange above; voice-generator builds the voice with the author, this skill validates and saves it. Always do the literacy profile before the writing samples, so the samples already sound like the character.
- **Adjust a voice**: same exchange in Update mode. Small changes (one range, one rule, one vocabulary note in a language layer) can be made here directly, with the author's OK, a version bump and a change log line.
- **Compare voices**: check that voices that should sound different really do (show their profiles side by side), and that one character's voice is consistent across forms and languages.
- **Maintain the lexicon**: add or change entries in the Bilingual Lexicon with the author's OK, and list the voices and chapters a change affects.
- **Retire or merge voices**: mark them retired in the Index; never delete a voice file that paragraphs still use.
- **Record decisions**: when the author makes a lasting voice decision (a reference author for a kind of voice, a rule for all voices), add it to the profile's "Voices: decisions so far" or to the Shared Rules.

## Notes

- Never change a voice file without the author's OK; show the change first.
- Keep voice files short enough to read quickly; the reference paragraphs and the rules matter more than long explanations.
- Existing voice files without language layers or Conveying feeling rules get them the next time they are updated, or before the co-writer first writes prose in that voice.
- The style framework and the method for reference authors are in the voice-generator skill; sources for engagement scoring are in the engagement-heatmap skill.
