import glob
import re

html_files = glob.glob('src/*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace href="about.html" with href="/about/"
    # Replace href="index.html" with href="/"
    content = re.sub(r'href="index\.html"', 'href="/"', content)
    content = re.sub(r'href="([^"]+)\.html"', r'href="/\1/"', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("HTML links updated for clean URLs.")