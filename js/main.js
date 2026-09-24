document.addEventListener('DOMContentLoaded', () => {
        // Set Active Menu Link Based on URL
    const currentPath = window.location.pathname.split("/").pop() || "index.html";
    
    // Desktop Nav
    document.querySelectorAll(".nav-links .nav-link").forEach(link => {
        const linkPath = link.getAttribute("href");
        if (linkPath === currentPath) {
            link.classList.add("active");
        } else {
            link.classList.remove("active");
        }
    });

    // Mobile Nav
    document.querySelectorAll(".mobile-nav-links .mobile-nav-link").forEach(link => {
        const linkPath = link.getAttribute("href");
        if (linkPath === currentPath) {
            link.style.color = "var(--color-green)";
            link.style.fontWeight = "bold";
        }
    });

        } else {
            link.classList.remove("active");
        }
    });

    // Inject Config Data
    injectConfigData();
    
    // Header Scroll Effect
    const header = document.querySelector('.site-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 10) {
                header.classList.add('scrolled');
    
    // Set Active Mobile Menu Link Based on URL
    document.querySelectorAll(".mobile-nav-links .mobile-nav-link").forEach(link => {
        const linkPath = link.getAttribute("href");
        if (linkPath === currentPath) {
            link.style.color = "var(--color-green)";
            link.style.fontWeight = "bold";
        }
    });

        } else {
                header.classList.remove('scrolled');
            }
        });
    }

    // Mobile Menu
    const menuBtn = document.querySelector('.mobile-menu-btn');
    const drawer = document.querySelector('.mobile-nav-drawer');
    const body = document.body;

    if (menuBtn && drawer) {
        const toggleMenu = () => {
            drawer.classList.toggle('open');
            body.classList.toggle('menu-open');
        };

        menuBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleMenu();
        });

        // Close on link click
        const mobileLinks = drawer.querySelectorAll('.mobile-nav-link, .btn');
        mobileLinks.forEach(link => {
            link.addEventListener('click', toggleMenu);
        });

        // Close on click outside
        document.addEventListener('click', (e) => {
            if (drawer.classList.contains('open') && !drawer.contains(e.target) && !menuBtn.contains(e.target)) {
                toggleMenu();
            }
        });
        
        // Close on Escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && drawer.classList.contains('open')) {
                toggleMenu();
            }
        });
    }

    // FAQ Accordion
    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(acc => {
        acc.addEventListener('click', () => {
            const isActive = acc.classList.contains('active');
            
            // Close all
            accordions.forEach(a => {
                a.classList.remove('active');
                a.nextElementSibling.style.maxHeight = null;
            });

            // If it wasn't active, open it
            if (!isActive) {
                acc.classList.add('active');
                const content = acc.nextElementSibling;
                content.style.maxHeight = content.scrollHeight + "px";
            }
        });
    });
});

function injectConfigData() {
    // Phone
    document.querySelectorAll('.config-phone').forEach(el => {
        if(el.tagName === 'A') el.href = `tel:${NEW_NABLIS_CONFIG.contact.phone}`;
        el.textContent = NEW_NABLIS_CONFIG.contact.phone;
    });
    
    // WhatsApp Global
    document.querySelectorAll('.config-whatsapp').forEach(el => {
        if(el.tagName === 'A') {
            const msg = el.getAttribute('data-wa-msg') || 'Hello New Nablis, I would like more information about your services.';
            el.href = `https://wa.me/${NEW_NABLIS_CONFIG.contact.whatsapp.replace(/\D/g, '')}?text=${encodeURIComponent(msg)}`;

    // Set Active Mobile Menu Link Based on URL
    document.querySelectorAll(".mobile-nav-links .mobile-nav-link").forEach(link => {
        const linkPath = link.getAttribute("href");
        if (linkPath === currentPath) {
            link.style.color = "var(--color-green)";
            link.style.fontWeight = "bold";
        }
    });

        } else {
            el.textContent = NEW_NABLIS_CONFIG.contact.whatsapp;
        }
    });

    // Email
    document.querySelectorAll('.config-email').forEach(el => {
        if(el.tagName === 'A') el.href = `mailto:${NEW_NABLIS_CONFIG.contact.email}`;
        el.textContent = NEW_NABLIS_CONFIG.contact.email;
    });

    // Address
    document.querySelectorAll('.config-address').forEach(el => {
        el.textContent = NEW_NABLIS_CONFIG.location.address;
    });

    // Working Hours
    document.querySelectorAll('.config-hours').forEach(el => {
        el.textContent = NEW_NABLIS_CONFIG.hours.display;
    });
}



