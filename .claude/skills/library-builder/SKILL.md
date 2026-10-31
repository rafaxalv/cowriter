---
name: "library-builder"
description: "Use when the author wants reference books for a book in this repo: it asks what kind of authors to look for, proposes public-domain authors and books with a short style analysis and fit, downloads the chosen ones into the shared library, and keeps a queue so long downloads can continue later."
---

# Library builder

Finds, proposes and downloads full texts of public-domain books into the repo's shared **library** (`library/`), as style references for the voices. Called by the author directly, or by **voice-generator** / **book-voices** when a reference author's text is missing.

This skill is generic: it serves every book in the repo. The library is shared, so nothing book-specific is written into it; the fit to one book is discussed in the chat (and, if the author wants, noted in that book's Author Library).

Files it owns:

| File | Role |
| --- | --- |
| `library/README.md` | What the library holds: one table per language (author, book, translator if any, where it is public domain, file), sources, and "Wanted, not yet found". |
| `library/QUEUE.md` | The download queue: everything chosen but not yet downloaded, so a long list can continue in a later chat. |
| `library/<author-slug>/<book-slug>.txt` | One plain-text file per book, with a short header (title, author, translator, language, source, public-domain note). |
| `.claude/skills/library-builder/scripts/` | The converters and the Wikisource downloader used below. |

Never store anything on the author's computer: every download goes into the repo, through the cloud workspace. Every commit goes through **book-repo**.

## 0. Start

1. Connect the repo with **book-repo** and pull.
2. Read `library/README.md` and `library/QUEUE.md` (create them from the templates at the end if missing).
3. If the queue has items not marked `done`, say how many and ask first: **continue the queue**, or **look for new books** (or both: continue in the background while proposing).

## 1. Ask what to look for

Read the book's `BOOK.md`, its Concept and its voice files (especially the target profiles and reference authors) so the questions are specific, then ask with AskUserQuestion, at most four questions, each with concrete options drawn from the book (multi-select where it makes sense):

1. **Language**: which language layer the references are for (the book's languages from `BOOK.md`; originals or translations).
2. **Style**: what the voice needs to learn (e.g. short raw sentences, oral or vernacular narration, menacing dialogue, irony, lyrical landscape, first-person testimony, letters).
3. **Period**: when the authors wrote (e.g. contemporary with the story, early 20th century, any).
4. **Stories**: what kind of story (e.g. slavery and freedom, war, frontier and land, family decline, childhood, migration, crime).

If the author already said what they want, skip the questions it answers.

## 2. Propose authors and books

Propose 6–10 options, ranked by fit. For each, in a compact table or list:

- **Author, book (year), language**, and the translation if it is not the original.
- **Style** in two lines: how it reads (sentences, register, narrator, dialogue, what it does with violence, humour, landscape).
- **Stories** in one line.
- **Fit**: which voice it would feed and which part of the book (one line, naming the voice file or chapter).
- **Status**: public domain where (see rules below), and where the text can be found (see sources). Mark anything already in the library.

Check every "public domain" and "source available" claim; don't assert from memory when unsure (search). Then ask the author to pick (AskUserQuestion, multi-select; they can also type titles).

### Public-domain rules (check per book, and per translation)

- **US**: published before 1 January of (current year − 95). In 2026, works published in 1930 or earlier.
- **Brazil, EU and most countries**: the author died more than 70 years ago (counted from 1 January after the death). In 2026, authors who died in 1955 or earlier. Brazil is "life + 70" too.
- A translation is a separate work: it needs its own check (the translator's death date, or the translation's publication date for the US). Modern translations are usually protected.
- Free only in some countries is fine when it serves the book's language layer there (e.g. a Brazilian author for the PT-BR layer); record the scope in the README ("BR only"). Never add a text that is protected everywhere.

## 3. Queue the choice

Add every chosen book to `library/QUEUE.md` with its planned source and status `wanted`, then start downloading. The queue is the source of truth for what is left: update it as each book finishes or fails.

## 4. Download strategy

Pick the fastest source that has the book, in this order, and batch work so no single chat runs forever:

1. **GitHub mirrors (fastest; git always works here)**, one `git clone --depth 1` at a time, never in parallel:
   - Standard Ebooks: `github.com/standardebooks/<author>_<title>_<translators>` (English originals and old translations). Check names with `git ls-remote <url> HEAD`; find exact names with a web search on standardebooks.org. Convert with `scripts/standardebooks2txt.py`.
   - GITenberg (Project Gutenberg mirror, ebooks up to about #53000): `github.com/GITenberg/<Title-With-Hyphens>_<ebook-id>`; accented letters and punctuation become `-` (e.g. `El-Gaucho-Mart-n-Fierro_14765`). Convert the `-8.txt` or `.txt` with `scripts/gutenberg2txt.py`.
   - NLTK `machado` corpus (Machado de Assis, complete works, Latin-1): sparse checkout of `packages/corpora/machado.zip` from `github.com/nltk/nltk_data` (branch `gh-pages`).
   - literaturaBR (a few Brazilian classics as R data): `github.com/sillasgonzaga/literaturaBR`, convert with `scripts/rda2txt.py`.
2. **Project Gutenberg direct** (one file per book): `https://www.gutenberg.org/cache/epub/<id>/pg<id>.txt`, then `scripts/gutenberg2txt.py`. Needs `www.gutenberg.org` in the allowed domains.
3. **Wikisource** (slow: one page per chapter, and Wikimedia throttles shared cloud addresses): `scripts/wikisource.py search <host> "<query>"` to find the page title, then `scripts/wikisource.py book ...` **in the background**, one book at a time. It paces requests, backs off on 429 and caches chapters in `<out>.parts/`, so an interrupted book resumes. Delete the `.parts` folder after the book is checked.
4. **Blocked sources** (e.g. dominiopublico.gov.br refuses cloud servers): mark the item `needs file` in the queue and ask the author to attach the file; convert what they attach.

If a fetch is refused by the network policy, say which domain the author would need to allow (Settings > Capabilities on claude.ai) and move on to the next item; never retry the same refused domain in a loop.

**Batching**: do the quick sources first (all GitHub items, then Gutenberg), commit them together, then run Wikisource books one by one in the background. Stop a session after about 30–40 minutes of downloading or when the author wants to stop; whatever is left stays in the queue with its status, ready for "continue the queue" in a later chat.

## 5. Check and save

For each finished book:

1. **Check it**: the word count is plausible for the book; open the start, a middle passage and the end; no navigation text, page numbers, license blocks or broken encoding; the header names the source and translator.
2. **Place it**: `library/<author-slug>/<book-slug>.txt` (lowercase, hyphens, no accents in the path).
3. **Update** the README table for its language (with the public-domain scope) and remove it from "Wanted"; mark it `done` in the queue with the date and word count.
4. **Save** through **book-repo**: show the author the list of files to be added (the texts are public domain and were chosen by them, so a list with word counts is enough), then one commit per batch, message naming the books.

## 6. Report

One short message: what was added (author, book), what is still in the queue and why (slow source, needs a domain allowed, needs a file), and the next step. If the books feed a voice, offer to add them as references in that book's `voices/00-author-library.md` (via **book-voices**; show the change first).

## Templates

`library/QUEUE.md`:

```markdown
# Library download queue

Books chosen for the library but not yet downloaded. Maintained by the library-builder skill; "continue the queue" picks up from here.

Status: `wanted` (not started), `downloading`, `needs domain` (name it), `needs file` (author to attach), `not found`, `done`.

| Author | Book | Language | PD scope | Source plan | Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
```
