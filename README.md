# Jonathan Ibrahim — Professional Site

Personal website for Jonathan Ibrahim, Strategic Operations Leader with 14 years building delivery infrastructure for growth-stage companies.

**Live at:** [jonathanibrahim.com](https://jonathanibrahim.com)
**Current branch:** `dev` — staging for the next production deploy.

---

## 🚀 What's New on `dev`

This branch is a substantial expansion over `master`. Three major pushes landed here:

1. **Content expansion** — added a full About page, a Case Studies bento archive, and an Insights (blog) archive with five published posts.
2. **Impeccable Agents integration** — a full skill pack for AI-assisted design and engineering (`.agents/skills/` + `.claude/skills/`), a project-level design brief ([.impeccable.md](.impeccable.md)), and three new docs covering copywriting, design system, and SEO metadata.
3. **Homepage overhaul** — [index.html](index.html) was rewritten to include a refined hero, About snippet, Expertise, Track Record, Timeline, and Connect sections.

Supporting changes:

- The legacy Pug + SCSS build pipeline (`src/pug/`, `src/scss/`, and every `scripts/build-*` / `scripts/render-*` helper) was removed. The site is now genuinely static — no bundler, no preprocessor.
- CSS was reorganized into a global [css/styles.css](css/styles.css) and an overrides-only [css/custom.css](css/custom.css).
- New brand assets: `Jonathan_Ibrahim_Headshot_2026.jpg`, `Jonathan_Ibrahim_Social_Media_Preview.jpg` (+ `.webp`), and `apple-touch-icon.png`.

---

## 🏗️ Architecture & Stack

Deliberate simplicity. No build pipeline, no bundler, no framework.

- **Frontend:** Vanilla HTML5, CSS3, and JavaScript
- **Styling:** Bootstrap 5.2.3 (via CDN) + custom CSS
- **Typography:** Google Fonts — **Varela Round** (headings/labels), **Nunito** (body)
- **Icons:** Font Awesome 6.3.0
- **Hosting:** GitHub Pages (static only)
- **Dependencies:** `package.json` pins Bootstrap 5.2.3 for reference; there is no install/build step required to run the site.

---

## 📂 File Map

### Top-level pages

    index.html             Hero, About snippet, Expertise, Track Record, Timeline, Connect
    about.html             Biography, Origin Story, Values, Hobbies
    case-studies.html      Archive — 12-col CSS Grid bento layout + filter pills
    insights.html          Blog archive — magazine layout, sticky category nav, dot-grid

### Case studies

    case-studies/
      case-study-template.html    Template for individual case study pages

### Insights (blog)

    insights/
      post-template.html                           Template for new posts
      clickup-hierarchy-explained.html             Published post
      freelancer-to-agency-side.html               Published post
      onboarding-process-that-doesnt-leak.html     Published post
      seo-2026-small-service-businesses.html       Published post
      the-discovery-process.html                   Published post

### Styles, scripts, assets

    css/styles.css         Global styles + Bootstrap variable overrides (only)
    css/custom.css         Page-specific or experimental overrides
    js/scripts.js          Navbar fade/shrink, ScrollSpy, IntersectionObserver fade-ins
    assets/                Headshots, social preview images, resume PDF, favicons

### Agent & documentation layer

    CLAUDE.md              Architectural constraints, design system, SOPs for AI agents
    .impeccable.md         Design brief — users, brand voice, aesthetic direction, principles
    skills-lock.json       Pinned skill versions for the Impeccable Agents pack
    .agents/skills/        Impeccable Agents skill modules (20+ skills)
    .claude/skills/        Same skill pack, surfaced for Claude Code
    docs/
      copywriting-guidelines.md    Tone, audience, biographical facts — read before writing copy
      design-system.md             Colors, typography, components, patterns
      seo-metadata-template.md     Canonical SEO/OG/Twitter/JSON-LD metadata patterns

---

## 🤖 AI-Assisted Development

This repository is intentionally optimized for AI coding agents — primarily Claude Code.

### Primary instruction files
- **[CLAUDE.md](CLAUDE.md)** — Tech stack constraints, design conventions, file map, and SOPs (add a blog post, add a case study, create a top-level page). Agents should read this first.
- **[.impeccable.md](.impeccable.md)** — Design brief: who the site is for, the brand personality, aesthetic direction, and anti-references (no purple `#7464a1`, no glassmorphism, no gradient text, etc.). Read this before making visual changes.

### Documentation
- **[docs/copywriting-guidelines.md](docs/copywriting-guidelines.md)** — Required reading before generating or updating any copy (tone, audience, biographical facts).
- **[docs/design-system.md](docs/design-system.md)** — Full design system reference.
- **[docs/seo-metadata-template.md](docs/seo-metadata-template.md)** — Boilerplate for `<title>`, meta description, OpenGraph, Twitter Card, and JSON-LD tags.

### Impeccable Agents skill pack
Skills are mirrored in both [.agents/skills/](.agents/skills/) and [.claude/skills/](.claude/skills/) so multiple agent runtimes can load them. The pack includes:

| Category       | Skills                                                         |
| -------------- | -------------------------------------------------------------- |
| Design craft   | `impeccable`, `shape`, `layout`, `typeset`, `colorize`         |
| Polish         | `polish`, `distill`, `quieter`, `bolder`, `delight`, `animate` |
| Critique/audit | `critique`, `audit`, `web-design-guidelines`                   |
| Performance    | `optimize`, `overdrive`, `adapt`                               |
| Copy           | `clarify`                                                      |
| SEO            | `seo`, `seo-audit`                                             |

Versions are pinned in [skills-lock.json](skills-lock.json).

---

## 🎨 Design System (Summary)

Full brief lives in [.impeccable.md](.impeccable.md) and [docs/design-system.md](docs/design-system.md). Short version:

- **Theme:** Dark only. No light mode.
- **Accent (teal):** `#64a19d` — used sparingly for CTAs, key stats, active states.
- **Backgrounds:** `#050505`, `#0d0d0d`, `#000` (tinted toward teal; never pure black in large fields).
- **Text:** `#fff`, `#ddd`, `#aaa`.
- **Borders/Dividers:** `#1a1a1a`, `#222`, `#333`.
- **Typography:** Varela Round for headings/labels, Nunito for body; responsive scale via `clamp()`.
- **Anti-references:** no purple (`#7464a1` is banned), no glassmorphism, no gradient text, no side-stripe card accents, no identical icon+heading+text grids, no neon-on-dark AI aesthetics.

---

## 📋 Common Tasks (SOPs)

Full SOPs live in [CLAUDE.md](CLAUDE.md). Quick reference:

### Add a new blog post
1. Duplicate [insights/post-template.html](insights/post-template.html) → rename to `insights/post-slug.html`.
2. Update `<title>`, meta description, `og:title`, `og:description`, `og:image`.
3. Update article header (title, date, category badge, read time).
4. Read [docs/copywriting-guidelines.md](docs/copywriting-guidelines.md), then author content.
5. Add the corresponding card to [insights.html](insights.html) under the correct category.

### Add a new case study
1. Duplicate [case-studies/case-study-template.html](case-studies/case-study-template.html) → rename to `case-studies/client-name.html`.
2. Update meta tags (`title`, `description`, `og:*`).
3. Update hero (client, tagline, stats, background image).
4. Read [docs/copywriting-guidelines.md](docs/copywriting-guidelines.md), then author the case study sections.
5. Add the card to the [case-studies.html](case-studies.html) bento grid (pick an appropriate slot size).

### Create a top-level page
1. Create `page-name.html` at the root.
2. Copy the nav + footer structure from an existing top-level page.
3. Add a `<link>` to the nav across every existing page.
4. Test responsiveness at 375px, 768px, and 1024px.

---

## 🚀 Development & Deployment

**Run locally** — open [index.html](index.html) directly in a browser, or serve the directory with any static file server:

```bash
npx serve .
```

**Deploy** — GitHub Pages serves the contents of the default branch. Merging `dev` → `master` publishes the site. No build step, no CI.
