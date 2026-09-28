import re

with open('css/components.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Update nav-link.active
content = re.sub(
    r'\.nav-link\.active\s*\{[^}]*\}',
    r'.nav-link.active {\n    background: rgba(108, 184, 54, 0.2); /* A subtle green translucent background */\n    color: var(--color-primary) !important;\n}',
    content
)

with open('css/components.css', 'w', encoding='utf-8') as f:
    f.write(content)

print("Active state updated.")