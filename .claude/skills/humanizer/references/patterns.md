# AI-Writing Pattern Catalog

Reference material for the humanizer skill. Twenty-nine patterns documented in Wikipedia's "Signs of AI Writing" guide (WikiProject AI Cleanup), all rooted in the same cause: LLMs regress to the statistically most likely output for the widest variety of cases, trading specificity for generic probability.

For each pattern: what to scan for, why it is a tell, how to fix. Before/after examples illustrate the transformation.

---

## Content patterns

### Pattern 1 — Significance inflation

**Scan for:** stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted.

**Problem:** LLM writing inflates the importance of arbitrary details by stating how they "represent" or "contribute to broader trends." The subject becomes simultaneously less specific and more exaggerated.

**Fix:** Remove the inflation phrase. Keep the fact. If no fact remains, cut.

Before:

> This initiative marks a pivotal moment in the evolution of regional business advisory services, reflecting broader trends in the industry.

After:

> This initiative expanded advisory capacity to serve companies under $5M in revenue for the first time.

---

### Pattern 2 — Notability and media claims

**Scan for:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence, profiled in, has been featured in.

**Problem:** LLMs assert notability by listing coverage without quoting it.

**Fix:** If the coverage claim is documented in the source material, cite the specific piece and what it said. If not documented, remove the claim.

Before:

> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

After:

> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

---

### Pattern 3 — Superficial -ing analyses

**Scan for:** highlighting/underscoring/emphasizing..., ensuring..., reflecting/symbolizing..., contributing to..., cultivating/fostering..., encompassing..., showcasing...

**Problem:** Present participle (-ing) phrases tacked onto sentence ends to add fake analytical depth without adding information.

**Fix:** Cut the -ing phrase. If the idea it gestures at is real, write it as a separate sentence with a concrete claim.

Before:

> We provide comprehensive SEO audits, ensuring client growth and reflecting our commitment to excellence.

After:

> We provide comprehensive SEO audits. Clients who complete a full audit average 3.2x organic traffic growth within six months.

---

### Pattern 4 — Promotional language

**Scan for:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning, diverse array, seamless.

**Problem:** LLMs default to advertisement-like prose, especially for anything that could be called "cultural heritage" or a local business.

**Fix:** Replace with neutral, specific language. Numbers and named facts beat adjectives every time.

Before:

> Nestled in the heart of San Diego, our renowned firm offers breathtaking results through our commitment to excellence.

After:

> Our San Diego firm has completed 200+ SEO engagements since 2018.

---

### Pattern 5 — Vague attributions

**Scan for:** Industry reports, Observers have cited, Experts argue, Some critics argue, Studies show, Research indicates, several sources.

**Problem:** AI attributes opinions to unnamed authorities.

**Fix:** Name the source, year, and specific claim, or remove.

Before:

> Due to its unique characteristics, the Haolai River is of interest to researchers and conservationists. Experts believe it plays a crucial role in the regional ecosystem.

After:

> The Haolai River supports several endemic fish species, according to a 2019 survey by the Chinese Academy of Sciences.

---

### Pattern 6 — Formulaic "challenges / future outlook" sections

**Scan for:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook section headings.

**Problem:** Rigid formulaic "challenges and future" sections tacked onto the end of a piece.

**Fix:** Integrate genuine challenges into relevant body sections as specific facts. Remove vague "future looks bright" conclusions.

Before:

> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

After:

> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

---

## Language and grammar patterns

### Pattern 7 — Banned AI vocabulary

**Words to eliminate:** actually (as opener), additionally (sentence-opener), align with, bolstered, crucial, delve, emphasizing, enduring, enhance, fostering, garner, highlight (as verb), interplay, intricate/intricacies, key (as adjective), landscape (as abstract noun), meticulous/meticulously, pivotal, showcase, tapestry (as abstract noun), testament, underscore (as verb), valuable, vibrant.

**Problem:** These words appear far more frequently in post-2023 text and tend to co-occur.

**Fix:** Replace each with the most direct specific alternative. If a sentence cannot survive without one of these words, the sentence probably is not saying anything real. Cut or rewrite from scratch.

Before:

> This valuable framework underscores the intricate interplay between SEO and content strategy, fostering long-term results.

After:

> This framework ties keyword research directly to content production. Teams that follow it see results compound across quarters, not campaigns.

---

### Pattern 8 — Copula avoidance

**Scan for:** serves as, stands as, marks, represents [a], boasts, features (as synonym for "has"), offers (as synonym for "has"), maintains (as synonym for "has"), functions as.

**Problem:** LLMs substitute elaborate constructions for simple copulas.

**Fix:** Replace with is, are, has. Nearly always cleaner.

Before:

> Gallery 825 serves as LAAA's exhibition space. The gallery features four separate rooms and boasts over 3,000 square feet.

After:

> Gallery 825 is LAAA's exhibition space. The gallery has four rooms totaling 3,000 square feet.

---

### Pattern 9 — Negative parallelisms

**Scan for:** Not only...but..., It's not just..., it's..., It is not merely..., Not X, but Y. Also clipped tailing negations such as "no guessing" or "no wasted motion" tacked onto the end of a sentence as a fragment.

**Problem:** Manufactured rhetorical contrast. Overused by LLMs because it sounds punchy with minimal thought behind it.

**Fix:** State the positive claim directly. Skip the rhetorical contrast.

Before:

> It's not just an audit. It's a growth roadmap.

After:

> The audit identifies specific fixes, ranked by estimated revenue impact.

Before (tailing negation):

> The options come from the selected item, no guessing.

After:

> The options come from the selected item without forcing the user to guess.

---

### Pattern 10 — Rule of three overuse

**Problem:** LLMs force ideas into groups of three to appear comprehensive. "Innovation, inspiration, and industry insights."

**Fix:** Use the number of items the content actually has. If you have one strong point, make one point. Cut the weakest of the three if all three exist only to complete the pattern.

Before:

> The event features keynote sessions, panel discussions, and networking opportunities. Attendees can expect innovation, inspiration, and industry insights.

After:

> The event includes talks and panels. There is also time for informal networking between sessions.

---

### Pattern 11 — Synonym cycling (elegant variation)

**Problem:** AI repetition-penalty code causes excessive synonym substitution. The protagonist becomes "the main character," then "the central figure," then "the hero." In business content, the company name becomes "the firm," then "the organization," then "the team."

**Fix:** Pick one name per entity and use it consistently.

Before:

> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

After:

> The protagonist faces many challenges but eventually triumphs and returns home.

---

### Pattern 12 — False ranges

**Scan for:** "from X to Y" constructions where X and Y are not on a meaningful scale. "from startups to enterprise," "from discovery to delivery," "from the singularity of the Big Bang to the grand cosmic web."

**Fix:** Cut the false range. State the actual scope plainly.

Before:

> We serve clients from early-stage startups to Fortune 500 enterprises.

After:

> We work with companies between $2M and $50M in revenue.

---

### Pattern 13 — Passive voice and subjectless fragments

**Scan for:** "No configuration file needed." "The results are preserved automatically." Subjectless imperative fragments that hide the actor.

**Fix:** Add the subject. Rewrite in active voice when it is clearer.

Before:

> No configuration file needed. The results are preserved automatically.

After:

> You do not need a configuration file. The system preserves the results automatically.

---

## Style patterns

### Pattern 14 — Em dash overuse

**Problem:** LLMs use em dashes far more than humans in professional writing, often mimicking "punchy" sales copy.

**Fix:** Per `voice/constraints.md` rule #1, use commas or parentheses for asides, periods for breaks. Em dashes are reserved for ranges (2020–2024) and code contexts. Do not use em dashes as rhythmic pauses, even sparingly.

Before:

> The term is primarily promoted by Dutch institutions—not by the people themselves. You don't say "Netherlands, Europe" as an address—yet this mislabeling continues—even in official documents.

After:

> The term is primarily promoted by Dutch institutions, not by the people themselves. You don't say "Netherlands, Europe" as an address. The mislabeling continues even in official documents.

---

### Pattern 15 — Boldface overuse

**Problem:** AI emphasizes phrases in boldface mechanically, often bolding every instance of a key term.

**Fix:** Bold only the first defining use of a term (if format calls for it) or table headers. Never bold mid-sentence phrases for emphasis in prose paragraphs.

Before:

> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

After:

> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

---

### Pattern 16 — Inline-header bullet lists

**Problem:** Bullets formatted as `- **Bold Header:** Description text` — almost exclusively AI output.

**Fix:** Rewrite as prose, or convert to plain bullets without the bold header. Tables are acceptable when the content is genuinely tabular.

Before:

> - **Speed:** Our platform processes requests in under 200ms.
> - **Accuracy:** Our models achieve 94% precision on benchmark tests.

After:

> Our platform processes requests in under 200ms with 94% model precision.

---

### Pattern 17 — Title case in prose headings

**Scan for:** H2/H3 headings with all main words capitalized.

**Fix:** Convert to sentence case (capitalize only the first word and proper nouns).

Before:

> ## Strategic Negotiations And Global Partnerships

After:

> ## Strategic negotiations and global partnerships

---

### Pattern 18 — Emojis in content

**Problem:** AI decorates headings or bullets with emojis.

**Fix:** Remove all emojis from article body, headings, and bullet lists. Use only when the target surface explicitly calls for them.

Before:

> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

After:

> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

---

### Pattern 19 — Curly quotation marks

**Problem:** Some AI tools use curly quotes ("...") instead of straight quotes ("...").

**Fix:** Replace curly quotes with straight quotes throughout.

---

## Communication patterns

### Pattern 20 — Chatbot artifacts

**Scan for:** "I hope this helps," "Of course!", "Certainly!", "Would you like...", "let me know," "here is a...", "Great question!"

**Problem:** Text meant as chatbot correspondence ends up in the content.

**Fix:** Remove entirely.

Before:

> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

After:

> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

---

### Pattern 21 — Knowledge-cutoff disclaimers

**Scan for:** "As of my last update," "While specific details are limited," "not widely documented in available sources," "based on available information."

**Fix:** Remove the disclaimer. If the underlying claim is uncertain, either source it properly or cut the claim.

Before:

> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

After:

> The company was founded in 1994, according to its registration documents.

---

### Pattern 22 — Sycophantic tone

**Scan for:** "Great question!", "You're absolutely right," "That's an excellent point," excessive affirmation language.

**Fix:** Remove. Start with the actual content.

Before:

> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

After:

> The economic factors you mentioned are relevant here.

---

## Filler and hedging patterns

### Pattern 23 — Filler phrases

| Before | After |
|---|---|
| In order to achieve this goal | To achieve this |
| Due to the fact that | Because |
| At this point in time | Now |
| In the event that | If |
| Has the ability to | Can |
| It is important to note that | [delete phrase, keep content] |
| In today's [adjective] world | [delete entirely] |
| When it comes to [topic] | [start with the actual point] |
| It goes without saying | [delete — then do not say it] |
| Moving forward | [delete or replace with specific timeframe] |
| At the end of the day | [delete entirely] |
| All things considered | [delete entirely] |

---

### Pattern 24 — Excessive hedging

**Scan for:** "could potentially possibly," "it might be argued that," "may have some effect," stacked qualifiers on a single claim.

**Fix:** Remove stacked qualifiers. One qualifier per claim is the maximum. If the claim requires heavy hedging, either source it or cut it.

Before:

> It could potentially possibly be argued that the policy might have some effect on outcomes.

After:

> The policy may affect outcomes.

---

### Pattern 25 — Generic positive conclusions

**Scan for:** "The future looks bright," "Exciting times lie ahead," "continues this journey toward excellence," "represents a major step in the right direction," "the sky's the limit."

**Fix:** Replace with a specific, concrete closing claim. A real next step, a specific outcome the reader can expect, or a specific call to action.

Before:

> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence.

After:

> The company plans to open two more locations next year.

---

### Pattern 26 — Hyphenated compound overuse

**Scan for:** third-party, cross-functional, client-facing, data-driven, decision-making, well-known, high-quality, real-time, long-term, end-to-end appearing with machine-like consistency throughout a piece.

**Problem:** AI hyphenates common word pairs with perfect consistency. Humans rarely hyphenate these uniformly.

**Fix:** Remove hyphens from common compound modifiers when used as adjectives before a noun. Retain hyphens in uncommon or technical compounds where the hyphen genuinely aids clarity.

Before:

> The cross-functional team delivered a high-quality, data-driven report on our client-facing tools. Their decision-making process was well-known for being thorough and detail-oriented.

After:

> The cross functional team delivered a high quality, data driven report on our client facing tools. Their decision making process was known for being thorough and detail oriented.

---

### Pattern 27 — Persuasive authority tropes

**Scan for:** "The real question is," "at its core," "in reality," "what really matters," "fundamentally," "the deeper issue," "the heart of the matter."

**Problem:** These phrases pretend to cut through noise to a deeper truth, but the sentence that follows is usually an ordinary point with added ceremony.

**Fix:** Cut the trope. Keep the point.

Before:

> At its core, what really matters is whether your SEO strategy drives qualified traffic.

After:

> SEO strategy should be measured by qualified traffic, not raw rankings.

---

### Pattern 28 — Signposting

**Scan for:** "Let's dive in," "let's explore," "let's break this down," "here's what you need to know," "now let's look at," "without further ado," "in this section we will."

**Fix:** Delete the signposting phrase. Start with the content.

Before:

> Let's dive into how caching works in Next.js. Here's what you need to know.

After:

> Next.js caches data at multiple layers, including request memoization, the data cache, and the router cache.

---

### Pattern 29 — Fragmented headers

**Scan for:** A heading followed by a one-line paragraph that merely restates the heading before the real content begins.

**Fix:** Delete the restatement sentence. Start the section with real content.

Before:

> ## Performance
>
> Speed matters.
>
> When users hit a slow page, they leave.

After:

> ## Performance
>
> When users hit a slow page, they leave.

---

## Source

[Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup. The patterns documented there are drawn from observations of thousands of instances of AI-generated text on Wikipedia.

Key insight from Wikipedia: "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."
