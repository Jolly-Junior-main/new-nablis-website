# What We Built: New Nablis Website

This document serves as a comprehensive overview of the newly developed website for **New Nablis**, a premier Cleaning and Contracting business. The project was built from the ground up using modern web standards, focusing on high performance, accessibility, and cutting-edge design aesthetics.

## Core Architecture & Tech Stack
- **Frontend Core:** Pure HTML5, CSS3, and Vanilla JavaScript (No heavy frameworks, ensuring blazing fast load times).
- **Deployment:** Cloudflare Pages (Serverless global CDN).
- **Styling:** Custom CSS with CSS Variables for easy theming, utilizing Flexbox and CSS Grid for responsive layouts.

## Key Features Developed

### 1. Modern Glassmorphism UI
The entire website is built around a modern "Glassmorphism" aesthetic. Key elements (like the navigation bar, contact cards, and service blocks) feature frosted-glass translucent backgrounds with subtle blurs (ackdrop-filter: blur()), providing a highly premium and futuristic feel.

### 2. Dual Theme (Light & Dark Mode)
- **Default Mode:** A sleek, professional Dark Mode that emphasizes the glowing elements and glass panels.
- **Light Mode Toggle:** A fully functional theme switcher in the navigation bar allows users to toggle to Light Mode. The entire color palette (ar(--color-bg-base), text colors, and glass transparencies) dynamically transitions to ensure perfect readability while maintaining the glass aesthetic.
- **Hero Image Exception:** The homepage hero text is permanently locked to white, as it always overlays a dark hero background image regardless of the selected theme.

### 3. Fully Responsive Navigation
- **Desktop:** A floating "pill-style" navigation bar with perfect vertical alignment, translucent hover states, and a seamless drop-down menu for the "Services" section.
- **Mobile:** A custom hamburger menu that slides out a mobile navigation drawer. The drawer includes nested, indented links for the services section for easy mobile browsing.
- **Dynamic Scrolling:** The navigation bar adapts and forms a solid glass panel at the top of the screen once the user begins scrolling down the page.

### 4. AI-Generated Asset Integration
To ensure the website visually stands out, we utilized advanced AI generation to create high-quality, 4K custom imagery:
- **Service Pages:** We generated 9 unique, photorealistic images tailored to specific services (e.g., Deep Cleaning, Floor Care, Light Remodeling, Estate Cleanouts) and dynamically embedded them into the respective .service-image placeholder blocks across cleaning.html, property-preparation.html, and contracting.html.
- **Contact Us Page:** We completely overhauled the Contact Us page layout to feature a 2x2 grid of modern, glowing 3D neon icons (Envelope, Headset, Map Pin, and Clock). These custom AI-generated icons perfectly match the cyber/glassmorphism dark UI style.

### 5. Multi-Language Support
The website is structured to support multi-language audiences, specifically targeting English, Arabic (العربية), and Amharic (አማርኛ) speakers, allowing the business to cater to its diverse client base in Qatar.

### 6. WhatsApp & Booking Integrations
- Floating WhatsApp buttons and dedicated "Instant Support" call-to-actions are strategically placed to drive high-conversion emergency bookings.
- A dedicated quote.html page houses the main lead-capture form.

## Page Breakdown
1. **index.html**: The main landing page featuring the hero section, company overview, and high-level service summaries.
2. **bout.html**: Details the company's mission, values, and dedication to quality.
3. **services.html**: The central hub for all services, providing pathways to specific service categories.
4. **cleaning.html**: Detailed page for Routine Janitorial, Deep Cleaning, and Floor Care.
5. **property-preparation.html**: Detailed page for Post-Construction, Move-In/Out, and Estate Cleanouts.
6. **contracting.html**: Detailed page for Light Remodeling, Property Maintenance, and Exterior Improvements.
7. **staffing.html**: Detailed page regarding Workforce and Staffing solutions.
8. **contact.html**: The reimagined 2x2 grid contact page with glowing neon icons and direct communication links.
9. **quote.html**: The direct booking and estimate request form.

## Conclusion
The New Nablis website is now a state-of-the-art, lightning-fast digital storefront. It leverages modern CSS capabilities and AI imagery to provide a premium user experience that establishes instant trust and authority in the contracting and cleaning sector.
