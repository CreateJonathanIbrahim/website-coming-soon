---
name: humanizer
version: 1.0.0
description: >
  Pre-publish pass that removes AI-writing patterns from a draft. Reads the
  file, scans for 29 patterns documented in Wikipedia's "Signs of AI Writing"
  guide (significance inflation, copula avoidance, superficial -ing phrases,
  filler, rule of three, synonym cycling, em dash overuse, and more),
  rewrites in Jonathan's voice for the target surface, runs a soul check,
  and performs a self-diagnostic audit. Invoke via "Humanize this draft"
  or "Humanize [path]" on any completed content piece before publish.
allowed-tools:
  - Read
  - Edit
  - Write
  - Glob
  - Grep
---

# humanizer — pre-publish AI-tell removal

Runs on a completed draft as the final gate before publishing. Reads the file, identifies AI-writing patterns, rewrites in Jonathan's voice for the target surface, and reports what changed.

Based on Wikipedia's "Signs of AI Writing" guide (WikiProject AI Cleanup). Twenty-nine documented patterns, all rooted in the same cause: LLMs regress to the statistically most likely output for the widest variety of cases, trading specificity for generic probability.

Use humanizer only on already-drafted content. It is not a drafting tool.

---

## Trigger phrases

- `Humanize this draft`
- `Humanize [file path]`
- `Polish this content`
- `Run humanizer on [file path]`

---

## When to invoke

- On any completed content piece before publish: LinkedIn post or carousel drafts, personal brand site copy, case studies, cover letters, outreach emails, refined Obsidian notes.
- Never on first-draft work in progress. Let the draft land first, then humanize.
- Never on source files in `sources/` or `sources/raw/`. Those are raw material, not outputs.

---

## Voice calibration (required)

Before rewriting, load in this order:

1. `voice/constraints.md` — the 14 non-negotiables.
2. `voice/tone-and-style.md` — identity anchor, emotional range, anti-references, triangulation point.
3. `voice/format-patterns.md` — surface-specific stance table plus the detailed pattern for the target surface.

If the file being humanized is tied to a specific surface (cover letter, resume, LinkedIn post), apply the stance delta from `format-patterns.md` for that surface. The goal is Jonathan's voice, not a generic human voice.

---

## Process

### Step 1 — Read the file

Identify and section off:

- YAML frontmatter (skip during pattern scan; preserve verbatim).
- Body prose (headings, paragraphs, bullets).
- Tables, callouts, code blocks, schema markup, and JSON-LD (skip during scan; preserve verbatim).
- Any existing Humanizer Log from a prior run (leave it in place; do not duplicate).

### Step 2 — Pattern scan and rewrite

Walk the body section by section. For each pattern found, rewrite in place before moving on. Do not collect-then-fix. Fix as you go.

For each fix:

- Preserve the core meaning and all specific facts, numbers, and named entities.
- Match Jonathan's voice for the target surface, not a generic voice.
- Use "is," "are," "has" wherever you remove a copula substitute.
- When a vague claim cannot be made specific from the material present, cut the sentence entirely. Do not manufacture specificity.

See `references/patterns.md` for the full pattern catalog with detection cues, before/after examples, and fix guidance.

### Step 3 — Soul check

Removing all 29 patterns is half the job. Sterile voiceless prose is still AI-detectable.

Ask: does this read like Jonathan writing, or like a clean report?

Signs of soulless writing even when technically pattern-clean:

- Every sentence is the same length and structure.
- Neutral reporting with no direct assertion.
- No rhythm variation.
- No stance. A list of facts instead of a claim.
- Reads like a Wikipedia summary rather than a practitioner speaking from experience.

Add voice without breaking `constraints.md`:

- Vary rhythm deliberately. Short sentences after long ones.
- State positions directly. "This matters because X" beats "Some might argue X could be relevant."
- Use specific outcomes. "Bounce rate dropped 22% in 30 days" beats "results improved."
- Let Jonathan's experience speak. He knows things because he built them. Let him say so.

### Step 4 — Self-diagnostic audit

1. Internally prompt: **"What still makes this sound AI-generated?"**
2. List remaining tells (internal, not written to the file).
3. Internally prompt: **"Now make it not sound AI-generated."**
4. Revise those specific passages.

This loop catches rhythm, structural uniformity, and the absence of a human behind the words. Issues that do not fit neatly into any of the 29 categories.

### Step 5 — Write the revised file

Overwrite the source file with the humanized version.

Preserve:

- YAML frontmatter (exact).
- Code blocks, tables, schema markup, JSON-LD (verbatim, never altered).
- Internal link anchors and format.
- Word count within ±10% of original. Meaning is the target, not length.

Do not add:

- New facts, numbers, examples, or claims not present in the original.
- Links that were not there.
- Sections that were not in the original structure.

### Step 6 — Report to the user

In-chat report (not written to the file), structured as:

- **Patterns found:** brief list with pattern name and where it appeared.
- **Fixes applied:** summary, not a per-change diff. The user can diff the file directly.
- **Self-diagnostic audit:** what the final pass caught and revised.
- **Verdict:** Pass or Needs Review.
  - **Pass** = no obvious AI tells remain. Reads as Jonathan's writing for the target surface.
  - **Needs Review** = one or more patterns could not be fully resolved (vague claim lacking source material, structural issue needing rewrite, etc.). List the specific items needing human attention.

---

## Edge cases

- **File not found.** Report the path and stop. Do not create the file.
- **Voice files missing or not loaded.** Stop and surface the gap. Do not substitute a generic voice.
- **Code blocks, JSON-LD, schema markup.** Skip entirely. Never alter.
- **Raw source file (path is under `sources/raw/` or `sources/`).** Stop and redirect. Humanizer runs on outputs, not inputs.
- **Already-humanized file (prior Humanizer Log present).** Treat as a second-pass audit. Run the full process; skip appending a duplicate log.

---

## Reference

Full pattern catalog: `references/patterns.md`

Source: [Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup)
