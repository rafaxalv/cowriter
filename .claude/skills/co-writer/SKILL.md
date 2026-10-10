---
name: "co-writer"
description: "Use when the user wants to work on a book project: planning or refining chapters, drafting or revising text, syncing changes across language versions and the other book files, choosing voices, or checking that the plot holds together."
---

# Co-writer

The co-writer is the author's writing partner for a whole book. It knows the story, the files and the other book skills, and it decides which of them to use. It does not replace them: it coordinates them, writes the prose from the scene maps, and keeps every file consistent.

This skill is generic. Everything specific to one book (story, key ideas, rules, working names, standing instructions from the author, file IDs) lives in that book's **00 Book Concept**, never in this skill.

## The process: Concept -> Chapters -> Scenes -> Book

| Level | File | What it is | Detail |
|---|---|---|---|
| 1 | **00 Book Concept** | A short introduction to the project for the author, a co-writer or an AI: working context (book, rules, working names, files), the story in brief, key ideas, how it is told, what to handle with care. Generic: no event lists. | Least |
| 2 | **Chapters** | The skeleton of the book: every event to describe in each chapter, in order, with when/where, ages, characters present, voice plan, open items, and sources for the real events that must be accurate. | Medium |
| 3 | **Scenes** | The scene maps: for each chapter, the events expanded into ordered scenes (when, where, point of view, characters, beats, motivations, feelings, reader feeling, place details, history carried, function, voice, target length). Built by the **scene-builder** skill. | High |
| 4 | **Book** | The final product: the scene maps written as prose, in the planned voices. | Full |

**The Concept branches into the reference files**, used at every level:

- **Character Bible**: who people are (personality, backstory, motives, relationships, minor details, inheritance chains), plus a **Continuity** section at the end with what the Book text has established (per character, and places, objects, dates).
- **Historical research** (the research folder): sources, records and notes that Chapters cites.
- **Voices** (Configuration/Voices, owned by book-voices): the voice files, Voice Index, Shared Rules and Bilingual Lexicon.

**How changes move:**

- **Down**: a concept decision shapes the Chapters; a Chapters event becomes one or more scenes; a scene becomes Book text. Never write a scene that is not in Chapters, or text that is not in a scene; add it to the level above first.
- **Up**: decisions made while building scenes (bridges, choices between options) go back into Chapters. When the Book deliberately changes something, update Scenes and Chapters (after the author confirms). When a decision changes the premise or a key idea, update the Concept. Keep the Concept short: it gets the idea, Chapters gets the events, Scenes gets the staging.
- **Sideways**: the Character Bible is updated with personality and backstory as decisions are made; its Continuity section is updated only from approved Book text. When the text contradicts the planned part of the Bible, the text wins and the plan is updated.

**Which file wins when they disagree:** for events, Chapters; for how a chapter is staged, Scenes; for what the text actually says, the Book and the Bible's Continuity section; for who people are, the Character Bible; for rules and key ideas, the Concept.

Trial files (marked TEST in their titles), if any exist, are only examples of the format; never treat them as the real Scenes or Book.

## The book skills and who does what

- **co-writer** (this skill): coordinates; plans chapters with the author; writes the prose from the scene maps; keeps files in sync.
- **scene-builder**: Chapters -> Scenes.
- **book-voices**: owns the voices; **voice-generator** builds or updates a voice with it.
- **chapter-review**: reviews a written chapter against its scene map, the voices, plot and continuity; sends paragraphs to **paragraph-review**.
- **paragraph-review**: checks and fine-tunes paragraphs against a voice.
- **engagement-heatmap**: scores pace and engagement.

## Start of every session: load the Book Concept

1. Find the book's **00 Book Concept** doc in the book's main folder (search Drive by title, or use the folder the author names).
2. Read it in full before anything else, then read the Chapters, Scenes and Character Bible sections the session needs.
3. Follow it. Where it conflicts with this skill, the Book Concept wins for that book.
4. When a new standing decision is made (a rule, a working name, a new file, a length change, a key idea), propose the matching change to the Concept and apply it after approval. If a Concept passage has been overtaken by Chapters, shorten it to the idea and point to Chapters.

## New project: create the Book Concept

If no Book Concept exists (a new book, or the author says so), create it before planning anything:

1. Ask, in one round, only what you cannot find in the existing files: working title; author and co-authors; languages (and which is written first); length target; the story spine in a few lines; any fixed story rules; the main folder in Drive.
2. Create the main folder structure if it does not exist (after asking): 00 Book Concept, Chapters, Scenes, Book, Character Bible (with a Continuity section at the end), a Configuration folder (Paragraph Parameters, Voices), and a research folder.
3. Create **00 Book Concept** from the template below, filled with the answers and the new file IDs. Keep it to a few pages. Show it to the author.

**Book Concept template** (headings, in this order):

- *Working context*: the book (title, author and co-authors, languages, length target and limit); working names; standing rules from the author; how the files fit together (the four levels and the reference files); files with Drive IDs; Book doc format; editing notes.
- *The book in one paragraph*.
- *The story in movements*: one or two lines per part, no event lists.
- *Key ideas*: motifs, themes or forces, central ironies, what passes between generations.
- *How it is told*: style, point of view and voices, chapter shape, tone.
- *Handle with care*: sensitive material, truth labels if the book mixes fact and invention.

## Where story decisions go

- **Every story line the author gives in the chat goes into the Chapters doc**, in the chapter where it happens, with all the details they gave (who, what, why, how it ends, lines they want repeated). Nothing that happens in the story lives only in the Character Bible, the Concept, Scenes or the chat.
- If a story line spans several chapters, write the set-up and the payoff in their chapters, with cross-references ("see ch. 21", "pays off in ch. 25"). Update any brainstorm or arc lists in the Chapters doc when they are affected.
- Real events that must be accurate get their sources in the chapter where they appear; longer research goes in the research folder.
- The **Character Bible** then gets the personality, backstory, motives, traits, relationships and short pointers to the chapters. It does not carry the plot on its own.
- The **Concept** changes only when a key idea or rule changes.
- When applying a change, update Chapters first, then the Character Bible, then the Concept if needed, then any scene map already built for that chapter; verify each. In the summary, list what went into each file.
- Before closing a topic, check that everything the author said in the conversation is in the Chapters doc.

## The writing flow (always in this order)

### 1. Plan the chapter (Chapters)

Work with the author until the chapter's events are **well defined**: when and where, ages, the stories in order, the characters present (checked against the Bible and its Continuity section), the history it carries with sources, the key ideas it touches, open items resolved or consciously left open, and a continuity check against the previous and next chapters. Show what is missing. Propose ideas, but the author decides; mark proposals as proposals.

### 2. Choose the voices

Read the Voice Index (via **book-voices**). Recommend which voice to use for the chapter and for any special parts (letters, documents, frame passages). If a needed voice does not exist or is still a draft, say so and offer to build it with **voice-generator** (which works with **book-voices**). Record the voice plan in the chapter's entry in Chapters.

### 3. Build the scenes (Scenes)

Run **scene-builder** on the chapter. It writes the scene map into Scenes and lists the decisions needed. Get the author's answers; scene-builder writes approved decisions back into Chapters.

### 4. Write the prose (from the scene map, in the voices)

- Read the chapter's scene map as it is now in Scenes (the author may have edited it directly; their wording wins), the voice files it names (core, language layer, rules, reference paragraphs), 00 Shared Rules and 00 Bilingual Lexicon.
- Write scene by scene, following the beats, motivations, feelings, place details and target lengths. Each paragraph belongs to one voice; note it so the Paragraph Parameters rows can be filled. If a voice is not defined yet, write plainly in the point of view the scene map gives and say so.
- Aim every scene at its **Reader feeling** from the scene map, using the **Conveying feeling** rules of the voice that writes it (each voice file defines how that voice makes the reader feel; see book-voices). If the voice has no such rules yet, say so and offer to add them with voice-generator before writing.
- Do not add events, named characters or facts that are not in the scene map. If the prose needs something new, propose it and, after approval, add it to Scenes and Chapters first.
- For a multilingual book, write first in the language the Concept names (or the one the author starts in); produce the others after the first is approved, so every version says the same thing.
- Write the draft in a working copy (a separate doc, for example "Book — Chapter N draft") or in the chat; never straight into the Book doc.
- At the end, list for the author: anything invented beyond the scene map, length against the target, whether each scene lands its Reader feeling (and where it is weakest), and points to check.

### 5. Review

- Run **chapter-review** on the draft (it checks against the scene map and coordinates **paragraph-review**) for voice, tuning, plot and continuity.
- Optionally run **engagement-heatmap** for pace and engagement, and compare its emotional curve with the Reader feeling planned for each scene.
- After approval, move the chapter into the **Book** doc, create its rows in **Paragraph Parameters** (if the project uses it) in the same pass, and add what the text has established to the **Continuity** section of the Character Bible.

### 6. Drafts

The Book doc is always the current draft (one working copy only). Before a major revision, save a snapshot copy to a **Drafts** subfolder in the main folder, named "Book — draft N — YYYY-MM-DD" (create the folder the first time, after asking). Snapshots are never edited. To compare drafts, read the snapshot and the current Book and list what changed.

## Syncing changes backwards and sideways

Changes can start anywhere: the author edits one language, a co-author edits another, a chapter plan or scene map changes, a character changes. Whenever the author says something changed, or at the start of any session on a chapter, run a sync check.

1. **Find the changes.** For a multilingual book, compare the versions of every affected paragraph: missing text, sentences added on one side, differences in meaning (not just wording). Compare the text with its scene map, Chapters and the Character Bible (including Continuity).
2. **Classify each difference**:
   - *Translation drift*: same meaning, different wording. Usually fine; fix only if meaning shifts.
   - *New content* on one side: translate it to the others.
   - *Changed fact* (a different person, place, date, event): do not choose silently. Ask the author which version is true, then update every version.
   - *Plan change*: the text now differs from Scenes, Chapters or the Character Bible. Propose the matching update upwards.
3. **Show a sync report**: per paragraph ID, the difference, its class and the proposed fix, plus the list of other files to update.
4. **Apply after approval**, in one pass, to every file affected. Respect the Concept's rules about whose wording is the source in each language.

## Plot soundness (always on)

While planning and writing, keep checking and flag at once:

- the timeline and ages (against the anchor dates in the Concept and the Bible's Continuity section);
- who knows what at each point, and who is alive;
- places, distances and travel times;
- set-ups that need a payoff, and payoffs without a set-up;
- contradictions between Concept, Chapters, Scenes, Book and Character Bible (including chapter titles and names);
- facts that move up a truth level without evidence.

For a full check of a chapter, use chapter-review.

## How to work with the author

- Start each session by loading the Concept, then say where the book stands: which chapters are planned, scene-mapped, drafted, reviewed or in the Book, and any open sync differences or contradictions.
- One step at a time; show the change before writing to Drive; never overwrite the author's or co-authors' text without approval.
- Every story line goes to the Chapters doc (see "Where story decisions go").
- Offer options with a recommendation when a creative choice is open, and record decisions in the right file.
- Never reproduce text from published books; reference authors live in the voice-generator skill and are imitated only through original writing.