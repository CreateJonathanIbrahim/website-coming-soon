# jonathanibrahim.com

Personal site for Jonathan Ibrahim — Strategic Operations Leader, Head of Project Management, ClickUp architect. Built as a single-page static site, deployed on GitHub Pages.

**Live:** [jonathanibrahim.com](https://jonathanibrahim.com)

---

## About this site

This is a deliberately small site with a deliberate job: present 14 years of operations and delivery work in a form you can read in under two minutes, and give the people who care — clients, collaborators, hiring teams — a fast path to the things that matter (resume, LinkedIn, email).

It's built as a static, single-page site so it stays fast, cheap to host, and trivial to maintain. The visual language is monochrome with a single teal accent (`#64a19d`) — every image runs through a grayscale filter so the accent is the only color that survives, and attention lands where it's supposed to.

## Tech stack

| Layer | Choice |
|---|---|
| HTML | [Pug](https://pugjs.org) templates → compiled `index.html` |
| CSS | [Sass](https://sass-lang.com) (SCSS) + [PostCSS](https://postcss.org) + Autoprefixer |
| JS | Vanilla ES6, IntersectionObserver, Bootstrap ScrollSpy |
| Framework | [Bootstrap 5.2.3](https://getbootstrap.com) (only runtime dependency) |
| Icons | [Font Awesome 6.3](https://fontawesome.com) via CDN |
| Fonts | Varela Round (display), Nunito (body) via Google Fonts |
| Dev server | [BrowserSync](https://browsersync.io) with [Chokidar](https://github.com/paulmillr/chokidar) file watching |
| Task runner | [Concurrently](https://github.com/open-cli-tools/concurrently) |
| Hosting | GitHub Pages with custom domain via `CNAME` |

## Project structure

```
.
├── index.html                 # Compiled output (committed so GitHub Pages serves it)
├── css/styles.css             # Compiled Bootstrap + theme (~12k lines, includes Bootstrap)
├── js/scripts.js              # Compiled JS (nav shrink, scrollspy, mobile collapse)
├── assets/                    # Headshots, resume PDF, section imagery, favicon
│
├── src/                       # Hand-edited sources — edit these, not root files
│   ├── pug/index.pug          # Page template
│   ├── scss/                  # Partials: variables, components, sections
│   │   ├── styles.scss        # Entry point
│   │   ├── variables/         # _colors.scss, _typography.scss
│   │   ├── components/        # _navbar.scss, _buttons.scss
│   │   └── sections/          # _masthead, _about, _projects, _signup, _contact, _footer
│   ├── js/scripts.js
│   └── assets/
│
├── scripts/                   # Node build & dev-server scripts
│   ├── build-{pug,scss,scripts,assets}.js
│   ├── render-*.js            # Incremental rebuilds triggered by the watcher
│   ├── sb-watch.js            # Chokidar watcher
│   ├── start.js               # Orchestrates watcher + BrowserSync via concurrently
│   └── clean.js
│
├── package.json
├── CNAME                      # jonathanibrahim.com
└── LICENSE                    # MIT (from upstream Start Bootstrap)
```

## Getting started

Requires Node.js and npm.

```bash
git clone https://github.com/<your-user>/website-coming-soon.git
cd website-coming-soon
npm install
npm start
```

`npm start` runs a full build, boots BrowserSync with live reload, and opens the site in your default browser. Edit anything under `src/`; the watcher recompiles and reloads.

## NPM scripts

| Script | What it does |
|---|---|
| `npm start` | Build everything, then launch BrowserSync with live reload |
| `npm run start:debug` | Same as `start`, with extra logging |
| `npm run build` | Clean + build Pug, SCSS, JS, and assets into the root |
| `npm run build:pug` | Compile `src/pug/index.pug` → `index.html` |
| `npm run build:scss` | Compile `src/scss/styles.scss` → `css/styles.css` with autoprefixer |
| `npm run build:scripts` | Copy `src/js/scripts.js` → `js/` |
| `npm run build:assets` | Copy `src/assets/` → `assets/` |
| `npm run clean` | Remove generated build artifacts |

## How the build works

The repo is its own dist — compiled artifacts (`index.html`, `css/`, `js/`, `assets/`) live at the root because GitHub Pages serves from the repo root. So you write in `src/`, and the build writes over the root files. Don't hand-edit the compiled files; the next rebuild will clobber them.

`scripts/start.js` uses Concurrently to run two things in parallel: the Chokidar watcher in `scripts/sb-watch.js` (which triggers the right `render-*.js` on file change) and BrowserSync (which injects CSS and reloads on JS/HTML changes).

## Design system

Pulled from `src/scss/variables/`.

**Colors**

| Token | Hex | Use |
|---|---|---|
| Teal (primary) | `#64a19d` | Accent — links, buttons, icons, timeline border, favicon mark |
| Black | `#050505` | Body background, hero, darkest sections |
| Gray 900 | `#212529` | Text on light surfaces, dark panels |
| Gray 100 | `#f8f9fa` | Light section backgrounds |
| White | `#ffffff` | Navbar, cards |

One accent, one only. Every image is filtered with `grayscale(100%)` so color never competes with the teal.

**Type**

- **Display:** Varela Round — hero H1, section headings (uppercase, wide letter-spacing)
- **Body:** Nunito (400–900) with a 0.0625em global letter-spacing
- Font stack falls back to system UI fonts if CDN fails

**Motion**

- Navbar fades in on first load, shrinks when the user scrolls past 50px
- Section content fades up on enter via IntersectionObserver (`0.15` threshold, `-100px` bottom margin)
- Bootstrap ScrollSpy keeps the active nav link in sync with the scroll position

## What's on the page

Single page, anchor-scrolled:

1. **Masthead** — name, title, and three CTAs (resume PDF, LinkedIn, email)
2. **About** — positioning statement and current role context
3. **Core Expertise** — three pillars (Program & Portfolio Management, Digital Operations Architecture, Web Strategy & Delivery)
4. **Track Record** — four headline metrics in icon cards
5. **Career Journey** — vertical timeline of roles with dates, companies, and scope
6. **Connect** — single email CTA
7. **Footer** — name, location, email, copyright

## SEO and performance

- **Structured data:** JSON-LD `Person` schema with job title, employer, location, education, and certifications
- **Social cards:** Open Graph (`og:type=profile`) + Twitter `summary_large_image`
- **Imagery:** Primary headshot ships as WebP; Bootstrap's responsive image classes handle scaling
- **Favicon:** Inline SVG data URI — a "JI" monogram in teal on near-black. No extra request, looks crisp at any density.
- **No tracking scripts** and no third-party JS beyond the Font Awesome and Bootstrap CDNs

## Deployment

GitHub Pages, straight from `master`. The `CNAME` file points the site at `jonathanibrahim.com`. Pushing to `master` publishes.

Because the repo root is the deployed site, always run `npm run build` before committing visual changes so the compiled `index.html` / `css/styles.css` / `js/scripts.js` match what's in `src/`.

## Roadmap

- Ongoing: content expansion — case studies and longer-form writing on delivery operations, ClickUp architecture, and remote team systems
- Eventual: platform migration to Webflow for easier content management, keeping the current monochrome + teal visual language

## Credits

Scaffolding and build pipeline forked from [Start Bootstrap — Grayscale](https://startbootstrap.com/theme/grayscale/) by [David Miller](https://davidmiller.io/), released under MIT. Bootstrap itself is by [Mark Otto](https://twitter.com/mdo) and [Jacob Thornton](https://twitter.com/fat).

All content, copy, site structure, and brand customization © Jonathan Ibrahim.

## License

MIT — see [LICENSE](LICENSE). The MIT grant covers the code scaffolding inherited from Start Bootstrap. Personal content (copy, imagery, resume, headshots) is not licensed for reuse.
