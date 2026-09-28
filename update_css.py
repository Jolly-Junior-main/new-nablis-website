import re

with open('css/components.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Update nav-dropdown-container
content = re.sub(
    r'\.nav-dropdown-container\s*\{\s*position:\s*relative;\s*display:\s*inline-block;\s*\}',
    r'.nav-dropdown-container {\n    position: relative;\n    display: flex;\n    align-items: center;\n}',
    content
)

# Update nav-dropdown-menu a color
content = re.sub(
    r'(\.nav-dropdown-menu a\s*\{[^}]*color:\s*)var\(--color-text-light\)',
    r'\1var(--color-primary)',
    content
)

with open('css/components.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updates applied.")