// Round 6 effects (prototype only). Runs after parse (defer), before motion.js.
// Features are listed in <html data-fx="..."> (fallback: by data-dir). Every effect is decorative:
// content is complete without it; it is off with reduced motion, and pointer effects need a fine pointer.
(() => {
  const root = document.documentElement;
  const dir = root.dataset.dir;
  const FX = new Set((root.dataset.fx || (dir === 'a' ? 'tilt nosign' : dir === 'b' ? 'split ribbon spotlight magnetic underline' : dir === 'c' ? 'tipcards' : '')).split(/\s+/).filter(Boolean));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = matchMedia('(hover: hover) and (pointer: fine)').matches;
  const live = !reduce && 'IntersectionObserver' in window;
  const once = (els, cls, opts = {}, stagger = 0) => {
    if (!live) { els.forEach((e) => e.classList.add(cls)); return; }
    const io = new IntersectionObserver((entries) => entries.forEach((e) => {
      if (!e.isIntersecting) return;
      const i = els.indexOf(e.target);
      setTimeout(() => e.target.classList.add(cls), i * stagger);
      io.unobserve(e.target);
    }), { threshold: 0.6, ...opts });
    els.forEach((e) => io.observe(e));
  };
  const track = (els, fn, reset) => {
    if (!fine || reduce) return;
    els.forEach((el) => {
      let raf = 0;
      el.addEventListener('pointermove', (ev) => {
        cancelAnimationFrame(raf);
        raf = requestAnimationFrame(() => { const b = el.getBoundingClientRect(); fn(el, (ev.clientX - b.left) / b.width, (ev.clientY - b.top) / b.height); });
      });
      el.addEventListener('pointerleave', () => { cancelAnimationFrame(raf); reset(el); });
    });
  };
  const CARDS = '.moment, section[aria-labelledby="today-i3"] > div > div';

  if (FX.has('tilt')) {
    track([...document.querySelectorAll(CARDS)], (el, x, y) => { el.style.setProperty('--ry', `${(x - 0.5) * 5}deg`); el.style.setProperty('--rx', `${(0.5 - y) * 4}deg`); },
      (el) => { el.style.setProperty('--ry', '0deg'); el.style.setProperty('--rx', '0deg'); });
  }
  if (FX.has('nosign')) {
    const lines = [...document.querySelectorAll('section[aria-labelledby="never-i3"] li')];
    lines.forEach((li) => li.insertAdjacentHTML('afterbegin', '<svg class="a-no" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="10"/><path d="M5 19 19 5"/></svg>'));
    once(lines, 'is-struck', { threshold: 0.9 }, 90);
  }
  if (FX.has('split')) {
    const h1 = document.querySelector('.hero-title');
    if (h1 && !reduce) {
      const words = h1.textContent.trim().split(/\s+/);
      h1.setAttribute('aria-label', h1.textContent.trim());
      h1.innerHTML = words.map((w, i) => `<span class="w" aria-hidden="true"><span style="--i:${i}">${w}</span></span>`).join(' ');
    }
  }
  if (FX.has('ribbon')) {
    const hero = document.querySelector('.hero');
    if (hero) hero.insertAdjacentHTML('beforeend', `<svg class="b-ribbon" viewBox="0 0 1440 400" preserveAspectRatio="none" aria-hidden="true" focusable="false">
      <path class="glow t" d="M-40 330 C 220 250, 380 380, 640 300 S 1040 150, 1480 250"/>
      <path class="glow c" d="M-40 350 C 240 290, 420 400, 680 320 S 1080 190, 1480 280"/>
      <path class="t" d="M-40 330 C 220 250, 380 380, 640 300 S 1040 150, 1480 250"/>
      <path class="c" d="M-40 350 C 240 290, 420 400, 680 320 S 1080 190, 1480 280"/></svg>`);
  }
  if (FX.has('spotlight')) {
    const glass = [...document.querySelectorAll(`${CARDS}, #join > div, .faq`)];
    glass.forEach((g) => g.classList.add('b-glass'));
    track(glass, (el, x, y) => { el.style.setProperty('--mx', `${x * 100}%`); el.style.setProperty('--my', `${y * 100}%`); el.classList.add('is-lit'); },
      (el) => el.classList.remove('is-lit'));
  }
  if (FX.has('magnetic')) {
    track([...document.querySelectorAll('.btn-coral')], (el, x, y) => { el.style.transform = `translate(${(x - 0.5) * 8}px, ${(y - 0.5) * 6}px)`; },
      (el) => { el.style.transform = ''; });
  }
  if (FX.has('underline')) once([...document.querySelectorAll('main h2')], 'is-drawn', { threshold: 0.8 });
  if (FX.has('tipcards')) once([...document.querySelectorAll('section[aria-labelledby="today-i3"] > div > div')], 'is-up', { threshold: 0.3 }, 110);

  // Sheen: a light reflection that follows a fine pointer across glass (custom properties only)
  if (FX.has('sheen')) {
    const els = [...document.querySelectorAll(`.lg, ${CARDS}, .hero-inner > div:last-child, .faq, .btn-glass`)];
    els.forEach((e) => e.classList.add('lg'));
    track(els, (el, x, y) => { el.style.setProperty('--sx', `${x * 100}%`); el.style.setProperty('--sy', `${y * 100}%`); el.classList.add('is-lit'); }, (el) => el.classList.remove('is-lit'));
  }

  // refract: Chromium can use an SVG filter as a backdrop filter; elsewhere the CSS keeps plain frosted glass
  if (FX.has('refract') && !matchMedia('(prefers-reduced-transparency: reduce)').matches) {
    const chromium = (navigator.userAgentData && navigator.userAgentData.brands || []).some((b) => /Chromium/.test(b.brand));
    if (chromium && document.getElementById('lg-refract')) root.classList.add('lg-refract');
  }

  // Liquid lens: one glass blob slides between the role tabs and stretches while it moves
  if (FX.has('lens')) {
    document.querySelectorAll('.role-tabs').forEach((group) => {
      const pills = [...group.querySelectorAll('.role-tab')];
      let pointerAt = 0; group.addEventListener('pointerdown', () => { pointerAt = performance.now(); });
      if (!pills.length) return;
      group.classList.add('has-blob');
      const blob = document.createElement('span'); blob.className = 'lens-blob'; blob.setAttribute('aria-hidden', 'true');
      group.prepend(blob);
      let cur = null;
      const place = (animate) => {
        const sel = pills.find((p) => p.getAttribute('aria-selected') === 'true') || pills[0];
        // Layout offsets, not client rects: the card may be mid-flight (transformed) when this runs
        const to = { x: sel.offsetLeft, y: sel.offsetTop, w: sel.offsetWidth, h: sel.offsetHeight };
        blob.style.width = `${to.w}px`; blob.style.height = `${to.h}px`;
        // Keyboard changes jump: nothing triggered by the keyboard animates (DESIGN_SYSTEM §8).
        if (animate && cur && !reduce && performance.now() - pointerAt < 800 && (cur.x !== to.x || cur.y !== to.y)) {
          const dx = to.x - cur.x, dy = to.y - cur.y, stretch = 1 + Math.min(Math.abs(dx) / to.w, 1.2) * 0.35;
          blob.animate([
            { transform: `translate(${cur.x}px, ${cur.y}px) scale(${cur.w / to.w}, ${cur.h / to.h})` },
            { transform: `translate(${cur.x + dx * 0.55}px, ${cur.y + dy * 0.55}px) scale(${stretch}, ${1 / Math.sqrt(stretch)})`, offset: 0.45 },
            { transform: `translate(${to.x}px, ${to.y}px) scale(1, 1)` },
          ], { duration: 520, easing: 'cubic-bezier(0.23, 1, 0.32, 1)' });
        }
        blob.style.transform = `translate(${to.x}px, ${to.y}px)`;
        cur = to;
      };
      place(false);
      new MutationObserver(() => place(true)).observe(group, { attributes: true, subtree: true, attributeFilter: ['aria-selected'] });
      addEventListener('resize', () => place(false));
      document.fonts && document.fonts.ready.then(() => place(false));
    });
  }
})();
