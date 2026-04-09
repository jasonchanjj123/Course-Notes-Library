(function() {
  const urlParams = new URLSearchParams(window.location.search);
  const query = urlParams.get('h');
  if (!query) return;

  // Add styles for the highlight
  const style = document.createElement('style');
  style.textContent = `
    .search-highlight-flash {
      background-color: #ffeb3b !important;
      transition: background-color 2s ease-out;
      border-radius: 3px;
      padding: 0 2px;
      box-shadow: 0 0 8px rgba(255, 235, 59, 0.8);
    }
    .search-highlight-fade {
      background-color: transparent !important;
    }
  `;
  document.head.appendChild(style);

  // Function to find and highlight text
  function highlightText(root, text) {
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
    let node;
    const regex = new RegExp(`(${text.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, '\\$&')})`, 'gi');
    const nodesToReplace = [];

    while (node = walker.nextNode()) {
      if (node.parentElement.tagName === 'SCRIPT' || node.parentElement.tagName === 'STYLE') continue;
      if (regex.test(node.nodeValue)) {
        nodesToReplace.push(node);
      }
    }

    nodesToReplace.forEach(textNode => {
      const parent = textNode.parentElement;
      const html = textNode.nodeValue.replace(regex, '<span class="search-highlight-flash">$1</span>');
      const tempDiv = document.createElement('div');
      tempDiv.innerHTML = html;
      
      while (tempDiv.firstChild) {
        parent.insertBefore(tempDiv.firstChild, textNode);
      }
      parent.removeChild(textNode);
    });

    // Scroll to the first highlight
    const firstHighlight = document.querySelector('.search-highlight-flash');
    if (firstHighlight) {
      setTimeout(() => {
        firstHighlight.scrollIntoView({ behavior: 'smooth', block: 'center' });
        
        // Fade out effect after a delay
        setTimeout(() => {
          document.querySelectorAll('.search-highlight-flash').forEach(el => {
            el.classList.add('search-highlight-fade');
          });
        }, 2000);
      }, 500);
    }
  }

  // Execute after a short delay to ensure rendering and scroll smooth-ness
  window.addEventListener('load', () => {
    highlightText(document.body, query);
  });
})();
