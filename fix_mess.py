import glob
import re

for file in glob.glob('*.html') + glob.glob('css/*.css'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Fix the messed up replacements
    content = content.replace('var(--color-text-light)fff;', 'var(--color-text-light);')
    content = content.replace('var(--color-text-light)fff', 'var(--color-text-light)')
    content = content.replace('var(--color-text-light);fff;', 'var(--color-text-light);')
    content = content.replace('var(--color-text-light);fff', 'var(--color-text-light)')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Regex mess ups fixed.")