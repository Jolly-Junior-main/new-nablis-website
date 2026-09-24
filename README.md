# New Nablis Cleaning and Contracting - Website

This is a complete, static HTML5/CSS3/Vanilla JS website built for New Nablis Cleaning and Contracting in Doha, Qatar.

## Architecture

- **No backend required:** This website consists entirely of static files.
- **No framework required:** Pure HTML, CSS, and Vanilla JavaScript.
- **Deployable anywhere:** Can be hosted on any static hosting provider (GitHub Pages, Netlify, Vercel, shared hosting `public_html`).

## How to Edit the Website

All central business information is managed in one file to make updates easy.

### Changing Contact Info (Phone, WhatsApp, Email, Address, etc.)

1. Open `js/config.js`
2. Update the values in the `NEW_NABLIS_CONFIG` object.
3. The changes will automatically reflect across the entire website (header, footer, contact page, WhatsApp buttons).

Example `js/config.js`:
```javascript
const NEW_NABLIS_CONFIG = {
    contact: {
        phone: "+974 0000 0000",
        whatsapp: "+97400000000",
        email: "info@newnablis.qa"
    }
};
```

### Changing Images

1. Place your new images in the appropriate folder under `assets/images/`.
2. Update the `src` attribute of the `<img>` tags or the background CSS in the HTML files.
3. Use WebP or AVIF format for better performance.

## How to Deploy

1. Open the finished project folder.
2. Confirm contact details in `js/config.js`.
3. Purchase a domain name and set up a static web hosting plan.
4. Upload all files (including `index.html`, `css/`, `js/`, `assets/`, etc.) to the root directory of your host (usually `public_html` or `www`).
5. Connect your domain to the hosting provider if not already connected.
6. Configure SSL/HTTPS in your hosting control panel to ensure secure connections.
7. Test the production domain in your browser.

## Browser Support

Tested and supported on all modern browsers:
- Google Chrome
- Microsoft Edge
- Mozilla Firefox
- Apple Safari (macOS & iOS)
- Android Chrome
