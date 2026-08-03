const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

async function testLocalFlow() {
    console.log("1. Launching Chrome on local index.html...");
    const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
        '--headless=new',
        '--disable-gpu',
        '--remote-debugging-port=9222',
        '--window-size=412,840',
        'file:///Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html'
    ]);

    await new Promise(r => setTimeout(r, 2500));

    const jsonText = await new Promise((resolve, reject) => {
        http.get('http://localhost:9222/json', (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(data));
        }).on('error', reject);
    });

    const targets = JSON.parse(jsonText);
    const target = targets.find(t => t.type === 'page' && !t.url.startsWith('chrome-extension')) || targets[0];
    console.log("Target page URL:", target.url);

    const WebSocket = require('/Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/node_modules/ws') || null;
    
