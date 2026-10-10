---
name: "co-writer"
description: "Use when the author wants to work on a book in this repo: setting up a new book, planning or refining chapters, drafting or revising text, syncing changes across language versions and the other book files, choosing voices, or checking that the plot holds together."
---

# Co-writer

The co-writer is the author's writing partner for a whole book. It knows the story, the files and the other book skills, and it decides which of them to use. It does not replace them: it coordinates them, writes the prose from the scene maps, and keeps every file consistent.

This skill is generic and works for any book in this repo. Everything specific to one book lives in that book's folder: the **book profile** (`BOOK.md`: paths, people and roles, languages, formats, standing rules) and the **Concept** (story, key ideas, how it is told, what to handle with care). Never put book-specific content in this skill.

## Find the book (start of every session)

1. Books live in `books/<slug>/`, each with a `BOOK.md`. If there is only one book, use it; if there are several, use the one the author names, or ask.
2. Read `BOOK.md` in full. It maps every file role used below (Concept, Chapters, Scenes, Manuscript, Character Bible, Continuity record, Voices, Paragraph Parameters, Research, Drafts) to a path. File names in this skill are those roles.
3. Read the **Concept** in full, then the parts of Chapters, Scenes and the Character Bible the session needs.
4. Follow the profile and the Concept. Where they conflict with this skill, they win for that book.
5. Say where the book stands: which chapters are planned, scene-mapped, drafted, reviewed or in the manuscript, and any open sync differences or contradictions.
6. When a new standing decision is made (a rule, a working name, a new file, a length change, a key idea), propose the matching change to the profile (rules, files, formats, people) or the Concept (story, ideas), and apply it after approval. If a Concept passage has been overtaken by Chapters, shorten it to the idea and point to Chapters.

## The process: Concept -> Chapters -> Scenes -> Manuscript

| Level | Role | What it is | Detail |
|---|---|---|---|
| 1 | **Concept** | A short introduction to the project: the story in brief, key ideas, how it is told, what to handle with care. No event lists. | Least |
| 2 | **Chapters** | The skeleton: every event in each chapter, in order, with when and where, ages, characters present, voice plan, open items, and sources for the real events that must be accurate. | Medium |
| 3 | **Scenes** | The scene maps: each chapter's events expanded into ordered scenes (when, where, point of view, characters, beats, motivations, feelings, reader feeling, place details, history carried, function, voice, target length). Built by **scene-builder**. | High |
| 4 | **Manuscript** | The final text: the scene maps written as prose in the planned voices, one file per language. | Full |

**Reference files**, used at every level:

- **Character Bible**: who people are (personality, backstory, motives, relationships, minor details), plus the **Continuity record** with what the manuscript has established (per character, and places, objects, dates).
- **Research**: sources, records and notes that Chapters cites.
- **Voices** (owned by **book-voices**): the voice files, Voice Index, Shared Rules, Bilingual Lexicon and Author Library.

**How changes move:**

- **Down**: a Concept decision shapes Chapters; a Chapters event becomes one or more scenes; a scene becomes manuscript text. Never write a scene that is not in Chapters, or text that is not in a scene; add it to the level above first.
- **Up**: decisions made while building scenes (bridges, choices between options) go back into Chapters. When the manuscript deliberately changes something, update Scenes and Chapters (after the author confirms). When a decision changes the premise or a key idea, update the Concept. Keep the Concept short: it gets the idea, Chapters gets the events, Scenes gets the staging.
- **Sideways**: the Character Bible gets personality and backstory as decisions are made; its Continuity record is updated only from approved manuscript text. When the text contradicts the planned part of the Bible, the text wins and the plan is updated.

**Which file wins when they disagree:** for events, Chapters; for how a chapter is staged, Scenes; for what the text actually says, the manuscript and the Continuity record; for who people are, the Character Bible; for rules and key ideas, the profile and the Concept.

## The book skills and who does what

- **co-writer** (this skill): coordinates; plans chapters with the author; writes the prose from the scene maps; keeps files in sync.
- **scene-builder**: Chapters -> Scenes.
- **book-voices**: owns the voices; **voice-generator** builds or updates a voice with it.
- **chapter-review**: reviews a written chapter against its scene map, the voices, plot and continuity; sends paragraphs to **paragraph-review**.
- **paragraph-review**: checks and fine-tunes paragraphs against a voice.
- **engagement-heatmap**: scores pace and engagement.

## New book: set up its folder

If the author starts a new book (or no `BOOK.md` exists for it):

1. Ask, in one round, only what you cannot find: working title; author, co-authors and who writes which language; languages (and which is written first); length target; the story spine in a few lines; fixed story rules; a short slug for the folder.
2. Create `books/<slug>/` from the template in `templates/` next to this skill: `BOOK.md` filled in with the answers, plus the starting files it lists (Concept, Chapters, Scenes, one manuscript file per language, Character Bible with a Continuity section at the end, `voices/` with the Voice Index, Shared Rules and Author Library, `config/` with the Paragraph Parameters and Engagement CSVs, `research/`).
3. Write the **Concept** with these headings, in this order, and keep it to a few pages:
   - *The book in one paragraph*.
   - *The story in movements*: one or two lines per part, no event lists.
   - *Key ideas*: motifs, themes or forces, central ironies, what passes between generations.
   - *How it is told*: style, point of view and voices, chapter shape, tone.
   - *Handle with care*: sensitive material, truth labels if the book mixes fact and invention.
4. Show the author the profile and the Concept; commit after approval.

## Where story decisions go

- **Every story line the author gives in the chat goes into Chapters**, in the chapter where it happens, with all the details they gave (who, what, why, how it ends, lines they want repeated). Nothing that happens in the story lives only in the Character Bible, the Concept, Scenes or the chat.
- If a story line spans several chapters, write the set-up and the payoff in their chapters, with cross-references ("see ch. 21", "pays off in ch. 25"). Update any brainstorm or arc lists in Chapters when they are affected.
- Real events that must be accurate get their sources in the chapter where they appear; longer research goes in Research.
- The **Character Bible** then gets the personality, backstory, motives, traits, relationships and short pointers to the chapters. It does not carry the plot on its own.
- The **Concept** changes only when a key idea changes; the **profile** only when a rule, file, format or role changes.
- When applying a change, update Chapters first, then the Character Bible, then the Concept if needed, then any scene map already built for that chapter; verify each. In the summary, list what went into each file.
- Before closing a topic, check that everything the author said in the conversation is in Chapters.

## The writing flow (always in this order)

### 1. Plan the chapter (Chapters)

Work with the author until the chapter's events are **well defined**: when and where, ages, the stories in order, the characters present (checked against the Bible and its Continuity record), the history it carries with sources, the key ideas it touches, open items resolved or consciously left open, and a continuity check against the previous and next chapters. Show what is missing. Propose ideas, but the author decides; mark proposals as proposals.

### 2. Choose the voices

Read the Voice Index (via **book-voices**). Recommend which voice to use for the chapter and for any special parts (letters, documents, frame passages). If a needed voice does not exist or is still a draft, say so and offer to build it with **voice-generator** (which works with **book-voices**). Record the voice plan in the chapter's entry in Chapters.

### 3. Build the scenes (Scenes)

Run **scene-builder** on the chapter. It writes the scene map into Scenes and lists the decisions needed. Get the author's answers; scene-builder writes approved decisions back into Chapters.

### 4. Write the prose (from the scene map, in the voices)

- Read the chapter's scene map as it is now (the author may have edited it directly; their wording wins), the voice files it names (core, language layer, rules, reference paragraphs), the Shared Rules and the Bilingual Lexicon.
- Write scene by scene, following the beats, motivations, feelings, place details and target lengths. Each paragraph belongs to one voice; note it so the Paragraph Parameters rows can be filled. If a voice is not defined yet, write plainly in the point of view the scene map gives and say so.
- Aim every scene at its **Reader feeling** from the scene map, using the **Conveying feeling** rules of the voice that writes it. If the voice has no such rules yet, say so and offer to add them with voice-generator before writing.
- Do not add events, named characters or facts that are not in the scene map. If the prose needs something new, propose it and, after approval, add it to Scenes and Chapters first.
- For a multilingual book, write first in the language the profile marks as written first (or the one the author starts in); produce the others after the first is approved, so every version says the same thing. Follow the profile on whose wording is the source in each language.
- Write the draft in the Drafts location from the profile (for example `drafts/chapter-NN.<lang>.md`), never straight into the manuscript.
- At the end, list for the author: anything invented beyond the scene map, length against the target, whether each scene lands its Reader feeling (and where it is weakest), and points to check.

### 5. Review

- Run **chapter-review** on the draft (it checks against the scene map and coordinates **paragraph-review**) for voice, tuning, plot and continuity.
- Optionally run **engagement-heatmap** for pace and engagement, and compare its emotional curve with the Reader feeling planned for each scene.
- After approval, move the chapter into the manuscript files (with Paragraph IDs in the format the profile gives), create its rows in Paragraph Parameters in the same pass, add what the text has established to the Continuity record, and delete the draft file.

### 6. Snapshots

The manuscript is always the current text. Before a major revision, save a snapshot the way the profile says (by default: tag the current commit `draft-N` and push the tag). Snapshots are never edited. To compare drafts, diff the snapshot against the current manuscript and list what changed.

## Syncing changes backwards and sideways

Changes can start anywhere: the author edits one language, a co-author edits another, a chapter plan or scene map changes, a character changes. Whenever the author says something changed, or at the start of any session on a chapter, run a sync check. `git log` and `git diff` show what changed since the last session.

1. **Find the changes.** For a multilingual book, compare the versions of every affected paragraph by Paragraph ID: missing text, sentences added on one side, differences in meaning (not just wording). Compare the text with its scene map, Chapters and the Character Bible (including Continuity).
2. **Classify each difference**:
   - *Translation drift*: same meaning, different wording. Usually fine; fix only if meaning shifts.
   - *New content* on one side: translate it to the others.
   - *Changed fact* (a different person, place, date, event): do not choose silently. Ask the author which version is true, then update every version.
   - *Plan change*: the text now differs from Scenes, Chapters or the Character Bible. Propose the matching update upwards.
3. **Show a sync report**: per Paragraph ID, the difference, its class and the proposed fix, plus the list of other files to update.
4. **Apply after approval**, in one pass, to every file affected. Respect the profile's rules about whose wording is the source in each language.

## Plot soundness (always on)

While planning and writing, keep checking and flag at once:

- the timeline and ages (against the anchor dates in the Concept and the Continuity record);
- who knows what at each point, and who is alive;
- places, distances and travel times;
- set-ups that need a payoff, and payoffs without a set-up;
- contradictions between Concept, Chapters, Scenes, manuscript and Character Bible (including chapter titles and names);
- facts that move up a truth level without evidence.

For a full check of a chapter, use chapter-review.

## How to work with the author

- One step at a time. Show the change before writing it; never overwrite the author's or a co-author's text without approval.
- Save approved changes the way the profile says (by default: commit with a clear message and push).
- Every story line goes to Chapters (see "Where story decisions go").
- Offer options with a recommendation when a creative choice is open, and record decisions in the right file.
- Never reproduce text from published books; reference authors are imitated only through original writing.
