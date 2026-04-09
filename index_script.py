import os
import json
import re
from html.parser import HTMLParser

class SimpleHTMLIndexer(HTMLParser):
    def __init__(self, base_url, course_name, chapter_name):
        super().__init__()
        self.base_url = base_url
        self.course_name = course_name
        self.chapter_name = chapter_name
        self.results = []
        self.current_section = {"title": chapter_name, "subtitle": course_name, "url": base_url, "content": ""}
        self.in_title = False
        self.in_h2_h3 = False
        self.in_content = False
        self.content_buffer = []
        self.section_id = ""

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)
        if tag in ['h2', 'h3']:
            # Save previous section if it has content
            if self.current_section['content']:
                self.results.append(self.current_section)
            
            self.section_id = attrs_dict.get('id', '')
            self.in_h2_h3 = True
            self.content_buffer = []
            url = f"{self.base_url}#{self.section_id}" if self.section_id else self.base_url
            self.current_section = {"title": "", "subtitle": f"{self.chapter_name} · {self.course_name}", "url": url, "content": ""}
        elif tag in ['p', 'li', 'blockquote', 'div']:
            # Basic content tags
            if 'callout-body' in attrs_dict.get('class', '') or tag in ['p', 'li', 'blockquote']:
                self.in_content = True

    def handle_endtag(self, tag):
        if tag in ['h2', 'h3']:
            self.current_section['title'] = "".join(self.content_buffer).strip()
            self.content_buffer = []
            self.in_h2_h3 = False
        elif tag in ['p', 'li', 'blockquote', 'div']:
            if self.in_content:
                text = "".join(self.content_buffer).strip()
                if text:
                    self.current_section['content'] += " " + text
                self.content_buffer = []
                self.in_content = False

    def handle_data(self, data):
        if self.in_h2_h3 or self.in_content:
            self.content_buffer.append(data)

    def finalize(self):
        if self.current_section['content']:
            self.results.append(self.current_section)
        return self.results

def generate_course_card(course_dir, meta, chapters):
    badge = meta.get("badge", "Course")
    title = meta.get("title", course_dir.replace('-', ' ').title())
    desc = meta.get("description", "Study materials and notes.")
    
    html = f'''      <!-- {course_dir.upper()} -->
      <div class="course-card">
        <div class="course-badge">{badge}</div>
        <h2 class="course-title">{title}</h2>
        <p class="course-desc">{desc}</p>
        <ul class="chapter-list">\n'''
        
    if not chapters:
        html += '''          <li><a href="#" class="chapter-link coming-soon"><span class="chapter-icon">📄</span> Library under construction <span class="status-tag">Coming Soon</span></a></li>\n'''
    else:
        for ch in chapters:
            html += f'''          <li><a href="{ch['url']}" class="chapter-link"><span class="chapter-icon">📄</span> {ch['title']}</a></li>\n'''
            
    html += '''        </ul>
      </div>\n'''
    return html

def update_index_html(cards_html):
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace the contents of <div class="course-grid">
    pattern = r'(<div class="course-grid">\s*\n)(.*?)(    </div>\s*</main>)'
    
    match = re.search(pattern, content, flags=re.DOTALL)
    if match:
        new_content = content[:match.start(2)] + cards_html + content[match.start(3):]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Updated index.html with new course grid.")
    else:
        print("Could not find course-grid in index.html to update. Ensure '<div class=\"course-grid\">' exists.")

def index_notes():
    index = []
    base_notes_dir = 'notes'
    
    cards_html = ""
    
    if not os.path.exists(base_notes_dir):
        print(f"Directory {base_notes_dir} does not exist.")
        return
        
    for course_dir in sorted(os.listdir(base_notes_dir)):
        course_path = os.path.join(base_notes_dir, course_dir)
        if not os.path.isdir(course_path):
            continue
            
        # Read meta.json if exists
        meta = {}
        meta_path = os.path.join(course_path, 'meta.json')
        if os.path.exists(meta_path):
            with open(meta_path, 'r', encoding='utf-8') as f:
                try:
                    meta = json.load(f)
                except json.JSONDecodeError:
                    print(f"Warning: Could not parse {meta_path}")
        
        course_name = meta.get("title", course_dir.replace('-', ' ').title())
        chapters = []
        
        for filename in sorted(os.listdir(course_path)):
            if filename.endswith('.html'):
                filepath = os.path.join(course_path, filename)
                with open(filepath, 'r+', encoding='utf-8') as f:
                    html = f.read()
                    
                    # Inject highlight script if not present
                    if 'highlight.js' not in html:
                        # Calculate relative path to root from notes/<course_dir>/<filename>
                        # Path: notes/ (1) + course_dir/ (2) + filename (3) - wait,
                        # File is notes/course/file.html
                        # dirname is notes/course (2 levels from root)
                        rel_to_root = "../../"
                        script_tag = f'\n<script src="{rel_to_root}highlight.js"></script>\n'
                        if '</body>' in html:
                            html = html.replace('</body>', f'{script_tag}</body>')
                            f.seek(0)
                            f.write(html)
                            f.truncate()
                        elif '</html>' in html:
                            html = html.replace('</html>', f'{script_tag}</html>')
                            f.seek(0)
                            f.write(html)
                            f.truncate()

                    # Extract title
                    title_match = re.search(r'<title>(.*?)</title>', html)
                    full_title = title_match.group(1) if title_match else filename
                    
                    # Clean up title for the card
                    base_title = full_title.split('—')[0].strip()
                    card_title = re.sub(r'^Chapter\s+(\d+)[\s:–-]*', r'Ch \1: ', base_title)
                    
                    chapters.append({
                        "title": card_title,
                        "url": f"notes/{course_dir}/{filename}"
                    })
                    
                    indexer = SimpleHTMLIndexer(f"notes/{course_dir}/{filename}", course_name, base_title)
                    indexer.feed(html)
                    index.extend(indexer.finalize())
                    
        cards_html += generate_course_card(course_dir, meta, chapters)
    
    with open('search-index.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)
        print("Generated search-index.json.")
        
    update_index_html(cards_html)

if __name__ == "__main__":
    index_notes()