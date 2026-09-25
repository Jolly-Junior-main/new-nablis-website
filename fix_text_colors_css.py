import glob
import re

for file in glob.glob('css/*.css'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # We shouldn't replace variables.css
    if 'variables.css' in file:
        continue
        
    content = re.sub(r'color:\s*#ffffff;?', 'color: var(--color-text-light);', content, flags=re.IGNORECASE)
    content = re.sub(r'color:\s*#fff;?', 'color: var(--color-text-light);', content, flags=re.IGNORECASE)
    content = re.sub(r'color:\s*white;?', 'color: var(--color-text-light);', content, flags=re.IGNORECASE)
    
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.7\s*\);?', 'color: var(--color-text-muted);', content)
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.8\s*\);?', 'color: var(--color-text-muted);', content)
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.5\s*\);?', 'color: var(--color-text-muted);', content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("CSS files text colors fixed.")