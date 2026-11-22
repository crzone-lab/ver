const initialCatalog = {"products":[{"name":"Apron","cat":"fashion","img":"assets/product-00.webp","names":{"ko":"앞치마","en":"Apron","ja":"エプロン","zh":"围裙","vi":"Tạp dề"},"id":"products-0"},{"name":"BAG","cat":"fashion","img":"assets/product-01.webp","names":{"ko":"가방","en":"Bag","ja":"バッグ","zh":"手提包","vi":"Túi xách"},"id":"products-1"},{"name":"CANDY","cat":"fashion","img":"assets/product-02.webp","names":{"ko":"캔디","en":"Candy","ja":"キャンディ","zh":"糖果","vi":"Kẹo"},"id":"products-2"},{"name":"Cushion","cat":"toy","img":"assets/product-03.webp","names":{"ko":"쿠션","en":"Cushion","ja":"クッション","zh":"抱枕","vi":"Gối tựa"},"id":"products-3"},{"name":"Diary (2)","cat":"paper","img":"assets/product-04.webp","names":{"ko":"다이어리 02","en":"Diary 02","ja":"手帳 02","zh":"手账本 02","vi":"Sổ tay 02"},"id":"products-4"},{"name":"Earphone case02","cat":"digital","img":"assets/product-05.webp","names":{"ko":"이어폰 케이스 02","en":"Earbud case 02","ja":"イヤホンケース 02","zh":"耳机保护套 02","vi":"Ốp tai nghe 02"},"id":"products-5"},{"name":"Earphone case03","cat":"digital","img":"assets/product-06.webp","names":{"ko":"이어폰 케이스 03","en":"Earbud case 03","ja":"イヤホンケース 03","zh":"耳机保护套 03","vi":"Ốp tai nghe 03"},"id":"products-6"},{"name":"Humidifier","cat":"digital","img":"assets/product-07.webp","names":{"ko":"가습기","en":"Humidifier","ja":"加湿器","zh":"加湿器","vi":"Máy tạo ẩm"},"id":"products-7"},{"name":"Keychain doll","cat":"toy","img":"assets/product-08.webp","names":{"ko":"인형 키링","en":"Plush keychain","ja":"ぬいぐるみキーホルダー","zh":"毛绒钥匙扣","vi":"Móc khóa thú bông"},"id":"products-8"},{"name":"Laptop case","cat":"digital","img":"assets/product-09.webp","names":{"ko":"노트북 파우치","en":"Laptop sleeve","ja":"パソコンケース","zh":"电脑包","vi":"Túi đựng laptop"},"id":"products-9"},{"name":"NOTE02","cat":"paper","img":"assets/product-10.webp","names":{"ko":"노트 02","en":"Notebook 02","ja":"ノート 02","zh":"笔记本 02","vi":"Sổ ghi chép 02"},"id":"products-10"},{"name":"Neck cushion","cat":"toy","img":"assets/product-11.webp","names":{"ko":"목베개","en":"Neck pillow","ja":"ネックピロー","zh":"颈枕","vi":"Gối cổ"},"id":"products-11"},{"name":"PHONE CASE02","cat":"digital","img":"assets/product-12.webp","names":{"ko":"휴대폰 케이스 02","en":"Phone case 02","ja":"スマホケース 02","zh":"手机壳 02","vi":"Ốp điện thoại 02"},"id":"products-12"},{"name":"Phone pouch","cat":"fashion","img":"assets/product-13.webp","names":{"ko":"휴대폰 파우치","en":"Phone pouch","ja":"スマホポーチ","zh":"手机包","vi":"Túi đựng điện thoại"},"id":"products-13"},{"name":"Pouch","cat":"fashion","img":"assets/product-14.webp","names":{"ko":"파우치","en":"Pouch","ja":"ポーチ","zh":"收纳包","vi":"Túi nhỏ"},"id":"products-14"},{"name":"Shampoo","cat":"life","img":"assets/product-15.webp","names":{"ko":"샴푸","en":"Shampoo","ja":"シャンプー","zh":"洗发水","vi":"Dầu gội"},"id":"products-15"},{"name":"Shopping bag","cat":"fashion","img":"assets/product-16.webp","names":{"ko":"쇼핑백","en":"Shopping bag","ja":"ショッピングバッグ","zh":"购物袋","vi":"Túi mua sắm"},"id":"products-16"},{"name":"Skin lotion","cat":"life","img":"assets/product-17.webp","names":{"ko":"로션","en":"Lotion","ja":"ローション","zh":"润肤乳","vi":"Sữa dưỡng da"},"id":"products-17"},{"name":"Tumbler02","cat":"fashion","img":"assets/product-18.webp","names":{"ko":"텀블러 02","en":"Tumbler 02","ja":"タンブラー 02","zh":"随行杯 02","vi":"Bình giữ nhiệt 02"},"id":"products-18"},{"name":"air purifier","cat":"digital","img":"assets/product-19.webp","names":{"ko":"공기청정기","en":"Air purifier","ja":"空気清浄機","zh":"空气净化器","vi":"Máy lọc không khí"},"id":"products-19"},{"name":"arttoy03","cat":"toy","img":"assets/product-21.webp","names":{"ko":"아트토이 03","en":"Art toy 03","ja":"アートトイ 03","zh":"潮玩摆件 03","vi":"Mô hình nghệ thuật 03"},"id":"products-21"},{"name":"arttoy04","cat":"toy","img":"assets/product-22.webp","names":{"ko":"아트토이 04","en":"Art toy 04","ja":"アートトイ 04","zh":"潮玩摆件 04","vi":"Mô hình nghệ thuật 04"},"id":"products-22"},{"name":"arttoy05","cat":"toy","img":"assets/product-23.webp","names":{"ko":"아트토이 05","en":"Art toy 05","ja":"アートトイ 05","zh":"潮玩摆件 05","vi":"Mô hình nghệ thuật 05"},"id":"products-23"},{"name":"arttoy06","cat":"toy","img":"assets/product-24.webp","names":{"ko":"아트토이 06","en":"Art toy 06","ja":"アートトイ 06","zh":"潮玩摆件 06","vi":"Mô hình nghệ thuật 06"},"id":"products-24"},{"name":"calendar","cat":"paper","img":"assets/product-25.webp","names":{"ko":"달력","en":"Calendar","ja":"カレンダー","zh":"台历","vi":"Lịch"},"id":"products-25"},{"name":"canvas shoes","cat":"fashion","img":"assets/product-26.webp","names":{"ko":"캔버스 운동화","en":"Canvas shoes","ja":"キャンバスシューズ","zh":"帆布鞋","vi":"Giày vải"},"id":"products-26"},{"name":"cap","cat":"fashion","img":"assets/product-27.webp","names":{"ko":"모자","en":"Cap","ja":"キャップ","zh":"帽子","vi":"Mũ"},"id":"products-27"},{"name":"carrier","cat":"fashion","img":"assets/product-28.webp","names":{"ko":"여행용 캐리어","en":"Suitcase","ja":"スーツケース","zh":"行李箱","vi":"Vali"},"id":"products-28"},{"name":"diary","cat":"paper","img":"assets/product-29.webp","names":{"ko":"다이어리","en":"Diary","ja":"手帳","zh":"手账本","vi":"Sổ tay"},"id":"products-29"},{"name":"earphone case","cat":"digital","img":"assets/product-30.webp","names":{"ko":"이어폰 케이스","en":"Earbud case","ja":"イヤホンケース","zh":"耳机保护套","vi":"Ốp tai nghe"},"id":"products-30"},{"name":"hair dryer","cat":"digital","img":"assets/product-31.webp","names":{"ko":"헤어드라이어","en":"Hair dryer","ja":"ヘアドライヤー","zh":"吹风机","vi":"Máy sấy tóc"},"id":"products-31"},{"name":"indoor shoes","cat":"fashion","img":"assets/product-32.webp","names":{"ko":"실내화","en":"Slippers","ja":"ルームシューズ","zh":"室内拖鞋","vi":"Dép đi trong nhà"},"id":"products-32"},{"name":"mug","cat":"fashion","img":"assets/product-33.webp","names":{"ko":"머그컵","en":"Mug","ja":"マグカップ","zh":"马克杯","vi":"Cốc"},"id":"products-33"},{"name":"phone case","cat":"digital","img":"assets/product-34.webp","names":{"ko":"휴대폰 케이스","en":"Phone case","ja":"スマホケース","zh":"手机壳","vi":"Ốp điện thoại"},"id":"products-34"},{"name":"t-shirt01","cat":"fashion","img":"assets/product-35.webp","names":{"ko":"티셔츠 01","en":"T-shirt 01","ja":"Tシャツ 01","zh":"T恤 01","vi":"Áo thun 01"},"id":"products-35"},{"name":"t-shirt02","cat":"fashion","img":"assets/product-36.webp","names":{"ko":"티셔츠 02","en":"T-shirt 02","ja":"Tシャツ 02","zh":"T恤 02","vi":"Áo thun 02"},"id":"products-36"},{"name":"toaster","cat":"digital","img":"assets/product-37.webp","names":{"ko":"토스터","en":"Toaster","ja":"トースター","zh":"烤面包机","vi":"Máy nướng bánh mì"},"id":"products-37"},{"name":"umbrella","cat":"fashion","img":"assets/product-38.webp","names":{"ko":"우산","en":"Umbrella","ja":"傘","zh":"雨伞","vi":"Ô"},"id":"products-38"},{"name":"Art toy 07","cat":"toy","img":"assets/arttoy-07.jpg","names":{"ko":"아트토이 07","en":"Art toy 07","ja":"アートトイ 07","zh":"艺术玩具 07","vi":"Đồ chơi nghệ thuật 07"},"id":"products-39"},{"name":"Art toy 08","cat":"toy","img":"assets/arttoy-08.jpg","names":{"ko":"아트토이 08","en":"Art toy 08","ja":"アートトイ 08","zh":"艺术玩具 08","vi":"Đồ chơi nghệ thuật 08"},"id":"products-40"},{"name":"Art toy 09","cat":"toy","img":"assets/arttoy-09.jpg","names":{"ko":"아트토이 09","en":"Art toy 09","ja":"アートトイ 09","zh":"艺术玩具 09","vi":"Đồ chơi nghệ thuật 09"},"id":"products-41"},{"name":"Art toy 10","cat":"toy","img":"assets/arttoy-10.jpg","names":{"ko":"아트토이 10","en":"Art toy 10","ja":"アートトイ 10","zh":"艺术玩具 10","vi":"Đồ chơi nghệ thuật 10"},"id":"products-42"},{"name":"Art toy 11","cat":"toy","img":"assets/arttoy-11.png","names":{"ko":"아트토이 11","en":"Art toy 11","ja":"アートトイ 11","zh":"艺术玩具 11","vi":"Đồ chơi nghệ thuật 11"},"id":"products-43"},{"name":"Art toy 12","cat":"toy","img":"assets/arttoy-12.png","names":{"ko":"아트토이 12","en":"Art toy 12","ja":"アートトイ 12","zh":"艺术玩具 12","vi":"Đồ chơi nghệ thuật 12"},"id":"products-44"},{"name":"Art toy 13","cat":"toy","img":"assets/arttoy-13.png","names":{"ko":"아트토이 13","en":"Art toy 13","ja":"アートトイ 13","zh":"艺术玩具 13","vi":"Đồ chơi nghệ thuật 13"},"id":"products-45"},{"name":"Art toy 14","cat":"toy","img":"assets/arttoy-14.png","names":{"ko":"아트토이 14","en":"Art toy 14","ja":"アートトイ 14","zh":"艺术玩具 14","vi":"Đồ chơi nghệ thuật 14"},"id":"products-46"},{"name":"Art toy 15","cat":"toy","img":"assets/arttoy-15.png","names":{"ko":"아트토이 15","en":"Art toy 15","ja":"アートトイ 15","zh":"艺术玩具 15","vi":"Đồ chơi nghệ thuật 15"},"id":"products-47"}],"reels":[{"src":"assets/zh1-square.mp4","poster":"assets/zh1-poster.webp","title":{"ko":"쥬비양의 첫 번째 이야기","en":"Zhubiyang · First moments","ja":"Zhubiyangの最初の物語","zh":"猪鼻羊的第一个故事","vi":"Câu chuyện đầu tiên của Zhubiyang"},"id":"reels-0"},{"src":"assets/reel-02.mp4","poster":"assets/reel-02.webp","title":{"ko":"쥬비양 릴스 02","en":"Zhubiyang Reels 02","ja":"Zhubiyang リール 02","zh":"猪鼻羊短视频 02","vi":"Zhubiyang Reels 02"},"id":"reels-1"},{"src":"assets/reel-03.mp4","poster":"assets/reel-03.webp","title":{"ko":"쥬비양 릴스 03","en":"Zhubiyang Reels 03","ja":"Zhubiyang リール 03","zh":"猪鼻羊短视频 03","vi":"Zhubiyang Reels 03"},"id":"reels-2"},{"src":"assets/reel-04.mp4","poster":"assets/reel-04.webp","title":{"ko":"쥬비양 릴스 04","en":"Zhubiyang Reels 04","ja":"Zhubiyang リール 04","zh":"猪鼻羊短视频 04","vi":"Zhubiyang Reels 04"},"id":"reels-3"},{"src":"assets/reel-05.mp4","poster":"assets/reel-05.webp","title":{"ko":"쥬비양 릴스 05","en":"Zhubiyang Reels 05","ja":"Zhubiyang リール 05","zh":"猪鼻羊短视频 05","vi":"Zhubiyang Reels 05"},"id":"reels-4"},{"src":"assets/reel-06.mp4","poster":"assets/reel-06.webp","title":{"ko":"쥬비양 릴스 06","en":"Zhubiyang Reels 06","ja":"Zhubiyang リール 06","zh":"猪鼻羊短视频 06","vi":"Zhubiyang Reels 06"},"id":"reels-5"},{"src":"assets/reel-07.mp4","poster":"assets/reel-07.webp","title":{"ko":"쥬비양 릴스 07","en":"Zhubiyang Reels 07","ja":"Zhubiyang リール 07","zh":"猪鼻羊短视频 07","vi":"Zhubiyang Reels 07"},"id":"reels-6"},{"src":"assets/reel-08.mp4","poster":"assets/reel-08.webp","title":{"ko":"쥬비양 릴스 08","en":"Zhubiyang Reels 08","ja":"Zhubiyang リール 08","zh":"猪鼻羊短视频 08","vi":"Zhubiyang Reels 08"},"id":"reels-7"}]};
let reels = initialCatalog.reels;

function renderReels() {
  const grid = document.querySelector('#reels-grid');
  if (!grid) return;
  const re = document.querySelector('#reels-empty');
  if (re) re.hidden = reels.length > 0;
  grid.replaceChildren(...reels.map(r => {
    const card = document.createElement('article');
    card.className = 'reel-card';
    const v = document.createElement('video');
    v.controls = true;
    v.playsInline = true;
    v.preload = 'metadata';
    v.src = r.src;
    if (r.poster) v.poster = r.poster;
    const titleText = r.title?.[lang] || r.title?.en || r.title?.ko || 'Zhubiyang';
    v.setAttribute('aria-label', titleText);
    v.addEventListener('play', () => grid.querySelectorAll('video').forEach(other => {
      if (other !== v) other.pause();
    }));
    const title = document.createElement('h3');
    title.textContent = titleText;
    const fallback = document.createElement('a');
    fallback.href = r.src;
    fallback.target = '_blank';
    fallback.rel = 'noopener noreferrer';
    fallback.textContent = (copy?.[lang]?.videoDownload || 'Download video') + ' ↗';
    fallback.className = 'video-fallback';
    v.addEventListener('error', () => {
      fallback.textContent = (copy?.[lang]?.videoFail || 'Playback failed') + ' ' + (copy?.[lang]?.videoDownload || 'Download video') + ' ↗';
    });
    const frame = document.createElement('div');
    frame.className = 'reel-frame';
    if (r.poster) frame.style.setProperty('--poster', `url("${r.poster}")`);
    frame.append(v);
    card.append(frame, title, fallback);
    return card;
  }));
}

const supported = ['ko', 'en', 'ja', 'zh', 'vi'];
function detectLanguage(saved, languages) {
  if (supported.includes(saved)) return saved;
  for (const locale of languages || []) {
    const base = locale.toLowerCase().split(/[-_]/)[0];
    if (supported.includes(base)) return base;
  }
  return 'en';
}

let savedLanguage = null;
try { savedLanguage = localStorage.getItem('zhubiyang-language'); } catch {}
let lang = detectLanguage(savedLanguage, navigator.languages || [navigator.language]);
let category = 'all', limit = Infinity, products = initialCatalog.products, selected = null;
const $ = s => document.querySelector(s);
const cats = ['all', 'toy', 'fashion', 'paper', 'digital', 'life'];
const productName = p => p.names?.[lang] || p.names?.en || p.name;

function translate() {
  renderReels();
  document.documentElement.lang = lang === 'zh' ? 'zh-CN' : lang;
  if (copy && copy[lang]) {
    document.querySelectorAll('[data-t], [data-extra]').forEach(el => {
      const key = el.dataset.t || el.dataset.extra;
      if (copy[lang] && copy[lang][key]) el.innerHTML = copy[lang][key];
    });
    if ($('#language')) {
      $('#language').value = lang;
      if (copy[lang].languageLabel) $('#language').setAttribute('aria-label', copy[lang].languageLabel);
    }
    if ($('nav') && copy[lang].navigationLabel) $('nav').setAttribute('aria-label', copy[lang].navigationLabel);
    if ($('#filters') && copy[lang].categoriesLabel) $('#filters').setAttribute('aria-label', copy[lang].categoriesLabel);
    if ($('#close') && copy[lang].closeLabel) $('#close').setAttribute('aria-label', copy[lang].closeLabel);
    if ($('meta[name="description"]') && copy[lang].intro) $('meta[name="description"]').content = copy[lang].intro;
    if (copy[lang].nav1) document.title = 'ZHUBIYANG · ' + copy[lang].nav1;
    if ($('#form-status') && $('#form-status').textContent && copy[lang].status) {
      $('#form-status').textContent = copy[lang].status;
    }
    if ($('#filters')) {
      $('#filters').replaceChildren(...cats.map(c => {
        const b = document.createElement('button');
        b.textContent = copy[lang][c] || c;
        b.className = c === category ? 'active' : '';
        b.setAttribute('aria-pressed', String(c === category));
        b.onclick = () => { category = c; translate(); };
        return b;
      }));
    }
  }
  render();
  if (selected && copy && copy[lang]) {
    if ($('#detail-category')) $('#detail-category').textContent = copy[lang][selected.cat] || selected.cat;
    if ($('#detail-name')) $('#detail-name').textContent = productName(selected);
    if ($('#large')) $('#large').alt = productName(selected);
  }
}

function render() {
  const filtered = products.filter(p => category === 'all' || p.cat === category);
  if ($('#count') && copy && copy[lang]) {
    $('#count').textContent = `${filtered.length} ${copy[lang].count || ''}`;
  }
  if ($('#grid')) {
    $('#grid').replaceChildren(...filtered.slice(0, limit).map(p => {
      const b = document.createElement('button');
      b.className = 'product';
      const wrap = document.createElement('div');
      wrap.className = 'product-image';
      const img = new Image();
      img.src = p.img;
      img.alt = productName(p);
      img.loading = 'lazy';
      wrap.append(img);
      const c = document.createElement('span');
      c.textContent = copy?.[lang]?.[p.cat] || '';
      const h = document.createElement('h3');
      h.textContent = productName(p) + ' ↗';
      b.append(wrap, c, h);
      b.onclick = () => {
        selected = p;
        if ($('#large')) { $('#large').src = p.img; $('#large').alt = productName(p); }
        if ($('#detail-name')) $('#detail-name').textContent = productName(p);
        if ($('#detail-category')) $('#detail-category').textContent = copy?.[lang]?.[p.cat] || '';
        if ($('#viewer') && typeof $('#viewer').showModal === 'function') $('#viewer').showModal();
      };
      return b;
    }));
  }
  if ($('#more')) $('#more').hidden = limit >= filtered.length;
}

if ($('#language')) {
  $('#language').onchange = () => {
    lang = $('#language').value;
    try { localStorage.setItem('zhubiyang-language', lang); } catch {}
    translate();
  };
}
if ($('#more')) $('#more').onclick = () => { limit += 9; render(); };
if ($('#close')) $('#close').onclick = () => { if ($('#viewer')) $('#viewer').close(); };
if ($('#viewer')) {
  $('#viewer').onclick = e => {
    if (e.target === $('#viewer')) {
      const r = e.target.getBoundingClientRect();
      if (e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom) e.target.close();
    }
  };
}
if ($('#product-inquiry')) {
  $('#product-inquiry').onclick = () => {
    if ($('#viewer')) $('#viewer').close();
    if ($('#inquiry textarea')) {
      $('#inquiry textarea').value = (copy?.[lang]?.productPrefix || '') + productName(selected) + '\n';
    }
  };
}
if ($('#inquiry')) {
  $('#inquiry').onsubmit = e => {
    e.preventDefault();
    const f = new FormData(e.target);
    const subject = 'ZHUBIYANG ' + (copy?.[lang]?.subject || 'Inquiry');
    const body = `Name: ${f.get('name')}\nCompany: ${f.get('company')}\nEmail: ${f.get('email')}\n\n${f.get('message')}`;
    window.location.href = 'mailto:crzone@kakao.com?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
    if ($('#form-status') && copy?.[lang]?.status) $('#form-status').textContent = copy[lang].status;
  };
}

translate();

async function refreshCatalog() {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), 10000);
  try {
    const response = await fetch('api_content.json', { cache: 'no-store', signal: controller.signal });
    if (!response.ok) throw Error('content');
    const data = await response.json();
    if (!Array.isArray(data.products) || !Array.isArray(data.reels)) throw Error('catalog');
    products = data.products;
    reels = data.reels;
    render();
    renderReels();
  } catch (error) {
    console.warn('Catalog refresh unavailable; keeping displayed collection.');
  } finally {
    clearTimeout(timer);
  }
}
refreshCatalog();
