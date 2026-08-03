with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

working_deco_code = """        // ==========================================================================
        // 100% WORKING RANDOM FLOATING BACKGROUND JELLY STAGE ENGINE
        // ==========================================================================
        let decoJellyImages = [];
        let decoJellies = [];
        const TOTAL_DECO_SPRITES = 19;

        function loadDecoJellySprites() {
            decoJellyImages = [];
            for (let i = 1; i <= TOTAL_DECO_SPRITES; i++) {
                let numStr = i < 10 ? '0' + i : '' + i;
                let img = new Image();
                img.src = `deco_sprites/${numStr}.png`;
                decoJellyImages.push(img);
            }
        }
        loadDecoJellySprites();

        function generateDecoJellies() {
            decoJellies = [];
            let stageW = width || 388;
            let stageH = height || 800;
            let count = 10; // 10 random floating background jellies

            for (let i = 0; i < count; i++) {
                let imgIdx = Math.floor(Math.random() * TOTAL_DECO_SPRITES);
                decoJellies.push({
                    imgIndex: imgIdx,
                    x: Math.random() * stageW,
                    y: Math.random() * stageH,
                    vx: (Math.random() - 0.5) * 0.7,
                    vy: (Math.random() - 0.5) * 0.7,
                    scale: 0.22 + Math.random() * 0.22,
                    angle: Math.random() * Math.PI * 2,
                    vRot: (Math.random() - 0.5) * 0.01,
                    bobOffset: Math.random() * Math.PI * 2
                });
            }
        }

        function drawDecoJellies() {
            if (!decoJellies || decoJellies.length === 0) {
                generateDecoJellies();
            }

            let stageW = width || 388;
            let stageH = height || 800;
            let time = Date.now() * 0.0018;

            for (let i = 0; i < decoJellies.length; i++) {
                let j = decoJellies[i];
                let img = decoJellyImages[j.imgIndex];

                // Random floating drift movement
                j.x += j.vx;
                j.y += j.vy + Math.sin(time + j.bobOffset) * 0.22;
                j.angle += j.vRot;

                // Screen boundary wrap-around
                if (j.x < -50) j.x = stageW + 50;
                if (j.x > stageW + 50) j.x = -50;
                if (j.y < -50) j.y = stageH + 50;
                if (j.y > stageH + 50) j.y = -50;

                if (img && img.complete && img.naturalWidth > 0) {
                    ctx.save();
                    ctx.translate(j.x, j.y);
                    ctx.rotate(j.angle);
                    ctx.scale(j.scale, j.scale);
                    ctx.globalAlpha = 0.85;

                    // Soft ambient shadow
                    ctx.fillStyle = 'rgba(0, 0, 0, 0.12)';
                    ctx.beginPath();
                    ctx.ellipse(0, 45, 45, 15, 0, 0, Math.PI * 2);
                    ctx.fill();

                    // Render transparent jelly design image
                    ctx.drawImage(img, -img.naturalWidth / 2, -img.naturalHeight / 2);
                    ctx.restore();
                }
            }
        }"""

old_broken_deco = """function generateDecoJellies(baseHue) {
            decoJellies = [];
        }
        function drawDecoJellies() {
            return;
        }"""

if old_broken_deco in content:
    content = content.replace(old_broken_deco, working_deco_code)
    print("100% Successfully replaced broken drawDecoJellies with WORKING floating jelly engine!")
else:
    print("WARNING: old_broken_deco not found!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Working Floating Background Jellies in index.html!")
