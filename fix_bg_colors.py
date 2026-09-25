import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    content = re.sub(r'background:\s*white;?', 'background: var(--color-text-light);', content, flags=re.IGNORECASE)
    content = re.sub(r'background:\s*#fff;?', 'background: var(--color-text-light);', content, flags=re.IGNORECASE)
    content = re.sub(r'background:\s*#ffffff;?', 'background: var(--color-text-light);', content, flags=re.IGNORECASE)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML backgrounds fixed.")