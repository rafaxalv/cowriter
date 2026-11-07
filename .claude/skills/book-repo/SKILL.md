---
name: book-repo
description: "Use for all commits, pushes, tags, and repository handoffs in this book workspace."
---

# Book repo

This skill owns Git operations for the current Cowriter checkout. Book skills prepare and validate changes; this skill saves approved changes.

## Connect

At the start of repository work:

1. Confirm the workspace root with `git rev-parse --show-toplevel` and confirm it is this Cowriter repository.
2. Confirm `origin` points to the expected GitHub repository. Do not print credential-bearing remote URLs.
3. Check `git status --short`, the current branch and latest commit. If the worktree contains changes from an earlier task, list them and ask what to do before proceeding.
4. Work on `main`. Before editing, pull the latest `origin/main` with `git pull --rebase origin main` when the worktree is clean.

## Before saving

1. Confirm the author approved the exact change set. Never commit unapproved book text or files.
2. Read the book's `BOOK.md` section on saving changes and follow its snapshot requirements.
3. Check `git status --short`, `git diff --stat` and the full diff. Stage only the intended files; do not include unrelated changes.
4. Run the relevant validation, including a whitespace check. Respect existing line-ending conventions.

## Commit and push

1. Commit one approved change set at a time to `main`. Use a plain message that says what changed and why; name the book and chapter when applicable.
2. Before pushing, run `git pull --rebase origin main`, then `git push origin main`.
3. Verify `git status -sb` shows `main` synchronized with `origin/main`. Report the change and short commit hash.
4. If a rebase conflicts, stop and show both versions for the author's decision. Never resolve a story conflict silently.
5. If a push is rejected, pull and rebase once, then retry once. If it still fails, leave the commit in place and report the reason.
6. Never force-push, rewrite published history or push another branch without the author's approval.

## GitHub authentication

If GitHub authentication fails, check `gh auth status`. For an expired login, start `gh auth login --hostname github.com --git-protocol https --web` and have the author complete authorization in the browser. Never ask the author to share a password, token or one-time code in chat.

## Book graph

When the book has a graph (`books/<slug>/graphify-out/`) and a saved change touched a file it covers (Chapters, the Character Bible, the Concept, Scenes, research; not those in `.graphifyignore`), say in one line that the graph is now behind and offer to refresh it. Do not refresh unasked: each refresh re-reads every changed file, so the author may prefer to batch several changes. A refresh follows the graphify rules in the repo's `CLAUDE.md` and is saved like any other change.

## Manuscript Desk

After changing the Concept, Chapters, Scenes, Character Bible, a voice file, `BOOK.md`, research or paragraph-review instructions, the Manuscript Desk's context is out of date. Follow its README to refresh only the affected context, docs and voice documents; do not re-upload paragraphs with unsynced edits. If the required ArtifactData tool is unavailable, say the refresh is blocked and do not claim it was done.

Before editing manuscript files or Paragraph Parameters, check the Manuscript Desk README for unsynced edits and sync them back first.
