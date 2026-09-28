import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # If it doesn't already have a favicon
    if '<link rel="icon"' not in content:
        # Insert before </head>
        content = content.replace('</head>', '    <link rel="icon" type="image/png" href="assets/images/logo/logo.png">\n</head>')
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)

print("Favicon added to all HTML files.")