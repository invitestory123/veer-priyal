/* Renders the per-function event cards, the "from" card and the closing message
   for this invitation. Data comes from window.INVITE_EXTRA (set in each page's config). */
(() => {
  const X = window.INVITE_EXTRA;
  if (!X) return;
  const B = X.base || './';
  const esc = s => String(s).replace(/[&<>"]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
  const lines = s => esc(s).replace(/\n/g, '<br>');
  const pin = '<svg viewBox="0 0 24 24" width="13" height="13" aria-hidden="true" fill="currentColor"><path d="M12 2a7 7 0 0 0-7 7c0 5.25 7 13 7 13s7-7.75 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6.5a2.5 2.5 0 0 1 0 5z"></path></svg>';

  const eventCard = ev => `
    <article class="fn-event${ev.navy ? ' fn-navy' : ''}">
      ${ev.icon ? `<img class="fn-icon" src="${B}assets/images/${ev.icon}" alt="" aria-hidden="true">` : ''}
      ${ev.invocation ? `<p class="fn-invocation">${lines(ev.invocation)}</p>` : ''}
      ${ev.intro ? `<p class="fn-intro">${lines(ev.intro)}</p>` : ''}
      <h3 class="fn-title ${ev.font || 'font-pinyon'}">${esc(ev.title)}</h3>
      ${ev.subtitle ? `<p class="fn-subtitle">${lines(ev.subtitle)}</p>` : ''}
      <img class="fn-orn" src="${B}assets/images/ornaments.webp" alt="" aria-hidden="true">
      <p class="fn-date">${esc(ev.date)}</p>
      <dl class="fn-times">${ev.times.map(t => `<div><dt>${esc(t[0])}</dt><dd>${esc(t[1])}</dd></div>`).join('')}</dl>
      ${ev.note ? `<p class="fn-note">${lines(ev.note)}</p>` : ''}
      ${ev.venues.map(v => `
        <div class="fn-venue">
          ${v.label ? `<p class="fn-venue-label">${esc(v.label)}</p>` : ''}
          <p class="fn-venue-name">${esc(v.name)}</p>
          ${v.address ? `<p class="fn-venue-addr">${lines(v.address)}</p>` : ''}
          ${v.map ? `<a class="fn-map t054-shimmer" href="${esc(v.map)}" target="_blank" rel="noopener noreferrer">${pin}View location</a>` : ''}
        </div>`).join('')}
      ${ev.details && ev.details.length ? `<ul class="fn-details">${ev.details.map(d => `<li>${esc(d)}</li>`).join('')}</ul>` : ''}
      ${ev.compliments ? `<div class="fn-compliments"><p class="fn-venue-label">With best compliments from</p><p>${lines(ev.compliments)}</p></div>` : ''}
    </article>`;

  const build = () => {
    const sections = [];
    sections.push(`
      <section data-custom="events" class="t054-card fn-section mx-auto w-full max-w-5xl px-5 pb-10 pt-10 sm:px-10 sm:py-14">
        <h2 class="fn-heading font-pinyon text-t054-script">${esc(X.eventsHeading)}</h2>
        <div class="fn-list">${X.events.map(eventCard).join('')}</div>
      </section>`);
    if (X.from) sections.push(`
      <section data-custom="from" class="t054-card fn-section mx-auto w-full max-w-5xl px-5 pb-10 pt-10 sm:px-10 sm:py-14">
        <p class="fn-venue-label">${esc(X.from.label)}</p>
        <p class="fn-from-name font-pinyon text-t054-script">${esc(X.from.name)}</p>
        ${X.from.address ? `<p class="fn-venue-addr">${lines(X.from.address)}</p>` : ''}
      </section>`);
    if (X.closing) sections.push(`
      <section data-custom="message" class="t054-card fn-section mx-auto w-full max-w-5xl px-5 pb-10 pt-10 sm:px-10 sm:py-14">
        <img class="fn-orn fn-orn-lg" src="${B}assets/images/ornaments.webp" alt="" aria-hidden="true">
        ${X.closing.paragraphs.map(p => `<p class="fn-closing">${lines(p)}</p>`).join('')}
        <p class="fn-sign-label">${esc(X.closing.signLabel)}</p>
        <p class="fn-sign font-pinyon text-t054-script">${esc(X.closing.sign)}</p>
      </section>`);
    return sections;
  };

  const inject = () => {
    const main = document.querySelector('#main');
    if (!main || main.querySelector('[data-custom]')) return;
    const anchor = main.querySelector('[data-section="countdown"]') || main.querySelector('[data-section="invitation"]');
    const closing = main.querySelector('[data-section="closing"]');
    if (!anchor || !closing) return;
    const [events, from, message] = build().map(html => {
      const t = document.createElement('template');
      t.innerHTML = html.trim();
      return t.content.firstElementChild;
    });
    anchor.after(events);
    if (from) closing.before(from);
    if (message) closing.before(message);
    const io = new IntersectionObserver(entries => entries.forEach(e => {
      if (e.isIntersecting) { e.target.classList.add('fn-in'); io.unobserve(e.target); }
    }), {threshold: .08});
    main.querySelectorAll('[data-custom], .fn-event').forEach(el => io.observe(el));
  };

  new MutationObserver(inject).observe(document.querySelector('#app'), {childList: true, subtree: true});
  inject();
})();
