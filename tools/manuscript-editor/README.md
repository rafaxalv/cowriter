# Manuscript Desk (manuscript editor)

A page for working on a book paragraph by paragraph. Works for any book in `books/`.

- Each paragraph is its own cell. Click a cell to select it and edit the text in place, in one language or side by side.
- The panel on the left shows the selected paragraph's voice and its 18 style dimensions. The shaded band is the range the voice allows, the tick is its base value. Moving a slider records a tuning for that paragraph only (for example "Violence rendering +1"); values outside the range turn amber and need a reason.
- **Run heatmap** asks Claude to score every sentence of the open chapter for engagement, tension, emotion and pace (the method of the engagement-heatmap skill), then highlights each sentence like a marker pen, from Flat (1) to Gripping (5), while the text stays editable. Each paragraph's header shows its overall score (the average of its sentences; hover it for the peak). The chart in the top bar, next to the heatmap controls, shows every paragraph's average and peak; **Hide chart** collapses it. The panel lists each sentence's scores and reason.
- **Apply to text** (in the panel, once you have moved a slider) rewrites the paragraph in every language to hit the new targets, using the paragraph-review skill's hand-tuning method. The request carries the skill's own instructions plus everything it would read in the repo: the voice file, the book profile, the Concept, the Shared Rules, the Bilingual Lexicon, the whole Character Bible with its Continuity section, the chapter's plan and scene map, and the paragraphs before and after. The new text replaces the old at once; the panel shows what changed and what to check, with **Undo rewrite**.
- Each paragraph also has a review status, open issues, "Add below" and "Remove" (removed paragraphs stay visible and can be restored until the next sync).

**Open it**: https://claude.ai/artifact/JUwgT7M2925eYnvdfMVWSB (private to Rafael). Scoring uses the viewer's own Claude usage and asks for permission the first time.

## How it connects to the repo

The page does not edit the repo directly. It keeps the book in its own store, and Claude moves it in and out:

1. **Keep the context current**: after changing the Concept, Chapters, Scenes, the Character Bible, a voice file, BOOK.md or the paragraph-review skill, re-run the export and upload only `books/<slug>/context/*`, `books/<slug>/voices/*` (update, with `if_version`) and `skills/paragraph-review`, so rewrites never use an outdated plan. Do not re-upload paragraphs that have unsynced edits.
1. **Load a book into the editor**: `python3 tools/manuscript-editor/export_book.py books/<slug> <out>` writes one JSON file per store document; upload them with the ArtifactData tool (`batch`, `set`, `file_path`) to the paths below. Re-loading replaces the editor's copy, so sync first if there are edits there.
2. **Sync edits back to the repo**: read the store with ArtifactData `list` and `out_dir` for each of `books/<slug>/paragraphs`, `books/<slug>/voices` and `books/<slug>/heatmaps`, then run `python3 tools/manuscript-editor/sync_back.py books/<slug> <out_dir>`. It rewrites the manuscript files (text, order, IDs; removed paragraphs dropped), `config/paragraph-parameters.csv` (voice, version, tuning, reason, status, issues, engagement avg and peak) and `config/engagement.csv` (latest scores of the first language). Show the author `git diff`, commit after approval, then set `syncedAt` on the `books/<slug>` document to the current time in milliseconds so the page stops flagging those paragraphs.

The page shows "not in repo yet" on every paragraph edited since the last sync.

## Store layout

| Path | Contents |
| --- | --- |
| `books/<slug>` | title, one-line context, languages (`key`, `code`, `file`), chapters (`id`, titles and part per language), the 18 dimensions, engagement anchors, `syncedAt` |
| `books/<slug>/paragraphs/<pid>` | `pid`, `chapter`, `order` (sort key), `text` per language key, `voice`, `tuning` (dimension number → offset from the voice base), `reason`, `status`, `notes`, `removed`, `updatedAt` |
| `books/<slug>/voices/<ID>` | `id`, `name`, `version`, `dims` (dimension number → `base`, `min`, `max`, `note`), from the voice file's Target profile table |
| `books/<slug>/context/book` | the files a rewrite must respect: `profile` (BOOK.md), `concept`, `sharedRules`, `lexicon`, `characterBible` |
| `books/<slug>/context/ch-<chapter>` | `plan` (the chapter's entry in Chapters) and `scenes` (its scene map) |
| `skills/paragraph-review` | `text`: the paragraph-review skill, sent with every rewrite |
| `books/<slug>/heatmaps/<chapter>_<lang>` | `runAt`, `summary`, `turning`, `hashes` (paragraph text at scoring time), `sentences` (`pid`, `i`, `start`, `end`, `e`, `e2`, `t`, `m`, `p`, `hot`, `r`, `u`) |

Language keys are the profile's language codes in lower case with `_` for `-` (`EN` → `en`, `PT-BR` → `pt_br`). New paragraphs added in the editor get the next free ID in the chapter, or a letter suffix when inserted between two (`01.014a`), as the book profile prescribes.

## Files

- `index.html`: the page (republish this file to update the artifact at the same URL).
- `export_book.py`: book folder → store documents.
- `sync_back.py`: store documents → book folder.
