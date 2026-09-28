import re

with open('css/responsive.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Update mobile-nav-link color
content = re.sub(
    r'(\.mobile-nav-link\s*\{[^}]*color:\s*)var\(--color-text-light\)',
    r'\1var(--color-primary)',
    content
)

with open('css/responsive.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Mobile updates applied.")