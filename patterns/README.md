# Patterns Library

A documented library of reusable HTML structural patterns. When you want to drop a known module (Insights preview grid, stat chip, connect/CTA block, etc.) into a new page, copy the markup from here, swap the placeholder content for page-specific content, and ship.

## How to use

1. Identify the pattern you want (see "Patterns" below)
2. Open the relevant `.html` snippet in this folder
3. Copy the markup
4. Paste into your target HTML file at the right insertion point
5. Replace placeholder strings (`<!-- TITLE -->`, `<!-- LINK -->`, `<!-- IMAGE-URL -->`, etc.) with real content
6. Verify visual rendering — the styling comes from `css/site.css` automatically because the markup uses shared classes

## How this differs from a real component system

This is a **markup template library**, not a runtime component system. The styling lives in `css/site.css` (shared classes) — that's what makes the pattern look right wherever you paste it. The HTML itself is just a copyable template; content varies intentionally per page.

For truly synchronized content across pages (where editing one source updates many), the right answer is a build step (Jekyll, Eleventy, etc.) or a different stack. We chose the markup-template approach because:

- Synced-content reuse is rare on a personal site (typically each page wants slightly different content even when the layout is shared)
- A build step adds local-development complexity that walks back the recent simplification away from Pug + SCSS
- The CSS consolidation in WS-1 already solved the styling-reuse half of the problem

If at any point you find yourself wanting truly synced content across 3+ pages, that's the trigger to revisit the build-step option.

## Patterns

> Folder is fresh as of 2026-04-26. Patterns get extracted here case-by-case as they prove worth reusing — typically when the same markup block has been copy-pasted to a third or fourth page.

(none populated yet)

## Adding a pattern

When a markup block is about to be copy-pasted for the third time:

1. Create `patterns/<pattern-name>.html` with just the markup block
2. Add an HTML comment block at the top describing:
   - The pattern's intent (what it does, when to use it)
   - Where it currently appears (which pages use it)
   - Required CSS classes (and which file they live in — usually `css/site.css`)
3. Use placeholder strings inside the markup: `<!-- TITLE -->`, `<!-- LINK -->`, `<!-- IMAGE-URL -->`, `<!-- DESCRIPTION -->`, etc. Make placeholders visually obvious so they're hard to miss when customizing.
4. Update the "Patterns" section above with a one-line entry: pattern name, what it is, where it currently appears
5. Commit with message `Add pattern: <pattern-name>`
