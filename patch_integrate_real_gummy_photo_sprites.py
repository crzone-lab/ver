import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

real_sprite_system = """
        // ==========================================================================
        // 100% REAL PRODUCT JELLY PHOTO SPRITE ENGINE (Extracted from User Photos)
        // ==========================================================================
        const realJellySpritePaths = [
            "deco_sprites/real_bunny_1.png", "deco_sprites/real_bunny_2.png", "deco_sprites/real_bunny_3.png",
            "deco_sprites/real_sugar_bear_1.png", "deco_sprites/real_sugar_bear_2.png", "deco_sprites/real_sugar_bear_3.png",
            "deco_sprites/real_gradient_bunny.png", "deco_sprites/real_sparkle_bunny.png",
            "deco_sprites/real_sea_1.png", "deco_sprites/real_sea_2.png", "deco_sprites/real_sea_3.png",
            "deco_sprites/real_sea_4.png", "deco_sprites/real_sea_5.png", "deco_sprites/real_sea_6.png",
            "deco_sprites/real_sea_7.png", "deco_sprites/real_sea_8.png", "deco_sprites/real_sea_9.png",
            "deco_sprites/real_sea_10.png", "deco_sprites/real_sea_11.png", "deco_sprites/real_sea_12.png",
            "deco_sprites/real_jelly_3.png", "deco_sprites/real_jelly_4.png", "deco_sprites/real_jelly_5.png",
            "deco_sprites/real_jelly_6.png", "deco_sprites/real_jelly_7.png", "deco_sprites/real_jelly_8.png"
        ];

        const loadedRealJellyImages = [];
        realJellySpritePaths.forEach(path => {
            const img = new Image();
            img.src = path;
            loadedRealJellyImages.push(img);
        });

        let decoJellies = [];

        function generateDecoJellies(baseHue) {
            decoJellies = [];
            const count = 26;
            for (let i = 0; i < count; i++) {
                let x = Math.random() * width;
                let y = Math.random() * height;

                // Varied realistic sizes (36px to 62px)
                const size = 36 + Math.random() * 26;
                const phase = Math.random() * Math.PI * 2;
                const angle = (Math.random() - 0.5) * Math.PI * 0.4;
                
                // Slow, gentle floating movement
                const vx = (Math.random() - 0.5) * 0.28;
                const vy = (Math.random() - 0.5) * 0.28;
                const vrot = (Math.random() - 0.5) * 0.003;

                const imgIndex = Math.floor(Math.random() * loadedRealJellyImages.length);
                
                decoJellies.push({ imgIndex, x, y, size, angle, phase, vx, vy, vrot });
            }
        }

        function drawDecoJellies() {
            let time = Date.now() * 0.002;
            decoJellies.forEach(d => {
                d.x += d.vx;
                d.y += d.vy;
                d.angle += d.vrot;

                const margin = d.size * 1.5;
                if (d.x < -margin) d.x = width + margin;
                if (d.x > width + margin) d.x = -margin;
                if (d.y < -margin) d.y = height + margin;
                if (d.y > height + margin) d.y = -margin;

                const dx = Math.sin(time * 0.8 + d.phase) * 5;
                const dy = Math.cos(time * 0.6 + d.phase * 1.5) * 5;
                const rot = d.angle + Math.sin(time * 0.5 + d.phase) * 0.08;

                const spriteImg = loadedRealJellyImages[d.imgIndex];
                if (spriteImg && spriteImg.complete && spriteImg.naturalWidth > 0) {
                    ctx.save();
                    ctx.translate(d.x + dx, d.y + dy);
                    ctx.rotate(rot);

                    // 3D Soft Drop Shadow
                    ctx.shadowColor = 'rgba(0, 0, 0, 0.24)';
                    ctx.shadowBlur = 10;
                    ctx.shadowOffsetY = 6;

                    const aspect = spriteImg.naturalWidth / spriteImg.naturalHeight;
                    let drawW = d.size;
                    let drawH = d.size / aspect;

                    ctx.drawImage(spriteImg, -drawW / 2, -drawH / 2, drawW, drawH);
                    ctx.restore();
                }
            });
        }
"""

start_marker = "// ==========================================================================\n        // REAL PHOTO-REALISTIC PRODUCT JELLY ENGINE"
if start_marker not in content:
    start_marker = "let decoJellies = [];"

idx1 = content.find(start_marker)
idx2 = content.find("function handleRecordToggle()", idx1)

if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + real_sprite_system.strip() + "\n\n        " + content[idx2:]
    print("100% Successfully integrated 32 real product jelly photo sprites into index.html!")
else:
    print(f"WARNING: Markers not found! idx1: {idx1}, idx2: {idx2}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Real Product Jelly Photo Sprites in index.html!")
