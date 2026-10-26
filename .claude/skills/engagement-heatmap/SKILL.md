---
name: "engagement-heatmap"
description: "Use when the author wants a chapter (or passage) of a book in this repo scored for reader engagement, pace and emotional impact, shown as a 5-level colored text heatmap with a chapter curve."
---

# Engagement heatmap

Reads a chapter of a book and scores how engaging each part is for a reader, then shows it as a heatmap: every word colored by its score, plus a curve for the whole chapter. The goal is to see where the text grips, where it rests, and where readers might start skimming.

This skill is generic. Everything specific to one book lives in that book's folder.

## Find the book

1. Books live in `books/<slug>/`, each with a `BOOK.md` (the book profile). If there is only one book, use it; otherwise use the one the author names, or ask.
2. Read `BOOK.md`: file paths (manuscript, Chapters, Continuity record, Paragraph Parameters, Engagement scores, Engagement Anchors), languages, the Paragraph ID format, and its notes for the skills (for example voices that are deliberately quiet). Then read the Concept for the book's tone.

## Where this method comes from

(Full links in References at the end.)

- **Narrative engagement** (Busselle & Bilandzic's narrative engagement scale): readers are engaged through understanding the story, attentional focus, emotional engagement, and the feeling of being inside the story world. Confusion lowers engagement as much as boredom does.
- **Suspense** is forward-looking uncertainty: an open question about an outcome that matters. **Surprise** is backward-looking: something unexpected given what came before (Wilmot & Keller 2020, scored sentence by sentence on a 5-point scale; Gerrig; Brewer).
- **Narrative arc** (Boyd, Blackburn & Pennebaker 2020): stories move from staging (setting, description) to plot progression (action) while cognitive tension builds toward a peak in the middle or late part.
- **Pace and novelty** (Toubia et al., "shapes of stories"; Zimmerman 2026 on semantic novelty): how fast the text moves into new ground, and how much new territory it covers, relate to readers' appetite.
- **Expectation** (Fong & Gui 2024): what readers expect to happen next, and how uncertain they are about it, predicts whether they keep reading, more than the emotion of the current text alone. Expected trouble keeps readers reading.
- **Limits of AI scoring** (Matlin et al., Georgia Tech): language models agree with humans on whether suspense is present and on whether it is rising or falling, but are poor at exact numbers and at turning points. So this skill scores against fixed anchor examples, scores relative to the chapter, flags uncertain spots, and treats real readers' reactions as the final judge.

## The 5-level scale

The main score is **engagement** (1-5). Each scored unit also gets three sub-scores on the same 1-5 scale, so the author can see *why*:

- **Tension**: is there an open question with stakes (danger, a secret, a choice, a threat of loss) that the reader wants answered? Does something unexpected happen?
- **Emotional impact**: how intense the feeling is (arousal), regardless of whether it is happy or sad.
- **Pace**: how fast story time and action move (1 = lingering description or reflection, 5 = rapid events).

Engagement is a judgment informed by the three, not their average: a slow, quiet paragraph can be highly engaging if a strong question hangs over it.

| Level | Name | What it looks like |
|---|---|---|
| 5 | Gripping | Stakes are in play right now: danger, a revelation, a decision with no way back. Outcome uncertain, strong emotion, the reader cannot stop. |
| 4 | Engaging | Clear tension or emotional charge, the story moves, the reader wants the next line. |
| 3 | Steady | Interesting and purposeful: setting up, mild tension, new information arriving at a good rate. |
| 2 | Calm | Description, reflection, background, slow passage of time. Restful; fine when it serves a purpose (after a peak, before a storm). |
| 1 | Flat | Nothing open to wonder about, repeats what the reader knows, summary without stakes, or confusing. Risk of skimming. |

Low is not automatically bad. A good chapter breathes: 2s after a 5 are often right. The problems are long flat stretches, 5s that run so long they numb the reader, and calm where the story needs urgency.

## Anchors (calibration)

Keep the book's **Engagement Anchors** file: for each level, 2-3 short paragraphs from the book itself that the author agrees deserve that score. The first time, propose anchors from the chapter being scored and ask the author to confirm or move them. Always score against these anchors so scores mean the same thing across chapters. Update anchors only with the author's OK.

## Steps

### 1. Gather context

Read the chapter from the manuscript (or the draft named); the chapter's plan in Chapters and its scene map in Scenes (the Reader feeling planned for each scene); a summary of the previous chapters (or the Continuity record), because suspense depends on what the reader already knows and fears; the Engagement Anchors; and the voices used (from Paragraph Parameters), so a deliberately calm voice is judged fairly.

### 2. Score

- **Unit of scoring: the sentence**, split into clauses when a long sentence clearly changes intensity midway. Research scores sentences or segments; single words carry no engagement on their own.
- **Word-level heatmap**: every word takes the score of its sentence or clause. Then mark **hot words**: the specific words where a jolt lands (a reveal, a name, a threat, a sensory shock). Hot words get an outline in the heatmap, not a different score.
- For each sentence record: engagement, tension, emotional impact, pace, and a one-line reason ("open question: will she get across?").
- Score each sentence twice, independently, reading in order. Where the two passes differ by 2 or more levels, mark the sentence **uncertain** and use the lower score.
- Also mark **turning points** (where the curve changes direction), since these are where AI scoring is least reliable; ask the author to check them.

### 3. Chapter analysis

- **Curve**: engagement per paragraph (average and peak) across the chapter, with tension, emotion and pace as thinner lines.
- **Flat stretches**: 3 or more consecutive paragraphs averaging 2 or less, unless planned.
- **Numb stretches**: long runs at 5 with no release.
- **Shape**: compare with the chapter's purpose in Chapters, the Reader feeling planned per scene, and the narrative arc (staging early, rising tension, a peak, release). Note where the chapter ends: on an open question (pulls the reader into the next chapter) or fully resolved.
- **Suggestions**: for each problem, the Paragraph IDs and a concrete idea (cut, compress into summary, add an open question, move a reveal, switch to scene). These are suggestions, never automatic edits; chapter-review and paragraph-review apply changes.

### 4. Every language

Score the language the profile marks as written first. If other language versions exist, score them too and flag paragraphs where the versions differ by 2 or more levels: the translation may have lost or added tension.

## Output

1. **Heatmap page**: an HTML page published as an artifact named "Heatmap - <book> - Chapter N" (republish the same artifact on reruns). Each word colored by its level using a 5-step sequential color scale that works in light and dark mode and for color-blind readers (load the dataviz skill for the palette), hot words outlined, uncertain sentences underlined dotted, Paragraph IDs in the margin, a legend, and on hover the sentence's sub-scores and reason. A toggle switches the coloring between engagement, tension, emotion and pace. The chapter curve sits at the top.
2. **Report in chat**: the curve in a few words, the 3-5 most important problems with Paragraph IDs, and the turning points to check.
3. **Data**: save sentence scores in the book's **Engagement** scores file (columns as the profile lists them), and add per-paragraph average and peak engagement to Paragraph Parameters (only those columns; never touch the others). Hand the changes to the **book-repo** skill, which saves them.

## Notes

- Scores are estimates of a typical reader, not truth. When beta readers mark where they got bored or could not stop, compare with the scores and adjust the anchors.
- Never rewrite text in this skill.
- Engagement is not the same as quality: a deliberately quiet passage (for example in a frame or author voice) can be exactly right at level 2.

## References

- Busselle, R. & Bilandzic, H. (2009). Measuring narrative engagement. Media Psychology. https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/39512
- Meta-analysis of the narrative engagement scale, "Engagement is not one thing": https://opus.bibliothek.uni-augsburg.de/opus4/frontdoor/index/index/docId/132636
- Wilmot, D. & Keller, F. (2020). Modelling Suspense in Short Stories as Uncertainty Reduction over Neural Representation. ACL. Sentence-level suspense; 5 human annotators per sentence on a 5-point scale; best model close to human agreement. https://ar5iv.labs.arxiv.org/html/2004.14905
- Matlin, G., Zhang, D., Loza, R., Popescu, D. M., Isbell, J., Chakraborty, C. & Riedl, M. (Georgia Tech). Do Language Models Agree with Human Perceptions of Suspense in Stories? LLMs agree on presence (78%+) and direction of suspense, poorly on magnitude and turning points. https://arxiv.org/pdf/2508.15794
- Fong, H. & Gui, G. (2024). Modeling Story Expectations to Understand Engagement. 30,258 chapters from 1,735 online books; expected negative valence predicts continued reading. https://arxiv.org/pdf/2412.15239v3
- Toubia, O. et al. How Quantifying the Shapes of Stories Predicts their Success (speed, volume, circuitousness). PNAS. https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/How-Quantifying-the-Shapes-of-Stories-Predicts-their-Success.pdf
- Zimmerman, W. F. (2026). Semantic Novelty at Scale: Narrative Shape Taxonomy and Readership Prediction in 28,606 Books. Volume of semantic novelty predicts downloads; circuitousness is mostly a length effect. https://arxiv.org/html/2602.20647v1
- Boyd, R. L., Blackburn, K. G. & Pennebaker, J. W. (2020). The narrative arc: Revealing core narrative structures through text analysis. Science Advances. Summary: https://news.utexas.edu/2020/08/07/authors-invisible-words-reveal-blueprint-for-storytelling/ ; method notes: https://liwc.app/help/aon
- Background on suspense in psychology, as replicated in Matlin et al.: Gerrig & Bernardo (1994); Brewer & Ohtsuka (1988); Delatorre et al. (2018); Lehne & Koelsch (2015).
