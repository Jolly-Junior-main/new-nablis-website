import glob
import re

html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    mobile_nav_services = r'<a href="services\.html" class="mobile-nav-link">Services</a>'
    mobile_dropdown_html = '''<a href="services.html" class="mobile-nav-link">Services</a>
        <div style="padding-left: 20px; display: flex; flex-direction: column; gap: 8px;">
            <a href="cleaning.html" class="mobile-nav-link" style="font-size: 14px; opacity: 0.8;">Cleaning</a>
            <a href="property-preparation.html" class="mobile-nav-link" style="font-size: 14px; opacity: 0.8;">Property Preparation</a>
            <a href="contracting.html" class="mobile-nav-link" style="font-size: 14px; opacity: 0.8;">Contracting</a>
            <a href="staffing.html" class="mobile-nav-link" style="font-size: 14px; opacity: 0.8;">Workforce & Staffing</a>
        </div>'''
    
    if '<div style="padding-left: 20px;' not in content:
        content = re.sub(mobile_nav_services, mobile_dropdown_html, content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print("Mobile sub-links added.")