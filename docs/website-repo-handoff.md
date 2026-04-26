# Website Repo Handoff — Context for Claude

**Source repo:** `C:\JonathanOS\` (private — personal operating system)
**Target repo:** `CreateJonathanIbrahim/website-coming-soon` (public — GitHub Pages, custom CNAME)
**Stack as of 2026-04-26:** Static HTML/CSS/JS, fork of Start Bootstrap "Coming Soon" theme. No SSG, no build step.
**Purpose of this document:** Hand off the parts of JonathanOS that the website repo's Claude sessions need to do good work, without dragging over the parts that do not apply.

---

## 1. Public-Repo Boundary — Read This First

The website repo is **public**. Everything committed to it is publicly readable, including `CLAUDE.md`, any `.claude/rules/` files, any skills, and any docs.

This must be encoded into the website repo's `CLAUDE.md` as a hard rule. Suggested wording:

> This repository is public. GitHub Pages publishes from it. Anything committed here is world-readable. Before writing or editing any file in this repo, ask: would I be comfortable with this content visible on the open web? If the content is private (income context, job-search status, family details, client names under NDA, ClickUp workspace IDs, internal task notes), it does not belong in a committed file. Route private context to `CLAUDE.local.md` (gitignored) or keep it out of the repo entirely.

What this means in practice:

- **Safe to commit:** voice files, pillars, the cornerstone architecture doc, generic skills (e.g., `humanizer`), path-scoped rule patterns, hook patterns, public-facing copy.
- **Must stay out (or live in `CLAUDE.local.md` only):** ClickUp workspace/space/list IDs, current employment status, job-search context, specific client engagements not yet public, anything tagged in JonathanOS auto-memory as personal context.
- **`CLAUDE.local.md`** belongs in `.gitignore` from day one. It is the right home for any Claude context that needs to be machine-local.

---

## 2. Copy Verbatim

These files transfer cleanly because they are already designed as Layer 3 stable reference and do not contain private context.

### `voice/` (all three files)
- `constraints.md` — never-do-this list. Loads every session, for every piece of content, including website copy.
- `tone-and-style.md` — how Jonathan thinks and communicates.
- `format-patterns.md` — structural rules per content type. Will need a website-specific addition over time (page-level patterns differ from post/carousel patterns), but the existing file is the right starting point.

These are non-negotiable for any output that will sit on the public site under Jonathan's name. The website's `CLAUDE.md` must instruct Claude to load these before writing or editing copy.

### `pillars/` (all six files, plus `_pillar-map.md`)
- `web-design.md` — most directly relevant. Anchors any case-study, services-page, or insights-page copy.
- `project-management-systems.md`, `digital-marketing-operations.md`, `claude-code-architecture.md`, `clickup-architecture.md`, `personal-systems.md` — give Claude breadth for writing about adjacent topics on the site (Insights/blog, About page, services framing).

Pillars describe thematic territory, not templates. Copy them as-is.

### `docs/architecture/claude-code-architecture-cornerstone.md`
The 1,024-line architectural manual for Claude Code projects. Generic to any project. Copy whole. Reference it from the website's `CLAUDE.md` so future sessions know where the principles live.

---

## 3. Patterns to Adapt

These are not files to copy verbatim. They are conventions JonathanOS uses that the website repo benefits from re-implementing in scope.

### The `.claude/rules/` path-scoped pattern
JonathanOS uses path-scoped rule files that auto-load when Claude works in matching paths (e.g., `content-production.md` fires when Claude touches `voice/`, `pillars/`, `sources/`, `content/`). The website repo will benefit from analogous rules over time. Study `.claude/rules/content-production.md`, `post-content.md`, and `carousel-content.md` in JonathanOS as shape examples — same YAML frontmatter pattern with `paths:` glob, same second-person imperative voice, same under-200-line discipline.

### The `humanizer` skill
At `skills/humanizer/` in JonathanOS. Catches AI tells that constraints.md does not name explicitly (inflated significance, rule-of-three overuse, copula avoidance, etc.). Directly applicable to website copy. Copy the skill folder over once the website repo has a `skills/` directory.

### The `pre-bash-guard.py` hook pattern
At `.claude/hooks/pre-bash-guard.py` in JonathanOS. Blocks `rm -rf`, `git push --force`, Windows disk format, `del /f /s /q`. Every repo benefits from this. Copy the concept (and the script if compatible) as soon as the website repo has hooks wired up.

### Hard rules from JonathanOS `CLAUDE.md` worth restating
- File-write confirmation gate before writing or deleting any file (state path and change, wait for explicit yes).
- Plan before architectural changes (any task with more than three steps or that touches structure gets a plan first).
- Stop and report on unexpected state — do not improvise past unresolved conditions.
- Voice files load before any content production, every time.

---

## 4. Voice and Style — Hard Rules to Encode in `CLAUDE.md`

These are the rules that must travel even if voice files have not been loaded yet in a given session, because a single forgotten rule pollutes published copy on a public site.

- **No em dashes used as pauses.** Use commas, periods, or parentheses. Em dashes for ranges (2020–2024) are acceptable. This is the single most common AI tell in Jonathan's outputs and must be enforced at the `CLAUDE.md` level, not just buried in `constraints.md`.
- **Voice files load before any copy production.** `voice/constraints.md` first, then `voice/tone-and-style.md`, then `voice/format-patterns.md`, then the relevant pillar file, then the working file.
- **No hollow openings or closings.** No "I'm excited to share," "In today's digital landscape," "What do you think?", "Drop a comment below."
- **Active voice.** Specific subjects, specific verbs.
- **No corporate abstraction.** Replace "drive value," "move the needle," "leverage" with the specific thing being described.

The full list lives in `voice/constraints.md`. The four bullets above are the ones worth duplicating into `CLAUDE.md` for visibility, because they are the failure modes that most often slip past when a session forgets to load constraints.md.

---

## 5. Auto-Memory That Does Not Travel — Encode Here Instead

JonathanOS-side auto-memory is namespaced to that project and will not load in the website repo's Claude sessions. Items below are worth carrying over by encoding them into the website's `CLAUDE.md` (public-safe items) or `CLAUDE.local.md` (private items).

### Public-safe — encode in `CLAUDE.md`

**Who Jonathan is, sanitized for a public profile.** Operations and project leadership across web design, digital marketing, and AI/automation. Founded Electrician Metrics (2019). Led the web development team at The Get Smart Group (2020-2022) managing 30-40 concurrent websites. Coordinates cross-functional design, dev, and content teams. Sees production from inside, not above.

**Voice everywhere.** Every output surface — website copy, blog posts, case studies, even meta tags and image alt text — must carry Jonathan's voice. Load `voice/` files before any production. This is a hard constraint, not a guideline.

**No em dashes.** (Restated here because it is the most-violated rule and worth saying twice.)

**Employer-facing framing — tell the truth on outward artifacts.** When the site references prior employers, frame them accurately and in the past tense where applicable (e.g., "WISE Digital Partners, Feb 2025 to April 2026"). Do not misrepresent current status, current role, or tenure. The website is an outward-facing artifact — the same truthfulness rule applies.

### Private — encode in `CLAUDE.local.md` (gitignored)

Anything about current employment status, active job applications, in-flight client work that is not yet public, family context, or income paths under development belongs only in `CLAUDE.local.md`. Do not let any of this content reach a committed file in the website repo.

If `CLAUDE.local.md` does not yet exist in the website repo, create it on first need and add it to `.gitignore` in the same change.

---

## 6. ClickUp Task Conventions

ClickUp is JonathanOS's task layer. The website repo can wire into the same ClickUp workspace if Jonathan wants website-related work tracked there alongside everything else. The conventions below describe **how** tasks get created. The actual workspace/space/list IDs are private and must live in `CLAUDE.local.md` or environment variables, never in a committed file.

### When to create a task
Only on:
- Explicit ask from Jonathan ("log a task for X")
- A clear action item surfaced mid-session
- A produced deliverable that should be logged

Never speculatively. "This seems useful to track" is not a trigger.

### Task model
- **Parent task** = a deliverable (e.g., "Build About page," "Write Insights post on build-process redesign")
- **Subtask** = a significant step toward that deliverable, only when the step is worth tracking on its own
- One list. No folders, no separate lists per project, no ClickUp Docs/tags/chat
- Never post to ClickUp chat channels

### Write policy
Auto-create and auto-update freely. ClickUp operations override the general file-write confirmation rule from `CLAUDE.md` — no per-write confirmation needed. This applies only to ClickUp, not to repo files.

### Required custom field: `JonathanOS Category`
Every task sets this field. Existing options:
- `Content Pipeline` — sources, briefs, posts, carousels (LinkedIn-side)
- `Personal` — general life/work tasks outside content and projects
- `Project` — multi-step initiatives (most website work fits here)
- `Session Capture` — ad-hoc action items surfaced mid-session

If a task fits multiple categories, pick the one that best describes what closing it would mean. Check current options via `get_custom_fields` before creating — new options may be added.

### Source file path convention
When a task maps to a file in the repo (a page, a post, a script), include the repo-relative path in the task description:

> Source: `posts/build-process-redesign.md`

No custom field for this — description only.

### Status flow

| Status | When Claude sets it |
|---|---|
| `PLANNING` | Deliverable identified but not yet scoped into subtasks |
| `WAITING` | Has a ClickUp dependency set — automation unblocks to `TO DO` |
| `PREPPED` | Has a real start date — automation promotes to `IN PROGRESS` at T-1h |
| `TO DO` | Ready to work, no date, no blocker |
| `IN PROGRESS` | Do not auto-set. Automations or Jonathan own this transition |
| `ON HOLD` | Voluntarily paused (distinct from `WAITING`) |
| `NEED TO REVIEW` | Jonathan asked for eyes before closing |
| `COMPLETE` | Terminal. Default target for all task closures |
| `UNBLOCK DEPENDENCY` | Never set unless Jonathan explicitly instructs. His manual marker for "complete enough to unblock the next task" |

### Session captures
Action items that surface mid-session:
1. If there is an obvious fit under an existing open parent task → create a subtask there with `JonathanOS Category = Session Capture`.
2. Otherwise → create a top-level parent task with `JonathanOS Category = Session Capture`.

### Default behaviors
- **Priority:** leave blank. Do not infer.
- **Tags:** never set.
- **Reminders:** never create unless explicitly asked.
- **Time tracking:** when Jonathan closes a session tied to a task, log a time entry for the session duration against that task.
- **Session start:** do not fetch open tasks automatically. Only pull on explicit request.

### Ignored fields
- `Calendar Date` — Jonathan uses this manually for a calendar-view workaround.
- `BASELINE_*` (start_date, duration, status, due_date) — ClickUp's native baselines feature, owned by ClickUp.

### Where the IDs live
The workspace ID, space ID, and list ID are operational secrets for the public repo's purposes — not because they are credentials, but because they are noise no public reader should see. Put them in `CLAUDE.local.md` under a "ClickUp" heading, or in `.claude/settings.local.json` env vars referenced as `${CLICKUP_LIST_ID}` etc. Never in a committed file.

---

## 7. What NOT to Bring

The following parts of JonathanOS do not belong in the website repo. They either reference systems the website does not interact with, or they encode private context that conflicts with the public-repo boundary.

- **Vault access rules and the vault itself** — `Deep Knowledge Base/` is a separate Obsidian repo. Not relevant to website work.
- **`.claude/rules/vault-access.md`, `source-intake.md`, `content-production.md`, `post-content.md`, `carousel-content.md`** — LinkedIn-content-specific. Their *shape* is worth studying (Section 3), but copying the files themselves drags in vocabulary that does not apply.
- **`sources/` and `content/` folders** — LinkedIn pipeline working directories.
- **Job application skills** — `jonathan-position-evaluator`, `jonathan-resume-customizer`, `jonathan-cover-letter-writer`. Private context.
- **`skills/youtube-transcript`, `skills/obsidian-markdown`, `skills/paulette-caption-writer`** — vault- or LinkedIn-specific. Skip.
- **`skills/caveman`** — token-compression dialogue mode. Optional, not necessary for website work.
- **Project memory items from JonathanOS auto-memory tagged as personal context** — phase state, current employment, in-flight engagements, application/interview tracking. Stays in JonathanOS auto-memory and `CLAUDE.local.md`; does not travel into committed files.

---

## 8. Open Questions for Jonathan

Things this handoff document cannot resolve without input — flag at the start of the website-repo migration session:

1. **Static stack will stay HTML/CSS/JS, or migrate to a SSG?** Current state is plain static. If a Jekyll or Astro migration is on the roadmap, voice file loading and folder layout decisions change. If staying static, no decision needed.
2. **ClickUp wired in, yes or no?** Two valid choices: (a) keep all task tracking in JonathanOS, surface website work there; (b) wire ClickUp MCP into the website repo too with IDs in `CLAUDE.local.md`. Pick one before the first task gets logged.
3. **First voice audit.** The current `index.html` in the website repo is mostly fork-default theme content. Worth a one-time pass after voice files land: read the page through `voice/constraints.md` and flag anything that violates the rules, before adding new copy on top of unchecked baseline.

---

## 9. Source Anchors

When in doubt, the canonical source for any rule referenced above lives at one of these paths in JonathanOS:

- Architecture: `docs/architecture/claude-code-architecture-cornerstone.md`
- Voice: `voice/constraints.md`, `voice/tone-and-style.md`, `voice/format-patterns.md`
- Pillars: `pillars/[name].md`, `pillars/_pillar-map.md`
- ClickUp conventions: `.claude/rules/clickup-integration.md`
- Vault rules (reference for shape, not content): `.claude/rules/vault-access.md`
- Master orientation pattern: `CLAUDE.md`

This document is the bridge. The cornerstone doc is the manual. The voice files are the constraint. Everything else flows from those three.
