const { spawn } = require('child_process');
const http = require('http');

async function runTest() {
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

    console.log("=== 1. START GAME SESSION ===");
    await send('Runtime.evaluate', { expression: "startGameSession()" });
    await new Promise(r => setTimeout(r, 1000));

    const resLobby = await send('Runtime.evaluate', {
        expression: "JSON.stringify({ lobbyDisplay: document.getElementById('lobby-screen').style.display, characterCardsCount: document.querySelectorAll('.grid-char-bubble').length, activeFeel: activeFeel })"
    });
    console.log("Lobby state:", resLobby.result.result.value);

    console.log("=== 2. TOGGLE FEEL PILLS ===");
    await send('Runtime.evaluate', { expression: "selectFeelPill('mochi')" });
    const pillMochiState = await send('Runtime.evaluate', { expression: "document.getElementById('pill-mochi').classList.contains('active')" });
    console.log("Mochi active:", pillMochiState.result.result.value);

    await send('Runtime.evaluate', { expression: "selectFeelPill('slime')" });
    const pillSlimeState = await send('Runtime.evaluate', { expression: "document.getElementById('pill-slime').classList.contains('active')" });
    console.log("Slime active:", pillSlimeState.result.result.value);

    await send('Runtime.evaluate', { expression: "selectFeelPill('jelly')" });
    const pillJellyState = await send('Runtime.evaluate', { expression: "document.getElementById('pill-jelly').classList.contains('active')" });
    console.log("Jelly active:", pillJellyState.result.result.value);

    console.log("=== 3. SELECT STRAWBERRY RABBIT (INDEX 0) ===");
    await send('Runtime.evaluate', { expression: "selectLobbyCharacter(0)" });
    await new Promise(r => setTimeout(r, 1000));

    const resPlayground = await send('Runtime.evaluate', {
        expression: "JSON.stringify({ lobbyDisplay: document.getElementById('lobby-screen').style.display, activeEmoji: activeEmoji, activeBase: activeBase, jellySrc: jellyImage.src.substring(jellyImage.src.lastIndexOf('/')+1) })"
    });
    console.log("Playground stage loaded character:", resPlayground.result.result.value);

    ws.close();
    chrome.kill();
}

runTest().catch(console.error);
