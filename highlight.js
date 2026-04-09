(function() {
  const urlParams = new URLSearchParams(window.location.search);
  const query = urlParams.get('h');
  if (!query) return;

  const decodedQuery = decodeURIComponent(query);

  // Add styles for the highlight
  const style = document.createElement('style');
  style.textContent = `
    .search-highlight-flash {
      background-color: #ffeb3b !important;
      transition: background-color 2s ease-out;
      border-radius: 3px;
      padding: 0 2px;
      box-shadow: 0 0 8px rgba(255, 235, 59, 0.8);
      color: #000 !important;
      display: inline-block;
    }
    .search-highlight-fade {
      background-color: transparent !important;
      box-shadow: none !important;
    }
  `;
  document.head.appendChild(style);

  function highlightAndScroll() {
    const text = decodedQuery;
    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, null, false);
    let node;
    const regex = new RegExp(`(${text.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, '\\$&')})`, 'gi');
    const nodesToReplace = [];

    while (node = walker.nextNode()) {
      if (node.parentElement.closest('script, style, nav, .sidebar')) continue;
      if (regex.test(node.nodeValue)) {
        nodesToReplace.push(node);
      }
    }

    nodesToReplace.forEach(textNode => {
      const parent = textNode.parentElement;
      if (!parent) return;
      
      const html = textNode.nodeValue.replace(regex, '<span class="search-highlight-flash">$1</span>');
      const span = document.createElement('span');
      span.innerHTML = html;
      
      parent.replaceChild(span, textNode);
    });

    // Scroll to the first highlight
    const firstHighlight = document.querySelector('.search-highlight-flash');
    if (firstHighlight) {
      // Force a slight delay to ensure browser layout is stable
      setTimeout(() => {
        firstHighlight.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        // Fade out effect
        setTimeout(() => {
          document.querySelectorAll('.search-highlight-flash').forEach(el => {
            el.classList.add('search-highlight-fade');
          });
        }, 3000);
      }, 300);
    }
  }

  if (document.readyState === 'complete') {
    highlightAndScroll();
  } else {
    window.addEventListener('load', highlightAndScroll);
  }
})();
