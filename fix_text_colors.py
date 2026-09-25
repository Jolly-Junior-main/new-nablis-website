import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Replace white text colors
    content = re.sub(r'color:\s*#ffffff;?', 'color: var(--color-text-light);', content, flags=re.IGNORECASE)
    content = re.sub(r'color:\s*#fff;?', 'color: var(--color-text-light);', content, flags=re.IGNORECASE)
    content = re.sub(r'color:\s*white;?', 'color: var(--color-text-light);', content, flags=re.IGNORECASE)
    
    # Replace rgba white text colors (like rgba(255,255,255,0.7) -> var(--color-text-muted))
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.7\s*\);?', 'color: var(--color-text-muted);', content)
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.8\s*\);?', 'color: var(--color-text-muted);', content)
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.5\s*\);?', 'color: var(--color-text-muted);', content)
    content = re.sub(r'color:\s*rgba\(\s*255\s*,\s*255\s*,\s*255\s*,\s*0\.6\s*\);?', 'color: var(--color-text-muted);', content)
    
    # SVG strokes and fills
    content = re.sub(r'stroke="#ffffff"', 'stroke="currentColor"', content, flags=re.IGNORECASE)
    content = re.sub(r'stroke="white"', 'stroke="currentColor"', content, flags=re.IGNORECASE)
    content = re.sub(r'fill="#ffffff"', 'fill="currentColor"', content, flags=re.IGNORECASE)
    content = re.sub(r'fill="white"', 'fill="currentColor"', content, flags=re.IGNORECASE)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML files text colors fixed.")