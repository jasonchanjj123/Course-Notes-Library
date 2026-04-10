# AI Agent Project Guide: Course Notes Library

This document provides a technical blueprint of the **Course Notes Library** for AI agents. It explains the system architecture, core logic, and the relationship between components to ensure safe and effective maintenance or expansion.

---

## 1. Project Purpose
A centralized, high-performance static repository for academic study guides. The system prioritizes **searchability**, **interactivity** (Knowledge Graphs, Flashcards), and **automated management**.

## 2. System Architecture
The project is a **Static Site with an Automated Build Pipeline**. It does not use a database; instead, it relies on a JSON-based search index generated from HTML source files.

### Core Components:
- **Frontend Hub (`index.html`):** The primary entry point. Features a Fuse.js-powered search engine with an advanced settings panel.
- **Source Notes (`notes/{course-id}/*.html`):** Semantic HTML files containing the actual study material.
- **The Brain (`index_script.py`):** A Python automation script that maintains the link between the source files and the Hub.
- **Search System:** Uses `Fuse.js` for fuzzy matching and `highlight.js` for post-navigation keyword highlighting.

---

## 3. Directory Structure
```text
/
├── index.html              # Library Hub UI & Search Logic
├── index_script.py         # Automation: Indexing & Hub Updates
├── search-index.json       # Generated: Global keyword/content map
├── highlight.js            # Global: Keyword navigation & flashing
├── CHANGELOG.md            # Version history
├── notes/
│   ├── {course-folder}/    # Individual course directories
│   │   ├── meta.json       # REQUIRED: Course title, badge, desc
│   │   └── {chXX}.html     # Study guides (Source Files)
└── raw_material/           # Unprocessed assets (PDFs, etc.)
```

---

## 4. The Automation Pipeline (`index_script.py`)
This script is the most critical component for an AI agent to understand. It performs three roles:
1.  **Crawl:** It scans the `notes/` directory for folders.
2.  **Metadata Extraction:** It reads `meta.json` from each folder to determine the UI appearance of the course card.
3.  **Indexing:** It parses every `.html` file, extracting:
    *   `<title>` for the link text.
    *   `<h2>` and `<h3>` tags as section anchors.
    *   Paragraphs and callouts for full-text search.
4.  **Injection:** It ensures `../../highlight.js` is linked in every HTML file.
5.  **Synchronization:** It replaces the `.course-grid` in `index.html` with newly generated cards.

---

## 5. Search & Navigation Logic
### Fuzzy Search
Located in `index.html`, the `Fuse` instance is dynamic. Users can adjust:
- `threshold`: Sensitivity of matching.
- `ignoreLocation`: Finding keywords deep within chapters.
- `weights`: Prioritizing Titles vs. Body Content.

### Keyword Highlighting (`highlight.js`)
When a search result is clicked, the URL is appended with `?h=keyword`.
The `highlight.js` script:
1.  Parses the `h` parameter.
2.  Uses `TreeWalker` to find the text node.
3.  Wraps the match in a `.search-highlight-flash` span.
4.  Scrolls the first match into the center of the viewport.
5.  Triggers a CSS fade-out after 3 seconds.

---

## 6. Design System & UI Standards
**Colors:**
- Navy (`#0d1b2a`), Gold (`#c9a84c`), Green (`#276749`).
**Typography:**
- Serif: `Playfair Display` (Headings).
- Sans: `Source Sans 3` (Body).
- Mono: `JetBrains Mono` (Metadata/Code).

**Interactive Components:**
- **Knowledge Graphs:** SVG-based. Nodes must have unique IDs and a `desc` field in the JS array for the tooltip system.
- **Flashcards:** Flip logic handled via `.flipped` class toggle.
- **Exercises:** Tiered badge system (Recall, Application, Synthesis).

---

## 7. Operational Checklist for AI Agents
When tasked with changes, follow this order:
1.  **Modified a Chapter?** Run `python index_script.py` to update the search index.
2.  **Added a Course?** Ensure a `meta.json` exists in the new folder before running the script.
3.  **Changed CSS?** Check the Dark Mode toggle (`data-theme="dark"`) to ensure contrast is maintained.
4.  **Updated Version?** Document the change in `CHANGELOG.md` under the `[1.x.x]` format.

---
*Created by Gemini CLI - April 2026*
