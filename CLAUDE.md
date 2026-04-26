# Project Context — Jonathan Ibrahim Professional Site

## 🔒 Public Repository Boundary

This repository is public. GitHub Pages publishes from it. Anything committed here is world-readable. Before writing or editing any file in this repo, ask: would I be comfortable with this content visible on the open web? If the content is private (income context, job-search status, family details, client names under NDA, ClickUp workspace IDs, internal task notes), it does not belong in a committed file. Route private context to `CLAUDE.local.md` (gitignored) or keep it out of the repo entirely.

## 🤖 Agent Behavior & Directives

- **Direct Output:** Keep explanations extremely brief. Output code directly without apologies, filler language, or conversational fluff.
- **Copywriting Context:** For generating text, case studies, blog posts, or updating biographical pages, **you must first read `docs/copywriting-guidelines.md`** to adhere to voice and tone constraints. Private operational context (audience framing, current employment, family details) lives in `CLAUDE.local.md`.
- **Preserve Structure:** Do not remove existing comments, HTML structure, or utility classes when editing files unless explicitly requested.
- **Verification:** Run a final read of all modified files to check for syntax errors before declaring a task complete.

## 🏗️ Tech Stack & Constraints

- **Core:** HTML5 + CSS3 + Vanilla JS (no frameworks like React or Vue).
- **Styling:** Bootstrap 5.2.3 (via CDN) + Custom CSS.
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

## 📋 Common Tasks (SOPs)

### Add a New Blog Post

1. Duplicate `insights/post-template.html` → rename to `insights/post-slug.html`.
2. Update `<title>`, meta description, `og:title`, `og:description`, and `og:image`.
3. Update article header: title, date, category badge, read time.
4. Read `docs/copywriting-guidelines.md`, then author content inside the `<article>` section.
5. Add the corresponding card to `insights.html` under the correct category section.

### Add a New Case Study

1. Duplicate `case-studies/case-study-template.html` → rename to `case-studies/client-name.html`.
2. Update meta tags (`title`, `description`, `og:*`).
3. Update hero: client name, tagline, stats, background image.
4. Read `docs/copywriting-guidelines.md`, then author the case study sections.
5. Add the corresponding card to `case-studies.html` bento grid (select appropriate slot size).

### Create a Top-Level Page

1. Create `page-name.html` at the root directory.
2. Copy the nav + footer structure from an existing top-level page.
3. Add a `<link>` to the nav across all existing pages.
4. Test mobile responsiveness at 375px, 768px, and 1024px.

## ⚙️ JavaScript & SEO Rules

- **Behavior (`js/scripts.js`):** Handles navbar fade-in (2s delay or scroll > 50px), navbar shrink (`.navbar-shrink`), Bootstrap ScrollSpy, and auto-closing mobile collapse navs.
- **SEO Requirements:** Full OpenGraph + Twitter Card tags on all pages. Ensure JSON-LD `Person` schema remains intact on `index.html`.
