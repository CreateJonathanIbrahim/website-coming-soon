# Changelog

All notable changes to this project are documented here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) adapted for [CalVer](https://calver.org/) versioning (`YYYY.MM.DD`). See the changelog policy section in [CLAUDE.md](CLAUDE.md) for what gets logged and when.

## [Unreleased]

> Tracking work on `dev` toward the next deploy to `master`. Versions get cut and dated when work reaches master.

### SETUP-1 — Public-repo boundary (COMPLETE — 2026-04-26)

**Added**
- `CLAUDE.local.md` (gitignored) for private operational context — ClickUp IDs, employment, family, in-flight client work
- Public-repo boundary rule in `CLAUDE.md` (verbatim from `docs/website-repo-handoff.md` §1)
- `.gitignore` patterns: `CLAUDE.local.md`, `*.local.md`, `.claude/settings.local.json`, `.env*`, `*.log`

**Changed**
- `README.md` line 3: removed present-tense employment leak; replaced with 14-year operations leader framing matching `index.html` meta description
- `docs/copywriting-guidelines.md`: removed stealth-mode bullet, Target Audience section, current-employer line, family names; flagged `voice/constraints.md` as canonical pending DECISION-6
- `docs/website-repo-handoff.md` line 187: sanitized specific company/state names; replaced with generic "private context" reference

**Removed**
- `docs/architecture.md` — JonathanOS architecture doc that did not belong in this public repo (was untracked; never committed)
- `docs/launch-handoff.md` — content moved to `CLAUDE.local.md` archive section (was untracked; never committed)

Commits: `f8ffe0e`, `add7078`

### SETUP-5 — Changelog and changelog policy (COMPLETE — 2026-04-26)

**Added**
- This `CHANGELOG.md` file
- Changelog Policy section in `CLAUDE.md`

### ClickUp task list — `JonathanIbrahim.com` (COMPLETE — 2026-04-26)

**Added**
- 31 tasks created in the `JonathanIbrahim.com` ClickUp list under the JonathanOS space: 5 SETUP parents, 6 DECISION parents, 8 WORKSTREAM parents, 12 subtasks under WS-6 (Insights voice rewrites) and WS-7 (Case studies)
- All tasks default to `PLANNING` status; statuses follow JonathanOS handoff §6 conventions

### SETUP-2 — Voice / pillars / cornerstone migration (IN PROGRESS)
- `voice/` (3 files: `constraints.md`, `tone-and-style.md`, `format-patterns.md`), `pillars/` (7 files: `_pillar-map.md` plus 6 pillar themes), and `docs/claude-code-architecture-cornerstone.md` staged in working tree (untracked); commit pending integration with `CLAUDE.md` voice loading rules and the four hard rules from `docs/website-repo-handoff.md` §4

### SETUP-3 — Humanizer skill, pre-bash-guard hook, path-scoped rules (IN PROGRESS)
- `.claude/skills/caveman/` and `.claude/skills/humanizer/` staged in working tree (untracked); pre-bash-guard hook and `.claude/rules/` directory not yet started

### SETUP-4 — Pre-launch baseline tag (NOT STARTED)
- Will tag `master` as `pre-launch-2026-04-26` for rollback safety before the dev → master merge

### DECISION-1 through DECISION-6 (NOT STARTED)
- Six pre-launch decisions scoped in ClickUp: CSS strategy, OG image strategy, hero copy, home carousel posture, Insights category redefinition, copywriting/voice reconciliation. Resolutions gate downstream workstreams.

### WS-1 through WS-8 (SCOPED, NOT STARTED)
- Eight workstreams scoped with checklists in ClickUp: CSS architecture rebuild, linking integrity sweep, imagery/assets, copy/content fixes + first voice audit, Insights archive restructure, Insights voice rewrites (5 posts + 1 planning subtask), 3 case studies, SEO infrastructure + pre-merge verification

---

## Tags and Versioning

- **CalVer scheme:** `YYYY.MM.DD` matching the date the version was cut
- **Versions are cut at deploys.** When work reaches `master`, the relevant `[Unreleased]` content gets renamed to `[YYYY.MM.DD]` and a fresh `[Unreleased]` block is started
- **Pre-launch baseline tag:** `pre-launch-2026-04-26` (will be created in SETUP-4) — reserved for one-command rollback if a launch breaks something on production
