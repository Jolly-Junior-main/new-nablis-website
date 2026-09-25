import glob
import re

for file in glob.glob('*.html'):
    with open(file, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Restore Arabic
    content = re.sub(
        r'<a href="#" onclick="changeLanguage\(\'ar\'\);[^>]*>\?\?\?\?\?\?\?</a>',
        """<a href="#" onclick="changeLanguage('ar'); return false;" style="display: block; padding: 10px 16px; color: white; text-decoration: none; border-bottom: 1px solid rgba(255,255,255,0.05); font-family: 'Cairo', sans-serif; font-size: 14px; text-align: left;">العربية</a>""",
        content
    )
    # Restore Amharic
    content = re.sub(
        r'<a href="#" onclick="changeLanguage\(\'am\'\);[^>]*>\?\?\?\?</a>',
        """<a href="#" onclick="changeLanguage('am'); return false;" style="display: block; padding: 10px 16px; color: white; text-decoration: none; font-family: 'Noto Sans Ethiopic', sans-serif; font-size: 14px; text-align: left;">አማርኛ</a>""",
        content
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)