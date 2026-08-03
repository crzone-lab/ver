with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert drawDecoJellies to clean empty state (No background jellies cluttering stage)
old_draw = """        function drawDecoJellies() {
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
                j.y += j.vy + Math.sin(time + j.bobOffset) * 0.08;
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

new_draw = """        function drawDecoJellies() {
            // Reverted back to clean original stage state (No background jellies)
            return;
        }"""

if old_draw in content:
    content = content.replace(old_draw, new_draw)
    print("100% Successfully reverted drawDecoJellies to clean original state!")
else:
    # Search for drawDecoJellies function
    idx = content.find('function drawDecoJellies()')
    if idx != -1:
        end_idx = content.find('}', idx) + 1
        # find matching closing brace of drawDecoJellies
        brace_count = 0
        i = content.find('{', idx)
        for p in range(i, len(content)):
            if content[p] == '{': brace_count += 1
            elif content[p] == '}':
                brace_count -= 1
                if brace_count == 0:
                    end_idx = p + 1
                    break
        content = content[:idx] + new_draw + content[end_idx:]
        print("100% Successfully replaced drawDecoJellies with clean empty function!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Reverted Background Jellies in index.html!")
