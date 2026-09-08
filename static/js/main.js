/**
 * Krupa Elevator Corporate Website Main Script
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. Sticky Navbar on Scroll
  const mainNavbar = document.querySelector('.main-navbar');
  const backToTopBtn = document.getElementById('backToTopBtn');

  const handleScroll = () => {
    const scrollY = window.scrollY || window.pageYOffset;

    // Navbar style toggle
    if (mainNavbar) {
      if (scrollY > 60) {
        mainNavbar.classList.add('scrolled');
      } else {
        mainNavbar.classList.remove('scrolled');
      }
    }

    // Back to top visibility
    if (backToTopBtn) {
      if (scrollY > 300) {
        backToTopBtn.classList.add('show');
      } else {
        backToTopBtn.classList.remove('show');
      }
    }
  };

  window.addEventListener('scroll', handleScroll);
  handleScroll(); // Initial check

  // 2. Back to top action
  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', (e) => {
      e.preventDefault();
      window.scrollTo({
        top: 0,
        behavior: 'smooth',
      });
    });
  }

  // 3. Animated Statistics Counters
  const statNumbers = document.querySelectorAll('.stat-number[data-target]');
  let counted = false;

  const countUp = () => {
    statNumbers.forEach((counter) => {
      const target = parseFloat(counter.getAttribute('data-target').replace(/,/g, ''));
      const duration = 1800; // ms
      const startTime = performance.now();

      const updateCount = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Easing out cubic
        const easeOut = 1 - Math.pow(1 - progress, 3);
        const currentVal = Math.floor(easeOut * target);

        counter.innerText = currentVal.toLocaleString();

        if (progress < 1) {
          requestAnimationFrame(updateCount);
        } else {
          counter.innerText = target.toLocaleString();
        }
      };

      requestAnimationFrame(updateCount);
    });
  };

  const statsSection = document.querySelector('.stats-section');
  if (statsSection && statNumbers.length > 0) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting && !counted) {
            counted = true;
            countUp();
          }
        });
      },
      { threshold: 0.25 }
    );
    observer.observe(statsSection);
  }

  // 4. Smooth Anchor Link Scrolling
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId.length > 1 && document.querySelector(targetId)) {
        e.preventDefault();
        const targetElement = document.querySelector(targetId);
        const offset = 90; // offset for sticky navbar
        const bodyRect = document.body.getBoundingClientRect().top;
        const elementRect = targetElement.getBoundingClientRect().top;
        const elementPosition = elementRect - bodyRect;
        const offsetPosition = elementPosition - offset;

        window.scrollTo({
          top: offsetPosition,
          behavior: 'smooth',
        });
      }
    });
  });

  // 5. Subtle Scroll Reveal Animations
  const revealElements = document.querySelectorAll('.reveal-on-scroll');
  if ('IntersectionObserver' in window && revealElements.length > 0) {
    const revealObserver = new IntersectionObserver(
      (entries, observer) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add('is-revealed');
            observer.unobserve(entry.target);
          }
        });
      },
      {
        threshold: 0.1,
        rootMargin: '0px 0px -40px 0px',
      }
    );

    revealElements.forEach((el) => {
      revealObserver.observe(el);
    });
  } else {
    revealElements.forEach((el) => el.classList.add('is-revealed'));
  }

  // 6. Direct click navigation for desktop navbar dropdown toggles
  const desktopDropdownToggle = document.getElementById('navbarProductsDropdown');
  if (desktopDropdownToggle) {
    desktopDropdownToggle.addEventListener('click', (e) => {
      if (window.innerWidth >= 1200) {
        const targetHref = desktopDropdownToggle.getAttribute('href');
        if (targetHref && targetHref !== '#') {
          window.location.href = targetHref;
        }
      }
    });
  }
});
