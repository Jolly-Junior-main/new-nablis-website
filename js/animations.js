document.addEventListener('DOMContentLoaded', () => {
    // Reveal Animations using IntersectionObserver
    const revealElements = document.querySelectorAll('.reveal');

    const revealOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const revealOnScroll = new IntersectionObserver(function(entries, observer) {
        entries.forEach(entry => {
            if (!entry.isIntersecting) {
                return;
            } else {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, revealOptions);

    revealElements.forEach(el => {
        revealOnScroll.observe(el);
    });
});

// Base CSS class for reveal
/* Add to main.css:
.reveal {
    opacity: 0;
    transform: translateY(30px);
    transition: all 0.6s ease;
}
.reveal.active {
    opacity: 1;
    transform: translateY(0);
}
*/
