# Project Context — Jonathan Ibrahim Professional Site

## Project Purpose

Professional portfolio and personal brand platform for Jonathan Ibrahim.

**Goals (in priority order):**
1. **Job search** — primary driver, but must be invisible. Nothing on the site signals active job hunting. The site reads as an established personal brand, not a job seeker's portfolio.
2. **Personal brand** — build authority and presence within technology, operations, and delivery leadership
3. **SEO foundation** — publish case studies and insights to establish search presence before migrating to Webflow

**Current phase:** Initial build. Collecting case study content and writing early blog posts. Once the foundation is solid, the plan is to migrate to Webflow using the Miranda Halim template as the design direction.

**No redesign planned for this iteration** — keeping the dark monochromatic look with teal accent and natural imagery throughout.

**Target audience:** Hiring managers and recruiters at tech/digital companies, peer network in operations and PM, future potential clients — without tipping off current employer WISE Digital Partners.

---

## Owner Profile

**Jonathan Ibrahim** — Half Lebanese, half Romanian, first-generation American born in Chicago. Father immigrated from Lebanon to Romania for medical school, met his Romanian mother there. Parents were both doctors. Raised in a household where precision and excellence were the baseline.

**Professional identity:** Delivery leader and Strategic Operations Leader. 14 years in web and delivery operations. Core superpower is translation — between client language and developer/designer execution, between strategic intent and operational output.

**Career (resume-verified):**
| Role | Company | Dates |
|------|---------|-------|
| Head of Project Management | WISE Digital Partners, Austin TX (Remote) | Feb 2025 – Present |
| Website Project Manager | The Get Smart Group, Austin TX (Remote) | Mar 2022 – Feb 2025 |
| Web Development Team Lead | The Get Smart Group, Austin TX (Remote) | Aug 2020 – Mar 2022 |
| Founder & CEO | Electrician Metrics, Chicago IL | Jan 2019 – Aug 2020 |
| Freelance WordPress Developer | Independent | 2012 – Present |

**WISE Digital Partners context:** Back-to-back Inc. 5000 placements. Fully remote digital marketing agency.
**Get Smart Group context:** Pool and hot tub industry's largest builders and global manufacturers. $30K average project.

**Key metrics:**
- 96% client retention · 91% revenue expansion (WISE)
- 100% ClickUp adoption in 60 days (52 users)
- 94% client retention, 23% profitability improvement (Get Smart Group PM role)
- 26% development efficiency improvement (Get Smart Group lead role)
- Lighthouse scores 40–50 → 90+ average
- 50+ people coordinated across 6 departments, 4 continents

**Core competencies:** Program Management · Portfolio Management · Delivery Operations · Cross-Functional Leadership · Client Relationship Management · ClickUp Architecture · Process Improvement · EOS Framework · Change Management · Agile/Scrum · WordPress/Elementor Development · SEO Strategy · Figma

**Technical proficiencies:**
- PM Tools: ClickUp, Airtable, Trello, Asana, EOS Framework
- Development: WordPress, Elementor, Figma, HTML/CSS, JavaScript, PHP
- Marketing: SEMrush, Google Analytics, Google Ads, Rank Math
- Automation: Claude AI, N8N, Zapier

**Education:**
- Business Administration — Loyola University Chicago, Chicago IL (2008–2009)
- Associate in Science — Joliet Junior College, Joliet IL (2011)

**Certifications:**
- Google Project Management Professional Certificate (2025) — 170+ hour specialization
- ClickUp Expert Certification (2024)
- Agile Project Management Certificate — Google (2025)
- Figma UI/UX Design Essentials — Udemy (2026)

**Personal:** Wife Paulette (married July 11, 2020 — got engaged, married, and moved Chicago→Austin all in three months during COVID). Son Jaxon, born ~2021, age 4. Hobbies: cooks every day, recently picked up fishing, collects flashlights/tools/knives/gizmos, large board game collection. "The specific hobby changes regularly. The curiosity doesn't."

**Core values (from about.html):**
1. Honesty, always — direct and plain, not diplomatic for comfort
2. Clarity over cleverness — best systems are invisible
3. Finish what you start — strategy without execution is creative writing
4. Leave it better than you found it

---

## Writing Voice & Tone

**The voice:** Authoritative expert on the surface, unexpected warmth and self-awareness underneath. Direct, frank, real. Unconventional for someone in his position — not corporate, not polished-for-LinkedIn.

**Structural patterns in his copy:**
- Short punchy opener. Then a longer explanatory follow-up.
- Em dashes used liberally for asides and rhythm
- First-person, present tense, conversational
- Specific numbers and concrete details over vague claims
- Self-aware admissions: "It's not a professional trait. It's closer to a compulsion."
- Humor that reveals character: "The kind of project that has no SOP and absolutely no room for process improvement — and I love every second of it."
- Pull quotes crystallize the core insight of a section
- Section labels as small uppercase stat-chip context setters (e.g. "Origin Story", "What Drives Me")

**Avoid:**
- Corporate buzzwords: "passionate about", "results-driven", "synergy", "leverage", "ecosystem"
- Passive voice
- Filler adjectives (incredible, amazing, transformative)
- Vague claims without specifics
- Anything that sounds like a LinkedIn summary written by committee

**The test:** Would a real, smart, slightly unconventional professional say this out loud? If it sounds like it came from a press release, rewrite it.

---

## Tech Stack
- HTML5 + CSS3 + Vanilla JS (no framework)
- Bootstrap 5.2.3 (CSS + JS via CDN)
- Google Fonts: **Varela Round** (headings, nav, labels) + **Nunito** 200–900 (body)
- Font Awesome 6.3.0 (icons)
- No bundler, no backend, no env vars, no database

## Design Philosophy

**Core principle:** Dark, sophisticated, professional without being flashy. Signals technical credibility.

**What we are NOT building in this iteration:**
- Light mode toggle
- Heavy animations or parallax
- Auto-playing media
- JS framework (React, Vue, etc.)
- CMS or backend
- Build pipeline / bundler

**Constraints:**
- GitHub Pages (static files only, no server-side)
- Deploy by pushing — no CI, no build step
- Must work on mobile (recruiters browse on phones)
- Nothing that reads as "I'm actively job hunting"

**Future direction:** Miranda Halim Webflow template is the design inspiration and planned destination post-migration. This iteration is the HTML/CSS foundation — not the final design.

---

## Design System

### Colors
| Role | Value |
|------|-------|
| Accent (teal) | `#64a19d` — links, badges, borders, highlights |
| Background dark | `#050505`, `#0d0d0d`, `#000` |
| Text | `#fff`, `#ddd`, `#aaa` |
| Borders/dividers | `#1a1a1a`, `#222`, `#333` |

### Typography
- Responsive scale via `clamp(min, preferred-vw, max)` on headings
- Nunito body at 1.88 line-height for long-form readability

### Conventions
- Dark theme throughout — no light mode
- Smooth CSS transitions on hovers; bounce animation on scroll chevrons
- Page-specific styles in `<style>` tags inside each HTML file — no separate SCSS
- Bootstrap CSS variables (`--bs-*`) for theming overrides
- Fade-in on scroll via IntersectionObserver + `.fade-in-section` / `.is-visible` classes

---

## File Map
```
index.html          Hero/landing — masthead, About snippet, Core Expertise, Track Record, Career Timeline, Connect, Footer
about.html          Biography — Origin Story, What Drives Me, Beyond the Work (family + hobbies), How I Work (values), CTA
case-studies.html   Archive — bento grid + filter pills
insights.html       Blog archive — magazine layout, sticky category nav, dot-grid texture
case-studies/
  case-study-test.html    Template for individual case study pages
insights/
  post-template.html      Template for individual blog posts
css/styles.css      Bootstrap 5.2.3 base + all custom styles (single file)
js/scripts.js       Navbar fade/shrink + ScrollSpy (77 lines)
assets/
  jonathan_professional_headshot_pic.jpg
  jonathan_ibrahim_Prof_Pic.jpg
  Jonathan_Ibrahim_Resume.pdf
  favicon.ico
  img/              Hero + section background images (9 files)
CNAME               jonathanibrahim.com
```

---

## Layout Patterns

### index.html sections (in order)
Navbar → Masthead hero → About snippet (image + text) → Core Expertise (3 alternating image+text rows, light bg) → Track Record (4 stat cards, black bg) → Career Timeline (teal left-border timeline, light bg) → Connect CTA (black bg) → Footer

### Case Studies (case-studies.html)
- CSS Grid, 12-col bento: `featured` 8×7, `tall-sidebar` 4×7, `wide` 6×5, `square` 4×5, `wide-lg` 8×5, `small` 3×4
- 2-col on tablets, 1-col on mobile
- Filter pills bar — JS filters cards by category

### Insights Archive (insights.html)
- Dot-grid background texture (`radial-gradient` 28px)
- Sticky category nav at `top: 68px`, horizontally scrollable pills
- Section dividers with category labels
- Categories: Systems, AI, Operations, ClickUp, SEO, Web Development
- Multiple card variants (featured, standard, compact)

### Individual Post (insights/post-template.html)
- 2-col grid: article body + sticky sidebar → 1-col below 991px
- Styled H2 with teal left border, code blocks, pull quotes

### About (about.html)
- Grayscale hero image, CSS filter
- Pull quotes (teal left border, subtle teal bg)
- Stat chips (teal badge labels)
- Hobby cards with hover lift + border highlight
- Value rows (numbered 01–04, teal number accent)
- Light bg sections alternate with dark bg sections

---

## Common Tasks

### Add a new blog post
1. Duplicate `insights/post-template.html` → rename to `insights/post-slug.html`
2. Update `<title>`, meta description, og:title, og:description, og:image
3. Update article header: title, date, category badge, read time
4. Write content inside `<article>` section
5. Add card to `insights.html` under the appropriate category section
6. Commit and push

### Add a new case study
1. Duplicate `case-studies/case-study-test.html` → rename to `case-studies/client-name.html`
2. Update meta tags
3. Update hero: client name, tagline, stats, background image
4. Write case study sections
5. Add card to `case-studies.html` bento grid (pick appropriate slot size)
6. Commit and push

### Update resume
1. Replace `assets/Jonathan_Ibrahim_Resume.pdf` (keep exact filename)
2. No code changes needed — all links point to same filename
3. Commit and push

### Add a new top-level page
1. Create `page-name.html` at root
2. Copy nav + footer structure from an existing page
3. Add `<link>` to nav in all existing pages
4. Keep dark theme and teal accents consistent
5. Test mobile at 375px, 768px, 1024px

---

## JavaScript Behavior (js/scripts.js)
- Navbar fade-in: 2s delay on load OR immediate on scroll > 50px
- Navbar shrink: `.navbar-shrink` class added on scroll
- ScrollSpy: Bootstrap ScrollSpy for active nav link
- Mobile collapse: auto-closes nav on item click
- Fade-in on scroll: IntersectionObserver on `.fade-in-section` elements (inline in each HTML file)

---

## SEO / Meta
- Full OpenGraph + Twitter Card on all pages
- JSON-LD `Person` schema on index.html: name, job title, Austin TX, WISE Digital Partners, Loyola + JJC education, Google PM / ClickUp Expert / Agile certs
- `knowsAbout`: Project Management, Program/Portfolio Management, ClickUp Architecture, Digital Operations, EOS Framework, WordPress Development, Cross-Functional Leadership, Process Improvement, Agile

---

## Development Workflow

**Local:**
```bash
npx serve .
# or open index.html directly in a browser
```

**Deploy:**
1. Make changes locally
2. Commit with descriptive message
3. Push to `main` branch
4. GitHub Pages rebuilds automatically (2–3 min)
5. Verify at jonathanibrahim.com

**Branch strategy:** `main` = production. No staging environment — direct to prod. Site is low-risk static content.
