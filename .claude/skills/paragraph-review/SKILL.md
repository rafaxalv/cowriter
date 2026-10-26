---
name: "paragraph-review"
description: "Use when the author wants a single paragraph or a few paragraphs of a book in this repo checked or fine-tuned against a voice, either on its own or as called by the chapter-review skill."
---

# Paragraph review

Checks and fine-tunes paragraphs of a book against a voice from the book's voices folder (managed by the book-voices skill). Usually it is called by **chapter-review**, which provides the context. It can also be used on its own for a quick check or for hand-tuning one paragraph.

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask.
2. Read `BOOK.md`: file paths, languages, people and roles (whose wording is the source in each language), the Paragraph ID format and the Paragraph Parameters columns.

## 1. Inputs

- **The paragraph(s)**, with Paragraph ID if known (for example 03.014), in one or several of the book's languages.
- **The voice**: read the voice file: the core (tags, literacy profile, target profile with base values and allowed ranges, voice rules, conveying-feeling rules) and the language layer for each language being checked (offsets, vocabulary strategy, phrase-building strategies, address and dialogue, literacy markers, language rules, reference paragraph). Also read the **Shared Rules** and the **Bilingual Lexicon**.
- **The tuning** for this paragraph: changes from the voice's base values, for example "Violence +1", with the reason. Tuning applies to every language.
- **The context packet** (from chapter-review): chapter goal, the scene and its Reader feeling, previous and next paragraphs, characters present and what they know, timeline point, relevant Continuity facts.

When used on its own, build a context packet sized to the job, not the whole book. The heavy context is the **chapter itself**: the paragraph, the paragraphs before and after it (same-ID neighbours) in every language, and the rest of the chapter's text, because that is what the rewrite must flow with. Everything else comes in as short briefs:

- **Voice brief**: the voice's rules, Conveying-feeling rules and, per language, its vocabulary, phrase-building, address and language rules (not the reference authors, scores or reference paragraphs).
- **Scene brief**: from the scene map in Scenes, the scene this paragraph belongs to (point of view, beats, Reader feeling); if there is no scene map yet, a short excerpt of the chapter's entry in Chapters.
- **Book brief**: the profile's people and roles (whose wording is the source in each language), its standing rules, and the Concept's handle-with-care notes.
- **Continuity facts** from the Continuity record (not the whole Character Bible).
- The paragraph's tuning and reason, from Paragraph Parameters; ask which voice applies if it is not obvious.

Open the full Character Bible, the chapter plan or the voice file only when the brief is not enough: the rewrite would touch a fact, a name or a relationship, the voice has no rules yet, or the author asks for a full review. If no voices exist yet, say so and suggest creating one with the book-voices skill. If the voice has no layer yet for a language, check that language against the core only and say so. Do not invent rules.

### Rewrite brief (sent with one-shot rewrites)

Rewrite the paragraph in every language of the book to hit the target profile (voice base + tuning). Change only what the new targets require; keep the writer's words, facts, events, names and meaning wherever possible. Each language is written natively, never translated word for word from another; both versions must say the same thing. The paragraph must still flow from the previous paragraph into the next and fit the chapter's text, the scene's beats and its Reader feeling. Follow the voice brief, the book's standing rules and the handle-with-care notes; respect the Continuity facts. Never add events, named characters or facts. Where the profile names a co-author's wording as the source in a language, change it only as far as the tuning requires and say so. A target outside the voice's allowed range is a deliberate exception: honour it and mention it. Return the new text per language, a one- or two-sentence summary of what changed, a short note per language, and a list of anything the author should check (a rule at risk, a conflict with the neighbours, the scene or Continuity, any word you had to add).

**From the Manuscript Desk** (`tools/manuscript-editor/`): its "Apply to text" button runs this skill's hand-tuning (section 3) through a single Claude call with no file access. The page sends the rewrite brief above plus the packet described here, taken from its store: the whole chapter in every language with the paragraph and its neighbours marked, the voice brief, the scene brief, the book brief and the Continuity facts, the target profile and the tuning reason. The rewrite is applied at once with an Undo, and the reply lists what to check. Keep the store's copy of these briefs current (reload the book's context after changing the plan, a voice or the profile).

## 2. Review each paragraph

Target for each language = the voice's core base values + that language's offsets + this paragraph's tuning.

For each language version:

- **Verdict**: On voice / Minor drift / Off voice.
- **Tags**: narrative person, addressed to and form match the voice.
- **Literacy**: vocabulary, spelling, grammar, punctuation and sentence length fit the character's literacy level and this language's literacy markers. Flag words or ideas the character could not plausibly know.
- **Language layer**: the vocabulary strategy, phrase-building strategies, forms of address, dialogue punctuation and language rules for this language; flag anachronisms, usage from the wrong country or region, and lexicon terms used differently from the Bilingual Lexicon.
- **Rules**: only rules that are broken or at risk (core voice rules, conveying-feeling rules, language rules and shared rules), quoting the exact words that cause it.
- **Profile drift**: dimensions where the paragraph is off its target, for example "Figurative density 5 (target 2)".
- **Suggested fix**: a minimal rewrite that keeps the writer's words, facts and voice where possible and changes only what is needed. Mark changes clearly. Skip if the paragraph is on voice.

Then across the language versions:

- **Equivalence**: every version says the same thing (same facts, same events, same people) and produces the same effect, each in its own language's way. Do not flag differences that the language layers explain (a longer sentence in one language, a kept foreign word). Flag differences in meaning, and any version that reads like a word-for-word translation of another.
- **Connection**: does it follow from the previous paragraph and lead into the next? Does it contradict anything in the context packet (timeline, who knows what, who is present)? Report these to chapter-review as connection issues rather than fixing plot on its own.

When the profile says a co-author's wording is the source in a language and they wrote this paragraph, keep their wording unless it breaks a rule or contains an error, and say so; fix the other languages to match their meaning.

## 3. Hand-tuning (hyper-tuning)

The author can tune one paragraph directly: "more explicit violence here", "slow this one down", "Sensory +2". Apply the change as tuning on top of the voice in every language, rewrite the paragraph, and show the before and after with the new tuning. If the requested tuning goes outside the voice's allowed range, say so: either keep it as a deliberate exception (record the reason) or suggest adjusting the voice with the book-voices skill. A request that only concerns one language's wording ("this sounds too modern") is fixed in that language without tuning.

## 4. Output and recording

For each paragraph, also produce its **parameter row**: Paragraph ID, voice ID and version, tuning, reason for tuning, review status, date, open issues. When called by chapter-review, return the results and rows to it; chapter-review applies them. When used on its own and the author approves a change, update the paragraph in every affected manuscript file and its row in **Paragraph Parameters** in the same pass (never change one without the other), then hand the change to the **book-repo** skill, which saves it.

## Notes

- The writer's own voice comes first: suggest, do not overwrite. Never rewrite paragraphs that are already on voice.
- Keep historical facts exactly as written; flag doubts separately.
- If a rule seems to fight the story in a specific spot, say so. It may be a voice rule to refine with the book-voices skill.
