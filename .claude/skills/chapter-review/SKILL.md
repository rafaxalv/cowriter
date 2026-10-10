---
name: "chapter-review"
description: "Use when the author wants a whole chapter of a book in this repo reviewed: voices, paragraph-level tuning, plot and continuity, and coherence with the rest of the book, coordinating the paragraph-review skill."
---

# Chapter review

Reviews one chapter of a book as a whole. It checks the text against the chapter's scene map, decides which voice applies where and how each paragraph should be tuned, sends each paragraph to the **paragraph-review** skill with enough context, and checks the plot and the voice across the chapter and the rest of the book.

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask.
2. Read `BOOK.md`: file paths, languages, people and roles (for example a co-author whose wording is the source in one language), the Paragraph ID format, the Paragraph Parameters columns and the standing rules. Then read the Concept.

The process: Concept -> Chapters (events, sources) -> Scenes (scene maps, built by scene-builder) -> Manuscript (text). The reference files: the Character Bible (with its Continuity record), the Research and the Voices.

## Files used

This skill reads: the **Concept**, **Chapters**, **Scenes** (the chapter's scene map), the chapter text (the manuscript files, or the draft the co-writer names), the **Character Bible** (including its **Continuity** record), the research files the chapter cites, the **Voices** (Voice Index, Shared Rules, Bilingual Lexicon and the voice files) and **Paragraph Parameters**. It writes to the manuscript, Paragraph Parameters and the Continuity record, only after the author approves.

### Paragraph Parameters

One row per paragraph, with the columns the profile lists (typically: Paragraph ID, Chapter, Opening words per language, Voice ID, Voice version, Tuning, Reason for tuning, Review status, Last reviewed, Open issues).

- **Paragraph ID**: as the profile defines it (typically chapter.paragraph, for example 03.014). The same ID covers every language version of a paragraph. A paragraph inserted later gets a suffix (03.014a) so the other IDs do not shift. Renumber only when the author asks, and then in every file together.
- **Tuning**: the changes from the voice's base values for this paragraph only, for example "Violence +1; Pace +1". Must stay inside the voice's allowed ranges.

### Continuity record

What the manuscript has established: per character (ages stated, physical details, names used, what they know), and places, objects, dates, money and possessions, open threads (set up, not yet paid off), each with the Paragraph ID. Facts are added only after a chapter is approved.

## Steps

### 1. Gather context

Read: the Concept; this chapter's entry and sources in Chapters; its scene map in Scenes; the chapter text in every language; the previous chapter and the next one if it exists (at least a summary of each); the Continuity record; the relevant Character Bible entries; the Voice Index, Shared Rules, Bilingual Lexicon and every voice that might apply; this chapter's existing rows in Paragraph Parameters.

### 2. Map the chapter

Split the chapter into paragraphs with IDs (match existing IDs and rows by ID and opening words). Group them into **moments**, using the scene map's scenes (a scene, a letter, a frame passage, a time jump). Check the text against the scene map:

- every scene is present, in the planned order, with its beats; flag scenes missing, merged or moved;
- nothing in the text goes beyond the scene map (new events, named characters or facts); flag each one for the author to approve or cut;
- each scene is near its target length.

For each moment, decide which voice applies (the scene map names it), and point out:

- places where the voice should change (for example a letter inside the narration) and whether the transition is clear to the reader;
- places where the current voice does not fit and a different voice, or an adjustment to the voice, is needed. Voice changes are made with the **book-voices** skill, not here.

Then plan the **tuning curve**: for each paragraph, any tuning inside the voice's ranges that serves the moment (for example more explicit violence at the worst moment, faster pace in an escape, more sensory detail on arrival in a new place). Keep tuning purposeful and sparse; most paragraphs should stay at the base values. Show the map and the planned tuning to the author before going on.

### 3. Send each paragraph to paragraph-review

For each paragraph, give paragraph-review a **context packet**:

- the voice ID and version, and the tuning for this paragraph with its reason;
- the chapter's goal and the scene this paragraph belongs to, with the scene's beats, motivations, feelings and Reader feeling from the scene map;
- a summary of what happens just before and just after, plus the previous and next paragraphs in full;
- the characters present, what each one knows at this point, and where we are in the timeline;
- the Continuity facts that this paragraph touches;
- whose wording is the source in each language for this paragraph (from the profile).

### 4. Check the whole chapter

With all paragraph results in hand, check:

- **Plot and logic**: contradictions with the Continuity record or earlier chapters (dates, ages, distances, who knows what, who is alive), unexplained jumps in cause and effect, characters acting on information they do not have, set-ups with no payoff and payoffs with no set-up, gaps against the scene map, the chapter plan and its sources.
- **History and facts**: anything that conflicts with the sources listed for the chapter.
- **Rules**: the profile's standing rules and the Concept's handle-with-care notes (for example names never given, things never shown directly).
- **Voice coherence**: each voice stays consistent across the chapter and with how it sounds in other chapters (compare with the Paragraph Parameters rows and reference paragraphs); transitions between voices are clear; tuning does not drift so much that the voice becomes unrecognizable.
- **Languages**: every language file has the same paragraphs with the same IDs, and they say the same thing.
- **Rhythm of the chapter**: whether the pace, violence and emotion curves across the chapter serve the story (for example, no long stretch at the same intensity), and whether each scene lands its Reader feeling.

### 5. Feed back to paragraph-review

When the chapter check finds a problem located in specific paragraphs (a contradiction, a broken link with the paragraph before, a transition that does not work), send those paragraphs back to paragraph-review with the problem described and the updated context, and get revised suggestions. Repeat until the chapter holds together or the issue needs the author's decision.

### 6. Report

1. Overview: verdict for the chapter and the 3-5 most important issues.
2. Chapter map: moments, voices, tuning curve, and the comparison with the scene map.
3. Plot and continuity issues, each with the Paragraph IDs involved and a suggested fix.
4. Voice coherence findings.
5. Paragraph results (from paragraph-review), only for paragraphs that need changes.
6. Proposed new Continuity facts.

### 7. Apply (only after the author approves)

Apply the approved changes to the **manuscript** files and **Paragraph Parameters** in the same pass: every changed, added or removed paragraph gets its row created, updated or marked removed, with voice, version, tuning, reason, status and date. Never update one without the other. Then add the approved facts to the Continuity record. If approved changes alter what happens, update the scene map in Scenes and the Chapters entry too. Keep every language version aligned; if only one was changed, flag the others for update, following the profile on whose wording is the source in each language (when a co-author's text is the source, the other languages are updated to match it). Save the changes the way the profile says (by default: commit and push).

## Notes

- The author's voice and story choices come first; suggest, do not impose.
- Keep historical facts as the author wrote them; flag doubts separately.
- Low-reliability material (legends, hearsay) is allowed when it comes from a character, not from the narrator as fact.
