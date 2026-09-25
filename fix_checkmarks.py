import os
import glob
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
        
    # Fix inline styles for checkmarks
    content = content.replace('.check-list li::before { content: "o"";', '.check-list li::before { content: "\\2714";')
    content = content.replace('.check-list li::before { content: "âœ”";', '.check-list li::before { content: "\\2714";')
    content = content.replace('.check-list li::before { content: "✔";', '.check-list li::before { content: "\\2714";')
    
    # Fix html text checkmarks
    content = content.replace('o"', '&#10004;')
    content = content.replace('âœ”', '&#10004;')
    content = content.replace('✔', '&#10004;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)