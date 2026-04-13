````markdown
# 🎨 Design System & UI Components

## 🤖 AI Directive

When asked to build or update a page, you MUST use the HTML patterns defined in this document. Do not invent new CSS classes, layouts, or Bootstrap overrides unless explicitly instructed. Replace the placeholder text and image paths with the relevant content for the current task.

> **Note:** The component code blocks below are intentionally empty. They will be filled in as each section/component is built out. Do not generate new patterns from scratch — reference existing HTML files in the project for current implementations.

---

## 1. Structure & Layout

### Standard Section Wrapper

**Use Case:** The container for every new vertical block of content on a page. Includes standard vertical padding and the IntersectionObserver fade-in class.

```html

```
````

### 12-Column Bento Card

**Use Case:** Used for the case studies and insights archive pages.

```html

```

---

## 2. Typography & Headings

### Primary Section Header

**Use Case:** The main title for a section (e.g., "Origin Story", "What Drives Me"). Always uses Varela Round.

```html

```

### Context Label / Stat Chip

**Use Case:** The small uppercase text used above headers or inside cards to provide context.

```html

```

---

## 3. Buttons & Actions

### Primary Action (Teal)

**Use Case:** The main call-to-action (e.g., "View Case Study", "Connect").

```html

```

### Inline Hyperlink

**Use Case:** Links embedded within paragraph text.

```html

```

---

## 4. Preview Reel Sections

### Case Studies Carousel (`#case-studies-preview`)

**Use Case:** A horizontally scrollable card carousel on the homepage showing 3 cards on desktop (≥992px), 2 on tablet (576–991px), 1 on mobile (<576px). Prev/next buttons use index-based navigation with infinite wrap-around. All styling lives in a `<style>` block inside `index.html` — do not move to `css/styles.css`.

**Colors:** Teal only (`#64a19d`).

**Section wrapper:**
```html
<section class="reel-section fade-in-section bg-black" id="case-studies-preview">
    <div class="container px-4 px-lg-5">
        <!-- Section header -->
        <div class="mb-4">
            <p class="stat-chip">Case Studies</p>
            <h2 class="text-white" style="font-family:'Varela Round',sans-serif; font-size:clamp(1.6rem,3vw,2.2rem);">Work Worth Reading About</h2>
            <p class="text-white-50" style="max-width:560px; font-size:1rem; line-height:1.7;">Real outcomes from real engagements — documented in detail.</p>
        </div>

        <!-- Carousel -->
        <div class="cs-carousel-wrapper">
            <div class="cs-carousel-track" id="csCarouselTrack">
                <!-- Repeat .cs-carousel-slide for each card -->
                <div class="cs-carousel-slide">
                    <a href="case-studies/slug.html" class="cs-reel-card">
                        <div class="cs-reel-card-img">
                            <div class="cs-reel-card-bg" style="background-image:url('assets/img/filename.jpg')"></div>
                            <div class="cs-reel-card-overlay"></div>
                        </div>
                        <div class="cs-reel-card-content">
                            <span class="cs-type-tag">Category</span>
                            <h3 class="cs-reel-card-title">Card Title</h3>
                            <p class="cs-reel-card-blurb">One or two sentences summarising the outcome.</p>
                            <span class="cs-reel-card-arrow">Read Case Study <i class="fas fa-arrow-right"></i></span>
                        </div>
                    </a>
                </div>
            </div>
        </div>

        <!-- Nav buttons: right-aligned desktop, centred tablet/mobile -->
        <div class="cs-carousel-nav mt-3">
            <button class="cs-carousel-btn" id="csPrev" aria-label="Previous"><i class="fas fa-chevron-left"></i></button>
            <button class="cs-carousel-btn" id="csNext" aria-label="Next"><i class="fas fa-chevron-right"></i></button>
        </div>

        <!-- CTA -->
        <div class="mt-4 text-center">
            <a class="btn btn-lg" href="case-studies.html" style="background:#64a19d;border-color:#64a19d;color:#050505;font-weight:600;">
                View All Case Studies <i class="fas fa-arrow-right ms-1"></i>
            </a>
        </div>
    </div>
</section>
```

**Key CSS classes (all in `index.html` `<style>` block):**

| Class | Purpose |
|---|---|
| `.cs-carousel-wrapper` | `overflow:hidden` container; clips overflowing slides |
| `.cs-carousel-track` | Flex row with `scroll-snap-type:x mandatory`, `overflow-x:auto`, hidden scrollbar |
| `.cs-carousel-slide` | Individual slide: `flex:0 0 calc((100% - 3rem)/3)` desktop → `calc((100% - 1.5rem)/2)` tablet → `100%` mobile |
| `.cs-reel-card` | Card shell: `display:flex; flex-direction:column`, dark bg, teal border on hover |
| `.cs-reel-card-img` | Fixed-height image area (`height:200px`, `overflow:hidden`) |
| `.cs-reel-card-bg` | Absolute-fill background-image; grayscale 30% → 0% on hover |
| `.cs-reel-card-overlay` | Subtle darkening gradient over image |
| `.cs-reel-card-content` | Text area below image; `flex:1`, `padding:1.4rem 1.5rem 1.5rem` |
| `.cs-type-tag` | Teal pill badge for category |
| `.cs-reel-card-title` | White, Varela Round, 1.05rem |
| `.cs-reel-card-blurb` | Muted white (`rgba(255,255,255,0.5)`), 0.83rem |
| `.cs-reel-card-arrow` | Teal "Read Case Study →" link text; gap widens on hover |
| `.cs-carousel-nav` | `justify-content:flex-end` desktop; `justify-content:center` ≤991px |
| `.cs-carousel-btn` | 2.5rem teal circle button; fills teal on hover |

**Carousel JS (inline `<script>` immediately after `</section>`):**
```js
(function() {
    var track = document.getElementById('csCarouselTrack');
    var slides = track.querySelectorAll('.cs-carousel-slide');
    var total = slides.length;
    var idx = 0;

    function getVisible() {
        if (window.innerWidth < 576) return 1;
        if (window.innerWidth < 992) return 2;
        return 3;
    }

    function goTo(i) {
        var visible = getVisible();
        var maxIdx = total - visible;
        if (i < 0) i = maxIdx;
        if (i > maxIdx) i = 0;
        idx = i;
        var slideWidth = slides[0].offsetWidth;
        var gap = 24; // 1.5rem at 16px base
        track.scrollTo({ left: idx * (slideWidth + gap), behavior: 'smooth' });
    }

    document.getElementById('csPrev').addEventListener('click', function() { goTo(idx - 1); });
    document.getElementById('csNext').addEventListener('click', function() { goTo(idx + 1); });
})();
```

> **Adding a new card:** Duplicate a `.cs-carousel-slide` block, update the `href`, `background-image`, category tag, title, and blurb. No JS changes needed — `total` is computed dynamically.

### Insights Preview Bento Grid (`#insights-preview`)

**Use Case:** A 5-card bento grid on the homepage showcasing featured insight posts. Uses a `bg-light` background to contrast with the dark sections above and below. All styling lives in a `<style>` block inside `index.html` — do not move to `css/styles.css`.

**Colors:** Teal only (`#64a19d`).

**Responsive layout:**
- **Desktop (≥992px):** 5-column grid — `[A–2col][B–1col][E–2col tall]` / `[C–1col][D–2col][E continued]`
- **Tablet (576–991px):** 3-column grid — `[A–2col][B–1col]` / `[C–1col][D–2col]` / `[E–3col full]`
- **Mobile (<576px):** Single column, all cards stack

**Grid slot roles:**
| Slot | Desktop | Tablet | Card type |
|------|---------|--------|-----------|
| `.irp-a` | col 1–2, row 1 | col 1–2, row 1 | Lead (2-wide) |
| `.irp-b` | col 3, row 1 | col 3, row 1 | Supporting |
| `.irp-c` | col 1, row 2 | col 1, row 2 | Supporting |
| `.irp-d` | col 2–3, row 2 | col 2–3, row 2 | Lead (2-wide) |
| `.irp-e` | col 4–5, rows 1–2 | col 1–3, row 3 | Featured tall |

**Section wrapper:**
```html
<section class="reel-section fade-in-section bg-light" id="insights-preview">
    <div class="container px-4 px-lg-5">
        <!-- Section header -->
        <div class="mb-4">
            <p class="stat-chip stat-chip-teal">Insights</p>
            <h2 class="text-dark" style="font-family:'Varela Round',sans-serif; font-size:clamp(1.6rem,3vw,2.2rem);">Thinking Out Loud</h2>
            <p class="text-muted" style="max-width:560px; font-size:1rem; line-height:1.7;">Section subheading copy.</p>
        </div>

        <!-- Bento grid -->
        <div class="insights-preview-grid">
            <a href="insights/slug.html" class="insight-reel-card irp-a">
                <div class="insight-reel-img-wrap">
                    <img src="assets/img/filename.jpg" alt="Alt text" />
                    <span class="insight-cat-badge">Category</span>
                </div>
                <div class="insight-reel-body">
                    <span class="insight-reel-title">Card Title</span>
                    <p class="insight-reel-blurb">One or two sentences describing the post.</p>
                    <div class="insight-reel-meta">Mon YYYY · X min read</div>
                </div>
            </a>
            <!-- Repeat card structure for .irp-b, .irp-c, .irp-d, .irp-e -->
        </div>

        <!-- CTA -->
        <div class="mt-4 text-center">
            <a class="btn btn-primary btn-lg" href="insights.html">
                Explore All Insights <i class="fas fa-arrow-right ms-1"></i>
            </a>
        </div>
    </div>
</section>
```

**Key CSS classes (all in `index.html` `<style>` block):**

| Class | Purpose |
|---|---|
| `.insights-preview-grid` | CSS grid container; `repeat(5,1fr)` desktop, `repeat(3,1fr)` tablet, `1fr` mobile |
| `.irp-a` – `.irp-e` | Grid placement classes; see slot table above |
| `.insight-reel-card` | Card shell: dark bg `#111`, teal border on hover, lift + shadow transition |
| `.insight-reel-img-wrap` | Image container; heights: 220px for `.irp-a`/`.irp-d`, 150px for `.irp-b`/`.irp-c`, flex-fill for `.irp-e` |
| `.insight-cat-badge` | Teal-bordered pill badge overlaid on image (top-left); matches `insights.html` `.cat-badge` style |
| `.insight-reel-body` | Text area below image; flex column, `padding:1.1rem 1.25rem 1.25rem` |
| `.insight-reel-title` | White, bold, 1.1rem (lead) / 0.9rem (supp); turns teal on hover |
| `.insight-reel-blurb` | Muted (`#666`), 0.83rem lead / 0.78rem supp; `flex:1` to push meta to bottom |
| `.insight-reel-meta` | Uppercase, `#555`, 0.7rem; always pinned to bottom via `margin-top:auto` |

> **Adding a new card:** Use the card HTML structure above with the appropriate `.irp-*` slot class. For placeholder posts, set `href="#"` and use `Coming soon` as the meta text.

---

## 5. Specialized Components

### The "Pull Quote" Block

**Use Case:** Used in blog posts and case studies to highlight a core insight or metric.

```html

```

### Tech Stack / Tools Pill

**Use Case:** Small visual badges to list software (e.g., ClickUp, WordPress, Figma).

```html

```

```

```
