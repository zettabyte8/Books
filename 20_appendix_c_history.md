# Appendix C: Prompt History (Annotated)

Reproduced verbatim. Annotations by the Venice AI audit identify what each prompt actually did.

| # | Prompt | Effect |
|---|---|---|
| 1 | "study of control and manipulation of mass amounts of people list branches of study light/dark methodologies desired outcomes vs actual historical outcomes run a local python script to generate a downloadable .pdf link…" | Established all three core structures. Everything downstream inherits them. |
| 2 | "Rerun prompt" | First of seven retries caused by file-generation failure. |
| 3 | "Are you agent generated when I click 'show more'…" | Meta. No content. |
| 4 | "…explain what you mean by fresh model response…" | Meta. Establishes that the session had no memory of itself. |
| 5 | "…you previously were successful in generating the files… read the session history" | Meta. |
| 6 | "I haven't closed this popup… you fail first attempt…" | Meta. |
| 7 | "Ok give it a try and I didn't click anything… there is no rerun button…" | Meta. Reveals the model assumed desktop throughout. |
| 8 | "digital-era algorithmic tactics" | Chapter 5 of the first edition. Bare noun phrase; the model chose all depth. |
| 9 | "additional historical case studies" | Chapter 4 of the first edition. Note: "additional" — the set was never specified, so the model selected. |
| 10 | "cognitive defense strategies" | Chapter 6 of the first edition. |
| 11 | "Generate both in one continuous document as have been doing" | Assembly instruction. |
| 12 | "Both" | Disambiguation. |
| 13 | "Expand each section as much as possible with available information convert into educational book ready for me to submit to a publisher" | The pivotal prompt. "As much as possible" produced length without pedagogy. |
| 14 | "Site references sources add complete prompt history… that it's written by Gemini prompted by Thomas G Coleman… suitable for use in schools" | Added the bibliography and provenance. |
| 15 | "Rerun previous prompt" | Final retry. |

**What the record shows.** Seven of fifteen prompts are about tooling, not content. Only six carry subject matter, and five of those are two-to-four word noun phrases. The book was therefore shaped almost entirely by model defaults — which is precisely why it arrived with academic prose and no lesson apparatus: the defaults of a chatbot are not the defaults of a classroom. Prompt 13 asked for "as much as possible" and got volume; nobody asked for objectives, summaries, or activities, and so none appeared.

**What the record does not show.** Every later change is invisible here. The three non-Atlantic chapters, the Overton case, the Speer source-problem box and the whole pedagogy all came from the audit, not from the session — and none of them has a prompt behind it. The prompt history is the origin of the book, not the book's method.

**Lesson for the student.** A prompt that specifies *audience and use* produces a different artefact from one that specifies *length*. Compare prompt 13 with: "Rewrite for 16-year-olds at a 900L reading level, with objectives, a summary, and one activity per section."