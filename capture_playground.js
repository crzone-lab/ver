const { spawn } = require('child_process');
const http = require('http');
const fs = require('fs');

const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
    '--headless=new',
    '--disable-gpu',
    '--remote-debugging-port=9222',
    '--window-size=412,840',
    'https://fruit-rabbit-touch-engine.vercel.app/#test-playground'
]);

setTimeout(async () => {
    try {
        const resp = await fetch('http://localhost:9222/json');
        const targets = await resp.json();
        console.log('Available targets:', targets.map(t => ({ type: t.type, url: t.url })));
        const pageTarget = targets.find(t => t.type === 'page' && t.url.includes('fruit-rabbit')) || targets.find(t => t.type === 'page') || targets[0];
        const wsUrl = pageTarget.webSocketDebuggerUrl;
        console.log('Connecting to target URL:', pageTarget.url);

        const ws = new WebSocket(wsUrl);

        let msgId = 1;
        const send = (method, params = {}) => new Promise(resolve => {
            const id = msgId++;
            const handler = (event) => {
                const data = JSON.parse(event.data);
                if (data.id === id) {
                    ws.removeEventListener('message', handler);
                    resolve(data);
                }
            };
            ws.addEventListener('message', handler);
            ws.send(JSON.stringify({ id, method, params }));
        });

        ws.onopen = async () => {
            console.log('Navigating to #test-playground via CDP...');
            await send('Page.navigate', { url: 'https://fruit-rabbit-touch-engine.vercel.app/#test-playground' });
            await new Promise(r => setTimeout(r, 6000));

            // Capture screenshot
            const shotRes = await send('Page.captureScreenshot', { format: 'png' });
            const buf = Buffer.from(shotRes.result.data, 'base64');
            const outPath = '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/playground_live_preview.png';
            fs.writeFileSync(outPath, buf);
            console.log('Saved playground screenshot to:', outPath);

            ws.close();
            chrome.kill();
            process.exit(0);
        };
    } catch (e) {
        console.error('Error:', e);
        chrome.kill();
        process.exit(1);
    }
}, 2500);
