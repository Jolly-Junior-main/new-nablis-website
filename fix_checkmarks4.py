import glob
for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Just replace all occurrences of that weird sequence
    content = content.replace('o"', '&#10004;')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)