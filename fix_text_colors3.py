import glob
import re

for file in glob.glob('*.html') + glob.glob('css/*.css'):
    if 'variables.css' in file: continue
    
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*[0-9.]+\s*\);?', 'color: var(--color-text-muted);', content)
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*[0-9.]+\s*\)', 'color: var(--color-text-muted)', content)
    
    # Also background: #2f2e32 -> var(--color-bg-base)
    content = re.sub(r'background:\s*#2f2e32', 'background: var(--color-bg-base)', content)
    content = re.sub(r'background-color:\s*#2f2e32', 'background-color: var(--color-bg-base)', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Remaining colors fixed.")