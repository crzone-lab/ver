const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

async function main() {
    const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
        '--headless=new',
        '--disable-gpu',
        '--remote-debugging-port=9222',
        '--window-size=412,840',
        'file:///Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html'
    ]);

    await new Promise(r => setTimeout(r, 3000));

    try {
        const jsonText = await new Promise((resolve, reject) => {
            http.get('http://localhost:9222/json', res => {
                let data = '';
                res.on('data', chunk => data += chunk);
                res.on('end', () => resolve(data));
            }).on('error', reject);
        });

        const targets = JSON.parse(jsonText);
        const target = targets.find(t => t.type === 'page' && !t.url.startsWith('chrome-extension')) || targets[0];
        const wsUrl = target.webSocketDebuggerUrl;
        console.log("Selected target URL:", target.url);
        console.log("WebSocket URL:", wsUrl);

        const ws = new WebSocket(wsUrl);
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

        // Explicitly navigate to local file
        await send('Page.navigate', { url: 'file:///Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html' });
        await new Promise(r => setTimeout(r, 3000));

        const info = await send('Runtime.evaluate', {
            expression: "JSON.stringify({ url: location.href, html: document.body ? document.body.innerHTML.substring(0, 300) : 'no_body' })"
        });
        console.log("Page info:", info.result.result.value);

        // 1. Capture Splash Screen
        const shotRes1 = await send('Page.captureScreenshot', { format: 'png' });
        fs.writeFileSync('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/audit_splash_screen.png', Buffer.from(shotRes1.result.data, 'base64'));
        console.log("Splash screen screenshot saved!");

        // 2. Click start game button -> Open Lobby Fruit Selection Screen
        const clickRes = await send('Runtime.evaluate', {
            expression: "const btn = document.querySelector('.start-game-btn'); if(btn){ btn.click(); 'clicked_start'; } else { 'not_found'; }"
        });
        console.log("Start click result:", clickRes);

        await new Promise(r => setTimeout(r, 1500));

        // Capture Lobby Fruit Selection Screen
        const shotResLobby = await send('Page.captureScreenshot', { format: 'png' });
        fs.writeFileSync('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/audit_lobby_screen.png', Buffer.from(shotResLobby.result.data, 'base64'));
        console.log("Lobby fruit selection screen screenshot saved!");

        // 3. Click first character card or play button to enter Playground
        const selectRes = await send('Runtime.evaluate', {
            expression: "const card = document.querySelectorAll('.grid-char-bubble')[0]; if(card){ card.click(); 'selected_card'; } else { selectLobbyCharacter(0); 'fallback_playground'; }"
        });
        console.log("Card selection result:", selectRes);

        await new Promise(r => setTimeout(r, 2000));

        // Capture Gameplay Stage Screen
        const shotRes2 = await send('Page.captureScreenshot', { format: 'png' });
        fs.writeFileSync('/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/clean_malrangi_preview.png', Buffer.from(shotRes2.result.data, 'base64'));
        console.log("Gameplay stage screenshot saved!");

        ws.close();
    } catch(err) {
        console.error("Error:", err);
    } finally {
        chrome.kill();
    }
}

main();
