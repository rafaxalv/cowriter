# Manuscript Desk (manuscript editor)

A page for working on a book, with two tabs: **Chapters** (the plan of record) and **Book** (the text, paragraph by paragraph). Works for any book in `books/`.

## Chapters tab

Each chapter's entry in the Chapters file, organized into four sections, each item its own editable cell:

- **Stories**: the events of the chapter, in order.
- **Facts**: historical facts the chapter relies on, each with a truth label (from BOOK.md) and the sources that back it.
- **Sources**: articles, books and links, numbered S1, S2… per chapter; each can point to one of the book's research files.
- **Notes**: open questions and options.

Select a cell to set it up in the panel on the left: its kind, a fact's truth label and "to verify" flag, which sources back a fact or event (tick them), which research file a source belongs to, or move it to another chapter. With nothing selected, the panel lists what is left to organize in the chapter (facts with no source or no label, things to verify, sources nobody cites) and the book's research files with the chapters that cite each one. The chapter header holds the "When / where" line, the counts, and a warning when the Chapters file and the Book file give the chapter different titles.

## Book tab

- Each paragraph is its own cell. Click a cell to select it and edit the text in place, in one language or side by side.
- The panel on the left shows the selected paragraph's voice and its 18 style dimensions. The shaded band is the range the voice allows, the tick is its base value. Moving a slider records a tuning for that paragraph only (for example "Violence rendering +1"); values outside the range turn amber and need a reason.
- **Run heatmap** asks Claude to score every sentence of the open chapter for engagement, tension, emotion and pace (the method of the engagement-heatmap skill), then highlights each sentence like a marker pen, from Flat (1) to Gripping (5), while the text stays editable. Each paragraph's header shows its overall score (the average of its sentences; hover it for the peak). The chart in the top bar, next to the heatmap controls, shows every paragraph's average and peak; **Hide chart** collapses it. The panel lists each sentence's scores and reason.
- **Apply to text** (in the panel, once you have moved a slider) rewrites the paragraph in every language to hit the new targets, following the paragraph-review skill's rewrite brief. The request is kept light: its bulk is the chapter itself (every paragraph in every language, with the one to rewrite and its neighbours marked); around it go short briefs: the voice's rules and language notes, the scene's beats and Reader feeling, the book's roles, standing rules and handle-with-care notes, and the Continuity facts. For chapter 1 that is about 30 KB. The new text replaces the old at once; the panel shows what changed and what to check, with **Undo rewrite**.
- Each paragraph also has a review status, open issues, "Add below" and "Remove" (removed paragraphs stay visible and can be restored until the next sync).

**Open it**: https://claude.ai/artifact/JUwgT7M2925eYnvdfMVWSB (private to Rafael). Scoring uses the viewer's own Claude usage and asks for permission the first time.

## How it connects to the repo

The page does not edit the repo directly. It keeps the book in its own store, and Claude moves it in and out:

1. **Keep the context current**: after changing the Concept, Chapters, Scenes, the Character Bible, a voice file, BOOK.md or the paragraph-review skill, re-run the export and upload only `books/<slug>/context/*`, `books/<slug>/voices/*` (update, with `if_version`) and `skills/paragraph-review`, so rewrites never use an outdated plan. Do not re-upload paragraphs that have unsynced edits.
1. **Load a book into the editor**: `python3 tools/manuscript-editor/export_book.py books/<slug> <out>` writes one JSON file per store document; upload them with the ArtifactData tool (`batch`, `set`, `file_path`) to the paths below. Re-loading replaces the editor's copy, so sync first if there are edits there.
2. **Sync edits back to the repo**: read the store with ArtifactData `list` and `out_dir` for each of `books/<slug>/paragraphs`, `books/<slug>/voices`, `books/<slug>/heatmaps`, `books/<slug>/plan` and `books/<slug>/planChapters`, then run `python3 tools/manuscript-editor/sync_back.py books/<slug> <out_dir>`. It rewrites each chapter entry of `outline/chapters.md` as When / where, Stories, Facts, Sources and Notes (removed items dropped; the file's introduction, part notes and arc brainstorm untouched), the manuscript files (text, order, IDs; removed paragraphs dropped), `config/paragraph-parameters.csv` (voice, version, tuning, reason, status, issues, engagement avg and peak) and `config/engagement.csv` (latest scores of the first language). Show the author `git diff`, commit after approval, then set `syncedAt` on the `books/<slug>` document to the current time in milliseconds so the page stops flagging those paragraphs.

The page shows "not in repo yet" on every paragraph and Chapters item edited since the last sync. The first sync of the Chapters tab reorganizes the whole Chapters file into the new sections, so review that diff with the author before committing.

## Store layout

| Path | Contents |
| --- | --- |
| `books/<slug>` | title, one-line context, languages (`key`, `code`, `file`), chapters (`id`, titles and part per language), the 18 dimensions, engagement anchors, `truthLabels`, `research` (path and title of each document in `research/`), `syncedAt` |
| `books/<slug>/paragraphs/<pid>` | `pid`, `chapter`, `order` (sort key), `text` per language key, `voice`, `tuning` (dimension number → offset from the voice base), `reason`, `status`, `notes`, `removed`, `updatedAt` |
| `books/<slug>/voices/<ID>` | `id`, `name`, `version`, `dims` (dimension number → `base`, `min`, `max`, `note`, from the voice file's Target profile table) and `brief` (Voice rules, Conveying feeling and each language layer without references or sample paragraphs) |
| `books/<slug>/context/book` | `brief` (BOOK.md's people and roles and standing rules, the Concept's handle-with-care notes, Shared Rules, Lexicon) and `continuity` (the Character Bible's Continuity section) |
| `books/<slug>/context/ch-<chapter>` | `brief`: per scene of the scene map, when, where, point of view, beats and Reader feeling (or the start of the chapter's plan if there is no scene map) |
| `skills/paragraph-review` | `brief`: the skill's "Rewrite brief" section, sent with every rewrite |
| `books/<slug>/plan/<id>` | one Chapters item: `id`, `chapter`, `order`, `kind` (`event`, `fact`, `source`, `note`), `text`, `label` (truth label), `verify`, `file` (research file path, sources only), `sources` (ids of the chapter's source items), `removed`, `updatedAt` |
| `books/<slug>/planChapters/<chapter>` | `title` (as written in the Chapters file), `when`, `updatedAt` |
| `books/<slug>/heatmaps/<chapter>_<lang>` | `runAt`, `summary`, `turning`, `hashes` (paragraph text at scoring time), `sentences` (`pid`, `i`, `start`, `end`, `e`, `e2`, `t`, `m`, `p`, `hot`, `r`, `u`) |

Language keys are the profile's language codes in lower case with `_` for `-` (`EN` → `en`, `PT-BR` → `pt_br`). New paragraphs added in the editor get the next free ID in the chapter, or a letter suffix when inserted between two (`01.014a`), as the book profile prescribes.

## Files

- `index.html`: the page (republish this file to update the artifact at the same URL).
- `export_book.py`: book folder → store documents.
- `sync_back.py`: store documents → book folder.
- `plan_md.py`: reads and writes the Chapters file as items (used by both scripts).
