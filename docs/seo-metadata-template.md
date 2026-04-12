# 🔍 SEO & Metadata Standard

## 🤖 AI Directive

When creating or updating a `.html` file, you MUST use this exact `<head>` structure to ensure technical SEO compliance before any auditor skills run. Only replace the bracketed variables (e.g., `{{PAGE_TITLE}}`) with contextually appropriate content. Do not omit any tags.

---

## 1. Global `<head>` Boilerplate

_Every_ HTML page must include this exact structure within the `<head>` tags. Ensure paths map correctly depending on directory depth (e.g., `../assets/` for nested files).

```html
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />

<title>{{PAGE_TITLE}} | Jonathan Ibrahim</title>
<meta name="title" content="{{PAGE_TITLE}} | Jonathan Ibrahim" />
<meta name="description" content="{{150_CHARACTER_DESCRIPTION_MAX}}" />
<meta name="author" content="Jonathan Ibrahim" />
<link
    rel="canonical"
    href="[https://jonathanibrahim.com/](https://jonathanibrahim.com/){{PAGE_SLUG}}"
/>

<meta property="og:type" content="{{website_OR_article}}" />
<meta
    property="og:url"
    content="[https://jonathanibrahim.com/](https://jonathanibrahim.com/){{PAGE_SLUG}}"
/>
<meta property="og:title" content="{{PAGE_TITLE}} | Jonathan Ibrahim" />
<meta property="og:description" content="{{150_CHARACTER_DESCRIPTION_MAX}}" />
<meta
    property="og:image"
    content="[https://jonathanibrahim.com/assets/og-image.jpg](https://jonathanibrahim.com/assets/og-image.jpg)"
/>

<meta property="twitter:card" content="summary_large_image" />
<meta
    property="twitter:url"
    content="[https://jonathanibrahim.com/](https://jonathanibrahim.com/){{PAGE_SLUG}}"
/>
<meta property="twitter:title" content="{{PAGE_TITLE}} | Jonathan Ibrahim" />
<meta property="twitter:description" content="{{150_CHARACTER_DESCRIPTION_MAX}}" />
<meta
    property="twitter:image"
    content="[https://jonathanibrahim.com/assets/og-image.jpg](https://jonathanibrahim.com/assets/og-image.jpg)"
/>

<link rel="icon" type="image/x-icon" href="assets/favicon.ico" />
<link rel="apple-touch-icon" href="assets/apple-touch-icon.png" />
```

---

## 2. JSON-LD Structured Data Schema

### A. Person / Identity Schema

**Use Case:** ONLY insert this script block at the bottom of the `<head>` on `index.html` and `about.html`. Do not put this on every page.

```html
<script type="application/ld+json">
    {
        "@context": "[https://schema.org/](https://schema.org/)",
        "@type": "Person",
        "name": "Jonathan Ibrahim",
        "url": "[https://jonathanibrahim.com](https://jonathanibrahim.com)",
        "image": "[https://jonathanibrahim.com/assets/headshot.jpg](https://jonathanibrahim.com/assets/headshot.jpg)",
        "jobTitle": "Head of Project Management",
        "worksFor": {
            "@type": "Organization",
            "name": "WISE Digital Partners"
        },
        "sameAs": [
            "[https://www.linkedin.com/in/jonathanibrahim/](https://www.linkedin.com/in/jonathanibrahim/)"
        ]
    }
</script>
```

### B. Article Schema

**Use Case:** ONLY insert this script block at the bottom of the `<head>` on individual blog posts inside the `/insights/` directory or individual case studies inside the `/case-studies/` directory.

```html
<script type="application/ld+json">
    {
        "@context": "[https://schema.org](https://schema.org)",
        "@type": "Article",
        "mainEntityOfPage": {
            "@type": "WebPage",
            "@id": "[https://jonathanibrahim.com/](https://jonathanibrahim.com/){{PAGE_SLUG}}"
        },
        "headline": "{{PAGE_TITLE}}",
        "description": "{{150_CHARACTER_DESCRIPTION_MAX}}",
        "image": "[https://jonathanibrahim.com/assets/og-image.jpg](https://jonathanibrahim.com/assets/og-image.jpg)",
        "author": {
            "@type": "Person",
            "name": "Jonathan Ibrahim",
            "url": "[https://jonathanibrahim.com](https://jonathanibrahim.com)"
        },
        "publisher": {
            "@type": "Organization",
            "name": "Jonathan Ibrahim",
            "logo": {
                "@type": "ImageObject",
                "url": "[https://jonathanibrahim.com/assets/favicon.ico](https://jonathanibrahim.com/assets/favicon.ico)"
            }
        },
        "datePublished": "{{YYYY-MM-DD}}",
        "dateModified": "{{YYYY-MM-DD}}"
    }
</script>
```
