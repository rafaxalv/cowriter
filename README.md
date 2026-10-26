# Cowriter

A workspace for writing books with Claude. The writing skills are shared and generic; each book keeps everything specific to it in its own folder.

## Layout

```
.claude/skills/        the book skills (generic, used by every book)
books/
  <slug>/
    BOOK.md            the book profile: paths, people, languages, formats, rules
    outline/           concept, chapters, scenes
    book/              the manuscript, one file per language
    characters/        Character Bible (with its Continuity section)
    voices/            voice files, voice index, shared rules, author library
    config/            paragraph parameters, engagement scores and anchors
    research/          sources, notes, timelines, images
    drafts/            chapters being written (created when needed)
tools/
  manuscript-editor/   Manuscript Desk: Chapters tab (events, facts, sources) and Book tab (paragraphs, voice tuning, heatmap)
```

## Books

| Folder | Book |
| --- | --- |
| [`books/grandgrandfather/`](books/grandgrandfather/) | Book: Grandgrand father story (working title), by Rafael. English and Brazilian Portuguese. |

## Skills

| Skill | What it does |
| --- | --- |
| co-writer | The writing partner: sets up a new book, plans chapters, writes prose from scene maps, keeps every file in sync. Coordinates the others. |
| scene-builder | Turns a chapter's events into an ordered scene map. |
| book-voices | Owns the narrative voices: creates, lists, compares, adjusts and validates them. |
| voice-generator | Builds or updates a voice from reference authors, with a fixed 18-dimension style framework. |
| chapter-review | Reviews a whole chapter: scene map, voices, tuning, plot, continuity. |
| paragraph-review | Checks and fine-tunes single paragraphs against a voice. |
| engagement-heatmap | Scores a chapter for engagement, tension, emotion and pace, as a heatmap. |
| book-repo | Connects this repo to a chat and saves every approved change (commit, push, snapshots). Kept as an account-level skill, outside the repo, so it works before the repo is connected. |

Every skill starts by finding the book's `BOOK.md` and reading it. To start a new book, ask the co-writer; it creates `books/<slug>/` from `.claude/skills/co-writer/templates/BOOK.md`.

## Tools

- **Manuscript Desk** (`tools/manuscript-editor/`): organize each chapter's events, facts and research sources (Chapters tab), and edit the book paragraph by paragraph, tuning each paragraph's voice parameters and running an engagement heatmap over a chapter (Book tab). It keeps its own copy of the book; Claude loads books into it and syncs edits back (see its README).
