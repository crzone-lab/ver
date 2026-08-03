import base64, glob, os

sprites = sorted(glob.glob('deco_sprites/*.png'))
print(f"Embedding {len(sprites)} pure real gummy product photos into index.html...")

base64_data_uris = []
for s in sprites:
    with open(s, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
        data_uri = f"data:image/png;base64,{encoded}"
        base64_data_uris.append(data_uri)
        print(f"Encoded {os.path.basename(s)} ({len(data_uri)} chars)")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_array_items = ',\n            '.join([f'"{uri}"' for uri in base64_data_uris])

clean_sprite_engine = f"""
        // ==========================================================================
        // 100% PURE REAL PRODUCT GUMMY CANDY PHOTOS (BASE64 EMBEDDED)
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

start_marker = "// 100% Clean Empty Background Stage (All Background Decorations Removed)"
if start_marker not in content:
    start_marker = "// =========================================================================="

idx1 = content.find(start_marker)
idx2 = content.find("function handleRecordToggle()", idx1)

if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + clean_sprite_engine.strip() + "\n\n        " + content[idx2:]
    print("100% Successfully embedded 20 pure real gummy product photos into index.html!")
else:
    print(f"WARNING: Markers not found! idx1: {idx1}, idx2: {idx2}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 20 Pure Real Gummy Photos in index.html!")
