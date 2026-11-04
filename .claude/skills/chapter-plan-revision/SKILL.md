---
name: "chapter-plan-revision"
description: "Use when revising a chapter plan in Chapters before scene-building: strengthen beats, arc, continuity, facts and readiness. Works on the plan, not on written prose."
---

# Chapter plan revision (before scenes)

Takes one chapter's entry in **Chapters** and makes it ready to become scenes: it brainstorms with the author where the chapter is thin, researches what must be accurate, organizes the entry, checks that the chapter fits the book and has no plot holes, and leaves it in the shape **scene-builder** needs. It works on the plan only: it never writes prose and never changes the manuscript (written chapters are reviewed with **chapter-prose-review**).

It is usually started by the author ("revise chapter 17"), by the **co-writer** when a chapter is planned, or by **scene-builder** when a chapter's readiness score is too low to build.

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask.
2. Read `BOOK.md` (files, standing rules, truth labels, people and roles) and the **Concept** in full (central pillars, how the book is told, handle-with-care notes).
3. Read the readiness rubric (`readiness.md` in the co-writer skill's folder).

## 1. Gather

Read, for the chapter:

- its full entry in **Chapters** (When / where, Readiness, Stories, Facts, Sources, Notes), and the entries of the **previous and next chapters**;
- every other place in Chapters that refers to this chapter ("ch. N", set-ups and payoffs, the arc brainstorm), and every place this chapter refers to;
- the **Character Bible** entries of everyone in it, and the **Continuity** record;
- the research files its sources point to;
- the chapter's voice (the book's Chapter Voices file) and the speech voices of its characters (see "Finding the voices of a scene" in book-voices);
- its scene map in **Scenes**, if one exists, and any written text.

## 2. Diagnose

Write a short diagnosis for the author (a table and a few lines), in five parts:

1. **Readiness**: the current score and each parameter (beats, arc, links, facts, decisions, voice), with what is missing for each.
2. **Plot holes and continuity**, checked one by one:
   - **Time and age**: dates, ages, seasons and durations agree with the neighbouring chapters, the Bible and the Continuity record; travel times and distances are possible for the period.
   - **Cause and effect**: every event has a cause in this chapter or an earlier one; nothing important happens only because the plot needs it (unless the book's theme is chance, and then the chance is visible).
   - **Who knows what**: no character acts on something they cannot know yet; secrets stay secret until they are revealed.
   - **Motivation**: each main character's choice follows from who they are in the Bible, or the change is shown.
   - **Set-ups and payoffs**: what this chapter plants is paid off later, and what it pays off was planted earlier, with cross-references both ways; flag set-ups that go nowhere and payoffs with no set-up.
   - **Contradictions** with other chapters, the Bible, the Concept or the research.
   - **Names and roles**: names as in the Bible; no new named character without the author's approval.
3. **Fit in the book**: what the chapter does that no other chapter does; which of the Concept's pillars it serves; its place in its part (pace, length against its neighbours, the book's balance); repeated beats or ideas that another chapter already carries.
4. **Facts**: real-world facts the chapter relies on, with their truth labels and sources; what is marked "to verify"; what is missing.
5. **Scene readiness**: what scene-builder will need and does not have yet (see section 6).

Rank the findings: what blocks scenes first, then what weakens the chapter, then polish.

## 3. Research (when needed)

For each fact that is missing, marked "to verify", or doubtful:

- search for sources (web search, the book's research folder, the shared library); prefer primary sources and serious secondary ones;
- record what is found in a research note in the book's research folder (in the language the book uses for research), with sources and truth labels, and what is still open;
- put the result into the chapter's **Facts**, linked to its **Sources**, with its truth label; keep "(to verify)" where the check failed;
- never upgrade a family tradition or a reconstruction into a fact, and never invent a source. When a site cannot be reached, say so and suggest another route.

Research only what the chapter needs; a fact that would only be decoration goes to the notes as an option.

## 4. Brainstorm with the author

Ask one round of 3-4 questions (multiple choice where possible, with AskUserQuestion when available), aimed at the weakest parameters and the holes found. Each question gives a **recommended** option first and real alternatives that change the story, not the wording; say what each costs or sets up. Typical questions:

- how a key moment unfolds (its beats), or which of two versions to keep;
- what a moment leaves in the point-of-view character (the arc);
- how to close a plot hole (several ways, each with its effect on other chapters);
- what to cut or move when the chapter carries too much (moving an event follows the co-writer's placement rule: propose event → chapter → position → why, and wait for confirmation);
- an open option in the notes that blocks the scenes.

Run more rounds while the author wants to; stop when the chapter scores 80 or the author is satisfied. Ideas are proposals until the author chooses; the author's own story lines go into Chapters with all their details.

## 5. Organize the entry

Rewrite the chapter's entry (shown first, applied after approval) so it reads cleanly and the Manuscript Desk can parse it:

- **When / where**, then the **Readiness** line (recalculated), then **Stories**, **Facts**, **Sources**, **Notes**, in that order (see the co-writer skill).
- A first item "**How the chapter runs**": the chapter's movements in order, in one or two sentences, and what the chapter is for.
- The events as **numbered items**, one moment per item (flat bullets, numbered like "**3.**" or "**3.2**", never nested), each with its key beats in order, who is there, and what the moment changes or leaves in the point-of-view character.
- Facts under **Facts** with truth labels and source links; sources numbered under **Sources**, with the research file when there is one.
- Open questions and options under **Notes**, each saying what it blocks.
- Decision tags kept short (for example "(decided <date>)"); no repeated explanations; cross-references both ways ("set-up for ch. 16"; "pays off ch. 9").

Then update, in the same change set: the **Character Bible** (short bullets with chapter pointers only), the neighbouring chapters' cross-references, the arc brainstorm if affected, the Concept if a central idea changed, and any scene map already built for the chapter.

## 6. Ready for scenes

Before closing, check that every key moment gives scene-builder what it needs:

- **When and where**, precise enough to stage (date or season, place, time of day when it matters).
- **Point of view**, and the **characters present**, written exactly as the Bible names them (their speech voices are found by these names).
- **The beats** in order, and the **turn**: what changes in the moment.
- **What the point-of-view character wants** in it, and **what it leaves** in them.
- **Set-ups and payoffs** it carries, with cross-references.
- **Facts** it brings in, sourced, and what must never be shown or said (handle-with-care, secrets).
- The chapter's **voice** chosen; speaking characters with a speech voice (their own or their group's), or flagged.
- Lines the author already hears, kept as written.

## 7. Close

1. Recalculate the **Readiness** line and show it before and after.
2. Show the author the changes (the reorganized entry, or the diff) and a short summary: holes found and how each was closed, research done (with sources), decisions made, what is still open.
3. After approval, hand the change set to the **book-repo** skill, which commits it; then say the Manuscript Desk's copy of the plan is out of date and offer to refresh it (steps in its README).
4. If the chapter now scores 80 or more, offer to run **scene-builder** on it.

## Rules

- The author decides; proposals are marked as proposals. Never apply a change to the book files before the author has seen it.
- Every story line the author gives goes into Chapters, in its chapter, with all its details; the Character Bible holds only short bullets.
- No new named characters, or expanded ones, without the author's approval.
- Follow the Concept's handle-with-care notes and the Shared Rules.
- Keep the plan lean: add what scenes need, cut repetition; a longer entry is not a better one.
