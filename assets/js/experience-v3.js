(() => {
  const reduced = matchMedia('(prefers-reduced-motion: reduce)');
  document.addEventListener('pointerdown', event => {
    const control = event.target.closest('button,a');
    if (!control || reduced.matches) return;
    control.classList.add('v3-pressed');
    const clear = () => control.classList.remove('v3-pressed');
    window.addEventListener('pointerup', clear, {once:true});
    window.addEventListener('pointercancel', clear, {once:true});
    setTimeout(clear,500);
  }, {passive:true});
  const observer = new IntersectionObserver(entries => entries.forEach(entry => {
    entry.target.classList.toggle('v3-floral-visible', entry.isIntersecting && !reduced.matches);
  }), {threshold:.05});
  const seen = new WeakSet();
  const attach = () => document.querySelectorAll('#main [data-section]').forEach(section => {
    if (!seen.has(section)) {seen.add(section);observer.observe(section);}
  });
  new MutationObserver(attach).observe(document.querySelector('#app'),{childList:true,subtree:true});
  attach();
})();
