const fs = require('fs');
const html = fs.readFileSync('/Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html', 'utf8');
const scriptContent = html.match(/<script>([\s\S]*?)<\/script>/)[1];

fs.writeFileSync('/Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/temp_script.js', scriptContent);
