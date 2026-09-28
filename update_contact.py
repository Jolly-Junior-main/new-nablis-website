import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the contact-dashboard section with the new grid
new_html = '''
    <style>
        .contact-style-grid {
            padding: 100px 0;
            background: transparent;
        }
        .contact-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 30px;
        }
        @media(max-width: 768px) {
            .contact-grid {
                grid-template-columns: 1fr;
            }
        }
        .contact-card {
            background: rgba(20, 25, 30, 0.6);
            border: 1px solid rgba(255, 255, 255, 0.05);
            border-radius: 16px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.3s ease;
        }
        body.light-mode .contact-card {
            background: rgba(255, 255, 255, 0.8);
            border: 1px solid rgba(0, 0, 0, 0.1);
        }
        .contact-card:hover {
            transform: translateY(-5px);
        }
        .contact-card .card-image {
            width: 100%;
            height: 250px;
            background-position: center;
            background-size: cover;
            border-bottom: 1px solid rgba(255,255,255,0.05);
        }
        body.light-mode .contact-card .card-image {
            border-bottom: 1px solid rgba(0,0,0,0.1);
        }
        .contact-card .card-content {
            padding: 30px;
        }
        .contact-card h3 {
            font-size: 22px;
            font-weight: 600;
            color: var(--color-text-light);
            margin-bottom: 12px;
        }
        .contact-card p {
            font-size: 15px;
            color: var(--color-text-muted);
            line-height: 1.6;
            margin-bottom: 20px;
        }
        .contact-card a, .contact-card .contact-detail {
            color: var(--color-primary);
            text-decoration: none;
            font-weight: 600;
            font-size: 16px;
        }
    </style>

    <section class="contact-style-grid">
        <div class="container reveal">
            <div style="text-align: center; margin-bottom: 60px;">
                <h2 style="font-size: 36px; color: var(--color-text-light); margin-bottom: 16px;">Contact Us</h2>
                <p style="color: var(--color-text-muted); max-width: 600px; margin: 0 auto;">We are here to assist you. Reach out through any of the channels below.</p>
            </div>
            
            <div class="contact-grid">
                <!-- Card 1 -->
                <div class="contact-card">
                    <div class="card-image" style="background-image: url('assets/images/contact_email_1790610007485.jpg');"></div>
                    <div class="card-content">
                        <h3>Email Support</h3>
                        <p>Drop us an email anytime. Our customer service team will review your inquiry and get back to you within 24 hours.</p>
                        <a href="mailto:info@newnablis.com">info@newnablis.com</a>
                    </div>
                </div>
                
                <!-- Card 2 -->
                <div class="contact-card">
                    <div class="card-image" style="background-image: url('assets/images/contact_phone_1790610035652.jpg');"></div>
                    <div class="card-content">
                        <h3>Instant Support</h3>
                        <p>Need immediate assistance or emergency booking? Call our support hotline or message us on WhatsApp for rapid response.</p>
                        <div class="contact-detail">+974 XXXXXXX</div>
                    </div>
                </div>
                
                <!-- Card 3 -->
                <div class="contact-card">
                    <div class="card-image" style="background-image: url('assets/images/contact_location_1790610071273.jpg');"></div>
                    <div class="card-content">
                        <h3>Headquarters</h3>
                        <p>Our main operations and management are located centrally. Feel free to visit us for formal contracting discussions.</p>
                        <div class="contact-detail">Doha, Qatar</div>
                    </div>
                </div>
                
                <!-- Card 4 -->
                <div class="contact-card">
                    <div class="card-image" style="background-image: url('assets/images/contact_clock_1790610093668.jpg');"></div>
                    <div class="card-content">
                        <h3>Working Hours</h3>
                        <p>Our teams are available six days a week to ensure your properties remain clean, maintained, and secure.</p>
                        <div class="contact-detail">Sat - Thu: 8:00 AM - 6:00 PM</div>
                    </div>
                </div>
            </div>
            
            <div style="margin-top: 60px; text-align: center;">
                <a href="quote.html" class="btn-brand" style="font-size: 18px; padding: 15px 40px;">Send a Direct Message</a>
            </div>
        </div>
    </section>
'''

# Find the main tag content and replace it
content = re.sub(
    r'<section class="contact-dashboard">.*?(?=\s*</main>)',
    new_html,
    content,
    flags=re.DOTALL
)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("contact.html updated with 2x2 grid.")