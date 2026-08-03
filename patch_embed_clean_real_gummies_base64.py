import base64, glob, os

# Only select the 100% pure real gummy candy photo sprites
target_files = [
    "deco_sprites/real_bunny_1.png",
    "deco_sprites/real_bunny_2.png",
    "deco_sprites/real_bunny_3.png",
    "deco_sprites/real_sugar_bear_1.png",
    "deco_sprites/real_sugar_bear_2.png",
    "deco_sprites/real_sugar_bear_3.png",
    "deco_sprites/real_gradient_bunny.png",
    "deco_sprites/real_sparkle_bunny.png"
]

base64_data_uris = []
for tf in target_files:
    if os.path.exists(tf):
        with open(tf, 'rb') as f:
            encoded = base64.b64encode(f.read()).decode('utf-8')
            data_uri = f"data:image/png;base64,{encoded}"
            base64_data_uris.append(data_uri)
            print(f"Encoded {tf} ({len(data_uri)} chars)")

print(f"Total base64 clean real gummy sprites: {len(base64_data_uris)}")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Generate JS inline array of Base64 Data URIs
js_array_items = ',\n            '.join([f'"{uri}"' for uri in base64_data_uris])

clean_sprite_engine = f"""
        // ==========================================================================
        // 100% CLEAN REAL PRODUCT GUMMY PHOTO SPRITE ENGINE (BASE64 EMBEDDED)
        // ==========================================================================
        const realJellyDataUris = [
            {js_array_items}
        ];

        const loadedRealJellyImages = [];
        realJellyDataUris.forEach(uri => {{
            const img = new Image();
            img.src = uri;
            loadedRealJellyImages.push(img);
        }});

        let decoJellies = [];

        function generateDecoJellies(baseHue) {{
            decoJellies = [];
            const count = 22;
            for (let i = 0; i < count; i++) {{
                let x = Math.random() * width;
                let y = Math.random() * height;

                const size = 42 + Math.random() * 24;
                const phase = Math.random() * Math.PI * 2;
                const angle = (Math.random() - 0.5) * Math.PI * 0.4;
                
                const vx = (Math.random() - 0.5) * 0.25;
                const vy = (Math.random() - 0.5) * 0.25;
                const vrot = (Math.random() - 0.5) * 0.003;

                const imgIndex = Math.floor(Math.random() * loadedRealJellyImages.length);
                
                decoJellies.push({{ imgIndex, x, y, size, angle, phase, vx, vy, vrot }});
            }}
        }}

        function drawDecoJellies() {{
            let time = Date.now() * 0.002;
            decoJellies.forEach(d => {{
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
                if (spriteImg && spriteImg.complete && spriteImg.naturalWidth > 0) {{
                    ctx.save();
                    ctx.translate(d.x + dx, d.y + dy);
                    ctx.rotate(rot);

                    ctx.shadowColor = 'rgba(0, 0, 0, 0.25)';
                    ctx.shadowBlur = 10;
                    ctx.shadowOffsetY = 6;

                    const aspect = spriteImg.naturalWidth / spriteImg.naturalHeight;
                    let drawW = d.size;
                    let drawH = d.size / aspect;

                    ctx.drawImage(spriteImg, -drawW / 2, -drawH / 2, drawW, drawH);
                    ctx.restore();
                }}
            }});
        }}
"""

# Replace in content
start_marker = "// ==========================================================================\n        // 100% REAL PRODUCT JELLY PHOTO SPRITE ENGINE"
if start_marker not in content:
    start_marker = "const realJellySpritePaths = ["

idx1 = content.find(start_marker)
idx2 = content.find("function handleRecordToggle()", idx1)

if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + clean_sprite_engine.strip() + "\n\n        " + content[idx2:]
    print("100% Successfully embedded clean base64 real gummy photo sprites into index.html!")
else:
    print(f"WARNING: Markers not found! idx1: {idx1}, idx2: {idx2}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Clean Base64 Embedded Real Gummies in index.html!")
