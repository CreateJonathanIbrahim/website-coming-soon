/*!
 * Start Bootstrap - Grayscale v7.0.6 (https://startbootstrap.com/theme/grayscale)
 * Copyright 2013-2023 Start Bootstrap
 * Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
 */
//
// Scripts
//

window.addEventListener('DOMContentLoaded', event => {
    const mainNav = document.body.querySelector('#mainNav');

    // --- 1. Custom Navbar Fade-In Logic ---
    if (mainNav) {
        const revealNav = () => {
            mainNav.classList.add('nav-is-visible');
        };

        // If user refreshes the page and is already scrolled past the 50px buffer
        if (window.scrollY > 50) {
            revealNav();
        } else {
            // Otherwise, wait 2 seconds
            let navTimeout = setTimeout(revealNav, 2000);

            // If user scrolls past 50px before the 2 seconds are up, reveal immediately
            document.addEventListener('scroll', function scrollReveal() {
                if (window.scrollY > 50 && !mainNav.classList.contains('nav-is-visible')) {
                    clearTimeout(navTimeout);
                    revealNav();
                    document.removeEventListener('scroll', scrollReveal);
                }
            });
        }
    }

    // --- 2. Theme Native Navbar Shrink Logic ---
    var navbarShrink = function () {
        if (!mainNav) {
            return;
        }
        // Added 50px buffer so it doesn't shrink on tiny layout shifts
        if (window.scrollY < 50) {
            mainNav.classList.remove('navbar-shrink');
        } else {
            mainNav.classList.add('navbar-shrink');
        }
    };

    // Shrink the navbar
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // --- 3. Theme Native ScrollSpy ---
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    }

    // --- 4. Theme Native Mobile Menu Collapse ---
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link'),
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
            }
        });
    });
});
