// Live layer: splash intro, flowing ribbon background, video control. Off when the visitor asks for reduced motion.
// Loaded synchronously at the end of <head>, so the preference is known before anything animates.
(() => {
  const root = document.documentElement;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;   // honoured as is: no override
  root.classList.toggle('rm', reduce);

  const ready = (fn) => (document.readyState === 'loading' ? document.addEventListener('DOMContentLoaded', fn) : fn());

  ready(() => {
    if (!reduce) { splash(); ribbons(); }
    videos();
    menu();
  });

  // ---------- Videos: play only while in view and only when motion is allowed; the button always works ----------
  function videos() {
    document.querySelectorAll('video[data-auto]').forEach((v) => {
      const btn = v.parentElement.querySelector('.vid-btn'); let userPaused = reduce;
      const sync = () => { if (btn) { btn.setAttribute('aria-pressed', String(v.paused)); btn.setAttribute('aria-label', v.paused ? 'Play video' : 'Pause video'); } };
      v.addEventListener('play', sync); v.addEventListener('pause', sync); sync();
      const rate = +v.dataset.rate || 1; v.defaultPlaybackRate = rate; v.playbackRate = rate;   // short clean clips play slowly
      if ('once' in v.dataset) v.addEventListener('ended', () => { userPaused = true; sync(); });   // holds its last frame; the button replays it
      if (btn) btn.addEventListener('click', () => { if (v.paused) { userPaused = false; v.play().catch(() => {}); } else { userPaused = true; v.pause(); } });
      if ('IntersectionObserver' in window) new IntersectionObserver(([e]) => { if (e.isIntersecting && !userPaused) v.play().catch(() => {}); else v.pause(); }, { threshold: 0.25 }).observe(v);
    });
  }

  // ---------- Splash: once per session, about two seconds, skippable; never with reduced motion ----------
  function splash() {
    let seen = false; try { seen = sessionStorage.getItem('coriva-splash') === '1'; sessionStorage.setItem('coriva-splash', '1'); } catch (e) {}
    const hold = /[?&]splash=hold/.test(location.search);   // review aid: keeps the splash on screen
    if ((seen && !hold) || location.hash.length > 1) return;
    root.classList.add('splash-on');
    const el = document.createElement('div'); el.className = 'splash'; el.setAttribute('aria-hidden', 'true');
    el.innerHTML = '<div class="splash-glow"></div><div class="splash-in"><img src="blob/00ef871558ec9b9f54c10a145d26dde5.png" alt="">'
      + '<p class="splash-name">' + 'Coriva'.split('').map((c, i) => `<span style="--i:${i}">${c}</span>`).join('') + '</p>'
      + '<p class="splash-tag">Every heartbeat matters.</p></div>';
    document.body.append(el);
    let done = false;
    const end = () => { if (done) return; done = true; el.classList.add('is-out'); root.classList.remove('splash-on'); setTimeout(() => el.remove(), 1100); };
    if (hold) return;
    setTimeout(end, 2300);
    ['pointerdown', 'keydown', 'wheel', 'touchstart'].forEach((t) => addEventListener(t, end, { once: true, passive: true }));
  }

  // ---------- Flowing ribbon: the logo's two strands as slow silk, drawn on a canvas behind dark sections ----------
  function ribbons() {
    const hosts = [...document.querySelectorAll('.s1, .calm, .pf-intro:not(.has-vid), .doc-hero, .join')   /* not under blurred glass (the bold scene's widgets): a moving layer there costs every frame */];
    if (!hosts.length || !('IntersectionObserver' in window)) return;
    const items = hosts.map((host) => {
      const c = document.createElement('canvas'); c.className = 'ribbon-cv'; c.setAttribute('aria-hidden', 'true');
      host.classList.add('has-ribbon'); host.prepend(c);
      return { host, c, ctx: c.getContext('2d'), on: false, w: 0, h: 0, seed: Math.random() * 10, pinned: host.matches('.s1, .pf-intro, .doc-hero') };
    });
    const size = (it) => { const r = it.c.getBoundingClientRect(); const d = Math.min(devicePixelRatio || 1, 1.25); it.w = r.width; it.h = r.height; it.c.width = Math.round(r.width * d); it.c.height = Math.round(r.height * d); it.ctx.setTransform(d, 0, 0, d, 0, 0); };
    const io = new IntersectionObserver((es) => es.forEach((e) => { const it = items.find((i) => i.host === e.target); it.on = e.isIntersecting; if (it.on) size(it); }), { rootMargin: '80px' });
    items.forEach((it) => io.observe(it.host));
    addEventListener('resize', () => items.forEach((it) => it.on && size(it)));
    const STR = [['20, 184, 166', 0.0], ['243, 111, 86', 1.7]];
    const draw = (it, t) => {
      const { ctx, w, h } = it; if (!w || !h) return;
      ctx.clearRect(0, 0, w, h);
      const base = it.host.classList.contains('s1') ? 0.55 : 0.5, amp = Math.min(h * 0.16, 120);
      for (const [rgb, ph] of STR) {
        for (let k = 0; k < 9; k++) {               // nine fine lines per strand read as one silk ribbon
          const o = k / 8, a = 0.10 + 0.42 * Math.sin(o * Math.PI);
          ctx.beginPath();
          for (let x = -20; x <= w + 20; x += 24) {
            const u = x / w;
            const y = h * base + Math.sin(u * 4.2 + t * 0.32 + ph + it.seed) * amp * (0.55 + 0.45 * Math.sin(u * 2.1 + t * 0.21 + ph))
              + Math.sin(u * 9 - t * 0.5 + ph * 2 + o * 1.6) * amp * 0.16 + (o - 0.5) * amp * 0.9 * Math.cos(u * 3.1 + t * 0.27 + ph);
            x === -20 ? ctx.moveTo(x, y) : ctx.lineTo(x, y);
          }
          ctx.strokeStyle = `rgba(${rgb}, ${a})`; ctx.lineWidth = 1.6; ctx.stroke();
        }
      }
    };
    let last = 0;
    const loop = (now) => {
      requestAnimationFrame(loop);
      if (document.hidden || now - last < 33) return;   // about 30 frames a second is plenty for slow silk
      last = now; const t = now / 1000;
      // A pinned intro stays "in view" behind the sheet for the whole page: stop drawing once the sheet has covered it
      for (const it of items) if (it.on && !(it.pinned && scrollY > it.host.offsetHeight)) draw(it, t);
    };
    requestAnimationFrame(loop);
  }
  // ---------- Mobile menu: a circle that opens from the button and fills the screen ----------
  // Takes over from the small toggle each page carries inline (the button is cloned to drop its listener).
  // The panel moves to <body> so no transformed or blurred header can clip it.
  function menu() {
    const old = document.querySelector('.hdr .menu-btn'), panel = document.querySelector('.menu-panel');
    if (!old || !panel) return;
    const T = (x) => (window.__CORIVA_T || {})[x] || x;   // run-time strings on translated pages
    const btn = old.cloneNode(true); old.replaceWith(btn);
    panel.classList.add('mnav'); panel.hidden = true; document.body.append(panel);
    const list = panel.querySelector('ul');
    const here = location.pathname.replace(/\.html$/, '').replace(/\/index$/, '/') || '/';
    [...list.children].forEach((li, i) => {
      li.style.setProperty('--i', i);
      const a = li.querySelector('a');
      if (!a) return;
      if (a.hasAttribute('lang')) {
        li.classList.add('mnav-lang');
        // Pages that still switch language in the browser (i18n.js): follow the header's working switch
        const head = document.querySelector('.hdr a.lang-inline');
        if (a.getAttribute('href') === '#' && head) { a.textContent = head.textContent; a.lang = head.lang; a.addEventListener('click', (e) => { e.preventDefault(); head.click(); }); }
        return;
      }
      const path = new URL(a.getAttribute('href'), location.href).pathname.replace(/\.html$/, '') || '/';
      if (path === here) a.setAttribute('aria-current', 'page');
    });
    // Group the language links (one or more) on a single row
    const langs = [...list.querySelectorAll('.mnav-lang')];
    if (langs.length > 1) { const row = langs[0]; langs.slice(1).forEach((li) => { row.append(...li.childNodes); li.remove(); }); }
    const cta = document.querySelector('.hdr .hdr-cta');
    if (cta) {
      const c = document.createElement('a'); c.className = 'mnav-cta'; c.href = cta.getAttribute('href');
      c.textContent = (cta.querySelector('.lbl-full') || cta).textContent.trim();
      c.style.setProperty('--i', list.children.length); panel.querySelector('nav').append(c);
    }
    // Everything except the header's own branch and the menu: made inert while the menu is open
    const outside = () => {
      const out = [];
      for (let n = btn.closest('header'); n && n !== document.body; n = n.parentElement)
        for (const sib of n.parentElement.children) if (sib !== n && sib !== panel && !sib.matches('script, style, link')) out.push(sib);
      return out;
    };
    let closing = 0, lastFocus = null;
    const set = (open) => {
      const r = btn.getBoundingClientRect(), x = r.left + r.width / 2, y = r.top + r.height / 2;
      panel.style.setProperty('--mx', x + 'px'); panel.style.setProperty('--my', y + 'px');
      panel.style.setProperty('--mr', Math.ceil(Math.hypot(Math.max(x, innerWidth - x), Math.max(y, innerHeight - y))) + 'px');
      btn.setAttribute('aria-expanded', String(open)); btn.setAttribute('aria-label', open ? T('Close menu') : btn.dataset.openLabel);
      document.documentElement.classList.toggle('mnav-on', open);
      outside().forEach((el) => { el.inert = open; });
      clearTimeout(closing);
      if (open) {
        lastFocus = document.activeElement; panel.hidden = false;
        requestAnimationFrame(() => requestAnimationFrame(() => panel.classList.add('is-open')));
        setTimeout(() => { const f = panel.querySelector('a'); if (f && btn.getAttribute('aria-expanded') === 'true') f.focus({ preventScroll: true }); }, reduce ? 0 : 280);
      } else {
        panel.classList.remove('is-open');
        closing = setTimeout(() => { panel.hidden = true; }, reduce ? 0 : 520);
        if (panel.contains(document.activeElement)) btn.focus({ preventScroll: true });
      }
    };
    btn.dataset.openLabel = btn.getAttribute('aria-label') || 'Menu';
    btn.addEventListener('click', () => set(btn.getAttribute('aria-expanded') !== 'true'));
    panel.addEventListener('click', (e) => { if (e.target.closest('a')) set(false); });
    document.addEventListener('keydown', (e) => {
      if (btn.getAttribute('aria-expanded') !== 'true') return;
      if (e.key === 'Escape') { set(false); btn.focus(); return; }
      if (e.key !== 'Tab') return;
      // Keep focus between the button and the menu while it is open
      const items = [btn, ...panel.querySelectorAll('a')], i = items.indexOf(document.activeElement);
      e.preventDefault();
      items[(i + (e.shiftKey ? -1 : 1) + items.length) % items.length].focus();
    });
    // Wider than the burger breakpoint: the menu has no button, so it must not stay open
    addEventListener('resize', () => { if (btn.getAttribute('aria-expanded') === 'true' && getComputedStyle(btn).display === 'none') set(false); });
  }
})();
