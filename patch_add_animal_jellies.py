with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update types in generateDecoJellies to include "rabbit", "cat", "dog"
old_types = """                const types = [
                    "strawberry", "strawberry", "apple", "apple", "grape", "grape",
                    "kiwi", "kiwi", "watermelon", "watermelon", "bear", "heart"
                ];"""

new_types = """                const types = [
                    "strawberry", "apple", "grape", "kiwi", "watermelon",
                    "bear", "heart", "rabbit", "cat", "dog"
                ];"""

if old_types in content:
    content = content.replace(old_types, new_types)

# 2. Rewrite draw3DGummyBear to fill each part independently so body has 100% SOLID interior with ZERO holes (누끼 구멍 100% 해결!)
old_bear_func = """        function draw3DGummyBear(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            applyGummyMotion(ctx, x, y, angle, time, phase);

            // 1. Dropshadow (3D ambient occlusion)
            ctx.shadowColor = 'rgba(0, 0, 0, 0.26)';
            ctx.shadowBlur = 14;
            ctx.shadowOffsetY = 11;

            // Define main silhouette path
            let bearPath = () => {
                ctx.beginPath();
                ctx.arc(0, -size * 0.12, size * 0.3, 0, Math.PI * 2);
                ctx.arc(-size * 0.24, -size * 0.36, size * 0.12, 0, Math.PI * 2);
                ctx.arc(size * 0.24, -size * 0.36, size * 0.12, 0, Math.PI * 2);
                ctx.ellipse(0, size * 0.25, size * 0.34, size * 0.42, 0, 0, Math.PI * 2);
                ctx.ellipse(-size * 0.32, size * 0.12, size * 0.12, size * 0.2, Math.PI / 6, 0, Math.PI * 2);
                ctx.ellipse(size * 0.32, size * 0.12, size * 0.12, size * 0.2, -Math.PI / 6, 0, Math.PI * 2);
                ctx.ellipse(-size * 0.24, size * 0.6, size * 0.15, size * 0.2, -Math.PI / 12, 0, Math.PI * 2);
                ctx.ellipse(size * 0.24, size * 0.6, size * 0.15, size * 0.2, Math.PI / 12, 0, Math.PI * 2);
                ctx.closePath();
            };

            bearPath();

            // 2. Translucent volumetric radial gradient (hot center glow to dark saturated border)
            let grad = ctx.createRadialGradient(-size * 0.12, -size * 0.12, size * 0.05, 0, size * 0.1, size * 0.72);
            grad.addColorStop(0, `hsla(${hue}, 100%, 82%, 0.98)`); // center core glow
            grad.addColorStop(0.6, `hsla(${hue}, 100%, 50%, 0.95)`); // syrup body
            grad.addColorStop(1, `hsla(${hue}, 100%, 24%, 1)`); // saturated rim
            ctx.fillStyle = grad;
            ctx.fill();"""

new_bear_func = """        function draw3DGummyBear(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            applyGummyMotion(ctx, x, y, angle, time, phase);

            // 1. Dropshadow (3D ambient occlusion)
            ctx.shadowColor = 'rgba(0, 0, 0, 0.26)';
            ctx.shadowBlur = 14;
            ctx.shadowOffsetY = 11;

            let grad = ctx.createRadialGradient(-size * 0.12, -size * 0.12, size * 0.05, 0, size * 0.1, size * 0.72);
            grad.addColorStop(0, `hsla(${hue}, 100%, 82%, 0.98)`);
            grad.addColorStop(0.6, `hsla(${hue}, 100%, 50%, 0.95)`);
            grad.addColorStop(1, `hsla(${hue}, 100%, 24%, 1)`);
            ctx.fillStyle = grad;

            // Fill each part independently to guarantee 100% SOLID interior without any holes
            let drawBearBodyParts = () => {
                ctx.beginPath(); ctx.ellipse(0, size * 0.25, size * 0.34, size * 0.42, 0, 0, Math.PI * 2); ctx.fill();
                ctx.beginPath(); ctx.arc(0, -size * 0.12, size * 0.3, 0, Math.PI * 2); ctx.fill();
                ctx.beginPath(); ctx.arc(-size * 0.24, -size * 0.36, size * 0.12, 0, Math.PI * 2); ctx.fill();
                ctx.beginPath(); ctx.arc(size * 0.24, -size * 0.36, size * 0.12, 0, Math.PI * 2); ctx.fill();
                ctx.beginPath(); ctx.ellipse(-size * 0.32, size * 0.12, size * 0.12, size * 0.2, Math.PI / 6, 0, Math.PI * 2); ctx.fill();
                ctx.beginPath(); ctx.ellipse(size * 0.32, size * 0.12, size * 0.12, size * 0.2, -Math.PI / 6, 0, Math.PI * 2); ctx.fill();
                ctx.beginPath(); ctx.ellipse(-size * 0.24, size * 0.6, size * 0.15, size * 0.2, -Math.PI / 12, 0, Math.PI * 2); ctx.fill();
                ctx.beginPath(); ctx.ellipse(size * 0.24, size * 0.6, size * 0.15, size * 0.2, Math.PI / 12, 0, Math.PI * 2); ctx.fill();
            };

            drawBearBodyParts();"""

if old_bear_func in content:
    content = content.replace(old_bear_func, new_bear_func)

# Fix bearPath calls inside draw3DGummyBear to use drawBearBodyParts
content = content.replace("bearPath();", "drawBearBodyParts();")

# 3. Add draw3DGummyRabbit, draw3DGummyCat, draw3DGummyDog functions & update drawDecoJellies switch case
new_animal_funcs = """
        function draw3DGummyRabbit(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            applyGummyMotion(ctx, x, y, angle, time, phase);

            ctx.shadowColor = 'rgba(0, 0, 0, 0.22)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 8;

            let grad = ctx.createRadialGradient(0, -size * 0.1, size * 0.05, 0, 0, size * 0.65);
            grad.addColorStop(0, `hsla(${hue}, 100%, 88%, 0.98)`);
            grad.addColorStop(0.6, `hsla(${hue}, 100%, 55%, 0.95)`);
            grad.addColorStop(1, `hsla(${hue}, 100%, 28%, 1)`);
            ctx.fillStyle = grad;

            // Rabbit ears
            ctx.beginPath(); ctx.ellipse(-size * 0.16, -size * 0.42, size * 0.11, size * 0.28, -Math.PI / 12, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(size * 0.16, -size * 0.42, size * 0.11, size * 0.28, Math.PI / 12, 0, Math.PI * 2); ctx.fill();
            // Rabbit body & head
            ctx.beginPath(); ctx.arc(0, size * 0.1, size * 0.38, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(0, -size * 0.1, size * 0.3, 0, Math.PI * 2); ctx.fill();

            // Inner ear highlights
            ctx.fillStyle = `hsla(${hue}, 100%, 92%, 0.7)`;
            ctx.beginPath(); ctx.ellipse(-size * 0.16, -size * 0.42, size * 0.05, size * 0.18, -Math.PI / 12, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(size * 0.16, -size * 0.42, size * 0.05, size * 0.18, Math.PI / 12, 0, Math.PI * 2); ctx.fill();

            // Specular highlights
            ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
            ctx.beginPath(); ctx.ellipse(-size * 0.08, -size * 0.18, size * 0.06, size * 0.03, Math.PI / 4, 0, Math.PI * 2); ctx.fill();
            ctx.restore();
        }

        function draw3DGummyCat(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            applyGummyMotion(ctx, x, y, angle, time, phase);

            ctx.shadowColor = 'rgba(0, 0, 0, 0.22)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 8;

            let grad = ctx.createRadialGradient(0, -size * 0.1, size * 0.05, 0, 0, size * 0.62);
            grad.addColorStop(0, `hsla(${hue}, 100%, 88%, 0.98)`);
            grad.addColorStop(0.6, `hsla(${hue}, 100%, 55%, 0.95)`);
            grad.addColorStop(1, `hsla(${hue}, 100%, 28%, 1)`);
            ctx.fillStyle = grad;

            // Cat ears (pointy triangles)
            ctx.beginPath();
            ctx.moveTo(-size * 0.3, -size * 0.05);
            ctx.lineTo(-size * 0.28, -size * 0.45);
            ctx.lineTo(-size * 0.05, -size * 0.2);
            ctx.closePath(); ctx.fill();

            ctx.beginPath();
            ctx.moveTo(size * 0.3, -size * 0.05);
            ctx.lineTo(size * 0.28, -size * 0.45);
            ctx.lineTo(size * 0.05, -size * 0.2);
            ctx.closePath(); ctx.fill();

            // Cat head & body
            ctx.beginPath(); ctx.arc(0, size * 0.12, size * 0.36, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(0, -size * 0.08, size * 0.32, 0, Math.PI * 2); ctx.fill();

            // Specular highlights
            ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
            ctx.beginPath(); ctx.ellipse(-size * 0.08, -size * 0.16, size * 0.06, size * 0.03, Math.PI / 4, 0, Math.PI * 2); ctx.fill();
            ctx.restore();
        }

        function draw3DGummyDog(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            applyGummyMotion(ctx, x, y, angle, time, phase);

            ctx.shadowColor = 'rgba(0, 0, 0, 0.22)';
            ctx.shadowBlur = 12;
            ctx.shadowOffsetY = 8;

            let grad = ctx.createRadialGradient(0, -size * 0.1, size * 0.05, 0, 0, size * 0.65);
            grad.addColorStop(0, `hsla(${hue}, 100%, 88%, 0.98)`);
            grad.addColorStop(0.6, `hsla(${hue}, 100%, 55%, 0.95)`);
            grad.addColorStop(1, `hsla(${hue}, 100%, 28%, 1)`);
            ctx.fillStyle = grad;

            // Dog floppy ears
            ctx.beginPath(); ctx.ellipse(-size * 0.32, -size * 0.05, size * 0.12, size * 0.24, Math.PI / 6, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(size * 0.32, -size * 0.05, size * 0.12, size * 0.24, -Math.PI / 6, 0, Math.PI * 2); ctx.fill();

            // Dog body & head
            ctx.beginPath(); ctx.arc(0, size * 0.15, size * 0.36, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(0, -size * 0.08, size * 0.3, 0, Math.PI * 2); ctx.fill();

            // Specular highlights
            ctx.fillStyle = 'rgba(255, 255, 255, 0.85)';
            ctx.beginPath(); ctx.ellipse(-size * 0.08, -size * 0.16, size * 0.06, size * 0.03, Math.PI / 4, 0, Math.PI * 2); ctx.fill();
            ctx.restore();
        }\n"""

old_draw_deco_switch = """                else if (j.type === "bear") {
                    draw3DGummyBear(ctx, j.x, j.y, j.size, j.hue, j.angle + angleWiggle, time, j.phase);
                }"""

new_draw_deco_switch = """                else if (j.type === "bear") {
                    draw3DGummyBear(ctx, j.x, j.y, j.size, j.hue, j.angle + angleWiggle, time, j.phase);
                } else if (j.type === "rabbit") {
                    draw3DGummyRabbit(ctx, j.x, j.y, j.size, j.hue, j.angle + angleWiggle, time, j.phase);
                } else if (j.type === "cat") {
                    draw3DGummyCat(ctx, j.x, j.y, j.size, j.hue, j.angle + angleWiggle, time, j.phase);
                } else if (j.type === "dog") {
                    draw3DGummyDog(ctx, j.x, j.y, j.size, j.hue, j.angle + angleWiggle, time, j.phase);
                }"""

if "function draw3DGummyRabbit" not in content:
    content = content.replace("function draw3DGummyBear", new_animal_funcs + "\n        function draw3DGummyBear")

if old_draw_deco_switch in content:
    content = content.replace(old_draw_deco_switch, new_draw_deco_switch)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% Solid Bear Jelly Fix & Added Rabbit, Cat, Dog 3D Floating Jellies in index.html!")
