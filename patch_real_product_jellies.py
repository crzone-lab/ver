import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

real_jelly_renderers = """
        // ==========================================================================
        // REAL PHOTO-REALISTIC PRODUCT JELLY ENGINE (Sugar Cubes, Glossy Bears, Glitter Bears)
        // ==========================================================================
        let decoJellies = [];

        function generateDecoJellies(baseHue) {
            decoJellies = [];
            const count = 28;
            for (let i = 0; i < count; i++) {
                let x = Math.random() * width;
                let y = Math.random() * height;

                const size = 32 + Math.random() * 22; 
                let hue = (baseHue - 45 + Math.random() * 90 + 360) % 360;

                const phase = Math.random() * Math.PI * 2;
                const angle = (Math.random() - 0.5) * Math.PI * 0.5;
                
                const vx = (Math.random() - 0.5) * 0.28;
                const vy = (Math.random() - 0.5) * 0.28;
                const vrot = (Math.random() - 0.5) * 0.004;

                // 3 Real Product Jelly Types: Sugar Cube, Glossy Translucent Haribo Bear, Glitter Star Bear
                const types = ["sugarcube", "sugarcube", "glossybear", "glossybear", "glitterbear"];
                const type = types[Math.floor(Math.random() * types.length)];
                
                let dust = [];
                if (type === "sugarcube") {
                    for (let s = 0; s < 24; s++) {
                        dust.push({ dx: (Math.random() - 0.5) * 0.85, dy: (Math.random() - 0.5) * 0.85, sz: 1 + Math.random() * 1.8 });
                    }
                } else if (type === "glitterbear") {
                    for (let g = 0; g < 10; g++) {
                        dust.push({ dx: (Math.random() - 0.5) * 0.6, dy: (Math.random() - 0.5) * 0.7, sz: 2 + Math.random() * 2.5, isStar: Math.random() > 0.5 });
                    }
                }
                
                decoJellies.push({ type, x, y, size, hue, angle, phase, vx, vy, vrot, dust });
            }
        }

        // 1. Photo-Realistic Sugar-Coated Cube Gummy (설탕 묻은 사각 큐브 젤리)
        function drawRealSugarCubeGummy(ctx, x, y, size, hue, angle, time, phase, dust) {
            ctx.save();
            ctx.translate(x, y);
            ctx.rotate(angle);

            ctx.shadowColor = 'rgba(0, 0, 0, 0.25)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 7;

            let s = size * 0.65;
            
            let grad = ctx.createLinearGradient(-s, -s, s, s);
            grad.addColorStop(0, `hsla(${hue}, 95%, 72%, 0.95)`);
            grad.addColorStop(0.5, `hsla(${hue}, 90%, 52%, 0.92)`);
            grad.addColorStop(1, `hsla(${hue}, 85%, 32%, 0.98)`);

            ctx.fillStyle = grad;
            ctx.beginPath();
            ctx.roundRect(-s, -s, s * 2, s * 2, 10);
            ctx.fill();

            ctx.shadowColor = 'transparent';
            ctx.fillStyle = 'rgba(255, 255, 255, 0.45)';
            ctx.beginPath();
            ctx.roundRect(-s * 0.85, -s * 0.85, s * 1.7, s * 0.6, 6);
            ctx.fill();

            if (dust) {
                ctx.fillStyle = 'rgba(255, 255, 255, 0.92)';
                dust.forEach(d => {
                    ctx.beginPath();
                    ctx.arc(d.dx * s, d.dy * s, d.sz, 0, Math.PI * 2);
                    ctx.fill();
                });
            }

            ctx.restore();
        }

        // 2. Photo-Realistic Translucent Glossy Gummy Bear (투명 하리보 곰젤리)
        function drawRealGlossyGummyBear(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            ctx.translate(x, y);
            ctx.rotate(angle);

            ctx.shadowColor = 'rgba(0, 0, 0, 0.22)';
            ctx.shadowBlur = 14;
            ctx.shadowOffsetY = 8;

            let r = size * 0.5;

            let grad = ctx.createRadialGradient(-r * 0.2, -r * 0.3, r * 0.1, 0, 0, r * 1.2);
            grad.addColorStop(0, `hsla(${hue}, 100%, 82%, 0.96)`);
            grad.addColorStop(0.6, `hsla(${hue}, 95%, 54%, 0.92)`);
            grad.addColorStop(1, `hsla(${hue}, 90%, 28%, 0.98)`);
            ctx.fillStyle = grad;

            ctx.beginPath(); ctx.arc(-r * 0.5, -r * 0.65, r * 0.28, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(r * 0.5, -r * 0.65, r * 0.28, 0, Math.PI * 2); ctx.fill();

            ctx.beginPath(); ctx.arc(0, -r * 0.3, r * 0.52, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(0, r * 0.32, r * 0.55, r * 0.62, 0, 0, Math.PI * 2); ctx.fill();

            ctx.fillStyle = `hsla(${hue}, 100%, 88%, 0.85)`;
            ctx.beginPath(); ctx.ellipse(0, -r * 0.22, r * 0.25, r * 0.18, 0, 0, Math.PI * 2); ctx.fill();

            ctx.shadowColor = 'transparent';
            ctx.fillStyle = 'rgba(255, 255, 255, 0.65)';
            ctx.beginPath(); ctx.ellipse(-r * 0.15, -r * 0.45, r * 0.2, r * 0.1, -0.3, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(-r * 0.22, r * 0.15, r * 0.15, r * 0.3, -0.2, 0, Math.PI * 2); ctx.fill();

            ctx.restore();
        }

        // 3. Sparkling Glitter Star Confetti Pastel Gummy Bear (글리터 별가루 파스텔 곰젤리)
        function drawRealGlitterSparkleGummyBear(ctx, x, y, size, hue, angle, time, phase, dust) {
            ctx.save();
            ctx.translate(x, y);
            ctx.rotate(angle);

            ctx.shadowColor = 'rgba(0, 0, 0, 0.18)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 6;

            let r = size * 0.48;

            let grad = ctx.createRadialGradient(-r * 0.2, -r * 0.3, r * 0.1, 0, 0, r * 1.2);
            grad.addColorStop(0, `hsla(${hue}, 80%, 90%, 0.95)`);
            grad.addColorStop(0.65, `hsla(${hue}, 75%, 68%, 0.88)`);
            grad.addColorStop(1, `hsla(${hue}, 70%, 45%, 0.92)`);
            ctx.fillStyle = grad;

            ctx.beginPath(); ctx.arc(-r * 0.5, -r * 0.62, r * 0.26, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(r * 0.5, -r * 0.62, r * 0.26, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(0, -r * 0.28, r * 0.5, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(0, r * 0.32, r * 0.52, r * 0.6, 0, 0, Math.PI * 2); ctx.fill();

            ctx.shadowColor = 'transparent';
            if (dust) {
                dust.forEach(d => {
                    ctx.fillStyle = d.isStar ? 'rgba(255, 255, 255, 0.95)' : `hsla(${(hue + 120) % 360}, 90%, 75%, 0.85)`;
                    ctx.beginPath();
                    ctx.arc(d.dx * r, d.dy * r, d.sz, 0, Math.PI * 2);
                    ctx.fill();
                });
            }

            ctx.restore();
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

                if (d.type === "sugarcube") {
                    drawRealSugarCubeGummy(ctx, d.x + dx, d.y + dy, d.size, d.hue, rot, time, d.phase, d.dust);
                } else if (d.type === "glitterbear") {
                    drawRealGlitterSparkleGummyBear(ctx, d.x + dx, d.y + dy, d.size, d.hue, rot, time, d.phase, d.dust);
                } else {
                    drawRealGlossyGummyBear(ctx, d.x + dx, d.y + dy, d.size, d.hue, rot, time, d.phase);
                }
            });
        }
"""

start_marker = "// Volumetric 3D Gummy shapes definitions"
end_marker = "function drawDecoJellies()"

if start_marker in content:
    idx1 = content.find(start_marker)
    idx2 = content.find("function handleRecordToggle()", idx1)
    if idx1 != -1 and idx2 != -1:
        content = content[:idx1] + real_jelly_renderers.strip() + "\n\n        " + content[idx2:]
        print("100% Successfully replaced old 2D cartoon deco jellies with Real Product Jellies!")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied Real Product Jellies update in index.html!")
