import os
import glob
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Fix the very specific broken string
    content = content.replace('.check-list li::before { content: "o"";', '.check-list li::before { content: "\\2714";')
    content = content.replace('o"', '&#10004;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)