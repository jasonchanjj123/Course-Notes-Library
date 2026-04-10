# Universal Study Guide Design System

> **Purpose:** This document is the single source of truth for building, extending, and maintaining every chapter study guide across **all courses** in this library — Financial Markets, Statistics, Machine Learning, Calculus, and any future subject. Follow it when writing a new chapter, starting a new course, retrofitting an old guide, or adding new component types.

---

## Table of Contents

1. [Design Philosophy](#1-design-philosophy)
2. [Library Architecture](#2-library-architecture)
3. [Typography System](#3-typography-system)
4. [Color Architecture](#4-color-architecture)
5. [Layout Structure](#5-layout-structure)
6. [CSS Variable Reference](#6-css-variable-reference)
7. [Component Library](#7-component-library)
   - [A · Page Hero](#a-page-hero)
   - [B · Section Header](#b-section-header)
   - [C · Prose & Text Utilities](#c-prose--text-utilities)
   - [D · Callout Boxes](#d-callout-boxes)
   - [E · Concept Cards & Grids](#e-concept-cards--grids)
   - [F · Flow Diagrams](#f-flow-diagrams)
   - [G · Formula Boxes](#g-formula-boxes)
   - [H · Comparison Tables](#h-comparison-tables)
   - [I · Flashcard Carousel](#i-flashcard-carousel)
   - [J · Feynman Explanation Cards](#j-feynman-explanation-cards)
   - [K · Knowledge Graph (SVG)](#k-knowledge-graph-svg)
   - [L · Exercise Tiers](#l-exercise-tiers)
   - [M · Cheat Sheet Cards](#m-cheat-sheet-cards)
   - [N · Code Block (STEM courses)](#n-code-block-stem-courses)
   - [O · Proof / Derivation Panel](#o-proof--derivation-panel)
8. [Course-Type Adaptations](#8-course-type-adaptations)
9. [JavaScript Architecture](#9-javascript-architecture)
10. [Dark Mode System](#10-dark-mode-system)
11. [Six-Section Structure](#11-six-section-structure)
12. [Multi-Chapter Assembly (Unified Hub)](#12-multi-chapter-assembly-unified-hub)
13. [New Course Setup Checklist](#13-new-course-setup-checklist)
14. [New Chapter Checklist](#14-new-chapter-checklist)
15. [Naming Conventions](#15-naming-conventions)
16. [Anti-Patterns to Avoid](#16-anti-patterns-to-avoid)

---

## 1. Design Philosophy

Every study guide is built around one principle: **active recall beats passive re-reading**. The design enforces this by organizing content into six distinct cognitive modes (Summary → Flashcards → Feynman → Graph → Exercises → Cheat Sheet), each targeting a different type of learning regardless of subject matter.

### Visual Language

The aesthetic is **editorial academic** — the authority and warmth of a well-typeset textbook combined with the density of a reference manual. The visual language adapts slightly by course type (see §8) but the structural vocabulary is constant:

- **Dark navy sidebar** anchors every page, creating a consistent workspace feel across all courses.
- **Chapter accent colors** provide visual identity per chapter without changing structural CSS.
- **Course accent families** group related chapters: a Finance course might use warm earth tones; a Statistics course might use cool blues; Machine Learning might use indigos and violets.
- **Serif display headings** (Playfair Display) give weight and hierarchy to section titles.
- **Sans-serif body** (Source Sans 3) ensures comfortable long-form reading.
- **Monospace labels** (JetBrains Mono) handle metadata, badges, code, and formula values — never body text.

### Guiding Rules

1. **One accent color per chapter.** It appears in the sidebar nav highlights, hero gradient, section badges, and callout borders. Never introduce a second accent per chapter.
2. **No layout changes between chapters or courses.** Structure is identical everywhere. Only colors, content, and course-type component choices change.
3. **Enrichment is always flagged.** Any content added beyond the raw lecture notes must carry a 📝 marker so students know what comes from slides vs. what was added by Claude.
4. **Every component is accessible.** Interactive elements have keyboard support (`tabindex`, `aria-*` labels). Color is never the sole means of conveying information.
5. **Course context is always visible.** The sidebar header shows both the **course name** and the **chapter number + title** at a glance — a student should know where they are within a fraction of a second.

---

## 2. Library Architecture

### Folder Structure

```
Course-Notes-Library/
├── STUDY-GUIDE-DESIGN-SYSTEM.md         ← this file (lives at root)
│
├── financial-markets/
│   ├── financial-markets-complete-study-guide.html   ← unified multi-chapter hub
│   ├── study-guide-ch01-financial-markets.html
│   ├── study-guide-ch02-interest-rates.html
│   ├── study-guide-ch03-security-valuation.html
│   ├── study-guide-ch04-federal-reserve.html
│   └── source/                          ← raw lecture PDFs / pptx (read-only)
│
├── statistics/
│   ├── statistics-complete-study-guide.html
│   ├── study-guide-ch01-descriptive-statistics.html
│   ├── study-guide-ch02-probability.html
│   └── source/
│
├── machine-learning/
│   ├── machine-learning-complete-study-guide.html
│   ├── study-guide-ch01-linear-regression.html
│   ├── study-guide-ch02-classification.html
│   └── source/
│
├── calculus/
│   ├── calculus-complete-study-guide.html
│   └── source/
│
└── {new-course}/
    ├── {new-course}-complete-study-guide.html
    └── source/
```

### File Naming Convention

```
study-guide-ch{NN}-{topic-slug}.html
```

- `NN` is zero-padded: `ch01`, `ch02`, ... `ch10`, `ch11`
- `topic-slug` is lowercase, hyphenated: `linear-regression`, `central-limit-theorem`
- Examples:
  - `study-guide-ch03-hypothesis-testing.html`
  - `study-guide-ch07-neural-networks.html`
  - `study-guide-ch02-interest-rates.html`

The unified hub for each course is always:
```
{course-slug}-complete-study-guide.html
```

---

## 3. Typography System

All chapters across all courses use the same three-font stack, loaded from Google Fonts.

```html
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Source+Sans+3:ital,wght@0,300;0,400;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

### Font Roles

| Font | Role | Used For |
|------|------|----------|
| `Playfair Display` | Display / Serif | `h1`, `h2`, hero titles, sidebar title |
| `Source Sans 3` | Body / Sans | All body text, paragraphs, labels, buttons |
| `JetBrains Mono` | Monospace | Section badges, nav labels, code, formula values, metadata tags |

### Type Scale

```css
h1  { font-family: 'Playfair Display'; font-size: 2.6rem; font-weight: 700; }
h2  { font-family: 'Playfair Display'; font-size: 1.8rem; font-weight: 600; }
h3  { font-family: 'Playfair Display'; font-size: 1.3rem; font-weight: 600; }
h4  { font-family: 'Source Sans 3';   font-size: 1rem;   font-weight: 600; }

p, li { font-family: 'Source Sans 3'; font-size: 1rem;   line-height: 1.75; }

.badge, .label, code {
  font-family: 'JetBrains Mono';
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}
```

### Rules

- **Never use Inter, Roboto, Arial, or system fonts** for display headings.
- `h1` appears only once per page (the hero title). `h2` opens each named topic within Section A.
- Heading hierarchy must be respected: `h2 → h3 → h4` — never skip levels.
- Bold (`<strong>`) is used for **key term introduction** on first mention only, not general emphasis.
- Italic (`<em>`) is used for titles, variable names in prose, and clarifying asides.
- For STEM courses: mathematical symbols in prose use `<em>` or a proper `<code>` inline span, never pasted Unicode math characters in body font.

---

## 4. Color Architecture

### Course Color Families

Each course is assigned a **color family** — a group of related hues, one per chapter. Chapters within a course share a tonal family while remaining visually distinct.

#### Current Course Assignments

| Course | Family | Hue Range |
|--------|--------|-----------|
| Financial Markets | **Warm Earth** | Gold → Teal → Emerald → Sienna |
| Statistics | **Cool Blue** | Steel Blue → Slate → Cyan → Ice |
| Machine Learning | **Deep Indigo** | Violet → Purple → Indigo → Lavender |
| Calculus | **Forest Green** | Pine → Sage → Moss → Fern |
| (New Course) | Pick from: Rose, Amber, Copper, Crimson, Ocean | — |

#### Chapter Accent Palette — Financial Markets

| Chapter | Accent Name | Base | Light | Pale | Border |
|---------|------------|------|-------|------|--------|
| Ch. 1 · Financial Markets | Gold | `#c9a84c` | `#e8c97a` | `#f5e9c8` | `rgba(201,168,76,0.25)` |
| Ch. 2 · Interest Rates | Teal | `#0e7490` | `#22d3ee` | `#ecfeff` | `rgba(14,116,144,0.20)` |
| Ch. 3 · Security Valuation | Emerald | `#065f46` | `#34d399` | `#ecfdf5` | `rgba(6,95,70,0.18)` |
| Ch. 4 · Federal Reserve | Sienna | `#8b4513` | `#c0623a` | `#f5e9e0` | `rgba(139,69,19,0.20)` |

#### Chapter Accent Palette — Statistics (recommended)

| Chapter | Accent Name | Base | Light | Pale | Border |
|---------|------------|------|-------|------|--------|
| Ch. 1 · Descriptive Stats | Steel Blue | `#1d4e89` | `#4a90d9` | `#eaf3fd` | `rgba(29,78,137,0.22)` |
| Ch. 2 · Probability | Slate | `#334155` | `#64748b` | `#f1f5f9` | `rgba(51,65,85,0.20)` |
| Ch. 3 · Distributions | Cyan | `#0369a1` | `#38bdf8` | `#e0f7ff` | `rgba(3,105,161,0.20)` |
| Ch. 4 · Hypothesis Testing | Ice | `#155e75` | `#67e8f9` | `#ecfeff` | `rgba(21,94,117,0.20)` |

#### Chapter Accent Palette — Machine Learning (recommended)

| Chapter | Accent Name | Base | Light | Pale | Border |
|---------|------------|------|-------|------|--------|
| Ch. 1 · Linear Regression | Violet | `#5b21b6` | `#8b5cf6` | `#f5f3ff` | `rgba(91,33,182,0.20)` |
| Ch. 2 · Classification | Purple | `#7e22ce` | `#c084fc` | `#faf5ff` | `rgba(126,34,206,0.20)` |
| Ch. 3 · Neural Networks | Indigo | `#3730a3` | `#818cf8` | `#eef2ff` | `rgba(55,48,163,0.20)` |
| Ch. 4 · Regularization | Lavender | `#4c1d95` | `#a78bfa` | `#f5f3ff` | `rgba(76,29,149,0.20)` |

> **Adding new chapters:** pick an accent that is visually distinct from all existing ones in the same course. Each accent needs four values: `base`, `light` (tinted, ~40% lighter), `pale` (very light bg, ~90% lighter), and `border` (rgba at 20–25% opacity).

> **Adding new courses:** pick a color family not yet assigned. Avoid duplicating the warm earth tones already used by Financial Markets.

### Shared Semantic Colors

These are identical across all courses and must not be changed:

```css
--navy:       #0d1b2a   /* sidebar background */
--navy-mid:   #1b2e45   /* sidebar hover states */
--navy-light: #243b55   /* sidebar active bg */
--cream:      #faf7f0   /* page background (light mode) */
--cream-dark: #f0ead8   /* surface, card bg (light mode) */
--text-dark:  #1a1a2e   /* headings */
--text-body:  #2d3748   /* body text */
--text-muted: #718096   /* secondary text, hints */
--green:      #276749   /* correct / positive */
--green-light:#e6f4ed   /* correct / positive bg */
--amber:      #b7791f   /* warning */
--amber-light:#fefce8   /* warning bg */
--red:        #9b2335   /* error / danger */
--red-light:  #fff1f2   /* error / danger bg */
--blue-accent:#2b6cb0   /* links, info */
--blue-light: #ebf4ff   /* info bg */
```

### Hero Gradient

Each chapter's hero uses a dark gradient: navy base + accent dark tint:

```css
/* Formula: linear-gradient(135deg, #0d1b2a 0%, {accent @ 60% darker} 55%, {accent @ 75% darker} 100%) */

/* Example — Gold (Financial Markets Ch.1) */
background: linear-gradient(135deg, #0d1b2a 0%, #2a1f05 55%, #1a1200 100%);

/* Example — Steel Blue (Statistics Ch.1) */
background: linear-gradient(135deg, #0d1b2a 0%, #0c2240 55%, #081525 100%);

/* Example — Violet (Machine Learning Ch.1) */
background: linear-gradient(135deg, #0d1b2a 0%, #2e1065 55%, #1a0840 100%);
```

---

## 5. Layout Structure

Every chapter page across every course uses this identical three-zone layout:

```
┌──────────────────────────────────────────────────────────┐
│  SIDEBAR (fixed, 270px)   │  MAIN CONTENT (flex: 1)      │
│  ┌──────────────────────┐ │  ┌──────────────────────────┐ │
│  │ Course label          │ │  │ PAGE HERO (gradient bg)  │ │
│  │ Chapter title         │ │  ├──────────────────────────┤ │
│  ├──────────────────────┤ │  │ CONTENT WRAPPER           │ │
│  │ NAV LINKS             │ │  │ max-width: 960px          │ │
│  │ · Section A–F         │ │  │ padding: 48px 60px        │ │
│  │ · Key topic anchors   │ │  │                           │ │
│  ├──────────────────────┤ │  │   Section A               │ │
│  │ Dark mode toggle      │ │  │   Section B               │ │
│  └──────────────────────┘ │  │   ...                     │ │
│                            │  └──────────────────────────┘ │
└──────────────────────────────────────────────────────────┘
```

### Sidebar Specs

```css
.sidebar {
  width: var(--sidebar-width);    /* 270px */
  min-height: 100vh;
  background: var(--navy);
  position: fixed;
  top: 0; left: 0; bottom: 0;
  overflow-y: auto;
  z-index: 100;
  display: flex;
  flex-direction: column;
}
```

**Sidebar anatomy (top → bottom):**
1. `.sidebar-header` — course label (small, muted) + chapter title (larger, accent-colored)
2. `<nav>` — navigation links in two groups: Sections (A–F) then Key Topics
3. `.sidebar-footer` — dark mode toggle button

The course label in the sidebar header is the course short name (e.g., "Financial Markets", "Statistics 101", "ML Fundamentals"). It appears above the chapter title in a smaller, muted color, so the hierarchy course → chapter is always visible.

### Main Content Specs

```css
.main {
  margin-left: var(--sidebar-width);
  flex: 1;
  min-width: 0;
}
.content {
  padding: 48px 60px 80px;
  max-width: 960px;
}
@media (max-width: 768px) {
  .main { margin-left: 0; }
  .content { padding: 32px 24px 60px; }
}
```

### Mobile Behavior

- Sidebar collapses off-screen at ≤ 768px.
- A hamburger button (`.mobile-menu-btn`) appears fixed at top-left.
- Tapping outside the sidebar (`.sidebar-overlay`) closes it.
- All layout shifts use CSS `transform`, not `display` toggling.

---

## 6. CSS Variable Reference

Copy this block verbatim as the `:root {}` for any new chapter in any course. Replace only the accent section.

```css
:root {
  /* ── STRUCTURAL (never change) ── */
  --navy:          #0d1b2a;
  --navy-mid:      #1b2e45;
  --navy-light:    #243b55;
  --sidebar-width: 270px;
  --shadow:        0 4px 24px rgba(13, 27, 42, 0.08);
  --shadow-strong: 0 8px 40px rgba(13, 27, 42, 0.15);
  --radius:        10px;
  --radius-sm:     6px;
  --transition:    0.22s ease;

  /* ── TEXT (never change) ── */
  --cream:         #faf7f0;
  --cream-dark:    #f0ead8;
  --text-dark:     #1a1a2e;
  --text-body:     #2d3748;
  --text-muted:    #718096;

  /* ── SEMANTIC (never change) ── */
  --green:         #276749;
  --green-light:   #e6f4ed;
  --amber:         #b7791f;
  --amber-light:   #fefce8;
  --red:           #9b2335;
  --red-light:     #fff1f2;
  --blue-accent:   #2b6cb0;
  --blue-light:    #ebf4ff;

  /* ── ACCENT (replace per chapter) ── */
  --accent:        #c9a84c;          /* base accent — unique per chapter */
  --accent-light:  #e8c97a;          /* 40% lighter */
  --accent-pale:   #f5e9c8;          /* very light bg, 90% lighter */
  --accent-border: rgba(201,168,76,0.25); /* 20-25% opacity */
}

/* Dark mode overrides */
[data-theme="dark"] {
  --cream:         #0f1923;
  --cream-dark:    #1a2535;
  --text-dark:     #e8e4d9;
  --text-body:     #c8c3b8;
  --text-muted:    #8899aa;
}
```

### Chapter Theming via `data-chapter`

In a unified multi-chapter hub, the accent changes automatically when the chapter panel is active:

```css
html[data-chapter="1"] { --accent: #c9a84c; --accent-light: #e8c97a; --accent-pale: #f5e9c8; }
html[data-chapter="2"] { --accent: #0e7490; --accent-light: #22d3ee; --accent-pale: #ecfeff; }
html[data-chapter="3"] { --accent: #065f46; --accent-light: #34d399; --accent-pale: #ecfdf5; }
html[data-chapter="4"] { --accent: #8b4513; --accent-light: #c0623a; --accent-pale: #f5e9e0; }
/* Add more as needed — chapters 5, 6, 7 ... */
```

---

## 7. Component Library

### A · Page Hero

Every chapter opens with a full-width hero section with dark gradient background, chapter badge, title, and subtitle.

```html
<div class="hero">
  <div class="hero-content">
    <div class="chapter-badge">Chapter 01</div>
    <h1>Chapter Title Here</h1>
    <p class="subtitle">Course Name · Topic tagline in one sentence</p>
    <div class="hero-meta">
      <span>🎓 Key Concept 1</span>
      <span>📊 Key Concept 2</span>
      <span>⚙️ Key Concept 3</span>
    </div>
  </div>
</div>
```

```css
.hero {
  background: linear-gradient(135deg, #0d1b2a 0%, {accent-dark} 55%, {accent-darker} 100%);
  padding: 80px 60px 60px;
  color: white;
}
.chapter-badge {
  font-family: 'JetBrains Mono';
  font-size: 0.7rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--accent-light);
  margin-bottom: 16px;
}
.hero h1 {
  font-size: 2.6rem;
  font-weight: 700;
  margin-bottom: 12px;
}
.hero .subtitle {
  font-size: 1.1rem;
  opacity: 0.8;
  margin-bottom: 32px;
}
.hero-meta {
  display: flex;
  gap: 24px;
  flex-wrap: wrap;
}
.hero-meta span {
  font-family: 'JetBrains Mono';
  font-size: 0.72rem;
  letter-spacing: 0.05em;
  opacity: 0.85;
}
```

---

### B · Section Header

Each of the six sections (A–F) starts with a labeled section header:

```html
<div class="section-header" id="section-a">
  <div class="section-badge">Section A</div>
  <h2>Chapter Summary</h2>
  <p class="section-desc">Core concepts distilled from lecture slides — read first.</p>
</div>
```

```css
.section-header {
  margin: 48px 0 32px;
  padding-bottom: 16px;
  border-bottom: 2px solid var(--accent-border);
}
.section-badge {
  font-family: 'JetBrains Mono';
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent);
  margin-bottom: 8px;
}
.section-header h2 { margin: 0 0 8px; }
.section-desc {
  color: var(--text-muted);
  font-size: 0.9rem;
  margin: 0;
}
```

---

### C · Prose & Text Utilities

```html
<!-- Standard topic block -->
<div class="topic-block">
  <h3>Topic Name</h3>
  <p>Body text. <strong>Key term</strong> introduced in bold on first use.</p>
</div>

<!-- Inline highlight for definitions -->
<span class="highlight">definition text</span>

<!-- Muted secondary note -->
<p class="note-text">📝 Note: enrichment content added beyond the slides.</p>
```

```css
.topic-block { margin: 0 0 36px; }
.topic-block h3 { color: var(--text-dark); margin-bottom: 10px; }

.highlight {
  background: var(--accent-pale);
  border-left: 3px solid var(--accent);
  padding: 2px 8px;
  border-radius: 3px;
}

.note-text {
  font-size: 0.85rem;
  color: var(--text-muted);
  font-style: italic;
}
```

---

### D · Callout Boxes

Four semantic variants: `info`, `warning`, `success`, `danger`. Plus a fifth `accent` variant that uses the chapter's accent color.

```html
<div class="callout callout-info">
  <div class="callout-icon">ℹ️</div>
  <div class="callout-body">
    <strong>Title (optional)</strong>
    <p>Body text explaining the callout.</p>
  </div>
</div>

<div class="callout callout-accent">
  <div class="callout-icon">⭐</div>
  <div class="callout-body">
    <strong>Key Insight</strong>
    <p>Chapter-specific insight using the accent color.</p>
  </div>
</div>
```

```css
.callout {
  display: flex;
  gap: 14px;
  padding: 16px 20px;
  border-radius: var(--radius-sm);
  border-left: 4px solid;
  margin: 24px 0;
}
.callout-info    { background: var(--blue-light);  border-color: var(--blue-accent); }
.callout-warning { background: var(--amber-light); border-color: var(--amber); }
.callout-success { background: var(--green-light); border-color: var(--green); }
.callout-danger  { background: var(--red-light);   border-color: var(--red); }
.callout-accent  { background: var(--accent-pale); border-color: var(--accent); }
.callout-icon    { font-size: 1.1rem; flex-shrink: 0; margin-top: 2px; }
.callout-body p  { margin: 4px 0 0; font-size: 0.9rem; }
```

---

### E · Concept Cards & Grids

Responsive card grid used for overviews, definition sets, or feature lists.

```html
<div class="card-grid">
  <div class="concept-card">
    <div class="card-icon">📐</div>
    <h4>Concept Name</h4>
    <p>One-to-two sentence description of this concept.</p>
  </div>
  <!-- repeat -->
</div>
```

```css
.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 20px;
  margin: 28px 0;
}
.concept-card {
  background: var(--cream-dark);
  border: 1px solid var(--accent-border);
  border-radius: var(--radius);
  padding: 24px 20px;
  transition: transform var(--transition), box-shadow var(--transition);
}
.concept-card:hover {
  transform: translateY(-3px);
  box-shadow: var(--shadow);
}
.card-icon { font-size: 1.6rem; margin-bottom: 10px; }
.concept-card h4 { color: var(--accent); margin: 0 0 8px; }
.concept-card p  { font-size: 0.88rem; color: var(--text-body); margin: 0; }
```

---

### F · Flow Diagrams

CSS-only horizontal flow diagrams for processes, pipelines, and causal chains.

```html
<div class="flow-diagram">
  <div class="flow-step">
    <div class="step-num">1</div>
    <div class="step-content">
      <strong>Step Title</strong>
      <p>Brief description.</p>
    </div>
  </div>
  <div class="flow-arrow">→</div>
  <div class="flow-step">
    <div class="step-num">2</div>
    <div class="step-content">
      <strong>Next Step</strong>
      <p>Brief description.</p>
    </div>
  </div>
</div>
```

```css
.flow-diagram {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin: 28px 0;
}
.flow-step {
  display: flex;
  align-items: flex-start;
  gap: 12px;
  background: var(--cream-dark);
  border: 1px solid var(--accent-border);
  border-radius: var(--radius);
  padding: 16px;
  flex: 1;
  min-width: 160px;
}
.step-num {
  background: var(--accent);
  color: white;
  width: 28px; height: 28px;
  border-radius: 50%;
  display: flex; align-items: center; justify-content: center;
  font-family: 'JetBrains Mono';
  font-size: 0.75rem;
  flex-shrink: 0;
}
.flow-arrow {
  font-size: 1.4rem;
  color: var(--accent);
  flex-shrink: 0;
}
```

---

### G · Formula Boxes

Used in any mathematically dense course (Statistics, Machine Learning, Calculus, Financial Models). Two variants: `formula-block` (display, centered, large) and `formula-inline` (small, within prose).

```html
<!-- Display formula -->
<div class="formula-box">
  <div class="formula-label">Normal Distribution PDF</div>
  <div class="formula-display">
    f(x) = (1 / σ√(2π)) · e<sup>−(x−μ)² / 2σ²</sup>
  </div>
  <div class="formula-vars">
    <span><em>μ</em> = mean</span>
    <span><em>σ</em> = standard deviation</span>
    <span><em>x</em> = value</span>
  </div>
</div>
```

```css
.formula-box {
  background: var(--navy);
  color: #e8e4d9;
  border-radius: var(--radius);
  padding: 24px 28px;
  margin: 28px 0;
  border-left: 4px solid var(--accent);
}
.formula-label {
  font-family: 'JetBrains Mono';
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--accent-light);
  margin-bottom: 12px;
}
.formula-display {
  font-family: 'JetBrains Mono';
  font-size: 1.15rem;
  line-height: 2;
  text-align: center;
  margin: 12px 0;
}
.formula-vars {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
  margin-top: 12px;
  font-size: 0.82rem;
  opacity: 0.75;
}
.formula-vars em { color: var(--accent-light); font-style: normal; }
```

---

### H · Comparison Tables

Styled HTML tables for side-by-side comparisons, parameter summaries, or method trade-offs.

```html
<div class="table-wrap">
  <table class="data-table">
    <thead>
      <tr>
        <th>Property</th>
        <th>Method A</th>
        <th>Method B</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>Complexity</td>
        <td class="cell-positive">O(n)</td>
        <td class="cell-negative">O(n²)</td>
      </tr>
    </tbody>
  </table>
</div>
```

```css
.table-wrap { overflow-x: auto; margin: 28px 0; }
.data-table { width: 100%; border-collapse: collapse; font-size: 0.9rem; }
.data-table th {
  background: var(--navy);
  color: var(--accent-light);
  font-family: 'JetBrains Mono';
  font-size: 0.7rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  padding: 12px 16px;
  text-align: left;
}
.data-table td {
  padding: 11px 16px;
  border-bottom: 1px solid var(--accent-border);
  color: var(--text-body);
}
.data-table tbody tr:hover { background: var(--accent-pale); }
.cell-positive { color: var(--green); font-weight: 600; }
.cell-negative { color: var(--red);   font-weight: 600; }
.cell-neutral  { color: var(--text-muted); }
```

---

### I · Flashcard Carousel

Section B — interactive flashcard deck with JS navigation. One card visible at a time; click to flip between question and answer.

```html
<div class="flashcard-section" id="ch{N}-flashcards">
  <div class="card-counter">Card <span id="ch{N}-current">1</span> of <span id="ch{N}-total">10</span></div>
  <div class="flashcard-container">
    <div class="flashcard" id="ch{N}-flashcard" onclick="flipCard{N}()">
      <div class="flashcard-front">
        <div class="card-label">Question</div>
        <p id="ch{N}-fc-question">First question text</p>
      </div>
      <div class="flashcard-back">
        <div class="card-label">Answer</div>
        <p id="ch{N}-fc-answer">First answer text</p>
      </div>
    </div>
  </div>
  <div class="card-controls">
    <button onclick="prevCard{N}()">← Previous</button>
    <button onclick="nextCard{N}()">Next →</button>
  </div>
</div>
```

**JavaScript template** (replace `{N}` with chapter number, `ch{N}_cards` with actual data):

```javascript
const ch{N}_cards = [
  { q: "Question 1", a: "Answer 1" },
  { q: "Question 2", a: "Answer 2" }
];
let ch{N}_idx = 0, ch{N}_flipped = false;

function flipCard{N}() {
  ch{N}_flipped = !ch{N}_flipped;
  document.getElementById('ch{N}-flashcard').classList.toggle('flipped', ch{N}_flipped);
}
function nextCard{N}() {
  ch{N}_idx = (ch{N}_idx + 1) % ch{N}_cards.length;
  ch{N}_flipped = false;
  updateCard{N}();
}
function prevCard{N}() {
  ch{N}_idx = (ch{N}_idx - 1 + ch{N}_cards.length) % ch{N}_cards.length;
  ch{N}_flipped = false;
  updateCard{N}();
}
function updateCard{N}() {
  const c = ch{N}_cards[ch{N}_idx];
  document.getElementById('ch{N}-fc-question').textContent = c.q;
  document.getElementById('ch{N}-fc-answer').textContent = c.a;
  document.getElementById('ch{N}-flashcard').classList.remove('flipped');
  document.getElementById('ch{N}-current').textContent = ch{N}_idx + 1;
}
```

**Aim for 15–25 flashcards per chapter.** For STEM courses, questions should alternate between conceptual ("What does a p-value represent?") and computational ("Given μ=10, σ=2, what is P(X > 14)?").

---

### J · Feynman Explanation Cards

Section C — expandable "explain like I'm new" cards. Each covers one core concept in plain language.

```html
<div class="feynman-card" id="feynman{N}-1">
  <div class="feynman-header" onclick="toggleFeynman('feynman{N}-1')">
    <div class="feynman-icon">🧠</div>
    <div class="feynman-title">
      <h3>Concept Name</h3>
      <p>Why it matters in one line.</p>
    </div>
    <span class="feynman-toggle">▼</span>
  </div>
  <div class="feynman-body" style="display:none">
    <p><strong>The core idea:</strong> Plain language explanation in 2–3 sentences.
       Avoid all jargon. Use analogies freely.</p>
    <p><strong>In practice:</strong> One concrete example or application.</p>
    <p><strong>The one thing to remember:</strong> A single crisp sentence the student can recall under pressure.</p>
  </div>
</div>
```

```javascript
function toggleFeynman(id) {
  const card = document.getElementById(id);
  const body = card.querySelector('.feynman-body');
  const toggle = card.querySelector('.feynman-toggle');
  const open = body.style.display === 'block';
  body.style.display = open ? 'none' : 'block';
  toggle.textContent = open ? '▼' : '▲';
  card.classList.toggle('open', !open);
}
```

**Aim for 4–6 Feynman cards per chapter**, covering the concepts most likely to be misunderstood or over-abstracted in the lecture slides.

---

### K · Knowledge Graph (SVG)

Section D — inline SVG visualization of concept relationships. JS-rendered from a node/edge data array.

```html
<div class="graph-container">
  <svg id="ch{N}-kg-svg" viewBox="0 0 800 480" preserveAspectRatio="xMidYMid meet"></svg>
</div>
```

```javascript
function initCh{N}Graph() {
  const nodes = [
    { id: 'n1', x: 400, y: 240, label: 'Central Concept', type: 'core' },
    { id: 'n2', x: 220, y: 140, label: 'Sub Concept A',   type: 'primary' },
    { id: 'n3', x: 580, y: 140, label: 'Sub Concept B',   type: 'primary' },
    { id: 'n4', x: 160, y: 340, label: 'Detail 1',        type: 'secondary' },
  ];
  const edges = [
    { from: 'n1', to: 'n2', label: 'relates to' },
    { from: 'n1', to: 'n3', label: 'depends on' },
    { from: 'n2', to: 'n4', label: 'includes'   },
  ];
  renderGraph('ch{N}-kg-svg', nodes, edges);
}
```

**Node types** (CSS classes on SVG `<circle>` or `<rect>`):

| Type | Meaning | Visual |
|------|---------|--------|
| `core` | Central topic of the chapter | Large circle, accent fill |
| `primary` | Major sub-topics | Medium circle, accent-light fill |
| `secondary` | Supporting concepts | Small circle, cream-dark fill |
| `formula` | Equations / models | Rounded rect, navy fill |

**Aim for 10–16 nodes per chapter**, with at most 2 levels of depth from the core node. Avoid spider webs with 30+ edges.

---

### L · Exercise Tiers

Section E — three progressive difficulty tiers. Answers toggle on click.

```html
<div class="exercise-section">
  <div class="tier-header tier-1">Tier 1 — Recall</div>

  <div class="exercise-card" id="ex-ch{N}-1">
    <div class="exercise-q">
      <span class="ex-num">1</span>
      <p>Question text here.</p>
      <button class="show-answer" onclick="ch{N}ToggleAnswer(this)">Show Answer</button>
    </div>
    <div class="exercise-answer" style="display:none">
      <p>Answer text here.</p>
    </div>
  </div>

  <div class="tier-header tier-2">Tier 2 — Application</div>
  <!-- ... -->

  <div class="tier-header tier-3">Tier 3 — Analysis</div>
  <!-- ... -->
</div>
```

**Tier guidelines:**

| Tier | Cognitive Level | Question Style |
|------|----------------|----------------|
| Tier 1 · Recall | Remember / Understand | Define X. What does Y mean? List the steps of Z. |
| Tier 2 · Application | Apply / Analyze | Calculate X given Y. Explain why Z happens when... |
| Tier 3 · Analysis | Evaluate / Synthesize | Compare X and Y. If Z changed, what would happen? Why? |

**STEM-specific Tier 2–3 questions** should include numerical problems with specific parameter values so students can verify their arithmetic.

```javascript
function ch{N}ToggleAnswer(btn) {
  const answer = btn.closest('.exercise-card').querySelector('.exercise-answer');
  const open = answer.style.display === 'block';
  answer.style.display = open ? 'none' : 'block';
  btn.textContent = open ? 'Show Answer' : 'Hide Answer';
}
```

**Aim for 5 exercises per tier (15 total) per chapter.** For quantitative chapters, increase Tier 2 to 7–8 problems.

---

### M · Cheat Sheet Cards

Section F — compact reference cards for rapid review before an exam.

```html
<div class="cheatsheet-grid">
  <div class="cheat-card">
    <div class="cheat-header">Key Formulas</div>
    <ul class="cheat-list">
      <li><code>formula = expression</code> — one-line description</li>
    </ul>
  </div>

  <div class="cheat-card">
    <div class="cheat-header">Key Terms</div>
    <dl class="cheat-definitions">
      <dt>Term</dt>
      <dd>Concise definition in 1 sentence.</dd>
    </dl>
  </div>

  <div class="cheat-card">
    <div class="cheat-header">Common Mistakes</div>
    <ul class="cheat-list cheat-warnings">
      <li>⚠️ Mistake description and why it's wrong.</li>
    </ul>
  </div>
</div>
```

```css
.cheatsheet-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 20px;
  margin: 28px 0;
}
.cheat-card {
  background: var(--cream-dark);
  border: 1px solid var(--accent-border);
  border-radius: var(--radius);
  overflow: hidden;
}
.cheat-header {
  background: var(--navy);
  color: var(--accent-light);
  font-family: 'JetBrains Mono';
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  padding: 10px 16px;
}
.cheat-list  { padding: 16px 20px; margin: 0; font-size: 0.88rem; }
.cheat-list li { margin-bottom: 8px; }
```

---

### N · Code Block (STEM Courses)

Required for Machine Learning, Statistics (R/Python), and any course with computational content.

```html
<!-- Labeled code block with copy button -->
<div class="code-block">
  <div class="code-header">
    <span class="code-lang">Python</span>
    <button class="copy-btn" onclick="copyCode(this)">Copy</button>
  </div>
  <pre><code class="lang-python">import numpy as np

# Linear regression with numpy
X = np.array([1, 2, 3, 4, 5])
y = np.array([2.1, 3.9, 6.1, 7.8, 10.0])
coeffs = np.polyfit(X, y, 1)
print(f"slope={coeffs[0]:.2f}, intercept={coeffs[1]:.2f}")
</code></pre>
</div>
```

```css
.code-block {
  background: #0d1117;
  border-radius: var(--radius);
  overflow: hidden;
  margin: 24px 0;
  border: 1px solid rgba(255,255,255,0.08);
}
.code-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 8px 16px;
  background: #161b22;
  border-bottom: 1px solid rgba(255,255,255,0.08);
}
.code-lang {
  font-family: 'JetBrains Mono';
  font-size: 0.65rem;
  color: var(--accent-light);
  letter-spacing: 0.1em;
  text-transform: uppercase;
}
.copy-btn {
  font-size: 0.75rem;
  background: rgba(255,255,255,0.08);
  border: none;
  color: #8b949e;
  cursor: pointer;
  padding: 4px 10px;
  border-radius: 4px;
}
.copy-btn:hover { background: rgba(255,255,255,0.15); color: white; }
pre {
  margin: 0;
  padding: 20px;
  overflow-x: auto;
  font-family: 'JetBrains Mono';
  font-size: 0.85rem;
  line-height: 1.7;
  color: #e6edf3;
}
```

```javascript
function copyCode(btn) {
  const code = btn.closest('.code-block').querySelector('code').textContent;
  navigator.clipboard.writeText(code).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = 'Copy', 1800);
  });
}
```

---

### O · Proof / Derivation Panel

For courses where showing mathematical derivations is pedagogically important (Statistics, Calculus, ML theory). Collapsible to avoid visual clutter.

```html
<div class="proof-panel">
  <div class="proof-header" onclick="toggleProof(this)">
    <span class="proof-badge">Derivation</span>
    <span class="proof-title">Proof of the Central Limit Theorem</span>
    <span class="proof-toggle">Show ▼</span>
  </div>
  <div class="proof-body" style="display:none">
    <p>Step 1: ...</p>
    <div class="formula-box">...</div>
    <p>Step 2: ...</p>
  </div>
</div>
```

```css
.proof-panel {
  border: 1px solid var(--accent-border);
  border-radius: var(--radius);
  margin: 24px 0;
  overflow: hidden;
}
.proof-header {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 14px 20px;
  background: var(--accent-pale);
  cursor: pointer;
  user-select: none;
}
.proof-badge {
  font-family: 'JetBrains Mono';
  font-size: 0.6rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  background: var(--accent);
  color: white;
  padding: 2px 8px;
  border-radius: 3px;
}
.proof-title { flex: 1; font-weight: 600; font-size: 0.9rem; }
.proof-toggle { font-family: 'JetBrains Mono'; font-size: 0.7rem; color: var(--text-muted); }
.proof-body { padding: 20px 24px; }
```

```javascript
function toggleProof(header) {
  const body = header.nextElementSibling;
  const toggle = header.querySelector('.proof-toggle');
  const open = body.style.display === 'block';
  body.style.display = open ? 'none' : 'block';
  toggle.textContent = open ? 'Show ▼' : 'Hide ▲';
}
```

---

## 8. Course-Type Adaptations

The six-section skeleton (A through F) is constant across all courses. What changes is the **component selection**, **exercise format**, and **knowledge graph structure** within those sections.

### Quantitative / STEM Courses
*(Statistics, Machine Learning, Calculus)*

**Characteristics:** Dense formulas, algorithmic thinking, computation over interpretation.

**Section A adaptations:**
- Use `formula-box` components (§G) liberally — at least one per major concept.
- Include a parameter table (`data-table`) after every formula listing what each variable means.
- Use `code-block` (§N) for any concept that has a direct Python/R implementation.
- Use `proof-panel` (§O) for derivations that are examinable but shouldn't dominate reading flow.
- Flow diagrams (§F) for algorithms: training loops, statistical test decision trees, etc.

**Section B (Flashcards):**
- Mix 50/50 conceptual ("What is the bias-variance tradeoff?") and computational ("σ² of a Bernoulli(p) distribution = ?").
- Include formula-recall cards: show name, ask student to write the formula.

**Section E (Exercises):**
- Tier 2 and Tier 3 should always include numerical problems with concrete values.
- Provide intermediate calculation steps in the answer, not just the final number.
- Include "sketch a graph" prompts — described verbally since the guide is HTML, not interactive.

**Knowledge graph:** Connect formulas as nodes (use `formula` node type), not just concepts.

---

### Finance / Economics Courses
*(Financial Markets, Macroeconomics, Corporate Finance)*

**Characteristics:** Institutional knowledge, market mechanisms, ratio analysis, scenario reasoning.

**Section A adaptations:**
- Use `concept-card` grids (§E) for market participants, instruments, or institutional actors.
- Flow diagrams (§F) for transmission mechanisms (e.g., Fed policy → interest rates → investment).
- Callout-accent boxes for key policy implications or market signals.
- Comparison tables (§H) for instrument comparisons (bonds vs. stocks, etc.).

**Section E (Exercises):**
- Tier 2: numerical problems (yield calculations, present value, rate of return).
- Tier 3: scenario analysis ("If inflation rises unexpectedly, trace the effect through...").

**Knowledge graph:** Mix institutional actors (Fed, banks, investors) with mechanisms (monetary policy, yield curve).

---

### Computer Science / Programming Courses
*(Algorithms, Databases, Systems)*

**Characteristics:** Pseudocode-first, Big-O, data structure diagrams.

**Section A adaptations:**
- Heavy use of `code-block` (§N) — preferably with working, copy-pasteable code.
- Flow diagrams for algorithm steps.
- Use `formula-box` for complexity expressions (`O(n log n)`).
- `proof-panel` for correctness proofs.

**Section B (Flashcards):**
- Include "what is the time complexity of X?" cards.
- Include "trace through this algorithm with input X" style questions.

**Knowledge graph:** Node types should reflect code entities (class, method, data structure) in addition to abstract concepts.

---

### Humanities / Social Sciences
*(History, Psychology, Sociology, Literature)*

**Characteristics:** Argument-driven, primary source citations, qualitative analysis.

**Section A adaptations:**
- Less formula use; more callout boxes for key claims, quotes, debates.
- Use `topic-block` prose sections with `highlight` spans for key terms.
- Timeline flows (§F) for historical sequences.
- No code blocks.

**Section E (Exercises):**
- Tier 2: compare and contrast two positions.
- Tier 3: write a thesis-level argument using evidence from the lecture.

**Knowledge graph:** Node types should reflect actors, events, and ideas; edges should be labeled with causal or thematic relationships.

---

## 9. JavaScript Architecture

### Core Principles

1. **All JS is inline** in the `<script>` tag at the end of `<body>`. No external `.js` files.
2. **All function names are namespaced** by chapter number to prevent collisions in the unified hub.
3. **Lazy initialization** — chapter-specific JS (graph rendering, card setup) only fires when that chapter becomes visible.
4. **No global state** — each chapter's state lives in chapter-prefixed variables.

### Mandatory Function Inventory

Every chapter HTML must define these functions (replace `{N}` with chapter number):

| Function | Purpose |
|----------|---------|
| `flipCard{N}()` | Toggle flashcard front/back |
| `nextCard{N}()` | Advance to next flashcard |
| `prevCard{N}()` | Go to previous flashcard |
| `updateCard{N}()` | Sync DOM to current card index |
| `toggleFeynman(id)` | Expand/collapse a Feynman card |
| `ch{N}ToggleAnswer(btn)` | Toggle exercise answer visibility |
| `initCh{N}Graph()` | Initialize the SVG knowledge graph |
| `chScrollTo(sectionId)` | Smooth-scroll to a section anchor |

### Chapter-Scoped State Variables

```javascript
// Pattern — always prefix with ch{N}_
const ch{N}_cards = [ /* flashcard data */ ];
let   ch{N}_idx = 0;
let   ch{N}_flipped = false;
```

### Unified Hub: `switchChapter(n)` Integration

When chapters are assembled into a unified hub (`{course}-complete-study-guide.html`), the assembly script wraps each chapter's panel in `<div id="ch{N}-panel">` and generates a `switchChapter(n)` function:

```javascript
function switchChapter(n) {
  // Hide all panels
  document.querySelectorAll('.chapter-panel').forEach(p => p.style.display = 'none');
  // Show target panel
  document.getElementById(`ch${n}-panel`).style.display = 'block';
  // Update data-chapter for CSS accent theming
  document.documentElement.setAttribute('data-chapter', n);
  // Update chapter tab bar active state
  document.querySelectorAll('.ch-tab').forEach((t, i) => t.classList.toggle('active', i + 1 === n));
  // Lazy-init this chapter's graph if not already rendered
  const graphSvg = document.getElementById(`ch${n}-kg-svg`);
  if (graphSvg && !graphSvg.dataset.initialized) {
    window[`initCh${n}Graph`]?.();
    graphSvg.dataset.initialized = 'true';
  }
}
```

---

## 10. Dark Mode System

### Implementation

Dark mode is toggled by setting `data-theme="dark"` on the `<html>` element:

```javascript
function toggleDark() {
  const html = document.documentElement;
  const isDark = html.getAttribute('data-theme') === 'dark';
  html.setAttribute('data-theme', isDark ? 'light' : 'dark');
  document.getElementById('dark-toggle').textContent = isDark ? '🌙 Dark Mode' : '☀️ Light Mode';
  localStorage.setItem('theme', isDark ? 'light' : 'dark');
}

// On load — restore saved preference
(function() {
  const saved = localStorage.getItem('theme') || 'light';
  document.documentElement.setAttribute('data-theme', saved);
})();
```

### CSS Dark Mode Variables

```css
[data-theme="dark"] {
  --cream:      #0f1923;
  --cream-dark: #1a2535;
  --text-dark:  #e8e4d9;
  --text-body:  #c8c3b8;
  --text-muted: #8899aa;
}
```

Only variable values are overridden. No structural CSS is duplicated in the dark block.

### Sidebar in Dark Mode

The sidebar is always dark (navy `#0d1b2a`) regardless of light/dark mode — it never changes background. Only the main content area switches.

---

## 11. Six-Section Structure

This structure is **universal across all courses and all chapter types**. The section letters (A–F) are fixed; only the content within each section adapts to the course type (see §8).

| Section | Name | Cognitive Mode | Effort Allocation |
|---------|------|----------------|-------------------|
| A | Chapter Summary | Comprehension | 40–50% of build time |
| B | Flashcards | Active Recall | 20% |
| C | Feynman Explanations | Deep Understanding | 15% |
| D | Knowledge Graph | Relational Mapping | 10% |
| E | Exercises | Application & Analysis | 10% |
| F | Cheat Sheet | Quick Reference | 5% |

### Section A — Chapter Summary

The largest section. Converts raw lecture slides into readable prose organized around topics, not slide numbers.

- Structure: `section-header` → 2 to 5 `topic-block`s → relevant components (callouts, formulas, tables, flows, code blocks) between blocks.
- Every major concept from the source material must appear here.
- Use `📝` to flag any enrichment content not in the original slides.
- Do **not** list slide numbers. Write as if the slides never existed.

### Section B — Flashcards

- 15–25 cards per chapter.
- Card format: question on front, concise answer on back.
- Quantitative courses: half cards should test formula recall or numerical setup.
- Use the JS carousel template (§I).

### Section C — Feynman Explanations

- 4–6 expandable cards.
- Target the concepts students most commonly mis-explain on exams.
- Each card: core idea (plain language) → concrete example → one-sentence takeaway.
- No jargon in the explanation body. Use the technical term in the card header only.

### Section D — Knowledge Graph

- 10–16 nodes, organized around a central concept.
- Use the SVG graph system (§K).
- For STEM: connect formulas to the concepts they describe.
- For Finance: connect institutional actors to mechanisms.

### Section E — Exercises

- 15 exercises across 3 tiers (5 each), or more for quantitative chapters (5/7/7).
- All answers are hidden until clicked.
- Tier 3 exercises should require integration across multiple concepts from the chapter.

### Section F — Cheat Sheet

- 3–5 cheat cards covering: key formulas, key terms, common mistakes/pitfalls.
- Should be printable at a glance — no more than 8–10 items per card.
- For STEM: include a "when to use X vs Y" comparison card.

---

## 12. Multi-Chapter Assembly (Unified Hub)

Each course has one `{course}-complete-study-guide.html` file that embeds all chapters in a single page with a tab-based chapter switcher.

### Assembly Structure

```
<html data-chapter="1" data-theme="light">
<head>
  <!-- Shared CSS: structural, typography, theming -->
  <!-- Per-chapter CSS: scoped to #ch{N}-panel -->
</head>
<body>
  <!-- Top tab bar: Chapter 1 | Chapter 2 | ... -->
  <div id="chapter-tabs">
    <button class="ch-tab active" onclick="switchChapter(1)">Ch.1 · Topic</button>
    <button class="ch-tab" onclick="switchChapter(2)">Ch.2 · Topic</button>
  </div>

  <!-- Shared sidebar (swaps nav per chapter) -->
  <div class="sidebar">...</div>

  <!-- Chapter panels (only one visible at a time) -->
  <div id="ch1-panel" class="chapter-panel"><!-- ch1 content --></div>
  <div id="ch2-panel" class="chapter-panel" style="display:none"><!-- ch2 content --></div>

  <!-- All chapter JS -->
  <script><!-- ch1 JS --></script>
  <script><!-- ch2 JS --></script>
  <script><!-- switchChapter() + init --></script>
</body>
```

### CSS Scoping for Assembly

When assembling, all CSS from each chapter's `<style>` block must be scoped to its panel ID to prevent class-name conflicts between chapters:

```python
def scope_css(css, scope):
    """Prefix all CSS rules with the chapter panel scope."""
    # ':root' and 'html' → keep as :root (shared vars)
    # 'body' → scope
    # '.dark' or '[data-theme="dark"]' → [data-theme="dark"] scope
    # '@media' → recurse into inner rules
    # all other selectors → f"{scope} {selector}"
```

### ID Namespacing for Assembly

All `id="X"` attributes and `href="#X"` anchors must be prefixed with `ch{N}-` when assembling:

- `id="flashcard"` → `id="ch2-flashcard"`
- `href="#section-b"` → `href="#ch2-section-b"`
- `getElementById('flashcard')` → `getElementById('ch2-flashcard')`

### Per-Course Assembly Script

Each course should have a Python assembly script at:
```
{course-folder}/build_unified.py
```

The script reads each individual chapter HTML, extracts and scopes CSS, namespaces IDs, renames JS functions, and writes the unified hub file.

---

## 13. New Course Setup Checklist

Use this checklist every time you add a completely new course to the library.

### Before Building Chapter 1

- [ ] **Choose a course slug** — lowercase, hyphenated (e.g., `machine-learning`, `statistics-101`)
- [ ] **Create the course folder** under `Course-Notes-Library/{course-slug}/`
- [ ] **Create a `source/` subfolder** and place all lecture PDFs there
- [ ] **Choose a color family** for the course (see §4) — must not clash with existing courses
- [ ] **Assign accent colors** for all known chapters (can add more later)
- [ ] **Note the course type** (quantitative, finance, CS, humanities) to select the right adaptations from §8
- [ ] **Confirm font stack** — same as all other courses (Playfair + Source Sans 3 + JetBrains Mono)

### Sidebar Header Fields (required for every chapter in the course)

```html
<div class="sidebar-header">
  <div class="course-label">Course Name</div>          <!-- e.g., "Statistics 101" -->
  <div class="course-code">STAT-101</div>              <!-- optional course code -->
  <div class="chapter-title">Ch.01 · Topic Name</div>
</div>
```

### Course-Level Metadata Block (add to Section A hero)

```html
<div class="hero-meta">
  <span>📚 {Course Name}</span>
  <span>📖 Chapter {N} of {Total}</span>
  <span>🎯 {Course Level — Intro / Intermediate / Advanced}</span>
</div>
```

### After Building All Chapters

- [ ] Create `{course-slug}-complete-study-guide.html` using the assembly script
- [ ] Verify `switchChapter()` works for all chapters
- [ ] Verify dark mode works across all chapters in the hub
- [ ] Verify mobile sidebar behavior
- [ ] Run the 25-point validation checklist (§14) on the unified hub

---

## 14. New Chapter Checklist

Use this checklist for every new individual chapter HTML file, for any course.

### Source Preparation

- [ ] Source PDF(s) extracted with `pdfplumber` — text saved to verify coverage
- [ ] All major topics from the source identified and listed
- [ ] Enrichment content planned and flagged with 📝

### Section A — Summary

- [ ] All major lecture topics covered
- [ ] At least one component per major topic (callout, formula, table, flow, code block)
- [ ] `h2 → h3 → h4` hierarchy maintained throughout
- [ ] No heading levels skipped
- [ ] All enrichment content marked 📝
- [ ] STEM courses: all key formulas have their own `formula-box`

### Section B — Flashcards

- [ ] 15–25 cards written
- [ ] Cards data array defined as `ch{N}_cards`
- [ ] All card functions namespaced: `flipCard{N}`, `nextCard{N}`, `prevCard{N}`, `updateCard{N}`
- [ ] Card counter DOM IDs namespaced: `ch{N}-current`, `ch{N}-total`, `ch{N}-fc-question`, `ch{N}-fc-answer`

### Section C — Feynman

- [ ] 4–6 Feynman cards written
- [ ] Each card has: core idea (plain language) → concrete example → one-sentence takeaway
- [ ] IDs formatted as `feynman{N}-{1..6}` (e.g., `feynman3-1`)
- [ ] `toggleFeynman(id)` function present and working

### Section D — Knowledge Graph

- [ ] 10–16 nodes defined
- [ ] Node/edge arrays named `ch{N}_nodes`, `ch{N}_edges`
- [ ] `initCh{N}Graph()` function present
- [ ] SVG container ID: `ch{N}-kg-svg`

### Section E — Exercises

- [ ] 15+ exercises across 3 tiers
- [ ] Exercise IDs: `ex-ch{N}-{1..15}`
- [ ] `ch{N}ToggleAnswer(btn)` function present
- [ ] Tier 3 exercises require multi-concept synthesis

### Section F — Cheat Sheet

- [ ] 3–5 cheat cards present
- [ ] Includes: key formulas (or terms), common mistakes
- [ ] STEM courses: includes "when to use X vs Y" card

### CSS & Theming

- [ ] `:root` uses correct accent variables for this chapter
- [ ] Dark mode block present: `[data-theme="dark"] { ... }`
- [ ] No hardcoded hex colors outside `:root` — all via CSS variables
- [ ] Mobile responsive — tested at 768px viewport

### JavaScript

- [ ] All functions namespaced with chapter number
- [ ] All state variables namespaced: `ch{N}_idx`, `ch{N}_flipped`
- [ ] `chScrollTo(id)` helper present for sidebar nav links
- [ ] Dark mode toggle function present with localStorage persistence

### Accessibility

- [ ] All interactive elements have `tabindex="0"` if not natively focusable
- [ ] Flashcard has `aria-label`
- [ ] Dark mode toggle button has clear label text
- [ ] Color is not the only means of conveying correctness/incorrectness in exercises

---

## 15. Naming Conventions

### File Names

```
{course-slug}-complete-study-guide.html
study-guide-ch{NN}-{topic-slug}.html
```

### CSS ID Names

```
{section-anchor}                    → section-a, section-b, ..., section-f
ch{N}-flashcard                     → ch2-flashcard
ch{N}-fc-question                   → ch3-fc-question
ch{N}-fc-answer                     → ch3-fc-answer
ch{N}-current, ch{N}-total          → ch1-current, ch1-total
feynman{N}-{card-num}               → feynman2-3
ch{N}-kg-svg                        → ch4-kg-svg
ex-ch{N}-{exercise-num}             → ex-ch2-7
ch{N}-panel                         → ch3-panel  (unified hub only)
```

### JavaScript Names

```
ch{N}_cards                         → ch2_cards
ch{N}_idx, ch{N}_flipped            → ch3_idx, ch3_flipped
ch{N}_nodes, ch{N}_edges            → ch1_nodes, ch1_edges
flipCard{N}(), nextCard{N}()        → flipCard2(), nextCard2()
prevCard{N}(), updateCard{N}()      → prevCard3(), updateCard3()
initCh{N}Graph()                    → initCh4Graph()
ch{N}ToggleAnswer(btn)              → ch2ToggleAnswer(btn)
toggleFeynman(id)                   → toggleFeynman('feynman3-2')
chScrollTo(sectionId)               → chScrollTo('ch2-section-b')
```

### CSS Class Names (structural — never chapter-specific)

These class names are shared across all courses and must not be redefined with conflicting styles in individual chapters. All chapter-specific overrides must be scoped to `#ch{N}-panel`:

`.sidebar`, `.main`, `.content`, `.hero`, `.section-header`, `.callout`, `.concept-card`, `.card-grid`, `.flashcard`, `.feynman-card`, `.formula-box`, `.data-table`, `.cheat-card`

---

## 16. Anti-Patterns to Avoid

### CSS Anti-Patterns

- ❌ **Never redefine shared class names** (`.content`, `.sidebar`, `.main`) with conflicting values in a chapter's `<style>` block without scoping them to `#ch{N}-panel`. This is the #1 cause of chapter conflicts in the unified hub.
- ❌ **Never hardcode hex colors** outside the `:root` block. Always use `var(--accent)`, `var(--text-body)`, etc.
- ❌ **Never duplicate the dark mode block** — one `[data-theme="dark"]` block at the bottom of each chapter's CSS is sufficient.
- ❌ **Never use `!important`** except in the dark mode override block, and even there only as a last resort.
- ❌ **Never use Unicode subscript/superscript characters** (`₀₁₂`, `⁰¹²`) in formula text — the fonts do not include these glyphs. Use `<sub>` and `<sup>` HTML tags instead.

### JavaScript Anti-Patterns

- ❌ **Never use global function names** without a chapter number suffix. `flipCard()` will conflict across chapters; `flipCard3()` will not.
- ❌ **Never query DOM without chapter-prefixed IDs** in chapter-specific functions. `document.getElementById('flashcard')` silently returns the wrong chapter's element.
- ❌ **Never call `initGraph()` on page load** — only call when the chapter panel is first made visible (lazy init via `switchChapter()`).
- ❌ **Never store chapter state in the DOM** (e.g., `dataset.idx`). Keep it in JS variables.

### Content Anti-Patterns

- ❌ **Never reproduce slide text verbatim** in Section A. Rewrite it as prose. Students should feel like they're reading a textbook section, not reading slide bullets.
- ❌ **Never leave Section E with only recall-level questions** (Tier 1 only). Every chapter must have Tier 2 and Tier 3 questions.
- ❌ **Never create more than 20 nodes in the knowledge graph.** Dense graphs are unreadable. 10–16 is the sweet spot.
- ❌ **Never add content to the cheat sheet that requires explanation.** If it needs explanation, it belongs in Section A. Section F must be scannable in 30 seconds.
- ❌ **Never skip the 📝 marker** on enrichment content. Students should always know what came from their lecture and what was added.

### Structural Anti-Patterns

- ❌ **Never change the sidebar width** (270px) or the content max-width (960px) per chapter. Layout consistency is part of the design.
- ❌ **Never create a second accent color per chapter.** The single accent system is what keeps the design coherent.
- ❌ **Never reuse accent colors across chapters** within the same course. Even if two chapters feel related, their accents must be visually distinct.
- ❌ **Never mix dark sidebar styles with light sidebar styles** in the same course. The sidebar is always dark navy; this is non-negotiable.

---

*Last updated: 2026-04 · Covers: Financial Markets, Statistics, Machine Learning, Calculus, and all future courses in this library.*
