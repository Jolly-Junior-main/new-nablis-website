document.addEventListener('DOMContentLoaded', () => {
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    
    document.querySelectorAll('.nav-links .nav-link').forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });

    document.querySelectorAll('.mobile-nav-links .mobile-nav-link').forEach(link => {
        const linkPath = link.getAttribute('href');
        if (linkPath === currentPath) {
            link.style.color = 'var(--color-primary)';
            link.style.fontWeight = 'bold';
        }
    });

    if (typeof injectConfigData === 'function') {
        injectConfigData();
    }
    
    const header = document.querySelector('.site-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 10) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        });
    }

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

        const mobileLinks = drawer.querySelectorAll('.mobile-nav-link, .btn-brand');
        mobileLinks.forEach(link => {
            link.addEventListener('click', toggleMenu);
        });

        document.addEventListener('click', (e) => {
            if (drawer.classList.contains('open') && !drawer.contains(e.target) && !menuBtn.contains(e.target)) {
                toggleMenu();
            }
        });
        
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && drawer.classList.contains('open')) {
                toggleMenu();
            }
        });
    }

    const accordions = document.querySelectorAll('.accordion-header');
    accordions.forEach(acc => {
        acc.addEventListener('click', () => {
            const isActive = acc.classList.contains('active');
            
            accordions.forEach(a => {
                a.classList.remove('active');
                a.nextElementSibling.style.maxHeight = null;
            });

            if (!isActive) {
                acc.classList.add('active');
                const content = acc.nextElementSibling;
                content.style.maxHeight = content.scrollHeight + 'px';
            }
        });
    });
});

function injectConfigData() {
    if (typeof NEW_NABLIS_CONFIG === 'undefined') return;
    
    document.querySelectorAll('.config-phone').forEach(el => {
        if(el.tagName === 'A') el.href = `tel:${NEW_NABLIS_CONFIG.contact.phone}`;
        el.textContent = NEW_NABLIS_CONFIG.contact.phone;
    });
    
    document.querySelectorAll('.config-whatsapp').forEach(el => {
        if(el.tagName === 'A') {
            const msg = el.getAttribute('data-wa-msg') || 'Hello New Nablis, I would like more information about your services.';
            el.href = `https://wa.me/${NEW_NABLIS_CONFIG.contact.whatsapp.replace(/\D/g, '')}?text=${encodeURIComponent(msg)}`;
        }
    });

    document.querySelectorAll('.config-email').forEach(el => {
        if(el.tagName === 'A') el.href = `mailto:${NEW_NABLIS_CONFIG.contact.email}`;
        el.textContent = NEW_NABLIS_CONFIG.contact.email;
    });

    document.querySelectorAll('.config-address').forEach(el => {
        el.textContent = NEW_NABLIS_CONFIG.location.address;
    });

    document.querySelectorAll('.config-hours').forEach(el => {
        el.textContent = NEW_NABLIS_CONFIG.hours.display;
    });
}

// Language Dropdown Toggle
document.addEventListener('DOMContentLoaded', () => {
    const langBtn = document.querySelector('.lang-btn');
    const langMenu = document.querySelector('.lang-menu');
    
    if (langBtn && langMenu) {
        langBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            if (langMenu.style.display === 'none' || langMenu.style.display === '') {
                langMenu.style.display = 'block';
            } else {
                langMenu.style.display = 'none';
            }
        });
        
        // Close when clicking outside
        document.addEventListener('click', (e) => {
            if (!langBtn.contains(e.target) && !langMenu.contains(e.target)) {
                langMenu.style.display = 'none';
            }
        });
    }
});
