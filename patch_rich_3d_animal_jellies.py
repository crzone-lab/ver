with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update types array in generateDecoJellies so rabbit, cat, dog appear frequently
old_types = """                const types = [
                    "strawberry", "apple", "grape", "kiwi", "watermelon",
                    "bear", "heart", "rabbit", "cat", "dog"
                ];"""

new_types = """                const types = [
                    "rabbit", "rabbit", "cat", "cat", "dog", "dog",
                    "bear", "bear", "strawberry", "apple", "grape", "heart"
                ];"""

if old_types in content:
    content = content.replace(old_types, new_types)

# 2. Rewrite draw3DGummyCat, draw3DGummyRabbit, draw3DGummyDog with full 3D volumetric features (eyes, nose, snout, whiskers, speculars)
new_animal_funcs = """        function draw3DGummyCat(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            applyGummyMotion(ctx, x, y, angle, time, phase);

            // 1. 3D Ambient Occlusion Dropshadow
            ctx.shadowColor = 'rgba(0, 0, 0, 0.24)';
            ctx.shadowBlur = 14;
            ctx.shadowOffsetY = 9;

            // 2. Volumetric 3D Radial Gradient
            let grad = ctx.createRadialGradient(-size * 0.1, -size * 0.1, size * 0.05, 0, 0, size * 0.65);
            grad.addColorStop(0, `hsla(${hue}, 100%, 86%, 0.98)`);
            grad.addColorStop(0.65, `hsla(${hue}, 100%, 52%, 0.95)`);
            grad.addColorStop(1, `hsla(${hue}, 100%, 24%, 1)`);
            ctx.fillStyle = grad;

            // Pointy Cat Ears
            ctx.beginPath();
            ctx.moveTo(-size * 0.35, -size * 0.05);
            ctx.lineTo(-size * 0.28, -size * 0.48);
            ctx.lineTo(-size * 0.05, -size * 0.22);
            ctx.closePath(); ctx.fill();

            ctx.beginPath();
            ctx.moveTo(size * 0.35, -size * 0.05);
            ctx.lineTo(size * 0.28, -size * 0.48);
            ctx.lineTo(size * 0.05, -size * 0.22);
            ctx.closePath(); ctx.fill();

            // Cat Head & Body
            ctx.beginPath(); ctx.arc(0, size * 0.15, size * 0.36, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(0, -size * 0.08, size * 0.32, 0, Math.PI * 2); ctx.fill();

            // Disable shadow for facial details
            ctx.shadowColor = 'transparent';

            // Inner Ear Pink Highlights
            ctx.fillStyle = `hsla(${hue}, 100%, 90%, 0.7)`;
            ctx.beginPath();
            ctx.moveTo(-size * 0.28, -size * 0.08);
            ctx.lineTo(-size * 0.24, -size * 0.38);
            ctx.lineTo(-size * 0.08, -size * 0.2);
            ctx.closePath(); ctx.fill();

            ctx.beginPath();
            ctx.moveTo(size * 0.28, -size * 0.08);
            ctx.lineTo(size * 0.24, -size * 0.38);
            ctx.lineTo(size * 0.08, -size * 0.2);
            ctx.closePath(); ctx.fill();

            // 3D Cute Cat Snout
            ctx.beginPath();
            ctx.ellipse(0, -size * 0.06, size * 0.13, size * 0.09, 0, 0, Math.PI * 2);
            let snoutGrad = ctx.createLinearGradient(0, -size * 0.12, 0, 0);
            snoutGrad.addColorStop(0, `hsla(${hue}, 100%, 94%, 0.95)`);
            snoutGrad.addColorStop(1, `hsla(${hue}, 90%, 55%, 0.95)`);
            ctx.fillStyle = snoutGrad;
            ctx.fill();

            // Nose
            ctx.beginPath();
            ctx.ellipse(0, -size * 0.09, size * 0.04, size * 0.025, 0, 0, Math.PI * 2);
            ctx.fillStyle = `hsla(${hue}, 100%, 18%, 0.85)`;
            ctx.fill();

            // Eyes
            ctx.fillStyle = `hsla(${hue}, 100%, 16%, 0.82)`;
            ctx.beginPath();
            ctx.arc(-size * 0.12, -size * 0.14, size * 0.035, 0, Math.PI * 2);
            ctx.arc(size * 0.12, -size * 0.14, size * 0.035, 0, Math.PI * 2);
            ctx.fill();

            // Whiskers
            ctx.strokeStyle = `hsla(${hue}, 100%, 20%, 0.55)`;
            ctx.lineWidth = size * 0.03;
            // Left whiskers
            ctx.beginPath(); ctx.moveTo(-size * 0.1, -size * 0.04); ctx.lineTo(-size * 0.36, -size * 0.08); ctx.stroke();
            ctx.beginPath(); ctx.moveTo(-size * 0.1, -size * 0.01); ctx.lineTo(-size * 0.34, size * 0.05); ctx.stroke();
            // Right whiskers
            ctx.beginPath(); ctx.moveTo(size * 0.1, -size * 0.04); ctx.lineTo(size * 0.36, -size * 0.08); ctx.stroke();
            ctx.beginPath(); ctx.moveTo(size * 0.1, -size * 0.01); ctx.lineTo(size * 0.34, size * 0.05); ctx.stroke();

            // Specular Glossy Reflections
            ctx.fillStyle = 'rgba(255, 255, 255, 0.88)';
            ctx.beginPath();
            ctx.ellipse(-size * 0.08, -size * 0.22, size * 0.07, size * 0.035, Math.PI / 4, 0, Math.PI * 2);
            ctx.fill();

            ctx.restore();
        }

        function draw3DGummyRabbit(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            applyGummyMotion(ctx, x, y, angle, time, phase);

            ctx.shadowColor = 'rgba(0, 0, 0, 0.24)';
            ctx.shadowBlur = 14;
            ctx.shadowOffsetY = 9;

            let grad = ctx.createRadialGradient(0, -size * 0.1, size * 0.05, 0, 0, size * 0.68);
            grad.addColorStop(0, `hsla(${hue}, 100%, 88%, 0.98)`);
            grad.addColorStop(0.65, `hsla(${hue}, 100%, 55%, 0.95)`);
            grad.addColorStop(1, `hsla(${hue}, 100%, 26%, 1)`);
            ctx.fillStyle = grad;

            // Rabbit ears
            ctx.beginPath(); ctx.ellipse(-size * 0.16, -size * 0.44, size * 0.12, size * 0.32, -Math.PI / 12, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(size * 0.16, -size * 0.44, size * 0.12, size * 0.32, Math.PI / 12, 0, Math.PI * 2); ctx.fill();
            // Rabbit body & head
            ctx.beginPath(); ctx.arc(0, size * 0.14, size * 0.38, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(0, -size * 0.08, size * 0.32, 0, Math.PI * 2); ctx.fill();

            ctx.shadowColor = 'transparent';

            // Inner ear highlights
            ctx.fillStyle = `hsla(${hue}, 100%, 92%, 0.7)`;
            ctx.beginPath(); ctx.ellipse(-size * 0.16, -size * 0.44, size * 0.05, size * 0.22, -Math.PI / 12, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(size * 0.16, -size * 0.44, size * 0.05, size * 0.22, Math.PI / 12, 0, Math.PI * 2); ctx.fill();

            // Eyes
            ctx.fillStyle = `hsla(${hue}, 100%, 16%, 0.82)`;
            ctx.beginPath();
            ctx.arc(-size * 0.11, -size * 0.12, size * 0.035, 0, Math.PI * 2);
            ctx.arc(size * 0.11, -size * 0.12, size * 0.035, 0, Math.PI * 2);
            ctx.fill();

            // Nose
            ctx.fillStyle = `hsla(${hue}, 100%, 22%, 0.85)`;
            ctx.beginPath();
            ctx.ellipse(0, -size * 0.06, size * 0.035, size * 0.025, 0, 0, Math.PI * 2);
            ctx.fill();

            // Specular highlights
            ctx.fillStyle = 'rgba(255, 255, 255, 0.88)';
            ctx.beginPath(); ctx.ellipse(-size * 0.08, -size * 0.2, size * 0.07, size * 0.035, Math.PI / 4, 0, Math.PI * 2); ctx.fill();
            ctx.restore();
        }

        function draw3DGummyDog(ctx, x, y, size, hue, angle, time, phase) {
            ctx.save();
            applyGummyMotion(ctx, x, y, angle, time, phase);

            ctx.shadowColor = 'rgba(0, 0, 0, 0.24)';
            ctx.shadowBlur = 14;
            ctx.shadowOffsetY = 9;

            let grad = ctx.createRadialGradient(0, -size * 0.1, size * 0.05, 0, 0, size * 0.68);
            grad.addColorStop(0, `hsla(${hue}, 100%, 88%, 0.98)`);
            grad.addColorStop(0.65, `hsla(${hue}, 100%, 55%, 0.95)`);
            grad.addColorStop(1, `hsla(${hue}, 100%, 26%, 1)`);
            ctx.fillStyle = grad;

            // Dog floppy ears
            ctx.beginPath(); ctx.ellipse(-size * 0.34, -size * 0.04, size * 0.14, size * 0.28, Math.PI / 6, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.ellipse(size * 0.34, -size * 0.04, size * 0.14, size * 0.28, -Math.PI / 6, 0, Math.PI * 2); ctx.fill();

            // Dog body & head
            ctx.beginPath(); ctx.arc(0, size * 0.16, size * 0.38, 0, Math.PI * 2); ctx.fill();
            ctx.beginPath(); ctx.arc(0, -size * 0.08, size * 0.32, 0, Math.PI * 2); ctx.fill();

            ctx.shadowColor = 'transparent';

            // Snout
            ctx.beginPath();
            ctx.ellipse(0, -size * 0.04, size * 0.14, size * 0.1, 0, 0, Math.PI * 2);
            let snoutGrad = ctx.createLinearGradient(0, -size * 0.1, 0, 0);
            snoutGrad.addColorStop(0, `hsla(${hue}, 100%, 94%, 0.95)`);
            snoutGrad.addColorStop(1, `hsla(${hue}, 90%, 55%, 0.95)`);
            ctx.fillStyle = snoutGrad;
            ctx.fill();

            // Nose
            ctx.fillStyle = `hsla(${hue}, 100%, 16%, 0.85)`;
            ctx.beginPath();
            ctx.ellipse(0, -size * 0.07, size * 0.045, size * 0.03, 0, 0, Math.PI * 2);
            ctx.fill();

            // Eyes
            ctx.fillStyle = `hsla(${hue}, 100%, 16%, 0.82)`;
            ctx.beginPath();
            ctx.arc(-size * 0.12, -size * 0.14, size * 0.035, 0, Math.PI * 2);
            ctx.arc(size * 0.12, -size * 0.14, size * 0.035, 0, Math.PI * 2);
            ctx.fill();

            // Specular highlights
            ctx.fillStyle = 'rgba(255, 255, 255, 0.88)';
            ctx.beginPath(); ctx.ellipse(-size * 0.08, -size * 0.2, size * 0.07, size * 0.035, Math.PI / 4, 0, Math.PI * 2); ctx.fill();
            ctx.restore();
        }"""

# Replace any existing draw3DGummyRabbit, draw3DGummyCat, draw3DGummyDog definitions
import re
content = re.sub(r'function draw3DGummyRabbit.*?(?=function draw3DGummyBear)', new_animal_funcs + '\n', content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Applied 100% Rich 3D Animal Jellies (Rabbit, Cat with Eyes/Nose/Whiskers, Dog) in index.html!")
