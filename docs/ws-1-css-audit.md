# WS-1 Phase 1: CSS Audit Catalog

**Status:** Phase 1 complete. Awaiting your review before Phase 2 starts.

This catalog maps every CSS rule across the repo and decides where each belongs after the WS-1 split. Three buckets:

- **SHARED** → moves to new `css/site.css`
- **PAGE** → stays inline in the HTML file's `<style>` block
- **DEAD** → deleted

**Files audited:** 11 HTML files (`<style>` blocks totalling ~2,270 lines), `css/styles.css` (theme override block, lines 13-90), `css/custom.css` (290 lines).

---

## Headline numbers

| Bucket | Approx rule count | Approx lines | Destination |
|---|---|---|---|
| Theme tokens (`:root`) | 1 block, ~80 props | ~80 | `site.css` (top) |
| Truly shared (multi-file) | ~50 selectors | ~350 | `site.css` |
| Insight-post duplicates (6 files × ~30 selectors) | ~30 selectors | ~700 → ~120 after dedup | `site.css` (under `.post-*` namespace) |
| Page-specific (kept inline) | ~150 selectors | ~1,100 | inline `<style>` blocks |
| Dead code (custom.css legacy) | ~5 selectors | ~80 | deleted |
| **Net** | | **~2,270 inline → ~1,250 inline + ~600 site.css** | ~45% reduction in duplication |

---

## Section A — Goes to `site.css`

### A1. Theme tokens (currently `css/styles.css` lines 13-90)

The full Bootstrap `:root` override block. Standalone, no dependencies, moves cleanly. Includes:

- Color tokens: `--bs-blue` … `--bs-dark` (Grayscale theme palette), `--bs-primary: #64a19d` (teal), `--bs-secondary: #7464a1` (purple — note: this is the banned color, defined here but should never be used)
- RGB equivalents (for `rgba()` math)
- Font tokens: `--bs-font-sans-serif`, `--bs-body-font-family` (Nunito)
- Border, gradient, link tokens

**Action:** Copy entire `:root` block from styles.css into the top of site.css.

### A2. Fade-in animation (used in 7 files)

Defined identically in: `case-studies.html`, `insights.html`, `case-study-template.html`, `insights/clickup-hierarchy-explained.html`, `insights/freelancer-to-agency-side.html`, `insights/onboarding-process-that-doesnt-leak.html`, `insights/post-template.html`, `insights/seo-2026-small-service-businesses.html`, `insights/the-discovery-process.html`.

```css
.fade-in-section {
    opacity: 0;
    transform: translateY(18px);  /* 20px in case-studies.html, 22px in case-study-template.html */
    transition: opacity 0.6s ease-out, transform 0.6s ease-out;
}
.fade-in-section.is-visible {
    opacity: 1;
    transform: translateY(0);
}
```

Minor drift in initial `translateY` values (18/20/22). Pick one (18px is the most common) and standardize.

**Note:** `js/scripts.js` references this — verify the consolidated rule keeps the IntersectionObserver fade working.

### A3. Stat chip (used in 2 files)

Defined nearly identically in `index.html` and `about.html`:

```css
.stat-chip {
    display: inline-block;
    background: rgba(100,161,157,0.12);
    border: 1px solid rgba(100,161,157,0.3);
    color: #64a19d;
    font-family: 'Varela Round', sans-serif;
    font-size: 0.8rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    padding: 0.35rem 0.85rem;
    border-radius: 2rem;
    margin: 0.25rem 0.25rem 0.25rem 0;  /* index.html uses margin-bottom: 1rem */
}
```

Pick the about.html version (4-direction margin, more flexible).

### A4. Insight post layout (the big duplication — 6 files)

Six files share an essentially identical block: `the-discovery-process.html`, `clickup-hierarchy-explained.html`, `freelancer-to-agency-side.html`, `onboarding-process-that-doesnt-leak.html`, `seo-2026-small-service-businesses.html`, `post-template.html`.

The duplicated rules (~30 selectors per file × 6 files = ~700 lines that collapse to ~120 in site.css):

- `.post-hero` (background image URL is the per-page variable; everything else identical)
- `.post-cat-badge`
- `.post-hero-title`
- `.post-meta-row`, `.post-meta-row span + span::before`
- `.post-layout` + `@media (max-width: 991px)` variant
- `.post-body` and all child selectors: `p`, `h2`, `h3`, `ul`, `ol`, `li`, `a`, `a:hover`, `strong`, `em`, `hr`, `blockquote`
- `.callout-box`, `.callout-box strong`
- `.post-sidebar`
- `.toc-label`, `.toc-list`, `.toc-list li a`, hover, active
- `.post-footer-cta`, `.post-footer-cta .btn`, `.post-footer-cta .btn-primary:hover`
- `.fade-in-section` (already covered in A2)

**Drift to flag:**
- `clickup-hierarchy-explained.html`: `.post-meta-row { color: #888 }` — others use `#555`. Pick one (the `#555` is more common, looks better against the dark hero gradient).
- `post-template.html`: missing `.post-footer-cta .btn` rules that the published posts have. Add them when consolidating.

**Per-page variable:** the hero image URL inside `.post-hero { background: ... url('...') }`. Solution: keep just the URL inline as a custom property override:

```css
/* in post-template.html, in published posts */
.post-hero {
    background-image: linear-gradient(...), url('https://images.unsplash.com/photo-XYZ');
}
```

Or use a CSS variable: `--post-hero-image: url(...)` set inline, consumed by site.css.

### A5. Footer (used everywhere)

Currently in `custom.css`:

```css
.footer {
    padding: 5rem 0;
}
```

Bare-bones, applies sitewide. **Action:** Copy to site.css.

### A6. Masthead (homepage hero, also used as `class="masthead"` on home)

Currently in `custom.css`. Active — referenced by the homepage hero. The `.masthead` class IS used in `index.html`. The rule loads `assets/img/bg-masthead.jpg` as background. **Verify this asset is still in active use** — if it's not visible on the current homepage (the hero image is now the 2026 headshot via WS-3, not a bg-masthead image), then this rule may be partly stale.

**Decision needed in Phase 2:** Verify masthead background-image is wanted; either migrate as-is to site.css or strip the background-image lines.

### A7. Contact section (homepage Connect block)

Currently in `custom.css`. The `.contact-section` class IS used in `index.html` (the Connect section). The rules include:

- `.contact-section` base (height, padding, flex layout)
- `.contact-section::before` (background image: `derek-livingston-P2TIXADqcFU-unsplash.jpg` with grayscale + transform). Active — the moose image IS visible on the current homepage Connect section.
- `.contact-section::after` (gradient overlay)
- `.contact-section > *` (z-index)
- `.contact-section .card` (border-bottom teal)
- `.contact-section .card h4`, `hr`
- `.contact-section .social a` and hover/active

**Action:** Migrate as-is to site.css. Visual treatment is intentional and current.

---

## Section B — Stays inline (page-specific)

### B1. `index.html` (~95% of its 630-line `<style>` block stays inline)

All home-only treatments:

- Hero entrance stagger: `.hero-reveal`, `.hero-d1` through `.hero-d6`, `.hero-sep`, `.masthead.hero-loaded` and child variants, scroll cue chevron, button press delight
- Career Journey Timeline: `.career-timeline`, `.career-entry`, `.career-year`, `.career-rule`, `.career-role`, `.career-company`, `.career-meta`, `.career-desc`, plus mobile media query
- Track Record Number Grid: `.tr-eyebrow`, `.tr-grid`, `.tr-cell`, `.tr-metric`, `.tr-metric-unit`, `.tr-label`, `.tr-desc`, plus mobile media query
- Core Expertise row entrances: `.expertise-row`, `.expertise-row--from-left/--from-right`, `.expertise-row.is-visible`, image grayscale lift, panel tint, heading teal shift
- Reduced motion preference handling for expertise rows
- Grain overlay (`.masthead::after`)
- Case-study reel cards: `.cs-reel-card` and all children — used only on home carousel
- Case-study carousel: `.cs-carousel-*` — home only
- Insights preview grid: `.insights-preview-grid`, `.irp-a` through `.irp-e`, `.insight-reel-card` and children, `.insight-cat-badge` — home only

**Note:** `.cs-reel-card` (home) and `.cs-card` (case-studies archive) are different components for different contexts. They share a naming root but different rules. Keep both inline.

### B2. `about.html` (~99% stays inline)

- `.about-page-header`, `.headline-accent`, `.subhead`, `.about-page-header img`
- `.about-section`, `.about-section-dark`, `.about-section-darker`, `.about-section-light`
- `.pull-quote`, `.pull-quote p`, `.pull-quote-light p`
- `.hobby-card` and children
- `.value-row`, `.value-number`, `.value-text h4`, `.value-text p`
- `.family-highlight` and children
- `.about-cta`

Only `.stat-chip` migrates to site.css (covered in A3).

### B3. `case-studies.html` (~95% stays inline)

- `.cs-archive-header` (with Unsplash bg)
- Filter pills: `.filter-bar`, `.filter-btn`, hover, active
- Bento grid: `.bento-grid`, `.bento-featured`, `.bento-tall`, `.bento-wide`, `.bento-square`, `.bento-wide-lg`, `.bento-small`, with media queries for tablet and mobile
- Case study card (archive variant): `.cs-card`, `.cs-card-bg`, `.cs-card-overlay`, `.cs-card-content`, `.cs-type-tag` (archive variant — see conflict in Section D), `.cs-filter-pill`, `.cs-card-title` (with bento-* size variants), `.cs-card-blurb`, `.cs-card-arrow`, `.cs-card-placeholder`, `.cs-card-wrap`

`.fade-in-section` migrates to site.css (covered in A2).

### B4. `insights.html` (~98% stays inline)

- Insights masthead: `.insights-hero`, `.insights-hero::before` (dot-grid), `.masthead-rule`, `.masthead-rule-thin`, `.masthead-kicker`, `.masthead-title`, `.masthead-tagline`, `.masthead-issue`
- Sticky category nav: `.cat-nav`, `.cat-nav-inner`, `.cat-nav-pill`, hover, active
- Section divider: `.section-divider`, `.section-label`, `.section-view-all`, hover
- Card system: `.insight-card`, `.card-img-wrap`, `.cat-badge`, `.card-body-inner`, `.card-title-link`, `.card-blurb`, `.card-meta`, lead/supporting variants, video card variant, video badge/play icon

`.fade-in-section` migrates to site.css.

**Note:** `.cat-badge` (insights archive) and `.insight-cat-badge` (home preview) are visually similar but named differently — kept page-specific.

### B5. `case-studies/case-study-template.html` (mostly inline, but template will be replicated)

This is the structural template for individual case studies. After WS-7 ships 3 real case studies, all of these rules will exist in 4 files. Worth pre-emptively migrating to site.css under a `.cs-*` namespace.

**Recommended treatment:** Migrate to site.css NOW under namespace, with the understanding that future case study files won't need to redefine.

Selectors:
- `.cs-hero`, `.cs-hero .scroll-chevron`, `@keyframes bounce`
- `.meta-badge`
- `.cs-section-title`
- `.specs-card`, `.specs-card .tool-pill`
- `.chaos-diagram`, `.tool-box`, `.arrow`, `.pain-point`
- `.video-placeholder`, `.play-icon`, `.video-label`
- `.cs-timeline`, `.cs-timeline-entry`, `.cs-timeline-dot`, `.cs-phase-number`, `.cs-timeline-img`, `.cs-timeline-img-caption`
- `.cs-img-wrap`, `.cs-img-caption`
- `.stat-divider`
- `.cs-testimonial`, `.cs-testimonial blockquote`, `.cs-testimonial .avatar`
- `.cs-learned`
- `.accordion-button`, `.accordion-item`, `.accordion-body` (Bootstrap accordion dark theme overrides)

**Decision in Phase 2:** Migrate as a "case-studies pattern" block, OR keep inline in template + each future case study. Lean migrate.

---

## Section C — Dead code (delete)

In `css/custom.css`:

| Selector | Status | Reason |
|---|---|---|
| `.about-section`, `.about-section p` | DEAD | Conflicts with about.html's inline `.about-section` (about.html wins via cascade); the residual rules (`background` gradient, `p { margin-bottom: 5rem }`) aren't visibly active in current page. |
| `.projects-section`, `.projects-section .featured-text`, `.project-text` | DEAD | No `.projects-section` class in current HTML files. Legacy from original Start Bootstrap Coming Soon theme. |
| `.project img`, `.project:hover img` | DEAD | No `.project` class in active use (verify against index.html — there's an Expertise section, but it uses `.expertise-*` namespace, not `.project`). |
| `.track-record-section`, `.track-record-section .card`, `.card hr` | DEAD | No `.track-record-section` class in current HTML — replaced by `.tr-grid` namespace inline in index.html. |
| `.signup-section`, `.signup-section .form-signup input` | DEAD | No signup form anywhere on the current site. |

**Action:** Delete custom.css entirely after migrating the live rules (`.masthead`, `.contact-section` family, `.footer`) to site.css.

---

## Section D — Conflicts and edge cases (decisions for Phase 2)

### D1. `.cs-type-tag` definition mismatch

| File | Border | Padding | Font-size |
|---|---|---|---|
| `index.html` (home reel) | 1px solid rgba(100,161,157,0.5) | 0.18rem 0.65rem | 0.65rem |
| `case-studies.html` (archive) | 1px solid #64a19d | 0.2rem 0.7rem | 0.68rem |

**Resolution options:**
- (a) Keep both, page-specific (current de facto state). Easy, maintains visual nuance.
- (b) Pick one and use sitewide. Slight visual drift on whichever page didn't define it.

Recommend (a). Mark the conflict in commit notes; revisit if a future redesign harmonizes them.

### D2. `.cat-badge` vs `.insight-cat-badge` naming

`insights.html` uses `.cat-badge`. `index.html` (home preview) uses `.insight-cat-badge`. Different names, similar styling. Could be unified, but per-file specificity is intentional (different positioning, sizes).

**Resolution:** Keep distinct naming, both stay inline in their respective files.

### D3. `.stat-chip` inline duplication

`index.html` line 134-147 has `.stat-chip` with `display: inline-block` declared twice (lines 135 and 146). Probably an editing artifact. Clean up when migrating to site.css.

### D4. `.fade-in-section` translateY drift

Three different initial transform values: 18px (most common), 20px (case-studies.html), 22px (case-study-template.html).

**Resolution:** Standardize on 18px in site.css.

### D5. `.post-meta-row` color drift

5 of 6 insight files use `#555`. `clickup-hierarchy-explained.html` uses `#888`. The `#555` looks more intentional against the dark gradient hero.

**Resolution:** Standardize on `#555` in site.css.

### D6. Custom.css `.masthead` background image

`custom.css` line 13 sets `.masthead { background: linear-gradient(...), url('../assets/img/bg-masthead.jpg') }`. **Verify** during Phase 2 that this asset is still meant to show as a hero background. If not, strip the URL when migrating.

### D7. `.fade-in-section` hidden double-`display`

`index.html` line 134-147 (stat-chip block) has `display: inline-block` on lines 135 AND 146 — clearly an editing leftover. Clean up.

---

## Section E — Phase 2 migration plan (preview)

When Phase 2 begins, the work is:

1. Download Bootstrap 5.2.3 minified to `css/bootstrap.min.css` (verify SHA against the c0bcf78… hash from the DECISION-1 test).
2. Create `css/site.css` with sections in this order:
   - `:root` theme tokens (from styles.css)
   - Layout / global (none yet identified — leave a section header for future use)
   - Animations (`.fade-in-section`)
   - Shared chip / badge (`.stat-chip`)
   - Insight post layout (the big consolidated `.post-*` block)
   - Case study layout (`.cs-hero`, `.cs-timeline`, etc. — the case-study-template namespace)
   - Footer (`.footer`)
   - Masthead (`.masthead`, `.masthead::after`)
   - Contact section (`.contact-section` family)
3. For each of the 11 HTML files: swap `<link>` tags, strip migrated rules from inline `<style>` block.
4. Delete `css/styles.css` and `css/custom.css`.
5. Visual parity check at 375 / 768 / 1024 / 1440 px.

Estimated Phase 2 duration: 2-3 hours including verification.

---

## Awaiting your review

Things I'd specifically like you to confirm before Phase 2 starts:

1. **D1 `.cs-type-tag`:** keep both page-specific (recommended) or harmonize?
2. **D6 `.masthead` background:** is `bg-masthead.jpg` still wanted as the hero background? Or should the URL get stripped?
3. **A7 case-study-template migration:** migrate the case-study namespace to site.css now (anticipating WS-7's 3 real case studies), or keep inline until WS-7 ships?
4. **A4 hero image variable:** for the insight posts, do you want the hero URL parameterized via CSS custom property, or just kept as a one-line inline override?

Anything else in this catalog you want me to investigate or expand before I start Phase 2.
