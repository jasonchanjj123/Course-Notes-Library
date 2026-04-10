---
name: study-guide-builder
description: Builds comprehensive academic study guides from PDFs/Slides following the Universal Study Guide Design System. Integrates pdf, study-tutor, and frontend-design skills to generate interactive, high-performance, and visually polished HTML notes.
---

# Study Guide Builder

This skill transforms raw academic materials into high-performance, interactive study guides. It enforces the **Editorial Academic** aesthetic and the **Active Recall** philosophy.

## Specialized Workflow

### 1. Ingestion (PDF/Slides)
- **Tool:** Use the `pdf` skill to extract all text, identifying headers, lists, and emphasis.
- **Goal:** Map the raw material into a logical hierarchy of topics.

### 2. Cognitive Processing
- **Tool:** Use `study-tutor` logic to:
  - Distill complex paragraphs into a **Section A Summary**.
  - Generate 15–25 **Section B Flashcards** (mix of conceptual and computational).
  - Select 4–6 complex concepts for **Section C Feynman Explanations**.
  - Map relationships for the **Section D Knowledge Graph**.
  - Design 15 **Section E Exercises** across 3 difficulty tiers.
  - Summarize 3–5 **Section F Cheat Sheet** cards.

### 3. Visual Refinement & Generation (HTML/CSS/JS)
- **Tool:** Use the `frontend-design` skill to refine the template and ensure a distinctive, production-grade interface.
- **Template:** Use `assets/template.html` as the boilerplate.
- **Design System:** Strictly follow [design-system.md](references/design-system.md).
  - **Aesthetics:** Avoid generic AI looks; ensure clean spacing, sophisticated interactive feedback, and platform-appropriate design.
  - **Colors:** Select an accent color from the appropriate family (§4).
  - **Typography:** Map `Playfair Display`, `Source Sans 3`, and `JetBrains Mono` to their respective roles (§3).
  - **Interactivity:** Ensure Knowledge Graphs are SVG-based and interactive (§K).

### 4. Technical Rigor
- **Namespacing:** All JS functions and HTML IDs must be prefixed with the chapter number (e.g., `initCh4Graph()`, `ch4-flashcard`) to avoid conflicts in the unified hub (§9, §15).
- **Injection:** Always include the link to `../../highlight.js` at the end of the body.
- **Sync:** After creating the `.html` file in the correct `notes/{course}/` folder, you MUST run `python index_script.py` to regenerate the search index and hub cards.

## Component Library Reference
See [design-system.md](references/design-system.md) for code snippets for:
- Callout Boxes (Info, Warning, success, etc.)
- Formula Boxes (STEM courses)
- Comparison Tables
- Feynman Cards
- Exercise Tier Headers
