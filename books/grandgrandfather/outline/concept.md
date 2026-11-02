# 00 Book Concept

A short introduction to the project for the author, a co-writer or an AI. It holds the central ideas only; the events, in order and with sources, live in **Chapters** (`outline/chapters.md`), and the people in the **Character Bible**. Last updated Nov 2, 2026 (reorganized: the working context brought up to date, the six movements replaced by a pointer to Chapters, the key ideas rewritten as central ideological pillars, in order of importance). The earlier long version is kept as "Book Concept — archive (long version, Oct 7, 2026)".

## Working context

  - **Book**: working title "Book: Grandgrand father story" (to decide). Author: Rafael; his mom writes or revises parts in Portuguese. English and Brazilian Portuguese side by side. Target about 300 pages (80,000–85,000 words); 350 is a hard limit. Word budgets per chapter are adjusted as he writes.
  - **The story and its structure**: see **Chapters** (`outline/chapters.md`), the backbone of the book, with every event per chapter, in order, with sources. Current shape: Prologue (The Fog) · Part I, Bahia (ch. 1–3) · Part II, War (ch. 4–9) · Part III, Free, not equal (ch. 10) · Part IV, The woman from Spain (ch. 11, Her Road) · Part V, Fortune (ch. 12, the Interlude, Tonico's Journey, ch. 13–16) · Part VI, The fall (ch. 17–18) · Epilogue (option). This file does not repeat the plot.
  - **Working names, for planning only**: Benedito (him) and Carmen (the woman from Spain). Never in the book text.
  - **Standing rules from Rafael**: every story line he gives goes into Chapters, with all his details, and he confirms which chapter an event goes into; the Character Bible holds only short bullets (personality, backstory, minor details); no new characters, or expanded ones, without his approval; he writes the funny childhood stories himself; show changes before applying them and never overwrite his or his mom's text without approval (her Portuguese is the source when she wrote it); brainstorm before cutting arcs; the book lives only in the repo (`rafaxalv/cowriter`), and downloads go into the repo, never onto his computer.
  - **How the files fit together**:
    1.  **00 Book Concept** (this file): the central ideas. Least detail.
    2.  **Chapters**: the skeleton. Every event per chapter, in order, with sources for real events that must be accurate.
    3.  **Scenes**: each chapter's events expanded into ordered scenes (when, where, point of view, characters, beats, motivations, feelings, place details, voice). Built by the scene-builder skill.
    4.  **Book**: the final text, written from the scenes in the planned voices. Full detail.
      - Branching from the Concept, used at every level: the Character Bible (who people are, plus a Continuity section with what the text has established), the historical research (`research/`), the Voices (`voices/`), and the shared reference library (`library/`, with style studies).
      - Changes flow down (concept → chapters → scenes → text); deliberate changes in the text flow back up.
  - **Files**: listed in the book profile, `BOOK.md` (paths in this repo).
  - **Manuscript format**: one file per language (`book/manuscript.en.md`, `book/manuscript.pt-br.md`), one paragraph per block, each preceded by a hidden Paragraph ID (chapter.row; prologue 00, interlude INT, epilogue 99) that matches across the two files.
  - **Manuscript Desk** (`tools/manuscript-editor/`): an editor page that keeps its own copy of the book; sync its edits back before changing the manuscript or Paragraph Parameters in the repo, and refresh it after the plan changes (steps in its README).
  - **Editing notes**: changes are shown first, applied after approval, then committed and pushed to GitHub through the book-repo skill (see `BOOK.md`).

## The book in one paragraph

A family story told by the author's grandmother: her grandfather was born enslaved, went to the Paraguayan War, came back free, won the lottery, bought farms and "bought a Spanish girl" whom he married; after his death the sons lost everything gambling. The book is immersive historical fiction built around those few remembered facts, with the real world of nineteenth-century Brazil around them. Much is invented; the history is not.

## Central ideological pillars

In order of importance. The voices draw on them in every chapter; the first one most of all.

### 1. Family and descent

  - **The central theme of the book.** What family means, how complex it is, how the people who came before us shape who we are, and how we, in turn, shape the people after us, often without knowing it. Nobody in the book chooses where they start; everyone passes something on.
  - **The three boys.** Benedito, Tonico and Ezequiel grow up on the same estate, in the shadow of the same master, and their family position decides their trajectory more than anything they do. Benedito, enslaved, the son of Luzia and Inácio, has a mother and a father and no rights. Tonico, the legitimate heir, has the name, the land and the debts, and the fear of his father. Ezequiel, the master's son whom nobody names, has the blood and nothing else: "Not black enough to fight, not white enough to be a master" (ch. 3). Three colours, three places in one family, three lives. They are the book's central exposition of how family can make or break a path; Tonico's milk-brother bond with Benedito and Ezequiel's unrecognised blood are the two faces of it.
  - **Slavery breaks family, and family survives it anyway.** Mothers sold away from their sons (Luzia), a master's son left unnamed (Ezequiel), a man used to father children for a fazenda, a father of too many to be father of any (Pata Seca, through the son Benedito meets in the war, ch. 4–7). And yet the bonds hold in other forms: the milk brother, the roda as a clan (Kalunga, Bastião), Luzia's letters, Tonico keeping them for years.
  - **What passes down.** Faith in luck, violence, the fear of losing everything, music and healing (the one good inheritance) pass from Luzia to him, to his sons, and on to the grandmother, the nursing assistant who never knew where her hands came from. The sons are named after the dead and the absent (Inácio, Manuel, Xosé). Repeated lines show the inheritance ("Why does he have to be so angry?"); nobody explains it. Some chains break; most do not.
  - **The book itself is a descendant's search.** Benedito searches for his mother; his own sons never know who he was; the author searches for a great-great-grandfather whose name is lost (decided Oct 30, 2026).
  - **For the voices.** Look for the family thread in every scene: a gesture, a phrase, a fear or a skill that came from someone before, or will reach someone after. Show it, never explain it; let the reader connect the generations. Every character is someone's child first.

### 2. Luck

  - **The luck of birth.** Being born a certain colour, into a certain family, on the right or wrong side of the estate decides almost everything (the three boys, pillar 1).
  - **The luck of the draw.** The lottery: twenty contos on one ticket, and a life turned over overnight. Luck sees no race, so he trusts it, more than God, more than people.
  - **The right place at the right time.** The war as a door to freedom; a newspaper that reaches Bahia; a girl seen in Albino's house; the agent on the steamer who only looks at the ox.
  - **Making your own luck.** Luzia learns that the orixás alone are not enough: *Deus ajuda quem cedo madruga*, and she saves, and buys her freedom. He stops waiting on luck when her letters come, and the Purchase is a decision, not a draw. Carmen, the only time it is said: "Men believe in luck; women count." The book weighs the two all the way through: what was given, and what was made.

### 3. Four forces in every scene: luck, freedom, violence, money

  - Luck sees no race, so he trusts it (pillar 2); freedom is not the happy ending; violence is the first language he learned, and he passes it on; money is freedom, and is not.

### 4. The missing names, and memory

  - **The missing names.** Neither he nor the woman from Spain is ever named; he whispers his true name to her on his deathbed and the reader never hears it. The only written list with his registered name, Padre Felício's, is lost at the end of the war (ch. 6, 9). Everyone remembers what he did; nobody remembers who he was. What survives when the name doesn't?
  - **The family's own forgetting.** The author's grandmother, who told the story, died after years with Alzheimer's; his grandfather has the disease too as the book is written. Her siblings died, the documents were lost, and by the time the family tried to check her stories it was too late. It was not the disease that erased a generation: memory was simply never valued; surviving came first (prologue, 00.001–00.010).
  - **The country's forgetting.** In December 1890 the finance minister Rui Barbosa ordered the slavery records held by the treasury to be burned \[DOCUMENTED; to cite\]. The state, too, chose not to remember. Real aspect for the author's note; never explained in the chapters.
  - **Memory you cannot trust.** The grandmother's fog in the frame, his failing memory at the end (never named as a disease, ch. 17): the reader is not always sure who is right.

### 5. Freedom

  - **What freedom is worth, and what it costs.** He bets his life on the war as a door to freedom, and gets it; then freedom in Corumbá is poorer and harder than he dreamed (Part III, "Free, not equal"). The paper says free; the street, the clerk who writes *preto* on the deed, and the neighbours say otherwise. Freedom is not the happy ending.
  - **Many kinds of freedom.** The law's (a letter of manumission, 1888 as news from far away), money's (the lottery buys land, not respect), and the inner kind that no paper gives: freedom from fear, from the war in his head, from the master he carries inside. He wins the first two and never the third.
  - **Freedom bought and sold.** Luzia buys her freedom, and still cannot go back to her son for lack of the fare. The free woman from Spain is sold, and he buys her: saving her and owning her at once ("You didn't save me, you own me", ch. 16).
  - **Liberdade, where nobody is free.** The farm whose name says everything he fought for traps everyone in it, each in a different way: him by fear and distrust, her by a marriage she never chose, the sons by their father's anger and rules. The narrator never points out the irony; the reader sees it.

### 6. Mirrors

  - The gossip says he is the master's son and it is false; Ezequiel is, and nobody says it. The enslaved man becomes a master; the free woman loses her freedom; the boyhood friendship across the colour line returns as the white "friends" who ruin his sons. The fence between the farms becomes the fence in the marriage (ch. 15).

## How it is told

  - **History blended in, never explained.** No factual step-outs; the real world enters through objects, documents, dialogue and rumour. The line between truth and invention is drawn once, in an author's note.
  - **Chance, contradictions, no judgement.** No heroes and no villains, Black or white; the reader sees the reasons behind each choice and weighs it.
  - **Voices.** The chapters are in close third person, following him and later her. The prologue and epilogue are in the author's own voice (AUTHOR-MAIN), about his grandmother.
  - **Chapter shape.** Hook, scene, texture, turn, cliffhanger. The book follows him, in long chapters. Her road before Corumbá is one chapter of her own (ch. 11): over many meetings at Albino's in 1877 she tells him her story, part by part, told from her side; it comes after they meet and before the lottery, so the reader knows who she is before he buys her (decided Nov 1–2, 2026).
  - **Tone range.** From a funny, mischievous childhood to the war's horror; humour keeps him from being only a victim.

## Handle with care

  - Scenes of slavery are told from inside the person being sold or used, never through the buyers' eyes; sexual violence is never shown directly. Exceptions chosen by Rafael: Ezequiel's goiabeira night (ch. 2) and first whipping (ch. 3) are explicit; they are cathartic character set-ups.
  - The hardships of freedom are his lived experience, never the narrator's verdict (the "better off enslaved" argument belonged to the planters).
  - Family traditions are never quietly turned into facts. Working notes use truth labels (DOCUMENTED, STRONGLY SUPPORTED, FAMILY TRADITION, PLAUSIBLE RECONSTRUCTION, FICTIONAL); the reader never sees them.
