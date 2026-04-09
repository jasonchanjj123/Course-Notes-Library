# Course Notes Library

A centralized, clear, and rigorous hub for academic materials.

## Features
- **Global Search:** Robust and fast keyword search across all courses and chapters using Fuse.js.
- **Modern UI:** Clean, typography-focused design optimized for readability.
- **Organized Structure:** Categorized by course and chapter.
- **Easy Deployment:** Ready for Vercel "Zero Config" deployment.

## Directory Structure
- `index.html`: The main library hub.
- `notes/`: Directory for course materials.
  - `financial-market/`: Financial Markets & Institutions course notes.
    - `ch01.html`, `ch02.html`, `ch03.html`: Individual chapters.

## How to add more courses
1.  **Create a folder** in `notes/` for the new course (e.g., `notes/113-1-calculus/`).
2.  **Add metadata** by creating a `meta.json` in the new folder with `title`, `badge`, and `description` (optional but recommended).
3.  **Add your HTML notes** to that folder.
4.  **Run the script**: Execute `python index_script.py` in your terminal. This will automatically update `index.html` with the new course card and regenerate the global `search-index.json`.
5.  **Add a "Back to Library" link** in the new HTML notes' sidebar (copy-paste from an existing chapter).

## Local Development
Simply open `index.html` in your browser, or use a live server (e.g., `npx serve .`).

## Deployment
Push this repository to GitHub and connect it to Vercel. Vercel will automatically detect and deploy the static site.
