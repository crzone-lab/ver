const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

async function testNativeCDP() {
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

    const ws = new WebSocket(target.webSocketDebuggerUrl);
    let msgId = 1;
    const pending = new Map();

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        if (data.id && pending.has(data.id)) {
            pending.get(data.id)(data);
            pending.delete(data.id);
        }
    };

    function send(method, params = {}) {
        return new Promise((resolve) => {
            const id = msgId++;
            pending.set(id, resolve);
            ws.send(JSON.stringify({ id, method, params }));
        });
    }

    await new Promise(r => ws.onopen = r);
    await send('Runtime.enable');

    console.log("=== 1. CALL startGameSession() ===");
    const res1 = await send('Runtime.evaluate', { expression: "startGameSession()" });
    console.log("startGameSession output:", res1.result);

    await new Promise(r => setTimeout(r, 1000));

    console.log("=== 2. INSPECT LOBBY STATE ===");
    const res2 = await send('Runtime.evaluate', {
        expression: "JSON.stringify({ lobbyDisplay: document.getElementById('lobby-screen').style.display, splashDisplay: document.getElementById('start-splash-screen').style.display, bubblesCount: document.querySelectorAll('.grid-char-bubble').length })"
    });
    console.log("Lobby state:", res2.result.result.value);

    console.log("=== 3. CLICK STRAWBERRY CARD (Index 0) ===");
    const res3 = await send('Runtime.evaluate', {
        expression: "selectLobbyCharacter(0, document.querySelectorAll('.grid-char-bubble')[0])"
    });
    console.log("selectLobbyCharacter output:", res3.result);

    await new Promise(r => setTimeout(r, 1000));

    console.log("=== 4. INSPECT PLAYGROUND STATE ===");
    const res4 = await send('Runtime.evaluate', {
        expression: "JSON.stringify({ lobbyDisplay: document.getElementById('lobby-screen').style.display, splashDisplay: document.getElementById('start-splash-screen').style.display, activeEmoji: activeEmoji, activeHue: activeHue, pointsLength: points ? points.length : null, jellyImageComplete: jellyImage ? jellyImage.complete : null, jellyImageWidth: jellyImage ? jellyImage.width : null })"
    });
    console.log("Playground state:", res4.result.result.value);

    ws.close();
    chrome.kill();
}

testNativeCDP().catch(console.error);
