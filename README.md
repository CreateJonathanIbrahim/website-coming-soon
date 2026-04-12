# Jonathan Ibrahim - Professional Site

Personal website for Jonathan Ibrahim, Strategic Operations Leader and Head of Project Management at WISE Digital Partners.

**Live at:** [jonathanibrahim.com](https://jonathanibrahim.com)

## 🏗️ Architecture & Stack

This project is built with deliberate simplicity. There is no build pipeline, no bundler, and no JavaScript framework.

- **Frontend:** Vanilla HTML5, CSS3, and JavaScript
- **Styling:** Bootstrap 5.2.3 (via CDN) + Custom CSS
- **Typography & Icons:** Google Fonts (Varela Round, Nunito) + Font Awesome
- **Hosting:** GitHub Pages

## 🤖 AI-Assisted Development

This repository is heavily optimized for AI coding agents (specifically Claude Code).

- **`CLAUDE.md`**: Contains the strict architectural constraints, design system, and SOPs for the agent.
- **`docs/copywriting-guidelines.md`**: Contains the biographical context, tone guidelines, and core values for generating copy.

If you are using an AI agent to edit this site, ensure it reads both files before executing tasks.

## 📂 Structure

- `index.html` — Main landing page
- `case-studies.html` — Case studies overview bento grid
- `insights.html` — Blog/insights archive
- `case-studies/` — Individual case study pages
- `insights/` — Individual insight/post pages
- `css/styles.css` — Global styles and Bootstrap overrides
- `js/scripts.js` — Core site scripts (navbar logic, scroll animations)
- `assets/` — Images, headshots, resume PDF, and favicon

## 🚀 Development & Deployment

**Run locally:**
You can open `index.html` directly in a browser, or serve the directory with any static file server:

```bash
npx serve .
```
