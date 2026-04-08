# Change Log

All notable changes to the **Course Notes Library** will be documented in this file.

## [1.1.0] - 2026-04-08
### Added
- **Full-Text Search:** Implemented robust search using `Fuse.js` that crawls actual note content (paragraphs, lists, blockquotes).
- **Indexing Script:** Created `index_script.py` to automatically generate `search-index.json` from HTML source files.
- **Search Snippets:** Added contextual text snippets and keyword highlighting to the search results UI.
- **Chapter 3:** Added "Interest Rates & Security Valuation" study guide to the library.

### Changed
- **Navigation:** Added "Back to Library" link to all individual study guide sidebars for better user flow.
- **Search Logic:** Migrated from hardcoded keywords to a dynamic JSON search index for better maintainability.

## [1.0.0] - 2026-04-08
### Added
- **Library Hub:** Created a "clear and rigorous" landing page (`index.html`) to organize multiple courses.
- **Course Organization:** Structured repository into `/notes/course-name/` for clean URLs and scalability.
- **README:** Comprehensive documentation for adding new courses and deploying to Vercel.
- **Git Setup:** Initialized repository with `.gitignore` to protect sensitive or heavy files (PDFs, node_modules).

### Security
- **PDF Exclusion:** Untracked and ignored all PDF files to keep the Git repository lightweight and deployment-ready.
