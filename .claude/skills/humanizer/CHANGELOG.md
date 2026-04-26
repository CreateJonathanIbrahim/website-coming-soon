# Changelog — humanizer skill

All notable changes to the humanizer skill are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Versions follow [Semantic Versioning](https://semver.org/).

---

## [1.0.0] — 2026-04-23

Initial release in `skills/`. Merged from two prior versions in `skills-to-review/Combine or Heavy Edit/`:

- `humanizer/` (v1.0.0, WISE Content Engine variant) — richer pattern catalog with before/after examples.
- `ai_humanizer/` (v2.5.1, generic standalone variant) — stronger personality-and-soul guidance.

### Added

- `SKILL.md` — executable spec wired to JonathanOS voice files (`voice/constraints.md`, `voice/tone-and-style.md`, `voice/format-patterns.md`). Invoked via `Humanize this draft` or `Humanize [path]`.
- `references/patterns.md` — full 29-pattern catalog (Wikipedia "Signs of AI Writing," WikiProject AI Cleanup) with detection cues, problem descriptions, fix guidance, and before/after examples.
- Six-step process: read → pattern scan + rewrite → soul check → self-diagnostic audit → write revised file → report.
- Voice calibration tied to `voice/` files rather than a per-client brand guide. Applies the stance delta from `format-patterns.md` for the target surface (LinkedIn, site, resume, cover letter, outreach, refined notes).
- Self-diagnostic audit loop: "What still makes this sound AI-generated?" → list → "Now make it not sound AI-generated" → revise.
- Personality and Soul section: guards against sterile voiceless prose that passes the pattern scan but still reads as machine output.
- Edge-case handling: missing files, missing voice files, code blocks, schema markup, raw source files, and re-runs on already-humanized files.

### Dropped from the WISE variant (not applicable to JonathanOS)

- Brand-guide-driven voice calibration. Voice files handle this.
- Pipeline-orchestrator "Task C" inline mode. No pipeline orchestrator in JonathanOS at this time.
- Batch-processing-all-client-copy mode. Single-file only.
- Appending a Humanizer Log section to the file. Report stays in chat by default.

### Source

[Wikipedia: Signs of AI Writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), maintained by WikiProject AI Cleanup.
