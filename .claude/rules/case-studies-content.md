---
description: When editing or creating a case study, load voice files, the web-design pillar, and verify employer/client framing rules.
paths:
  - "case-studies/**/*.html"
---

# Case study production

You are editing or creating a case study. Before writing or revising:

1. Load `voice/constraints.md`.
2. Load `voice/tone-and-style.md`.
3. Load `voice/format-patterns.md` — the "Case studies" section under "Personal brand site."
4. Load `pillars/web-design.md` (most case studies are web-design or PM/ops projects). Add `pillars/clickup-architecture.md` or `pillars/project-management-systems.md` if relevant to the project being documented.
5. Check `CLAUDE.local.md` for client-attribution rules, NDA constraints, and current-employer framing.

## Case study structural pattern

Per `voice/format-patterns.md`:

- **Headline:** the outcome in one sentence, with the metric.
- **Context:** company, industry, scale, the problem at the start.
- **The decision:** what Jonathan chose to do and why, including what he chose not to do.
- **The system:** the specific mechanism he built. Screenshots, diagrams, or concrete examples where possible.
- **What changed:** before/after with real numbers. No vanity metrics.
- **What he would do differently:** one honest reflection.

Length: 800-1500 words.

## Hard rules (canonical source: `voice/constraints.md`)

- No em dashes as pauses.
- No hollow openings or closings.
- Active voice.
- No corporate abstraction.
- **Truthful framing rule** (per `docs/website-repo-handoff.md` §5): reference any past or current employer accurately, in past tense where applicable. Do not name current employer's clients in a way that signals departure intent.

## Before publish

- Run the `humanizer` skill on the draft.
- Verify employer/client attribution against `CLAUDE.local.md` constraints.
- Confirm with Jonathan before merging. Case studies require explicit sign-off.
