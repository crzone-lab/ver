(()=>{const supported=['ko','en','ja','zh','vi'];let dictionary={},lang='ko',observer;const originals=new WeakMap(),attributes=new WeakMap();const selector=document.querySelector('#language-select');let preference='auto';try{preference=localStorage.getItem('fruit-language')||'auto'}catch{}if(!supported.includes(preference)&&preference!=='auto')preference='auto';selector.value=detect(preference);
function detect(value){if(value!=='auto')return value;for(const locale of navigator.languages||[navigator.language]){const base=String(locale).toLowerCase().split('-')[0];if(supported.includes(base))return base}return'en'}
function text(source){
  const trimmed=source.trim();
  if(!trimmed||lang==='ko')return source;
  let translated=dictionary[trimmed]?.[lang];
  if(!translated){
    const normalized=trimmed.replace(/\s+/g,' ');
    translated=dictionary[normalized]?.[lang];
  }
  if(!translated){
    const stripped=trimmed.replace(/^[\s\.\,\!\?]+|[\s\.\,\!\?]+$/g,'');
    if(dictionary[stripped]?.[lang])translated=dictionary[stripped][lang];
  }
  return translated ? source.replace(trimmed,translated) : source;
}
function apply(root=document.body){const walker=document.createTreeWalker(root,NodeFilter.SHOW_TEXT);const nodes=[];let n;while(n=walker.nextNode())nodes.push(n);for(const node of nodes){if(node.parentElement?.closest('script,style,select,textarea,.chat-bubble'))continue;let state=originals.get(node);if(!state||node.nodeValue!==state.last)state={source:node.nodeValue,last:node.nodeValue};const next=text(state.source);if(next!==node.nodeValue)node.nodeValue=next;state.last=next;originals.set(node,state)}for(const el of root.querySelectorAll('[placeholder],[aria-label],[alt]')){let saved=attributes.get(el)||{};for(const key of ['placeholder','aria-label','alt']){if(!el.hasAttribute(key))continue;const value=el.getAttribute(key),state=saved[key];if(!state||value!==state.last)saved[key]={source:value,last:value};const next=text(saved[key].source);if(next!==value)el.setAttribute(key,next);saved[key].last=next}attributes.set(el,saved)}}
function choose(value){lang=detect(value);selector.value=lang;document.documentElement.lang=lang;document.body.dataset.language=lang;document.title=lang==='ko'?'FRUIT RABBIT · 과일토끼':'FRUIT RABBIT · CRZONE';observer?.disconnect();apply();observer?.observe(document.body,{subtree:true,childList:true,characterData:true});document.dispatchEvent(new CustomEvent('fruit-language-change',{detail:lang}))}
selector.addEventListener('change',()=>{try{localStorage.setItem('fruit-language',selector.value)}catch{}choose(selector.value)});fetch('translations.json?v=arttoy4').then(r=>{if(!r.ok)throw Error();return r.json()}).then(d=>{dictionary=d;observer=new MutationObserver(()=>{observer.disconnect();apply();observer.observe(document.body,{subtree:true,childList:true,characterData:true})});choose(preference)}).catch(()=>{selector.value='ko';selector.disabled=true});window.fruitLocale={get language(){return lang},translate:text};})();