# Cowriter: the great-great-grandfather book

Working files for Rafael's book about his great-great-grandfather: born enslaved in Bahia, freed by the Paraguayan War, winner of a lottery, owner of a farm at Jacadigo, husband of a woman trafficked from Spain. Immersive historical fiction, written in English and Brazilian Portuguese side by side.

This repo was copied from the Google Drive folder *Projeto Livro* on 10 Oct 2026. Drive was left untouched; from now on this repo is meant to be the master copy.

## How the files fit together

```
outline/concept.md  →  outline/chapters.md  →  outline/scenes.md  →  book/manuscript.en.md
   key ideas              every event,            each chapter            book/manuscript.pt-br.md
   and rules              chapter by chapter      broken into scenes      the text
```

Changes flow down (concept → chapters → scenes → text); deliberate changes in the text flow back up. Used at every level: the Character Bible, the research and the voices.

## Layout

| Folder | What's in it | Drive original |
| --- | --- | --- |
| `book/manuscript.en.md`, `book/manuscript.pt-br.md` | The book text, one file per language. Matching paragraphs share an ID (chapter.row; prologue 00, interlude INT, epilogue 99) in a hidden comment, so the two versions stay in step | Book |
| `outline/concept.md` | Key ideas, standing rules, the story in six movements | 00 Book Concept |
| `outline/concept-archive.md` | The long earlier version of the concept (Oct 7, 2026) | Configuration / Book Concept — archive |
| `outline/chapters.md` | The plan of record: every event per chapter, with sources | Chapters |
| `outline/scenes.md` | Scene maps (chapter 1 in progress) | Scenes |
| `characters/character-bible.md` | Who everyone is, plus the Continuity section | Character Bible |
| `voices/` | Narrative voices (NARR-MAIN, AUTHOR-MAIN, BASE-LETTERS-DESPERATE), shared rules, author library, voice index | Configuration / Voices |
| `config/` | Engagement anchors, engagement and paragraph-parameter sheets (CSV) | Configuration |
| `research/paraguayan-war/` | War research notes, Paraguayan perspective, slavery timeline and compilation | Registros historicos |
| `research/timelines/` | Paraguayan War timeline (1811–1892) and the timeline recipe | Registros historicos / Timelines |
| `research/places/` | Jacadigo (location note and the Região search) | Claude project note; Região |
| `research/family/` | Maternal family tree research, family memories and stories, MyHeritage screenshot | Registros historicos |
| `research/freed-slave-rights-1865-1888.md` | What a freed slave could and couldn't do | Registros historicos |
| `research/sources/dados-gerais.md` | Source doc on the Zuavos baianos and Dom Obá (Bento, Kraay, COPIR) | Dados gerais |

Portuguese documents stay in Portuguese, so nothing is lost in translation.

## Still only in Drive

These binary files were not copied; they are still in *Projeto Livro*:

- `Imagens/`: nine photos (including `candido_fonseca.jpeg`)
- `Registros historicos/garajo,+8.+Borba.pdf`
- `Registros historicos/MyHeritage Family chart.png`

Upload them here (or ask Claude to) if you want them versioned too.

## Rules that apply everywhere

- Neither he nor the woman from Spain is ever named in the book text. Working names for planning only: Joaquim and Carmen.
- Every story line Rafael gives goes into `outline/chapters.md`; the Character Bible holds personality, backstory and minor details.
- No new characters, or expanded ones, without Rafael's approval. He writes the funny childhood episodes himself.
- Never overwrite Rafael's or his mom's text without approval; when his mom wrote the Portuguese, it is the source and the English follows it.
