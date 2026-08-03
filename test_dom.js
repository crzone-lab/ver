
const fs = require('fs');
const html = fs.readFileSync('/Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html', 'utf-8');
const js = html.split('<script>')[1].split('</script>')[0];

const jsdom = require('jsdom');
const { JSDOM } = jsdom;

const dom = new JSDOM(html, { runScripts: "dangerously" });
const window = dom.window;

console.log("Lobby children count:", window.document.getElementById('lobby-character-grid').children.length);
