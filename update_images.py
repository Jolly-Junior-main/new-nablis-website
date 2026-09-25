import re

def update_file(filename, replacements):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for text_placeholder, image_filename in replacements.items():
        # Look for <div class="service-image"> \n <div style="...">[Image: X]</div> \n </div>
        # And replace it with <div class="service-image" style="background: url('assets/images/X.jpg') center/cover;"></div>
        
        # Regex to match the placeholder
        pattern = r'<div class="service-image">\s*<div[^>]*>\[' + re.escape(text_placeholder) + r'\]</div>\s*</div>'
        replacement = f'<div class="service-image" style="background: url(\'assets/images/{image_filename}\') center/cover;"></div>'
        
        content = re.sub(pattern, replacement, content)
        
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

cleaning_reps = {
    'Image: Deep Cleaning': 'deep_cleaning.jpg',
    'Image: Routine Janitorial': 'routine_janitorial.jpg',
    'Image: Floor Care': 'floor_care.jpg'
}
update_file('cleaning.html', cleaning_reps)

contracting_reps = {
    'Image: Light Remodeling': 'light_remodeling.jpg',
    'Image: Property Maintenance': 'property_maintenance.jpg',
    'Image: Exterior Improvements': 'exterior_improvements.jpg'
}
update_file('contracting.html', contracting_reps)

property_prep_reps = {
    'Image: Post Construction Cleaning': 'post_construction.jpg',
    'Image: Move In/Out Turnkey': 'move_in_out.jpg',
    'Image: Estate Cleanout': 'estate_cleanout.jpg'
}
update_file('property-preparation.html', property_prep_reps)

print("Updated HTML files with background images!")