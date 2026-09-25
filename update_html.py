import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Add Theme Toggle Button
    button_html = '''<button class="theme-toggle" aria-label="Toggle Theme" style="background: transparent; border: 1px solid var(--glass-border); color: var(--color-text-light); padding: 6px 12px; border-radius: 20px; display: flex; align-items: center; justify-content: center; cursor: pointer;" onclick="toggleTheme()">
              <svg class="sun-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="5"></circle><line x1="12" y1="1" x2="12" y2="3"></line><line x1="12" y1="21" x2="12" y2="23"></line><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line><line x1="1" y1="12" x2="3" y2="12"></line><line x1="21" y1="12" x2="23" y2="12"></line><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line></svg>
              <svg class="moon-icon" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display: none;"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path></svg>
          </button>
          '''
    if 'class="theme-toggle"' not in content:
        content = content.replace('<div class="lang-dropdown"', button_html + '<div class="lang-dropdown"')

    # 2. Replace hardcoded inline colors
    content = content.replace('color: #fff', 'color: var(--color-text-light)')
    content = content.replace('color: white', 'color: var(--color-text-light)')
    content = content.replace('color: rgba(255,255,255,0.7)', 'color: var(--color-text-muted)')
    content = content.replace('color: rgba(255,255,255,0.5)', 'color: var(--color-text-muted)')
    content = content.replace('border: 1px solid rgba(255,255,255,0.1)', 'border: 1px solid var(--glass-border)')
    content = content.replace('border: 1px solid rgba(255, 255, 255, 0.1)', 'border: 1px solid var(--glass-border)')
    content = content.replace('border-bottom: 1px solid rgba(255,255,255,0.05)', 'border-bottom: 1px solid var(--glass-border)')
    content = content.replace('background: rgba(40,40,45,0.95)', 'background: var(--glass-bg-hover)')
    content = content.replace('background: rgba(40, 40, 45, 0.6)', 'background: var(--glass-bg)')
    content = content.replace('background: rgba(255, 255, 255, 0.02)', 'background: var(--glass-border)')
    content = content.replace('background: rgba(255, 255, 255, 0.05)', 'background: var(--glass-border)')
    content = content.replace('rgba(255,255,255,0.2)', 'var(--glass-border)')
    
    # Let's fix the SVG colors too
    content = content.replace('stroke="#fff"', 'stroke="currentColor"')
    content = content.replace('stroke="white"', 'stroke="currentColor"')
    content = content.replace('stroke="#1a1a1a"', 'stroke="currentColor"')
    content = content.replace('fill="#fff"', 'fill="currentColor"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Updated HTML files.")