const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

async function debugLiveClick() {
    console.log("1. Launching Chrome on local index.html...");
    const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
        '--remote-debugging-port=9222',
        '--headless=new',
        '--no-sandbox',
        '--disable-gpu',
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

    const WebSocket = require('/Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/node_modules/ws');
    const ws = new WebSocket(target.webSocketDebuggerUrl);

    let msgId = 1;
    function send(method, params = {}) {
        return new Promise((resolve) => {
            const id = msgId++;
            const handler = (data) => {
                const res = JSON.parse(data);
                if (res.id === id) {
                    ws.removeListener('message', handler);
                    resolve(res);
                }
            };
            ws.on('message', handler);
            ws.send(JSON.stringify({ id, method, params }));
        });
    }

    await new Promise(resolve => ws.on('open', resolve));
    await send('Runtime.enable');
    await send('Page.enable');

    ws.on('message', (data) => {
        const msg = JSON.parse(data);
        if (msg.method === 'Runtime.consoleAPICalled') {
            console.log("CONSOLE LOG:", msg.params.args.map(a => a.value || a.description).join(' '));
        } else if (msg.method === 'Runtime.exceptionThrown') {
            console.error("RUNTIME EXCEPTION:", msg.params.exceptionDetails.text, msg.params.exceptionDetails.exception.description);
        }
    });

    console.log("2. Executing startGameSession()...");
    await send('Runtime.evaluate', { expression: "startGameSession()" });
    await new Promise(r => setTimeout(r, 1000));

    console.log("3. Inspecting Lobby Status...");
    const status1 = await send('Runtime.evaluate', {
        expression: "JSON.stringify({ lobbyDisplay: document.getElementById('lobby-screen').style.display, gridBubbles: document.querySelectorAll('.grid-char-bubble').length })"
    });
    console.log("Lobby Status:", status1.result.result.value);

    console.log("4. Clicking Strawberry Card (Index 0)...");
    const clickRes = await send('Runtime.evaluate', {
        expression: "selectLobbyCharacter(0, document.querySelectorAll('.grid-char-bubble')[0])"
    });
    console.log("selectLobbyCharacter result:", clickRes);

    await new Promise(r => setTimeout(r, 1000));

    console.log("5. Inspecting Playground Stage Status...");
    const status2 = await send('Runtime.evaluate', {
        expression: "JSON.stringify({ lobbyDisplay: document.getElementById('lobby-screen').style.display, splashDisplay: document.getElementById('start-splash-screen').style.display, activeEmoji: typeof activeEmoji !== 'undefined' ? activeEmoji : null, pointsLength: typeof points !== 'undefined' ? points.length : null, jellyImageWidth: jellyImage ? jellyImage.width : null })"
    });
    console.log("Playground Status:", status2.result.result.value);

    const shot = await send('Page.captureScreenshot', { format: 'png' });
    fs.writeFileSync('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/debug_live_stage.png', Buffer.from(shot.result.data, 'base64'));
    console.log("Saved debug_live_stage.png!");

    ws.close();
    chrome.kill();
}

debugLiveClick().catch(console.error);
