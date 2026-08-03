with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update generateDecoJellies and drawDecoJellies to load all 19 deco_sprites transparent PNGs and float randomly
floating_jellies_code = """        // ==========================================================================
        // RANDOM FLOATING BACKGROUND JELLY STAGE ENGINE (19 DECO SPRITES)
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
            let count = 10; // 10 random floating jellies on background stage
            for (let i = 0; i < count; i++) {
                let imgIdx = Math.floor(Math.random() * TOTAL_DECO_SPRITES);
                decoJellies.push({
                    imgIndex: imgIdx,
                    x: Math.random() * width,
                    y: Math.random() * height,
                    vx: (Math.random() - 0.5) * 0.8,
                    vy: (Math.random() - 0.5) * 0.8,
                    scale: 0.28 + Math.random() * 0.28,
                    angle: Math.random() * Math.PI * 2,
                    vRot: (Math.random() - 0.5) * 0.012,
                    bobOffset: Math.random() * Math.PI * 2
                });
            }
        }

        function drawDecoJellies() {
            if (!decoJellies || decoJellies.length === 0) {
                generateDecoJellies();
            }

            let time = Date.now() * 0.002;

            for (let i = 0; i < decoJellies.length; i++) {
                let j = decoJellies[i];
                let img = decoJellyImages[j.imgIndex];

                // Update position (random floating drift)
                j.x += j.vx;
                j.y += j.vy + Math.sin(time + j.bobOffset) * 0.25;
                j.angle += j.vRot;

                // Screen boundary wrap-around / bounce
                if (j.x < -40) j.x = width + 40;
                if (j.x > width + 40) j.x = -40;
                if (j.y < -40) j.y = height + 40;
                if (j.y > height + 40) j.y = -40;

                if (img && img.complete && img.naturalWidth > 0) {
                    ctx.save();
                    ctx.translate(j.x, j.y);
                    ctx.rotate(j.angle);
                    ctx.scale(j.scale, j.scale);
                    ctx.globalAlpha = 0.85;

                    // Soft ambient shadow underneath floating jelly
                    ctx.fillStyle = 'rgba(0,0,0,0.12)';
                    ctx.beginPath();
                    ctx.ellipse(0, 45, 45, 15, 0, 0, Math.PI * 2);
                    ctx.fill();

                    // Draw transparent jelly design image
                    ctx.drawImage(img, -img.naturalWidth / 2, -img.naturalHeight / 2);
                    ctx.restore();
                }
            }
        }"""

old_deco_placeholder = """        function generateDecoJellies() {
            decoJellies = [];
        }
        function drawDecoJellies() {
        }"""

if old_deco_placeholder in content:
    content = content.replace(old_deco_placeholder, floating_jellies_code)
    print("100% Successfully updated generateDecoJellies & drawDecoJellies!")
else:
    # Find generateDecoJellies function to replace
    idx = content.find('function generateDecoJellies()')
    if idx != -1:
        end_idx = content.find('}', content.find('function drawDecoJellies()')) + 1
        content = content[:idx] + floating_jellies_code + content[end_idx:]
        print("100% Successfully replaced generateDecoJellies & drawDecoJellies block!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Floating Background Jellies Engine in index.html!")
