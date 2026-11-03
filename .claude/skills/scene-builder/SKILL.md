---
name: "scene-builder"
description: "Use when the author wants a chapter of a book in this repo broken into scenes: it turns the chapter's events from Chapters into an ordered scene map in Scenes, ready to be written as prose."
---

# Scene builder

Turns the events listed for one chapter in **Chapters** into a **scene map** in **Scenes**: the scenes in a logical order, each with everything a writer needs before writing prose. It is called by the **co-writer** (or directly by the author). It never writes prose and never changes the manuscript.

The process: **Concept** -> **Chapters** -> **Scenes** (this skill) -> **Manuscript** (written by the co-writer with the voices). The reference files used at every level: the **Character Bible** (with its Continuity record), the **Research** and the **Voices**.

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask.
2. Read `BOOK.md`: it maps the file roles used below to paths, and gives the standing rules (for example working names, names never used in the text) and the truth labels.

## 1. Gather context

Read, for the chapter:

- the **Concept** (how it is told, handle-with-care notes, chapter shape, key ideas) and the length target in the profile;
- the chapter's full entry in **Chapters**, including sources and open items, and the entries of the previous and next chapters;
- the **Character Bible** entries of everyone who appears, and its **Continuity** record;
- the research files the chapter's sources point to, when a scene needs more historical or factual detail;
- the **Voice Index** (via book-voices) to know which voices exist, and the **voice file** of the voice chosen for the chapter: its scores on narrative technique (19-26) and scene architecture (27-31), and its narrative technique and scene architecture rules;
- the scene maps of the previous and next chapters in **Scenes**, if they exist.

### 1a. Readiness check (before building)

Read the chapter's **Readiness** line (computed with the co-writer's `readiness.md`; recalculate it first if it is missing or older than the chapter's last change).

- **80 or more**: build.
- **60-79**: before building, ask the author one short round of questions (3-4, multiple choice where possible) on the two weakest parameters, for example the beats of a key moment, what it leaves in the point-of-view character, an open option. Write the answers into Chapters (after approval), recalculate the score, then build.
- **Below 60**: do not build. Say what is missing, parameter by parameter, and offer to run **chapter-revision** on the chapter.
- If the voice parameter is low because the chapter's voice has no scene architecture scores (27-31), offer to complete them with **voice-generator** first; if the author prefers to go on, build with the defaults below and mark the map "voice profile incomplete".

Never fill a gap by inventing story: a gap becomes a question, or a **[proposal]**.

If Scenes does not exist yet, create it at the path the profile gives (after asking) with the header below.

Before changing a scene map that already exists, re-read it: the author may have edited it directly. Keep the author's wording, add to it rather than overwrite it, and carry any new story detail they wrote into Chapters.

## 2. Build the scenes

0. **Read the voice's scene shape.** Before grouping events, turn the voice's scores into concrete decisions for this chapter and write them in the map's header ("Voice shape"):
   - **27 Scene length** sets how many scenes the chapter's budget is cut into (low: many short scenes; high: few long ones).
   - **19 Event entry** and **28 Scene opening** set where each scene starts (with setup and orientation, or late, on an action or a line).
   - **20 Event exit** and **29 Scene ending** set where each scene stops (carried into the aftermath, or cut at or before the peak, on an image or a line).
   - **21 Peak treatment** and **22 Action granularity** decide which moments are slowed down beat by beat and which are compressed or told after the fact.
   - **30 Transitions** and **10 Chronology** decide how scenes are joined (summary bridges, or hard cuts and jumps, flashbacks).
   - **31 Scene focus** and **9 Scene vs summary** decide whether texture events get their own scenes or are braided into others, and what is told as summary between scenes.
   - **23-26** (feelings, interior access, inference, subtext) set what each scene leaves unsaid, recorded per scene below.
   The voice's scene architecture rules override these defaults where they are more specific. When the voice has no scores for 27-31, use 3 (balanced) and say so.
1. **List every event** in the chapter's Chapters entry. Each event must land in at least one scene; one scene can carry several events.
2. **Group and order.** Turn events into scenes (a continuous moment in one place and time). Order them so cause leads to effect and the chapter follows the Concept's chapter shape (for example hook, texture, turn, cliffhanger). Daily-life or texture events can be woven into other scenes instead of standing alone. Prefer scenes driven by action (something happens, someone wants something) over summary or description.
3. **Find the gaps.** Where the Chapters entry jumps (in time, place or logic), add a bridge scene or passage, marked **[proposal]**.
4. **Fill the fields** for each scene:
   - **When** (date or period; ages of the main characters);
   - **Where** (place, and what kind of place);
   - **Point of view**;
   - **Characters** (named characters from the Bible, written exactly as the Bible names them, because the speech voices are looked up by these names; unnamed extras described by role); for each character who speaks, their speech voice ID and the chapter's setting from it (see "Finding the voices of a scene" in book-voices), or "no speech voice yet";
   - **What happens** (the beats, in order);
   - **Motivations** (what each character wants in the scene);
   - **Feelings** (what each character feels, and what they hide);
   - **Reader feeling** (the emotion the reader should feel, which may differ from what the characters feel or understand, for example disgust while the character is only tired and confused; and the concrete sensory details that will create it: smells, textures, sounds, bodies, dirt, light). Name one main feeling and, if needed, how it shifts through the scene (for example warmth, then shock, then a tender ache);
   - **Place details** (senses: sounds, smells, light, objects);
   - **History carried** (the real fact or piece of the world the scene brings in, how it enters without explanation, with a source or truth label);
   - **Forces or themes touched** (from the Concept);
   - **Function** in the chapter (hook, texture, turn, set-up, payoff, cliffhanger) and set-ups or payoffs it serves elsewhere;
   - **Voice** (which voice from the Voice Index, or "to define") and **voice shape**: one line on how the voice shapes this scene (where it opens and cuts, what is slowed down, what stays off the page or unsaid);
   - **Open items**;
   - **Scene shape** (the scene-level decisions; the voice's scene architecture gives the defaults, the scene decides): **Opening**: orientation first, or in the action, and on what (a gesture, a line of dialogue, an image, an object); **Ending**: resolved, or cut, and on what (an image, a line, an unanswered question); **Into the next scene**: summary bridge, hard cut, or jump in time or place (for the chapter's last scene: how the chapter ends); **Length**: the target in words. When a choice departs from the voice's default (28 Scene opening, 29 Scene ending, 30 Transitions, 27 Scene length, 31 Scene focus), say why in a few words, as a chapter's tuning gives a reason: for example "cuts on the boy's eyes although the voice usually carries events into their aftermath: the memory he never tells".
5. **Shape curve.** Read the Scene shape of all scenes in order, next to the voice's defaults: the pattern of lengths, openings, endings and joins should read as this voice across the chapter, with departures where the moment needs them and few enough that the habit stays visible. Flag runs that break the voice without a reason.
6. **Feeling curve.** Read the Reader feeling of all scenes in order and check the chapter's emotional curve: avoid several scenes in a row with the same feeling, and make sure the chapter's last scene lands its feeling (relief, dread, a hook).
7. **Budget.** Give the chapter a target length from the profile's length target and the number of chapters; share it across scenes, and say which scenes to trim first.

## 3. Rules

- Nothing appears in a scene that is not in Chapters or in the Bible, unless marked **[proposal]**.
- **No new named characters** without the author's approval; unnamed extras are allowed and described by role.
- Follow the Concept's handle-with-care notes (for example what is never shown directly). A strong Reader feeling (disgust, horror) is created through senses and what is implied, never by showing sexual violence directly.
- Facts that must be accurate carry a source or a truth label (from the profile), and "to verify" when unsure. Never upgrade a tradition or a reconstruction into a fact.
- Check names against the Bible (for example a working name used by two characters) and dates and ages against the Continuity record, and flag clashes.

## 4. Output

Write the scene map into **Scenes** under a heading "Chapter N — Title (scene map, draft X, date)", with:

- a short header: source in Chapters, the chapter's Readiness score at the time of building, voice plan and **voice shape** (step 0), target length, chapter shape, throughline, dates used;
- one section per scene with the fields above;
- a **Checks** list at the end: every Chapters event and where it is covered; the feeling curve (one line per scene with its Reader feeling); the shape curve (one line per scene: opening → ending → join, length, and any departure from the voice with its reason); proposals to approve; clashes and open items; sources to add; total length.

Show the author a short summary (a table of scenes with their Reader feeling and scene shape) and the decisions needed. Do not mark the map ready until the author has answered them.

## 5. After approval

- Write every approved proposal and decision back into the chapter's entry in **Chapters** (bridges, choices between options, new details), so Chapters stays the record of events.
- Update the scene map to remove the [proposal] marks for what was approved, and note the date.
- Hand the changes to the **book-repo** skill, which saves them.
- Hand the map to the **co-writer** for the prose. The prose must aim at each scene's Reader feeling.

## Scenes header (first time only)

"The scene maps of the book: the step between Chapters and the manuscript. For each chapter, the events in Chapters are expanded into ordered scenes with everything a writer needs. The co-writer then writes each scene map as prose in the manuscript. Process: Concept -> Chapters -> Scenes -> Manuscript; the Character Bible, the research and the Voices are used at every level. Every scene carries a Reader feeling field: the emotion the reader should feel and the sensory details that create it."
