// Round 7 (prototype): the header becomes a glass capsule once the page is scrolled. Everything else is CSS.
(() => {
  const hdr = document.querySelector('.hdr');
  if (!hdr) return;
  let raf = 0;
  const update = () => { raf = 0; hdr.classList.toggle('is-scrolled', scrollY > 24); };
  addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(update); }, { passive: true });
  update();

  // Carousel for each role's day: previous / next buttons and position dots; the strip keeps native swipe
  document.querySelectorAll('.s2-right .day').forEach((day) => {
    const tiles = [...day.children]; if (tiles.length < 2) return;
    const car = document.createElement('div'); car.className = 'car';
    const arrow = (d) => `<svg viewBox="0 0 24 24" aria-hidden="true"><path d="${d}"/></svg>`;
    car.innerHTML = `<button type="button" aria-label="Previous moment">${arrow('M15 5l-7 7 7 7')}</button><button type="button" aria-label="Next moment">${arrow('M9 5l7 7-7 7')}</button><span class="car-dots" aria-hidden="true">${tiles.map(() => '<i></i>').join('')}</span>`;
    day.after(car);
    const [prev, next] = car.querySelectorAll('button'); const dots = [...car.querySelectorAll('i')];
    const stepW = () => tiles[1].offsetLeft - tiles[0].offsetLeft;
    const sync = () => {
      const max = day.scrollWidth - day.clientWidth, x = day.scrollLeft;
      const i = Math.min(tiles.length - 1, x >= max - 2 ? tiles.length - 1 : Math.round(x / stepW()));
      dots.forEach((d, k) => d.classList.toggle('on', k === i));
      prev.disabled = x <= 2; next.disabled = x >= max - 2;
    };
    prev.addEventListener('click', () => day.scrollBy({ left: -stepW() }));
    next.addEventListener('click', () => day.scrollBy({ left: stepW() }));
    let raf2 = 0; day.addEventListener('scroll', () => { if (!raf2) raf2 = requestAnimationFrame(() => { raf2 = 0; sync(); }); }, { passive: true });
    new MutationObserver(sync).observe(day.closest('.lens-panel'), { attributes: true, attributeFilter: ['hidden'] });
    addEventListener('resize', sync); sync();
  });
})();
