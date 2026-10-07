document.addEventListener('DOMContentLoaded', () => {
    
    // 1. Initialize Lenis for Buttery Smooth Scrolling
    const lenis = new Lenis({
        duration: 1.2,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // Apple-like easing
        direction: 'vertical',
        gestureDirection: 'vertical',
        smooth: true,
        mouseMultiplier: 1,
        smoothTouch: false, // leave native on mobile
        touchMultiplier: 2,
        infinite: false,
    });

    function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // 2. Register GSAP ScrollTrigger
    if (typeof gsap !== 'undefined') {
        gsap.registerPlugin(ScrollTrigger);

        // Update ScrollTrigger on Lenis scroll
        lenis.on('scroll', ScrollTrigger.update);

        gsap.ticker.add((time)=>{
          lenis.raf(time * 1000);
        });
        
        gsap.ticker.lagSmoothing(0, 0);

        // 3. Staggered Hero Entrance
        const heroTitle = document.querySelector('.hero-title-text');
        if (heroTitle) {
            gsap.from(".hero-title-text", { y: 50, opacity: 0, duration: 1, ease: "power4.out", delay: 0.2 });
            gsap.from(".hero-subtitle-text", { y: 30, opacity: 0, duration: 1, ease: "power4.out", delay: 0.4 });
            gsap.from(".hero-full-actions", { y: 30, opacity: 0, duration: 1, ease: "power4.out", delay: 0.6 });
        }

        // 4. Parallax Hero Image
        const heroSection = document.querySelector('.hero-full');
        if (heroSection) {
            gsap.to(heroSection, {
                backgroundPosition: "50% 100%",
                ease: "none",
                scrollTrigger: {
                    trigger: heroSection,
                    start: "top top",
                    end: "bottom top",
                    scrub: true
                }
            });
        }

        // 5. Scroll Reveals for all other elements
        gsap.utils.toArray('.reveal').forEach(element => {
            // Check if it's already animated by the hero sequence to avoid double animation
            if (!element.classList.contains('hero-title-text') && !element.classList.contains('hero-subtitle-text') && !element.classList.contains('hero-full-actions')) {
                gsap.fromTo(element, 
                    { y: 50, opacity: 0 },
                    {
                        y: 0,
                        opacity: 1,
                        duration: 1,
                        ease: "power3.out",
                        scrollTrigger: {
                            trigger: element,
                            start: "top 85%", // Trigger when element is 85% down the screen
                            toggleActions: "play none none reverse"
                        }
                    }
                );
            }
        });
        
        // 6. Stats Counter Animation (if stats exist)
        const statValues = document.querySelectorAll('.stat-value');
        if(statValues.length > 0) {
            statValues.forEach(stat => {
                let endValue = parseFloat(stat.innerText.replace(/[^0-9.]/g, ''));
                if(endValue) {
                    gsap.fromTo(stat, 
                        { innerHTML: 0 }, 
                        {
                            innerHTML: endValue,
                            duration: 2,
                            ease: "power2.out",
                            snap: { innerHTML: 1 },
                            scrollTrigger: {
                                trigger: stat,
                                start: "top 90%"
                            },
                            onUpdate: function() {
                                // Keep any symbols like + or % 
                                if(stat.innerText.includes('%')) stat.innerHTML = Math.round(this.targets()[0].innerHTML) + '%';
                                else if(stat.innerText.includes('+')) stat.innerHTML = Math.round(this.targets()[0].innerHTML) + '+';
                            }
                        }
                    );
                }
            });
        }
    }
});
