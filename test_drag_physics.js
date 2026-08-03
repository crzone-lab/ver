const fs = require('fs');
const http = require('http');
const WebSocket = require('ws');
const { spawn } = require('child_process');

async function testDrag() {
    const chrome = spawn('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', [
        '--remote-debugging-port=9222',
        '--headless=new',
        '--no-sandbox',
        '--disable-gpu',
        'file:///Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html'
    ]);

    await new Promise(r => setTimeout(r, 2500));

    const json = await new Promise((resolve, reject) => {
        http.get('http://localhost:9222/json', (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => resolve(JSON.parse(data)));
        }).on('error', reject);
    });

    const target = json.find(t => t.type === 'page' && !t.url.startsWith('chrome-extension'));
    const ws = new WebSocket(target.webSocketDebuggerUrl);

    await new Promise(resolve => ws.on('open', resolve));
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

    await send('Page.enable');
    await new Promise(r => setTimeout(r, 1000));

    // Evaluate mesh node movements during drag
    const evalRes = await send('Runtime.evaluate', {
        expression: `
            (function() {
                // Initialize playground mode directly
                const splash = document.getElementById('start-splash-screen');
                if (splash) splash.style.display = 'none';
                setScreenMode('playground');
                
                // Get initial positions
                const before = points.map(p => ({ x: Math.round(p.x), y: Math.round(p.y) }));
                
                // Simulate drag on node index 20 (middle of rabbit) by moving touch down 80px
                grabbedPointIndex = 20;
                isTouching = true;
                touchX = points[20].x;
                touchY = points[20].y + 80;
                
                // Run draw step once to trigger drag shift
                draw();
                
                const after = points.map(p => ({ x: Math.round(p.x), y: Math.round(p.y) }));
                
                return JSON.stringify({
                    topEarBefore: before[0],
                    topEarAfter: after[0],
                    middleBefore: before[20],
                    middleAfter: after[20],
                    bottomFeetBefore: before[63],
                    bottomFeetAfter: after[63],
                    topDeltaY: after[0].y - before[0].y,
                    middleDeltaY: after[20].y - before[20].y,
                    bottomDeltaY: after[63].y - before[63].y
                });
            })()
        `
    });

    console.log("TEST RESULTS:", evalRes.result.result.value);
    ws.close();
    chrome.kill();
}

testDrag().catch(console.error);
