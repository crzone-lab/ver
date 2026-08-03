
const fs = require('fs');
const html = fs.readFileSync('/Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html', 'utf8');
const scriptContent = html.match(/<script>([\s\S]*?)<\/script>/)[1];

const lines = scriptContent.split('\n');
let codeSoFar = '';
for (let i = 0; i < lines.length; i++) {
    codeSoFar += lines[i] + '\n';
    try {
        new Function(codeSoFar);
    } catch (e) {
        if (e.message.includes("Unexpected token ','") || e.message.includes("Unexpected token")) {
            console.log(`Line ${i + 1}: ${lines[i]}`);
            console.log('Error message:', e.message);
        }
    }
}
