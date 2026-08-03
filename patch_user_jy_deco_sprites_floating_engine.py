with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update loadDecoJellySprites, generateDecoJellies, and drawDecoJellies to load all 19 jy-*.png files without ANY image processing
new_deco_engine = """        // ==========================================================================
        // 100% UNTOUCHED USER DECO JELLIES FLOATING STAGE ENGINE (jy-01 ~ jy-19)
        // ==========================================================================
        let decoJellyImages = [];
        let decoJellies = [];
        const DECO_FILE_NAMES = [
            'jy-01.png', 'jy-02.png', 'jy-03.png', 'jy-04.png', 'jy-05.png',
            'jy-06.png', 'jy-07.png', 'jy-08.png', 'jy-09.png', 'jy-10.png',
            'jy-11.png', 'jy-12.png', 'jy-13.png', 'jy-14.png', 'jy-15.png',
            'jy-16.png', 'jy-17.png', 'jy-18.png', 'jy-19.png'
        ];

        function loadDecoJellySprites() {
            decoJellyImages = [];
            for (let i = 0; i < DECO_FILE_NAMES.length; i++) {
                let img = new Image();
                img.src = `deco_sprites/${DECO_FILE_NAMES[i]}`;
                decoJellyImages.push(img);
            }
        }
        loadDecoJellySprites();

        function generateDecoJellies() {
            decoJellies = [];
            let stageW = width || 388;
            let stageH = height || 800;

            for (let i = 0; i < DECO_FILE_NAMES.length; i++) {
                decoJellies.push({
                    imgIndex: i,
                    x: Math.random() * stageW,
                    y: Math.random() * stageH,
                    vx: (Math.random() - 0.5) * 0.15, // Ultra-slow relaxing drift
                    vy: (Math.random() - 0.5) * 0.15,
                    scale: 0.12 + Math.random() * 0.32, // Diverse sizes (small to large)
                    angle: Math.random() * Math.PI * 2,
                    vRot: (Math.random() - 0.5) * 0.005,
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
            let time = Date.now() * 0.0015;

            for (let i = 0; i < decoJellies.length; i++) {
                let j = decoJellies[i];
                let img = decoJellyImages[j.imgIndex];

                // Slow random floating drift
                j.x += j.vx;
                j.y += j.vy + Math.sin(time + j.bobOffset) * 0.12;
                j.angle += j.vRot;

                // Infinite wrap-around
                if (j.x < -60) j.x = stageW + 60;
                if (j.x > stageW + 60) j.x = -60;
                if (j.y < -60) j.y = stageH + 60;
                if (j.y > stageH + 60) j.y = -60;

                if (img && img.complete && img.naturalWidth > 0) {
                    ctx.save();
                    ctx.translate(j.x, j.y);
                    ctx.rotate(j.angle);
                    ctx.scale(j.scale, j.scale);
                    ctx.globalAlpha = 0.88;

                    // Soft ambient shadow
                    ctx.fillStyle = 'rgba(0, 0, 0, 0.10)';
                    ctx.beginPath();
                    ctx.ellipse(0, 45, 45, 15, 0, 0, Math.PI * 2);
                    ctx.fill();

                    // Render untouched user original jelly image
                    ctx.drawImage(img, -img.naturalWidth / 2, -img.naturalHeight / 2);
                    ctx.restore();
                }
            }
        }"""

# Find existing drawDecoJellies or deco engine block in index.html
idx = content.find('function loadDecoJellySprites()')
if idx == -1:
    idx = content.find('function drawDecoJellies()')

if idx != -1:
    # find end of drawDecoJellies
    brace_count = 0
    start_brace = content.find('{', content.find('function drawDecoJellies()'))
    end_idx = start_brace
    for p in range(start_brace, len(content)):
        if content[p] == '{': brace_count += 1
        elif content[p] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_idx = p + 1
                break
    content = content[:idx] + new_deco_engine + content[end_idx:]
    print("100% Successfully updated index.html with new User JY Deco Jellies Engine!")
else:
    print("WARNING: Could not locate drawDecoJellies function!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied User JY Deco Jellies Engine in index.html!")
