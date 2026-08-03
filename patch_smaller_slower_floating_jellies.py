with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update generateDecoJellies and drawDecoJellies for smaller size (0.10 ~ 0.22 scale) and ultra-slow relaxing drift (vx, vy = 0.18 max)
old_floating_code = """        function generateDecoJellies() {
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
        }"""

new_floating_code = """        function generateDecoJellies() {
            decoJellies = [];
            let stageW = width || 388;
            let stageH = height || 800;
            let count = 10; // 10 small, slow floating background jellies

            for (let i = 0; i < count; i++) {
                let imgIdx = Math.floor(Math.random() * TOTAL_DECO_SPRITES);
                decoJellies.push({
                    imgIndex: imgIdx,
                    x: Math.random() * stageW,
                    y: Math.random() * stageH,
                    vx: (Math.random() - 0.5) * 0.18, // Ultra-slow relaxing drift
                    vy: (Math.random() - 0.5) * 0.18,
                    scale: 0.10 + Math.random() * 0.12, // Small, elegant size
                    angle: Math.random() * Math.PI * 2,
                    vRot: (Math.random() - 0.5) * 0.004,
                    bobOffset: Math.random() * Math.PI * 2
                });
            }
        }"""

if old_floating_code in content:
    content = content.replace(old_floating_code, new_floating_code)
    print("100% Successfully updated generateDecoJellies for smaller size & slower speed!")

# Update bobbing motion speed in drawDecoJellies
old_bobbing = "j.y += j.vy + Math.sin(time + j.bobOffset) * 0.22;"
new_bobbing = "j.y += j.vy + Math.sin(time + j.bobOffset) * 0.08;"

if old_bobbing in content:
    content = content.replace(old_bobbing, new_bobbing)
    print("100% Successfully updated bobbing speed in drawDecoJellies!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Smaller & Slower Floating Jellies in index.html!")
