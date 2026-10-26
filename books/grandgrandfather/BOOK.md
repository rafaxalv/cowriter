# Book profile: Grandgrand father story

The profile every book skill reads first. It says where this book's files are, who works on it, which languages it is written in, how its files are formatted and which standing rules apply. The story itself, its key ideas and what to handle with care are in `outline/concept.md`; read that next.

All paths below are relative to this folder (`books/grandgrandfather/`).

## The book

- **Working title**: Book: Grandgrand father story (to decide).
- **In one line**: a family story told by Rafael's grandmother. Her grandfather, born enslaved in Bahia (1846), fought in the Paraguayan War, came home free, won the lottery, bought a cattle farm at Jacadigo (Corumbá) and "bought a Spanish girl" whom he married; after his death the sons lost everything at cards. Immersive historical fiction around those few remembered facts.
- **Length**: about 300 pages (80,000–85,000 words); 350 pages is a hard limit.
- **Status (Oct 2026)**: prologue, chapter 1 and epilogue drafted; chapter 1 scene map in progress.

## People and roles

- **Rafael** (the author): plans the story, writes in English, decides everything. Talk to him in English unless he writes in Portuguese.
- **Rafael's mom** (co-author, Portuguese): writes or revises parts in Brazilian Portuguese. Where she wrote the Portuguese, her text is the source: keep her wording (change it only to fix an error, and say so) and update the English to match her meaning. Her Portuguese is also the model for how the PT-BR layer of a voice should sound.

## Languages

| Code | Language | Manuscript | Written first? |
| --- | --- | --- | --- |
| EN | English | `book/manuscript.en.md` | Yes, by default (Rafael writes in English) |
| PT-BR | Brazilian Portuguese | `book/manuscript.pt-br.md` | When Rafael's mom writes first, her Portuguese leads |

Every passage exists in both languages and says the same thing; neither is a word-for-word translation of the other.

## Files

| Role (name used by the skills) | Path |
| --- | --- |
| Concept | `outline/concept.md` (earlier long version, archive only: `outline/concept-archive.md`) |
| Chapters (plan of record) | `outline/chapters.md` |
| Scenes (scene maps) | `outline/scenes.md` |
| Manuscript | `book/manuscript.en.md`, `book/manuscript.pt-br.md` |
| Drafts (chapters being written) | `drafts/` (create when first needed) |
| Character Bible | `characters/character-bible.md` |
| Continuity record | the **Continuity** section at the end of the Character Bible |
| Voices folder | `voices/` |
| Voice Index | `voices/00-voice-index.csv` |
| Shared Rules | `voices/00-shared-rules.md` |
| Bilingual Lexicon | `voices/00-bilingual-lexicon.md` (create when first needed) |
| Author Library | `voices/00-author-library.md` |
| Author search record | `voices/author-search-2026-10.md` |
| Voice files | `voices/<ID>.md`, e.g. `voices/NARR-MAIN.md` |
| Paragraph Parameters | `config/paragraph-parameters.csv` |
| Engagement scores | `config/engagement.csv` |
| Engagement Anchors | `config/engagement-anchors.md` |
| Research | `research/` (war, timelines, places, family records, sources, images) |
| Timeline recipe | `research/timelines/how-to-build-a-timeline.md` |

## Formats

- **Manuscript**: one file per language. `#` title, `##` parts, prologue and epilogue, `###` chapters and the interlude. Each paragraph is preceded by its ID in a hidden comment, e.g. `<!-- 01.003 -->`; the same ID marks the same paragraph in both files. Chapters not yet written hold a placeholder: `*(to be written)*` / `*(a escrever)*`.
- **Paragraph ID**: chapter.row with three digits, e.g. `01.014`. Prologue `00`, epilogue `99`, the interlude `INT`. A paragraph inserted later gets a suffix (`01.014a`) so the other IDs do not shift; renumber only when Rafael asks, and then in both files together.
- **Paragraph Parameters** (CSV): Paragraph ID, Chapter, Opening words (EN), Opening words (PT), Voice ID, Voice version, Tuning, Reason for tuning, Review status, Last reviewed, Open issues, Engagement avg, Engagement peak.
- **Engagement** (CSV): Paragraph ID, Sentence, Opening words, Engagement, Tension, Emotion, Pace, Hot words, Uncertain, Reason, Date.
- **Voice Index** (CSV): ID, Name, Type, Whose voice, When used, Based on, Version, Status, Notes.
- **Voice IDs**: `NARR-<NAME>` for narrators, `AUTHOR-<NAME>` for the author's own voice, `CHAR-<NAME>-<FORM>` for characters (e.g. `CHAR-LUZIA-LETTERS`), `BASE-<NAME>` for base voices, `DOC-<NAME>` for document voices.
- **Truth labels** (working notes only, never in the text): DOCUMENTED, STRONGLY SUPPORTED, FAMILY TRADITION, PLAUSIBLE RECONSTRUCTION, FICTIONAL. The research files also use Documented / Contested / Tradition / To verify.

## Standing rules from Rafael

1. Every story line he gives in the chat goes into Chapters, in the chapter where it happens, with all his details. The Character Bible holds personality, backstory and minor details.
2. No new characters, or expanded existing ones, without his approval.
3. He writes the funny childhood episodes himself (from his own and his cousins' childhood); never invent them.
4. Show changes before writing them; never overwrite his or his mom's text without approval.
5. Don't cut arcs yet: brainstorm first, then select against the page budget.
6. Neither he (the great-great-grandfather) nor the woman from Spain is ever named in the book text. **Working names, for planning only**: Benedito (him) and Carmen (the woman from Spain). Use them in chats, Chapters, Scenes and the Character Bible; never in the manuscript.

## How changes are saved

- Show the proposed change first; apply it only after Rafael approves.
- Then commit to `main` with a short message saying what changed and why, and push.
- A chapter being written lives in `drafts/chapter-NN.<lang>.md` until it is approved; then it moves into the manuscript.
- Before a major revision of the manuscript, tag the current commit `draft-N` (N = next number) and push the tag. Tags are never moved. To compare drafts, diff the tag against the current manuscript.

## Voices: decisions so far

- **NARR-MAIN** (main narrator, draft 0.1): close third person, raw and sensory; blend of Itamar Vieira Junior, García Márquez and Tarantino.
- **AUTHOR-MAIN** (Rafael's own voice, draft 0.1): prologue, epilogue and author passages.
- **NARR-GRANDMA**: to be redefined; grandma now appears only inside AUTHOR-MAIN, quoted or retold.
- **BASE-LETTERS-DESPERATE** (draft): base for letters from female characters in desperate conditions; reference author Svetlana Alexievich, adjusted to each character's literacy.
- Voice files written before language layers or Conveying-feeling rules get them the next time they are updated, or before the co-writer first writes prose in that voice.

## Notes for the skills

- **Language layers**: in Portuguese, everyday Brazilian words, words of Tupi, Bantu and Yoruba origin, regionalisms of Bahia, the Pantanal and Mato Grosso do Sul, period words of the 1800s; no Portugal-only usage. In English, keep untranslated and clear by context: senzala, engenho, jornal, ganhadeira, orixá, capitão do mato, Sinhô/Sinhá, carta de alforria, sucuri.
- **Native models for each language**: Gonçalves and Vieira Junior (PT-BR); Szalay and McCarthy (EN); García Márquez, Roa Bastos and Alexievich reach both through translation.
- **Engagement**: anchors are not set yet; propose them from the first chapter scored. Quiet passages in AUTHOR-MAIN can be exactly right at level 2.
- **Low-reliability material** (legends, hearsay, propaganda) is welcome only in a character's mouth, never from the narrator as fact.
