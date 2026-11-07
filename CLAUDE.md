# Cowriter repo

- Books live in `books/<slug>/`. Before working on a book, read its `BOOK.md` (the book profile), then its Concept. If there are several books and it is unclear which one is meant, ask.
- The skills in `.claude/skills/` are generic and shared by every book. Never put book-specific content (story, names, rules, paths of one book) in a skill; put it in that book's folder, usually in `BOOK.md`.
- Show proposed changes to book files first; apply them after the author approves. Every commit, push and tag goes through `.claude/skills/book-repo/SKILL.md`; no other skill runs git commit, push or tag itself.
- The Manuscript Desk (`tools/manuscript-editor/`) keeps its own copy of a book. Before changing a book's manuscript or Paragraph Parameters in the repo, check whether the editor has unsynced edits and sync them first (steps in its README), so neither side overwrites the other.

## graphify

Each book can have its own knowledge graph in `books/<slug>/graphify-out/`: characters, places, events, sources and how they connect. A book's `.graphifyignore` says which of its folders the graph covers.

Rules:
- Run graphify from the book's folder (`cd books/<slug>`), so `graphify-out/` and `.graphifyignore` are found. If the tool is missing, install it with `pip install graphifyy`.
- When a book's `graphify-out/graph.json` exists, use `graphify query "<question>"`, `graphify path "<A>" "<B>" --undirected` or `graphify explain "<name>"` for questions about who or what connects to what, before reading many files. Read raw files only for the lines the graph points to. The files themselves (research, Character Bible, Chapters) stay the source of truth; the graph is a map of them.
- Read the book's `graphify-out/GRAPH_REPORT.md` only for a broad overview.
- After research files, the Character Bible or the Chapters file change, refresh the graph with `/graphify . --update` from the book's folder; it re-reads only changed files. (`graphify update` alone only handles code and does not see Markdown changes.)
- A book graph holds only story things: people, places, events, chapters, motifs, songs, laws, cited works. Never make a node for a file itself (no node for the Chapters file, the Character Bible or a research note) and no "mentions" links from files; every node already records its source file. Tell any extraction subagent this.
- `graphify export html` writes a page that loads its graph library from unpkg.com, which the claude.ai file preview blocks. After each export, replace that `<script src="https://unpkg.com/vis-network...">` tag with the library inlined (`npm pack vis-network@9.1.6`, file `standalone/umd/vis-network.min.js`).
- A committed `graph.json` is rewritten whole on every build, so a large diff to it is expected.
