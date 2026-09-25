import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The exact string in index.html
    # <a href="services.html" class="nav-link">Services <svg width="10" height="6" viewBox="0 0 10 6" fill="none" style="margin-left:4px;vertical-align:middle"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
    
    # We will use regex to catch slight whitespace differences
    pattern = r'<a href="services\.html" class="nav-link">Services[^<]*<svg.*?svg></a>'
    
    dropdown_html = '''<div class="nav-dropdown-container">
                    <a href="services.html" class="nav-link">Services <svg width="10" height="6" viewBox="0 0 10 6" fill="none" style="margin-left:4px;vertical-align:middle"><path d="M1 1L5 5L9 1" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                    <div class="nav-dropdown-menu">
                        <a href="cleaning.html">Cleaning</a>
                        <a href="property-preparation.html">Property Preparation</a>
                        <a href="contracting.html">Contracting</a>
                        <a href="staffing.html">Workforce & Staffing</a>
                    </div>
                </div>'''
    
    new_content = re.sub(pattern, dropdown_html, content)
    
    # Also update cache busters while we're at it (from v=8 to v=9)
    new_content = new_content.replace('?v=8', '?v=9')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print("Dropdowns added and cache busters updated.")