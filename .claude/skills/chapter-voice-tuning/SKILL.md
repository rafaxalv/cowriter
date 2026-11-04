---
name: "chapter-voice-tuning"
description: "Use when the author wants to fine-tune the narrative voice of one chapter of a book in this repo: reads the Concept and the chapter's plan, proposes changes to the voice's 31 parameters for that chapter, and settles them through a round of questions; records them in Chapter Voices."
---

# Chapter voice tuning

Sets a chapter's **tuning**: the few changes to its narrator voice's 31 parameters that make that voice right for this chapter (for example a war chapter that runs faster and closer to the violence, or a chapter of waiting where time blurs). The voice itself stays the same; only this chapter moves, inside the voice's allowed ranges. The skill reads the Concept and the chapter, proposes a tuning, settles it with the author through a round of questions, and records it in the book's **Chapter Voices** file.

The tuning is used at both levels: **scene-builder** applies it to the voice's narrative technique and scene architecture (19-31) when it decides each scene's shape, and the **co-writer** and the review skills apply all of it to the prose. So the best moment to tune a chapter is after its plan is ready (chapter-plan-revision) and before its scenes are built.

It tunes the **narration** only. How characters speak in dialogue is the character-voice skill; creating or changing a voice itself (its base values, ranges, rules) is voice-generator and book-voices. It never writes into the manuscript.

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask. If the author has not named the chapter, ask which one.
2. Read `BOOK.md` (files, standing rules, voices decisions) and the **Concept** in full: the central pillars, how the book is told, and the handle-with-care notes. The pillars say what every chapter's voice must carry; the handle-with-care notes set limits no tuning may cross.

## 1. Gather

Read, for the chapter:

- its entry in **Chapters** (How the chapter runs, the events and their beats, what each moment leaves in the point-of-view character), the part notes above it (for example how a whole part is told), and the previous and next chapters' entries, briefly;
- its scene map in **Scenes** and any written text (drafts or manuscript), if they exist;
- its row in **Chapter Voices** (voice, current tuning, reason), and the rows of the chapters around it;
- the voice file: the 31 dimensions with base values and **allowed ranges**, the voice rules, conveying-feeling, narrative technique and scene architecture rules (the dimensions and their 1 and 5 ends are in voice-generator's framework).

## 2. A reading of the chapter

Write the author a short reading (6-10 lines): what the chapter is for in the book and which pillars it serves; its emotional weather (dread, tenderness, numbness, triumph, comedy); its key moments and what each asks of the prose (violence, intimacy, a long time span, waiting, a crowd, a letter); its pace and time span; whose point of view; and how it should feel against its neighbours (a breath after a battle, a fall after a rise).

Then a **proposed tuning** as a table: dimension, base, allowed range, proposed change, why (tied to a moment of the chapter or a line of the Concept). Rules for the proposal:

- **Few changes**: usually 2-5, each with a reason. Most chapters move little; a chapter that needs more than 6 or 7 changes may need another voice (say so and offer book-voices).
- **Inside the ranges.** A change beyond a range is proposed only as a marked exception, with the choice to keep it as a deliberate exception or to widen the range through book-voices.
- **Fixed points**: dimensions that the Concept or the voice holds still (for example "no verdicts", or how sexual violence is handled) are listed as not tunable for this chapter, with the reason.
- **Whole-chapter settings**: tuning applies to the whole chapter; a single moment is shaped by the writing within those settings (and by the scene map's Scene shape), not by its own tuning.

## 3. Round of questions

Ask one round of 3-4 questions (multiple choice; with AskUserQuestion when it is available). Each question is about **how the chapter should feel to read**, not about numbers: the options are translated into parameter changes, shown briefly with each option ("Violence +1, Peak treatment +1"). The **recommended** option comes first, marked "(Recommended)"; the alternatives lead to really different chapters. Where it helps, give each option a one-line original sample set in the chapter, so the author hears the difference. Choose the questions from what the chapter most depends on, usually in this order:

1. **The central moment**: how close the reader is to it, and how slowly it is told (distance, interior access, violence rendering, peak treatment, action granularity, feeling rendering).
2. **Time and pace**: how time moves through the chapter (scene vs summary, pace, chronology; for example time that blurs, or a single night told minute by minute).
3. **Temperature and inference**: how much is felt openly and how much is left unsaid (emotional temperature, reader inference, dialogue subtext, figurative density, sensory detail).
4. **Shape**: how the chapter is cut (scene length, openings and endings, transitions, scene focus), when the scene map does not already settle it.

Also offer, where it fits, **"keep the base"** for a dimension: no tuning is often right. If the answers open new questions, ask one more short round; stop when the author is satisfied.

## 4. Check

Before recording, check the tuning:

- every change inside the voice's range (or a recorded exception);
- consistent with the voice's rules and conveying-feeling rules, and with the Concept's handle-with-care notes;
- against the neighbouring chapters: contrasts are deliberate (a breath after a battle), not accidental jolts;
- the changed dimensions agree with each other (for example "cut at the peak" with "peak slowed, beat by beat" needs a reason).

Optionally, write one short sample paragraph from a key moment of the chapter, in the voice at its base and then with the tuning, in the book's first language, so the author can hear it. Samples are never put into the manuscript.

## 5. Record and hand over

1. Show the author the new row for **Chapter Voices**: Chapter, Voice ID, **Tuning** written as dimension names with offsets from the base, separated by semicolons, using the framework's names (for example `Pace +1; Violence rendering +1; Scene vs summary -1`), and **Reason for tuning** in one sentence.
2. If the chapter's voice changes, or a range was widened, say what follows (book-voices for the voice file; recalculate the chapter's Readiness line if the voice parameter changes).
3. After approval, hand the change to the **book-repo** skill, which commits it. Then say that the Manuscript Desk's copy is out of date and offer to refresh it (its README: the chapter's `chapterVoice` document and context).
4. If the chapter already has written text, offer to rewrite it to the new tuning with **paragraph-review** (its hand-tuning, chapter by chapter); if it has a scene map, note any scene whose Scene shape now clashes with the tuning.

## Rules

- The author decides; proposals are marked as proposals. Never change Chapter Voices before the author has approved.
- Tuning is per chapter, never per paragraph or scene.
- Keep it sparse: a tuning is a few purposeful changes with reasons, not a new voice.
- Never tune away from the Concept's handle-with-care notes or the Shared Rules.
