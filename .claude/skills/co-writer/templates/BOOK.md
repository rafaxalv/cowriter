# Book profile: <working title>

The profile every book skill reads first. It says where this book's files are, who works on it, which languages it is written in, how its files are formatted and which standing rules apply. The story itself, its key ideas and what to handle with care are in `outline/concept.md`.

All paths below are relative to this folder (`books/<slug>/`).

## The book

- **Working title**: <title> (to decide?)
- **In one line**: <the story spine>
- **Length**: <target> words; <limit> is a hard limit.
- **Status**: <what is planned, drafted, done>

## People and roles

- **<Author>** (the author): <what they write, in which language; they decide everything>.
- **<Co-author>** (optional): <what they write; whose wording is the source in which language>.

## Languages

| Code | Language | Manuscript | Written first? |
| --- | --- | --- | --- |
| EN | English | `book/manuscript.en.md` | Yes |

(Add a row per language, e.g. PT-BR, `book/manuscript.pt-br.md`.)

## Files

| Role (name used by the skills) | Path |
| --- | --- |
| Concept | `outline/concept.md` |
| Chapters (plan of record) | `outline/chapters.md` |
| Scenes (scene maps) | `outline/scenes.md` |
| Manuscript | `book/manuscript.<lang>.md` (one per language) |
| Drafts (chapters being written) | `drafts/` |
| Character Bible | `characters/character-bible.md` |
| Continuity record | the **Continuity** section at the end of the Character Bible |
| Voices folder | `voices/` |
| Voice Index | `voices/00-voice-index.csv` |
| Shared Rules | `voices/00-shared-rules.md` |
| Bilingual Lexicon | `voices/00-bilingual-lexicon.md` (multilingual books; create when first needed) |
| Author Library | `voices/00-author-library.md` |
| Voice files | `voices/<ID>.md` |
| Paragraph Parameters | `config/paragraph-parameters.csv` |
| Engagement scores | `config/engagement.csv` |
| Engagement Anchors | `config/engagement-anchors.md` |
| Research | `research/` |

## Formats

- **Manuscript**: one file per language. `#` title, `##` parts, `###` chapters. Each paragraph is preceded by its ID in a hidden comment, e.g. `<!-- 01.003 -->`; the same ID marks the same paragraph in every language file. Chapters not yet written hold a placeholder line.
- **Paragraph ID**: chapter.row with three digits, e.g. `01.014`. Prologue `00`, epilogue `99`. A paragraph inserted later gets a suffix (`01.014a`); renumber only when the author asks, in all language files together.
- **Paragraph Parameters** (CSV): Paragraph ID, Chapter, Opening words (one column per language), Voice ID, Voice version, Tuning, Reason for tuning, Review status, Last reviewed, Open issues, Engagement avg, Engagement peak.
- **Engagement** (CSV): Paragraph ID, Sentence, Opening words, Engagement, Tension, Emotion, Pace, Hot words, Uncertain, Reason, Date.
- **Voice Index** (CSV): ID, Name, Type, Whose voice, When used, Based on, Version, Status, Notes.
- **Voice IDs**: `NARR-<NAME>`, `AUTHOR-<NAME>`, `CHAR-<NAME>-<FORM>`, `BASE-<NAME>`, `DOC-<NAME>`.
- **Truth labels** (if the book mixes fact and invention; working notes only): DOCUMENTED, STRONGLY SUPPORTED, FAMILY TRADITION, PLAUSIBLE RECONSTRUCTION, FICTIONAL.

## Standing rules from the author

1. Every story line the author gives in the chat goes into Chapters, in the chapter where it happens, with all their details.
2. No new characters, or expanded existing ones, without the author's approval.
3. Show changes before writing them; never overwrite the author's or a co-author's text without approval.
4. <any other rule: names never given, working names, things the author writes personally>

## How changes are saved

- Show the proposed change first; apply it only after the author approves.
- Then commit to `main` with a short message saying what changed and why, and push.
- A chapter being written lives in `drafts/chapter-NN.<lang>.md` until it is approved; then it moves into the manuscript.
- Before a major revision of the manuscript, tag the current commit `draft-N` and push the tag.

## Voices: decisions so far

- <none yet>

## Notes for the skills

- <language-layer notes: words kept untranslated, regional and period vocabulary, usage to avoid>
- <engagement notes: which voices are deliberately quiet>
