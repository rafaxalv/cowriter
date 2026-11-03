---
name: "character-voice"
description: "Use when the author wants to create, update or review how a character of a book in this repo speaks in dialogue: fluency, sentence building, figures of speech, recurring words and manners, set per chapter as the character changes; built from the character's story, Character Bible entry and the Concept, through a round of questions."
---

# Character voice (how a character speaks)

Builds and maintains a **speech voice** for one character: how they talk whenever they speak in dialogue (and, unless the author says otherwise, in their quoted thoughts). It sets their fluency in the language, how complex their sentences are, the figures of speech they reach for, the words, forms of address and manners that keep coming back, and what they never say. A speech voice can change over the book, so it holds a **base** and a **setting per chapter**.

It works in exchange with **book-voices**, which owns the voices folder and saves the file, and it is read by the **co-writer** and **scene-builder** (when dialogue is planned and written) and by **chapter-review** and **paragraph-review** (when dialogue is checked). It never writes prose and never changes the manuscript.

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask.
2. Read `BOOK.md`: voices folder, voice ID convention, languages, people and roles, standing rules (for example working names that never appear in the text), truth labels.
3. Read the **Concept** in full: the central ideas, how the book is told, and the handle-with-care notes.

## 0. Generic voices for groups

When the author asks for voices for the many characters who do not need one of their own, build **base speech voices** (`BASE-SPEECH-<GROUP>`), one per group that shares a background (for example enslaved and freed people of one region, the landed class, soldiers, a foreign people, immigrants, people speaking a learned language). Each holds the same sections as a character speech voice, with typical scores for the group, and a **Variants** section with one line per listed character (what sets them apart) instead of settings per chapter. List every character it covers in the Voice Index's **Whose voice** (Type "Base speech"), so a character without their own voice is found through it. When a character later gets their own speech voice, start from their group's base voice and remove them from its list.

## 1. Gather the character

Read, for the character the author names:

- their **Character Bible** entry (who they are, origin, first language, literacy, class and status, relationships, arc) and the **Continuity** record (what the text has already established about how they speak);
- every chapter in **Chapters** where they appear or speak, in order, noting where their life changes (a move, freedom, money, a loss, ageing, learning to read, a new language), because that is where their speech may change;
- the **Voice Index**, the **Shared Rules**, the **Bilingual Lexicon** and any voice the character already has (letters, testimony): the speech voice must stay consistent with them, and clearly different from the other characters they talk to most;
- the research files on their language, region, period or trade, when the chapters cite them;
- any dialogue already written for them in the manuscript or scene maps.

Then write a short **portrait of their speech** for the author (8-12 lines): what their background makes likely (first language, schooling, region, trade, faith, status), how they change across the book, and the two or three things that should make them recognisable in one line of dialogue. Mark what comes from the Bible or Chapters and what is your inference.

## 2. Round of questions

Ask the author one round of 3-4 questions (multiple choice where possible; with AskUserQuestion when it is available), before writing anything. Each question gives a **recommended** option first (marked "(Recommended)") and real **alternatives** that lead to different characters, not different wordings. Cover, in this order of importance:

1. **How distinct** the character should sound: blending into the narration's register, clearly recognisable, or **very distinct** (a voice the reader could pick out with no speech tag). Ask this first: if the author chooses very distinct, the alternatives in the next questions move further toward the extremes (much less fluent or much more ornate, a strong verbal tic, a habit of speaking only in proverbs or questions), and say so.
2. **Fluency and language**: first language, how well they speak the book's languages, whether and when they slip into another language, and, for a learner, **how broken their speech is** and which kinds of mistakes they make (from their first language), with sample lines for each option; how this is carried on the page in each language of the book (see "Handle with care").
3. **Figures of speech and recurring words**: where their images come from (faith, the land, a trade, the sea, the war, the church, the market), signature words and phrases, forms of address they use and expect.
4. **Change over time**: which chapters change how they speak and how (for example more fluent after years in a new country, harder and shorter after a loss, more formal once rich), or whether their speech stays fixed while the world around them changes.

If the answers open new questions (a second language, a secret they never speak of), ask one more short round. Never fill a gap by inventing a fact about the character's past; a gap is a question, or a **[proposal]** marked as such.

## 3. The speech profile

Score the **base** on these twelve dimensions (1-5, with a one-line reason each, from the Bible, the chapters and the author's answers):

| # | Dimension | 1 | 5 |
|---|---|---|---|
| S1 | Fluency in the language of the scene | broken: frequent errors, missing words, first-language word order | effortless, idiomatic |
| S2 | Sentence complexity | single clauses, fragments | long sentences with subordinate clauses |
| S3 | Register | plain, rough, slang | formal, elevated, learned |
| S4 | Figurative speech | literal | proverbs, images and sayings in most lines |
| S5 | Turn length | a word or two | speeches |
| S6 | Directness | hints, evades, talks around | says exactly what they mean |
| S7 | Emotional display | guarded, flat | open, loud |
| S8 | Code-switching | never leaves the scene's language | often uses words or phrases from another language |
| S9 | Regional and period marking | neutral | strongly marked by region, class or period |
| S10 | Humour and irony | none | constant jokes, teasing or irony |
| S11 | Deference | blunt, commanding | deferential, careful, formal address |
| S12 | Conversational control | follows, answers | leads, interrupts, changes the subject |

Allowed ranges are not needed: a character's speech varies by chapter (section 4), and within a scene the writing follows the moment.

Then the **key ideas** (bullet points, each short and checkable on one line of dialogue):

- **What makes them recognisable** (2-4 bullets): the habits that should show in almost every speech.
- **Figures of speech**: where their images come from, with two or three original sample phrases.
- **Signature words and phrases** (and in which language): words they repeat, a saying they come back to, a way of swearing or praying; how often (rationed: a signature line that appears in every scene stops working).
- **Forms of address**: what they call others, what they want to be called, and how that changes with status.
- **Manners and tics**: physical or verbal habits that go with speech (a pause before answering, answering a question with a question, laughing at their own jokes).
- **Never says**: words, subjects or tones that are outside this character (their own name, a word they would not know, a feeling they never name).
- **Under pressure**: how their speech changes when angry, afraid, grieving or lying.

For a learner, add **Typical mistakes**: the 3-6 kinds of error they make (from their first language), with an original example of each, and which ones fade first as they learn.

And one **language layer per language of the book**: how the fluency (including a learner's mistakes, which differ by language), the code-switching and the regional marking are carried in that language (syntax, word order, word choice, untranslated words and how context makes them clear), with two or three short original sample lines. The character's level is the same in every language; only the means differ. Words they keep in their first language go to the **Bilingual Lexicon** (through book-voices).

## 4. Settings per chapter

A table with one row per chapter where the character speaks:

| Chapter | Changes from the base | Why (what happened to them) | Notes for the writer |
|---|---|---|---|
| 3 | S1 +1, S7 -1 | ... | ... |

- Write only the dimensions that change, as offsets from the base (for example "S1 +1"), and any key idea that appears, disappears or changes in that chapter (a new form of address, a phrase dropped).
- Changes follow the character's life in Chapters; each has a reason. Keep them few and gradual unless an event breaks the character (then say so).
- A chapter with no row uses the base, or the last row before it if the author chose "changes persist" (ask which, once, and record it).

## 5. Handle with care

- **Learners speak like learners.** A character who is learning the language of the scene can speak broken English or broken Portuguese: wrong genders and tenses, missing articles, word order from their first language, words borrowed or invented when the right one is missing, simple sentences when they would like to say more. Model the mistakes on the character's **first language** (the errors a Spanish or Galician speaker makes in Portuguese are not those of a Yoruba speaker), keep them **consistent** from scene to scene, and let them **change with the chapters** as the character learns (section 4). Their errors are in the grammar, never in their intelligence: what they mean stays sharp, and they can be the cleverest person in the room.
- **No caricature.** Broken speech, a regional accent or a second language is never played as a joke at the character's expense, and never built from the stock "dialect" of old fiction that mocked enslaved, colonised, migrant or working-class people. Prefer syntax, word choice and rhythm to spelling: phonetic misspelling (eye dialect) is used only if the author chooses it, lightly, for one or two marked words, and the same way for every character who would say them. Limited schooling never makes a character less intelligent on the page.
- **Period and place.** Check plausibility: words, forms of address, slurs and titles of the period and region. A slur or period term that a character would use is written only where the book's standing rules allow it, and never by the narration; flag it to the author.
- **Consistency.** The speech voice must agree with the character's other voices (letters, testimony: same person, different form) and with the Continuity record; when the text already contradicts the plan, the text wins and the plan is updated (after the author confirms).
- Follow the Concept's handle-with-care notes and the Shared Rules.

## 6. The file and the hand-over

The file is named by the voice ID from the profile's convention, with the form **SPEECH** (for example `CHAR-<NAME>-SPEECH.md`). Use these exact section headings, because the other skills and the Manuscript Desk read them: `## Who and when`, `## Portrait`, `## Author's choices`, `## Speech profile`, `## Key ideas`, `## Typical mistakes` (learners only), `## Language layer: <CODE>` (one per language), `## Settings per chapter`, `## Neighbour voices`, `## Open decisions`, `## Change log`. In order:

1. ID, name, type ("Character speech"), version, status, date; whose voice (link to the Character Bible entry) and when it is used (all their dialogue, or named chapters).
2. The portrait of their speech (section 1), with sources.
3. The author's choices (the answers, briefly), including how distinct.
4. The speech profile: base scores with reasons (section 3).
5. Key ideas (section 3).
6. Language layers (section 3).
7. Settings per chapter (section 4), and whether changes persist.
8. Neighbour voices: the characters they talk to most, and how they stay different from each.
9. Open decisions; change log.

Hand the finished file to **book-voices**, which checks it (ID, neighbours, Shared Rules, Lexicon entries), adds it to the Voice Index (Type "Character speech"; **Whose voice** = the character's name exactly as the Character Bible and the scene maps write it, plus aliases separated by " / "), and saves it after the author approves. book-voices hands the change to the **book-repo** skill, which commits it.

## 7. How the other skills use it

- **Finding it**: every skill finds a scene's speech voices from the scene card's **Characters** field, matched to the Voice Index by name (see "Finding the voices of a scene" in book-voices). The Manuscript Desk does the same when it rewrites a paragraph: the chapter's context carries the speech voices of the characters in its scene map, at that chapter's setting.
- **scene-builder**: in each scene card, for every character who speaks, note their speech voice and the chapter's setting ("speaks per CHAR-X-SPEECH, ch. 7 row"), and any line the plan already gives them.
- **co-writer**: when writing dialogue, follow the speaker's speech voice at the chapter's setting; the narration around it stays in the chapter's narrator voice.
- **paragraph-review** and **chapter-review**: check every line of dialogue against its speaker's speech voice for that chapter (fluency, sentence building, figures, signature words rationed, never-says), in every language, and flag drift between chapters that the per-chapter table does not explain.
- **Updating**: when the author changes a character's arc in Chapters, or when written dialogue drifts on purpose, run this skill again on that character: show the rows that change and update the file through book-voices.
