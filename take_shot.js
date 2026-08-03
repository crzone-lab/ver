
const puppeteer = require('puppeteer');
(async () => {
    try {
        const browser = await puppeteer.launch({
            headless: 'new',
            args: ['--no-sandbox', '--disable-setuid-sandbox']
        });
        const page = await browser.newPage();
        await page.setViewport({ width: 412, height: 840 });
        await page.goto('https://fruit-rabbit-touch-engine.vercel.app', { waitUntil: 'networkidle0', timeout: 15000 });
        await page.screenshot({ path: '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/live_preview.png' });
        console.log("Puppeteer screenshot saved to live_preview.png!");
        await browser.close();
    } catch(err) {
        console.error("Puppeteer error:", err.message);
        process.exit(1);
    }
})();
