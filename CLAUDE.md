# Cowriter repo

- Books live in `books/<slug>/`. Before working on a book, read its `BOOK.md` (the book profile), then its Concept. If there are several books and it is unclear which one is meant, ask.
- The skills in `.claude/skills/` are generic and shared by every book. Never put book-specific content (story, names, rules, paths of one book) in a skill; put it in that book's folder, usually in `BOOK.md`.
- Show proposed changes to book files first; apply them after the author approves. Every commit, push and tag goes through the **book-repo** skill (an account-level skill, so it also works before the repo is connected); no other skill runs git commit, push or tag itself.
- The Manuscript Desk (`tools/manuscript-editor/`) keeps its own copy of a book. Before changing a book's manuscript or Paragraph Parameters in the repo, check whether the editor has unsynced edits and sync them first (steps in its README), so neither side overwrites the other.
