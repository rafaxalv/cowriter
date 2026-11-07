# Book profile: Grandgrand father story

The profile every book skill reads first: how the work on this book is organized. It says who works on it, where its files are and how they fit together, the order of work for each chapter, which languages it is written in, how its files are formatted, and which standing rules apply. The book's ideas (its central question, pillars, how it is told and what to handle with care) are in the **Concept**, `outline/concept.md`; read that next. Last updated Nov 3, 2026 (reorganized: the Concept's working context moved here; files, working order and rules brought up to date).

All paths below are relative to this folder (`books/grandgrandfather/`).

## The book

- **Working title**: Book: Grandgrand father story (to decide).
- **In one line**: a family story told by Rafael's grandmother. Her grandfather, born enslaved in Bahia (1846), fought in the Paraguayan War, came home free, won the lottery, bought a cattle farm at Jacadigo (Corumbá) and "bought a Spanish girl" whom he married; after his death the sons lost everything at cards. Immersive historical fiction around those few remembered facts.
- **Shape** (the plot itself lives in Chapters): Prologue (The Fog) · Part I, Bahia (ch. 1–3) · Part II, War (ch. 4–9) · Part III, Free, not equal (ch. 10) · Part IV, The woman from Spain (ch. 11, Her Road) · Part V, Fortune (ch. 12, the Interlude, Tonico's Journey, ch. 13–16) · Part VI, The fall (ch. 17–18) · Epilogue (option).
- **Length**: about 300 pages (80,000–85,000 words); 350 pages is a hard limit. Word budgets per chapter are adjusted as he writes.
- **Status (Nov 3, 2026)**: every chapter planned in Chapters, each with a Readiness score; chapter revision under way, lowest scores first (ch. 8 revised Nov 3). Prologue, chapter 1 and epilogue drafted; chapter 1 scene map at draft 2. Voices: the main narrator, the author's voice, a letters base, and 21 speech voices (11 characters, 10 groups).

## People and roles

- **Rafael** (the author): plans the story, writes in English, decides everything. Talk to him in English unless he writes in Portuguese.
- **Rafael's mom** (co-author, Portuguese): writes or revises parts in Brazilian Portuguese. Where she wrote the Portuguese, her text is the source: keep her wording (change it only to fix an error, and say so) and update the English to match her meaning. Her Portuguese is also the model for how the PT-BR layer of a voice should sound.
- **Where the book lives**: only in the repo (`rafaxalv/cowriter`), with the Manuscript Desk as its editor. Downloads (sources, books, images) go into the repo, never onto Rafael's computer.

## Languages

| Code | Language | Manuscript | Written first? |
| --- | --- | --- | --- |
| EN | English | `book/manuscript.en.md` | Yes, by default (Rafael writes in English) |
| PT-BR | Brazilian Portuguese | `book/manuscript.pt-br.md` | When Rafael's mom writes first, her Portuguese leads |

Every passage exists in both languages and says the same thing; neither is a word-for-word translation of the other.

## How the files fit together

1. **Concept**: the central question, the pillars, how the book is told, what to handle with care. Least detail.
2. **Chapters**: the skeleton and plan of record. Every event per chapter, in order, with sources for real events that must be accurate, and each chapter's Readiness score.
3. **Scenes**: each chapter's events expanded into ordered scenes (when, where, point of view, characters, beats, motivations, feelings, place details, voice and scene shape). Built by scene-builder.
4. **Manuscript**: the final text, written from the scenes in the planned voices. Full detail.

Used at every level: the **Character Bible** (who people are, plus the Continuity record of what the text has established), the **research**, the **voices**, and the **shared library** (reference books and style studies). Changes flow down (Concept → Chapters → Scenes → Manuscript); deliberate changes in the text flow back up.

## Files

| Role (name used by the skills) | Path |
| --- | --- |
| Concept | `outline/concept.md` (earlier versions: in the git history) |
| Chapters (plan of record) | `outline/chapters.md` (the index: notes, parts, links) and `outline/chapters/` (one file per chapter, e.g. `08-asuncion.md`; read and edit only the chapter you need) |
| Scenes (scene maps) | `outline/scenes.md` |
| Alternatives (undecided arcs, working notes) | `outline/alternatives/` (e.g. `purchase.md`); Chapters stays the plan of record |
| Manuscript | `book/manuscript.en.md`, `book/manuscript.pt-br.md` |
| Drafts (chapters being written) | `drafts/` (create when first needed) |
| Character Bible | `characters/character-bible.md` |
| Continuity record | the **Continuity** section at the end of the Character Bible |
| Voices folder | `voices/`: narrators (`NARR-`), the author's voice (`AUTHOR-`), base voices (`BASE-`, including the group speech voices `BASE-SPEECH-`), character voices (`CHAR-<NAME>-<FORM>`, including the speech voices `CHAR-<NAME>-SPEECH`) |
| Voice Index | `voices/00-voice-index.csv` |
| Shared Rules | `voices/00-shared-rules.md` |
| Bilingual Lexicon | `voices/00-bilingual-lexicon.md` (create when first needed) |
| Author Library | `voices/00-author-library.md` |
| Author search record | `voices/author-search-2026-10.md` |
| Voice files | `voices/<ID>.md`, e.g. `voices/NARR-MAIN.md` |
| Chapter Voices | `config/chapter-voices.csv` (each chapter's voice and tuning) |
| Paragraph Parameters | `config/paragraph-parameters.csv` |
| Engagement scores | `config/engagement.csv` |
| Engagement Anchors | `config/engagement-anchors.md` |
| Readiness rubric | `.claude/skills/co-writer/readiness.md` (the score itself is a line in each chapter's entry in Chapters) |
| Research | `research/`: `paraguayan-war/`, `timelines/`, `places/`, `daily-life/`, `family/`, `people/`, `music/`, `capoeira/`, `sources/`, `images/`; research notes are often written in Portuguese |
| Timeline recipe | `research/timelines/how-to-build-a-timeline.md` |
| Shared library | `library/` at the repo root (reference books, style studies, download queue); shared by every book |
| Manuscript Desk | `tools/manuscript-editor/` (the editor page and its export, sync and refresh steps in its README) |

## Working order for each chapter

1. **Revise the plan** (chapter-plan-revision): brainstorm, research, organize the entry, close plot holes, until the Readiness score is 80 or more (or Rafael is satisfied).
2. **Tune the voice** (chapter-voice-tuning): the chapter's narrator tuning, settled through a round of questions; recorded in Chapter Voices.
3. **Build the scenes** (scene-builder): the scene map in Scenes, with the chapter's tuning applied to the scene shape and each speaker's speech voice.
4. **Write** (co-writer): the draft in `drafts/`, in both languages, from the scene map.
5. **Review** (chapter-prose-review with paragraph-review; engagement-heatmap when useful), then the approved chapter moves into the manuscript.

Alongside: **character-voice** for how characters speak; **book-voices** and **voice-generator** for the voices themselves; **library-builder** for reference books; **book-repo** for every commit and push. After every change to the plan, refresh the Manuscript Desk; before changing the manuscript or Paragraph Parameters, sync its edits back first (steps in its README).

## Formats

- **Manuscript**: one file per language. `#` title, `##` parts, prologue and epilogue, `###` chapters and the interlude. Each paragraph is preceded by its ID in a hidden comment, e.g. `<!-- 01.003 -->`; the same ID marks the same paragraph in both files. Chapters not yet written hold a placeholder: `*(to be written)*` / `*(a escrever)*`.
- **Chapters entry**: each chapter has When / where, a Readiness line, then Stories, Facts, Sources and Notes, in that order. Stories are flat bullets (never nested), the events numbered like **3.** or **3.2**, opening with "How the chapter runs". Facts carry truth labels and point to numbered Sources.
- **Paragraph ID**: chapter.row with three digits, e.g. `01.014`. Prologue `00`, epilogue `99`, the interlude `INT`. A paragraph inserted later gets a suffix (`01.014a`) so the other IDs do not shift; renumber only when Rafael asks, and then in both files together.
- **Chapter Voices** (CSV): Chapter, Voice ID, Tuning, Reason for tuning. Voice tuning is set per chapter, never per paragraph (decided Nov 3, 2026): one voice and one tuning for the whole chapter.
- **Paragraph Parameters** (CSV): Paragraph ID, Chapter, Opening words (EN), Opening words (PT), Voice ID (the chapter's voice, or the paragraph's own voice for a letter or document, which keeps that voice's base values), Voice version, Review status, Last reviewed, Open issues, Engagement avg, Engagement peak.
- **Engagement** (CSV): Paragraph ID, Sentence, Opening words, Engagement, Tension, Emotion, Pace, Hot words, Uncertain, Reason, Date.
- **Voice Index** (CSV): ID, Name, Type, Whose voice, When used, Based on, Version, Status, Notes.
- **Voice IDs**: `NARR-<NAME>` for narrators, `AUTHOR-<NAME>` for the author's own voice, `CHAR-<NAME>-<FORM>` for characters (e.g. `CHAR-LUZIA-LETTERS`), `BASE-<NAME>` for base voices, `DOC-<NAME>` for document voices.
- **Truth labels** (working notes only, never in the text): DOCUMENTED, STRONGLY SUPPORTED, FAMILY TRADITION, PLAUSIBLE RECONSTRUCTION, FICTIONAL. The research files also use Documented / Contested / Tradition / To verify.

## Standing rules from Rafael

1. Every story line he gives in the chat goes into Chapters, in the chapter where it happens, with all his details; he confirms which chapter an event goes into (propose event → chapter → position → why, and wait). The Character Bible holds only short bullets: personality, backstory and minor details, with chapter pointers.
2. No new characters, or expanded existing ones, without his approval.
3. He writes the funny childhood episodes himself (from his own and his cousins' childhood); never invent them.
4. Show changes before applying them; never overwrite his or his mom's text without approval. Nothing is committed without his approval.
5. Don't cut arcs yet: brainstorm first, then select against the page budget.
6. Neither he (the great-great-grandfather) nor the woman from Spain is ever named in the book text. **Working names, for planning only**: Benedito (him) and Carmen (the woman from Spain). Use them in chats, Chapters, Scenes and the Character Bible; never in the manuscript.
7. **Dates** (decided Nov 3, 2026): dates matter only for major events. The researched dates stay in Facts for accuracy; the text tells time as the characters live it (in the war he often loses track of time).

## How changes are saved

- Show the proposed change first; apply it only after Rafael approves.
- Then commit to `main` through the book-repo skill, with a short message saying what changed and why, and push.
- A chapter being written lives in `drafts/chapter-NN.<lang>.md` until it is approved; then it moves into the manuscript.
- Before a major revision of the manuscript, tag the current commit `draft-N` (N = next number) and push the tag. Tags are never moved. To compare drafts, diff the tag against the current manuscript.

## Voices: decisions so far

- **NARR-MAIN** (main narrator, draft 0.1): close third person, raw and sensory; blend of Itamar Vieira Junior, García Márquez and Tarantino.
- **AUTHOR-MAIN** (Rafael's own voice, draft 0.1): prologue, epilogue and author passages.
- **NARR-GRANDMA**: to be redefined; grandma now appears only inside AUTHOR-MAIN, quoted or retold.
- **Speech voices** (character-voice, Nov 3, 2026): how characters speak in dialogue: 11 character voices (`CHAR-<NAME>-SPEECH`) and 10 group voices (`BASE-SPEECH-<GROUP>`), each with settings per chapter. A scene's speech voices are found from the Characters field of its scene card. Learners may speak broken English or Portuguese.
- **Chapter tuning**: one voice and one tuning per chapter, in Chapter Voices (chapter-voice-tuning); no tuning per paragraph.
- **BASE-LETTERS-DESPERATE** (draft): base for letters from female characters in desperate conditions; reference author Svetlana Alexievich, adjusted to each character's literacy.
- Voice files written before language layers or Conveying-feeling rules get them the next time they are updated, or before the co-writer first writes prose in that voice.

## Notes for the skills

- **Language layers**: in Portuguese, everyday Brazilian words, words of Tupi, Bantu and Yoruba origin, regionalisms of Bahia, the Pantanal and Mato Grosso do Sul, period words of the 1800s; no Portugal-only usage. In English, keep untranslated and clear by context: senzala, engenho, jornal, ganhadeira, orixá, capitão do mato, Sinhô/Sinhá, carta de alforria, sucuri.
- **Native models for each language**: Gonçalves and Vieira Junior (PT-BR); Szalay and McCarthy (EN); García Márquez, Roa Bastos and Alexievich reach both through translation.
- **Engagement**: anchors are not set yet; propose them from the first chapter scored. Quiet passages in AUTHOR-MAIN can be exactly right at level 2.
- **Low-reliability material** (legends, hearsay, propaganda) is welcome only in a character's mouth, never from the narrator as fact.
