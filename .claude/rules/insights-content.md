---
description: When editing or creating Insights blog posts, load voice files and the relevant pillar before writing.
paths:
  - "insights/**/*.html"
---

# Insights post production

You are editing or creating an Insights blog post. Before writing or revising any content in the post:

1. Load `voice/constraints.md` — the 14 non-negotiables for any copy.
2. Load `voice/tone-and-style.md` — identity anchor and emotional range.
3. Load `voice/format-patterns.md` — the Insights section under "Personal brand site."
4. Identify the relevant pillar from `pillars/_pillar-map.md` and load that pillar file. Most Insights posts touch one or two pillars.

## Insights structural pattern

Per `voice/format-patterns.md`:

- **Title:** a claim, not a topic. Specific.
- **Opening:** no throat-clearing. First sentence makes a claim or names a specific observation.
- **Body:** argument with evidence. 800-1500 words. Same specificity discipline as a case study.
- **Closing:** a single observation that shifts how the reader thinks about the argument.

## Hard rules (canonical source: `voice/constraints.md`)

- No em dashes used as pauses. Use commas, periods, or parentheses.
- No hollow openings ("I'm excited to share," "In today's digital landscape").
- No hollow closings ("What do you think?", "Drop a comment below").
- Active voice with specific subjects and specific verbs.
- No corporate abstraction ("drive value," "leverage," "synergy").

## Before publish

Run the `humanizer` skill on the draft. It catches the AI-tell patterns that `voice/constraints.md` does not name explicitly.

## What stays out

- Do not edit the post template's HTML structure (head, nav, footer, JSON-LD) without a deliberate reason.
- Do not modify the page-specific `<style>` block in the post unless changing visual treatment.
- Do not put page-specific CSS in `css/styles.css` — keep it inline per `CLAUDE.md`.
