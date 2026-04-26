# Project Context — Jonathan Ibrahim Professional Site

## 🔒 Public Repository Boundary

This repository is public. GitHub Pages publishes from it. Anything committed here is world-readable. Before writing or editing any file in this repo, ask: would I be comfortable with this content visible on the open web? If the content is private (income context, job-search status, family details, client names under NDA, ClickUp workspace IDs, internal task notes), it does not belong in a committed file. Route private context to `CLAUDE.local.md` (gitignored) or keep it out of the repo entirely.

## 🤖 Agent Behavior & Directives

- **Direct Output:** Keep explanations extremely brief. Output code directly without apologies, filler language, or conversational fluff.
- **Voice (canonical):** `voice/` files are canonical for any copy produced under Jonathan's name. Load order before writing or editing copy: `voice/constraints.md` → `voice/tone-and-style.md` → `voice/format-patterns.md` → the relevant pillar from `pillars/` (use `pillars/_pillar-map.md` to identify which pillar applies). Run the `humanizer` skill on drafts before publish.
- **Voice — four non-negotiables** (canonical source: `voice/constraints.md`): no em dashes as pauses; no hollow openings or closings; active voice with specific subjects and verbs; no corporate abstraction.
- **Architecture Reference:** `docs/claude-code-architecture-cornerstone.md` is the architectural manual for Claude Code projects (CLAUDE.md design, hooks, rules, skills/agents, layer hierarchy). Load on demand for architecture decisions.
- **Private Context:** Audience framing, current employment, family details, and in-flight client work live in `CLAUDE.local.md` — never in committed files.
- **Preserve Structure:** Do not remove existing comments, HTML structure, or utility classes when editing files unless explicitly requested.
- **Verification:** Run a final read of all modified files to check for syntax errors before declaring a task complete.

## 🏗️ Tech Stack & Constraints

- **Core:** HTML5 + CSS3 + Vanilla JS (no frameworks like React or Vue).
- **Styling:** Bootstrap 5.2.3 local + custom site styles (split into a vanilla Bootstrap base file and a `site.css` for theme overrides plus shared rules — see WS-1 implementation in CHANGELOG).
- **Typography:** Google Fonts (**Varela Round** for headings/labels, **Nunito** for body).
- **Icons:** Font Awesome 6.3.0.
- **Infrastructure:** GitHub Pages deployment (static files only). No bundler, no backend, no environment variables, no database.

## 🎨 Design Philosophy & System

**Core Principle:** Dark, sophisticated, professional. Monochromatic look with a teal accent. No light mode.

**Colors:**

- Accent (Teal): `#64a19d` (links, badges, borders, primary highlights)
- Background Dark: `#050505`, `#0d0d0d`, `#000`
- Text: `#fff`, `#ddd`, `#aaa`
- Borders/Dividers: `#1a1a1a`, `#222`, `#333`

**Styling Conventions:**

- **Global CSS:** Base styles and Bootstrap variable overrides (`--bs-*`) live in `css/styles.css`.
- **Page-Specific CSS:** Must be placed in `<style>` tags inside the specific HTML file's `<head>`. Do not put page-specific rules in the global stylesheet.
- **Typography:** Responsive scale via `clamp(min, preferred-vw, max)` on headings.
- **Animations:** Smooth CSS transitions on hovers; bounce animation on scroll chevrons; fade-in on scroll via IntersectionObserver (`.fade-in-section` / `.is-visible`).

## 📂 File Map

    index.html          Hero/landing, About snippet, Expertise, Track Record, Timeline, Connect
    about.html          Biography, Origin Story, Values, Hobbies
    case-studies.html   Archive — CSS Grid 12-col bento layout + filter pills
    insights.html       Blog archive — magazine layout, sticky category nav, dot-grid
    case-studies/
      case-study-template.html    Template for individual case study pages
    insights/
      post-template.html      Template for individual blog posts
    css/styles.css      Bootstrap 5.2.3 base + global custom styles ONLY
    css/custom.css      Page-specific or experimental overrides (untracked; do not move rules here unless intentional)
    js/scripts.js       Navbar fade/shrink + ScrollSpy + IntersectionObserver logic
    assets/             Images, headshots, resume PDF, favicon
    voice/              Canonical voice files — constraints, tone-and-style, format-patterns
    pillars/            Six thematic territories + _pillar-map.md (load relevant pillar before content production)
    docs/
      claude-code-architecture-cornerstone.md   Architecture reference (load on demand)
      design-system.md                          Full design system reference
      seo-metadata-template.md                  SEO/OG/Twitter/JSON-LD boilerplate
      website-repo-handoff.md                   JonathanOS handoff context for this repo
    .claude/
      hooks/pre-bash-guard.py                   PreToolUse hook blocking destructive commands
      rules/                                    Path-scoped rules (auto-load when editing matching paths)
      settings.json                             Claude Code settings (hooks, permissions)
      skills/                                   22 skills (impeccable design pack + caveman + humanizer + seo + seo-audit)

## 📋 Common Tasks (SOPs)

### Add a New Blog Post

1. Duplicate `insights/post-template.html` → rename to `insights/post-slug.html`.
2. Update `<title>`, meta description, `og:title`, `og:description`, and `og:image`.
3. Update article header: title, date, category badge, read time.
4. Load `voice/` files (constraints → tone-and-style → format-patterns → relevant pillar from `pillars/`), then author content inside the `<article>` section.
5. Run the `humanizer` skill on the draft before publish.
6. Add the corresponding card to `insights.html` under the correct category section.

### Add a New Case Study

1. Duplicate `case-studies/case-study-template.html` → rename to `case-studies/client-name.html`.
2. Update meta tags (`title`, `description`, `og:*`).
3. Update hero: client name, tagline, stats, background image.
4. Load `voice/` files (constraints → tone-and-style → format-patterns → relevant pillar from `pillars/`), then author the case study sections.
5. Run the `humanizer` skill on the draft before publish.
6. Add the corresponding card to `case-studies.html` bento grid (select appropriate slot size).

### Create a Top-Level Page

1. Create `page-name.html` at the root directory.
2. Copy the nav + footer structure from an existing top-level page.
3. Add a `<link>` to the nav across all existing pages.
4. Test mobile responsiveness at 375px, 768px, and 1024px.

## ⚙️ JavaScript & SEO Rules

- **Behavior (`js/scripts.js`):** Handles navbar fade-in (2s delay or scroll > 50px), navbar shrink (`.navbar-shrink`), Bootstrap ScrollSpy, and auto-closing mobile collapse navs.
- **SEO Requirements:** Full OpenGraph + Twitter Card tags on all pages. Ensure JSON-LD `Person` schema remains intact on `index.html`.

## 🪝 Hooks and Path-Scoped Rules

- **Hook (`.claude/hooks/pre-bash-guard.py`):** Wired into PreToolUse via `.claude/settings.json` with matchers `Bash|PowerShell`. Blocks unambiguously destructive shell commands: `rm -rf` on root/home/wildcards/system paths, `git push --force` without `--force-with-lease`, `git reset --hard`, Windows `format`/`del /f /s`/`rd /s /q`, `dd`/`mkfs` disk writes, `chmod 777` on system paths. Day-to-day deletions of specific files inside the repo are not blocked. To bypass for an intentional case, run the command in a separate terminal outside Claude Code.

- **Path-scoped rules (`.claude/rules/`):** Each rule file has YAML frontmatter with `paths:` glob patterns. When you are editing files matching a rule's glob, read the rule before making changes. Current rules:
    - `.claude/rules/insights-content.md` — fires for `insights/**/*.html`. Voice file load order, structural pattern, hard rules, humanizer requirement.
    - `.claude/rules/case-studies-content.md` — fires for `case-studies/**/*.html`. Voice + web-design pillar load, employer-framing rules, humanizer requirement.

  Add new rule files under `.claude/rules/` as new content surfaces emerge.

## 📜 Changelog Policy

The site has an active [`CHANGELOG.md`](CHANGELOG.md) at the repo root. Update it as work progresses — do not let it drift.

**Format:** [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) adapted for [CalVer](https://calver.org/) (`YYYY.MM.DD`). Categories used: Added, Changed, Deprecated, Removed, Fixed, Security.

**What gets logged:**

- Every workstream-level outcome (e.g., "WS-1: CSS architecture rebuild — Bootstrap moved to CDN, site.css consolidated")
- Every decision resolution (e.g., "DECISION-1 resolved: option B")
- Every voice rewrite of an Insights post (one entry per post)
- Every case study published
- Structural infrastructure changes (gitignore, hook patterns, rule files, build pipeline)

Per-task detail lives in ClickUp task descriptions. Per-file detail lives in commit messages. The changelog is the workstream-level layer between them.

**When versions get cut:**

- Cut a `[YYYY.MM.DD]` version when work reaches `master` (i.e., dev → master merge)
- Until then, all in-flight work lives under `[Unreleased]`
- The date IS the version. Add a one-line subtitle for milestones (e.g., `## [2026.06.15] — Initial launch`)

**Workflow:**

1. As you complete a meaningful chunk of work, add an entry to `[Unreleased]` under the appropriate workstream (or category, for cross-cutting work).
2. When merging to master, rename `[Unreleased]` → `[YYYY.MM.DD]` and start a new empty `[Unreleased]` block.
3. Prefer separate commits for changelog updates when feasible (e.g., "Changelog: WS-2 linking sweep complete").
