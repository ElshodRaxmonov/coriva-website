// Coriva public website: proposed motion layer (prototype). Runs after parse (defer).
// html.m-on was set in <head> only when IntersectionObserver exists; html.m-reduce when the visitor asks for reduced motion.
(() => {
  const root = document.documentElement;
  const on = root.classList.contains('m-on');
  const vh = () => window.innerHeight || 800;

  // ---------- Section reveals: once, below the fold only (content above the fold is never hidden) ----------
  const io = on ? new IntersectionObserver((entries) => {
    for (const e of entries) if (e.isIntersecting) { e.target.classList.add('is-in'); io.unobserve(e.target); }
  }, { threshold: 0.15 }) : null;
  const HEADING = (el) => /^H[1-3]$/.test(el.tagName) || el.matches('.sec-lead, .eyebrow-ink') || (el.tagName === 'P' && el.previousElementSibling && /^H2$/.test(el.previousElementSibling.tagName));
  const SKIP = '.card, form, .faq > div, details, [role=tablist], .orbit, .glimpse, .trace, .lens-panel, .state-panel, .preview';
  if (on) {
    const sections = [...document.querySelectorAll('main > section, main > div:not(.c-sheet), main > .c-sheet > section, main > .c-sheet > div:not(.sky)')].filter((s) => !s.matches('.hero, .pf-intro, .doc-hero'));
    for (const s of sections) {
      const box = s.querySelector(':scope > .wrap') || s;
      for (const child of box.children) {
        if (child.matches(SKIP) || child.querySelector('form')) continue;
        if (child.getBoundingClientRect().top < vh() * 0.92) continue;
        child.setAttribute('data-reveal', '');
        child.style.setProperty('--m-delay', HEADING(child) ? '0ms' : '120ms');
        io.observe(child);
      }
    }
    document.querySelectorAll('.orbit, .glimpse').forEach((el) => io.observe(el));
  }

  // ---------- Platform: a step is "reached" when it crosses 60% of the viewport ----------
  if ('IntersectionObserver' in window) {
    const reach = new IntersectionObserver((entries) => {
      for (const e of entries) if (e.isIntersecting) { e.target.classList.add('is-reached'); reach.unobserve(e.target); }
    }, { rootMargin: '0px 0px -40% 0px' });
    document.querySelectorAll('.station').forEach((s) => reach.observe(s));
  }

  // ---------- Replay helpers: restart a one-shot animation class ----------
  const replay = (el, cls) => { if (!el) return; el.classList.remove(cls); void el.offsetWidth; el.classList.add(cls); };

  // ---------- Home: the day draws when the lens is first seen and on every role change ----------
  const lens = document.getElementById('lens');
  if (on && lens) {
    const drawVisible = () => replay(lens.querySelector('.lens-panel:not([hidden]) .day'), 'm-draw');
    const first = new IntersectionObserver((entries) => {
      if (entries.some((e) => e.isIntersecting)) { drawVisible(); first.disconnect(); }
    }, { threshold: 0.25 });
    first.observe(lens.querySelector('.day') || lens);
    const mo = new MutationObserver((list) => {
      for (const m of list) if (!m.target.hidden) replay(m.target.querySelector('.day'), 'm-draw');
    });
    lens.querySelectorAll('.lens-panel').forEach((p) => mo.observe(p, { attributes: true, attributeFilter: ['hidden'] }));
  }

  // ---------- Waitlist and contact: the check draws when the Sent state is shown ----------
  if (on) {
    const mo = new MutationObserver((list) => {
      for (const m of list) if (!m.target.hidden) replay(m.target.querySelector('.sent'), 'm-play');
    });
    document.querySelectorAll('.state-panel').forEach((p) => mo.observe(p, { attributes: true, attributeFilter: ['hidden'] }));
  }

  // ---------- Shareable role links on the home page (#for-doctors ...) ----------
  document.querySelectorAll('[role=tablist][data-hashes]').forEach((list) => {
    const hashes = list.dataset.hashes.split(',');
    const tabs = [...list.querySelectorAll('[role=tab]')];
    const i = hashes.indexOf(location.hash.slice(1));
    if (i > 0) tabs[i].click();
    tabs.forEach((t, k) => t.addEventListener('click', () => { try { history.replaceState(null, '', '#' + hashes[k]); } catch (e) {} }));
    list.addEventListener('keydown', () => setTimeout(() => {
      const k = tabs.findIndex((t) => t.getAttribute('aria-selected') === 'true');
      if (k >= 0) try { history.replaceState(null, '', '#' + hashes[k]); } catch (e) {}
    }, 0));
  });

  // ---------- Header: hides while reading down, returns on scroll-up (UX brief §8) ----------
  const hdr = document.querySelector('.hdr');
  if (hdr) {
    // It hides only when the visitor scrolls down. Scroll magnetism can pull the page down a little right
    // after the visitor scrolls up (to a nearby section start); that movement is not theirs, so it must not
    // hide the header and its menu button again. `intent` is the direction of the visitor's last input.
    let last = window.scrollY, ticking = false, intent = 0, touchY = null;
    const menuOpen = () => hdr.querySelector('.menu-btn[aria-expanded="true"]');
    addEventListener('wheel', (e) => { if (e.deltaY) intent = Math.sign(e.deltaY); }, { passive: true });
    addEventListener('touchstart', (e) => { touchY = e.touches[0].clientY; }, { passive: true });
    addEventListener('touchmove', (e) => { const y = e.touches[0].clientY; if (touchY !== null && Math.abs(y - touchY) > 2) { intent = y < touchY ? 1 : -1; touchY = y; } }, { passive: true });
    addEventListener('keydown', (e) => {
      if (['ArrowDown', 'PageDown', 'End', ' '].includes(e.key)) intent = 1;
      else if (['ArrowUp', 'PageUp', 'Home'].includes(e.key)) intent = -1;
    });
    const update = () => {
      ticking = false;
      const y = window.scrollY;
      if (y < 120) { hdr.classList.remove('hdr-pinned', 'hdr-show'); }
      else {
        hdr.classList.add('hdr-pinned');
        if (y < last - 4 || menuOpen()) hdr.classList.add('hdr-show');
        else if (y > last + 4 && intent !== -1) hdr.classList.remove('hdr-show');
      }
      last = y;
    };
    window.addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
    hdr.addEventListener('focusin', () => hdr.classList.add('hdr-show'));
  }
})();
