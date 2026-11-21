// Round 8 (prototype), pages other than home: the intro headline rises word by word, with the heart mark as a chip.
// Runs before motion.js. The headline's accessible name is kept; nothing else is changed.
(() => {
  const h1 = document.querySelector('main h1');
  if (!h1 || h1.children.length) return;
  const text = h1.textContent.trim();
  h1.setAttribute('aria-label', text);
  h1.innerHTML = text.split(/\s+/).map((w, i) => `<span class="w" aria-hidden="true"><span style="--i:${i}">${w.replace(/&/g, '&amp;').replace(/</g, '&lt;')}</span></span>`).join(' ')
    + '<span class="r8-mark" aria-hidden="true"><img src="blob/00ef871558ec9b9f54c10a145d26dde5.png" alt=""></span>';
})();
