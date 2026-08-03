import base64, glob, os
from PIL import Image
import numpy as np

files = sorted(glob.glob('deco_sprites/real_jelly_candy_*.png'))
valid_candy_paths = []

for f in files:
    img = Image.open(f).convert('RGBA')
    w, h = img.size
    arr = np.array(img)
    alpha = arr[:,:,3]
    transparent_pixels = np.sum(alpha == 0)
    total_pixels = w * h
    trans_ratio = transparent_pixels / total_pixels
    
    r, g, b = arr[:,:,0], arr[:,:,1], arr[:,:,2]
    pink_mask = (r > 220) & (g < 140) & (b > 130) & (alpha > 0)
    pink_ratio = np.sum(pink_mask) / (total_pixels - transparent_pixels + 1)
    
    # Select only genuine real gummy candies (transparency > 0.2, pink ratio < 0.25, height > 35, width > 35)
    if pink_ratio < 0.25 and trans_ratio > 0.2 and h > 35 and w > 35:
        valid_candy_paths.append(f)

print(f"Filtered {len(valid_candy_paths)} 100% PURE REAL GUMMY CANDY SPRITES!")

base64_data_uris = []
for p in valid_candy_paths:
    with open(p, 'rb') as f:
        encoded = base64.b64encode(f.read()).decode('utf-8')
        data_uri = f"data:image/png;base64,{encoded}"
        base64_data_uris.append(data_uri)
        print(f"Encoded {os.path.basename(p)} ({len(data_uri)} chars)")

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

start_marker = "// ==========================================================================\n        // 100% USER'S EXACT 5 UPLOADED JELLY PHOTO SPRITES ENGINE"
if start_marker not in content:
    start_marker = "// =========================================================================="

idx1 = content.find(start_marker)
idx2 = content.find("function handleRecordToggle()", idx1)

if idx1 != -1 and idx2 != -1:
    content = content[:idx1] + clean_sprite_engine.strip() + "\n\n        " + content[idx2:]
    print("100% Successfully embedded 100% pure real gummy candy photo sprites into index.html!")
else:
    print(f"WARNING: Markers not found! idx1: {idx1}, idx2: {idx2}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% Pure Real Gummy Photo Sprites in index.html!")
