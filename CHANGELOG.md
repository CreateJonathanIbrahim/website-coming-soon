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

### SETUP-2 — Voice / pillars / cornerstone migration (COMPLETE — 2026-04-26)

**Added**
- `voice/` (3 files): `constraints.md` (14 non-negotiables), `tone-and-style.md` (identity, emotional range, anti-references), `format-patterns.md` (site-scoped structural guidance)
- `pillars/` (7 files): `_pillar-map.md` plus pillar themes for project-management-systems, digital-marketing-operations, claude-code-architecture, web-design, clickup-architecture, personal-systems
- `docs/claude-code-architecture-cornerstone.md` (1023-line architecture reference, load on demand)
- `docs/website-repo-handoff.md` (sanitized in SETUP-1; tracked here)
- `CLAUDE.md` Agent Behavior section: new `Voice (canonical)` directive with load order, `Voice — four non-negotiables` bullet, `Architecture Reference` and `Private Context` bullets

**Changed**
- `pillars/_pillar-map.md`: removed "Active weighting (temporary, 2026-04)" section that referenced active job search (public-repo boundary violation)
- `voice/format-patterns.md`: scoped to personal brand site only — removed LinkedIn carousel/post, when-to-choose, resume, cover letter, and outreach email sections (those surfaces are out-of-scope for this repo; their guidance lives in JonathanOS)
- `CLAUDE.md` File Map: added voice/, pillars/, docs/ entries with one-line descriptions
- `CLAUDE.md` SOPs (Add a New Blog Post, Add a New Case Study): updated to load voice/ files; added humanizer skill step before publish; numbered to 6 steps each
- `README.md`: updated File Map and Documentation sections; updated both SOPs to load voice/ files instead of `docs/copywriting-guidelines.md`

**Removed**
- `docs/copywriting-guidelines.md` — superseded by `voice/` files. The voice files are canonical per JonathanOS handoff §2; this resolves DECISION-6 (em-dash conflict) in favor of `voice/constraints.md`

### SETUP-3 — Humanizer skill, pre-bash-guard hook, path-scoped rules (COMPLETE — 2026-04-26)

**Added**
- `.claude/skills/caveman/` and `.claude/skills/humanizer/` (migrated from JonathanOS)
- `.claude/hooks/pre-bash-guard.py` — Python PreToolUse hook that blocks unambiguously destructive shell commands. Tested against 7 cases (rm -rf /, rm -rf ~, git push --force, git push --force-with-lease, git reset --hard, rm -rf node_modules, ls -la); blocks 4 dangerous, allows 3 safe
- `.claude/settings.json` — wires pre-bash-guard into PreToolUse with matchers `Bash|PowerShell`
- `.claude/rules/insights-content.md` — path-scoped rule for `insights/**/*.html`. Voice file load order, Insights structural pattern from `voice/format-patterns.md`, hard rules, humanizer requirement
- `.claude/rules/case-studies-content.md` — path-scoped rule for `case-studies/**/*.html`. Voice + web-design pillar load, employer-framing rules per `docs/website-repo-handoff.md` §5, humanizer requirement
- `🪝 Hooks and Path-Scoped Rules` section in `CLAUDE.md` documenting the hook, current rules, and the path-scoped rules pattern

**Removed**
- `.agents/` directory (entire mirror of `.claude/skills/`). Single source of truth at `.claude/skills/` going forward. If a non-Claude-Code runtime ever needs the skills, regenerate the mirror from `.claude/skills/` at that time.

**Changed**
- `CLAUDE.md` File Map: added `.claude/hooks/`, `.claude/rules/`, `.claude/settings.json`, `.claude/skills/` entries
- `README.md` Impeccable Agents skill pack section: removed mirror language, points at `.claude/skills/` only
- `README.md` File Map: replaced `.agents/skills/` and `.claude/skills/` mirror lines with the four `.claude/` entries (skills, hooks, rules, settings)

**Patterns blocked by pre-bash-guard:**

- `rm -rf` targeting root, home directory, wildcards, or single-segment system paths (`/usr`, `/etc`, `/var`, etc.)
- `git push --force` / `-f` without `--force-with-lease`
- `git reset --hard` (any args)
- Windows `format <drive>:`, `del /f /s`, `rd /s /q`
- `dd` writing to `/dev/sd*`, `/dev/nvme*`, etc.
- `mkfs.*` filesystem creation
- `chmod 777` on root or system paths

`rm -rf` of specific repo paths (node_modules, dist, etc.) is not blocked.

### SETUP-4 — Pre-launch baseline tag (COMPLETE — 2026-04-26)

**Added**
- Local git tag `pre-launch-2026-04-26` pointing at `master` HEAD (`9d1d84d` — "Update README.md", 2026-04-22). Reserved for one-command rollback if a future launch breaks something on production. Tag is local until pushed via GitHub Desktop.

### DECISION-1 through DECISION-6 (NOT STARTED)
- Six pre-launch decisions scoped in ClickUp: CSS strategy, OG image strategy, hero copy, home carousel posture, Insights category redefinition, copywriting/voice reconciliation. Resolutions gate downstream workstreams.

### WS-1 through WS-8 (SCOPED, NOT STARTED)
- Eight workstreams scoped with checklists in ClickUp: CSS architecture rebuild, linking integrity sweep, imagery/assets, copy/content fixes + first voice audit, Insights archive restructure, Insights voice rewrites (5 posts + 1 planning subtask), 3 case studies, SEO infrastructure + pre-merge verification

---

## Tags and Versioning

- **CalVer scheme:** `YYYY.MM.DD` matching the date the version was cut
- **Versions are cut at deploys.** When work reaches `master`, the relevant `[Unreleased]` content gets renamed to `[YYYY.MM.DD]` and a fresh `[Unreleased]` block is started
- **Pre-launch baseline tag:** `pre-launch-2026-04-26` — points at `master` HEAD (`9d1d84d`, 2026-04-22). Reserved for one-command rollback if a launch breaks something on production. Created locally on 2026-04-26; push to origin via GitHub Desktop when convenient.
