---
name: "paragraph-review"
description: "Use when Rafael wants a single paragraph or a few paragraphs of his book checked or fine-tuned against a voice, either on its own or as called by the chapter-review skill."
---

# Paragraph review

Checks and fine-tunes paragraphs of Rafael's book against a voice from the **Voices** folder in Drive (managed by the book-voices skill). Usually it is called by **chapter-review**, which provides the context. It can also be used on its own for a quick check or for hand-tuning one paragraph.

## 1. Inputs

- **The paragraph(s)**, with Paragraph ID if known (for example 03.014), in English, Portuguese or both.
- **The voice**: read the voice file: the core (tags, literacy profile, target profile with base values and allowed ranges, voice rules) and the language layer for each language being checked (offsets, vocabulary strategy, phrase-building strategies, address and dialogue, literacy markers, language rules, reference paragraph). Also read **00 Shared Rules** and **00 Bilingual Lexicon**.
- **The tuning** for this paragraph: changes from the voice's base values, for example "Violence +1", with the reason. Tuning applies to both languages.
- **The context packet** (from chapter-review): chapter goal, the moment, previous and next paragraphs, characters present and what they know, timeline point, relevant Continuity Log facts.

When used on its own: ask which voice applies if it is not obvious, read the existing row in the **Paragraph Parameters** sheet for its tuning, and read the paragraphs before and after it in the Book doc for minimal context. If no voices exist yet, say so and suggest creating one with the book-voices skill. If the voice has no layer yet for a language, check that language against the core only and say so. Do not invent rules.

## 2. Review each paragraph

Target for each language = the voice's core base values + that language's offsets + this paragraph's tuning.

For each language version:

- **Verdict**: On voice / Minor drift / Off voice.
- **Tags**: narrative person, addressed to and form match the voice.
- **Literacy**: vocabulary, spelling, grammar, punctuation and sentence length fit the character's literacy level and this language's literacy markers. Flag words or ideas the character could not plausibly know.
- **Language layer**: the vocabulary strategy, phrase-building strategies, forms of address, dialogue punctuation and language rules for this language; flag anachronisms, Portugal-only usage in the Portuguese, and lexicon terms used differently from 00 Bilingual Lexicon.
- **Rules**: only rules that are broken or at risk (core voice rules, language rules and shared rules), quoting the exact words that cause it.
- **Profile drift**: dimensions where the paragraph is off its target, for example "Figurative density 5 (target 2)".
- **Suggested fix**: a minimal rewrite that keeps the writer's words, facts and voice where possible and changes only what is needed. Mark changes clearly. Skip if the paragraph is on voice.

Then for the pair:

- **EN/PT equivalence**: both versions say the same thing (same facts, same events, same people) and produce the same effect, each in its own language's way. Do not flag differences that the language layers explain (a longer Portuguese sentence, a kept Portuguese word in the English). Flag differences in meaning, and any version that reads like a word-for-word translation of the other.
- **Connection**: does it follow from the previous paragraph and lead into the next? Does it contradict anything in the context packet (timeline, who knows what, who is present)? Report these to chapter-review as connection issues rather than fixing plot on its own.

When Rafael's mom wrote the Portuguese, keep her wording unless it breaks a rule or contains an error, and say so; fix the English to match her meaning.

## 3. Hand-tuning (hyper-tuning)

Rafael can tune one paragraph directly: "more explicit violence here", "slow this one down", "Sensory +2". Apply the change as tuning on top of the voice in both languages, rewrite the paragraph, and show the before and after with the new tuning. If the requested tuning goes outside the voice's allowed range, say so: either keep it as a deliberate exception (record the reason) or suggest adjusting the voice with the book-voices skill. A request that only concerns one language's wording ("this Portuguese sounds too modern") is fixed in that language without tuning.

## 4. Output and recording

For each paragraph, also produce its **parameter row**: Paragraph ID, voice ID and version, tuning, reason for tuning, review status, date, open issues. When called by chapter-review, return the results and rows to it; chapter-review applies them. When used on its own and Rafael approves a change, update the paragraph in the **Book** doc and its row in the **Paragraph Parameters** sheet in the same pass. Never change one without the other.

## Notes

- The writer's own voice comes first: suggest, do not overwrite. Never rewrite paragraphs that are already on voice.
- Keep historical facts exactly as written; flag doubts separately.
- If a rule seems to fight the story in a specific spot, say so. It may be a voice rule to refine with the book-voices skill.