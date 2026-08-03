
const puppeteer = require('puppeteer');
(async () => {
    try {
        const browser = await puppeteer.launch();
        const page = await browser.newPage();
        await page.setViewport({ width: 412, height: 840 });
        await page.goto('file:///Users/crzone/.gemini/antigravity/scratch/fruit-rabbit-touch-engine/index.html');
        await page.waitForTimeout(500);
        
        // Click Start Game Button
        await page.click('.start-game-btn');
        await page.waitForTimeout(1000);

        await page.screenshot({ path: '/Users/crzone/.gemini/antigravity/brain/827de87e-5067-4327-9014-bff4ce181bb6/playground_after_start_click.png' });
        await browser.close();
        console.log('Successfully clicked Game Start and captured screenshot!');
    } catch(err) {
        console.error(err);
    }
})();
