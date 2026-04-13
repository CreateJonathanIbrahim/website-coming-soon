# SEO & Metadata Standard

**Version:** 1.0  
**Last Updated:** April 12, 2026  
**Maintained By:** Jonathan Ibrahim  

**Change Log:**
- 2026-04-12: Initial version created with comprehensive SEO guidelines

---

## TL;DR — For AI/Claude Code

**DO NOT READ THIS ENTIRE FILE.** Use it as a reference library. Jump to the section you need.

### When Creating/Updating Pages:

**For ANY page:** Read [Section 2: Global Head Boilerplate](#2-global-head-boilerplate)
- Copy the complete `<head>` structure
- Replace `{{VARIABLES}}` with page-specific content
- Follow the og:type and image path rules in the tables

**For blog posts:** Also add [Section 3: Article-Specific Meta Tags](#3-article-specific-meta-tags)

**For JSON-LD:** Jump to [Section 4](#4-json-ld-structured-data), copy the relevant schema only:
- Homepage/About → Person Schema (4.A)
- Blog posts → BlogPosting Schema (4.B) + Breadcrumb Schema (4.D)
- Case studies → Case Study Schema (4.C) + Breadcrumb Schema (4.D)

**Need examples?** See bottom of document for complete working examples.

**Need testing tools?** Jump to [Section 8: Testing Checklist](#8-testing-checklist)

### Quick Reference Values (Pre-Filled):

```
Twitter: @JonCreates89
GitHub: CreateJonathanIbrahim
Default OG Image: assets/Jonathan_Ibrahim_Social_Media_Preview.jpg
Publisher Logo: assets/Jonathan_Ibrahim_Headshot_2026.jpg
Apple Touch Icon: assets/apple-touch-icon.png
Default Meta Description: "Head of Project Management specializing in Digital Marketing, ClickUp architecture, and cross-functional team coordination. Based in Austin, TX."
Timestamp Format: YYYY-MM-DD (date only, no times)
```

### File Structure (Jump to What You Need):

| Need | Go To |
|------|-------|
| Complete `<head>` template | [Section 2](#2-global-head-boilerplate) |
| Blog post meta tags | [Section 3](#3-article-specific-meta-tags) |
| JSON-LD schemas | [Section 4](#4-json-ld-structured-data) |
| Image specs and paths | [Section 5](#5-image-requirements) |
| Sitemap/robots.txt | [Section 6](#6-additional-seo-files) |
| Performance rules | [Section 7](#7-performance--technical-seo) |
| Validation tools | [Section 8](#8-testing-checklist) |
| Working examples | [Template Usage Examples](#template-usage-examples) |

**Remember:** Only read what you need for the current task. This is a reference document, not a sequential instruction manual.

---

## Table of Contents

1. [AI Directive](#1-ai-directive)
2. [Global Head Boilerplate](#2-global-head-boilerplate)
3. [Article-Specific Meta Tags](#3-article-specific-meta-tags)
4. [JSON-LD Structured Data](#4-json-ld-structured-data)
5. [Image Requirements](#5-image-requirements)
6. [Additional SEO Files](#6-additional-seo-files)
7. [Performance & Technical SEO](#7-performance--technical-seo)
8. [Testing Checklist](#8-testing-checklist)

---

## 1. AI Directive

When creating or updating any `.html` file, use the exact `<head>` structure defined in this document to ensure technical SEO compliance. Only replace the bracketed variables (e.g., `{{PAGE_TITLE}}`) with contextually appropriate content. Do not omit any required tags unless explicitly noted as optional.

**Key Principles:**
- Every page must have unique title and description
- All image paths must be absolute URLs (https://jonathanibrahim.com/...)
- Canonical URLs must match the actual page URL exactly
- Timestamps use YYYY-MM-DD format (no times)
- Character limits are hard limits (title: 60 chars, description: 155 chars)

---

## 2. Global Head Boilerplate

### Required Structure

Every HTML page must include this exact structure within the `<head>` tags.

**Path Rules:**
- Root-level pages (`index.html`, `about.html`, etc.): Use `assets/`
- Nested pages (`insights/post.html`, `case-studies/client.html`): Use `../assets/`

**Asset Status:**
All required assets exist in `assets/` directory:
- ✅ `Jonathan_Ibrahim_Social_Media_Preview.jpg` (1200×630px OG image)
- ✅ `Jonathan_Ibrahim_Headshot_2026.jpg` (square publisher logo)
- ✅ `apple-touch-icon.png` (180×180px iOS icon)
- ✅ Favicon: Inline SVG (no separate file)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#64a19d" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />

    <!-- Primary Meta Tags -->
    <title>{{PAGE_TITLE}} | Jonathan Ibrahim</title>
    <meta name="description" content="{{META_DESCRIPTION — max 155 characters}}" />
    <meta name="author" content="Jonathan Ibrahim" />
    <link rel="canonical" href="https://jonathanibrahim.com/{{PAGE_SLUG}}" />

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="{{website OR article — see rules below}}" />
    <meta property="og:site_name" content="Jonathan Ibrahim" />
    <meta property="og:url" content="https://jonathanibrahim.com/{{PAGE_SLUG}}" />
    <meta property="og:title" content="{{PAGE_TITLE}} | Jonathan Ibrahim" />
    <meta property="og:description" content="{{META_DESCRIPTION — max 155 characters}}" />
    <meta property="og:image" content="https://jonathanibrahim.com/{{IMAGE_PATH — see rules below}}" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />

    <!-- Twitter Card -->
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:url" content="https://jonathanibrahim.com/{{PAGE_SLUG}}" />
    <meta name="twitter:title" content="{{PAGE_TITLE}} | Jonathan Ibrahim" />
    <meta name="twitter:description" content="{{META_DESCRIPTION — max 155 characters}}" />
    <meta name="twitter:image" content="https://jonathanibrahim.com/{{IMAGE_PATH — see rules below}}" />
    <meta name="twitter:creator" content="@JonCreates89" />

    <!-- Favicon -->
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%23050505%22/><text x=%2250%22 y=%2274%22 text-anchor=%22middle%22 font-size=%2265%22 font-family=%22sans-serif%22 font-weight=%22900%22 fill=%22%2364a19d%22>JI</text></svg>" />
    <link rel="apple-touch-icon" href="{{assets/ OR ../assets/}}apple-touch-icon.png" />

    <!-- Google Search Console Verification (add when available) -->
    <!-- <meta name="google-site-verification" content="YOUR_VERIFICATION_CODE" /> -->

    <!-- Analytics (add when implemented) -->
    <!-- Example: Google Analytics 4 -->
    <!-- <script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script> -->
</head>
```

### Content Type Rules (`og:type`)

| Page Type | `og:type` Value |
|-----------|----------------|
| Homepage (`index.html`) | `website` |
| About page (`about.html`) | `website` |
| Archive pages (`insights.html`, `case-studies.html`) | `website` |
| Individual blog posts (`insights/post-slug.html`) | `article` |
| Individual case studies (`case-studies/client-slug.html`) | `article` |

### Image Path Rules (`og:image` and `twitter:image`)

| Page Type | Image Path |
|-----------|-----------|
| Homepage, About, Archive pages | `assets/Jonathan_Ibrahim_Social_Media_Preview.jpg` |
| Blog posts (all) | `assets/Jonathan_Ibrahim_Social_Media_Preview.jpg` |
| Case studies (custom image available) | `assets/case-studies/{{CLIENT_SLUG}}-og.jpg` |
| Case studies (no custom image) | `assets/Jonathan_Ibrahim_Social_Media_Preview.jpg` |

**Always use absolute URLs:**
```html
<!-- Correct -->
<meta property="og:image" content="https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg" />

<!-- Wrong -->
<meta property="og:image" content="/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg" />
<meta property="og:image" content="assets/Jonathan_Ibrahim_Social_Media_Preview.jpg" />
```

### Robots Meta Tag

**Default:** Omit this tag on all public, indexable pages.

**Only add for these specific cases:**
```html
<!-- Use ONLY on draft pages, thank-you pages, or staging previews -->
<meta name="robots" content="noindex, nofollow" />
```

---

## 3. Article-Specific Meta Tags

### When to Use

Add these tags **only** to individual blog posts (`insights/post-slug.html`) and case studies (`case-studies/client-slug.html`).

**Do NOT add to:**
- Homepage
- About page
- Archive pages (insights.html, case-studies.html)

### Article Meta Tags

Insert these immediately after the standard Open Graph tags:

```html
<!-- Article-Specific Open Graph Tags (blog posts and case studies only) -->
<meta property="article:published_time" content="{{YYYY-MM-DD}}" />
<meta property="article:modified_time" content="{{YYYY-MM-DD}}" />
<meta property="article:author" content="https://jonathanibrahim.com/about" />
```

**Date Format Rules:**
- Use `YYYY-MM-DD` format only (no times, no time zones)
- `published_time`: Set once on creation, never change
- `modified_time`: Set equal to `published_time` on creation, update when content meaningfully changes

**Examples:**
```html
<!-- On creation (March 15, 2026) -->
<meta property="article:published_time" content="2026-03-15" />
<meta property="article:modified_time" content="2026-03-15" />

<!-- After major edit (April 20, 2026) -->
<meta property="article:published_time" content="2026-03-15" />
<meta property="article:modified_time" content="2026-04-20" />
```

---

## 4. JSON-LD Structured Data

### A. Person Schema (Identity)

**Use Case:** Insert at the bottom of `<head>` on `index.html` and `about.html` only.

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org/",
    "@type": "Person",
    "name": "Jonathan Ibrahim",
    "url": "https://jonathanibrahim.com",
    "image": "https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Headshot_2026.jpg",
    "jobTitle": "Head of Project Management",
    "description": "Head of Project Management specializing in Digital Marketing, ClickUp architecture, and cross-functional team coordination. Based in Austin, TX.",
    "worksFor": {
        "@type": "Organization",
        "name": "WISE Digital Partners"
    },
    "address": {
        "@type": "PostalAddress",
        "addressLocality": "Austin",
        "addressRegion": "TX",
        "addressCountry": "US"
    },
    "sameAs": [
        "https://www.linkedin.com/in/jonathanibrahim/",
        "https://github.com/CreateJonathanIbrahim",
        "https://twitter.com/JonCreates89"
    ]
}
</script>
```

**Optional additions (when available):**
- Add YouTube channel URL to `sameAs` array when created
- Add other professional profiles as needed

### B. Blog Post Schema

**Use Case:** Insert at the bottom of `<head>` on individual blog posts (`insights/`) only.

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://jonathanibrahim.com/{{PAGE_SLUG}}"
    },
    "headline": "{{PAGE_TITLE}}",
    "description": "{{META_DESCRIPTION — max 155 characters}}",
    "image": "https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg",
    "author": {
        "@type": "Person",
        "name": "Jonathan Ibrahim",
        "url": "https://jonathanibrahim.com"
    },
    "publisher": {
        "@type": "Organization",
        "name": "Jonathan Ibrahim",
        "logo": {
            "@type": "ImageObject",
            "url": "https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Headshot_2026.jpg"
        }
    },
    "datePublished": "{{YYYY-MM-DD}}",
    "dateModified": "{{YYYY-MM-DD}}"
}
</script>
```

**Date Rules:**
- `datePublished`: Set once on creation, never change
- `dateModified`: Set equal to `datePublished` on creation, update only when content is meaningfully edited (not for typo fixes)

### C. Case Study Schema

**Use Case:** Insert at the bottom of `<head>` on individual case studies (`case-studies/`) only.

```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Article",
    "mainEntityOfPage": {
        "@type": "WebPage",
        "@id": "https://jonathanibrahim.com/{{PAGE_SLUG}}"
    },
    "headline": "{{PAGE_TITLE}}",
    "description": "{{META_DESCRIPTION — max 155 characters}}",
    "image": "https://jonathanibrahim.com/{{IMAGE_PATH — see rules in Section 2}}",
    "author": {
        "@type": "Person",
        "name": "Jonathan Ibrahim",
        "url": "https://jonathanibrahim.com"
    },
    "publisher": {
        "@type": "Organization",
        "name": "Jonathan Ibrahim",
        "logo": {
            "@type": "ImageObject",
            "url": "https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Headshot_2026.jpg"
        }
    },
    "datePublished": "{{YYYY-MM-DD}}",
    "dateModified": "{{YYYY-MM-DD}}"
}
</script>
```

### D. Breadcrumb Schema

**Use Case:** Insert at the bottom of `<head>` on individual blog posts and case studies only.

**For blog posts:**
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://jonathanibrahim.com"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "Insights",
            "item": "https://jonathanibrahim.com/insights"
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": "{{PAGE_TITLE}}",
            "item": "https://jonathanibrahim.com/{{PAGE_SLUG}}"
        }
    ]
}
</script>
```

**For case studies:**
```html
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
        {
            "@type": "ListItem",
            "position": 1,
            "name": "Home",
            "item": "https://jonathanibrahim.com"
        },
        {
            "@type": "ListItem",
            "position": 2,
            "name": "Case Studies",
            "item": "https://jonathanibrahim.com/case-studies"
        },
        {
            "@type": "ListItem",
            "position": 3,
            "name": "{{PAGE_TITLE}}",
            "item": "https://jonathanibrahim.com/{{PAGE_SLUG}}"
        }
    ]
}
</script>
```

---

## 5. Image Requirements

### OG Image (Social Media Preview)

**File:** `assets/Jonathan_Ibrahim_Social_Media_Preview.jpg`  
**Dimensions:** 1200×630px (required for proper display on Facebook, LinkedIn, Twitter)  
**Format:** JPG (WebP not supported by all social platforms)  
**File Size:** <300KB (faster load on social platforms)  
**Purpose:** Used in all og:image and twitter:image tags

**Content Guidelines:**
- Include your name and/or key message
- Use brand colors (teal #64a19d as accent)
- Ensure text is readable at thumbnail size
- Avoid fine details that disappear when scaled down
- Test preview at https://www.opengraph.xyz/

**Current Image:** ✅ Exists in assets/

### Publisher Logo (JSON-LD)

**File:** `assets/Jonathan_Ibrahim_Headshot_2026.jpg`  
**Dimensions:** Square aspect ratio (minimum 200×200px)  
**Format:** JPG  
**Purpose:** Used in BlogPosting and Article schemas as publisher logo

**Current Image:** ✅ Exists in assets/

### Apple Touch Icon

**File:** `assets/apple-touch-icon.png`  
**Dimensions:** 180×180px (required for iOS home screen bookmarks)  
**Format:** PNG  
**Design:** Dark background (#050505) with teal "JI" monogram (#64a19d), matching inline SVG favicon

**Current Image:** ✅ Exists in assets/

### Favicon

**Implementation:** Inline SVG (no separate file)  
**Design:** Dark background (#050505), teal "JI" monogram (#64a19d), 20px border radius

**Current Implementation:** ✅ Inline SVG in all pages

```html
<link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%23050505%22/><text x=%2250%22 y=%2274%22 text-anchor=%22middle%22 font-size=%2265%22 font-family=%22sans-serif%22 font-weight=%22900%22 fill=%22%2364a19d%22>JI</text></svg>" />
```

### Case Study Custom Images (Optional)

**File Pattern:** `assets/case-studies/{{CLIENT_SLUG}}-og.jpg`  
**Dimensions:** 1200×630px  
**Format:** JPG  
**Purpose:** Optional custom OG images for individual case studies

**Implementation:**
- Create custom image for each case study if available
- If custom image doesn't exist, fall back to default `Jonathan_Ibrahim_Social_Media_Preview.jpg`
- Always use absolute URLs in meta tags

**Example:**
```html
<!-- Custom case study image exists -->
<meta property="og:image" content="https://jonathanibrahim.com/assets/case-studies/wise-digital-partners-og.jpg" />

<!-- No custom image, use default -->
<meta property="og:image" content="https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg" />
```

---

## 6. Additional SEO Files

### Sitemap.xml

**Location:** Root directory (`/sitemap.xml`)  
**Purpose:** Helps search engines discover and index all pages

**Template:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <!-- Homepage -->
    <url>
        <loc>https://jonathanibrahim.com/</loc>
        <lastmod>2026-04-12</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    
    <!-- About Page -->
    <url>
        <loc>https://jonathanibrahim.com/about</loc>
        <lastmod>2026-04-12</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    
    <!-- Insights Archive -->
    <url>
        <loc>https://jonathanibrahim.com/insights</loc>
        <lastmod>2026-04-12</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.7</priority>
    </url>
    
    <!-- Case Studies Archive -->
    <url>
        <loc>https://jonathanibrahim.com/case-studies</loc>
        <lastmod>2026-04-12</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    
    <!-- Individual Blog Post Example -->
    <url>
        <loc>https://jonathanibrahim.com/insights/post-slug</loc>
        <lastmod>2026-04-12</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>
    
    <!-- Individual Case Study Example -->
    <url>
        <loc>https://jonathanibrahim.com/case-studies/client-slug</loc>
        <lastmod>2026-04-12</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.6</priority>
    </url>
</urlset>
```

**Update Rules:**
- Regenerate whenever you add a new page
- Update `<lastmod>` when page content changes significantly (not for typos or minor edits)
- Submit to Google Search Console after updates

**Priority Guidelines:**

| Page Type | Priority | Change Frequency |
|-----------|----------|------------------|
| Homepage | 1.0 | weekly |
| About | 0.8 | monthly |
| Archive pages | 0.7 | weekly (insights) or monthly (case studies) |
| Individual posts | 0.6 | monthly |

### Robots.txt

**Location:** Root directory (`/robots.txt`)  
**Purpose:** Tells search engines which pages to crawl

**Standard Template (All Pages Public):**
```
User-agent: *
Allow: /

Sitemap: https://jonathanibrahim.com/sitemap.xml
```

**With Exclusions (If Needed):**
```
User-agent: *
Allow: /
Disallow: /drafts/
Disallow: /thank-you/
Disallow: /test/

Sitemap: https://jonathanibrahim.com/sitemap.xml
```

**Common Exclusions:**
- `/drafts/` - Work-in-progress content
- `/thank-you/` - Form confirmation pages
- `/test/` - Testing/staging pages
- `/private/` - Private or internal pages

---

## 7. Performance & Technical SEO

### Resource Loading Order

Optimize `<head>` tag order for fastest load:

1. **Critical meta tags** (charset, viewport)
2. **Preconnect to external domains:**
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
```
3. **Title and meta tags**
4. **CSS (defer non-critical):**
```html
<!-- Critical CSS inline in <head> for above-the-fold content -->
<style>
    /* Inline critical CSS here */
</style>

<!-- Non-critical CSS deferred -->
<link rel="stylesheet" href="css/styles.css" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="css/styles.css" /></noscript>
```
5. **Favicon and icons**
6. **Structured data (JSON-LD)**
7. **JavaScript (defer or async):**
```html
<script src="js/scripts.js" defer></script>
```

### Core Web Vitals Targets

**Required Performance Standards:**

| Metric | Target | Critical Threshold |
|--------|--------|-------------------|
| **Largest Contentful Paint (LCP)** | <2.5s | 4.0s |
| **First Input Delay (FID)** | <100ms | 300ms |
| **Cumulative Layout Shift (CLS)** | <0.1 | 0.25 |
| **First Contentful Paint (FCP)** | <1.8s | 3.0s |
| **Time to Interactive (TTI)** | <3.8s | 7.3s |

**Test Tools:**
- Google PageSpeed Insights: https://pagespeed.web.dev/
- Chrome DevTools Lighthouse
- Web.dev Measure: https://web.dev/measure/

### Image Optimization

**Required Practices:**

1. **Format:**
   - Use WebP with JPG fallback for photos
   - Use SVG for icons and logos
   - Use PNG only when transparency required (not WebP-compatible)

2. **Compression:**
   - Compress all images to <200KB each
   - Tools: TinyPNG (https://tinypng.com/), Squoosh (https://squoosh.app/)

3. **Lazy Loading:**
```html
<!-- All images except above-the-fold hero -->
<img src="image.jpg" alt="Description" loading="lazy" width="800" height="600" />
```

4. **Dimensions:**
   - Always include width and height attributes
   - Prevents layout shift (improves CLS score)
   - Use actual rendered dimensions

5. **Alt Text:**
   - Every image must have descriptive alt text
   - Exception: Decorative images use `alt=""`
   - Max 125 characters, describe content, include keywords naturally

**Example:**
```html
<img 
    src="assets/project-screenshot.jpg" 
    alt="ClickUp workspace dashboard showing project timeline and task dependencies"
    width="1200" 
    height="800" 
    loading="lazy"
/>
```

### Font Loading

**Optimal Strategy:**

```html
<head>
    <!-- Preconnect to Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    
    <!-- Load fonts with display=swap -->
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&family=Playfair+Display:wght@700&display=swap" rel="stylesheet" />
</head>
```

**display=swap:**
- Shows fallback font immediately
- Swaps to web font when loaded
- Prevents invisible text (FOIT)

---

## 8. Testing Checklist

### Before Publishing Any New Page

**Required Validation:**

- [ ] **HTML Validation**  
  Tool: https://validator.w3.org/  
  Must pass with zero errors

- [ ] **Meta Tags Review**  
  Tool: https://metatags.io/  
  Check: title length, description length, OG preview

- [ ] **Open Graph Preview**  
  Tool: https://www.opengraph.xyz/  
  Verify: image displays correctly, title/description accurate

- [ ] **Twitter Card Preview**  
  Tool: https://cards-dev.twitter.com/validator (if available)  
  Verify: large image card displays correctly

- [ ] **Structured Data**  
  Tool: https://search.google.com/test/rich-results  
  Must pass with zero errors or warnings

- [ ] **Mobile-Friendly Test**  
  Tool: https://search.google.com/test/mobile-friendly  
  Must pass

- [ ] **Page Speed**  
  Tool: https://pagespeed.web.dev/  
  Target: 90+ on all metrics (Performance, Accessibility, Best Practices, SEO)

**Optional Validation:**

- [ ] **Schema Markup Validator**  
  Tool: https://validator.schema.org/  
  Paste page URL or HTML

- [ ] **Broken Links Check**  
  Tool: https://validator.w3.org/checklink  
  Check all internal and external links

- [ ] **Accessibility Audit**  
  Tool: Chrome DevTools Lighthouse  
  Target: 95+ accessibility score

### Manual Verification Checklist

**Before publishing, manually verify:**

- [ ] Page title under 60 characters (including " | Jonathan Ibrahim")
- [ ] Meta description under 155 characters
- [ ] Canonical URL matches actual page URL exactly
- [ ] All images have descriptive alt text (not generic "image" or filename)
- [ ] OG image displays correctly in social preview tools
- [ ] All links work (no 404s)
- [ ] Mobile responsive on 375px, 768px, 1024px, 1440px viewports
- [ ] Page loads in <3 seconds on 3G connection
- [ ] No console errors in browser DevTools
- [ ] JSON-LD dates in correct YYYY-MM-DD format
- [ ] All absolute URLs use https:// (not http://)

### Post-Publication Monitoring

**Within 24-48 hours:**

- [ ] Verify page appears in Google Search Console "Coverage" report
- [ ] Check for any crawl errors in Search Console
- [ ] Test live URL in social media preview tools (LinkedIn, Twitter)
- [ ] Verify sitemap.xml updated and submitted to Search Console

**Within 1-2 weeks:**

- [ ] Monitor Google Search Console for impressions/clicks
- [ ] Check for any mobile usability issues
- [ ] Review Core Web Vitals report

---

## Quick Reference Tables

### Page-Specific Meta Tag Requirements

| Page Type | og:type | Image Path | Article Tags | BlogPosting Schema | Breadcrumb Schema |
|-----------|---------|------------|--------------|-------------------|-------------------|
| Homepage | website | default OG | ❌ | ❌ | ❌ |
| About | website | default OG | ❌ | ❌ | ❌ |
| Insights Archive | website | default OG | ❌ | ❌ | ❌ |
| Case Studies Archive | website | default OG | ❌ | ❌ | ❌ |
| Individual Blog Post | article | default OG | ✅ | ✅ | ✅ |
| Individual Case Study | article | custom or default | ✅ | Article Schema | ✅ |

### Character Limits Reference

| Element | Ideal Length | Maximum | Hard Cutoff |
|---------|-------------|---------|-------------|
| Page Title (without " \| Jonathan Ibrahim") | 40-50 chars | 60 chars | Google truncates at ~60 |
| Meta Description | 140-155 chars | 155 chars | Google truncates at ~155 |
| OG Title | 60-90 chars | 95 chars | Facebook truncates at ~95 |
| OG Description | 140-155 chars | 200 chars | Facebook truncates at ~200 |
| Image Alt Text | 80-125 chars | 125 chars | Screen readers may cut off |

### Common Page Slugs

| Page Type | Example Slug | Full URL |
|-----------|--------------|----------|
| Homepage | (empty) | https://jonathanibrahim.com/ |
| About | about | https://jonathanibrahim.com/about |
| Insights Archive | insights | https://jonathanibrahim.com/insights |
| Case Studies Archive | case-studies | https://jonathanibrahim.com/case-studies |
| Blog Post | insights/post-title | https://jonathanibrahim.com/insights/post-title |
| Case Study | case-studies/client-name | https://jonathanibrahim.com/case-studies/client-name |

---

## Template Usage Examples

### Example 1: Homepage (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#64a19d" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />

    <title>Strategic Operations Leader & Head of Project Management | Jonathan Ibrahim</title>
    <meta name="description" content="Head of Project Management specializing in Digital Marketing, ClickUp architecture, and cross-functional team coordination. Based in Austin, TX." />
    <meta name="author" content="Jonathan Ibrahim" />
    <link rel="canonical" href="https://jonathanibrahim.com/" />

    <meta property="og:type" content="website" />
    <meta property="og:site_name" content="Jonathan Ibrahim" />
    <meta property="og:url" content="https://jonathanibrahim.com/" />
    <meta property="og:title" content="Strategic Operations Leader & Head of Project Management | Jonathan Ibrahim" />
    <meta property="og:description" content="Head of Project Management specializing in Digital Marketing, ClickUp architecture, and cross-functional team coordination. Based in Austin, TX." />
    <meta property="og:image" content="https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />

    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:url" content="https://jonathanibrahim.com/" />
    <meta name="twitter:title" content="Strategic Operations Leader & Head of Project Management | Jonathan Ibrahim" />
    <meta name="twitter:description" content="Head of Project Management specializing in Digital Marketing, ClickUp architecture, and cross-functional team coordination. Based in Austin, TX." />
    <meta name="twitter:image" content="https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg" />
    <meta name="twitter:creator" content="@JonCreates89" />

    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%23050505%22/><text x=%2250%22 y=%2274%22 text-anchor=%22middle%22 font-size=%2265%22 font-family=%22sans-serif%22 font-weight=%22900%22 fill=%22%2364a19d%22>JI</text></svg>" />
    <link rel="apple-touch-icon" href="assets/apple-touch-icon.png" />

    <!-- Person Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org/",
        "@type": "Person",
        "name": "Jonathan Ibrahim",
        "url": "https://jonathanibrahim.com",
        "image": "https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Headshot_2026.jpg",
        "jobTitle": "Head of Project Management",
        "description": "Head of Project Management specializing in Digital Marketing, ClickUp architecture, and cross-functional team coordination. Based in Austin, TX.",
        "worksFor": {
            "@type": "Organization",
            "name": "WISE Digital Partners"
        },
        "address": {
            "@type": "PostalAddress",
            "addressLocality": "Austin",
            "addressRegion": "TX",
            "addressCountry": "US"
        },
        "sameAs": [
            "https://www.linkedin.com/in/jonathanibrahim/",
            "https://github.com/CreateJonathanIbrahim",
            "https://twitter.com/JonCreates89"
        ]
    }
    </script>
</head>
```

### Example 2: Blog Post (insights/clickup-architecture-guide.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#64a19d" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />

    <title>How to Architect ClickUp for 50+ Users | Jonathan Ibrahim</title>
    <meta name="description" content="A complete guide to designing ClickUp workspaces that scale. From hierarchy decisions to automation strategies for growing teams." />
    <meta name="author" content="Jonathan Ibrahim" />
    <link rel="canonical" href="https://jonathanibrahim.com/insights/clickup-architecture-guide" />

    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="Jonathan Ibrahim" />
    <meta property="og:url" content="https://jonathanibrahim.com/insights/clickup-architecture-guide" />
    <meta property="og:title" content="How to Architect ClickUp for 50+ Users | Jonathan Ibrahim" />
    <meta property="og:description" content="A complete guide to designing ClickUp workspaces that scale. From hierarchy decisions to automation strategies for growing teams." />
    <meta property="og:image" content="https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />

    <!-- Article-specific tags -->
    <meta property="article:published_time" content="2026-04-12" />
    <meta property="article:modified_time" content="2026-04-12" />
    <meta property="article:author" content="https://jonathanibrahim.com/about" />

    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:url" content="https://jonathanibrahim.com/insights/clickup-architecture-guide" />
    <meta name="twitter:title" content="How to Architect ClickUp for 50+ Users | Jonathan Ibrahim" />
    <meta name="twitter:description" content="A complete guide to designing ClickUp workspaces that scale. From hierarchy decisions to automation strategies for growing teams." />
    <meta name="twitter:image" content="https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg" />
    <meta name="twitter:creator" content="@JonCreates89" />

    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%23050505%22/><text x=%2250%22 y=%2274%22 text-anchor=%22middle%22 font-size=%2265%22 font-family=%22sans-serif%22 font-weight=%22900%22 fill=%22%2364a19d%22>JI</text></svg>" />
    <link rel="apple-touch-icon" href="../assets/apple-touch-icon.png" />

    <!-- BlogPosting Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BlogPosting",
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": "https://jonathanibrahim.com/insights/clickup-architecture-guide"
        },
        "headline": "How to Architect ClickUp for 50+ Users",
        "description": "A complete guide to designing ClickUp workspaces that scale. From hierarchy decisions to automation strategies for growing teams.",
        "image": "https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Social_Media_Preview.jpg",
        "author": {
            "@type": "Person",
            "name": "Jonathan Ibrahim",
            "url": "https://jonathanibrahim.com"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Jonathan Ibrahim",
            "logo": {
                "@type": "ImageObject",
                "url": "https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Headshot_2026.jpg"
            }
        },
        "datePublished": "2026-04-12",
        "dateModified": "2026-04-12"
    }
    </script>

    <!-- Breadcrumb Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://jonathanibrahim.com"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Insights",
                "item": "https://jonathanibrahim.com/insights"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": "How to Architect ClickUp for 50+ Users",
                "item": "https://jonathanibrahim.com/insights/clickup-architecture-guide"
            }
        ]
    }
    </script>
</head>
```

### Example 3: Case Study with Custom Image (case-studies/wise-digital-partners.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="theme-color" content="#64a19d" />
    <meta name="referrer" content="strict-origin-when-cross-origin" />

    <title>WISE Digital Partners: Building Delivery Infrastructure | Jonathan Ibrahim</title>
    <meta name="description" content="How I architected ClickUp infrastructure for 52 users, achieving 96% client retention and 91% revenue expansion across 20 concurrent projects." />
    <meta name="author" content="Jonathan Ibrahim" />
    <link rel="canonical" href="https://jonathanibrahim.com/case-studies/wise-digital-partners" />

    <meta property="og:type" content="article" />
    <meta property="og:site_name" content="Jonathan Ibrahim" />
    <meta property="og:url" content="https://jonathanibrahim.com/case-studies/wise-digital-partners" />
    <meta property="og:title" content="WISE Digital Partners: Building Delivery Infrastructure | Jonathan Ibrahim" />
    <meta property="og:description" content="How I architected ClickUp infrastructure for 52 users, achieving 96% client retention and 91% revenue expansion across 20 concurrent projects." />
    <meta property="og:image" content="https://jonathanibrahim.com/assets/case-studies/wise-digital-partners-og.jpg" />
    <meta property="og:image:width" content="1200" />
    <meta property="og:image:height" content="630" />

    <!-- Article-specific tags -->
    <meta property="article:published_time" content="2026-04-12" />
    <meta property="article:modified_time" content="2026-04-12" />
    <meta property="article:author" content="https://jonathanibrahim.com/about" />

    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:url" content="https://jonathanibrahim.com/case-studies/wise-digital-partners" />
    <meta name="twitter:title" content="WISE Digital Partners: Building Delivery Infrastructure | Jonathan Ibrahim" />
    <meta name="twitter:description" content="How I architected ClickUp infrastructure for 52 users, achieving 96% client retention and 91% revenue expansion across 20 concurrent projects." />
    <meta name="twitter:image" content="https://jonathanibrahim.com/assets/case-studies/wise-digital-partners-og.jpg" />
    <meta name="twitter:creator" content="@JonCreates89" />

    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><rect width=%22100%22 height=%22100%22 rx=%2220%22 fill=%22%23050505%22/><text x=%2250%22 y=%2274%22 text-anchor=%22middle%22 font-size=%2265%22 font-family=%22sans-serif%22 font-weight=%22900%22 fill=%22%2364a19d%22>JI</text></svg>" />
    <link rel="apple-touch-icon" href="../assets/apple-touch-icon.png" />

    <!-- Article Schema (for case studies) -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "Article",
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": "https://jonathanibrahim.com/case-studies/wise-digital-partners"
        },
        "headline": "WISE Digital Partners: Building Delivery Infrastructure",
        "description": "How I architected ClickUp infrastructure for 52 users, achieving 96% client retention and 91% revenue expansion across 20 concurrent projects.",
        "image": "https://jonathanibrahim.com/assets/case-studies/wise-digital-partners-og.jpg",
        "author": {
            "@type": "Person",
            "name": "Jonathan Ibrahim",
            "url": "https://jonathanibrahim.com"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Jonathan Ibrahim",
            "logo": {
                "@type": "ImageObject",
                "url": "https://jonathanibrahim.com/assets/Jonathan_Ibrahim_Headshot_2026.jpg"
            }
        },
        "datePublished": "2026-04-12",
        "dateModified": "2026-04-12"
    }
    </script>

    <!-- Breadcrumb Schema -->
    <script type="application/ld+json">
    {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": 1,
                "name": "Home",
                "item": "https://jonathanibrahim.com"
            },
            {
                "@type": "ListItem",
                "position": 2,
                "name": "Case Studies",
                "item": "https://jonathanibrahim.com/case-studies"
            },
            {
                "@type": "ListItem",
                "position": 3,
                "name": "WISE Digital Partners: Building Delivery Infrastructure",
                "item": "https://jonathanibrahim.com/case-studies/wise-digital-partners"
            }
        ]
    }
    </script>
</head>
```

---

## Maintenance & Updates

### When to Update This Document

- New social platforms require different meta tags
- Google/search engines change structured data requirements
- New image assets added to the site
- Core Web Vitals targets change
- New pages or page types added to site structure

### Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-04-12 | Initial comprehensive SEO template created |

---

**Document maintained by Jonathan Ibrahim**  
**Questions or updates needed? Contact: create@jonathanibrahim.com**
