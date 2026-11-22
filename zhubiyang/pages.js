const supported = ['ko', 'en', 'ja', 'zh', 'vi'];
let lang;
try { lang = localStorage.getItem('zhubiyang-language'); } catch {}
if (!supported.includes(lang)) {
  lang = (navigator.languages || [navigator.language]).map(l => l.split('-')[0]).find(l => supported.includes(l)) || 'en';
}

let pageData = null, poses = [], filter = 'all', selected = null;
const $ = s => document.querySelector(s);
const t = key => (pageData && pageData.ui && pageData.ui[key] && pageData.ui[key][lang]) ? pageData.ui[key][lang] : (key || '');
const name = p => (p && p.title && p.title[lang]) ? p.title[lang] : '';

function apply() {
  if (!pageData) return;
  document.documentElement.lang = lang === 'zh' ? 'zh-CN' : lang;
  if ($('#language')) {
    $('#language').value = lang;
    if (copy && copy[lang] && copy[lang].languageLabel) $('#language').setAttribute('aria-label', copy[lang].languageLabel);
  }
  if (copy && copy[lang]) {
    document.querySelectorAll('[data-t]').forEach(e => {
      if (copy[lang][e.dataset.t]) e.innerHTML = copy[lang][e.dataset.t];
    });
  }
  document.querySelectorAll('[data-extra]').forEach(e => {
    e.textContent = t(e.dataset.extra);
  });
  const pageTitleKey = document.body.dataset.page === 'poses' ? 'posesTitle' : 'storyTitle';
  document.title = 'ZHUBIYANG · ' + t(pageTitleKey);
  if ($('#pose-close') && copy && copy[lang] && copy[lang].closeLabel) {
    $('#pose-close').setAttribute('aria-label', copy[lang].closeLabel);
  }
  if (document.body.dataset.page === 'poses') renderPoses();
  else renderStory();
  if (selected) {
    if ($('#pose-caption')) $('#pose-caption').textContent = name(selected);
    if ($('#pose-large')) $('#pose-large').alt = name(selected);
  }
}

function renderPoses() {
  if (!pageData) return;
  if ($('#pose-filters')) {
    $('#pose-filters').replaceChildren(...['all', 'daily', 'motion', 'mood', 'friends'].map(c => {
      const b = document.createElement('button');
      b.textContent = t(c);
      b.className = filter === c ? 'active' : '';
      b.setAttribute('aria-pressed', String(filter === c));
      b.onclick = () => { filter = c; renderPoses(); };
      return b;
    }));
  }
  const list = poses.filter(p => filter === 'all' || p.category === filter);
  if ($('#pose-count')) $('#pose-count').textContent = list.length + ' / ' + poses.length + ' — ' + t('zoom');
  if ($('#pose-grid')) {
    $('#pose-grid').replaceChildren(...list.map((p, i) => {
      const b = document.createElement('button');
      b.className = 'pose-tile';
      const im = new Image();
      im.src = p.image;
      im.alt = name(p);
      im.loading = 'lazy';
      const cap = document.createElement('span');
      cap.textContent = name(p);
      b.append(im, cap);
      b.onclick = () => {
        selected = p;
        if ($('#pose-large')) { $('#pose-large').src = p.image; $('#pose-large').alt = name(p); }
        if ($('#pose-caption')) $('#pose-caption').textContent = name(p);
        if ($('#pose-viewer') && typeof $('#pose-viewer').showModal === 'function') $('#pose-viewer').showModal();
      };
      return b;
    }));
  }
}

function renderStory() {
  if (!pageData) return;
  renderBrand();
  if ($('#story-chapters') && pageData.stories) {
    $('#story-chapters').replaceChildren(...pageData.stories.map((s, i) => {
      const article = document.createElement('article');
      article.className = 'story-chapter';
      const art = document.createElement('div');
      art.className = 'chapter-art';
      const im = new Image();
      im.src = s.image;
      im.alt = s.title[lang];
      im.loading = 'lazy';
      art.append(im);
      const text = document.createElement('div');
      text.className = 'chapter-copy';
      const num = document.createElement('span');
      num.className = 'chapter-number';
      num.textContent = String(i + 1).padStart(2, '0');
      const h = document.createElement('h2');
      h.textContent = s.title[lang];
      const p = document.createElement('p');
      p.textContent = s.body[lang];
      text.append(num, h, p);
      article.append(art, text);
      return article;
    }));
  }
}

function renderBrand() {
  if (!pageData || !pageData.brand) return;
  const b = pageData.brand;
  const section = $('#brand-concept');
  if (!section) return;
  section.replaceChildren();
  const eyebrow = document.createElement('span');
  eyebrow.className = 'eyebrow';
  eyebrow.textContent = 'BRAND CONCEPT';
  const h = document.createElement('h2');
  h.textContent = b.title[lang];
  const intro = document.createElement('p');
  intro.textContent = b.intro[lang];
  const names = document.createElement('div');
  names.className = 'brand-syllables';
  for (const s of b.syllables) {
    const cell = document.createElement('div');
    const word = document.createElement('strong');
    word.textContent = s.word;
    const meaning = document.createElement('span');
    meaning.textContent = s.meaning[lang];
    cell.append(word, meaning);
    names.append(cell);
  }
  const points = document.createElement('div');
  points.className = 'brand-points';
  for (const p of b.points) {
    const a = document.createElement('article');
    const title = document.createElement('h3');
    const body = document.createElement('p');
    title.textContent = p.title[lang];
    body.textContent = p.body[lang];
    a.append(title, body);
    points.append(a);
  }
  section.append(eyebrow, h, names, intro, points);
}

if ($('#language')) {
  $('#language').onchange = () => {
    lang = $('#language').value;
    try { localStorage.setItem('zhubiyang-language', lang); } catch {}
    apply();
  };
}

if ($('#pose-close')) {
  $('#pose-close').onclick = () => { if ($('#pose-viewer')) $('#pose-viewer').close(); };
}
if ($('#pose-viewer')) {
  $('#pose-viewer').addEventListener('click', e => {
    if (e.target === $('#pose-viewer')) {
      const r = e.target.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) e.target.close();
    }
  });
}

Promise.all([
  fetch('pages-data.json').then(r => { if (!r.ok) throw Error(); return r.json(); }),
  fetch('poses.json').then(r => { if (!r.ok) throw Error(); return r.json(); })
]).then(([d, p]) => {
  pageData = d;
  poses = p;
  apply();
}).catch(() => {
  const pIntro = document.querySelector('.page-intro p');
  if (pIntro && copy && copy[lang] && copy[lang].loadFail) {
    pIntro.textContent = copy[lang].loadFail;
  }
});
