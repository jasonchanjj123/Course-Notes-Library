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

def index_notes():
    index = []
    notes_dir = 'notes/financial-market'
    for filename in sorted(os.listdir(notes_dir)):
        if filename.endswith('.html'):
            filepath = os.path.join(notes_dir, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                html = f.read()
                
                # Extract course and chapter from file
                title_match = re.search(r'<title>(.*?)</title>', html)
                title = title_match.group(1).split(' — ')[0] if title_match else filename
                
                course_match = re.search(r'<div class="sidebar-course">(.*?)</div>', html)
                course = course_match.group(1).strip() if course_match else "Financial Markets"
                
                indexer = SimpleHTMLIndexer(f"notes/financial-market/{filename}", course, title)
                indexer.feed(html)
                index.extend(indexer.finalize())
    
    with open('search-index.json', 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2)

if __name__ == "__main__":
    index_notes()
